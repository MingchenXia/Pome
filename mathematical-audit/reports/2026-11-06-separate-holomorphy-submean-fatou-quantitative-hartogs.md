# Self-contained submean–Fatou replacement for the uniform Taylor-coefficient step of separate holomorphy

**Date:** 2026-11-06. **Finding:** POME-SEPHOL-HARTOGS-SUBMEAN-FATOU-001. **Severity:** low. **Status:** verified repair (a replacement for a named analytic step, proposed in audit only). **The printed theorem is correct; this is not a false-theorem finding.**

## Exact production target and conventions

- Reviewed production main SHA: b6933b772f41b45918f7e25ed1afbbb1fd892272.
- Actual current chapter/section: Chapter 9, §9.12, *Separate holomorphy*. Integrated reading file: docs/sections/separate-holomorphy/index.html, blob 2eafedb77d4a45f0133a5d92e27ad16b0be44ffd.
- Theorem 9.12.1, source klimek-pluripotential-theory:120C7FB1, permanent tag 362351A63FB6, statement physical line 8, original proof physical lines 13–50. Section source klimek-pluripotential-theory:DACB76D2 and section permanent tag 0C9E908FA1D6.
- Precise replacement location: line 36 defines holomorphic coefficients and subharmonic functions, lines 39–42 invoke the “subharmonic Hartogs lemma” to obtain a *uniform* coefficient estimate from a *pointwise* root-test bound. The bounded-patch Baire construction is at lines 22–28; the normal convergence and final recentering are at lines 42–50.
- Hypotheses as printed: an arbitrary open set Ω⊂ℂⁿ and a complex-valued function f separately holomorphic in each coordinate, with no measurability, continuity or local-boundedness assumption. The induction is over n. The proposed argument concerns the nontrivial n≥2 case and uses only the submean inequality and Fatou's lemma.

## Elementary uniform upper-bound lemma (proved here)

Let U⊂ℝᵈ be open, d≥2, and let (v_j) be subharmonic functions on U (allowing terms identically −∞). Assume that for every compact K⊂U there is a finite uniform upper bound for all v_j on K and that

\[
\limsup_{j\to\infty}v_j(x)\leq c\quad\text{for every }x\in U,
\]

where c is finite. Then for every compact K⊂U,

\[
\limsup_{j\to\infty}\sup_{x\in K}v_j(x)\leq c. \tag{A}
\]

**Proof without invoking the Hartogs lemma or subharmonic compactness.**
If (A) fails, take ε>0, indices j_k→∞, and x_k∈K such that v_{j_k}(x_k)≥c+ε. After taking a subsequence, x_k→x∈K. Choose ρ>0 with the closed Euclidean ball \(\overline{B(x,3\rho)}\subset U\), and a common finite upper bound M>c of the v_j on that ball. We may assume v_{j_k} is not identically −∞. Fix 0<δ<ρ. For large k,
\(B(x,\rho-\delta)\subset B(x_k,\rho)\subset B(x,3\rho)\).
Writing V_ρ for the volume of the radius-ρ ball, the submean inequality and the nonnegativity of M−v_{j_k} yield

\[
v_{j_k}(x_k)
 \leq \frac1{V_\rho}\int_{B(x_k,\rho)}v_{j_k}
 =M-\frac1{V_\rho}\int_{B(x_k,\rho)}(M-v_{j_k})
 \leq M-\frac1{V_\rho}\int_{B(x,\rho-\delta)}(M-v_{j_k}).
\]

On the fixed smaller ball, the pointwise hypothesis implies
\(\liminf_k (M-v_{j_k})\geq M-c\).
Fatou's lemma applied to nonnegative integrands thus gives

\[
\limsup_k v_{j_k}(x_k)
 \leq M-(M-c)\frac{V_{\rho-\delta}}{V_\rho}.
\]

Let δ↓0: the right side tends to c, contradicting \(v_{j_k}(x_k)\geq c+\varepsilon\). This proves (A). The case of an identically −∞ term cannot occur in the selected bad subsequence. No sequential compactness of a function space, regularization or interchange of a signed limit and integral has been assumed. □

