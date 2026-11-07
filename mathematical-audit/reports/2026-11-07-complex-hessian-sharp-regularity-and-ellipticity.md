# Smooth admissible approximation with bounded complex Hessian but no real C1,1 limit; two necessary ellipticity bounds

**Review date:** 2026-11-07. **Production main:** b6933b772f41b45918f7e25ed1afbbb1fd892272.

**Finding IDs:** POME-HESS-LOG-SINGULAR-C11-OBSTRUCTION-001 and POME-HESS-TWO-ELLIPTICITY-BOUNDS-SHARP-001. Both are **low / verified conditional deduction** (explicit elementary countermodels to tempting *strengthenings*, not counterexamples to printed results). The elementary calculations themselves are unconditional; the label reflects that the surrounding Pome analytic proof chain is not certified.

## Exact current reading-edition anchors

- **Global analytic range:** docs/sections/complex-hessian-equations/index.html, blob 5331b937ccdaba51f1ec006d5e72dc84f7addfbf, §8.1 physical line 7, section permanent tag CFD38285654D. Here 2 <= m < n.
- **Main regularity claim:** docs/sections/complex-hessian-equations--bounded-complex-hessians-and-elliptic-extensions/index.html, blob fdd9225b1d778e1debaf94f75ef65175d4bd4484. Lemma 8.5.1 source non-kahler-pluripotential-theory:835B5652, permanent tag 89771FD1FD15, physical lines 10–27, especially hypotheses 11–15 and explicit reservation at 27 that a bounded full real Hessian is **not** asserted.
- **Main ellipticity claim:** same HTML / blob. Lemma 8.5.3 source non-kahler-pluripotential-theory:B1F0AA6B, permanent tag BAC60298D0F2, physical lines 62–98, in particular its *joint* lower normalized Hessian-root and upper trace constraints (65–69), derivative bounds (93), and concave tangent-envelope construction (73–98). Its real extension and ellipticity constants appear at lines 102–110.
- **Derivative conventions:** docs/sections/complex-hessian-equations--the-admissible-cone/index.html, blob 925e6109ab7d800cde9bec4b0487842b2e6877a8. Lemma 8.2.5 source non-kahler-pluripotential-theory:53FFB5F3, permanent tag 7710D01DF6F5, physical lines 104–130; normalized root F=(S_m / binom(n,m))^(1/m).

These are selected theorem/proof anchors; no claim of complete §8.5, Evans–Krylov–Caffarelli, or global analytic-equation verification.

## A. A uniformly strictly admissible sequence without C1,1 compactness

Let X = (C/(Z+iZ))^n with n >= 3 and its flat Kähler form omega. Fix a small coordinate polydisk, write z_1=x+iy and r=(x^2+y^2)^(1/2), and define
\[
h(x,y)=
\begin{cases}
(x^2-y^2)\log r,&r>0,\\
0,&r=0.
\end{cases}
\]
Take a real smooth cutoff chi supported in that polydisk, equal to one near the origin, and extend H(z)=chi(z)h(z_1) by zero to X.

**Distributional derivative computation.** Away from r=0, Q=x^2-y^2 is harmonic and
\[
\Delta_{\mathbb R^2}(Q\log r)
=2\nabla Q\cdot \nabla\log r=\frac{4Q}{r^2}=4\cos(2\theta).
\]
The right-hand side is bounded. This equality also holds in distributions **without an extra delta mass**: h=O(r^2|\log r|), \(\nabla h=O(r(1+|\log r|))\), and both boundary terms in integration by parts on the circle of radius r tend to zero. Thus \(\partial_{z_1}\partial_{\bar z_1}h=Q/r^2\) almost everywhere, with magnitude at most one. The first derivatives of h are bounded and tend to zero on r=0. The product rule with the fixed cutoff shows that **every coefficient** of \(\partial\bar\partial H\) on X is in L-infinity: terms involving derivatives of chi use only bounded H and bounded first derivatives of h. The complex Hessian has an essentially bounded representative globally.

Let \(\rho_\varepsilon\) be any nonnegative smooth periodic approximate identity on the flat torus; set \(H_\varepsilon=H*\rho_\varepsilon\). Then \(H_\varepsilon\) is globally smooth and converges uniformly to H. Distributional differentiation commutes with periodic convolution, so
\[
\sup_{\varepsilon>0}\|dd^cH_\varepsilon\|_{L^\infty}
\le C\|dd^cH\|_{L^\infty}<\infty,
\qquad
\sup_\varepsilon \|H_\varepsilon\|_\infty\le\|H\|_\infty.
\]
The bound on the Hermitian operator norm holds in the fixed flat frame. Choose a constant a>0 so small that
\[
\omega+dd^c(aH_\varepsilon)\ \ge\ \tfrac12\omega
\]
for every epsilon. Hence \(u_\varepsilon=aH_\varepsilon\) satisfies **even the uniform strictly positive Kähler (and thus m-admissible) lower bound**, as well as all hypotheses of Lemma 8.5.1.

