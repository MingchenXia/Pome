# Magnetic spectral-atom differentiation and a cross-chapter tensor/divisor audit

**Date:** 2026-11-24 (Asia/Shanghai). **Main audited:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. **Status:** current integrated reading edition only, not source-repository or transitive proof-chain certification.

## Exact inspected material

- **Entire current §2.19**, `docs/sections/concrete-completed-tensor-products/index.html` (main blob `358f584ab4004b3531629e87f1dd73bdea1256d4`, physical HTML lines 5–82). Source labels `demailly-complex-geometry:E56C631F`, `:4D711A6B`, `:C614F79A`; permanent tags `84C71E271314` (Proposition 2.19.1), `96A052277244` (Proposition 2.19.2), `C9CDFE118A86` (Proposition 2.19.3). Checked the actual coefficient proofs of the projective/injective tensor identities, arbitrary index sets, and the finite-barycentric approximation for compact spaces that are not necessarily Hausdorff. The exact crossnorms and the non-Hausdorff quantifier are retained. Previous *selected* §2.19 proofs, including the 2026-11-04 projective/injective Fourier gap, remain historical work, not new findings here.
- **Entire current §2.24**, `docs/sections/magnetic-models-and-spectral-localization/index.html` (blob `ee89de7d23cc96a8546c736ac7d068546b126f3a`, physical HTML lines 5–110). Lemma 2.24.2 tag `3E8E852DB903` (line 11), measures (2.24.4–5) tags `6919A4A3FD8F`, `72E6618A3A3C` (lines 31–45), Lemma 2.24.6 source `demailly-complex-geometry-2FD17158`, tag `0F14CB3D46F3` (lines 49–71), Proposition 2.24.8 source `demailly-complex-geometry-7DBC83A8`, tag `C554004EA447` (lines 76–110), equation (2.24.10) tag `B6FBF3F18EA3` (lines 100–109). Checked oscillator modes, zero-field density, all-rank local mass bounds, quadratic-form spectral comparison, and Dirichlet localization. The existing 2026-10-27 fixed-boundary-width **O(R^-1)** improvement and 2026-11-15 magnetic midpoint bounds are **previous findings, not new progress**.
- **Entire expository/problem §24.12**, `docs/sections/questions-on-relative-canonical-classes-and-cotangent-tensors/index.html` (blob `7b2763d35ab776a5bb0a17a34e8a2e6b3546358f`, physical lines 5–20), Conjecture 24.12.1 tag `3E0B91E5DF69`, Question 24.12.2 tag `2C2AE81C4020`. Both are expressly open questions, not presented as theorems; no resolution is asserted.
- **Repeat-only dependency spot check** §20.7, `docs/sections/meromorphic-sections-and-divisor-classes/index.html` (blob `d0c40d1e3f6f515eb13169ed1cd3fb447ca161c8`), Proposition 20.7.3 tag `ACC6D09EDDD9`, where the displayed Poincaré–Lelong sign agrees with the global `dd^c=(i/2π)∂∂bar` convention and holomorphic-frame transition ratios. A 2026-11-21 direct full review already exists; no newly earned coverage or new finding for this repeat.
- **Selected preliminary dependency context** §2.9 (blob `b2366d2a9604cc6f39cf45ced697905978dff8ab`): Fourier normalization, Plancherel and Riesz energy in §§2.9.2–6, and Hessian multiplier definitions around §§2.9.9–12. This is *not* full-section review. No new Calderón–Zygmund or singular-integral proof certification is asserted.

## Finding POME-MAGNETIC-RIESZ-ATOM-C1-LOCUS-001

**Severity:** low. **Status:** verified conditional deduction, not a printed error or an independent spectral theorem. **Exact input:** the locally finite nonnegative convolution measure \(\mu_b\) in (2.24.4–5) and its continuous-test convergence from Lemma 2.24.6. Here \(n\ge1\), \(b=(b_1,\ldots,b_n)\in[0,\infty)^n\), \(E\in\mathbb R\), and
\[
 \nu_b(E)=\mu_b([0,E)),\qquad r_b(E)=\int(E-t)_+\,d\mu_b(t).
\]
**Conclusion:** the exact left/right energy derivatives are
\[
 \partial_E^-r_b(E)=\mu_b([0,E))=\nu_b(E),\qquad
 \partial_E^+r_b(E)=\mu_b([0,E]).
\]
Thus \(r_b\) is differentiable at \(E\) exactly when \(\mu_b(\{E\})=0\). More explicitly,
\[
 \mu_b(\{E\})=
 \begin{cases}
 0,&\text{if some }b_j=0,\\
 \displaystyle\left(\prod_{j=1}^n\frac{b_j}{2\pi}\right)
 \#\left\{p\in\mathbb Z_{\ge0}^n:
 E=\sum_{j=1}^n(2p_j+1)b_j\right\},&\text{if every }b_j>0.
 \end{cases}
