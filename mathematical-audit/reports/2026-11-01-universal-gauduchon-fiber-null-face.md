# 2026-11-01 — uniqueness of the exposed null-current face in the Gauduchon radial counterexample

**Production main reviewed:** `b6933b772f41b45918f7e25ed1afbbb1fd892272` (not modified). **Scope:** actual integrated §§12.14.6, 12.14.10, 12.14.13 and 24.3.2, plus an independently selected §15.32.6 proof check. Demailly approximation/regularization, the dedicated Bergman/L²/Ohsawa–Takegoshi/multiscale/positivity-loss programme, and its prerequisites were not examined.

## POME-GAUD-UNIVERSAL-FIBER-EXPOSED-001

**Severity:** low. **Status:** verified conditional deduction. No false original theorem, full upstream certification, or production repair is asserted.

**Exact anchors.** Main `docs/sections/a-gauduchon-variational-volume--positive-volume-without-bigness/index.html`, blob `4e892ab379abdfa3b6520671db344e94bbc7a51a`: the model is specified at **lines 10–20**; Theorem **12.14.6**, source `non-kahler-pluripotential-theory:7A1559DF`, permanent tag `ECAB6BFB33FD`, is at **lines 100–140**; Proposition **12.14.10**, source `non-kahler-pluripotential-theory:EDD3E86A`, permanent `0E9506DB4E70`, at **lines 169–205**; Proposition **12.14.13**, source `non-kahler-pluripotential-theory:4D5B675F`, permanent `F8EA88FD522E`, at **lines 243–274**. Main `docs/sections/problems-in-hermitian-pluripotential-theory--positive-gauduchon-volume-and-bigness/index.html`, blob `e64a919194dbc4dbd1739cd02811a5c45e252358`: Proposition **24.3.2**, source `non-kahler-pluripotential-theory:B0E460AB`, permanent `32F82EA89236`, **lines 26–68**, with the determinant-collapse discussion **lines 71–84**. §24.3.2 was already directly sampled on **2026-10-29**; the present work is an *additional*, independent proof/model analysis, not its first coverage.

### Claim: rigidity of every almost-null Gauduchon test

Keep the printed notation: for \(m\ge2\), \(n=m+1\), set
\[
 B=\mathbb P^m,\quad X=B\times\mathbb P^1,\quad
 t=\frac{m-1}{m},\qquad
 x([Z_0:\ldots:Z_m])=\frac{\sum_{i=1}^{m}|Z_i|^2}{\sum_{i=0}^{m}|Z_i|^2}.
\]
Write \(\omega\) and \(w\) for the pullbacks of the Fubini–Study forms normalized by \(\int_B\omega^m=\int_{\mathbb P^1}w=1\), and set
\[
 a=x/t,\quad h=\omega+w,\quad\theta=\omega+a\,w,\quad
 p=[1:0:\cdots:0],\quad Z=\{p\}\times\mathbb P^1.
\]
Here \(\int_Zh=1\), \(\theta\ge0\), and the kernel of \(\theta\) over \(Z\) is precisely its vertical tangent line. Let
\[
 \mathscr C=\left\{T\text{ positive of bidegree }(m,m):
       dd^c T=0,\ \int_Xh\wedge T=1\right\}.
\]
Then the exposed zero face is a singleton:
\[
 \boxed{\left\{T\in\mathscr C:\int_X\theta\wedge T=0\right\}=\{[Z]\}.}\tag{1}
\]
In particular, for **any directed net** \(T_\alpha\in\mathscr C\) satisfying \(\int_X\theta\wedge T_\alpha\longrightarrow0\), one has \(T_\alpha\rightharpoonup[Z]\) along the *original indexing net*.

