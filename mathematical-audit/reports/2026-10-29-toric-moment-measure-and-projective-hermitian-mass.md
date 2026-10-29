# Mathematical audit, 29 October 2026: toric moment-measure normalization and Hermitian mass on projective products

## Immutable review basis and scope

Production <code>main</code>: <code>b6933b772f41b45918f7e25ed1afbbb1fd892272</code> (checked on this run). This is **selected proof-level scrutiny**, not a certification of entire sections or the collection. The integrated, publicly available reading edition was read directly. No source/published-body/canonicalization/permanent-tag edits are authorized by this report.

The first selection is §21.14.6–8 (new direct proof audit), with §21.14.4 and §21.12.8/13 as comparisons of definitions and normalization, *not* independently certified inputs. The second is §11.1.4–5 and §11.1.11–18 (selected nonexcluded mass polynomial, explicit formula, and comparison-principle steps), using only elementary product geometry. No claim of full-section certification is made.

## POME-HOPF-TORIC-MOMENT-PUSHFORWARD-001

**Classification:** low severity / **verified conditional deduction**; original Proposition 21.14.8 and Theorem 21.14.4 are correct at the reviewed steps. This is an optional, quantitatively sharper corollary, not an allegation of error or a full theorem proof.

**Integrated anchors:** <code>docs/sections/hopf-fibrations-and-toric-potentials/index.html</code>, blob <code>0e83de13efbd70dfddc64a8eed40baed2d4359c5</code>; §21.14.6–8, lines **141–201**, source <code>non-kahler-pluripotential-theory:7515BE71</code>, permanent Proposition tag <code>F23340CADBE0</code>, homogeneity equation source <code>8E23893D</code>, permanent tag <code>5DB0E5246A09</code>. For the fiber normalization compare lines **16–20, 52–55, 61–106** and Theorem 21.14.4 source <code>8A7CCCFA</code> / permanent tag <code>94243AEE3360</code>. Convention comparison (no claim of separate proof certification): <code>docs/sections/toric-pluripotential-theory-on-ample-line-bundles/index.html</code>, blob <code>56a1a55dfc8185aee0e6d495a6a93d8a2313d76b</code>, lines **96–101, 163–175, 238–290**.

**Precise hypotheses.** Let \(n\ge2\), \(d=n-1\), \(k>0\) (real), \(\sigma=\mathrm{dd}^{\mathrm c}\log\sum|z_i|^2\) on \(\mathbb P^d\) with \(\int_{\mathbb P^d}\sigma^d=1\), and let \(v\) be a smooth torus-invariant real function with \(\tau=k\sigma+\mathrm{dd}^{\mathrm c}v>0\). On the dense projective torus use \(z_n=1\), \(q_i=\log|z_i|^2\), \(\theta_i=\arg z_i\) for \(1\le i\le d\), and
\[
 \widehat F(q)=k\log(1+\sum_{i=1}^d e^{q_i})+v(q),\quad
 p_i=\partial_{q_i}\widehat F,\quad p_n=k-\sum_{i=1}^d p_i.
\]
Proposition 21.14.8 asserts that \(\mu:q\mapsto(p_1,\ldots,p_d)\) bijects \(\mathbb R^d\) with the open simplex
\[
 \Delta_k^\circ=\{p_i>0,\ \sum_{i=1}^d p_i<k\}.
\]

**New exact conclusion.** For every bounded Borel \(g\) on \(\overline{\Delta_k}\),
\[
 \int_{\mathbb P^d}g(\mu)\,\tau^d
 =d!\int_{\Delta_k}g(p)\,\mathrm dp_1\cdots\mathrm dp_d.
 \tag{A}
\]
In particular the pushforward is **flat Lebesgue measure** of density \(d!\), not density 1 and not Euclidean hypersurface measure on the simplex in \(\mathbb R^n\); its total mass is \(k^d\). For \(k=1\), in the scalar Hopf manifold \(X_n\), write \(u=\pi^*v\) and retain the original \(\omega=\alpha+\zeta\). Theorem 21.14.4 and the fiber normalization \(\int_{\pi^{-1}(y)}\zeta=2\) give
\[
 (\mu\circ\pi)_*((\omega+\mathrm{dd}^{\mathrm c}u)^n)
 =2n\,d!\,\mathbf1_{\Delta_1}\,\mathrm dp,\qquad
 \int_{X_n}(\omega+\mathrm{dd}^{\mathrm c}u)^n=2n.
 \tag{B}
\]
Here \(\mu\circ\pi\) is defined almost everywhere; the omitted coordinate divisors are null for the smooth measures. More generally, if one *defines* the positive Hermitian form \(\omega^{(k)}=k\alpha+\zeta\), the same direct binomial expansion gives density \(2n\,d!\) on \(\Delta_k\) and total mass \(2n k^d\). This generalized background is a new conditional construction, **not** the displayed formula of Theorem 21.14.4 for its original fixed \(\omega\).

