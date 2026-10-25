# Toric nonanalytic poles: exact multiplier ideals and inradius-based functional stability

**Audit date:** 2026-10-25. **Reviewed main:** b6933b772f41b45918f7e25ed1afbbb1fd892272. **Starting audit-branch checkpoint:** 32c05202d3b751bed383fdafe875ec0e6e63f036. **Scope:** first selected proof-level review of sections 11.41–11.43; no claim of entire-section or upstream mathematical certification.

The following deductions extend two *correct printed results*. The source arguments were read in their integrated, continuous reading edition, not inferred from section titles. No approximation, Bergman kernel, dedicated L2 or Ohsawa–Takegoshi program is invoked.

## POME-TORIC-ROOT-IDEAL-THRESHOLDS-001

**Severity:** low. **Status:** verified conditional deduction; not a false theorem or an existing proof gap. **Proposed action:** optional explicit multiplier-ideal/jumping-number example following Proposition 11.43.10, through a separately reviewable change. **Affected mathematical uses:** comparison of ideal types, Lelong number and Monge–Ampère mass for the nonanalytic isolated poles of section 11.43.

**Pinned source and precise anchors.** Proposition 11.43.10, source label non-kahler-pluripotential-theory-D8F4FD4C, permanent tag 70BE47F32080, and Eq. 11.43.12, source label non-kahler-pluripotential-theory-6D52D243, permanent tag 6654DDDC658F: docs/sections/normalization-and-weak-adjoint-measures--convex-body-criteria-for-varying-references/index.html, blob 22591682db1e501e5359d120ed21606e25c5aba0, physical lines 160–225 (especially 162–169, 194–203). For the bounded comparison of the support and entropy transforms use Lemma 11.43.2, source label non-kahler-pluripotential-theory-124461E4, tag 832F0D3BF7D6, same file lines 27–84. Basic multiplier-ideal integrability convention is verified against Lemma 5.37.1, source label non-kahler-pluripotential-theory-94144E8D, permanent tag C21A2A6F9E07: docs/sections/plurisubharmonic-functions-and-singularities--multiplier-ideals-and-logarithmic-poles/index.html, blob 9256668b88735f821d06b0919466a6a8cba777ed, lines 5–42. This last check concerns a definition and elementary radial integrability only, **not** regularization.

**Statement.** Let \(n\ge2,\ 0<a\le1\), and let \(\Phi_{P_a}\) be the \(\omega_{\mathrm{FS}}\)-psh potential on \(\mathbb P^n\) of Proposition 11.43.10, where
\[
P_a=\{p_i\ge0,\ \sum_i p_i\le1,\ \sum_i\sqrt{p_i}\ge\sqrt a\}.
\]
At \(o=[1:0:\cdots:0]\), for every real \(c>0\) one has the **exact stalk**
\[
\boxed{\quad
\mathcal I(c\Phi_{P_a})_o
 =\bigl(z^\alpha:\alpha\in\mathbb N^n,\
       (\sum_{i=1}^n\sqrt{\alpha_i+1})^2>ac\bigr).\quad}
\]
Thus the complex singularity exponent is
\[
\boxed{\quad c_o(\Phi_{P_a})=n^2/a.\quad}
\]
For \(n=2,a=1\), the first two ideal jumps occur at \(c=4\) and
\(c=(1+\sqrt2)^2=3+2\sqrt2\); the stalk is respectively the unit ideal
for \(c<4\), the maximal ideal for \(4\le c<3+2\sqrt2\), and its square
for \(3+2\sqrt2\le c<(1+\sqrt3)^2\).
The last displayed interval is asserted only up to the next degree-two threshold
\((1+\sqrt3)^2\); no full jumping-number enumeration is asserted.

