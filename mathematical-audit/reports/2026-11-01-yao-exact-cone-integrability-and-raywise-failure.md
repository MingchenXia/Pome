# 2026-11-01: Exact maximal-cone criterion for toric multiplier-ideal characters

**Reviewed production main:** b6933b772f41b45918f7e25ed1afbbb1fd892272 (unchanged). **Status:** low / **verified conditional deduction**. This is neither a false theorem nor a claim that the full toric metric/envelope construction has been verified. It is distinct from the historically logged POME-TOR-YAO-EDGE-001: that older item noticed the non-strict endpoint in one direction; the present finding proves a global necessary-and-sufficient local integrability criterion and gives an explicit failure of tests restricted to individual fan rays. No source/registry/permanent-tag edit is proposed as part of this audit commit.

## Primary integrated reading-edition anchors

- Main file: docs/sections/toric-pluripotential-theory-on-ample-line-bundles/index.html, **Git blob 56a1a55dfc8185aee0e6d495a6a93d8a2313d76b**.
- Theorem **21.12.31** (Yao): source label **sgpt:59CD0BEC**, permanent tag **E109952155FB**, lines **600–694**; part (2), source clause 0772D430, lines 606–614; the local chart/integrability reduction, lines **633–672**; the original tube argument, lines **675–693**.
- Newton body Definition **21.12.27**, source label **sgpt:CC64AE504A19**, permanent tag **CC64AE504A19**, lines **535–544** (the source label and permanent tag must be checked separately before any patch; this report relies on the displayed definition, not on their equality). Model-envelope Proposition **21.12.29**, source label **sgpt:11748980D2DF**, permanent **11748980D2DF**, lines **563–593**, is a **conditional input**.
- Corollary **21.12.35**, permanent tag **05A4124B7E31**, lines **699–813**, was checked specifically at its uniform lattice-neighborhood argument (lines 756–809), **not certified** in full.
- Toric charts and squared-logarithm convention: §21.12.1, permanent tag **DD9C13434AA7**, lines **26–112**. Theorem 21.9.5 (character sections), Proposition 21.12.24 (toric real MA identity), and Proposition 16.6.18 (preservation of multiplier ideals under taking the model envelope) remain dependencies, not newly verified proof chains.

**Convention:** \(\nu_i=\log|z_i|^2\), \(dd^c=i\partial\bar\partial/(2\pi)\), and the toric support function is \(h_\Delta(v)=\max_{a\in\Delta}\langle a,v\rangle\). Let \(P\) be the smooth full-dimensional lattice polytope and \(\Delta=\Delta(\omega,\varphi)\subset P\) a nonempty compact convex Newton body for a nontrivial toric \(\omega\)-PSH metric. Work under the model reduction quoted at the start of the printed Theorem 21.12.31: replacing \(\varphi\) by \(P_\omega[\varphi]\) preserves both its multiplier ideal and \(\Delta\), and \(F_\varphi-h_\Delta\) is bounded. The present argument does not reprove that reduction or use any excluded Demailly regularization/L²/Bergman programme.

## Exact criterion

For a maximal cone \(\tau\) of the smooth complete normal fan \(\Sigma\), let \(u_{\tau,1},\ldots,u_{\tau,n}\) be its primitive ray generators, a lattice basis. For each \(m\in P\cap M\), define
\[
H_m(v)=\langle m,v\rangle-h_\Delta(v),\qquad
A_\tau(m)=\max_{\substack{c_i\ge0\\\sum_i c_i=1}}
H_m\left(-\sum_i c_i u_{\tau,i}\right).
\]
The maxima are attained: \(H_m\) is continuous, positively homogeneous and Lipschitz (compact \(\Delta\)), and the coefficient simplex is compact. The **exact character criterion** is
\[
\boxed{\quad
\chi^m\in H^0(X,L\otimes\mathcal I(\varphi))
\quad\Longleftrightarrow\quad
A_\tau(m)<1\text{ for every maximal }\tau\in\Sigma.
\quad}
\]
For \(m\notin P\cap M\), \(\chi^m\) is not a global section at all; the displayed equivalence is deliberately restricted to \(m\in P\cap M\). The criterion covers lower-dimensional \(\Delta\) and all simplex faces, without any unproved full-dimensional-interior assumption.

**Proof, both directions.** The maximal affine charts cover \(X\), and near the fixed point of a maximal cone \(\tau\) the section has squared local norm comparable, after replacing by the model metric, to \(\exp H_m(\nu)\). In polar logarithmic coordinates \(t_i=-\log|z_i|^2\ge0\), the ordinary local multiplier-ideal integral is finite exactly when
\[
I_\tau(m)=
\int_{\mathbb R_{\ge0}^n}
\exp\left(H_m\left(-\sum_i t_i u_{\tau,i}\right)-\sum_i t_i\right)\,dt
<\infty .
\]
This is precisely the chart computation in the printed proof (lines 655–672), with bounded multiplicative comparisons. If \(A_\tau(m)<1\), compactness supplies \(\delta_\tau=1-A_\tau(m)>0\). Writing \(s=\sum_i t_i\) and \(c_i=t_i/s\) for \(s>0\), homogeneity gives an exponent at most \(-\delta_\tau s\), so \(I_\tau(m)\le\delta_\tau^{-n}<\infty\).

