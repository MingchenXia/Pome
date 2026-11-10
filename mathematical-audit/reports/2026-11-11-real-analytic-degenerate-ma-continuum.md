# An uncountable smooth solution family for one fixed real-analytic degenerate Monge–Ampère density

**Date:** 2026-11-11. **Finding ID:** POME-DEGENMA-ANALYTIC-CONTINUUM-001. **Severity:** low. **Status:** verified conditional deduction. The printed Theorem 14.29.1 is **not refuted**. This strengthens its explicit construction; it is not a verification of the full degenerate Monge–Ampère theory.

**Reviewed production main:** b6933b772f41b45918f7e25ed1afbbb1fd892272.

## Integrated sources and stable anchors

1. **The actual §14.29 reading edition:** docs/sections/uniqueness-for-degenerate-equations--a-real-analytic-density/index.html, main blob 2f00a81edc49855971bb3a6d774603ee5bbf40db. Theorem **14.29.1**, source non-kahler-pluripotential-theory:3ADFF2BE, permanent tag DD001DBBE659, physical lines **10–20**. Prescribed determinant and divided differences, lines **40–53**, equation (14.29.5), source non-kahler-pluripotential-theory:D437FCA0, tag 3FD3DD269BA8. Bump and three coefficients, lines **56–89**, in particular equation (14.29.9), source non-kahler-pluripotential-theory:67BD1F7C, tag 025CE4264442. Equal-product identity (14.29.10), lines **92–105**, source non-kahler-pluripotential-theory:B91BE3E6, tag 17DDFD1D68B2. Global extension and strictly positive Hermitian background, lines **108–165**; correction equation (14.29.13), source non-kahler-pluripotential-theory:BF19C5B7, tag 1FC5DA40EAF0. Section heading 14.29.4, permanent tag CB8BE6BADB1A.
2. **The actual §14.26 reading edition:** docs/sections/uniqueness-for-degenerate-equations--smooth-nonuniqueness-for-a-degenerate-density/index.html, main blob 7240d97e9192c70acf09f755ec90a5420bc11ef7. Rank-one forms and their wedge calculation, physical lines **23–49**, in particular equation (14.26.4), source non-kahler-pluripotential-theory:7BBBEE11, permanent tag 71DFC7D0861C. Radial Hessian formula (14.26.5), lines **52–57**, source non-kahler-pluripotential-theory:99713047, permanent tag 1C52D8C53893.
3. The main table of contents in docs/chapters/monge-ampere-equations/index.html confirms §§14.26–14.29 are separate. In the previous 2026-11-07 audit, the inverse-ellipticity threshold and infinite flat jets in §14.29 were checked separately; the duplicate rendered equation (14.29.7) remains a different, already recorded finding.

## Strengthening of the printed theorem

**Proposition (for the explicit model in Theorem 14.29.1).** On $X=\mathbb P^3$, keep the **same fixed smooth nonclosed Hermitian background**
$$
\omega=\omega_0+dd^c\rho
$$
and the **same fixed globally real-analytic density**
$$
f_*(t)=(t-a)^2(t-b)^2,\qquad
a=\frac1{1+e},\qquad b=\frac e{1+e}.
$$
Then
$$
(\omega+dd^c u)^3=f_*(t)\,\omega_X^3,\qquad \sup_X u=0
$$
has **uncountably many pairwise distinct smooth $\omega$-plurisubharmonic solutions**, rather than only the two explicit solutions originally exhibited. Their forms are positive definite off the two real hypersurfaces $M_\pm=\{r=\pm1\}$ and have complex rank two on $M_\pm$. The theorem is a conditional strengthening using the printed global geometric construction, **not** a new theorem for arbitrary analytic densities.

### Step 1. Scalar determinant equation and two barriers

