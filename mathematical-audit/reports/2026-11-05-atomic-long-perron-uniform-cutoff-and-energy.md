# A singular atomic endpoint, its long Perron segments, and an exact cutoff-energy correction

**Date:** 2026-11-05. **Reviewed production main:** b6933b772f41b45918f7e25ed1afbbb1fd892272. **Audit branch:** review/mathematical-audit.

**Finding:** POME-GEO-ATOMIC-LONG-PERRON-CUTOFF-001. **Severity:** low. **Status:** verified conditional deduction (not a false printed theorem, not a complete dependency-chain certification). This adds an independently calculated atomic endpoint/cutoff model to the existing §17.9 proof review, not another registration of the smooth logistic-ray energy calculation.

## Exact integrated reading anchors

- Main file docs/sections/relative-energy-and-perron-segments--extremal-slopes-and-long-perron-segments/index.html, blob **023e78b3da0fd8f33d39177dba02f410b10f376c**. Proposition **17.9.1**, source **foundations-of-pluripotential-theory:58E4D688**, permanent tag **0583958ACA6D**, physical lines **11–25** (endpoint essential slopes). Proposition **17.9.2**, source **foundations-of-pluripotential-theory:2B4D191D**, permanent tag **A6533ED6CC68**, physical lines **34–72**, especially the bounded truncated endpoints and comparison in **54–72**. Section tag 66FE6F0ACABE.
- Dependency crosscheck only: Theorem **17.7.8**, source foundations-of-pluripotential-theory:108758A0 / permanent 2FECBE87C487, and Proposition **17.7.9**, source :470B93BF / permanent DD04D189A4D3; main file docs/sections/relative-energy-and-perron-segments--subgeodesics-and-perron-segments/index.html, blob 662f60d73fc585b6ea3b710f2a3472bac1de8a7c, lines **186–209**, **214–250**. Theorem **17.8.3**, source :907171A2 / permanent 678A18D6D406, main file docs/sections/relative-energy-and-perron-segments--energy-along-weak-geodesics/index.html, blob 8d9b7af925289346c96df751c67049e90c9dfe1d, lines **58–112**, for affine energy along bounded weak geodesics. Proposition **17.17.11**, source non-kahler-pluripotential-theory:42E4DFA8 / permanent 377F0AD20B28, main file docs/sections/test-curves-and-legendre-duality/index.html, blob 704ed205a974fe18e2dc502b13ceaf382b4af4b3, lines **206–239**, is contextual rather than a new theorem-level review.

The normalization is $dd^c=(i/2\pi)\partial\bar\partial$, $\omega=dd^c\log(1+|z|^2)$ on $\mathbb P^1$, and $\int_{\mathbb P^1}\omega=1$. Put $\phi=0$ (full-mass model) and
$$
m(z)=\frac{|z|^2}{1+|z|^2}\in[0,1],\qquad
u(z)=\log m(z),\quad u(0)=-\infty,\quad u(\infty)=0.
$$
Here $\omega+dd^c u=\delta_0\ge0$, so $u$ is a legitimate singular $\omega$-psh endpoint with $u\le\phi$. This is independent of all excluded approximation/regularization work.

## 1. Explicit smooth long-ray candidate and the complete Perron comparison

For $T>0$ and $0\le s\le T$ define
$$
u_T=\max\{u,-T\}=\log\max\{m,e^{-T}\},\qquad
L_s^T=G_{s/T}(0,u_T).
$$
Define a different, smooth family
$$
R_s(z)=\log\frac{e^{-s}+|z|^2}{1+|z|^2}
      =\log\bigl(e^{-s}+(1-e^{-s})m(z)\bigr),\qquad s\ge0.
$$
Each $R_s$ is smooth on $\mathbb P^1$, satisfies $-s\le R_s\le0$, $R_s(0)=-s$, $R_s(\infty)=0$, and has positive curvature
$$
\omega+dd^cR_s=dd^c\log(1+e^s|z|^2)>0.
$$

