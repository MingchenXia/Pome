# 2026-11-06 — exact projective weak geodesics from diagonal holomorphic flows

**Finding ID:** POME-GEO-PROJECTIVE-DIAGONAL-EXACT-001  
**Status:** verified conditional deduction (a self-contained exact-model verification, **not** a false printed theorem or a complete verification of the general geodesic existence/energy theory).  
**Severity:** low. **Scope:** selected integrated §17.7 and §17.8, with §17.3 energy definition; earlier audit findings remain unchanged.

## Fixed source and provenance

Reviewed production `main` **b6933b772f41b45918f7e25ed1afbbb1fd892272**. The actual reading-edition files, rather than only detached source numbers, were inspected:

- `docs/sections/relative-energy-and-perron-segments--subgeodesics-and-perron-segments/index.html`, blob **662f60d73fc585b6ea3b710f2a3472bac1de8a7c**, physical lines **6–24, 100–110, 180–211, 213–254**: Definition 17.7.1 (`foundations-of-pluripotential-theory:15664095` / permanent `B0604A42ABDF`), Proposition 17.7.4 (`:424728F5` / `61A0C5DD7757`), Definition 17.7.7 (`:041BC264` / `4A0AFDAD6156`), Theorem 17.7.8 (`:108758A0` / `2FECBE87C487`), Proposition 17.7.9 (`:470B93BF` / `DD04D189A4D3`).
- `docs/sections/relative-energy-and-perron-segments--energy-along-weak-geodesics/index.html`, blob **8d9b7af925289346c96df751c67049e90c9dfe1d**, physical lines **58–65 and 65–116**: Theorem 17.8.3 (`foundations-of-pluripotential-theory:907171A2` / `678A18D6D406`), especially its energy-affinity conclusion.
- `docs/sections/relative-energy-and-perron-segments--relative-monge-ampere-energy/index.html`, blob **16fdcc4c6a6f0cc75e69ba267bd7da2b2d7922a1**, physical lines **31–37**: Definition 17.3.2 (`foundations-of-pluripotential-theory:582D55DC` / `240EF1DE5889`) and energy equation 17.3.3 (`:8C7506A6` / `F19AAFA93177`).

The table of contents on this main has 25 chapters and 747 numbered sections. These are **selected** model/implication checks within previously partially sampled sections, not full section certifications.

## Exact statement and hypotheses

Take \(X=\mathbb P^n\), \(n\ge1\), with \(\omega=dd^c\log\sum_{j=0}^{n}|Z_j|^2\) in a homogeneous local trivialization, where \(dd^c=(i/2\pi)\partial\bar\partial\); normalize \(\int_X\omega^n=1\). Let \(a_0,\ldots,a_n\in\mathbb R\). Define globally smooth \(\omega\)-potentials
\[
 u_t([Z])=\log\frac{\sum_{j=0}^{n}e^{2a_jt}|Z_j|^2}{\sum_{j=0}^{n}|Z_j|^2},\qquad0\le t\le1.
\]
Then the **unrestricted Perron weak geodesic** from \(u_0=0\) to \(u_1\) is exactly \(u_t\). In addition,
\[
 E_{\omega}^{0}(u_t)=\frac{2t}{n+1}\sum_{j=0}^{n}a_j,\qquad
 \partial_tu_t=2\sum_j a_jp_j,\qquad
 \partial_t^2u_t=4\Bigl(\sum_j a_j^2p_j-(\sum_j a_jp_j)^2\Bigr),
\]
where \(p_j=e^{2a_jt}|Z_j|^2/\sum_k e^{2a_kt}|Z_k|^2\). Thus the pointwise time profile is **strictly convex** when the support of \(Z\) includes two distinct weights, although the integrated Monge–Ampère energy is **exactly affine**. Also \(\inf_X\dot u_t=2\min_j a_j\) and \(\sup_X\dot u_t=2\max_j a_j\), attained at the corresponding coordinate fixed points.

## Proof: the candidate is a genuine joint subgeodesic

Let \(S=\{\zeta\in\mathbb C:0<\Re\zeta<1\}\). The map
\[
 F:\mathbb P^n\times S\longrightarrow\mathbb P^n,\qquad
 ([Z],\zeta)\longmapsto[e^{a_0\zeta}Z_0:\cdots:e^{a_n\zeta}Z_n]
\]
is holomorphic. For \(U([Z],\zeta)=u_{\Re\zeta}([Z])\), its curvature satisfies
\[
 \operatorname{pr}_X^*\omega+dd^c U=F^*\omega\ge0.
\]
Indeed the local potential on the left is \(\log\sum_j|e^{a_j\zeta}Z_j|^2\). Hence \(U\) is a jointly \(\operatorname{pr}_X^*\omega\)-psh family, not merely a collection of slice-wise psh functions and convex time profiles. It is smooth up to \(\Re\zeta=0,1\), with the prescribed endpoints. Moreover,
\[
  (\operatorname{pr}_X^*\omega+dd^cU)^{n+1}=(F^*\omega)^{n+1}=0
\]
because the target has complex dimension \(n\). This vanishing needs no unbounded non-pluripolar continuity theorem.

## Proof: comparison with every Perron competitor (not just toric competitors)

