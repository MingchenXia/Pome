# Complex Hessian audit: Liouville rescaling, trace absorption and \(L^1\)-stable mixed products

**Date:** 2026-11-21. **Main SHA:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`. **Audit branch starting SHA:** \`8d0f8c8ff318a0b0de4b687df9faf35e324f0ea8\`. The **integrated reading edition** was read directly, not merely source statements or matching theorem numbers. No main, mathematical source, registry, canonical tag, site or CI changes.

## Exact scope (three whole directly examined sections)

| Integrated reading file on main | Blob SHA and physical mathematical lines | Statements and proof steps inspected |
| --- | --- | --- |
| \`docs/sections/complex-hessian-equations--liouville-and-gradient-estimates/index.html\` (§8.3) | \`74cda06ad4bf75ab5fcba6e841c9ad4aa9424981\`; **5–157** of 168 lines | Lemma **8.3.1** source \`non-kahler-pluripotential-theory:88E13750\`, permanent \`89F810E43B3E\` (line 20); Theorem **8.3.2** source \`32D9A170\`, tag \`96D01E7C4F0F\` (line 34); Proposition **8.3.3** source \`A456C079\`, tag \`B863BB49A505\` (line 113). |
| \`docs/sections/complex-hessian-equations--a-trace-estimate-with-a-prescribed-potential/index.html\` (§8.4) | \`3d7fe6d1867a0d8ac268042a59e112329a6c8af3\`; **5–311** of 322 lines | Lemmas **8.4.1–8.4.2**, permanent \`B276B9DFAC29\`/\`61C6DAF48B41\` (lines 20, 36); Proposition **8.4.3**, tag \`FDAFFF47B8A3\` (80); torsion/eigenvalue and gradient Lemmas **8.4.4–8.4.5**, tags \`C357698AC1AF\`/\`174BDA603BF2\` (105,161); Proposition **8.4.6**, source \`77D3B686\`, tag \`23966DC8CDBF\` (189); Corollary **8.4.7**, tag \`BEA27E46DAEE\` (295). |
| \`docs/sections/complex-hessian-equations--bounded-complex-hessians-and-elliptic-extensions/index.html\` (§8.5) | \`fdd9225b1d778e1debaf94f75ef65175d4bd4484\`; **5–148** of 159 lines | Lemma **8.5.1**, source \`non-kahler-pluripotential-theory:835B5652\`, tag \`89771FD1FD15\` (11); Lemma **8.5.2**, source \`E0A89860\`, tag \`1881F6670EF4\` (33); Lemma **8.5.3**, source \`B1F0AA6B\`, tag \`BAC60298D0F2\` (63); Proposition **8.5.4**, source \`659459E7\`, tag \`6FBA7BB8AC94\` (123). |

§8.1 (the project-wide **\(2\le m<n\)** convention) and selected §8.2 cone inequalities are used as stated, **not** counted as whole-section reviews. The Euclidean Liouville argument of §8.3 itself explicitly allows \(1\le m\le n\); the later compact Hessian ellipticity argument uses \(m\ge2\).

## Verification notes, with distinctions

**§8.3:** Local uniform limit stability uses strict lower test functions; the comparison argument is a strictified contact test, not an unsupported measure limit. For bounded normalized \(0\le v\le1\), \(v\) and \(v^2\) are subharmonic. Monotone radial convolution averages tend to 1 and are asymptotically translation-independent. The dichotomy fixes the small-radius \(\rho\) before choosing the large radius and uses a nonzero directional Dirichlet integral when the reduced-dimensional Liouville alternative is ruled out. In Proposition 8.3.3, the \(\Gamma_2\) inequality bounds all Hessian eigenvalues by the trace, rescaling kills the smooth background by \(R_j^{-2}\), and the upper density bound \(BR_j^{-2m}\to0\) excludes a strictly admissible lower test. The key unproved transitive inputs are the Euclidean subharmonic/Hessian-cone comparison, local elliptic estimates and the base Liouville theorem. No new confirmed printed error from this check.

**§8.4:** In Lemma 8.4.1, \(|a-b|^2\ge(7/8)|a|^2-7|b|^2\) and \(\chi''=12q^2\) give exactly \(84q^2|b|^2\); the \(q\ge8\) absorption leaves \(q^2|a|^2-1\). Lemma 8.4.2 uses the **positive** \(F_i\) and the lower cone bound \(F_i\ge f_0/(m!S)\); the fixed comparison derivative \(b_i\) must remain in the error. Proposition 8.4.3 has two genuinely separate eigenvalue regimes. Lemma 8.4.4 differentiates a lower support for the top eigenvalue while keeping \(D^2F\) at the **unperturbed** \(W\), a necessary distinction for the spectral concavity term. The proof of Proposition 8.4.6 chooses the small tolerance \(\varepsilon\), then the large weight \(A\), then \(\delta\): the trace bound is uniform in derivatives of \(v\), **not** in the fixed comparison function's \(C^2\)-norm. The torsion commutator and smooth maximum-principle estimates were checked for signs, but their fully quantified universal constants and all underlying elliptic theory are not independently certified here.

**§8.5:** Lemma 8.5.1 correctly obtains all finite \(W^{2,p}\) estimates from a uniform **complex** Hessian bound by local Laplace estimates, without asserting a bounded full real Hessian. Lemma 8.5.2 uses coefficient products of bounded complex Hessians and telescopes **only the closed \(dd^c u\) factors**; smooth, possibly nonclosed \(\theta_a\) factors belong in the test form and their derivatives are not discarded. Lemma 8.5.3 requires the inherited \(m\ge2\) cone condition to get bounded \(K\) from \(S_2\), and establishes a globally defined concave uniformly elliptic tangent-plane extension. Proposition 8.5.4 uses \(L^\infty\) coefficient control and Mazur convexification for the limit cone, rather than concluding pointwise cone closure from arbitrary weak convergence. Viscosity passage uses the extension on all real Hessians. **No false theorem found** in these three entire sections.

## New finding: \(L^1\)-to-mixed-Hessian quantitative continuity

**ID:** \`POME-HESSIAN-L1-MIXED-PRODUCT-STABILITY-001\`. **Severity:** low. **Status:** **verified conditional deduction**, *not a printed source error*. Anchors: §8.5 Lemmas **8.5.1–8.5.2**, paths/tags and physical lines **11–61** above; §8.1 convention. The argument is independent of the user-excluded approximation programme.

Let \(X\) be a compact complex \(n\)-manifold, with a fixed smooth Hermitian metric and volume, and \(1\le k\le n\). For each \(a=1,\ldots,k\), let \(u_j^a\) be smooth real functions with a common bound
\[
\sup_{j,a}\bigl(\|u_j^a\|_{L^\infty(X)}+\|dd^c u_j^a\|_{L^\infty(X)}\bigr)\le H,
\]
and suppose **only** \(u_j^a\to u^a\) in \(L^1(X)\). Then, for every \(0<\beta<1\),
\[
u_j^a\longrightarrow u^a\text{ in } C^{1,\beta}(X);
\]
the limits have bounded distributional complex Hessian, and for arbitrary fixed smooth real \((1,1)\)-forms \(\theta_a\), not necessarily closed, the coefficient-defined mixed currents satisfy
\[
\bigwedge_{a=1}^k(\theta_a+dd^c u_j^a)\ \rightharpoonup\
\bigwedge_{a=1}^k(\theta_a+dd^c u^a).
\]
More precisely, if \(d=2n\), then for each fixed compactly supported smooth complementary-degree test form \(\eta\),
\[
\left|\left\langle\bigwedge_a(\theta_a+dd^cu_j^a)
-\bigwedge_a(\theta_a+dd^cu^a),\eta\right\rangle\right|
\le C_\eta\sum_{a=1}^k\|u_j^a-u^a\|_{L^1}^{1/(d+1)}.
\]
The constants depend on the fixed geometry, \(H\), \(k,\theta_a\) and \(\eta\), **not** on \(j\). This is a safe, not claimed optimal, exponent.

**Full justification:** On nested coordinate balls, \(\Delta u_j^a=4\sum_i(u_j^a)_{i\bar i}\) is uniformly bounded. The interior \(W^{2,p}\) estimates used in Lemma 8.5.1 and finite covers give a uniform \(W^{2,p}\) bound for every finite \(p>1\). For \(p>d\), compact embedding gives uniform \(C^1\) bounds and relative compactness in \(C^{1,\beta}\) after choosing \(p>d/(1-\beta)\). Every convergent subsequence has the prescribed \(L^1\)-limit; hence the **entire sequence** converges in \(C^{1,\beta}\). Weak-star compactness and distributional testing give bounded \(dd^c u^a\).

For completeness, if \(w=u_j^a-u^a\), let \(M=\|w\|_\infty\) and let \(x_0\) realize its absolute maximum. The already established uniform Lipschitz bound gives \(|w|\ge M/2\) on a geodesic ball of radius \(\min(r_0,M/(2L))\). Compact Hermitian geometry gives ball-volume lower bounds \(cr^d\). Since \(M\) is also uniformly bounded, this yields
\[
M\le C\|w\|_{L^1}^{1/(d+1)}
\]
(including the constant-function case \(L=0\)). Apply Lemma 8.5.2 to the **now proved** uniform convergence, telescoping the closed \(dd^c\)-factors while incorporating each smooth \(\theta_a\) into the test form. Its pairing bound is \(C_\eta\sum_a\|u_j^a-u^a\|_\infty\). Substitution gives the displayed \(L^1\) Hölder rate. No false interchange of products under mere weak \(W^{2,p}\) convergence is used.

**Proposed optional addition:** record this \(L^1\)-topology replacement and explicit safe modulus after §8.5.2; it is useful when examining §8.5.4 and approximation/limit arguments elsewhere in the **nonexcluded** complex-Hessian chapter. It does not by itself prove existence, regularity, or simultaneous varying-index convergence for arbitrary bounded Hessian potentials.

## Genuine open proof input

**ID:** \`POME-HESSIAN-EKC-REGULARITY-EXTERNAL-001\`. **Severity:** medium. **Status:** **external dependency** (not a proof gap caused by an incorrect displayed calculation). Anchor: §8.5 around physical **95–121**, after Lemma **8.5.3** permanent \`BAC60298D0F2\`, before Proposition 8.5.4. The reading edition explicitly invokes an interior **Evans–Krylov–Caffarelli \(C^{2,\beta}\)** estimate for globally concave real uniformly elliptic operators with controlled \(x\)-oscillation, including continuous viscosity solutions. The tangent-plane construction checks the operator's hypotheses, but a complete proof of this PDE regularity theorem is **not supplied in §8.5**. The reference is a real mathematical input, not merely historical attribution. **Affected dependents:** the final \(C^{2,\beta}\) and smooth-bootstrapping assertions of §8.5 and regularity uses in §§8.6–8.8. **Proposed action:** retain named attribution and state the exact viscosity/coefficients version of the estimate (or supply an independently checked self-contained proof); **do not** present the Hessian operator's extension alone as a complete regularity proof.

## Ledger boundary and exclusions

This review adds **three current whole direct section readings**, not three newly established historical first visits. It adds **one conditional deduction**, **one explicit external dependency**, **zero complete transitive upstream-chain certificates**, and **zero newly confirmed false printed theorems**. It did not redo §8.2, §8.9 or excluded work; earlier ledger entries, canonical choices, proof substitutions and stable tags are unchanged. Demailly approximation/regularization and its dedicated Bergman, L2, Ohsawa–Takegoshi, multiscale-atlas and positivity-loss programme remain **deferred-by-user, not resolved or certified**. Hironaka is the only declared permitted external exception; the EKC input remains **unresolved** as an audit certification requirement. No tests, builds, GitHub Actions, publication or private source reads were performed.
