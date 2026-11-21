# 2026-11-22: toric Newton bodies under suprema and exact curve-section rounding

## Revision, scope, and classification

- Reviewed **main**: b6933b772f41b45918f7e25ed1afbbb1fd892272. Review branch at the start of the session: dc874cc2b3779155168f1152bf7db07d3f9d9f52.
- **Whole current reading-edition direct review:** docs/sections/convex-analysis-and-toric-potentials--legendre-duality-and-convex-envelopes/index.html, physical mathematical lines 11–139, blob 347fa1f0fc35c13b1d1c45193ab997ed456966e4, including Theorem 21.3.2 (permanent 011FA81B0000) and Proposition 21.3.3 (53A9D470F1AC). Full transitive dependence on §21.2 was **not** certified; prior historical visits are unreconciled.
- **Whole current direct rereview, NOT first coverage:** docs/sections/analytic-cycles-and-cartier-cycles/index.html, lines 7–74, blob d4817ac64b1365bd967d42cd474fec169f992e28; Definitions/Propositions 20.6.2–4 (BE0C86A8DD65, FD8966432506, AA96C35C8290) and quadric example 20.6.5 (0C462992AB3A). The previously reported non-Cartier obstruction is **not** a new finding.
- **Selected only:** docs/sections/toric-pluripotential-theory-on-ample-line-bundles/index.html, blob 56a1a55dfc8185aee0e6d495a6a93d8a2313d76b: Theorem 21.12.13 at lines 239–279, Proposition 21.12.23 and Example 21.12.22 at lines 391–462, mass Proposition 21.12.24 at lines 466–480, and Newton-body Definition 21.12.27 at lines 535–545. The remaining 21.12 claims were **not** audited.
- **Selected nonexcluded curve counting ONLY:** docs/sections/holomorphic-sections-and-hermitian-mass/index.html, blob 5f00431e7986d899dc833c89175686b75f09371d, §19.8.10–11, lines 255–288, source tag CB9DFB6A and permanent 1E6D5AA611CC. No review or extension of the dedicated Bergman/regularization programme, including §19.8.1–3.
- Two verified **conditional deductions**, both low severity. No new confirmed printed error; no complete transitive proof-chain certification. No tests, builds, CI, source, main, registry, tags, or site changes.

## POME-TORIC-NEWTON-SUP-CONVEX-HULL-001 — Newton body of an arbitrary toric upper envelope

**Status:** verified conditional deduction; **severity:** low; not a counterexample to the printed statements.

Assume the smooth compact ample toric setting of §21.12: the moment polytope P is compact and full dimensional, and \(\{\varphi_i:i\in I\}\) is a nonempty family of torus-invariant \(\omega\)-psh potentials satisfying a **uniform upper bound**. Define
\[
 \Phi=(\sup_i\varphi_i)^*,\qquad
 \Delta_i=\overline{\operatorname{dom}G_{\varphi_i}}\subseteq P,\qquad
 C=\overline{\operatorname{conv}}\bigcup_i\Delta_i.
\]
Here the star on the supremum denotes upper-semicontinuous regularization, not Legendre duality. Then
\[
 \boxed{\Delta(\omega,\Phi)=C},\qquad
 \boxed{\int_X\operatorname{MA}_{\omega}(\Phi)=n!\operatorname{vol}(C)}.
\]
This includes arbitrarily indexed families; no sequential compactness or interchange of limits is used.

**Proof.** Put \(F_i=F_{\varphi_i}\), \(G_i=F_i^*\) and \(F=F_\Phi=\sup_iF_i\), by Proposition 21.12.23. The functions \(F_i\) are finite closed convex functions; their conjugate domains have closures \(\Delta_i\). By Fenchel–Moreau (Theorem 21.3.2), for any \(x\in N_{\mathbb R}\),
\[
 F_i(x)=\sup_{p\in\operatorname{dom}G_i}
   \big(\langle p,x\rangle-G_i(p)\big)
 \leq F_i(0)+h_{\Delta_i}(x).
\]
The uniform upper bound on \(\varphi_i\) implies \(M:=\sup_iF_i(0)<\infty\). Since \(h_{\Delta_i}\leq h_C\),
\(F(x)\leq M+h_C(x)\).
Taking conjugates reverses order, so
\[
 G_\Phi=F^*\geq(M+h_C)^*=\chi_C-M.
\]
Hence \(\operatorname{dom}G_\Phi\subseteq C\). Conversely \(F\geq F_i\) implies \(G_\Phi\leq G_i\), so \(\operatorname{dom}G_\Phi\) contains every \(\operatorname{dom}G_i\). Its closed convex hull therefore contains C, and the previous inclusion proves equality. The volume identity follows from Proposition 21.12.24, conditional on its established real/complex Monge–Ampère normalization.

