# Constant-torus Gauduchon thresholds: exact spectral face, smooth nonattainment, and an eigenvalue-crossing cusp

**Finding:** POME-GAUD-TORUS-SPECTRAL-FACE-CUSP-001.  
**Date:** 2026-11-08. **Severity:** low. **Status:** verified conditional deduction (self-contained explicit model, conditional only as an interpretation of the general Pome framework). **No printed theorem is refuted.**  
**Production main inspected:** b6933b772f41b45918f7e25ed1afbbb1fd892272.

## Pinpointed integrated reading-edition statements

1. docs/sections/gauduchon-metrics-and-linear-mass--the-gauduchon-criterion-for-positivity/index.html, main blob **6dd43b62800206fb0302fd4261372d7882e5170d**:
   - Theorem 11.6.1 (generalized Lamari criterion), source label **non-kahler-pluripotential-theory:87DC00D0**, permanent tag **88BE3B63D9E5**, physical lines **10–30**, proof **32–74**.
   - Corollary 11.6.2 (attained curvature threshold), source **non-kahler-pluripotential-theory:EAE0F4AE**, permanent **F83E15A1F529**, physical lines **81–96**.
   - Lemma 11.6.3 (zero smooth Gauduchon degree), source **non-kahler-pluripotential-theory:DC67F892**, permanent **91B8C8A3C10E**, physical lines **104–116**.
2. docs/sections/gauduchon-metrics-and-linear-mass--compactness-and-duality-of-gauduchon-currents/index.html, main blob **31d17f258f2ff178bf52be3d3f92d5a995878d3a**:
   - Proposition 11.7.1, source **non-kahler-pluripotential-theory:C21ACA47**, permanent **155386134D9E**, physical lines **7–42**, with normalized compact convex Gauduchon-current closure.
   - Corollary 11.7.4, source **non-kahler-pluripotential-theory:4B74203A**, permanent **A97DA8CE2358**, physical lines **47–70**, concavity and continuous dependence of the threshold.
3. docs/sections/gauduchon-metrics-and-linear-mass--conservation-of-the-trace-mass/index.html, main blob **34af83ff391b5e5590cd9cb10ca4cd2b3faff02c**, Proposition 11.5.1, source **non-kahler-pluripotential-theory:0D4A42C8**, permanent **828FAD1A35BF**, is a contextual trace conservation input (not independently certified here).
4. docs/sections/conventions/index.html, blob **ef778e54d8d7413242387e95c52269b3c7d42cae**, physical line **123** supplies connected compact manifold conventions. No assertion of missing connectedness is made.

## Exact example and proof

Let $E=\mathbb C/(\mathbb Z+i\mathbb Z)$, $X=E\times E$, and let $\beta=\frac{i}{2}\,dz\wedge d\bar z$ be the translation-invariant positive $(1,1)$-form on $E$. Thus $\int_E\beta=1$. Put $\zeta_j=\pi_j^*\beta$, $\omega=\zeta_1+\zeta_2$, and fix two real constants $a<b$. Consider the smooth closed real form
$$
\theta=a\zeta_1+b\zeta_2.
$$
Our normalization is $\int_X\zeta_1\wedge\zeta_2=1$ and $\zeta_j^2=0$.

**Exact threshold and nonattainment by smooth Gauduchon metrics.**
For every smooth positive Gauduchon metric $\gamma$ (in fact, every smooth Hermitian metric),
$$
\int_X(\theta-a\omega)\wedge\gamma
=(b-a)\int_X\zeta_2\wedge\gamma>0.
$$
The strict inequality follows pointwise from the nonzero semipositive rank-one $\zeta_2$ and strict positivity of $\gamma$. Hence every normalized Gauduchon degree is strictly greater than $a$.

Nevertheless, for every $\varepsilon>0$, the *Kähler*, hence Gauduchon, metric
$$
\gamma_\varepsilon=\varepsilon\zeta_1+\zeta_2
$$
satisfies the exact identities
$$
\int_X\omega\wedge\gamma_\varepsilon=1+\varepsilon,\qquad
\int_X\theta\wedge\gamma_\varepsilon=a+b\varepsilon,
$$
and therefore
$$
\frac{\int_X\theta\wedge\gamma_\varepsilon}
{\int_X\omega\wedge\gamma_\varepsilon}
=a+\frac{(b-a)\varepsilon}{1+\varepsilon}.
$$
By the definition in Corollary 11.6.2, **$\kappa_\omega(\theta)=a$**, and *no smooth Gauduchon metric realizes this infimum*. There is no contradiction with the separate assertion that the **potential lower-curvature bound** $\theta+dd^c u\ge a\omega$ is attained: here $u=0$ already gives it. Confusing attainment of the curvature bound with attainment of its smooth test infimum would be an error; the printed text distinguishes the two correctly.

