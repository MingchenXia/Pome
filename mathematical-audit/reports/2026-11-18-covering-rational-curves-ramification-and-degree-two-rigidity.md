# 2026-11-18: Ramification budget and degree-two rigidity for dominating rational-curve families

**Finding:** POME-FOL-COVERING-CURVE-RAMIFICATION-DEGREE2-001  
**Severity / status:** low / **verified conditional deduction**, not a false printed theorem or a repair of the movable-cone input.  
**Reviewed main:** b6933b772f41b45918f7e25ed1afbbb1fd892272.  
**Branch reviewed before writing:** review/mathematical-audit, previously existing; no reset.  
**Integrated reading edition:** docs/sections/tangent-slopes-and-covering-rational-curves/index.html, blob 88c8dc4651dc7d9cd21609d3d453521f97e0190d.  
**Source and permanent anchors:** Lemma 9.76.1: cao-paun-foliations:AA1A5BE2 / 4F2E71913C12, physical line 12, proof lines 17–27, especially the determinant section at 18–24. Corollary 9.76.2: cao-paun-foliations:0B126172 / 8876081BAAEC, lines 32–58 (consequence only). Section tag F15BB5328B60.  
**Dependents and contexts:** §9.75.4 (positive-slope foliation consequences), §9.76.2 (uniruled/pseudoeffective equivalence), §9.77.1 (deformation corollary); their global proof chains are not certified here.

## Exact additional statement

Let \(X\) be a compact Kähler \(n\)-fold and \(S\) a smooth connected complex manifold. Let
\[
F:\mathbb P^1\times S\longrightarrow X
\]
be holomorphic and dominating, with every \(f_s=F|_{\mathbb P^1\times\{s\}}\) nonconstant. Denote the common curve class by \(\alpha\), and write
\[
d=-K_X\cdot\alpha=\deg f_s^*T_X.
\]
Choose \(s\) for which there is \(z_0\in\mathbb P^1\) with \(dF_{(z_0,s)}\) surjective and \(df_s|_{z_0}\ne0\). Such pairs form a nonempty open subset, by dominance and generic smoothness.

For each \(p\in\mathbb P^1\), let \(r_p\) be the common vanishing order of the local components of the vector-bundle map \(df_s:T_{\mathbb P^1}\to f_s^*T_X\). Equivalently, choose a local nowhere-zero tangent frame and a target-bundle frame and take the minimum of the orders of its \(n\) coefficient functions; this is independent of the frames. Only finitely many \(r_p\) are nonzero. Then
\[
\boxed{\qquad 0\le\sum_{p\in\mathbb P^1}r_p\le d-2.\qquad} \tag{A}
\]
More precisely, there are \(n-1\) global holomorphic sections \(v_2,\ldots,v_n\) of \(f_s^*T_X\), arising from parameter variations of \(F\), such that
\[
D=df_s\wedge v_2\wedge\cdots\wedge v_n
\in H^0\!\left(\mathbb P^1,\det(f_s^*T_X)\otimes
T_{\mathbb P^1}^{*}\right)
\]
is not identically zero. Its effective zero divisor has **exact total degree \(d-2\)**, and contains the ramification divisor \(\sum r_p[p]\). This is a geometric interpretation, not an assertion that the divisor of \(D\) is independent of the chosen complementary sections.

In particular, if \(d=2\), then \(D\) is nowhere zero and
\[
\boxed{f_s^*T_X\simeq\mathcal O_{\mathbb P^1}(2)
\oplus\mathcal O_{\mathbb P^1}^{\oplus(n-1)},\qquad
N_{f_s}\simeq\mathcal O_{\mathbb P^1}^{\oplus(n-1)}.} \tag{B}
\]
Here \(N_{f_s}=\operatorname{coker}(df_s)\) is a genuine locally free normal bundle since \(f_s\) is then an immersion. Thus a minimal-anticanonical-degree member of a dominating family is an unramified free immersion with trivial normal bundle, without any assumption that it is embedded.

## Complete proof of (A) and (B)

Dominance gives a point at which \(F\) has differential of rank \(n\). Since the restriction to every fiber is nonconstant, the locus where its fiber differential has rank one is dense in the product (the critical locus on each fiber is discrete). We can select \((z_0,s)\) where both conditions hold.

The derivative of \(F\) with respect to an arbitrary fixed parameter tangent vector \(w\in T_sS\) defines a global holomorphic section \(v_w\) of \(E=f_s^*T_X\) on the entire \(\mathbb P^1\). Because the differential of \(F\) is surjective at \((z_0,s)\) and \(df_s(z_0)\ne0\), choose \(n-1\) such vectors \(w_i\) so that the values of \(df_s\) and \(v_{w_i}\) at \(z_0\) span \(E_{z_0}\). These become \(v_2,\ldots,v_n\). In the case \(n=1\) the list is empty.

