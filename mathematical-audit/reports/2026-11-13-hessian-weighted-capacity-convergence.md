# Nonmonotone capacity convergence in the weighted signed-measure lemma

- **Finding:** POME-HESS-WEIGHT-CAPACITY-VAGUE-STABILITY-001.
- **Date / severity / status:** 2026-11-13; low; **verified conditional deduction**. The printed result is **not** false and no correction to its existing hypotheses is required.
- **Reviewed production main:** b6933b772f41b45918f7e25ed1afbbb1fd892272.
- **Integrated reading-edition file:** docs/sections/complex-hessian-equations--local-capacities-and-decreasing-products/index.html, blob 115d285f6b1f76d284463c396e7e87db2b9dbdc3.
- **Primary stable anchors:** Definition 8.11.2, source non-kahler-pluripotential-theory:016F1DC8, permanent FA49D2074193, physical lines 48–61; Lemma 8.11.11, source non-kahler-pluripotential-theory:59C81738, permanent 978D54F1054C4, physical lines 259–279 (permanent-tag display is 978D54F1054C; see clarification below); Theorem 8.11.12, source B227378C, permanent C044CD1C65C4, lines 281–295; Lemma 8.11.13, source 915C1E41, permanent E64937A67BD2, lines 300–318; Theorem 8.11.14, source C3C23711, permanent 945FEE7DBDC5, lines 320–334.
- **Independent context inspected:** Lemma 8.11.1 (source 7121E570, permanent 370C4F1C4AF0, lines 19–46), equation 8.11.3 (source 32422401, permanent A08EAEC63C44, lines 64–71), Proposition 8.11.6 (source 22C64532, permanent 390B1CE08171, lines 146–237), and §8.9.3/§8.9.8 as declared internal dependencies. §8.9 integrated blob 117b866408974cdf706bf305df75e35e1b8affde.
- **Tag clarification:** The correct permanent identifier for Lemma 8.11.11 is 978D54F1054C, with **12** hexadecimal characters. No source tag or published tag is altered.

## Generalized statement

Let \(U\) be a coordinate ball of the printed chapter, \(0\le s\le m\), and \(c_s^*\) the smooth Hessian outer capacity of Definition 8.11.2. Let \((\nu_\alpha)\) be a **net** of real signed Radon measures converging vaguely to a signed Radon measure \(\nu\), i.e. against \(C_c(U)\). Assume that, for every relatively compact open \(V\Subset U\), a constant \(C_V\), independent of \(\alpha\), satisfies

\[
|\nu_\alpha|(E)\le C_V c_s^*(E)
\qquad\text{for every Borel }E\subset V.
\tag{1}
\]

Let \(b_{i,\alpha},b_i:U\to\mathbb R\), \(1\le i\le\ell\), be Borel functions uniformly bounded in absolute value by one common constant. Assume **only the limits** \(b_i\) are locally \(c_s^*\)-quasicontinuous and, for each \(K\Subset U\) and \(\delta>0\),

\[
c_s^*\!\left(K\cap\{|b_{i,\alpha}-b_i|>\delta\}\right)\longrightarrow0
\quad(\alpha\to\infty)
\tag{2}
\]

for each \(i\). There is no monotonicity, continuity or quasicontinuity hypothesis on the approximating \(b_{i,\alpha}\). For every continuous real \(F\) on a compact box containing the ranges,

\[
F(b_{1,\alpha},\ldots,b_{\ell,\alpha})\,\nu_\alpha
\rightharpoonup
F(b_1,\ldots,b_\ell)\,\nu
\quad\text{vaguely}.
\tag{3}
\]

In addition, (1) **automatically holds for \(\nu\)** with the same local constants, and the measures \(\nu_\alpha\) automatically have uniformly bounded variation on each compact set. Thus neither of these two conclusions needs to be assumed separately. The statement remains a theorem for arbitrary directed nets, not just sequences. The uniform constants in (1), rather than an individual constant for each index, are essential.

## Proof

**1. Finite local capacity and uniform variations.**
For \(K\Subset V\Subset U\), the smooth bounded-potential mass estimate from Lemma 8.11.1 gives \(c_s(V)<\infty\). Monotonicity implies

\[
\sup_\alpha|\nu_\alpha|(K)\le C_V c_s^*(K)\le C_V c_s(V)<\infty.
\tag{4}
\]

For any relatively compact open \(G\subset V\), the dual representation of total variation gives

\[
|\nu|(G)
=\sup_{\substack{\psi\in C_c(G)\\|\psi|\le1}}
\left|\int\psi\,d\nu\right|
\le\liminf_\alpha|\nu_\alpha|(G)
\le C_V c_s(G).
\tag{5}
\]

This inequality is valid for nets: for each fixed \(\psi\), its integral converges before taking the supremum. For Borel \(E\subset K\Subset V\), choose an arbitrary open \(O\supset E\) in \(U\) and apply (5) to \(O\cap V\) (or a relatively compact open exhaustion of it). Since \(c_s(O\cap V)\le c_s(O)\), taking the infimum over \(O\) proves

\[
|\nu|(E)\le C_Vc_s^*(E).
\tag{6}
\]

No Portmanteau assertion for signed measures is being assumed; (5) is a consequence of the variational definition of their **total variation**.

