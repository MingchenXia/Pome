# Normal-locus lifting through normalization: complete direct section review

**Finding:** POME-NORM-NORMAL-LOCUS-LIFTING-001  
**Date:** 2026-11-20 (Asia/Shanghai)  
**Classification:** **low / verified conditional deduction**. This is an additional result, not a false printed theorem, duplicate, or complete upstream-chain certification.  
**Reviewed main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.  
**Integrated file:** `docs/sections/complex-spaces-and-modifications--reduced-spaces-and-normalization/index.html` (blob `06439f43d1ce8e83d2529682c9a630bffa3d9c22`).  
**Actual direct reading:** all mathematical paragraphs, statements, and proof steps of §9.4, physical HTML lines **7–199** (ten entries 9.4.1–9.4.10, including the two examples). The initial navigation and final citation/interface markup are not mathematical proofs.
**Permanent / source anchors:** Lemma 9.4.4 `D73CC9F08C05` / `foundations-of-pluripotential-theory:E60680A7`, lines 87–108; Lemma 9.4.5 `58E87F89D557` / `:571B5EA0`, lines 116–137; Theorem 9.4.6 `12A47DB401E2` / `:7042BB57`, lines 142–159; Corollary 9.4.9 `EE1633042D3D` / `:405861C0`, lines 185–192; Example 9.4.10 `60A14C7A1845` / `:680F3928`, lines 197–199.

## New theorem (sufficient hypothesis, uniqueness, and sharp boundary)

Let \(X\) be a reduced Hausdorff second-countable complex space under the collection conventions, \(\nu:\widetilde X\to X\) its finite normalization, and \(N\subset X\) its nonnormal locus. Let \(Y\) be any normal complex space, not necessarily smooth or equidimensional, and let \(F:Y\to X\) be holomorphic. **Assume \(E:=F^{-1}(N)\) is nowhere dense in \(Y\)** (equivalently, \(F\) takes every irreducible germ of \(Y\) generically into the normal locus of \(X\)). Then there is a **unique holomorphic** \(\widetilde F:Y\to\widetilde X\) such that
\[
                       \nu\circ\widetilde F=F.
\]
No properness, surjectivity, or bimeromorphicity assumption on \(F\) is needed. In particular, a nonconstant analytic disc whose image is not contained in \(N\) has a unique holomorphic lift, provided its inverse image of \(N\) has empty interior (automatic for a connected disc by the identity theorem and analyticity of \(N\)).

The assumption cannot simply be deleted from a **universal uniqueness** assertion: for the node \(X=\{zw=0\}\subset\mathbb C^2\), the constant map from a disc \(Y=\Delta\) to the node has two distinct constant holomorphic lifts, one to each of the two points over the origin. This is a counterexample to the *unqualified proposed lifting statement*, **not** to Theorem 9.4.6. The hypothesis is sufficient, not asserted necessary for every individual map (constant maps to a cusp, for example, have only one possible point over the cusp).

## Proof

**1. The normalization is an isomorphism over \(X\setminus N\).** By Lemma 9.4.4, \(N\) is an analytic subset. It is nowhere dense because regular points are normal and the regular locus is dense. At every normal \(x\), Proposition 9.4.3 gives \(\widetilde{\mathcal O}_{X,x}=\mathcal O_{X,x}\). In the graph realization of Lemma 9.4.5, the finitely many weakly holomorphic coordinate generators are therefore holomorphic near \(x\), after shrinking; their graph is a holomorphic graph over a neighborhood of \(x\). Uniqueness in Theorem 9.4.6 identifies that graph with \(\nu\) locally. Thus
\[
             \nu:\widetilde X\setminus\nu^{-1}(N)\xrightarrow{\ \cong\ }X\setminus N
\]
is biholomorphic, including at normal *singular* points. Consequently \(F|_{Y\setminus E}\) has the canonical holomorphic lift
\[
       \widetilde F_0=(\nu|_{\nu^{-1}(X\setminus N)})^{-1}\circ F.
\]

**2. Extension at an arbitrary point \(y\in E\).** Put \(x=F(y)\). The fiber \(\nu^{-1}(x)=\{q_1,\ldots,q_r\}\) is finite. Choose pairwise disjoint neighborhoods \(W_j\Subset W'_j\) of its points, with each \(W'_j\) a local analytic-model chart of \(\widetilde X\), so that the ambient holomorphic coordinate functions are bounded on \(W_j\). Properness of \(\nu\) yields a neighborhood \(U\ni x\) such that
\[
                         \nu^{-1}(U)\subset\bigcup_{j=1}^r W_j.
\]
Otherwise there are points \(x_k\to x\) and \(q_k\in\nu^{-1}(x_k)\setminus\bigcup W_j\); properness over a compact neighborhood gives a convergent subsequence with limit in \(\nu^{-1}(x)\), a contradiction.

