# Moving point blow-ups: arbitrary nef b-divisor volume gaps invisible on fixed models

- **Date:** 2026-11-04.
- **Finding ID:** `POME-BDIV-MOVING-POINT-CONTINUUM-001`.
- **Severity/status:** low / **verified conditional deduction**. Not a false printed theorem, a new missing-proof allegation, or a complete certification of §20.1.
- **Reviewed production main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.
- **Integrated reading edition:** `docs/sections/the-theory-of-b-divisors/index.html`, blob `4a793dfd462badcb351f54a36cb030cde14a399b`, physical lines **57–119** and definition lines **123–129**.
- **Stable sources/permanent tags:** Definition 20.1.6 `sgpt:0B20B6FE` / `E6F6681E7170` (lines 57–62); Lemma 20.1.7 `sgpt:54FCB4C1` / `F5B2C1F1E318` (67–96); Equation 20.1.8 `sgpt:D44AA2EA` / `3BFB2E87E034` (68–70); Example 20.1.9 `sgpt:048A0D73` / `7AF528B0FB3B` (100–119); Definition 20.1.10 `sgpt:2D01378B` / `908967DFB37E` (123–125).
- **Actual new scope:** independently calculate arbitrary prescribed single-volume losses in all dimensions `n>=2`, including *positive-volume* terms, and identify the stronger finite-model exact-equality phenomenon. The printed example only covers `n=2` and a zero-volume sequence; other previously reviewed oscillation and intersection examples are not repeated or reclassified.

## Statement

Let `n>=2`, `X=P^n`, and `H=c_1(O(1))`, normalized by `H^n=1`. For each `c∈[0,1]` there exists a sequence `D_i^{(c)}` of **nef Cartier b-divisors** converging in the exact componentwise Euclidean topology of Definition 20.1.5 to the Cartier b-divisor `D(H)`, for which

```
vol(D_i^{(c)}) = c  for all i,     vol(D(H)) = 1.
```

For every *finite* set of fixed smooth modifications `rho_a:Y_a→X`, and every `c∈[0,1]`, one can moreover choose a single nef Cartier b-divisor `D^{(c)}` with `vol D^{(c)}=c` whose trace on **each** `Y_a` equals `rho_a^*H` exactly. Thus no finite family of model traces even detects the difference; the volume functional is upper semicontinuous, as the printed Lemma 20.1.7 says, but is not continuous at `D(H)` and can have any gap in `[0,1]`. The case `c=1` has gap zero. There is no analogue of this point-blow-up construction in dimension one.

## Direct construction, nefness and exact volume

Fix a point `p∈P^n`, let `pi_p:Bl_p X→X`, with exceptional divisor `E_p`, and for `0<=t<=1` put
`A_{p,t}=pi_p^*H-t[E_p]`. The class `pi_p^*H` is nef. So is `pi_p^*H-[E_p]`: the hyperplanes through `p` give a **basepoint-free** linear system on the blow-up (the resolved projection from `p` to `P^{n-1}`). Because
`A_{p,t}=(1-t)pi_p^*H+t(pi_p^*H-[E_p])`,
`A_{p,t}` is nef, and its Cartier b-divisor `D_{p,t}` is nef by Definition 20.1.11.

The volume is computed without an asserted polynomial-intersection formula. In affine coordinates at `p`, a degree-`k` homogeneous polynomial on `P^n` vanishes to order at least `m` at `p` exactly when it has no local monomial of total degree below `m`. For `0<=m<=k`,
```
h^0(Bl_p X, k pi_p^*O(1) ⊗ O(-m E_p))
  = binom(n+k,n) - binom(n+m-1,n).
```
(Here the second binomial is zero for `m=0`.) For rational `t`, take `k` divisible by its denominator and `m=kt`; the asymptotics of the binomial polynomials give volume `1-t^n`. For real `t`, take `m=ceil(kt)`; the same exact count and `m/k→t` give `1-t^n` by the real-divisor volume definition (or squeeze between rational `t` using monotonicity). On higher models, pullback does not change the volume, so Definition 20.1.6 yields
`vol D_{p,t}=1-t^n` (including `t=0,1`). Choose `t=(1-c)^{1/n}`.

