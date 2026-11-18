# Semipositive curvature rank, bigness, and sharp section-growth boundary

**Audit date:** 2026-11-19. **Finding:** `POME-SEMIPOSITIVE-FULLRANK-BIGNESS-IFF-001`.
**Classification:** low / **verified conditional deduction**. The printed corollary is correct; there is **no confirmed error or repair**.

## Immutable source coordinates and scope

- Reviewed `main` commit: `b6933b772f41b45918f7e25ed1afbbb1fd892272`.
- Directly read the **whole integrated** `docs/sections/section-growth-of-semipositive-line-bundles/index.html`, blob `41526a319c45c861a8303776f155096d1f36614a`, physical lines **5–22**.
- Corollary **19.10.1**: source `demailly-complex-geometry:4B096A2D`, permanent tag **`F31884F26A29`**, lines **7–19**. Its displayed equation **19.10.2**: source `demailly-complex-geometry:15584614`, permanent tag **`2B3916324C79`**, lines **9–11**. Section tag `54DA59AC17EF`.
- Read *dependency statements and their local argument*, **not complete proof chains**: `docs/sections/holomorphic-morse-inequalities/index.html` §10.96.1 tag `778548FB8A37` (lines 7–40); `docs/sections/flags-convex-bodies-and-section-growth/index.html` §19.9.16 tag `1EBEF54DB76D` (lines 349–359), §19.9.17 tag `EECB2B1DF1A4` (lines 365–373), and §19.9.20 tag `14480FFA5B57` (lines 431–447).
- No review of the separate L², Bergman, Ohsawa–Takegoshi, Demailly-regularization, multiscale-atlas, or positivity-loss proof programmes.

## Direct proof check of the printed statement

Write `a_m=m^{-n}h^0(X,L^m)` and `b_m=m^{-n}h^1(X,L^m)`. For smooth semipositive curvature, the Morse index integrals satisfy `I_q=0` for `q>0`, and `I_0=(1/n!)\int_X\Omega_L^n`. The weak `q=0` inequality of §10.96.1 yields `\limsup a_m\le I_0`. The strong `q=1` inequality yields `\limsup(b_m-a_m)\le-I_0`. Since `b_m\ge0`, `\limsup(-a_m)\le-I_0`, hence `\liminf a_m\ge I_0`. In dimension one the `q=1=n` relation is the Euler equality, with the same conclusion. The proof has the correct sign, correct leading coefficient, and does **not** require a Kähler base. The global holomorphic Morse inequalities are retained as **conditional upstream inputs**, not certified here.

## Newly recorded exact equivalence

Assume `n\ge1` and `X` **connected**, compact and complex, and `(L,h)` a smooth Hermitian holomorphic line bundle with `\Omega_L\ge0`. Put
```math
r=\max_{x\in X}\operatorname{rank}_{\mathbb C}(\Omega_L)_x\in\{0,\ldots,n\}.
```
Then the following are equivalent:

1. `r=n` (the curvature is positive definite at **some** point);
2. `\int_X\Omega_L^n>0`;
3. `\lim_{m\to\infty}m^{-n}h^0(X,L^m)>0`;
4. `\kappa(L)=n` (equivalently, `L` is big in the section-growth sense).

Indeed, in local Hermitian coordinates the top wedge is a **continuous nonnegative** density given by the product of the nonnegative eigenvalues, so (1) iff (2). Corollary 19.10.1 gives (2) iff (3) and the precise positive limit `\int\Omega_L^n/n!`. For (3) ⇒ (4), the intrinsic graded-series counting theorem §19.9.16 says that when the section-ratio transcendence degree is `d<n`, section dimensions are `O(m^d)`; positive `m^n` growth forces `d=n`. For (4) ⇒ (1), use the contrapositive of (1) ⇒ (3) together with §19.9.20's estimate below: if `r<n`, then `\kappa(L)\le r<n`. Thus a connected `X` satisfying these conditions is **Moishezon**: its meromorphic function field has transcendence degree `n`. No Kähler hypothesis on `X` is inserted.

For `r<n`, §19.9.20 supplies the stronger **upper bound**
```math
h^0(X,L^m)=O(m^r),
```
whose independent proof chain (especially §19.9.16, algebraic image dimension, and its holomorphic analytic inputs) is *not* certified by this session. A positive lower bound of order `m^r` **does not follow** from rank `r`, as the following complete model proves.

## All-dimensional sharpness and flat-twist obstruction (elementary model)

Fix integers `0\le r<n` and put `T=E^{n-r}` for an elliptic curve `E`, `X=\mathbb P^r\times T`. Let `p,q` be the projections, equip `H=p^*\mathcal O_{\mathbb P^r}(1)` with pulled-back Fubini–Study metric and choose an **infinite-order unitary flat** line bundle `F\in\mathrm{Pic}^0(T)`. Put `H_F=H\otimes q^*F`, using a flat metric on `F`. Their smooth curvature forms coincide, are semipositive and have **constant rank `r`**. Yet for every `m\ge1`,
```math
h^0(X,H^m)=\binom{m+r}{r}\sim m^r/r!,\qquad h^0(X,H_F^m)=0.
```
For the second identity, `F^m` is nontrivial with first Chern class zero. A nonzero holomorphic section would yield an effective divisor `D` with `\int_D\omega_T^{\dim T-1}=0`; positivity forces `D=\varnothing`, whence `F^m\simeq\mathcal O_T`, contradiction. Künneth then kills all product sections. This proves that `O(m^r)` is sharp for **every** rank `r<n` but can have zero lower-growth even with exactly the same curvature form. The special elliptic-ruled flat-twist phenomenon in the previously logged §19.11 audit is **not** counted as a second independent discovery; the contribution here is the full-rank **iff** criterion and its uniform rank-boundary synthesis.

If `X` is **disconnected**, the positive volume/global growth condition only forces **at least one** connected component to be Moishezon; it does not imply that all components are Moishezon. This explains the connectedness hypothesis in the global field statement, without modifying the printed Corollary 19.10.1.

## Classification, impact and remaining dependencies

- **Status:** verified conditional deduction; **severity:** low. No false printed theorem, no confirmed proof gap in §19.10.1, no change to its hypotheses or normalization.
- **Proposed optional documentation addition:** after Corollary 19.10.1, state full-rank iff top-volume iff big for **connected** `X`, distinguishing rank-`r<n` upper bounds from the absent lower bounds. This is a *proposed* mathematical note only, not a source/registry patch.
- **Affected dependents/interfaces:** §19.9.16–20 (section-growth/Iitaka dimension), §10.96.1 (holomorphic Morse asymptotics), §19.8.12 (existing rank-deficient Hopf model), §19.11 (existing flat-twist boundary). Do **not** canonicalize “rank `r`” with “growth exactly `m^r`”.
- **Unresolved upstream inputs:** full proof-level certification of spectral Morse asymptotics §10.96.1, the full graded-series and modification chain §19.9.16/20, and the precise meromorphic field interpretation. The present deduction is conditional on these stated results. None of those unreviewed inputs is silently certified.
- **Deferred-by-user:** all original Demailly approximation/regularization and dedicated Bergman, L², OT, multiscale-atlas and positivity-loss proof-completion checkpoints. Preserve their existing ledgers as deferred, not resolved.

**Coverage:** first direct visit and **complete direct proof reading of exactly §19.10 (one printed corollary)**; contextual partial readings of §10.96 and §19.9 only. No other section newly certified in full; **zero** complete transitive dependency-chain certifications. Main ToC remains 25 chapters / 747 numbered sections. No test/build/CI/site/main/source/tag action.
