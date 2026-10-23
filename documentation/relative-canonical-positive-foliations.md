# Relative canonical bundles and positive foliations

The source `cao-paun-foliations` selects the reviewed Cao–Păun contribution
through `contributions/cao-paun-foliations.tex` in Gerby-Literature. Its
`books.json` registration pins the exact reviewed source edition used for
ordinary export, independently of later advances on `main`.
`CAO_PAUN_SOURCE_DIR` may select a genuine clean checkout of that
revision for a local build. Registration enables export; it does not
establish a merge, public deployment, or mathematical formalization.

The selected material consists of twelve reviewed proof packets covering
restricted Lelong numbers, singular-metric vanishing and section
envelopes, relative canonical positivity, restricted concentration and
conormal algebraicity, movable slopes, positive foliations, cotangent
quotients, and deformation of canonical pseudo-effectivity. It preserves
the hypotheses of each local deduction. In particular, the relative
canonical theorem requires its rational Hodge and fiber-vanishing
conditions. The general relative-canonical conjecture and the question
about numerical dimension on a maximal rationally connected quotient
remain a conjecture and a question.

## Subject placement

The twenty-two mathematical source sections join five existing chapters.
The source history joins the shared subject history at the end of the
project. No new source-by-source reading chapter is introduced.

| Shared chapter | Added subjects |
| --- | --- |
| Lelong numbers, multiplier ideals, and regularization | Smooth blowups and restricted Lelong numbers; projective-bundle integration; diagonal logarithmic weights; anisotropic concentration; singularities along a compact center |
| Complex spaces and modifications | Local projectivity from relative positivity; projective Hartogs extension; conormal positivity; the local leaf quotient; holomorphic forms and positive foliations; covering rational curves; deformation of canonical pseudo-effectivity |
| Cohomology, positivity, and geometric loci | Strictly positive singular metrics; Euler characteristics under flat twists; singular bundle determinants; relative canonical positivity; maximal slopes; tensor products and involutivity; tautological metrics; numerical dimension of cotangent quotients |
| Sections, graded series, and Okounkov bodies | Flat twists of adjoint section envelopes |
| Problems in pluripotential theory | The relative-canonical conjecture and cotangent-tensor numerical-dimension question |

All reader locators are generated after placement. Source labels and
permanent tags do not depend on chapter numbers. The ordinary source
export contains 65 tags: 23 section headings, 36 theorem-like records
including the two open statements, and six equations. More explicitly,
its non-section kinds are eight
theorems, sixteen lemmas, five propositions, five corollaries, one
conjecture, one question and six equations. These are source inventory
counts, not claims of new independent Pome theorems or formal proofs.

The local covering-curve lemma is independent of the positive-foliation
and cotangent-quotient conclusions. The foliation proof uses Fujiki's
external deformation theorem directly where needed, so a forward
reference to the later canonical deformation consequence is not used as
a premise. Chapter grouping does not replace the lemma-level dependency
review.

## Reader context and canonical reuse

The native ambient convention is preserved in every mathematical
section and independently displayed record: ambient manifolds are
connected unless stated otherwise, while fibers may be disconnected and
the section envelopes are treated componentwise. The adapter adds this
existing convention to displayed HTML only. It leaves statement TeX,
proof HTML, labels and permanent tags unchanged; the history record does
not receive a mathematical convention paragraph.

Standalone statements and equations additionally receive the separately
reviewed native setup needed to interpret them. The adapter binds each
selected context to exact source proof and rendered-fragment hashes, adds
only that recorded context, and preserves original statement TeX and proof
HTML. A small number of continuous sections receive the reviewed link back
to setup in an earlier section. This restores hypotheses and definitions
that the native manuscript places before the extracted record; it does not
create a new theorem or alter permanent tags.

The contribution reuses 34 reviewed canonical Pome interfaces at 35
specific consumer pairs. It does not replace a result merely because an
old source number resembles a current locator. The reviewed source
selection distinguishes canonical statements, additional deductions,
and different hypotheses. Existing mathematical content, proof guards
and tag mappings remain in place.

Major attribution joins `history--positivity-and-hermitian-volume`.
The source history alias and raw historical prose fingerprint are
registered in `reading/history/registry.json`; the original source prose
remains available through Sources. Fifteen bibliography identities are
deduplicated with the shared references. Exact PT `1409.5504v1` and HPS
`1611.08768v2` locators remain beside the necessary mathematical inputs,
so an existing bibliography identity does not obscure the consulted
statement version. Repeated per-entry Sources paragraphs are not added.

## Exact export boundary

The adapter is an exact copy of the accepted
`integrations/S0082/cao-paun-foliations.py.in` in Gerby-Literature. Its
SHA-256 is
`036dc0a5faaf33fd9a23b79bd866ad322f8bae4952af568f8791482bd49d4f2b`.
It checks the source manifest and all eighteen allowed payload files
against both their reviewed hashes and the actual Git HEAD bytes. The
manifest includes the entrypoint, twelve portable proof fragments,
bibliography, canonical reference map, reviewed layout, open statements
and historical attribution. Retained source papers and private research
records are outside the public export graph.

The strict source preparation also retains the exact earlier public
payload hashes and input graphs. Compilation or export does not amend
mathematical review evidence; each proof has its own exact-byte review
and any accepted display transformation is recorded separately.

## Explicit external theorem inputs

`proofs/open-dependencies.json` records nine precise interfaces at their
actual consuming tags. They cover relative pluricanonical Bergman
variation; analytic base change and Euler characteristics; the
multiplier-ideal direct-image metric; movable tensor semistability;
compact-leaf cycle families; geometric flattening and relative rational
quotients; the projective rationally connected section theorem;
projective canonical uniruledness; and Fujiki deformation of
uniruledness.

Each row states its exact consulted versions, hypotheses, consumer
fingerprints, actual bounded reading scope, remaining external scope,
reason and next action. A consumer tag does not identify a new locally
proved external theorem. The local submean/Jacobian, determinant,
finite-filtration and neat-model calculations do not by themselves
reconstruct these deeper theories. Existing Hironaka and Demailly
elimination dispositions are preserved.

## Validation and publication boundary

Before publication, run ordinary exports from the accepted real source
commit, the complete Python and JavaScript suites, and the complete
nine-source build with numbering, deduplication, source-history and local
link checks. The export must be repeatable and retain the exact open
statement kinds. Compare every earlier source tag and canonical mapping
with the previous edition.

Desktop/mobile review must cover every new mathematical subject and
formal statement, representative existing pages from all earlier sources,
the source index, shared history and bibliography, and equation, tag,
footnote and citation behavior. The existing Kelvin-transform,
Bedford–Taylor, Klimek Green-function and Demailly Morse-row checks remain
regressions. A successful local preview does not establish an accepted
merge or live publication; those require their own exact commit and
inclusion receipts.
