# Measurable Monge–Ampère density and plurifine continuity

Date: 2026-11-24. Reviewed main: b6933b772f41b45918f7e25ed1afbbb1fd892272.

Freshly read AGENTS.md (eda69505b93b4782290d9cfac07c8651dedd17c5), documentation/proof-expansions.md (8b37e218c74d5a93637e0f092cf5f29cc338a94d), audit LATEST and README and the existing matrix and ledger. The chapter 5 rendered TOC confirms the locators below. The following are present-main direct reads, not claims of historically first visits or complete upstream certificates. No excluded Demailly approximation, Bergman, L2, Ohsawa–Takegoshi, multiscale or positivity-loss programme was reopened. Elementary Euclidean convolution here is the bounded local product calculus, not Demailly approximation.

## POME-CONTINUOUS-MA-AC-DENSITY-MEASURABLE-001

Severity: low. Status: verified conditional deduction, not a false printed theorem.

Location: docs/sections/plurisubharmonic-functions-and-singularities--products-with-smooth-backgrounds/index.html, blob e2ba89b51376ba0296846221109c664a0c29b2c3, Lemma 5.28.10 source tag 60F484B5, permanent C5B4B944142C, lines 185–196; Lemma 5.28.12 source tag 106856C9, permanent 00AB47766404, lines 205–216. The earlier mixed inequality is Lemma 5.28.7, permanent 6C81352D9EE7, lines 134–179, in particular equation 5.28.9, permanent 4547B4E0976D.

**Strengthening.** Let U be an open subset of C^n, beta=dd^c|z|^2, theta a smooth real (1,1)-form (not necessarily closed), u continuous, and T=theta+dd^c u positive. Write the Lebesgue decomposition of the bounded product as T^n=F beta^n+nu_s, with F nonnegative locally integrable and nu_s positive singular. Then
\[
  \det_\beta T_{\rm ac}=F \quad\text{almost everywhere}.
\]
Neither continuity of F nor absence of nu_s is required. More generally the convolution inequality of Lemma 5.28.10 holds for a measurable g>=0 in L^n_loc with T^n>=g^n beta^n.

**Proof.** Work on a relatively compact coordinate ball and a smaller ball with a margin for all translations in the support of a fixed smooth compactly supported probability kernel chi_delta. Let a finite partition of the kernel support into Borel pieces of diameter at most h have kernel masses w_i, and choose a representative y_i in each piece of positive mass. Set T_h=sum_i w_i T(.-y_i), g_h=sum_i w_i g(.-y_i). All the translated currents are positive; their potentials are continuous and their backgrounds smooth. Repeated use of (5.28.9) gives T_h^n>=g_h^n beta^n. Translation of beta is exact because it is constant.

As h tends to zero, the averaged potentials converge uniformly on smaller compact sets to u*chi_delta, and averaged smooth backgrounds converge in C^infty there (each derivative is uniformly continuous on the compact enlarged set). For g, extend its restriction to a sufficiently enlarged relatively compact neighborhood by zero. Translation is continuous in L^n(R^{2n}), including n=1, as follows by density of continuous compactly supported functions and translation invariance of the norm. Minkowski's integral inequality bounds the L^n error between g_h and g*chi_delta by the supremum of the translation differences over shifts of size at most h. Hence g_h converges in L^n on the smaller ball. In particular g_h^n tends to (g*chi_delta)^n in L^1, using
\[
 |a^n-b^n|\le n|a-b|(a+b)^{n-1}
\]
and Hölder (for n=1 just the L^1 bound).

For clarity, uniform convergence of the potentials here implies weak convergence of the products even though the backgrounds are not closed. Choose a common fixed quadratic correction q so that the corrected potentials are bounded PSH on a smaller ball, including the limit. Expand each product into closed Hessian powers and smooth background factors as in (5.28.1). For the closed factors, telescope the difference of powers, pair with a smooth test form, and use closedness to integrate dd^c onto the test. The resulting bound is a constant times the sup norm of the potential difference times the local mass of mixed bounded Hessian products. Nested cutoffs bound these masses uniformly. Smooth background factors and their derivatives converge; their replacement in the tests is justified by the same uniform local mass bound. This gives T_h^n -> (T*chi_delta)^n weakly. It follows that
\[
 (T*\chi_\delta)^n\ge (g*\chi_\delta)^n\beta^n .
\]

Now take g=F^{1/n}. For a shrinking smooth nonnegative radial approximate identity, T*chi_delta -> T_ac coefficientwise almost everywhere by differentiation of finite coefficient measures, and g*chi_delta -> g at Lebesgue points of g. Thus det_beta T_ac >= F almost everywhere. The same bounded-product continuity argument, now with delta tending to zero and the uniformly convergent continuous potentials, gives (T*chi_delta)^n -> T^n weakly. The convolved forms are positive. Fatou applied to their nonnegative determinants times each nonnegative compactly supported test function gives (det_beta T_ac) beta^n <= T^n as measures. By uniqueness of the Lebesgue decomposition, det_beta T_ac <= F almost everywhere, proving equality. No assertion about the size or support of nu_s follows from this argument.

