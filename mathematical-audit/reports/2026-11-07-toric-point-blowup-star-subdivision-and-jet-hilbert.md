# A toric point blowup: star subdivision, jet ideals, intersection form, and exact Hilbert count

**Finding:** `POME-TORIC-BLOWUP-STAR-SUBDIVISION-JETS-001` — **low / verified conditional deduction**. The printed toric statements tested below are **not refuted**. The explicit blowup and its intersection calculations are a new independent, non-product geometric model; this is not a repeat of the earlier Hirzebruch trapezoid, non-Delzant cone, or Laurent-series checks.

**Production main inspected:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. Integrated reading edition (not source numbers):

- `docs/sections/convex-analysis-and-toric-potentials--smooth-lattice-polytopes-and-projective-charts/index.html`, Git blob `f442a7b663689b97a9b89689b8b7ae8b366a53fe`: Lemma **21.8.2(4)**, `foundations-of-pluripotential-theory:86BADE82` / permanent `41C54729DBFD`, physical lines **24–61, 87–105**; Theorem **21.8.3**, source `foundations-of-pluripotential-theory:0F7315B0` / permanent `E49F0370E203`, lines **107–142** (chart construction and its stated hypotheses).
- `docs/sections/convex-analysis-and-toric-potentials--fans-divisors-and-character-sections/index.html`, Git blob `7ad2e6dbdd0ce59e1bf08cd9cb3c046e8c87ff6c`: Proposition **21.9.1** source `foundations-of-pluripotential-theory:4C5E5EB3` / permanent `9FD0EEED0DBF`, lines **10–32**; Proposition **21.9.2** source `foundations-of-pluripotential-theory:86CCC496` / permanent `7B4A7CC50CDC`, lines **34–67**; Proposition **21.9.3**, source `foundations-of-pluripotential-theory:43543C56` / permanent `C62B8871AA1C`, lines **69–106**; Theorem **21.9.5**, source `foundations-of-pluripotential-theory:BD98CC5B` / permanent `69D3D97E7701`, lines **138–166**, especially the facet support function, character sections, and inverse-weight convention.

## Exact claim and hypotheses

Let `M=Z^2`, take integers `d>ell>0`, and put
\[
P_{d,\ell}=\{(p,q)\in\mathbb R^2:p,q\ge0,\quad \ell\le p+q\le d\}.
\]
This is a two-dimensional **smooth lattice polytope**, not merely a simple polytope. Its associated projective toric surface `X_P` is the blowup `B=Bl_{[0:0:1]}(P^2)`. If `H` is the pullback of a line avoiding the center and `E` is the exceptional curve, then the polytope line bundle is `L=dH-ell E`; for every integer `k>=0`,
\[
H^0(B,L^k)=\operatorname{span}\{X^pY^qZ^{kd-p-q}:
p,q\in\mathbb Z_{\ge0},\ k\ell\le p+q\le kd\}.
\]
interpreted as plane degree-`kd` forms vanishing to order at least `k ell` at the blown-up point. The displayed monomials are linearly independent, and
\[
h^0(B,L^k)=\binom{kd+2}{2}-\binom{k\ell+1}{2}
=\frac{d^2-\ell^2}{2}k^2+\frac{3d-\ell}{2}k+1.
\]
The invariant boundary gives `-K_B=3H-E`, `H^2=1`, `H.E=0`, `E^2=-1`, and
\[
L^2=d^2-\ell^2,\qquad (-K_B)\cdot L=3d-\ell,\qquad
L\cdot E=\ell,\quad L\cdot(H-E)=d-\ell.
\]
In particular `2 area(P)=L^2`, and the entire linear Hilbert coefficient is `(1/2)(-K_B).L=(3d-ell)/2`, independently of a general asymptotic lattice-count theorem.

## Direct proof

**(1) Delzant/fan check.** The four vertices are `(ell,0),(d,0),(0,d),(0,ell)`. The primitive inward facet normals, in cyclic order, are
\[
(0,1),\quad (-1,-1),\quad (1,0),\quad (1,1).
\]
The support constants in `p>=0,q>=0,d-p-q>=0,p+q-ell>=0` are respectively `0,0,d,-ell` for rays `(1,0),(0,1),(-1,-1),(1,1)`. At each vertex the two primitive edge vectors form a basis of `Z^2`; for example at `(ell,0)` they are `(1,0),(-1,1)`, and at `(0,ell)` they are `(0,1),(1,-1)`. The other two vertices have edge bases `(-1,0),(-1,1)` and `(0,-1),(1,-1)` up to order. Every determinant has absolute value one. The fan rays are exactly the three rays of `P^2` together with the inserted ray `(1,1)=(1,0)+(0,1)`, subdividing its positive first quadrant.

