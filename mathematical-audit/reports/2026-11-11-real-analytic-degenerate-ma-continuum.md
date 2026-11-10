# A full interval of smooth solutions for the fixed real-analytic degenerate Monge–Ampère density in §14.29

**Date:** 2026-11-11. **Finding:** `POME-DEGENMA-ANALYTIC-CONTINUUM-001` — **low / verified conditional deduction**. The printed Theorem 14.29.1 is **not false**. This is a stronger consequence of its exact coefficient construction; it is neither a proof of the general uniqueness theory nor a repair of the already recorded duplicated display (14.29.7). **Reviewed production main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.

## Exact integrated reading-edition anchors

- `docs/sections/uniqueness-for-degenerate-equations--a-real-analytic-density/index.html`, main blob `2f00a81edc49855971bb3a6d774603ee5bbf40db`: Theorem **14.29.1**, physical lines **10–20**, source `non-kahler-pluripotential-theory:3ADFF2BE`, permanent tag `DD001DBBE659`; the divided differences, `d_*`, and their positivity, lines **40–53**, equation 14.29.5 source `:D437FCA0`, tag `3FD3DD269BA8`; the flat bump, `x_b,y_b,z_b`, and strict positivity (x_b>p,y_b>p,z_b>|q|), lines **56–89**, equation 14.29.9 source `:67BD1F7C`, tag `025CE4264442`; equal product (14.29.10), lines **92–105**, source `:B91BE3E6`, tag `17DDFD1D68B2`; global extension, fixed positive background and two potential representatives, lines **108–165**, particularly equation 14.29.13 source `:BF19C5B7`, tag `1FC5DA40EAF0`. Section 14.29.4 has permanent tag `CB8BE6BADB1A`.
- `docs/sections/uniqueness-for-degenerate-equations--smooth-nonuniqueness-for-a-degenerate-density/index.html`, main blob `7240d97e9192c70acf09f755ec90a5420bc11ef7`: rank-one forms, cubic polarization and radial chain rule, §14.26.2 physical lines **23–64**; equation (14.26.4), source `:7BBBEE11`, tag `71DFC7D0861C`; equation (14.26.5), source `:99713047`, tag `1C52D8C53893`.
- `docs/chapters/monge-ampere-equations/index.html`: actual current chapter/section order, with §14.29 distinct from §§14.27–14.28.

## New strengthened statement

**Proposition (for the exact printed real-analytic model).** Keep **the same fixed smooth nonclosed Hermitian background** (omega=omega_0+dd^c\rho) on (X=\mathbb P^3) and **the same fixed globally real-analytic function**
[
f_*(t)=(t-a)^2(t-b)^2,qquad a=(1+e)^{-1},quad b=e(1+e)^{-1},
]
constructed in the proof of Theorem 14.29.1. Then
[
(omega+dd^cu)^3=f_*(t),omega_X^3,qquad sup_Xu=0
]
has **uncountably many pairwise distinct smooth (omega)-psh solutions**, not merely the two exhibited in the printed theorem. Their solution forms are strictly positive away from (M_-\cup M_+) and have rank two on (M_\pm=\{r=\pm1\}). No assumption on Demailly regularization is used.

### Proof, with the singular endpoint continuation justified

