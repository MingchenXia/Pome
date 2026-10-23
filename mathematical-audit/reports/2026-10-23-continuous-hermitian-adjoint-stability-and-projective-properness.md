# Mathematical audit: continuous Hermitian adjoint stability and projective-complement properness

**Audit:** 2026-10-23 15:00 Asia/Shanghai. **Reviewed main:** b6933b772f41b45918f7e25ed1afbbb1fd892272. **Reviewed audit head before writing:** c4ccdc092ac7b6da2cea58ee228a475c7b8ba4bf. Freshly read main AGENTS.md (eda69505b9...), documentation/proof-expansions.md (8b37e218...), README.md, the current 25-chapter/747-section index, and branch review/mathematical-audit README.md and mathematical-audit/LATEST.md (2fe8436063...). The index is not mathematical proof certification. **Excluded:** all Demailly approximation/regularization and its dedicated Bergman, L2, Ohsawa–Takegoshi, multiscale-atlas and positivity-loss programme; previous records remain deferred-by-user.

## Exact selected integrated reading

- §11.24, docs/sections/gauduchon-metrics-and-linear-mass--fredholm-theory-for-a-continuous-hermitian-form/index.html, blob 8fd933d027ecdba0c2df8efe7524e3984613857a: Lemma 11.24.1, source non-kahler-pluripotential-theory:DEA6C8EFE702, permanent tag DEA6C8EFE702, lines 11–15 and 20–67. Read coefficient-freezing estimate, ABP/maximum principle, Fredholm and resolvent arguments. Historical POME-HERM-CZ-INTERNAL-001 and POME-HERM-ABP-001 already cover particular earlier checks and are not new findings here.
- §11.25, docs/sections/gauduchon-metrics-and-linear-mass--limits-of-adjoint-measures/index.html, blob 48117e4e5901381d5ae692cfd29f2cf5f1325abc: Proposition 11.25.1, source non-kahler-pluripotential-theory:3E5CF25D, tag 3E5CF25D6E23, lines 11–26, contextual comparison only. Its regularization-dependent §11.1.7 input is excluded.
- §11.26, docs/sections/gauduchon-metrics-and-linear-mass--conformal-changes-and-directional-curvature-positivity/index.html, blob d54016b202422bde3bc5e2c6e493e4618918a7d7: Theorem 11.26.3, source AFF6DB5A7BE1, tag AFF6DB5A7BE1, lines 35–66; Proposition 11.26.7, source 9EFFDFAE03AF, tag 9EFFDFAE03AF, lines 96–105. Checked the Gauduchon-compatible trace equation, conformal curvature sign and determinant minimum obstruction.
- §11.16, docs/sections/gauduchon-metrics-and-linear-mass--convex-norms-and-gauduchon-degrees--a-fixed-stein-hypersurface-for-all-finsler-metrics/index.html, blob 36f7dc4335a24458b4cddf7d0bec6faa132a5215: Lemma 11.16.1 source 27B5E82A, tag 00BCE16BE996, lines 14–21; Lemma 11.16.2 source 0EE74B86, tag 8C1AF91F05D6, lines 26–52; Theorem 11.16.3 source 9A061C42, tag 0A9CF0366804, lines 56–94. Examined separation, Runge induction and nondegenerate critical-point jets.
- §11.17, docs/sections/gauduchon-metrics-and-linear-mass--convex-norms-and-gauduchon-degrees--concave-neighborhoods-and-dual-norms/index.html, blob d49b7d4f2a213c8b70abfe2f337562202bb58dfb: Theorem 11.17.2, source 007613F4, tag 854B49CB03B9, lines 55–125. Examined vertical supporting-ball and negative Levi-plane arguments, but not the separate smoothing proposition §11.10.5.
- §11.18, docs/sections/gauduchon-metrics-and-linear-mass--convex-norms-and-gauduchon-degrees--curvature-and-projective-complement-exhaustions/index.html, blob fab309d460a8411fefcd1ef32a094927d6feea10: Lemma 11.18.1, source F8D5B741, tag 5022159B8350, lines 28–46; Theorem 11.18.2, source 9BF81039, tag B93CB03C68B7, lines 50–68, introductory assumptions lines 10–25.
- §11.19, docs/sections/gauduchon-metrics-and-linear-mass--convex-norms-and-gauduchon-degrees--negative-bundle-metrics-and-logarithmic-weights/index.html, blob e2ac81482338821333aa39bf2e357be8f110ad3f: Proposition 11.19.1, source 7A72F8E9, tag FD9DEB3AA8D6, lines 19–42, plus the strict fiber integrability threshold lines 49–58. Selected Hessian and fiber-order check only.

