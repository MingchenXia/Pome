# 2026-10-24 — new Gauduchon integrated-math defects and adjoint gradient-map injectivity

**Freshly reviewed main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`; **preserved initial review head:** `483af246c8dd314ccd5da749929aa4feab949363`. Freshly read main AGENTS.md and documentation/proof-expansions.md, review branch README.md, LATEST.md, cumulative ledger and exact current chapter 14 table of contents. [Dated complete mathematical audit with pinned integrated HTML tags/lines](reports/2026-10-24-gauduchon-multiline-tags-and-adjoint-monotonicity.md).

- **POME-GAUD-ALIGN-SPLIT-001 — medium / confirmed integration error:** equations 14.13.3, 14.14.5, 14.14.10 exist as full multiline displays in the selected section proofs, but have separately addressable **incomplete** tail-only tags A6EC7DDEACFB, 143977813E90, D807F632DAD7; individual tag pages have malformed nested `aligned/align` math. Preserve all permanent tags while mapping them to the canonical **full** displays; no source patch or merge performed.
- **POME-GAUD-SECOND-DERIV-GLYPH-001 — low / confirmed mathematical-notation defect:** unicode U+201D appears in place of `\phi''` and `\psi''` in equation 14.14.5 and another `\phi''` in §14.14.12's cancellation. Proposed exact TeX replacements; not a counterexample to the intended Hessian estimate.
- **POME-GAUD-ADJOINT-GRADIENT-MONO-001 — low / verified conditional deduction:** the smooth normalized Gauduchon adjoint probability map `F -> mu_F` is strictly monotone/injective modulo constants. For `H=G-F`, its exact pairing `integral H d(mu_G-mu_F)` equals the positive integral of the Hessian square along the smooth solution path; a positive Bregman-divergence formula follows. Assumes existing smooth existence, connectedness and adjoint-kernel theorems; not unconditional PDE certification.
- **Actual first selected proof-level coverage:** previously inventory-only §§14.13–14.18, including matrix weights, eigenvalue/torsion estimate passages, Liouville cone maximality, blowup scaling, concave elliptic extension and adjoint scalar variation. The external Evans–Krylov/Schauder prerequisites and full hardest estimates remain **unverified**, not falsely labeled correct. The `section 25.6` locator in §14.17.1 is a **candidate stale source-reference** for later semantic checking, not a confirmed mathematical flaw in this run.
- **Writes:** new English report, one small read-only reproduction script, ledger, coverage matrix and this checkpoint **only** on `review/mathematical-audit`. No main/source/body/registry/tag modifications, publication, CI, complete build, or formal verification. Dedicated Demailly approximation/regularization, Bergman/L²/Ohsawa–Takegoshi/multiscale/positivity-loss remain **deferred-by-user**, neither solved nor reopened.

---

# 2026-10-24 — sharp global stability of real-convex logarithmic extremals

**Freshly reviewed main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. **Starting review head:** `e543f66bdfa7475a80d56233c6d3c02584334469`. Freshly re-read main `AGENTS.md`, `documentation/proof-expansions.md`, review-branch `README.md` and prior `mathematical-audit/LATEST.md`, the existing ledger, 747-row ToC coverage matrix, and the actual integrated HTML sources. [Complete English source-anchored report](reports/2026-10-24-real-convex-extremals-sharp-hausdorff-stability.md).

- **POME-REALCONVEX-SCALE-001 — low / verified conditional deduction, NOT a false theorem.** For compact symmetric real convex bodies \(E\) with \(0\) in the real interior, the exact **global** displacement \(\|V_{sE}-V_E\|_\infty=\operatorname{arcosh}(1/s)\) for \(0<s\le1\). Equality is attained at **every real boundary point of \(E\)**. The proof uses the slit-plane harmonic maximum/minimum principles for \(g=V_{[-1,1]}\) and the integrated real-polar extremal formula, without an approximation theorem.
- **POME-REALCONVEX-HAUS-001 — low / verified conditional deduction, NOT a proof gap.** Centrally symmetric real convex \(E,F\) sharing a radius-\(r\) inball have \(\|V_E-V_F\|_\infty\le\operatorname{arcosh}(1+d_H(E,F)/r)\). Equality occurs for concentric balls of radii \(r\) and \(r+\varepsilon\), so the **half-Hölder exponent is optimal**. Consequent multiplicative control of the fixed-ball \(\alpha_B\) and exact Robin scaling \(c(sE)=s c(E)\) are distinguished from Bedford–Taylor capacity.
- **New actual proof coverage:** first selected direct proof review of §§16.30, 16.31 and 16.33 with source labels, permanent tags, blob SHAs and physical HTML line anchors recorded in report and ledger. §7.10.1–2 were also crosschecked as **context only**; previous findings are unchanged. Not a certification of whole sections, entire upstream domain-of-holomorphy/regularity arguments, the whole 747-section collection, or any computer/formal build.
- **Writes and limits:** only this report and the cumulative `LEDGER.md`, `SECTION_MATRIX.md` and `LATEST.md` on `review/mathematical-audit`. No changes to `main`, source mathematics, proof registry, canonicalization, tags, CI, website, PRs or merge. Dedicated Demailly approximation/regularization and Bergman/L²/Ohsawa–Takegoshi/multiscale/positivity-loss remain **deferred-by-user**, not resolved/certified and not reopened.

---

# 2026-10-24 — uniform L¹ density stability of adjoint supports; variation obstruction for Gauduchon traces

**Fresh main SHA:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. **Preserved review head at session start:** `ef0dc853b6c104d0ee6b63393751253c3d5f58a7`. Reviewed integrated §§11.31, 11.33–11.36 in selected proof detail; §11.32 standing assumptions only. [New full English proof report](reports/2026-10-24-gauduchon-trace-tv-and-adjoint-support-nets.md).

- **POME-GAUD-TRACE-TV-COUNTEREXAMPLE-001 — low / verified conditional deduction, no false printed theorem:** the elliptic-curve smooth positive sequence of Example 11.31.8 has \(\|u_k\|_\infty\to0\) but its signed Gauduchon trace difference has **exact total-variation norm \(1/\pi\)** for every \(k\). The original weak-homeomorphism theorem and sharp bounded-Lipschitz exponent stay valid; they cannot be promoted to TV.
- **POME-ADJOINT-DUAL-UNIFORM-L1-001 — low / verified conditional deduction:** \(B_\varphi\) has an explicit *uniform* \(L^1\)-continuity modulus on the entire \(\|F\|_\infty\le M\) ball: \(|B(F)-B(G)|\le\sqrt t+2M\Psi_{B(0)+2M}(\sqrt t)\), \(t=\|F-G\|_1\le1\), where \(\Psi_L\to0\) is the uniform-concentration gauge of the compact \(H_\varphi\)-sublevel. No rate for \(\Psi_L\) is invented.
- **POME-ADJOINT-SUPPORT-NET-STABILITY-001 — low / verified conditional deduction:** bounded logarithmic densities converging in measure along **any directed net**, with arbitrary supporting probabilities, have weak \(L^1\)-compact supporter values; every subnet limit supports the limiting density, and uniqueness there forces the *entire net* to converge weakly \(L^1\), without cofinal-sequence assumptions.
- **Exact scope and exclusions:** initial integrated direct review of §§11.31,11.33–11.36, selected proofs only; no section, external PDE/elliptic chain or user-deferred smoothing programme certified. The cited §5.42.5 smooth approximation was not audited; §11.34 divisorial smoothing subsection was not reopened. The 747-row ToC matrix remains inventory. No build, CI, publication, merge or source edits.

---

# 2026-10-24 — circle monodromy, integral Čech torsion and broad sheaf-theoretic proof audit

**Fresh reviewed main:** b6933b772f41b45918f7e25ed1afbbb1fd892272. **Preserved starting review head:** 819f23618f6aaa89d7e4bae734e86636e118edb1. Freshly read main AGENTS.md and documentation/proof-expansions.md, review README.md and this LATEST.md, existing full ledger and the 747-row ToC coverage matrix. [Source-anchored English report](reports/2026-10-24-circle-local-system-monodromy-and-cech-comparison.md).

- **POME-CIRCLE-LOCAL-MONODROMY-001 — low / verified conditional deduction, not a false printed theorem.** For any commutative ring R and module L with invertible monodromy T, the local system on S¹ has H⁰=ker(T−I), H¹=coker(T−I), and no higher cohomology. Full integral two-arc alternating Čech calculation, including the GL₂(Z) unipotent example with H¹=Z⊕Z/m, and the cyclic-permutation monodromy verification of finite covering direct images; no unwarranted field coefficients or sequential limit assumptions.
- **Actual first proof-level review** of previously inventory-only §§10.43,10.44,10.67,10.70: Godement/flabby and Čech double-complex arguments, soft sheaves and ordered-vs-alternating cochains, PID Tor and direct-sum Künneth normalization, local-system transport and the singular/sheaf comparison. Selected proof steps, not certification of whole sections or the entire transitive topology/analysis chain; no new error alleged. Earlier §§10.26–10.29 findings encountered in the ledger were **not repeated**.
- **Writes and exclusions:** dated report and cumulative ledger, matrix and checkpoint only, on review/mathematical-audit. No main/source/reading-edition/tag/registry changes; no full build, script, CI, formalization, PR creation, merge or publication. Dedicated Demailly approximation/regularization, Bergman, L², Ohsawa–Takegoshi, multiscale and positivity-loss work remains **deferred-by-user**, not resolved or certified.

---

# 2026-10-24 — exact disc Green values on holomorphic retracts; sharp exponential-density ordering

**Freshly reviewed main:** b6933b772f41b45918f7e25ed1afbbb1fd892272. **Preserved starting audit head:** 020dd1227f1dfd2d093fe3fe676398554edadce3. Re-read current main AGENTS.md, documentation/proof-expansions.md, review-branch README.md and this LATEST.md, plus the existing ledger and all 747 ToC rows before working. [New source-anchored complete report](reports/2026-10-24-green-holomorphic-retract-and-exponential-density-order.md).

- **POME-GREEN-HOLO-RETRACT-001 — low / verified conditional deduction, no false theorem:** For an arbitrary proper domain D (including unbounded domains) with holomorphic p:D→Δ and section i:Δ→D, both the symmetric Green envelope W_D and the ordinary Green g_D are exactly the disc Green function on i(Δ)×i(Δ). Direct proof uses a separately PSH and jointly SH Schwarz kernel with both boundary-distance constraints and the opposite inequality from pulling back negative Green competitors. The unbounded strictly pseudoconvex §7.27.3 Hartogs example consequently has exact disc values for **all** retract pairs although the Green slice at (0,0) collapses on the entire line w=0.
- **POME-EXP-MA-DENSITY-RATIO-001 — low / verified conditional deduction, no false theorem:** For fixed-type θ-PSH solutions of MAθ(u)=e^(λu)f dV above a strict analytic barrier, two-sided e^ε comparisons of densities imply the **sharp** uniform bound sup_X|u_f−u_g|≤ε/λ. One-sided f≤g gives u_f≥u_g. Proof is a strict-comparison application to shifted potentials, with sharpness from exact density scaling. This does **not** claim existence or add an L^p-only uniform stability theorem.
- **Actual first selected proof coverage:** formerly inventory-only §§7.22,7.26–7.27,15.13–15.15. Checked the asymmetric Green competitor and polynomial exhaustion, Colombeau-algebra quantifiers and positive-kernel capacity convergence, unbounded symmetric Green envelopes, strict barrier comparison, Gauduchon trace determinant bound, and the bounded-family stability Hölder exponent. Six section rows updated to **selected proof coverage only**; no full section or upstream compactness/PDE existence result certified.
- **Next broad-scope rotation:** choose unreviewed nonexcluded §10.26–10.30 cohomology/rigidity or §15.17–15.18 local regular-locus PDE estimates, and separately rotate into b-divisor/toric/NA material by currently insufficiently checked individual entries. Verify actual ToC and source tags afresh. The current session did **not** read §15.16's regularization-based construction or reopen any part of the excluded programme.
- **Changes and limits:** new English report plus cumulative ledger, 747-row matrix and this checkpoint **only**, on review/mathematical-audit. No main/source/body/registry/tag changes, CI, complete build, scripts, formalization, PR, merge, or website publication. User-deferred Demailly approximation/regularization, Bergman/L²/Ohsawa–Takegoshi/multiscale-atlas/positivity-loss items stay **deferred-by-user**, not resolved/certified.

---

# 2026-10-24 — positive-volume model uniformity for arbitrary nets; order-free Lelong Hölder stability

**Fresh reviewed main:** b6933b772f41b45918f7e25ed1afbbb1fd892272. **Preserved starting audit head:** a2b15d37528ac44513466941ed339b40fea0fd92. Re-read main AGENTS.md and documentation/proof-expansions.md, review README.md and this LATEST.md, the ledger and full 747-row ToC matrix. [New source-anchored mathematical report](reports/2026-10-24-positive-volume-net-uniformity-and-lelong-holder.md).

- **POME-VOLCOMP-UNIFORM-NETS-001 — low / verified conditional deduction; not an error in the source.** On positive-lower-volume ordinary models, the comparison d_theta has no triangle inequality, but its symmetric small-comparison entourages define a separated countably based **complete uniformity**. Every **Cauchy directed net** converges: select a not-necessarily-cofinal Cauchy sequence, use the source's sequential completeness, and transfer its convergence uniformly to the entire net with the quantitative quasi-triangle modulus.
- **POME-VOLCOMP-LELONG-HOLDER-001 — low / verified conditional deduction; not an error in the source.** For any two potentials with lower singularity volume ≥delta>0 and any **fixed** smooth compact modification pi, their pointwise Lelong profiles differ uniformly by at most C_pi min{1,(d_theta(u,v)/delta)^(1/n)}. Use max(u,v) and the printed one-sided Lelong comparison twice; positivity of both differences yields the exact bound **without a factor 2**. It also controls generic divisorial values and implies uniform Lelong convergence for d-convergent directed nets in M_delta.
- **Actual fresh proof-level coverage:** §§13.19, 13.21 and 13.23 (domination, monotone volumes, rooftops/capacity), plus substantive expansion of previously narrow §13.22 coverage (quasi-triangle, sequential completeness); §13.18.3 was used as a checked prerequisite, not newly certified. The trace corollary's approximation step was not reopened. No entire section or dependency graph is fully certified; 747 ToC entries remain a coverage **inventory**.
- **Strict exclusions and writes:** Dedicated Demailly approximation/regularization, Bergman/L²/Ohsawa–Takegoshi/multiscale/positivity-loss work remains **deferred-by-user**, neither solved nor certified. Only audit Markdown is updated on review/mathematical-audit. No main/source/body/tag/registry edits, tests, scripts, build, CI, website publishing, new PR or merge.

---

# 2026-10-24 — sharp high-dimensional tube radius and Loewner-concave circle spectral normalization

**Fresh reviewed main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. **Preserved review head:** `159cdade25335ecd8ede3b353dd293261af4fb4f`. Read current main `AGENTS.md` and `documentation/proof-expansions.md`, review-branch `README.md`, existing `LATEST.md`, ledger and actual 747-row coverage matrix. [New complete, source-anchored English report](reports/2026-10-24-sharp-tube-radius-and-matrix-spectral-factor-order.md).

- **POME-TUBE-RADIUS-SHARP-001 — low / verified conditional deduction, not a false theorem.** On the radius-`r` tube around a circle in `R^m` (`m≥3`), `s-r=-dist(·,∂T_r)` is subharmonic *throughout* the tube iff `r≤(m−2)R/(m−1)`. For its exterior complement the boundary distance is subharmonic on a **full interior collar iff the inequality is strict**. Direct cylindrical Laplacian and decreasing `s_epsilon` proof; §9.19.1's published sufficient condition remains correct.
- **POME-CIRCLE-SPECTRAL-FACTOR-ORDER-001 — low / verified conditional deduction, not a false theorem.** For smooth positive matrix symbols `W` on `S¹`, the §9.23 Hardy minimizer's canonical matrix `A(W)=H(0)*H(0)` is Loewner-monotone and concave in `W`, satisfies `cI≤A(W)≤∫W` when `W≥cI`, and obeys the **exact** normalized determinant identity `log det A(W)=∫log det W`. Proof uses the printed closed-disc-invertible spectral factor and the harmonic mean-value property.
- **Actual new coverage:** selected integrated §§9.19,9.21–9.24 including the inverse-shear Fatou–Bieberbach construction, Hardy restriction singular numbers, circle Toeplitz factorization and stationary-disc Green regularity. Conditional §9.20 and analytic prerequisites are **not** certified; no fully audited section. The unrelated dedicated Demailly/Bergman/L²/OT/multiscale/positivity-loss programme stays **deferred-by-user**, unopened.
- **Scope and writes:** four audit Markdown files only; no modification of main/source/reader/registry/tags, tests, full build, GitHub Actions CI, automatic publication, PR or merge.

---

# 2026-10-24 — filtration test curves: an invalid pointwise Fekete limit, with exact limsup repair

**Fresh reviewed main:** b6933b772f41b45918f7e25ed1afbbb1fd892272. **Preserved starting review head:** 81bcb013b6d99e412145d5c113246bbcef767077. Reviewed current main AGENTS.md, documentation/proof-expansions.md, and audit-branch README.md/LATEST.md, cumulative ledger, current 747-row matrix, actual integrated §17.14 and narrowly selected §22.1 cross-references. [Dated complete counterexample, stable source labels, physical HTML lines and local correction](reports/2026-10-24-filtration-pointwise-fekete-obstruction.md).

- **POME-FILT-FEKETE-LIM-001 — medium / confirmed error in a printed auxiliary formula, with a verified local repair.** Equation 17.14.11 (tag 79C9CAB675E4) claims an ordinary pointwise normalized limit exists for the superadditive filtered section potentials. On a smooth elliptic ruled surface with **big** tautological line bundle twisted by nontrivial two-torsion, the trivial allowed filtration gives odd-degree normalized potentials equal to -infinity on the distinguished elliptic section, while even degrees stay uniformly bounded below. Thus the limit does not exist for any fixed parameter below the filtration endpoint. The correct **pointwise limsup** always equals the supremum, by the multiples-subsequence proof. This is **not a counterexample to** the following envelope/test-curve construction, which uses the supremum already; the proposed text repair is not integrated.
- **Actual newly reviewed passages:** first selected proof-level reading of §§17.14.1–.6, .8, .10, .14–.15; §17.11 and §21.1 are section-title wrappers. Narrow §22.1 reading concerned exact dependencies only, not any excluded analytic proof programme. Previous 747 rows preserved, the §17.14 row upgraded to *selected proof coverage only*; no entire section or theorem chain certified.
- **Remote edits restricted to review/mathematical-audit:** one new English proof report plus ledger, matrix and this checkpoint; one report-only source-label correction. No mathematical source, published reading edition, permanent tags, registry, main, CI, PR, merge or website publication was changed. No full project build, scripts or formal verification were run. Earlier distinct findings, including the §22.1.88 concave-tail defect, retain their previous statuses. **Dedicated Demailly approximation/regularization, Bergman, L², Ohsawa–Takegoshi, multiscale-atlas and positivity-loss work remains deferred-by-user, not resolved or certified.**

---

# 2026-10-24 — bounded convex products and the exact invariant-distance/Green maximum law

**Fresh reviewed main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`; preserved review head `67932751b0c12a0b1b9dc908a229afb6fa41e3b5`. [Source-anchored proof, stable labels and scope](reports/2026-10-24-convex-product-geodesics-and-green-max-formula.md).

