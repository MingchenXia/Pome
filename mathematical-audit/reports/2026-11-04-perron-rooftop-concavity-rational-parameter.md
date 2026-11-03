# Audit report — 2026-11-04 — concavity and rational reduction of the Perron rooftop parameter

**Finding ID:** \`POME-GEOD-ROOFTOP-RATIONAL-LEGENDRE-001\`  
**Classification:** low / **verified conditional deduction** (the printed statements are not false; this is not a full verification of the geodesic-existence proof).  
**Reviewed production main:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`.  
**Target reading-edition file:** \`docs/sections/relative-energy-and-perron-segments--subgeodesics-and-perron-segments/index.html\`; reviewed main blob \`662f60d73fc585b6ea3b710f2a3472bac1de8a7c\`.

## Exact source anchors and hypotheses

- Theorem **17.7.8**, original source label \`foundations-of-pluripotential-theory:108758A0\`, permanent tag \`2FECBE87C487\`, physical lines **186–209**: existence of weak Perron geodesics between full-relative-mass potentials.
- Proposition **17.7.9**, source \`foundations-of-pluripotential-theory:470B93BF\`, permanent tag \`DD04D189A4D3\`, lines **214–251**: endpoint order, translation covariance and monotonicity. These are checked for compatibility, not reproved here.
- Proposition **17.7.10**, source \`foundations-of-pluripotential-theory:40348539\`, permanent tag \`6DDFC01E2315\`, physical lines **256–271**: Legendre–rooftop expression for the geodesic.
- The rooftop \`P_\theta\` is that of Definition 16.11.5. The relative-full-mass guarantee that the rooftops below are not identically minus infinity is stated in Proposition 17.4.7 and invoked explicitly by Proposition 17.7.10, line **266**. This audit does not recertify these upstream theorems.

Assume the printed standing setting: a compact complex manifold \`X\`, a smooth closed real \`(1,1)\`-form \`θ\` with big class, a model potential \`φ\` of positive mass, and \`u_0,u_1 ∈ E(X,θ,φ)\`. For each real \`s\`, put

\[
q_s=P_\theta(u_0,u_1-s).
\]

The rooftop is \`θ\`-psh, nontrivial, and obeys \`q_s≤u_0\` and \`q_s≤u_1-s\`.

## Direct proof of the new parameter conclusions

**1. Sharp order and one-Lipschitz bound.** For \`h≥0\`, the second obstacle decreases as \`s\` increases, hence \`q_{s+h}≤q_s\`. Also \`q_s-h\` is \`θ\`-psh and satisfies both obstacles for \`q_{s+h}\`:

\[
q_s-h\leq u_0-h\leq u_0,\qquad
q_s-h\leq u_1-s-h=u_1-(s+h).
\]

By the definition of the rooftop as the maximal \`θ\`-psh minorant, \`q_s-h≤q_{s+h}\`. Therefore the **pointwise** extended-valued inequalities are

\[
\boxed{q_s-h\ \leq\ q_{s+h}\ \leq\ q_s\qquad(s\in\mathbb R,\ h\geq0).}
\]

This directly proves monotonicity and the optimal one-Lipschitz bound in \`s\`, with no compactness or limit theorem. A point at which \`q_s=-∞\` for one parameter is a common polar point for **all** parameters. At all other points the values are finite for every \`s\`, and \`s\mapsto q_s(x)\` is one-Lipschitz.

**2. Pointwise concavity.** For \`s_0,s_1∈R\` and \`0≤λ≤1\`, the function

\[
w=(1-\lambda)q_{s_0}+\lambda q_{s_1}
\]

is \`θ\`-psh, because a convex combination of \`θ\`-psh functions remains \`θ\`-psh. Moreover

\[
w\leq u_0,\qquad
w\leq (1-\lambda)(u_1-s_0)+\lambda(u_1-s_1)
=u_1-\big((1-\lambda)s_0+\lambda s_1\big).
\]

It is therefore an admissible competitor for \`q_{(1-\lambda)s_0+\lambda s_1}\`, yielding

\[
\boxed{q_{(1-\lambda)s_0+\lambda s_1}
\geq (1-\lambda)q_{s_0}+\lambda q_{s_1}.}
\]

In particular, on the common finite locus, the rooftop profile is concave, continuous, nonincreasing and has all secant slopes in \`[-1,0]\`. The statement is not that \`q_s\` is *convex* in \`s\`; its direction follows from taking a **supremum of admissible psh minorants**.

**3. The full real Legendre parameter is reducible to rational parameters, exactly.** Fix \`x∈X\` and \`0<t<1\`. On the common finite locus, the preceding one-Lipschitz estimate shows that

\[
s\longmapsto q_s(x)+ts
\]

is continuous on \`R\`. By density of \`Q\`, \`sup_{s∈R}(q_s(x)+ts)=sup_{s∈Q}(q_s(x)+ts)\`. On the common polar locus both suprema are \`-∞\`, hence equality also holds there. Proposition 17.7.10 therefore has the **equivalent countable representation**

\[
\boxed{
G_t(u_0,u_1)
=\left(\sup_{s\in\mathbb Q}\{P_\theta(u_0,u_1-s)+ts\}\right)^*
\quad(0<t<1).
}
\]

The equality *before* regularization holds pointwise for every \`x\`. Consequently the same upper-semicontinuous regularization is obtained on \`X\` or, as in the printed proposition, jointly on \`X\times S\`. This is a special countable reduction for the ordered scalar parameter; it does **not** assert that every psh family or net is sequential, nor justify any exchange with Monge–Ampère limits.

**4. Both slope bounds and the possible corner are attained.** Take \`u_0=u_1=φ\` (the model potential itself is in the standing full-mass class). Then the two obstacles differ by a constant and the rooftop is exactly

\[
q_s=\phi+\min\{0,-s\}.
\]

Indeed the right-hand side is \`θ\`-psh and is the pointwise minimum of the two obstacles, so it is the rooftop. Its scalar profile has slope \`0\` for \`s<0\`, slope \`-1\` for \`s>0\`, and a genuine corner at \`s=0\`. Thus the global bounds are optimal and differentiability cannot be inferred from the printed hypotheses. The Legendre supremum gives \`G_t(φ,φ)=φ\`, consistently with Proposition 17.7.9(6).

## Adjudication, dependencies, and suggested insertion

The integrated Proposition 17.7.10 is **correct as stated**. The new results are exact parameter inequalities and an exact countable reduction of its displayed formula, not a correction of a false theorem, not a proof-gap resolution, and not a new full-geodesic theorem. The deduction uses only convexity of the \`θ\`-psh cone, the rooftop order characterization, and the existing existence and Legendre formula as internal conditional inputs. The proof does **not** use Demailly approximation/regularization or any dedicated Bergman, weighted \`L^2\`, Ohsawa–Takegoshi, multiscale-atlas or positivity-loss programme. Those previously indexed inputs remain **deferred-by-user** and have not been examined.

**Proposed editorial change only:** after Proposition 17.7.10, optionally add a short lemma stating \`q_s-h≤q_{s+h}≤q_s\`, pointwise parameter concavity, and the rational-parameter formula; retain the original source attribution, numbering, permanent tags and the unrestricted real-parameter formula. Relevant downstream users include the rooftop/Legendre discussion of §§17.7–17.8 and §17.17; this is a safe countable *formula*, not a new regularity or measure-convergence assertion.

**Actual new review coverage:** the parameter dependence and countable reduction of Proposition 17.7.10 (physical lines 256–271) and exact order/covariance hypotheses in Proposition 17.7.9 (lines 214–251), within **already partly reviewed §17.7**. Theorem 17.7.8 (lines 186–209), §16.11 rooftop construction and §17.4.7 are contextual dependencies only. No entire section, theorem dependency chain, project or formal proof is certified.

**Project boundary:** current main ToC **25 chapters, 747 numbered sections, zero fully mathematically certified sections**. Existing confirmed errors, proof gaps, external dependencies and all \`deferred-by-user\` items retain their earlier classifications. Audit Markdown only; no main, body, registry, canonicalization, permanent-tag, build, test, CI or website change.
