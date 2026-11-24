# Global differential forms and vector fields on the increasing Stein-surface union

Date: 2026-11-24. Finding **POME-STEIN-UNION-GLOBAL-DIFFERENTIAL-COMPLEX-001** (low / verified conditional deduction, not a printed error).

## Immutable anchors and prior work

Main b6933b772f41b45918f7e25ed1afbbb1fd892272. Example 9.27.1, source demailly-complex-geometry:BBFF78A8, permanent F00C66A8D202, in docs/sections/separation-strict-exhaustions-and-coverings--an-increasing-union-of-affine-stein-surfaces/index.html, blob 26b2e856fc24b04616b0840caec5c688cc045ffa, lines 8–12 (stage equations), 18–30 (smooth stages and open embeddings), 32–46 (projection and escaping discs). The global entire-function algebra and the symplectic form and sphere periods were already established in [October 30](2026-10-30-stein-union-entire-algebra-and-holder-interpolation.md) and [November 16](2026-11-16-stein-union-hamiltonian-periods-infinite-h2.md). Neither is counted as new.

## New result and proof

Write \(a_j=1/j,\ p_\nu(z)=\prod_{j\le\nu}(z-a_j),\ X_\nu=\{wt=p_\nu(z)\}\) and \(X=\bigcup X_\nu\) with the specified open embeddings. Put \(\pi=(z,w)\), \(A=\mathcal O(\mathbb C^2)\). The earlier proof gives \(\mathcal O(X)=\pi^*A\) (injective because the image contains \(w\ne0\)); the nowhere-vanishing two-form \(\Omega=dz\wedge dw/w\) extends in each stage as \(dt\wedge dw/p_\nu'(z)\) near \(w=0\).

**Vector fields.** For any global holomorphic vector field \(V\), both \(V(z)=F(z,w)\) and \(V(w)=G(z,w)\) descend to entire functions. On the whole line \(L_j=\{z=a_j,w=0\}\) in stage \(X_j\), the differentiated stage equation gives
\[
 p_j'(a_j)F(a_j,0)=tG(a_j,0).
\]
Using \(t=0\) and \(t=1\) gives \(F(a_j,0)=G(a_j,0)=0\). The identity theorem at the accumulating roots gives \(F(z,0)=G(z,0)=0\) on all of \(\mathbb C\). Entire division by \(w\) follows from \(F(z,w)=w\int_0^1\partial_w F(z,sw)\,ds\) and likewise for \(G\). Thus \(F=wa,\ G=wb\) with \(a,b\in A\).

Conversely any such pair lifts, on each stage, as
\[
 V_\nu=wa\,\partial_z+wb\,\partial_w+
      (p_\nu'(z)a-tb)\partial_t.
\]
It annihilates the defining equation and is holomorphic. On \(w\ne0\), the lifts agree because they have the same two coordinate components; hence by density they agree everywhere on overlaps. Consequently the global vector-field module is freely generated over \(A\) by the lifts of \((w,0)\) and \((0,w)\). At each point of \(L_j\) their values span exactly the vertical line: both first components vanish and the first generator has last component \(p_j'(a_j)\ne0\). Away from \(w=0\) they span the tangent plane. Thus the tangent bundle is not globally generated, despite freeness of its global section module.

**Differential forms.** Contraction with the nowhere-zero \(\Omega\) is a bundle isomorphism \(TX\simeq\Omega_X^1\). On \(w\ne0\) contraction of the above lift is \(a\,dw-b\,dz\), so analytic continuation gives the same formula everywhere. Hence every global holomorphic one-form uniquely descends from \(\mathbb C^2\):
\[
 \Gamma(X,\Omega_X^1)=A\,dz\oplus A\,dw,\qquad
 \Gamma(X,\Omega_X^2)=A\,\Omega.
\]
The evaluation of the first module on \(L_j\) has rank one, since \(dz=(t/p_j'(a_j))dw\) there and \(dw\ne0\). For a one-form \(P\,dz+Q\,dw\),
\[
 d(P\,dz+Q\,dw)=w(\partial_z Q-\partial_w P)\Omega .
\]
Every entire \(h\) is of the form \(\partial_zQ\) by the entire primitive \(Q(z,w)=\int_0^z h(\zeta,w)d\zeta\) (or the straight-segment integral). Thus the image of \(d\) in degree two is exactly \(wA\,\Omega\). A closed global one-form descends to a closed entire one-form because pullback is injective on the dense coordinate locus. Such a form is exact: its entire primitive is
\[
 H(z,w)=\int_0^1[zP(sz,sw)+wQ(sz,sw)]\,ds,
\]
as differentiation using \(\partial_w P=\partial_zQ\) shows. The cohomology of the **complex of global holomorphic differential forms** is therefore
\[
 H^0=\mathbb C,\qquad H^1=0,\qquad H^2=A/wA\simeq\mathcal O(\mathbb C).
\]
This is not an assertion of holomorphic de Rham hypercohomology or of acyclicity of the sheaves on this non-Stein surface.

**Comparison with smooth de Rham classes.** The degree-two natural map from this global complex to smooth complex-valued de Rham cohomology is injective. Represent a class by \(f(z)\Omega\). The previously constructed spheres \(C_j\) have periods \(2\pi i\int_{a_{j+1}}^{a_j} f(z)dz\), by the same direct circle parametrization (which applies to entire functions). If the smooth class vanishes, all these periods vanish by Stokes. For an entire primitive \(B'=f\), the values \(B(a_j)\) are then constant; the identity theorem implies \(B\) is constant, so \(f=0\). This gives an infinite-dimensional space of smooth cohomology classes represented by global holomorphic top forms; no surjectivity claim.

## Other direct reading in this session

- §9.25 heading-only (blob 89f1c30a6df3c3df624fd05943a5cc64460824b8); no mathematical proof to certify.
- §9.26 entire mathematical lines 7–67, blob c04701d0358d43a3a3f1aed61e7cdd2a48305417, path docs/sections/separation-strict-exhaustions-and-coverings--local-holomorphic-separation-and-strict-exhaustion/index.html. In 9.26.1 (C1041DBBD4EC), local separation from the center suffices for finite sphere covering, strict local Hessian, and the summable seminorm construction. Its invoked regularized maximum is taken as a premise, not reopened. In 9.26.2 (A1FE9ED85940), the closed diagonal and graph in the products are the correct closedness statements, not closedness of the individual submanifolds in the ambient spaces; the reciprocal barrier gives proper sublevels. No new error.
- §9.27 complete direct mathematical lines 8–47; checked simple roots, inverses on \(z\ne a\) or \(w\ne0\), Hausdorff countable open union and escaping disc argument. Earlier selected historical work remains credited.
- §9.28 entire mathematical lines 7–141, blob ef92b5dc5bb4c143345621ea60ca52f3ca7d1872, path docs/sections/separation-strict-exhaustions-and-coverings--strictly-plurisubharmonic-exhaustions-on-coverings/index.html. Lemma 9.28.1 (source 83A0D387, tag 9DBBB1BAE0CF) correctly proves compact balls via total boundedness and finite extension of the radius. Prop. 9.28.2 (CD2B2989, E200BE9CFD9E) fixes a common sheet for the Cauchy tail before using inverse continuity. Prop. 9.28.3 (09F8EE91, 7808CCD76C79) correctly cancels sheetwise constants in positive-order derivatives; its ordinary Lipschitz distance mollification is distinct from excluded Demailly approximation. Thm. 9.28.5 (F653208F, 73159A8CF2BB) uses the complete metric \(g_0+d\psi\otimes d\psi\), and the convex base correction dominates the Hessian loss, ensuring properness by the distance lower bound. No new printed error or unclosed local step identified.
- §10.3 complete direct mathematical lines 7–158, blob 6f5ff9b768ca4f5c0892dc59398cfda1f7d44df3, path docs/sections/global-potentials-and-positive-cohomology-classes--normalized-potentials-and-minimal-singularities/index.html. Checked connected overlap propagation and normalization in 10.3.1, integrability/exponential scaling in 10.3.2–3, summable pole construction in 10.3.5, actual subnet and monotone-net premise in 10.3.6, minimal envelope in 10.3.8, modification pullback compactness and upper semicontinuity of an infimum of Lelong numbers in 10.3.9, and local Dirichlet comparison in 10.3.10. These are conditional on the cited internal inputs; no new transitive certificate. In particular sequential compactness is used in metric L1, not in arbitrary weak current topology.
- §9.29 only statement and initial context inspected; its Hörmander L2 programme is outside scope and not revisited. §10.2 only selected trace and Hodge formulas (10.2.11–15) inspected, no full-section certification.

## Disposition

Proposed addition: a remark following Example 9.27.1; no correction of its true non-Stein conclusion. The result describes a global differential complex and not the full sheaf cohomology. No downstream theorem refuted. Four whole mathematical direct readings, one heading-only, two selected; historical first visits not asserted. All dedicated Demailly approximation/regularization, Bergman, L2, Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof programmes remain deferred-by-user. No build, test suite, CI, publication or production edits.
