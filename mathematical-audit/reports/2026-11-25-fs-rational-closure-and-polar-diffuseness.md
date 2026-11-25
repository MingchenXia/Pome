# Rational Fubini–Study closure and Sobolev diffuseness of bounded potential differences

Reviewed production main: b6933b772f41b45918f7e25ed1afbbb1fd892272. Starting audit head: 99840a8d0e4c2553394d8faa676780f9ce66a667. Date: 2026-11-25.

## POME-FS-RATIONAL-FINITE-OPERATIONS-001

Low / verified deduction from the printed definitions; a quantifier clarification is proposed, not a false theorem finding.

Integrated file: docs/sections/plurisubharmonic-functions--plurisubharmonic-metrics-on-line-bundles/index.html, blob 0fd91c7a6a8228fef2ac1328a80f40c4609b5e0f. SGPT source FBA740A0 / permanent 9FE903B6E5A8 (Definition 5.20.14, lines 180–191); source CE1E7AF0 / permanent 8FCD7BEEDD56 (Definition 5.20.15, lines 195–207). The heading says Q-convex combinations but the accompanying quantifier says t in (0,1) without explicitly restricting t to Q.

Fix a reference metric h0 on a line bundle L on a connected compact complex manifold as in the section. For two nontrivial FS potentials write
\[
\phi_i=m_i^{-1}\max_j(\log |s_{ij}|_{h_0^{m_i}}^2+\lambda_{ij}),\qquad i=1,2,
\]
with positive integer m_i and rational lambda_ij. A maximum of the two is again FS: choose M a common multiple of m1,m2, replace each section by its (M/m_i)-th tensor power and each lambda by (M/m_i)lambda, then take the union of both lists. This is the pointwise minimum operation on metrics. Zero sections can simply be omitted.

For rational t=a/b in (0,1), with 0<a<b integers, let q=lcm(m1,m2), M=bq, p=aq/m1 and r=(b-a)q/m2. All p,r,M are positive integers. The sections
\[
s_{1j}^{\otimes p}\otimes s_{2k}^{\otimes r}\in H^0(X,L^M)
\]
and rational weights p lambda_1j+r lambda_2k give exactly t phi1+(1-t)phi2 after taking the maximum over pairs and dividing by M. The identity holds on the finite locus, and also at poles since a maximum over a finite list is minus infinity exactly when every section vanishes there. Products of nonzero sections are not identically zero on connected X. Therefore FS is closed under both operations; for the rational interpretation, generalized FS equals FS (also if FS is empty, since the empty set is closed under these binary operations).

If instead t ranges over all real (0,1), this equality is false. On P^1 with L=O(1) and the Fubini–Study reference h0, take phi1=log |Z_0|^2_{h0}, and phi2=max(log |Z_0|^2_{h0},log |Z_1|^2_{h0}); both are FS with m=1 and zero rational weights. In the chart Z_1 !=0 and z=Z_0/Z_1, near z=0, phi1=log |z|^2-log(1+|z|^2) and phi2=-log(1+|z|^2). Thus the real combination with irrational t has local expansion t log |z|^2+O(1). For every nontrivial FS potential the coefficient of log |z|^2 at that point is min_j ord_0(s_j)/m, necessarily rational: the minimum-order terms dominate a finite maximum, and the reference metric contributes only a smooth weight. The irrational combination is therefore not FS. This uses neither regularization nor section extension.

Proposal: explicitly write t in Q intersect (0,1) if the Q-convex heading is intended, and optionally record closure as a lemma. If real combinations are intended, change the heading and retain the distinct generalized class. Downstream: any use of 5.20.15 that identifies generalized FS with FS or asserts rational singularity coefficients requires this distinction; no particular downstream theorem is declared false, and an exhaustive reverse-dependency search was not performed. No changes to the body or permanent tags.

## POME-POLAR-BOUNDED-DIFFERENCE-SOBOLEV-DIFFUSE-001

Low / verified conditional deduction, not a printed error.

Integrated file: docs/sections/plurisubharmonic-functions-and-singularities--polar-curvature/index.html, blob 334a5f34230c1da094a6822f30408e669f052b4b. Sources non-kahler-pluripotential-theory:43D9FD13 / 8F61C8BDD569 (Lemma 5.46.1, lines 11–24); 98A2FD1E / EB97F93DAD74 (Lemma 5.46.2, lines 29–50); F9AAD931 / 09F56C9DE42C (Proposition 5.46.3, lines 58–80).

