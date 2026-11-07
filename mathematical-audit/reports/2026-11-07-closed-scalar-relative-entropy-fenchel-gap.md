# Exact Fenchel/Kullback–Leibler gap for the closed-background scalar

**Date:** 2026-11-07. **Finding:** POME-CLOSED-SCALAR-FENCHEL-KL-GAP-001. **Severity:** low. **Status:** verified conditional deduction, not a confirmed error or full proof-chain certification.

## Pinned integrated reading edition

Production main: b6933b772f41b45918f7e25ed1afbbb1fd892272.

- `docs/sections/normalization-and-weak-adjoint-measures--entropy-and-the-closed-case/index.html`, blob `0710d0732ae7ef81de3d3d62206a0f9c6b5d321f`. Formula (11.37.2), source `non-kahler-pluripotential-theory:65FF799F`, permanent tag `803909FECEC0`, physical lines 54–61. Proposition 11.37.3, source `non-kahler-pluripotential-theory:460EAE65`, permanent `33DF3CE1122A`, lines 64–76; entropy variational Lemma 11.37.1, source `non-kahler-pluripotential-theory:C2CF0A52`, permanent `2E4E82F8C3FC`, lines 19–50.
- `docs/sections/normalization-and-weak-adjoint-measures--a-convex-functional-on-probability-measures/index.html`, blob `9a4ba5a98abd3273a6872c68beccf764e936d3f0`. Dual definition (11.35.1), source `non-kahler-pluripotential-theory:A5C670F7`, permanent `FFB47018170B`, lines 10–17; Proposition 11.35.2 / formula (11.35.3), sources `A1D8D375` / `86EF99CC`, permanent `0C21983AC42D` / `88A1B49C1D77`, lines 20–39.
- `docs/sections/normalization-and-weak-adjoint-measures--supporting-probability-measures/index.html`, blob `a8afa97be049b56b6c7d18302499364022feaa39`, Proposition 11.34.5, source `non-kahler-pluripotential-theory:55DDB559`, permanent `792D6FEF2F3C`, physical lines 73–93.
- `docs/sections/normalization-and-weak-adjoint-measures--the-scalar-functional/index.html`, blob `fff86de757578ed2be369ba752123f62f3d31044`, Theorem 11.33.4, source `non-kahler-pluripotential-theory:547E9FD9`, permanent `8810E18F852C`, lines 61–78.

## Hypotheses and exact new deduction

Let \(X\) be compact Kähler, \(\theta\) Kähler, \(\varphi\) a standing prescribed ordinary singularity type with fixed positive non-pluripolar mass \(m_\varphi>0\); let \(\mathrm dV\) be any smooth positive finite volume form (not necessarily of total mass one). **Conditionally on the already integrated fixed-mass assertion in Theorem 13.8.7 and scalar existence in Theorem 15.12.1**, the printed identities are
\[
 B_\varphi(F)=\log m_\varphi-\log Z_F,\quad
 H_\varphi(\nu)=\log m_\varphi+\mathrm{Ent}_{\mathrm dV}(\nu),\quad
 Z_F=\int_Xe^F\,\mathrm dV
\]
for real \(F\in C(X)\) and Borel probability \(\nu\); the unique supporting measure is \(\nu_F=Z_F^{-1}e^F\,\mathrm dV\). For every probability \(\nu\), including those with infinite entropy, the **Fenchel gap is exactly relative entropy**:
\[
 \boxed{\quad H_\varphi(\nu)-\int_X F\,\mathrm d\nu-B_\varphi(F)
   =D_{\mathrm{KL}}(\nu\Vert\nu_F)
   \ \geq\ \tfrac12\|\nu-\nu_F\|_{\mathrm{var}}^2.\quad} \tag{A}
\]
Here \(\|\lambda\|_{\mathrm{var}}=|\lambda|(X)\), so it is **twice** the usual probabilistic total-variation distance between two probabilities. The gap is zero **if and only if** \(\nu=\nu_F\). In particular, every \(\varepsilon\)-approximate minimizer of the dual problem obeys \(\|\nu-\nu_F\|_{\mathrm{var}}\leq\sqrt{2\varepsilon}\); the bound is independent of \(m_\varphi\) and the total volume of \(\mathrm dV\).

