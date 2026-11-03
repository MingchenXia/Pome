# Independent selected mathematical audit: transverse divisors and non-pluripolar mixed mass (2026-11-04)

**Finding ID:** POME-NPP-TRANSVERSE-DIVISORS-MIXED-PERMANENT-001  
**Severity:** low. **Status:** verified conditional deduction (sharp explicit model; no false printed theorem, no general theorem certification).  
**Reviewed production main:** b6933b772f41b45918f7e25ed1afbbb1fd892272.

## Exact inspected statements and anchors

1. Integrated **13.2**, docs/sections/non-pluripolar-products--truncation-and-plurifine-locality/index.html, main blob 81be8c5acc360c96bd3c5acba05a3cdb5fafaf4c: the actual truncated-current definition, physical lines 7–13; Lemma 13.2.2, source foundations-of-pluripotential-theory:CE1D6DA5, permanent D59675D9F6D8, lines 34–52 (especially polar-zero limit); Definition 13.2.4, source foundations-of-pluripotential-theory:9D8E4DD8, permanent D79952D7E272, lines 57–63; Proposition 13.2.6, source foundations-of-pluripotential-theory:E82F0D73, permanent 7F7123F92478, lines 80–85, 90–115 (locality and multilinearity).
2. Integrated **13.5**, docs/sections/non-pluripolar-products--global-finiteness-and-bounded-cohomological-mass/index.html, main blob 943517743538820940559eae8469ce98ecf5fcd5: Theorem 13.5.4, source foundations-of-pluripotential-theory:A00627D3, permanent 3783DE0B4D00, lines 84–90 (global finiteness and cohomological bound); Example 13.5.6, source foundations-of-pluripotential-theory:D71F11C5, permanent 3D09B5B530AA, lines 123–125 (a one-dimensional polar atom); Proposition 13.5.8, source foundations-of-pluripotential-theory:13A73596, permanent A93A2F4C95C2, lines 132–141 (mixed **lower**, not upper, bound from diagonal densities).

These are already partly inspected sections in the coverage matrix. This increment is a *new two-dimensional transverse-pole and general-dimensional permanent model*, not the old one-dimensional isolated-pole example, old power-log thresholds, or a rereading/certification of the general proofs.

## Model, exact hypotheses, and full calculation

Take $X=(\mathbf P^1)^n$, $n\ge 2$, with projections $\pi_i$ and normalized Fubini–Study forms $\omega_i=\pi_i^*\omega_{\rm FS}$, where $\int_{\mathbf P^1}\omega_{\rm FS}=1$ and
$$
\theta=\sum_{i=1}^n\omega_i,\qquad \int_X\theta^n=n!.
$$
Let $D_i=\pi_i^{-1}(\{0\})$. In the affine coordinate $z_i$ write
$$
g_i=\log\frac{|z_i|^2}{1+|z_i|^2},
$$
understood as a global extended-valued function on the $i$th projective line; at infinity it extends smoothly with value zero, and at zero it equals $-\infty$. With the Pome convention $dd^c=\frac{i}{2\pi}\partial\bar\partial$, the Poincaré–Lelong identity reads
$$
dd^c g_i=[D_i]-\omega_i.
$$
Consequently, for any real matrix $A=(a_{ji})_{1\le j,i\le n}$ with $0\le a_{ji}\le1$, the global functions and currents
$$
u_j=\sum_{i=1}^n a_{ji}g_i,\qquad
T_j=\theta+dd^c u_j
=\sum_{i=1}^n\big((1-a_{ji})\omega_i+a_{ji}[D_i]\big)
$$
satisfy $u_j\in\operatorname{PSH}(X,\theta)$ and $T_j\ge0$, all with the same Kähler cohomology class $[\theta]$. In particular, the weight coefficients are nonnegative, so there is no implicit subtraction of positive divisors.

Put $I=\{i:\exists j,\ a_{ji}>0\}$ and $Z=\bigcup_{i\in I}D_i$. This is precisely the union of the pole sets of $u_1,\dots,u_n$ (discarding indices of zero coefficient). On $X\setminus Z$, all $u_j$ are smooth, and
$$
T_j\big|_{X\setminus Z}=\sum_i(1-a_{ji})\omega_i.
$$
For each cutoff level, the defining indicator set $\bigcap_j\{u_j>-k\}$ is disjoint from $Z$. Local Bedford–Taylor agreement therefore identifies each non-pluripolar product off $Z$ with the ordinary wedge of the displayed smooth forms. Theorem 13.5.4 supplies local/global finiteness on compact Kähler $X$, while Lemma 13.2.2 ensures that its limit charges no pluripolar set, in particular no component or intersection of $Z$. Thus the product is precisely the zero extension of that smooth wedge from $X\setminus Z$. The smooth wedge itself gives no mass to the divisor set $Z$, so it extends unchanged to all of $X.

