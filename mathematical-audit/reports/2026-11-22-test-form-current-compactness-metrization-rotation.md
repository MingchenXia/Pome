# 2026-11-22: Current-family weak metrizability and cross-chapter audit

## Baseline and scope

Reviewed Pome **main** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. The pre-write audit branch head was `f7668c3ca33e35d6ab67aca3b5a9451ef00507cb`. The current 25-chapter TOC has **747 sections**.

**Complete direct readings of integrated mathematics:** §2.10, test-form topology and current compactness, `docs/sections/test-form-topology-and-compactness-of-currents/index.html` (blob `420522ce2f3e4d8a8cbc3d8a3c1bb270d62ece4b`, physical lines **7–129**, source `demailly-complex-geometry`, *not the excluded regularization programme*); §21.5, real Alexandrov Monge–Ampère measures, `docs/sections/convex-analysis-and-toric-potentials--the-real-monge-ampere-measure/index.html` (blob `7089aa41ae2422b1bd6b5094e46668cbc8ed37be`, mathematical lines **7–157**, source `foundations-of-pluripotential-theory`); §19.1, introductory Okounkov bodies, `docs/sections/the-theory-of-okounkov-bodies/index.html` (blob `e58bf2e05976402030964165451485a4c57a330f`, lines **7–38**, source `sgpt`). The introductory section does *not* certify the theorems in §§19.2–19.6.

**Complete recheck**, not a historical first visit: §20.5, `docs/sections/divisors-and-logarithmic-limits-on-analytic-cycles/index.html` (blob `dae567406b2030e550664ca57b1fe77911d956d4`, lines **7–155**). **Selected only**, not an entire §22.1 review: §§22.1.54–63 on Duistermaat–Heckman measures, `docs/sections/non-archimedean-pluripotential-theory/index.html` (blob `8448d710690ebe1cc28040f9611d05c9d008a961`, lines **902–1096**).

## POME-TESTFORMS-POINTWISE-BOUNDED-WEAK-COMPACT-METRIZABLE-001

**Severity low; status verified conditional deduction**, not a false printed theorem. Theorem 2.10.5 has source label `demailly-complex-geometry:6DD9E811`, permanent tag `423C948D346B`, physical lines **95–129**. Prerequisites: Proposition 2.10.2 source `E541977A`, permanent `BC76137F21A7`, lines **11–40**; Proposition 2.10.3 source `1DAD97D6`, permanent `257A408A0F68`, lines **48–70**; equation (2.10.6) tag `73EE691E4241`, lines **117–124**.

**Proposition.** For a smooth Hausdorff second-countable real manifold \(M\), \(0\le p\le \dim M\), and any **pointwise bounded** set of currents \(A\subset \mathcal D'_p(M)\), the closure \(K=\overline A\) under the *full weak topology* \(\sigma(\mathcal D'_p,\mathcal D^p)\) is **compact metrizable**. It is therefore sequentially compact. There exists a countable family of test forms \(\{\varphi_j\}_{j\ge1}\), chosen independently of \(A\), for which
\[
d_K(S,T)=\sum_{j\ge1}2^{-j}\min\{1, |(S-T)(\varphi_j)|\}
\]
induces precisely the weak topology on \(K\).

**Proof.** As in §2.10.3 choose a compact exhaustion \(K_1\subset\operatorname{Int}K_2\subset\cdots\). For each \(j\), the fixed-support smooth test space \(E_j=\mathcal D^p_{K_j,\infty}\) is a Fréchet space by §2.10.2. It is **separable**: choosing countably many compact coordinate cubes, the map recording each coefficient and each derivative on each cube embeds \(\mathcal E^p_\infty(M)\) as a subspace of a countable product of \(C(Q)\) spaces, where each compact-metric \(Q\) gives a separable sup-norm Banach space. A countable product of second-countable metrizable spaces is second-countable, and every subspace is second-countable and separable. Thus \(E_j\) is separable. Fix a countable dense \(D_j\subset E_j\); \(\bigcup_jD_j\) is countable and dense in the *actual test-form topology*, because each inclusion \(E_j\to\mathcal D^p(M)\) is continuous and every test form has support in one \(K_j\).

