# Radial full-mass solutions: unbounded potentials at finite metric distance

Date: 2026-11-25. Reviewed main: b6933b772f41b45918f7e25ed1afbbb1fd892272.
Starting audit head: 29ba305c0f7f13ba06ec91e70403a7351638611a.

**POME-RADIAL-SPARSE-MASS-UNBOUNDED-FINITE-DISTANCE-001** — low / verified conditional deduction, not a printed theorem error. The two integral criteria of Theorem 10.22.1 are independent. In particular, the reverse separation to the bounded-but-complete example in 10.22.7(3) occurs for smooth strictly positive punctured radial densities of finite total mass: an unbounded full-mass potential with zero Lelong number and finite distance to the puncture. Its metric completion adds a single point there. The printed theorem remains correct.

## Immutable integrated anchors

- docs/sections/bott-chern-classes-and-singular-loci--radial-densities-and-metric-completeness/index.html, blob 239bbc1a79923b3728c535de109261f852efe059, physical lines 7–113, source non-kahler-pluripotential-theory. Theorem 10.22.1 source 04E2602C / permanent A86593744D2D, lines 11–54; mass and slope F205E7AE4ECC (17–20), boundedness B8FF1DABE923 (22–25), distance 585DD6478F46 (27–30), blowup C19D1AD0E901 (33–37). Theorem 10.22.7 source 0ABAA07A / permanent FF884313C070, lines 60–113; critical iterated logarithm 5C6F9700C172 (85–90).
- docs/sections/bott-chern-classes-and-singular-loci--density-zeros-and-metric-degeneration/index.html, blob 77de3087c6e9fb85dd397a633ee45140051abf1c, mathematical lines 7–120; Example 10.21.11 source BE87FD9F / permanent 554ACF84A13B, lines 113–120: positive-slope interpolation and radial completion.

## Reduction and construction

