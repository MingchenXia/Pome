# Finding ledger — arithmetic selection under an unequal two-pole weight

- **Stable ID:** `POME-PARTIAL-KERNEL-RATIONAL-IRRATIONAL-ROUNDING-001`.
- **Date:** 2026-11-09.
- **Severity:** low.
- **Status:** verified conditional deduction (supplemental example family); **not** confirmed error, proof gap, completed repair or complete certification.
- **Printed theorem:** §18.46.2 retains the correct \(t=1/2\) result.
- **Pinned main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`; reading edition `docs/sections/partial-kernels-and-quotient-equilibrium--rounding-in-multiplier-ideal-kernel-families/index.html`, blob `f1c3a22bdbfa2598789f5df1ee8369eca29ff815`.
- **Provenance:** Theorem `non-kahler-pluripotential-theory:5A74DD32`, permanent `318BC0622217`, physical lines 36–49,54–100. Section source/permanent `E838CB8C/73EEA7DBAB83`. Equation (18.46.4) `778924A6/7E8D4542A29B`, lines 67–71.
- **Exact finding:** For \(\psi_t=t\log|z|^2-\log(1+|z|^2)\), \(0<t<1\), the allowed exponents are \(\lfloor mt\rfloor\le\alpha\le m-\lfloor m(1-t)\rfloor\). Therefore the cardinality is one if \(mt\) is integral and two otherwise. Rational \(t=u/b\) yields denominator-\(b\) oscillating \(q!/m^q\)-kernel limits; irrational \(t\) yields the single two-band limit; all \(t\) have an unoscillating dimension-normalized limit.
- **Full mathematical derivation:** [source-anchored report](../reports/2026-11-09-partial-kernel-rational-irrational-rounding.md).
- **Proposed change (not applied):** Optional Remark after Theorem 18.46.2 with the rational/irrational degree-rounding formula and normalized measure distinction.
- **Affected downstream interpretation:** §18.30 selected spaces, §18.32 partial envelopes, §18.46 partial-kernel measure normalizations; **none** established as an erroneous downstream theorem.
- **Explicit dependency boundary:** Internal multiplier-ideal order \(\Rightarrow\) divisor Lelong comparison (§5.37.3), psh fiber restriction, classical non-pluripolar definition assumed and not re-certified. Algebraic counts, beta norms, concentration and binomial bounds proved directly. Demailly regularization, and dedicated Bergman/\(L^2\)/OT/multiscale/positivity-loss programme remain **deferred-by-user**: not touched, not resolved.
- **Coverage and limitations:** First selected proof-level §18.46 read; §§18.30,18.32,18.45,18.47 are contextual only. No full-section proof certification, no build/tests/CI/formal proof.
