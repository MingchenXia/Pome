# 2026-11-19 — convex Kobayashi boundary-distance audit ledger

- **ID:** `POME-CONVEX-KOBAYASHI-LOG-BOUNDARY-PROPER-GEODESIC-001`
- **Status:** **verified conditional deduction** (low severity). **Not** a confirmed false theorem, independent proof gap, or a repair integrated into the reading edition.
- **Main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. **Integrated source:** `docs/sections/disc-interpolation-on-convex-domains/index.html` blob `c0f853924bef4d4b35d3580d5c330de6613b1407`. **Anchors:** Theorem 9.18.1, source label `klimek-pluripotential-theory:9F2D2DA4`, permanent `7F33F823B79C`, lines 10–58 (especially 47–55); stationary-disc Proposition 9.18.2, source `klimek-pluripotential-theory:B5E61683`, permanent `0A57323E9BD0`, lines 60–86; nonconvex illustration lines 87–95.
- **Hypotheses:** nonempty bounded convex `D subset C^n`, `n>=1`, original Poincare normalization `atanh`, no boundary regularity required.
- **Justification:** `|log dist(a,partial D)-log dist(b,partial D)|<=2k_D(a,b)`, universally sharp on the unit disc; supporting half-plane plus Schwarz contraction supplies the exact proof. Along with printed Theorem 9.18.1, this gives compact closed metric balls and minimizing parametrized geodesics from extremal discs. [Full proof](../reports/2026-11-19-convex-kobayashi-boundary-distance-proper-geodesic.md).
- **Proposed correction:** optional corollary/proof note after Theorem 9.18.1, **not** modification of any printed theorem. No confirmed source error.
- **Affected dependents:** quantitative version of §9.18.1's boundary-distance/completeness step; metric interpretation of §9.18.1 extremal discs. Other dependents not checked.
- **Residual:** §9.17.2–5 upstream chain only statement context, no comprehensive upstream certification.
- **Deferred by user:** Demailly approximation/regularization and dedicated Bergman, L2, Ohsawa–Takegoshi, multiscale-atlas, positivity-loss programme; untouched, neither resolved nor certified.
