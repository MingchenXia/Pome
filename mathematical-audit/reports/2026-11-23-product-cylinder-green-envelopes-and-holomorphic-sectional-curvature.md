# 2026-11-23: Green envelopes on product cylinders, CLN collar constants, Gauduchon trace and Chern sectional curvature

**Reviewed current main:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`. **Review-branch starting head:** \`52242fc6c94a6b0e5e62024a147417887f9c6577\`. This is a mathematical reading of the **integrated HTML edition**, with precise physical line and blob anchors, not a certification of all historical proofs. Existing 747-section TOC matrix is retained without treating older "LEGACY-UNRECONCILED" rows as genuinely never visited.

**Scope:** Full direct reading of current §§7.27, 7.32, 11.28, and a **full repeat** of §11.5 (its previous 2026-11-19 full review and sharp trace-deficit deduction remain credited to that older report). Only three sections are newly recorded as current full reviews here; none has a complete transitive upstream proof certificate. The user-excluded Demailly approximation/regularization and Bergman/L²/Ohsawa–Takegoshi/multiscale-atlas/positivity-loss proof-completion programme is **deferred-by-user**, neither reopened nor certified. Any referenced smoothing in §7.32 is logged as a dependency and not audited as a new programme.

## POME-GREEN-PRODUCT-CYLINDER-REDUCTION-001

**Classification:** low / **verified conditional deduction**, not an error in any printed theorem. The conclusion follows directly from the stated bounded-domain and unbounded-domain envelope definitions and the Liouville theorem for nonpositive plurisubharmonic functions on Euclidean space. Its dependencies are restricted to those explicit definitions/Liouville; this is **not** a claim that all of §§7.19 or 7.27 have independently certified upstream chains.

**Anchors:** §7.27 Proposition 7.27.1 (source \`klimek-pluripotential-theory:71A15571\`, permanent \`A2711B944A6D\`, physical lines 11–24), Proposition 7.27.2 (source \`klimek-pluripotential-theory:DC0D60AB\`, permanent \`28AAE4E86F18\`, lines 29–52), and Example 7.27.3 (source \`klimek-pluripotential-theory:E575F65F\`, permanent \`7F276A63690B\`, lines 57–72), file \`docs/sections/symmetric-green-envelopes-on-unbounded-domains/index.html\`, blob \`76c965efd42eb17ffa9c34c8b7b0408d56a9e2ce\`. The original bounded symmetric-envelope definition is at \`docs/sections/symmetric-envelopes-and-finite-collections-of-poles/index.html\`, lines 35–46, Proposition 7.19.3 (source \`klimek-pluripotential-theory:5793A4E7\`, permanent \`557F24B2F2DD\`, blob \`8e33a409fa4a7c6eea29ab48727741ed9b1e167d\`).

**Statement and exact hypotheses.** Let \(\Omega\subset\mathbb C^m\) be **any bounded domain**, and \(k\ge1\). On the unbounded product domain \(D=\mathbb C^k\times\Omega\subset\mathbb C^{k+m}\), with all Green functions and \(W\)-envelopes using the respective ambient Euclidean norms and the extended minus-infinity convention, one has for \(z,a\in\mathbb C^k\) and \(w,b\in\Omega\)
\[
 \boxed{g_D((z,w),(a,b))=g_\Omega(w,b),\qquad
 W_D((z,w),(a,b))=W_\Omega(w,b).}
\]
In particular, \(g_D\) is symmetric exactly when \(g_\Omega\) is symmetric; equivalently \(W_D=g_D\) exactly when \(W_\Omega=g_\Omega\). No isolated-pole or total-mass assertion is claimed.

**Proof, Green function.** A nonpositive PSH function \(u\) on \(D\), including the allowed identically-minus-infinity fibers, is constant along each entire affine \(\mathbb C^k\) fiber: fix \(w\); the restriction \(z\mapsto u(z,w)\) is nonpositive PSH on \(\mathbb C^k\), hence constant or \(-\infty\) by Liouville. Therefore \(u(z,w)=v(w)\) with \(v(w)=u(0,w)\in\mathrm{PSH}(\Omega)\), or identically \(-\infty\). If \(u\) is a pole competitor at \((a,b)\), the restriction \(u(a,w)=v(w)\) has the requisite upper logarithmic pole inequality at \(b\), so \(v\) is a competitor for \(g_\Omega(\,\cdot\,,b)\); thus \(g_D\le g_\Omega\circ\mathrm{pr}_\Omega\). Conversely, any negative PSH pole competitor \(v\) on \(\Omega\) pulls back to a negative PSH function on \(D\), and
\[
 v(w)\le\log|w-b|+O(1)
 \le\log\sqrt{|z-a|^2+|w-b|^2}+O(1)
\]
near \((a,b)\). It is an admissible \(D\)-competitor, proving the reverse inequality. No regularization, capacity limit or exchange of infima is used.

**Proof, symmetric envelope.** Write \(d_\Omega(w)=\mathrm{dist}(w,\mathbb C^m\setminus\Omega)\). Elementary product geometry gives
\[
 d_D(z,w)=d_\Omega(w),\quad
 H_\Omega(w,b)=\log|w-b|-\log\max\{d_\Omega(w),d_\Omega(b)\}
 \le H_D((z,w),(a,b)).
\]
For an admissible kernel \(F\le0\) in the definition of \(W_D\), its **separate** PSH property and Liouville imply it is independent of both fiber variables \(z,a\); write \(F((z,w),(a,b))=f(w,b)\). The reduced \(f\) is separately PSH. As \(F\) is jointly SH and independent of \(z,a\), its distributional full Laplacian is exactly the lifted Laplacian in \(w,b\); hence \(f\) is jointly SH (or identically \(-\infty\)). Evaluating the \(D\)-constraint at the equal fiber coordinates \(z=a\) yields \(f(w,b)\le H_\Omega(w,b)\). Therefore \(f\) is an admissible \(\Omega\)-kernel, so \(W_D\le W_\Omega\circ(\mathrm{pr}_\Omega,\mathrm{pr}_\Omega)\). Conversely an admissible \(f\) for \(W_\Omega\), pulled back along the two projections, remains jointly SH, separately PSH and nonpositive, and obeys \(f\le H_\Omega\le H_D\). This proves \(W_D\ge W_\Omega\), including the empty/extended cases. Symmetry equivalences follow from the exact identities.

**Explicit case and scope warning.** For \(\Omega=\Delta\subset\mathbb C\),
\[
 W_D((z,w),(a,b))=g_D((z,w),(a,b))
 =\log\left|\frac{w-b}{1-\bar b w}\right|.
\]
For any fixed pole \((a,b)\), the minus-infinity locus is \(\mathbb C^k\times\{b\}\), not a point. A bounded-domain classical \(2^{-(k+1)}\) isolated-atom formula cannot be inferred. This gives an all-\(k\) exact product-cylinder model and complements (does **not** repeat) the strongly pseudoconvex, non-product domain in Example 7.27.3.

**Affected dependents and proposed change:** This is an optional additional example/remark after §7.27.3; it clarifies the limits of transferring §7.19.3's isolated-pole mass argument to unbounded products. The present §7.27 claims are **not contradicted**. Any source/body insert should be a separate reviewable patch, not an audit-branch modification.

## Independent checks and remaining qualifications

### §7.27 — whole direct

The exhaustion argument in Proposition 7.27.1 (physical lines 16–24) uses domain monotonicity and the negative-envelope exhaustion theorem without treating a decreasing **net** as a sequence; only the bounded-domain **domain exhaustion** here is countable. In Proposition 7.27.2 (lines 34–52), the separately PSH/SH envelope's upper regularization, the joint-Laplacian argument when \(g_D\) is symmetric, and the distance bound \(\log|z-w|-\log\max\{d(z),d(w)\}\) were checked with the possibility of identically-minus-infinity slices retained. Example 7.27.3 (57–72): the Levi determinant of \(q=|w|^2(1+|z|^2)\) is \(|w|^2>0\) near the boundary; the whole \(\{w=0\}\) line forces every negative-pole competitor to be \(-\infty\) there. No new confirmed printed error. Upstream bounded-domain envelope/Green comparison and canonical USC envelope theorems remain un-certified transitively.

### §7.32 — whole direct, one corollary plus explanatory argument

\`docs/sections/quantitative-chern-levine-nirenberg-bounds/index.html\`, blob \`efb37e29f386268fefb8c17bfd31ab2ef123dc4d\`, Corollary 7.32.2, source \`demailly-complex-geometry:07A49BA9\`, permanent \`EAB247B80433\`, lines **7–45**; scope paragraph **49**. Checking *only the nonexcluded algebra and current integrations*: with \(N=2M+3\eta\) and \(A=4N/\delta\), the displayed inner estimate at lines 38–44 becomes \((3+8B/\delta)M\,m_T\) after \(j\to\infty,\eta\downarrow0\). Including boundary measure adds at most \(M m_T\), giving \((4+8B/\delta)M\,m_T\le(4\delta_0+8B)M\,m_T/\delta\) because \(0<\delta\le\delta_0\). The constant and inequality direction are consistent. The common-collar identities invoke §7.29.1, and smooth decreasing majorants invoke §7.31.1: these are **explicit un-certified dependencies**; the excluded approximation programme was not re-examined. The location of the "preceding geometric hypotheses" should be preserved/clarified in any future editorial rewrite, not classified as a false theorem.

### §11.5 — full repeat, not new full-coverage credit

\`docs/sections/gauduchon-metrics-and-linear-mass--conservation-of-the-trace-mass/index.html\`, blob \`34af83ff391b5e5590cd9cb10ca4cd2b3faff02c\`, mathematical lines **7–76**. Proposition 11.5.1 (source \`non-kahler-pluripotential-theory:0D4A42C8\`, permanent \`828FAD1A35BF\`, lines 11–28) uses distributional integration by parts against \(dd^c(\gamma^{n-1})=0\), including the polar-set current mass, not the non-pluripolar product. Corollary 11.5.3 (permanent \`A9609E0AE7B9\`, lines 36–46) compares the positive \((n-1,n-1)\) forms with uniform constants. Proposition 11.5.4 (permanent \`BFC1330527CA\`, lines 57–76) has the required \(1/n\) in the trace/AM–GM normalization. An earlier 2026-11-19 complete direct review and **sharp trace deficit** deduction already exist: neither is repeated as a new finding or first visit.

### §11.28 — whole direct

\`docs/sections/gauduchon-metrics-and-linear-mass--holomorphic-sectional-curvature/index.html\`, blob \`06c98914b1a3e3d43b546a52213b043ec03b4d24\`, mathematical lines **7–189**. Lemma 11.28.2 (source \`non-kahler-pluripotential-theory:4B4CC53A\`, permanent \`8D640C26806F\`, lines 39–56): the complex Gaussian fourth moment is the sum of the two pairings, giving \(Q+B\), and the h-norm fourth moment equals \(u^2+q\). Proposition 11.28.3 (source \`non-kahler-pluripotential-theory:6FA99DEC\`, permanent \`37B317ABBC08\`, lines 73–122): checked the \(2(Q-B)=|T|^2-D_g\) contraction, the factor \(1/4\) in the \(|T|^2\) cancellation and the Stokes removal of \(D_g\), which requires the **reference metric g to be Kähler**. Corollary 11.28.5 (source \`non-kahler-pluripotential-theory:3BE7346A\`, permanent \`550E97762605\`, lines 127–136) uses \(\mathrm{Ric}(g)\ge0\) and \(H_h\le0\) to make all three integrated terms nonnegative. Proposition 11.28.7 (source \`non-kahler-pluripotential-theory:DEA2B6B5\`, permanent \`19F2C00A6056\`, lines 148–177): its torus argument uses the *periodic* integration identity at lines 160–171 to force \(\partial h=0\), and treats \(m=1\) separately. Corollary 11.28.8 (source \`non-kahler-pluripotential-theory:0BFF310F\`, permanent \`7AE0B102B55A\`, lines 182–189) uses a finite unramified cover only to descend closedness/flat curvature, not to infer existence on a disconnected base. The \(\mathrm{Ric}(g)\) sign and Chern curvature convention remain consistent in these checked steps. No new confirmed error; the full differential-geometric background of the antisymmetrization is not independently certified in its entire upstream chain.

## Audit delta and follow-up scope

**+3 newly recorded whole current direct sections** (§§7.27, 7.32, 11.28), **+1 whole repeat** (§11.5), **+1 low verified conditional deduction**, **+0 newly confirmed printed errors**, **+0 fully transitive proof-chain certifications**; historical first visits are unresolved. Remain to review nonexcluded §§7.28–7.31 dependencies separately, more sections in the 747-section actual TOC, and the §11.28 curvature antecedents. No build, test, CI, publication, main/source/registry/tag changes.
