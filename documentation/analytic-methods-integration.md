# Singular metrics, generation and canonical systems

The `analytic-methods` contribution exports an explicitly reviewed selection
from the Gerby-Literature study of Demailly's *Analytic Methods in Algebraic
Geometry* (S0050). It is distinct from the earlier *Complex Analytic and
Differential Geometry* contribution (S0002) and the later S0120 survey.
The current eighty-packet candidate is a bounded mathematical selection.
It does not assert complete-book or recursive dependency closure.

## Current selection

The exact packet order is shared by `RESULTS` in
`adapters/analytic-methods.py` and the source manifest. The selection comprises
R0300–R0347 except R0306, R0360–R0381, and R0382–R0392. The first sixty-nine
packets retain their previously accepted order; the eleven new packets are
appended in ascending order. R0306 is excluded because its smooth
weak-exhaustion statement is already proved at `E5505B695336`.

The earlier selection includes singular estimates and division, coherent
generation, nef dimensions and vanishing, integral-normalized envelopes,
coherent Euler polynomials and growth, surface positivity and adjoint jets,
compact Hermitian regularization, smooth and ambient jet estimates, and
geometric or spectral counterexamples. The following additions have separate
accepted proof and portable-export reviews.

| Packet | Subject placement | Reviewed scope |
| --- | --- | --- |
| R0382 | General complex cohomology; connections | Finite-divisor comparisons, varying-class cohomology envelopes, and integral approximation of real curvature forms. The finite-divisor estimate retains its finite-group uniformity hypothesis. |
| R0383 | Section growth; strict singular metrics | A section bound uniform over line bundles, degree-zero numerical limits, and the corresponding compact-complex consequences. The projective-modification theorem remains an explicit external input. |
| R0384 | Dolbeault spectral asymptotics; holomorphic Morse inequalities | Uniform freezing and fixed-threshold asymptotics for varying unitary connections, iterated spectral limits, the individual-degree joint upper limit, and transcendental cohomology envelopes. The cumulative joint counterexample remains intact. |
| R0385 | Complete-metric estimates and division | Exact and approximate original-metric twisted estimates under a smooth plurisubharmonic exhaustion, retaining arbitrary positive smooth twisting functions. |
| R0386 | Analytic singularities; multiplier ideals | Global Bergman approximation on compact Hermitian manifolds and the finite-system and divisorial threshold formulas, with the metric, volume and group hypotheses explicit. |
| R0387 | Complex spaces; rational curves | One-point family degree descent over the complex numbers under the stated projective-compactification and proper-family hypotheses. This does not supply a Hom-scheme dimension theorem or a dimension-only Fano curve bound. |
| R0388 | Dolbeault spectral asymptotics | A fixed nonintegrable connection whose degree-one kernel changes under a conformal base-metric perturbation, disproving the proposed finite-level multiplicative comparison. No general cumulative asymptotic metric conclusion is inferred. |
| R0389 | General complex cohomology and modifications | Uniform positive-degree projective comparison, fixed-power upper-limit identification, and transfer through a projective modification. Ordinary limits in every higher degree are not assumed. |
| R0390 | Holomorphic Morse inequalities; jet bundles | Singular jet tail bounds in degrees strictly above the singular-set dimension, leading cohomological comparison, and a boundary-degree concentration example. The example does not refute the large-jet-order section-growth conclusion. |
| R0391 | Holomorphic Morse inequalities; complex surfaces | Varying-class Euler limits, endpoint degrees and final cumulative Morse sums in every dimension, and all cohomological degrees on compact complex surfaces. |
| R0392 | Sheaf cohomology; holomorphic Morse inequalities | Relative projective-bundle vanishing and all-degree cohomology identification for the actual ambient bounded-jet pushforward at sufficiently large divisible weights. The separate tail restriction still controls the Morse-inequality range. |

Higher interior cohomological degrees on non-Moishezon manifolds of dimension
at least three, general cumulative spectral metric independence, fast-curvature
restriction for that cumulative envelope, low-degree singular jet/Fujita
estimates, and the remaining Fano prerequisites retain their separately
recorded scope. A narrower proved result or a counterexample to an intermediate
argument is not presented as closure of the broader theorem.

## Organization, canonical reuse and history

The source layout has 186 reviewed subject rows. The eleven additions supply
33 new complete mathematical heading boundaries; `collection.json` explicitly
promotes them in source order within the existing subjects. Proofs are never
split to manufacture a new section. Pome generates current section, statement
and equation numbers; source numbers remain provenance.

Compact singular-metric Nadel vanishing is canonical at `4F4355678C85`.
The equivalent R0302 corollary and its heading reuse that entry, preserving
the preferred Cao–Păun statement and proof and both source variants. R0302's
local resolution and sharp estimate remain independent statements. The
complete real-exponent monomial germ criterion is already at `F8F1C7EFDAD8`;
R0316 contributes its finite generator box and convention calculation.
R0301 supplies the uniform-generation step in `sgpt/lma:varphian`
(`A8896460B129`) through the existing guarded proof expansion. Other results
with materially different hypotheses remain separate.

