from pathlib import Path
import sys
import unittest

from bs4 import BeautifulSoup
from pybtex.database.input.bibtex import Parser
from pybtex.plugin import find_plugin

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "adapters"))
from common import bibliography_entry_for_html


class BibliographyTests(unittest.TestCase):
    def test_tex_publication_link_renders_as_a_real_link_without_changing_source(self):
        database = Parser().parse_string(r"""
@misc{book, author={Jean-Pierre Demailly}, year={2012},
 title={Complex Analytic and Differential Geometry},
 howpublished={\href{https://example.org/~author/book.pdf}{Author's website}}}
@article{paper, author={An Author}, title={A paper}, year={2000},
 journal={A journal}, volume={1}, pages={1--2}}
""")
        style = find_plugin("pybtex.style.formatting", "plain")()
        backend = find_plugin("pybtex.backends", "html")()

        def render(entry):
            return next(iter(style.format_entries([entry]))).text.render(backend)

        original = database.entries["book"]
        converted = bibliography_entry_for_html(original)
        soup = BeautifulSoup(render(converted), "html.parser")
        self.assertEqual(soup.a["href"], "https://example.org/~author/book.pdf")
        self.assertIn("Author's website", soup.get_text())
        self.assertNotIn(r"\href", soup.get_text())
        self.assertNotIn("url", original.fields)
        self.assertEqual(converted.fields["title"], original.fields["title"])
        self.assertEqual(converted.persons, original.persons)
        self.assertEqual(converted.fields["year"], original.fields["year"])
        paper = database.entries["paper"]
        self.assertEqual(render(bibliography_entry_for_html(paper)), render(paper))
