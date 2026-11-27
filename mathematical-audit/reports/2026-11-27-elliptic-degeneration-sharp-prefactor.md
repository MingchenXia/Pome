# Elliptic surface degeneration: exact leading prefactor

Date: 2026-11-27. Reviewed main: b6933b772f41b45918f7e25ed1afbbb1fd892272.
Starting audit head: 8a260b600cc1905c507220736fca1ed1fce79aca.

## POME-ELLIPTIC-DEGENERATION-SHARP-PREFACTOR-001

Severity low; status **verified conditional deduction**, not a printed error.
Current integrated file:
`docs/sections/a-gauduchon-variational-volume--orders-of-degeneration-at-the-nef-boundary--elliptic-surface-volumes-and-order-spectra/index.html`
(blob 0218ee5a373d19c4b293d9d492ba3b1fdffdef6a).
Whole mathematical lines 7–144 reviewed. Proposition 12.21.1
(permanent DE2BA13B1A92, source 494B4B98), lines 26–50;
Proposition 12.21.4 (58574FAEC5B7, DF362DC6), lines 55–78;
Proposition 12.21.5 (41097C9AFBD2, 20FC0A7D), lines 83–144.
The latter's equations 12.21.6–7 and Step 2, lines 115–143, provide
logarithmic errors only. The following gives a relative asymptotic.

Keep the exact probability form, perturbation, and coefficients of
12.21.5. Write epsilon = exp(-L), p(t)=P(t)/t, where P is the printed
oscillating profile or P(t)=sigma*t, with 0<alpha<=p<=beta<1.
Then, as L tends to infinity,

\[
 I\sim \pi e^L/L,\qquad
 K=(1+o(1))\pi e^{L-P(L)}L^{-2}J(p(L)),
 \quad J(b)=\int_{\mathbb R}\frac{e^{-bs}}{1+e^{-s}}\,ds
 =\frac{\pi}{\sin(\pi b)}.
\]
Consequently
\[
 \mathcal V_\mu(\theta+e^{-L}h)
 =(1+o(1))\frac{2\pi}{L\sin(\pi p(L))}e^{-L-P(L)}.
\]
The error is relative along the entire real limit, not just subsequences.
In particular for P(t)=sigma*t the volume is asymptotic to
\[
 \frac{2\pi}{\sin(\pi\sigma)}
 \frac{\epsilon^{1+\sigma}}{\log(1/\epsilon)} .
\]
Thus the ratio to the pure power epsilon^(1+sigma) tends to zero,
even though the logarithmic order equals 1+sigma.

### Proof

In the printed construction the complement of the coordinate disk
contributes O(1) to both integrals. On the disk the area substitution
t=|zeta|^-2 yields exactly pi*t^-2 dt, as in lines 115–118.
For I divide by pi*e^L. On t>=L the logistic factor
(1+exp(L-t))^-1 differs from 1 by at most exp(L-t); integrating the
difference against t^-2 costs at most L^-2. The integral of t^-2
over [L,infinity) equals L^-1. On [L/2,L] the factor is at most
exp(t-L), giving at most 4/L^2. On [T0,L/2] it is at most exp(-L/2),
giving O(exp(-L/2)). This proves the first asymptotic.

For K, normalize the local integral by pi*e^(L-P(L))*L^-2.
Its integrand after t=L+s is
\[
 \mathbf1_{s\ge T_0-L}
 \left(\frac L{L+s}\right)^2
 \frac{\exp(P(L)-P(L+s))}{1+\exp(-s)}.
\]
The printed derivative bounds c0<=P'<=d0<1 imply that on
[T0,L/2] the normalized integral is bounded by
\[
 L^2 e^{-(1-d_0)L/2}\int_{T_0}^\infty t^{-2}\,dt=o(1).
\]
On t>=L/2 the integrand is at most 4 exp((1-d0)s) for s<0,
and at most exp(-c0*s) for s>=0. Both are integrable on their
respective half-lines. The explicit formula for p gives
P'(t)-p(t)=O(1/log t) and p'(t)=O(1/(t log t)).
Thus for every fixed R, uniformly for |s|<=R,
P(L+s)-P(L)-p(L)*s tends to zero. In the constant-profile case
this is exact. On each such compact interval the normalized
integrand differs by o(1) uniformly from
exp(-p(L)*s)/(1+exp(-s)). The latter has uniformly integrable
tails because alpha<=p(L)<=beta. Compact convergence followed by
these uniform tail bounds proves that the normalized integral
equals J(p(L))+o(1), without assuming convergence of p(L).
J is bounded above and bounded away from zero on [alpha,beta].
The O(1) complement is negligible since L-P(L)>=(1-beta)L.

