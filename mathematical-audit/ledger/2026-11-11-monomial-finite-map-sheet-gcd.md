# Classified audit finding — 2026-11-11 — monomial finite-map sheet degree

| Field | Value |
| --- | --- |
| Stable ID | `POME-CYCLE-MONOMIAL-FINITE-MAP-GCD-001` |
| Severity | **low** |
| Status | **verified conditional deduction** |
| Reviewed main | `b6933b772f41b45918f7e25ed1afbbb1fd892272` |
| Integrated blob | `docs/sections/divisors-and-logarithmic-limits-on-analytic-cycles/index.html` @ `dae567406b2030e550664ca57b1fe77911d956d4` |
| Exact anchor | Lemma 20.5.3 source `demailly-complex-geometry:FF68839A`, permanent `323D5DA3E240`, lines 27–59; Theorem 20.5.5 source `:D58680EB`, permanent `F1C928146DBC`, lines 64–127; Example .11 permanent `FF4839E28893`, line 155 |
| Hypotheses | (gcd(p,q)=1), (p,q,m,n\in\mathbb Z_{>0}), finite proper (F(x,y)=(x^m,y^n)), irreducible (D={y^p=x^q}) |
| Verified conclusions | (F_*[D]=gcd(pm,qn)[B]); (F^*[B]=\sum_{zeta^{mn/d}=1}[y^p=zeta x^q]), each summand maps with degree (d); (F_*F^*[B]=mn[B]); local divisor order (pma+qnb=d(Pa+Qb)). |
| Dependencies | Internal §20.5.3 proper image/current pushforward and §20.5.5 normalized Poincaré–Lelong for analytic cycles; these general theorems **not** independently certified. Algebraic degree/factorization independently proved. |
| Proposed correction | **None to source:** printed generic-sheet result is correct. Guard against replacing the individual restricted degree (d) by ambient degree (mn). |
| Affected/nearby | §§20.4, 20.6 and 20.8 cycle/pushforward normalization; no downstream theorem newly shown false. |
| Overlap | 2026-11-01 two *distinct* singular curve intersection and 2026-11-08 moving-divisor collision retained unchanged; not counted as new. |
| Full proof | [2026-11-11 monomial finite-map gcd](../reports/2026-11-11-monomial-finite-map-curve-sheet-gcd.md) |
| Coverage | [Precise visited anchors](../coverage/2026-11-11-ch20-monomial-finite-map-sheet-gcd.md); +0 first-visited sections, +0 complete certifications. |
| Deferred | Demailly regularization and dedicated Bergman/L²/OT/multiscale/positivity-loss **deferred-by-user**, no status change. |
