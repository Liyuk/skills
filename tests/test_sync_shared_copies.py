import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / 'scripts/sync_shared_copies.py'


class SharedCopyTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        shared = self.root / 'shared'
        shared.mkdir()
        (shared / 'contract.md').write_text('canonical\n')
        tree = shared / 'tree'
        tree.mkdir()
        (tree / 'note.md').write_text('shared note\n')
        (self.root / 'skills/sample').mkdir(parents=True)
        manifest = {
            'files': [{
                'source': 'shared/contract.md',
                'destinations': ['skills/sample/references/contract.md'],
            }],
            'trees': [{
                'source': 'shared/tree',
                'destinations': ['skills/sample'],
            }],
        }
        (shared / 'manifest.json').write_text(json.dumps(manifest))

    def module(self):
        spec = importlib.util.spec_from_file_location('sync_shared_copies', SCRIPT)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module

    def test_write_then_check_passes(self):
        module = self.module()
        written = module.write_copies(self.root)
        self.assertEqual(
            ['skills/sample/references/contract.md', 'skills/sample/note.md'],
            written,
        )
        self.assertEqual([], module.copy_errors(self.root))

    def test_drift_is_reported(self):
        module = self.module()
        module.write_copies(self.root)
        (self.root / 'skills/sample/note.md').write_text('edited copy\n')
        errors = module.copy_errors(self.root)
        self.assertTrue(any('differs from shared/tree/note.md' in e for e in errors))

    def test_unlisted_contract_is_reported(self):
        module = self.module()
        module.write_copies(self.root)
        extra = self.root / 'skills/sample/references/decision-and-review-contract.md'
        extra.write_text('extra\n')
        errors = module.copy_errors(self.root)
        self.assertTrue(any('not listed' in e for e in errors))


if __name__ == '__main__':
    unittest.main()
