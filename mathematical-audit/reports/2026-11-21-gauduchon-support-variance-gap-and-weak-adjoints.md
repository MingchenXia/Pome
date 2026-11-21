# Gauduchon supporting-probability variance gap and weak adjoint audit — 2026-11-21

## Baseline and direct scope

- Main commit: `b6933b772f41b45918f7e25ed1afbbb1fd892272` (read anew); audit branch parent before this report: `9c7bfcf4ced6e2d194abfe931c655e755e87fd3f`.
- Integrated section **§12.8**, `docs/sections/a-gauduchon-variational-volume--supporting-probabilities-represented-by-maximizing-currents/index.html`, blob `ed1ad2bf6220cd086a44d7ee92ca7779666288d9`: all mathematical paragraphs, Lemma **12.8.1** (source `non-kahler-pluripotential-theory:E1B004B5`, permanent `47843166E777`), Theorem **12.8.2** (source `non-kahler-pluripotential-theory:3606F8FD`, permanent `E9E119AAA269`), and section introduction (permanent `7C2BB0FDDDF5`). Anchors: `#non-kahler-pluripotential-theory-E1B004B5`, `#non-kahler-pluripotential-theory-3606F8FD`, or the permanent `/tag/...` links.
- Integrated section **§24.7**, `docs/sections/problems-in-hermitian-pluripotential-theory--weak-gauduchon-adjoints/index.html`, blob `e9f7c4bcab38a796064574591d87fdbd9be58331`: all mathematical paragraphs of the weak-adjoint problem summary and **Conjecture 24.7.1** (source `non-kahler-pluripotential-theory:68ABC3B8`, permanent `7C0A1CE5EC77`), section tag `C528B286A8D7`.
- Only selected dependency/context checks in §12.7 (source §12.7.3 `0537569F9F52`, main blob `1c0f7efb92914b8a55754bd5039d7319392fb03b`) and the §11.34 supporting-probability results as cited in §24.7. §12.7 was already fully reviewed; **it is not a newly completed section here**.
- This is **two current whole-section direct reads**; neither is claimed as a historical first visit or an independently certified transitive proof chain. The review excludes the user-deferred approximation/regularization, Bergman, L², Ohsawa–Takegoshi, multiscale atlas and positivity-loss completion programmes.

## New finding: `POME-GAUDUCHON-SUPPORT-VARIANCE-QUADRATIC-GAP-001`

**Classification:** low; **verified conditional deduction** from the existing duality theorem; **not a false theorem or a repair of a printed error**.

**Hypotheses and precise result.** Let (X) be a connected compact complex manifold of complex dimension (n\ge 2), (omega) a Hermitian metric, (mathrm dV) a smooth strictly positive volume form, and (F,h\in C(X,\mathbb R)). Use the nonsingular reference (0), the normalization (B_0(F)), and the compact normalized Gauduchon-current set (mathscr G_omega) as in §§12.7–12.8. Choose **any** maximizing current (T\in\mathscr M(F)), and write
[

u=
u_{T,F}=rac{Gamma_F(T)}{M(F)}\in\mathcal A_0(F),qquad
V=\operatorname{Var}_{
u}(h)=\int h^2\,\mathrm d
u-\left(\int h\,\mathrm d
u\right)^2,qquad
R=\max_X h-\min_X h.
]
Then for every real (t),
[
\boxed{B_0(F+t h)\le B_0(F)-t\int_Xh\,\mathrm d
u-
\frac{t^2}{2n}\exp\!\left(-\frac{|t|R}{n}\right)V.}
\tag{*}
]
In particular if (h) is nonconstant (
u)-almost everywhere (so (V>0)), the supporting-affine inequality at (F) is **strict along this direction at every nonzero (t)**. For smooth (F), the maximizing probability has a smooth positive density, so every nonconstant continuous (h) has (V>0). This is a quantitative improvement of the Jensen support inequality already printed inside the proof of Theorem 12.8.2; it does **not** assert twice differentiability of (B_0), uniqueness of weak adjoints, or a globally uniform strict-concavity modulus.

