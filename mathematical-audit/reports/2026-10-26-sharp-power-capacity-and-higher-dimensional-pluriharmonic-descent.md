# 2026-10-26 — sharp power-capacity exponent and higher-dimensional pluriharmonic descent

**Revision actually inspected:** Pome `main` `b6933b772f41b45918f7e25ed1afbbb1fd892272`. **Scope:** selected current integrated proof passages in §§15.33, 14.19, 11.22, 5.48 and the Bedford–Taylor capacity/comparison inputs §§7.3–7.4. None of these full sections, or their transitive dependencies, is certified. The author's Demailly approximation/regularization and its dedicated Bergman, L², Ohsawa–Takegoshi, multiscale-atlas and positivity-loss programme is **deferred-by-user**, not reopened or certified. No testing, build, CI, deployment, or mathematical-body/canonical-tag changes.

## Finding POME-POWER-CAPACITY-EXPONENT-SHARP-001

**Severity:** low. **Status:** verified conditional deduction, **not** a false printed theorem.

**Original integrated anchors (all on the pinned main):**

- Theorem 15.33.1, tag `35816840F731`, and inequality 15.33.2, tag `7DAF690D3482`; `docs/sections/equations-with-prescribed-singularities--power-capacity-bounds-and-threshold-equations/index.html`, blob `a36500eaaa461a2f9582d144a9700466460aabdf`, lines 11–26 and proof lines 32–82.
- Theorem 15.33.6, tag `B37DD22EFF75`, same file, lines 95–187; radial top-product equation 15.33.8 (tag `F1C776CF9796`) at lines 119–131, and ball-mass/outside-density estimate 15.33.9 (tag `F69DF10A862E`) at lines 134–156.
- Definition 7.4.2, tag `E9E7C75396D2`; `docs/sections/bedford-taylor-products-and-local-capacity--weighted-estimates-and-monge-ampere-capacity/index.html`, blob `801a6ce8d25a6db19202cbc295937a135a9a208e`, lines 86–94.
- Theorem 7.3.11 (local bounded Bedford–Taylor comparison), tag `D0AF90DDC7A5`; `docs/sections/bedford-taylor-products-and-local-capacity--decreasing-continuity-and-symmetry/index.html`, blob `96a9e39e85fab5774ebdac0c6d9d006338a4e42c`, lines 304–338. These named local inputs are used conditionally; this report does not independently certify all of Bedford–Taylor theory.

**Precise new statement.** Fix any compact Hermitian complex `n`-fold `(X,h)`, `n≥1`, and `α>0`. For the positive density `f` constructed in the proof of Theorem 15.33.6, with its distinguished point `x_0`, write `μ=f\,dV=MA_h(u)`. On sufficiently small holomorphic coordinate balls `B_r=B(x_0,r)`, with `L_r=1-\log r^2`, there are constants `0<c<C<∞` such that

\[
cL_r^{-n}\leq\operatorname{Cap}_h(B_r)\leq CL_r^{-n},
\qquad
cL_r^{-n(1+\alpha)}\leq\mu(B_r)\leq CL_r^{-n(1+\alpha)}.
\]

Consequently **the exponent `1+α` in this concrete density's power-capacity bound is sharp**: for every `β>α` and every finite `A_β`, the proposed bound

\[
\mu(E)\leq A_\beta\operatorname{Cap}_h(E)^{1+\beta}
\quad\text{for all Borel }E
\]

fails already for the concentric balls `E=B_r`. This is stronger than the printed assertion that the density is not in any `L^p`, `p>1`; it is **not** a claim that the universal estimate in Theorem 15.33.1 is false.

**Proof.** On a sufficiently small centered ball the printed potential is `u=\delta(1-\log |z|^2)^{-\alpha}-\mathrm{constant}`, with `dd^cu\geq0` there. The exact local radial identity at 15.33.8 and its integrated version at lines 128–131 give

\[
\int_{B_r}(dd^cu)^n=\delta^n\alpha^nL_r^{-n(\alpha+1)}.
\]

Because every term of the binomial expansion of `(h+dd^cu)^n` is nonnegative in this ball,

\[
\mu(B_r)\geq\delta^n\alpha^nL_r^{-n(\alpha+1)}.
\]

Conversely, the source estimate (15.33.9) yields `μ(B_r)\leq C[L_r^{-n(\alpha+1)}+r^2]`; the `r^2` term is negligible relative to any fixed inverse power of `L_r`. This proves the two-sided mass estimate.

We now prove the necessary **local-capacity upper bound**, including the boundary-mass subtlety. Let `B_R` be a larger concentric coordinate ball and `0<r<R`. The relative radial extremal

\[
v_r(z)=\max\left\{-1,\frac{\log(|z|/R)}{\log(R/r)}\right\}
\]

is bounded psh, equal to `-1` on `B_r` and `0` at `∂B_R`. Its top Bedford–Taylor measure is concentrated on the sphere `|z|=r`, with total mass

