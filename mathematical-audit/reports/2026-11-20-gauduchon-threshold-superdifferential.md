# Direct mathematical audit: Gauduchon threshold, minimizing faces and exact directional derivatives

**Date:** 2026-11-20. **Reviewed main:** b6933b772f41b45918f7e25ed1afbbb1fd892272.

**New finding:** POME-GAUD-THRESHOLD-DANSKIN-SUPERDIFFERENTIAL-001. Severity **low**; status **verified conditional deduction**, not an error in the printed results and not a transitive proof certificate.

## Precise integrated sources read

- docs/sections/gauduchon-metrics-and-linear-mass--compactness-and-duality-of-gauduchon-currents/index.html, main blob **31d17f258f2ff178bf52be3d3f92d5a995878d3a**: complete mathematical lines **5–76**. Proposition 11.7.1, source label **non-kahler-pluripotential-theory:C21ACA47**, permanent tag **155386134D9E**, lines 16–45; its (11.7.2) source/permanent **9C9E2FC6/7F6E8313B3F8** and (11.7.3) **84FCF311/EDF0C9D4A983**. Corollary 11.7.4, source/permanent **4B74203A/A97DA8CE2358**, lines 47–73.
- Selected upstream: docs/sections/gauduchon-metrics-and-linear-mass--the-gauduchon-criterion-for-positivity/index.html, blob **6dd43b62800206fb0302fd4261372d7882e5170d**, Theorem 11.6.1 lines 11–73, Corollary 11.6.2 (permanent **F83E15A1F529**) lines 82–97, Lemma 11.6.3 lines 105–126. Also docs/sections/gauduchon-metrics-and-linear-mass--conformal-gauduchon-metrics/index.html, blob **ecb4bf9e593dfb25f1644f0561d1aa65bf096b10**, Theorem 11.4.2 lines 20–56; §11.3 introductory connected/dimension context, line 7.
- No assertion of full upstream verification. The earlier torus minimizing-face/cusp example POME-GAUD-TORUS-SPECTRAL-FACE-CUSP-001 remains historical and is **not** recounted as a new finding.

## Claim

Let X be a compact **connected** complex n-fold, n at least two, and let omega be a fixed Hermitian form. Use the established compact convex set C_omega from Proposition 11.7.1: the weak closure of smooth strictly positive normalized dd^c-closed (n−1,n−1)-forms. For smooth real (1,1)-forms theta, eta, write

\[
\kappa(\theta)=\min_{T\in\mathscr C_\omega}\langle\theta,T\rangle,\qquad
F_\theta=\{T\in\mathscr C_\omega:\langle\theta,T\rangle=\kappa(\theta)\}.
\]

Here the pairing means integration of the wedge product. The minimizing set F_theta is a nonempty weakly compact convex **exposed face**. Both one-sided directional derivatives exist with the *exact* formulas

\[
\lim_{t\downarrow0}\frac{\kappa(\theta+t\eta)-\kappa(\theta)}t
 =\min_{T\in F_\theta}\langle\eta,T\rangle,\qquad
\lim_{t\uparrow0}\frac{\kappa(\theta+t\eta)-\kappa(\theta)}t
 =\max_{T\in F_\theta}\langle\eta,T\rangle.
\]

It follows that the following conditions are equivalent: (a) the minimizing current is unique, (b) the two directional slopes agree for **every** smooth real direction, (c) kappa is Gâteaux differentiable at theta, with derivative eta ↦ pairing(eta,T_theta). Moreover the **concave superdifferential** of kappa on the Fréchet space of smooth real (1,1)-forms, identified in its continuous dual, is **exactly F_theta**. No smoothness of the minimizing current is asserted; Gâteaux differentiability is not replaced by an unsupported stronger C^0-Fréchet differentiability claim.

## Complete argument, conditional on Proposition 11.7.1

Set K=C_omega, a(T)=pairing(theta,T), b(T)=pairing(eta,T), m=min_K a, F={a=m}. The printed proposition supplies nonempty weak compact convex K and continuity of a,b. For each t choose T_t attaining min_K(a+t b).

