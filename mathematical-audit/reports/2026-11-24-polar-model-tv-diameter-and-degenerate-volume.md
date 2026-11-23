# 2026-11-24 — Polar-curvature metric diameter versus zero singularity volumes

**Reviewed `main` commit:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. **Audit branch starting head:** `5d2ac25683aed605b0edf3486c5478c24fa0cf19`.

**Status:** `POME-ZERO-VOLUME-POLAR-TV-SHARP-DIAMETER-001` — **low / verified conditional deduction**, not a false printed theorem, not a certified transitive proof chain. No new confirmed source error or missing-proof diagnosis is asserted.

## Exact integrated evidence and coverage

The following are current **integrated reading-edition** files, not inferred source-manuscript coordinates.

- **§18.13**, `docs/sections/multiplier-ideal-envelopes-and-goodness--a-topology-on-ordinary-singularity-types--countable-poles-and-all-obstacles/index.html`, blob `c43a70e953f433b61a2cda67e02c2c57a0448427`, physical lines **7–130**: countable poles, cutoff profiles, exponentially integrable sums, obstacle envelopes. Theorem **18.13.1**, source label `non-kahler-pluripotential-theory:B30A34DC`, permanent tag `6529F0A74D79`, lines 13–100; Proposition **18.13.4**, source label `non-kahler-pluripotential-theory:D2CE9F8B`, permanent tag `AB19DE43A7F6`, lines 101–130.
- **§18.14**, `docs/sections/multiplier-ideal-envelopes-and-goodness--a-topology-on-ordinary-singularity-types--relative-divisors-and-fiber-obstacles/index.html`, blob `1eedc79121fde5c31477c771648040f68769929b`, physical lines **7–452**: connected-fiber divisorial removal, extended-real fiber obstacle and compactness, multiplier-ideal cancellation, variable obstacles, ramified example, disconnected-fiber counterexample, finite covering correction. Proposition **18.14.1**, source label `non-kahler-pluripotential-theory:2CF04C42`, permanent tag `1195E1B9B18D`, lines 31–98; Corollary **18.14.10**, source `non-kahler-pluripotential-theory:88162FB7`, permanent tag `20390B807B79`, lines 401–452.
- **§18.15**, `docs/sections/multiplier-ideal-envelopes-and-goodness--a-topology-on-ordinary-singularity-types--divisorial-products-and-zero-volume/index.html`, blob `203607fc492e0027cbfd8f71d64ec6c0b3c57bf3`, physical lines **7–278**: product-envelope reduction, zero-volume examples, polar-curvature metric, nonclosed and semipositive backgrounds. Definition **18.15.6–7**, source `non-kahler-pluripotential-theory:8A7CC477`, permanent tag `F217B40D9074`, lines 133–143; Proposition **18.15.8**, source `non-kahler-pluripotential-theory:4766BD27`, permanent tag `6DEB26AFE67E`, lines 146–182; Corollaries **18.15.9–10**, labels `non-kahler-pluripotential-theory:A4881E6B`, `non-kahler-pluripotential-theory:FE33610B`, permanent tags `DFCE5415EAB5`, `13B4DE048053`, lines 189–278.

The independent argument below uses the exact definition of the metric in §18.15.6–8 and the product isometry and zero-volume results there. General compact-curve existence invokes the identified earlier curve classification **§13.28.1**; the explicit projective-line case is computed without that classification. Upstream dependencies (including §§13.28, 18.14, and the general theory of extended products) are **not** thereby certified.

## New consequence: sharp diameter and nonseparable analytic models

Let `C` be a connected compact complex curve carrying a smooth positive `(1,1)`-form `eta`, let `A=∫_C eta>0`, and use the product model locus `S_Psi` in Proposition 18.15.8. Its metric is

```tex
\rho_\Psi(\Phi(q),\Phi(r))=
  \|\mu_q-\mu_r\|_{\mathrm{TV}},\qquad
\mu_q=\mathbf 1_{\{q=-\infty\}}(\eta+dd^c q).
```

Since every positive polar-curvature measure has mass at most `A`, the triangle inequality yields `rho_Psi≤2A`. **Equality is attained.** For any `x∈C`, let `q_x` be the normalized Green potential satisfying

```tex
\eta+dd^c q_x=A\,\delta_x,\qquad\sup_C q_x=0.
```

Existence is the ordinary Green/Poisson solution on a compact curve (also supplied by the model classification of §13.28.1). To check that it is itself an ordinary model, take an ordinary competitor `v≤0` with `v≤q_x+O(1)`. On `C\setminus\{x\}`, `dd^c(v-q_x)=eta+dd^c v≥0`. The difference is bounded above near `x`, so the removable-singularity theorem extends it as a subharmonic function to `C`. It must be constant, and that constant is at most zero at a point where `q_x=0` (since `v≤0`). Thus `v≤q_x` and `P_eta[q_x]=q_x`. Its polar curvature is exactly `A delta_x`.