\[
\int_{B_R}(dd^cv_r)^n=[2\log(R/r)]^{-n}
\]

under the project's normalization `dd^c=(i/2π)∂\bar∂`. This follows either by the truncated radial flux formula, whose radial slope jumps from `0` to `1/(2\log(R/r))` in the variable `s=\log|z|^2`, or directly from the finite-max Bedford–Taylor construction.

For any `w\in PSH(B_R)` with `0\leq w\leq1`, set `U_\varepsilon=(1+\varepsilon)v_r`, `V=w-1`. The boundary condition of Theorem 7.3.11 holds because `U_\varepsilon\to0` at `∂B_R` and `V\leq0`. On **all of the open ball** `B_r` one has `U_\varepsilon=-(1+\varepsilon)<V`, including where `w=0`. Thus comparison (with this strict perturbation to avoid losing charge on the contact set) gives

\[
\int_{B_r}(dd^cw)^n
\leq\int_{\{U_\varepsilon<V\}}(dd^cV)^n
\leq\int_{\{U_\varepsilon<V\}}(dd^cU_\varepsilon)^n
\leq\frac{(1+\varepsilon)^n}{[2\log(R/r)]^n}.
\]

Letting `ε\downarrow0` and taking the supremum proves `Cap_{B_R}(B_r)\leq[2\log(R/r)]^{-n}`. We do not incorrectly treat the extremal's sphere charge as lying in the *open* ball.

To pass from local to global Hermitian capacity, choose one fixed smooth `q` on `B_R` with `dd^cq\geq h`. For any global admissible `0\leq\varphi\leq1`, `h+dd^c\varphi\geq0`, the function `q+\varphi` is bounded psh on `B_R`. With fixed `M=1+\sup_{B_R}q-\inf_{B_R}q`, the function `w=(q+\varphi-\inf q)/M` lies in `[0,1]`, and positivity/multilinearity imply

\[
(h+dd^c\varphi)^n\leq (dd^c(q+\varphi))^n=M^n(dd^cw)^n.
\]

Consequently `Cap_h(B_r)\leq M^n[2\log(R/r)]^{-n}\leq CL_r^{-n}`.

Finally Theorem 15.33.6 itself proves `μ(E)\leq A\,Cap_h(E)^{1+\alpha}` for all Borel sets. Apply it to `B_r` and combine with the just-proved mass lower bound:

\[
\operatorname{Cap}_h(B_r)\geq
(\delta^n\alpha^n/A)^{1/(1+\alpha)}L_r^{-n}.
\]

The two sharp asymptotics follow. For `β>α`, use only the mass *lower* and capacity *upper* bounds to conclude

\[
\frac{\mu(B_r)}{\operatorname{Cap}_h(B_r)^{1+\beta}}
\geq cL_r^{n(\beta-\alpha)}\longrightarrow+\infty .
\]

All comparison operations here concern ordinary **bounded** local Bedford–Taylor products, never the excluded Demailly approximation programme. The constants depend on the fixed chart/background/construction, not on `r`.

**Proposed noninvasive addition:** a sharpness remark immediately after Theorem 15.33.6 or the final tail estimate. **Affected dependents:** interpretation of §15.33's power-capacity theorem and any attempt to upgrade this constructed datum to a larger exponent. No defect in the printed theorem or required source correction.

## Finding POME-PLURI-FIBER-HIGHERDIM-001

**Severity:** low. **Status:** verified conditional deduction, **not** a false printed theorem.

**Source:** Lemma 11.22.4, permanent tag `3CD7629C6061`, `docs/sections/gauduchon-metrics-and-linear-mass--pluriharmonic-currents/index.html`, blob `046c12d159f8aaeff268c57d822253da11ed41ba`, lines 101–132 (especially 105–121). Lemmas 11.22.1–2, tags `D9A37BB4C36B`, `25BD2AAB112A`, lines 11–59, were also examined for the positivity and `dd^c` scope; Lemma 11.22.3's heat-flow proof is **not** a new regularization project.

**Prior-ledger distinction:** `POME-PLURI-FIBER-LIOUVILLE-001` (18 October) already treats **one-dimensional Riemann-surface fibers** characterized by positive-*harmonic* Liouville. That older finding is retained, **not** re-counted. The new statement below treats arbitrarily high-dimensional complex fibers and uses positive-*pluriharmonic* Liouville, with an explicit converse on trivial bundles.

**Precise new statement.** Let `π:Z→Y` be a holomorphic fiber bundle over a complex `ℓ`-fold `Y`, `ℓ≥1`, with connected complex fiber `F` of **arbitrary dimension `k≥1`**. Assume every nonnegative real pluriharmonic function on `F` is constant. For any positive real `(1,1)` current `S` on `Z` satisfying

\[
dd^cS=0,\qquad S\wedge\pi^*\eta^\ell=0
\]

