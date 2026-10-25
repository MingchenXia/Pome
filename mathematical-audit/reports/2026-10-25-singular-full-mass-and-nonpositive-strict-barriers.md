# Sharp absolute-continuity failure for full-mass currents and sign-free strict barriers

**Checkpoint (UTC):** 2026-10-25T04:01:46.191Z. **Integrated main reviewed:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`.
**Audit branch:** \`review/mathematical-audit\`. This is a **selected proof audit**, not a certification of any section, theorem dependency tree, or the entire collection.

## Exact integrated source anchors

| Passage | Integrated main path; blob SHA; lines | Stable source label / permanent tag |
| --- | --- | --- |
| Lemma 13.31.1, determinant bound and truncated proof | \`docs/sections/absolutely-continuous-and-non-pluripolar-mass/index.html\`; \`bea17d8041a7af4a252913e0f700b44d77521f82\`; lines 7–16, 19–97 | \`transcendental-positive-cones-6D2B462A\` / \`C7894CAD8593\` |
| Equation 13.31.2, differentiation of singular measures | Same file, lines 21–49 | \`transcendental-positive-cones-1C2CEE7B\` / \`58A08DA1A586\` |
| Corollaries 13.31.3–4, supremum of a.c. determinant masses | Same file, lines 103–136 | \`transcendental-positive-cones-A2E98A80\` / \`1E1CF458220D\`; \`transcendental-positive-cones-AA4B08E5\` / \`04768594F11F\` |
| Strict-subsolution construction, Cor. 13.20.3 and Prop. 13.20.4 | \`docs/sections/volumes-under-bounded-mass--strict-barriers-and-background-variation/index.html\`; \`2fb8697ad0f1e916245d9adafde27f40f97b46f3\`; lines 76–112 | \`non-kahler-pluripotential-theory-40A9BCB2\` / \`D51B82B18D30\`; \`non-kahler-pluripotential-theory-DE77A39F\` / \`0729BE10D92E\` |
| Lemma 13.20.1 and upper-volume perturbation | Same file, lines 10–71 and 134–169 | \`non-kahler-pluripotential-theory-1DBB631B\` / \`EDD01F5B65E5\`; \`non-kahler-pluripotential-theory-95AB9149\` / \`F4C607C7C503\` |
| One-sided and two-sided background comparison | \`docs/sections/volumes-under-bounded-mass--model-comparison-under-background-changes/index.html\`; \`9031cedd29e8ed20dc720a8119d326ff727a2113\`; lines 10–92, 105–164; and \`docs/sections/volumes-under-bounded-mass--two-sided-background-perturbations/index.html\`; \`45c385fe6dc2c7a8b877b27e3bf854da9c4ac463\`; lines 13–32, 36–91, 98–124 | §§13.25.1–3 (\`61209D2B61BD\`, \`F274299A5A71\`, \`1ED63BC3072B\`), §13.26.1 (\`D5C96B9222A4\`), §13.26.3 (\`218C2CE831D1\`) |
| Green kernel on a compact curve, used only for independent model construction | \`docs/sections/volumes-under-bounded-mass--model-potentials-on-curves/index.html\`; \`4ec0e8d5c90ad5df4e84f17bbc03a2298415e29f\`; lines 10–16, 19–58 | §13.28.1 \`2422DD1AB3AB\`; Green kernel internal cross-reference §20.3.9 \`0A6FA0C6A351\` |

## POME-FULLMASS-SINGULAR-AC-001 — low / verified conditional deduction

**Claim (new sharpness example, not a false printed theorem).** For every \`n >= 1\` there are a flat projective complex torus \`X=E^n\`, a flat Kähler form \`theta\`, and a **bounded continuous** \`theta\`-psh potential \`u\` with positive closed current \`T=theta+dd^c u\` such that

\[
 \underline{\operatorname{vol}}_\theta(u)
 =\overline{\operatorname{vol}}_\theta(u)
 =\int_X\langle T^n\rangle
 =\int_X\theta^n=n!>0,\qquad
 T_{\rm ac}=0\quad\text{almost everywhere}.
\]

In particular, \(\int_X(T_{\rm ac})^n=0\). There are **smooth Kähler forms** \(T_t=\theta+dd^c u_t\) with \(u_t\to u\) **uniformly** and

\[
 \int_X((T_t)_{\rm ac})^n=n!,\qquad
 \bigl\|T_t^n-\langle T^n\rangle\bigr\|_{\mathrm{TV}}=2n!
 \quad(t>0).
\]

Thus a positive lower singularity volume, even at full cohomological mass with bounded potentials, gives **no positive lower bound** on the pointwise absolutely-continuous determinant mass. Uniform potential convergence does **not** imply continuity of this determinant integral or total-variation convergence of the Monge–Ampère measures. This is compatible with, and sharpens the interpretation of, the **upper** inequality in Lemma 13.31.1.

**Complete construction and proof.** Let \`E=C/(Z+iZ)\`, with normalized translation-invariant Kähler form \(\omega_E\) of mass \(1\). Identify a small real arc of the horizontal circle with \([0,1]\), place inside it a middle-thirds Cantor set, and let \(\nu\) be its standard nonatomic Cantor probability measure. Put \(\alpha=\log 2/\log 3>0\). At generation \(k\), basic intervals have lengths \(3^{-k}\), masses \(2^{-k}\), and pairwise disjoint interiors; an interval of length comparable to \(3^{-k}\) meets a uniformly bounded number of them. Thus a constant \(C\), independent of the center, satisfies

\[
 \nu(B(x,r))\le C r^\alpha\qquad(0<r<1/10).
\]

This measure is singular with respect to area on \(E\). Choose the internally defined normalized Green kernel \(G(x,y)\) with \(dd_x^cG(x,y)=\delta_y-\omega_E\). Its sole singularity is logarithmic on the diagonal, with a smooth bounded remainder locally. Set \(U(x)=\int_EG(x,y)\,d\nu(y)\). The Frostman estimate implies, uniformly in \(x\),

\[
 \int_{d(x,y)<r}\log(1/d(x,y))\,d\nu(y)
 \le C' r^\alpha\bigl(\log(1/r)+1/\alpha\bigr)\xrightarrow[r\downarrow0]{}0.
\]

Split the integral into a neighborhood of and the complement of the diagonal. The displayed estimate controls the near-diagonal piece uniformly; the complement is continuous in \(x\). Hence \(U\) is **continuous and bounded**, and distributional differentiation gives
\(\omega_E+dd^cU=\nu\).

Let \(\pi_i:E^n\to E\) denote projection and put
\(\theta=\sum_{i=1}^n\pi_i^*\omega_E\), \(u=\sum_i\pi_i^*U\), and \(T=\sum_i\pi_i^*\nu\).
Every coefficient measure of \(\pi_i^*\nu\) is supported in \(\pi_i^{-1}(\operatorname{supp}\nu)\), a set of zero \(2n\)-dimensional Lebesgue measure. Therefore \(T_{\rm ac}=0\). Since all potentials are locally bounded, non-pluripolar and Bedford–Taylor powers coincide. Their product rule for currents pulled back from distinct factors gives

\[
 \langle T^n\rangle=T^n
 =n!\,\pi_1^*\nu\wedge\cdots\wedge\pi_n^*\nu
 =n!\,\nu^{\otimes n},
 \qquad \int_X\langle T^n\rangle=n!.
\]

One can verify this product directly by smoothing \(U\) on each elliptic factor: the smooth wedge is the ordinary product density, and Bedford–Taylor locality/continuity for uniform locally bounded psh approximations passes to the limit. Because \(u\) is bounded, every \(\theta\)-psh potential of the same ordinary singularity type is bounded. Stokes/Bedford–Taylor integration on the compact Kähler torus gives total mass \(\int_X\theta^n=n!\) for each such potential; hence **both** singularity volumes equal \(n!\).

For the smooth approximation, use the positive heat kernel \(H_t\) of the flat torus. Let \(U_t=H_t*U\) and \(\nu_t=H_t*\nu\). Then \(\nu_t\) has a strictly positive smooth density, \(\int_E\nu_t=1\), \(\omega_E+dd^cU_t=\nu_t\), and \(U_t\to U\) uniformly by continuity of \(U\). Define \(u_t=\sum_i\pi_i^*U_t\) and \(T_t=\theta+dd^cu_t=\sum_i\pi_i^*\nu_t\). Each \(T_t\) is a smooth **strictly positive Kähler form**, and

\[
 T_t^n=n!\,\nu_t^{\otimes n},\qquad
 \int_X T_t^n=n!.
\]

But \(T_t^n\) is absolutely continuous while \(T^n=n!\nu^{\otimes n}\) is carried by the product Cantor set of Lebesgue measure zero. The two measures are mutually singular, with common mass \(n!\), whence their signed-measure total-variation norm is exactly \(2n!\). The pointwise a.c. tensor of \(T\) is zero, whereas \((T_t)_{\rm ac}=T_t\). This proves every assertion.

**Consequences and dependency boundary.** In the positive-volume minimal singularity type, the ordinary singularity-volume pseudometric gives \(d_\theta(u,0)=0\), although the full-mass Monge–Ampère measures \(T^n\) and \(\theta^n\) are mutually singular. This does **not** contradict §13.31.4's supremum formula (whose supremum is attained by the smooth flat \(\theta\)). It does not depend on the analytic approximations used in Corollary 13.31.3: the curve Green kernel, elementary Frostman bound, heat convolution and bounded Bedford–Taylor products suffice. Affected readers: §§13.31.1/.4, 13.20.1/.3/.6, the ordinary-singularity-model discussion in §13.28. Proposed correction: **optional explanatory example**, not a correction of any false statement.

## POME-STRICT-BARRIER-NONPOS-BG-001 — low / verified conditional deduction

**Sharpening (not an error in printed Proposition 13.20.4).** The extra assumption \(\theta\ge0\) in Proposition 13.20.4 is unnecessary **for its one-way conclusion**. Let \(\theta\) be any **smooth real** \((1,1)\)-form on the compact Hermitian manifold, let \(u\in\mathrm{PSH}(X,\theta)\), and suppose \(\underline{\operatorname{vol}}_\theta(u)>0\). By Corollary 13.20.3, which did not assume \(\theta\ge0\), there exist \(w\le u\) and \(\delta>0\) with \(\theta+dd^cw\ge\delta\omega\). By compactness choose a **positive** constant \(C\) satisfying \(\theta\le C\omega\), irrespective of any lower eigenvalue of \(\theta\). For every

\[
 0<t<\min\{1,\delta/C\},
\]

we obtain

\[
 (1-t)\theta+dd^cw
   =(\theta+dd^cw)-t\theta
   \ge(\delta-tC)\omega\ge0.
\]

Thus \(w\) is an admissible competitor for \(P_{(1-t)\theta}(u)\), so

\[
 \boxed{P_{(1-t)\theta}(u)\ge w\not\equiv-\infty}
\]

for **every** such \(t\), not merely one value, without \(\theta\ge0\). The proof also shows that the smaller background is big, since the inequality is strict for the chosen \(t\). No converse is asserted: the separate §16.28.69 lower mass argument has its own hypotheses, not checked here. Affected passage: §13.20.4 and its forward comparison to §16.28.66. Proposed optional amendment: drop \(\theta\ge0\) from Proposition 13.20.4 alone and state the full interval of allowable rescalings, while checking any downstream converse separately.

## Other selected proof checks and unresolved boundaries

- **§13.20.1/.3/.6:** checked the contact-set inclusion \(C_j\subset\{u\le-k\}\), the \(n2^n v_+\) mixed-mass error and \(b_\delta-1=\delta/(2^{n+1}nK)\), the convex strict-subsolution construction and the ordered-background mixed-mass expansion. No contradiction was found; upstream contact localization and global non-pluripolar mixed-mass bound remain independent proof obligations.
- **§13.25.1–3:** directly checked decomposition change \(u\mapsto u-f\), ordinary-model reprojection, and the common lower-volume estimate; the three upper-volume errors yield the stated two-sided comparison. **§13.25.5**: read the statement and the nonanalytic volume-sandwich steps only, without certifying any analytic approximation construction.
- **§13.26.1/.3:** checked the form inequalities \(c_\varepsilon\widehat\theta_\varepsilon\ge\theta+\varepsilon h\) and the upper/lower model sandwiches, plus the three-error comparison and two-reference transport argument. **§13.26.7**: statement and dependency reading only, not its analytic approximation proof.
- **§13.31.1:** checked the ordinary radial convolution/Lebesgue differentiation argument, truncation by \(\{u>-j\}\), a.c.-matrix monotonicity, and Fatou/Bedford–Taylor passage. In particular, it proves only \((T_{\rm ac})^n\le\langle T^n\rangle\), not equality. **§13.31.3**: the existence of the same-class analytic modification approximants is an upstream input not re-proved here; the independent example above does not invoke it.
- **§13.32:** *not reviewed.* Its dedicated gentle/Demailly quasi-equisingular approximation input is **deferred-by-user**. Similarly, no attempt was made to complete the regularization/Bergman/L²/Ohsawa–Takegoshi/multiscale atlas/positivity-loss programme through §§13.25–13.26.
- **Audit limitations:** no section or full proof dependency tree certified; no main/source/reading-edition/registry/tag files altered; no CI, site build, formal verification or website publication performed. Previous ledger findings remain unchanged.