**(2) Explicit blowup charts, rather than an unexplained toric equivalence.** On the dense torus use `x=X/Z=chi^(1,0)`, `y=Y/Z=chi^(0,1)`. The §21.8.3 chart at `(ell,0)` has coordinates `u=x`, `t=y/x`, and its map to the plane chart `Z!=0` is `(u,t) -> (x,y)=(u,ut)`. The chart at `(0,ell)` has `s=x/y`, `v=y`, mapping `(s,v)->(x,y)=(sv,v)`. On the overlap, `s=1/t` and `v=ut`, and the exceptional curve is `u=0` or `v=0`; it is `P^1`. These are exactly the two standard charts of the blowup of the origin in `A^2`. The remaining two vertex charts coincide with the usual plane charts off the center. The toric maps therefore glue to the global blowup, without importing a resolution theorem.

The transition of the normal coordinates along `E` is `v=t u` over `s=1/t`; this is the transition of the tautological line `O_{P^1}(-1)`. Hence `N_{E/B}=O_E(-1)` and `E^2=-1`. A generic line avoiding the center has class `H`, is disjoint from `E`, and meets another generic such line in one point: `H.E=0`, `H^2=1`.

**(3) Divisor and section identification.** By the explicit facet-order formula of §21.9.2, the invariant divisors for rays `(1,0),(0,1),(-1,-1),(1,1)` are respectively the strict transforms of `X=0`, `Y=0`, `Z=0`, and the exceptional curve `E`. Their classes are `H-E,H-E,H,E`. The support constants give `D_P=dD_{(-1,-1)}-ell D_{(1,1)}=dH-ell E`, exactly the divisor of the meromorphic frame in §21.9.5. A plane monomial `X^pY^qZ^{kd-p-q}` of degree `kd` has vanishing order `p+q` at `[0:0:1]`. Its strict transform is a section of `k(dH-ell E)` precisely when `p+q>=k ell`. Conversely, the §21.9.5 Laurent coefficients are constrained by the four facet inequalities `p,q>=0`, `p+q<=kd`, `p+q>=k ell`, so there are no other global sections. The dual linearization acts on the `chi^m s_0^k` line by `chi^{-m}` as written in the theorem; one must not replace this by the natural action on functions.

**(4) Exact counting and canonical crosscheck.** Degree-`kd` homogeneous monomials form a set of cardinality `binom(kd+2,2)`. Those with `p+q<k ell` have cardinality `sum_{j=0}^{k ell-1}(j+1)=binom(k ell+1,2)`. Their difference gives the asserted polynomial (also at `k=0`, where the excluded sum is empty). The Euclidean area is that of the triangle `p,q>=0,p+q<=d` minus the triangle `p,q>=0,p+q<ell`, namely `(d^2-ell^2)/2`. The four lattice edge lengths sum to `2(d-ell)+d+ell=3d-ell`.

The logarithmic meromorphic two-form `dx/x wedge dy/y` has, in each unimodular toric chart, one simple pole along each coordinate boundary and no other zero or pole, because a unimodular monomial change of variables multiplies its logarithmic wedge by determinant `+1` or `-1`. Thus `-K_B` is the sum of the four invariant divisors, namely `(H-E)+(H-E)+H+E=3H-E`. Combining this with the intersection numbers of (2) proves the identities and matches the exact quadratic and linear coefficients; no use of Hirzebruch–Riemann–Roch is needed to establish the count.

**(5) Essential full-dimensionality wall.** At `ell=0` the fourth inequality is redundant: the toric construction yields `P^2`, with no exceptional ray. At `ell=d>0` the polytope collapses to the segment `p+q=d`. Its character map factors through the one-dimensional quotient torus with coordinate `x/y`, and its closure is the degree-`d` rational normal curve `P^1` (not the blowup surface); in degree `k`, it has `kd+1` characters. The collapse illustrates why the **nonempty interior** hypothesis in §21.8 is indispensable. It does not contradict either §21.8.3 or §21.9.5, which work in the smooth full-dimensional setting.

## Audit judgment and dependency boundaries

**Status:** verified conditional deduction, low severity; **neither a false theorem nor a claimed full proof of the general toric theory**. The local charts, monomial selection, counts and divisor classes are explicit. Identification with the *integrated* general projective construction uses its stated vertex-monomial chart and character-divisor rules (§§21.8.3, 21.9.2, 21.9.5); their entire higher-dimensional dependency chains are not recertified. The old `POME-TORIC-ACTION-INVERSE-INFERENCE-001` proof-exposition issue remains distinct and unchanged. No source/body/canonicalization patch is required; this report documents the sharp role of full dimension and the inserted exceptional fan ray. Affected dependents: §21.9.5 normalized volume/character statements, §21.8.3 smoothness hypothesis, and geometric intersection interpretation of the toric polarization. The earlier §21.7 lattice asymptotic is only checked here through an exact special-family count.

**Scope:** selected portions only of §§21.8–21.9. No whole section certified, no CI/build/formal verification/publication, and no excluded Demailly-regularization/Bergman/L2/OT/multiscale/positivity-loss proof programme reopened.
