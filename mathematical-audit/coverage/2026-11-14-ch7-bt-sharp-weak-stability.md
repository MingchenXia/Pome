# 2026-11-14 precise chapter/section coverage delta

**Reviewed main SHA:** `b6933b772f41b45918f7e25ed1afbbb1fd892272` (current navigation: 25 chapters, 747 unique numbered sections). **Review branch at start:** `e5ee9af141323083fa757a2487fa78ea1d4853aa`.

| Chapter/numbered section | Actual session reading | Integrated main path / blob and tags | Result | Remaining coverage |
|---|---|---|---|---|
| 7 / §7.2 Bounded potentials and recursive products | Direct reading of Definition 7.2.1 lines 16--25; Prop. 7.2.2 lines 29--77; CLN Thm 7.2.5 lines 98--119; Prop. 7.2.6 lines 125--155; exact signed telescoping and trace bound | `docs/sections/bedford-taylor-products-and-local-capacity--bounded-potentials-and-recursive-products/index.html`, blob `18bd2395f3b76941b2c677079c09eb6accc5a9cb`; tags `254CDCCCAB5E`, `D9911E035563`, `2A84C325AB58`, `2F39A3F97E8E` | `POME-BT-UNIFORM-BL-SQRT-SHARP-001`, conditional quantitative corollary, original claims not refuted | Only selected proof portions and a new corollary, not all §7.2 upstream hypotheses and dependencies |
| 7 / §7.3 Decreasing continuity and symmetry | Cross-read Theorem 7.3.7 statement lines 132--139, initial symmetry proof at line 148 as internal input; no reproof of remaining long decreasing-limit argument | `docs/sections/bedford-taylor-products-and-local-capacity--decreasing-continuity-and-symmetry/index.html`, blob `96a9e39e85fab5774ebdac0c6d9d006338a4e42c`; source `foundations-of-pluripotential-theory:8B1F9B78`; tag `D87C13B3250A` | Internal conditional dependency only | No whole-section or transitive certification |

**Actual new first proof visits:** 0 (both sections previously partly visited). **Whole-section certificates:** 0. No other chapter/section coverage changed. Earlier findings and tags are preserved. [Report](../reports/2026-11-14-bt-sharp-bl-weak-stability.md) · [ledger](../ledger/2026-11-14-bt-bl-weak-stability.md).

**Explicit exclusions:** Demailly approximation/regularization and dedicated Bergman/`L^2`/Ohsawa--Takegoshi/multiscale-atlas/positivity-loss programme stay **deferred-by-user**; no new mathematical scrutiny of them. No source edits, global proofs, CI, builds, project test suite, or publication.
