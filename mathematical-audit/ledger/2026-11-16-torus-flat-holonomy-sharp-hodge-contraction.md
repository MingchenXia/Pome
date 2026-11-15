# 2026-11-16 — flat torus holonomy and sharp Hodge homotopy

**Stable finding ID:** POME-HODGE-TORUS-SHARP-HOLONOMY-HOMOTOPY-001  
**Severity/status:** low / **verified conditional deduction**; explicit torus theorem self-contained, general Pome elliptic/Hodge claims remain unverified globally. **Not** a confirmed error, proof gap, or source repair.

Main SHA: b6933b772f41b45918f7e25ed1afbbb1fd892272.
Current integrated files:
- docs/sections/complete-metric-laplacians-and-reduced-cohomology/index.html (blob 93b74f8a110bb6c45a7e53cdaed0910af7eb5118), Prop 2.21.2 source demailly-complex-geometry:CF433F03 / tag E40060D5FC24 at lines 10–38; Thm 2.21.3 source :CDC5D23B / tag CE09CDC33E77 at 40–83; Cor 2.21.5 source :63A1AB33 / tag A76DD53006C1 at 85–104.
- docs/sections/differential-operators-and-elliptic-regularity--maximal-domains-and-formal-adjoints/index.html (blob 63b73681ef8b511fff1308685388f027ead75a77): Prop 2.17.2, formal adjoints.
- docs/sections/hodge-theory-curvature-and-compact-vanishing--compact-hodge-theory-and-analytic-duality/index.html (blob b7001303a35ddd5c91f40e81cfc93523e8d6b8ab): Thm 10.46.4 source demailly-complex-geometry:7CE52240 / tag BD1EEDFB2146, lines 108–140.

**Exact statement/model:** on T^m, m >= 2, for flat unitary connection d+i alpha·dx, the q-form Laplacian has eigenvalues |k+alpha|² each with multiplicity binomial(m,q); harmonic dimensions are binomial(m,q) precisely at alpha in Z^m and zero elsewhere. The Green norm is gamma(alpha)^(-2), and the degree-lowering canonical homotopy has optimal norm gamma(alpha)^(-1), where gamma is dist(alpha,Z^m) off the lattice and 1 on it. The heat trace is a smooth Gaussian lattice sum; no continuous choice of bounded homotopies can keep norms bounded near a lattice point, by a degree-zero test vector.

**Proof/correction/dependents:** full Fourier proof, signs, domain closure, exact constants and optimality in [report](../reports/2026-11-16-torus-flat-holonomy-sharp-hodge-contraction.md). No correction required; optionally add this higher-dimensional example via separately reviewed future patch. Cor 2.21.5 and Thm 10.46.4 remain consistent. Previous 2026-10-28 S¹ dimension-jump finding is retained, not counted as new.

**Limits:** selected model/theorem checks only; all general upstream elliptic assertions remain conditional. No full section certification. All excluded Demailly regularization and dedicated Bergman/L2/OT/multiscale/positivity-loss proofs remain **deferred-by-user**, neither resolved nor certified.
