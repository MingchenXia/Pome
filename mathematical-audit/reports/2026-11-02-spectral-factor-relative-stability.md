# Relative stability of the canonical matrix spectral factor at the disc centre

**Date:** 2026-11-02. **Reviewed production \`main\`:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`. **Classification:** \`POME-CIRCLE-SPECTRAL-FACTOR-RELATIVE-STABILITY-001\`, **low / verified conditional deduction**. This is an additional quantitative consequence of a correct theorem, not a discovered false statement, missing proof, completed global dependency chain, or an applied source repair.

**Integrated reading edition:** \`docs/sections/smooth-positive-matrix-factorization-on-the-circle/index.html\`, Git blob \`04780d065ee474f3bb3255db297ac435e00485a1\`, Theorem **9.23.1**, original source \`klimek-pluripotential-theory:02D391FB\`, permanent tag \`35AF621E1787\`, physical lines **7–69**. In particular, Hardy-space minimization and its normalization occur at lines **18–34**; smoothness, positivity of the constant matrix and the invertible factor \`H=A^{1/2}F^{-1}\` at lines **36–66**, and uniqueness at **68**. For conditional downstream context, compare Lemma **9.24.3**, \`klimek-pluripotential-theory:8C00762F\`, permanent tag \`106A14BC1AFE\`, in \`docs/sections/smooth-green-functions-on-strongly-convex-domains/index.html\`, blob \`e19df8fd1692c138eddd5f2fff8822de588e03ec\`, lines **89–102** (coercive projected inverse). Neither the full stationary-disc theorem nor its entire prior dependency chain is certified here.

## Statement

Let \`m≥2\`, and let \`W_0,W_1:S^1→Herm_m\` be smooth strictly positive symbols. With normalized angular measure \`dm=dθ/(2π)\` and the vector-valued Hardy class \`H²\`, define the *central minimal-energy matrix* \`A(W)\` by

\[
v^* A(W)v=\min_{\substack{f\in H^2(S^1,\mathbb C^m)\\ f(0)=v}}
\int_{S^1} f(\zeta)^*W(\zeta)f(\zeta)\,dm(\zeta).
\tag{1}
\]

Theorem 9.23.1 constructs a unique minimizer for every \`v\`, an analytic invertible \`F_W\` with \`F_W(0)=I\`, and a canonical choice of spectral factor \`H_W=A(W)^{1/2}F_W^{-1}\`, for which \`H_W(0)=A(W)^{1/2}\`.

Suppose for some \`ε≥0\` one has at **every** point of \`S¹\`
\[
e^{-\varepsilon}W_0\preceq W_1\preceq e^{\varepsilon}W_0.
\tag{2}
\]
Then
\[
\boxed{e^{-\varepsilon}A(W_0)\preceq A(W_1)\preceq e^{\varepsilon}A(W_0),}
\quad
|\log\det A(W_1)-\log\det A(W_0)|\le m\varepsilon.
\tag{3}
\]
Equivalently, the canonical central energy matrix is **nonexpansive for the order-based Thompson distance**, where this distance for a pair of positive matrices is the least \`ε\` allowing the two inequalities in (2). The coefficient \`1\` in the order-distance bound and the coefficient \`m\` in the determinant bound are **sharp**, attained when \`W_1=e^\varepsilon W_0\` for \`ε>0\`.

More quantitatively, suppose both symbols have common bounds
\[
cI\preceq W_i(\zeta)\preceq CI,\qquad 0<c\le C,\quad i=0,1,
\]
and let \(\delta=\sup_{\zeta\in S^1}\|W_1(\zeta)-W_0(\zeta)\|_{\mathrm{op}}\). Then
\[
\boxed{\|A(W_1)-A(W_0)\|_{\mathrm{op}}\le (C/c)\delta,\qquad
\|H_{W_1}(0)-H_{W_0}(0)\|_{\mathrm{op}}\le
\frac{C\,\delta}{2c^{3/2}}.}
\tag{4}
\]
The estimates concern the **central normalized factor only**; (4) makes no claim about uniform boundary derivatives or full \`C^s\` stability of the factors.

## Proof and check of all limits

For every admissible \`f\`, (2) yields
\(e^{-\varepsilon}Q_{W_0}(f)\le Q_{W_1}(f)\le e^\varepsilon Q_{W_0}(f)\).
Taking the infimum over the **same nonempty affine Hardy space** \`f(0)=v\` and using (1) gives the quadratic-form inequalities (3) for every \`v\`; no interchange of limits or minimax theorem is involved. Conjugate by \`A(W_0)^{-1/2}\` to see that all \`m\` eigenvalues of the relative matrix lie in \`[e^{-ε},e^ε]\`. Their logarithms sum to the log-determinant difference, proving the second inequality. If \`W_1=e^ε W_0\`, the minimizing functions are unchanged and \`A(W_1)=e^ε A(W_0)\`, giving equality in both bounds.

For (4), let \`f_{i,v}\` denote the minimizer for \`W_i\` with value \`v\`. From \`W_i≥cI\` and the constant competitor \`f≡v\`,
\[
c\|f_{i,v}\|_{L^2}^2\le v^*A(W_i)v
\le \int v^*W_i v\,dm\le C|v|^2.
\tag{5}
\]
Using \`f_{0,v}\` as a competitor in the second minimization,
\[
v^*(A(W_1)-A(W_0))v
\le Q_{W_1}(f_{0,v})-Q_{W_0}(f_{0,v})
\le \delta(C/c)|v|^2.
\]
Interchange indices to obtain the opposite inequality. This proves the first estimate in (4). Also \`cI≤A(W_i)≤CI\` by Parseval and constant competitors. Put \`P=A(W_1)^{1/2}\`, \`Q=A(W_0)^{1/2}\`, and \`X=P-Q\`. The exact Sylvester identity \`PX+XQ=A(W_1)-A(W_0)\` has the solution
\[
X=\int_0^\infty e^{-tP}\big(A(W_1)-A(W_0)\big)e^{-tQ}\,dt,
\]
because the matrix integrand is exponentially norm-integrable and differentiation under this finite-dimensional absolutely convergent integral gives \`PX+XQ=A(W_1)-A(W_0)\`. Spectral positivity gives \(\|e^{-tP}\|,\|e^{-tQ}\|\le e^{-t\sqrt c}\); therefore \(\|X\|\le \|A(W_1)-A(W_0)\|/(2\sqrt c)\), proving the second estimate. The identification \`H_{W_i}(0)=A(W_i)^{1/2}\` is exactly the **normalized factor** constructed in the integrated proof; arbitrary unnormalized spectral factors differ by constant unitary matrices and need not satisfy this last numerical estimate without aligning that gauge.

There is a sharp small-perturbation scalar check even though \`m≥2\`: take \`W_0=cI_m\`, \`W_1=(c+\delta)I_m\`. Then \`A(W_i)=W_i\` and \(\|H_{W_1}(0)-H_{W_0}(0)\|=\delta/(\sqrt{c+\delta}+\sqrt c)\sim\delta/(2\sqrt c)\), consistent with (4) and showing the square-root step cannot generally be linearized with coefficient below \`1/(2√c)\` at a constant symbol.

**Disposition:** No false printed theorem or proof gap was identified. Optional *proposed* corollary after Theorem 9.23.1 stating (3) and (4), without changing the theorem, permanent tag, source attribution, or published reading edition. These central-gauge bounds may be used when comparing positive circle symbols in Riemann–Hilbert and stationary-disc linearizations; they do **not** independently prove the smooth dependence in Proposition 9.24.4. Direct inspection is limited to the indicated Hardy minimization, positivity, gauge normalization, and the contextual projected coercivity statement. The analytic regularity of complete stationary-disc families remains an unverified dependency.

**Coverage and exclusions:** This is **new quantitative proof-level work within previously sampled §9.23**, plus a hypothesis/normalization crosscheck of already-sampled §9.24.3, **not** new first-section coverage or a full-section certification. The actual collection remains 25 chapters, 747 numbered sections, and zero complete mathematics-section certifications. All existing confirmed errors, proof gaps, external dependencies and unresolved records remain unchanged. The dedicated Demailly approximation/regularization, Bergman, weighted L², Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof programme stays **deferred-by-user**, not resolved or reopened. No build, CI, source-body change, formalization, site publication or whole-project test is claimed.
