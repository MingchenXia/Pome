# Strong time-Sobolev approximation of subgeodesic suprema by finite joins

**Date:** 2026-11-25  
**Finding:** POME-SUBGEO-FINITE-JOIN-STRONG-W11-001  
**Severity/status:** low / verified conditional deduction, not a printed error.  
**Main:** b6933b772f41b45918f7e25ed1afbbb1fd892272.

## Anchors and actual scope

- Integrated file: docs/sections/geodesic-rays-in-the-space-of-potentials/index.html, blob 52bf9e459a0dfb1c8afe79556db037450be06bb3. Direct selected reading, lines 7–399 (whole subgeodesics subsection 17.10.1 and initial Perron discussion), with the statement of 17.10.24 at 403–410; not the full 1956-line section.
- Definition 17.10.2, sgpt:9287531D / 8699FCF63094, lines 27–46; Proposition 17.10.7, sgpt:DBC4F9ED / 1880C1FBD88F, 88–139; Corollary 17.10.9, sgpt:B35F3B4F / C645EE3517E1, 144–171; Corollary 17.10.11, sgpt:9B844C56 / E31D1E7DDF87, 176–189.
- Proposition 17.10.13, sgpt:BBFDD373 / 5ECD747A7B0B, 194–266: arbitrary nonempty family of subgeodesics with uniformly upper bounded endpoints, supremum regularized separately on each time slice, again a subgeodesic with the endpoint suprema. This is the principal input. Proposition 17.10.15, sgpt:9B4FABF4 / E5064A497AB8, 271–296 and Lemma 17.10.16, sgpt:F358A89F / 3BEBB86C7F79, 301–350 were also read; their continuity and gluing arguments do not use the new deduction.
- Also read the entire problem exposition §24.11, docs/sections/problems-in-hermitian-pluripotential-theory--equations-on-singular-spaces/index.html, blob 95fe41df613a9b40e64fdd1f5992492e2add31f1, mathematical lines 7–24. Problem 24.11.1 (non-kahler-pluripotential-theory:A6F8C69E / A63319B4B931, lines 19–21) remains open; it explicitly distinguishes descent, finite mass and continuity. Its cited cone and curve results were not independently certified in this session. No claim to solve the problem.
- Actual ToC parsed from docs/index.html: 747 section links. Global compact-connected convention checked at docs/sections/conventions/index.html line 123. Prior coverage and findings preserved.

## Statement

Work under the exact hypotheses of Proposition 17.10.13. Write u^i for the given paths, u_t for the regularized supremum of their time-t slices (including the endpoints), and, for each nonempty finite F subset I, set v^F_t=max_{i in F} u^i_t. Fix any smooth positive volume dV. In addition to the printed conclusion, the inclusion-directed net of finite joins converges in both

\[
 C([0,1];L^1(X,dV))\quad\text{and}\quad W^{1,1}([0,1];L^1(X,dV)).
\]

In particular the time derivatives converge strongly in L1(dt dV), and the path variations converge. There is an increasing sequence of finite sets attaining both limits, but the assertion concerns the full directed net, not just that sequence.

This is conditional on the printed supremum theorem, its slice envelope inputs, and the scalar convexity, lower-envelope and q.e. endpoint conclusions identified above. It extends, rather than repeats, POME-GEO-SUBGEO-L1-VARIATION-W11-SHARP-001 (2026-11-11), which gives W11 and exact variation of an individual path, not convergence of the derivatives of finite joins. It is distinct from the earlier test-curve finite-join compact-time L1 result (POME-TC-FINITEJOIN-UNIFORM-L1-001) and from any family-uniform endpoint modulus.

## Proof

1. Each finite maximum is a subgeodesic by 17.10.13 (or by maximum on the strip and L1 convergence of finite maxima at endpoints). It is bounded above by u at every slice. Choose i0 in I and restrict to finite sets containing i0, a cofinal subset of the directed set. Set m0=inf_{0<t<1}u^{i0}_t. By 17.10.7 this is theta-psh, including the lower bounds at the endpoints. Thus m0 <= v^F_t <= u_t <= M, where M is a finite common constant upper bound for the endpoints and hence for all intermediate slices. The functions m0 and M are integrable. This bound does not require bounded singularities.

