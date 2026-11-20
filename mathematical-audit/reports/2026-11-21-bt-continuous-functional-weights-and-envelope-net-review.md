# 2026-11-21: decreasing Bedford–Taylor products and $P$-envelope nets

**Baseline:** main commit `b6933b772f41b45918f7e25ed1afbbb1fd892272`. Audit branch: `review/mathematical-audit`. This report concerns only the *current integrated reading edition*, not the source repositories. The exclusions requested on 2026-10-17 (Demailly regularization/approximation and its dedicated Bergman, L2, Ohsawa–Takegoshi, multiscale-atlas and positivity-loss programme) were not reopened.

## Exact scope and source provenance

1. **Entire mathematical §7.3**, `docs/sections/bedford-taylor-products-and-local-capacity--decreasing-continuity-and-symmetry/index.html`, blob `96a9e39e85fab5774ebdac0c6d9d006338a4e42c`, physical lines **7–363**. Main anchors: Theorem 7.3.7, source `foundations-of-pluripotential-theory:8B1F9B78` / permanent `D87C13B3250A`, lines **134–229**; Corollary 7.3.8, source `foundations-of-pluripotential-theory:45C06B5C` / permanent `8BD7803A393B`, lines **234–274**; Proposition 7.3.10 `0453AAB39932`, lines **279–300**; Theorem 7.3.11 `D0AF90DDC7A5`, lines **304–341**; Corollary 7.3.12 `F2BBEF3BF09B`, lines **346–363**.
2. **Entire mathematical §16.4**, `docs/sections/the-envelope-operators--p-envelopes--properties-of-the-p-envelope/index.html`, blob `8e6c974a566fdf9d42b6bffbdb67422b7427f655`, physical lines **7–263**. Anchors: Proposition 16.4.1 source `sgpt:0C43BCE4` / permanent `055CAE14F80F` (lines **11–34**); 16.4.2 `CF5FECD1B547` (39–89); 16.4.3 `8EB68D9BFB64` (94–107); 16.4.4 source `sgpt:DE839E2D` / permanent `048490BEAC8C` (112–181); Corollary 16.4.8 `953C40C3B9B8` (186–210); Proposition 16.4.9 source `sgpt:1A5AE3C4` / permanent `3654A10A0CCC` (215–263).
3. **Selected dependency checks only, not entire sections:** CLN Theorem 7.2.5 (`docs/sections/bedford-taylor-products-and-local-capacity--bounded-potentials-and-recursive-products/index.html`, blob `18bd2395f3b76941b2c677079c09eb6accc5a9cb`, lines **99–117**, permanent `2A84C325AB58`); Corollary 5.17.5 (tag `B5E91AB35965`, lines 6–33 of its tag page); Corollary 13.13.12 (`37623491DEDC`, lines 6–45); Corollary 13.13.16 (`7CB7A3C51640`, lines 6–76); Lemma 13.13.30 (`1CC7CDBE65A9`, statement lines 6–16). None of these selected checks certifies the entire upstream chain.

## Finding POME-BT-CONTINUOUS-FUNCTIONAL-WEIGHTS-001

**Severity:** low. **Status:** verified conditional deduction; **not** a false statement or a repair of a printed error. **Dependency:** the printed decreasing Bedford–Taylor weighted convergence in Theorem 7.3.7, the polynomial-weight extension in Corollary 7.3.8, and the local Chern–Levine–Nirenberg estimate in Theorem 7.2.5.

**Claim.** Let \(\Omega\subset\mathbb C^n\) be open, let \(T\) be a closed positive current of bidimension \((r,r)\), and fix \(0\le q\le r\). Suppose \(u_{1,j},\ldots,u_{q,j}\) and \(v_{1,j},\ldots,v_{m,j}\) are decreasing sequences of locally bounded plurisubharmonic functions, with locally bounded limits \(u_1,\ldots,u_q\) and \(v_1,\ldots,v_m\), respectively. Write
\[
S_j=dd^cu_{1,j}\wedge\cdots\wedge dd^cu_{q,j}\wedge T,
\qquad S=dd^cu_1\wedge\cdots\wedge dd^cu_q\wedge T.
\]
For **every continuous** \(F:\mathbb R^m\to\mathbb R\), not necessarily polynomial, positive, monotone or differentiable, one has the weak convergence of signed currents
\[
\boxed{\ F(v_{1,j},\ldots,v_{m,j})S_j
\longrightarrow F(v_1,\ldots,v_m)S\ }.
\]
More generally, on each fixed compact range containing all these weight vectors over the support of a test form, one may replace \(F\) on the left by bounded Borel symbols \(F_j\) satisfying \(\|F_j-F\|_\infty\to0\) on that range. In particular this covers moving continuous symbols converging uniformly on compact sets. This statement is **sequential**; no unproved extension to arbitrary directed nets is asserted.

