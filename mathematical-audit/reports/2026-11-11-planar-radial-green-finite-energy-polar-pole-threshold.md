# A sharp planar radial finite-energy Green potential with a polar pole

**Finding:** `POME-GREEN-RADIAL-POLAR-ENERGY-THRESHOLD-001`.  
**Classification:** low / **verified conditional deduction**. The printed Example 4.5.5 is **correct**; this is an explicit one-parameter realization with an exact integrability threshold, not a source correction or a certification of the general Green-energy theory.  
**Production main reviewed:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.  
**Integrated source:** `docs/sections/green-energy-and-martin-boundaries/index.html`, Git blob `976a90f2a5eba299658f73a1eee8b9d3fef8020f`, standing hypotheses and Green-energy normalization **physical lines 7–13** and **Example 4.5.5, physical line 71**. Stable original source label `classical-potential-theory:898691BF`, permanent tag `61A5D2A82793`. Cross-check: `docs/sections/green-functions-and-potentials/index.html`, blob `63c74d1c4a0958633b42903a0e3a4526f42b7588`, §3.5.4 **physical lines 33–35**, source chunk `classical-potential-theory:D6A0F97E`, permanent heading tag `870251679082`. Theorem 4.5.2, permanent tag `CC3D1AD9179B` (physical lines 17–29), is used only for contextual comparison, not as a premise of the calculation.

## Exact statement

Let $D=\{z\in\mathbb C:|z|<1\}$ and use the unnormalized positive planar Green kernel
\[
  G_D(z,w)=\log\left|\frac{1-\overline w z}{z-w}\right|,
  \qquad -\Delta_zG_D(z,w)=2\pi\delta_w.
\]
For any $0<\gamma<1$, put $t=\log(1/|z|)$ for $z\ne0$, and define
\[
 F_\gamma(t)=
 \begin{cases}
   \gamma t,&0\le t\le1,\\
   t^\gamma+\gamma-1,&t\ge1,
 \end{cases}
 \qquad U_\gamma(z)=F_\gamma(\log(1/|z|)),\quad U_\gamma(0)=+\infty.
\]
There is a finite positive Radon measure
\[
 d\mu_\gamma(z)=
 \frac{\gamma(1-\gamma)}{2\pi|z|^2(\log(1/|z|))^{2-\gamma}}
 \mathbf1_{\{0<|z|<e^{-1}\}}\,dA(z)
\]
with **no atom at the origin** and total mass $\mu_\gamma(D)=\gamma$, such that $G_D\mu_\gamma=U_\gamma$ at **every** point, in the extended-real sense. Thus its Green potential is finite on $D\setminus\{0\}$ and infinite precisely on the compact polar set $\{0\}$.

For every $q>0$,
\[
 \int_D U_\gamma^q\,d\mu_\gamma<\infty
 \quad\Longleftrightarrow\quad \gamma(q+1)<1.
\]
In particular the **exact energy threshold** is
\[
 I_D(\mu_\gamma)<\infty \iff 0<\gamma<\tfrac12,
 \qquad
 I_D(\mu_\gamma)=
 \frac{2\gamma^2(1-\gamma)}{1-2\gamma}
 \quad(0<\gamma<\tfrac12).
\]
For $\gamma=1/2$ the energy divergence is logarithmic in the integration parameter $t$; for $1/2<\gamma<1$ it is polynomial. The exponent $1/2$ is sharp **for this explicit radial family only**, not an asserted universal regularity threshold.

## Complete computation and proof

**1. Radial Green-average identity.** For $r=e^{-t}$ and $\rho=e^{-s}$, the elementary circle means of logarithms give
\[
 \frac1{2\pi}\int_0^{2\pi}G_D(re^{i\theta},\rho e^{i\varphi})\,d\varphi
 =-\log\max(r,\rho)=\min(t,s).
\]
Indeed $r\rho<1$, so the circle mean of $\log|1-r\rho e^{i\varphi}|$ is zero, while the mean of $\log|r-\rho e^{i\varphi}|$ is $\log\max(r,\rho)$. At coincident radii the logarithmic singularity is integrable on the circle.

