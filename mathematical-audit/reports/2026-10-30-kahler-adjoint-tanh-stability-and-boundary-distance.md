# Mathematical audit — 2026-10-30: sharp Kähler adjoint stability and a boundary-distance crosscheck

**Reviewed production `main`:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.
**Audit-only branch:** `review/mathematical-audit`.
**Scope:** first selected *nonexcluded* review of §§24.6 and 24.7, with precisely delimited checks of §§11.34.1 and 12.6.1. No Demailly approximation/regularization, Bergman/L²/Ohsawa–Takegoshi, multiscale-atlas or positivity-loss completion work was undertaken. Existing exclusions retain status **deferred-by-user**.

## POME-KAHLER-ADJOINT-TANH-TV-001

**Severity:** low. **Status:** **verified conditional deduction**; the printed general Conjecture 24.7.1 is **not resolved**, and no printed theorem is false.

**Integrated reading-edition anchors on the pinned main:**

- §24.7, `docs/sections/problems-in-hermitian-pluripotential-theory--weak-gauduchon-adjoints/index.html`, blob `e9f7c4bcab38a796064574591d87fdbd9be58331`, section tag `C528B286A8D7`, physical lines **7–18**. Conjecture **24.7.1**, source `non-kahler-pluripotential-theory:68ABC3B8`, permanent tag `7C0A1CE5EC77`, physical **10–12**. Line 15 states the known closed-Kähler case but does not provide the sharp nonlinear stability estimate below.
- §11.34, `docs/sections/normalization-and-weak-adjoint-measures--supporting-probability-measures/index.html`, blob `a8afa97be049b56b6c7d18302499364022feaa39`; supporting inequality **(11.34.1)**, source `non-kahler-pluripotential-theory:44A5BEA2`, permanent tag `4DA0C1CF8861` (also independently read `docs/tag/4DA0C1CF8861/index.html`, blob `d50b82567386271130ffa20e60cd9cc11df23fc4`). The sign is `B(G) <= B(F) - integral (G-F) dnu`.
- This is an explicit *closed Kähler benchmark*. It neither invokes a weak nonlinear linearization in a Hermitian background nor assumes regularity of solutions for nonsmooth F.

**Hypotheses and notation.** Let \(X\) be a connected compact Kähler manifold, \(\omega\) a fixed Kähler form, and \(\mathrm dV\) a smooth positive probability volume form. Work with the nonsingular reference \(\varphi=0\). Let \(M=\int_X\omega^n>0\), with the same overall Monge–Ampère normalization as the equation, and let \(F,G,H,K\in C(X,\mathbb R)\). The closedness of \(\omega\) and the full-mass identity for bounded solutions imply that the scalar attached to
\[
 \mathrm{MA}_\omega(u)=c_0(F)e^F\,\mathrm dV
\]
is forced to equal
\[
 c_0(F)=\frac{M}{Z_F},\qquad Z_F=\int_X e^F\,\mathrm dV.
\]
The existence of a solution for each continuous F is the *existing* Kähler MA input; only the scalar identity and ensuing functional calculation are proved here.

Define
\[
 B_0(F)=\log M-\log Z_F,\qquad
 \nu_F=\frac{e^F\,\mathrm dV}{Z_F}.
\]
Then \(B_0:C(X)\to\mathbb R\) is real analytic as a map of real Banach spaces, and
\[
 D B_0(F)[H]=-\int_X H\,\mathrm d\nu_F,\qquad
 D^2B_0(F)[H,K]=-\operatorname{Cov}_{\nu_F}(H,K).
\]
In particular, the supporting-probability set of (11.34.1) is exactly \(\mathcal A_0(F)=\{\nu_F\}\). More quantitatively, for the dual total-variation norm \(\|\sigma\|_{\mathrm{TV},*}:=\sup_{\|h\|_\infty\le1}|\int h\,\mathrm d\sigma|\) (twice the usual probabilistic TV distance for two probabilities),
\[
 \boxed{\quad
 \|\nu_F-\nu_G\|_{\mathrm{TV},*}
 \le 2\tanh\!\left(\frac{\operatorname{osc}_X(G-F)}4\right)
 \le \|G-F\|_\infty.
 \quad}
\]
The first inequality has the *best possible universal right-hand side at every prescribed positive oscillation*, even for smooth F and G on any fixed compact positive-dimensional Kähler manifold with fixed smooth \(\mathrm dV\). The second has optimal infinitesimal constant one.

**Complete proof.** The exponential power series converges locally uniformly in the Banach algebra \(C(X)\), so \(F\mapsto Z_F\) is analytic and positive, and \(\log Z_F\) is locally real analytic. Differentiating under the integral establishes the derivative and covariance identities. Convexity of \(\log Z\) gives the supporting inequality with the sign of (11.34.1). Differentiability implies uniqueness of the representing supporting probability.

