# 2026-11-17 — §14.7 fixed-data smooth exponential equation, large parameter

| ID | Severity | Classification | Exact locus | Resolution / remaining inputs |
| --- | --- | --- | --- | --- |
| \`POME-SMOOTH-EXP-LARGE-LAMBDA-RESOLVENT-001\` | low | **verified conditional deduction** | main \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`; \`docs/sections/smooth-monge-ampere-equations--the-smooth-exponential-equation/index.html\` blob \`1de4acc3150f79f4275f8aa507d2c044edb32d8f\`; Prop 14.7.1 \`non-kahler-pluripotential-theory:CF8EC5AE\` / \`C52E44D9C563\` physical lines 10–22; Thm 14.7.2 \`non-kahler-pluripotential-theory:793E5FA5\` / \`97F5C96646CC\`, lines 26–51 | Exact order-reversing \(C^0\) Lipschitz comparison, sharp constant shifts, all-orders **fixed-\(F\)** \(C^0\) large-\(\lambda\) expansion with coefficients \(-F,-L_\omega F,-L_\omega^2F-\tfrac12\mathrm{tr}(\omega^{-1}dd^cF)^2\) and explicit scalar sub/supersolutions. No original theorem false. Theorem 14.7.2 smooth existence (elliptic §14.5.5/.8) is **conditional**; no proof of it supplied. |

**Full proof:** [report](../reports/2026-11-17-smooth-exponential-large-lambda-asymptotic.md). **Coverage delta:** [coverage](../coverage/2026-11-17-ch14-smooth-exponential-large-lambda.md).

**Proposed correction/addition:** optional non-production corollary to Theorem 14.7.2, after independent review. No actual source/body/registry change. The fixed-\(F\) expansion is *not* valid as stated for \(F=-\lambda f\); §16.28.2 remains unaffected. All user-excluded Demailly regularization/Bergman/\(L^2\)/OT/multiscale/positivity-loss proof programmes remain **deferred-by-user** (neither resolved nor certified).

**Coverage:** existing selected §14.7 review augmented; **+0 first visits / +0 full-section certifications**; main ToC independently counted **25/747**. No build, project tests, Actions CI or publication was run.
