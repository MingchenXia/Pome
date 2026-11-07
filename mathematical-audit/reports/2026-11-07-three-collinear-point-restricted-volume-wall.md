# Three collinear plane points: exact restricted-volume wall, section ranks, and volume gradient

**Finding:** POME-RESVOL-THREE-COLLINEAR-WALL-001. **Status:** verified conditional deduction. **Severity:** low (a new independent algebraic model, *not* a refutation of a Pome theorem). **Reviewed production main:** b6933b772f41b45918f7e25ed1afbbb1fd892272. **Date:** 2026-11-07.

## Precisely reviewed reading-edition locations

- docs/sections/divisorial-restricted-volumes/index.html, blob 8eb1127568e77d6d045098361c366ceeb846b909, §20.8 introduction at physical line 7, Theorem 20.8.3 **statement only** at lines 64–66 (source label transcendental-positive-cones:42C59BDB; permanent tag 8DC7DAC31FB7); Proposition 20.8.16 **statement only** at lines 350–352 (source label transcendental-positive-cones:682A1645; permanent tag 7ED04B77FCC6). The nonexcluded section's rest, notably the theorem's general proof, is **not** certified.
- docs/index.html, blob 68e66f6b30cdaaee887dc3c91580cdd0a38d8801, current §20.8 table-of-contents locator, to avoid assuming old source numbering.
- The proof of Lemma 20.8.1 and any regularization-dependent premises of Proposition 20.8.16 are **excluded/deferred-by-user**, not examined or supplied here. Classical-to-analytic restricted-volume identification is explicitly **conditional** on the corresponding internal results.

## Completely explicit algebraic calculation

Let p1,p2,p3 be three distinct collinear points of P², on L={W=0}. Blow them up to X, with H the pullback of a line, exceptional curves E1,E2,E3, and C=H-E1-E2-E3 the strict transform of L. Then C²=-2, C·Ei=1, Ei²=-1 and Ei·Ej=0 (i≠j). Take positive integers d,m with d>m and D=dH-m(E1+E2+E3). This is a big divisor, as the following *explicit section count* proves, with no asymptotic Riemann–Roch, Zariski-decomposition theorem, or approximation invoked.

For k≥1 put N=kd, M=km. Write every homogeneous polynomial F of degree N uniquely as Σ(j=0..N) W^j f_(N-j)(X,Y). Vanishing to order M at each pi is **equivalent** to the requirement that, for j<M, the binary form f_(N-j) vanish at each of the three points of P¹ to order at least M-j. Consequently

h0(X,kD) = Σ(j=0..M-1) max{0,N-3M+2j+1} + (N-M+1)(N-M+2)/2.    (1)

This is an equality in every degree, not just an asymptotic estimate: the three vanishing conditions on binary forms cut out the product of three coprime linear factors, and there are N-3M+2j+1 coefficients if that number is positive.

Set a_k=max{0,ceil((3M-N)/2)}, q_k=M-a_k and δ_k=N-3M+2a_k≥0. Direct summation of (1) gives

h0(X,kD)=q_k²+δ_k q_k+(N-M+1)(N-M+2)/2.                 (2)

For m<d<3m one has 0≤δ_k≤1, q_k/k→(d-m)/2, and hence

vol_X(D)=lim(k→∞) 2h0(kD)/k² = (3/2)(d-m)².             (3)

For d≥3m, a_k=0; the same exact formula gives

vol_X(D)=d²-3m².                                      (4)

The two expressions agree at d=3m. At d=m, the only sections are powers of W and vol=0; no claim of bigness is made there.

**Fixed component and restricted image ranks.** Every F above is divisible by W^a_k, and there exists such an F with precisely that power: at j=a_k, choose f_(N-a_k) with the prescribed three roots. Thus the fixed multiplicity of C in |kD| is exactly a_k, including the parity effect when 3M-N is odd.

The image of the restriction H0(X,kD)→H0(Ei,(kD)|Ei) has dimension **M-a_k+1**. Indeed its tangent-degree-M leading forms at pi are exactly multiples of W^a_k. Surjectivity onto that subspace follows because, after factoring W^a_k, the residual degree N-a_k is at least 3(M-a_k): choose products of (M-a_k) powers of three general lines through the three distinct points, times a form nonzero at the points. Varying the line through pi spans every degree-(M-a_k) binary form by polarization. In contrast, restriction to C has image dimension max{0,N-3M+1}, because it is evaluation at W=0 of degree-N binary forms with three order-M zeroes.

Therefore the **classical** restricted volumes (using rank/k for curve restrictions) are

