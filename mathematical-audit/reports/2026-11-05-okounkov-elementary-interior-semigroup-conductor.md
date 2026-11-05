# An elementary uniform interior conductor for Okounkov semigroups

Date: 2026-11-05. **POME-OKO-UNIFORM-INTERIOR-SEMIGROUP-CONDUCTOR-001** — **medium / verified repair (audit-only proposed proof replacement)**. The existing printed theorems have **not** been refuted: their saturation arguments cite external results. Here an elementary lattice-semigroup lemma supplies *two* specific replacements. The unrelated Kaveh–Khovanskii counting/volume theorem is **not** replaced, and no full section is certified.

## Exact integrated reading-edition anchors

Production **main**: \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`.

1. \`docs/sections/almost-semigroups/index.html\`, blob \`33898b2963ad0f8b7e30bf414276642f60925b74\`: **Lemma 19.7.25**, source \`sgpt:4791A323\`, permanent tag \`E41D68AC6F7C\`, statement at physical lines **372–376**, proof **381–389**. The precise external premise to replace is the interior lattice-point inclusion ascribed to **[Theorem 1, KK12]**, line **382**.
2. \`docs/sections/the-theory-of-okounkov-bodies--almost-semigroups/index.html\`, blob \`33212916f9ea7754f51f8194cfb76c2fcbe8efab\`: **Theorem 19.2.5**, source \`sgpt:D2CDA8AC\`, permanent \`37D86D761E81\`, statement **92–94**, proof **97–104** and equations **19.2.6–7** at **107–111**. The proof's compact-interior lattice inclusion, attributed to **[Lemma 4.8, WN14]**, has another occurrence in \`docs/sections/almost-semigroups/index.html\` at **401–410**; its reference and historical attribution should remain visible even after a self-contained substitution.
3. Supporting internal geometric lemma: **Lemma 19.7.7**, source \`sgpt:E50EA8A4\`, permanent \`5C4A19C5ED0B\`, same \`almost-semigroups/index.html\`, lines **66–94**. It converts interior lattice inclusion into an inner-body Hausdorff inclusion. **Theorem 19.7.20**, source \`sgpt:282DA4DD\`, permanent \`85641516C8CA\`, same file **299–319**, is *still* an external counting theorem in the original proof of the volume identity; the present argument never claims to derive its general asymptotic-counting conclusion.

Chapter-19 current reading ToC is \`docs/chapters/sections-okounkov/index.html\` (blob \`2d50c059b2f2c487b402a11afdfc0f131400b1e5\`): §19.2 is an introductory section referring forward to §19.7, so the two similarly titled sections are **not** adjudicated as duplicate mathematical entries.

## Self-contained saturation lemma (the new proof)

Let \(M\subseteq\mathbb Z^d\) be an additive semigroup with group of differences
\(\langle M\rangle_{\mathbb Z}=\mathbb Z^d\), and suppose \(K=\overline{\operatorname{cone}(M)}\) is a full-dimensional closed convex cone. Let \(D\subseteq K\) be a closed cone whose unit directions \(D\cap S^{d-1}\) are a compact subset of \(\operatorname{Int}K\). Then
\[
  \boxed{\exists R_D>0:\quad x\in D\cap\mathbb Z^d,\ \|x\|\ge R_D\ \Longrightarrow\ x\in M.}\tag{*}
\]
We may adjoin zero to \(M\) without changing any assertion about large vectors.

**Step 1 (finite polyhedral interior cover).** For every unit vector \(u\in\operatorname{Int}K\), there is a *finite* subset \(F_u\subset M\) such that \(u\in\operatorname{Int}\operatorname{cone}(F_u)\). Indeed, take a small simplex of \(d+1\) points in \(\operatorname{Int}K\) with \(u\) strictly inside its convex hull; each vertex can be approximated arbitrarily closely by an element of \(\operatorname{cone}(M)\), because its closure is \(K\). Each approximation uses only finitely many generators from \(M\), and a sufficiently small perturbation preserves the interior inclusion. Compactness of \(D\cap S^{d-1}\) supplies a single finite \(F\subset M\) with
\[
 D\setminus\{0\}\subseteq \operatorname{Int}P,\qquad P:=\operatorname{cone}(F),
\]
where the inclusion has a *uniform angular margin*. Enlarge \(F\) by a finite set of elements of \(M\) that generates \(\mathbb Z^d\) as a group (possible since \(\mathbb Z^d\) is finitely generated as a subgroup of itself). Still denote the resulting finitely generated semigroup by \(M_0\subset M\) and its closed polyhedral cone by \(P\). The angular margin persists.

**Step 2 (elementary conductor; no normalization theorem).** Write \(M_0=\sum_{j=1}^r\mathbb Z_{\ge0}a_j\), \(a_j\in\mathbb Z^d\), and set
\[
 Q=\sum_{j=1}^r[0,1]a_j,\qquad\mathcal R=Q\cap\mathbb Z^d.
\]
The bounded set \(Q\) has finitely many integral points. For each \(r_0\in\mathcal R\), the equality \(\langle M_0\rangle_{\mathbb Z}=\mathbb Z^d\) allows a representation \(r_0=p_{r_0}-q_{r_0}\) with \(p_{r_0},q_{r_0}\in M_0\). Put \(c=\sum_{r_0\in\mathcal R}q_{r_0}\in M_0\). For every \(y\in P\cap\mathbb Z^d\), choose a real nonnegative conical representation \(y=\sum_j t_ja_j\) and split off integer parts:
\[
 y=\sum_j\lfloor t_j\rfloor a_j+r_y,\qquad
 r_y=\sum_j(t_j-\lfloor t_j\rfloor)a_j\in\mathcal R.
\]
Now
\[
 c+y=\sum_j\lfloor t_j\rfloor a_j
       +p_{r_y}+\sum_{r_0\in\mathcal R,\ r_0\ne r_y}q_{r_0}\in M_0.
\]
Consequently \(c+(P\cap\mathbb Z^d)\subset M_0\). Uniform angular separation of \(D\setminus\{0\}\) from \(\partial P\) means that \(x-c\in P\) for every \(x\in D\) of sufficiently large norm. Such integral \(x\) therefore belongs to \(M_0\subseteq M\), proving (*).

This proof is elementary finite-dimensional convex geometry and finite integer-residue decomposition. In particular it uses neither [Theorem 1, KK12] nor [Lemma 4.8, WN14], and contains **no** regularization, Bergman, weighted-\(L^2\), OT, multiscale, or positivity-loss argument.

## Application A: a complete replacement for the external step of Lemma 19.7.25

Retain the **exact printed hypotheses**: \(S,S'\in\mathcal S'(C)\) both generate \(\mathbb Z^{n+1}\), and \(\operatorname{vol}(S\cap S')>0\). Set \(K=C(S)\cap C(S')\). Since \(S\cap S'\subset K\) and its positive-volume growth implies \(\dim K=n+1\), this cone has nonempty interior. Choose any full-dimensional closed conical sector \(D\) whose nonzero directions lie compactly in \(\operatorname{Int}K\). Apply (*) separately to \(S\) and \(S'\). All sufficiently long lattice vectors in \(D\) belong to **both** semigroups.

Because \(D\) has an interior lattice direction \(v\), the pairs \(mv,mv+e_j\) are in \(D\cap(S\cap S')\) for all large \(m\), where \(e_j\) are the standard basis vectors. Their differences are \(e_j\), so the group generated by \(S\cap S'\) is all \(\mathbb Z^{n+1}\). Thus \(S\cap S'\in\mathcal S'(C)\). For every rational ray in \(\operatorname{Int}K\), choose such a sector \(D\); some large integral multiple of the rational ray is in \(S\cap S'\). Rational rays are dense in \(\operatorname{Int}K\) and \(C(S\cap S')\) is closed, so \(K\subseteq C(S\cap S')\). The reverse inclusion is immediate. This proves **both conclusions** of Lemma 19.7.25 without its quoted external interior-saturation result.

The positive-volume hypothesis cannot simply be dropped: in \(d=2\), with \(C=\{(x,k):0\le x\le2k,\ k\ge0\}\), put
\[
 S=C\cap\{x\le k\}\cap\mathbb Z^2,\quad
 S'=C\cap\{x\ge k\}\cap\mathbb Z^2.
\]
The groups generated by \(S\) and \(S'\) are \(\mathbb Z^2\) (use \((0,1),(1,1)\) and \((1,1),(2,1)\)), but \(S\cap S'=\{(k,k):k\ge0\}\) has zero normalized one-dimensional slice volume and generates only a rank-one group. This is a check on the *hypotheses*, not a counterexample to the lemma.

## Application B: a replacement for the WN14 step in Theorem 19.2.5

Let \(S\in\mathcal S'(C)\), \(K_S=C(S)\), and \(\Delta(S)=\{x:(x,1)\in K_S\}\). If \(E\subset\operatorname{Int}\Delta(S)\) is compact, the directions \(\{(x,1)/\|(x,1)\|:x\in E\}\) form a compact set of directions inside \(\operatorname{Int}K_S\). The sector generated by them obeys (*). Thus for every sufficiently large **integer** \(k\),
\[
 x\in kE\cap\mathbb Z^n\quad\Longrightarrow\quad(x,k)\in S,
\]
a *stronger* result than the printed proof requires (it asserts actual membership in \(S_k\), not merely in its convex hull). Applied to an inner parallel body \(E=\Delta(S)_\delta\), this supplies the lattice-point hypothesis of the already internal Lemma 19.7.7. That lemma's quantitative inner-body inclusion gives
\[
 d_{\mathrm{Haus}}(\Delta_k(S),\Delta(S))\longrightarrow0
\]
exactly as in the existing printed final paragraph. The separate equality
\(\lim k^{-n}|S_k|=\operatorname{vol}\Delta(S)\)
continues to invoke **Theorem 19.7.20**: it is not established by the elementary conductor lemma alone.

## Boundary and dependency audit

The adjective **interior** is essential: the full-lattice subsemigroup \(M=\langle(0,2),(1,1),(1,2)\rangle\subset\mathbb Z^2\) has cone \(0\le x\le k\), yet the boundary point \((0,k)\) is missing whenever \(k\) is odd. Its generated group is \(\mathbb Z^2\) because \((1,2)-(1,1)=(0,1)\) and then \((1,1)-(0,1)=(1,0)\). Thus (*) must **not** be extrapolated to boundary rays. Likewise the full-lattice condition is indispensable: a semigroup contained in the index-two lattice \(\{(x,k):x\in2\mathbb Z\}\) cannot contain all interior ambient lattice points.

**Classification.** Verified audit-only mathematical proof replacement for **two specific non-Hironaka external uses**, not a false theorem or a merged source repair. Keep [KK12], [WN14], and [Kho92] as historical attribution; leave **Theorem 19.7.20** and downstream volume/existence chains unverified. Affected dependents for later separate inspection: §19.7.27–29, Theorem 19.7.32, Corollary 19.2.8, and §19.4's partial Okounkov bodies. No canonicalization, permanent tags, or integrated reading files changed.
