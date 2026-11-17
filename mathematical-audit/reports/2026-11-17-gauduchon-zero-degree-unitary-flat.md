# Zero Gauduchon degree and rigidity of positive curvature currents

- **Finding ID:** POME-GAUD-ZERO-DEGREE-UNITARY-FLAT-001
- **Date:** 2026-11-17
- **Severity / status:** low / **verified conditional deduction**, not a correction of a false printed theorem.
- **Reviewed main:** b6933b772f41b45918f7e25ed1afbbb1fd892272.
- **Integrated reading edition:** \`docs/sections/holomorphic-sections-and-hermitian-mass/index.html\`; blob \`5f00431e7986d899dc833c89175686b75f09371d\`.
- **Stable anchors:** subsection 19.8.4, permanent tag \`E5AAFD4B6553\`, physical lines 104–116; Theorem 19.8.5, source \`non-kahler-pluripotential-theory:6E03C7D3\`, permanent tag \`1DFDCCEF325D\`, physical lines 118–148 (especially the positive-current trace at lines 142–148). Related Poincaré–Lelong and Gauduchon trace input: §11.5.1, permanent tag \`828FAD1A35BF\`, cited at §19.8 line 142.
- **Actual scope:** direct inspection of the integrated degree formula, proof of Theorem 19.8.5, and the positive-current paragraph; independent proof of the following precise rigidity corollary. Sections 19.8.7 and 20.4 were considered only for comparison, not newly certified. Neither the Bergman proof programme nor regularization was opened.

## Statement (precise hypothesis)

Let \`X\` be a **connected compact complex manifold**, \`gamma\` a smooth positive Gauduchon Hermitian form, and \`L\` a holomorphic line bundle with smooth Hermitian metric \`h\` and curvature \`beta=c_1(L,h)\` in the normalization
\[
 dd^c=\frac{i}{2\pi}\partial\bar\partial,\qquad
 \deg_\gamma L=\int_X\beta\wedge\gamma^{n-1}.
\]
Assume \`L\` is **Bott–Chern pseudoeffective** in the concrete sense that some (possibly singular) quasi-psh potential \`u\` has
\[
 T=\beta+dd^c u\geq0
\]
as a closed positive \((1,1)\)-current. Then
\[
\boxed{\deg_\gamma L=0
\quad\Longleftrightarrow\quad
 L\text{ admits a smooth Hermitian metric with zero Chern curvature}.}
\]
In this equivalence, the right-hand condition does not need a separate pseudoeffectivity assumption, and implies zero degree for **every** Gauduchon metric. Furthermore, if \(\deg_\gamma L=0\), **every** positive current \(\beta+dd^cu\) in this Bott–Chern class is zero; every such \(u\) is smooth, and a zero-curvature Hermitian metric is unique up to multiplication by a positive constant.

The statement does **not** say that \`L\` is holomorphically trivial or torsion; a non-torsion unitary-flat line bundle need not have any nonzero holomorphic sections, as the integrated elliptic-curve example at lines 213–214 illustrates.

## Proof

1. **Zero trace mass forces the current to vanish.** Since \(\gamma\) is Gauduchon, \(dd^c(\gamma^{n-1})=0\). The integration-by-parts/trace identity from §19.8.5 yields
\[
  \int_X T\wedge\gamma^{n-1}
 =\int_X\beta\wedge\gamma^{n-1}
 =\deg_\gamma L.
\]
The left side is the mass of a positive \((1,1)\)-current relative to the smooth strictly positive \((n-1,n-1)\)-form \(\gamma^{n-1}\). It is nonnegative and vanishes only if \(T=0\). To check the last implication locally, fix a Hermitian coordinate ball: the positive semidefinite matrix of coefficient measures of \(T\) has vanishing trace measure when the wedge mass vanishes, so every diagonal measure and, by positivity/Cauchy–Schwarz, every off-diagonal coefficient measure is zero. For \(n=1\), the same statement is simply vanishing of a positive measure of mass zero. Thus \(\deg_\gamma L=0\) forces \(T=0\).

2. **No singular zero-curvature weights.** Now \(dd^c u=-\beta\) as distributions. On a coordinate ball with a smooth local curvature potential \(\chi\), \(\beta=dd^c\chi\), the distribution \(u+\chi\) satisfies \(dd^c(u+\chi)=0\). Taking the trace gives the ordinary distributional Laplace equation \(\Delta(u+\chi)=0\). Weyl's lemma makes \(u+\chi\) smooth and harmonic; in fact it is pluriharmonic because its full \(\partial\bar\partial\) vanishes. Hence \(u\) is smooth on \(X\). The smooth metric \(h'=h\,e^{-u}\) has Chern curvature \(\beta+dd^c u=T=0\), giving a unitary-flat Chern connection.

3. **Conversely and uniqueness.** If \(h'\) is a smooth Hermitian metric on \(L\) with curvature zero, \(0\) is a positive closed representative of \(c_1(L)\), and the Gauduchon degree is zero, independently of the chosen Gauduchon metric. If \(h_1,h_2\) are two such metrics, write \(h_2=h_1e^{-f}\) for a smooth global real \(f\). Their curvature equality gives \(dd^c f=0\). A real pluriharmonic function on a connected compact complex manifold is constant by the maximum principle. Therefore \(h_1,h_2\) differ by a positive constant.

As a slightly more general convex-cone observation, a pseudoeffective real Bott–Chern \((1,1)\)-class whose Gauduchon degree vanishes against a **single** smooth Gauduchon form is the zero class: its positive representative is zero. This is a deduction from positivity, not a claim of strict separation by a *single* Gauduchon functional for arbitrary non-pseudoeffective classes.

## Dependencies, comparison, and proposed disposition

The integrated §19.8.5 proof already establishes the key mass identity and its vanishing consequence (lines 142–148), but does not explicitly state the **iff** characterization of a pseudoeffective degree-zero line bundle by existence of a smooth unitary-flat metric, nor the elimination of singular positive weights and uniqueness up to scale. The added Weyl/max-principle step completes this corollary. Theorem 19.8.5 remains correct: its separate claim about nonzero sections is strictly stronger in a different direction and must not be conflated with curvature-flatness. The elliptic non-torsion example already present at lines 213–214 prevents that conflation.

**Suggested source/body change (proposal only):** add this short corollary after the positive-current paragraph of §19.8.5, with a reference to the existing normalized trace identity. Do not replace its statement, proof, source attribution, or permanent tag. Potentially relevant other sections are §11.5 (Gauduchon traces), §10.40 (integral Chern classes and unitary flat bundles), and §19.8.7 (restriction-degree obstruction); none was recertified in this run.

**Open upstream items:** the collection's full smooth positive-current trace and distributional harmonic regularity dependency chains were not reverified. The argument assumes the printed Stokes/Gauduchon identity and standard local Weyl regularity. It requires no Demailly approximation/regularization and no Bergman, \(L^2\), Ohsawa–Takegoshi, multiscale atlas, or positivity-loss proof completion. All such excluded work remains **deferred-by-user**, not resolved/certified.

**Coverage:** §19.8 previously had selected proof-level audits; this run gives **+0 newly first-visited numbered sections, +0 wholly certified sections**. It is a narrow verified corollary, not a claim that all of §19.8 or the 25-chapter/747-section project has been checked. No tests, builds, CI, or website publication were run.
