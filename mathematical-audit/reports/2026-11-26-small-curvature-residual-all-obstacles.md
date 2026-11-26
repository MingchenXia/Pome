# Small-curvature residuals are invisible to all ordinary obstacle envelopes in a strict type

Date: 2026-11-26. Reviewed main: `b6933b772f41b45918f7e25ed1afbbb1fd892272`; starting audit branch: `56dd82f5ab73f4e91b4f2a4a021784e932207978`.

## Finding POME-SMALL-CURVATURE-RESIDUAL-ALL-OBSTACLES-001

**Severity/status:** low / verified conditional deduction, not a refutation of an existing theorem. No Demailly regularization or dedicated prerequisite programme is used in the new argument.

### Exact reading-edition anchors

* docs/sections/multiplier-ideal-envelopes-and-goodness--small-curvature-and-strict-ordinary-types/index.html, blob a6e3cc7cb9c6931688e089bb67b2ed12766f6a0b. Equation 18.27.1 (permanent 4A552AB10BA9, physical lines 7–14), Lemma 18.27.2 (96F4F5465740, lines 18–41), Theorem 18.27.4 (0E6CABEB995A, lines 76–95). Lemma 18.27.3 (E5C4A193363D, lines 49–62) invokes classical current regularization 5.36.3 and is **deferred-by-user**, not examined or certified here. In 18.27.4 only the subtraction/order and converse construction are checked; its smooth-representative implication retains that deferred dependency.
* docs/sections/plurisubharmonic-functions-and-singularities--obstacle-envelopes/index.html, blob 30716faee83d2ac0ec84b3684e319210980bd14f, Definition 5.40.4 (65C9C3635D58, lines 118–135); envelope definition and bound in lines 20–36, 73–82. The smooth approximation premise in 5.40.3 is not used.
* docs/sections/plurisubharmonic-functions-and-singularities--normalized-compactness/index.html, blob d7ff8eafea43197c77de4bfd335bed0764ab4f69, Theorem 5.25.2 (FC59B7D406A3, lines 32–52), specifically its uniform L1 estimate for normalized h-psh functions.
* docs/sections/problems-in-hermitian-pluripotential-theory--topologies-on-singularity-types/index.html, blob a351191a71a44cda68bc8aa1ed801049449fbd0f. Whole mathematical exposition lines 7–93; Problem 24.8.4 (35C633451730, line 89) remains open. Lines 26–32 distinguish all-obstacle equality from equality at zero; lines 67–82 describe first polar and higher residual obstructions. Regularization-dependent references at lines 17, 23, 39, 48 are recorded as dependencies, not reopened. No cited theorem is certified transitively by this exposition read.

### Statement

Let X be a connected compact complex manifold, h a Hermitian form and theta a smooth real (1,1)-form, not necessarily closed. Suppose u is theta-psh and its ordinary type has a strict representative s, i.e. s ~ u and theta+dd^c s >= epsilon h for some epsilon>0. Suppose q is quasi-psh and satisfies (18.27.1): for every delta>0 there exists q_delta ~ q with dd^c q_delta >= -delta h. No assumption of boundedness, analytic singularities, bounded mass or positive lower mass is made.

Then the type of u+q admits a strict theta-psh representative v, and for every continuous real obstacle F one has

\[
P_{\theta,F}[v]=P_{\theta,F}[u].
\]

The left side depends only on the ordinary type, so it can be denoted by the envelope of the summed type. Furthermore, for every competitor w in the definition of the right side and every 0<t<1 there is a competitor w_t in the definition of the left side such that

\[
\|w_t-w\|_{L^1}\le t(\|s_F-w\|_{L^1}+\epsilon C_h),
\]

where s_F is a fixed translate of s below F, and C_h is the normalized compactness constant. Competitors of **exact** summed type are L1-dense in the original competitor set in the sense that every original competitor is an L1 limit of exact-summed-type competitors (not an assertion of equality of the two sets).

### Proof

Normalize q_delta by subtracting its supremum, so q_delta<=0. The scaled function q_delta/delta belongs to PSH(X,h) and has supremum zero. Theorem 5.25.2 yields

\[
\|q_\delta\|_1\le C_h\delta.
\]

For a fixed delta_0 in (0,epsilon), set v=s+q_{delta_0}. The sum of quasi-psh functions is quasi-psh and finite almost everywhere. Addition preserves bounded type inequalities in the extended-real sense, so v~u+q and theta+dd^c v >= (epsilon-delta_0)h. In particular the summed type is admissible and strict. Since q_{delta_0}<=0 and s~u, one has v<=u+C; hence every competitor of the summed type is an original competitor.

