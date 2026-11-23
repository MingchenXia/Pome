> **SUPERSEDED — 2026-11-23 verified audit retraction.** Four missing-compactness/connectedness source-error claims in this record (Gauduchon §11.4.2; RC-positivity §§11.26.3/11.26.7; dependent Ricci-flat §11.27.4 recorded separately) are **WITHDRAWN**. The actual current §1.1 convention, `docs/sections/conventions/index.html` blob `ef778e54d8d7413242387e95c52269b3c7d42cae` line 123, states that `X` is **connected and compact unless otherwise specified**. The noncompact or disconnected examples therefore fall outside these theorem hypotheses; they do **not** establish printed errors. Earlier mathematical computations and unrelated review observations remain historical evidence, not a complete proof certification. See [new anchored retraction](../reports/2026-11-23-blowup-density-weak-endpoint-and-resolved-poles-connectedness.md).

# Compactness and connectedness in Gauduchon and RC-positivity assertions: cross-chapter audit

**Date:** 2026-11-22. **Current main reviewed:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`.
**Scope:** all current integrated mathematical text of §§5.63, 6.53, 11.26; introductory §16.10; selected direct prerequisite checks §§1.1, 11.3 and Theorem 11.4.2. This is a reading-edition audit, not a direct modification of source manuscripts. Historical first-visit counts and transitive proof certifications are **not** claimed.

## Scope and exact anchors

| Section / type | Exact integrated reading-edition path (relative to repository root) | Git blob on reviewed main | Read or checked |
|---|---|---|---|
| §5.63 current/positive currents | \`docs/sections/positive-current-coefficient-bounds-and-support-maxima/index.html\` | \`cb4c3d4e9d653b216cff05eaf23aafb2a01425ec\` | Entire mathematical lines 5–108; Proposition 5.63.2, Lemma 5.63.3, Theorem 5.63.4 |
| §6.53 projective bundle | \`docs/sections/projective-bundle-integration/index.html\` | \`3bf371940d1159461d77d04b3a6e6ba8e5d0f065\` | Entire mathematical lines 5–61; Lemma 6.53.1, Corollary 6.53.2, Proposition 6.53.3 |
| §11.26 directional curvature | \`docs/sections/gauduchon-metrics-and-linear-mass--conformal-changes-and-directional-curvature-positivity/index.html\` | \`d54016b202422bde3bc5e2c6e493e4618918a7d7\` | Entire mathematical lines 5–109; Definition 11.26.1, Lemma 11.26.2, Theorem 11.26.3, Example 11.26.6, Proposition 11.26.7 |
| §16.10 roadmap | \`docs/sections/envelopes-and-model-potentials/index.html\` | \`decb273ec97fcb9bb0ace2e0b90270723ecbea3e\` | Entire introductory text, lines 5–18; **not** a proof certification of referenced §16.11–27 results |
| §11.4 prerequisite | \`docs/sections/gauduchon-metrics-and-linear-mass--conformal-gauduchon-metrics/index.html\` | \`ecb4bf9e593dfb25f1644f0561d1aa65bf096b10\` | Targeted reading of Theorem 11.4.2 and proof, lines 20–57; previously fully visited, not counted anew |
| §11.3 and global §1.1 scope | \`docs/sections/gauduchon-metrics-and-linear-mass/index.html\`, \`docs/sections/conventions/index.html\` | §1.1 \`ef778e54d8d7413242387e95c52269b3c7d42cae\` | Selected standing-hypothesis lines: §11.3 line 7, §1.1 line 23; no compactness/connectedness convention for all complex manifolds |

## POME-GAUDUCHON-CONFORMAL-COMPACT-CONNECTED-001

**Severity:** medium. **Status:** **confirmed error of the unqualified reading-edition formulation**; the standard compact connected version is not disproved. **Source:** \`non-kahler-pluripotential-theory:F1B1A709\`; permanent Pome tag \`3978AEB15BD7\`; Theorem 11.4.2, lines 20–24 and proof 29–56 of the above §11.4 file.

**Printed hypothesis and issue.** The assertion "Every Hermitian form \(\eta\)" has a conformal Gauduchon representative, with \(\rho>0\) unique up to one positive scalar, does not say that \(X\) is **compact and connected**. The current global convention §1.1, line 23, assumes only paracompactness for a complex manifold; §11.3, line 7, specifies \(\omega\) and \(n\ge2\) without adding compactness or connectedness. The proof invokes Fredholm theory for a compact elliptic operator, integration on \(X\), and the one-dimensional kernel of an operator that has independent constants on each component.

**Counterexample 1 (compact but disconnected).** Let \(X=X_1\sqcup X_2\) be two copies of \(\mathbb P^2\), with Kähler forms \(\eta_i\). Set \(\rho=1\) on \(X_1\) and \(\rho=2\) on \(X_2\). Then \(\rho\) is smooth and positive and \(dd^c(\rho\eta^{n-1})=0\), just as for \(\rho\equiv1\), but the two functions are not constant positive multiples of one another. Thus uniqueness up to a *single global* scalar is false even on compact \(X\).

**Counterexample 2 (connected but noncompact).** Let \(X=B^2\subset\mathbb C^2\), \(\eta=i\sum_j dz_j\wedge d\bar z_j\). Both \(\rho_0=1\) and \(\rho_1=1+\frac12\operatorname{Re} z_1\) are strictly positive on \(B^2\); since \(dd^c\rho_i=0\) and \(d\eta=0\), both satisfy \(dd^c(\rho_i\eta)=0\). They are not constant multiples. This is a direct failure of uniqueness, without assuming anything about existence in other noncompact settings.

**Proposed correction (not applied):** explicitly assume \(X\) compact and connected, \(n\ge2\), in Theorem 11.4.2 and in any standalone assertion of one-dimensional adjoint kernel. For disconnected compact \(X\), existence holds componentwise and uniqueness is *one positive scalar per connected component*. Do not describe these counterexamples as disproving the classical compact connected theorem. **Affected dependents:** §11.4 proof lines 36–56, §§11.5–11.7, §11.23 normalized adjoint measure, Theorem 11.26.3, and later Gauduchon duality where these hypotheses are implicitly used. Existing conditional smooth-family finding assumes compact connected \(X\) and is unaffected.

## POME-RCPOSITIVE-GLOBAL-SPREAD-DISCONNECTED-001

**Severity:** medium. **Status:** **confirmed error of the unqualified reading-edition theorem**. **Source:** \`non-kahler-pluripotential-theory:894C16C8\`; permanent tag \`AFF6DB5A7BE1\`; Theorem 11.26.3 at §11.26 line 35 and proof lines 40–66. The local §11.26 assumptions (line 10) require rank \(>0\) and \(n\ge2\), not connectedness.

**Counterexample satisfying all the printed pointwise hypotheses, with compact \(X\).** Put \(X=X_1\sqcup X_2\) with \(X_i\simeq\mathbb P^2\), and choose \(\omega\) Fubini–Study on each component. Let \(E|_{X_1}=\mathcal O_{\mathbb P^2}(1)\) with its positively curved Fubini–Study metric and \(E|_{X_2}=\mathcal O_{X_2}\) with the flat metric. This defines a rank-one holomorphic bundle and smooth Hermitian metric on \(X\). Its mean curvature satisfies \(K_{\omega,h}\ge0\) everywhere. It is RC-positive on the nonempty open set \(U=X_1\). But for any smooth \(f\) and \(t>0\), the curvature of \(e^{-tf}h\) on the trivial factor \(X_2\) is \(t\,i\partial\bar\partial f\). At a maximum of \(f|_{X_2}\), this is negative semidefinite, so it has **no** positive tangent direction. The conclusion of Theorem 11.26.3 fails.

**Where the proof uses the missing condition.** Lines 41–54 construct a scalar right-hand side \(\rho=1-c\chi\) with \(\chi\) supported inside \(U\), chosen to have *global* zero \(\gamma^n\)-mean. On a disconnected compact manifold a Poisson equation with kernel consisting of componentwise constants requires zero mean on **each component**. On \(X_2\), \(\rho\equiv1\) violates compatibility; line 47's global integral is insufficient.

**Proposed correction:** assume \(X\) **compact and connected**; or require RC-positivity on a nonempty open set of *each* component and carry out the Poisson construction separately there. The original compact connected proof remains conditional on the stated §11.4 and §11.23 elliptic inputs; this note does not certify those full chains. **Affected dependents:** §11.26 concluding paragraph lines 109, downstream use of the RC-positive spreading theorem (including §11.27 examples).

## POME-RCPOSITIVE-FLAT-DETERMINANT-NONCOMPACT-001

**Severity:** medium. **Status:** **confirmed error of the unqualified reading-edition proposition**. **Source:** \`non-kahler-pluripotential-theory:78702390\`; permanent tag \`9EFFDFAE03AF\`; Proposition 11.26.7 line 96 and proof 101–104.

**Counterexample.** On the unit ball \(X=B^2\subset\mathbb C^2\), take the trivial holomorphic line bundle \(E=X\times\mathbb C\). Its determinant admits the constant flat metric \(h_0=1\). Independently equip \(E\) with the smooth metric \(h=e^{-|z|^2}\). Under the explicit §11.18 convention \(F_h=\bar\partial(h^{-1}\partial h)\),
\[
 F_h=\partial\bar\partial |z|^2,\quad
 iF_h=i\sum_{j=1}^2 dz_j\wedge d\bar z_j>0 .
\]
Thus \(h\) is uniformly RC-positive (rank one), and its mean curvature with respect to the Euclidean Hermitian form is positive definite. This contradicts both exclusions in the printed proposition, since the *same line bundle* also admits the flat metric \(h_0\). The proof's global minimum of \(b=\log(h/h_0)\) need not exist on noncompact \(X\).

**Proposed correction:** require \(X\) **compact** (componentwise the argument still applies if disconnected). Then each smooth real \(b\) attains a minimum; at that point \(iF_{\det h}=-i\partial\bar\partial b\) cannot have a positive direction. **Affected dependents:** final §11.26 paragraph (lines 109–110) and any flat-determinant obstruction applied outside the compact setting. This is a **false theorem as printed under the project's stated scope**, not merely a gap in an otherwise valid global statement.

## Other complete-section checks, without new confirmed errors

**§5.63:** Directly compared the index complement/phase-polarization proof of Proposition 5.63.2 (11–40), including the \(p=0,n\) endpoints, weighted diagonal scaling and zero-weight passage. Lemma 5.63.3 (45–78) uses compactly supported upper semicontinuous test functions, vague upper portmanteau, a cofinal convergent subnet, truncations \(\max(f_{k_0},-m)\), and decreasing integration; it does **not** replace vague with narrow convergence. The support maximum theorem (83–108) has the stated \(p\ge1\), compact support and strict-psh defining function. Its smooth-decreasing-majorant lemma (§7.31.1) is recorded as a dependency, not independently certified or reopened as any user-excluded regularization programme.

**§6.53:** Read the generic complex-line Lelong number proof (9–16), blowup minimum (21–31), and projective-bundle pushforward (36–61). Checked that the one-dimensional divisorial contribution multiplies by the fiber volume \(v=\int_{\pi^{-1}(x)}\omega^{r-1}\), that the \(r=1\) case reduces to the identity, and that the higher-dimensional argument explicitly addresses restriction through the disc center instead of silently deleting an atom. The source's potential-gluing/Hodge and generic-slicing inputs remain conditional dependencies, not independently certified. No new contradiction is asserted.

**§16.10:** Read its entire introductory overview (5–18), distinguishing global obstacle envelopes, singularity envelopes and the referenced relative capacities. It contains references to later results but no new proof certified here. No claim of full coverage of §§16.11–27.

**§11.26 other steps:** Definition 11.26.1, trace/eigenvalue Lemma 11.26.2, example's zero-trace \(2\times2\) curvature (74–91) and conformal curvature sign (56–65) checked directly. The formula \(F_{e^{-tf}h}=F_h+t\partial\bar\partial f\,\mathrm{Id}\) agrees with the declared §11.18 sign. The problem in the two global results is scope (compactness/connectedness), not an incorrect local curvature computation.

## Dependency/status separation and scope delta

- **Three** current integrated substantive sections were fully directly read: §§5.63, 6.53, 11.26; **one** short introductory section fully read: §16.10. Exact limited rechecks: §11.4 (prior full review), §11.3 (standing scope), §1.1 (project conventions).
- **Three** stable medium-severity confirmed formulation errors/counterexamples, not a new mathematical proof of the standard compact connected versions. No complete transitive upstream proof chain is certified.
- Existing earlier §11.4 smooth-parameter result explicitly assumed compact connected \(X\); it remains a **verified conditional deduction**, not evidence that the unqualified printed theorem is correct.
- No work on Demailly regularization or dedicated Bergman, \(L^2\), Ohsawa–Takegoshi, multiscale atlas or positivity-loss proof-completion. Existing notes remain **deferred-by-user**, not resolved or certified.
- No builds, Python/JS tests, GitHub Actions, source/registry/canonicalization/permanent-tag edits, main branch edits, PR merge, or website publication.