**An infinite-dimensional minimizing face in the weak closure.**
Normalize
$$
T_\varepsilon=\frac{\gamma_\varepsilon}{1+\varepsilon}
\rightharpoonup T_0=\zeta_2.
$$
All these are smooth normalized Gauduchon forms for $\varepsilon>0$, and $T_0$ is a rank-one positive closed current with $\int_X\omega\wedge T_0=1$ and $\int_X\theta\wedge T_0=a$. Hence $T_0\in\mathscr C_\omega$ realizes the minimum in Proposition 11.7.1.

More strongly, take *any* smooth strictly positive $f$ on the second elliptic factor, with $\int_E f\beta=1$. Define
$$
T_f=\pi_2^*(f\beta)=f(z_2)\zeta_2,\qquad
T_{\varepsilon,f}=\frac{\varepsilon\zeta_1+f(z_2)\zeta_2}{1+\varepsilon}.
$$
Because $f\beta$ is a top-degree form on a complex curve, $d(f\beta)=0$. Hence $T_f$ and $T_{\varepsilon,f}$ are $d$-closed and $dd^c$-closed. The form $T_{\varepsilon,f}$ is a *smooth strictly positive* Gauduchon $(1,1)$-form on the surface, normalized by $\int_X\omega\wedge T_{\varepsilon,f}=1$, and tends smoothly to $T_f$ as $\varepsilon\downarrow0$. Thus each $T_f$ lies in the prescribed closure $\mathscr C_\omega$, and
$$
\int_X\theta\wedge T_f=a,\qquad
\int_X\omega\wedge T_f=1.
$$
Distinct positive densities $f$ give distinct minimizing currents. Consequently the minimizing face contains an **infinite-dimensional convex family** of rank-one semipositive smooth currents; it is not uniquely determined by a simple lowest eigenvalue. This claim does *not* classify every current in the minimizing face.

**Exact eigenvalue-crossing cusp, even inside the positive cone.**
For $-1<t<1$ let
$$
\theta_t=(1+t)\zeta_1+(1-t)\zeta_2>0.
$$
Exchanging the two factors when needed in the calculation above yields
$$
\boxed{\kappa_\omega(\theta_t)=\min\{1+t,1-t\}=1-|t|.}
$$
This is concave and $1$-Lipschitz as Corollary 11.7.4 requires, but *not differentiable at $t=0$*. For every $t\ne0$ within this interval, the minimizing value is not reached by any smooth Gauduchon metric; for $t=0$ every smooth Gauduchon metric attains the ratio $1$. Therefore no general $C^1$ dependence of the optimal Gauduchon-degree threshold can be inferred from the printed concavity/continuity statement, even along smooth families of *strictly positive* closed backgrounds.

## Severity, status, suggested incorporation, dependencies

**Classification:** low / verified conditional deduction; exact elementary counterexamples to two *unprinted strengthened assertions* (smooth attainment of the test infimum, and differentiability of the threshold). Theorem 11.6.1, Corollary 11.6.2, Lemma 11.6.3, Proposition 11.7.1, and Corollary 11.7.4 are **not refuted**, and no proof gap is alleged. The entire Lamari/Fredholm/compactness argument has **not** been re-certified by these explicit calculations. The only mathematical inputs for the model are exterior-product algebra, closedness of top-degree forms on an elliptic curve, and positivity of Hermitian forms; Hironaka, Demailly regularization and all excluded Bergman/L²/OT/multiscale/positivity-loss work play no role.

**Proposed optional addition (not applied):** a post-Corollary 11.7.4 illustrative example distinguishing attainment of curvature thresholds from attainment by smooth Gauduchon tests, exhibiting the whole infinite-dimensional family $T_f$ and the exact $1-|t|$ cusp. Preserve all existing permanent tags and historical attribution.

**Affected dependents/interpretation:** optimization and minimizer statements in §§11.6–11.7, and any later derivation that treats $\kappa_\omega$ as smooth or presumes a smooth minimizing Gauduchon test. Existing correctly qualified printed results are unaffected.

**Exact new coverage:** selected explicit two-factor torus proof and new smooth-closure minimizing-family check against §§11.6.2–3 and 11.7.1/.4. These sections had been previously partially reviewed; **no new first theorem-level section, no whole-section certification**. §11.5.1 and §1.1 are convention/dependency contexts only. Current main table of contents: **25 chapters / 747 numbered sections / zero wholly certified mathematics sections**. Existing resolved, unresolved and genuine-duplicate classifications remain untouched. Owner-excluded Demailly approximation/regularization and dedicated Bergman/L²/Ohsawa–Takegoshi/multiscale/positivity-loss tasks remain **deferred-by-user**, not resolved or certified. No main/source/registry/canonicalization changes, formal verification, project build, GitHub Actions or publication.