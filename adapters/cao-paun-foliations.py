"""Ordinary Pome adapter for the exactly reviewed Cao–Păun payload.

This template is inactive until an accepted source manifest and all selected
portable files exist. It reads only the exact public payload and that manifest.
The common exporter independently requires a real, clean source Git revision.
"""

from hashlib import sha256
from html import escape
import json
from pathlib import Path, PurePosixPath
import re
import subprocess
import sys

SLUG = "cao-paun-foliations"
PREFIX = "integrations/S0082"
ENTRY = f"contributions/{SLUG}.tex"
BIB = f"contributions/{SLUG}.bib"
LAYOUT = f"{PREFIX}/section-layout.json"
CANONICAL = f"{PREFIX}/canonical-references.json"
QUESTIONS = f"{PREFIX}/open-questions.tex"
HISTORY = f"{PREFIX}/project-history.tex"
MANIFEST = f"{PREFIX}/source-manifest.json"
HASH = re.compile(r"[a-f0-9]{64}\Z")
TAG = re.compile(r"[A-F0-9]{12}\Z")
LABEL = re.compile(r"\\label\s*\{([^{}]+)\}")
REF = re.compile(r"\\(?:[cC]ref|[cC]pageref|eqref|ref|pageref|autoref|nameref)\*?\s*\{([^{}]+)\}")
HEAD = re.compile(r"\\(?:part|chapter|section|subsection|subsubsection)\*?\s*\{")
POME = re.compile(r"https://mingchenxia\.github\.io/Pome/tag/([A-F0-9]{12})/\Z")
OPEN = {"conj:general-relative-canonical-psef": "conjecture",
        "q:mrc-cotangent-numerical-dimension": "question"}
CHAPTERS = {"singularities-regularization", "sections-okounkov", "positivity-cohomology",
            "complex-spaces", "problems-history", "historical-notes"}
CONVENTIONS = ("Ambient manifolds are connected unless stated otherwise. "
               "Fibers need not be connected; the section-envelope arguments "
               "treat their connected components separately.")
PRIVATE = re.compile(
    r"(?:library/(?:originals|inbox)|sources/S\d{4}/(?:research|reviews|export-plan)"
    r"|results/R\d{4}/(?:proof|record|history)|(?:^|[\s{\"/])(?:errata|tracking)/"
    r"|/workspace/|/tmp/|(?:file|sandbox):|private\s+(?:review|research|literature|draft|record)"
    r"|continuing\s+mathematical\s+review)", re.I)
UNSUPPORTED = re.compile(
    r"\\(?:catcode|csname|inputencoding|includeonly|openin|openout|read|write|newread|newwrite"
    r"|directlua|special|verbatiminput|lstinputlisting|includegraphics|graphicspath|subfile"
    r"|includepdf|externaldocument|import|subimport|InputIfFileExists|IfFileExists|verb|VerbatimInput)\b"
    r"|\\begin\{(?:verbatim\*?|Verbatim|lstlisting|filecontents\*?)\}", re.I)


def require(condition, message):
    if not condition:
        raise ValueError(message)


def digest(data):
    return sha256(data).hexdigest()


def parse_json(data):
    def unique(pairs):
        result = {}
        for key, value in pairs:
            require(key not in result, "Repeated JSON key: " + key)
            result[key] = value
        return result
    return json.loads(data, object_pairs_hook=unique)


def path_for(source, name):
    require(isinstance(name, str) and name and "\\" not in name and "\0" not in name,
            "Invalid portable path")
    rel = PurePosixPath(name)
    require(not rel.is_absolute() and ".." not in rel.parts and rel.as_posix() == name,
            "Noncanonical portable path")
    path = source
    for part in rel.parts:
        path = path / part
        require(not path.is_symlink(), "Symlink in portable path")
    require(path.resolve().is_relative_to(source.resolve()) and path.is_file(),
            "Missing or escaping portable file: " + name)
    return path


def uncomment(text):
    lines = []
    for line in text.splitlines(keepends=True):
        for i, char in enumerate(line):
            if char != "%":
                continue
            j = i - 1
            while j >= 0 and line[j] == "\\":
                j -= 1
            if (i - j - 1) % 2 == 0:
                line = line[:i] + ("\n" if line.endswith("\n") else "")
                break
        lines.append(line)
    return "".join(lines)


def review_bound(review, dated=False):
    require(isinstance(review, dict) and review.get("status") == "accepted"
            and isinstance(review.get("reviewer"), str) and review["reviewer"].strip()
            and isinstance(review.get("evidence"), list) and review["evidence"],
            "Missing accepted review binding")
    if dated:
        require(isinstance(review.get("checked_at"), str) and review["checked_at"].strip(),
                "Missing dated review binding")
    for row in review["evidence"]:
        require(isinstance(row, dict) and isinstance(row.get("path"), str)
                and HASH.fullmatch(str(row.get("sha256", ""))), "Unbound review evidence")


def manifest_for(source):
    manifest = parse_json(path_for(source, MANIFEST).read_bytes())
    require(isinstance(manifest, dict) and manifest.get("version") == 1
            and manifest.get("source_slug") == SLUG and manifest.get("status") == "reviewed-export",
            "No final reviewed Cao–Păun source manifest")
    results = manifest.get("results")
    require(isinstance(results, list) and results and all(isinstance(r, str) for r in results)
            and len(results) == len(set(results))
            and set(results) <= {f"R{i:04d}" for i in range(205, 217)}, "Invalid selected results")
    paths = {r: f"contributions/{SLUG}/{r}.tex" for r in results}
    require(manifest.get("proof_paths") == paths, "Changed selected proof paths")
    expected = {ENTRY, BIB, LAYOUT, CANONICAL, QUESTIONS, HISTORY, *paths.values()}
    files = manifest.get("files")
    require(isinstance(files, dict) and set(files) == expected
            and all(HASH.fullmatch(str(h)) for h in files.values()), "Changed exact public allowlist")
    inputs = manifest.get("payload_input_sha256")
    require(isinstance(inputs, dict) and set(inputs) == expected
            and all(HASH.fullmatch(str(h)) for h in inputs.values()), "Missing exact input hashes")
    review_bound(manifest.get("selection_review"), dated=True)
    reviews, transforms = manifest.get("result_reviews"), manifest.get("proof_transformations")
    require(isinstance(reviews, dict) and set(reviews) == set(results)
            and isinstance(transforms, dict) and set(transforms) == set(results),
            "Incomplete proof reviews or transformations")
    for result in results:
        item, names = transforms[result], []
        require(isinstance(item, dict) and item.get("transformation") in ("verbatim", "uncomment")
                and item.get("portable_proof_sha256") == files[paths[result]]
                and item.get("research_proof_sha256") == inputs[paths[result]],
                "Changed accepted proof transformation: " + result)
        for role in ("root_review", "independent_review"):
            review = reviews[result].get(role)
            review_bound(review)
            require(review.get("accepted_proof_sha256") == item["research_proof_sha256"],
                    "Review does not bind accepted original proof: " + result)
            names.append(review["reviewer"])
        require(names[0] != names[1], "Independent reviewer must differ from root")
    return manifest


