# 2026-10-27 — Compact-obstacle nonexpansiveness, the essential joint Kiselman hypothesis, and curvature integrality

**Reviewed current main:** <code>b6933b772f41b45918f7e25ed1afbbb1fd892272</code>. **Starting audit head:** <code>e7c35a7de7fc45dca138d53838f3c33e1140e2f2</code>. **Scope:** fresh first selected proof-level reading of §§5.40, 5.41, 5.45; contextual internal dependency check of §5.12.2 only. All author-excluded Demailly approximation/regularization, dedicated Bergman, L², Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof completion remains **deferred-by-user**, not reviewed, resolved or certified.

## Pinned integrated sources

| Target | Precise public main source; immutable file blob SHA | Permanent Pome tag; physical lines |
| --- | --- | --- |
| Compact obstacle envelopes | <code>docs/sections/plurisubharmonic-functions-and-singularities--obstacle-envelopes/index.html</code>; <code>30716faee83d2ac0ec84b3684e319210980bd14f</code> | §5.40.1 <code>294BB4EEA84F</code>, lines 44–78; §5.40.3 <code>630365A8F8B8</code>, lines 97–116; §5.40.5 <code>44FD5A853A0A</code>, lines 142–165; §5.40.6 <code>F031A16FF76F</code>, lines 169–199; §5.40.10 <code>B986B6AE211B</code>, lines 250–283; §5.40.12 <code>1709375DAB71</code>, lines 293–320. |
| Minimum principle and Legendre duality | <code>docs/sections/plurisubharmonic-functions-and-singularities--the-minimum-principle/index.html</code>; <code>3a96ad51514a61efa6802d09305f90a4c9cbef2d</code> | §5.41.1 <code>ADD743D2224C</code>, lines 11–24; §5.41.3 <code>ED1DA0551379</code>, lines 35–62; §5.41.5 <code>742009E66DA3</code>, lines 74–103; §5.41.8 <code>FAE98D3A3F69</code>, lines 122–134; §5.41.9 <code>5EA08D4F62B2</code>, lines 137–158. |
| Existing *internal* Kiselman lemma | <code>docs/sections/plurisubharmonic-functions--kiselman-s-minimum-principle/index.html</code>; <code>e26179ee7cbb45fe10f7b4aabb9057ca33739a87</code> | Theorem 5.12.1 <code>1F87EF4FCF69</code>, lines 20–98; Corollary 5.12.2 <code>2C1A82803889</code>, lines 100–129. |
| Closed metric curvature | <code>docs/sections/plurisubharmonic-functions-and-singularities--curvature-of-line-bundles/index.html</code>; <code>28b44ce67341b26ec1d01db0feaa83adbb6b357a</code> | §5.45.1 <code>620B099907AB</code>, lines 9–31. |

Reader source tags above are stable provenance anchors. The **original source entry labels** were not independently reconstructed from the published section HTML in this run; no fabricated source-label or source-number mapping is asserted. All mathematical comparisons are to these integrated statements and their existing proofs.

## POME-KISELMAN-JOINT-PSH-ESSENTIAL-001
**Severity:** low. **Status:** verified conditional deduction / sharpness counterexample; printed Proposition 5.41.3 is **not false**.

**Precise claim.** In Proposition 5.41.3 one cannot replace the hypothesis that the complexified function on \(X\times S_I\) satisfies \(\pi^*\theta+dd^cU\ge0\) by the conjunction of (i) each \(u_t\in\mathrm{PSH}(X,\theta)\), (ii) pointwise finite strict convexity of \(t\mapsto u_t(x)\), and (iii) a bounded parameter interval, even if \(X\) is a compact Kähler curve and every \(u_t\) is smooth and uniformly strictly \(\theta\)-psh.

