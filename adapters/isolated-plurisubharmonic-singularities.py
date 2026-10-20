"""Export the reviewed isolated-singularity supplement through its exact source manifest.

Only the selected mathematical input graph, bibliography and subject history
are read. Original scans and private research records are outside this graph.
"""
import json
from hashlib import sha256
from pathlib import Path, PurePosixPath
import re
import sys
from common import configure, export, uncomment

SLUG = 'isolated-plurisubharmonic-singularities'
ENTRYPOINT = 'contributions/isolated-plurisubharmonic-singularities.tex'
BIBLIOGRAPHY = 'contributions/isolated-plurisubharmonic-singularities.bib'
MANIFEST = 'integrations/S0076/source-manifest.json'
LAYOUT = 'integrations/S0076/section-layout.json'
BRIDGES = 'integrations/S0076/canonical-references.json'
HISTORY = 'integrations/S0076/project-history.tex'
HEAD = re.compile(r'\\(?:section|subsection|subsubsection)\*?\s*\{')
REFERENCES = re.compile(r'\\(cref|Cref|eqref|ref|autoref)\*?\s*\{([^}]+)\}')


def proof_paths(manifest):
    results=manifest['results']
    paths=manifest.get('proof_paths')
    if not isinstance(paths,dict) or set(paths)!=set(results):
        raise ValueError('Incomplete selected proof path map')
    for result,name in paths.items():
        if name != f'contributions/{SLUG}/{result}.tex':
            raise ValueError('Proof path is outside the selected contribution graph: '+result)
    if len(set(paths.values()))!=len(paths):
        raise ValueError('Repeated selected proof path')
    return paths


def manifest_for(source):
    manifest = json.loads((source/MANIFEST).read_text())
    if manifest.get('version') != 1 or manifest.get('source_slug') != SLUG:
        raise ValueError('Invalid isolated-singularity manifest identity')
    if manifest.get('status') != 'reviewed-export' or not manifest.get('results'):
        raise ValueError('isolated-singularity export has no final reviewed selection')
    review = manifest.get('selection_review', {})
    if (review.get('status') != 'accepted' or not review.get('evidence')
            or not review.get('reviewer') or not review.get('checked_at')):
        raise ValueError('Isolated-singularity selection needs an explicit final review receipt')
    results = manifest['results']
    reviews = manifest.get('result_reviews', {})
    if set(reviews) != set(results) or any(
            r.get('status') != 'accepted' or not r.get('evidence')
            for r in reviews.values()):
        raise ValueError('Every selected isolated-singularity proof needs acceptance evidence')
    if len(set(results)) != len(results) or any(not re.fullmatch(r'R\d{4}',r) for r in results):
        raise ValueError('Invalid or repeated selected result')
    paths=proof_paths(manifest)
    transformations=manifest.get('proof_transformations',{})
    if set(transformations)!=set(results):
        raise ValueError('Every selected proof needs a frozen portable transformation')
    for result in results:
        proof_hash=transformations[result].get('research_proof_sha256','')
        if not re.fullmatch(r'[a-f0-9]{64}',proof_hash):
            raise ValueError('Missing accepted original proof hash: '+result)
        roles=[]
        for role in ('root_review','independent_review'):
            binding=reviews[result].get(role,{})
            if (binding.get('status')!='accepted' or not binding.get('reviewer')
                    or binding.get('accepted_proof_sha256')!=proof_hash
                    or not binding.get('evidence')):
                raise ValueError('Missing exact root/independent proof review: '+result)
            for evidence in binding['evidence']:
                if (not isinstance(evidence,dict) or not evidence.get('path')
                        or not re.fullmatch(r'[a-f0-9]{64}',evidence.get('sha256',''))):
                    raise ValueError('Unbound proof-review evidence: '+result)
            roles.append(binding['reviewer'])
        if roles[0]==roles[1]:
            raise ValueError('Independent proof reviewer must differ from root: '+result)
    expected = {ENTRYPOINT, BIBLIOGRAPHY, LAYOUT, BRIDGES, HISTORY, *paths.values()}
    if (not isinstance(manifest.get('files'), dict)
            or set(manifest['files']) != expected
            or any(not isinstance(h, str) or not re.fullmatch(r'[a-f0-9]{64}', h)
                   for h in manifest['files'].values())):
        raise ValueError('isolated-singularity export file graph differs from exact public allowlist')
    return manifest


