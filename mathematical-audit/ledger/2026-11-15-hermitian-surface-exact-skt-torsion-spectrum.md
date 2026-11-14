# 2026-11-15 classified finding — complex-surface SKT torsion spectrum

- **Stable ID:** POME-HERM-SKT-SURFACE-EXACT-TORSION-SPECTRUM-001
- **Status:** verified conditional deduction; **severity:** low.
- **Theorem truth:** The printed Corollary 11.48.21 remains correct. This is a strictly sharper surface-specific sufficiency estimate, **not a counterexample** and not a complete analytic proof repair.
- **Reviewed main SHA:** b6933b772f41b45918f7e25ed1afbbb1fd892272; integrated docs/sections/hermitian-torsion-and-the-bochner-identity/index.html blob 4656b430de6ec989ef121eca550afda0be407222.
- **Source/permanent labels:** demailly-complex-geometry:D2AA9D04 / DBCAF8FF0340 (11.48.13); demailly-complex-geometry:72367915 / E96E372480D4 (11.48.15); demailly-complex-geometry:7E456199 / 5029210C26BC (11.48.21); lines 103–107, 155–203, 227–244.
- **Assumptions:** $n=2$; for the global vanishing deduction additionally compact $X$, $\partial\bar\partial\omega=0$, strict lower curvature operator positivity.
- **New calculation:** $aa^*+a^*a=|\partial\omega|_\omega^2P$ with $P$ orthogonal rank four on $\Lambda^*T^*X\otimes\mathbb C$ whenever torsion is nonzero. Vanishing bidegree blocks: $(1,q)$, $(0,2)$, $(2,0)$. Optimal uniform coefficient 1 replaces the printed surface coefficient 4.
- **Proof:** explicit decomposable $(2,1)$-form and exterior-occupancy argument, plus independent exact 16-by-16 arithmetic check; full details: [report](../reports/2026-11-15-hermitian-surface-exact-skt-torsion-spectrum.md).
- **Upstream unverified:** general Hermitian Bochner identity, elliptic/Hodge inputs behind the printed corollary. No independent transitive theorem certification.
- **Action:** optional additional surface corollary, *proposed only*; preserve existing dimension-independent result and permanent tags.
- **Existing defects:** the 2026-10-25 equation alias and U+201D errors are still open; **not re-registered** here.
- **Coverage:** §11.48 selected proof passages previously partly read; +0 first numbered-section visits / +0 entire-section certificates; [matrix delta](../coverage/2026-11-15-hermitian-surface-exact-skt-torsion-spectrum.md).
- **Excluded programme:** Demailly approximation/regularization and dedicated Bergman/L2/OT/multiscale/positivity-loss remain **deferred-by-user**.
