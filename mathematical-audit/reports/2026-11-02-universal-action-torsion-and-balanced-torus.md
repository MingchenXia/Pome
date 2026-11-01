# Universal vanishing of the Hermitian geodesic-action torsion defect

**Finding ID:** `POME-GEO-UNIVERSAL-TORSION-KAHLER-001` — **low / verified conditional deduction**; not a false theorem or a certified upstream proof.  
**Date:** 2026-11-02. **Production main reviewed:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.

## Exact current integrated anchors

1. `docs/sections/perron-interpolation-and-the-geodesic-equation/index.html`, blob `dc8dc381257360c94fe1c792499bb1ddf1bf5997`: Proposition **17.16.9**, permanent tag `5885FD8F9550`, lines 167–183 (smooth Schur complement); Theorem **17.16.12**, source `non-kahler-pluripotential-theory:983F8C01`, permanent `7A7AE56CA513`, lines 214–247; equation **17.16.13**, permanent `DCC8DA6D179E`, lines 216–219; Corollary **17.16.14**, source `non-kahler-pluripotential-theory:8881F196`, permanent `BE24BBA15991`, lines 252–262.
2. `docs/sections/gauduchon-metrics-and-linear-mass--the-adjoint-measure-of-the-linearization/index.html`, blob `519e50338be6560f6b2856fddce212738f5109bc`: Proposition **11.23.4**, source `non-kahler-pluripotential-theory:B9B9F692`, permanent `A914D4D9C6CB`, lines 58–73; Example **11.23.5**, source `non-kahler-pluripotential-theory:324594DA`, permanent `28F39F2B7C2C`, lines 77–100.
3. `docs/sections/torsion-and-the-variation-of-mass/index.html`, blob `9abec9685e33a1b40f9c0765381408eb52b325d3`: Lemma **11.1.2**, permanent `3B0A8DD950AD`, lines 15–25 (formal integration by parts); Theorem **11.1.7** (Chiose), source `non-kahler-pluripotential-theory:5CD99CBA`, permanent `FB90FC741F25`, lines 100–159 (universal *Gauduchon* condition).

## Precise statement: all velocity jets at one metric, versus all potentials

Let $X$ be a compact complex manifold of dimension $n\geq2$, $\omega>0$ a smooth Hermitian $(1,1)$-form, and
$$
\mathcal H_\omega=\{u\in C^\infty(X,\mathbb R):\eta_u:=\omega+dd^c u>0\},
\qquad T_u=\eta_u^{n-1}.
$$
For a smooth real velocity $f$, define the difference between the right sides of the stationary-action equation (17.16.13) and the product homogeneous Monge–Ampère equation (17.16.10) as a smooth top-degree form:
$$
\boxed{\mathfrak T_{\eta_u}(f)
=n f\bigl(df\wedge d^cT_u-d^c f\wedge dT_u\bigr)
+\frac n2 f^2dd^cT_u.}
$$

**Fixed potential:** For each $u\in\mathcal H_\omega$, the identity $\mathfrak T_{\eta_u}(f)\equiv0$ for *every* real smooth $f$ holds **if and only if**
$$
d(\eta_u^{n-1})=0.
$$
Thus vanishing for every velocity at one background is exactly the **balanced** condition, stronger than Gauduchon in general.

**All potentials:** The following conditions are equivalent: (i) $d\omega=0$ (Kähler); (ii) every $\eta_u$, $u\in\mathcal H_\omega$, is balanced; (iii) $\mathfrak T_{\eta_u}(f)=0$ for all admissible $u$ and all real smooth $f$. Therefore non-Kählerity can always be detected by an admissible potential and a velocity jet in the **difference of the two PDE expressions**.

These are *pointwise differential-operator* identities, **not** existence results and **not** an assertion that actual paths solving one geodesic equation fail to solve the other. The universal *Gauduchon* persistence and constant-mass equivalence is already Theorem 11.1.7 (Chiose) and Proposition 11.23.4, with attribution retained. The stronger **balanced** and first-order speed-jet criterion here is distinct.

## Self-contained proof of the new equivalences

**1. Vanishing of the velocity defect detects balancedness.** Fix $\eta>0$, $T=\eta^{n-1}$, and assume $\mathfrak T_\eta(f)=0$ for all smooth real $f$. Testing $f\equiv1$ gives $dd^cT=0$. Fix any $x\in X$ and real $g$ with $g(x)=0$. Evaluating the identity for $f=1+s g$ at $x$ and comparing coefficients of $s$ now gives
$$
\bigl(dg\wedge d^cT-d^c g\wedge dT\bigr)_x=0
\quad\text{for every possible }dg_x.
$$
Writing $d^c=c_i(\bar\partial-\partial)$ for the nonzero purely imaginary normalization factor $c_i$, the left side is
$$
2c_i\bigl(\partial g\wedge\bar\partial T-\bar\partial g\wedge\partial T\bigr)_x.
$$
Here $\bar\partial T$ has bidegree $(n-1,n)$ and $\partial T$ its complex conjugate. Wedge with arbitrary $(1,0)$-covectors detects all coefficients of $\bar\partial T$. Any complex $(1,0)$ differential can arise as $\partial g_x$ for a *real* smooth $g$; testing a covector and its $i$ multiple shows $\partial T=\bar\partial T=0$ at $x$. Thus $dT=0$ everywhere. Conversely $dT=0$ implies $d^cT=dd^cT=0$, immediately forcing $\mathfrak T_\eta(f)=0$ for all $f$.

