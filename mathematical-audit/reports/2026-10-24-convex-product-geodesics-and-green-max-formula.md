# Bounded convex products: exact invariant distances, Green functions, and extremal-disc flexibility

**Checkpoint:** 2026-10-24; first selected proof-level review of the current integrated §§9.17–9.18 and §9.20.
**Reviewed `main`:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.
**Finding:** `POME-CONVEX-PRODUCT-INVARIANT-MAX-001` — **low / verified conditional deduction**, not a printed-theorem error. This deduction relies on the explicitly stated and partially inspected Lempert existence result (Theorem 9.20.5); the latter's entire proof chain is **not** thereby certified. The same product formula can be proved by independent analytic methods, but no such additional input is claimed here.

## Integrated reading-edition anchors and hypotheses

- **§9.17 Proposition 9.17.4**, source `klimek-pluripotential-theory-17EB5D84`, permanent tag `F0CC92394671`: `docs/sections/schwarz-estimates-and-invariant-distances/index.html`, blob `11789d8f51f81ec69de4fbb206c1186c73540b0e`, physical lines **110–145**. The Carathéodory, Lempert one-disc, Kobayashi and Green function contraction bounds hold on domains; conventions use `q(0,t)=atanh(t)` and `g_D(a,a)=-infinity`.
- **§9.17 Proposition 9.17.5**, source `klimek-pluripotential-theory-B51FDB0F`, permanent tag `32C365095F79`, same file/blob, lines **159–174**: `c_D <= sigma_D <= k_D`.
- **§9.18 Theorem 9.18.1**, source `klimek-pluripotential-theory-9F2D2DA4`, permanent tag `7F33F823B79C`: `docs/sections/disc-interpolation-on-convex-domains/index.html`, blob `c0f853924bef4d4b35d3580d5c330de6613b1407`, lines **10–56**. Its domain must be **bounded and convex**.
- **§9.18 Proposition 9.18.2**, source `klimek-pluripotential-theory-B5E61683`, permanent tag `0A57323E9BD0`, same file/blob, lines **61–84**. The stationary lift is an explicit hypothesis, not a property supplied for every extremal disc without proof.
- **§9.20 Propositions 9.20.1–9.20.4 and Theorem 9.20.5**, source respectively `klimek-pluripotential-theory-0D2877F2`, `klimek-pluripotential-theory-A18B79C9`, `klimek-pluripotential-theory-0555BBFB`, `klimek-pluripotential-theory-D47F53B8`, `klimek-pluripotential-theory-5E98FA95`, permanent tags `659A580EE96C`, `415609592B60`, `5DE7AB27F999`, `E378BBBF406D`, `7264782B9A80`: `docs/sections/complex-geodesics-on-bounded-convex-domains/index.html`, blob `406faf6cf759c6aa6ed9b0cee3792ba6b5a85f65`, lines **10–32**, **37–80**, **85–114**, **119–168**, **173–205**. The final theorem supplies a holomorphic retract disc through **each pair of distinct points** in a bounded convex domain.
- Example 9.20.6, source `klimek-pluripotential-theory-CE4E1BD6`, permanent tag `8E0727128F9C`, same blob, lines **210–218**, was checked only for the boundary-continuity qualification.

## Finding POME-CONVEX-PRODUCT-INVARIANT-MAX-001

**Precise claim.** Let `m>=1` and let `D_i` be nonempty bounded convex domains in `C^{n_i}` (with `n_i>=1`). Put `D=D_1 x ... x D_m`, and write `z=(z_i)`, `w=(w_i)`. With exactly the printed invariant-distance and logarithmic Green normalizations,

```math
 c_D(z,w)=k_D(z,w)=delta_D(z,w)=sigma_D(z,w)
          = max_i c_{D_i}(z_i,w_i)
          = max_i delta_{D_i}(z_i,w_i),
```

and

