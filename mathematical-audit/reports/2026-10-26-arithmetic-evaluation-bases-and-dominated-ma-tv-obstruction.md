# 2026-10-26 — weighted arithmetic evaluation bases and a sharp limitation of dominated Monge–Ampère convergence

**Reviewed `main`:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. **Audit branch at start:** `4a799ff13c278b916617194425d86996aa9cf47c`. **Checkpoint (UTC):** 2026-10-26T10:57Z.

**Scope.** First selected statement/proof-level review of current reading-edition §§9.55 and 15.37 (not complete section verification). In §9.55 only the growth/zero-counting and elementary interpolation arguments through Example 9.55.11 were examined; its subsequent weighted point extension, `L²`, and `\bar\partial` programme (§9.55.12 onward) was **not** examined. In §15.37 the standing assumptions and selected rooftop/extraction/capacity convergence passages were read. Demailly approximation/regularization and its *dedicated* Bergman, `L²`, Ohsawa–Takegoshi, multiscale-atlas, and positivity-loss proof-completion programme remain **deferred-by-user**, neither repaired nor certified by this report.

## POME-ARITH-EVAL-BASIS-ORDERS-001

**Status:** verified conditional deduction; **severity:** low; **printed theorem:** correct (not a proposed error). **Suggested action:** optional corollary after §9.55.8; retain existing numerical lower bound and attribution.

**Exact integrated evidence.** `docs/sections/entire-function-growth-and-algebraic-zero-sets--entire-function-growth-and-arithmetic-zero-sets/index.html`, main blob `465572b3785941e02714482e9d69735fcbcdcc73`. Theorem 9.55.1, source label `demailly-complex-geometry-F0566573`, permanent tag `2112DD801FC5`, lines 11–21 and proof lines 26–79; in particular the proper-polynomial weighted zero-fiber lower bound (9.55.3), tag `61D05B507A13`, lines 16–21. Corollary 9.55.8, source `demailly-complex-geometry-CE420F64`, tag `16B6E15BB4A5`, statement lines 85–93 and interpolation proof lines 99–109. Example 9.55.11, source `demailly-complex-geometry-9C417C3E`, tag `DDE636CB719F`, lines 114–116. The comparison only uses these statements, not subsequent analytic existence arguments.

**Strengthening.** Let `S\subset\mathbb C^n` be a finite nonempty set and let
```math
\delta=\min\{\deg P:0\ne P\in\mathbb C[z_1,\ldots,z_n],\ P|_S=0\},\qquad
h=\binom{\delta+n-1}{n}.
```
Let `\mathcal B(S)` denote the **finite nonempty** family of size-`h` subsets `B\subset S` for which the evaluation map
```math
\operatorname{ev}_B:\mathbb C[z]_{<\delta}\longrightarrow\mathbb C^B
```
is an isomorphism. For a nonzero entire function `f`, put
```math
\mathfrak m_S(f)=\max_{B\in\mathcal B(S)}
\sum_{w\in B}\operatorname{ord}_w f .
```
Then a constant `C_S\ge2`, depending only on `S` and **not** on `f,r,R`, satisfies, for `R\ge r\ge1`,
```math
\boxed{\log M_f(r)\le\log M_f(R)
-\delta^{1-n}\mathfrak m_S(f)\log\frac{R}{C_Sr}.}
```
For every nonzero polynomial `f` of degree `D`, passing to `R\to\infty` at fixed `r` gives the weighted zero estimate
```math
\boxed{D\ge\delta^{1-n}\mathfrak m_S(f).}
```
In particular, because every basis has `h` points, this strictly refines the use of the **minimum** vanishing order in Corollary 9.55.8 whenever the orders are uneven.

