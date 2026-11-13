# Selected audit coverage — 2026-11-13 — Chapter 21 square-slope wall

**Reviewed main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. **Finding:** `POME-TORIC-SQUARE-DIAGONAL-ATOM-WALL-001`, low / verified conditional deduction, not an error in printed results.

| Section | Integrated content and stable tags | Direct review performed | Excluded from claim |
|---|---|---|---|
| §21.5 | `docs/sections/convex-analysis-and-toric-potentials--the-real-monge-ampere-measure/index.html`, blob `7089aa41ae2422b1bd6b5094e46668cbc8ed37be`. Theorem 21.5.1 source `foundations-of-pluripotential-theory:4A0FAEB3`, permanent `409656CC47D4`, physical lines 10–39; Theorem 21.5.2 source `:6403CF44`, permanent `F4072D9ED060`, lines 43–85. | Re-read normalized Alexandrov definition, conjugate-gradient pushforward, proof of vague convergence and exact slope-body/full-mass statements; independently derived the entire three-regime 2D piecewise-affine family, Legendre costs and measure weights. | Did not certify arbitrary-convex subgradient measurability, general subsequential compactness, or the mixed real MA uniqueness proof. |
| §21.6 | `docs/sections/convex-analysis-and-toric-potentials--compact-convex-envelopes-and-full-mass-limits/index.html`, blob `b3b4e34fff767a717df812a381f905589b257fb3`; Lemma 21.6.1 source `:30FFD831`, permanent `FCDAD9CEC8CE`, physical lines 10–28; Lemma 21.6.2 source `:55EDF0D7`, permanent `F2FABB0A312F`, lines 32–46. | Checked the precise finite-mass hypothesis and its narrow consequence, convex-envelope compatibility of the explicitly computed conjugates, and the stronger but *false* TV inference by exact positive/negative parameter wall calculations. | General capacity, toric-to-complex MA, and unrelated convex envelope claims not certified. |

These sections had already been selectively sampled. **Newly first-visited numbered sections: 0. Newly fully certified sections: 0.** Current production table of contents remains **25 chapters / 747 numbered sections**, with **zero fully certified numbered sections**. This is an additive proof-level coverage record, not a retroactive chapter audit.

[Complete proof](../reports/2026-11-13-square-tropical-monge-ampere-wall.md) · [classification](../ledger/2026-11-13-square-tropical-monge-ampere-wall.md).

**Deferred-by-user:** Demailly approximation/regularization and its dedicated Bergman/L²/OT/multiscale-atlas/positivity-loss completion programme are untouched.
