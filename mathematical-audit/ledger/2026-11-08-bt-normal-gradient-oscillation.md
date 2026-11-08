# POME-BT-NORMAL-TRACE-GRADIENT-OSCILLATION-001 — classified ledger

**Date / reviewed main:** 2026-11-08 / `b6933b772f41b45918f7e25ed1afbbb1fd892272`. **Starting audit head:** `698bbdcd81a1f957375261543e41ab5b09d40ad4`.  
**Severity:** low. **Status:** verified conditional deduction (sharpness). NOT a confirmed error, proof gap, verified repair, genuine duplication, or full theorem certification.

**Integrated anchor:** `docs/sections/bedford-taylor-products-and-local-capacity--gradients-against-positive-currents/index.html`, blob `520e13d0d2cc8e4a23e43bba61b940d7c5c1f8b2`, §7.14. Lemma 7.14.3 source `foundations-of-pluripotential-theory:3CDA1967`, permanent `8B33E7CC2E18`, lines 48–64, 69–109; coefficient identity (7.14.1) source `foundations-of-pluripotential-theory:DEE3D747`, permanent `9148FE66924C`, lines 25–32; gradient measure (7.14.4) source `foundations-of-pluripotential-theory:7591087E`, permanent `F48E1DFF8563`, lines 50–54.

**Finding:** on a bidisk, $\Theta=[w=0]$, $H=\mathrm{diag}(1/\pi,0)$, and explicit smooth PSH $v_k=m_k^{-1}\log(e^{a_k}+e^{b_k+m_k\Re w})\downarrow\max(0,\Re w)$ with $m_k=4^k$, $(a_k,b_k)$ alternating between $(1,3)$, $(3,1)$, satisfy $H^{1/2}\partial v_k\equiv0$ on $\Theta$, but adjacent ordinary gradients have trace-$L^2$ distance exactly $\frac{\tanh 1}{2}\sqrt{\mu(K)}>0$. Proof uses monotonicity of the three-parameter log-sum-exp and exact normal derivatives. No printed theorem false.

**Correct interpretation / optional note:** retain energy seminorm, not unweighted ambient $L^2(\Theta\wedge\beta)$. Add an optional warning; do not change the lemma's hypotheses or proof.

**Affected dependents:** Theorem 13.3.1 and similar gradient cutoff arguments **only if** they erroneously strengthen to full ambient gradient convergence; none newly shown false. **External inputs:** none beyond elementary calculus / integration current; the transitive proofs of §7.14, §13.3 are not certified.

**Disposition:** existing resolved/unresolved ledgers unchanged. Owner-excluded regularization/Bergman/weighted-L2/OT/multiscale/positivity-loss stays **deferred-by-user**. Full mathematical details: [report](../reports/2026-11-08-bt-normal-gradient-oscillation.md).
