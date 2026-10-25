# 2026-10-26 — sharp global generation, generic evaluation tuples, and the extension conic on \(\mathbf P^1\)

**Reviewed Pome main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. **Pre-write audit head:** `da5a0c6dc72accab2f22e5059ff6a4423a360f72`. This is a mathematical audit of selected *integrated reading-edition* proofs, not a certification of a chapter, source manuscript, or entire dependency chain. All findings below concern the portions expressly outside the author's deferred approximation programme.

## Primary integrated anchors and exact coverage

- `docs/sections/vector-bundles-connections-and-extensions--grassmannians-and-finite-generating-spaces/index.html`, blob `1e60418dd73f475dfee1b660f059c84a1ef1137b`: Proposition **10.35.1**, tag `C0EB2A25CDC8`, lines 10–40; Lemma **10.35.2**, tag `F9789093E482`, lines 42–64; Theorem **10.35.3**, tag `CD7786C05633`, lines 66–79; Proposition **10.35.4**, tag `0CE84812A13F`, lines 82–103; examples **10.35.5/6**, tags `75477746633A`/`384A806754ED`, lines 105–125. The Grassmannian chart, minor-rank argument, Baire step, global quotient metric assertion and nonproper example were read at the displayed proof level. The differential-geometric curvature prerequisite 10.34.9 was *not* transitively certified.
- `docs/sections/vector-bundles-connections-and-extensions--smooth-bundles-connections-and-holomorphic-extensions/index.html`, blob `a279d0fdc49429317a4772c932547934cc5c7f97`: Theorem **10.36.6**, tag `08655B144691`, lines 111–141; Proposition **10.36.7**, tag `CCF7A9609341`, lines 146–158; Corollary **10.36.8**, tag `DD24E61268DB`, lines 160–170; Theorem **10.36.10** and Equation **10.36.11**, tags `B7A8F8D8A536`/`3E0F17FBE3F5`, lines 181–220 (current orientation/sign checked); Proposition **10.36.12**, tag `84111D436822`, lines 222–248; Theorem **10.36.13**, tag `304DF496E0BF`, lines 250–270; Proposition **10.36.14**, tag `732A25F31FC3`, lines 272–300. The extension classification and explicit \(\mathcal O(-2)\hookrightarrow\mathcal O^2\) examples were checked directly. Earlier 10.36.1–5 were consulted only as notation; **not** fully reviewed.
- As an independent nonexcluded rotation: `docs/sections/classes-with-a-nonclosed-background/index.html`, blob `3cebca63712deb760cf2399c06ca1b5a37b6d851`: Proposition **10.30.2** `5F6B6BF8B562` lines 32–54, Theorem **10.30.4** `28C8F709D1CC` lines 67–89, Corollary **10.30.5** `9157A5A52988` lines 95–111, Proposition **10.30.10** `6436A9863EBA` lines 197–211. Checked the prescribed-derivative affine class, pushforward \(g_*\pi'^*\theta=\pi^*\theta\) as a current under degree-one modifications, and the exceptional correction's sign. The source's analytic-regularization results 10.30.7–8 (lines 127–190) are **deferred-by-user**, not reviewed here; 10.30.10's existence premise 13.14.18 is conditional.
- Internal elementary input: `docs/sections/hodge-theory-curvature-and-compact-vanishing--twisted-differential-forms-on-projective-space/index.html`, blob `1099020d78b8b36519f68ba31ce180c0d843f518`, Proposition **10.51.5** tag `74AA0E1253DB`, lines 70–92, and Theorem **10.51.6** tag `BEB304EB7449`, lines 94–108, together with divisor/line-bundle results in §10.78.5 (tag `5A999DD34D98`). These input statements were compared, not independently recertified.

## POME-GENSEC-GLOBAL-SHARP-001

**Severity:** low. **Status:** verified conditional deduction; printed Theorem 10.35.3 is **correct**. **Proposed edit:** add an optional optimality example after that theorem; do not modify its assumptions.

For every pair of integers \(n\ge1,\ r\ge1\), the bound \(n+r\) in the **global-generation** clause of Theorem 10.35.3 is the best possible uniform bound among rank-\(r\) bundles on complex \(n\)-manifolds, already for a projective base. Put
\[
 X=\mathbf P^n,\qquad E=\mathcal O_{\mathbf P^n}(1)\oplus\mathcal O_{\mathbf P^n}^{\oplus(r-1)}.
\]
The \(n+1\) coordinate sections of the first summand and the \(r-1\) constant unit sections of the second give \(n+r\) global generators.

Conversely suppose a \(p\)-dimensional section space \(V\subset H^0(X,E)\) generates at every point. Project its sections onto the trivial summand. This gives a **constant** linear map \(A:V\to\mathbf C^{r-1}\), necessarily onto. To generate a fiber vector in the \(\mathcal O(1)\) factor with zero trivial component at any point, the sections in \(\ker A\) must generate \(\mathcal O(1)\) globally. Under \(H^0(\mathbf P^n,\mathcal O(1))=(\mathbf C^{n+1})^*\), a proper linear subspace of linear forms has a nonzero common kernel vector; its forms simultaneously vanish at the corresponding projective point. Consequently any globally generating linear system has dimension at least \(n+1\). Hence
\[
 p-(r-1)=\dim\ker A\ge n+1,\qquad
 \boxed{p\ge n+r}.
\]
No Chern-class or external Bertini statement is needed. The same conclusion holds trivially at \(n=0\), with \(p\ge r\).

**Affected dependents:** the advertised generator bound 10.35.3 and classifying maps of 10.35.4, not the separate higher first-jet/pair bound. **No counterexample to the printed theorem.**

## POME-EVAL-RESIDUAL-GENERIC-001

**Severity:** low. **Status:** verified conditional deduction; strengthens the *quantifier* of Lemma 10.35.2, not its numerical inequality. **Proposed edit:** optional Baire-genericity corollary after 10.35.2.

In the exact hypotheses of Lemma 10.35.2, including a finite or countable collection of families, let \(p\) dominate each family-specific \(b+R\). In the Fréchet space \(H^0(X,E)^p\), the set of tuples simultaneously spanning every fiber in every prescribed family is **dense \(G_\delta\)** (a countable intersection of open dense sets). For finitely many families with **compact** parameter bases, the set is **open dense**.

**Proof.** For a compact \(K\) in one parameter manifold, the set of tuples for which all evaluations have full rank on \(K\) is open in compact-convergence topology: in finitely many local trivializations the sum of squares of the maximal minors has a positive minimum on \(K\), which persists under uniform perturbations. The proof of Lemma 10.35.2, lines 49–59, proves this open set is dense by a finite-dimensional parameter perturbation and a rank-stratum dimension bound
\[
 \operatorname{codim}_{\mathbf C}\{\operatorname{rank}<R\}=p-R+1>b.
\]
Choose a countable compact exhaustion for every parameter base and intersect the corresponding open dense sets. Baire completeness, proved at lines 48–49, makes that intersection dense \(G_\delta\). If only finitely many compact bases occur, their full-base full-rank conditions form a finite intersection of open dense sets, and hence are open dense. This uses no sequential compactness of a noncompact base. For first-jet and distinct-pair families of Theorem 10.35.3, take \(B=X\) and \(B=X\times X\setminus\Delta\) with the printed ranks; the same residual conclusion follows.

**Affected dependents:** Lemma 10.35.2 and Theorem 10.35.3 (the selected finite generators are generic, not just existential). This is **not** an assertion that a nonproper classifying map is an embedding; 10.35.6 correctly demonstrates the contrary.

## POME-EXT-P1-CONIC-001

**Severity:** low. **Status:** verified conditional deduction; printed Theorems 10.36.13 and Proposition 10.36.14 remain **correct**. **Proposed edit:** an optional finer classification following the example in Proposition 10.36.14, with the following direct proof.

Fix \(S=\mathcal O_{\mathbf P^1}(-2)\), \(Q=\mathcal O_{\mathbf P^1}(2)\). Theorem 10.36.13 identifies extension diagrams, with identity maps on the ends, with
\[
 H^1(\mathbf P^1,\operatorname{Hom}(Q,S))
 =H^1(\mathbf P^1,\mathcal O(-4))\simeq\mathbf C^3.
\]
On the standard cover \(U_0=\{[1:z]\}\), \(U_\infty=\{[w:1]\}\), \(w=1/z\), use the Čech representatives
\[
 e(z)=\frac a z+\frac b{z^2}+\frac c{z^3}.
\]
The connecting map of the extension twisted by \(\mathcal O(-1)\),
\[
 \delta_e:H^0(\mathcal O(1))\longrightarrow H^1(\mathcal O(-3)),
\]
is cup product by \(e\), up to the global sign convention for connecting maps. With \(\{1,z\}\) as a basis of \(H^0(\mathcal O(1))\) and \(\{z^{-1},z^{-2}\}\) as the Čech basis of \(H^1(\mathcal O(-3))\), multiplication and deletion of Čech coboundaries give
\[
 \delta_e\sim
 \begin{pmatrix}a&b\\ b&c\end{pmatrix};
 \qquad \det\delta_e=ac-b^2.
\]
This may change by a global nonzero scalar under frame conventions, but its rank and the projective conic are intrinsic.

Write \(E_e\) for the middle bundle of \(0\to\mathcal O(-2)\to E_e\to\mathcal O(2)\to0\). **Precisely**:
\[
 \boxed{
 E_e\simeq
 \begin{cases}
 \mathcal O(-2)\oplus\mathcal O(2),& (a,b,c)=(0,0,0),\\[2pt]
 \mathcal O(-1)\oplus\mathcal O(1),& ac=b^2,\ (a,b,c)\ne0,\\[2pt]
 \mathcal O\oplus\mathcal O,& ac\ne b^2.
 \end{cases}}
\]

**Proof of all three implications without Birkhoff–Grothendieck.** For the twisted sequence
\(0\to\mathcal O(-3)\to E_e(-1)\to\mathcal O(1)\to0\), the long exact sequence gives
\[
 h^0(E_e(-1))=2-\operatorname{rank}\delta_e.
\]
For \(e\ne0\), the sequence twisted by \(-2\) has connecting map \(H^0(\mathcal O)\to H^1(\mathcal O(-4))\) carrying \(1\) to \(e\ne0\), so \(H^0(E_e(-2))=0\). The untwisted connecting map \(H^0(\mathcal O(2))\to H^1(\mathcal O(-2))\) is multiplication by \(e\); in the Čech bases its coefficient row is \((a,b,c)\), so it is onto for \(e\ne0\), giving \(h^0(E_e)=2\).

If \(\delta_e\) has rank one, its nonzero kernel yields a nonzero section of \(E_e(-1)\). This section cannot vanish at any point \(p\), since its vanishing would give a nonzero section of \(E_e(-1)(-p)\simeq E_e(-2)\), just excluded. It therefore gives a subbundle \(\mathcal O\hookrightarrow E_e(-1)\) with quotient \(\mathcal O(-2)\), by \(\det E_e\simeq\mathcal O\). This sequence splits since \(\operatorname{Ext}^1(\mathcal O(-2),\mathcal O)=H^1(\mathcal O(2))=0\). Thus \(E_e=\mathcal O(1)\oplus\mathcal O(-1)\).

If \(\delta_e\) has rank two, then \(h^0(E_e(-1))=0\) and \(h^0(E_e)=2\). Take two linearly independent global sections. Their wedge is a section of \(\det E_e=\mathcal O\), so it is either identically zero or a nonzero constant. If identically zero, their saturated rank-one image is a holomorphic line subbundle \(L\simeq\mathcal O(d)\) of \(E_e\) with at least two independent sections. On \(\mathbf P^1\), \(d\ge1\), and hence \(H^0(L(-1))\ne0\), injecting into \(H^0(E_e(-1))=0\): contradiction. The wedge is therefore nowhere zero, and the two sections are a global frame, \(E_e\simeq\mathcal O^2\). If \(e=0\), the extension is split by Theorem 10.36.13. All cases follow from internal projective-line cohomology and elementary exact sequences.

Allowing scalar automorphisms of the fixed end line bundles, Proposition 10.36.14 gives the projective extension space \(\mathbf P^2\) for nonsplit diagrams. The equation
\[
 \boxed{ac-b^2=0\subset\mathbf P^2}
\]
is a **smooth conic** separating the orbit classes whose middle bundle is \(\mathcal O(1)\oplus\mathcal O(-1)\) from the open complement, all of whose middle bundles are \(\mathcal O^2\). Smoothness is immediate from the projective gradient \((c,-2b,a)\). The source's two distinct \(\mathcal O^2\)-middle-bundle diagrams in 10.36.14 are consistent with, and are refined by, this whole open two-dimensional family. The zero extension gives the third splitting type. **Diagram classes and abstract middle-bundle classes must not be conflated.**

**Affected dependents:** extension classification 10.36.13–14, twisted cohomology §10.51 and projective-curve examples §10.78. This does not assert an error in those sources, nor does it replace their statements with only the special \(\mathbf P^1\) case.

## Remaining limits, dispositions and editorial boundaries

The checked rank-stratum/Baire argument uses existing Fréchet completeness and finite-dimensional rank geometry. The conic proof uses the displayed long exact sequence and \(\mathbf P^1\) cohomology; these inputs were read but their complete upstream sheaf-cohomology derivations were **not** independently audited here. The sign of the line-current identity 10.36.11 agrees with \(d(dz/z)=2\pi i[0]\) and \(c_1(L)=(i/2\pi)F_D\) with the source convention; no new sign error was established. Affine nonclosed-background functoriality is conditional on the earlier trace results and no mass continuity is inferred from weak current convergence.

**No newly confirmed false mathematical theorem or proof-gap claim in this increment.** All three IDs are low-severity **verified conditional deductions**, not proposed repairs to false results. Exact new selected-proof coverage: §10.35 (listed passages), §10.36 (listed passages), §10.30 (listed nonexcluded passages); no full section, all 747 ToC entries, or dependent chain certified. No source, original manuscript, proof registry, permanent tag, main branch or published page changed; no tests, build, CI, website deployment or formal verification run. Dedicated Demailly approximation/regularization and its Bergman, \(L^2\), Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof-completion programme **remains deferred-by-user**, neither solved nor certified.