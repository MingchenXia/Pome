# Reduced Fréchet cohomology duality and cup-product rotation — 2026-11-27

Reviewed main: `b6933b772f41b45918f7e25ed1afbbb1fd892272`. Starting audit head: `9da41ab39f39fb0c0a588f2c1aa67dc940716602`. Scope: direct reading of all mathematical lines of §§10.57–10.59, not a transitive proof certificate. The designated Demailly approximation/regularization, dedicated Bergman, L², Ohsawa–Takegoshi, multiscale-atlas and positivity-loss programmes remain deferred-by-user.

## Finding POME-FRECHET-REDUCED-COHOMOLOGY-DUALITY-001

Severity: low. Status: verified conditional deduction (not a printed theorem error). Anchor: Lemma 10.59.2, permanent tag 42254A734333, source label 557D9B2C, physical lines 27–40; Corollary 10.59.3, permanent tag CFEFE5F704F2, source label 66861AB4, lines 45–63, in `docs/sections/spectral-sequences-support-and-cup-products--integration-contraction-and-precise-duality-scope/index.html` (blob 55412114272bdaf8f2b79ad36d829454862b32c9).

The printed lemma correctly assumes both adjacent ranges closed and concludes an algebraic identification with the continuous dual, not a strong-dual topological isomorphism. There is a useful exact description without either closed-range assumption. This is distinct from the earlier POME-DE-RHAM-PERIOD-CLOSED-RANGE-001, which concerns automatic real de Rham closed range via the period comparison.

### General statement and proof

Let E^bullet be a complex of Hausdorff locally convex spaces over R or C (in particular Fréchet spaces), with continuous differentials. Set Z=ker d^k, B=im d^{k-1}, D=d^k. Let primes denote continuous linear duals, and write M^perp for its annihilator. Give E^k' the weak-star topology sigma(E^k',E^k). Define the ordinary and weak-star reduced dual cohomology in complementary degree by

    H = Z/B,   H_red = Z/closure(B),
    H_dual = B^perp / im D',
    H_dual,red = B^perp / closure_weak-star(im D').

The closure of B is taken in E^k, equivalently in Z since Z is closed. Then restriction induces the canonical exact sequence of vector spaces

    0 -> Z^perp / im D' -> H_dual -> (H_red)' -> 0,

and the canonical algebraic isomorphism

    H_dual,red = (H_red)'.

The pairing of H and H_dual is well defined by evaluation. Its left radical is closure(B)/B and its right radical is Z^perp/im D'. Thus the reduced pairing separates both factors.

Proof: every functional on H_red is a continuous functional on Z annihilating B. It extends continuously to E^k by the seminorm form of Hahn–Banach (complex version as in 10.59.2). Conversely every T in B^perp restricts to such a functional. The kernel consists exactly of the functionals vanishing on Z; im D' lies in that kernel. This proves exactness. To compute the weak-star closure, let T vanish on Z, and prescribe any finite list x_1,...,x_N in E^k. The formula S_0(sum a_i D x_i)=sum a_i T(x_i) is well defined since any relation among D x_i gives an element of Z. The span is finite dimensional in the Hausdorff target, so S_0 is continuous and extends continuously to E^{k+1} by Hahn–Banach. Then D'S agrees with T on the finite list, hence belongs to every prescribed weak-star neighborhood of T of this form. Conversely every D'S vanishes on Z, and this annihilator is weak-star closed. Therefore closure_weak-star(im D')=Z^perp. Finally if z in Z is not in closure(B), the Hausdorff locally convex quotient Z/closure(B) has a continuous functional nonzero at [z], which extends to E^k. This proves the left radical formula, and the right one follows from restriction.

In the Fréchet setting, if only D has closed range, its induced bijection E^k/Z -> im D is a homeomorphism by open mapping. Each T vanishing on Z therefore factors as a continuous functional on im D, which extends to E^{k+1}. Thus im D'=Z^perp, and the unreduced dual cohomology already equals (H_red)'. Incoming closed range is needed only to identify H itself with its Hausdorff reduction and separate the unreduced ordinary group. If only B is closed, the restriction onto H' remains surjective but may have a nonzero kernel. No strong-dual closure or strong-dual topological isomorphism is asserted.

### Independent sharpness of the adjacent assumptions

Take the Hilbert space l², identifying its continuous dual using the standard Hilbert pairing (work over R for simplicity), and let A(x)_j=x_j/j for j>=1. Its range is dense (contains finitely supported sequences) but proper: y_j=1/j belongs to l² but has no l² preimage. Its transpose is A.

1. For the complex 0 -> E^k=l² --A--> E^{k+1}=l² -> 0, the incoming range is closed and H=0, yet H_dual=l²/im A is nonzero, entirely the right radical.
2. For 0 -> E^{k-1}=l² --A--> E^k=l² -> 0, the outgoing range is closed, H=l²/im A is nonzero, but H_dual=0, so the whole ordinary group is the left radical.

These are counterexamples to dropping the respective assumptions from the *unreduced* assertion of Lemma 10.59.2, not to the printed lemma, and are abstract complexes, not geometric Dolbeault counterexamples.

