# General real convex bodies: zero boundary mass and sharp Hausdorff-to-TV estimate

Date: 2026-11-27 (Asia/Shanghai). Reviewed main: b6933b772f41b45918f7e25ed1afbbb1fd892272. Starting audit head: 861855574f849ff67c164c87274e46d2fe0cf9e1.

## Finding POME-REAL-CONVEX-NONSYMMETRIC-BOUNDARY-TV-001

Severity low; status **verified conditional deduction** (not a printed error). Theorem 16.42.6 (source F1D83716, permanent 69C6DC7FA336) assumes symmetry and its stated density formula requires that assumption. The boundary-mass and layer parts can instead be established for *every* full-dimensional compact real convex body, with no smoothness or symmetry. A further consequence is a sharp local Hölder-1/2 Hausdorff-to-total-variation bound, including arbitrary directed nets. The older 2026-10-26 symmetric qualitative TV and smooth Lorentz results are not counted again.

### Hypotheses and proof

Use the reading edition's dd^c convention and logarithmic class L_1. Translate so that the origin is interior to K, and choose radii 0<rho<=R with rho B subset K subset R B, where B is the closed real unit ball. Write M=2^(-n), m_K for the Minkowski gauge and A=R/rho. All measures below have mass M. The regularized extremal U=V_K^* is locally bounded with logarithmic growth of minimal singularity type, and its MA is supported on K (16.34.2). In fact U=V_K is continuous: for any real interior point use a small real cube centered there, whose raw extremal is continuous and zero there; the sandwich 0<=V_K<=V_K^*<=V_cube gives zero contact. At a boundary point x, the complex affine line h(s)=(1-s)x joins x to 0 through interior points for 0<s<=1. Proposition 16.32.7 (source BC2EEB85, permanent 5886156A306E) gives zero contact also at x. The compact zero-contact criterion gives global continuity. In particular no assertion of real analytic boundary is needed.

Exactly as in the printed 16.42.6, put gamma=1/2 log(1+|z|^2), omega=dd^c gamma on the affine chart and q=U-gamma on projective space. q is bounded omega-PSH. For t>1 use the projective automorphism F_t[Z0:Z']=[Z0:tZ'] and a_t=1/2 log((|Z0|^2+t^2|Z'|^2)/(|Z0|^2+|Z'|^2)), b_t=q∘F_t+a_t. Change variables in the bounded energy cocycle to get E(b_t)-E(q)=E(a_t)<=M log t. As t^(-1)K subset K, b_t>=q on the affine chart, and the same ordering holds at infinity (where F_t fixes every point and a_t=log t). The nonnegative j=0 term of the cocycle, and support and zero contact on K, give

    integral_K U(tx) d mu_K(x) <= (n+1) M log t.       (1)

This part of the printed proof never uses symmetry. It is conditional on the cited bounded projective energy and MA inputs, not a new proof of those inputs.

Replace the symmetric interval step as follows. For each x in K with m_K(x)>=r>0, choose a real polar functional ell with ell(x)=m_K(x), max_K ell=1. This follows from a supporting plane at x/m_K(x), normalized by its positive support value. Since rho B subset K, ||ell||<=1/rho. Put a=-min_K ell, so 0<a<=A. The affine complex-linear scalar map

    L(z)=(2 ell(z)+a-1)/(1+a)

takes K into [-1,1]. Composing the continuous Joukowski interval extremal with L is PSH of logarithmic growth and zero on K, hence is an admissible competitor for U. For tr>1 this gives

    U(tx) >= arcosh(1+2(t m_K(x)-1)/(1+a))
          >= arcosh(1+2(tr-1)/(1+A)).

Combine with (1), and choose t=r^(-2). For every 0<r<1,

    mu_K({m_K>=r}) <= 2(n+1) M log(1/r) /
                      arcosh(1+2(1/r-1)/(1+A)).      (2)

