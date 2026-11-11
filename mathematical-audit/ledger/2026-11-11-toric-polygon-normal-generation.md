# POME-TORIC-POLYGON-NORMALGEN-PICK-REEVE-001

- Date: 2026-11-11
- Severity: **low**
- Status: **verified conditional deduction**
- Main reviewed: `b6933b772f41b45918f7e25ed1afbbb1fd892272`
- Chapters/sections: §§21.7, 21.8, 21.9 (already partly reviewed); **0 new first visits, 0 entire sections certified**
- Finding: Every full-dimensional lattice polygon admits a unimodular triangulation and `(kP∩M)+(lP∩M)=((k+l)P∩M)` for all `k,l≥0`. The exact count is `Area(P)k²+B(P)k/2+1`; its Ehrhart/section-ring series is `[1+(I+B-3)t+It²]/(1-t)³`. For the *smooth Delzant surface* of Pome Theorems 21.8.3 and 21.9.5, all section-multiplication maps are surjective and the embedding is projectively normal. The non-Delzant Reeve tetrahedra `conv(0,e1,e2,(1,1,q))`, `q≥2`, have the lattice hole `(1,1,1)∈2P` and show the two-dimensional conclusion cannot be extended to **arbitrary** 3-polytopes.
- Why nonduplicate: Theorem 21.7.3 proves a *leading lattice asymptotic*, not this exact all-degree formula; §21.9.5 lists graded character-section bases, but does not assert surjectivity of multiplication or projective normality. Earlier audit models treated moment metrics, arbitrary invariant divisors, and non-Delzant toric singularities, not polygon normal generation or its sharp unrestricted-dimension failure.
- Precise anchors: `docs/sections/convex-analysis-and-toric-potentials--smooth-lattice-polytopes-and-projective-charts/index.html` lines 10–21, 24–85, 89–112, 107–155; main blob `f442a7b663689b97a9b89689b8b7ae8b366a53fe`, Theorem source/permanent `foundations-of-pluripotential-theory:0F7315B0/E49F0370E203`. `docs/sections/convex-analysis-and-toric-potentials--fans-divisors-and-character-sections/index.html` lines 138–166; blob `7ad2e6dbdd0ce59e1bf08cd9cb3c046e8c87ff6c`, Theorem source/permanent `foundations-of-pluripotential-theory:BD98CC5B/69D3D97E7701`. `docs/sections/convex-analysis-and-toric-potentials--lattice-points-and-volume/index.html` lines 57–89; blob `5d209b7f4d2156c19bc3fb300303405df6321230`, Theorem source/permanent `foundations-of-pluripotential-theory:364BCD30/831AEEB7084F`.
- Proposed correction: optional *surface-only* supplementary corollary after 21.9.5, preserving all theorem tags and historical references; no defect in printed theorem.
- Affected dependents: subsequent toric-surface line-bundle/section-ring and graded-series applications; no assertion of higher-dimensional smooth-polytope normality.
- Upstream status: the finite combinatorial arguments and elementary semigroup integrality are verified here; the full integrated geometry hypotheses and proofs of 21.8.3/21.9.5 remain conditional.
- Deferred-by-user: entire Demailly approximation/regularization and dedicated Bergman, weighted L², OT, multiscale and positivity-loss proof-completion programme. Not reopened or marked resolved.
- Full proof: [dated report](../reports/2026-11-11-toric-polygon-normal-generation-pick-reeve-boundary.md).
