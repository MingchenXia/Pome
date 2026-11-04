# Classified ledger — 2026-11-04 — intermediate Hessian cone scalar shift

| Stable finding ID | Severity | Status | Precise claim and scope | Correction / dependency impact |
| --- | --- | --- | --- | --- |
| `POME-HESS-CONE-SHIFT-ASYMPTOTIC-SHARP-001` | low | **verified conditional deduction** | For each `2 <= m <= n`, the positive spectrum `(L^(m-1),1^(n-m+1))`, `L>1`, has exact maximum scalar shift `t_*=1` while the printed `e_m = sigma_m/(m sigma_(m-1))=S_m/((n-m+1)S_(m-1))` tends to `1` as `L->infinity`. Thus there is no uniform multiplicative strengthening `C e_m`, `C>1`, of the cone shift, despite the strict finite-spectrum margin for `m>=2`. | Theorem/lemma statement and printed proof **correct**. Optional independently reviewable sharpness remark after Lemma 8.2.3; related iteration Lemma 8.2.4 and derivative Lemma 8.2.5 are not refuted or transitively certified. |

**Reviewed production main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.

**Primary reading anchor:** `docs/sections/complex-hessian-equations--the-admissible-cone/index.html`, main blob `925e6109ab7d800cde9bec4b0487842b2e6877a8`; Lemma **8.2.3**, source `non-kahler-pluripotential-theory:42B9BB86`, permanent `F86594126C69`, physical lines **43–74**. Downstream reading context: Lemma **8.2.4** source `:3E489B35` / tag `94C4E018DD25` lines **76–100**, Lemma **8.2.5** source `:53FFB5F3` / tag `7710D01DF6F5` lines **104–124**. Actual PDE scope §8.1 is `2<=m<n`; `m=n` is an expressly stated algebraic aside, not a PDE generalization.

[Full standalone argument and exact normalization](../reports/2026-11-04-hessian-uniform-cone-shift-sharpness.md).

**Classification preservation:** Earlier coefficient-derivative sharpness `POME-HESS-SHARP-DIAGONAL-DERIVATIVE-001` and all existing errors, proof gaps, external inputs, duplicates and repairs remain unchanged. Owner-excluded Demailly approximation/regularization, Bergman, weighted-`L^2`, OT, multiscale and positivity-loss proof programme is still **deferred-by-user**, not resolved or certified. This audit performs no software build, tests, CI, publication, source edits, formal verification, or full-section certificate.
