# Uniform-density perturbations: joint current-and-determinant-measure stability for Gauduchon maximizers

**Date:** 2026-11-13 (Asia/Shanghai). **Reviewed production main:** b6933b772f41b45918f7e25ed1afbbb1fd892272.  
**Finding:** POME-GAUD-DET-JOINT-DENSITY-GRAPH-NET-001.  
**Severity:** low. **Status:** verified conditional deduction; no printed theorem is refuted and no missing proof is being represented as a false statement.  
**Boundary:** The Demailly approximation/regularization and dedicated Bergman, L2, Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof-completion programme is **deferred-by-user**, not checked or certified here.

## Exact integrated reading-edition anchors

1. Section 12.7, *A compact dual problem over Gauduchon currents*: docs/sections/a-gauduchon-variational-volume--a-compact-dual-problem-over-gauduchon-currents/index.html, Git blob **1c0f7efb92914b8a55754bd5039d7319392fb03b**. The coefficient-matrix normalization and determinant measure, Equation 12.7.1, source non-kahler-pluripotential-theory:919BAA56, permanent tag **A99038CD10B4**, physical lines **13–35**. Lemma 12.7.2, source non-kahler-pluripotential-theory:EF340E54, tag **FB6C2382E066**, physical lines **39–69**. Theorem 12.7.3, source non-kahler-pluripotential-theory:B931D275, tag **0537569F9F52**, physical lines **74–105**. The section anchor is source non-kahler-pluripotential-theory:3314ED2C, permanent **54ADA5D399DA**, lines **5–12**.
2. Section 12.8, *Supporting probabilities represented by maximizing currents*: docs/sections/a-gauduchon-variational-volume--supporting-probabilities-represented-by-maximizing-currents/index.html, Git blob **ed1ad2bf6220cd086a44d7ee92ca7779666288d9**. Lemma 12.8.1, source non-kahler-pluripotential-theory:E1B004B5, tag **47843166E777**, physical lines **20–44**. Theorem 12.8.2, source non-kahler-pluripotential-theory:3606F8FD, tag **E9E119AAA269**, lines **46–98**. Section source non-kahler-pluripotential-theory:0A067F39, permanent **7C2BB0FDDDF5**, lines **5–17**.
3. Section 12.15, *Varying the probability measure*: docs/sections/a-gauduchon-variational-volume--varying-the-probability-measure/index.html, blob **440964738faf623f2e0942bbc7fd21d5f2a3ed69**, Proposition 12.15.1 (source non-kahler-pluripotential-theory:408236E7, permanent **37E6FFC01EDB**), inspected only as a distinct fixed-density quotient comparison. This is **not** a claim to review all of 12.15.

Original historical attribution and permanent tags are left untouched. All anchors identify the currently integrated reading edition; no source theorem number was used as a substitute for a content match.

## Exact conditional proposition

Retain the standing hypotheses of Section 12.7: a connected compact complex manifold X with complex dimension n at least two, a fixed Hermitian background form omega, a smooth positive probability volume form dV, and the compact convex space of normalized positive dd^c-closed (n-1,n-1)-currents

\[
\mathscr G_\omega=\{T\geq0:dd^cT=0,\ \int_X\omega\wedge T=1\}.
\]

For real continuous F define the determinant measure and its maximal mass by the printed formulas

\[
\Gamma_F(T)=f_F(\det P_T)^{1/n}\sigma_T,\quad
f_F=(e^F dV/\omega^n)^{1/n},\quad
\sigma_T=\omega\wedge T,\quad
\operatorname{tr}P_T=n,
\]
\[
\mathfrak D_F(T)=\Gamma_F(T)(X),\quad
M(F)=\max_{T\in\mathscr G_\omega}\mathfrak D_F(T)>0,\quad
\mathscr M(F)=\operatorname*{argmax}\mathfrak D_F.
\]

**Proposition (joint stability for arbitrary directed nets).**
Let \((F_i)_{i\in I}\) be **any directed net** of continuous real functions with \(\delta_i:=\|F_i-F\|_\infty\to0\), and choose *arbitrarily* \(T_i\in\mathscr M(F_i)\). Then:

1. For any F,G and \(\delta=\|G-F\|_\infty\),
   \[
   e^{-\delta/n}M(F)\leq M(G)\leq e^{\delta/n}M(F),\qquad
   |B_0(G)-B_0(F)|\leq\delta
   \]
   where \(B_0(F)=-n\log M(F)\). Also \(M(F+c)=e^{c/n}M(F)\) and \(B_0(F+c)=B_0(F)-c\).
