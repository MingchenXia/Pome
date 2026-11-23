# 2026-11-23 — exact Lee-curvature energy coefficient and cross-chapter trace review

## Baseline and exact coverage

- **Reviewed current main:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`. The source of the mathematics audited here is the integrated Pome reading edition, not private scans.
- **Full direct mathematical reading:** \`docs/sections/locally-conformally-kahler-geometry/index.html\`, Git blob \`6ebf8e604b45d3eb748037af506145273ca3875d\`, physical **lines 7–1355**: the section introduction and §§23.2.1–72, including LCK/Lee forms, the Kähler covering, twisted operators, Vaisman volume uniqueness, Hopf radial ODE, Chern–Ricci/Gauduchon rigidity, the Lee–Gauduchon duality, modifications, strongly Gauduchon metrics, and positive exact currents. The earlier reading of §§23.2.35–45 is **repeat work**, not a claimed new historical first visit. Full transitive dependencies are not certified.
- **Selected nonexcluded cross-check:** \`docs/sections/the-trace-operator/index.html\`, Git blob \`1f3a3e4f0317a308b43bd3df53dda84c5f3fa50a\`, **§20.2.29–37** (lines **660–821**), and the statement/formal-algebra portions of **§20.2.38–43** (lines **824–843, 885–940**). This is **not a whole §20.2 review**. §20.2.39 Step 1, physical lines 850–884, invokes quasi-equisingular approximation: it remains outside the authorized scope, not resolved or certified.
- **New finding:** \`POME-LEE-CURVATURE-ENERGY-EXACT-COEFFICIENT-001\`, **low / verified conditional deduction**, **not** an original-theorem error. No new confirmed false printed theorem and no complete upstream proof-chain certification.
- All Demailly approximation/regularization, Bergman, L2, Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof-completion work remains **deferred-by-user**.

## POME-LEE-CURVATURE-ENERGY-EXACT-COEFFICIENT-001

### Exact sources and hypotheses

The §23.2 introduction (line **8**) explicitly assumes that \(X\) is a **connected compact complex manifold of dimension \(n\geq2\)**. Let \(\omega\) be any smooth LCK Hermitian metric, \(d\omega=\lambda\wedge\omega\), \(d\lambda=0\), and \(g\) its associated real Riemannian metric. Use the project's convention
\[
d^c=\frac{i}{4\pi}(\bar\partial-\partial),
\qquad \lambda^c=d^c f\quad\text{locally if }df=\lambda,
\qquad \kappa_\lambda=d^c\lambda=-d\lambda^c.
\]
The directly checked inputs are **Proposition 23.2.7**, permanent tag \`11EBB7AD1165\`, and its **Eq. 23.2.8**, tag \`35851308DD2B\` (HTML lines **82–124**), together with **Proposition 23.2.14**, permanent tag \`E5F423FF7707\` (lines **187–212**). Source label family: \`non-kahler-pluripotential-theory\`.

### Result and complete additional calculation

For arbitrary such LCK data, the integrated Stokes formula has the following **exact** real-norm coefficient:
\[
\boxed{
\int_X\kappa_\lambda\wedge\omega^{n-1}
=\frac{n-1}{4\pi n}\int_X|\lambda|_g^2\,\omega^n.
}
\]
If \(V(t)=\int_X(\omega+t\kappa_\lambda)^n\), then
\[
\boxed{
V'(0)=\frac{n-1}{4\pi}\int_X|\lambda|_g^2\,\omega^n.
}
\]
These expressions are in terms of the **unnormalized** top wedge \(\omega^n\). If one uses \(d\operatorname{vol}_g=\omega^n/n!\) instead, the right-hand integrals acquire a factor \(n!\). Thus \(V'(0)>0\) exactly when the Lee form is not identically zero.

Here is the complete new coefficient calculation. At a fixed point, choose a \(g\)-orthonormal unitary real coframe \(x_j,y_j\) for which \(\omega=\sum_{j=1}^n x_j\wedge y_j\). Write
\[
\lambda=\sum_{j=1}^n(a_jx_j+b_jy_j),
\qquad
\lambda^c=\frac{1}{4\pi}\sum_{j=1}^n(a_jy_j-b_jx_j).
\]
The second equality follows from the stated \(d^c\) convention, as seen on the real coordinate functions of a unitary chart. When wedging \(\lambda\wedge\lambda^c\) with \(\omega^{n-1}\), all off-diagonal contributions vanish and each diagonal \(x_j\wedge y_j\) contributes \(\omega^n/n\). Hence
\[
\lambda\wedge\lambda^c\wedge\omega^{n-1}
=\frac{\sum_j(a_j^2+b_j^2)}{4\pi n}\,\omega^n
=\frac{|\lambda|_g^2}{4\pi n}\,\omega^n.
\]
Substitute into **Eq. 23.2.8**,
\[
\int_X\kappa_\lambda\wedge\omega^{n-1}
=(n-1)\int_X\lambda\wedge\lambda^c\wedge\omega^{n-1},
\]
and differentiate the finite wedge polynomial \(V(t)\) at \(0\). This uses no regularization, approximants, limit interchange, elliptic existence theorem or unproved compactness step in the **additional** calculation. It remains conditional on the printed Stokes identity, which was directly checked.

**Independent sign/factor check:** for the §23.2.24 scalar Hopf Vaisman example (lines **395–419**), \(\omega=\alpha+\beta\), \(\kappa_\lambda=\alpha\), \(\lambda\wedge\lambda^c=\beta\), and the radial one-form has \(|\lambda|_g^2=4\pi\). Directly,
\[
\int_X(\omega+t\kappa_\lambda)^n
=\int_X\big((1+t)\alpha+\beta\big)^n
=(1+t)^{n-1}\int_X\omega^n,
\]
because \(\alpha^n=\beta^2=0\). The derivative at zero agrees exactly with the formula above.

### Classification and impact

**Low / verified conditional deduction.** The original Propositions **23.2.7** and **23.2.14** are not false; the extra expression makes the normalization of their positivity statement quantitatively explicit. **Optional proposed addition** (not a source patch): insert the real-norm formula after Eq. 23.2.8. It also fixes the exact scale of the initial-volume slope in §23.2.14–15 and the positive Lee pairing used in §23.2.10–11. No permanent label or provenance change is needed.

## Cross-chapter direct checks

1. **§23.2.1–12, lines 7–181:** the explicit section hypothesis \(n\ge2\) is crucial for uniqueness of the Lee form; no dimension-one counterexample applies to this text. Checked conformal signs, global \(d^c\lambda=-d\lambda^c\), the Stokes pairing and the distinction between a nonzero de Rham-exact Bott–Chern class and a pseudoeffective class. The claimed obstruction to class C depends on the separate Kähler-modification input.
2. **§23.2.13–17, lines 182–316:** checked the polynomial positive derivative and top-power vanishing, the constant least-eigenvalue degeneration argument, and the Hopf example with an indefinite Lee curvature but a semipositive representative of its class. There is no contradiction between them.
3. **§23.2.18–45, lines 317–775:** checked the conjugation formula \(D_\lambda=e^fdd^c e^{-f}\), the nontrivial twisted action of constants, the horizontal-degree Stokes argument for transverse mass, and the positive periodic radial ODE and Lee-period ordering. The earlier audit of §23.2.35–45 remains acknowledged as a **re-read**. The smooth Hermitian Monge–Ampère existence/uniqueness input **14.2.1** for the general Vaisman-volume result is **not transitively certified**.
4. **§23.2.46–72, lines 777–1355:** checked the displayed Bianchi/Bochner algebra and tensor symmetries, the concrete Kodaira quotient, finite-dimensional separation for Lee–Gauduchon duality (23.2.60), the first cohomology comparison across modifications (23.2.63), and the strongly Gauduchon exact-current duality and mass estimate (23.2.69–70). The generalized Lamari criterion **11.6.1**, the Kähler \(\partial\bar\partial\)-lemma on a modification, and the positive-current weak compactness invoked there remain upstream, not independently certified.
5. **§20.2.29–37, lines 660–821:** differentiated the two distinct definitions of restricted volume (non-Kähler vs non-nef locus); tracked the **diagonal selection** \(\epsilon_j<1/j\) in Eq. 20.2.36, then the two-sided mass inequalities and monotonicity. This is not an interchange of unrelated limits. The arguments use existing internal mass continuity and monotonicity input **20.2.17, 16.9.30, 13.13.11** and a cited restricted-volume continuity theorem, all **not transitively certified** here.
6. **§20.2.38–43, selected lines 824–843 and 885–940:** only statement and formal algebraic comparison. §20.2.39 **Step 1 quasi-equisingular approximation (850–884) is deferred-by-user**, not silently completed or reexamined.

## Accounting and restrictions

**1 whole present-main §23.2 directly read (historical earlier partial preserved); 1 selected, nonexcluded §20.2; 1 low verified conditional deduction; 0 newly confirmed false original theorems; 0 complete transitive certificates.** No builds, tests, CI, main, source bodies, registry, permanent tags, publication, or private data. The excluded programme remains **deferred-by-user**.
