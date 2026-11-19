# 2026-11-20 — Analytic-set excision for non-pluripolar products and exact cohomological mass discrepancy

**Finding ID:** `POME-NPP-ANALYTIC-EXCISION-DIVISOR-MASS-001`  
**Classification:** low / **verified conditional deduction** (not a false printed statement, a proposed repair, or a new proof of upstream Bedford–Taylor theory).  
**Production main reviewed:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.

## Integrated reading-edition anchors

1. `docs/sections/non-pluripolar-products--fiber-integration-and-modifications/index.html`, blob `9954a43d90d5cae8ef744968636d7a5912348fce`. Complete mathematical content directly read at physical lines **7–57**. Corollary **13.6.1**, source `foundations-of-pluripotential-theory:BAE2819F`, permanent `BEC54934FC2C`, lines **10–33**; its fiber identity source/permanent `73910199/F6B4982710D8`, lines **16–19**. Proposition **13.6.3**, source `foundations-of-pluripotential-theory:3F4A3A88`, permanent `0811FFDF15B7`, lines **35–55**.
2. `docs/sections/non-pluripolar-products--closedness-and-cutoff-gradients/index.html`, blob `f781fa61bd20944c7c4798e0e0984cfb81ef069f`. Complete mathematical content directly read at physical lines **7–50**. Theorem **13.3.1**, source `foundations-of-pluripotential-theory:A226C692`, permanent `8A125B338F90`, lines **10–48**.
3. Selected **dependency statements only**, not complete direct section readings: bounded Bedford–Taylor slicing **13.4.6**, source `foundations-of-pluripotential-theory:917DDB45`, permanent `7F078C7DCBDD`, in `docs/sections/non-pluripolar-products--bounded-factors-and-the-first-degree-product/index.html`, blob `d234ab96e33bfd24ad1d53d29332b2c021cddeff`, lines **157–189**; global finiteness Theorem **13.5.4** and mass bound **13.5.5**, source/permanent `A00627D3/3783DE0B00` and `82C17B5F/896BDD434F7F` in `docs/sections/non-pluripolar-products--global-finiteness-and-bounded-cohomological-mass/index.html`, blob `943517743538820940559eae8469ce98ecf5fcd5`, lines **84–121**. Truncation/locality Lemma **13.2.2**, source/permanent `CE1D6DA5/D59675D9F6D8`, used as an existing conditional input; no new review credit assigned here.

## Direct proof audit of the printed sections

For **13.3.1**, the local normalization `u_j <= 0` follows after shrinking and subtracting constants. For `u=sum u_j`, the cutoff `w_k=max(1+u/k,0)` is bounded psh, vanishes off the *common* truncation region `O_k`, and increases to one outside the pole locus. The bounded-current integration-by-parts identity for `E_{Theta_k}(w_k)` gives a uniform cutoff-gradient bound from local finiteness, even though the untruncated `Theta_k` masses need not themselves be uniformly bounded off `O_k`. The support of `zeta'(w_k)` lies inside `O_k`; dominated convergence against the limiting locally finite positive product therefore kills the derivative term. The final constant strongly positive `gamma` testing spans the required coefficient directions. **No new printed error or standalone proof gap identified.**

For **13.6.1**, a fiber restriction cannot be identically minus infinity because of the pointwise lower bound `W_z >= phi-C`. The mixed total-space/fiber identity uses bounded Bedford–Taylor slicing before a *monotone* common pole cutoff; the off-tuple restriction when `j=0` or `j=r` is harmless because the extra potential has the same pole set by bounded difference. The bounded signed difference weight follows by subtracting `C` times the unweighted identity. For **13.6.3**, the biholomorphic locus comparison and the fact that both sides assign zero mass to the exceptional analytic loci justify both pushforward identities, including in degree `p=1`. No formula takes an illicit wedge product with an exceptional divisor. **Neither printed claim is refuted.**

## New deduction: analytic-set excision

**Proposition.** Let `X` be a complex manifold, `1 <= p <= dim_C X`, and `A subset X` a nowhere-dense closed analytic set. Suppose `T_1,...,T_p` and `S_1,...,S_p` are two tuples of positive closed `(1,1)`-currents, with their mixed non-pluripolar products defined as locally finite currents. If `T_j|_(X\A)=S_j|_(X\A)` for every `j`, then

\[
\boxed{\langle T_1\wedge\cdots\wedge T_p\rangle
=\langle S_1\wedge\cdots\wedge S_p\rangle.}
\]

