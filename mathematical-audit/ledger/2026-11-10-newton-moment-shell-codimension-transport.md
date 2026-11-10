# Classified audit ledger — 2026-11-10 — Newton moment-shell transport

- **Stable ID:** `POME-NEWTON-SHELL-CODIM-TRANSPORT-001`
- **Status:** verified conditional deduction; **severity:** low.
- **Not a:** confirmed error, proof gap, genuine duplication, verified full repair, or external-dependency certification.
- **Reviewed production main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.
- **Exact main reading-edition file:** `docs/sections/partial-kernels-and-quotient-equilibrium--newton-selection-and-moment-shell-limits/index.html`; blob `65fe8b5b93df2243f35a45d139e4f6f7829a905a`.
- **Source anchors:** §18.45 source `non-kahler-pluripotential-theory:4CCEF308` / permanent `5CEF27CB9AAA`, lines 5–38. Lemma 18.45.3 `:7F9C5680` / `F0A638931204`, lines 52–87. Theorem 18.45.7 `:E068131C` / `2EC775894117`, lines 94–135. Theorem 18.45.11 `:45F963D6` / `C6669A63F760`, lines 144–164; Eq. 18.45.12 `:393C1130` / `BAC3E7E057E7`, lines 145–148. Example 18.45.14 `:9B9B702A` / `9600E351F18B`, lines 179–187. All abbreviated source labels have namespace `non-kahler-pluripotential-theory`.
- **Hypotheses:** rational compact `Q⊂int P`, affine lattice translate `b∈Z^n`, `0≤d=dim Q≤n`, torus-invariant smooth positive probability `ν`, smooth torus-invariant `w`, `D²F>0` everywhere, full selected monomial spaces `V_m`, fixed smooth distance on compact `X=(P¹)^n`.
- **Conclusion:** `Π_m=B_mν/N_m` converges to `Π=μ_Q/(d! vol_Λ Q)` in `W1` at `O(m^-1/2)`; for `d<n`, this order is **sharp** as a Wasserstein metric, with `W1≥c m^-1/2`. Uniform Gaussian fluctuations `sqrt(m)(r-r(q))⇒N(0,D²F(r(q))^-1)`.
- **Justification:** exact angular-orthogonal monomial probability, uniform coercive Laplace moments, uniform local Gaussian limit, Euclidean radial coupling plus `d`-dimensional lattice-cell `O(1/m)` comparison; normal-distance Lipschitz test on an interior piece of the shell yields the matching lower bound. [Full proof](../reports/2026-11-10-newton-moment-shell-codimension-transport.md).
- **Proposed correction/addition:** optional quantitative Remark after Theorem 18.45.11, not a repair; no source-body change.
- **Affected dependents:** quantitative Newton-shell normalized measure comparisons in §18.45, with the codimension distinction explicit; no extension to unrelated kernel families.
- **Unresolved:** proof chains of global envelope, non-pluripolar mass and other §§18.45 claims not independently certified. No original theorem declared false. Prior confirmed errors/gaps/external inputs unchanged.
- **Deferred by user:** entire Demailly approximation/regularization and its dedicated Bergman, L², Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof-completion plan remains **deferred-by-user**, not resolved.
- **Coverage:** §18.45 first selected proof-level visit; 1 new numbered-section visit, 0 whole-section certifications. ToC 25 chapters / 747 sections. Audit Markdown only; no production/source/registry/tags/canonicalization/build/CI/publication changes.
