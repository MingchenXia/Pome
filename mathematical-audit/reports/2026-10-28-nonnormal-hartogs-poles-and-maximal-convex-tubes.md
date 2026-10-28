# Mathematical audit — 28 October 2026: isolated nonnormal Hartogs poles and maximal convex tubes

**Production main inspected:** <code>b6933b772f41b45918f7e25ed1afbbb1fd892272</code>.
**Audit branch starting HEAD:** <code>8574b4195dc023866c9763a133a0138db90b5510</code>.
**Boundary:** mathematical audit only; no production/source/renderer/tag/website/CI changes. Both substantive findings below are **verified conditional deductions** about sharpness of printed assumptions, **not counterexamples to the statements actually printed**. They are distinct from earlier §9.38/9.39 audit entries. The proofs do not use any part of the author-excluded Demailly approximation programme.

## POME-HARTOGS-NORMALITY-ISOLATED-POLE-001

**Severity:** low. **Status:** verified conditional deduction; printed Corollary 9.38.1 and Lemma 9.38.2 remain correct with normality.

**Exact integrated anchors:** <code>docs/sections/normal-spaces-and-tube-continuation--continuation-on-normal-complex-spaces/index.html</code>, main blob <code>fa09a923ef076a99d638d038020ddd3b884afaa7</code>. Section §9.38 tag <code>48351356D0F9</code> / source <code>demailly-complex-geometry:EB3237B0</code>, lines 5–7 (reduced, Hausdorff, countable-basis and normality conventions). Corollary **9.38.1**, permanent tag <code>512196636E86</code>, source <code>demailly-complex-geometry:75A8246F</code>, lines 10–26. Lemma **9.38.2**, permanent tag <code>DA978F0F96EA</code>, source <code>demailly-complex-geometry:F60855BF</code>, lines 30–54. Related Theorem 9.38.5 tag <code>F35BA7139EC4</code>, lines 90–109, depends on normality and uses a different meromorphic-extension assertion; its full proof chain is *not* certified here.

**Claim checked and complete model proof.** The normality assumption cannot simply be dropped from codimension-two Hartogs continuation or the codimension-one purity of the meromorphic *pole set*, even for an irreducible reduced complex surface and a function meromorphic on the entire surface.

Take the finite monomial algebra
$$
A=\mathbb C[s^2,st,t^2,s^3,t^3]\subset\mathbb C[s,t]
$$
and its reduced affine analytic surface $X=\operatorname{Spec}(A)^{an}$. It is the closed image of the polynomial map
$$
\Phi:\mathbb C^2\longrightarrow\mathbb C^5,\qquad
(s,t)\longmapsto (s^2,st,t^2,s^3,t^3).
$$
Indeed $s$ and $t$ are integral over $A$ by the monic relations $S^2-s^2$ and $T^2-t^2$; thus $\mathbb C[s,t]$ is a finite $A$-module and $\Phi$ is a finite map with closed analytic image. Equivalently, $\Phi$ is proper directly: the $s^2,t^2$ coordinates bound $|s|,|t|$ above the inverse image of a compact set. The source is irreducible; consequently $X$ is reduced and irreducible of complex dimension two, Hausdorff and second countable. Denote its vertex by $o=\Phi(0,0)$.

The map $\Phi$ is an isomorphism outside $o$. On $s\ne0$, recover $s$ from coordinate 4 divided by coordinate 1 and then $t$ from coordinate 2 divided by $s$; on $t\ne0$, recover $t$ from coordinate 5 divided by coordinate 3 and then $s$ from coordinate 2 divided by $t$. These are holomorphic formulas on the respective image charts and cover $X\setminus\{o\}$.

