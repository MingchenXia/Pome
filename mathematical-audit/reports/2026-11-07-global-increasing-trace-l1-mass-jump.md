# 2026-11-07 — globally realized increasing-trace discontinuity with exact ambient rates

**Finding ID:** **POME-TRACE-GLOBAL-INCREASING-L1-MASS-JUMP-001**. **Severity:** low. **Status:** **verified conditional deduction**, *not* a false printed theorem or a verification of the general trace construction. The original increasing-discontinuity Example 20.2.23 is correct. This report supplies a global realization, all projective dimensions, an exact ambient \(L^1\) rate, a sharp sublevel-volume rate, and a maximal non-pluripolar mass contrast not quantified by the printed local example.

**Reviewed production main:** b6933b772f41b45918f7e25ed1afbbb1fd892272 (unchanged).
**Integrated reading source:** docs/sections/the-trace-operator/index.html, Git blob 1f3a3e4f0317a308b43bd3df53dda84c5f3fa50a; Definition 20.2.6 physical lines 224–230 (source sgpt:DC6538A0, permanent ADF6E265888F); Example 20.2.15 lines 309–313 (source sgpt:050DD15F, permanent 917FA516701F); Proposition 20.2.22 lines 445–468 (source sgpt:762F23ED, permanent 58627BFD2457); Example 20.2.23 lines 548–560 (source sgpt:E0CF7EEA, permanent 531FFD6D4B64).
**Non-pluripolar definition crosscheck:** docs/sections/non-pluripolar-products--truncation-and-plurifine-locality/index.html, blob 81be8c5acc360c96bd3c5acba05a3cdb5fafaf4c, physical lines 7–13 and 57–63; Definition 13.2.4 source foundations-of-pluripotential-theory:9D8E4DD8, permanent D79952D7E272.

## Statement and precise hypotheses

Fix an integer \(n\ge2\), put \(X=\mathbb P^n\), and normalize \(\omega=\omega_{\mathrm{FS}}\) by \(\int_X\omega^n=1\) and \(dd^c=\frac{i}{2\pi}\partial\bar\partial\). Let \(H_i=\{Z_i=0\}\) and let \(Y=H_2\simeq\mathbb P^{n-1}\). Define global upper-semicontinuous \(\omega\)-psh potentials
\[
 F_i([Z])=\log\frac{|Z_i|^2}{\sum_{k=0}^n|Z_k|^2},\qquad
 u_j=\max\{F_1,j^{-1}F_2\},\quad j=1,2,\ldots.
\]
Then \(u_j\le0\) increases, has analytic singularities and satisfies \(\nu(u_j,Y)=0\). Its pointwise supremum equals \(0\) off \(Y\) and \(F_1|_Y\) on \(Y\), while its upper-semicontinuous regularization is \(0\) on all of \(X\).

Writing \(H_n=\sum_{k=1}^n k^{-1}\), there is the **exact sharp ambient rate**
\[
 \lim_{j\to\infty} j\int_X(-u_j)\,\omega^n=H_n.
\]
For each fixed \(\delta>0\), there is the **exact exponentially small sublevel rate**
\[
 \lim_{j\to\infty}e^{j\delta}
   \int_{\{u_j<-\delta\}}\omega^n
   =n\bigl[1-(1-e^{-\delta})^{\,n-1}\bigr].
\]
Nevertheless the analytic restriction representative on \(Y\) is always \(F_1|_Y\); its total non-pluripolar \((n-1)\)-fold Monge–Ampère mass is **zero**, whereas the trace of the limiting potential \(0\) has mass **one**. Thus even quantitatively strong ambient \(L^1\)/volume convergence does not justify an increasing-limit interchange with the trace.

## Complete elementary model proof

**(1) Global positivity and analytic singularities.** Poincaré–Lelong applied in a local projective frame yields
\[
 \omega+dd^cF_i=[H_i].
\]
Consequently \(F_1\) and \(F_2/j\) are \(\omega\)-psh, since
\[
 \omega+dd^c(F_2/j)=(1-1/j)\omega+j^{-1}[H_2]\ge0.
\]
The maximum of two functions with this common lower curvature bound is again \(\omega\)-psh (add a local smooth potential of \(\omega\) before taking the maximum). Near \(H_1\cap H_2\) choose a chart trivializing \(\mathcal O(1)\), with local equations \(z_1,z_2\). Up to locally bounded terms,
\[
 u_j=\max\{\log|z_1|^2,j^{-1}\log|z_2|^2\}
     =j^{-1}\log(|z_1|^{2j}+|z_2|^2)+O(1),
\]
using \(0\le\log(A+B)-\max(\log A,\log B)\le\log2\).
Elsewhere \(u_j\) is locally bounded, so every \(u_j\) has analytic singularities. At the generic point of \(Y\) one has \(Z_1\ne0\), hence \(u_j=F_1\) locally near that point and \(\nu(u_j,Y)=0\). Finally \(F_2\le0\), so \(F_2/j\) increases with \(j\); this proves monotonicity. At \(X\setminus Y\), \(F_2/j\to0\), so \(u_j\to0\). On \(Y\), \(F_2=-\infty\), hence \(u_j=F_1\) for all \(j\). The complement of \(Y\) is dense, giving \((\sup_j u_j)^*=0\).