**Strict mass gain under maximum.** With \(X=\mathbb P^1\), \(P=[0,1]\), take the exact two toric potentials of Example 21.12.22:
\[
 \varphi(z)=\log\frac{|z|^2}{1+|z|^2},\qquad
 \psi(z)=\log\frac1{1+|z|^2}.
\]
They have \(\Delta_\varphi=\{1\}\), \(\Delta_\psi=\{0\}\), so each non-pluripolar Monge–Ampère mass is zero. Nevertheless
\[
 \max(\varphi,\psi)=\log\frac{\max(1,|z|^2)}{1+|z|^2}
\]
is globally bounded, has Newton body \([0,1]\), and has full mass \(1\). This is **not** a false printed theorem: Example 21.12.22 instead studies their rooftop infimum.

**Suggested optional addition:** an audit-only corollary following Proposition 21.12.23 stating the convex-hull formula, and its mass consequence conditional on Proposition 21.12.24. **Affected users:** toric maxima/envelopes, Newton bodies and full-mass tests (notably §21.12.38). No canonicalization or permanent tag is to be changed.

## POME-CURVE-SECTION-ROUNDING-GAP-001 — all-degree section-gap bound and eventual exact periodic rounding

**Status:** verified conditional deduction; **severity:** low; not a false printed result.

Use exactly the hypotheses and conventions of §19.8.10–11: a compact Riemann surface of genus \(g\), a line bundle of degree \(\ell\), logarithmic coefficients \(c_j>0\) at distinct points \(p_j\), total \(d=\sum_jc_j\leq\ell\), and weighted-integrable/bounded section spaces \(\mathcal H_m(u)\) and \(\mathcal W_m(u)\). Put
\(R_m=\#\{j:mc_j\notin\mathbb Z\}\).

For **every** positive integer \(m\),
\[
 \boxed{0\leq h^0(\mathcal H_m(u))-h^0(\mathcal W_m(u))\leq R_m\leq r}.
\]
If \(\ell>d\), then for all sufficiently large \(m\),
\[
 \boxed{h^0(\mathcal H_m(u))-h^0(\mathcal W_m(u))=R_m},
\]
and separately
\[
 \begin{aligned}
 h^0(\mathcal H_m(u))
 &=m(\ell-d)+\sum_j\{mc_j\}+1-g,\\
 h^0(\mathcal W_m(u))
 &=m(\ell-d)-\sum_j(\lceil mc_j\rceil-mc_j)+1-g.
 \end{aligned}
\]
When every \(c_j\) is rational, both eventual dimension functions are degree-one quasipolynomials (period dividing the least common multiple of denominators).

**Proof.** Theorem 19.8.11 identifies the spaces with sections of \(L^m(-D_m^H)\) and \(L^m(-D_m^W)\), where \(D_m^H=\sum_j\lfloor mc_j\rfloor p_j\) and \(D_m^W=\sum_j\lceil mc_j\rceil p_j\). The difference divisor is \(\sum_{j:mc_j\notin\mathbb Z}p_j\). The inclusion of invertible sheaves gives a short exact sequence
\[
 0\to L^m(-D_m^W)\to L^m(-D_m^H)
 \to\bigoplus_{j:mc_j\notin\mathbb Z}Q_{j,m}\to0,
\]
where each \(Q_{j,m}\) is a one-dimensional skyscraper sheaf. Global sections immediately give the all-degree upper bound. If \(\ell>d\), then
\(\deg L^m(-D_m^W)=m(\ell-d)+O(1)>2g-2\) for large \(m\).
By Serre duality, its first cohomology vanishes; hence the global restriction map onto the skyscraper sum is surjective, giving exact gap \(R_m\). Riemann–Roch (or the same vanishing applied to both bundles) supplies the displayed exact dimensions. The rational-period claim follows from periodic fractional parts.

This is sharper than the equal **leading** slopes in Theorem 19.8.11; it does **not** alter its assumptions or solve any Bergman approximation question. **Suggested optional addition:** a corollary after Theorem 19.8.11, preserving the original theorem and historical attribution. **Affected users:** exact curve section counts and vanishing-order comparisons. The Riemann–Roch/Serre input is used as already stated in the integrated proof, not newly certified here.

## Cross-check and open ledger

- §21.3: conjugate properness, epigraph separation (including the vertical separation case), the directed-decreasing convex-family argument, convex envelope and infimal convolution identities, and finite-convex sum conjugation were checked directly. No new failure identified.
- §20.6: local finiteness, sheaf gluing and stalks, Weil/Cartier distinction, and the quadric rank-one parametrization and equivariance obstruction were rechecked; **the old non-Cartier finding is not counted again**. Its named analytic component and local factoriality prerequisites were not certified transitively.
- §21.12: only the listed selected statements and proof anchors were checked, **not** the complete 1,045-line section.
- §19.8: only the curve-logarithmic divisor/Riemann–Roch subsection was read; no Bergman kernel or regularization programme was revisited.
- Dedicated Demailly approximation/regularization, Bergman/L²/Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof-completion activities remain **deferred-by-user**, neither resolved nor certified.
- No build, software tests, CI, browser verification, publication or code/registry edits were performed. The audit remains mathematically conditional on the explicitly cited upstream facts.
