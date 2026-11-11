# Finding ledger — 2026-11-11 — radial polar-pole Green energy

**Stable ID:** `POME-GREEN-RADIAL-POLAR-ENERGY-THRESHOLD-001`  
**Severity:** low.  
**Status:** **verified conditional deduction**, **not** confirmed error, proof gap, or source duplication.  
**Production main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.  
**Source:** `docs/sections/green-energy-and-martin-boundaries/index.html` (blob `976a90f2a5eba299658f73a1eee8b9d3fef8020f`), Example 4.5.5 original `classical-potential-theory:898691BF`, permanent `61A5D2A82793`, physical line 71; §4.5.1 lines 7–13. Disk Green convention crosschecked against §3.5.4 (blob `63c74d1c4a0958633b42903a0e3a4526f42b7588`, original chunk `classical-potential-theory:D6A0F97E`, permanent `870251679082`, lines 33–35).

## Verified result and exact failure boundary

For (0<\gamma<1), on (D=\{|z|<1\}), use the unnormalized Green kernel and radial measure
```text
t = log(1/|z|)
F_gamma(t) = gamma*t                 for 0 <= t <= 1
           = t^gamma + gamma - 1     for t >= 1
dmu_gamma = gamma*(1-gamma)/(2*pi*|z|^2*t^(2-gamma))
            * 1_(0<|z|<exp(-1)) dA
```
Then `G_D mu_gamma=F_gamma(t)` everywhere (with (+\infty) at 0), `mu_gamma(D)=gamma`, `mu_gamma({0})=0`. For every (q>0), the `q`th potential moment against `mu_gamma` is finite exactly when `gamma*(q+1)<1`. In particular
```text
I(mu_gamma) = 2*gamma^2*(1-gamma)/(1-2*gamma)   for 0<gamma<1/2
I(mu_gamma) = +infinity                        for 1/2<=gamma<1
```
The endpoint divergence is logarithmic in the radial integration variable. The theorem's capacity construction remains correct and is not replaced. The exponent is sharp for this family **only**, not a universal energy criterion.

**Proof:** circle-mean Green identity `avg_angle G_D(e^-t,e^-s)=min(t,s)`; radial mass `dm_gamma(s)=gamma*(1-gamma)*s^(gamma-2)ds` for `s>=1`; direct split integral for the potential, and a power-integral test for the moments. Matching values and derivatives at `t=1` exclude a hidden circle mass. The derivative tends to zero at infinity, excluding an atom at the origin. See the [full proof](../reports/2026-11-11-planar-radial-green-finite-energy-polar-pole-threshold.md).

**Proposed correction/insertion:** optional explicit companion example after Example 4.5.5; no correction of the printed theorem is required. Retain permanent tags and historical attribution.

**Dependents:** only Example 4.5.5 and comparisons with Theorem 4.5.2; nothing refuted. General Green-energy, Martin boundary, and Hilbert-completion statements still need independent review. User-excluded Demailly approximation/regularization and dedicated Bergman/L²/OT/multiscale/positivity-loss programme remains **deferred-by-user**, not certified or resolved.

**Actual coverage:** selected proof-level visit to existing partially reviewed §4.5, §3.5 normalization context; **0 first section visits / 0 complete section certifications**; actual ToC **25 chapters / 747 numbered sections**. No source, production main, registry, tags, builds, CI or publication changes.
