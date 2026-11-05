# Classified ledger addendum — 2026-11-05 — planar Robin upper coefficient

**Finding ID:** `POME-ROBIN-PLANAR-UPPER-CONSTANT-TWO-001`  
**Severity:** low  
**Status:** **verified conditional deduction** (sharp quantitative corollary; **not** a confirmed error, proof gap, or general theorem replacement).  
**Prior art in this audit:** `POME-CUBE-ROBIN-EXACT-001` establishes different real-cube exact values and lower-coefficient sharpness; it remains unchanged. No duplication is asserted.

**Reviewed main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.  
**Integrated file:** `docs/sections/robin-capacity-and-its-quantitative-comparison/index.html`; blob `525f388094d0efb6b9ef9f8701d8ac459fd22814`.  
**Statement:** Theorem **16.37.3**, physical lines **79–85** (proof **87–111**), source `klimek-pluripotential-theory:DAE157DD`, permanent tag `27353237EC80`; definitions physical **7–13**; equilibrium support and total mass invoked **104**.

**Exact hypothesis:** `n=1`; `K subset closed B(0,rho)`, `0<rho<=1`, compact and nonpolar (polar case by zero convention); `alpha(K)=exp(-sup_{|z|<=1}V_K^*)`; `c(K)=exp(-gamma(V_K^*))`; `dd^c=i partial barpartial/(2pi)`.

**Conclusion and justification:** `alpha(K)<=c(K)<=(1+rho)alpha(K)`, with `1+rho` optimal for every fixed `0<rho<=1`; hence the best `C_1` in the printed theorem is exactly `2`. The compactly supported probability measure `nu=2 dd^c V_K^*` yields `V_K^*(z)=int log|z-w| dnu(w)-log c(K)` by the logarithmic fundamental solution and harmonic Liouville. On the fixed unit disk, `|z-w|<=1+rho`, giving the sharp inequality. The explicit disks `K_r=closed B(rho-r,r)` have `c(K_r)=r`, `alpha(K_r)=r/(1+rho-r)`, so their ratio tends to `1+rho`. Full derivation in [the English report](../reports/2026-11-05-sharp-planar-robin-fixed-ball-capacity-constant.md).

**Dependencies:** standard planar equilibrium support `supp(dd^c V_K^*) subset K` and full-growth total mass `int dd^c V_K^*=1/2`, both explicitly used by printed §16.37.3. Those upstream results were not generally independently re-proved here. No hidden regularization programme.

**Proposed action:** optional corollary to Theorem 16.37.3 with the exact n=1 constant and radius-refinement; keep historical attribution and all permanent labels unchanged. No production edit. **Potential dependents:** any use of the quantitative planar Robin/fixed-ball comparison; not a claimed higher-dimensional estimate or a reproof of §16.37.5.

**Actual coverage:** selected **§16.37.3 only**, on a previously partly reviewed current-ToC section; neither the whole §16.37 nor any chapter has been mathematically certified. `25/747/0` inventory persists. Older errors, gaps, external inputs, duplications, repairs and deferred items retain prior statuses; Demailly approximation/regularization and dedicated Bergman/L²/OT/multiscale/positivity-loss programme explicitly remain **deferred-by-user**.

**Review actions:** statement/proof read, normalization and sharp family checked analytically. No builds/tests/CI/formalization/publication. No edits to main/source/body/registry/tags.
