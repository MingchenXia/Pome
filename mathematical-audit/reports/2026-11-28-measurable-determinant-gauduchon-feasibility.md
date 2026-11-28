# Measurable determinant constraints and exact Gauduchon feasibility

Date: 2026-11-28. Reviewed main: `b6933b772f41b45918f7e25ed1afbbb1fd892272`. Audit starting head: `df12374537b6e96708c25cc414a326a8340daebd`.

## POME-GAUDUCHON-MEASURABLE-DETERMINANT-FEASIBILITY-001
Severity: low. Status: verified conditional deduction (optional strengthening, not a false printed theorem). No production patch.

### Anchors and scope
- `docs/sections/determinant-bounds-and-gauduchon-separation/index.html`, blob `21ee4c9d517250bec607fa5ebd5630b41a7bd658`: all mathematical lines 7–117. Lemma 10.97.1, permanent EFEC3AC4D264 / source 6F0D5B86, lines 11–40; Proposition 10.97.4, permanent 970E2C8817B1 / source 538E99DD, lines 45–112; Remark 10.97.9, line 117.
- Internal prerequisites checked at `docs/tag/BB19C89586B1/index.html`, blob aa42e5bf0d65db9ad907894ecb67f7f17659f1d9, Lemma 7.8.1 lines 6–27 (matrix trace duality); `docs/tag/88BE3B63D9E5/index.html`, blob dcb20d8ae494fd3003a0730adba1dd8a18ecaca3, Theorem 11.6.1 lines 37–57 (distributional potential from annihilator); `docs/tag/3978AEB15BD7/index.html`, blob 2b016d68ceb8cbe86cb052e58754efb9339af300, Theorem 11.4.2 lines 6–41 (conformal Gauduchon representative). These retain the existing elliptic Fredholm, maximum principle and weak compactness inputs; no transitive certification.
- Selected downstream check: `docs/sections/transcendental-morse-inequalities/index.html`, blob 8c3b365abcfd969b94e36611e28d6b87dfddc45b, Theorem 10.98.2 permanent DE32EEA596CD, lines 39–135. The concentration/regularization input at line 37 is deferred-by-user insofar as it invokes excluded regularization; it is assumed and not reopened. The smooth equation input and volume comparison at lines 7–11, 60–67, 137 are not independently certified. The trace estimates (10.98.6–8) use Cauchy–Schwarz and the mixed-wedge identity; the lower bound m_j²/B≥B−2/j is valid for j>B⁻¹. Taking j→∞ against each fixed cutoff before k→∞ is justified. The nef passage keeps the difference class fixed, requiring only continuity of intersections. The proof invokes Proposition 10.97.4 exactly with its smooth positive density hypothesis.

### Exact criterion
Let X be compact connected complex of dimension n≥2, ψ a smooth closed real (1,1)-form, dV a smooth positive volume form, and q≥0 in L¹(dV). Put
`C_q={T≥0 : (T_ac)^n ≥ q^n dV a.e.}`,
where the wedge denotes the pointwise determinant of the absolutely continuous coefficients, not a product of currents. In particular q^n need not be integrable. Then the following are equivalent:

(i) There exists a positive closed current R=ψ+dd^c u, u a real distribution, in C_q.
(ii) For every smooth Gauduchon metric χ,
```
∫_X ψ∧χ^(n−1) ≥ ∫_X q (χ^n/dV)^((n−1)/n) dV.
```

The feasible set of R in (i), when nonempty, is weakly compact and convex. If equality holds in (ii) for any single χ, the feasible current is unique, is absolutely continuous, and is necessarily
`R=q (dV/χ^n)^(1/n) χ`.
In particular this explicit current must be closed. No existence is claimed from a single test.

