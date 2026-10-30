# 2026-10-30: sharp entropic modulus for the ideal-envelope metric on a projective-line pole family

**Reviewed production main:** <code>b6933b772f41b45918f7e25ed1afbbb1fd892272</code>. **Audit scope:** new selected proof reading of §§18.7.1–3, with independent model-level verification of §18.6.1 and §18.4.8, and reuse (not republication) of the previously audited §16.21 projective-line free-boundary envelope. Nothing in §§18.7.4–9, the Demailly approximation/regularization or the dedicated Bergman, \(L^2\), Ohsawa–Takegoshi, multiscale-atlas and positivity-loss programme is being audited here. **No whole section or dependency chain is certified.**

## Anchors in the actual integrated reading edition

- Proposition **18.7.1**, source <code>non-kahler-pluripotential-theory:305955D4</code>, permanent tag **B727D2CB45A6**: <code>docs/sections/multiplier-ideal-envelopes-and-goodness--limits-of-analytic-envelopes/index.html</code>, main blob **764fb239e47ddf264f688649849e6b737b23dab7**, physical lines **13–22** (hypotheses/conclusion), **27–44** (cluster-value argument). Corollary **18.7.2**, source <code>non-kahler-pluripotential-theory:D36545F2</code>, permanent tag **5AE1D9158EE3**, same blob lines **52–69** (ideal inclusions and divisorial bounds). Example **18.7.3**, source <code>non-kahler-pluripotential-theory:3E654694</code>, permanent tag **504A5958272F**, same blob lines **78–97**: different, nonordered curve approximation; it is not re-registered.
- Proposition **18.6.1**, source <code>non-kahler-pluripotential-theory:C2DA1190</code>, permanent tag **47A414940A74**, with metric equation source **63AB3400**, permanent tag **CE9BB18A9158**: <code>docs/sections/multiplier-ideal-envelopes-and-goodness--geometry-of-ideal-classes/index.html</code>, main blob **64b1c0de9266a28727de07ca3502a13ab974f001**, physical lines **19–35**. Definition **18.4.1** and Proposition **18.4.8**, permanent tags **F1F202AEE8FD** and **EB95710FF4D7**, <code>docs/sections/multiplier-ideal-envelopes-and-goodness--ideal-projection/index.html</code>, main blob **f1979b73c857f4874dd4a5cb10b93bcc047ebbdc**, lines **11–18**, **130–147**.
- Definition **16.21.1**, permanent tag **99168E437529**, and Proposition **16.21.2**, permanent tag **037CA226D141**: <code>docs/sections/envelopes-and-model-potentials--singularity-envelopes/index.html</code>, main blob **8d55c95795ea2a0a3cf5cb81bd4abb4ba867a16a**, physical lines **10–38**. Its exact projective-line free-boundary calculation was already logged as **POME-MODEL-P1-FREEBOUNDARY-EXACT-001** in <code>mathematical-audit/reports/2026-10-24-projective-line-singularity-envelope-contact-free-boundary.md</code>. **That formula is reused and not a new finding here.**

## POME-IDEAL-P1-SHARP-ENTROPY-MODULUS-001

**Status / severity:** **low / verified conditional deduction**. This is a sharp quantitative model consequence of the printed ideal-model metric and qualitative stability proposition, **not** a false source theorem, general quantitative stability theorem, or a completed general proof repair. The only standard curve inputs are the one-dimensional correspondence between curvature atoms and Lelong numbers, the multiplier-ideal/valuative criterion (printed Theorem 5.37.3, tag **3F1FC2F620B4**), and elementary subharmonic comparison.

### Exact hypotheses

