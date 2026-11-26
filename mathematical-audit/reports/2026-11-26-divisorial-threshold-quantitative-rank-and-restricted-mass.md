# Quantitative divisorial threshold deficit and a shorter restricted-mass vanishing argument

Date: 2026-11-26. Reviewed main: b6933b772f41b45918f7e25ed1afbbb1fd892272. Audit-only proposals; no production edits.

## POME-DIVISOR-THRESHOLD-SEMIPOSITIVE-RANK-DEFICIT-001

Severity low; status **verified conditional deduction**, not a printed theorem error. Targets Proposition 10.18.1 (source F984B99B, permanent 7B0AC7895B1F, physical lines 14–48) and Corollary 10.18.4 (source 321DCAD0, permanent 852EFF5927B9, lines 87–98), in docs/sections/bott-chern-classes-and-singular-loci--divisorial-components-at-the-threshold/index.html, blob 4a6c6ea644b14c491a94592bfdc849acecb16fad.

Retain all hypotheses and notation of Proposition 10.18.1: compact Hermitian X, n>=2, nonzero f>=0 in L^1(dV), p=f^(1/n), b=b_omega(f), a positive subsolution coefficient c and an effective real divisor E dominated by the subsolution current. In addition assume a smooth semipositive representative beta of E with at least r eigenvalues >= lambda>0 relative to omega at every point, for some fixed 1<=r<=n. Set rho=b^(-1/n), g=(dV/omega^n)^(1/n), G=max_X g. For r<n define C_r=(n/r)^(r/n)(n/(n-r))^((n-r)/n), and C_n=1.

For every smooth normalized Gauduchon test T set x=integral beta wedge T, sigma=omega wedge T (a probability). The matrix convention of 12.7.1 is tr P=n and beta wedge T=(tr(BP)/n)sigma; the determinant measure is g det(P)^(1/n) sigma. In a unitary basis diagonalizing B, let s be the sum of the first r diagonal entries of P divided by n, selecting eigenvalues >=lambda. Set y=tr(BP)/n. Then 0<=s<=1 and lambda s<=y. Hadamard's inequality (Gram volume, valid by a positive-definite perturbation for singular P), followed by arithmetic-geometric mean on the two blocks, gives for r<n

    det(P)^(1/n) <= C_r s^(r/n)(1-s)^((n-r)/n)
                   <= C_r (y/lambda)^(r/n).

For r=n, y>=lambda, and det(P)^(1/n)<=1<=y/lambda. Consequently for any bounded measurable q>=0 (essential bound relative to dV, since T is smooth),

    D_q(T) <= G ||q||_infty C_r (x/lambda)^(r/n).

Here the integration step is Jensen for the concave power r/n against the probability sigma. This is a quantitative estimate on each test, not a claim that arbitrary positive currents are limits of smooth tests.

If p is bounded, take any smooth maximizing sequence T_j, with D_p(T_j)->rho by the printed smooth supremum formula. Then

    liminf_j x_j >= L := lambda (rho/(G C_r ||p||_infty))^(n/r) >0.

For general p in D_omega^0 define tau_K=rho_omega(p 1_{p>K}). The exact tail bound in Theorem 12.10.1 gives D_p(T)-D_min(p,K)(T)<=tau_K, uniformly in T, and tau_K->0. Thus for each K>0 with tau_K<rho,

    liminf_j x_j >= L_K := lambda ((rho-tau_K)/(G C_r K))^(n/r)>0.

The already printed trace-budget estimate at lines 39–45 is x_j <= 1-c^(1/n) D_p(T_j). Taking the limit yields

    c <= b (1-L_K)^n,

with 0<L_K<1 whenever a positive-coefficient subsolution as assumed exists. In the bounded case replace L_K by L above (if L>=1 then no such positive c can exist). One can use the supremum of the L_K; the inequalities themselves imply it is <1 if c>0. This strictly improves the qualitative exclusion of c=b for the stated uniform-rank case, even when the linear class threshold kappa_omega(beta) is zero. No existence of a maximizer or compactness of a sequence is needed for this deduction. The same argument gives the bounded-p estimate without separately invoking uniform integrability. The general case with beta vanishing at points and arbitrary nonzero p outside D_omega^0 is not claimed.

Sharpness of the matrix power for r<n: on a flat product of n elliptic curves choose omega with total volume one and dV=omega^n, and beta=lambda times the sum of the first r coordinate forms. For 0<s<1 take the constant diagonal matrix P_s with entries ns/r (first r) and n(1-s)/(n-r) (remaining n-r). Its trace is n; the corresponding constant positive (n-1,n-1) form T_s has sigma=omega^n and is dd^c-closed. For p=1, x_s=lambda s and D_1(T_s)=C_r s^(r/n)(1-s)^((n-r)/n). Thus no larger power of x_s works uniformly for all such smooth tests near x=0. This does not assert sharpness of the subsolution coefficient bound, since these tests need not maximize D_1. The example is a pointwise/test inequality, independent of any existence theorem for a subsolution.