Therefore the function $f$ defined by $f(\Phi(s,t))=s$ is holomorphic on $X\setminus\{o\}$. It is *meromorphic on all of* $X$: in the fraction field of the irreducible local coordinate ring, $f$ is the quotient of coordinates 4 and 1, with nonzero denominator. But $f$ is not holomorphic at $o$. If it were, it would locally equal the restriction of an ambient holomorphic function $H$ on $\mathbb C^5$ (the defining local model of an analytic subspace). By uniqueness on the dense complement, $H\circ\Phi=s$ near the origin of $\mathbb C^2$. Every coordinate of $\Phi$ vanishes to order at least two; hence $d(H\circ\Phi)_0=0$, while $d(s)_0\ne0$, a contradiction.

Thus the pole set in the *precise sense of Lemma 9.38.2*, namely the non-holomorphic germ locus of a meromorphic function, is
$$
P_f=\{o\},\qquad \operatorname{codim}_X P_f=2,
$$
and $f\in\mathcal O(X\setminus P_f)$ does not extend holomorphically to $X$. The irreducible surface is not normal at $o$: $s$ is integral over $A$ but is absent from its local holomorphic ring, as just shown. So neither conclusion contradicts the original **normal-space** statements.

**Disposition:** preserve normality in Corollary 9.38.1, Lemma 9.38.2 and any reader-side generalization. This test also distinguishes the actual meromorphic pole set from the vanishing locus of an arbitrary chosen denominator. Optional explicit sharpness example only; no patch to original mathematics. Affected dependencies to watch: §9.38.5 meromorphic continuation and §§9.58–9.60 nonnormal analytic models. The finite algebraic-to-analytic identification is the sole standard structural input; no global Hartogs theorem is used to prove this model.

## POME-BOCHNER-TUBE-CONVEX-HULL-MAXIMAL-001

**Severity:** low. **Status:** verified conditional deduction; printed Theorem 9.39.7 remains correct.

**Exact integrated anchors:** <code>docs/sections/normal-spaces-and-tube-continuation--holomorphic-extension-from-a-connected-tube/index.html</code>, main blob <code>a94e3aa490fee004284dab37f4f6e35094bf2bfa</code>. Section §9.39 tag <code>DD3391B92728</code> / source <code>demailly-complex-geometry:DA207C74</code>, lines 5–10; Theorem **9.39.7** (Bochner tube theorem), permanent tag <code>E5EB0154B387</code>, source <code>demailly-complex-geometry:F7AA195B</code>, statement lines 97–100 and proof lines 103–148. Lemma 9.39.2, tag <code>7D65E928B1FB</code>, lines 27–60, is a *previously reviewed* internal proof input, not independently re-certified here. Proposition 9.39.10 tag <code>08FF9CEC303A</code> is a selected dependent.

**Claim and direct proof.** Let $\omega\subset\mathbb R^n$ be nonempty, open and connected, and put $C=\operatorname{conv}\omega$. Theorem 9.39.7 ensures that *every* holomorphic function on the tube $T_\omega=\omega+i\mathbb R^n$ extends to $T_C=C+i\mathbb R^n$. This common guaranteed convex-tube base is **maximal**, in the following precise sense: for every point $z_0=x_0+iy_0\notin T_C$ there is a holomorphic function on $T_\omega$ that has no holomorphic extension to any connected open domain containing both $T_C$ and $z_0$.

Indeed $C$ is open and convex. Separation of the point $x_0\notin C$ from the open convex set $C$ gives a *nonzero real linear form* $\ell$ with
$$
\ell(x)<\ell(x_0)\qquad\text{for every }x\in C.
$$
This strict inequality on $C$ holds also when $x_0\in\partial C$: a supporting linear form may attain its bound on the boundary, but cannot attain it at an interior point unless it vanishes. Complexify $\ell$ to $\ell_{\mathbb C}(z)=\sum_{j=1}^na_jz_j$ for real coefficients $a_j$, and define
$$
F_{z_0}(z)=\frac{1}{\ell_{\mathbb C}(z-z_0)}.
$$
For every $z=x+iy\in T_C$ the real part of the denominator equals $\ell(x)-\ell(x_0)<0$. Thus $F_{z_0}$ is holomorphic on $T_C$ and in particular on $T_\omega$. Yet its denominator vanishes at $z_0$. Suppose $\widetilde F$ were holomorphic on a connected open $D$ containing $T_C\cup\{z_0\}$ and agreeing with $F_{z_0}$ on $T_\omega$. The holomorphic function $\ell_{\mathbb C}(z-z_0)\widetilde F(z)-1$ vanishes on the nonempty open subset $T_\omega$, hence identically on $D$ by the identity theorem, but evaluates to $-1$ at $z_0$. Contradiction.

