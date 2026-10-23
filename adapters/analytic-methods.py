"""Export the reviewed analytic-methods supplement through its exact source manifest.

Only the selected mathematical input graph, bibliography and subject history
are read. Original scans and private research records are outside this graph.
"""
import json
from hashlib import sha256
from pathlib import Path, PurePosixPath
import re
import sys
from bs4 import BeautifulSoup, Tag
from common import configure, export, uncomment

SLUG = 'analytic-methods'
RESULTS = ('R0302', 'R0301', 'R0300', 'R0308', 'R0304', 'R0303', 'R0305', 'R0307',
           'R0309', 'R0310', 'R0311', 'R0312', 'R0313', 'R0314', 'R0315', 'R0316',
           'R0317', 'R0322', 'R0321', 'R0323', 'R0324', 'R0325', 'R0326',
           'R0327', 'R0329', 'R0328', 'R0330', 'R0331', 'R0332', 'R0318',
           'R0319', 'R0320', 'R0333', 'R0334', 'R0335', 'R0336', 'R0337',
           'R0338', 'R0339', 'R0340', 'R0343', 'R0341', 'R0342', 'R0344', 'R0345', 'R0346', 'R0347')
ENTRYPOINT = 'contributions/analytic-methods-public.tex'
BIBLIOGRAPHY = 'contributions/analytic-methods-public.bib'
MANIFEST = 'integrations/S0050/source-manifest.json'
LAYOUT = 'integrations/S0050/section-layout.json'
BRIDGES = 'integrations/S0050/canonical-references.json'
HISTORY = 'integrations/S0050/project-history.tex'
HEAD = re.compile(r'\\(?:section|subsection|subsubsection)\*?\s*\{')
REFERENCES = re.compile(r'\\(cref|Cref|eqref|ref|autoref)\*?\s*\{([^}]+)\}')
PARAGRAPHS = {
    'R0309': ('Quantifiers in the jet-volume application.',
              'heading:quantifiers-in-the-jet-volume-application'),
    'R0334': ('Relation to a class-valued numerical dimension.',
              'heading:relation-to-a-class-valued-numerical-dimension'),
}


def proof_paths(manifest):
    results=manifest['results']
    paths=manifest.get('proof_paths',{r:f'results/{r}/proof.tex' for r in results})
    if not isinstance(paths,dict) or set(paths)!=set(results):
        raise ValueError('Incomplete selected proof path map')
    for result,name in paths.items():
        if name != f'contributions/{SLUG}/{result}.tex':
            raise ValueError('Proof path is outside the selected contribution graph: '+result)
    if len(set(paths.values()))!=len(paths):
        raise ValueError('Repeated selected proof path')
    return paths


def manifest_for(source):
    path = (source / MANIFEST).resolve()
    if not path.is_relative_to(source.resolve()) or not path.is_file():
        raise ValueError('Missing or escaping analytic-methods manifest')
    manifest = json.loads(path.read_text())
    if manifest.get('version') != 1 or manifest.get('source_slug') != SLUG:
        raise ValueError('Invalid analytic-methods manifest identity')
    if manifest.get('status') != 'reviewed-export' or not manifest.get('results'):
        raise ValueError('analytic-methods export has no final reviewed selection')
    review = manifest.get('selection_review', {})
    if (review.get('status') != 'accepted' or not review.get('evidence')
            or not review.get('reviewer') or not review.get('checked_at')):
        raise ValueError('Analytic-methods selection needs an explicit final review receipt')
    results = manifest['results']
    if tuple(results) != RESULTS:
        raise ValueError('Analytic-methods selection changed; review the adapter allowlist')
    reviews = manifest.get('result_reviews', {})
    if set(reviews) != set(results) or any(
            r.get('status') != 'accepted' or not r.get('evidence')
            for r in reviews.values()):
        raise ValueError('Every selected analytic-methods proof needs acceptance evidence')
    if len(set(results)) != len(results) or any(not re.fullmatch(r'R\d{4}',r) for r in results):
        raise ValueError('Invalid or repeated selected result')
    paths=proof_paths(manifest)
    expected = {ENTRYPOINT, BIBLIOGRAPHY, LAYOUT, BRIDGES, HISTORY, *paths.values()}
    if (not isinstance(manifest.get('files'), dict)
            or set(manifest['files']) != expected
            or any(not isinstance(h, str) or not re.fullmatch(r'[a-f0-9]{64}', h)
                   for h in manifest['files'].values())):
        raise ValueError('analytic-methods export file graph differs from exact public allowlist')
    return manifest


