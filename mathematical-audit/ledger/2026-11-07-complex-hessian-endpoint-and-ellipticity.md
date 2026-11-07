# Ledger increment — 2026-11-07 — complex Hessian versus full real Hessian and ellipticity bounds

## POME-HESS-LOG-SINGULAR-C11-OBSTRUCTION-001
- **Severity / status:** low / verified conditional deduction. Original Lemma 8.5.1 is **correct**, not a confirmed error, full repair, or duplicate.
- **Reviewed main:** b6933b772f41b45918f7e25ed1afbbb1fd892272.
- **Exact location:** docs/sections/complex-hessian-equations--bounded-complex-hessians-and-elliptic-extensions/index.html, blob fdd9225b1d778e1debaf94f75ef65175d4bd4484, Lemma 8.5.1 source non-kahler-pluripotential-theory:835B5652 / permanent 89771FD1FD15 / physical lines 10–27.
- **Hypotheses and complete result:** on a complex flat torus of dimension n>=3, cut off (x^2-y^2) log sqrt(x^2+y^2) and convolve periodically. Uniformly bounded smooth approximants and dd^c coefficients, uniform convergence, and even omega+dd^c u_j >= omega/2 hold; the limit has unbounded full real Hessian and fails C^{1,1}. Calculation and distributional boundary-term proof in [report](../reports/2026-11-07-complex-hessian-sharp-regularity-and-ellipticity.md).
- **Proposed correction:** none needed. Optional accurate sharpness remark in separately reviewed content patch, not on audit branch.
- **Affected dependents:** §§8.5–8.8 regularity cannot assume C^{1,1} merely from bounded complex-Hessian coefficients.
- **Open:** the externally cited Evans–Krylov–Caffarelli regularity step remains unverified here; no blanket theorem certification.

## POME-HESS-TWO-ELLIPTICITY-BOUNDS-SHARP-001
- **Severity / status:** low / verified conditional deduction. Lemma 8.5.3 is **correct** under both standing restrictions, not a false theorem.
- **Location:** same main HTML/blob; Lemma 8.5.3 source non-kahler-pluripotential-theory:B1F0AA6B / permanent BAC60298D0F2 / physical lines 62–110. Supporting Lemma 8.2.5 source non-kahler-pluripotential-theory:53FFB5F3 / permanent 7710D01DF6F5, docs/sections/complex-hessian-equations--the-admissible-cone/index.html, blob 925e6109ab7d800cde9bec4b0487842b2e6877a8, lines 104–130.
- **Hypotheses / calculations:** n=3,m=2, Gamma_2 matrices diag(t,t^{-1},0) with fixed sigma_2 and unbounded trace, and diag(1,epsilon,0) with bounded trace and sigma_2 tending to zero. Both have derivative spectra containing eigenvalues tending both to zero and infinity. Exact formulas in report.
- **Proposed correction:** none. Optional separate sharpness remark; do not weaken either K hypothesis.
- **Affected dependents:** the uniform real elliptic tangent-plane extension and §§8.5.4, 8.6–8.8 estimates require both controls. Distinct from prior sharper coordinatewise derivative **coefficient** finding POME-HESS-SHARP-DIAGONAL-DERIVATIVE-001.

**Coverage and exclusions:** selected already partly sampled §8.5, §8.2 context; 0 new first visits / 0 full mathematical-section certifications; main inventory 25/747/0. Historical statuses unchanged, excluded Demailly regularization/Bergman/L2/OT/multiscale/positivity-loss still **deferred-by-user**. No production/code/site/CI/test/formalization changes.