Under the bounded-difference hypotheses of 5.46.3, its conclusion holds on every locally pluripolar Borel set B, not just the common pole set. More generally in each coordinate ball, every real or imaginary coefficient measure of dd^c(u-v) vanishes in total variation on Borel sets of zero relative W^{1,2} capacity. Here capacity zero means every compact subset K has smooth tests with values in [0,1], equal to one near K, compactly supported in the ball and tending to zero in W^{1,2}. No statement about higher Hessian products is intended.

Proof: write w=u-v off the common pole set and extend arbitrarily there; the pole set has Lebesgue measure zero. Lemma 5.46.1 gives w in W^{1,2}_loc because w is locally bounded and its distributional Laplacian is a signed Radon measure. Each coefficient measure nu of dd^c w, or its real/imaginary part, is thus a bounded functional on W^{1,2}_0 of each relatively compact smaller ball D: integration by parts bounds its action on smooth tests by C ||grad w||_{L^2(D)} ||grad test||_{L^2(D)}. For a compact K of zero capacity in the positive Hahn set of nu, choose an open O compactly contained in D containing K with nu^-(O)<epsilon. Given capacity tests psi_j, multiply by a fixed smooth cutoff supported in O and equal to one near K. The resulting tests eta_j remain in [0,1], equal one near K, have support in O, and tend to zero in W^{1,2} by the product rule. Then
\[
\nu^+(K)\leq \int\eta_j\,d\nu^+
\leq |\langle \nu,\eta_j\rangle|+\nu^-(O).
\]
First j -> infinity, then epsilon -> 0 gives nu^+(K)=0. Inner regularity on B intersect the positive Hahn set gives nu^+(B)=0; applying the argument to -nu gives nu^-(B)=0. For a locally pluripolar B, work in countably many relatively compact coordinate neighborhoods on which B lies in the pole set of a nontrivial local psh function. Lemma 5.46.2 supplies exactly these tests for every compact subset of B. Countable covering yields the assertion globally. Smooth forms give these sets zero mass (capacity zero implies zero Lebesgue measure directly from the L^2 norm of tests), so for arbitrary smooth real backgrounds theta,beta one obtains
\[
1_B(\theta+dd^c u)=1_B(\beta+dd^c v).
\]
In particular the printed common-pole identity is a special case. The argument is also valid whenever w is locally W^{1,2} and its complex Hessian has measure coefficients, with no need for w to be bounded or itself a difference of quasi-psh functions.

Scope: local Euclidean estimates and cutoff lemma as printed, not a transitive verification. Potential dependents: polar curvature on fixed Borel carriers and subsequent trace comparisons, with no new implication about nonlinear Monge–Ampere measures. This is distinct from the earlier affine reweighting result.

## Direct reading and dependencies

- §5.20, selected nonexcluded mathematical lines 7–207 and 285–323, blob above: Hermitian norm convention, Poincare–Lelong sign, FS model on P^1, metric tensor product and convex-fiber counterexample. For the latter the two radial complex Hessians of the exhaustion are respectively 1/(|s|^2-1)^2 and 4/(4-|s|^2)^2; the two real fiber balls are disjoint and the absolute-value cusp violates submean. Lines 214–280 (OT extension and Bergman approximation) explicitly deferred-by-user; not reviewed.
- §5.45, whole direct mathematical lines 7–28, docs/sections/plurisubharmonic-functions-and-singularities--curvature-of-line-bundles/index.html, blob 28b44ce67341b26ec1d01db0feaa83adbb6b357a, tag 620B099907AB: frame change subtracts log|g|^2 and d(theta+dd^c u)=dtheta. Prior integral-period obstruction not relogged.
- §5.46, whole direct mathematical lines 7–170, blob above: energy estimate, capacity-zero tests, Jordan decomposition, elliptic trace injectivity, proper pushforward/restriction, cutoff chain rule and fixed-measure dominated convergence. Local potential and elliptic regularity inputs (5.4.3 and general elliptic theory), pullback (5.43.18), and bounded BT chain rule/energy convergence in 5.46.7 are conditional upstream inputs; no complete certification of them. Ordinary local convolution in the printed Sobolev proof is not the excluded Demailly approximation programme.
- Chapter 5 actual ToC checked: 66 numbered sections; matrix retains the existing 747 numbered rows. Historical first-ever coverage not asserted.

Two whole direct sections (one of them previously sampled), one nonexcluded selected section, two deductions, one clarification candidate within the first deduction, zero newly confirmed false theorems, zero newly demonstrated proof gaps, zero complete upstream proof-chain certifications. No tests, build, CI, production/source/registry/tag/site edits. All user-excluded programmes remain deferred-by-user, not resolved.