**(2) Exact \(L^1\) rate.** Set \(a_i=-F_i\ge0\). Pointwise,
\[
 j(-u_j)=\min\{j a_1,a_2\}.
\]
On a full \(\omega^n\)-measure subset, \(a_1>0\) and \(a_2<\infty\). Thus \(\min(j a_1,a_2)\uparrow a_2\), and monotone convergence reduces the limit to \(\int_X-\log t_2\,\omega^n\), with \(t_i=|Z_i|^2/\sum|Z_k|^2\). The normalized Fubini–Study probability is the projectivization of independent standard complex Gaussian coordinates: their squared norms are independent exponential random variables, so \((t_0,\ldots,t_n)\) is the uniform Dirichlet distribution on the simplex. In particular \(t_2\) has density \(n(1-t)^{n-1}\,dt\) on \((0,1)\). The integral is elementary:
\[
 \mathbb E[-\log t_2]
  =\int_0^1\frac{1-(1-t)^n}{t}\,dt
  =\sum_{k=0}^{n-1}\int_0^1(1-t)^k\,dt=H_n.
\]
This simultaneously gives \(\|u_j\|_{L^1}\le H_n/j\) and sharp asymptotic equality.

**(3) Exact fixed-threshold volume rate.** Let \(q=e^{-\delta}\in(0,1)\). Since \(u_j<-\delta\) is equivalent to \(t_1<q\) **and** \(t_2<q^j\), condition on \(t_2=t\). The marginal density is \(n(1-t)^{n-1}\); conditional on \(t_2=t\), the normalized coordinate \(t_1/(1-t)\) has Beta\((1,n-1)\) density. Its probability of being less than \(q/(1-t)\) approaches \(1-(1-q)^{n-1}\) as \(t\downarrow0\). Integrating over \(0<t<q^j\), dividing by \(q^j\) and using continuity at \(t=0\) gives the stated limit. In particular the cruder estimate \(\operatorname{vol}\{u_j<-\delta\}\le 1-(1-e^{-j\delta})^n\le n e^{-j\delta}\) is valid for **every** \(j\).

**(4) Restriction and mass contrast.** Since \(F_2|_Y=-\infty\), one has the exact representative \(u_j|_Y=F_1|_Y\). The restriction is not identically \(-\infty\), and Poincaré–Lelong on \(Y\) gives
\[
 \omega|_Y+dd^c(F_1|_Y)=[D],
 \qquad D=H_1\cap Y.
\]
Outside the divisor \(D\) this current is identically zero; by Definition 13.2.4 its non-pluripolar self-product puts no mass on the pluripolar set \(D\). Consequently
\[
 \int_Y\langle(\omega|_Y+dd^cF_1|_Y)^{n-1}\rangle=0.
\]
On the other hand \(\operatorname{Tr}_Y(0)\) has the smooth representative \(0\), with \(\int_Y\omega^{n-1}=1\). Example 20.2.15 identifies the trace of each \(u_j\), which has analytic singularities and generic Lelong number zero along \(Y\), with \(F_1|_Y\) **up to \(P\)-equivalence**. Passage from this explicit representative to the total trace mass uses the existing invariance of non-pluripolar volume under \(P\)-equivalence; this upstream general theorem is *not* recertified here. The two representative masses \(0\) and \(1\) themselves are calculated independently.

## Classification, correction and limits

This is a **verified conditional deduction / quantitative global strengthening**, not a counterexample to any printed result. The local two-variable phenomenon in the original Example 20.2.23 remains correct; our distinct contribution is a globally well-defined \(\mathbb P^n\) family together with the optimal \(H_n/j\) integral constant, exact exponential sublevel constant, and maximal restricted non-pluripolar mass contrast. Proposition 20.2.22 is expressly about **decreasing \(d_S\)-convergent nets**; it is not contradicted. We have **not proved ambient \(d_S\) convergence**, only the stated \(L^1\) and volume convergence. Do not silently replace either topology or reverse its monotonicity.

**Proposed nonproduction edit:** optionally add this explicit globally normalized model and the mass caveat as a qualification after Example 20.2.23. Keep all existing stable source tags, permanent tags, attribution and the decreasing-net theorem. **Potential affected dependents:** any future use of increasing \(L^1\)-convergent (or in-measure-convergent) analytic potentials to infer convergence of traces, restricted non-pluripolar masses or restricted volumes without a separately justified continuity principle. No specific downstream printed theorem is declared false.

**Verified scope:** only the global explicit family, projective probability integrals and divisorial NPP cutoff, plus selected integrated Example 20.2.15 and Example 20.2.23; Proposition 20.2.22 checked only for its *directional hypothesis*. The trace construction, \(P\)-equivalence/mass invariance and any regularization-dependent part of its general proofs are **not** claimed verified. All owner-excluded Demailly approximation/regularization and dedicated Bergman, weighted-\(L^2\), Ohsawa–Takegoshi, multiscale-atlas and positivity-loss programmes remain **deferred-by-user**, neither reopened nor certified.
