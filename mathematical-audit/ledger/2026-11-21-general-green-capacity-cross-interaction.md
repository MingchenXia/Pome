# POME-GREEN-CAPACITY-GENERAL-CROSS-INTERACTION-001

**Date:** 2026-11-21  
**Main:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`  
**Severity/status:** low / **verified conditional deduction**. **No false source theorem and no complete upstream proof certification.**

**Anchor:** integrated \`docs/sections/polar-sets-capacity-and-sweeping/index.html\`, blob \`aa814f26482e8ed27e51c945e9202c797449158b\`, Theorem 4.3.7 source \`classical-potential-theory:5388371B\`, permanent \`ABDF7610F7B2\`, lines 61–94; finite-energy/polar supporting argument §4.5 lines 81–85. Full cross-chapter report [here](../reports/2026-11-21-general-green-capacity-interaction-and-cross-chapter-psh-review.md).

**Hypotheses:** connected admissible Greenian \(\Omega\subset\mathbb R^d\) (\(d\ge2\)); disjoint compact \(K,L\Subset\Omega\), both of positive capacity; \(\gamma=\min_{K\times L}G_\Omega>0\), \(a=C(K)>0\), \(b=C(L)>0\).

**Deduction:**
\[
 C_\Omega(K\cup L)\le\frac{a+b}{1+\gamma\min(a,b)}<a+b.
\]
Let \(\eta_K,\eta_L,\nu\) be equilibrium measures of the three compacts and \(x=\nu(K)\), \(y=\nu(L)\). Finite energy of \(\nu\) implies its restrictions charge no polar sets, so \(V_K=1\) on \(K\), \(V_L=1\) on \(L\) \(\nu\)-a.e. Tonelli reciprocity yields \(a\ge x+\gamma ay\), \(b\ge y+\gamma bx\). Sum and use \(x+y=C(K\cup L)\). Both connectedness and positive capacities matter: disconnected components have zero cross kernel, and a polar compact has zero charge.

**Correction / dependents:** No printed correction required; optional independent capacity consequence. Applies to Green equilibrium charges and sweeping bounds, not to Demailly approximation. Distinct from and generally weaker in the special equal-ball setting than the earlier \`POME-CLASS-TWO-BALL-CAPACITY-INTERACTION-001\`, which already computed the sharp leading Newtonian interaction. Preserve all earlier tags, versions, hypotheses, and provenance. Upstream equilibrium/finite-energy claims remain conditional, not transitive certificates.

**Current coverage:** §§5.5 and 9.9 completely read (new direct coverage), §4.3 completely rechecked (not newly counted), selective §4.5; zero complete transitive dependency certificates. Excluded regularization programme **deferred-by-user**. No tests, build, CI, main/source/site/tag or canonicalization changes.