Enumerate this dense union as \(\{\varphi_j\}\). Theorem 2.10.5 proves that \(K\) is compact **and contains only continuous currents**, using fixed-support Baire estimates followed by full-product compactness. Evaluation on \(\{\varphi_j\}\) gives a continuous map \(K\to\mathbb C^{\mathbb N}\). It is injective because continuous currents agreeing on the dense set agree on every test form. Compact-to-Hausdorff continuous injectivity implies a homeomorphism onto its image, which is compact metrizable. Pulling back the standard product metric gives the displayed formula. Sequential compactness is concluded **after** metrizability, not assumed beforehand.

**Sharp warning:** on \(M=\mathbb R\), take \(p=0\), \(T_j=\partial_x^j\delta_j\). Every compactly supported smooth test vanishes near \(j\) eventually, so \(T_j\to0\) weakly, while supports escape to infinity and distribution orders tend to infinity. Theorem 2.10.5 must **not** be misstated as providing one common compact support or globally bounded order for the family. Neither is needed in this argument.

**Suggested addition:** an audit-only optional corollary after Theorem 2.10.5; no repair of the printed theorem required. Potential dependents include compact-current extraction in §§5.19, 5.63, 11.22 **when pointwise boundedness has been proved**. This deduction depends on the printed theorem; it is **not** a full transitive certificate of every prerequisite.

## Additional verified scopes

**§21.5 (permanent 07CCE1F902ED).** Directly checked Theorem 21.5.1 (permanent 409656CC47D4) regarding completed-Lebesgue-measurable subgradient images and \(n!\) normalization, including dimension zero; Theorem 21.5.2 (permanent F4072D9ED060) regarding compact/open portmanteau and **vague, not necessarily narrow**, convergence, with \(F_j(x)=\max(0,x-j)\) illustrating mass escaping; Proposition 21.5.4 (permanent 5D8A7A7D734E) regarding Hessian regularity and the correct \(1/n!\) polarization normalization. No new printed error. Existing mixed-volume, affine covariance and transport findings are not re-registered.

**§19.1 (permanent 2DF8DA44EB89).** Directly checked the introduction's ordinary graded semigroup \(\Gamma(L)\) versus the generally non-semigroup \(\Gamma(L,\phi)\), and the stated almost-semigroup/flag constructions. These are explanatory statements, not independent proof certification of §§19.2–19.6.

**§20.5 whole recheck.** Verified the shape and hypotheses of local logarithmic \(L^1\) convergence, proper divisor pushforward with integer sheet multiplicities, Poincaré–Lelong on reduced cycles via the permitted resolution input, proper intersections and the cusp example. A defining function must be nonzero on each irreducible component. Previous zero-splitting and net findings remain unchanged.

**§22.1.54–63 selected.** Definition 22.1.55 (permanent 9ADEFD2FF381), Theorem 22.1.56 (permanent 0AD7F80A793D) and Proposition 22.1.60 (permanent 492A145E9067) use fixed Okounkov bodies, moment comparison and levelwise convergence. The stated flag independence and vague convergence still depend on §§19.5.26, 19.6.19/22/23; these upstream inputs are not independently certified here. No complete §22.1 verification is claimed.

## Ledger boundaries

**One new low verified conditional deduction**, **zero new confirmed source theorem errors**, **zero transitive proof-chain certifications**, **three full current direct readings** (one introduction), **one complete repeat**, **one selected passage**. No assertion of historical first visit. The 747-section register records coverage rather than full certification.

Excluded Demailly approximation/regularization, dedicated Bergman, L², Ohsawa–Takegoshi, multiscale-atlas and positivity-loss completion remains **deferred-by-user**, neither reopened nor solved. No project builds, tests, CI, GitHub Actions, publication or source/registry/permanent-tag/main changes.
