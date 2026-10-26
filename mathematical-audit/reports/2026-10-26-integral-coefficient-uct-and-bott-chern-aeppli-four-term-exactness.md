# 2026-10-26 — finite-coefficient universal coefficient sequence and Bott–Chern/Aeppli exactness

**Review checkpoint:** 2026-10-26T10:02:42.102Z. **Reviewed main:** b6933b772f41b45918f7e25ed1afbbb1fd892272. **Audit parent:** 46967f87c66ee4279ca09f6e82ee8a7265ebe8ed. **Scope:** selected integrated proofs in §§10.63–10.64 and §§10.84–10.86, not complete chapters and not transitive certification. All five were previously inventory-only in the 747-section matrix. No source/body, canonicalization, registry, permanent-tag, CI, build, or published-site edits.

**Explicit exclusion:** No part of Demailly approximation/regularization or its dedicated Bergman, L², Ohsawa–Takegoshi, multiscale-atlas, or positivity-loss proof-completion programme was opened. Any historical records about it remain **deferred-by-user**, neither resolved nor certified. None of the deductions below needs those results.

## 1. POME-COEFF-UCT-FINITE-GOOD-COVER-001

**Classification:** low severity; **verified conditional deduction**, not an error in a printed theorem. The conditional input is the finite free integral cochain model in Theorem 10.64.1, itself supported by the selected good-cover arguments of §10.63.

**Precise integrated anchors, reviewed main b6933b772f41b45918f7e25ed1afbbb1fd892272:**
- docs/sections/spectral-sequences-support-and-cup-products--constant-coefficients-and-integral-cohomology-lattices/index.html, blob 468705ce2e2cbad662a2fc316b65e16311dae105: Lemma 10.63.2, permanent tag 73465E4FD7CC, lines 12–25; Theorem 10.63.3, tag 0FA0E78E20CF, lines 30–37; Theorem 10.63.5, tag 2AA913B1559D, lines 43–93; Lemma 10.63.7, tag A49628740AA3, lines 98–105.
- docs/sections/spectral-sequences-support-and-cup-products--a-finite-integer-complex-and-coefficient-comparison/index.html, blob 5dfc94ab65a71cdd8cfe9d648552a9f014056fdf: Theorem 10.64.1, tag F04BCA811EFA, lines 8–19; Lemma 10.64.2, tag 7C6F99D51075, lines 24–37; Theorem 10.64.3, tag 04921B659563, lines 42–53.

**Strengthening, with precise hypotheses.** Let M be a compact smooth manifold and A any abelian group. There is a natural short exact sequence

\[
0\longrightarrow H^q(M,\underline{\mathbb Z})\otimes_{\mathbb Z}A
\longrightarrow H^q(M,\underline A)
\longrightarrow \operatorname{Tor}^{\mathbb Z}_1
 (H^{q+1}(M,\underline{\mathbb Z}),A)
\longrightarrow0.
\tag{UCT}
\]

The sequence is functorial in coefficient homomorphisms; it splits as an abstract sequence of groups, but there is no claimed canonical splitting. In particular, the rational and real coefficient isomorphisms printed in Theorem 10.64.3 are the torsion-free special cases. For finite coefficients, the Tor term need not vanish.

**Full finite-cochain proof.** Choose the finite integral Čech complex D of Theorem 10.64.1, whose differentials have integer matrices and which computes cohomology with every coefficient group A. Write \(Z^q=\ker(d^q:D^q\to D^{q+1})\), \(B^q=\operatorname{im}d^{q-1}\), and \(H^q=Z^q/B^q\). As a subgroup of a finite free abelian group, \(B^{q+1}\) is free (the elementary subgroup argument in Lemma 10.64.2). The exact sequence \(0\to Z^q\to D^q\to B^{q+1}\to0\) therefore splits, so choose, noncanonically, \(D^q=Z^q\oplus B^{q+1}\) with d zero on the first summand and the inclusion \(B^{q+1}\hookrightarrow Z^{q+1}\) on the second.

