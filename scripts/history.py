"""Reviewed subject-based history, retaining source notes and permalink aliases."""
from copy import deepcopy
from hashlib import sha256
import json
from pathlib import Path
from bs4 import BeautifulSoup
from reading_edits import attribution_markup


def curate_history(entries, topics, source_tags, configuration, registry_path):
    registry_path = Path(registry_path)
    registry = json.loads(registry_path.read_text())
    if registry.get('version') != 1:
        raise ValueError('Unsupported historical exposition registry')
    configuration = deepcopy(configuration)
    chapter = next(c for c in configuration['chapters'] if c['slug'] == 'historical-notes')
    old_topics = set(chapter['topics'])
    historical = {tag: e for tag, e in entries.items() if e['topic'] in old_topics}
    question_topic = registry['questions']['slug']
    question_tags = {tag for tag, e in historical.items() if not e['variants'][0].get('section')}
    question_tags.add(registry['questions']['heading'])
    topics[question_topic] = {'slug': question_topic, 'title': registry['questions']['title'], 'description': ''}
    questions = next(c for c in configuration['chapters'] if c['slug'] == registry['questions']['chapter'])
    questions['topics'].append(question_topic)
    for tag in question_tags:
        historical[tag]['topic'] = question_topic
    heading = historical[registry['questions']['heading']]
    heading['section_intro'] = True
    heading['variants'][0]['caption'] = registry['questions']['title']
    prose = {tag: e for tag, e in historical.items() if tag not in question_tags}
    seen, retained, replacements = set(), [], {}
    for section in registry['sections']:
        members = section['members']
        if section['tag'] not in members or seen.intersection(members):
            raise ValueError('Repeated or missing historical section member')
        variants = []
        for tag in members:
            if tag not in prose:
                raise ValueError(f'Missing historical source heading: {tag}')
            for original in prose[tag]['variants']:
                key = original['source'] + '/' + original['label']
                if sha256(original['html'].encode()).hexdigest() != registry['source_sha256'].get(key):
                    raise ValueError(f'Review changed historical source prose: {key}')
                retained.append({'source': original['source'], 'tag': section['tag'], 'label': original['label'], 'html': attribution_markup(BeautifulSoup(original['html'], 'html.parser'))})
                variants.append({**original, 'html': '', 'caption': section['title'], 'historical_alias': True})
                source_tags[original['source'], original['tag']] = section['tag']
            seen.add(tag)
        preferred = prose[section['tag']]['variants'][0]
        variants.sort(key=lambda v: (v['source'], v['label']) != (preferred['source'], preferred['label']))
        path = (registry_path.parent / section['file']).resolve()
        if not path.is_relative_to(registry_path.parent.resolve()) or path.suffix != '.html':
            raise ValueError('Historical exposition files must remain in their directory')
        variants[0].update(html=path.read_text(), historical_alias=False)
        replacements[section['tag']] = {**prose[section['tag']], 'title': section['title'], 'topic': section['slug'], 'variants': variants, 'section_intro': True, 'historical': True, 'merge_note': ''}
        topics[section['slug']] = {'slug': section['slug'], 'title': section['title'], 'description': ''}
    if seen != prose.keys():
        raise ValueError(f'Unassigned historical source headings: {sorted(prose.keys() - seen)}')
    for tag in prose:
        del entries[tag]
    entries.update(replacements)
    chapter['topics'] = [s['slug'] for s in registry['sections']]
    for topic in old_topics:
        topics.pop(topic)
    return configuration, retained
