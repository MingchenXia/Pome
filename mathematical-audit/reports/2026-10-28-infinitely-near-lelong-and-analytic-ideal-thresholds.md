# Mathematical audit — 28 October 2026: infinitely near Lelong numbers and analytic-ideal thresholds

**Reviewed production `main`:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. **Review branch starting HEAD:** `74ed8e9ada205ba2f214facc675dcd52c2a87669`. This is a selected-passage check of the **integrated reading edition**. The two findings are **low / verified conditional deduction** (independent examples); neither says that a printed theorem is false. Existing proofs of global coherence, strong openness, multiplier-ideal restriction, Demailly approximation/regularization, Bergman, weighted L², Ohsawa–Takegoshi, multiscale atlases, and positivity-loss completion were **not** reopened or certified.

## Exact integrated passages and provenance

- `docs/sections/plurisubharmonic-functions--lelong-numbers-and-multiplier-ideal-sheaves/index.html`, blob `2315574feb57cd6bf57c3d64e4221da2eabc3cc9`: Definition **5.16.11**, source entry `sgpt-AF4A6BE6` (source tag `AF4A6BE6`), permanent reader tag `E9EA7799080C`, physical lines **137–145**; Remark **5.16.12**, source `sgpt-277B8867`, reader tag `4E2D4F8663A3`, lines **148–153**; Lemma **5.16.17**, source `sgpt-B8094988`, tag `C85C2748AE0B`, statement **189–193**, inserted proof **194–196**. The project's `dd^c=i\partial\bar\partial/(2\pi)` convention is used, so `\nu(\log|z|^2,0)=1`.
- `docs/sections/plurisubharmonic-functions--analytic-singularities/index.html`, blob `877d567c35ff3e75a0c1c874be251d75bf9f4927`: Definition **5.18.11**, source `sgpt-133FCD5C`, permanent tag `99446B95B55B`, physical lines **124–126**; Lemma **5.18.12**, source `sgpt-FA864488`, reader tag `D9F25876A735`, statement **129–131**, local-resolution formula **133–155**. Its compactness hypothesis is not inferred for the local example below.

## POME-LELONG-INFINITELY-NEAR-JUMP-001

**Severity / status:** low / **verified conditional deduction**. The original Definition 5.16.11 and Lemma 5.16.17 are correct. **Affected:** interpretation of infinitely near divisorial valuations, first-blowup point Lelong identities, any canonicalization comparing divisors only by their image in the original space. **Action:** optional explanatory counterexample; preserve both valuations, their source tags and the original lemma.

On a neighborhood of `0\in\mathbb C^2` set
\[
\varphi(x,y)=\log(|x|^2+|y|^4).
\]
It is psh and has \(\nu(\varphi,0)=1\), since the supremum on a small Euclidean ball is \(\log(r^2+O(r^4))\).

Blow up the origin. In the chart \(y=t,\ x=tw\),
\[
\varphi\circ\pi_1=\log|t|^2+\log(|w|^2+|t|^2).
\]
At the generic point of the first exceptional divisor \(E_1=\{t=0\}\), the second term is locally bounded; hence \(\nu(\varphi,E_1)=1\). At the point \((t,w)=(0,0)\), however, the Lelong number of the pullback is \(2\), the sum of the logarithmic coefficient \(1\) and that of \(\log(|w|^2+|t|^2)\). Blow up this point. In its chart \(t=s,\ w=sz\),
\[
\varphi\circ\pi_1\circ\pi_2
=2\log|s|^2+\log(1+|z|^2).
\]
Thus the new exceptional prime \(E_2\) has \(\nu(\varphi,E_2)=2\). Both divisors lie over \(0\), but they define distinct valuations and have distinct generic Lelong numbers:
\[
\nu(\varphi,0)=\nu(\varphi,E_1)=1,\qquad
\nu(\varphi,E_2)=2.
\]
This does **not** contradict the first-blowup lemma, which refers to \(E_1\), or model independence for a **fixed** divisorial valuation.

