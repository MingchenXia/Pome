# 2026-10-29 — finite equations for affine analytic sets and quantitative limits of exponential densities

**Reviewed production main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. **Scope:** independent mathematical deductions from the actual integrated reading edition; no source/editorial or registry edit. Both findings are **low severity / verified conditional deduction**, not false printed theorems, not certified full proofs of their upstream results. No previously open issue is closed.

## POME-FINITE-PROJECTION-BOUNDED-EQUATIONS-001

**Status:** verified conditional deduction. **Severity:** low. **Statement:** an effective strengthening of the algebraicity implication in Theorem 9.61.4; no error in that theorem.

**Exact integrated source:** `docs/sections/affine-algebraicity-and-linear-growth/index.html`, main blob `8f2301f7696a0b230950918ae20a7f9e57be768b`. Lemma 9.61.2: source `demailly-complex-geometry:F8362024`, permanent tag `D8FA405BDFAC`, lines 10–26; its cone bound (9.61.3): tag `D6D620F9E57D`, lines 12–15. Theorem 9.61.4: source `demailly-complex-geometry:A33B88FE`, tag `D15F5F84A74A`, lines 31–60, especially proof lines 44–58 (fiber polynomial, polynomial coefficient degree and special fibers).

**Precise hypotheses.** Let `A` be a nonempty pure `p`-dimensional closed analytic subset of `C^p × C^q`, `q=n-p≥1`, with `|z''|≤C(1+|z'|)`. Its coordinate projection is proper and finite by Lemma 9.61.2. Let `d` be the generic covering degree if `p>0`; for `p=0`, put `d=#A`. Fix **any** `N=d(q-1)+1` pairwise distinct complex numbers `t_1,...,t_N`. Write

$$
\ell_t(w_1,\ldots,w_q)=\sum_{k=0}^{q-1}t^k w_{k+1}.
$$

Outside the exceptional base set, define the monic fiber polynomial

$$
P_t(z',T)=\prod_{a\in\pi^{-1}(z')}(T-\ell_t(a'')).
$$

The symmetric coefficients extend to polynomials of total degree at most their coefficient index, exactly as established at integrated lines 44–56. Consequently

$$
F_t(z',z'')=P_t(z',\ell_t(z''))
$$

is a polynomial of **total degree at most** `d`, and the finitely many fixed directions cut out the exact reduced analytic set:

$$
\boxed{ A=\bigcap_{j=1}^{d(q-1)+1}V(F_{t_j}). }
$$

This is a **set-theoretic** presentation, not an ideal-generation, scheme-theoretic, complete-intersection, or optimal-minimal-generator assertion. The case `q=0` is `A=C^n` and needs no equations.

**Proof of uniform finite separation.** Inclusion `A⊂∩V(F_t)` follows from the original fiber-polynomial identity and density of the unramified base locus. A special fiber has at most `d` **distinct** points: choose pairwise disjoint neighborhoods of its points; the open mapping property of the finite proper map ensures that a nearby base point outside the exceptional set meets all these neighborhoods, so their number does not exceed the number `d` of generic sheets. Let `b=(b',b'')∉A`; for every distinct `a∈π^{-1}(b')`, the difference `b''-a''` is nonzero, and

$$
g_a(t)=\ell_t(b''-a'')
$$

is a nonzero polynomial in `t` of degree at most `q-1`. The union of the roots of at most `d` such polynomials has cardinality at most `d(q-1)`. Among the prescribed `N` directions some `t_j` avoids them all. Every root of `P_{t_j}(b',T)` is the value of `ℓ_{t_j}` on the **actual special fiber**, with multiplicities, as proved in integrated lines 56–58 by properness and convergence of the generic fibers. Therefore `F_{t_j}(b)≠0`. This proves the boxed equality. If `p=0`, the same argument uses the unique finite fiber without an exceptional set.

**Sharpness of the direction count for this fixed moment-curve method.** For `q≥2`, let `t_1,...,t_{d(q-1)}` be any distinct numbers and `b=0∈C^q`. Partition them into `d` blocks of `q-1` numbers. For block `i`, let `a_i` be the coefficient vector (constant through leading coefficient) of the monic polynomial `∏_{t_j \text{ in block }i}(T-t_j)`. The vectors `a_i` are distinct and nonzero; put `A=\{a_1,\ldots,a_d\}`. For **every** prescribed `t_j`, one `a_i` satisfies `ℓ_{t_j}(a_i)=0=ℓ_{t_j}(b)`, so all `d(q-1)` fiber polynomials vanish at `b∉A`. Thus the uniform `d(q-1)+1` guarantee cannot be improved for this moment-curve selection. For `q=1`, one polynomial suffices and degree `d` is sharp for `d` distinct points in `C`.

**Proposed non-production correction/enhancement:** optionally insert the finite-direction construction after Theorem 9.61.4 as a corollary, retaining the original proof and its Remmert/finite-map, analytic-removability, and dimension dependencies. **Affected downstream readers:** finite-type affine analytic models in §§9.58–9.61 and effective set-theoretic equations. The underlying proper finite projection and analytic coefficient-extension inputs are **conditional**, not independently certified in this increment.

## POME-EXPONENTIAL-LP-TAIL-RATE-001

