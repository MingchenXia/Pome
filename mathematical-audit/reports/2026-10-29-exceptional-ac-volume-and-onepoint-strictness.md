# Exceptional-divisor absolute-continuous volume and sharp strict-point vanishing hypothesis

**Audit date:** 2026-10-29. **Reviewed production main:** b6933b772f41b45918f7e25ed1afbbb1fd892272. **Scope:** direct, selected mathematical comparison of the current integrated reading edition in §§13.31.1, 13.31.3–4 and 10.92.1, with §10.91.2 used solely to identify the strictness hypothesis and §10.90 read only as the heading for its subject group. **No entire theorem proof chain, section or chapter is certified.**

This report is independent of the user-deferred Demailly approximation/regularization, Bergman, weighted L2, Ohsawa–Takegoshi, multiscale-atlas, and positivity-loss proof-completion programmes. The analytic existence/vanishing inputs elsewhere in the reading edition are **not** reopened. Neither item below is a counterexample to its printed theorem.

## POME-AC-VOLUME-EXCEPTIONAL-NEGATIVE-001

**Severity:** low. **Status:** verified conditional deduction; the printed theorem and corollaries are correct. **Suggested editorial action:** optional explicit worked example after Corollary 13.31.4, making clear that determinant volume need not equal the cohomological top self-intersection on a non-nef big class.

**Exact integrated reading-edition anchors:** <code>docs/sections/absolutely-continuous-and-non-pluripolar-mass/index.html</code>, main blob <code>bea17d8041a7af4a252913e0f700b44d77521f82</code>. Lemma 13.31.1 (permanent tag <code>C7894CAD8593</code>, source <code>transcendental-positive-cones:6D2B462A</code>, physical lines 7–98); Corollary 13.31.3 (tag <code>1E1CF458220D</code>, source <code>transcendental-positive-cones:A2E98A80</code>, lines 103–120); Corollary 13.31.4 (tag <code>04768594F11F</code>, source <code>transcendental-positive-cones:AA4B08E5</code>, lines 124–136).

**Claim and hypotheses.** Let $\pi:X=\mathrm{Bl}_{p}\mathbb P^2\to\mathbb P^2$ be the blowup at one point, let $H=\pi^*c_1(\mathcal O_{\mathbb P^2}(1))$ and let $E$ be the exceptional divisor class. For each positive integer $a$, the integral class $\alpha_a=H+a[E]$ is big, and
$$
\operatorname{Vol}(\alpha_a)=1,\qquad
\alpha_a^2=1-a^2.
$$
A closed positive current in this class attaining the determinant supremum in Corollary 13.31.4 is
$$
T_a=\pi^*\omega_{\mathrm{FS}}+a[E],\qquad
\int_X(T_{a,\mathrm{ac}})^2=1,
$$
where $\int_{\mathbb P^2}\omega_{\mathrm{FS}}^2=1$. Thus for $a=2$, the class has **negative cohomological self-intersection $-3$** but positive volume $1$, and its absolutely continuous determinant already attains the optimal value. The discrepancy $\operatorname{Vol}(\alpha_a)-\alpha_a^2=a^2$ is unbounded along these explicit big classes.

**Proof, including the section-count step.** On $E\simeq\mathbb P^1$, the normal bundle is $\mathcal O_E(E)=\mathcal O_{\mathbb P^1}(-1)$ and $\mathcal O_E(H)$ is trivial. For $m\ge1$ and every integer $j\ge1$, restriction gives the exact sequence
$$
0\longrightarrow \mathcal O_X(mH+(j-1)E)
\longrightarrow\mathcal O_X(mH+jE)
\longrightarrow\mathcal O_E(-j)\longrightarrow0.
$$
Since $H^0(E,\mathcal O_E(-j))=0$, the induced map on $H^0(X,\cdot)$ is an isomorphism. Iterating from $j=1$ to $ma$ gives
$$
h^0(X,\mathcal O_X(mH+maE))
=h^0(X,\mathcal O_X(mH))
=h^0(\mathbb P^2,\mathcal O(m))
=\binom{m+2}{2}.
$$
By the definition of volume of an integral divisor on a projective surface,
$\operatorname{Vol}(\alpha_a)=\lim_{m\to\infty}(2/m^2)h^0(X,mH+maE)=1$; in particular $\alpha_a$ is big. The intersection relations $H^2=1$, $H\cdot E=0$, $E^2=-1$ give $\alpha_a^2=1-a^2$.

The divisor current $[E]$ is concentrated on a Lebesgue-null analytic curve, whereas $\pi^*\omega_{\mathrm{FS}}$ is smooth, so $T_{a,\mathrm{ac}}=\pi^*\omega_{\mathrm{FS}}$ almost everywhere. The exceptional curve has zero smooth volume and $\pi$ is a biholomorphism off it, whence
$\int_X(\pi^*\omega_{\mathrm{FS}})^2=\int_{\mathbb P^2}\omega_{\mathrm{FS}}^2=1$.
The original Corollary 13.31.4, using its Lemma 13.31.1 upper bound, then certifies that no other positive current in $\alpha_a$ has larger absolutely continuous determinant integral. **The example, section growth, and equality for the displayed current are proved directly; the general supremum upper bound remains an identified internal input, not re-proved here.**

**Dependents / nonclaims:** This tests non-nef positive-cone volume conventions, numerical positive products, and any attempted replacement of $\operatorname{Vol}(\alpha)$ by $\alpha^n$ in §§13.31–13.32 or §10 positivity arguments. It says nothing about numerical intersection of arbitrary higher-dimensional currents. It is not a duplicate of the existing full-mass but purely singular absolutely-continuous-current example: here a current **attains full determinant volume** while the class has arbitrarily negative algebraic self-intersection.

