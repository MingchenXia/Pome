# Mathematical audit — full-degree asymptotic density for almost semigroups and their finite Boolean combinations

**Date:** 2026-11-11. **Production main directly inspected:** b6933b772f41b45918f7e25ed1afbbb1fd892272. **Review branch:** review/mathematical-audit. **Stable finding:** POME-OKO-ALMOST-SG-FULL-DEGREE-DENSITY-001. **Severity:** low. **Status:** verified conditional deduction. This is an additional conclusion, **not** a false printed theorem or a completed section certification.

## Precise integrated statements and anchors

- Main reading edition: docs/sections/almost-semigroups/index.html, Git blob **33898b2963ad0f8b7e30bf414276642f60925b74**. Pointed cone and graded slices (§19.7.15–17), lines **211–230**; the pseudometric is displayed at line **230**. Lemma **19.7.18** (source **sgpt:A07DB3BE**, permanent **7887065F3C7C**) lines **233–254**, establishes the triangle inequality. Theorem **19.7.20** (source **sgpt:282DA4DD**, permanent **85641516C8CA**) lines **299–319** gives the degree-counting theorem, including the **all-degree limit only for semigroups generating the whole lattice**. Lemma **19.7.21** (source **sgpt:DB644801**, permanent **DCB8E8464FB6**) lines **320–336** proves the 1-Lipschitz property; the extension to the pseudometric closure is at **340–344**. Lemma **19.7.25** (source **sgpt:4791A323**, permanent **E41D68AC6F7C**) lines **372–389** proves that intersections of full-group semigroups with positive volume are themselves full-group semigroups. Definition **19.7.31** (source **sgpt:7DD4FA88**, permanent **B0C65454CC85**) lines **530–532** defines positive-volume almost semigroups. Theorem **19.7.32** (source **sgpt:ED83BFDD**, permanent **1551B679B8B7**) lines **535–544, 551–655** supplies the continuous body map and the volume identity.
- The corresponding **distinct integrated statement version** in docs/sections/the-theory-of-okounkov-bodies--almost-semigroups/index.html, blob **33212916f9ea7754f51f8194cfb76c2fcbe8efab**, defines the pseudometric at **22–29**, the Lipschitz volume extension at **32–45**, almost semigroups at Definition **19.2.9** (source **sgpt:E4CCE4D8**, permanent **78B565EC56CF**, lines **68–70**) and the body extension at Theorem **19.2.10** (source **sgpt:870F54F8**, permanent **2534E787147E**, lines **73–82**). The two versioned entries are intentionally retained; identical subject matter is not itself evidence of a canonicalization error.

These exact displayed statements, not only headings, were inspected. Theorem 19.7.20's outside KK12 attribution is a genuine historical/source input in the reading edition. A **separate existing audit** POME-OKO-GENERAL-GRADED-PERIOD-001 provides an internal proof of its exact counting claim, while the separate interior-filling part used in 19.7.25 has not been recertified here.

## New theorem: actual limits, not only limsups

Fix an integer n≥0 and a closed convex cone
$$
C\subset\mathbb R^n\times\mathbb R_{\ge0},\qquad C\cap\{t=0\}=\{0\}.
$$
Write \(A=C\cap\mathbb Z^{n+1}\), \(S_k=\{x\in\mathbb Z^n:(x,k)\in S\}\), and
$$
a_k(S)=k^{-n}|S_k|,\qquad
D_k(S,T)=k^{-n}|S_k\triangle T_k| .
$$
All these sets are finite for k>0, because the slices of C are compact. Let \(\mathcal S'(C)\) denote the additive semigroups in A which generate the **whole** group \(\mathbb Z^{n+1}\), and let \(\overline{\mathcal S'(C)}\) be their pseudometric closure in \(\widehat{\mathcal S}(C)\). No semigroup property is assumed of a limit member.

