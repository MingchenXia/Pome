# Tangential complete intersections and a detached malformed alignment

**Audit date:** 2026-11-01. **Production main reviewed:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`.
**Audit branch:** \`review/mathematical-audit\`, based on its existing history; no reset.
**Actual selected review:** the integrated reading edition of §§7.28.1, 7.30.1/.3, and 20.5.5/.10. Context: §7.12.1 (the prior finite-family inequality is **not** a new finding). All dedicated Demailly approximation/regularization, Bergman, L², Ohsawa–Takegoshi, multiscale-atlas and positivity-loss work is expressly **deferred-by-user** and has not been examined.

## POME-HAUS-ORPHAN-ALIGN-001 — low / confirmed error (reading-edition representation, not a false theorem)

**Exact main file:** \`docs/sections/classical-products-with-controlled-unbounded-loci--classical-products-under-hausdorff-intersection-conditions/index.html\`; Git blob \`9cde5bfdeb2e3c0457216278945df46eb230e42b\`.

At **physical lines 35–40**, the statement of Proposition **7.30.3** (source \`demailly-complex-geometry:A5207F44\`, permanent tag \`1AC7DC75B159\`) displays two estimates in a single \`align\` environment. The source equation group is \`demailly-complex-geometry:4D770B18\`, permanent tag \`1D4FB6D7DCBB\`; its second row ends in the explicit source-numbered \`\tag{7.30.6}\`. The mathematical inequality is valid *as stated*, subject to the proposition's hypotheses and its unrecertified proof.

At **physical line 157**, after the proof has already ended, a separate \`reading-chunk\` is emitted with id \`entry-FB8CDED199AB\`, source \`demailly-complex-geometry:9EEEF3B3\`, and permanent tag **\`FB8CDED199AB\`**. It repeats *precisely the second inequality* from line 38 and hard-codes the same \`\tag{7.30.6}\`. Its math source has the forbidden nested display structure

\`\`\`tex
\[\begin{aligned}\begin{align}
  \|dd^c u_1\wedge\cdots\wedge dd^c u_q\wedge T\|_L
   &\le C\|T\|_K\prod_j\sup_{K\setminus V_j}|u_j|.
  \tag{7.30.6}
\end{align}\end{aligned}\]
\`\`\`

An \`align\` display cannot be nested inside \`aligned\` inside \`\[...\]\`; this is a source-level TeX/MathJax syntax defect, independent of whether a browser happens to mask its error. The duplicate is also an independent orphaned reading step after the end of the proof, with a second occurrence of the source number rather than a generated, canonical equation locator.

**Proposed correction (not applied):** Trace the source-equation registry and canonical placement for the separate \`9EEEF3B3\` formula. Keep both permanent tags \`1D4FB6D7DCBB\` and \`FB8CDED199AB\` and both provenance labels resolvable; map the latter to the canonical second-row equation or a specific row anchor within the first group, with the generated current Pome equation numbering. Remove the duplicate *display* and improper nesting through a separately reviewable production patch, **not** by deleting the independent tag or hand-editing \`docs/\`. Check links from §7.28.1, Proposition 7.30.3 and any equation references. No mathematical change to the estimates, no claim that the theorem is false. **Status:** unresolved, proposed production repair only. **Related history:** earlier Hausdorff-subfamily sharpness \`POME-BT-HAUSDORFF-SUBFAMILY-SHARP-001\` remains a distinct mathematical finding.

## POME-CI-TANGENT-MULTIPLICITY-001 — low / verified conditional deduction (new nontransverse model)

**Integrated anchors:**
- \`docs/sections/classical-products-with-controlled-unbounded-loci/index.html\`, blob \`21dc39a9b02a4c1820f081a0c3a82e9f8ffca727\`: Theorem **7.28.1**, source \`demailly-complex-geometry:F96C3380\`, permanent \`1BBBF8109419\`, lines **6–22**.
- \`docs/sections/classical-products-with-controlled-unbounded-loci--classical-products-under-hausdorff-intersection-conditions/index.html\`, blob as above: Proposition **7.30.3**, source \`demailly-complex-geometry:A5207F44\`, permanent \`1AC7DC75B159\`, Hausdorff condition equation source \`3115851B\`, permanent \`E561BB270A1B\`, lines **29–40**.
- \`docs/sections/divisors-and-logarithmic-limits-on-analytic-cycles/index.html\`, blob \`dae567406b2030e550664ca57b1fe77911d956d4\`: Theorem **20.5.5**, source \`demailly-complex-geometry:D58680EB\`, permanent \`F1C928146DBC\`, lines **63–69**, and Theorem **20.5.10**, source \`demailly-complex-geometry:34D8935D\`, permanent \`DDB973C0C1DD\`, lines **132–149**.

In a small bidisc in \(\mathbb C^2\), let \(z,w\) denote the coordinates and take **arbitrary integers** \(a,b,k\ge1\). Set

\[
u_1=a\log|z|^2,\qquad u_2=\log|w^b+z^k|^2,\qquad T=1.
\]

The unbounded loci are the supports of \(Z_1=\operatorname{Div}(z^a)\) and \(Z_2=\operatorname{Div}(w^b+z^k)\). For \(p=q=2\), every singleton intersection has real Hausdorff dimension at most \(2<3=2p-2+1\); the common intersection is \(\{0\}\), so its \(\mathcal H^1\) measure is zero. Thus **all** of the exact subfamily conditions of Proposition 7.30.3/ Theorem 7.28.1 hold, including in tangent or reducible configurations. No normal-crossings or transversality assumption is added.

With Pome's \(dd^c=(i/2\pi)\partial\bar\partial\), the normalized Poincaré–Lelong identity gives \(dd^cu_1=a[z=0]\). On the smooth line \(\{z=0\}\), the second potential restricts to \(b\log|w|^2\), which is locally \(L^1\) for the line current. The cycle-restriction recursion of Theorem 20.5.5 therefore gives the **exact classical product**

\[
\boxed{\quad dd^cu_1\wedge dd^cu_2
=a\,dd^c\!\left(\log|w^b+z^k|^2\,[z=0]\right)
=ab\,\delta_{(0,0)}.\quad}
\]

This is also the local algebraic intersection number: the Artinian ring
\[
\mathbb C\{z,w\}/(z^a,w^b+z^k)
\]
has the \(\mathbb C\)-basis \(z^iw^j\), \(0\le i<a\), \(0\le j<b\). Indeed \(z^a=0\) and the monic relation \(w^b=-z^k\) reduce every series to a unique such normal form; polynomial division by the monic relation proves independence. Its colength is **\(ab\)**, independent of the tangency exponent \(k\). In particular the coefficient is not falsely replaced by \(a\), \(b\), or by a transversality-only count.

The **non-pluripolar** product of these two divisorial currents is zero on the bidisc: outside their polar divisors both currents vanish, and its definition discards the pole sets. The distinction between classical and non-pluripolar products is already a recorded phenomenon for transverse coordinate divisors; **this tangential multiplicity-\(ab\) family is a separate exact benchmark**, not a rediscovery of \`POME-BT-HAUSDORFF-SUBFAMILY-SHARP-001\`.

**Independent small check performed:** SymPy lexicographic Gröbner bases were computed for \((a,b,k)=(1,1,1),(2,3,1),(3,2,5),(4,5,2),(5,4,7)\). In each case the initial ideal is \((w^b,z^a)\), giving colengths \(1,6,6,20,20\) respectively. This is a **finite exact-arithmetic check only**; the argument above, not the five computations, proves the general family.

**Adjudication:** Theorems 7.28.1, 20.5.5 and 20.5.10 and Proposition 7.30.3 are **not shown false**. The result is an explicit conditional consistency/sharpness test of the existing integrated cycle-product and normalization claims, relying on the stated internal Poincaré–Lelong/cycle-restriction results. This is **not** a whole-theorem proof-chain certification. It supplies a candidate optional example after Theorem 20.5.10 and checks the intersection-multiplicity convention for dependent §20.6 cycle computations; no production change was made.

## Scope, ledger and verification

New focused work: inspect the detached equation at **§7.30 line 157**, compare to Proposition 7.30.3 at **lines 35–40**, and verify the tangent divisor model against the **actual** Theorems 7.28.1 and 20.5.5/.10. The wider §7.30 proof and all dependency chains were **not** recertified; §7.12 was merely cross-checked and contains an **older** separate finite-family finding. The actual ToC remains **25 chapters, 747 numbered sections, zero complete mathematical sections certified**. All old confirmed errors, proof gaps, external dependencies, conditional repairs and \`deferred-by-user\` entries remain in their existing states.

Only the four audit Markdown deliverables are proposed for \`review/mathematical-audit\`. No changes to \`main\`, source books, \`docs/\`, registries, permalinks or canonicalization; no GitHub Actions, site publication, build, formal verification, or whole-project tests. No excluded approximation/Bergman/L²/OT/multiscale/positivity-loss work was touched.
