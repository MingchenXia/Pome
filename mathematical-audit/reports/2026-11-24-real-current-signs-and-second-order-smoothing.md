# Audit: real-current signs and second-order variable-kernel smoothing
**Date:** 2026-11-24 (Asia/Shanghai)  
**Reviewed integrated main:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`  
**Audit branch:** \`review/mathematical-audit\`  
**Scope:** Complete current mathematical text of §§5.53–5.55; §5.52 has headings only, without mathematical claims; a selected repeat verification of previously completely read §4.5. No historical first-visit assertion. No full transitive proof-chain certification.

## 1. Verified conditional deduction — POME-REAL-CURRENT-RADIAL-SMOOTHING-SECOND-ORDER-001

**Severity:** low. **Status:** verified conditional deduction, *not* an error in the printed theorem.  
**Precise source:** \`docs/sections/real-currents-submersions-and-homotopies--global-smoothing-and-the-poincare-lemma-for-currents/index.html\`, main blob \`597a770e3f087693b98968c6e5fcf8bcd9ca0841\`, Lemma 5.54.1 (source \`demailly-complex-geometry:7A345420\`, permanent \`A748F8312A04\`, physical lines 11–35), Theorem 5.54.2 (source \`demailly-complex-geometry:C92BDA92\`, permanent \`7D93F6AD9C80\`, physical lines 40–81), particularly the explicit averaged pushforward formula at lines 51–54.  
**Dependencies:** the diffeomorphism \`F_v(x)=x+psi(x)v\` of Lemma 5.54.1, the direct-image definition from Theorem 5.53.1, and elementary Taylor's formula. The construction of \`R_epsilon\` is used exactly as printed; no excluded approximation or external analytic theorem is used.

Choose the radial mollifier in Theorem 5.54.2 to be a *fixed rescaling* \(\rho_\varepsilon(v)=\varepsilon^{-m}\rho(v/\varepsilon)\), where \(\rho\in C_c^\infty(B(0,1))\) is radial, nonnegative and of integral one. Let \(M_k=\int_{\mathbb R^m}|v|^k\rho(v)\,dv\), \(M_2>0\), and \(\kappa_\rho=M_2/(2m)\). Let \(\mu\) be a finite signed Radon measure on \(\Omega\subset\mathbb R^m\), viewed as a **degree-\(m\)** current; let \(\psi\) be the smooth function provided by Lemma 5.54.1. Then, for every \(\phi\in C_c^\infty(\Omega)\),

\[
|\langle R_\varepsilon\mu-\mu,\phi\rangle|
\le \frac{M_2\varepsilon^2}{2}\|\psi\|_\infty^2
|\mu|(\Omega)\|D^2\phi\|_{\rm op,\infty}.
\tag{1}
\]

Moreover,
\[
\varepsilon^{-2}(R_\varepsilon\mu-\mu)
\ \longrightarrow\ \kappa_\rho\Delta(\psi^2\mu)
\quad\text{in }\mathcal D'(\Omega),
\tag{2}
\]
with the explicit remainder
\[
\left|\varepsilon^{-2}\langle R_\varepsilon\mu-\mu,\phi\rangle
-\kappa_\rho\int_\Omega\psi^2\Delta\phi\,d\mu\right|
\le \frac{M_3\varepsilon}{6}\|\psi\|_\infty^3
|\mu|(\Omega)\|D^3\phi\|_{\rm op,\infty}.
\tag{3}
\]

The limiting operator is the **distributional Laplacian of \(\psi^2\mu\)**, not \(\psi^2\Delta\mu\). In particular it records the spatially variable smoothing radius. Formula (2) does not assert second-order convergence in total variation or a uniform second-order Wasserstein estimate.

**Proof.** For a degree-\(m\) current, the test form has degree zero. The explicit construction (lines 51–54) and the definition of pushforward yield
\[
\langle R_\varepsilon\mu,\phi\rangle
=\int_\Omega\int_{B(0,1)}
\phi(x+\varepsilon\psi(x)v)\rho(v)\,dv\,d\mu(x).
\]
The integral makes sense for a finite signed measure because \(\phi\) is bounded. Taylor's formula along the segment from \(x\) to \(x+\varepsilon\psi(x)v\), which remains in \(\Omega\) by Lemma 5.54.1, gives a linear term \(\varepsilon\psi(x)\nabla\phi(x)\cdot v\), a quadratic term
\(\frac12\varepsilon^2\psi(x)^2D^2\phi(x)[v,v]\), and a cubic remainder bounded by \(\varepsilon^3\|\psi\|_\infty^3|v|^3\|D^3\phi\|_{\rm op,\infty}/6\). Radiality gives \(\int v\rho(v)\,dv=0\) and \(\int v_i v_j\rho(v)\,dv=(M_2/m)\delta_{ij}\). The first-order cancellation and Taylor's second-order bound give (1); integrating the quadratic term gives (2) and (3). No interchange of two unbounded limits occurs: the remainder is uniform in \(x\) and integrable against \(|\mu|\).

The order \(\varepsilon^2\) cannot generally be improved: take \(\mu=\delta_{x_0}\) at an interior point with \(\psi(x_0)>0\) and a compactly supported test \(\phi\) equal to \(|x-x_0|^2\) near \(x_0\). For all sufficiently small \(\varepsilon\),
\[
\langle R_\varepsilon\mu-\mu,\phi\rangle
=M_2\psi(x_0)^2\varepsilon^2>0.
\]
For positive probability measures with finite first moment, the coupling \((x,x+\varepsilon\psi(x)v)\) also gives the *different*, first-order transportation estimate
\(W_1(R_\varepsilon\mu,\mu)\le\varepsilon\|\psi\|_\infty\le\varepsilon/4\).
This does not contradict the second-order weak-test cancellation.

**Proposed correction/addition:** Optional standalone remark after Theorem 5.54.2 describing (1)–(3) under a fixed radial scaling. No theorem text needs repair. **Dependents:** distributional test-error analyses based on §5.54.2, but no dependent theorem is asserted to improve without checking its own hypotheses. **Limitations:** \(\rho_\varepsilon\) must be chosen with a fixed radial profile to assert the specific normalized limit (2); the printed theorem permits more general approximate identities.

## 2. Real pushforward, submersion and Stokes sign checks

- **§5.53.1**, \`docs/sections/real-currents-submersions-and-homotopies--currents-on-real-manifolds-and-fiber-signs/index.html\`, blob \`188386272430128f7ae086f28d5e685ce45dec3c\`, source \`demailly-complex-geometry:710BD6AD\`, permanent \`CCE8A237C582\`, lines 7–46: for a current of dimension \(p\), the direct-image differential sign is \((-1)^{(m_2-p+1)-(m_1-p+1)}=(-1)^{m_1-m_2}\), as printed. The cylinder convention at lines 33–45 produces the stated endpoint signs, including the degree-zero interval test.
- **§5.53.2**, same file, source \`demailly-complex-geometry:DC0D446B\`, permanent \`01AAD02BF915\`, lines 51–78: the fiber-first orientation yields \(\int F^*t\wedge\phi=(-1)^{rq}\int t\wedge F_*\phi\); the extra factor \((-1)^{rq}\) in current pullback is essential. Real relative dimension is even for complex submersions, so this factor is then \(1\). No mismatch detected.
- **§5.55.1**, \`docs/sections/real-currents-submersions-and-homotopies--integration-over-real-submanifolds/index.html\`, blob \`09cf11ebb628e7a198bbe84befd8d5c68ead5854\`, source \`demailly-complex-geometry:25F759A0\`, permanent \`E09F702EB680\`, lines 8–41: for an oriented \(p\)-submanifold with boundary in ambient dimension \(m\), \(\mathrm d[Z]=(-1)^{m-p+1}[\partial Z]\). Combining with §5.53.1 gives \(\mathrm d(F_*[Z])=(-1)^{m_2-p+1}F_*[\partial Z]\), consistent with the target-degree sign. The outward-normal-first interval check agrees with the printed formula. The proof uses \(C^1\) approximation of coordinate charts, not an unjustified smooth pullback of a merely \(C^1\) chart.

These are direct local checks, **not** a complete certification of source-current theory or of all hypotheses in subsequent applications. No new false printed theorem or proof gap established here.

## 3. Distinct repeat-only classical reading

**§4.5**, \`docs/sections/green-energy-and-martin-boundaries/index.html\`, blob \`976a90f2a5eba299658f73a1eee8b9d3fef8020f\`, lines 7–213, had already been read completely on 2026-11-22 and is not new coverage. This session rechecked the signed-energy definiteness argument (§4.5.2, lines 23–30), positive-cone completion and failure of signed completeness (§4.5.4–5, lines 47–72), and the order of compactness/metrizability in the Martin construction (§4.5.8–12, lines 95–185). No new independent finding arose; the earlier source labels and prior audit evidence are preserved. The Martin representation and all its topological prerequisites are not here re-certified transitively.

## 4. Audit accounting and exclusions

- Direct full current mathematics: §§5.53, 5.54, 5.55 (**three** sections); §5.52 is a heading-only parent, not a theorem review.
- Repeat-only: selected §4.5; **not** counted as a fresh entire section.
- New: one low-severity **verified conditional deduction**; zero newly confirmed printed errors; zero newly confirmed proof gaps; zero complete upstream proof-chain certifications.
- The longstanding Demailly approximation/regularization, dedicated Bergman, \(L^2\), Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof-completion programmes are **deferred-by-user, not resolved/certified**. The fact that the checked real smoothing operator is also sometimes called regularization does *not* reopen that excluded programme: §5.54 is a separate, elementary real-current convolution/homotopy construction, and this report does not touch Demailly's positivity-controlled psh approximation.
- No build, tests, GitHub Actions, publication, main changes, source-body changes, registry edits, or tag changes.
