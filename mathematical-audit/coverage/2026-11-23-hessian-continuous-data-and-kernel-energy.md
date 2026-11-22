# 2026-11-23 — direct Hessian and selected Gaussian energy review

Current production main b6933b772f41b45918f7e25ed1afbbb1fd892272; audit branch before work 5636f3929942f6837f4c2af5e53cb9085f81d9e6.

| ToC section | Blob / source scope | Actually performed | Limit |
| --- | --- | --- | --- |
| §8.6 | docs/sections/complex-hessian-equations--proper-equations-and-admissible-approximation/index.html; 841dd207876499be9d83045facf862a323e60994 | Entire current math lines 7–205; penalty upper tests, Gårding sign, decreasing obstacles and upstream references | Whole direct review, not complete transitive certification; prior penalty stability not counted again |
| §8.8 | docs/sections/complex-hessian-equations--continuous-equations-and-regularity/index.html; 62cace2a2bdec93860bf4b5ba9cb4653b4ed2b50 | Entire current math lines 5–94; proper solver, regularity bridge, Banach fixed point; new continuous-data deduction | Whole direct review, not complete transitive certification; prior smooth linear response retained |
| §4.1 | docs/sections/potentials-energy-and-capacity/index.html; 4962a7cd576a64cb47fa0955dcc80cf87c3da9d1 | Only lines 21–241, Gaussian factorization, planar signed energy, equilibrium minimization | Selected **not whole**; lines 242–876 not reviewed here |
| §8.4/§8.5/§8.7 | source blobs and paths in the report | Only §8.4.6 lines 188–197, §8.5.3 lines 63–116, §8.7.9 lines 204–222 | Targeted dependencies, no new full review |

**Delta:** 2 entire current direct sections, 1 partial, 3 dependency checks; one verified conditional deduction; 0 confirmed original errors; 0 complete transitive proof chains; historic first visits unreconciled. The original ToC retains **747 rows**.

Uncertified: §8.6.1 global PDE solver and §8.5 Evans–Krylov–Caffarelli input, §8.7 product convergence, §4.1 beyond selected lines. User-excluded Demailly regularization and dedicated Bergman/L²/OT/multiscale/positivity-loss programmes remain deferred-by-user. No production changes, CI, build or tests.
