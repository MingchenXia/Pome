# POME-WEIERSTRASS-COEFFICIENT-ORDER-ROOT-EXPONENT-001

- **Date / reviewed main:** 2026-11-22 / `b6933b772f41b45918f7e25ed1afbbb1fd892272`.
- **Severity / status:** low / **verified conditional deduction**, not a false printed theorem, not a proof-gap repair.
- **File / blob / permanent source:** `docs/sections/complex-spaces-and-modifications--division-and-finite-analytic-modules/index.html` / `8f776a57a63b2917689b38f5c59b677a11cecce8` / Eq. 9.2.1 source `foundations-of-pluripotential-theory:1F95143C` and permanent `667706D7A5E8`, lines 16–29.
- **Statement and full proof:** [dated report](../reports/2026-11-22-weierstrass-root-exponents-and-coherence.md); if the coefficient $a_j$ has order $s_j$ at zero, the roots obey $|w|\le C\|z'\|^{\min_j s_j/j}$. Coefficient Taylor bounds plus the explicit monic-polynomial root inequality give the estimate; $w^m-z_1^s$ proves universal sharpness.
- **Proposed change:** optional note after Eq. 9.2.1, preserving tags and attribution; no mandatory correction.
- **Affected dependent passages:** Weierstrass division root localization and uniform estimates (9.2.2; lines 54–58); bounded removable extension on vertical fibers (9.2.9; lines 176–182); potential use by finite-analytic-map results §9.3.
- **Limits:** this is a bound on *all root moduli*, not a canonical labeling of branches. Current §9.2 directly read whole, but upstream Theorem 5.5.2 and all transitive chains not independently certified; §19.5.32 selected check assumes its stated geometric inputs. Dedicated excluded approximation/L² programmes remain deferred-by-user.