Tensor the resulting differential with A. Its degree-q cycles are
\[
(Z^q\otimes A)\ \oplus\
\ker(B^{q+1}\otimes A\longrightarrow Z^{q+1}\otimes A),
\]
and its degree-q boundaries lie in the first summand and equal the image of \(B^q\otimes A\to Z^q\otimes A\). Right exactness of tensor product identifies the first quotient with \(H^q\otimes A\). Because \(0\to B^{q+1}\to Z^{q+1}\to H^{q+1}\to0\) is a length-one free resolution (both B and Z free), its tensor kernel is exactly \(\operatorname{Tor}_1^{\mathbb Z}(H^{q+1},A)\). This proves (UCT) and yields an abstract splitting after the chosen decompositions. The inclusion of the first summand and the Tor connecting morphism recover the standard coefficient-natural maps, independently of the arbitrary splitting. Finally use the coefficient-natural Čech/sheaf comparison from Theorem 10.64.1.

**Sharp obstruction to naïve field extension.** For the two-term integral cochain complex \(D^0=\mathbb Z\xrightarrow{\times 2}D^1=\mathbb Z\), one has \(H^0(D)=0\) and \(H^1(D)=\mathbb Z/2\), whereas \(H^0(D\otimes\mathbb Z/2)=\mathbb Z/2\). Thus \(H^q(D)\otimes A\to H^q(D\otimes A)\) can fail to be surjective even for a finite free integral complex; the Tor term is indispensable. This is an algebraic test, not a claim that this particular two-term complex is a given Pome manifold model.

**Proposed addition:** a short UCT corollary after Theorem 10.64.3, with no changes to the correct existing field-coefficient statement or normalizations. **Affected dependents:** integral period lattices, coefficient comparisons, torsion-sensitive cup products, and any arguments transporting real-de Rham ranks to finite coefficients. No specific downstream false statement is alleged. The compact-good-cover and sheaf comparison inputs were inspected at their indicated passages but not independently certified as a whole dependency chain.

## 2. POME-BC-AEPPLI-FOUR-TERM-001

**Classification:** low severity; **verified conditional deduction**, not a false statement or a repair. This extends an existing three-term exactness observation by a fourth term and an additional proved exactness.

**Precise integrated anchors, reviewed main b6933b772f41b45918f7e25ed1afbbb1fd892272:**
- docs/sections/general-complex-cohomology-and-modifications--the-frolicher-filtration/index.html, blob ca98ecdb53f2ec77b439fdeb826dfa1dc6c60bdc: Theorem 10.84.1, tag F105D4917B45, statement lines 8–18 and spectral-page rank proof lines 24–43.
- docs/sections/general-complex-cohomology-and-modifications--bott-chern-and-aeppli-comparison/index.html, blob d47c823a457ed5daa1b8b0a5cdfae06f65f86980: definitions at lines 8–13; bounded double-complex Lemma 10.85.1, tag D823F74394BA, lines 17–24; smooth/current comparison Theorem 10.85.2, tag 72D73EDC0883, lines 29–40.
- docs/sections/general-complex-cohomology-and-modifications--finite-sheaf-complexes-for-bott-chern-cohomology/index.html, blob 311feffd4a3e3869a0856744b35af77059fa7c1a: Lemma 10.86.1 tag 6C01A2D464F2, lines 11–26; Proposition 10.86.2 tag 6ED26B437C1C, lines 30–71; Theorem 10.86.3 tag 69060D8AFA59, lines 76–93, especially the three-term exactness at lines 86–92.

**Exactness (all complex manifolds, not necessarily compact or Kähler):** with \(a=\partial\), \(b=\bar\partial\), the canonical sequence
\[
H_{\bar\partial}^{p,q}(X)
 \longrightarrow H_{\mathrm A}^{p,q}(X)
 \xrightarrow{\ \bar\partial\ }H_{\mathrm{BC}}^{p,q+1}(X)
 \longrightarrow H_{\bar\partial}^{p,q+1}(X)
\tag{BA}
\]
is **exact at the two middle terms**. The first three terms and exactness at A are explicitly printed in the proof of Theorem 10.86.3; the fourth map and exactness at BC are a distinct, elementary addition. End terms are *not* asserted injective or surjective. The conjugate \(\partial\)-sequence is equally exact at its middle terms. All maps and the assertion are compatible with smooth forms and currents through Theorem 10.85.2.

