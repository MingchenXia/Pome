# Fine neighborhoods have Lebesgue density one: full direct §§2.8 and 4.2 audit (2026-11-21)

## Revision, scope and verdict

- Production \`main\` reviewed: \`b6933b772f41b45918f7e25ed1afbbb1fd892272\` (re-fetched during this session).
- Full integrated current §2.8: \`docs/sections/measures-and-distributions--densities-and-differentiation-of-integrals/index.html\`, blob \`1b600ca8444edebc8e05e300cb86ae371e9f8535\`, mathematical lines 7–225 (comments/navigation excluded).
- Full integrated current §4.2: \`docs/sections/fine-topology-and-balayage/index.html\`, blob \`d4c8eed09391441b4b6d13e2fa402a60da70be0d\`, mathematical lines 7–577 (comments/navigation excluded).
- Directly checked the statements and displayed arguments in both sections. In §2.8: dyadic bounded Radon–Nikodym construction, dominated real distributions, cube maximal inequality, Lebesgue differentiation, Poincaré on cubes and the pointwise quadratic expansion at Lebesgue points of a bounded distributional Hessian. In §4.2: fine subbasis/thinness, polar discreteness, Green-energy Hilbert identity, equilibrium probability minimization, reduction and Poisson modification, sweeping with compact bounded and finite-energy source measures, Choquet countable subcovers modulo polar sets, quasi-openness, and the classical-fine/plurifine distinction.
- New finding: one **low / verified conditional deduction** sharpening §4.2.5. **No new confirmed incorrect printed theorem or proof step.** Complete transitive proof-chain certifications: **zero**. Historic first visits are unreconciled and not asserted.

## Finding POME-FINE-NEIGHBORHOOD-LEBESGUE-DENSITY-ONE-001 — verified conditional deduction (low severity)

### Printed anchors and hypotheses

The current §4.2.4 (source tag \`D80928DD\`, permanent \`CAAD6BABA60C\`, lines 52–81) shows that for every fine neighborhood \`N\` of a point \`x\` in an open \`\Omega\subset\mathbb R^d\`, \`d\ge2\`, there are a Euclidean neighborhood \`V\` of \`x\`, a subharmonic function \`u\in SH(V)\`, and a finite real \`a<u(x)\` such that
\[
x\in E:=V\cap\{u>a\}\subset N.
\]
The current §4.2.5 (source \`01F6C408\`, permanent \`9E787ECDB068\`, lines 86–99) proves only that every sufficiently small Euclidean ball centered at \`x\` contains a Borel subset of \`N\` of **positive** Lebesgue measure. The §4.2.22 quasi-Lindelöf result (source \`333EA4BE\`, permanent \`730413AAC920\`, lines 491–518) establishes Lebesgue measurability of fine-open sets in the completed measure space. §2.8.3 (source \`01CADB42\`, permanent \`CF98893DE93E\`, lines 80–117) supplies the separate differentiation context; its almost-everywhere assertion is not itself used to upgrade §4.2.5.

### Stronger statement

For any **fine-open** set \`U\subset\Omega\` and every \`x\in U\`,
\[
\boxed{\quad\lim_{r\downarrow0}\frac{|U\cap B(x,r)|}{|B(x,r)|}=1.\quad}
\]
For **every fine neighborhood** \`N\` (not assumed measurable), there exists a Borel set \`E\subset N\` containing \`x\` whose relative density at \`x\` is one. If \`N\` happens to be Lebesgue measurable, it has density one at \`x\` as well. In particular, the fine topology on \`\Omega\` is included in the Lebesgue density topology (under completed Lebesgue measurability).

There is an explicit *local quantitative* strengthening. Choose \`V,u,a\` as above and \`r_0>0\` with \`\overline{B(x,r_0)}\subset V\`. For \`0<r<r_0\` put \`M(r)=\sup_{\overline{B(x,r)}}u\`; then \`u(x)\le M(r)<\infty\` and
\[
\boxed{\quad
\frac{|B(x,r)\setminus E|}{|B(x,r)|}
\le\frac{M(r)-u(x)}{M(r)-a}\longrightarrow0 .
\quad}
\]
The conclusion requires the actual finite-value inequality \`u(x)>a\`; it does **not** assert that an arbitrary superlevel set has density one at an arbitrary boundary point or at a point where \`u=-\infty\`.

### Complete deduction

Subharmonicity gives the ball submean inequality for \`u\`. Since \`u\le M(r)\` everywhere on the ball and \`u\le a\` off \`E\`, integration yields
\[
u(x)\le \frac{1}{|B_r|}\int_{B_r}u
\le \frac{|E\cap B_r|}{|B_r|}M(r)+
\left(1-\frac{|E\cap B_r|}{|B_r|}\right)a.
\]
The integrals are legitimate for a subharmonic function finite at \`x\`: it is locally integrable and cannot be identically minus infinity on the component. Rearrangement (using \`M(r)-a>0\`) gives the boxed inequality. Upper semicontinuity at \`x\` gives
\[
u(x)\le M(r),\qquad \limsup_{r\downarrow0}M(r)\le u(x),
\]
so \`M(r)\to u(x)\` and the right side tends to zero. Since \`E\subset N\`, its relative density-one property also gives the outer-measure complement bound for \`N\`; if \`U\` is fine-open, §4.2.22 makes \`U\` completed-Lebesgue-measurable and the density identity follows.

The phenomenon is genuinely topological and not an assertion of Euclidean openness. The countable dense polar set \`\mathbb Q^d\cap\Omega\` is finely closed by §4.2.6 (permanent \`498B2C3E2413\`, lines 104–141); its complement is a fine-open, Euclidean-nonopen set of relative Lebesgue measure one in every sufficiently small ball centered at one of its points.

### Status, dependencies, effects and correction

- **Classification:** low / **verified conditional deduction**, not a confirmed printed error, not a complete upstream certification, not a source or registry repair.
- **Checked mathematical input:** the printed fine-neighborhood basis §4.2.4 and standard submean/usc properties (printed §3.4.5), and the fine-open measurability result §4.2.22 for the measurable conclusion.
- **New dependent observation:** §4.2.5 can be strengthened from *positive mass* to *full Euclidean density at the center*. The result also clarifies the difference between almost-everywhere Lebesgue differentiation in §2.8.3 and **every-point** density for fine-open neighborhoods.
- **Proposed correction/addition (review-only):** append this corollary and its two-line supremum/submean argument after §4.2.5. Do not replace or delete existing text, references, source tags, or attribution. No production edit authorized this session.
- **Still unverified transitively:** §3.4.5 submean theory, §4.1.26 fine quasi-continuity and polar exceptions, §4.1.17 energy-polar noncharging, §3.4.22 Choquet lemma, and §4.2.22's whole dependency chain. These were read as internal inputs, not recursively certified.

## Independent mathematical audit notes (no additional finding counted)

### §2.8

1. **Dominated measures:** §2.8.1, lines 11–46, is based on finite-measure dyadic conditional averages \`g_k\`, with the orthogonality \`\|g_l-g_k\|_2^2=\|g_l\|_2^2-\|g_k\|_2^2\`. The passage to a Borel density and the patching of local cubes uses countable partitions, not unjustified pointwise convergence of all dyadic averages.
2. **Distributions:** §2.8.2, lines 54–75, uses positivity of \`C\nu\pm T\` and uniqueness of Radon representatives. The local patching uses locally finite test partitions and bounded densities.
3. **Lebesgue differentiation:** §2.8.3, lines 80–117, uses a finite disjoint subcollection with factor \`3^d\`, density of compactly supported continuous functions in \`L^1\`, and then a compact exhaustion; there is no assumption that almost-everywhere Lebesgue points are all points.
4. **Real Hessians:** §2.8.4–5, lines 125–225, checks the cube Poincaré scaling \`l\`, \`dC\` as the operator-norm bound for a matrix with all entries bounded by \`C\`, and the distributional chain-rule scaling in \`G_r(y)=(\nabla f(x+ry)-\nabla f(x))/r-A(x)y\`. The Taylor claim is restricted to common Lebesgue points of the Hessian coefficients, not asserted at every point.

### §4.2

1. **Fine bases:** §4.2.2–8, lines 24–170. The finite positive subharmonic witness at the base point is essential in §4.2.4, and the restriction of local polar measures away from that point in §4.2.6 avoids accidentally forcing the witness to minus infinity at its center.
2. **Energy:** §4.2.11–12, lines 196–286. The positive-definite signed Green energy is obtained as an \`L^2\` gradient norm; the equilibrium minimizer uniqueness uses strict quadratic polarization for finite-energy signed measures. Finite-energy measures do not charge polar sets.
3. **Balayage:** §4.2.13–18, lines 290–450. The compact reduction of §4.2.14 has bounded Green potential and an actual finite-energy swept measure, while §4.2.18 treats a finite-energy source using a monotone sequence of bounded-potential **partial measures**; no claim of monotonicity for arbitrary source families has been substituted.
4. **Fine covers:** §4.2.20–25, lines 455–577. The quasi-Lindelöf exception is polar, not necessarily empty, and the topology induced on a complex hypersurface by the classical fine topology is contrasted with the complex-line-generated topology without treating the two as equal.

## Coverage and outstanding scope

Exactly **two full present integrated sections** were directly read: §§2.8 (lines 7–225) and 4.2 (lines 7–577), with selected earlier-result statements referenced only as internal prerequisites. This does not imply these were the first historical reviews or that the collection is fully audited. **Zero** complete transitive proof-chain certifications and **zero** builds/tests/CI executions are claimed. Existing findings and deferred items remain unchanged. In particular, Demailly regularization/approximation, dedicated Bergman, L², Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof-completion programmes remain **deferred-by-user**, not resolved or certified. No source/body/registry/canonicalization/permanent tag/main/site changes are part of this report.
