# Audit of the toric polytope-translation and character-linearization conventions

**Date:** 2026-11-02. **Reviewed production main:** b6933b772f41b45918f7e25ed1afbbb1fd892272.
**Finding:** POME-TORIC-POLYTOPE-TRANSLATION-WEIGHTS-001.
**Severity / classification:** low / **verified conditional deduction** (no false theorem or repair applied).
**Scope:** first selected direct proof-level check in §21.9 (the section was previously used as context for §§21.7–21.8). The printed character-order, section, and torus-action conventions agree under lattice translations. This audit proves an additional equivariant distinction; it does **not** certify the entire toric construction or §21.9.

## Reproducible reading-edition anchors

- **Main:** b6933b772f41b45918f7e25ed1afbbb1fd892272.
- **Integrated §21.9:** docs/sections/convex-analysis-and-toric-potentials--fans-divisors-and-character-sections/index.html, blob **7ad2e6dbdd0ce59e1bf08cd9cb3c046e8c87ff6c**. The inner-normal fan and its face data appear at lines 7–29; the principal character-divisor convention at lines 35–39 and 57–61; character gluing at lines 70–101; the full section/character decomposition at lines 139–167, especially the divisor formula at 139–157, the lattice inequalities at 158–164, and the contragredient torus action at 166.
- **Internal source labels / permanent tags:** foundations-of-pluripotential-theory:4C5E5EB3 / 9FD0EEED0DBF (Proposition 21.9.1); foundations-of-pluripotential-theory:86CCC496 / 7B4A7CC50CDC (Proposition 21.9.2); foundations-of-pluripotential-theory:43543C56 / C62B8871AA1C (Proposition 21.9.3); foundations-of-pluripotential-theory:BD98CC5B / 69D3D97E7701 (Theorem 21.9.5).
- **Upstream chart construction:** docs/sections/convex-analysis-and-toric-potentials--smooth-lattice-polytopes-and-projective-charts/index.html, blob **f442a7b663689b97a9b89689b8b7ae8b366a53fe**, lines 89–112, 126–132 and 142–154; foundations-of-pluripotential-theory:0F7315B0 / E49F0370E203 (Theorem 21.8.3).
- **Other stated dependency:** the lattice-counting result Theorem 21.7.3; not reproved here.

## Statement and exact scope

Let M be a rank-n lattice, N its dual, and P a full-dimensional smooth lattice polytope. Its facets have primitive **inward** normals u_rho and equations
\[
P=\{m\in M_{\mathbb R}:\langle m,u_\rho\rangle+a_\rho\geq0\},
\qquad a_\rho\in\mathbb Z.
\]
For a lattice translation b in M set P_b=P+b and identify its projective toric model with X_P by reindexing the homogeneous coordinate labelled m+b as the coordinate labelled m. Under this identification:

1. The inner normal fan, the toric base T-action, and the underlying projective toric variety do not change. The facet constants and divisors change by
\[
a_{\rho,b}=a_\rho-\langle b,u_\rho\rangle,\qquad
D_{P_b}=D_P-\operatorname{div}(\chi^b).
\]
Thus the line bundles are (noncanonically as equivariant bundles, but canonically after the specified coordinate reindexing) isomorphic as ordinary holomorphic bundles.
2. The distinguished meromorphic sections are related by
\[
s_{0,b}=\chi^{-b}s_0
\]
under the ordinary-bundle identification. In degree k, the **same underlying sections** correspond via
\[
\chi^{m+kb}s_{0,b}^{\,k}=\chi^m s_0^{\,k},
\qquad m\in kP\cap M .
\]
The equality also holds at k=0, with the usual 0P={0} convention.
3. The **natural torus linearizations are not the same**: on the identified hyperplane bundle the P_b-action is the P-action twisted by the character \(\chi^{-b}\); on its kth power the twist is \(\chi^{-kb}\). Hence the basis line indexed by m has character \(\chi^{-m}\) for P but character \(\chi^{-(m+kb)}\) for P_b. Forgetting the linearization, the spaces of sections and their dimensions agree. This shift must be retained in any canonicalization of character decompositions.

These deductions are conditional on the **printed** chart construction and action conventions. They are not independent proof of the global existence or smoothness theorems.

## Full derivation

**Fan and divisor.** For every facet rho of P, the corresponding translated facet rho+b has the same inward primitive u_rho. Indeed
\[
\langle m+b,u_\rho\rangle+
(a_\rho-\langle b,u_\rho\rangle)
=\langle m,u_\rho\rangle+a_\rho.
\]
Therefore corresponding faces and their normal cones are unchanged. Proposition 21.9.2 gives, as a meromorphic identity on the dense torus and hence on X_P,
\[
\operatorname{ord}_{D_\rho}(\chi^b)=\langle b,u_\rho\rangle.
\]
There are no other codimension-one components of the divisor of a character, because the complement of the torus is the union of precisely these invariant prime divisors and \(\chi^b\) is invertible on the torus. Summing produces the displayed relation between D_{P_b} and D_P. This proves ordinary linear equivalence, not equality of distinguished Cartier divisors.

