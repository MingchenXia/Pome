# Mathematical audit: anisotropic Monge–Ampère concentration and totally real pluripolar nullity

**Checkpoint:** 2026-10-23, Asia/Shanghai. **Reviewed main:** b6933b772f41b45918f7e25ed1afbbb1fd892272. **Starting review branch:** 102b599aeb30be2eef2d3ecc9df5a350eae489e0. Audit-only report, not a source correction or publication.

Freshly inspected main AGENTS.md (blob eda69505b93b4782290d9cfac07c8651dedd17c5), documentation/proof-expansions.md (8b37e218c74d5a93637e0f092cf5f29cc338a94d), the actual 25-chapter/747-section ToC (c0c07abf4d8f7575b54cff2ec694fcf987f51cf8), and the review-branch README.md (7967ffabeccea69fd80a5ec5d364e0a8e6bca137) and mathematical-audit/LATEST.md (blob 6b77ee90f0c06afd45d988b3376329904e613232). The inventory is **not** a statement of verification of 747 sections.

## Exact new coverage and source anchors

1. **§6.55**, docs/sections/concentrating-restricted-singularities/index.html, blob **3167593400ca0dd405a850fbafd634d0f0b97e48**. Section source **cao-paun-foliations:12922FE5**, permanent tag **0D6DE152AF94**. Directly reviewed Lemma 6.55.1, source **cao-paun-foliations:A77E2EB0**, permanent tag **279034C7A935**, HTML lines **9–25** (proper polynomial degree, scaling, exact total top-degree mass). In Proposition 6.55.2, source **cao-paun-foliations:77E495BB**, permanent tag **F6E99CEFC668**, inspected only local smooth Monge–Ampère mass, comparison, and fixed-m convergence, lines **31–70**; Eq. 6.55.3 tag **6DD9160CD03C** and Eq. 6.55.4 tag **8472787D115A**. Its subsequent gentle analytic approximation, multiplier ideals, and positivity-loss steps **lines 72–93 are entirely deferred-by-user**. The new finding below concerns the exact **smooth model** of Lemma 6.55.1 only.
2. **§6.45**, docs/sections/lelong-densities-generalized-masses-and-multiplicity--rotation-of-an-arbitrary-isolated-continuous-weight/index.html, blob **9175f1ac475bf4a9f9d9a1749037ae86beb675e8**. Directly checked only Lemma 6.45.1, source **demailly-complex-geometry:F7E1037D**, permanent tag **D72B7AE5B407**, HTML lines **8–31**: one-variable Riesz/Fubini, real cube slices, complexification of the skew-Hermitian Lie algebra and Haar density. Theorem 6.45.2 and its smoothing/current-product proof (from line 36 onward) **were not audited**.
3. **No newly claimed coverage** for §§6.56, 9.74. They were consulted for dependencies and duplicate-finding prevention: remote SECTION_MATRIX.md already documents the earlier **POME-CAOPAUN-CENTER-UNIFORM-LELONG-001** and **POME-CAOPAUN-FOLIATION-CYCLE-INPUT-001**. These are **not** new items or relabeled as resolved here.

## POME-CAOPAUN-MA-ANISOTROPIC-ITERLIMIT-001

**Status:** verified conditional deduction; **severity:** low (sharp limit-order diagnostic, not an error in Lemma 6.55.1 or Proposition 6.55.2). **Hypotheses:** complex dimension \(n\ge 2\), integer \(m\ge1\), \(\varepsilon>0\), and normalization \(dd^c=\frac{i}{2\pi}\partial\bar\partial\). Put

\[
F_m(z)=(z_1,z_2^m,\ldots,z_n^m),\qquad
f_{m,\varepsilon}=m^{-(n-1)/n}\log(|F_m(z)|^2+\varepsilon),\qquad
\mu_{m,\varepsilon}=(dd^cf_{m,\varepsilon})^n.
\]

The printed Lemma 6.55.1 proves that \(\mu_{m,\varepsilon}\) is a probability measure on \(\mathbb C^n\).

**Exact marginal-tail formula:** for every \(r>0\) and \(2\le j\le n\),

\[
\boxed{\mu_{m,\varepsilon}(\{|z_j|>r\})=
       \frac{\varepsilon}{\varepsilon+r^{2m}}.}\tag{1}
\]

For the unpowered first coordinate,
\[
\mu_{m,\varepsilon}(\{|z_1|>r\})=
\frac{\varepsilon}{\varepsilon+r^2}.
\]