- **POME-CONVEX-PRODUCT-INVARIANT-MAX-001 — low / verified conditional deduction, NOT a false theorem.** For a finite product of nonempty bounded convex domains, all four invariant pseudodistances `c,k,delta,sigma` (and every Schwarz–Pick system) equal the maximum of the factor distances; the pluricomplex Green function equals the maximum of the factor Green functions. We construct a common extremal holomorphic disc and a left inverse from a factor achieving the largest distance. Whenever a second factor has a strictly smaller distance, that disc can be varied through infinitely many extremal retract discs; tied maximal factors give distinct left inverses.
- **Actual new proof coverage:** §§9.17, 9.18 and 9.20, selected direct reading of integrated Schwarz–Pick contractions, convex-disc gluing, stationary-disc argument, `H^1` boundary functional, dual weight and smooth strong-convex exhaustion. Their complete external/internal analytic prerequisites were **not** certified. This result uses Theorem 9.20.5 conditionally and does not duplicate historical finite-disc or stationary-winding findings.
- **No errors newly certified; no whole section certified.** Only audit Markdown is proposed; no source/body/tag/registry/main/CI/website changes. 747 remains the current table-of-contents inventory. Dedicated Demailly approximation/Bergman/L²/OT/multiscale/positivity-loss programme remains **deferred-by-user**, not reopened or marked resolved.

---

# 2026-10-24 — positive-current extension cones and finite pluripolar restriction

**Fresh main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`; review branch retained and advanced without resetting or merging. [Complete proof, source tags, blob SHAs and physical line anchors](reports/2026-10-24-elmir-extension-cone-and-polar-restriction-boolean-algebra.md).

- **POME-ELMIR-EXTENSION-CONE-001 — low / verified conditional deduction.** If $E$ is closed locally complete pluripolar and positive closed $T$ on $X\setminus E$ has locally finite mass up to $E$, **all** positive closed extensions are $T^0+R$, where $T^0$ is the Skoda–El Mir coefficientwise zero extension and $R$ is an arbitrary positive closed current supported on $E$. Unique zero-$E$-mass extension; without zero-mass, $c\delta_0$ gives nonuniqueness on a punctured complex curve. For finite $E,F$, their coefficient restrictions satisfy $P_EP_F=P_{E\cap F}$ and $P_E+P_F=P_{E\cup F}+P_{E\cap F}$. This uses the original 5.60.3 and 5.60.6 **conditionally**, does not certify their complete proofs and does not allege a false theorem.
- **Actually inspected:** §5.60.3 p=1 boundary-energy argument and general-$p$ reduction, 5.60.6 restriction; §5.61.2 integration current extension and §5.61.1 finite-projection dependencies; §§5.53.1–2 current pushforward/submersion derivative signs; §5.44.7 **smooth** Hermitian torsion Leibniz signs. Prior §5.61.1 coverage retained rather than rewritten. The 747-section matrix is inventory and none of these whole sections was certified.
- **Unresolved / conditional:** full Skoda–El Mir proof, relative Richberg input, finite analytic parametrization and nonsmooth Hermitian capacity passages remain upstream; no excluded Demailly regularization steps reopened. Proposed optional body corollary only, **no main/source/tag/registry/website changes**. No full project build, tests, CI, scripts, publication or formalization.
- **Run outcome:** new English report, ledger entry, matrix refresh and this checkpoint are the only authorized review-branch document edits; link and remote commit should be checked below in the final audit report. No existing finding was deleted or recast as resolved. The historical Demailly approximation/Bergman/L²/OT/multiscale/positivity-loss backlog remains **deferred-by-user**.

---

# 2026-10-24 — selected topological foundations audit (§§2.10, 2.12, 2.23)

**Fresh main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`; retained review branch, no reset. [Complete proof and physical source anchors](reports/2026-10-24-test-form-escaping-nets-and-frechet-compactness.md).

