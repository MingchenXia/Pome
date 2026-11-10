# POME-FT-JET-NILPOTENCE-THRESHOLD-001 — classification ledger

- **Date:** 2026-11-10.
- **Reviewed main SHA:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.
- **Severity:** low.
- **Status:** **verified conditional deduction**; original Proposition 9.58.3 and Proposition 9.60.1 remain correct. Neither a confirmed error, a proof gap in the source, a genuine duplicate, nor a verified repair.
- **Primary anchor:** `docs/sections/finite-type-algebraic-models-and-analytic-structure-sheaves--finite-type-models-and-nilpotent-structure/index.html`, blob `96eb7c1f6ee63ce6d222ed3f608a242a0a64b7f0`, source `demailly-complex-geometry:5EF3B92E`, permanent `72F3ADBDFF9A`, Proposition 9.58.3 at physical lines 35–55. Standing conventions at line 7; nilradical at lines 59–60.
- **Context/affected dependencies:** §9.59.1, source `demailly-complex-geometry:20E582B2` / permanent `476B5A661E43`, blob `4373897c66d3fae21cab98bec91fff3457d23ade`, lines 10–12; §9.60.1, source `demailly-complex-geometry:2090FB67` / permanent `57433F7B0D87`, blob `7a3c24deaab8602c3d2b4be2e31d739f02b5a657`, lines 10–31.
- **Finding:** centered dual-number maps identify with `Hom_k(m_x/m_x^2,k)`. For `A_m=k[t]/(t^m)` the exact `q`-jet criterion is `ord_e y>=ceil((q+1)/m)`; every nonzero tangent lifts through `q=m-1` but not through `q=m`. Same closed-point topological space and same first tangent dimension do not determine nilpotent order.
- **Proposed correction:** no source theorem correction. Optional new remark on jet lifting and on nonreduced canonicalization; retain the existing propositions.
- **Proof:** [dated complete argument](../reports/2026-11-10-finite-type-nilpotent-jet-threshold.md).
- **Coverage:** [exact boundaries](../coverage/2026-11-10-ch9-nilpotent-jet-threshold.md); 0 first visits, 0 full certifications, actual ToC 25/747.
- **Unresolved:** categorical/analytic upstream dependencies are not transitively certified. No other pre-existing findings were altered.
- **Deferred by user:** Demailly regularization and the dedicated Bergman/L²/OT/multiscale/positivity-loss proof programme, not reopened, resolved or certified.
