# Sharp logarithmic sublevel capacity and quantitative Bedford–Taylor mass decay

**Audit:** 2026-10-25 UTC; **reviewed main:** b6933b772f41b45918f7e25ed1afbbb1fd892272; **starting audit branch head:** c241cc29a997b256a55271b032483c60a268e258. Selected proof inspection only; no complete section or dependent theory certified.

## Exact integrated source anchors

- **§5.27:** docs/sections/plurisubharmonic-functions-and-singularities--local-products-and-capacity/index.html, main blob **ddb2ac8d9de27a22152872e07e5e787d138a790e**; section permanent tag **5E507B6993DC**. BT Theorem 5.27.1 tag **8B1218AE4FDC** lines 10–16; weighted-limit Lemma 5.27.2 tag **2A60C2B3B4C3** lines 21–61; cutoff/range **Eq. 5.27.3**, source **non-kahler-pluripotential-theory:0B0E74EF**, permanent **F138661713A9**, lines **104–117**; mass-decay Lemma 5.27.27 source **non-kahler-pluripotential-theory:B41297A6**, permanent **55862640C106**, lines **547–561**; unbounded mass-concentration Proposition 5.27.30 tag **026A64B7A5A2**, lines 605–662.
- **§5.28:** docs/sections/plurisubharmonic-functions-and-singularities--products-with-smooth-backgrounds/index.html, main blob **e2ba89b51376ba0296846221109c664a0c29b2c3**, section tag **5E2B332B89B4**. Decomposition independence/positivity Proposition 5.28.2 tag **3EDAB69A7289** lines 20–42; contact Lemma 5.28.3 **5087175B2C39** lines 53–69; submersion Lemma 5.28.4 **636D22C6199B** lines 76–88; determinant lower bound Proposition 5.28.6 **2A843EB4B4AE** lines 114–126; mixed-density freezing Lemma 5.28.7 **6C81352D9EE7** lines 133–180.
- **§5.29:** docs/sections/plurisubharmonic-functions-and-singularities--hermitian-capacity/index.html, main blob **77a9098e9bb922425d11c5b04d8927a3997ad44e**, section tag **DD310AD8B258**. Local-to-global capacity Lemma 5.29.2, source **non-kahler-pluripotential-theory:96A183CE**, permanent **5CEF121C5391**, lines **35–78**; sublevel **Eq. 5.29.4**, source **non-kahler-pluripotential-theory:B2A1C46F**, permanent **3EF8F920CDD3**, lines **41–44**; gluing lines **50–69**; capacity domination Lemma 5.29.16 **F56E1BEB2997** lines 315–333; finite non-pluripolar measure Lemma 5.29.18 **D0C7DB81F772** lines 371–389; curve Theorem 5.29.23 **FD7A4AE0DAC6** lines 468–491.
- **§16.13 incremental recheck (earlier selected coverage exists):** docs/sections/envelopes-and-model-potentials--measures-on-contact-sets--concentration-on-the-contact-set/index.html, main blob **840ebcb98be09245369315fa0c0288b936040098**, section tag **954F538078ED**. Contact Lemma 16.13.1 permanent **15A418789279** lines 10–27; minimal-potential Lemma 16.13.2 **691B1A212F1A** lines 31–39; l.s.c. obstacle Lemma 16.13.3 **175BA4BB6A7C** lines 43–65; quasi-continuous contact Theorem 16.13.4 **38E18A798D6B** lines 69–145.

## POME-HERM-CAP-LOGPOLE-SHARP-001 — low / verified conditional deduction

**Status:** Printed Lemma 5.29.2 and sublevel Eq. 5.29.4 are **correct**; this is a new sharpness example. **Proposed action:** optional explanatory corollary; do not strengthen the exponent in downstream capacity iteration or contact-envelope exceptional-set estimates.

