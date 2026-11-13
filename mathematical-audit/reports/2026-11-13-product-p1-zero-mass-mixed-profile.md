# Chapter 17, §17.6: arbitrary orders of mass collapse and the mixed-mass profile on products of projective lines

**Finding ID:** POME-ENV-PRODUCT-ZEROMASS-MIXED-ORDER-001  
**Date:** 2026-11-13  
**Status:** verified conditional deduction (new explicit model, no printed theorem refuted).  
**Severity:** low.  
**Reviewed production main:** b6933b772f41b45918f7e25ed1afbbb1fd892272.  
**Scope:** original §17.6.1 mass interpolation and §17.6.4–5 mixed-mass ceiling; selected formula-level verification of §13.2.6 and §16.21.2(3). No regularization or dedicated Bergman/L2/OT/multiscale/positivity-loss audit.

## Exact reading-edition anchors

- docs/sections/relative-energy-and-perron-segments--singularity-envelopes-at-arbitrary-mass/index.html, blob addc238e2dc806ff14a69fa8c8e5bdf46da448f2: Proposition 17.6.1, source foundations-of-pluripotential-theory:1031B084, permanent DC1056C1A4A1, lines 16–21; mixed measures and polynomial Step 2, lines 31–43, Equation 17.6.2 (permanent C6464A625C78), lines 53–55; Definition 17.6.4, source :739AB03B, permanent 0C3B4338E463, lines 130–136; Theorem 17.6.5, source :402BEA9A, permanent C6C3A19AAB0D, lines 139–180, especially mixed-mass comparison lines 150–172.
- docs/sections/non-pluripolar-products--truncation-and-plurifine-locality/index.html, blob 81be8c5acc360c96bd3c5acba05a3cdb5fafaf4c: Proposition 13.2.6, source foundations-of-pluripotential-theory:E82F0D73, permanent 7F7123F92478, lines 80–85, 90–115 (locality and multilinearity).
- docs/sections/envelopes-and-model-potentials--singularity-envelopes/index.html, blob 8d55c95795ea2a0a3cf5cb81bd4abb4ba867a16a: Proposition 16.21.2, source foundations-of-pluripotential-theory:92AD249D, permanent 037CA226D141, lines 19–41 (especially mixed-mass preservation in clause 3, lines 32–38).
- The normalization throughout is $dd^c=(i/2\pi)\partial\bar\partial$ and $\int_{\mathbf P^1}\omega_{\mathrm{FS}}=1$.

## Claim and complete explicit calculation

Let $n\ge2$, $X=(\mathbf P^1)^n$, and let $\omega_i=\pi_i^*\omega_{\mathrm{FS}}$, $\theta=\sum_{i=1}^n\omega_i$. This is a Kähler form, so its normalized minimal potential is $V_\theta=0$. Let $D_i$ be the inverse image of $[1:0]$ on the $i$th factor and put
\[
g_i=\pi_i^*\log\frac{|Z_1|^2}{|Z_0|^2+|Z_1|^2}.
\]
Here $g_i\le0$, $g_i$ is finite away from $D_i$, and the normalized Poincaré–Lelong identity gives
\[
dd^cg_i=[D_i]-\omega_i.
\]
For every vector $\mathbf b=(b_1,\ldots,b_n)\in[0,1]^n$, define $u_{\mathbf b}=\sum_i b_i g_i$ and $\lambda_i=1-b_i$. Then $u_{\mathbf b}\in\operatorname{PSH}(X,\theta)$, $u_{\mathbf b}\le0$, and
\[
\theta_{u_{\mathbf b}}=
\sum_i b_i[D_i]+\sum_i\lambda_i\omega_i.
\]
On the complement of the (finite union of) polar divisors $D_i$ for which $b_i>0$, this current is the smooth semipositive form $\alpha_{\mathbf b}=\sum_i\lambda_i\omega_i$. The defining non-pluripolar truncation/locality rule restricts every mixed product to that complement and charges none of those divisors. Since a smooth form gives zero mass to a hypersurface, its extension by zero is the same smooth form globally. Thus, for every $0\le k\le n$,
\[
\big\langle\theta_{u_{\mathbf b}}^k\wedge\theta^{n-k}\big\rangle
=\alpha_{\mathbf b}^{\,k}\wedge\theta^{n-k}.
\]
This equality is for **non-pluripolar** products, not for the ordinary divisor-containing wedge; it follows directly in this explicit model and does not require a limit interchange.

Because $\omega_i^2=0$, forms on distinct factors commute, and $\int_X\omega_1\wedge\cdots\wedge\omega_n=1$, the full mixed-mass vector is
\[
a_k(\mathbf b)
=\int_X\big\langle\theta_{u_{\mathbf b}}^k\wedge\theta^{n-k}\big\rangle
=k!(n-k)!\sum_{\substack{I\subseteq\{1,\ldots,n\}\\|I|=k}}\prod_{i\in I}(1-b_i)
=k!(n-k)!\,e_k(1-b_1,\ldots,1-b_n).
\tag{1}
\]
In particular, the top mass is $a_n=n!\prod_i(1-b_i)$, hence vanishes as soon as any $b_i=1$.

