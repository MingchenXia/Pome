# 2026-11-06 — §21.9 Laurent and inverse-character proof-step ledger

Reviewed main b6933b772f41b45918f7e25ed1afbbb1fd892272; exact integrated HTML blob 7ad2e6dbdd0ce59e1bf08cd9cb3c046e8c87ff6c. [Detailed English proof](../reports/2026-11-06-toric-laurent-cauchy-and-action-inverse.md). Historical provenance remains foundations-of-pluripotential-theory; no canonical merges proposed.

| Stable finding ID | Severity | Status | Exact passage | Mathematical conclusion and required action |
| --- | --- | --- | --- | --- |
| POME-TORIC-LAURENT-ANNULAR-CAUCHY-001 | low | verified conditional deduction | §21.9.4; source D75B0BB2, permanent 00432B20A966; reading lines 112–136 | Direct \(n\)-variable polyannular Cauchy proof, sign-controlled inner boundary and \(3^nC_K\) normal convergence. Correct printed lemma; optional replacement if removing dependency on quoted one-variable Laurent theorem. Classical Cauchy formula remains a named elementary input. No proof gap claimed. |
| POME-TORIC-ACTION-INVERSE-INFERENCE-001 | low | confirmed error (*proof exposition only*) | §21.9.5; source BD98CC5B, permanent 69D3D97E7701; reading line 166, with definition line 156 | Invariance of \(s_0=\chi^{-v}s_v\) needs the action on \(\chi^{-v}\), not on \(\chi^v\). Replace this one explanatory clause in a **separately reviewable proposed patch**. Theorem, divisor sign and section-weight formula are correct; previous translation-weight audit remains distinct. |

Both findings are **audit-only**: no production or source edits. No prior error/proof-gap status is changed; all user-excluded regularization work remains deferred-by-user. Section 21.9 stays *partially audited*, not certified.