def selected_text(source,name,manifest):
    rel = PurePosixPath(name)
    if rel.is_absolute() or '..' in rel.parts or '\\' in name:
        raise ValueError('Invalid selected analytic-methods path')
    path=(source/name).resolve()
    if not path.is_relative_to(source.resolve()) or not path.is_file():
        raise ValueError('Missing or escaping selected analytic-methods path: '+name)
    data=path.read_bytes()
    if sha256(data).hexdigest()!=manifest['files'].get(name):
        raise ValueError('Review changed analytic-methods export file: '+name)
    return uncomment(data.decode('utf-8'))


def close_group(text,start):
    depth,pos=1,start
    while pos<len(text) and depth:
        if text[pos]=='\\':
            match=re.match(r'\\(?:[A-Za-z@]+|.)',text[pos:])
            pos += len(match[0]) if match else 1
            continue
        depth += (text[pos]=='{')-(text[pos]=='}')
        pos += 1
    if depth:raise ValueError('Unbalanced selected heading')
    return pos


def validate_canonical_binding(name,binding):
    if (not isinstance(binding,dict) or not binding.get('review_evidence')
            or not isinstance(binding.get('caption_tex'),str) or not binding['caption_tex'].strip()):
        raise ValueError('Unreviewed canonical reference: '+name)
    review=binding.get('consumer_review',{})
    if not isinstance(review,dict) or review.get('status')!='accepted' or not review.get('evidence'):
        raise ValueError('Canonical reference consumer review pending: '+name)
    if not re.fullmatch(r'[A-F0-9]{8,12}',binding.get('tag','')):
        raise ValueError('Invalid canonical tag: '+name)


def prepare_fragment(text,result,layout,bridges,local_labels,editorials_already_applied=False):
    # Reviewed wording changes precede label/title/reference transformations.
    # Portable fragments may already contain exactly the reviewed replacement.
    for placement in layout.values():
        if placement.get('result_id')!=result:
            continue
        for rewrite in placement.get('editorial_rewrites',[]):
            old,new,reason=(rewrite.get(key) for key in ('old','new','reason'))
            if (not all(isinstance(value,str) and value for value in (old,new,reason))
                    or old in new):
                raise ValueError('Invalid reviewed editorial rewrite: '+result)
            if editorials_already_applied:
                continue
            count=text.count(old)
            if count==1:
                text=text.replace(old,new,1)
            elif count!=0 or text.count(new)!=1:
                raise ValueError('Stale or repeated reviewed editorial rewrite: '+result)
    # Stable synthetic labels are reviewed in LAYOUT, independent of numbering.
    edits=[]
    for count,match in enumerate(HEAD.finditer(text),1):
        end=close_group(text,match.end())
        if not text[end:].lstrip().startswith(r'\label'):
            label=f'sec:analytic-methods-{result.lower()}-{count}'
            if label not in layout:raise ValueError('Unreviewed synthetic heading: '+label)
            edits.append((end,rf'\label{{{label}}}'))
    for pos,label in reversed(edits):text=text[:pos]+label+text[pos:]
    if not HEAD.search(text):
        label=f'sec:analytic-methods-{result.lower()}-1'
        if label not in layout:raise ValueError('Missing reviewed fragment heading')
        text=rf"\section{{{layout[label]['title_tex']}}}\label{{{label}}}"+'\n'+text
    # Subject splits are permitted only before a complete named statement.
    # Keeping these edits here preserves the frozen research proof bytes.
    for label, placement in layout.items():
        anchor=placement.get('split_before_label')
        if placement.get('result_id')!=result or not anchor:
            continue
        if re.search(r'\\label\s*\{'+re.escape(label)+r'\}',text):
            continue  # Already transformed, and protected by the manifest hash.
        pattern=re.compile(r'\\begin\{(?:theorem|proposition|lemma|corollary|definition|example|remark)\}'
                           r'(?:\[[^\]]*\])?\s*\\label\s*\{'+re.escape(anchor)+r'\}')
        matches=list(pattern.finditer(text))
        if len(matches)!=1:
            raise ValueError('Subject split must precede one complete named statement: '+anchor)
        pos=matches[0].start()
        text=(text[:pos]+rf"\section{{{placement['title_tex']}}}\label{{{label}}}"+'\n\n'+text[pos:])
    # Titles describe their mathematical subject; labels and proof text stay fixed.
    for match in reversed(list(HEAD.finditer(text))):
        end=close_group(text,match.end())
        following=re.match(r'\s*\\label\s*\{([^}]+)\}',text[end:])
        if not following or following[1] not in layout:
            raise ValueError('Unreviewed explicit subject heading')
        title=layout[following[1]].get('title_tex')
        if title:
            text=text[:match.end()]+title+text[end-1:]
    def reference(match):
        names=[s.strip() for s in match[2].split(',')]
        if all(name in local_labels for name in names):return match[0]
        output=[]
        for name in names:
            if name in local_labels:
                output.append('\\'+match[1]+'{'+name+'}')
                continue
            binding=bridges.get(name)
            validate_canonical_binding(name,binding)
            # Captions are reviewed descriptions, never copied source numbers.
            output.append(r'\href{https://mingchenxia.github.io/Pome/tag/'+binding['tag']+'/}{'+binding['caption_tex']+'}')
        return ', '.join(output)
    text=REFERENCES.sub(reference,text)
    if result in PARAGRAPHS:
        title,label=PARAGRAPHS[result]
        heading=r'\paragraph{'+title+'}'
        if text.count(heading)!=1:
            raise ValueError('Review changed analytic-methods paragraph: '+result)
        text=text.replace(heading,heading+r'\label{'+label+'}',1)
    if re.search(r'\\(?:input|include)\b',text):
        raise ValueError('Nested analytic-methods proof input: '+result)
    if re.search(r'\\paragraph\*?\{Sources\.?\}',text):
        raise ValueError('Move per-entry attribution to the final subject history')
    return text