- **POME-TESTFORM-ESCAPING-NET-001 — low / verified conditional deduction.** On a noncompact second-countable smooth manifold the LF test-form space has a convergent-to-zero net of nonzero forms whose supports eventually avoid every compact set; no tail is bounded. This illustrates precisely why §2.10.3 makes its common-support convergence claim only for **sequences**; the printed theorem is not false.
- **POME-CURRENT-MOVING-ORDER-001 — low / verified conditional deduction.** The weakly compact family `{0,delta_n^(n):n>=1}` has neither common compact support nor a fixed global finite order, but has the `K`-dependent equicontinuity required by the **correct** §2.10.5. Explicit scaled-bump order obstruction proved.
- **POME-FINEST-LCS-BOUNDED-SUPPORT-001 — low / verified conditional deduction.** In the finest locally convex topology on `C^(I)`, bounded sets have finite common basis support and bounded coordinates. Nonetheless a zero-convergent net can escape every finite basis span, reconciling the genuinely net-based completeness proof of §2.23.1.
- **Actual additional checks:** §§2.10.2–5, 2.12.1/.3/.5, 2.23.1–5 selected printed proof steps; compactness uses subnets, and Cartan–Serre compact-perturbation hypotheses were traced. No false theorem or complete section certified. The 747-section matrix is inventory, not a count of certified sections. No script/build/CI/publication/formalization, no main/source/tag/registry change. **The dedicated Demailly approximation/Bergman/L²/OT/multiscale/positivity-loss programme remains deferred-by-user, not reopened or certified.**

---

# 2026-10-24 — new finite-curve retraction nearest-point threshold (§§18.19–18.21, 18.23–18.24)

**Fresh reviewed main:** b6933b772f41b45918f7e25ed1afbbb1fd892272. **Starting preserved branch:** c415400c20ea5b9147b81bedb59e4f1c5ec061fa. Fresh main AGENTS.md and documentation/proof-expansions.md, review-branch README.md and LATEST.md, current ledger/matrix and five actual integrated section sources checked. [Full dated source-anchored mathematical proof](reports/2026-10-24-finite-curve-polar-retraction-sharp-threshold.md).

- **POME-CURVE-FINITE-RETRACT-SHARP-001 — verified conditional deduction / low; NOT a printed-theorem error.** The finite-map polar-measure retraction \(P=d^{-1}r^*r_*\) has the **sharp** real signed-measure TV complement norm \(\|I-P\|=2(1-1/d)\), including branch multiplicities. Its induced model retraction is nearest-point for **every** model if \(d\le2\); for every \(d\ge3\) and positive base area the exact factor is attained by an analytic point-pole model and R is **not** nearest. In degree two nearest models need not be unique. For base area zero both spaces are singletons. This extends §18.24.4's cubic example and §18.24.2 without contradicting them; conditional on the integrated finite-map and curve classification inputs.
- **Actual new coverage:** selected §18.19 stretching and all-obstacle equivalence, §18.20 semipositive auxiliary factor / bigness / mass, §18.21 sixfold combinatorics, §18.23 branched trace scaling and sheet-loss, and §18.24 fiber maximum, polar measure retraction, volumes and cubic example. All five were previously inventory-only; no complete section, internal dependency or original theorem was certified. 747 is a ToC inventory.
- **No** software script/full build/CI/publication/formal checker/main/source/tag/registry/PR/merge changes. Excluded Demailly approximation and dedicated Bergman/\(L^2\)/Ohsawa–Takegoshi/multiscale/positivity-loss proof programme remains **deferred-by-user**, untouched. Next run should rotate to another nonexcluded inventory-only section.

---

# 2026-10-24 — first selected §§12.34–12.36 audit: Gauduchon dual faces and a unique endpoint current

**Fresh `main`:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. Starting review head `b655b89bf5a489b9916c038a407c344a80af4bf3`; branch preserved without reset. Freshly read `main/AGENTS.md`, `main/documentation/proof-expansions.md`, review-branch `README.md` and prior `LATEST.md`, cumulative matrix/ledger, and current published reading-edition source passages. [Complete English, source-anchored mathematical report](reports/2026-10-24-gauduchon-current-faces-and-endpoint-uniqueness.md).

- **POME-GAUD-FACE-DERIVATIVE-001 — low / verified conditional deduction, NOT an original theorem error.** Compact normalized Gauduchon current duality gives exact left/right directional derivatives of \(m_h(\theta)\) as max/min of \(\int\eta\wedge T\) over the minimizing face, plus an optimal 1-Lipschitz background bound and quantitative stability of the *fixed-reference affine* Chern–Ricci positivity threshold. Proof uses weak compactness of **nets**, not sequential compactness.
- **POME-CRF-ENDPOINT-CURRENT-UNIQUE-001 — low / verified conditional deduction, NOT a printed proposition error.** In the explicit \(\mathbb P^m\times\mathbb P^1\) endpoint model of Proposition 12.34.12, the only normalized positive \(dd^c\)-closed annihilator is \([Z]/2\); its trace probability is precisely normalized Fubini–Study \(w|_Z\). This follows from the printed support/rank identities, \(dd^c\)-closedness and the scalar Poisson equation on the connected curve.
- **POME-CRF-PARABOLIC-INPUT-001 — medium / external dependency, NOT an erroneous flow theorem.** Theorem 12.34.4's higher regularity/continuation at physical lines 173–175 uses the parabolic Evans–Krylov and Schauder package without establishing it internally in that step; short-time parabolic existence at line 112 likewise quoted. Keep this honest analytic proof dependency for later independent treatment.
- **Actual coverage:** §§12.34–12.36, selected reading-edition separation, parabolic barrier/trace, divisor subtraction, Hopf threshold/volume and positive-current endpoint steps; §12.7 coefficient normalization only as a dependency check. 747 sections remain inventory, **not certification**. No build/scripts/CI/publication/formalization, no main/source/tag/registry change. User-excluded Demailly and dedicated Bergman/L²/Ohsawa–Takegoshi/multiscale/positivity-loss material stays **deferred-by-user**, neither reopened nor resolved.

---

# 2026-10-24 — curve models: GH permutation couplings and trace-versus-\(L^1\) separation

**Fresh main:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`. The review branch was retained without reset. New first selected nonexcluded proof coverage of §§18.17, 18.18, 18.22; context only §§18.16,13.28–29,5.43 and15.19. **[Complete source-anchored proofs](reports/2026-10-24-curve-model-permutation-gh-and-trace-l1-separation.md).**

- **POME-CURVE-GH-PERMUTATION-001 — verified conditional deduction / low; not a printed-theorem error.** For biholomorphically matchable curve factors the GH upper bound on ordinary and ideal product-model spaces improves to the minimum, over allowable permutations \(\pi\), of \(\sum_i|a_i A_i-b_{\pi(i)}A_{\pi(i)}|\); general-background counterpart uses \(\sum_i|B_i-B'_{\pi(i)}|\). Two identical curve factors with coefficients \((t,0)\) and \((0,t)\) yield isometric abstract spaces, despite positive printed coordinatewise upper bound. Exact §18.17.5 and §18.18.3 references and proof given in report; no equality assertion for arbitrary incomparable vectors.
- **POME-CURVE-TRACE-L1-NONCONVERSE-001 — verified conditional deduction / low; not a printed-theorem error.** On the connected-fiber compact complex fibration of §18.22 with \(A>0\), moving full polar point masses \(A\delta_{s_j}\rightharpoonup A\delta_s\) give normalized ordinary models \(U_j\to U\) in every smooth-volume \(L^1(X)\) and weakly convergent first traces, while polar-model distance is identically \(2A\) and trace TV distance is \(2\kappa_\gamma A\). This rules out only an *unstated converse* to §18.22.3's actual metric-to-\(L^1\) continuity, with critical fiber multiplicity retained.

No entire section certified. No new false theorem found. No script/build/CI/publication/formalization/source/body/registry/tag change; only audit notes are to be committed. Excluded Demailly approximation and all dedicated Bergman/\(L^2\)/Ohsawa–Takegoshi/multiscale/positivity-loss work remain **deferred-by-user**, untouched. Rotate to another untouched chapter at the next checkpoint.

---

# 2026-10-24 — first selected §§11.20–11.21 product curvature and Hopf convexity audit

**Fresh reviewed main:** b6933b772f41b45918f7e25ed1afbbb1fd892272; starting audit head 98790582c8b79d2cecd0c0574ec0480e4616a528, preserved without reset. Current main AGENTS.md, documentation/proof-expansions.md, the existing review-branch README.md, previous LATEST.md, both audit ledgers, and actual published Hermitian reading-edition sections were freshly read. [Exact English report with proofs, source IDs/tags/blobs and physical line anchors](reports/2026-10-24-product-mean-curvature-uniform-gap-and-hopf-index.md).

- **POME-PROD-MEAN-UNIFORM-SPECTRAL-001 — verified conditional deduction / low; not a false theorem.** For Hermitian external tensor products with factor mean curvature \(K_i\geq\kappa_i I>0\), the kth largest eigenvalue of the curvature coefficient form satisfies \(\lambda_k(\alpha_{h,v})\geq(\min_i\kappa_i/n_i)h(v,v)\), even for entangled fiber tensors. The full projective-complement \(q\)-convexity conclusion persists under arbitrary sufficiently small \(C^2\) **nonproduct** perturbations of the metric. Proof via orthogonal block traces, min-max and compact-sphere curvature continuity, conditional on original Theorem 11.18.2 in its valid compact-base setting.
- **POME-GAUD-HERMITEIN-INPUT-001 — external dependency / medium, NOT a counterexample.** Corollaries 11.18.4 and 11.20.3 use the classical Hermitian–Einstein existence theorem for slope-stable bundles over compact Gauduchon manifolds, but the inspected proof invokes rather than establishes that deep input. The stability/degree corollaries are *conditional* until a complete internal proof is matched or written. Theorem 11.20.2 with a directly supplied positive-mean-curvature metric does not depend on this existence theorem.
- **Actual additional §11.21 verification:** radial maximum/Lagrange multiplier in 11.21.1, Hopf curvature and elliptic-fiber signs in 11.21.4, and diagonal direct-sum homogeneous metrics in 11.21.5. The printed mixed-sign interval for the convexity index remains undetermined. The earlier §11.18.2 compact-base proof gap is retained under its old ID; products in §11.20 have compact base and do not trigger it. Only §§11.20–11.21 were moved from inventory-only to selected-proof coverage. The 25-chapter/747-section matrix is an inventory, not certification.
- **Checks performed:** exact integrated HTML statements and selected proof steps, trace/degree normalization and finite-dimensional min-max argument; no numeric script, full build/tests, CI, publication, formalization or main/source/tag/registry modification. Review notes alone were pushed. No new PR or merge.
- **Hard exclusion unchanged:** the dedicated Demailly approximation/regularization and Bergman, \(L^2\), Ohsawa–Takegoshi, multiscale-atlas and positivity-loss programme stays **deferred-by-user**, never resolved, certified or silently reopened. Next audit should rotate to a different previously inventory-only nonexcluded section rather than remain in this curvature chain.

---

# 2026-10-24 — selected §14.22–23 and §§15.29, 15.32 proof review (nonexcluded)

**Fresh main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`; starting branch `64aa119a69c33891dc59b9b443f5f9a6fc89bb02`, retained without reset. Read main AGENTS.md, documentation/proof-expansions.md, current integrated HTML, actual 25-chapter/747-section inventory and branch README.md / latest checkpoint. The existing PR #9 is already merged/closed; no new PR opened. [Detailed English report](reports/2026-10-24-root-net-dominated-convergence-and-determinant-squared-gap.md).

