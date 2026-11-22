# Coverage checkpoint — 2026-11-23: contact trace bound and Gauduchon matrix

Reviewed main commit: b6933b772f41b45918f7e25ed1afbbb1fd892272. Existing audit branch review/mathematical-audit was preserved. The chapter/section mapping is from the current main table of contents, not inferred from source book numbers.

| Current section | Physical reading edition / blob | Exact scope | Certification |
| --- | --- | --- | --- |
| §14.12 | docs/sections/smooth-monge-ampere-equations--the-adjoint-equation-for-gauduchon-volume/index.html; de0b040ee22f128bf16c89048267075a01f15e66 | All mathematical lines 5–110; variation 14.12.1, formal adjoint 14.12.3, positivity/Fredholm hypothesis, n=2 and eta=gamma consistency | Entire current section directly checked; no complete upstream proof-chain certification |
| §14.13 | docs/sections/smooth-monge-ampere-equations--the-matrix-structure-of-the-gauduchon-equation/index.html; 6e1faedde219b856c0bf5ecaf566403ae999772e | All mathematical lines 7–180; Hodge-star normalization, torsion-index formula 14.13.3, sorted inverse weights, coercivity 14.13.7 and matrix concavity 14.13.8 | Entire current section checked; previously reported split tag A6EC7DDEACFB NOT a new finding |
| §16.14 | docs/sections/envelopes-and-model-potentials--measures-on-contact-sets--obstacles-with-bounded-metric-laplacian/index.html; e9ce0caf7bd8b123062d9cb6fffd49fdfd0d5ffb | All mathematical lines 5–281: nonbounded Hessian example, W^(2,2) localization, contact density Prop. 16.14.6, W^(2,p), signed weak products | Entire current section directly checked; one NEW sharp conditional trace-product deduction, no transitive certificate |
| §§3.9, 17.2, 20.7 and comparison §20.6 | Existing previously audited current blobs, retained in matrix | Revisited selected ambient hypotheses and proof mechanisms during source/dependency checks | REPEAT only; no added whole count |

Full proof: ../reports/2026-11-23-contact-trace-bound-gauduchon-matrix.md; finding: ../ledger/2026-11-23-contact-trace-bound.md.

Delta: +3 complete CURRENT direct section checks, not asserted historically first; +1 verified conditional deduction; +0 newly confirmed false theorems; +0 new presentation findings (historic issue checked but not repeated); +0 completed transitive dependency chains. No data were inferred from the presence of 747 section records.

Open/deferred: §7.13.4 contact-density foundations, §10.2 elliptic inverse, portions of §14.12 Fredholm, §16.14 Sobolev inversion remain uncertified. All user-excluded Demailly approximation/regularization and dedicated Bergman/L2/OT/multiscale/positivity-loss proof programmes are **deferred-by-user**. No build, tests, CI, main/source/registry/tag, or website changes.
