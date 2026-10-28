# Mathematical audit — multiplier ideals under maxima and the critical Sobolev boundary (28 October 2026)

**Pinned production main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. **Pre-write review HEAD:** `467b09fa9df1071dd2106b9cf78f32d0529f7314`. **Scope:** first independent direct model calculation for selected §16.24.1–2 and a new endpoint stress test of the argument in selected §11.24.1. The integrated sections were read at the specific Git blobs identified below. Both original statements remain correct; these are **verified conditional deductions / sharp qualifications to possible extensions**, not false theorems, full proof certifications, or production repairs.

## POME-MULTIPLIER-MAX-IDEAL-SUM-001

**Severity / status:** low / **verified conditional deduction** (an obstruction to a stronger ideal-algebra claim; no error in the printed proposition or lemma).

**Exact locus:** `docs/sections/envelopes-and-model-potentials--divisorial-constraints-under-envelopes/index.html`, current-main Git blob `40f522a64d7e846a4507c27e8ac9b4fa382c514c`. Proposition **16.24.1**, source `foundations-of-pluripotential-theory:73492AFD`, permanent tag `585A4246348B`, physical HTML lines **14–43**; Lemma **16.24.2**, source `foundations-of-pluripotential-theory:AC593099`, permanent tag `FFB5A7083041`, physical lines **45–61**. The latter correctly states that maximum preserves divisorial-Lelong-number equivalence, not that the corresponding multiplier ideals obey an ideal-sum identity.

**Global model meeting the section's hypotheses.** Put (X=\mathbf P^1\times\mathbf P^1), choose standard Fubini–Study forms (\omega_i=\mathrm{pr}_i^*\omega_{\rm FS}), and set (\theta=\omega_1+\omega_2). Let (D_1=\{a\}\times\mathbf P^1) and (D_2=\mathbf P^1\times\{b\}), with respective defining holomorphic sections (s_i) of (\mathrm{pr}_i^*\mathcal O(1)) and smooth metrics (h_i) of curvature (\omega_i). Normalize the section norms if desired and define
[
u=\log|s_1|_{h_1}^{2},\qquad v=\log|s_2|_{h_2}^{2}.
]
With the Pome normalization (dd^c=\frac{i}{2\pi}\partial\bar\partial), Poincaré–Lelong gives
[
\theta+dd^c u=[D_1]+\omega_2\ge0,\qquad
\theta+dd^c v=[D_2]+\omega_1\ge0.
]
Thus both are globally (\theta)-psh and uniformly bounded above. At the crossing (p=D_1\cap D_2), take coordinates ((x,y)) in which
[
u=\log|x|^2+O(1),\qquad v=\log|y|^2+O(1).
]
Every (O(1)) here is smooth and locally bounded; consequently it does not change a multiplier ideal. The convention in the reading edition is (\mathcal I(w)=\{f: |f|^2e^{-w}\in L^1_{\rm loc}\}).

**Direct ideal calculation.** Since ( |f|^2/|x|^2 ) is locally integrable if and only if (f) is divisible by (x) (use Fubini along transverse (x)-discs for necessity, and boundedness after division for sufficiency),
[
\mathcal I(u)_p=(x),\qquad \mathcal I(v)_p=(y),\qquad
\mathcal I(u)_p+\mathcal I(v)_p=(x,y).
]
On the other hand,
[
\max(u,v)=\log\max\{|x|^2,|y|^2\}+O(1)
         =\log(|x|^2+|y|^2)+O(1).
]
Its exponential inverse is comparable with (r^{-2}) in real dimension four; (\int_0^\epsilon r^{3}r^{-2}\,dr<\infty). Hence the constant germ belongs to its multiplier ideal and
[
\boxed{\mathcal I(\max\{u,v\})_p=\mathcal O_{X,p}
\ \supsetneq\ \mathcal I(u)_p+\mathcal I(v)_p=(x,y).}
]
This is an **exact local counterexample to an *unprinted* proposed ideal-sum rule**, not a counterexample to §16.24.1 or Lemma 16.24.2. The latter correctly uses the minimum of divisorial Lelong numbers. The multiplier-ideal operation cannot simply be replaced by a sum of the component multiplier ideals when canonicalizing upper envelopes.

