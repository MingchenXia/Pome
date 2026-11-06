# Status ledger — 2026-11-06 — §22.1.109 minimax

**Stable finding:** POME-NA-ORDERED-NET-LEGENDRE-MINIMAX-001. **Severity:** low. **Status:** verified repair of a specific printed proof step, **not** a false theorem or entire-proof certification. **Reviewed main:** b6933b772f41b45918f7e25ed1afbbb1fd892272.

Proposition 22.1.109 (source sgpt:0D711EA7, permanent 9F673331DE01) at docs/sections/non-archimedean-pluripotential-theory/index.html, main blob 8448d710690ebe1cc28040f9611d05c9d008a961, physical lines 1618–1674, invokes convex-duality Proposition 21.11.36 at line 1673 for equation (22.1.110) (source sgpt:67271763 / permanent 115AEB4414B4). The cited identity includes closure, and the individual Legendre domains have varying maxima. A direct [finite-grid arbitrary-net proof](../reports/2026-11-06-na-ordered-net-legendre-minimax.md) verifies the exchange using the **decreasing parameter direction** in Definition 17.12.1 and verifies the sharp endpoint bound B_i <= A_i+(a_i-a). An affine countermodel shows why the parameter monotonicity is essential.

**Confirmed as repaired:** this last minimax/endpoint step only. **Open/uncertified:** earlier mass/d_S and valuation-limit premises in §22.1.109 lines 1641–1656, its entire conclusion, and downstream §22.1.111 and §22.1.113. No new theorem counterexample. Previous confirmed errors and proof gaps stay in their earlier classifications, including the unrelated §22.1 concave-envelope issue.

**Deferred-by-user, not resolved:** Demailly regularization and the dedicated Bergman/weighted-L2/OT/multiscale/positivity-loss programme. Source/body/registry/tag edits not performed.
