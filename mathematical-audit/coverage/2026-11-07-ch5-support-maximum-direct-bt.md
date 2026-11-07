# Additive exact coverage — 2026-11-07 — positive-current support maximum

**Current actual ToC:** 25 chapters, 747 numbered sections, zero entire sections mathematically certified. §5.63 (current tag `D5078EF0D73A`) and §7.2 have previously been partly reviewed, so **zero first visits**. Reviewed production main: `b6933b772f41b45918f7e25ed1afbbb1fd892272`.

| Current section | Main reading-edition file and blob | Exact statement, source/permanent tags and physical anchors | Newly checked reasoning | Not checked / scope limit |
| --- | --- | --- | --- | --- |
| 5.63 | `docs/sections/positive-current-coefficient-bounds-and-support-maxima/index.html`, `cb4c3d4e9d653b216cff05eaf23aafb2a01425ec` | Theorem 5.63.4, source `demailly-complex-geometry:A8039435`, permanent `949B825CA873`; lines **82–87** statement and **90–108** proof | Direct locally bounded truncation `max(u-b+epsilon*psi,0)`, BT positivity, Stokes, support detection; covers non-smooth, possibly unbounded-below psh without smoothing. Finding `POME-CURRENT-SUPPORT-MAX-DIRECT-BT-001` (**low / verified repair of proof route**); theorem not false. | Rest of §5.63 not rechecked; prior findings unchanged. No review of 7.31.1 or the excluded Demailly programme. |
| 7.2 | `docs/sections/bedford-taylor-products-and-local-capacity--bounded-potentials-and-recursive-products/index.html`, `18bd2395f3b76941b2c677079c09eb6accc5a9cb` | Definition 7.2.1, source `foundations-of-pluripotential-theory:DE7531DE` / permanent `254CDCCCAB5E`, lines **16–25**; Proposition 7.2.2, source `foundations-of-pluripotential-theory:D16BD033` / permanent `D9911E035563`, lines **29–54** | Exact locally bounded BT positivity, locality and closedness premises used in the alternative proof. | Full transitive proof chain not recertified. |

[Detailed proof](../reports/2026-11-07-psh-support-maximum-direct-bt-truncation.md) · [classified finding](../ledger/2026-11-07-current-support-maximum-direct-bt.md).

**Coverage arithmetic:** 0 newly visited ToC sections; 0 completely verified sections. No build, tests, CI, formal verification, public website change, or main/source/registry/permanent-tag edit.
