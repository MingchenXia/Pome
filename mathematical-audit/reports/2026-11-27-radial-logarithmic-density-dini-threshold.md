# Radial logarithmic density errors and singular obstacle envelopes

Date: 2026-11-27. Reviewed main: b6933b772f41b45918f7e25ed1afbbb1fd892272. Starting audit head: 9670cdb4f4a0b6b39eb6adcb9064d07400e29995.

## Scope and disposition

Direct complete mathematical reading of current integrated §§11.46 (physical lines 7–242, blob 2b3580e24274771d63446a63973adfd55402892a) and 11.47 (lines 7–230, blob 6b7ce2bc15721b43ea2b2294294cfcca84be2ff3). Their paths are respectively
- docs/sections/normalization-and-weak-adjoint-measures--residual-regularity-in-radial-singularity-types/index.html
- docs/sections/normalization-and-weak-adjoint-measures--envelopes-for-singular-radial-obstacles/index.html

These are new whole direct conditional coverage entries in the current matrix, not assertions of historical first visits. No new false printed theorem or demonstrated proof gap. Existing bounded-product, truncation and local PSH extension inputs are conditional, not transitive certificates. Demailly regularization and its dedicated prerequisites remain deferred-by-user.

## POME-RADIAL-DENSITY-LOG-DINI-THRESHOLD-001

Low severity; verified conditional deduction, not a printed error. Theorem 11.46.8 (source 084E3C9F, permanent F273E69013C1, lines 67–127) assumes a power error O(r^delta). Proposition 11.46.17 (source 9C7D8406, permanent F4F876167D51, lines 174–202) proves sharp derivative thresholds for such errors. The following instead identifies the sharp threshold for logarithmic errors and an exact weighted Dini criterion for one-sign errors.

Keep the hypotheses of 11.46.8 concerning k, alpha, the reference, smooth radial nonnegative probability density q off o (including infinity). Replace only (11.46.9) by g(r)=q/q_alpha-1=o(1) as r decreases to zero. Put t=-log r, L=1+t, b=k(1-alpha), a(t)=Q_alpha(e^{-t})^k. Then the radial inverse still gives a genuine normalized kappa-PSH potential U, with unit non-pluripolar mass and canonical sublogarithmic pole. It need not have the same ordinary type.

Claim: if
\[
  \int_{t_0}^\infty |g(e^{-t})|(1+t)^{\alpha-1}\,dt<\infty,
\]
then the residual R=U-u_alpha extends continuously at o. If g is eventually of one sign, this criterion is also necessary for boundedness of R, hence for ordinary type equality. In particular for |g|=O(L^{-beta}) with beta>alpha the ordinary type is retained. The threshold beta>alpha is sharp, including the endpoint.

