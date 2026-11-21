# Gauduchon supporting-probability variance gap and weak-adjoint audit — 2026-11-21

## Baseline and precise scope

- Main: `b6933b772f41b45918f7e25ed1afbbb1fd892272` (freshly read); review branch before the original report: `9c7bfcf4ced6e2d194abfe931c655e755e87fd3f`.
- Direct, **whole mathematical section §12.8**, `docs/sections/a-gauduchon-variational-volume--supporting-probabilities-represented-by-maximizing-currents/index.html`, blob `ed1ad2bf6220cd086a44d7ee92ca7779666288d9`: all prose and proofs of **Lemma 12.8.1** (source `non-kahler-pluripotential-theory:E1B004B5`, permanent `47843166E777`) and **Theorem 12.8.2** (source `non-kahler-pluripotential-theory:3606F8FD`, permanent `E9E119AAA269`). Section tag `7C2BB0FDDDF5`.
- Direct, **whole mathematical section §24.7**, `docs/sections/problems-in-hermitian-pluripotential-theory--weak-gauduchon-adjoints/index.html`, blob `e9f7c4bcab38a796064574591d87fdbd9be58331`: all mathematical discussion and **Conjecture 24.7.1** (source `non-kahler-pluripotential-theory:68ABC3B8`, permanent `7C0A1CE5EC77`); section tag `C528B286A8D7`.
- Selected prerequisite check in §12.7.2–3, blob `1c0f7efb92914b8a55754bd5039d7319392fb03b` (the previously audited §12.7 is **not** counted as a new full section). §11.34 cited inputs were located but not re-proved.
- Main-file anchors: `#non-kahler-pluripotential-theory-E1B004B5`, `#non-kahler-pluripotential-theory-3606F8FD`, `#non-kahler-pluripotential-theory-68ABC3B8`; the above permanent tags also provide stable reader links.

## POME-GAUDUCHON-SUPPORT-VARIANCE-QUADRATIC-GAP-001

**Severity: low. Status: verified conditional deduction**, not a false printed theorem and not a repair of a proof gap. The bound extends the Jensen inequality explicitly used inside the proof of §12.8.2. It is conditional on the established internal Gauduchon duality theorem; it is not a transitive certification of all analytic inputs.

Let \(X\) be compact, connected, complex of dimension \(n\ge 2\), with Hermitian \(\omega\), smooth positive volume form \(\mathrm dV\), and continuous real data \(F,h\). Use the nonsingular reference potential \(0\). Let \(T\in\mathscr M(F)\) be **any** maximizing normalized Gauduchon current. Set
\[
\nu=\frac{\Gamma_F(T)}{M(F)}\in\mathcal A_0(F),\qquad
V=\operatorname{Var}_{\nu}(h)
 =\int_X h^2\,\mathrm d\nu-
   \left(\int_X h\,\mathrm d\nu\right)^2,\qquad
R=\max_X h-\min_X h.
\]
Then **for every real \(t\)**,
\[
\boxed{
B_0(F+t h)\le B_0(F)-t\int_X h\,\mathrm d\nu
-\frac{t^2}{2n}e^{-|t|R/n}\operatorname{Var}_{\nu}(h).
}\tag{*}
\]
If \(h\) is nonconstant \(\nu\)-almost everywhere, its variance is positive and the support-affine inequality is strict for every \(t\ne 0\). For smooth \(F\), the unique maximizing Gauduchon current is smooth and strictly positive, and its determinant probability has a smooth positive density. Thus the strict inequality holds for all nonconstant continuous \(h\) in that case. The estimate is an **upper supporting tangent gap**, not a claim that the entire scalar functional is twice differentiable.

### Full proof

