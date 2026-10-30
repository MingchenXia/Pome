# Latest mathematical audit checkpoint — 2026-10-31 — sharp central-binomial cofactor bounds and broad cross-checks

**Reviewed production main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. [Exact pinned proof and selected cross-chapter checks](reports/2026-10-31-sharp-binomial-cofactor-and-cross-chapter-guard.md).

- **`POME-MA-COFACTOR-SHARP-CENTRAL-BINOMIAL-001` — low / verified conditional deduction:** Printed Eq. **14.21.8** is **correct but nonsharp**. For \(k=n-1\), \(H=A+B\), \(T=\sum_{j=0}^{k}A^jB^{k-j}\), the sharp positive-form comparison is \(\binom{k}{\lfloor k/2\rfloor}^{-1}H^k\le T\le H^k\). Both constants are optimal even for semipositive forms with equal *zero* top determinant, via complementary coordinate-rank models. The exact beta-average formula \(T=(k+1)\int_0^1(tA+(1-t)B)^kdt\) gives an independent check. Optional stronger coefficient in the §14.21 cofactor proof; this is **not** a new uniqueness theorem or a repaired false statement.
- **Actual newly selected proof coverage:** §14.20.1 and §14.21.8–9, cofactor segment of §14.21.3, plus selected independent §9.5.6 finite-map/zero-set argument and the **smooth algebraic part only** of §11.1.7. Prior records concerning §§9.5 and 11.1 are retained, not duplicated. The §11.1.7 bounded-potential approximation citation remains conditional/**deferred-by-user**, not reopened. **25 chapters / 747 numbered ToC sections / zero complete mathematical section certifications.** No tests/build/CI/publication/formalization or source edits.

---

# Latest mathematical audit checkpoint — 2026-10-31 — sharp closed-class L1 scalar and probability bounds

**Reviewed production main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. [Complete anchored conditional proof and optimality](reports/2026-10-31-closed-scalar-sharp-l1-tv.md).

- **POME-CLOSED-LOGPART-SHARP-L1-TV-001 — low / verified conditional deduction:** For closed semipositive big `theta` on a compact Kähler manifold with the prescribed ordinary-type scalar equation available, the closed-mass identity gives `B_phi(F)=log(m_phi)-log∫exp(F)dV` and unique supporting measure `nu_F=exp(F)dV/∫exp(F)dV`, extending printed Eq. 11.37.2 beyond strictly Kähler `theta`. For `|F|,|G|<=M` and `V=∫dV`, **both** `|B_phi(G)-B_phi(F)|` and `d_TV(nu_F,nu_G)` are at most `exp(2M)||F-G||_{L1(dV)}/V`. This coefficient is sharp for each inequality by two-valued densities on a shrinking measurable set. Printed results are correct; this is not a general nonclosed Hermitian statement or a new mass/existence proof. Distinct from earlier L-infinity/tanh TV findings.
- **Actual new proof-level coverage:** selected Eq. 11.33.1 / Theorem 11.33.5 and Eq. 11.37.2 / Proposition 11.37.3 (incremental, not previously unreviewed sections). Theorem 13.8.7 and Theorem 15.12.1 are conditional internal dependencies; excluded regularization proofs not reopened. **25 chapters / 747 numbered ToC sections / zero entire-section mathematical certifications.** No project tests/build/CI/publication/formalization; historical issues and excluded programme remain **deferred-by-user**.

---

# Latest mathematical audit checkpoint — 2026-10-31 — exact quadratic Bedford–Taylor Dirichlet envelopes

**Reviewed production main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. [Complete pinned proof and source anchors](reports/2026-10-31-quadratic-dirichlet-spectral-envelope.md).

- **POME-BT-QUADRATIC-DIRICHLET-EIGENVALUE-001 — low / verified conditional deduction:** For Hermitian $A$ and quadratic boundary data $\varphi_A(z)=z^*Az+2\operatorname{Re}P(z)+c$ on the unit sphere, the homogeneous ball Dirichlet solution is exactly $H_A(z)=\varphi_A(z)+\lambda_{\min}(A)(1-|z|^2)$. The Hessian $A-\lambda_{\min}(A)I$ is semipositive and singular; the unique Perron interpretation is conditional on existing §7.7.4 comparison/uniqueness. For $A_t=(1-t)A+tB$, the exact concavity defect is $[\lambda_{\min}(A_t)-(1-t)\lambda_{\min}(A)-t\lambda_{\min}(B)](1-|z|^2)\geq0$. Equality for $0<t<1$ is equivalent to a common minimum eigenvector; orthogonal $2\times2$ diagonal projectors produce strict defect $(1-|z|^2)/2$. For $A\geq0$, the same formula gives the explicit §7.7.5 global quadratic balayage. This **does not repeat** the earlier boundary sup-norm isometry finding.
- **Actual fresh coverage:** first selected §7.7.6–7 maximality proof check; §7.7.4/5 uniqueness/gluing context and §7.3.11 comparison as a conditional internal input only. Exact reading-version blob and source/permanent tags, paragraphs and line anchors appear in the report. **25 chapters / 747 current numbered ToC sections / zero completely certified mathematical sections**. Five exact-rational local sanity checks were executed; no project tests/build, CI, publishing or formal verification. All historical findings and user-excluded Demailly/regularization/Bergman/L²/OT/multiscale/positivity-loss programme remain unchanged and **deferred-by-user**.

---

# Latest mathematical audit checkpoint — 2026-10-31 — exact Newtonian shell Gram matrix and polynomial accumulation threshold

**Reviewed production main:** b6933b772f41b45918f7e25ed1afbbb1fd892272. [Exact source-pinned proof, sharp convergence criterion/rate and signed incompleteness distinction](reports/2026-10-31-newton-spherical-shell-polynomial-threshold.md).

- **POME-GREEN-SHELL-GRAM-THRESHOLD-001 — low / verified conditional deduction:** A new all-shell Gram formula in classical §4.5.5 gives \(I(\sigma_{r_j}-\sigma_1,\sigma_{r_k}-\sigma_1)=\delta_{\max(j,k)}\), \(\delta_j=r_j^{-1}-1\). For any strictly increasing \(r_j\uparrow1\), signed shell partial sums are energy-Cauchy **iff** \(\sum j\delta_j<\infty\). For \(r_j=1-j^{-p}\), \(j\ge2\), this is exactly **\(p>2\)**, and the squared tail has sharp asymptotic \(2n^{2-p}/((p-1)(p-2))\). Despite Cauchy convergence, no signed Radon energy limit exists because the open-ball restriction has infinitely many unit-mass shells approaching the compact boundary. This is a quantitative **new** criterion extending, not repeating, the already printed geometric signed-incompleteness example or the separate historical positive-shell convergence finding. Original printed §4.5.4 and Example §4.5.5 remain correct; §4.5.2's energy pairing is a conditional internal input.
- **Precisely new coverage:** selected classical potential theory §4.5.5 Gram/accumulation and §§4.5.2/.4 hypotheses; §4.5.6 and Martin §§4.5.8–13 background only. **25 chapters / 747 numbered actual ToC sections / zero complete-section certifications.** Sixteen exact-rational finite-Gram comparisons were executed, but no project tests/build/CI/formalization. All prior findings and user-deferred Demailly regularization/Bergman/L²/OT/multiscale/positivity-loss work remain unchanged. Only English audit notes/check script were added; main, source, registry, website, tags were not modified.

---

# Latest mathematical audit checkpoint — 2026-10-31 — sharp (L^p) atomic trace Poisson stability and the (L^1) obstruction

**Reviewed main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. [Complete anchored proof, exact (L^1) counterexample and smooth endpoint instability](reports/2026-10-31-atomic-trace-poisson-sharp-lp-endpoint.md).

- **POME-TRACE-POISSON-LP1-SHARP-001 — low / verified conditional deduction (printed Theorem 20.3.15 correct):** For a compact curve, fixed atomic trace (D) of mass (d<M), and normalized nonnegative densities (f,g\in L^p), (p>1), the uniquely normalized **bounded Poisson corrections** obey the sharp-topology stability estimate `||s_f-s_g||_infinity <= (M-d) C_{Y,eta,p} ||f-g||_p` with `C=sup_x ||G(x,.)||_{p/(p-1)}<infinity`. An exact affine formula also isolates the dependence on total atomic mass, not its locations. **The (p>1) assumption cannot universally be replaced by (p=1):** an explicit positive integrable density proportional to `1/(r^2 log^2(1/r))` has an unbounded logarithmic Green potential and no solution in the smooth ordinary trace type. Even smooth strictly positive probability densities may converge in (L^1) while their normalized smooth Poisson solutions fail to converge uniformly (rescaled bump of weight `1/|log epsilon|`). This is a proof of a precise endpoint obstruction, **not** a false printed theorem.
- **New selected coverage:** direct §20.3.15 proof and normalization; §20.3.10 Green/atomic mass used as a stated internal input; §20.3.13 context only. **25 chapters / 747 actual ToC sections / zero complete mathematical-section certifications.** Existing errors, gaps, dependences and deferred-by-user Demailly regularization/Bergman/`L^2`/OT/multiscale/positivity-loss work unchanged. Notes-only: no source, main, registry, site, CI, build or formal verification.

---

# Latest mathematical audit checkpoint — 2026-10-30 — exact shifted-grid Haar averaging and one infinite-order equivariance generator

**Reviewed main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. [Source-pinned proof report](reports/2026-10-30-shift-averaging-and-one-rotation-grading.md).

- **POME-TORIC-HAAR-SHIFT-EXACT-001 — low / verified conditional deduction:** Theorem 21.7.3 (source `foundations-of-pluripotential-theory:364BCD30`, tag `831AEEB7084F`) admits a finite-`k` **exact** Haar-shift identity for any integrable compactly supported weight: the average of normalized shifted-grid sums equals its integral. On `[0,alpha]`, count variance is exactly `{k*alpha}(1-{k*alpha})/k^2 <=1/(4k^2)`. The sharp deterministic `O(1/k)` error recorded earlier is *different* and not repeated. A five-case exact-rational script was executed successfully.
- **POME-NA-ONE-GENERATOR-GRADING-001 — low / verified conditional deduction:** Lemma 22.1.94 (source `sgpt:AB6FE74C`, tag `76252E7717AC`) needs only **one** multiplier `a` of infinite multiplicative order with `sigma_a(I) subset I` to force full `C^*` grading. A finite Vandermonde inversion proves the claim without topological density; `I=(t^q-1)` is the sharp root-of-unity obstruction. The existing canonical-filtration finding remains separate, as does §22.1.96's external GAGA input.
- **Exact new mathematical coverage:** the finite-shift quantifier in §21.7.3 and the one-generator algebraic hypothesis of §22.1.94. §§21.9.5/22.1.96 were **context/dependency only**; no full-section or upstream verification. **25 chapters / 747 numbered ToC sections / zero complete mathematical-section certifications**. All earlier errors/gaps/deferrals unchanged; dedicated Demailly/regularization/Bergman/`L^2`/OT/multiscale/positivity-loss programme **deferred-by-user** and not reopened. Audit-only, no main/source/site/CI/build/formalization edits.

---

# Latest mathematical audit checkpoint — 2026-10-30 — sharp Perron endpoint contraction and nonsmooth convex subgradient nets

**Reviewed production main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. [Complete proof, original source/permanent tags, physical lines and pinned main HTML blobs](reports/2026-10-30-perron-endpoint-stability-and-convex-subgradient-nets.md).

- **POME-PERRON-AFFINE-ENDPOINT-CONTRACTION-001 — low / verified conditional deduction:** direct new early §17.16.2/.3/.6/.7 proof audit yields a **sharp time-affine two-endpoint Perron comparison**, with coefficients \(1-t,t\). Consequence: arbitrary directed nets of uniformly perturbed endpoints give jointly uniform time/space convergence of Perron segments (off their common pole set), without sequential compactness. The statement works for smooth nonclosed Hermitian backgrounds. The printed results remain correct; §5.24 and §5.40 inputs are not independently certified.
- **POME-CONVEX-SUBGRAD-NET-SQUEEZE-001 — low / verified conditional deduction:** direct new §21.11.63 support-line proof check extends the correct **one-dimensional sequential derivative lemma** to **all subgradients, arbitrary directed nets and finite dimensions**, without assuming the approximants differentiable or the touching upper bound convex. Alternating affine slopes under \(g(x)=|x|\) show the touching function's differentiability cannot be omitted.
- **Precisely selected coverage:** §§17.16.2/.3/.6/.7, §21.11.63; §21.11.20 contextual only. **25 chapters / 747 current ToC sections / zero complete mathematical section certifications**; old findings untouched. Demailly regularization/Bergman/L²/OT/multiscale/positivity-loss remains **deferred-by-user**, not revisited. **Audit-only**, no production, CI, build, or publication.

# Latest mathematical audit checkpoint — 2026-10-30 — test-curve Choquet dead slices and a conditional complete local repair

**Reviewed production main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. [Exact integrated labels/line anchors, diagnostic model, conditional repair and independent Hessian-scope guard](reports/2026-10-30-test-curves-choquet-dead-slices-and-hessian-guard.md).

- **POME-TC-CHOQUET-DEAD-SLICES-001 — low–medium / proof gap (verified conditional local repair proposed, not integrated):** Proposition **17.15.31** at lines 680–684 falsely calls **all** finite-join rational slices `PSH(X,theta)` before invoking §5.14.3: if the selected subset's terminal maximum is **below** rational `q<M`, its slice is identically `-infinity`. Explicit `P^1` step-curve parameters `b=0,2`, `q=1` refute **the proof inclusion only**, not the theorem. Restrict the Choquet family to `Fin_q(I)={J: max_{j in J} Gamma^j_max >= q}`, including the **equality** endpoint allowed by §17.12.3; discarded terms are all `-infinity`. Countable selection then works, and §17.12.5 reconstructs every real slice from rational ones, avoiding additional nonlinear mass-continuity appeals. Earlier **POME-CHOQUET-TOPOLOGICAL-REPAIR-001** is a distinct already-proposed repair of foundational §5.14.3, not repeated.
- **Independent breadth:** first selected §§8.11–8.12 Hessian capacity, torsion, weighted convergence, maxima, and positive-mass steps; the `omega^(n-q-2)` exponent in §8.11.4 is **legitimate** because Chapter 8 explicitly assumes `2<=m<n`—no false-positive issue opened. **Actual selected** §§17.15.20/.22/.25/.28/.31; §§17.12.1/.3/.5/.6; §5.14.3 prerequisite statement; §§8.11–8.12 designated proof steps. **25 chapters / 747 ToC sections / zero completely certified sections**. Existing statuses and all user-excluded Demailly/regularization/Bergman/L²/OT/multiscale/positivity-loss work remain **deferred-by-user**. Audit-only, no main/body/source/tag/site/CI/build/formal verification.

---

# Latest mathematical audit checkpoint — 2026-10-30 — Grassmannian radial moment threshold and malformed equation permalink

**Reviewed production main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. [Pinned source labels, equations, full sharp radial calculation and exact reader-error evidence](reports/2026-10-30-averaged-plane-radial-power-and-detached-equation.md).

- **POME-PLANE-RADIAL-POWER-THRESHOLD-001 — low / verified conditional deduction:** for averaged complex \(q\)-planes \(A_q\) in \(\mathbb C^n\), \(1\le q\le n\), \((A_q\wedge\beta^q)|_{\mathbb C^n\setminus\{0\}}=(q/n)|z|^{-2(n-q)}\beta^n\) and radial mass is exactly \(2q r^{2q-1}dr\). Therefore \(\int_{|z|<R}|z|^{-\gamma}A_q\wedge\beta^q<\infty\) precisely when \(\gamma<2q\); at critical \(\gamma=2q\), logarithmic damping \([\log(e/|z|)]^{-p}\) works precisely for \(p>1\), with explicit integrals. Original §§5.57.4/7/11 remain mathematically correct; current average-plane calculus is **not** Demailly regularization. This is distinct from earlier `POME-SPHERE-LOG-HARMONIC-001` about random linear-functional logarithms.
- **POME-PLANE-ALIGN-DETACHED-001 — medium / confirmed integration/canonicalization error:** §5.57.7's **Equation 5.57.10**, source `demailly-complex-geometry:26C290A4`, tag `128DDD633F87`, is printed with a raw `277` numbering in the complete two-line proof inequality but detached into a malformed nested-alignment **right-hand-side-only** standalone tag page. Propose one complete tagged equation and one complete permalink; no mathematical theorem is false. The earlier analogous **different** §12.4.3 bug is preserved, not repeated.
- **Actual selected coverage:** §5.57.4 mass/coefficient formula, §5.57.7 Fubini/partial rendering, §5.57.11 recursive identity and the standalone equation page. Previous §5.57.1 checks are context only. **25 chapters / 747 actual numbered sections / zero whole-section certifications**; old ledger statuses and excluded approximation/regularization/Bergman/L²/OT/multiscale/positivity-loss work unchanged as **deferred-by-user**. Audit-only, no source, registry, main, site, CI, project build or formalization action.

---

# Latest mathematical audit checkpoint — 2026-10-30 — smooth full-mass sequence with diffuse polar zero-Lelong limit

**Reviewed production main:** b6933b772f41b45918f7e25ed1afbbb1fd892272. [Fully pinned proof and exact reading-edition anchors](reports/2026-10-30-diffuse-polar-zero-lelong-mass-loss.md).

- **POME-NPP-DIFFUSE-POLAR-SMOOTH-MASS-001 — low / verified conditional deduction:** an explicit superexponential binary Cantor probability μ on P¹ has no atoms and is entirely supported on the pole set of its ω_FS-psh logarithmic potential u, so its current has **all Lelong numbers zero**, classical total mass 1, but **non-pluripolar mass zero**. An explicit elementary kernel family gives smooth strictly positive ω_FS+dd^cu_δ of mass 1, u_δ↓u in L¹/extended capacity, weak current convergence to μ, and **exact mass loss 1** in the non-pluripolar limit. Unlike printed §13.7.6, this defect is completely diffuse and invisible to point Lelong numbers. The older Cantor weak-closure finding is retained separately, not recounted. No false printed theorem alleged.
- **Actual new selected coverage:** §13.2.2/.4 definition and restriction, §13.7.3/.5/.6, §13.11.8, and §13.8.7 statement plus nonexcluded comparison only; **25 chapters / 747 current numbered sections / zero fully certified sections**. §13.8.5's excluded §6.17.1 reference remains **deferred-by-user**, without inspection. All other unresolved/deferred ledgers unchanged. Audit files only; no main, source, registry, tag, site, CI, build, or publication edits.

---

# Latest mathematical audit checkpoint — 2026-10-30 — weighted projective products and complete flat Gauduchon Hessian cones

**Reviewed production main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. [Full self-contained model proof and pinned source anchors](reports/2026-10-30-weighted-projective-products-flat-gauduchon-metric.md).

- **POME-GAUD-WEIGHTED-PRODUCT-FLAT-001 — low / verified conditional deduction:** on `X=prod P^{d_j}`, with fixed normalized product probability `mu_0`, the root variational volume of `theta_a=sum a_j alpha_j` is exactly `[n!/(prod d_j!)]^{1/n} prod a_j^{d_j/n}`, proved directly by pointwise AM–GM and the Kähler minimizing test, **without PDE existence**. Minimizers are precisely constant multiples of `theta_a`. The finite-dimensional background-class Hessian metric is `sum(d_j/n)(da_j/a_j)^2`, globally Euclidean in weighted log coordinates; all geodesics, distances, completeness and constant-volume infinite-distance degenerations follow. The printed `P^1 x P^1` example is not repeated as new. For arbitrary smooth probability the formula is conditional on the printed smooth equation §12.2.3, not a new external-input verification.
- **New selected coverage:** integrated §12.2.1/3 quotient and equality, §12.4.1/4 Hessian normalization, §12.6.1 and higher-factor extension of §12.6.2. **25 chapters / 747 numbered sections / zero fully certified mathematical sections.** All previous issues retain their status. User-excluded Demailly regularization/Bergman/L²/OT/multiscale/positivity-loss work remains **deferred-by-user**, entirely untouched. Audit notes only, no main, sources, permanent tags, site, CI or project build.

---

# Latest mathematical audit checkpoint — 2026-10-30 — sharp entropic modulus for the ideal-class metric

**Reviewed production main:** <code>b6933b772f41b45918f7e25ed1afbbb1fd892272</code>. [Fully anchored report and proof](reports/2026-10-30-ideal-model-entropy-metric-sharp-modulus.md).

- **POME-IDEAL-P1-SHARP-ENTROPY-MODULUS-001 — low / verified conditional deduction:** first selected, nonexcluded §18.7.1–3 stability/proof and §18.6.1 metric review. For one analytic pole of weight \(c\in[0,1]\) on \(\mathbb P^1\), the ideal metric with \(dV=\omega_{\rm FS}\) is **exactly** \(|F(c)-F(d)|\), \(F(c)=c+(1-c)\log(1-c)\). Its **sharp uniform modulus within this family** is \(\delta(1-\log\delta)\), attained near weight 1, so no uniform Lipschitz bound in the Lelong gap is available even for ideal-ordered approximations; at weight 0, distance is \(\delta^2/2+O(\delta^3)\). This refines the earlier **POME-MODEL-P1-FREEBOUNDARY-EXACT-001** by calculating the *ideal metric and endpoint rate*, not by rediscovering the envelope. Proposition 18.7.1 remains correct; its \(L^1\) convergence is qualitative. Full current-main blobs, stable tags, numbered physical lines, independent maximum principle and derivative proof, proposed optional corollary and affected dependents appear in the report. The standalone Python scalar check passed (five midpoint integrals, four endpoint gaps); no build or general verification.
- **Coverage:** actual new selected §§18.7.1–3 and §18.6.1 metric formula; §18.4.8 and §16.21 only constrained comparisons. **25 chapters / 747 current ToC sections / zero completely verified sections**. All previous errors, gaps and user-deferred items retain prior statuses. Demailly approximation/regularization and dedicated Bergman, L², OT, multiscale-atlas and positivity-loss proof completion remain strictly **deferred-by-user**; no work on §§18.7.4–9 or their proof inputs. Changes confined to audit Markdown and one small reproducible scalar check on review/mathematical-audit. No production/main/source/registry/tag/site/CI action.

---

# Latest mathematical audit checkpoint — 2026-10-30 — triangular Hopf meromorphic-field dichotomy

**Reviewed production main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. [Full independent proof and source anchors](reports/2026-10-30-jordan-hopf-meromorphic-field-dichotomy.md).

- **POME-HOPF-JORDAN-MEROMORPHIC-FIELD-001 — low / verified conditional deduction:** among the printed triangular Hopf contractions of §23.3.3, the linear Jordan quotient `F_1(z,w)=(lambda z,lambda w+z)` has **only constant meromorphic functions**, while every `p>=2` quotient `F_p(z,w)=(lambda z,lambda w+z^p)` has meromorphic-function field exactly `C((w+z^p/(lambda-lambda^p))/z)`; their algebraic dimensions are respectively 0 and 1. Proof uses invariant meromorphic-germ homogeneous terms, rational translation rigidity and the already noted nonlinear scalar conjugacy; **conditional** on the separately printed §9.72.1 codimension-two meromorphic Hartogs extension. Theorem 23.3.3 is not false and no older conjugacy result is re-registered.
- **Actual new selected coverage:** full printed statement/proof of §23.3.3 (including iteration formula), §9.72.1 statement and dependency only. §§23.2.14–17/.20/.25–29, §§8.13.4–8 and §§21.7–10 were context/earlier-ledger crosschecks, **not new certifications**. Coverage remains **25 chapters / 747 ToC sections / zero entire-section certifications**. Excluded Demailly approximation/regularization and its dedicated Bergman/L²/OT/multiscale/positivity-loss work remain **deferred-by-user**. Audit-only; no main, sources, CI or publication changes.

---

# Latest mathematical audit checkpoint — 2026-10-30 — an exact constant Monge–Ampère one-form curl on a pluriclosed complex torus

**Reviewed production main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. [Full pinned source anchors and independent calculation](reports/2026-10-30-pluriclosed-torus-constant-curl-and-mass.md).

- **POME-HERM-TORUS-CURL-001 — low / verified conditional deduction; no false theorem:** on a flat complex two-torus, choose a smooth, positive **nonclosed but pluriclosed** off-diagonal Hermitian form \(\omega_\varepsilon\). For every smooth \(u\), the total mass is exactly \(2-\varepsilon^2\), while the Monge–Ampère one-form has **constant nonzero curl** \((d\alpha)_u(v,w)=-\varepsilon\pi\) for explicit trigonometric \(v,w\). Its integral along a small potential rectangle is exactly \(-\varepsilon\pi st\), and the radial-energy differential differs from \(\alpha\) by \(\varepsilon\pi s/2\) at \(u=sv\) in direction \(w\). Thus §11.1 smooth mass invariance does **not** imply §11.2 one-form exactness, even on a manifold admitting Kähler metrics. The printed results are correct.
- **Actual new selected coverage:** §11.2.1–4 one-form/symmetry/primitive tests, §11.2.7/.10/.12 radial differential, and §11.1.5/.7/.10 smooth mass equations; no entire theorem chain or section certified. **25 chapters / 747 current ToC sections / zero complete-section certifications.** Historical findings preserved. Demailly approximation/regularization and dedicated Bergman/\(L^2\)/OT/multiscale/positivity-loss work remain **deferred-by-user**, unexamined. Audit-only: no main, source, registry, site, build, CI, publication, or formalization changes.

---

# Latest mathematical audit checkpoint — 2026-10-30 — entire-function algebra of a Stein open union; optimality of conditional Hölder interpolation

**Reviewed main:** b6933b772f41b45918f7e25ed1afbbb1fd892272. [Full pinned mathematics and proofs](reports/2026-10-30-stein-union-entire-algebra-and-holder-interpolation.md). Audit notes only.

- **POME-STEIN-UNION-ENTIRE-ALGEBRA-001 — low / verified conditional deduction, no false theorem:** the increasing union of affine Stein surfaces of Example 9.27.1 has \(\mathcal O(X)=\pi^*\mathcal O(\mathbb C^2)\). Its holomorphic hulls equal inverse images of ordinary polynomial hulls under \(\pi=(z,w)\); even a singleton on a zero fiber has an entire affine-line hull. Proof uses Laurent coefficients vanishing at the accumulating \(a_j=1/j\). A separate nonaccumulating-integers construction gives a global function \(\sin(\pi z)/w\) not descended from any entire function, proving the accumulation hypothesis matters. Distinct from the previously recorded psh-exhaustion obstruction and the §9.30 Hartogs bridge.
- **POME-HOLDER-ABSTRACT-SMOOTHING-OPT-001 — low / verified conditional deduction:** the last, elementary step from uniform smoothing error \(O(s^q)\) and gradient \(O(1/s)\) to exponent \(q/(1+q)\) is sharp **using only those two estimates**, by a cutoff cusp and mollification at width \(s^{1+q}\). The numerical exponents of printed Theorems 15.5.1/.4 and the conditional continuity modulus in 15.6.1 are consistent. This neither asserts global sharpness within Monge–Ampère solution classes nor verifies the excluded regularization inputs.
- **Actual coverage:** first conditional post-input proof checks in previously inventory-only §§15.5–15.6, incremental new §9.27 global algebra/hulls, §9.26 and §9.30 as contextual comparisons; **25 chapters / 747 numbered ToC sections / zero complete mathematical-section certifications**. All earlier errors/gaps/external dependencies preserved. Dedicated Demailly regularization, Bergman, \(L^2\), Ohsawa–Takegoshi, multiscale and positivity-loss work remain **deferred-by-user**, without reopening. No production/code/site/build/CI/publication/formalization changes.

---

# Latest mathematical audit checkpoint — 2026-10-30 — fixed ordinary restriction with a continuum of atomic trace masses

**Reviewed production main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. [Complete compact projective-product model and exact all-real-weight multiplier-ideal computation](reports/2026-10-30-atomic-trace-continuum-fixed-restriction.md).

- **POME-TRACE-ATOMIC-INTERPOLATION-001 — low / verified conditional deduction; no false theorem.** On `X=P¹×P¹`, `Y={z=0}×P¹`, construct `u_s∈PSH(X,omega_z+omega_w)`, `0≤s≤1`, whose restrictions to `Y` all equal the **same** logarithmic `phi_w`, but `I(tu_s)=O_X(-floor(st)D_w)` for **all real t>0**. Consequently `D_{u_s}=s delta_p`, `Tr_Y^at(u_s)~s phi_w`, and the residual curve measure is `(1-s)omega_w`. The finite ideal trace has **exact sharp** TV error `s-floor(ms)/m<1/m`. This is a compact continuum-strengthening of the existing §20.3.6 strict local example, **not** a repetition of its endpoint; original §§20.3.2/.6/.10/.13 and 20.4.2 correct in this model.
- **Actual selected proof/model coverage:** first direct §§20.3.2/.4/.6/.10/.13 all-real-weight ideal, restriction, Poisson and measure crosschecks, and first selected §20.4.2 curve-case mass sharpness; relevant integrated permanent tags, physical lines, main blobs in the report. **No complete mathematical section certified**; standing inventory **25 chapters / 747 numbered ToC sections / 0 complete certifications**. All historical errors/gaps/external dependencies unchanged. Dedicated Demailly regularization/Bergman/L²/Ohsawa–Takegoshi/multiscale/positivity-loss remains **deferred-by-user** and unexamined. Audit documentation only; no production change/build/CI/publication.

---

# Latest mathematical audit checkpoint — 2026-10-30 — sharp critical DH moments and exact Wasserstein convergence rates for concave roofs

**Reviewed main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. [Complete pinned-label mathematical proof](reports/2026-10-30-okounkov-critical-tail-and-wasserstein-rates.md). Audit-branch notes only.

- **POME-OKO-ROOF-CRITICAL-WASSERSTEIN-001 — low / verified conditional deduction, no false theorem:** For explicit concave roofs `G_alpha=-x_1^(-alpha)-(1-x_1)^(-alpha)` on a fixed n-cube and bounded upper roofs `G_alpha,epsilon`, DH laws converge **narrowly**; limiting negative tail is asymptotic to `2R^(-1/alpha)`, `p`-th absolute moment is finite exactly when `alpha*p<1`, and at/above the threshold the bounded approximants' moments diverge logarithmically/polynomially. For `p>=1`, `alpha*p<1`, monotone quantile coupling gives the **exact** transport cost and sharp rate `W_p^p~2 epsilon^(1-alpha*p) integral_0^infty(t^(-alpha)-(t+1)^(-alpha))^p dt`. In particular explicit `W_1=2(1-(1+epsilon)^(1-alpha)+epsilon^(1-alpha))/(1-alpha)` when `alpha<1`. This is not the older two-curve finite-W1 profile result or the old increasing-test-curve false-hypothesis report; general geometric NA realizability is not claimed. Original §19.6.19 **correct with extended moments**.
- **Actual incremental proof/model coverage:** selected source-anchored §§19.6.1/.5/.7/.18/.19/.22, not a whole-section certification; **first §11.3 introductory Gauduchon page inspected**, *expository/context only* (not mathematical proof coverage). Standing matrix **25 chapters / 747 numbered ToC sections / zero complete mathematical-section certifications**. Historical errors, gaps, external dependencies preserved. Demailly approximation/regularization and dedicated Bergman/L²/Ohsawa–Takegoshi/multiscale/positivity-loss programme remain **deferred-by-user**, untouched. No production edits/build/CI/publication/formalization.

---

# Latest mathematical audit checkpoint — 2026-10-30 — density-one fine neighborhoods and strict density-topology inclusion

**Reviewed production main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. [Complete quantitative proof and halfspace nonthinness counterexample](reports/2026-10-30-fine-neighborhoods-lebesgue-density-and-strictness.md). Audit branch only.

- **POME-FINE-LEBESGUE-DENSITY-001 — low / verified conditional deduction.** Every classical fine neighborhood N of x contains a basic set {u>a} with u(x)>a. If M_r is the sup of u on the closed r-ball, the submean inequality gives outer complement proportion at most (M_r-u(x))/(M_r-a), tending to zero by upper semicontinuity. Thus every fine-open set has Lebesgue density one at each point and every finely continuous metric-valued map is approximately continuous.
- **POME-FINE-DENSITY-STRICT-001 — low / verified conditional deduction.** The measurable set U=R^d\(H\{0}), H={x_1=0}, has density one at every point of U, but is not fine-open at 0. The positive harmonic function |x_1| on B\H is a barrier at 0, so the closed hyperplane is nonthin there by printed Theorem 4.4.22, and removing 0 does not change thinness. Hence classical fine topology is **strictly coarser** than Lebesgue density topology for d>=2. Neither printed theorem is false.
- **Exact scope:** first explicit quantitative reanalysis of selected §4.2.2/.4–.5, conditional §4.2.22 measurability, and new selected §4.4.22 halfspace barrier; **not** the older §4.2.25 classical-versus-plurifine or §4.4.26 Wiener findings. Pinned main physical line anchors and tags in report. **25 chapters / 747 numbered ToC sections / zero full-section certifications**; no earlier statuses closed. Excluded Demailly approximation/regularization and dedicated Bergman/L²/Ohsawa–Takegoshi/multiscale/positivity-loss programme remain **deferred-by-user**, not touched. No main/source/body/registry/site/build/CI/formalization changes.

---
# Latest mathematical audit checkpoint — 2026-10-30 — atomic Dirichlet defect despite total-variation Monge–Ampère convergence

**Reviewed production main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. [Exact new measure-level proof, integrated tags and physical line anchors](reports/2026-10-30-dirichlet-defect-atom-with-tv-ma-convergence.md). Audit branch only.

- **POME-ENERGY-DIRICHLET-DEFECT-ATOM-001 — low / verified conditional deduction, no false theorem.** For smooth strictly Kähler potentials `u_a=a log((|z|²+epsilon_a)/(1+|z|²))` on `P¹`, with `a² log(1/epsilon_a) -> Lambda`, the Monge–Ampère probabilities satisfy **dual total-variation distance at most `2a`** from Fubini–Study, whereas the positive Dirichlet-energy measures `du_a wedge d^c u_a` converge **narrowly to `Lambda delta_0`**. Their total mass equals `a²(log(1/epsilon_a)+O(1))` and mass off every fixed pole neighborhood is `O(a²)`. For `Lambda>0` the gradient measures cannot converge in total variation: the distance to the Dirac limit tends to `2 Lambda`. This is a measure-level sharpening, **not** repetition of old scalar-energy `POME-ENERGY-L1-SHARP-001`.
- **Actual new coverage:** selected direct §17.4.11 radial-model audit (tag `27DF9596E862`), first selected §1.1 `dd^c` convention check (tag `DE921263`), and first **navigation-only** inventory §2.15 (tag `73E021597E92`). §17.3.16 and §17.4.4 only conditional context. **25 chapters / 747 numbered ToC sections / zero whole-section certifications**. Previous error/gap/dependency statuses unchanged; Demailly approximation/regularization and dedicated Bergman/L²/Ohsawa–Takegoshi/multiscale/positivity-loss programme **deferred-by-user**, not touched. No main/source/body/registry/site/build/CI/formalization changes.

---
# Latest mathematical audit checkpoint — 2026-10-30 — exact arbitrary-polyradius Bedford–Taylor relative capacity and its distinguished-torus mass

**Reviewed main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. [Full source-anchored proof](reports/2026-10-30-polydisc-relative-capacity-and-clifford-torus.md). Audit branch `review/mathematical-audit`; source and production edition unchanged.

- **POME-BT-POLYDISC-SHILOV-CAP-001 — low / verified conditional deduction:** for \(\Omega=\prod\Delta(R_i)\), \(K=\prod\overline\Delta(r_i)\), \(L_i=\log(R_i/r_i)\), the exact extremal is \(\max(-1,\max_i\log(|z_i|/R_i)/L_i)\); its Monge–Ampère measure is **\(1/(2^n\prod_iL_i)\)** times normalized Haar probability on the **distinguished n-torus** \(\{|z_i|=r_i\ \forall i\}\). Both inner and outer BT capacities equal this mass. Proven by finite coordinatewise powers plus monotone compact exhaustion for irrational ratios and the exact complex/real toric Jacobian. Printed §§7.16.1/.4/.5 and 21.5.1 are correct in the model; original general results and BT continuity not independently certified.
- **Actual new proof-level scope:** selected §7.16.1(2–3), norm-ball formula, §7.16.4 proper-map equivariance, §7.16.5 capacity/mass statement, §21.5.1–2 real measure normalization. **25 chapters / 747 numbered current ToC sections / zero complete-section certifications**. Older ledger statuses unchanged. The Demailly approximation/regularization and dedicated Bergman/L²/OT/multiscale/positivity-loss programme remains **deferred-by-user**, not reopened. No main/source/website/CI/build/formalization changes.

---

# Latest mathematical audit checkpoint — 2026-10-30: primitive Gauduchon root deficit and endpoint determinant concentration

**Reviewed main:** b6933b772f41b45918f7e25ed1afbbb1fd892272. [Full new direct proof and source anchors](reports/2026-10-30-primitive-gauduchon-radial-deficit-and-endpoint-collapse.md).

- **POME-PRIMGAUD-ROOT-DEFICIT-001** — low / verified conditional deduction: exact normalized root-volume deficit in §24.4.13, \(\mathcal E=(x-1)^2(x+2)/2\), \(x=\sqrt{3a/(a+\bar g)}\). Printed Proposition 24.4.13 is correct; equality fixes \(\bar g=2a\), not the oscillation of \(g\).
- **POME-PRIMGAUD-ENDPOINT-ESCAPE-001** — low / verified conditional deduction: on a non-Kähler primitive elliptic bundle, exact root-volume equalizers with fixed degree have determinant densities \(k_\varepsilon=Cg_\varepsilon^{2/3}\); they converge strongly to zero in every \(L^q\), \(1\le q<3/2\), retain fixed nonzero critical \(L^{3/2}\) norm and diverge in every \(q>3/2\), while root-volume measures concentrate. Do not confuse the determinant measure (12.7.1) with root volume; this does **not** solve the lower-mass Problem 24.4.14.
- **Actual new coverage:** first direct selected proof-level §§24.4.8/.13 and open-problem boundary §24.4.14; selected §12.7.1 and §§12.9.1–2 normalization crosschecks; §24.11.1 statement-level problem inventory; §§10.32 and 10.45 structurally navigation-only. **25 chapters / 747 numbered ToC sections / zero complete-section certifications**. Existing confirmed errors, proof gaps and external dependencies unchanged. Demailly regularization and its dedicated Bergman/L²/OT/multiscale/positivity-loss programme remain strictly **deferred-by-user**; no source, main, registry, site, CI, build or formalization changes.

---

# Latest mathematical audit checkpoint — 2026-10-30: Hausdorff loss under nuclear-module base change; new §§24.8–24.9 problem inventory

**Reviewed main:** b6933b772f41b45918f7e25ed1afbbb1fd892272. [Full anchored elementary proof and problem quantifier audit](reports/2026-10-30-relative-nuclear-basechange-hausdorff-loss.md).

- **POME-RELNUC-BASECHANGE-HS-LOSS-001 — low / verified conditional deduction, printed Lemma 9.46.3 correct.** A one-term B-nuclear endomorphism on the disk algebra B has **Hausdorff one-dimensional** original cokernel B/zB. Continuous extension of scalars to smooth functions C on a closed interval through z→h=exp(-1/x²) gives the cyclic **non-Hausdorff** cokernel C/hC. Its ideal closure is exactly the flat functions at zero; the quotient is infinite-dimensional over the complex numbers. Distinct from the earlier example that already had a non-Hausdorff original cokernel. Theorem 9.46.5 and downstream §9.47 must not infer Hausdorffness from finite generation; no printed result disproved.
- **First selected statement-level §24.8.4 / §24.9.1 checks:** isolated the full topology/analytic-closure requirement and the “every divisor on every modification” realization quantifier. Open questions remain open, and cited regularization/approximation material was not reviewed.
- **Actual scope:** §9.46.3 exact model and relevant §9.46.5 statement; previously unreviewed §§24.8.3–4 and 24.9.1 *problem/hypothesis* inventory only. **25 chapters / 747 numbered ToC entries / zero entirely certified sections**. Historical statuses unchanged. Excluded Demailly approximation/regularization and dedicated Bergman/L²/OT/multiscale/positivity-loss programme stay **deferred-by-user**. Audit Markdown only; no main, source, site, tests/build, CI, or formalization changes.

---

# Latest mathematical audit checkpoint — 2026-10-30: irrational null-leaf closures and a Hartogs coefficient criterion beyond maximal continuation

**Reviewed production main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. [Complete new independent calculations and exact integrated anchors](reports/2026-10-30-irrational-null-leaf-closures-and-hartogs-coefficients.md).

- **POME-NULL-LEAF-KRONECKER-CLOSURE-001 — low / verified conditional deduction.** In §7.15's constant-rank null foliation model on `(C*)²`, the irrational-`a` immersed leaf `(z0 exp(t), w0 exp(a t))` is dense in **exactly** the real Levi-flat hypersurface `log|w|-a log|z|=constant`; it is injective but not embedded. For rational `a=p/q`, the leaf is the closed embedded algebraic curve `w^q z^(-p)=constant`. This strengthens the printed intrinsic-topology illustration without challenging the theorem.
- **POME-HARTOGS-EQUALITY-WITHOUT-EXISTENCE-001 — low / verified conditional deduction.** §9.15.1's coefficient identity can hold even when the chosen holomorphic function does **not** have the Hartogs domain as its domain of existence: on `H={|w|<1,|zw|<1}`, `f=1/(1-w)+1/(1-zw)` has `c_j=1+z^j`, whose **unregularized** logarithmic coefficient limsup is exactly `max(0,log|z|)`, while `f` extends across `(0,i)`. The constant function shows the domain-of-existence hypothesis cannot be deleted from the universal statement. Separate from the previous usc-star necessity example.
- **Scope:** direct selected mathematical checks in §§7.15 and 9.15; §18.2 was checked only as an **expository, unnumbered** page, not as proof coverage. **25 chapters / 747 numbered ToC sections / zero entire-section certifications**. Prior statuses unchanged. Demailly approximation/regularization and dedicated Bergman/L²/OT/multiscale/positivity-loss programme remain **deferred-by-user**, untouched. Audit Markdown only; no production, source, site, tests/build, CI or formalization change.

---

# Latest mathematical audit checkpoint — 2026-10-30: ordered degenerate Monge–Ampère branches and navigation-only sections

**Pinned production main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. [Complete proof, original/permanent tags and precise anchors](reports/2026-10-30-degenerate-ma-ode-separation-and-navigation-inventory.md).

- **POME-DEGENMA-ORDER-QUANT-SEPARATION-001 — low / verified conditional deduction; no false theorem.** On the fixed smooth degenerate equation of Theorem 14.27.1, solutions `h_eta` of the first-order ODE are *strictly ordered throughout the full middle band*: for `eta1<eta2`, `h_eta1-h_eta2=(eta2-eta1) exp(integral_0^r a)`, where `a` is the explicit divided difference of the nonlinear ODE coefficient. After sup normalization the **exact oscillation** of the potential difference is the integral of this positive slope separation over `(-1,1)`; its extrema occur on the two distinct outer components. Uniform compact-interior ODE bounds yield `||u_eta1-u_eta2||_infinity >= b exp(-L_b b)|eta2-eta1|` for small parameters. This differs from the prior C-infinity nonisolation finding and does not reprove the full global background construction.
- **Newly classified previously unreviewed heading-only ToC entries:** §§2.11, 5.52, 9.37, 9.48, 10.53 and 10.76 each contain only navigation/citation UI, not a mathematical theorem or proof. Their inventory status is **navigation-only**, not theorem/section certification; following mathematical sections remain to be reviewed separately.
- **Actual coverage:** new selected §14.27.3/.7 ODE comparison and Theorem 14.27.1 normalization; structural inventory checks of six headings. **25 chapters / 747 numbered ToC entries / zero fully mathematically certified sections.** All historical errors and open gaps retain their statuses. Demailly approximation/regularization and its dedicated Bergman/L²/OT/multiscale-atlas/positivity-loss programme remain **deferred-by-user**, not reopened. No production, sources, publication, CI, build, or formal verification changes.

---

# Latest mathematical audit checkpoint — 2026-10-30: exact radial Newtonian sphere sweeping and escape

**Reviewed production main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. [Complete source-anchored proof](reports/2026-10-30-newton-shell-projection-and-exterior-escape.md).

- **POME-GREEN-SPHERE-SWEEP-ESCAPE-001 — low / verified conditional deduction.** On `R^d` for `d>=3`, an explicit Newtonian shell model computes the unique Hilbert-energy projection onto measures supported on a sphere `S_s`: for any finite positive rotation-invariant finite-energy measure `mu`, its spherical sweep is `c_s sigma_s`, with `c_s=mu(closed B_s)+s^(d-2) integral_{|y|>s}|y|^(2-d)dmu(y)`, and the energy residual has norm squared `||mu||²-c_s²s^(2-d)`. Sweeping an outside unit shell inward loses precisely `1-(s/r)^(d-2)` total mass, matching the **ordinary exterior** harmonic escape term of Theorem 4.4.11; no Helms-harmonicity at infinity is asserted for the zero-at-infinity hitting function. Original Theorems 4.4.11 and 4.5.6 are correct in the examined model; this is **not** general theorem certification. Prior shell-energy incompleteness, weak-versus-strong convergence, and nonexpansive projection findings were not repeated.
- **Actual coverage:** new selected direct checks of §4.4.11 and §4.5.1/.6 with only contextual comparisons to §4.5.2/.4/.5; no complete section verification. **25 chapters / 747 numbered ToC sections / zero entirely certified sections**. All historical confirmed errors, proof gaps, candidates, external dependencies and the excluded Demailly approximation/regularization/Bergman/L²/OT/multiscale-atlas/positivity-loss programme remain at their prior statuses, the excluded portion specifically **deferred-by-user**. No main/source/body/registry/site/build/CI/formal verification modifications.

---

# Latest mathematical audit checkpoint — 2026-10-30: sharp Kähler adjoint total-variation stability

**Reviewed production main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. [Complete new proof and pinned source anchors](reports/2026-10-30-kahler-adjoint-tanh-stability-and-boundary-distance.md).

- **POME-KAHLER-ADJOINT-TANH-TV-001 — low / verified conditional deduction.** For a fixed closed Kähler background, continuous log density F and smooth probability dV, the normalization functional has the explicit analytic formula B_0(F)=log M-log ∫exp(F)dV; its unique supporting probability is nu_F=exp(F)dV/∫exp(F)dV, with Hessian minus the covariance. New exact universal sharp stability: dual TV norm of nu_F-nu_G is at most 2 tanh(osc(G-F)/4), and at most ||F-G||_infinity. Optimality holds by two-level densities approximated by smooth functions. **No general Hermitian uniqueness claim:** Conjecture 24.7.1 remains open.
- **First selected §24.6–7 review:** §24.7.1 benchmark and sign of supporting Eq. 11.34.1; §24.6.1 and the degree-one root-volume radial isometry in Proposition 12.6.1 checked at selected steps only. The general completion problem 24.6.1 remains open; no entire theorem dependency chain verified.
- **Actual scope:** 25 current chapters / 747 distinct numbered ToC sections / zero entire-section certifications. All historical unresolved/deferred items unchanged. Demailly approximation/regularization and dedicated Bergman, L², Ohsawa–Takegoshi, multiscale atlas and positivity-loss proof programme remain **deferred-by-user**, neither reopened nor certified. Audit Markdown only: no production, source, tag, registry, site, CI, build or formal-verification changes.

---
# Latest mathematical audit checkpoint — 2026-10-30: sharp tautological fiber nonvanishing and exceptional numerical dimension

**Pinned production main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. [English proof, permanent tags and physical anchors](reports/2026-10-30-tautological-fiber-sharpness-and-exceptional-numerical-dimension.md).

- **POME-TAUT-FIBER-N-OPTIMAL-001 — low / verified conditional deduction; Lemma 10.108.1 correct.** For all \(r\ge2\), a hyperplane-pole singular metric on \(\mathcal O_{\mathbf P^{r-1}}(1)\) at \(m\varepsilon C=1\) has \(\mathcal I(h^m)=\mathcal O(-(m+1)H)\). Thus the lemma's target is \(\mathcal O(N-r-1)\), which has no global sections for \(N\le r\), and exactly one at \(N=r+1\). **The uniform \(N\ge r+1\) threshold is sharp.** The prior tautological open-model metric-extension candidate remains unresolved.
- **POME-NUMDIM-EXCEPTIONAL-POSPRODUCT-001 — low / verified conditional deduction, analytic-current characterization conditional.** On \(X=\operatorname{Bl}_p\mathbf P^2\), \(\omega\in H-dE\), \(0<d<1\), every positive \(S=T+\varepsilon\omega\in E+\varepsilon[\omega]\) has generic exceptional coefficient \(a\ge1-\varepsilon d\), so the residual mass outside the polar set is \(\le\varepsilon\). Consequently \(\langle[E]\rangle\cdot\omega=0\), \(\nu(E)=0\) under the printed convention, despite the **ordinary** pairing \(E\cdot\omega=d>0\). No simultaneous regularization or general positive-product equivalence was reaudited.
- **First direct selected §24.5 coverage:** checked exact fixed-\(\varepsilon\) zero-class mass scaling, plus the closed and Gauduchon-surface Stokes contrast, at physical line 10; the existence of unbounded mass is only the cited conditional input and no open problem was solved.
- **Actual scope:** selected §§10.108.1, 10.109 introduction/degree-one and §24.5 first paragraph. **25 chapters, 747 current ToC sections, zero whole-section certifications**. All historical statuses unchanged; expressly excluded Demailly approximation/regularization and dedicated Bergman/L²/OT/multiscale/positivity-loss work remain **deferred-by-user**. No main, source, site, CI, build or formalization changes.

---

# Latest mathematical audit checkpoint — 2026-10-29: non-Archimedean divisorial-pointwise versus full-pointwise limits and a stale equation label

**Reviewed production main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. [Complete new example, proof, stable source tags and physical anchors](reports/2026-10-29-nonarchimedean-divisorial-limit-and-fs-label.md).

- **POME-NA-DIV-POINTWISE-NONUSC-001 — low / verified conditional deduction.** New selected §22.1.66–76 mathematical review: on `P^1`, rational Fubini–Study metrics `Phi_m=(1-1/m)Phi+(1/m)log|Z_0|` **increase** to `Phi=max(log|Z_0|,log|Z_1|)` at all divisorial valuations but remain `-infinity` at the closed-support semivaluation `[0:1]` where `Phi=0`. The raw full-Berkovich pointwise limit fails upper semicontinuity. This is compatible with, and explains the precise **divisorial-pointwise** convergence topology and Conjecture 22.1.76; no printed theorem is false and no envelope conjecture was proved.
- **POME-NA-FS-STALE-EQUATION-LABEL-001 — medium / confirmed reading-edition integration error, unresolved.** At §22.1.70 lines 1178–1185 the correct Fubini–Study formula is given the **unlinked literal source number `13.37`**, not a generated §22.1 equation label/permalink. Propose a separate renderer correction after checking for a true source equation tag; do not edit the published body. This is **not a mathematical formula error**.
- **False-positive excluded:** §22.1.66's `U^An` condition “support meets U” matches the published Boucksom–Jonsson definition; do not replace it with “center in U”. **Actual scope:** selected §22.1.66–76 definitions, model computation, cross-reference; all other BJ theorems conditional, no whole section certified. **25 chapters / 747 current ToC sections / zero whole-section certifications**. Historical errors, especially §22.1.88, and user-deferred Demailly/Bergman/L²/OT/multiscale/positivity-loss remain unchanged. No production/main/site/source/build/CI/formalization changes.

---

# Latest mathematical audit checkpoint — 2026-10-29: sharp zero-mass normalized tails and quantitative envelope-volume estimate

**Pinned production main:** b6933b772f41b45918f7e25ed1afbbb1fd892272. [Complete P¹ current calculation, optimized finite-A bound, stable source labels and physical line anchors](reports/2026-10-29-zero-mass-envelope-tail-sharpness.md).

- **POME-ENV-ZEROMASS-TAIL-OPT-001 — low / verified conditional deduction; printed Proposition 17.6.1 correct.** Incremental selected **§17.6** proof review: on \(\mathbb P^1\) with \(u=\log(|z|^2/(1+|z|^2))\), \(\omega+dd^cu=[0]\) has **zero non-pluripolar mass**, but \(w_\varepsilon=(1-\varepsilon)u\) has \(\mu_{w_\varepsilon}=\varepsilon\omega\), \(m_\varepsilon=\varepsilon\), and its normalized tail is exactly \(e^{-A/(1-\varepsilon)}\uparrow r(A)=e^{-A}\) as \(\varepsilon\downarrow0\). Hence Eq. 17.6.2 is attained asymptotically despite mass collapse. Optimizing the printed Eq. 17.6.3 gives, for fixed \(\delta>0\) and sufficiently small \(r(A)\), a uniform finite-obstacle volume bound of order \(r(A)^{1/(n+1)}\), without a positive mass lower bound. This exponent is optimal **for balancing the proof's two terms**, not an asserted intrinsic geometric sharpness result. §16.25.4/§17.5.6 conditional inputs checked at statement level, not certified. Distinct from pre-existing **POME-ENV-MASS-ORDER-001** (total-mass vanishing order).
- **Earlier same-day incremental §21.5 finding:** **POME-TORIC-MIXED-ESCAPE-001** remains documented immediately below; §11.48 old 2026-10-25 glyph/alias errors were only rechecked, **not new findings or repairs**.
- **Actual coverage:** new selected Step 2–6 quantitative checks in previously partly reviewed §17.6 and mixed-measure calculation in previously partly reviewed §21.5. **25 chapters / 747 numbered current ToC sections / zero complete-section certifications**. All pre-existing errors and deferred Demailly approximation/regularization, Bergman/L²/OT/multiscale/positivity-loss remain unchanged. No production main, source/registry/tag/site edits, builds, CI or formal verification.

---

# Latest mathematical audit checkpoint — 2026-10-29: mixed real Monge–Ampère mass escaping with one moving argument

**Reviewed production main:** b6933b772f41b45918f7e25ed1afbbb1fd892272. [Full exact proof and source-tag/line anchors](reports/2026-10-29-hermitian-bochner-aliases-and-mixed-toric-escape.md).

- **POME-TORIC-MIXED-ESCAPE-001 — low / verified conditional deduction.** In §21.5, for any \(n\ge2\) and \(F_i(x)=a_i(x_i-c_i)_+\), \(a_i>0\), the Alexandrov definition and printed polarization give exactly \(\operatorname{MA}_{\mathbb R}(F_1,\ldots,F_n)=(\prod_i a_i)\delta_c\). Fixing the first \(n-1\) functions and translating **only** \(F_{n,j}=a_n(x_n-j)_+\to0\) locally uniformly gives mixed measures of constant positive mass supported at \((0,\ldots,0,j)\). They converge **vaguely, not narrowly**, to the zero mixed measure. This is a new genuinely mixed-dimensional sharpening of the *already printed* one-variable Example 21.5.3, not an error in Proposition 21.5.4; it independently verifies the \(n!\)/\(1/n!\) normalization.
- **Historical recheck, not new findings:** §11.48's five invalid equation aliases and two U+201D/double-prime corruptions were **already recorded** under **POME-HERM-BOCHNER-EQUATION-ALIASES-001** and **POME-HERM-BOCHNER-DOUBLEPRIME-001** in the [2026-10-25 report](reports/2026-10-25-hermitian-affine-background-scaling-and-bochner-equation-aliases.md); statuses remain unchanged. The present report's adjoint-algebra and conformal-torsion check adds supporting calculations only, **not** a rediscovered error or resolved repair.
- **Actual scope:** incremental §21.5.1–4 mixed calculation; historical §11.48 recheck and selected contextual §11.5 Stokes/AGM check **not counted as new section coverage**. **25 chapters / 747 ToC numbered sections / zero complete-section certificates.** Every historical error/proof gap and all dedicated Demailly approximation/regularization, Bergman, L²/Ohsawa–Takegoshi, multiscale and positivity-loss work remain unchanged and **deferred-by-user** where applicable. No production/source/registry/tag/site changes, builds, CI, publication or formal verification.

---

# Latest mathematical audit checkpoint — 2026-10-29: full-lattice Okounkov conductors, symmetric-difference isometry and infinite convex envelopes

**Reviewed production main:** b6933b772f41b45918f7e25ed1afbbb1fd892272. [Pinned source tags, physical main lines, complete selected proofs and counterexamples](reports/2026-10-29-full-lattice-conductor-isometry-and-infinite-convex-envelopes.md).

- **POME-OKO-FULL-LATTICE-CONDUCTOR-001 — low / verified repair of full-lattice subcase only.** A finite-cone residue/conductor proof gives uniform lattice saturation on compact interior subsets of $\Delta(S)$ for $\operatorname{gp}(S)=\mathbb Z^{n+1}$, and therefore the precise full-degree $|S_k|/k^n\to\operatorname{vol}\Delta(S)$. It removes KK12/WN14 as *proof inputs for this restricted case*, not for the arbitrary-semigroup theorem; their historical attribution is retained.
- **POME-OKO-SYMDIFF-ISOMETRY-001 — low / verified conditional deduction.** Exact $d_{\rm sg}(S,T)=\operatorname{Leb}(\Delta(S)\triangle\Delta(T))$ for full-lattice semigroups, including zero-volume intersections, extends to positive-volume almost semigroups. Their pseudometric quotient is the positive-volume compact-convex-body space with symmetric-difference measure metric; no completeness at zero-volume boundary is claimed.
- **POME-CVX-INFINITE-FAMILY-BOUNDARY-001 — low / verified conditional deduction.** Two explicit infinite families with all effective domains in a common compact set defeat, respectively, closedness/biconjugacy and infimum attainment of a hypothetical infinite-family version of the *correct finite* Lemma 21.6.1. Do not silently drop finiteness.
- **Actual coverage:** incremental selected §§19.2, 19.7 and 21.6; *first* selected §24.3.2 positive-Gauduchon-volume proof check, no new error and its external/internal prerequisites not certified. **25 chapters / 747 numbered ToC sections / zero complete-section certificates.** All historical findings and user-deferred Demailly/regularization/Bergman/L²/OT/multiscale/positivity-loss statuses unchanged. No production/main/source/CI/site edits.

---

# Latest mathematical audit checkpoint — 2026-10-29: generalized-mass level atoms and a logistic ray's exact energy

**Reviewed production main:** b6933b772f41b45918f7e25ed1afbbb1fd892272. [Full source-tagged, line-anchored report with independently checked formulas](reports/2026-10-29-generalized-level-atoms-and-logistic-ray-energy.md).

- **POME-GENLELONG-LEVEL-JUMP-001 — low / verified conditional deduction.** First selected nonexcluded direct audit of §§6.34.2/.5/.8: a **fixed-weight** $p=0$ positive-measure example attains the upper closed-level bound in (6.34.9), so the printed right limit cannot generally be replaced by the open-level value. Independently, a support-relative compact complex line current with the psh weight $\max(0,\log|w|^2)$ has a unit circle of generalized mass at level zero; shifting the weight down by $1/j$ gives locally uniform convergence of $e^{\varphi_j}$ but fails open-level mass continuity in positive bidimension. Both printed statements are correct. No Demailly approximation/regularization or dedicated excluded proof has been considered.
- **POME-RWN-LOGISTIC-RAY-ENERGY-001 — low / verified conditional deduction.** Incremental smooth computation on the **already partly reviewed** explicit $\mathbb P^1$ Legendre ray §17.17.11/.12: its velocity sends the mass-one Monge–Ampère form to **uniform measure on [0,1]** for every $t$, hence every positive moment is $1/(q+1)$, and its Aubin–Mabuchi energy is **exactly $t/2$**. This checks the normalization directly without claiming a new proof of the general Perron correspondence or geodesic energy theorem.
- **Actual coverage:** new selected §§6.34.2/.5/.8; incremental §17.17.10–12; §17.8.3 is normalization context only and §6.42 is convention/navigation only. **25 chapters / 747 numbered ToC sections / zero complete-section certificates.** All previous errors, gaps, external inputs, and user-deferred work retain their prior statuses. No main, sources, tags, registries, generated site, build, CI, or formalization changes.

---

# Latest mathematical audit checkpoint — 2026-10-29: conformal Kähler Hessian comparison and irreducible nodal cubic

**Reviewed production main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. [Two source-tagged complete model arguments](reports/2026-10-29-conformal-hessian-mass-and-irreducible-nodal-cubic.md).

- **POME-HESS-CONFORMAL-KAHLER-MASS-001 — low / verified conditional deduction.** New direct selected inspection of Theorem 8.13.4 and Example 8.13.5 (with actual standing assumption 2 <= m < n). For any compact Kähler (X,beta), n>=3, and arbitrary smooth conformal Hermitian omega=e^phi beta, unmodified m-Hessian comparison for every allowed m holds **iff phi is constant**. If nonconstant, the single f=e^((n-1)phi) has strictly negative mass derivative in every intermediate degree; u=t f and a constant larger than u violate the mass comparison on the whole X. All printed results correct; no upstream bounded-current or modified comparison proof recertified.
- **POME-NORM-IRREDUCIBLE-NODAL-CUBIC-001 — low / verified conditional deduction.** New selected §9.4.6/.9/.10 inspection: the projective *irreducible* nodal cubic Y²Z=X²(X+Z) has P¹ normalization by explicit cubic homogeneous forms, two points over its node, local delta invariant 1 and an explicit conductor ideal. Global irreducibility is not local unibranchness. Distinct from the previous coprime monomial cusp model; printed normalization/unibranch statements correct.
- **Actual coverage:** selected §§8.1, 8.13.4–5, 9.4.6/.9/.10; §§8.9–12, 8.13.3/.8–.12 and 9.3/9.5 only necessary context, not fully certified. **25 chapters / 747 numbered ToC sections / zero complete-section certificates.** All old confirmed errors, gaps and dependencies unchanged. Demailly approximation/regularization and its dedicated Bergman/L²/OT/multiscale/positivity-loss programme remain **deferred-by-user**; no main/source/site/CI/formalization edits.

---

# Latest mathematical audit checkpoint — 2026-10-29: sharp finite-p Monge–Ampère stability exponent

**Reviewed main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. [Complete project-tagged proof](reports/2026-10-29-prescribed-ma-stability-sharp-exponent.md).

- **POME-PRESMA-STABILITY-EXPONENT-SHARP-001 — low / verified conditional deduction.** First new exact sharpness analysis of the printed §15.4.1 exponent, for every complex dimension n and p>1. A **fixed** bounded `ω_FS`-psh cusp solution on P^n has `MA(u)=f dV` with `f∈L^p`, while `v_δ=max(u,min(u)+δ)` has pointwise height δ and `L¹` excess asymptotic to a positive constant times `δ^(1+2n/β)` for any `β∈(2−2/p,2)`. Hence any universal exponent above `(p−1)/(np+p−1)` fails, proving that the printed strict range is optimal as a supremum; endpoint **not** settled. For p=∞ a smooth model yields the ceiling 1/(n+1). Theorem 15.4.1 remains **correct**, no open problem is closed.
- **Actual coverage:** selected integrated theorem/proof §§15.4.1 (lines 10–28 and 33–87); §15.4.3 statement and §§15.5–15.6 dependency context only, **not** their dedicated regularization proofs. Still **25 chapters / 747 ToC sections / zero completely certified sections**. Historical issues and Demailly/regularization/Bergman/L²/OT/multiscale/positivity-loss items remain **deferred-by-user**. No main, source, registry, site, CI or formal verification changes.

---
# Latest mathematical audit checkpoint — 2026-10-29: countably dense divisorial poles, strict moving-point Lelong limit, and ellipse capacity

**Reviewed production main:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`. [Exact source tags, main blob/physical lines and independent selected proofs](reports/2026-10-29-dense-divisors-moving-lelong-and-ellipse-capacity.md).

- **POME-DENSE-DIVISOR-LOCI-DOMINATION-001 — low / verified conditional deduction.** First direct nonexcluded §5.38.1/.5/.6 selected proof review: on \`P¹×P¹\`, a finite-mass sum of prime divisor currents with **dense, non-locally-finite support** satisfies the printed countable-divisor domination criterion. The L¹-defined qpsh model \`v=Σ 2^{-j}π₁*q_{p_j}\` tests the finite-partial-sum positivity limit exactly. Printed Lemma 5.38.5 correct; internal Siu/divisorial-removal premise conditional.
- **POME-MOVING-POINT-LELONG-STRICT-LIMSUP-001 — low / verified conditional deduction.** §5.38.7's fixed-point Lelong upper semicontinuity is **strict** for moving analytic logarithmic poles \`q_{p_j}→q_p\` in L¹ with common Fubini–Study lower bound, because at fixed \`p\`, \`ν(q_{p_j},p)=0\` while \`ν(q_p,p)=1\`. No smoothing or dedicated excluded approximation.
- **POME-PLANAR-ELLIPSE-GREEN-CAPACITY-001 — low / verified conditional deduction.** New §3.8.2 conformal-model calculation gives \`cap(K_{a,b})=(a+b)/2\` for a filled ellipse and identifies equilibrium law as the pushforward of uniform angle under \`F(w)=((a+b)/2)(w+((a-b)/(a+b))/w)\`, with arcsine degeneration. Distinct from earlier real-cube Joukowski and planar polar-boundary findings; printed proposition correct.
- **Actual coverage:** first direct selected §5.38.1/.5–.8; incremental §3.8.2. §5.38.9 and dedicated Bergman/L²/OT/multiscale/positivity-loss proof programme **deferred-by-user**, not examined; §§5.24/.33/.37 and §10.4 conditional context only. **25 chapters / 747 numbered ToC sections / zero entire-section certifications.** All prior issues retain historical status. No main/source/site/registry/build/CI/formalization changes.

---

# Latest mathematical audit checkpoint — 2026-10-29: sharp moving-radius penalty and finite-energy curve traces

**Reviewed production main:** <code>b6933b772f41b45918f7e25ed1afbbb1fd892272</code>. [Pinned integrated anchors, hypotheses and complete new arguments](reports/2026-10-29-varying-radius-penalty-and-curve-finite-energy-traces.md).

- **POME-ENVELOPE-VARYING-RADIUS-SHARP-BARRIER-001 — low / verified conditional deduction.** New §16.18.1 direct proof gives the locally uniform **O(ε log(1/ε))** penalized-infimum error, with exact e^s constant-upper-endpoint model attaining ε log(1/ε)+O(ε). A moving endpoint b=B+C_b|z|² shows the printed **c C_b** curvature-loss coefficient is universally optimal; no printed error.
- **POME-CURVE-TRACE-FINITE-ENERGY-001 — low / verified conditional deduction.** The §15.31.4 **trace clause only** holds under the weaker assumptions μ polar-null and Q_μ∈H¹, even when Q_μ is unbounded. Explicit radial μ_p with density proportional to 1/(r²(log(1/r))^p) has a bounded H¹→L¹(μ_p) trace exactly for p>3/2, yet Q_p(0)=−∞ for p≤2. The nearby exponential-equation regularity still requires its own hypotheses; no theorem declared false.
- **Actual coverage:** newly inspected §16.18.1 and strengthened §15.31.4; §15.31.3 context only and previously checked §5.53 sign conventions not recounted. **25 chapters / 747 distinct ToC sections / zero entire-section certifications.** All prior statuses unchanged; Demailly regularization and dedicated Bergman/L²/OT/multiscale/positivity-loss remain **deferred-by-user**, untouched. No main/source/site/registry/build/CI/formalization changes.

---

# Latest mathematical audit checkpoint — 2026-10-29: Schwarz quadratic jets and Gauduchon equation-alias rendering

**Reviewed production main:** <code>b6933b772f41b45918f7e25ed1afbbb1fd892272</code>. [Pinned integrated source labels, physical-line anchors and complete selected proofs](reports/2026-10-29-schwarz-quadratic-jet-and-gauduchon-equation-alias.md).

- **POME-SCHWARZ-QUADRATIC-JET-MEAN-001 — low / verified repair of selected proof step only.** In §9.17.1, the quadratic real Taylor jet of a C² function <code>v=exp(h)</code> with a PSH pole admits no pure holomorphic quadratic terms. Bounded subharmonic removal and the *circle sub-mean property* alone establish this, eliminating the printed proof's nonthin-segment input. Proposition 9.17.1 itself is not false, and its remaining Green/leafwise dependencies are not certified.
- **POME-GAUD-SECONDVAR-EQ-ALIAS-NESTED-001 — medium / confirmed reading-edition integration error, not a false PDE claim.** §12.4.1 correctly prints both rows of (12.4.2)–(12.4.3), but its section tail duplicates row (12.4.3) inside an illegal nested <code>aligned</code>/<code>align</code> display; the permanent equation (12.4.3) standalone page contains the same malformed fragment. The source tags and intended second-variation mathematics are valid. Propose canonical row aliases and legal standalone rendering in a separate patch.
- **Actual coverage:** new selected §9.17.1 jet proof; incremental §12.4.1–4 equation/normalization audit; §§9.33, 10.42 **navigation-only**, with no substantive mathematical statements on their index pages. Original **25 chapters / 747 numbered ToC sections / zero entire-section certifications**; previous issues remain unchanged and dedicated Demailly approximation/regularization with Bergman/L²/OT/multiscale/positivity-loss completion stays **deferred-by-user**. Read-only three-page exact text checks performed; no builds, browser tests, CI, main/source/site/registry/formalization edits.

---

# Latest mathematical audit checkpoint — 2026-10-29: Radon sequential compactness and oscillatory mixed b-divisor intersections

**Reviewed production main:** <code>b6933b772f41b45918f7e25ed1afbbb1fd892272</code>. [Pinned integrated source labels, physical-line anchors and independent proofs](reports/2026-10-29-vague-sequential-compactness-and-oscillatory-mixed-bdivisor.md).

- **POME-RADON-LOCAL-MASS-SEQUENTIAL-COMPACT-001** — low / **verified conditional deduction**: Theorem 2.7.3's positive locally bounded Radon-measure class is not only compact under Willard subnets: its vague topology is metrizable and every sequence has a convergent subsequence. A countable compact-support dense test family and an elementary diagonal extraction establish this under the original hypotheses. The printed theorem is correct.
- **POME-BDIV-MIXED-OSCILLATION-POSITIVE-001** — low / **verified conditional deduction**: two big nef Cartier b-divisor sequences on \(\mathbb P^2\), individually of constant positive volumes \(1-a^2\) and \(1-b^2\), converge modelwise to the Cartier hyperplane b-divisor, but their mixed intersections alternate between \(1-ab\) and \(1\). This is separate from the existing printed **zero-volume** Example 20.1.9; Proposition 20.1.47's upper semicontinuity remains correct.
- **Actual coverage:** selected proof/definition checks §§2.7.3 and 20.1.7/.9/.10–12/.39/.40/.41/.43/.45/.47/.49; navigation-only first inspection §§16.1/.2/.10 and 9.25. **25 chapters / 747 numbered sections / zero complete-section certifications**. Every old issue status unchanged; excluded approximation/regularization and dedicated Bergman/L²/OT/multiscale/positivity-loss work remains **deferred-by-user**. No source/main/site/registry/build/CI/formalization changes.

---

# Latest mathematical audit checkpoint — 2026-10-29: lsc density viscosity criterion and divergent weak circle energies

**Reviewed production main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. [Exact source labels, main blob/physical-line anchors and complete arguments](reports/2026-10-29-lsc-bt-densities-and-circle-weak-energy.md).

- **POME-BT-LSC-VISCOSITY-EXTENSION-001** — low / **verified conditional deduction**: Proposition 7.8.3's measure/upper-test/distributional equivalence and convolution estimate extend from continuous densities to finite nonnegative **lsc and locally integrable** densities, using explicit increasing Lipschitz minorants. The bounded upper-semicontinuous point spike \(f=\mathbf1_{\{x_0\}}\), \(u=0\), shows no such **pointwise** equivalence for arbitrary Borel/USC representatives. The original printed proposition is correct.
- **POME-CLASS-CIRCLE-WEAK-ENERGY-DIVERGENCE-001** — low / **verified conditional deduction**: normalized arclength on a radius-\(R\) circle has logarithmic capacity exactly \(R\); atomless finite-energy arc measures \(\mu_N\rightharpoonup\mu\) can nevertheless satisfy \(I_D(\mu_N)\ge N/(2\pi)+O(1/N)\to\infty\). Theorem 4.1.7 correctly uses energy **lower** semicontinuity; weak convergence alone does not give energy convergence.
- **Actual coverage:** new selected §4.1.5/.7 proof/normalization inspection and extended §7.8.1–4, 7.8.6/8; §7.6.1–2 selected locality checks only. **25 chapters / 747 numbered sections / zero whole-section certifications**; all older statuses unchanged. All excluded Demailly regularization and dedicated Bergman/L²/OT/multiscale/positivity-loss work remains **deferred-by-user**, untouched. No main/source/registry/site/build/CI/formalization changes.

---

# Latest mathematical audit checkpoint — 2026-10-29: verified finite concave-tail repair and weak polar-measure closure obstruction

**Reviewed production main:** <code>b6933b772f41b45918f7e25ed1afbbb1fd892272</code>. [Exact source-label, permanent-tag, physical-line report](reports/2026-10-29-concave-envelope-tail-repair-and-weak-polar-closure.md).

- **POME-NA-CONCAVE-TAIL-REPAIR-001** — **medium / verified repair of the finite recursion only**: independently proves that changing the incorrect §22.1.88 left-tail assignment from unprimed to **primed last-node value** yields the least concave majorant for arbitrary finite real data and hence the canonical $\theta$-psh-valued finite construction. Full slope monotonicity and minimality proof; a new seeded 10,000-case scalar check is archived. **Existing POME-NA-CONCAVE-TAIL-001 remains a confirmed, unresolved error in production main**; Lemmas 22.1.89 and 22.1.107 are not transitively certified.
- **POME-CURVE-POLAR-WEAK-CLOSURE-001** — low / **verified conditional deduction**: explicit logarithmic-capacity-zero Bernoulli Cantor support gives finite-rational-atomic analytic models of fixed non-pluripolar mass $1/2$ whose polar measures converge **weakly** to a **nonideal nonatomic polar model**. The TV model distance remains **1** and the limiting model's distance to the ideal locus is **$1/2$**. This does not challenge the correct printed TV-closedness theorem.
- **Actual scope:** newly complete combinatorial correction argument for selected §22.1.88 (source still wrong), plus new weak-topology stress test of previously sampled §§13.28 and 13.30; §21.11.12 and §13.29.1 contextual only. **25 chapters / 747 unique numbered ToC sections / zero whole-section certifications.** Old statuses unchanged and all user-excluded Demailly approximation/regularization with dedicated Bergman/L²/OT/multiscale/positivity-loss tasks remain **deferred-by-user**. No main/source/site/build/CI/formalization change.

---

# Latest mathematical audit checkpoint — 2026-10-29: toric simplex moment measure and projective Hermitian mass in all dimensions

**Reviewed production main:** <code>b6933b772f41b45918f7e25ed1afbbb1fd892272</code>. [Exact integrated anchors, hypotheses and independent proofs](reports/2026-10-29-toric-moment-measure-and-projective-hermitian-mass.md).

- **POME-HOPF-TORIC-MOMENT-PUSHFORWARD-001** — low / **verified conditional deduction**: for smooth strictly positive toric \(k\sigma+\mathrm{dd}^{\mathrm c}v\) on \(\mathbb P^{n-1}\), the §21.14.8 logarithmic-gradient map pushes its top power forward to \((n-1)!\,\mathrm dp_1\cdots\mathrm dp_{n-1}\) on the open affine simplex of size \(k\), with total mass \(k^{n-1}\). For the original \(k=1\) Hopf background, the fiber factor is exactly \(2n\); more general \(k\alpha+\zeta\) is distinguished as a derived background. The printed statements remain correct; not a duplicate of the broader §21.12 toric dictionary.
- **POME-HERM-PROJECTIVE-MASS-ALLDIM-001** — low / **verified conditional deduction**: the nonclosed two-torus Hermitian example of §11.1.12 times any compact Kähler \((n-2)\)-fold has exact smooth-potential mass \(\binom n2(4-\pi^2t)BV\). Taking a projective factor yields comparison failure on a projective manifold of **every** complex dimension \(n\ge2\), because the chosen background is nonclosed. Direct elementary product calculation, not a new surface example or an allegation that Kähler comparison fails.
- **Actual coverage:** first selected proof scrutiny §21.14.6–8 and selected all-dimensional extension of §11.1.11–18; selected formula checks §11.1.4–5; §21.14.4 normalization checked; §21.12.8/13 and related sections are context only. **25 chapters / 747 numbered ToC sections / zero complete section certifications**. No prior finding closed; all user-excluded approximation/regularization and dedicated Bergman/L²/OT/multiscale/positivity-loss work stays **deferred-by-user**; its §5.32.1 dependency was noted but not reopened. No production edits, tests, CI, build, or publication.

---

# Latest mathematical audit checkpoint — 2026-10-29: Hölder sublevels and exact exceptional-flag Okounkov body

**Reviewed production main:** <code>b6933b772f41b45918f7e25ed1afbbb1fd892272</code>. [Full anchored report with hypotheses and complete calculations](reports/2026-10-29-holder-sublevel-and-exceptional-flag-body.md).

- **POME-DEGEN-HOLDER-SUBLEVEL-001** — low / **verified conditional deduction**: the square-root connectivity/uniqueness criterion of §14.21.13 extends to $C^{1,\alpha}$ nonnegative densities, $0<\alpha<1$, with sharp topological threshold $\operatorname{Vol}\{f\le t\}=o(t^{1/(1+\alpha)})$ (liminf suffices). In the hypotheses of §14.21.3, even $C^{1,1}$ potentials suffice. A flat torus density achieves exactly $2/\pi$ times the critical power while its positive set is disconnected. This is **not** a Monge–Ampère nonuniqueness example; the maximum-principle theorem remains an unrecertified internal input.
- **POME-BLOWUP-EXCEPTIONAL-FLAG-OKO-001** — low / **verified conditional deduction**: for $\operatorname{Bl}_p\mathbb P^2$, $L=aH+bE$, $a,b\ge1$ integers, flag $E\supset\{q\}$, all degree-$m$ valuations are precisely $(mb+k,j)$ with $0\le j\le k\le ma$. Its saturated degree-one-generated semigroup yields a translated triangle of area $a^2/2$, independently of $b$; this adds **valuation information**, not a repeat of the previously registered exceptional-volume calculation.
- **Actual coverage:** incremental selected, nonexcluded proof calculations in §§14.21.3/.13 and 19.9.1/.2/.5–7. §§14.20, 19.7 are context only. **25 chapters / 747 numbered ToC sections / zero complete-section certifications**. Previous ledger statuses unchanged; excluded Demailly approximation/regularization and dedicated Bergman/L²/OT/multiscale/positivity-loss tasks remain **deferred-by-user**. No production or publication changes, CI, build, or formal verification.

---

# Latest mathematical audit checkpoint — 2026-10-29: projective-vertex vanishing, explicit jets, and geodesic time speed

**Reviewed production main:** <code>b6933b772f41b45918f7e25ed1afbbb1fd892272</code>. [Full mathematical report, stable source labels, physical lines, and scope](reports/2026-10-29-projective-vertices-jets-and-geodesic-time-speed.md).

- **POME-PROJECTIVE-VERTICES-WALDSCHMIDT-EXACT-001** — low / **verified conditional deduction**: for the $n+1$ coordinate vertices in $\mathbb P^n$ ($n\ge2$), independently proved $\omega_t=\lceil (n+1)t/n\rceil$ and $\Omega=(n+1)/n$. The refined §9.56.4/.6 exceptional-locus inequality is **exactly attained** with $(X_0\cdots X_n)^k$ and zero fractional divisor. General analytic extension inputs NOT audited.
- **POME-PROJECTIVE-JET-CRT-SHARP-001** — low / **verified conditional deduction**: first selected nonexcluded §10.39.1 projective model, explicit polynomial construction gives simultaneous $m$-jet interpolation for $N$ points with $k\ge N(m+1)-1$ on $\mathbb P^n$; threshold is **sharp for $\mathbb P^1$** by dimension. General printed $L^2$ proof remains deferred.
- **POME-GEODESIC-FULL-TIME-LIPSCHITZ-001** — low / **verified conditional deduction**: §17.7.8 interval-restriction plus §17.7.9 endpoint bound give sharp $|G_t-G_s|\le C|t-s|$ on the common finite locus for endpoint distance $\le C$ q.e. Upstream existence and energy results not recertified.
- **Actual coverage:** first selected independent nonexcluded §10.39.1 model; incremental selected §§9.56.1/.4/.6 and 17.7.8–9; first **navigation-only** subject headers §§9.54 and 10.38. Original **25 chapters / 747 numbered ToC sections / zero whole-section certifications**. No prior finding resolved; all dedicated Demailly approximation/regularization and Bergman/L²/OT/multiscale/positivity-loss work remains **deferred-by-user**. No main/source/site/registry/tag/build/CI/formalization changes.

---

# Latest mathematical audit checkpoint — 2026-10-29: irrational weighted-section semigroup and signed Bott–Chern mass

**Reviewed main:** <code>b6933b772f41b45918f7e25ed1afbbb1fd892272</code>. [Complete source-tag/physical-line report](reports/2026-10-29-irrational-weighted-sections-and-bc-signed-mass.md).

- **POME-CURVE-BOUNDED-SECTION-FG-RATIONAL-001** — low / **verified conditional deduction**: for the explicit positive-weighted \( \mathbb P^1 \) model of §19.8.11, the bounded weighted section algebra is finitely generated **exactly when** the logarithmic pole coefficient is rational, although its Hilbert function grows linearly for every coefficient. Also exact integral/bounded dimension gap \(1_{\{mc\notin\mathbb Z\}}\). Original theorem correct, not a new general finite-generation claim.
- **POME-BC-FIXED-CLASS-SIGNED-MASS-001** — low / **verified conditional deduction**: on \( \mathbb P^1 \), the smooth closed signed representatives \(T_t=\gamma+t\,\mathrm{dd}^{\mathrm c}\phi\) have identical Bott–Chern class and trace but unbounded total-variation and normalized-potential norms. The common negative lower bound in §10.11.1 and positivity in §20.4.20 are essential. Printed statements correct.
- **Actual coverage:** new calculations in previously partly reviewed §§19.8.8–11, 10.11.1–2, and model-only §20.4.20. First **navigation-only** identification of formerly inventory-only §§10.10 and 5.59 (subject headers, no theorem certification). Original **25 chapters / 747 numbered ToC sections / zero complete section certifications** unchanged. No prior finding closed.
- Dedicated Demailly approximation/regularization and Bergman/L²/OT/multiscale/positivity-loss programmes remain **deferred-by-user**. No main/source/registry/site/tag/build/CI/formalization changes.

---

# Latest mathematical audit checkpoint — 2026-10-29: exact Picard–Albanese polarization index and generic nonalgebraic two-tori

**Reviewed main:** <code>b6933b772f41b45918f7e25ed1afbbb1fd892272</code>. [Exact physical-line, source/tag, hypotheses and proofs](reports/2026-10-29-pic-alb-polarization-index-and-generic-tori.md).

- **POME-PIC-ALB-EXACT-PRODUCT-INDEX-001** — low / **verified conditional deduction**: for \(X=C_g\times\mathbb P^{n-1}\), \(g\ge1,n\ge2\), with integral Kähler form \(\omega=\alpha+k\beta\), the *actual* §10.80.4 map satisfies \(B\Lambda=-k^{n-1}\Gamma\) and exact lattice index \(k^{2g(n-1)}\). The induced Picard polarization has type \((k^{n-1})^g\), not necessarily principal. §10.79.11 is explicitly a conditional internal input. Printed Theorem 10.80.4 correct.
- **POME-TORUS-INTEGRAL-H2-NONPOLARIZATION-001** — low / **verified conditional deduction**: a Baire-generic linear complex structure on \(\mathbb R^4/\mathbb Z^4\) has no nonzero integral \((1,1)\) class, despite six independent integral degree-two periods, and hence is nonprojective. Explicit isotropic complementary-plane argument establishes each nonzero lattice condition is proper in both orientation components. Printed Riemann-form criterion §10.80.2 and its minus-sign convention correct.
- **Actual new coverage:** first selected independent proof/model review of §§10.80.2–4; §10.80.1 premise/context only, §10.79.11 and §§10.79.2/.4–5 plus §§10.65.1–2 used as internal lattice prerequisites, not certified. The original **25 chapters / 747 numbered ToC sections / zero complete section certifications** remain. No other old finding closed.
- All dedicated Demailly approximation/regularization plus Bergman/L²/OT/multiscale/positivity-loss programmes remain **deferred-by-user** and untouched. No body/main/source/registry/site/tag/CI/build/formalization modification.

---

# Latest mathematical audit checkpoint — 2026-10-29: exceptional divisor determinant volume and sharp strict-point vanishing

**Reviewed production main:** b6933b772f41b45918f7e25ed1afbbb1fd892272. [New source/tag/blob/physical-line report](reports/2026-10-29-exceptional-ac-volume-and-onepoint-strictness.md).

- **POME-AC-VOLUME-EXCEPTIONAL-NEGATIVE-001** — low / **verified conditional deduction**: for $X=\mathrm{Bl}_p\mathbb P^2$ and $\alpha_a=\pi^*H+a[E]$ ($a\ge1$ integer), $\operatorname{Vol}(\alpha_a)=1$ but $\alpha_a^2=1-a^2$; the positive current $\pi^*\omega_{\mathrm{FS}}+a[E]$ **attains** $\int T_{\mathrm{ac}}^2=1$. Direct exact-sequence proof of section growth; general upper bound still conditional on printed §13.31.1. §§13.31.3–4 remain correct, not a previously recorded full-mass singular-current repetition.
- **POME-ONEPOINT-STRICT-ELLIPTIC-PRODUCT-001** — low / **verified conditional deduction**: for all $n\ge2$, $X=\mathbb P^{n-1}\times C$ with $C$ elliptic, $L=p_1^*\mathcal O(n)$ is semipositive but nowhere strictly positive, yet $H^{n,1}(X,L)=H^{0,n-1}(X,L^{-1})=\mathbb C$. The **strictly positive/negative at one point** premise in printed §10.92.1 is indispensable even on connected projective manifolds. No claim about higher-rank thresholds.
- **Actual coverage:** incremental proof/model checks §§13.31.3–4 and 10.92.1, comparison-only §10.91.2; first orientation of §10.90 (subject heading only, *not* a theorem audit). Unchanged **25-chapter / 747-section inventory; zero entire sections certified**. No previous finding closed.
- All dedicated Demailly approximation/regularization and Bergman/L2/OT/multiscale/positivity-loss proof work remains **deferred-by-user** and untouched; no main/source/site/tag/registry/build/CI/formalization changes.

---

# Latest mathematical audit checkpoint — 2026-10-29: torsion-free Hartogs and all-fiber non-pluripolar disintegration

**Reviewed production main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`; **starting review HEAD:** `4e82d8059895628c7120e4007e31980b5e648a7a`. [New source/tag/blob/physical-line proof report](reports/2026-10-29-hartogs-torsionfree-and-fiber-disintegration.md).

- **POME-HARTOGS-TORSIONFREE-SATURATION-001** — low / **verified conditional deduction**, §9.72.1 printed lemma correct: reflexivity of the ambient sheaf may be relaxed to torsion-freeness. Explicit `(z,w) ⊕ O` nonreflexive example; coherent kernel construction, saturated uniqueness; meromorphic Hartogs remains an identified conditional internal input.
- **POME-FIBER-BOREL-DISINTEGRATION-001** — low / **verified conditional deduction**, §13.6.1 correct: the printed local truncation argument actually proves bounded-Borel-weight disintegration, not only weights `1` and `W-Φ`. Mass bounds and monotone truncation control the fiber integrals.
- **POME-FIBER-ALL-SLICES-LOWER-BOUND-001** — low / **verified conditional deduction**, §13.6.1 correct: on `P¹ × P¹`, a vertical logarithmic divisor gives a joint psh potential `W ≤ Φ` whose special slice is identically `-∞`; the lower domination is necessary for **every** slice to be defined.
- **Actual coverage:** incremental selected §§9.72.1 and 13.6.1; §13.6.3 definition/statement distinction only. Previously inventory-only index sections §§9.57, 10.83 read **orientation-only**, no mathematical proof certification. Original **25 chapters / 747 numbered ToC sections / zero complete sections certified**. All Demailly approximation/regularization and dedicated Bergman/L²/OT/multiscale/positivity-loss work **deferred-by-user** and untouched. No main/source/site/registry/tag/build/CI/formalization modifications.

---

# Latest mathematical audit checkpoint — 2026-10-29: effective fiber equations and exponential Lp tails

**Reviewed main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`; **starting audit branch:** `7ce98250c3524e0d440c9fb857cf5286363dae03`. [Pinned source/tag/line-anchored proofs](reports/2026-10-29-effective-fiber-equations-and-exponential-lp-tails.md).

- **POME-FINITE-PROJECTION-BOUNDED-EQUATIONS-001** — low / **verified conditional deduction**, not a false theorem: in the exact linear-cone, proper finite-projection setting of §9.61.4 with generic degree `d`, vertical dimension `q≥1`, `d(q-1)+1` fixed moment-curve fiber equations of total degree at most `d` cut out the analytic set *set-theoretically*. The direction bound is sharp for this fixed method (explicit finite-fiber obstruction).
- **POME-EXPONENTIAL-LP-TAIL-RATE-001** — low / **verified conditional deduction**, not a false theorem: §15.17.3's λ-exponential density convergence admits an exact `L^p` tail bound, with conditional `O(λ)` under `(B-V_θ)f∈L^p`. A normalized local log-pole example demonstrates **no universal positive power rate** under only envelope domination and `f∈L^p`; it is **not** a counterexample to PDE solutions.
- **Actual coverage:** incremental §9.61.4 and first selected nonexcluded §15.17.3–4, §15.16.5/§15.17.1 statements and §9.61.2 contextual only. Original **25 chapters / 747 numbered sections / zero whole-section certifications** retained; the proof of §15.17.1 and all dedicated Demailly approximation/regularization, Bergman/L²/OT/multiscale/positivity-loss programmes remain **deferred-by-user** and were not inspected. No main/source/site/CI/build/formalization changes.

---

# Latest mathematical audit checkpoint — 2026-10-29: polar boundary spike and A1 Remmert reduction

**Reviewed main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`; **audit starting HEAD:** `558b2abca69b5f2e2d118a0cbcb03478bf7413f4`. [Exact pinned source/tag/line proof report](reports/2026-10-29-polar-boundary-spike-and-cotorsor-remmert.md).

- **POME-PLANAR-GREEN-POLAR-BOUNDARY-SPIKE-001** — low / **verified conditional deduction**, not a false theorem: for the **nonpolar** compact `closed unit disc ∪ {2}`, the raw logarithmic polynomial envelope is zero at 2, while its USC regularization equals `log⁺|z|` and has positive exterior boundary limit `log 2` there. Proposition 3.8.2's polar boundary exception is essential.
- **POME-COTORSOR-A1-REMMERT-001** — low / **verified conditional deduction**, not a false theorem: the zero-ruling torsor's printed cover `C² × Tot(O_P¹(-2))` has a proper Remmert reduction to `C² × {AC=B²}`, contracting precisely its exceptional P¹ fibers; all global holomorphic functions descend. Conditional solely on the printed global cover identification, not on a new proof of its elliptic-lattice construction.
- **Actual new scope:** selected proofs/models of §§3.8.2 and 12.33.3; earlier §§3.8.1 and 12.33.2 context only. Existing **25 chapters / 747 numbered sections / zero complete-section certifications**, no fresh full ToC recount because main unchanged. All dedicated Demailly approximation/regularization and Bergman/L²/OT/multiscale/positivity-loss programmes remain **deferred-by-user**. No production edits, build, CI or formal proof verification.

---

# Latest mathematical audit checkpoint — 2026-10-29: Hopf character divisors and separately smooth subharmonic peaks

**Reviewed main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. [Dated proof, source/tag and physical-line anchored report](reports/2026-10-29-hopf-picard-and-separately-smooth-subharmonic-peaks.md).

- **POME-HOPF-CHAR-MEROMORPHIC-SECTIONS-001** — low / **verified conditional deduction**: on a scalar Hopf surface the character bundle \(L_a\) has a nonzero meromorphic section precisely when \(a=2^m\) for some integer \(m\). Thus \(L_3\) is a holomorphic line bundle outside the image \(\operatorname{Div}\to\operatorname{Pic}\). Correct printed §20.7.3, conditional on the normal-space meromorphic Hartogs extension §9.38.5.
- **POME-SEPARATE-SMOOTH-SUBHARM-PEAK-001** — low / **verified conditional deduction**: the published §3.7 example admits a strengthened **separately \(C^\infty\), separately subharmonic** construction with arbitrarily large diagonal peaks, still finite and not jointly USC; §3.6.1's joint upper-bound/majorant hypothesis remains indispensable. Original §3.7 and §3.6.1 correct.
- **POME-POLY-CONNECTED-COMPLEMENT-NECESSITY-001** — low / **verified conditional deduction**: the connected-complement hypothesis of §3.7.1 is necessary as well as sufficient for universal polynomial approximation of functions holomorphic near compact \(K\), by a bounded complementary-hole maximum-modulus obstruction.
- **Actual selected scope:** first direct proof-level §3.7.1 and its untagged example (formerly contextual); deeper §3.6.1–2; incremental §20.7.3. Only contextual §9.38.5 and §23.1. Existing **25 chapters, 747 numbered sections, zero whole-section certifications**. All user-excluded Demailly approximation/regularization and dedicated Bergman, L², OT, multiscale-atlas and positivity-loss proof programme remains **deferred-by-user**, not resolved. No production/source/site/registry/tag/build/CI/formalization changes.

---

# Latest mathematical audit checkpoint — 2026-10-29: smooth Hessian parameter response and ordinary-type nonseparation fiber

**Reviewed current main:** b6933b772f41b45918f7e25ed1afbbb1fd892272. [Complete new direct proof and continuum example with source keys, permanent tags, main blobs and physical line anchors](reports/2026-10-29-hessian-linear-response-and-envelope-nonseparation.md).

- **POME-HESSIAN-SMOOTH-LINEAR-RESPONSE-001** — low / **verified conditional deduction**; §8.8.3 correct. Under a smooth one-parameter family of proper intermediate-degree Hessian exponents with common barriers and uniform derivative lower bound kappa, implicit elliptic differentiation gives (L_w-f_t) dot(w)=f_s, ||dot(w)||_infty<=||f_s||_infty/kappa, and f_s>=0 forces dot(w)<=0. The constant is attained for f_s=t+sc. This is the smooth **linear response operator**, not a repetition of the earlier §8.13 one-sided *measure-residual* estimate. New direct selected §8.8.1–3 proof inspection; upstream global PDE a priori/viscosity inputs conditional.
- **POME-ORDINARY-TYPE-UNCOUTABLE-FIBER-001** — low / **verified conditional deduction**, §18.10.1 correct. Convex compositions u_alpha=1-(1-w)^alpha for 0<alpha<1 of one cutoff logarithmic omega-psh pole give continuum many **distinct** bounded-difference classes, all with P_omega[u_alpha]=P_omega[u_alpha]_I=0 and identical tau_{omega,0} neighborhoods. Incremental §18.10.1 check only; its mass comparison was not reaudited.
- **Coverage:** exact main ToC unchanged at **25 chapters / 747 numbered sections / zero whole-section certifications**. Only §8.8 directly newly audited; §18.10 incremental. All dedicated Demailly approximation/regularization, Bergman/L2/OT/multiscale/positivity-loss work remains **deferred-by-user**, not resolved. No production/main/source/site/body/registry/tag/CI/build/formalization changes.

---

# Latest mathematical audit checkpoint — 2026-10-29: bounded Bedford–Taylor TV obstruction, Kähler variance, and explicit modification lift

**Reviewed main:** b6933b772f41b45918f7e25ed1afbbb1fd892272; **original review HEAD:** a228e82aa470a173bd82c9b3291f5e4e900157d6. [Complete new mathematics with exact source keys, permanent tags and main physical lines](reports/2026-10-29-bt-tv-kahler-variance-and-divisor-lift.md).

- **POME-BT-UNIFORM-PSH-SINGULAR-TV-001** — low / **verified conditional deduction**: smooth uniformly bounded psh potentials on the disk converge uniformly, but their Bedford–Taylor measures remain mutually singular with the circular weak limit, and their signed total-variation norm tends to \(2\). Printed Theorem 7.5.8 only asserts weak convergence, and is correct.
- **POME-KAHLER-MA-NORMALIZATION-VARIANCE-001** — low / **verified conditional deduction**: **Kähler-only**, \(b(F)=\log\int_X\omega^n-\log\int_Xe^F\,dV\), hence for affine \(F_t=F+tG\), \(\ddot b_t=-\operatorname{Var}_{\nu_t}(G)\) in all complex dimensions. Comparing Theorem 14.8.1 yields an exact weighted complex-Hessian-square identity; the general Hermitian result and prior variance/n inequality remain distinct.
- **POME-MODIFICATION-DIVISOR-AEPPLI-LIFT-001** — low / **verified conditional deduction**: on \(\operatorname{Bl}_p\mathbb P^2\), the lifted positive current of a line through \(p\) is \([\widetilde L]+[E]\). Dropping \([E]\) leaves the pushforward unchanged but violates the required Aeppli pullback class. Theorem 5.66.2 is correct in this explicit model; its Hodge heat proof was **not** opened.
- **Coverage:** first selected **nonexcluded** §5.66.2 divisor model; incremental §§7.5.8 and 14.8.1. Context only §§7.2, 14.1, 14.4, 11.23. Original **25 chapters / 747 numbered sections / zero entire sections certified**. Demailly approximation and dedicated Bergman/L²/Ohsawa–Takegoshi/multiscale/positivity-loss remain **deferred-by-user**. No production/source/registry/tag/site/CI/build/formalization changes.

---

# Latest mathematical audit checkpoint — 2026-10-28: current homotopy mass topology and nonzero second spectral differential

**Reviewed main:** b6933b772f41b45918f7e25ed1afbbb1fd892272; **starting audit branch:** 7aa546a53cb1d997f423f79cf74539ef11d92336. [Complete independently checked calculations, exact source labels/tags/blobs/lines](reports/2026-10-28-current-homotopy-mass-and-spectral-d2.md).

- **POME-CURRENT-HOMOTOPY-TV-GAP-001** — low / **verified conditional deduction**, §5.54.2 correct: for compactly supported finite-mass degree-q currents the de Rham homotopy correction obeys a quantitative mass estimate M(K_eps T) <= C eps M(T). On an atomic 1-current, the bound is sharply linear in eps, while the associated smooth average remains TV-distance 2 from the atom at every eps. This is a stress test of the **real current homotopy**, not the user-excluded Demailly psh-regularization proof programme.
- **POME-SPECTRAL-D2-ZIGZAG-001** — low / **verified conditional deduction**, §10.54.2 correct: an explicit four-term bounded double complex has two nonzero E2 terms joined by an isomorphism d2; its total complex is acyclic. The calculation independently checks the filtered representative and totalization signs without asserting E2 collapse.
- **Exact coverage:** first selected *nonexcluded current-homotopy portion only* of previously inventory-only §5.54; incremental §10.54.2; §5.54.1 and §10.55.2 necessary context only. **25 chapters / 747 numbered sections, zero fully certified**. All Demailly approximation/regularization, dedicated Bergman/L2/OT/multiscale/positivity-loss work remains **deferred-by-user**. No body/main/source/registry/site/permanent-tag/build/CI/formalization modifications.

---

# Latest mathematical audit checkpoint — 2026-10-28: monomial Newton multiplier ideals and sharp elliptic relative embedding

**Reviewed main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`; **starting audit HEAD:** `3c8eab9c71d11875033be6435db7ef5e61bcf4f2`. [Full physical-line, source-label, permanent-tag and mathematical proofs](reports/2026-10-28-monomial-newton-ideals-and-elliptic-relative-embedding.md).

- **POME-MONOMIAL-NEWTON-MULTIPLIER-001** — low / **verified conditional deduction**, printed Theorem 6.12.8 correct: direct polar-logarithmic integral proof of the exact Newton-polyhedron multiplier-ideal formula for *arbitrary finite monomial ideals*, including all strict boundary faces and analytic power-series sufficiency. For `(x²,y³)`, the log canonical threshold is exactly `5/6`; the constant fails to be integrable at equality, and `I(φ)=(x,y)` at `c=5/6`. Entirely outside user-excluded regularization/Bergman/L²/OT proof programmes.
- **POME-RELATIVE-ELLIPTIC-POWER-OPTIMAL-001** — low / **verified conditional deduction**, printed Lemma 9.71.1 correct: on the trivial elliptic family with fiber degree-one positive line bundle, the first tensor power admitting the required closed relative projective embedding is **exactly 3**, by curve Riemann–Roch and separation of points/first jets. General Grauert base change remains a quoted external input; the earlier L² vanishing proof remains user-deferred.
- **Exact new scope:** first selected independent nonexcluded model in previously inventory-only **§6.12**; incremental independent sharpness in already selected **§9.71**; internal §10.78.9 and §7.1 introduction only as conditional/contextual references. Existing **25 chapters / 747 numbered ToC sections**, **zero** full-section certifications. No previously open mathematical error or proof gap silently repaired or relabeled; all excluded tasks stay **deferred-by-user**. No main/source/tag/registry/site/CI/build/formalization changes.

---

# Latest mathematical audit checkpoint — 2026-10-28: toric facet vanishing distributions and Newton interior coercivity

**Reviewed main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`; **starting audit HEAD:** `c7a5d4213bc2dab8b3e8b35684c2425d2ec29ba0`. [Full source-anchored proof and exact coverage](reports/2026-10-28-toric-facet-filtration-and-logsum-coercivity.md).

- **POME-TORIC-FACET-VANISH-DH-001** — low / **verified conditional deduction**: toric character sections have exact normalized vanishing-weight empirical distributions converging narrowly to the facet affine-functional pushforward of polytope Lebesgue measure. On `P=d Delta_2` the (unnormalized) DH density is `(d-t) 1_[0,d](t) dt`, probability moments `2 d^j/[(j+1)(j+2)]`. The published §21.9.5 and §19.6.18 remain correct; earlier §19.6.16 error is not duplicated.
- **POME-LOGSUM-RELINT-COERCIVITY-001** — low / **verified conditional deduction**: §21.4.6's bounded-below condition `alpha in conv(beta_i)` sharpens to quotient-space coercivity and integrability of `exp(-H_alpha)` **iff** `alpha` lies in the relative interior of the finite Newton polytope; boundary points lose both. Explicit symmetric one-variable integral equals `pi/b`.
- **Exact incremental coverage:** new selected §§21.4.6 and 21.9.2/.5; §19.6 definitions and §21.7.3 only as conditional inputs. **25 chapters / 747 numbered sections, no entire section certified.** User-excluded Demailly approximation/regularization + dedicated Bergman/L2/OT/multiscale/positivity-loss work remains **deferred-by-user**. No main/source/site/CI/build/formalization changes.

---

# Latest mathematical audit checkpoint — 2026-10-28: nonnormal isolated Hartogs poles and maximal convex tubes

**Reviewed main:** <code>b6933b772f41b45918f7e25ed1afbbb1fd892272</code>; **starting audit HEAD:** <code>8574b4195dc023866c9763a133a0138db90b5510</code>. [New complete sharpness proofs with source labels, permanent tags, and exact physical lines](reports/2026-10-28-nonnormal-hartogs-poles-and-maximal-convex-tubes.md).

- **POME-HARTOGS-NORMALITY-ISOLATED-POLE-001**, low / **verified conditional deduction**: the irreducible nonnormal affine surface Spec C[s²,st,t²,s³,t³] has a meromorphic function s that is holomorphic away from its codimension-two vertex but not at the vertex. This proves normality is essential to §9.38.1 Hartogs extension and §9.38.2 purity of the meromorphic non-holomorphic-germ pole set. The **printed normal-space results are correct**.
- **POME-BOCHNER-TUBE-CONVEX-HULL-MAXIMAL-001**, low / **verified conditional deduction**: for each point outside the convex-hull tube of an open connected real base, a separating real linear form defines a holomorphic hyperplane-reciprocal function on the original tube that cannot extend through that point. §9.39.7 is therefore optimal as the **common guaranteed** convex-tube extension, not as the maximal domain of every individual function. The printed theorem remains correct; its extension existence proof is still an upstream conditional input.
- **Precise coverage:** new targeted model proofs as increments in **already selected §§9.38–9.39**; first **statement-level only** §18.3 hypothesis/conclusion crosscheck against §18.1.2, **no excluded proof reopened**. §9.37 heading context only. Existing **25 chapters / 747 distinct ToC sections** retained, **zero** whole sections certified. All Demailly approximation/regularization plus dedicated Bergman/L²/OT/multiscale/positivity-loss tasks retain **deferred-by-user**; no production/source/registry/tag/site/CI/build/formalization edits.

---

# Latest mathematical audit checkpoint — 2026-10-28: local mixed residual masses and the classical/non-pluripolar split

**Reviewed main:** b6933b772f41b45918f7e25ed1afbbb1fd892272; **starting audit HEAD:** 6d65a806d4ce26e4745b11045a94df9f782cd799. [Detailed proofs, tags, exact file blobs and physical lines](reports/2026-10-28-local-mixed-logconvexity-and-isolated-npp-discrepancy.md).

- **POME-LOCAL-MIXED-MASS-LOGCONVEX-SHARP-001** — low / **verified conditional deduction**: for isolated analytic weights a=log(|z|^(2p)+|w|^(2q)), b=log(|z|²+|w|²) in C², the classical residual mixed atoms are (m0,m1,m2)=(1,min(p,q),pq). The local **log-convex** inequality of printed §6.51.1 is correct in this model, can be arbitrarily strict, and must not be replaced by global cohomological log-concavity.
- **POME-ZERO-LELONG-CLASSICAL-NPP-SPLIT-001** — low / **verified conditional deduction**: the explicit isolated weights U_n in printed §6.50.11/.14 satisfy (dd^c U_n)^n_classical=δ0 with ν(U_n,0)=0, while the Definition 13.11.1 non-pluripolar top product is identically zero. Every restricted truncated product vanishes already at finite cutoff; this contrast requires no problematic limit interchange. The upstream classical mass construction remains conditional, not independently certified here.
- **Exact coverage:** first selected nonexcluded proof and statement passages in previously inventory-only §§6.50 and 6.51; incremental Definition 13.11.1; §6.49 dependency context only. The original **25 chapters / 747 distinct section IDs** remain in the matrix; **zero** whole sections certified. All Demailly approximation/regularization and dedicated Bergman/L²/OT/multiscale/positivity-loss items remain **deferred-by-user**. No production/source/body/registry/site/tag changes or builds, CI, tests or formal verification.

---

# Latest mathematical audit checkpoint — 2026-10-28: maxima of multiplier ideals and the critical Sobolev C¹ boundary

**Reviewed main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`; **starting audit HEAD:** `467b09fa9df1071dd2106b9cf78f32d0529f7314`. [Detailed mathematical proofs, source tags and physical lines](reports/2026-10-28-max-ideals-and-critical-sobolev-boundary.md).

- **POME-MULTIPLIER-MAX-IDEAL-SUM-001** — low / **verified conditional deduction**, printed §16.24.1–2 correct. On `P¹×P¹`, the global θ-psh divisor weights `u=log|s₁|²`, `v=log|s₂|²` satisfy `I(u)_p=(x)`, `I(v)_p=(y)` but `I(max(u,v))_p=O_p`; hence the multiplier ideal of a maximum is **not** generally the ideal sum `(x,y)`, despite the correct minimum formula for divisorial Lelong numbers. Distinguish ideal operations when integrating §16.6/§18.4.
- **POME-HERM-SOB-CRITICAL-C1-001** — low / **verified conditional deduction**, printed §11.24.1 correct. A compactly supported `f(x)=χ(|x|)x₁ log log(e/|x|)` belongs to `W^{2,2n}` in real dimension `2n≥2`, while its gradient is unbounded. Thus the proof's `W^{2,p}→C¹` step cannot be invoked at `p=2n`. This **does not disprove** Fredholm theory at the endpoint.
- **Precise new coverage:** incremental selected arguments in previously sampled §§16.24 and 11.24; introductory §§16.1, 11.3, 18.2 were contextual only. Existing ToC matrix retains **25 chapters / 747 section IDs**, **zero whole-section certifications**. No previously excluded Demailly approximation/regularization or dedicated Bergman/L²/OT/multiscale/positivity-loss work reopened; statuses remain **deferred-by-user**. No main, source, registry, site, tags, build, tests, CI or publication changes.

---

# Latest mathematical audit checkpoint — 2026-10-28: directional torus, sharp jet order and two equation aliases

**Reviewed current main:** b6933b772f41b45918f7e25ed1afbbb1fd892272; **starting audit HEAD:** d8e5ca08d6218c1ece22e7c89236661ee672ab92. [Complete three-finding source/tag/physical-line report](reports/2026-10-28-directional-torus-jet-threshold-and-equation-alias.md).

- **POME-DIRECTIONAL-EQ-ALIAS-NESTED-001** — medium / **confirmed error (reading-edition integration only)**: in §6.37, complete (6.37.6–7) occur inside Theorem 6.37.5, but separate retained-tag chunks F71249678342/B7F196B96D6D at line 128 and both tag pages show isolated terminal equalities, with invalid nested aligned/align markup. This is a **distinct two-tag manifestation** of the previously documented §6.36 alias-export defect; not a false theorem and not a new mathematical duplication. Keep the source tags; propose canonical complete-equation rendering.
- **POME-DIRECTIONAL-JET-THRESHOLD-SHARP-001** — low / **verified conditional deduction**: Cor. 6.39.13's condition (k+1) min(lambda) >= max(lambda) is essential for uniform k-jet invariance. On the line z1=0, coordinate systems (z1,z2) and (z1+z2^(k+1),z2) share k-jets but yield generalized numbers k+2 and k+1 for weights (1,k+2). Original corollary **correct**.
- **POME-DIRECTIONAL-TORUS-BINOMIAL-GAP-001** — low / **verified conditional deduction**: V=log|z1^m+z2^b|^2 has exact weighted-torus mean r min(m/lambda1,b/lambda2), supremum 2 log(A+B), and a sharp within-family mean–supremum defect at most 2 log 2, including equality on resonant slopes. Directional-number identification remains conditional on the printed theorem.
- **Actual new coverage:** selected, nonexcluded pieces of previously inventory-only §§6.37 and 6.39; §6.34/§6.36 only as existing conditional inputs. Main-aligned ToC inventory remains 25 chapters / 747 sections, **zero** whole sections certified. All Demailly approximation/regularization and its dedicated Bergman/L2/Ohsawa–Takegoshi/multiscale/positivity-loss programmes remain **deferred-by-user**. No main/source/registry/permanent-tag/website edits, tests, builds, CI or formalization.

---

# Latest mathematical audit checkpoint — 2026-10-28: finite Dolbeault traces, exact blowup jets and the projective dimension bound

**Reviewed current main:** <code>b6933b772f41b45918f7e25ed1afbbb1fd892272</code>; **starting audit HEAD:** <code>5aa4f41894c9c26fba96e433aaa68783245c4ec2</code>. [Complete three-finding source/tag/physical-line report](reports/2026-10-28-finite-dolbeault-trace-point-jets-and-projection-dimension.md).

- **POME-FINITE-DOLBEAULT-TRACE-SPLIT-001** — low / **verified conditional deduction**: the current-valued left inverse of the correct §10.91.1 modification injection extends to every surjective proper generically finite holomorphic map of positive degree \(d\), with the exact normalized transfer \(d^{-1}f_*\). Branch loci have measure zero; bundle-valued smooth/current Dolbeault comparison is a stated, unrecertified input.
- **POME-BLOWUP-POINT-JET-H1-OPTIMAL-001** — low / **verified conditional deduction**: on the one-point blowup of \(\mathbb P^2\), \(h^1(kH-mE)=\binom{m+1}{2}-\binom{\min(k,m-1)+2}{2}\) for all \(m\ge1,k\ge0\), giving the **exact** threshold \(k\ge m-1\). This verifies that the linear order in correct Proposition 10.41.1 cannot be uniformly reduced to sublinear growth.
- **POME-EMBEDDING-DIMENSION-GENUS2-001** — low / **verified conditional deduction**: a genus-two curve admits no embedding into \(\mathbb P^2\), whereas Theorem 10.41.2 embeds it into \(\mathbb P^3\); the universal \(2n+1\) bound is optimal for \(n=1\), without claiming sharpness in all dimensions.
- **Actual coverage:** first targeted proof pass in previously inventory-only **§10.41**; incremental §10.91.1 (already sampled 2026-10-27), and contextual §10.43.11/§10.87.1 only. Fresh ToC count **25 chapters / 747 sections**, **zero** whole sections certified. All dedicated Demailly approximation/regularization and Bergman/L²/Ohsawa–Takegoshi/multiscale/positivity-loss projects retain **deferred-by-user** status. No main/source/registry/tag/website/build/CI/formalization changes.

---

# Latest mathematical audit checkpoint — 2026-10-28: nodal cycle stalks and arbitrary convex intersection closure

**Reviewed current main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`; **starting audit branch HEAD:** `761432437250660fe278ee086c041a8a0b30600a`. [Detailed two-finding report](reports/2026-10-28-nodal-cycle-stalks-and-convex-interior-closure.md).

- **POME-CYCLE-NODAL-LOCAL-BRANCH-001** — low / **verified conditional deduction**, not a false theorem. The globally irreducible nodal plane curve `y²=x²(1+x)` has analytic 1-cycle global module `Λ[C]` but stalk at the node `Λ[C_+]⊕Λ[C_-]`; restriction is the diagonal `[C]→(1,1)`. Correct §20.6.3 gluing/branch rule must not be canonicalized by global component counts.
- **POME-CONVEX-INTERIOR-ANCHOR-001** — low / **verified conditional deduction**, original §19.7.11 correct. For an **arbitrary**, possibly uncountable family of convex sets sharing an open ball, closure commutes with intersection. A direct common-anchor proof avoids interchange of limits or sequential compactness; explicit nested strip-plus-origin example shows failure with nonempty but empty-interior intersection.
- **Actual coverage:** incremental selected passages in §§20.6 and 19.7, both previously sampled; no entire section certified. Fresh count **25 chapters / 747 numbered sections**. All Demailly approximation/regularization and dedicated Bergman/L²/OT/multiscale/positivity-loss work stays **deferred-by-user**. No main/source/body/registry/tag/site/build/CI/formalization change.

---

# Latest mathematical audit checkpoint — 2026-10-28: null-form reducibility and MRC products over curves

**Reviewed current main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`; **starting review head:** `a75651e5fdedfb2aee64a6f344715ab19d9072ad`. [Detailed two-finding source/tag/physical-line-anchored report](reports/2026-10-28-null-reducibility-and-mrc-curve-products.md).

- **POME-NULL-ALPHA-REDUCIBILITY-001** — low / **verified conditional deduction**. Smooth closed complex \(\alpha=(i/2)dz_1\wedge d\bar z_2\) and smooth semipositive \(\beta=(i/2)dz_3\wedge d\bar z_3\) on \(\mathbb C^3\) satisfy every wedge test of §7.15.4 with \(p=q=1\), yet their common real kernel is zero rather than the hypothetical complex dimension \(1\). The retained reducibility assumption on \(\alpha\) is indispensable; this complements, without duplicating, the printed example that drops positivity of \(\beta\). Original proposition correct.
- **POME-MRC-PROJECTIVE-CURVE-COTENSOR-001** — low / **verified conditional deduction**. For \(X=\mathbb P^r\times C\), \(r\ge1\), \(g(C)\ge1\), the MRC quotient is \(q:X\to C\). Any pseudoeffective \(L\) admitting \(L\to(\Omega_X^1)^{\otimes m}\ne0\) is \(q^*M\) with \(0\le\deg M\le m(2g-2)\); genus one forces \(M\) trivial. Hence \(\nu(X,L)\le\nu(C,K_C)\), sharply, for this entire family. This is a **special case of open Question 24.12.2 only**, not a general resolution.
- **Actual coverage:** incremental direct §7.15.4 + first selected §24.12.2 hypothesis/model check; prior §19.10/§22.1 checks consulted only to avoid duplicate findings. **747** ToC IDs, **zero** whole sections certified. All Demailly approximation/regularization plus dedicated Bergman/L²/OT/multiscale/positivity-loss work remains **deferred-by-user**. No main/site/source/body/registry/permanent-tag/CI/build/formalization modification.

---

# Latest mathematical-audit checkpoint — 2026-10-28, non-Delzant toric cone and intrinsic almost-complex torsion

**Reviewed current main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. **Starting audit HEAD:** `59a8c1afae4ef4f6e5ae7a3be5342c6b4e3aa02f`. [Pinned theorem tags, physical lines, and complete algebraic checks](reports/2026-10-28-nondelzant-quadric-and-almost-complex-torsion.md).

- **POME-TORIC-NONDELZANT-QUADRIC-CONE-001** — low / **verified conditional deduction**, not a false theorem: the non-Delzant integral triangle `conv{(0,0),(2,0),(0,1)}` produces the projective quadric cone `Z0 Z2=Z1²`, singular at its non-unimodular vertex. Thus the smooth-polytope hypothesis in §21.8.3 is genuinely necessary for smooth affine vertex charts. Older toric reference-cycle findings are unchanged.
- **POME-ALMOSTCOMPLEX-TORSION-BRACKET-001** — low / **verified conditional deduction**, not a false theorem: the explicit distribution `T^{1,0}=span{∂z1, ∂z2+z1∂bar z1}` has bracket `∂bar z1`, tests the minus sign of the torsion correction in Eq. 9.53.3 and shows `(d'')² z1` is a nonzero `(0,2)` form. The formally integrable hypothesis in Eq. 9.53.4 cannot be omitted.
- **Actual scope:** incremental selected nonexcluded statement/proof and countermodel checks in §§21.8 and 9.53, both already partially reviewed; not new first-section counts and not full certifications. The current chapter ToC contains 747 distinct numbered sections; **zero** completely certified. No source, main, canonicalization, registry, tag, website, CI, build or formalization edits. All Demailly approximation/regularization and dedicated Bergman/L²/OT/multiscale/positivity-loss programme notes remain **deferred-by-user**.

---
# Latest mathematical-audit checkpoint — 2026-10-28, cone-adapted multiplicity and Jensen equation alias

**Reviewed main:** b6933b772f41b45918f7e25ed1afbbb1fd892272. **Starting audit HEAD:** 4264019bb6a9cbee7d007d53542f0bf2e1861aa6. [Exact integrated file paths, permanent tags, physical lines and proofs](reports/2026-10-28-cone-adapted-projections-and-jensen-equation-alias.md).

- **POME-JENSEN-EQ-ALIAS-NESTED-001** — **medium / confirmed error in reading-edition integration only** (not a false theorem): §6.36 canonical complete two-line Eq. 6.36.6 is followed by a separate truncated right-hand-side fragment with invalid nested aligned/align delimiters; its permanent tag page reproduces the bad fragment. Recommend suppressing the orphan chunk and linking its stable tag to the full canonical formula without changing mathematical content.
- **POME-CONE-PROJECTION-SHEET-UNBOUNDED-001** — low / **verified conditional deduction**, printed §§6.35.2 and 6.38.3 correct: reduced irreducible plane germs y^m=x^k (coprime k>m) have ordinary multiplicity m, but the non-cone-adapted finite y-projection has k sheets and weighted number k. The ratio k/m is unbounded with m fixed, proving the sharp need for the stated cone hypothesis.
- **Independent §6.36 Jensen test:** in dimension one for the radial log pole, the full-pole equation is the explicitly permitted extended identity +infinity=+infinity; the finite annular equation reads r-r0=r-r0. Not a third new finding.
- **Precisely limited new coverage:** selected nonexcluded passages in §§6.35, 6.36, 6.38 only; prior §§6.43–6.48 contextual. **747** numbered ToC sections retained; **zero** complete sections certified. The theorem's smoothing reference and all dedicated Demailly approximation/regularization, Bergman/L²/OT/multiscale/positivity-loss work remain **deferred-by-user**, not reopened. No main/source/body/registry/tag/site/build/CI/formalization changes. Existing audit PR #9 is closed and merged; no new PR.

---

# Latest mathematical-audit checkpoint — 2026-10-28, infinitely near divisors and analytic-ideal thresholds

**Reviewed `main`:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. **Starting audit HEAD:** `74ed8e9ada205ba2f214facc675dcd52c2a87669`. [Exact source/tag/physical-line anchored proof report](reports/2026-10-28-infinitely-near-lelong-and-analytic-ideal-thresholds.md).

- **POME-LELONG-INFINITELY-NEAR-JUMP-001** — low / **verified conditional deduction**: for \(\log(|x|^2+|y|^4)\), point Lelong and first exceptional generic Lelong are \(1\), but the exceptional divisor of a second blowup at a special point has generic Lelong \(2\). Distinct divisorial valuations must not be canonicalized merely by their center. §5.16.11 model-independence wording also needs an explicit common-resolution comparison step if expanded; its statement is correct.
- **POME-ANALYTIC-IINF-MULTIPLIER-GAP-001** — low / **verified conditional deduction**: the analytic weight \(\log(|x|^4+|y|^6)\) on a bidisc has \(\mathcal I=(x,y)\) but \(\mathcal I_\infty=(x^2,xy^2,y^3)\). Full elementary weighted-integrability and uniform-dominance threshold proofs are in the report. No false printed theorem or completed global analytic input.
- **Actual new coverage:** selected nonexcluded statements/proof fragments of §§5.16 and 5.18, which were previously only inventoried; 747 unique ToC sections retained, **none fully certified**. §5.18.9–10 approximation and the entire dedicated Demailly/Bergman/L²/OT/multiscale/positivity-loss programme remain **deferred-by-user**, not reopened. No main/site/source/registry/tag/build/CI/formalization changes.

---

# Latest mathematical-audit checkpoint — 2026-10-28, classical collar endpoints and projective nilradical twists

**Reviewed `main`:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. **Starting review HEAD:** `2f9bca2d9bf51ea9aecffca37a5b36da5189c9a1`. [Three exact source/tag/line-anchored proofs](reports/2026-10-28-classical-collar-sharp-endpoints-and-projective-nilradical-twists.md).

- **POME-COLLAR-WEIGHT-TOP-ENDPOINT-001**, low / **verified conditional deduction**: Corollary 7.31.3's \(q\le n-1\) is sharp. On the complex ball with \(u_j=V=\log|z|^2\), all boundaries avoid the isolated pole; the \(q<n\) trace has integrable logarithmic weight, but the **classical** top product is \(\delta_0\) and cannot integrate \(V\). Conditionally, permitted \(q<n\) traces charge no complete pluripolar set defined by an ambient psh function.
- **POME-COLLAR-ANALYTIC-LOCUS-DIM-ENDPOINT-001**, low / **verified conditional deduction**: for \(1\le p<n\), the current \(T=[\{z_{p+1}=\cdots=z_n=0\}]\) and \(u=\log|z_{p+1}|^2\) prove the analytic-pole-locus threshold \(\dim A\le p-1\) in §7.31.4 is optimal.
- **POME-PROJ-NILRADICAL-GLUING-TWIST-001**, low / **verified conditional deduction**: two allowed nonreduced graded Proj constructions have the same reduced \(\mathbb P^1\), but nilradicals \(\mathcal O(-1)\) and \(\mathcal O\), respectively, and are not isomorphic; preserve distinct nonreduced structures in §9.59/9.60.
- **Actual scope:** first selected nonexcluded §7.31 non-smoothing passages; increment in historically selected §9.59 and §9.60.1 context. **747** unique ToC section IDs retained, **zero** whole sections certified. All prior issue statuses unchanged. §7.31.1 smoothing and the entire dedicated Demailly/Bergman/L²/OT/multiscale/positivity-loss programme remain **deferred-by-user**. No source/main/registry/tag/site/CI/build/formalization modifications.

---

# Latest mathematical audit checkpoint — 2026-10-28, elliptic Hodge families and real de Rham closed range

**Current main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. **Starting audit HEAD:** `6086d6374afc442a6ba5dfed05ef182301b544b1`. [Dated source/tag/line-anchored proof report](reports/2026-10-28-hodge-family-semicontinuity-and-real-derham-closed-range.md).

- **POME-HODGE-HARMONIC-UPPER-SEMICONT-001** — low / **verified conditional deduction**. For a $C^1$-continuous compact family of elliptic complexes with uniformly positive scalar Laplacian symbols, the harmonic/cohomology dimensions are upper semicontinuous. Uniform Gårding + compact $H^1\to L^2$ proves this without a general eigenvalue-continuity theorem. The flat unitary connection $d+it\,dx$ on $S^1$ exhibits a strict drop; printed §10.46 is correct.
- **POME-DE-RHAM-PERIOD-CLOSED-RANGE-001** — low / **verified conditional deduction**. Via the standard de Rham period comparison, every ordinary real de Rham differential has closed range in the compact-open smooth Fréchet topology on a second-countable manifold; hence the *real* duality hypothesis of §10.59.3 is automatically met. The compact/ordinary pairing uses the **continuous**, not full algebraic, dual; $\coprod S^1$ gives an exact product/direct-sum distinction. The smooth-period comparison is conditional, not a new proof of §10.70.3. No assertion for arbitrary noncompact Dolbeault ranges.
- **First selected proof-level scope:** §§10.46, 10.57, 10.59 only; §10.70.3 dependency crosscheck, not first coverage. Actual current main rendered chapter ToC re-counted: **25 chapters, 747 unique section IDs**, **zero** full sections certified. Demailly approximation/regularization and dedicated Bergman/$L^2$/OT/multiscale/positivity-loss work remains **deferred-by-user**, unopened. No original false theorem found, no project builds/tests/CI/formalization or production edits.

---

# Latest mathematical audit checkpoint — 2026-10-28, Lefschetz norms, curvature thresholds, and duplicated proof

**Fresh production main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. **Starting audit HEAD:** `7b3b9f87f5e66dde96194ca2b3137d300b94fe8b`. [Detailed source/tag/physical-line anchored English report](reports/2026-10-28-lefschetz-norm-curvature-threshold-and-duplicate-proof.md).

- **POME-CURVATURE-CANONICAL-PROOF-DOUBLE-RENDER-001** — **medium / confirmed error in reading-edition integration, not a false theorem**: the entire canonical proof of Theorem 10.48.3 is also rendered verbatim below the “See Theorem 10.48.3” shared-entry reference in §10.49, without a local theorem statement. Exact normalized 2,481-character proof equality checked. Propose suppressing only the stray proof via a separately reviewed renderer/canonicalization patch, preserving canonical theorem, proof, aliases, attribution and permanent tags.
- **POME-LEFSCHETZ-HARMONIC-NORM-OPTIMAL-001** — **low / verified conditional deduction**: from §10.47.1/15 obtain sharp global harmonic Lefschetz norm bounds `s!‖v‖ ≤ ‖ω^s∧v‖ ≤ (s+⌊k/2⌋)!/⌊k/2⌋! ‖v‖` for `s=n−k`, with both constants attained by parallel forms on flat tori. Upstream Hodge analytic input is conditional.
- **POME-PARTIAL-CURVATURE-BOUNDARY-SHARP-001** — **low / verified conditional deduction**: `X=ℙ^(n−s+1) × T^(s−1)`, `L=p₁*O(n−s+3)` has curvature rank `n−s+1` everywhere but nonzero `H^{n,s−1}(X,L)` and `H^{s−1}(X,L^k)` for every `k≥1`. Thus thresholds of §10.49.4 and §10.49.6 are optimal. The printed vanishing theorems remain correct.
- **Precisely limited new coverage:** §§10.47, 10.48, 10.49 at specified statements/proofs. §11.3/11.5 only background. **747** ToC IDs, **zero** full sections certified. All user-excluded Demailly approximation/regularization and dedicated Bergman/L²/Ohsawa–Takegoshi/multiscale/positivity-loss work remains **deferred-by-user**, unopened. No main/source/registry/tag/site/CI/build/formalization change.

---

# Latest mathematical audit checkpoint — 2026-10-28, exponential measure-order sharpness and transcendental Morse coefficient

**Fresh production main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. **Starting audit HEAD:** `2f3bb4465182ee0ac5c3f62b70746776895a3c25`. [Full two-finding source/tag/line-anchored report](reports/2026-10-28-exponential-measure-order-and-transcendental-morse-sharpness.md).

- **POME-EXP-MEASURE-LOGRATIO-LINF-SHARP-001** — low / **verified conditional deduction**: nonzero finite non-pluripolar data with (e^mmu\le\nu\le e^Mmu) yield ordered unique exponential solutions (u-M/\lambda\le v\le u-m/\lambda); the coefficient (1/\lambda) and both signs are sharp for constant multiples. Selected §10.31.44 and §13.19.3 only; existence, domination and related analytic prerequisites remain conditional.
- **POME-TRANS-MORSE-COEFF-N-SHARP-001** — low / **verified conditional deduction**: on ((\mathbf P^1)^n), (a=\sum h_i), (b=t h_1) gives *equality* in §10.98.2 and shows its coefficient (n) is optimal, even when (b) is made Kähler by a small perturbation. The trace/eigenvalue constants and final simultaneous-nef perturbation have been independently checked. Printed §10.98's regularization input at line 37 is **deferred-by-user**, not reopened or certified.
- **Actual new limited coverage:** §§10.31 and 10.98, previously inventory-only. Exact anchors and conditional inputs in the report. **747** current unique ToC sections, **zero** completely certified sections. No claim of full existence proofs, project builds/tests/CI/formalization or publication. All excluded Demailly approximation/regularization and dedicated Bergman/L²/OT/multiscale/positivity-loss tasks remain **deferred-by-user**.

---

# Latest mathematical audit checkpoint — 2026-10-28, Morse equation aliases and metric/spectral limits

**Fresh production main:** b6933b772f41b45918f7e25ed1afbbb1fd892272. **Starting audit HEAD:** d16eef2f0c21ce6226a5efbcd4305a6ff0a8e77f. [Exact source/tag/physical-line anchored report](reports/2026-10-28-morse-equation-aliases-metric-gh-and-spectral-vague.md).

- **POME-HOLO-MORSE-ALIGN-ALIASES-001** — medium / **confirmed reading-edition integration error**, **not a false theorem**: §10.96.1 correctly displays three holomorphic Morse rows, but §10.96.3–4 are each duplicated as malformed nested display-environment aliases, including on their own permanent-tag pages. Repair the canonical group-row placement without dropping any permanent tags. No production patch has been made.
- **POME-METRIC-COMPLETIONS-GH-001** — low / **verified conditional deduction**: uniform convergence of the completed-distance pullback pseudometrics in Corollary 5.39.8 yields Gromov–Hausdorff convergence of compact metric quotients, with a sharp factor-one-half distortion bound. No noncollapse is claimed absent a uniform positive lower metric bound.
- **POME-MORSE-SPECTRAL-VAGUE-001** — low / **verified conditional deduction**: Theorem 10.95.5's small-spectrum counting convergence at continuity points implies vague convergence of normalized full spectral counting measures, including possible atoms in the limiting distribution; convergence of counts at those atoms is **not** inferred.
- **First selected proof-level inspection:** §§5.39, 10.95, 10.96 only, with precise limits in the report. **747** current ToC section IDs preserved; **zero** completely certified sections. The original spectral/magnetic analytic inputs remain conditional. No main/source/body/registry/permanent-tag/site/CI/build/browser/formalization edits. All user-excluded Demailly approximation/regularization and dedicated Bergman/L²/OT/multiscale/positivity-loss programmes remain **deferred-by-user** and untouched.

---

# Latest mathematical audit checkpoint — 2026-10-28, Siu residual pole and positive-cone threshold

**Fresh production main:** b6933b772f41b45918f7e25ed1afbbb1fd892272. **Starting audit HEAD:** aa3e29c54e6dc51f099751ec4aecff64370d68ff. [Source/tag/line anchored report](reports/2026-10-28-siu-residual-lelong-and-movable-duality-gauge.md).

- **POME-SIU-RESIDUAL-POINT-LELONG-001** — low / **verified conditional deduction**: on ℂ², $T=dd^c\log|z|^2$ has a positive point Lelong number but a purely residual bidimension-one Siu decomposition; its classical square is $\delta_0$ and its non-pluripolar square vanishes. The explicit regularized Hessian density integrates to 1, with no false printed theorem.
- **POME-MOVABLE-DUAL-THRESHOLD-GAUGE-001** — low / **verified conditional deduction**: assuming the printed §10.100.1 cone duality, the one-sided pseudoeffective threshold is exactly the supremum of normalized negative pairings with individual modified Kähler single powers. Sharp explicit ℙ¹×ℙ¹ limit and strict-gap estimate. The approximation cited by §10.100 remains **deferred-by-user** and unverified.
- **First limited coverage:** §§6.40, 6.49, 10.100; precise selected claims and dependencies are in the report, not whole-section certifications. **747** unique ToC IDs; **zero** completely certified sections. No main/source/body/registry/tag/site/CI/test/build/formalization changes. All prior user-deferred dedicated Demailly/Bergman/L²/OT/multiscale/positivity-loss tasks remain **deferred-by-user**.

---

# Latest mathematical audit checkpoint — 2026-10-28, infinite Ext products and non-PID injective dimensions

**Fresh production main:** b6933b772f41b45918f7e25ed1afbbb1fd892272. **Review starting HEAD:** 8e85fb0c7ae18c5f4dcb1d1e2745d04a280e4ca8. [Complete current-main source/tag/line-anchored report](reports/2026-10-28-infinite-ext-products-nonpid-length-and-coherent-topology.md).

- **POME-EXT-INFINITE-CYCLIC-PRODUCT-001** — low / **verified conditional deduction**: $\operatorname{Ext}^1_{\mathbb Z}(\bigoplus_{r\ge1}\mathbb Z/2^r,\mathbb Z)=\prod_{r\ge1}\mathbb Z/2^r$, not a direct sum; this Ext even has elements of infinite order. The printed finite-generation qualifier in §10.68.4 is correct and essential.
- **POME-EXT-NONPID-INJECTIVE-DIMENSION-001** — low / **verified conditional deduction**: over $R=\mathbb Q[x,y]$, the explicit length-two Koszul resolution gives $\operatorname{Ext}^2_R(R/(x,y),R)=\mathbb Q$. Thus PID length-one injective resolutions from §10.68.2 cannot be extended to arbitrary commutative rings.
- **Actual new selected coverage:** §§10.68 (explicit algebraic resolution/UCT proofs) and 9.51 (only cover-order Lemma 9.51.1, Mayer–Vietoris cone Lemma 9.51.9 and compact finiteness Theorem 9.51.10, conditional on their cited nonexcluded inputs). No new false printed theorem. User-excluded weighted $L^2$ §9.51.2 and all dedicated Demailly regularization/Bergman/L²/OT/multiscale/positivity-loss work remain **deferred-by-user** and unopened. Exactly **747** ToC IDs retained, **zero** entire sections certified. No main, source, body, tags, registry, site, tests, CI or formalization changes.

---

# Latest mathematical audit checkpoint — 2026-10-28, componentwise top cohomology and one-point vanishing

**Fresh main:** b6933b772f41b45918f7e25ed1afbbb1fd892272. **Starting audit branch HEAD:** f134fde1c03070e7c70c23f5fc9bc04feae70261. [Full current integrated-source mathematical report](reports/2026-10-28-top-degree-components-ext-and-onepoint-connectedness.md).

- **POME-TOP-COHOM-COMPONENT-PRODUCT-001**, low / **verified conditional deduction**: top-degree ordinary cohomology on a possibly disconnected paracompact n-manifold is the **product** of orientation-coinvariant classes from its compact connected components; connected noncompact components contribute zero. R disjoint union S¹ has nonzero H¹ despite being noncompact, so the printed connected hypothesis matters.
- **POME-DUALIZING-EXT-STALK-ENDPOINT-001**, low / **verified conditional deduction**: on R with A=Z/2 and M=Z, Hom=0 but Ext¹=Z/2, giving a genuine degree-one dualizing cohomology row; the Ext hypothesis of §10.72.3 is necessary.
- **POME-ONEPOINT-VANISH-EACH-COMPONENT-001**, low / **verified conditional deduction**: P¹ disjoint union P¹ with O(1) on one and O on the other is semipositive globally and strictly positive somewhere but has H^{1,1}=C. To extend §10.92.1 to disconnected compact manifolds, strict positivity **on every component** is a sufficient condition. The printed connected corollary is correct.

New first **selected, not complete** proof coverage §§10.71, 10.72, 10.92. §10.91 merely a historically checked dependency; §9.55 already has a separate finding and is not repeated. All **747** ToC section IDs retained and **zero** entire sections certified. No new confirmed false printed theorem, build, tests, formalization, CI, main/source/body/tag/registry change or publication. Excluded Demailly approximation/regularization and dedicated Bergman/L²/OT/multiscale/positivity-loss items remain **deferred-by-user**.

---

# Latest mathematical-audit checkpoint — 2026-10-28, bounded exponential stability and smooth-center blowup density thresholds

**Fresh production main:** b6933b772f41b45918f7e25ed1afbbb1fd892272. **Starting review head:** 17ec85a05311aeb681827ed0bc6f797d0e90803a. [Detailed source-anchored English proof and explicit limitations](reports/2026-10-28-resolved-blowup-lp-and-bounded-exponential-stability.md).

- **POME-BOUNDED-EXP-DENSITY-L1-STABILITY-001** — low / **verified conditional deduction**: for a fixed bounded Monge–Ampère reference, uniformly bounded nonnegative densities converging in L1(reference), with positive limiting mass, give bounded exponential-equation solutions converging in L1 and capacity, and their Monge–Ampère measures converge in total variation. This is sequential, and depends on the existing uniform trace estimate, normalized psh compactness, and dominated capacity stability of §15.10; no independent existence proof.
- **POME-BLOWUP-PUSHFORWARD-LP-CODIM-001** — low / **verified conditional deduction**: a smooth positive volume upstairs pushed through the blowup of a smooth complex codimension-r center produces downstairs density in Lp **exactly** for 1<=p<r/(r-1); logarithmic divergence at the endpoint. Extends the point-center r=n example in §15.22.7. Jacobian calculation independently checked for r=2,...,6.
- **POME-RESOLVED-REMAINDER-FIBER-CRITERION-001** — low / **verified conditional deduction**: a continuous (in particular Hölder) resolved remainder descends continuously across a proper modification **iff** it is constant on every fiber. Thus printed §15.22.2's Hölder remainder *on Y* cannot imply a continuous remainder on X when its exceptional trace varies, as explicitly allowed in §15.22.7.

**Actual new limited coverage:** §§15.10 (Step 2), 15.16 (Steps 2–3 only), 15.22 (blowup density, pushforward and mass-defect algebra); all three were inventory-only. **747** distinct ToC section IDs retained; **zero** whole sections certified. §15.16 Step 1 and any analytic input relying on the user-excluded Demailly approximation/regularization and dedicated Bergman/L2/OT/multiscale/positivity-loss programme remain **deferred-by-user**, not reopened or resolved. No new confirmed false theorem, no main/source/body/registry/tag/website/CI/build/formalization changes. Only a five-case symbolic Jacobian cross-check was run.

---

# Latest mathematical-audit checkpoint — 2026-10-28, ideal-type collapse, sharp current dimensions, Stein jet endpoint

**Fresh production main:** b6933b772f41b45918f7e25ed1afbbb1fd892272. **Starting review head:** 9bac0ec9e795112180b7af459d01f1d14fee153d. [Exact current-reading source-anchored report](reports/2026-10-28-zero-lelong-ideal-collapse-hausdorff-threshold-and-jet-endpoint.md).

- **POME-IDEAL-ZEROLELONG-COLLAPSE-001** — low / **verified conditional deduction**: on a disc, the subharmonic family \(u_a=-(-\log|z|^2)^a\), \(0<a<1\), has zero Lelong numbers and *trivial multiplier ideals for every real weight* \(k>0\), but produces an uncountable strictly ordered chain of distinct ordinary singularity types. Printed §5.33 order/ideal comparison remains correct; optional semantic guard, not a false theorem.
- **POME-HAUSDORFF-TRACE-EXPONENT-SHARP-001** — low / **verified conditional deduction**: integration current of a complex \((n-j)\)-plane positively charges a set of zero Hausdorff \(s\)-measure for every \(s>2(n-j)\), so the null-set exponent of correct Corollary 5.34.3 is optimal. Independent §5.34.4 projective-line Lelong normalization was checked without new defect.
- **POME-STEIN-JET-WEIGHT-ENDPOINT-001** — low / **verified conditional deduction**, *local mechanism only*: a holomorphic germ of order \(m\) is integrable against \(|z|^{-2c}\) on \(\mathbb C^n\) exactly when \(m>c-n\). Therefore \(c=n+\ell\) in Theorem 9.29.1 is the smallest coefficient that forces vanishing of all order-\(\le\ell\) holomorphic jets by the local weighted argument. The corollary's hull implication was also checked; global \(L^2\) existence and smoothing inputs remain conditional, **not** audited.

**Actual new selected coverage:** §§5.33, 5.34, 9.29, limited to specified integrated passages; 747 ToC section IDs retained and **zero** whole sections certified. No new confirmed false theorem. Entire Demailly approximation/regularization and dedicated Bergman/\(L^2\)/Ohsawa–Takegoshi/multiscale/positivity-loss proof-completion programme remains **deferred-by-user**, untouched. No main/source/registry/permanent-tag/site/build/CI/formalization changes.

---

# Latest mathematical-audit checkpoint — 2026-10-28, normalized finite-map trace and compact de Rham duality

**Pinned main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. **Initial audit HEAD:** `d66ceeb98dac4938559f13344d8f996feba2376c`. [Detailed dated source-anchored report](reports/2026-10-28-finite-curve-trace-average-and-algebraic-duality.md).

- **POME-CURVE-FINITE-TRACE-PSH-AVERAGE-001** — low / **verified conditional deduction**, no false theorem. For any degree-\(d\) finite holomorphic map of compact curves and \(h\in\mathrm{PSH}(C',r^*\beta)\), the normalized ramification-weighted fiber trace \(A_rh=d^{-1}\sum_{r(x)=s}e_xh(x)\) is \(\beta\)-psh, has curvature \(\beta+dd^cA_rh=d^{-1}r_*(r^*\beta+dd^ch)\), and Lelong numbers \(d^{-1}\sum_x\nu(h,x)\). Explicit quadratic-map \(\mathbb P^1\) example proves that this is **not** the printed §5.43.15 fiber maximum, which has minimum adjusted Lelong number. The two valid semantics must not be deduplicated; optional corollary, no body modification.
- **Actual new selected proof-level reading:** **§5.43** finite-curve descent and trace §§5.43.4–.16 (selected only); **§10.73** de Rham compact-support trace sign and algebraic duality (selected only). §5.44 was **already historically reviewed**; this run merely crosschecked fixed and moving non-pluripolar measure arguments without repeating older findings. All **747** current section records retained, **zero** whole-section certifications; no new confirmed false printed theorem.
- Dependencies such as full Godement/Ext duality, Cegrell fixed-measure convergence, and the bounded-current torsion calculus remain conditional. All dedicated Demailly approximation/regularization, Bergman/L²/Ohsawa–Takegoshi/multiscale/positivity-loss historical items remain **deferred-by-user**, untouched. No main/body/source/registry/tags/site/build/CI/formalization modifications.

---

# Latest mathematical audit — 2026-10-27, sharp Hessian coefficient and codimension-two heat trace rates

**Pinned main:** b6933b772f41b45918f7e25ed1afbbb1fd892272. **Branch:** review/mathematical-audit. [Complete dated source-anchored report](reports/2026-10-27-hessian-deleted-coefficient-and-heat-lp-rates.md).

- **POME-HESS-DELETED-COEFF-SHARP-001** — low / **verified conditional deduction**: Lemma 8.2.8 is correct, and its factor \((1-c_{N,q})^{-1}=4/3\) is actually attained at \(n=4,m=2,q=1\) by the boundary Hessian eigenvalues \((\sqrt3-2,\sqrt3-2,1,1)\); interior cone points approach equality. This is within the actual §8.1 assumption \(2\leq m<n\), not the superseded out-of-scope \(m=1\) objection.
- **POME-HEAT-CODIM2-LP-RATE-SHARP-001** — low / **verified conditional deduction**: Lemma 3.10.5 and heat mass conservation give \(t|\int (h_t\rho)F|\leq B^{1/p}\rho(X)^{1-1/p}t^{1-1/p}\|F\|_p\) for \(1<p\leq\infty\). Explicit fixed singular \(L^p\) functions on a flat two-torus show the polynomial exponent is optimal; an \(L^1\) example has only logarithmic decay, excluding any general positive-power rate. Distinct from older POME-HEAT-FROSTMAN-CODIM-001.
- **New first selected reading:** §10.88 Proposition 10.88.2 (étalé Hausdorff identity principle and coherence in the *regular/polynomial ring-sheaf* category), correct as printed. §§8.2 and 3.10 are increments, not new first-review rows. **747** unique current ToC rows remain; **zero** complete section certifications; no new confirmed false theorem. Existing unresolved and **deferred-by-user** items remain unchanged. Dedicated Demailly approximation/regularization and Bergman/\(L^2\)/OT/multiscale/positivity-loss programme remains entirely unexamined. No main/source/registry/tags/site/build/CI/formalization changes.

---

# Latest mathematical-audit checkpoint — 2026-10-27, compact embedding and positive Green-energy weak/strong separation

**Fresh current main:** b6933b772f41b45918f7e25ed1afbbb1fd892272. **Starting audit HEAD:** 228abedaaea2ac833f281ee60f65a11711cc3eaf. **Exact integrated-source report:** [2026-10-27 compact-coordinate embedding and energy weak/nonstrong](reports/2026-10-27-compact-coordinate-embedding-and-energy-weak-nonstrong.md).

**Two new low-severity verified conditional deductions, no false printed theorem:** POME-COMPACT-CHART-EMBEDDING-BILIPSCHITZ-001 proves the cutoff-coordinate map of Lemma 5.2.7 is already a smooth embedding and its chord metric is bi-Lipschitz to any smooth Riemannian distance on **connected compact** X. POME-GREEN-ENERGY-WEAK-NONSTRONG-SPHERES-001 gives \(\mu_j=2^{-j}\sigma_{4^{-j}}\) on \(\mathbb R^3\), with \(\|\mu_j\|^2=1\), mass \(2^{-j}\to0\), and \(\|\mu_j-\mu_{j+1}\|=1\): vague/weak-energy convergence does not imply strong energy convergence. No conclusion on arbitrary nets is inferred from a sequential theorem.

**Actual limited coverage:** first selected nonexcluded §§5.2 and 6.10 (only Proposition 6.10.6's algebraic closure step, **not** its OT/L2/Hilbert-space dependencies), with an incremental direct §§4.5.4–5 energy check. §7.1 used only for normalization consistency. All **747** unique ToC sections retained, **zero** complete sections certified. No builds, tests, CI, formalization, source/registry/tag/main changes or site publication. Demailly approximation/regularization and its dedicated Bergman/L2/OT/multiscale/positivity-loss programme remain **deferred-by-user**, untouched.

---

# Latest mathematical-audit checkpoint — 2026-10-27, algebraic cusp avoidance and sharp Finsler fiber margins

**Fresh current `main`:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`; **starting audit HEAD:** `0dd559673f4d539ff49838a3da3ddc003c96a7a5`. **Full exact source-anchored report:** [sharp cubic non-integrability locus and fiber margins](reports/2026-10-27-projective-cusp-avoidance-and-fiber-convexity-margins.md).

**Two low-severity, verified conditional deductions; no false printed theorem:** `POME-PROJ-CUSP-AVOIDANCE-DIM-SHARP-001` constructs the irreducible cubic $Z_0Z_1^2-Z_2^3$ with coefficient $r=11/12$ on $\mathbb P^n$, $n\geq3$: its non-integrability locus is exactly the linear $\mathbb P^{n-2}$, so §9.56.2's avoiding $\mathbb P^{n-a-1}=\mathbb P^1$ dimension is optimal. `POME-FINS-FIBER-MARGIN-EXACT-001` computes the exact convexity constant in Example 11.10.1 as $c_*(z)=|z|^2$ for $z\ne0$ but $c_*(0)=1$, showing quantitative failure of uniform neighborhood fiber convexity from individual-fiber convexity.

**Independent selected §10.77 review:** main proof-level passages 10.77.5–7/.10 (surface exhaustion, normalized univalent Jacobian/coefficients, normal-family embedding); no new defect, no certification of Hodge/Riemann mapping upstream inputs. **Actual new coverage:** selected §9.56 and §10.77; §11.10 exact example increment with previous historical check retained. All **747** unique ToC sections remain, **zero** entire sections certified. No body/main/registry/tags/site/CI/build/formalization changes. The entire dedicated Demailly approximation/regularization and Bergman/$L^2$/OT/multiscale/positivity-loss programme remains **deferred-by-user**, untouched; §9.56.3 extension was not audited.

---

## Previous checkpoint (preserved verbatim)

# Latest mathematical-audit checkpoint — 2026-10-27, compact obstacle envelopes and Kiselman sharpness

**Pinned reviewed main:** <code>b6933b772f41b45918f7e25ed1afbbb1fd892272</code>. **Audit branch:** <code>review/mathematical-audit</code>. **Full English mathematics and anchored proofs:** [report](reports/2026-10-27-compact-obstacle-kiselman-joint-positivity-and-curvature-integrality.md).

**Four new low-severity IDs, no false printed theorem:** <code>POME-KISELMAN-JOINT-PSH-ESSENTIAL-001</code> proves on compact \(\mathbb P^1\) that smooth uniformly strictly \(\theta\)-psh slices and strict \(t\)-convexity on a bounded interval do *not* make the parameter infimum \(\theta\)-psh without joint \((x,t+i s)\) positivity; exact Schur determinant is negative. <code>POME-KISELMAN-INTERNAL-COROLLARY-REFERENCE-001</code> gives the precise existing internal proof bridge from Corollary 5.12.2 to Proposition 5.41.3, retaining its historical SGPT/Kiselman attribution (verified repair proposal, not body edit). <code>POME-COMPACT-OBSTACLE-SUPNORM-STABILITY-001</code> gives the sharp coefficient-one envelope comparison for **arbitrary bounded obstacles on a non-pluripolar compact set** in any big, potentially nonclosed \(\theta\) background (extended-valued inequalities, finite-locus norm only). <code>POME-LINE-CURVATURE-INTEGRAL-PERIOD-001</code> demonstrates a closed smooth positive \(\sqrt2\,\omega_{\rm FS}\) which still cannot be singular line-bundle curvature because its period is nonintegral. Printed §5.41.3 and §5.45.1 are correct under their actual hypotheses.

**Actual coverage newly upgraded:** only selected §§5.40, 5.41, 5.45, with §5.12.2 checked as an existing internal dependency. The **747** unique actual ToC rows remain, **zero** complete-section certifications; upstream normal compactness, Josefson, comparison and proof of §5.12.2 not certified. No body/source/registry/tags/main/website/build/CI/formalization modifications. The entire dedicated Demailly approximation/regularization and Bergman/L²/Ohsawa–Takegoshi/multiscale-atlas/positivity-loss proof-completion programme remains **deferred-by-user**, untouched.

---
## Previous checkpoint (preserved verbatim)

# Latest mathematical-audit checkpoint — 2026-10-27, holomorphic hulls and saturated Hartogs extensions

**Pinned reviewed main:** <code>b6933b772f41b45918f7e25ed1afbbb1fd892272</code>. **Branch:** <code>review/mathematical-audit</code>. **Dated proof report:** [Hartogs saturation and punctured hull](reports/2026-10-27-hartogs-saturated-sheaves-and-punctured-hull.md).

**Three new low-severity verified conditional deductions, no false printed theorem:** (1) <code>POME-HARTOGS-SATURATED-NONBUNDLE-001</code>: on a punctured bidisc the saturated extension of the subbundle generated by \((z,w)\) has torsion-free but non-locally-free quotient \((z,w)\), so is not a subbundle at the puncture; §9.72.1 tag <code>0A2146B324EB</code> lines 9–18. (2) <code>POME-HARTOGS-CODIMONE-ESSENTIAL-001</code>: \((1,e^{1/z})\) gives a saturated subbundle on a punctured disc with no saturated coherent extension across the codimension-one point; same source/tag. (3) <code>POME-HOLOHULL-PUNCTURED-SPHERE-001</code>: the holomorphic hull of the unit sphere in \(\mathbb C^2\setminus\{0\}\) is exactly the punctured closed ball, which is not compact in that manifold; §9.13.2 tag <code>8FBCDB96A2E2</code>, lines 52–89.

**Actually new selected proof coverage:** §9.13, Proposition 9.13.1 and Theorem 9.13.2, including Cauchy-homogeneous and interpolation/Baire steps; previously listed as inventory only. §9.72 received incremental edge-case validation, not new first-review coverage. §9.71's Grauert base-change dependence was contextually rechecked but is **not a new finding**. The 747-section matrix is preserved; no full section is certified.

**Outstanding:** §9.72 relies on normal meromorphic codimension-two extension; §9.71 relies on Grauert base-change and on user-deferred §10.102 inputs. The entire Demailly approximation/regularization and dedicated Bergman/L²/Ohsawa–Takegoshi/multiscale/positivity-loss programme remains **deferred-by-user**, not resolved or certified. No source, main, tags, builds, CI or publication changed.

---
## Previous checkpoint (preserved verbatim)

# 2026-10-27 — Strictly positive Monge–Ampère density is essential for local trace-to-smoothness; measurable-coefficient ABP input

**Freshly reviewed main:** b6933b772f41b45918f7e25ed1afbbb1fd892272. **Starting audit head:** 5dc554e85f165dfb8656f891d7244c03d59b3dca. [Full dated source-pinned report](reports/2026-10-27-degenerate-ma-trace-sharpness-and-abp-viscosity.md).

- **POME-MA-INTERIOR-POSITIVE-DENSITY-NECESSITY-001 — low / verified conditional deduction:** In complex dimension $n\geq2$, $u(z)=(\max\{\operatorname{Re}z_1,0\})^2$ is psh and $C^{1,1}$ but not $C^2$, has bounded current trace $\operatorname{tr}_\beta dd^cu=\mathbf1_{\{\operatorname{Re}z_1>0\}}/2$, and has zero Bedford–Taylor top product. Hence the $F>0$ hypothesis in Proposition 15.18.5 cannot be weakened to smooth $F\geq0$. The printed proposition itself is not false.
- **POME-MA-INTERIOR-ABP-VISCOSITY-INPUT-001 — medium / external dependency:** The §15.18.5 $W^{2,q}$ strong-solution-to-viscosity passage (main lines 202–210) explicitly invokes GT01 Aleksandrov maximum principle, including a *measurable coefficient field* in the lower-test direction, then variable-coefficient Evans–Krylov and Schauder. This is an application-specific **unresolved self-containment input**, not a duplicate assertion that the general Evans–Krylov theorem is new; existing **POME-MA-SMOOTH-REG-EXTERNAL-001** remains unresolved.
- **Actual newly inspected coverage:** selected lines 50–126, 135–213, 225–290 and 295–411 of **§15.18 only** (the last two are limited hypothesis/sign reviews), one formerly inventory-only ToC row upgraded. All **747** distinct numbered ToC rows remain; **zero** complete-section certifications. No build/tests/CI/formalization/main/source/tag/site modification. Dedicated Demailly approximation/regularization, Bergman/$L^2$/OT/multiscale/positivity-loss programmes remain **deferred-by-user** and unopened.

---

# 2026-10-27 — Unibranch obstacle descent, strictly convex Gauss maps, and Hermitian sharpness

**Reviewed current main:** b6933b772f41b45918f7e25ed1afbbb1fd892272. **Starting audit head:** cf7cc8c49f2fd2b51bd085ae89429a9db2ad2684. [Full proof with source labels, tags, file SHA and physical line anchors](reports/2026-10-27-unibranch-obstacle-descent-gauss-map-gaussian-sharpness.md).

- **POME-UNIBRANCH-CONTINUOUS-OBSTACLE-DESCENT-001 — low / verified conditional deduction:** for a proper compact Kähler modification $\pi:Y\to X$ with $X$ unibranch, any continuous obstacle $f$ and nonempty $\mathrm{PSH}(X,\theta)$ satisfy $\pi^*P_\theta(f)=P_{\pi^*\theta}(f\circ\pi)$; proof uses the actual pullback bijection and descent, without commuting usc regularization with pullback. Previously open Fornæss–Narasimhan input **POME-UNI-EXT-FN-001** stays unresolved.
- **POME-STRICT-CONVEX-GAUSS-DIFFEO-001 — low / verified conditional deduction:** the compact strictly tangent-convex $C^2$ domain in Proposition 9.16.2 has every boundary point exposed and a globally $C^1$-diffeomorphic outward Gauss map $\partial D\to S^{m-1}$. No $C^2$ inverse is claimed.
- **POME-COMPLETE-HERM-GAUSSIAN-SHARPNESS-001 — low / verified conditional deduction:** on complete flat $\mathbb C$ with Gaussian Hermitian line metric, the minimum-norm $\bar\partial$ solution saturates **constant one** in the precise inverse-curvature energy estimate of Theorem 11.49.3; $A\ge\lambda_0 I$ also gives the expected closed-form spectral gap. Transitive energy/graph-core inputs remain conditional.
- **Independent §9.53 check, no separate finding:** correct minus sign of the non-integrability tensor, polynomial $\bar\partial$ homotopy correction and uniform Levi error were read directly. The global Newlander–Nirenberg $L^2$ existence chain was not audited.
- **Actual new coverage:** selected passages only in §§9.10, 9.16, 9.53, 11.49; four previously inventory-only ToC rows upgraded, all 747 unique section identifiers retained, zero full sections certified. No new false printed theorem, no build/tests/CI/formal proof/source/main/tag/site change. All dedicated Demailly approximation/regularization, Bergman/L²/OT/multiscale/positivity-loss items remain **deferred-by-user** and unopened.

---

# 2026-10-27 — Quantified Hölder-dominated Monge–Ampère interpolation; exact determinant-duality curve boundary

**Reviewed main:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`; **audit starting head:** \`c5174d2febe6dbc34110438dba394fec5b3e2f56\`. [Complete English report with hypotheses, source labels, permanent tags, physical lines and proofs](reports/2026-10-27-holder-dominated-ma-interpolation-and-determinant-curve-edge.md).

- **POME-HOLDER-DOMINATED-MA-UNIFORM-INTERPOLATION-001 — low / verified conditional deduction:** For any (even uncountable) family of normalized bounded continuous $h$-psh potentials $\varphi_i$ whose Monge–Ampère measures are uniformly dominated by those of uniformly $C^{0,\alpha}$ $h$-psh references, the *pairwise* norm bound $\|\varphi_i-\varphi_j\|_\infty\le C\|\varphi_i-\varphi_j\|_{L^1}^{\alpha/((\alpha+2n)(6n+1))}$ follows from the existing Hölder-measure, square-capacity and stability estimates. This makes the §15.25 uniform-convergence mechanism quantitative **without** checking its separately deferred §5.42.7 regularization input.
- **POME-GAUD-DETERMINANT-DIM1-EXACT-001 — low / verified conditional deduction:** Proposition 10.97.4's trace-feasibility condition has an elementary exact $n=1$ analogue: $\int_X\psi\ge\int_X\nu$ is necessary and sufficient for a smooth representative $R=\psi+dd^cu\ge\nu$; at equality any admissible positive current equals $\nu$. The printed $n\ge2$ proposition remains unchanged and correct under its own conditions.
- **Independent selected §9.50 check (no extra new finding):** spectral q-convex metric and conditional bundle vanishing/Runge-density proof passages checked. On $\mathbb C\supset\Delta$, polynomials approximate $1/(1-z)$ in all compact smooth seminorms but no entire extension exists: density cannot be upgraded to surjectivity. No excluded Hilbert-complex L² proof-completion work was reopened.
- **Actual new coverage:** first selected proof-level §§9.50, 10.97 and 15.25 (three inventory-only rows upgraded), 747 unique current ToC rows preserved, no entire section/upstream chain certified and no newly false printed theorem. No tests/builds/CI/formalization/publishing/main/source/tag changes. All Demailly approximation/regularization and dedicated Bergman/L²/Ohsawa–Takegoshi/multiscale/positivity-loss work remains **deferred-by-user** and untouched.

---

# 2026-10-27 — Exact Hartogs bridge hull, complete finite-volume Kähler puncture cusp, and Hodge-symbol sign checks

**Reviewed main:** b6933b772f41b45918f7e25ed1afbbb1fd892272; **initial review head:** de4c9e61443ae6d23e794c739688e877a38c653c. [Complete English proof, labels, blobs and physical lines](reports/2026-10-27-hartogs-bridge-exact-hull-and-explicit-puncture-kahler-cusp.md).

- **POME-HARTOGS-BRIDGE-EXACT-HULL-001 — low / verified conditional deduction:** §9.30's glued two-chart Riemann domain has the *exact* holomorphic hull of its example circle $K$: $\widehat K_{\mathcal O(X)}=\pi^{-1}(\{z=3/4,|w|\le7/8\})$, including both points over the negative unglued overlap. This explicit formula strengthens the existing noncompactness demonstration; Proposition 9.30.1 remains correct.
- **POME-PUNCTURE-KAHLER-FINITE-CUSP-001 — low / verified conditional deduction:** §9.31.2's complete Kähler metric on $\mathbb C^n\setminus\{0\}$ admits an independent explicit elementary construction with a **finite-volume puncture cusp**, $\omega_{\mathrm{eucl}}+\lambda i\partial\bar\partial(\chi[-\log\log(1/|z|^2)])$. Exact Hessian radial/tangential eigenvalues and integrable $r^{-2n}L^{-(n+1)}$ density are proved; no dedicated $L^2$ or regularization proof is revisited. The regular-open hypothesis of §9.31.1 remains necessary.
- **Independent selected §10.82 check:** Hodge-star and formal-adjoint signs, scalar principal symbol of the twisted Laplacian, and exact nonflat counterexample to interpreting $D$ as a cochain differential; no false theorem found and no extra new finding claimed.
- **Actual coverage:** first specified proof-level inspection of exactly §§9.30, 9.31 and 10.82 (three inventory rows upgraded), preserving **747** ToC section rows. No complete-section or upstream analytic-division/Hodge theorem certification; no CI/build/tests/formalization/publishing or main/source/tag changes. Dedicated Demailly approximation/regularization, Bergman/L²/Ohsawa–Takegoshi/multiscale/positivity-loss programmes remain **deferred-by-user** and untouched.

---

# 2026-10-27 — Quasi-everywhere equality strengthens plurifine locality; closed contact sets do not suffice

**Reviewed main:** b6933b772f41b45918f7e25ed1afbbb1fd892272. **New selected proof review:** §§5.9 and 5.47, contextual cross-check (not recounted) of previously reviewed §13.2. [Detailed report with stable tags, physical main lines, complete proof and boundary counterexample](reports/2026-10-27-quasieverywhere-plurifine-locality-and-closed-contact-counterexample.md).

- **POME-PLURIFINE-QE-EQUALITY-LOCALITY-001 — low / verified conditional deduction:** If psh tuples agree off a pluripolar exceptional set inside a *plurifine-open* $W$, the agreement automatically holds pointwise on all of $W$. The equalizer is plurifine closed since the extended-real target is Hausdorff, and the complement of every pluripolar set is plurifinely dense (Prop. 5.47.16). Hence locally bounded Bedford–Taylor products agree on $W$ (Thm. 5.47.22); if both non-pluripolar products are locally finite, they also agree on $W$ (Prop. 13.2.6). The result does not require $W$ or the exceptional set to be Borel. **Boundary sharpness:** $u=\max\{0,\log|z|^2\}$ and $v=0$ agree on the closed unit disk but $dd^cu$ gives mass one on its boundary while $dd^cv=0$. Plurifine openness cannot simply be removed.
- **Adjudication and exact scope:** no newly disproved printed theorem. Proof-level selected entries: §5.47.14–16, .20–23, .25/.27, and §5.9.1/.3–4; contextual verification of §13.2.2/.6. Two formerly inventory-only matrix entries upgraded, not entire sections. 747 chapter/section identifiers preserved; no build, CI, formal proof, release or website publication. All Demailly regularization and dedicated Bergman/L²/OT/multiscale/positivity-loss historical items remain **deferred-by-user**, neither certified nor reopened.

---

# 2026-10-27 — Point-ideal blowup: first nef Cartier b-divisor model and strict Dolbeault descent

**Reviewed main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`; **starting audit head:** `1352f713ef37704dabde09d82995ac7849d48e2d`. [Full pinned-source proof and exact labels](reports/2026-10-27-point-ideal-bdivisor-model-and-modification-dolbeault.md).

- **POME-POINT-IDEAL-BDIVISOR-NONBASE-CARTIER-001 — low / verified conditional deduction:** on \(\mathbb P^2\), \(T=\omega_{\rm FS}+dd^c\log(|Z_1|_{\rm FS}^2+|Z_2|_{\rm FS}^2)\) has analytic singularity only at \(p=[1:0:0]\), so its base divisorial part is zero. On \(\widetilde X=\operatorname{Bl}_p\mathbb P^2\), \(\pi^*T=[E]+f^*\omega_{\rm FS,\mathbb P^1}\): the trace b-divisor has its nef Cartier realization upstairs, but not on the original base, as integration over \(E\) distinguishes the classes (1 versus 0). The same explicit form shows that modification pullback on \(H^{1,1}_{\bar\partial}\) need not be surjective, consistently with the printed split-injection theorem.
- **Actual new scope:** §20.4.11/.14–15/.18 selected proof and example, plus first selected §10.91.1–2. §20.4.20/.22/.24 previously reviewed, **not** recounted. No newly false printed theorem, whole-section certification, project builds/tests, CI, formal verification or publication. All 747 section identifiers retained; Demailly approximation/regularization and the dedicated Bergman/L²/OT/multiscale/positivity-loss programme remain **deferred-by-user** and unexamined.

---

# 2026-10-27 — Pluriclosed surface volume, a continuum of I-equivalent polar masses, and sharp one-sided mixed-MA bounds

**Reviewed main:** b6933b772f41b45918f7e25ed1afbbb1fd892272. [Full pinned English proofs, source tags, permanent tags and physical lines](reports/2026-10-27-pluriclosed-surface-mass-and-inequivalent-mixed-ma-bounds.md).

- **POME-GAUD-SURFACE-MASS-PLURICLOSED-001 — low / verified conditional deduction:** on a compact complex surface, total Hermitian MA mass satisfies \(\int(\theta+dd^cv)^2=\int\theta^2+2\int v\,dd^c\theta\); for a positive background potential-independence is equivalent to \(dd^c\theta=0\), not \(d\theta=0\). An explicit nonclosed, positive pluriclosed metric on the flat complex 2-torus demonstrates the distinction.
- **POME-POLAR-I-TYPE-MASS-CONTINUUM-001 — low / verified conditional deduction:** scaling the existing §13.4.11 atom-free polar potential gives all \(\omega_{\rm FS}\) non-pluripolar masses \(1-t\), \(t\in[0,1]\), all multiplier ideals trivial, but pairwise different ordinary and P-singularity types; positive P-background \((1+\delta)\omega_{\rm FS}\) handles the endpoint \(t=1\). The old §16.8.19 pairwise example is explicitly *not* registered again.
- **POME-MIXED-MA-NONREVERSE-KAHLER-001 — low / verified conditional deduction:** on \((\mathbb P^1)^n\), strictly Kähler \(T_{i,\varepsilon}=\omega_i+\varepsilon\sum_j\omega_j\) have pure top-density \(n!(1+\varepsilon)\varepsilon^{n-1}\), but mixed density \(\sum_{k=0}^n\binom nk k!\varepsilon^k\to1\); no dimension-only reverse geometric-mean estimate. Proportional Kähler forms attain coefficient 1 in the printed *lower* bound.

**Actual scope:** first selected proof passages in §§13.4–13.5, first explanatory/definition-only review in §§12.1 and 16.7; prior §§16.3/16.8 used as dependencies, not re-counted. All **747** ToC section identifiers retained; no whole-section certification, new false printed theorem, source edit, project build, CI, formal verification or publication. All previously deferred-by-user Demailly approximation/regularization and dedicated Bergman/L2/OT/multiscale/positivity-loss work remains untouched.

---

# 2026-10-27 — Split Frölicher pages under modifications; explicit complex-torus Hodge numbers

**Reviewed main:** b6933b772f41b45918f7e25ed1afbbb1fd892272; **starting review head:** 70608f5b76eda0322898690d69552a01a52c7d8a. [Complete source-anchored proofs and boundary conditions](reports/2026-10-27-modification-frolicher-retract-and-torus-fourier-hodge.md).

- **POME-MODIFICATION-FROLICHER-PAGE-SPLIT-001 — low / verified conditional deduction:** §10.87.1's chain-level current identity, plus smooth/current Dolbeault \(E_1\)-comparison, gives a split injection of **every** Frölicher \(E_r^{p,q}\) under compact modifications. Page dimensions, differential ranks and total-degree Frölicher defects are nondecreasing upstairs. No ascending-degeneration assertion.
- **POME-FUJIKI-ODD-BETTI-OBSTRUCTION-001 — low / verified conditional deduction:** all odd Betti numbers of Fujiki-class compact complex manifolds are even. The primary scalar Hopf surface \(S^3\times S^1\) has \(b_1=b_3=1\) and therefore no Kähler modification.
- **POME-COMPLEX-TORUS-FOURIER-DOLBEAULT-001 — low / verified conditional deduction:** §10.81.1's full real lattice quotient has \(h^{p,q}=\binom np\binom nq\) and \(b_k=\binom{2n}k\). An explicit order-\(-1\) Fourier contraction kills every nonzero frequency. Kähler strong Hodge gives identical Bott–Chern dimensions.
- **Actual new coverage:** first selected proof-level **§§10.81 and 10.87** only. §§10.84–86 previously audited and reused as dependencies, not counted again; 747 unique ToC rows, zero complete-section certifications. No printed theorem found false in this pass, no build/tests/CI/formal verification or site publication. Demailly approximation/regularization and its dedicated Bergman/L²/Ohsawa–Takegoshi/multiscale/positivity-loss work remain **deferred-by-user** and unopened.

---

# 2026-10-27 — Global Hermitian sublevel capacity and circle-supported max-Fubini–Study curvature

**Reviewed main:** b6933b772f41b45918f7e25ed1afbbb1fd892272; **starting review head:** ac620c1713fd3da8d846132b457cedd1221a6977. [Complete source-anchored English report](reports/2026-10-27-hermitian-global-sublevel-capacity-and-fs-circle-curvature.md).

- **POME-HERMITIAN-GLOBAL-SUBLEVEL-CAP-001 — low / verified conditional deduction:** on a fixed connected compact Hermitian manifold, normalized \(u\in\mathrm{PSH}(X,\omega)\) have \(c_\omega(\{u<-t\})\le C_{X,\omega}/t\) uniformly in \(u\) and \(t>0\), with globally sharp \(t^{-1}\) order on \(\mathbb P^1\), witnessed by the circle mass \((1-e^{-(t+1)})/(t+1)\) of a bounded \(\omega\)-psh test. This is not a duplicate of the prior *local* weighted-CLN capacity finding.
- **POME-FS-MAX-CIRCLE-CURVATURE-001 — low / verified conditional deduction:** \(\max(\log|X_0|^2,\log|X_1|^2)\) defines a pole-free continuous max-Fubini–Study metric on \(\mathcal O_{\mathbb P^1}(1)\) whose positive curvature is normalized arclength on \(|z|=1\), not a smooth density or a complex-analytic divisor.
- **Actual scope:** first selected proof-level checks in §§10.6 and 10.9 (two inventory rows upgraded). No original theorem found false, no whole section or upstream BT/CLN comparison certified. All 747 section rows and historical ledger statuses retained. No Demailly approximation/regularization or dedicated Bergman/L²/OT/multiscale/positivity-loss activity; all remain **deferred-by-user**. No source/main/registry/tag edit, build, tests, CI, formalization or publication.

---

# 2026-10-27 — Quantitative Hartogs–Bochner boundary extension, non-splitting jets, and polar affine reweighting

**Reviewed main:** b6933b772f41b45918f7e25ed1afbbb1fd892272; **starting review head:** b71610cf5edf7ad06ac8f1be1d9ad4d522247c18. [Full English report with main blobs, stable labels and physical lines](reports/2026-10-27-hartogs-bochner-log-modulus-and-jet-nonsplitting.md).

- **POME-CR-BOUNDARY-LOGMODULUS-001 — low / verified conditional deduction:** in §9.36.1, the existing compact-support Cauchy-type homotopy kernel and C² collar produce a C||f||C¹ * h(1+log(R/h)) modulus for the continuous holomorphic extension, hence all C^{0,alpha} exponents alpha<1; a constant-on-each-boundary-component annulus example proves the printed connected-boundary hypothesis cannot be deleted.
- **POME-JET-EXACT-NONSPLIT-001 — low / verified conditional deduction:** §10.93.3 yields 0 -> Sym^k Omega¹ tensor E -> J^k E -> J^{k−1}E -> 0; splitting at k=1 equals a holomorphic connection. On P¹, J¹O(1) = O², but 0 -> O(−1) -> O² -> O(1) -> 0 does not holomorphically split, despite very ampleness.
- **POME-POLAR-AFFINE-REWEIGHT-001 — low / verified conditional deduction:** §5.46.3 implies exact polar-curvature scaling 1_S dd^c(chi(u)) = c 1_S dd^c u for negative psh u and convex nondecreasing chi with chi(t)=ct+O(1) at −infinity, c>0. Ratio-only asymptotics are not claimed sufficient.
- **Actual coverage:** first **selected** §9.36.1, §10.93.1/.3–4 and §5.46.1–5 (three inventory rows upgraded); §5.49 homotopy reused, not counted as a newly audited section. **747 unique section entries retained, no whole section certified.** All printed theorems checked here remain correct; several upstream analytic prerequisites are conditional. No project build/tests, CI, formal verification, website publication, main/source/registry/tag change. Dedicated Demailly approximation/regularization, Bergman/L²/Ohsawa–Takegoshi/multiscale-atlas/positivity-loss completion remains **deferred-by-user**, untouched.

---

# 2026-10-27 — Finsler polar uniformity needs compactness; independently checked normal-current signs

**Reviewed main:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`; **starting review head:** \`bde22f904afce4cde92892d88ffb6a494d36d691\`. [Complete counterexample, local uniform repair, and pinned proof anchors](reports/2026-10-27-finsler-polar-global-margin-and-normal-current-support.md). 

- **POME-FINSLER-POLAR-GLOBAL-MARGIN-001 — medium / confirmed error under unqualified standalone hypotheses:** §11.12.3 claims one fiberwise convexity margin on arbitrary \(E\to X\); on noncompact \(\mathbf C\), \(G=e^{\operatorname{Re}z}|v|^2\) has zero Kobayashi curvature but \(Q=e^{-\operatorname{Re}z}|\xi|^2\), so no global \(c>0\). The **intended compact-base theorem is correct**. Verified repair: require compact \(X\), or state locally uniform \(c_U>0\) for each relatively compact \(U\Subset X\); only the local conclusion is needed as convexity input in §11.12.6. No related smoothing programme reopened.
- **New actual coverage:** selected proof checks in §§11.11–11.12 (tautological curvature, Finsler Schur formula and polar convexity) and §§5.55–5.56 (the \(C^1\) Stokes sign and normal-current conormal/support argument). **Four former inventory-only ToC rows upgraded**, 747 unique identifiers retained; no whole section certified. §11.3 context-only. No project tests/build/CI/formal verification, publication, or source/main edits. Dedicated Demailly psh approximation/regularization/Bergman/\(L^2\)/Ohsawa–Takegoshi/multiscale/positivity-loss remains **deferred-by-user**, untouched.

---

# 2026-10-27 — Sharp radial residual Sobolev threshold and quantitative equilibrium-mass stability

**Reviewed main:** b6933b772f41b45918f7e25ed1afbbb1fd892272; **starting audit head:** f06fc11b2c80c4ba71dc1ab7fcea90166e47b2d4. [Source-anchored complete conditional proofs and counterexamples](reports/2026-10-27-radial-residual-critical-sobolev-and-obstacle-mass-stability.md).

- **POME-RADIAL-RESIDUAL-CRITICAL-SOBOLEV-001 — low / verified conditional deduction:** for radial MA density relative error O(r^δ) near the prescribed pole in complex dimension k≥2, 0<δ<1, the residual has sharp W^{2,p} regularity **including** p=k/(1−δ), with log integrability at the endpoint; the printed normalized perturbation shows failure for every larger p. For 1/2<δ<1 its C^{1,2δ−1} regularity and sharpness also follow without density-derivative assumptions. Printed §§11.46.8/.17 remain correct.
- **POME-RADIAL-OBSTACLE-KOLMOGOROV-SHARPNESS-001 — low / verified conditional deduction:** fixed-support C²-bounded convex radial obstacles have equilibrium MA radial cumulative distributions differing by O(√||F−G||∞), and a smooth strictly convex localized bump proves the 1/2 exponent optimal. This is **not** total-variation stability. Printed §§11.47.5/.8/.11 remain correct.
- **New actual selected coverage:** §§11.46–11.47 (radial inverse, density zeros, sharp perturbations, convex obstacle, contact/mass and C^{1,1} control) and independently §9.49 (ambient ideal logarithm, Levi normal-block argument, q-convex subspace/neighborhood construction); exactly three prior inventory-only ToC rows upgraded, all 747 unique identifiers retained. §7.31.2–4 contextual non-regularization check only; §7.31.1 smoothing and all dedicated Demailly/Bergman/L²/OT/multiscale/positivity-loss work **deferred-by-user**, untouched. No full-section certification, confirmed false theorem, project build/test/CI/formalization or publication.

---

# 2026-10-27 — Finite closed maps do not preserve cohomological dimension; compact-submanifold obstruction makes strong n-convexity sharp

**Reviewed main:** b6933b772f41b45918f7e25ed1afbbb1fd892272; **starting audit head:** 9ff39885f090f324eed569465cb12e69198e417c. [Complete English proofs, source variants, exact files and permanent tags](reports/2026-10-27-finite-map-cohomological-dimension-and-sharp-q-convexity.md).

- **POME-FINITE-CLOSED-COHDIM-ASYMMETRY-001 — low / verified conditional deduction:** §10.61.3 proves cd(X)≤cd(Y) for a closed finite-fiber map from a Hausdorff X. The binary-digit map from the Cantor space C onto [0,1] is compact, closed, onto, at most two-to-one, yet cd(C)=0<1=cd([0,1]). If the map has a continuous section, equality does follow. Printed sheaf Leray, soft-resolution and metric-product results remain true.
- **POME-STRONG-Q-COMPACT-SUBMANIFOLD-OBSTRUCTION-001 — low / verified conditional deduction:** a compact complex q-submanifold forbids strong q-convexity near it by the Levi maximum principle and dimension count. The noncompact n-fold P^(n−1)×C (n≥2) is never strongly (n−1)-complete, while §9.52.8 supplies a smooth strongly n-convex exhaustion; the universal threshold is sharp. Printed q-completeness criteria remain correct.
- **New exact coverage:** selected proof-level §§9.52, 10.61, 10.62 (3 previously inventory-only entries); 747 unique original ToC rows retained, zero full-section certifications. No new confirmed false mathematical theorem or resolved old finding, and no builds/CI/formal verification/published website. Dedicated Demailly approximation/regularization and Bergman/L²/OT/multiscale/positivity-loss remain **deferred-by-user** and untouched.

---

# 2026-10-27 — Compact ∂̄-primitive hole support and six genus-two Weierstrass branch points

**Reviewed main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. [Full exact-source-anchored English report](reports/2026-10-27-compact-dbar-hole-support-and-genus-two-weierstrass-branching.md).

- **POME-DBAR-PRIMITIVE-HOLE-SUPPORT-001 — low / verified conditional deduction:** §5.49.1/.4, the canonical compact-support homotopy solution vanishes on the unbounded complementary component of the support of its closed (p,1) input. If the complement is connected, the primitive has support inside the input support; a radial cutoff on an annulus proves the bounded-hole obstruction is sharp. Printed Hartogs and compact-support theorems are correct.
- **POME-GENUS2-WEIERSTRASS-BRANCH-001 — low / verified conditional deduction:** §10.78.14/.16/.17 and §10.79.13 simple-pole criterion imply exactly six distinct weight-one Weierstrass points in genus 2; a degree-two function centered at any one is simply ramified at exactly these six. The printed Wronskian and Riemann–Hurwitz results remain correct.
- **POME-POINT-SHEAF-FINITE-CECH-ACYC-001 — low / verified conditional deduction:** §10.78.4's index-selection contracting homotopy applies to all positive Čech degrees on any finite open cover. No unverified higher-degree Čech/derived comparison is asserted.
- **Coverage:** previously inventory-only §§5.49, 10.78, 10.79 upgraded at precisely recorded passages; 747 original section keys retained, zero whole sections certified. No new confirmed mathematical error. Dedicated Demailly approximation/regularization and Bergman/L²/OT/multiscale/positivity-loss **deferred-by-user** and untouched. No tests/build/CI/formalization/published docs/main/registry/permanent-tag mutations.

---

# 2026-10-27 — Quantitative calibration defect and fourth-order Kähler potential jet

**Reviewed main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`; **starting review head:** `a619aa2756a221271ac24b1bf166d7e898532a87`. [Full precise English proof and anchors](reports/2026-10-27-calibration-defect-and-kahler-quartic-potential-jet.md).

- **POME-CALIBRATION-ANGLE-DEFECT-001 — low / verified conditional deduction:** §10.89.2–3 gives the exact volume deficit Vol(Y)−Vol(Z)=∫_Y(1−c(TY)), bounding the integral of squared normal components of J on TY with sharp universal coefficient 1/4 (p=1) or 1/(2p) (p≥2). Equality forces complex-oriented Y; the original calibrated volume inequality remains correct.
- **POME-KAHLER-QUARTIC-POTENTIAL-001 — low / verified conditional deduction:** §10.94.2 and curvature equation 10.94.3 give the explicit potential jet Φ=|z|²−(1/4)ΣC_(j bar k l bar m) z_j z_l bar z_k bar z_m+O(|z|⁵), modulo pluriharmonic gauge, with the exact unscaled Chern convention. A CP¹ Fubini–Study and symbolic derivative check confirm its sign and factor; no error in the printed theorem.
- **Coverage:** newly selected nonexcluded §§10.89 and 10.94 at pinned passages only; 747 unique ToC rows preserved and zero whole sections certified. No existing statuses changed. Demailly approximation/regularization and the dedicated Bergman/L²/Ohsawa–Takegoshi/multiscale/positivity-loss programme remain **deferred-by-user**. No build, CI, formal verification, website publication, main/source/registry/permanent-tag change.

---

# 2026-10-27 — Landau midpoint defect, quantitative magnetic Dirichlet Riesz rate, and nuclear Banach rigidity

**Reviewed main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`; **starting review head:** `1e130a81f5b539996317119059f22ff7839815c6`. [Exact-source anchored complete proofs](reports/2026-10-27-magnetic-riesz-rates-and-nuclear-banach-rigidity.md).

- **POME-LANDAU-RIESZ-MIDPOINT-001 — low / verified conditional deduction:** in one magnetic pair, writing x=E/(2b) and N=max(0,ceil(x−1/2)), exact identity r₀(E)−r_b(E)=b²(N−x)²/(2π), hence sharp global error ≤b²/(8π) and counting error ≤b/(4π), both attained at odd Landau thresholds.
- **POME-MAGNETIC-DIRICHLET-RATE-001 — low / verified conditional deduction:** the existing exact variational bound (2.24.10) with a *fixed-width* rather than sqrt(R)-width boundary cutoff yields uniform finite-volume Dirichlet Riesz error O((E_*^n+E_*^{n+1})/R), all b_j≥0 and bounded shapes. Printed o(1) statement remains true.
- **POME-NUCLEAR-BANACH-FINITE-DIM-001 — low / verified conditional deduction:** a Banach space is nuclear as a Fréchet space iff finite-dimensional; compact nuclear canonical link forces compact identity, then elementary Riesz-lemma separation. The original nuclear-space theorems remain correct as read.
- **New actual coverage:** selected proof-level §§2.24.2/.6/.8 and §§2.13.1–3, **two inventory-only rows upgraded**; exactly 747 section rows retained, none fully certified. No project tests/build/CI or website publish. Dedicated Demailly approximation/regularization and its Bergman/L²/OT/multiscale/positivity-loss programme remain **deferred-by-user**; no part reexamined.

---

# 2026-10-27 — vanishing-density third-derivative jumps and dimension-sharp discontinuous constant-MA models

**Reviewed main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`; **review branch starting head:** `73a3e3e094c607129b9d4d2329c9c6de99b13034`. [Full English proofs with physical anchors, blobs and permanent tags](reports/2026-10-27-vanishing-density-sobolev-jumps-and-higher-dimensional-constant-ma-discontinuities.md).

- **POME-DEGENERATE-MA-THIRD-SOBOLEV-JUMP-001 — low / verified conditional deduction:** §15.20.8's symmetric projective positive-exponent solutions and selected limit are locally W^{2,∞} on the vanishing-density band but fail W^{3,1} across each transition hypersurface; the third transverse derivative contains a nonzero surface Dirac term of exact coefficient J=z₀(t*)−p′(t*)>0. The printed C^{1,1} but non-C² theorem is correct; model construction and radial flux remain conditional inputs.
- **POME-CONSTANT-MA-DISCONTINUITY-DIMENSION-001 — low / verified conditional deduction:** §15.21.8's two-dimensional constant-MA potential has **exact** discontinuity locus {(0,w):w≠0}, not the entire polar set. Cartesian products lift its constant-density local counterexample and §15.21.12's compact flat-torus gluing to every complex dimension ≥2, retaining boundedness, minimal singularities and failure of every L^p (p>1); dimension one is excluded by the linear distributional Poisson equation. No printed theorem refuted and no additional global smooth-density regularity asserted.
- **Actual newly selected proof-level coverage:** §§15.20.1/.4/.5/.8 and 15.21.2/.8/.12/.15 with exact passages in the report; two inventory-only ToC rows upgraded. **747 unique current section rows retained, no whole section certified**. Prior findings preserved.
- **Scope:** dedicated Demailly approximation/regularization and Bergman/L²/Ohsawa–Takegoshi/multiscale-atlas/positivity-loss completion remain **deferred-by-user**, never reopened. Only review-branch audit Markdown, no math body/registry/source/permanent-tag/main/CI/build/formal proof/website updates.

---

# 2026-10-27 — projective twisted Euler polynomial and doubled-hyperplane automorphisms

**Reviewed main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`; **starting audit head:** `e506fcdabac003a47bb5e3040f3989d9c03dcdf7`. [Full English proof report with exact blobs, source labels and physical anchors](reports/2026-10-27-projective-twisted-euler-and-double-hyperplane-automorphisms.md).

- **POME-PN-TWISTED-EULER-POLYNOMIAL-001 — low / verified conditional deduction:** Bott's §10.51.6 cohomology regimes give, for all integer k and 0≤p≤n (including n=0), χ(P^n,Ω^p(k))=binom(k−1,p)binom(k+n−p,n−p) with polynomial binomial convention. Complete case and Serre symmetry proofs; independently checked 1044 small integer tuples. The printed Bott theorem remains correct; Hodge/Nakano/Serre prerequisites are conditional.
- **POME-DOUBLE-HYPERPLANE-AUTOMORPHISMS-001 — low / verified conditional deduction:** a doubled-hyperplane self-map (f,a,c) is invertible exactly when its reduced map f is biholomorphic and its nilpotent normal multiplier c never vanishes; explicit inverse and composition law. §9.60.1's older analytic-coherence external dependency remains open; no theorem falsity or certification claimed.
- **Actual coverage:** new selected proof-level §§10.50.1–3 and 10.51.1–6; incremental §§9.58.2–3, 9.60.1. Exactly two previously inventory-only ToC rows upgraded, **747 distinct rows retained**, none entirely certified. Existing §9.60 external dependency and all other historical statuses preserved.
- **Scope:** dedicated Demailly approximation/regularization, Bergman/L²/Ohsawa–Takegoshi/multiscale-atlas/positivity-loss programme **deferred-by-user**, untouched. Only audit Markdown; no source/main/body/registry/tags, CI, build, formal proof or publication.

---
# 2026-10-27 — sharp PSH sublevel capacity and exact Gauduchon Jensen deficit

**Reviewed main:** b6933b772f41b45918f7e25ed1afbbb1fd892272; **starting audit head:** 5db8b393779ea541959178060daba9668e14f1e0. [Full source-anchored English proof report](reports/2026-10-27-sharp-psh-sublevel-capacity-and-gauduchon-jensen-defect.md).

- **POME-BT-PSH-SUBLEVEL-CAP-RATE-001 — low / verified conditional deduction:** §7.4.1 weighted CLN gives Cap_D(K∩{V<−t})≤C||V||_{L¹(L)}/t uniformly over bounded BT competitors. The exact disk model V=log|z| proves optimal t^(−1) order: for t>log 2, 1/[2(t+1)]≤Cap_Δ(Δ_{e^(−t)}). Correctly handles the *strict* sublevel by placing the test mass on a smaller circle. Printed estimates remain correct.
- **POME-GAUD-JENSEN-DEFECT-001 — low / verified conditional deduction:** §12.4.1 second variation yields the exact integral affine-chord deficit of the Gauduchon root λ along any segment of positive backgrounds, with Green kernel min(t,s)−ts and squared traceless linearized form. Equality recovers existing §12.3.1 rigidity. This adds a quantitative identity, not a global uniform strict-concavity modulus.
- **New actual selected proof-level coverage:** §18.1.2 **only** implication (2)↔(3) and §18.1.17/.19 finite maxima/Choquet nonempty-family passage, without touching excluded quasi-equisingular analytic-approximation proofs; §18.1 advances from inventory to selected. Incremental §§7.2–7.4 and 12.2–12.5 previously already selected; §§7.1,12.1,18.2–18.3 contextual introduction only. 747 unique ToC rows preserved, no full section certified, no confirmed false theorem.
- **Scope boundary:** Dedicated Demailly approximation/regularization/Bergman/L²/Ohsawa–Takegoshi/multiscale-atlas/positivity-loss programme remains **deferred-by-user** and untouched. No main/source/registry/permanent-tag changes, build, tests, CI, formal proof or publication.

---

# 2026-10-26 — countable-divisor valuation tails and convex-body lattice discrepancy

**Reviewed main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`; **starting audit head:** `1904c6a0c5c91594db14fb6c197ad48f51443640`. [Full report with fixed physical anchors](reports/2026-10-26-divisorial-tail-nonuniformity-and-convex-lattice-rate.md).

- **POME-COUNTABLE-DIV-TAIL-NONUNIFORM-001 — low / verified conditional deduction:** In the §13.24.7 projective-plane countably many lines model, the order tail after *every fixed N* has unbounded supremum over all smooth modifications and prime divisors: infinitely-near exceptional divisors above a point of one tail line have order `r a_j`. This does not refute the printed pointwise convergence or its fixed-(π,E) trace bound; no uniform bound is available.
- **POME-CONVEX-ALLBODIES-LATTICE-RATE-001 — low / verified conditional deduction:** The convex-body counting clause in §19.7.20 has an elementary quantitative `O_K(1/k)` inradius-bound valid for every full-dimensional compact convex body, with matching cube lower-order example; **not** a replacement for the general KK12 almost-semigroup theorem. Existing semigroup-count and slice-proof findings were checked for duplication and retained unchanged.
- **Actual new scope:** §13.24.6–10 selected nonexcluded proof-level; §14.20.1 formula/normalization-only; incremental §19.7 convex-body counting. **Two** previous inventory-only ToC rows upgraded (one only formula-level), all 747 distinct rows retained. No full section certified and no new false printed theorem.
- **Scope:** §13.24.1–5 analytic approximation proof and dedicated Demailly approximation/regularization/Bergman/L²/Ohsawa–Takegoshi/multiscale/positivity-loss programme **deferred-by-user**, not reopened, resolved or certified. No main/source/registry/tag changes, tests/build/CI, or publication.

---

# 2026-10-26 — canonical PSH representative bridge and compact scalar Hermitian rigidity

**Reviewed main:** b6933b772f41b45918f7e25ed1afbbb1fd892272; **starting audit head:** ae3e637b72cd32c394b906f6677b88a152b9b36e. [Source-anchored detailed proof](reports/2026-10-26-psh-representative-internal-bridge-and-hermitian-scalar-rigidity.md).

- **POME-QPSH-DISTRIBUTIONAL-INTERNAL-BRIDGE-001 — low / verified repair:** §5.22.2 cites external DemCADG for the canonical distributional PSH representative, but the complete identical local input is **already proved** in §5.9.1 (tag 2A4F77263F48). Exact local quadratic-correction and overlap-gluing replacement given. Keep historical attribution; do not merge distinct relative/global and flat/local statements.
- **POME-HERM-SCALAR-COMPACT-RIGIDITY-001 — low / verified conditional deduction:** on compact connected complex X of dimension n≥2, all real distributional pairs satisfying fixed θ+ddᶜu=aγ, γ Hermitian, have identical scalar a and differ in u only by a constant. The difference b solves db=−bCγ, hence has fixed strict sign unless zero, contradicted by extrema of the potential difference. Dimension one and noncompact sharp counterexamples included.
- **Actual new selected proof-level:** §§5.22–5.24 (relative representatives, background changes, maximal/gluing/extension principles); §5.9.1 directly consulted as internal source. **Three inventory-only ToC rows upgraded; 747 unique rows retained**. No complete-section/earlier-PDE certification, no printed theorem refuted.
- **Scope:** dedicated Demailly approximation/regularization/Bergman/L²/Ohsawa–Takegoshi/multiscale-atlas/positivity-loss activity remains **deferred-by-user** and untouched. Only audit Markdown; no tests, build, CI, formal verification, publication or main/source/registry/permanent-tag edits.

---

# 2026-10-26 — local essential floors for smooth tests; explicit logarithmic-obstacle cutoff

**Reviewed main:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`; **starting audit head:** \`f3f9ec6a391336765c096b0a5c029b7b48762fdd\`. [Source-anchored proofs and complete hypotheses](reports/2026-10-26-individual-density-smooth-tests-and-log-pole-obstacle-cutoff.md).

- **POME-SMOOTH-TEST-LOCAL-FLOOR-001 — low / verified conditional deduction:** For any probability density \(f\in L^1\), bounded below by \(c>0\) and with local essential infimum \(c\) on every nonempty open set, the §15.28.8 smooth comparison threshold is exactly \(C_h^{\mathrm{sm}}(f)=c_h(1)/c\), *without requiring zero lower mass*. The existing §15.28.9 nonattainment example is a special case; its separation \(b_h(f)=0<C_h^{\mathrm{sm}}(f)\) remains valid. Scalar order/homogeneity inputs conditional.
- **POME-OBSTACLE-SCALAR-CUTOFF-001 — low / verified repair:** §16.44.1's implicit truncation of a logarithmic-pole obstacle admits an explicit smooth one-variable convex cutoff \(F_R\), with \(\psi\le F_R(\psi)\le\max(\psi,-R)\), unchanged curvature lower bound, *identical envelope* and *identical obstacle infimum*. This supplies the missing displayed computation, without reopening the excluded Demailly programme. Upstream §16.15.7 penalized existence and convergence remain conditional.
- **Actual newly inspected:** integrated §15.28 (threshold closure, maximal subsolutions, smooth-test construction) and entire single-lemma §16.44; supporting §§15.1, 15.27.1, 16.15.7 consulted only. Two previously inventory-only ToC rows upgraded; **747 unique rows retained**, no entire section certified and no false printed theorem reported.
- **Scope:** Demailly approximation/regularization and dedicated Bergman/\(L^2\)/Ohsawa–Takegoshi/multiscale/positivity-loss programme remain **deferred-by-user** and untouched. Only audit Markdown on the review branch. No tests, build, CI, formal proof, publication, source/main/registry/tag edits.

---

# 2026-10-26 — finite polynomial equilibrium transport and gauge-independent PSH boundary distances

**Reviewed main:** b6933b772f41b45918f7e25ed1afbbb1fd892272; **starting audit head:** fb3f1a07c6791d6b269e32527f17fa490a82412a. [Complete source-anchored English report](reports/2026-10-26-proper-polynomial-equilibrium-transport-and-gauge-independent-boundary-psh.md).

- **POME-PROPER-POLY-EQUILIBRIUM-PUSH-001 — low / verified conditional deduction.** Newly selected §16.32: under the regular leading homogeneous degree-d hypothesis, the starred extremal identity is exact, push-forward of the non-pluripolar compact/bounded-set equilibrium Monge–Ampère measure is exactly preserved, and L-regularity is equivalent at all points of inverse fibers, including ramification. Generic degree d^n is justified by projective homogenization. BT local covariance and pluripolar-zero properties remain explicit conditional inputs. No original theorem refuted.
- **POME-BOUNDARY-GAUGE-BOUNDED-PSH-001 — low / verified conditional deduction.** Newly selected §9.14: any two continuous positive complex-homogeneous boundary gauges on a nonempty proper pseudoconvex domain give negative-log boundary-distance PSH functions and explicit PSH exhaustions differing by globally bounded terms; no convexity/triangle inequality, and no comparison of Levi forms claimed. Full Oka upstream not certified.
- **Coverage:** first selected proof-level §§16.32, 9.14; §9.13.2 definition/context only. The prior POME-HULL-JET-INTERP-001 was found in the ledger and **not repeated**. Exactly 747 current ToC section rows remain; none fully certified. No confirmed new error, no former issue closed.
- **Scope:** Demailly approximation/regularization and dedicated Bergman/L²/Ohsawa–Takegoshi/multiscale-atlas/positivity-loss programme remain **deferred-by-user** without inspection. Only audit Markdown; main, source bodies, registry and tags untouched. No build, CI, formal proof, publishing or project tests.

---

# 2026-10-26 — supporting probability stability and first variation of logarithmic product selection

**Reviewed main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`; **starting audit head:** `336e7987e04aacf0e430e060d50a641e7e20255f`. [Source-anchored English proofs](reports/2026-10-26-critical-support-semicontinuity-and-logarithmic-linear-response.md).

- **POME-CRITICAL-SUPPORT-UHC-001 — low / verified conditional deduction.** First selected proof-level inspection §11.44, Proposition 11.44.5 (tag `91FDE4AB5C22`) and Proposition 11.44.9 (tag `AD91D203DE64`), main file `docs/sections/normalization-and-weak-adjoint-measures--selection-by-a-vanishing-exponential-parameter/index.html` blob `aaa0a6363ade7e865aeea7ab43b7770748fedbaa`, lines 49–170: supporting probabilities are uniformly L^r absolutely continuous for fixed L^p density, and their graph is closed under L^q density convergence and weak probability convergence, 1<q<p, with an explicit quantitative bound for the convex support function. This does **not** assert lower hemicontinuity.
- **POME-LOGMODEL-FIRST-ORDER-001 — low / verified conditional deduction.** First selected proof-level inspection §11.45, Theorem 11.45.9 (tag `72A7418012F7`), main file `docs/sections/normalization-and-weak-adjoint-measures--selection-for-logarithmic-models-on-products/index.html` blob `f0b92ec93b3184a6af1c804b07bd3454b957d6bc`, lines 108–218: for fixed logarithmic product data, the Green residual has explicit first variation `w_1=G*[A_0(ψ+w_0−J)]` and O(σ²) uniform remainder; the centered scalar has the corresponding second-order expansion. It is not claimed for arbitrary varying data.
- **Coverage:** §§11.44–11.45 newly upgraded from inventory to **selected proof-level**, with limited passages and conditional dependencies; 747 distinct actual-ToC rows preserved, **no whole section certified**. Neither result asserts a false printed theorem, nor resolves unrelated earlier audit findings.
- **Scope and writes:** Author-excluded Demailly approximation/regularization and dedicated Bergman/L²/Ohsawa–Takegoshi/multiscale/positivity-loss proofs remain **deferred-by-user**, not resolved. Only audit Markdown updated on `review/mathematical-audit`; `main`, mathematical body, registry and permanent tags untouched. No tests, build, formal proof, CI or website publication performed.

---

# 2026-10-26 — arithmetic interpolation bases and the weak/TV boundary of dominated Monge–Ampère limits

**Reviewed main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`; **starting audit head:** `4a799ff13c278b916617194425d86996aa9cf47c`; **UTC checkpoint:** 2026-10-26T10:57Z. [Exact integrated statement/proof anchors and complete English arguments](reports/2026-10-26-arithmetic-evaluation-bases-and-dominated-ma-tv-obstruction.md).

- **POME-ARITH-EVAL-BASIS-ORDERS-001 — low / verified conditional deduction:** §9.55.1/.8's degree-`\delta` polynomial interpolation yields the stronger growth coefficient `\delta^{1-n}\max_B\sum_{w\in B}\operatorname{ord}_w f`, maximizing over independent evaluation bases `B` of `\mathbb C[z]_{<\delta}`. This strictly improves the printed minimum-order coefficient and is exactly sharp for `S=\{(0,0),(1,0),(0,1)\}, f=xy`. The original growth theorem and corollary remain correct.
- **POME-MA-DOMINATED-WEAK-NOT-TV-001 — low / verified conditional deduction:** §15.37.19 cannot be strengthened to total-variation convergence: smooth `\omega`-psh cosine potentials on a flat complex torus converge to zero in `C^1`, and their Monge–Ampère densities are uniformly bounded above/below by positive constants and dominated by one fixed smooth non-pluripolar measure, but their TV distance to the limit is exactly `(2a/\pi)\int\omega^n` for every index. The printed *weak*-convergence theorem remains correct.
- **Actual newly selected coverage:** §§9.55.1/.8/.11 and §§15.37.13/.17/.19 plus standing setup; no entire section or all prerequisites certified. Exactly 747 section rows retained. The dedicated Demailly approximation/regularization/Bergman/`L²`/Ohsawa–Takegoshi/multiscale/positivity-loss programme remains **deferred-by-user** (not inspected/resolved/certified); §9.55.12 onward explicitly skipped. No project build, CI, publishing or source/main/registry/tag changes.

---

# 2026-10-26 — integral finite-coefficient UCT and four-term Bott–Chern/Aeppli exactness

**Reviewed main:** b6933b772f41b45918f7e25ed1afbbb1fd892272; **starting audit head:** 46967f87c66ee4279ca09f6e82ee8a7265ebe8ed; **UTC:** 2026-10-26T10:02:42.102Z. [Complete English proof report, precise integrated main SHA/blob/labels/lines](reports/2026-10-26-integral-coefficient-uct-and-bott-chern-aeppli-four-term-exactness.md).

- **POME-COEFF-UCT-FINITE-GOOD-COVER-001 — low / verified conditional deduction:** Theorem 10.64.1's finite free integer cochain model gives the natural short exact universal coefficient sequence, with Tor(H^{q+1}(M,Z),A) and an abstract but noncanonical splitting for every abelian coefficient A. The 2-term multiplication-by-2 test shows why Theorem 10.64.3's rational/real comparison must not be extrapolated to finite coefficients. The printed theorems are correct.
- **POME-BC-AEPPLI-FOUR-TERM-001 — low / verified conditional deduction:** §§10.85–10.86 yield exactness of H_{bar∂}^{p,q} → H_A^{p,q} → H_BC^{p,q+1} → H_{bar∂}^{p,q+1} at both middle terms, for all complex manifolds; only the first three arrows' exactness was already printed. The additional BC-kernel step is proved from definitions, with compact dimension consequences and current compatibility; no Kähler, L², or regularization input.
- **Actual first selected theorem/proof-level coverage:** §§10.63, 10.64, 10.84, 10.85, 10.86, exact sources in report. All **747 section inventory rows** retained, none certified as an entire section; nonexamined §10.43/44/54/55 prerequisites remain conditional. No new confirmed error; no prior ledger item resolved. Dedicated Demailly approximation/regularization, Bergman, L², Ohsawa–Takegoshi, multiscale and positivity-loss programme remains **deferred-by-user**; not inspected. No build, CI, formal verification, publication, main/source/body/registry/permanent-tag changes.

---

# 2026-10-26 — Kähler envelope Hessian hypotheses and bounded complex-trace regularity limits

**Reviewed main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`; [precise integrated proofs, examples and status boundaries](reports/2026-10-26-kahler-envelope-one-sided-hessian-and-bounded-trace-limits.md).

- **POME-ENVELOPE-SOFTMIN-ONESIDED-SHARP-001 — low / verified conditional deduction:** two fixed smooth obstacles \(\pm\varphi\) on \(\mathbb P^1\) have smooth soft minima with uniform values/gradients and **upper** real Hessian, but real-Hessian lower bound of order \(-1/\delta\) at their crossing. Exact negative-variance calculation validates the one-sided input in Lemma 16.16.1 and Theorem 16.16.7; original printed results are **not false**.
- **POME-TRACE-COMPLEX-HESSIAN-NOT-C11-001 — low / verified conditional deduction:** the explicit subharmonic \(2|z|^2+\operatorname{Re}(z^2)\log|z|\) has \(1\le u_{z\bar z}\le3\) almost everywhere but unbounded real Hessian. This checks the *logical limit* of §16.19.1's final bounded-complex-Hessian-to-\(C^{1,\gamma}\) reasoning, **not** a counterexample to the envelope theorem.
- **Actual selected first proof review:** §16.16 Lemma .1 and Theorem .7; §16.19 Theorem .1 (specific normal-coordinate, soft-min variance, moving-radius algebra, Laplacian-to-Sobolev passages). The §6.17.1 gentle-analytic-singularity regularization dependency is expressly **deferred-by-user**, not reopened or certified. All 747 ToC rows retained; no whole section certified. No build, CI, formalization, site publishing, or main/source/registry/permanent-tag edits.

---

# 2026-10-26 — Ricci-flat RC-curvature spectral margin; quantitative HSC/Ricci pinching

**Reviewed main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`; **starting audit head:** `62d2b5e0bb67c2f50fe96d46407d3e434820e474`. [English source-anchored report and proofs](reports/2026-10-26-rc-curvature-spectral-gap-and-quantitative-hsc-ricci-pinching.md).

- **POME-RC-CURVATURE-SPECTRAL-GAP-001 — low / verified conditional deduction:** on a Ricci-flat Kähler surface, the infimum of the largest directional Chern-curvature eigenvalue, normalized by fiber norm squared, equals precisely half the minimum singular value of the anti-self-dual curvature operator. Direct norm calculation from the integrated Hodge projection in §11.27.1, not the stronger fixed-direction “uniform RC” condition. Printed result correct; Lemma 11.27.2's long Bochner identity not independently certified.
- **POME-HSC-RICCI-QUANT-PINCH-001 — low / verified conditional deduction:** if compact Kähler `g` has `Ric(g)≥−Λω_g` and tangent Hermitian `h` has Chern `H_h≤−κ`, then `∫|S|² +(κ/2)∫[(tr_g h)²+tr((g^{-1}h)²)] ≤ Λ∫tr_g h`. Under `h≥cg`, this gives `κc≤2Λ/(n+1)`, with strict positive equality only if `h=cg` and `g` is a negative constant-holomorphic-sectional-curvature Kähler metric. Uses the exact Gaussian factor in Lemma 11.28.2 and global torsion identity in Proposition 11.28.3 as conditional inputs, not a new assertion of their full independent proof.
- **Actual first selected theorem/proof-level coverage:** §§11.27 and 11.28, with §11.26.2–3 as contextual support. Existing flat-torus integral averaging finding `POME-HERM-TORUS-AVG-001` retained unchanged. 747 unique section inventory rows preserved, no chapter/section certified wholesale. The dedicated Demailly approximation/regularization/Bergman/`L²`/OT/multiscale/positivity-loss programme remains **deferred-by-user**, entirely unexamined. No main/source/registry/tag edits, build, CI, site publishing or formalization.

---

# 2026-10-26 — quotient Griffiths curvature, flat ambiguity of integral Chern curvature, and Levi sign

**Reviewed main:** b6933b772f41b45918f7e25ed1afbbb1fd892272. [Detailed source-anchored report](reports/2026-10-26-griffiths-quotient-curvature-and-flat-curvature-fibers.md).

- **POME-TAUT-GRIFFITHS-POSITIVITY-001 — low / verified conditional deduction:** for a fixed smooth Hermitian E, the induced quotient metric on O_E(1) over P(E*) is (strictly) Chern-positive iff E is (strictly) Griffiths-positive. Direct exact Chern-normal horizontal/vertical proof in §10.37.3, valid also at rank one. Printed proposition correct.
- **POME-INTEGRAL-CURVATURE-UNITARY-FLAT-TORSOR-001 — low / verified conditional deduction:** given an integral smooth real closed (1,1) curvature form ω, metrized holomorphic lines realizing ω, modulo unitary holomorphic isometry, form an H1(X,U(1)_loc.const) torsor. Explicit C* flat metric example distinguishes isometry classes modulo integers; Theorems 10.40.2/.5/.6 correct, upstream classification conditional.
- First selected proof-level §§9.34, 10.37, 10.40, including an independent **correct** Levi-bracket factor-four/sign check, selected boundary-normal-form and integral Chern sign checks. No entire section or underlying Oka/Hodge/projective prerequisites certified. Exactly 747 ToC matrix rows preserved. Demailly approximation/regularization and its dedicated Bergman/L2/OT/multiscale/positivity-loss programme **deferred-by-user**, untouched. No build, CI, formal verification, publication, main/source/registry/tag changes.

---

# 2026-10-26 — maximal exponential solutions: log-density comparison; ambient GH convergence under nets

**Reviewed main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`; [source-anchored complete proof](reports/2026-10-26-maximal-exponential-density-ratios-and-ambient-gh-nets.md).

- **POME-EXP-GREATEST-LOGRATIO-001 — low / verified conditional deduction:** For comparable nonzero integrable densities \(af\leq g\leq bf\), greatest exponential solutions satisfy \(u_f-\log b/\lambda\leq u_g\leq u_f-\log a/\lambda\); normalized solutions differ by at most \(\log(b/a)/\lambda\) on their common finite locus. Scaling \(g=tf\) leaves the normalized solution and its Monge–Ampère measure **exactly** unchanged. Printed Theorem 15.35.2 is correct; no new \(L^p\) premise.
- **POME-GH-AMBIENT-NET-COLLAPSE-001 — low / verified conditional deduction:** §15.19.22's uniform distance/GH collapse works for an arbitrary **directed net** and with vanishing **ambient** (rather than intrinsic) neighborhood diameters. Direct complete core-excursion proof; §15.19.26's intrinsic sufficient bound remains valid.
- **First selected proof-level §§15.19, 15.35, 15.36** only; original 747-row coverage matrix preserved, no full section certified. Previously recorded radial moment and product scalar findings not re-counted. All author-excluded Demailly approximation/regularization/Bergman/L²/OT/multiscale/positivity-loss work remains **deferred-by-user**. No source, main, registry, tag changes, project tests, builds, CI, formal verification or publishing.

---

# 2026-10-26 — plurifine continuity proof-step counterexample and compact psh-metric rigidity

**Reviewed main:** b6933b772f41b45918f7e25ed1afbbb1fd892272; **starting audit head:** fa67cc496e98284a33f33b40027cc40aa4455255. [Complete English source-anchored report and proof](reports/2026-10-26-plurifine-qpsh-proof-step-and-curvature-metric-rigidity.md).

- **POME-PLURIFINE-QPSH-OPEN-STEP-001 — low-to-medium / confirmed error in proof step; verified repair proposed, not integrated:** Proposition 5.15.18 remains **true**, but its proof at integrated line 343 falsely assumes the quasi-psh interval-level set is Euclidean-open near each point. The psh series with logarithmic poles accumulating at a finite-potential point disproves that step. A complete local plurifine-neighborhood argument, or simply continuity of psh weights plus smooth corrections in the defining topology, fixes the proof without external input. The downstream fine-open comparison and quasi-extrema corollaries are not disproved.
- **POME-PSH-METRIC-CURVATURE-RIGIDITY-001 — low / verified conditional deduction:** on a compact connected Kähler manifold, two psh metrics on one holomorphic line bundle have identical Chern currents iff their fiber metrics differ by one global positive constant. The singular-fiber equality follows from canonical psh representatives; noncompact pluriharmonic rescaling shows compactness sharp for a constant ratio. The main sources are §§5.19–5.20, and local Weyl/current results remain conditional inputs.
- **Actual newly selected:** §§5.15, 5.19 and the **nonexcluded part** of §5.20, with exact statement/proof tags and line anchors in the report. The 747-entry ToC coverage matrix remains unique; no complete section or transitive prerequisite chain certified. **§5.20.16–17 and the entire dedicated Demailly approximation/regularization/Bergman/L²/Ohsawa–Takegoshi/multiscale/positivity-loss programme were skipped**, remaining **deferred-by-user**. No main/source/registry/tag modifications, tests, builds, CI, formalization or publication.

---

# 2026-10-26 — self-contained Choquet selection and trace-zero closed-current rigidity

**Reviewed main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`; **starting audit head:** `b52b5ca74b1ce183425b1ec29dbb900af3ba56e7`. [Detailed source-anchored proofs, statuses and limitations](reports/2026-10-26-choquet-countable-basis-and-equal-trace-current-rigidity.md).

- **POME-CHOQUET-TOPOLOGICAL-REPAIR-001 — low / verified repair (proposed, not integrated):** Proposition 5.14.3's currently external Choquet selection step [GZ17, Lemma 4.31] has a complete internal replacement: on any second-countable space, rational-threshold witnesses on a countable basis produce a countable subfamily with the **same upper-semicontinuous regularized supremum**. This uses no analytic approximation theorem, works for extended-real functions, and yields the printed psh proposition. An uncountable disjoint union of discs with component-indicator pluriharmonic functions proves the countability hypothesis cannot be dropped uniformly. The printed theorem is **correct**; the report proposes, but does not apply, a self-contained proof.
- **POME-TRACE-POTENTIAL-RIGIDITY-001 — low / verified conditional deduction:** for a **fixed Euclidean holomorphic chart**, every real d-closed (1,1)-current with vanishing flat trace is smooth and locally the `dd^c` of a **real harmonic** function. Thus equal-trace positive closed currents have canonical psh potentials differing pointwise by a smooth harmonic function, and identical local singularity invariants. This uses §5.4's closedness trace identity, the internal Weyl lemma and smooth local exactness. A strictly-positive off-diagonal Hessian example shows trace equality does not imply equality of currents in dimension at least two; equality holds in dimension one. No extension to traces in unrelated Hermitian metrics.
- **Actual newly selected integrated-source checks:** §§5.3.7, 5.4.1–3, 5.13.9/.17, 5.14.2/.3, 16.40.1/.2; §5.2.3 convention separately shows submanifolds **are defined closed** in this collection, avoiding a false error report about §5.3.9. The real-analytic principalization input in §16.40 is explicitly permitted but remains external. Exactly **five** previously inventory-only section rows upgraded to selected proof-level or prerequisite checks; **all 747 ToC section rows unique, none wholly certified**. No tests/builds, CI, formal verification, publishing or main/source/body/registry/permanent-tag edits. The entire author-excluded Demailly approximation/regularization and dedicated Bergman/L²/Ohsawa–Takegoshi/multiscale/positivity-loss programme remains **deferred-by-user**, not reopened, resolved or certified.

---

# 2026-10-26 — exact elliptic prolongation degeneracy and smooth-parameter normalization

**Reviewed main:** b6933b772f41b45918f7e25ed1afbbb1fd892272. [Detailed English proofs, precise source anchors and conditional boundaries](reports/2026-10-26-elliptic-prolongation-sharp-symbol-and-smooth-normalization-basechange.md).

- **POME-ELLIPTIC-PROLONG-EXACT-DEGEN-001 — low / verified conditional deduction:** for the rank-three prolonged second-order operator of Proposition 2.20.11, the principal symbol is invertible **exactly when t²≠2**. The two singular t-levels and offending real covector slopes are computed explicitly; the printed |t|<1 restriction remains correct but is not sharp for *ellipticity alone*. A limited SymPy polynomial test confirmed the commutator identity, not the full proof.
- **POME-NORMALIZATION-SMOOTH-BASE-001 — low / verified conditional deduction:** normalization commutes with product by an arbitrary smooth complex manifold. A self-contained Cauchy-coefficient argument establishes normality of the product; finite bimeromorphic uniqueness completes the claim **conditionally on Theorem 9.4.6**. Existing proof-gap **POME-NORM-COUNTABLE-COVER-001 remains unresolved**.
- **Actual scope:** first selected proof-level §§2.20.1/.4/.11/.12 and §§9.11.2/.3/.5/.7; §9.4.3–6 only incremental crosscheck. The previous **POME-UNI-EXT-FN-001** Fornaess–Narasimhan external dependency remains open. 747-section ToC is an inventory, none certified wholesale. Entire dedicated Demailly approximation/regularization/Bergman/L²/OT/multiscale/positivity-loss programme remains **deferred-by-user**. No builds, CI, publishing, source, main, tag or registry changes.

---

# 2026-10-26 — exact Guillemin boundary Hessians; topologically trivial nonprincipal divisors

**Reviewed main:** b6933b772f41b45918f7e25ed1afbbb1fd892272; **audit base:** 08addf9b957793fcd958f87f5e1bafb54e044da3. [Full English proofs, stable tags and precise integrated anchors](reports/2026-10-26-guillemin-stratum-hessian-and-nonprincipal-null-chern-divisors.md).

- **POME-GUILLEMIN-STRATUM-HESSIAN-001 — low / verified conditional deduction:** Theorem 21.10.1's boundary-stratum local inverse yields an **exact positive determinant formula** for the Guillemin curvature Hessian in every vertex coordinate chart, including all boundary orbits; at a torus-fixed point the diagonal entries are explicit exponentials of the *nonincident* facet constants. This is genuinely higher-dimensional and all-strata, distinct from the earlier one-dimensional segment example; the printed theorem is correct.
- **POME-DIVISOR-CHERN-NONPRINCIPAL-001 — low / verified conditional deduction:** On a complex elliptic curve, the divisor [p]-[q] for p≠q has **zero integral Chern class but is not principal**; elementary doubly-periodic residue proof. This separates the valid principal-divisor kernel of the divisor-to-Pic map in §20.7.3 from the much larger kernel of c1. No converse printed in the source is alleged false.
- **Actual focused proof re-review:** integrated §21.10.1 (local inverse, Hessian and transition proof, lines 24–89) and §20.7.3 (Poincaré–Lelong/divisor class proof, lines 12–28); §§21.8–21.9 consulted only for dependencies. The **747-row** current ToC coverage matrix is preserved, no whole section certified; earlier toric and Cartier audit IDs unchanged. Excluded Demailly approximation/regularization/Bergman/L²/Ohsawa–Takegoshi/multiscale/positivity-loss remains **deferred-by-user**. No project tests, builds, CI, publication, main/source/registry/permanent-tag changes.

---

# 2026-10-26 — symmetric convex equilibrium measures: total variation under Hausdorff nets and sharp \(C^2\) boundary integrability

**Reviewed main:** b6933b772f41b45918f7e25ed1afbbb1fd892272; **starting audit head:** fda6c6f604017ac7acc8ceb90f2c743b632f7621; **UTC checkpoint:** 2026-10-26T01:06:06.774Z. [Detailed English proofs and actual integrated anchors](reports/2026-10-26-real-convex-equilibrium-tv-and-smooth-boundary-endpoint.md).

- **POME-REAL-CONVEX-EQUILIBRIUM-TV-001 — low / verified conditional deduction:** for arbitrary directed Hausdorff-convergent nets of full-dimensional origin-symmetric real convex bodies, their equilibrium measures converge in **total variation**. Polar-volume density formulas give uniform convergence on every \(rK\), \(r<1\); the uniform \(O(\sqrt{1-r})\) Minkowski boundary-layer mass bound eliminates the remainder without sequential extraction.
- **POME-SMOOTH-CONVEX-DENSITY-LORENTZ-001 — low / verified conditional deduction:** for any real convex \(C^2\) body (no symmetry or strictly positive curvature), the equilibrium density has exact distribution-tail order \(T^{-2}\); hence weak \(L^2\) but no finite Lorentz \(L^{2,q}\), \(L^p\) exactly when \(p<2\), and sharp square-density logarithmic threshold \(\beta>1\). The ball gives an explicit nonzero leading constant. Distinct from the older **nonsmooth cube** Lorentz finding; no double-counting.
- **Actual selected proof-level coverage:** first §16.42.1–6 with full pinned current blobs/tags/physical lines; §16.34.2 support/mass, §16.36.1 normalization, §16.33.6 real-body formula were dependency checks, not full certifications. A prior §16.39.1 result is retained as historical. 747 existing ToC sections preserved, no complete section certified. Entire author-excluded Demailly approximation/regularization/Bergman/\(L^2\)/Ohsawa–Takegoshi/multiscale/positivity-loss program remains **deferred-by-user**. No tests, builds, CI, publication or main/source/registry/tag changes.

---

# 2026-10-26 — Lelong strata: compact-uniform weak-net semicontinuity and optimal Hausdorff dimension

**Reviewed main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`; **starting audit head:** `9f186281dfdc5eb8ce35b374496eddb273d5e747`. [Complete source-anchored proof](reports/2026-10-26-lelong-net-compact-strata-and-sharp-level-dimension.md).

- **POME-LELONG-NET-COMPACT-STRATA-001 — low / verified conditional deduction:** weak convergence of arbitrary directed nets of positive closed fixed-bidimension currents implies `limsup_i sup_K ν(T_i,·) ≤ max_K ν(T,·)` for every compact `K`; consequently high-Lelong strata eventually avoid every compact set disjoint from the limit stratum. Proof uses the source's normalized monotonicity, good radii, upper vague-measure bounds on a fixed closed ball, and finite covers; no sequential compactness. Applies also to `L¹_loc`-convergent directed psh nets. Smooth `dd^c log(|z_1|²+ε)` converging to a divisor proves **no reverse** persistence.
- **POME-LELONG-LEVEL-SHARP-DIM-001 — low / verified conditional deduction:** the `2p` Hausdorff dimension exponent of the high-Lelong strata in Theorem 6.33.13 is sharp for the integration current of a complex `p`-plane, including the `p=0` atom convention. No assertion about the optimal numerical `4^{2p}` covering constant.
- **Actual first selected proof coverage:** §§6.7.1/.6/.9 and §§6.33.1/.5/.7–8/.10/.13, with exact integrated blobs, stable tags, physical anchors and conditional inputs in the report. Current 747-section ToC matrix remains an inventory, not a certification. Entire dedicated Demailly approximation/regularization/Bergman/L²/OT/multiscale/positivity-loss programme remains **deferred-by-user**. No builds, CI, publication, main/source/body/registry/permanent-tag changes.

---

# 2026-10-26 — sharp power-capacity exponent and higher-dimensional pluriharmonic descent

**Reviewed main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`; **starting audit head:** `4c37fd3422f4292ff4f4e0262398882aff775aed`. [Complete current-source-anchored proofs](reports/2026-10-26-sharp-power-capacity-and-higher-dimensional-pluriharmonic-descent.md).

- **POME-POWER-CAPACITY-EXPONENT-SHARP-001 — low / verified conditional deduction:** Theorem 15.33.6's explicit `L¹\setminus\bigcup_{p>1}L^p` density realizes **exactly** the power-capacity exponent `1+α`: on centered small balls, `μ(B_r)\asymp(\log(1/r))^{-n(1+α)}` and `Cap_h(B_r)\asymp(\log(1/r))^{-n}`; every stronger exponent fails. A complete local-capacity upper-bound proof uses the truncated radial extremal, Theorem 7.3.11 comparison with a strict perturbation, and a fixed smooth local correction. The printed theorem remains correct; BT inputs conditional.
- **POME-PLURI-FIBER-HIGHERDIM-001 — low / verified conditional deduction:** Lemma 11.22.4 extends from one-dimensional fibers to arbitrary-dimensional complex fibers satisfying positive-**pluriharmonic** Liouville; in particular all `ℂ^k` and compact connected complex fibers. Its necessity for universal descent on trivial bundles follows from an explicit horizontal current. This is genuinely distinct from the historical one-dimensional `POME-PLURI-FIBER-LIOUVILLE-001`, which is not re-counted.
- **Actual selected passages:** first selected §15.33.1/.6, §14.19.14/.16/.23, §11.22.4 (with .1/.2 contexts), and §5.48.1/.2. Supporting §§7.3.11 and 7.4.2 inspected; no full section or dependency chain certified. 747 current ToC rows retained. The author's Demailly approximation/regularization, Bergman, L², Ohsawa–Takegoshi, multiscale atlas and positivity-loss programme remains **deferred-by-user**. No tests, builds, CI, publication, main/source/registry/permanent-tag edits.

---

# 2026-10-26 — sharp finite generators, Baire-generic evaluations, and the \(\mathbf P^1\) extension conic

**Reviewed main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`; **starting audit head:** `da5a0c6dc72accab2f22e5059ff6a4423a360f72`. [Complete integrated-source-anchored mathematical proof](reports/2026-10-26-generation-sharp-baire-ext-conic.md).

- **POME-GENSEC-GLOBAL-SHARP-001 — low / verified conditional deduction:** Theorem 10.35.3's \(n+r\) global-generator bound is best possible for every \(n,r\ge1\). On \(\mathbf P^n\), \(\mathcal O(1)\oplus\mathcal O^{r-1}\) requires exactly \(n+r\) generators; elementary proof by constant trivial-component projection and common zeros of linear forms.
- **POME-EVAL-RESIDUAL-GENERIC-001 — low / verified conditional deduction:** Lemma 10.35.2's good \(p\)-tuples actually form a dense \(G_\delta\) for countably many admissible evaluation families, and an open dense set when finitely many parameter bases are compact. Proof extracts the topology and rank-stratum/Baire argument already present in the integrated lemma.
- **POME-EXT-P1-CONIC-001 — low / verified conditional deduction:** For extensions \(0\to\mathcal O(-2)\to E\to\mathcal O(2)\to0\) on \(\mathbf P^1\), the explicit connecting matrix \(\bigl(\begin{smallmatrix}a&b\\b&c\end{smallmatrix}\bigr)\) stratifies all extension classes: zero gives \(E=\mathcal O(-2)\oplus\mathcal O(2)\); the smooth projective conic \(ac=b^2\) of nonzero classes gives \(\mathcal O(-1)\oplus\mathcal O(1)\); its complement gives \(\mathcal O^2\). The proof uses explicit Čech cohomology and elementary section arguments, not Birkhoff–Grothendieck. This refines 10.36.14's noninjective forgetful map without declaring it false.
- **First selected proof-level coverage:** §§10.35 and 10.36, plus nonexcluded 10.30.2/.4/.5/.10; sources, current blobs, tags and physical line anchors are in the report. The 747-section ToC inventory remains an inventory only; **no complete section or chain certified**. Original 10.30.7–8 analytical regularization and the entire author's Demailly/Bergman/\(L^2\)/Ohsawa–Takegoshi/multiscale/positivity-loss programme remain **deferred-by-user**, not resolved or certified. No tests, builds, CI, publishing, source-body/registry/permanent-tag or main edit.

---

# 2026-10-26 — sharp dimension of supports of continuous-potential Kähler currents

**Reviewed main:** b6933b772f41b45918f7e25ed1afbbb1fd892272; **starting audit head:** 30f42bcd426a34956ae7f291bc227ec7f821b56c. [Full mathematical report](reports/2026-10-26-null-kahler-current-sharp-support-dimension.md).

- **POME-NULL-KAHLER-SUPPORT-HDIM-SHARP-001 — low / verified conditional deduction:** Corollary 5.65.2 forces \(\dim_{\rm H}\operatorname{Supp}T\geq2n-2\) for any nonzero positive \(dd^c\)-closed (1,1)-current on a compact Kähler \(n\)-fold. Equality holds in every dimension on \((\mathbf P^1)^n\) for a nonzero Kähler-class current with **continuous** global potential and **null** support: pull back a zero-dimensional digit Cantor measure with uniformly continuous logarithmic potential. No printed theorem is declared false. The previously audited Cantor capacity estimate is reused, not re-counted.
- **Actual newly selected proof coverage:** §5.64.1–2 and §5.65.1–2, with exact integrated lines and tags in the report. §5.64.3 and the approximation-dependent part of §5.64.4 were **not** checked. Matrix preserves exactly 747 unique current ToC rows; no complete section or proof chain certified. Dedicated Demailly regularization/Bergman/\(L^2\)/Ohsawa–Takegoshi/multiscale/positivity-loss remains **deferred-by-user**, neither solved nor certified. No source/body/tag edits, CI, builds, publication or formal checks.

---

# 2026-10-26 — sharp hyperplane relative mass and envelope-system cross-reference

**Reviewed main:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`; **pre-write audit head:** \`32d74a53c3a62797d733d8fdb4a75ba4da90e3ec\`. [Source-anchored complete English review](reports/2026-10-26-hyperplane-relative-mass-sharpness-and-envelope-system-crossref.md).

- **POME-REL-ENVELOPE-MASS-SHARP-001 — low / verified conditional deduction:** On fixed \(\mathbb P^n\), \(u=a\log|s_H|^2\) obeys \(P_{a\omega_{\rm FS}}(u)=u\) and has non-pluripolar top mass exactly \((1-a)^n v_-(\omega_{\rm FS})\); its entire mixed non-pluripolar profile is \((1-a)^k\omega_{\rm FS}^n\). Thus Lemma 16.28.69's constant is optimal, not wrong.
- **POME-IDEAL-PROJECTION-REFERENCE-KIND-001 — additional confirmed editorial occurrence:** proof of §16.29.3, line 65, calls Proposition 18.4.4 a “corollary”, just as already reported elsewhere in §18.4.5. This is a **new affected location of the same existing ID**, not a new theorem error or duplicated finding.
- **Actual first selected proof coverage:** §§16.28.68–70 and 16.29.3/.5/.9/.13/.16–18/.20–22. Old 747-section ToC matrix retained, exactly two previously inventory-only rows upgraded; none fully certified. Relevant BT/ideal/recovery dependencies stay conditional, dedicated Demailly regularization/Bergman/L²/Ohsawa–Takegoshi/multiscale/positivity-loss programme remains **deferred-by-user**. No builds, tests, CI, publishing, main/source/registry/tag changes.

---

# 2026-10-26 — bounded Dirichlet root concavity; selected §§5.8 and 13.32

**Reviewed main:** b6933b772f41b45918f7e25ed1afbbb1fd892272; **starting audit head:** db2677f8d5620e138d2849d3f9c7111e1945b6d4. [Full English source-pinned review](reports/2026-10-26-bounded-dirichlet-root-concavity-and-numerical-product-review.md).

- **POME-BT-DIRICHLET-JOINT-ROOT-CONCAVITY-001 — low / verified conditional deduction:** on a ball, the bounded-measurable-density Monge–Ampère Dirichlet operator is jointly pointwise concave in the nonnegative density root F=f^{1/n} and continuous boundary values. Proved by finite continuous-data subsolution mixtures (Lemma 7.9.1), L¹ data stability (Theorem 7.10.2), and canonical psh representatives. Constant-density quadratic solutions give equality. Neither theorem is alleged false; distinct previous mixed-current, sharp sup-norm, and capacity results are not re-counted.
- **Actual inspected passages:** first selected proof-level Lemma 5.8.2 / Theorem 5.8.4 and the nonexcluded Lemma 13.32.2 / Propositions 13.32.5–6; incremental §§7.9–7.10. All 747 original ToC rows retained; no whole section certified. Approximating-sequence proof portions of §13.32.1/.3 and the author's entire Demailly/regularization/Bergman/L²/Ohsawa–Takegoshi/multiscale/positivity-loss programme remain **deferred-by-user**, never resolved or certified. No tests/build/CI/site/publication/main/source/registry/tag edit.

---

# 2026-10-26 — fixed-root Gauduchon determinant stability and critical/supercritical separation

**Reviewed main:** b6933b772f41b45918f7e25ed1afbbb1fd892272; **starting audit head:** cd37374044b1a4fb86c814bd39412f4c88ab91ae. [Complete English source-anchored report](reports/2026-10-26-gauduchon-fixed-root-lq-stability-and-concentration.md).

- **POME-GAUD-FIXED-ROOT-STABILITY-001 — low / verified conditional deduction:** for the complete normalized positive-current family in Theorem 12.18.8, a **fixed strictly positive smooth root** r has attaining density k_r. Every current with deficit Delta=C||r||_n-int r k_T satisfies a quantitative critical-norm bound ||k_T-k_r||_q <= 2^((3-q)/2) sqrt[C Delta/((q-1)||r||_n)], q=n/(n-1), C=V^(-1/n); exponent 1/2 is optimal on smooth closed torus examples. Applies to arbitrary directed near-maximizing nets. Original theorem remains true, with mass/existence inputs conditional.
- **POME-GAUD-CONCENTRATION-LQ-VS-LP-001 — low / verified conditional deduction:** the smooth concentrating family of Proposition 12.18.2 has ||k_S-C||_q <= C[2/log(1/epsilon)]^(1/q), and the associated currents converge in coefficientwise total variation at rate O(1/log), although L^p density norms diverge for **all p>q**, as the source proves. Distinct from 12.18.17's varying-root sequence; no false source theorem asserted.
- **Actual first selected proof reading:** §12.18.1/.2/.6/.8/.13/.15/.17 (integrated proof lines 13–361); §12.18 upgraded from inventory only, all 747 ToC rows retained, no full section certified. Upstream smooth Monge–Ampère, mass invariance, duality and BT product chains not fully certified. Dedicated Demailly/regularization/Bergman/L2/Ohsawa–Takegoshi/multiscale/positivity-loss remains **deferred-by-user**. No tests/build/CI/website/source/main/registry/tag changes.

---

# 2026-10-26 — sharp weak endpoint for a smooth-center blowup; new §§15.23–15.24 coverage

**Reviewed main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`; **pre-write audit head:** `6fc009d70378c952fb5567bbf9420994453deeab`. [Source-anchored complete mathematical report](reports/2026-10-26-blowup-endpoint-weak-lp-and-root-audit-crosscheck.md).

- **POME-BLOWUP-WEAK-ENDPOINT-001 — low / verified conditional deduction:** for one codimension-\(r\ge2\) smooth-center blowup, nonnegative \(f\in L^p\), \(1<p<\infty\), has pushforward density \(F\in L^{s_*,\infty}\) with \(s_*=rp/((r-1)p+1)\), and \(\|F\|_{L^{s_*,\infty}}\le C\|f\|_{L^p}\). An explicit logarithmically weighted \(L^p\) datum fails at the *strong* \(L^{s_*}\) endpoint and at every higher weak exponent; the printed strict-\(L^s\) result remains correct. No PDE endpoint theorem is claimed.
- **Actual selected proof checks:** first pass §§15.23.2/.5/.10, 15.24.1/.4; §15.32.1/.4–.6/.9/.11 incremental comparison only, with historical directed-net result **not** re-registered. The existing 747-section matrix is retained, with no entire section or existence theorem certified. Dedicated Demailly/regularization/Bergman/L²/Ohsawa–Takegoshi/multiscale/positivity-loss research remains **deferred-by-user**. No tests/build/CI/site publication/main/source/registry/tag edits.

---

# 2026-10-25 — distributional Hessian representatives and square-root gradient stability

**Reviewed main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`; **starting audit head:** `129bd677b54aa15fd3c6c53bacaa696facc3f950`. [Complete source-anchored proof report](reports/2026-10-25-distributional-hessian-representatives-and-c0-to-c1-stability.md).

- **POME-DISTRIBUTIONAL-HESSIAN-REP-001 — low / verified conditional deduction:** even an *arbitrary real distribution* with locally bounded measurable distributional Hessian has a unique canonical `C¹,¹_loc` representative; on convex sets the gradient Lipschitz constant equals the essential operator-norm Hessian bound, and the printed entrywise `dC` bound is optimal. The printed §2.8.5 remains correct, with an optional strengthened statement.
- **POME-DISTRIBUTIONAL-C0C1-MODULUS-001 — low / verified conditional deduction:** common operator-norm Hessian bound `M` plus uniform `C⁰` error `δ` implies interior gradient error at most `inf_{0<t<r}(δ/t+Mt)`, hence `2√(Mδ)` in the small-error range. The Hölder-1/2 exponent is optimal, and arbitrary uniformly converging directed nets converge in compact-local `C¹` without selecting sequences.
- **Actual first selected proof-level coverage:** §2.8.1–5; §2.9.2/.4–6/.10–12/.19/.22/.24/.26–28 separately crosschecked with **no new Fourier claim** (previous Fourier/incidence finding IDs retained). 747-section ToC matrix is preserved, no entire section certified. The user-excluded Demailly approximation/regularization/Bergman/L²/Ohsawa–Takegoshi/multiscale/positivity-loss programme remains **deferred-by-user**. No project build, CI, formal verification, publication, source/main/tag/registry edit.

---

# 2026-10-25 — sharp Hölder Monge–Ampère ball masses and smooth density logarithmic cost

**Reviewed main:** b6933b772f41b45918f7e25ed1afbbb1fd892272; **starting audit head:** be465808e940d7f97ccc520bbfcfb4d114e5db6d. [Complete source-anchored mathematical report](reports/2026-10-25-sharp-holder-ball-mass-and-smooth-density-log-cost.md).

- **POME-SMOOTH-MA-LOG-COST-001 — low / verified conditional deduction:** an explicit smooth positive family on fixed \(\mathbb P^1\times\mathbb P^{n-1}\) has \(\sup U=0\), \((\omega+dd^cU)^n\leq\Lambda\omega^n\) and \(\|U\|_\infty=\log\Lambda\). Thus the printed Theorem 14.3.5 remains correct, but its uniform constant necessarily grows at least logarithmically in \(\Lambda\).
- **POME-HOLDER-BALL-MASS-EXPONENT-001 — low / verified conditional deduction:** on any Hermitian \(n\)-fold, a \(C^{0,\alpha}\) \(h\)-psh potential has \(\mathrm{MA}_h(u)(B_r)=O(r^{n\alpha})\); the bound is sharp for every \(0<\alpha\leq1\), with exact radial model \(\int_{B_r}(dd^c|z|^\alpha)^n=(\alpha/2)^nr^{n\alpha}\). For each \(0<\alpha<1\), the original spherical construction also admits a sharp singular-shell version. Earlier exponent-\(1/2\) records are *not* repeated.
- **Actual coverage:** first selected proof passages §§14.3, 14.5 and 15.26; §5.27.25 incremental local normalization crosscheck only. Neither the entire sections nor downstream existence results certified. All 747 actual ToC inventory entries preserved. Entire dedicated Demailly/regularization/Bergman/L²/Ohsawa–Takegoshi/multiscale/positivity-loss programme remains **deferred-by-user**. No complete project build, CI, formal verification, publication or main/source/tag/registry edits.

---

# 2026-10-25 — finite non-Archimedean joins and semipositive torsion oscillations

**Reviewed main:** b6933b772f41b45918f7e25ed1afbbb1fd892272; **starting audit head:** 5ef8820193c8afb40a85a2dc69513af720faff21. [Complete source-anchored proof report](reports/2026-10-25-nonarchimedean-finite-joins-and-torsion-semipositive-growth.md).

- **POME-NA-FINITE-JOIN-ORDER-001 — low / verified conditional deduction:** order-reflecting comparison Theorem 22.1.111 and §17.15.17 prove analytification carries every nonempty finite join to pointwise maximum. The extended order distance is preserved and finite joins are sharp 1-Lipschitz. This supplies a precise **partial internal proof** of §22.1.112, distinct from old translation/scaling ID POME-NA-OPS-001; other [Xia23Operations] inputs remain unverified.
- **POME-SEMIPOS-TORSION-OSCILLATION-001 — low / verified conditional deduction:** on $E\times\mathbb P^{n-1}$ a flat $q$-torsion factor tensored with $\mathcal O(1)$ yields a smooth semipositive line bundle with $\Omega_L^n=0$ but exact $h^0(L^k)=\mathbf1_{q\mid k}\binom{k+n-1}{n-1}$. Thus normalized order-$k^{n-1}$ growth oscillates; printed Corollary 19.10.1 is **correct**, but no general second coefficient exists.
- **Actual selected coverage:** further §22.1.31/.73/.105/.111/.112 and §17.15.12–17, plus independent §19.10.1–2 sharpness test; earlier §22.1 and §19.10 records retained without repetition. No entire section, project comparison theorem, or Morse inputs certified. 747-row ToC inventory preserved. Excluded dedicated Demailly/regularization/Bergman/L²/OT/multiscale/positivity-loss work remains **deferred-by-user**. No tests/build/CI/publication/source/main/registry/tag changes.

---

# 2026-10-25 — uniform nuclear Fredholm presentations and sharp non-Hausdorff caveat

**Reviewed main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`; **starting audit head:** `1cf916e662cd720ecc31f0ea084d4218d44312e0`. [Full source-anchored proof](reports/2026-10-25-nuclear-perturbation-uniform-presentations-and-nonhausdorff-cokernels.md).

- **POME-RELNUC-BASECHANGE-FP-001 — low / verified conditional deduction:** Lemma 9.46.3's nuclear-factorization proof yields a single finite square matrix over the Banach algebra whose base changes present *every* actual cokernel, algebraically and topologically even in the non-Hausdorff category; this is stronger than finite generation, not a false theorem.
- **POME-RELNUC-NONHAUS-COKER-001 — low / verified conditional deduction:** multiplication by the coordinate function in `C([0,1])` gives a one-term relative-nuclear map with nonclosed `(I-v)` image; non-Hausdorff disclaimer in §9.46.3 cannot be removed.
- **Actual coverage:** first selected §§9.41–9.43,9.45; incremental §§9.44,9.46–9.47; §9.40 overview only. No full section or upstream Oka/nuclear exactness chain certified. All 747 ToC rows remain; excluded Demailly/regularization/Bergman/L²/OT/multiscale/positivity-loss research stays **deferred-by-user**. No tests, build, CI, site publication, source/registry/tag/main edits.

---

# 2026-10-25 — sharp convex-log tube bound and strict Gauduchon current-volume gap

**Reviewed main:** b6933b772f41b45918f7e25ed1afbbb1fd892272; **starting audit head:** 7c0d4aeb97427357b864127978530f757d16fb2a. [Complete English source-anchored report](reports/2026-10-25-convex-tube-log-majorant-and-strict-gauduchon-volume-gap.md).

- **POME-TUBE-CONVEXLOG-MAJORANT-001 — low / verified conditional deduction:** sharp logarithmic barycentric majorant for any continuous positive real-base bound on holomorphic functions on a connected tube; Bochner extension is isometric in the H-infinity norm. Printed §9.39.7 true.
- **POME-GAUD-STRICT-DOM-GAP-001 — low / verified conditional deduction:** positive current difference S>=tau h yields exact sharp root-volume gap tau lambda_mu(h) and volume gap ((epsilon+tau)^n-epsilon^n) V_mu(h); equality for theta=tau h, beta=0. Printed §12.24.1 true.
- **New actual selected proof coverage:** §§9.38–9.39 and 12.24; §12.2 is defining-quotient crosscheck, §9.37 orientation. No complete section/dependency chain certified; 747 ToC rows retained. Dedicated Demailly approximation/regularization/Bergman/L²/Ohsawa–Takegoshi/multiscale/positivity-loss remains **deferred-by-user**. No tests/build/CI/site/main/source/tag/registry writes.

---

# 2026-10-25 — ideal-obstacle concavity and projection-reference correction

**Reviewed main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`; **starting audit head:** `1689f9475b9a125be4606f0b8ce46fa49aae6b27`. [Complete pinned English proof/audit](reports/2026-10-25-ideal-obstacle-concavity-and-projection-reference-kind.md).

- **POME-IDEAL-PROJECTION-REFERENCE-KIND-001 — low / confirmed error (editorial only):** Corollary 18.4.5 cites the last identity of nonexistent “corollary 18.4.4”; the actual source is Proposition 18.4.4. No mathematical claim is alleged false; propose a one-word reference-kind correction only.
- **POME-IDEAL-OBSTACLE-CONCAVITY-001 — low / verified conditional deduction:** the ideal envelope is concave under convex interpolation of smooth obstacles, pointwise 1-Lipschitz in the obstacle sup norm with **sharp** constant, and uniformly continuous for arbitrary directed nets of uniformly convergent obstacles. Also yields a separated-product sum-of-errors bound via existing §18.16.2, whose other dependencies remain conditional.
- **New selected coverage:** §§18.4, 18.16, 18.25; narrow original-source crosschecks in §§18.12.2, 5.37.3–4 and 5.43.18/.24. No full-section certification, 747 actual ToC rows retained. All user-excluded Demailly regularization/Bergman/L²/Ohsawa–Takegoshi/multiscale/positivity-loss work remains **deferred-by-user**, not reopened. No builds, tests, CI, source/registry/tag/main modifications or publication.

---

# 2026-10-25 — exact ideals of a nonanalytic toric pole and inradius stability

**Reviewed main:** b6933b772f41b45918f7e25ed1afbbb1fd892272. **Report first committed:** 418657b8ce92f54026c4a5943bfc5197ed8ac93f; **subsequent net-proof clarification:** 11c779acd9ed7113782f5acb0fd593d5b937a55d. [Source-anchored full proofs](reports/2026-10-25-toric-nonanalytic-multiplier-ideals-and-inradius-stability.md).

- **POME-TORIC-ROOT-IDEAL-THRESHOLDS-001 — low / verified conditional deduction, printed Proposition 11.43.10 correct:** for its nonanalytic pole \(\Phi_{P_a}\) on \(\mathbb P^n\), the multiplier-ideal stalk at \(o\) is precisely the monomial ideal generated by \(z^\alpha\) with \((\sum_i\sqrt{\alpha_i+1})^2>ac\) at weight \(c\). The complex singularity exponent is \(n^2/a\). Strict endpoints proved by disjoint fixed-size boxes in logarithmic polar variables, and arbitrary germs handled by rotation averaging and finite monomial generation; no approximation programme used.
- **POME-CONVEX-INRADIUS-FUNCTIONAL-001 — low / verified conditional deduction, printed Theorem 11.43.6 correct:** a limiting convex body's ball \(B(c_0,R)\subset K\) automatically supplies a common translated simplex on a Hausdorff-convergent tail. Its scalar difference obeys \(n|\log(r_i/r)|-n\log(1-d_H(K_i,K)/R)\). A separate integrable-barrier/compact-complement argument proves \(L^1\) convergence along arbitrary directed nets (not via net-dominated-convergence).
- **Actual first selected coverage:** §§11.41–11.43 only, with basic multiplier-ideal convention in §5.37.1; no entire section certified. All previous ledger records retained. The dedicated Demailly approximation/regularization, Bergman, L2, Ohsawa–Takegoshi, multiscale-atlas and positivity-loss programme is **deferred-by-user**. No build, CI, publication, source/registry/tag/main changes.

---

# 2026-10-25 — OT transverse probability simplex and exact Nakano twist spectrum

**Main:** b6933b772f41b45918f7e25ed1afbbb1fd892272. **Pre-write audit head:** e1d505fe5494bf2a2f056b0aabd1eb07f7e13166. **UTC checkpoint:** 2026-10-25T09:10:42.055Z. [Complete English proof and anchors](reports/2026-10-25-ot-transverse-probability-simplex-and-projective-tangent-spectrum.md).

- **POME-OT-TRANSVERSE-PROBABILITY-SIMPLEX-001 — low / verified conditional deduction:** on an Inoue surface of type (1,1), normalized continuous theta-psh potentials are AFFINELY HOMEOMORPHIC, in the uniform topology, to Borel probability measures on the transverse log-circle in weak-star topology. Their transverse curvature is the measure mu=ds+(D²−D)h of mass log(lambda); every such measure occurs, including singular-continuous measures. The printed OT rigidity theorem and atomic example remain correct.
- **POME-PROJTANGENT-TWIST-NAKANO-SPECTRUM-001 — low / verified conditional deduction:** for the induced metric on T P^n tensor O(k), n>=2, the exact Nakano eigenvalues are k and k+2, with skew/symmetric multiplicities n(n−1)/2 and n(n+1)/2. Griffiths strict positivity iff k>=0; Nakano strict positivity iff k>=1. The n=1 exception is explicitly retained. Original formulas correct.
- **Actual selected coverage:** proof-level selected §10.29 and previously inventory-only §10.34 algebraic curvature; incremental §10.28 historical slicing; §10.33 algebraic curvature only; §10.32 context only. Old OT lattice/trace/mass and blowup findings not repeated. 747 current ToC rows retained, no complete-section certification. Dedicated Demailly approximation/regularization and Bergman/dedicated L2/OT/multiscale/positivity-loss programme remains **deferred-by-user**. No tests, build, CI, publication, source/registry/tag/main changes.

---

# 2026-10-25 — Grassmannian slice density excess and monomial multiplicity intervals

**Reviewed main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`; **starting review head:** `c080a549e4e5208cf8e95daa8eef2bb238d38336`. [Full English source-anchored report](reports/2026-10-25-grassmannian-slice-excess-and-monomial-multiplicity-intervals.md).

- **POME-GRASSMANN-SLICE-L1-EXCESS-001 — low / verified conditional deduction:** §6.41.9's exact averaged finite-radius density identity implies \(\int\nu(T_S,0)\,d\nu_q=\nu(T,0)\), and the exact **nonnegative \(L^1\) slice excess** \(\|D_{T_S}(a)-\nu(T_S,0)\|_{L^1(\nu_q)}=D_T(a)-\nu(T,0)\to0\). Also gives a Markov bound and convergence along arbitrary shrinking-radius nets. Printed theorem remains correct.
- **POME-MONOMIAL-MULTIPLICITY-INTERVAL-001 — low / verified conditional deduction:** for diagonal finite monomial maps the attainable ratios \(\nu(F_*T,0)/\nu(T,0)\) realize **every real value** between the products of the smallest and largest \(p\) exponents. The same holds for directional generalized Lelong numbers with real positive weights, realized by positive combinations of two coordinate-plane integration currents. The printed §6.47 bounds are correct.
- **Actual selected proof audit:** first targeted §6.41.1/.2/.4/.5/.7/.9; incremental §6.47.1–2 with §§6.43.1–2, 6.46.1–2 as internal dependency checks. The 22 October §§6.43–6.44/6.46–6.48 review is retained rather than falsely repeated as first coverage. No whole-section certification; all 747 rows preserved. All dedicated Demailly/Bergman/L²/OT/multiscale/positivity-loss work remains **deferred-by-user**. No project build, tests, CI, publication, source/main/tag/registry edits.

---

# 2026-10-25 — capacity-dominated exponential moduli and a logarithmically slow non-pluripolar measure

**Reviewed main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`; **starting review head:** `e5cd7f073f0a34a5ceab7fd0e89c561a646d3145`. [Complete source-anchored English mathematics](reports/2026-10-25-nonpluripolar-exponential-moduli-and-slow-logarithmic-example.md).

- **POME-CAP-DOM-EXP-MODULUS-001 — low / verified conditional deduction:** a finite measure satisfying `mu(E)<=A Cap_omega(E)^gamma` admits a uniform exponential damping modulus `O(lambda^gamma)` if `0<gamma<1`, `O(lambda log(1/lambda))` if `gamma=1`, and `O(lambda)` if `gamma>1`; proof by the exact layer-cake identity and §5.29.4.
- **POME-NONPOLAR-SLOW-EXP-001 — low / verified conditional deduction:** a **fixed** absolutely continuous non-pluripolar probability on P¹ and a **fixed** normalized logarithmic potential have exact damping `I(lambda)~1/log(1/lambda)`. Finite non-pluripolarity alone implies no universal positive power rate. §5.44.5 remains correct and is not claimed false.
- **Actual selected coverage:** new §5.26.2, incrementally §§5.25.1–3, 5.44.2/.4/.5/.7/.10/.12, §5.29.2 and §5.22 standing setup as narrow dependencies; no whole-section or upstream Skoda/Cegrell certification. Existing 747 ToC rows preserved. Entire dedicated Demailly approximation/regularization, Bergman, L², OT, multiscale and positivity-loss programme stays **deferred-by-user**, not reopened. No build, tests, CI, publication, source/tag/registry/main edits.

---

# 2026-10-25 — birational multiplier-ideal projection formula: internal Jacobian repair

**Reviewed main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`; **starting audit head:** `737b1429ac8bb8c3e4b34b4e6c66d906862bc23e`. [Pinned complete English proof and source anchors](reports/2026-10-25-multiplier-ideal-birational-jacobian-rule.md).

- **POME-MI-BIRATIONAL-JACOBIAN-001 — medium / verified repair of a genuine external dependency:** §16.6.4 cites Dem12 for the sheaf identity \(\mathcal I_X(\phi)=\pi_*(K_{Y/X}\otimes\mathcal I_Y(\phi\circ\pi))\). A direct proof by holomorphic Jacobians, Hartogs extension and change of variables supplies exactly the missing birational pushforward step; Proposition 16.6.10 still requires its separate internal psh descent theorem. The printed claim is not false.
- **POME-MI-SMOOTH-CENTER-FLOOR-001 — low / verified conditional deduction:** exact smooth-center logarithmic multiplier ideal \(\mathfrak m_Z^{\max(0,\lfloor c\rfloor-\operatorname{codim}Z+1)}\), with a codimension-two counterexample to the *unprinted* formula omitting the relative Jacobian divisor.
- **New selected proof-level coverage:** §16.6 (only enumerated claims); §§5.16, 5.17 and 9.10 narrowly crosschecked as dependencies. Neither a whole section nor the project certified. §16.6.22 Bergman approximation, and all dedicated user-excluded regularization/Bergman/L²/OT/multiscale/positivity-loss work, remain **deferred-by-user**.

---

# 2026-10-25 — sharp Hermitian sublevel capacity and quantitative Bedford–Taylor mass decay

**Reviewed main:** b6933b772f41b45918f7e25ed1afbbb1fd892272; **starting review head:** c241cc29a997b256a55271b032483c60a268e258. [Exact English mathematics, source tags and line anchors](reports/2026-10-25-sharp-logpole-hermitian-capacity-and-quantitative-bt-mass.md).

- **POME-HERM-CAP-LOGPOLE-SHARP-001 — low / verified conditional deduction:** a fixed normalized logarithmic psh potential on P¹ has global sublevel capacities comparable to 1/t, with explicit circular test and local-to-global glued curvature. The printed 5.29.4 tail exponent is sharp, **not false**.
- **POME-BT-HARMONIC-L1-QUANT-001 — low / verified conditional deduction:** quantitative mixed BT mass bound \(C M^{k-1}\|p-h\|_{L^1}\), with pluriharmonic h and common middle-ball sup bound; optimal homogeneous exponent and arbitrary directed-net convergence. The correct unbounded §5.27.30 examples do not violate it.
- **Actual first selected proof coverage:** §§5.27–5.29; **incremental** existing selected §16.13 recheck, no complete section certified. 747 ToC rows retained, user-excluded regularization/Bergman/L²/OT/multiscale/positivity-loss programme **deferred-by-user**. No tests, build, CI, formal proof or source/registry/tag/main/site changes.

---

# 2026-10-25 — full-mass singular determinant obstruction and non-semipositive strict barriers

**Reviewed main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`; **UTC checkpoint:** 2026-10-25T04:01:46.191Z. [Complete mathematical report, counterexample and source anchors](reports/2026-10-25-singular-full-mass-and-nonpositive-strict-barriers.md).

- **POME-FULLMASS-SINGULAR-AC-001 — low / verified conditional deduction:** For every n, a flat Kähler torus \(E^n\) has a bounded continuous full-mass potential \(u\) with \(T_{\rm ac}=0\) even though \(\underline{\rm vol}_\theta(u)=\int\langle T^n\rangle=\int\theta^n=n!\). Smooth Kähler approximations have uniformly convergent potentials, unchanged mass \(n!\), but Monge–Ampère measures at signed-TV distance \(2n!\) from the limit. Detailed Frostman Cantor/Green/heat proof; printed Lemma 13.31.1 remains correct and can be strict maximally.
- **POME-STRICT-BARRIER-NONPOS-BG-001 — low / verified conditional deduction:** The one-way smaller-background criterion of Proposition 13.20.4 holds without \(\theta\ge0\), for **every** sufficiently small positive reduction \(t\), using the strict barrier supplied by §13.20.3 and the universal smooth-form upper bound \(\theta\le C\omega\). The printed proposition is true; only optional hypothesis sharpening is proposed.
- **Actual selected proof review:** §§13.20, 13.25–13.26, 13.31; dependency-only §13.28 Green kernel. No chapter/section certified. §13.31.3 modification approximation, §§13.25.5/13.26.7 analytic approximation, and all dedicated Demailly/Bergman/L²/OT/multiscale/positivity-loss work remain **deferred-by-user/unverified**, not reopened. Matrix 747 current ToC rows preserved. No local code checks, builds, CI, formalization, publishing, PR, source/main/tag/registry edits.

---

# 2026-10-25 — exact Robin and fixed-ball capacities of real cubes

**Reviewed main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`; **audit starting head:** `ce0d84a24630262859540f0d02f8f2586646f8bb`. [Exact English source-anchored proof and selected proof checks](reports/2026-10-25-exact-robin-capacity-for-real-cubes.md).

- **POME-CUBE-ROBIN-EXACT-001 — low / verified conditional deduction:** for `K_r=[-r,r]^n`, `c(K_r)=r/2`, `alpha(K_r)=r/(1+sqrt(1+r^2))`, and their ratio approaches one as `r→0`. This proves sharpness of the lower coefficient in §16.37.3; the printed theorem is correct. The one-variable Joukowski bound and §16.36 product-max formula give a complete elementary proof and an independent normalized arcsine-measure check.
- **Actual selected proof review:** §§16.37, 16.38, 16.41; §16.36 current-source cross-check only. Earlier `POME-CUBE-LORENTZ-ENDPOINT-001` was located in the historic ledger and **not counted as new**. No whole section certified; all 747 existing ToC rows preserved. No builds, tests, CI, formalization, site publication or source/main/tag/registry writes. Dedicated Demailly regularization/Bergman/L²/OT/multiscale/positivity-loss research remains **deferred-by-user**.

---

# 2026-10-25 — coupled mollification of Radon nets and a compactly supported signed-net obstruction

**Reviewed main:** b6933b772f41b45918f7e25ed1afbbb1fd892272. **Starting audit head:** 17db5e9b50cd5d14568e717f95a199f8d5da1786. [Full English source-anchored proof](reports/2026-10-25-joint-mollification-positive-nets-and-signed-obstruction.md).

- **POME-MEASURE-JOINT-MOLL-NET-001 — low / verified conditional deduction:** for an arbitrary directed vague-convergent net of **positive** Radon measures μ_i and any ε_i→0, the coupled smooth measures (μ_i*ρ_{ε_i})dx converge vaguely to μ, and their derivatives converge distributionally. A net of signed measures has the same conclusion under eventual locally uniform total-variation bounds. Proof uses one compact cutoff giving eventual local mass control, and locally uniform convergence of ordinary test-function convolution.
- **POME-SIGNED-NET-NONUNIFORM-MOLL-001 — low / verified conditional deduction:** an explicit algebraic construction gives a net of finite signed atomic measures **supported in one fixed compact interval**, converging to zero against *every* C_c test, and ε_i→0, but a fixed smooth ψ tests all mollified measures to **1**. Infinite linear independence of ψ*ρ_ε follows from positive even moments and a Vandermonde argument. The hypothetical arbitrary-signed-net strengthening is false; the printed fixed-distribution Proposition 2.5.3(2) remains correct.
- **Actual new selected proof coverage:** §§2.2–2.5, with incremental §§2.6.1–2.6.2. No complete section or dependency chain certified and no project build/test/CI/formalization/site publication. All 747 existing ToC rows preserved. Ordinary Euclidean convolution here does not reopen the **deferred-by-user** Demailly approximation/regularization/Bergman/L²/OT/multiscale/positivity-loss programme.

---

# 2026-10-25 — exact rational birational jumps and noncommuting Gauduchon cone limits

**Fresh main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. **UTC checkpoint:** 2026-10-25T01:00:02.981Z. **Starting review head:** `1efbbcaad782d1b0e58210ed2809d19a4fa4f9fc`. [Full English source-anchored report and proofs](reports/2026-10-25-gauduchon-rational-blowup-jumps-and-double-scaling.md).

- **POME-GAUD-BLOWUP-RATIONAL-JUMPS-001 — low / verified conditional deduction:** Strengthen Proposition 12.23.1: for a smooth nonclosed semipositive product background and one smooth-center blowup, the Gauduchon variational-volume **ratio** has an explicit positive Beta-function prefactor and exponent `(m-1)/k`. Choosing `m=a+1, k=b, p>(a+1)/b` realizes **every positive rational jump `a/b`** with *both* endpoint orders positive. The printed proposition and its integer cases are correct.
- **POME-GAUD-CONE-DOUBLE-SCALE-001 — low / verified conditional deduction:** On `P¹×P^q`, `theta_t=t B1+B2`, `Omega=B1+B2`: exact `V_mu(theta_t+epsilon Omega)=(q+1)(t+epsilon)(1+epsilon)^q`. Fixed-background order is 0 at `t>0` and 1 at `t=0`, despite `C^infty` convergence; `t=epsilon^s` has double-scale slope `min(s,1)`. This does not contradict §§12.25–12.26's **fixed** parameter order results.
- **Actual newly selected proof coverage:** §§12.21–12.23 and 12.25–12.26, including explicit elliptic determinant/Schur computations, birational Gauduchon test transport, the blowup model's Beta integral, singular divisor comparison and maximal-rank criterion. §12.24 context only; no complete section or PDE/Hironaka prerequisite certified. All 747 section rows preserved. No test/build/CI/formalization/publication/PR/main/tag/registry writes. User-excluded regularization programme remains **deferred-by-user**.

---

# 2026-10-25 — changing-background curve models have no general midpoints and may have infinite path length

**Fresh main:** b6933b772f41b45918f7e25ed1afbbb1fd892272. **UTC checkpoint:** 2026-10-25T00:03:40.568Z. **Starting audit head:** 6622b52999cc3ecac84707afcf359954a732382a. [Complete English report with proofs and exact source anchors](reports/2026-10-25-curve-joint-metric-intrinsic-and-boundary-completeness.md).

- **POME-CURVE-JOINT-NONMIDPOINT-001 — low / verified conditional deduction:** The complete joint space of Theorem 13.30.3 need not be geodesic. Two positive scalar-multiple backgrounds with zero polar measure and C^0 separation above the clipping threshold admit **no metric midpoint**; the fixed-background geodesic statement is unchanged.
- **POME-CURVE-JOINT-NONRECTIFIABLE-001 — low / verified conditional deduction:** Every D-continuous path has length bounded below by the **unclipped** weighted series of endpoint C^k distances. On a flat elliptic curve, two area-one positive backgrounds differing by a small sine density give a finite-D-distance, topologically connected pair with **no rectifiable connecting path** for standard derivative C^k norms.
- **POME-PSH-BOUNDARY-COMPLETE-METRIC-001 — low / verified conditional deduction:** On a bounded C^\infty pseudoconvex domain, the explicit §9.35 power exhaustion gives the smooth complete Kähler potential Φ=−log(−u), with collar bound H_Φ≥(η/2)|∂δ|²/δ²+η|ξ|². No claim of C^\infty metric under merely C² boundary regularity.
- **Actual newly selected proof coverage:** §§9.35, 10.60, 13.28–13.30, not whole sections or upstream dependency chains; §9.31 is comparison context only. No false theorem claimed, no tests/build/CI/publication/main/source/registry/tag edits. User-excluded Demailly regularization and its Bergman/L²/Ohsawa–Takegoshi/multiscale/positivity-loss programme stays **deferred-by-user**.

---

# 2026-10-25 — sharp support-family hypothesis and high-dimensional Kummer nonrigidity

**Freshly reviewed integrated main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. **UTC checkpoint:** 2026-10-24T23:03:27Z. **Audit starting head:** `8271f45fb6762fa2372d5c4e5d5cd072ee02bf60`. [Complete English report with proofs, source labels and exact line anchors](reports/2026-10-25-soft-support-sharpness-and-kummer-semipositive-families.md).

- **POME-SUPPORT-ENLARGE-SHARP-001 — low / verified conditional deduction, not a false theorem.** For the soft continuous-function sheaf on the real line and supports confined to a singleton, nonenlargability permits `H^1_{\{0\}}` of dimension continuum; `1/x` obstructs supported lifting despite soft kernel. This demonstrates that Theorem 10.56.2's enlargability is essential. Compact-support applications remain valid under their locally compact hypotheses.
- **POME-KUMMER-INFINITE-SEMIPOSITIVE-001 — low / verified conditional deduction, not a false proposition.** In §10.27.2 the single irrational nef, square-zero Bott–Chern class has smooth semipositive representatives varying over embedded affine balls of every finite dimension, all vanishing near the sixteen exceptional curves.
- **Actual new selected proof coverage:** §§10.27, 10.54–10.56; rechecked selected §10.26 passages *without re-registering* older GH/rational-diameter deductions from 20 October. All 747 table-of-contents rows preserved. This is neither complete proof verification of these sections nor certification of the collection, complex-space input or hypercohomology comparison.
- **Boundary:** Dedicated user-excluded Demailly approximation/regularization and associated Bergman/L²/Ohsawa–Takegoshi/multiscale/positivity-loss proof programme remains **deferred-by-user**, not solved/certified or reopened. No tests, full build, CI, publication, source/tag/registry/main writes, PR, or merge.

---

# 2026-10-25 — Hermitian affine scaling and new Bochner equation reading defects

**Reviewed main:** b6933b772f41b45918f7e25ed1afbbb1fd892272. **UTC checkpoint:** 2026-10-24T22:00:23Z. [Complete source-anchored English report](reports/2026-10-25-hermitian-affine-background-scaling-and-bochner-equation-aliases.md). Newly selected proof-level review: §§11.37–11.40, 11.48 (not whole-section certifications); §11.42 context only.

- **POME-HERM-BOCHNER-EQUATION-ALIASES-001 — medium / confirmed reading-edition integration error:** five new independent permanent tags for Eqs. 11.48.5/.11/.12/.17/.18 duplicate existing canonical grouped equations as invalid nested aligned/align displays at physical line 247, with full rows at lines 27, 101 and 162. Preserve all tags, retain the full original rows, and repair only their alias/standalone rendering; not a false mathematical identity.
- **POME-HERM-BOCHNER-DOUBLEPRIME-001 — low / confirmed notation error:** the canonical 11.48.5 and 11.48.18 rows, as well as aliases, contain right-double-quote U+201D after delta/Delta instead of TeX double primes; main section blob 4656b430de6ec989ef121eca550afda0be407222, physical lines 27/162/247.
- **POME-HERM-BACKGROUND-AFFINE-SCALING-001 — low / verified conditional deduction:** for beta'=c beta+dd^c h positive (c>0), exact B_beta'=B_beta+n log c for all bounded tests; hence H shifts by the same constant and support-probability sets are identical; v_±(beta')=c^n v_±(beta). Complete elementary pushforward proof in the report, sharpens endpoints of §11.40.2 and crosschecks §11.38.3 without assuming closedness.
- **Limits:** selected entropy/type/background proof passages only, plus a finite n=2 torsion matrix calculation, not full torsion-Bochner verification. Actual 747-section ToC coverage retained. Demailly approximation/regularization and its dedicated Bergman/L2/OT/multiscale/positivity-loss proof-completion programme remains **deferred-by-user**, not opened or certified. Only audit Markdown updated on review/mathematical-audit; no main, source, registry, permanent tag or published-doc modification, CI or automatic publication.

---

# 2026-10-25 — normalization gluing does not imply global second countability; cusp pullback multiplicities

**Reviewed main:** b6933b772f41b45918f7e25ed1afbbb1fd892272. **Starting review head:** 640c02dd3371f29da4a372fac6fc0cec2a15d0fd. Fresh main AGENTS.md and documentation/proof-expansions.md; review README.md, prior LATEST.md, cumulative ledger and actual 747-row section matrix reread. [Complete English report with exact main HTML blobs, stable tags and line anchors](reports/2026-10-25-normalization-countability-and-cusp-current-pullback.md).

- **POME-NORM-COUNTABLE-COVER-001 — medium / confirmed proof-step error, not a false theorem:** Theorem 9.4.6, physical HTML line 157, assumes X globally has a countable basis although reduced complex spaces are defined locally and §5.2 explicitly allows uncountably many components. The uncountable disjoint union of discs gives a paracompact reduced complex space with no countable basis; its normalization is the identity. Remove the unnecessary countability/subcover/paracompactness inference and use the local analytic atlas and Hausdorff gluing already established. No original statement or permanent tag changed.
- **POME-PL-CUSP-RESTRICTION-001 — low / verified conditional deduction:** For cusp normalization \(\nu(t)=(t^2,t^3)\), Poincaré–Lelong and local-potential pullback give \(\nu^*[x=0]=2[0]\), \(\nu^*[y=0]=3[0]\); ambient holomorphic pullback orders belong to \(\langle2,3\rangle\), whereas weakly holomorphic t has order one. Pullback of the entire cusp divisor is inadmissible, as its potential becomes identically \(-\infty\). This checks the hypotheses and current normalization in §§5.5–5.6; earlier conductor findings unchanged.
- **Actual new coverage:** first selected integrated proof reading of §§5.5–5.6; incremental gluing/countability check in previously partially reviewed §9.4 and parametric-curve check in §9.5; §5.2 definition only. **No full section or upstream theorem chain certified.** All 747 ToC rows preserved.
- **Scope/writes:** only this audit report, cumulative ledger, selected section-matrix rows and LATEST on review/mathematical-audit; no main/source/registry/tag changes, tests, builds, CI, publication, formal proof or PR merge. User-deferred Demailly approximation/regularization, Bergman/L2/OT/multiscale/positivity-loss programme remains **deferred-by-user**, not reopened.

---

# 2026-10-25 — smooth full-mass toric limits fail total-variation convergence; moving convex-body lattice theorem

**Pinned main:** b6933b772f41b45918f7e25ed1afbbb1fd892272. **Session checkpoint:** 2026-10-24T20:00:00Z. **Report:** [Toric softmax and moving lattice bodies](reports/2026-10-25-toric-softmax-total-variation-and-moving-lattice-bodies.md).

- **POME-TORIC-SOFTMAX-TV-001 — low / verified conditional deduction:** \(F_t=t\log(1+\sum_i e^{x_i/t})\) converges *globally uniformly* to the simplex support function \(h_P=\max(0,x_1,\ldots,x_n)\); all real Monge–Ampère measures have full mass 1 on the **same** simplex slope body. Explicit positive smooth densities converge narrowly to \(\delta_0\) but stay at signed total-variation norm 2 from it. Printed §§21.5.1–4 correct; this is a sharp limit on strengthening topology, not a new error.
- **POME-LATTICE-MOVING-BODY-001 — low / verified conditional deduction:** exact lattice-cell sandwich \(K_{\delta_k+\sqrt n/k}\subset U_k\subset K^{\delta_k+(r_k+\sqrt n)/k}\) extends §21.7.3 uniformly in arbitrary translations to varying \(K_k\to K\) in Hausdorff distance, including lower-dimensional bodies. No unproved Okounkov or semigroup step is inferred.
- **Coverage:** all displayed selected proofs in §§21.5 and 21.7 reread and explicit strengthened results proved; previously inventory-only §§21.1 and 17.11 inspected **as introductory/convention pages only**, not proof-certified. §19.9 contextual only. All 747 existing matrix rows retained. No complete section or dependency chain certified.
- **Checks/writes:** local standard-library finite determinant checks n=1..8 and 1D lattice sanity checks k=100,400,1600 passed, *not* a project build/formal proof. Only an additive English report, arithmetic check, ledger/matrix/checkpoint on review/mathematical-audit; no main/source/registry/tag/CI/publication/merge. Demailly approximation/regularization and its dedicated Bergman/L2/OT/multiscale/positivity-loss programme remains **deferred-by-user**.

---

# 2026-10-25 — classical collar equation alias, sharp incidence threshold, nonclosed L2 range

**Fresh main:** b6933b772f41b45918f7e25ed1afbbb1fd892272; **preserved starting audit head:** 54d1a2a3bfd77ad8e789fd5485a95f3e2e8d8118. **Actual UTC checkpoint:** 2026-10-24T19:03:59.946Z. Freshly read current main AGENTS.md and documentation/proof-expansions.md, review README.md and prior LATEST.md/ledger/matrix; reconstructed the relevant sections from the main 747-section table of contents. [Full mathematical report with exact source labels, permanent tags, main blob SHAs, line anchors and proofs](reports/2026-10-25-classical-product-equation-alias-sharp-incidence-and-l2-closed-range.md).

- **POME-CLASSICAL-COLLAR-ALIGN-DUP-001 — medium / confirmed integration error:** Eq. 7.29.3 is **already complete as the second row of a two-row align** under tag 9135B1E39C61; its extra standalone alias F8A095BBD0A5 is wrongly exported as nested aligned/align TeX and duplicates the row. Fix the alias and standalone rendering without changing any permanent tag, provenance or valid mathematical estimate. Additional instance of the exporter-defect class previously found in §14.13–14.14, not a repeat of those original three occurrences.
- **POME-INCIDENCE-HAUSDORFF-SHARP-001 — low / verified conditional deduction:** Hausdorff exponent 2s+1 in §7.29.6 is optimal: a closed real-linear subspace of dimension 2s+1 intersects **every** rotated complex (n−s)-plane in a nonzero real line, so meets **every** positive-radius sphere even though its \(\mathcal H^\alpha\) measure vanishes for all \(\alpha>2s+1\). The printed lemma is correct; the proposed stronger bound is false.
- **POME-L2-UNREDUCED-NONCLOSED-001 — low / verified conditional deduction:** on complete flat \(\mathbb R\), f(x)=(1+x²)⁻¹ has no \(H^1\) primitive but is an \(L^2\) limit of derivatives of compactly supported smooth functions. Hence unreduced \(L^2\) cohomology in degree 1 is nonzero while reduced/harmonic degree 1 is zero. The closure bars in §2.21.5 are essential; printed corollary correct.
- **New proof-level coverage:** previously inventory-only §§2.19, 2.21 and 7.29. Directly checked selected projective/injective tensor norms and non-Hausdorff C(K×L) density, maximal Laplacian/reduced-complex arguments, and collar mass/weighted classical products and incidence. **No entire section or prerequisite chain certified.** §7.31 statements were contextual only; §7.31.1's Demailly/curvature-loss proof **not audited**.
- **Scope and writes:** only new report and additive ledger, 747-row matrix and this checkpoint on review/mathematical-audit; main/source/registry/tags/website unchanged; no build/tests/CI/publication/formalization/merge. All previously deferred-by-user approximation/regularization, Bergman, L², Ohsawa–Takegoshi, multiscale and positivity-loss programmes remain **deferred-by-user**, not reopened or certified.

---

# 2026-10-25 — Stein open unions have no psh exhaustion; homogeneous replacement dependency

**Fresh main:** b6933b772f41b45918f7e25ed1afbbb1fd892272; **preserved starting audit head:** e48a94aa1a6fcde1518d433c1ab504904e687c5c. Freshly read main AGENTS.md and documentation/proof-expansions.md, review README.md, previous LATEST.md, ledger and actual current 747-section ToC matrix. [Detailed source-anchored mathematical report](reports/2026-10-25-stein-union-psh-obstruction-and-local-homogeneous-dependency.md).

- **POME-STEIN-UNION-NO-PSH-EXHAUST-001 — low / verified conditional deduction:** Example 9.27.1's non-holomorphically-convex increasing Stein union admits **no psh exhaustion at all**, even without continuity or smoothness: the compact set K bounds every psh function along escaping holomorphic discs with boundary in K. This strengthens, not refutes, the example.
- **POME-HOLOCONV-PSH-EXHAUST-BRIDGE-001 — low / verified repair proposed only:** exact acyclic elementary manifold proof for the smooth psh-exhaustion input used in Theorem 9.26.1; existing Prop. 9.32.8 is a broader, distinct internal theorem, not a duplicate for deletion.
- **POME-HOM-DIRICHLET-SMOOTH-EXT-001 — medium / external dependency:** Lemma 15.7.1 uses smooth Guan–Li Dirichlet existence for a possibly nonclosed Hermitian background. Internal Thm 7.9.2 proves only a continuous / local C1,1 closed-background version; it is **not** a matching replacement. Remaining Steps of 15.7.2 were checked conditionally; no false theorem established.
- **Actual new coverage:** first selected integrated proof reading of §§9.26–9.27 and §15.7; §9.32.8 matched as a dependency, §15.8.4–6 and the **post-continuity** half of §15.8.1 checked conditionally. §§15.5–6, §15.8.1's regularization-based continuity and all dedicated Demailly/Bergman/L²/OT/multiscale/positivity-loss work remain **deferred-by-user**, not solved/certified.
- **Scope:** no source/body/registry/tag/main changes, no tests, builds, CI, publication, formalization or PR merge; sections not wholly certified.

---

# 2026-10-25 — capacity-weight uniform-bound necessity and zero-volume model boundary

**Freshly reviewed main:** b6933b772f41b45918f7e25ed1afbbb1fd892272; **preserved starting review head:** 0d4c742dbf33e1a714b9426ebbacde9c3a5ff165. Freshly read main AGENTS.md and documentation/proof-expansions.md, review README.md, prior LATEST.md, ledger and the 747-section coverage matrix, then inspected current integrated §§13.12 and 13.27 with an exact §18.4.8 dependency check. [Full source-anchored English report](reports/2026-10-25-capacity-weight-bound-and-zero-volume-boundary.md).

- **POME-CAP-WEIGHT-UNIFORM-BOUND-SHARP-001 — low / verified conditional deduction:** smooth nonnegative approximate identities on \(\mathbb P^1\) converge to zero in global big-class capacity while their weighted fixed smooth measures converge to a Dirac measure. Explicit Riesz–Jensen small-ball capacity bound. This confirms the **uniform boundedness of the weights** in Theorem 13.12.8 is genuinely necessary; it does not refute the theorem.
- **POME-MODEL-ZERO-VOLUME-BOUNDARY-001 — low / verified conditional deduction:** rational one-pole analytic ordinary models \(p_a\) on \(\mathbb P^1\) satisfy \(L(p_a)=U(p_a)=1-a\) and \(d_\theta(p_a,p_b)=|a-b|\). The \(a_j=1-1/j\) family is \(d_\theta\)-Cauchy but has no limit in \(\mathcal M_+(\theta)\), clarifying the reciprocal-mass condition of Theorem 13.27.4; the printed theorem remains correct.
- **Actual new coverage:** selected proofs and exact source anchors for previously inventory-only §§13.12 (capacity comparison, monotone directed nets, weighted continuity) and 13.27 (nonmetric triangle example, volume continuity, chain metric, completion). §18.4.8 only a prerequisite statement; no full section or upstream chain certified. No new confirmed errors or proof gaps.
- **Writes/limits:** dated report plus additive cumulative ledger/matrix/checkpoint only, exclusively on review/mathematical-audit; no main/source/registry/tag edits, CI, publication, build or formalization. Dedicated Demailly approximation/regularization and Bergman/L²/Ohsawa–Takegoshi/multiscale/positivity-loss work remains deferred-by-user, never reopened or certified.

---

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