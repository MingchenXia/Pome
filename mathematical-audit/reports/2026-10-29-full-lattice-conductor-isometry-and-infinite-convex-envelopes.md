# Audit report — full-lattice Okounkov semigroups, exact symmetric-difference metric, and infinite convex envelopes

**Date:** 2026-10-29. **Reviewed production main:** b6933b772f41b45918f7e25ed1afbbb1fd892272. **Audit-only branch:** review/mathematical-audit. **Scope:** selected proof passages in §§19.2, 19.7 and 21.6, with a first direct check of Proposition 24.3.2. No source changes, build, CI, website publication, or formal verification. All the dedicated Demailly approximation/regularization/Bergman/L²/Ohsawa–Takegoshi/multiscale/positivity-loss programme remains **deferred-by-user**.

## Pinned reading-edition anchors and provenance

- **§19.2:** docs/sections/the-theory-of-okounkov-bodies--almost-semigroups/index.html, main blob 33212916f9ea7754f51f8194cfb76c2fcbe8efab. Source book **sgpt**. The cone and full-lattice setup occurs on physical lines 10–19 and 54–60; $d_{\rm sg}$, Eq. 19.2.1, source label sgpt:2379D50B and permanent tag **A3A5C96E566B**, lines 22–29; the generating-lattice Definition 19.2.3 source sgpt:C5989909, permanent tag **923345ACA44A**, lines 88–90. Theorem 19.2.5, source sgpt:D2CDA8AC, tag **37D86D761E81**, lines 91–111; Corollary 19.2.8, source sgpt:6A0E7DEB, tag **9FB3E8CE18F7**, lines 113–121; Theorem 19.2.10, source sgpt:870F54F8, tag **2534E787147E**, lines 73–82.
- **§19.7:** docs/sections/almost-semigroups/index.html, main blob 33898b2963ad0f8b7e30bf414276642f60925b74. Theorem 19.7.20, source sgpt:282DA4DD, permanent **85641516C8CA**, lines 299–319, cites the general Kaveh–Khovanskii (KK12) input; Lemma 19.7.25 source sgpt:4791A323, tag **E41D68AC6F7C**, lines 371–386; Lemma 19.7.27 source sgpt:C3725EB6, tag **B1ED8431B1B9**, lines 426–435; Lemma 19.7.28 source sgpt:28FF1674, tag **323C6B6B61D0**, lines 444–471; Theorem 19.7.32 source sgpt:ED83BFDD, tag **1551B679B8B7**, lines 534–645. The direct §19.2.5 proof also quotes WN14 Lemma 4.8 at §19.7 lines 401–410.
- **§21.6:** docs/sections/convex-analysis-and-toric-potentials--compact-convex-envelopes-and-full-mass-limits/index.html, main blob b3b4e34fff767a717df812a381f905589b257fb3. Lemma 21.6.1 source foundations-of-pluripotential-theory:30FFD831, tag **FCDAD9CEC8CE**, statement lines 10–12 and integrated replacement proof lines 14–30. The related Proposition 21.3.3, tag **53A9D470F1AC**, is dependency context only.
- **First direct selected §24.3 check:** docs/sections/problems-in-hermitian-pluripotential-theory--positive-gauduchon-volume-and-bigness/index.html, main blob e64a919194dbc4dbd1739cd02811a5c45e252358. Proposition 24.3.2 source non-kahler-pluripotential-theory:B0E460AB, permanent **32F82EA89236**, physical lines 26–67; equation 24.3.3 tag **C672C5EDF4D5**, lines 62–65. The statement distinguishes the *root volume* from the *bigness threshold*. This is a theorem check, not certification of the cited Gauduchon threshold theorem.

## POME-OKO-FULL-LATTICE-CONDUCTOR-001

**Severity/status:** low / **verified repair, restricted to the full-lattice semigroup dependency**. The printed theorems are not declared false; the full general KK12 theorem for arbitrary subsemigroups remains a genuine external input, not resolved here.