Conversely choose a maximizing \(c\) with \(A_\tau(m)\ge1\), and write \(J=\{i:c_i>0\}\), a nonempty set; take \(i_0\in J\). In the positive orthant use the tube
\(t_{i_0}=c_{i_0}s\), \(t_i=c_i s+y_i\) for \(i\ne i_0\), with \(s>1\) and all \(0<y_i<1\), including indices with \(c_i=0\). The Jacobian is \(c_{i_0}>0\), and Lipschitz continuity of \(H_m\) gives, uniformly in the bounded \(y\)'s,
\[
H_m\left(-\sum_i t_i u_{\tau,i}\right)-\sum_i t_i
=s(A_\tau(m)-1)+O(1).
\]
Consequently \(I_\tau(m)\) dominates a positive constant times
\(\int_1^\infty e^{s(A_\tau(m)-1)}\,ds=\infty\).
The argument works when the maximizer lies on **any face** of the simplex (including a single ray) and at the **critical equality** \(A_\tau(m)=1\). Since the maximal charts are finite in number, their local integrability is equivalent to global membership. This proves both implications.

## Exact failure of a ray-only test, even when all fan rays pass

Take \(X=\mathbb P^1\times\mathbb P^1\), \(L=\mathcal O(2,2)\), \(P=[0,2]^2\), \(m=(0,0)\), and
\[
\Delta=\operatorname{conv}\{(2,0),(0,2)\},\quad
F_\varphi(\nu_1,\nu_2)=\log(e^{2\nu_1}+e^{2\nu_2}).
\]
This is a global toric semipositive singular metric on \(L\), represented by the two torus character sections with exponents \((2,0),(0,2)\); its convex logarithmic sum differs from \(h_\Delta\) by a bounded function, so its Newton body is exactly \(\Delta\).

For all **four primitive rays** \(u\in\{e_1,e_2,-e_1,-e_2\}\) in the square's normal fan, one has \(H_m(-u)\in\{0,-2\}<1\). Yet at the positive-cone midpoint \(u=(e_1+e_2)/2\),
\[
H_m(-u)=1.
\]
In the affine chart at the origin the local metric weight is \(\log(|z_1|^4+|z_2|^4)\), modulo a smooth term, and the local representative of \(\chi^m\) is the constant \(1\). Its multiplier-ideal integral diverges:
\[
\int_{|z_i|<\varepsilon}\frac{dA(z_1)\,dA(z_2)}
{|z_1|^4+|z_2|^4}
=\pi^2\int_0^{\varepsilon^2}\int_0^{\varepsilon^2}
\frac{dx\,dy}{x^2+y^2}=\infty .
\]
For instance, restrict the last integral to \(0<x<\varepsilon^2/2\) and \(x<y<2x\); the result is bounded below by a fixed positive multiple of \(\int dx/x\). Therefore \(\chi^0\notin H^0(X,L\otimes\mathcal I(\varphi))\), although every **single-ray** \(H_m(-u)\) test passes strictly. This proves the **full coefficient simplex cannot be replaced by its vertices**. It is a counterexample to a tempting but unprinted shortcut, not to Theorem 21.12.31.

## Disposition, dependencies and coverage

**Severity low; status verified conditional deduction.** The original two implications of Yao's theorem remain correct. The stronger exact maximal-cone criterion can be offered as an optional corollary immediately after Theorem 21.12.31, retaining Yi Yao's attribution, both existing clauses and every permanent tag. The fact that the printed strict \(>1\) condition can be sharpened to \(\ge1\) was already recorded as **POME-TOR-YAO-EDGE-001** and is **not** counted as a new independent finding here. The new parts are the simultaneous **if and only if** across all maximal charts, the face-uniform proof, and the explicit **all-fan-rays-pass but character fails** example. Potential dependent usage: character-space localization in Corollary 21.12.35, comparison with Newton bodies and multiplier ideal sections in §§21.12–21.13, and toric lattice asymptotics. No downstream theorem was shown false.

**Actual selected scope:** detailed reading of §21.12.31 including the local model, both inequalities, all cone faces; §21.12.29 model formula and §21.12.35 lattice-neighborhood proof only as conditional/contextual checks. Independently opened the **previously unreviewed** §6.42 at docs/sections/lelong-densities-generalized-masses-and-multiplicity--multiplicities-and-lelong-numbers-under-holomorphic-maps/index.html, main blob **6277ee1be4d5cc08777aca6c82e9663518be6961**, source **demailly-complex-geometry:2E584F85**, permanent section tag **1A00687E6A1B**, physical line **7**: the actual page contains only a conventions/provenance paragraph and no numbered theorem or proof. This is a **navigation/definition-only inspection**, not mathematical certification or an audit of the excluded approximation programme. Neighboring §§6.43, 7.28 and 7.31 are not reaudited.

**Overall inventory:** 25 chapters, 747 numbered ToC sections in the previously established current-main matrix; **zero fully mathematically certified sections**. All existing open findings and user-deferred Demailly approximation/regularization plus its dedicated Bergman, L², OT, multiscale-atlas and positivity-loss proof-completion work stay **deferred-by-user**. No source code, production main, permanent tags, CI, publication, formalization or website files touched; no project test/build asserted.
