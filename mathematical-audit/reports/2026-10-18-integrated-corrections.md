# Integrated audit corrections and historical synthesis

Date: 18 October 2026 (Asia/Shanghai).

Reviewed reading baseline: `66f8176be2a006b9404ae6db49ee15621dea5523`.
Retained audit head: `4eced13357cd108d1c2b72fad38d6280ee0ffb9f`.
The author's current request authorizes production corrections, consolidation into
`main`, removal of surplus branches and PRs, and rewriting the historical chapter.
It supersedes the older audit-only publication boundary.

## Dispositions

| Finding | Integrated disposition |
| --- | --- |
| POME-CAP-001 | Corrected. The monotone-net proposition asserts local capacity convergence on an open set, and global convergence for `U=X`. |
| POME-XREF-001 | Corrected before numbering. Descendants follow their canonical statement, including through absorbed clauses. Permanent equation tag `EF5655B5F536` is unchanged. |
| Adjacent weighted convergence theorem `272876B00528` | Internal proof supplied using the already proved bounded weighted Bedford–Taylor theorem and capacity comparison. |
| POME-DUP-001 | Retain the reviewed equivalent canonical definitions; no further mathematical merging. |
| Verified coherence/Richberg deductions | Retain the audit records. They did not identify an additional false theorem needing a production repair. |
| Demailly approximation and its dedicated analytic prerequisite programme | Deferred by the author. No approximation theorem, positivity estimate, or multiplier-ideal threshold is strengthened or certified here. The local Bergman reference suggestion belongs to this deferred programme. |
| Broad external-dependency and chapter-coverage candidates | Remain candidates, not newly confirmed errors or completed whole-book verification. |

## Capacity: quantifiers, proof, and uses

The existing definition of convergence in capacity on **all** of an open set is
preserved. A separate local definition tests both exceptional inequalities on
every compact subset. The displayed proposition is corrected by a fingerprinted
reading edit, preserving its statement root, clause anchors, permanent tags,
source TeX and source-statement guard. Its new proof is propagated into both the
standalone entry and its enclosing section.

For decreasing nets, quasi-continuity of the limit and compactness give a
finite-intersection proof on the complement of a small-capacity open set. For
increasing nets, Choquet selection and directedness yield a dominated increasing
sequence with the same regularized supremum. Its discrepancy is pluripolar;
quasi-continuity and Dini's finite-cover argument give uniform convergence off a
small-capacity open set. Monotonicity then controls the entire tail of the net.
Neither argument assumes a countable cofinal subset of the directed set.

The projective-line boundary-annulus counterexample is included, with admissible
circle-mass potentials proving exceptional capacity exactly one. Uniform
boundedness or replacing nets with sequences would not repair the former claim.

The superseded citation-only proof directions are fingerprinted and moved to Sources, preserving attribution. The adjacent weighted theorem is unchanged in strength. Its proof explains why
only local capacity convergence is needed for compactly supported current tests,
obtains a bounded quasi-continuous representative of the limit weight, and uses
a smooth local correction and expansion of mixed products. There is no appeal
to a potential for a nonclosed background form.

A structured-reference scan of all four reviewed active exports finds no direct
use of `prop:mono_psh_cap` outside the proposition and its enclosing section.
Existing local arguments use their separately stated local theorems; the global
definition is therefore not silently weakened for downstream applications.

## Placement and historical organization

`scripts/structure.py` resolves canonical non-heading parents after section
promotion, using both variants and absorbed clauses, and places descendants in
the parent's section before assigning reader numbers. The exact reported
canonical definition and its equation now have the same current-section prefix.
The shared map still supplies markup, mathematics, standalone titles,
breadcrumbs, navigation, and search; no reader ordinal is hard-coded.

The historical chapter is rewritten as ten continuous subject-based sections,
covering every mathematical chapter: classical potential theory; complex
positivity and singularities; nonlinear products; Hermitian geometry and volume;
Monge–Ampère and Hessian equations; singularity envelopes; energy and geodesics;
algebraic/convex/non-Archimedean methods; singular and locally conformal geometry;
and reading perspectives. It contains about 3,860 words.

All 51 former prose headings are accounted for by reviewed aliases, with source
HTML fingerprints requiring renewed review if the original notes change.
Original notes and bibliography remain under Sources. The seven formal
conjectures/problems and their heading move intact to a section of the problems
chapter. Former section/topic routes remain redirects, including fragment-specific routes into the reorganized sections. Prose aggregation is
excluded from the count of mathematical duplicate statements.

## Verification boundary

The Python suite passes 80 tests; the JavaScript suite passes 4 tests. New
regressions cover a moved equation inside an absorbed clause, historical alias
numbering, preservation of formal questions, changed-source rejection, and
incomplete historical coverage. The raw-export integration check verifies all
proof/prose/source guards, capacity correction propagation, historical coverage,
and the exact reported canonical definition/equation placement. `git diff
--check` passes.

A complete four-source build, local-link and locator validation, and desktop/mobile
browser verification are required before publication. The final delivery message
records their actual outcome. These software checks are separate from the
mathematical arguments and do not constitute formal verification. No CI workflow
or new recurring job is introduced.