Nevertheless \(u=aH\notin C^{1,1}(X)\). Indeed chi=1 on the x-axis near zero and
\[
\partial_x u(x,0)=a(2x\log|x|+x),\qquad \partial_xu(0,0)=0.
\]
The quotient \(\big|\partial_xu(x,0)-\partial_xu(0,0)\big|/|x|
=a|2\log|x|+1|\) diverges. The Hessian has a logarithmically divergent real component, even though the complex trace is bounded. On the other hand h is C^1 and \(D^2h=O(1+|\log r|)\) off r=0; it belongs to \(C^{1,\alpha}\) for every alpha<1 and has locally finite W^{2,p} norm for every finite p. This exactly matches, and shows the endpoint sharpness of, the printed conclusion.

**Interpretation:** it is invalid to infer uniform C1,1 control from uniform L-infinity control of \(dd^cu_\varepsilon\), even after adding uniform strict m-admissibility and uniform convergence. The printed Lemma 8.5.1 **does not** make that inference. Local mollification here is elementary convolution of a bounded-coefficient distribution, **not** Demailly regularization.

## B. Both hypotheses in the matrix compactness lemma are individually essential

Here take n=3, m=2 (within §8.1), and put
\[
F(A)=\sqrt{S_2(A)/3},\qquad
F_i(A)=\frac{S_1(\lambda|i)}{2\sqrt{3S_2(A)}}.
\]
First, for t>=1 define \(A_t=\operatorname{diag}(t,t^{-1},0)\). These matrices lie in the **open** cone Gamma_2, have \(S_2(A_t)=1\), hence \(F(A_t)=1/\sqrt3\), but \(\operatorname{tr}A_t=t+t^{-1}\to\infty\). Their full derivative spectrum is
\[
DF(A_t)=\frac1{2\sqrt3}\operatorname{diag}
(t^{-1},t,t+t^{-1}).
\]
Therefore, a fixed positive lower bound on \(\sigma_2\) **alone** supplies neither a positive uniform lower ellipticity constant nor a finite uniform upper constant.

Second, for 0<epsilon<=1 let \(B_\varepsilon=\operatorname{diag}(1,\varepsilon,0)\). They are in Gamma_2 and satisfy \(\operatorname{tr}B_\varepsilon\le2\), but \(S_2(B_\varepsilon)=\varepsilon\to0\). Now
\[
DF(B_\varepsilon)=\frac1{2\sqrt{3}}\operatorname{diag}
(\sqrt\varepsilon,\varepsilon^{-1/2},(1+\varepsilon)\varepsilon^{-1/2}).
\]
Thus an upper trace bound **alone** also yields neither kind of uniform derivative bound. Neither example belongs to **one fixed** nonempty K of Lemma 8.5.3 with *both* \(\operatorname{tr}\le L\) and \(\sigma_2\ge f_0^2>0\). The lemma and its infimum-of-tangent-planes extension remain correct.

These examples test the **necessity of both compactness restrictions**, not the optimal numerical coefficient in Lemma 8.2.5. In particular, they neither replace nor duplicate the 2026-10-31 finding POME-HESS-SHARP-DIAGONAL-DERIVATIVE-001 concerning a sharper coordinatewise lower coefficient on a fixed cone.

## Status, dependents, and limitations

1. POME-HESS-LOG-SINGULAR-C11-OBSTRUCTION-001 — severity **low**, status **verified conditional deduction**; no false printed statement. Complete local/global construction above. Proposal: add a warning/example after §8.5.1 only in a separately reviewed content PR, retaining source attribution and tags. **Dependents:** regularity/elliptic compactness arguments in §8.5 and later §8.6–8.8 cannot silently upgrade W^{2,p}/C^{1,alpha} to C1,1 before further PDE estimates.
2. POME-HESS-TWO-ELLIPTICITY-BOUNDS-SHARP-001 — severity **low**, status **verified conditional deduction**; no false printed statement. Exact matrix computations above. Proposal: add a sharpness remark to §8.5.3 only through a separately reviewed proposal. **Dependents:** the uniform elliptic extension in §8.5.4 and the later Evans–Krylov application require both positive lower Hessian-root and bounded trace to stay on one K; neither may be dropped.
3. **Unresolved/external inputs not repaired:** the cited interior Evans–Krylov–Caffarelli estimate, global smooth solution/a priori results, and full convergence/viscosity chains of §§8.5–8.8 have not been independently certified. No new circularity or mathematical duplication identified. These concrete sharpness countermodels are not proof substitutes for those theorems.
4. **Deferred-by-user:** Demailly approximation/regularization and dedicated Bergman, weighted L2, Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof-completion work stay deferred, not resolved or certified. They were not audited.

**Actual coverage:** only the specified §8.5.1 and §8.5.3 hypotheses/conclusions, §8.2.5 derivative normalization and §8.1 standing dimension as context. The main-ToC inventory is **25 chapters / 747 numbered sections / zero complete mathematical-section certifications**. §8.5 and §8.2 were **already partly sampled**: zero new first visits, and no whole-section proof chain is certified. There was no build, CI, browser verification, source/registry/canonicalization edit, or publication.