def require_committed_payload(source, names):
    """Bind every exported byte, including the manifest, to the real HEAD.

    The shared exporter's clean-diff check does not see untracked files.
    Reading each selected path from HEAD closes that provenance gap without
    modifying the shared exporter or trusting the working-tree manifest alone.
    """
    command = ["git", "-C", str(source)]
    head = subprocess.run(command + ["rev-parse", "--verify", "HEAD"],
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    require(head.returncode == 0, "Reviewed source has no committed Git HEAD")
    revision = head.stdout.decode("ascii").strip()
    require(re.fullmatch(r"[a-f0-9]{40}", revision), "Invalid committed source revision")
    for name in sorted(names):
        path = path_for(source, name)
        committed = subprocess.run(command + ["show", f"{revision}:{name}"],
                                   stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        require(committed.returncode == 0,
                "Reviewed source file is absent from HEAD: " + name)
        require(committed.stdout == path.read_bytes(),
                "Reviewed source file differs from HEAD: " + name)
    return revision


def file_commands(text, command):
    token = re.compile(r"\\" + command + r"\b")
    matches = list(re.finditer(r"\\" + command + r"\s*\{([^{}\\]+)\}", text))
    require(len(matches) == len(token.findall(text)), "Only literal braced file commands are allowed")
    return [m[1].strip() for m in matches]


def tex_path(name):
    return name if name.endswith(".tex") else name + ".tex"


def headings(text):
    result = []
    for match in HEAD.finditer(text):
        start, depth, pos = match.end(), 1, match.end()
        while pos < len(text) and depth:
            if text[pos] == "\\":
                token = re.match(r"\\(?:[A-Za-z@]+|.)", text[pos:])
                pos += len(token[0]) if token else 1
                continue
            depth += (text[pos] == "{") - (text[pos] == "}")
            pos += 1
        require(depth == 0, "Unclosed subject title")
        label = re.match(r"\s*\\label\s*\{([^{}]+)\}", text[pos:])
        require(label is not None, "Subject heading lacks a stable label")
        result.append((label[1], text[start:pos - 1]))
    return result


def canonical_tags(text):
    found = set()
    for url in re.findall(r"https?://[^\s{}<>\"\\]+", text):
        if "mingchenxia.github.io/pome" in url.lower():
            match = POME.fullmatch(url)
            require(match is not None, "Malformed or unbound canonical URL")
            found.add(match[1])
    for target in re.findall(r"\\(?:href|url)\s*\{([^{}]*)\}", text):
        if "pome/tag" in target.lower() or target.startswith("tag/"):
            require(POME.fullmatch(target) is not None, "Unsupported canonical link")
    return found


def source_conventions(material):
    """Read the reviewed global hypothesis without dropping front matter.

    The shared renderer exports labelled mathematical fragments, so prose
    before the first section is absent from their HTML. Bind the unchanged
    native convention explicitly and retain it with each reading context.
    """
    entry = material[ENTRY]
    require(entry.count(r"\begin{document}") == 1, "Changed portable entrypoint")
    preamble, body = entry.split(r"\begin{document}", 1)
    declarations = re.findall(r"\\newcommand\{\\caopaunconventions\}\{([^{}\\]+)\}", preamble)
    require(len(declarations) == 1 and " ".join(declarations[0].split()) == CONVENTIONS
            and preamble.count(r"\caopaunconventions") == 1
            and body.count(r"\caopaunconventions") == 1,
            "Missing or changed reviewed source conventions")
    return CONVENTIONS


def selected_material(source):
    manifest = manifest_for(source)
    require_committed_payload(source, {MANIFEST, *manifest["files"]})
    material = {}
    for name, expected in manifest["files"].items():
        data = path_for(source, name).read_bytes()
        require(digest(data) == expected, "Reviewed payload changed: " + name)
        text = data.decode("utf-8")
        require(PRIVATE.search(text) is None, "Private material in portable payload")
        material[name] = uncomment(text) if name.endswith(".tex") else text
    texts = {name: text for name, text in material.items() if name.endswith(".tex")}
    results, paths = manifest["results"], manifest["proof_paths"]
    graph_order = [ENTRY, *(paths[r] for r in results), QUESTIONS, HISTORY]
    expected_inputs = graph_order[1:]
    require([tex_path(v) for v in file_commands(texts[ENTRY], "input")] == expected_inputs
            and not file_commands(texts[ENTRY], "include"), "Changed portable graph order")
    require(file_commands(texts[ENTRY], "bibliography") == [BIB[:-4]], "Changed bibliography graph")
    for name, text in texts.items():
        require(UNSUPPORTED.search(text) is None, "Unsupported dynamic/file-reading TeX")
        if name != ENTRY:
            require(not any(file_commands(text, cmd) for cmd in ("input", "include", "bibliography")),
                    "Nested portable input")
    labels = [label for text in texts.values() for label in LABEL.findall(text)]
    require(len(labels) == len(set(labels)), "Duplicate portable label")
    local = set(labels)
    require(not ({v.strip() for text in texts.values() for group in REF.findall(text)
                  for v in group.split(",")} - local), "Unresolved portable reference")
    owners = {label: result for result in results for label in LABEL.findall(texts[paths[result]])}
    positions = {result: i for i, result in enumerate(results)}
    for result in results:
        for group in REF.findall(texts[paths[result]]):
            for label in map(str.strip, group.split(",")):
                other = owners.get(label)
                require(not other or other == result or positions[other] < positions[result],
                        "Portable proof precedes its explicit prerequisite")
    pattern = re.compile(r"\\begin\{(question|conjecture)\}(?:\[[^\]]*\])?\s*\\label\s*\{([^{}]+)\}[\s\S]*?\\end\{\1\}")
    blocks = list(pattern.finditer(texts[QUESTIONS]))
    require({m[2]: m[1] for m in blocks} == OPEN and len(blocks) == 2, "Changed open-statement scope")
    open_receipt = {m[2]: {"kind": m[1], "status": "open", "sha256": digest(m[0].encode())} for m in blocks}
    require(manifest.get("open_statements") == open_receipt, "Open-statement text or status changed")
    require(sum(len(pattern.findall(text)) for text in texts.values()) == 2, "Unexpected open statement")

    layout = parse_json(material[LAYOUT])
    require(isinstance(layout, dict) and layout.get("version") == 1
            and layout.get("source_slug") == SLUG and isinstance(layout.get("sections"), list),
            "Invalid subject layout")
    actual = [row for name in graph_order for row in headings(texts[name])]
    rows = layout["sections"]
    require(len(rows) == len(actual), "Incomplete subject layout")
    for row, (label, title) in zip(rows, actual):
        require(set(row) == {"label", "title_tex", "chapter"} and row["label"] == label
                and row["title_tex"] == title and row["chapter"] in CHAPTERS,
                "Changed subject boundary or order")
        require("\\" not in title, "A TeX subject title needs an explicit reviewed plain-text adapter extension")
    by_label = {row["label"]: row for row in rows}

    public = parse_json(material[CANONICAL])
    require(isinstance(public, dict) and public.get("version") == 1 and public.get("source_slug") == SLUG,
            "Invalid canonical public map")
    uses = {}
    for name in [*texts, BIB]:
        result = next((r for r in results if name == paths[r]), None)
        consumer = result or {ENTRY: "entrypoint", BIB: "bibliography", QUESTIONS: "questions", HISTORY: "history"}[name]
        for tag in canonical_tags(material[name]):
            uses.setdefault(tag, {})[consumer] = manifest["payload_input_sha256"][name]
    references, reviews = public.get("references"), manifest.get("canonical_reviews")
    require(isinstance(references, dict) and set(references) == set(uses)
            and isinstance(reviews, dict) and set(reviews) == set(uses), "Incomplete canonical-consumer map")
    for tag, consumers in uses.items():
        row = references[tag]
        require(TAG.fullmatch(tag) and row.get("url") == f"https://mingchenxia.github.io/Pome/tag/{tag}/"
                and row.get("consumers") == consumers and HASH.fullmatch(str(row.get("statement_sha256", ""))),
                "Changed canonical statement or consumer scope")
        source_row = row.get("source", {})
        require(set(source_row) == {"book", "revision", "label"}
                and re.fullmatch(r"[a-f0-9]{40}", str(source_row.get("revision", "")))
                and all(isinstance(v, str) and v for v in source_row.values()), "Invalid canonical source identity")
        review_bound(reviews[tag], dated=True)
    source_conventions(material)
    return manifest, material, by_label, graph_order


def prepare_article(source):
    _, material, _, order = selected_material(source)
    article = material[ENTRY]
    require(article.count(r"\begin{document}") == 1, "Changed portable entrypoint")
    preamble, body = article.split(r"\begin{document}", 1)
    require(r"\newtheorem{theorem}{Theorem}[section]" in preamble,
            "Review native theorem counter declarations")
    body = re.sub(r"\\input\s*\{([^{}]+)\}", lambda m: material[tex_path(m[1])], body)
    body = body.replace(r"\maketitle", "").replace(r"\tableofcontents", "")
    body = re.sub(r"\\(?:bibliographystyle|bibliography)\s*\{[^{}]+\}", "", body)
    body = re.sub(r"\b(?:[Tt]heorems?|[Ll]emmas?|[Pp]ropositions?|[Cc]orollar(?:y|ies)|"
                  r"[Dd]efinitions?|[Ee]xamples?)\s*(?:~\s*)?(?=\\[cC]ref\*?\s*\{)", "", body)
    declarations = [line for line in preamble.splitlines() if line.startswith((r"\newtheorem", r"\newcommand"))]
    # Unlike the earlier isolated-singularity adapter, preserve the two open
    # environment kinds while normalizing native alias counters for Gerby.
    declarations = [re.sub(
        r"(\\newtheorem\{(?:proposition|lemma|corollary|definition|example|remark|question|conjecture)\})"
        r"\[(?:proposition|lemma|corollary|definition|example|remark|question|conjecture)\]",
        lambda m: m[1] + "[theorem]", line) for line in declarations]
    return "\\documentclass{article}\n\\usepackage{amsmath,amssymb,hyperref}\n" + "\n".join(declarations) + "\n\\begin{document}\n" + body


# Exact source and renderer bindings for the reviewed 64-record context map.
READER_CONTEXT = json.loads(r'''
{
  "version": 1,
  "audit_sha256": "b07c5e466fa71657719ffdc02a9dee9c92f22450c8085c76016366b1d2b325ab",
  "source_sha256": {
    "contributions/cao-paun-foliations/R0205.tex": "75760db9ef041d405685edf9b680f47c1f425f96d463f799a115af3f7e6f84c4",
    "contributions/cao-paun-foliations/R0206.tex": "3edcb6477330225f02068c3318d5c9d8cf8d372a8a33ebb19dbc2604add6b6d2",
    "contributions/cao-paun-foliations/R0207.tex": "6cc2d374c9d96d53f9d7f43cfd355e11ad25daec7e47f9847f8c77f0e690d782",
    "contributions/cao-paun-foliations/R0208.tex": "a52c18a755d8200ffec8fd135d5fd8bdaeb7892891ec7195426802573686ec60",
    "contributions/cao-paun-foliations/R0209.tex": "8550b5d3a71d064871fdcd4ba660d30f4cc4349a087f8142fee663726d84c1c0",
    "contributions/cao-paun-foliations/R0210.tex": "730cdc7976831e4c6e8c26fc9bbfa7339c5812e33e1135ade15915af19458c83",
    "contributions/cao-paun-foliations/R0211.tex": "23524457d865c653365c2a66a9645a385ee46152b8d5dad2689750bed0e7480b",
    "contributions/cao-paun-foliations/R0212.tex": "c5411590b8fdbfb8a40373081d16dfb0aa61a63f1d6b179947759cb9bb221aa2",
    "contributions/cao-paun-foliations/R0213.tex": "0e98e611ff29e5d03bca5f2f1bb2249b40425a6e3b700af48c20e41faa5f8d98",
    "contributions/cao-paun-foliations/R0214.tex": "c00162efe64d67c02cf5341eb0a20a47e3f1ec2b221c1158fde1fead34b9c39f",
    "contributions/cao-paun-foliations/R0215.tex": "9c9a82bdde5b4901d161f7d3f0c03aff7357efca8144fe46c67929598c88ecfe",
    "contributions/cao-paun-foliations/R0216.tex": "a57a6759c3cce9000a870afc622eef7fc29ec95ce58c380953f67a37a0a703dd",
    "integrations/S0082/open-questions.tex": "0e976e1ec4bf6aac9899d10447daffeb65bc01ab7abb893eb180873091cadb0e"
  },
  "native_fragments": {
    "lelong-conventions": {
      "source_path": "contributions/cao-paun-foliations/R0205.tex",
      "first_line": 4,
      "last_line": 8,
      "sha256": "abcd9d4fc2ae1074a01bcad705e35629282a1861a70763cdf1787cafeffe3f60"
    },
    "circular-mean": {
      "source_path": "contributions/cao-paun-foliations/R0205.tex",
      "first_line": 10,
      "last_line": 20,
      "sha256": "58ce98b675ed5de4d8eff22f200572e5467e3470ab05f863444e366a12f0250e"
    },
    "blowup-setting": {
      "source_path": "contributions/cao-paun-foliations/R0205.tex",
      "first_line": 23,
      "last_line": 31,
      "sha256": "f2ff2605049543893a2a17027b215edc26e0e44912f6b349775d1e16cf88c7b0"
    },
    "generic-line": {
      "source_path": "contributions/cao-paun-foliations/R0205.tex",
      "first_line": 96,
      "last_line": 98,
      "sha256": "a74e4dddbde9d77924e2f9379c558cfa32f1cf09f852a7ccb55034820c27d27f"
    },
    "flat-envelope-setting": {
      "source_path": "contributions/cao-paun-foliations/R0206.tex",
      "first_line": 5,
      "last_line": 20,
      "sha256": "867a95d1bf7bf870f09ee2eca8d40b6fc64709294a8c2d0691790bc30961940c"
    },
    "flat-normalization-construction": {
      "source_path": "contributions/cao-paun-foliations/R0206.tex",
      "first_line": 38,
      "last_line": 69,
      "sha256": "9fc1554dd8875455b78f08375cb1a12257423e938d85c58eebfc7f7914924a17"
    },
    "flat-invariant-ratio": {
      "source_path": "contributions/cao-paun-foliations/R0206.tex",
      "first_line": 74,
      "last_line": 80,
      "sha256": "d697d50e9226f2708a4e918a49597f22075620a631df80897ab98c51dd105cf3"
    },
    "relative-map-and-ramification": {
      "source_path": "contributions/cao-paun-foliations/R0207.tex",
      "first_line": 58,
      "last_line": 65,
      "sha256": "332622917ec60c8ab5c759a104cded8685042e9e0c3d8b8fa0478d985cb17786"
    },
    "multiplier-weight": {
      "source_path": "contributions/cao-paun-foliations/R0208.tex",
      "first_line": 4,
      "last_line": 4,
      "sha256": "ed796bf911225cf094d704c25c3a812231b409ea47b16419a6e5023179f28a8b"
    },
    "diagonal-weight-setting": {
      "source_path": "contributions/cao-paun-foliations/R0208.tex",
      "first_line": 7,
      "last_line": 12,
      "sha256": "1570e260a35bcdfc13efd6e5000cd4289df03334deab4b8fbf4d0f232cb3bbc2"
    },
    "normalized-pole-model": {
      "source_path": "contributions/cao-paun-foliations/R0208.tex",
      "first_line": 60,
      "last_line": 71,
      "sha256": "ea3f1e100331a8a3beb6ea0b9206fd8e322fcb8ff78a3fa0bdd4c71cfe467872"
    },
    "concentration-setting": {
      "source_path": "contributions/cao-paun-foliations/R0208.tex",
      "first_line": 91,
      "last_line": 99,
      "sha256": "a6570b2c50ba2e2fd015f27b788b686c611fee447c730f9908410885afee7214"
    },
    "concentration-construction": {
      "source_path": "contributions/cao-paun-foliations/R0208.tex",
      "first_line": 102,
      "last_line": 119,
      "sha256": "e1cc19a7d4b23920284285d4e5ee7f2107e4c9e8072a43bdb251fffa359918c9"
    },
    "pole-limit-construction": {
      "source_path": "contributions/cao-paun-foliations/R0208.tex",
      "first_line": 128,
      "last_line": 144,
      "sha256": "1af67bd1844da33dcd4d8357f2964611b58feae99d16e473c5d19cb79bcd2b47"
    },
    "pole-bound": {
      "source_path": "contributions/cao-paun-foliations/R0208.tex",
      "first_line": 145,
      "last_line": 149,
      "sha256": "6a9bb45930982a74bc34b3a9c14e745660748978158116d0fe1d78d999a58eb1"
    },
    "vanishing-order-construction": {
      "source_path": "contributions/cao-paun-foliations/R0208.tex",
      "first_line": 151,
      "last_line": 165,
      "sha256": "1d3a549b6743eced1cbed998cf215169bd7b34c4af3dfe9d8bc5244704e6cab7"
    },
    "compact-center-setting": {
      "source_path": "contributions/cao-paun-foliations/R0209.tex",
      "first_line": 10,
      "last_line": 22,
      "sha256": "2f26a120ccd1f0c1965bd2fade3ce1548b11eaed06bb432895f79efc5ce735ab"
    },
    "compact-center-coefficient": {
      "source_path": "contributions/cao-paun-foliations/R0209.tex",
      "first_line": 25,
      "last_line": 33,
      "sha256": "0652decb7326cdb3895eddc1522d0c37645d5f321b21ed5b9ce291928eed7b9a"
    },
    "compact-center-model": {
      "source_path": "contributions/cao-paun-foliations/R0209.tex",
      "first_line": 35,
      "last_line": 52,
      "sha256": "e8a8fe86f537366c16d23b5c569fedd26fd7f0033c4a2e0ae6a64b7937f1a9db"
    },
    "compact-center-currents": {
      "source_path": "contributions/cao-paun-foliations/R0209.tex",
      "first_line": 54,
      "last_line": 76,
      "sha256": "419705c51be3940fa26961405c0ae414ea4c2f89aa632caf4f021b6d6cd396a0"
    },
    "compact-center-extension": {
      "source_path": "contributions/cao-paun-foliations/R0209.tex",
      "first_line": 78,
      "last_line": 115,
      "sha256": "5f2884c69ff7870cb44d6a3f070d1502370e3f95de4d4d0913eca6d704f9a0d7"
    },
    "conormal-approximate-definition": {
      "source_path": "contributions/cao-paun-foliations/R0210.tex",
      "first_line": 4,
      "last_line": 11,
      "sha256": "46fc1a150887fee54d04e1a3d1ce7f9c2dd4f28f94c17294a5c48e6b3f8306cd"
    },
    "conormal-theorem-setting": {
      "source_path": "contributions/cao-paun-foliations/R0210.tex",
      "first_line": 14,
      "last_line": 20,
      "sha256": "f5293ec44f333e24950d842866d6b5b04b35e169f8092562780671775289dcaa"
    },
    "leaf-relation-setting": {
      "source_path": "contributions/cao-paun-foliations/R0210.tex",
      "first_line": 148,
      "last_line": 167,
      "sha256": "7785ea0146f7b1364ea47ec840c33a5392a7f8e5cc0a27fc7e7a67f236fe7fab"
    },
    "degree-and-slope-definition": {
      "source_path": "contributions/cao-paun-foliations/R0211.tex",
      "first_line": 4,
      "last_line": 16,
      "sha256": "a1b400ad9b4d9739b9bbafbfaa1ba4cd1e176b2a65a5bb34501ddbae4c2c60fd"
    },
    "movable-cone-definition": {
      "source_path": "contributions/cao-paun-foliations/R0211.tex",
      "first_line": 22,
      "last_line": 29,
      "sha256": "10fcba8fd44e30dfc55c6d4347d8aab4c1b90a45da421a9d250fac98ae43c333"
    },
    "tensor-semistability-input": {
      "source_path": "contributions/cao-paun-foliations/R0211.tex",
      "first_line": 140,
      "last_line": 150,
      "sha256": "80ff6a7f554f04c4917efdad286817eb0bfca66e35b88ebb7e5027f19e6acfb7"
    },
    "tautological-approximate-definition": {
      "source_path": "contributions/cao-paun-foliations/R0212.tex",
      "first_line": 4,
      "last_line": 14,
      "sha256": "47af7de2eea9c40a7215feb602e5e852c1772e80ba3f8b1abfa73e370896537a"
    },
    "two-forms-native-scope": {
      "source_path": "contributions/cao-paun-foliations/R0213.tex",
      "first_line": 21,
      "last_line": 26,
      "sha256": "1e492ed4aba900a2bf9fd4405202def1dd4e6ff198e6bdd5b16ba978f5ef0e5a"
    },
    "foliation-main-scope": {
      "source_path": "contributions/cao-paun-foliations/R0213.tex",
      "first_line": 48,
      "last_line": 52,
      "sha256": "c248668e1ecad627a181b044d3cc2eaed3d7a01e6d766b9000ae5c0491e583aa"
    },
    "numerical-dimension-definition": {
      "source_path": "contributions/cao-paun-foliations/R0214.tex",
      "first_line": 4,
      "last_line": 44,
      "sha256": "3d60dcf26693ee4d2e712a1e53bb5ded296562c3eaf9678ef20ddc5e36fce822"
    },
    "uniruled-definition": {
      "source_path": "contributions/cao-paun-foliations/R0214.tex",
      "first_line": 107,
      "last_line": 113,
      "sha256": "660aa507ec1d26cf5f00bd1e6bf279898a372a01726854fe6b51460e67a71ca6"
    },
    "cone-duality-reference": {
      "source_path": "contributions/cao-paun-foliations/R0214.tex",
      "first_line": 74,
      "last_line": 83,
      "sha256": "8220210b2320f25bf61ddf0b76cd15fb696d1ef0f2988e1f1d87ce7643bd0b56"
    },
    "fujiki-deformation-input": {
      "source_path": "contributions/cao-paun-foliations/R0215.tex",
      "first_line": 4,
      "last_line": 12,
      "sha256": "1ffda0604d5f9b7e7dae624d39259527fc2dabe4e2f31cb021650c82e148ce71"
    },
    "conjecture-status": {
      "source_path": "integrations/S0082/open-questions.tex",
      "first_line": 10,
      "last_line": 13,
      "sha256": "532fe8f6f2f556e4b06d21cc5a52dd6b2960bf3d79586d03326a75594a088012"
    },
    "question-status": {
      "source_path": "integrations/S0082/open-questions.tex",
      "first_line": 20,
      "last_line": 20,
      "sha256": "32f596213f2dd276ccebaceadbed7c0f7ea18358000dbdb506e12df8c92b8727"
    },
    "concentration-solution": {
      "source_path": "contributions/cao-paun-foliations/R0208.tex",
      "first_line": 120,
      "last_line": 126,
      "sha256": "850a6537e9c021454e0c296f723661e8e0ddbd43feee1c61ebb9236288c877f0"
    },
    "compact-center-inequality-lead": {
      "source_path": "contributions/cao-paun-foliations/R0209.tex",
      "first_line": 117,
      "last_line": 118,
      "sha256": "c41053ddc7e1c21b5ca78284d906f4b1a341670d5e9abc92fa2da53e08e5ae5f"
    },
    "free-curve-statement": {
      "source_path": "contributions/cao-paun-foliations/R0214.tex",
      "first_line": 115,
      "last_line": 121,
      "sha256": "a2f83d7b69f2c26e6152ffa599faab8d3054ef70750cd056ac3c69241d9cf8d4"
    }
  },
  "blocks": {
    "lelong-conventions": {
      "source_label": "sec:blowup-restricted-lelong",
      "source_path": "contributions/cao-paun-foliations/R0205.tex",
      "scope": "section-prose",
      "atom_count": 4,
      "atoms": [
        {
          "index": 0,
          "sha256": "6980ab910a9d29c4b5129cbfaa75626edfab78727f4897edaa5e52d0cc8c4b73"
        }
      ],
      "native_fragments": [
        "lelong-conventions"
      ]
    },
    "lelong-normalization": {
      "source_label": "sec:blowup-restricted-lelong",
      "source_path": "contributions/cao-paun-foliations/R0205.tex",
      "scope": "section-prose",
      "atom_count": 4,
      "atoms": [
        {
          "index": 0,
          "sha256": "6980ab910a9d29c4b5129cbfaa75626edfab78727f4897edaa5e52d0cc8c4b73",
          "slice": [
            0,
            83
          ]
        }
      ],
      "native_fragments": [
        "lelong-conventions"
      ]
    },
    "circular-mean": {
      "source_label": "sec:blowup-restricted-lelong",
      "source_path": "contributions/cao-paun-foliations/R0205.tex",
      "scope": "section-prose",
      "atom_count": 4,
      "atoms": [
        {
          "index": 1,
          "sha256": "baa24ef6589b04ac8101f9860db7c79a66d65357a2d65fee09c1bf4324a0e023"
        },
        {
          "index": 2,
          "sha256": "879fb1ab9cd8cace2789900d7082e9aa2db6974a2f9b7477d7ffecd59707259b"
        },
        {
          "index": 3,
          "sha256": "d86c5378a3dd33c0b2620a9e2a4b6e89d0d18977ca8550d0d2d5f5400e7a1d11"
        }
      ],
      "native_fragments": [
        "circular-mean"
      ]
    },
    "blowup-setting": {
      "source_label": "prop:smooth-blowup-lelong-factor-two",
      "source_path": "contributions/cao-paun-foliations/R0205.tex",
      "scope": "statement",
      "atom_count": 3,
      "atoms": [
        {
          "index": 0,
          "sha256": "555ef5d68449caebd10dd2ecef4916170ea129ace9ab62e5cb662f02b8c4ee80",
          "slice": [
            0,
            74
          ]
        }
      ],
      "native_fragments": [
        "blowup-setting"
      ]
    },
    "flat-envelope-setting": {
      "source_label": "thm:flat-twist-adjoint-envelope",
      "source_path": "contributions/cao-paun-foliations/R0206.tex",
      "scope": "statement",
      "atom_count": 3,
      "atoms": [
        {
          "index": 0,
          "sha256": "3fc880b0241274003968d6c9527191039f1a339958a6f98201e4db7b1257b7e3"
        },
        {
          "index": 1,
          "sha256": "f30efaae1386385cfc53608e1a0047d5bf6bb4ca9c02bb4aab302b5c1750cf33"
        },
        {
          "index": 2,
          "sha256": "480e1a19869c65cdb8c14726d03eb01e973aa409c2f361f694a838018f2113e6",
          "slice": [
            0,
            60
          ]
        }
      ],
      "native_fragments": [
        "flat-envelope-setting"
      ]
    },
    "flat-normalization-construction": {
      "source_label": "thm:flat-twist-adjoint-envelope",
      "source_path": "contributions/cao-paun-foliations/R0206.tex",
      "scope": "proof",
      "atom_count": 15,
      "atoms": [
        {
          "index": 2,
          "sha256": "f983e730d8beb3cd2b0e74fdf16f3f53a6768e029c19d377ccc4279726f39398"
        },
        {
          "index": 3,
          "sha256": "61d0bd8be3839bc15e02d6e490cfa58cf8ab1c61760e5d7abc8477f266f87cbe"
        },
        {
          "index": 4,
          "sha256": "81e765b8be96b6e53910584bd70859cd117d5ad1a3011c9a1a526cc968b43fed"
        },
        {
          "index": 5,
          "sha256": "3cfebf766bb9b62c5b57fed941621444499fae77e2dc0e30a520c86ef2e4e808"
        },
        {
          "index": 6,
          "sha256": "61738bf203c0e908d58ea4596a93aba9482979723a5203b9aa365ab66c90714f"
        }
      ],
      "native_fragments": [
        "flat-normalization-construction"
      ]
    },
    "flat-invariant-ratio": {
      "source_label": "thm:flat-twist-adjoint-envelope",
      "source_path": "contributions/cao-paun-foliations/R0206.tex",
      "scope": "proof",
      "atom_count": 15,
      "atoms": [
        {
          "index": 8,
          "sha256": "16292e856aa489d126c6a383842069f27039416bf3bb217975ae0d79e32854f4",
          "slice": [
            0,
            76
          ]
        }
      ],
      "native_fragments": [
        "flat-invariant-ratio"
      ]
    },
    "relative-map-and-ramification": {
      "source_label": "sec:relative-canonical-positivity",
      "source_path": "contributions/cao-paun-foliations/R0207.tex",
      "scope": "section-prose",
      "atom_count": 4,
      "atoms": [
        {
          "index": 1,
          "sha256": "f37e660caa00ff88dcec7837a8b34d8271f2e6970b2eec31b7d0e7188ba5acb8"
        },
        {
          "index": 2,
          "sha256": "ce687d68a4ee8d62be0ab2539c5e6e9b39f4aff3a39868fc6ece7089f825d7cf"
        },
        {
          "index": 3,
          "sha256": "4ec01d39b67b9d68a01ecb1207284551962e264df4a2143a94b2244bd9b342ad"
        }
      ],
      "native_fragments": [
        "relative-map-and-ramification"
      ]
    },
    "multiplier-weight": {
      "source_label": "sec:diagonal-multiplier-weights",
      "source_path": "contributions/cao-paun-foliations/R0208.tex",
      "scope": "section-prose",
      "atom_count": 1,
      "atoms": [
        {
          "index": 0,
          "sha256": "2f70be56961f3c1ac1257b207c1fa8b843c11f76a2a0b1b6015d3c811c91dbdf"
        }
      ],
      "native_fragments": [
        "multiplier-weight"
      ]
    },
    "diagonal-weight-setting": {
      "source_label": "lem:diagonal-monomial-multiplier-ideal",
      "source_path": "contributions/cao-paun-foliations/R0208.tex",
      "scope": "statement",
      "atom_count": 5,
      "atoms": [
        {
          "index": 0,
          "sha256": "a2697faa8e841262ef10a74946184c967362bf85ce5dd605a42fc28d48f1aa23"
        },
        {
          "index": 1,
          "sha256": "df88824447d2de580403016e6ee2ebd3d7dfc5d95ebcf632601c2786aac7e221"
        },
        {
          "index": 2,
          "sha256": "da047a467e33099bbd8c961c00436162935d17e583b4a2aced979467644db1ec"
        }
      ],
      "native_fragments": [
        "diagonal-weight-setting"
      ]
    },
    "normalized-pole-model": {
      "source_label": "lem:normalized-diagonal-pole-mass",
      "source_path": "contributions/cao-paun-foliations/R0208.tex",
      "scope": "statement",
      "atom_count": 5,
      "atoms": [
        {
          "index": 0,
          "sha256": "a98d6764af3c42d417837f67a83a48ba378700f01741aa7c4ebdc11529981231"
        },
        {
          "index": 1,
          "sha256": "47c21ce27877b7402544a034d44237430301429780380148b42e86c6445439c2"
        },
        {
          "index": 2,
          "sha256": "1e2a66a9942e937050e7afa8d979d1c2046c1cbb04adac9c18d293aa2dfb04e1"
        },
        {
          "index": 3,
          "sha256": "4dd3dfa5d89448e40840d15b423be703c52c35129eb1f2cbc457647a0c556b30"
        },
        {
          "index": 4,
          "sha256": "d8fb8ae8626b7d5baea8f2aa9eb8492af6d8035322d0aecc1acb6df1b8f28384"
        }
      ],
      "native_fragments": [
        "normalized-pole-model"
      ]
    },
    "concentration-setting": {
      "source_label": "prop:anisotropic-global-concentration",
      "source_path": "contributions/cao-paun-foliations/R0208.tex",
      "scope": "statement",
      "atom_count": 2,
      "atoms": [
        {
          "index": 0,
          "sha256": "0a03ff342884a8fae158f5a71086fdb62013407b45a5a5189620b45ef5a3d6b9"
        },
        {
          "index": 1,
          "sha256": "f693b10e0de610176f4ddba1bb59d55e5984975e4a708d1f0d92695dcab5189f"
        }
      ],
      "native_fragments": [
        "concentration-setting"
      ]
    },
    "concentration-construction": {
      "source_label": "prop:anisotropic-global-concentration",
      "source_path": "contributions/cao-paun-foliations/R0208.tex",
      "scope": "proof",
      "atom_count": 20,
      "atoms": [
        {
          "index": 0,
          "sha256": "d7e0cacf15b8a8e3cf93041f22528a95259b0793679f337455e89ec4fe86ccf6"
        },
        {
          "index": 1,
          "sha256": "1312c743f1cfda379c307cad45dfd019d90b597915af90008ffc73a737f24ebb"
        },
        {
          "index": 2,
          "sha256": "2a196378503c79d1ff7e3dda86a86f5c526716c69397f1575b651ee964ab6ee9"
        },
        {
          "index": 3,
          "sha256": "2968346dfa591190fdadc2ee90d5dbc7511d552bbfc05d8f1b52d4659661be79"
        },
        {
          "index": 4,
          "sha256": "20a4ad722dddf192e213fbf520ff81977e508a03b3c16a3c55f404a70d0a19fa"
        }
      ],
      "native_fragments": [
        "concentration-construction"
      ]
    },
    "concentration-solution": {
      "source_label": "prop:anisotropic-global-concentration",
      "source_path": "contributions/cao-paun-foliations/R0208.tex",
      "scope": "proof",
      "atom_count": 20,
      "atoms": [
        {
          "index": 5,
          "sha256": "2b3c4fe834a3cd4bff6d3140fef5244da0ee6f27180224177e82a5a213cf741f"
        },
        {
          "index": 6,
          "sha256": "3526791199cb38c0d6046dafcce3f70c7f1a1a585fca9b5471a8dfa9a6d78983"
        }
      ],
      "native_fragments": [
        "concentration-solution"
      ]
    },
    "pole-limit-construction": {
      "source_label": "prop:anisotropic-global-concentration",
      "source_path": "contributions/cao-paun-foliations/R0208.tex",
      "scope": "proof",
      "atom_count": 20,
      "atoms": [
        {
          "index": 7,
          "sha256": "194177239f3cb869cd049bfa1206f1787c907fda45a6d71b9ce64a029e45dfaa"
        },
        {
          "index": 8,
          "sha256": "965e33e5047adda972a3e464af458cca27e52eaf0a00b02512ccbb33149670b7"
        }
      ],
      "native_fragments": [
        "pole-limit-construction"
      ]
    },
    "pole-bound": {
      "source_label": "prop:anisotropic-global-concentration",
      "source_path": "contributions/cao-paun-foliations/R0208.tex",
      "scope": "proof",
      "atom_count": 20,
      "atoms": [
        {
          "index": 9,
          "sha256": "a52533aab718f839854bd2c3fd66f6bb417db947107d095abf6140c0a22898ed"
        },
        {
          "index": 10,
          "sha256": "71e4beac08f4abe3e48e8347c5a268bb02a065d7b47eccb9eef093c00da08f7a"
        }
      ],
      "native_fragments": [
        "pole-bound"
      ]
    },
    "pole-error-convention": {
      "source_label": "prop:anisotropic-global-concentration",
      "source_path": "contributions/cao-paun-foliations/R0208.tex",
      "scope": "proof",
      "atom_count": 20,
      "atoms": [
        {
          "index": 10,
          "sha256": "71e4beac08f4abe3e48e8347c5a268bb02a065d7b47eccb9eef093c00da08f7a"
        }
      ],
      "native_fragments": [
        "pole-bound"
      ]
    },
    "vanishing-order-construction": {
      "source_label": "prop:anisotropic-global-concentration",
      "source_path": "contributions/cao-paun-foliations/R0208.tex",
      "scope": "proof",
      "atom_count": 20,
      "atoms": [
        {
          "index": 11,
          "sha256": "1ee03d822af3a3d74a36892dc21a61a40197096f45893703a664a59efbcace04"
        },
        {
          "index": 12,
          "sha256": "c35a2b4e8a85e089becfdf4bb78350a222407213d98064ffbe721f41a6a4666e"
        },
        {
          "index": 13,
          "sha256": "72f0b2a94b29de87994bbaf8d9e55f6a5384deac3017f72b7fbbe73cd5bc4ef7"
        },
        {
          "index": 14,
          "sha256": "aa5842c60a01ce2fa02114cfffc9599393ee360844c43187ce1ce5b39d431f1d"
        }
      ],
      "native_fragments": [
        "vanishing-order-construction"
      ]
    },
    "compact-center-setting": {
      "source_label": "prop:compact-center-lelong-propagation",
      "source_path": "contributions/cao-paun-foliations/R0209.tex",
      "scope": "statement",
      "atom_count": 3,
      "atoms": [
        {
          "index": 0,
          "sha256": "74dcac1cf3e55de1305e45df82a1d4c19e12ef4735af2cb47b5fe65f66d81842"
        },
        {
          "index": 1,
          "sha256": "11dfc94e030e6da994f0e131c1863e6c2f8cebb90f7e5e1189b6784be5b74098"
        },
        {
          "index": 2,
          "sha256": "276baa0a25324d6fd18edc4b86523038a7a08f2f78f7ec2eadc41043b6ca5891"
        }
      ],
      "native_fragments": [
        "compact-center-setting"
      ]
    },
    "compact-center-coefficient": {
      "source_label": "prop:compact-center-lelong-propagation",
      "source_path": "contributions/cao-paun-foliations/R0209.tex",
      "scope": "proof",
      "atom_count": 19,
      "atoms": [
        {
          "index": 0,
          "sha256": "359c5513c2509606681c742aca14e210897f9169b107c21387a2f7e9d15989e7",
          "slice": [
            0,
            188
          ]
        },
        {
          "index": 0,
          "sha256": "359c5513c2509606681c742aca14e210897f9169b107c21387a2f7e9d15989e7",
          "slice": [
            485,
            552
          ]
        }
      ],
      "native_fragments": [
        "compact-center-coefficient"
      ]
    },
    "compact-center-model": {
      "source_label": "prop:compact-center-lelong-propagation",
      "source_path": "contributions/cao-paun-foliations/R0209.tex",
      "scope": "proof",
      "atom_count": 19,
      "atoms": [
        {
          "index": 1,
          "sha256": "e3450f649a78327d55a2a0debd99b8826a5875b25c3bfaed8bac12ae51e54079"
        },
        {
          "index": 2,
          "sha256": "a56c0b858d00ff020bbf78a42784643dea8435873292f73aeffb03d7146c4610"
        },
        {
          "index": 3,
          "sha256": "0b5595a8f52d22ce2d01ef53451b8a4f431cf63a85ff8e4cd762569ed50e3cf8",
          "slice": [
            0,
            98
          ]
        }
      ],
      "native_fragments": [
        "compact-center-model"
      ]
    },
    "compact-center-currents": {
      "source_label": "prop:compact-center-lelong-propagation",
      "source_path": "contributions/cao-paun-foliations/R0209.tex",
      "scope": "proof",
      "atom_count": 19,
      "atoms": [
        {
          "index": 4,
          "sha256": "e8fdc03a813cfb97040e93de9acae5d65e2238b011e69a96fdcad06e152c4e09"
        },
        {
          "index": 5,
          "sha256": "492655c7c0b5add42e88eb73be5eb497dce18e7ed8ff990af1f6df7afc1e1491"
        },
        {
          "index": 6,
          "sha256": "dc8d1025995b18b6c8ffe574bf8cedba3420c97f89cfd5545c90e554e52bc51a"
        },
        {
          "index": 7,
          "sha256": "b79f5c28484563a8d28562a18a40a09b5771d3b62d12618de13a6bcefcded034"
        },
        {
          "index": 8,
          "sha256": "df1d5937b7fa147459e28ba1b2cd22a556e56e66fc192a45c25414954ea0cba3"
        }
      ],
      "native_fragments": [
        "compact-center-currents"
      ]
    },
    "compact-center-inequality-lead": {
      "source_label": "prop:compact-center-lelong-propagation",
      "source_path": "contributions/cao-paun-foliations/R0209.tex",
      "scope": "proof",
      "atom_count": 19,
      "atoms": [
        {
          "index": 16,
          "sha256": "b4f6860b5eda6b219dd0d05f6b1271d9c831d57c2294075c76c35d4ec6804b76"
        }
      ],
      "native_fragments": [
        "compact-center-inequality-lead"
      ]
    },
    "conormal-approximate-definition": {
      "source_label": "sec:conormal-positivity-analytic-germs",
      "source_path": "contributions/cao-paun-foliations/R0210.tex",
      "scope": "section-prose",
      "atom_count": 1,
      "atoms": [
        {
          "index": 0,
          "sha256": "bef4b837e048514ed5bd4de46c4504528195fa446df6f924584e9590df88367f"
        }
      ],
      "native_fragments": [
        "conormal-approximate-definition"
      ]
    },
    "compact-complex-ambient": {
      "source_label": "sec:movable-slope-filtrations",
      "source_path": "contributions/cao-paun-foliations/R0211.tex",
      "scope": "section-prose",
      "atom_count": 3,
      "atoms": [
        {
          "index": 0,
          "sha256": "38bab20396de83b485cee478c245a13a34df2ab416f3b5e94938e2c0da750e59",
          "slice": [
            0,
            39
          ]
        }
      ],
      "native_fragments": [
        "degree-and-slope-definition"
      ]
    },
    "degree-and-slope-definition": {
      "source_label": "sec:movable-slope-filtrations",
      "source_path": "contributions/cao-paun-foliations/R0211.tex",
      "scope": "section-prose",
      "atom_count": 3,
      "atoms": [
        {
          "index": 0,
          "sha256": "38bab20396de83b485cee478c245a13a34df2ab416f3b5e94938e2c0da750e59"
        },
        {
          "index": 1,
          "sha256": "841a12e44325461ba39bfb8c1eb52118993b4877e8d888cfc3576b97af801b71"
        },
        {
          "index": 2,
          "sha256": "748fc5535309af4690798e96c0099ed0adf94719979c695d1272780bbb4ce2ae",
          "slice": [
            0,
            95
          ]
        }
      ],
      "native_fragments": [
        "degree-and-slope-definition"
      ]
    },
    "movable-cone-definition": {
      "source_label": "sec:movable-slope-filtrations",
      "source_path": "contributions/cao-paun-foliations/R0211.tex",
      "scope": "section-prose",
      "atom_count": 3,
      "atoms": [
        {
          "index": 2,
          "sha256": "748fc5535309af4690798e96c0099ed0adf94719979c695d1272780bbb4ce2ae",
          "slice": [
            405,
            909
          ]
        }
      ],
      "native_fragments": [
        "movable-cone-definition"
      ]
    },
    "tensor-semistability-input": {
      "source_label": "sec:tensor-slopes-and-involutivity",
      "source_path": "contributions/cao-paun-foliations/R0211.tex",
      "scope": "section-prose",
      "atom_count": 1,
      "atoms": [
        {
          "index": 0,
          "sha256": "67543b4cfcab36a573586853d0e4565ef5f8a923db58c20a500591773afed5c6"
        }
      ],
      "native_fragments": [
        "tensor-semistability-input"
      ]
    },
    "tautological-approximate-definition": {
      "source_label": "sec:tautological-metrics-movable-slopes",
      "source_path": "contributions/cao-paun-foliations/R0212.tex",
      "scope": "section-prose",
      "atom_count": 1,
      "atoms": [
        {
          "index": 0,
          "sha256": "dff8ef6c9b811f8b747fa247c7cae2de8760db952c123860a26ab0895289b613"
        }
      ],
      "native_fragments": [
        "tautological-approximate-definition"
      ]
    },
    "numerical-dimension-definition": {
      "source_label": "sec:numerical-dimension-cotangent-quotients",
      "source_path": "contributions/cao-paun-foliations/R0214.tex",
      "scope": "section-prose",
      "atom_count": 9,
      "atoms": [
        {
          "index": 0,
          "sha256": "2628927b12b02c7d1dea288afe1f8123787c1f3b40cf6e6f65d85b137d881f9c"
        },
        {
          "index": 1,
          "sha256": "e6a0c34ee295596db5802efab79e275e5425f84a2ee4d73b5d6f9e699b6d8a16"
        },
        {
          "index": 2,
          "sha256": "5d729a2a93149b5a1e42b26941372bdeb3faf3d00b70c6f7215164c8e28da3a6"
        },
        {
          "index": 3,
          "sha256": "4319c9543ee14d64b7a7fcc43fc10ca827ffd3eab94e3ddbf8d6ef3e7a469925"
        },
        {
          "index": 4,
          "sha256": "d9289e6903fff871baf53042aeb7fc385bfcbd8d763d5c8a32d6c983add3866c"
        },
        {
          "index": 5,
          "sha256": "2ff0ba8a652b00fdfc82656329b8fd7543ecc6029ad90eb496e851e9c5cb7937"
        },
        {
          "index": 8,
          "sha256": "c6954aab5b1aab796996866115602e24b015ccbbf14e96703f28c8960778f7f3",
          "slice": [
            561,
            749
          ]
        }
      ],
      "native_fragments": [
        "numerical-dimension-definition"
      ]
    },
    "fujiki-deformation-input": {
      "source_label": "sec:deformation-canonical-pseudoeffectivity",
      "source_path": "contributions/cao-paun-foliations/R0215.tex",
      "scope": "section-prose",
      "atom_count": 1,
      "atoms": [
        {
          "index": 0,
          "sha256": "2fc39e7771dad6657f0688b508aeab1e5b9143eb7bbdf53f2ea7b763e26eadae"
        }
      ],
      "native_fragments": [
        "fujiki-deformation-input"
      ]
    }
  },
  "bridges": {
    "blowup-reference": {
      "html": "<p>The blowup estimate used below is <a href=\"/tag/B1934518\">the smooth-center blowup proposition</a>.</p>",
      "sha256": "a48c53167ce96661fcdfef147edfb8e43dc6cee47512a58c64818c61aa74b475",
      "native_fragments": [
        "blowup-setting"
      ],
      "source_paths": [
        "contributions/cao-paun-foliations/R0205.tex"
      ],
      "reason": "Resolve the inherited preceding-proposition reference without copying its conclusion."
    },
    "generic-line-reference": {
      "html": "<p>The generic-line restriction used below is <a href=\"/tag/3DE2308F\">the generic-line Lelong-number lemma</a>.</p>",
      "sha256": "92b027afb2278a0ebd76a63b97c60bb0fba8866f7084d524c0b797e6c7d6ba24",
      "native_fragments": [
        "generic-line"
      ],
      "source_paths": [
        "contributions/cao-paun-foliations/R0205.tex"
      ],
      "reason": "Name the preceding lemma used in the independently displayed proof."
    },
    "normalized-pole-reference": {
      "html": "<p>The normalized diagonal-pole model used below is given by <a href=\"/tag/A77E2EB0\">the normalized-pole mass lemma</a>.</p>",
      "sha256": "f9a9705cea464aa9282dfd2d141c460d6697022684c5d4ffb93f3f7b707f73a0",
      "native_fragments": [
        "normalized-pole-model"
      ],
      "source_paths": [
        "contributions/cao-paun-foliations/R0208.tex"
      ],
      "reason": "Identify the preceding lemma after its model is copied outside its native section."
    },
    "compact-center-extension": {
      "html": "<p>Let $P$ be the global closed positive extension of $P_0$ to $C$ constructed in the proof of <a href=\"/tag/6F802F01\">compact-center Lelong propagation</a>.</p>",
      "sha256": "822e7743eb9e901e7a838290bc190379da0dd068a3323f3c7267c1bb579b38b1",
      "native_fragments": [
        "compact-center-extension"
      ],
      "source_paths": [
        "contributions/cao-paun-foliations/R0209.tex"
      ],
      "reason": "Supply the precise constructed extension without duplicating its codimension-two proof."
    },
    "leaf-relation-ambient": {
      "html": "<p>Let $X$ be compact Kähler. The <a href=\"/tag/DB4DFCD8\">conormal dimension-jump criterion</a> is applied below in $X\\times X$, with $C$ the diagonal copy of $X$, $C_0=U$ and $V=\\mathcal F^*|_U$.</p>",
      "sha256": "18366428f248362a8b2a4edd3901eed98707d1170bf4042f5fac7dbe6d6fe1f2",
      "native_fragments": [
        "conormal-theorem-setting",
        "leaf-relation-setting"
      ],
      "source_paths": [
        "contributions/cao-paun-foliations/R0210.tex"
      ],
      "reason": "Restore the compact Kähler ambient and identify the exact diagonal application and preceding theorem."
    },
    "tensor-movable-ambient": {
      "html": "<p>Here $X$ is compact Kähler and $\\alpha$ is a movable class.</p>",
      "sha256": "b074f9667b7d39ce378117090b2ba0fdd0930cce0fb2de44f4703af261e6d2bf",
      "native_fragments": [
        "degree-and-slope-definition",
        "movable-cone-definition",
        "tensor-semistability-input"
      ],
      "source_paths": [
        "contributions/cao-paun-foliations/R0211.tex"
      ],
      "reason": "Specialize the general degree conventions to the compact Kähler/movable hypotheses actually used by the tensor and bracket deductions."
    },
    "two-forms-movable-class": {
      "html": "<p>Here $\\alpha$ is a movable class.</p>",
      "sha256": "aae1438ff83b0783ea5060159e67c07439ce8f5e8157bbeff48eb0092c384137",
      "native_fragments": [
        "two-forms-native-scope",
        "foliation-main-scope",
        "tensor-semistability-input"
      ],
      "source_paths": [
        "contributions/cao-paun-foliations/R0211.tex",
        "contributions/cao-paun-foliations/R0213.tex"
      ],
      "reason": "State the inherited movable-class scope without importing the later theorem as a hypothesis."
    },
    "maximal-piece-ambient": {
      "html": "<p>Here $X$ is compact Kähler and $\\alpha$ is a movable class.</p>",
      "sha256": "b074f9667b7d39ce378117090b2ba0fdd0930cce0fb2de44f4703af261e6d2bf",
      "native_fragments": [
        "foliation-main-scope",
        "tensor-semistability-input"
      ],
      "source_paths": [
        "contributions/cao-paun-foliations/R0211.tex",
        "contributions/cao-paun-foliations/R0213.tex"
      ],
      "reason": "Restore only the ambient/class assumptions inherited by the corollary."
    },
    "cone-duality-reference": {
      "html": "<p>The cone duality used below is the <a data-proof-entry=\"DF6FA97EF816\" href=\"https://mingchenxia.github.io/Pome/tag/DF6FA97EF816/\">duality of the pseudo-effective and movable cones</a>.</p>",
      "sha256": "c92b5171fb300b14af62c430962ccb9ba3ae23bb3d7cbbedcb719fb638b923a3",
      "native_fragments": [
        "cone-duality-reference"
      ],
      "source_paths": [
        "contributions/cao-paun-foliations/R0214.tex"
      ],
      "reason": "Supply the exact canonical input already used in the native preceding section."
    },
    "free-curve-reference": {
      "html": "<p>The covering-curve lemma used below is <a href=\"/tag/AA1A5BE2\">the free-covering-curve movable-degree lemma</a>.</p>",
      "sha256": "bc2cc5aa7a53a80c6a1fd9f06cde80ed368747556ba78d188af788321bb62e6f",
      "native_fragments": [
        "free-curve-statement"
      ],
      "source_paths": [
        "contributions/cao-paun-foliations/R0214.tex"
      ],
      "reason": "Make the already stated predecessor explicit in standalone reading."
    }
  },
  "entries": {
    "sec:blowup-restricted-lelong": {
      "kind": "section",
      "section": true,
      "disposition": "retained-context",
      "reason": "Retains the normalization, circular mean, blowup proposition and residual-lemma setting in continuous order.",
      "context": []
    },
    "prop:smooth-blowup-lelong-factor-two": {
      "kind": "proposition",
      "section": false,
      "disposition": "required-context",
      "reason": "The proof uses m_u and the cited diagonal mean formula; both definition and canonical citation precede the extracted proposition.",
      "context": [
        "lelong-conventions",
        "circular-mean"
      ]
    },
    "lem:blowup-residual-lelong": {
      "kind": "lemma",
      "section": false,
      "disposition": "required-context",
      "reason": "The statement begins In the same setting and uses pi without identifying the smooth-center blowup. Link the preceding proposition as well.",
      "context": [
        "lelong-conventions",
        "blowup-setting",
        "blowup-reference"
      ]
    },
    "sec:projective-bundle-lelong": {
      "kind": "section",
      "section": true,
      "disposition": "retained-context",
      "reason": "Retains the generic-line lemma, blowup-fiber corollary and bundle-integration proposition together.",
      "context": []
    },
    "lem:generic-line-lelong-restriction": {
      "kind": "lemma",
      "section": false,
      "disposition": "retained-context",
      "reason": "The psh/complex-line setting and canonical growth/Jensen references are inside the record.",
      "context": []
    },
    "cor:blowup-fiber-minimum-lelong": {
      "kind": "corollary",
      "section": false,
      "disposition": "reference-navigation",
      "reason": "A smooth-center blowup supplies pi in ordinary mathematical usage; its preceding generic-line lemma should be an explicit canonical reference in standalone reading.",
      "context": [
        "generic-line-reference"
      ]
    },
    "prop:projective-bundle-lelong-pushforward": {
      "kind": "proposition",
      "section": false,
      "disposition": "reference-navigation",
      "reason": "All statement objects are supplied; preceding lemma in the proof refers to the generic-line lemma omitted from this record.",
      "context": [
        "generic-line-reference"
      ]
    },
    "sec:nadel-singular-metric-vanishing": {
      "kind": "section",
      "section": true,
      "disposition": "retained-context",
      "reason": "The statement contains compact Kaehler geometry, positive curvature and full quadratic multiplier convention; all proof setup is internal.",
      "context": []
    },
    "thm:compact-nadel-vanishing": {
      "kind": "theorem",
      "section": false,
      "disposition": "retained-context",
      "reason": "The geometry, positive curvature bound and full quadratic multiplier convention are stated; proof setup and canonical inputs are internal.",
      "context": []
    },
    "sec:relative-positivity-projectivity": {
      "kind": "section",
      "section": true,
      "disposition": "retained-context",
      "reason": "The submersion, relative line positivity, complete linear system, base-change input and disconnected/zero-dimensional cases survive.",
      "context": []
    },
    "lem:relative-positivity-projectivity": {
      "kind": "lemma",
      "section": false,
      "disposition": "retained-context",
      "reason": "The statement is self-contained and the exact base-change input is inside its proof, including disconnected and zero-dimensional fibers.",
      "context": []
    },
    "sec:projective-hartogs-extension": {
      "kind": "section",
      "section": true,
      "disposition": "retained-context",
      "reason": "The codimension-two, projective-target and reflexive-sheaf hypotheses, plus canonical extension input, are internal.",
      "context": []
    },
    "lem:codim-two-projective-extension": {
      "kind": "lemma",
      "section": false,
      "disposition": "retained-context",
      "reason": "All statement hypotheses and the exact canonical extension reference are internal.",
      "context": []
    },
    "sec:euler-characteristic-flat-twists": {
      "kind": "section",
      "section": true,
      "disposition": "retained-context",
      "reason": "The smooth projective and Picard-zero setting occurs in the lemma and proof. The implicit name Z is native wording, not an extraction loss.",
      "context": []
    },
    "lem:flat-twist-euler-characteristic": {
      "kind": "lemma",
      "section": false,
      "disposition": "retained-context",
      "reason": "The smooth projective and Picard-zero setting is internal. The implicit name Z is native wording, not an omitted outside antecedent.",
      "context": []
    },
    "sec:singular-metric-determinants": {
      "kind": "section",
      "section": true,
      "disposition": "retained-context",
      "reason": "The metric nondegeneracy, dual-log-norm psh condition and lower-bound convention are stated locally.",
      "context": []
    },
    "lem:singular-griffiths-determinant-positive": {
      "kind": "lemma",
      "section": false,
      "disposition": "retained-context",
      "reason": "The metric hypotheses and lower-bound convention are inside the lemma, and its proof constructs all local objects.",
      "context": []
    },
    "sec:flat-adjoint-section-envelopes": {
      "kind": "section",
      "section": true,
      "disposition": "retained-context",
      "reason": "Retains the theorem data and the entire normalization construction, including its labelled equation.",
      "context": []
    },
    "thm:flat-twist-adjoint-envelope": {
      "kind": "theorem",
      "section": false,
      "disposition": "retained-context",
      "reason": "Z,F,A,m0,D,flat metrics,envelope normalization and divisibility are in the statement; construction is in the retained proof.",
      "context": []
    },
    "eq:full-weight-shokurov-normalization": {
      "kind": "equation",
      "section": false,
      "disposition": "required-context",
      "reason": "The isolated equation otherwise leaves Z,s,u_k,k0,k,h_F,h_A prime and the invariant ratio undefined.",
      "context": [
        "flat-envelope-setting",
        "flat-normalization-construction"
      ],
      "after_context": [
        "flat-invariant-ratio"
      ]
    },
    "sec:relative-canonical-positivity": {
      "kind": "section",
      "section": true,
      "disposition": "retained-context",
      "reason": "Retains the map and D(p) definition between the local lemma and relative theorem.",
      "context": []
    },
    "lem:uniform-submean-complex-submanifold": {
      "kind": "lemma",
      "section": false,
      "disposition": "retained-context",
      "reason": "All local geometry, regularity, curvature, Euclidean-volume and dimensional constants are stated internally.",
      "context": []
    },
    "thm:rational-hodge-relative-adjoint": {
      "kind": "theorem",
      "section": false,
      "disposition": "required-context",
      "reason": "Surjectivity, compact Kaehler X/Y, the map p, and the precise divisorial sum D(p) precede the theorem environment.",
      "context": [
        "relative-map-and-ramification"
      ]
    },
    "sec:diagonal-multiplier-weights": {
      "kind": "section",
      "section": true,
      "disposition": "retained-context",
      "reason": "Retains the full exp(-phi) convention and the monomial setting adjacent to the threshold.",
      "context": []
    },
    "lem:diagonal-monomial-multiplier-ideal": {
      "kind": "lemma",
      "section": false,
      "disposition": "convention-enhancement",
      "reason": "The full exp(-phi) convention is omitted from the statement but recoverable from its proof phi=2g. Carry the short exact convention with the statement.",
      "context": [
        "multiplier-weight"
      ]
    },
    "eq:diagonal-multiplier-threshold": {
      "kind": "equation",
      "section": false,
      "disposition": "required-context",
      "reason": "The standalone inequality loses the metric weight, parameter ranges, and the meaning of the monomial beta.",
      "context": [
        "multiplier-weight",
        "diagonal-weight-setting"
      ]
    },
    "sec:anisotropic-restricted-concentration": {
      "kind": "section",
      "section": true,
      "disposition": "convention-enhancement",
      "reason": "The local model and mass lemma are retained; the same dd^c normalization is available through its actual canonical mass-formula link.",
      "context": []
    },
    "lem:normalized-diagonal-pole-mass": {
      "kind": "lemma",
      "section": false,
      "disposition": "convention-enhancement",
      "reason": "The source-wide dd^c unit normalization is outside this record. Its proof already links 558E1268EEED, which explicitly gives the identical normalization; this is a standalone-convention enhancement, not an unsupported mass theorem.",
      "context": [
        "lelong-normalization"
      ]
    },
    "prop:anisotropic-global-concentration": {
      "kind": "proposition",
      "section": false,
      "disposition": "required-context",
      "reason": "The proof uses f_m_epsilon and the preceding lemma for its mass estimate; that model is outside the extracted proposition.",
      "context": [
        "lelong-normalization",
        "normalized-pole-reference",
        "normalized-pole-model"
      ]
    },
    "eq:anisotropic-concentration-equation": {
      "kind": "equation",
      "section": false,
      "disposition": "required-context",
      "reason": "The PDE requires the parent geometry, local pole model, eta,chi,a,b and normalized solution construction.",
      "context": [
        "lelong-normalization",
        "normalized-pole-reference",
        "normalized-pole-model",
        "concentration-setting",
        "concentration-construction"
      ]
    },
    "eq:anisotropic-global-pole-bound": {
      "kind": "equation",
      "section": false,
      "disposition": "required-context",
      "reason": "The bound requires the coordinate setting, psi_m limit, positive C independent of m, and bounded-error convention.",
      "context": [
        "lelong-normalization",
        "normalized-pole-reference",
        "normalized-pole-model",
        "concentration-setting",
        "concentration-construction",
        "concentration-solution",
        "pole-limit-construction"
      ],
      "after_context": [
        "pole-error-convention"
      ]
    },
    "eq:corrected-restricted-vanishing-order": {
      "kind": "equation",
      "section": false,
      "disposition": "required-context",
      "reason": "The inequality concerns Taylor monomials of I(k psi_m) surviving z1=0, with dyadic k and C fixed by the mass construction.",
      "context": [
        "lelong-normalization",
        "normalized-pole-reference",
        "normalized-pole-model",
        "concentration-setting",
        "concentration-construction",
        "concentration-solution",
        "pole-limit-construction",
        "pole-bound",
        "vanishing-order-construction"
      ]
    },
    "sec:compact-center-restricted-singularities": {
      "kind": "section",
      "section": true,
      "disposition": "retained-context",
      "reason": "The parent proposition and full current/extension construction are retained.",
      "context": []
    },
    "prop:compact-center-lelong-propagation": {
      "kind": "proposition",
      "section": false,
      "disposition": "retained-context",
      "reason": "All ambient geometry, restriction condition and constants are stated; the divisorial residual described below is inside the retained proof.",
      "context": []
    },
    "eq:compact-center-lelong-lower": {
      "kind": "equation",
      "section": false,
      "disposition": "required-context",
      "reason": "The equation loses its geometry and the definitions of a,T,p,P; P is the positive global extension of the fiber integral.",
      "context": [
        "lelong-conventions",
        "compact-center-setting",
        "compact-center-coefficient",
        "compact-center-model",
        "compact-center-currents",
        "compact-center-extension",
        "compact-center-inequality-lead"
      ]
    },
    "sec:conormal-positivity-analytic-germs": {
      "kind": "section",
      "section": true,
      "disposition": "retained-context",
      "reason": "Retains the approximate-psef definition immediately before the dimension-jump theorem.",
      "context": []
    },
    "thm:conormal-positivity-dimension-jump": {
      "kind": "theorem",
      "section": false,
      "disposition": "required-context",
      "reason": "The statement says in the stated approximate sense; that exact epsilon-metric definition is outside the theorem.",
      "context": [
        "conormal-approximate-definition"
      ]
    },
    "sec:foliation-leaf-relation": {
      "kind": "section",
      "section": true,
      "disposition": "required-context",
      "reason": "The separate reading section inherits compact Kaehler X and the approximate psef meaning; preceding theorem must identify the conormal criterion.",
      "context": [
        "leaf-relation-ambient",
        "conormal-approximate-definition"
      ],
      "section_context": true
    },
    "sec:movable-slope-filtrations": {
      "kind": "section",
      "section": true,
      "disposition": "retained-context",
      "reason": "Retains compact X, determinant degree, alpha conditions, all slope definitions and the movable-cone discussion.",
      "context": []
    },
    "lem:noetherian-degree-maximum": {
      "kind": "lemma",
      "section": false,
      "disposition": "required-context",
      "reason": "Compact complex ambient X is outside the lemma and is used for the coherent-subsheaf ascending chain condition.",
      "context": [
        "compact-complex-ambient"
      ]
    },
    "thm:movable-hardernarasimhan-filtration": {
      "kind": "theorem",
      "section": false,
      "disposition": "required-context",
      "reason": "For such a degree functional loses the determinant pairing, divisor nonnegativity, compact X and extremal slope definitions.",
      "context": [
        "degree-and-slope-definition"
      ]
    },
    "lem:dual-slopes-and-hom-vanishing": {
      "kind": "lemma",
      "section": false,
      "disposition": "required-context",
      "reason": "The statement omits the degree functional and allowed alpha, needed for same-rank monotonicity and the slope symbols.",
      "context": [
        "degree-and-slope-definition"
      ]
    },
    "sec:tensor-slopes-and-involutivity": {
      "kind": "section",
      "section": true,
      "disposition": "retained-context",
      "reason": "Retains the exact compact-Kaehler/movable tensor semistability input before its deductions; general slope definitions can be reached in the preceding degree section.",
      "context": []
    },
    "prop:tensor-maximal-minimal-slopes": {
      "kind": "proposition",
      "section": false,
      "disposition": "required-context",
      "reason": "Under that semistability input otherwise has no referent. The compact Kaehler/movable scope and exact input must remain visible.",
      "context": [
        "degree-and-slope-definition",
        "movable-cone-definition",
        "tensor-movable-ambient",
        "tensor-semistability-input"
      ]
    },
    "cor:positive-first-hn-piece-involutive": {
      "kind": "corollary",
      "section": false,
      "disposition": "required-context",
      "reason": "The compact Kaehler/movable setting is omitted, although the tensor and Hom-vanishing argument uses it.",
      "context": [
        "degree-and-slope-definition",
        "movable-cone-definition",
        "tensor-movable-ambient",
        "tensor-semistability-input"
      ]
    },
    "sec:tautological-metrics-movable-slopes": {
      "kind": "section",
      "section": true,
      "disposition": "retained-context",
      "reason": "Retains the positive-rank reflexive ambient setup, fixed-model approximate-psef definition, fiber lemma and theorem.",
      "context": []
    },
    "lem:projective-fiber-weighted-section": {
      "kind": "lemma",
      "section": false,
      "disposition": "retained-context",
      "reason": "Its projective fiber, curvature bound, m-epsilon constraint and N bound are internal. The parent reflexive sheaf/model is not needed for this abstract fiber lemma.",
      "context": []
    },
    "thm:approximate-psef-nonnegative-maximal-slope": {
      "kind": "theorem",
      "section": false,
      "disposition": "required-context",
      "reason": "The statement omits positive-rank reflexive E, compact Kaehler X, X0, fixed model P and the precise approximate-psef definition.",
      "context": [
        "tautological-approximate-definition"
      ]
    },
    "sec:holomorphic-forms-positive-foliations": {
      "kind": "section",
      "section": true,
      "disposition": "retained-context",
      "reason": "Retains the principal compact-Kaehler/movable theorem and its deductions. The two-forms lemma uses the native implicit movable scope; standalone rows require that scope to be explicit.",
      "context": []
    },
    "lem:rational-hodge-kahler-class": {
      "kind": "lemma",
      "section": false,
      "disposition": "retained-context",
      "reason": "Its compact Kaehler setting and rational-class conclusion are internal, as are its canonical lattice and Hodge references.",
      "context": []
    },
    "lem:positive-foliation-annihilates-two-forms": {
      "kind": "lemma",
      "section": false,
      "disposition": "required-context",
      "reason": "The first assertion uses alpha without explicitly calling it movable; the native final clause and tensor input supply that inherited scope. Use a short reviewed bridge, not the entire later theorem.",
      "context": [
        "degree-and-slope-definition",
        "movable-cone-definition",
        "two-forms-movable-class"
      ]
    },
    "thm:positive-minimum-foliation-rc": {
      "kind": "theorem",
      "section": false,
      "disposition": "retained-context",
      "reason": "The compact-Kaehler, nonzero saturated involutive and movable-positive-minimum hypotheses are stated. Quotient, flattening and deformation inputs are described inside the retained proof.",
      "context": []
    },
    "cor:positive-maximal-piece-rc": {
      "kind": "corollary",
      "section": false,
      "disposition": "required-context",
      "reason": "The corollary omits compact Kaehler X and movable alpha inherited from the main theorem. Do not import its nonzero-F or conclusion as an additional hypothesis.",
      "context": [
        "degree-and-slope-definition",
        "movable-cone-definition",
        "maximal-piece-ambient"
      ]
    },
    "sec:numerical-dimension-cotangent-quotients": {
      "kind": "section",
      "section": true,
      "disposition": "retained-context",
      "reason": "Retains the exact positive-intersection numerical dimension and minus-infinity convention before the assertions.",
      "context": []
    },
    "lem:numerical-dimension-psef-monotonicity": {
      "kind": "lemma",
      "section": false,
      "disposition": "required-context",
      "reason": "The compact Kaehler ambient, positive-intersection convention and symbol nu are defined before the lemma.",
      "context": [
        "numerical-dimension-definition"
      ]
    },
    "thm:psef-canonical-cotangent-quotients": {
      "kind": "theorem",
      "section": false,
      "disposition": "required-context",
      "reason": "Its geometry is stated, but the line-injection assertion uses the inherited numerical-dimension convention including nu(L)=-infinity for non-psef L.",
      "context": [
        "numerical-dimension-definition"
      ]
    },
    "sec:tangent-slopes-uniruledness": {
      "kind": "section",
      "section": true,
      "disposition": "reference-navigation",
      "reason": "The geometric hypotheses and uniruled definition survive; cited cone duality lacks its citation within this separate section.",
      "context": []
    },
    "lem:free-covering-curve-movable-degree": {
      "kind": "lemma",
      "section": false,
      "disposition": "reference-navigation",
      "reason": "The statement is self-contained; cited cone duality in the proof refers to a canonical input linked in the preceding numerical section.",
      "context": [
        "cone-duality-reference"
      ]
    },
    "cor:uniruled-tangent-slope-equivalence": {
      "kind": "corollary",
      "section": false,
      "disposition": "reference-navigation",
      "reason": "The geometric and movable hypotheses are stated; preceding lemma and cone duality should have explicit canonical links.",
      "context": [
        "cone-duality-reference",
        "free-curve-reference"
      ]
    },
    "sec:deformation-canonical-pseudoeffectivity": {
      "kind": "section",
      "section": true,
      "disposition": "retained-context",
      "reason": "Retains the exact Fujiki input and citation before the corollary.",
      "context": []
    },
    "cor:deformation-canonical-psef": {
      "kind": "corollary",
      "section": false,
      "disposition": "required-context",
      "reason": "The statement is self-contained, but the proof invokes the stated deformation theorem whose exact hypotheses and citation precede the environment.",
      "context": [
        "fujiki-deformation-input"
      ]
    },
    "sec:relative-canonical-open-questions": {
      "kind": "section",
      "section": true,
      "disposition": "convention-enhancement",
      "reason": "Both open kinds and their surrounding status prose are retained. A numerical-dimension definition link is useful for the second question.",
      "context": []
    },
    "conj:general-relative-canonical-psef": {
      "kind": "conjecture",
      "section": false,
      "disposition": "retained-context",
      "reason": "The surjective compact-Kaehler map, metric/fiber hypotheses and conjecture kind survive; the existing global connectedness paragraph is present.",
      "context": []
    },
    "q:mrc-cotangent-numerical-dimension": {
      "kind": "question",
      "section": false,
      "disposition": "convention-enhancement",
      "reason": "The question states its geometric setting and retains question kind; a definition link/context would make the chosen numerical dimension explicit.",
      "context": [
        "numerical-dimension-definition"
      ]
    }
  }
}
''')


from bs4 import BeautifulSoup, NavigableString, Tag


def _context_digest(value):
    return sha256(value.encode("utf-8")).hexdigest()


def _paragraph(parts):
    markup = "".join(item.output_ready() if isinstance(item, NavigableString)
                     else str(item) for item in parts)
    if not BeautifulSoup(markup, "html.parser").get_text().strip():
        return []
    return ["<p>" + markup + "</p>"]


def _blocks(container):
    """Flatten renderer paragraph nesting without changing its inline contents."""
    result, pending = [], []
    for child in container.children:
        if isinstance(child, NavigableString):
            pending.append(child)
        elif isinstance(child, Tag) and child.name == "p":
            result += _paragraph(pending)
            pending = []
            result += _blocks(child)
        elif isinstance(child, Tag) and child.name in {
            "div", "ol", "ul", "table", "blockquote", "figure"
        }:
            result += _paragraph(pending)
            pending = []
            result.append(str(child))
        elif isinstance(child, Tag):
            require(child.name not in {"article", "section", "h1", "h2", "h3"},
                    "Unexpected nested context structure")
            pending.append(child)
    return result + _paragraph(pending)


def context_atoms(record, scope):
    """Return exact prose/display atoms of a separately reviewed source record."""
    field = "proof_html" if scope == "proof" else "statement_html"
    require(field in record, "Context source lacks rendered field")
    soup = BeautifulSoup(record[field], "html.parser")
    for old in soup.select(".source-conventions, .reader-context"):
        old.decompose()
    # Canonical-link decoration belongs to the adapter after the extraction.
    # Its presence in an earlier exported fixture must not affect the guard.
    for anchor in soup.select("[data-proof-entry]"):
        del anchor["data-proof-entry"]
    if scope == "section-prose":
        require(record["section"], "Context prose source is not a section")
        result = []
        for node in soup.children:
            if not isinstance(node, Tag):
                continue
            if re.fullmatch(r"h[1-6]", node.name) or node.name == "article" or node.find("article"):
                continue
            if node.name == "p":
                result += _blocks(node)
            else:
                require(node.name in {"div", "ol", "ul", "table", "blockquote"},
                        "Unexpected section context node")
                result.append(str(node))
        return result
    require(scope in {"statement", "proof"}, "Unknown reviewed context scope")
    if scope == "statement":
        roots = soup.select('article[id="' + record["tag"] + '"]')
    else:
        roots = soup.select("article.env-proof")
    require(len(roots) == 1, "Missing or ambiguous context source root")
    root = roots[0]
    for marker in root.select("a.environment-identifier, .qed"):
        marker.decompose()
    if scope == "proof":
        heading = root.find("strong")
        require(heading is not None and heading.get_text(strip=True) == "Proof.",
                "Changed proof context heading")
        heading.decompose()
    return _blocks(root)


def _copy_markup(atoms):
    """A context copy links to source labels but never owns their root IDs."""
    markup = re.sub(r"\\label(?:\[[^]]*\])?\s*\{[^{}]*\}", "", "\n".join(atoms))
    soup = BeautifulSoup(markup, "html.parser")
    # Copied displays are context, not a second owner of a numbered equation.
    # Inline references retain data-tag so the destination can renumber them.
    for marker in soup.select(".equation-label, .tag-id, .environment-identifier"):
        marker.decompose()
    for node in soup.select("[id]"):
        del node["id"]
    for node in soup.select("[data-gerby-tag]"):
        del node["data-gerby-tag"]
    for anchor in soup.select('a[href]'):
        match = re.fullmatch(
            r"https://mingchenxia\.github\.io/Pome/tag/([A-F0-9]{12})/",
            anchor["href"],
        )
        if match:
            anchor["data-proof-entry"] = match[1]
    return str(soup)


def _selected_atom(atoms, selection, name):
    """Select a whole atom, or a reviewed contiguous range within one paragraph."""
    index, expected = selection["index"], selection["sha256"]
    require(isinstance(index, int) and 0 <= index < len(atoms),
            "Invalid reader context atom")
    atom = atoms[index]
    require(_context_digest(atom) == expected,
            "Reader context rendered source changed: " + name)
    if "slice" not in selection:
        return atom
    require(atom.startswith("<p>") and atom.endswith("</p>"),
            "Only a reviewed paragraph can be shortened")
    start, end = selection["slice"]
    inner = atom[3:-4]
    require(isinstance(start, int) and isinstance(end, int)
            and 0 <= start < end <= len(inner), "Invalid paragraph context range")
    fragment = inner[start:end]
    require(str(BeautifulSoup(fragment, "html.parser")) == fragment,
            "Reader context range breaks inline markup")
    require(fragment.count("$") % 2 == 0,
            "Reader context range breaks inline mathematics")
    return "<p>" + fragment + "</p>"


def apply_reader_context(manifest, material, records, spec):
    """Validate the complete reviewed context map before changing any record."""
    by_label = {row["label"]: row for row in records}
    require(len(by_label) == len(records), "Repeated context target label")
    historical = set(re.findall(r"\\label\s*\{([^{}]+)\}",
                               material["integrations/S0082/project-history.tex"]))
    require(set(by_label) - historical == set(spec["entries"]),
            "Reader context map does not cover the exact mathematical export")
    for path, expected in spec["source_sha256"].items():
        require(manifest["files"].get(path) == expected,
                "Reader context native source changed: " + path)
    for name, fragment in spec.get("native_fragments", {}).items():
        path = fragment["source_path"]
        require(path in spec["source_sha256"], "Unbound native context fragment")
        lines = material[path].splitlines(keepends=True)
        first, last = fragment["first_line"], fragment["last_line"]
        require(1 <= first <= last <= len(lines)
                and _context_digest("".join(lines[first - 1:last])) == fragment["sha256"],
                "Reader context native fragment changed: " + name)

    pieces = {}
    for name, bridge in spec.get("bridges", {}).items():
        require(bridge["source_paths"]
                and all(path in spec["source_sha256"] for path in bridge["source_paths"]),
                "Unbound editorial context bridge")
        require(bridge["native_fragments"]
                and all(name in spec["native_fragments"] for name in bridge["native_fragments"]),
                "Editorial context bridge lacks exact native evidence")
        require(_context_digest(bridge["html"]) == bridge["sha256"]
                and bridge["reason"].strip(),
                "Changed editorial context bridge")
        soup = BeautifulSoup(bridge["html"], "html.parser")
        require(not soup.select("[id], article, .environment-identifier, .equation-label"),
                "Editorial context bridge creates a mathematical entry")
        pieces[name] = bridge["html"]
    for name, block in spec["blocks"].items():
        require(name not in pieces, "Repeated reader context component")
        source = by_label.get(block["source_label"])
        require(source is not None, "Reader context source label disappeared")
        require(block["source_path"] in spec["source_sha256"],
                "Unbound reader context source file")
        require(block["source_label"] in re.findall(r"\\label\s*\{([^{}]+)\}",
                                                    material[block["source_path"]]),
                "Reader context source label moved to a different file")
        atoms = context_atoms(source, block["scope"])
        require(block["native_fragments"]
                and all(name in spec["native_fragments"] for name in block["native_fragments"]),
                "Rendered context selection lacks exact native evidence")
        require(len(atoms) == block["atom_count"],
                "Reader context source structure changed: " + name)
        selected = []
        for selection in block["atoms"]:
            selected.append(_selected_atom(atoms, selection, name))
        require(selected, "Empty reviewed reader context selection")
        pieces[name] = _copy_markup(selected)

    local_tags = {row["tag"] for row in records}
    for name, markup in pieces.items():
        soup = BeautifulSoup(markup, "html.parser")
        require(not soup.select("[id], [data-gerby-tag], .tag-id, .equation-label,"
                                " .environment-identifier, article, script, style"),
                "Context copy creates a mathematical owner or executable content")
        for anchor in soup.select("a[href]"):
            href = anchor["href"]
            require(not href.startswith("#"), "Dangling fragment reference in context")
            if href.startswith("/tag/"):
                require(href.removeprefix("/tag/") in local_tags,
                        "Unresolved context source reference")

    planned = {}
    for label, decision in spec["entries"].items():
        row = by_label[label]
        require(row["kind"] == decision["kind"]
                and row["section"] == decision["section"],
                "Reader context entry kind changed: " + label)
        require(isinstance(decision["reason"], str) and decision["reason"].strip(),
                "Missing reader context disposition")
        placements = {"before": decision["context"],
                      "after": decision.get("after_context", [])}
        names = [name for group in placements.values() for name in group]
        require(len(names) == len(set(names)) and all(name in pieces for name in names),
                "Invalid reader context component map")
        require(not (row["section"] and names)
                or decision.get("section_context") is True,
                "Unreviewed section context injection")
        require(not placements["after"] or not row.get("proof_html", "").strip(),
                "Post-statement context requires a separately reviewed proof boundary")
        wrappers = {position: '<div class="reader-context" data-context-position="'
                    + position + '">' + "\n".join(pieces[name] for name in group)
                    + '</div>\n' for position, group in placements.items() if group}
        wrappers = {position: str(BeautifulSoup(markup, "html.parser").div) + "\n"
                    for position, markup in wrappers.items()}
        for field in ("html", "statement_html"):
            require(field in row, "Reader context target lacks rendered field")
            existing = BeautifulSoup(row[field], "html.parser").select(".reader-context")
            require(len(existing) == len({node.get("data-context-position")
                                          for node in existing}),
                    "Repeated reader context wrapper")
            if existing:
                require({node.get("data-context-position"): str(node) + "\n"
                         for node in existing} == wrappers,
                        "Existing reader context differs from reviewed selection: " + label)
                continue
            if not wrappers:
                continue
            value = row[field]
            if "before" in wrappers:
                convention = re.match(r'<p class="source-conventions">.*?</p>\s*',
                                      value, flags=re.S)
                position = convention.end() if convention else 0
                value = value[:position] + wrappers["before"] + value[position:]
            if "after" in wrappers:
                value += wrappers["after"]
            planned[(label, field)] = value

    # Proof fields, native TeX, root identifiers, kinds, and tags are untouched.
    # Whole sections change only where the map explicitly records missing
    # inherited context; their nested formal entries are never duplicated.
    for (label, field), value in planned.items():
        by_label[label][field] = value
    return records


def assign_topics(source, records):
    manifest, material, layout, order = selected_material(source)
    convention_html = '<p class="source-conventions">' + escape(source_conventions(material)) + '</p>\n'
    historical_labels = set(LABEL.findall(material[HISTORY]))
    labels, seen = {}, set()
    for name in order:
        topic = None
        for label in LABEL.findall(material[name]):
            if label in layout:
                row = layout[label]
                topic = "Historical and bibliographical notes" if row["chapter"] == "historical-notes" else row["title_tex"]
                seen.add(label)
            require(topic is not None, "Label precedes its subject boundary")
            labels[label] = topic
    require(seen == set(layout), "Unused subject boundary")
    exported = {label for row in records for label in [row["label"], *row.get("aliases", [])]}
    require(exported == set(labels), "Ordinary export lost or added source labels")
    for row in records:
        row["topic"] = labels[row["label"]]
        require(all(labels[alias] == row["topic"] for alias in row.get("aliases", [])),
                "An exported alias crosses a subject boundary")
        if row["label"] in OPEN:
            require(row["kind"] == OPEN[row["label"]], "Renderer changed an open statement kind")
        # Full section fragments already contain their nested raw statements.
        # Adding context to each independently exported record therefore gives
        # one note per continuous reading section and one per standalone entry,
        # without changing frozen proof text, statement fingerprints or tags.
        if row["label"] not in historical_labels:
            for field in ("html", "statement_html"):
                if field in row and not row[field].startswith(convention_html):
                    row[field] = convention_html + row[field]
        for field in ("html", "proof_html"):
            if field in row:
                row[field] = re.sub(
                    r'(<a\b(?![^>]*\bdata-proof-entry=)[^>]*\bhref="https://mingchenxia\.github\.io/Pome/tag/([A-F0-9]{12})/")([^>]*)>',
                    lambda m: m[1] + ' data-proof-entry="' + m[2] + '"' + m[3] + '>', row[field])
    return apply_reader_context(manifest, material, records, READER_CONTEXT)


if __name__ == "__main__":
    from common import configure, export
    configure(SLUG, "Relative canonical bundles and positive foliations",
              "https://github.com/MingchenXia/Gerby-Literature",
              author="Gerby Literature", bibliography=BIB)
    export(Path(sys.argv[1]), Path(sys.argv[2]), prepare=prepare_article, transform=assign_topics)
