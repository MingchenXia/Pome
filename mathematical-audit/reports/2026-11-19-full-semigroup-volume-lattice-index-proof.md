# An elementary proof of the general Kaveh–Khovanskii slice-counting statement

**Date:** 2026-11-19. **Finding ID:** POME-OKO-GENERAL-LATTICE-INDEX-COUNTING-001. **Severity:** medium (dependency centrality). **Status:** verified repair — an **audit-only proposed replacement proof** for a genuine cited external mathematical input, not a false printed theorem, merged repair, or certification of all dependent theorems.

**Baseline:** main \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`. Integrated reading-edition anchors:

* \`docs/sections/almost-semigroups/index.html\`, blob \`33898b2963ad0f8b7e30bf414276642f60925b74\`: **Theorem 19.7.20**, source \`sgpt:282DA4DD\`, permanent tag \`85641516C8CA\`, physical lines **299–319**. Its printed proof-input is [Theorem 2, KK12], explicitly quoted at lines 299–320.
* \`docs/sections/the-theory-of-okounkov-bodies--almost-semigroups/index.html\`, blob \`33212916f9ea7754f51f8194cfb76c2fcbe8efab\`: **Theorem 19.2.5**, source \`sgpt:D2CDA8AC\`, permanent \`37D86D761E81\`, proof lines **98–104**, volume equality permanent \`4E701FB8EA13\`, lines **106–108**, and Hausdorff convergence permanent \`A57FF2EE0305\`, lines **109–111**. Its corresponding argument also appears in the longer §19.7, lines 397–412.
* **Lemma 19.7.21**, source \`sgpt:DB644801\`, permanent \`DCB8E8464FB6\`, lines **320–341**, uses the slice-counting assertion for the volume pseudometric estimate. **Lemma 19.7.25**, source \`sgpt:4791A323\`, permanent \`E41D68AC6F7C\`, lines **372–389**, is relevant but its interior-conductor step has **already** received a separate, earlier audit-only repair: \`POME-OKO-UNIFORM-INTERIOR-SEMIGROUP-CONDUCTOR-001\` (2026-11-05). That work is not counted as a new discovery here.

## Precise statement and the missing normalizing lattice

Assume the original pointed-cone hypotheses: \(C\subset\mathbb R^n\times\mathbb R_{\geq0}\) is a closed convex cone with \(C\cap\{t=0\}=\{0\}\), and \(S\subseteq C\cap\mathbb Z^{n+1}\) is an additive semigroup. Set
\[
G=\langle S\rangle_{\mathbb Z},\qquad
K=\overline{\operatorname{cone}(S)},\qquad
\Delta=\{x\in\mathbb R^n:(x,1)\in K\}.
\]
By pointedness, \(\Delta\) is a compact convex set whenever \(S\) has a positive-degree element. Use the convention \(\lvert S_N\rvert=0\) for empty slices.

**Strengthening of the printed Theorem 19.7.20.** If \(\operatorname{rank}G\leq n\), then \(N^{-n}\lvert S_N\rvert\to0\). If \(\operatorname{rank}G=n+1\), define
\[
g\mathbb Z=\operatorname{pr}_{n+1}(G),\qquad
\Lambda=\{x\in\mathbb Z^n:(x,0)\in G\}.
\]
Then \(g\geq1\), \(\Lambda\) is a full-rank sublattice of \(\mathbb Z^n\), \(\Delta\) has positive \(n\)-volume, and
\[
\boxed{\lim_{\substack{N\to\infty\\g\mid N}}
  N^{-n}\lvert S_N\rvert
 =\frac{\operatorname{vol}_n(\Delta)}
        {[\mathbb Z^n:\Lambda]}.}\tag{A}
\]
For \(g\nmid N\), \(S_N=\varnothing\), so the unrestricted limsup is the right side of (A). Hence for **every** positive integer \(a\) divisible by \(g\),
\[
\lim_{k\to\infty}(ka)^{-n}\lvert S_{ka}\rvert
=\limsup_{N\to\infty}N^{-n}\lvert S_N\rvert.
\]
If \(G=\mathbb Z^{n+1}\), then \(g=1\) and \(\Lambda=\mathbb Z^n\); (A) is exactly the volume equality in the printed Theorem 19.7.20 and Equation 19.2.6. The dimension-zero convention is \(\operatorname{vol}_0\{\mathrm{pt}\}=1\), with horizontal lattice covolume \(1\).

## Proof

**1. Elementary lattice-coset counting.** Let \(\Lambda\subset\mathbb R^n\) be any full-rank lattice of covolume \(h\), let \(\xi_N+\Lambda\) be arbitrary translates, and let \(B\) be a compact convex set. Then
\[
\lim_{N\to\infty}N^{-n}
  \#\bigl(NB\cap(\xi_N+\Lambda)\bigr)
=\operatorname{vol}_n(B)/h.\tag{B}
\]
Indeed, fix a half-open fundamental parallelepiped \(P\) for \(\Lambda\), of volume \(h\) and diameter \(D\). Translate its tiling by \(\xi_N\). Every tile containing a lattice point of \(NB\) lies in the closed \(D\)-neighborhood of \(NB\); every tile completely inside \(NB\) contributes its marked lattice point. The discrepancy between tile counts and \(\operatorname{vol}(NB)/h\) is bounded by the volume, divided by \(h\), of the \(D\)-neighborhood of the boundary of \(NB\). After scaling by \(N^{-n}\), this is at most \(h^{-1}\operatorname{vol}\{x:\operatorname{dist}(x,\partial B)\leq D/N\}\), which tends to zero because the boundary of a convex body has \(n\)-dimensional Lebesgue measure zero. If \(B\) lies in a lower-dimensional affine space, its outer \(D/N\) neighborhood has volume tending to zero, giving the same conclusion. For \(n=0\) the assertion is immediate. The argument works for **moving** coset translations, not just a fixed lattice shift.

**2. Reuse of the already proved uniform interior conductor.** The 2026-11-05 report \`POME-OKO-UNIFORM-INTERIOR-SEMIGROUP-CONDUCTOR-001\` proves the following lemma by a finite-generator integer-residue calculation: for an additive semigroup \(M\) generating its ambient full-rank lattice \(G\), and for a compact cone of nonzero directions strictly inside \(\operatorname{Int}\overline{\operatorname{cone}(M)}\), all sufficiently long lattice points of \(G\) in that cone belong to \(M\). Its proof chooses finitely many generators whose cone contains the angularly compact sector and which generate \(G\). Writing a lattice point as integral generator multiples plus one of finitely many residual lattice vectors yields a **single conductor** \(c\) such that
\[
c+(\operatorname{cone}(M_0)\cap G)\subseteq M_0\subseteq M.
\]
Deep interior vectors \(v\) satisfy \(v-c\in\operatorname{cone}(M_0)\), proving the lemma. This is precisely the prior verified step; it is **not** a new finding in this report. The argument is invariant under lattice isomorphism and therefore applies to the sublattice \(G\), not just the full \(\mathbb Z^{n+1}\).

**3. Full-rank case.** If \(\operatorname{rank}G=n+1\), then \(K\) is full dimensional; the compact height-one section \(\Delta\) has nonempty interior. Let \(E=\Delta_\delta\) be a nonempty inner parallel convex body for sufficiently small \(\delta>0\). The directions through \(\{(x,1):x\in E\}\) are compactly contained in \(\operatorname{Int}K\). Step 2 therefore implies, uniformly in \(x\) and \(N\),
\[
\{x\in NE:(x,N)\in G\}\subseteq S_N
\quad\text{for all sufficiently large }N.\tag{C}
\]
The reverse outer bound \(S_N\subseteq\{x\in N\Delta:(x,N)\in G\}\) is immediate.

Let \(w\in\mathbb Z^n\) satisfy \((w,g)\in G\). For each \(N=mg\), the lattice points in the degree-\(N\) slice of \(G\) form the coset
\[
G_N=mw+\Lambda.
\]
Consequently (B) and (C) yield
\[
\frac{\operatorname{vol}(E)}{[\mathbb Z^n:\Lambda]}
\leq \liminf_{g\mid N}N^{-n}|S_N|
\leq \limsup_{g\mid N}N^{-n}|S_N|
\leq\frac{\operatorname{vol}(\Delta)}{[\mathbb Z^n:\Lambda]}.
\]
As \(\delta\downarrow0\), the inner bodies \(\Delta_\delta\) increase to the interior of \(\Delta\); their volumes tend to \(\operatorname{vol}(\Delta)\), since \(\partial\Delta\) has measure zero. This proves (A) without a normality assumption, finite generation of \(S\), or any Kaveh–Khovanskii counting theorem.

**4. Lower-rank case.** If \(S\) has no positive-degree elements, all positive slices are empty. Otherwise the projection of \(G\) to the degree coordinate is \(g\mathbb Z\) for some \(g>0\), and the horizontal subgroup \(G\cap(\mathbb Z^n\times\{0\})\) has rank \(\operatorname{rank}G-1\). Every nonempty degree-\(N\) slice of \(G\) is a translate of this fixed lattice, inside an \(O(N)\) bounded subset of its real affine span (because \(S\subset C\) and the height-one section of \(C\) is compact). It therefore contains at most \(O(N^{\operatorname{rank}G-1})=O(N^{n-1})\) candidate lattice points. In particular \(N^{-n}|S_N|\to0\). This includes non-finitely-generated semigroups and \(n=0\) with \(G=\{0\}\).

**5. Convex-body lattice count and dependence.** Taking \(\Lambda=\mathbb Z^n\) and a fixed coset in (B) proves the convex-body count stated as the last part of Theorem 19.7.20; for a general lattice its natural normalized Lebesgue measure is \(h^{-1}\operatorname{vol}_n\). For full-group \(S\) the above yields Equation 19.2.6 directly. Combined with the earlier interior-conductor repair and internal Lemma 19.7.7, it also gives the Hausdorff conclusion (19.2.7) via the already printed inner-body argument. Lemma 19.7.21's Lipschitz estimate may now use this fully proved slice-counting theorem instead of an external existence premise.

## Independent sanity checks and sharp boundaries

* For \(n=1\), \(S=\{(x,k):k\geq0,\ 0\leq x\leq k,\ x\equiv0\pmod2\}\) has \(\Delta=[0,1]\), degree image \(g=1\), horizontal lattice \(2\mathbb Z\), and \(\lvert S_k\rvert=\lfloor k/2\rfloor+1\). Its normalized count tends to \(1/2=\operatorname{vol}(\Delta)/2\), not the full Euclidean volume \(1\). Hence the group-generating hypothesis in the second clause of the printed theorem is essential.
* Restricting that semigroup further to even degrees gives \(g=2\); positive odd-degree slices vanish, while along even degrees the limit is still \(1/2\). This demonstrates why the **limsup** and the phrase **sufficiently divisible** cannot be replaced by an unrestricted limit in the general statement.
* If \(S=\{(0,k):k\geq0\}\) in dimension \(n=1\), the generated group has rank one and \(k^{-1}|S_k|=1/k\to0\), as required.
* A small finite count check for the first two semigroups at degrees \(10,11,50,51,100,101,500\) agrees with these exact formulas; the check is illustrative, **not** verification of arbitrary infinite semigroups.

## Classification, coverage, and follow-up boundaries

This is a **complete, elementary replacement proof for the stated scope of Theorem 19.7.20**, proposed in audit Markdown only. Its historical [KK12] attribution must be retained: historical credit is not an unproved mathematical dependency. The separate previously repaired interior-saturation inputs [Theorem 1, KK12] and [Lemma 4.8, WN14] are **not** logged again. No printed theorem is shown false. This proof is not integrated into the reading edition, and does not certify Theorem 19.7.32's general almost-semigroup limit argument, higher graded-series applications, or all of §19.7.

**Fresh direct coverage:** the complete mathematical body of §19.2, lines **7–134**, including equations, Theorem 19.2.5 and Corollaries 19.2.8/13, was checked for hypotheses, equivalence, count normalization and links to §19.7; selected §19.7 lines **299–341, 369–412** were compared, with Theorem 19.7.20 checked proof-level. **+1 entire directly read section (§19.2), +1 selected partial dependency section (§19.7), +0 certification of full transitive downstream chains.** Historical first-visit status is unreconciled; §19.7's earlier 2026-11-05 audit remains separately counted. The user-excluded Demailly regularization/Bergman/\(L^2\)/OT/multiscale/positivity-loss programme is entirely **deferred-by-user**, neither resumed nor certified. No source, registry, permanent-tag, main, site, CI or build modification is proposed or performed in this report.
