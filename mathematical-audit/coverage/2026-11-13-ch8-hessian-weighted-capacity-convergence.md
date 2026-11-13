# Exact selected coverage: Chapter 8, §8.11, 2026-11-13

- Reviewed production main: b6933b772f41b45918f7e25ed1afbbb1fd892272.
- Chapter/section reading source: docs/sections/complex-hessian-equations--local-capacities-and-decreasing-products/index.html (blob 115d285f6b1f76d284463c396e7e87db2b9dbdc3).
- Supporting source: docs/sections/complex-hessian-equations--bounded-potentials-and-recursive-hessian-currents/index.html (blob 117b866408974cdf706bf305df75e35e1b8affde).
- Finding: POME-HESS-WEIGHT-CAPACITY-VAGUE-STABILITY-001, **low / verified conditional deduction**, [full proof](../reports/2026-11-13-hessian-weighted-capacity-convergence.md), [ledger](../ledger/2026-11-13-hessian-weighted-capacity-convergence.md).

| Exact entry | Stable source / permanent label | Integrated physical lines | Actual depth |
| --- | --- | --- | --- |
| Lemma 8.11.1 | non-kahler-pluripotential-theory:7121E570 / 370C4F1C4AF0 | 19–46 | Uniform compact local mass, used to show finite \(c_s(V)\); earlier proof not transitively certified |
| Definition 8.11.2, capacity remarks, (8.11.3) | :016F1DC8 / FA49D2074193; equation :32422401 / A08EAEC63C44 | 48–71 | Direct capacity / outer-open / subadditivity / finite-mass definitions |
| Proposition 8.11.6 | :22C64532 / 390B1CE08171 | 146–237 | Selected capacity convergence and quasicontinuity proof context; not all torsion integrations independently proved |
| Lemma 8.11.11 | :59C81738 / 978D54F1054C | 259–279 | Complete hypothesis/proof inspection; proved strict nonmonotone net generalization with automatic limit domination |
| Theorem 8.11.12 | :B227378C / C044CD1C65C4 | 281–295 | Selected uses of 8.11.11, not full recursive-current certificate |
| Lemma 8.11.13 | :915C1E41 / E64937A67BD2 | 300–318 | Selected capacity domination on positive shifted products; not independently re-proved |
| Theorem 8.11.14 | :C3C23711 / 945FEE7DBDC5 | 320–334 | Selected application of 8.11.11; no claimed full theorem-chain certificate |
| §8.9.3 and §8.9.8 | :354EA0C7 / EB2FA13CDDE0; :B3E694DA / A1E60FC7AA88 | 46–95, 156–176 of §8.9 | Context only; no excluded Demailly regularization reopened |

**Coverage accounting:** Current main still has 25 chapters / 747 numbered sections as recorded by the actual ToC matrix; §8.11 previously partly inspected; **+0 newly first-visited numbered sections / +0 complete section certifications** this run. Analytic Hessian-capacity estimates, smooth admissible approximation and arbitrary \(D_p,Q_p\) constructions not certified transitively. Existing deferred-by-user Demailly programme stays deferred; no production/CI/site edits or build/test claims.