Fix \(0<a<1\), \(X=\mathbb P^1\), \(\omega=dd^c\log(1+|z|^2)\) with mass one, and
\[
u_a(z)=a\log\frac{|z|^2}{1+|z|^2},\qquad u_a(\infty)=0.
\]
Poincaré–Lelong gives \(dd^c\log|z|^2=[0]\), so \(\sup_Xu_a=0\) and \(\omega+dd^cu_a=(1-a)\omega+a[0]\ge0\). For \(E_t=\{u_a<-t\}\), algebra yields
\[
E_t=\{|z|<r_t\},\qquad r_t=(e^{t/a}-1)^{-1/2}.
\]
For large \(t\), let \(B=\{|z|<1\}\), \(B'=\{|z|<3/4\}\), and \(s_t=r_t/2\); then \(E_t\Subset B'\) and \(0<s_t<1\). On \(B\), the explicit bounded subharmonic test
\[
v_{s_t}(z)=\max\left\{0,1+\frac{\log|z|}{\log(1/s_t)}\right\}
\]
lies in \([0,1]\), and its Laplacian is supported on the circle \(|z|=s_t\). Under \(dd^c=(i/2\pi)\partial\bar\partial=(4\pi)^{-1}\Delta\,dx\,dy\), the jump of \(r\partial_r v_{s_t}\) is \(1/\log(1/s_t)\), so
\[
dd^c v_{s_t}=\frac{\sigma_{s_t}}{2\log(1/s_t)}
\]
for probability circular measure \(\sigma_{s_t}\). This circle lies **strictly inside** \(E_t\); therefore
\[
\operatorname{cap}(E_t\cap B',B)\ge\frac1{2\log(1/s_t)}.
\]
Lemma 5.29.2, lines 50–66, explicitly glues **each** local test to a global \(\omega\)-psh function whose curvature on \(B'\) dominates \(\delta dd^c v\), where a single \(\delta>0\) depends only on the fixed balls and background. Consequently
\[
\operatorname{Cap}_\omega(E_t)\ge
\frac{\delta}{2\log(2/r_t)}
=\frac{\delta}{2\log2+\log(e^{t/a}-1)}.
\]
The last lower bound is asymptotic to \(\delta a/t\). Eq. 5.29.4 provides \(\operatorname{Cap}_\omega(E_t)\le C/t\). Hence this one fixed normalized logarithmic potential satisfies \(c_a/t\le\operatorname{Cap}_\omega(E_t)\le C_a/t\) at all sufficiently large \(t\). No \(O(t^{-1-\eta})\) replacement with \(\eta>0\) is valid in general. **The exact leading capacity coefficient is not asserted.** \(\square\)

## POME-BT-HARMONIC-L1-QUANT-001 — low / verified conditional deduction

**Status:** Quantitative strengthening of correct Lemma 5.27.27; not a false theorem. **Proposed action:** optional sharpened local lemma. **Affected dependents:** mixed BT mass and concentration arguments must retain common boundedness; this result does not contradict the unbounded §5.27.30 construction.

Let \(B'\Subset B\Subset B_1\Subset\Omega\subset\mathbb C^n\) be fixed concentric balls, \(\kappa=dd^c|z|^2\), and \(h\) real pluriharmonic near \(B_1\). Suppose \(p\) is psh there and \(|p-h|\le M\) on \(B\), \(M>0\). For every \(1\le k\le n\),
\[
\boxed{\int_{B'}(dd^cp)^k\wedge\kappa^{n-k}
\le C_{B',B,B_1,k} M^{k-1}\|p-h\|_{L^1(B_1)}.}
\]
**Proof:** Put \(q=p-h\). Because \(dd^ch=0\), \(q\) is psh. With nonnegative \(\chi\in C_c^\infty(B_1)\) equal to one near \(\overline B\), positivity and Stokes give
\[
0\le\int_Bdd^cq\wedge\kappa^{n-1}
\le\int_{B_1}\chi dd^cq\wedge\kappa^{n-1}
=\int_{B_1}q\,dd^c\chi\wedge\kappa^{n-1}
\le C\|q\|_{L^1(B_1)}.
\]
On \(B\), \(q+M\) is psh and lies in \([0,2M]\), with \(dd^c(q+M)=dd^cp\). Apply the **first** range estimate of Eq. 5.27.3 (lines 104–117) to \(q+M\) and nested balls \(B'\Subset B\); its left side is at most \(C(2M)^{k-1}\) times the trace integral just estimated. This proves the bound with a constant independent of \(p,h,M\). For an **arbitrary directed net** \(p_i\to h\) in \(L^1(B_1)\) obeying one common \(M\), the same pointwise inequality immediately gives mass tending to zero; no subsequence or swapping of limits is used. The exponent \(k-1\) is homogeneously optimal: on fixed balls take \(p_t=t|z|^2\), \(h=0\), \(M_t=t\sup_B|z|^2\). The left side scales as \(t^k\), but \(\|p_t\|_{L^1(B_1)}\) and \(M_t\) scale as \(t\). Any power other than \(k-1\), with a constant uniform for all amplitudes \(t>0\), fails at \(t\to0\) or \(t\to\infty\). \(\square\)

## Actual proof review and residual obligations

In §5.27 selected the auxiliary-variable weighted BT convergence (§5.27.2), nested-cutoff mass estimate (§5.27.3), common-local-bound mass stability (§5.27.27), and contrast with smooth concentration (§5.27.30). The measure-cluster realization elsewhere in §5.27 is **not audited**. In §5.28 selected nonclosed-background freezing/positivity, contact max, submersion pullback, \(C^{1,1}\) eigenvalue determinant algebra and mixed-density estimates (§§5.28.2–4, 6–7). In §5.29 selected local-to-global test gluing, bounded mixed capacity domination, non-pluripolar uniform capacity absolute continuity and zero-area curve stability (§§5.29.2, 16, 18, 23); other Hölder and trace estimates not verified. The earlier selected §16.13 inspection was **incrementally revisited** for max/locality (§16.13.1), local obstacle balayage (§16.13.3), and capacity-exception / weighted truncation (§16.13.4); no new full claim or duplicate finding. Internal §7.5 weighted BT capacity and §10.3.10 local balayage, §10.4.6 big-class input remain **conditional, not transitively certified**.

No confirmed incorrect printed theorem or new genuine duplicate in this sample. **Demailly approximation/regularization and its dedicated Bergman, L², Ohsawa–Takegoshi, multiscale-atlas and positivity-loss programme are deferred-by-user, neither resolved nor certified, and not reopened.** No tests, builds, CI, formal verification, publication, source/canonicalization/registry/tag/main edits, new PR or merge.