For the nonperturbative bound, put \(h=G-F\), \(a=\min_X h\), \(b=\max_X h\), \(A=e^a\), \(C=e^b\), and \(L=e^h\in[A,C]\). Relative to \(\nu_F\), let \(m=\int L\,\mathrm d\nu_F\in[A,C]\). Then
\[
 \nu_G=(L/m)\nu_F,\qquad
 \|\nu_G-\nu_F\|_{\mathrm{TV},*}=\frac1m\int|L-m|\,\mathrm d\nu_F.
\]
For \(A\le x\le C\), convexity of \(x\mapsto|x-m|\) puts it below its endpoint chord:
\[
 |x-m|\le \frac{C-x}{C-A}(m-A)+\frac{x-A}{C-A}(C-m).
\]
Taking expectations and using \(\int L=m\) gives
\[
 \frac1m\int|L-m|\,\mathrm d\nu_F
 \le\frac{2(C-m)(m-A)}{(C-A)m}.
\]
The right-hand side is maximized over \(m\in[A,C]\) at \(m=\sqrt{AC}\) (differentiate \((A+C)-m-AC/m\)); its value is
\[
 2\,\frac{\sqrt C-\sqrt A}{\sqrt C+\sqrt A}
 =2\tanh((b-a)/4).
\]
Since \(b-a\le2\|G-F\|_\infty\) and \(2\tanh(t/2)\le t\) for \(t\ge0\), the final Lipschitz bound follows.

**Sharpness (including smooth data).** Given \(d=b-a>0\), write \(q=e^{d/2}\) and select a measurable set \(E\subset X\) of \(\mathrm dV\)-mass \(p=1/(q+1)\); the smooth positive volume is nonatomic. Set \(F=0\) and \(G=d\,\mathbf1_E\) temporarily. Then \(L=e^G\) takes values \(1,q^2\), has mean \(m=q\), and direct evaluation gives
\[
 \|\nu_G-\nu_0\|_{\mathrm{TV},*}
 =\frac{2(q-1)}{q+1}
 =2\tanh(d/4).
\]
Approximate \(\mathbf1_E\) in \(\mathrm dV\)-measure by smooth functions \(g_j\), with \(0\le g_j\le1\), whose essential oscillations tend to one. Taking \(G_j=dg_j\) and using dominated convergence of their exponentials and normalization constants gives the asserted arbitrarily sharp *smooth* examples. Taking \(d\downarrow0\) shows sharpness of the Lipschitz constant one. These are supremum statements; equality for a nonconstant continuous G on connected X is not asserted.

**Proposed addition and dependents.** Optional self-contained quantitative remark after §24.7.1 or Eq. 11.34.1 stating the exact Kähler log-partition formula, covariance Hessian and sharp tanh bound. The result supplies a benchmark for the distinct *open* Hermitian uniqueness/weak-adjoint problem and for comparisons of supporting measures; it is **not** a proof of Conjecture 24.7.1 for general Hermitian backgrounds, and does not close any earlier ledger entries.

## First direct selected §24.6 crosscheck (no new finding)

**Reading anchors:** `docs/sections/problems-in-hermitian-pluripotential-theory--degeneration-orders-and-finite-distance-boundaries/index.html`, main blob `692b010fe882c30c0a612f07e29e0d2fb3307a23`, section tag `7B777ACFF4E8`, physical lines **7–20**, **23–33**, problem **24.6.1** source `non-kahler-pluripotential-theory:433C9481` / permanent tag `B93ADA1B6064`. Compared with **Proposition 12.6.1**, `docs/sections/a-gauduchon-variational-volume--the-hessian-metric-and-its-completion/index.html`, main blob `23a7f2a1dab791569c39a0ff5f056f52bfc200fe`, source `non-kahler-pluripotential-theory:9494E2B6`, tag `88C1708A920C`, lines **25–62**.

Recomputed directly the *degree-one* homogeneity \(\lambda_\mu(s\theta)=s\lambda_\mu(\theta)\) (do **not** substitute degree n for the *root* volume): \(g_\theta(\theta,\theta)=1\), \(g_\theta(\theta,\chi)=D\log\lambda_\mu(\theta)[\chi]\), and \(g_{s\theta}(s\chi,s\eta)=g_\theta(\chi,\eta)\). Thus the printed exact product metric and unit coefficient of the logarithmic radial distance agree with the conventions. It verifies only the specified local finite-dimensional identities and the logical boundary setup of §24.6, not the general metric-completion problem or all referenced degeneration examples. **No new stable finding ID** is assigned to this already printed formula.

## Coverage and integrity

- **New actual nonexcluded review:** §§24.7.1 and 24.7 introductory/Kähler normalization comparison; §24.6.1 and its radial geometry with §12.6.1 as a selected checked dependency. §11.34.1 inspected for the sign and supporting-measure convention. No whole section, whole theorem dependency chain, chapter, or project is certified.
- **Existing inventory unchanged:** 25 current chapters, 747 unique numbered section rows, zero complete-section certifications.
- **Statuses retained:** all prior confirmed errors, proof gaps, external dependencies and conditional repairs remain in the ledger; Demailly approximation/regularization and its dedicated Bergman, L², Ohsawa–Takegoshi, multiscale and positivity-loss proof programme remain **deferred-by-user**, neither resolved nor reopened.
- **No source/registry/canonicalization/permanent-tag/main/docs modifications, builds, GitHub Actions CI, publication or formal verification.** Only audit Markdown is proposed for this branch.
