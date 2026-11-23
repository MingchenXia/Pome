# Classical current products: sharp support obstruction; b-divisor volume and net order — 2026-11-23

## Baselines, actual reading, and exclusions

Current production main: **b6933b772f41b45918f7e25ed1afbbb1fd892272**. Pre-review branch HEAD: **2854fc03cc4ce34149dba35b8f1ba64d81b70b74**. The integrated reading edition was inspected, not a source-book theorem inferred from a matching number. All locations below are *physical HTML source lines*, distinct from generated reader paragraph numbers.

- **Complete direct §7.28**, [integrated text](../../docs/sections/classical-products-with-controlled-unbounded-loci/index.html), main blob **21dc39a9b02a4c1820f081a0c3a82e9f8ffca727**, mathematical lines **5–67**. Theorem 7.28.1: source **demailly-complex-geometry:F96C3380**, permanent **1BBBF8109419**, statement lines 6–10, recursive and weighted continuity proof lines 13–67.
- **Complete direct §7.30**, [integrated text](../../docs/sections/classical-products-with-controlled-unbounded-loci--classical-products-under-hausdorff-intersection-conditions/index.html), blob **9cde5bfdeb2e3c0457216278945df46eb230e42b**, mathematical lines **10–154**. Lemma 7.30.1 source **demailly-complex-geometry:3D4DAD02**, permanent **162A0666C4BB**, lines 10–25; Proposition 7.30.3 source **demailly-complex-geometry:A5207F44**, permanent **1AC7DC75B159**, lines 29–89; its nullness Eq. 7.30.4 permanent **E561BB270A1B**, lines 30–34; localization Eq. 7.30.7 permanent **AC44B2B308D3**, lines 62–69.
- **Selected, not entire §7.29**: [integrated text](../../docs/sections/classical-products-with-controlled-unbounded-loci--classical-products-with-compact-unbounded-loci/index.html), blob **65666651048e9ada933a763b7d381766f8b43965**. Lemma 7.29.1, source **demailly-complex-geometry:828A36D4**, permanent **438B9224299E**, lines 10–43; Theorem 7.29.5, source **demailly-complex-geometry:B0311B48**, permanent **8FBB0E4DE397**, lines 46–133; Lemma 7.29.6 statement and sphere-band argument, lines 137–154 only. Previous §7.29 audit findings remain prior work, not new discovery.
- **Selected, not entire §7.31**: [integrated text](../../docs/sections/classical-products-with-controlled-unbounded-loci--collars-relative-to-the-support-of-the-base-current/index.html), blob **86de377d6e6f17fc1a08a6e789a681ddfaabfac5**, Corollary 7.31.4 source **demailly-complex-geometry:4876F9E5**, permanent **EBA900FA96EF**, physical lines **69–84**; Theorem 7.31.2 statement and collar qualifications, lines 27–50. The regularization lemma 7.31.1 was NOT independently audited.
- **Selected, not entire §20.1**, [integrated text](../../docs/sections/the-theory-of-b-divisors/index.html), blob **4a793dfd462badcb351f54a36cb030cde14a399b**, Lemma 20.1.7 source **sgpt:54FCB4C1**, permanent **F5B2C1F1E318**, lines 66–99; Example 20.1.9 source **sgpt:048A0D73**, permanent **7AF528B0FB3B**, lines 100–126; Theorem 20.1.15 source **sgpt:A0644B2C**, permanent **6EB1B4E1D222**, *only* volume argument in Step 3, lines **209–259**, including Eq. 20.1.17 permanent **35EFEAF9683D** and Eq. 20.1.18 permanent **725B7EF61286**. Its dedicated Demailly approximation mechanism was expressly NOT examined.

## POME-BT-SUPPORT-DIMENSION-COEFFICIENT-BREAKDOWN-001

**Classification:** low / **verified conditional deduction (sharpness example)**, not a false printed theorem, repair, or upstream proof certification.

