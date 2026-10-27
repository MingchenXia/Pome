# Mathematical audit: finite-map trace descent, moving-measure limits, and compact-support de Rham duality

**Review date:** 28 October 2026 (Asia/Shanghai)  
**Pinned current main:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`  
**Initial audit branch HEAD:** \`d66ceeb98dac4938559f13344d8f996feba2376c\`  
**Audit scope:** new direct inspection of the indicated proofs of §5.43 and §10.73, and an incremental comparison with selected steps of §5.44. No complete section or dependent proof chain is certified. The user-excluded Demailly approximation/regularization and dedicated Bergman, L², Ohsawa–Takegoshi, multiscale-atlas, and positivity-loss proof-completion programme was not inspected; historic entries remain **deferred-by-user**.

## POME-CURVE-FINITE-TRACE-PSH-AVERAGE-001

**Severity:** low. **Status:** verified conditional deduction; **neither** a false printed theorem nor an integrated repair. **Proposal:** add an optional finite-curve-trace corollary after Lemma 5.43.16 without replacing the existing distinct maximum-descent lemma or changing its historical attribution.

**Integrated main:** \`docs/sections/plurisubharmonic-functions-and-singularities--pullback-and-descent/index.html\` (blob \`e5cccf608a51dd1629374fc68a1d3d7e6fd15958\`).
**Exact anchors and provenance:** §5.43.14 introductory finite-map conventions, physical lines 268–270; Lemma **5.43.15**, lines 274–299, source label \`non-kahler-pluripotential-theory:A483620D\`, permanent tag \`0018DC5A7DD0\`; weighted trace and pulled-back measures, lines 303–346; Lemma **5.43.16**, source \`non-kahler-pluripotential-theory:01A85B2E\`, permanent tag \`151A1D744DE7\`; relevant Lemma 5.43.8 (pullback Lelong number), lines 126–148, permanent tag \`11E6C3E4D36C\`. Section tag \`88AEFA5005B9\`.

**Exact statement and hypotheses.** Let \(r:C'\to C\) be a finite surjective holomorphic map of degree \(d>0\) between connected compact Riemann surfaces, with ramification indices \(e_x\), and let \(\beta\) be any smooth real \((1,1)\)-form on \(C\), \(\sigma=r^*\beta\). Suppose \(h\in\mathrm{PSH}(C',\sigma)\) is not identically \(-\infty\). Define the extended-valued normalized trace
\[
 A_rh(s)=\frac{1}{d}\sum_{r(x)=s}e_xh(x).
\]
There are no \(+\infty\) terms because \(h\) is quasi-psh. Then
\[
\boxed{\quad A_rh\in\mathrm{PSH}(C,\beta),\quad
\beta+dd^c A_rh=\frac1d\,r_*(\sigma+dd^ch),\quad
\nu(A_rh,s)=\frac1d\sum_{r(x)=s}\nu(h,x).\quad}
\]
Moreover \(A_r(v\circ r)=v\) for \(v\in\mathrm{PSH}(C,\beta)\), and \(A_r\) preserves pointwise order and additive constants. These are statements about \(\sigma=r^*\beta\), **not** arbitrary positive background forms on \(C'\). The pushforward on the right is the pushforward of a positive \((1,1)\)-current (a measure) with its usual, *unweighted* pushforward convention; its ramification has already been accounted for by the trace on potentials.

**Proof, including critical fibers and poles.** Work on a small disk \(V\subset C\) where \(\beta=dd^ca\), with \(a\) smooth. Then \(H=h+a\circ r\) is subharmonic on \(r^{-1}(V)\), and
\[
 A_rh+a=\frac1d\sum_{r(x)=s}e_xH(x).
\]
Off the finitely many branch values this is an ordinary finite sum of subharmonic functions composed with local inverse branches, and hence subharmonic. It is locally bounded above and extends subharmonically over the branch values. To identify that extension with the specified **ramification-weighted pointwise trace**, fix a branch point \(x\) of index \(e\), use \(t=z^e\), and set \(H_x(z)=H(z)\). The sum of \(H_x\) over the \(e\) inverse branches of \(t\) has the following exact mean on \(|t|=\delta\):
\[
 \frac{1}{2\pi}\int_0^{2\pi}\sum_{z^e=\delta e^{i\theta}}
   H_x(z)\,d\theta
 =e\,\frac{1}{2\pi}\int_0^{2\pi}
   H_x(\delta^{1/e}e^{i\phi})\,d\phi
 \longrightarrow eH_x(0).
\]
The final limit is the standard circular-mean convergence for subharmonic functions, including the case \(H_x(0)=-\infty\). Upper semicontinuity yields the matching upper bound for the trace's punctured-disk limit. Summing over the disjoint branch disks proves that the removable extension has the prescribed value at the branched fiber. In particular, its value is \(-\infty\) if **any** ramification-weighted summand is a pole. Hence the traced potential is globally \(\beta\)-psh and not identically \(-\infty\).

For the measure identity, in each unbranched disk the chain rule for \(dd^c\), tested against compactly supported functions, says that the Laplacian of the branch trace is the pushforward of \(dd^cH\). Both sides extend as positive measures across branch values. The equality including atoms follows equivalently by the local logarithmic-potential/Riesz representation used explicitly in the proof of Lemma 5.43.16 (main lines 335–341): \(dd^c\operatorname{Tr}_rH=r_*dd^cH\), without an extra ramification factor on the pushed-forward measure. Since
\(r_*(r^*\beta)=d\beta\) for a finite degree-\(d\) map, subtraction of \(a\) yields the displayed curvature identity. As \(dd^c h\) and \(\sigma+dd^ch\) have the same atoms, the point-mass formula for Lelong numbers on curves gives the last identity. Finally \(\sum_{r(x)=s}e_x=d\) proves \(A_r(v\circ r)=v\), order preservation, and equivariance under constants.

**Why the existing maximum descent must remain distinct.** Printed Lemma 5.43.15 defines \(m_h(s)=\max_{r(x)=s}h(x)\) and proves
\[
\nu(m_h,s)=\min_{r(x)=s}\frac{\nu(h,x)}{e_x}.
\]
The normalized trace has \(\nu(A_rh,s)=d^{-1}\sum_x\nu(h,x)\); generally these differ, and the exact pointwise inequality is \(A_rh\le m_h\), with strict inequality possible even at the level of pole sets. Thus it would be a **genuine semantic error** to deduplicate, canonicalize or substitute one construction for the other.

**Explicit non-equivalence on a ramified global map.** Take \(C=C'=\mathbb P^1\), \(r([X:Y])=[X^2:Y^2]\), \(d=2\), and let \(\beta=\omega_{\mathrm{FS}}\) with total mass one. Write
\[
 P(X,Y)=(X-Y)(X-2Y),\qquad
 h([X:Y])=\log\frac{|P(X,Y)|^2}{|X|^4+|Y|^4}.
\]
The quotient has projective degree zero and defines a global quasi-psh function with
\[
r^*\omega_{\mathrm{FS}}+dd^ch=[P=0]\geq0.
\]
Over \(s=[1:1]\), the two unramified preimages are \(x_+=[1:1]\) and \(x_-=[-1:1]\), with \(h(x_+)=-\infty\), \(h(x_-)>-\infty\), and respective Lelong numbers \(1,0\). Therefore \(A_rh(s)=-\infty\) and \(\nu(A_rh,s)=1/2\), whereas \(m_h(s)>-\infty\) and \(\nu(m_h,s)=0\). Both are nevertheless \(\beta\)-psh; neither printed lemma is disproved.

**Dependencies, limitations, and downstream relevance.** This uses only finite maps of compact smooth curves, the standard local Riesz/subharmonic calculus, and §5.43.16's finite-map trace/pullback conventions; no analytic regularization, \(L^2\) estimates, or global singularity resolution. The comparison applies to §5.43's finite-fiber descent and to later finite-factor maps such as the §18.24.3 selection discussion, **only** if those arguments really require fiber averages rather than maxima. No assertion about pushforward of higher-dimensional non-pluripolar products, arbitrary nonproper maps, or general complex-space fibers is made. Existing maximum and measure-pullback statements and their historical attribution should be preserved.

## Independent proof inspections without additional finding IDs

**§5.44, a historically covered section (increment, *not* first review).** Re-read Lemma 5.44.2, Lemma 5.44.5 and the measure-smoothing Lemma 5.44.12 in \`docs/sections/plurisubharmonic-functions-and-singularities--integration-against-non-pluripolar-measures/index.html\`, main blob \`15c449ab02d6f8df98edfa07f5286af7ac8e72d1\`, lines 9–31, 48–87, 203–264; stable tags \`983B3E6349BB\`, \`D260E972F57C\`, \`88E063207C1B\` (the former tag is read from the integrated section). Checked the polarity of the submean inequality in lines 233–239 and the order of moving radii versus tail envelopes in lines 241–255: no new false statement identified. The fixed-measure Cegrell convergence lemma and the full smooth-to-bounded torsion calculus remain *conditional upstream inputs*, not certified. The historical §5.44.5 capacity-modulus and slowly decaying non-pluripolar examples \`POME-CAP-DOM-EXP-MODULUS-001\` and \`POME-NONPOLAR-SLOW-EXP-001\` are **not** re-registered. No dedicated Demailly approximation proof was entered.

**§10.73, first selected proof inspection; a separate cohomological branch.** Theorem 10.73.1, source \`demailly-complex-geometry:4380D9A9\`, permanent tag \`7ECFE434A83A\`, \`docs/sections/spectral-sequences-support-and-cup-products--the-trace-in-de-rham-cohomology/index.html\`, blob \`1e9f8a101aedc20796ea0c47caa03f452e2c6b9a\`, physical lines 7–44. Selected steps: finite-support difference-cochain calculation on the oriented line (lines 21–29), partition-of-unity trace sign (31–39), compact-support Stokes and top integration (41), and dependence on the algebraic Ext-vanishing / Poincaré duality statement of §§10.68/10.72 (43). In the line model, \(\oplus_{k\in\mathbb Z}\mathbb R \xrightarrow{\Delta} \oplus_{k\in\mathbb Z}\mathbb R\) has injective \(\Delta\), with image the finite sequences of total sum zero, so its cokernel is \(\mathbb R\) as claimed. For a countable disjoint union \(X=\coprod_{j\geq1}\mathbb R\), the theorem correctly predicts \(H_c^1(X,\mathbb R)=\bigoplus_j\mathbb R\) and \(H^0(X,\mathbb R)=\prod_j\mathbb R\), which **is** the full algebraic dual, not a finite direct sum. No independent verification of all Godement-dualizing-complex and Ext prerequisites; no whole-section certification, and no new definite defect found. This ordinary de Rham topic is unrelated to the user-excluded dedicated Demailly approximation programme, notwithstanding historical provenance of the source.

## Coverage and disposition

- **Newly upgraded from current inventory-only:** selected passages of **§5.43** (5.43.4–.5, .7–.8, .13, .15–.16 with focus on finite trace) and **§10.73** (the one theorem and its sign/finite-support argument). **§5.44** receives an incremental comparison only and was already partly reviewed on 24–25 October.
- **One new stable finding** \`POME-CURVE-FINITE-TRACE-PSH-AVERAGE-001\`: low / verified conditional deduction; original results remain correct; proposal is optional explanatory corollary, not an integrated edit.
- **747** unique current numbered section records remain in the coverage matrix, with **zero** whole-section or full-project mathematical certifications. All earlier confirmed errors, proof gaps, unresolved external inputs and **deferred-by-user** items preserve their previous status.
- **No** changes to \`main\`, mathematical bodies, registries, canonical entries, source repositories, published websites, permanent tags, CI, builds or formalizations. No project-wide test or build was run.
