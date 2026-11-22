# Mathematical audit — strict topology of inverse-limit cohomology and a cross-section rotation

Date: 2026-11-22. Reviewed production **main**: \`b6933b772f41b45918f7e25ed1afbbb1fd892272\` (checked against the current remote ref).
Audit branch only: \`review/mathematical-audit\`. The chapter/section inventory remains **25 / 747**; its legacy-unknown states are not interpreted as unreviewed.

## Finding POME-INVLIMIT-COHOMOLOGY-STRICT-TOPOLOGY-001

**Severity:** low. **Status:** verified conditional deduction. **Not** an original false theorem, an unconditional repair, or a certification of all upstream mathematics.

**Source:** \`docs/sections/open-maps-nuclear-spaces-and-inverse-limits--cohomology-of-countable-inverse-limits/index.html\`, blob \`30e6e5800601450ce52d9c01dc5abea06a403d6e\`, main physical lines 7–187. In particular Theorem 2.14.4, lines 77–119, source \`demailly-complex-geometry:3D7EF38C\`, permanent tag \`50E84369B7A2\`; Theorem 2.14.6, lines 122–159, source \`demailly-complex-geometry:7A48110C\`, permanent \`10E2183C49C3\`. Internal Fréchet open-map/quotient theorem 2.12.1, \`docs/sections/open-maps-nuclear-spaces-and-inverse-limits--open-maps-compact-perturbations-and-finite-cohomology/index.html\`, lines 13–29, source \`demailly-complex-geometry:F97537CF\`, permanent \`71B16A3EF23E\`.

### Statement (conditional topological strengthening)

Let \((E_\nu^\bullet,r_\nu)_{\nu\ge0}\) be a countable inverse system of complexes of Hausdorff complex Fréchet spaces. Suppose all bonding maps are **degreewise dense** and, for a fixed degree \(q\):

1. \(B^q(E_\nu)=d(E_\nu^{q-1})\) is **closed** in \(Z^q(E_\nu)\) for every \(\nu\) (equivalently, every \(H^q(E_\nu)\) is Hausdorff);
2. the bonding maps \(H^{q-1}(E_{\nu+1})\to H^{q-1}(E_\nu)\) have dense image.

Then **\(B^q(E)\) is closed in \(Z^q(E)\)** for \(E=\varprojlim E_\nu\), and the canonical map
\[
  \Theta^q:H^q(E)\longrightarrow\varprojlim H^q(E_\nu)
\]
is a **topological isomorphism of Fréchet spaces**, not just an algebraic bijection. Both sides use exactly the quotient/subspace topologies stated in §2.14.

### Complete deduction under the stated hypotheses

Every \(Z^q(E_\nu)\) is a closed Fréchet subspace. Hypothesis (1), together with Proposition 2.12.1, makes \(H^q(E_\nu)=Z^q(E_\nu)/B^q(E_\nu)\) a Hausdorff Fréchet space. Its countable inverse limit \(K\) is a closed subspace of their product and hence Fréchet and Hausdorff.

By the degreewise-density assumption and Theorem 2.14.4, \(\Theta^q:H^q(E)\to K\) is surjective; hypothesis (2) invokes precisely its additional injectivity clause, so \(\Theta^q\) is algebraically bijective and continuous. Write \(Z=Z^q(E)\), a Fréchet space since \(E\) is the degreewise closed inverse limit. The composite
\[
  L: Z\twoheadrightarrow H^q(E)\xrightarrow{\ \Theta^q\ }K
\]
is continuous and satisfies \(\ker L=B^q(E)\), because \(\Theta^q\) is injective. Since \(K\) is Hausdorff, the kernel is **closed** in \(Z\), proving the additional closed-range assertion without assuming it at the limit level. Thus \(H^q(E)=Z/B^q(E)\) is itself Fréchet. The continuous bijection \(\Theta^q\) between these two Fréchet spaces is open by Proposition 2.12.1, so its inverse is continuous. This proves the topological claim. There is **no** use of weak sequential compactness or an illicit interchange of inverse limits and closures.

Example: complexes supported in degree \(q\), with \(E_\nu^q=\mathbb C^{\nu+1}\) and surjective coordinate-truncation bonds, satisfy the hypotheses. The resulting isomorphism identifies both cohomologies with \(\mathbb C^{\mathbb N}\) in their **product Fréchet topology**, so the conclusion is not limited to finite-dimensional cohomology.

**Why the extra assumption matters:** The printed Theorem 2.14.4 intentionally works with possibly non-Hausdorff cohomology. Without closed finite-stage boundaries, the inverse-limit target is not known to be a Hausdorff Fréchet space, and the Fréchet open mapping argument above is unavailable. This report does *not* assert that the topological conclusion always fails without hypothesis (1).

**Suggested source change (proposal only):** insert an optional corollary after Theorem 2.14.4 with exactly the two additional hypotheses; record the resulting automatic closedness of limit boundaries. Do not replace the stronger-in-generality original theorem. **Dependents:** topological variants of the abstract Mittag–Leffler conclusion in Theorem 2.14.6, strict inverse-limit cohomology comparisons, and continuous dependence arguments requiring actual quotient topologies. No production text was edited.

## Direct reading scope and checks

### §2.12 — Open maps, compact perturbations and finite cohomology

Whole integrated section directly read: \`docs/sections/open-maps-nuclear-spaces-and-inverse-limits--open-maps-compact-perturbations-and-finite-cohomology/index.html\`, blob \`dd12ea5ca837e3ec507930eeed8a0eb38bd3f6a4\`, physical mathematical lines **7–119**. Proposition 2.12.1 \`F97537CF/71B16A3EF23E\`: quotient completeness via diagonal representatives; open mapping by Baire and successive corrections; closed graph via a graph projection. Corollary 2.12.2 \`BCEF25A2/181D2DF97074\`: finite-codimensional image **of a continuous Fréchet map** is closed, not an arbitrary algebraic subspace. Theorem 2.12.3 \`5C1FDFEE/E27FE1F7DE85\`: finite-functional cutoff of compact images, neighborhood compactness (not merely bornological compactness), closed embedding using a convergent **subnet**, and the Fréchet requirement of the quasi-epimorphism half. Theorem 2.12.5 \`77D28452/D8E2BCEBC75D\`: compact perturbation of the open cycle-plus-boundary map and the quotient-topological openness conclusion. No newly confirmed error. Earlier finite-rank Fredholm index audit of 2026-11-07 remains separately classified and is not repeated here.

### §2.14 — Cohomology of countable inverse limits

Whole current integrated mathematical section directly read, \`docs/sections/open-maps-nuclear-spaces-and-inverse-limits--cohomology-of-countable-inverse-limits/index.html\`, blob \`30e6e5800601450ce52d9c01dc5abea06a403d6e\`, physical lines **7–187**. Lemma 2.14.2 \`AAE7DFD2/139720D2EFCA\` uses summably approximate lifts and consistent complete metrics; Lemma 2.14.3 \`2FF64411/86AC6A041C11\` uses the **actual**, possibly non-Hausdorff quotient topology. Theorem 2.14.4 \`3D7EF38C/50E84369B7A2\` controls both the error and its primitive in equation 2.14.5 (permanent \`F2EC9B6D00D9\`), which is essential when boundaries are not closed; the injectivity proof invokes cohomology-density one degree lower. Theorem 2.14.6 \`7A48110C/10E2183C49C3\` preserves the distinction between surjective, dense and injective bonding maps; Proposition 2.14.7 \`CD05CCE6/F529678A1F94\` specifically requires dense **kernel** transitions. The earlier 2026-11-10/11 sharpness examples (surjectivity-density and injectivity-shift findings) are not re-registered. No newly confirmed false printed assertion.

### §2.23 — Completions and locally convex quotients

Full **recheck**, *not* first-time full coverage: \`docs/sections/completions-and-locally-convex-quotients/index.html\`, blob \`e2c6d25d35020ccefa739f04aa893e173f73c17e\`, mathematical lines **7–120**. Lemma 2.23.1 \`C85CEBC0/0628F713D150\` uses Cauchy **nets** in the finest locally convex topology. Example 2.23.2 \`B6DA08BE/D7A9E3E20E73\` correctly distinguishes closures of neighborhood images from openness of the underlying map. Lemma 2.23.3 \`69616994/5F1410BEA2F7\` uses a locally compact ordinal plank and an incomplete quotient of a complete compact-open function space; Example 2.23.4 \`8F41A0A7/B0973308F142\` explicitly does **not** establish failure with all four factors complete. Proposition 2.23.5 \`5740E9A4/6118C797DA34\` concerns Fréchet strict epimorphisms only. Existing 2026-11-20 completeness and ordinal-plank records remain unchanged. No new confirmed printed error.

### §16.7 — Comparison of singularities

Whole brief structural section directly read: \`docs/sections/comparison-of-singularities/index.html\`, blob \`65883f4ebc5ac5e3612212dceda85467eeb84d7b\`, lines **5–23**. Definition 16.7.1 source \`sgpt:410CBDE6\`, permanent \`3E4D57445698\`: the ordinary quasi-psh singularity comparison is an additive-constant preorder; the introductory transition to P and multiplier-ideal preorders and to the ray pseudometric preserves, rather than identifies, the different equivalence classes. This is **introductory/definitional** coverage, not an audit of all §16.8 or §16.9 statements.

### §2.13 — narrow prerequisite read only

Selected Theorem 2.13.5, \`docs/sections/open-maps-nuclear-spaces-and-inverse-limits--nuclear-spaces-and-completed-tensor-products/index.html\`, blob \`ecbf01a4ed81461ba32f1e0c88c6a550ebaa8135\`, lines **138–158**, source \`demailly-complex-geometry:A161219A\`, permanent \`7434BE36F417\`, for the **projective quotient** argument used by Proposition 2.23.5. This does not reopen, review or certify Bergman restrictions or any dedicated regularization/L²/OT proof-completion programme. §2.13 **not** counted as a whole-section review.

## Classification, unresolved items, and scope boundaries

- New classified finding: **one low / verified conditional deduction**, POME-INVLIMIT-COHOMOLOGY-STRICT-TOPOLOGY-001. It has a complete deduction from specifically stated internal theorems, but those entire transitive proof chains have **not** been independently certified.
- New confirmed false source theorems: **zero**. New confirmed original proof gaps: **zero**. New mathematical duplicates: **zero**. New unproved external dependencies: **zero**.
- Theorem 2.14.4's original non-Hausdorff generality remains important. The topological upgrade requires **all stated additional conditions**; it is not an unconditional proof repair.
- Historic reports about finite-rank perturbations, inverse-limit density thresholds, finest-topology completeness and ordinal plank examples are **retained**, not counted as new discoveries.
- User-excluded Demailly approximation/regularization and its Bergman, L², Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof-completion programme remain **deferred-by-user**, neither resolved nor certified. No excluded proof completion was undertaken.
- **Exact incremental direct coverage:** three whole current mathematical sections (§§2.12, 2.14, 16.7, of which the last is brief/definitional); one whole **repeat** (§2.23); one **selected** prerequisite (§2.13). **Zero** fully certified transitive proof chains. No first-ever-visit claim.
- No tests, build, CI, automatic merge, website publication, registry/source/canonicalization/permanent tag or main modifications were performed. Changes are audit notes only.