For any \(G\in C(X,\mathbb R)\), put \(\nu_t=\nu_{F+tG}\). Then
\[
 B_\varphi'(F+tG)[G]=-\int_XG\,\mathrm d\nu_t,\qquad
 \frac{\mathrm d^2}{\mathrm dt^2}B_\varphi(F+tG)
 =-\operatorname{Var}_{\nu_t}(G), \tag{B}
\]
and both exact integrated identities hold:
\[
 \boxed{B_\varphi(F+G)-B_\varphi(F)+\int_XG\,\mathrm d\nu_F
 =-\int_0^1(1-t)\operatorname{Var}_{\nu_t}(G)\,\mathrm dt,} \tag{C}
\]
\[
 \boxed{D_{\mathrm{KL}}(\nu_{F+G}\Vert\nu_F)
 =\int_0^1t\,\operatorname{Var}_{\nu_t}(G)\,\mathrm dt.} \tag{D}
\]
These formulas show strict concavity modulo constant directions: equality in (C) occurs precisely when \(G\) is constant on \(X\), as each Gibbs probability has full support. They also identify the Hessian as the negative covariance bilinear form.

## Complete elementary justification of the new steps

For \(\nu=h\,\mathrm dV\) and \(k=e^F/Z_F>0\), expansion of the printed entropy gives
\[
 H_\varphi(\nu)-\int F\,\mathrm d\nu-B_\varphi(F)
 =\int h\log(h/k)\,\mathrm dV.
\]
If \(\nu\not\ll\mathrm dV\), both sides of (A) are \(+\infty\), since \(\nu_F\sim\mathrm dV\). No ambiguous difference of infinite quantities occurs because \(B_\varphi(F)\) and \(\int F\,\mathrm d\nu\) are finite.

Here is a self-contained quantitative KL estimate. Let \(A=\{h\geq k\}\), \(p=\nu(A)\), \(q=\nu_F(A)\). Conditional Jensen on \(A\) and its complement gives
\[
 D_{\mathrm{KL}}(\nu\Vert\nu_F)\geq
 p\log(p/q)+(1-p)\log((1-p)/(1-q)).
\]
The Bernoulli entropy on the right, as a function of \(p\) with fixed \(q\), vanishes with zero derivative at \(p=q\) and has second derivative \(1/[p(1-p)]\geq4\). Thus it is at least \(2(p-q)^2\), including endpoints by continuity. As \(p-q=\frac12\int|h-k|\,\mathrm dV=\frac12\|\nu-\nu_F\|_{\mathrm{var}}\), (A) follows. A singular \(\nu\) has infinite KL gap and satisfies the estimate trivially.

Differentiation under the integral in \(Z_{F+tG}\) is legitimate for continuous \(F,G\) on compact \(X\); it gives \((\log Z)'=\mathbb E_{\nu_t}G\), \((\log Z)''=\mathbb E_{\nu_t}G^2-(\mathbb E_{\nu_t}G)^2\). This proves (B). Taylor's formula with integral remainder proves (C). Finally
\[
 D_{\mathrm{KL}}(\nu_t\Vert\nu_0)
 =t\mathbb E_{\nu_t}G-\log(Z_{F+tG}/Z_F),
\]
whose derivative is \(t\operatorname{Var}_{\nu_t}(G)\); integrate from \(0\) to \(1\) for (D). Positivity and full support make variance zero exactly for continuous constants.

## Scope, classification and affected dependents

**Classification:** low / **verified conditional deduction**. The printed §11.35.2, §11.37.3, §11.34.5 and §11.33.4 are **not contradicted**. This adds a quantitative uniqueness certificate for the closed/Kähler dual minimizer, not a correction of an invalid theorem. It sharpens the *interpretation* of §11.35.3 and §11.37.3 and can be used when assessing approximate supporting measures, but **does not** imply an analogous identity for a nonclosed Hermitian background or for arbitrary singularity types without the fixed-mass premise. The original nontrivial existence and fixed-mass inputs remain conditional; no full transitive proof certification. Demailly approximation/regularization and its dedicated Bergman/L²/Ohsawa–Takegoshi/multiscale/positivity-loss programme were **not** inspected or invoked.

**Actual coverage:** selected displayed identities/proofs in §§11.33–11.35, 11.37 and a new explicit KL/Pinsker/covariance deduction, not all statements of any of those sections. All were previously sampled, so **no new first section visit**; 25 chapters / 747 numbered sections / zero full mathematical section certifications. No source, published reading edition, registry, or tags changed. No build, CI, formalization, or website publication performed.