Dependencies: matrix definition in 12.7.1 (permanent A99038CD10B4; docs/sections/a-gauduchon-variational-volume--a-compact-dual-problem-over-gauduchon-currents/index.html, blob 1c0f7efb92914b8a55754bd5039d7319392fb03b, lines 13–35); determinant absolute continuity 12.9.1 (input); 12.10.1 (permanent 41D17749328B, docs/sections/a-gauduchon-variational-volume--integrable-densities-in-the-compact-gauduchon-problem/index.html, blob 1b7a423b1f46d3f1e7b6211c14cd2d4e85cc4a73, lines 10–61); smooth supremum 15.29.1 and trace-budget inequality in 10.18.1. These remain conditional inputs, not transitive certificates. Proposed addition after 10.18.4, no replacement of original hypotheses or tags.

## POME-RESTRICTED-MASS-RANK-DEFICIENT-NEF-BOUND-001

Severity low; status **verified conditional deduction / shorter proof**, not a printed error. Proposition 10.16.9 (source 3CEE22F0, permanent FE6CD72EA03A, lines 137–161) in docs/sections/bott-chern-classes-and-singular-loci--finite-restricted-masses-of-closed-classes/index.html, blob 55a282956e2131880d8200dacbe849c85ef475a0.

Keep the resolved factorization in the printed proof: rho:W_hat->W a Kähler modification, F:W_hat->Q holomorphic into the Kähler resolution of the image of g, P=C F^*kappa_Q smooth closed semipositive, A=P-rho^*g^*eta smooth closed semipositive, dim Q<k, so P^k=0. For any positive representative S of g^*a the positive closed current U=rho^*S+A represents {P}. For each t>0 and any Kähler form h on W_hat,

    integral <(rho^*S)^k> <= integral <U^k>
       <= integral <(U+t h)^k> <= integral (P+t h)^k.

The last bound follows directly from Step 1 of Proposition 10.16.3 (source C72F9777, permanent 5D137EECD5CC, lines 44–53): P+t h is a smooth Kähler representative, and bounded truncations have its cohomological mass. Send t to zero on the right, a finite polynomial in t; it tends to integral P^k=0. Thus the desired vanishing follows by the modification invariance in Step 3, without calling on the general nef volume equality (10.16.6), diagonal mass concentration, or bigness criterion. The point-image case follows by exactly the same Kähler perturbation of the zero class. No limit of measures or interchange of a supremum and a limit is used. More generally, the same proof shows R_Z(b)<=integral b^k for every nef class b, using a Kähler representative of b+t{h}; hence a nef class of zero top intersection has zero invariant independently of the positive-volume case.

Affected dependent: 10.16.9 itself, any later use of dimension-deficient vanishing. Proposed proof simplification only. Factorization, modification invariance, positive multilinear non-pluripolar products and Kähler bounded mass are still inputs. The class-C subspace and Kähler-model facts of lines 10–13 and the classical mass-concentration and volume results of lines 66,115,121 are recorded existing dependencies, not newly proved; resolution is the permitted external input. No attempt to reopen regularization.

## Direct coverage

- §10.16, above exact file/blob, mathematical lines 7–185 (whole direct conditional). Common refinement construction, comparison by adding a closed form, diagonal pushforward factor M=k integral b^(k-1) wedge kappa, descent inequality, nef null-locus union and distinction between intrinsic restricted mass and ambient numerical restricted volume checked. Positive-volume characterization and null-locus equality remain quoted inputs.
- §10.17, docs/sections/bott-chern-classes-and-singular-loci--divisorial-traces-with-bounded-remainder/index.html, blob 336833c05262c42310ca72254358088739b2ca27, mathematical lines 7–150 (whole direct conditional). Lemma 10.17.3 (source 3EFD2D7A, permanent 21B7909B2B52) bounded extension across the divisor, polynomial polarization, exact total-transform coefficients, invariance under metric change and common refinement, strict-current descent and the two distinct blowup examples checked. Nefness of a class with bounded positive potentials (20.4.17) is a named dependency, not reopened. In 10.17.9 the exceptional curve rules out any bounded strictly positive representative by restriction and Stokes, while 10.17.10's section of the exceptional ruled surface has positive intrinsic restricted mass despite lying inside the null locus. No conflict between these versions.
- §10.18, above exact file/blob, mathematical lines 7–123 (whole direct conditional). Trace residual, sign of the exceptional self-intersection, distinction between smooth closure and full Gauduchon-current cone, support of determinant on the zero set of the semipositive representative, and Hopf test quotient t^(1/3) checked. No claim that singular [E] wedge T exists. The underlying adjoint/determinant results remain inputs.
- Selected dependencies §12.7 lines 13–65 and §12.10 lines 10–61. No whole-section or new upstream certification for these dependencies.

No confirmed printed error, substantive new gap, or complete transitive proof-chain certificate in this session. Two deductions, three whole directly read conditional sections, two selected supporting sections; historic first visits not asserted. The current TOC and matrix were compared by section number: 747 each, no missing or extra number. Excluded programmes remain deferred-by-user. No build, tests, CI, automatic site publication, source, registry or permanent-tag changes.