**Complete direct proof.** For a \(\bar\partial\)-closed (p,q)-form \(\alpha\), one has \(\partial\bar\partial\alpha=0\), so its class defines an Aeppli class; a \(\bar\partial\)-boundary is zero in Aeppli. For any Aeppli class represented by \(\alpha\) with \(\partial\bar\partial\alpha=0\), the form \(\bar\partial\alpha\) is both \(\partial\)-closed and \(\bar\partial\)-closed. Replacing \(\alpha\) by \(\alpha+\partial u+\bar\partial v\) alters \(\bar\partial\alpha\) by \(-\partial\bar\partial u\), a Bott–Chern boundary. Finally a BC class maps to its ordinary Dolbeault class because \(\partial\bar\partial\)-boundaries are \(\bar\partial\)-boundaries.

If the BC class of \(\bar\partial\alpha\) vanishes, write \(\bar\partial\alpha=\partial\bar\partial u\). Then \(\bar\partial(\alpha+\partial u)=0\), proving exactness at A. Conversely, if a BC class represented by \(\beta\) maps to zero in Dolbeault, write \(\beta=\bar\partial\alpha\); since \(\partial\beta=0\), \(\partial\bar\partial\alpha=0\). Hence the Aeppli class of \(\alpha\) maps to \([\beta]_{\mathrm{BC}}\), proving exactness at BC. The proof treats out-of-range indices as zero in the standard double complex; no limiting argument, Kähler identity, singular-weight estimate, or approximation theorem is involved.

For a compact complex manifold the finite-dimensionality in Theorem 10.86.3 immediately yields
\[
h_{\mathrm A}^{p,q}\leq h_{\bar\partial}^{p,q}+h_{\mathrm{BC}}^{p,q+1},
\]
and, more precisely,
\[
h_{\mathrm A}^{p,q}
=\operatorname{rank}(H_{\bar\partial}^{p,q}\to H_{\mathrm A}^{p,q})
+\dim\ker(H_{\mathrm{BC}}^{p,q+1}\to H_{\bar\partial}^{p,q+1}).
\]
The analogous \(\partial\)-bound also holds. These bounds do not turn the canonical maps into arbitrary direct-sum isomorphisms.

**Proposed addition:** add the fourth arrow and the one-line BC exactness argument after the displayed sequence in Theorem 10.86.3. **Affected dependents:** BC/Aeppli and Dolbeault comparison, cohomology of currents, and possible dimension estimates in non-Kähler Hodge theory. The original claims remain correct. This review checked the sign of \(\bar\partial\partial=-\partial\bar\partial\) in Theorem 10.85.2 and the special endpoint cases \(p=1\) or \(q=1\) in Proposition 10.86.2; the entire proof machinery, including all §10.43 and §10.55 inputs, is *not* independently certified.

## Coverage and ledger discipline

- **Actually inspected:** §§10.63.2–7 (selected homotopy/good-cover construction), 10.64.1–3 (finite integral Čech complex, lattice comparison), 10.84.1 (Frölicher rank/equality proof), 10.85.1–2 (bounded bicomplex staircase and forms/currents comparison), 10.86.1–3 (local resolution, endpoint conventions, BC/Aeppli finite-dimensionality and exactness).
- **Not checked:** every other result in these sections, complete proofs of referenced §10.43 Dolbeault, §10.44 paracompactness, §10.54–55 sheaf/spectral comparison, or any full chapter. Neither finding establishes a new source error; both are conditional internal consequences.
- **Existing issues:** no prior confirmed error, proof gap, duplicate, or external dependency is marked resolved by this report. In particular, all Demailly-related matters remain **deferred-by-user**.
- **Tests:** direct mathematical algebra and index checks only; no repository builds, CI, formal proof assistant, site publication or mathematical-body edits. Historical attribution and permanent tags are unchanged.
