# Mixed real Monge–Ampère mass, compact slope bodies, and lattice-count polarization

**Date:** 2026-11-20. **Status:** verified conditional deduction (low severity); **not** a printed theorem error, independent upstream-chain certification, or a claim of mathematical originality.  
**Finding:** `POME-REALMA-MIXED-SLOPE-COUNT-POLARIZATION-001`. **Audited production main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.

## Exact integrated reading-edition anchors

- `docs/sections/convex-analysis-and-toric-potentials--the-real-monge-ampere-measure/index.html`, blob `7089aa41ae2422b1bd6b5094e46668cbc8ed37be`, all mathematical lines 6–160. In particular Theorem 21.5.1, source `foundations-of-pluripotential-theory:4A0FAEB3`, permanent tag `409656CC47D4`, lines 10–41; Theorem 21.5.2, source `6403CF44`, tag `F4072D9ED060`, lines 43–87; Proposition 21.5.4, source `EAD83A50`, tag `5D8A7A7D734E`, lines 98–160; polarization (21.5.5), source `24CC29A7`, tag `D38381F0AC43`, lines 143–148.
- `docs/sections/convex-analysis-and-toric-potentials--compact-convex-envelopes-and-full-mass-limits/index.html`, blob `b3b4e34fff767a717df812a381f905589b257fb3`, all mathematical lines 6–49; compact-domain closed infimum/attainment Lemma 21.6.1, source `30FFD831`, tag `FCDAD9CEC8CE`, lines 10–30; finite-measure tightness Lemma 21.6.2, source `55EDF0D7`, tag `F2FABB0A312F`, lines 32–48.
- `docs/sections/convex-analysis-and-toric-potentials--lattice-points-and-volume/index.html`, blob `5d209b7f4d2156c19bc3fb300303405df6321230`, all mathematical lines 6–108; Hausdorff/volume Proposition 21.7.2, source `5E9AEE47`, tag `EDD78BC61BD7`, lines 27–55; translated lattice-count Theorem 21.7.3, source `364BCD30`, tag `831AEEB7084F`, lines 57–91; Corollary 21.7.4, source `D6B87DCB`, tag `CF4226A5034F`, lines 93–107.
- **Selected prerequisite only (not a whole-section audit):** `docs/sections/convex-analysis-and-toric-potentials--slope-bodies-and-bounded-growth/index.html`, blob `56a9a1c19e7234e2aa258d5ad1b66a5679ace190`, Definition 21.4.1, source `CF692075`, tag `E8746DA689A7`, lines 10–16; Proposition 21.4.2, source `67A1B562`, tag `D6E7C0B06FAD`, lines 19–54, including the precise compact-slope Minkowski equality.

All direct checks used the actual integrated HTML, including replacement proofs and their internal links, not only theorem titles or source labels. The 2026-11-18 finite-k lattice discrepancy finding and 2026-11-17 higher-Wasserstein endpoint finding remain distinct and are **not** re-counted.

## Conditional theorem and complete deduction from identified Pome statements

Let `n >= 1`. Let `F_1,...,F_n` be finite convex functions on `N_R` whose **closed slope bodies** `K_i := closure(dom F_i^*)` are compact convex nonempty subsets of `M_R`; lower-dimensional bodies are allowed. Let `MA_R` use exactly the `n!` convention of Theorem 21.5.1 and Proposition 21.5.4. Put `K_J := sum_{j in J} K_j`, with `K_empty = {0}`. Then

\[
\boxed{\operatorname{MA}_{\mathbb R}(F_1,\ldots,F_n)(N_{\mathbb R})
=\sum_{J\subseteq\{1,\ldots,n\}}(-1)^{n-|J|}\operatorname{vol}(K_J).}\tag{A}
\]

The right side is **finite and nonnegative**, including when individual bodies have empty interior. For every choice of lattice translations `a_k` (one common translation in each alternating summand), Theorem 21.7.3 further gives

