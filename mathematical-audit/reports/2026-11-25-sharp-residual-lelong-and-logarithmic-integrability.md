# Sharp residual Lelong bounds and anisotropic logarithmic endpoints

Date: 2026-11-25. Reviewed production main: b6933b772f41b45918f7e25ed1afbbb1fd892272. Starting audit head: 082bf508e976a211e6742e9b7bb707c273eb382f.
Read main AGENTS.md and documentation/proof-expansions.md, audit LATEST.md and README.md at these exact revisions, and the current numbered contents. No production edit.

## POME-BLOWUP-RESIDUAL-LELONG-SHARP-INTERVAL-001

Low / verified conditional deduction, not an error in the printed theorem.
Anchors: docs/sections/blowups-and-restricted-lelong-numbers/index.html, blob 9f495608f9c3fe1000ecfa5bbcd06693058e852f, Proposition 6.52.1 source tag B1934518 / permanent 3948CB675433, lines 21–46; Lemma 6.52.2 source tag 9CEC4F73 / permanent 3C256C55C09B, lines 51–68. Also docs/sections/projective-bundle-integration/index.html, blob 3bf371940d1159461d77d04b3a6e6ba8e5d0f065, Corollary 6.53.2 permanent 3B59FC78B4DD, lines 21–31.

Let pi blow up a smooth connected center of codimension at least two, E its exceptional divisor, T=pi_* T_hat for a positive closed (1,1)-current T_hat. Put b=nu(pi^*T,E), a=nu(T_hat,E), and c=nu(T,x) at x in the center. Lemma 6.52.2 establishes the residual identity R=T_hat-a[E]=pi^*T-b[E]. Since E is smooth, additivity gives nu(R,y)=nu(pi^*T,y)-b on its fiber over x. Proposition 6.52.1 and the fiber minimum formula of 6.53.2 consequently give
\[
 c-b\le \nu(R,y)\le 2c-b,\qquad
 \min_{y\in\pi^{-1}(x)}\nu(R,y)=c-b.
\]
Here 0<=b<=c, by positivity and the attained minimum. In particular a point blowup has b=c, since the minimum on the entire smooth exceptional divisor equals its generic number. For a point blowup the best uniform bound is therefore nu(R,y)<=c, half the coefficient in the printed general bound.

Both ends are sharp for each prescribed pair 0<=b<=c when the center has positive dimension. Work on P^n, n>=3, and blow up the linear center C={Z_1=...=Z_q=0}, 2<=q<n. Let x=[1:0:...:0]. With affine coordinates z_1,...,z_q,v_1,...,v_{n-q}, take
\[
 T=b[H]+(c-b)[D],\quad H=\{Z_2=0\},\quad
 D=\{Z_0Z_2+Z_1^2+Z_{q+1}^2=0\}.
\]
The quadric is smooth at x and does not contain C, whereas H contains C to order one. Both hypersurfaces have multiplicity one at x, so the downstairs Lelong number is c and the generic exceptional coefficient is b. In the chart z_1=t,z_2=tu_2,z_j=tu_j (j>=3), the local defining functions upstairs are tu_2 and tu_2+t^2+v_1^2. At the exceptional point with all centered coordinates zero both have order two. Hence the pullback Lelong number there is 2c and its residual is 2c-b. In the chart aligned with z_2, the functions become t and t+t^2u_1^2+v_1^2. At its centered exceptional point both have order one, hence residual c-b. One can take T_hat=pi^*T since pushforward gives T; the same residual identity also covers any allowed T_hat. For point centers take T=c[H] on P^n, n>=2, with H a hyperplane through x; its strict transform has multiplicity one along the fiber directions contained in H and zero on other directions, giving both endpoints 0 and c. The case c=0 is trivial.

Thus the printed factor two cannot be improved uniformly across positive-dimensional centers, while its point-center specialization can. This is distinct from the prior 2026-10-28 infinitely-near valuation example (which did not establish a uniform sharp residual interval with prescribed generic coefficient). Proposed addition: corollary after 6.52.2, preserving the general bound and all tags. Dependencies: the printed support/divisorial residual identity, the pullback Lelong comparison, generic-versus-minimal Lelong on a smooth divisor and the fiber-minimum formula. The downstream 6.56.1 uses the fiber minimum, not a mistaken upper bound. No source theorem refuted or full upstream chain certified.

## POME-DIAGONAL-LOG-WEIGHT-CRITICAL-DAMPING-001

Low / verified deduction in the explicit local model. Anchor: docs/sections/diagonal-logarithmic-weights/index.html, blob 6173c615897c1f0afe50c0c2f1ceae0020107fde, Lemma 6.54.1 source tag 8334DD33 / permanent F8F1C7EFDAD8, lines 12–42, especially equation 6.54.2 (permanent E7DD351F1AE3). The original criterion is correct. The following is an independent elementary proof and logarithmic endpoint refinement, not an extension/regularization argument.

