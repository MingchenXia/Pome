# Audit of the codimension-two removable-set argument: a truncated-direction Remmert gap and a direct repair

**Date:** 2026-11-16.
**Stable finding ID:** POME-PSH-CODIM2-DIRECTION-IMAGE-001.
**Classification:** low–medium severity; **proof gap** in one printed proof step, with a **verified local repair** proposed in this report. **The theorem is not refuted.**
**Reviewed main:** b6933b772f41b45918f7e25ed1afbbb1fd892272.
**Integrated reading edition:** docs/sections/plurisubharmonic-functions--properties-of-plurisubharmonic-functions/index.html, blob e7d871122eca3eb7416ab8a993063cdc8d3987f3.
**Source/locator:** SGPT source statement sgpt-1E88697D (source tag 1E88697D), permanent theorem tag DAE812E1A818; clause (1) source tag 7EBFD328 and permanent clause tag A8DA4460C6EC. Theorem and two cases: physical lines 179–195. The codimension-two argument: lines 214–245; specifically, the direction-projection assertion in line 237. This report does not edit the mathematical body or permanent tags.

## Hypotheses and conclusion audited

Let X be a complex manifold, let Z be an analytic subset of complex codimension at least two at every point, and let u be plurisubharmonic on X\Z. Theorem 5.14.10(1) asserts that u has a unique plurisubharmonic extension, determined on Z by the punctured-neighborhood limsup. There is no a priori upper bound for u near Z in clause (1). The proof reduces to verifying local upper boundedness, after which it invokes the separately stated codimension-one, locally upper-bounded extension case.

For a contradiction, the printed proof chooses z in Z, points x_j in X\Z tending to z with u(x_j) tending to +infinity, a line L through z meeting Z locally only at z, and a small closed ball around z whose intersection with L has a boundary circle on which u is uniformly upper bounded. It needs lines L_j through x_j, converging to L and avoiding Z within this ball, in order to apply the one-variable maximum principle to u restricted to L_j.

## Exact gap: a closed-ball truncation is not a proper holomorphic map of analytic spaces

Line 237 says that the closure of Z intersected with a sufficiently small ball is a "compact analytic set" and that its direction projection is proper; it then invokes Remmert's proper mapping theorem to infer that the image lies in a proper analytic subset of projective direction space.

This application is not valid as written. Even when Z extends analytically beyond the closed ball, its intersection with a **closed Euclidean ball** is generally a compact set **with a real boundary**, not a complex analytic space to which Remmert's proper holomorphic mapping theorem applies. On the **open** analytic space Z intersected with the ball, the direction projection need not be proper; compactness of the truncation cannot be used to turn the open map into a proper holomorphic map. Thus the displayed Remmert implication is not a justified proof step. No falsity of the removable-singularity theorem follows: the desired avoidance property is correct, but needs a different argument.

For clarity, the often-useful principle that a continuous image of a compact set is compact does not imply that the image is a complex analytic subset. The mistake concerns the mathematical category in which the projection is proper, not the existence of limits of the resulting lines.

## Complete replacement of the direction-avoidance step

Work in a coordinate chart centered at z in C^n, n at least two. Choose r>0 such that the closed Euclidean ball K_0=closure(B(z,r)) lies in the chart, and write K=Z intersect K_0. Shrinking r as necessary, Z is analytic in an open neighborhood of K_0. Let x be any point in B(z,r)\Z. Consider the projective direction map

\[
q_x:K\longrightarrow\mathbf P^{n-1},\qquad y\longmapsto[y-x].
\]

This is well defined and continuous on K, since x is not in Z and K is compact. Its image A_x=q_x(K) is compact. **A_x has empty interior.** Indeed, an analytic set of complex dimension at most n-2 is the countable union of smooth complex-analytic strata (successive regular loci of its singular sets), each of real dimension at most 2n-4. On each relatively compact smooth chart of each stratum, q_x is smooth; by the elementary rank/measure-zero form of Sard's theorem, its image has zero (2n-2)-dimensional measure in the smooth projective manifold P^{n-1}. Countably many charts suffice. Thus A_x has measure zero and hence, being compact, is nowhere dense. When n=2, K is locally discrete and compact, so the same conclusion is immediate because A_x is finite.