On $U=\{A\ne0,\ B\ne0\}\subset\mathbb P^3$, define
$$
r=\log\frac{|A|^2}{|B|^2},\quad
P=dd^c\log|A|^2,\quad Q=dd^c\log|B|^2,\quad
R=dr\wedge d^c r.
$$
The rank-one forms satisfy $P^2=Q^2=R^2=0$ and
$$
(xP+yQ+zR)^3=6xyz\,P\wedge Q\wedge R.
$$
For the coefficients in §14.29.4, abbreviate $x=x_b$, $y=y_b$, $z=z_b$, and set
$$
p(r)=e^{-1/(1-r^2)}\quad(-1<r<1),\qquad
q=p',\qquad d_*(r)=(1-r^2)^2 H_*(r)^2.
$$
The printed coefficient formulas imply
$$
x>p,\qquad y>p,\qquad z>|q|\qquad\text{on }(-1,1),
$$
and the determinant identity (14.29.10) states
$$
(x+p)(y-p)(z+q)=(x-p)(y+p)(z-q)=d_*.
$$
For any radial potential $G(r)-\rho$ with slope $h=G'$, the radial Hessian formula (14.26.5) yields
$$
\omega+dd^c(G-\rho)
=(x+h)P+(y-h)Q+(z+h')R.
$$
Its determinant equals $f_*(t)\omega_X^3$ exactly if
$$
h'=\mathcal F(r,h):=
\frac{d_*(r)}{(x(r)+h)(y(r)-h)}-z(r),
\qquad -x(r)<h<y(r).
\tag{1}
$$
By the equal-product identity, **both** $h_+=p$ and $h_-=-p$ solve (1) on $I=(-1,1)$.

### Step 2. Continuum of ordered solutions and global interior continuation

Choose $\lambda\in(-1,1)$ and solve (1) with
$$
h_\lambda(0)=\lambda p(0).
$$
The right-hand side is smooth on its open domain. Uniqueness for scalar ODEs prevents $h_\lambda$ from crossing either solution $\pm p$, so throughout its maximal existence interval
$$
-p(r)<h_\lambda(r)<p(r).
\tag{2}
$$
Given a compact subinterval $J\Subset I$, the strict inequalities $x>p$ and $y>p$ are uniform on $J$. The closed order interval $-p\le h\le p$ over $J$ is thus a compact subset of the domain of the ODE. Standard continuation at a finite interior endpoint extends the solution beyond it. Hence (2) holds for a **smooth solution on the entire interval** $(-1,1)$.

### Step 3. Smooth extension at both degenerate zero hypersurfaces

A key point is that solving the ODE on the open interval does **not** by itself prove smoothness at $r=\pm1$. From the *actual printed* coefficients,
$$
xy=p^2+\tfrac12 z(1-r^2)^2,\qquad
(x(-1),y(-1))=(1,0),\qquad
(x(1),y(1))=(0,1),
$$
and $z(\pm1)=\sqrt{2}\,H_*(\pm1)>0$. Since $p$ (and all its derivatives) vanishes faster than every power of the endpoint distance $\delta=1-|r|$, the rationalization of $x,y$ gives
$$
y(r)\asymp(r+1)^2\quad (r\to-1),\qquad
x(r)\asymp(r-1)^2\quad (r\to1).
$$
The other one of $x,y$ stays uniformly positive at each endpoint. Uniformly for all $|\xi|\le p(r)$, one of $x+\xi$, $y-\xi$ is bounded below by a fixed positive constant and the other by $c\delta^2$. All coefficient derivatives are bounded there, while every mixed derivative of the reciprocal denominator is bounded by a finite power of $\delta^{-1}$. Consequently, for every fixed nonnegative integers $j,k$,
$$
\sup_{|\xi|\le p(r)}
|\partial_r^j\partial_\xi^k\mathcal F(r,\xi)|
\le C_{jk}\delta^{-N_{jk}}.
\tag{3}
$$
Put $k_\lambda=h_\lambda-p$. Subtract the scalar ODEs for $h_\lambda$ and $p$:
$$
k_\lambda'=a_\lambda(r)k_\lambda,\qquad
a_\lambda(r)=\int_0^1
\partial_\xi\mathcal F(r,p+s k_\lambda)\,ds.
\tag{4}
$$
The trapping bound gives $|k_\lambda|\le2p$. Differentiate (4) inductively. Formula (3), the chain rule, the fact that every derivative of $p$ equals $p$ times an at-most-polynomially blowing-up factor, and the already established derivative estimates imply
$$
|k_\lambda^{(j)}(r)|
\le C_{j,\lambda}\,p(r)\delta^{-N_{j,\lambda}}
\quad\text{for all }j\ge0.
\tag{5}
$$
To spell out the induction: for $j=0$ use the trapping estimate; when differentiating (4) $j$ times, derivatives of $a_\lambda$ involve derivatives of $\mathcal F$ bounded by (3), derivatives of $p$, and derivatives of $k_\lambda$ of order at most $j$, all controlled by the induction hypothesis. This bounds the $(j+1)$-st derivative by $p$ times a power of $\delta^{-1}$.

Every right-hand side of (5) tends to zero as $\delta\downarrow0$. Hence every derivative of $h_\lambda=p+k_\lambda$ extends continuously by zero at $r=\pm1$. The usual elementary derivative-extension argument (compare the printed Lemma 14.27.7, lines 124–171 of its own section) proves that the function equal to $h_\lambda$ on $(-1,1)$ and zero outside is $C^\infty(\mathbb R)$ and **infinitely flat at both endpoints**.

### Step 4. Global smooth solutions and pairwise distinctness

Take a primitive
$$
G_\lambda(r)=\int_0^r h_\lambda(s)\,ds.
$$
It is smooth and constant on each tail $(-\infty,-1]$ and $[1,\infty)$, so the associated radial function extends over the two omitted projective lines, exactly as noted at §14.26.2, lines 65–66. Define
$$
\widetilde u_\lambda=G_\lambda(r)-\rho.
$$
On the band, the first two coefficients of its form are strictly positive by (2), while equation (1) gives
$$
z+h_\lambda'=\frac{d_*}{(x+h_\lambda)(y-h_\lambda)}>0.
$$
Thus $\omega+dd^c\widetilde u_\lambda$ is positive definite on the band. On the endpoints it equals $\omega_0$, of rank two; outside the band it equals the printed $\omega_0$, positive definite away from those endpoints. The wedge identity from §14.26.2 and (1) prove
$$
(\omega+dd^c\widetilde u_\lambda)^3
=f_*(t)\,\omega_X^3
$$
on the band, and by continuity on all of $X$. The **same** background $\omega$ and density $f_*$ were used for every $\lambda$.

Normalize
$$
u_\lambda=\widetilde u_\lambda-\sup_X\widetilde u_\lambda.
$$
Distinct $\lambda$ give different first derivatives $h_\lambda(0)=\lambda p(0)$, with $p(0)>0$, so the resulting potentials cannot differ by constants. There are continuum-many choices of $\lambda$, completing the proof.

### Separate exact algebra check: affine interpolation is *not* the answer

For $|\tau|\le1$, the naive interpolation of the printed two solution forms has coefficient product
$$
(x+\tau p)(y-\tau p)(z+\tau q).
$$
Using the printed identities $x-y=-r$ and $q(xy-p^2)=-zrp$, direct expansion yields
$$
(x+\tau p)(y-\tau p)(z+\tau q)-d_*
=(1-\tau^2)p\bigl[p(z+\tau q)-rq\bigr].
\tag{6}
$$
On the interior $p>0$, $z>|q|$ and $rq=-2r^2p/(1-r^2)^2\le0$. Thus the right-hand side is **strictly positive** whenever $|\tau|<1$. Hence the continuum of exact solutions above genuinely uses the nonlinear ODE; merely taking convex combinations of two solutions does not preserve their common determinant. This is an exact finite calculation, not a numerical test.

## Classification and dependent claims

**Status:** verified conditional deduction, **low**. Theorem 14.29.1 is correct as stated; its two original solutions were explicitly constructed. The strengthening shows that the **same fixed equation** admits an uncountable smooth family. The scalar ODE comparison, interior continuation, flat endpoint limits and distinctness are proved here. The global algebraic-geometric forms $P,Q,R$, the fixed smooth metric $\omega$, and their projective extension are used from the actual integrated §§14.26 and 14.29; their **entire independent upstream verification is not claimed**.

**Proposed editorial change:** an optional corollary after Theorem 14.29.1 with this ordered-ODE proof, retaining all historical attribution, source labels and permanent tags. No source/body/registry/canonicalization edits were made.

**Affected dependents:** the §14.20 introductory distinction between closed/degenerate uniqueness and nonclosed examples; §§14.27–14.29 as cross-comparisons of open-band, smooth quadratic and analytic quadratic density zeros. No conclusion for arbitrary analytic densities or closed Kähler backgrounds follows.

**Exact coverage:** selected proof-level audit of §14.29 coefficient identities and global assembly and §14.26 radial calculation; both previously partially reviewed. **0 newly first-visited numbered sections; 0 whole-section mathematical certifications**; pinned main TOC **25 chapters and 747 numbered sections**.

**Excluded programme remains deferred-by-user:** all Demailly approximation/regularization and dedicated Bergman, L², Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof completion. No build, tests, GitHub Actions CI, formal verification or website publication.
