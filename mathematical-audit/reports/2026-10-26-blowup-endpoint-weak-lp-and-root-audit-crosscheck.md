# 2026-10-26 — A sharp weak endpoint for blowup pushforward densities and selected independent crosschecks

**Actual checkpoint (UTC):** 2026-10-25T17:04:42.882Z. **Reviewed main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. **Starting audit head:** `6fc009d70378c952fb5567bbf9420994453deeab`. **Scope:** selected proof passages in §§15.23.2, 15.23.5, 15.23.10, 15.24.1, 15.24.4 and additional limited checks of §15.32. None of the complete sections or the upstream PDE results has been certified.

**Author-deferred:** All dedicated Demailly approximation/regularization, Bergman, L², Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof-completion work remains **deferred-by-user**. Dependent PDE inputs are recorded, not revisited.

## POME-BLOWUP-WEAK-ENDPOINT-001

**Severity:** low. **Status:** verified conditional deduction, **not a false theorem**. The printed strong \(L^s\) result for strict subcritical exponents is correct.

**Pinned source:** `docs/sections/equations-with-prescribed-singularities--minimal-singularities-on-blowups/index.html` at current main, blob `884c20eb0ab2b613129a84232e9b6688f3aba993`. Section setup lines 10–17. Proposition 15.23.2 has stable source label `non-kahler-pluripotential-theory-7C4F9B6C`, permanent tag `E42F32DA29D8`, lines 20–56. Theorem 15.23.5 has stable source label `non-kahler-pluripotential-theory-3D393512`, permanent tag `66FFA0C36433`, lines 60–90. Its exponent (15.23.7), tag `7E7FF8A6A54E`, is at lines 67–70; its Jacobian identity (15.23.8), tag `2BE1216FD9F5`, appears at lines 77–85. The iterated-blowup Theorem 15.23.10, stable label `non-kahler-pluripotential-theory-5971231E`, tag `37D35D78F0C6`, lines 102–121, is used for comparison only.

### Exact claim

Let \(\pi:X=\operatorname{Bl}_Z Y\to Y\) be the blowup of a compact smooth complex manifold \(Y\) along a **smooth center \(Z\) of complex codimension \(r\ge2\)**. Fix smooth positive volume forms \(\mu\) on \(X\) and \(v\) on \(Y\). For \(1<p<\infty\), let \(f\ge0\) belong to \(L^p(X,\mu)\), and write
\[
\pi_*(f\mu)=Fv,\qquad s_*=\frac{rp}{(r-1)p+1}.
\]
Then the endpoint Lorentz estimate
\[
\boxed{\sup_{t>0}t\,v(\{F>t\})^{1/s_*}
\le C_{\pi,\mu,v,p}\,\|f\|_{L^p(X,\mu)}}
\]
holds. In particular \(F\in L^{s_*,\infty}(Y,v)\). This estimate is independent of Monge–Ampère existence and regularization. **Strong** \(L^{s_*}\) is false for some admissible \(L^p\) data, and no strictly larger weak-\(L^s\) exponent is universally valid.

### Direct proof of the weak endpoint

