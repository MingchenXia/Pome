# 2026-11-10 — Mixed absolutely continuous exterior powers versus non-pluripolar products

**Finding:** POME-NPP-MIXED-AC-WEDGE-ORDER-001  
**Classification:** low / **verified conditional deduction** (not a false printed statement; not a repaired upstream theorem).  
**Production main:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`.  
**Audit branch baseline:** \`92f375d423405ab2fec9e73333a89d5d7103d429\`.

## Source-anchored scope

This review independently extends one *part* of the integrated reading-edition proof, rather than certifying the chapter.

- \`docs/sections/absolutely-continuous-and-non-pluripolar-mass/index.html\`, blob \`bea17d8041a7af4a252913e0f700b44d77521f82\`: **Lemma 13.31.1**, source \`transcendental-positive-cones:6D2B462A\`, permanent tag \`C7894CAD8593\`, statement physical lines **8–16**, mollifier/Fatou argument **21–63**, truncation and density-limit argument **65–97**. The printed lemma only asserts the *top self-power* inequality.
- \`docs/sections/bedford-taylor-products-and-local-capacity--decreasing-continuity-and-symmetry/index.html\`, blob \`96a9e39e85fab5774ebdac0c6d9d006338a4e42c\`: **Theorem 7.3.7**, source \`foundations-of-pluripotential-theory:8B1F9B78\`, permanent \`D87C13B3250A\`, statement **133–139**, proof **143–229**. We use its locally bounded, simultaneous *decreasing-sequence* continuity only; its full proof graph is not re-certified.
- \`docs/sections/non-pluripolar-products--truncation-and-plurifine-locality/index.html\`, blob \`81be8c5acc360c96bd3c5acba05a3cdb5fafaf4c\`: the common truncations **9–16**, **Lemma 13.2.1** source \`foundations-of-pluripotential-theory:D7E74DBE\`, permanent \`6632853A40C9\`, **19–27**; **Lemma 13.2.2** source \`:CE1D6DA5\`, permanent \`D59675D9F6D8\`, **34–53**, and **Definition 13.2.4** source \`:9D8E4DD8\`, permanent \`D79952D7E272\`, **57–63**. Restriction to plurifine superlevel sets and local finiteness are kept as explicit internal dependencies.

## New conditional proposition (all mixed degrees, not only the top self-power)

Let \`U\` be a complex manifold of dimension \`n\`. Let \`1<=p<=n\` and \`T_i\` be arbitrary closed positive \`(1,1)\`-currents on \`U\`, with locally finite mixed non-pluripolar product
\[
S=\langle T_1\wedge\cdots\wedge T_p\rangle .
\]
Let \`A_i=(T_i)_{\rm ac}\` denote the measurable semipositive \`(1,1)\`-tensor obtained from the Lebesgue-absolutely-continuous coefficient measures in local coordinates. Then the *pointwise algebraic wedge* \`A_1\wedge\cdots\wedge A_p\` defines a locally integrable strongly positive \`(p,p)\`-current, although no \`A_i\` need be closed, and
\[
\boxed{\quad
0\le A_1\wedge\cdots\wedge A_p\le
\langle T_1\wedge\cdots\wedge T_p\rangle
\quad}
\]
in the positive-current ordering. For \`p=n\` and all \`T_i=T\`, this recovers the **local measure inequality** in Lemma 13.31.1. For \`p<n\`, the conclusion is a comparison of **currents**, not merely of top-degree integrals.

### Proof, bounded potentials

Work on a relatively compact coordinate ball with \`T_i=dd^c u_i\` and each \`u_i\` locally bounded psh. Choose a single sequence \`r_j\downarrow0\`; standard *radial local convolution* gives smooth psh \`u_{i,r_j}=u_i*\rho_{r_j}\downarrow u_i\` on a smaller ball. This ordinary local Bedford–Taylor mollification is **not** the user-excluded Demailly regularization or any dedicated Bergman/L²/OT programme.

The coefficientwise Lebesgue-differentiation fact already proved at lines 21–49 of Lemma 13.31.1 gives, on a common full-Lebesgue-measure set,
\[
dd^c u_{i,r_j}(x)\longrightarrow A_i(x)\qquad(i=1,\ldots,p).
\]
For a nonnegative smooth strongly positive complementary test form \`Phi\` of bidegree \`(n-p,n-p)\`, all scalar densities
\[
(dd^c u_{1,r_j}\wedge\cdots\wedge dd^c u_{p,r_j})\wedge\Phi
\]
are nonnegative, as is their pointwise limit \`(A_1\wedge\cdots\wedge A_p)\wedge\Phi\`. Fatou gives
\[
\int(A_1\wedge\cdots\wedge A_p)\wedge\Phi
\le\liminf_j\int(dd^c u_{1,r_j}\wedge\cdots\wedge dd^c u_{p,r_j})\wedge\Phi.
\]
By the **simultaneous decreasing** continuity of printed Theorem 7.3.7, the right-hand side converges to the bounded Bedford–Taylor product against \`Phi\`. Thus the claimed order holds for locally bounded potentials, and the left algebraic wedge is locally integrable: taking \`Phi\` strictly strongly positive on a compact subset controls its coefficient trace, using the finite BT mass there. No claim that the individual \`A_i\` are closed is required. Coordinate changes preserve the decomposition into absolutely continuous and singular coefficient measures and the algebraic wedge.

### Proof, arbitrary singular potentials

Locally choose psh potentials \`u_i<=0\` with \`T_i=dd^c u_i\`, and set
\[
u_{i,k}=\max(u_i,-k),\quad
O_k=\bigcap_{i=1}^p\{u_i>-k\},\quad
S_k=\mathbf1_{O_k}\bigwedge_{i=1}^p dd^c u_{i,k}.
\]
Each \`u_{i,k}\` is locally bounded. The bounded-case order, multiplied by the indicator \`1_{O_k}\` via Lemma 13.2.1, yields
\[
\mathbf1_{O_k}\bigwedge_i (dd^c u_{i,k})_{\rm ac}\ \le\ S_k.
\]
**Plurifine locality** on the common strict superlevel set identifies the coefficient measures of \`dd^c u_{i,k}\` and \`T_i\` there, hence also their absolutely continuous density matrices. Consequently the left-hand side is exactly
\[
\mathbf1_{O_k}(A_1\wedge\cdots\wedge A_p).
\]
The sets \`O_k\` increase and exhaust the complement of the union of the pole sets \`\{u_i=-\infty\}\`, which is Lebesgue-null. The algebraic wedge is a nonnegative, possibly initially nonintegrable measurable tensor. Monotone convergence for each pairing with a strongly positive test form, together with the locally finite increasing current limit \`S_k\uparrow S\` from Lemma 13.2.2, proves that it is locally integrable and bounded by \`S\`. There is **no** interchange of unproved nonmonotone limits and **no** use of sequential compactness to obtain a net assertion.

### Sharp strictness model in every degree

On \`U=\{z\in\mathbb C^n:|z_i|<2\}\` set, for \`1<=i<=p\`,
\[
u_i(z)=\max\{0,\log|z_i|^2\},\qquad T_i=dd^c u_i .
\]
Each potential is locally bounded psh. The normalized Poincaré–Lelong/Stokes computation with \`dd^c=i\partial\bar\partial/(2\pi)\` gives
\[
dd^c\max\{0,\log|z|^2\}=\sigma_{S^1},
\]
the normalized angular measure on the unit circle in the corresponding complex coordinate. The Hessian coefficient measures of each \`T_i\` are supported on the real hypersurface \`\{|z_i|=1\}\`, so **all** \`A_i=0\` almost everywhere. But by the separate-variable Bedford–Taylor product,
\[
\langle T_1\wedge\cdots\wedge T_p\rangle
=T_1\wedge\cdots\wedge T_p
=\sigma_{S^1}^{\boxtimes p}
\]
in the first \`p\` variables (as a \`(p,p)\`-current, with unconstrained remaining variables). It is nonzero. When \`p=n\`, its total mass on \`U\` is **1**. Thus the lower bound is sharp, but equality does **not** hold in general, even for bounded continuous potentials and locally finite mixed NPP. This is an all-degree independent-variable test, not a repeat of the older *compact full-mass Cantor torus / total-variation convergence* finding \`POME-FULLMASS-SINGULAR-AC-001\`.

## Verdict, dependencies and proposed addition

**No false printed statement found.** Lemma 13.31.1 remains valid, and the mixed lower-degree statement is a **verified conditional deduction** with a complete displayed argument conditional on the integrated local differentiation theorem, bounded Bedford–Taylor decreasing continuity, and plurifine restriction/truncation machinery. This run does not certify those upstream results transitively. The standing assumption that the **mixed** NPP is locally finite is essential to treat its limit as an ordinary current; absent that, the right side may have infinite compact trace mass.

Propose an **optional corollary after Lemma 13.31.1** stating the positive-current comparison for \`p<=n\`, with a note on the circle-current strictness example. Do not modify the original source theorem, history/attribution, permanent tags, proof registry or canonicalization. Dependent areas that may use this corollary include mixed non-pluripolar product estimates (§§13.2, 13.13) and volume pairings (§13.32), **without** claiming to repair or certify those sections. All Demailly approximation/regularization and dedicated Bergman, L², Ohsawa–Takegoshi, multiscale and positivity-loss proof completion remains **deferred-by-user**, untouched.
