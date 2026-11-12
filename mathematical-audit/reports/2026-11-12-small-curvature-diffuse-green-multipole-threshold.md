# 2026-11-12 — Diffuse Green poles in a small-curvature ordinary type: exact finite-point strictness threshold

**Finding ID:** POME-IDEAL-SMALLCURV-DIFFUSE-GREEN-THRESHOLD-001  
**Severity/status:** low / **verified conditional deduction** (explicit model; no printed theorem is refuted).  
**Reviewed production main:** b6933b772f41b45918f7e25ed1afbbb1fd892272.  
**Integrated reading-edition file:** docs/sections/multiplier-ideal-envelopes-and-goodness--small-curvature-and-strict-ordinary-types/index.html; blob a6e3cc7cb9c6931688e089bb67b2ed12766f6a0b.  
**Scope:** §18.27, particularly property (18.27.1), Lemma 18.27.2 and Theorem 18.27.4. This is an explicit, nontrivial unbounded-residual test of the theorem, **not** a proof of the general theorem or its regularization-dependent step.

## Source anchors and audit boundary

- §18.27 heading permanent tag 0A2CF48796FA, original source non-kahler-pluripotential-theory:B27C5590; physical lines 5–15.
- Equation 18.27.1 original non-kahler-pluripotential-theory:7EF9FD2F, permanent 4A552AB10BA9, lines 9–14.
- Lemma 18.27.2 original :23EAD3EF, permanent 96F4F5465740, lines 17–45.
- Lemma 18.27.3 original :E21E31BD, permanent E5C4A193363D, lines 48–64. **Its proof explicitly invokes the excluded current regularization at physical line 55: retained as deferred-by-user, not independently checked here.**
- Theorem 18.27.4 original :E6C58118, permanent 0E6CABEB995A, lines 75–95 (divisorial conventions in lines 66–72).

## Complete explicit model (no regularization)

Normalize \(dd^c=\frac{i}{2\pi}\partial\bar\partial\), and let \(X=\mathbb P^1\), \(\omega=\omega_{\rm FS}\) with \(\int_X\omega=1\). Write \(G(x,y)=\log [x,y]^2\), the logarithm of squared chordal distance, where
\[
dd^c_xG(x,y)=\delta_y-\omega,\qquad G(x,y)\leq0.
\]
The identity follows in an affine chart from \(G(z,w)=\log|z-w|^2-\log(1+|z|^2)-\log(1+|w|^2)\) and Poincaré–Lelong. All later integrals are against explicit **finite, nonatomic** positive measures.

Choose distinct \(p_1,\ldots,p_s\) and disjoint unitary affine coordinate disks \(U_i\) with \(z_i(p_i)=0\). Fix \(0<\alpha_i<1\), \(c_i>0\), and on \(|z_i|<e^{-2}\) set
\[
d\mu_i(z_i)=\frac{c_i\,\mathbf1_{\{|z_i|<e^{-2}\}}}
{2\pi |z_i|^2(-\log|z_i|)^{1+\alpha_i}}\,dA(z_i),
\qquad \mu=\sum_{i=1}^s\mu_i.
\]
In polar variables \(t=-\log r\), the radial mass is exactly \(c_i t^{-1-\alpha_i}dt\), hence
\[
\mu_i(X)=\frac{c_i}{\alpha_i2^{\alpha_i}}<\infty,\qquad
\mu_i(\{|z_i|<e^{-T}\})=\frac{c_i}{\alpha_i T^{\alpha_i}}\quad(T\ge2).
\]
There are no point atoms, including at the centers. Define the quasi-psh potential
\[
q(x)=\int_XG(x,y)\,d\mu(y),\qquad dd^cq=\mu-\mu(X)\omega .
\]
The potential is not identically minus infinity: \(G(\cdot,y)\) is uniformly integrable against \(\omega\) by spherical invariance, so Fubini gives \(q\in L^1(X)\). Its only poles are the \(p_i\). For \(r=|z_i|\), \(t=-\log r\to\infty\), the elementary angular average
\[
\frac1{2\pi}\int_0^{2\pi}\log|z_i-\rho e^{i\vartheta}|^2\,d\vartheta
=2\log\max(r,\rho)
\]
gives, with all smooth chordal denominators and other-pole contributions bounded,
\[
\begin{aligned}
q(z_i)&=-2c_i\left(\int_2^t u^{-\alpha_i}\,du
+t\int_t^\infty u^{-1-\alpha_i}\,du\right)+O(1)\\
&=-\frac{2c_i}{\alpha_i(1-\alpha_i)}
(-\log|z_i|)^{1-\alpha_i}+O(1).
\end{aligned}
\]
Thus \(q(p_i)=-\infty\), \(q\) is genuinely unbounded, yet \(\nu(q,p_i)=0\) because \(1-\alpha_i<1\); all other point Lelong numbers are also zero. Its first-Hessian polar curvature is zero: \(1_{\{q=-\infty\}}dd^cq=\sum_i\mu(\{p_i\})\delta_{p_i}=0\).

