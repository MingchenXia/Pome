"""Export only the explicitly selected, fingerprinted Klimek source graph."""
import json
from hashlib import sha256
from pathlib import Path
import re
import sys

from common import configure, export, uncomment

SLUG = "klimek-pluripotential-theory"
ENTRYPOINT = "contributions/klimek-pluripotential-theory.tex"
MANIFEST = "integrations/S0003/source-manifest.json"
RESULTS = ("R0031",) + tuple(f"R{i:04d}" for i in range(34, 73)) + ("R0074", "R0075", "R0073", "R0076", "R0077", "R0078")
FRAGMENTS = {f"results/{r}/proof": f"results/{r}/proof.tex" for r in RESULTS}


def prepare_fragment(text, result):
    text = text.replace(r"\paragraph{Sources.}",
                        r"\noindent\textbf{Sources.}")
    # Give every previously unlabelled subject heading an explicit stable
    # namespace. Bibliographical prose is not a new reading section.
    count = 0
    pattern = r"\\(section|subsection|subsubsection)\*?\{[^{}]+\}"

    def heading(match):
        nonlocal count
        count += 1
        if text[match.end():].lstrip().startswith(r"\label{"):
            return match[0]
        return match[0] + rf"\label{{sec:klimek-{result.lower()}-{count}}}"

    return re.sub(pattern, heading, text)


def selected_text(source, name, manifest):
    path = (source / name).resolve()
    if not path.is_relative_to(source.resolve()) or not path.is_file():
        raise ValueError(f"Missing or escaping selected source file: {name}")
    data = path.read_bytes()
    if sha256(data).hexdigest() != manifest["files"].get(name):
        raise ValueError(f"Review the changed selected source file: {name}")
    return uncomment(data.decode("utf-8"))


def prepare_article(source):
    manifest = json.loads((source / MANIFEST).read_text())
    article = selected_text(source, ENTRYPOINT, manifest)
    preamble, body = article.split(r"\begin{document}", 1)
    if (r"\documentclass[11pt,a4paper]{article}" not in preamble
            or r"\newtheorem{theorem}{Theorem}[section]" not in preamble):
        raise ValueError("Review the selected article's class and numbering")
    used = []

    def include(match):
        name = match[1]
        if name not in FRAGMENTS or name in used:
            raise ValueError(f"Unreviewed or repeated selected input: {name}")
        used.append(name)
        text = selected_text(source, FRAGMENTS[name], manifest)
        if re.search(r"\\(?:input|include)\b", text):
            raise ValueError(f"Nested selected source input: {name}")
        return prepare_fragment(text, name.split("/")[1])

    body = re.sub(r"\\(?:input|include)\s*\{([^}]+)\}", include, body)
    if used != list(FRAGMENTS):
        raise ValueError("Review the selected input order and complete graph")
    if re.search(r"\\(?:input|include)\b", body):
        raise ValueError("Unexpanded selected source input")
    body = body.replace(r"\maketitle", "").replace(r"\tableofcontents", "")
    body = body.replace(r"\paragraph{Sources.}",
                        r"\noindent\textbf{Sources.}")
    body = re.sub(r"\\(?:bibliographystyle|bibliography)\{[^}]+\}", "", body)
    body = re.sub(r"\\begingroup\s*\\small\s*\\endgroup", "", body)
    # PDF layout packages have no role in the web parser. Preserve the
    # declared mathematical macros/environments without loading TeX-only
    # package implementations into plasTeX.
    declarations = [line for line in preamble.splitlines()
                    if line.startswith((r"\newtheorem", r"\newcommand"))]
    # aliascnt gives PDF cross-references their actual environment kind.
    # The web parser assigns kinds from the environments themselves and
    # only needs their shared numerical counter.
    declarations = [re.sub(
        r"(\\newtheorem\{(?:proposition|lemma|corollary|definition|example|remark)\})"
        r"\[(?:proposition|lemma|corollary|definition|example|remark)\]",
        lambda match: match[1] + "[theorem]", line)
        for line in declarations]
    web_preamble = (r"\documentclass{article}" + "\n"
                    + r"\usepackage{amsmath,amssymb,hyperref}" + "\n"
                    + "\n".join(declarations) + "\n")
    return web_preamble + r"\begin{document}" + "\n" + body


def assign_topics(source, records):
    manifest = json.loads((source / MANIFEST).read_text())
    layout = json.loads(selected_text(
        source, "integrations/S0003/section-layout.json", manifest))
    headings = {item["label"]: item["title"] for item in layout["sections"]}
    if len(headings) != len(layout["sections"]):
        raise ValueError("Repeated reviewed section heading")
    labels = {"sec:klimek-conventions": headings["sec:klimek-conventions"]}
    seen_headings = {"sec:klimek-conventions"}
    for result in RESULTS:
        text = prepare_fragment(
            selected_text(source, f"results/{result}/proof.tex", manifest), result)
        current = None
        for label in re.findall(r"\\label\{([^}]+)\}", text):
            if label in labels:
                raise ValueError(f"Duplicate selected label: {label}")
            if label in headings:
                current = headings[label]
                seen_headings.add(label)
            if current is None:
                raise ValueError(f"Label precedes its reviewed section: {label}")
            labels[label] = current
    if seen_headings != headings.keys():
        raise ValueError("Review complete selected section layout")
    if {record["label"] for record in records} != labels.keys():
        raise ValueError("Review all selected labels and subject assignments")
    canonical_link = re.compile(
        r'href="https://mingchenxia\.github\.io/(?:Pome|Gerby)/tag/([A-F0-9]{8,12})/"')
    for record in records:
        record["topic"] = labels[record["label"]]
        for field in ("html", "proof_html"):
            if field in record:
                record[field] = canonical_link.sub(
                    lambda match: match[0] + ' data-proof-entry="' + match[1] + '"',
                    record[field])
    return records


if __name__ == "__main__":
    configure(SLUG, "Local and global pluripotential theory: supplements after Klimek",
              "https://github.com/MingchenXia/Gerby-Literature",
              author="Gerby Literature preparation after Maciej Klimek",
              bibliography="contributions/klimek-pluripotential-theory.bib")
    export(Path(sys.argv[1]), Path(sys.argv[2]),
           prepare=prepare_article, transform=assign_topics)