The determinant \(D\) is consequently a nonzero holomorphic section of
\[
L=\det E\otimes T_{\mathbb P^1}^{*},
\qquad
\deg L=\deg E-2=d-2.
\]
The divisor of a nonzero holomorphic section of a line bundle on the projective line is effective of total degree \(\deg L\). This simultaneously reproves the numerical part \(d\ge2\) of the printed lemma. At each point \(p\), if every local component of \(df_s\) vanishes to order at least \(r_p\), then the determinant \(D\) also vanishes to order at least \(r_p\): in a local frame every term in the wedge determinant contains one component of \(df_s\). Summing gives (A).

If \(d=2\), then \(\deg L=0\) and the nonzero section \(D\) has no zeros. Therefore the bundle homomorphism
\[
T_{\mathbb P^1}\oplus\mathcal O_{\mathbb P^1}^{n-1}
\longrightarrow E,\qquad
(\xi,c_2,\ldots,c_n)\longmapsto
df_s(\xi)+\sum_{i=2}^n c_i v_i
\]
has nowhere vanishing determinant, hence is an isomorphism at every point, and so is a holomorphic vector-bundle isomorphism. It identifies \(df_s\) with inclusion of the \(T_{\mathbb P^1}\simeq\mathcal O(2)\) summand. This proves that \(df_s\) never vanishes and that its normal quotient is trivial, establishing (B). Nothing about cone duality, MRC quotients, resolution, or a Demailly approximation theorem was used.

**Scope of the parameter choice.** The proof applies to every \(s\) for which at least one \((z,s)\) has surjective \(dF\) and nonzero \(df_s\), not automatically to every special member of the family. Constancy of \(d\) alone does not justify a claim about the normal bundle of a singular or nondominating special fiber.

## Sharp ramification model in all dimensions

For any integer \(m\ge1\), let \(T\) be a compact complex torus of dimension \(n-1\), with \(T\) a point for \(n=1\), and set \(X=\mathbb P^1\times T,\ S=T\). Let
\[
F([z_0:z_1],t)=([z_0^m:z_1^m],t).
\]
This is a dominating holomorphic family. For each \(s=t\), the anticanonical degree is \(d=2m\), since \(K_T\) is trivial. The map \([z_0:z_1]\mapsto[z_0^m:z_1^m]\) has precisely two ramification points, each of order \(m-1\). Therefore
\[
\sum_pr_p=2m-2=d-2,
\]
so the constant one in (A), and its additive threshold \(2\), are sharp even for positive-dimensional parameter spaces and compact Kähler targets of any complex dimension.

## Equality does not force a global product

Take \(X=\mathbb F_m=\mathbb P_{\mathbb P^1}(\mathcal O\oplus\mathcal O(m))\) for \(m>0\). Let \(E_0=\mathcal O\oplus\mathcal O(m)\), and let \(S=\operatorname{Fr}(E_0)\) be its holomorphic frame bundle over \(\mathbb P^1\). This is a connected complex manifold (its fiber \(\mathrm{GL}_2(\mathbb C)\) is connected). Each frame determines a biholomorphism from a fixed \(\mathbb P^1\) to the corresponding projective fiber of \(X\). Evaluation gives a globally defined dominating holomorphic map \(F:\mathbb P^1\times S\to X\), with all fiber maps nonconstant. The fiber tangent sequence, restricted to one fiber, splits:
\[
0\to\mathcal O(2)\to f_s^*T_X\to\mathcal O\to0,
\qquad H^1(\mathbb P^1,\mathcal O(2))=0.
\]
Hence \(d=2\) and the normal bundle is trivial as predicted. But \(\mathbb F_m\) for \(m>0\) has a section of self-intersection \(-m\), and is not the trivial ruled surface \(\mathbb P^1\times\mathbb P^1\). Thus (B) must **not** be strengthened to global product triviality or embeddedness without separate arguments.

## Classification, proposed text, and audit boundary

This is a **verified conditional deduction**, not a confirmed error in Lemma 9.76.1. The printed determinant argument is valid and contains exactly the data needed for the refined conclusion. Proposed *reviewable* addition, immediately after physical line 24:

> For members at which the family evaluation is submersive somewhere along the curve, the ramification divisor of \(f_s\) is bounded by the vanishing divisor of the determinant section above and has degree at most \(-K_X\cdot\alpha-2\). In the extremal case \(-K_X\cdot\alpha=2\), this determinant does not vanish; the tangent bundle restricts as \(\mathcal O(2)\oplus\mathcal O^{n-1}\), and \(f_s\) is an immersion with trivial normal bundle.

No proposed change to the lemma's hypotheses or to the movable-class assertion. The movable cone identification in line 26, the positive-slope equivalence in Corollary 9.76.2, and the deeper cycle-space and Fujiki inputs in §§9.75–9.77 remain separately conditional/unverified. This report covers the derivative/determinant passage of one lemma and a comparison of one corollary, **not** all of §9.76 or any chapter. No excluded regularization, Bergman, L², Ohsawa–Takegoshi, multiscale-atlas or positivity-loss proof programme was inspected.

**Checks performed:** symbolic line-bundle degree and determinant-zero calculation, projective-space map ramification order, Hirzebruch-fiber normal sequence. No code, numerical tests, compilation, CI, or site publication.