Every smooth Gauduchon metric \(\gamma_\alpha\) satisfies \(dd^c(\gamma_\alpha^m)=0\). Hence the above conclusion applies to \(\gamma_\alpha^m\) if the \(h\)-trace is normalized to one and the \(\theta\)-pairing tends to zero. Furthermore, the printed positive root-volume identity \(\lambda_\mu(\theta)=n^{1/n}>0\), **used only conditionally here**, gives
\[
 0\le D_\mu(\gamma_\alpha)
   \le n^{-1/n}\int_X\theta\wedge\gamma_\alpha^m\longrightarrow0.
\]
Thus Proposition 12.14.13's explicitly constructed family is not special in its current limit: **all** normalized almost-threshold Gauduchon families converge to the same fiber current.

### Proof of the unique exposed face

1. **Weak compactness for genuine nets.** The \(h\)-trace controls each coefficient measure of a positive current of bidegree \((m,m)\); fixed trace mass one therefore bounds all coefficient measures. Weak-* compactness for positive currents on compact \(X\), together with the continuity of \(dd^c\) in the distribution topology, shows that \(\mathscr C\) is weakly compact and Hausdorff. Neither sequential compactness nor sequential diagonal extraction is required.
2. **Support and the one allowed tangent direction.** The smooth form \(\theta\) is strictly positive definite on \(X\setminus Z\). Thus, if \(T\in\mathscr C\) has \(\int_X\theta\wedge T=0\), the positive measure \(\theta\wedge T\) is identically zero, and every compact \(K\subset X\setminus Z\) has \(\theta\ge c_Kh\) for some \(c_K>0\); consequently \(T|_{X\setminus Z}=0\). Along \(Z\), \(\theta\) is strictly positive in the \(m\) horizontal directions and vanishes only in the one vertical direction. The Hermitian matrix of coefficient measures of \(T\) is positive. Vanishing contraction with \(\theta\) forces all its horizontal diagonal measures to vanish; positivity and Cauchy–Schwarz for the coefficient matrix then kill its horizontal/vertical mixed coefficients. Hence \(T\) has only its vertical tangent component and is represented by a finite positive measure \(\nu\) on \(Z\simeq\mathbb P^1\): for any smooth \((1,1)\)-test form \(\beta\),
   \[
     T(\beta)=\int_Z \frac{i^*\beta}{w}\,d\nu,
   \]
   where \(i:Z\hookrightarrow X\) is the inclusion. The displayed quotient is the scalar coefficient of the top-degree form \(i^*\beta\) relative to the positive area form \(w\).
3. **Gauduchon closure is enough.** Given a smooth real \(f\) on \(Z\), extend it to \(\widetilde f\) on \(X\). Since \(dd^cT=0\),
   \[
      0=T(dd^c\widetilde f)
       =\int_Z\frac{dd^cf}{w}\,d\nu.
   \]
   The elementary Poisson equation on the compact Riemann surface \(\mathbb P^1\) solves \(dd^cf=g\,w\) for each smooth \(g\) with \(\int_Zg\,w=0\) (with the fixed \(dd^c\) normalization absorbed into the Laplacian). Therefore \(\int_Zg\,d\nu=0\) for every such \(g\); hence \(\nu=cw\). The trace normalization gives \(c=\int_Xh\wedge T=\nu(Z)=1\), so \(T=[Z]\). Crucially, this uses **\(dd^cT=0\)**, not the stronger and unavailable hypothesis **\(dT=0\)**.
4. **Original-net convergence.** Every cluster point of a directed net \(T_\alpha\) with vanishing \(\theta\)-pairing is, by (1), equal to \([Z]\). In the compact Hausdorff space \(\mathscr C\), uniqueness of all cluster points implies convergence of the entire net. The final determinant estimate is exactly the printed root-volume inequality, *not* an independent certification of its analytic construction.

### A sharp quantitative off-fiber bound

