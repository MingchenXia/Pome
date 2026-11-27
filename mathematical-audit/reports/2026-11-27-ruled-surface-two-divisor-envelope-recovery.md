# Two-divisor recovery phase diagram on the ruled surface

Date: 2026-11-27. Reviewed main: b6933b772f41b45918f7e25ed1afbbb1fd892272. Audit parent: 6d35bffbb24d82efad3a166bcf58eddd84b3138c.

**POME-ENVSYS-RULED-TWO-DIVISOR-RECOVERY-001** — low / verified conditional deduction, not a false printed theorem. Whole direct conditional §16.29, mathematical lines 7–611 of `docs/sections/envelope-systems-over-hermitian-perturbations/index.html`, blob 856e240bbc5c86058ff861873f11e87db021e1bd. Previous selected readings (including the November 13 cutoff result) are not new discoveries; no historical first-visit claim.

## Anchors and assumptions

Use exactly the connected compact ruled surface of Lemma 16.29.16 (source non-kahler-pluripotential-theory:4D5EE4B0, permanent F6C7CDB99C6E, lines 283–359). Write D for the infinity section, F for one fiber, σ for the pullback of the flat probability form called σ_0 in that lemma, and κ=θ+σ for its Kähler form. Write ψ_D, ψ_F for the potentials in lines 350, 361–365, with θ+dd^c ψ_D=[D], σ+dd^c ψ_F=[F]. In particular θ is nef, its only positive representative is [D], and θ²=σ²=0 in cohomology, ∫θ∧σ=1. The last identity follows by integrating θ along each fiber, where it is normalized curvature of O(1).

Theorem 16.29.17 (source 8B6F5DC9, permanent 761E4875D2B4, lines 367–411) treats only the prescribed fiber pole of coefficient one. Proposition 16.29.18 (source D0AABEC0, permanent 7F133849FE58, lines 413–431) computes its mass decay. The retraction and ideal criterion are 16.29.9 (source 4E3712DE, permanent E94DE568F212, lines 134–191) and 16.29.11 (source 1152FB03, permanent 93A1136C4F72, lines 193–209).

## Claim

Fix any curve parameters a<c. Let b,d be nonnegative real numbers (fiber and section coefficients, respectively). Consider systems with constant parameter slices and with all-weight multiplier ideals
\[
\mathcal I(t q_\eta)=\mathcal O_X(-\lfloor tb\rfloor F-\lfloor td\rfloor D),\quad t>0.
\]
Such a system exists precisely for (b,d) in the closed unit square. It is unique for these prescribed data. It is realized in κ except when b=1 and d<1. In that exceptional edge every system has the same retraction, the constant curve with slice
\[
q_*=\psi_F+\psi_D-\sup_X(\psi_F+\psi_D).
\]
Thus the fiber of R over this curve contains a strictly ordered continuum of different systems. This is a statement about the prescribed two-divisor ideal family, not a classification of every possible ideal class in that fiber.

For every ε>0 along η=εκ, the exact total non-pluripolar mass is
\[
\int_X\mathrm{MA}^{\rm ext}_{(1+\epsilon)\kappa}(q_{\epsilon\kappa})
=2(1-d+\epsilon)(1-b+\epsilon).
\]
At ε=0 the mass of the retracted slice is 2(1-d)(1-b) throughout the square (including the nonrealized edge).

## Proof

1. Necessity. For every ε>0, q=q_{εκ} is a potential in the closed Kähler background (1+ε)κ. The all-weight ideal formula forces its generic Lelong numbers on F and D to be b and d, respectively (the printed generic valuative criterion, or the generic orders of the ideals for integer weights divided by the weight in the limit). Siu decomposition gives the closed positive residual
\[
T=(1+\epsilon)\kappa+dd^cq-b[F]-d[D]
\]
in class (1+ε-d)[θ]+(1+ε-b)[σ]. Pairing with the smooth semipositive σ yields 1+ε-d≥0. Pairing with θ is also nonnegative: pair first with the smooth semipositive θ_t+(t/4)π^*σ_0/π from lines 309–348, then let t→0 in cohomology (T is closed and has finite mass). This gives 1+ε-b≥0. Let ε decrease to zero. No convergence of T is assumed.

2. Sufficiency. For a pair in the square and every Hermitian η>0, the residual smooth background (1-d)θ+(1-b)σ+η has a smooth semipositive representative up to dd^c of a smooth function: take (1-d)θ_t+(1-b)σ+η, choosing t sufficiently small by the explicit lower curvature bound and compactness. (If d=1 take no correction.) Thus
\[
u_\eta=b\psi_F+d\psi_D+(1-d)f_t
\]
is (κ+η)-psh, with f_t from lines 342–348. The SNC coordinates at F∩D give precisely the displayed ideals by independent radial integration in each coordinate. This holds for arbitrary real b,d, with no rationality or common analytic-singularity coefficient requirement. Put q_η=P_{κ+η}[u_η]_I and take constant slices for τ<c. Projection preserves all-weight ideals; the uniqueness of fixed representatives in the same background proves compatibility for all η≥η', uniqueness of the system, and membership by Definition 16.29.2. Constants added for normalization do not change the ideals.