**Complete deduction from the printed growth theorem.** By the minimality of `\delta`, the evaluation map from the `h`-dimensional vector space `\mathbb C[z]_{<\delta}` to `\mathbb C^S` is injective. Elementary row selection supplies at least one `h`-point evaluation basis, so `\mathcal B(S)` is nonempty. For each such `B` and every multiindex `|\alpha|=\delta`, choose the unique polynomial `R_{\alpha,B}` of degree less than `\delta` whose values on `B` equal those of `z^\alpha`. Put `P_{\alpha,B}=z^\alpha-R_{\alpha,B}`, listing all degree-`\delta` monomials. The highest homogeneous components `z^\alpha` have common zero exactly the origin, and `P_{\alpha,B}(w)=0` for **every** `w\in B`. Consequently Theorem 9.55.1 and its *integer* local multiplicity bound (9.55.3) imply for each fixed `B`, with a constant `C_B` independent of `f`,
```math
\log M_f(r)\le\log M_f(R)-
\delta^{1-n}\left(\sum_{w\in B}\operatorname{ord}_w f\right)
\log\frac{R}{C_Br}
\quad(R>C_Br).
```
There are only finitely many bases. Set `C_S=\max_{B\in\mathcal B(S)}C_B`. If `R>C_Sr`, all logarithms are positive, and replacing `C_B` by `C_S` weakens each inequality; maximize the sums over `B`. If `R\le C_Sr`, the new logarithmic subtraction is nonpositive, so monotonicity of `M_f` proves the same conclusion. If `f` is polynomial of degree `D`, `\log M_f(R)=D\log R+O(1)` as `R\to\infty`, giving the degree inequality. This also covers `\operatorname{ord}_w f=0`, constant `f`, and `n=1`; no new analytic lemma is needed.

**A strict and sharp two-dimensional example.** Take
```math
S=\{(0,0),(1,0),(0,1)\}\subset\mathbb C^2,\quad
\delta=2,\quad h=3,\quad f(x,y)=xy.
```
The evaluations of `1,x,y` form an invertible `3\times3` matrix, so the unique basis is all of `S`. The orders are `2,1,1`, respectively; hence `\mathfrak m_S(f)=4`. An explicit interpolating map is
```math
P=(x^2-x,xy,y^2-y),
\quad P^{-1}(0)=S,
\quad Q=(x^2,xy,y^2).
```
The new coefficient is `\delta^{1-n}\mathfrak m_S(f)=2`, versus the printed coarse bound `(\delta+1)\min_{S}\operatorname{ord}f/2=3/2`. It is **sharp**: `M_f(R)=R^2/2`, so no lower-growth coefficient exceeding 2 can hold for this `f` as `R\to\infty`. The example's root equations, evaluation determinant 1 and arithmetic coefficient 2 were separately checked in a scratch SymPy calculation; this is not a formal proof or build.

**Dependency and limitation.** The result is conditional on Theorem 9.55.1's weighted Jensen/proper-map theorem and integer lower bound, including its underlying weighted pole-mass theory (§§6.34, 6.35, 6.44, 6.46). Those are **not** all independently certified here. The elementary interpolation construction and sharpness example have complete arguments above. Not every `h`-point subset is a basis; replacing `\mathcal B(S)` by arbitrary subsets would be unjustified. This result does not use, review, or repair any dedicated `L²` or Demailly regularization result.

## POME-MA-DOMINATED-WEAK-NOT-TV-001

**Status:** verified conditional deduction (sharpness counterexample to an **unasserted** strengthening); **severity:** low; **printed theorem:** correct. **Suggested action:** optional remark following §15.37.19 stating that its weak convergence cannot in general be upgraded to total-variation convergence, even under smooth uniform convergence with two-sided bounded densities.

**Exact integrated evidence.** `docs/sections/relative-equations-under-positive-lower-mass/index.html`, main blob `75535cb099b754589883aa9f9fa4867fabd89d86`. Standing positive-lower-mass and reference conditions lines 8–49; Lemma 15.37.13, source `non-kahler-pluripotential-theory-F56DEC9E`, tag `E5ED88B4042A`, lines 271–337 (particularly the finite rooftop contact bound (15.37.14), tag `EEB0F315C2A3`, lines 289–303); Proposition 15.37.17, source `non-kahler-pluripotential-theory-8424FFA4`, tag `D220D741C684`, lines 344–386; Theorem 15.37.19, source `non-kahler-pluripotential-theory-4EA71F8C`, tag `6FBF04A6D4DE`, statement and proof lines 394–419. The original conclusion is **capacity convergence of potentials and weak convergence of measures**.

