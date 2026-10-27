# Audit of Morse equation aliases, metric completions, and spectral counting measures — 28 October 2026

**Reviewed production main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. **Starting audit branch:** `d16eef2f0c21ce6226a5efbcd4305a6ff0a8e77f`. **Scope:** selected integrated mathematical reading-edition passages in §§5.39, 10.95, and 10.96. These were inventory-only entries in the existing coverage matrix. This is **not** certification of any whole section or of the underlying magnetic-field spectral theorem. In particular, the author-excluded Demailly approximation/regularization and its dedicated Bergman, L², OT, multiscale and positivity-loss programmes were **not** inspected, extended, or relied on as proof-completion tasks. The name of the historical source of §§10.95–10.96 is provenance, not a reopening of that programme.

## POME-HOLO-MORSE-ALIGN-ALIASES-001 — confirmed error in integrated equation rendering, not a false theorem

**Severity:** medium (reading-edition integration/navigation). **Status:** confirmed error. **Affected material:** the three displayed formulas of Theorem 10.96.1 and the two separately generated equation entries and permanent-tag pages. **Main path:** `docs/sections/holomorphic-morse-inequalities/index.html`, blob `704bff3556692ef4068fce494ac0ee156a227b4f`, physical lines **16–21** (correct grouped display), **25–43** (the proof), and **44** (two extra generated reading chunks). **Source/provenance:** `demailly-complex-geometry:4762DBCB` (theorem, permanent tag `778548FB8A37`), `demailly-complex-geometry:AA111217` (grouped display, tag `6B15B5C74219`), `demailly-complex-geometry:BE49D869` (extra equation, tag `D6DA1926A1BC`), `demailly-complex-geometry:7C37CBC7` (extra equation, tag `8AE70D2D36EE`).

The grouped display at lines 18–21 already contains all three labelled rows, with equation numbers **10.96.2**, **10.96.3**, and **10.96.4**, in a single top-level LaTeX `align`. The separate chunks at line 44 then *repeat* the latter two mathematical rows. Each extra chunk embeds the malformed nesting

```tex
\[\begin{aligned}\begin{align} ... \end{align}\end{aligned}\]
```

The duplicate content and nesting occur in the actual integrated HTML, not just in metadata. The tag routes independently confirm the problem: `docs/tag/D6DA1926A1BC/index.html` (blob `3ced8814157891680d440dcad3977c85aaf86398`, physical line 5) and `docs/tag/8AE70D2D36EE/index.html` (blob `a9621174cdb734038817ddb6384ba04256fd5f7c`, physical line 5) contain the same malformed single-row nested-display representation, while `docs/tag/6B15B5C74219/index.html` (blob `078915aa69b36c9870ada22de538b13bab8b64ba`, physical line 5) contains the complete valid grouped formula.

**Justification:** mathematical equality of each repeated row follows by direct symbol comparison with the second and third rows of the first display. An AMS `align` environment is not a valid nested child of `aligned`, and additional display-math delimiters wrap the nesting. The intended inequalities themselves are not contradicted. No browser or MathJax execution was performed; this finding identifies a definite duplicated/malformed TeX source in the generated reading edition, not a measured browser failure.

**Proposed correction:** repair *upstream reading-edition group-row/descendant placement* in a separately reviewable production patch so that each theorem row appears exactly once. Preserve the theorem, each equation number and **all three permanent equation tags**, with standalone tags resolving to corresponding rows/anchors of the one grouped display rather than a duplicate standalone invalid TeX formula. Preserve history/provenance. Update any tag-route rendering and navigation from the same canonical equation-group map. Require rendering and link checks before future production publication. **No source/body/registry/HTML/tag changes were made in this audit branch.**

## POME-METRIC-COMPLETIONS-GH-001 — quantitative Gromov–Hausdorff convergence

**Severity:** low. **Status:** verified conditional deduction. **Main path:** `docs/sections/plurisubharmonic-functions-and-singularities--potential-regularity-and-metric-distance/index.html`, blob `26695e8698b9114b97108efb16ec94f3984ee308`; **§5.39.1**, physical lines **13–46**, source `non-kahler-pluripotential-theory:EF691FCE`, tag `230882F1D833`; **§5.39.6**, lines **65–108**, source `non-kahler-pluripotential-theory:97B8A37E`, tag `21429B9E1BF3`; **Corollary 5.39.8**, lines **135–166**, source `non-kahler-pluripotential-theory:017413AB`, tag `D3B517FBCE4F`.

