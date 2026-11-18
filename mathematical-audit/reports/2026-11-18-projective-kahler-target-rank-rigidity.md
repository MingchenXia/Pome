# Complete direct review of §10.75 and Kähler-target rigidity for projective-space maps

- Date: 2026-11-18.
- Finding ID: **POME-CPN-KAHLER-TARGET-RANK-RIGIDITY-001**.
- Severity: **low**; status: **verified conditional deduction**. Both printed §10.75 results are correct under their expressly cited inputs. No false original theorem or missing proof is alleged.
- Current production main reviewed: **b6933b772f41b45918f7e25ed1afbbb1fd892272**.
- Actual integrated text: **docs/sections/spectral-sequences-support-and-cup-products--the-integer-cohomology-ring-of-projective-space/index.html**, main blob **cb90abebae459659c273b9de67848f3feded35e3**.
- Section 10.75: original source **demailly-complex-geometry:B117AD24**, permanent section tag **D599A476FAC0**, physical lines 5–13. Lemma 10.75.1: original **demailly-complex-geometry:1EB6C39D**, permanent **419BAFBD0FA6**, hypothesis and conclusion at lines 17–21, complete proof at lines 26–42. Theorem 10.75.2: original **demailly-complex-geometry:FF8EE3A7**, permanent **0CD4D885B4B4**, statement and signed comparison at lines 47–55, complete proof at lines 60–80.
- Context only: §10.40 (integral Chern class/curvature, main blob **281267b7fbf079fde2fbc5060294ff338bd11085**), §10.50 (normalized Fubini–Study volume, blob **a45ae3fefbf6746eca800f490163ac7ce2456c07**), §10.58 (multiplicative real/de Rham comparison and sign, blob **635f86f3f9848c1bf3f53af96067eac42d63f892**), §10.71 (oriented cap duality, blob **88ed77871455097c456cafaba2cca34986f3a3fb**). These contextual sections are **not** fully certified by this run.
- User-deferred work: Demailly approximation/regularization and its dedicated Bergman, L², Ohsawa–Takegoshi, multiscale-atlas and positivity-loss completion programmes are entirely outside this review.

## Direct audit of the two printed results

**Lemma 10.75.1 (integral groups).** Take a hyperplane H=P^(n−1) in P^n. Its complement is C^n. The cited relative/support comparison identifies H^q(P^n,H;Z) with compactly supported H^q(C^n;Z), which integral orientation/cap duality identifies with Z only for q=2n. The long exact sequence therefore identifies H^q(P^n;Z) with H^q(H;Z) below 2n−1, annihilates degree 2n−1 and identifies the degree-2n group with Z. Induct from P^0. Iterated linear-hyperplane inclusions yield exactly the asserted restriction isomorphisms. The endpoint n=0 and torsion are handled integrally, not inferred from real cohomology. **No error was found in physical lines 26–42.**

**Theorem 10.75.2 (integer ring and signs).** Write h=c_1^Z(O(1)) using the project's specified positive-connecting Chern-class convention and write ω for the normalized Fubini–Study form, with ∫_(P^k)ω^k=1. The project's multiplicative augmentation comparison Θ is *not* the ordinary unsigned identification: its positive inverse comparison Ψ satisfies
\[
 \Theta_q^{-1}=\epsilon_q\Psi_q,\qquad
 \epsilon_q=(-1)^{q(q+1)/2},\qquad
 \Theta_2(h_{\mathbb R})=-[\omega].
\]
Multiplicativity and ε_(2k)=(-1)^k give
\[
 \Theta_{2k}(h_{\mathbb R}^{k})=(-1)^k[\omega^k],
 \qquad \operatorname{tr}_{\mathbb P^k}(h^k)=(-1)^k.
\]
The latter is ±1, hence h^k is primitive in the integral degree-2k group; linear restriction transfers primitivity to P^n. These primitive powers exhaust the nonzero integral groups. All higher powers vanish by degree, establishing Z[h]/(h^(n+1)), including n=0. The **positive de Rham generator is −h**, not h, in this project's Θ convention. Reversing that sign would incorrectly contradict physical lines 69–79. **No error was found in the theorem or its entire printed proof.**

These checks are direct proof audits **conditional** on the separately printed integral cap-duality, support comparison, functorial multiplicative cup product, Chern-class normalization, and ∫ω^k=1. They do not certify those whole upstream sections.

## New consequence: nonconstant maps from P^n to Kähler targets cannot drop rank or have positive-dimensional fibers

