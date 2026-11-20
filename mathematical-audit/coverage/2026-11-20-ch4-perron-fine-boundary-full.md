# 2026-11-20 — Chapter 4 Perron/fine-boundary direct coverage

**Baseline:** current production main **b6933b772f41b45918f7e25ed1afbbb1fd892272**, review branch **review/mathematical-audit**. The live Table of Contents still has 25 chapters / 747 numbered sections at this main revision. Historic first visits are **LEGACY-UNRECONCILED**, not asserted as newly reviewed.

| Scope | Exact integrated file / main blob | Physical lines | Scope audited | Status |
| --- | --- | --- | --- | --- |
| §4.4 Perron theory and fine boundary limits | docs/sections/perron-theory-and-fine-boundary-limits/index.html / 4bc2fb9317e2b6f6bb5b2d90208c677da8275eba | **7–381** | Entire mathematical section, all statement/proof paragraphs including compactified theory and Wiener test | **THIS-RUN-FULL; LEGACY-UNRECONCILED**; not transitive certification |
| §4.1.16/.19/.21 capacity and equilibrium normalization | docs/sections/potentials-energy-and-capacity/index.html / 4962a7cd576a64cb47fa0955dcc80cf87c3da9d1 | **450–482, 560–625, 628–642**, selected | Capacity and relative Green kernel prerequisites for planar model only | **CURRENT-PARTIAL**; §4.1 not fully reviewed here |

**New:** one conditional mathematical deduction, **POME-WIENER-PLANAR-SUPEREXP-LOGLOG-001**, with uniform planar relative-capacity proof and sharp log/loglog transition; [full report](../reports/2026-11-20-planar-wiener-superexponential-obstacles.md). The pre-existing **2026-10-30 d≥3** model is retained, not repeated or reclassified.

**Counts for this run:** **+1 entire direct section (§4.4)**, **+1 selected prerequisite section (§4.1)**, **+0 complete upstream proof-chain certificates**, **+0 newly confirmed printed errors**, **+1 new verified conditional deduction**. This does not turn any of the other 746 sections into certified work.

**Outstanding:** upstream fine-topology, sweeping, exterior Kelvin/lowering, polar discrepancy, and full Perron-integral representation remain dependent on established inputs rather than being independently reproved here. The excluded Demailly approximation/regularization and dedicated Bergman/L²/Ohsawa–Takegoshi/multiscale/positivity-loss work stays **deferred-by-user**, not solved or certified. Documentation only; no tests, builds, GitHub Actions, source editing, or publishing.
