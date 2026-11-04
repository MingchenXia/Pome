# 2026-11-05 additive classification — half-space Poisson boundary recovery

**Main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. **Status ledger entry:** `POME-HARM-HALFSPACE-VAGUE-BOUNDARY-UNIQUENESS-001`, **low / verified conditional deduction**. Original Theorem 3.2.6 and Theorem 3.2.12 **correct**, no repair of a false theorem or proof gap claimed.

| Finding | Current statement and exact tag | Verified new result | Unresolved dependencies and correction |
| --- | --- | --- | --- |
| `POME-HARM-HALFSPACE-VAGUE-BOUNDARY-UNIQUENESS-001` | §3.2.6, `docs/sections/kelvin-transforms-and-half-space-potentials/index.html` blob `f2615a5393af724c3996978212162f94911ff9d9`, physical lines 64–75, source `classical-potential-theory:1C8A330A` / permanent `6BC86EEF03A9`; weight `:358F89A3` / `8F7C774A9D89`. | Under the **printed weighted Radon hypothesis**, `h(·,t)dx` converges **vaguely**, for all `t↓0`, to the *unique* measure `ν`; every boundary atom is `(s_(d-1)/2) lim_(t↓0)t^(d-1)h(z_0,t)`. Direct compact/tail domination, no finite-total-mass or sequential-subsequence assumption. | Theorem 3.2.6's general boundary-measure *existence* construction and its compact-measure selection input remain unverified in this increment. Proposed additional corollary only; no body change. Earlier `POME-HARM-HALFSPACE-CONE-GROWTH-SHARP-001` handled the **vertical coefficient** separately and is **not** re-opened or relabeled. |

**Independent new proof-step check:** §3.2.2 Kelvin transform, source `classical-potential-theory:B1AA5815` / permanent `97BA27062B9F`, lines 16–49: direct Laplacian chain-rule cancellation including `d=2` verified, **not** a whole-theorem dependency certificate. **Context only:** §3.2.12, source `:BB6DAC3F` / `9ADD2DF19642`, kernel normalization `:E7E82020` / `AB2849CD8791`, lines 141–180.

**Resolved/unresolved/deferred ledger discipline:** This entry is *verified conditional deduction*, not `verified repair`; all existing confirmed errors, proof gaps, candidates, external dependencies, genuine duplications, verified repairs and resolved items retain their prior classification. All explicit owner-excluded approximation/regularization/Bergman/weighted-L²/OT/multiscale/positivity-loss work remains **deferred-by-user**. No full chapter/section certification.

[Full precise mathematical proof](../reports/2026-11-05-half-space-poisson-vague-boundary-uniqueness.md).