**Direct verification that $R_s$ is the weak geodesic between $R_0=0$ and $R_T$ on every $[0,T]$.** On the strip $0<\operatorname{Re}\zeta<T$, complexify $R$ using $s=\operatorname{Re}\zeta$. The holomorphic family of projective automorphisms $F(z,\zeta)=e^{\zeta/2}z$ satisfies
$$
p_1^*\omega+dd^c R_{\operatorname{Re}\zeta}=F^*\omega\ge0.
$$
The right side has complex rank at most one on the complex surface $\mathbb P^1\times S$, hence its square vanishes. More decisively, take any Perron competitor $V_\zeta$ for endpoints $0,R_T$ (imaginary-translation invariant, $p_1^*\omega$-psh, $L^1$ boundary endpoints at most $0,R_T$). Fiber convexity and its endpoint bound give $V_s\le(s/T)R_T\le0$. Set
$$
W(y,\zeta)=V_\zeta(e^{-\zeta/2}y)-R_{\operatorname{Re}\zeta}(e^{-\zeta/2}y).
$$
Pulling the positive current back by $(y,\zeta)\mapsto(e^{-\zeta/2}y,\zeta)$ yields $p_y^*\omega+dd^cW\ge0$, so for each fixed $y$, $\zeta\mapsto W(y,\zeta)$ is subharmonic. It is uniformly bounded above by $T$, since $V_s\le0$ and $R_s\ge-T$. The endpoint upper convex bound, together with the uniform smooth convergence of $R_s$ to $R_0,R_T$, gives $\limsup W\le0$ on both vertical boundary lines (the moving projective coordinate causes no problem because the endpoint bound is pointwise and uniform). The bounded-above subharmonic maximum principle on a strip implies $W\le0$: for completeness apply the bounded-domain maximum principle to $W-\varepsilon\cos(k(s-T/2))\cosh(k\eta)$, with $0<k<\pi/T$, on increasingly tall rectangles and then let $\varepsilon\downarrow0$. Therefore $V_s\le R_s$, while $R$ itself is a competitor. This establishes the claimed Perron equality without assuming that affine energy alone proves maximality.

For $a=e^{-T}$ we have the **exact endpoint sandwich**
$$
u_T=\log\max\{m,a\}\ \le\
R_T=\log\bigl(a+(1-a)m\bigr)
\ \le\ u_T+D_T,
\qquad D_T=\log(2-a).
$$
Indeed, the ratio $(a+(1-a)m)/\max\{m,a\}$ increases for $0\le m\le a$, decreases for $a\le m\le1$, and reaches its exact maximum $2-a$ at $m=a$. Thus $D_T$ is the **best uniform endpoint shift**; we do not claim it is the optimal interior geodesic error. Applying the proven Perron segment for $R$, the endpoint monotonicity of 17.7.9(1), and its affine-shift rule 17.7.9(2), gives
$$
\boxed{\quad
R_s-\frac{s}{T}\log(2-e^{-T})\ \le\ L_s^T\ \le\ R_s,
\qquad 0\le s\le T. \quad}
$$
Consequently, for each fixed $s\ge0$, the long-Perron limit in 17.9.2 is not merely a regularized monotone supremum but the explicitly smooth $R_s$, and the convergence is uniform in $z$, with a concrete $O(s/T)$ error. This does **not** assert a rate uniform as $s$ grows proportionally to $T$.

## 2. Exact extremal endpoint speeds even before taking the long limit

The elementary competitor $q_s=\max\{u,-s\}$ from the proof of Proposition 17.9.2 gives $L_s^T\ge q_s\ge-s$. Conversely the convex upper bound gives $L_s^T\le(s/T)u_T\le0$. At the pole $z=0$, both bounds are $-s$, and at $z=\infty$, both bounds are zero. Hence, **for every finite $T>0$ and $0\le s\le T$,**
$$
\boxed{\min_{\mathbb P^1}L_s^T=L_s^T(0)=-s,\qquad
\max_{\mathbb P^1}L_s^T=L_s^T(\infty)=0.}
$$
The essential extrema are identical because the functions are continuous, and puncturing either point does not alter essential extrema. This is an explicit sharp, singular-endpoint test of both signed-speed clauses of Proposition 17.9.1, not a restatement of its abstract proof.

## 3. Exact energy of the singular cutoff and finite-length correction

