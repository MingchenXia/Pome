# Flat Kähler-torus boundary test for the foliation leaf-relation criterion

**Date:** 2026-11-04. **Reviewed production main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. **Finding ID:** `POME-FOL-TORUS-LEAFREL-RATIONAL-IRRATIONAL-001`. **Classification:** low / **verified conditional deduction** (independent explicit models; **neither** a false theorem nor a general proof certification).

## Exactly inspected integrated anchors

- `docs/sections/from-local-leaves-to-a-meromorphic-fibration/index.html`, main blob `285a6dbc3d2aeddc105f931a2377cc90d2d101de`, source `cao-paun-foliations:A7CD555C`, section/permanent tag `6374AD3A13A2`: pseudo-effectivity convention, physical line 8; regular foliation, local leaf relation and normal/conormal identification, lines 12–18; closure-dimension and quotient implication, line 21; Barlet/cycle-space inputs and projections, lines 24–27.
- `docs/sections/conormal-positivity-of-an-analytic-germ/index.html`, main blob `8884dd6b27094e69d54d97004ffa1bd81558c6b8`: Theorem **9.73.1**, source `cao-paun-foliations:DB4DFCD8`, permanent tag `E76BA49374E5`, physical lines 10–14 (statement); its proof and external positivity inputs were **not** re-certified.
- The section inventory is that of the current 25-chapter/747-numbered-section reading edition; this increment adds a concrete model to previously selected §9.74 steps, **not** a complete review of that section or of the external `Ou2025` cycle-space lemma.

## Explicit Kähler surface and two genuinely different analytic closures

Set `E = C/(Z+iZ)` and `A = E × E`, a compact connected Kähler surface. Its tangent bundle is holomorphically trivial. For any real `alpha`, let `F_alpha` be the nowhere-vanishing constant holomorphic rank-one subbundle generated in the covering coordinates by
```text
v_alpha = ∂/∂z + alpha ∂/∂w .
```
The quotient `T_A/F_alpha` is trivial, e.g. the constant holomorphic one-form `dw-alpha dz` has kernel `F_alpha`. Thus the sheaf is **saturated**, the distribution involutive, and its regular locus `U` is all of `A`. Furthermore `F_alpha^* ≅ O_A`; its flat zero-curvature metric satisfies §9.74's approximate pseudo-effectivity convention for every `epsilon>0`.

For small `epsilon>0`, the local leaf-relation germ near the diagonal of `A×A` is parametrized holomorphically by
```text
(p,t) ↦ (p, p + [(t,alpha t)]),    p∈A, |t|<epsilon .
```
It is a smooth local complex submanifold of dimension `2+1=3`, with normal along the diagonal `N_{A/S}≅F_alpha`: a tangent pair `(u,u+s v_alpha)` maps to the difference `s v_alpha`. This explicitly verifies the integrated lines 12–18, including the **normal** rather than conormal sign convention.

### Irrational slope: a genuine dimension jump

Let `alpha=√2`. The immersed complex leaf subgroup
`H_alpha = {[(t,alpha t)] : t∈C} ⊂ A`
is dense in the **entire real four-torus** `A`. Write `t=x+iy`. In real torus coordinates the subgroup is
`(x,y,alpha x,alpha y) mod Z^4`.
For any prescribed first and third real coordinates `(a,b) mod Z²`, put `x=a+k`, `k∈Z`. The first coordinate is exactly `a`, and the third is `alpha a+k alpha`, dense modulo one because rotation by irrational `alpha` is dense. The same independent choice `y=c+l` gives any prescribed second and fourth coordinates. (Density of an irrational circle rotation follows directly from the pigeonhole small-return argument.) Hence `closure(H_alpha)=A`.