2. The varying maximizers are *asymptotically maximizing for the fixed density F*:
   \[
   e^{-2\delta_i/n}M(F)\leq \mathfrak D_F(T_i)\leq M(F).
   \]
   In addition, with the **signed-measure variation norm** (not half the probability total-variation distance),
   \[
   \|\Gamma_{F_i}(T_i)-\Gamma_F(T_i)\|_{\mathrm{TV}}
      \leq(e^{\delta_i/n}-1)\mathfrak D_F(T_i)\longrightarrow0.
   \]
   This is a bound between the two determinant measures **at the same current \(T_i\)**, not a total-variation convergence assertion at the limiting current.
3. For **each** weakly convergent subnet \(T_{i_j}\rightharpoonup T\), the limit is in \(\mathscr M(F)\), and **jointly**
   \[
   \Gamma_{F_{i_j}}(T_{i_j})\rightharpoonup\Gamma_F(T),
   \qquad
   \frac{\Gamma_{F_{i_j}}(T_{i_j})}{M(F_{i_j})}
     \rightharpoonup\frac{\Gamma_F(T)}{M(F)} .
   \]
   The convergence of finite measures is weak convergence against continuous test functions on compact X.
4. The set-valued map \(F\mapsto\{(T,\Gamma_F(T)/M(F)):T\in\mathscr M(F)\}\) has a **closed graph** and is upper hemicontinuous in the weak current/probability topologies under uniform perturbations of F. If \(\mathscr M(F)\) is a singleton, the **entire original net** of maximizing currents converges to it. If only all maximizing currents at F have the same normalized determinant measure, the entire net of normalized determinant measures converges to that single probability even if the currents do not converge.

No claim of lower hemicontinuity, uniqueness of a maximizing current at nonsmooth F, or total-variation convergence to \(\Gamma_F(T)\) is made.

## Proof with full limiting details

For the same fixed current T, Equation 12.7.1 gives the *identity of positive finite measures*
\[
\Gamma_G(T)=e^{(G-F)/n}\Gamma_F(T).
\tag{1}
\]
If \(\delta=\|G-F\|_\infty\), then integration of the elementary bounds \(e^{-\delta/n}\leq e^{(G-F)/n}\leq e^{\delta/n}\) yields
\[
e^{-\delta/n}\mathfrak D_F(T)\leq\mathfrak D_G(T)
 \leq e^{\delta/n}\mathfrak D_F(T)
\]
**uniformly in T**. Taking maxima over the same compact \(\mathscr G_\omega\) gives assertion 1. The constant translation follows directly from (1); taking logarithms and invoking Theorem 12.7.3 yields the bound on \(B_0\).

For assertion 2, use \(\mathfrak D_{F_i}(T_i)=M(F_i)\) and both comparisons:
\[
\mathfrak D_F(T_i)\geq e^{-\delta_i/n}M(F_i)
                \geq e^{-2\delta_i/n}M(F).
\]
The upper bound is the definition of \(M(F)\), so its mass converges along the **net**. Equation (1) also implies
\[
\|\Gamma_{F_i}(T_i)-\Gamma_F(T_i)\|_{\mathrm{TV}}
 =\int_X|e^{(F_i-F)/n}-1|\,d\Gamma_F(T_i)
 \leq(e^{\delta_i/n}-1)\mathfrak D_F(T_i).
\]
There is no exchange of weak current limits with a nonlinear determinant here; this estimate compares densities before taking a limit.

Fix an arbitrary weakly convergent subnet \(T_{i_j}\to T\). Lemma 12.7.2 identifies \(\mathfrak D_F\) as an infimum of continuous linear functionals; in particular it is **upper semicontinuous**. Hence
\[
\mathfrak D_F(T)\geq\limsup_j\mathfrak D_F(T_{i_j})=M(F).
\]
The opposite bound is tautological, proving \(T\in\mathscr M(F)\).