2. At each rational time in [0,1], including endpoints, the countable selection property for the slice supremum (the Choquet input cited in the printed proof of 17.10.13) gives a countable subfamily with the same regularized supremum. Union over these countably many times, include i0, enumerate it and let F_j be increasing finite initial sets (if the union is finite the sequence may stabilize). At a fixed rational time the raw increasing limit of the finite maxima equals its regularization almost everywhere by the envelope property used in the printed proof. Remove the union of the exceptional sets at these times. By 17.10.7 and 17.10.9, after additionally removing a single null set for the countably many paths v^F_j and u, all of their scalar time sections are finite continuous convex functions on [0,1]. The lower bound m0 is finite there. The pointwise increasing supremum of v^F_j is finite convex on the open interval and so continuous there; its agreement with u at the dense rational times implies equality at every interior time. At the two endpoints equality was already selected. Hence Dini's theorem for the continuous scalar functions on the compact interval gives pointwise-in-x uniform convergence. Since sup_t(u_t-v^F_j_t) is measurable (sup over rational times on the full-measure set) and bounded by M-m0, dominated convergence gives

\[
 \int_X \sup_{t\in[0,1]}|u_t-v^{F_j}_t|\,dV\longrightarrow0 .
\]

In particular the convergence is in C([0,1];L1).

3. At almost every (t,x) in (0,1) times X, all these convex functions and the limiting one are differentiable in t. Measurability follows using difference quotients and the joint measurable complexifications; the common exceptional product-null set follows by Fubini. At a differentiability point of u, sandwich the derivative of v^F_j between the two difference quotients at t-h,t,t+h. First let j tend to infinity at fixed h, then let h decrease to zero. This proves g_j=partial_t v^F_j -> g=partial_t u almost everywhere. For any continuous scalar convex function f on the closed interval, its absolute derivative integrates to f(0)+f(1)-2 min f (see the 2026-11-11 report for the full individual-path proof). By scalar uniform convergence the endpoint and minimum values converge pointwise in x. The expression is bounded by 2(M-m0). Dominated convergence and Tonelli therefore give

\[
 \int_0^1\!\int_X|g_j|\,dVdt\longrightarrow\int_0^1\!\int_X |g|\,dVdt.
\]

For real derivatives, |g_j-g| <= |g_j|+|g| and |g_j|+|g|-|g_j-g| -> 2|g| pointwise. Fatou's lemma for this nonnegative quantity gives limsup int|g_j-g|<=0 using convergence of the two norms. Thus the derivatives converge strongly in L1(dt dV). By the individual-path W11 representation, this is exactly convergence of the Bochner derivatives; step 2 already implies convergence of the paths in L1(dt dV). No MA measure or curvature limit has been exchanged.

4. The full finite-join net converges. For C([0,1];L1), every F containing F_j satisfies 0<=u-v^F<=u-v^F_j, proving the claim. For derivative convergence suppose otherwise: there exists epsilon>0 such that for every finite starting set some larger F has derivative distance at least epsilon. Recursively choose such bad sets G_j containing G_{j-1} union F_j. This is possible precisely by the asserted failure of net convergence, not by assuming a countable cofinal subset of I. Along this increasing sequence, squeeze v^F_j<=v^G_j<=u; step 2's pointwise scalar uniform convergence and common lower bound persist. Step 3 applies verbatim and contradicts the derivative distance. The discarded sets for the G_j are countable in number, so no uncountable union of null sets is used. The full net result follows; the variation assertion follows from strong derivative convergence and the individual-path identity.

## Adjudication and downstream use

The selected supremum theorem is not refuted. Its proof calls the product supremum a subgeodesic before establishing the endpoint property; this may simply be read as a jointly theta-psh interior path until the endpoint argument is finished. The new result requires the actual endpoint conclusion, not only joint positivity. A proposed optional corollary after 17.10.13 would enable strong time-Sobolev approximations of Perron envelopes in 17.10.20/22 whenever the endpoint theorem is applicable. It does not establish convergence of nonlinear MA products, convergence in d1 energy, or a uniform rate over families. No change to the source, registry, permanent tags, or canonicalization is proposed by this note.

Coverage: 1 selected repeat mathematical section (§17.10), 1 whole problem exposition (§24.11, previously legacy-unreconciled), zero complete transitive proof chains, zero new printed errors or unresolved proof gaps, one new conditional deduction. Historic first visits not asserted. All excluded Demailly regularization/Bergman/L2/Ohsawa–Takegoshi/multiscale/positivity-loss programmes remain deferred-by-user, not resolved or certified. No tests, build, CI or publication run.