Major attribution belongs in the connected project-wide subject history.
All 31 prior analytic-methods source-history strands are retained. The
eighty-packet extension appends reviewed prose to four strands and adds two
strands on varying cohomology classes and unitary connections. Their exact
source HTML fingerprints are checked in `reading/history/registry.json`.
The prior raw prose prefixes were verified against their original hashes;
the source-generated history heading numbers shift because the new proofs
precede the history. This explicit fingerprint review does not weaken the
guard. Original notes and source revisions remain available under Sources.

## Export contract

The entry point is `contributions/analytic-methods-public.tex`. The adapter
reads `integrations/S0050/source-manifest.json`, which selects exactly
85 content files:

- the article and its bibliography;
- eighty portable proof fragments under `contributions/analytic-methods/`;
- the section layout, canonical-reference map and project history under
  `integrations/S0050/`.

The manifest is a separate control file. The reviewed canonical interface has
224 bindings. Selection acceptance, per-packet evidence, research-to-portable
proof hashes, exact content hashes, canonical-consumer acceptance and complete
label coverage remain mandatory. A nested input, unexpected file, escaping
path or symlink, changed hash, unreviewed link, or additional packet fails the
export. Retained scans, source dossiers, research audits and unselected proof
attempts are outside this public graph.

Portable transformations preserve mathematical statements and proofs while
providing reviewed subject headings, complete-statement boundaries and stable
references. The existing R0316 narrowing and R0322 proof-order correction
retain their explicit recorded transformations. R0389's portable numerical
comparison is deliberately restricted to positive cohomological degrees;
its degree-zero input reuses R0383's canonical section comparison. This
recorded narrowing avoids a duplicate statement while retaining the full
research proof. A source research packet alone never authorizes its public
inclusion.

Standalone statements receive only their reviewed native introductory
conventions and local notation. Single-prefix and composed `prefix_chain`
bindings each check native and rendered hashes, packet identity, source order
and target order. The assembled candidate has 91 context bindings covering
267 target occurrences; the eleven-packet extension adds 17 bindings covering
48 target occurrences, including three new composed chains. Copied introductions retain links while removing duplicate
formula and tag ownership. Full sections retain their own introductions;
proof HTML, permanent tags and formal kinds remain unchanged.

## Validation and exact revisions

The frozen sixty-nine-packet selection at source
`3b2b5577db5182a2ca0e45fb53daf6f6daa48805` was built through the ordinary
unmodified Pome pipeline at `c2cfe85325e619cd7c858602b22bc7aba20e4b2c`.
The successful run finished on 24 October 2026 at 07:50:46 UTC and produced
7,930 entries, 836 topics and 25 shared chapters from ten sources. Its full
log SHA-256 is
`775dc0cec7e8e25178d604cdce37be2eddbc8ad8e77d56250a7c396feb4c19de`.

The existing suites passed 101 Python tests and 13 named JavaScript tests.
All ten standalone targets of the seven newly composed context chains passed
Chrome checks at desktop and mobile widths. Twenty initial viewport
screenshots were inspected. Math rendering, duplicate source IDs, JavaScript
errors and document overflow were checked across the loaded pages. External
comment services were outside that local check. This evidence is scoped to
the exact sixty-nine-packet revisions; it is not a fresh native-PDF review or
a review of every mathematical proof.

The eighty-packet candidate requires its own final exact source pin and
ordinary full build. Its provisional raw render has 647 source records;
that number is not a final canonical collection count. Prior build evidence
is retained separately and must not be relabeled as an eighty-packet success.
Pome PR19 remains unmerged, and no publication is asserted by these receipts.

## Reproducing a build

Use a clean genuine Git checkout at the source revision in `books.json`,
selected by `ANALYTIC_METHODS_SOURCE_DIR`. The five older Gerby-Literature
adapters may share a separate clean checkout of their registered main
revision; `CAO_PAUN_SOURCE_DIR` selects the independent Cao–Păun pin.
Build provenance comes from the actual Git commit, not from a materialized
directory with a substitute commit.

The standard commands remain:

```sh
.venv/bin/python -m unittest discover -s tests
node --test tests/*.test.mjs
.venv/bin/python scripts/build.py --fetch
```

The TeX environment needs the genuine `doublestroke` package (`dsfont.sty`)
in addition to the dependencies in the main README. The successful frozen
build supplied the official CTAN package through the normal TeX search paths;
no diagram source, font stub, build check or export guard was substituted.
Targeted browser checks follow the owner's 23 October instruction in
`AGENTS.md`: use them for affected rendering, layout, navigation or interaction,
and state the exact scope of any reused evidence.

Publication remains a separate action. This integration adds no formal proof
mapping and makes no claim that the retained external geometric inputs have
been proved internally.
