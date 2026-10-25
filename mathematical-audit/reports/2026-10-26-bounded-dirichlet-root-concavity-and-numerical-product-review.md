# 2026-10-26 — root concavity for bounded Dirichlet data and selected numerical-product review

**Reviewed main:** b6933b772f41b45918f7e25ed1afbbb1fd892272.
**Starting audit head:** db2677f8d5620e138d2849d3f9c7111e1945b6d4.

## Exact integrated sources

1. Section 5.8: docs/sections/plurisubharmonic-functions--the-line-definition-and-upper-semicontinuity/index.html, main blob 7a23771b2b16ff8610174712a72ceb42fcf011ff. Lemma 5.8.2 (source foundations-of-pluripotential-theory-2FA9F6A1, permanent tag 3C70A4ABB14A), lines 18–54; Theorem 5.8.4 (source foundations-of-pluripotential-theory-68860CF1, tag 1A391017E17A), lines 66–102.
2. Section 7.9: docs/sections/bedford-taylor-products-and-local-capacity--the-ball-dirichlet-problem-with-continuous-density/index.html, main blob ff1d5dfff1913156b45875eabf921f60af553b99. Lemma 7.9.1 (source foundations-of-pluripotential-theory-89405657, tag 0FF4AFFE0ED0), lines 16–38; Theorem 7.9.2 (source foundations-of-pluripotential-theory-69935D4D, tag A092925717E1), lines 40–50 and subsequent proof.
3. Section 7.10: docs/sections/bedford-taylor-products-and-local-capacity--bounded-measurable-densities/index.html, main blob 762b841b0cb243784dc988f04dbf2779da66c469. Lemma 7.10.1 (source foundations-of-pluripotential-theory-74804636, tag C09E42A43E93), lines 10–35; Theorem 7.10.2 (source foundations-of-pluripotential-theory-9C25B561, tag C9116FCEFCD2), lines 37–109, in particular stability at 90–106.
4. Section 13.32: docs/sections/numerical-positive-products/index.html, main blob 60abb2fa549c5fc76d759af419f863fedace7cfd. Lemma 13.32.2 (source transcendental-positive-cones-314E95A0, tag 85B840A3A734), lines 30–44; Proposition 13.32.5 (source transcendental-positive-cones-49C0DE98, tag 37818757E0D6), lines 85–102; Proposition 13.32.6 (source transcendental-positive-cones-30448720, tag B28D656FB542), lines 104–128.

## POME-BT-DIRICHLET-JOINT-ROOT-CONCAVITY-001

**Severity/status:** low / **verified conditional deduction**; optional strengthening, not a false source theorem.

**Statement.** Let B=B(a,R) be a ball in C^n, n>=1. Let I be a finite nonempty index set, lambda_i>=0 with sum_i lambda_i=1. Let F_i be nonnegative bounded measurable functions on B and phi_i real continuous functions on its boundary. With U_{f,phi} denoting the unique bounded psh Dirichlet solution from Theorem 7.10.2, put F=sum_i lambda_i F_i and phi=sum_i lambda_i phi_i. Then

\[
\boxed{\quad \sum_i \lambda_i U_{F_i^n,\varphi_i}
\ \le\ U_{(\sum_i\lambda_iF_i)^n,\,\sum_i\lambda_i\varphi_i}
\quad \text{pointwise on } B.\quad}
\]

Thus the Dirichlet solution operator is jointly concave as a function of the **density root** F=f^{1/n} and the boundary datum phi. The interpolation coefficients are exact; equality holds for constant F_i=c_i and constant phi_i=d_i since

\[
U_{c_i^n,d_i}(z)=d_i+c_i(|z-a|^2-R^2),
\qquad dd^c |z-a|^2=\eta.
\]

**Proof.** Extend each F_i by zero outside B and convolve it with the same nonnegative approximate identity. Write F_{i,m} for the resulting continuous, nonnegative and uniformly bounded roots. They converge in L^1(B) to F_i. Because all roots are bounded by a common M, the elementary estimate

\[
|s^n-t^n|\le nM^{n-1}|s-t|,\qquad 0\le s,t\le M
\]