- **POME-DEGEN-EQUALDET-SQUARE-GAP-001** — low, **verified conditional deduction**, not an error: exact square-sum and affine-invariant log-spectrum inequalities refine §14.23.3–4 for positive Hermitian A,B of equal determinant in complex dimensions 2 and 3.
- **POME-SUBSOL-ROOT-NET-DOMCONV-001** — low, **verified conditional deduction**, not an error: the norm-closed bounded-root ideal in §15.32.9 has dominated convergence for **arbitrary nets converging in measure**. It does **not** have arbitrary pointwise-net dominated convergence: directed complements of finite subsets are pointwise decreasing to zero while all represent the constant L^n class 1. The printed sequence-in-measure statement remains correct.
- **Actual coverage:** selected integrated proofs in §§14.22–23 and §§15.29, 15.32 only; 747 matrix entries are ToC inventory, not certification. The §14.22 real symbol/product rules and §14.23 Stokes/W^{2,n} approximations were checked only at specified lines, not transitive verification of all analytic inputs. No new confirmed false theorem or independently certified complete section.
- **No** full build/tests/CI, website publication, PR/merge, formal verification, numerical scripts or main/source/body/registry/permanent-tag edits. Entire dedicated Demailly approximation/regularization, Bergman, L², Ohsawa–Takegoshi, multiscale-atlas, positivity-loss programme remains **deferred-by-user**; not reopened, resolved or certified.

---

# 2026-10-24 — new bounded Bedford–Taylor functional calculus and Ross–Witt Nyström pole-set proof correction

**Fresh main SHA:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. **Starting audit-branch SHA:** `386f923cf4eabdeb753591ca90690cea03b2ae32`, preserved. Required current main `AGENTS.md`, `documentation/proof-expansions.md`, review-branch `README.md`, prior `LATEST.md`, all 747 matrix rows and the cumulative ledger were freshly read. **Complete English arguments, source revisions, physical anchors and proposed changes:** [2026-10-24 detailed report](reports/2026-10-24-bt-continuous-weights-and-rwn-pole-quantifier.md).

- **POME-BT-CONTINUOUS-WEIGHT-001 — low / verified conditional deduction, NOT a false theorem.** For a fixed positive closed base current and decreasing locally bounded psh potential arrays with locally bounded limits, polynomial-weight convergence from §7.3.8 extends to `H(v_{1,j},...,v_{m,j})S_j` for any continuous `H:R^m→R`. Uniform local CLN mass controls and polynomial approximation on a common compact value box justify taking the j-limit first and uniform approximation second; neither discontinuous/unbounded weights nor moving base currents are included. Optional corollary after §7.3.8; no source-body changes.
- **POME-RWN-POLE-QUANTIFIER-001 — low / proof gap in a proof step, with verified local a.e. correction.** Proposition 17.13.35 Step 1 improperly asserts a finite optimizing time `t0` for **every** point y, including poles `ℓ*τ(y)=−∞`. On the admissible P¹ test-curve model of Example 17.12.13 (with `φ=0` and singular `varphi=a log[|z|²/(1+|z|²)]`), `ℓ_t(0)=−t` and for `τ=−1/2`, `ℓ*τ(0)=−∞`, so the displayed assertion has no t0. Quantify only outside the pluripolar pole set; it is null for smooth volume and gives the needed full-time-integral inequality almost everywhere. Proposition 17.13.35 itself **is not shown false**, and its converse strong-openness step was not recertified.
- **Actual coverage, not certification:** selected proofs in §§7.2.2/.5/.6, 7.3.3/.7/.8/.10/.11, 7.5.2/.4/.6/.7/.8, 7.6.1, 17.13.5/.11/.15/.21/.35/.38; contextual §17.12.13. Other earlier findings in these sections were preserved and not relogged. The 25 chapters/747 sections remain a **table-of-contents inventory**, not a claim of completed review.
- **Verified actions:** direct mathematical arguments, explicit projective-line counterexample to the Step-1 quantifier, checked real integrated HTML file paths/source labels/permanent tags and physical lines; updates only to the existing `review/mathematical-audit` audit documents. **Not run:** tests, scripts, full build, CI, web publication or formal checker; no new PR/issue/merge, no modifications to main, sources, reader bodies, registries, canonical tags.
- **Explicit exclusion:** dedicated Demailly approximation/regularization and Bergman/L²/Ohsawa–Takegoshi/multiscale-atlas/positivity-loss proof-completion remain fully **deferred-by-user**, neither reopened, resolved nor certified. Next substantive rotation should prefer another previously inventory-only nonexcluded section (e.g. b-divisor restriction, non-Archimedean or Hermitian torsion), not an excluded dependency programme.

---

# 2026-10-24 — new higher \(C^r\) degenerate MA examples and exact torus mass; §§7.24–7.25,7.33,9.12

**Fresh main SHA:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`; **review branch initial head:** `aed8f3f3d33d96a52ddebee74c84ac18d0f76923`, preserved without reset. Required main `AGENTS.md` and `documentation/proof-expansions.md`, the actual ToC (25 chapters and **747** sections as inventory), and review `README.md`, previous `LATEST.md`, matrix and ledger were read freshly. [Detailed English proof, exact permanent/source tags and integrated file anchors](reports/2026-10-24-degenerate-density-higher-creg-and-weighted-torus-mass.md).

- **`POME-DEGEN-CREG-SCALE-001` — low / verified conditional deduction, not a false theorem.** For every \(n\ge3\) and integer \(3\le r\le2n-3\), an anisotropically supported nonnegative \(C^r\) density produces a continuous Bedford–Taylor complex MA Dirichlet solution on the unit ball which is not \(C^{1,1}\) near the origin. Exact n=3,r=3 choice \(\alpha=8,\beta=26\) gives derivative margin \(26-3\cdot8=2>0\) and variation lower exponent \(23/12<2\). This genuinely improves printed §7.24.1's \(C^2\) model, beyond the previously logged C² parameter criterion, **conditional on the original Dirichlet comparison and CLN inputs**.
- **`POME-SEPMAX-WEIGHTED-TORUS-001` — low / verified conditional deduction.** For \(f(z)=\max(0,\lambda_i\log(|z_i|^2/R_i^2))\), \((dd^cf)^p=(\prod_i\lambda_i)\cdot\) normalized Haar measure on the product of radius-\(R_i\) circles. Separated maxima of two such blocks yield the tensor product with **no** multinomial factor (§7.33.3); full Alexandrov gradient simplex \(p!\) and the \(\log|z|^2\) toric Jacobian independently confirm the coefficient. Not a new proof of the abstract multi-block result already in the ledger.
- **New selected proof coverage:** §7.24.1 (\(C^r\) cutoff derivative estimates, radial free-contact argument, covariance/CLN exponents); §7.25.1–2 (relative extremal pasting signs, lower semicontinuity and Green boundary equivalence); §7.33.1/3 (positive-current recurrence and tensor factorization); §9.12.1 (Baire/Hartogs proof); §21.12.24 **normalization-only**. Matrix rows updated exactly; these are not whole-section certifications. No new confirmed error or genuine external input is asserted.
- **Checks actually run:** `mathematical-audit/checks/check_deg_density_creg_parameters.py` passed **100 exact rational** parameter cases (\(3\le n\le12\), \(3\le r\le2n-3\)); this tests inequalities only. **Not run:** project-wide build/tests, CI, website publishing, formal proof, automatic merges or deletion. Writes exclusively to audit reports/checks/matrix/ledger/LATEST on `review/mathematical-audit`; no main, permanent tag, registry or source modifications.
- **User exclusion continues without exceptions:** Demailly approximation/regularization and dedicated Bergman/L²/Ohsawa–Takegoshi/multiscale-atlas/positivity-loss programme remains `deferred-by-user`, never resolved or certified. Prior ledger and unresolved items preserved. **Next rotation:** comparatively unreviewed trace/restriction, non-Archimedean, b-divisor or Hermitian topics, avoiding all excluded chains.

---

# 2026-10-24 — exact \(\mathbb P^1\) singularity-envelope free boundary; §§16.20–16.21

**Reviewed current main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`; **starting review head:** `db3212d649a3aa35bfffe2faa74bbf67e784a6fe`, preserved. Fresh required main AGENTS.md, documentation/proof-expansions.md, 25-chapter/747-section ToC, review-branch README.md, previous LATEST.md, matrix and ledger read. [Complete English proof, exact source/reader tags, file blobs and physical anchors](reports/2026-10-24-projective-line-singularity-envelope-contact-free-boundary.md).

- **POME-MODEL-P1-FREEBOUNDARY-EXACT-001 — low / verified conditional deduction; NOT a false Pome theorem.** On normalized \(X=\mathbb P^1\), \(0<a<1\), \(u_a=a\log(|z|^2/(1+|z|^2))\), set \(R_a^2=a/(1-a)\) and \(h=-a\log a-(1-a)\log(1-a)\). The **exact** singularity envelope is \(w_a=a\log|z|^2+h-\log(1+|z|^2)\) for \(|z|\le R_a\), and \(0\) outside. Direct removable-pole subharmonic comparison proves maximality against *all*, not only radial, competitors. Curvature and non-pluripolar measures: \(\omega+dd^cw_a=a[0]+\mathbf1_{|z|\ge R_a}\omega\), \(\mu_{w_a}=\mathbf1_{|z|\ge R_a}\omega\), while \(\mu_{u_a}=(1-a)\omega\). Thus both masses equal \(1-a\), **equality** holds in the support domination of Proposition 16.21.3, but the measures differ by total variation \(2a(1-a)\). No shell current at the free boundary.
- **New actual selected proof coverage:** §16.21.1–3 (singularity-envelope competitor/rooftop and mixed-mass passage; limiting contact domination), §16.20.2 Steps 1–5 (weighted pole cutoff, polynomial polarization and weak-Hessian density), §16.20.4 consequence. §21.1 was *convention-only*. None of §§16.20–21 or general mixed-mass/capacity/PDE prerequisite chains is certified. Entire ToC is an inventory.
- **Actual verification:** direct analytic maximum principle, one-dimensional distributional curvature and Fubini–Study radial integration. **Not run:** arithmetic scripts, full project tests/build, CI, publication, formalization or PR/issue/merge actions; no changes to main, reader text, source repositories, permanent tags, registries or canonicalization.
- **User exclusion strictly preserved:** Demailly approximation/regularization, and dedicated Bergman/L²/Ohsawa–Takegoshi/multiscale-atlas/positivity-loss completion, remain **deferred-by-user**, neither reopened nor certified.

---

# 2026-10-24 — sharp isolated point-pole volume deficit; complex-surface Gauduchon adjoint

**Freshly reviewed current `main`:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. **Starting audit head:** `7fb748161aee81ecfc0e1cf438b604db18f1dfe5`, preserved without reset. Freshly read main AGENTS.md, documentation/proof-expansions.md, actual 25-chapter/747-section ToC, and review-branch README, prior LATEST, SECTION_MATRIX, LEDGER. **Detailed source-anchored English proof:** [2026-10-24 point-pole and Gauduchon-surface audit](reports/2026-10-24-point-pole-volume-deficit-and-surface-adjoint.md).

