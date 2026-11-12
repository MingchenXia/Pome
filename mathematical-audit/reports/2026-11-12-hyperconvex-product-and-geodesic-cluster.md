# Product hyperconvexity and full boundary clusters of smooth convex-domain geodesics

**Checkpoint:** 2026-11-12. **Reviewed production main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. **Scope:** two independent, non-regularization mathematical audits of the integrated reading edition. Neither original statement is refuted.

**Finding A:** `POME-GREEN-FINITE-PRODUCT-HYPERCONVEX-001` — **low / verified conditional deduction** (direct proof of the product-exhaustion equivalence; interpretation using Green functions is conditional only on the printed Green equivalence).

**Finding B:** `POME-CONVEX-GEODESIC-TRANSVERSE-HINFTY-CLUSTER-001` — **low / verified conditional deduction** (direct geometric/complex-analytic verification of a stronger version of the printed example; no general Lempert existence theorem used).

## Exact reading-edition anchors

1. **§7.25 Proposition 7.25.1:** source `klimek-pluripotential-theory:22DDEF74`, permanent tag `B63D9FDC459B`, integrated path `docs/sections/boundary-zero-green-functions-and-hyperconvexity/index.html`, blob `4680003b95a90211015a03b44bd634eb331fb426`, physical lines **7–35**. The hypothesis is a **bounded domain** admitting a negative PSH exhaustion (poles permitted); the conclusion is existence of a **continuous** negative PSH exhaustion.
2. **§7.25 Theorem 7.25.2:** source `klimek-pluripotential-theory:10813A3E`, permanent tag `033C98D473B9`, same path/blob, physical lines **37–59**. The three equivalent conditions concern a bounded domain, hyperconvexity, and zero boundary limits of an isolated-pole pluricomplex Green envelope for one/every pole. Its use of an earlier Green-continuity theorem is **not** re-certified here.
3. **§9.20 Example 9.20.6:** source `klimek-pluripotential-theory:CE4E1BD6`, permanent tag `8E0727128F9C`, integrated path `docs/sections/complex-geodesics-on-bounded-convex-domains/index.html`, blob `406faf6cf759c6aa6ed9b0cee3792ba6b5a85f65`, physical lines **209–219**. Printed example gives one non-continuously extendible retract disc over a smooth convex domain.
4. **§9.20 Theorem 9.20.5** (context, not a new proof-level certification): source `klimek-pluripotential-theory:5E98FA95`, permanent tag `7264782B9A80`, same path/blob, physical lines **172–205**. We do **not** invoke the theorem's global retract-disc existence or recertify its `H^1`/stationary-lift proof chain. The elementary holomorphic contraction principle used here is the internal §9.17 invariant-distance input, only.

## A. Finite products of hyperconvex bounded domains: exact equivalence

Let `m>=2` and let `D_j\subset C^{n_j}` be **nonempty bounded domains**. Set `D=D_1×...×D_m`. Then:

> `D` admits a continuous negative plurisubharmonic exhaustion **if and only if** each `D_j` does.

