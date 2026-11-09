# A sharp degreewise-density obstruction to inverse-limit cohomology surjectivity

- **Finding:** POME-INV-LIM-COHOM-SURJECTIVITY-DENSITY-001
- **Date:** 2026-11-10
- **Status:** verified conditional deduction (self-contained counterexample to an **unprinted weakening**); **severity:** low for the present text, potentially high for downstream uses dropping hypotheses.
- **Production main reviewed:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\` (unchanged at review).
- **Integrated source:** \`docs/sections/open-maps-nuclear-spaces-and-inverse-limits--cohomology-of-countable-inverse-limits/index.html\`, blob \`30e6e5800601450ce52d9c01dc5abea06a403d6e\`.
- **Stable location:** section permanent tag \`0A983B5FB454\`; Theorem 2.14.4 source \`demailly-complex-geometry:3D7EF38C\`, permanent \`50E84369B7A2\`, physical lines **78–117**, especially the degree-\(q-1\) density step at **91–109**; Theorem 2.14.6 source \`demailly-complex-geometry:7A48110C\`, permanent \`10E2183C49C3\`, physical lines **123–157**, especially clause (1) **123–126** and proof **144–145**; Lemma 2.14.2 source \`demailly-complex-geometry:AAE7DFD2\`, permanent \`139720D2EFCA\`, physical lines **42–54**.
- **Scope:** a new, independent failure model for *surjectivity* of the cohomology comparison after deleting density of degreewise bonding maps; not a claim that any printed theorem is false.

## Exact hypotheses of the printed results

Theorem 2.14.4 assumes a countable inverse sequence of complexes of Hausdorff complex Fréchet spaces, with **dense bonding maps in every degree**. It asserts that
\[
\Theta^q:H^q(\varprojlim E_\nu^\bullet)\longrightarrow
\varprojlim H^q(E_\nu^\bullet)
\]
is surjective. It separately requires density of the cohomology bonding maps in degree \(q-1\) for injectivity. Theorem 2.14.6 explicitly retains the degreewise density hypotheses and, in its clause (1), assumes surjective cohomology transitions in degree \(q\) to deduce surjectivity and openness of the projection to stage zero.

We test exactly what happens to the **surjectivity conclusions** if degreewise density is omitted, **even when the degree-\(q\) cohomology transitions remain isomorphisms**. This is logically distinct from the earlier POME-INV-LIM-DENSE-DEGREE-NONEXACT-001, which has dense maps at the complex level and exhibits an injectivity/exactness obstruction when the preceding-degree cohomology transitions lack density.

## A fully explicit two-term Hilbert complex

Let \(H=\ell^2(\mathbb N_0,\mathbb C)\), let \(e_0,e_1,\dots\) be its standard orthonormal basis, and set
\[
S:H\to H,\qquad S(b_0,b_1,\dots)=(0,b_0,b_1,\dots).
\]
At **every** level \(\nu\ge0\) take the same two-term cochain complex
\[
E_\nu^{-1}=H,\qquad E_\nu^0=\mathbb C\oplus H,\qquad
d_\nu(y)=(0,y),
\]
with all remaining degrees zero. The spaces are Hilbert (in particular, Hausdorff Fréchet), all differentials are continuous, and each \(d_\nu\) has **closed** image. The cohomology is
\[
H^{-1}(E_\nu^\bullet)=0,\qquad H^0(E_\nu^\bullet)=
(\mathbb C\oplus H)/(\{0\}\oplus H)\simeq\mathbb C
\]
as a **Hausdorff topological vector space**.

Define the bonding maps, independent of \(\nu\), by
\[
r_\nu^{-1}(y)=Sy,\qquad
r_\nu^0(a,b)=(a,\; a e_0+Sb).
\]
These are bounded complex-linear maps and commute with \(d\), since
\(r_\nu^0(0,y)=(0,Sy)=d_{\nu-1}(Sy)\). The induced map
\[
H^0(E_{\nu+1}^\bullet)\longrightarrow H^0(E_\nu^\bullet)
\]
is the **identity on \(\mathbb C\)**: in particular, it is an isomorphism, hence surjective and dense. Thus
\[
\varprojlim H^0(E_\nu^\bullet)\cong\mathbb C.
\]

By contrast, the bonding maps on the complexes are **not dense**:
\[
r_\nu^{-1}(H)=SH=\{y:y_0=0\},\qquad
r_\nu^0(\mathbb C\oplus H)
=\{(a,b):b_0=a\}.
\]
Both images are proper closed codimension-one subspaces. This identifies precisely the omitted hypothesis.

## Computation of the inverse-limit complex

A compatible element \(y=(y_\nu)\in\varprojlim E_\nu^{-1}\) obeys \(y_\nu=Sy_{\nu+1}\). For each fixed \(\nu\), it follows for every \(N\) that
\(y_\nu\in S^NH\). Since \(\bigcap_{N\ge0}S^NH=\{0\}\),
\[
\varprojlim E_\nu^{-1}=\{0\}.
\]

A compatible element \(((a_\nu,b_\nu))_\nu\in\varprojlim E_\nu^0\) obeys
\[
a_\nu=a_{\nu+1}=a,\qquad b_\nu=a e_0+S b_{\nu+1}.
\]
Iteration gives, for **every** \(N\ge1\),
\[
b_\nu=a(e_0+\cdots+e_{N-1})+S^N b_{\nu+N}.
\tag{*}
\]
Therefore the first \(N\) coordinates of the *fixed vector* \(b_\nu\) all equal \(a\), and
\[
\|b_\nu\|_H^2\ge N|a|^2\quad\hbox{for all }N.
\]
Since \(b_\nu\in\ell^2\), necessarily \(a=0\). Formula (*) then gives
\(b_\nu\in \bigcap_N S^NH=\{0\}\). Hence
\[
\boxed{\varprojlim E_\nu^0=\{0\},\qquad
H^0(\varprojlim E_\nu^\bullet)=0.}
\]
The natural map is therefore
\[
\boxed{\Theta^0:0\longrightarrow\mathbb C,}
\]
which is **not surjective**, despite every stage cohomology bonding map being the identity.

The displayed bound is also a finite-stage **quantitative obstruction**: a lift through levels \(0,\dots,N\) of the compatible nonzero class \(a\) forces the vector at level zero to have squared norm at least \(N|a|^2\). It cannot converge to a genuine infinite-stage lift. This does not depend on non-Hausdorff cohomology or an unproved interchange of limits.

## Mathematical verdict, correction and dependents

**No printed theorem is contradicted.** The example violates a hypothesis expressly retained by Theorems 2.14.4 and 2.14.6. The printed constructive proof uses degree-\(q-1\) density to make successive coboundary errors summable at lines 91–109; this mechanism cannot be applied to the present shift system.

A useful **proposed Remark after Theorem 2.14.4** is: *The surjectivity of \(\Theta^q\) can fail, even for two-term Hilbert complexes with closed boundaries and isomorphisms on degree-\(q\) cohomology, if the degreewise density assumption is dropped.* Include the shift example, or cite this audit note. The same remark protects use of clause (1) of Theorem 2.14.6: surjective bonding maps on cohomology alone do **not** replace degreewise density.

The affected proof locations are **2.14.4 (surjectivity)** and **2.14.6(1)**, but only for potential *future* applications with weakened hypotheses. The existing Theorem 2.14.6(3) injectivity and the earlier dense-degree/nonexactness result address **different** hypotheses and conclusions. No source text, canonical tag, or theorem body has been changed.

## Coverage and checks

Selected proof/statement examination at §2.14.2, §2.14.4, §2.14.6(1), including the exact error-correction step; independent complete algebraic and Hilbert-norm verification of the new two-term inverse-system example. Previously visited §2.14: **0 first-visited numbered sections and 0 whole-section certifications**. Current table of contents: **25 chapters, 747 numbered sections**. No analytic regularization/Bergman/L²/OT/multiscale/positivity-loss work was consulted; those items remain **deferred-by-user**. No project build, unit tests, CI, formal verification, site publication, or source/registry modifications were performed.
