# Finite even-order degeneracy and smooth Hermitian Monge–Ampère nonuniqueness

- **Finding:** `POME-DEGENMA-ALL-EVEN-VANISHING-ORDERS-001`
- **Classification:** low / **verified conditional deduction** (an audit-only strengthening, **not** an error in the printed theorem; not a complete transitive proof-chain certification).
- **Review date:** 2026-11-19.
- **Main commit:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.
- **Integrated reading edition:** `docs/sections/uniqueness-for-degenerate-equations--quadratic-density-zeros/index.html`, blob `7a70517262563acf523940c261daa8ec11a8cb55`; directly inspected mathematical paragraphs **lines 7–157**, including both theorem, the coefficient construction, the ODE, its barriers and smooth extension, and the proof of uncountably many normalized solutions.
- **Stable source / permanent references:** Theorem 14.28.1 `non-kahler-pluripotential-theory:EC99526C` / `9C11A9E88B60` (lines 11–21); coefficient equation 14.28.2 `689AB380` / `ACD0920D4D78` (28–35); Lemma 14.28.3 `A5AC3FD9` / `624B2CF7FBA2` (65–75), ODE 14.28.4 `8FF0501E` / `3D1CCE4952BA` (66–95), factorization 14.28.5 `D95AB7A3` / `86148D5BD1E9` (97–116), and endpoint decay 14.28.6 `49BEBAB6` / `94F5CC68CD22` (116–134).
- **Directly inspected contextual dependencies:** `docs/sections/uniqueness-for-degenerate-equations--smooth-nonuniqueness-for-a-degenerate-density/index.html`, blob `7240d97e9192c70acf09f755ec90a5420bc11ef7`, lines 10–66 (rank-one forms and their normalized cubic); `docs/sections/non-pluripolar-monge-ampere-measures/index.html`, blob `5d0f652ffaaaef81cf74d1786082e429f71b3b89`, Proposition 13.14.15 lines 235–250 (bounded-mass invariance, **upstream proof not independently certified**).

## Theorem (audit-only strengthening)

For **every positive even integer** `m=2k >= 2`, there exist a smooth strictly positive nonclosed Hermitian form `omega_m` and a smooth nonnegative `g_m` on `X=P^3` such that:

1. `g_m` is positive outside two disjoint smooth real hypersurfaces `M_-, M_+`. In a neighborhood of each, `g_m = tau^m a`, where `tau` is a smooth signed defining function and `a` is smooth and strictly positive; in particular the **exact** transverse vanishing order is `m`.
2. `(omega_m+dd^c u)^3 = g_m omega_X^3` admits **uncountably many distinct smooth omega_m-psh solutions** normalized by `sup_X u=0`.
3. `omega_m` has the bounded-mass property, conditional only on the established projective/Kähler mass identities and Proposition 13.14.15 for the bounded-potential formulation.

The original Theorem 14.28.1 proves `m=2`; this theorem strengthens only the allowed order of the density zero. It does not claim uniqueness failure for closed/Kähler backgrounds, or results for an arbitrary given density.

## Proof

**1. Global geometric coefficients and exact zero order.** Use the original block-coordinate construction on `X=P(C^2\oplus C^2)` and `U={A != 0, B != 0}`:
`r=log(|A|^2/|B|^2)`, `P=dd^c log|A|^2`, `Q=dd^c log|B|^2`, and `R=dr\wedge d^c r`. The original identities
`P^2=Q^2=R^2=0`, `(xP+yQ+zR)^3=6xyz P\wedge Q\wedge R`,
`dd^c G(r)=G'(P-Q)+G''R` and
`omega_X=sigma P+(1-sigma)Q+sigma' R`, `sigma=e^r/(1+e^r)`,
are used without changing normalization.

Fix **even** `m>=2` and replace just `p=(1-r^2)^2` in (14.28.2) by
`p_m(r)=(1-r^2)^m`. Retain the same smooth `a,b,chi,kappa` from the printed proof and define
```
x=(1-chi)(p_m+a)+chi*sigma,
y=(1-chi)(p_m+b)+chi*(1-sigma),
z=1-chi+chi*sigma',
omega_0=xP+yQ+zR,
rho=epsilon*(r*r-1)*kappa(r),  omega_m=omega_0+dd^c rho.
```
Evenness ensures `p_m>=0` on **all** of `R`, not only on the central band. In `|r|>=3/2`, `chi=1`; hence `omega_0=omega_X` there and extends smoothly across both projective ends. The coefficients are positive away from `r=±1`, and at each hypersurface exactly one of `x,y` is zero and the other two are positive. Near `r=-1` they are `(1+p_m,p_m,1)`; near `r=+1`, `(p_m,1+p_m,1)`. The same compactness and sign argument of lines 38–47, now with `p_m`, makes `omega_m` positive for sufficiently small `epsilon>0`. At `r=0`, `x'=y'=0,z=1`; the printed formula for `d omega_m=d omega_0` is nonzero. Thus the background is Hermitian and nonclosed.

Set `g_m omega_X^3=omega_0^3`. The ratio of the rank-one cubic coefficients near either degeneracy hypersurface is exactly
```
g_m(r) = (1+p_m(r))*(1-r*r)^m / (sigma(r)*(1-sigma(r))*sigma'(r)).
```
Its denominator is smooth and positive at `±1`; `1-r^2` has simple normal zero there. The density therefore has **exact** order `m`, and has no other zeros.

