# Cyclic inequalities for supporting measures of the normalization scalar

**Date:** 2026-11-17. **Stable finding ID:** `POME-SCALAR-SUPPORT-CYCLIC-KL-001`. **Severity:** low. **Status:** **verified conditional deduction**. This is not a confirmed error or a certification of the transitive analytic proof chain.

## Pinned integrated statements and hypotheses

Reviewed production main: `b6933b772f41b45918f7e25ed1afbbb1fd892272`.

- `docs/sections/normalization-and-weak-adjoint-measures/index.html` (blob `031b5d62d25d7ff03d95e4a14988399527cc946a`), physical lines 5–10, section permanent tag `7091FEDB43F0`, source `non-kahler-pluripotential-theory:75571769`: connected compact complex manifold, positive smooth reference volume, semipositive big Hermitian background, model ordinary singularity type with the stated smaller-background nonvanishing condition.
- `docs/sections/normalization-and-weak-adjoint-measures--the-scalar-functional/index.html` (blob `fff86de757578ed2be369ba752123f62f3d31044`): equation 11.33.1, source `non-kahler-pluripotential-theory:19974F5F`, permanent `9D47DB96B6E3`, lines 10–23; Proposition 11.33.2, source `6D175DAF`, permanent `2770AB03C0D2`, lines 26–50; Theorem 11.33.4, source `547E9FD9`, permanent `8810E18F852C`, lines 61–79.
- `docs/sections/normalization-and-weak-adjoint-measures--bounded-measurable-densities-and-stability/index.html` (blob `9c045c6e7a5bc4f0830874030c18dad0cafae905`), Theorem 11.36.1, source `non-kahler-pluripotential-theory:ECDF9BCE`, permanent `99653D7759E2`, lines 10–18 (supporting inequality (11.36.2), source `4DCA70F5`, permanent `F840087A1B81`, lines 12–15); proof lines 20–55.
- `docs/sections/normalization-and-weak-adjoint-measures--entropy-and-the-closed-case/index.html` (blob `0710d0732ae7ef81de3d3d62206a0f9c6b5d321f`), equation 11.37.2, source `non-kahler-pluripotential-theory:65FF799F`, permanent `803909FECEC0`, physical lines 54–61. Its fixed-mass input Theorem 13.8.7 remains a conditional upstream input.

Assume the printed existence/uniqueness-of-scalar and supporting-probability results. Let (B=B_\varphi) on real (L^\infty(\mathrm dV)), and let (\mathcal A(F)) be the nonempty set of absolutely continuous probability measures with
\[
 B(G)\le B(F)-\int_X(G-F)\,\mathrm d\nu,\quad \nu\in\mathcal A(F).
\]
We do not identify arbitrary Hermitian supporting measures with Gibbs probabilities.

## Exact finite-cycle inequality and equality analysis

For (F,G\in L^\infty(\mathrm dV)) and (\nu_F\in\mathcal A(F)), define the (orientation-dependent) supporting gap
\[
 \mathscr D_B(F,G;\nu_F):=
 B(F)-B(G)-\int_X(G-F)\,\mathrm d\nu_F\ge0.
\]
Every term is finite because both (B) values are real and (G-F) is bounded. For **any finite ordered cycle** (m\ge2), (F_1,\ldots,F_m\in L^\infty), (F_{m+1}=F_1), and arbitrary choices (\nu_i\in\mathcal A(F_i)),
\[
 \boxed{-\sum_{i=1}^{m}\int_X(F_{i+1}-F_i)\,\mathrm d\nu_i
 =\sum_{i=1}^{m}\mathscr D_B(F_i,F_{i+1};\nu_i)\ge0.}\tag{1}
\]
In particular the two-point sign is
\[
 \int_X(G-F)\,\mathrm d(\nu_G-\nu_F)\ge0.
\]
**Proof.** Each gap is nonnegative by the exact supporting inequality in 11.36.2. Summing its definition, the (B(F_i)-B(F_{i+1})) terms telescope. This proves (1) without requiring uniqueness, differentiability of (B), or any continuity of (F\mapsto\nu_F).

**Equality is characterized, even in the nonclosed Hermitian setting:** (1) is equality precisely when each selected (\nu_i) supports (B) at *both* (F_i) and (F_{i+1}). Indeed all individual gaps are nonnegative, so their zero sum forces all gaps to vanish. If the gap for (F,G,\nu_F) vanishes, then for every (H),
\[
 B(H)\le B(F)-\int(H-F)\,\mathrm d\nu_F
 = B(G)-\int(H-G)\,\mathrm d\nu_F,
\]
so (\nu_F\in\mathcal A(G)). The converse follows by applying the two supporting inequalities in opposite directions. Moreover concavity and the same supporting hyperplane sandwich give the exact affinity
\[
 B((1-t)F+tG)=(1-t)B(F)+tB(G)\quad(0\le t\le1)
\]
on each equality edge. **No strict concavity in an arbitrary nonclosed background is asserted.**

## Closed Kähler specialization: the exact KL cycle identity

