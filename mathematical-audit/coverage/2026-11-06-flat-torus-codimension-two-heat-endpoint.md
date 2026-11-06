# Section coverage increment — 2026-11-06 — first selected heat-kernel endpoint model

**Actual reading ToC:** Chapter 3, §3.10 “Heat kernels on compact manifolds” (not a chapter-wide audit). **Reviewed production main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. Overall collection tracking is unchanged: **25 chapters, 747 numbered sections, zero completely mathematically certified sections**.

| Main integrated content actually read | Proven in this pass | Not established |
| --- | --- | --- |
| `docs/sections/heat-kernels-on-compact-manifolds/index.html`, blob `c59a1b3fab9433f1aae95db99adb4821857b5d8d`; Lemma **3.10.1**, lines **10–18**; selected proof of compact heat/Gaussian estimates **19–83**, source `transcendental-positive-cones:327DDB8B`, permanent `126365F8EBD6`. | Checked the sign (h_t=e^{-td^*d}), mass-one normalization and compatibility of the periodized flat-torus kernel with the printed heat convention. | No complete independent reconstruction of the general compact spectral theorem, elliptic regularity, Nash inequality, Moser iteration or Gaussian bound. |
| Same main HTML, Lemma **3.10.5** and proof, lines **85–105**, source `transcendental-positive-cones:DD00B1CA` / tag `56A174D59425`. | **New** complete flat-torus codimension-two growth/saturation calculation, exact (L^1) pairing rates for power and logarithmic fixed data, and proof that the (L^1) endpoint is not an $L^\infty$ limit or polynomial estimate; finding `POME-HEAT-CODIM2-LOGARITHMIC-L1-ENDPOINT-001`. | Generality of the theorem not independently certified, no specific downstream false statement, no full §3.10 certificate. |

**Unchanged categories:** prior resolved/unresolved/external items remain in their existing files; Demailly approximation/regularization and the dedicated Bergman, weighted-L2, Ohsawa–Takegoshi, multiscale-atlas, and positivity-loss proof-completion programmes remain **deferred-by-user**, not resolved or certified. Source, main, registries, tags, CI and publication not modified.

[English proof and precise hypotheses](../reports/2026-11-06-flat-torus-codimension-two-heat-endpoint.md) · [status ledger](../ledger/2026-11-06-flat-torus-codimension-two-heat-endpoint.md).
