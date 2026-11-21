# Cross-chapter audit: conformal Gauduchon response, transverse duality, and local models

**Date:** 2026-11-21. **Reviewed current main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. This audit reads the **integrated HTML reading edition**. It adds two conditional mathematical deductions and records one genuinely external valuation-realization input. None is a counterexample to a printed theorem or a complete certification of its upstream proof chain. All source, registry, tag, main, and website edits remain outside this audit branch.

## Exact direct coverage

| Section and current integrated file | Blob / mathematical lines | Direct review |
| --- | --- | --- |
| §5.4, `docs/sections/complex-differential-forms-and-positive-currents--local-potentials-for-closed-1-1-currents/index.html` | `acfdd3d1e174fdb55473771b42e7e33b6f17ea18`, 5–135 | Hermitian coefficient/trace normalization and closedness identities (5.4.1), one-variable Cauchy kernel, parameterwise Dolbeault solution, Poincaré homotopy formula, distributional local potentials, pluriharmonic uniqueness, pullback and connected-component alternative (§5.4.2–4) |
| §9.8, `docs/sections/complex-spaces-and-modifications--connected-fibers-and-resolution-models/index.html` | `6ad8bec31c3089b7eab91f199f5a1eb355a12c40`, 5–81 | Proper connected-fiber argument, normal finite bimeromorphic factorization, codimension-two exceptional image, uniqueness of strict transforms, graph closure/common smooth model, smooth-center common refinement conditional on Hironaka |
| §11.4, `docs/sections/gauduchon-metrics-and-linear-mass--conformal-gauduchon-metrics/index.html` | `ecb4bf9e593dfb25f1644f0561d1aa65bf096b10`, 5–61 | Elliptic index, one-dimensional adjoint nullspace, sign from maximum principle, strong minimum principle, conformal exponent and trace normalization |
| §11.8, `docs/sections/gauduchon-metrics-and-linear-mass--transverse-concentration-of-gauduchon-tests/index.html` | `93c2b63848b752f3ef660c1bcd599d0be1bc1e40`, 5–85 | Transverse approximate identity, Lamari dual separation, normalized-psh compactness, Siu analytic locus, local Cartier converse, uniform lower Hessian estimate and chart-support caveat |

**Selected supporting statements, not whole-section reviews:** §11.6, `docs/sections/gauduchon-metrics-and-linear-mass--the-gauduchon-criterion-for-positivity/index.html`, blob `6dd43b62800206fb0302fd4261372d7882e5170d`, lines 11–73 and 82–96 (Theorem 11.6.1 and Corollary 11.6.2); §19.3, `docs/sections/the-theory-of-okounkov-bodies--flags-and-valuations/index.html`, blob `9190d2ae0d3e51ca0ca965000cb9b5b2ec965c85`, lines 17–43 and 379–387 (Remarks 19.3.3 and 19.3.23); §19.4, `docs/sections/the-theory-of-okounkov-bodies--algebraic-partial-okounkov-bodies/index.html`, blob `c661e264cab0995a2a344453039940028feff8e0`, lines 59–67 (Proposition 19.4.7, Step 1). §19.3 already received a complete direct review on 2026-11-20; the present selected revisit is **not** additional whole-section coverage. No excluded approximation/Bergman/L2/OT programme was opened.

## POME-GAUDUCHON-CONFORMAL-FAMILY-SMOOTHNESS-001

**Status:** verified conditional deduction; **severity:** low; **printed theorem:** unchanged. **Primary anchor:** Theorem 11.4.2, source `non-kahler-pluripotential-theory:F1B1A709`, permanent `3978AEB15BD7`, lines 20–57, especially the adjoint-kernel proof at 29–56. **Dependents:** Gauduchon trace duality, normalized adjoint measures and Hermitian mass estimates for smoothly varying Hermitian backgrounds (§§11.5–11.7 and related later applications).

**Statement.** Let \(X\) be connected and compact of complex dimension \(n\ge2\), and let \(\eta_t\) be a smooth one-parameter family of smooth positive Hermitian forms on a parameter interval \(I\). The uniquely normalized positive Gauduchon density
\[
  dd^c(\rho_t\eta_t^{n-1})=0,\qquad \int_X\rho_t\eta_t^n=1
\tag{1}
\]
depends smoothly on \((t,x)\). With a dot denoting differentiation at \(t=t_0\), its derivative is **uniquely characterized** by
\[
 dd^c\!\left(\dot\rho\,\eta^{n-1}+(n-1)\rho\,\eta^{n-2}\wedge\dot\eta\right)=0,
 \qquad
 \int_X\!\left(\dot\rho\,\eta^n+n\rho\,\dot\eta\wedge\eta^{n-1}\right)=0.
\tag{2}
\]
Thus the normalized map \(\eta\mapsto\rho_\eta\), and \(\eta\mapsto\rho_\eta^{1/(n-1)}\eta\), is locally smooth in the standard \(C^{k,\alpha}\)-Banach scales of sufficiently high regularity; no invariance under the unnormalized conformal scaling of \(\eta\) is asserted.