**Complete local proof.** On a small punctured coordinate polydisc about \(o\),
write \(x_i=\log|z_i|^2=-y_i\) with all \(y_i\ge R>0\). The logarithmic
Fubini–Study potential \(L(x)\) is bounded there. By the bounded
difference \(0\le g_{P_a}-h_{P_a}\le\log(n+1)\), the potential
\(\Phi_{P_a}=g_{P_a}-L\) differs by a bounded function from \(h_{P_a}\).
The equality case of Cauchy–Schwarz in Eq. 11.43.12, valid for **every**
\(y_i>0\), yields
\[
h_{P_a}(-y)=-\min_{p\in P_a}\sum_i p_i y_i
=-\frac{a}{\sum_i y_i^{-1}}.
\]
Indeed the minimizer is \(p_i=a/(y_i^2(\sum_j y_j^{-1})^2)\);
its coordinate sum is at most \(a\le1\), so it is admissible.
In polar coordinates the squared monomial and Euclidean-volume factors
are, up to a harmless constant,
\[
|z^\alpha|^2\,dV_{\mathbb C^n}
 =\exp\bigl[-\sum_i(\alpha_i+1)y_i\bigr]\,dy\,d\vartheta.
\]
Consequently membership of \(z^\alpha\) in the local multiplier ideal is
equivalent to convergence of
\[
I_\alpha(c)=\int_{[R,\infty)^n}
\exp\left[-\sum_i q_i y_i+
\frac{ca}{\sum_i y_i^{-1}}\right]dy,
\qquad q_i=\alpha_i+1.
\]
Put \(M=(\sum_i\sqrt{q_i})^2\). Cauchy–Schwarz gives
\[
(\sum_iq_i y_i)(\sum_i y_i^{-1})\ge M.
\]
If \(ca<M\), the exponent is bounded above by
\(-[1-ca/M]\sum_iq_i y_i\), giving exponential integrability.

If \(ca\ge M\), consider disjoint cubes of fixed side length \(1\)
around points \(y_i=t/\sqrt{q_i}\), for sufficiently large separated \(t\).
At their centers the exponent equals \(t(\sum_i\sqrt{q_i})(ca/M-1)\ge0\).
On each fixed-size cube the exponent differs from its center value
by at most a constant independent of \(t\): its first derivatives are
\(-q_i+ca/[y_i^2(\sum_jy_j^{-1})^2]\), uniformly bounded near that ray.
Each cube therefore contributes a uniform positive amount to the
integral, even at the endpoint \(ca=M\); the sum diverges. This proves
the strict threshold, including equality.

The weight is coordinatewise rotation-invariant. For a holomorphic germ
\(f=\sum_\alpha a_\alpha z^\alpha\), angular orthogonality and Tonelli
give the necessity of the threshold for every nonzero coefficient.
Conversely, the set of good exponents is upward-closed in
\(\mathbb N^n\); by Dickson's finite-generation lemma its monomial ideal
has finitely many generators. A holomorphic power series containing
only good exponents belongs to that monomial ideal (group coefficients
by a finite minimal monomial divisor); the finitely many resulting
holomorphic quotients are bounded on a smaller polydisc. Integrability
of each generator proves sufficiency. Finally the constant monomial
has \(M=n^2\), giving the complex singularity exponent and the explicit
two-dimensional jumps. No valuative theorem, Bergman construction,
approximation program or unproved limit interchange is used.

**Consistency check.** The directional coefficient (11.43.12) along
\(\lambda=(1,\ldots,1)\) is \(a/n\), hence
\(\nu(\Phi_{P_a},o)=a/n\) in the displayed normalizations, while the
global non-pluripolar mass is \(1-\kappa_n a^n\) by (11.43.11).
The exact ideal formula gives additional information invisible to the
single ordinary Lelong number. This is a new deduction, not an
assertion that the original nonanalyticity proof is incomplete.

## POME-CONVEX-INRADIUS-FUNCTIONAL-001

**Severity:** low. **Status:** verified conditional deduction, strengthening a hypothesis of a correct theorem. **Proposed action:** optional corollary to Theorem 11.43.6, not an edit to the printed theorem. **Affected dependents:** varying-reference normalization scalars and supporting probabilities, especially when only a Hausdorff limit body is prescribed.

**Pinned source and anchors.** Theorem 11.43.6, source label non-kahler-pluripotential-theory-CD5F37A4, permanent tag 93F19A4F37D3, Eq. 11.43.7 tag 720678E2362C and Eq. 11.43.8 tag 08069BF2F396: same 11.43 HTML blob 22591682db1e501e5359d120ed21606e25c5aba0, physical lines 114–158. Model/mass normalization is Lemma 11.43.3, tag 59D09F5BD0FB, lines 85–113, and Theorem 11.42.1, source label non-kahler-pluripotential-theory (entry tag 1DCF668EBCCF), docs/sections/normalization-and-weak-adjoint-measures--the-mass-determined-by-the-functional/index.html, blob 9766d5ddf698ae153a6ba635ab9933d471356d67, lines 10–49.

