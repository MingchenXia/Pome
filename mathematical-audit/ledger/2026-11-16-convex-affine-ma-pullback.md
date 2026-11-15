# Classified finding — 2026-11-16

**ID:** `POME-CONVEX-MA-GL-AFFINE-PULLBACK-MIXED-001`. **Severity:** low. **Status:** **verified conditional deduction** (not a confirmed error or proof gap).

- **Source:** main `b6933b772f41b45918f7e25ed1afbbb1fd892272`; §21.5 integrated blob `7089aa41ae2422b1bd6b5094e46668cbc8ed37be`, path `docs/sections/convex-analysis-and-toric-potentials--the-real-monge-ampere-measure/index.html`.
- **Exact proof anchors:** source `foundations-of-pluripotential-theory:4A0FAEB3` / permanent `409656CC47D4` / lines 10–40; source `:EAD83A50` / permanent `5D8A7A7D734E` / lines 99–159; mixed polarization source `:24CC29A7` / permanent `D38381F0AC43` / lines 135–159.
- **Hypotheses:** dimension (n\geq1); (F_i\) finite convex on all (\mathbb R^n); common real linear (A), translation (b), (\lambda_i>0), affine (\ell_i). No differentiability or coercivity assumptions.
- **Justification:** [complete report](../reports/2026-11-16-convex-real-ma-affine-pullback-and-rank-collapse.md) establishes the exact dual slope-map identity for invertible (A), (n!\)-measure covariance, polarization to all mixed cases, and zero n-volume of slope image for singular (A). Exact smooth and atomic checks isolate first- versus second-determinant powers; a small symbolic 2x2 check was actually run.
- **Conclusion:** printed §21.5.1 and §21.5.4 are **not refuted**; the affine theorem is an additional exact consequence. The general internal measure construction and underlying convex duality are **conditional inputs**, not newly transitively certified.
- **Suggested correction:** none to the printed theorem. Optionally document the distinction between one Jacobian factor for the **pushforward law**, two for the **smooth density**, plus rank-deficient collapse.
- **Affected dependents (not certified):** §21.6; §§21.12–21.13; §§19.2,19.7 coordinate-normalization conventions.
- **Scope:** previously partly visited §21.5, zero new first section visits or complete certifications; user-excluded regularization programs **deferred-by-user**. Public audit notes only; no main/CI/build/site writes.
