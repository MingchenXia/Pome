# Toric strict slack, fixed divisors, and elementary minimal growth

Date: 2026-11-26. Reviewed main: b6933b772f41b45918f7e25ed1afbbb1fd892272.

## Scope and exact anchors

Integrated reading edition: docs/sections/toric-pluripotential-theory-on-big-line-bundles/index.html, blob d77d383b4bee977cca473ea43627ee7ac449cfda. New selected reading of lines 464–497 (flag examples, up to the excluded approximation lemma), 700–915 (stratum Lelong formula, minimal growth, and opening convex correspondence). Rechecked setup and normalization lines 7–392 (in particular 21.13.2, 21.13.5, 21.13.8, Examples 21.13.15 and .17, 21.13.23, Definitions .25–.27 and Proposition .28 statement). The approximation-dependent 21.13.38–39 is not audited or certified; its use in the original minimal-growth proof is merely recorded. Normalization recheck: docs/sections/toric-pluripotential-theory-on-ample-line-bundles/index.html, lines 96–150, equation 21.12.6 tropicalization convention log|chi^m|^2 and Lemma 21.12.7. Current TOC docs/chapters/index.html has exactly 747 section identifiers, equal to the current matrix set with no repetitions. No whole-section or historical first-visit claim.

## POME-TORIC-NEGATIVE-PART-STRICT-SLACK-001

Severity: medium. Status: confirmed error in the prose equivalence following (21.13.51), not in the displayed minimal-multiplicity formula or Theorem 21.13.45. Source SGPT tag 24E2E20F, permanent 70B4F53FBB2E, physical lines 823–840, in particular 834–840. The setup is a smooth projective toric variety and a big integral invariant divisor D. Write P=P_D, and set
\[
d_\rho=a_\rho+\min_{m\in P}\langle m,u_\rho\rangle.
\]
The text asserts a prime divisor occurs in the negative part iff its inequality is redundant in defining P. In the ordinary polyhedral meaning (deleting it leaves the set unchanged), the converse is false.

**Counterexample within the printed hypotheses.** Use the collection's own Example 21.13.15 (permanent B328D39711DF, lines 209–242), the blowup of P^2 at [1:0:0] with D the pullback of a line missing this point. The rays are (1,0),(0,1),(-1,-1),(1,1); coefficients are 0,0,1,0. Thus P={x>=0,y>=0,x+y<=1}; the exceptional inequality x+y>=0 is implied by the first two. Its equality set is the vertex (0,0), and d_E=0. The pulled-back Fubini–Study form is a smooth semipositive representative, so minimal divisorial multiplicity is zero independently of any approximation or volume theorem. The divisor is big (its square is 1, or its section count is that of O(k) on P^2), and nef; E is not a negative component. Example 21.13.17 instead has strictly positive slack d_E=1, which explains why the two examples must be distinguished.

**Proposed correction.** Occurrence is equivalent to strict slack d_rho>0, or equivalently Q_rho empty, not mere redundancy. Strict slack implies redundancy: if a point satisfying all other inequalities violates this one, the segment to an interior point of P meets its equality hyperplane while satisfying the others, a contradiction. Redundancy with equality possible (even only at a vertex) gives zero coefficient. Replace the ambiguous phrase about removing redundancies by the exact coefficient formula for the modified-nef part:
\[
D_{\rm mov}=\sum_\rho(a_\rho-d_\rho)D_\rho
=\sum_\rho[-\min_{m\in P}\langle m,u_\rho\rangle]D_\rho.
\]
All coefficients are rational and P_{D_mov}=P: each new inequality is tighter but holds on P. In particular one tightens each inequality to the actual supporting value, rather than deleting a divisor or setting its coefficient to zero. On a common denominator multiple the character sections have no common divisorial zeros, as every ray minimum is attained at a rational vertex, and no section has a zero on the dense torus. This is consistent with the modified-nef terminology; no independent proof of the general analytic Zariski decomposition is asserted here.

Affected: the explanatory criterion after (21.13.51) itself and any use of redundancy as a test for negative components. Corollary 21.13.43 uses the correct equality-face test; no correction to it or the displayed coefficient formula is necessary. Direct downstream reference search across all files not completed.

## POME-TORIC-MINIMAL-GROWTH-ELEMENTARY-001