**Statement (also valid for arbitrary directed nets).** Let \(K\subset\Sigma\subset\mathbb R^n\) be a convex body and \(B(c_0,R)\subset K\) a closed Euclidean ball with \(R>0\). Let convex bodies \(K_i\subset\Sigma\) converge in Hausdorff distance \(d_i=d_H(K_i,K)\to0\) along any directed net, and let \(r_i\to r>0\). For all indices with \(d_i<R\),
\[
\boxed{\quad
c_0+(1-d_i/R)(K-c_0)
\subset K_i
\subset c_0+(1+d_i/R)(K-c_0).\quad}
\]
In particular,
\[
(1-d_i/R)^n\mathrm{Vol}(K)
\le\mathrm{Vol}(K_i)
\le(1+d_i/R)^n\mathrm{Vol}(K),
\]
and for the normalization scalars of Theorem 11.43.6 one obtains
\[
\boxed{\quad
\sup_{G\in C(X,\mathbb R)}
|B_i(G)-B(G)|
\le n|\log(r_i/r)|-n\log(1-d_i/R).\quad}
\]
There is **no need to assume a common translated simplex in advance**:
it exists automatically on a tail of the net. Therefore all
solvability, eventual positive mass, \(L^1\)/locally uniform reference
convergence, and singleton supporting-set conclusions of Theorem
11.43.6 hold eventually. Uniformly converging continuous tests have
the same total-variation bound (11.43.8).

**Proof.** For every Euclidean unit vector \(v\), support functions
satisfy \(|h_{K_i}(v)-h_K(v)|\le d_i\).
Since \(B(c_0,R)\subset K\),
\(h_K(v)-c_0\cdot v\ge R\). Consequently
\[
h_{K_i}(v)\ge h_K(v)-d_i
\ge c_0\cdot v+(1-d_i/R)(h_K(v)-c_0\cdot v),
\]
and similarly
\[
h_{K_i}(v)\le h_K(v)+d_i
\le c_0\cdot v+(1+d_i/R)(h_K(v)-c_0\cdot v).
\]
Inclusion of compact convex sets is equivalent to the support-function
inequalities, so the nested homotheties follow; taking Euclidean
volumes gives the quantitative bounds. Their logarithms satisfy
\[
\left|\log\frac{\mathrm{Vol}(K_i)}{\mathrm{Vol}(K)}\right|
\le -n\log(1-d_i/R),
\]
because \(\log(1+x)\le-\log(1-x)\) for \(0\le x<1\).
Using the exact scalar formula
\(B_i(G)=n\log r_i+\log(n!\mathrm{Vol}(K_i))-\log Z_G\)
proves the claimed uniform inequality.

If \(d_i<R/2\), then \(B(c_0,R/2)\subset K_i\) by the first homothety
(or directly by support functions); the same ball lies in \(K\).
Since \(\Sigma\subset B(0,1)\), choosing
\(p_*=c_0\) and \(0<\delta<\min\{R/2,1\}\) gives
\(p_*+\delta\Sigma\subset K_i\cap K\) for all such \(i\).
Thus the common-simplex hypothesis of the printed theorem holds
automatically on this tail. Its remaining claims apply with no
sequential compactness assumption; the estimates themselves are
pointwise and hence valid for directed nets.

This does not address moving blowup centers, nonclosed Hermitian
backgrounds or limits whose convex body loses interior. In particular,
the proof must **not** be used when \(R=0\).

## Actual scope and ledger disposition

Read the integrated statements/proofs of §§11.41.1/.3/.5/.6/.7/.8,
11.42.1/.3/.4 and 11.43.2/.3/.6/.10/.13/.15/.17.
Proof-level analysis was concentrated on the two displayed deductions
and the cited transformations/volume formulas; this is **selected
coverage, not certification** of all these results or their
transitive Monge–Ampère existence/uniqueness inputs. The upstream
closed big-class existence criterion, bounded-product mass identity,
and the full Hermitian scalar PDE theory remain conditional internal
inputs. No false source theorem was found in the selected passages.

All historical Demailly approximation/regularization and dedicated
Bergman, L2, Ohsawa–Takegoshi, multiscale-atlas and positivity-loss
items remain **deferred-by-user**, neither examined nor certified.
No mathematical source/body/registry/canonicalization/permanent-tag/main
changes, build, CI, website publication, or formal proof is claimed.