**Hypotheses and exact model.** Fix integers \(1\le p<n\), a coordinate ball \(B\subset\mathbb C^n\), the smooth \(p\)-plane \(Y=B\cap\{z_{p+1}=\cdots=z_n=0\}\), and the integration current \(T=[Y]\), closed positive of bidimension \((p,p)\). Define the psh function \(u=\log|z_{p+1}|\), with \(u=-\infty\) on \(Y\). Its unbounded locus \(L(u)=B\cap\{z_{p+1}=0\}\) has analytic intersection \(L(u)\cap\operatorname{supp}T=Y\), of complex dimension **exactly \(p\)**.

**Exact obstruction and rate.** For \(M>0\), the bounded psh truncation \(u_M=\max(u,-M)\) restricts to the constant \(-M\) on \(Y\). Thus, for every nonnegative compactly supported test form \(\eta\) of complementary degree with \(\langle T,\eta\rangle>0\),
\[
\langle -u_MT,\eta\rangle=M\langle T,\eta\rangle\longrightarrow+\infty.
\]
Consequently \(uT\) is **not** coefficient-integrable on any open set intersecting \(Y\), and the recursive *classical* current \(dd^c(uT)\) is undefined. The obstruction is exact, not just an unspecified failure of a mass estimate.

At the same time \(u_MT=-MT\) as currents and \(dd^cT=0\), so
\[
dd^c(u_MT)=0\qquad\text{for every }M,\quad\text{hence }dd^c(u_MT)\rightharpoonup0.
\]
**Convergence of unweighted truncated Hessian currents does not imply existence of their coefficient-integrable classical recursive product.** In particular, a zero limiting current here is not proof that \(dd^c(uT)\) was classically defined. No claim about all possible alternative products is made.

Corollary 7.31.4 (permanent EBA900FA96EF, lines 69–84) imposes analytic dimension at most \(p-1\) for automatic coefficient integrability of \(uT\). This model proves that replacing \(p-1\) by \(p\) is impossible for arbitrary positive bidimension-\(p\) base currents when \(p<n\). It does **not** say the hypothesis is necessary for each individual current/potential, nor does it assert the \(p=n\) case has the same obstruction: for \(T=1\), ordinary psh functions are locally Lebesgue integrable.

**Disposition / dependents:** no change to the correct stated Corollary 7.31.4 or Theorem 7.28.1. Propose an optional sharpness remark distinguishing coefficient integrability and distributional limits after §7.31.4; relevant to recursive classical BT products in §§7.28–7.31 and comparisons with non-pluripolar products. Original tags and historical attribution remain untouched.

## POME-BDIV-REGULARIZATION-NET-VOLUME-ORDER-001

**Classification:** medium / **candidate proof gap and unverified external dependency**, NOT a confirmed false theorem and NOT a certified repair.

**Precise logical issue, outside the excluded programme.** Lemma 20.1.7 (lines 66–99, permanent F5B2C1F1E318) proves only
\[
\limsup_i\operatorname{vol}\mathbb D_i\le\operatorname{vol}\mathbb D
\]
for arbitrary coordinatewise-convergent pseudo-effective b-divisor **nets**. It establishes equality for **decreasing** nets. Example 20.1.9 (lines 100–126) explicitly supplies nef Cartier b-divisors with the *same root* on \(\mathbb P^2\), coordinatewise converging to the Cartier b-divisor of \(H\), yet their volumes are identically zero while the limit volume is one. Hence neither convergence, nefness, nor a fixed root alone imply continuity.

In the proof of Theorem 20.1.15 (lines 209–259, especially lines 251–259), after establishing \(\mathbb D(T_j)\to\mathbb D(T)\), the text invokes Lemma 20.1.7 for the equality
\[
\operatorname{vol}\mathbb D(T)
=\lim_j\operatorname{vol}\mathbb D(T_j).
\]
The displayed passage does **not itself identify a decreasing-order premise** for these b-divisors. The previous bound \(a_E^j\le a_E\) only compares each approximant against the limit; it does **not** by itself compare \(a_E^j\) with \(a_E^{j+1}\). This is a missing **documented inference**, not a counterexample to the theorem: the invoked approximation result may impose stronger order information, which is in the expressly excluded Demailly-regularization scope and was not reopened.