### Proof
Write T in a chart as a positive matrix measure M with density A relative to Lebesgue measure. If dV is expressed in that frame, write h for its positive smooth determinant-normalized density (including the wedge normalization). The exact same test as (10.97.3), with h^(1/n) replaced by q h^(1/n), expresses the condition det A≥q^n h as weakly closed linear half-spaces. The right side is locally finite by q∈L¹. The forward direction follows from trace duality and positivity of the singular part. In the reverse direction take the absolutely continuous densities of the measure inequalities, first for a countable dense collection of constant positive B; outside their common null set take the infimum over all B. This proves convexity and weak closedness for nets, as well as stability under removal of the singular part or addition of a positive current. The set is nonempty: relative to any smooth Hermitian χ the L¹ form Tχ=q(dV/χ^n)^(1/n)χ is positive and has determinant exactly q^n dV a.e.

For necessity of (ii), diagonalize R_ac with respect to χ. The pointwise AM–GM inequality gives R_ac∧χ^(n−1)≥((R_ac)^n/χ^n)^(1/n)χ^n≥q(χ^n/dV)^((n−1)/n)dV. The singular trace is nonnegative, and the total trace equals the trace of ψ by distributional integration by parts. For sufficiency Tχ attains exactly the right-hand trace, so (ii) supplies the auxiliary current required by the separation proof of 10.97.4 with C_q replacing C_ν.

For completeness, F=ψ+im dd^c is weakly closed by the annihilator identity of 11.6.1, whose construction works for arbitrary real currents. Fix Γ₀=χ₀^(n−1) strictly positive and dd^c-closed by 11.4.2. All S∈F have the same Γ₀ pairing. If a net W_a=T_a−S_a in C_q−F converges weakly, the Γ₀ mass of the positive T_a is eventually bounded; a subnet converges weakly to T∈C_q and S_a converges along it to T−W∈F. Thus C_q−F is closed. If 0 is absent, strict separation yields smooth σ and c>0 with ⟨T−S,σ⟩≥c. Arbitrary affine variations in S give dd^cσ=0, and positive additions to T give σ≥0. For small ε>0, σ+εΓ₀ is strictly positive dd^c-closed, and ⟨T−ψ,σ+εΓ₀⟩≥c−ε⟨ψ,Γ₀⟩>0 uniformly in T. By the positive root construction it equals χ^(n−1) for a smooth Gauduchon χ. This contradicts the Tχ test. Hence the intersection is nonempty. The same fixed Γ₀ mass identity bounds all positive feasible currents; the intersection of the two closed convex sets is therefore weakly compact, including for nets.

If equality in (ii) holds for a metric χ, the nonnegative singular trace and the nonnegative a.e. trace deficit must both vanish. Strict positivity of χ kills the singular matrix measure. Where q>0, equality in AM–GM forces all eigenvalues of R_ac relative to χ to equal q(dV/χ^n)^(1/n); where q=0 the trace must be zero, so all eigenvalues vanish. Thus R=Tχ and uniqueness follows. This proof does not use regularization, nor does it form a non-pluripolar or Bedford–Taylor product for R.

### Consequences and limits
The original smooth ν criterion is recovered by q=(ν/dV)^(1/n). For q=0 the result recovers the closed-background positivity criterion, not a replacement for the more general nonclosed-background Lamari theorem. The measurable extension includes q with q^n not integrable; no finite volume bound or identification with a non-pluripolar measure is asserted. In the Kähler setting, any additional theorem bounding the integrated determinant must still have its own hypotheses checked. No new external input beyond the existing separation and elliptic prerequisites. Theorem 10.98.2 is a downstream application; its original smooth-density argument is unaffected.

## Actual coverage
Whole direct conditional §10.97; selected §10.98 lines 39–135 and the three internal tagged prerequisites above. The previous matrix rows for 10.97 and 10.98 were LEGACY-UNRECONCILED with no section-specific evidence; no historical first-visit claim. The chapter 10 TOC contains 109 numbered sections. No new confirmed theorem errors or demonstrated proof gaps; one optional deduction; no full upstream proof-chain certification. All excluded Demailly approximation/regularization, dedicated Bergman/L²/Ohsawa–Takegoshi/multiscale/positivity-loss work remains deferred-by-user. No build, tests, CI, main/source/registry/permanent tag edits or publication.
