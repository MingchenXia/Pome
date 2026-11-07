# 2026-11-08 — Sharp Poisson harmonic-measure norms and disk total variation

**Finding POME-PERRON-POISSON-NORM-TV-SHARP-001** — **low / verified conditional deduction**. The printed theorem is not false.

**Production main checked:** b6933b772f41b45918f7e25ed1afbbb1fd892272. Integrated path **docs/sections/perron-theory-and-fine-boundary-limits/index.html**; blob **4bc2fb9317e2b6f6bb5b2d90208c677da8275eba**; section 4.4 permanent **5CFAC22DC258**. **Theorem 4.4.2:** source **classical-potential-theory:410B64F2**, permanent **09873BDAF3E0**, physical lines **10–35** (especially line 11, representation/equivalent norms 27–33). **Theorem 4.4.11** source classical-potential-theory:07EA9CB6 / permanent E16C09608A00 / lines 123–139 was only checked contextually for interior/exterior Poisson conventions.

## Precise statement

For the unit ball \(B\subset\mathbb R^d\), \(d\ge2\), let \(\omega_x\) denote Perron harmonic measure. At \(x=re_1\), \(0\le r<1\), with normalized sphere measure \(\sigma_0\),
\[
\omega_0=\sigma_0,\qquad
\frac{d\omega_{re_1}}{d\omega_0}(\zeta)
=P_r(\zeta)=\frac{1-r^2}{|re_1-\zeta|^d}.
\]
For \(1\le p<\infty\), the *sharp two-way* norm equivalence is
\[
\boxed{\|\mathrm{id}:L^p(\omega_0)\to L^p(\omega_{re_1})\|
=\left(\frac{1+r}{(1-r)^{d-1}}\right)^{1/p}},
\]
\[
\boxed{\|\mathrm{id}:L^p(\omega_{re_1})\to L^p(\omega_0)\|
=\left(\frac{(1+r)^{d-1}}{1-r}\right)^{1/p}}.
\]
At \(p=\infty\) both norms equal 1. Therefore equivalence in Theorem 4.4.2 is not uniformly quantitative when the interior evaluation point approaches the sphere; the theorem does not assert uniformity.

For \(d=2\), the exact **full signed total-variation norm**, *twice* the standard probability total-variation distance, is
\[
\boxed{\|\omega_{re_1}-\omega_0\|_{\mathrm{TV}}
=\frac4\pi\arcsin r}.
\]
Its gap to 2 is exactly \((4/\pi)\arccos r\sim(4\sqrt2/\pi)\sqrt{1-r}\) as \(r\uparrow1\). Although \(\omega_{re_1}\rightharpoonup\delta_{e_1}\), its full-TV distance to that point mass equals 2 for every \(r<1\), as the measures are mutually singular.

## Proof independent of an external Poisson formula

Let \(P(x,\zeta)=(1-|x|^2)|x-\zeta|^{-d}\) for \(|x|<1\) and \(|\zeta|=1\). With \(v(x)=|x-\zeta|^{-d}\), one has \(\nabla v=-d(x-\zeta)|x-\zeta|^{-d-2}\), \(\Delta v=2d|x-\zeta|^{-d-2}\), and
\[
\Delta_xP
=2d|x-\zeta|^{-d-2}
[-|x-\zeta|^2+2x\cdot(x-\zeta)+1-|x|^2]=0.
\]
The average \(I(x)=\int P(x,\zeta)d\sigma_0(\zeta)\) is smooth, harmonic and rotationally invariant on the full ball; smooth radial harmonic functions on a ball are constant, and \(I(0)=1\). Hence \(I\equiv1\). For continuous \(f\), the function \(u(x)=\int P(x,\zeta)f(\zeta)d\sigma_0(\zeta)\) is harmonic and tends to \(f(\zeta_0)\) as \(x\to\zeta_0\): mass outside any neighborhood of \(\zeta_0\) tends to zero, and uniform continuity controls the rest. The maximum principle identifies the unique continuous Dirichlet solution. Uniqueness of representing measures against continuous \(f\) identifies \(P(x,\cdot)\sigma_0\) with Pome's \(\omega_x\).

On the sphere, the distances \(|re_1-\zeta|\) have minimum \(1-r\) and maximum \(1+r\), attained at \(e_1\) and \(-e_1\). Thus
\[
\max P_r=\frac{1+r}{(1-r)^{d-1}},\quad
\min P_r=\frac{1-r}{(1+r)^{d-1}}.
\]
Integrating \(|f|^p\) against these density bounds gives the two norm estimates. They are **sharp**, since indicator functions of shrinking positive-measure caps at \(e_1\) or \(-e_1\) yield the limiting maximum or reciprocal minimum. At \(p=\infty\), both measures have precisely the same null sets.

For \(d=2\), let \(\zeta=e^{i\theta}\). Then
\(P_r(\theta)=(1-r^2)/(1-2r\cos\theta+r^2)\), and \(P_r>1\) precisely for \(|\theta|<\alpha=\arccos r\). Both probabilities have mass 1, whence
\[
\|\omega_{re_1}-\omega_0\|_{\mathrm{TV}}
=2\left[\frac1{2\pi}\int_{-\alpha}^{\alpha}P_r(\theta)d\theta-\frac\alpha\pi\right].
\]
The substitution \(t=\tan(\theta/2)\) gives
\[
\frac1{2\pi}\int_{-\alpha}^{\alpha}P_r\,d\theta
=\frac2\pi\arctan\left(\frac{1+r}{1-r}\tan\frac\alpha2\right)
=\frac2\pi\arctan\sqrt{\frac{1+r}{1-r}}.
\]
Since \(\arctan\sqrt{(1+r)/(1-r)}=\pi/4+\frac12\arcsin r\) and \(\alpha=\pi/2-\arcsin r\), the asserted exact total variation follows. The case \(r=0\) is by continuity. The boundary asymptotic follows from \(\arccos r\sim\sqrt{2(1-r)}\).

## Audit judgment, correction, dependencies, coverage

**Status: low / verified conditional deduction**, not a false theorem, not a repair of a missing general proof, and not a new external dependency. The unit-ball computation is complete. Theorem 4.4.2's equivalent finite-\(p\) measures and interior weak continuity are compatible with it. This audit **does not** transitively verify the general-domain Perron class, polar completions or every dependency.

**Suggested annotation only:** after Theorem 4.4.2, one can add these exact constants and explain why they depend on the interior evaluation point. Any downstream argument requiring pole-*uniform* \(L^p\) norm equivalence close to \(\partial B\) needs a separate hypothesis; **no specific false downstream claim was identified**. Preserve original history, attribution, source tags and permanent tags.

**Coverage:** newly inspected Theorem 4.4.2 in previously partly reviewed §4.4 (previous work addressed Wiener/fine-boundary and exterior-ball clauses). **0 newly first-visited numbered sections; 0 mathematically certified complete sections; actual inventory 25 chapters / 747 sections / 0 certifications.** Existing classifications unchanged. User-excluded Demailly approximation/regularization and dedicated Bergman, weighted-\(L^2\), Ohsawa–Takegoshi, multiscale-atlas and positivity-loss work remains **deferred-by-user**. No build, tests, GitHub Actions CI, formal verification, production or source edits, canonicalization changes, or publication.
