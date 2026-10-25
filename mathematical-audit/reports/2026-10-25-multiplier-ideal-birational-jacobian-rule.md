# 2026-10-25 — birational multiplier-ideal transformation without an external proof and a sharp smooth-center check

**Reviewed `main`:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.
**Review baseline:** `737b1429ac8bb8c3e4b34b4e6c66d906862bc23e`.
**Scope:** first selected proof-level reading in §16.6, with precise crosschecks of §§5.16, 5.17 and 9.10. This does **not** certify these sections or the full theory of multiplier ideals. The regularization/Bergman/L²/Ohsawa–Takegoshi/multiscale/positivity-loss proof-completion programme remains **deferred-by-user**, not resolved.

## POME-MI-BIRATIONAL-JACOBIAN-001 — medium / verified repair of a genuine external dependency

**Exact integrated source.** Proposition 16.6.4, SGPT source label `3CAA346A`, permanent tag `BBF7977859F1`, `docs/sections/the-envelope-operators--multiplier-ideal-envelopes/index.html`, blob `e37e0c4f6273acf41ee2e6d46d99ee5018bf78d5`, physical lines **82–109**. The implication `(2) => (1)` quotes Dem12, Proposition 5.8, for the multiplier-ideal transformation rule. Its downstream Proposition 16.6.10, source label `D63378B8`, permanent tag `E535E4DC5384`, uses the same comparison at lines **180–210**. The other implication `(1) => (2)` uses the divisorial criterion in 16.6.2 and is **not** independently recertified here.

**Hypotheses and exact replacement.** Let \(\pi:Y\to X\) be a proper bimeromorphic holomorphic map between smooth complex manifolds of the same dimension and let \(\phi\) be quasi-psh on \(X\). The Kähler hypothesis of the cited proposition is stronger than needed for this local statement. Write \(J_\pi\) for the holomorphic complex Jacobian in local coordinates, \(R=\operatorname{div}(J_\pi)\) for the relative canonical divisor, and \(K_{Y/X}\simeq\mathcal O_Y(R)\). With the **Pome weight convention** \(\mathcal I(\phi)=\{f:|f|^2e^{-\phi}\text{ is locally integrable}\}\), one has the identity of ideal sheaves
\[
 \boxed{\quad \mathcal I_X(\phi)
   =\pi_*\bigl(\mathcal O_Y(R)\otimes\mathcal I_Y(\phi\circ\pi)\bigr).\quad} \tag{A}
\]
Here \(\mathcal O_Y(R)\otimes\mathcal I_Y\) is viewed as a subsheaf of meromorphic functions on \(Y\), via the natural divisor inclusion. This is a sheaf identity, not a statement that raw pullback ideals coincide.

**Complete local proof.** Work over a relatively compact coordinate ball \(U\Subset X\). Since \(X\) is smooth (hence normal), a proper birational morphism is an isomorphism away from an analytic subset \(A\subset X\) of codimension at least two. Any meromorphic function on \(Y\) with poles confined to \(R\) therefore determines a holomorphic function on \(U\setminus A\), and this extends uniquely across \(A\) by the holomorphic Hartogs/Riemann extension theorem. In particular the natural map \(\pi_*\mathcal O_Y(R)\to\mathcal O_X\) identifies the two sheaves.

