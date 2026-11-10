# 2026-11-11 classified ledger entry

- **Stable ID:** POME-NPP-MASS-ROOT-POWER-SHARPNESS-001
- **Severity/status:** low / verified conditional deduction. **No false published theorem is alleged.**
- **Reviewed main:** b6933b772f41b45918f7e25ed1afbbb1fd892272.
- **Result:** Sharp concavity \(M((1-t)u_0+tu_1)^{1/n}\ge(1-t)M(u_0)^{1/n}+tM(u_1)^{1/n}\) for global non-pluripolar top mass on connected compact Kähler manifolds, \(n\ge1\), including zero masses; \(\alpha>1/n\) fails along a strictly positive-mass hyperplane segment on \(\mathbb P^n\). Root mass is concave for positive model test curves and continuous to their left endpoint.
- **Full proof, strict-sharpness countermodel, and anchors:** [report](../reports/2026-11-11-npp-sharp-root-mass-concavity-and-test-curves.md); Theorem 13.13.5, source **sgpt:5DEDC013** / permanent **7F7BE8292E76**, §13.13 lines **50–59**, blob **4ace6181d3767e6d5ac3a681c36e392e33b717a2**; Proposition 13.11.4, **sgpt:B86D7001 / 9E81D36B1290**, §13.11 lines **79–93**, blob **054a7661c855824b86eb749e211fc3da88a599de**; Proposition 17.12.9, **sgpt:37ECD68D / B7CD1B90CFDA**, §17.12 lines **133–144**, blob **6dfdfc2b5e599eb3a19a9558a9c963e79df71dc7**.
- **Genuine external dependency:** DDNL19log proof of Theorem 13.13.5's mixed-mass inequality; independently **unverified**, and not part of the excluded Demailly approximation programme. Internal mass multilinearity, monotonicity and test-curve positive-mass results have been used selectively, **not fully certified**.
- **Correction/affected dependents:** Propose an optional corollary and sharpness example after Theorem 13.13.5 plus a cross-reference in §17.12.9. Nothing patched in source; downstream §§17.12–17.18 only conditionally affected. Distinct from earlier Dirichlet root concavity.
- **Coverage:** 0 first proof-level section visits, 0 whole-section certifications, actual current ToC 25/747.
- **Unchanged deferred status:** Demailly approximation/regularization, dedicated Bergman/L²/OT/multiscale/positivity-loss programme remains **deferred-by-user, not resolved**. No main/source/registry/tags/tests/build/CI/site changes.
