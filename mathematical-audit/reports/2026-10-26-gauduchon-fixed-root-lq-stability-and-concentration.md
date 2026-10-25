# 2026-10-26 — fixed-root determinant stability versus concentration

**Reviewed main:** b6933b772f41b45918f7e25ed1afbbb1fd892272.
**Audit head before writing:** cd37374044b1a4fb86c814bd39412f4c88ab91ae.
**Integrated reading edition:** docs/sections/a-gauduchon-variational-volume--geometric-bounds-and-determinant-concentration/index.html, blob 6316720e1ce9112dc6b9b2f62db91361cba7e0cc.
**Provenance:** non-kahler-pluripotential-theory; source labels 6957E040 (Theorem 12.18.8), 1F4A2E2C (Equation 12.18.9), DB141F7B (Proposition 12.18.2), B7A807F6 (Equation 12.18.4); permanent tags 3EA495FF9D1A, 290803738499, 89AE8B534538 and A89800F03DB4.

The results below are **verified conditional deductions**, not allegations that the printed statements are false. Their standing inputs are the integrated theorem's determinant-density bound and sharp support formula, which in turn invoke the smooth prescribed-volume theorem 14.2.1, the bounded-mass identity 11.1.7 and the intrinsic determinant Lemma 12.18.6. Those complete upstream chains have **not** been independently certified here.

## POME-GAUD-FIXED-ROOT-STABILITY-001

**Severity/status:** low / **verified conditional deduction** (optional strengthening).

**Source anchors:** Theorem 12.18.8, lines 131–196; exact sharp support identity (12.18.9), lines 140–145; attaining density in lines 177–195; intrinsic formula (12.18.7), lines 103–124.

**Statement.** Assume the hypotheses of Theorem 12.18.8: a compact complex n-fold, n >= 2, with a positive Hermitian form beta satisfying dd^c(beta^j)=0 for j=1,...,n-1, a probability volume form dV and V=int_X beta^n. Put q=n/(n-1) and C=V^(-1/n). Fix a **strictly positive smooth real function** r, and set N=||r||_{L^n(dV)}. The smooth attaining current T_r supplied by that theorem has determinant density

\[
k_r=C\,r^{n-1}/N^{n-1},\qquad \|k_r\|_q=C,\qquad \int_X r k_r\,dV=CN.
\]

For every normalized positive Gauduchon current T in the same family, with determinant density k=k_T and fixed-root deficit

\[
\Delta_r(T)=CN-\int_X r\,k\,dV\ \ge 0,
\]

one has the **quantitative stability inequality**

\[
\boxed{\quad
\|k-k_r\|_{L^q(dV)}
\le
2^{(3-q)/2}\sqrt{\frac{C\,\Delta_r(T)}{(q-1)\,N}}.
\quad} \tag{A}
\]

The square-root exponent is optimal, already for smooth positive closed currents on a fixed flat complex torus and fixed root r=1. Consequently, any **directed net** of currents with fixed-root deficits tending to zero has determinant densities converging strongly to k_r in L^q, without extracting a sequence. No convergence of the currents themselves is inferred merely from (A).

**Proof.** Define the probability measure \(d\rho=(r/N)^n dV\), and the nonnegative measurable function \(x=k/k_r\). The strict positivity of r makes this quotient well-defined everywhere. Since \(k_r^q\,dV=C^q\,d\rho\), the theorem's bound \(\|k\|_q\le C\) gives

\[
\int x^q\,d\rho\le1,\qquad
\int x\,d\rho
=\frac{\int r k\,dV}{CN}
=1-\varepsilon,\qquad
\varepsilon=\frac{\Delta_r(T)}{CN}.
\]

For \(1<q\le2\) and \(x\ge0\), the integral Taylor remainder (with continuity at x=0) gives

\[
D_q(x):=x^q-1-q(x-1)
=q(q-1)(x-1)^2\int_0^1(1-s)(1+s(x-1))^{q-2}\,ds
\ge \frac{q(q-1)}2\frac{(x-1)^2}{(1+x)^{2-q}}.
\]

Indeed \(1+s(x-1)\le1+x\) and \(q-2\le0\). The first two displayed moment bounds imply

\[
\int D_q(x)\,d\rho
=\int x^q\,d\rho-1+q\varepsilon
\le q\varepsilon,
\qquad
J:=\int\frac{(x-1)^2}{(1+x)^{2-q}}\,d\rho
\le\frac{2\varepsilon}{q-1}.
\]

Hölder's inequality with exponents \(2/q\) and \(2/(2-q)\) (the \(q=2\) case taken directly) yields

\[
\int|x-1|^q\,d\rho
\le J^{q/2}
\left(\int(1+x)^q\,d\rho\right)^{(2-q)/2}.
\]

The elementary convexity estimate \((1+x)^q\le2^{q-1}(1+x^q)\) gives \(\int(1+x)^q\,d\rho\le2^q\). Therefore

\[
\|x-1\|_{L^q(\rho)}
\le2^{(2-q)/2}\sqrt{\frac{2\varepsilon}{q-1}},
\]

and multiplication by C proves (A).

To prove **optimality of the exponent**, take \(X=E^n\), \(\beta=\sum_j\omega_j\) and \(dV=\bigwedge_j\omega_j\) as in Proposition 12.18.2 (lines 34–77). Choose a nonconstant smooth real mean-zero function \(\phi\) on the first elliptic factor. For sufficiently small real t, set \(f_t=1+t\phi>0\). By the one-dimensional dd^c potential argument already given on lines 69–77, the closed positive form \(A_t=f_t\omega_1+\sum_{j\ge2}\omega_j\) is in the cohomology class of beta, and \(T_t=A_t^{n-1}/V\) is a normalized positive current. Its density is \(k_t=C f_t^\alpha\) with \(\alpha=(n-1)/n=1/q\). For the **fixed root** r=1,

