# Mixed discriminant: rank-one degeneracy and complete threefold inertia

Date: 2026-11-26 (Asia/Shanghai). Reviewed main: `b6933b772f41b45918f7e25ed1afbbb1fd892272`.
Audit branch parent: `90abeb9241106cfa1552e855bfd23abba484114d`.

## POME-MIXED-DISCRIMINANT-RANK-ONE-THREEFOLD-INERTIA-001

Severity: low. Status: verified conditional deduction (not a false printed theorem or a demonstrated proof gap).

Anchor: `docs/sections/complex-differential-forms-and-positive-currents--currents-and-positivity/index.html`, blob `deba65cba51b4275b523879202e6254db0db2b5c`, Lemma 5.3.3 tag `3D25BAD0C21E` (physical lines 127–174), Lemma 5.3.4 source label `36DBF0BE`, permanent tag `8907196C3513` (179–222). The principal-minor identity and its factor 1/n occur at lines 193–199. The original Lemma 5.3.4 assumes all fixed matrices positive definite and is not refuted.

### General rank-one fixed factor

Let n>=3, A_n=a vv* with a>0 and v a unit vector, and A_3,...,A_(n-1) positive definite Hermitian matrices. Define Q(M,N)=D_n(M,N,A_3,...,A_n) on the real space of Hermitian matrices, using D_n(A,...,A)=det A. Write C(M) for compression to v-perp and B_j=C(A_j). Then

    Q(M,N)=(a/n) D_(n-1)(C(M), C(N), B_3,...,B_(n-1)).

Indeed, use a unitary change of basis with v=e_n; expanding det(t A_n+Y) in t gives det Y+t a det C(Y), and comparison of the coefficient containing each variable once gives (n-1)!/n!=1/n. Compression is surjective (extend a matrix by zero), and each B_j is positive definite by restriction. Lemma 5.3.4 in dimension n-1 gives nondegeneracy and inertia (1,(n-1)^2-1) on the compression space. Thus

    rad Q = {M : C(M)=0},
    inertia(Q) = (1, (n-1)^2-1, 2n-1).

The third entry counts zero eigenvalues. The kernel consists of the last real diagonal entry and the last complex row/column off-diagonal entries; its real dimension is 1+2(n-1). For positive definite H, Q(H,H)>0. The Q-primitive hyperplane Q(M,H)=0 is negative semidefinite, with equality exactly for M in rad Q. Strict negativity on the full primitive hyperplane is impossible.

### Complete threefold classification with one arbitrary semipositive factor

Let n=3 and A=A_3>=0. Diagonalize A unitarily as diag(a_1,a_2,a_3), a_i>=0. Write x_i=M_ii (real), z_ij=M_ij for i<j (complex). Applying the same principal-minor identity to each a_i P_i gives

    3 Q(M,M)
       = a_1(x_2 x_3-|z_23|^2)
         +a_2(x_1 x_3-|z_13|^2)
         +a_3(x_1 x_2-|z_12|^2).

The diagonal real block and the three complex off-diagonal blocks are orthogonal by polarization. A positive a_i contributes two negative real directions in the corresponding complex block; a zero a_i contributes two zero directions. The diagonal block has:

* rank 0 A: zero form;
* rank 1 A, say a_1>0: a_1 x_2 x_3 has one positive, one negative and one zero direction;
* rank 2 A, say a_1,a_2>0: x_3(a_2 x_1+a_1 x_2) again has one positive, one negative and one zero direction;
* rank 3 A: the symmetric matrix with zero diagonal and off-diagonals a_3/2,a_2/2,a_1/2 has determinant a_1 a_2 a_3/4>0 and trace zero. Its three real eigenvalues are nonzero; product and sum force one positive and two negative eigenvalues.

Multiplication by 1/3 does not change inertia. The complete table (positive, negative, zero) is

| rank A | inertia Q |
|---|---|
| 0 | (0,0,9) |
| 1 | (1,3,5) |
| 2 | (1,5,3) |
| 3 | (1,8,0) |

For rank 2 in the displayed coordinates the radical is exactly x_3=0, a_2 x_1+a_1 x_2=0, z_13=z_23=0, with z_12 arbitrary. In rank 1 the general compression description applies; in rank 3 the radical is zero. In every nonzero rank Q(H,H)>0 for positive definite H because some a_i>0 and its corresponding principal two-by-two minor of H is positive. Orthogonal decomposition along H gives negative semidefiniteness on the primitive hyperplane, with nullspace exactly the indicated radical. This is an equality-case statement, not merely the inequality obtained by letting A+epsilon I tend to A.

### Editorial recommendation and affected scope

Keep the hypotheses and proof of Lemma 5.3.4 intact. Add the rank-one and n=3 statements as a separate optional corollary; any use of strict mixed primitive negativity for a semipositive background must check the radical or retain the strict positivity hypothesis. Immediate dependencies: Lemma 5.3.3 and the lower-dimensional Lemma 5.3.4. No downstream theorem declared false; downstream citation graph not fully traversed. Distinct from POME-BT-CONTACT-MIXED-DISCRIMINANT-HALL-RANK-001, which concerns scalar mixed discriminant positivity, not bilinear inertia.

## Actual coverage

* §5.3: selected physical lines 58–222, including closedness, spanning, interior and dual positivity (factor 2^p(n-p)! in line 79 and polarization sign in line 81), mixed determinant normalization and principal-minor induction for strict inertia. Also selected 227–301 (trace and Borel coefficient measures, chart Jacobian, positivity and countable extraction). Not a whole-section or transitive certificate. No new printed theorem error or proof gap established.
* §5.2: selected physical lines 7–126 of `docs/sections/complex-differential-forms-and-positive-currents--complex-manifolds-and-differential-forms/index.html`, blob `886a687d5029616950683fe55defce1fe6854b12`; equation 5.2.1 `E0E563B56BCE`, equation 5.2.2 `284A415465F7`, proposition 5.2.4 `A683A13C69D9`, equation 5.2.5 `B25865120DE7`. Checked Cauchy coefficient/tail bound, rank-chart argument, countable-basis proof and complex orientation Jacobian. Not a whole-section review.
* Fresh main AGENTS.md and documentation/proof-expansions.md, branch LATEST.md and README.md were retrieved. The current chapter 5 index located the two sections; the coverage matrix was not fully reconciled with all chapter indexes this run. Both rows previously recorded legacy-unreconciled; no first-ever visit asserted.
* Demailly approximation/regularization and dedicated Bergman/L2/OT/multiscale/positivity-loss proof-completion programme remain deferred-by-user, not solved. No source or registry edits, builds, software tests, CI, publication or complete transitive proof-chain certifications.
