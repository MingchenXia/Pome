# Mathematical audit: anisotropic ordinary model boxes

Date: 21 October 2026. Reviewed Pome main: b8edb6d5fb0f26f5eae0b7b8c8b8d0230c66d9c6.
Status: three verified conditional deductions, all low severity; no new confirmed erroneous theorem. The mathematical proofs below are conditional on the original integrated box-family identity and do not certify all of its analytic prerequisites.

## Integrated sources and stable anchors

The principal source is docs/sections/multiplier-ideal-envelopes-and-goodness--a-topology-on-ordinary-singularity-types--complete-model-topologies/index.html, blob 68eeaf5ddec20d0b312939d31a14a13ae7b99cbd.

Proposition 18.26.26 has source label non-kahler-pluripotential-theory-136FBC90, permanent tag FC2CCCE62C86, HTML lines 905–974; in particular the box symmetric-difference identity is at lines 956–961. Its analytic inputs include Lemma 18.26.15, label non-kahler-pluripotential-theory-5913A45C, permanent tag D3CEEE21DA5C, starting line 358; Lemma 18.26.16, label non-kahler-pluripotential-theory-141FB985, tag 4C3ACB006A19, line 435; Proposition 18.26.17, label non-kahler-pluripotential-theory-EBFD683C, tag 5F93C15013C0, line 503. Also inspected Corollary 18.26.24, label non-kahler-pluripotential-theory-13C065BA, tag 9829FC8151FB, starting line 817, and Proposition 18.26.25, label non-kahler-pluripotential-theory-80EE7259, tag 085AE6785656, line 866.

The comparison itself is defined in docs/sections/volumes-under-bounded-mass--cauchy-convergence-of-model-potentials/index.html, blob 60816afd3098bf1fc5d1a190c0f21f45924264cf, Definition 13.22.1, source label non-kahler-pluripotential-theory-82BBCEC3, tag A220D62C8412, lines 10–31. Related Proposition 13.22.4, label non-kahler-pluripotential-theory-6F23D12A, tag 38359A611D4C, starts line 55. The general volume comparison is not a metric: it may fail the triangle inequality. Only the special constructed box family has a metric by Proposition 18.26.26.

## Shared identity

Keep the exact hypotheses of Proposition 18.26.26: a connected compact complex manifold of dimension n>=2, a positive Hermitian background satisfying dd^c(omega^q)=0 for 1<=q<n, a positive box B=[alpha,beta]^n with 0<alpha<beta, a fixed admissible 0<t<=t0, and the particular normalized ordinary models p_a. Let R_a=product_j[0,a_j], and let m(a)=product_j a_j. The source establishes

d_omega(p_a,p_b) = t^n [m(a)+m(b)-2m(a wedge b)]
                  = t^n Leb(R_a symmetric_difference R_b).

Indeed, since the underlying one-variable potential g is nonpositive, max(h_a,h_b)=h_(a wedge b), while the volume is U(p_a)=A-t^n m(a). The results below use this exact identity and elementary measure theory; they do not independently reprove the residual Monge–Ampere product or projection invariance.

## POME-IDEAL-BOX-GEODESIC-001

Status: verified conditional deduction. Severity: low. Proposed action: optional corollary following Proposition 18.26.26.

For every a,b in B, the restricted metric space {p_x : x in B} contains a constant-speed minimizing geodesic joining p_a to p_b. Put c=a wedge b. Follow a line segment from a to c, then a line segment from c to b, reparameterizing by the respective rectangle-volume changes.

On either branch the rectangles are nested, so distances are exactly t^n times the absolute change in m. For x on the first branch and y on the second, min(x_j,y_j)=c_j for every j (in every coordinate at least one of a_j,b_j equals c_j). Thus

d(p_x,p_y)=t^n[(m(x)-m(c))+(m(y)-m(c))].

This equals the sum of arclength contributions through c. Because alpha>0, the rectangle volume is strictly monotone along each nonconstant branch. Invert its variation to obtain an isometric parametrization of the interval of length d(p_a,p_b). If one branch is constant, omit it. In dimension at least two, a monotone diagonal path and an axis-by-axis monotone path between comparable distinct parameters give different minimizing geodesics: uniqueness fails.