**Complete conditional proof.** From Theorem 12.7.3, (B_0=-n\log M). Holding the chosen (T) fixed while changing its continuous density gives
[
M(F+t h)\ge\mathfrak D_{F+t h}(T)
=M(F)\int_X\exp(t h/n)\,\mathrm d
u .
]
Thus
[
B_0(F+t h)-B_0(F)\le -n K(t),\qquad
K(s)=\log\int_X\exp(s h/n)\,\mathrm d
u .
]
The boundedness of (h) permits differentiation under the integral for every (s\in\mathbb R). Let
[
\mathrm d
u_s=\frac{\exp(s h/n)}{\int\exp(s h/n)\,\mathrm d
u}\,\mathrm d
u.
]
Then (K'(0)=\int h\,\mathrm d
u/n) and (K''(s)=\operatorname{Var}_{\nu_s}(h)/n^2). Pointwise,
[
\frac{\mathrm d
u_s}{\mathrm d
u}\ge
\exp(-|s|R/n).
]
Indeed both the numerator and its normalizing denominator lie between the corresponding extrema of (exp(s h/n)). Taking the infimum over constants (c\in\mathbb R) in the identity
(operatorname{Var}_\rho(h)=\inf_c\int (h-c)^2\,\mathrm d\rho)
shows
[
K''(s)\ge n^{-2}\exp(-|s|R/n)\,V.
]
For (s) between (0) and (t), the lower bound is at least (n^{-2}\exp(-|t|R/n)V). Taylor's theorem with integral remainder (valid for both signs of (t)) therefore yields
[
K(t)\ge t\int h\,\mathrm d\nu/n+
t^2\exp(-|t|R/n)V/(2n^2).
]
Multiplying by (-n) proves (*). The argument never replaces a net by a sequence, does not interchange singular Monge–Ampère limits, and invokes no deferred regularization result.

**Sharp logical boundaries.** This yields a strict **upper supporting tangent gap** for each chosen support probability with positive variance; it is not a general equality for (B_0), nor proof that (B_0) has a Hessian. If (h) is constant, (V=0) and the exact translation identity (B_0(F+t h)=B_0(F)-th) is consistent with (*). For a continuous nonsmooth datum, the maximizing current and supporting probability need not be unique, as Conjecture 24.7.1 explicitly stresses.

**Suggested optional source addition (not applied):** After the Jensen estimate in Theorem 12.8.2, state (*) as a quantitative corollary with the explicit hypotheses. Do not modify its existing theorem or its historical attribution. Potential dependents: stability/slope analysis of §11.34 supporting probabilities and the differentiability problem of §24.7.1; this does **not** settle that problem.

## Independent audit observations and dependency ledger

1. **§12.8.1 (verified conditional proof steps, no newly confirmed source error):** the determinant-root functional is concave and one-homogeneous; taking the two-sign perturbations (1\pm\varepsilon h) after equality of maximal masses identifies *the whole determinant measure*, not merely its total mass. For a fixed (F), the theorem states a **sequence** result. A separate already-existing 2026-11-21 finding `POME-GAUDUCHON-DUAL-MAXIMIZER-VARYING-DENSITY-NETS-001` handles varying-density near-maximizing nets; it is intentionally not relabelled or recounted here.
2. **§12.8.2 (verified conditional proof steps):** (M(F+t h)) is expanded uniformly over normalized currents because (Gamma_F(T)(X)\le M(F)); (Fmapsto B_0(F)) has directional right derivatives given by maximum integrals over (mathscr N(F)), and separation supplies equality of the supporting sets. The existing theorem explicitly distinguishes a unique determinant probability from a unique maximizing current; the variance result does not collapse this distinction.
3. **§24.7 (problem-status verification, not a theorem certification):** Conjecture 24.7.1 is *open within the reading edition* for arbitrary continuous (F) and Hermitian background. Its discussion records smooth, Kähler, generic (G_\delta), controlled-Hessian and product partial cases, and distinguishes a bounded ordinary reference from singular divisorial references. Nothing in (*) resolves it. No contradiction between §24.7's uniqueness question and §12.8's existence/compactness was identified.
4. **External/uncertified inputs:** the nonlinear smooth Hermitian Monge–Ampère solvability invoked through §12.2.3/§12.7.3, compactness of normalized Gauduchon currents (§11.7), and absolute continuity of supports (§11.34.2) are used as established internal statements here, **not re-proved**. Historical attribution is preserved; dependency-chain certification remains open. No Demailly approximation/regularization machinery was checked.

## Outcome

- New: **one** rigorous conditional quantitative gap finding, `POME-GAUDUCHON-SUPPORT-VARIANCE-QUADRATIC-GAP-001`.
- Direct coverage: **all mathematics in current §§12.8 and 24.7**; selected prerequisite statements in §12.7. No first-ever visit claimed, and **zero full upstream chains** newly certified.
- No newly confirmed false printed theorem, new genuine duplicate, or source-body fix.
- No builds, tests, GitHub Actions CI, permanent-tag/registry changes, website publication, main changes, or source-repository edits.
