# 2026-11-22 — independent signed mollifier scales

## POME-BT-SIGNED-INDEPENDENT-MOLLIFIER-SCALES-001

- **Severity/status:** low / **verified conditional deduction**, not a false theorem or repaired missing proof.
- **Reviewed main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.
- **Exact source:** `docs/sections/generalized-products-and-their-associated-bounded-products/index.html`, main blob `ccdb1ff3375fa102c90f78bd97dd4c6a26ae6ed9`; Theorem **7.26.3** source `klimek-pluripotential-theory:77522B43` / permanent `5C50A7C32E5B`, physical lines 105–137; Lemma **7.26.2** source `8C5E7ECD` / permanent `8DF858D7EC52`, lines 73–103.
- **Claim:** for locally bounded PSH `u_j`, each factor may be mollified by its *own* real signed integral-one test kernel and its *own* scale `ε_j(t)→0` without relative-rate assumptions; their mixed smooth `dd^c` wedge converges weakly to the classical mixed Bedford–Taylor product.
- **Proof:** individually split each signed unit-mass kernel into the difference of two positive unit-mass kernels with coefficients `a_j^±` satisfying `a_j^+−a_j^−=1`; use Lemma 7.26.2 on each positive mollification and bounded mixed BT continuity in capacity for all `2^k` terms; sum coefficients `∏_j(a_j^+−a_j^−)=1`. Details in [report](../reports/2026-11-22-independent-signed-mollifiers-and-green-hyperconvexity.md).
- **Limits:** no positive current claimed for signed intermediate wedges, no unbounded-input association asserted, and no transitive certification of BT capacity continuity.
- **Remedy/affected dependents:** optional separately reviewable strengthening after Theorem 7.26.3; generalizes its same-kernel bounded association discussion without changing its correct statement or tags. No production/source edits.
- **Further dependencies:** §7.21.1 quoted Hörmander input (dedicated L² programme **deferred-by-user**), and Green comparison, Dirichlet and Bedford–Taylor capacity-continuity inputs noted in the report; these are not fresh proof-gap accusations.

**Prior findings unchanged:** `POME-MA-DEGENERATE-C2-PARAMETER-WINDOW-001`, `POME-GREEN-FINITE-PRODUCT-HYPERCONVEX-001`. Whole-section coverage is documented separately in [scope](../coverage/2026-11-22-green-asymmetry-degenerate-density-colombeau.md).
