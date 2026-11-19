# 2026-11-20 — Hessian cone and maximum-locality classification

## POME-HESS-TWO-CONE-LORENTZ-DUALITY-001
- **Status:** verified repair, *partial and audit-only*; **severity:** low.
- **Hypotheses:** Hermitian n-fold, `n>=3`, `m=2`, Hermitian matrices in the closed positive `2`-Hessian cone.
- **Target:** `docs/sections/complex-hessian-equations--the-admissible-cone/index.html` blob `925e6109ab7d800cde9bec4b0487842b2e6877a8`, lines 7–36 and 113–130; source/permanent tags `E3011B0D/C5A4D9AE83ED`, `99D246B6/B372916B922F`, `53FFB5F3/7710D01DF6F5`.
- **Finding:** `Gamma_2` is the future cone of the Lorentz quadratic form `Q(A)=tr(A)^2-tr(A^2)`; hence the dual cone, mixed positivity, and concavity of `sqrt(sigma_2)` have a complete internal algebraic proof.
- **Limit:** general `m>2` Gårding and nonsmooth viscosity/distributional equivalence are not proved. Neither theorem is refuted; the external input was explicitly declared.
- **Proposed correction:** optional precisely scoped `m=2` proof supplement, never a silent general-`m` substitution. [Complete proof](../reports/2026-11-20-hessian-two-cone-lorentz-locality.md).

## POME-HESS-TWO-CONE-SHARP-DIAGONAL-001
- **Status:** verified conditional deduction; **severity:** low.
- **Hypotheses:** `n>=3`, closed `Gamma_m` Hermitian `M`, `2<=m<=n`, unit `v`.
- **Target:** §8.2.5 lines 113–130, `non-kahler-pluripotential-theory:53FFB5F3/7710D01DF6F5`; §8.2.7 lines 159–179, `:25ADAEE1/B0643A9A1173`.
- **Finding:** `-((n-2)/n)tr M <= <Mv,v> <= tr M`. Both endpoints sharp for `m=2`; no sharpness claim for larger `m`.
- **Proposed correction:** optional remark refining the negative side of the existing valid `|M_{1bar1}|<=tr M`; do not extend absolute coefficient bounds to top degree `m`. [Complete proof](../reports/2026-11-20-hessian-two-cone-lorentz-locality.md).

## Other classifications
- **§8.12:** complete *direct* reading of printed 8.12.1–5 (lines 6–170, blob `8750df56019c14e16704607ca20fa8b90f137fb0`); no new confirmed error/gap. Upstream §§8.11.10–13 remain **external dependencies not certified here**.
- **Historical:** prior §8.2 and §8.12 selected reviews retained; neither is counted as a new first visit.
- **Exclusion:** all user-specified Demailly/Bergman/L²/OT/multiscale/positivity-loss proof programmes remain **deferred-by-user**, not resolved or certified.
- **Baseline:** main `b6933b772f41b45918f7e25ed1afbbb1fd892272`. Full-section direct increment **+2**; complete upstream-chain increment **+0**. No builds, tests, CI or source/site edits.