implies F_{i,m}^n -> F_i^n in L^1(B). Similarly, putting G_m=sum_i lambda_i F_{i,m}, one has G_m^n -> F^n in L^1(B), with a common uniform density bound.

Let u_{i,m}=H_{F_{i,m}^n,phi_i} be the continuous Dirichlet solutions supplied by Theorem 7.9.2. Applying Lemma 7.9.1 successively with c=0 shows that v_m=sum_i lambda_i u_{i,m} is a bounded psh subsolution whose Monge–Ampere measure dominates G_m^n eta^n. Its boundary values are phi. Hence, by the continuous-data Perron characterization,

\[
v_m\le H_{G_m^n,\varphi}.
\]

Theorem 7.10.2, applied to each uniformly bounded density sequence and to the corresponding G_m^n, gives convergence in L^1(B) to U_{F_i^n,phi_i} and U_{F^n,phi}, respectively. Thus the desired inequality holds almost everywhere in B. Both sides are bounded psh; their canonical subharmonic representatives are obtained from small-ball averages (Theorem 5.9.1, permanent tag 2A4F77263F48). Averaging the a.e. inequality and shrinking the ball upgrades it to the pointwise inequality. Direct substitution verifies equality for the displayed quadratic models, including n=1.

**Correction/dependents.** Propose an optional corollary following Theorem 7.10.2; do not change the printed theorem. Downstream uses include bounded-density Perron comparison and mixture subsolutions. The preceding proof uses the already integrated bounded Bedford–Taylor products and their comparison theorem *conditionally*, not a new proof of those foundations. It is distinct from existing ledger IDs POME-BT-FINITE-MINKOWSKI-001 (mixed-current inequality), POME-BT-DIR-SHARP-001 (supremum-norm estimate), POME-BT-L1CAP-001 and POME-BT-DIRICHLET-GLOBAL-CAP-001 (capacity stability). Those earlier findings are retained and are **not** repeated as new discoveries.

## Independent selected proof inspections

**§5.8 (first selected pass):** Lines 18–54: the support K_v lies inside an open union of transverse components, and compactness supplies a finite component subcover for applying positive distributional Laplacians to nonnegative slice test functions. Lines 66–102: the finite-valued case first obtains Borel measurability via disc averages and reverse Fatou, invokes the joint upper bound and the canonical subharmonic representative, and compares almost-everywhere on complex lines; truncation then treats extended-valued functions. The use of min(u,N) is solely as a bounded measurable integrand, **not** as a claimed subharmonic function. Corollary 2.9.28 and Theorem 3.4.12 remain conditional upstream inputs in this audit.

**§7.9–§7.10 (incremental):** The subsolution comparison direction and the passage from continuous approximating roots to bounded measurable solutions are compatible with the explicit proofs. This pass does not re-label the earlier global-capacity and mixed-product audit findings as new.

**§13.32 (first selected nonexcluded pass):** Lemma 13.32.2's simultaneous exceptional correction retains strict positivity even for t=delta_i, since S_{i,t}>=(delta_i-t)pi^*omega+t gamma>0; each finite mixed intersection is polynomial in t. Proposition 13.32.5 distinguishes convergence of *cohomological pairings* from convergence of chosen current representatives, and numerical suprema from an order-cofinality assertion on divisorial singularity types. Proposition 13.32.6's interior order squeeze is valid under the explicit assumption alpha-delta omega pseudo-effective, and finite-dimensional H^{1,1} is spanned by Kähler classes. These selected steps were checked; the upstream approximation existence and full positive-product mass-continuity chain were **not** certified.

**Deferred by express user request:** The strict gentle and analytic approximation proofs in Lemma 13.32.1 and Theorem 13.32.3, including any Bergman, L^2, Ohsawa–Takegoshi, multiscale or positivity-loss subprogramme, were not audited or extended. Their presence as logical dependencies of 13.32.5–6 is recorded only as deferred-by-user, not resolved. Hironaka principalization remains the expressly permitted quoted input. The use of Theorem 7.10.2's already established elementary density-mollification step is a dependency, not reopening the dedicated excluded research.

**Coverage limits:** Exact selected passages in §§5.8, 7.9–7.10 and 13.32 only. No whole section or transitive proof chain certified. No tests, builds, CI, publication, formal verification or mathematical source/body/registry/tag edits.