**Proof with all limit interchanges.** Fix a compactly supported test form \(\eta\) and compact sets \(K\subset\operatorname{Int} L\Subset\Omega\) with \(K\supset\operatorname{Supp}\eta\). The decreasing locally bounded families are uniformly bounded on \(L\) by their first terms and their locally bounded limits. Choose \(M>0\) so that all \(v_{a,j}|_K\) and \(v_a|_K\) belong to \([-M,M]\). By the CLN bound (7.2.5),
\[
\sup_j \|S_j\|_K+\|S\|_K<\infty.
\]
Fix \(\varepsilon>0\). We construct a real polynomial \(P\) with \(\sup_{[-M,M]^m}|F-P|<\varepsilon\), without importing an approximation theorem: transfer the cube affinely to \([0,1]^m\) and use the multivariate Bernstein polynomials. For a continuous \(G\) on \([0,1]^m\),
\[
B_NG(t)=\sum_{k_1,\ldots,k_m=0}^N G(k/N)\prod_{a=1}^m\binom N{k_a}t_a^{k_a}(1-t_a)^{N-k_a}.
\]
Interpreting this as \(\mathbb E\,G(K_1/N,\ldots,K_m/N)\) for independent binomials \(K_a\), Chebyshev and a union bound yield, uniformly in \(t\),
\[
|B_NG(t)-G(t)|
\le\omega_G(\delta)+\frac{m\|G\|_\infty}{2N\delta^2},
\]
where \(\omega_G\) is the modulus of continuity. First choose \(\delta\) small and then \(N\) large, obtaining the polynomial \(P\). The finite polynomial assertion of Corollary 7.3.8 gives \(P(v_{1,j},\ldots,v_{m,j})S_j\to P(v_1,\ldots,v_m)S\). Since the current coefficient measures are bounded by their trace measures and \(\eta\) has bounded coefficients, there is a constant \(C_\eta\), independent of \(j\) and \(P\), with
\[
\begin{aligned}
|\langle F(v_j)S_j-F(v)S,\eta\rangle|
&\le 2C_\eta\varepsilon
+|\langle P(v_j)S_j-P(v)S,\eta\rangle|.
\end{aligned}
\]
Taking \(j\to\infty\), then \(\varepsilon\downarrow0\), proves the claim. If \(F_j\to F\) uniformly on the box, the extra term is bounded by \(C_\eta\|F_j-F\|_\infty\to0\). No interchange of polynomial approximation and current limits occurs without this uniform mass bound. \(\square\)

**Why this is not simply the printed polynomial claim.** The statement handles any continuous nonlinear functional calculus, for example \(F(t_1,t_2)=|t_1-t_2|\), \(\min(t_1,t_2)\), or a nonanalytic smooth/continuous cutoff, including a moving uniformly convergent family of such symbols. No differentiability or psh property of \(F(v_j)\) is assumed; only bounded Borel multiplication of a positive order-zero current is required. The statement is consistent with the previous **POME-BT-NONQC-FIXED-WEIGHT-CONCENTRATION-001** obstruction for discontinuous fixed Borel weights, which is **not** re-counted here; continuous \(F\) is essential to this argument.

**Proposed correction / downstream use:** no correction to the printed theorem. The strengthening could be placed as a reviewable corollary *after* 7.3.8, without replacing the existing historical source or permanent tags. Useful to later capacity/contact-set comparisons using continuous cutoffs of multiple moving bounded psh weights. No source, registry, or canonicalization file is changed.

## Direct mathematical checks, without new confirmed printed errors

**§7.3.** Verified the compactly supported current integration by parts in Lemma 7.3.3 (lines 40–69), the upper-semicontinuous-weight semicontinuity lemma (74–89), smoothing/monotonicity of the two-variable regularized maximum (97–114), and the collar + induction + trace-mass proof of Theorem 7.3.7 (134–229). Corollary 7.3.8's signed polynomial polarization (234–274) is finite; locality on the Borel, not necessarily open, strict-order set in Proposition 7.3.10 (279–300) is appropriately proved using smooth approximants; the comparison and domination arguments (304–363) retain their boundary and local boundedness hypotheses. The printed hypotheses are not asserted removable.

**§16.4.** Checked the exact pullback correspondence in 16.4.1 conditional on 5.17.8 and birational non-pluripolar mass invariance, concavity/order in 16.4.2, and arbitrary decreasing directed nets of normalized fixed points in 16.4.3 (not replaced with merely sequential compactness). In 16.4.4, for each fixed tail \(i\ge i_0\) the varying-background potentials lie in \(\mathrm{PSH}(X,\theta+\epsilon_{i_0}\omega)\); thus Corollary 13.13.16 applies only after fixing \(i_0\), as written. The lower mixed-mass bound and upper contact-mass bound have the correct orientations. Lelong convergence uses the *positive limit mass*, the scalar \(\delta\)-comparison and the fixed-tail uniform Lelong bound. Corollary 16.4.8 and increasing-net Proposition 16.4.9 use the positive-mass quantitative domination input and a uniform \(L^1\) bound for normalized envelopes, not a fictitious cofinal sequence. No new confirmed printed error was established in these clauses.

## Open/deferred ledger and coverage limitation

- **Unresolved / external-input verification:** full independent proofs of the original bounded weighted BT convergence (7.3.7), the complete CLN recursive proof (7.2.5), the global non-pluripolar comparison/quantitative domination chain (13.13.11–13.13.30), and all connected assumptions of 5.17.8 remain **not transitively certified**. The explicitly selected premises above were checked only as needed; no false theorem is claimed.
- **Deferred-by-user (unchanged):** Demailly regularization/approximation, dedicated Bergman, L2, Ohsawa–Takegoshi, multiscale-atlas, and positivity-loss completion efforts; pre-existing notes stay deferred, not resolved.
- **Exact increment:** **two entire direct mathematical reading sections** (§7.3 and §16.4), **five selected prerequisite statements** in three other sections, **one new verified conditional deduction**, **zero** newly established whole-upstream-chain certifications. Historical first-visit statuses remain unreconciled. No tests/builds, CI, publication, main/source/registry/permanent-tag changes.