To prove the nonlinear determinant-measure continuity without invoking any false continuity of determinant under weak measure limits, let \(h\in C(X,\mathbb R)\). Choose \(\varepsilon>0\) with \(1\pm\varepsilon h>0\) everywhere and set \(G_\pm=F+n\log(1\pm\varepsilon h)\). Formula (1) gives
\[
\mathfrak D_{G_\pm}(T_{i_j})
 =\int_X(1\pm\varepsilon h)\,d\Gamma_F(T_{i_j}).
\]
Upper semicontinuity at T, for each fixed continuous \(G_\pm\), yields
\[
\limsup_j\int_X(1\pm\varepsilon h)\,d\Gamma_F(T_{i_j})
 \leq\int_X(1\pm\varepsilon h)\,d\Gamma_F(T).
\tag{2}
\]
The unweighted masses on both sides converge to the common value \(M(F)\). Subtracting those masses in (2), the **plus** inequality gives the upper bound for the integrals against h; the **minus** inequality gives the lower bound. Therefore
\[
\int_Xh\,d\Gamma_F(T_{i_j})\to\int_Xh\,d\Gamma_F(T).
\]
This is valid for arbitrary convergent subnets, with no sequential compactness assumption. Assertion 2's stronger *same-current* variation estimate now permits replacing the left measure by \(\Gamma_{F_{i_j}}(T_{i_j})\); assertion 1 gives \(M(F_{i_j})\to M(F)>0\), so the normalized measures converge as stated.

For the final graph assertion, compactness of \(\mathscr G_\omega\) supplies convergent **subnets** of any net of \(T_i\), and the previous paragraph identifies all possible joint limits. The graph is closed, with values compact by Theorem 12.7.3 and Lemma 12.8.1. Upper hemicontinuity follows from the closed graph with compact current range and the compact space of probabilities on compact X. In the singleton-current case, a net not converging to the unique limit would have a subnet outside an open neighborhood and then a further convergent subnet, contradicting the joint cluster classification. The same argument applied to normalized determinant measures proves the final assertion when their limiting value, but not necessarily their representing current, is unique.

Theorem 12.8.2 identifies the normalized determinant measures of maximizing currents with the supporting probabilities \(\mathcal A_0(F)\) as a **conditional internal input**. The new result therefore also gives a lift of uniform-density support stability to actual maximizing Gauduchon currents. It does not re-prove the theorem's use of the adjoint scalar or absolute-continuity theory.

## Classification, dependence and disposition

**POME-GAUD-DET-JOINT-DENSITY-GRAPH-NET-001:** **low / verified conditional deduction**. The printed Lemma 12.7.2, Theorem 12.7.3, Lemma 12.8.1 and Theorem 12.8.2 are **not** contradicted. The present proof checks the crucial two-sign determinant-measure limiting step and extends the printed **sequential** Lemma 12.8.1 to genuinely arbitrary directed nets under **varying continuous** densities.

**Conditional internal inputs:** compactness of normalized Gauduchon-current set (§11.7), the matrix-density variational identity and upper semicontinuity (Lemma 12.7.2), existence/positivity of the maximum (Theorem 12.7.3), and (only for identification with the abstract supergradient face) Theorem 12.8.2. The deeper smooth Monge–Ampère equation, §11.33 scalar theory and §11.34 probability absolute-continuity chain are **not** transitively certified. No Demailly approximation or dedicated excluded programme is inspected.

**Nonduplication:** The 2026-11-02 bounded-L1 support stability report concerns abstract §11.33–11.35 supporting probabilities and weak-L1 density limits; it does **not** prove a joint limit of maximizing Gauduchon currents and their nonlinear determinant measures. The 2026-10-24 §12.34 report inspected §12.7.1–2 only for coefficient normalization. Section 12.15.1 compares smooth probability measures in a different variational quotient and is not this joint graph statement.

**Proposed correction/addendum:** optionally insert a corollary after Lemma 12.8.1 (or after Theorem 12.8.2) stating the exact uniform-perturbation, net, and measure-topology qualifications above. This is an *additive proposed change*, not a correction to a false original theorem. Preserve existing source labels, history, and permanent tags. Potential dependents: continuous-density scalar sensitivity (§12.7.3), support/current representation (§12.8.2), and the varying-reference-measure discussion (§12.15); no downstream result is declared certified.

**Actual coverage:** substantive proof-level reinspection of the determinant variation and semicontinuity in §12.7.1–3 and the two-sign lemma and support identification in §12.8.1–2, plus a **statement-only** scope crosscheck at §12.15.1. Section 12.7 had previously been touched for coefficient normalization, but this proof-level content is new. Historical first-visit credits remain conservatively **+0** pending reconciliation; **+0 entire-section certifications**. The current table of contents continues to have **25 chapters and 747 numbered sections**. No source/body, registry, canonicalization, tags, build, test suite, CI, or publication change is made.
