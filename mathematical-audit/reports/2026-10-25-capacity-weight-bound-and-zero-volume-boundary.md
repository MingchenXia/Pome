# 2026-10-25 — Capacity-weight sharpness and the zero-volume boundary of model comparison

**Reviewed immutable main:** b6933b772f41b45918f7e25ed1afbbb1fd892272. **Review branch head read before writing:** 0d4c742dbf33e1a714b9426ebbacde9c3a5ff165. **Status:** two low-severity *verified conditional deductions*, neither a false printed theorem nor an allegation of a missing proof. Only specified integrated mathematical statements and proof passages were checked. The full upstream theorem dependencies remain conditional.

## Scope and source anchors

1. **§13.12, quasi-continuity, capacity, and weighted Bedford–Taylor continuity.** Integrated source: docs/sections/non-pluripolar-products--quasi-continuous-functions/index.html, blob **110ec8727eca146a1304cfd43fdbeb4eebf96290**. Definition 13.12.1, source anchor sgpt-9B23E7DB, permanent tag **C96BE5099B6A**, lines 10–15; big-class capacity comparison Theorem 13.12.2, sgpt-731F5229, tag **C5C10F2AB708**, lines 19–26; zero-capacity characterization Theorem 13.12.4, sgpt-BE8E66B3, tag **9F9E57CC1422**, lines 43–55; convergence-in-capacity Definition 13.12.6, sgpt-ECF23FD9, tag **F7490AE48EAC**, lines 68–74; monotone-net Proposition 13.12.7, sgpt-606EEC85, tag **D56D6D4A5E94**, lines 77–98; weighted convergence Theorem 13.12.8, sgpt-B4CE255F, tag **272876B00528**, lines 100–111.
2. **§13.27, the positive-volume model metrization.** Integrated source: docs/sections/volumes-under-bounded-mass--a-complete-metric-on-positive-volume-models/index.html, blob **bf369ddac8a96939938efeca55db76faae3109c8**. Example 13.27.1, source non-kahler-pluripotential-theory-AFF10A6E, tag **A1CA1768E392**, lines 10–63; Proposition 13.27.2, source non-kahler-pluripotential-theory-17A47BEB, tag **44E1935166EC**, lines 76–103; Theorem 13.27.4, source non-kahler-pluripotential-theory-B2475A61, tag **126E2D85CA62**, lines 107–181; Corollary 13.27.9, source non-kahler-pluripotential-theory-FE60915F, tag **5AF48DFCEE5A**, lines 185–193. Context prerequisite: Proposition 18.4.8, docs/sections/multiplier-ideal-envelopes-and-goodness--ideal-projection/index.html, blob **f1979b73c857f4874dd4a5cb10b93bcc047ebbdc**, lines 133–138, states that the ordinary projection of an analytic singularity is equivalent to it.

## POME-CAP-WEIGHT-UNIFORM-BOUND-SHARP-001

**Status:** verified conditional deduction. **Severity:** low. **Not a false theorem.** The uniform bound on the weights in Theorem 13.12.8 is essential, even for a fixed smooth Kähler factor and smooth nonnegative quasi-continuous weights.

Take \(X=\mathbb P^1\), \(\theta=\omega_{\mathrm{FS}}\) with \(\int_X\omega_{\mathrm{FS}}=1\), and a point \(o=[0:1]\). Choose \(r_j\downarrow0\), a smooth nonnegative \(\chi_j\) supported in the affine disk \(D(o,r_j)\), and normalize
\[
\int_X \chi_j\,\omega_{\mathrm{FS}}=1.
\]
Then \(\chi_j\,\omega_{\mathrm{FS}}\rightharpoonup\delta_o\) weakly: for any continuous test function \(h\), its integral differs from \(h(o)\) by at most the oscillation of \(h\) on \(D(o,r_j)\).

Nevertheless \(\chi_j\to0\) in \(\operatorname{Cap}_{\omega_{\mathrm{FS}}}\). Here is a direct uniform small-disk bound. As the minimal envelope is \(V_{\omega_{\mathrm{FS}}}=0\), every capacity competitor \(v\) satisfies \(-1\le v\le0\). In the fixed affine coordinate centered at \(o\), put \(s_v=v+\log(1+|z|^2)\). This is bounded subharmonic on a fixed disk \(D_R\), with uniform bounds independent of \(v\), and \(dd^c s_v=\omega_{\mathrm{FS}}+dd^c v=:\mu_v\). The circle-mean/Riesz–Jensen formula and monotonicity of \(t\mapsto\mu_v(D_t)\) imply
\[
\mu_v(D_r)\log(R/r)\le C_R
\quad(0<r<R/2).
\]
The harmless normalization factor in the circle-mean identity is absorbed into \(C_R\). Taking the supremum over \(v\) yields
\[
\operatorname{Cap}_{\omega_{\mathrm{FS}}}(D(o,r))
\le \frac{C_R}{\log(R/r)}\longrightarrow0.
\]
For every fixed \(\delta>0\), the set \(\{\chi_j>\delta\}\) is contained in \(D(o,r_j)\); the other order-exceptional set for the limit zero is empty. Therefore the weights converge in the precise two-inequality sense of Definition 13.12.6, yet their weighted smooth measures converge to \(\delta_o\ne0\), not to the predicted zero measure.