Use the convention and normalized radial family of 10.22.1. Put \(s=|y|^2\), \(t=\log(1/s)\), and \(m=sU'(s)\). For a smooth strictly positive integrable function \(f\) on \(t\ge 1\), let
\[
M(t)=\int_t^\infty f(v)\,dv,\quad m(s)=M(\log(1/s)),\quad
D(s)=s^{-n}M(t)^{n-1}f(t).
\]
Then \(m'(s)=f(t)/s>0\). The exact density equation \(s^{n-1}D=m^{n-1}m'\) holds, \(m(0+)=0\), and the local mass up to radius squared \(s\) equals \(m(s)^n\) by integration. The radial criteria of the theorem now become
\[
U(e^{-1})-U(e^{-T})=\int_1^T M(t)\,dt,\qquad
\int_0^{e^{-1}}\frac{\sqrt{m'(s)}}{2\sqrt{s}}ds
=\frac12\int_1^\infty\sqrt{f(t)}\,dt.
\]
By Tonelli, \(\int_1^\infty M(t)dt=\int_1^\infty(v-1)f(v)dv\) (allowing infinity).

Fix a nonnegative smooth bump \(\chi\) supported in \((-1/4,1/4)\) of integral one. For \(t\ge1\), set
\[
f(t)=e^{-t}+\sum_{j=1}^\infty 2^{-j}\chi(t-4^j).
\]
The sum is locally finite, the supports disjoint, \(f\) is smooth and strictly positive, and its integral is finite. Its first moment diverges since the j-th bump contributes at least \(2^{-j}(4^j-5/4)\). On the other hand, subadditivity of the square root gives
\[
\int_1^\infty\sqrt f\,dt
\le \int_1^\infty e^{-t/2}dt+
\left(\int_{\mathbb R}\sqrt{\chi}\,dt\right)\sum_{j\ge1}2^{-j/2}<\infty.
\]
Thus \(U\to-\infty\) at the puncture while the radial length is finite. Since \(M(t)\to0\), averaging \(\int_1^T M(t)dt\) over \([1,T]\) shows \(U(e^{-T})/T\to0\). The residual Lelong number is zero.

To globalize, multiply the inner slope by a small positive constant (equivalently scale \(f\)). For any fixed \(\lambda>0\), arrange that its value at an inner matching radius is strictly less than the outer slope \(\lambda s/(1+s)\) at a larger matching radius. Join the two positive derivative germs on sufficiently narrow collars using a smooth strictly positive derivative on the intermediate interval, with its integral equal to the positive difference of endpoint values. This is possible: the collar integrals can be made smaller than the difference, a sufficiently small positive interpolating baseline leaves a positive deficit, and a nonnegative interior bump fills that deficit. Integration matches both slope values and all derivative germs. Set \(m=\lambda s/(1+s)\) outside the outer matching radius. Define \(D=(m/s)^{n-1}m'\) globally on \(s>0\). It is positive smooth, has the required outer formula, and \(n\int_0^\infty s^{n-1}D(s)ds=\lambda^n\) because \(m(0+)=0\) and \(m(\infty)=\lambda\). Integrate \(U'=m/s\), matching the Fubini–Study potential outside. The local extension and non-pluripolar mass argument of 10.22.1 gives the global full-mass solution, with smooth metric off the origin, unbounded potential and zero Lelong number. No regularization or approximation theorem is used in the new calculation.

## Metric completion

On a sphere of Euclidean radius \(R=\sqrt{s}\), the induced metric, compared to the unit sphere's standard metric by radial dilation, has its eigenvalues bounded above by a universal constant times \(\max(m(s),s m'(s))=\max(M(t),f(t))\) (the Hopf direction is controlled by the radial complex eigenvalue, and the remaining directions by the tangential eigenvalue). Choose \(t_j=4^j+1\), where \(f(t_j)=e^{-t_j}\) and \(M(t_j)\to0\). The intrinsic diameters of these spheres tend to zero. Any two points sufficiently near the puncture can be joined by radial segments to one common such sphere, and a path along that sphere. Each radial segment's length is bounded by a fixed multiple of the tail of \(\int\sqrt{f}\) from the smaller logarithmic radius; hence the diameters in the ambient metric of the punctured neighborhoods tend to zero. The radial distance to the puncture is finite, and the metric is smooth positive away from it. No other completion points occur (compactness away from the puncture, and positivity of the metric on annuli separating the puncture from any fixed regular point). Thus precisely one point is added. The blowup is isometric off its exceptional divisor and the same completion conclusion holds there, conditionally on the blowup identification of 10.22.1.

For the opposite separation, 10.22.7(3) already supplies bounded potentials with infinite distance for \(n<d\le2n\). This is not counted as a new result. The present construction shows that neither boundedness nor finite metric distance implies the other in the full radial family. It does not contradict the printed power and logarithm asymptotics, which concern restricted density classes.

## Direct review and dependencies

10.21: checked the ramified-map Jacobian and radial length (10.21.1), Hopf pullback differentiation and divisorial barrier formula (10.21.3), determinant/trace lower bound and Schur complement path construction (10.21.6), fiberwise constancy plus quadratic vanishing and Hadamard estimate (10.21.9), Pogorelov Hessian determinant and gluing estimates (10.21.10), and power-type exceptional density and normal-distance calculations (10.21.11). The latter's exponent is \(\ell=n\gamma-1\); its insufficiency example \(\ell=n\) has \(\gamma=1+1/n\), so the residual Hessian is not smooth at the divisor. No new confirmed theorem error from this direct read.
10.22: verified the slope ODE, positivity, gluing and mass normalization, the two integral criteria, and the three stated asymptotic regimes by direct integral comparison (not differentiating an asymptotic error). The critical \(d\)-thresholds \(n\) and \(2n\) are distinct and correct. The distance integral is a finiteness criterion; no absolute Riemannian normalization constant is asserted here.

Upstream inputs not transitively certified: the psh removable point lemma 5.24.7 (F3A890BB2575), non-pluripolar locality/no mass on pluripolar sets, full-mass uniqueness in the closed theory (the printed reference to history §25.10 is not by itself a proof), the blowup structure 15.23.2 (E42F32DA29D8), and extended operator agreement 13.14.3 (99C7ACBB2589). The smooth gluing in 10.21.10 uses the elementary convex regularized maximum, not the excluded Demailly programme. No attempt to certify that programme or its prerequisites was made.

Proposed addition: after Theorem 10.22.7, add the sparse-density example to emphasize the independence of the two general criteria; any later boundedness inference solely from finite radial distance would require extra density hypotheses. No existing downstream theorem is refuted; exhaustive reverse-reference search not performed.

Coverage: two entire current mathematical sections directly read, previous historical first visits unreconciled, one new conditional deduction, zero newly confirmed printed errors, zero new demonstrated proof gaps, zero complete transitive chains. Actual main ToC and audit matrix each contained the same 747 section numbers, with no duplicates or omissions, before this update. All excluded programmes remain deferred-by-user, not resolved or certified. No software tests, builds, CI, publication, or production edits.