\[
\boxed{\operatorname{MA}_{\mathbb R}(F_1,\ldots,F_n)(N_{\mathbb R})
=\lim_{k\to\infty}\frac{1}{k^n}
\sum_{J\subseteq\{1,\ldots,n\}}(-1)^{n-|J|}
\#\bigl(kK_J\cap(M+a_k)\bigr).}\tag{B}
\]

The same limit remains valid if **each** `kK_J` is replaced by its outer `r_{J,k}`-parallel body where every `r_{J,k}>=0` and `r_{J,k}/k ->0`; only finitely many `J` occur. This includes a zero-dimensional `K_J` for the empty subset: its normalized count is at most `k^{-n}`, while its volume is zero for `n>0`.

### Proof

1. Proposition 21.4.2 proves `K_{F+G}=K_F+K_G` when `K_F` is compact; its proof at the anchored lines explicitly uses the compactness needed to interchange the closure and the Minkowski sum. The conjugate scaling identity `(tF)^*(p)=tF^*(p/t)` for `t>0` yields `K_{tF}=tK_F`. Thus every finite nonempty sum `F_J=sum_{j in J}F_j` has compact slope body `K_{F_J}=K_J`, by induction. For `J=empty`, `F_J=0`, so `K_{F_J}={0}`.
2. By Theorem 21.5.1, `MA_R(F_J)(N_R)=n! vol(K_J)`; these masses are finite by compactness, so alternating sums have **no** indeterminate `infinity - infinity` terms. Integrate the actual reading-edition polarization formula (21.5.5) from Proposition 21.5.4 over the whole space. The factor `1/n!` there cancels the factor `n!` in each diagonal mass, proving (A). Proposition 21.5.4 supplies positivity of the mixed measure, proving the otherwise nonobvious nonnegativity of the finite difference of volumes. No appeal to an unproved mixed-volume polynomial theorem is needed.
3. For each of the finitely many compact convex sets `K_J`, apply Theorem 21.7.3 with constant weight `f=1` and `r_k=0`; the theorem explicitly permits empty interior and arbitrary translated lattices uniformly. Hence `k^{-n}#(kK_J intersect (M+a_k)) -> vol(K_J)` for each `J`. Taking their finite alternating sum and applying (A) gives (B). The sublinear outer-thickening variant follows from the same theorem for each `J`.

This establishes a direct audit bridge between the Alexandrov dual-pushforward normalization, mixed-measure polarization, compact-domain Legendre/Minkowski bookkeeping, and geometric lattice counts. If one **additionally** invokes the classical convention for mixed volume `V`, formula (A) reads `MA_R(F_1,...,F_n)(N_R)=n! V(K_1,...,K_n)`; that identification is **not** used as an external premise in this proof.

## End-to-end checks of the three sections

- **§21.5:** Verified the need for completed Lebesgue measurability (the exceptional nondifferentiability set in dual space is null), the distinctions between vague and narrow convergence, the local-Hessian `C^{1,1}` dominated-convergence argument, positivity of polarization limits, and the exact `n!` / `1/n!` cancellation. No newly confirmed false printed statement or internal proof gap identified. The already documented higher-Wasserstein limitation remains separate.
- **§21.6:** Checked compact-domain infimum attainment and lower semicontinuity including zero barycentric weights; checked the use of total-mass convergence and tightness to upgrade vague to narrow convergence. Neither check requires reopening any excluded analytic regularization.
- **§21.7:** Checked support-function/Hausdorff equality, boundary-zero-volume for degenerate convex bodies, half-open fundamental-cell inclusions, translations `a_k` of arbitrary size, `o(k)` boundary error, and the dimension-zero exception. No new printed error; the existing 2026-11-18 *finite-k* discrepancy refinement was not repeated.

**Classification:** `POME-REALMA-MIXED-SLOPE-COUNT-POLARIZATION-001` — **low / verified conditional deduction**. This is *not* a false theorem, correction of a missing proof, or certification of upstream sections 21.2–21.4/2.2/2.8/5.3. **Suggested source change:** optionally insert (A)–(B) as a cross-reference after Proposition 21.5.4 or Theorem 21.7.3 **in a separate reviewable patch only**; no main/registry/tag/source edit here. **Affected potential dependents:** geometric mixed-volume and toric section-growth comparisons (§21.9.5); this does **not** independently prove any real-to-complex Monge–Ampère identification or the analytic arguments of §21.12.

## Audit boundaries

**New full direct readings:** three current sections §§21.5–21.7, not a claim of first-ever visits (historical matrix statuses were not fully reconciled). **Selected prerequisite:** §21.4.2 only. **Fully independently certified upstream proof chains:** zero. No builds, tests, CI, website publication or source writes. All user-excluded Demailly approximation/regularization, Bergman/L²/Ohsawa–Takegoshi/multiscale/positivity-loss programmes stay **deferred-by-user**, not resolved or certified.
