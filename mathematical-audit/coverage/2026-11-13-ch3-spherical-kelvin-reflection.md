# Exact increment — 2026-11-13, Chapter 3, §3.3.15

**Production main:** b6933b772f41b45918f7e25ed1afbbb1fd892272. **Audit base:** review/mathematical-audit @ 84482766272068d46754ed37589b5ab81440bae1. Actual current reading-edition inventory: **25 chapters, 747 numbered sections**.

| Exact area | Source label / permanent tag | Integrated file blob and physical line anchors | Actual scope, not full certification |
| --- | --- | --- | --- |
| §3.3.15 heading | classical-potential-theory heading / A9175B0B7BA5 | docs/sections/classical-harmonic-analysis/index.html @ 75e982788e627af602981823a82863cbd36ee712, line 215 | Direct identification of the reflection unit |
| Lemma 3.3.16 (Bocher) | classical-potential-theory:6C6775C3 / B0CFE200676D | same file, 217–226 | Read for optional dependency comparison only; prior 2026-11-04 proof audit not repeated |
| Theorem 3.3.17 | classical-potential-theory:2BBE313C / 14F410C2E770 | same file, 229–241 (statement 229–231; existing proof 233–241) | Direct independent proof, explicit Kelvin formula on the larger annulus and full interface flux argument; printed theorem correct |
| Kelvin theorem 3.2.2 and Eq. 3.2.3 | classical-potential-theory:B1AA5815 / 97BA27062B9F; classical-potential-theory:074F2D29 / 0E9BCA99B831 | docs/sections/kelvin-transforms-and-half-space-potentials/index.html @ f2615a5393af724c3996978212162f94911ff9d9, lines 16–49, especially 18–20 | Inspected exact Laplacian covariance; no re-audit of all §3.2 |
| Elementary annulus bounds | internal maximum principle, ball Poisson gradient bound, Green identity, Weyl | explicitly derived and scoped in [report](../reports/2026-11-13-spherical-kelvin-odd-reflection-collar.md) | Conditional standard internal inputs, not complete upstream chapter certification |

**Classification:** POME-HARM-KELVIN-SPHERE-EXPLICIT-COLLAR-001, low / **verified conditional deduction**; no source false theorem, no purported full replacement certification of all other dependencies. Affects only the optional strengthened proof of 3.3.17 and its unspecified downstream uses.

**Matrix accounting:** §3.3 was already partially audited. This run gives **0 first-visited numbered sections** and **0 completely certified sections**; broad chapter ledger and other 746 rows are unchanged. The 25/747 counts refer to actual main contents, not certified coverage. The excluded Demailly and dedicated Bergman/$L^2$/OT/multiscale/positivity-loss work remains **deferred-by-user**, not resolved.

Only audit Markdown is authorized. No build, tests, CI, publication or production/source/tag/registry writes were carried out.
