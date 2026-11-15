# Ledger — 2026-11-15 — optimized BT energy/capacity exponent

**ID:** \`POME-BT-ENERGY-CAPACITY-OPTIMAL-EXPONENT-001\`
**Status:** **verified conditional deduction**
**Severity:** low
**False printed theorem?:** No. Lemma 7.11.19 and Proposition 7.11.22 remain correct as stated.
**Reviewed main:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`
**Integrated file/blob:** \`docs/sections/bedford-taylor-products-and-local-capacity--local-energy-moments/index.html\` / \`e619f7aa95f80ce11aa676193b054db3180e59d4\`.
**Tags/anchors:** Lemma 7.11.19 \`foundations-of-pluripotential-theory:2F603F4B\` / \`546063653198\`, lines 386–426; Eq. 7.11.21 \`:2CDB386B\` / \`92D8C50415C8\`, lines 394–398; Proposition 7.11.22 \`:871210E1\` / \`1036F9F7DDDA\`, lines 428–486.

**New proven implication (conditional on printed lemma):** \(\mu_\varphi(E)\le K_{n,p}e_p(\varphi)^{n/(n+p)}\operatorname{Cap}_B(E)^{p/(n+p)}\), \(K_{n,p}=(n+p)/(n^{n/(n+p)}p^{p/(n+p)})\), including null-capacity handling. Explicit bounded radial \(\mathcal E_0(D)\) functions with uniformly bounded p-energy prove exponent \(p/(p+1)\) optimal for \(n=1\). No general \(n\ge2\) optimality or sharp numerical constant is claimed.

**Dependency/status boundary:** Reuses existing general BT truncation inequality and the previously audited exact unit-disc capacity. Lemma 7.11.18, §7.3.7 and underlying classical BT chain are **not transitively certified**. No new proof of the full Theorem 7.11.30 existence argument.

**Proposed correction:** Optional editorial addition after Eq. 7.11.21, reviewable separately; no direct main/source/registry/canonicalization edits.
**Affected downstream scope:** Proposition 7.11.22, Lemma 7.11.27, Theorem 7.11.30 (possible refinements only, not verified downstream theorem repairs).

**Complete English proof:** [report](../reports/2026-11-15-optimized-bt-energy-capacity-exponent.md). **Exact coverage:** [coverage](../coverage/2026-11-15-ch7-bt-energy-capacity-sharpness.md). New first-visited numbered sections 0; new whole-section certificates 0; 25 chapters/747 numbered sections.

**Deferred-by-user, not certified:** All user-excluded Demailly regularization/approximation and dedicated Bergman/L²/Ohsawa–Takegoshi/multiscale/positivity-loss proof programme. Existing confirmed errors and other ledger statuses untouched.