- **`POME-VOL-POINT-LELONG-OPTIMAL-001` — low / verified conditional deduction, NOT a false theorem.** On `P^n` with normalized Fubini–Study background, `u_a=a log[(|Z_1|²+...+|Z_n|²)/(|Z_0|²+...+|Z_n|²)]` and `v=0` give **exact** non-pluripolar mass `1-a^n`, relative upper-volume deficit `D=a^n`, positive lower reference volume `delta=1`, and point Lelong jump `a`. The radial flux derivation is direct; the volume-over-equivalent-types step invokes the already stated closed-class invariance. The projective-line bound establishes `C_id=1` uniformly and the example attains equality in §13.18.3, proving the exponent `1/n` and the constant optimal on this model.
- **`POME-GAUD-SURFACE-ADJOINT-SCALAR-001` — low / verified conditional deduction, NOT a false theorem.** In the printed §14.10 ansatz at `n=2`, `eta_u=gamma_0+dd^c u` and `int eta_u²=int gamma_0²+2int u dd^c gamma_0`. The adjoint density of §14.12 is **constant iff the initial metric `gamma_0` is Gauduchon**, not merely because the auxiliary `gamma` is. Under that additional condition `rho_u=1/int gamma_0²` for all admissible `u`, and a prescribed-volume solution has explicitly `b=log[(int gamma_0²)/(int e^F gamma²)]`. Without it the affine volume correction remains and density need not be constant; a conformal non-Gauduchon torus metric is a counter-limitation to any overstatement.
- **Precise new selected proof coverage:** §§13.16 conventions, 13.17.1–2 contact/monotonicity, 13.18.1/.3/.5 comparison and deficit mechanism, 14.10.1 surface ansatz, and 14.12.1/.3 adjoint specialization. These are previously inventory-only §§13.16–13.18 and 14.12 plus newly selected §14.10 surface steps; **no complete section or PDE/external dependency chain certified**. Existing curve mass-deficit and adjoint sign findings not relogged. The matrix retains all 747 ToC rows, NOT 747 certifications.
- **Checks actually run:** direct algebraic/polar integrations and compact surface Stokes arguments, with precise proofs in the report. **No** numeric scripts, full project tests, compilation/site build, CI, publication, formal verification, PR/merge operation or edits to main, mathematics reading bodies, source repositories, registry, canonicalization or permanent tags.
- **Strict exclusion unchanged:** all dedicated Demailly approximation/regularization, Bergman, L², Ohsawa–Takegoshi, multiscale-atlas and positivity-loss work remains `deferred-by-user`, not reopened, resolved or certified.

---

# 2026-10-24 — sharper divisorial Jacobian bound and selected complex-space proof audit

**Fresh reviewed main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. **Starting review head:** `88f6d58078d2c10e0759449d16a765157e62b8f6`, preserved without reset. Freshly read `main/AGENTS.md`, `main/documentation/proof-expansions.md`, current actual ToC (25 chapters, 747 inventory entries), and `review/mathematical-audit/README.md` and prior `LATEST.md`; consulted SECTION_MATRIX and LEDGER for de-duplication.

- **`POME-DIV-JAC-CODIM-001` — low / verified conditional deduction, NOT a false printed theorem.** For a generically full-rank map of smooth complex n-folds and prime divisor E with codimension-r image center, `ord_E J_f >= Σ ord_E(z_i∘f)−1 >= r−1` for r adapted local target coordinates. The normal differentials contain r factors of the local equation but at most one dt factor can survive their exterior product. Equality holds on a codimension-r smooth-center blowup. In §9.8.6's principalization iteration, the decrement in Jacobian order can be strengthened from 1 to r−1 at a stage with smooth center of codimension r. This remains **conditional** on its explicit Hironaka input and common-model results. [Complete English proof with source tags, exact blobs and line anchors](reports/2026-10-24-divisorial-jacobian-codimension-bound-and-model-audit.md).
- **Actual newly selected proof inspection:** §9.6.2–3 graph blowup/invertible ideals and pivot Jacobian, §9.7.5 restricted principalization and exceptional support, §9.8.1–2 connected fibers and normality, §9.8.6 selected chain-rule, codimension and termination, §9.9.4 finite-projection psh upper bound. The potential issue of nonreduced analytic spaces was **discarded** after checking the explicit reduced-space convention in §9.4. No complete section or entire Remmert/analytic-projection/Hironaka chain was certified. Newly marked §§9.6–9.9 in the durable 747-row matrix; existing ledger findings unchanged.
- **No executions:** numerical or symbolic test suite, project build, CI, website publication, formal proof check or PR operation. Only direct analytic/exterior-product calculation was performed. `main`, sources, reading bodies, registries and permanent tags remain untouched.
- **Strict user exclusion preserved:** Demailly approximation/regularization and dedicated Bergman/L2/Ohsawa–Takegoshi/multiscale-atlas/positivity-loss completion programme remain **`deferred-by-user`**, neither resolved nor certified.

---

# 2026-10-24 — classical Green-domain nets and weakly converging Riesz potentials

**Fresh current main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. **Starting review checkpoint:** `141dbb1e556805545630385d4ec55bdf6e4a5ba8`; preserved existing review branch and cumulative audit records without reset. Freshly read main AGENTS.md, documentation/proof-expansions.md, current ToC, and review branch README.md and earlier LATEST.md. Detailed, source-anchored [English mathematical report](reports/2026-10-24-green-directed-exhaustions-and-weak-kernel-potentials.md).

- **POME-CLASS-GREEN-DIRECTED-EXHAUST-001 — low / verified conditional deduction.** The monotone Green-kernel convergence of §3.1.34 extends from sequences to **arbitrary directed increasing families** of bounded regular domains whose union is bounded regular, in C∞_loc off the fixed pole. The proof uses a compact-exhausting auxiliary chain as a squeeze and interior estimates for the harmonic pole-cancelled differences. It does **not** assert that the auxiliary chain is cofinal, nor that a theorem for regular domains covers irregular domains.
- **POME-CLASS-POTENTIAL-WEAK-L1-001 — low / verified conditional deduction.** For nets of finite positive measures with fixed compact support and weak convergence, convolution with the fundamental solution converges in L1_loc, and smoothly on compact sets off the support. Complete argument uses the compact L1(K)-valued translation map and finite-rank partition-of-unity approximation; no sequential compactness assumption. **Sharp limitation:** in d=2, `ν_j=(2π/j)δ_{e^{-j}e_1}⇀0` while `(E_2*ν_j)(0)=−1` for all j, so pointwise potential convergence at every point is false *without extra conditions*. This does not contradict any printed theorem.
- **Actual new proof coverage:** previously inventory-only §§3.1 and 3.4, selected Perron/barrier/Green monotonicity and exhaustion, fundamental potential/Fubini, Riesz decomposition, Choquet and polar extension steps. Exact main blobs, source labels, permanent tags and line anchors are in the report and ledger. **No complete section certified.** ToC remains 25 chapters / 747 sections, a section inventory only.
- **Review scope exclusions unchanged:** dedicated Demailly regularization/approximation, Bergman, L2, Ohsawa–Takegoshi, multiscale-atlas and positivity-loss programme remain **deferred-by-user**, not reopened, resolved or certified. No arithmetic/numeric scripts, whole-project tests/build, CI, website publication, formalization, source/registry/permanent-tag/main modifications, new PR/issue, paid services or automatic merge.

---

# 2026-10-24 — upper-semicontinuous varying-measure inequality along arbitrary nets

**Fresh main:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`; **starting review head:** \`c3ee48024045c9e23ac92f32acbc72ad235b6ab5\`. First new selected nonexcluded proof-level review of §§**5.61–5.63** and **10.101** (formerly inventory-only), with source blobs and stable tags in [the complete report](reports/2026-10-24-usc-weak-measure-nets-and-analytic-cycle-audit.md).

- **POME-USC-WEAK-NET-001**, **low / verified conditional deduction**: the sequential upper weak inequality of Lemma 5.63.3 extends to **arbitrary directed nets** of decreasing upper-semicontinuous weights and vaguely converging positive Radon measures, with any vaguely convergent subnet of signed products. Full proof uses compact-set portmanteau via finite layer sums and genuine net continuity from above for compact superlevel sets; there is **no sequence-subnet shortcut**. It proves \`f ∈ L1_loc(mu)\` and \`nu <= f mu\` under the precise original integrability and cluster hypotheses. The printed theorem is **not false** and has **not** been changed.
- Additional restricted checks: Lemma 5.61.1 finite analytic projections and trace mass; Theorem 5.61.2 extension **dependency only**; Theorem 5.62.3 annihilator-rank step, Lemma 5.62.4 divergence decomposition, Theorem 5.62.5 connected-leaf gluing; Proposition 5.63.2 finite polarization coefficient bound; Lemma 10.101.1 Kähler Aeppli dual separation. Other large prerequisites NOT certified.
- Theorem 5.63.4 nonsmooth extension via 7.31.1 and Proposition 10.101.2 pullback via 5.66.2 were explicitly **not reopened**: all excluded approximation/regularization work remains \`deferred-by-user\`.
- No project tests/build/CI, formalization, publishing, source/registry/tag/main modifications, arithmetic scripts, duplicate issues or new PR. Current 25 chapters / 747 sections is a ToC **inventory**, not completion.

---

# Pome audit — 2026-10-24: sharp logarithmic density-cutoff rate; withdrawn polar false positive

**Fresh main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`; review branch preserved (starting head `442f4d9c2be5e37a9d79facc203c7257c86769f5`). Freshly read `main/AGENTS.md`, `main/documentation/proof-expansions.md`, current main 25-chapter/747-section ToC, branch `README.md`, `mathematical-audit/README.md`, this prior `LATEST.md`, matrix and ledger. [Complete new English derivations and source-blob/line anchors](reports/2026-10-24-product-density-truncation-and-polar-audit-correction.md).

- **POME-PRODUCT-TRUNC-SCALAR-LOGRATE-001 — low / verified conditional deduction.** In the exact §15.30 product model with `β=k(1-α)>0`, `M_t=∫min(q_α,t)κ^k`, `c_0=binom(m+k,m)∫h_0^m`, and `f=Rq_α`, proved `(log t)^β(1−M_t)→α^k k^β` and **for the actual, unfactorized cutoffs** `(log j)^β[c_H(min(f,j))−c_0]→c_0 α^k k^β`. This is a rate/corollary, not a false original theorem. It is separate from the previously logged energy-moment threshold and conditional on the printed radial flux and scalar monotonicity.
- **POME-AUDIT-POLAR-HYP-WITHDRAWAL-001 — medium / verified repair of audit classification only.** Prior ledger `POME-EQUIL-POLAR-HYP-001` was a **false positive**: the *old blob SHA quoted by the prior report itself*, as well as current main, explicitly assumes **compact and non-pluripolar K** in §16.35.3. The polar singleton used as a prior counterexample was inadmissible. Withdraw the former `confirmed error` status; this is NOT a reading-edition repair or full proof certification.
- **Actual newly selected proof review:** §15.30.1–3 radial algebra, density and scalar bounds; selected §15.30.6 bounded-factor/truncation steps. §15.27.1, §15.31.3 and §16.34.2 were contextual; §16.35.3 was read for historical audit verification. A separate §16.36 weak-Lorentz result was *already logged* and was not repeated. No full section certified; 747 is an inventory, not completed proof coverage.
- **Actual check:** `checks/check_product_density_scalar_log_rate.py` ran **27** numerical high-log-threshold diagnostics in Python standard library. No project-wide tests/build, CI, publication, source/body/registry/tag/main changes, new PR/issue, formalization, merge or paid services.
- **Strict exclusion unchanged:** Demailly approximation/regularization and dedicated Bergman/L²/Ohsawa–Takegoshi/multiscale-atlas/positivity-loss proof-completion remain `deferred-by-user`; not reopened, resolved, or certified.

---

# Pome audit — 2026-10-23: exact Hopf-basic Monge–Ampère tails and Gauduchon orders

**Fresh main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`; **start audit head:** `47001d69d14580fe34a55faf5a6474defad9213c`, preserved without reset. Read `main/AGENTS.md`, `main/documentation/proof-expansions.md`, the current main `README.md` and ToC (25 chapters / 747 **inventory** sections), plus `review/mathematical-audit/README.md` and the earlier `LATEST.md`. Actual first selected proof-level inspections: §§17.16.16, 17.16.30; separately only §§12.19.20, 12.20.1. No entire section or upstream theorem corpus is certified.

- **`POME-HOPF-BASIC-ENERGY-EXACT-TAIL-001` — low / verified conditional deduction, NOT a false theorem or missing proof.** For the canonical `v_a=1-(1-ψ)^a` on `ℙ^d`, `0<a<1`, `τ=(1+R)^{1/a}`: `MA_κ(v_a)({v_a<-R})=[e^{1-τ}+a(1-e^{1-τ})τ^{a-1}]^d` **exactly** for R≥0. Thus tails are asymptotic to `a^dR^{-d(1-a)/a}`; all finite moments satisfy `∫(-v_a)^q MA<∞ iff a<d/(d+q)`, with logarithmic divergence at equality. The Hopf pullback has precisely `2n` times the tail. The radial Stokes and layer-cake proof and source blobs/labels/permanent tags are in [the dated report](reports/2026-10-23-hopf-basic-exact-energy-tail-and-gauduchon-orders.md). This extends the printed `q=2` example without changing it.
- §12.19.20 periodic derivative constraint `p'≥−1`, `|p|≤1` and `Lr²/4−r³/6` sharp bound rechecked in its selected one-dimensional proof only; §12.20.1 log-order sign reversal/rescaling verified conditional on the stated variational monotonicity/homogeneity. Not a certification of either full section, the threefold construction or analytic equation.
- Prior Kähler `E²` completion/CAT(0) external dependency `POME-GEO-EXT-CAT-001` unchanged. The entire dedicated Demailly approximation/regularization, Bergman/L²/Ohsawa–Takegoshi/multiscale-atlas/positivity-loss programme remains **`deferred-by-user`**, not reopened or certified. No new arithmetic script, full project tests/build, CI, website publication, source/body/registry/permanent-tag/main changes, merge or PR operation.

