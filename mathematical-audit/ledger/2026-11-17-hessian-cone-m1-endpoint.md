# Finding ledger — 2026-11-17 — admissible cone m=1 boundary

| ID | Section/source | Severity | Status | Correction | Affected dependencies |
|---|---|---|---|---|---|
| `POME-HESS-CONE-M1-TRACE-BOUND-FALSE-001` | §8.2 Lemma 8.2.5, `non-kahler-pluripotential-theory:53FFB5F3`, tag `7710D01DF6F5`, physical lines 113–133 of `docs/sections/complex-hessian-equations--the-admissible-cone/index.html` | medium | **confirmed error** (third displayed inequality at m=1, n>=2) | Restrict `|M_{1\\bar1}|<=tr M` to `m>=2` (or PSD M). Keep two coefficient inequalities unchanged. Proposed only. | §8.4.2 cited use safely assumes m>=2; §8.5 cited use invokes first coefficient bound and is unaffected. Other users not exhaustively checked. |

Reviewed main `b6933b772f41b45918f7e25ed1afbbb1fd892272`; integrated blob `925e6109ab7d800cde9bec4b0487842b2e6877a8`. Direct counterexample `n=2,m=1,M=diag(2,-1)` has `S_1=1>0` but `|M_{11}|=2>tr M=1` and `S_2=-2`. [Full anchored report](../reports/2026-11-17-hessian-cone-m1-endpoint-false-trace-bound.md).

Distinct from earlier `POME-HESS-SHARP-DIAGONAL-DERIVATIVE-001`, which addresses only a sharper **correct** lower bound on `F_i` for `m>=2`. Demailly and all dedicated excluded programmes: **deferred-by-user**.