For instance, continuity of u does not imply nu_s=0: in dimension one, u(z)=max(0,log|z|^2) on an annulus meeting |z|=1 with theta=0 is continuous subharmonic; its dd^c is the normalized circle measure, singular with respect to beta. The formula gives F=0 and T_ac=0, as required.

Dependencies: the printed bounded-product local expansion and positivity (5.28.2), closed mixed inequality (5.27.5, permanent DBC85A3C1608, lines 138–144 of the local-products-and-capacity section, blob ddb2ac8d9de27a22152872e07e5e787d138a790e), and the local measure differentiation theorem used by 5.28.12. These are not certified transitively here. Suggested correction: none needed in the current theorem; optionally broaden the statements of 5.28.10 and 5.28.12 and include the above L^n quadrature argument. The existing continuous-density applications retain their hypotheses; no downstream theorem needs repair on this account.

## POME-PLURIFINE-QPSH-POLE-CONTINUITY-001

Severity: low. Status: verified local proof repair, not a false theorem.

Location: docs/sections/plurisubharmonic-functions--plurifine-topology/index.html, blob 855febeeb3846c2e749c80b5381a5a80ca3c6e7b, Proposition 5.15.18, source tag 53418890, permanent E49CF7960E4C, lines 329–355. Line 335 claims that continuity on the finite-valued locus suffices because the pole set is closed. Closedness of that set alone does not prove continuity there. Line 343 asks for an ordinary open neighborhood in a set already only known to be plurifinely open; an ordinary open neighborhood in the ambient domain suffices for the subsequent bounds.

**Replacement proof.** Locally write phi=psi+b with psi PSH and b smooth real-valued. Definition 5.47.14 (permanent 09A00D4B8096, docs/sections/pluripolar-sets-and-the-plurifine-topology/index.html, blob 1bfa1fc213c9d9cf3db6ec015a10aeb21617aa2c, lines 275–286) gives plurifine continuity of psi and contains the ordinary topology, so b is plurifinely continuous. Addition from [-infinity,infinity) times R into [-infinity,infinity) is continuous in the order topology, with -infinity+b=-infinity. Explicitly, at a finite-valued point use ordinary continuity of addition. At a pole x, given any real c choose a local bound b<=M and intersect that ordinary neighborhood with {psi<c-M}; it contains x and phi<c there. This verifies the neighborhood criterion at the pole. It also works for an arbitrary continuous correction b. Hence phi is plurifinely continuous. No assertion about Euclidean openness of its strict superlevels is needed.

Affected local dependents: Corollaries 5.15.19 and 5.15.21 (lines 361–420), using comparison sets and quasi-extrema. Their conclusions stand. In 5.15.21, the displayed W is read as the union of the two pole loci (points where either potential is -infinity), not a choice of only one locus. The finite-locus difference is continuous; removing additional pluripolar sets does not change extrema by the fine density lemma. No new density-one finding is claimed; the earlier POME-FINE-NEIGHBORHOOD-LEBESGUE-DENSITY-ONE-001 already covers the real fine topology.

## Coverage and limits

- Entire mathematical body of 5.15, physical lines 7–441: thinness witness normalization and global logarithmic-series construction, finite unions, Cartan equivalence, topology base and local restriction, compact fine neighborhoods, holomorphic pullback, quasi-PSH continuity, pluripolar density and quasi-extrema. Checked the normalization in 5.15.6: subtract the finite value at x and scale the strict negative gap before truncating below at -1. The construction's finite value at x guarantees its decreasing PSH sum is nontrivial. See repair above.
- Entire mathematical body of 5.28, physical lines 7–248: binomial independence and coefficient freezing, contact inequality (compact-set portmanteau in the correct direction), submersion pullback, C^{1,1} coefficients, determinant lower bound, mixed inequality and its partition-of-unity error estimate, convolution, ac density, convex two-potential chain rule. In the freezing step of 5.28.7 the error is controlled by a fixed positive locally finite measure; the partition weights sum to one, so no cardinality loss. No newly confirmed false theorem. The chain-rule and BT inputs are not certified transitively.
- Selected dependencies only: 5.27.1–2 and 5.27.5 (physical lines 11–60 and 138–144), and Definition 5.47.14 and its basic-neighborhood discussion (275–286). No whole-section claims for these two long sections.
- Two whole current direct mathematical readings, two selected dependencies, one new conditional strengthening, one local proof repair, zero confirmed false theorems, zero complete transitive proof certificates. Existing deferred notes unchanged. No build, tests, CI, production/body/registry/tag or publication edits.
