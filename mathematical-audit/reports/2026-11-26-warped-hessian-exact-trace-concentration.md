# Exact warped-product trace concentration and finite-end distance; threshold and d_S rotation

Date: 2026-11-26. Reviewed main: b6933b772f41b45918f7e25ed1afbbb1fd892272. Audit-only proposal. No production changes, tests, builds, CI or publication.

## POME-WARPED-HESSIAN-EXACT-EXTREME-TRACE-001

Severity low; verified conditional deduction, not a false printed theorem. Integrated file docs/sections/a-gauduchon-variational-volume--the-hessian-metric-and-its-completion/index.html, blob 23a7f2a1dab791569c39a0ff5f056f52bfc200fe. Theorem 12.6.32 (40DF235D735C; source 14DB163A), Proposition 12.6.36 (02AE1B3B4027), Lemma 12.6.39 (1EF963CF5EA2), Proposition 12.6.49 (94A159D3DBDB; source 6E3D6B9F), Proposition 12.6.51 (2AC49E96484C; source A9E94D54). Physical lines 610–1062, specifically 719–780 and 929–983. Retain the printed assertions and add the following sharper conclusion, conditional for the geometric application on the existing warped-product metric construction. No regularization input is used in the additional argument.

Use the original assumptions: compact connected Kähler base B of complex dimension m>=2, smooth positive probability volume sigma, smooth nonconstant a, and compact curve C with area form w of integral one. At a specified end take f=a or f=M-a, as in Lemma 12.6.39. Its zero set consists of finitely many disjoint smooth compact submanifolds Z_i, with f comparable to dist(Z_i)^k_i in full tubes. Put d_i=real codimension, r_i=d_i/k_i, r=min_i r_i.

**Intrinsic leading-order measure.** In a Riemannian normal tubular identification at Z_i, write f(exp_z y)=P_z(y)+O(|y|^(k_i+1)), with P_z homogeneous of degree k_i on the real normal fiber. The original smoothness and two-sided power bound imply that k_i is a positive even integer: along any fixed normal ray the first nonzero Taylor coefficient must occur at precisely the comparable power, since infinite flatness would contradict the lower bound. The lower coefficients therefore vanish for all rays, and the degree k_i Taylor polynomial is strictly positive away from zero with uniform upper and lower bounds on the unit normal sphere. Smoothness and compactness give a uniform remainder. No extra nondegeneracy hypothesis is necessary. Express sigma in normal coordinates as a smooth positive density J(z,y) times induced submanifold volume and Euclidean normal volume. Define the finite positive measure
\[
 dA_i(z)=J(z,0)\,\operatorname{vol}_{N_zZ_i}\{y:P_z(y)<1\}\,d\operatorname{vol}_{Z_i}(z).
\]
Set A=sum of A_i over r_i=r, regarded as a measure on B, and write A_*=A(B)>0.

For every continuous test function g on B,
\[
 F_g(t)=\int_{\{f<t\}}g\,\sigma=t^r\left(\int g\,dA+o(1)\right).
\]
Indeed in each tube substitute y=t^{1/k_i}Y. The lower power bound restricts Y to a fixed bounded ball; the indicator converges almost everywhere to that of P_z(Y)<1 (its boundary has normal Lebesgue measure zero by homogeneity and positivity). The other factors converge to g(z)J(z,0); dominated convergence on the compact normal disk bundle proves the contribution t^{r_i}. The complement has no contribution for small t. This also proves independence of the tubular choice for A by the intrinsic left-hand side.

