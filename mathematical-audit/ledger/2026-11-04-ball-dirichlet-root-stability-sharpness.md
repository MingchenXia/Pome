# Additive classified finding — 2026-11-04

**ID:** `POME-BT-BALL-DIRICHLET-SHARP-ROOT-STABILITY-001`  
**Status:** **verified conditional deduction** (not confirmed error, not proof gap, not verified repair).  
**Severity:** low.  
**Reviewed main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.  
**Affected integrated source:** `docs/sections/bedford-taylor-products-and-local-capacity--the-ball-dirichlet-problem-with-continuous-density/index.html`, blob `ff1d5dfff1913156b45875eabf921f60af553b99`; Theorem 7.9.2 source `foundations-of-pluripotential-theory:69935D4D`, permanent `A092925717E1`, lines 41–50; Eq. 7.9.3 source `foundations-of-pluripotential-theory:0390D064`, permanent `B8751A529320`, lines 46–48; proof 130–154. Lemma 7.9.1 source `:89405657`, tag `0FF4AFFE0ED0`, lines 17–35.

**Precisely tested hypotheses:** fixed ball `B(a,R)`, `n>=1`, nonnegative smooth constant densities `s^n,t^n`, boundary constants `-d,0` with `s>=t>=0,d>=0`; printed `eta=dd^c|z|^2`.

**Verified result:** the smooth explicit solutions `s(|z-a|^2-R^2)-d` and `t(|z-a|^2-R^2)` make both terms of Eq. 7.9.3 sharp **simultaneously**: exact norm `d+R^2(s-t)`. General bound `||H_f-H_g||<=boundary difference+R^2||f-g||_infty^(1/n)` and no exponent `>1/n` uniformly at zero density. Complete calculation, parameter dependence, and negative higher-exponent test: [full proof](../reports/2026-11-04-ball-dirichlet-sharp-root-stability.md).

**Mathematical classification:** correct printed theorem with a **new optimality corollary**, not a repair or a statement of a false theorem. The model's solution identification invokes printed uniqueness/comparison; the full BT existence chain remains conditional. **Proposed (unapplied) addition:** include the sharp constant model and optimal Hölder exponent as a remark after Eq. 7.9.3.

**Actual coverage and dependent:** newly inspected selected §7.9.1–2 / Eq. 7.9.3 at anchored lines; checked §7.10's explicit extension of Eq. 7.9.3 to bounded measurable densities (**statement/context only**), not its unrelated `L^1` convergence proof. No prior findings resolved; no new full-section certification. Dedicated Demailly approximation/regularization, Bergman, weighted L², Ohsawa–Takegoshi, multiscale and positivity-loss work remains **deferred-by-user**. 
