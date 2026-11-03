# 2026-11-04 — Pinch-point normalization, conductor and non-open unibranch locus

**Finding:** POME-NORM-PINCH-CONDUCTOR-BRANCH-JUMP-001  
**Classification:** low / **verified conditional deduction** (explicit normalisation model; **no printed theorem refuted**).  
**Reviewed production main:** b6933b772f41b45918f7e25ed1afbbb1fd892272.  
**Scope:** A genuinely two-dimensional singular analytic space and exact sheaf/conductor and branch-fibre computation; this is different from previously audited one-dimensional monomial curves and tangential cusp–line conductors. No regularization, Bergman, weighted L², Ohsawa–Takegoshi, multiscale-atlas, or positivity-loss arguments are involved.

## Pinpointed integrated targets (physical HTML lines)

- File: \`docs/sections/complex-spaces-and-modifications--reduced-spaces-and-normalization/index.html\` (main blob \`06439f43d1ce8e83d2529682c9a630bffa3d9c22\`).
- Weakly holomorphic definition, line **34**; Proposition **9.4.3**, source \`foundations-of-pluripotential-theory:AC231B8D\`, permanent tag \`36422A732754\`, lines **52–79** (integral closure and finite limits on an *irreducible germ*).
- Lemma **9.4.4**, source \`foundations-of-pluripotential-theory:E60680A7\`, permanent \`D73CC9F08C05\`, lines **87–108** (analytic non-normal locus and conductor-like endomorphism sheaf).
- Lemma **9.4.5**, source \`foundations-of-pluripotential-theory:571B5EA0\`, permanent \`58E87F89D557\`, lines **116–136** (local finite normalization and branch fibres).
- Theorem **9.4.6**, source \`foundations-of-pluripotential-theory:7042BB57\`, permanent \`12A47DB401E2\`, lines **141–159** (global normalization, exact pushforward sheaf).
- Definition **9.4.8**, source \`foundations-of-pluripotential-theory:C9F1CBB2\`, permanent \`0E1E539882AD\`, line **180**; Corollary **9.4.9**, source \`foundations-of-pluripotential-theory:405861C0\`, permanent \`EE1633042D3D\`, lines **184–191** (global unibranch hypothesis).

## Complete calculation

Consider the reduced hypersurface
\[
 X=\{(x,y,z)\in\mathbf C^3:x^2=y^2z\},
 \qquad L=\{x=y=0\}\subset X,
\]
and the map
\[
 \nu:\mathbf C^2_{y,t}\longrightarrow X,\qquad (y,t)\longmapsto(yt,y,t^2).
\]
Everything below may be restricted to a sufficiently small neighborhood of the origin; no compactness of X is required.

**1. Reduced, irreducible at the pinch point, but singular along a line.** The polynomial $f=x^2-y^2z$ is irreducible in $\mathbf C\{x,y,z\}$ at the origin. Indeed, Weierstrass preparation in $x$ would make a nontrivial factorization into $(x-a(y,z))(x+a(y,z))$, requiring $a(y,z)^2=y^2z$. Unique factorization in the regular local ring $\mathbf C\{y,z\}$ first implies $a=yb$, then $b^2=z$, impossible because the $z$-adic order of a square is even. Thus $(X,0)$ has **one** irreducible branch. The gradient $(2x,-2yz,-y^2)$ vanishes exactly on $L$, so $X_{\mathrm{sing}}=L$ and $X_{\mathrm{reg}}=\{y\ne0\}$.

At a different point $p=(0,0,z_0)\in L$ with $z_0\ne0$, a holomorphic square root of $z$ exists near $p$, and
\[
 x^2-y^2z=(x-y\sqrt z)(x+y\sqrt z).
\]
The two distinct local factors define two smooth branches. Thus the **unibranch-at-a-point property is not open** on this example: the origin is unibranch, while every neighborhood of it contains two-branch singular points.

**2. Finite normalization and fibre jump.** Write
\[
 A=\mathbf C\{x,y,z\}/(x^2-y^2z)
   \simeq \mathbf C\{y,z\}\oplus x\,\mathbf C\{y,z\}
   =\mathbf C\{y,yt,t^2\}\subset B=\mathbf C\{y,t\}.
\]
Here the direct sum is as modules over $\mathbf C\{y,z\}$; the equality of the displayed analytic rings uses Weierstrass division. Also
\[
 B=\mathbf C\{y,z\}\oplus t\,\mathbf C\{y,z\}=A+At,
 \qquad t^2=z,\quad yt=x.
\]
Hence $B$ is finite integral over $A$. The function-field extensions agree because $t=x/y$ on $\{y\ne0\}$; $B$ is regular, hence integrally closed. For any $q$ in the common fraction field integral over $A$, its monic equation over $A\subset B$ makes it integral over $B$, so $q\in B$. Thus $B$ is **exactly** the integral closure of $A$. The map $\nu$ is finite and bimeromorphic; globally it is proper since $|t|^2=|z|$ bounds its inverse image of any compact subset of $X$.

Over $p=(0,0,z_0)$ the fibre is precisely $\{(0,t):t^2=z_0\}$. Therefore
\[
 \#\nu^{-1}(0,0,0)=1,\qquad
 \#\nu^{-1}(0,0,z_0)=2\quad(z_0\ne0),
\]
and the map is an isomorphism on $X_{\mathrm{reg}}$. It is **not injective over any neighborhood of the origin**, although the fibre over the origin is a singleton. This matches the *local-branch* formula of Theorem 9.4.6 and does not contradict Corollary 9.4.9: that corollary requires **every** germ on X to be irreducible, not merely the germ at the chosen point.

**3. The exact weakly holomorphic quotient and conductor.** On $X_{\mathrm{reg}}$, the function $t=x/y$ is holomorphic and satisfies $t^2=z$, so it is locally bounded near the entire singular line. Thus $t$ belongs to the sheaf of **weakly** holomorphic functions on X. At the origin $|t|=|z|^{1/2}\to0$, giving the unique finite limit claimed for an irreducible germ in Proposition 9.4.3. At a point $z_0\ne0$ on L, the two branch limits are $+\sqrt{z_0}$ and $-\sqrt{z_0}$, so the same weakly holomorphic function has **no single-valued continuous extension there**. It is not holomorphic at the origin either, since $t\notin A$ (its odd-in-$t$ term has coefficient not divisible by $y$).

Because
\[
 A=\mathbf C\{y,z\}\oplus yt\,\mathbf C\{y,z\},
 \qquad B=\mathbf C\{y,z\}\oplus t\,\mathbf C\{y,z\},
\]
we have an exact quotient
\[
 B/A\simeq t\,\mathbf C\{z\},
\]
as an $A$-module; $x$ and $y$ act by zero and $z$ acts by multiplication. Its support is exactly L, as claimed for the non-normal locus by Lemma 9.4.4. The conductor is
\[
 \mathfrak c=\{a\in A:aB\subset A\}=yB=(x,y)A.
\]
Indeed $yB\subset A$; if $aB\subset A$, reduce modulo $yB$. The image of $a$ is $a_0(t^2)\in\mathbf C\{t^2\}$, but the condition that $at\in A$ forces $a_0(t^2)t\in\mathbf C\{t^2\}$, hence $a_0=0$ by parity. This proves the reverse inclusion.

For the specific radical ideal $I=\sqrt{(y)}=(x,y)A=yB$ defining $\{y=0\}$, multiplication gives an exact isomorphism
\[
 \operatorname{Hom}_A(I,I)=\{q\in\operatorname{Frac}A:qI\subset I\}
 =\{q:qB\subset B\}=B.
\]
The middle identification uses that $I$ contains the nonzerodivisor $y$. This independently **tests the exact conductor-endomorphism mechanism** used in the proof of Lemma 9.4.4, not merely its set-theoretic support.

## Assessment and dependency ledger

**No printed error found in the selected claims.** All fibre, local-limit, integral-closure, support and weakly holomorphic identifications agree with the integrated results. The explicit non-open unibranch locus is a counterexample **only to the unprinted inference** that a singleton normalization fibre at one point implies injectivity in a neighborhood; it is not a counterexample to the actual global-unibranch homeomorphism corollary.

**Suggested text-only addition (not applied):** insert the above pinch-point computation as an example after Corollary 9.4.9, illustrating the distinction between a one-point fibre and a globally unibranch space, with the exact conductor as an optional companion to Lemma 9.4.4. Keep all source attribution and permanent tags. **Affected readers/dependents:** hypotheses of Definition 9.4.8/Corollary 9.4.9 and normalization-based descent in §§9.9–9.11; no downstream theorem is claimed false.

**Pre-existing issue explicitly left unchanged:** the separately logged global-gluing countability/paracompactness proof-step finding \`POME-NORM-COUNTABLE-COVER-001\` and the proposed repair \`POME-NORM-PERFECT-PARACOMPACT-REPAIR-001\` have already been reviewed; this report neither reopens nor resolves them.

**Coverage boundary:** new, complete calculation of this particular two-dimensional analytic normalization and the selected cited proof clauses; no full §9.4, Theorem 9.4.6 in arbitrary spaces, or transitive analytic-coherence proof certification. The main ToC remains 25 chapters / 747 sections, with zero mathematical sections completely certified. All owner-excluded work remains **deferred-by-user**. No build, tests, CI, source edit, automatic publication, or formal verification.
