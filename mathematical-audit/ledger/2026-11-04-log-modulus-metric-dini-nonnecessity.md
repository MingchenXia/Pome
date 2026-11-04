# Classified finding: logarithmic-modulus metric completion outside square-root Dini regime

- **Stable ID:** `POME-METRIC-DINI-NONNECESSITY-LOGPOLE-001`.
- **Date:** 2026-11-04.
- **Reviewed main SHA:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.
- **Severity:** low.
- **Status:** **verified conditional deduction** (independent exact boundary example, **not** confirmed error or proof gap).
- **Scope:** selected new logarithmic-modulus and radial-metric computations, already partially reviewed §5.39; *not* whole-section certification.
- **Integrated file:** `docs/sections/plurisubharmonic-functions-and-singularities--potential-regularity-and-metric-distance/index.html`, **blob `26695e8698b9114b97108efb16ec94f3984ee308`**, physical lines **58–105** and **109–124**; context **10–44, 126–169**.
- **Source and permanent labels:** Equation 5.39.5 `non-kahler-pluripotential-theory:618F80CA` / `06D8010B670C`; Theorem 5.39.6 `non-kahler-pluripotential-theory:97B8A37E` / `21429B9E1BF3`; Corollary 5.39.7 `non-kahler-pluripotential-theory:2F17E044` / `380EB17A4350`; boundary context Theorem 5.39.1 `:EF691FCE` / `230882F1D833`.
- **Hypotheses:** In the disk `|z|<R<exp(-(a+2))`, `a>0`, set `v_a(0)=0`, `v_a(z)=(-log|z|)^{-a}`, `theta=0`, and `eta=dd^c v_a` off `A={0}`. The current is positive and `eta` is smooth strictly Hermitian on the punctured domain.
- **Complete calculation:** For `L=log(1/r)`, `Delta v_a=a(a+1)/(r² L^{a+2})`; `eta=(Delta v_a/4)omega_E`, and `dd^c v_a(B_r)=(a/2)L^{-a-1}` with no Dirac atom. The optimal modulus is exactly `m(s)=(-log s)^{-a}` since the radial profile is concave/increasing near zero. Hence `int_0^s sqrt(m(t))/t dt=+infinity` iff `0<a<=2`; the radial completion distance is nevertheless exactly `C_a (log(1/r))^{-a/2}` for **every** `a>0`, with collapsing angular circumference.
- **Conclusion and distinction:** The printed condition `a>2` is **sufficient, not necessary**, precisely as Corollary 5.39.7 already says. Neither Theorem 5.39.6 nor Corollary 5.39.7 is false. Do not replace sufficient conditions by an unwarranted general necessary-and-sufficient criterion; this calculation applies to an explicit radial family.
- **Affected dependents:** Any reading of the Dini hypothesis in Theorem 5.39.6 and consequent compactness statement 5.39.8 as a **necessary** regularity threshold; no existing printed dependence is invalidated. Earlier `POME-METRIC-COMPLETIONS-GH-001` is mathematically distinct and unchanged.
- **Proposed correction:** Optional explanatory example immediately after Corollary 5.39.7; retain the theorem, source attribution, permanent tags and all prior conditional/general statuses. No source/body patch was applied.
- **External inputs:** none beyond standard radial differentiation and local metric length; **excluded** Demailly approximation/regularization, Bergman, weighted L², Ohsawa–Takegoshi, multiscale and positivity-loss work untouched, still **deferred-by-user**.
- **Proof:** [full independent English report](../reports/2026-11-04-log-modulus-finite-intrinsic-distance-beyond-dini.md).
- **Verification scope:** direct algebra and differential-geometric proof; no tests, builds, CI, publication, formal verification or transitive audit of all §5.39 dependencies.
