# Infinite Ext products, the non-PID injective-dimension boundary, and coherent topology checks

Date: 2026-10-28. **Fresh production main reviewed:** b6933b772f41b45918f7e25ed1afbbb1fd892272. **Scope:** selected mathematical arguments in two previously inventory-only sections, not complete-section verification. The entire user-excluded Demailly approximation/regularization programme, including dedicated Bergman, L², Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof completion, remains **deferred-by-user**, neither inspected nor resolved.

## Current integrated sources, immutable content identifiers and precise anchors

1. **§10.68, injective modules and extension modules.** Main file: **docs/sections/spectral-sequences-support-and-cup-products--injective-modules-and-extension-modules/index.html**, blob **a26517e086ac8ed8c5d590cad04b203a2f602f99**. Proposition 10.68.1, source **demailly-complex-geometry:2FD2BEAD**, permanent tag **4C5B1C59E318**, physical lines **10–25**. Proposition 10.68.2, source **demailly-complex-geometry:A99EA81C**, tag **9253F65EBAE8**, lines **28–56**. Proposition 10.68.3, source **demailly-complex-geometry:112471C8**, tag **E2AECDB17A12**, lines **60–102**. Corollary 10.68.4, source **demailly-complex-geometry:82FDC40D**, tag **7E187B2EFD5F**, lines **106–122**. Theorem 10.68.6, source **demailly-complex-geometry:9119DC26**, tag **04CB406A4809**, lines **126–193**; its exact universal-coefficient sequence 10.68.7 has tag **F019AD1FFDA1**, lines **131–136**. Corollary 10.68.9, tag **978F936E4CF9**, lines **196–204**; Remark 10.68.10, tag **7498A6ED04B4**, lines **208–211**. These are current reading-edition statements and proofs, not guessed source theorem numbers.
2. **§9.51, coherent sections and Stein vanishing.** Main file: **docs/sections/convex-neighborhoods-and-coherent-vanishing--coherent-sections-and-stein-vanishing/index.html**, blob **b25b9fd626fe95865e728c2f180eadb84c00b44b**. Lemma 9.51.1, source **demailly-complex-geometry:1DA19751**, permanent tag **95172CE64D2D**, physical lines **10–38**. Lemma 9.51.9, source **demailly-complex-geometry:301AB7EF**, permanent tag **600DE1CB7CE6**, lines **178–202**. Theorem 9.51.10, source **demailly-complex-geometry:3541C0AE**, tag **7C6C814BF9A5**, lines **204–214**. The §9.51.2 smooth-strict-PSH exhaustion result, source **demailly-complex-geometry:6034E313**, tag **7D7D2E32D0F3**, lines **42–59**, invokes the user-excluded global weighted L² scheme; its proof is **not examined**.

## POME-EXT-INFINITE-CYCLIC-PRODUCT-001

**Severity:** low. **Status:** verified conditional deduction (elementary calculation itself independent of external analysis); **printed Corollary 10.68.4 and Theorem 10.68.6 remain correct**. **Hypotheses:** coefficient ring $\mathbb Z$, arbitrary rather than finitely generated first argument. **Affected dependents:** the finite-generation clause in Corollary 10.68.4, and use of Theorem 10.68.6 for complexes without finite-type homology. **Proposed addition:** optional infinite-generation example immediately after Corollary 10.68.4; do not alter either statement or its permanent tags.

Take
\[
A=\bigoplus_{r=1}^{\infty}\mathbb Z/2^r\mathbb Z,\qquad M=\mathbb Z.
\]
The exact length-one free resolution is
\[
0\longrightarrow\bigoplus_{r\ge1}\mathbb Z e_r
 \xrightarrow{\ \operatorname{diag}(2^r)\ }
 \bigoplus_{r\ge1}\mathbb Z e_r
 \longrightarrow A\longrightarrow0.
\]
Every coordinate map is injective, and its cokernel is precisely the corresponding cyclic group, proving exactness without a finiteness assumption. Applying $\operatorname{Hom}_{\mathbb Z}(-,\mathbb Z)$ turns **direct sums into full products**, giving the cochain differential
\[
\prod_{r\ge1}\mathbb Z\xrightarrow{\ (x_r)\mapsto(2^r x_r)\ }
\prod_{r\ge1}\mathbb Z.
\]
Hence
\[
\boxed{\operatorname{Hom}_{\mathbb Z}(A,\mathbb Z)=0,\qquad
\operatorname{Ext}^1_{\mathbb Z}(A,\mathbb Z)
\simeq\frac{\prod_{r\ge1}\mathbb Z}{\prod_{r\ge1}2^r\mathbb Z}
\simeq\prod_{r\ge1}\mathbb Z/2^r\mathbb Z.}
\]
Coordinatewise reduction is surjective with exactly the indicated kernel (choose representatives independently); there is **no legitimate replacement of this product by a direct sum**. Moreover the element $(1\bmod 2^r)_{r\ge1}$ has infinite order: given nonzero integer $m$, take $r$ with $2^r\nmid m$. Thus even though $A$ is torsion, its first Ext group here is **not** a torsion abelian group. A finite cyclic direct-sum formula cannot be extrapolated by silently changing product to sum or assuming Ext commutes with filtered colimits in the first variable.

