# Arbitrary directed-net stability for non-pluripolar products; direct §17.9 review
**Date:** 2026-11-20. **Reviewed production main:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`.

## Direct scope and anchors

- All mathematical lines **7–209** of §13.7, \`docs/sections/non-pluripolar-products--capacity-convergence-and-loss-of-mass/index.html\`, blob \`d66813856cb813722806ab912afdfd4815d2da97\`. Source \`foundations-of-pluripotential-theory\`. Lemma 13.7.3: source \`4720F1AB\`, permanent \`274B700496A8\`, lines 42–67. Lemma 13.7.4: source \`FE9C8C30\`, permanent \`88D1663D1111\`, lines 75–102. Theorem 13.7.5: source \`AB4EBE3B\`, permanent \`67C4F7EC316E\`, lines 107–134. Proposition 13.7.8: source \`8CF7A9C6\`, permanent \`4B60F7F33590\`, lines 148–171. Corollary 13.7.9: source \`82DB3E57\`, permanent \`D73416504271\`, lines 176–209.
- All mathematical lines **7–75** of §17.9, \`docs/sections/relative-energy-and-perron-segments--extremal-slopes-and-long-perron-segments/index.html\`, blob \`023e78b3da0fd8f33d39177dba02f410b10f376c\`. Proposition 17.9.1: source \`foundations-of-pluripotential-theory:58E4D688\`, permanent \`0583958ACA6D\`, lines 11–26. Proposition 17.9.2: source \`:2B4D191D\`, permanent \`A6533ED6CC68\`, lines 34–75.

## POME-NPP-CAPACITY-DIRECTED-NET-WEIGHTED-001

**Severity: low. Status: verified conditional deduction (not a printed error).** Conditional on the actual sequential Theorem 13.7.5 and Corollary 13.7.9, not on Demailly regularization. Their complete upstream chains have **not** been certified.

Let \(X\) be a compact Kähler \(n\)-fold and \(I\) any directed set. Let \(T_{j,\alpha}=\theta_j+dd^c u_{j,\alpha}\) and \(T_j=\theta_j+dd^c u_j\) be positive closed currents, \(1\le j\le p\le n\), with \(u_{j,\alpha}\to u_j\) in **extended local capacity**, defined by the arctangent distance in §13.7.2, along the original net. Write \(R_\alpha=\langle T_{1,\alpha}\wedge\cdots\wedge T_{p,\alpha}\rangle\) and \(R=\langle T_1\wedge\cdots\wedge T_p\rangle\).

**Claim.** The quantities \(\sup_X u_{j,\alpha}\) are jointly uniformly bounded above on some tail. For each smooth strongly positive \((n-p,n-p)\)-form \(\eta\),
\[
\liminf_\alpha\int_X R_\alpha\wedge\eta\ge\int_XR\wedge\eta.
\]
If additionally
\[
\limsup_\alpha\int_X R_\alpha\wedge\omega^{n-p}
\le\int_X R\wedge\omega^{n-p},
\]
then \(R_\alpha\rightharpoonup R\) as the **original directed net**, with no countable cofinality assumption.

For Borel weights \(0\le\chi_\alpha,\chi\le A<\infty\), suppose \(\chi_\alpha\to\chi\) locally in capacity and \(\chi\) is quasi-continuous. Then the same lower bound holds with \(R_\alpha,R\) replaced by \(\chi_\alpha R_\alpha,\chi R\); under the preceding unweighted mass condition the weighted currents converge weakly (as Radon measures when \(p=n\)). Locally the lower-bound statements also hold if the products are locally finite and local psh representatives are *eventually locally uniformly bounded above*.

### Proof

**Countable determining tests and noncofinal extraction.** Fix the finite atlas of Definition 13.7.2, countable compact exhaustions in its charts, and countably many positive rational thresholds. For each \(j\), the capacities of the arctangent discrepancy sets on those compacts tend to zero along \(I\). Add ordinary capacity discrepancy tests for \(\chi_\alpha\), if present. Enumerate all these scalar tests \(q_1,q_2,\ldots\). If \(B\subset I\) is cofinal, choose inductively \(\alpha_k\in B\), increasing, so that \(q_i(\alpha_k)\le1/k\) for all \(i\le k\). Indeed finite collections of these inequalities hold on a common tail; directedness gives a joint lower index, then cofinality of \(B\) provides a member above it and \(\alpha_{k-1}\). Thus along the selected **ordinary sequence**, every potential converges in extended local capacity and every selected weight converges in local capacity. Importantly, \((\alpha_k)\) need **not** be cofinal in \(I\).

**Uniform upper normalization.** If no tail bounds \(\max_j\sup_Xu_{j,\alpha}\), then for each \(k\) the set \(B_k=\{\alpha:\max_j\sup_Xu_{j,\alpha}>k\}\) meets *every* tail. Choose increasing \(\alpha_k\in B_k\) satisfying the first \(k\) discrepancy tests with error \(1/k\). The resulting sequence converges in extended capacity to each \(u_j\). The *sequential* global-normalization clause of Lemma 13.7.3 bounds each \(\sup_Xu_{j,\alpha_k}\); finitely many \(j\) give a joint bound, contradicting \(\max_j\sup_Xu_{j,\alpha_k}>k\). Restrict to this common upper-bound tail thereafter.

**Lower bound.** If the claimed net inequality failed for \(\eta\), choose \(\varepsilon>0\) such that the bad set \(B=\{\alpha:\int R_\alpha\wedge\eta<\int R\wedge\eta-\varepsilon\}\) is cofinal. Apply the selection procedure to \(B\), respecting the upper-bound tail. The resulting sequence fulfills exactly the hypotheses of *sequential* Theorem 13.7.5, and its lower limit must be at least \(\int R\wedge\eta\), a contradiction. For compactly supported local tests the same argument applies under the stated local hypotheses.

**Weak convergence with mass control.** If \(R_\alpha\) failed to converge weakly, one fixed smooth test form \(\zeta\) and \(\varepsilon>0\) would give a cofinal bad set \(B=\{\alpha:|\langle R_\alpha-R,\zeta\rangle|>\varepsilon\}\). In addition to the capacity tests, impose at the \(k\)-th selection the eventual bound \(\int R_{\alpha_k}\wedge\omega^{n-p}\le\int R\wedge\omega^{n-p}+1/k\), available from the net mass limsup condition. The *sequential* convergence clause of Theorem 13.7.5 now forces \(R_{\alpha_k}\rightharpoonup R\), contradicting membership in \(B\). No sequential compactness of a nonmetrizable current space has been assumed.

**Varying weights.** Include the capacitary tests for \(\chi_\alpha\) in the same extraction. A failure of either weighted lower inequality or, with mass control, weighted weak convergence would produce a cofinal bad set and a selected sequence to which the actual **sequential** Corollary 13.7.9 applies, giving the corresponding contradiction. There is no interchange of a directed-net limit with the \(C\to\infty\) or \(\varepsilon\downarrow0\) truncation limits.

This is a countably determined *bad-test extraction* argument. It does not assert sequentiality of arbitrary weak-current topologies or existence of countable cofinal indices.

### Review of original statements, caveats and affected dependents

The full §13.7 direct reading checked chart-capacity comparison, truncation/arctangent equivalence, cutoff weights and Bedford–Taylor locality, lower semicontinuity, the Fubini–Study loss-of-mass example, monotone directed psh nets, and quasi-continuous varying weights. In §17.9 the full proofs of endpoint essential sup/inf slopes, subgeodesic \(q_s=\max(u,\phi-s)\), long-segment monotonicity, and the bounded-change estimate \(Cs/T\) were read. No **new** printed error was established; prior §13.7 mass-loss and §17.9 endpoint-slope findings were **not** recounted. The noncofinal sequence selection is compatible with §13.7.8's explicit warning.

**Remaining upstream inputs:** §7.4.3 local capacity comparison, §7.5.2 quasi-continuity, §7.5.8 sequential weighted bounded Bedford–Taylor convergence, §13.2.2 truncation locality, §13.5.4–5 mass bounds, §10.3.1 global normalization, §17.7.8–9 weak-geodesic comparison. These are **not** certified in this report. This finding differs from the previously recorded local-uniform bounded BT net stability (POME-BT-JOINT-NET-STABILITY-001): its hypotheses and conclusions concern **extended capacity**, **non-pluripolar** products, **mass-controlled** weak convergence and **varying quasi-continuous weights**.

**Proposed patch:** a separately reviewable corollary after §13.7.9, explicitly warning that the extracted contradiction sequence need not be cofinal; preserve original statements, source attribution and permanent tags. Potential dependents include directed model-envelope and energy-approximation constructions **only when their precise mass/weight hypotheses hold**. Excluded Demailly approximation/regularization and Bergman, L², Ohsawa–Takegoshi, multiscale and positivity-loss completion stay **deferred-by-user**, not verified or resolved.

**Coverage delta:** two whole integrated sections directly read; zero fully certified upstream dependency chains; no tests, builds, CI, source/main, registry, tag or website edits.
