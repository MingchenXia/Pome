# Local semiconvexity of extended volume and its exact boundary differential

Date: 2026-11-28. Main reviewed: b6933b772f41b45918f7e25ed1afbbb1fd892272. Audit branch at start: b37b64cebbc17413ae1ab82e2836387e5d55e0ec.

## Scope and anchors

Whole direct conditional reading of the integrated mathematical text in
[§10.99](https://github.com/MingchenXia/Pome/blob/b6933b772f41b45918f7e25ed1afbbb1fd892272/docs/sections/variations-of-the-volume/index.html),
physical lines 8–208, blob 0b744b6432968b1320d63f5ebe67246108bb3ecf.
The matrix previously had only LEGACY-UNRECONCILED for this section; no historical first-visit claim.

- 10.99.1 (B05D26A510EC / source 85AF2FC8), lines 8–21: simultaneous approximation and mixed nef monotonicity, conditional on the stated cofinality. The mixed bound follows by pairing the positive difference current with smooth Kähler perturbations of the remaining nef factors.
- Lines 26–49 (source section 2E8D1C0B, permanent F956FFB5439C): zero extension, boundary product and numerical premises. These are class products, not weak-current continuity.
- 10.99.4–5, lines 53–90: cone comparison uses both signed increments, then a finite Kähler basis; degree zero is constant. In particular the Lipschitz bound for P is local to the big cone.
- 10.99.6 (64857FC6958D / source F8F5EBF6), lines 95–130: uniform lower variation. The coefficient sum 2^(n-1)-1, order A_j <= B_j, G_j <= 2 B_j, and projection B_j^n=H^n all give the stated bound.
- 10.99.8 (BF3A71BBF47B / source 0FF4E50C), lines 135–152: the two-sided quadratic remainder follows by exchanging x and y and using local Lipschitz continuity of P.
- 10.99.10, lines 157–184: continuity at the boundary precedes segment integration; the segment's big part is an interval, and the gradient is bounded by its Kähler coordinates.
- 10.99.11 (A4F489BD4673 / source E897FBC3), lines 189–208: Euler differentiation in the big cone and the stated decreasing Kähler boundary-product limit.

All these arguments were checked conditional on the numerical premises in lines 26–49, including 13.31.4, 13.32.3–4/6 and 10.98.2, modification invariance and class-mass monotonicity. The approximation-dependent input 13.32.3 is recorded, not reopened (deferred-by-user insofar as it requires the excluded programme). No proof of those upstream results is certified here.

## POME-VOLUME-BOUNDARY-SEMICONVEX-DIFFERENTIAL-001

Severity low; status verified conditional deduction, not a printed error. Retain exactly the hypotheses of §10.99 (nonempty connected compact Kähler X, n>=1). Let V be the real (1,1) class space with a Euclidean norm, E the pseudoeffective cone, B its interior, f=vol extended by zero, P the positive (n-1)-product, with the printed empty-product convention n=1. Under the numerical premises above:

1. The zero extension f is locally semiconvex on all of V.
2. At every a on the boundary of E, with L_a(h)=n P(a) dot h,

       f(a+h) = max(0,L_a(h)) + o(||h||).

   In particular f is Frechet differentiable there iff P(a)=0, and then its derivative is zero. This is a uniform first-order expansion, not merely a formula for each fixed Kähler direction.
3. If P(a) != 0, the closed tangent cone of E at a is precisely {h:L_a(h)>=0}. The one-sided directional derivatives are the positive part of L_a. The ordinary convex subdifferential of f+C||.||^2 on a sufficiently small ball at a is 2Ca+[0,L_a], with covectors identified using the Euclidean pairing.

### Proof

**Uniform lower support.** Inspect lines 105–129 of the printed proof of 10.99.6. The sole use of U in choosing H is boundedness: H-x is Kähler for all x in U and H+/-v Kähler for all unit v. For any bounded set of big classes the same H works, even when its closure meets the boundary. For each individual x the approximation is taken separately; no uniform approximation rate is needed because the intersection bound and remainder constant C=2n(2^(n-1)-1)H^n are independent of x and of the approximating models. Therefore
       
       f(x+h) >= f(x)+nP(x) dot h-C||h||^2

for every big x in the bounded set and ||h||<=1. At a boundary point a choose x=a+epsilon omega in a fixed bounded set and pass to the limit using the printed perturbation limits for f and P and continuity of the zero extension (10.99.10). This gives the identical inequality at a. At any nonbig point x the inequality with the zero covector is immediate from f(x)=0 and f>=0. Thus on any bounded convex ball of diameter at most 1, f+C||x||^2 has an affine global lower support at each x: expand the square and use the appropriate covector. It equals the supremum of these affine functions, hence is convex. This proves local semiconvexity. At boundary points both the zero covector and nP(a) are valid lower supports for f with the quadratic error.

**Radial limit.** Suppose a is on the boundary and b=a+t0 h is big for some t0>0. For 0<t<t0 set s=t/t0. Choose a Kähler omega and c>0 with b-c omega big. Pseudoeffective monotonicity of the Kähler-coordinate tests F_kappa in line 42 gives

       F_kappa((1-s)a+s c omega) <= F_kappa(a+t h).

The class on the left is big and equals (1-s)(a+(s c/(1-s))omega). Its coordinate tends to F_kappa(a) by the printed boundary perturbation limit and degree n-1 homogeneity. Also choose C0>0 with C0 omega-h Kähler. Then

       F_kappa(a+t h) <= F_kappa(a+t C0 omega),

whose limit is again F_kappa(a). The squeeze applies to a finite Kähler basis, so P(a+t h) -> P(a) along this fixed inward ray. This does not assert arbitrary boundary continuity of P.

For t>0 small, a+t h is big by convexity; the derivative of f there in the ray direction is nP(a+t h) dot h (10.99.8). Integrate on [delta,t] and let delta decrease to zero, using continuity at a and boundedness of the integrand near zero. The quotient f(a+t h)/t tends to L_a(h), necessarily nonnegative. If there is no big point along the positive ray, f is identically zero there, and the boundary lower support implies L_a(h)<=0 on dividing by t and taking t down to zero. This dichotomy yields the directional formula in every h.

**Uniformity.** By 10.99.10, f is Lipschitz in a neighborhood of a. The maps h -> f(a+t h)/t on the unit sphere are equi-Lipschitz for sufficiently small t. Their pointwise limit max(0,L_a(h)) is continuous. A finite net on the compact unit sphere proves uniform convergence (bound at a nearby net point and add the two Lipschitz errors). Substituting t=||h|| proves the claimed uniform expansion. A positive part of a nonzero linear functional is not linear, while it is identically zero if the functional vanishes; perfect pairing gives the differentiability criterion.

**Tangent cone and subdifferential.** For any b in B, the boundary perturbation monotonicity with positive Kähler tests shows L_a is nonnegative on E: for e in E, f(a+t e)>=0 alone is not enough, but for a+epsilon omega big, monotonicity of f in direction e implies nP(a+epsilon omega) dot e>=0 by differentiating at zero. Pass to the boundary. Orthogonality (10.99.11) gives L_a(a)=0. If L_a is nonzero, its value on any b in B is strictly positive (a linear functional nonnegative on a full-dimensional cone cannot vanish at an interior point unless zero). Hence every direction from a into E has nonnegative L_a. Conversely if L_a(h)>0, the boundary lower support forces f(a+t h)>0 for all sufficiently small t>0, hence a+t h is big. Taking closures gives the precise tangent halfspace.

Finally, for the convex function g=f+C||.||^2, its one-sided directional derivative at a is 2Ca dot h+max(0,L_a(h)). A covector p is a convex subgradient exactly when p dot h is bounded above by that derivative in every direction: necessity follows by taking the directional limit of the supporting inequality; sufficiency follows from monotonicity of secant slopes on each segment. The set of such covectors is exactly 2Ca+[0,L_a] by finite-dimensional separation (or test both signs in ker L_a, then a direction with L_a=1 and its negative). This proves the last assertion, also if L_a=0.

### Sharpness and limitations

Already on a compact curve, f(degree)=max(0,degree) by the printed n=1 convention and derivative formula. Thus the non-differentiable boundary case is genuine, and one cannot generally extend the printed interior C^1 assertion across the boundary. No rate for the little-o remainder, no global boundary continuity of P, and no uniform C^{1,1} extension is asserted.

Suggested optional addition after 10.99.11: state the local semiconvexity and the boundary expansion with the above proof. No replacement of the correct printed theorem is required. Relevant downstream uses are any application of 10.99.8 or 10.99.11 at boundary classes; no actual downstream error is asserted. The approximation and Morse inputs remain conditional.

## Accounting

One whole direct conditional section, zero newly confirmed theorem errors, zero demonstrated proof gaps, zero complete upstream certifications. Additional §10.108 reconnaissance not counted as proof coverage (its L2 programme not reviewed); §11.49 not reviewed mathematically in this increment. Current chapter 10 TOC has 109 distinct sections, matching the current matrix; all 747 matrix section identifiers are unique. Other chapters not freshly re-enumerated. No software tests, builds, CI, production edits or publication. Existing user-deferred records unchanged.