**Precise claim.** Let $C\subset\mathbb R^n\times\mathbb R_{\ge0}$ be closed and convex with $C\cap\{t=0\}=\{0\}$. Let $S\subset C\cap\mathbb Z^{n+1}$ be an additive semigroup whose generated group is all of $\mathbb Z^{n+1}$, as in the printed $\mathcal S'(C)$. Let $K=\Delta(S)=\{x:(x,1)\in C(S)\}$. For every compact $E\subset\operatorname{int}K$, there exists $k_E$ such that
$$
(kx,k)\in S \quad\text{for every }k\ge k_E,\quad x\in E\cap k^{-1}\mathbb Z^n.
$$
In particular, all positive integer levels occur eventually and
$$\lim_{k\to\infty}k^{-n}|S_k|=\operatorname{Leb}_n(K)>0.$$
This proves the parts of the quoted KK12/WN14 consequences needed for full-lattice semigroups without importing those theorems. It is *not* a proof of Theorem 19.7.20 for arbitrary $S\in\mathcal S(C)$, where index/degree-periodicity issues remain.

**Proof of the conductor.** Because $E$ lies strictly inside the full-dimensional closed cone $C(S)$ at height one, and $C(S)$ is the closure of the cone of finite positive linear combinations of members of $S$, a finite set $F_0\subset S$ can be chosen so that $E\times\{1\}$ lies in the ordinary interior of its finite cone. One way to see this is to choose, around each point of $E\times\{1\}$, a sufficiently small simplex with vertices in the *nonclosed* cone of $S$, expand each vertex in finitely many members of $S$, and extract a finite subcover of $E$. As $\operatorname{gp}(S)=\mathbb Z^{n+1}$, finitely many additional members $F_1\subset S$ generate that entire lattice as a group. Put $F=F_0\cup F_1$, $M=\sum_{v\in F}\mathbb N v$, and $D=\sum_{v\in F}\mathbb R_{\ge0}v$.

For any $y\in D\cap\mathbb Z^{n+1}$ write $y=\sum_{v\in F}t_vv$ with $t_v\ge0$ and set
$$r=y-\sum_{v\in F}\lfloor t_v\rfloor v.$$
Then $r\in \mathbb Z^{n+1}\cap\sum_{v\in F}[0,1]v$, a **finite** set $R$. Each $r\in R$ is a difference $a_r-b_r$ with $a_r,b_r\in M$, because $\operatorname{gp}(F)=\mathbb Z^{n+1}$. With $c=\sum_{r\in R}b_r\in M$, every such residue satisfies $c+r\in M$. It follows that
$$c+(D\cap\mathbb Z^{n+1})\subset M\subset S.$$
Let $D'$ be a compact slice of the *interior* of $D$ containing $E\times\{1\}$. Uniform openness of a convex cone gives $(kx,k)-c\in D$ for all sufficiently large integers $k$ and all $x\in E$; these vectors are integral whenever $kx\in\mathbb Z^n$. The displayed conductor inclusion proves the claim. The same argument works in degree dimension $n=0$ with the evident one-dimensional interpretation.

For counts, every $S_k$ lies in $kK\cap\mathbb Z^n$. A fixed compact convex $E$ of positive volume inside $\operatorname{int}K$ is eventually saturated, so $E$ gives a lower bound. For every compact convex body $A$, the translates of the unit cube by $\mathbb Z^n$, compared with inner/outer parallel neighborhoods of $kA$, give
$$k^{-n}\#(kA\cap\mathbb Z^n)\longrightarrow\operatorname{Leb}_n(A).$$
Let $E$ exhaust the interior of $K$ and use the upper bound from $K$. This yields the asserted full-level limit. There is no sequential compactness assumption on a general space or undocumented interchange of the level limit with semigroup regularization.

**Proposed correction/dependents.** The §19.2.5/§19.7.25/.27/.28 arguments can optionally cite this internally proved *full-lattice* saturation lemma in place of the corresponding specialized KK12/WN14 use. Retain the original references as historical attribution, and retain KK12 as a logged general external input for §19.7.20 and any arbitrary-subsemigroup application. No original proof has been replaced in production.

