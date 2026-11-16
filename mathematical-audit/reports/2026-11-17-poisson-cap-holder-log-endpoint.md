# 2026-11-17 — Sharp Poisson boundary rates from spherical-cap variation

**Finding ID:** POME-HARM-POISSON-CAP-HOLDER-ENDPOINT-001  
**Classification:** low / **verified conditional deduction**; **no printed theorem refuted**.  
**Reviewed main:** b6933b772f41b45918f7e25ed1afbbb1fd892272.  
**Integrated file:** docs/sections/classical-harmonic-analysis/index.html, Git blob 75e982788e627af602981823a82863cbd36ee712.  
**Anchors:** §3.3.9 (permanent tag CAE5D89698DF; local radial kernel and integration-by-parts, physical lines 118–140); §3.3.12 (tag 5F363A880A82, lines 160–185; cap differentiation); §3.3.14 (tag EEE7DD56F49D, lines 190–205; exact cone kernel bound and annular argument). All statements are from the current integrated reading edition, source family classical-potential-theory. See also the Poisson kernel formula in the proof of §3.3.9. This is not a re-audit of the previously recorded fine-cover-separation repair or tangential-approach counterexample.

## Proposition (conditional sharpening at a fixed boundary point)

Write \(S=\partial B(0,1)\subset\mathbb R^d\), \(d\ge2\), \(\sigma\) for unnormalized surface measure, and \(C_s(\zeta)=\{y\in S:|y-\zeta|\le s\}\). Let \(\nu\) be a finite signed measure. Suppose, for some \(\alpha>0\), \(\delta\in(0,1)\), and \(M\ge0\),
\[
 |\nu|(C_s(\zeta))\le M s^{d-1+\alpha}\quad(0<s\le\delta).
 \tag{1}
\]
For any finite non-tangential aperture \(A\ge1\), uniformly as \(x\to\zeta\) with \(|x-\zeta|\le A(1-|x|)\) and \(t=1-|x|\),
\[
 |P_B\nu(x)|\le C_{d,A,\alpha,\delta}
 \bigl(M+|\nu|(S)\bigr)
 \begin{cases}
 t^\alpha,&0<\alpha<1,\\
 t\log(e/t),&\alpha=1,\\
 t,&\alpha>1.
 \end{cases} \tag{2}
\]
All three orders are **optimal** even for absolutely continuous positive measures, already along the radius \(x=(1-t)\zeta\). If \(\mu=f(\zeta)\sigma+\nu\), the same bound applies to \(|P_B\mu(x)-f(\zeta)|\). In particular, for an \(L^1\) density \(f\) satisfying \(|f(y)-f(\zeta)|\le L|y-\zeta|^\alpha\) in a neighborhood of \(\zeta\), its Poisson integral obeys (2). No rates are asserted from merely the almost-everywhere differentiation theorem.

## Upper estimate

The *exact* kernel (with respect to surface measure) is
\[
 P_B(x,y)=\frac{1-|x|^2}{s_{d-1}|x-y|^d},
 \quad s_j=|\mathbb S^j|.
\]
The original proof of §3.3.14, line 197–203, establishes
\[
 P_B(x,y)\le C_{d,A}\,t(t+|y-\zeta|)^{-d}. \tag{3}
\]
For \(2t<\delta/2\), split \(S\) into \(C_t\), the dyadic annuli \(2^{j-1}t<s\le 2^jt\le\delta\), one possible final truncated annulus, and the complement of \(C_{\delta/2}\). On the innermost cap, (1),(3) give \(CMt^{1-d}t^{d-1+\alpha}=CMt^\alpha\). On the \(j\)th annulus, they give at most
\[
 CM\,t (2^jt)^{-d}(2^jt)^{d-1+\alpha}
 =CM\,t^\alpha 2^{j(\alpha-1)}. \tag{4}
\]
The truncated outer annulus has the same estimate with its actual outer radius between \(\delta/2\) and \(\delta\). The complement contributes at most \(C_{d,A,\delta}\, t|\nu|(S)\). Summing (4) gives a convergent geometric sum for \(\alpha<1\), \(O(\log(\delta/t))\) terms for \(\alpha=1\), and \(O((\delta/t)^{\alpha-1})\) for \(\alpha>1\). This proves (2), uniformly over the *whole cone*, without passing to subsequences. For \(t\) outside this small range the bound follows by increasing the constant.

