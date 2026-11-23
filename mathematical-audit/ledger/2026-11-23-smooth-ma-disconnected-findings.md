# 2026-11-23 — smooth Hermitian Monge–Ampère connectedness findings

Baseline main **b6933b772f41b45918f7e25ed1afbbb1fd892272**. Complete argument, exact primary blob SHA, tags, anchors and dependents: [report](../reports/2026-11-23-smooth-ma-disconnected-normalization-and-variational-rotation.md).

| Stable finding ID | Status / severity | Statement | Counterexample and proposed repair |
| --- | --- | --- | --- |
| POME-SMOOTH-MA-DISCONNECTED-GLOBAL-SCALAR-001 | **confirmed error / medium** | §14.2.1, source 3EE16849, permanent F33DA8C9DF9F, docs/sections/smooth-monge-ampere-equations--scalar-bounds-and-uniqueness/index.html:10–15 | Two disjoint compact curves, dV=ω, F=0 versus log 2; integration separately forces e^b=1 and 1/2. Require connectedness, or componentwise scalars plus compatibility. |
| POME-SMOOTH-MA-DISCONNECTED-UNIQUENESS-001 | **confirmed error / low** | §14.2.4, source E26E18C6, permanent 366AA2E61158, same file:50–64 | Two normalized smooth solutions differ by distinct constants on components. Scalar equality b=c is true; replace globally constant with locally constant or require connectedness. |
| POME-SMOOTH-MA-DISCONNECTED-C0-ESTIMATE-001 | **confirmed error / medium** | §14.3.5, source C569075E, permanent EEF74F1DEBB8, docs/sections/smooth-monge-ampere-equations--the-potential-bound-from-weighted-integration/index.html:108–149 | u_M=0 on one component, −M on the other has η=ω, Λ=1, global sup 0, unbounded norm. Require connectedness or componentwise normalization. |

**Downstream conditional, not a fourth standalone finding:** §14.4.1 has a surviving componentwise-constant kernel despite the one global linear mean condition; §14.6 relies on the failed global existence/estimate and must carry the corrected hypothesis. **Unaffected:** §14.7's positive-exponential comparison removes the additive kernel. No verified repair has been applied, and no full upstream verification is claimed. All excluded regularization programmes remain deferred-by-user.
