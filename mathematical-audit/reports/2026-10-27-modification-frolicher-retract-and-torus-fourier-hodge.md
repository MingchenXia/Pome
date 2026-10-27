# Selected mathematical audit: Frölicher-page retracts under modifications and the cohomology of complex tori

**Date:** 2026-10-27. **Reviewed current main:** b6933b772f41b45918f7e25ed1afbbb1fd892272. **Starting review head:** 70608f5b76eda0322898690d69552a01a52c7d8a. **Branch:** review/mathematical-audit.

**Scope:** First selected proof-level review of integrated §10.87.1 and §10.81.1. The exact already-audited §10.84.1, §10.85.2 and smooth/current comparison §10.43.11 were reread only as stated dependencies; they are **not** counted as new section coverage. There are no changes to mathematical statements, proofs, source repositories, proof registry, canonicalization, permanent tags, main, CI or the published website. The dedicated Demailly approximation/regularization, Bergman, L², Ohsawa–Takegoshi, multiscale-atlas and positivity-loss programme is **deferred-by-user**, neither reopened nor certified.

## Reading-edition anchors and mathematical inputs

- §10.87, Theorem **10.87.1**, source label **demailly-complex-geometry-451F3847**, permanent tag **C4B9BA82F24B**; main <code>docs/sections/general-complex-cohomology-and-modifications--strong-hodge-structure-under-modifications/index.html</code>, blob <code>6414dd82e72d4af59e4706e105c4752501e9829f</code>, physical lines **7–27**: natural Bott–Chern-to-Dolbeault/de Rham maps at 7–13, statement at 17, pushforward and smooth/current comparisons at 23, current-level identity on modifications at 25, strong Hodge descent at 27. The local standing bidegree and double-complex conventions are in <code>docs/sections/general-complex-cohomology-and-modifications/index.html</code>, blob <code>09afe450589f7169d2f2296d0606882b11efec60</code>, lines **5–9**.
- §10.84, Theorem **10.84.1**, source **demailly-complex-geometry-3389B9E4**, permanent **F105D4917B45**, main <code>docs/sections/general-complex-cohomology-and-modifications--the-frolicher-filtration/index.html</code>, blob <code>ca98ecdb53f2ec77b439fdeb826dfa1dc6c60bdc</code>, physical lines **8–18, 25–43**. In particular, the exact total-degree page-loss identity is at lines 27–33. This was already selected and reported on 2026-10-26, not a new coverage claim.
- §10.85, Theorem **10.85.2**, source **demailly-complex-geometry-6E4A6CC9**, permanent **72D73EDC0883**, main <code>docs/sections/general-complex-cohomology-and-modifications--bott-chern-and-aeppli-comparison/index.html</code>, blob <code>d47c823a457ed5daa1b8b0a5cdfae06f65f86980</code>, physical lines **29–39**. Smooth/current Dolbeault comparison **§10.43.11** is the filtered \(E_1\)-comparison input. Neither was independently re-proved here.
- §10.81, Example **10.81.1**, source **demailly-complex-geometry-B6799A76**, permanent **EA6824E4DE53**, main <code>docs/sections/compact-curves-periods-and-complex-tori--complex-lattice-quotients/index.html</code>, blob <code>bf4f45ec25bac897ca8248be581a52ef82f4e62f</code>, physical lines **8–14**: full real lattice, complex charts and constant positive Kähler metric. Kähler strong Hodge input: §10.47.13, permanent **8719651E2EA0**, cited directly at §10.87 line 27.

## POME-MODIFICATION-FROLICHER-PAGE-SPLIT-001

**Severity:** low. **Status:** verified conditional deduction. **Not** a false printed theorem or an unconditional transitive proof certification.

**Statement.** If \(\mu:\widetilde X\to X\) is a modification of compact complex manifolds as in Theorem 10.87.1, then for **every** Frölicher page \(r\ge1\), every bidegree \((p,q)\), and every total degree \(k\), the canonical pullback is a split injection
\[
 E_r^{p,q}(X)\hookrightarrow E_r^{p,q}(\widetilde X).
\]
The retraction is obtained from pushforward of currents and the canonical smooth/current comparison. If \(t_r^k\) is the total rank of \(d_r\) leaving total degree \(k\), and \(e_r^k=\sum_{p+q=k}\dim E_r^{p,q}\), then
\[
 \dim E_r^{p,q}(X)\le \dim E_r^{p,q}(\widetilde X),\quad
 t_r^k(X)\le t_r^k(\widetilde X),\quad
 e_r^k(X)-b_k(X)\le e_r^k(\widetilde X)-b_k(\widetilde X).
\]
In particular the **Frölicher defect** \(D_k=\sum_{p+q=k}h^{p,q}-b_k\) cannot decrease on passing from \(X\) to \(\widetilde X\). All inequalities include \(r=1\), zero bidegrees, and arbitrary compact complex (not necessarily Kähler) source and target.

