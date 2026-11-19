# 2026-11-19 exact coverage: §2.21

**Baseline:** \`main\` \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`; existing 25-chapter, 747-section table-of-contents inventory retained. **Integrated source**: \`docs/sections/complete-metric-laplacians-and-reduced-cohomology/index.html\`, blob \`93b74f8a110bb6c45a7e53cdaed0910af7eb5118\`.

| Reader section/entry | Direct inspection | Result |
| --- | --- | --- |
| §2.21 introduction, lines 7–8 | completeness, bundle, domain and scalar-product conventions | checked |
| Proposition 2.21.2, lines 10–36, permanent \`E40060D5FC24\` | maximal adjoints, cutoffs, joint graph cores | directly checked; upstream input not fully certified |
| Theorem 2.21.3, lines 40–81, permanent \`CE09CDC33E77\` | elliptic regularity, energy estimate, adjoint-domain self-adjointness, smooth kernel, zero-dimensional case | directly checked; upstream input not fully certified |
| Corollary 2.21.5, lines 85–103, permanent \`A76DD53006C1\` | closed kernel/range orthogonals, flatness, reduced cohomology | directly checked; precise sharpness proved |

**New:** \`POME-CONN-CURVATURE-ORTHOGONALITY-IFF-FLAT-001\`, [full proof](../reports/2026-11-19-metric-connection-curvature-orthogonality.md), **low / verified conditional deduction**, without changing the original theorem or its hypotheses.

**Actual change:** +1 entire section directly read, +0 certified upstream chains. Prior first-visit status is *unreconciled*; no new first-visit count. The 25/747 matrix remains a coverage inventory, not a certification. User-excluded approximation/regularization and dedicated Bergman/\(L^2\)/Ohsawa–Takegoshi/multiscale/positivity-loss programmes are **deferred-by-user**. No CI, build, site or source changes.