Consequently, for any direction \(\theta_0\in\mathbf P^{n-1}\) and any \(\delta>0\), there exists \(\theta\notin A_x\) with Fubini–Study distance \(d_{\rm FS}(\theta,\theta_0)<\delta\). The affine complex line through x in direction \(\theta\) is disjoint from K: a point y of intersection would give \([y-x]=\theta\in A_x\), a contradiction.

Apply this construction with \(x=x_j\), \(\theta_0\) the direction of the fixed line L, and \(\delta=1/j\). Choose \(\theta_j\notin q_{x_j}(K)\), \(d_{\rm FS}(\theta_j,\theta_0)<1/j\), and let \(L_j=x_j+\mathbb C\theta_j\). Then \(L_j\cap K=\varnothing\), and, because \(x_j\to z\) and \(\theta_j\to\theta_0\), the affine lines \(L_j\) converge to L. In particular, for all sufficiently large j, their boundary circles \(L_j\cap\partial B(z,r)\) lie in the previously constructed open neighborhood U on which u<0. The subharmonic maximum principle on the disc \(L_j\cap B(z,r)\) gives \(u(x_j)\le0\), contradicting \(u(x_j)\to+\infty\).

This supplies exactly the missing direction-avoidance assertion. It uses basic analytic-set dimension/regular-locus facts, compactness, Sard's measure-zero theorem and the one-variable maximum principle. It does **not** use Remmert's proper mapping theorem or any analytic approximation, Bergman, weighted L2, Ohsawa–Takegoshi, or multiscale gluing result.

The argument fixes the local step in clause (1); it does **not** by itself reverify the independently quoted codimension-one extension result used earlier at lines 204–212, nor every theorem that depends transitively on 5.14.10. The Brelot/Grauert–Remmert historical attribution should remain unchanged.

## Separate direct checks (not additional findings)

I also read the literal hypotheses and proof of Lemma 5.14.16 (source sgpt-4B736FC3, permanent tag 49CC56CB484C; lines 287–352) and Corollary 5.14.20 (source sgpt-A3A928E4, permanent tag 79C564A098F9; lines 353–365). The finite-threshold argument in Lemma 5.14.16 legitimately excludes points where the subsidiary psh function is minus infinity, because the maximum there is the original psh function. The local boundary-neighborhood construction is valid without requiring relative compactness of the subdomain. I found no new counterexample to these two statements in this selected check. Corollary 5.14.20 is an internal reuse of the independently identified maximum-gluing proposition; its general upstream proof is not certified here.

Proposition 5.14.21 (source sgpt-1F7D0D7B, tag 3EDBDD31B3F1, lines 367–382) was inspected only to classify its cited Bedford–Taylor Dirichlet existence input; **no mathematical certification of the balayage existence/uniqueness assertion was attempted**. The locally bounded homogeneous Monge–Ampère Dirichlet input is a genuine external dependency unless its established internal equivalent is independently linked.

## Proposed patch, affected dependents, and coverage

Replace only the Remmert sentence at physical line 237 with the compact direction-map/measure-zero argument above. Do not change the theorem statement, historic attribution, reader numbering, source tags or other source/body text as part of this audit. The immediate dependent is the codimension-two step of Theorem 5.14.10; later applications of this extension result should refer to the repaired argument only after review/integration. No claim of a false published theorem, full section certification, or transitive proof certification is made.

This adds selected proof-level inspection of 5.14.10(1) and 5.14.16/20, and a dependency classification only for 5.14.21. Section 5.14 had already been partially visited for Choquet's lemma in the October audit; therefore **zero newly first-visited numbered sections** and **zero newly wholly certified sections** are counted. The main table of contents previously counted 25 chapters and 747 numbered sections; this run did not independently recount them.

All Demailly approximation/regularization and dedicated Bergman, weighted-L2, Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof-completion work remain **deferred-by-user**, neither resolved nor certified. The run is audit-documentation-only; no project build, test suite, CI, source, registry, main-branch or website modification is claimed.
