# Incremental exact coverage — 2026-11-07 — high-codimension PSH branch compatibility

Reviewed production main: `b6933b772f41b45918f7e25ed1afbbb1fd892272`. This is a **selected incremental mathematical check** in two previously partly reviewed sections; **zero new first-opened mathematical sections** and **zero entire-section certifications**. The actual ToC inventory baseline remains **25 chapters / 747 numbered sections**; its full section matrix in [SECTION_MATRIX.md](../SECTION_MATRIX.md) is not replaced by this additive record.

| Section | Actual new verification | Stable source / permanent identifier | Integrated path / main blob and physical lines | Status | Unchecked |
| --- | --- | --- | --- | --- | --- |
| 9.9 | Proposition 9.9.4's conclusion is *upper boundedness*, not removability. New explicit transverse `r`-branch `n>=2` model meets codimension condition but has no PSH extension for incompatible constants. | `foundations-of-pluripotential-theory:A6674849` / `B43080BD49F3` | `docs/sections/complex-spaces-and-modifications--plurisubharmonic-functions-on-reduced-spaces/index.html`, `d9d8091b530c9843e5a725b49af2400936aeaa3a`, lines 62–90 | Verified conditional deduction; theorem correct | Complete finite-projection proof and other §9.9 statements |
| 9.10 | Theorem 9.10.14 explicitly requires unibranchness; source's existing nodal-curve footnote is codimension one; new example shows failure without this hypothesis even at arbitrary codimension `n>=2`. Exact iff for branch constants and affine pluriharmonic models. | `sgpt:EEFC0C9A` / `C69D2F0ABA4F`; codimension-two clause `C2D00AE1EE6E` | `docs/sections/pluripotential-theory-on-unibranch-spaces/index.html`, `6edfa6b19fa7cdbaf0c2665389fa7b3ca338cdf4`, lines 110–155 | Verified conditional deduction; theorem correct | Positive extension proof's transitive inputs, global descents |

No new confirmed error, proof-gap closure, duplication, full mathematical-section certification, tests/builds/CI or publication. No user-deferred approximation/regularization/Bergman/weighted-L²/OT/multiscale/positivity-loss proof work was reopened.

[Complete argument](../reports/2026-11-07-high-codimension-branchwise-psh-nonremovability.md) · [classified ledger](../ledger/2026-11-07-branchwise-psh-nonremovability.md).
