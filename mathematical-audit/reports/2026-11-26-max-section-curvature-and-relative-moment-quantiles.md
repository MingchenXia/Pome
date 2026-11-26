# Audit — exact curvature support for finite maximum section metrics and relative moment quantiles

Date: 2026-11-26. Reviewed main: b6933b772f41b45918f7e25ed1afbbb1fd892272.
Audit parent: a6721464d8b895e1f5a430eea7c1c26e7f62fd8b.

## 1. POME-FS-MAX-EXACT-SUPPORT-TORSION-001

Severity low; status **verified conditional deduction**, not an error in the printed result.

Anchor: docs/sections/global-potentials-and-positive-cohomology-classes--curvature-and-metrics-defined-by-sections/index.html, blob ff56aa13950da3423135bb0bbaf40bcc980c21a1, Definition 10.6.8 (permanent 9CC891317C85, source 058B5289), lines 118–123, and Proposition 10.6.9 (permanent E5F620306821, source 869166DD), lines 127–142. The paragraph after the definition proves vanishing of the curvature on some open set. The following identifies its entire support and the smooth locus of the class of metrics.

Let X be connected compact, of positive complex dimension, L a holomorphic line bundle, and h a finite maximum FS metric in the sense of the definition. In a frame e write its local weight as

\[
 W=\frac1m\max_i(\log|f_i|^2+\lambda_i),\quad s_i=f_i e^m.
\]

Discard identically zero sections. Identify two indices if the weighted squared norms \(e^{\lambda_i}|s_i|_{h_0^m}^2\) agree identically on X; this condition is independent of the smooth reference metric. Let Z denote the common zero set; let S consist of points outside Z where two distinct remaining indices attain the maximum.

**Claim.** The support of \(c_1(L,h)\) is exactly \(Z\cup S\); it has smooth volume measure zero. Consequently the current is singular with respect to smooth volume (each coefficient measure is supported on that null set). In particular, FS(L) contains a smooth metric if and only if L is torsion in Pic(X), i.e. some positive tensor power is holomorphically trivial. Every smooth FS metric is flat, and in the torsion case these metrics are precisely the flat metrics, unique up to positive scalar.

Proof. At a point outside Z with a unique remaining maximizer, the positive gap in weighted squared norms persists on a neighborhood. The maximizing section is nowhere zero on a smaller neighborhood and W is pluriharmonic there. Thus curvature vanishes on the complement of Z union S. At a point of Z, if the curvature vanished on a neighborhood, its local PSH weight would be pluriharmonic there (take the trace of its distributional complex Hessian and use the harmonic representative, then the canonical PSH representative). This contradicts W=-infinity at the point. At a point outside Z with two distinct active indices i,j, shrink to a ball on which both sections are nonzero. If the curvature vanished there, W would be pluriharmonic. Each harmonic difference W minus the corresponding scaled log norm is nonnegative and vanishes at the center. The minimum principle forces both differences to vanish throughout the ball. Thus the weighted squared norms coincide on the ball. Their equality is a real-analytic identity in local frames; it propagates across overlapping charts on connected X because multiplication by the same nonvanishing transition factor preserves equality. This contradicts the identification of indices. These arguments establish exact support, including at the base locus.

For each pair of distinct indices the equality is the zero set of a nonidentically zero real-analytic function in any connected coordinate ball with a holomorphic frame; it has Lebesgue measure zero. One elementary justification is induction in real dimension using convergent power series on small boxes: expand in one variable about a fixed center, choose a nonzero coefficient analytic in the other variables; the exceptional slices where that coefficient vanishes are null by induction, and the zeros on each remaining one-dimensional slice are discrete. Countably many boxes and Fubini suffice. The common zero locus Z is null because at least one section is not identically zero. This proves the singularity assertion. The support is closed as it is the finite union of closed weighted-max tie sets, including Z (or directly by the proved support identity).

If h is smooth, its curvature is smooth and vanishes outside a volume-null set, hence is zero everywhere. For any nonzero section s_i in its presentation, \(\log |s_i|_{h^m}^2\) is globally PSH by the local flat weight formula, not identically -infinity. The global maximum principle on connected compact X makes it a finite constant (also established in §10.9 introduction). So s_i has no zeros and trivializes \(L^m\). Conversely a nowhere vanishing section of \(L^m\) supplies a smooth FS metric by the single-section formula; its curvature vanishes. If h' is any other smooth flat metric on L, its logarithmic ratio to this one is globally pluriharmonic and constant. Rescaling the section in the single-section formula realizes any positive constant multiple, even with lambda=0, so every flat metric on a torsion L is FS. This is an exact finite-section statement, not a Bergman approximation or density claim. In particular a non-torsion flat line bundle cannot have a smooth FS metric; indeed any nonzero section of any power would be nowhere vanishing by the same maximum principle, so its FS set is empty.

Internal inputs: local PSH representatives and harmonic maximum principle; line-bundle metric and curvature conventions of §10.6; §10.9 opening compact maximum principle. The real-analytic zero-set argument is given above. No claim to certify all upstream inputs. The printed paragraph and Proposition 10.6.9 remain correct under their analytic-singularity convention. Proposed optional addition after the paragraph at line 123; no source edit. Affected scope: any use of the max-section FS class in §10.6.9 and subsequent section-metric arguments that might conflate classical smooth log-sum and finite max metrics; no particular false downstream statement asserted.

## 2. POME-RELATIVE-MOMENT-STRETCH-QUANTILE-001

Severity low; status **verified conditional deduction**. Printed Proposition 10.31.8 is not refuted.