## Exact sharpness and the critical logarithm

Fix \(\zeta\in S\). Take the positive measure
\[
 d\nu_\alpha(y)=|y-\zeta|^\alpha\,d\sigma(y).
\]
It satisfies (1), since \(\sigma(C_s)\le Cs^{d-1}\). Write \(x=(1-t)\zeta\). The identity
\[
 |x-y|^2=t^2+(1-t)|y-\zeta|^2
\]
and spherical polar coordinates in chordal distance \(s=|y-\zeta|\) give the **exact one-dimensional integral**
\[
 P_B\nu_\alpha((1-t)\zeta)
 =\frac{t(2-t)s_{d-2}}{s_{d-1}}
 \int_0^2
 \frac{s^{d-2+\alpha}(1-s^2/4)^{(d-3)/2}}
 {[t^2+(1-t)s^2]^{d/2}}\,ds. \tag{5}
\]
The surface shell Jacobian here is
\(s_{d-2}s^{d-2}(1-s^2/4)^{(d-3)/2}ds\), including the integrable endpoint factor for \(d=2\).

For \(0<\alpha<1\), replace \(s=tu\) in a fixed small cap. Dominated convergence in \(\mathbb R^{d-1}\), valid precisely because \(\alpha<1\), and the \(O(t)\) far-cap contribution yield
\[
 \lim_{t\downarrow0}t^{-\alpha}P_B\nu_\alpha((1-t)\zeta)
 =\frac{s_{d-2}}{s_{d-1}}
 B\left(\frac{d-1+\alpha}{2},\frac{1-\alpha}{2}\right)>0. \tag{6}
\]
For \(\alpha=1\), the \(t\ll s\ll1\) integrand in (5) equals
\((2s_{d-2}/s_{d-1})\,t\,s^{-1}\) to leading order. Comparing the exact factors in (5) on \(s\in[t,\delta]\) and estimating the inner and outer remainder gives
\[
 P_B\nu_1((1-t)\zeta)
 =\frac{2s_{d-2}}{s_{d-1}}\,t\log(1/t)+O(t). \tag{7}
\]
For \(\alpha>1\), the limiting kernel divided by \(t\) is
\(2/(s_{d-1}|y-\zeta|^d)\). It is integrable against \(d\nu_\alpha\) exactly for \(\alpha>1\). Dominated convergence and the spherical beta integral give
\[
 \lim_{t\downarrow0}t^{-1}P_B\nu_\alpha((1-t)\zeta)
 =\frac{2^{\alpha-1}s_{d-2}}{s_{d-1}}
 B\left(\frac{\alpha-1}{2},\frac{d-1}{2}\right)>0. \tag{8}
\]
As a normalization check, \(\alpha=2\) gives the coefficient \(2\) exactly: the harmonic mean of \(|y-\zeta|^2=2-2\zeta\cdot y\) is \(2t\). Equations (6)–(8) prove that none of the three rates in (2) can improve for all such measures, including the logarithmic endpoint \(\alpha=1\).

## Scope and dependencies

This is a new **conditional quantitative corollary** of the explicit ball Poisson kernel and spherical-cap geometry used in §3.3.14. It neither challenges Theorems 3.3.9, 3.3.12 or 3.3.14, nor certifies their full upstream harmonic-measure construction, local Riesz theory, or the chapter as a whole. The variation hypothesis (1) is essential: signed cap mass cancellation alone does not imply it. The radial examples establish global *order* sharpness, not a universal optimal constant in arbitrary non-tangential cones. No Demailly approximation, Bergman, \(L^2\), Ohsawa–Takegoshi, multiscale-atlas, or positivity-loss argument is used.

**Suggested additive patch (not applied):** place a labeled quantitative corollary after the proof of §3.3.14, with hypothesis (1), three rates, and the sharp positive-density family (5). Preserve original statement, source attribution, permanent tags, and the older cap-differentiation proof.  
**Affected dependents:** any later use of Poisson boundary traces requiring an explicit modulus may cite this scoped bound after integration; absent (1), retain the qualitative almost-everywhere result.  
**Coverage:** additional direct proof-level inspection of §3.3.9, §3.3.12, §3.3.14 and the current cone estimate; §3.3 previously partly reviewed; **0 new first-visited numbered sections, 0 fully mathematically certified sections**. No build, project test suite, CI, website publication or main/source edit was performed.