def selected_text(source,name,manifest):
    rel = PurePosixPath(name)
    if rel.is_absolute() or '..' in rel.parts or '\\' in name:
        raise ValueError('Invalid selected isolated-singularity path')
    path=(source/name).resolve()
    if not path.is_relative_to(source.resolve()) or not path.is_file():
        raise ValueError('Missing or escaping selected isolated-singularity path: '+name)
    data=path.read_bytes()
    if sha256(data).hexdigest()!=manifest['files'].get(name):
        raise ValueError('Review changed isolated-singularity export file: '+name)
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
            label=f'sec:isolated-singularities-{result.lower()}-{count}'
            if label not in layout:raise ValueError('Unreviewed synthetic heading: '+label)
            edits.append((end,rf'\label{{{label}}}'))
    for pos,label in reversed(edits):text=text[:pos]+label+text[pos:]
    if not HEAD.search(text):
        label=f'sec:isolated-singularities-{result.lower()}-1'
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
    if re.search(r'\\(?:input|include)\b',text):
        raise ValueError('Nested isolated-singularity proof input: '+result)
    if re.search(r'\\paragraph\*?\{Sources\.?\}',text):
        raise ValueError('Move per-entry attribution to the final subject history')
    return text


def selected_material(source):
    manifest=manifest_for(source)
    selected_text(source,BIBLIOGRAPHY,manifest)
    layout=json.loads(selected_text(source,LAYOUT,manifest))['sections']
    layout_by_label={s['label']:s for s in layout}
    if len(layout_by_label)!=len(layout):raise ValueError('Duplicate reviewed isolated-singularity heading')
    bridges=json.loads(selected_text(source,BRIDGES,manifest))['references']
    # Portable fragments already contain resolved hrefs. Validate their entire
    # selected interface map even when no unresolved cref needs replacement.
    for name,binding in bridges.items():
        validate_canonical_binding(name,binding)
    paths=proof_paths(manifest)
    texts={r:selected_text(source,paths[r],manifest) for r in manifest['results']}
    history=selected_text(source,HISTORY,manifest)
    labels=[label for text in [*texts.values(),history] for label in re.findall(r'\\label\s*\{([^}]+)\}',text)]
    if len(set(labels))!=len(labels):raise ValueError('Duplicate selected isolated-singularity label')
    transformations=manifest.get('proof_transformations')
    if transformations is not None:
        if not isinstance(transformations,dict) or set(transformations)!=set(texts):
            raise ValueError('Incomplete portable isolated-singularity proof transformations')
        for result,binding in transformations.items():
            name=paths[result]
            if (not isinstance(binding,dict)
                    or binding.get('portable_proof_sha256')!=manifest['files'][name]
                    or not re.fullmatch(r'[a-f0-9]{64}',binding.get('research_proof_sha256',''))
                    or not binding.get('transformation')):
                raise ValueError('Portable isolated-singularity proof hash binding changed: '+result)
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
        raise ValueError('Duplicate prepared isolated-singularity label')
    if set(layout_by_label)-set(final_labels):
        raise ValueError('Unused reviewed isolated-singularity subject boundary')
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
        raise ValueError('Review isolated-singularity theorem numbering declarations')
    used=[]
    expected={path.removesuffix('.tex'):r for r,path in proof_paths(manifest).items()}
    expected[HISTORY.removesuffix('.tex')]='project-history'
    def include(match):
        name=match[1]
        if name not in expected or name in used:raise ValueError('Unexpected/repeated isolated-singularity input')
        used.append(name)
        return history if expected[name]=='project-history' else texts[expected[name]]
    body=re.sub(r'\\(?:input|include)\s*\{([^}]+)\}',include,body)
    if used!=list(expected) or re.search(r'\\(?:input|include)\b',body):
        raise ValueError('isolated-singularity input graph/order changed')
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
            if label in labels:raise ValueError('Duplicate isolated-singularity label: '+label)
            if label in layout:
                topic=layout[label]['topic'];seen.add(label)
            if topic is None:raise ValueError('Label before reviewed isolated-singularity subject: '+label)
            labels[label]=topic
    if seen != set(layout):
        raise ValueError('Missing or reordered isolated-singularity subject boundary')
    exported_labels={label for r in records for label in [r['label'],*r.get('aliases',[])]}
    if exported_labels!=set(labels):
        raise ValueError('Incomplete isolated-singularity exported label coverage')
    for record in records:
        record['topic']=labels[record['label']]
        if any(labels[alias]!=record['topic'] for alias in record.get('aliases',[])):
            raise ValueError('Aliased labels cross reviewed subject boundaries')
        for field in ('html','proof_html'):
            if field in record:
                record[field]=re.sub(r'href="https://mingchenxia\.github\.io/Pome/tag/([A-F0-9]{8,12})/"',
                    lambda m:m[0]+' data-proof-entry="'+m[1]+'"',record[field])
    return records


if __name__=='__main__':
    configure(SLUG,'Isolated plurisubharmonic singularities',
              'https://github.com/MingchenXia/Gerby-Literature',
              author='Gerby Literature',bibliography=BIBLIOGRAPHY)
    export(Path(sys.argv[1]),Path(sys.argv[2]),prepare=prepare_article,transform=assign_topics)
