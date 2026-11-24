# Fiber-normalized polar traces for arbitrary Hermitian metrics; product-model review

Date: 2026-11-25. Reviewed main: `b6933b772f41b45918f7e25ed1afbbb1fd892272`. Audit branch starting head: `b1ab131276761565eed7b6ee70515ecd8998bf51`.

## POME-CURVE-FIBER-NORMALIZED-HERMITIAN-TRACE-001

Severity: low. Status: verified conditional deduction, **not** a false printed theorem, nor a complete upstream proof certificate. The Gauduchon hypothesis in the printed lemma is used to make the fiber mass constant. It is not needed for a fiberwise normalized trace isometry.

Primary anchor: `docs/sections/multiplier-ideal-envelopes-and-goodness--a-topology-on-ordinary-singularity-types--models-over-a-curve/index.html`, blob `5eda7a473def5f1a58bd23c4d2a1a88e4b52313c`, lines 46–81 (Lemma 18.22.2, source non-kahler-pluripotential-theory:36C4D938 / permanent 4A14B90776C1), lines 85–124 (Proposition 18.22.3, source FA6BA0A7 / permanent AD848996B76C). Lemma 18.22.1 at lines 20–42, source 1C54E58D / permanent 717F85615B2A. The global connected compact convention is respected.

### Statement

Keep the surjective holomorphic map p:X→C with connected fibers, X smooth compact connected of dimension n≥2, C a compact connected Riemann surface. Let H be **any** smooth Hermitian metric on X, not necessarily Gauduchon. Put F_s=p^{-1}(s) as an effective divisor with multiplicities, and define the positive measure K_s=[F_s]∧H^{n-1}, and k(s)=K_s(X).

Then s↦K_s is weakly continuous, k is positive continuous with positive minimum, and for every finite real signed Borel measure μ on C,
```
L_H(μ)=p^*μ∧H^{n-1} = ∫_C K_s dμ(s)  (weak integral),
p_*L_H(μ)=k μ,
L_H(1_B μ)=1_{p^{-1}(B)}L_H(μ),
|L_H(μ)|=L_H(|μ|).
```
In particular the TV norm is ∫ k d|μ|. The normalized kernel N_s=K_s/k(s) is a continuous probability kernel supported on the corresponding fiber. The operator J_H(μ)=(1/(k∘p))L_H(μ) preserves total variation exactly and p_*J_H(μ)=μ. It is continuous for the weak topology of signed measures, **including nets**; no sequential compactness of arbitrary signed nets is used.

For the pullback model space of 18.22.3 replace its constant-normalized distance by
```
d_H(U,V)=∫_X (k∘p)^{-1} d|λ_U^H−λ_V^H|,
λ_U^H=1_{U=−∞}(θ+dd^c U)∧H^{n-1}.
```
Then d_H(U,V)=||μ_v−μ_w||_TV, independently of H. Thus all the metric conclusions of 18.22.3 remain unchanged. The unweighted trace distances for two fixed smooth Hermitian forms are even bi-Lipschitz comparable on this particular pullback locus via the extrema of the ratio of their fiber masses.

### Proof

Use the positive-measure Green solution construction at lines 46–58, and the proof of 18.22.2 at lines 74–76 **before** taking a pushforward. For positive probability measures μ_j→μ weakly on C, their mean-zero Green potentials have a uniform lower curvature bound −η. Normalized compactness bounds their suprema and yields L¹ precompactness, and uniqueness of the mean-zero Poisson solution identifies every subsequential limit. Thus the whole sequence converges in L¹(C). The pullback L¹ lemma (5.43.10, source DA81C6B2 / permanent 633794C1EFC2, `docs/sections/plurisubharmonic-functions-and-singularities--pullback-and-descent/index.html`, blob e5cccf608a51dd1629374fc68a1d3d7e6fd15958, lines 175–184) gives L¹(X) convergence. Taking dd^c and pairing with smooth test forms gives weak current convergence p^*μ_j→p^*μ. This part of the argument does not require H to be Gauduchon.

Apply to δ_{s_j}→δ_s, using the Poincaré–Lelong identification p^*δ_s=[F_s] at line 80, with all multiplicities retained. Wedge with H^{n-1}. The resulting positive measures converge on smooth functions, and their masses converge (test 1). Uniform approximation of continuous functions by smooth ones then proves weak convergence on all continuous functions. Since C is metrizable, this sequential argument proves continuity of s↦∫f dK_s for each f∈C(X); it is not an inference about sequential compactness of a measure net. Every F_s is a nonempty divisor, so k(s)>0 by strict positivity of H on its regular locus. Compactness gives 0<min k≤max k<∞.

For positive finite μ of nonzero mass approximate μ/m by finite positive atomic probabilities converging weakly (e.g. partition C into Borel sets of diameter ≤1/j and select one point per nonempty cell, retaining its mass). The preceding L¹ argument applies, after rescaling, to their pullbacks and traces. For each continuous f the atomic identity passes to the limit against the continuous function s↦∫f dK_s. This proves the asserted weak integral for positive μ, hence for signed μ by linearity. The zero measure case is immediate. The kernel is Borel: by monotone approximation of open-set indicators by continuous functions and a monotone-class argument, s↦K_s(E) is measurable for Borel E. Consequently the weak identity extends to bounded Borel tests, by uniqueness of finite measures and the same monotone-class argument.