Fix a continuous F and subtract a constant from s to obtain s_F<=F (compactness and the lower bound of F suffice). Let w<=F be theta-psh with w<=u+C_w. Put

\[
w_t=(1-t)w+t s_F+q_{t\epsilon}.
\]

Then
\[
\theta+dd^c w_t=(1-t)(\theta+dd^cw)+t(\theta+dd^cs_F)+dd^cq_{t\epsilon}\ge0.
\]
Also w_t<=F, and w_t<=u+q+C_t because both w and s_F are more singular than or equivalent to u and q_{t epsilon}~q. Equivalently w_t<=v+C'_t, including at poles. Thus w_t is a competitor of the summed type. The L1 estimate follows immediately from the normalized q bound and the triangle inequality.

Let P be the left envelope. It is theta-psh by the upper-envelope result, since the competitor family is nonempty and bounded above. It dominates every w_t pointwise. Along any sequence t decreasing to zero, L1 convergence has an almost-everywhere convergent subsequence, so P>=w almost everywhere. The local submean representative comparison (5.24.3) gives P>=w everywhere. Taking the supremum over all original competitors and then upper semicontinuous regularization gives P>=P_{theta,F}[u]. The opposite inequality was proved above. No choice uniform in w is needed, nor any interchange of supremum and limit.

For exact-type approximants, translate v to v_F<=F. For each t and positive integer j, max(w_t,v_F-j) is theta-psh (local maximum principle), is below F, and has exactly the type of v: it lies above v_F-j and below v_F plus a constant. As j tends to infinity it decreases pointwise to w_t. Its difference from w_t is nonnegative and dominated by (v_F-w_t)_+, which is integrable. Dominated convergence lets us choose j(t) with L1 error at most t. The resulting exact-type approximants converge to w with explicit error at most t(1+||s_F-w||_1+epsilon C_h). This is a sequence construction, not an assertion about sequential compactness in a nonmetrizable topology.

### Consequences and limits

* For u=0 and theta=h (or any smooth strictly positive theta), a small-curvature residual can be unbounded yet its ordinary envelope equals the unrestricted envelope below every continuous F. This does not assert q is bounded or ordinarily equivalent to zero.
* Under the smooth positive representative hypothesis of 18.27.4, the divisorial type sigma_Delta itself is strict: sigma_Delta+f has curvature [Delta]+B+dd^c f. Consequently adding q leaves all its ordinary obstacle envelopes unchanged. This strengthens the sufficient direction of 18.27.4 without invoking its regularization-dependent necessary direction.
* If a strict ordinary type has a nonzero envelope deficit after adding a quasi-psh residual, the latter cannot satisfy (18.27.1), whenever the summed type is admissible. In particular this criterion does not identify all zero-Lelong or zero-first-polar-curvature residuals with small-curvature residuals.
* No assertion about ideal envelopes, equality of non-pluripolar masses, or arbitrary nonstrict types is made. The general zero-volume/nonbig extension problem 24.8.4 remains open. All upstream statements used as internal dependencies (normalized compactness, maximum, upper-envelope and representative comparison) remain conditional at the transitive level.

### Scope, novelty and ledger

The 2026-11-12 small-curvature diffuse Green/multipole threshold report already reviewed §18.27 in part; do not count this as a historical first visit or repeat its construction. The new argument compares arbitrary ordinary strict types under all continuous obstacles, rather than deciding the strictness of a curve divisor. The matrix is updated with selected nonexcluded review, not whole-section certification, since 18.27.3 is deferred.

In Lemma 18.27.2 the scaling, Gauduchon trace bound and pullback of the lower curvature bound are valid conditional on its cited inputs (5.38.8, 5.46.3/7, 11.4.2, 5.43.18); no re-proof of those chains is asserted. In Theorem 18.27.4 the divisor subtraction, ordinary comparison off the divisor and converse curvature estimate are valid conditional on their cited inputs. No new source error or demonstrated proof gap is reported.

Whole direct exposition §24.8, selected mathematical §18.27 and dependency statements §§5.25,5.40. The actual main table of contents and durable matrix have 747 numbered sections each, no duplicate or missing identifiers. No first historical visit or full transitive proof certificate is claimed.

**Proposed correction/addition:** optional independent corollary following §18.27.4, with cross-reference from §24.8. No changes to the reading edition, registry, sources or permanent tags. The excluded regularization/Bergman/L2/OT/multiscale/positivity-loss work remains deferred-by-user, not resolved or certified. No tests, project builds, CI, website publication or merge performed.
