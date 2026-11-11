# 2026-11-12 — classified mathematical finding

- **ID:** `POME-NPP-SNC-STRATIFIED-MASS-DEFECT-001`
- **Severity:** low
- **Status:** verified conditional deduction (no false theorem, no missing proof, no duplication)
- **Reviewed main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`
- **Location:** `docs/sections/non-pluripolar-products--capacity-convergence-and-loss-of-mass/index.html`, blob `d66813856cb813722806ab912afdfd4815d2da97`; Theorem 13.7.5 source `foundations-of-pluripotential-theory:AB4EBE3B`, permanent `67C4F7EC316E`, physical 106–135; Example 13.7.6 source `:D5678E03`, permanent `ACAEA8D8BE87`, physical 138–143. Dependencies: §13.5.1 permanent `06A36B9354A5`; §13.2.4 permanent `D79952D7E272`.
- **Hypotheses:** `P^n`, `n≥2`, `n` coordinate transverse hyperplanes, one factor `(1-λ_i)ω+λ_i[H_i]` per hyperplane, `λ_i∈[0,1]`; smooth decreasing `ω`-psh Hermitian-norm approximations.
- **Verified formula:** weak smooth wedge limit `Σ_S (∏_{i∈S}λ_i)(∏_{i∉S}(1-λ_i)) [H_S]∧ω^{n-|S|}`; singular NPP product equals `(∏_i(1-λ_i))ω^n`. Lost strata have total mass `1-∏(1-λ_i)`.
- **Complete justification:** positive smooth factors in `[ω]`, compactness of positive probability measures, vanishing of an individual factor in `C^∞` away from its hyperplane, invariance and uniqueness of normalized projective Haar measure on each transverse intersection. See [full proof](../reports/2026-11-12-npp-normal-crossing-stratified-weak-limit.md).
- **Previously filed distinct results:** `POME-NPP-PROJECTIVE-DIVISOR-PARTIAL-DEFECT-001` (same hyperplane), `POME-BT-HAUSDORFF-SUBFAMILY-SHARP-001` (all coefficients one, classical endpoint). Not a re-registration.
- **Affected dependents / proposed correction:** §13.7.5/.9 mass-conservation qualification; optional explanatory example only, **no theorem correction warranted**.
- **Coverage:** previously partly visited §13.7, with §§13.2 and 13.5 only crosschecked; **+0** first proof-level section visits and **+0** entire-section certificates. Excluded Demailly approximation/Bergman/L²/OT/multiscale/positivity-loss remains **deferred-by-user**. No full-theory validation or tests.