**Counterexample with full calculation.** On \(X=\mathbb P^1\), take the normalized Fubini–Study form
\[
\theta=\omega_{\mathrm{FS}}=dd^c\log(1+|z|^2),\qquad dd^c=\frac{i}{2\pi}\partial\bar\partial
\]
in the affine chart \(z=Z_1/Z_0\). Set \(h([Z_0:Z_1])=2\operatorname{Re}(Z_1\overline{Z_0})/(|Z_0|^2+|Z_1|^2)\). This is a smooth global real function, and \(h(z)=z+\bar z+O(|z|^2)\) at \(z=0\). Choose \(C>0\) with \(-C\omega_{\mathrm{FS}}\le dd^ch\le C\omega_{\mathrm{FS}}\), then \(a>0\) with \(aC<1/2\). On \(I=(-1,1)\), define
\[
u_t(x)=a\,t\,h(x)+\frac{a^2}{4}t^2.
\]
For all \(|t|<1\), \(\theta+dd^cu_t=\omega_{\mathrm{FS}}+a t\,dd^ch\ge(1-aC)\omega_{\mathrm{FS}}>\omega_{\mathrm{FS}}/2\). For every \(x\), the dependence on \(t\) is strictly convex and finite. However, on the open neighborhood \(|h(x)|<a/2\), its minimizing parameter \(t_*=-2h(x)/a\) belongs to \(I\), so
\[
q(x)=\inf_{-1<t<1}u_t(x)=-h(x)^2.
\]
At \(z=0\), \(\partial_z\partial_{\bar z}(h^2)=2|\partial_zh|^2=2\), whereas \(\partial_z\partial_{\bar z}\log(1+|z|^2)=1\). Consequently \(\theta+dd^cq=-(i/2\pi)\,dz\wedge d\bar z\) at this point: **\(q\notin\mathrm{PSH}(X,\theta)\)** despite all separate conditions.

The omitted joint condition really fails: if \(U(z,w)=u_{\operatorname{Re}w}(z)\), then at \((z,w)=(0,0)\) the coefficient matrix of \(\pi^*\theta+dd^cU\), after dropping the common positive \(i/(2\pi)\), is
\[
\begin{pmatrix}1&a/2\\a/2&a^2/8\end{pmatrix},
\qquad\det=-a^2/8<0.
\]
This is precisely the Schur-complement obstruction. **Proposed correction:** keep the joint psh hypothesis; optionally place this compact sharpness example after Proposition 5.41.3. **Affected dependents:** minimum-principle applications in §5.41, pointwise Legendre inversion and §17 test curves; no theorem needs alteration under its printed assumptions.

## POME-KISELMAN-INTERNAL-COROLLARY-REFERENCE-001
**Severity:** low. **Status:** verified repair of an unnecessary external proof-reference *at this application*, conditional on the established internal corollary; not certification of every proof supporting that corollary.

Proposition 5.41.3 lines 39–43 names a classical local Kiselman result from SGPT. But existing Pome **Corollary 5.12.2**, permanent tag <code>2C1A82803889</code>, gives exactly the local principle needed: for a psh function on a ball \(D\) times a translation-invariant strip \(I+i\mathbb R\), the infimum over \(I\) is psh or identically \(-\infty\), and affine parameter shifts are allowed. In the proof of 5.41.3, after choosing \(r\) with \(dd^cr=\beta+\eta\kappa\), the function \(U+r\circ\pi\) fits these hypotheses on the local coordinate ball. Apply Corollary 5.12.2, obtain \(q+r\) psh or \(-\infty\), and keep the printed \(-\theta-2\eta\kappa\) bound, \(\eta\downarrow0\), and connectedness argument unchanged. **Proposed source/body patch, not applied here:** replace the proof-input citation at 5.41.3 by internal §5.12.2; preserve the SGPT/Kiselman historical attribution in the appropriate history/bibliography. Neither a new external theorem nor a review of the author-excluded Demailly programme is required. **Affected dependent:** the 5.41.3 branch used in §5.41.9 and subsequent test-curve constructions.

## POME-COMPACT-OBSTACLE-SUPNORM-STABILITY-001
**Severity:** low. **Status:** verified conditional deduction; strengthens a different obstacle class from Proposition 5.40.3 and assumes the *printed* Proposition 5.40.6.