for a Hermitian `η` on `Y`, there exists a unique positive `dd^c`-closed `(1,1)` current `R` on `Y` with `S=\pi^*R`. If `S` is closed, so is `R`. In particular this holds for **`F=\mathbb C^k` for every `k`**, or for **any compact connected complex manifold** as fiber, without assuming `k=1`.

**Proof.** Work in a bundle trivialization `U\times F` and base coordinates `w_1,\ldots,w_\ell`. Positivity represents the `(1,1)` coefficient measures by a positive semidefinite Hermitian matrix relative to their trace measure. Wedge with `π^*\eta^\ell` detects every **vertical-vertical** matrix coefficient, now a `k\times k` positive block. The vanishing assumption therefore makes this whole block zero; Cauchy–Schwarz for the positive matrix makes every **vertical-horizontal** block zero too. Consequently

\[
S=(i/2\pi)\sum_{\alpha,\beta=1}^{\ell}
s_{\alpha\bar\beta}(w,z)\,dw_\alpha\wedge d\bar w_\beta .
\]

The coefficient of `dz_a\wedge d\bar z_b\wedge dw_\alpha\wedge d\bar w_\beta` in `dd^cS=0` gives, for every `a,b,α,β`,

\[
\partial_{z_a}\partial_{\bar z_b}s_{\alpha\bar\beta}=0
\quad\text{as distributions}.
\]

Pairing the horizontal positive matrix with `v\in\mathbb C^\ell` and with an arbitrary nonnegative compactly supported test density `ξ(w)` on the base produces a **nonnegative real pluriharmonic distribution on `F`**. The local Weyl lemma (distributional `∂\bar∂=0`) makes it a smooth nonnegative pluriharmonic function. By the assumed Liouville property it is constant along `F`. Polarization in `v` and linearity in `ξ` show each `s_{\alpha\bar\beta}` is independent of `z` and pulled back from a coefficient distribution on `U`. Pairing against one compactly supported fiber density of integral one gives the positive descended current `R_U`. Pullback by a submersion is injective on currents; therefore `dd^cR_U=0`, and also `dR_U=0` if `dS=0`. Uniqueness glues the `R_U` across trivializations.

On `F=\mathbb C^k`, restrict a nonnegative pluriharmonic function to every affine complex line: each restriction is a nonnegative harmonic function on `ℂ` and hence constant; the original function is constant. On compact connected `F`, a real pluriharmonic function is locally harmonic and attains a maximum, so it is constant by the maximum principle.

**Optimal fiber condition on trivial bundles.** Conversely, if `F` admits a nonconstant nonnegative real pluriharmonic `a(z)`, let `U\subset\mathbb C^\ell` be a coordinate ball and `η_0` a fixed flat Kähler form there. On `U\times F`, the horizontal current `S=(1+a(z))\pi^*\eta_0` is positive, `dd^c`-closed and satisfies `S\wedge\pi^*\eta_0^\ell=0`, but is not a pullback. Thus positive-pluriharmonic Liouville is also **necessary** for the universal descent assertion on all trivial bundles.

**Proposed noninvasive addition:** a higher-fiber-dimensional corollary to Lemma 11.22.4, explicitly referring to the older Riemann-surface `POME-PLURI-FIBER-LIOUVILLE-001` instead of duplicating it. **Affected dependents:** positivity/trace descent arguments used for fibered Hermitian current classes. No claim that arbitrary holomorphic maps admit current pullbacks.

## Additional passages actually checked; no new issue registered

- **§14.19:** Lemma 14.19.14 (tag `370AD0860DAD`, lines 209–248), Lemma 14.19.16 (tag `9C1A40570E78`, lines 254–297), and Proposition 14.19.23 (tag `3B70BD39881D`, lines 370–407), in `docs/sections/continuous-solutions-and-normalization/index.html`, blob `e4a9ece552056fdc387f170362cc1cc5c5fd4091`. Inspected sublevel parameter choice `δ_ε\asymp ε^3`, iteration `a(s_{j+1})≤a(s_j)/2`, capacity lower bound and the stability exponent `α/[3n(1+α)+α]`. These are **selected internal deduction and sign checks**, not a certification of the smooth Hermitian equation or all PDE inputs.
- **§5.48:** Theorem 5.48.1 (tag `8F5E6DB87531`, lines 14–35) and Theorem 5.48.2 (tag `5FF0038BBA5C`, lines 41–69), `docs/sections/stokes-formula-and-homotopies/index.html`, blob `bd3ba3b5150ff2a60c265f67706f74f9c980333c`. Selected boundary-orientation signs and `dt` homotopy identity checked; no new error or deduction asserted.

The present report records **only** these specific integrated passages. Historical records, canonical source tags, differently quantified results and nets stay intact. In particular, no current theorem is labeled false, no new regularization work is undertaken, and neither build nor formal proof verification is claimed.