def selected_material(source):
    manifest=manifest_for(source)
    # The common renderer reads the bibliography later; validate its exact
    # bytes and path here before any part of that export can proceed.
    selected_text(source,BIBLIOGRAPHY,manifest)
    layout=json.loads(selected_text(source,LAYOUT,manifest))['sections']
    layout_by_label={s['label']:s for s in layout}
    if len(layout_by_label)!=len(layout):raise ValueError('Duplicate reviewed analytic-methods heading')
    bridges=json.loads(selected_text(source,BRIDGES,manifest))['references']
    # Portable fragments already contain resolved hrefs. Validate their entire
    # selected interface map even when no unresolved cref needs replacement.
    for name,binding in bridges.items():
        validate_canonical_binding(name,binding)
    paths=proof_paths(manifest)
    texts={r:selected_text(source,paths[r],manifest) for r in manifest['results']}
    history=selected_text(source,HISTORY,manifest)
    labels=[label for text in [*texts.values(),history] for label in re.findall(r'\\label\s*\{([^}]+)\}',text)]
    if len(set(labels))!=len(labels):raise ValueError('Duplicate selected analytic-methods label')
    transformations=manifest.get('proof_transformations')
    if transformations is not None:
        if not isinstance(transformations,dict) or set(transformations)!=set(texts):
            raise ValueError('Incomplete portable analytic-methods proof transformations')
        for result,binding in transformations.items():
            name=paths[result]
            if (not isinstance(binding,dict)
                    or binding.get('portable_proof_sha256')!=manifest['files'][name]
                    or not re.fullmatch(r'[a-f0-9]{64}',binding.get('research_proof_sha256',''))
                    or binding['research_proof_sha256'] != manifest['result_reviews'][result].get('research_proof_sha256')
                    or not binding.get('transformation')):
                raise ValueError('Portable analytic-methods proof hash binding changed: '+result)
    linked_tags = set(re.findall(r'https://mingchenxia\.github\.io/Pome/tag/([A-F0-9]{8,12})/', '\n'.join(texts.values())))
    reviewed_tags = {binding['tag'] for binding in bridges.values()}
    if linked_tags != reviewed_tags:
        raise ValueError('Canonical dependency links differ from the reviewed interface')
    # selected_text has already checked these exact portable bytes. Heading
    # labels and reference bridges can interrupt a previously applied wording
    # replacement, so only the verified portable binding skips that operation.
    prepared={r:prepare_fragment(text,r,layout_by_label,bridges,set(labels),
                                editorials_already_applied=transformations is not None)
              for r,text in texts.items()}
    history=prepare_fragment(history,'history',layout_by_label,bridges,set(labels))
    final_labels=[label for text in [*prepared.values(),history]
                  for label in re.findall(r'\\label\s*\{([^}]+)\}',text)]
    if len(set(final_labels))!=len(final_labels):
        raise ValueError('Duplicate prepared analytic-methods label')
    if set(layout_by_label)-set(final_labels):
        raise ValueError('Unused reviewed analytic-methods subject boundary')
    return manifest,layout_by_label,prepared,history


