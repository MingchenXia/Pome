# Classified finding — 2026-11-07

**ID:** `POME-NA-CHOQUET-FINITE-JOIN-EXHAUSTION-001`  
**Severity / status:** **low / verified conditional deduction**; no false published theorem.  
**Reviewed main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.

**Target.** Integrated Proposition 22.1.37, `docs/sections/non-archimedean-pluripotential-theory/index.html`, blob `8448d710690ebe1cc28040f9611d05c9d008a961`, physical lines 566–591; source **`sgpt:284D07DA`**, permanent **`21737B0303A5`**. Supporting Definition 22.1.34 and Propositions 22.1.32, 22.1.36 (physical 504–561). Integrated Proposition 17.15.31, `docs/sections/test-curves--operations-on-test-curves/index.html`, blob `3da617be8f58713f764d49ba22f49b803149a5e8`, physical 662–719; source **`sgpt:6B576942`**, permanent **`4B67ABC0083D`**. Endpoint convention Remark 17.12.3, `docs/sections/test-curves--the-notion-of-test-curves/index.html`, blob `6dfdfc2b5e599eb3a19a9558a9c963e79df71dc7`, physical 43–47; source **`sgpt:FCDC9660`**, permanent **`3D73AB2E32CB`**.

**New check.** A uniformly maximal-parameter-bounded family of NA metrics admits an increasing *sequence of finite joins* realizing its full `sup^*`, by countable Choquet extraction at the cofinal Kähler forms \(\omega_0/m\). For the countable pairs \((m,q)\) with rational \(q<M\), an exceptional **locally pluripolar** set suffices to recover each regularized projected \(q\)-level from pointwise increasing limits. On \(\mathbb P^1\), constant model test curves with maxima \(a_j=1-1/j\) show that **no finite join** need attain the supremum. More sharply, the endpoint extension of the supremum at its new maximum \(1\) is \(0\), whereas \(\sup_j \Gamma^{(j)}_1=-\infty\) for the individually extended curves. This explicitly distinguishes the test-curve supremum from taking the pointwise extended endpoint supremum.

**Mathematical dependencies / limitations.** The countable selection uses Proposition 17.15.31 (ultimately local Choquet, Proposition 5.14.3), projected-sup compatibility Proposition 22.1.36 and finite-join properties Propositions 22.1.32–33. The model's finite-stage nonattainment and endpoint mismatch are direct computations. This is not an independent complete proof of all those inputs, not convergence in volume/DH/trace, and not a complete-section certificate. No external theorem or excluded regularization subproject was introduced.

**Proposed optional explanation.** Adjacent to Proposition 22.1.37, explain that countable extraction can be enumerated into an *increasing sequence of finite joins*, but one cannot replace the regularized NA supremum by a single finite join or by the pointwise supremum of separately extended endpoint levels.

**Affected dependents (not individually certified):** monotone-volume Proposition 22.1.39, trace Definition 22.1.50, and DH convergence Proposition 22.1.60 must retain their independent hypotheses.

[Complete English proof](../reports/2026-11-07-nonarchimedean-choquet-finite-join-exhaustion.md) · [Exact coverage](../coverage/2026-11-07-ch22-na-choquet-finite-joins.md). Previously recorded confirmed errors, proof gaps, candidates, dependencies, duplicates and repairs stay unchanged; user-excluded Demailly regularization/Bergman/L²/OT/multiscale/positivity-loss work remains **deferred-by-user**.
