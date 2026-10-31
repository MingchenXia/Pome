# Audit: fiberwise multiplier-ideal collapse versus positive-mass growth on a curve (2026-10-31)

**Reviewed production main:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`.
**Audit-only branch:** \`review/mathematical-audit\`.
**Finding:** **POME-FIBER-POSMASS-DESCENT-OBSTRUCTION-001** — **low / verified conditional deduction**. It is an explicit obstruction to a *universal* positive-mass reference in the question of §24.10.2; **it does not contradict Problem 24.10.2**, which asks for sufficient hypotheses and already warns that not every selecting weight need admit such a reference. No original theorem or lemma is shown false.

## Exact integrated anchors and provenance

| Object | Production file and blob | Stable original source label / permanent tag | Physical HTML lines |
| --- | --- | --- | --- |
| Problem 24.10.2 (descent and \(o(m^q)\) reference) | \`docs/sections/problems-in-hermitian-pluripotential-theory--sections-kernels-and-the-dimension-of-growth/index.html\`, \`172c54fa873ed9a051dc85ddfa4c28e1d4bcdac9\` | \`non-kahler-pluripotential-theory:3C96DD18\` / \`4813DF6B9029\` | 39–55, especially 42–51 |
| Lemma 5.37.1 (normal logarithmic pole and ideal exponent) | \`docs/sections/plurisubharmonic-functions-and-singularities--multiplier-ideals-and-logarithmic-poles/index.html\`, \`9256668b88735f821d06b0919466a6a8cba777ed\` | \`non-kahler-pluripotential-theory:94144E8D\` / \`C21A2A6F9E07\` | 10–30 |
| Lemma 5.37.7 (ideal pullback by a *submersion*) | same §5.37 file and blob | \`non-kahler-pluripotential-theory:BD00E282\` / \`2FA053FE56D9\` | 135–163 |
| Example 5.37.8 (critical-map pullback counterexample) | same §5.37 file and blob | \`non-kahler-pluripotential-theory:FD30A3D0\` / \`E39EAA145A67\` | 167–177 |

The local multiplier ideal uses \(|f|^2e^{-u}\); \(\mathrm{dd}^c=(i/2\pi)\partial\bar\partial\), so \(\mathrm{dd}^c\log|z|^2=[0]\). This review is **not** about Demailly regularization, Bergman approximation, \(L^2\) extension or the excluded proof-completion programme. Lemma 5.37.7 applies to pullbacks of *base* weights; it must not be applied to the fiber-dependent weight below.

## 1. Elementary one-dimensional zero-atom integrability

**Lemma.** If \(v\) is subharmonic near \(0\in\mathbf C\) and its Riesz measure \(\lambda=\mathrm{dd}^cv\) has no atom at \(0\), then \(e^{-pv}\) is integrable on some neighborhood of \(0\) for every fixed finite \(p>0\).

**Proof.** Choose a sufficiently small disk \(D_R\) with \(p\lambda(D_R)<1\); this is possible because \(\lambda(\{0\})=0\). The local Riesz decomposition gives, on \(D_R\),
\[
 v(z)=h(z)+\int_{D_R}\log|z-\zeta|^2\,d\lambda(\zeta),
\]
with \(h\) harmonic (the bounded smooth local correction is harmless). On \(D_{R/2}\), \(h\) is bounded below. If \(a=\lambda(D_R)>0\), Jensen's inequality for the probability \(\lambda/a\) yields
\[
 e^{-pv(z)}\le C\int_{D_R}|z-\zeta|^{-2pa}\frac{d\lambda(\zeta)}a .
\]
The right-hand side is integrable in \(z\in D_{R/2}\), uniformly in \(\zeta\in D_R\), because \(pa<1\). If \(a=0\), \(v\) is harmonic on the smaller disk. This uses only Riesz decomposition and Jensen, not an \(L^2\) extension theorem. \(\square\)

## 2. Positive non-pluripolar mass forces linear growth on \(\mathbf P^1\)

Let \(\theta=\omega_{\mathrm{FS}}=c_1(\mathcal O_{\mathbf P^1}(1),h_{\mathrm{FS}})\), with \(\int_{\mathbf P^1}\theta=1\), and let \(\psi\in\operatorname{PSH}(\mathbf P^1,\theta)\). Put
\[
 \mu=\theta+\mathrm{dd}^c\psi,\qquad
 M=\int_{\mathbf P^1}\langle\mu\rangle>0,\qquad
 W_m=H^0\bigl(\mathbf P^1,\mathcal O(m)\otimes\mathcal I(m\psi)\bigr).
\]
The measure \(\mu\) is positive of total mass \(1\). Let \(\nu_x=\mu(\{x\})\) denote its atomic masses. Every positive atom is a logarithmic pole, so it is excluded from the one-dimensional non-pluripolar measure. Consequently
\[
 \sum_{x\in\mathbf P^1}\nu_x\le 1-M. \tag{1}
\]

**Claim (sharp bound).** For every integer \(m\ge1\),
\[
 \boxed{\dim W_m\ \ge\ m-\sum_x\lfloor m\nu_x\rfloor+1\ \ge\ mM+1.} \tag{2}
\]

**Proof.** At a point \(x\), choose a local smooth potential \(\rho\) of \(\theta\). The function \(u=\psi+\rho\) is subharmonic and
\[
 u=\nu_x\log|z|^2+v,\qquad \mathrm{dd}^cv\ge0,\qquad
 (\mathrm{dd}^cv)(\{x\})=0.
\]
Put \(k=\lfloor m\nu_x\rfloor\) and \(\beta=m\nu_x-k\in[0,1)\). For any holomorphic germ \(g\in(z^k)\),
\[
 |g|^2e^{-m\psi}\le C|z|^{-2\beta}e^{-mv}.
\]
Choose Hölder conjugates \(p,p'>1\) with \(\beta p'<1\) (for \(\beta=0\), any conjugates). The preceding zero-atom lemma gives \(e^{-mpv}\in L^1_{\mathrm{loc}}\), while \(|z|^{-2\beta p'}\in L^1_{\mathrm{loc}}\). Thus
\[
 (z^{\lfloor m\nu_x\rfloor})\subseteq \mathcal I(m\psi)_x.
\]
Only finitely many \(x\) have \(\lfloor m\nu_x\rfloor>0\). Set \(D_m=\sum_x\lfloor m\nu_x\rfloor[x]\). The local inclusions imply \(\mathcal O(-D_m)\subseteq\mathcal I(m\psi)\), hence
\[
 \dim W_m\ge h^0(\mathbf P^1,\mathcal O(m)(-D_m))
 =m-\deg D_m+1.
\]
Equation (1) gives \(\deg D_m\le m(1-M)<m\), justifying the last equality and (2). \(\square\)

**Sharpness.** For \(0<\alpha<1\), take \(\psi=\alpha\log|s_x|_{h_{\mathrm{FS}}}^2\) for a section \(s_x\) vanishing once at \(x\). Then
\(\mu=(1-\alpha)\theta+\alpha[x]\) and \(M=1-\alpha\). The direct radial calculation of §5.37.1 gives
\(\mathcal I(m\psi)=\mathcal O(-\lfloor m\alpha\rfloor[x])\), so
\[
 \dim W_m=m-\lfloor m\alpha\rfloor+1,\qquad
 \lim_{m\to\infty}\frac{\dim W_m}{m}=M.
\]
Thus the coefficient \(M\) in (2) cannot be improved uniformly.

## 3. Smooth-submersion example with identically vanishing selected spaces

Take
\[
 X=\mathbf P^1_b\times\mathbf P^1_f,\quad B=\mathbf P^1_b,\quad
 \pi=\operatorname{pr}_b,\quad A=\mathcal O_B(1),\quad\theta=\omega_{\mathrm{FS},b}.
\]
Fix \(p\in\mathbf P^1_f\), a section \(s_p\) of \(\mathcal O_f(1)\) with zero \(p\), and any \(c>0\). Set
\[
 D=B\times\{p\},\quad
 \varphi=c\log|s_p|^2_{h_{\mathrm{FS},f}},\quad
 \omega=\operatorname{pr}_b^*\omega_{\mathrm{FS},b}
       +c\,\operatorname{pr}_f^*\omega_{\mathrm{FS},f}.
\]
Both factors and \(X\) are Kähler; \(\omega\) is a Hermitian form. Poincaré–Lelong gives
\[
 \omega+\mathrm{dd}^c\varphi
   =\operatorname{pr}_b^*\omega_{\mathrm{FS},b}+c[D]\ge0,
\]
so \(\varphi\in\operatorname{PSH}(X,\omega)\), exactly as required in Problem 24.10.2.

For \(mc\ge1\), every nonzero \(s\in H^0(B,A^m)\) fails the ideal condition along \(D\): near any \(b\) with \(s(b)\ne0\), its pullback is independent of the fiber coordinate \(w\) and
\[
 |\pi^*s|^2e^{-m\varphi}\asymp |s(b)|^2|w|^{-2mc}.
\]
The integral in the fiber coordinate diverges precisely when \(mc\ge1\). By holomorphic descent, therefore,
\[
 \boxed{V_m=H^0(X,\pi^*A^m\otimes\mathcal I(m\varphi))=0
 \quad\text{for every integer }m\ge\lceil 1/c\rceil.} \tag{3}
\]
On the other hand, *every* putative \(\theta\)-psh base reference \(\psi\) of positive non-pluripolar mass \(M\) satisfies \(\dim W_m\ge mM+1\) by (2). Consequently \(W_m\not\subseteq V_m\) for all sufficiently large \(m\), and the requested \(o(m)\) discrepancy cannot hold. This is a **fully explicit obstruction to an unconditional existence assertion**, not a negative answer to the stated open-ended problem of finding suitable extra conditions.

More generally, a logarithmic singularity of positive coefficient in a normal fiber direction along a divisor dominating the base is incompatible with pullback sections for all sufficiently large powers. One must distinguish such *fiberwise nonintegrability* from base-direction singularities that can be encoded by a positive-mass base ideal.

## Audit disposition and dependence boundaries

- **Status:** low / **verified conditional deduction** (indeed the local obstruction and the \(\mathbf P^1\) count are proved here using Riesz/Jensen, radial integrability, Poincaré–Lelong and \(h^0(\mathbf P^1,\mathcal O(d))\)). No printed theorem is proved false. The existing qualification at §24.10.2 line 55 anticipates that universal descent cannot be assumed.
- **Proposed action:** optional note after Problem 24.10.2 explaining the generic-fiber divisorial obstruction and the sharp \(\mathbf P^1\) positive-mass count. Preserve all original source labels, permanent tags and historical attribution. No production patch is made here.
- **Affected interpretation:** §24.10.2 (conditions for base references); §18.37.1 and §§18.39.* are *contextual downstream comparisons only*, not audited or repaired here. §5.37.7 is consistent: its hypotheses concern \(u\circ p\), unlike the fiber-dependent \(\varphi\) of (3). §5.37.8 concerns critical maps, not this submersion obstruction.
- **Actual proof coverage:** first selected nonexcluded inspection of §5.37.1 and §5.37.7–8; first selected statement/quantifier inspection of §24.10.2 with a new self-contained \(\mathbf P^1\) obstruction and the local dimension proof. §24.10.1/.3/.4 and §18.37/§18.39 are context only; no entire numbered section is certified.
- **Project-wide boundary:** 25 chapters, 747 numbered ToC sections, zero fully mathematically certified sections. All existing confirmed errors, proof gaps, candidates, external inputs and historical variants retain their prior status. Demailly approximation/regularization and its dedicated Bergman/\(L^2\)/Ohsawa–Takegoshi/multiscale-atlas/positivity-loss work remain **deferred-by-user**, not resolved or reopened. No project build, CI, formalization, website publication, source/body/tag/registry edit, or automatic PR merge was performed.