Let \(X=\mathbb P^1\) with affine coordinate \(z\), and use the precise Pome convention
\[
dd^c=\frac{i}{2\pi}\partial\bar\partial,\qquad
\omega=dd^c\log(1+|z|^2),\qquad \int_X\omega=1.
\]
For \(0\leq c\leq1\) put
\[
u_c(z)=c\log\frac{|z|^2}{1+|z|^2},\qquad u_0=0.
\]
Then \(\omega+dd^c u_c=(1-c)\omega+c\delta_0\geq0\), and \(u_c\) is normalized by \(\sup_Xu_c=0\). For any real \(s>0\), direct polar integrability near \(0\) gives
\[
\mathcal I(su_c)_0=(z)^{\lfloor sc\rfloor},
\]
with trivial multiplier ideals away from \(0\). The floor follows from \(|z|^{2k-2sc}\in L^1_{\rm loc}(\mathbb C)\) if and only if \(k-sc>-1\). Consequently the ideal class detects \(c\) and \(c\mapsto[u_c]_{\mathcal I}\) is injective.

### The envelope, with direct comparison (recall, not a new discovery)

For \(0<c<1\) set
\[
r_c^2=\frac{c}{1-c},\qquad H(c)=-c\log c-(1-c)\log(1-c).
\]
The already audited common ordinary/ideal envelope is
\[
p_c=P_\omega[u_c]_{\mathcal I}=P_\omega[u_c]
=\begin{cases}
c\log|z|^2+H(c)-\log(1+|z|^2),& |z|^2\leq r_c^2,\\
0,& |z|^2\geq r_c^2.
\end{cases}
\]
Endpoint values are \(p_0=0\), \(p_1=u_1\). Here is an independent check adequate for this report. The two pieces have matching values and first radial derivatives, so
\[
\omega+dd^c p_c=c\delta_0+\mathbf1_{\{|z|>r_c\}}\omega
\]
with no artificial boundary-circle atom. In particular \(p_c\) is an admissible nonpositive potential in the same ideal class as \(u_c\) (their difference is bounded). If \(v\leq0\) is another \(\omega\)-psh potential in that ideal class, its curvature has atom exactly \(c\) at \(0\). On the disc \(|z|<r_c\), the distribution
\[
G=v+\log(1+|z|^2)-c\log|z|^2-H(c)
\]
has \(dd^cG=(\omega+dd^cv)-c\delta_0\geq0\), hence has a subharmonic representative including at \(0\). The boundary comparison gives \(\limsup G\leq0\), since \(\log(1+r_c^2)=c\log r_c^2+H(c)\) and \(v\leq0\). By the subharmonic maximum principle \(G\leq0\); outside the disc \(v\leq0=p_c\). Thus every ideal competitor is dominated by \(p_c\). The same argument applies to the ordinary competitor class. This proof does not invoke any regularization, Bergman construction or limiting curvature estimate.

### Exact ideal metric and sharp global modulus on this family

Let \(t=|z|^2/(1+|z|^2)\in[0,1]\). The normalized Fubini–Study measure pushes forward to **Lebesgue measure \(dt\)**. For \(0<t<c\),
\[
p_c(t)=H(c)+c\log t+(1-c)\log(1-t)
=-D_{\rm KL}({\rm Bern}(c)\Vert{\rm Bern}(t)),
\]
while \(p_c(t)=0\) for \(t\geq c\). The endpoint formulas are understood by continuous limits. In particular \(p_d\leq p_c\) whenever \(c\leq d\), since the envelope competitors for pole coefficient \(d\) form a smaller family.

Write
\[
F(c)=\int_X(-p_c)\,\omega
=\int_0^c\left[c\log\frac c t+(1-c)\log\frac{1-c}{1-t}\right]dt.
\]
Differentiating under this proper integral for \(0<c<1\) (the moving-boundary integrand is zero at \(t=c\)), and using
\(\int_0^c\log(t/(1-t))dt=c\log c+(1-c)\log(1-c)\), gives
\[
F'(c)=\int_0^c\log\frac{c(1-t)}{(1-c)t}\,dt=-\log(1-c).
\]
The boundary value \(F(0)=0\) therefore yields the closed formula
\[
\boxed{F(c)=c+(1-c)\log(1-c),\quad 0\leq c\leq1,}
\]
with \(0\log0=0\) and \(F(1)=1\). By Proposition 18.6.1, choosing the probability volume form \(dV=\omega\), the **exact ideal-envelope metric** on this family is
\[
\boxed{d_{\mathcal I,\omega,\omega}([u_c],[u_d])
=|F(d)-F(c)|.}
\]

