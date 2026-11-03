# Additive classification ledger — 2026-11-03 polar Martin point and compact sweep

| Field | Value |
| --- | --- |
| Stable ID | POME-MART-PUNCTURE-SWEEP-PERRON-POLAR-001 |
| Production main reviewed | b6933b772f41b45918f7e25ed1afbbb1fd892272 |
| Severity | Low |
| Status | **verified conditional deduction** (not confirmed error, not proof gap, not complete theorem certification) |
| Main integrated path | docs/sections/green-energy-and-martin-boundaries/index.html |
| Main blob | 976a90f2a5eba299658f73a1eee8b9d3fef8020f |
| Primary anchors | Lemma 4.5.10 source classical-potential-theory:F432655F / permanent B0A113187C30 / physical lines 126–149; Theorem 4.5.12 source classical-potential-theory:57D18B4C / permanent 6736FBE7368C / lines 165–185; Theorem 4.5.13 source classical-potential-theory:854603A2 / permanent 0E65F552B1A6 / lines 189–214 |
| Normalization context only | Lemma 4.5.8 source classical-potential-theory:AB110663 / permanent D878F27BAB16 / lines 94–102; Theorem 4.5.9 source classical-potential-theory:1677A9F0 / permanent 9D6B5CF5E0CF / lines 106–122 |
| Specific hypotheses | Omega=D minus {0}, reference 0<abs(a)<1, b=phi(G_D(.,a)) equals G_D(.,a) near 0, inner circle C_r of sufficiently small radius r<abs(a), ordinary Dirichlet Green convention G_D=kappa log abs((1-conj(w)z)/(z-w)) |
| New verified calculation | Rhat_{C_r} K_0=log(1/max(abs(z),r))/log(1/abs(a)); gamma_{0,C_r}=[b(t)/(kappa log(1/abs(a)))] sigma_r(dt) is a probability measure but generally not uniform; gamma_{0,C_r} converges weakly to delta_0 in Martin space. Continuous Perron data at the polar minimal point 0 have no effect on the solution, and the representing measure chi of 1 assigns zero mass there. |
| Correct versus false / missing | Printed Theorems 4.5.12–13 and Lemma 4.5.10 survive this model; no false theorem or missing general proof established. |
| Nonduplication boundary | Prior POME-MART-EXTERIOR-BALL-INFINITY-001 already calculated the Kelvin-equivalent puncture/end **kernel**; do not recertify it as new. This record instead proves exact cutoff-weighted compact reduction and Perron polar-data invisibility. Previous POME-MART-SWEEP-PROJECTIVE-001 is a distinct abstract consistency claim. |
| Proposed correction | Optional editorial example after 4.5.13 distinguishing minimal Martin point from positive harmonic measure, showing explicit finite-r b-weighted sweep. No source/body edits. |
| Affected dependents | 4.5.10 compact reduction normalization, 4.5.12 sweeping-limit and minimal representation interpretation, 4.5.13 continuous Perron resolutivity |
| Unresolved inputs | General Martin representation and sweeping on arbitrary Greenian domains, fine-polar-removability prerequisites as stated internally, no entire §4.5 proof certification |
| User exclusion | Demailly approximation/regularization and dedicated Bergman, weighted L2, OT, multiscale atlas and positivity-loss work stay **deferred-by-user**, not resolved or certified |
| Report | [Full derivation](../reports/2026-11-03-punctured-disk-polar-martin-sweep-and-perron.md) |
| Coverage | Additional distinct model proof in previously sampled §4.5; no first-reviewed numbered section and no whole-section certification; actual 25 chapters / 747 numbered ToC sections / zero complete-section certificates |

No build, tests, CI, formalization, source edits, main pushes or website publication performed.
