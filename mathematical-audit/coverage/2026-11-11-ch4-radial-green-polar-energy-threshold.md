# Exact selected coverage — 2026-11-11 — Chapter 4 Green energy

**Reviewed main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272` (unchanged during this session).  
**Branch:** `review/mathematical-audit`.  
**New stable finding:** `POME-GREEN-RADIAL-POLAR-ENERGY-THRESHOLD-001`, low / verified conditional deduction.

| Current ToC section | Actual inspection | Source tag and physical anchors | Audit level |
| --- | --- | --- | --- |
| §4.5 Green energy and Martin boundaries | Current Example 4.5.5 and exact construction of a finite-energy potential infinite at a polar singleton; §4.5.1 normalization; contextual comparison with Theorem 4.5.2 | `docs/sections/green-energy-and-martin-boundaries/index.html`; blob `976a90f2a5eba299658f73a1eee8b9d3fef8020f`; Example original `classical-potential-theory:898691BF`, permanent `61A5D2A82793`, physical line **71**; standing convention **7–13**; Theorem 4.5.2 permanent `CC3D1AD9179B`, lines **17–29** | **Selected proof-level model only**, not general energy/Hilbert/Martin verification |
| §3.5 Green functions and potentials | Planar unnormalized fundamental kernel convention, checked for disk model | `docs/sections/green-functions-and-potentials/index.html`; blob `63c74d1c4a0958633b42903a0e3a4526f42b7588`; §3.5.4 source chunk `classical-potential-theory:D6A0F97E`, permanent `870251679082`, physical **33–35** | Normalization only; no new proof-level count |

**Proven new quantitative facts:** exact radial measure and Green potential, no point/circle atom, total mass `gamma`, all potential moments finite iff `gamma*(q+1)<1`, exact energy for `0<gamma<1/2` and divergence at/above the sharp `1/2` family threshold. This **does not** repeat the earlier sphere-shell Green projection, Martin boundary, energy weak-vague, or Hilbert incompleteness examples.

**Counts:** Previously mathematically sampled §§4.5 and 3.5: **0 newly first-visited numbered sections**, **0 fully mathematically certified sections** this run; current inventory **25 chapters, 747 unique numbered sections**. All other matrix cells unchanged. General earlier unresolved/external findings retained. Excluded approximation/regularization with Bergman/L²/Ohsawa–Takegoshi/multiscale/positivity-loss stays `deferred-by-user`. No tests/builds/CI/site changes.