Let \(V\) be the complexification of **any** competitor in Definition 17.7.7, with endpoint potentials \(v_0\le u_0\) and \(v_1\le u_1\). By Proposition 17.7.4, \(V\le(1-t)u_0+tu_1\) for \(t=\Re\zeta\), so \(V\) has a uniform upper bound on the full strip. Fix nonzero \(w=(w_0,\ldots,w_n)\in\mathbb C^{n+1}\), and consider the holomorphic curve
\[
 \gamma_w(\zeta)=[e^{-a_0\zeta}w_0:\cdots:e^{-a_n\zeta}w_n].
\]
The function
\[
 H_w(\zeta)=V(\gamma_w(\zeta),\zeta)
             +\log\sum_j|e^{-a_j\zeta}w_j|^2
\]
is subharmonic on \(S\), or identically \(-\infty\): the added logarithm is the pulled-back smooth Fubini–Study local potential along the nonvanishing holomorphic lift. It is bounded above because the logarithm is uniformly bounded for \(0\le\Re\zeta\le1\), independently of \(\Im\zeta\).

At either finite vertical boundary, \(\limsup H_w\le\log\sum_j|w_j|^2\). To justify this **even when the competitor has only \(L^1\) endpoint convergence**, fix \(s\in(0,1)\). Convexity and the endpoint inequality of Proposition 17.7.4, applied after restricting to \([0,s]\), give \(v_t(x)\le(1-t/s)u_0(x)+(t/s)M_s\) for \(t<s\), where \(M_s=\sup_Xv_s<\infty\); hence the joint upper limit as \((x,t)\to(x_*,0)\) is at most \(u_0(x_*)\). The symmetrical chord on \([s,1]\) gives the \(u_1\) bound. Along \(\gamma_w(iy)\) and \(\gamma_w(1+iy)\), the candidate satisfies identically
\[
 u_t(\gamma_w(t+iy))+\log\sum_j|e^{-a_j(t+iy)}w_j|^2
   =\log\sum_j|w_j|^2.
\]
The standard **bounded-above strip subharmonic maximum principle** now gives \(H_w\le\log\sum|w_j|^2\): for \(h=H_w-\log\sum|w_j|^2\), compare on \([0,1]\times[-R,R]\) with the positive harmonic barrier
\(\epsilon\cos\bigl(\tfrac{\pi}{2}(t-\tfrac12)\bigr)\cosh(\tfrac{\pi y}{2})\).
It is positive on the two vertical sides; for large \(R\), it also dominates the uniform upper bound for \(h\) on the two horizontal sides. First let \(R\to\infty\) on compact subsets and then \(\epsilon\downarrow0\). An identically \(-\infty\) leaf is automatic.

Evaluate at any \(([Z],\zeta)\) by choosing \(w_j=e^{a_j\zeta}Z_j\). The inequality is exactly \(V([Z],\zeta)\le U([Z],\zeta)\). As the explicit \(U\) is itself a competitor with exact endpoints, the full Perron upper envelope equals \(U\) *pointwise*. Neither a toric-only envelope assertion nor a uniqueness theorem for a degenerate homogeneous Monge–Ampère equation was assumed.

## Proof: exact energy, normalizations and sharp time behavior

The slice map \(F_t([Z])=[e^{a_jt}Z_j]\) is an automorphism and \(\omega_{u_t}=F_t^*\omega\). The smooth Kähler energy of Definition 17.3.2 is
\[
 E_\omega^0(u)=\frac{1}{n+1}\sum_{k=0}^n\int_X
       u\,\omega_u^k\wedge\omega^{n-k},\qquad E_\omega^0(0)=0.
\]
Differentiating, using \(d\omega=d\omega_u=0\) and Stokes to move \(dd^c\) from \(\dot u\) onto \(u\), the \(k\)-sum telescopes and gives
\[
 \frac d{dt}E_\omega^0(u_t)=\int_X\dot u_t\,\omega_{u_t}^n.
\]
With \(W=F_t([Z])\), the normalized weights in \(\dot u_t\) become \(|W_j|^2/\sum_k|W_k|^2\); permutation invariance of \(\omega^n\), together with \(\sum_j |W_j|^2/\sum_k|W_k|^2=1\) and \(\int\omega^n=1\), shows that each coordinate has average \(1/(n+1)\). Therefore \(E'_\omega(u_t)=2\sum_j a_j/(n+1)\) and the asserted energy formula follows.

Twice differentiating the finite log-sum-exp expression proves the weighted variance identity, with strict positivity whenever two nonzero coordinates have different weights; at a coordinate fixed point the variance is zero and \(\dot u_t=2a_j\). The extrema of the first derivative are exactly twice the smallest/largest weights. As a one-dimensional explicit normalization check, on \(\mathbb P^1\) with weights \((0,a)\),
\[
 u_t(z)=\log\frac{1+e^{2at}|z|^2}{1+|z|^2},
 \qquad E(u_t)=at;
\]
the first-variation integral reduces to \(2a\int_0^\infty s(1+s)^{-3}\,ds=a\).

## Adjudication, proposed action, and dependents

**No printed mathematical error is demonstrated.** The explicit unrestricted Perron calculation independently tests the distinction between *joint* subgeodesic positivity and slice-wise convexity, the boundary control in the definition of a competitor, and the coefficient/normalization in Theorem 17.8.3. The result is **verified conditional deduction / exact model**; it does not certify the general existence theorem, non-pluripolar integration by parts in §17.8, or finite-energy limiting arguments. No background-regularization program was consulted or reopened. An optional expository insertion could present this diagonal-flow model, preserving all existing theorem tags and attribution. Potential contextual dependents: §17.9 extremal speeds, §17.10 rays, §17.16 Perron interpolation, and §21.10 toric metrics; **none** of these are thereby certified. Prior unresolved and user-deferred ledger entries remain untouched. No project tests, build, browser checks, CI, or website publication were performed.
