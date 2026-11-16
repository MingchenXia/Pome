# Dilated unimodular simplices: normal generation, exact Hilbert functions and reciprocity

**Finding:** `POME-TORIC-DILATED-SIMPLEX-VERONESE-NORMAL-001`  
**Date:** 2026-11-17  
**Severity / classification:** low / **verified conditional deduction** (independent explicit toric model); no incorrect printed theorem asserted, and no original proof certified transitively.  
**Reviewed main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. **Review branch:** `review/mathematical-audit`.

## Exact integrated reading-edition anchors

* `docs/sections/convex-analysis-and-toric-potentials--smooth-lattice-polytopes-and-projective-charts/index.html`, blob `f442a7b663689b97a9b89689b8b7ae8b366a53fe`: Definition **21.8.1**, source label `5FF56EB5`, permanent tag `E11C7A4F96AC`, physical line 11; Lemma **21.8.2(4)**, source `86BADE82`, permanent `41C54729DBFD`, lines 25, 49–55, 84; Theorem **21.8.3**, source `0F7315B0`, permanent `E49F0370E203`, statement lines 108–112, proof/chart/line-bundle passages 118–154.
* `docs/sections/convex-analysis-and-toric-potentials--fans-divisors-and-character-sections/index.html`, blob `7ad2e6dbdd0ce59e1bf08cd9cb3c046e8c87ff6c`: Theorem **21.9.5**, source label `BD98CC5B`, permanent tag `69D3D97E7701`, section basis and asymptotic formula lines 139–149, proof of the monomial basis lines 155–167.
* `docs/sections/convex-analysis-and-toric-potentials--lattice-points-and-volume/index.html`, blob `5d209b7f4d2156c19bc3fb300303405df6321230`: Theorem **21.7.3**, source `364BCD30`, permanent `831AEEB7084F`, lines 58–62 and proof 67–89; **context/normalization only**.

This is a new explicit all-dimensional specialization and stress test of the already integrated theorems, not a claim that their general proofs are complete. Unlike the previously audited non-Delzant singular Veronese-cone model and the dimension-two polygon normal-generation result, the present polytope is **smooth**, and the assertion covers every `n >= 1` and every `d >= 1`.

## Statement, all dimensions

Let `M = Z^n`, `n >= 1`, and let `d >= 1` be an integer. Put

[
P=dDelta_n={minmathbb R_{ge0}^n:sum_{i=1}^n m_ile d},
qquad A=Pcap M.
]

Let `X_P`, `L`, and the character sections be exactly those of §§21.8–21.9. Then:

1. `P` is Delzant, and the character map `T -> P^{|A|-1}` extends to the **degree-`d` Veronese embedding** (
u_d:mathbb P^nhookrightarrow mathbb P^{inom{n+d}{n}-1}). In particular ((X_P,L)simeq(mathbb P^n,mathcal O_{mathbb P^n}(d))).
2. For every `k >= 0` the exact section dimension is
   [
   h^0(X_P,L^k)=#(kdDelta_ncapmathbb Z^n)
   =inom{dk+n}{n}.
   ]
   All multiplication maps
   [
   operatorname{Sym}^k H^0(X_P,L)longrightarrow H^0(X_P,L^k)
   ]
   are surjective. The homogeneous coordinate ring is the `d`-th Veronese subring (mathbb C[x_0,ldots,x_n]^{(d)}); it is integrally closed, so the embedding is **projectively normal**.
3. The Hilbert polynomial is exactly (inom{dk+n}{n}), not merely asymptotic, and the projective degree is (deg X_P=d^n). For `k >= 1`,
   [
   #(operatorname{Int}(kP)capmathbb Z^n)
     =inom{dk-1}{n}
     =(-1)^ninom{-dk+n}{n}.
   ]
   Thus Ehrhart reciprocity holds by an entirely elementary count in this model. The generating function is rational with denominator ((1-t)^{n+1}); its numerator coefficient at `t^j`, `0 <= j <= n`, is
   [
   h^*_j=sum_{i=0}^{j}(-1)^iinom{n+1}{i}inom{d(j-i)+n}{n}.
   ]

## Complete calculation

**Smooth fan and embedding.** At vertex `0` the primitive edges are `e_1,...,e_n`. At vertex `de_j` they are `-e_j` and `e_i-e_j` for `i != j`, a (mathbb Z)-basis: subtracting the `-e_j` column from each `e_i-e_j` column produces the standard basis vectors. Thus the hypotheses of Lemma 21.8.2(4) and Theorem 21.8.3 hold for every `n,d`.

