# 2026-11-16 — additive §12.2 Gauduchon quotient audit

**Main:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`. **Reading-edition HTML:** \`docs/sections/a-gauduchon-variational-volume--the-quotient-and-the-smooth-equation/index.html\`, Git blob \`9ec67161d46b3ba20afa1b1c9a0c84f29322763e\`. **Source variant:** \`non-kahler-pluripotential-theory\`. **Section permanent tag:** \`43BF29E33E59\`.

| Integrated locator | Source / permanent tags; physical lines | Actual new inspection | Boundary |
| --- | --- | --- | --- |
| Definition 12.2.1 | source \`6E1DBC11\`, permanent \`0C4AF7E2CEBB\`, lines 16–21 | exact quotient and denominator normalization; Gauduchon ray invariance | existing definitions, not new proof certification |
| Proposition 12.2.2 | source \`CEFAD6D9\`, permanent \`4AF37F3C8091\`, lines 25–45 | numerator current-Stokes and background invariance consulted | no new global cone conclusion certified |
| Theorem 12.2.3 | source \`876DF057\`, permanent \`2DB664A6EFDF\`, lines 58–80, AM–GM lines 69–75, Gauduchon uniqueness line 77 | independently proved **sharp** weighted pairwise determinant-normalized anisotropy deficit, exact in dimension two, and sharp n-dimensional torus counterexample to any larger constant | smooth Monge–Ampère existence Thm. 14.2.1 and Gauduchon representative Thm. 11.4.2 conditional |
| Theorem 12.3.1 | source \`6B1A74F2\`, permanent \`2220E0C47510\`, neighboring §12.3 lines 10–33 | downstream statement and concavity context only | no first-variation/second-variation proof recertification |

**Finding:** [POME-GAUD-QUOTIENT-SHARP-PAIRWISE-ANISOTROPY-001](../reports/2026-11-16-gauduchon-sharp-pairwise-quotient-deficit.md), **low / verified conditional deduction**; printed Theorem 12.2.3 correct. [Separate ledger](../ledger/2026-11-16-gauduchon-sharp-pairwise-quotient-deficit.md). Small exact rational arithmetic check is reproducible at [checks/check_gauduchon_pairwise_deficit.py](../checks/check_gauduchon_pairwise_deficit.py); it samples sharpness models but is **not a proof**, project test suite or build.

**Coverage accounting:** §12.2 was already partially inspected. This increment gives **0 newly first-visited numbered sections; 0 completed whole-section certifications**. Main ToC currently 25 chapters / 747 numbered sections. The excluded regularization/Bergman/L2/Ohsawa–Takegoshi/multiscale/positivity-loss programme remains **deferred-by-user**; no main/body/registry/tag/CI/site changes.