**Explicit example in every complex dimension `n\ge1`.** Let
```math
X=(\mathbb C/(\mathbb Z+i\mathbb Z))^n,\quad
\omega=\frac{i}{2\pi}\sum_{k=1}^n dz_k\wedge d\bar z_k,\quad
\theta=\omega,\quad\varphi=0.
```
Here `\varphi` is a model reference and `P_{\varepsilon\theta}(0)=0`; the Kähler class has `v_-(\theta)=\int_X\omega^n>0` by the bounded Bedford–Taylor/Stokes mass identity. Fix `0<a<1`, write `x_1=\operatorname{Re}z_1\pmod{\mathbb Z}`, and set
```math
u_j(z)=\frac{a}{\pi^2 j^2}\cos(2\pi jx_1).
```
These are globally defined smooth `\theta`-psh functions, uniformly converging to zero **even in `C^1`**. Indeed
```math
\partial_{z_1}\partial_{\bar z_1}u_j
=-a\cos(2\pi jx_1),\qquad
\theta+dd^c u_j=
\frac{i}{2\pi}\left[
(1-a\cos(2\pi jx_1))dz_1\wedge d\bar z_1+
\sum_{k=2}^n dz_k\wedge d\bar z_k\right]>0.
```
Because only one diagonal factor varies,
```math
\mu_{u_j}=(\theta+dd^c u_j)^n
=(1-a\cos(2\pi jx_1))\,\omega^n,
\quad
\mu_0=\omega^n.
```
Thus **all** `\mu_{u_j}` are bounded by the one fixed finite non-pluripolar measure `\nu=(1+a)\omega^n`; their densities are also bounded **below** by `1-a>0`. The original Theorem 15.37.19 indeed yields weak convergence, also directly seen by Fourier cancellation. Yet
```math
\boxed{\|\mu_{u_j}-\mu_0\|_{\mathrm{TV}}
= a\int_X|\cos(2\pi jx_1)|\,\omega^n
=\frac{2a}{\pi}\int_X\omega^n>0\quad\forall j.}
```
Here `\|\cdot\|_{\mathrm{TV}}` denotes the variation **norm** of a signed measure, not half the distance between probability measures. This does not contradict the theorem, since the theorem asserts only weak convergence. Nor does it contradict other sections asserting total-variation stability under *different, stronger* density-shape hypotheses. In particular, it is not a replay of the earlier toric softmax-versus-narrow example: here a **single common smooth dominating measure**, positive lower/upper density bounds, Kähler background, and even `C^1` convergence of the potentials are built into the counterexample.

**Dependency and limitation.** The algebraic Hessian, measure, and variation calculations above are unconditional for the smooth example. Placing it precisely under Theorem 15.37.19 uses only the elementary Kähler bounded-mass and model-reference facts; the theorem's extensive rooftop, tail, and capacity proof chain is **not** fully certified by this example. In particular, no new claim of falsehood or proof gap is being made for Lemma 15.37.13, Proposition 15.37.17, or Theorem 15.37.19.

## Scope ledger and verification

- **Actual new selected proof inspection:** §§9.55.1/.8/.11 (growth setup, homogeneous-leading-form comparison, interpolation, and arithmetic extremal example), and §§15.37.13/.17/.19 with its standing assumptions and the finite-rooftop contact partition. Exact main paths, source labels, permanent tags, line anchors and blobs are above. §9.55.12 onward (weighted point extension, `L²` methods) **excluded**. The full analytic proof of weighted Jensen, unbounded rooftop estimates, the zero-domination lemma and all transitive prerequisites are **unverified dependencies**, not certified.
- **Statuses:** both new IDs are **low / verified conditional deduction**; no new confirmed false theorem, no inferred proof gap, no repairs marked integrated and no old ledger status changed. The basis result suggests an optional corollary; the oscillatory example suggests a warning on a stronger conclusion that was **never printed**.
- **Checks actually run:** one short scratch SymPy computation for the explicit three-point zero fiber, determinant and the elementary `2/\pi` absolute-cosine integral. No project tests, full build, CI, browser rendering, formalization, source/body/registry/tag modifications or website publication.
- **Coverage accounting:** 2 first selected proof-level sections from the current 747-row chapter/section inventory. No entire section/chapter, transitive dependency chain, or excluded programme has been mathematically certified. All prior resolved/unresolved/deferred records are retained, including every **deferred-by-user** approximation item. Only audit documentation should be updated on `review/mathematical-audit`.