**Proof, conditional on the same Fredholm and Schauder/elliptic machinery as Theorem 11.4.2.** Fix \(k\ge0\), \(0<\alpha<1\), and a fixed positive volume form \(dV\). For each smooth positive \(\eta\) consider the linear operator
\[
 Q_\eta:C^{k+2,\alpha}(X)\longrightarrow
    \left\{f\,dV:f\in C^{k,\alpha}(X),\ \int_X f\,dV=0\right\},
 \qquad Q_\eta(a)=dd^c(a\eta^{n-1}).
\]
The image has zero integral by Stokes. The formal adjoint is the second-order operator \(L_\eta\) in lines 29–38, up to its harmless positive constant and volume-form identification. That operator has constant kernel by the maximum principle. The Fredholm alternative therefore makes \(Q_\eta\) **onto the mean-zero top forms**; its kernel is the one-dimensional span of the strictly positive \(\rho_\eta\) from Theorem 11.4.2. Hence
\[
 A_\eta(a)=\left(Q_\eta(a),\int_Xa\,\eta^n\right)
\]
is a bounded linear isomorphism from \(C^{k+2,\alpha}(X)\) onto the above mean-zero forms times \(\mathbb R\): its kernel is zero since \(\int_X\rho_\eta\eta^n>0\). Surjectivity follows by correcting any \(Q_\eta\)-preimage by a scalar multiple of \(\rho_\eta\). The coefficients of \(A_\eta\) depend smoothly on a smooth parameter \(\eta_t\), so the bounded inverse depends smoothly on \(t\) wherever invertibility holds. In particular
\(\rho_t=A_{\eta_t}^{-1}(0,1)\) is a smooth \(C^{k+2,\alpha}\)-valued family. Taking arbitrarily high \(k\), elliptic regularity and compatibility of the unique normalized solutions give joint \(C^\infty\) regularity. Differentiating (1) gives (2). Conversely, the homogeneous version of (2) has \(\dot\rho\) in \(\ker Q_\eta\) with zero \(\eta^n\)-integral, hence \(\dot\rho=0\), proving uniqueness. This is an audit-only conditional stability corollary, not an independent construction of the Fredholm theory used by §11.4.

**Proposed action:** optionally state (1)–(2) as a parameter-response lemma, preserving the original Gauduchon attribution and theorem. **Uncertified dependency:** index-zero scalar elliptic Fredholm theory, regularity of the bounded inverse in the parameter, and the maximum principle; these do not become fully certified by this derivative argument.

## POME-GAUD-TRANSVERSE-DUAL-THRESHOLD-001

**Status:** verified conditional deduction; **severity:** low; **printed results:** unchanged. **Anchors:** §11.8, lines 10–22 (\(B_\delta,C_\delta\)); Theorem 11.8.1, source `non-kahler-pluripotential-theory:8F4DC027`, permanent `B0762464DCDC`, lines 26–51; Proposition 11.8.2, source `non-kahler-pluripotential-theory:79BF143E`, permanent `26C9605156BE`, lines 56–81; supporting Theorem 11.6.1, source `non-kahler-pluripotential-theory:87DC00D0`, permanent `88BE3B63D9E5`, lines 11–73.

**Statement.** Retain **exactly** the chart, cutoff, smooth nonnegative density and Gauduchon test normalization of §11.8, with \(\omega>0\). For any sufficiently small fixed \(\delta>0\), \(0<C_\delta<\infty\) and
\[
 \boxed{\sup\{\lambda\ge0:\ \exists u\in\mathrm{PSH}(X,\omega)
 \text{ with }\omega+dd^cu\ge\lambda B_\delta\}=C_\delta^{-1}.}
\tag{3}
\]
The supremum in (3) is *attained*: there exists a normalized global \(\omega\)-psh potential for the exact coefficient \(1/C_\delta\). If \(X\) has no analytic hypersurface then the sharp achievable transverse coefficient tends to \(0\) as \(\delta\downarrow0\). If an effective Cartier divisor agrees with \(\{\zeta=0\}\) with multiplicity one on the **entire cutoff chart**, the exact coefficient remains bounded below by the explicit positive constant \(\epsilon/(4\|p\|_\infty)\) of Proposition 11.8.2. No converse at singular crossings is claimed.

