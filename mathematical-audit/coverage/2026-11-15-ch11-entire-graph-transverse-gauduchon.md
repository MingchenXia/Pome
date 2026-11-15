# Exact chapter/section coverage delta: 2026-11-15, Chapter 11 §11.8

**Reviewed main:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`; **actual ToC:** 25 chapters and 747 numbered sections.

| Section and current entry | Exact main integrated source | Depth of new review | Result and nonclaim |
| --- | --- | --- | --- |
| **11.8**, setup | \`docs/sections/gauduchon-metrics-and-linear-mass--transverse-concentration-of-gauduchon-tests/index.html\` blob \`93c2b63848b752f3ef660c1bcd599d0be1bc1e40\`, physical lines 5–22, source \`non-kahler-pluripotential-theory:22A7F863\`, permanent \`959649DAC54D\` | Direct read of normalized test cone, local product coordinates, kernel normalization, \(B_\delta\), \(C_\delta\) | Correct form/normalization on graph chart |
| **11.8.1**, Theorem | Same blob, lines **25–53**, source \`non-kahler-pluripotential-theory:8F4DC027\`, permanent \`B0762464DCDC\` | Reread Lamari/\(L^1\)/Siu dependence and global component conclusion; apply to entire graph | Conditional use, not upstream theorem certification |
| **11.8.2**, Proposition | Same blob, lines **55–81**, source \`non-kahler-pluripotential-theory:79BF143E\`, permanent \`26C9605156BE\` | Independently check full-chart Cartier agreement, \(\delta^2/(|\zeta|^2+\delta^2)^2\), and \(4P/\epsilon\) bound | Correct, conditional and localized |
| **11.7.1**, context only | \`docs/sections/gauduchon-metrics-and-linear-mass--compactness-and-duality-of-gauduchon-currents/index.html\` blob \`31d17f258f2ff178bf52be3d3f92d5a995878d3a\`, source \`non-kahler-pluripotential-theory:C21ACA47\`, permanent \`155386134D9E\` | Background normalized cone, not a new full proof | No new certification of §11.7 |

**New finding:** \`POME-GAUD-TRANSVERSE-ENTIRE-GRAPH-DICHOTOMY-001\`, low / verified conditional deduction. A fixed affine graph \(\zeta=w-f(z)\) in \(\mathbf P^2\), \(f\) entire, has uniformly bounded \(C_\delta\) precisely for polynomial \(f\); for nonpolynomial \(f\) the full limit diverges. The negative argument is not based on the mere presence/absence of global divisors: it proves the topological projective closure of a transcendental entire graph contains the entire line at infinity, excluding containment in an irreducible global analytic curve. [Full hypotheses and proof](../reports/2026-11-15-gauduchon-transverse-entire-graph-dichotomy.md).

**Matrix accounting:** prior §11.8 already marked selected/partly audited on 2026-10-22. This run adds **zero** newly first-visited numbered sections and **zero** whole-section certifications; all remaining Chapter 11 results retain their earlier statuses. No tests, build, CI or publishing performed. The excluded Demailly approximation/regularization and dedicated Bergman/L2/OT/multiscale/positivity-loss programme remains deferred-by-user.
