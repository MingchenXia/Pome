# 2026-11-08 — Smooth positive densities with a fixed floor and vanishing subsolution thresholds

**Finding ID:** \`POME-SUBSOL-SMOOTH-FLOOR-L1-COLLAPSE-001\`.
**Status:** **low / verified conditional deduction**, conditional on the specifically cited internal theorems below. **No printed theorem is asserted false and no source proof is certified in full.**
**Reviewed production main:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`.
**Audit branch at initial inspection:** \`review/mathematical-audit\`, head \`3113da724406885e2c18fd3513151d8e70d88525\`.

## Precise reading-edition anchors and internal premises

1. \`docs/sections/equations-with-prescribed-singularities--stability-of-the-subsolution-threshold/index.html\` (main blob \`903ae0ce7173604063a833295dd94e971b18fd72\`): Theorem **15.32.1**, source \`non-kahler-pluripotential-theory:7D3A6CA8\`, permanent \`D988D47D5E0E\`, physical lines **11–29**; its scalar upper semicontinuity \(\limsup b_h(f_j)\leq b_h(f)\) under \(L^1\) convergence. Equation **15.32.2**, source \`:E5730646\`, permanent \`ACC15559958B\`, lines **15–29**. This proof, not the previously audited root-lattice/net clauses 15.32.5/.9, is the new target.
2. \`docs/sections/equations-with-prescribed-singularities--lower-mass-and-solvability-for-all-measures/index.html\` (main blob \`fc7d4f24f72d9b6ec898eedc961b789e65ef3e25\`): Theorem **15.27.3**, source \`non-kahler-pluripotential-theory:59B533D4\`, permanent \`C7AA7377C144\`, lines **76–111**, supplies a *single* \(L^1\) probability density \(f_*\geq m>0\) without positive scaled subsolution when \(v_-(h)=0\). Corollary **15.27.6**, source \`:7F42D506\`, permanent \`05B92E5A4684\`, lines **140–150**, supplies the zero-threshold mixtures \((1-t)g+tf_*\).
3. \`docs/sections/equations-with-prescribed-singularities--subsolutions-for-an-individual-density/index.html\` (main blob \`9262e6b9fd8929cbdd3f75bacbe2a532839d1dbe\`): Theorem **15.28.4**, source \`non-kahler-pluripotential-theory:76378BFC\`, permanent \`CC13A9B1D927\`, lines **69–88**, identifies threshold zero with absence of positive scaled subsolutions; Proposition **15.28.7**, source \`:58DB2491\`, permanent \`69BB1D568698\`, lines **127–139**, gives \(b_h(q)=c_h(q)>0\) for every nonzero smooth nonnegative density and \(b_h(f)\geq v_-(h)/\int f\,dV\).
4. \`docs/sections/continuous-solutions-and-normalization/index.html\` (main blob \`e4a9ece552056fdc387f170362cc1cc5c5fd4091\`): the standing compact Hermitian setup, physical **7–10**; Theorem **14.19.2** (Kołodziej–Nguyen), source \`non-kahler-pluripotential-theory:C8D798C2\`, permanent \`C8D798C2D2F0\`, physical **27–35**, continuous normalized solvability; and Theorem **14.19.19**, source \`:FD57C562\`, permanent \`EA32B8891E2B\`, physical **303–310**, positive uniform lower bound on the \(L^p\)-norm of any normalized bounded-solution density. The named attribution is preserved.

These are **internal premises read in the integrated edition**, not re-proved here. The only additional approximation performed below is elementary smoothing of *scalar \(L^1\) densities* on a compact smooth manifold, **not** any plurisubharmonic, Demailly, Bergman, \(L^2\), Ohsawa–Takegoshi, multiscale-atlas, or positivity-loss procedure.

## New quantitative instability theorem

Let \(X\) be a connected compact complex manifold of dimension \(n\geq1\), \(h\) a smooth Hermitian form, and \(dV\) a smooth positive volume form. Assume \(v_-(h)=0\). Fix **any** smooth strictly positive probability density \(g\), so \(\int_Xg\,dV=1\). For any two prescribed sequences \(\delta_j,\varepsilon_j>0\) tending to zero, there exist smooth strictly positive probability densities \(q_j\) with

\[
\boxed{
 \|q_j-g\|_{L^1(dV)}<\delta_j,\qquad
 q_j\geq\tfrac12 g \ \text{pointwise},\qquad
 0<c_h(q_j)=b_h(q_j)<\varepsilon_j.
} \tag{A}
\]

Thus the normalization scalar, restricted even to **smooth probability densities with the common positive lower bound \(\tfrac12\min_Xg\)**, has no positive \(L^1\)-local lower bound at *any* smooth strictly positive density. The density limit \(g\) itself has \(c_h(g)>0\), so the discontinuity is genuine even with a common positive pointwise floor.

Moreover, for every **fixed** \(p>1\) there exists \(a_p>0\), depending only on \((X,h,dV,p)\), such that

\[
\boxed{\quad c_h(q_j)\,\|q_j\|_{L^p(dV)}\geq a_p,\qquad
 \|q_j\|_{L^p(dV)}\geq a_p/\varepsilon_j\longrightarrow+\infty.\quad} \tag{B}
\]

The same selected sequence works **simultaneously for all fixed** \(p>1\); this does not assert any \(p\)-uniform constant or rate independent of \(p\).

### Proof of (A)

Let \(f_*\) be the nonnegative \(L^1\) probability density in Theorem 15.27.3. By Corollary 15.27.6 and Theorem 15.28.4, for every \(0<t<1\) the probability density

\[
g_t=(1-t)g+t f_*
\]

has \(b_h(g_t)=0\), even though \(g_t\geq(1-t)g\) and
\(\|g_t-g\|_1=t\|f_*-g\|_1\leq2t\). In general \(g_t\) is not smooth: **this is exactly where the published statement alone stops**.

Choose smooth nonnegative probability densities \(f_{*,k}\) with \(f_{*,k}\to f_*\) in \(L^1\). For completeness, cover \(X\) by finitely many coordinate charts, split \(f_*dV\) by a nonnegative smooth partition of unity, approximate each positive finite scalar measure density in its chart by nonnegative convolution with a compactly supported ordinary real mollifier, sum the smooth approximants, and divide by their positive integrals (which tend to one). This preserves nonnegativity and yields the stated \(L^1\) convergence. No plurisubharmonic regularization is involved.

For a fixed \(0<t<1\), put

\[
q_{t,k}=(1-t)g+t f_{*,k}.
\]

Each \(q_{t,k}\) is a **smooth strictly positive probability density**,
\(q_{t,k}\geq(1-t)g\), and
\(\|q_{t,k}-g\|_1=t\|f_{*,k}-g\|_1\leq2t\). As \(k\to\infty\), \(q_{t,k}\to g_t\) in \(L^1\). Theorem 15.32.1 gives
\(\limsup_k b_h(q_{t,k})\leq b_h(g_t)=0\). Nonnegativity of \(b_h\) therefore gives
\(b_h(q_{t,k})\to0\). Since \(q_{t,k}\) is smooth and positive, Proposition 15.28.7 gives \(b_h(q_{t,k})=c_h(q_{t,k})>0\).

For each \(j\), choose \(0<t_j<\min\{1/2,\delta_j/2\}\); then choose \(k_j\) sufficiently large that \(0<c_h(q_{t_j,k_j})<\varepsilon_j\). Set \(q_j=q_{t_j,k_j}\). This proves **every** inequality in (A), without exchanging a limit in \(t\) and a limit in \(k\) or requiring an unproved diagonal compactness theorem.

### Proof of (B)

For each \(j\), let \(u_j\in\mathrm{PSH}(X,h)\cap C(X)\) be a normalized bounded solution of
\((h+dd^c u_j)^n=c_h(q_j)q_j\,dV\), provided by Theorem 14.19.2 and uniqueness of its normalization scalar. For fixed \(p>1\) apply the second inequality of Theorem 14.19.19 to the right-hand-side density \(F_j=c_h(q_j)q_j\). It gives

\[
a_p\leq\|F_j\|_{L^p}=c_h(q_j)\|q_j\|_{L^p}.
\]

Substitute \(c_h(q_j)<\varepsilon_j\), proving (B). This uses no convergence claim for the solutions \(u_j\), whose potentials and Monge–Ampère measures have **not** been audited here.

### Exact conditional converse

If \(v_-(h)>0\), Proposition 15.28.7 instead gives \(b_h(q)\geq v_-(h)\) for **every** probability density \(q\) (and thus \(c_h(q)\geq v_-(h)\) for every smooth one). Combining this with (A), **conditional on all cited inputs**, yields an equivalent scalar criterion:

> \(v_-(h)>0\) if and only if, at one (equivalently every) smooth strictly positive probability density \(g\), the values \(c_h(q)\) on smooth strictly positive probability densities \(q\) have a positive lower bound throughout some \(L^1\) neighborhood of \(g\), even when the neighborhood is restricted by the floor \(q\geq\tfrac12g\).

The direction \(v_-=0\) is the new contribution; the direction \(v_->0\) is the direct published mass bound. The criterion is **not** a claim that the general normalized equation has continuous solution selection in \(L^1\).

## Classification, correction proposal, dependent statements and limits

- **Status/severity:** **low / verified conditional deduction**. Theorems **15.27.3**, **15.32.1**, **15.28.4**, **15.28.7**, **14.19.2** and **14.19.19** remain **unrefuted**, their analytic inputs **not independently certified**. A false theorem must not be inferred from discontinuity in a weaker topology.
- **Proposed future text-only note (not applied to production):** after Theorem 15.32.1, state (A) as a corollary, emphasizing the common strict positive floor and the divergence (B). This clarifies that smooth densities alone do **not** restore \(L^1\)-continuity; no permanent tags or provenance need alteration.
- **Affected dependents:** the scalar-topology interpretation of §§15.27–15.28, §15.32 (especially its \(L^1\)-upper-semicontinuity versus root-norm topology), and quantitative density requirements in §14.19. No conclusion about capacities, convergence of potentials, convergence of Monge–Ampère measures, equations for singular data, or equivalence of solution operators follows.
- **New scope:** first direct proof-level crosscheck of §15.32.1 with the mixture from §15.27.6 and the \(L^p\)-density lower bound of §14.19.19; **all numbered sections were previously partly sampled**, so **zero new first-visited sections and zero whole-section certifications**. Actual current inventory: **25 chapters, 747 numbered sections, zero complete mathematical-section certifications**.
- **Deferred by user:** the Demailly approximation/regularization and dedicated Bergman, weighted-\(L^2\), Ohsawa–Takegoshi, multiscale-atlas, positivity-loss programmes remain **deferred-by-user**, not verified or resolved. This audit did not touch them.
- **Operations:** audit Markdown only; **no** changes to production main, source entries, registries, canonicalization, permanent tags, GitHub Actions CI, website publishing, software build or formal verification.
