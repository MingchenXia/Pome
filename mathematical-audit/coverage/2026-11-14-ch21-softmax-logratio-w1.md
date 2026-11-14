# 2026-11-14 — Chapter 21 precise selected-proof coverage delta

**Pinned main:** b6933b772f41b45918f7e25ed1afbbb1fd892272. **Actual table of contents:** 25 chapters / 747 numbered sections. The preexisting matrix remains the baseline; no section is newly declared completely certified.

| Section | Actual inspected current main source | This session's new check | Scope and status |
| --- | --- | --- | --- |
| §21.1 | docs/sections/convex-analysis-and-toric-potentials/index.html, blob e875ab348461c739ae3799c6906f8f13b9050ba7, physical lines 7–18 | Re-read lattice and n! volume conventions | Contextual only; previously visited |
| §21.5 | docs/sections/convex-analysis-and-toric-potentials--the-real-monge-ampere-measure/index.html, blob 7089aa41ae2422b1bd6b5094e46668cbc8ed37be, Theorem 21.5.1 lines 10–39 (source foundations-of-pluripotential-theory-4A0FAEB3, tag 409656CC47D4), Theorem 21.5.2 lines 43–85 (source -6403CF44, tag F4072D9ED060), Proposition 21.5.4 lines 98–157 (source -EAD83A50, tag 5D8A7A7D734E) | Exact normalized-simplex-to-independent-exponentials Jacobian, logistic coordinate laws, all tails, and exact \(\ell^1\)-Wasserstein coefficient \(2n\varepsilon\log2\). Rechecked integrated theorem hypotheses and normalization | Previously partly proof-reviewed, **not** a first visit; verified conditional deduction POME-TORIC-SOFTMAX-LOGRATIO-W1-001, low; no printed error; [full report](../reports/2026-11-14-softmax-logratio-sharp-l1-wasserstein.md) |

**Accounting:** +0 newly first-visited numbered sections, +0 entire-section mathematical certifications. The October 25 narrow-vs-TV simplex finding and its proof remain unchanged; this is a new *quantitative first-Wasserstein* check, not a duplicate claim. User-excluded approximation/regularization and dedicated Bergman/L2/OT/multiscale/positivity-loss proofs stay **deferred-by-user**. No tests/builds/CI, site publication, source-body or permanent-tag changes.
