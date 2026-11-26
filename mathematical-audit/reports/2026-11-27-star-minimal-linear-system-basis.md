# Minimal linear systems of hyperplane star configurations and arithmetic-growth review

Date: 2026-11-27 (Asia/Shanghai)
Reviewed main: b6933b772f41b45918f7e25ed1afbbb1fd892272
Starting audit head: ef261a7a0a5e4fc01b0fe0efe7f123a06c8358b8

## Finding: POME-STAR-MINIMAL-BASIS-STABILIZATION-001

Severity: low. Status: verified deduction (strengthening; no false printed theorem or missing proof).

**Integrated target.** docs/sections/projective-vanishing-degree-configurations/index.html, blob 8c1603d341f3dc45bf5c7124e396e9f1e8eb235c, §9.69.2, permanent FB7CD3CDDE23, source demailly-complex-geometry:84AEA91E, lines 7–41; specifically the restriction argument at 22–30 and product division at 32–40. Definition 9.56.1 (permanent 145E38D5855C, source 4C4F1642), docs/sections/entire-function-growth-and-algebraic-zero-sets--refined-bounds-for-simultaneous-vanishing-orders/index.html, blob 8ff4e22eede7fe72ba7bbceeb221ef8b2ed20cf7, lines 10–20.

Let \(N>n\ge1\), with \(H_i=(\ell_i=0)\) in precisely the general position of Theorem 9.69.2, and \(S\) their \(n\)-fold intersection set. Put \(P=\prod_{i=1}^N\ell_i\). Let \(W_t\) denote the vector space of forms of the minimum degree \(\omega_t(S)\) with order at least \(t\) at every point of \(S\), including zero. The earlier POME-STAR-SYMBOLIC-EXACT-001 established
\[
d_t=\omega_t(S)=t+(N-n)\lceil t/n\rceil.
\]
The earlier POME-STAR-EXTREMAL-RIGIDITY-001 established uniqueness up to scalar exactly for multiples of \(n\) (when \(n\ge2\)). Neither result is counted again.

**New exact basis in the first block.** For \(1\le t\le n\), put \(d=N-n+t\). Then
\[
W_t=\bigoplus_{|J|=d}\mathbb C\,\prod_{j\in J}\ell_j,\qquad
\dim W_t=\binom{N}{n-t}.
\]
Thus all the indicated products form a basis, not merely two independent examples.

**Proof.** Each product contains at least \(t\) of the \(n\) incident hyperplanes at any point of \(S\). For independence, restrict a linear relation to the intersection of the hyperplanes indexed by the complement of a fixed \(J\) (size \(n-t\)). Every other term contains a factor from that complement and vanishes there. The fixed term is not identically zero on this linear space: by independence, adjoining any one further hyperplane makes a proper hyperplane of the intersection. For an empty complement the same argument is simply nonvanishing of the full product. This gives independence.

For spanning use induction on \(n\), then \(N\) for fixed \(n\). In dimension one the claim is root counting. The case \(t=n\) is the already proved product rigidity. For \(N=n+1\), general position means that the equations form a basis of the space of linear forms; their intersection points are the coordinate vertices. A degree \(t+1\) monomial vanishes to order at least \(t\) at every vertex iff each exponent is at most one. In a polynomial no cancellation of distinct monomials changes these order conditions (use the coordinate chart at each vertex and homogeneity). Thus the squarefree products of degree \(t+1\) span.

Now take \(N>n+1\), \(1\le t<n\). Restrict a given \(F\in W_t\) to \(H_N\). The induced arrangement in \(H_N\simeq\mathbf P^{n-1}\) has \(N-1\) hyperplanes in general position, with star points \(S\cap H_N\). Its minimum degree for order \(t\) is also \(d=(N-1)-(n-1)+t\). By dimension induction the restriction of \(F\) is a linear combination of restrictions of products of \(d\) distinct equations from \(\ell_1,\ldots,\ell_{N-1}\); this includes the case of zero restriction. Lift the combination using the identical products in the ambient space. These lifts are already in \(W_t\). Subtract them from \(F\); the difference is \(\ell_N G\) with \(G\) homogeneous of degree \(d-1\). At each star point of the first \(N-1\) hyperplanes, \(\ell_N\) is nonzero (no \(n+1\) hyperplanes meet). Thus \(G\) vanishes to order at least \(t\) there. Since \(N-1>n\) and its minimum degree is \(d-1\), induction on \(N\) expresses \(G\) as a combination of products of \(d-1\) distinct equations among the first \(N-1\). Multiplying by \(\ell_N\) proves the spanning claim. Notice the necessity of the \(N=n+1\) base: when \(N=n\) the single-point space instead has dimension \(\binom{t+n-1}{n-1}\), and squarefree products need not span. For \(n=1\) both descriptions agree.

