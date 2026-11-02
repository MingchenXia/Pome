# Classified audit ledger increment — 2026-11-03

**Reviewed production main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`  
**Review branch:** `review/mathematical-audit`  
**Finding:** `POME-GEO-SUBGEO-ENDPOINT-SANDWICH-001`  
**Severity:** low  
**Status:** **verified conditional deduction** (independent qualitative proof plus sharp limitation; no erroneous printed theorem).

**Location:** `docs/sections/geodesic-rays-in-the-space-of-potentials/index.html`, main blob `52bf9e459a0dfb1c8afe79556db037450be06bb3`. Prop. 17.10.7 `sgpt:DBC4F9ED` / permanent `1880C1FBD88F`, lines 88–139; Cor. 17.10.9 `sgpt:B35F3B4F` / `C645EE3517E1`, lines 144–170; Prop. 17.10.13 `sgpt:BBFDD373` / `5ECD747A7B0B`, lines 194–266; Eq. 17.10.14 `sgpt:5593AC43` / `BA313A9B1A1F`, lines 244–257.

**Checked hypotheses:** compact connected Kähler X, smooth closed big θ, two nonempty endpoint families uniformly bounded above; ordinary (possibly singular) θ-psh subgeodesics. Choquet's countable reduction and quasi-everywhere endpoint equality remain stated inputs.

**New proof:** for a countable representing family, `u_t → u_0` almost everywhere by the individual q.e. endpoint limits, the countable polar exceptional union, and the convex-chord upper bound. Fix one member and set `w=inf_{0<t<1} u_t^{i0}`; Prop. 17.10.7 makes w an integrable θ-psh minorant. Set `W=max(u_0,u_1)`; then `w ≤ u_t,u_0 ≤ W`. Since `W-w ∈ L¹(X)`, dominated convergence proves endpoint convergence in `L¹` without the compactness step in lines 259–265. Symmetric at t=1. This is an alternative proof, not a claim that the existing proof is invalid.

**Sharp limitation:** spatially constant convex V-shaped subgeodesics with both endpoints zero and values in [-1,0] attain L¹ distance one at time ε→0; no family-uniform modulus depending only on common endpoints and height bounds exists. The construction does not refute the qualitative result or imply the same deficiency for canonical Perron geodesics.

**Proposed correction:** optional explanatory proof insertion and a guard against unqualified quantitative endpoint claims. No source/body/tag/registry change applied. **Affected dependent:** potential rate-strengthenings of Prop. 17.10.13; Lemma 17.10.22 unchanged.

**Actual incremental coverage:** new targeted examination of the **early** §17.10.7/.9/.13/.14 endpoint and supremum steps; §17.10 was *already partially reviewed* for later radial energy. Not the whole section, not a certified dependency chain. The table of contents still has 25 chapters and 747 numbered sections; no whole section is mathematically certified.

**Preserved classifications:** all prior confirmed errors, proof gaps, external inputs, genuine duplicates, conditional repairs and **deferred-by-user** findings remain unchanged. Demailly approximation/regularization and dedicated Bergman, weighted L², Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof completion were not touched.

**Report:** [proof and sharpness example](../reports/2026-11-03-subgeodesic-supremum-endpoint-sandwich-and-nonuniformity.md). No tests, build, CI, formalization, website or main/source modification was carried out.
