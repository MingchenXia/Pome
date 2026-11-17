# Exact Beta–Bernstein projective-fiber mass and its endpoint bias (17 November 2026)

**Finding:** POME-NPP-PROJECTIVE-BETA-BERNSTEIN-BIAS-001  
**Classification:** low / verified conditional deduction; no original statement refuted.  
**Reviewed main:** b6933b772f41b45918f7e25ed1afbbb1fd892272.  
**Integrated file:** docs/sections/non-pluripolar-products--mass-comparison-and-projective-fibers/index.html, blob dd89e44c511fd6f6bdd164a09a77c1637c42b410.  
**Precisely inspected:** Lemma 13.8.2, source foundations-of-pluripotential-theory:F84147BD / permanent 984FFB015C24 (physical lines 61–70, computation 135–153 and locally bounded passage 157–162); Proposition 13.8.5, source CCE5A11D / permanent A00B4940B406 (lines 166–181 and proof 185–213); Equation 13.8.6, source 46575BF5 / permanent 56FDDE3E50E0 (lines 176–179); Theorem 13.8.7, source 6A80B686 / permanent 60DE4F681F75 (lines 218–244, especially the Beta endpoint argument at 229–242). Corollary 13.8.8 (249–262) is dependent context only.

## Precisely scoped claim

Let X be a compact Kähler manifold of complex dimension n >= 1, theta a smooth closed real (1,1)-form, phi_0,phi in PSH(X,theta). Assume **as a premise** that phi_0 has closed pole set and is smooth off that set, so that Proposition 13.8.5 and its projective mass formula apply; do not infer existence of phi_0 by auditing an excluded regularization construction. Define positive currents T_0=theta+dd^c phi_0 and T=theta+dd^c phi, and the finite, nonnegative mixed masses

\[
M_k=\int_X \left\langle T_0^{n-k}\wedge T^k\right\rangle,\qquad 0\le k\le n.
\]

Let Phi_N be exactly the projective-fiber potential of Proposition 13.8.5, and normalize its mass by

\[
A_N=\binom{n+N}{n}^{-1}
 \int_{X\times\mathbb P^N}
 \left\langle(\widetilde\theta+dd^c\Phi_N)^{n+N}\right\rangle .
\]

Then for *every* positive integer N, rather than just asymptotically,

\[
\boxed{A_N=\sum_{k=0}^{n}w_{N,k}M_k,\qquad
w_{N,k}=\frac{n!\,N\,(N+k-1)!}{k!\,(N+n)!}.}\tag{1}
\]

The w_{N,k} are strictly positive, sum to one, and w_{N,n}=N/(N+n). Consequently,

\[
\boxed{|A_N-M_n|\le \frac{n}{N+n}
 \max_{0\le k<n}|M_k-M_n|.}\tag{2}
\]

For each *fixed* pair (T_0,T), the exact leading bias is

\[
\boxed{\lim_{N\to\infty}N(A_N-M_n)=n(M_{n-1}-M_n),}\tag{3}
\]

in fact A_N=M_n+n(M_{n-1}-M_n)/N+O(N^{-2}). No sign for A_N-M_n is forced without additional singularity ordering. These identities involve the non-pluripolar masses, *not* the cohomological intersection numbers of theta unless all required full-mass hypotheses are independently established.

## Proof of the weights and estimate

The multilinearity of non-pluripolar products of positive currents, used explicitly at the end of Theorem 13.8.7, gives the ordinary Bernstein polynomial

\[
f(t)=\int_X\langle((1-t)T_0+tT)^n\rangle
=\sum_{k=0}^n\binom nk(1-t)^{n-k}t^k M_k.
\]

By the exact projective mass formula (13.8.6), A_N=N\int_0^1f(t)t^{N-1}dt. Integrating each of the n+1 terms (a *finite* sum) yields

\[
\begin{aligned}
w_{N,k}
&=\binom nk N\int_0^1 t^{N+k-1}(1-t)^{n-k}dt\\
&=\binom nk N\,\mathrm B(N+k,n-k+1)\\
&=\frac{n!N(N+k-1)!}{k!(N+n)!}.
\end{aligned}
\]

In particular \(\sum_k w_{N,k}=N\int_0^1t^{N-1}\sum_k\binom nk t^k(1-t)^{n-k}dt=1\). Direct substitution at k=n shows w_{N,n}=N/(N+n). Therefore

\[
A_N-M_n=\sum_{k=0}^{n-1} w_{N,k}(M_k-M_n).
\]