---

# Pome audit — 2026-10-23 22:48 Asia/Shanghai: radial currents and a Lelong-number jump

**Fresh verified main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`; **review head at start:** `083c6e784a6a2ece5131f3710fc4c9b08d8726e9` (preserved, never reset). Freshly read `main/AGENTS.md`, `main/documentation/proof-expansions.md`, `main/docs/chapters/index.html`, `review/mathematical-audit/README.md` and this review-branch `LATEST.md` before mathematical review. Actual current ToC: 25 chapters and 747 section entries — **inventory only**, not whole-section/proof certification.

**New first selected nonexcluded proof-level inspection:** §5.58 `docs/sections/real-currents-submersions-and-homotopies--radial-positive-currents/index.html` (blob `994a47ced79c1995630dd32b0d9703faddf9c173`), Thm 5.58.3 (`FB41A7CE1CEE`), Cor 5.58.9 (`4F0954956743`), radial eigenvalue and BV flux formulas; supporting only the density normalization of §6.33.1 (`7ACCEC6E0526`). Did **not** certify complete §§5.58/6.33, independently reprove §5.60 Skoda–El Mir, or audit any excluded approximation programme.

- **`POME-RADIAL-LELONG-DENSITY-JUMP-001` — low / verified conditional deduction.** For an invariant closed positive current `T` of bidegree `(p,p)`, `1<=p<n`, coefficient `u(t)` from §5.58 and `m=n-p`, its zero extension has exact centered open-ball trace `R^{2m}u(2log R-)` and Lelong number `u(-infinity)`. The decreasing bounded psh truncations `max(log|z|²,-j)` have p-th powers tending **weakly on all C^n** to the radial limit of Lelong 1, while every approximant has Lelong 0. Shell `|z|=exp(-j/2)` has trace mass `exp(-mj)`. This is not a counterexample to the printed theorems; only a warning that weak convergence does not imply Lelong-number continuity. [Complete new English proof, exact source labels and line anchors](reports/2026-10-23-radial-current-shell-density-and-lelong-jump.md).
- **Verified small check:** `checks/check_radial_shell_lelong_density.py`; **546** exact rational shell/open/closed mass algebra cases ran locally. Not a substitute for analytic proof. The 747-row matrix and cumulative ledger were updated without dropping old records or changing historical statuses.
- **Excluded unchanged:** All user-deferred Demailly regularization/approximation, dedicated Bergman/L²/Ohsawa–Takegoshi/multiscale-atlas/positivity-loss programme remain `deferred-by-user` and were not reopened. No project-wide test/build, CI, site publication, formalization, source/body/registry/permanent-tag or main-branch changes. No automatic merge, PR or issue operations.

---

# Pome audit — 2026-10-23: the fixed-ample hyperelliptic test succeeds first at m=1

**Reviewed main** b6933b772f41b45918f7e25ed1afbbb1fd892272; **start-of-session audit head** 7f664ec1776df5c0ebb80d9a13b21b80f5b5cf53, preserved (no reset). Freshly read AGENTS.md, documentation/proof-expansions.md, the current main table of contents (25 chapters / 747 section inventory), and README.md and LATEST.md on review/mathematical-audit. No whole section or project is certified.

**Actually new selected proof coverage:** §§11.29–11.30, specifically strict Levi/Griffiths equivalence, finite-section first jets and coefficient matrices, C² density and convex alternatives (selected proof passages only), the hyperelliptic cover section splitting, the root-weight ramification obstruction, and the fixed-A level-zero test. §11.28 was only context; a previously logged torus result was not repeated. [Complete English report with source-label, permanent-tag, file-blob and physical-line anchors, as well as full new proof](reports/2026-10-23-hyperelliptic-first-ample-twist-is-one.md).

- **POME-HYPERELLIPTIC-FIXED-TWIST-ONE-001** — **low / verified conditional deduction**, NOT an original theorem error. For the exact §11.30 hyperelliptic family with any q>=2 and any fixed FS basis of A=L^q, the first successful twist in Theorem 11.29.9 is exactly **m=1**. The already-printed first *root-weight* level j=q−1 is a different test family: j=qm for the fixed-A family. An explicit nonnegative quadratic combination of products of sections and branch-coordinate sections produces a strictly psh fiber-quadratic function at m=1; m=0 fails by ramification. The proof treats the arbitrary-basis metric, checks positivity on the null line at each branch point, and closes the argument by a compact uniform Schur complement. No general effective m bound is asserted.
- **Verification:** direct symbolic/analytic derivation checked, without a numerical grid or claimed formal verification. No Pome build, full tests, CI, automatic website publication, source/body/registry/permanent tag/main modifications or PR operations. Remote branch commits and blob verification are to be independently checked after writing.

**Strict exclusion:** Demailly approximation/regularization and the dedicated Bergman/L²/Ohsawa–Takegoshi/multiscale-atlas/positivity-loss proof completion programme remain **deferred-by-user**, not examined or certified. Historical ledger and matrix entries are preserved. All 747 ToC sections remain an inventory, not a whole-project review count.

---

# Pome mathematical audit — 2026-10-23: subfamily singularity intersections and sharp CLN collar loss

**Reviewed main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`, with fresh required AGENTS.md, documentation/proof-expansions.md, current integrated ToC (25 chapters / **747 inventory-only sections**), audit branch README.md and prior LATEST.md; initial review-branch head `e54b793736c6e9e926e1e2acdfc5c2580ffa5ba2` preserved, never reset.

**New substantive, specifically limited proof inspection:** §7.28 Theorem 7.28.1 (all-subfamily pole-locus Hausdorff condition, weighted product integrability), §7.30 Proposition 7.30.3 / Eq. 7.30.4 (intersection-dimension bounds, selected cutoff estimates), §7.32 Corollary 7.32.2 (collar-depth mass estimate). §§7.29/7.31 consulted **only as contextual dependencies**. Theorem 7.28.1's full continuity induction, cutoff intricacies and nonexcluded external dependencies remain unverified; no entire section is certified. All precise paths, source labels, permanent tags and physical line anchors: [complete dated English proof](reports/2026-10-23-complete-intersection-pole-mass-and-sharp-cln-collar.md).

- **POME-BT-HAUSDORFF-SUBFAMILY-SHARP-001:** low / `verified conditional deduction`, **not an original-theorem error**. Normal-crossing coordinate logarithms satisfy every Hausdorff subfamily test and have unit classical intersection mass, but NPP product zero; repeated coordinate divisor satisfies singleton tests yet makes the weighted product nonintegrable, demonstrating the importance of the higher-intersection tests.
- **POME-CLN-COLLAR-INVDELTA-OPT-001:** low / `verified conditional deduction`, **not an original-theorem error**. On the unit disc, `u=log|z|²`, `ψ=|z|²−1` gives `||uT||=||T||=1`, collar `Mδ=−log(1−δ)`, hence `δ/Mδ→1`. Therefore Corollary 7.32.2's `δ^{-1}` **exponent** is optimal; the printed numerical constant is not claimed sharp.

**Actual finite software validation:** `checks/check_bt_subfamilies_collar.py` executed **352 integer codimension identities and 500,500 exact rational collar inequalities**, all passed. This is **not** a proof of psh theory. No full project tests or build, GitHub Actions CI, website publication, formal verification, source/body/registry/permanent-tag edits, merge, force push or PR change. The new report, small check, selected section rows of SECTION_MATRIX.md and two finding rows of LEDGER.md were submitted to **review/mathematical-audit only**, with the audit branch unchanged except for normal forward commits; complete remote verification must be checked separately.

**Excluded as requested:** all Demailly approximation/regularization and dedicated Bergman/L²/Ohsawa–Takegoshi/multiscale-atlas/positivity-loss work remains **`deferred-by-user`**, not reexamined, resolved or certified. In particular §7.31.1's general smoothing is a dependency boundary, not an audit task. Historical records and unchanged findings remain intact.

---

# Pome mathematical audit — 2026-10-23: anisotropic MA limits and pluripolar Haar nullity

**Precisely reviewed main:** b6933b772f41b45918f7e25ed1afbbb1fd892272; **existing audit branch preserved** from 102b599aeb30be2eef2d3ecc9df5a350eae489e0 (never reset). Fresh required main AGENTS.md, documentation/proof-expansions.md, current 25-chapter/747-section HTML ToC, and review-branch README.md and LATEST.md were read. The section count is **inventory only**, not mathematical certification.

**Direct first-time nonexcluded proof review:** Lemma 6.55.1 and smooth fixed-m part of Proposition 6.55.2 (only lines 31–70); independent Lemma 6.45.1 on Haar-null intersection of pluripolar sets and totally-real slices. The detailed source blob SHAs, source labels, permanent tags, paragraph/line anchors, hypotheses, complete derivations, and affected dependents are in [dated report](reports/2026-10-23-anisotropic-restricted-ma-noncommuting-limits.md). Previously reviewed §6.56 and §9.74 appeared solely as de-duplication crosschecks; prior findings are **not** presented again as new coverage.

- **POME-CAOPAUN-MA-ANISOTROPIC-ITERLIMIT-001** — low, **verified conditional deduction**, **not** a source theorem error. Exact Cauchy-powered-coordinate tail epsilon/(epsilon+r^(2m)); complete family of nontrivial torus weak limits as m→∞, epsilon_m↓0; the two iterated m/epsilon measure limits do **not** commute. Original §6.55.2 takes epsilon↓0 with m fixed, hence remains unrefuted.
- **POME-TOTALLY-REAL-PLURIPOLAR-NULL-001** — low, **verified conditional deduction**, **not** a source theorem error. Maximal real-analytic totally-real submanifolds are locally pluripolar-null in smooth induced volume by holomorphic complexification and real-cube Riesz/Fubini. This properly generalizes the U(n) lemma under exact hypotheses.

**Actual checks:** executed checks/check_anisotropic_ma_limit_order.py in the local Python runtime: **630 exact rational finite identities and bounds PASSED**. This is not a formal proof or a validation of the limiting argument. **Not run:** full project tests or build, CI, browser rendering, website publication, mathematical formal verification. No source/body/registry/canonical-tag/main changes or PR manipulation. The new report, small reproducible checker, matrix and ledger changes were committed on the audit branch; final remote-commit verification follows separately, and successful commit SHAs must not be guessed.

**Strict exclusion remains:** Demailly approximation/regularization and dedicated Bergman/L²/Ohsawa–Takegoshi/multiscale-atlas/positivity-loss proof completion **deferred-by-user** (neither reopened, resolved nor certified). In particular §6.55.2 from line 72 and §6.45.2's smoothing/current-product programme were not audited. All historical finding statuses remain intact.

---

# Pome mathematical-audit checkpoint — 2026-10-23 19:07 Asia/Shanghai

