# Mathematical audit: finite-map Dolbeault trace, exact point-jet cohomology, and optimal projective embedding dimension

**Date:** 2026-10-28 (Asia/Shanghai).  
**Pinned production main:** b6933b772f41b45918f7e25ed1afbbb1fd892272.  
**Starting audit branch HEAD:** 5aa4f41894c9c26fba96e433aaa68783245c4ec2.  
**Scope:** directly read the integrated proof of Proposition 10.41.1, Theorem 10.41.2 and Corollary 10.41.3, and revisited Proposition 10.91.1; examined only the explicitly named upstream current-comparison/change-of-variables statements. This is a limited proof pass, not certification of either whole section. Dedicated Demailly approximation/regularization and Bergman, weighted L2, Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof programmes remain **deferred-by-user** without reopening them.

## POME-FINITE-DOLBEAULT-TRACE-SPLIT-001

**Severity:** low. **Status:** verified conditional deduction (a rigorous extension of a correct statement, not a false theorem).  
**Integrated locus:** Proposition **10.91.1**, source <code>demailly-complex-geometry:CAB0AEA4</code>, permanent tag <code>35E27213FA56</code>, <code>docs/sections/one-point-curvature-positivity-and-vanishing--one-point-positivity-and-modification-descent/index.html</code>, main Git blob <code>95b3f78a729e01664c4a24d3ef8aa96143ead523</code>, physical lines **7–40** (especially 18–40); exact same proposition's permanent page <code>docs/tag/35E27213FA56/index.html</code>, lines 6–36. The proof explicitly invokes Corollary **10.43.11**, tag <code>EE08E1840318</code> (smooth/current Dolbeault comparison), and Theorem **10.87.1**, tag <code>C4B9BA82F24B</code> (degree-one modification change of variables); these upstream comparisons are **conditional inputs**, not newly certified.

**Generalization, with the exact hypothesis.** Let \(f:Y\to X\) be a **surjective proper generically finite holomorphic map of topological degree \(d>0\)** between compact complex manifolds of the same pure dimension \(n\). The map may have branch and critical loci and need not be a modification. For any holomorphic vector bundle \(F\) on \(X\) and \(0\leq p,q\leq n\), the pullback
\[
 f^*:H_{\bar\partial}^{p,q}(X,F)\longrightarrow H_{\bar\partial}^{p,q}(Y,f^*F)
\]
has a **canonical left inverse on cohomology**, namely
\[
 \frac1d\,(\text{smooth/current comparison})^{-1}\circ
 f_*\circ(\text{smooth/current comparison}).
\]
Here the pushforward is on \(f^*F\)-valued currents, tested against smooth compactly supported \(F^*\)-valued complementary forms. In particular \(f^*\) is split injective over \(\mathbb C\), without any Kähler hypothesis.

**Proof and verification.** Properness ensures that pullbacks of compactly supported test forms have compact support; local holomorphic frames and the projection formula make \(f_*\) globally well-defined and show \(\bar\partial_F f_*=f_*\bar\partial_{f^*F}\). For a smooth \(F\)-valued \((p,q)\)-form \(a\), pair with an \(F^*\)-valued complementary-degree test form \(\eta\). On the complement of the critical values and branch locus, \(f\) is a \(d\)-sheeted covering and the (holomorphic, hence orientation-preserving) change-of-variables formula gives
\[
 (f_*f^*a)(\eta)=\int_Yf^*(a\wedge\eta)=
 d\int_X a\wedge\eta .
\]
The analytic branch/critical sets have real measure zero, so equality extends to all smooth tests: \(f_*f^*a=d\,a\) as \(F\)-valued currents. Both chain maps commute with \(\bar\partial\); the actual smooth/current Dolbeault quasi-isomorphisms of Corollary 10.43.11 therefore transport \(d^{-1}f_*\) to the required left inverse. This also covers \(q=0\). The scalar integral is an ordinary complex-valued top-form integral after contraction, so there is no missing factor of \(d\) from bundle rank or of \((-1)\) from relative dimension zero.

