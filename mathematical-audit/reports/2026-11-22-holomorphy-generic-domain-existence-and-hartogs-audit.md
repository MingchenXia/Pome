# Domains of existence are residual: whole-section Chapter 9 audit (2026-11-22)

**Production baseline:** main \`b6933b772f41b45918f7e25ed1afbbb1fd892272\` (unchanged). **Audit branch:** \`review/mathematical-audit\`. **Scope:** complete *current integrated reading-edition* mathematical bodies of §§9.12–9.15, not a certification of every transitive prerequisite and not a claim of first historical inspection. All source scans and the excluded Demailly/Bergman/L²/Ohsawa–Takegoshi/multiscale/positivity-loss programme were left untouched.

## Anchored input inventory

| Section | Exact integrated page (on baseline main) | Git blob SHA | Physical lines and stable source/permanent identifiers |
| --- | --- | --- | --- |
| §9.12 Separate holomorphy | \`docs/sections/separate-holomorphy/index.html\` | \`2eafedb77d4a45f0133a5d92e27ad16b0be44ffd\` | Theorem 9.12.1, lines 7–53, source \`klimek-pluripotential-theory:120C7FB1\`, permanent \`362351A63FB6\` |
| §9.13 Hulls and domains | \`docs/sections/holomorphic-hulls-and-domains-of-holomorphy/index.html\` | \`f2bbaea02a3b85847acc503b83d0cf4dfa11e9d0\` | Proposition 9.13.1, lines 16–38, source \`klimek-pluripotential-theory:5FBBEDD6\`, permanent \`36B688C7F361\`; Theorem 9.13.2, lines 51–89, source \`klimek-pluripotential-theory:18A483AD\`, permanent \`8FBCDB96A2E2\` |
| §9.14 PSH hulls/boundary gauges | \`docs/sections/plurisubharmonic-hulls-and-general-boundary-distances/index.html\` | \`9b491cd7d9fcb7adb3b43c8daf2d8a29a0ed4077\` | Proposition 9.14.1, lines 13–47, source \`klimek-pluripotential-theory:DAAFC667\`, permanent \`D1E020BB8CEA\`; Proposition 9.14.2, lines 49–60, source \`klimek-pluripotential-theory:ADFB854F\`, permanent \`CE8195E08F54\` |
| §9.15 Complete Hartogs domains | \`docs/sections/complete-hartogs-domains-and-taylor-coefficients/index.html\` | \`641a66c419e4a1f7207cd301b51f27f3a6efd6f9\` | Proposition 9.15.1, lines 7–31, source \`klimek-pluripotential-theory:7CA9E7D7\`, permanent \`202C805DC8A2\` |

The anchors refer to physical lines in the one-line-heavy HTML blobs. This report reads those generated *mathematical* bodies, not merely source theorem titles.

## POME-HOLOMORPHY-GENERIC-DOMAIN-EXISTENCE-001

**Classification:** low severity / **verified conditional deduction**, **not a false source theorem**. The printed Theorem 9.13.2 states the existence of *one* function having a holomorphically convex open subset of \(\mathbb C^n\) as its domain of existence. Its proof in lines 84–88 actually gives the following category-theoretic strengthening.

**Claim.** If \(\Omega\subset\mathbb C^n\) is any nonempty holomorphically convex open set (disconnected is allowed), equip the Fréchet space \(\mathcal O(\Omega)\) with the compact-open topology. The subset
\[
 \mathcal N_\Omega=\{f\in\mathcal O(\Omega):
       \text{\(\Omega\) is a domain of existence for \(f\) in the precise sense of §9.13}\}
\]
is **dense \(G_\delta\)**. Equivalently the set of holomorphic functions admitting an extension from *some* nonempty local piece to *some* connected open set crossing \(\partial\Omega\) is **meagre**. More precisely, \(\mathcal N_\Omega\) itself (not just a dense subset thereof) is a countable intersection of open dense sets. The converse holds too: if \(\Omega\) is not a domain of holomorphy under §9.13's definition, \(\mathcal N_\Omega\) is empty. The empty-boundary case \(\Omega=\mathbb C^n\) gives \(\mathcal N_\Omega=\mathcal O(\Omega)\).

**Complete argument, conditional only on the printed §9.13.1 interpolation theorem.** Fix countably many *rational* Euclidean balls \((b,B)\) with \(\overline b\subset B\cap\Omega\) and \(B\not\subset\Omega\). For \(N\ge1\) let
\[
 E_{b,B,N}=\left\{f\in\mathcal O(\Omega):\
 \exists F\in\mathcal O(B),\ \sup_B|F|\le N,\
 F|_b=f|_b\right\}.
\]
This is closed. Indeed, for compact-open convergence \(f_j\to f\), a sequence of corresponding \(N\)-bounded extensions is a normal family on \(B\). Montel gives a subsequence converging locally uniformly to an \(N\)-bounded \(F\in\mathcal O(B)\), whose restriction to \(b\) equals \(f\). The Fréchet topology is metrizable, so sequential closedness suffices.

It has empty interior. Let \(W\) be the connected component of \(B\cap\Omega\) containing \(b\). Since \(W\) is nonempty and proper in connected \(B\), it has an interior-to-\(B\) boundary point \(a\in\partial\Omega\cap B\). Choose distinct \(z_j\in W\) tending to \(a\); these form a closed discrete set in \(\Omega\). By the printed interpolation part of Proposition 9.13.1, a holomorphic \(h\) exists with \(h(z_j)=j\). It cannot extend from \(b\) to \(B\), because the identity theorem on \(W\) would force any such extension to agree with \(h\) on \(W\), yet a holomorphic function on \(B\) is bounded near \(a\), contrary to \(h(z_j)=j\). If \(E_{b,B,N}\) contained an open neighborhood of \(f_0\), it would contain both \(f_0\) and \(f_0+\varepsilon h\) for sufficiently small nonzero \(\varepsilon\); subtracting their \(B\)-extensions would extend \(h\), a contradiction.

The countable union \(\bigcup_{b,B,N}E_{b,B,N}\) is therefore meagre; its complement is dense \(G_\delta\) by Baire, since \(\mathcal O(\Omega)\) is Fréchet. This complement is **exactly** \(\mathcal N_\Omega\). Membership in any \(E_{b,B,N}\) witnesses failure of the domain-of-existence property. Conversely, an extension from a nonempty \(V\subset U\cap\Omega\) to connected \(U\) crossing the boundary agrees by identity on the component \(W\) containing \(V\); an interior boundary point in \(U\) and suitably small rational balls \(b\Subset W\cap B\Subset U\) produce an \(E_{b,B,N}\) containing \(f\), since the extension is bounded on a slightly smaller ball. (The endpoint component issue is explicitly handled: rational \(b\) need not lie in the original \(V\), only in that component \(W\).) Finally, if \(\Omega\) is not a domain of holomorphy, the *common* continuation datum in the printed definition applies to every \(f\), so \(\mathcal N_\Omega=\varnothing\).

**Why this is additional, but conditional:** the printed theorem asserts existence of one such \(f\); the proof above identifies the exact topological size and Borel complexity of all such \(f\). It uses the existing arbitrary-discrete-value interpolation in §9.13.1 and elementary normal families/Baire, *not* an independently certified proof of that proposition or of the higher-level holomorphic-convexity criterion. No changes to reader statements or tags are proposed.

**Affected dependents:** any use of §9.13.2's (holomorphic convexity \(\Rightarrow\) single-domain-of-existence function) implication can adopt the stronger generic version if desired. This is an optional mathematical-text improvement, not a necessary correction or a canonicalization change. Earlier ledger finding \`POME-HULL-JET-INTERP-001\` concerns jet interpolation and is **not** duplicated.

## Four whole-section proof-step review notes (no other newly confirmed errors)

1. **§9.12, lines 7–53:** with separate holomorphy, dimension induction makes the slices \(f(\cdot,t)\) holomorphic; the closed sets \(F_N\subset\overline D\) cover \(\overline D\), and Baire yields a bounded product patch. The coefficient functions \(c_j(z')\) are holomorphic and \(j^{-1}\log|c_j|\) are plurisubharmonic (allowing identically \(-\infty\)); their pointwise radius estimate and the locally uniform upper bound meet the Hartogs-lemma hypotheses needed for locally normal convergence. This is a review of a correct proof, not a claim to independently certify every result used by Hartogs' lemma.
2. **§9.13, lines 16–89:** the exhaustion's \(\sum|g_{\nu,l}^{p_\nu}|^2\) is smoothly locally summable by Hilbert-valued Cauchy estimates; successive finite interpolation polynomials vanish at preceding points; the proof treats arbitrary nonconvex **complex-homogeneous** boundary gauges, not merely norms. For such a gauge, uniform Cauchy estimates in each direction furnish homogeneous Taylor convergence on compact subsets of the balanced gauge ball, and the hull bounds pass through holomorphic test functions. No finite-generation/Stein assumption was inserted.
3. **§9.14, lines 13–60:** the PSH hull is closed because continuous PSH testing functions suffice by local convolution and maximum gluing; its compactness is supplied by a continuous PSH exhaustion. In the sublevel step, a limiting analytic disc lies in the ambient pseudoconvex \(G\), then the submean/maximum principle for the USC PSH function \(v\) keeps the disc in \(\{v<c\}\). The directional Oka argument referenced by this section remains a separately required upstream input. The previously logged general-gauge comparison \`POME-BOUNDARY-GAUGE-BOUNDED-PSH-001\` is unchanged.
4. **§9.15, lines 7–31:** the l.s.c. positive fiber radius yields an open complete Hartogs set; uniform fiber dilations over compact subsets give normally convergent holomorphic Taylor expansions. The coefficient-radius limsup equality needs the **domain-of-existence hypothesis**: without it only \((\limsup j^{-1}\log|c_j|)^*\le-\log R\) follows. We have not repeated earlier explicit Hartogs examples or natural-boundary findings.

**Status and bounds:** 4 present-main mathematical sections directly read in full; 1 *new* conditional deduction; 0 new confirmed statement errors; 0 complete transitive proof-chain certificates; no formal verification. No test/build/CI was run; no \`main\`, production body, source, proof registry, tags or published pages were changed. Demailly regularization and its dedicated Bergman/L²/OT/multiscale/positivity-loss programme remains **deferred-by-user**, not resolved/certified.
