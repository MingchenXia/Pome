# 2026-11-14 — Chapter 21 toric softmax logarithmic-ratio transport

| Finding ID | Location and fixed main | Classification | Severity | Disposition and dependents |
| --- | --- | --- | --- | --- |
| POME-TORIC-SOFTMAX-LOGRATIO-W1-001 | §21.5.1/.2/.4, docs/sections/convex-analysis-and-toric-potentials--the-real-monge-ampere-measure/index.html, blob 7089aa41ae2422b1bd6b5094e46668cbc8ed37be, lines 10–39, 43–85, 98–157; sources foundations-of-pluripotential-theory-4A0FAEB3/6403CF44/EAD83A50, permanent tags 409656CC47D4/F4072D9ED060/5D8A7A7D734E | verified conditional deduction (no false theorem) | low | Exact marginal logistic law, \(P(|X_i|>s)=2/(1+e^{s/\varepsilon})\), and \(W_{1,\ell^1}=2n\varepsilon\log2\). Optional quantitative addendum, no modification to printed theorem. Relevant to §21.5.2, §21.6.2 and toric transport estimates. Existing TV sharpness POME-TORIC-SOFTMAX-TV-001 is **not** counted again. |

**Reviewed production main:** b6933b772f41b45918f7e25ed1afbbb1fd892272. **Proof:** [full dated report](../reports/2026-11-14-softmax-logratio-sharp-l1-wasserstein.md). **Coverage:** [precise delta](../coverage/2026-11-14-ch21-softmax-logratio-w1.md).

**Remaining limitations:** no general transport-continuity theorem, no full §21.5 or upstream convex-duality certification; excluded Demailly regularization/Bergman/L2/OT/multiscale/positivity-loss work remains **deferred-by-user**. No CI, build, publication, or source edits.
