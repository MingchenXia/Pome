# 2026-10-25 — ideal-obstacle concavity, projection reference-kind correction, and separated-product audit

**Pinned source:** \`MingchenXia/Pome\` \`main\` at \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`.
**Starting audit branch:** \`1689f9475b9a125be4606f0b8ce46fa49aae6b27\`.
**Checkpoint (UTC):** 2026-10-25T11:02:14.702Z.
**Scope:** new selected proof inspection in §§18.4, 18.16, 18.25; a narrow dependency reread in §18.12.2 and §§5.37.3–4, 5.43.18, 5.43.24. No whole section or upstream analytic chain is certified.

**Explicit user exclusion:** Demailly approximation/regularization, its dedicated Bergman, L², Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof-completion programme were **not** reopened. Pre-existing items there remain **deferred-by-user**, not repaired or certified. The §18.7 analytic-approximation chain and §§18.28–18.47 partial-kernel chain are outside this run.

## POME-IDEAL-PROJECTION-REFERENCE-KIND-001 — confirmed error (reference kind only), low

**Location.** \`docs/sections/multiplier-ideal-envelopes-and-goodness--ideal-projection/index.html\`, blob \`f1979b73c857f4874dd4a5cb10b93bcc047ebbdc\`, lines **99–106**, Corollary 18.4.5, stable permanent tag \`B853F2E6C70B\`. The actual source is **Proposition** 18.4.4, tag \`2506B7AD6F19\`, lines **69–91** of the same file.

**Precisely confirmed defect.** The first sentence of the proof of Corollary 18.4.5 says "by the last identity in **corollary 18.4.4**". There is no Corollary 18.4.4: the cited last identity is in **Proposition 18.4.4**,
\[
 P_\theta[P_\theta[u]_{\mathcal I}]=P_\theta[u]_{\mathcal I}.
\]
The subsequent finite extended-mass conclusion invokes Proposition 16.28.7 for ordinary envelope fixed points.

**Correction proposed:** replace *corollary 18.4.4* by *Proposition 18.4.4* in that proof sentence. This is a precise editorial cross-reference-kind error, **not** a counterexample to Corollary 18.4.5, **not** a missing mathematical implication, and **not** a change to the permanent tag. Affected dependent: reading-edition proof metadata/citation accuracy for 18.4.5; no further mathematical dependent is presently shown to fail. **No source/registry/canonical text changed in this audit branch.**

## POME-IDEAL-OBSTACLE-CONCAVITY-001 — verified conditional deduction, low

**Precise sources.** §18.4 Theorem 18.4.2, tag \`7F20FD198864\`, blob \`f1979b73c857f4874dd4a5cb10b93bcc047ebbdc\`, lines 22–50; §18.12 Proposition 18.12.2, tag \`84E9AB1A05B4\`, \`docs/sections/multiplier-ideal-envelopes-and-goodness--a-topology-on-ordinary-singularity-types--all-smooth-obstacles/index.html\`, blob \`6bfe360706d85c21e83b0212de472de716d8c04c\`, lines 45–70; the all-modifications Lelong/ideal criterion in §5.37.3, \`docs/sections/plurisubharmonic-functions-and-singularities--multiplier-ideals-and-logarithmic-poles/index.html\`, blob \`9256668b88735f821d06b0919466a6a8cba777ed\`, lines 55–74. The explicit comparison of obstacles in §18.12.1, tag \`DAA4A0418197\`, gives an L¹ bound; the following establishes pointwise concavity and the sharp sup-norm statement.

**Statement.** Let \`X\` be connected compact complex, \(\theta\) any smooth real (1,1)-form and \(u\in\mathrm{PSH}(X,\theta)\). For smooth real obstacles \(F,G\), write
\[
 Q_F=P_{\theta,F}[u]_{\mathcal I},\qquad Q_G=P_{\theta,G}[u]_{\mathcal I}.
\]
For every \(s\in[0,1]\), with \(H=(1-s)F+sG\),
\[
 \boxed{(1-s)Q_F+sQ_G\leq P_{\theta,H}[u]_{\mathcal I}.}
 \tag{A}
\]
Moreover,
\[
 \boxed{\|Q_F-Q_G\|_{L^\infty(X)}\leq\|F-G\|_{L^\infty(X)}.}
 \tag{B}
\]
The constant 1 is optimal: equality holds for every constant translation \(G=F+c\). Consequently \(F_i\to F\) uniformly along an **arbitrary directed net** of smooth obstacles implies \(P_{\theta,F_i}[u]_{\mathcal I}\to P_{\theta,F}[u]_{\mathcal I}\) uniformly (without subsequences or any interchange of limits).

**Proof of (A).** Proposition 18.12.2 gives \(Q_F,Q_G\in\mathrm{PSH}(X,\theta)\), \(Q_F\leq F\), \(Q_G\leq G\), and \(Q_F\sim_{\mathcal I}u\sim_{\mathcal I}Q_G\). Their convex combination \(Q_s\) has curvature
\[
 \theta+dd^c Q_s=(1-s)(\theta+dd^cQ_F)+s(\theta+dd^cQ_G)\geq0
\]
and lies below \(H\). For every local modification \(\pi\) with smooth source and every \(y\) on it, linearity of Lelong numbers under positive linear combinations gives
\[
 \nu(Q_s\circ\pi,y)
 =(1-s)\nu(Q_F\circ\pi,y)+s\nu(Q_G\circ\pi,y)
 =\nu(u\circ\pi,y).
\]
The all-modifications criterion in Theorem 5.37.3 implies \(Q_s\sim_{\mathcal I}u\); thus \(Q_s\) is an **actual ideal competitor** below \(H\). The envelope dominates it. The endpoints \(s=0,1\) are immediate. This uses no analytic approximation.

**Proof of (B) and optimality.** For \(F\leq G\), inclusion of competitor families gives \(Q_F\leq Q_G\). Addition of a constant \(c\) bijects the competitor families below \(F\) and \(F+c\) because bounded shifts preserve multiplier ideals; hence \(Q_{F+c}=Q_F+c\). Put \(\delta=\|F-G\|_\infty\) and sandwich \(F-\delta\leq G\leq F+\delta\). The preceding facts yield \(Q_F-\delta\leq Q_G\leq Q_F+\delta\). With \(G=F+c\) this is equality, hence the constant is sharp. The directed-net assertion follows from the bound itself, using no sequential compactness.

**Separated-product consequence and boundary.** For §18.16.2, tag \`9E5A9E7C5770\`, Eq. 18.16.3 tag \`F57341993FE4\`, \`docs/sections/multiplier-ideal-envelopes-and-goodness--a-topology-on-ordinary-singularity-types--several-curve-factors/index.html\`, blob \`93e080ea9c15c5ec03b28c2ec51eb469c769603b\`, lines 55–115, the already printed tensorization identity gives for two families of separated obstacles \(F_i,G_i\)
\[
 \left\|P_{\gamma,\sum_iF_i\circ\pi_i}[u]_{\mathcal I}
       -P_{\gamma,\sum_iG_i\circ\pi_i}[u]_{\mathcal I}\right\|_\infty
 \leq\sum_i\|F_i-G_i\|_\infty.
\]
The same proof shows joint concavity under coordinatewise interpolation. This is **conditional on the existing tensorization theorem**, not a certification of all of its Green-potential inputs. Formula (A) itself applies to arbitrary smooth (not necessarily separated) obstacles; the exact tensorization formula is **not** claimed for mixed obstacles.

**Suggested action:** an optional short corollary after Proposition 18.12.2, with the stronger \(C^0\) modulus and concavity. No revision of the existing proposition is needed. Affected dependents: obstacle-coordinate comparison (§18.12), separated-curve products (§18.16), and any use of arbitrary directed families of obstacles.

## Other directly inspected integrated proofs (no new error asserted)

**§18.4, first selected review.** Read Theorem 18.4.2 (ideal projection is an actual competitor and idempotent), Proposition 18.4.3 (commutation with modification), Proposition 18.4.4 (ordinary/ideal envelope order), Corollary 18.4.5, Proposition 18.4.6 (order/scaling/subadditivity), and Proposition 18.4.8 / Corollary 18.4.9 (analytic/divisorial types), at lines 22–170 of the above pinned HTML. Narrowly compared the exact pullback and class-descent statements with Proposition 5.43.18, tag \`A7090F92CA39\`, and Lemma 5.43.24, tag \`83C3A394E5BB\`, \`docs/sections/plurisubharmonic-functions-and-singularities--pullback-and-descent/index.html\`, blob \`e5cccf608a51dd1629374fc68a1d3d7e6fd15958\`, lines 352–372 and 509–520. This does not reprove the entire valuative criterion or its analytic prerequisites.

**§18.16, first selected review.** Read Lemma 18.16.1, tag \`D9950FF0BE1C\` (lines 23–51); Proposition 18.16.2, tag \`9E5A9E7C5770\` (lines 62–115); Proposition 18.16.5, tag \`B61109A06541\` (lines 139–158); and Corollary 18.16.6, tag \`A5CCF14B62D6\` (lines 175–206). Explicitly checked the potentially delicate induction step in Proposition 18.16.2: the partial supremum \(a(t)=\bigl(\sup_{y'}[v(y',t)-F'(y')]\bigr)^*\leq e_m(t)\) is the **necessary** reason for \(v(\cdot,t)-e_m(t)\leq F'\); the simpler bound \(e_m\leq F_m\) alone would **not** imply this. The text has the required \(a\leq e_m\) comparison, so **no gap is charged**. The zero-area curve case uses the harmonic gauge; the finite sum of polar total variations and the \(\Theta_0\) non-bigness proof pass their degree check: \(T=(\bigwedge_i\pi_i^*\eta_i)\wedge\kappa^k\) has bidegree \((n-1,n-1)\), is closed, \(\Theta_0\wedge T=0\), and the auxiliary curve term has positive pairing. Curve Green and polar-metric classification inputs remain conditional.

**§18.25, first selected review.** Read complete Example 18.25.1, tag \`6CA9B76E77A0\`, \`docs/sections/multiplier-ideal-envelopes-and-goodness--a-topology-on-ordinary-singularity-types--hopf-surface-fibers-and-unbounded-ambient-mass/index.html\`, blob \`23b0b6d65db6f0e3119cca84a69006c215243902\`, lines 11–66. Checked the local incidence equations \(tz_0=sz_1\) for the blowup of \((z_0,z_1)\), the quotient by scalar contraction, degree-one change of variables and the nonnegative mixed-wedge inequality \((A+B)^3\geq B^3\) when \(A>0,B\geq0\). The unbounded-mass conclusion **depends on** the previously established Hopf mass construction in §23.1.1 and its bounded-mass criterion, not independently re-proved here. The rank-one curve model assertions depend on §§18.22.1–3. No counterexample to the printed example was found.

**Remaining work:** individual verification of upstream §5.37.3 and the Green/curve metric results, the analytic hypotheses of §23.1.1, and all other unreviewed sections. The two findings above are not a certification of any chapter, source, proof registry, or transitive proof chain. No tests, build, CI, website publication, formal verification or merge performed.
