# Exact additive coverage: 2026-11-08 — §8.10 strong H1 monotone upgrade

**Main SHA:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`  
**Branch at audit start:** \`review/mathematical-audit\` / \`93a4f15949ca63e85d3a7de31bd6905cd551e391\`.  
**Current main table of contents:** 25 chapters; 747 numbered sections; zero entire mathematical sections certified.

| Chapter/section | Directly inspected on current production main | Stable tags and precise physical lines | Result and coverage boundary |
| --- | --- | --- | --- |
| 8.10 — Sobolev capacity and two Hessian factors (previously partly visited) | \`docs/sections/complex-hessian-equations--sobolev-capacity-and-two-hessian-factors/index.html\`, blob \`25f25433cb9b17de6715a5b05f8b3c15b95a18cd\` | \`non-kahler-pluripotential-theory:1DDAECA7\` / \`FFBF9CD42640\`, lines 59–95; \`non-kahler-pluripotential-theory:8E387C3E\` / \`A82044827575\`, lines 101–125; \`non-kahler-pluripotential-theory:C0AF8E7E\` / \`B40742E0DD08\`, lines 131–149; Sobolev/Gauduchon lines 10–28 | Proved new **conditional** strong H1 monotone convergence and pairwise energy identity from weighted-product continuity: \`POME-HESS-CAP-STRONG-H1-MONOTONE-001\`. This does not reclassify any printed theorem or certify approximation prerequisites. [Proof](../reports/2026-11-08-hessian-strong-h1-monotone.md) · [ledger](../ledger/2026-11-08-hessian-strong-h1-monotone.md). |
| 8.10.5 — context only | Same file | \`non-kahler-pluripotential-theory:A19E0DE8\` / \`0241EC758621\`, lines 155–177 | Possible dependent use, not a fresh independent proof certification. |
| 8.6.6 / 11.4.2 — declared dependencies only | Earlier integrated results referenced by §8.10 | not re-audited in this run | Existing smooth admissible decreasing approximation and Gauduchon existence are used **conditionally**; excluded Demailly approximation/regularization is not investigated. |

**Count in this run:** 0 newly first-visited sections; 1 previously partly visited section with genuinely new lemma-level deduction; 0 newly fully audited sections; 0 complete-section mathematical certifications. Open/unresolved prior ledgers unchanged. Demailly regularization and dedicated Bergman/weighted-L2/OT/multiscale/positivity-loss programme remain **deferred-by-user**.

**Scope and verification:** direct main reading-edition statements/selected proofs and a new written mathematical proof. No project tests, builds, CI, formal verification, source/registry/canonicalization changes, or publication.
