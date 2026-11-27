# Full restriction is not the Okounkov slice of an arbitrary big class

- Finding: **POME-OKOUNKOV-BIG-SLICE-FULL-RESTRICTION-001**.
- Severity: high (false clause in a foundational statement); status: confirmed error, proposed qualification, not integrated.
- Reviewed main: b6933b772f41b45918f7e25ed1afbbb1fd892272. Starting audit head: 9f0f425670eef2f75beb8b0b0d2c37d29958843a.
- Scope: selected nonexcluded portions of §19.5, not a whole-section or transitive proof certificate.

## Anchors

* docs/sections/the-theory-of-okounkov-bodies--transcendental-partial-okounkov-bodies/index.html, blob a53c6b2f80c3775e9d646f57808425823ec4a4ac, physical lines 7–52: Definition 19.5.2 (AD7EC900552C), Theorem 19.5.4 (E839B4A35A2A, source CE657E18), final clause lines 44–49 (111D84FB6B1C, source F0C64B11). The theorem allows any big class and any smooth flag; the final clause identifies the small positive first-coordinate slice with the entire Okounkov body of the restricted cohomology class. No Kähler or nef hypothesis appears there.
* docs/sections/the-theory-of-okounkov-bodies--flags-and-valuations/index.html, blob 9190d2ae0d3e51ca0ca965000cb9b5b2ec965c85, lines 23–38, 51–76, 104–108: flag valuations, Definition 19.3.6 (78704BB19535), compatibility for Cartier divisors, Example 19.3.8 (534C64D15BE3).
* docs/sections/the-trace-operator/index.html, blob 1f3a3e4f0317a308b43bd3df53dda84c5f3fa50a, lines 92–101, 225–245: analytic restriction and trace definition 20.2.6 (ADF6E265888F). No approximation theorem is re-audited.
* Same §19.5, lines 431–470: Lemma 19.5.32 (082A647C2B55), especially lines 457–469, uses the slice clause only in the Kähler case. Lines 7–175 were inspected, including 19.5.7–12, but no complete dependency certification is implied.

## Explicit counterexample with both sides defined and positive-dimensional

Let X be the blowup of P^2 at p, H the pullback of the line class and E the exceptional divisor. Then H^2=1, H.E=0, E^2=-1. Set alpha=H+E, a big integral class (adding the effective E to the big H preserves bigness). Let C be the strict transform of a line through p, so C=H-E, C^2=0, C.E=1, and C is a smooth P^1. Choose x in C outside E. This is a smooth flag X>C>{x} on a connected compact projective manifold. For every 0<t<1,

    (alpha-t[C]).C = ((1-t)H+(1+t)E).C = 2.

Thus the right side of the printed identity is the interval [0,2]. Indeed a positive class of degree 2 on P^1 has precisely this Okounkov body: point atoms have size at most 2 and rational effective divisors of degree 2 realize a dense set of sizes.

The actual slice is [0,1-t], not [0,2]. Here is an elementary computation in the integral class, with the standard projective compatibility of the transcendental and ordinary Okounkov bodies as stated in the cited DRWNXZ introduction (arXiv:2309.07584v3, 5 January 2026, around HTML lines 81–86). This compatibility is a declared external input, not certified transitively by this report.

For any nonzero section of m(H+E), write its effective divisor as k C+b E+D, where k,b are nonnegative integers and D is effective containing neither C nor E. Since D.E>=0,

    0 <= (mH+mE-kC-bE).E = -m-k+b,

so b>=m+k. The second flag valuation is ord_x((bE+D)|_C)=ord_x(D|_C), since x is not on E. It is at most D.C=2m-b<=m-k. Therefore every normalized valuation (s,y) satisfies s>=0, y>=0 and s+y<=1; the closed convex hull also does.

Conversely choose two lines in P^2 not through p, with strict transforms A and B meeting C respectively at x and at a different point. For nonnegative integers k,j with k+j<=m the effective divisor

    k C+(m+k) E+j A+(m-k-j) B

has class m(H+E) and normalized valuation (k/m,j/m). These lattice points are dense in the triangle {s>=0,y>=0,s+y<=1}. Thus the ordinary body is exactly that triangle; via projective compatibility so is the transcendental body. No asymptotic approximation of arbitrary PSH weights enters this calculation. In particular, the discrepancy holds for arbitrarily small positive t and even for Y_1 not contained in the non-Kähler locus (the Kähler locus includes X\E, as is seen from H-delta E ample and the positive added divisor (1+delta)E).

Alternatively, the same upper bound follows directly in the analytic-singularity setting if one uses the trace/ordinary restriction agreement for residual analytic potentials: subtract a[C]+b[E] with a,b the two generic Lelong numbers from a positive current in alpha. The residual is positive, has no generic pole on either curve, and ordinary restriction to E has mass b-1-a>=0; restriction to C has mass 2-b. At x the E divisor contributes zero. This is the same inequality y<=1-a. This alternate derivation is conditional on the stated restriction compatibility and is not needed for the algebraic computation.

## Source comparison and proposed correction

The cited paper [DRWNXZ, Transcendental Okounkov bodies, arXiv:2309.07584v3](https://arxiv.org/html/2309.07584v3), §7, Property C_n (HTML lines 845–857), identifies the (n-1)-dimensional slice volume with the restricted volume for interior first-coordinate t, with the (n-1)! factor. It does not identify the slice as a set with the unrestricted body of the cohomology class on Y_1 in the general big case. Its Lemma 7.5 uses partial bodies of actual restricted currents. The obstruction above is the forced intersection of the fixed divisor with C. Merely requiring the flag hypersurface not to be contained in the non-Kähler locus is insufficient.

Propose separating the general restricted-volume identity (explicit external input from DRWNXZ, with its interior-t hypothesis) from any full-body slice identity restricted to a Kähler class alpha-t[Y_1], where an extension input is available. Do not advertise a complete proof of the latter here; check the exact extension theorem hypotheses separately, without reopening the excluded regularization programme. A direct check in the example gives restricted volume 1-t rather than full degree 2: the sections with vanishing k along C, divided by the defining equation of C to power k, have the forced divisor (m+k)(E intersect C); the remaining degree m-k is realized by products of lines not through p. For rational t=k/m the resulting restricted series on C is exactly that fixed section times the complete degree m-k series. Its normalized dimension tends to 1-t.

## Dependents and coverage

The direct occurrence of the affected clause in the same section is Lemma 19.5.32, Step 2, lines 457–469. It explicitly assumes beta Kähler, so the counterexample does not refute that lemma. The remaining uses of 19.5.4 in §19.5 (lines 112,180,188,375,403,443,463,626,652) invoke other properties or cite the theorem collectively; those are not refuted by this example. Other repository-wide dependents have not been exhaustively located.

Selected new review §19.5.1–12 (physical lines 7–175), contextual repeat §19.5.32 (431–470), selected §19.3 (23–108) and §20.2 (92–101,225–245). Existing §19.5.32 audit is not counted again. Zero newly whole sections, one confirmed false clause, zero new demonstrated proof gaps, zero complete upstream certifications. The projective compatibility and restricted-volume identity are explicit external inputs. Demailly approximation, its dedicated Bergman/L2/OT/multiscale/positivity-loss work remain deferred-by-user; no excluded proof is reopened. No builds, project tests, CI, production edits, or publication.
