# Two logarithmic poles: multiplier-ideal rounding, nonadditivity, and the same limiting Okounkov body

**Date:** 2026-11-03. **Reviewed production `main`:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. **Finding:** `POME-OKO-TWO-POLE-FLOOR-CEILING-001` — **low / verified conditional deduction**. This is a direct calculation in a new singular two-pole model, **not** a claim that any printed Pome theorem is false, not a full-section certification, and not a rerun of the earlier unweighted projective-line twisting model `POME-OKO-P1-TWIST-001`.

## Exact reading-edition references and scope

- `docs/sections/the-theory-of-okounkov-bodies--algebraic-partial-okounkov-bodies/index.html`, blob `c661e264cab0995a2a344453039940028feff8e0`, source `sgpt`. Definition 19.4.2, source `sgpt:F679E79A`, permanent `0F5DB984097B`, **physical lines 25–33**; Definition 19.4.3, source `sgpt:68553106`, permanent `DCCC835656D0`, **lines 37–42**; Proposition 19.4.11, source `sgpt:DBBE11BD`, permanent `AE88967EEE84`, **lines 141–169**; Theorem 19.4.16, source `sgpt:1C31F648`, permanent `A653D079A694`, **lines 250–255**; Corollary 19.4.19, source `sgpt:7E7DA8C6`, permanent `56E59F7A3150`, **lines 276–283**; equation 19.4.21, permanent `2AE36B08DED5`, **lines 292–309**.
- `docs/tag/99446B95B55B/index.html`, blob `4c3eaa6c3f2736da98145867be4a44b465e266a8`, Definition 5.18.11, permanent `99446B95B55B` (supremum-growth ideal); `docs/tag/A3A5C96E566B/index.html`, blob `2c246bf67b4394481f5e1e150fe77ae23cbf2e1d`, equation 19.2.1 (the asymptotic symmetric-difference pseudometric).
- A separate **selected proof-step** check: `docs/sections/equations-with-prescribed-singularities--the-homogeneous-equation-with-a-holder-reference/index.html`, blob `0defdec5270db7ff34625b638c9ac2a31264ca4a`, Theorem 15.25.1, source `non-kahler-pluripotential-theory:6A4C8C89`, permanent `8CE230CD94D4`, **lines 11–19, 25–69**. Its Lemma 5.42.7 approximation input was **only recorded as an upstream dependency**, not audited.

## Model and independent computation

Use the convention `dd^c=i/(2π)∂∂̄`. Let `X=P^1`, `L=O(d)` with integer `d>=1`, `ω=ω_FS` normalized by `∫_X ω=1`, and `θ=dω`. Let `s_0,s_∞` be the canonical sections of `O(1)` cutting out `0=[1:0]` and `∞=[0:1]`. Fix **rational** `a,b>0` with `a+b<d`, and set
```math
φ=a\log|s_0|_{FS}^{2}+b\log|s_\infty|_{FS}^{2}.
```
The Poincaré–Lelong identity gives the **exact current equality**
```math
θ+dd^cφ=(d-a-b)ω+a[0]+b[∞].
```
Thus `φ` has analytic singularities and `θ_φ` is a Kähler current (its smooth residual dominates `(d-a-b)ω`). In dimension one the non-pluripolar product deletes the two polar atoms, so `⟨θ_φ⟩=(d-a-b)ω` and `vol(θ_φ)=d-a-b>0`.

In a coordinate `z` centered at a pole of coefficient `a`, the local integrability of `z^j` against `e^{-kφ}` is exactly
```math
\int_0^\delta r^{2j-2ka+1}\,dr<\infty\quad\Longleftrightarrow\quad j>ka-1\quad\Longleftrightarrow\quad j\ge\lfloor ka\rfloor.
```
On the other hand, Definition 5.18.11 gives `\log|z^j|^2\le ka\log|z|^2+O(1)` **if and only if** `j>=ceil(ka)`. Consequently, with the analogous condition at infinity,
```math
\mathcal I(kφ)=\mathfrak m_0^{\lfloor ka\rfloor}\mathfrak m_\infty^{\lfloor kb\rfloor},\qquad
\mathcal I_\infty(kφ)=\mathfrak m_0^{\lceil ka\rceil}\mathfrak m_\infty^{\lceil kb\rceil}.
```
Here the notation denotes the globally defined two-point ideal sheaves; these formulas hold for **every positive integer k**, with integral threshold values handled correctly.

