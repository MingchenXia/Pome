# 2026-11-09 classified finding ledger: nilpotent holomorphic power rates

| ID | Severity | Status | Target | Judgment | Proposed patch |
| --- | --- | --- | --- | --- | --- |
| POME-STEIN-NILPOTENT-POWER-RATE-001 | low | verified conditional deduction | §9.32.6, demailly-complex-geometry:BA15E5E8, permanent FE34E9B148D1, physical lines 95–106; production main b6933b772f41b45918f7e25ed1afbbb1fd892272 | Printed theorem **correct**. On \(X_k=\{w^k=0\}\) with \(f=a+w\), scalar \(|f|=a\) but a continuous intrinsic seminorm has \(p(f^m)=\binom m{k-1}a^{m-k+1}\). Therefore the theorem's \(r>a\) is sharp; \(r=a\) fails to admit a uniform prefactor, with arbitrarily high polynomial losses. | Optional independent Example following Lemma 9.32.6. Keep all hypotheses, historical attribution, stable labels and permanent tags. |

**Exact proof:** [2026-11-09-nilpotent-holomorphic-powers-exact-rate.md](../reports/2026-11-09-nilpotent-holomorphic-powers-exact-rate.md). **Exact coverage:** [2026-11-09-ch9-nilpotent-powers-intrinsic-topology.md](../coverage/2026-11-09-ch9-nilpotent-powers-intrinsic-topology.md).

**Affected dependents:** (9.32.7) lifting/convergence criterion and Proposition 9.32.8, source paragraph lines 109–134. They must retain a strict scalar-to-intrinsic decay margin; neither is proved false. The Fréchet-topology identification 9.51.5 remains an upstream dependency of the printed *general* lemma; the explicit model is independently established.

**Unresolved / deferred ledger:** No pre-existing findings are reclassified, repaired or certified here. Any general coherent-section continuity proof dependencies remain open under their existing statuses. The owner-excluded Demailly regularization, Bergman, \(L^2\), Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof-completion work stays **deferred-by-user**, without investigation or attempted closure.