**Hypothesis boundary / nonexample.** If proper surjectivity and positive degree are removed, a point inclusion into an elliptic curve pulls back a nonzero holomorphic \(1\)-form to zero, so no general injectivity can hold. The statement is over characteristic-zero coefficients, where \(d^{-1}\) is legal; it makes no claim for torsion-valued integral cohomology. **Dependents / proposed correction:** optional generalization as a separate remark under §10.91.1, retaining the original modification statement, provenance and permanent tag. The curvature-vanishing Theorem 10.91.2 has additional Kähler and metric hypotheses and is **not** automatically generalized by this trace argument alone.

## POME-BLOWUP-POINT-JET-H1-OPTIMAL-001

**Severity:** low. **Status:** verified conditional deduction (an exact model and sharpness of the linear threshold in a correct original proposition).  
**Integrated locus:** Proposition **10.41.1**, source <code>demailly-complex-geometry:91D659DC</code>, permanent tag <code>A8BE0AECFD69</code>, <code>docs/sections/jets-integral-curvature-and-projective-embeddings--blowup-vanishing-and-small-projective-embeddings/index.html</code>, main blob <code>b73726f6a164aff26a488453d5cd10db6153948f</code>, physical lines **20–64**, particularly the uniform bound \(k\geq Cm\) at 20–24 and its curvature proof at 29–61.

**Exact quantitative model.** Let \(\pi:Y=\operatorname{Bl}_p\mathbb P^2\to\mathbb P^2\) blow up one point, let \(E\) be the exceptional \((-1)\)-curve, and set \(H=\pi^*\mathcal O_{\mathbb P^2}(1)\). For **all integers \(m\geq1,\ k\geq0\)**,
\[
 \boxed{\quad h^1\bigl(Y,\mathcal O_Y(kH-mE)\bigr)
 =\binom{m+1}{2}
 -\binom{\min\{k,m-1\}+2}{2}.\quad}
\]
Thus \(H^1=0\) **if and only if** \(k\geq m-1\); at the preceding degree \(k=m-2\) (when \(m\geq2\)), \(h^1=m\). Hence the linear-in-\(m\) order in Proposition 10.41.1 is genuinely necessary even for a fixed smooth projective surface and a single blown-up point. The original coarse uniform constant \(C>0\) remains valid; the point-example exact threshold is not asserted for general manifolds.

**Self-contained jet/cohomology computation.** The blowup is the incidence hypersurface
\(Y=\{Z_1V-Z_2U=0\}\subset\mathbb P^2_{[Z]}\times\mathbb P^1_{[U:V]}\), whose projection to \(\mathbb P^2\) is \(\pi\). For \(k\geq0\), the incidence exact sequence is
\[
 0\to\mathcal O(k-1,-1)\to\mathcal O(k,0)
 \to\mathcal O_Y(kH)\to0.
\]
Since \(\mathcal O_{\mathbb P^1}(-1)\) is acyclic, Künneth and the standard projective-space line-bundle cohomology give
\[
 H^1(Y,\mathcal O_Y(kH))=0,\qquad
 H^0(Y,\mathcal O_Y(kH))=H^0(\mathbb P^2,\mathcal O(k)).
\]
Now use the Cartier divisor thickening exact sequence
\[
 0\to\mathcal O_Y(kH-mE)\to\mathcal O_Y(kH)
 \to\mathcal O_{mE}(kH)\to0.
\]
Because \(H|_E\) is trivial, the filtration
\(0\to\mathcal O_E(m-1)\to\mathcal O_{mE}\to\mathcal O_{(m-1)E}\to0\)
and \(H^1(\mathbb P^1,\mathcal O(j))=0\) for \(j\geq0\) show
\(h^0(mE,\mathcal O_{mE}(kH))=\sum_{j=0}^{m-1}(j+1)=\binom{m+1}{2}\).
Trivialize \(\mathcal O(k)\) near \(p\) and take local affine coordinates \(x,y\). Pullback of a polynomial whose lowest nonzero homogeneous term has degree \(j\) vanishes along \(E\) **exactly** to order \(j\). Therefore polynomials in \(x,y\) of degree \(<m\) inject into \(H^0(mE,\mathcal O_{mE}(kH))\); their dimension equals the latter, proving they form the full jet space. The restriction map from global homogeneous degree-\(k\) polynomials has image exactly the jets of degrees \(\leq\min(k,m-1)\), of rank \(\binom{\min(k,m-1)+2}{2}\). The long cohomology sequence identifies its cokernel with the displayed \(H^1\), giving the exact formula. No approximation, weighted estimates, or hidden limit interchange is involved.