**Verified sufficient conditional repair (not an unconditional theorem repair).** It is enough to establish that the approximating psh potentials \(\varphi_j\) are decreasing **in singularity order**: for every \(j\), \(\varphi_j\ge\varphi_{j+1}+O(1)\) locally (the stronger condition \(\varphi_j\downarrow\varphi\) also suffices). For any fixed modification \(\pi:Y\to X\) and prime divisor \(E\subset Y\), order of local potentials gives
\[
\nu_E(\pi^*T_j)\le\nu_E(\pi^*T_{j+1}).
\]
Their total cohomology classes on \(Y\) are the same, so Siu decomposition gives
\[
\{\operatorname{Reg}\pi^*T_j\}
-\{\operatorname{Reg}\pi^*T_{j+1}\}
=\sum_E\bigl(\nu_E(\pi^*T_{j+1})-\nu_E(\pi^*T_j)\bigr)\{E\}\ \succeq0.
\]
The sum is an effective divisorial current (interpreted as a convergent positive current, not an unjustified absolute sum of class coordinates). Thus \(\mathbb D(T_j)\) is decreasing in the b-divisor pseudo-effective order on **every model**. Together with already-established coordinatewise convergence, precisely the *decreasing-net* part of Lemma 20.1.7 yields the desired equality. This verification does not establish that the actual \(T_j\) used in Theorem 20.1.15 satisfy that sufficient hypothesis.

**Next nonexcluded editorial step:** insert an explicit reference or proof that this actual approximating family is order-monotone (or state another continuity theorem with its exact hypotheses) immediately before the volume equality. If the excluded approximation result supplies such monotonicity, update classification to verified conditional repair after an authorized future audit; otherwise retain a genuine proof gap. Affected dependents: volume equality in Theorem 20.1.15 and later uses of that b-divisor/current identification, including §§20.1.24–27. Nothing is changed in production main.

## Other direct mathematical checks and limits

For §7.30, the square identity for the cutoff commutator \(B_\chi(v)=dd^c(\chi v)-\chi dd^cv\) (Eq. 7.30.2, permanent DBD412CA248A, lines 17–25) is algebraically correct. For nonnegative bounded psh \(v,\chi\), the squares \(v^2,(v+\chi)^2,\chi^2\) are psh by convex increasing composition. The general smooth \(\chi\) is a difference of nonnegative smooth psh functions locally. This controls derivative terms by bounded-product estimates without assuming the full classical product for singular slots at the start.

The Hausdorff threshold in Proposition 7.30.3 uses all \(m\)-fold intersections, not merely the full \(q\)-fold intersection. The projection cylinder and compact support step are at lines 62–88; proof of weighted continuity in §7.28 uses induction on total slots and on locally unbounded slots (lines 16–66). These dependencies were directly read, but their entire transitive chains—including the finite-cover smooth regularization and all bounded Bedford–Taylor hypotheses—are **not certified**. The earlier sharp radial threshold result for §7.29.5 remains a distinct historical finding; it is not recounted here.

**Actual counts:** 2 entirely directly read current sections (§§7.28, 7.30); selected mathematical passages in 3 other sections (§§7.29, 7.31, 20.1); 1 verified sharpness deduction, 1 unresolved medium candidate/dependency, 0 new confirmed false printed statements, 0 complete upstream proof-chain certifications. Historic first visits remain unreconciled. All **747 numbered section records** are preserved.

**Scope gate:** Demailly approximation/regularization and its Bergman, \(L^2\), Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof-completion programmes are **deferred-by-user**, not certified or examined. No CI, builds, project tests, source/registry/canonicalization/tag edits, main changes, merges, or website publication.