**Status:** verified conditional deduction. **Severity:** low. **Statement:** quantitative refinement and optimal absence of a universal power rate under the bare envelope domination used in Proposition 15.17.3. No false printed theorem or PDE counterexample.

**Exact integrated source:** `docs/sections/equations-with-prescribed-singularities--local-holder-continuity-in-a-big-background/index.html`, main blob `dac69f16acb822663bd2262d36976cf17bdcc9ad`; Proposition 15.17.3, source `non-kahler-pluripotential-theory:779CEE41`, permanent tag `D11439C1393F`, lines 81–113, particularly lines 99–105. Corollary 15.17.4, source `B67C1123`, tag `64893D9DABFE`, lines 118–128, checked only for the limit/symmetry logic. The **assumed** uniform envelope interval is printed in `docs/sections/equations-with-prescribed-singularities--minimal-singularities-in-an-arbitrary-big-background/index.html`, blob `4805502723e87defe8ae12616a3d2d550fb8dd75`, Lemma 15.16.5, source `190E6ECF`, tag `DA20F7BB0188`, lines 145–163. The proof of Theorem 15.17.1 citing excluded regularization is **not** examined.

Assume the exact bounds from Lemma 15.16.5:
`V_θ-B≤v_λ≤V_θ≤0`, `m≤c_λ≤C`, and `0≤f∈L^p(dV)`, `p>1`. Put `h=B-V_θ≥0`, allowing `h=+∞` on its pluripolar locus. Pointwise almost everywhere,

$$
0\le 1-e^{\lambda v_\lambda}
\le \min\{1,\lambda h\}.
$$

Thus for **every** `L>0`,

$$
\boxed{\|(1-e^{\lambda v_\lambda})f\|_p
\le \lambda L\|f\|_p+\|f\,1_{\{h>L\}}\|_p.}
$$

The second term tends to zero as `L→∞` because `f∈L^p` and `h` is finite off a set of smooth volume zero; choosing `L=L(\lambda)→∞` with `\lambda L(\lambda)→0` recovers the published strong `L^p` convergence **without assuming a rate**. Under the **additional, explicitly stated hypothesis** `hf∈L^p(dV)`, one obtains the quantitative estimate

$$
\boxed{\|(1-e^{\lambda v_\lambda})f\|_p\le
\lambda\|hf\|_p,}
$$

and, using the printed bound `c_λ≤C`,

$$
\|c_\lambda e^{\lambda v_\lambda}f-cf\|_p
\le |c_\lambda-c|\|f\|_p+C\lambda\|hf\|_p.
$$

No rate for `|c_λ-c|` follows from these inequalities.

**No universal positive power rate from domination plus `f∈L^p` alone.** This is an **abstract local test**, explicitly **not** a family of solutions of the global PDE. On the unit disc set `V(z)=\log|z|≤0`, `v_\lambda=V`, `B=0`. Fix `0<a<p` and let the nonnegative radial density `f` satisfy

$$
|f(re^{i\theta})|^p=
\frac{a}{2\pi}r^{-2}(\log(1/r))^{-1-a}
\mathbf1_{\{0<r<e^{-1}\}}.
$$

Direct polar integration gives `\|f\|_p=1`. With `t=-\log r`,

$$
\|(1-e^{\lambda V})f\|_p^p
=a\int_1^\infty(1-e^{-\lambda t})^p t^{-1-a}\,dt
=a\lambda^a\int_\lambda^\infty
(1-e^{-s})^p s^{-1-a}\,ds.
$$

Since `0<a<p`, the last integral converges to a strictly positive finite number as `\lambda↓0`: near zero the integrand behaves like `s^{p-1-a}`, at infinity like `s^{-1-a}`. Hence the norm is asymptotic to a positive multiple of `\lambda^{a/p}`. Taking `a>0` arbitrarily small rules out a **universal** exponent `\beta>0` under just the interval and `L^p` assumptions. This **does not** disprove a better rate under the actual Monge–Ampère equation and its additional structure.

**Proposed non-production addition:** a short tail estimate remark after Proposition 15.17.3, explicitly separating dominated convergence, conditional `O(\lambda)` with a weighted moment, and the inability to infer a rate for `c_\lambda-c`. **Affected downstream readers:** λ→0 density convergence and local Hölder compactness in §15.17; the exponential-solution selection discussion. All global PDE existence, convergence and regularization-related inputs remain **conditional/deferred**, not recertified.

## Exact coverage and boundaries

Direct proof-level mathematical review this increment: §9.61.4 fiber-polynomial argument and new finite-direction construction (increment to previously selected §9.61); §15.17.3 density limit and §15.17.4 symmetry/compactness passages (first **selected nonexcluded** coverage in previously inventory-only §15.17). Context only: §9.61.2, §15.16.5 bounds, §15.17.1 **statement**. No attempt to verify any Demailly regularization/approximation or the dedicated Bergman, weighted L², Ohsawa–Takegoshi, multiscale-atlas, positivity-loss proof programme, including no disguised transitively dependent audit. Preserve excluded ledger records as **deferred-by-user**, never resolved. **25 chapters, 747 numbered ToC sections, zero entire sections certified.** No build, tests, CI, source, registry, permanent-tag, generated-site, or main changes.