For the chain complex $K_0=A$, $K_q=0$ for $q\ne0$, the sequence of Theorem 10.68.6 yields $H^0(\operatorname{TotHom}(K,I))=0$ and $H^1(\operatorname{TotHom}(K,I))\simeq\prod_{r\ge1}\mathbb Z/2^r\mathbb Z$ for any injective resolution $I^\bullet$ of $\mathbb Z$. This is a **conditional application of the printed general derived-Hom theorem**, not a new proof of arbitrary unbounded-total independence. It differs from the **single finite cyclic** example already printed in Remark 10.68.10.

## POME-EXT-NONPID-INJECTIVE-DIMENSION-001

**Severity:** low. **Status:** verified conditional deduction, not a false theorem. **Hypotheses:** general commutative ring versus the specific PID hypothesis in Proposition 10.68.2 and Corollary 10.68.4. **Affected dependents:** attempts to use a two-term injective resolution or degree-one universal-coefficient sequence over an arbitrary commutative ring. **Proposed addition:** optional algebraic counterexample after Proposition 10.68.2; preserve its stated PID restriction.

Let $k=\mathbb Q$, $R=k[x,y]$, $A=R/(x,y)=k$ and $B=R$. The Koszul sequence
\[
0\longrightarrow R\xrightarrow{\ d_2\ }R^2
 \xrightarrow{\ d_1\ }R\longrightarrow k\longrightarrow0,
\quad d_2(t)=(-yt,xt),\quad d_1(u,v)=xu+yv,
\]
is a free resolution. To prove exactness at $R^2$, if $xu+yv=0$, reducing modulo $x$ gives $yv\equiv0$ in $k[y]$, hence $v=xw$, and then $u=-yw$. This also proves no hidden flatness assumption. Applying Hom into $R$ gives the dual complex
\[
R\xrightarrow{\ (x,y)\ }R^2\xrightarrow{\ (u,v)\mapsto-yu+xv\ }R.
\]
Its degree-two cohomology is
\[
\boxed{\operatorname{Ext}^2_R(k,R)=R/(x,y)\simeq k\ne0.}
\]
If $R$ admitted an injective resolution of $B=R$ of length at most one, then $\operatorname{Hom}_R(k,I^\bullet)$ would be concentrated in degrees zero and one, contradicting the displayed nonzero degree-two Ext. Thus **the universal length-one injective-resolution conclusion for a PID does not extend to all commutative rings**. This calculation uses no analytic regularization or unproved literature theorem; it is a counterexample to a hypothetical weakening, not to Proposition 10.68.2 as stated. There is no claim that a two-row universal-coefficient sequence is valid for $R=k[x,y]$.

## Independent selected §9.51 proof inspection, no additional finding ID

- **Lemma 9.51.1**: checked the variable-radius argument directly. The function $r(x)=10^{-2}\inf_y(a(y)+|x-y|)$ is $10^{-2}$-Lipschitz and positive on $V$. A maximal disjoint family of radius-$r$ balls gives a countable $3r_j$ cover; if $z$ lies in one enlarged ball, $r_j\in[r(z)/1.03,r(z)/0.97]$. The original disjoint balls sit inside a Euclidean ball of radius $4r(z)/0.97$, so the elementary packing bound is at most $(4\cdot1.03/0.97)^m<5^m$. The subsequent sheaf cohomological vanishing is **conditional on the separate Čech-to-Godement cover-order result 10.44.15**; that input was not recertified. No arithmetic or subordination defect was found in these selected lines.
- **Lemma 9.51.9**: with cochain restriction-difference $r:A^\bullet\to B^\bullet$, the printed cone differential $D(a,b)=(da,ra-db)$ satisfies $D^2(a,b)=(0,rda-dra)=0$. The short exact cone sequence and the flabby Godement Mayer–Vietoris argument respect the ordinary sheaf difference sign. Continuity and openness on possibly non-Hausdorff quotient cohomology remain **conditional on the cited topological cohomological openness result 2.12.5** and acyclic-basis comparisons; no assertion about Hausdorffness is silently introduced.
- **Theorem 9.51.10**: checked the finite-cover compact restriction mechanism: for finite intersections of concentric relatively compact patches, $\overline{U'_I}\subset U_I$; finitely many compact cochain restrictions and the cited Fréchet cohomological compactness criterion give finite-dimensional Hausdorff cohomology **conditional on** the nuclear/compact-restriction input Corollary 9.51.6, acyclic-cover comparison and Theorem 2.12.5. This is **not** independent certification of Cartan–Serre finiteness or its analytic prerequisites.
- **Excluded dependency boundary**: the weighted $L^2$ existence/fast-weight/holomorphic approximation proof in Lemma 9.51.2, and other results whose proof requires that same dedicated programme, were **not** inspected as part of this session. They stay user-deferred. Historical attribution and stable labels remain unchanged.

## Exact coverage and disposition

First selected proof-level inspection in **§10.68** (explicit projective/injective resolution algebra, universal coefficient cocycles and finitely generated boundary) and **§9.51** (only Lemma 9.51.1, Lemma 9.51.9, Theorem 9.51.10 under recorded prerequisites). These are two previously inventory-only ToC rows, not full-section reviews. **All 747** distinct numbered ToC sections remain in the coverage matrix; **zero** sections or chapters are certified as wholly verified. No new confirmed false existing theorem and no repeated historical issue are asserted. No builds, project tests, formal verification, GitHub Actions, website publication, body/source/registry/canonicalization or permanent-tag modification was performed. Existing unresolved, resolved, and user-deferred statuses must be preserved.

Next rotations should prioritize previously unreviewed, nonexcluded proof-level units in the remaining mathematical project, not revisit the dedicated Demailly/Bergman/L² programme.