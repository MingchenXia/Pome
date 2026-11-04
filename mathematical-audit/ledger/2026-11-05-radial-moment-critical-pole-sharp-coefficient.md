# Finding ledger — 2026-11-05 — sharp radial critical first-moment divergence

| Stable finding ID | Severity | Exact status | Printed theorem false? | Proposed action |
| --- | --- | --- | --- | --- |
| **POME-RADIAL-MOMENT-CRITICAL-POLE-COEFF-001** | **low** | **verified conditional deduction** | **No.** Proposition 15.36.8 is correct. | Optional quantitative corollary; proposal only, do not edit source/main/tags. |

**Reviewed production main:** b6933b772f41b45918f7e25ed1afbbb1fd892272.

**Pinpoint source:** main [docs/sections/equations-with-prescribed-singularities--radial-selection-for-integrable-densities/index.html](../../docs/sections/equations-with-prescribed-singularities--radial-selection-for-integrable-densities/index.html), blob **e007da9bd1c2136d289b278ba69a9cf8d4694d9e**, Proposition **15.36.8**, physical lines **118–154**, source label **non-kahler-pluripotential-theory:013390C6**, permanent tag **704167C1A830**; Equation **15.36.9**, physical lines **124–127**, source **non-kahler-pluripotential-theory:13638BD6**, permanent tag **24634670B4B5**. Lemma 15.30.1 and Theorem 15.36.5 are context dependencies, not fully certified.

**Exact hypotheses:** the current §15.36 radial model on $\mathbb P^k$ with $k\ge2$, $0<\alpha<1$, printed normalized density $q_\alpha$, and first moment $M_\alpha=\int u_\alpha q_\alpha\kappa^k$. Let $\alpha_c=k/(k+1)$.

**Complete mathematical result and proof:** in the linked [dated English proof](../reports/2026-11-05-radial-moment-critical-pole-sharp-coefficient.md). For all $0<\alpha<\alpha_c$,
$$
\frac{\alpha^{k+1}}{k-(k+1)\alpha}
\le -M_\alpha
\le \frac{\alpha^{k+1}}{k-(k+1)\alpha}+k\alpha,
$$
hence $\lim_{\alpha\uparrow\alpha_c}(\alpha_c-\alpha)(-M_\alpha)=\alpha_c^{k+1}/(k+1)$ (equal to $8/81$ for $k=2$). The physical truncated first moment grows as $\alpha_c^{k+1}\log R+O(1)$ exactly at $\alpha_c$; for $\alpha>\alpha_c$, it is asymptotic to $k(1-\alpha)\alpha^k R^{(k+1)\alpha-k}/((k+1)\alpha-k)$. The essential step is the **uniform** bound $0\le F_\alpha^k-A_\alpha^k\le k e^{1-x}$ and the **non-negligible** Stieltjes boundary term. These are proved, not guessed from scaling.

**Distinct from prior findings:** existing **POME-RADIAL-MOMENT-SPECTRUM-001** established the moment finiteness spectrum; **POME-PRODUCT-TRUNC-SCALAR-LOGRATE-001** concerns truncating the forcing density, not the first-moment pole or its physical radial cutoff coefficient. Preserve both prior IDs and states.

**Affected dependents / limitations:** quantifies §15.36.8's scalar-centering branch and the $k=2$ elliptic fivefold example; contextual to Theorem 15.36.5 and Corollary 15.36.11. It does **not** assert a simultaneous $(\lambda,\alpha)$ asymptotic or certify §15.36 existence, PDE steps, general closed-class uniqueness, or the full radial representation proof.

**Scope / preservation:** selected mathematical passage §15.36.8–9 only, not entire §15.36 or any proof chain. Actual current collection 25 chapters, 747 numbered sections, **0 wholly certified mathematical sections**. All historical errors, gaps, candidates, duplicates, external inputs and verified repairs unchanged. Demailly regularization/Bergman/weighted $L^2$/Ohsawa–Takegoshi/multiscale/positivity-loss programme remains **deferred-by-user**, neither restarted nor certified. Only audit Markdown changes; no main/source/tags/CI/build/publication.