**Complete deduction at the named dependency level.** Give the smooth de Rham bicomplex \(\mathcal A(X)\) the finite decreasing filtration \(F^p\) by holomorphic bidegree, as in §10.84.1. Give currents \(\mathcal D(X)\) the identical filtration. The inclusion \(\iota_X:\mathcal A(X)\to\mathcal D(X)\) is a filtered chain map which is an isomorphism on \(E_1\), because \(E_1\) is Dolbeault cohomology and smooth/current Dolbeault comparison §10.43.11 is an isomorphism. Therefore it is an isomorphism on **every** \(E_r\), including the limiting page, by taking cohomology page by page. The same holds on \(\widetilde X\).

Smooth pullback \(\mu^*:\mathcal A(X)\to\mathcal A(\widetilde X)\) and current pushforward \(\mu_*:\mathcal D(\widetilde X)\to\mathcal D(X)\) preserve bidegree and commute with \(\partial,\bar\partial\). Since a modification has multiplicity one on its dense biholomorphic locus, §10.87.1 line 25 proves the **chain-level**, not merely cohomological, identity
\[
 \mu_*\iota_{\widetilde X}\mu^*=\iota_X
 \qquad\text{on all smooth differential forms on }X.
\]
Transport the current pushforward to the smooth Frölicher pages via the isomorphisms \(\iota_{X,r}\) and \(\iota_{\widetilde X,r}\), obtaining
\[
 R_r=\iota_{X,r}^{-1}\mu_{*,r}\iota_{\widetilde X,r}.
\]
The chain-level identity gives \(R_r\mu_r^*=\mathrm{id}_{E_r(X)}\). All maps commute with \(d_r\), so
\[
 (E_r(\widetilde X),d_r)
   =\mu_r^*(E_r(X),d_r)\oplus(\ker R_r,d_r)
\]
as complexes, not merely as vector spaces. Consequently pagewise dimensions and outgoing differential ranks split additively. Taking the next cohomology page identifies \(\ker R_{r+1}\) with the cohomology of \((\ker R_r,d_r)\). Its total-degree dimensions can only decrease with page number, by the nonnegative rank-loss identity of §10.84.1, lines 27–33. At \(E_\infty\), the total-degree dimensions equal Betti numbers. Hence
\[
 [e_r^k(\widetilde X)-b_k(\widetilde X)]
 -[e_r^k(X)-b_k(X)]
 =e_r^k(\ker R_r)-e_\infty^k(\ker R_\infty)\ge0.
\]
This also proves the asserted inequalities on ranks and on each bidegree.

**Required inputs and limits:** §10.87.1 current-level multiplicity-one identity and pushforward rules, §10.43.11 global smooth/current Dolbeault comparison, §10.84.1 finite filtered spectral sequence. We did not independently establish the cited current comparison or general spectral-sequence construction. No sequential compactness or unstated interchange of limits is used; this is a finite-length spectral-sequence argument. The result does not assert that Frölicher degeneration or strong Hodge decomposition automatically **ascends** under a modification.

**Proposed edit:** Optional precise corollary after Theorem 10.87.1, not a change to the theorem. **Affected dependents:** invariance and comparison questions for Frölicher pages, Hodge-number growth, de Rham and Bott–Chern behavior under compact modifications.

## POME-FUJIKI-ODD-BETTI-OBSTRUCTION-001

**Severity:** low. **Status:** verified conditional deduction, with explicit compact complex counterexample to a possible overextension of the Fujiki-class conclusion; the printed Theorem 10.87.1 is correct.

**Statement and proof.** If \(X\) is in Fujiki class \((\mathcal C)\) in the precise sense of §10.87 (it admits a compact Kähler modification), every **odd Betti number** \(b_{2j+1}(X)\) is even. Theorem 10.87.1 gives a canonical pure-type de Rham direct sum and conjugation switches \((p,q)\) with \((q,p)\). For odd \(p+q\), no pair has \(p=q\). Therefore
\[
 b_{2j+1}(X)=
 2\sum_{\substack{p<q\\p+q=2j+1}}
 \dim H^{p,q}_{\mathrm{BC}}(X)\in 2\mathbb Z.
\]
This is a necessary condition, not a characterization of Fujiki class.

For an explicit obstruction, the scalar primary Hopf surface
\[
 H=(\mathbb C^2\setminus\{0\})/\langle z\mapsto 2z\rangle
\]
is diffeomorphic to \(S^3\times S^1\) by \(z\mapsto(z/\|z\|,\log_2\|z\|\bmod\mathbb Z)\). Hence \(b_1(H)=b_3(H)=1\); it admits **no Kähler modification**. The diffeomorphism and cohomology are elementary, so this supplies an independent concrete obstruction rather than invoking a non-Kähler classification theorem.

