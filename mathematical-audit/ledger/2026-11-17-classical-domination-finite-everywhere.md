# 2026-11-17 — classical Green domination at an infinite polar pole

- **ID:** POME-CLASS-DOMINATION-FINITE-POINTWISE-SHARP-001
- **Severity/status:** low / verified conditional deduction (sharpness of a stated assumption; printed theorem correct)
- **Main SHA:** b6933b772f41b45918f7e25ed1afbbb1fd892272
- **Source:** docs/sections/polar-sets-capacity-and-sweeping/index.html, blob aa814f26482e8ed27e51c945e9202c797449158b; Theorem 4.3.10, source classical-potential-theory:FA6C8523 / permanent C4F5D8B270EB, lines 121–130.
- **Hypothesis audited:** p=G_Ω μ **finite everywhere**; comparison on supp μ outside a polar set.
- **Complete counterexample to an unprinted weakening:** Ω=B(0,1), μ=δ_0, p=G_B(·,0). Then p(0)=+∞, p>0 elsewhere; w=ηp for 0<η<1 satisfies w≥p at supp μ as +∞≥+∞ but fails everywhere else, even with no polar exception. Alternatively w=0 works if Z={0} is excluded. p is finite a.e.; p∈Lq for all finite q in d=2 and precisely 1≤q<d/(d−2) in d≥3.
- **Disposition:** do not change the printed theorem. If desired, add a caution against a.e.-finite or Lq replacements by separate reviewable patch. Related polar support and sweeping dependents remain conditional on their own hypotheses.
- **Unresolved inputs not misclassified as repaired:** Lusin continuous-potential decomposition and boundary behavior of compact Green potentials in lines 127–130 were not independently proved here.
- **Coverage:** existing partial §4.3; selected 4.3.10 newly inspected and elementary Green model proved; +0 first-visited numbered sections; +0 entire-section certifications.
- **Excluded work:** Demailly regularization and its dedicated Bergman/L²/OT/multiscale/positivity-loss programme remains deferred-by-user.
- [Full anchored report](../reports/2026-11-17-classical-domination-polar-pole-finiteness.md).