Use the dimension-one Aubin–Mabuchi normalization
$$
E(v)=\frac12\int_{\mathbb P^1}v(\omega+\omega_v),\qquad E(0)=0.
$$
Under $\omega$, the moment coordinate $m$ is uniformly distributed on $[0,1]$ (directly, the radial $\omega$ mass equals $dm$). Thus
$$
\int_{\mathbb P^1}u_T\,\omega
=\int_0^a(-T)\,dm+\int_a^1\log m\,dm=-1+e^{-T}.
$$
There is no Dirac mass at $0$ for the bounded potential $u_T$. On $\{m<a\}$, $u_T=-T$ and $\omega_{u_T}=\omega$ has mass $a$. On $\{m>a\}$, $u_T=\log m$ and $\omega_{u_T}=0$; across the contact circle $\{m=a\}$ there is positive mass $1-a$, from the jump of the radial derivative (or total cohomological mass one). The entire measure $\omega_{u_T}$ is therefore carried by the level $\{u_T=-T\}$, so $\int u_T\omega_{u_T}=-T$. We obtain the **exact formula**
$$
\boxed{\quad E(u_T)=-\frac T2-\frac{1-e^{-T}}2.\quad}
$$
For comparison, the smooth ray $R_s$ has $E(R_s)=-s/2$. This follows independently by changing variables in the two integrals: if $b=e^{-s}$, then $R_s(m)=\log(b+(1-b)m)$, and $\omega_{R_s}$ has $m$-density $b/(b+(1-b)m)^2$, giving
$$
\int R_s\,\omega=-1+\frac{bs}{1-b},\qquad
\int R_s\,\omega_{R_s}=1-\frac{s}{1-b}\qquad(s>0).
$$
Their sum equals $-s$ (and the formula extends continuously to $s=0$). These are elementary smooth/circle computations, not a repetition of the previously recorded positive logistic-ray moment law.

Applying Theorem 17.8.3 **conditionally** to the actual bounded weak geodesic $L^T$ now gives the **exact finite-length energy**
$$
\boxed{\quad E(L_s^T)
=\frac{s}{T}E(u_T)
=-\frac s2-\frac{s(1-e^{-T})}{2T}.\quad}
$$
In particular $E(L_s^T)\to E(R_s)$ for fixed $s$, with a signed correction explicitly equal to $-s(1-e^{-T})/(2T)$. This is a conditional use of the printed general energy-affinity theorem, **not** a complete independent proof of its analytic non-pluripolar integration prerequisites.

## Classification, dependencies, and proposed correction

The printed Propositions 17.9.1 and 17.9.2 are **not refuted**. The new verified conditional deduction is the explicit atomic singularity model, the best uniform endpoint distortion, the quantitative finite-long-segment Perron estimate, the exact realized extrema, and the finite-cutoff energy correction. It is distinct from POME-RWN-LOGISTIC-RAY-ENERGY-001 (smooth positive ray and moment law on §17.17) and POME-GEO-PAIRWISE-EXTREMAL-SPEED-001 (general signed essential-slope corollary), neither of which computed the singular cutoff $u_T$ or the long-Perron error and energy correction.

**Suggested optional addition:** after Proposition 17.9.2, include this atomic-endpoint example and its uniform comparison, retaining existing source attribution, permanent tags, and conventions. The direct weak-geodesic comparison uses elementary subharmonic maximum principles and the printed convex endpoint control; the finite-length energy formula still relies on Theorem 17.8.3. Upstream Bedford–Taylor/NPP and full general Perron, energy, and model-singularity chains remain **uncertified**. No false theorem, repaired theorem, duplication, build, formalization, or whole-section certificate is claimed.

**Exact new coverage:** targeted model verification of §17.9.1 (lines 11–25) and §17.9.2 (34–72), including singular-endpoint truncated rays and convergence; §17.7.8–9, §17.8.3, §17.17.11 are only dependency/convention crosschecks. The entire explicitly excluded Demailly approximation/regularization and dedicated Bergman, weighted-L², Ohsawa–Takegoshi, multiscale-atlas, and positivity-loss completion programme remains **deferred-by-user**, not reopened or certified. This report changes audit Markdown only.