## POME-ONEPOINT-STRICT-ELLIPTIC-PRODUCT-001

**Severity:** low. **Status:** verified conditional deduction; the printed one-point strictness hypothesis is essential, and Corollary 10.92.1 is correct. **Suggested editorial action:** optional sharpness example after Corollary 10.92.1; retain strict positivity at one point.

**Exact integrated reading-edition anchors:** <code>docs/sections/one-point-curvature-positivity-and-vanishing--one-point-vanishing-on-compact-complex-manifolds/index.html</code>, main blob <code>92bd47c3486213df134952fce23f4291c3ae81ca</code>, Corollary 10.92.1 tag <code>B3500F172230</code>, source <code>demailly-complex-geometry:269B809F</code>, physical lines 7–29, especially the strict-point hypothesis at line 8 and vanishing claims at lines 10 and 16. Comparison-only conditional Theorem 10.91.2 tag <code>8532D3ED47E8</code>, source <code>demailly-complex-geometry</code>, <code>docs/sections/one-point-curvature-positivity-and-vanishing--one-point-positivity-and-modification-descent/index.html</code>, blob <code>95b3f78a729e01664c4a24d3ef8aa96143ead523</code>, lines 46 onward.

**Claim and hypotheses.** For every integer $n\ge2$, take an elliptic curve $C$, the compact connected projective manifold $X=\mathbb P^{n-1}\times C$, and
$$
L=p_1^*\mathcal O_{\mathbb P^{n-1}}(n).
$$
The natural metric on the rank-one bundle $L$ has semipositive curvature at every point, but its curvature vanishes along $T C$ at **every** point, so it is nowhere strictly Griffiths/1-positive. Nevertheless,
$$
H^{n,1}_{\bar\partial}(X,L)\simeq\mathbb C\ne0,
\qquad
H^{0,n-1}_{\bar\partial}(X,L^{-1})\simeq\mathbb C\ne0.
$$
Thus dropping *strictness at one point* from either the positive-bundle $(n,q)$ vanishing or the seminegative line-bundle $(0,q)$ vanishing gives false assertions, **even on projective manifolds**. This does not test a general higher-rank $m$-positivity threshold.

**Complete elementary verification.** The pullback Fubini–Study curvature of $L$ is semipositive and has the elliptic tangent direction in its kernel everywhere. Its negative is a seminegative curvature form for $L^{-1}$, and similarly is never strictly negative. Since $K_C$ is trivial and $K_{\mathbb P^{n-1}}=\mathcal O(-n)$, one has $K_X\otimes L\simeq\mathcal O_X$. Dolbeault and Künneth yield
$$
H^{n,1}_{\bar\partial}(X,L)
=H^1(X,K_X\otimes L)
=H^1(X,\mathcal O_X)
=H^1(C,\mathcal O_C)
\simeq\mathbb C.
$$
For the negative bundle, Serre duality on projective space gives
$$
H^{n-1}(\mathbb P^{n-1},\mathcal O(-n))
\simeq H^0(\mathbb P^{n-1},\mathcal O)^*
\simeq\mathbb C;
$$
all intermediate cohomology groups of $\mathcal O(-n)$ vanish (for $n=2$, its $H^0$ vanishes). Künneth then gives
$$
H^{0,n-1}_{\bar\partial}(X,L^{-1})
=H^{n-1}(X,L^{-1})
\simeq H^{n-1}(\mathbb P^{n-1},\mathcal O(-n))
\otimes H^0(C,\mathcal O_C)
\simeq\mathbb C.
$$
Here $q=1$ in the positive case and $q=n-1<n$ in the negative case, exactly within the asserted vanishing ranges when strictness is present. Compactness, connectedness, and even Kählerness are all satisfied, isolating the missing strictness as the obstruction.

**Dependents / nonclaims:** §10.91.2, §10.92.1, and one-point positivity arguments for vanishing; do not weaken strictness to semipositivity alone. This example does **not** audit the general external geometric elimination/compact Kähler modification input, nor any Bergman/L2/extension proof chain. It is different from the prior *disconnected-components* caveat in the audit ledger: this example is connected.

## Scope and verification boundary

- **New passage-level mathematical inspection:** Corollary 13.31.3's section-growth/modification claim and Corollary 13.31.4's determinant-volume statement, with its upper bound (Lemma 13.31.1) used as an established conditional input; Corollary 10.92.1's positive/negative strictness hypotheses and vanishing ranges. **Incremental** on previously selected §§13.31 and 10.92.
- **Previously inventory-only §10.90:** checked that it is a subject heading, permanent tag <code>3209A23008E4</code>, not a hidden independent theorem. It is marked *orientation only*, not proof review.
- Both explicit model calculations above were completed by direct sheaf exact sequences, intersection numbers, Dolbeault/Künneth/Serre duality. **No project build, automated tests, CI, browser verification, formal proof checking, or full mathematical certification were performed.**
- Retain the existing **25 chapters / 747 numbered sections** matrix from the unchanged pinned current-main ToC; this is **not** a fresh exhaustive count. **Zero complete section or chapter certifications.**
- Previously established confirmed errors, proof gaps, genuine external dependencies, and all user-deferred Demailly approximation/regularization/Bergman/L2/OT/multiscale-atlas/positivity-loss proof work are not marked repaired or resolved. Source manuscripts, reading-edition HTML, site, proof registries, canonicalizations, permanent tags, and production main remain untouched.