**New eventual exact stabilization of each residue class.** Assume \(n\ge2\). Write \(t=qn+r\) with \(q\ge0\), \(1\le r<n\), and put \(q_0=n-1-r\). For every \(q\ge q_0\),
\[
W_{qn+r}=P^{q-q_0}\,W_{q_0n+r}.
\]
In particular the dimension is constant along this entire tail. For \(r=n-1\), \(q_0=0\), so the explicit first-block basis gives, for every \(q\ge0\),
\[
W_{qn+n-1}
=\bigoplus_{i=1}^N\mathbb C\,P^q\prod_{j\ne i}\ell_j,\qquad
\dim W_{qn+n-1}=N .
\]
This holds in all dimensions \(n\ge2\) (including every odd order when \(n=2\)). The case of residue zero was proved earlier, not a new result.

**Proof.** If \(q>q_0\), then \(q+r>n-1\) and \(\lceil (qn+r)/(n-1)\rceil>q+1=\lceil (qn+r)/n\rceil\). The exact initial-degree formula in the induced arrangement on any \(H_i\) gives a strictly larger lower degree than \(d_t\), since \(N-n>0\). Hence every restriction of any \(F\in W_t\) to \(H_i\) vanishes identically. All distinct linear factors divide \(F\), so \(P\) divides it. At each star point \(P\) has exactly order \(n\). The quotient has order at least \(t-n\) and degree \(d_t-N=d_{t-n}\), hence belongs to \(W_{t-n}\). The converse follows by multiplication. Iteration proves the claimed equality, with no assertion that \(q_0\) is the optimal stabilization threshold for every configuration or residue.

The exact degree formula used above can also be recovered by dimension induction and product division as in the earlier report: a nonzero restriction gives the lower bound in dimension \(n-1\), which is at least \(d_t\); if all restrictions vanish, divide by \(P\), reducing \(t\) by \(n\), with the \(t\le n\) case following from degree at least \(N\). Products \(P^q\prod_{j\in J}\ell_j\), \(|J|=N-n+r\) for \(r>0\), attain the bound; multiples of \(n\) use \(P^q\). Dimension one is root counting. This is recalled solely as a dependency, not logged as a new result.

**Correction/dependents.** The printed theorem is correct. No correction needed; an optional corollary would give the exact first-block basis and residue stabilization for later use in symbolic-power interpolation and extremal section counts. No printed downstream theorem is declared repaired. No excluded analytic input is used.

## Further direct coverage