To instantiate the remaining factors of the weighted theorem, take \(p=1\), \(\theta_1=\omega_{\mathrm{FS}}\), and \(\varphi_1^j=\varphi_1=0\). These are uniformly bounded and trivially converge in capacity. All hypotheses of Theorem 13.12.8 except the **uniform bound on \(\chi_j\)** hold. Its stated hypothesis is therefore genuinely necessary; do **not** weaken it in canonicalization or a future consolidation with other weighted-continuity results.

**Suggested action:** optional counterexample remark immediately after 13.12.8; keep the theorem's existing uniform-bound hypothesis. **Affected dependents:** weighted Bedford–Taylor continuity, varying densities, and weak convergence of weighted currents. No extra regularization programme or external \(L^2\) result is invoked.

## POME-MODEL-ZERO-VOLUME-BOUNDARY-001

**Status:** verified conditional deduction. **Severity:** low. **Not a counterexample to Theorem 13.27.4.** In contrast, this example shows why the reciprocal lower-volume condition in that complete metric is indispensable.

Again let \(X=\mathbb P^1\), \(\theta=\omega_{\mathrm{FS}}\), and \(D=\{Z_0=0\}\). For rational \(0\le a<1\) set
\[
u_a=a\log\frac{|Z_0|^2}{|Z_0|^2+|Z_1|^2},
\qquad
p_a=P_\theta[u_a].
\]
With \(dd^c=\frac{i}{2\pi}\partial\bar\partial\), Poincaré–Lelong gives
\[
\theta+dd^c u_a=(1-a)\theta+a[D].
\]
Thus the non-pluripolar product discards the polar atom and has mass \(1-a\). More generally, every \(\theta\)-psh potential equivalent to \(u_a\) has exactly the same Lelong coefficient \(a\) at \(D\), no other polar loci, and curvature current of total cohomological mass \(1\). Hence its one-dimensional non-pluripolar mass is \(1-a\), proving that the *upper and lower singularity volumes* both equal \(1-a\). Proposition 18.4.8 makes \(p_a\) an analytic ordinary model of the same singularity type, so
\[
\boxed{L(p_a)=U(p_a)=1-a>0.}
\]

For \(a\le b\), the singularity constraint for \(u_b\) is stronger than that for \(u_a\). The ordinary-envelope competitor families are nested, hence \(p_b\le p_a\) and \(\max(p_a,p_b)=p_a\). The definition \(d_\theta(p,q)=2U(\max(p,q))-U(p)-U(q)\) therefore gives the **exact isometric pole-coefficient identity**
\[
\boxed{d_\theta(p_a,p_b)=|a-b|.}
\]
The rational one-pole models are thus an isometric rational subset of \([0,1)\) for the nonmetric volume comparison.

Take \(a_j=1-1/j\), \(j\ge2\). The positive-volume models \(p_{a_j}\) are \(d_\theta\)-Cauchy because \(d_\theta(p_{a_j},p_{a_k})=|1/j-1/k|\), while \(L(p_{a_j})=1/j\to0\). They **cannot** converge for \(d_\theta\) to any point of \(\mathcal M_+(\theta)\): Proposition 13.27.2 says convergence to a positive-volume model forces convergence of lower volumes to a strictly positive number. Equivalently, \(1/L(p_{a_j})=j\) is not Cauchy. This verifies on an explicit analytic family the nontrivial need for the reciprocal-mass term in Theorem 13.27.4.

**Suggested action:** optional one-pole example following Example 13.27.1 or Theorem 13.27.4; preserve the theorem's reciprocal-volume Cauchy criterion. **Affected dependents:** positive-volume model topologies, varying background comparisons, analytic ideal-model completion. This says nothing about zero-volume models belonging to \(\mathcal M_+\): they do not.

## Additional direct proof inspection and limitations

- In **13.12.7**, checked the decreasing *directed-net* argument: after removal of a capacity-small open set where the limit is continuous and finite, the closed upper-deviation sets form a decreasing directed family with empty intersection. Compactness plus the finite intersection property forces eventual emptiness; no countable cofinal subnet is assumed. For increasing nets, the countable Choquet *selection* is dominated by selected indices in the original directed set and is used only to control its entire tail, not assumed cofinal.
- In **13.12.8**, checked that the proof passes to local bounded Bedford–Taylor coordinates and expands a bounded product against fixed smooth forms. The counterexample above checks a necessary hypothesis only; it does **not** independently certify all weighted-continuity/Choquet-capacitability inputs.
- In **13.27.1–4**, checked the displayed \(\mathbb P^2\) volumes and discrepancy \(2a^2>0\) for failure of the triangle inequality, the lower-volume modulus, and the three-entourage chain-metrization mechanism. In particular the chain argument applies triple relation composition with a reciprocal-mass cutoff; it is not a proof that the original \(d_\theta\) is a metric. The explicit \(\mathbb P^1\) family supplies a separate zero-volume escape obstruction.
- Proposition **18.4.8** was checked for the exact analytic-envelope singularity-type assertion **as a dependency only**. We did not audit its complete proof, any Demailly regularization, Bergman kernel, \(L^2\), Ohsawa–Takegoshi, multiscale atlas, or positivity-loss arguments.
- **Not performed:** complete chapter/section certification, all dependencies, project build, CI, website publication, formal verification, permanent-tag edits, source/registry changes, or mathematical assertions about unretrieved pages.

**Coverage update:** only selected proof passages of previously inventory-only §§13.12 and 13.27 were newly read at proof level. The actual 25-chapter/747-section ToC matrix stays an inventory, not a verification count. Historical dedicated approximation work remains **deferred-by-user** (not resolved/certified).