Proof: the exact inverse (11.46.11), lines 87–94, defines Q=M^{1/k} and U'=(Q-P)/r with U(infinity)=0. Positivity near o, smoothness away from o and at infinity, and nonnegative radial/tangential eigenvalues follow as in 11.46.8. The reference estimates (11.46.6), lines 48–55, imply a(t)~alpha^k L^{-b} and -a'(t)~b alpha^k L^{-b-1}. The cumulative error is exactly
\[
 E(t)=M(e^{-t})-a(t)=\int_t^\infty g(e^{-s})(-a'(s))\,ds .
\]
In particular |E|/a <= sup_{s>=t}|g(e^{-s})| ->0. Consequently Q/Q_alpha ->1, and the positive-root mean-value theorem yields constants independent of large t such that
\[
 |Q-Q_\alpha|\asymp L^{(k-1)(1-\alpha)}|E(t)|.
\]
In the t variable dR/dt=-(Q-Q_alpha). Since Q~alpha L^{alpha-1}, integration also shows U(t)~ -L^alpha, so the canonical pole exists and the local decreasing radial truncation argument applies. Its non-pluripolar measure has exactly the given density away from o, excludes o, and has total mass one.

Write d=(k-1)(1-alpha). The integral of |dR/dt| is bounded by a constant times
\[
 \int_{t_0}^\infty L^d\int_t^\infty |g(e^{-s})|(1+s)^{-b-1}\,ds\,dt.
\]
Tonelli gives the integral in s with weight
\[
 (1+s)^{-b-1}\frac{(1+s)^{d+1}-(1+t_0)^{d+1}}{d+1}.
\]
For large s it is comparable to (1+s)^{d-b}=(1+s)^{alpha-1}. This proves sufficiency; no interchange of signed integrals is used. If g has constant sign on the tail, the absolute value of E equals its corresponding positive integral, and dR/dt has fixed sign there. The same comparison now proves necessity for boundedness; if the integral diverges, R diverges with sign opposite to g. The sign-changing case is asserted only in the sufficient direction.

More precisely, suppose g(e^{-t})~c L^{-beta}, beta>0, c nonzero (signed asymptotic). Integration of the exact tail, using the reference asymptotic and a relative error uniformly small on s>=t, gives
\[
 E(t)\sim \frac{c b\alpha^k}{b+\beta} L^{-b-\beta},
 \qquad Q-Q_\alpha\sim C L^{\alpha-1-\beta},
 \qquad C=\frac{c\alpha(1-\alpha)}{b+\beta}.
\]
Hence
\[
\begin{array}{ll}
 R(t)\sim -\frac{C}{\alpha-\beta}L^{\alpha-\beta}, &0<\beta<\alpha,\\
 R(t)\sim -C\log L, &\beta=\alpha,\\
 R(t)-R_\infty\sim \frac{C}{\beta-\alpha}L^{\alpha-\beta}, &\beta>\alpha.
\end{array}
\]
These signs follow from dR/dt=-(Q-Q_alpha). The equivalences with nonzero leading coefficients follow by integrating a uniform relative error on a sufficiently late tail (or the standard elementary comparison of integrals); constants of normalization do not affect the divergent cases.

For explicit compact sharpness examples choose a radial smooth cutoff chi_0 supported in r<1, equal to one near zero, and a nonzero nonnegative chi_1 supported in a disjoint finite annulus. Define q=q_alpha[1+c(L^{-beta}chi_0-B chi_1)], with the first term understood as zero outside its support and B chosen as the ratio of the two integrals against q_alpha kappa^k. A small nonzero signed c gives positive density everywhere off o and exact probability mass, retaining smoothness at infinity. This realizes all three regimes without a formal local-only solution. In particular q/q_alpha ->1 and all finite-weight multiplier ideals remain trivial (U~ -L^alpha as a growth asymptotic, alpha<1), but the ordinary singularity type changes for beta<=alpha. Here the growth asymptotic is not ordinary-type equivalence.

The printed power-error theorem remains unchanged. Proposed optional addition immediately after 11.46.17: logarithmic/Dini refinement with the one-sign necessity explicitly retained. Corollary 11.46.22's product residual conclusion extends to the Dini-sufficient case with continuity only, conditional on its product measure identity; the original higher regularity statements are not claimed for logarithmic errors. No claim for nonsymmetric solutions.

## Other direct checks

- 11.46.2 (2E23F061 / 3CE4F16CE935, lines 21–58): reference determinant normalization, exact slope limits and integrability exponent; multiplier ideal integral converges for each finite weight. 11.46.15 (8DE2B504 / 33B8FF26FB4B, lines 145–168): logarithmic derivatives of the cumulative error have the stated sign, and arbitrary exponential flatness absorbs each r^{-j}. 11.46.17: compensation mass and sharp derivative coefficients checked. 11.46.20 (005BE737 / 7D9147EC36A1, lines 208–221): open zero-annulus construction keeps positive cumulative central mass. 11.46.22 (BEDA2B56 / 7C248BB2EDD2, lines 227–242): product binomial factor, truncation, and v_- implication correct conditional on bounded product calculus.
- 11.47.2 (E8945F16 / 3CD979065654, lines 27–40) and 11.47.5 (CFB699D8 / 7444FA94A222, lines 56–102): tangent asymptotics, contact derivative inequalities, slope bounds, left and both right tail alternatives checked. The lower bound A-||F|| and upper bound A+F force ordinary type and canonical value at o.
- 11.47.8 (5490AE95 / EA98BEE991F7, lines 107–122): radial flux increments, absence of atoms at finite radii and hyperplane, total mass, and sup norm nonexpansiveness. 11.47.11 (62FDF78C / 278AD9E56CEA, lines 134–184): contact-set derivative equality a.e., tail derivative sign, bounds in the inverse radius coordinate and interpolation exponent checked; no C^{1,1} convergence claim.
- 11.47.14 (609D1A19 / E4713F2FEF7D, lines 193–218): exact slice bound also follows immediately without the displayed local convolution argument. On a product coordinate polydisk take a local smooth potential phi(z) for kappa and a smooth q(y) with dd^c q >= h_0. Then v+phi(z)+q(y) is genuinely PSH. Restricting to y=y_0 gives PSH or identically -infinity, and subtracting the constant q(y_0) gives the exact kappa bound. Local identically -infinity restrictions patch via the connected slice and the PSH alternative on overlaps. This is merely a direct simplification of the printed argument, not a separate new finding or any global regularization input. The rest follows by competitor comparison and dimensional product calculus. 11.47.15 (DF9FEFA9 / 1E30DC99E57B, lines 223–230): invariant Hopf metric and sign d(ds wedge d^cs)=-ds wedge dd^cs checked.

No project tests, build, CI, publication, source edits or full upstream certification. Prior reports/ledger retained; no historical first-visit claim.