- §9.69: complete integrated mathematical content, physical lines 5–43, blob above. The general-position restriction, distinctness of points, product divisibility, base cases \(N=n\) and \(n=1\), and the asymptotic infimum were checked. Historical partial audit explicitly retained.
- §9.70: docs/sections/arithmetic-values-of-meromorphic-functions/index.html, blob b86bd8674f2b816933bc624627b8bbd3f263e377, physical lines 5–129, whole direct conditional review. Lemma 9.70.2 (BAA8DAF93F9F / EC967494, lines 7–18): counting images and choosing an integer \(H\) gives the strict pigeonhole inequality, including zero rows. Lemma 9.70.3 (08B68F4101B6 / 16EC2C28, lines 22–36): fixed field basis and denominator growth are linear in total degree plus differentiation order; coefficients cost an exponential factor and \(k\) factors of \(O(s+k+1)\). Constant derivation polynomials can be bounded using a degree upper bound \(b\ge1\). Lemma 9.70.4 (5A16550DA466 / 626E1CB4, lines 40–100): discard indices with \(a_i\ge A_0\); their contribution to \(\sum a_i/A_0\) is at least their number, yielding \(\gamma=e-n-\sum_{J}a_i/A_0>0\). This justifies the strict surplus in the rectangular monomial count. The coefficient bounds remain valid when the actual first nonzero jet order \(t\) exceeds the imposed order \(T\), since \(t\ge T\); the product of conjugates gives the \(D-1\) exponent and Cauchy's factorial contributes the remaining exponent one. Clearing denominators preserves nonzero entire functions and does not reduce vanishing orders, including at common zeros of denominators. The fixed distinguished boundaries avoid these zeros by choosing a common generic direction and small radii; Cauchy's estimates are applied to the original coordinate derivatives by a fixed linear coordinate change. Monotonicity of \(u/R(u)^{a_i}\) uses \(1-a_i/A_0>0\). Theorem 9.70.11 (406E1C3E45A6 / 2070D5FF, lines 104–126): finite selection of evaluation functionals in a finite-dimensional polynomial space is legitimate even for an infinite set \(S\). Dividing the Schwarz estimate by \(t\log t\) and sending \(\epsilon\) to zero gives the stated bound, also when all orders vanish (then no nonempty \(S\) can satisfy the premises). The finite-set Schwarz inequality is taken as an internal input from the preceding growth sections; its full upstream proof is not independently certified here. The repeated displayed equations in the terminal alias entries at line 129 are not treated as distinct mathematical statements. No new demonstrated proof gap in the inspected steps.
- §9.71: docs/sections/local-projectivity-from-relative-positivity/index.html, blob f17614b598855bda6fc15f266135d6fe238638cf, whole direct conditional mathematical lines 5–37. Lemma 9.71.1 (A53CEC220C70 / cao-paun-foliations:4BE67CB0). Uniform vertical positivity on the inverse image of a relatively compact neighborhood is valid by properness. The quoted Grauert Euler-characteristic/base-change input at lines 24–30 supplies both local freeness and the fiber map (not one in place of the other). Properness makes images of the coherent cokernel support and rank-failure locus closed. For injectivity the convergent subsequences used at line 34 lie in a fixed compact inverse image over a relatively compact neighborhood; ordinary manifolds are metrizable locally and compact subsets here are sequentially compact. The immersion and proper injectivity give a closed embedding, with the tautological identification supplied by evaluation. Disconnected or zero-dimensional fibers cause no problem. The external Grauert input and the internal vanishing theorem 10.102.1 (excluded proof programme not reopened), as well as Kodaira embedding, remain premises rather than newly certified proofs. The earlier flat-twist obstruction in POME-RELPROJ-FLAT-TWIST-GLOBAL-TAUTOLOGY-001 is not repeated.
- §9.57: docs/sections/finite-type-algebraic-models-and-analytic-structure-sheaves/index.html, blob 26cc1bdcd471c8050a12b1b659be36d21e55db7b, line 5, subject landing page only; no mathematical theorem covered.
- §9.56.1: contextual definition and normalization, lines 7–32 only; not a new full section review.

## Coverage and limits

Fresh main and audit head, AGENTS.md, documentation/proof-expansions.md, audit LATEST.md and README.md were fetched. The actual main docs/chapters/index.html numbered section links and the audit SECTION_MATRIX numbered rows were compared: 747 unique section identifiers on each side, no missing or extra identifiers, no duplicate matrix rows. This is an inventory check, not full mathematical verification. Three whole current direct conditional sections (§§9.69–71), one heading-only subject page (§9.57), one contextual selection. Prior historical coverage remains unreconciled; no first-ever visit is asserted. One new verified elementary deduction, zero new confirmed printed errors or demonstrated gaps, zero full upstream proof-chain certifications. Demailly approximation/regularization and its dedicated Bergman, L2, Ohsawa–Takegoshi, multiscale and positivity-loss programme remain deferred-by-user. No tests, builds, CI, website publication, registry/source/body/tag/main edits or automatic merges.