**2. Balancedness of every positive potential perturbation forces Kählerity.** Since $d(dd^c u)=0$,
$$
d(\omega+dd^cu)^{n-1}
=(n-1)d\omega\wedge(\omega+dd^cu)^{n-2}.
$$
At a fixed $x$, the values $(dd^cu)_x$ of globally smooth, sufficiently small, compactly supported real perturbations contain an open neighborhood of $0$ in the real vector space of Hermitian $(1,1)$-forms; positivity is retained. If all the perturbed forms are balanced, the polynomial in $Q$,
$$
Q\longmapsto d\omega_x\wedge(\omega_x+Q)^{n-2},
$$
vanishes on that open neighborhood and hence identically. Its top homogeneous component is
$$
d\omega_x\wedge Q^{n-2}=0\qquad\text{for every Hermitian }Q.
$$
For $n=2$ this already reads $d\omega_x=0$. For $n\geq3$, polarizing $Q^{n-2}$ and testing products of elementary $(1,1)$-covectors detects every $(2,1)$ and $(1,2)$ coefficient of $d\omega_x$, so $d\omega_x=0$. As $x$ was arbitrary, $\omega$ is Kähler. Conversely $d\omega=0$ implies $d\eta_u=0$ for every $u$, so all powers are closed. Combining with step 1 establishes the equivalences.

**3. An exact, previously unnoted strengthening of the printed torus example.** Example 11.23.5 is on $X=E^3$ with $\eta_j=dx_j\wedge dy_j$,
$$
b=e^{\cos(2\pi x_1)},\qquad c=b^{-1},\qquad
\omega=\eta_1+b\eta_2+c\eta_3.
$$
The *initial* form is actually **balanced**, not merely Gauduchon, because $bc=1$ and $db,dc$ are multiples of $dx_1$:
$$
\omega^2=2b\eta_1\wedge\eta_2+
2c\eta_1\wedge\eta_3+2\eta_2\wedge\eta_3,
\qquad d\omega^2=0.
$$
Nevertheless $d\omega=db\wedge\eta_2+dc\wedge\eta_3\not\equiv0$.
Take precisely the existing $v=\cos(2\pi x_2)$ and $dd^cv=h\eta_2$ with $h=-\pi\cos(2\pi x_2)$. For the printed positive range $0<|s|<1/(\pi e)$, write $\omega_s=\omega+sdd^cv$. Using $dh\wedge\eta_2=0$ and $bc=1$ yields the **exact torsion identity**
$$
\boxed{d\omega_s^2=2s h\,dc\wedge\eta_2\wedge\eta_3.}
$$
At $x_1=1/4$, $x_2=0$ one has $dc=2\pi\,dx_1$, $h=-\pi$, hence
$$
d\omega_s^2=-4\pi^2s\,dx_1\wedge\eta_2\wedge\eta_3\ne0.
$$
The printed example already proves failure of Gauduchon persistence after the perturbation; this checks the stronger fact that **balancedness** fails arbitrarily close to an initially balanced non-Kähler metric.

## Independent first-variation cross-check and status

For a smooth path $u_t$, put $f=\dot u_t$, $\eta_t=\omega+dd^c u_t$, $T_t=\eta_t^{n-1}$. Differentiating
$$
\mathscr S(u)=\tfrac12\int_0^1\!\int_X\dot u_t^2\,\eta_t^n\,dt
$$
in a test direction $v_t$ vanishing at both endpoints, integrating in time and then by parts on $X$ via Lemma 11.1.2 gives the term
$$
-\ddot u\,\eta^n-nf\,dd^cf\wedge T
+\frac n2dd^c(f^2T).
$$
The exact Leibniz expansion of $dd^c(f^2T)$ produces $n\,df\wedge d^cf\wedge T$, the mixed first-order terms with signs as printed, and $(n/2)f^2dd^cT$. **The coefficients $n$ and $n/2$ and both torsion signs in (17.16.13) are consistent.** The claim is thus a *new conditional deduction / extra algebraic audit*, not a proof-gap allegation.

**Proposed change:** optional corollary after Theorem 17.16.12 and an explicit balanced-but-non-Kähler observation after Example 11.23.5. No source, registry, canonical content, tags, or published reader altered. **Affected dependents:** §§17.16.9–14, 11.1.7–8, 11.23.4–5 and interpretation of action stationarity versus homogeneous/Perron equations.

**Exact coverage:** new selected first-variation and all-speed algebraic inspection of §17.16.12; new direct balancedness/differential test of §11.23.5; previously sampled §§17.16,11.23,11.1, no additional first-covered section or whole theorem/section certification. Main ToC remains **25 chapters, 747 numbered sections, zero fully certified mathematical sections**. All excluded Demailly regularization/approximation, Bergman, $L^2$, Ohsawa–Takegoshi, multiscale-atlas and positivity-loss work stays **deferred-by-user**; no CI, tests, build, formalization or website publication.