**Affected dependents / disposition:** Interpret the maximum/upper-envelope claims in §16.24 and their uses by ideal envelopes (§16.6) and ideal projection (§18.4) through divisorial order or the actual multiplier-ideal definition, never through an unproved identity (\mathcal I(\max)=\mathcal I(u)+\mathcal I(v)). Optional self-contained warning example; **no source-body, registry, tag or main change**. The computations do not invoke any excluded approximation/regularization theorem.

## POME-HERM-SOB-CRITICAL-C1-001

**Severity / status:** low / **verified conditional deduction** (sharp obstruction to extending *the printed proof method*, not an assertion that the Fredholm conclusion itself fails at the critical exponent).

**Exact locus:** `docs/sections/gauduchon-metrics-and-linear-mass--fredholm-theory-for-a-continuous-hermitian-form/index.html`, current-main blob `8fd933d027ecdba0c2df8efe7524e3984613857a`. Lemma **11.24.1**, source `non-kahler-pluripotential-theory:2FF004A4`, permanent tag `DEA6C8EFE702`, physical HTML lines **11–21** (hypothesis (p>2n)), **36–58** (weak maximum principle / (C^1) passage); Eq. 11.24.3 tag `88F9E749216F`, lines **44–49**.

Put (d=2n\ge2) and work in a real coordinate ball centered at the origin. Choose (\chi\in C_c^\infty) identically one near zero. For (0<r=|x|\ll1) put
[
f(x)=\chi(r)x_1\log\log(e/r),\qquad f(0)=0.
]
Near zero, radial differentiation gives
[
|D^2f(x)|\le \frac{C}{r\log(e/r)},\qquad
\int_{|x|<\epsilon}|D^2f|^d\,dx
\le C'\int_0^\epsilon\frac{dr}{r(\log(e/r))^d}<\infty
\quad(d>1).
]
The zeroth and first derivatives are also (L^d); integration by parts over punctured balls shows that the distributional derivatives have no point mass at the origin. Thus (f\in W^{2,d}\), in particular (f) is continuous. But on the positive (x_1)-axis
[
\partial_1 f(r,0,\ldots,0)
=\log\log(e/r)-\frac1{\log(e/r)}\longrightarrow+\infty.
]
Therefore (f\notin C^1), even locally. Consequently, at (p=d=2n), the convergence (W^{2,p}\to C^1) used in the proof's boundary-approximation and tangent-point gradient argument **is not available**. The printed (p>2n) condition is essential *to this particular (C^1)-based reasoning*. No failure of the lemma at (p=d) has been proved: a different PDE method might treat that endpoint.

**Affected dependents / disposition:** Preserve the explicitly stated (p>2n) in §11.24.1 and in uses of its (C^1)-based maximum-principle passage. Any future statement for (p=2n) must use a different argument, not a silent invocation of the above embedding. Optional standalone endpoint caution; **no mathematical theorem error or completed PDE proof certification**. No excluded Demailly/Bergman/weighted-L²/OT programme used.

## Coverage and independent verification boundary

Directly reread the integrated mathematical statements and selected proof steps of **§16.24.1–2** (divisorial ideal equivalence, arbitrary-family upper envelopes, the distinction between maximum valuations and ideals), plus **§11.24.1** (continuous-coefficient trace-operator hypothesis and the (C^1) maximum-principle passage). The chapter-level introductory §§16.1, 11.3 and 18.2 were read only for context, **not counted as certified mathematical sections**. Both substantive sections had *previous limited coverage*; this is **incremental work**, not a claim of first review or of whole-section certification. The existing actual-ToC inventory remains **25 chapters / 747 numbered sections**, with **zero whole sections certified**. No claim is made to have reread all 747 sections in this session. Existing confirmed errors, candidates, open gaps, external inputs and user-deferred items retain their prior status.

All Demailly approximation/regularization and its dedicated Bergman, weighted L², Ohsawa–Takegoshi, multiscale-atlas, and positivity-loss proof-completion work is expressly **deferred-by-user**, not reviewed, resolved, or certified. No tests, full build, CI, website publication or formal verification were performed.