Assume now the *additional* hypotheses of printed (11.37.2): (\theta) is Kähler and the ordinary singularity type has fixed positive mass (m_\varphi). Write (Z_F=\int_X e^F\,\mathrm dV), (\mu_F=Z_F^{-1}e^F\mathrm dV). The printed identities give
\[
 B(F)=\log m_\varphi-\log Z_F,\qquad \mathcal A(F)=\{\mu_F\}.
\]
For bounded measurable (F,G), all Gibbs measures are mutually absolutely continuous, and
\[
 \begin{aligned}
 \mathscr D_B(F,G;\mu_F)
 &=\log(Z_G/Z_F)-\int_X(G-F)\,\mathrm d\mu_F\\
 &=\int_X\log\frac{\mathrm d\mu_F}{\mathrm d\mu_G}\,\mathrm d\mu_F
 =D_{\rm KL}(\mu_F\Vert\mu_G).
 \end{aligned}
\]
Consequently (1) sharpens to the **exact multi-density identity**
\[
 \boxed{-\sum_{i=1}^{m}\int_X(F_{i+1}-F_i)\,\mathrm d\mu_{F_i}
 =\sum_{i=1}^{m}D_{\rm KL}(\mu_{F_i}\Vert\mu_{F_{i+1}})
 \ge \tfrac12\sum_{i=1}^{m}\|\mu_{F_i}-\mu_{F_{i+1}}\|_{\rm var}^{2}.}\tag{2}
\]
Here (\|\sigma\|_{\rm var}=|\sigma|(X)), **twice** the conventional probabilistic total-variation distance. The last bound is the sharp Pinsker inequality (also independently derived in the existing 2026-11-07 single-pair Fenchel-gap report). Equation (2), unlike that earlier one-base-point result, keeps track of **all successive bases and selected supergradients in an arbitrary oriented finite cycle**.

For completeness, Pinsker follows by taking (A=\{\mathrm d\mu/\mathrm d\rho\ge1\}) for (\mu\ll\rho), applying conditional Jensen on (A) and (X\setminus A), and using that the Bernoulli relative entropy has second derivative (1/[p(1-p)]\ge4) in its first mass (p). This yields (D_{\rm KL}(\mu\Vert\rho)\ge2(\mu(A)-\rho(A))^2=\frac12\|\mu-\rho\|_{\rm var}^2).

**Rigidity.** Equality of the left side of (2) with zero holds precisely when (\mu_{F_i}=\mu_{F_{i+1}}) for all (i), equivalently each (F_{i+1}-F_i) is (\mathrm dV)-almost everywhere constant. Conversely constant shifts produce equality. This characterization is valid for measurable (F_i), not only continuous functions.

**Sharpness check.** Normalize (\mathrm dV(X)=1); choose a measurable (A\subset X) with (\mathrm dV(A)=1/2). Put (G=0) and, for (0<\epsilon<1/2), (F_\epsilon=\log(1+2\epsilon)\) on (A), (\log(1-2\epsilon)) off (A). Then (Z_{F_\epsilon}=1), (\|\mu_{F_\epsilon}-\mu_0\|_{\rm var}=2\epsilon), and
\[
 D_{\rm KL}(\mu_{F_\epsilon}\Vert\mu_0)
 =(1/2+\epsilon)\log(1+2\epsilon)+(1/2-\epsilon)\log(1-2\epsilon)
 =2\epsilon^2+O(\epsilon^4).
\]
The reverse KL is also (2\epsilon^2+O(\epsilon^4)). Thus the two-cycle gap equals (4\epsilon^2+O(\epsilon^4)), whereas the Pinsker lower bound in (2) is (4\epsilon^2), verifying optimality of its universal coefficient (1/2). This is an analytic limit calculation, not a software test.

## Classification, dependencies, coverage

**Status:** low / verified conditional deduction. The printed 11.33.2, 11.33.4, 11.36.1 and 11.37.2 are **not refuted**; no new repair of a false theorem is claimed. The general cyclic inequality is a finite-dimensional convex-analytic consequence of 11.36.2, while the KL identity uses *only in the Kähler case* the fixed-mass and explicit Gibbs formulas of 11.37.2. It must not be transported to nonclosed Hermitian backgrounds without a separate argument. The earlier single-pair Fenchel/KL report remains distinct and intact.

**Affected dependents / proposed use:** provides a sign/equality diagnostic for chains of normalization-scalar supporting probabilities in §§11.34–11.36, and an exact multi-density entropy certificate for the closed case §11.37; no production correction proposed. Nontrivial existence, uniqueness of (c_\varphi(F)), and fixed-mass theory remain **uncertified analytic inputs**. These sections were already partially audited: **+0 first-visited numbered sections; +0 fully certified sections**. Current 25-chapter / 747-numbered-section inventory retained. Excluded Demailly approximation/regularization and dedicated Bergman, (L^2), Ohsawa–Takegoshi, multiscale atlas and positivity-loss programmes remain **deferred-by-user**, not solved or certified. No project build, software test suite, CI, mathematical-body edit or publication in this review.
