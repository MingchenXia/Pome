# A self-contained local-to-global convexity bridge in the planar distance criterion

**Checkpoint:** 2026-11-20. **Finding ID:** `POME-PLANAR-DISTANCE-LOCAL-CONVEX-GEODESIC-001`. **Status:** **verified repair** (audit-only self-contained replacement for an unlinked classical input, together with a verified conditional deduction). **Severity:** low. **No original Pome theorem is refuted.**

**Reviewed production main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. **Integrated reading edition:** `docs/sections/planar-boundary-distance-and-convexity/index.html`; blob `25fd0fd57d3e51f9224a25341ace77584b2a1a2a`. **Complete direct mathematical reading:** §3.9, physical HTML lines **7–107**. Section permanent tag **B2AAD3B5B63F**. Relevant source/permanent labels: Proposition 3.9.1 `klimek-pluripotential-theory:79D31B13 / 964B6728E795` (lines 7–33); Proposition 3.9.2 `klimek-pluripotential-theory:219D9DEC / 59D258340230` (lines 37–87, especially **44–78**); Proposition 3.9.3 `klimek-pluripotential-theory:366D2F88 / BBEB233BF8A4` (lines 91–107).

## Exact input and classification

Proposition 3.9.2 starts with a nonempty proper **closed** set F in the **real plane** and a **connected open** neighborhood G of all of F. It assumes that the Euclidean distance d_F is subharmonic on G. Its integrated proof first proves the semiconcavity/distributional Hessian upper bound on G\F, combines subharmonicity and the eikonal identity to obtain a nonnegative Hessian **in dimension two**, proves local convexity of F, and constructs a continuous nearest-point retraction P:G→F. This proves connectedness of F. The final line at physical **78** invokes “the closed connected local-convexity proposition” without an accompanying argument or internal locator in that paragraph. The classical local-to-global lemma is valid; below is a complete standalone proof, so this is **not a false statement** or an independently established project-wide missing proof. The optional replacement eliminates the need for that unlinked input at this use.

The previous `POME-DIST-HIGHERDIM-CIRCLE-TUBE-SUBHARMONIC-001` (2026-11-13) concerns a **false hypothetical extension to dimensions >=3**; it is a distinct result and is **not counted again** here.

## Lemma: a closed connected locally convex subset is convex

Let F be a nonempty, closed, connected subset of Euclidean space R^N. Suppose each p in F has r_p>0 such that F∩B(p,r_p) is convex. Then F is convex.

**Step 1: polygonal connectivity.** Fix a in F. Let A consist of points of F that can be connected to a by a finite polygonal path entirely in F. For p in A, the relatively open neighborhood F∩B(p,r_p) lies in A: each q in it is reached by adjoining the segment [p,q] to a path to p. The same argument shows the complement F\A is relatively open: if p outside A, no point q in F∩B(p,r_p) lies in A, for otherwise appending [q,p] would connect p to a. Hence A is relatively clopen. Since F is connected and a∈A, A=F. In particular, any two points admit a finite-length curve in F.

**Step 2: existence of a shortest curve.** Fix a,b in F and a polygonal competitor of finite length L_0. Let L_* be the infimum of lengths of rectifiable paths in F joining a to b. Choose paths of length at most L_0+1 converging in length to L_*. Parametrize each proportionally to arclength on [0,1]; they are uniformly (L_0+1)-Lipschitz and their images lie in the fixed closed ball B(a,L_0+1). Arzelà–Ascoli gives a uniformly convergent subsequence with limit gamma:[0,1]→F (closedness is essential). For every partition of [0,1], its chord sum converges to the corresponding sum for gamma, hence length(gamma) <= liminf length(gamma_j)=L_* by taking a supremum over partitions. Since gamma is a competitor, equality holds.

**Step 3: every shortest curve is straight.** Fix t_0 in [0,1]. There is a convex local ball B(gamma(t_0),r)∩F. By continuity choose a parameter interval I about t_0 whose entire image lies in that ball. For any s<t in I, the chord between gamma(s),gamma(t) lies in F∩B by convexity, and replacing the subpath gamma|[s,t] by that chord cannot increase the length. Global minimality forces
[
operatorname{length}(gamma|_{[s,t]})=|gamma(t)-gamma(s)|.
]
Equality in the triangle inequality for every intermediate point implies the subpath is a straight segment traversed without backtracking. Since gamma was parametrized at constant speed, gamma is affine in the parameter on I. These overlapping local affine descriptions imply gamma is globally affine on [0,1]. Thus gamma([0,1])=[a,b]⊂F. The endpoints were arbitrary, so F is convex. QED.

