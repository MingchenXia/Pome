# Classified finding — 2026-11-07 — positive-current support maximum

| Stable finding ID | Severity | Status | Reviewed main | Exact new mathematical coverage |
| --- | --- | --- | --- | --- |
| `POME-CURRENT-SUPPORT-MAX-DIRECT-BT-001` | low | verified repair **of proof route**, not false theorem | `b6933b772f41b45918f7e25ed1afbbb1fd892272` | Theorem 5.63.4 (source `demailly-complex-geometry:A8039435`, permanent `949B825CA873`), `docs/sections/positive-current-coefficient-bounds-and-support-maxima/index.html` blob `cb4c3d4e9d653b216cff05eaf23aafb2a01425ec`, physical lines 82–108; bounded BT 7.2.1–2 (source labels `foundations-of-pluripotential-theory:DE7531DE`, `:D16BD033`, permanent `254CDCCCAB5E`, `D9911E035563`), `docs/sections/bedford-taylor-products-and-local-capacity--bounded-potentials-and-recursive-products/index.html` blob `18bd2395f3b76941b2c677079c09eb6accc5a9cb`, lines 16–54 |

The general-psh step in the printed proof cites the separate smooth-decreasing-majorant lemma 7.31.1 at line 107. This note **does not assess or reopen that lemma**. Instead, for `b` above the boundary positive-part supremum, `v=max(u-b+epsilon*psi,0)` is *already locally bounded psh*: the maximum removes unboundedness below. Its BT product with the closed positive current is positive. Compact-support Stokes annihilates the positive trace mass; on `{u-b+epsilon*psi>0}`, locality gives `dd^c(vT)>=epsilon*dd^c(psi) wedge T`, and strict positivity detects the support. This proves the exact support maximum without approximating `u`.

**Sharpness:** p=0 permits a positive closed point mass with empty boundary support; without closedness, a nonnegative compactly supported smooth scalar current similarly defeats the conclusion. Both examples violate printed assumptions and are not false-theorem findings.

**Proposed edit:** optionally replace only the proof's general-psh paragraph with the direct argument, subject to separate source review. **Affected dependents:** uses of Theorem 5.63.4 on singular psh functions; no implication that BT 7.2.2's entire proof chain has been recertified. **Other ledger classifications:** unchanged. Excluded dedicated approximation/regularization etc. remains **deferred-by-user**. No new first visit or whole-section certification.

[Complete English proof](../reports/2026-11-07-psh-support-maximum-direct-bt-truncation.md).