Severity: low. Status: verified conditional shorter proof of Theorem 21.13.45 (SGPT 7CCE1B26, permanent 1293B87EF09F, lines 753–818), and the minimal divisorial coefficient formula (21.13.51). The proof avoids the original comparison with partial Okounkov bodies and its approximation input, the BEGZ existence theorem and BB real regularity theorem. This is a direct finite-character and elementary convex argument, not a Bergman approximation.

Retain the printed smooth invariant reference h with curvature theta. On the torus use x=Trop(z) as in 21.12, so log|chi^m|^2=<m,x>. The fixed rational section s_D has divisor D and F_theta(x)=-log|s_D|_h^2 by (21.13.23), source CDCD55296D94 (permanent equation tag). For any nonidentically -infinity toric theta-psh phi, F=F_theta+phi on the torus is finite convex by 21.13.25 and 21.12.7. For a ray u_rho and a fixed x, the real path x-t u_rho, t->+infinity, has a representative tending to the dense orbit of D_rho: in a smooth maximal cone containing rho, use the dual character coordinates, let the rho coordinate tend to zero with log squared modulus decreasing by t, and keep the other coordinates fixed and nonzero. The meromorphic section has order a_rho there and its remaining smooth nonvanishing factor has bounded log norm. Consequently
\[
F_\theta(x-tu_\rho)=t a_\rho+O_x(1).
\]
Compactness bounds phi from above. If p is any subgradient of F at x, the supporting inequality gives
\[
F(x)-t\langle p,u_\rho\rangle\le F(x-tu_\rho)\le t a_\rho+O_x(1).
\]
Divide by t and let t tend to infinity to get <p,u_rho>>=-a_rho. Hence every subgradient lies in P, with no strict positivity or mass hypothesis. Taking a subgradient at x and testing at 0 proves F(x)<=F(0)+h_P(x), where h_P(x)=max_{p in P}<p,x>. In particular Delta(theta,phi) is contained in P by Definition 21.13.27. This also gives the upper bound for F_{V_theta}; V_theta is invariant by uniqueness of its envelope under the torus action.

For the lower bound choose a single integer q clearing the denominators of every vertex v of P. The characters s_v=chi^{qv}s_D^q are global holomorphic sections of L^q by the character-section formula in the proof of 21.13.8. Set
\[
\psi=q^{-1}\log\sum_v |s_v|_{h^q}^2-C
\]
with C chosen so psi<=0. This is theta-psh by the local log-sum formula for finitely many holomorphic functions, and therefore V_theta>=psi. No varying q, Hilbert inner product, L2 estimate or approximation is involved. On the torus,
\[
F_\psi=q^{-1}\log\sum_v e^{q\langle v,x\rangle}-C,
\quad
h_P-C\le F_\psi\le h_P-C+q^{-1}\log\#\mathrm{Vert}(P).
\]
Thus F_V-h_P is globally bounded. Moreover V_theta-psi is bounded on the torus and hence throughout X in the singularity-type sense by local psh upper-semicontinuous extension across the boundary (the usual uniqueness of the psh extension). The local character weights also show that the generic Lelong number of psi on D_rho is exactly min_v(a_rho+<v,u_rho>): at a point of the dense orbit the remaining factors of the monomials are nonvanishing, so the log-sum equals the smallest power of the transverse coordinate times a bounded factor in the logarithm. This proves (21.13.51) without the partial Okounkov comparison.

To derive Delta(theta,V_theta)=P from the bounded support-function estimate, the conjugate F_V^* has effective domain P: it is finite for p in P by the lower support bound and infinite outside P by separating hyperplane and the upper support bound. Apply the existing convex-gradient/domain identification cited as 21.11.62 (not recertified here), or the standard corresponding recession-slope fact. Proposition 21.13.28 then gives the stated n! vol(P) mass identity. These last dependencies are conditional, not complete transitive certifications. The support comparison itself and the minimal divisorial coefficients need neither the external existence/regularity results nor Demailly approximation. Preserve historical attribution in the existing footnote.

## Coverage and limitations

Selected §21.13 only; later energy, geodesic and restriction statements not audited in this run. §21.12 normalization dependency only. One confirmed erroneous prose implication, one conditional shorter proof, zero newly refuted numbered theorem statements, zero complete upstream certifications. Excluded Demailly regularization/Bergman/L2/Ohsawa–Takegoshi/multiscale/positivity-loss programmes remain deferred-by-user, not resolved. No builds, tests, CI, website publication or production edits.