```math
 g_D(z,w)=max_i g_{D_i}(z_i,w_i).
```

In addition, **any** Schwarz–Pick pseudodistance system `s` as defined in §9.17.4 satisfies
```math
 s_D(z,w)=max_i s_{D_i}(z_i,w_i).
```
All Green values at the pole are interpreted as `-infinity`; the formulas include coincident coordinates, and for `z=w` the distance is zero and `g_D(z,z)=-infinity`.

**Proof.** Fix distinct `z,w`. For each factor set
```math
 t_i=tanh(delta_{D_i}(z_i,w_i)), \qquad t=max_i t_i.
```
By §9.20.5 and the normalization of `q`, `0<=t_i<1`; for `t_i>0`, there are holomorphic `f_i:Delta->D_i`, `P_i:D_i->Delta` with
```math
 f_i(0)=z_i,\quad f_i(t_i)=w_i,\quad P_i\circ f_i=id_Delta.
```
When `t_i=0`, use the constant map `f_i(ζ)=z_i=w_i`. Since `z≠w`, `0<t<1`. Define
```math
 F_i(ζ)=f_i((t_i/t)ζ)\ (t_i>0),\qquad F_i(ζ)=z_i\ (t_i=0);
 \qquad F=(F_1,\ldots,F_m):Delta\longrightarrow D.
```
Then `F(0)=z`, `F(t)=w`. Choose any `i_0` attaining the maximum. Its factor is unscaled: `F_{i_0}=f_{i_0}`. Consequently
```math
 P=P_{i_0}\circ pr_{i_0}:D\to Delta,\qquad P\circ F=id_Delta.
```
Thus the two holomorphic contractions give
```math
 q(0,t)=c_D(z,w)=delta_D(z,w)=k_D(z,w)=sigma_D(z,w).
```
Alternatively, the `delta` upper bound comes directly from `F`; the reverse lower bound follows by composing any joining disc with every coordinate projection. The other three equalities follow from `c<=sigma<=k<=delta` and the holomorphic left inverse. By §9.20.5 in the factors, `atanh(t_i)` is each factor's common distance, whence the maximum formula.

For the Green function, holomorphic contraction (§9.17.4) under each projection gives
```math
 \max_i g_{D_i}(w_i,z_i)\le g_D(w,z).
```
The same contraction under `F` gives
```math
 g_D(w,z)=g_D(F(t),F(0))\le g_Delta(t,0)=\log t.
```
Since the factor retracts imply `g_{D_i}(w_i,z_i)=log(t_i)` when `t_i>0`, and the coincident-coordinate value is `-infinity`, the left hand side is `log t`. This proves equality (and relabeling `w,z` proves the displayed formula). For `z=w`, the stated diagonal conventions settle both identities. Finally, every Schwarz–Pick system is squeezed between `c` and `k` by Proposition 9.17.4, and these coincide for all bounded convex factors and for their product. Hence the universal-system assertion follows. No limit of currents, sequence/net compactness, or excluded approximation theorem is used in this deduction. QED.

### Flexibility and nonuniqueness of geodesic representatives

The constructed `F` has a left inverse and is extremal for **every** two distinct parameters, not just `0,t`. The product formula therefore gives an explicit constructive supplement to Lempert's existence theorem on products with corners.

Suppose `m>=2` and some `t_j<t`. If `t_j>0`, replace the `j`th factor above by
```math
 f_j(\varphi_\varepsilon(ζ)),\quad
 \varphi_\varepsilon(ζ)=(t_j/t)ζ+\varepsilon ζ(ζ-t).
```
For `|\varepsilon|<(1-t_j/t)/(1+t)`, this maps `Delta` into `Delta` and preserves values `0,t_j` at `0,t`. Different `\varepsilon` give different discs because `P_j\circ f_j=id` forces injectivity. If `t_j=0`, replace the constant coordinate by
```math
 F_j(ζ)=z_j+\varepsilon v ζ(ζ-t)
```
for any nonzero `v in C^{n_j}` and all sufficiently small complex `\varepsilon`; the open ball about `z_j` contained in `D_j` controls its image. In either case, the dominant-factor left inverse `P` is unchanged. There are infinitely many pair-extremal retract discs.

