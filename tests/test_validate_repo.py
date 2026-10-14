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
        self.write('README.md', '[sample](skills/sample/SKILL.md)\n')

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


if __name__ == '__main__':
    unittest.main()