**Proposed edit:** Optional corollary/remark adjacent to §10.87.1; relevant to compact modification criteria and Hopf/LCK examples. **Not** a proof of the converse, or a review of the unrelated Demailly regularization programme.

## POME-COMPLEX-TORUS-FOURIER-DOLBEAULT-001

**Severity:** low. **Status:** verified conditional deduction. The original Example 10.81.1 is correct.

**Statement.** Under precisely Example 10.81.1's hypothesis that \(\Gamma\subset\mathbb C^n\) is the integer span of a real basis, set \(X=\mathbb C^n/\Gamma\). For every \(0\le p,q\le n\),
\[
 H_{\bar\partial}^{p,q}(X)
 \simeq\bigwedge^p(\mathbb C^n)^{*(1,0)}
 \otimes\bigwedge^q(\mathbb C^n)^{*(0,1)},\quad
 h^{p,q}=\binom np\binom nq,\quad b_k=\binom{2n}k.
\]
These are **canonical constant-form representatives** after the given affine torus structure is fixed. Via its Kähler metric and the strong Hodge theorem (§10.47.13), also \(h_{\mathrm{BC}}^{p,q}=\binom np\binom nq\). All formulas include \(n=0\).

**Direct Fourier proof, independent of analytic approximation/regularization.** Fix real coordinates on \(V_{\mathbb R}/\Gamma\) induced by the lattice basis and let \(\Gamma^*\) be the integral dual frequency lattice. A smooth form \(\alpha\) has Fourier expansion \(\sum_{m\in\Gamma^*}e^{2\pi i m(x)}\alpha_m\) with constant coefficient forms \(\alpha_m\). Repeated integration by parts gives rapid coefficient decay, allowing termwise differentiation and multiplication by order-\(-1\) frequency symbols. The complex structure is translation invariant, so on the \(m\)-th Fourier component,
\[
 \bar\partial_m=\eta_m\wedge,\qquad
 \eta_m=(2\pi i\,dm)^{0,1}.
\]
For \(m\ne0\), the real covector \(dm\) has nonzero \((0,1)\)-part. Choose contraction \(\iota_{v_m}\) with \(\eta_m(v_m)=1\) and \(\|\iota_{v_m}\|\le C/\|m\|\) for a fixed Euclidean norm. Exterior algebra gives
\[
 (\eta_m\wedge)\iota_{v_m}+\iota_{v_m}(\eta_m\wedge)=\mathrm{id}.
\]
Thus the \(m\ne0\) Dolbeault subcomplex is contractible. The order-\(-1\) bound preserves rapid Fourier decay, so the contractions assemble into a homotopy on smooth global forms. At \(m=0\), \(\bar\partial=0\), giving exactly the constant \((p,q)\)-forms and their stated dimensions. Replacing \(\eta_m\) by the full \(2\pi i\,dm\) gives the identical de Rham contraction and all constant real forms, hence \(b_k=\binom{2n}k\). The Kähler conclusion follows from the actual constant positive Hermitian metric in Example 10.81.1, not from a stronger assumption on the lattice.

**Inputs and limits:** elementary Fourier series of smooth periodic functions and the printed Kähler/strong Hodge theorem for the Bott–Chern identification. This is not a numerical test, a formal proof, or a certification of all upstream Hodge theory. **Proposed edit:** Optional worked example after §10.81.1. **Affected dependents:** compact-torus Dolbeault/Hodge dimension examples, Frölicher page examples, integral-period discussions and BC dimension comparisons.

## Actual verification and coverage boundaries

Directly reread the integrated statement and proof §10.87.1 lines 7–27: verified bidegree preservation, multiplicity-one identity, smooth/current BC comparison use, split-map argument, and the distinction between a canonical pure-type de Rham sum and an arbitrary splitting of the Frölicher filtration. Checked the actual full-lattice quotient and constant Kähler form in §10.81.1 lines 8–14, and supplied a nonzero-frequency contracting homotopy. The §10.84 page-loss algebra and §10.85 current comparison were **context/dependency crosschecks only**, having been recorded in an earlier run.

**First newly selected inventory rows:** exactly **§10.81 and §10.87**. The current 747-section ToC matrix retains its original keys; no entire section, full chapter, or entire transitive dependency chain has been certified. No new confirmed false theorem, proof gap, external citation failure or genuine duplicate was established in these selected passages. Pre-existing confirmed errors, unresolved dependencies, verified repairs and author-deferred items remain unchanged. PR #9 is already **closed and merged**; no new PR or issue is opened.

**Execution:** mathematical reasoning and live GitHub source/blob checks only. No executable mathematical tests, project builds, CI, formal verification, or website publication were performed. 