In particular, if \(\varepsilon_m=r^{2m}\) with \(0<r<1\), then \(\varepsilon_m\downarrow0\) but \(\mu_{m,\varepsilon_m}(\{|z_j|>r\})=1/2\) for **every** \(m\). The mass is not uniformly concentrated at the origin in the pair \((m,\varepsilon)\).

**All coupled weak limits:** let \(m\to\infty\) and \(\varepsilon_m\downarrow0\) with
\[
R=\lim_{m\to\infty}\varepsilon_m^{1/(2m)}\in[0,1].
\]
Write \(h_R\) for Haar probability on the complex circle \(\{|z|=R\}\), with \(h_0=\delta_0\). Then, as finite Radon probability measures in the narrow topology,
\[
\boxed{\mu_{m,\varepsilon_m}\ \Longrightarrow\
  \delta_0\otimes h_R^{\otimes(n-1)}.}\tag{2}
\]
In particular, \(\varepsilon_m=e^{-2am}\), \(a>0\), produces the nontrivial real \((n-1)\)-torus of radius \(e^{-a}\). For each **fixed** \(m\), however, \(\mu_{m,\varepsilon}\Rightarrow\delta_0\) as \(\varepsilon\downarrow0\).

**Iterated limits do not commute:** for every fixed \(\varepsilon>0\),
\[
\mu_{m,\varepsilon}\ \Longrightarrow\
\lambda_\varepsilon^{(1)}\otimes h_1^{\otimes(n-1)}
\quad(m\to\infty),
\qquad
d\lambda_\varepsilon^{(1)}(w)
=\frac{\varepsilon}{\pi(\varepsilon+|w|^2)^2}\,dA(w).
\]
Consequently
\[
\boxed{
\lim_{m\to\infty}\lim_{\varepsilon\downarrow0}\mu_{m,\varepsilon}
  =\delta_0,\qquad
\lim_{\varepsilon\downarrow0}\lim_{m\to\infty}\mu_{m,\varepsilon}
  =\delta_0\otimes h_1^{\otimes(n-1)}\ne\delta_0.}\tag{3}
\]

**Complete proof.** For \(g_\varepsilon(w)=\log(\varepsilon+|w|^2)\), its Hermitian Hessian matrix has tangential eigenvalues \((\varepsilon+|w|^2)^{-1}\) (multiplicity \(n-1\)) and radial eigenvalue \(\varepsilon(\varepsilon+|w|^2)^{-2}\). Thus
\[
\lambda_\varepsilon=(dd^cg_\varepsilon)^n
=\frac{n!\,\varepsilon}{\pi^n(\varepsilon+|w|^2)^{n+1}}\,dV(w),
\qquad \lambda_\varepsilon(\mathbb C^n)=1.
\]
The polynomial \(F_m\) has generic degree \(m^{n-1}\), and the normalizing exponent in \(f_{m,\varepsilon}\) gives
\[
\mu_{m,\varepsilon}=m^{-(n-1)}F_m^*\lambda_\varepsilon.
\]
Accordingly, integrate any bounded Borel test \(\Phi(z)\) by averaging \(\Phi\) over the \(m^{n-1}\) inverse images of \(w\), then integrating against \(\lambda_\varepsilon(dw)\). Critical values are null and do not affect this formula.

Integrating the displayed density over the remaining \(n-1\) complex coordinates yields the exact marginal
\[
\int_{\mathbb C^{n-1}}
\frac{n!\,\varepsilon\,dV(y)}
     {\pi^n(\varepsilon+|w_j|^2+|y|^2)^{n+1}}
=\frac{\varepsilon}{\pi(\varepsilon+|w_j|^2)^2},
\]
by the polar Beta integral
\(\int_{\mathbb C^k}(A+|y|^2)^{-p}dV
=\pi^k\Gamma(p-k)A^{k-p}/\Gamma(p)\).
Integrating in polar coordinates from \(|w_j|=r^m\) to infinity gives (1), because \(|z_j|^m=|w_j|\) for \(j\ge2\). The first-coordinate formula is identical with exponent one.