def reference_kind_prefixes(text):
    # cleveref supplies the actual referenced environment kind. Hand-written
    # prefixes can repeat it or name a different kind; ordinary ref is numeric.
    return re.sub(r'\b(?:[Tt]heorems?|[Ll]emmas?|[Pp]ropositions?|'
                  r'[Cc]orollar(?:y|ies)|[Dd]efinitions?|[Ee]xamples?)'
                  r'\s*(?:~\s*)?(?=\\[cC]ref\*?\s*\{)', '', text)


def prepare_article(source):
    manifest,layout,texts,history=selected_material(source)
    article=selected_text(source,ENTRYPOINT,manifest)
    preamble,body=article.split(r'\begin{document}',1)
    if r'\newtheorem{theorem}{Theorem}[section]' not in preamble:
        raise ValueError('Review analytic-methods theorem numbering declarations')
    used=[]
    expected={path.removesuffix('.tex'):r for r,path in proof_paths(manifest).items()}
    expected[HISTORY.removesuffix('.tex')]='project-history'
    def include(match):
        name=match[1]
        if name not in expected or name in used:raise ValueError('Unexpected/repeated analytic-methods input')
        used.append(name)
        return history if expected[name]=='project-history' else texts[expected[name]]
    body=re.sub(r'\\(?:input|include)\s*\{([^}]+)\}',include,body)
    if used!=list(expected) or re.search(r'\\(?:input|include)\b',body):
        raise ValueError('analytic-methods input graph/order changed')
    body=body.replace(r'\maketitle','').replace(r'\tableofcontents','')
    body=re.sub(r'\\(?:bibliographystyle|bibliography)\{[^}]+\}','',body)
    body=reference_kind_prefixes(body)
    declarations=[line for line in preamble.splitlines() if line.startswith((r'\newtheorem',r'\newcommand'))]
    # Native alias counters preserve cleveref kinds. The web parser assigns
    # kinds from environments and needs only the shared theorem counter.
    declarations=[re.sub(
        r'(\\newtheorem\{(?:proposition|lemma|corollary|definition|example|remark)\})'
        r'\[(?:proposition|lemma|corollary|definition|example|remark)\]',
        lambda match:match[1]+'[theorem]',line) for line in declarations]
    return '\\documentclass{article}\n\\usepackage{amsmath,amssymb,hyperref}\n'+'\n'.join(declarations)+'\n\\begin{document}\n'+body


def assign_topics(source,records):
    manifest,layout,texts,history=selected_material(source)
    labels={}
    seen=set()
    texts['project-history']=history
    for result in [*manifest['results'],'project-history']:
        topic=None
        for label in re.findall(r'\\label\s*\{([^}]+)\}',texts[result]):
            if label in labels:raise ValueError('Duplicate analytic-methods label: '+label)
            if label in layout:
                topic=layout[label]['topic'];seen.add(label)
            if topic is None:raise ValueError('Label before reviewed analytic-methods subject: '+label)
            labels[label]=topic
    if seen != set(layout):
        raise ValueError('Missing or reordered analytic-methods subject boundary')
    exported_labels={label for r in records for label in [r['label'],*r.get('aliases',[])]}
    if exported_labels!=set(labels):
        raise ValueError('Incomplete analytic-methods exported label coverage: '
                         f'missing={sorted(set(labels)-exported_labels)}, '
                         f'extra={sorted(exported_labels-set(labels))}')
    for record in records:
        record['topic']=labels[record['label']]
        if any(labels[alias]!=record['topic'] for alias in record.get('aliases',[])):
            raise ValueError('Aliased labels cross reviewed subject boundaries')
        for field in ('html','proof_html'):
            if field in record:
                record[field]=re.sub(r'href="https://mingchenxia\.github\.io/Pome/tag/([A-F0-9]{8,12})/"',
                    lambda m:m[0]+' data-proof-entry="'+m[1]+'"',record[field])
    return apply_reader_context(manifest,layout,texts,records)


FORMAL = re.compile(r'\\begin\{(?:theorem|proposition|lemma|corollary|definition|example|remark)\}')