vol_(X|Ei)(D)=m, if d≥3m;  (d-m)/2, if m<d<3m;
vol_(X|C)(D)=max{0,d-3m}.                               (5)

At the wall d=3m the C-restriction has rank 1 in each degree but restricted volume 0. If m<d<3m, C is fixed and E_i is not a fixed component. The distinction between a dimension-zero restriction image and a sublinear one is explicit.

**Independent intersection / negative-part check.** In the middle chamber put a=(3m-d)/2>0 and b=(d-m)/2>0. Then

D=P+aC,   P=b(3H-E1-E2-E3),   P·C=0,   P²=6b².         (6)

For any irreducible proper transform of a plane curve of degree e not equal to L, with multiplicities r_i at the pi, Bézout with L gives e≥r1+r2+r3. Thus P·curve=b(3e-Σr_i)>0; P·Ei=b>0 and P·C=0. Consequently P is nef, and the only irreducible curve with P-degree zero is C. Formula (3) reads vol(D)=P²=6b², verified **independently** by the exact polynomial count, not inferred from a general Zariski theorem. In the nef chamber d≥3m, the same Bézout argument gives D nef and (4) becomes D². In particular, for (d,m)=(5,2), D²=13 but vol(D)=27/2, and the three exceptional restricted volumes are 3/2 rather than the naive intersection D·Ei=2.

## Direct derivative test, without invoking the analytic theorem

For rational s sufficiently close to zero, consider D_s=D+sE1; pass to divisible k so kD_s is integral. The same coefficient-by-W argument, now allowing multiplicities M1=k(m-s), M2=M3=km, gives the **exact finite-degree count**

h0(kD_s)=Σ(j=0..kd) max{0,kd-j-Σ(i=1..3)max(Mi-j,0)+1}.   (7)

As a Riemann sum, this yields the independently derived continuous piecewise-polynomial volume function

vol(D_s)=2∫(t=0..d) [d-t-(m-s-t)_+ -2(m-t)_+]_+ dt.       (8)

When m<d<3m, with a=(3m-d)/2, differentiation of (8) at s=0 has no boundary term, because the positive-part integrand vanishes at its moving zeros; the derivative is 2∫(t=a..m)dt=d-m=2b. When d>3m it is 2∫(t=0..m)dt=2m. These are **exactly twice** the respective restricted volumes on E1 in (5), as required by the surface instance of Theorem 20.8.3. The comparison with that analytic theorem is conditional on its identification of the classical restricted volume with restricted current mass and on E1 meeting the Kähler locus; the calculation of (7)–(8) itself is unconditional.

For the fixed negative curve C in the middle chamber, D+sC=(d+s)H-(m+s)ΣEi and the middle-chamber volume (3) is constant in s, so the directional derivative is zero. This is **not** an application of Theorem 20.8.3 to C, since C lies in the non-Kähler locus. It is consistent with Proposition 20.8.16's zero numerical restricted volume there. The fact that P has C as its only null curve follows from the explicit Bézout intersection test; identifying this algebraic null locus with the analytic non-Kähler locus is *not* re-proved here.

## Scope and decision

- **No false printed theorem.** Equations (1)–(8) are a new, self-contained, non-toric/algebraic intersection test of the hypotheses and normalizations in Theorem 20.8.3 and Proposition 20.8.16. The total volume, fixed negative curve, restricted-image rank, wall, and one-sided derivative were calculated from actual sections.
- **Dependencies:** the statements of Theorem 20.8.3 and Proposition 20.8.16, and their analytic equivalences with classical ranks, remain conditional. The internal general volume-gradient theorem, positive-product construction and non-Kähler locus identification were *not* transitively certified. Every dedicated Demailly regularization, Bergman, weighted L², Ohsawa–Takegoshi, multiscale and positivity-loss proof line remains **deferred-by-user**.
- **Affected mathematical comparisons:** §20.8.3's divisor-direction derivative; §20.8.16's distinction between positive product and the naive signed intersection D·Ei, and between ordinary and numerical restricted volumes. Proposed production action: **none**; optionally add this independent three-collinear-point model to future examples after a separate reviewable PR. No edits to text, source tags, registries or canonicalization.
- **Coverage:** selected **statement-level** anchors §20.8.3/.16 with an independent elementary model, not the omitted general proofs; §20.8 was already partly reviewed. **Zero newly first-visited sections and zero newly certified entire sections.** Current project inventory: 25 chapters, 747 numbered sections, 0 certified entire sections.
- **Checks actually performed:** checked the identities (1) and (2) for five (d,m) samples and k∈{1,2,3,4,7} (25 finite integer comparisons, no general build). No CI, site publication, formal verification, or production edits.
