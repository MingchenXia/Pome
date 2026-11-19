# Direct coverage — 2026-11-20 (Chapter 8)

| Section | Integrated path | Blob | Mathematical lines checked | Mode |
| --- | --- | --- | --- | --- |
| §8.1 (context only) | `docs/sections/complex-hessian-equations/index.html` | `5331b937ccdaba51f1ec006d5e72dc84f7addfbf` | 7–16 | hypotheses/context only |
| §8.2 (full) | `docs/sections/complex-hessian-equations--the-admissible-cone/index.html` | `925e6109ab7d800cde9bec4b0487842b2e6877a8` | 6–269 | direct all mathematical paragraphs, proofs of 8.2.3–10 and declared inputs |
| §8.12 (full) | `docs/sections/complex-hessian-equations--locality-and-maxima-of-bounded-potentials/index.html` | `8750df56019c14e16704607ca20fa8b90f137fb0` | 6–170 | direct 8.12.1–5 and proof-dependency check |

**Main commit:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.

**New direct whole sections:** 2. **Selected context:** 1. **Full upstream proof-chain certifications:** 0. Earlier partial work in §§8.2 and 8.12 remains historically unreconciled; no first-visit claim.

**Findings:** [full report](../reports/2026-11-20-hessian-two-cone-lorentz-locality.md), [classification](../ledger/2026-11-20-hessian-two-cone-lorentz.md). The special `m=2` Lorentz calculation supplies a complete algebraic replacement of part of the declared Gårding input and proves the sharp negative and positive diagonal interval. The general `m>2` Gårding theory, nonsmooth viscosity/distributional equivalence, and §8.11 weighted capacity/monotone convergence are **not** independently verified. Nothing in the user-excluded Demailly/Bergman/L²/OT/multiscale/positivity-loss programme was reopened. No builds/tests/CI/site/main/source/tag changes.