Anchor: docs/sections/big-backgrounds-under-bounded-mass/index.html, blob 0cc1ca66dd13369d9ae3f4aa43bb3bb074c05571. Proposition 10.31.8, permanent 56A4FC216C27, source A5D06B67, lines 154–232; equation 10.31.9 permanent C1417B0EF5E7/source 784C92A4, line 169; equation 10.31.10 permanent 525AD3E9DFE4/source 5EBA72B0, line 178; stretched tail estimate line 208. Adopt all standing hypotheses in lines 8–48 (big smooth possibly nonclosed theta, bounded mass property, model reference with positive lower volume, full-mass class, finite non-pluripolar measures). Fix w in the relative full-mass class and choose w' of its ordinary type with w' <= w and \(\delta=M-\mu_{w'}(X)<\ell/2\) as in the proof. Choose R real with

\[
 q_R=\mu_{w'}(\{w'<-R\})<\ell-\delta.
\]

Such R exists by finiteness and absence of mass on the pole set. Put \(D_R=\ell-\delta-q_R>0\).

For every relative full-mass u with \(\int(w-u)_+\,d\mu_u\le K\), let p=P_theta(u,w'). By contact support and ordered contact,

\[
 \int(w'-p)\,d\mu_p\le K.
\]

The integrands here and below are defined off the polar sets, which all measures in question ignore. This is the printed argument for (10.31.9), with its final one-sided variant (lines 225–231), applied directly to w'. For every b>=1 put \(h_b=Q_b(p,w')\), with h_1=p. The printed class stability for stretching and finite rooftops guarantees h_b in the relative full-mass class. Since p<=w', h_b<=p<=w'. For b>1 the contact estimate at lines 205–208 gives

\[
 \mu_{h_b}(\{h_b\le w'-bs\})\le b^n K/s\qquad(s>0).
\]

For b=1 the same assertion is Markov's inequality. The maximum estimate (10.31.10) applied to a=h_b at t=bs gives

\[
 \mu_{h_b}(\{h_b>w'-bs\})\le
 \mu_{w'}(\{h_b>w'-bs\})+\delta.
\]

If A=-R-sup_X h_b>0, choose s=A/b. Then the set in the right side is contained in \(\{w'<-R\}\), with the correct strict inequality. Splitting the total mass and using the lower bound ell yields

\[
 \ell\le \frac{b^{n+1}K}{A}+q_R+\delta.
\]

Thus A<=b^{n+1}K/D_R. If A<=0, the bound below already holds. In particular,

\[
 \boxed{\sup_X Q_b(P_\theta(u,w'),w')\ge
 -R-\frac{b^{n+1}K}{\ell-\delta-q_R}\quad(b\ge1).}
\]

The same estimate for b=1 gives \(\sup_X u\ge -R-K/D_R\). It works for K=0 as well: a positive A would contradict ell>q_R+delta. One may take the best bound over all admissible R, with a single fixed near-maximal-mass w'. No density, integrability, or uniform bound on w' itself beyond the printed assumptions is required.

This provides an explicit uniform noncollapse estimate for the stretched rooftops, rather than only ruling out collapse by contradiction. The powers of b follow from the printed contact bound and scaling of the threshold; no optimality claim. The proof is conditional on the existing class stability, locality, contact support, ordered contact and mass interval. It does not prove these upstream statements, nor the entire existence theorem 10.31.3. Affected dependents: 10.31.11 and the fixed-measure / moment compactness framework in 10.31.5, 10.31.8. No regularization or excluded analytic programme reopened. Optional addition after the stretched tail inequality at line 208.

## 3. Direct coverage and limits

- §10.6, full mathematical lines 7–142, blob ff56aa13950da3423135bb0bbaf40bcc980c21a1: frame curvature/metric transformations, local flat lift construction and connected overlaps, compact exhaustion/diagonal Montel argument, finite-dimensionality by separated orthonormal sequence, singular pointwise metric conventions, Poincare–Lelong normalization, projective charts and dual tautological convention, rational max/convex combination algebra. All checked conditional on cited local analytic tools. In particular rational coefficients of the weights remain as printed; arbitrary constant rescalings of sections in the definition do not change that convention. No whole upstream certificate.
- §10.31, selected lines 7–272, blob 0cc1ca66dd13369d9ae3f4aa43bb3bb074c05571: standing hypotheses, fixed-measure extraction skeleton, moment compactness, stretching contradiction and tail-envelope capacity convergence. Verified the order of extraction/limits in the displayed argument conditional on referenced ingredients, not the extraction theorem's complete proof. Lines 275 onward, including higher moments and equation existence, are not reviewed this run.
- §10.9, selected mathematical lines 7–114, blob 2346c71320d5c7772f9f055cc8b80699edf536a5: compact maximum principle, nonclosed background and coefficient freezing, binomial independence of local Bedford–Taylor product definition, positivity under local convolution with a vanishing error, monotone continuity, propagation of noncollapse through finite overlapping chart cover. The Hermitian background is not presumed closed. The local bounded BT continuity inputs are used as stated, not re-proved. The later global pole and comparison proof is not covered. No Demailly approximation is used; the bounded local BT calculation is a separate nonexcluded construction.
- §5.18, selected introductory definition/convention context only (lines 7–16, blob 877d567c35ff3e75a0c1c874be251d75bf9f4927); dedicated approximation-related closure proof not revisited.

Actual table of contents at docs/chapters/index.html: 747 distinct section identifiers; matrix has 747 matching distinct identifiers, no missing or extra rows. All four selected matrix rows previously LEGACY-UNRECONCILED; no historical first-visit claim. Two new conditional deductions; one full conditional section, two selected mathematical sections, one convention-only context; zero new confirmed source errors, demonstrated proof gaps or complete transitive proof certifications. Existing excluded programmes remain deferred-by-user, not solved. No builds, tests, CI, website publication, source/body/registry/permanent-tag changes.