Let S(z)=sum_j |z_j|^{2a_j}, a_j>0, beta in N^n, b_j=(beta_j+1)/a_j, B=sum b_j, and 0<R<1. For Euclidean Lebesgue volume dV and real p,c,
\[
 \int_{S<R}|z^\beta|^2 S^{-c}(\log(1/S))^{-p}\,dV
 =K_\beta\int_0^R s^{B-c-1}(\log(1/s))^{-p}\,ds,
\quad
 K_\beta=\frac{\pi^n}{\prod_j a_j}
 \frac{\prod_j\Gamma(b_j)}{\Gamma(B)}.
\]
Proof: integrate angular variables and substitute t_j=|z_j|^{2a_j}. Each factor becomes (pi/a_j)t_j^{b_j-1}dt_j. Substitute s=sum t_j, t_j=s y_j with y in the unit simplex. The Jacobian is s^{n-1}. The simplex integral of prod y_j^{b_j-1} equals prod Gamma(b_j)/Gamma(B), as follows by applying the identical substitution to the product of one-dimensional integrals of e^{-t_j}t_j^{b_j-1}. This argument uses only Tonelli on nonnegative integrands; the simplex integral is positive and finite since b_j>0. For n=1 it is one.

Putting L=log(1/s) gives the exact convergence test
\[
 \int_{\log(1/R)}^\infty e^{-(B-c)L} L^{-p}\,dL<\infty
 \iff B>c\ \text{or}\ (B=c,\ p>1).
\]
If B<c the exponential growth dominates every polynomial. At B=c and p=1 the divergence is logarithmic in L. For p=0 and B>c the integral is precisely K_beta R^{B-c}/(B-c), so its simple pole as c increases to B has residue in the variable B-c equal to K_beta. At B=c,p>1 the finite value is K_beta (log(1/R))^{1-p}/(p-1). No factorial is missing. This recovers the original strict criterion without the toric recession lemma.

For any holomorphic germ g on a sufficiently small polydisc, choose R so the closure of {S<R} lies inside that polydisc. Angular orthogonality and Tonelli identify its integral with the sum of the monomial integrals weighted by squared Taylor coefficients. Every exponent with nonzero coefficient must obey the displayed condition. The admissible exponents form an upward-closed subset of N^n, with finitely many minimal elements (Dickson's lemma). Assign each Taylor term to one of those minimal exponents dividing it; its quotient series converges absolutely on a smaller polydisc, hence is bounded on a yet smaller one. The finite sum of the corresponding generators times bounded holomorphic factors is integrable by the monomial calculation and the finite-sum squared norm inequality. Thus the weighted germ ideal is exactly generated by the stated exponents, including the boundary monomials if and only if p>1. The zero germ is automatic. The logarithmically damped weight need not be psh; in particular this is not a counterexample to strong openness for psh weights. No general multiplier-ideal coherence, extension or approximation statement is invoked.

Affected: the elementary monomial test at 6.55.2 lines 74–90 (unchanged for p=0). Proposed independent proof or optional endpoint corollary at 6.54.1. Distinct from earlier finite-generation and integer rounding examples. The approximation invoked by 6.55.2 at line 72, permanent dependency 080EF8C715CF, remains deferred-by-user.

## Actual additional review and unresolved inputs

- §6.52 entire mathematical lines 8–68, blob above. The angular monomial matrix preserves Haar probability (integer determinant one); the negative logarithm reverses the two mean inequalities. Support and Siu subtraction inputs retained.
- §6.54 entire mathematical lines 8–42, blob above. Verified normalization of full metric weight, strict recession boundary, Taylor orthogonality and ideal generation by the independent computation.
- §6.51 selected lines 11–57 and 72–154, docs/sections/radial-growth-and-residual-mass/index.html, blob 3b7a7a2965306db7a2bde4c5f91c171bae685546. Checked residual log-convexity weighted integration by parts, uniform annular mass control, graph-Crofton dominated convergence and cutoff equality of collar masses. Permanent tags BE4AE95DA940, 30125A1CC71C, E8283D7F161B. Classical product continuity, Crofton normalization and all the zero-Lelong construction upstream inputs are not transitively certified; numerical Corollary 6.51.9 not claimed reviewed. §6.50 read for context only; no coverage upgrade.
- §6.55 selected nonexcluded lines 9–70, 74–96 (same chapter), docs/sections/concentrating-restricted-singularities/index.html, blob 3167593400ca0dd405a850fbafd634d0f0b97e48, permanent tags 279034C7A935 and F6E99CEFC668. Checked degree cancellation, density total mass and boundary comparison direction, local limiting inequality, strict exponent rounding and Zariski-dense restriction. The explicit gentle analytic approximation step at line 72 stays deferred; the smooth compact MA and normalized compactness inputs are retained conditionally. Not a whole-section certificate.
- §6.56 selected historical-repeat lines 22–73, docs/sections/singularities-along-a-compact-center/index.html, blob e2174cb28e3fdf0ce5c7b63ec4bdd6f774b55516, source 6F802F01/permanent 4E92E37E64AC. Checked exceptional normal-bundle convention, normalized closed fiber mass, Poincare–Lelong subtraction sign, codimension-two extension distribution gluing and affine cohomological mass bound. Earlier uniform-center improvement of 2026-10-23 is not new. Grassmannian extension 9.72.1, resolution, fiber restriction and psh extension remain inputs.
- §6.53 selected repeat lines 21–31, fiber minimum used above; prior full direct status retained.

Two whole direct current sections, three selected nonexcluded principal sections and one selected repeat dependency. No new confirmed errors or demonstrated proof gaps, two new deductions, zero full transitive proof-chain certifications. Legacy first visits not claimed. All excluded Demailly approximation/regularization and its dedicated Bergman, L2, OT, multiscale and positivity-loss proof-completion records remain deferred-by-user. No builds, tests, CI, source, registry, permanent tag or website edits.
