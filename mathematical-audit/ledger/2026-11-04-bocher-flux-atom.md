# 2026-11-04 incremental classified ledger — Bôcher flux

**Reviewed main:** b6933b772f41b45918f7e25ed1afbbb1fd892272. **Reading-edition blob:** 75e982788e627af602981823a82863cbd36ee712.

| Stable finding ID | Severity | Status | Precisely reviewed content | Result | Suggested action |
| --- | --- | --- | --- | --- | --- |
| POME-HARM-BOCHER-FLUX-ATOM-001 | low | **verified conditional deduction** | Lemma 3.3.16, source classical-potential-theory:6C6775C3, permanent B0CFE200676D, docs/sections/classical-harmonic-analysis/index.html lines 217–226 | The printed decomposition is correct. Independent spherical-mean/Harnack/Green-identity calculation gives \(-\Delta h=\kappa_d c\delta_a\), \(c=-\kappa_d^{-1}\int_{S_r}\partial_\nu h\), and the exact limiting spherical-average coefficients. | Optional flux/atom corollary; preserve theorem/proof/attribution. |

**Evidence:** [Full proof](../reports/2026-11-04-bocher-flux-and-distributional-atom.md). Internal analytic inputs: Theorem 3.1.7 and (3.1.8) (permanent A60BA3B2DBFC / D63569C18649), Proposition 3.1.19 (DAC835A39525), Weyl's lemma Theorem 3.1.11 (C9127FBA9AE8), all at main file docs/sections/harmonic-functions-and-the-dirichlet-problem/index.html, blob fc02188d6e246a21aa07acd8bf6d3712761ba6e5. Exact dependency proofs not recertified.

**Coverage/state accounting:** One newly checked lemma and an independent flux calculation in previously partly checked §3.3. No complete mathematical-section certification. Current ToC inventory remains 25 chapters / 747 numbered sections / zero completely certified sections. Existing confirmed errors, proof gaps, candidates, genuine duplications, external dependencies, verified repairs, and previously resolved items are **not reclassified** by this increment. All Demailly approximation/regularization and dedicated Bergman, L², OT, multiscale-atlas and positivity-loss programme entries remain **deferred-by-user**, not resolved/certified. No source/body/registry/tag/main/CI/build/site modification.
