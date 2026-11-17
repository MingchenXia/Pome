# Chapter 8: the \(m=1\) endpoint of the trace-to-gradient estimate

**Date:** 2026-11-17  
**Stable finding:** \`POME-HESS-M1-GRADIENT-ELLIPTIC-ENDPOINT-001\`  
**Severity/status:** low / **verified conditional deduction**, with an explicit sharpness example for a *weakened* hypothesis; **no error in the printed proposition**.  
**Reviewed production main:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`  
**Integrated reading edition:** \`docs/sections/complex-hessian-equations--liouville-and-gradient-estimates/index.html\`  
**Integrated HTML blob:** \`74cda06ad4bf75ab5fcba6e841c9ad4aa9424981\`  
**Exact anchor:** Proposition **8.3.3**, physical lines **109–117** (statement), **122–129** (why the printed \(m\ge2\) argument uses \(S_2\)), and **131–151** (blow-up and elliptic estimates); permanent tag **B863BB49A505**; source **non-kahler-pluripotential-theory:hessian:hessian-trace-to-gradient** (source tag **A456C079**, revision \`9d4f324ca55f5db30f60825aba5733ecd24a42b5\`). Earlier Lemma 8.2.5, tag **7710D01DF6F5**, is only a *comparison*, not an invoked input.

## What is and is not claimed

Proposition 8.3.3 states a gradient estimate for \(2\le m\le n\), assuming a fixed compact Hermitian background, a uniform \(C^0\) bound, an upper bound for the \(m\)-Hessian density, and an auxiliary trace bound \(A(1+\sup|\partial u|^2)\). Its proof explicitly uses \(S_2>0\) to control every eigenvalue by the trace. That eigenvalue step is not available for \(m=1\), as independently demonstrated by the already recorded error in the *different* Lemma 8.2.5. **Nevertheless the conclusion of Proposition 8.3.3 extends to \(m=1\) by a different argument, and its auxiliary trace bound is unnecessary at this endpoint.**

This note verifies that additional claim conditional on the same standard fixed-operator interior \(W^{2,p}\) elliptic estimate already used at physical line 138 of the printed proof. It does **not** certify that elliptic estimate's full internal dependency chain or the printed \(m\ge2\) nonlinear Liouville argument.

## Endpoint theorem and proof

Let \(X\) be any compact complex manifold of dimension \(n\ge1\), \(\omega\) a fixed smooth Hermitian metric, and \(\theta\) a fixed smooth real \((1,1)\)-form. For fixed \(M,B>0\), consider all real \(u\in C^\infty(X)\) with
\[
 |u|\le M,\qquad \theta+dd^cu\in\Gamma_1(\omega),\qquad
 \frac{(\theta+dd^cu)\wedge\omega^{n-1}}{\omega^n}\le B.
\]
There is a constant \(C=C(X,\omega,\theta,M,B)\) such that
\[
  \sup_X|\partial u|_\omega\le C.
\]
**No extra estimate of the form**
\(\operatorname{tr}_\omega(\theta+dd^cu)\le A(1+\sup|\partial u|_\omega^2)\)
**is needed.**

Indeed put \(q=\operatorname{tr}_\omega(\theta+dd^cu)\) and
\(\Delta_\omega u=\operatorname{tr}_\omega(dd^cu)\). The elementary wedge/trace identity gives
\[
 \frac{(\theta+dd^cu)\wedge\omega^{n-1}}{\omega^n}=\frac{q}{n}.
\]
The defining first-cone inequality is \(q>0\). Therefore \(0<q\le nB\), and
\[
 \bigl\|\Delta_\omega u\bigr\|_{L^\infty}
 =\bigl\|q-\operatorname{tr}_\omega\theta\bigr\|_{L^\infty}
 \le nB+\|\operatorname{tr}_\omega\theta\|_{L^\infty}.
\]
This is a **fixed-coefficient, uniformly elliptic scalar equation**. For any \(p>2n\), a finite coordinate-chart cover and the standard interior \(W^{2,p}\) estimate (applied on smaller concentric charts) give
\[
 \|u\|_{W^{2,p}(X)}\le
 C_p\bigl(\|\Delta_\omega u\|_{L^p(X)}+\|u\|_{L^p(X)}\bigr)
 \le C'_p(nB+\|\operatorname{tr}_\omega\theta\|_\infty+M).
\]
The \(L^p\) term for \(u\) removes any need to normalize an additive constant. Sobolev–Morrey on each chart, \(W^{2,p}\hookrightarrow C^{1,\alpha}\) with \(\alpha=1-2n/p>0\), gives the asserted uniform gradient estimate. The coefficients of \(\Delta_\omega\) and the charts are fixed throughout, so the constants do not depend on \(u\). \(\square\)

## Sharp boundary: the density bound cannot simply be dropped

This is an independent smooth model **for complex dimension \(n\ge2\)**, testing the proposed endpoint theorem rather than the original \(m\ge2\) proposition. It shows that **bounded \(u\), first-cone admissibility, and even the feedback trace inequality with a fixed \(A\)** do not control gradients when the fixed upper density bound \(B\) is removed.

Take the flat complex torus \(X=(\mathbb C/(\mathbb Z+i\mathbb Z))^n\), \(\theta=\omega=i\sum dz_j\wedge d\bar z_j\), and set \(d=2n\ge4\). Fix \(0\le\rho\in C_c^\infty(B_{\mathbb R^d}(0,1/8))\) with \(\int\rho=1\). For \(\epsilon>0\) small, view
\[
 f_\epsilon(x)=\epsilon^{-2}\rho(x/\epsilon)
\]
as a smooth function on the torus, extended by zero off its coordinate ball. With the flat *real* Laplacian \(L=\sum_{\ell=1}^{d}\partial_{x_\ell}^2\), its integral is \(m_\epsilon=\epsilon^{d-2}\). Choose the mean-zero solution
\[
 L u_\epsilon=f_\epsilon-m_\epsilon .
\]
Equivalently \(u_\epsilon=G*f_\epsilon\), where \(LG=\delta_0-1\) and \(\int G=0\). By standard local fundamental-solution subtraction (valid for \(d\ge3\)),
\[
 G(x)=-c_d|x|^{2-d}+H(x),\qquad c_d>0,
\]
near zero, with \(H\) smooth there. The Green kernel is smooth away from zero.

The elementary integrability of \(|x|^{2-d}\) gives \(\|u_\epsilon\|_\infty\le C\): for centers within \(O(\epsilon)\) of the support, scale \(x=\epsilon s\); for farther centers use
\(m_\epsilon\,\operatorname{dist}(x,\operatorname{supp} f_\epsilon)^{2-d}\)
and the bounded smooth part. In particular this estimate is independent of \(\epsilon\).

On each fixed \(s\)-ball,
\[
 u_\epsilon(\epsilon s)=U(s)+O(\epsilon^{d-2}),\quad
 \nabla_x u_\epsilon(\epsilon s)
   =\epsilon^{-1}\nabla_s U(s)+O(\epsilon^{d-2}),
 \qquad
 U(s)=-c_d\int_{\mathbb R^d}|s-y|^{2-d}\rho(y)\,dy .
\]
The errors are uniform with first derivatives in the indicated scaled variable (and the \(\nabla_x\) error is \(O(\epsilon^{d-2})\) from the smooth torus remainder). \(U\) is bounded, smooth, nonconstant, and decays at infinity, so \(\nabla U(s_0)\ne0\) somewhere. The convolution bound for the gradient kernel \(|x|^{1-d}\), split into distances \(O(\epsilon)\) and greater, also gives
\[
 c\epsilon^{-1}\le R_\epsilon:=\sup_X|\partial u_\epsilon|_\omega
 \le C\epsilon^{-1}.
\]
Here and below all constants are independent of sufficiently small \(\epsilon\).

The \(dd^c\) convention of Pome is \(dd^c=(i/2\pi)\partial\bar\partial\). For the indicated flat \(\omega\),
\[
 \operatorname{tr}_\omega(\omega+dd^cu_\epsilon)
 =n+\kappa L u_\epsilon
 =n+\kappa(f_\epsilon-\epsilon^{d-2}),\qquad \kappa=\frac1{8\pi}>0.
\]
Hence this trace is positive for all small \(\epsilon\), i.e. the smooth form lies in \(\Gamma_1(\omega)\). Furthermore
\[
 \operatorname{tr}_\omega(\omega+dd^cu_\epsilon)
 \le n+\kappa\|\rho\|_\infty\epsilon^{-2}
 \le A(1+R_\epsilon^2)
\]
with a **fixed** \(A\), thanks to the gradient lower bound. Yet
\(R_\epsilon\to\infty\). The missing hypothesis is precisely a **uniform** \(B\): since \(f_\epsilon\) has supremum of order \(\epsilon^{-2}\), the normalized first-Hessian density
\(\frac1n\operatorname{tr}_\omega(\omega+dd^cu_\epsilon)\)
is unbounded. This is **not a counterexample under the printed assumptions**.

## Dependency, classification, and proposed treatment

- **Verified conditional deduction / low:** extend the *conclusion* of Proposition 8.3.3 to \(m=1\), explicitly using the fixed-coefficient elliptic estimate. At this endpoint the auxiliary trace inequality \(A(1+R^2)\) is redundant. The wedge/trace identity and reduction to a bounded scalar Laplacian are proved above; the standard local elliptic \(W^{2,p}\) estimate remains an acknowledged analytic input already used by the source text.
- **Verified conditional deduction / low (sharpness clause):** without the fixed upper bound \(B\), the remaining \(m=1\) hypotheses do not imply a gradient bound, as the torus construction shows. This tests a *hypothetical weakening*, not a false source theorem.
- **No repair claimed for Lemma 8.2.5.** Its \(m=1\) eigenvalue/trace inequality is still a separate confirmed error and remains unresolved on production main. It should not be used as an input to the endpoint extension.
- **Proposed future source patch, not applied:** add an endpoint paragraph after Proposition 8.3.3, or change its range to \(1\le m\le n\) and provide the separate \(m=1\) proof above. Do not extend its \(S_2\)-based argument to \(m=1\).
- **Affected dependents:** estimates for the scalar \(m=1\) trace equation gain the endpoint result; the printed \(m\ge2\) applications, including §§8.4–8.5, are not changed or certified. No Demailly approximation, dedicated Bergman, \(L^2\), Ohsawa–Takegoshi, multiscale-atlas, or positivity-loss proof programme was revisited.

**Coverage performed:** selected statement and proof paragraphs of Proposition 8.3.3, comparison of its \(S_2\) argument with the \(m=1\) scalar equation, and an independently constructed smooth torus family. Chapter/section inventory freshly read from \`docs/collection.json\`: **25 chapters, 747 numbered sections**. §8.3 had prior partial coverage; **0 newly first-visited sections, 0 complete section certifications**. No build, tests, CI, publication, source, canonicalization, or permanent-tag modifications.
