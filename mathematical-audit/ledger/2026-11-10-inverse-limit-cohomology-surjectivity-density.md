# 2026-11-10: inverse-limit cohomology surjectivity needs chain-level density

| Finding ID | Severity | Status | Location | Finding | Proposed action | Dependents |
| --- | --- | --- | --- | --- | --- | --- |
| POME-INV-LIM-COHOM-SURJECTIVITY-DENSITY-001 | low for existing statements | verified conditional deduction | §2.14.4, §2.14.6(1); main `b6933b77`; permanent `50E84369B7A2`, `10E2183C49C3` | Two-term Hilbert complexes have \(H^0(E_\nu)\simeq\mathbb C\) and identity cohomology transitions, but their inverse-limit complex is zero if \(r^{-1}=S\), \(r^0(a,b)=(a,ae_0+Sb)\). Thus \(\Theta^0:0\to\mathbb C\) is not onto **after deleting chain-level density**. | Optional source-body Remark, separately reviewable; do not weaken existing hypotheses. | Potential weakened uses of Theorem 2.14.4 surjectivity and Theorem 2.14.6(1). |

[Complete proof with source labels, blob, physical anchors, and sharp finite-stage norm obstruction](../reports/2026-11-10-inverse-limit-cohomology-surjectivity-density.md).

The *printed* Theorems 2.14.4 and 2.14.6 retain the dense degreewise maps and are **not false**. Complementary but distinct prior `POME-INV-LIM-DENSE-DEGREE-NONEXACT-001` concerns injectivity when cohomology transitions are not dense; do not merge the findings.

Previously resolved/unresolved ledgers unchanged. The requested Demailly approximation/regularization and dedicated Bergman, L², Ohsawa–Takegoshi, multiscale and positivity-loss programme remains `deferred-by-user`, neither resolved nor certified.