3. Recovery off the exceptional edge. If b<1, choose t>0 so that (1-b)σ dominates the negative bound on (1-d)θ_t. Then u=bψ_F+dψ_D+(1-d)f_t is already κ-psh. If b=d=1 use u=ψ_F+ψ_D. In either case take the constant original-background ideal-envelope curve. Its E-image is the system just constructed, by equality of ideals in every final background. Hence it is realized. This also includes d=1,b<1 with no correction.

4. Recovery on the exceptional edge. For b=1,d<1, Theorem 16.29.9 yields q=R(q_η) along a decreasing cofinal sequence. Its generic Lelong number on F is at least one by upper semicontinuity under the decreasing limit (the input used at lines 394–400). Consequently κ+dd^c q-[F] is a closed positive representative of [θ]. Lemma 16.29.16 identifies it with [D]. The canonical representatives then give q=q_* after normalization sup q=0. Its all-weight ideal data have both coefficients one. Hence Proposition 16.29.11 rules out realization for d<1. As d increases, the ideals decrease, and order preservation of the fixed ideal envelope makes q_η decrease. Distinct d have distinct ideals at some positive weight (take the weight large enough to separate the two floors), so the order is strict as an order of systems, although all retractions coincide. The b=d=1 system is the greatest realized system below every one of these edge systems and is the endpoint of this chain.

5. Mass calculation without an irrational-coefficient gap. In a closed background β=(1+ε)κ, subtract the two generic divisorial components from β+dd^c q_η as in step 1. The residual has the locally integrable potential w=q_η-bψ_F-dψ_D in the smooth background (1+ε-d)θ+(1+ε-b)σ. Its canonical quasi-psh representative is bounded above on the compact manifold. On the complement of F∪D, the normalized competitor u_η-sup u_η lies below q_η and supplies a lower bound for w, since its smooth remainder is bounded. The canonical representative extends that bound everywhere (use the local submean representative, or the a.e. order property of quasi-psh representatives). Hence w is bounded. This elementary argument avoids applying the analytic-singularity proposition 18.4.8 to a sum of arbitrary incommensurable divisorial coefficients. Plurifine locality identifies the non-pluripolar product of q_η with the bounded residual product off F∪D; both put zero mass on F∪D. Closed-background Bedford–Taylor/Stokes gives the residual mass as the square of its class, namely 2(1-d+ε)(1-b+ε). The same reasoning applies at ε=0 when there is an original-background competitor, as in step 3. For the nonrealized edge the limit has current [F]+[D] and zero non-pluripolar mass, agreeing with the formula at ε=0. No passage of untruncated Monge–Ampère products through a limit is used.

## Direct review and dependencies

Read §16.29 mathematical lines 7–611 at the pinned main. Checked normalization/endpoint and transition inequalities (7–128), cofinal retraction/adjunction (129–215), gauge constants and smooth torus mass noninvariance (216–268), ruled-surface Hessian and Schur complement (269–359), fiber pole/zero mass construction (360–431), Hopf transverse descent and system compatibility (432–512), conditional recovery and countable hyperplane example (514–589), exact pullback caveat (590–611). The Hessian off the section has mixed entry it(1-tv²)/(2(1+t|v|²)²); its Schur complement is t(1-t|v|²)/(4(1+t|v|²)), and at infinity the complement is A-t/4, as printed. The cofinal comparison and the gauge bounds are pointwise with uniform constants. Exact pullbacks are not independent positive-background systems.

Selected dependency entries 18.4.2 (7F20FD198864), 18.4.6 (EAFF378DAF48), 18.4.8 (EB95710FF4D7), 13.21.7 (9EA752566EF2) were retrieved; no full upstream certification. The deduction uses the printed projection, generic Lelong/Siu, canonical representative, bounded-product and retraction inputs. The Hopf recovery part uses 13.21.7 and the countable hyperplane formulas 13.24.7–8, not certified here. Any regularization inputs in those chains remain deferred-by-user, not reopened. No new demonstrated gap in the printed ruled-surface argument: its coefficient-one case is valid conditional on those inputs. The new statement is a proposed audit-note extension, not an edit to any theorem, registry, source, or tag.

Also reread §3.7 lines 7–37 (blob a4a17c61ef30efb6fc6e20f105baeca052bbed43) and §3.6 lines 7–93 (blob 1d3c9ebe0d7093f0f069dc2b25b0a47f907a), repeat only; the grid approximation and separate subharmonicity example are not new. Selected excerpts from §19.3/19.9 and whole short §19.10 were repeat/context only, not counted in the fresh coverage delta. No builds, tests, CI, website publication, production edits or complete transitive certification. Matrix has 747 distinct section rows; chapter 16's 44 actual current ToC entries match exactly. One full direct present-current section newly recorded in the matrix; previous selected audit reports preserved.
