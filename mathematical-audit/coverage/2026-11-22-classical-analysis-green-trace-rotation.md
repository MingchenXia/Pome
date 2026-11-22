# 2026-11-22 — direct coverage: classical harmonic analysis, Green potentials, selected trace

**Reviewed main:** b6933b772f41b45918f7e25ed1afbbb1fd892272. **Branch for notes:** review/mathematical-audit. This is a per-run direct-reading record, not an assertion of a first historical visit or a complete dependency certificate.

| Current ToC section | Present-main blob / path | Exact extent | Status |
| --- | --- | --- | --- |
| §3.3 Classical harmonic analysis | 75e982788e627af602981823a82863cbd36ee712; docs/sections/classical-harmonic-analysis/index.html | Entire mathematical lines 10–239: compact differentiation, ball averages, weak selection, cap coverings/differentiation, radial and nontangential limits, Bôcher and sphere reflection | CURRENT-DIRECT-FULL; prior historical coverage unreconciled |
| §3.5 Green functions and potentials | 63c74d1c4a0958633b42903a0e3a4526f42b7588; docs/sections/green-functions-and-potentials/index.html | Entire mathematical lines 7–205: lowering, Greenian domain existence, symmetry/exhaustion, Riesz decomposition, potential continuity and generalized Laplacian | CURRENT-DIRECT-FULL; prior historical coverage unreconciled |
| §20.2 The trace operator | 1f3a3e4f0317a308b43bd3df53dda84c5f3fa50a; docs/sections/the-trace-operator/index.html | ONLY selected lines 105–220, 352–440, 445–543, 565–635. Not the full section, not §20.2.28 or §§20.2.29–end | CURRENT-SELECTED; transitive dependencies unresolved |

**New status:** POME-CLASSICAL-BALL-AVERAGE-SHARP-GRADIENT-001, low / verified conditional deduction, no source theorem error. [Full proof and exact anchors](../reports/2026-11-22-classical-ball-averages-green-potentials-and-trace-rotation.md).

**Quantified delta:** +2 whole present-main sections directly read; +1 selected passage/section; +1 low conditional deduction; +0 confirmed errors, +0 complete transitive upstream certifications. Historical first visits are not inferred from legacy-unreconciled rows.

**Dependencies:** compact-metric Riesz representation and cube Lebesgue differentiation (§3.3), local Riesz/Harnack/harmonic reduction (§3.5) and §16.9/§18.1 model/distance premises (§20.2) are still not independently certified in full. Any trace theorem whose proof cites excluded regularization inputs retains only an unreviewed dependency mark. User-deferred Demailly regularization and dedicated Bergman/L²/OT/multiscale/positivity-loss programme remains excluded, unresolved and uncertified.

No tests, build, CI, main/source/registry/label/site modifications.