For each \(0<r<t\), on \(\{x\ge r\}\) the pointwise Hermitian inequality is
\[
   \theta=\omega+\frac{x}{t}w\ge\frac{r}{t}(\omega+w)=\frac{r}{t}h.
\]
Every positive \((m,m)\) current \(T\) consequently satisfies the **measure-level** estimate
\[
 \boxed{\int_{\{x\ge r\}}h\wedge T\le\frac{t}{r}\int_X\theta\wedge T.}\tag{2}
\]
The constant \(t/r\) is optimal. For \(q\in B\) with \(x(q)=r\), the closed positive vertical-fiber current \(T=[\{q\}\times\mathbb P^1]\) has left side \(1\) and \(\theta\)-pairing \(r/t\), so equality holds.

It is also sharp **within smooth balanced metric powers**, in the limiting sense. Choose \(q_\varepsilon\to q\) with \(x(q_\varepsilon)>r\), and smooth nonnegative probability densities \(f_\varepsilon\omega^m\) supported in arbitrarily small neighborhoods of \(q_\varepsilon\) contained in \(\{x>r\}\). Define
\[
 \Gamma_\varepsilon=
   \frac{f_\varepsilon\,\omega^m+\varepsilon h^m}{1+n\varepsilon}.
\]
Since \(f_\varepsilon\omega^m\) is top-degree on \(B\), it is closed. Moreover, \(\Gamma_\varepsilon>0\), \(d\Gamma_\varepsilon=0\), and \(\int_Xh\wedge\Gamma_\varepsilon=1\), using \(\int_Xh^n=n\). The positive-root theorem invoked in the proof of Proposition 12.14.13 gives a smooth balanced metric \(b_\varepsilon\) with \(b_\varepsilon^m=\Gamma_\varepsilon\). Then
\[
 \int_{\{x\ge r\}}h\wedge\Gamma_\varepsilon\longrightarrow1,\qquad
 \int_X\theta\wedge\Gamma_\varepsilon\longrightarrow r/t,
\]
so the ratio converges to \(t/r\). No singular current is being passed off as a smooth balanced form.

### Classification, dependencies, and coverage

**Verdict:** low / verified conditional deduction. Theorem 12.14.6, Propositions 12.14.10/13 and Proposition 24.3.2 are **not refuted**. Equations (1)–(2) and the uniqueness of the weak null-current limit are new local deductions; the determinant conclusion uses the already printed positive root volume. The proof invokes positive-current weak compactness, a positive matrix-of-measures argument, the standard Poisson equation on \(\mathbb P^1\), and the separately stated positive-root theorem for the sharp smooth approximation; these inputs have not been transitively certified as part of this run. Proposed action: optional corollary after §12.14.13 or the §24.3.2 discussion, preserving all labels, historical attribution and distinct Gauduchon versus balanced hypotheses. Affected dependents are the §12.14 volume-versus-threshold test discussion and §24.3 determinant-denominator collapse analysis; no source or canonicalization change is made.

**Independent selected crosscheck, no fresh mathematical error:** Proposition **15.32.6** source `non-kahler-pluripotential-theory:500DB50B`, permanent `C926F63790E3`, in `docs/sections/equations-with-prescribed-singularities--stability-of-the-subsolution-threshold/index.html` blob `903ae0ce7173604063a833295dd94e971b18fd72`, **lines 103–129**. Checked its \(L^1\)-embedding of the root norm, its nonnegative Cauchy partial sums and their \(L^n\)-obstruction. The unbounded-normalization input from §§12.15.4/12.2.3 remains conditional. §15.32 was historically sampled, not first covered here.

**Actual work:** further selected §24.3.2 proof-level reading (**first sampled 2026-10-29**), new exact radial exposed-face proof and sharpness, selected §12.14.6/.10/.13, plus the independent §15.32.6 argument. **25 current main chapters / 747 numbered ToC sections / zero whole mathematical-section certifications**. All older resolved/unresolved/external/deferred findings remain unchanged. User-excluded Demailly approximation/regularization and its dedicated Bergman/L²/OT/multiscale/positivity-loss programme remains **deferred-by-user**, neither resolved nor reopened. No mathematical software tests, builds, CI, formalization, website publication, main/source/docs/tags/registry changes.