def introductory_markup(record):
    """Return only prose/displays before the first formal environment."""
    if not record.get('section'):
        raise ValueError('Reader context source must be a section')
    soup=BeautifulSoup(record['statement_html'],'html.parser')
    for node in soup.select('.reader-context'):
        node.decompose()
    for node in soup.select('[data-proof-entry]'):
        del node['data-proof-entry']
    pieces=[]
    for node in soup.children:
        if not isinstance(node,Tag):
            continue
        if re.fullmatch(r'h[1-6]',node.name):
            continue
        if node.name=='article' or node.find('article'):
            break
        if node.name not in {'p','div','ol','ul','table','blockquote'}:
            raise ValueError('Unexpected analytic-methods introduction structure')
        pieces.append(str(node))
    return '\n'.join(pieces)


def copy_context(markup):
    """Copied conventions retain links, while source entries own all IDs."""
    markup=re.sub(r'\\label(?:\[[^]]*\])?\s*\{[^{}]*\}','',markup)
    soup=BeautifulSoup(markup,'html.parser')
    for node in soup.select('.equation-label, .tag-id, .environment-identifier'):
        node.decompose()
    for node in soup.select('[id]'):
        del node['id']
    for node in soup.select('[data-gerby-tag]'):
        del node['data-gerby-tag']
    if soup.select('article,script,style'):
        raise ValueError('Reader context cannot copy a statement or executable content')
    for anchor in soup.select('a[href]'):
        match=re.fullmatch(r'https://mingchenxia\.github\.io/Pome/tag/([A-F0-9]{8,12})/',anchor['href'])
        if match:
            anchor['data-proof-entry']=match[1]
    return str(soup)


def apply_reader_context(manifest,layout,texts,records):
    """Supply exact reviewed native introductions to isolated formal entries.

    Complete sections already contain these conventions. Only explicitly
    listed later subject splits also receive a copy. The source and rendered
    prefix hashes guard both the native boundary and the renderer extraction.
    """
    by_label={record['label']:record for record in records}
    planned={}
    for label,placement in layout.items():
        binding=placement.get('reader_context')
        if binding is None:
            continue
        result=placement.get('result_id')
        if result not in manifest['results'] or label not in by_label:
            raise ValueError('Missing analytic-methods reader context source')
        text=texts[result]
        scope=binding.get('native_scope','packet')
        if scope not in {'packet','section'}:
            raise ValueError('Invalid analytic-methods native context scope')
        if scope=='section':
            headings=list(HEAD.finditer(text))
            starts=[]
            for heading in headings:
                end=close_group(text,heading.end())
                following=re.match(r'\s*\\label\s*\{([^}]+)\}',text[end:])
                if following and following[1]==label:
                    starts.append(heading.start())
            if len(starts)!=1:
                raise ValueError('Missing native reader context section: '+label)
            start=starts[0]
            stop=next((h.start() for h in headings if h.start()>start),len(text))
            text=text[start:stop]
        first=FORMAL.search(text)
        if first is None or sha256(text[:first.start()].encode()).hexdigest()!=binding.get('native_prefix_sha256'):
            raise ValueError('Native reader context boundary changed: '+result)
        markup=introductory_markup(by_label[label])
        if not markup.strip() or sha256(markup.encode()).hexdigest()!=binding.get('rendered_prefix_sha256'):
            raise ValueError('Rendered reader context boundary changed: '+result)
        targets=binding.get('targets')
        local=set(re.findall(r'\\label\s*\{([^}]+)\}',text))
        if (not isinstance(targets,list) or not targets or len(set(targets))!=len(targets)
                or label in targets or not set(targets)<=local or not binding.get('reason')):
            raise ValueError('Invalid analytic-methods context target map')
        context='<div class="reader-context" data-context-position="before">'+copy_context(markup)+'</div>\n'
        for target in targets:
            record=by_label.get(target)
            if (record is None or target in planned
                    or record['kind'] not in {'theorem','proposition','lemma','corollary','definition','example','remark','section','subsection','subsubsection'}):
                raise ValueError('Missing or invalid reader context target: '+target)
            if record['section'] and (target not in layout or layout[target].get('result_id')!=result):
                raise ValueError('Reader context crosses a subject packet')
            planned[target]=context
    for label,context in planned.items():
        record=by_label[label]
        for field in ('html','statement_html'):
            if BeautifulSoup(record[field],'html.parser').select('.reader-context'):
                raise ValueError('Repeated analytic-methods reader context')
            record[field]=context+record[field]
    return records


if __name__=='__main__':
    configure(SLUG,'Singular metrics, generation and canonical systems',
              'https://github.com/MingchenXia/Gerby-Literature',
              author='Gerby Literature',bibliography=BIBLIOGRAPHY)
    export(Path(sys.argv[1]),Path(sys.argv[2]),prepare=prepare_article,transform=assign_topics)