Therefore the convex-hull extension of Theorem 9.39.7 cannot be **uniformly enlarged for all input functions**. This is not an assertion that *each individual* function has precisely this maximal domain (for example constants extend to all of $\mathbb C^n$). It also does not replace the theorem's connectedness requirement. The proof of maximality is elementary convex separation and the holomorphic identity theorem; the existence of the extension to $T_C$ is the printed Bochner theorem, retained as a conditional input rather than re-proved here.

**Disposition:** optional sharpness corollary for Theorem 9.39.7, preserving its connectedness and open-base assumptions; useful for §9.39.10 and any subsequent geometric-envelope interpretation. Do not confuse common extension domains with function-specific analytic continuation, and preserve historical attribution to Bochner.

## Statement-level cross-check, not a proof certification: §18.3

First targeted comparison of an otherwise **inventory-only** section: <code>docs/sections/multiplier-ideal-envelopes-and-goodness--the-kahler-characterization/index.html</code>, main blob <code>b24886056e3f78ae5322ccb763a0e4dc8c2272eb</code>, section tag <code>649A8A26E78B</code>, source <code>non-kahler-pluripotential-theory:5E9C6D83</code>, lines 5–15. Its Kähler, closed big background and positive non-pluripolar mass premises agree with the original three-way characterization in Theorem 18.1.2, permanent tag <code>F9085BB700B0</code>, <code>docs/sections/good-singularities/index.html</code> main blob <code>638301f48e081c04a2d766e827b577b073acb359</code>, statement lines 42–65. The three conditions are $d_S$-closure of analytic types, equality of non-pluripolar masses, and equality of ordinary/ideal envelopes. §18.3 is expository and repeats this theorem with its qualifications; no new counterexample or duplicate mathematical theorem was identified. The excluded regularization-dependent proof of Theorem 18.1.2 was **not opened or certified**. Record this as **statement-level/context only**, not a promoted proof-level audit and not a full-section certification.

## Coverage, unresolved dependencies, and exclusions

- **New proofs:** two explicit sharpness countermodels, incrementally revisiting selected arguments in **§9.38.1–2** and **§9.39.7**. §9.37 is a heading/context only. **First statement-level** matching of §18.3 against §18.1.2, with no proof certification. Previous findings and statuses in §§9.38–9.39 remain unchanged, including the earlier convex-log majorant computation.
- **Review inventory:** retain all **25 chapters and 747 distinct numbered section rows**; **zero full sections or chapters certified**. The majority of section-level proofs and many upstream internal results remain unreviewed; in particular, neither the full §9.38 normal-space extension chain nor the full §9.39 disc-continuation chain was recertified.
- **External/conditional inputs:** finite algebraic-to-analytic model construction and ordinary convex separation for the new models; the printed Bochner theorem is conditional for the common-extension existence direction. No new false printed theorem, proof gap, genuine duplication or verified complete repair established.
- **User-deferred:** **all** Demailly approximation/regularization and its dedicated Bergman, weighted L², Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof-completion programme remain **deferred-by-user**, neither resolved nor certified. No work on these premises or under another label.
- No project tests, full builds, browser tests, CI, formal verification, main/site/source/permanent-tag/registry changes or automatic publication were undertaken.