More sharply, for \(0<\delta\leq1\), \(|c-d|=\delta\), the derivative \(-\log(1-t)\) is increasing, so the largest increment of \(F\) on an interval of length \(\delta\) is attained at the right endpoint \(1\). Thus the **optimal uniform modulus for this entire ordered one-pole family** is
\[
\boxed{\ \sup_{|c-d|=\delta}d_{\mathcal I,\omega,\omega}([u_c],[u_d])
=F(1)-F(1-\delta)=\delta(1-\log\delta).\ }
\]
There is **no** constant \(C\) such that the ideal metric of this family is bounded by \(C|c-d|\) for all coefficients: the quotient by \(\delta\) blows up as \(\delta\downarrow0\) at the full-pole endpoint. At the opposite, nonsingular endpoint,
\[
F(\delta)=\frac{\delta^2}{2}+O(\delta^3),
\]
so the ideal distance is *quadratic* in the pole coefficient to first order there. The non-Lipschitz claim is **only** about a proposed valuation-error-to-ideal-metric estimate; Proposition 18.6.1 itself never asserted such a Lipschitz bound.

### Direct stress test of the qualitative stability proposition

For \(u=u_1\), choose any rational sequence \(c_j\uparrow1\) with \(c_j<1\), e.g. \(c_j=1-j^{-1}\), \(j\geq2\), and put \(a_j=u_{c_j}\), \(\epsilon_j=0\). Then \(u_1\preceq_{\mathcal I}a_j\), and **all** local-divisor Lelong numbers converge (the only nonzero one is \(c_j\) at \(0\)). The ordinary and ideal envelopes coincide at every stage. The computed distance is exactly
\[
\left\|P_\omega[a_j]_{\mathcal I}-P_\omega[u_1]_{\mathcal I}\right\|_{L^1(\omega)}
=\frac{1+\log j}{j}\longrightarrow0,
\]
not \(O(1/j)\). This confirms, rather than contradicts, the **qualitative** conclusion of Proposition 18.7.1 under its printed ideal-order and divisorial hypotheses. No rate is implied in that proposition. Example 18.7.3 uses an entirely different failure when the order hypothesis is dropped; it is neither duplicated nor invalidated.

### Classification and proposed action

**Proposed correction:** none. An optional **new corollary/example** after Proposition 18.6.1, cross-referenced at Proposition 18.7.1, could state the exact ideal metric and endpoint-optimal \(\delta(1-\log\delta)\) modulus for this one-pole family; do not claim a bound for general \(X\), general weights or all ideal classes. **Affected dependents:** metric geometry in §18.6, stability discussion in §18.7.1 and the earlier explicit singularity envelope §16.21.1. No source statement, proof registry, canonicalization, historical attribution or permanent tag should be modified by the audit.

**Precisely reviewed:** entire selected statement and compactness/divisorial-cluster argument of Proposition 18.7.1 (physical lines 13–44), the fixed-weight ideal-inclusion calculation in Corollary 18.7.2 (lines 52–69), Example 18.7.3 (lines 78–97) for nonduplication, metric formula/proof of Proposition 18.6.1 (lines 19–35), and comparison with the already audited model §16.21. **Unreviewed:** all transitive L1-pullback and valuative theorems, all other §§18.7.4–9 proof programmes, and every excluded regularization-related input. Hence no entire section or theorem chain certified.

**Reproducible scalar sanity check:** <code>mathematical-audit/checks/check_ideal_envelope_entropy.py</code> independently approximates \(\int(-p_c)\omega\) by midpoint quadrature for five coefficients and verifies the exact endpoint modulus for four gaps, using only the Python standard library. This numerical check was run locally and passed; the written derivative/maximum-principle argument, not the check, is the mathematical justification. No project build, CI, website publishing, formalization or whole-repository test was performed.
