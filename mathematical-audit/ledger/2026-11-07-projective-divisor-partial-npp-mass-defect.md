# Audit ledger — 2026-11-07 — projective partial NPP mass defect

**POME-NPP-PROJECTIVE-DIVISOR-PARTIAL-DEFECT-001** — **low / verified conditional deduction**. No false printed theorem or new proof gap.

Reviewed main **b6933b772f41b45918f7e25ed1afbbb1fd892272**. Target: docs/sections/non-pluripolar-products--capacity-convergence-and-loss-of-mass/index.html, blob d66813856cb813722806ab912afdfd4815d2da97, lines 41–67, 106–140. Source label / permanent tag: Theorem 13.7.5 foundations-of-pluripotential-theory:AB4EBE3B / 67C4F7EC316E; Example 13.7.6 foundations-of-pluripotential-theory:D5678E03 / ACAEA8D8BE87.

**Hypotheses and complete new model:** $X=\mathbf P^n$, $n\ge1$, $H=\{Z_0=0\}$, $0<\alpha\le1$, $u=\alpha\log(|Z_0|^2/|Z|^2)$, $u_k=\max(u,-k)\downarrow u$, with all products taken relative to normalized $\omega_{\rm FS}$. The $u_k$ are bounded $\omega$-psh and converge in extended capacity. Every $T_k^n$ has mass $1$, but $\langle T^n\rangle=(1-\alpha)^n\omega^n$, and the exact weak limit of bounded products is $(1-\alpha)^n\omega^n+[1-(1-\alpha)^n][H]\wedge\omega^{n-1}$. The interface on $Y=e^{-k/\alpha}$ has mass $[1-(1-\alpha)^n](1-e^{-k/\alpha})^n$. The ambient variable $Y$ has Beta$(1,n)$ law; the residual measure's location follows from transitive $U(1)\times U(n)$-invariance. Every defect fraction $\beta\in[0,1]$ is obtained by $\alpha=1-(1-\beta)^{1/n}$, with $\alpha=0$ trivial.

**Dependency qualification:** the bounded-current mass-one fact uses the *uncertified general* Proposition 13.5.1, source 4EE18BE1 / permanent 06A36B9354A5, blob 943517743538820940559eae8469ce98ecf5fcd5, lines 10–32; NPP pole-discarding uses Definition 13.2.4, source 9D8E4DD8 / tag D79952D7E272, blob 81be8c5acc360c96bd3c5acba05a3cdb5fafaf4c, lines 57–64. Projective normalization §10.6.7 blob ff56aa13950da3423135bb0bbaf40bcc980c21a1, lines 108–113. These are crosschecked, not fully certified.

**Impact:** Theorem 13.7.5's lower inequality remains correct and its mass hypothesis fails in the example; Example 13.7.6 remains correct. Affected dependents: §13.7.5, weighted §13.7.9, any §13–17 argument passing to the NPP product through truncated weak limits. **Proposed addition:** optional quantitative model after Example 13.7.6; no source change.

[Proof](../reports/2026-11-07-projective-divisor-partial-npp-mass-defect.md) · [Actual coverage](../coverage/2026-11-07-projective-divisor-partial-npp-mass-defect.md).

**Other statuses:** prior confirmed errors, proof gaps, candidates, external dependencies, duplications and repairs unchanged. Excluded Demailly/Bergman/L²/OT/multiscale/positivity-loss work remains **deferred-by-user**, not resolved.
