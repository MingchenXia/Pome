# Arithmetic rational/irrational rounding in an explicit partial-kernel family

**Finding:** POME-PARTIAL-KERNEL-RATIONAL-IRRATIONAL-ROUNDING-001.  
**Date:** 2026-11-09. **Severity:** low. **Status:** verified conditional deduction (a new explicit family; no claim that an existing theorem is false or that its analytic upstream dependencies are fully certified).

**Reviewed production main:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`.  
**Integrated reading edition:** \`docs/sections/partial-kernels-and-quotient-equilibrium--rounding-in-multiplier-ideal-kernel-families/index.html\`, blob \`f1c3a22bdbfa2598789f5df1ee8369eca29ff815\`. Section 18.46 source \`non-kahler-pluripotential-theory:E838CB8C\`, permanent tag \`73EEA7DBAB83\`, physical lines 5–10. Theorem 18.46.2 source \`non-kahler-pluripotential-theory:5A74DD32\`, permanent tag \`318BC0622217\`, physical lines **36–49**, proof **54–100**. Equation 18.46.1 source/permanent \`6F82427C/C673111EE95F\` (lines 27–29); equation 18.46.4 source/permanent \`778924A6/7E8D4542A29B\` (lines 67–71). The section's half-weight model is the special case \(t=1/2\).

## Precise supplemental claim

Let \(q\ge1\), \(Y=(\mathbb P^1)^q\), \(X=\mathbb P^1\times Y\), \(L=\mathcal O(1,\ldots,1)\), \(\theta=\sigma_0+\theta_Y\), \(h\) the product Fubini–Study metric and \(\nu=\sigma_0\otimes\nu_Y\), with the same normalizations as the printed theorem. Fix **any** \(0<t<1\), not necessarily rational. In the first affine coordinate set

\[
 \psi_t(z)=t\log|z|^2-\log(1+|z|^2),\qquad \psi_t=\psi_t\circ p_0,
\]
\[
 h(t)=-t\log t-(1-t)\log(1-t),\qquad E_t=\psi_t+h(t).
\]

These define a global \(\theta\)-psh function with
\[
 \theta+dd^c\psi_t=t[D_0]+(1-t)[D_\infty]+\theta_Y.
\]
Write \(V_m(t)=H^0(X,L^m\otimes\mathcal I(m\psi_t))\), its dimension \(N_m(t)\), its orthonormal partial kernel \(\mathcal B_m(t)\) and \(U_m(t)=m^{-1}\log\mathcal B_m(t)\).

**(1) Exact selection and arithmetic dichotomy.** Define
\[
 r_m=\lfloor mt\rfloor,\quad s_m=\lfloor m(1-t)\rfloor,\quad
 a_m=m-r_m-s_m+1.
\]
Then
\[
 V_m(t)=\operatorname{span}\{z^\alpha e_0^m\otimes s:
 r_m\le\alpha\le m-s_m,\ s\in H^0(Y,\mathcal O_Y(m,\ldots,m))\},
\]
and
\[
 N_m(t)=a_m(m+1)^q,\qquad
 a_m=\begin{cases}1,&mt\in\mathbb Z,\\2,&mt\notin\mathbb Z.\end{cases}
\]
If \(t=u/b\) is reduced rational, \(a_m=1\) precisely when \(b\mid m\), and \(a_m=2\) otherwise. If \(t\) is irrational, **\(a_m=2\) for every \(m\)**.

**(2) Envelope and potential/current convergence.** The \(\mathcal I\)-order envelope with obstacle \(0\) on \(K=X\) equals \(E_t\). On every compact subset of \(X\setminus(D_0\cup D_\infty)\),
\[
 U_m(t)\longrightarrow E_t
\]
uniformly. More precisely, in the first affine coordinate and for all sufficiently large \(m\),
\[
 |U_m(t)-E_t|\le
 \frac{C_{t,q}\log(m+1)+C_t|\log |z|^2|}{m}.
\]
Thus \(U_m(t)\to E_t\) in \(L^p(X)\) for all finite \(p\), with respect to smooth volume forms, and \(\theta+dd^cU_m(t)\rightharpoonup\theta+dd^cE_t\). Moreover \(\langle(\theta+dd^cE_t)^{q+1}\rangle=0\).

**(3) All subsequential kernel-measure limits.** Let \(\varsigma_t\) be normalized Haar measure on the circle
\[
 |z|^2=\frac{t}{1-t}.
\]
For every sequence of positive integers \(m_j\to\infty\) along which \(a_{m_j}=a\in\{1,2\}\) is constant,
\[
 \frac{q!}{m_j^q}\mathcal B_{m_j}(t)\nu
 \rightharpoonup a\,q!\,\varsigma_t\otimes\nu_Y.
\]
For **all** \(0<t<1\) one has the unoscillating dimension normalization
\[
 N_m(t)^{-1}\mathcal B_m(t)\nu\rightharpoonup\varsigma_t\otimes\nu_Y.
\]
For rational \(t\), the \(q!/m^q\)-normalized measures therefore have two distinct limits, along multiples and nonmultiples of the denominator; for irrational \(t\), that entire normalized sequence converges to \(2q!\,\varsigma_t\otimes\nu_Y\). The ambient \((q+1)!/m^{q+1}\)-normalization tends to zero in total variation in either case.

## Complete elementary model calculation

1. **Divisor coefficients and selected exponents.** In the chart at infinity with \(w=1/z\),
\[
 \psi_t=(1-t)\log|w|^2-\log(1+|w|^2).
\]
The local one-variable multiplier-ideal test is
\[
 |z|^{2\ell}e^{-m\psi_t}\in L^1_{\mathrm{loc}}
 \iff \ell-mt>-1
 \iff \ell\ge \lfloor mt\rfloor.
\]
The same test at infinity gives \(s_m\). Every section of \(\mathcal O_{\mathbb P^1}(m)\) is a polynomial of degree at most \(m\); this proves the stated exponent interval and, using \(mt+m(1-t)=m\), the exact count. The Y-factor contributes \((m+1)^q\). The calculations work equally when \(mt\) is an integer: the strict integrability inequality is retained, not rounded by guesswork.

2. **Exact beta norms.** Put \(x=|z|^2/(1+|z|^2)\in[0,1]\). The Fubini–Study area pushes to \(dx\), and different monomials are orthogonal. For \(0\le\alpha\le m\),
\[
 \|z^\alpha e_0^m\|^2=\int_0^1x^\alpha(1-x)^{m-\alpha}\,dx
  =\frac1{(m+1)\binom m\alpha}.
\]
The kernel on Y is exactly \((m+1)^q\). Hence, with \(A_m=\{\alpha:r_m\le\alpha\le m-s_m\}\),
\[
 \mathcal B_m(t)=(m+1)^{q+1}
     \sum_{\alpha\in A_m}\binom m\alpha x^\alpha(1-x)^{m-\alpha}.
\]
This formula is valid at both coordinate poles by its homogeneous interpretation; it yields \(\int_X\mathcal B_m\,d\nu=N_m\) exactly.

3. **Concentration.** The probability measure obtained by normalizing one monomial's squared norm has uniform angular variable and radial \(x\)-law \(\mathrm{Beta}(\alpha+1,m-\alpha+1)\). Because \(\alpha=mt+O(1)\), its mean \((\alpha+1)/(m+2)\to t\), and its variance
\[
 \frac{(\alpha+1)(m-\alpha+1)}{(m+2)^2(m+3)}=O_t(1/m).
\]
Chebyshev and uniform continuity on compact \(\mathbb P^1\) imply weak convergence of **each** of the at most two normalized monomial measures to \(\varsigma_t\). Their sum, multiplied by the exactly constant Y-kernel, proves all measure claims. The dimension normalization divides by the exact number \(a_m\) of terms, whereas the \(m^q\) normalization does not. Thus the rational/irrational distinction is entirely arithmetic, not a failure of the weak convergence of each individual monomial probability law.

4. **Potential estimate.** For \(\alpha=mt+O(1)\), the elementary binomial/Stirling estimate yields
\[
 \log\binom m\alpha=m h(t)+O_t(\log(m+1)).
\]
Since
\[
 \psi_t=t\log x+(1-t)\log(1-x),\quad
 (\alpha-mt)\log\frac{x}{1-x}=(\alpha-mt)\log|z|^2,
\]
the logarithm of each summand of the kernel divided by \(m\) differs from \(\psi_t+h(t)\) by the displayed error bound. Taking the sum of only one or two positive terms changes its logarithm by at most \(\log2\). Integrability of every finite power of the logarithmic coordinate singularities gives the \(L^p\) convergence. Distributional differentiation of the \(L^1\) convergence gives the weak current convergence, without interchanging incompatible limits.

5. **Envelope.** For an \(\mathcal I\)-order competitor \(v\le0\) quasi-everywhere, the stated internal multiplier-ideal/Lelong implication (Theorem 5.37.3) forces Lelong numbers at least \(t\) along \(D_0\) and \(1-t\) along \(D_\infty\). On a fiber where the restriction is not identically \(-\infty\), the positive curvature measure has total mass one and atoms of masses at least \(t\) and \(1-t\), which exhaust the mass. The restricted potential therefore differs from \(\psi_t\) by a constant \(c(y)\). A fiber on which the restriction is identically \(-\infty\) satisfies the desired upper bound trivially. The submean principle promotes the obstacle bound to everywhere; since \(\max_{\mathbb P^1}\psi_t=-h(t)\), every constant satisfies \(c(y)\le h(t)\). Thus \(v\le E_t\); conversely \(E_t\le0\), has the same \(\mathcal I\)-type as \(\psi_t\), and is a competitor. The original internal comparison theorem and restrictions remain **conditional dependencies**; the arithmetic, norms, concentration and Stirling bounds above are independent calculations.

6. **Top non-pluripolar mass.** On \(X\setminus(D_0\cup D_\infty)\), \(\theta+dd^cE_t=\theta_Y\) has rank \(q<q+1\). The non-pluripolar product does not charge the two polar divisors, giving zero top mass. This uses the existing NPP definition, not any excluded approximation argument.

## Verdict, risk, proposed patch, dependents

**Verdict:** Theorem 18.46.2 and its half-weight proof remain mathematically consistent. The supplement is a **verified conditional deduction** rather than a proven repair, a contradiction, or a certified complete analytic proof chain. Severity **low**: a useful exact generalization and a reminder that degree-normalization asymptotics depend on arithmetic denominator. An optional **Remark after Theorem 18.46.2** could state the rational/irrational dichotomy and the exact formula for \(a_m\), keeping all existing permanent tags and historical attribution. Do not identify this family with the different Newton selection of §18.45 or the three-band model §18.47 solely by similar kernel titles.

**Affected dependents/interpretation:** §18.46 dimension and weak-measure normalization, §18.30 selected-space definitions and §18.32 partial-envelope setup. This gives a concrete warning for statements assuming a single \(m^q\)-normalized partial-kernel limit without controlling multiplier-ideal rounding. No specific other printed theorem has been proved false. **Deferred by user, not examined:** Demailly regularization and its dedicated Bergman, \(L^2\), Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof-completion programme. Only explicit algebraic monomial integrals are used; no global Bergman estimates, weighted \(L^2\) correction or analytic proof expansion is attempted.

**Verification scope:** Direct reading-edition statement/proof inspection, exact floor arithmetic, beta-integral and variance calculation and independent binomial bound. No build, CI, numerical tests, formalization, publication, source-body or canonicalization changes. This is the **first direct selected mathematical proof review of §18.46**, not a full section certification.