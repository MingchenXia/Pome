# Closed-class scalar continuity without a uniform density bound: exact Vitali criterion and a shrinking-cap obstruction

**Date:** 2026-11-12. **Stable finding ID:** \`POME-SCALAR-VITALI-UNBOUNDED-SPIKE-001\`. **Severity:** low. **Status:** **verified conditional deduction** (the printed theorem is correct and its uniform-boundedness hypothesis is not being relaxed). **Reviewed production main:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`. **Review branch:** \`review/mathematical-audit\`.

## Exact integrated sources and coverage

1. \`docs/sections/normalization-and-weak-adjoint-measures/index.html\`, blob \`031b5d62d25d7ff03d95e4a14988399527cc946a\`, §11.32 standing **connected compact** and model-reference hypotheses, physical line 7, section permanent tag \`7091FEDB43F0\`. This is an *assumption check*, not a theorem-level certification.
2. \`docs/sections/normalization-and-weak-adjoint-measures--the-scalar-functional/index.html\`, blob \`fff86de757578ed2be369ba752123f62f3d31044\`: Equation 11.33.1, source \`non-kahler-pluripotential-theory:19974F5F\`, permanent \`9D47DB96B6E3\`, physical lines 10–20; Theorem 11.33.5, source \`non-kahler-pluripotential-theory:D502EBBF\`, permanent \`5E3583383688\`, physical lines 89–116. The latter explicitly requires **uniformly bounded** \(F_j,F\) and \(L^1(dV)\) convergence; its proof exploits this in the exponential Lipschitz step.
3. \`docs/sections/normalization-and-weak-adjoint-measures--entropy-and-the-closed-case/index.html\`, blob \`0710d0732ae7ef81de3d3d62206a0f9c6b5d321f\`: Equation 11.37.2, source \`non-kahler-pluripotential-theory:65FF799F\`, permanent \`803909FECEC0\`, physical lines 54–61. This is the exact *closed-class* log-partition and supporting-probability formula used below.
4. §§11.34–11.35 are **dependent context only** for supporting probabilities and their convex dual. No general nonclosed Hermitian scalar existence, regularization, or non-pluripolar limit theorem is certified here.

## Precise result: necessary and sufficient replacement in the closed case

Let \(X\) be a connected compact Kähler manifold, \(dV\) a smooth positive finite volume measure, and \(\theta\) a Kähler form with a fixed model reference \(\varphi\) of positive finite ordinary-type mass \(m_\varphi\). Take a **sequence** of individually bounded real measurable \(F_j\), not necessarily uniformly bounded, and bounded real \(F\), with \(F_j\to F\) in \(dV\)-measure (in particular this applies to \(L^1(dV)\) convergence). Assume the prescribed ordinary-type equation and the exact closed-class mass formula of Eq. 11.37.2. Write
\[
Z_j=\int_X e^{F_j}\,dV,\quad Z=\int_Xe^F\,dV,\quad
B_\varphi(F_j)=\log m_\varphi-\log Z_j,\quad
\nu_j=\frac{e^{F_j}}{Z_j}\,dV.
\]
The following are **equivalent**:

(a) \(B_\varphi(F_j)\to B_\varphi(F)\);

(b) \(Z_j\to Z\);

(c) \(e^{F_j}\to e^F\) in \(L^1(dV)\);

(d) the family \(\{e^{F_j}:j\geq1\}\) is **uniformly integrable** with respect to \(dV\).

Under these equivalent conditions the supporting probabilities converge **in total variation**:
\[
d_{\mathrm{TV}}(\nu_j,\nu_F)
=\tfrac12\bigl\|e^{F_j}/Z_j-e^F/Z\bigr\|_{L^1(dV)}\longrightarrow0.
\]
The claim is specific to the **closed fixed-mass situation**. It does not replace the proof of §11.33.5 in general nonclosed Hermitian geometry, where the total non-pluripolar mass need not remain fixed. It is formulated for sequences only, with no unwarranted assertion about arbitrary nets.

**Proof.** (a)\(\Leftrightarrow\)(b) follows by the printed logarithmic formula and \(0<Z<\infty\). Because exponentiation is continuous, \(e^{F_j}\to e^F\) in measure. (c)\(\Rightarrow\)(b) by integration; (c)\(\Rightarrow\)(d) by uniform integrability of an \(L^1\)-convergent sequence. Conversely, (d) and convergence in measure imply (c) by the finite-measure Vitali theorem: truncate the integrands uniformly on small sets and apply bounded convergence in measure to their truncations. Finally (b)\(\Rightarrow\)(c) is the nonnegative **Scheffé lemma**: from any subsequence choose a further subsequence along which \(e^{F_j}\to e^F\) a.e. If their integrals tend to \(Z\), then
\[
\int_X|e^{F_j}-e^F|\,dV
=Z_j+Z-2\int_X\min(e^{F_j},e^F)\,dV\to0
\]
along that further subsequence, by dominated convergence for the minimum (bounded by \(e^F\in L^1\)). Every subsequence has such a further subsequence, hence the full \(L^1\) sequence converges. The displayed total-variation conclusion now follows from \(Z_j\to Z>0\) and the triangle inequality. No singular product limit or elliptic compactness is interchanged.

## Explicit sharp obstruction on \(\mathbb P^1\)

Normalize \(\int_{\mathbb P^1}\omega_{\rm FS}=1\), and take \(dV=\theta=\omega_{\rm FS}\), \(\varphi=0\). In the affine coordinate \(z\), set \(y=|z|^2/(1+|z|^2)\). The Fubini–Study moment pushforward of \(\omega_{\rm FS}\) is Lebesgue measure \(dy\) on \([0,1]\). Let
\[
a_j=e^{-j},\quad E_j=\{y\leq a_j\},\quad
F_j=j\,\mathbf1_{E_j}\quad(j\geq1).
\]
Thus every \(F_j\) belongs to \(L^\infty\) **individually**, but \(\|F_j\|_\infty=j\), and
\[
\|F_j\|_{L^1(\omega_{\rm FS})}=j e^{-j}\to0,\qquad
Z_j=\int e^{F_j}\omega_{\rm FS}=2-e^{-j}\to2,\qquad Z(0)=1.
\]
Consequently
\[
B_0(F_j)=-\log(2-e^{-j})\to-\log2\ne B_0(0)=0.
\]
The supports of the positive spikes shrink to a point, but their **exponential** mass does not: \(\int_{E_j}e^{F_j}\omega_{\rm FS}=1\). This proves failure of uniform integrability and of any extension of Theorem 11.33.5 based on \(L^1\) convergence alone without its common upper bound.

The supporting probability is \(\nu_j=e^{F_j}\omega_{\rm FS}/Z_j\); since its density is \(>1\) on \(E_j\) and \(<1\) outside,
\[
d_{\mathrm{TV}}(\nu_j,\omega_{\rm FS})
=\nu_j(E_j)-\omega_{\rm FS}(E_j)
=\frac1{2-e^{-j}}-e^{-j}\longrightarrow\frac12.
\]
Thus neither the scalar **nor its supporting probability** is continuous under this unrestricted \(L^1\) perturbation.

**Direct realization without invoking the general singular MA existence theorem.** Put \(s=\log|z|^2\), \(y(s)=e^s/(1+e^s)\), and \(f_j(y)=e^{j\mathbf1_{[0,a_j]}(y)}/Z_j\). Define
\[
h_j(y)=\int_0^y f_j(t)\,dt,\quad
\Psi_j'(s)=h_j(y(s)),\quad
\Psi_j(s)=\int_{-\infty}^s h_j(y(\tau))\,d\tau.
\]
Then \(h_j(0)=0\), \(h_j(1)=1\), and a.e. \(\Psi_j''(s)=f_j(y(s))y(s)(1-y(s))\). The reference radial potential \(\Phi(s)=\log(1+e^s)\) has \(\Phi''=y(1-y)\). Hence on \(\mathbb C^\times\),
\[
dd^c\Psi_j=f_j(y)\,dd^c\Phi
=\frac{e^{F_j}}{Z_j}\omega_{\rm FS}.
\]
Since \(f_j\) is bounded above and below by positive constants for fixed \(j\), \(\Psi_j-\Phi\) has finite limits at \(s=\pm\infty\) (its derivative is \(O(e^s)\) at \(-\infty\), \(O(e^{-s})\) at \(+\infty\)); it extends to a bounded continuous global \(\omega_{\rm FS}\)-psh potential \(u_j\) on \(\mathbb P^1\), with no extra atom at the poles. After adding a constant, \(\sup u_j=0\). Thus the prescribed MA equations whose scalars are computed above really have bounded-potential solutions, even without relying on the general existence theory. The jump of \(F_j\) is permitted by the printed measurable-density hypotheses.

For contrast, \(G_j=-j\mathbf1_{E_j}\) has the *same* \(L^1\)-norm decay but \(\int e^{G_j}\omega_{\rm FS}=1-e^{-j}+e^{-2j}\to1\). The obstruction is loss of control of **positive exponential tails**, not merely absence of a common lower bound.

## Classification, dependencies, and nonduplication

- **Severity/status:** low / **verified conditional deduction**. **No printed statement is false.** Theorem 11.33.5 retains its valid common \(L^\infty\) bound, whereas its unbounded-density extension fails in the explicit Kähler model.
- **New content:** an **if-and-only-if uniform-integrability criterion** for closed-class scalar continuity, its total-variation consequence, and a completely realized \(\mathbb P^1\) shrinking-cap counterexample with exact scalar and TV limits. The previously recorded 2026-10-31 \`POME-CLOSED-LOGPART-SHARP-L1-TV-001\` established the optimal **uniform-box** Lipschitz coefficient; the 2026-11-07 closed-class KL/Fenchel note addressed bounded derivatives and entropy. Neither is repeated or reclassified here.
- **Proposed documentation-only correction, not applied:** immediately after §11.33.5 or Eq. 11.37.2, insert a clearly labeled *closed-class conditional* remark stating the Vitali criterion and this optimality counterexample; do not weaken the general Hermitian theorem or edit source/registry/permanent tags directly.
- **Dependents potentially affected by an unjustified unbounded-density generalization:** scalar continuity §11.33.5, supporting probabilities §11.34, convex dual §11.35 and closed-case formula §11.37.2. These exact printed results are not contradicted; a purported unconditional \(L^1\) convergence of scalar or supporting probabilities would be.
- **Actual coverage:** selected proof-level recheck of §11.33.5 and §11.37.2, §11.32 hypotheses only. All were previously partly inspected; **+0 first-visited numbered sections; +0 fully certified sections**. The baseline current table of contents contains **25 chapters and 747 numbered sections**. The general model-mass statement and singular PDE existence remain internal conditional inputs for the abstract theorem; the explicit \(\mathbb P^1\) obstruction above is constructive.
- **Owner exclusion:** Demailly approximation/regularization and the dedicated Bergman, \(L^2\), Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof-completion programme remain **deferred-by-user**, neither reopened nor certified. No tests, build, GitHub Actions CI, website publication, production-source changes or source-repository writes were performed.
