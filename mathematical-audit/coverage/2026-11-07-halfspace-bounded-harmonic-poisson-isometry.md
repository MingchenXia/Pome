# 2026-11-07 incremental coverage: half-space harmonic traces

**Production main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. **Current-ToC inventory:** 25 chapters / 747 numbered sections / 0 fully mathematically certified sections.

| Current ToC section | Exact source / integrated anchors inspected | Actual new coverage | Not certified / status |
| --- | --- | --- | --- |
| **3.2**, Kelvin transforms and half-space potentials (previously partly audited) | `docs/sections/kelvin-transforms-and-half-space-potentials/index.html` blob `f2615a5393af724c3996978212162f94911ff9d9`, physical lines **55–75, 80–136, 138–180**. Source `classical-potential-theory:1C8A330A`, tag `6BC86EEF03A9` (3.2.6); source `classical-potential-theory:BB6DAC3F`, tag `9ADD2DF19642` (3.2.12); source `classical-potential-theory:E7E82020`, tag `AB2849CD8791` (3.2.13). | `POME-HALFSPACE-BOUNDED-POISSON-ISOMETRY-001`: independent bounded-harmonic classification and (L^infty) isometric trace, with verified unbounded-measure tail control, plus sharp contrasting unbounded examples. | **Selected proof only**; no whole §3.2 certification, no first-visit recount. Theorems 3.2.6 and 3.2.12 not independently re-proved in full. |
| **2.8**, Densities and differentiation of integrals (internal dependency, previously sampled) | `docs/sections/measures-and-distributions--densities-and-differentiation-of-integrals/index.html` blob `1b600ca8444edebc8e05e300cb86ae371e9f8535`, physical lines **7–46**; source `foundations-of-pluripotential-theory:43819F13`, tag `9790D3B21542`. | Hypothesis/conclusion match for the Radon domination (
ule M,dx'Rightarrow
u=g,dx'), (0le gle M), used as an internal dependency. | No certification of the whole density lemma's transitive proof chain, §2.8, or all measure results. |

**Ledger:** [classification](../ledger/2026-11-07-halfspace-bounded-harmonic-poisson-isometry.md) · [full mathematical proof](../reports/2026-11-07-halfspace-bounded-harmonic-poisson-isometry.md). All older errors, gaps, external inputs, genuine duplicates, verified repairs, and user-deferred items remain in their old classifications. Excluded Demailly regularization/Bergman/weighted L²/Ohsawa–Takegoshi/multiscale/positivity-loss work is **deferred-by-user**, not audited here. No build, tests, CI, formal verification, publishing, source, registry or permanent-tag modifications.