Take the flag valuation `ν=ord_0`. Since the monomials `Z_0^{dk-j}Z_1^j` for `0<=j<=dk` form a basis, the exact degree-`k` valuation sets are
```math
\Gamma(θ,φ)_k=\{j\in\mathbb Z:\lfloor ka\rfloor\le j\le dk-\lfloor kb\rfloor\},
\qquad
\Gamma^\infty(θ,φ)_k=\{j\in\mathbb Z:\lceil ka\rceil\le j\le dk-\lceil kb\rceil\}.
```
Empty integer intervals mean the empty set; for all sufficiently large `k` both are nonempty. Therefore
```math
\Delta_k(θ,φ)=[\lfloor ka\rfloor/k,\ d-\lfloor kb\rfloor/k],\quad
\Delta_k^\infty(θ,φ)=[\lceil ka\rceil/k,\ d-\lceil kb\rceil/k]
```
for large `k`, and both converge in Hausdorff distance, with error **at most `1/k`**, to
```math
\boxed{\Delta_\nu(θ,φ)=[a,d-b],\quad \operatorname{length}\Delta_\nu(θ,φ)=d-a-b=\int_X\langle θ_φ\rangle.}
```
In particular the *exact* section counts for large `k` are
```math
h^0(X,L^k\otimes\mathcal I(kφ))=dk-\lfloor ka\rfloor-\lfloor kb\rfloor+1,
\quad
h^0(X,L^k\otimes\mathcal I_\infty(kφ))=dk-\lceil ka\rceil-\lceil kb\rceil+1.
```
The degree-`k` symmetric difference consists of at most **two** valuations. With the *actual* definition (19.2.1), `d_{sg}(Γ,Γ^∞)=limsup_{k→∞}k^{-1}|Γ_k△Γ_k^∞|=0`. This verifies the conclusion of equation 19.4.21 in the present model **without** using the quasi-equisingular approximation machinery.

### Important finite-degree distinction: the ordinary family need not be additive

Set **`d=2` and `a=b=3/5`**. Degree one has `Γ_1={0,1,2}`: in particular `Z_0^2` is allowed. Its square `Z_0^4` has valuation `0`, but `Γ_2={1,2,3}` because `floor(2·3/5)=1`; hence `(0,1)+(0,1)=(0,2)` is **not** in `Γ`. So the ordinary multiplier-ideal valuation family is **not a semigroup**. In contrast the supremum-growth family `Γ^∞` *is* additive: `ceil(x)+ceil(y)>=ceil(x+y)` guarantees that products preserve both required vanishing orders. The two families nevertheless have the **same** limiting body `[3/5,7/5]` and asymptotic volume `4/5`.

This is a genuine finite-degree rounding obstruction rather than a mathematical defect in the printed construction: §19.4 uses the **almost-semigroup / `d_{sg}`-closure** framework and does not assert that ordinary `Γ` is additive. A future canonicalization must not silently identify the finite-level sets or replace `Γ` by an honest semigroup. The calculation is different from the older unweighted `P^1` twisting-interval check and from the prior §19.4.43 denominator-clearing proof-gap report; their statuses remain unchanged.

## Separate selected check in §15.25.1 (not a new finding)

Lines 25–36 first approximate `g` by continuous `g_l` in `L¹(σ)`. The needed estimate is
```math
\int_X|g_l^{1/n}-g^{1/n}|\,dσ\le
σ(X)^{1-1/n}\bigl(\int_X|g_l-g|\,dσ\bigr)^{1/n},
```
since `|x^{1/n}-y^{1/n}|^n<=|x-y|`. For **each fixed** `l` the weak convergence of the selected smooth-reference measures applies to continuous `g_l` and the first `l` continuous test products; their diagonal construction therefore gives `ν_l⇒ν` without improperly testing weak convergence against an arbitrary Borel `g`.

Conditionally on the cited trace bound 5.29.20 and the positive limit of `I_l=∫g_l^{1/n}h_{v_l}^n`, the integrated mixed inequality (lines 41–47) yields `c_l<=B^n/(A I_l^n)` for a common trace bound `B`. Conditionally on the backwards capacity lemma 14.19.16 and comparison 14.19.14, the proof's displayed estimate (line 58) gives `c_l>=D^na_0/(Cν_l(X))`. These are distinct upper/lower inputs; they justify the compact positive scalar interval used in the limit **only if** the invoked results apply uniformly as stated. We checked the displayed hypotheses and exponent of their integrated statements, **not** the proof-completion chain. In particular the approximation invoked from §5.42.7 stays **deferred-by-user** and was not reopened.

## Disposition, proposal, and coverage boundaries

**Status:** low / verified conditional deduction for the two-pole exact calculation; no false printed theorem and no source patch applied. **Suggested optional documentation:** after Definitions 19.4.2–3, give the `d=2,a=b=3/5` finite-degree non-semigroup example and its asymptotically zero `d_{sg}` distance. **Potential dependents:** Theorem 19.4.16 and Corollary 19.4.19 may use the limiting almost-semigroup data; source-registry deduplication must not conflate ordinary multiplier ideals with supremum-growth ideals. Historical attributions are unchanged.

**Actually reviewed:** selected §19.4.2–3, 19.4.11, 19.4.16, 19.4.19–21, the precise §19.2.1 pseudometric, §5.18.11 growth-ideal definition and selected §15.25.1 density/trace/capacity lines 25–69. Analytic-singularity resolution, abstract volume identities, Monge–Ampère existence, full transitive `d_{sg}` theory and the excluded approximation are **not** independently certified. No test suite, project build, CI, website publication, formalization, or source/registry/permanent-tag modification was performed. Existing deferred-by-user notes remain deferred, **not** resolved.