**Claim A.** For **every** \(S\in\overline{\mathcal S'(C)}\), including members of volume zero,
$$
\boxed{\lim_{k\to\infty}a_k(S)=\operatorname{vol}(S).} \tag{A}
$$
In particular, for a positive-volume almost semigroup, its Okounkov-body volume in 19.7.32 is the actual asymptotic normalized **cardinality at every sufficiently large degree**, not merely the previously defined limsup or the limit of an approximating sequence.

**Claim B.** Given a finite list \(S_1,\ldots,S_r\in\overline{\mathcal S'(C)}\), every fixed Boolean expression formed using finite intersections, unions and set differences inside A has a **genuine full-degree normalized cardinality limit**. In particular,
$$
\boxed{\lim_{k\to\infty}D_k(S,T)=d_{\rm sg}(S,T)}
\qquad (S,T\in\overline{\mathcal S'(C)}). \tag{B}
$$
Thus the limsup in the ambient definition becomes an ordinary limit **on this closure**. Neither assertion gives an effective finite-k rate without additional information.

### Proof of Claim A

By the pseudometric definition of closure, choose genuine full-lattice semigroups \(S^{(j)}\) with \(e_j=d_{\rm sg}(S^{(j)},S)\to0\). For every k,
$$
|a_k(S)-a_k(S^{(j)})|\le D_k(S,S^{(j)}).
$$
The **full-group** conclusion of Theorem 19.7.20, with its exact group hypothesis, gives
\(a_k(S^{(j)})\to v_j:=\operatorname{vol}(S^{(j)})\) through all positive k. Hence
$$
v_j-e_j\le\liminf_{k\to\infty}a_k(S)
\le\limsup_{k\to\infty}a_k(S)\le v_j+e_j.
$$
Lemma 19.7.21 and its explicitly displayed 1-Lipschitz extension imply
\(|v_j-\operatorname{vol}(S)|\le e_j\).
Letting \(j\to\infty\) proves (A), with the explicit interim error bound
$$
\limsup_{k\to\infty}|a_k(S)-\operatorname{vol}(S)|\le 2e_j
\quad\text{for every }j.
$$
No uniform-in-k interchange of two limits was made: j was fixed first, and then the eventual bounds were sent to zero.

### Proof of Claim B

First consider a finite family \(S^{(1)},\ldots,S^{(r)}\) of **genuine** full-group semigroups. For any nonempty index subset \(I\), the intersection \(T_I=\bigcap_{i\in I}S^{(i)}\) is an additive semigroup. If \(\operatorname{vol}(T_I)=0\), its normalized slice cardinalities tend to zero because the nonnegative limsup defining volume is zero. If the volume is positive, each partial intersection in any iterated construction also has positive volume; repeatedly applying Lemma 19.7.25 shows \(T_I\in\mathcal S'(C)\). Theorem 19.7.20 then gives convergence of \(a_k(T_I)\) through **all** positive k. Inclusion-exclusion, or equivalently the multilinear expansion of a Boolean indicator in the indicator functions of the input sets, proves the full-degree limit for every fixed Boolean expression of the \(S^{(i)}\). Complements, if used, are taken relative to A; its full-lattice semigroup also has the required degree limit when \(\mathcal S'(C)\) is nonempty.

For general \(S_1,\ldots,S_r\) in the closure, choose approximants \(S_i^{(j)}\in\mathcal S'(C)\) with \(d_{\rm sg}(S_i^{(j)},S_i)\to0\). At each degree k, changing the inputs changes the membership of a Boolean expression only at a point at which at least one input changes. Therefore for any fixed Boolean expression F,
$$
\left|\,
 k^{-n}|F(S_{1,k},\ldots,S_{r,k})|
 -
 k^{-n}|F(S_{1,k}^{(j)},\ldots,S_{r,k}^{(j)})|
\right|
\le \sum_{i=1}^r D_k(S_i,S_i^{(j)}).
$$
Fix j and take the upper limit over k, obtaining an error at most \(\sum_i d_{\rm sg}(S_i,S_i^{(j)})\). The approximating Boolean expression already has a true limit. For any \(\varepsilon>0\), choose j so this sum is below \(\varepsilon\), then take k large so the approximating sequence is Cauchy. The limsup and liminf of the target expression differ by at most \(2\varepsilon\). They therefore agree. Apply this to symmetric difference F, whose definition has limsup exactly \(d_{\rm sg}\), to obtain (B).

This proof is entirely finite-set algebra **after** the correctly scoped full-group counting input and intersection lemma. It does not infer an all-degree limit for arbitrary semigroups.

## Two sharp scope checks

1. **The whole-group hypothesis cannot be removed.** For n=1, let
\(C=\{(x,k):k\ge0,\ 0\le x\le k\}\) and
$$
S_{\rm even}=\{(x,k)\in C\cap\mathbb Z^2: k\equiv0\pmod2\}.
$$
This is an additive semigroup, but its generated group is \(\mathbb Z\times2\mathbb Z\). For even k, \(a_k(S_{\rm even})=(k+1)/k\to1\); for odd k, \(a_k(S_{\rm even})=0\). Hence the limsup volume is 1 but **the full-degree limit does not exist**. This does not contradict Theorem 19.7.20: its full-degree conclusion expressly assumes generation of the whole lattice. The previously recorded degree-period theorem analyzes such genuine semigroups separately.
2. **Zero pseudodistance gives no quantitative finite-degree rate.** In the same cone set \(S_{\rm full}=C\cap\mathbb Z^2\) and, for an arbitrarily large fixed integer N,
$$
S^{[N]}=S_{\rm full}\setminus\{(x,N):x=0,\ldots,N\}.
$$
The set \(S^{[N]}\) need not be a semigroup, but belongs to the pseudometric closure and satisfies \(d_{\rm sg}(S^{[N]},S_{\rm full})=0\), because their slices differ at only one finite degree. Nevertheless \(a_N(S^{[N]})=0\), while \(\operatorname{vol}(S^{[N]})=1\). This explains why Claim A controls the tail limit and **does not** authorize an effective bound uniformly over large finite k from \(d_{\rm sg}\) alone.

## Audit classification, scope and proposed action

- **Status:** low / **verified conditional deduction**. Theorems 19.7.20 and 19.7.32, Lemma 19.7.21 and the positive-volume intersection lemma 19.7.25 are **not refuted**. No replacement proof or source-body edit is required by the new conclusion.
- **Suggested optional correction:** insert a short corollary after Theorem 19.7.32, stating the full-degree counting limit for the pseudometric closure, with the semigroup-period and no-uniform-rate caveats. This is a **proposed** change to the reading edition, not performed. Do not merge or canonicalize the distinct labels of the §19.2 and §19.7 versions.
- **Dependents worth checking separately:** §19.2.10 and §19.7.32 Okounkov-body continuity; §§19.3–19.6 algebraic and partial Okounkov constructions. The proof does not certify those constructions, all of §19.7, the interior-filling theorem's entire upstream derivation, or any arbitrary-net statement.
- **Actual incremental review:** direct current-main proof and hypothesis review of §§19.7.18, .20–.21, .25, .31–.32 and §§19.2.9–.10; first visit of a previously unreviewed numbered section **0** (both sections had earlier selected audits), whole-section certifications **0**; actual main ToC **25 chapters / 747 numbered sections**. No Demailly approximation/regularization, Bergman, weighted L², Ohsawa–Takegoshi, multiscale-atlas or positivity-loss work was reopened: all remain **deferred-by-user**, not resolved.
- **Operational boundaries:** Markdown audit report only; no source files, body, registry, canonicalization, permanent tags, main, CI, tests, build or website publication were changed or represented as verified.