For t>0, evaluating at a member of F minimizing b gives
\[
\kappa(\theta+t\eta)-m\le t\min_F b.
\]
Since a(T_t)≥m, division by t gives
\[
\frac{\kappa(\theta+t\eta)-m}{t}\ge b(T_t).
\]
Also 0≤a(T_t)−m≤t(\min_F b−b(T_t))≤Ct, using boundedness of b on K. Consequently every weak cluster point of T_t as t↓0 is in F. Weak compactness (and the metrizability established in the printed proof on the fixed trace-mass family, if choosing sequences) yields liminf b(T_t)≥min_F b. Combining the two inequalities gives the first formula; no hidden exchange of nonlinear measure limits is used.

For t<0, evaluate at a member of F **maximizing** b. The negative denominator reverses the inequality, giving a quotient ≥max_F b. At a minimizing T_t, (a(T_t)−m)/t≤0, so that quotient is ≤b(T_t). Again a(T_t)→m and its cluster points lie in F, hence the limit is max_F b. This proves the second formula.

If F has distinct currents S and T, they are separated by some smooth real (1,1)-test form eta; hence min_F b<max_F b and the two slopes disagree. Conversely a singleton F gives the same continuous linear derivative in every direction, proving the Gâteaux equivalence.

Every T∈F is a supergradient because
\[
\kappa(\theta+h)\le\langle\theta+h,T\rangle
=\kappa(\theta)+\langle h,T\rangle.
\]
Conversely a continuous linear supergradient L obeys
\[
\min_{T\in F}\langle h,T\rangle\le L(h)
 \le\max_{T\in F}\langle h,T\rangle
\]
for each smooth direction h, by applying the supergradient inequality to positive and negative multiples and invoking the two derivative formulas. If L did not belong to the weakly compact convex set F, Hahn–Banach separation by evaluation on a smooth test form would contradict one of these inequalities. Thus the entire superdifferential equals F.

## Direct proof audit and scope limits

1. **Proposition 11.7.1, lines 16–45:** fixed trace mass controls coefficient measures, and positivity, dd^c-closedness and normalization pass to weak limits. The current topology on this bounded family is metrizable by a separable family of continuous coefficient tests; the printed sequential use in Corollary 11.7.4 is therefore justified. The separation step gives a smooth testing form and applies §11.6.2; it is a conditional dependency, not a false theorem.
2. **Corollary 11.7.4, lines 47–73:** taking infima of linear pairings gives concavity. Its order-unit Lipschitz constant 1 follows exactly from \(\int_X\omega\wedge T=1\). The printed cluster-minimizer conclusion is consistent with the stronger derivative formulas.
3. **External dependencies:** the proof of §11.6.2 uses the Lamari criterion in §11.6.1, and §11.4.2 uses elliptic Fredholm theory, a strong maximum principle and *connectedness* (explicit at §11.4 line 48). The present deduction assumes connected X. This review has not independently certified all these antecedents or the subsequent applications in Chapter 12. §11.7's final exceptional-curve and nefness references (§10.18.3 and §12.34.1) were not independently re-proved.
4. **Classification:** no newly confirmed false printed statement or standalone proof gap in the directly reviewed §11.7; the above is a **verified conditional deduction**. The optional source/body improvement is to insert the one-sided derivative and superdifferential formulas only through a separately reviewable proposed patch/PR, preserving all attributions, canonicalizations and permanent tags. Relevant dependent arguments concern perturbation of the Gauduchon threshold, uniqueness of weak minimizers, and convex duality.
5. **Excluded scope:** no Demailly approximation/regularization, dedicated Bergman, L², Ohsawa–Takegoshi, multiscale atlas, or positivity-loss programme was touched. Its old notes remain **deferred-by-user**, not resolved/certified.

**Exact coverage delta:** +1 complete **direct** section reading (§11.7, lines 5–76); selected prerequisite statement/proof reads in §§11.4 and 11.6; +0 full upstream-chain certifications; no historical first-visit claim. No builds, tests, CI, automatic publication, main changes, source-body edits or permanent-tag changes.