Assume precisely the global hypotheses of Corollary 5.39.8 on a compact connected manifold \(X\): the continuous potentials have a common square-root-Dini modulus, the smooth backgrounds have uniformly bounded coefficients, and each positive current is a smooth positive Hermitian form off a proper analytic set. Let \(Y_j\) be the intrinsic-metric completion of \(X\setminus A_j\), and \(d_j\) the pullback pseudometric on \(X\) of its completed distance. The printed corollary supplies a subsequence, still indexed by \(j\), for which \(d_j\to d_\infty\) **uniformly on \(X\times X\)**, with \(d_\infty\) a continuous pseudometric.

**Stronger conclusion, with exact quantitative bound:**

\[
Y_\infty:=X/\{d_\infty=0\},\qquad
d_{\rm GH}(Y_j,Y_\infty)
\ \leq\ \frac12\sup_{x,y\in X}|d_j(x,y)-d_\infty(x,y)|
\ \longrightarrow\ 0.
\]

In particular, no lower-bound assumption on the currents is needed for **GH precompactness of their metric completions**; the limit may be a collapsed quotient. If, additionally, \(T_j\geq c\,\omega_0\) off \(A_j\) for a fixed \(c>0\), then \(d_\infty\geq\sqrt c\,d_{\omega_0}\). Hence \(Y_\infty\) identifies canonically with \(X\), without collapsing distinct points. The common Dini upper modulus supplies the reverse topological continuity, so this identification is a homeomorphism (no unproved bi-Lipschitz assertion).

**Proof in full, assuming the printed corollary:** The continuous surjection \(\pi_j:X\to Y_j\) from the corollary identifies exactly the points at zero \(d_j\)-distance. Thus \(X/{\sim_j}\), where \(x\sim_j y\iff d_j(x,y)=0\), is isometric onto \(Y_j\), with no assumption that \(\pi_j\) is injective. Similarly \(Y_\infty=X/{\sim_\infty}\) is a compact metric space: the quotient is compact since \(X\) is compact and \(d_\infty\) continuous. Consider the relation

\[
\mathcal R_j=\{(\pi_j(x),[x]_\infty):x\in X\}\ \subseteq\ Y_j\times Y_\infty.
\]

Both projections are surjective, even when the zero-distance equivalence relations differ. Its distortion is bounded by
\[
\operatorname{dis}(\mathcal R_j)
=\sup_{x,y\in X}|d_j(x,y)-d_\infty(x,y)|=:\varepsilon_j.
\]
The elementary correspondence characterization of GH distance gives \(d_{\rm GH}\leq\varepsilon_j/2\). This last characterization can be proved directly by putting cross-distances between points in the two quotients equal to the infimum of \(\varepsilon_j/2+d_j(\pi_j x,u)+d_\infty([x]_\infty,v)\) over \(x\in X\), with an arbitrarily small positive extra offset if \(\varepsilon_j=0\), and taking the induced common ambient metric. Thus no hidden compactness-of-correspondence issue is needed.

**Sharpness of the factor \(1/2\):** take \(A_j=\varnothing\), \(v_j=0\), and \(T_j=\theta_j=\epsilon_j\omega_0\) with \(\epsilon_j\downarrow0\). The printed corollary's common Dini hypothesis holds, e.g. with \(m(r)=r^2\), and \(d_j=\sqrt{\epsilon_j}\,d_{\omega_0}\), \(d_\infty=0\). Thus \(Y_\infty\) is a singleton, \(\varepsilon_j=\sqrt{\epsilon_j}\operatorname{diam}(X,d_{\omega_0})\), and
\[
d_{\rm GH}(Y_j,\{\mathrm{pt}\})=\tfrac12\operatorname{diam}(Y_j)=\varepsilon_j/2.
\]
The last equality follows both from the diameter bound for any embedding and from placing one new point at distance half the diameter in a metric extension. Therefore the universal numerical coefficient cannot be improved.

**Conditionality / affected dependents:** this is a consequence of the exact **already printed** §5.39.8 uniform pseudometric convergence, not an independent proof of the cutoff mass estimate, real-geodesic segment averaging or analytic-set avoidance arguments upstream. It can be appended as a metric corollary for the compactness/degeneration framework without changing the original statement.

## POME-MORSE-SPECTRAL-VAGUE-001 — spectral measures converge vaguely, including atoms in the limit

**Severity:** low. **Status:** verified conditional deduction. **Main path:** `docs/sections/dolbeault-spectral-asymptotics/index.html`, blob `8ebaf0d0f3d1254997b019f0a66e8e9848367335`. **Lemma 10.95.2:** physical lines **22–64**, source `demailly-complex-geometry:023C015F`, tag `0EAC1C0027AB`; **Theorem 10.95.5:** physical lines **66–130**, source `demailly-complex-geometry:C1E122A4`, tag `151C621E620C`. The subsequent finite-dimensional cancellation in **Theorem 10.96.1**, `docs/sections/holomorphic-morse-inequalities/index.html:25–43`, source `demailly-complex-geometry:4762DBCB`, tag `778548FB8A37`, was also checked separately; it is algebraically consistent and is **not** the integration defect above.