## POME-OKO-SYMDIFF-ISOMETRY-001

**Severity/status:** low / **verified conditional deduction**, using the preceding explicit full-lattice conductor proof. This does not certify all the nested-limit arguments in Theorem 19.7.32.

**Claim.** For any $S,T\in\mathcal S'(C)$ with $K=\Delta(S)$, $L=\Delta(T)$,
$$
d_{\mathrm{sg}}(S,T)=\operatorname{Leb}_n(K\triangle L)
=\operatorname{Leb}_n(K)+\operatorname{Leb}_n(L)-2\operatorname{Leb}_n(K\cap L).
$$
The same formula extends to every pair of **positive-volume almost semigroups** in $\overline{\mathcal S'(C)}_{>0}$, using the continuous Okounkov-body map of §19.7.32. Consequently the pseudometric quotient of this positive-volume space is isometric to the space of full-dimensional compact convex subsets of the ambient level-one slice $P=\{x:(x,1)\in C\}$ with metric $\operatorname{Leb}_n(K\triangle L)$. In particular zero $d_{\rm sg}$ detects exactly the convex body, without requiring the intersection semigroup to have positive volume.

**Proof.** For actual full-lattice $S,T$, the levelwise intersection lies in $k(K\cap L)\cap\mathbb Z^n$. On each compact convex $E\Subset\operatorname{int}(K\cap L)$, the previous conductor gives $kE\cap\mathbb Z^n\subset S_k\cap T_k$ for sufficiently large $k$. When $K\cap L$ has nonempty interior, exhaust its interior by such $E$; the inner/outer cube count proves
$$k^{-n}|S_k\cap T_k|\to\operatorname{Leb}_n(K\cap L).$$
If the intersection has empty interior, it is a lower-dimensional compact convex set; its $O(1/k)$ parallel neighborhood has volume tending to zero, so the same limit is zero. The separate full-level counts and the identity
$|S_k\triangle T_k|=|S_k|+|T_k|-2|S_k\cap T_k|$
then give the exact symmetric-difference formula; crucially the limsup in Eq. 19.2.1 is a genuine limit here.

To pass to almost semigroups, first note that full-dimensional compact convex subsets of a fixed compact $P$ have a *positive-volume-local* equivalence between Hausdorff convergence and convergence in symmetric-difference volume. The forward direction is dominated convergence of indicators away from the boundary (a convex-body boundary is Lebesgue-null). Conversely, from a sequence converging in symmetric-difference measure to a positive-volume convex body, Blaschke compactness gives a Hausdorff-convergent subsubsequence; its limit has the same indicator almost everywhere, hence is exactly the target compact convex body. This uniqueness applies to every subsequence. Thus a $d_{\rm sg}$-Cauchy sequence of full-lattice semigroups whose limiting volume is positive has a unique limiting convex body; the isometry identity survives in the limit by
$$\bigl|\operatorname{Leb}(A\triangle B)-\operatorname{Leb}(A'\triangle B')\bigr|
\le \operatorname{Leb}(A\triangle A')+\operatorname{Leb}(B\triangle B').$$
For any full-dimensional compact convex $K\subset P$, $R_K=\operatorname{cone}(K)\cap\mathbb Z^{n+1}$ has full-lattice generated group: for large $k$, a small ball inside $K$ contains adjacent points of $k^{-1}\mathbb Z^n$, and the same holds at levels $k$ and $k+1$; their differences generate all coordinate directions. Also $\Delta(R_K)=K$. It represents the corresponding quotient class and proves surjectivity.

**Limits.** Positivity of volume is essential to reconstruct bodies from measure convergence; the metric space of positive-volume convex bodies need **not** be complete as bodies collapse to zero volume. Do not infer a uniform global equivalence of the Hausdorff and symmetric-difference topologies at that boundary. The stronger formula is optional; original §19.2.10 and §19.7.32 remain correct. It does not identify semigroups pointwise, only their zero-distance equivalence classes.

**Proposed correction/dependents.** An optional corollary after Theorem 19.7.32 or Lemma 19.7.28, and a metric reinterpretation in §19.2; no duplicate issue, tag merge, or canonicalization change. The general KK12 theorem is not certified.

## POME-CVX-INFINITE-FAMILY-BOUNDARY-001

**Severity/status:** low / **verified conditional deduction**, exhibiting two distinct failures of a *hypothetical* extension of the correct printed finite-family Lemma 21.6.1. Not a confirmed error of that lemma.

The printed assumption $r<\infty$ cannot be dropped merely because all effective domains lie in one compact set.

**Loss of lower semicontinuity and of the conjugate identity.** On $\mathbb R$ take $G_j=\iota_{\{1/j\}}$ for $j\ge4$ (value zero at $1/j$ and $+\infty$ elsewhere), all closed proper convex and supported on $K=[0,1]$. The finite-combination convex envelope of their pointwise infimum is exactly
$$H=\iota_{\operatorname{conv}\{1/j:j\ge4\}}=\iota_{(0,\,1/4]}.$$
It is proper convex but **not lower semicontinuous** at zero. For each $p\in\mathbb R$, $G_j^*(p)=p/j$, and therefore
$$\sup_{j\ge4}G_j^*(p)=\max\{p/4,0\},\qquad
(\sup_jG_j^*)^*=\iota_{[0,\,1/4]} \ne H.$$
This verifies failure of both automatic closedness and the displayed biconjugate identity for the raw infinite convex envelope.

**Independent failure of attainment even when the envelope is closed.** Take $G_j(0)=1/j$ and $G_j(x)=+\infty$ for $x\ne0$. Their pointwise infimum and convex envelope are the closed proper convex indicator $\iota_{\{0\}}$, but its value $0$ at zero is the infimum of finite convex combinations of positive numbers $1/j$ and is not attained. This failure cannot be repaired merely by assuming the resulting envelope is closed.

**Proposed correction/dependents.** Preserve the explicit **finite** hypothesis of Lemma 21.6.1. Any future arbitrary-family convex or toric envelope result needs an independent epigraph/attainment compactness assumption or must explicitly take the lower-semicontinuous convex hull; those are different definitions, and the latter does not restore attainment. This constrains extrapolation of the proof of §21.6.1 and use of Fenchel conjugacy (§21.3.3), but no printed theorem is false.

## Additional first selected review: Proposition 24.3.2

The §24.3.2 proof is consistent with its hypotheses. For a normalized Gauduchon metric with $A_h(\gamma)=1$, the defining positive root-volume infimum gives $\lambda_\mu(\theta)D_\mu(\gamma)\le A_\theta(\gamma)$, Eq. 24.3.3. If $\theta$ is not big, the cited Gauduchon threshold criterion gives $\inf A_\theta/A_h=0$ and normalized minimizing sequences; all such sequences have $D_\mu\to0$. If a minimizing sequence instead has $\liminf D_\mu\ge\delta>0$, its limit satisfies $\kappa_h(\theta)\ge\delta\lambda_\mu(\theta)$, hence is big. No new flaw or new proof claim is registered. The referenced threshold criterion and general volume theory were *not* transitively certified; the surrounding surface problem remains an open question, not a theorem.

## Coverage and status boundaries

**New substantive increments:** selected full-lattice/conductor and metric comparisons in §§19.2.1/.3/.5/.8/.10 and 19.7.20/.25/.27/.28/.32; selected countable-family counterexamples against the *unwritten* extension of §21.6.1; **first** direct selected proof check of §24.3.2. Earlier reviews of §§19.2,19.7,21.6 retain their own records and are not counted as first visits. Nearby §§19.3,21.3 and the original external KK12 theorem are contextual only. **25 current chapters / 747 numbered ToC sections / zero fully certified sections**. No existing confirmed error, gap, dependency or deferred-by-user record has been closed. No source/body/registry/main/tag/site mutation, build, CI, browser verification, or formalization work.