**Direct proof, including factors and signs.** Under the collection's convention \(\mathrm{dd}^{\mathrm c}=\frac{i}{2\pi}\partial\bar\partial\) and \(q_i=\log|z_i|^2\), the explicit complex Hessian calculation yields
\[
 \tau=\frac1{2\pi}\sum_{i,j=1}^d
  \widehat F_{ij}(q)\,\mathrm dq_i\wedge\mathrm d\theta_j .
\]
The Hessian is positive definite, hence the gradient map is a local diffeomorphism. Proposition 21.14.8 proves that it is a global bijection onto \(\Delta_k^\circ\), so it is a diffeomorphism. Wedge algebra and the positive complex orientation give
\[
 \tau^d=\frac{d!}{(2\pi)^d}\det D^2\widehat F(q)\,
   \mathrm dq_1\cdots\mathrm dq_d\,
   \mathrm d\theta_1\cdots\mathrm d\theta_d
\]
(with the indicated orientation convention). Each angular variable ranges over \(2\pi\), leaving \(d!\det D^2\widehat F\,\mathrm dq\). Since \(D\mu=D^2\widehat F\), change of variables gives (A) for nonnegative Borel \(g\), hence by decomposition for bounded signed \(g\). The projective boundary has zero measure for the smooth \(\tau^d\). Volume of the affine-coordinate simplex is \(k^d/d!\). Finally, \(\zeta^2=0\), horizontal dimension \(d\), and the fiber integral 2 give \(\pi_*((\pi^*\tau+\zeta)^n)=2n\,\tau^d\); (B) follows. The entire argument is direct differential geometry conditional only on the already printed Hopf-fiber identities and the verified proposition's global gradient diffeomorphism.

**Comparison and proposal.** The broader toric/Legendre framework of §21.12 already gives related convex dictionaries, but §21.14 retains an independent valid Hopf-specific fiber normalization. These statements must **not** be merged as a purported genuine duplicate. Optionally add (A)–(B) as a moment-measure and normalization cross-check at §21.14.8, referring to the earlier toric framework while retaining both provenance records. Affects toric Monge–Ampère/section-growth comparisons (§§21.12, 21.14, 19.9) and Hopf descended mass (§23.1); no previously open finding is closed.

## POME-HERM-PROJECTIVE-MASS-ALLDIM-001

**Classification:** low severity / **verified conditional deduction**; original mass polynomial, Example 11.1.12 and comparison-principle obstruction are correct. This is an all-dimensional/projective strengthening of the **same explicit construction**, not a new general mass-invariance theorem.

**Integrated anchors:** <code>docs/sections/torsion-and-the-variation-of-mass/index.html</code>, blob <code>9abec9685e33a1b40f9c0765381408eb52b325d3</code>, §11.1.4–5, lines **68–96, 99–152**, source mass theorem <code>non-kahler-pluripotential-theory:D4902E5B</code> / permanent tag <code>2B3316345A4A</code>; §11.1.11–18, lines **208–294**, Example 11.1.12 source <code>028A9E19</code> / permanent tag <code>F336FEED9D87</code>, equation 11.1.13 source <code>F1D489BD</code> / permanent tag <code>914CB776FFB8</code>, comparison Proposition 11.1.16 source <code>77EFDB7F</code> / permanent tag <code>2A8C104899E8</code>.

**Precise hypotheses.** Let \(E=\mathbb C/(\mathbb Z+i\mathbb Z)\), \(S=E\times E\), and use the original smooth positive forms \(\beta_j=\frac{i}{2\pi}\mathrm dz_j\wedge\mathrm d\bar z_j\). Define \(h(x_1)=\cos(2\pi x_1)\), \(b=2+h\), \(a_t=1-\pi^2t h\), \(\omega_{S,t}=a_t\beta_1+b\beta_2\), and \(u_t=t h\), so \(\omega_{S,t}=\omega_{S,0}+\mathrm{dd}^{\mathrm c}u_t\). Let \(n\ge2\), let \(Y\) be any compact Kähler manifold of complex dimension \(n-2\) (a point for \(n=2\)), let \(\eta\) be Kähler, \(V=\int_Y\eta^{n-2}>0\) (set \(V=1\) if \(Y\) is a point), and
\[
 X=S\times Y,\quad \Omega=\operatorname{pr}_S^*\omega_{S,0}
   +\operatorname{pr}_Y^*\eta,\quad U_t=\operatorname{pr}_S^*u_t .
\]
For \(|t|<\pi^{-2}\), \(\Omega+\mathrm{dd}^{\mathrm c}U_t>0\) although \(\Omega\) is not closed.

