# 2026-11-09 — Gauduchon derivative cofactor inversion: classified finding

| Stable ID | Severity | Status | Scope |
| --- | --- | --- | --- |
| `POME-GAUD-DERIVATIVE-COFACTOR-STABILITY-001` | low | **verified conditional deduction** | §12.5 Proposition 12.5.1, with §§12.2–12.3 as unverified hypotheses |

**Reviewed main SHA:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.

**Primary integrated reading edition:** `docs/sections/a-gauduchon-variational-volume--recovering-a-positive-class-from-its-gauduchon-derivative/index.html`, blob `829d10abfa8f92c7c77fde66704adb6486ccdc93`; §12.5.1 source `non-kahler-pluripotential-theory:765CFEAC`, permanent `4BBB232A044C`, lines 22–43, setup lines 7–19. Dependencies crosschecked: §12.2.3 source/permanent `non-kahler-pluripotential-theory:876DF057/2DB664A6EFDF`, lines starting 59, blob `9ec67161d46b3ba20afa1b1c9a0c84f29322763e`; §12.3.2 source/permanent `non-kahler-pluripotential-theory:6D3F0AB8/94AFD9E43DE0`, lines starting 34, blob `d94e3fc055b0642a86495c27ad8f5af6f24f17d1`.

**Precise result:** Fix a Hermitian reference `omega_0`, common smooth positive `mu=rho omega_0^n`, and `theta_i in P` with positive variational values `lambda_i`. For derivative representatives `Xi_i`, define the positive matrices `B_i` uniquely by `Xi_i wedge eta = trace(B_i H_eta) omega_0^n/n`. Then the solution Hermitian matrices satisfy `H_{Omega_i}=lambda_i rho^{1/n}(det B_i)^{1/n} B_i^{-1}`. Under `aI <= B_i <= bI`, the inverse difference has the explicit bound `||Omega_1-Omega_2||_C0 <= ||rho||_inf^{1/n} ((b/a)|lambda_1-lambda_2| + (2b/a^2) max(lambda_i) ||B_1-B_2||_C0)`. Complete cofactor/Jacobian and derivative-of-inverse derivation in the [English report](../reports/2026-11-09-gauduchon-derivative-cofactor-inversion-stability.md).

**Diagnosis:** The printed theorem and proof are **not false**. This is a new quantitative *consequence*, not a repair of a proven gap. Its PDE existence, differentiability and Gauduchon-minimizer premises remain **conditional external-to-this-review internal dependencies**. The ellipticity constants are hypotheses on the compared derivative matrices; no global bound or forward bi-Lipschitz estimate is asserted.

**Suggested source-side correction (not implemented):** optional independent Remark after Proposition 12.5.1 containing the wedge-normalized cofactor inversion and its ellipticity-bounded stability. Preserve all source versions, history, tags and original proposition.

**Potential affected dependents:** quantitative reconstruction from variational data in §12.6; no false downstream statement identified. **Coverage:** new subargument in already partly examined §12.5; §§12.2–12.3 statement crosschecks only; **0 new first visits; 0 full mathematical-section certifications; actual ToC 25 chapters/747 sections**. All old confirmed errors, gaps, duplicates and external dependencies untouched; owner-excluded approximation/regularization, Bergman, L², Ohsawa–Takegoshi, multiscale atlas and positivity-loss remain **deferred-by-user**. Audit Markdown only; no source/main/CI/build/publishing changes.