Let \(E\) denote the exceptional divisor and \(W=d(\pi_*\mu)/dv\). Both \(\mu(E)\) and \(v(Z)\) are zero. In a standard normal blowup chart, with coordinates tangential to \(Z\) suppressed, the map is \((z,w)\mapsto(z,zw)\) with complex Jacobian \(z^{r-1}\). The exceptional projective fibers admit a finite cover by bounded affine angular charts. Smooth positive Jacobian factors stay uniformly comparable on their compact closures. Consequently
\[
W(y)\le C\,\operatorname{dist}(y,Z)^{-2(r-1)}
\]
in a sufficiently small tubular neighborhood of \(Z\); away from it \(W\) is bounded. Real normal codimension \(2r\) implies
\[
v(\{W>t\})\le C\,t^{-r/(r-1)}
\]
for large \(t\). Put \(a=r/(r-1)>1\). Splitting the layer-cake integral of \(W\) on a measurable set \(A\subset Y\) at \(T\asymp v(A)^{-1/a}\) gives
\[
\begin{aligned}
\int_A W\,dv
&=\int_0^\infty v(A\cap\{W>t\})\,dt\\
&\le Tv(A)+C\int_T^\infty t^{-a}\,dt
\le C'v(A)^{1-1/a}=C'v(A)^{1/r}.
\end{aligned}
\]
Adjust the constant for large sets or thresholds. Thus \(\pi_*\mu(A)\le C'v(A)^{1/r}\). By Hölder upstairs, with \(p'=p/(p-1)\),
\[
\int_A F\,dv
=\int_{\pi^{-1}(A)}f\,d\mu
\le \|f\|_p\,\mu(\pi^{-1}(A))^{1/p'}
\le C''\|f\|_p\,v(A)^{1/(rp')}.
\]
For \(A=\{F>t\}\) one also has \(tv(A)\le\int_A F\,dv\). Finally
\[
1-\frac1{rp'}=\frac{(r-1)p+1}{rp}=\frac1{s_*},
\]
so \(t\,v(A)^{1/s_*}\le C''\|f\|_p\) as claimed. No limiting argument for singular Monge–Ampère products occurs.

### Strong-endpoint counterexample and optimal weak exponent

Work in an adapted chart above a relatively compact open part of \(Z\), and restrict \(w\) to a bounded positive-angular-measure patch. Let \(\chi\) be a nonnegative cutoff supported there, equal to one in a smaller patch. For sufficiently small \(z\), set
\[
f(z,w,y)=\chi(z,w,y)\,|z|^{-2/p}
\bigl(\log(e/|z|)\bigr)^{-\beta},
\qquad \frac1p<\beta\le\frac1{s_*}.
\]
The interval of \(\beta\) is nonempty since \(s_*<p\). The upstairs integrability requirement reduces to
\[
\int_0^\varepsilon
\frac{dt}{t(\log(e/t))^{\beta p}}<\infty,
\]
so \(f\in L^p(X,\mu)\). On a downstairs positive-angular-measure normal cone where \(\chi=1\), the density satisfies
\[
F\asymp |z|^{-2(r-1+1/p)}
\bigl(\log(e/|z|)\bigr)^{-\beta}.
\]
There the downstairs normal volume is comparable to \(t^{2r-1}dt\) (all remaining angular and tangential volumes are uniformly bounded above and below). Because \(s_*(r-1+1/p)=r\),
\[
\int_YF^{s_*}\,dv\ \gtrsim\
\int_0^\varepsilon
\frac{dt}{t(\log(e/t))^{\beta s_*}}=\infty,
\]
as \(\beta s_*\le1\). This defeats universal strong-\(L^{s_*}\) even though the weak endpoint holds. For any \(s'>s_*\), normal annuli of scale \(t\) in the same cone have downstairs volume comparable to \(t^{2r}\) and \(F\) bounded below by \(ct^{-2r/s_*}(\log(e/t))^{-\beta}\). Hence their contribution to the weak-\(L^{s'}\) quasi-norm grows at least as
\[
c\,t^{-2r/s_*+2r/s'}(\log(e/t))^{-\beta}\longrightarrow\infty.
\]
So the weak exponent \(s_*\) is optimal.

**Proposed optional correction / dependents:** add a Lorentz endpoint corollary immediately after the measure pushforward estimate in Theorem 15.23.5, retaining the original strict-\(L^s\) claim, historic attribution and permanent tags. It does **not** imply a target Monge–Ampère endpoint \(L^\infty\) or Hölder theorem. Nor does this single-blowup estimate automatically prove an endpoint for the composite in Theorem 15.23.10. The theorem's analytic existence input is a separate unverified dependency, not a demonstrated error.

## Additional actual independent proof checks (no duplicate finding)

**§15.23:** The expression \(\theta=\pi^*h+c\Theta_E\), \(\mathrm{dd}^cL=[E]-\Theta_E\), and the modified divisor metric \(L'=L+\sigma\), \(\Theta'_E=\Theta_E-\mathrm{dd}^c\sigma\), give exactly
\[
\theta+\mathrm{dd}^c((c+\delta)L'-c\sigma)
=\pi^*h+(c+\delta)[E]-\delta\Theta'_E.
\]
This confirms the displayed sign in Proposition 15.23.2 on the selected lines. Distinguished the divisor current from the smooth Jacobian density in Theorem 15.23.5; the full distributional descent and iterated-blowup classification were **not** certified.

**§15.24 (first selected proof pass):** `docs/sections/equations-with-prescribed-singularities--representing-measures-in-an-ordinary-type/index.html`, blob `124c7650d904ff9617e90fe5e283c98e72261ea5`. Proposition 15.24.1 permanent tag `A46357C92C12`, lines 10–114; Lemma 15.24.4 tag `F9088D3DDEBB`, lines 118–129. Checked the ordinary-type sandwich \(\varphi-C_k\le q_k\le\varphi\), monotone weighted convex combination \(\psi_N\downarrow\psi\), fixed-\(k\) positive mixed-mass domination and the need for \(\sigma\)-finiteness of the extended measure before invoking Radon–Nikodym. The local domination Lemma 5.27.10, full extended-product Theorem 13.14.3 and strict-current existence remain conditional internal inputs; no new unsupported claim about them.

**§15.32 (incremental crosscheck):** `docs/sections/equations-with-prescribed-singularities--stability-of-the-subsolution-threshold/index.html`, blob `903ae0ce7173604063a833295dd94e971b18fd72`, Theorem 15.32.1 tag `D988D47D5E0E` lines 11–29; Propositions 15.32.4–.6 tags `D697A55DE07C`, `4C06D1B94BD1`, `C926F63790E3` lines 40–129; Proposition 15.32.9 tag `2210D4123A64` lines 196–231; Proposition 15.32.11 tag `7A2CC1A3258E` lines 248–281. Rechecked specific truncation, measure, root-norm normalization and completeness steps. Crucially **POME-SUBSOL-ROOT-NET-DOMCONV-001** and its arbitrary-directed-net formulation already appear in the 2026-10-24 report; they are **not** new findings.

## Unresolved / deferred / verification boundary

No new confirmed false theorem or proof gap was established. The single-blowup Lorentz endpoint is a complete geometric-measure-theoretic deduction. The analytic PDE assertions of §15.23.5, full birational-current classification, §15.24 extended-product and sigma-finite results, Gauduchon duality, and iterated blowups are not all independently certified. User-deferred approximation programme remains **deferred-by-user**, not reclassified as resolved. No build, CI, formal verification, site publication, source HTML, original manuscripts, registries, permanent tags or main-branch edits were made.