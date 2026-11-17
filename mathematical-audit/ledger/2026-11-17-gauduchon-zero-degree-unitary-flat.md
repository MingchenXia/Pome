# Classified finding: zero-degree Gauduchon rigidity

- **ID:** `POME-GAUD-ZERO-DEGREE-UNITARY-FLAT-001`
- **Date:** 2026-11-17
- **Severity:** low
- **Status:** **verified conditional deduction** (original printed theorem correct; not a verified repair).
- **Main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`
- **Anchor:** `docs/sections/holomorphic-sections-and-hermitian-mass/index.html`, blob `5f00431e7986d899dc833c89175686b75f09371d`; Theorem 19.8.5, source `non-kahler-pluripotential-theory:6E03C7D3`, permanent `1DFDCCEF325D`, lines 118–148, especially 142–148.
- **Hypotheses:** connected compact complex manifold, Gauduchon Hermitian metric, holomorphic line bundle whose Bott–Chern first Chern class has a positive closed representative, and zero Gauduchon degree.
- **Conclusion / proof:** positivity and vanishing trace mass imply the current is zero; the resulting distributional \(dd^c\) equation is locally harmonic, hence its potential is smooth; modifying the metric produces a zero-curvature Chern connection. Conversely curvature zero implies all Gauduchon degrees vanish. Flat metric unique up to positive scale.
- **Not implied:** existence of nonzero holomorphic sections, torsion, holomorphic triviality, or validity without pseudoeffectivity.
- **Proposed correction:** optional explicit corollary after §19.8.5; preserve the existing result and historical attribution.
- **Upstream:** printed §11.5.1/§19.8.5 trace identity and ordinary Weyl's lemma; general foundational proof chain not recertified.
- **Affected dependents:** possible strengthening for §§10.40 and 19.8.7; no downstream error established.
- **Scope:** [full report](../reports/2026-11-17-gauduchon-zero-degree-unitary-flat.md); [precise coverage](../coverage/2026-11-17-ch19-gauduchon-flat-rigidity.md). The dedicated regularization/Bergman/L²/OT/multiscale/positivity-loss programme remains **deferred-by-user**, not certified.