**Precise theorem.** Let n≥1, let (Y,η) be a compact Kähler manifold of arbitrary dimension, and let f:P^n→Y be holomorphic. Either f is constant, or:

1. There is a **strictly positive real c** such that [f*η]=c[ω_FS] in H²(P^n,R).
2. Its differential has rank n on a nonempty open set; equivalently, the analytic image has dimension n.
3. Every fiber is finite. In particular, if dim_C Y<n then every such holomorphic map is constant.

This is **not** the earlier 2026-11-12 graph/diagonal intersection calculation for self-maps of P^n. It applies to **any compact Kähler target** and establishes a dimension/fiber obstruction, rather than computing a graph class or re-reporting a degree.

**Complete proof.** By the degree-two case of the integrated integral ring (and real coefficient extension), [ω_FS] spans H²(P^n,R). Thus [f*η]=c[ω_FS] for a unique real c. Because f*η is a semipositive smooth (1,1)-form,
\[
 c=\frac{\int_{\mathbb P^n}f^*\eta\wedge\omega^{n-1}}
          {\int_{\mathbb P^n}\omega^n}\ge0.
\]
At every point, the trace of f*η with respect to ω is nonnegative and is positive precisely where df≠0, since η is positive definite. If f is nonconstant, df≠0 somewhere and on a nonempty open set, so the integral is strictly positive and c>0.

Cohomological multiplicativity and closedness of η and ω now imply the **strict** top-degree identity
\[
 \int_{\mathbb P^n}(f^*\eta)^n
   =c^n\int_{\mathbb P^n}\omega^n=c^n>0.
\]
If rank(df)≤n−1 everywhere then (f*η)^n vanishes pointwise, contradiction. The maximal-rank locus is open and nonempty. If dim_C Y<n the rank is everywhere ≤dim_C Y<n, forcing f to be constant.

For the assertion about fibers, suppose that f^{-1}(y) has an irreducible positive-dimensional component V of pure dimension q≥1. It is a compact analytic subvariety of P^n. On its smooth locus f*η vanishes on all tangent vectors, hence
\[
 0=\int_V f^*\eta\wedge\omega^{q-1}
   =c\int_V\omega^q>0.
\]
The equality uses the cohomological identity on the closed integration current [V] and Stokes; the strict inequality is positivity of the Fubini–Study volume on V. This contradiction excludes every positive-dimensional fiber. No projective algebraicity or resolution theorem is needed for the numerical argument; the standard analytic-subvariety integration current is a stated internal prerequisite, not independently re-proved here.

**Sharpness / boundary.** The identity f=id:P^n→P^n has maximal rank n and realizes the boundary dim_C Y=n. For n≥2 the rational linear projection
\[
 [Z_0:\cdots:Z_n]\dashrightarrow[Z_0:\cdots:Z_{n-1}]
\]
is nonconstant but has a base point and is **not** a holomorphic map on all P^n: the holomorphic hypothesis cannot be dropped. No new self-map degree formula is counted; the earlier POME-PROJ-GRAPH-DIAGONAL-INTEGRAL-SIGNS-001 remains a distinct, already registered computation.

## Classification, correction, dependents, coverage

- Status: **verified conditional deduction**; severity **low**; **no printed error / no proof gap / no actual canonicalization defect**. The two printed §10.75 statements and their full local proof arguments survive scrutiny.
- Proposed optional addition (not performed): place a clearly labeled corollary after Theorem 10.75.2 stating Kähler-target dimension and finite-fiber rigidity, retaining its positivity-of-pullback and analytic-cycle inputs. Never overwrite the source or permanent tags.
- Affected potential users: any later use of holomorphic projective-space maps and projective/flag constructions (§§9.59, 10.40, 19.9) may cite the new rigidity consequence if it needs it; no existing dependent is claimed to be false. Distinguish real positive [ω] from the project's signed integral generator h in any cohomological comparison.
- Actual main TOC: **25 chapters, 747 numbered sections**. §10.75 was **previously context-read** in the November 12 graph audit, so newly first-visited numbered sections: **0**. Full direct proof-level section inspections newly completed: **1 (§10.75)**. Fully certified transitive dependency chains: **0**. Contextual §§10.40, 10.50, 10.58, 10.71: **not** newly certified.
- No tests, builds, GitHub Actions, publication or source/body/registry/tag/main changes are asserted. The excluded programmes remain **deferred-by-user**, not resolved.
