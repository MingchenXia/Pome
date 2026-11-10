# Mathematical audit: noncompact projective complements contain escaping compact projective fibers

**Finding:** `POME-PROJ-COMP-BASE-ESCAPING-COMPACT-FIBERS-001` — **high / confirmed error** in the *unqualified noncompact scope* of printed Theorem 11.18.2. This is an actual counterexample to the stated conclusion, **not merely a gap in its published exhaustion construction**. The theorem is valid with the added hypothesis that the base (X) is compact, using the displayed proof. A downstream corollary is dependent on the theorem but is **not itself refuted by the example**.

**Reviewed production main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272` (rechecked 2026-11-11). **Audit branch before writing:** `79e5084fc4507ef7996d4c6cce06fe5dc877fd00`. **Current ToC:** 25 chapters, 747 numbered sections; zero fully mathematically certified. We only audited selected statements, not whole sections.

## Actual integrated reading and stable anchors

1. `docs/sections/gauduchon-metrics-and-linear-mass--convex-norms-and-gauduchon-degrees--curvature-and-projective-complement-exhaustions/index.html`, main blob `fab309d460a8411fefcd1ef32a094927d6feea10`: standing assumptions lines **10–25**, Lemma **11.18.1** lines **29–45**, source `non-kahler-pluripotential-theory:F8D5B741`, permanent tag `5022159B8350`; Theorem **11.18.2** lines **51–68**, source `non-kahler-pluripotential-theory:9BF81039`, permanent tag `B93CB03C68B7`. Its text says `E -> X` is a holomorphic rank-`r` bundle with (n\geq1) and imposes no compactness hypothesis; its proof uses "**Since the ambient projective bundle is compact**" at physical line **67**. Corollary **11.18.4** lines **91–105**, source `non-kahler-pluripotential-theory:B119F64B`, permanent tag `18D33491ABFD`, invokes this theorem.
2. `docs/sections/gauduchon-metrics-and-linear-mass--convex-norms-and-gauduchon-degrees--concave-neighborhoods-and-dual-norms/index.html`, main blob `d49b7d4f2a213c8b70abfe2f337562202bb58dfb`, physical line **129**: an (N)-fold is (q)-convex if it has a smooth exhaustion with at least (N-q+1) strictly positive Levi eigenvalues **outside a compact set**. The definition is not a global strictly-PSH requirement.
3. `docs/sections/gauduchon-metrics-and-linear-mass/index.html`, main blob `02d635e918120c4026c38d14119db9377eefe61f`, line **7**: chapter-wide convention fixes a Hermitian form and (n\geq2), *not* compactness; §11.18 explicitly chooses (n\geq1). `docs/sections/conventions/index.html`, main blob `ef778e54d8d7413242387e95c52269b3c7d42cae`, physical lines **11, 23**: spaces/manifolds are paracompact/Hausdorff, not assumed compact.

## Counterexample: positive curvature in (d) independent directions, (2)-convexity fails

Fix any integer (d\geq2) and set
[
B=\mathbb P^d,qquad X=B\times\mathbb C,qquad
n=d+1,qquad E=\operatorname{pr}_B^*\mathcal O_{\mathbb P^d}(1),qquad r=1.
]
Equip (E) with the pullback of its standard positive Fubini–Study Hermitian metric (h). Its Chern coefficient form satisfies
[
\alpha_{h,v}=\mathrm i,h(F_hv,v)=h(v,v)\operatorname{pr}_B^*\omega_{\rm FS}
]
up to the fixed positive normalization of (omega_{\rm FS}) in §11.18. Indeed in the affine chart (mathcal O(1)) has squared frame norm (h(e,e)=(1+\lVert z\rVert^2)^{-1}); the printed (F_h=\bar\partial(h^{-1}\partial h)) gives
(mathrm iF_h=mathrm i\partial\bar\partial\log(1+\lVert z\rVert^2)>0) on (mathbb P^d).
Thus for **every** (x\in X) and (v\ne0), (alpha_{h,v}) has exactly (s=d) positive eigenvalues, and zero in the (mathbb C)-direction. All hypotheses of Theorem 11.18.2 hold, including (0\leq s\leq n).

That theorem asserts that
[
U_E=\mathbb P(\mathcal O_X\oplus E)\setminus\mathbb P(\mathcal O_X)
]
is (q=(n+r-s)=(d+1)+1-d=2)-convex. Its complex dimension is (N=n+r=d+2), hence a purported (2)-convex exhaustion must have **at least (N-1=d+1) strictly positive Levi eigenvalues** outside one compact set (K\subset U_E).

The infinity divisor (Z=\mathbb P(E)\subset U_E) is closed and is canonically isomorphic to (X) since (r=1). For each (t\in\mathbb C), the fiber
[
Y_t=\mathbb P(E)|_{\mathbb P^d\times\{t\}}
\simeq\mathbb P^d
]
is a compact complex submanifold of (U_E), of complex dimension (d). They **escape every fixed compact subset** of (U_E): the projection (U_E\to\mathbb C) has compact image on (K), so choose (t) outside that image. This escape argument is essential because the definition only asks for Levi positivity outside (K).

Suppose a smooth real exhaustion (psi) gave the claimed (2)-convexity. Choose (t) with (Y_t\cap K=\varnothing). The restriction (psi|_{Y_t}) attains a maximum at some (p\in Y_t). Its Levi form at (p) is **negative semidefinite on the (d)-dimensional complex tangent space** (T_p^{1,0}Y_t). Every positive definite subspace for (mathcal L_psi(p)) meets (T_p^{1,0}Y_t) trivially, hence has dimension at most
[
\dim_\mathbb C U_E-\dim_\mathbb C Y_t=(d+2)-d=2.
]
But (2)-convexity requires (d+1\geq3) positive eigenvalues at (p\notin K). **Contradiction**. The theorem's asserted conclusion is false for every (d\geq2). No regularization, analytic PDE input or external vanishing theorem is used.

## Precise correction, affected dependents, and status

**Proposed source-body correction (NOT applied):** insert "**Assume in addition that (X) is compact**" before the curvature hypothesis in Theorem 11.18.2. With compact (X), the ambient projective bundle is compact; its cutoff function (psi=\chi(G)/G) tends to (+\infty) on approach to the removed zero section and its finite sublevels are compact. Lemma 11.18.1 gives the required (s+1) positive Levi directions near that removed section, so the printed argument then establishes the corrected theorem. The corrected case is a **verified repair**, not a justification of the original noncompact claim.

**Impacted dependencies:** Corollary 11.18.4 (permanent tag `18D33491ABFD`) applies the theorem and should state/receive the compactness condition for its first, pointwise-mean-curvature clause; its Hermitian–Einstein stable-bundle clause uses an additional quoted compact-manifold existence input. Corollary 11.18.5 works over the compact Hirzebruch surface and is unaffected by this counterexample. Definition 11.18.3 integrates over (X); on noncompact (X), degree may also require a separately specified convergence assumption, but this is **not needed** for the counterexample. Lemma 11.18.1 is a correct local differential calculation; no defect is alleged there.

**Reclassification:** prior `POME-PROJ-COMP-BASE-PROPER-001` (2026-10-23, **proof gap**) established only the failure of the printed cutoff to be proper when (X) is noncompact and explicitly did **not** disprove the theorem. The present escaping-family argument upgrades the **theorem itself** to **confirmed error** for the noncompact scope. Preserve that prior record as historical evidence, linked to this stronger finding; do not silently rewrite or erase it.

**Coverage:** newly examined explicit projective-line-bundle model and the full logical obstruction at §11.18.2, with the exact §11.17 (q)-convexity definition and chapter/global scope checked. Both sections had been partly audited, so **0 new first-visited numbered sections; 0 whole-section certifications**. No tests, build, formalization, CI, website publication, other-source or main edits. The owner-excluded Demailly approximation/regularization and dedicated Bergman, L², Ohsawa–Takegoshi, multiscale-atlas and positivity-loss programme remain **deferred-by-user**, not resolved or certified.