**2. A family of trapped ODE solutions.** On `(-1,1)` solve
```
h'=F(r,h):=x*y*z/((x+h)*(y-h))-z,  h(0)=-eta.
```
The solution `h=0` is the reference. Fix any `0<c<1`. Since `p_m,p_m' -> 0` at each endpoint, the signed barrier residual for `h=-c*p_m` obeys
```
lim_(r -> -1+) [F(r,-c*p_m)+c*p_m'] = -c/(1+c) < 0,
lim_(r -> +1-) [F(r,-c*p_m)+c*p_m'] =  c/(1-c) > 0.
```
The explicit formulas are precisely the original lines 81–93 with `p_m` substituted; no coefficient of the leading residual changes. ODE continuous dependence on a fixed middle compact interval gives `eta_0>0` such that, for all `0<eta<eta_0`, the solution exists there, stays in `-x<h<y`, is strictly negative, and is above the barrier at both selected endpoints. ODE uniqueness prevents crossing `h=0`, while the strict residual signs prevent a first crossing of `-c p_m` **backwards** toward `-1` and **forwards** toward `+1`. In these endpoint collars, `-c p_m<=h<0`; these inequalities keep `x+h,y-h` positive and uniformly away from the ODE-domain boundary on every compact subinterval. The continuation theorem yields a solution on all of `(-1,1)`.

**3. Faster-than-polynomial endpoint flatness.** The exact algebraic factorization remains
```
h' = h L(r,h),  L=z*(x-y+h)/((x+h)*(y-h)).
```
For the trapped solution, the explicit endpoint triples above and `0<c<1` imply, after shrinking the collars,
`L(r,h)>=C_-/p_m(r)` near `-1` and
`L(r,h)<=-C_+/p_m(r)` near `+1`, for positive constants. Since `h<0`,
`(log(-h))'=L(r,h)`. Put `d=1-|r|`. As `p_m(r)\asymp d^m`,
```
int d^(-m) dd = d^(1-m)/(1-m),   m>1.
```
Backward integration on the left and forward integration on the right give
```
|h(r)| <= C exp(-A/d^(m-1)).
```
This bound holds with positive `A,C` depending on the individual solution. Along the trapped graph, the denominators in `L` are bounded below by a positive constant times `p_m` (and the other factor is positive and bounded below), so every mixed partial derivative of the rational function `L` has at most polynomial growth in `d^{-1}`. Differentiate `h'=hL(r,h)` inductively: for every `j>=0`,
```
|h^(j)(r)| <= C_j d^(-N_j) exp(-A/d^(m-1)).
```
All derivatives tend to zero at both endpoints; extending `h` by zero to `R` is `C^infty` and flat at `±1`. This is the printed proof's derivative induction with the **new exact decay exponent `m-1`**, rather than exponent 1.

**4. Smooth global solutions and bounded mass.** Choose any primitive `G_eta` of the extended `h_eta`; it is constant near either end and therefore `G_eta(r)` extends to `P^3`. Put `u_eta=G_eta(r)-rho`. On the band, by the chain rule,
```
omega_m+dd^c u_eta
=(x+h_eta)P+(y-h_eta)Q+(z+h_eta')R.
```
The first two coefficients are positive and the ODE gives
`z+h_eta'=xyz/((x+h_eta)(y-h_eta))>0`. At the endpoints and outside the band, the form agrees with semipositive `omega_0`. The rank-one cubic identity yields
`(omega_m+dd^c u_eta)^3=omega_0^3=g_m omega_X^3` globally. Distinct `eta` give distinct slopes at `r=0`, hence potentials different modulo constants; normalizing each by `sup_X u_eta` leaves an uncountable family.

Finally `omega_m<=C omega_X` on compact `X`; for each smooth `omega_m`-psh `v`, positivity and the Kähler Stokes identity bound
```
int_X (omega_m+dd^c v)^3
 <= C^3 int_X (omega_X+dd^c(v/C))^3
 = C^3 int_X omega_X^3.
```
The extension from smooth to all bounded admissible `v` is exactly the conditional use of Proposition 13.14.15; its proof includes a regularization input that is **not reopened in this audit**.

**5. Sharp parity observation.** If a smooth nonnegative density is positive on both sides of a smooth real hypersurface and has a finite, exact normal vanishing order `m` with nonzero leading coefficient, `m` must be even: an odd leading term changes sign on the two sides. Consequently the construction realizes **every possible positive finite order**, in the sense of such a smooth nonnegative transverse zero with smooth positive leading factor.

## Status, severity, correction and dependencies

- **Status:** verified conditional deduction / low severity. The original statement for quadratic zeros is correct; **no confirmed false theorem and no new missing proof step** are asserted.
- **Suggested correction:** optional new corollary/addendum after Theorem 14.28.1, replacing the exponent `2` by any positive even `m` and decay `exp(-A/d)` by `exp(-A/d^(m-1))`; retain all original permanent/source tags and all historical attribution. No body/registry/canonicalization edits were performed.
- **Affected mathematical scope:** extends the boundary of smooth nonuniqueness examples; it does **not** alter any printed theorem's hypotheses or conclusions. Relevant dependents concern uniqueness under degenerate densities in §§14.20–14.29.
- **Uncertified upstream inputs:** full §14.26 rank-one global geometry and all of Proposition 13.14.15's bounded-current approximation chain. Only the explicit used identities / statement were read. These are **not** labeled repaired/certified.
- **Excluded by user, unresolved:** Demailly approximation/regularization and Bergman, L2, Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof-completion programmes remain `deferred-by-user`; no work was done on them.
- **Coverage delta:** +1 **whole directly read section** (§14.28, mathematical lines 7–157); +0 full transitive dependency chains. The chapter/section matrix still has 25 chapters / 747 sections; an unknown historical first visit is **not** counted as a new first visit.
- **Execution:** mathematical reading and algebraic inequalities above; **no project tests, builds, GitHub Actions, publication, or source/registry/main edits**.
