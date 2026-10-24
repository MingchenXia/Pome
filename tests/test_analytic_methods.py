"""The reviewed S0050 graph must remain complete and exclude private inputs."""
import hashlib
import copy
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "adapters"))
spec = importlib.util.spec_from_file_location("analytic_methods", ROOT / "adapters/analytic-methods.py")
adapter = importlib.util.module_from_spec(spec)
spec.loader.exec_module(adapter)


class AnalyticMethodsTests(unittest.TestCase):
    def fixture(self, root):
        def write(name, text):
            path = root / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(text)

        paths = {r: f"contributions/analytic-methods/{r}.tex" for r in adapter.RESULTS}
        layout = []
        for result, name in paths.items():
            label = "sec:" + result
            layout.append({"result_id": result, "label": label, "title_tex": result, "topic": "First subject"})
            text = rf"""\section{{{result}}}\label{{{label}}}
\begin{{theorem}}\label{{thm:{result}}}For $x<y$, a selected statement.\end{{theorem}}
\begin{{proof}}Complete mathematical proof for {result}.\end{{proof}}
"""
            if result == "R0301":
                text += r"""\begin{corollary}\label{cor:second-subject}A consequence.\end{corollary}
\begin{proof}Use \cref{thm:R0301}.\end{proof}
"""
                layout.append({"result_id": result, "label": "sec:second-subject", "title_tex": "Second subject",
                               "topic": "Second subject", "split_before_label": "cor:second-subject"})
            if result == "R0302":
                text += r"\href{https://mingchenxia.github.io/Pome/tag/2EE58CB34CD0/}{a checked canonical premise}" + "\n"
            if result in adapter.PARAGRAPHS:
                title,_=adapter.PARAGRAPHS[result]
                text += r"\paragraph{"+title+"}\nA bounded scope qualification.\n"
            write(name, text)
        layout.append({"label": "sec:history", "title_tex": "History", "topic": "Historical and bibliographical notes"})
        write(adapter.HISTORY, r"\section{History}\label{sec:history}Subject attribution \cite{SelectedBook}." + "\n")
        write(adapter.BIBLIOGRAPHY, "@book{SelectedBook,author={Example, Author},title={Selected source},year={2011},publisher={Example}}\n")
        write(adapter.LAYOUT, json.dumps({"sections": layout}))
        bridges = {"external": {"tag": "2EE58CB34CD0", "caption_tex": "a checked canonical premise",
                   "review_evidence": ["fixture review"], "consumer_review": {"status": "accepted", "evidence": ["fixture review"]}}}
        write(adapter.BRIDGES, json.dumps({"references": bridges}))
        inputs = [*paths.values(), adapter.HISTORY]
        write(adapter.ENTRYPOINT, r"""\documentclass{article}
\newtheorem{theorem}{Theorem}[section]
\newtheorem{corollary}[theorem]{Corollary}
\begin{document}
""" + "\n".join(r"\input{" + p.removesuffix(".tex") + "}" for p in inputs) + "\n" + r"\end{document}")
        selected = [adapter.ENTRYPOINT, adapter.BIBLIOGRAPHY, adapter.LAYOUT, adapter.BRIDGES, adapter.HISTORY, *paths.values()]
        manifest = {"version": 1, "source_slug": adapter.SLUG, "status": "reviewed-export", "results": list(adapter.RESULTS),
                    "proof_paths": paths, "selection_review": {"status": "accepted", "reviewer": "fixture", "checked_at": "2026-10-22", "evidence": ["fixture"]},
                    "result_reviews": {r: {"status": "accepted", "evidence": ["fixture"]} for r in adapter.RESULTS},
                    "files": {p: hashlib.sha256((root / p).read_bytes()).hexdigest() for p in selected}}
        write(adapter.MANIFEST, json.dumps(manifest))
        write("library/originals/private.tex", "PRIVATE SOURCE SENTINEL")
        return manifest

    def rehash(self, root, name):
        path = root / adapter.MANIFEST
        manifest = json.loads(path.read_text())
        manifest["files"][name] = hashlib.sha256((root / name).read_bytes()).hexdigest()
        path.write_text(json.dumps(manifest))

    def test_export_has_all_labels_proofs_subject_splits_and_no_private_content(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            source, output = root / "source", root / "export"
            self.fixture(source)
            subprocess.run(["git", "init", "-q", str(source)], check=True)
            subprocess.run(["git", "-C", str(source), "add", "."], check=True)
            subprocess.run(["git", "-C", str(source), "-c", "user.name=Test", "-c", "user.email=test@example.invalid", "commit", "-qm", "fixture"], check=True)
            subprocess.run([sys.executable, str(ROOT / "adapters/analytic-methods.py"), str(source), str(output)], check=True, capture_output=True)
            entries = json.loads((output / "entries.json").read_text())
            expected = {f"{kind}:{r}" for kind in ("sec", "thm") for r in adapter.RESULTS}
            expected.update({"sec:second-subject", "cor:second-subject", "sec:history"})
            expected.update(label for _,label in adapter.PARAGRAPHS.values())
            self.assertEqual({e["label"] for e in entries}, expected)
            self.assertEqual(len(json.loads((output / "tags.json").read_text())), len(expected))
            result = next(e for e in entries if e["label"] == "cor:second-subject")
            self.assertEqual(result["topic"], "Second subject")
            self.assertIn("Use", result["proof_html"])
            self.assertTrue(all("x&lt;y" in e["statement_html"] for e in entries if e["kind"] == "theorem"))
            self.assertTrue(any('data-proof-entry="2EE58CB34CD0"' in e["html"] for e in entries))
            self.assertFalse(any("PRIVATE SOURCE SENTINEL" in p.read_text() for p in output.rglob("*") if p.is_file()))

    def test_changed_proof_bibliography_or_layout_stops_export(self):
        for name in ["contributions/analytic-methods/R0302.tex", adapter.BIBLIOGRAPHY, adapter.LAYOUT]:
            with self.subTest(name=name), tempfile.TemporaryDirectory() as temporary:
                root = Path(temporary)
                self.fixture(root)
                with (root / name).open("a") as stream:
                    stream.write("\nchanged after review\n")
                with self.assertRaisesRegex(ValueError, "Review changed"):
                    adapter.prepare_article(root)

    def test_private_manifest_addition_and_retired_packet_are_rejected(self):
        for mutation in ["private-file", "retired-packet"]:
            with self.subTest(mutation=mutation), tempfile.TemporaryDirectory() as temporary:
                root = Path(temporary)
                manifest = self.fixture(root)
                if mutation == "private-file":
                    manifest["files"]["library/originals/private.tex"] = "0" * 64
                else:
                    manifest["results"].append("R0306")
                (root / adapter.MANIFEST).write_text(json.dumps(manifest))
                with self.assertRaises(ValueError):
                    adapter.prepare_article(root)

    def test_rehashed_nested_and_repeated_inputs_still_fail(self):
        for change in ["nested", "repeated"]:
            with self.subTest(change=change), tempfile.TemporaryDirectory() as temporary:
                root = Path(temporary)
                self.fixture(root)
                if change == "nested":
                    name = "contributions/analytic-methods/R0302.tex"
                    (root / name).write_text((root / name).read_text() + r"\input{library/originals/private}")
                else:
                    name = adapter.ENTRYPOINT
                    text = (root / name).read_text()
                    original = r"\input{contributions/analytic-methods/R0302}"
                    (root / name).write_text(text.replace(original, original + original))
                self.rehash(root, name)
                with self.assertRaises(ValueError):
                    adapter.prepare_article(root)

    def test_selected_symlink_cannot_escape_the_repository(self):
        with tempfile.TemporaryDirectory() as temporary:
            base = Path(temporary)
            root = base / "source"
            self.fixture(root)
            name = "contributions/analytic-methods/R0302.tex"
            target = root / name
            outside = base / "outside.tex"
            outside.write_bytes(target.read_bytes())
            target.unlink()
            target.symlink_to(outside)
            with self.assertRaisesRegex(ValueError, "escaping"):
                adapter.prepare_article(root)

    def test_unreviewed_canonical_dependency_is_rejected(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self.fixture(root)
            name = "contributions/analytic-methods/R0302.tex"
            text = (root / name).read_text().replace("2EE58CB34CD0", "AAAAAAAAAAAA")
            (root / name).write_text(text)
            self.rehash(root, name)
            with self.assertRaisesRegex(ValueError, "Canonical dependency links"):
                adapter.prepare_article(root)

    def context_fixture(self):
        prefix = r"\section{Topology}\label{sec:topology}" + "\nLet $X$ be compact.\n"
        text = prefix + r"\begin{theorem}\label{thm:topology}The quotient is Hausdorff.\end{theorem}"
        intro = '<p>Let $X$ be compact.</p>\n<div class="equation" id="FORMULA"><span class="equation-label">1</span><div>\\[Z/B\\]</div></div>'
        statement = '<article class="env-theorem" id="THEOREM"><p>The quotient is Hausdorff.</p></article>'
        proof = '<article class="env-proof"><p>The denominator is closed.</p></article>'
        rows = [dict(label='sec:topology',tag='SECTION',kind='section',section=True,
                    statement_html='<h2>Topology</h2>'+intro+statement+proof,
                    html='<h2>Topology</h2>'+intro+statement+proof),
                dict(label='thm:topology',tag='THEOREM',kind='theorem',section=False,
                    statement_html=statement,html=statement+proof,proof_html=proof)]
        binding = dict(native_prefix_sha256=hashlib.sha256(prefix.encode()).hexdigest(),
            rendered_prefix_sha256=hashlib.sha256(intro.encode()).hexdigest(),
            targets=['thm:topology'],reason='The standalone theorem needs the compactness convention.')
        return {'results':['R0315']}, {'sec:topology':{'result_id':'R0315','reader_context':binding}}, {'R0315':text}, rows

    def test_standalone_context_retains_assumptions_without_duplicate_formula_owners(self):
        manifest,layout,texts,rows = self.context_fixture()
        before = copy.deepcopy(rows)
        adapter.apply_reader_context(manifest,layout,texts,rows)
        self.assertIn('Let $X$ be compact.',rows[1]['statement_html'])
        self.assertNotIn('id="FORMULA"',rows[1]['html'])
        self.assertNotIn('equation-label',rows[1]['html'])
        self.assertEqual(rows[1]['proof_html'],before[1]['proof_html'])
        self.assertEqual(rows[0],before[0])
        self.assertEqual(rows[1]['html'].count('id="THEOREM"'),1)

    def test_changed_native_or_rendered_context_requires_review(self):
        for field in ('native','rendered'):
            with self.subTest(field=field):
                manifest,layout,texts,rows = self.context_fixture()
                if field=='native':
                    texts['R0315']=texts['R0315'].replace('compact','complete')
                else:
                    rows[0]['statement_html']=rows[0]['statement_html'].replace('compact','complete')
                with self.assertRaisesRegex(ValueError,'context boundary changed'):
                    adapter.apply_reader_context(manifest,layout,texts,rows)

    def test_section_context_uses_its_own_module_and_rejects_cross_module_target(self):
        manifest,layout,texts,rows=self.context_fixture()
        original=texts['R0315']
        texts['R0315']=r'\section{Other}\label{sec:other}Other assumptions.\begin{lemma}\label{lem:other}Other result.\end{lemma}'+'\n'+original
        layout['sec:topology']['reader_context']['native_scope']='section'
        adapter.apply_reader_context(manifest,layout,texts,rows)
        self.assertIn('compact',rows[1]['html'])
        self.assertNotIn('Other assumptions',rows[1]['html'])
        manifest,layout,texts,rows=self.context_fixture()
        texts['R0315']+='\n'+r'\section{Other}\label{sec:other}\begin{lemma}\label{lem:other}Other result.\end{lemma}'
        binding=layout['sec:topology']['reader_context']
        binding['native_scope']='section'
        binding['targets']=['lem:other']
        with self.assertRaisesRegex(ValueError,'context target map'):
            adapter.apply_reader_context(manifest,layout,texts,rows)

    def chained_context_fixture(self):
        global_prefix=r'\section{Conventions}\label{sec:global}'+'\nThe base is compact.\n'
        local_prefix=r'\subsection{Local notation}\label{sec:local}'+'\nLet $A$ denote its curvature.\n'
        text=global_prefix+local_prefix+r'\begin{theorem}\label{thm:local}The integral is finite.\end{theorem}'
        global_markup='<p>The base is compact.</p>'
        local_markup='<p>Let $A$ denote its curvature.</p>'
        statement='<article class="env-theorem" id="LOCAL"><p>The integral is finite.</p></article>'
        proof='<article class="env-proof"><p>Integrate the bound.</p></article>'
        rows=[dict(label='sec:global',kind='section',section=True,statement_html='<h2>Conventions</h2>'+global_markup,html=global_markup),
              dict(label='sec:local',kind='subsection',section=True,statement_html='<h3>Local notation</h3>'+local_markup+statement,html=local_markup+statement+proof),
              dict(label='thm:local',kind='theorem',section=False,statement_html=statement,html=statement+proof,proof_html=proof)]
        chain=[dict(label=label,native_prefix_sha256=hashlib.sha256(native.encode()).hexdigest(),
                    rendered_prefix_sha256=hashlib.sha256(markup.encode()).hexdigest())
               for label,native,markup in [('sec:global',global_prefix,global_markup),('sec:local',local_prefix,local_markup)]]
        layout={'sec:global':dict(result_id='R0375'),
                'sec:local':dict(result_id='R0375',reader_context=dict(prefix_chain=chain,targets=['thm:local'],reason='Retain packet conventions and local notation in that order.'))}
        return {'results':['R0375']},layout,{'R0375':text},rows

    def test_chained_context_preserves_ancestor_and_local_order_without_changing_proofs(self):
        manifest,layout,texts,rows=self.chained_context_fixture()
        before=copy.deepcopy(rows)
        adapter.apply_reader_context(manifest,layout,texts,rows)
        rendered=rows[2]['statement_html']
        self.assertLess(rendered.index('base is compact'),rendered.index('denote its curvature'))
        self.assertLess(rendered.index('denote its curvature'),rendered.index('integral is finite'))
        self.assertEqual(rendered.count('class="reader-context"'),1)
        self.assertEqual(rows[:2],before[:2])
        self.assertEqual(rows[2]['proof_html'],before[2]['proof_html'])

    def test_each_chained_native_and_rendered_prefix_is_hash_checked(self):
        for position in (0,1):
            for field in ('native','rendered'):
                with self.subTest(position=position,field=field):
                    manifest,layout,texts,rows=self.chained_context_fixture()
                    if field=='native':
                        word='compact' if position==0 else 'curvature'
                        texts['R0375']=texts['R0375'].replace(word,'changed')
                    else:
                        rows[position]['statement_html']+='<p>Changed context.</p>' if position==0 else ''
                        if position==1:
                            rows[position]['statement_html']=rows[position]['statement_html'].replace('curvature','changed')
                    with self.assertRaisesRegex(ValueError,'context boundary changed'):
                        adapter.apply_reader_context(manifest,layout,texts,rows)

    def test_chained_prefix_order_packet_scope_and_target_order_are_guarded(self):
        for mutation in ('reverse','repeat','cross-packet','preceding-target','ambiguous-legacy'):
            with self.subTest(mutation=mutation):
                manifest,layout,texts,rows=self.chained_context_fixture()
                binding=layout['sec:local']['reader_context']
                if mutation=='reverse':binding['prefix_chain'].reverse()
                elif mutation=='repeat':binding['prefix_chain'][1]=copy.deepcopy(binding['prefix_chain'][0])
                elif mutation=='cross-packet':layout['sec:global']['result_id']='R0376'
                elif mutation=='preceding-target':binding['targets']=['sec:global']
                else:binding['native_scope']='packet'
                with self.assertRaises(ValueError):
                    adapter.apply_reader_context(manifest,layout,texts,rows)

    def test_new_context_schema_does_not_allow_a_pending_selection(self):
        with tempfile.TemporaryDirectory() as temporary:
            root=Path(temporary);manifest=self.fixture(root)
            manifest['selection_review']['status']='pending'
            (root/adapter.MANIFEST).write_text(json.dumps(manifest))
            with self.assertRaisesRegex(ValueError,'explicit final review receipt'):
                adapter.prepare_article(root)


if __name__ == "__main__":
    unittest.main()
