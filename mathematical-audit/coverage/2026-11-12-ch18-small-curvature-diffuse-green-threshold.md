# 2026-11-12 — Exact proof-level coverage: §18.27

**Production main:** b6933b772f41b45918f7e25ed1afbbb1fd892272. **Reading edition:** docs/sections/multiplier-ideal-envelopes-and-goodness--small-curvature-and-strict-ordinary-types/index.html (blob a6e3cc7cb9c6931688e089bb67b2ed12766f6a0b). **Current ToC:** 25 chapters / 747 numbered sections.

| Current section/tag | Level reached in this run | Retained boundary |
| --- | --- | --- |
| §18.27 equation 18.27.1, 4A552AB10BA9; lines 9–14 | Verified explicit unbounded quasi-psh example with ordinary-equivalent tail truncations and curvature errors tending to zero | General class of all small-curvature types not certified |
| §18.27 Lemma 18.27.2, 96F4F5465740; lines 17–45 | Checked the conclusion concretely: Lelong zero and zero first-Hessian polar mass despite unbounded poles; direct Green/current calculation | General compact-modification pullback and Gauduchon trace proof not certified |
| §18.27 Lemma 18.27.3, E5C4A193363D; lines 48–64 | **Dependency recorded only**; line 55 invokes excluded current regularization | **deferred-by-user**, never resolved or implied by the example |
| §18.27 Theorem 18.27.4, 0E6CABEB995A; lines 75–95 | Both directions established directly for θ=aω_FS and arbitrary finite real point divisor Δ on P¹ with explicit diffuse unbounded residual | Full theorem remains conditional on other internal inputs, including excluded .3 |

**Increment:** §18.27 already had selected proof-level coverage (POME-IDEAL-SMALL-CURV-LATTICE-001); **+0 first-visited numbered sections, +0 entire-section mathematical certifications**. Other 746 numbered sections were *not* checked in this run. The new finding is [POME-IDEAL-SMALLCURV-DIFFUSE-GREEN-THRESHOLD-001](../reports/2026-11-12-small-curvature-diffuse-green-multipole-threshold.md), low / verified conditional deduction, and is distinct from the prior lattice-closure audit. Dedicated Demailly regularization/Bergman/L²/OT/multiscale/positivity-loss programme remains deferred-by-user, not audited.