**Dependents / proposed correction:** retain Proposition 10.41.1 unchanged; optionally add the sharp projective-plane one-point jet example next to its coarse vanishing estimate and point-jet interpolation applications. The standard line-bundle cohomology and Künneth identities used here are elementary background inputs, not a full independent certification of the proof registry's analytic vanishing theorem §10.33.14.

## POME-EMBEDDING-DIMENSION-GENUS2-001

**Severity:** low. **Status:** verified conditional deduction (a sharpness witness for a correct universal bound).  
**Integrated locus:** Theorem **10.41.2**, source <code>demailly-complex-geometry:DB857A8E</code>, permanent tag <code>AF752427463F</code>, same §10.41 main blob <code>b73726f6a164aff26a488453d5cd10db6153948f</code>, physical lines **69–101** (secant/tangent dimension proof 75–100). Also read Corollary **10.41.3**, source <code>demailly-complex-geometry:C5BD1F28</code>, permanent tag <code>4E2A659999BE</code>, physical lines **105–121**.

**Sharpness in dimension one.** A smooth compact genus-two curve exists: the smooth compactification of
\(y^2=\prod_{j=1}^{6}(x-j)\) is a degree-two branched cover of \(\mathbb P^1\) at six simple branch points, so Riemann–Hurwitz gives \(2g-2=2(-2)+6=2\), hence \(g=2\). If such a curve embedded into \(\mathbb P^2\), its image would be a smooth plane curve of some degree \(d\geq1\). Adjunction on \(\mathbb P^2\), using \(K_{\mathbb P^2}=\mathcal O(-3)\) and the normal bundle \(\mathcal O_C(d)\), yields
\[
 2g-2=d(d-3),\qquad
 g=\frac{(d-1)(d-2)}2.
\]
The possible genera for \(d=1,2,3,4,\ldots\) are \(0,0,1,3,6,\ldots\), never \(2\). Hence a genus-two curve cannot holomorphically embed in \(\mathbb P^2\), whereas Theorem 10.41.2 supplies an embedding into \(\mathbb P^3\). The universal \(2n+1=3\) **cannot** be uniformly lowered for \(n=1\). In dimension zero, two distinct points likewise cannot embed into \(\mathbb P^0\), confirming the \(2n+1=1\) bound is sharp for disconnected zero-dimensional manifolds. These examples do **not** assert optimality in every positive dimension.

**Proof review / dependents:** inspected the theorem's explicit secant and tangent bad-center sets, the real-dimension/measure-zero bound and the argument that secant limits on the diagonal land in tangent directions. Its compactness passage is sequential because the projective manifolds in this proof are metrizable; no arbitrary-net compactness claim was made. The usual projective normal/adjunction facts above give the genus obstruction. Optional short sharpness remark only. The algebraicity step in §10.41.2 still calls Theorem 10.40.10; this separate internal dependency was not independently recertified.

## Coverage, prior findings and exclusions

- Re-read current <code>main</code> ref, <code>AGENTS.md</code>, <code>documentation/proof-expansions.md</code>, audit <code>LATEST.md</code>, and review-branch <code>README.md</code> before the session. The <code>main</code> SHA matches the pinned audit basis above.
- Freshly enumerated the 25 current chapter indexes: **747 distinct numbered sections**. **§10.41** was previously inventory-only and now has its **first** selected proof-level inspection of Proposition 10.41.1 and Theorem 10.41.2/Corollary 10.41.3; **§10.91** was already partly sampled on 2026-10-27, so its Proposition 10.91.1 review is an **increment only**, not a first section. Corollary 10.43.11 and Theorem 10.87.1 are context/dependencies, not newly certified coverage. **No entire section or chapter** was certified.
- Historical issues, including existing errors, proof gaps, candidate dependencies and all **deferred-by-user** notes, retain their previous statuses. None of the three new findings declares a printed theorem false, repairs a transitive proof chain, or authorizes canonicalization changes.
- No main/source/registered-proof/permanent-tag/published-document change, no builds, tests, CI, formalization, automatic merge, issue or pull request creation, and no publication. All dedicated Demailly approximation/regularization, Bergman, L2, Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof-completion work remains **deferred-by-user**.