**New exact conclusion, all dimensions.** With \(B=\int_S\beta_1\wedge\beta_2>0\),
\[
 \int_X(\Omega+\mathrm{dd}^{\mathrm c}U_t)^n
   =\binom n2(4-\pi^2t)BV.
 \tag{C}
\]
Thus the mass derivative is the strictly negative constant
\(-\binom n2\pi^2 BV\) for every \(n\ge2\). If \(Y=\mathbb P^{n-2}\) with normalized Fubini–Study form, then \(X\) is **projective in every complex dimension \(n\ge2\)**, yet the arbitrarily selected nonclosed Hermitian background \(\Omega\) has varying Monge–Ampère mass among smooth strict potentials. For any \(-\pi^{-2}<t<0\), choose \(C>|t|\), take \(U=0\), \(W=U_t+C\). Then \(U<W\) everywhere while
\[
 \int_{\{U<W\}}(\Omega+\mathrm{dd}^{\mathrm c}W)^n
 >
 \int_{\{U<W\}}(\Omega+\mathrm{dd}^{\mathrm c}U)^n.
\]
This is a sharp, explicit obstruction to the **unmodified** comparison inequality in all dimensions even when the underlying complex manifold admits a Kähler metric. It does not contradict Kähler-background comparison: \(\Omega\) itself is nonclosed.

**Direct proof.** In the expansion of \((\operatorname{pr}_S^*\omega_{S,t}+\operatorname{pr}_Y^*\eta)^n\), bidegree forces exactly two factors from \(S\) and \(n-2\) from \(Y\). Thus
\[
 (\Omega+\mathrm{dd}^{\mathrm c}U_t)^n
   =\binom n2\operatorname{pr}_S^*(\omega_{S,t}^2)
      \wedge\operatorname{pr}_Y^*(\eta^{n-2}).
\]
The source's original computation gives \(\int_S\omega_{S,t}^2=(4-\pi^2t)B\). For completeness, \(\omega_{S,t}^2=2a_tb\,\beta_1\wedge\beta_2\) and the \(x_1\)-period averages of \(h\), \(h^2\) are respectively 0 and \(1/2\), so the integral is \((4-\pi^2t)B\). Fubini proves (C). Positivity follows from \(1-\pi^2|t|>0\), \(1\le b\le3\), \(\eta>0\). The constant shift does not affect the Hessian; the indicated comparison inequality fails. No approximation/regularization/L²/OT input is used.

**Comparison and proposal.** The surface calculation is printed at §11.1.12; (C) is a strictly all-dimensional direct extension and is not a second proof of the same surface statement. It is optional as an illustration after §11.1.18; it shows why the usual Kähler comparison does not become valid merely because the complex manifold is projective. Affects §§11.1.5–18, 14.19, 14.25, and Hermitian volume bounds. No previously open case is certified or resolved.

## Coverage, unresolved and deferred boundary

Actual first direct selected proof-level audit: §21.14.6–8 and §11.1.11–18, with exact formulas §11.1.4–5 scrutinized. §21.14.4 is inspected for its fiber factor; §21.12.8/13, §19.8.12 and §23.1 are comparison/context only. No complete §21.14, §11.1, or other section is certified. The existing collection inventory remains **25 chapters / 747 numbered ToC sections / zero fully certified sections**. No old finding is relabeled resolved, nor is any confirmed error asserted in these two models.

The proof of Theorem 11.1.7 for *bounded* potentials (integrated lines 146–147) invokes globally decreasing smooth strict approximation at §5.32.1. This is recorded only as an existing **deferred-by-user** regularization dependency; it was **not** checked, extended, reopened, or treated as resolved. All prior Demailly approximation/regularization and dedicated Bergman, weighted L², Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof-completion projects retain **deferred-by-user** status. No external source quotation was imported and no source attribution removed.

Checks performed: direct reading of the cited integrated HTML, independent exterior-algebra, coordinate-Jacobian, simplex-volume and Fourier-period calculations. No software tests, builds, GitHub Actions, website publication, formal verification, source or main change were performed.
