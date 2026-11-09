# Audit — exact multiplier-ideal losses under ramification and diagonal restriction

**Date:** 2026-11-09. **Production main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272` (read afresh). **Audit branch:** `review/mathematical-audit`. **Scope:** selected nonexcluded elementary integration and algebraic checks at §6.10, with §6.6 introductory provenance only. No claim to verify the extension/Hilbert-space proofs of Theorem 6.10.1 or their Ohsawa–Takegoshi, weighted L², or Bergman dependencies. Demailly regularization and the owner's excluded proof-completion programme remain deferred-by-user.

## Exact integrated anchors and statements

- `docs/sections/lelong-numbers-and-multiplier-ideals--restriction-products-and-integral-closure/index.html`, blob `878526739ee043892cdc85040a280504328b6dea`, physical lines **20–35**: Theorem **6.10.1**, original source `foundations-of-pluripotential-theory:6A3EE132`, permanent tag `DFD10C71D607`. Its independent-product equality (6.10.3) has original equation label `foundations-of-pluripotential-theory:5253F6F9`, permanent tag `01EC6A2D5998`, physical lines **26–30**; diagonal subadditivity inclusion (6.10.4) has original equation label `foundations-of-pluripotential-theory:888EBDCC`, permanent tag `0EA6BB9CDFD8`, physical lines **31–35**.
- Same file, physical lines **66–81**: Corollary **6.10.5**, original source `foundations-of-pluripotential-theory:67803CD5`, permanent tag `05791D2DFFAA`, states `I(phi ∘ f) ⊆ f^{-1} I(phi) · O_X` and equality for submersions. Its graph/submersion proof invokes the preceding excluded analytic dependency; the comparison *statement* is our target.
- Same file, physical lines **84–93**: Proposition **6.10.6**, original source `foundations-of-pluripotential-theory:914E443D`, permanent tag `675539E4A76C`. An earlier 2026-10-27 audit already checked its elementary integral-closure root-bound step; **this report does not re-register or re-claim that work**.
- §6.6 navigation/introduction `docs/sections/lelong-numbers-and-multiplier-ideals/index.html`, main blob `4da528eba15449e622c6459d970935c4b92d4f6d`, section original label `foundations-of-pluripotential-theory:1D553871`, permanent tag `8494F0D4F79D`. Its overview, not a proof, was read for scope only.

**Convention:** `dd^c=i/(2π)∂∂̄` and `I(phi)=\{h:|h|²exp(-phi)\in L^1_loc\}`; the logarithmic weight is **`phi_c(z)=c log|z|²`**, not half that function. All models are local holomorphic germs; no unlicensed smooth or singular approximation is used.

## Basic elementary lemma (complete proof)

For `c≥0`, on a disc at the origin, the multiplier ideal of `phi_c=c log|z|²` is
```text
             I(phi_c)_0 = (z^{floor(c)}).
```
Indeed a nonzero holomorphic germ is `h(z)=z^k a(z)` with `a(0)≠0`. On a smaller disc, `|a|` is bounded above and below by positive constants. Thus its weighted squared norm is finite precisely when
```text
  ∫_0^ε r^{2k - 2c + 1} dr < ∞
      ⇔ 2k - 2c + 1 > -1
      ⇔ k > c - 1 ⇔ k ≥ floor(c).
```
This includes the integer boundary case: at `k=c-1` for integral `c≥1` the integral diverges logarithmically. The zero germ is in every ideal. No analytic extension theorem is involved.

## Finding POME-MI-BRANCH-FLOOR-DEFECT-001

**Severity:** low. **Status:** verified conditional deduction (sharpness model for the printed inclusion, *not* a false theorem). **Anchor:** Corollary 6.10.5, lines 66–81, above.

For an arbitrary integer `m≥2`, take the finite branched map `f_m:(C,0)→(C,0)`, `f_m(w)=w^m`. With `c=q+t≥0`, `q=floor(c)` and `0≤t<1`, direct use of the lemma gives
```text
  f_m^{-1} I(phi_c) · O = (w^{m q}),
  I(phi_c ∘ f_m)       = (w^{floor(m c)})
                        = (w^{m q + floor(m t)}).
```
Consequently the inclusion of Corollary 6.10.5 is strict exactly when `floor(m t)>0`. The **exact defect** as a local finite-length quotient is
```text
 length_{O_{C,0}} [ (f_m^{-1}I(phi_c)·O)_0 / I(phi_c∘f_m)_0 ]
       = floor(m t),                     0 ≤ floor(m t) ≤ m−1.
