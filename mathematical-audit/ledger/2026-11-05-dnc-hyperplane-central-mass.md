# 2026-11-05 status ledger: normal-cone hyperplane central mass

**Finding:** `POME-DNC-HYPERPLANE-CENTRAL-MASS-001`; **severity low; status verified conditional deduction**. The printed theorem is not disproved or fully verified.

**Location:** reviewed `main` `b6933b772f41b45918f7e25ed1afbbb1fd892272`, file `docs/sections/divisorial-restricted-volumes/index.html` blob `8eb1127568e77d6d045098361c366ceeb846b909`. Theorem **20.8.3** source `transcendental-positive-cones:42C59BDB`, permanent `8DC7DAC31FB7`; lines 64–79; (20.8.4)–(20.8.8) lines 115–143, 157–160 and derivative lines 227–233.

**Verified:** For `X=P^n, Y=P^(n-1), alpha=aH` and `W=Bl_(Y×0)(X×P^1)`, `beta=aA+bB-cE` has exact `Vol(beta)=(n+1)(b-c)a^n+a^(n+1)-(a-c)^(n+1)` in an ample chamber, while the two central restricted volumes are `(a-c)^n` and `a^n-(a-c)^n`, summing to `a^n`. The base-fiber difference is `(n+1)a^n`; the derivative is `na^(n-1)`. This supplies a distinct all-dimensional polynomial consistency check for (20.8.4)–(20.8.8), not the earlier two-point model.

**Disposition:** No source edit. Proposed permanent regression check of constants, projective-bundle conventions, and signs for the general §20.8 volume-derivative argument and its dependents. General Legendre, envelope, restricted NPP mass, and limiting steps remain unverified. Excluded regularization/Bergman/L2/OT/multiscale/positivity-loss inputs are **deferred-by-user**, not repaired. [Full English proof](../reports/2026-11-05-hyperplane-deformation-to-normal-cone-volume-check.md).