On $(\mathbf P^1)^n$ one has $\omega_i^2=0$ and degree-two forms commute. Expanding, **only permutations of the distinct coordinate forms survive**. Hence the following identity of measures, not merely of total masses:
$$
\boxed{\ \left\langle T_1\wedge\cdots\wedge T_n\right\rangle
=\operatorname{perm}(B)\,\omega_1\wedge\cdots\wedge\omega_n,\quad
B_{ji}=1-a_{ji},\quad
\operatorname{perm}(B)=\sum_{\sigma\in S_n}\prod_{j=1}^n B_{j,\sigma(j)}.\ }
$$
Since the product of the normalized coordinate Fubini–Study forms has integral one, its coefficient is exactly the total non-pluripolar mixed mass. If all $T_j=T_{\mathbf a}$ with the same vector $\mathbf a=(a_i)$, each of the $n!$ summands equals $\prod_i(1-a_i)$, giving
$$
\boxed{\ \int_X\langle T_{\mathbf a}^n\rangle=n!\prod_{i=1}^n(1-a_i).\ }
$$
The cohomological bound $n!$ is sharp for all $a_i=0$, but may be strictly smaller (or zero) for fixed nonzero divisorial weights; no mass has been assigned to the pluripolar divisor strata or their intersections.

## Two-dimensional strict-mixed example

For $n=2$ take the positive closed currents
$$
T=\omega_2+[D_1],\qquad S=\omega_1+[D_2],\qquad
\theta=\omega_1+\omega_2.
$$
They are represented by the respective $\theta$-psh potentials $g_1$ and $g_2$. The *own* non-pluripolar Monge–Ampère measures vanish:
$$
\boxed{\langle T^2\rangle=0,\qquad \langle S^2\rangle=0,}
$$
as their smooth remainders off the poles have rank one and squares $\omega_2^2=\omega_1^2=0$. Nevertheless,
$$
\boxed{\langle T\wedge S\rangle=\omega_1\wedge\omega_2,\qquad
\int_X\langle T\wedge S\rangle=1.}
$$
Thus it is **false** that vanishing of the two individual non-pluripolar top products forces their mixed non-pluripolar product to vanish, or that their own top masses yield a general upper estimate on the mixed mass that vanishes with those masses. Neither strengthening is printed in Pome.

For a continuously varying version, let
$$
T_a=(1-a)\omega_1+\omega_2+a[D_1],\quad
S_a=\omega_1+(1-a)\omega_2+a[D_2]\quad(0\le a\le1).
$$
Directly from the same determinant-permanent calculation,
$$
\int_X\langle T_a^2\rangle
=\int_X\langle S_a^2\rangle=2(1-a),\qquad
\int_X\langle T_a\wedge S_a\rangle=1+(1-a)^2.
$$
The mixed mass exceeds either diagonal top mass by exactly $a^2$. The mixed-lower-bound Proposition 13.5.8 is entirely consistent: when $a=1$, its diagonal lower-density inputs are zero, so it gives the trivial *lower* bound $0$ rather than an upper bound. This also distinguishes the present model from §13.5.6, which checks only a pure divisor current on $\mathbf P^1$.

## Audit verdict, dependence and action

**Verdict:** the printed 13.2.2/13.2.4/13.2.6, 13.5.4, 13.5.6 and 13.5.8 are not refuted. The new permanent formula is a verified conditional deduction based on the identified internal non-pluripolar cutoff/locality and compact finiteness theorems, Poincaré–Lelong, and elementary Fubini–Study cohomology; it is **not** a self-contained certification of those upstream general theorems. No potentially illegitimate wedge of divisor currents, no Dirac-atom self-intersection, and no interchange of cutoff and weak limit is used. In particular, the classical intersection current $[D_1]\wedge[D_2]$ is **not** silently substituted for the non-pluripolar product.

**Suggested correction/addition (not applied):** a short explicit example after Example 13.5.6 illustrating the $n=2$ zero-own-mass/positive-mixed-mass phenomenon and emphasizing that Proposition 13.5.8 is a lower-bound assertion. This is documentation, not a theorem repair. **Affected dependents:** interpretation of mixed-mass inequalities in §13.5 and applications of product truncation in §§13.2/13.7; no printed dependent has been shown false.

**Actual coverage:** direct new normal-crossing product model for §§13.2,13.5, selected source lines above only; the local-to-global theorem proof, cohomological finiteness proof, capacity theory, and the entire two sections are **not certified**. The main table of contents is 25 chapters / 747 numbered sections / zero fully certified mathematical sections. Existing confirmed errors/gaps/externals unchanged. Demailly approximation/regularization and dedicated Bergman, weighted $L^2$, Ohsawa–Takegoshi, multiscale atlas, positivity-loss proof completion remain **deferred-by-user and unexamined**. Audit Markdown only; no production/main/source/tags/registry/CI/build/site changes.