Let \(X\) be compact, \(\theta\) a **big** smooth real (1,1)-form (not assumed closed), and \(K\subset X\) compact non-pluripolar. For any two **bounded, not necessarily measurable or continuous**, real obstacles \(\psi,\phi\) on \(K\), let
\[
E_K(\psi)=\left(\sup\{u\in\mathrm{PSH}(X,\theta):u\le\psi\text{ pointwise on }K\}\right)^*.
\]
Proposition 5.40.6 guarantees each envelope is \(\theta\)-psh with minimal singularities. Put \(\delta=\sup_K|\psi-\phi|<\infty\). For every competitor \(u\le\psi\), \(u-\delta\le\phi\) is a competitor for \(E_K(\phi)\), so \(u\le E_K(\phi)+\delta\). Supremum and upper-semicontinuous regularization preserve this inequality (the right side is already upper semicontinuous), giving \(E_K(\psi)\le E_K(\phi)+\delta\); interchange \(\psi,\phi\) for the opposite bound. Thus the **extended-valued** inequalities
\[
E_K(\phi)-\delta\le E_K(\psi)\le E_K(\phi)+\delta
\]
hold on all of \(X\), and the ordinary sup-norm bound \(\|E_K(\psi)-E_K(\phi)\|_\infty\le\delta\) holds on their **common finite locus**; no \(-\infty-(-\infty)\) is formed. The Lipschitz coefficient 1 is sharp: \(X=K=\mathbb P^1,\theta=\omega_{\rm FS}\), with constant obstacles \(0\) and \(\delta>0\), have envelopes exactly \(0,\delta\). The same argument works for q.e. compact obstacle envelopes by the equality asserted in 5.40.6. **Proposed:** short nonexpansiveness corollary after §5.40.6, retaining the big and non-pluripolar compact hypotheses; do not claim continuity from the author-deferred §5.32.1 approximation path. **Affected dependents:** compact-obstacle and rooftop stability comparisons in §16 and §18 where this exact competitor class occurs.

## POME-LINE-CURVATURE-INTEGRAL-PERIOD-001
**Severity:** low. **Status:** verified conditional deduction / hypothesis-boundary example; printed Proposition 5.45.1 is **correct** and asserts only necessity of closedness.

Closedness of a proposed line-bundle curvature current is **not sufficient**: on \(\mathbb P^1\), set \(\theta=\sqrt2\,\omega_{\rm FS}\) with \(\int_{\mathbb P^1}\omega_{\rm FS}=1\). This \(\theta\) is smooth, strictly positive and closed. For every globally defined locally integrable \(u\), \(\int_{\mathbb P^1}dd^cu=0\) by the current Stokes formula, so \(T=\theta+dd^cu\) has total integral \(\sqrt2\). If \(T\) were the curvature of any singular Hermitian metric with locally integrable weights on any holomorphic line bundle \(L\to\mathbb P^1\), the Chern-class normalization in §5.45.1 would give \(\int_{\mathbb P^1}T=\deg L\in\mathbb Z\), a contradiction. **Proposed:** optionally state the integral cohomology obstruction in the discussion after Proposition 5.45.1; retain the existing closedness proof unchanged. This is a separate issue from the nonclosed Hermitian curvature obstruction, and no Lefschetz-(1,1) sufficiency assertion is made. **Affected dependents:** interpretation of section growth/multiplier ideals in terms of genuine line bundles rather than arbitrary closed real backgrounds.

## Additional directly checked passages and honest limitations

- §5.40.1's countable weighted sum uses the uniform normalized \(L^1\)-bound and does not confuse q.e. with pointwise constraints; §5.40.5/6's perturbation comparison was read as stated, without replacing its upstream Josefson/compactness inputs.
- §5.40.10–12's ball-hyperplane pole and finite-obstacle inequalities were directly checked for sign, parameter monotonicity and the uniform-on-compact \(e^{-t/m}\) bound; no separate new finding was registered, nor any nonexistent canonical self-intersection of divisor currents.
- §5.41.5, 5.41.8 and 5.41.9's endpoint/left-continuity and pointwise biconjugacy arguments were read as conditional users of the established Kiselman and psh-uniqueness inputs; their entire transitive proof chain was **not** certified.
- §5.45.1 was directly checked using local weight changes \(\varphi'=\varphi-\log|g|^2\), \(d\,dd^c=0\), and the precise normalization; the period obstruction above is additional, not an accusation that the printed statement is false.
- **Exactly three** previously inventory-only ToC section rows (§§5.40, 5.41, 5.45) receive *selected proof-level* coverage, plus contextual §5.12.2; the actual existing matrix's 747 distinct rows are retained. **Zero entire sections, chapters or uninspected dependencies were certified.** No software builds/tests, CI, formal verification, published site, original body, source, tag or proof registry modifications were performed.

**Statuses preserved:** All prior unresolved findings remain unresolved unless independently addressed; no old findings are repeated as new progress. Specifically, any old Demailly approximation/regularization, Bergman, L², Ohsawa–Takegoshi, multiscale-atlas or positivity-loss proof-completion finding remains **deferred-by-user** and unexamined.
