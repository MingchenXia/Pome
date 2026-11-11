# 2026-11-11 — relative projectivity, global tautological twist

- **ID:** `POME-RELPROJ-FLAT-TWIST-GLOBAL-TAUTOLOGY-001`
- **Severity / status:** **low / verified conditional deduction** (not a printed error, not a proof-gap classification of Lemma 9.71.1).
- **Reviewed production main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.
- **Exact source:** `docs/sections/local-projectivity-from-relative-positivity/index.html`, blob `f17614b598855bda6fc15f266135d6fe238638cf`; §9.71 section tag `045F6241DBBD`; Lemma 9.71.1 original `cao-paun-foliations:4BE67CB0` / permanent `A53CEC220C70`; physical lines **8–13**, **18–36**.
- **Finding:** On compact base `V` the printed relative-positive local lemma globalizes to an embedding into `P((p_*A^K)^∨)`, not necessarily into a fixed `P^N×V` carrying the *un-twisted* hyperplane bundle. For `M=P^1×V`, non-torsion `F∈Pic^0(V)`, and `A=O_{P^1}(1)⊠F`, the latter stronger globalization is impossible for all powers, although `P((p_*A^k)^∨)` is itself a product. The missing factor in its relative tautological `O(1)` is `p_V^*F^k`.
- **Proof and precise scope:** [full argument](../reports/2026-11-11-relative-projectivity-flat-twist-tautological-obstruction.md). Compact base proof uses finite locally relatively-very-ample covers, a common Veronese power, the printed uniform vertical vanishing and Grauert base change; obstruction restricts to any constant `P^1` section and uses `H^0(V,F^k)=0`.
- **Proposed correction:** **No correction required to Lemma 9.71.1.** Optional addendum after it; any future global application must retain the relative projective bundle and `O(1)` or a base twist. §9.72 was consulted only for context; no dependent theorem is judged erroneous.
- **Unverified upstream inputs:** printed Grauert1960 base change and Kodaira/vanishing theorems. These were not reproved; the conclusion is a verified conditional deduction.
- **Coverage delta:** §9.71 had an earlier selected proof visit, so **0 first visits / 0 whole-section certifications**, ToC **25/747**.
- **Deferred-by-user:** all Demailly regularization and dedicated Bergman/L²/OT/multiscale/positivity-loss programmes stay deferred, not resolved. No builds, CI, source or site changes.