**Proof.** \(C_\delta<\infty\) follows from the smooth pointwise upper bound \(B_\delta\le M_\delta\omega\) and normalization \(\int\omega\wedge\Theta=1\). It is strictly positive because \(B_\delta\not\equiv0\) and any smooth strictly positive normalized Gauduchon test \(\Theta\) integrates it positively. If \(\omega+dd^cu\ge\lambda B_\delta\), integration against every Gauduchon test and \(dd^c\Theta=0\) yield \(1\ge\lambda\int B_\delta\wedge\Theta\), so \(\lambda C_\delta\le1\). Conversely, for \(\lambda=1/C_\delta\) the same inequality gives
\[
 \int_X(\omega-\lambda B_\delta)\wedge\Theta\ge0
\]
for **all** smooth positive Gauduchon tests, using their scale normalization. The generalized Lamari criterion (§11.6.1) produces \(u\) with \(\omega-\lambda B_\delta+dd^cu\ge0\); adding a constant makes \(\sup_Xu=0\). Thus (3) holds with attainment. The two geometric consequences are exactly the conditional implications of §§11.8.1 and 11.8.2, with the constants and chart restriction preserved.

**Proposed action:** optional exact dual-threshold corollary; do not modify §11.8 in this branch. **Uncertified inputs:** generalized Lamari separation, global normalized-psh compactness, Siu analyticity; this proof does not certify their transitive dependencies. The existing 2026-11-15 entire-graph example is not counted again.

## POME-OKOUNKOV-FLAG-REALIZATION-EXTERNAL-001

**Status:** external dependency; **severity:** medium (used to reduce arbitrary maximal-rank valuations to flags); **not** a false theorem and **not** a duplicate of the 2026-11-19 semigroup-counting input. **Anchors:** §19.3 Remark 19.3.3, source `sgpt:00F064E7`, permanent `5AA6A085DBB0`, lines 42–43; Remark 19.3.23, source `sgpt:0BC30008`, permanent `53FF6E808B22`, lines 379–387; Proposition 19.4.7 Step 1, source/label within §19.4, permanent `632B1323B741`, lines 59–67. Reviewed §19.3 current blob `9190d2ae0d3e51ca0ca965000cb9b5b2ec965c85`, §19.4 blob `c661e264cab0995a2a344453039940028feff8e0`.

The claim that any surjective rank-\(n\) valuation with ordered value group \(\mathbb Z^n_{\rm lex}\) is equivalent, by an order-preserving unitriangular integral matrix, to a flag valuation **on a modification** is explicitly imported from **[Theorem 2.9, CFKLRS17]** at §19.3.3. It is used as an existence premise in §19.3.23 and in the “without loss of generality flag” step of §19.4.7. The elementary unitriangular matrix multiplication in §§19.3.14/.17/.22 proves the *compatibility and independence after a flag model exists*, not the realization of an arbitrary valuation by a flag model. Hironaka resolution alone has not been shown by this integrated text to imply the claimed realization. This is a genuine mathematical input, not merely historical attribution; retain its named citation.

**Precisely missing step:** for an arbitrary such valuation \(\nu\), produce a smooth birational model \(Z\to X\), a smooth admissible flag \(W_\bullet\) on \(Z\), and \(G\in\operatorname{Aut}(\mathbb Z^n_{\rm lex})\) satisfying \(\nu=\nu_{W_\bullet}G\) as valuations on \(\mathbb C(X)^\times\). The present pass does not supply this construction, and it **does not** classify the cited result as false. For the **conditional special case** where such \(Z,W_\bullet,G\) are already given, the downstream matrix transport §§19.3.14/.17/.22 applies without that existence theorem. In §19.4.7 one must in addition explicitly compare pulled-back sections and their valuation vectors before changing the projective model; this is an obligation to spell out, not an established error.

**Proposed action:** track a separately scoped proof or precise internal lemma for valuation realization and birational section correspondence, preserving the [CFKLRS17] historical citation. Do not move this finding into the excluded Demailly regularization programme. §§19.3 and 19.4 were **not** newly reviewed in full this run.

## Classification, dependencies, and cumulative boundaries

**New findings this session:** two low-severity verified *conditional deductions*, one medium-severity genuine *external dependency*. **New confirmed false printed statements: zero.** The four current direct section readings are not claimed as historical first visits, and none proves the complete transitive dependencies of a chapter. The existing separate §19.3 full review of 2026-11-20 remains intact. We detected no new exact mathematical duplication warranting a canonical-tag change; §11.8's exact optimizer follows §11.6 but is a specialized quantitative consequence, not a replacement for the earlier [whole-graph] example.

**Upstream still unverified:** §5.4 uses Riesz/fundamental solution, smooth \(\bar\partial\) homotopy and Weyl's lemma; §9.8 uses proper-image analytic geometry, normality and (only where appropriate) permitted Hironaka resolution/principalization; §11.4 uses scalar elliptic Fredholm and maximum principles; §11.8 uses Lamari separation, psh \(L^1\) compactness, and Siu's theorem; §19.3.3 uses CFKLRS17. **Exclusions:** Demailly approximation/regularization, its Bergman, \(L^2\), Ohsawa–Takegoshi, multiscale-atlas and positivity-loss completion programmes remain **deferred-by-user**, not resolved, repaired or certified. If another result depends on those inputs, record but do not reopen them. No tests, computations, builds, CI, automated publication, main/source/registry/tag/site modifications were performed.
