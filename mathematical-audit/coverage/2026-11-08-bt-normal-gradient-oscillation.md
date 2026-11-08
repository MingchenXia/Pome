# Additive precise coverage — 2026-11-08 — normal-gradient oscillation in previously reviewed §7.14

**Main SHA:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. **Starting audit head:** `698bbdcd81a1f957375261543e41ab5b09d40ad4`. **Stable finding:** `POME-BT-NORMAL-TRACE-GRADIENT-OSCILLATION-001` (low / verified conditional deduction).
**ToC placement:** Chapter 7 *Local Monge–Ampère theory and capacity*, §7.14 *Gradients against positive currents*, permanent section tag `166A7FDE3C64`.
**Integrated page:** `docs/sections/bedford-taylor-products-and-local-capacity--gradients-against-positive-currents/index.html`, blob `520e13d0d2cc8e4a23e43bba61b940d7c5c1f8b2`.

| Actual reviewed item | Stable source / permanent tag | Physical anchor | Coverage judgment |
|---|---|---|---|
| Matrix density of positive current and energy identity (7.14.1) | `foundations-of-pluripotential-theory:DEE3D747` / `9148FE66924C` | lines 10–32 | Checked normalization in the line-current model. |
| Lemma 7.14.3, energy-gradient convergence, proof Step 1 | `foundations-of-pluripotential-theory:3CDA1967` / `8B33E7CC2E18` | lines 48–64, 69–84 | New complete explicit monotone-smooth sharpness example; not general proof certification. |
| Relative gradient measure identity (7.14.4) | `foundations-of-pluripotential-theory:7591087E` / `F48E1DFF8563` | lines 50–54, 102–109 | Tested exactly on an integration current and constant restrictions. |
| Downstream use in Theorem 13.3.1 | tag `8A125B338F90` | cited in §7.14 introduction line 7 | Dependency map only, not a new proof review. |

**Mathematical scope:** log-sum-exp entropy monotonicity, local-uniform monotone PSH convergence, exact current coefficient matrix, alternating normal derivative and failure of full trace $L^2$ convergence. Full [English proof](../reports/2026-11-08-bt-normal-gradient-oscillation.md) and [classification](../ledger/2026-11-08-bt-normal-gradient-oscillation.md).

**First-visit count:** zero. The existing SECTION_MATRIX row records an earlier direct §7.14 review (2026-10-22, `POME-BT-CURRENT-MULTICHAIN-001`); the new oscillating-normal-gradient proof is different from that multivariate chain-rule check. §13.3 is an existing downstream dependency and not a new first visit. **Fully certified sections:** 0. Current actual ToC baseline **25 chapters / 747 numbered sections / 0 complete mathematical certifications**. Prior findings and their statuses unchanged; Demailly approximation/regularization and dedicated Bergman/weighted-L2/OT/multiscale/positivity-loss programme **deferred-by-user**. Audit Markdown only, no production or website changes.
