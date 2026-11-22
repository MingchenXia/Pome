# Direct coverage — 2026-11-23

Reviewed **main** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. Directly read the currently integrated mathematical body of **four** different numbered sections, without asserting historical first visits or full mathematical verification of any complete dependency chain.

| Current TOC section | Integrated file under `docs/sections/` | Physical mathematical lines | Main blob SHA | Status |
| --- | --- | --- | --- | --- |
| §10.66 sphere cohomology | `spectral-sequences-support-and-cup-products--the-sphere-calculation/index.html` | 8–24 | `2a90367f355fa5c9a2b27a0746d388e3877ae503` | whole direct |
| §10.67 tensor and Tor | `spectral-sequences-support-and-cup-products--algebraic-tensor-products-and-universal-coefficients/index.html` | 7–249 | `fc7abc376ab34a4f6436d92820088f13f1bf69f9` | whole direct |
| §10.68 injectives and Ext | `spectral-sequences-support-and-cup-products--injective-modules-and-extension-modules/index.html` | 7–210 | `a26517e086ac8ed8c5d590cad04b203a2f602f99` | whole direct |
| §11.27 Ricci-flat surfaces | `gauduchon-metrics-and-linear-mass--ricci-flat-kahler-surfaces/index.html` | 7–168 | `119ac604fd60b412ecb7d51910cfcecc04b3b7cf` | whole direct; one confirmed false unqualified theorem |

**New:** `POME-RICCI-FLAT-KAHLER-RCPOSITIVE-DISCONNECTED-001`, medium / confirmed theorem statement error; counterexample X=K3 disjoint union flat 2-torus. Full [report](../reports/2026-11-23-ricci-flat-disconnected-rc-positivity-and-tor-ext-direct-audit.md) and [finding](../ledger/2026-11-23-ricci-flat-tangent-disconnected.md).

**Not certified:** flabby/Godement and cohomology background; finite spectral-sequence elimination and chain comparison; projective/injective resolution upstream; detailed Ricci-flat curvature Bochner formulas; and the §11.26 conformal Poisson result until its known connectedness repair is applied. No complete transitive verification, project tests or builds.

**Deferred-by-user, not audited or certified:** Demailly approximation and regularization, dedicated Bergman, L², Ohsawa–Takegoshi, multiscale atlas and positivity-loss completion programmes. No source or site modifications.