**Proof.** Every point of `X\A` has a coordinate neighborhood on which the positive closed currents of each pair coincide. Their local psh potentials therefore differ by a pluriharmonic function. The bounded Bedford–Taylor products on each common sublevel region, and hence their monotone non-pluripolar limits, are unchanged by adding such pluriharmonic terms (equivalently, use the printed plurifine locality). Thus the two non-pluripolar products coincide on the open set `X\A`. A proper analytic set is locally contained in a holomorphic zero set; its logarithm is psh and equals minus infinity there. Consequently `A` is pluripolar. Neither non-pluripolar product charges `A`; this is true for all coefficient/trace measures and not just for their top-degree masses. Decomposing each coefficient measure over the disjoint Borel sets `X\A` and `A` gives equality on all of `X`. The local-finiteness hypothesis allows these positive coefficient measures and the resulting equality of currents to be used without a hidden infinite-mass subtraction. QED.

**Divisor corollary.** If `D_j` are arbitrary effective real divisors and `R_j` are positive closed `(1,1)`-currents, then

\[
\boxed{\langle(R_1+[D_1])\wedge\cdots\wedge(R_p+[D_p])\rangle
=\langle R_1\wedge\cdots\wedge R_p\rangle}
\]

whenever the products are locally finite. Indeed the summands `[D_j]` restrict to zero off `A=union_j |D_j|`. No exceptional-divisor assumption, cohomological equality, or expansion of the singular wedge is required.

**Modification corollary.** For a modification `pi:Y->X` between compact Kähler manifolds, effective divisors `D_j` on `Y`, and positive closed `R_j` upstairs, Proposition 13.6.3 and analytic-set excision give

\[
\pi_*\langle (R_1+[D_1])\wedge\cdots\wedge (R_p+[D_p])\rangle
=\langle\pi_*R_1\wedge\cdots\wedge\pi_*R_p\rangle.
\]

This includes exceptional and nonexceptional divisors alike; the conclusion concerns **non-pluripolar** products, not ordinary tensor/wedge products nor equality of currents `R_j+[D_j]` and `R_j`.

## Exact projective mass discrepancy (sharp unbounded separation)

Let `X=P^n`, normalize the Fubini–Study form by `int_X omega^n=1`, and let `H` be a hyperplane. Poincaré–Lelong gives `[H]` the cohomology class `[omega]` for the project's convention `dd^c=i/(2pi) partial barpartial`. For every `c_j>=0` put `T_j=omega+c_j[H]`. The divisor corollary yields

\[
\langle T_1\wedge\cdots\wedge T_p\rangle=\omega^p
\quad(1\le p\le n),
\]

while the cup-product class is `prod_j(1+c_j)[omega]^p`. In particular

\[
\int_X\langle T_c^n\rangle=1,
\qquad
\int_X[T_c]^n=(1+c)^n.
\]

For `c>0`, these differ, and their ratio is unbounded as `c->infinity`. This is **not a failure** of the printed cohomological upper mass bound: it illustrates why a positive current's non-pluripolar mass must not be silently replaced by the intersection number of its possibly divisorial cohomology class.

## Status and downstream obligations

- **Status:** low / **verified conditional deduction**. The printed Theorem 13.3.1, Corollary 13.6.1 and Proposition 13.6.3 remain valid at the directly inspected steps. No body patch is needed; if incorporated elsewhere, state explicitly that the equality concerns non-pluripolar products, not ordinary current multiplication.
- **Dependencies not independently certified in this run:** the full bounded Bedford–Taylor construction and slicing (especially §13.4), the complete §13.2 plurifine-locality chain, the global mass estimate §13.5, the coordinate invariance of current products, and the full positive-current theory. Their use here is conditional and transparent. Hironaka is not invoked.
- **Potential dependents for review:** §13.5 cohomological mass comparisons, §13.6 modifications, §13.8 projective fiber mass, §13.13 non-pluripolar product properties, and §20 b-divisor/restriction arguments. No downstream theorem or full transitive proof chain is certified here.
- **Coverage:** +2 **complete current direct section readings** (§13.3, §13.6), +2 selected prerequisite statement reviews (§13.4, §13.5), +0 entire upstream-chain certificates. Historical first visits are *not* asserted; some §13.6 results were already inspected on earlier dates, but this new excision/cohomology calculation is distinct from the previous étale-correlation and fiber-energy computations.
- **Exclusion:** Demailly approximation/regularization and all dedicated Bergman, L², Ohsawa–Takegoshi, multiscale-atlas, and positivity-loss proof-completion work remain **deferred-by-user**, neither resolved nor certified. Nothing in this review reopens that programme.
- **Operational boundary:** audit Markdown only, no main/source/registry/permanent-tag/site changes; no builds, software tests, CI or publication. The displayed projective identity was checked algebraically, not advertised as a software test.