## POME-HERM-ADJOINT-C0-LP-LIPSCHITZ-001

**Status:** verified conditional deduction; **severity:** low, not a source theorem error. Assume all Fredholm and comparison conclusions of Lemma 11.24.1. Let X be a compact connected complex n-fold, dV a smooth positive volume, p>2n, p'=p/(p-1), and sigma a continuous positive Hermitian form. Let L_sigma u=tr_sigma(dd^c u) act W^{2,p}->L^p.

**Statement:** There is a unique nonnegative rho_sigma in L^{p'}(dV), with integral one, satisfying
\[
\int_X (L_\sigma u)\rho_\sigma\,dV=0\qquad(u\in W^{2,p}).
\]
For each fixed sigma there are epsilon,C>0 such that every positive continuous sigma' with ||sigma'-sigma||_{C^0}<epsilon satisfies
\[
\boxed{\|\rho_{\sigma'}-\rho_\sigma\|_{L^{p'}}\le C\|\sigma'-\sigma\|_{C^0}.}
\]
In particular, arbitrary directed C^0-convergent nets of positive forms yield strong L^{p'} convergence of normalized linear adjoint densities. This makes NO claim about the unresolved nonlinear weak adjoints in §11.25.

**Proof, existence and positivity.** By Lemma 11.24.1, A_sigma=I-L_sigma is invertible W^{2,p}->L^p. Set T=A_sigma^{-1}. The ABP comparison for a nonpositive zeroth-order coefficient makes T positivity preserving; T1=1. Sobolev embedding p>2n makes T:L^p->C(X) bounded (indeed into C^1) and T:C(X)->C(X) compact. Its dual therefore preserves Radon probabilities. Starting from a point mass nu_0, set nu_N=(1/N) sum_{k=0}^{N-1}(T^*)^k nu_0. On compact metrizable X the probabilities have a weak-star convergent subsequence. Since ||(T^*-I)nu_N||_{TV}<=2/N, a limit nu is T^*-invariant. For continuous g,
\[
|\nu(g)|=|\nu(Tg)|\le\|Tg\|_\infty\le C\|g\|_{L^p}.
\]
Thus nu=rho_sigma dV with rho_sigma>=0 in L^{p'} and integral one. For smooth u, (I-L_sigma)u is continuous; invariance implies \int (L_sigma u)rho_sigma=0. Sobolev density extends it to W^{2,p}. The codimension-one range of L_sigma has a one-dimensional L^{p'} annihilator by the lemma, proving normalized uniqueness. The Cesaro SEQUENCE here constructs one invariant probability on a compact metrizable space; it does not assume countable cofinality for an arbitrary directed net.

**Proof, Lipschitz stability.** Positive matrix inversion is locally Lipschitz in C^0, hence
\[
\|L_{\sigma'}-L_\sigma\|_{W^{2,p}\to L^p}
 \le C_0\|\sigma'-\sigma\|_{C^0}.
\]
The Neumann resolvent identity at A_sigma makes ||(I-L_sigma')^{-1}||_{L^p->W^{2,p}} uniformly bounded for nearby sigma'. The invariant-probability construction above consequently bounds ||rho_sigma'||_{L^{p'}} uniformly. Given f in L^p, set c=\int f rho_sigma dV. Since Ran L_sigma is closed and equals the annihilator hyperplane of rho_sigma, a zero-mean u solves L_sigma u=f-c with ||u||_{W^{2,p}}<=C_1||f||_p by the quotient bounded inverse theorem. Since rho_sigma' annihilates L_sigma',
\[
\int f(\rho_{\sigma'}-\rho_\sigma)dV
=\int [(L_\sigma-L_{\sigma'})u]\rho_{\sigma'}\,dV.
\]
Hölder, the uniform bound on rho_sigma', the coefficient operator estimate, and the quotient inverse bound give absolute value <= C||sigma'-sigma||_{C^0}||f||_p. Duality yields the boxed L^{p'} estimate. The inequality holds eventually along **every directed net**. QED.

**Proposed addition:** a corollary after Lemma 11.24.1, conditional on its analytic inputs, preserving existing labels and historical attribution. Useful for linear adjoint limits and perturbing continuous Hermitian backgrounds; do not conflate with nonlinear Monge–Ampere measures.

## POME-PROJ-COMP-BASE-PROPER-001

**Status:** proof gap / missing hypothesis, **medium severity**; NOT an established false theorem. Theorem 11.18.2 (source non-kahler-pluripotential-theory:9BF81039; tag B93CB03C68B7) states a q-convexity result for U_E=P(O_X+E)\P(O_X), but its opening at lines 10–25 does not assume compactness of X. The projective-complement proof at line 67 relies explicitly on: "Since the ambient projective bundle is compact, every sublevel set of psi is compact." This inference requires compact X. The project-wide convention at docs/sections/conventions/index.html:23 requires paracompactness, not compactness; §11.3:7 fixes a Hermitian form but does not impose global compactness.

**Concrete failure of the proof construction:** take X=C, E=X times C with its constant metric and s=0 (the printed curvature eigenvalue hypothesis is then vacuous). The proof's cutoff psi=chi(|v|^2)/|v|^2 vanishes for fixed large nonzero v; its zero sublevel contains the noncompact copy X times {v}. Hence THIS psi is not a proper exhaustion of U_E. In this example U_E itself is Stein, so this does not refute the convexity conclusion. Distinguish a missing proof from a false theorem.

**Repair:** explicitly require compact X in Theorem 11.18.2 (then the displayed proof is valid) and inherit that in Corollary 11.18.4, source B119F64B, permanent tag 18D33491ABFD, lines 91–105. Alternatively supply a new proper base exhaustion and prove it preserves the required number of positive Levi directions in the noncompact setting. Neither noncompact conclusion nor its repair has been established here.

## POME-STEIN-OKA-WEIL-INPUT-001

**Status:** external dependency, medium for the self-contained-proof preference, not a false theorem. The §11.16 opening at line 10 quotes Oka–Weil approximation on Stein holomorphically convex compacts. Lemma 11.16.1 actually proves the elementary two-disk polynomial separation, but Lemma 11.16.2 uses GLOBAL holomorphic approximation at lines 35–51 to construct a single function satisfying countably many displaced tests. Theorem 11.16.3 depends on this at lines 85–94. No independent internal proof of the global Oka–Weil theorem was established in this review. Retain attribution and record it as a genuine external analytic input for possible future internal proof.

## Verification boundary

Seven sections received specific proof/dependency reading, **none whole-section certified**. Earlier §11.24 CZ/ABP findings are not repeated. A separate finite-state rational Markov-resolvent illustration checks only elementary sign/normalization algebra; it is not a PDE proof. No Pome-wide tests/build, CI, formal verification, website publication, source/body/registry/tag edits, or merge. All excluded Demailly/Bergman/L2/OT/multiscale/positivity-loss work remains deferred-by-user.