**2. Positive measure, total mass and no hidden circle/point charge.** In the variable $s=\log(1/|w|)$, polar area $dA=\rho\,d\rho\,d\varphi$ transforms the displayed $\mu_\gamma$ into the radial mass density
\[
 d m_\gamma(s)=\gamma(1-\gamma)s^{\gamma-2}\mathbf1_{s\ge1}\,ds.
\]
The mass is $\gamma(1-\gamma)\int_1^\infty s^{\gamma-2}ds=\gamma$. This definition has neither an atom at $0$ nor a circle measure at $r=e^{-1}$. Independently, $F_\gamma$ is $C^1$ at $t=1$, with matching values and derivatives both $\gamma$, so its distributional radial Laplacian has no interface delta. As $t\to\infty$, $F'_\gamma(t)=\gamma t^{\gamma-1}\to0$, ruling out a logarithmic point atom. Directly, $\Delta_zU_\gamma=F''_\gamma(t)/|z|^2$ off $0$ and the interface, with $F''_\gamma=\gamma(\gamma-1)t^{\gamma-2}$ for $t>1$, hence $-\Delta U_\gamma=2\pi\mu_\gamma$.

**3. Exact Green representation, including the singular point.** By Tonelli and the circle-average formula,
\[
 (G_D\mu_\gamma)(e^{-t})=
 \gamma(1-\gamma)\int_1^\infty\min(t,s)s^{\gamma-2}\,ds.
\]
For $0\le t\le1$ this equals $\gamma t$. For $t\ge1$, split at $s=t$ to obtain
\[
 \gamma(1-\gamma)\left(\int_1^t s^{\gamma-1}ds
   +t\int_t^\infty s^{\gamma-2}ds\right)
 =(1-\gamma)(t^\gamma-1)+\gamma t^\gamma
 =t^\gamma+\gamma-1.
\]
At $z=0$, the integrand of the Green kernel equals $s$ on radius $e^{-s}$, so
\(G_D\mu_\gamma(0)=\gamma(1-\gamma)\int_1^\infty s^{\gamma-1}ds=+\infty\).
The representation also shows directly that the Green potential is positive and superharmonic and vanishes continuously on the unit circle.

**4. All moments, energy and sharpness.** For (q>0),
\[
 \int_D U_\gamma^q\,d\mu_\gamma
 =\gamma(1-\gamma)\int_1^\infty
 (s^\gamma+\gamma-1)^q s^{\gamma-2}\,ds.
\]
The integrand is asymptotic to (\gamma(1-\gamma)s^{\gamma(q+1)-2}\); the power-integral criterion gives the stated strict threshold, including divergence at equality. At $q=1$ and $0<\gamma<1/2$ the integral is explicitly
\[
 \gamma(1-\gamma)\left(\frac1{1-2\gamma}
            +\frac{\gamma-1}{1-\gamma}\right)
 =\frac{2\gamma^2(1-\gamma)}{1-2\gamma}.
\]
By Tonelli $I_D(\mu_\gamma)=\int G_D\mu_\gamma\,d\mu_\gamma$, with no invalid subtraction of infinite terms. As an independent normalization check, the radial Dirichlet identity reads
\[
 \frac1{2\pi}\int_D|\nabla U_\gamma|^2dA
 =\int_0^\infty |F'_\gamma(t)|^2dt
 =\gamma^2+\gamma^2\int_1^\infty t^{2\gamma-2}dt,
\]
which agrees exactly with the energy formula when finite.

## Mathematical classification and integration proposal

**Status:** verified conditional deduction, **low** severity. The displayed Green-kernel calculation is self-contained once the unnormalized planar disk Green formula is fixed. It verifies an explicit model of printed **Example 4.5.5** and its compatibility with Theorem 4.5.2's no-polar-mass statement: (\mu_\gamma(\{0\})=0\), even though (U_\gamma(0)=+\infty\). Neither the general finite-energy equivalence nor the general Martin-boundary and balayage results are certified by this example. There is **no confirmed source error, no proof gap in Example 4.5.5, and no duplicate theorem claim**.

**Proposed optional insertion (not applied):** after Example 4.5.5, give the explicit radial density and potential, note the $C^1$ gluing at $r=e^{-1}$, and state the sharp $q$-moment criterion. Preserve the original capacity construction, its attribution, source tag and permanent tag; the new example is complementary rather than a replacement.

**Affected dependents:** Example 4.5.5 and pedagogical comparisons with Theorem 4.5.2/4.5.4 only; no downstream theorem is invalidated. The heat kernel, complex Monge–Ampère, Demailly approximation/regularization and the dedicated Bergman/weighted-$L^2$/Ohsawa–Takegoshi/multiscale/positivity-loss proof-completion programme were **not reopened** and remain **deferred-by-user**. No main, source, registry, tags, website or CI modification. No build, formal verification or project tests were performed.

**Precise coverage:** direct proof-level check of Example 4.5.5's polar-pole statement and standing Green normalization, plus the §3.5.4 kernel convention. The remaining proofs of §§4.5 and 3.5 were **not** reviewed in this run. Both sections already had selected mathematical coverage: **0 first-visited numbered sections / 0 whole-section certifications**. The inventory remains **25 chapters, 747 numbered sections** at the pinned main.