In a pair of local coordinate frames of \(K_Y\) and \(\pi^*K_X\), multiplication by the relative Jacobian \(J_\pi\) identifies the canonical effective section of \(K_{Y/X}\) with the divisor \(R\). The local frame \(1/J_\pi\) of \(\mathcal O_Y(R)\) makes a descended meromorphic section \(f\circ\pi\) have coefficient \((f\circ\pi)J_\pi\). Consequently the right side of (A) contains \(f\) precisely when
\[
 (f\circ\pi)J_\pi\in \mathcal I_Y(\phi\circ\pi)
 \quad\text{at every point over the neighborhood of }x.
\]
This coefficient condition is equivalent to local integrability of
\[
 |f\circ\pi|^2\,|J_\pi|^2e^{-\phi\circ\pi}\,dV_Y. \tag{B}
\]
The ordinary holomorphic change-of-variables identity (multiplicity one off the exceptional image) says, on every relatively compact \(U'\Subset U\),
\[
 \int_{\pi^{-1}(U')} |f\circ\pi|^2e^{-\phi\circ\pi}|J_\pi|^2\,dV_Y
   =\int_{U'} |f|^2e^{-\phi}\,dV_X. \tag{C}
\]
Different smooth coordinate volume densities introduce only locally bounded positive factors. The exceptional and its image have Lebesgue measure zero, so they do not affect (C). Properness makes the preimage of \(\overline{U'}\) compact; finitely many charts show that finiteness of (B) locally everywhere above \(U'\) is equivalent to finiteness of the integral in (C). Thus \(f\in\mathcal I_X(\phi)\) if and only if the descended section lies in the right side of (A). This proves the identity on stalks, hence on sheaves.

If \(\pi^*\phi\sim_{\mathcal I}\pi^*\psi\), applying (A) to each \(k\phi,k\psi\), for every integer \(k>0\), gives \(\mathcal I_X(k\phi)=\mathcal I_X(k\psi)\). This establishes exactly Proposition 16.6.4's quoted `(2) => (1)` step without Dem12. It also supplies the relevant half of the birational comparison used by Proposition 16.6.10; the **separate** positive-current descent theorem 5.17.8 remains a required internal input.

**Independent internal crosscheck.** The source's own finite-test proof expansion at Theorem 5.16.18, permanent tag `B2A67FDA22D2`, `docs/sections/plurisubharmonic-functions--lelong-numbers-and-multiplier-ideal-sheaves/index.html`, blob `2315574feb57cd6bf57c3d64e4221da2eabc3cc9`, lines **200–229**, already derives the identical Jacobian exponent by change of variables on a log resolution. The present sheaf-theoretic argument adds the missing *direct birational pushforward* bridge; it is not a duplicate proof of the valuative theorem. The descent used in Proposition 16.6.10 is internally supplied at Proposition 5.17.8, source label `0E9ABD1F`, permanent tag `AF2A3F35959C`, `docs/sections/plurisubharmonic-functions--quasi-plurisubharmonic-functions/index.html`, blob `8891129803a9c17d6a779d0944614e111b414a52`, lines **97–106**.

**Suggested separately reviewable source patch (NOT applied).** Replace the external proof input after Proposition 16.6.4 by a concise in-text local proof using (A)–(C); keep Dem12 as historical attribution/reference, preserve source and permanent tags. A shorter internal link to the §5.16.18 change-of-variables proof may accompany it, but must state the relative Jacobian divisor explicitly. No claim is made about the rest of the deep divisorial criterion, nor the existence theory for envelopes.

## POME-MI-SMOOTH-CENTER-FLOOR-001 — low / verified conditional deduction

**Exact local model and sign check.** Let \(Z=\{z_1=\cdots=z_r=0\}\subset\mathbb C^{r+s}\), \(r\ge2\), with smooth transverse coordinates and \(c\ge0\). For the psh weight
\[
 \phi=c\log\bigl(|z_1|^2+\cdots+|z_r|^2\bigr)
\]
and the ideal \(\mathfrak m_Z=(z_1,\ldots,z_r)\), one has the exact formula
\[
 \boxed{\ \mathcal I(\phi)=
 \mathfrak m_Z^{\max\{0,\lfloor c\rfloor-r+1\}}\ }. \tag{D}
\]
To verify it directly, expand a holomorphic \(f\) by transverse homogeneous order \(m\); its leading polynomial is nonzero on a set of positive spherical measure. In the transverse radial variable the defining integral has the integrability threshold
\(\int_0^\delta t^{\,2m-2c+2r-1}\,dt<\infty \iff m+r>c\).
For integral \(m\), this is exactly \(m\ge\max(0,\lfloor c\rfloor-r+1)\). The same test in transverse slices, or the smooth blowup below, gives the stated ideal sheaf. This includes integer threshold values, where the strict inequality matters.

For the blowup \(\pi:\operatorname{Bl}_Z\mathbb C^{r+s}\to\mathbb C^{r+s}\), a chart \(z_1=u,\ z_j=uv_j\ (2\le j\le r)\) has \(J_\pi=u^{r-1}\) and \(\phi\circ\pi=c\log|u|^2+O(1)\). Hence
\[
 R=(r-1)E,\quad
 \mathcal I_Y(\phi\circ\pi)=\mathcal O_Y(-\lfloor c\rfloor E),\quad
 \pi_*\mathcal O_Y((r-1-\lfloor c\rfloor)E)
   =\mathfrak m_Z^{\max(0,\lfloor c\rfloor-r+1)}.
\]
This independently tests (A) and its \((r-1)\)-discrepancy. In codimension two with \(c=2\), the **correct** ideal is \(\mathfrak m_Z\); the incorrect raw pushforward omitting \(\mathcal O(E)\) gives \(\mathfrak m_Z^2\). This is a counterexample to a *naive unweighted projection rule*, not to any printed Pome statement.

**Basis and proposed action.** Same Proposition 16.6.4 lines 82–109, the local integrability convention at Theorem 5.16.18, and the normal-space/modification context of Corollary 9.10.10, source label `BDB64C24`, permanent tag `178E0605C99D`, `docs/sections/pluripotential-theory-on-unibranch-spaces/index.html`, blob `6edfa6b19fa7cdbaf0c2665389fa7b3ca338cdf4`, lines **94–107**. Add (D), if desired, as a local calibration example, without changing canonical entries. Dependents: multiplier-ideal restriction/pullback, the envelope invariance chain §§16.6.4/10 and later ideal-model comparisons. No false printed theorem established.

## Actual breadth, risk and deferred ledger

- **Direct selected integrated proof reading:** §16.6.2–5, 16.6.9–11, 16.6.17–18, 16.6.27–30. The finiteness-of-support arguments for arbitrary directed nets in 16.6.29–30 were checked only for their stated use of \(\epsilon_i\to0\), uniformly \(L^1\)-bounded normalized potentials and already named mass/extrapolation inputs. None is certified transitively.
- **Supporting exact local source checks:** §5.16.18/21; §5.17.8; §9.10.10. These checks do not convert those three entire sections to reviewed status; the higher-level ideal/valuation criterion and psh descent retain their listed internal premises.
- **Expressly not audited:** §16.6.22's Bergman-type quasi-equisingular approximation and its normalization/multiscale/positivity-loss underpinnings; all such historical audit matters remain **deferred-by-user**, not solved. Its other displayed conclusion was read only to record the dependency.
- **No section, chapter, entire Pome collection, build, CI, formal proof or publication is certified.** Only audit notes should be committed to `review/mathematical-audit`; mathematical source, permanent tags, main and the published site must not change.