**Current main read:** b6933b772f41b45918f7e25ed1afbbb1fd892272; **review branch preserved** (starting SHA 408d3e0816e2b72756c8bf27a5ae3eae54ecc51c). Freshly read main AGENTS.md, documentation/proof-expansions.md, the 25-chapter/747-section actual ToC, and review-branch README.md and this LATEST.md. Section counts remain inventory, not mathematical certification. The new Markdown report, one exact script, three changed section-matrix rows and three new ledger IDs are on the audit branch, subject to independent final remote verification.

**New, actually selected proof/model review:** §19.1 (graded partial Okounkov series), §10.105.1 (intrinsic/extrinsic submean proof), and the metric-extension boundary of §10.108.2. Precise source labels, permanent tags, physical HTML line anchors, hypotheses, complete proofs/diagnostic and proposed changes: [dated report](reports/2026-10-23-divisorial-okounkov-floor-and-minimal-submanifold-defect.md). §§19.2 and 19.4 were consulted solely to align definitions; §§9.77 and 10.103–104 were already covered and were only rechecked, **not counted as new coverage**.

- **POME-OKO-DIV-FLOOR-SERIES-001** — low, **verified conditional deduction**, not a false theorem: exact P¹ Hilbert/valuation floors, iff-integral literal semigroup closure, pseudometric-zero equivalent ceiling semigroup, partial body [c,d] and non-pluripolar mass d−c for 0≤c<d.
- **POME-REL-MINIMAL-SUBMEAN-DEFECT-001** — low, **verified conditional deduction**, not an error: exact nonnegative monotonicity defect and equality rigidity for nonnegative subharmonic functions on complex submanifolds of Euclidean space, plus curved graph sharpness.
- **POME-TAUT-MODEL-METRIC-EXT-001** — medium **candidate**, not a confirmed theorem error: §10.108.2 passes from an open-locus curvature-bound metric to a compact-resolution multiplier ideal without an explicit controlled extension lemma. The punctured-disc diagnostic shows lower curvature alone is insufficient, but does not refute existence of a better choice of metric.

**De-duplication:** The Fujiki deformation input encountered again in §9.77 was **already logged** as POME-CAOPAUN-FUJIKI-DEFORMATION-INPUT-001 in the prior 2026-10-23 compact-center/cohomology-jumps report. It is not entered anew. The previously checked §§10.103–104 likewise remain historical rechecks.

**Actually executed:** checks/check_divisorial_okounkov_and_submean.py: 266,539 exact rational Hilbert/carry cases, 2,184 nonintegral carry witnesses, seven flat symbolic radial identities and one curved-graph derivative identity passed. These are sanity checks, not formal proofs or a project-wide validation. No whole section certified, no full build, CI, website publication, main/source/permanent-tag changes, new PR, merge, force push or deletion.

**Hard exclusion unchanged:** Demailly approximation/regularization and the dedicated Bergman, L², Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof-completion programme remain **deferred-by-user**, without any reinspection or resolution. Separate L²/relative Bergman inputs in §§10.105/10.108 were explicitly not followed. Historical audit ledgers are preserved below and in LEDGER.md.

---

# Pome mathematical audit checkpoint — 2026-10-23 18:05 Asia/Shanghai

**Freshly confirmed main:** b6933b772f41b45918f7e25ed1afbbb1fd892272. Existing audit branch before writes: 05da6df6c5968380c550de3cadd22dca975a7fd8. Read current main AGENTS.md, documentation/proof-expansions.md, main ToC, audit-branch README.md and audit-branch mathematical-audit/LATEST.md; actual inventory is 25 chapters / 747 numbered sections (**inventory, not mathematical certification**).

**Substantive selected new proof review:** §22.1.54–60 (DH moments, finite-energy tails, monotone volume convergence) and §20.4.19–24 (Gauduchon-normalized positive-current decomposition and net topology). Dependencies §19.5.26(1), §19.6.18–19, §11.31.3 directly crosschecked, not fully certified. Stable tags, current-main blobs, exact integrated line anchors and full proofs: [dated English report](reports/2026-10-23-dh-volume-profile-wasserstein-and-gauduchon-net-continuity.md).

- **POME-NA-DH-W1-PROFILE-001**, low / **verified conditional deduction**: in the common positive-mass left-end model and finite-first-moment setting, W1 of normalized DH measures equals L1 difference of their cumulative level-volume profiles divided by mass. Ordered curves specialize to first-moment difference / mass. Exact terminal-atom formula included. Distinct from prior nonquantitative stochastic-order finding.
- **POME-BC-GAUD-NET-L1-001**, low / **verified repair**: validates the weak-current-to-L1-potential continuity claim in Lemma 20.4.20 for arbitrary directed nets by uniform qpsh L1 compactness and uniqueness of all subnet limits; original statement not shown false.

**Independent arithmetic check:** 22,251 exact rational finite-atom W1/survival-profile cases passed, not a proof of NA analytic facts. New check script: [checks/check_dh_w1_profile.py](checks/check_dh_w1_profile.py). Updated 747-row [SECTION_MATRIX.md](SECTION_MATRIX.md) and historic [LEDGER.md](LEDGER.md) without resetting prior findings. The existing §19.6.16 false statement and §22.1.88 concave-envelope issue remain unresolved; neither reclassified nor repeated as new progress.

**Scope:** Demailly approximation/regularization and the dedicated Bergman, L2, Ohsawa–Takegoshi, multiscale and positivity-loss proof-completion programme remain entirely **deferred-by-user**, not reexamined, resolved or certified. No source/body/canonicalization/permanent-tag change, main write, website publication, GitHub Actions CI, PR/issue creation, merge, full-project tests/build, or formal verification was performed. Remote commit outcome should be verified separately after this checkpoint update.

---

# Pome mathematical audit checkpoint — 2026-10-23 17:37 Asia/Shanghai

**Freshly confirmed main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`; existing review branch before writes: `f3435da74f5eb748d1d15529b04f3f600ceec4f8`. Re-read main `AGENTS.md`, `documentation/proof-expansions.md`, current main and 25-chapter / **747-section** ToC, and review branch `README.md` / `mathematical-audit/LATEST.md`. The 747 sections are inventory, **not mathematical certification**.

**Actual new inspection:** first selected integrated proof review of §§13.14–13.15; contextual checks of Lemma 5.26.2 and Eq. 5.27.9 only. The `§13.15.2` regularization citation is **deferred-by-user**, not followed. Full assumptions, exact tags, HTML anchors, complete arguments and limitations are in [the dated English report](reports/2026-10-23-root-integrable-weights-and-lr-mass-concentration.md).

- `POME-NPP-WEIGHT-ROOTCAP-001`, **verified conditional deduction / low**: root-integrable weight composition yields *linear* capacity domination; for polynomial weights `(1-u)^(-q)`, `q>n`, this improves the existing sublinear power capacity bound, retaining its broader `q>n-2` range. Conditional upon internal Bedford–Taylor/chain-rule inputs; no source result refuted.
- `POME-HERM-EXP-LR-001`, **verified conditional deduction / low**: the smooth prescribed-mass family has quantitative `O(epsilon_j)` convergence in every fixed finite `L^r` for potentials and `exp(-p w_j)-1`; an unbounded infinite-mass family enjoys analogous `L^r` convergence. This does not imply control of MA mass.

**GitHub synchronization:** verified English report commit `7ac66a8c5d3a6b9617850296f30528a4c0b942c1`, small check script commit `145a407364103b86b51e9b385d835bdfd1005bae`, cumulative 747-row `SECTION_MATRIX.md` update `537b648750eb2e63ab3e0af61aa7fb904eb0751c` (preserving previous entries), cumulative `LEDGER.md` update `1aa7e87cbf80c3c44e925fec3c3de2fdf7cecdbe` (historical statuses preserved). **175 exact scalar SymPy consistency cases passed** (not a formal proof). Remote file/head verification is recorded after this checkpoint. No complete project build, CI, publication, main, source, permanent tag or registry change.

**Strict user exclusion:** dedicated Demailly approximation/regularization, Bergman/L²/Ohsawa–Takegoshi/multiscale/positivity-loss proof-completion remains `deferred-by-user`, not reopened, resolved or certified. Many sections remain inventory-only or partially reviewed; keep rotating.

---

# Pome mathematical audit checkpoint — 2026-10-23 16:57 Asia/Shanghai

**Fresh main** `b6933b772f41b45918f7e25ed1afbbb1fd892272` and current 25-chapter / **747-section** table of contents (inventory, **not** certification). Freshly read `AGENTS.md`, `documentation/proof-expansions.md`, current `main`, and `README.md` / `mathematical-audit/LATEST.md` on this review branch. Actual new selected proof review: §§6.56, 9.74, 9.77, 10.103, 10.104, with upstream §9.72 and §9.76 **dependency-only** checks. No entire section or external theorem independently certified.

New [dated English mathematical report](reports/2026-10-23-compact-center-uniform-lelong-and-cohomology-jumps.md), committed at `2f53c1da18d822f7918af9dc044c3dbc7b5bea02` and verified after the Markdown delimiter cleanup commit `fe9d0488c0b4636de1341cca5daa1d344397064a`. The [cumulative 747-section coverage matrix](SECTION_MATRIX.md) was synchronized without dropping earlier rows; its current blob `7267edf5bce044f26ec3a652f39121d1b29d4008` matches the local matrix byte-for-byte. The [cumulative ledger](LEDGER.md) was also newly synchronized on this branch, retaining historical findings and their statuses (commit `f3164d2893ed84f0b0ef6e5a948774261dcdf432`). No new arithmetic/regression script was run or copied.

- `POME-CAOPAUN-CENTER-UNIFORM-LELONG-001` — **verified conditional deduction**, low: §6.56 global normal-bundle current gives exact (Q_a=\omega_C-a\Xi) and one **uniform-in-(y\in C_0)** compact-center Lelong bound, retaining the defined analytic residual hypothesis; original theorem is not false.
- `POME-CAOPAUN-PIC0-HODGE-JUMPS-001` — **verified conditional deduction**, low: vector-bundle (h^q(F\otimes\rho)) is upper semicontinuous under arbitrary `Pic^0` nets, not necessarily constant; the existing Euler-characteristic lemma is correct.
- `POME-CAOPAUN-FOLIATION-CYCLE-INPUT-001` — **external dependency**, medium: Ou2025/Barlet generic compact-cycle and meromorphic leaf quotient theorem at §9.74, openly cited but not internally proved.
- `POME-CAOPAUN-FUJIKI-DEFORMATION-INPUT-001` — **external dependency**, medium: Fujiki's Kähler deformation invariance of uniruledness needed for §9.77.1; the inspected formal contraposition is correct.

**Scope:** completely skip Demailly approximation/regularization and the dedicated Bergman/L²/Ohsawa–Takegoshi/multiscale/positivity-loss completion programme. Historical notes remain **`deferred-by-user`**, neither reopened, resolved nor certified. §§6.55 and 10.108's excluded analytic programmes were not reviewed. No source/body/registry/canonicalization/permanent-tag changes, `main` changes, CI, build, automatic merge, PR, formal verification or website publication. Only review-branch audit Markdown was written; exact section-level work and external dependencies are in the new report and ledger. The separate lengthy historical `COVERAGE.md` local log has not yet been completely uploaded; the newly synchronized full `SECTION_MATRIX.md` is the durable authoritative section coverage matrix.

---

# Pome mathematical audit checkpoint — 2026-10-23 15:54 Asia/Shanghai

**Reviewed `main`:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`; current table of contents: 25 chapters / 747 sections (inventory, **not certification**). Refreshed `main/README.md`, `main/AGENTS.md`, `main/documentation/proof-expansions.md`, and review-branch `README.md` / `mathematical-audit/LATEST.md`. **Actual new selected proof reading:** §5.50 (plurithin annuli and plurifine limits), §5.51 (nonpluripolar smooth curves), §5.57 (sphere logarithm and plane averages), with only limited internal dependency checks on §4.1.17 and §5.47.10. No whole section or upstream theorem chain certified.