For completeness, substitute x=e^s to obtain J(b)=integral_0^infinity
x^(-b)/(1+x) dx. A keyhole contour for z^(-b)/(1+z), with argument
in (0,2*pi), has vanishing small and large arcs for 0<b<1.
The two ray integrals give (1-exp(-2*pi*i*b))*J(b); the residue at
-1 gives 2*pi*i*exp(-pi*i*b). Division yields pi/sin(pi*b).
Alternatively the real-integral form of J suffices for all conclusions.

By 12.21.1, V=2 epsilon (1+K)/I for these rank-one coefficients.
Since K tends to infinity, substitution gives the displayed formula.
No regularization or L2 extension is involved.

### Checks of the printed arguments and dependencies

* Lines 10–49: q+epsilon>0, (a+epsilon)(q+epsilon)-|r|^2>0,
  and the choice of c makes A-a-epsilon mean zero. Fourier inversion
  on the flat torus gives a smooth real solution: the nonconstant
  Fourier coefficients are rapidly decreasing, and division by the
  nonzero Laplacian eigenvalues preserves this. The determinant is c,
  and the wedge square is 2c times the stated probability measure.
  The conformal metric gamma=Omega/(q+epsilon) is Gauduchon because
  its vertical coefficient is constant, while dd^c of the other
  coefficients repeats a base differential. In fact the equality
  in the variational quotient follows directly by pointwise
  arithmetic-geometric mean plus Stokes (12.2.3 proof, lines 68–79);
  neither global smooth equation existence nor general conformal
  Gauduchon existence is required for this explicit example.
* Lines 55–78: area in the disk is pi*d|zeta|^2; the logarithmic
  constant pi and finite-order substitution are correct, and
  the nonclosedness follows from dq wedge omega_2. Monotonicity of
  the root volume at epsilon=0 uses 12.2.2.
* Lines 83–144: both derivatives are bounded away from zero as
  required; smoothness at the pole follows from exponential decay
  against each polynomial derivative. The mixed derivatives cannot
  cancel dq wedge omega_2. The printed weaker logarithmic estimates
  and liminf/limsup are valid. No need to replace the theorem.
* Context: 12.2, file docs/sections/a-gauduchon-variational-volume--the-quotient-and-the-smooth-equation/index.html
  (blob 9ec67161d46b3ba20afa1b1c9a0c84f29322763e), lines 17–79:
  definition, monotonicity, determinant equality. 12.20,
  docs/sections/a-gauduchon-variational-volume--orders-of-degeneration-at-the-nef-boundary/index.html
  (blob a7c145c5d1ceb0f1326bfb155f75dc9d854f14a0), lines 10–101:
  logarithmic order definition and comparison; this prefactor is
  only for the fixed mu,h and specified local profile, not invariant
  under arbitrary perturbations. Its order conclusion remains the
  printed invariant. No effect on other theorem conclusions.
  The closed nef formula, general measure-change comparison and
  general perturbation continuity are not newly certified.
* Additional selected reading: 12.33, lines 76–95, Proposition
  12.33.3 (0414E2D53266), blob 67f63edb723e3cfd5ddb9723cc6061190e473feb,
  docs/sections/a-gauduchon-variational-volume--orders-of-degeneration-at-the-nef-boundary--cotangent-extensions-with-zero-ruling-component/index.html.
  Conditional on the printed transitions, fiber contraction gives
  simple connectivity of the proposed cover, and the zero section
  contains compact rational curves obstructing holomorphic
  separability. Algebraic weight decomposition and its earlier
  bundle-cohomology dependencies not certified in this run.

## Coverage and disposition

One whole direct conditional section (12.21); selected contextual
12.2, 12.20, 12.33. Previous legacy status not reconciled, no
historical first-visit assertion. Current TOC has 747 section IDs;
the pre-update matrix has 747 distinct section IDs with exact match.
One new conditional deduction; zero new confirmed errors or
demonstrated gaps; zero full upstream-chain certificates.
Proposed addition: the above optional relative asymptotic after
12.21.5 Step 2. No production changes, tests, builds, CI or
publication. All excluded approximation/regularization, dedicated
Bergman/L2/OT/multiscale/positivity-loss programmes remain
deferred-by-user, not certified.
