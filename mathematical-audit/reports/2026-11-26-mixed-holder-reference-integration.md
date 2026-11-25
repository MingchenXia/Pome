# Mixed Hölder reference integration and analytic singularity review — 2026-11-26

Production main: `b6933b772f41b45918f7e25ed1afbbb1fd892272`. Audit parent: `5e5a03a451127df4b43709257967d18e2a969a43`.
Scope: elementary bounded local Bedford–Taylor calculus, not the user-deferred Demailly approximation programme. All regularization/Bergman/weighted L2/OT/multiscale-atlas/positivity-loss work remains deferred-by-user.

## POME-HOLDER-MIXED-REFERENCE-CANCELLATION-001

Low / verified conditional deduction; **not a false printed theorem**. Proposed strengthening, not a source edit.

Anchor: `docs/sections/plurisubharmonic-functions-and-singularities--hermitian-capacity/index.html`, blob `77a9098e9bb922425d11c5b04d8927a3997ad44e`, Lemma 5.29.7 (source non-kahler-pluripotential-theory:43921D37, permanent D9AF18430F97), physical lines 112–159; equation 5.29.8 (source F87713B6, permanent 16B648CFC04A), lines 152–159. The proof uses the valid but coarse Hessian bound O(epsilon^-2) at line 125, hence exponent alpha/(alpha+2n). Corollary 5.29.9 (source 9E2FA0D5, permanent F701C1999BDC), lines 165–175, and the tail bound Lemma 5.29.10 (EF54C7C9A0A8), lines 184–212, are direct downstream applications.

### Statement

Let B' be compactly contained in a coordinate ball B in C^n. For i=1,...,n let p_i be PSH on B and uniformly bounded in C^{0,alpha_i}(B), with 0<alpha_i<=1. Let a,b be PSH on B with |a|,|b|<=M, M>=1. Define
```
s = sum_i (2/alpha_i - 1),
gamma = 1/(1+s),
L = integral_B |a-b| dV.
```
Then
```
integral_B' |a-b| dd^c p_1 wedge ... wedge dd^c p_n <= C_M L^gamma.
```
The constant is uniform with fixed nested balls, Hölder bounds and exponents. For a common alpha, gamma=alpha/(2n-(n-1)alpha), strictly better than alpha/(2n+alpha) for all n>=1. The proof below also gives a pre-optimization error with coefficient O((1+M)^2), useful for growing truncation bounds. No optimality assertion in dimensions n>1.

### Proof

Take a fixed smooth cutoff chi, supported strictly inside B, equal to 1 on B', 0<=chi<=1, and enough larger nested balls for convolution and mass estimates. Write f=|a-b|=2 max(a,b)-a-b.

Use a smooth nonnegative radial convolution kernel kappa of integral one supported in the unit ball. For small epsilon_i>0 put q_i=p_i*kappa_{epsilon_i} on the intermediate balls. These are smooth PSH with common sup bounds. The zeroth and second derivative estimates, using integral D^2 kappa=0, are
```
||q_i-p_i||_infty <= C epsilon_i^alpha_i,
D^2 q_i(x) = integral [p_i(x-y)-p_i(x)] D^2 kappa_{epsilon_i}(y) dy,
0 <= dd^c q_i <= C epsilon_i^(alpha_i-2) dd^c |z|^2.
```
The second identity is for each real second derivative and follows by differentiating convolution in the kernel variable; the integral of every second derivative of the kernel is zero. Changing variables y=epsilon_i w proves the displayed bound. This is an elementary local convolution estimate for bounded Hölder functions, not a singularity/positivity-loss approximation result.

Telescope the mixed products, replacing one p_i by q_i at a time. The i-th difference is dd^c(p_i-q_i) wedge T_i with T_i the mixed product of the remaining n-1 original or smoothed references; all are bounded PSH with uniform bounds. By the same local integration by parts as 5.29.7,
```
integral chi f dd^c(p_i-q_i) wedge T_i
 = integral (p_i-q_i) dd^c(chi f) wedge T_i.
```
For completeness the variation of the last signed measure is bounded by C(1+M)^2 uniformly in all convolution radii. For smooth factors the term chi dd^c f wedge T_i is bounded in variation by the sum of the positive Hessian terms for a,b,max(a,b) (use smooth decreasing convolution of these three functions separately). The term f dd^c chi wedge T_i is bounded by the trace mass of T_i times C M. For the first-derivative terms take a nonnegative cutoff eta=1 near supp chi, translate each bounded PSH h to 0<=h<=2M, and use closedness:
```
integral eta dh wedge d^c h wedge T_i
 = (1/2) integral h^2 dd^c eta wedge T_i
   - integral eta h dd^c h wedge T_i <= C M^2.
```
Local Chern–Levine–Nirenberg bounds control each trace and Hessian mass; Cauchy–Schwarz against T_i bounds the derivative cross terms. These estimates use only uniform bounds, not derivatives of the references. For nonsmooth factors use simultaneous locally bounded decreasing radial convolutions on intermediate balls, also of max(a,b), and take the displayed linear combination. The ordinary and weighted Bedford–Taylor continuity (5.27.1 and 5.27.2) identifies the weak limits of f times mixed products and of dd^c(chi f T_i); the uniform variation bound passes by weak lower semicontinuity. Since p_i-q_i is continuous on the support, its pairing passes to the limit. Alternatively, when applying the identity at fixed epsilon_i approximate p_i-q_i uniformly on that support and use the uniform variation bound. No differentiation of an uncontrolled product of distributions is needed.

