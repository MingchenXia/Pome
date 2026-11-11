# Classified mathematical audit finding — 2026-11-12

| Field | Value |
| --- | --- |
| Stable ID | POME-GEOD-CP1-NONFLOW-TORIC-SPEED-001 |
| Status | **verified conditional deduction** |
| Severity | **low** |
| Main SHA | b6933b772f41b45918f7e25ed1afbbb1fd892272 |
| Report | [Proof and anchors](../reports/2026-11-12-cp1-nonflow-toric-geodesic-energy-speed.md) |
| Printed theorem | **Theorem 17.8.3 remains correct** in the tested setting; no original error confirmed |
| Primary integrated file | docs/sections/relative-energy-and-perron-segments--energy-along-weak-geodesics/index.html |
| Primary blob / anchor | 8d9b7af925289346c96df751c67049e90c9dfe1d; physical lines 58–113 |
| Primary provenance | foundations-of-pluripotential-theory:907171A2; permanent tag 678A18D6D406 |
| Dependents | Exact toric subcase of affine-energy Theorem 17.8.3; all finite p-velocity norms |
| Proposed correction | None to printed statements, proof registry, source, tags, or canonicalization |
| Scope | Selected integrated §§17.3, 17.7, 17.8; +0 first visits; +0 complete certifications |

**New result.** The smooth toric weak geodesic on \(\mathbb P^1\) defined by Legendre conjugation of \(g_t(y)=y\log y+(1-y)\log(1-y)+t\varepsilon y(1-y)\), \(0<\varepsilon<2\), has \(E_\omega^0(u_t)=-\varepsilon t/6\), \(\int|\dot u_t|^p\omega_{u_t}=\varepsilon^p B(p+1,p+1)\) for all real \(p\ge1\), \(L^2\) speed \(\varepsilon/\sqrt{30}\), and joint smooth homogeneous Monge–Ampère zero. Full Perron identification uses the existing Theorem 17.7.8 as an explicitly **unverified upstream premise**; its toric convex-order calculation is direct.

**Nonduplication.** Unlike POME-GEO-PROJECTIVE-DIAGONAL-EXACT-001 (2026-11-06), the moment-velocity function is quadratic, not affine; this family is not a diagonal holomorphic projective flow. Neither earlier logistic-ray nor other geodesic findings are counted again.

**Outstanding/deferred.** General Perron existence (§17.7.8), weighted Bedford–Taylor/local maximality (§17.8.1–2), non-pluripolar product integration (§§13.6, 17.2), and finite-energy limits (§17.8.3 Step 5) are not certified. The owner's excluded Demailly regularization, dedicated Bergman/L²/Ohsawa–Takegoshi/multiscale/positivity-loss programme remains **deferred-by-user**, not resolved. No complete section or chapter was certified.
