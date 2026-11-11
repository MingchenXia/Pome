# Finding ledger — inverse-limit cohomology injectivity sharpness (2026-11-11)

| Field | Verified entry |
| --- | --- |
| Stable finding ID | \`POME-INV-LIM-COHOM-INJECTIVITY-SHIFT-001\` |
| Severity / status | **low / verified conditional deduction** |
| Printed theorem error? | **No.** Theorem 2.14.4 expressly includes the missing \(H^{q-1}\)-density assumption. |
| Reviewed production main | \`b6933b772f41b45918f7e25ed1afbbb1fd892272\` |
| Integrated source file | \`docs/sections/open-maps-nuclear-spaces-and-inverse-limits--cohomology-of-countable-inverse-limits/index.html\` |
| HTML Git blob | \`30e6e5800601450ce52d9c01dc5abea06a403d6e\` |
| Exact anchors | §2.14 introductory conventions lines 5–16; Theorem 2.14.4 lines 77–83, proof 85–118; Theorem 2.14.6(3) lines 123–139, proof 142–159; Proposition 2.14.7 lines 162–185 |
| Stable source and permanent tags | \`demailly-complex-geometry:3D7EF38C\` / \`50E84369B7A2\`; \`:7A48110C\` / \`10E2183C49C3\`; \`:CD05CCE6\` / \`F529678A1F94\` |
| Exact hypotheses tested | All stage complexes Hilbert; every degreewise bonding map surjective; **induced \(H^0\) bonding map not dense**; equivalently the kernel bonding map is the right shift \(R\), not dense |
| Fully checked countermodel | \(E_\nu^0=H\oplus H\xrightarrow{\mathrm{pr}_2}E_\nu^1=H\), \(r^0(h,y)=(Rh+y_0e_0,Ly)\), \(r^1=L\), \(H=\ell^2(\mathbb N_0)\), \(LR=I\) |
| Conclusion | All \(H^1(E_\nu)=0\) but \(H^1(\varprojlim E_\nu)=\mathbb C^{\mathbb N}/\ell^2\ne0\); nonclosed boundaries, reduced cohomology zero; inverse limit of stagewise short exact sequences fails right-surjectivity without kernel density |
| Proposed correction | **None to statements/proofs.** Optional explicit sharpness note next to Theorem 2.14.4 and Proposition 2.14.7 |
| Affected dependents | Any application dropping induced \(H^{q-1}\)-density from 2.14.4/.6(3), or dropping kernel density in 2.14.7; no printed dependent is hereby declared false |
| Prior distinct finding | \`POME-INV-LIM-COHOM-SURJECTIVITY-DENSITY-001\` (2026-11-10) concerns **surjectivity** of the inverse-limit cohomology map without **degreewise** density, not injectivity under degreewise surjectivity |
| Deferred-by-user | Demailly approximation/regularization, dedicated Bergman/\(L^2\)/Ohsawa–Takegoshi/multiscale/positivity-loss proof completion remain deferred, neither resolved nor certified |

**Proof:** [source-anchored report](../reports/2026-11-11-inverse-limit-cohomology-injectivity-sharpness.md).

No full proof-chain certification, source-code or reading-edition edits, CI/build, or publication.
