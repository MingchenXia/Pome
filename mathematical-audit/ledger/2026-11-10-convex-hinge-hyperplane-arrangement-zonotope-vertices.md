# 2026-11-10 — hinge-arrangement real MA ledger

**ID:** `POME-CONVEX-MA-HINGE-ZONOTOPE-VERTICES-001`  
**Status / severity:** **verified conditional deduction / low**.  
**Main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.  
**Main page:** `docs/sections/convex-analysis-and-toric-potentials--the-real-monge-ampere-measure/index.html`, blob `7089aa41ae2422b1bd6b5094e46668cbc8ed37be`.  
**Anchors:** §21.5 source/permanent `foundations-of-pluripotential-theory:34803B32/07CCE1F902ED`, lines 5–9; Theorem 21.5.1 `:4A0FAEB3/409656CC47D4`, lines 10–42; Proposition 21.5.4 `:EAD83A50/5D8A7A7D734E`, lines 99–160; Equation 21.5.5 `:24CC29A7/D38381F0AC43`, lines 143–151.

**Finding:** For `F=sum_i c_i max(a_i.x-b_i,0)` with `c_i>0`, `MA_R(F)=n! sum_{|I|=n, det A_I!=0} |det A_I| prod_{i in I}c_i delta_{A_I^{-1}b_I}`, grouping coincident vertices; exact mixed `n`-hinge atom has no factorial; total mass `n! vol(sum_i [0,c_i a_i])`. The count is by independent normal *subsets*, not by distinct geometric vertices. Proof uses finite-stratum subgradient-nullity, polarization and multilinearity, with the printed §21.5 normalization. Nonconcurrent and concurrent three-line examples verify the distinction.

**Nature:** New exact finite-dimensional consequence, **not** an error/repair of Proposition 21.5.4, not the earlier separable permanent or moving-crease example. **Suggested correction:** optional source corollary after Proposition 21.5.4, proposed only. **Affected dependents:** §21.11 convex-body interpretation and suitable §21.12 toric PL models; no automatic transfer to non-pluripolar/infinite families.

**Unresolved / external:** General §21.5 real MA and mixed-measure upstream proofs remain unverified as complete chains; finite convex separation is the only elementary external ingredient in this new proof. Every pre-existing ledger issue is unchanged. User-excluded Demailly regularization and dedicated Bergman/L²/OT/multiscale/positivity-loss work remains **deferred-by-user**, never resolved or certified.

[Full proof](../reports/2026-11-10-convex-hinge-hyperplane-arrangement-zonotope-vertices.md) · [actual coverage](../coverage/2026-11-10-ch21-hinge-arrangements-zonotope-vertices.md)