**Forward direction (individual factors => product).** Choose continuous negative PSH exhaustions `rho_j` on `D_j`. The function
\[
\rho(z_1,\ldots,z_m)=\max_{1\le j\le m}\rho_j(z_j)
\]
is continuous and strictly negative. Pullbacks of PSH functions through coordinate projections are PSH; finite maxima of locally bounded-above PSH functions are PSH. For every `t>0`,
\[
\{\rho<-t\}=\prod_j\{\rho_j<-t\}.
\]
Each factor on the right has compact closure contained in `D_j`, so the product is relatively compact in `D\). This is an exhaustion. Note that **the minimum** of the `rho_j` would not have this property or automatically be PSH; the sign and maximum are essential.

**Reverse direction (product => individual factors).** Fix `j` and choose constants `a_i\in D_i` for all `i\ne j`. If `rho<0` is a continuous PSH exhaustion on `D`, then the affine holomorphic slice
\[
\rho_j(z_j)=\rho(a_1,\ldots,a_{j-1},z_j,a_{j+1},\ldots,a_m)
\]
is continuous, PSH and negative. If `z_j^{(k)}` lies in `\{\rho_j<-t\}`, its embedded sequence lies in `\{\rho<-t\}`, whose closure is compact in `D`. Its coordinate projections have convergent subsequences **inside** `D_j`. Thus `\{\rho_j<-t\}` is relatively compact for every `t>0`. This establishes the equivalence without any Monge–Ampère theorem or regularization.

**Exact Green-boundary consequence (conditional on Theorem 7.25.2).** For these bounded nonempty factors, the preceding equivalence and the printed single-pole criterion imply:
\[
\begin{aligned}
&\exists a\in D:\quad g_D(z,a)\longrightarrow0
    \quad(z\to \xi\in\partial D,\ z\in D)\\
&\qquad\Longleftrightarrow \quad
\text{every factor }D_j\text{ is hyperconvex}\\
&\qquad\Longleftrightarrow\quad
\forall a\in D:\quad g_D(z,a)\longrightarrow0
    \quad(z\to \xi\in\partial D,\ z\in D).
\end{aligned}
\]
This does **not** assert a product formula for arbitrary-domain Green functions; nor does it independently prove the source Green-continuity input. Boundedness is retained throughout.

**Status and dependents.** Direct product-exhaustion statement: fully justified elementary deduction. Green reformulation: verified **conditional deduction**, with dependency exactly Theorem 7.25.2 and its internal upstream Green boundary result. No source error detected. Optional correction/addition: a separate corollary under §7.25 stating this finite-product criterion; no edit to production text, canonicalization, permanent tags or history.

## B. Infinite-dimensional transverse freedom and complete boundary cluster disk

Retain the actual smooth bounded convex domain of Example 9.20.6:
\[
D=\{(z_1,z_2)\in\mathbb C^2: |z_1|^2+\chi(|z_2|^2)<1\},
\]
where `\chi` is the printed smooth, convex, nondecreasing, proper function with `\chi=0` on `[0,1]` and `\chi'>0` on `(1,\infty)`.

**Domain checks.** The composition `\chi(|z_2|^2)` is convex because `|z_2|^2` is convex and `\chi` is convex and nondecreasing; `|z_1|^2` is convex. Properness of `\chi` makes `D` bounded. On its defining level `|z_1|^2+\chi(|z_2|^2)=1`, either `z_1\ne0`, in which case the defining gradient is nonzero in the first coordinate, or `z_1=0`, in which case `\chi(|z_2|^2)=1` forces `|z_2|>1` and `\chi'(|z_2|^2)>0`, so the second-coordinate gradient is nonzero. Thus `\partial D` is indeed smooth.

**A whole analytic family, not merely one example.** For every holomorphic `h:Delta->C` with `|h(zeta)|<=1` everywhere (in particular every member of the closed unit ball of `H^\infty(Delta)`), define
\[
 f_h(\zeta)=(\zeta,h(\zeta)),\qquad P(z_1,z_2)=z_1.
\]
Then `\chi(|h(\zeta)|^2)=0`, hence `|\zeta|^2+\chi(|h(\zeta)|^2)=|\zeta|^2<1` and `f_h(\Delta)\subset D`. Conversely `|P(z)|<1` on `D`, so `P:D->Delta` is holomorphic and `P\circ f_h=id_Delta`. Schwarz–Pick contraction under `f_h` and `P` gives, for all `\zeta,\eta\in\Delta`,
\[
 c_D(f_h(\zeta),f_h(\eta))
 = k_D(f_h(\zeta),f_h(\eta))
 = q(\zeta,\eta),
\]
with `q(0,t)=atanh(t)` as in the integrated reading edition. Thus these are all holomorphic retract/geodesic discs, regardless of any boundary regularity of `h`. The parameter map `h\mapsto f_h` is injective, exhibiting an **infinite-dimensional** family in one fixed smoothly bounded convex domain. No classification of *all* geodesics in `D` is claimed.

