# Ledger — 2026-11-09-multiplier-ideal-branch-and-diagonal-floor-defects

**Main** `b6933b772f41b45918f7e25ed1afbbb1fd892272`; **branch** `review/mathematical-audit`; **reading page** `docs/sections/lelong-numbers-and-multiplier-ideals--restriction-products-and-integral-closure/index.html` @ `878526739ee043892cdc85040a280504328b6dea`.

| Stable ID | Severity | Status | Mathematical scope | Anchor | Correction / dependents |
| --- | --- | --- | --- | --- | --- |
| `POME-MI-BRANCH-FLOOR-DEFECT-001` | low | verified conditional deduction | `f(w)=w^m`, `phi=c log|z|²`: pullback quotient length exactly `floor(m{c})`, attaining all `0,…,m−1`. Printed Cor. 6.10.5 remains correct. | §6.10.5, original `foundations-of-pluripotential-theory:67803CD5`, permanent `05791D2DFFAA`, physical lines 66–81 | Proposed example; never replace pullback inclusion with equality at a branch divisor without further hypotheses; no downstream printed misuse established. |
| `POME-MI-DIAGONAL-FLOOR-CARRY-001` | low | verified conditional deduction | Diagonal ideal-product exponent defect `floor(sum_i {c_i})`, attaining `0,…,k−1`; independent-product formula checked by angular Fourier orthogonality. Printed Theorem 6.10.1 unchanged. | §6.10.1, original `foundations-of-pluripotential-theory:6A3EE132`, permanent `DFD10C71D607`; Eqs. 6.10.3 `5253F6F9/01EC6A2D5998`, 6.10.4 `888EBDCC/0EA6BB9CDFD8`, physical lines 20–35 | Proposed sharpness remark; diagonal subadditivity cannot be strengthened to equality generally, unlike external product. |

See [complete elementary proofs](../reports/2026-11-09-multiplier-ideal-branch-and-diagonal-floor-defects.md) and [precise selected coverage](../coverage/2026-11-09-ch6-multiplier-ideal-ramification-and-diagonal.md).

**Unresolved / dependency boundary:** full analytic proof of 6.10.1 and the special extension/Hilbert/weighted L² chain **not audited**, not declared incorrect. Existing §6.10.6 integral-closure step from 2026-10-27 is unchanged and not registered again. All other ledger rows remain untouched.

**Deferred-by-user (unchanged):** Demailly approximation/regularization and dedicated Bergman, L², Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof-completion programme; preserved, neither verified nor resolved.