\]
The multiplicity is finite at any fixed energy. Consequently the counting function \((b,E)\mapsto\nu_b(E)\) is jointly continuous **at every point** where the limiting \(\mu_b\) has no atom at \(E\). Conversely, if \(\mu_b(\{E\})>0\), even varying \(E\) alone produces a jump, hence joint continuity fails. In particular one zero-field pair removes all atomic nondifferentiability, while at an all-positive Landau threshold the Riesz mean has a genuine corner.

**Complete elementary argument.** For fixed \(b,E\), local finiteness gives a finite mass on a bounded interval containing \(E\). Difference quotients of \( (E-t)_+\) for \(h\downarrow0\), with derivatives \(1_{\{t\le E\}}\) on the right and \(1_{\{t<E\}}\) on the left, are bounded by one on that interval; dominated convergence proves both formulas (outside the interval the quotient vanishes). If a \(b_j=0\), then \(\mu_{b_j}=dt/(4\pi)\) is atomless; convolution of any locally finite measure supported in \([0,\infty)\) with it has no atoms, by Tonelli on compact intervals. If all \(b_j>0\), expanding the finite convolutions gives exactly the displayed weighted multiplicity, with finite count because each \(p_j\le E/(2b_j)\). Lemma 2.24.6 establishes vague convergence \(\mu_{b^{(k)}}\to\mu_b\), including transitions to zero field. If \(\mu_b(\{E\})=0\), choose nearby energies \(E-\delta\), \(E+\delta\) with no endpoint atoms, sandwich \(\mu_{b^{(k)}}([0,E_k))\) between the corresponding fixed endpoint distribution functions for \(E_k\to E\), and use weak convergence plus \(\delta\downarrow0\). The case \(E\le0\) is covered by support in \([0,\infty)\) and zero atom at zero. Conversely an atom at \(E\) forces \(\nu_b(E+\epsilon)-\nu_b(E)\ge\mu_b(\{E\})\) for each \(\epsilon>0\), so continuity fails.

**Interpretation:** this identifies the *precise* differentiability/parameter-continuity locus, not merely the strict-counting convention printed after (2.24.5). A legitimate dependent may differentiate \(r_b(E)\) only at non-atomic energies; the \(C^0\) finite-volume uniform Riesz estimate of Proposition 2.24.8 alone gives no \(C^1\) estimate across Landau levels. Do **not** replace \([0,E)\) by \([0,E]\) in the existing formula or canonicalization. No new published-text correction required. The harmonic-oscillator spectral decomposition, and all unreviewed upstream operator domain assertions, remain dependencies, not transitively certified.

## Other direct checks and boundaries

- §2.19.1: a finite tensor's projective \(\ell^1\) norm equals its coefficient sum after finite-coordinate truncation; \(\ell^1(I)\) vectors have countable support even for uncountable \(I\). No unsanctioned sequential-compactness assertion.
- §2.19.2: the injective norm is the coefficient supremum, and finite matrices are dense in \(c_0(I\times J)\); its polar assertion does **not** identify the entire dual with the projective tensor product.
- §2.19.3: finite sup-norm nets of the compact image \(x\mapsto f(x,\cdot)\) yield continuous barycentric coefficient functions on *arbitrary compact* \(K\); the proof uses no Hausdorff separation of \(K\). The quantitative finite-net argument is already printed and **not** submitted as a new deduction.
- §2.24.8: the full-space spectral Riesz upper bound, localized positive-contraction lower bound, and varying-field uniform constants are internally consistent in the reviewed steps; the **O(1/R)** strengthening belongs to 2026-10-27, not this run.
- §24.12: neither conjecture is a proven theorem; the relative canonical result's rational Hodge/two-form hypotheses and the cotangent numerical-dimension question are kept separate.

**New confirmations this run:** zero false printed theorems, zero independently established local proof gaps, one new conditional spectral deduction, two mathematical sections fully directly read (§§2.19,2.24), one whole problem/expository section read (§24.12), one repeat-only (§20.7), one selected (§2.9); historical first visits unresolved. **Zero complete transitive proof chains certified**. No build, tests, CI, automatic publication, main/source/registry/tag edits. Demailly approximation/regularization and all designated Bergman/L²/Ohsawa–Takegoshi/multiscale/positivity-loss programmes remain **deferred-by-user**, neither verified nor resolved. The source identifier `demailly-complex-geometry` is provenance only; no excluded proof-completion work was undertaken.