Let \(\lambda_{k,q,\ell}\geq0\) be the eigenvalues, with multiplicities, of \(2\square_{L^k\otimes F}/k\) on \((0,q)\)-forms. Define the locally finite positive measures
\[
\mu_{k,q}=k^{-n}\sum_\ell\delta_{\lambda_{k,q,\ell}}
\qquad\text{on }[0,\infty).
\]
Define \(\mu_q\) through the integrated constant-magnetic-field model of Theorem 10.95.5; equivalently its distribution function is
\[
\mu_q([0,t])=r\int_X\sum_{|J|=q}
\nu_{b(x)}(t+V_J(x))\,dV_\omega
\]
at its continuity points \(t\), using the theorem's conventions for the local counting measures \(\nu_b\).

**Conclusion:** \(\mu_{k,q}\rightharpoonup\mu_q\) *vaguely*, i.e.
\[
\int\varphi\,d\mu_{k,q}\longrightarrow\int\varphi\,d\mu_q
\quad\text{for each }\varphi\in C_c([0,\infty)).
\]
This statement does **not** say the eigenvalue count converges at a jump of the limiting counting function; that would require extra analysis.

**Proof:** Theorem 10.95.5 provides convergence of the cumulative masses at all \(t\) outside a countable exceptional set containing all non-continuity points of the limiting distribution. The model's uniform local density/count bound ensures \(\mu_q([0,T])<\infty\) for every fixed \(T\), while any fixed sufficiently large continuity point \(T'\!>T\) bounds \(\sup_{k\geq k_0}\mu_{k,q}([0,T])\) by the convergent sequence \(\mu_{k,q}([0,T'])\). Choose a finite partition of \([0,T']\) with endpoints all continuity points of the limiting distribution; the measures of its half-open cells converge by subtracting cumulative counts. Approximate an arbitrary continuous compactly supported test uniformly by cellwise-constant functions; the common local mass bound controls the error. This proves vague convergence. In the printed §10.96 proof, the auxiliary finite-complex identity \(c_k^j=h_k^j+b_j+b_{j+1}\) gives precisely the alternating sum defect \(-b_{q+1}\); with \(q=n\) it vanishes. The independent scale arithmetic in §10.95 is also consistent: \(k l_k^4=k^{-1/3}\), \(\sqrt{k}l_k=k^{1/6}\), and the partition error \(k^{-1}(\eta_k l_k)^{-2}=k^{-1/4}\) for \(l_k=k^{-1/3}\), \(\eta_k=k^{-1/24}\).

**Conditionality / affected dependents:** This is only a measure-theoretic consequence of the printed spectral counting theorem and its stated model bound. The constant-field Dirichlet model, magnetic heat-kernel density, all analytic localization and full holomorphic Morse inequalities are **not newly independently certified**. The new result can clarify spectral-distribution applications without asserting pointwise count convergence at atoms.

## Exact coverage and exclusions

- **§5.39 (first selected proof read):** Theorem 5.39.1 local trace-mass cutoff/annular segment estimate, Theorem 5.39.6 monotone-modulus dyadic integral step, Corollaries 5.39.7–8 including Arzelà–Ascoli of pullback pseudometrics; only the stated passages, not every upstream measure/geometry input. Source/HTML anchors as above.
- **§10.95 (first selected proof read):** Lemma 10.95.2 local form-comparison and scaling, Theorem 10.95.5 Dirichlet bracketing, IMS localization, and Riesz-to-count passage; reliance on the earlier magnetic model remains conditional.
- **§10.96 (first selected proof read):** printed Theorem 10.96.1 spectral-to-cohomology rank bookkeeping and curvature-index sign matching, plus the unequivocal equation-alias duplication in the integrated page and two permanent-tag pages. No new counterexample to the holomorphic Morse inequalities is claimed.

This upgrades precisely three previously *inventory-only* rows of the 747-row current ToC coverage matrix to **selected** inspection; it certifies **zero** full sections. No old finding was repeated as new, and all existing resolved/unresolved/deferred records are retained. All user-deferred dedicated Demailly approximation/regularization, Bergman, L², Ohsawa–Takegoshi, multiscale-atlas and positivity-loss issues remain **deferred-by-user**, not repaired or independently certified. Only Markdown audit records were prepared; no source repository, production main, proof registry, permanent tag, generated site, GitHub Actions, build, test suite, browser rendering or formal proof checking was changed/executed.
