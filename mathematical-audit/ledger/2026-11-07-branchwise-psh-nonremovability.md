# Classified finding — POME-PSH-BRANCH-CODIM-NONREMOVABILITY-001

- **Date:** 2026-11-07.
- **Status / severity:** **verified conditional deduction / low**. Complete elementary sharpness example for *unstated* codimension-only extension, conditional only in its comparison with the original positive theorem; **neither printed theorem is false**.
- **Reviewed main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.
- **Source anchors:** §9.9 Proposition 9.9.4 `foundations-of-pluripotential-theory:A6674849`, permanent `B43080BD49F3`, `docs/sections/complex-spaces-and-modifications--plurisubharmonic-functions-on-reduced-spaces/index.html:62-90`, blob `d9d8091b530c9843e5a725b49af2400936aeaa3a`; §9.10 Theorem 9.10.14 `sgpt:EEFC0C9A`, permanent `C69D2F0ABA4F`, clause `C2D00AE1EE6E`, `docs/sections/pluripotential-theory-on-unibranch-spaces/index.html:139-155`, blob `6edfa6b19fa7cdbaf0c2665389fa7b3ca338cdf4`.
- **Hypotheses checked:** reduced union of `r>=2` coordinate `n`-planes (`n>=2`) meeting only at the origin; the omitted point has codimension `n` in each branch; finite branchwise constant PSH data are uniformly bounded.
- **Complete obstruction:** restriction of any purported extension to the `i`th coordinate disc is subharmonic, constant `c_i` punctured, so its central value equals `c_i`. Unequal constants make simultaneous extension impossible, including for the USC envelope with central value `max c_i`.
- **Difference from previously printed example:** §9.10's pre-existing source footnote gives only a **codimension-one** two-curve intersection. This records a separate **codimension-at-least-two** model and exact `r`-branch criterion, not a duplicate theorem or replacement attribution.
- **Proposed action:** preserve both statements, proof and author attribution; optionally cross-link §9.9's upper-bound result to §9.10's nonremovability caveat. No source edit performed.
- **Affected dependents:** any future singular-space Hartogs/envelope descent inference that drops unibranchness; no particular downstream statement condemned without reviewing it.
- **Full proof:** [dated report](../reports/2026-11-07-high-codimension-branchwise-psh-nonremovability.md). **Selected coverage:** [increment](../coverage/2026-11-07-ch9-branchwise-codimension-nonremovability.md).
- **Scope:** other §9.9 and §9.10 arguments and all external inputs not certified; user-excluded Demailly approximation/regularization and dedicated Bergman/L²/OT/multiscale/positivity-loss program **deferred-by-user**, not solved.