The all-smoothed product is bounded by C prod_i epsilon_i^(alpha_i-2) dV. Summation gives the explicit estimate
```
integral chi f wedge_i dd^c p_i
 <= C(1+M)^2 sum_i epsilon_i^alpha_i
       + C L prod_i epsilon_i^(alpha_i-2).
```
Choose epsilon_i=t^(1/alpha_i) with t=L^(1/(1+s)) for sufficiently small positive L so all radii are admissible. The first term is O((1+M)^2 t) and the second is O(L t^-s)=O(t). Large L is covered by the uniform local mass bound and f<=2M; if L=0 send t to zero. This proves the assertion. No interchanging iterated uncontrolled limits occurs. The same constants apply to arbitrary indexed families with common bounds, and yield a modulus for nets with L tending to zero.

### Sharpness in dimension one

In the unit disk take p(z)=|z|^alpha, B' a fixed smaller centered disk, and for T>1
```
a_T = max(log|z|,-T)/(T+1),
b_T = max(log|z|,-T-1)/(T+1).
```
Both are PSH and between -1 and 0. Their difference is supported on |z|<exp(-T), bounded by 1/(T+1), and equal to 1/(T+1) on |z|<=exp(-T-1). Under the project convention dd^c=i/(2pi) partial barpartial, the radial mass of dd^c p on the disk of radius r is alpha r^alpha/2 (integrate the Euclidean Laplacian and divide by 4pi). Thus L<=pi exp(-2T)/(T+1), while the weighted integral is at least (alpha/2) exp(-alpha(T+1))/(T+1). For any exponent beta>alpha/2 the ratio to L^beta diverges as T tends to infinity. This proves optimality of the improved exponent gamma=alpha/2 in n=1 even for a fixed Hölder reference and uniformly bounded PSH tests. It is not a sharpness claim in higher dimensions.

### Downstream scope

For 5.29.9, use its fixed smooth local quadratic correction and common alpha: the same improved exponent follows by the printed finite cover. For 5.29.10, let a_0>0 be the fixed exponential-volume-tail exponent at line 203. With M=m+1 and L<=C exp(-a_0 m), the pre-optimization bound gives C(1+m)^2 exp(-a_0 gamma m), hence any rate c<a_0 gamma after enlarging C. Proposition 5.29.13 uses only existence of a positive rate; its qualitative statement is unchanged. These deductions are conditional on the existing bounded-product, CLN and weighted-continuity inputs (5.27.1–2; selected direct read of 5.27 lines 7–60, blob ddb2ac8d9de27a22152872e07e5e787d138a790e). No independent complete certification of these or their upstream dependencies is made.

## Direct coverage and separate checks

* §5.1, `docs/sections/complex-differential-forms-and-positive-currents/index.html`, blob fec3c3e220607b33de74642b64e444ac8f21b41e, mathematical lines 7–16: entire introduction, no theorem certification. Differentiation, normalization of Poincaré–Lelong, and countability qualifier for compactness agree with stated context.
* §5.7, `docs/sections/plurisubharmonic-functions/index.html`, blob bc8a7baa7d35967c7d56a357c4d9022ff36a51d9, lines 7–30: entire introduction; distinction of pointwise and distributional representatives, qualifications for Kiselman, and monotone subnet convention checked as exposition. Regularization, OT, etc. mentioned as dependencies only, not pursued.
* §5.33, `docs/sections/plurisubharmonic-functions-and-singularities--singularity-type-and-multiplier-ideals/index.html`, blob c80624ee98ec8a3500112df6411c98bf4520fa86, lines 7–65: whole direct mathematical read. Proposition 5.33.1 (B667D338 / EFC5ED339FC3) uses compactness for global bounded smooth differences. Proposition 5.33.2 (C73A1DEC / 32843D040902) has the correct ideal-inclusion direction and exponential constant. Example 5.33.3 (07A23101 / 36A8480CE7DF) gives m>lambda-1, including the divergent integer endpoint; all positive real weights distinguish logarithmic coefficients. No assertion that arbitrary ideal types determine ordinary singularity types.
* §5.34, `docs/sections/plurisubharmonic-functions-and-singularities--analytic-types-and-restriction/index.html`, blob cff8b3156b07aff2f3d881d83d04608e87b7f2c8, lines 7–132: whole direct read, conditional on cited inputs. Proposition 5.34.1 (A55E69E3 / AAD8908A0CF9) uses rational commensurability and product/sum ideals, not arbitrary real scalars or preservation of smooth remainders. For restriction, the image ideal must not vanish identically on the connected submanifold. The zero-Lelong pole at lines 57–63 is PSH by increasing convex composition and has identically infinite negative restriction. Corollary 5.34.3 (5103AFE8 / C6F4FBF73B9E) correctly uses bidimension n-j and coefficient trace domination; the previously logged internal-dependency substitution POME-HAUSDORFF-LELONG-INTERNAL-001 and sharpness POME-HAUSDORFF-TRACE-EXPONENT-SHARP-001 are not new findings. Example 5.34.4 (22A3233E / 697E97CED780): sum lambda_j=1/2; affine-line trace mass (r^2-d^2)_+ has the correct normalization; dominated convergence uses summable coefficients even at accumulation points; the strict level set excludes its limit. Siu analyticity is an existing dependency, not re-proved.
* §5.29 selected physical lines 7–285 only (not whole section; no claims on lines 289 onward). Gluing test agrees with constant near outer boundary; local-to-global capacity comparison and inverse-power direction checked. The projective extremal measure support in lines 227–233 remains an input. §5.27 selected dependency lines 7–60 as above.

New: one verified conditional deduction, zero confirmed printed errors, zero newly demonstrated proof gaps; two whole substantive direct sections, two whole introductory readings, two selected sections. Historical first-ever visits not asserted. No complete transitive proof certificates. Previous matrix records are preserved; no full current ToC reconciliation this run. No builds, tests, CI, source/registry/permanent-tag or published-site changes.
