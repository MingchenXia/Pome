# Ledger — POME-FORMALJ-BRACKET-ORDER-OBSTRUCTION-001

- **Date:** 2026-11-16.
- **Severity:** low.
- **Status:** verified conditional deduction (self-contained model), not a confirmed error or proof gap.
- **Scope:** Proposition 9.53.2, equation 9.53.3, Lemma 9.53.5, Theorem 9.53.13 **necessity only**, main `b6933b772f41b45918f7e25ed1afbbb1fd892272`.
- **Anchor:** `docs/sections/formal-integrability-and-smooth-complex-coordinates/index.html` blob `218b71104a05350a9bb37b63c64638efecbd1e42`, physical lines 10–40 / 44–75 / 162–204; source/permanent labels given in the [full proof](../reports/2026-11-16-formal-integrability-bracket-order-sharpness.md).
- **Finding:** For `bar L1=partial_bar1+epsilon*bar(z2)*partial_z2`, `bar L2=partial_bar2`, the integrability tensor is nonzero, the torsion decomposition sign is correct, all local smooth CR functions depend only on `z1`, and the coordinate-approximation order cannot be improved past `s=1`. This proves the hypothesis necessity for `s>=2` and a sharp contrast with complex dimension one.
- **Proposed correction:** none to printed claims; optional illustrative example in a separately reviewable production PR only.
- **Dependents:** §9.53.2/.5, §9.53.13 necessity; hard converse, L2/elliptic machinery and all remaining material not certified.
- **Excluded work:** Demailly approximation/regularization and its dedicated Bergman/L2/OT/multiscale/positivity-loss proof plan remain **deferred-by-user**.
