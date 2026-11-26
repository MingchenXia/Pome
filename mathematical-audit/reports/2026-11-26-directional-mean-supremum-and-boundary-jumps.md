# Directional mean–supremum control and exact boundary-measure jumps

Date: 2026-11-26. Reviewed main: `b6933b772f41b45918f7e25ed1afbbb1fd892272`. Audit-only proposals.

## POME-DIRECTIONAL-MEAN-SUP-BOUNDED-DEFECT-001
Low / verified conditional deduction, not an error in the printed theorem.

Anchor: `docs/sections/lelong-densities-generalized-masses-and-multiplicity--directional-boundary-measures-and-growth/index.html`, blob `f4db1608fec003cc9e6055d2bb9e1db447254477`, lines 7–125; in particular Lemma 6.37.2 (source FCF277F6, permanent 8A0C22EC23BC), (6.37.4) lines 61–64 and Theorem 6.37.5 (source 28BEBFE4, permanent E3EFBBDA7787), lines 88–125.

With exactly the hypotheses and notation of 6.37.5, fix h>0 and let
`c=prod_j (1-exp(-h/(2 lambda_j)))/(1+exp(-h/(2 lambda_j)))`, so 0<c<1. Write m(r)=m_V(r), H(r)=H_V(r), g(r)=H(r)-m(r)>=0 and L=nu(dd^c V,a,lambda)/Lambda. Then g is bounded on every sufficiently negative half-line, and

`0 <= limsup_{r->-infty} g(r) <= h L/c.`

In particular, if the directional number is zero then g(r)->0, even if V has a pole at a. The ordinary directional growth bound H(r)<=L r+O(1) also follows. This is a quantitative strengthening for arbitrary PSH germs, not the earlier special binomial computation POME-DIRECTIONAL-TORUS-BINOMIAL-GAP-001.

Proof: choose r0 so the closed polydiscs at all r<=r0 lie in the PSH domain and m is finite convex nondecreasing on a neighborhood of (-infty,r0]. Apply (6.37.4) to V-H(r+h) on the outer polydisc; it is nonpositive there. The inner/outer radius ratios are fixed exp(-h/(2 lambda_j)). Taking the supremum on the inner polydisc gives H(r)<=c m(r+h)+(1-c)H(r+h). Consequently

`g(r) <= m(r+h)-m(r)+(1-c)g(r+h)` for r+h<=r0.

By convexity the finite secant slopes on this half-line are bounded above by M, e.g. a right secant slope at r0 to a slightly larger admissible level. Thus m(r+h)-m(r)<=h M. For r<=r0 let k=floor((r0-r)/h). Iteration gives g(r)<=h M(1-(1-c)^k)/c+(1-c)^k g(r+kh). The latter argument lies in (r0-h,r0], where g is at most H(r0)-m(r0-h), finite by the printed theorem. This proves boundedness. The fixed-length secant slopes of a finite convex function tend to its limiting slope at -infinity, here L by 6.37.5 (or 6.36.7). Taking limsup in the recurrence, using its finite left-tail bound, yields G<=h L+(1-c)G, as claimed. Finally convexity gives m(r)<=m(r0)+L(r-r0) because every finite secant slope is at least L. Add the bounded g. No interchange of unrelated limits and no regularization step is used. No claim that h/c is the best constant.

Proposed addition: append this short proof after 6.37.5; retain its statements, attribution and tags. The identification with the generalized mass is conditional on 6.36.7, 6.37.1 and the existing Poisson estimate; their upstream chains are not certified. No existing dependent is asserted false.

## POME-JENSEN-BOUNDARY-RIGHT-JUMP-001
Low / verified conditional deduction. Anchor: `docs/sections/lelong-densities-generalized-masses-and-multiplicity--boundary-measures-and-the-weighted-jensen-formula/index.html`, blob `a341258d025614e3f8d6852f170f519df7362554`, Proposition 6.36.1 (source B538716D, permanent E5EFE4D4F285), lines 11–34.

Under the printed extended-continuous weight and compact-low-sublevel hypotheses, for every r<R the exact weak right limit is
`mu_{r+}=mu_r+1_{phi=r} sigma`.
Thus the boundary-measure map is weakly continuous at r if and only if sigma gives the level zero mass. Its right jump is a positive measure, with total jump sigma({phi=r}); there are at most countably many nonzero jumps on any compact interval below R (indeed on the entire range by countable exhaustion). No atom at a finite level is silently dropped.

Proof: if s decreases to r, max(phi,s) tends locally uniformly to max(phi,r), with bounded difference <=s-r. Bounded-product uniform continuity yields A_s -> A_r. On compact tests, the indicators 1_{phi>=s} increase to 1_{phi>r}, and sigma is locally finite. Subtract the limiting restricted measure from A_r and use (6.36.2). The same proof applies to arbitrary directed monotone nets: for the restriction, the convergence of the real thresholds is bracketed by r+1/k, and local finite-measure continuity along that sequence gives the desired test convergence, including signed continuous tests by positive/negative parts. The stated left limit was already proved. If the level mass is positive, a compactly supported nonnegative test equal to one on the compact level detects the nonzero jump. For the countability assertion use disjoint level sets inside compact low sublevels with finite sigma mass. Example n=1, phi=max(log|z|^2,0) on C, R>0: sigma is angular probability on |z|=1, mu_0=0 while the weak right limit is that probability. Thus the existing one-sided qualifier is essential. The example is locally bounded and needs no excluded approximation. Proposed addition after 6.36.1; retain the finite Jensen differences 6.36.5 and their open/closed endpoints.

## Actual coverage and dependency boundaries

- 6.36: direct mathematical text lines 7–145. Checked the cutoff support, positivity sign and mass normalization in 6.36.1, Tonelli and inner truncation identity in 6.36.3, monotonicity-based unbounded pole limit (lines 73–89), weighted angular comparison and real coefficient passage, and off-origin vanishing by a local holomorphic change of variables in 6.36.9. The finite-annulus identity avoids cancellation of infinite integrals. Existing 7.31.1/2 approximation and product premises are recorded only, not reopened or independently certified.
- 6.37: direct whole mathematical text lines 7–125. Checked the missing-coordinate rank argument, Haar probability normalization, iterated Poisson inequality by bounded truncations, negative-sign kernel estimate and negative-denominator slope squeeze. Earlier equation alias defects (6.36 line 148, 6.37 line 128) and the binomial result are retained, not counted as new.
- 6.34: contextual line 7 confirms extended continuity is part of the weight definition, so all finite truncations are continuous; selected statements only. 6.41: contextual inspection of the incidence construction and finite-radius average, not a whole review or new finding.
- The actual main docs/index.html numbered ToC and the starting SECTION_MATRIX contain exactly 747 distinct section identifiers each, with empty set differences. Both 6.36 and 6.37 had legacy-unreconciled rows; historic LATEST records earlier selected visits, so no historical first-visit claim.
- Two conditional mathematical deductions, zero new confirmed theorem errors, zero demonstrated new gaps, zero complete upstream proof-chain certificates. All designated Demailly approximation/regularization, Bergman, L2, Ohsawa–Takegoshi, multiscale and positivity-loss programmes remain deferred-by-user, not resolved. No builds, tests, CI, production or source edits.