```
Every integer `r∈{0,…,m−1}` occurs: take `c=r/m`, so the downstairs ideal is the entire local ring while the upstairs ideal is `(w^r)`. In particular, the defect is unbounded as the ramification order increases even when every downstairs ideal is trivial.

The same exact sheaf-level failure holds generically along a smooth ramification divisor in any dimension using `f_m(w_1,…,w_n)=(w_1^m,w_2,…,w_n)` and `phi_c(z)=c log|z_1|²`. The map is finite and étale away from `w_1=0`. In higher dimension the quotient is supported on the branch divisor and is not a finite-length module at a point; **the length formula above is asserted only in complex dimension one**. Submersions are unaffected, and a non-submersion can also have equality (for instance `c` integral). Hence neither direction of the printed statement is altered.

## Finding POME-MI-DIAGONAL-FLOOR-CARRY-001

**Severity:** low. **Status:** verified conditional deduction (optimality of the printed diagonal *inclusion*; not an error). **Anchors:** Theorem 6.10.1 equations (6.10.3) and (6.10.4), lines 26–35.

For `k≥2` and `c_1,…,c_k≥0` on the same disc,
```text
  I( (sum_i c_i) log|z|² ) = (z^{floor(sum_i c_i)}),
  product_i I(c_i log|z|²) = (z^{sum_i floor(c_i)}).
```
The deficit in exponents is
```text
  r = floor(sum_i c_i) − sum_i floor(c_i)
    = floor(sum_i {c_i}),                 0 ≤ r ≤ k−1.
```
Every `r∈{0,…,k−1}` is attained: set `c_i=r/k` for all `i` (including `r=0`). When `k=2` and `c_1=c_2=3/4`, the right side of (6.10.4) is `O`, while the left side is `(z)`: the theorem correctly states an inclusion rather than equality. The quotient of the larger right-hand-side ideal by the smaller left-hand-side ideal has `C`-dimension exactly `r`.

For comparison, on a product of two **independent** coordinate discs, `Phi(z,w)=c log|z|²+d log|w|²` satisfies exactly
```text
        I(Phi) = (z^{floor(c)} w^{floor(d)}),
```
which is (6.10.3), not the diagonal assertion. Here is a proof independent of its excluded Hilbert-space expansion: for holomorphic `F=∑_{p,q≥0} a_{pq}z^p w^q` on a sufficiently small bidisc, integrate its squared modulus against the radial weight `|z|^{-2c}|w|^{-2d}` over angular variables. Orthogonality gives, on truncated annuli, a sum of nonnegative terms proportional to `|a_{pq}|²∫r^{2p-2c+1}dr∫s^{2q-2d+1}ds`. If the norm is finite, every nonzero `a_{pq}` requires `p≥floor(c)` and `q≥floor(d)`; conversely divisibility by `z^{floor(c)}w^{floor(d)}` leaves a bounded holomorphic factor and two integrable weights. This independently confirms the formula for these explicit weights. Restriction to the diagonal `z=w` can then acquire the exact `r`-step defect already computed.

## Classification, dependencies, and proposed change

Neither **6.10.5** nor **6.10.1** is disproved. The sharp defects explicitly distinguish **non-submersive pullback** and **diagonal restriction** from the **independent-variable product**; none permits turning the indicated inclusion into equality in general. The elementary one-dimensional radial integral, Taylor expansion, angular orthogonality and ideal quotient lengths are fully checked **within these models**. The global general-weight theorem, coherence of multiplier ideals, Ohsawa–Takegoshi extension and Hilbert bases are **not certified here**; any existing source dependency on those statements remains at its prior status and is not treated as a new gap caused by these examples.

**Proposed audit-only editorial change (not applied to production):** add a short independent `Example` after Corollary 6.10.5 recording `f(w)=w^m` and the `floor(mc)-m floor(c)` defect, and a `Remark` next to (6.10.4) illustrating the `floor(c+d)-floor c-floor d` diagonal carry. Preserve historical provenance, the original theorem numbers and permanent tags. Affected uses are any unreviewed downstream argument claiming equality for an arbitrary holomorphic map or for diagonal subadditivity; **no such downstream misuse is asserted without its own direct inspection**.

**Precise added coverage:** previously algebraically sampled §6.10, but now *new selected* Cor. 6.10.5, equations (6.10.3–4), and two independent exact sharpness calculations. §6.6 was opened only to read its introduction (not mathematically certified). **Zero newly fully certified sections**; ToC baseline **25 chapters / 747 numbered sections**. No builds/tests/formalization/CI/publication, no source/registry/canonicalization edits. Demailly regularization, dedicated Bergman/L²/OT/multiscale/positivity-loss programmes remain **deferred-by-user**, not resolved.