## Application to the exact coefficient step

Following the printed Baire argument, there are a relatively compact polydisc P'⊂ℂⁿ⁻¹, a disc D(b,r) in the last coordinate and M<∞ with |f|≤M on P'×D(b,r). Separate Cauchy estimates then make f jointly holomorphic on this small product, so the Taylor coefficients \(c_j(z')=\partial_{z_n}^jf(z',b)/j!\) are holomorphic on P'. For every fixed 0<r₀<r, Cauchy's inequality gives \(|c_j(z')|\leq M r_0^{-j}\) uniformly on P' (or on slightly smaller products if desired). Hence \(v_j=j^{-1}\log|c_j|\), j≥1, are subharmonic in the real space ℝ²⁽ⁿ⁻¹⁾ and locally uniformly bounded above; the identically zero coefficient is treated as \(v_j\equiv-\infty\).

Assume the whole vertical disc D(b,R) stays inside Ω over P'. For each fixed z'∈P', the separately holomorphic function w↦f(z',w) has its Taylor series at b convergent in D(b,R). Cauchy–Hadamard gives
\(\limsup_j v_j(z')\leq-\log R\).
Apply the just-proved elementary lemma with \(c=-\log R\). For any compact L⊂P' and any 0<s<R, the strict inequality \(-\log R<-\log s\) implies that for all sufficiently large j,

\[
\sup_{z'\in L}|c_j(z')|\leq s^{-j}. \tag{B}
\]

For 0<t<s the tail of \(\sum_j c_j(z')(w-b)^j\) is dominated on \(L\times\overline{D(b,t)}\) by \(\sum_j(t/s)^j\). The finitely many initial terms are holomorphic, so the series converges normally and coincides with f for each fixed z' by the one-variable Taylor theorem. This proves the previously cited propagation step directly. The other parts of the printed proof—Baire's nested-disc construction and recentering a polydisc around any desired point—then supply joint holomorphy without presupposing local boundedness.

**Strict radius loss is meaningful.** For \(f(z',w)=(1-w/R)^{-2}\) on P'×D(0,R), the coefficients are \(c_j=(j+1)R^{-j}\); thus estimate (B) with \(s=R\) and constant 1 fails for every j≥1, even for a jointly holomorphic function independent of z'. Any s<R works eventually. This example rules out silently replacing the strict radius inequality by its endpoint in the quoted step.

## Classification and limits

- **Verified repair, not a false theorem or a claimed new proof gap:** the integrated theorem correctly invokes the classical subharmonic Hartogs lemma. The argument above supplies a fully explicit substitute for that single analytic input, addressing the earlier audit's “upstream Hartogs lemma not independently recertified” boundary. It proposes an optional self-contained replacement at physical lines 39–42, not a change of hypothesis or conclusion.
- **Dependency audit:** the substitute relies on the real submean inequality and Fatou's lemma only; the induction additionally uses elementary one-variable Cauchy, Cauchy–Hadamard, Baire/nested compact discs and Weierstrass convergence. None is Demailly approximation, Bergman, weighted L², Ohsawa–Takegoshi, multiscale gluing or positivity-loss work.
- **Affected downstream assertion:** Theorem 9.12.1's use of local uniform Taylor convergence, and only such downstream uses conditional on it. No claim is made to have independently certified all higher-dimensional complex-space facts, all of Chapter 9, or the complete transitive dependency graph.
- **Exact new coverage:** replacement of the subharmonic Hartogs step in §9.12.1 lines 36–48; separate inspection of the Baire bounded-patch and endpoint recentering lines 22–28 and 50. §9.12 was *already selected-reviewed* on 2026-10-24; this is a new proof of the specific previously unaudited analytic lemma, not first section coverage. Current actual ToC is 25 chapters / 747 numbered sections / zero whole mathematical-section certifications.
- All previously classified findings and the owner-deferred approximation/regularization-related programme retain their previous status. No source, production, permanent-tag, registry or published documentation changes were applied. No tests, build, CI or formal verification were run.