On the open band (I=(-1,1)) in the coordinate (r=log(|A|^2/|B|^2)), abbreviate the **printed** coefficients (x=x_b, y=y_b, z=z_b), the bump (p=e^{-1/(1-r^2)}), (q=p'), and the prescribed positive determinant product
[
d_*(r)=(1-r^2)^2H_*(r)^2.
]
The rank-one forms (P,Q,R) and the chain rule (14.26.5) imply that a radial potential (G(r)-\rho), whose slope is (h=G'), has solution form
[
A_h=(x+h)P+(y-h)Q+(z+h')R.
]
The equation (A_h^3=f_*(t)omega_X^3) is **equivalent in (I)** to the ordinary differential equation
[
h'=\mathcal F(r,h):=\frac{d_*(r)}{(x(r)+h)(y(r)-h)}-z(r),
qquad -x(r)<h<y(r).                                           	ag{1}
]
Both (h_+(r)=p(r)) and (h_-(r)=-p(r)) solve (1): this is exactly the **two equal-products identity (14.29.10)**. The displayed strict inequalities (x>p, y>p) on (I) ensure that ([-p(r),p(r)]) lies strictly inside the ODE domain.

For each (\lambda\in(-1,1)), solve (1) with the distinct initial datum (h_\lambda(0)=\lambda p(0)). Local existence and uniqueness hold because (\mathcal F) is smooth on the open domain. A solution cannot cross either of the two known solutions (\pm p). Thus
[
-p(r)<h_\lambda(r)<p(r)                                           	ag{2}
]
throughout its interval of existence. On each compact subinterval (J\Subset I), the two denominators in (1) are uniformly bounded below by (x-p>0) and (y-p>0); (2) therefore confines the solution to a compact subset of the ODE domain. The standard continuation theorem extends it **across every finite interior endpoint**. Hence (h_\lambda) exists smoothly on **all** (I), rather than just near (r=0).

It remains to check a critical point not supplied by ordinary interior ODE existence: **extension across the two degenerate hypersurfaces**. At (r=-1), the printed formulas give (x(-1)=1), (y(r)\asymp(r+1)^2), (z(-1)>0); at (r=1) they give (y(1)=1), (x(r)\asymp(r-1)^2), (z(1)>0). Indeed
[
xy=p^2+\tfrac12 z(1-r^2)^2,qquad x(-1)=y(1)=1,
]
and (z(\pm1)=\sqrt2H_*(\pm1)>0). Since (p) and all its derivatives are smaller than every power of the endpoint distance (\delta=1-|r|), all segments (\xi\in[-p(r),p(r)]) satisfy: **one** of (x+\xi,y-\xi) is bounded below by a positive constant, and the **other** is at least (c\delta^2).

Thus on these segments every fixed mixed partial derivative (\partial_r^j\partial_\xi^k\mathcal F(r,\xi)) is (O(\delta^{-N_{j,k}})) for some finite integer (N_{j,k}). Put (k_\lambda=h_\lambda-p). Subtract the equation for (p) from (1):
[
k_\lambda'=a_\lambda(r)k_\lambda,quad
a_\lambda(r)=\int_0^1 \partial_\xi\mathcal F(r,p+s k_\lambda)\,ds. 	ag{3}
]
Initially (|k_\lambda|\le 2p), so (k_\lambda=O(p)) is flat to order zero. Equation (3) and the derivative bounds show by induction that, for each (j\ge0),
[
|k_\lambda^{(j)}(r)|\le C_{j,\lambda}\,p(r)\delta^{-N_{j,\lambda}}.
]
For the induction, differentiate (3); derivatives of (a_\lambda) are finite combinations of derivatives of (\mathcal F), (p) and the previously controlled derivatives of (k_\lambda), and remain bounded by powers of (\delta^{-1}). Every derivative of (p) has the same flat-times-polynomial property. **All derivatives of (h_\lambda=p+k_\lambda) therefore tend to zero at both endpoints**. Extension by (h_\lambda=0) for (|r|\ge1) is (C^\infty), using the same elementary derivative-continuation argument as in the printed Lemma 14.27.7. No illegal interchange of singular limits is involved.

Let (G_\lambda(r)=\int_0^r h_\lambda(s)\,ds). It is smooth and constant on each tail (( -\infty,-1]) and ([1,\infty)), so the radial function extends smoothly across both omitted projective lines exactly as in §14.26.2. Define (\widetilde u_\lambda=G_\lambda(r)-\rho) globally. On (I), equation (1) gives (z+h_\lambda'=d_*/((x+h_\lambda)(y-h_\lambda))>0); the other two coefficients are positive by (2). The form is therefore **strictly positive in the band**. At the endpoints it agrees with (\omega_0), has complex rank two, and outside the band it equals the printed semipositive (\omega_0), strictly positive away from the zero levels. Its cube is the required (f_*(t)\omega_X^3) everywhere, by (1), (14.26.4), and continuity.

Normalize (u_\lambda=\widetilde u_\lambda-\sup_X\widetilde u_\lambda). The fixed background and the real-analytic density do not depend on (\lambda). Different (\lambda)'s give different slopes at (r=0) (as (p(0)>0)), so their potentials cannot differ by constants. This yields uncountably many normalized smooth solutions. \(\square\)

### Independent finite algebra check (not a replacement for the ODE proof)

Writing (A_\tau=\omega_0+\tau[p(P-Q)+qR]), the **printed** relations (x-y=-r), (q(xy-p^2)=-zrp), and ((x+p)(y-p)(z+q)=(x-p)(y+p)(z-q)=d_*) give for every (|\tau|\le1)
[
(x+\tau p)(y-\tau p)(z+\tau q)-d_*
=(1-\tau^2)p\big[p(z+\tau q)-rq\big]>0
quad\text{on }I\text{ when }|\tau|<1.
]
Here (rq=-2r^2p/(1-r^2)^2\le0) and (z>|q|). This **strict determinant surplus for naive linear interpolation** distinguishes the new nonlinear ODE solution continuum from a merely convex segment of the two printed solutions. The algebraic identity was independently sampled at several (r,\tau) values; numerical sampling is **not** used as proof.

## Classification, dependencies, and recommended editorial action

- **Status:** verified conditional deduction; **severity low** (strengthening, not a mathematical error); **no printed theorem refuted**. The ODE comparison/continuation, endpoint flatness and pairwise distinction are proved above. Global geometric construction of (P,Q,R,\rho,\omega_0) and the rank-one determinant identity are used exactly as printed in §§14.26 and 14.29 and have not been independently re-certified end to end.
- **Proposed correction:** add a *Corollary* after Theorem 14.29.1 asserting an uncountable family **for the same fixed analytic density and fixed Hermitian form**, with the ordered initial-slope ODE and endpoint flatness proof. Do **not** replace the original theorem or erase its historical attribution, tags, or provenance.
- **Affected dependents:** the introduction to uniqueness for degenerate equations (§14.20), Theorem 14.29.1 (strengthened, not repaired), and cross-comparisons with the weaker infinite-order density example §14.27 and quadratic smooth density example §14.28. Nothing in the proof implies uniqueness/nonuniqueness on closed Kähler backgrounds or extends to arbitrary analytic densities.
- **Coverage:** selected proof-level pass of §14.29.4–14.29.14 and §14.26.2. Already partly visited previously: **0 newly first-visited numbered sections**; **0 whole-section certifications**. Actual pinned table of contents: **25 chapters / 747 sections**.
- **Exclusions preserved:** Demailly regularization and the dedicated Bergman, L², Ohsawa–Takegoshi, multiscale-atlas and positivity-loss completion programmes remain **deferred-by-user**, neither revisited nor certified. No main/source/registry/tag edits, build, CI, website update or formal verification.
