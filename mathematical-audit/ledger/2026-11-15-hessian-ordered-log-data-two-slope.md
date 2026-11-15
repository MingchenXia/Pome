# 2026-11-15 — Ordered logarithmic Hessian data

- **Stable finding:** \`POME-HESS-ORDERED-LOGDATA-TWO-SLOPE-001\`
- **Classification:** **low / verified conditional deduction**; source statement correct, **not** a confirmed theorem error, not an applied repair.
- **Reviewed main:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`.
- **Source:** \`docs/sections/complex-hessian-equations--hessian-mass-and-global-comparison/index.html\`, blob \`580d3bc2b10ebd01d880b2a31fc6930436570aac\`.
- **Exact anchors:** Theorem 8.13.10 \`non-kahler-pluripotential-theory:98425BFC\` / \`A532C77D7D0C\`, lines 281–303; Proposition 8.13.12 \`non-kahler-pluripotential-theory:3FE616D3\` / \`FBE7E9A6BE5E\`, lines 330–353; Corollary 8.13.13 \`non-kahler-pluripotential-theory:126D8F14\` / \`5460C4009B01\`, lines 355–365.
- **Hypotheses/claim:** \(\kappa\le\partial_t f\le\Lambda\), same finite Radon \(\nu\), bounded admissible solutions \(u,v\) with actual values in \([A,B]\), and \(0\le a\le h_1-h_2\le b\) \(\nu\)-a.e. imply **\(v-b/\kappa\le u\le v-a/\Lambda\)** everywhere.
- **Proof:** strict domination on the sets \(\{u<v-b/\kappa-\delta\}\) and \(\{v-a/\Lambda+\delta<u\}\), using only \(u,v\) inside \(f\); take \(\delta\downarrow0\). Constant solutions with \(f=\kappa t\) or \(f=\Lambda t\) separately prove both coefficients optimal.
- **Conditional input:** Theorem 8.13.10's full bounded Hermitian domination, and its underlying §§8.12, 8.11/8.9 theory, not fully audited. **No** Demailly approximation/regularization or dedicated Bergman/L²/OT/multiscale/positivity-loss work was opened; those findings remain **deferred-by-user**.
- **Proposal/affected downstream:** optional new corollary after §8.13.12, relevant to §8.13.13 and proper-equation stability; never silently alter printed statements or provenance.
- **Audit delta:** selected already-visited §8.13 proof passages; **0 newly first-visited sections; 0 fully certified sections**; ToC **25 chapters / 747 sections**. No production/source edits, builds, CI, site publication or automatic merge.
- **Full report:** [English proof](../reports/2026-11-15-hessian-ordered-log-data-two-slope.md). [Exact coverage](../coverage/2026-11-15-ch8-hessian-ordered-log-data.md).
