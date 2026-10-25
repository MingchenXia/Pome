# Hyperplane saturation of the relative-envelope mass bound; an additional projection-reference mismatch

**Date:** 2026-10-26 (Asia/Shanghai).  
**Reviewed Pome \`main\`:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`.  
**Pre-review audit branch head:** \`32d74a53c3a62797d733d8fdb4a75ba4da90e3ec\`.  
**Scope:** New selected proof-level coverage in §§16.28 and 16.29. No complete section or upstream dependency chain is certified.

## Exact integrated sources

1. \`docs/sections/envelopes-and-volumes-of-singularities/index.html\`, blob \`0bdddc04cbc0cefd05591fdffc0796f3405b2a69\`. New direct inspection concentrated on Lemma **16.28.68** (source label \`non-kahler-pluripotential-theory-415491B2\`, tag \`F644817639FD\`, lines **1225–1245**), Lemma **16.28.69** (source \`non-kahler-pluripotential-theory-94A16878\`, tag \`18D2E34A9D42\`, lines **1246–1267**), and Theorem **16.28.70** (source \`non-kahler-pluripotential-theory-4BB7FC4C\`, tag \`0EA7F76611B5\`, lines **1268–1293**). The section assumes a smooth **semipositive and big** background \(\theta\).
2. \`docs/sections/envelope-systems-over-hermitian-perturbations/index.html\`, blob \`856e240bbc5c86058ff861873f11e87db021e1bd\`. Selected statements/proofs: Proposition **16.29.3** (source \`non-kahler-pluripotential-theory-C6135113\`, tag \`160B15BF08FE\`, lines **50–68**), Proposition **16.29.5** (tag \`7DD8E9433762\`, lines **74–101**), Theorem **16.29.9** (tag \`E94DE568F212\`, lines **134–190**), Proposition **16.29.13** (tag \`5B2E6F75BA98\`, lines **221–248**), Lemma **16.29.16** (tag \`F6C7CDB99C6E\`, lines **283–359**), Theorem **16.29.17** and Proposition **16.29.18** (tags \`761E4875D2B4\`, \`7F133849FE58\`, lines **367–430**), and Proposition **16.29.20**, Lemma **16.29.21**, Theorem **16.29.22** (tags \`D9BF9081FC38\`, \`2478F9CE0209\`, \`2DB4FF5FB5C1\`, lines **449–567**).
3. Cross-reference target: \`docs/sections/multiplier-ideal-envelopes-and-goodness--ideal-projection/index.html\`, blob \`f1979b73c857f4874dd4a5cb10b93bcc047ebbdc\`: **18.4.4 is a Proposition**, source label \`F9497834\`, permanent tag \`2506B7AD6F19\`. Its already-recorded misdescription in §18.4.5 is not recounted as a new discovery.

## POME-REL-ENVELOPE-MASS-SHARP-001

**Severity/status:** low / **verified conditional deduction**. The printed Lemma 16.28.69 is correct; this is a sharpness example, not an allegation of a false theorem.

**Statement.** For each integer \(n\geq1\) and each real \(0<a<1\), the factor \((1-a)^n\) in Lemma 16.28.69 is optimal even for a **fixed compact Kähler manifold**, even when the smaller-background envelope satisfies \(P_{a\theta}(u)=u\), and even when \(u\) has a single smooth divisorial pole. More precisely, let \(X=\mathbb P^n\), \(\theta=\omega_{\rm FS}\), and \(H\subset X\) be a hyperplane. There is a normalized \(u\in\mathrm{PSH}(X,\theta)\) with
\[
 P_{a\theta}(u)=u,\qquad
 \int_X\operatorname{MA}_{\theta}(u)
     =(1-a)^n v_-(\theta).
\]
Indeed, the full non-pluripolar mixed profile is
\[
 \big\langle(\theta+dd^cu)^k\big\rangle\wedge\theta^{n-k}
   =(1-a)^k\theta^n,\qquad 1\le k\le n,
\]
as global measures (and as currents in the natural bidegree).

**Proof.** Equip \(\mathcal O_{\mathbb P^n}(H)\simeq\mathcal O(1)\) with the Fubini–Study Hermitian metric and scale its defining section \(s_H\) so that \(\sup_X|s_H|^2=1\). With the repository's convention \(dd^c=(i/2\pi)\partial\bar\partial\), put
\[
 \psi_H=\log|s_H|^2\le0,\qquad u=a\psi_H .
\]
Poincaré–Lelong gives
\[
 dd^c\psi_H=[H]-\theta,\quad
 \theta+dd^cu=(1-a)\theta+a[H]\ge0,\quad
 a\theta+dd^cu=a[H]\ge0.
\]
Thus \(u\) is \(\theta\)-psh *and* \(a\theta\)-psh. It is admissible in the envelope defining \(P_{a\theta}(u)\), while every admissible function is at most \(u\) quasi-everywhere. The psh canonical representative extends that bound everywhere, and upper-semicontinuous regularization does not exceed the psh obstacle \(u\). Consequently \(P_{a\theta}(u)=u\), with no comparison theorem or regularization argument.

On \(X\setminus H\) the curvature is the smooth form \((1-a)\theta\). The non-pluripolar product agrees there with its ordinary smooth product and by definition charges no mass on the pluripolar divisor \(H\). Therefore its \(k\)-fold self-product, paired with the remaining smooth factors, is globally \((1-a)^k\theta^n\); the smooth form gives zero mass to \(H\) as well. In particular
\[
 \int_X\mathrm{MA}_{\theta}(u)=(1-a)^n\int_X\theta^n.
\]
Because \(\theta\) is **closed**, Bedford–Taylor integration by parts shows that every bounded \(\theta\)-psh potential has total mass \(\int_X\theta^n\). Hence \(v_-(\theta)=\int_X\theta^n>0\), and equality in the printed bound follows.

This construction works at every \(a\in(0,1)\), without varying the background. It also records all mixed exponents \((1-a)^k\), rather than merely the top-degree one. The compact Kähler mass invariance and the standard locality/non-charging definitions of non-pluripolar products are the explicit upstream inputs; their **full** internal proof chains are not certified in this session.

**Suggested correction:** none to the theorem or proof. An optional sharpness paragraph immediately after Lemma 16.28.69 can record the hyperplane example and mixed profile. Affected dependents: the constant carried into Theorem 16.28.70 and any proposed improvement of its mass factor; **no** claim is made that all additional assumptions of 16.28.70 are satisfied by this particular divisorial reference.

## Additional location for existing POME-IDEAL-PROJECTION-REFERENCE-KIND-001

**Severity/status:** low / **confirmed error (editorial reference kind only)**. The same already-logged root issue has a **second distinct source location**, not a new false mathematical theorem and not a re-registration of the §18.4.5 finding.

In \`docs/sections/envelope-systems-over-hermitian-perturbations/index.html\`, **line 65**, the proof of Proposition 16.29.3 says “By **corollary** 18.4.4” and links to tag \`2506B7AD6F19\`. But the target in \`docs/sections/multiplier-ideal-envelopes-and-goodness--ideal-projection/index.html\` is **Proposition 18.4.4**, source \`F9497834\`. The mathematical use—that ideal-model fixedness entails ordinary-envelope fixedness—is appropriate: it follows from the last identity of that proposition.

**Suggested correction:** replace only “corollary” by “proposition” at this new location, as also separately proposed for the earlier §18.4.5 occurrence. Preserve its link, tag, proof and attribution. Affected dependent: the bibliographic/reference wording in Proposition 16.29.3; no logical dependency is invalidated.

## Selected proof checks without newly asserted finding IDs

- **§16.28.68–70:** checked the roles of the smaller-background competitor, the contact-set mass comparison, positivity of bounded potentials in the remaining big background, and the \(\delta\downarrow0\) step. The constant-sharpness model above does not certify the contact-set theorem or the full general Hermitian volume theory.
- **§16.29.5 and 16.29.9:** reviewed order preservation, preservation of the all-weight multiplier-ideal class, limit curvature inequalities and the cofinality of \(h/j\) among positive Hermitian perturbations. The use of a single countable cofinal family is justified here by domination of each \(\eta>0\) by a sufficiently small \(h/j\); it is **not** a blanket sequential-compactness assumption.
- **§16.29.13:** checked how the smooth gauge change transports backgrounds and how the uniform gauge sandwich identifies ideals of the limiting curves; no new estimate is claimed.
- **§16.29.16–18:** checked deck invariance of \(v=w-\operatorname{Im}z\), the curvature Schur complement \(t(1-t|v|^2)/(4(1+t|v|^2))\ge-t/4\), the order-one divisorial multiplier ideals of the transverse normal-crossing pair, and the closed-class mass expansion with \(D^2=0\). The Liouville lemma on periodic subharmonic functions and the global analytic-current uniqueness step remain dependent on their upstream Pome proofs.
- **§16.29.20–22:** checked the geometric setup for equivariant descent, fiberwise invariance of the ideal envelope and the recovery argument conditional on the **upstream** positive-lower-volume theorem 13.21.7. Did not claim a new proof of that theorem or the entire Hopf bounded-mass construction.

## Coverage / unresolved / deferred / actions

**Actual new sections promoted from inventory-only:** exactly §§16.28 and 16.29, *selected mathematical proof passages only*. No complete section, chapter, Bedford–Taylor infrastructure, mixed mass theory, or theorem 13.21.7 is certified. Current actual ToC remains 25 chapters and 747 section identifiers (an inventory, not a completeness claim).

**Outstanding conditional dependencies:** compact Kähler bounded-product mass invariance, non-pluripolar locality, contact-measure comparison and Hermitian bounded positive mass (§16.28); uniqueness of fixed ideal representatives and preservation of multiplier ideals (§18.4), positive-volume recovery (§13.21), and the ruled-surface Liouville/nef model (§16.29). These are separate items for future nonexcluded audit, not purported errors.

**Strictly deferred by user:** the entire dedicated Demailly approximation/regularization programme, including Bergman, L², Ohsawa–Takegoshi, multiscale-atlas, and positivity-loss proof completion. None is reopened or marked resolved. No CI, project build, formal check, website publication, source/registry/canonicalization/tag changes or main-branch edits were performed.