For (2), couple all measures using a single random vector \(\Xi\in\mathbb C^n\) with density \(n!/\{\pi^n(1+|\xi|^2)^{n+1}\}\). Set \(w=\sqrt{\varepsilon_m}\,\Xi\), \(z_1=w_1\), and choose each \(z_j\) uniformly among the \(m\)-th roots of \(w_j\), independently conditional on \(\Xi\). This generates \(\mu_{m,\varepsilon_m}\) exactly. For almost every \(\Xi\), its coordinates \(\Xi_j\) are nonzero, and
\[
|z_1|=\sqrt{\varepsilon_m}|\Xi_1|\to0,\qquad
|z_j|=\varepsilon_m^{1/(2m)}|\Xi_j|^{1/m}\to R \quad(j\ge2).
\]
The conditional root angles form translated regular \(m\)-gons; their product empirical measures converge to product Haar measure on \((S^1)^{n-1}\). The conditional average of any bounded continuous \(\Phi\) therefore converges to its integral against \(\delta_0\otimes h_R^{\otimes(n-1)}\). The bound by \(\|\Phi\|_\infty\) and dominated convergence in \(\Xi\) justify the **narrow** convergence, with no assumed interchange of singular currents or uniformity in \(m\). For fixed \(m\), the same coupling and \(\varepsilon\downarrow0\) instead make **all** coordinates tend to zero, proving the fixed-\(m\) statement. For fixed \(\varepsilon\), \(z_1=\sqrt\varepsilon\Xi_1\) persists while all other root radii tend to one; the same root-angle argument gives the asserted product limit. Finally \(\sqrt\varepsilon\Xi_1\to0\) almost surely as \(\varepsilon\downarrow0\), giving (3). QED.

**Implication and correction policy.** Proposition 6.55.2 uses a **fixed \(m\)** before taking its \(\varepsilon\)-subsequence in lines 61–70, so these calculations do **not** refute it. They demonstrate that silently interchanging those parameters, or postulating uniform concentration in \(m\), would be invalid. Add an optional example/caution after Lemma 6.55.1, preserving its source tag and the separate, regularization-dependent later proof. **Do not** re-open lines 72–93 or claim to have verified the original existence theorem.

## POME-TOTALLY-REAL-PLURIPOLAR-NULL-001

**Status:** verified conditional deduction; **severity:** low (generalization of the printed Haar-null lemma; no erroneous source statement). **Source:** the self-contained real-cube proof and holomorphic Lie-chart construction of Lemma 6.45.1, blob/tag/lines above.

**Claim.** If \(Y\) is a complex \(N\)-manifold, \(N\ge1\), \(M\subset Y\) is an embedded real-analytic **maximally totally real** submanifold of real dimension \(N\), and \(P\) is locally pluripolar in a neighborhood of \(M\), then \(P\cap M\) has measure zero for every smooth positive \(N\)-dimensional density on \(M\). This includes the printed unitary-group assertion with \(Y=\mathrm{GL}_n(\mathbb C)\), \(N=n^2\), \(M=\mathrm U(n)\).

**Proof.** Near \(x\in M\), choose a real-analytic coordinate parametrization \(F:V\subset\mathbb R^N\to M\). Its component power series complexifies to a holomorphic map \(\widetilde F\) from a complex polydisc in \(\mathbb C^N\) to \(Y\). Since \(M\) is maximally totally real, the real tangent vectors \(dF(e_j)\) are complex linearly independent, so the complex derivative of \(\widetilde F\) is invertible. The complex inverse function theorem makes \(\widetilde F\) biholomorphic after shrinking. A local nontrivial psh function \(u\) having \(P\) in its \(-\infty\) set pulls back to a nontrivial psh function \(u\circ\widetilde F\) on that polydisc. The real-cube Fubini induction in lines 13–23 proves that its \(-\infty\) set intersects the real cube in Lebesgue measure zero: the one-variable base follows by the local Riesz decomposition and uniform local integrability of \(\log|t-a|\). Hence \(F^{-1}(P)\) is null in \(V\). Smooth density in real-analytic coordinates is locally bounded above, and a countable atlas covers \(M\), proving the claim. QED.

**Boundary:** maximal total reality and real-analyticity are used for the holomorphic local complexification. This does **not** assert the same result for arbitrary smooth lower-dimensional real submanifolds, some of which can lie inside a pluripolar analytic set. This is an optional separate lemma, not a replacement or canonical duplicate of the original unitary statement.

## Validation, open issues, and user-directed exclusions

The exact small rational-tail checker accompanies this report; it verifies algebraic identities and some finite-parameter mass-concentration inequalities, **not** the measure-theoretic limiting proof. No full Pome build, tests, CI, browser rendering, formal verification, source/registry/tag change, or website publication was performed. The previously recorded §6.56 compact-center and §9.74 cycle-space findings were observed but **not counted again**; the cycle-space foundation remains an external input as already recorded. No theorem was newly shown false.

**Strict exclusion:** The user-deferred Demailly approximation/regularization programme and its dedicated Bergman, \(L^2\), Ohsawa–Takegoshi, multiscale-atlas, and positivity-loss proof-completion work remain **deferred-by-user**. In particular §6.55.2 after line 70 and §6.45.2's smoothing/current-product proof are *not* certified by this checkpoint. The historical ledger is preserved.