For the exact positive-mass interpolation used in the printed Proposition 17.6.1, set
\[
w_{\varepsilon,\mathbf b}
=(1-\varepsilon)u_{\mathbf b}+\varepsilon V_\theta
=(1-\varepsilon)u_{\mathbf b},\qquad 0<\varepsilon<1.
\]
On the polar complement the residual form is
$\alpha_{\varepsilon,\mathbf b}
=\sum_i(1-(1-\varepsilon)b_i)\omega_i$.
The same direct calculation gives the **exact**, rather than merely asymptotic, mass:
\[
m_\varepsilon(\mathbf b)
=\int_X\langle\theta_{w_{\varepsilon,\mathbf b}}^n\rangle
=n!\prod_{i=1}^n\bigl(1-(1-\varepsilon)b_i\bigr).
\tag{2}
\]
Equivalently, substituting (1) into the Step 2 binomial expansion of §17.6 reproduces (2), providing a normalization check of all coefficients.

If precisely $r\ge1$ of the $b_i$ equal $1$ and all others are strictly smaller than $1$, then
\[
\lim_{\varepsilon\downarrow0}\varepsilon^{-r}m_\varepsilon(\mathbf b)
=n!\prod_{i:b_i<1}(1-b_i)>0.
\tag{3}
\]
Thus **each exact order $r=1,\ldots,n$ occurs while the unperturbed top non-pluripolar mass is identically zero**. Taking $b_i=1$ for $i\le r$ and $b_i=0$ otherwise yields the simplest closed formulas
\[
u_r=\sum_{i=1}^r g_i,\quad
a_k(u_r)=
\begin{cases}
k!(n-k)!\binom{n-r}{k},&0\le k\le n-r,\\
0,&n-r<k\le n,
\end{cases}
\qquad m_\varepsilon(u_r)=n!\varepsilon^r.
\tag{4}
\]
The last identity is a direct check on the $\varepsilon^na_0$ lower bound in the printed Step 2: the bound is sharp for $r=n$ and strictly suboptimal in its order for every $r<n$.

For clarity, on $X=\mathbf P^1\times\mathbf P^1$, $u_1=g_1$ and $u_2=g_1+g_2$ are ordered $u_2\le u_1$, have the **same zero top mass**, but the vectors $(a_0,a_1,a_2)$ are respectively $(2,1,0)$ and $(2,0,0)$. Their exact positive-mass interpolations are $2\varepsilon$ and $2\varepsilon^2$. By the printed mixed-mass preservation Proposition 16.21.2(3), their singularity envelopes cannot be equal: equality would force the mixed-mass vectors to coincide. This **last envelope-distinction step is conditional on that printed proposition**, not a new standalone verification of its general proof.

## Mathematical consequence and limitation

The $n+1$ entries of the mixed-mass vector in Definition 17.6.4 retain information that the top mass alone loses, and they exactly determine the entire interpolation polynomial in Proposition 17.6.1. A proposed replacement of the mixed-mass equalities by only the top-mass equality would fail to encode these different zero-mass types; on the surface the discrepancy already occurs at degree one.

This proves an explicit family of conditional diagnostic models and coefficient normalizations; **it does not refute Proposition 17.6.1, Definition 17.6.4, or Theorem 17.6.5**. The general envelope convergence, rooftop/relative comparison and mixed-mass preservation proofs are not transitively certified. No claim is made that the mixed-mass vector alone determines the entire singularity type. The example is distinct from the earlier one-dimensional sharp normalized-tail calculation: it gives a dimension-dependent hierarchy of possible vanishing orders and a full mixed-mass profile.

**Suggested correction:** no source statement needs correction. Add (1)–(4) as an optional example after the printed Step 2 to document the sharp range of mass-degeneration orders and explain why the zero-mass ceiling retains all mixed degrees. Any such body change belongs in a separately reviewable patch, not this audit branch.

**Affected dependents:** the mass polynomial/normalized-tail discussion in Proposition 17.6.1; the precise mixed-mass definition in §17.6.4; the conditional equality/ceiling argument in Theorem 17.6.5; general mixed non-pluripolar multilinearity (Proposition 13.2.6) and preservation by envelopes (Proposition 16.21.2(3)). No source/body or permanent tag was changed.

**Coverage accounting:** substantive new analytic/algebraic calculation for the selected Step 2 and the ceiling's exact hypotheses in **previously partially visited §17.6**. New first-visited numbered sections: **0**. Completely certified numbered sections: **0**. The actual current ToC still has 25 chapters and 747 numbered sections; this model does not certify its analytic upstream. Excluded Demailly approximation/regularization and dedicated Bergman, L2, Ohsawa–Takegoshi, multiscale-atlas and positivity-loss work remains **deferred-by-user**, not resolved or certified. No builds, tests, CI or site publishing.
