# 2026-11-16 — concentric spherical interaction masses and critical Lipschitz endpoint

- **ID:** \`POME-SPHERE-NESTED-MASS-CRITICAL-LIPSCHITZ-001\`
- **Severity / classification:** low / **verified conditional deduction**; no false printed theorem; the explicit lower coefficient of Proposition 15.26.2 was conservative, not erroneous.
- **Revision:** main \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`; integrated §15.26 blob \`354dfdf5224fac8896103ec09aa5936351021914\`; §5.27 blob \`ddb2ac8d9de27a22152872e07e5e787d138a790e\`.
- **Precise sources:** Eq. 15.26.1 original \`non-kahler-pluripotential-theory:4C0F3404\` / permanent \`938F2C76C18A\` lines 10–23; Proposition 15.26.2 original \`non-kahler-pluripotential-theory:92442012\` / \`8F3C95237950\` lines 26–65; Lemma 5.27.25 original \`non-kahler-pluripotential-theory:961DE4FB\` / \`3242D4BA1F13\`, around lines 518–527 and following proof.
- **Proof:** exact radial Stieltjes \`d((g')^n)\` gives shell masses \`((1+q_a)^n-q_a^n)d_{j,a}^n\`, with \`q_a=(2^a-1)^{-1}\`, not merely the individually retained \`d_{j,a}^n\`. In the printed \`a=1/2\` case the valid domination coefficient improves by \`(2+sqrt(2))^n-(1+sqrt(2))^n\`. The new \`a=1\` version yields a **Lipschitz** (but non-\`C^1\` at the center) global \`h\`-psh potential and singular spherical Monge–Ampère domination by \`(2^n-1)S_{n,1}/Z_1^n\`. No claim the mixed background coefficient is globally sharp.
- **Dependencies:** internal bounded Bedford–Taylor continuity and §5.27.25 radial flux identity; downstream \`15.26.3\` and \`15.26.4\` only conditionally inherit the domination for the new probability. Upstream existence in \`15.25.1\`, \`15.10.1\` not certified.
- **Suggested patch:** optional quantitative remark + separate endpoint construction; **not applied to main/body/registry**.
- **Coverage:** §15.26, §5.27 already partly inspected: +0 numbered-section first visits / +0 complete section certifications; current 25 chapters / 747 numbered sections.
- **Excluded programme:** Demailly regularization, Bergman, \(L^2\), Ohsawa–Takegoshi, multiscale-atlas and positivity-loss remain **deferred-by-user**. Prior findings \`POME-SPHERE-MA-NORM-001\`, \`POME-SPHERE-HOLDER-SHARP-001\`, \`POME-HOLDER-BALL-MASS-EXPONENT-001\` unchanged.

[Full source-anchored proof](../reports/2026-11-16-concentric-sphere-mixed-mass-and-lipschitz-endpoint.md) · [coverage delta](../coverage/2026-11-16-ch15-concentric-shell-endpoint.md).