**The projective model and its linearization.** Let A=P cap M and define the coordinate permutation
\[
R_b:\mathbb C^{A}\longrightarrow\mathbb C^{A+b},
\qquad (R_bZ)_{m+b}=Z_m.
\]
On the dense torus,
\[
(R_b\iota_P)(t)=[\chi^m(t)]_{m+b},\qquad
\iota_{P_b}(t)=[\chi^{m+b}(t)]_{m+b}
=[\chi^b(t)\chi^m(t)]_{m+b}.
\]
These projective points are identical, so the permutation identifies the **closures** X_P and X_{P_b}, not merely their dense tori. It also preserves the local monomial coordinates because \((m+b)-(v+b)=m-v\).

Write \(\rho_P(\tau)\) for the diagonal action on \(\mathbb C^{A}\) with weight \(\chi^m(\tau)\) in coordinate m, and similarly for P_b. Then, **as an equality of linear maps**,
\[
\rho_{P_b}(\tau)R_b
=\chi^b(\tau)R_b\rho_P(\tau).
\]
The scalar disappears projectively and hence the induced base action is unchanged. It does **not** disappear on the tautological line over each point: relative to R_b, the O(-1) fibers are multiplied by \(\chi^b\). Dualizing gives the twist \(\chi^{-b}\) on O(1), and tensoring gives \(\chi^{-kb}\) in degree k. This explicitly distinguishes ordinary line-bundle isomorphism from isomorphism of the **given** linearizations.

**Distinguished section and weight computation.** With s_v the coordinate frame over U_v, Theorem 21.9.5 defines \(s_0=\chi^{-v}s_v\). After relabelling, \(s_{v+b,b}=s_v\) as ordinary local frames. Consequently
\[
s_{0,b}=\chi^{-(v+b)}s_{v+b,b}
=\chi^{-b}s_0.
\]
The lattice bijection \(m\mapsto m+kb\) carries \(kP\cap M\) onto \(k(P+b)\cap M\), and the displayed basis equality follows by raising \(s_{0,b}\) to the kth power. But the action on sections is \((\tau\cdot s)(x)=\tau\cdot s(\tau^{-1}x)\), and in the printed proof (line 166) the coordinate frame s_v has weight \(\chi^{-v}\), so s_0 is invariant and \(\chi^m s_0^k\) has weight \(\chi^{-m}\). Repeating with the translated coordinate representation yields weight \(\chi^{-(m+kb)}\), **not** \(\chi^{-m}\). Thus changing the polytope by a lattice translation shifts its intrinsic character labels while leaving its underlying section dimensions unchanged.

**Concrete sign check on P^1.** Take M=Z, P=[0,1], b=1. The inward normals are +1 at 0 and -1 at 1, with facet constants 0 and 1. Write D_0 and D_infty for the two invariant points, so
\[
D_P=D_\infty,\quad \operatorname{div}(z)=D_0-D_\infty,\quad
D_{[1,2]}=-D_0+2D_\infty=D_P-\operatorname{div}(z).
\]
Both bundles have degree one and the same underlying H^0 of dimension two. For k=1 the old weights are {1,chi^(-1)} (lattice labels 0,1), whereas the translated model has weights {chi^(-1),chi^(-2)} (labels 1,2), exactly a twist by chi^(-1). For general k the labels {0,...,k} become {k,...,2k}, giving a twist by chi^(-k). This independently checks the sign of both the divisor and representation formulas.

## Proof-dependency and canonicalization disposition

The apparent theorem-level loop between Theorem 21.8.3 and Theorem 21.9.5 is **staged, not a mathematical circular proof**: the §21.8.3 chart construction at lines 118–132 is established before any use of §21.9.5; §21.9.5 then uses those charts and its own Laurent argument; only the later **very ampleness** assertion of §21.8.3 (line 142) invokes the now-available section-basis theorem. An automated coarse theorem-to-theorem dependency graph can misclassify the steps as cyclic. Keep distinct steps when reviewing internal dependencies.

**Disposition:** correct printed formulas; no confirmed error or gap. Recommend an optional explanatory remark immediately after Theorem 21.9.5 recording the translation formulas, the distinction between ordinary and equivariant line bundles, and the contragredient sign. Preserve the source labels, permanent tags, both distinct embeddings/linearizations, and historical CLS11 attribution. Do **not** merge genuinely distinct linearized statements based only on isomorphic underlying varieties/bundles.

**Affected dependents:** toric character decompositions of H^0(X_P,L^k), toric polytope and section asymptotics, and any future equivalence or canonicalization comparing polytopes differing by a lattice translate. Theorem 21.9.5 itself requires no correction. No external mathematical input was newly introduced.

**Coverage accounting:** first selected direct §21.9 divisor/linearization/character proof check, touching 21.9.1–3 and 21.9.5 and the §21.8.3 staged dependency; no general recheck of all fan or Laurent theorem proofs, no first certification of an entire numbered section. Actual ToC remains 25 chapters / 747 numbered sections / zero fully mathematically certified sections. All earlier findings retain their classifications. The user-deferred Demailly approximation/regularization, Bergman, weighted L2, Ohsawa–Takegoshi, multiscale atlas and positivity-loss programme was not touched.

**Operations:** audit-note proposal only; no source/body/registry/canonicalization/tag or production-main modification; no project build, test suite, GitHub Actions CI, formal verification or website publication.