The §12.7.3 identity \(B_0=-n\log M\), with \(T\) held fixed, gives
\[
M(F+t h)\ge\mathfrak D_{F+t h}(T)
=M(F)\int_X e^{t h/n}\,\mathrm d\nu.
\]
Consequently
\[
B_0(F+t h)-B_0(F)\le -nK(t),\qquad
K(s)=\log\int_X e^{s h/n}\,\mathrm d\nu.
\]
Because \(h\) is bounded, differentiation under the integral is valid for all real \(s\). Define the exponentially tilted probability
\[
\mathrm d\nu_s=
\frac{e^{s h/n}}{\int_Xe^{s h/n}\,\mathrm d\nu}\,\mathrm d\nu.
\]
Then
\[
K'(0)=\frac1n\int_Xh\,\mathrm d\nu,\qquad
K''(s)=\frac1{n^2}\operatorname{Var}_{\nu_s}(h).
\]
The tilted density satisfies pointwise
\[
\frac{\mathrm d\nu_s}{\mathrm d\nu}\ge e^{-|s|R/n}.
\]
Indeed, the quotient between the minimum and maximum values of \(e^{s h/n}\) equals \(e^{-|s|R/n}\), and its normalizing integral lies between those extrema. For any probability \(\rho\),
\(\operatorname{Var}_\rho(h)=\inf_{c\in\mathbb R}\int(h-c)^2\,\mathrm d\rho\);
therefore
\[
\operatorname{Var}_{\nu_s}(h)
\ge e^{-|s|R/n}\operatorname{Var}_\nu(h).
\]
For every \(s\) between \(0\) and \(t\), this is at least \(e^{-|t|R/n}V\). Taylor's formula with integral remainder (also when \(t<0\)) implies
\[
K(t)\ge \frac{t}{n}\int_Xh\,\mathrm d\nu
+\frac{t^2}{2n^2}e^{-|t|R/n}V.
\]
Substitution into the upper bound for \(B_0\) proves (*).

The case \(R=0\) reduces to the exact translation identity
\(B_0(F+t h)=B_0(F)-th\), and the variance term vanishes. The inequality does not claim a positive **uniform** variance lower bound for nonsmooth \(F\), does not settle differentiability, and says nothing about uniqueness of maximizing currents.

**Proposed nonproduction correction:** if desired, append this as a *quantitative corollary* to the Jensen supporting inequality of §12.8.2, retaining the existing statement, original historical attribution, and permanent tags. Potential mathematical dependents: §11.34 slope and adjoint stability, and the §24.7.1 differentiability/uniqueness problem; the latter is **not resolved**.

## Other reviewed steps and unresolved inputs

1. **§12.8.1:** after equality of the maximizing total masses, opposite perturbations \(1\pm\varepsilon h\) uniquely identify weak cluster determinant **measures**, rather than only their masses. The affineness assertion uses the measure inequality from the determinant-root concavity and equality of total masses on maximizing currents. No new printed error detected. The older `POME-GAUDUCHON-DUAL-MAXIMIZER-VARYING-DENSITY-NETS-001` already studies varying-density near-maximizing nets; it is **not a new finding here**.
2. **§12.8.2:** the exponential Taylor remainder is uniform on \(\mathscr G_\omega\) as the determinant measures have bounded mass; the one-sided derivative of \(B_0\) is represented by maximization over compact supporting measures, and separation establishes the reverse inclusion. The text correctly distinguishes uniqueness of the determinant probability from uniqueness of the maximizing current. The bound (*) strengthens its already printed Jensen inequality, not its existence result.
3. **§24.7:** Conjecture 24.7.1 asks for a *single* supporting probability at each continuous ordinary logarithmic density on a Hermitian background. This remains open in the text despite smooth, Kähler, generic \(G_\delta\), controlled-Hessian, and product partial cases. The singular divisorial examples address different hypotheses and are not counterexamples to the conjecture. The variance estimate (*) adds no uniqueness assertion.
4. **Conditional external/upstream inputs:** the normalized smooth Hermitian Monge–Ampère existence theorem (§12.2.3), compactness of normalized positive \(dd^c\)-closed Gauduchon currents (§11.7), and supporting-probability absolute continuity (§11.34.2) are used as internal cited statements, but their entire upstream proof chains were **not** certified here. Historical citations are retained. No approximation/regularization, dedicated Bergman, L², Ohsawa–Takegoshi, multiscale or positivity-loss proof programme was re-opened.

**Outcome:** +2 whole current direct section reads (§§12.8, 24.7), +1 verified conditional deduction, +0 entire transitive proof chains certified; historical first visits unknown. No confirmed false printed theorem. No builds, tests, CI, main/source/registry/tag changes or website publication.
