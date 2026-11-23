# Mathematical audit — arbitrary normal-end weights and determinant-only failure

Date: 2026-11-23. **Reviewed main:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`. **Review branch:** \`review/mathematical-audit\`. This document audits the *integrated reading edition*, not the titles alone. Neither result below refutes a printed theorem, and neither imports any excluded Demailly regularization material.

## Exact reviewed scope and anchors

1. **Complete direct mathematical reading, §10.25**, \`docs/sections/bott-chern-classes-and-singular-loci--normal-length-near-a-divisor/index.html\` (main blob \`326cea8684e76a3b0bdb41bb03c85e893aa47477\`, physical lines **7–236**). Source \`non-kahler-pluripotential-theory:3CD86FAA\`, permanent \`D05A6736BCFF\`, Proposition **10.25.1**, lines 28–101; equation **10.25.2**, source \`38956030\` / permanent \`C974FBD89E14\`, lines 30–33; normal derivative estimate **10.25.3**, permanent \`13887090B60F\`, lines 44–55; Schur inequality **10.25.4**, permanent \`EA79C36F0DB1\`, lines 79–90; Corollary **10.25.5**, source \`8E3E406B\` / permanent \`A12B874B6590\`, lines 106–121; explicit critical/subcritical profiles in Examples **10.25.11** and **10.25.12**, permanent \`36258B2EA152\` (lines 196–216) and \`2D0F50D560BC\` (lines 218–232). Checked matrix normalization, the complex/real derivative factor 4, the absolute-continuity tail argument, the distributional no-atom calculation, and both radial length integrals.
2. **Selected direct §10.24**, \`docs/sections/bott-chern-classes-and-singular-loci--an-incomplete-metric-in-a-big-class/index.html\` (main blob \`883d0dcdbae1b442feb63047138dfad88c7d9058\`). Theorem **10.24.1**, source \`non-kahler-pluripotential-theory\`, permanent \`8A2E8673E914\`, and calculation **10.24.4**, permanent \`8F4A3AEF872F\`: selected initial projective blowup model, measure identity, minimality/energy and the finite-distance argument, approximately physical lines 7–152. **Not** the whole §10.24, which continues to line 628, and not transitive verification of its comparison theorem.
3. **Whole mathematical §9.5 revisited**, \`docs/sections/complex-spaces-and-modifications--analytic-curves-and-finite-maps/index.html\` (blob \`2c725646172203283ac4564bddd46213d9a75cbe\`, lines 7–115), including one-dimensional normalization, avoidance by analytic arcs, finite-fiber/proper-image argument, and pure codimension-one zero sets. This section **already had** a historical complete review, so this is **not** counted as a newly fully covered section or a new finding.
4. **Selected §§9.4 and 9.8**, rather than complete fresh reviews: \`docs/sections/complex-spaces-and-modifications--reduced-spaces-and-normalization/index.html\` (blob \`06439f43d1ce8e83d2529682c9a630bffa3d9c22\`), weakly holomorphic sheaf/conductor and local normalization steps in Lemmas 9.4.2–5, Theorem 9.4.6 and Corollary 9.4.9; \`docs/sections/complex-spaces-and-modifications--connected-fibers-and-resolution-models/index.html\` (blob \`6ad8bec31c3089b7eab91f199f5a1eb355a12c40\`), Theorem 9.8.1, Corollary 9.8.2 and the initial codimension-two argument of Proposition 9.8.3. No historic normalization/conductor or local-fiber findings are repeated.

## POME-SCHUR-ARBITRARY-END-WEIGHT-001

**Severity:** low. **Status:** verified conditional deduction (genuine theorem-level extension of a sufficient condition, *not* a printed error). **Target:** §10.25.1 and equations 10.25.2–4, source/permanent anchors listed above.

**Statement.** Let \(X\) be a compact complex manifold equipped with a smooth Hermitian form \(\omega\), and \(D\subset X\) a nonempty smooth effective divisor. Put \(M=X\setminus D\), \(R=|s_D|\) for a fixed smooth norm of \(\mathcal O_X(D)\), and \(\tau=-\log R^2\), normalized so \(\tau\geq1\). Let \(T\) be any smooth strictly positive real \((1,1)\)-form on \(M\), with **no closedness requirement**. Near \(D\), let \(E_\tau=\ker\partial\tau\), and let \(B_\tau=T|_{E_\tau}\), interpreted with determinant \(1\) if \(\dim_\mathbb C X=1\). Suppose that a positive continuous function \(w:[\tau_0,\infty)\to(0,\infty)\) and a constant \(c>0\) satisfy
\[
\frac{\det_\omega T}{\det_\omega B_\tau}\geq c\,R^{-2}w(\tau)^2
\qquad\text{on }\{\tau>\tau_0\}
\]
and
\[
\boxed{\int_{\tau_0}^\infty w(t)\,dt=\infty.}
\]
Then \((M,g_T)\) is a **complete Riemannian manifold**. The power-weight statement in the printed Proposition 10.25.1 corresponds to \(w(t)=t^{-p/2}\), and this integral diverges exactly when \(p\leq2\). In contrast to merely replacing one exponent by another, the criterion allows arbitrary oscillating positive weights with no monotonicity.

**Proof.** The local divisor coordinate calculation in the printed (10.25.3) gives \( |\partial\tau|_\omega^2\leq C R^{-2}\) on a sufficiently deep end, after increasing \(\tau_0\) if necessary. Write the Hermitian matrix of \(T\) in an \(\omega\)-unitary frame with its first normal vector perpendicular to \(E_\tau\). If \(S\) is the Schur complement of the tangential block, completion of the square yields, for each real tangent vector \(v\),
\[
g_T(v,v)\geq S\frac{|\partial\tau(v)|^2}{|\partial\tau|_\omega^2}
\geq \frac cC w(\tau)^2|\partial\tau(v)|^2
\geq\frac{c}{4C}w(\tau)^2|d\tau(v)|^2.
\]
Define \(\Phi(t)=0\) for \(t\leq\tau_0\) and \(\Phi(t)=\int_{\tau_0}^t w(s)\,ds\) for \(t>\tau_0\). It is locally Lipschitz, and for a.e. parameter on every piecewise smooth curve in \(M\),
\[
|d(\Phi\circ\tau)(v)|\leq 2\sqrt{C/c}\,\sqrt{g_T(v,v)}.
\]
Integrating along paths gives a global length-distance Lipschitz constant \(2\sqrt{C/c}\). Because \(\Phi(t)\to\infty\) and \(\tau(x)\to\infty\) as \(x\to D\), compactness of \(X\) makes \(\Phi\circ\tau\) proper on \(M\). Consequently a \(g_T\)-Cauchy sequence lies in a compact subset of \(M\), has a convergent subsequence in the manifold topology, and converges in the length distance by local comparability of \(g_T\) with a Euclidean metric. This proves completeness without any monotone-weight or analytic regularization input.

**Sharpness in diagonal product geometry.** The integral divergence condition cannot be relaxed uniformly. Let \(E=\mathbb C/(\mathbb Z+i\mathbb Z)\), \(X=E^n\), \(D=\{0\}\times E^{n-1}\), \(\omega_0=\sum_j\pi_j^*\omega_E\), and choose a product norm on \(\mathcal O_X(D)\) with \(R^2=a|z_1|^2\) near \(D\). If \(w\) is positive smooth with \(\int_{\tau_0}^\infty w(t)\,dt<\infty\), put \(b=R^{-2}w(\tau)^2\) near \(D\), extend \(b\) smoothly and positively to \(M\), and set
\[
T_w=b\,\pi_1^*\omega_E+\sum_{j=2}^n\pi_j^*\omega_E .
\]
The tangential block has determinant \(1\), and \(\det_{\omega_0}T_w/\det_{\omega_0}B_\tau=b=R^{-2}w(\tau)^2\) near \(D\). Yet the radial segment \(z_1=r\downarrow0\), with the other coordinates fixed, has length proportional to
\[
\int_0^\varepsilon r^{-1}w(-\log(ar^2))\,dr=\tfrac12\int_{-\log(a\varepsilon^2)}^\infty w(t)\,dt<\infty.
\]
Its points form a Cauchy sequence without limit in \(M\). Thus the **one-variable integral divergence criterion is optimal within this diagonal Hermitian model class**, including complex dimension \(n=1\). No claim of necessity for arbitrary non-diagonal positive forms is made.

**Affected dependents / repair:** Proposition 10.25.1 is already correct. A permissible optional addition after it would state this arbitrary-weight criterion and the diagonal sharpness example. Its proof uses only the Schur complement identity, (10.25.3), compactness and elementary path-length geometry. Corollary 10.25.5 can inherit this extension if its density/potential/tangential bounds yield such a Schur lower bound; the original \(L^1\) and energy claims are not re-proved.

## POME-DETERMINANT-ONLY-HERMITIAN-END-FAIL-001

**Severity:** low. **Status:** verified conditional deduction (explicit countermodel to a **hypothetical weakening**, *not* a false printed theorem). **Target:** the introductory warning before Proposition 10.25.1, §10.25 integrated lines 7–26, and the crucial denominator \(\det_\omega B_\tau\) in (10.25.2).

**Statement and full construction.** On the same \(X=E^2\), \(D=\{0\}\times E\), take \(\omega_0=\pi_1^*\omega_E+\pi_2^*\omega_E\) and a smooth norm with \(\tau=-\log R^2\geq1\). On \(M=X\setminus D\) set
\[
\boxed{T=\pi_1^*\omega_E+e^{\tau^2}\pi_2^*\omega_E.}
\]
It is smooth, positive definite and Hermitian on \(M\). In the background \(\omega_0\)-unitary product frame, \(\det_{\omega_0}T=e^{\tau^2}\). For **every** \(N>0\),
\[
e^{\tau^2}/R^{-N}=\exp(\tau^2-N\tau/2)\longrightarrow\infty
\quad(x\to D);
\]
in particular the determinant alone obeys arbitrarily strong divisorial lower bounds, including \(cR^{-2}\tau^{-p}\) for any fixed \(p\). Nevertheless the radial normal curve \(r\downarrow0\) has the **unmodified finite flat \(\omega_E\)-length**. Its points are Cauchy but have no limit in \(M\); hence \((M,g_T)\) is incomplete.

For the intrinsic tangential hyperplane \(E_\tau=\ker\partial\tau=T^{1,0}E\) near \(D\),
\[
\det_{\omega_0} B_\tau=e^{\tau^2},\qquad
\frac{\det_{\omega_0}T}{\det_{\omega_0}B_\tau}=1.
\]
The volume explosion is entirely absorbed by tangential directions: the **normal Schur complement stays constant**. This shows why the tangential-block denominator in (10.25.2) is indispensable, even against superpolynomial determinant growth. The example is deliberately Hermitian and generally non-closed. **It does not purport to refute** Corollary 10.25.5, which imposes an exponential Monge–Ampère equation, an upper bound on \(\det B_\tau\), and additional potential/data hypotheses.

**Affected dependents / proposed correction:** None require correction. If desired, add this explicit \(E^2\) example as a caution after (10.25.2), preserving the printed theorem, the power-threshold examples 10.25.11–12, and their historical attribution.

## Rechecked or remaining dependencies

- The §10.25 Schur inequality uses only positive Hermitian linear algebra. Its claimed factor \(1/4\) between \(|\partial\tau(v)|^2\) and \(|d\tau(v)|^2\) is correct. The printed \(p=2\) integral threshold is exact; the two displayed sample radial lengths are consistent.
- The printed §10.24.1 blowup model uses the closed identity \(T=\pi^*\omega_2+2[E]\) and a different mechanism of incompleteness. It must **not** be collapsed with the nonclosed tangent-inflation countermodel above.
- Nonexcluded upstream dependencies not fully certified this run: the **complete** comparison/finite-energy chain invoked in §10.24, global singularity-model statements and possible wider algebraic models; in §9.5, the full local-branch and finite-map prerequisites; in §10.25, the product measure and capacity inputs for full-mass profiles. These do not enter the two new elementary geometric proofs.
- The Demailly approximation/regularization, Bergman, \(L^2\), Ohsawa–Takegoshi, multiscale atlas and positivity-loss proof-completion programs are explicitly **deferred-by-user**, neither reopened nor certified.
- **Coverage accounting:** one whole current mathematical section (§10.25) directly read; one partial (§10.24), two selected current complex-space steps (§9.4 and §9.8); one complete current re-reading of already recorded §9.5. Two new conditional deductions, zero confirmed printed errors, zero new complete upstream dependency-chain certifications. No tests, builds, CI, source/registry changes or publication.