## Finite-model invisibility, including all nonprojective smooth modifications

Let `rho_a:Y_a→X`, `a=1,...,r`, be finitely many fixed smooth proper modifications. Each is an isomorphism over the complement of a proper closed analytic subset `Z_a⊊X`. Choose `p∈X\setminus ⋃Z_a`. The common-model comparison of the blow-up `Bl_p X` with each `Y_a` is a blow-up at the unique point over `p` on `Y_a`, possibly after a common smooth resolution. The new exceptional class pushes forward to zero. The pushforward trace of `A_{p,t}` to `Y_a` is therefore exactly `rho_a^*H` for every `a`. No quantitative approximation is used in this step.

For a single sequence simultaneously handling *every* fixed model, choose affine-coordinate points `p_i` whose countably many complex coordinates are algebraically independent over `Q`. For each fixed `d`, the space of polynomials of degree at most `d` on `C^n` has dimension `N_d=binom(n+d,n)`. The evaluation matrix on *any* `N_d` of the `p_i` is invertible: its determinant is a polynomial over `Z` in the selected coordinates and is **not the zero polynomial**, since evaluation functionals over all points span the dual of the polynomial space. Algebraic independence makes this determinant nonzero. Hence no nonzero degree-`d` polynomial vanishes on `N_d` members of the sequence, and no proper algebraic subset of `P^n` contains infinitely many `p_i`.

For any fixed smooth modification `rho:Y→P^n`, the failure-of-isomorphism locus in `X` is proper closed analytic. By the **classical Chow algebraicity theorem** it is algebraic, and hence eventually avoided by `p_i`. The traces of `D_{p_i,t}` on `Y` are then precisely `rho^*H` for all sufficiently large `i`. This is convergence on each fixed model, *not* an assumption of countably many models or sequential compactness for arbitrary nets. The example is an explicit **sequence** within the general net topology. All terms have volume `1-t^n=c`, while the limit has volume `1`.

**External input accounting:** The only additional geometric input in the full all-model convergence argument beyond the Pome b-divisor definitions is Chow algebraicity of analytic subsets of projective space (and the standard fact that a proper bimeromorphic map is an isomorphism off a proper analytic set). The exact finite-model assertion and all section-count/nefness arguments do not use Chow. The internal birational invariance of line-bundle volume is used to identify the finite realization with its b-divisor volume. This note does **not** claim to replace or certify the general proof of Lemma 20.1.7 or of volume continuity for monotone nets.

## Disposition

- **Printed results:** Lemma 20.1.7 and Example 20.1.9 remain correct. The proof of upper semicontinuity and the monotone-net conclusion is consistent with the example.
- **New result:** arbitrary prescribed loss, including strict *positive*-volume losses, on a convergent sequence in every dimension `n>=2`; exact finite-model invisibility. It is a verified extension of a **previously partially audited** section, not a certification of that section.
- **Suggested nonproduction amendment:** after Example 20.1.9, mention `pi_p^*H-tE` with `vol=1-t^n` as the higher-dimensional and arbitrary-gap form; note that finitely many fixed traces cannot distinguish it from `H`.
- **Affected dependents:** Any use of Lemma 20.1.7 that upgrades `limsup vol D_i<=vol D` to equality for **nonmonotone** families, even with terms all big/nef Cartier, would need extra hypotheses. No such incorrect downstream invocation is asserted without tracing it.
- **Excluded scope:** Demailly approximation/regularization, Bergman, weighted L², Ohsawa–Takegoshi, multiscale atlas, and positivity-loss proof completion remain **deferred-by-user**.
