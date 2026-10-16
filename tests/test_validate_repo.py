import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / 'scripts/validate_repo.py'


class ValidationTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.write('skills/sample/SKILL.md', '---\nname: sample\ndescription: Review supplied evidence.\nlicense: MIT\n---\n# Sample\n[Method](references/method.md)\n')
        self.write('skills/sample/references/method.md', '# Method\n')
        self.write('skills/sample/LICENSE', 'MIT License\n')
        self.write('skills/sample/agents/openai.yaml', 'interface:\n  display_name: Sample\n  short_description: Review evidence\n')
        self.put('skills/sample/evals/evals.json', [{'id': 'normal', 'prompt': 'Review.', 'expected_output': 'Bound conclusions.', 'files': []}])
        self.put('catalog/skills.json', {'version': '0.1.0', 'skills': [{'name': 'sample', 'path': 'skills/sample', 'invocation': 'automatic', 'sources': ['origin'], 'status': 'preview'}]})
        self.put('catalog/sources.json', {'sources': [{'id': 'origin', 'role': 'test fixture'}]})
        self.put('.claude-plugin/plugin.json', {'name': 'liyuk-skills', 'version': '0.1.0', 'skills': ['./skills/sample']})
        self.put('.claude-plugin/marketplace.json', {'name': 'liyuk', 'owner': {'name': 'Liyuk'}, 'plugins': [{'name': 'liyuk-skills', 'source': './'}]})
        self.write('README.md', '[English README](README.en.md)\n[sample](skills/sample/SKILL.md)\n')
        self.write('README.en.md', '[Chinese](README.md)\n')

    def write(self, name, text):
        p = self.root / name
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text)

    def put(self, name, value):
        self.write(name, json.dumps(value))

    def check(self):
        self.assertTrue(SCRIPT.is_file(), 'validator has not been implemented')
        spec = importlib.util.spec_from_file_location('validator', SCRIPT)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module.validate(self.root)

    def test_self_contained_package_passes(self):
        self.assertEqual([], self.check())

    def test_missing_reference_is_reported(self):
        (self.root / 'skills/sample/references/method.md').unlink()
        self.assertTrue(any('missing' in e for e in self.check()))

    def test_existing_reference_outside_package_is_rejected(self):
        self.write('shared.md', '# Shared')
        self.write('skills/sample/references/method.md', '[Shared](../../../shared.md)')
        self.assertTrue(any('outside' in e for e in self.check()))

    def test_symlink_reference_escape_is_rejected(self):
        self.write('shared.md', '# Shared')
        p = self.root / 'skills/sample/references/method.md'
        p.unlink()
        p.symlink_to(self.root / 'shared.md')
        self.assertTrue(any('outside' in e for e in self.check()))

    def test_wrong_name_is_rejected(self):
        p = self.root / 'skills/sample/SKILL.md'
        p.write_text(p.read_text().replace('name: sample', 'name: another'))
        self.assertTrue(any('name' in e for e in self.check()))

    def test_explicit_mode_requires_both_client_policies(self):
        p = self.root / 'catalog/skills.json'
        data = json.loads(p.read_text()); data['skills'][0]['invocation'] = 'explicit'; self.put('catalog/skills.json', data)
        self.assertTrue(any('invocation' in e for e in self.check()))

    def test_plugin_inventory_drift_is_rejected(self):
        self.put('.claude-plugin/plugin.json', {'name': 'liyuk-skills', 'version': '0.1.0', 'skills': []})
        self.assertTrue(any('plugin skills' in e for e in self.check()))

    def test_duplicate_eval_ids_are_rejected(self):
        case = {'id': 'same', 'prompt': 'Review', 'expected_output': 'Review', 'files': []}
        self.put('skills/sample/evals/evals.json', [case, case])
        self.assertTrue(any('duplicate' in e for e in self.check()))

    def test_unknown_source_is_rejected(self):
        self.put('catalog/sources.json', {'sources': []})
        self.assertTrue(any('source' in e for e in self.check()))

    def test_wrong_json_shape_returns_diagnostic(self):
        self.put('catalog/skills.json', {'skills': 'not-a-list'})
        self.assertTrue(self.check())

    def test_missing_eval_field_returns_diagnostic(self):
        self.put('skills/sample/evals/evals.json', [{'id': 'incomplete'}])
        self.assertTrue(any('eval' in e for e in self.check()))

    def test_wrong_source_files_shape_returns_diagnostic(self):
        for files in [None, 42, 'not-a-list']:
            with self.subTest(files=files):
                self.put('catalog/sources.json', {'sources': [{'id': 'origin', 'files': files}]})
                self.assertTrue(any('source' in e for e in self.check()))

    def test_duplicate_yaml_key_is_rejected(self):
        p = self.root / 'skills/sample/SKILL.md'
        p.write_text(p.read_text().replace('name: sample', 'name: sample\nname: sample'))
        self.assertTrue(any('duplicate' in e for e in self.check()))

    def test_task_flow_with_unknown_hyphenated_skill_is_rejected(self):
        self.write('skills/ask-liyuk/references/task-flows.md', '先用`ghost-skill`，再接`sample`。\n')
        self.assertTrue(any('task-flows' in e and 'ghost-skill' in e for e in self.check()))

    def test_task_flow_with_only_known_skills_passes(self):
        self.put('catalog/skills.json', {'version': '0.1.0', 'skills': [{'name': 'sample', 'path': 'skills/sample', 'invocation': 'automatic', 'sources': ['origin'], 'status': 'preview'}]})
        self.write('skills/ask-liyuk/references/task-flows.md', '先用`sample`。\n')
        self.assertEqual([], self.check())

    def test_task_flow_prose_is_not_a_skill_reference(self):
        self.write('skills/ask-liyuk/references/task-flows.md', 'source-backed / 1-on-1 是说明文字。先用`sample`。\n')
        self.assertEqual([], self.check())

    def test_task_flow_unknown_single_word_and_numeric_names_rejected(self):
        self.write('skills/ask-liyuk/references/task-flows.md', '先用`missing`，再用`stage-2`。\n')
        errors = self.check()
        for name in ['missing', 'stage-2']:
            self.assertTrue(any('task-flows' in e and name in e for e in errors))

    def test_description_must_name_boundary_neighbor(self):
        self.write('skills/other/SKILL.md', '---\nname: other\ndescription: Handle the other task.\nlicense: MIT\n---\n# Other\n')
        self.write('skills/other/LICENSE', 'MIT License\n')
        self.write('skills/other/agents/openai.yaml', 'interface:\n  display_name: Other\n  short_description: Other task\n')
        self.put('skills/other/evals/evals.json', [{'id': 'normal', 'prompt': 'Review.', 'expected_output': 'Bound conclusions.', 'files': []}])
        catalog = json.loads((self.root / 'catalog/skills.json').read_text())
        catalog['skills'].append({'name': 'other', 'path': 'skills/other', 'invocation': 'automatic', 'sources': ['origin'], 'boundary': '改用 sample。'})
        catalog['skills'][0]['boundary'] = '改用 other。'
        self.put('catalog/skills.json', catalog)
        self.put('.claude-plugin/plugin.json', {'name': 'liyuk-skills', 'version': '0.1.0', 'skills': ['./skills/sample', './skills/other']})
        errors = self.check()
        self.assertTrue(any('sample: description omits neighboring skill' in e and 'other' in e for e in errors))
        self.assertTrue(any('other: description omits neighboring skill' in e and 'sample' in e for e in errors))

    def test_readme_section_counts_must_match(self):
        self.write('README.md', '[English README](README.en.md)\n[sample](skills/sample/SKILL.md)\n\n## 一\n\n## 二\n')
        self.write('README.en.md', '[Chinese](README.md)\n\n## One\n')
        self.assertTrue(any('section count differs' in e for e in self.check()))

    def test_missing_repo_link_is_reported(self):
        self.write('docs/note.md', '[Missing](missing.md)\n')
        self.assertTrue(any('missing local link' in e for e in self.check()))


if __name__ == '__main__':
    unittest.main()
