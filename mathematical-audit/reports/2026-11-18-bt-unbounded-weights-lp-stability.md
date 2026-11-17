# §7.5: Unbounded quasi-continuous weights under a moving trace-moment bound

**Finding ID:** POME-BT-UNBOUNDED-WEIGHT-LP-UI-001  
**Classification:** low / **verified conditional deduction**, not a false printed theorem and not a claim that the upstream Bedford–Taylor machinery is globally certified.  
**Reviewed main:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\` (2026-11-18).  
**Integrated reading edition:** \`docs/sections/bedford-taylor-products-and-local-capacity--quasi-continuity-and-convergence-in-capacity/index.html\`, blob \`464778b7ca6f1a456e36b24ecb4a0c93ab6948d3\`.  
**Stable anchors:** Definition 7.5.5, original \`foundations-of-pluripotential-theory:F3E0CD1A\`, permanent \`DAD5D0809372\`, physical lines 84–89; Lemma 7.5.7, original \`foundations-of-pluripotential-theory:39398ED2\`, permanent \`880C30054932\`, lines 125–166 (trace/capacity domination at 125–147, fixed and varying bounded weights at 148–166); Theorem 7.5.8, original \`foundations-of-pluripotential-theory:2B1AA42A\`, permanent \`42828E3BDDFA\`, lines 172–185. These are the **integrated main HTML physical lines**, not original manuscript coordinates.

## Precisely delimited extension

Let \(B\Subset\mathbb C^n\) be a ball, \(0\le q\le n\), and \(S_a=dd^c u_{1,a}\wedge\cdots\wedge dd^c u_{q,a}\) be a **directed net** of positive Bedford–Taylor currents, with potentials in one family uniformly bounded on each compact subset of \(B\). Assume \(S_a\to S\) weakly on the **original directed index set**. Write \(\beta=dd^c|z|^2\) and \(\mu_a=S_a\wedge\beta^{n-q}\), \(\mu=S\wedge\beta^{n-q}\); the \(q=0\) convention is \(S_a=1\).

Let \(f_a:B\to\mathbb R\) be finite real Borel functions converging to a finite real **quasi-continuous** function \(f\) locally in Bedford–Taylor capacity. Do **not** assume a pointwise bound on \(f_a\) or \(f\). Instead suppose there is a fixed \(p>1\) such that, for every compact \(K\Subset B\),
\[
 M_{K,p}:=\sup_a\int_K |f_a|^p\,d\mu_a<\infty.
\]
Then \(f_aS_a\to fS\) weakly, with the products interpreted as order-zero currents whose coefficients are locally integrable. In fact \(f\in L^p_{\mathrm{loc}}(\mu)\), a conclusion, **not an extra hypothesis**.

The same assertion holds for sequences; that version uses the printed Lemma 7.5.7 directly. The arbitrary-net version uses only its quantitative, fixed-test weighted-capacity argument (lines 148–166), which is independent of any sequential extraction. The result also applies after the unweighted product convergence of Theorem 7.5.8, so the printed bounded-weight hypothesis there can be replaced by the **moving trace \(L^p\) assumption** as a separate conditional corollary.

## Complete deduction from the specified inputs

Set \(T_R(t)=\max(-R,\min(R,t))\) for \(R>0\). The maps \(T_R\) are 1-Lipschitz, so \(T_R(f_a)\to T_R(f)\) locally in capacity. The limit \(T_R(f)\) is bounded and quasi-continuous, and all \(T_R(f_a)\) are bounded by \(R\). Lemma 7.5.7 therefore gives
\[
 T_R(f_a)S_a\longrightarrow T_R(f)S
 \qquad\text{weakly for every fixed }R.
 \tag{1}
\]
This statement holds for the original directed net: the proof's measure bounds and small-capacity estimates quantify over all sufficiently late indices, without choosing a subsequence.

**The limiting moment is automatic.** Fix \(K\Subset\operatorname{Int}K'\Subset B\) and a nonnegative continuous cutoff \(\chi\le1\), identically 1 on \(K\), supported in \(K'\). The functions \(|T_R(f_a)|^p\) converge in capacity to bounded quasi-continuous \(|T_R(f)|^p\). Apply the *trace-measure* instance of (1) with these weights:
\[
 \int\chi |T_R(f)|^p\,d\mu
 =\lim_a\int\chi |T_R(f_a)|^p\,d\mu_a
 \le M_{K',p}.
\]
Monotone convergence as \(R\uparrow\infty\) yields
\[
 \int_K|f|^p\,d\mu\le M_{K',p}. \tag{2}
\]
No informal exchange of the two limits \(a\to\infty\) and \(R\to\infty\) is made; \(R\) is fixed first and the final monotone limit is taken only on \(\mu\).

**Uniform-integrability removal of clipping.** For every real \(t\) and \(p>1\),
\[
 |t-T_R(t)|=(|t|-R)_+\le R^{1-p}|t|^p.
 \tag{3}
\]
Hence the trace tails satisfy
\[
 \sup_a\int_K|f_a-T_R(f_a)|\,d\mu_a
 \le R^{1-p}M_{K,p},
\]
while (2) gives the same decay for \(f-T_R(f)\) with respect to \(\mu\). Positivity of \(S_a,S\) bounds the total variations of all coefficient measures by a dimensional multiple of their trace measures (the positivity estimate invoked in the proof of Lemma 7.5.7, lines 148–150). Consequently, for each compactly supported smooth test form \(\Phi\),
\[
 \left|\langle(f_a-T_R(f_a))S_a,\Phi\rangle\right|
 \le C_{n,q,\Phi}R^{1-p}M_{K,p},
 \tag{4}
\]
and likewise for the limiting current, with \(K\) chosen to contain \(\operatorname{supp}\Phi\). Fixing \(R\), use (1), then take \(R\uparrow\infty\) in the two errors (4). This proves weak convergence on the original net. Local \(L^1\) integrability, so that all products are defined, follows from Hölder and the locally finite trace mass.

There is no claim of an intrinsic \(L^p\) estimate for every Bedford–Taylor weight: the moving moment bound is an **additional, explicitly required assumption**. Nor does this result imply arbitrary products of unbounded psh functions are defined.

## Endpoint and relation to the earlier ledger

The strict threshold \(p>1\) cannot be replaced by a mere uniform \(L^1(\mu_a)\) bound. On the unit disc take the fixed smooth positive current \(S=dd^c|z|^2\), \(\mu=S\), and nonnegative smooth bumps \(f_j\) supported in \(\{|z|<1/j\}\), normalized by \(\int f_j\,d\mu=1\). Their supports have relative condenser capacity tending to zero (equivalently, use the explicit logarithmic relative extremals), so \(f_j\to0\) locally in capacity and the moving \(L^1\) norms equal 1. Yet \(f_j\mu\rightharpoonup\delta_0\ne0\), since the supports shrink to the origin. This is the **previously documented bounded-weight/L1 obstruction**, recalled only to delimit the *new positive \(L^p\) theorem*; it is **not counted as a new counterexample finding**.

The condition \(p>1\) is sufficient but not necessary: the proof needs only locally uniform integrability of the weighted trace densities \(\{f_a\}\) relative to \(\{\mu_a\}\), together with a corresponding limiting trace-tail bound obtained by the fixed-clipping argument. A single global exponent is a concrete, reproducible criterion.

## Classification, dependents, and proposed placement

**Status:** verified conditional deduction; **severity:** low. The printed Lemma 7.5.7 and Theorem 7.5.8 remain correct, with their **bounded** weights and sequence hypotheses unchanged. Proposed source-independent addition: record the theorem above as an optional corollary to §7.5.7, replacing bounded weights by a moving uniform \(L^p\) trace-moment condition. Potential dependents: §7.5.8's weighted-product conclusion and other uses of weighted Bedford–Taylor limits that have this added moment estimate. Do not silently change any of their hypotheses.

**Genuine unverified upstream inputs:** the original localized mixed-product capacity domination in Lemma 7.5.7(1), weak-current positivity/coefficient trace domination, and its original bounded-weight convergence proof; §§7.3–7.4 underlying Bedford–Taylor construction and capacity properties. Those are *precisely* the conditional ingredients; this report does not certify them. The previous net and L1-obstruction findings remain separate, not merged or renamed.

**Coverage accounting:** New verification of clipping, automatic limiting \(L^p\) integrability and sharp \(R^{1-p}\) tail removal at §7.5.7, plus the consequence at §7.5.8. The section had already been sampled: **zero first-time numbered sections; zero entirely certified sections**. No build, test suite, CI, source/body/registry modification or publication. The owner-excluded Demailly approximation/regularization, Bergman, L², Ohsawa–Takegoshi, multiscale-atlas and positivity-loss programme remains **deferred-by-user**, not reviewed or certified.
