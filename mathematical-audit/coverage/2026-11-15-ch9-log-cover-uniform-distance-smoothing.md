# Selected coverage delta — 2026-11-15 — Chapter 9 infinite covering

**Reviewed main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. **Branch parent SHA at review:** `1740dd07663ff23297ac41f8fe2fdf269b302265`. **Classification:** selective direct proof/model check, not complete theorem-dependency certification. [Full proof](../reports/2026-11-15-log-cover-uniform-distance-smoothing-sharp-levi.md).

| Section | Actual content examined | Exact integrated anchor and tags | Coverage status |
| --- | --- | --- | --- |
| §9.25 | Structural navigation heading only; already noted earlier | `docs/sections/separation-strict-exhaustions-and-coverings/index.html`, blob `89f1c30a6df3c3df624fd05943a5cc64460824b8`, section `D10F3B8AA2A1`, line 5 | No mathematical proof or new first-visit credit |
| §9.26 | Only convention of proper finite smooth exhaustions, no re-audit of Theorem 9.26.1 | `docs/sections/separation-strict-exhaustions-and-coverings--local-holomorphic-separation-and-strict-exhaustion/index.html`, blob `c04701d0358d43a3a3f1aed61e7cdd2a48305417`, section `B52903F03BA2`, opening convention | Context only |
| §9.28.2 | Lifted complete metric and distance properness; independently computed on \(\exp:\mathbb C^m\to(\mathbb C^*)^m\) | `docs/sections/separation-strict-exhaustions-and-coverings--strictly-plurisubharmonic-exhaustions-on-coverings/index.html`, blob `ef92b5dc5bb4c143345621ea60ca52f3ca7d1872`, source `demailly-complex-geometry:CD2B2989`, permanent `E200BE9CFD9E`, lines 30–45 | New exact model, not full general verification |
| §9.28.3 | Distinct distance-error, positive-derivative sheet bounds and Levi lower estimate all checked on the same \(m\)-dimensional covering | Same blob, source `demailly-complex-geometry:09F8EE91`, permanent `7808CCD76C79`, lines 48–101 | New model simultaneously tests all conclusions; proof chain only partially rechecked |
| §9.28.5 | Finite continuous properness and exact \(H_F\ge2I\), sharp for fixed \(F\) | Same blob, source `demailly-complex-geometry:F653208F`, permanent `73159A8CF2BB`, lines 104–142 | Direct conditional deduction only, no general proof certificate |

**Accounting:** 25 actual chapters / 747 numbered sections at unchanged main. §§9.25, 9.26, 9.28 were already in the historical audit: **0 new first-visited sections, 0 entire-section certifications**. §9.28 has a new independent quantitative example, not merely a repeat of the 2026-11-01 finite-degree criterion or 2026-11-02 complete-Kähler-composition theorem.

**Outstanding:** generic covering theorem's global derivative smoothing and metric dependencies have not been independently transitively verified; nothing in the user-excluded regularization programmes has been reopened. No full build or automated test claims.
