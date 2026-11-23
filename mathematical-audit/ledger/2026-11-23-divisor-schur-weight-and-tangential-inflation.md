# 2026-11-23 — Schur end weights and determinant concentration

Main reviewed: \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`. Audit branch: \`review/mathematical-audit\`. These findings concern integrated §10.25 (source \`non-kahler-pluripotential-theory\`) and **are not false source theorems**.

| Finding ID | Severity | Status | Exact source anchors | Correction / dependents |
| --- | --- | --- | --- | --- |
| **POME-SCHUR-ARBITRARY-END-WEIGHT-001** | low | verified conditional deduction | §10.25.1 source \`3CD86FAA\`, permanent \`D05A6736BCFF\`; (10.25.2) \`38956030\`/\`C974FBD89E14\`; (10.25.3) \`13887090B60F\`; (10.25.4) \`EA79C36F0DB1\`; blob \`326cea8684e76a3b0bdb41bb03c85e893aa47477\`, lines 28–101 | General complete end if Schur \(\ge cR^{-2}w(\tau)^2\) with positive continuous \(w\) and \(\int^\infty w=\infty\); necessary in product diagonal model; optional addition after §10.25.1 and conditional strengthening of Cor. 10.25.5. |
| **POME-DETERMINANT-ONLY-HERMITIAN-END-FAIL-001** | low | verified conditional deduction | §10.25 introduction lines 7–26 and equation (10.25.2), source \`38956030\`, permanent \`C974FBD89E14\` | On \(E^2\setminus(\{0\}\times E)\), \(T=\omega_1+e^{\tau^2}\omega_2\) is incomplete although \(\det T\) dominates all fixed divisor powers, because \(\det B=e^{\tau^2}\) and Schur \(=1\). Tangential divisor is indispensable. This is **not** a counterexample to the more restrictive closed/MA equation hypotheses elsewhere. |

[Complete statement, proofs and limitations](../reports/2026-11-23-schur-integral-criterion-and-determinant-only-countermodel.md) · [Exact coverage](../coverage/2026-11-23-divisor-normal-length-and-complex-space-rotation.md).

The §10.24.1 selected proof and §9.4/9.5/9.8 complex-space review are not promoted to full transitive certification. Historical findings were not relogged. All excluded regularization and its dedicated analytic proof-completion programs remain **deferred-by-user**.
