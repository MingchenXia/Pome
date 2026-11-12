# 2026-11-13 — sphere-reflection classification ledger

| Stable ID | Severity | Status | Exact verified scope | Remaining dependencies and action |
| --- | --- | --- | --- | --- |
| POME-HARM-KELVIN-SPHERE-EXPLICIT-COLLAR-001 | low | **verified conditional deduction** | For every real continuous zero-Dirichlet harmonic function on $r\le|x-a|\le R$, its odd Kelvin reflection defines a harmonic function on **all** $r<|x-a|<R^2/r$. Detailed paired-interface distribution proof eliminates any unproved boundary $C^1$ assumption. §3.3.17, source classical-potential-theory:2BBE313C, permanent 14F410C2E770, main HTML blob 75e982788e627af602981823a82863cbd36ee712 lines 229–241; §3.2.2 source classical-potential-theory:B1AA5815, permanent 97BA27062B9F, blob f2615a5393af724c3996978212162f94911ff9d9 lines 16–49. | Printed theorem remains correct, not a verified repair of an error. Local internal Kelvin, maximum principle, Poisson gradient estimate, Green and Weyl inputs; transitive certification absent. Optional source revision must be separate PR, not an audit-branch edit. |

* Main SHA: b6933b772f41b45918f7e25ed1afbbb1fd892272.
* [Detailed self-contained argument](../reports/2026-11-13-spherical-kelvin-odd-reflection-collar.md) and [precise selected coverage](../coverage/2026-11-13-ch3-spherical-kelvin-reflection.md).
* The 2026-11-04 Bocher flux and 2026-11-12 Fatou cone findings in §3.3 are **prior** and are not counted as new work.
* No entries changed from confirmed error to repaired, or from external dependency to certified. All author-excluded Demailly regularization, Bergman, $L^2$, OT, multiscale-atlas and positivity-loss programmes remain **deferred-by-user**.
