# Exact coverage increment — 2026-11-14 — diagonal higher Hessian masses

Reviewed **production main** `b6933b772f41b45918f7e25ed1afbbb1fd892272`, current numbered ToC baseline **25 chapters / 747 sections** (no independent regeneration). The review branch parent checked before this increment is `f0526c28500ad1b49ece7740bf2b0895e399b949`.

| Section | Current main file, blob | Printed anchors and labels | Actual inspection |
| --- | --- | --- | --- |
| §8.1 | `docs/sections/complex-hessian-equations/index.html`, `5331b937ccdaba51f1ec006d5e72dc84f7addfbf` | line 7, section permanent `CFD38285654D` | Actual scope \(2\le m<n\), read |
| §8.9 | `docs/sections/complex-hessian-equations--bounded-potentials-and-recursive-hessian-currents/index.html`, `117b866408974cdf706bf305df75e35e1b8affde` | lines 36–56 (recursion), 83–115 (shifted product); (8.9.5) `17FA1BFF2491`; Thm 8.9.6 `non-kahler-pluripotential-theory:61CC9D08` / `846671D5582A` | Selected definitions, expansion and positivity/local identification checked; upstream not transitively certified |
| §8.10 | `docs/sections/complex-hessian-equations--sobolev-capacity-and-two-hessian-factors/index.html`, `25f25433cb9b17de6715a5b05f8b3c15b95a18cd` | lines 185–205 Lemma 8.10.6 `:350D7B3A` / `2A6BE9847309`; lines 209–246 Example 8.10.7 `:36B886BE` / `AEB4F2397BBF` | Whole two-factor displayed example and codimension-two capacity proof reread, checked hypotheses against diagonal all-degree extension |
| §8.11 | `docs/sections/complex-hessian-equations--local-capacities-and-decreasing-products/index.html`, `115d285f6b1f76d284463c396e7e87db2b9dbdc3` | lines 281–293 Thm 8.11.12 `:B227378C` / `C044CD1C65C4`; 301–331 as downstream context | Joint weak product identification read as conditional input; no full capacity induction certification |

Prefix `non-kahler-pluripotential-theory` applies to abbreviated source labels above.

**Coverage counters:** all §§8.1, 8.9–8.11 were already partly sampled in this branch. **0 newly first-visited numbered sections, 0 newly fully certified sections.** New work is one explicit, all-degree, diagonal product construction with a self-contained tensor-product calculation. The actual indexed ToC inventory remains 25/747; this is **not** 747 mathematical certifications.

**Findings:** [report](../reports/2026-11-14-diagonal-hessian-higher-codimension-sobolev-polar.md), [classified ledger](../ledger/2026-11-14-diagonal-hessian-higher-codimension.md), status `verified conditional deduction`; no original theorem refuted. The exact current hypotheses \(2\le m<n\) avoid the prior false-positive endpoint objections.

**Dependencies and exclusions:** §8.11.12 and §8.9.6 are conditional upstream for identifying Pome's recursive current with the local smooth tensor-product limit. Demailly regularization and the excluded Bergman/\(L^2\)/OT/multiscale/positivity-loss programme stay **deferred-by-user**. No project tests, builds, CI, production modifications, or publication.
