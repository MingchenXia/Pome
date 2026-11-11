# POME-PARTIAL-Fock-GAMMA-GLOBAL-TV-SHARP-001

- **Date:** 2026-11-11.
- **Severity/status:** **low / verified conditional deduction**; original printed theorem is **not refuted**.
- **Main reviewed:** b6933b772f41b45918f7e25ed1afbbb1fd892272.
- **Actual new coverage:** §18.41 first selected proof-level mathematical visit (**+1 first visited**); no section or chapter fully certified.
- **Precise source:** docs/sections/partial-kernels-and-quotient-equilibrium--degenerate-curvature-and-growing-vanishing-orders/index.html; blob dae61db0ce6641977b7cc33469d95e9c820a7bff; Proposition 18.41.1 source **non-kahler-pluripotential-theory:0D642FCA**, permanent **85EDCA2D872C**, lines 26–50; equation 18.41.2 source **:CEEB555A**, permanent **33E9A1B502F8**, line 28; Theorem 18.41.9 source **:4EBD44F4**, permanent **313505FAE88E**, lines 145–216; equation 18.41.10 source **:9BF776B4**, permanent **F26D2556A21E**, line 151. Section tag **99460DD0DBB7**.
- **Finding:** for Gaussian selected entire-function spaces (r=1, m>0, integer q≥1), the **global finite total variation of the difference of two infinite measures** is exactly (1/m)E|Gamma(q,1)−a| for the radial threshold m|z|²>a. At a=q this equals 2q^qe^{-q}/(mΓ(q)). At a=mλ with q=floor(mλ), sqrt(m) times the variation tends to sqrt(2λ/π); the signed defect equals λ−q/m. This is stronger than the original local-TV convergence, not a correction.
- **Proof:** independently checked the monomial basis and the Poisson/gamma identity; layer-cake gives exact global variation and signed mass; gamma integration by parts gives the factorial constant; Stirling and |mλ−q|<1 give the sharp rate.
- **Proposed optional addition:** Gaussian-only corollary following Theorem 18.41.9; **no source/body/registry/canonicalization edits**.
- **Affected dependents:** model-level quantitative kernel comparisons in subsequent localization, no automatic compact-manifold transfer. The r>1 sharp global-TV constant and §18.42 L² correction are **not** proved.
- **No duplicate:** prior §18.41 had inventory-only coverage; the original theorem contains no global rate or gamma absolute-deviation identity.
- **Deferred-by-user:** Demailly approximation/regularization and the dedicated Bergman/L²/Ohsawa–Takegoshi/multiscale/positivity-loss proof-completion programme, **not resolved or certified**.
- **Full report:** [proof and status](../reports/2026-11-11-fock-selected-kernel-gamma-global-tv-rate.md).