All coefficients on the right are nonnegative; their sum is exactly n/(N+n). This proves (2), with no passage under a weak limit. For n=2,N=2, (w_{2,0},w_{2,1},w_{2,2})=(1/6,1/3,1/2), an independent factorial/normalization crosscheck.

Finally w_{N,n-1}=nN/((N+n)(N+n-1)), while for every k<=n-2 one has w_{N,k}=O(N^{k-n}); in particular their sum is O(N^{-2}). Since the M_k are fixed finite numbers, Nw_{N,n-1}->n and Nw_{N,k}->0 for all k<=n-2, which proves (3) and the stated remainder. The n=1 case has no k<=n-2 terms and is exact: A_N-M_1=(M_0-M_1)/(N+1).

## Sharp geometric examples, both signs, and faster decay

Take X=\mathbb P^n, theta=omega_FS with \(\int_X\omega_{\mathrm{FS}}^n=1\), and a hyperplane H defined by a section s of O(1). Normalize the Hermitian metric so that

\[
dd^c\log|s|_h^2=[H]-\omega_{\mathrm{FS}}.
\]

For \(0<\varepsilon<1\) set \(\phi_\varepsilon=(1-\varepsilon)\log|s|_h^2\), so \(T_\varepsilon=\varepsilon\omega_{\mathrm{FS}}+(1-\varepsilon)[H]\).
Non-pluripolar products give zero mass to H; on its complement T_epsilon equals epsilon omega_FS. Thus, with T_0=omega_FS and T=T_epsilon, the mixed masses are **exactly** M_k=epsilon^k and

\[
f(t)=(1-(1-\varepsilon)t)^n,\quad
A_N-\varepsilon^n
=\frac{n(1-\varepsilon)\varepsilon^{n-1}}N+O(N^{-2})>0
\]

to leading order. In particular the O(N^{-1}) rate is genuinely attained by a singular current, for every n >= 1.

Reverse the roles: T_0=T_epsilon, T=omega_FS. This is still allowed by Proposition 13.8.5, since the pole divisor of phi_0 is closed and phi_0 is smooth off it. Now M_k=epsilon^{n-k}, f(t)=(epsilon+(1-epsilon)t)^n, and

\[
A_N-1=-\frac{n(1-\varepsilon)}N+O(N^{-2})<0
\]

to leading order. Thus even for a smooth Kähler reference class there is **no universal one-sided direction** for finite-N approximation.

At the boundary epsilon=0 with smooth T_0=omega_FS and T=[H], all mixed masses M_k with k>=1 vanish, and the exact formula reduces to

\[
A_N=w_{N,0}=\frac{n!\,N!}{(N+n)!}\sim n!\,N^{-n},
\]

showing a faster rate can occur without contradicting the sharp worst-case O(N^{-1}) upper bound. These examples test non-pluripolar product conventions, not any Demailly-regularization argument.

## Status, dependencies, and proposed insertion

- **Verified conditional deduction, low severity.** The algebra, weights, error bound, leading coefficient and projective examples are verified under the displayed NPP multilinearity and projective mass formula. Theorem 13.8.7 and Proposition 13.8.5 are **not false**, and the above does not certify their full proof chains.
- **Internal mathematical inputs not re-certified:** finite NPP masses and multilinearity (13.5.4 / 13.2.6); local simplex pushforward (13.8.2); projective global mass identity (13.8.5). The existence clause for a suitable reference phi_0 may cite the explicitly **deferred-by-user** regularization programme; it is not needed for the two explicit projective examples and has not been reopened.
- **Affected dependent:** Theorem 13.8.7 uses the limit of \(Nt^{N-1}\) against the Bernstein polynomial f. Equations (1)–(3) provide an exact quantitative supplement and a two-sided sign diagnostic; Corollary 13.8.8 uses the resulting mass comparison but needs no logical change.
- **Proposed optional text-only mathematical-body patch, NOT applied:** after Equation 13.8.6 or in the proof of Theorem 13.8.7, add the weight formula, the n/(N+n) estimate and an explicit warning that the finite-N bias may have either sign. Preserve all source and permanent tags, existing theorem wording and historical attribution.
- **Coverage:** selected new proof-level examination of the Beta endpoint coefficient structure and the two singular Kähler models in §13.8. Previously partially audited §13.8: 0 newly first-visited sections, 0 fully certified sections. No other chapter or section is inferred complete. No build, project test suite, CI or publication was run.