If at least two distinct factors attain `t>0`, **one and the same** constructed retract disc has at least two distinct holomorphic left inverses `P_i\circ pr_i`, as these depend nontrivially on different independent coordinates. These are statements about product-domain flexibility, not uniqueness of smooth strongly convex geodesics.

## Independent checks of selected proof passages

1. **§9.17.4, lines 134–145:** the bound `c<=k<=delta`, Green contraction and the local affine-disc estimate have the exact directions used above. The local `atanh(|z-a|/r)` bound is used only for an **inner** Euclidean ball; it does not falsely assume the domain is convex.
2. **§9.18.1, lines 17–43:** in the triangle interpolation, for `0<A<B<1`, `L(0)=1`, `L(B)=0`, and `0<L|_T<1` because `x+x^{-1}` is decreasing on `(0,1)`. The pole at `A` cancels as `f(A)=g(A)`; the convex hull argument is properly made for a compact boundary image within `D`. The more global existence theorem is still a conditional internal input.
3. **§9.18.2, lines 75–83:** the sign of the support inequality for `G/ζ` yields winding zero, so `G` has one zero, counted with multiplicity. This validates the local left-inverse step under the **stationary dual hypothesis**; that hypothesis must not be silently omitted.
4. **§9.20.2, lines 61–79:** on the unit circle, the positive weight transforms the dual to
```math
 \varphi h={ζ H(ζ)(1-tζ)\over
 (ζ-\lambda)(ζ-\eta)(1-\bar\lambda ζ)(1-\bar\eta ζ)}.
```
The poles at the new interpolation nodes disappear when multiplied by variations vanishing at those nodes, so the Cauchy integral is zero. This is a sign/pole check only, not full certification of the Hahn–Banach/`H^1` representation chain.
5. **§9.20.3–5, lines 91–113, 147–167 and 185–205:** the rate from `atanh|ζ| <= C+(1/2)log(1/d(f(ζ)))` has the direction `d(f(ζ))<=C'(1-|ζ|)`; combining with the exterior tangent-ball derivative estimate yields `|f'(ζ)|<=C(1-|ζ|)^{-1/2}`. The stationary-lift positivity, exhaustion and diagonal normal-family steps were read but their complete analytic dependencies were not recertified. Example §9.20.6 legitimately rules out replacing strong real convexity by arbitrary smooth convex boundary for universal closed-disc continuity.

**Classification and proposal.** No newly confirmed incorrect statement or missing hypothesis was established in these selected passages. `POME-CONVEX-PRODUCT-INVARIANT-MAX-001` is a **verified conditional deduction**, with the stated bounded-convex and factor-retract hypotheses; it is **not** independent proof of all of §9.20. Propose a separately reviewable, optional product-domain corollary after Theorem 9.20.5 (including coincident-coordinate conventions and explicit nonuniqueness), without changing existing proof bodies, source attributions, canonicalizations, or permanent tags. Direct dependents: product Carathéodory/Kobayashi/Lempert distances, product pluricomplex Green functions, and extremal-disc examples.

**Coverage:** first explicit selected-proof entries for §§9.17, 9.18, 9.20 (partly cross-referenced historically but previously inventory-only in the matrix). Contextual §§9.19 and 9.24 are not upgraded. No complete chapter/section is certified; all 747 sections are only a table-of-contents inventory. **Not run:** full Pome build, CI, website publication, formal verification, numerical scripts. **Strictly deferred by user:** Demailly approximation/regularization and its dedicated Bergman, L², Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof-completion programme. Historical findings retained unchanged as `deferred-by-user`, neither solved nor certified.