**Exact cluster set, strengthening the two printed paths.** Put
\[
 w(\zeta)=\frac{1+\zeta}{1-\zeta},\qquad
 h_a(\zeta)=a\,e^{-w(\zeta)},\quad 0<a\le1.
\]
For `|\zeta|<1`, `\operatorname{Re}w(\zeta)>0`, so `|h_a(\zeta)|<a<=1`; the disc `f_{h_a}` is admissible. As `\zeta\to1` within `Delta`, `|w(\zeta)|\to\infty` in the right half-plane, hence all possible cluster values of `h_a` are in the closed disk `a\overline\Delta`.

Every `c` with `0<|c|<a` is actually achieved along points approaching 1. Write `c=|c|e^{i\theta}`, choose
\[
 \sigma=-\log(|c|/a)>0,\qquad
 w_k=\sigma+i(2\pi k-\theta),\qquad
 \zeta_k=\frac{w_k-1}{w_k+1}.
\]
Then `\operatorname{Re}w_k>0`, `\zeta_k\in\Delta`, `\zeta_k\to1`, and `h_a(\zeta_k)=a e^{-\sigma}e^{-i(2\pi k-\theta)}=c`. For `|c|=a`, replace `\sigma` by `1/k`; the values converge to `c`. For `c=0`, take `w_k=k\to+\infty`. Therefore the **full cluster set** is
\[
 \operatorname{Clust}_{\zeta\to1}h_a(\zeta)
    =a\overline\Delta,\qquad
 \operatorname{Clust}_{\zeta\to1}f_{h_a}(\zeta)
    =\{1\}\times a\overline\Delta.
\]
With `a=1/2` this gives the exact cluster set of the **printed** Example 9.20.6. The broader `a=1` choice clusters onto the entire flat complex disk `\{1\}\times\overline\Delta\subset\partial D`. These are boundary cluster sets, **not** claims that `f_h` has continuous extension or a unique boundary value. In particular the printed non-extension conclusion is correct.

**Status and dependents.** Verified direct elementary deduction from the explicitly displayed domain and the projection left inverse. Proposed optional addendum: state the entire `H^\infty` graph family and exact cluster disk after Example 9.20.6. It clarifies failure of uniqueness/regularity for extremal discs on smooth but not strongly real convex boundaries. The prior finding `POME-CONVEX-PRODUCT-INVARIANT-MAX-001` studies products of *several bounded convex domains* using the global Lempert theorem; **the present finding does neither**, and is not a repeated product-distance computation.

## Coverage, qualifications and publication boundary

**New direct proof checks:** the smoothness/convexity/retract mechanism of Example 9.20.6, the maximal boundary cluster, the §7.25 PSH-exhaustion restriction and product maximum, and the exact §7.25 Green-criterion dependency. **Not newly first-visited:** §§7.25 and 9.20 were previously partly checked (2026-10-24, with additional §7.25 boundary work on 2026-11-10). **0 newly first-visited numbered sections; 0 fully certified sections.** The production table of contents continues to list **25 chapters and 747 numbered sections**; this is inventory, not certification. The upstream Green theorem, full Lempert chain, other geodesic boundary regularity theorems and all unrelated sections remain uncertified here.

**Excluded/deferred by user:** all Demailly approximation/regularization and dedicated Bergman, `L^2`, Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof completion. Those historical notes retain **deferred-by-user**, neither verified nor resolved. No external private source, paid service, construction of singular limiting wedge products or inappropriate exchange of limits is used. No build, software tests, formal verification, GitHub Actions, publication, main/source/registry/permanent-tag/canonicalization mutation or merge was performed.