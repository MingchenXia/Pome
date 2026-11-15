# Ledger — 2026-11-15 — smooth relative energy Jensen/Dirichlet gap

- **Stable finding ID:** POME-ENERGY-SMOOTH-JENSEN-DIRICHLET-001.
- **Classification:** low / **verified conditional deduction**; neither confirmed theorem error nor print-proof gap nor source repair.
- **Reviewed main:** b6933b772f41b45918f7e25ed1afbbb1fd892272.
- **Integrated file/blob:** docs/sections/relative-energy-and-perron-segments--relative-monge-ampere-energy/index.html / 16fdcc4c6a6f0cc75e69ba267bd7da2b2d7922a1.
- **Source/reader anchors:** foundations-of-pluripotential-theory:582D55DC / permanent 240EF1DE5889 / lines 32–37; foundations-of-pluripotential-theory:44639882 / 9086ABF36774 / lines 41–93; foundations-of-pluripotential-theory:A4AB3054 / 356D15D0C316 / lines 95–118; equation 17.3.5 source A392067F / permanent 46190A7C1B2F / lines 43–45.
- **Hypotheses:** connected compact Kähler \(X\), smooth admissible \(u,v\), endpoint Kähler forms bounded below/above by \(\lambda\omega,\Lambda\omega\), \(0<\lambda\le\Lambda\). No such quantitative smoothness hypothesis is attributed to the original arbitrary relative finite-energy statement.
- **Result:** exact positive Green-kernel Jensen deficit, with \(n\lambda^{n-1}/2\) lower and \(n\Lambda^{n-1}/2\) upper coefficients times \(t(1-t)D_\omega(v-u)\); strictness modulo constants. In \(n=1\) equality holds without uniform bounds. On \(\mathbf P^1\) with \(\omega=dd^c\log(1+|z|^2)\), \(f=|z|^2/(1+|z|^2)\), the exact midpoint deficit for \(0\) and \(\varepsilon f\) is \(\varepsilon^2/48\).
- **Proof:** [full direct derivation](../reports/2026-11-15-energy-uniform-jensen-dirichlet-cp1.md); [precise coverage](../coverage/2026-11-15-ch17-energy-jensen-cp1.md); [small arithmetic check](../checks/check_energy_jensen_cp1.py).
- **Correction/dependents:** no required correction, optional quantified remark after Proposition 17.3.9; does not certify singular finite-energy extension §17.3.19, relative mass/BT prerequisites or geodesic-energy descendants (§§17.7–17.9). The old degenerate-current equality examples in §17.2 are distinct and remain on record.
- **Status of unresolved/deferred material:** unchanged. Demailly approximation/regularization and dedicated Bergman, \(L^2\), Ohsawa–Takegoshi, multiscale atlas and positivity-loss work remain **deferred-by-user**, not resolved.
- **Coverage count:** +0 first-visited numbered sections; +0 fully certified numbered sections; 25 chapters / 747 numbered sections.
