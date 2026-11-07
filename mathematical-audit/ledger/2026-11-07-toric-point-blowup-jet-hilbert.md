# Classified finding: POME-TORIC-BLOWUP-STAR-SUBDIVISION-JETS-001

- **Date:** 2026-11-07; **main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.
- **Status:** **verified conditional deduction**; **severity:** low. This is an explicit smooth toric blowup model; printed Lemma 21.8.2(4), Theorem 21.8.3, Propositions 21.9.1–3 and Theorem 21.9.5 remain correct on tested hypotheses. It is **not** a full certification.
- **Stable labels:** `foundations-of-pluripotential-theory:86BADE82` / `41C54729DBFD` (§21.8.2); `:0F7315B0` / `E49F0370E203` (§21.8.3); `:4C5E5EB3` / `9FD0EEED0DBF` (§21.9.1); `:86CCC496` / `7B4A7CC50CDC` (§21.9.2); `:43543C56` / `C62B8871AA1C` (§21.9.3); `:BD98CC5B` / `69D3D97E7701` (§21.9.5).
- **Exact integrated anchors:** `docs/sections/convex-analysis-and-toric-potentials--smooth-lattice-polytopes-and-projective-charts/index.html` blob `f442a7b663689b97a9b89689b8b7ae8b366a53fe`, lines 24–61, 87–142; `docs/sections/convex-analysis-and-toric-potentials--fans-divisors-and-character-sections/index.html` blob `7ad2e6dbdd0ce59e1bf08cd9cb3c046e8c87ff6c`, lines 10–32, 34–67, 69–106, 138–166.
- **Hypotheses:** `d,ell` integers `0<ell<d`, full-dimensional Delzant polygon with four primitive normals. The boundary `ell=d` **does not satisfy** the full-dimensionality hypothesis.
- **Proved:** `X_P=Bl_p P^2`, `L=dH-ell E`, explicit standard blowup charts and `E^2=-1`, all-degree jet-ideal character basis, `h^0(kL)=((d²-ell²)k²+(3d-ell)k)/2+1`, and `-K=3H-E`. At the wall `ell=d`, the projective character variety is the rational normal curve instead.
- **Justification:** See [full chart and monomial proof](../reports/2026-11-07-toric-point-blowup-star-subdivision-and-jet-hilbert.md). No numerical-only inference.
- **External/general dependencies outstanding:** entire higher-dimensional vertex-chart/character-section formalism and lattice asymptotic chain are not certified. Earlier toric Laurent inverse-character exposition finding stays untouched.
- **Correction proposed:** no mathematical correction to printed theorem; preserve nonempty-interior/smoothness qualifications and do not extrapolate surface conclusions to the `ell=d` degeneration.
- **Affected dependents:** §21.8.3, §21.9.2, §21.9.5, toric volume/character identification.
- **Prior statuses/exclusions:** unchanged; Demailly approximation/regularization and dedicated Bergman, L², OT, multiscale and positivity-loss programme remain **deferred-by-user**, not resolved.