**2. A fixed quasicontinuous weight.**
Let \(f=F(b_1,\ldots,b_\ell)\). Finite unions of small exceptional sets and continuity of \(F\) show that \(f\) is locally \(c_s^*\)-quasicontinuous. Fix \(\phi\in C_c(U)\) supported in \(K\Subset V\) and \(M=\sup|F|\). For every \(\varepsilon>0\), find an open \(G\subset U\) with \(c_s(G)<\varepsilon\) and \(f|_{A}\) continuous, \(A=K\setminus G\). The bounded Tietze extension theorem gives a continuous \(g\) on \(U\), \(|g|\le M\), agreeing with \(f\) on \(A\). Because \(\phi g\in C_c(U)\),

\[
\begin{aligned}
\left|\int\phi f\,d(\nu_\alpha-\nu)\right|
&\le \left|\int\phi g\,d(\nu_\alpha-\nu)\right|\\
&\quad+2M\|\phi\|_\infty
\bigl(|\nu_\alpha|(K\cap G)+|\nu|(K\cap G)\bigr).
\end{aligned}
\tag{7}
\]

The first term tends to zero by vague convergence; the second is at most \(4MC_V\|\phi\|_\infty\varepsilon\). Let \(\varepsilon\downarrow0\). Hence \(f\nu_\alpha\rightharpoonup f\nu\).

**3. Capacity convergence removes monotonicity.**
Let \(f_\alpha=F(b_{1,\alpha},\ldots,b_{\ell,\alpha})\). Given \(\eta>0\), uniform continuity of \(F\) on the compact box supplies \(\delta>0\) such that \(\max_i|x_i-y_i|\le\delta\) implies \(|F(x)-F(y)|\le\eta\). On

\[
B_\alpha=K\cap\bigcup_{i=1}^{\ell}
\{|b_{i,\alpha}-b_i|>\delta\},
\]

we bound \(|f_\alpha-f|\le2M\), and on \(K\setminus B_\alpha\) it is at most \(\eta\). By (1), countable subadditivity (only finitely many \(i\) here), and (2),

\[
\begin{aligned}
\left|\int\phi(f_\alpha-f)\,d\nu_\alpha\right|
&\le \|\phi\|_\infty\left[
\eta C_Vc_s(V)+2MC_V\sum_{i=1}^{\ell}
c_s^*\!\left(K\cap\{|b_{i,\alpha}-b_i|>\delta\}\right)
\right]\\
&\longrightarrow \text{a quantity at most }
\eta C_Vc_s(V)\|\phi\|_\infty .
\end{aligned}
\tag{8}
\]

Then \(\eta\downarrow0\), and combine (7)–(8) to obtain (3). At no point is a weak limit of nonlinear Hessian products taken; only the explicitly assumed measure convergence and uniform capacity domination are used.

## Recovery of the printed lemma, and indispensable hypothesis

In printed Lemma 8.11.11, there are finitely many **countable** decreasing families \(b_i^j\downarrow b_i\), all their members and limits locally quasicontinuous. For fixed \(K\) and any \(\varepsilon>0\), select small-capacity open exceptional sets for **every** \(b_i^j\) and \(b_i\), with summable capacity budgets. Outside their open union \(G\), all these functions are continuous on the compact \(K\setminus G\), and the decreasing sequences converge to continuous limits. Dini's theorem gives uniform convergence there. Consequently, for every \(\delta>0\), the bad set in (2) is eventually contained in \(G\); its outer capacity is smaller than \(\varepsilon\). This proves (2) and recovers the printed conclusion, while weakening it in the nonmonotone case.

By contrast, capacity domination **cannot simply be removed**. In a coordinate ball take \(s=0\), so \(c_0^*\) is smooth volume outer measure. Choose \(x_j\ne x_0\) with \(x_j\to x_0\), set \(\nu_j=\delta_{x_j}\), \(\nu=\delta_{x_0}\), and \(b_j=b=\mathbf1_{\{x_0\}}\). This bounded Borel limit is volume-quasicontinuous (remove an arbitrarily small open ball around \(x_0\)), and the capacity discrepancy \(c_0^*(\{|b_j-b|>\delta\}\cap K)\) is identically zero. Nevertheless, \(b_j\nu_j=0\) whereas \(b\nu=\delta_{x_0}\). The moving Dirac masses do not satisfy (1). This is **not** a counterexample to the printed lemma.

## Proposed optional replacement and dependent results

An optional separate strengthening of Lemma 8.11.11 may state (1)–(3), with the original monotone statement preserved as a corollary. It should **not** silently replace its stated hypotheses in source/registry or claim unconditional weighted convergence of arbitrary weak measures. Theorem 8.11.12 uses the monotone special case at physical lines 285–290, and Theorem 8.11.14 uses it for \(Q_p\) at lines 328–332. Under an independently proved capacity convergence of their weights, the more general deduction applies; the analytic local capacity estimates and construction of \(D_p,Q_p\) remain **conditional internal inputs**, not certified by this result.

**Coverage:** New exact proof-level scrutiny of Definition 8.11.2, Lemma 8.11.11 and its uses in Theorems 8.11.12/14, plus supporting finite local mass from Lemma 8.11.1 and §8.9.8. Previously partly sampled §8.11; **zero** newly first-visited numbered sections and **zero** entire-section/theorem-chain certifications. Actual existing ToC matrix is 25 chapters and 747 numbered sections. No build, test suite, CI, website publication or production edit was performed. The user-excluded Demailly regularization/approximation and dedicated Bergman, \(L^2\), Ohsawa–Takegoshi, multiscale-atlas and positivity-loss programme remains **deferred-by-user**, not resolved.