The RHS is O_{n,A}(sqrt(1-r)) as r increases to 1, because arcosh(1+s)/sqrt(2s) tends to 1. For A=1 this recovers the printed symmetric expression (for symmetric K one can directly use a=1 even if R/rho>1). The layers decrease to the boundary, so finite measure continuity gives mu_K(boundary K)=0. Proposition 16.42.2 supplies an absolutely continuous interior density; support on K gives global absolute continuity and integral M. No continuous representative of that density in the nonsymmetric case is asserted.

### Quantitative TV for nonsymmetric convex bodies

Let L be another full-dimensional real convex body, and h=d_H(K,L)<rho in Euclidean Hausdorff distance. Set delta=h/rho, P=(1+delta)K, B0=(1-delta)K. Uniform difference of support functions is at most h (by comparing nearest points). Since every unit-direction support value of K is at least rho, separation by support planes proves B0 subset K intersect L and K union L subset P.

By obstacle monotonicity U_P<=U_K,U_L; all are zero on int B0. The bounded ordered-contact inequality therefore gives both mu_K and mu_L >= mu_P restricted to int B0, as measures on the ambient real space. Let lambda be that common submeasure. Both positive remainders have mass M-lambda(R^n). Thus, for the total variation norm |mu_L-mu_K|(R^n),

    ||mu_L-mu_K||_TV <= 2 mu_P(P\int B0)
                      = 2 mu_K({m_K >= (1-delta)/(1+delta)}).

The equality is pullback by dilation, from the affine extremal covariance and local BT pullback. Formula (2) proves a local O_{n,A}(M sqrt(h/rho)) estimate as h/rho tends to zero. This is a deterministic two-body bound: any directed Hausdorff-convergent net satisfies TV convergence without extracting sequences. The case h=0 is equality of bodies.

Sharpness of the exponent in every dimension follows from K=[-1,1]^n and L=(1+delta)K. The printed cube measure (16.36.1) has product density (2pi)^(-n) product_j (R0^2-x_j^2)^(-1/2) on the cube of half-side R0. In the expanded cube the slab 1<x_1<1+delta has mass bounded below by a fixed positive multiple of sqrt(delta), by integrating the first factor and integrating the other n-1 factors over their full intervals. This slab is outside K. Hence the TV norm is at least this mass, while h=sqrt(n)delta. No uniform exponent greater than 1/2 is possible even at this fixed K. This sharpness is distinct from the previous qualitative symmetric TV result.

### Proposed correction / dependents

Optional separate proposition after 16.42.6, not removal of symmetry from its polar-volume-density statement (16.42.3). Uses 16.32.7, 16.33 interval formula, 16.34.2, 16.36.1, 16.42.2, bounded ordered contact and 17.3.4 cocycle. It strengthens the boundary and convergence conclusions for nonsymmetric bodies. No printed theorem refuted; no new external input beyond the existing conditional dependencies.

## Direct coverage and proof checks

All paths below are current integrated reading edition files on the pinned main. Line ranges refer to physical HTML lines (excluding navigation and bibliography). Historical first visits not claimed; earlier 16.39 and 16.42 work in LATEST retained.