For distinct `x,y`, the two Dirac measures are mutually singular, and therefore

```tex
\boxed{\rho_\Psi(\Phi(q_x),\Phi(q_y))=2A},
\qquad
\boxed{\operatorname{diam}(\mathcal S_\Psi,\rho_\Psi)=2A}.
```

The uncountable set indexed by `x∈C` is pairwise `2A`-separated, so the complete geodesic metric space `S_Psi`, and its ideal-model subspace, are **nonseparable** and **not totally bounded**, even though their upper-volume pseudometric `d_Theta` is **identically zero** by Proposition 18.15.8. This is a quantitative structure of the *specified* polar-curvature metric, not a statement about every singularity topology.

For a completely explicit **analytic-singularity** realization, take `C=P^1`, `eta=sigma` the probability Fubini–Study form (`A=1`), and for `x=[x_0:x_1]` put, for `z=[z_0:z_1]`,

```tex
q_x(z)=\log\frac{|z_0x_1-z_1x_0|^2}
 {(|z_0|^2+|z_1|^2)(|x_0|^2+|x_1|^2)}.
```

With Pome's `dd^c=i/(2pi)∂bar∂` convention, Poincaré–Lelong gives `sigma+dd^c q_x=delta_x` and `sup q_x=0`; the logarithmic pole coefficient is exactly one. Take `Z=P^k` with its hyperplane log potential `Psi` and let `a_x=Psi+q_x∘p` on `M=P^1×P^k`. These are normalized ordinary **and ideal** models with **analytic singularities**. They satisfy simultaneously

```tex
x\ne y\Longrightarrow\rho_\Psi(a_x,a_y)=2,\qquad
d_\Theta(a_x,a_y)=0.
```

Furthermore, `x_j→x` implies `q_{x_j}→q_x` in `L^1(P^1)`: select unitary transformations `U_j→I` with `U_jx=x_j`; then `q_{x_j}=q_x∘U_j^{-1}`, and the action of near-identity smooth isometries is strongly continuous on `L^1`. Fiber integration therefore yields `a_{x_j}→a_x` in `L^1(M)` for every smooth positive volume form, while **`rho_Psi(a_{x_j},a_x)=2` for every distinct `x_j`**. In particular, the printed implication `rho→0 ⇒ L^1→0` is strict and has no converse.

Corollaries 18.15.9–10 put the **same functions and same polar metric** on the nonclosed positive backgrounds (nonconstant `f>0`) and semipositive backgrounds `f≥0`, including `f=0` with non-big `Theta_0`; hence the same `2`-separated analytic family, nonseparability, `L^1`/metric nonconverse, and zero upper-volume pseudometric persist in those explicitly stated backgrounds. **No assertion** is made that all Gauduchon or all nonclosed backgrounds have these properties.

## Cross-checks, qualifications and dependencies

- The **coefficient is `2A`**, not `A`: Pome uses the total-variation *norm* `||delta_x-delta_y||_TV=2` for distinct points, not the probabilistic half-TV distance.
- The Green pole is a legitimate `eta`-psh model even when its entire curvature mass is atomic; the proof above verifies its model property, rather than assuming every `eta`-psh potential is a model.
- The uncountable separation in this **polar-curvature total-variation metric** is distinct from the earlier registered `POME-TRACE-MOVING-ATOMS-NONSEPARABLE-L1-001` about trace singularity metrics. This report adds the **sharp diameter and an explicit all-analytic zero-volume family** and does not re-register the earlier result.
- §18.13's Jensen exponential-integrability argument and §18.14's connected-fiber descent, the extended-real obstacle cap, and the explicit ramification and disconnected-fiber examples were directly checked in the present edition; no new printed error or proof gap was confirmed from those checks. This **does not** constitute a complete certification of any transitive analytic dependency.
- User-excluded Demailly approximation/regularization, dedicated Bergman, L², Ohsawa–Takegoshi, multiscale atlas and positivity-loss programmes were **not** inspected or continued; existing notes remain **deferred-by-user**, neither solved nor certified.

## Proposed placement and affected dependents

Optionally add this as a *separately reviewable proposed remark* immediately after Proposition 18.15.8, with the `P^1` explicit construction and a note that `d_Theta` fails to detect a nonseparable, finite-diameter family. Relevant downstream examples are Corollaries 18.15.9–10. No body, canonical registry, permanent tag, published page, source repository, or main edit is authorized or performed in this audit.

**This run:** 3 entire current mathematical sections read directly (18.13, 18.14, 18.15); 1 new low conditional deduction; 0 new confirmed false printed theorems, 0 new documented proof gaps, 0 complete upstream-chain certificates. No build, tests, GitHub Actions, or website publication.