\[
\Delta_1(T_t)
=C\left[1-\int(1+t\phi)^\alpha\,dV\right]
=\frac{C\alpha(1-\alpha)}2\,t^2\int\phi^2\,dV+O(t^3),
\]

whereas

\[
\|k_t-C\|_q
=C\alpha\,|t|\,\|\phi\|_q+O(t^2).
\]

Thus the square-root power cannot be replaced by any greater exponent in a uniform deficit estimate. The construction uses only elementary Taylor expansion and the compact-curve Poisson equation, not a regularization argument.

**Disposition/proposed correction:** Theorem 12.18.8 and its proof remain correct as checked conditionally; optionally append (A) as a corollary immediately after the sharp support identity. Affected dependents: quantitative interpretation of 12.18.2 and 12.18.17 for **fixed** roots, and any claim that a fixed-root near-maximizer need not converge at the critical determinant density exponent. This theorem does **not** control L^p for p>q.

## POME-GAUD-CONCENTRATION-LQ-VS-LP-001

**Severity/status:** low / **verified conditional deduction** (sharpness strengthening, not an error).

**Source anchors:** Proposition 12.18.2, lines 34–96; forms and density in (12.18.4), lines 58–74; higher-moment blowup (12.18.3), lines 43–48 and 85–91. Further context: Theorem 12.18.17, lines 289–361, concerns a different sequence of **varying** maximizing roots and is not being re-registered.

**Statement.** For the exact sequence \(S_\varepsilon=T_{\varepsilon,t_\varepsilon}\) of Proposition 12.18.2 with \(t_\varepsilon=1/\log(1/\varepsilon)\), not only does the fixed-root deficit tend to zero, but

\[
\boxed{\quad
\|k_{S_\varepsilon}-C\|_q
\le C\,[2/\log(1/\varepsilon)]^{1/q}
\longrightarrow0,\quad C=V^{-1/n}.
\quad} \tag{B}
\]

Moreover, the **currents themselves** converge to the unique fixed-root maximizer \(T_*\) in the total-variation norms of all matrix coefficients in the displayed product frame, with error O(1/log(1/epsilon)). At the same time, for every p>q, the L^p norms of their determinant densities diverge, and the L-infinity norms diverge, as proved in the original source. Thus **even strong critical L^q convergence of densities and strong coefficient-measure convergence of currents do not control any higher L^p moment**.

**Proof.** Recall \(f_{\varepsilon,t}=1-t+t b_\varepsilon\), where \(b_\varepsilon\ge0\) and \(\int b_\varepsilon\,dV=1\), and \(k_{\varepsilon,t}=C f_{\varepsilon,t}^{\alpha}\) with \(\alpha=1/q\) (equation 12.18.4). For nonnegative a,b and \(0<\alpha<1\), subadditivity of \(s^\alpha\) gives \(|a^\alpha-b^\alpha|^{1/\alpha}\le|a-b|\). Consequently,

\[
\|k_{\varepsilon,t}-C\|_q^q
\le C^q\int|f_{\varepsilon,t}-1|\,dV
=C^q t\int|b_\varepsilon-1|\,dV
\le2C^q t.
\]

This gives (B). The same exact form expansion yields

\[
T_{\varepsilon,t}-T_*
=\frac{t}{n}(b_\varepsilon-1)\sum_{i=2}^n H_i.
\]

In the fixed smooth basis \(H_i\), each nonzero scalar coefficient has total variation at most \(2t/n\) (with volume normalized to one). This is coefficientwise total-variation convergence. Finally, original lines 85–91 prove \(\int k_{S_\varepsilon}^p\,dV\ge C_{n,p}t_\varepsilon^{\alpha p}\varepsilon^{2-2\alpha p}\to\infty\) for p>q; the same lines prove L-infinity blowup. There is no conflict between these stronger convergences and supercritical concentration.

**Disposition/proposed correction:** Proposition 12.18.2 is mathematically correct as printed; optionally add the two-line critical-norm/total-variation convergence argument after its proof. This sharply separates fixed-root maximization, strong endpoint convergence, and supercritical moment failure.

## Actual proof-reading coverage and boundaries

This is the **first selected proof-level audit of §12.18**, previously an inventory-only row in the 747-section matrix. Directly inspected the integrated statements and arguments at: 12.18.1 (lines 13–29); 12.18.2 and its formulas (34–96); 12.18.6 (103–126); 12.18.8 (131–198); 12.18.13 (201–229); 12.18.15 (232–288); 12.18.17 (291–361). Checked explicitly the sign/normalization of the first-factor dd^c Poisson equation; \(V=n!\); \(q=n/(n-1)\); rank-one coefficient singularity in 12.18.17; and the distinction between bounded-potential Monge–Ampère mass and the intrinsic determinant measure of a limiting current. No confirmed false theorem or new proof gap was found in these selected lines.

**Uncertified inputs:** smooth Monge–Ampère existence in 14.2.1, mass invariance in 11.1.7, the determinant duality/strict-maximizer framework of §§12.7–12.9, and full Bedford–Taylor product continuity (used separately in 12.18.17). No new claim of self-contained proof for them; no complete §12.18 or chapter certification.

**Author-directed exclusion remains in force:** all dedicated Demailly approximation/regularization, Bergman, L2, Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof-completion questions remain **deferred-by-user**, neither resolved nor reopened. Historical attribution and the source's permanent tags are retained.

No project tests, formalization, build, CI, website publication, manuscript/source/registry/tag editing or main-branch changes were performed.