Since \(Y\) is normal, each germ \((Y,y)\) is irreducible. Corollary 9.4.9 gives an arbitrarily small connected neighborhood \(V\ni y\), with \(F(V)\subset U\), such that \(V\setminus E\) is connected (the analytic set \(E\) is nowhere dense). The connected image \(\widetilde F_0(V\setminus E)\) lies in just **one** of the disjoint \(W_j\). Compose \(\widetilde F_0\) with the ambient coordinate functions of \(W'_j\). Each composition is holomorphic and bounded on \(V\setminus E\). Lemma 9.4.4 (bounded holomorphic extension on a normal space across a nowhere-dense analytic set) extends these coordinates uniquely and holomorphically to \(V\).

Their combined holomorphic map lands in \(\overline{W_j}\subset W'_j\) by continuity and density. The holomorphic equations of the analytic subset \(\widetilde X\cap W'_j\) hold on the dense set \(V\setminus E\), hence everywhere on \(V\). Thus the coordinate extensions define a holomorphic \(\widetilde F_V:V\to\widetilde X\). Its composition with \(\nu\) agrees with \(F\) on \(V\setminus E\), hence everywhere by continuity.

**3. Gluing and uniqueness.** Extensions constructed on overlapping neighborhoods agree on the dense subset outside \(E\) because \(\nu\) has a unique inverse there; they agree everywhere by continuity and the Hausdorff property. They glue to the required map. Any other holomorphic lift must equal \(\widetilde F_0\) on dense \(Y\setminus E\), and therefore equals \(\widetilde F\) globally.

**4. Why the boundary condition matters.** For the nodal curve in Example 9.4.10, normalization is the disjoint union of the two axes. The constant map \(F:\Delta\to X,\ F(t)=(0,0)\) has \(E=\Delta\) and admits two distinct lifts \(\Delta\to\widetilde X\). Their composites with \(\nu\) coincide. This establishes failure of uniqueness without a generic-normal-locus condition; no claim is made about failure of existence in all such cases. \(\square\)

## Direct-check audit log for the integrated section

- **§9.4.1–2, lines 23–48:** checked density under bimeromorphic maps and branchwise weak holomorphy, including connected regular loci and bounded extension; the indispensable internal input is Lemma 9.2.9.
- **§9.4.3, lines 56–78:** checked the discriminant/Vandermonde clearing argument, nonzerodivisor selection on all branches, finite integral closure, and the connected finite cluster set. This is not a certification of the full §9.2–§9.3 constructions.
- **§9.4.4, lines 87–108:** checked coherent-support via minors and Nakayama's determinant argument, the \(\mathcal I^k\)-conductor step, and extension of bounded functions on normal complex spaces; used in the new theorem.
- **§9.4.5–6, lines 116–159:** checked monic-polynomial bounds, graph closure, finite fibers, local normality, uniqueness and gluing. The older audit-only **POME-NORM-PERFECT-PARACOMPACT-REPAIR-001** concerns a different, previously logged paracompact gluing issue and is **not** counted again or declared resolved; the current integrated text explicitly assumes a countable basis.
- **§9.4.7–10, lines 168–199:** checked local normalization interpretation, unibranch versus normal, finite proper one-point fibers, and node/cusp examples. In particular a unibranch singularity need not be normal.

**External inputs:** none introduced by the new theorem; it uses the integrated Lemma 9.4.4, Theorem 9.4.6 and Corollary 9.4.9. Their upstream Lemmas 9.2.6/.9 and Theorems 9.3.4/.10 remain *internal dependencies not transitive proof certificates*. No Demailly approximation, Bergman, \(L^2\), Ohsawa–Takegoshi, multiscale, or positivity-loss work was opened. Hironaka is not needed.

## Status, correction proposal, and impact

**Status:** verified conditional deduction, **low** severity. The printed Theorem 9.4.6 is **not refuted**; the qualification applies to the *new* lifting formulation. No new confirmed original error, new genuine duplication, or completed transitive proof certification is asserted. **Proposed change:** retain this theorem as an optional internal corollary after §9.4.9, with explicit density condition and the node counterexample; source, body, registry, permanent tags and main remain untouched. It may help validate future lifts of discs and normal sources in §§9.5, 9.9–9.11, but those downstream uses are **not** independently certified here.

**Coverage delta:** one entire §9.4 directly reread; no assertion of first-ever review because earlier partial §9.4 normalization/conductor/flatness reports exist; zero new fully transitive dependency chains. No tests, builds, CI, or website publication.