* docs/sections/geometric-polynomial-approximation-and-local-uniqueness/index.html, blob 334d2453d12bdfeab3379fb0489bba3ddebf1ddb, lines 7–113. Theorem 16.38.1 F97596C6/DE0691E14C0E, examples 16.38.2 D0F11BDE/C6B88322442F and 16.38.3 4ED1578E/61CD9F3FD5EA. Checked the weighted l1 Banach space, Baire closed sets via bounded holomorphic normal families, and uniqueness on each neighborhood component. The constant C_q in the polynomial estimate can be eliminated by applying it to p^k and taking k-th roots, yielding the raw extremal bound -log q in a neighborhood of K via the polynomial characterization. Both isolated-point and accumulating-point examples respect the distinction between raw and regularized extremals. In the latter, the denominator estimate |a_j-a_k|>=2^(-max(j,k)) holds, and for i>n the factors with k>j give product 2^(-(n-j)(n-j+1)/2), while the remaining denominator losses are bounded by the convergent product C_0^2. The limsup exponent is (1/8)/8=1/64. No error found.
* docs/sections/a-continuous-foliation-by-extremal-ellipses/index.html, blob 7dc4c57a46027c89cf963aed3a647fed7ce17af4, lines 8–79, Theorem 16.39.1 B7A370FF/DCB9565E6FDC. Checked the phase quotient, strict monotonicity of Q_z, both y=0 and y nonzero limits, bracketing continuity of the inverse, and injectivity/immersion/properness on each exterior disk. The removable singularity at infinity for a bounded-above subharmonic difference and the polar functional attaining q(w) supply both bounds. No transverse differentiability or global triviality inferred.
* docs/sections/local-regularity-of-analytic-polyhedra/index.html, blob d6f9bd0c7e54de98ea0d02c1180eb8befc857997, lines 7–57, Lemma 16.40.1 6CA8DF2C/DD2047D70ACD, Theorem 16.40.2 D3099F01/8ED77FB38EC4. Checked fixed-sign subsequence outside the zero locus, properness of real analytic principalization, prime coordinate factorization, analytic arc with correct signs, holomorphic complexification of its parameter and nonthinness of an interval. The principalization theorem is the expressly declared permitted resolution input, not newly certified; no Demailly regularization is involved.
* docs/sections/equilibrium-densities-and-boundaries-of-real-convex-bodies/index.html, blob 431eebdd82ef03991a95d2f16bb77dfb084278a7, lines 7–217. Lemma 16.42.1 68D40FF9/CBCC93967447 (7–29); Proposition 16.42.2 3C4B5998/B7B8F93CC817 (34–49); Proposition 16.42.3 D5322D11/86440B2CBCE4 (54–105); Lemma 16.42.4 58266096/16C56B7B3FDA (110–119); Theorem 16.42.5 010CEA22/1E10E926515B (124–163); Theorem 16.42.6 F1D83716/69C6DC7FA336 (168–217). Checked the n!/(4pi)^n coefficient from the real Hessian, exposed-face zero volume, ordered-contact inequality directions for enclosing/inscribed cubes, the local uniform Taylor estimate and support-body volume, Gaussian smoothing of the real gauge squared (not the excluded complex regularization programme), uniform rolling radius and normal tube, analytic boundary pluripolarity and open-tube Portmanteau direction. For 16.42.6 the cocycle change of reference and dilation ordering are sound; the new proof only replaces the final use of symmetry. No claim that S_x(K^circ) is always convex.

Selected dependency checks: 16.32.7 lines 137–145 (maps-and-regularity-of-global-extremals, blob b20154011d37d46a4d0cc7751863207e5debf183); 16.33.1 and interval construction lines 8–47 (real-compact-sets-and-explicit-extremal-formulas, blob a5f8e9cd6aa60a22f344aadbdf8370422ce3220a); 16.34.2 support/mass lines 48–66 (logarithmic-total-mass-and-bounded-obstacle-support, blob 47387388cb62e2b99cf6f78370c914aa6f75909d); 17.3.4 cocycle (relative-energy-and-perron-segments--relative-monge-ampere-energy, blob 16fdcc4c6a6f0cc75e69ba267bd7da2b2d7922a1, lines 42–90). These are not whole new dependency reviews.

Four whole direct conditional readings; one new conditional finding; no new confirmed printed errors, demonstrated proof gaps or complete transitive proof certifications. Reconcile the four chapter-16 matrix rows without erasing legacy history. Demailly approximation/regularization and dedicated Bergman/L2/OT/multiscale/positivity-loss programmes remain deferred-by-user. No tests, builds, CI, publication or production changes.