New dated [English report](reports/2026-10-23-sharp-spherical-log-average-and-nonpolar-zero-dimensional-cantor.md), **independently fetched after GitHub commit `254f710de666362e8e354e46363b66c7d29e775a`**, and new [small exact check](checks/check_spherical_log_and_cantor_capacity.py), independently fetched after commit `be4ad6ff03848ac848cb16b2b51940a5e186c300`. The exact-rational script covers 239 finite identities/separation checks, **not** analytic/formal proofs.

- **POME-SPHERE-LOG-HARMONIC-001** — low / `verified conditional deduction`: the invariant-sphere logarithmic average has optimal constant `c_n=-H_{n-1}`; its absolute moment has an exact binomial formula, with sharp upper constant `H_{n-1}` (equality for `|z|<=1`). Strengthens Lemma 5.57.1, does not refute it.
- **POME-SMOOTH-NONPOLAR-CANTOR-CAPACITY-001** — low / `verified conditional deduction`: the specific Cantor slices in Theorem 5.51.1 have classical logarithmic capacity at least `Q^{-2}` uniformly and the zero-dimensional transverse Cantor set has capacity at least `(2*10^6)^{-1}`. This is **not** relative Green capacity and is not an error in the original theorem.

**Scope:** all Demailly approximation/regularization and dedicated Bergman/L²/Ohsawa–Takegoshi/multiscale-atlas/positivity-loss proof-completion remains strictly **`deferred-by-user`**, neither examined, resolved nor certified. No source/body/registry/canonicalization/permanent-tag, `main`, published site, CI, build, formalization, merge or PR changes. The complete local 747-row matrix and consolidated historical ledger still require separate synchronization; prior remote history is preserved below. All remote writing in this checkpoint was to `review/mathematical-audit` only.

---

# Pome mathematical audit checkpoint — 2026-10-23 15:00 Asia/Shanghai

**Fresh reviewed main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`; existing audit branch read at `c4ccdc092ac7b6da2cea58ee228a475c7b8ba4bf` before writing. Fresh main `AGENTS.md`, `documentation/proof-expansions.md`, main/branch `README.md`, existing audit `LATEST.md` and current 25-chapter/747-section table of contents checked. The inventory is **not** mathematical verification. Only selected integrated proof steps were read, in §§11.16–11.19 and 11.24–11.26 (including contextual §11.25 and §11.24 historical audit crosscheck). **No whole section certified.**

New detailed audit-only English report: [continuous Hermitian adjoint stability and projective-complement properness](reports/2026-10-23-continuous-hermitian-adjoint-stability-and-projective-properness.md), committed as `fcfd098a310608711c183542e136634e9141d5af` and independently read remotely. Small [finite-state rational resolvent check](checks/check_stationary_resolvent_matrix_analogy.py), committed as `61ed677450473e95a0143e6e676757c0cab60109`; **7 exact-rational finite-state examples executed locally**, NOT a PDE or formal proof.

- **POME-HERM-ADJOINT-C0-LP-LIPSCHITZ-001** — low / `verified conditional deduction`: unique nonnegative normalized L^{p'} adjoint density of a continuous positive Hermitian trace operator on compact connected X, locally Lipschitz in the C^0 coefficient topology for p>2n; arbitrary directed-net strong L^{p'} stability. Conditional on the full Fredholm/comparison premises of Lemma 11.24.1.
- **POME-PROJ-COMP-BASE-PROPER-001** — medium / `proof gap`: the constructed exhaustion in Theorem 11.18.2 relies on compactness of the ambient projective bundle, but compact X is not stated in its section-local hypotheses. A trivial bundle over C refutes the *claimed properness of that cutoff*, not the convexity theorem. Proposed repair: state compact X, or supply a new noncompact properness argument.
- **POME-STEIN-OKA-WEIL-INPUT-001** — medium / `external dependency`: the global Oka–Weil approximation invoked by Lemma 11.16.2 and Theorem 11.16.3 remains an explicit unproved-in-this-audit analytic input; the elementary polynomial separation Lemma 11.16.1 is internally proved.

**Scope and synchronization:** this checkpoint adds audit-only documents to `review/mathematical-audit`, not main, manuscripts, registries, tags or the published reading edition. The detailed cumulative local 747-row coverage matrix and the most recent local ledger are not yet fully synchronized; historic remote records are preserved, not overwritten. Earlier `POME-HERM-CZ-INTERNAL-001` / `POME-HERM-ABP-001` findings are unchanged and not new progress. Demailly approximation/regularization and dedicated Bergman/L²/Ohsawa–Takegoshi/multiscale/positivity-loss completion stay **`deferred-by-user`**, neither reopened nor certified. No project-wide tests/build, CI, formal verification, automatic merge, PR or website publication.

---

# Synchronization checkpoint — 23 October 2026

The author explicitly authorized another normal push attempt. This synchronization uses the existing `review/mathematical-audit` branch without resetting it and does not change `main`, source manuscripts, generated reading pages, registries, or permanent tags.

## Newly synchronized and independently verified

- [HN exterior-power slopes and movable tensor-semistability dependency report](reports/2026-10-23-hn-exterior-polygon-and-movable-dependency.md), committed as `b304a27f0ce6d0d58bb37f9b513949a4d15ce0fe`. The remotely read content blob `c91d66d8138c6de441ddd9ae89535cb58f6a86d9` matches the local report exactly.
- [Exact HN exterior-power consistency check](checks/check_hn_wedge_polygon.py), committed as `27b1ca9edfed4783ec27b7602f31cedfb675219c` and independently fetched after writing. It is a finite combinatorial consistency check, not a proof of analytic sheaf semistability.

The report's closing write log describes the earlier 12:53 audit checkpoint and its failed write attempt. It is preserved as history; the successful user-authorized retry recorded here supersedes that earlier report-only synchronization status.

## Mathematical status and actual coverage

The reviewed main remains `b6933b772f41b45918f7e25ed1afbbb1fd892272`, also confirmed by a fresh branch read during this synchronization. The report records selected proof inspection of §§10.106–10.107 and §9.76, with dependency-limited checks of §§9.75, 10.109 and 19.11. It does not certify those entire sections or the full project.

- `POME-CAOPAUN-HN-WEDGE-POLYGON-001`: **verified conditional deduction**. The maximum and minimum slopes of reflexive exterior powers are the sums of the largest and smallest repeated HN slopes, conditional on the stated movable-class tensor-semistability theorem.
- `POME-CAOPAUN-MOVABLE-TENSOR-INPUT-001`: **external dependency**. The Ou/Toma movable tensor-semistability input remains a genuine unproved-in-this-audit prerequisite, not a false theorem.

This synchronization does **not** upload the entire accumulated local archive. Other pending reports, the cumulative local section matrix, ledger and coverage log remain pending unless separately verified as synchronized. Their old remote versions must not be mistaken for the complete current local record.

Demailly approximation/regularization and the dedicated Bergman/L²/Ohsawa–Takegoshi/multiscale/positivity-loss completion programme remain **deferred-by-user**, neither resumed nor certified. No project build, CI setup, website publication, automatic merge, force push, or new mathematical review was performed by this synchronization. Historical remote text is preserved below.

---

> Integration status — 18 October 2026: the audit branch has been incorporated into `main`. Confirmed capacity and placement defects are repaired; see [the integration report](reports/2026-10-18-integrated-corrections.md). Demailly approximation and its dedicated prerequisite audit remain deferred by the author. Older priorities, branch-only restrictions, and scheduling descriptions below are historical, not current instructions. This integration does not certify the unreviewed chapters or every external dependency.

# Audit checkpoint — broad-scope review, 17 October 2026

## Current mandate (supersedes older priorities)

The author has explicitly requested that Demailly approximation be ignored and that the rest of the entire project be checked. Skip that approximation programme and its dedicated Bergman/L2/extension/multiscale prerequisite work. Do not keep returning to it under another dependency label. Existing notes remain historical, deferred-by-user, NOT resolved or certified. The old first-priority and next-unit text in README.md and the historical checkpoint below is superseded by this instruction.

The hourly schedule and authorized pushes to `review/mathematical-audit` continue. Review the other chapters in rotation, documenting mathematical errors, genuine duplicates, proof omissions, hypotheses and actual external dependencies. Hironaka remains the permitted external exception. Preserve attribution. No direct changes to main, source manuscripts or published pages, and no automatic merge, publication or CI.

## New reviewed coverage

Reviewed main: `66f8176be2a006b9404ae6db49ee15621dea5523`.
Starting audit head: `91f48c1323d7c717c53204a6bc3b3d362010b726`.

[Whole-project coverage matrix](COVERAGE.md) records all 25 current chapters; it is an initial broad-pass ledger, not a claim that those chapters have been checked.

[New report: POME-CAP-001](reports/2026-10-17-open-set-capacity-counterexample.md).

**Confirmed error:** Proposition 13.12.7, tag `D56D6D4A5E94`, asserts whole-open-set capacity convergence of monotone local psh nets. Its own Definition 13.12.6 tests all of U. On the projective line with normalized Fubini–Study theta and U the unit disc, u_j=|z|^(2j) are uniformly bounded smooth psh functions decreasing to zero, but Cap_theta({u_j>1/2})=1 for every j. The report constructs admissible global circle-mass test potentials and proves the exact capacity value. This failure already occurs for sequences; adding uniform boundedness is not a repair.

**Correction direction, not yet integrated:** distinguish local convergence on every compact subset of U from global convergence on all U. Supply the corrected net theorem separately and inspect actual downstream uses. Do not silently change the meaning of capacity convergence everywhere. Keep POME-CAP-001 open until a reviewed correction is integrated.

The mathematical body of Section 13.12 was read, including both definitions above and Theorem 13.12.8. The latter's enclosing section defers its proof to GZ17; locating an internal replacement is pending. No falsehood of that weighted current-convergence theorem is asserted. The rest of Chapter 13 has not been certified. No full project tests, build, or formal verification were run in this increment; the counterexample is justified analytically, not by a numerical test grid.

## Next broad-scope units

1. Chapter 16: envelope order, supremum regularization, model-potential limits and exact proof dependencies.
2. Chapter 7: local Bedford–Taylor/capacity statements, comparisons and limits; distinguish local from global quantifiers.
3. Chapter 17: energy, geodesic and test-curve statements, then other unreviewed chapters in COVERAGE.md, including Hermitian volume/torsion and the algebraic, toric and non-Archimedean parts.

Track applications of POME-CAP-001 alongside this rotation; do not spend all future sessions in one chain. Preserve existing unresolved items outside the excluded programme. Detailed prior reports not yet synchronized remain historical pending artifacts, not a reason to resume the excluded priority.

## Superseded checkpoint retained as history — not the current work queue

Reviewed main: `66f8176be2a006b9404ae6db49ee15621dea5523`.
Audit branch has new coverage note: [POME-DEP-009, Richberg/psh primitives](reports/2026-10-17-richberg-coverage-check.md).

Newly read integrated proofs: Theorem 3.4.12 (subharmonic convolution); Theorem 5.9.1 and Proposition 5.9.2 (positive Hessians); Lemma 6.3.2 (Fejer barrier); Lemma 6.3.3 (Richberg); Theorem 6.3.4 (strict psh exhaustion). Quantitative local bump, convex regularized-max and finite gluing steps checked; no new confirmed false theorem. A separate detailed English review and exact-rational check remain local.

Still open: POME-REG-001/002 and conditional POME-REG-009 (prescribed nonclosed continuous positivity bound); POME-XREF-001; POME-DEP-001/005–008; global duplicate and dependency ledger. Third–eighth detailed reports remain unsynced.

Next: verify lower subharmonic/distributional primitives, revisit variable-scale Bergman comparison and underlying L2 estimates. This review did not run the full project test/build nor change published material.
