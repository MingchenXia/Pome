# Positive-sum wedge criterion for a common complex null foliation

**Stable finding ID:** \`POME-NULL-POSITIVE-SUM-WEDGE-FOLIATION-001\`; **date** 2026-11-12; **severity/status** low / **verified conditional deduction**. No printed theorem is refuted. Production main \`b6933b772f41b45918f7e25ed1afbbb1fd892272\` examined.

**Exact integrated reading edition:** \`docs/sections/integral-leaves-of-constant-rank-null-distributions/index.html\`, blob \`564667ab5d008b0ffa1d29f5b7ecc578c19d2f04\`.

| Pome statement | Original source label | Permanent tag | Physical lines actually checked |
| --- | --- | --- | --- |
| Proposition 7.15.1 (Frobenius) | \`klimek-pluripotential-theory:8305DF08\` | \`0E3D24D5541E\` | 10–34 |
| Proposition 7.15.2 (complex graph) | \`klimek-pluripotential-theory:D96E34E4\` | \`C2EBFD69CEA4\` | 38–46 |
| Theorem 7.15.3 (common null foliation) | \`klimek-pluripotential-theory:FB2152E8\` | \`8FE75D79B9CA\` | 50–79 |
| Proposition 7.15.4 (two-form rank test) | \`klimek-pluripotential-theory:3B18B0CF\` | \`992E9692EF3B\` | 83–107 |
| Example 7.15.5 (indefinite obstruction) | \`klimek-pluripotential-theory:D21B8572\` | \`849194DD5398\` | 114–124 |

## Exact new mathematical deduction

Let \(\Omega\subset\mathbb C^n\) be open and let \(\beta_1,\ldots,\beta_s\) be **real semipositive \(d\)-closed \(C^\ell\) \((1,1)\)-forms**, with \(\ell\ge1\). Fix **strictly positive** real weights \(t_j\). Set \(B=\sum_jt_j\beta_j\). Assume that for the same integer \(0\le r\le n\) at every \(x\in\Omega\),
\[
 B^r(x)\ne0,\qquad B^{r+1}(x)=0,
\]
with \(B^0=1\) and the second condition vacuous for \(r=n\).

Then \(D_x=\bigcap_j\ker\beta_j(x)\) is a complex \(C^\ell\) distribution of **constant rank \(n-r\)**. It is involutive; its maximal connected leaves have intrinsic complex manifold structures and injective holomorphic immersions into \(\Omega\). If \(\beta_j=dd^cu_j\) with real \(u_j\in C^{\ell+2}\), each \(u_j\) is pluriharmonic on every leaf and each ambient partial derivative \(\partial_{z_a}u_j\) is holomorphic along the leaf.

The criterion does **not** impose constant rank on any individual \(\beta_j\), unlike what one might unnecessarily impose when applying the source's general common-nullspace theorem. The positive-sum wedge condition is also equivalent pointwise to: *some* mixed wedge of degree \(r\) of the \(\beta_j\) is nonzero, whereas **all** mixed wedges of degree \(r+1\) vanish. The nonzero mixed choice may vary with the point.

## Detailed proof: no cancellation, kernels and brackets

In a unitary frame let \(H_j\) be the positive-semidefinite Hermitian coefficient matrix of \(\beta_j\). Put \(H=\sum_jt_jH_j\). For each \(v\in\mathbb C^n\),
\[
 \langle Hv,v\rangle=\sum_jt_j\langle H_jv,v\rangle.
\]
All summands are nonnegative and every \(t_j>0\), so \(\langle Hv,v\rangle=0\) precisely when \(\langle H_jv,v\rangle=0\) for **every** \(j\). For a positive-semidefinite Hermitian matrix, vanishing of this quadratic form is equivalent to membership in the kernel. Thus
\[
 \ker H=\bigcap_j\ker H_j.
\]
The wedge powers of a positive Hermitian \((1,1)\)-form vanish in degrees strictly above its complex matrix rank and are nonzero in all lower degrees. The hypotheses yield \(\operatorname{rank}H(x)=r\) everywhere and consequently \(\dim_\mathbb C D_x=n-r\).

For any \(k\), the expansion \(B^k=\sum_{j_1,\ldots,j_k}t_{j_1}\cdots t_{j_k}\,\beta_{j_1}\wedge\cdots\wedge\beta_{j_k}\) is a **sum of positive \((k,k)\)-forms**. There is no cancellation: pairing with any strongly positive complementary decomposable test form gives a sum of nonnegative real numbers. In particular vanishing of \(B^{r+1}\) is equivalent to vanishing of *all* degree-\(r+1\) mixed products, and nonvanishing of \(B^r\) means at least one degree-\(r\) mixed product is nonzero. This verifies the alternative wedge test, including boundary values \(r=0,n\).

Since \(B\) is \(C^\ell\) and has constant rank, an invertible-minor argument constructs local \(C^\ell\) frames for its kernel. Let \(X,Y\) be local \(C^1\) sections of \(D\), and \(Z\) any local vector field. Closedness gives
\[
 0=dB(X,Y,Z)=-B([X,Y],Z);
\]
each other exterior-derivative term either contains a null argument or differentiates an identically zero pairing. So \([X,Y]\in D\). Proposition 7.15.1 supplies local integral plaques and injectively immersed maximal real leaves, and Proposition 7.15.2 converts their complex tangent spaces into complex leaf structures. This is the *intrinsic* leaf topology, not a claim that global leaves are embedded.

For \(\beta_j=dd^cu_j\), its pullback to any leaf vanishes, proving leafwise pluriharmonicity. For a holomorphic local leaf immersion \(\psi\), the Hermitian null pairing gives
\[
 \partial_{\bar t_b}((u_j)_{z_a}\circ\psi)
 =\sum_k(u_j)_{z_a\bar z_k}(\psi)\,
               \overline{\partial_{t_b}\psi_k}=0,
\]
establishing holomorphy of every ambient first holomorphic derivative on the leaf.

## Exact example with both individual ranks jumping

On \(\mathbb C^3\) let
\[
 u_1=|z_1|^4+|z_2|^2,\qquad u_2=|z_1|^2+|z_2|^4,\qquad \beta_j=dd^cu_j.
\]
After omitting their identical positive \(dd^c\) normalization factor, the Hermitian matrices are
\[
 H_1=\operatorname{diag}(4|z_1|^2,1,0),\qquad
 H_2=\operatorname{diag}(1,4|z_2|^2,0).
\]
The rank of \(H_1\) jumps from \(1\) to \(2\) across \(z_1=0\), and that of \(H_2\) jumps from \(1\) to \(2\) across \(z_2=0\). However,
\[
 H_1+H_2=\operatorname{diag}(1+4|z_1|^2,1+4|z_2|^2,0)
\]
has rank **exactly 2 everywhere**. Its second wedge is nowhere zero and its third wedge is zero, so the common leaves are precisely the complex lines \(\{z_1=c_1,\ z_2=c_2\}\). Thus neither factor needs constant rank, and the criterion gives the correct regular foliation directly.

**Necessity of positivity and rank hypotheses:** if \(\beta_1=dd^c|z_1|^2\), \(\beta_2=-dd^c|z_1|^2\), then \(B=\beta_1+\beta_2=0\), but the common kernel has positive codimension; without semipositivity sum-rank cancellation invalidates the assertion. Signed weights likewise permit cancellation even with positive forms. With only \(dd^c|z_1|^4\), the rank genuinely changes at \(z_1=0\), so the fixed-degree wedge condition cannot be omitted.

## Audit status, proposed correction and dependency boundaries

**Low / verified conditional deduction, no theorem error or source correction required.** The Hermitian kernel identity, wedge positivity, bracket computation and explicit model have been proved directly. The general passage from a \(C^\ell\) involutive distribution to immersed complex leaves uses the printed Frobenius and complex-graph theorems (§§7.15.1–2), whose selected proof steps were examined but whose entire analytic dependency chains were not independently certified. Do **not** reclassify this as an unconditional repair or full certification of Theorems 7.15.1–4.

**Optional proposed addition (not applied to production):** a corollary directly after Theorem 7.15.3 recording this positive-sum wedge criterion and the individual-rank-jump example, preserving canonical tags and historical attribution.

**Affected dependents:** applications of the common nullspace/foliation framework (§§7.15.3–4) to *families of semipositive closed forms*, including verifying null foliations when only the sum has constant rank. Not claimed to repair other statements. Prior separately recorded reducibility, irrational-leaf, rank-jump and nonclosed-contact warnings were checked for overlap and are not duplicated.

**Actual scope:** selected further proof-level inspection in §7.15 (source lines 10–124), a previously partially reviewed section; **0 newly first-visited numbered sections, 0 entire sections or theorem chains certified**. ToC remains 25 chapters/747 sections. The author-excluded Demailly approximation/regularization plus dedicated Bergman, \(L^2\), Ohsawa–Takegoshi, multiscale and positivity-loss completion programme remains **deferred-by-user**, not resolved/certified. No build, CI, formal verification, production/main/source/registry/tag changes or site publishing.