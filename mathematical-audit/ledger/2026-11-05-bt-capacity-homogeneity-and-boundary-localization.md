# Classified ledger — 2026-11-05 — Bedford–Taylor capacity localization and homogeneity

**Reviewed main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.
**Detailed report:** [Bedford–Taylor capacity homogeneity](../reports/2026-11-05-bt-capacity-homogeneity-and-boundary-localization.md).
**Current integrated proof:** `docs/sections/bedford-taylor-products-and-local-capacity--bounded-measurable-densities/index.html`, blob `762b841b0cb243784dc988f04dbf2779da66c469`.

| Stable finding ID | Status / severity | Proof-level scope and exact anchors | Correction, dependents and limits |
| --- | --- | --- | --- |
| `POME-BT-CAP-EXPONENT-HOMOGENEITY-001` | **verified conditional deduction / low** | Lemma **7.10.1** source `foundations-of-pluripotential-theory:74804636`, permanent `C09E42A43E93`, physical lines **11–13, 19–33**; negative-tail step in Theorem **7.10.2** source `:9C25B561` / `C9116FCEFCD2`, **66–78**. Exact smooth quadratic ball model gives nonempty compactly contained comparison sets, \(\int (dd^cu_\lambda)^n=(7\lambda/4)^n\), capacity \(C_n>0\); forces exponent \(t^n\). Derive \(\mathrm{Cap}\{u<v-2\delta\}\le M\delta^{-(n+1)}\int(v-u)_+\eta^n\); joint scaling forces power \(n+1\) with universal scale-free constant. | Printed lemma correct; possible short explanatory note only. Depends on the printed comparison principle/mixed Bedford–Taylor products for the general inequality. **No general proof-chain certification**, no coefficient sharpness claim. |
| `POME-BT-CAP-LOCALIZATION-NECESSARY-001` | **verified conditional deduction / low** | Same Lemma **7.10.1**, same source/permanent tags and lines: constants \(u=0,v=2,s=0,t=1\) on the unit ball have RHS zero but positive LHS when the strict set is the entire domain. | The printed relatively compact comparison-set hypothesis is necessary unless replaced by another boundary condition. **Not** a counterexample to the stated lemma. No source patch. |

**Unchanged classifications:** earlier §7.9–10 findings and all other confirmed-error/proof-gap/external-dependency/duplicate/verified-repair statuses; Demailly approximation/regularization and the dedicated Bergman/\(L^2\)/OT/multiscale/positivity-loss programme remain **deferred-by-user**. No actual whole-section verification, tests, CI, publication or production modification.