For q>0 put I_q(g,e)=integral_B g sigma/(f+e)^q. The exact asymptotic formulas as e tends to zero are:
\[
 \begin{aligned}
 e^{q-r} I_q(g,e)&\longrightarrow r\,\mathrm B(r,q-r)\int g\,dA &&(q>r),\\
 I_r(g,e)/\log(1/e)&\longrightarrow r\int g\,dA &&(q=r),\\
 I_q(g,e)&\longrightarrow\int_B g f^{-q}\sigma &&(q<r).
 \end{aligned}
\]
Here B denotes the beta integral. To prove the first two, use the layer formula I_q(g,e)=q integral_0^infty F_g(t)(t+e)^(-q-1) dt; Fubini is justified for fixed e by the absolute bound using |g|. For q>r scale t=e u, and use |F_g(t)|<=C t^r on the positive axis after increasing C. The integrable majorant is Cq u^r/(1+u)^(q+1); the resulting constant q B(r+1,q-r)=r B(r,q-r) by integration by parts. For q=r fix a small t0. The integral of t^r/(t+e)^(r+1) from 0 to t0 equals log(1/e)+O(1): split at e and compare with 1/t above e, where the integrated difference is bounded by a constant times integral_e^t0 e/t^2. The o(t^r) error is bounded by any prescribed multiple of t^r after decreasing t0; the integral above t0 is uniformly bounded. This proves the logarithmic limit, including signed g. For q<r, f^{-q} is integrable by the tube bounds, so dominated convergence suffices.

**Exact normalized trace limit.** In the setting of 12.6.49–51 write L_j=s_j(f+e_j), s_j->s_0>0 and b_j->b>0. For 1<r<=2,
\[
 \frac{\sigma/L_j^2}{\int_B\sigma/L_j^2}\rightharpoonup A/A_*,
 \qquad
 T_j=\frac{\gamma_j^m}{t_j}\rightharpoonup p_B^*(A/A_*).
\]
Thus the entire sequence converges even for several positive-dimensional extreme components. The limit gives component weights A_i(Z_i)/A_* (zero for r_i>r). By 12.6.50 the other term m A_j^{m-1} wedge w has trace m b_j^{m-1}, uniformly bounded, whereas the first term's trace diverges. This proves the current limit, with pullback under the product projection defined by fiber integration on test forms. The normalization is exact:
\[
 t_j\sim \frac{A_*}{n s_0^2}
 \begin{cases}
 r\,\mathrm B(r,2-r)e_j^{r-2},&1<r<2,\\
 2\log(1/e_j),&r=2.
 \end{cases}
\]
The numerator and denominator in 12.6.51 are exactly n b_j^m/t_j, so the corresponding leading constants follow by inversion. All assertions also hold for arbitrary nets of coefficient parameters tending to the same end: scalar limits as e->0 hold on the ordinary real parameter, while the uniformly bounded positive remainder tends to zero against each fixed smooth test form. No extraction of a sequential subnet is needed.

**Exact finite-end Hessian distance.** For r>1 let H0=integral f^{-1}sigma. In the notation of 12.6.40 use H=I_1(1,e), J=I_2(1,e), K=I_3(1,e). Then
\[
 G_f(e)\sim
 \begin{cases}
 C_r e^{r-3},&1<r<3,\\
 C_3\log(1/e),&r=3,\\
 C_\infty,&r>3,
 \end{cases}
\]
where C_r=2 A_* r B(r,3-r)/(n H0), C_3=6 A_* /(n H0), and C_infty=(2/n)(I_3(1,0)/H0-(I_2(1,0)/H0)^2)>0. For 1<r<2, J^2/K=O(e^{r-1}) tends to zero; for r=2 it is O(e log^2(1/e)); for 2<r<=3, J is bounded and K diverges. For r>3 all moments converge and the limiting variance is strictly positive because f is nonconstant under the positive probability with density 1/(H0 f). The distance along the Euclidean R coordinate to the completed boundary line, at fixed b, is integral_0^e sqrt(G_f(t)) dt. The resulting equivalents are
\[
 \frac{2\sqrt{C_r}}{r-1}e^{(r-1)/2},\qquad
 \sqrt{C_3}\, e\sqrt{\log(1/e)},\qquad
 \sqrt{C_\infty}\,e,
\]
respectively. The middle equivalent follows by substituting t=e u and dominated convergence with the integrable bound sqrt(1+log(1/u)) on (0,1). These are intrinsic to the three-parameter family, not the full background space. The printed estimates remain valid. Potential dependents: 12.6.41, 12.6.49–51, examples 12.6.53–54; no assertion about arbitrary endpoint solutions or infinite-order/intersecting extreme strata.