**Separate proof-interface check:** physical line 142 of Definition 5.16.11 cites Siu semicontinuity for model independence. Siu provides well-defined generic values, but the cross-model comparison additionally uses a smooth common dominating model and the fact that its maps are biholomorphic near the generic points of the strict transforms of one fixed divisorial valuation. Pullbacks agree on that common model and local biholomorphic invariance identifies the generic Lelong numbers. Such a common-model existence is standard resolution/principalization (the permitted Hironaka input); the missing intermediate sentence is a **proposed clarification, not evidence of a false definition**. No global valuative criterion or excluded analytic proof is asserted.

## POME-ANALYTIC-IINF-MULTIPLIER-GAP-001

**Severity / status:** low / **verified conditional deduction**. Definition 5.18.11 and its inclusion \(\mathcal I_\infty\subset\mathcal I\) are correct and the inclusion can be strict even for a simple finite-generated analytic singularity. **Affected:** identification of \(\mathcal I_\infty\) with multiplier ideals, local singularity/ideal canonicalization and the separate rounded asymptotics of §5.18.13. **Action:** optional two-dimensional model distinguishing the ideals; do not merge them or modify a permanence tag.

Take \(X\) to be a bidisc near the origin, and put
\[
\psi(x,y)=\log(|x|^4+|y|^6).
\]
This is a local psh weight with analytic singularities from \((x^2,y^3)\). For every pair of nonnegative integers \((a,b)\), the germ \(x^ay^b\) is in the ordinary multiplier ideal iff
\[
\frac{a+1}{2}+\frac{b+1}{3}>1.
\tag{A}
\]
Indeed, use radial coordinates \(r=|x|,s=|y|\), followed by \(R=r^2,S=s^3\). Up to nonzero constants the weighted integral is
\[
\iint_{R,S\ge0}
\frac{R^{a}S^{2(b+1)/3-1}}{R^2+S^2}\,dR\,dS.
\]
In polar coordinates \((R,S)=\rho(\cos\theta,\sin\theta)\), its radial factor is \(\rho^{(a+1)+2(b+1)/3-3}\,d\rho\); the angular beta integral is finite because both exponents are positive. It converges precisely under (A). Distinct monomials are orthogonal after angular integration; thus the monomial criterion controls every holomorphic germ, rather than only monomials. In particular the constant fails (A), while both \(x\) and \(y\) satisfy it:
\[
\mathcal I(\psi)_0=(x,y).
\]

On the other hand, by the exact pointwise definition of \(\mathcal I_\infty\),
\[
x^a y^b\in\mathcal I_\infty(\psi)_0
\quad\Longleftrightarrow\quad
\frac a2+\frac b3\ge1.
\tag{B}
\]
For necessity restrict to \(|x|^2=|y|^3=\rho\to0\); for sufficiency set \(R=|x|^2,S=|y|^3\) and use \(R^{a}S^{2b/3}\le (R^2+S^2)^{a/2+b/3}\le C(R^2+S^2)\) locally when the sum of exponents is at least one. For a general holomorphic germ, apply Cauchy's coefficient estimate on the distinguished tori \(|x|=\rho^{1/2}, |y|=\rho^{1/3}\) to rule out every Taylor monomial violating (B). The allowed monomials form the finitely generated ideal
\[
\mathcal I_\infty(\psi)_0=(x^2,xy^2,y^3)
\quad\subsetneq\quad (x,y)=\mathcal I(\psi)_0.
\]
This example does not rely on the global coherence proof's log resolution, strong openness, Briançon–Skoda, OT, or the user-excluded approximation machinery. The result compares the **local germs** of the definitions, not a new assertion about global compactness.

## Scope and outstanding dependencies

The two previously inventory-only ToC rows **§§5.16 and 5.18** were directly inspected at the specified nonexcluded lines and updated to **selected-passage coverage only**. In §5.16 we did **not** certify Siu's theorem, general multiplier-ideal coherence, subadditivity, the global valuative criterion, strong openness, the smooth-morphism multiplier formula, or its OT-based restriction theorem. In §5.18 we did **not** review approximation §5.18.9–10 or their prerequisites, nor the quoted analytic extension theorem §5.18.16. The full historical **747** unique numbered sections and **zero** whole-section certifications are unchanged. The entire Demailly regularization/approximation plus dedicated Bergman/weighted-L²/OT/multiscale/positivity-loss proof completion remains **deferred-by-user**, neither resolved nor certified. No project build, test, CI, website publication, source/body/registry, permanent-tag, main, or formalization changes.
