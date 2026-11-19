# Optimal quadratic metric jets in holomorphic Kähler normal coordinates

**Date:** 2026-11-19. **Finding ID:** \`POME-KAHLER-METRIC-QUADRATIC-JET-MINIMAX-001\`. **Severity/status:** low / **verified conditional deduction**. This strengthens the interpretation of a correct printed theorem. **No printed false theorem, independent proof gap or fully certified transitive dependency is claimed.**

**Reviewed production main:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`. **Reading-edition path:** \`docs/sections/kahler-normal-coordinate-jets/index.html\`, complete mathematical text and proof at physical HTML **lines 7–77**, blob \`4fd58352bd134c2715fc4cbf1e0074a42a7e0657\`. **Theorem 10.94.2:** source label \`demailly-complex-geometry:07136048\`, permanent **\`64B6971EF741\`**, statement lines 10–29 and proof lines 31–77. **Curvature expansion (10.94.3):** source \`demailly-complex-geometry:159ABCDF\`, permanent **\`F8EFB833957C\`**, lines 15–22. **Curvature symmetries (10.94.4):** source \`demailly-complex-geometry:9390894A\`, permanent **\`89C5EDFA346C\`**, lines 24–27. The cubic coordinate change (10.94.6), permanent **\`9F6B4FD758C3\`**, is at lines 49–62. The earlier Kähler normal-coordinate lemma **\`B12EA9BB1DC1\`** is cited at line 34; its full prior proof chain is **not** newly certified.

## Additional theorem: an exact chart minimax

Let \((X,\omega)\) be a smooth Kähler manifold of complex dimension \(n\ge1\), and fix \(p\in X\). Work with the precise Hermitian convention of §10.94,
\[
\omega=i\sum_{l,m}g_{l\bar m}\,dz_l\wedge d\bar z_m,
\]
and the **unscaled** Chern curvature coefficients \(C_{j\bar k l\bar m}\) in the printed equation (10.94.3). For \(v\in\mathbb C^n\), set
\[
\mathcal R_p(v)_{l\bar m}
=\sum_{j,k}C_{j\bar k l\bar m}(p)v_j\bar v_k,
\qquad
\kappa_p=\max_{\|v\|=1}\|\mathcal R_p(v)\|_{\mathrm{op}}.
\]
Under changes of unitary tangent frame, the entries of \(\mathcal R_p(v)\) change by unitary conjugation and \(v\) changes by a unitary map. Thus \(\kappa_p\ge0\) is well-defined, independent of the particular unitary frame.

Let \(\mathcal N_p\) denote the holomorphic coordinate germs centered at \(p\) and **normalized to first order**, i.e. \(G(0)=I\) and \(dG(0)=0\) for \(G(z)=(g_{l\bar m}(z))\). Such charts exist by printed Theorem 10.94.2. For one such chart \(z\), define its second-order metric distortion
\[
\mathcal D(z)=
\limsup_{r\downarrow0}
\frac{1}{r^2}\sup_{|w|=r}\|G(w)-I\|_{\mathrm{op}}.
\]
Then
\[
\boxed{\min_{z\in\mathcal N_p}\mathcal D(z)=\kappa_p.}\tag{*}
\]
In particular, the following are equivalent at a given point \(p\):

1. \(\kappa_p=0\);
2. the Chern curvature tensor of the Kähler metric vanishes at \(p\);
3. there exist holomorphic coordinates at \(p\) with \(G(z)=I+O(|z|^3)\).

This is **pointwise jet rigidity**, not flatness on any neighborhood and not an assertion about a globally flat metric.

## Proof, including why arbitrary cubic coordinate changes cannot improve the bound

For any \(z\in\mathcal N_p\), first-order normalization gives the second-order real Taylor expansion, uniform for \(w\) in a sufficiently small ball,
\[
G(w)-I
=-\mathcal R_p(w)
+H(w,w)+H(w,w)^*+O(|w|^3),\tag{1}
\]
where \(H(w,w)\) denotes a matrix-valued holomorphic homogeneous quadratic polynomial. Indeed, the mixed coefficient of \(w_j\bar w_k\) is
\(\partial_j\partial_{\bar k}G(0)=-C_{j\bar k l\bar m}(p)\), by the explicit unscaled curvature computation in printed proof lines 70–76; the remaining real second-degree terms have bidegrees \((2,0)\) and \((0,2)\). If the linear frames of two such charts differ, they differ by a unitary transformation, which preserves the supremum and the operator norm.

Fix a unit vector \(v\in\mathbb C^n\), write \(w=re^{i\theta}v\) and average (1) with respect to \(\theta\):
\[
\frac1{2\pi}\int_0^{2\pi}\!\bigl(G(re^{i\theta}v)-I\bigr)\,d\theta
=-r^2\mathcal R_p(v)+O(r^3).\tag{2}
\]
The holomorphic and antiholomorphic quadratic terms carry Fourier frequencies \(2,-2\), so both average to zero. Convexity of the matrix operator norm (or the triangle inequality for the integral) implies
\[
\frac1{r^2}\sup_{|w|=r}\|G(w)-I\|_{\mathrm{op}}
\ge
\left\|-\mathcal R_p(v)+O(r)\right\|_{\mathrm{op}}.
\]
Let \(r\downarrow0\) and then maximize over \(\|v\|=1\). This proves
\(\mathcal D(z)\ge\kappa_p\) in **every** first-order normalized holomorphic chart.

The cubic coordinate construction in the *printed* Theorem 10.94.2 explicitly removes the \((2,0)\) and \((0,2)\) Taylor coefficients, giving its equation (10.94.3):
\[
G(w)-I=-\mathcal R_p(w)+O(|w|^3).
\]
Uniformity of this Taylor remainder on each small Euclidean sphere proves
\(\mathcal D(z)=\max_{\|v\|=1}\|\mathcal R_p(v)\|_{\mathrm{op}}=\kappa_p\).
This proves (*), with an **attained** minimum; no compactness of the space of charts or limiting sequence of coordinate changes is invoked.

If \(\mathcal R_p(v)=0\) for every \(v\), then polarization of the Hermitian sesquilinear form
\((v,w)\mapsto\sum_{j,k}C_{j\bar k l\bar m}v_j\bar w_k\), separately for each \(l,m\), implies all \(C_{j\bar k l\bar m}(p)=0\). Conversely curvature vanishing makes the printed cubic-normal expansion \(G=I+O(|w|^3)\). If some chart had that order-three remainder, its mixed second derivatives would vanish, so the curvature would vanish. This proves the equivalence.

## Sharp model and distinction from earlier audit work

In the standard affine chart about \(0\in\mathbb P^1\), take the Hermitian metric with the Fubini–Study local coefficient
\[
g_{z\bar z}=(1+|z|^2)^{-2}
=1-2|z|^2+O(|z|^4).
\]
This is already first-order normalized and has unscaled Chern curvature \(C_{1\bar1 1\bar1}=2\). Hence \(\kappa_0=2\) and \(\mathcal D(z)=2\): **no** holomorphic coordinate germ preserving \(G(0)=1,dG(0)=0\) can improve the second-order operator-norm coefficient below \(2\). A Euclidean flat chart has \(\kappa_p=\mathcal D=0\). These show the obstruction has the stated exact, not merely qualitative, size.

The earlier finding **\`POME-KAHLER-QUARTIC-POTENTIAL-001\`** calculated the quartic coefficient in a *Kähler potential*. It is preserved as independent existing work, **not** re-logged here. The present quantitative **minimax over all holomorphic chart germs** concerns matrix-valued metric coefficients and an invariant optimal norm; the phase-averaging lower bound is the new argument.

## Direct printed-proof review and classification

- Lines 7–29: checked the metric convention, definition of the unscaled Chern curvature and Kähler symmetry statements.
- Lines 33–43: the first-order normal chart is a clearly cited prior internal dependency. Its existence is assumed from the integrated result, not falsely presented as a wholly new independent proof.
- Lines 43–65: checked symmetry of the pure holomorphic quadratic coefficients and cubic coordinate correction: differentiating \(\frac13\sum B_{jklm}x_jx_kx_l\) produces the required \(\sum B_{jklm}x_jx_k\,dx_l\), with no missing factor.
- Lines 68–77: checked matrix index transposition \(H_{ml}=g_{l\bar m}\) and the sign \(\bar\partial(\bar z_kdz_j)=-dz_j\wedge d\bar z_k\); this yields \(C=-\partial\bar\partial g\) and the stated conjugation and Kähler symmetries.

**Verdict:** No new confirmed printed error, gap or false theorem. The new theorem is a **verified conditional deduction** using the correctly stated normal-coordinate construction; no full transitive proof certification.

**Proposed correction/addition:** Optional *new corollary* after Theorem 10.94.2 stating (*) and pointwise order-three rigidity, retaining all historical attribution and permanent tags. **Affected dependents:** local choice of holomorphic frames for curvature expansions and any later use of order-two jet coefficients; their proofs were not audited here. **Excluded/deferred:** Demailly approximation/regularization and the specifically excluded Bergman, \(L^2\), Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof-completion programmes remain **deferred-by-user**, not resolved or certified. No portion of that programme was reopened.

**Coverage:** +1 full directly read numbered section **§10.94** (mathematical lines 7–77); +0 fully certified upstream chains. Prior first-visit status is unreconciled. No tests, builds, GitHub Actions, automatic site publication or changes to main, mathematical body, registry, canonicalization or tags.
