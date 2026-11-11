# Relative Kodaira embeddings: global projective-bundle form and a flat-twist obstruction

Date: 2026-11-11  
Finding: `POME-RELPROJ-FLAT-TWIST-GLOBAL-TAUTOLOGY-001`  
Severity: **low**  
Status: **verified conditional deduction**. This is **not** an error in the printed local lemma; the global-projective-space obstruction concerns a stronger, unstated assertion.

## Reproducible reading-edition scope

- Production `main`: `b6933b772f41b45918f7e25ed1afbbb1fd892272`.
- Integrated HTML: `docs/sections/local-projectivity-from-relative-positivity/index.html`, blob `f17614b598855bda6fc15f266135d6fe238638cf`.
- Section §9.71, permanent section tag `045F6241DBBD`. Lemma 9.71.1, source `cao-paun-foliations:4BE67CB0`, permanent entry tag `A53CEC220C70`; physical HTML lines **8–13** (hypotheses and statement), **15–36** (printed proof).
- The lemma asserts only an embedding **locally over the base** into a product `P^N × U`, together with the equality of the indicated line bundles. Its proof uses relative evaluation at lines 24–34. The source has not claimed a global product embedding.
- Context only: §9.72, `docs/sections/projective-hartogs-extension/index.html`, blob `3191443b49a20377356f519b5e98ec29259f1c7c`, was checked for its adjacency and theorem context; no new certification of §9.72.

## Positive conditional globalization on a compact base

**Proposition.** Let `p:M → V` be a **surjective proper holomorphic submersion** between complex manifolds, let `V` be compact, and let `A` be a holomorphic line bundle admitting a smooth Hermitian metric with strictly positive curvature on every positive-dimensional fiber (the zero-dimensional case is vacuous). Then for some integer `K>0` the sheaf `E_K=p_*A^K` is locally free, and the complete relative linear system gives a **closed embedding over V**
[
j:Mlongrightarrowmathbf P(E_K^ee),qquad
j^*mathcal O_{mathbf P(E_K^ee)}(1)simeq A^K.
]
Here `P` parametrizes **lines** in the indicated dual bundle. No trivialization of `E_K` is claimed.

**Proof.** For every `v∈V`, Lemma 9.71.1 supplies a neighborhood `U_v`, an exponent `k_v>0`, and a relative closed embedding of `M_{U_v}` into a fixed projective space over `U_v`, with pullback `A^{k_v}` of the hyperplane bundle. Compactness gives finitely many such neighborhoods `U_i` and exponents `k_i`. Choose a common multiple `K` of all `k_i`, sufficiently large for the uniform vertical Kodaira vanishing used in the printed proof. Composing the local embeddings with fiberwise `(K/k_i)`-uple Veronese embeddings shows that `A^K` is relatively very ample over **these same** `U_i`; no unproved uniform shrinking of neighborhoods is involved.

Because `M` is compact and the curvature of `A` is uniformly positive on the vertical tangent bundle, the printed comparison of `K_{M/V}^{-1}` with a high power of `A` yields `H^q(M_v,A_v^K)=0` for every `q>0` and all `v`, at a common sufficiently large `K`. As in lines 24–30 of the original proof, the **stated Grauert base-change input** and local constancy of the fiber Euler characteristic give a locally free `E_K` and canonical fiber identifications `E_Kotimesmathbb C(v)simeq H^0(M_v,A_v^K)`. The global evaluation is surjective, since the local relatively very ample descriptions already supply generators on each `U_i`. Dualized evaluation therefore defines a global holomorphic `j:M→P(E_K^ee)`. On each fiber its complete linear series is an embedding, because the local Veronese system is a subsystem of the complete series. Consequently `j` is injective and an immersion: its vertical differential is injective and the base component of `j` is `p`. It is proper, being over the proper `p`; a proper injective holomorphic immersion is a closed holomorphic embedding. Dual evaluation gives the displayed tautological identity. □

This proposition is conditional on the printed vanishing, Kodaira embedding, and Grauert base-change inputs. It **does not** independently establish these analytic theorems or their L²-based proofs.

