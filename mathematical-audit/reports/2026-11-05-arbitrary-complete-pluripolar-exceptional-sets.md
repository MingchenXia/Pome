# Arbitrary complete pluripolar sets as exact defects of increasing bounded PSH sequences

**Finding ID:** `POME-BT-ARBITRARY-COMPLETE-POLAR-DEFECT-001`  
**Status:** verified conditional deduction (no false printed theorem; no general proof repair).  
**Severity:** low (sharpness of the exceptional-set conclusion, not a source defect).  
**Production main examined:** `b6933b772f41b45918f7e25ed1afbbb1fd892272` (2026-11-05).  
**Integrated source:** `docs/sections/bedford-taylor-products-and-local-capacity--increasing-limits-and-exceptional-envelopes/index.html`, blob `5e763bdc928794938c37dc3c7a51cc406472d076`, physical lines 6–15, 18–25, 47–57 and 62–78.  
**Stable labels:** Theorem 7.6.1, source `foundations-of-pluripotential-theory:36787F42`, permanent `A4C45B704647`; Corollary 7.6.2, source `foundations-of-pluripotential-theory:2ACED3F4`, permanent `D865A8538D7D`.  
**Direct dependents checked only contextually:** Proposition 13.7.8, `docs/sections/non-pluripolar-products--capacity-convergence-and-loss-of-mass/index.html`, source `foundations-of-pluripotential-theory:8CF7A9C6`, permanent `4B60F7F33590`, main blob `d66813856cb813722806ab912afdfd4815d2da97`, physical lines 147–173. Its use of increasing-limit capacity convergence is consistent with the present example.

## Exact realization theorem

Let `D` be a domain in `C^n`, let `w in PSH(D)` be nontrivial (not identically negative infinity), and set `E={w=-infinity}`. For every relatively compact domain `U\Subset D`, there is an increasing sequence `(u_j)` of PSH functions on `U` with `-1<=u_j<=0` such that

```text
sup_j u_j(x) = -1  if x in E intersect U,
             =  0  otherwise;
(sup_j u_j)^* = 0 on U.
```

Thus the defect set `{sup_j u_j < (sup_j u_j)^*}` is **exactly** `E intersect U`, not just a subset of a pluripolar set. The opening paragraph of the printed §7.6 exhibits this phenomenon for the hyperplane `{z_1=0}`; the same mechanism realizes the pole set of **any** nontrivial local PSH function, including complete pluripolar sets far from hypersurfaces.

**Proof.** Upper semicontinuity on the compact closure of `U` gives a finite upper bound `M` for `w` there. Put `v=w-max(M,0)-1`, so `v<0` on `U`, and define
```text
u_j = max{ -1, v/j },    j = 1,2,...
```
The maximum of two PSH functions is PSH; hence `u_j` is PSH, between -1 and 0, and increasing because `v<=0`. If `x in E` all `u_j(x)=-1`; if `x not in E`, `v(x)` is finite and `u_j(x) increases to 0`. Since `w` is nontrivial PSH, its pole set has Lebesgue measure zero (and empty interior), so `U\setminus E` is dense. The pointwise supremum is at most zero and is zero on this dense complement, forcing its upper semicontinuous regularization to be identically zero. In particular `u_j\uparrow0` almost everywhere, but `u_j\not\uparrow0` pointwise on `E`.

By Theorem 7.6.1 the sequence nevertheless converges to zero in local Monge–Ampere capacity and its bounded Bedford–Taylor products converge (where degrees are defined). Corollary 7.6.2 gives `Cap_D^*(K intersect E)=0` for every compact `K\Subset U`. This capacity claim is **conditional on** the existing internal Bedford–Taylor/capacity chain and is not an independent recertification of it; the exact defect-set construction itself needs only the elementary PSH maximum property and the standard pole-set nullity statement.

## Direct one-dimensional current calculation (normalization check)

On `D={|z|<1}\subset C`, take `w(z)=log|z|^2`; then `E={0}` and

```text
u_j(z) = max{-1, (1/j) log |z|^2},   r_j=exp(-j/2).
```

With the Pome convention `dd^c=(i/2pi) partial barpartial=(1/4pi) Delta` on real scalar distributions in one complex dimension, `u_j=-1` on `|z|<=r_j`, while outside this disk its outward radial derivative is `2/(jr)`. The jump of the normal derivative across the circle is `2/(j r_j)`, and its integral around the circle is `4pi/j`; therefore

```text
dd^c u_j = (1/j) sigma_(r_j),
u_j dd^c u_j = -(1/j) sigma_(r_j),
```

where `sigma_r` is normalized angular probability measure on `|z|=r`. Both currents converge to zero **in total variation** on every fixed relatively compact subset of the disk, while the pointwise supremum retains the isolated dip `-1` at the origin. This verifies the coefficient and sign against the first-degree case of printed Theorem 7.6.1, rather than merely citing general weak convergence. The calculations use no regularization.

## Interpretation, proposed addition, remaining gaps

**No theorem correction is required.** Theorem 7.6.1 correctly assumes almost-everywhere, rather than pointwise, convergence. Corollary 7.6.2's zero-capacity exceptional set cannot be improved to an empty set even for increasing **uniformly bounded** PSH sequences: in fact any local complete pluripolar pole set can occur *exactly*. A proposed, separately reviewable expository remark following Corollary 7.6.2 could record the construction `max(-1,w/j)` and the circle-flux check. Do **not** replace the printed hyperplane example or its historical provenance.

**Dependencies not newly certified:** PSH maximum stability, nullity of nontrivial PSH pole sets, Theorem 7.6.1's general weighted BT-product induction, local capacity continuity in §7.5, and the §13.7.8 passage from increasing sequences to arbitrary directed nets. In particular the present construction contains only a **sequence**, not a claim of cofinal sequences for arbitrary directed sets. No section, chapter, or theorem dependency chain is certified in full.

**Audit scope:** Newly reviewed the integrated claim and proof in §7.6.1–2 and the concrete consequence for §13.7.8 (the latter context only). Earlier §7.6 checks and all prior finding classifications are preserved. All user-excluded Demailly approximation/regularization, dedicated Bergman, L2, Ohsawa–Takegoshi, multiscale and positivity-loss work remains **deferred-by-user**. No production source, permanent tag, registry, build, test, CI or publication change is authorized or performed.