### Geometric application and proposed addition

Use the precise continuous-dual identification and complementary current signs of 10.59.3, lines 60–62. Without a closed-range assumption the smooth ordinary de Rham or Dolbeault quotient and the complementary compact-current quotient still have the above radicals. Replacing the former by its Hausdorff reduction and the latter by the quotient of closed compact currents by weak-star closure of compact-current boundaries gives a separating pairing and the algebraic continuous-dual identification. Here weak-star means evaluation on *all smooth complementary forms* with no support restriction, not just on compactly supported tests. By 10.57.1 the unreduced compact-current quotient agrees algebraically with compactly supported smooth/sheaf cohomology; one may transport the right radical under this comparison, but no equality with closure in an independently defined topology on compactly supported smooth forms is claimed. If the outgoing ordinary differential has closed range, the unreduced compact group already identifies with the continuous dual of reduced ordinary cohomology.

Propose an optional paragraph after 10.59.2 or 10.59.3; do not weaken the existing perfect/separating pairing statements for unreduced groups. Affected dependents are the compact/ordinary pairing and trace realization of 10.59.3; the compact perfect duality of 10.57.2 and 10.59.1 is unchanged. No new external mathematical input beyond Hahn–Banach, the finite-dimensional subspace topology, and the closed-range Fréchet open mapping argument already used by the printed lemma. Their upstream chains and the smooth/current comparison have not been independently certified here.

## Whole direct conditional reading

- §10.57, `docs/sections/spectral-sequences-support-and-cup-products--compact-supported-forms-currents-and-compact-duality/index.html`, blob b7aa363efc0c0104512b4291b9a0adb88e349fdb, mathematical lines 7–44. 10.57.1 (A9627E651E13 / 5AC46646), lines 8–24: support acyclicity, augmentation, real orientation and bundle Dolbeault resolution assumptions retained. 10.57.2 (12F3669A5BAA / 9CA26CBE), lines 29–44: compact-support equals ordinary on compact spaces; harmonic finite-dimensional duality only under the cited compact hypotheses. No noncompact perfection inferred.
- §10.58, `docs/sections/spectral-sequences-support-and-cup-products--cup-products-and-differential-resolution-comparisons/index.html`, blob 635f86f3f9848c1bf3f53af96067eac42d63f892, mathematical lines 7–217. 10.58.3 (16CBD1C5A6C8 / 7028C5FA), lines 31–66: the two middle cofaces have opposite signs, associativity follows by shared endpoints, and evaluation at the stalk splits B->GB R_x-linearly so dimension shifting does not require flatness of A. For the commutativity induction the connecting sign is (-1)^p; combined with (-1)^{p(q-1)} it gives (-1)^{pq}. 10.58.6 (501BF07CE068 / 5FA4B309), lines 75–94: total product sign (-1)^{ba'}, finite support under locally finite relatively compact covers; every extra index meets the compact union of active closures. 10.58.7 (6F68DD8223F3 / 67439612), lines 102–122: functoriality, properness for compact pullbacks, cylinder intersections and Koszul factor (-1)^{qp'}; no Künneth claim. 10.58.9 (3E96DCA67FB2 / F8D85C5F), lines 131–161: total-product factor (-1)^{rb}; positive connecting versus augmentational convention epsilon_n=(-1)^{n(n+1)/2}, with epsilon_{r+s}/(epsilon_r epsilon_s)=(-1)^{rs}. 10.58.11 (45A6B240A010 / A0BB72D2), lines 166–197: Dolbeault chain pairing (-1)^{ps} wedge accounts for resolution degree q rather than full degree p+q; associativity exponent ps+(p+r)t=rt+p(s+t). 10.58.13 (FF9CB82C72A2 / 3B2B998D), lines 202–217: partition contraction inserts first index and new differential crosses t-1 earlier factors, yielding (-1)^{n(n-1)/2}; ratio to augmentational convention (-1)^n is multiplicative. No arbitrary current wedge asserted.
- §10.59, path/blob above, mathematical lines 7–63. 10.59.1 (E68024FC9A71 / 6D6C8923), lines 11–22: trace sign (-1)^{p(n-q)} and compact/ordinary complementary supports. 10.59.2–3 as above: checked both Hahn–Banach extensions, closed-range quotient homeomorphism, continuous vs algebraic dual, orientation and dual-bundle types.

The cited local resolutions 10.43.11, 10.44.9, 10.56.1–3/9, Godement comparison 10.43.15–16 and 10.55.4/6, compact analytic duality 10.46.7/10, and locally convex inputs 2.10.2/4, 2.12.1 are used conditionally; this is not their independent proof certification.

## Coverage and disposition

The actual main `docs/index.html` section links (747) were compared to the 747 distinct section rows of SECTION_MATRIX.md, with zero missing or extra numbers. These three rows previously had bare legacy-unreconciled status; this records direct current full-section reading, not historical first visits. One new conditional deduction, no new confirmed printed errors, no demonstrated proof gaps, zero complete transitive chains. No production/source/registry/permanent-tag edits. No builds, software tests, Actions CI or website publication.