## Explicit obstruction to replacing the global projective bundle by a product

**Proposition (sharp base-twist model).** Let `V` be an elliptic curve and let `F∈Pic^0(V)` be non-torsion. Put
[
M=mathbf P^1	imes V,quad p=operatorname{pr}_2,quad
A=operatorname{pr}_1^*mathcal O_{mathbf P^1}(1)otimesoperatorname{pr}_2^*F.
]
Then `A` admits a metric with positive curvature on each `P^1` fiber. **For no** `k>0` and `N≥0` does there exist a holomorphic map over `V`,
[
G:Mlongrightarrowmathbf P^N	imes V,qquad
A^ksimeq G^*operatorname{pr}_1^*mathcal O_{mathbf P^N}(1).
]
Thus the local product conclusion of Lemma 9.71.1 cannot simply be globalized, **even though the relevant global projective bundle is isomorphic as a projective-space bundle to a product**.

**Proof.** Any degree-zero line bundle on an elliptic curve admits a smooth flat unitary metric. Tensor this on `F` with the Fubini–Study metric of `O(1)` on `P^1`; the vertical curvature is strictly positive. Fix `x_0∈P^1` and restrict a hypothetical `G` to the holomorphic section `s(v)=(x_0,v)`. The claimed hyperplane identity becomes
[
F^ksimeq h^*mathcal O_{mathbf P^N}(1),
qquad h=operatorname{pr}_1circ Gcirc s:V	omathbf P^N.
]
The right-hand bundle is globally generated, hence possesses a nonzero global holomorphic section (choose a hyperplane section nonvanishing at one point of `h(V)`). In contrast, a nontrivial degree-zero line bundle on a compact Riemann surface has **no** nonzero holomorphic section: the zero divisor of such a section would be effective of degree zero, hence empty, trivializing the bundle. Non-torsion ensures `F^k` remains nontrivial for every `k>0`. Contradiction. □

For completeness, write `W_k=H^0(P^1,O(k))`, so
[
E_k=p_*A^k=W_kotimes F^k,qquad
mathbf P(E_k^ee)simeqmathbf P(W_k^ee)	imes V.
]
Under this **projective-space-bundle** isomorphism,
[
mathcal O_{mathbf P(E_k^ee)}(1)
simeqoperatorname{pr}_1^*mathcal O_{mathbf P(W_k^ee)}(1)
otimesoperatorname{pr}_2^*F^k.
]
The relative embedding `j=(v_k,mathrm{id}_V)` is the degree-`k` Veronese map fiberwise, and its tautological pullback is precisely `A^k`. The nontrivial `F^k` twist is the obstruction **in the tautological line-bundle normalization**, not in the underlying projective-space bundle.

## Audit verdict, dependencies and proposed documentation

- **No original theorem falsified.** Lemma 9.71.1 is local over `V`; the two propositions clarify its optimal global form.
- Affected dependents: a future argument replacing the local maps by a global `P^N×V` embedding *while retaining the exact equality `A^k=G^*O(1)`* would fail. Global arguments must keep `P(E_K^ee)` and its relative `O(1)` or explicitly track a base pullback twist. No presently printed dependent theorem was found to make this global claim.
- Proposed optional addendum after Lemma 9.71.1: state the compact-base relative-projective-bundle globalization and the elliptic flat-twist caution. **Do not** modify source, registry, canonicalization, statement tags, or `main` as part of this audit.
- The Grauert base-change theorem and the cited projective embedding/vanishing inputs remain **external or independently unverified internal inputs**. This report proves only the finite-cover/Veronese globalization and the elliptic countermodel conditional on those inputs.
- Scope: §9.71 selected proof-level mathematical reading; §9.72 adjacency/reference context only. **0 new first-visited numbered sections**, **0 completely certified sections**; the established current table of contents has **25 chapters and 747 sections**.
- The user-excluded Demailly approximation/regularization, dedicated Bergman, L², Ohsawa–Takegoshi, multiscale-atlas, and positivity-loss programme remains **deferred-by-user, not resolved or certified**. None of those proofs was reopened. No project build, test suite, GitHub Actions CI, formal verification, or website publication was run.
