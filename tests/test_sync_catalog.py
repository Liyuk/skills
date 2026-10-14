import importlib.util
import json
from pathlib import Path
import subprocess
import tempfile
import unittest

import yaml

SCRIPT = Path(__file__).resolve().parents[1] / 'scripts/sync_catalog.py'


class CatalogSyncTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.entry = {
            'name': 'sample', 'path': 'skills/sample', 'invocation': 'explicit',
            'display_name': 'Sample', 'short_description': 'Review the evidence',
            'core_judgment': 'Evidence bounds the conclusion', 'when_to_use': 'Review existing material',
            'input_example': 'Review this proposal', 'result_example': 'Evidence and next action',
            'boundary': 'Do not rewrite unless asked', 'group': 'Engineering',
            'origin': 'distilled', 'author_calibration': 'candidate',
            'behavior_validation': 'structure-only', 'validation_report': 'evals/report.md',
            'sources': ['test'],
        }
        self.write('README.md', 'Human introduction\n<!-- skills-catalog:start -->\nold\n<!-- skills-catalog:end -->\nHuman footer\n')
        self.put('catalog/skills.json', {'version': '0.4.0', 'skills': [self.entry]})
        self.write('evals/report.md', '# Actual validation scope\n')
        self.put('.claude-plugin/plugin.json', {'name': 'liyuk-skills', 'author': {'name': 'Liyuk'}, 'version': '0.3.0', 'skills': []})
        self.write('skills/sample/agents/openai.yaml', 'interface:\n  default_prompt: Keep my custom prompt\npolicy:\n  allow_implicit_invocation: false\n  custom_flag: true\n')

    def write(self, path, text):
        p = self.root / path
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text)

    def put(self, path, data):
        self.write(path, json.dumps(data))

    def renderer(self):
        self.assertTrue(SCRIPT.is_file(), 'catalog renderer not implemented')
        spec = importlib.util.spec_from_file_location('catalog_sync', SCRIPT)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module

    def test_render_preserves_human_readme_and_has_usable_doc(self):
        output = self.renderer().render(self.root)
        self.assertIn('Human introduction', output['README.md'])
        self.assertIn('Human footer', output['README.md'])
        self.assertIn('docs/skills/sample.md', output['README.md'])
        self.assertIn('Evidence bounds the conclusion', output['docs/skills/sample.md'])
        self.assertFalse((self.root / 'docs/skills/sample.md').exists())

    def test_metadata_preserves_prompt_and_unrelated_policy(self):
        output = self.renderer().render(self.root)
        meta = yaml.safe_load(output['skills/sample/agents/openai.yaml'])
        self.assertEqual(meta['interface']['default_prompt'], 'Keep my custom prompt')
        self.assertTrue(meta['policy']['custom_flag'])
        self.assertFalse(meta['policy']['allow_implicit_invocation'])
        self.assertEqual(meta['interface']['short_description'], 'Review the evidence')

    def test_plugin_preserves_identity_and_syncs_version(self):
        plugin = json.loads(self.renderer().render(self.root)['.claude-plugin/plugin.json'])
        self.assertEqual(plugin['author']['name'], 'Liyuk')
        self.assertEqual(plugin['version'], '0.4.0')
        self.assertEqual(plugin['skills'], ['./skills/sample'])

    def test_duplicate_name_rejected(self):
        self.put('catalog/skills.json', {'version': '0.4.0', 'skills': [self.entry, self.entry]})
        with self.assertRaises(ValueError):
            self.renderer().render(self.root)

    def test_path_escape_rejected(self):
        self.entry['path'] = '../outside'
        self.put('catalog/skills.json', {'version': '0.4.0', 'skills': [self.entry]})
        with self.assertRaises(ValueError):
            self.renderer().render(self.root)

    def test_ambiguous_validation_state_rejected(self):
        self.entry['behavior_validation'] = 'migrated'
        self.put('catalog/skills.json', {'version': '0.4.0', 'skills': [self.entry]})
        with self.assertRaises(ValueError):
            self.renderer().render(self.root)

    def test_wrong_validation_state_type_is_diagnostic(self):
        self.entry['behavior_validation'] = []
        self.put('catalog/skills.json', {'version': '0.4.0', 'skills': [self.entry]})
        with self.assertRaises(ValueError):
            self.renderer().render(self.root)

    def test_missing_validation_report_rejected(self):
        (self.root / 'evals/report.md').unlink()
        with self.assertRaises(ValueError):
            self.renderer().render(self.root)

    def test_missing_readme_marker_rejected(self):
        self.write('README.md', 'Handwritten only')
        with self.assertRaises(ValueError):
            self.renderer().render(self.root)

    def test_check_detects_drift_then_passes_after_write(self):
        self.renderer()
        command = [str(Path(__import__('sys').executable)), str(SCRIPT), '--root', str(self.root)]
        drift = subprocess.run(command + ['--check'], capture_output=True, text=True)
        self.assertEqual(drift.returncode, 1)
        self.assertFalse((self.root / 'docs/skills/sample.md').exists())
        written = subprocess.run(command + ['--write'], capture_output=True, text=True)
        self.assertEqual(written.returncode, 0, written.stderr)
        checked = subprocess.run(command + ['--check'], capture_output=True, text=True)
        self.assertEqual(checked.returncode, 0, checked.stdout)
        p = self.root / 'docs/skills/sample.md'
        p.write_text('drift')
        self.assertEqual(subprocess.run(command + ['--check'], capture_output=True).returncode, 1)


if __name__ == '__main__':
    unittest.main()