To determine **analytic Zariski closure of the local germ**, not merely topological closure of a global leaf, take any closed analytic subset `Z⊂A×A` containing the local `S`. Apply the biholomorphism `(p,q)↦(p,q-p)`. For each fixed `p∈A`, the analytic fiber `Z_p⊂A` contains the small analytic arc `t↦[(t,alpha t)]`. The inverse image of `Z_p` under this holomorphic map from `C` is analytic and contains a nonempty open disc, so is all of `C` by the one-variable identity theorem. Consequently `Z_p` contains `H_alpha`; because `Z_p` is closed and `H_alpha` is dense, `Z_p=A`. This holds for every `p`, whence **`Z=A×A`**. Thus the local leaf relation has `dim S=3` but analytic closure `M=A×A` of dimension **4**.

There is **no nonconstant meromorphic quotient with those leaves as fibers**. For completeness, a meromorphic map `f:A⇢Y` with compact target and whose general fibers contain the leaves has a closed analytic graph `Gamma_f⊂A×Y`. Invariance of `f` along every translation by `H_alpha`, as meromorphic maps, makes `Gamma_f` invariant under the subgroup. Its stabilizer under translations is closed, because the graph is closed; density makes it invariant under **all** translations of `A`. The graph of a generically single-valued map with this invariance must have constant value, hence `f` is constant. Equivalently a nonconstant quotient would have compact proper general leaf closures, impossible here.

### Rational slope: no dimension jump and a holomorphic quotient

Let `alpha=a/b∈Q`, with integers `a,b`, `b>0`, `gcd(a,b)=1`. The group homomorphism
`f_{a,b}:A→E,quad f_{a,b}(z,w)=b w-a z`
is a surjective holomorphic submersion with **connected** elliptic kernel: a primitive integer row `(-a,b)` extends to an integer unimodular matrix, which induces an automorphism of `E²` taking the kernel to `E×{0}`. The leaf subgroup `H_alpha` is precisely this kernel (its tangent is the line of `v_alpha`, and it is the connected kernel).

The analytic leaf relation is the closed smooth subset
`M_alpha = {(p,q)∈A² : f_{a,b}(q)=f_{a,b}(p)}`,
of complex dimension **3**. The local relation germ `S` is open inside this subset around the diagonal, so its analytic Zariski closure equals `M_alpha`, and `dim M_alpha=dim S=3`. Here `f_{a,b}` explicitly realizes the quotient.

## Precise inference and boundary

In **both** cases `F_alpha^*` is the **same trivial, hence pseudo-effective**, holomorphic line bundle. Nevertheless the analytic closure of the local leaf-relation germ jumps in dimension for `alpha=√2`, and does **not** jump for `alpha∈Q`. Therefore pseudo-effectivity of the foliation conormal **does not decide** whether the §9.74 dimension equality and meromorphic quotient exist. The **printed direction** `non-pseudo-effective conormal ⇒ no dimension jump ⇒ meromorphic quotient` remains correct and is not weakened or reversed by these models. In the irrational model the hypothesis of non-pseudo-effectivity is false, as required by the contrapositive of Theorem 9.73.1. In the rational model non-pseudo-effectivity is not necessary for the quotient.

**No general theorem is proved or refuted.** The examples require only explicit holomorphic torus geometry, the one-variable identity theorem and elementary irrational-rotation density. They do **not** require the quoted Barlet compactness, cycle-family or `Ou2025` meromorphic-fibration inputs. Those remain genuine **external dependencies** for the general §9.74 passage, neither resolved nor certified. The user-excluded Demailly approximation/regularization, Bergman, weighted L², Ohsawa–Takegoshi, multiscale and positivity-loss proof-completion programmes remain **deferred-by-user**, untouched.

**Proposed nonproduction change:** optionally append these rational/irrational compact-torus models after §9.74's closure-dimension paragraph to prevent a converse interpretation. Preserve original attribution and source/permanent tags. **Affected downstream interpretations:** §9.74's quotient inference and uses of the conormal non-pseudo-effectivity hypothesis in §9.75–9.77 (logical scope only; no theorem patch asserted).

**Coverage accounting:** exact integrated §9.74 lines 8, 12–18, 21, 24–27; Theorem §9.73.1 statement only. Neither the analytic-cycle existence result nor a complete section proof is newly certified. No main/source, registry, tags, CI, tests, build, or publication changes.
