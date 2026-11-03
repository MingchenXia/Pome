# Classified mathematical-audit ledger — 2026-11-03 — infinite divisorial trace rates

**Reviewed production main:** b6933b772f41b45918f7e25ed1afbbb1fd892272. **Audit branch:** review/mathematical-audit. **No source modification.**

| Finding ID | Severity / status | Exact target | Mathematical finding | Resolution / affected dependencies |
| --- | --- | --- | --- | --- |
| **POME-BDIV-INFINITE-DYADIC-TRACE-RATE-001** | **low / verified conditional deduction**; no false original theorem | Theorem 20.4.2, source **non-kahler-pluripotential-theory:E6DD8E29**, permanent **A67FA9DFB4BC**, main **docs/sections/divisorial-currents-on-compact-modifications/index.html**, blob **79d6e21f9d3784bf3761846f77f90ad075253644**, physical lines **35–82** | On the identity model \(\mathbf P^2\), the positive current \(T=\sum_{j\geq1}2^{-j}[L_j]\) has finite-level divisorial trace \(D_m=\sum_j\lfloor m2^{-j}\rfloor[L_j]/m\) and infinite limit \(S=T\). The exact \(\omega_{\mathrm{FS}}\)-mass error is \(e_{2^k}=2^{-k}=1/m\) but \(e_{2^k-1}=k/(2^k-1)=\log_2(m+1)/m\); the all-integer sequence is not monotone (the \(L_1\)-coefficient falls from \(1/2\) to \(2/5\) from \(m=4\) to \(m=5\)). Thus all-integer \(O(1/m)\) convergence cannot be inferred from the printed hypotheses. | **No repair needed:** the printed theorem promises convergence and increasingness **only for dyadic indices**, both verified in the model. Proposed *illustrative* post-theorem note; any future quantitative use in §§20.4.5/.15 requires a rate hypothesis. Neither dependent is refuted. |

**Context-only dependency:** Theorem 20.3.2, source non-kahler-pluripotential-theory:BF417B5C, permanent 7CD874C73EC9, main docs/sections/restriction-and-intrinsic-trace-data/index.html, blob dbc3b722ceacb8232fe4c7b711e5ad98b0708f06, physical lines 35–51. Its general proof chain, including excluded analytic approximants, was **not** reopened. The fixed-model divisor coefficients were derived directly from one-variable local integrability.

**Actual coverage:** new exact infinite-divisor multiplier-ideal/trace-mass test of Theorem 20.4.2, not a complete proof of §20.4 or a new whole-section certification. Previous §20.3 atomic-curve and §13.24 countable-current findings remain separate and unchanged. Do not promote the earlier selected §20.4.20/.26 work to full certification.

**Existing ledger retained:** prior confirmed errors, proof gaps, external dependencies, verified repairs, withdrawals and all Demailly approximation/regularization and dedicated Bergman, weighted \(L^2\), OT, multiscale-atlas, positivity-loss records remain unchanged, with the excluded subset **deferred-by-user**, neither resolved nor certified. No project build, CI, formalization or publication was performed.

[Full independently derived proof and limits](../reports/2026-11-03-infinite-line-trace-dyadic-logarithmic-rate.md).
