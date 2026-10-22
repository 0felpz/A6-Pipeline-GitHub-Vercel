from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class TestSite(unittest.TestCase):
    def test_html_existe(self):
        self.assertTrue((ROOT / 'public' / 'index.html').is_file())

    def test_estrutura_html(self):
        html = (ROOT / 'public' / 'index.html').read_text(encoding='utf-8').lower()
        for trecho in ('<!doctype html>', '<html', '<title>', '</html>'):
            with self.subTest(trecho=trecho):
                self.assertIn(trecho, html)

if __name__ == '__main__':
    unittest.main()