Because K_s is carried by p^{-1}(s), its pushforward equals k(s)δ_s. This proves the pushforward and restriction identities directly, for every Borel B. Jordan carriers of μ^+ and μ^- pull back to disjoint Borel carriers, proving the absolute-variation identity. Division by k∘p is bounded and on each fiber equals division by k(s). Thus J_H has kernel N_s and preserves TV and pushforward. For any weakly convergent signed net μ_i→μ, testing J_H against f∈C(X) amounts exactly to testing μ_i against the fixed continuous function s↦∫f dN_s. This proves net continuity without any bound on the norms of the net.

Apply the restriction formula with B={v=−∞}, to the curvature T_v of the descended potential v. It yields λ_U^H=L_H(μ_v). By linearity and the normalized TV equality this gives the asserted metric formula; use 18.22.3 for the existing curve classification and metric geometry. For H_1,H_2, the unweighted distances equal ∫k_j d|μ_v−μ_w|; bound their ratio between min_C(k_2/k_1) and max_C(k_2/k_1).

### Necessity of variable normalization

Let X=C×F for a compact connected complex (n−1)-fold F with a Hermitian metric ω_F, p the first projection, and choose a smooth positive area form η on C. For any nonconstant positive smooth h on C put H=p^*η+(h∘p)pr_F^*ω_F. Then k(s)=h(s)^{n−1}∫_F ω_F^{n−1}, nonconstant. The unnormalized trace of δ_s has this mass, so no single scalar can give the TV isometry for every signed measure. This is not a counterexample to the printed Gauduchon lemma. In fact the printed proof correctly obtains constant k from dd^c H^{n−1}=0.

Dependencies: normalized compactness, mean-zero Green solution and its uniqueness, pullback L¹ continuity, Poincaré–Lelong, and the curve model classification in 13.29.1. These remain explicit inputs; their complete chains are not certified. Proposed addition after 18.22.2 or 18.22.3, not a replacement of the Gauduchon version. Affected downstream: 18.22.3 and its metric formulation; 18.22.4's envelope criterion is unchanged. No claim about arbitrary higher-dimensional base maps or non-pullback model loci.

## Actual coverage and checks

All paths below under `docs/sections/multiplier-ideal-envelopes-and-goodness--a-topology-on-ordinary-singularity-types--` followed by the listed slug and `/index.html`.

- §18.19 `equality-below-all-obstacles-on-separated-products` (blob 210f78503d542610158a162e3d9aa670c317e97b, math lines 7–96), whole direct. Lemma 18.19.1 D5E145AE/AFE454C19DE7: the slice argument uses a point at which the stretching competitor and all coordinate potentials are finite; the adjusted competitor has the sign −bc_j+(b−1)d_j, correct. Convex inequalities at poles avoid subtracting infinities. Proposition 18.19.2 C2A5E634/36E07E6B83DA: zero normalization and independence of coordinates recover each equality. Corollary 18.19.3 62E5083B/9E4426687FC0: taking the maximum with a low translate does not remove the ordinary upper singularity bound; the slice is not identically −∞. The argument gives equality below mixed obstacles, not a coordinatewise formula for them. Relative-envelope, divisor reduction, and all-weight ideal inputs retained.
- §18.20 `auxiliary-compact-complex-factors` (blob f1b6f67c60fe76ec140541127caf1203fea7ff7f, lines 7–109), whole direct. Lemma 18.20.1 99435545/F61F12847624: semipositive form vanishing on horizontal slices annihilates mixed components by positivity, so ordinary restriction is legitimate. The countable divisorial sum has finite mass, by the fixed product metric and finite curve masses; the ideal implication uses 5.38.5, not certified here. Proposition 18.20.2 B1DF5EB4/85AC8B179E4B: analytic singularity equivalence under restriction and pullback; L¹ comparison by product integration is independent of α. Corollary 18.20.3 0CCF8E3F/1B6E50A3B70B: addition of convex stretching competitors is valid including poles. Corollary 18.20.4 9C6B848E/47BA03C63283: the test form at line 99 is closed by top degree on T, and has the necessary positive pairing against a product metric; its background pairing vanishes for zero curve area. Smooth gauge proves sufficiency when the transverse form is strictly positive. The statement does not claim necessity of this strict positivity for general α.
- §18.21 `a-polar-metric-in-a-background-with-unbounded-mass` (blob 6b792da459c824cdf1aa665b07965695b4d28e98, lines 7–48), whole direct. Example C569F5CB/00A4B8521863: the factor 120=6!/3! is correct, mixed smooth terms are positive, and the lower estimate uses min h>0. The nonclosedness follows from the independent Y/T bidegree in the exterior derivative. The distance 1 is the TV norm of a single unit atom. Hopf unbounded-mass input 23.1.1 retained, not re-proved.
- §18.22 `models-over-a-curve` (blob 5eda7a473def5f1a58bd23c4d2a1a88e4b52313c, lines 7–140), whole direct. The local rank-one smooth decreasing approximation in 18.22.1 is elementary one-variable convolution, not the excluded Demailly programme. No change to that programme. Critical values do not affect the Poincaré–Lelong multiplicities or the Borel carrier argument. Corollary 18.22.4 source 81459FC5/permanent DFA6018C6C86: descent and surjectivity transfer the convex inequality for each b≥1; the smooth-obstacle conclusion depends on 18.12.2. No new printed errors found.
- §5.43.10 lines 175–184, selected dependency recheck only; its proof uses L¹ compactness and the finite critical-value set, not regularization.

Four whole current direct sections, one selected dependency; historical first visits not asserted. One conditional deduction, zero newly confirmed errors, zero new demonstrated proof gaps, zero complete transitive certificates. All explicitly excluded Demailly/Bergman/L²/OT/multiscale/positivity-loss programmes remain deferred-by-user, not resolved. No production source, registry, tags, main or website edits. No builds, tests or CI run.