Associate a lattice point (alpha=(alpha_1,ldots,alpha_n)in A) to the `(n+1)`-tuple ((d-sumalpha_i,alpha_1,ldots,alpha_n)). This is a bijection between `A` and nonnegative exponent vectors of total degree `d`. On the torus chart `x_0 != 0` of (mathbb P^n), with `t_i=x_i/x_0`, the Veronese coordinates
(x_0^{d-sumalpha_i}x_1^{alpha_1}cdots x_n^{alpha_n})
are `x_0^d chi^alpha(t)`, hence define the very same projective point as the printed toric character map. The Veronese image is closed (the source is compact) and contains the dense torus image, so it equals `X_P`. The linear system consists of **all** degree-`d` homogeneous monomials; its pullback of the hyperplane line bundle is (mathcal O_{mathbb P^n}(d)). This also directly checks the chart/line-bundle normalization of §21.8.3.

**Exact dimension and surjective multiplication.** The indexed basis of §21.9.5 identifies an element of `H^0(X_P,L^k)` with a monomial of total degree `dk` in `n+1` variables. Stars and bars gives (inom{dk+n}{n}) possibilities. Given a nonnegative exponent vector ((a_0,ldots,a_n)) with total `dk`, distribute its `dk` variable occurrences into `k` successive groups of exactly `d` occurrences. Each group determines a degree-`d` monomial, and their product is the prescribed degree-`dk` monomial. This proves the multiplication map onto for **every** `k`, with no hypothesis about general lattice polytopes or dimension two.

**Normality.** The section algebra generated in degree one is
[
R_d=igoplus_{kge0}mathbb C[x_0,ldots,x_n]_{dk}.
]
The diagonal scalar action of the group (mu_d) of `d`-th roots of unity multiplies each homogeneous polynomial of degree `q` by (zeta^q); hence `R_d=C[x_0,...,x_n]^{mu_d}`. If `u` belongs to the fraction field of `R_d` and is integral over `R_d`, its monic relation also makes it integral over `C[x_0,...,x_n]`. The polynomial ring is a UFD and therefore integrally closed, so `u` is a polynomial. As a quotient of invariants, `u` is invariant under (mu_d), and hence belongs to `R_d`. This proves integral closure. No invocation of any excluded regularization, Bergman or `L^2` argument occurs.

**Degree and reciprocity.** As a polynomial in `k`, (inom{dk+n}{n}) has leading coefficient `d^n/n!`; its projective Hilbert degree is therefore `d^n`, consistent with (c_1(mathcal O(d))^n=d^n). Interior lattice points are exactly (alpha_ige1) for `1 <= i <= n` and (sumalpha_i<dk). Introducing (alpha_0=dk-sum_{i=1}^nalpha_ige1) and subtracting one from all `n+1` coordinates leaves a nonnegative `(n+1)`-tuple of total `dk-n-1`, whose count is (inom{dk-1}{n}) (zero if `dk<=n`). The negative-binomial identity gives the displayed reciprocity. Finally, the `(n+1)`-st finite difference of a polynomial of degree `n` vanishes; multiplying the Hilbert series by ((1-t)^{n+1}) yields the numerator coefficients above and no terms beyond degree `n`.

**Finite independent check, not proof.** Direct exhaustive enumeration of degree-`d` exponent vectors and their `k`-fold sums produced exactly all degree-`dk` vectors in `(n,d,k)=(2,2,3),(3,2,3),(3,3,2)`, with respective counts `28,84,84`. The all-`n,d,k` argument is the grouping proof above; these three checks are not presented as project tests or as general verification.

## Classification, dependency boundary, and proposed change

**Status:** verified conditional deduction / low severity. **No false printed theorem and no new proof gap detected** in the selected printed statements; the direct identification is a model-level independent verification, while the use of the full character-section correspondence as a general theorem remains a cited internal dependency (§21.9.5). Normality itself is verified for this model by an independent invariant-ring argument. The usual polynomial-UFD fact and Hilbert-degree interpretation are elementary algebraic inputs, not research-level analytical assumptions.

**Suggested optional production addition, not applied:** insert a short all-dimensional `d Delta_n` worked example following §21.9.5, clarifying the distinction between `X_P` smoothness, normality of its affine projective cone, and surjectivity of the homogeneous multiplication maps; do not infer these for arbitrary Delzant polytopes from this example alone. Dependents: §21.8.3 projective charts/very ampleness, §21.9.5 character basis and section asymptotics, and downstream toric section-count comparisons. The historical sources and tags remain unchanged.

**Coverage:** newly proof-reviewed **selected model consequences** of already partly sampled §§21.8–21.9; §21.7 is contextual only. **+0 first-visited numbered sections, +0 entirely certified sections**. The main ToC previously counted 25 chapters / 747 numbered sections; this run separately checked the actual chapter-21 ToC as 14 numbered sections, and did not recertify the all-project total. Demailly approximation/regularization and dedicated Bergman, L2, Ohsawa–Takegoshi, multiscale-atlas and positivity-loss programmes remain **deferred-by-user**, not resolved. No main/source/body/registry/tag/build/CI/publication edit or general theorem certification.