## POME-DS-DECREASING-NET-CLAUSE-LABELS-001

Low / confirmed proof cross-reference error, NOT a false theorem and NOT a missing mathematical argument. Integrated docs/sections/comparison-of-singularities--the-d-s-pseudometric/index.html, blob 1c3f119a636ff59de0407c7fb2278d35f2d81b2d. Corollary 16.9.14 tag F84D53FDA599; physical lines 270–358. The three clauses are d_S convergence (1), convergence of every mixed mass (2), convergence of top mass (3, under positive limiting mass). The proof at lines 311–317 correctly establishes 1 iff 2 via Lemma 16.9.7. It then labels the k=n specialization "2 implies 1" and the argument starting "Assume (3)" as "1 implies 2". These must be 2 implies 3 and 3 implies 2, respectively. The actual stretching argument under (3) at lines 325–343 gives limsup mixed mass <= target by b_j->infinity and the opposite bound by monotonicity; the equality case at lines 317–323 and envelope identification at 345–357 are consistent. Correct the source-level clause references, including structured link targets, not just visible numbers; preserve all permanent clause tags. Proof logic survives this repair, conditional on existing §§16.8.7, 16.8.22–23, 16.3.9, 16.3.14, 16.4.3 and 13.13.11. No downstream mathematical conclusion refuted. No production patch applied.

## Coverage and dependencies

- Selected §12.6, physical 610–1062 (warped product construction, derivative and variance, finite ends, fiber tests, bounded endpoint equations, base-potential convergence, cofactor trace and explicit examples). Also selected physical 7–226 (homogeneous radial splitting and first examples, invariant mean, balancedness and matrix Hessian). The middle invariant-metric development is not included in this coverage claim. Fixed-volume Hessian equality and smooth/continuous base MA existence, stability, uniqueness and bounded product inputs are conditional on cited internal results; no transitive certificate.
- Whole direct conditional §15.32, docs/sections/equations-with-prescribed-singularities--stability-of-the-subsolution-threshold/index.html, blob 903ae0ce7173604063a833295dd94e971b18fd72, physical 7–294. Checked infimum semicontinuity and truncation sup formula (15.32.1 D988D47D5E0E, source 7D3A6CA8), lattice norm triangle inequality and lower semicontinuity, graph-norm completeness (15.32.5 4C06D1B94BD1), failure of root-norm completeness at infinite upper mass (15.32.6 C926F63790E3: nonnegative Cauchy series converges in L1 but its limit dominates each summand whose Ln norms grow), uniform-tail criterion and density of smooth roots (15.32.9 2210D4123A64), and exact product-factor isometry and log tail (15.32.11 7A2CC1A3258E). The convergence-in-measure argument on bounded sets uses finite volume and uniform boundedness; the Ln part follows by the same truncation argument, not a need to assume pointwise convergence of the entire sequence. Cited threshold variational representation, scalar mass bounds, examples, subcritical estimate and product formula remain conditional; no new error identified here.
- Selected §16.9 physical 7–358: ray join, P-preorder equality, mass formula, continuity and monotone nets. Only the clause-reference error above is newly recorded; no complete §16.9 claim. The actual ray metric, nonpluripolar monotonicity, stretching and model-envelope premises remain internal inputs, not re-certified.

All excluded Demailly approximation/regularization and dedicated Bergman/L2/OT/multiscale/positivity-loss programmes remain deferred-by-user. Historical first visits are not asserted. One whole direct conditional section, two selected sections, one new conditional deduction and one proof cross-reference defect, zero newly demonstrated false theorem statements, zero substantive new proof gaps, zero complete upstream certifications.
