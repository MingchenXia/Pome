from copy import deepcopy
from hashlib import sha256
import json
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from history import curate_history
from numbering import assign_numbers


class HistoryTests(unittest.TestCase):
    def setUp(self):
        def entry(tag, source, heading=True):
            variant = dict(source=source, label=tag, tag=tag, caption=tag, title=tag,
                           html=f'<p id="{tag}">Original {tag}.</p>', section=heading, kind='section' if heading else 'problem')
            return dict(tag=tag, variants=[variant], topic='old-history', components=[], kind=variant['kind'])
        self.entries = {tag: entry(tag, source, heading) for tag, source, heading in [('A', 'first', True), ('B', 'second', True), ('Q', 'second', True), ('P', 'second', False)]}
        self.topics = {'old-history': {'title': 'History'}}
        self.links = {(v['source'], v['tag']): tag for tag,e in self.entries.items() for v in e['variants']}
        self.config = {'chapters': [dict(slug='problems', number=1, topics=[]), dict(slug='historical-notes', number=2, topics=['old-history'])]}
        self.registry = dict(version=1, questions=dict(slug='questions', title='Questions', heading='Q', chapter='problems'),
                             sections=[dict(tag='A', slug='new-history', title='A connected history', members=['A', 'B'], file='history.html')],
                             source_sha256={v['source']+'/'+v['label']: sha256(v['html'].encode()).hexdigest() for e in self.entries.values() for v in e['variants']})

    def curate(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)
            (root/'history.html').write_text('<p>A connected exposition.</p>')
            (root/'registry.json').write_text(json.dumps(self.registry))
            return curate_history(self.entries,self.topics,self.links,self.config,root/'registry.json')

    def test_history_has_one_reading_section_and_all_source_aliases(self):
        question=deepcopy(self.entries['P'])
        config,notes=self.curate()
        self.assertEqual(set(self.entries), {'A','Q','P'})
        self.assertEqual(self.links['second','B'],'A')
        self.assertEqual(config['chapters'][1]['topics'],['new-history'])
        self.assertEqual(config['chapters'][0]['topics'],['questions'])
        self.assertEqual(self.entries['P']['variants'],question['variants'])
        self.assertEqual(len(notes),2)
        self.assertTrue(all('id=' not in note['html'] for note in notes))
        numbers=assign_numbers({c['slug']:c for c in config['chapters']},self.entries)
        self.assertEqual(numbers['second','B']['number'],numbers['first','A']['number'])
        self.assertEqual(self.entries['P']['number'],'1.1.1')

    def test_changed_historical_source_requires_review(self):
        self.entries['B']['variants'][0]['html']='<p>Changed attribution.</p>'
        with self.assertRaisesRegex(ValueError,'Review changed historical source'):
            self.curate()

    def test_unassigned_historical_heading_fails(self):
        self.registry['sections'][0]['members']=['A']
        with self.assertRaisesRegex(ValueError,'Unassigned historical'):
            self.curate()


if __name__=='__main__':
    unittest.main()