Do not extrapolate this to the unrestricted volume comparison d_omega, which is not a metric in general.

## POME-IDEAL-BOX-NEGTYPE-001

Status: verified conditional deduction. Severity: low. Proposed action: optional structural corollary.

In the Hilbert space H=L^2([0,beta]^n, Lebesgue), define F(a)=t^(n/2) 1_(R_a). Since indicator differences take values in {-1,0,1},

d_omega(p_a,p_b)=||F(a)-F(b)||_H^2.

Thus sqrt(d_omega) is a Hilbert metric on this restricted family. For any finite a_i in B and real c_i with sum_i c_i=0, expanding squares gives the exact conditional-negative-type identity

sum_(i,j) c_i c_j d_omega(p_(a_i),p_(a_j))
    = -2 ||sum_i c_i F(a_i)||_H^2 <= 0.

Moreover, exp(-s d_omega(p_a,p_b)) is a positive semidefinite kernel for every s>=0. A self-contained argument: write v_i=F(a_i) and expand

exp(-s||v_i-v_j||^2)
=exp(-s||v_i||^2)exp(-s||v_j||^2)
 sum_(k>=0) (2s)^k/k! <v_i,v_j>^k.

For every k, the matrix of powers of inner products is the Gram matrix of Hilbert tensor powers v_i^(tensor k). Partial sums are positive semidefinite; conjugating by the positive diagonal weights and taking an entrywise limit retains positive semidefiniteness. This proof does not require an external kernel theorem.

## POME-IDEAL-BOX-ISORES-MIDPOINT-001

Status: verified conditional deduction. Severity: low. Proposed action: optional caveat/corollary on the fixed-residual-data strata.

Fix alpha^n<P<beta^n. In the slice F_P={p_a: a in B, m(a)=P}, Proposition 18.26.26 gives the *same full residual measure on the pole set* and the same two singularity volumes for all members. Yet for distinct a,b in the slice and every c in the slice,

d(p_a,p_b)=d(p_a,p_c)+d(p_c,p_b) implies c=a or c=b.

Proof: equality for symmetric-difference L1 distances of three indicator functions forces the pointwise triangle inequality to be equality a.e., hence R_a intersection R_b is contained in R_c and R_c is contained in R_a union R_b up to null sets. If an origin rectangle R_c is contained in the union of two origin rectangles R_a,R_b, then R_c is contained in at least one of them. Otherwise some coordinate i has c_i>a_i and some coordinate j has c_j>b_j. Whether i=j or i differs from j, a positive-measure subrectangle in R_c then lies outside both R_a and R_b. Contradiction. Since Leb(R_a)=Leb(R_b)=Leb(R_c)=P, containment forces equality of the rectangles and thus c=a or c=b. In particular, distinct endpoints have no nontrivial metric midpoint in this stratum. The full box is geodesic, but its constant-residual-data slices are not geodesic in the induced metric.

An exact example at n=2 is a=(2,1/2), b=(1,1), c=(3/2,2/3), with identical products 1 but distances divided by t^2 equal 1, 1/2 and 2/3 for (a,b), (a,c), (c,b) respectively. The triangle inequality is strict: 1<7/6.

## Scope, dependencies and workflow

This session inspected the selected integrated proof steps and checked the algebraic implications of the displayed source identity. Unverified upstream analytic inputs include the full Bedford–Taylor product and its truncation limits, singularity-type invariance of residual measures, equality of volume under ordinary model projection, and the positive-volume separation theorem. No entire section or chapter is certified. No original Pome statement is classified false by these findings. The new claims are optional deductions, not replacement proofs or verified repairs. Historical attribution and permanent tags remain unchanged. The user-excluded Demailly approximation/regularization and dedicated Bergman/L2/Ohsawa–Takegoshi/multiscale/positivity-loss work was not reopened; older notes remain deferred-by-user.

Local exact rational check: 425 box-pair path equalities, 3 Gram/negative-type checks, and 234 fixed-volume strict-triangle examples. These checks supplement, not replace, the written proof. Full Pome tests, build, CI, publication and formal mathematical verification were not run.

Source/body/registry/canonicalization edits are proposals only. This is an audit note for review/mathematical-audit, not an edit to main, canonical source repositories, published docs, or permanent tags.
