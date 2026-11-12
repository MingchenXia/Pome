# Classified finding: higher-dimensional circular-tube distance

**Date:** 2026-11-13  
**Stable ID:** POME-DIST-HIGHERDIM-CIRCLE-TUBE-SUBHARMONIC-001  
**Severity:** low  
**Status:** verified conditional deduction  
**Object:** Proposition 3.9.2 (printed planar theorem **correct**); companion Proposition 3.9.3 context only.

- Main: b6933b772f41b45918f7e25ed1afbbb1fd892272; integrated docs/sections/planar-boundary-distance-and-convexity/index.html; blob 25fd0fd57d3e51f9224a25341ace77584b2a1a2a.
- Source: klimek-pluripotential-theory:219D9DEC; permanent tag 59D258340230; HTML lines 37–87, dimension-specific passage 60–70.
- Hypotheses tested: replacement \(\mathbb R^2\rightsquigarrow\mathbb R^m\), \(m\ge3\), while retaining proper closed nonconvex \(F\), connected open \(G\supset F\), and subharmonicity of \(d_F\) on \(G\).
- Result: the circle \(F_R=S^1_R\times\{0\}^{m-2}\) and connected \(\varepsilon\)-tube \(G_\varepsilon\), \(0<\varepsilon<R/2\), satisfy \(\Delta d_F=[m-2+(r-R)/r]/d_F>0\) in distributions, yet \(F_R\) is not convex. The shrinking-tube flux tends to zero, so there is no hidden singular negative measure at \(F_R\).
- **Distinction:** counterexample only to **unprinted dimension extension**; not a source error and not a proof gap in the actual \(\mathbb R^2\) theorem. Earlier planar slab-rigidity finding remains separate.
- Proposed correction: optional warning that the theorem relies on real dimension two, preserving source/section tags; do not alter proof or main from this audit branch.
- Dependents: only hypothetical use of Proposition 3.9.2/3 in real dimension \(m\ge3\); none of the current printed dependent results shown false.
- Full derivation: [dated report](../reports/2026-11-13-higher-dimensional-circular-tube-distance-subharmonic.md). Exact scope: [coverage record](../coverage/2026-11-13-ch3-circular-tube-distance-subharmonic.md).
- Resolved/unresolved/deferred ledger: self-contained countermodel **verified**; original planar theorem unchanged; full section and transitive inputs unverified; user-excluded Demailly regularization/Bergman/\(L^2\)/Ohsawa–Takegoshi/multiscale/positivity-loss programme **deferred-by-user**.
