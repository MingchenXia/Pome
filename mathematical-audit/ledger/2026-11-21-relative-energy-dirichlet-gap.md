# POME-RELENERGY-STRICT-CONCAVITY-DIRICHLET-GAP-001

- **Date/main:** 2026-11-21 / \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`.
- **Severity/status:** low / **verified conditional deduction**; **not** a false theorem, missing proof, or full upstream certification.
- **Integrated locator:** \`docs/sections/relative-energy-and-perron-segments--relative-monge-ampere-energy/index.html\`, lines 42–116, main blob \`16fdcc4c6a6f0cc75e69ba267bd7da2b2d7922a1\`.
- **Permanent source anchors:** Proposition 17.3.4 \`foundations-of-pluripotential-theory:44639882\`, tag \`9086ABF36774\`; equation 17.3.5 source \`A392067F\`, tag \`46190A7C1B2F\`; Proposition 17.3.9 source \`A4AB3054\`, tag \`356D15D0C316\`.
- **Hypotheses/conclusion:** smooth \`u,v~phi\` on connected compact Kähler \`X\` with \`theta_u,theta_v>=delta omega\`, \`delta>0\`, satisfy
  \[
  E_\theta^\phi((1-t)u+tv)-(1-t)E_\theta^\phi(u)-tE_\theta^\phi(v)
  \ge \frac{n\delta^{n-1}}2t(1-t)\int_Xd(v-u)\wedge d^c(v-u)\wedge\omega^{n-1}.
  \]
  This is strict for nonconstant differences at interior \`t\`. Equality as formula for \`n=1\`.
- **Proof:** exact smooth second variation \`-n int dh wedge d^c h wedge theta_{u_t}^{n-1}\`, positivity, and subtracting the quadratic barrier. Full argument: [dated report](../reports/2026-11-21-relative-energy-strict-concavity-and-convex-measure-rotation.md).
- **Suggested correction/extension:** optional independent corollary after §17.3.9, not a correction to the original theorem. The existing result is correct; retain its attribution/tags and smooth/strict-positivity hypotheses.
- **Dependents/gaps:** energy strictness/equality and possible Poincaré coercivity; not yet certified across singular \`E^1\` potentials. §17.2, §13.2/§13.8 and §16.21–§16.27 remain dependency inputs; excluded Demailly regularization-related programmes remain **deferred-by-user**.
