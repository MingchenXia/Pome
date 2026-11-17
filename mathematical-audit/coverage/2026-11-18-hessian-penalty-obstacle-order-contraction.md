# 2026-11-18 — incremental coverage of §8.6 Hermitian Hessian penalties

**ID:** POME-HESS-PENALTY-OBSTACLE-CONTRACTION-001. Main SHA \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`. Directly reviewed reading-edition HTML \`docs/sections/complex-hessian-equations--proper-equations-and-admissible-approximation/index.html\` blob \`841dd207876499be9d83045facf862a323e60994\`.

| Number / anchor | Coverage actually checked | Status |
| --- | --- | --- |
| §8.1 opening, section \`CFD38285654D\` | \(X\) compact connected, Hermitian \(\omega\), \(2\le m<n\) | Standing hypothesis only |
| §8.2 opening, tag \`F677D35E0BD7\` | Gårding cone upward monotonicity and \(H_m\) normalization | Conditional algebraic input |
| §8.6.1 source \`non-kahler-pluripotential-theory:91CAEA62\`, permanent \`8B310CC2C1A1\`, lines 11–36 | Smooth existence/uniqueness statement, comparison at extrema, linearization; new exact *two-penalty-input* maximum-principle result | Verified conditional deduction; elliptic PDE a priori estimates not certified |
| §8.6.2 source \`761F7FD5\`, tag \`B8367971A40D\`, lines 45–94 | Smooth arbitrary obstacles and bounds; consistency of new 1-Lipschitz comparison | Existing proof sampled; not fully certified |
| §8.6.5 source \`32B364F9\`, tag \`DFE78235C5E9\`, lines 129–169 | Approximation rate and sharp extra \(O(1/N)\) only under strict admissibility of the smooth obstacle | Additional selected proof, no error |
| §8.6.6 tag \`68BE4F589DCE\`, lines 174–201 | Decreasing approximation statement and affected-dependency scan | Context only |
| §8.7.1 tag \`D2A0F255F625\` | Continuous-product use of smooth approximants | Context only |

Current generated ToC: **25 chapters / 747 numbered sections**. §8.6 was already partially visited; this run adds **0 newly first-visited numbered sections** and **0 complete section certifications**. No tests/build/CI/publication, no source/body/registry/tag edits. Excluded Demailly approximation and all dedicated Bergman/L²/OT/multiscale/positivity-loss programmes remain **deferred-by-user**.

See [proof report](../reports/2026-11-18-hessian-penalty-obstacle-order-contraction.md) and [classification](../ledger/2026-11-18-hessian-penalty-obstacle-order-contraction.md).
