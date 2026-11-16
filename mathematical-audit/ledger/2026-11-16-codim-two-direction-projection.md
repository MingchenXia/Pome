# POME-PSH-CODIM2-DIRECTION-IMAGE-001

- **Date:** 2026-11-16.
- **Severity/status:** low–medium; **proof gap** in the integrated proof of Theorem 5.14.10(1), with a **verified local repair proposed**. **Not a confirmed false theorem.**
- **Reviewed main SHA:** b6933b772f41b45918f7e25ed1afbbb1fd892272.
- **Location:** docs/sections/plurisubharmonic-functions--properties-of-plurisubharmonic-functions/index.html, main blob e7d871122eca3eb7416ab8a993063cdc8d3987f3, lines 214–245, especially 237; source sgpt-1E88697D, permanent tag DAE812E1A818; codimension-two clause source 7EBFD328 / permanent A8DA4460C6EC.
- **Hypotheses:** analytic Z of codimension at least two; u psh on X\Z; no assumed upper bound near Z.
- **Precise fault:** a compact truncation Z intersect closed ball is generally not an analytic space without real boundary; a direction map from its **open** analytic part is not shown proper. Remmert's proper holomorphic mapping theorem does not yield the claimed proper analytic image of the closed-ball truncation.
- **Proposed repair:** for x outside Z, the compact direction image \(\{[y-x]:y\in Z\cap\overline B\}\) has real measure zero in \(\mathbf P^{n-1}\), by analytic-stratum dimension \(2n-4<2n-2\). Its complement is dense; choose directions converging to the reference direction and avoiding Z, then apply the original one-variable maximum principle. Full proof and quantified construction in [the dated report](../reports/2026-11-16-codimension-two-remmert-direction-avoidance.md).
- **Dependents:** Theorem 5.14.10(1) and any later appeal to codimension-two psh extension. Theorem remains valid; its other inputs and transitive dependencies are **not** certified. Historical Brelot/Grauert–Remmert attribution should be kept.
- **Other direct checks:** Lemma 5.14.16 (49CC56CB484C; lines 287–352) and Corollary 5.14.20 (79C564A098F9; lines 353–365) selected proof passages show no new identified defect. Proposition 5.14.21 (3EDBDD31B3F1) cited Dirichlet input only classified as external, not audited.
- **Coverage:** §5.14 already partly visited for Choquet selection; +0 first numbered sections, +0 full-section certifications. Existing main ToC inventory 25/747 not recounted. Excluded regularization/dedicated work **deferred-by-user**; audit only.
