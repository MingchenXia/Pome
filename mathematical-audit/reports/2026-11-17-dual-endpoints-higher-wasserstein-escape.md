# Dual endpoint convergence does not control higher Wasserstein moments of one-dimensional real Monge–Ampère measures

**Date:** 2026-11-17. **Finding:** \`POME-REALMA-WP-ENDPOINT-MOMENT-FAIL-001\`. **Severity:** low. **Status:** **verified conditional deduction**; the printed results are **not errors**. The deduction uses Pome Theorem 21.5.1 as the integrated Alexandrov pushforward input, not a new certification of its complete upstream convex-analysis proof.

## Exact repository anchor and mathematical scope

Reviewed \`main\` \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`.

- \`docs/sections/convex-analysis-and-toric-potentials--the-real-monge-ampere-measure/index.html\`, blob \`7089aa41ae2422b1bd6b5094e46668cbc8ed37be\`: Theorem **21.5.1**, source \`foundations-of-pluripotential-theory:4A0FAEB3\`, permanent tag \`409656CC47D4\`, physical lines **11–40**, supplies \(\operatorname{MA}_{\mathbf R}(F)=(G')_*(1_{(0,1)}\,ds)\) in dimension one, where \(G=F^*\) and \(\operatorname{dom}G=[0,1]\). Theorem **21.5.2**, source \`foundations-of-pluripotential-theory:6403CF44\`, permanent \`F4072D9ED060\`, lines **44–84**, gives vague continuity under locally uniform convergence and the full-mass criterion. Its Example **21.5.3**, permanent \`6BCC82ADB7C7\`, lines **90–96**, is an earlier *loss-of-mass* example and is not repeated here.
- \`docs/sections/convex-analysis-and-toric-potentials--compact-convex-envelopes-and-full-mass-limits/index.html\`, blob \`b3b4e34fff767a717df812a381f905589b257fb3\`: Lemma **21.6.2**, source \`foundations-of-pluripotential-theory:55EDF0D7\`, permanent \`F2FABB0A312F\`, lines **33–45**, upgrades vague convergence plus total-mass convergence to narrow convergence.
- \`docs/sections/measures-and-distributions--weak-convergence-of-measures/index.html\`, blob \`45720b2399a645a1a9a8148873fdc01c634fc5d7\`: Proposition **2.6.3**, source \`foundations-of-pluripotential-theory:A9ED3F7E\`, permanent \`54258F39AC23\`, and the section's vague/narrow distinction, are checked as contextual consistency, not newly certified.

## Statement: exact endpoint values and uniform primal/dual limits do not imply W_q convergence for q>1

Fix any \(q>1\). Choose \(\delta_j\downarrow0\), \(0<\delta_j<1\), and put
\[
\varepsilon_j=\delta_j^{q/(q-1)},\qquad
M_j=\delta_j/\varepsilon_j.
\]
Take \(j\) sufficiently large so \(0<\varepsilon_j<1/2\). Define the closed proper convex function \(G_j\) by setting it to \(+\infty\) outside \(P=[0,1]\), and on \(P\) by
\[
G_j(s)=
\begin{cases}
-M_js,&0\le s\le\varepsilon_j,\\
-\delta_j,&\varepsilon_j\le s\le1-\varepsilon_j,\\
-\delta_j+M_j(s-1+\varepsilon_j),&1-\varepsilon_j\le s\le1.
\end{cases}
\]
Set \(G=0\) on \([0,1]\), \(G=+\infty\) elsewhere; let \(F_j=G_j^*\) and \(F=G^*=\max\{0,x\}\). The slopes of \(G_j\) are \(-M_j,0,M_j\), in increasing order; hence \(G_j\) is convex. Both endpoint values are *identically correct*, not merely convergent:
\[
F_j^*(0)=G_j(0)=0=G(0),\qquad
F_j^*(1)=G_j(1)=0=G(1).
\]
Moreover, the uniform dual error and the Fenchel-conjugation sup inequality yield
\[
\sup_{[0,1]}|G_j-G|=\delta_j,\qquad
\sup_{\mathbf R}|F_j-F|\le\delta_j.
\]
All \(F_j,F\) are finite convex functions with *the same full slope body* \([0,1]\) and Alexandrov mass one; there is no loss of mass in the limit.

Theorem 21.5.1 directly evaluates the measures from the piecewise constant a.e. derivatives of \(G_j\):
\[
\boxed{\quad
\mu_j:=\operatorname{MA}_{\mathbf R}(F_j)
=\varepsilon_j\delta_{-M_j}
 +(1-2\varepsilon_j)\delta_0
 +\varepsilon_j\delta_{M_j},
\qquad
\mu:=\operatorname{MA}_{\mathbf R}(F)=\delta_0.\quad}
\]
This explicitly verifies the printed narrow-convergence assertion \(\mu_j\rightharpoonup\delta_0\): for any bounded continuous test function \(h\),
\[
\left|\int h\,d\mu_j-h(0)\right|\le4\varepsilon_j\|h\|_\infty\to0.
\]
Because the target measure is a Dirac mass, every coupling with \(\delta_0\) sends all source points to \(0\). There is no optimal-transport existence or monotone-coupling input: for **every** \(r\ge1\),
\[
\boxed{\quad W_r(\mu_j,\delta_0)^r
=\int|x|^r\,d\mu_j
=2\varepsilon_jM_j^r
=2\delta_j^r\varepsilon_j^{\,1-r}
=2\delta_j^{(q-r)/(q-1)}.\quad}
\]
In particular
\[
W_1(\mu_j,\delta_0)=2\delta_j\to0,\qquad
W_q(\mu_j,\delta_0)=2^{1/q}\quad\text{for all }j,
\]
and \(W_r(\mu_j,\delta_0)\to+\infty\) for \(r>q\). Each measure has finite moments of every order separately. For the particularly transparent choice \(q=2\), \(\delta_j=1/j\), \(\varepsilon_j=1/j^2\), the measure equals
\[
j^{-2}\delta_{-j}+(1-2j^{-2})\delta_0+j^{-2}\delta_j,
\quad W_1=2/j,\quad W_2=\sqrt2.
\]

## Exact scope, logical consequences, and correction

This is a **sharp boundary test** for attempting to strengthen either printed narrow-convergence theorem to a higher-moment transport statement. Its added force beyond prior audit findings is that **both conjugate endpoint values are fixed exactly**, both primal and dual convex functions converge **uniformly** (not only locally), every measure has the same full mass, and even \(W_1\) converges. The already recorded \`POME-TORIC-1D-W1-DUAL-ENDPOINT-001\` remains intact and is **not** recounted as this finding. The older escaped-mass Example 21.5.3 is mathematically different.

**Proposed addition, not a source edit:** whenever a dependent argument seeks \(W_q\) (\(q>1\)) convergence of \(\operatorname{MA}_{\mathbf R}(F_j)\), require a genuine \(q\)-moment tightness/uniform integrability condition on the a.e. dual gradients \(|(F_j^*)'|^q\), beyond full mass, narrow convergence, and dual endpoint values. In this model \(\int_{\{|x|>R\}}|x|^q\,d\mu_j=2\) for arbitrarily large \(j\) (take \(M_j>R\)). Thus the missing condition fails maximally. This proposal does not claim a printed Pome theorem used an invalid \(W_q\) upgrade; **no actual false dependent theorem has been identified**.

**Dependencies and limitations:** the finite-slope and pushforward conclusions are conditional on the integrated Theorem 21.5.1; the three-atom calculation, convexity, uniform conjugate bound, narrow convergence, and transport costs are independently checked algebraically. No whole-section proof or other upstream analytic inputs are certified. No regularization, Bergman, L², Ohsawa–Takegoshi, multiscale, or positivity-loss programme was examined; existing notes remain **deferred-by-user**.

**Actual coverage:** new proof-level cross-subject stress test of the already partially reviewed §§21.5–21.6, with §2.6 contextual consistency. **0 newly first-reviewed numbered sections; 0 entire-section certifications.** Previously recorded collection inventory: 25 chapters / 747 numbered sections; no claim to have certified all. No build/tests/CI/website publication and no changes to mathematical source bodies, registry, main, or permanent tags.