For \(T>2\), define
\[
\mu_T=\sum_i\mu_i|_{\{|z_i|<e^{-T}\}},\quad
m_T=\mu_T(X)=\sum_i\frac{c_i}{\alpha_i T^{\alpha_i}}\longrightarrow0,\quad
q_T=G*\mu_T.
\]
The removed measure \(\mu-\mu_T\) has bounded density supported away from every \(p_i\); its logarithmic potential is a bounded continuous function on compact \(X\). Consequently \(q_T-q\) is **globally bounded**, in the ordinary singularity sense (including at the pole points), so \(q_T\sim q\) while
\[
dd^cq_T=\mu_T-m_T\omega\geq-m_T\omega.
\]
Given any \(\delta>0\), a sufficiently large \(T\) has \(m_T<\delta\). This proves the **non-vacuous** small-curvature property (18.27.1) for an explicitly unbounded residual, without Demailly approximation or any Bergman, \(L^2\), Ohsawa–Takegoshi, multiscale, or positivity-loss arguments.

## Sharp multi-divisor threshold, independently proved in dimension one

Take an arbitrary effective real divisor \(\Delta=\sum_{i=1}^s\lambda_i[p_i]\), \(\lambda_i\ge0\), and put \(\Lambda=\sum_i\lambda_i\). Choose the divisor metrics represented by
\[
\sigma_\Delta=\sum_i\lambda_iG(\cdot,p_i),\qquad
dd^c\sigma_\Delta=[\Delta]-\Lambda\omega.
\]
For \(\theta=a\omega\) with real \(a\), the ordinary singularity type
\(\sigma_\Delta+q+O(1)\) contains \(v\) satisfying
\(\theta+dd^cv\geq\varepsilon\omega\) for some \(\varepsilon>0\)
**if and only if \(a>\Lambda\)**.

**Sufficiency.** If \(a>\Lambda\), choose \(T\) with \(m_T<(a-\Lambda)/2\). With \(v=\sigma_\Delta+q_T\sim\sigma_\Delta+q\),
\[
a\omega+dd^cv
=[\Delta]+\mu_T+(a-\Lambda-m_T)\omega
\geq\frac{a-\Lambda}{2}\omega.
\]
This is a direct construction, not a consequence imported from Lemma 18.27.3.

**Necessity.** Let \(v\sim\sigma_\Delta+q\) and \(a\omega+dd^cv\geq\varepsilon\omega\). Bounded changes preserve local Lelong numbers, and the explicit asymptotic proves \(\nu(v,p_i)=\lambda_i\). On a Riemann surface the positive current \(T=a\omega+dd^cv\) is a positive measure whose atom at \(p_i\) has mass \(\lambda_i\) in this normalization. The positive measure \(T-\varepsilon\omega\) has the same atoms (since \(\omega\) has none), and its total mass is \(a-\varepsilon\), by Stokes. Hence
\[
a-\varepsilon\ \geq\ \sum_i\lambda_i=\Lambda,
\]
so \(a>\Lambda\). Nothing is assumed about sequences versus nets, and no limit of singular wedge products is taken.

This sharp scalar threshold independently tests both directions of printed Theorem 18.27.4 in a family where the residual is unbounded, has zero Lelong numbers, and satisfies (18.27.1). It does not assert that the **general** theorem has been proved independently of its cited current-regularization input.

## Classification, deduplication and affected dependents

**Status:** verified conditional deduction; **severity:** low. The exact finite-pole Green construction and degree threshold are directly proved above, with only the elementary Poincaré–Lelong kernel normalization and Stokes identity. The general theorem's dependency on Lemma 18.27.3 remains **deferred-by-user**, neither resolved nor certified. There is **no confirmed error** or new general repair. The earlier POME-IDEAL-SMALL-CURV-LATTICE-001 concerned algebraic cone/max closure of small-curvature representatives; it did not construct this diffuse unbounded Green residual or compute a sharp multi-atom strict-current threshold, and its status is unchanged.

**Proposed optional addition:** after §18.27.4, add a short worked \(\mathbb P^1\) example with the tail Green measures and the criterion \(a>\sum_i\lambda_i\). Preserve the original theorem, historical attribution, source labels, permanent tags and all variants. **Affected discussions:** §§18.27.1–4 (exact hypotheses and possible examples), adjacent ordinary-versus-ideal type discussions; no change to the proof graph or to any excluded regularization programme.

**Coverage:** precise selected proof-level revisit of §18.27.1, .2 and .4, plus identification—not audit—of regularization-dependent .3. The current ToC and section matrix have 25 chapters and 747 numbered sections; §18.27 was already marked partially reviewed before this run: **0 newly first-visited numbered sections, 0 fully certified sections**. No mathematical text, sources, registry, canonicalization, permanent tags, CI, test suite, project build, or published docs were changed.