This proof uses only elementary topology of connected sets, the finite polygonal path construction, compactness of bounded equi-Lipschitz curves, and the equality case of the triangle inequality. It does **not** use sequential compactness of an infinite-dimensional current space, Hessian regularization, Bergman kernels, L² methods, or the user-deferred programme.

## Further exact consequence: firm nearest-point nonexpansiveness

Under Proposition 3.9.2's hypotheses, the preceding lemma completes the proof that F is nonempty closed convex. Hence the metric projection P_F:R²→F is uniquely defined **globally**, not merely on G. For p=P_F(x) and any z∈F, the minimality of p along p+t(z-p), 0≤t≤1, gives
[
langle x-p,z-panglele 0. 	ag{1}
]
For x,y with p=P_F(x), q=P_F(y), choose z=q in (1) and then z=p for y. Adding yields the *firm nonexpansive* inequality
[
oxed{ |P_F(x)-P_F(y)|^2
le langle P_F(x)-P_F(y),x-yangle . } 	ag{2}
]
In particular |P_F(x)-P_F(y)|≤|x-y|. Moreover
[
|(I-P_F)(x)-(I-P_F)(y)|^2
=|x-y|^2+|p-q|^2-2langle x-y,p-qangle
le |x-y|^2. 	ag{3}
]
For D(x)=d_F(x)^2/2, comparison with the same minimizing point p at x+h gives
[
D(x+h)le D(x)+langle x-p,hangle+	frac12|h|^2.
]
Comparison with P_F(x+h) in the other direction, together with (2), gives the matching lower estimate up to O(|h|²). Thus D is differentiable with gradient x-P_F(x), and (3) makes the gradient globally 1-Lipschitz:
[
oxed{ Din C^{1,1}(mathbb R^2),quad

abla D(x)=x-P_F(x),quad
operatorname{Lip}(
abla D)le 1. } 	ag{4}
]
This is a **verified conditional deduction** and not a claim that the printed proposition included the stronger projection assertion. If F is a point, equality in the gradient Lipschitz bound holds, so the universal constant 1 is sharp.

## Direct review of the other arguments

- **§3.9.1 (lines 13–33):** The minimal-segment polygonal path yields a triangle with a missing point. The rightmost-highest missing point provides a local supporting half-plane with strict missing-point inequality on a positive-area half-ball. The mean-value contradiction is correctly oriented: d exceeds an affine harmonic function on a positive-measure part of the ball, whereas -d subharmonic would require the opposite supermean inequality. The converse uses the concavity of boundary distance for convex D.
- **§3.9.2 (lines 43–70):** On G\F the distance is semiconcave, while subharmonicity bounds the other eigenvalues from below. Thus d is C^{1,1} there; differentiating |∇d|²=1 makes one Hessian eigenvalue zero. In **R² only**, Δd≥0 implies the remaining eigenvalue is nonnegative. Local convexity of the zero set then follows by the chord argument; nearest projection is continuous up to F and makes F connected. The only replacement supplied here is Step 1–3 above, after that connectedness step.
- **§3.9.3 (lines 97–107):** G=U∪int(F) is connected because each component of int(F) meets the connected boundary collar U; the subharmonicity is local and the distance vanishes on int(F). The two separated closed disks illustrate why a **disconnected** boundary neighborhood does not suffice. This use of §3.9.2 remains intact.

**Affected dependents:** direct use in Proposition 3.9.2 and Proposition 3.9.3; potential later uses of global metric projections if added. **Proposed correction (not applied):** insert the three-step local-convexity proof immediately before the invocation at §3.9.2 line 78; optionally append (2)–(4) as a remark with proper attribution. Keep all original provenance/source numbers/permanent tags, and retain the existing historical attribution. No source, registry, canonicalization or published document was edited.

**Coverage:** complete direct reading of all **three** current §3.9 propositions and their complete printed proofs (lines 7–107); **+1 whole-section direct reading**, **+0 completed transitive dependency chains**, **+0 first-ever section visits asserted** (the section already had partial audits). No numerical or software checks, compilation, rendering, CI or site publication performed. All user-excluded regularization/Bergman/L²/OT/multiscale/positivity-loss proof programmes remain **deferred-by-user**, not resolved or certified.
