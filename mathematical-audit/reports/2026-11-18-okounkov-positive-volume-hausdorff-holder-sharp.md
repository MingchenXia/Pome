# Mathematical audit — sharp quantitative Hausdorff stability of positive-volume Okounkov bodies

**Date:** 2026-11-18. **Reviewed production main SHA:** b6933b772f41b45918f7e25ed1afbbb1fd892272. **Review branch:** review/mathematical-audit.

**Stable finding:** POME-OKO-POSVOL-HAUSDORFF-HOLDER-SHARP-001. **Severity:** low. **Status:** verified conditional deduction. **Disposition:** additive quantitative corollary; no false printed statement, no claim of an entire-section certification. The exact symmetric-difference identity used below was already recorded as POME-OKO-SYMDIFF-ISOMETRY-001 and is **not a new finding**.

## Exact reading-edition anchors and hypotheses

Main file: docs/sections/almost-semigroups/index.html, Git blob **33898b2963ad0f8b7e30bf414276642f60925b74** (physical line numbers below).

* Pointed cone, grading and slices: §19.7.15–17, lines **211–230**; pseudometric equation **19.7.17** at **228–230**, source label **sgpt:A996EEF7**, permanent tag **642E2D6850DF** (tag is printed in the equation's code badge).
* Definition **19.7.26**, source **sgpt:56C14254**, permanent **0270FA2C03BD**, lines **393–400**, defines the body as the degree-one slice of the closed cone.
* Theorem **19.7.20**, source **sgpt:282DA4DD**, permanent **85641516C8CA**, lines **299–319**, supplies all-degree lattice counts only with the appropriate generated-lattice condition.
* Lemma **19.7.25**, source **sgpt:4791A323**, permanent **E41D68AC6F7C**, lines **372–389**, identifies the cone of a positive-volume intersection. Its interior-filling assertion cites KK12 and remains an explicitly conditional input outside the saturated models.
* Definition **19.7.31**, source **sgpt:7DD4FA88**, permanent **B0C65454CC85**, lines **530–532**, restricts almost semigroups to positive volume.
* Theorem **19.7.32**, source **sgpt:ED83BFDD**, permanent **1551B679B8B7**, lines **535–544** and proof **550–655**, extends the body map continuously in the Hausdorff topology.

The paired **distinct statement version**, Theorem **19.2.10** (source **sgpt:870F54F8**, permanent **2534E787147E**) occurs at docs/sections/the-theory-of-okounkov-bodies--almost-semigroups/index.html, blob **33212916f9ea7754f51f8194cfb76c2fcbe8efab**, lines **73–84**. This entry is kept as a valid separate presentation; it is not a canonicalization duplicate just because the conclusion overlaps §19.7.32.

## New quantitative theorem

Let \(n\ge1\), let \(C\subset\mathbf R^n\times\mathbf R_{\ge0}\) be the pointed closed convex cone fixed in §19.7.15, and choose \(R>0\) such that its compact height-one slice is contained in \(B_R(0)\). Let \(S,T\in\overline{\mathcal S'(C)}_{>0}\) be positive-volume almost semigroups. Assume the bodies \(K=\Delta(S)\) and \(L=\Delta(T)\) each contain **some** closed Euclidean ball of radius \(r>0\); the two centers need not agree.

Write \(\omega_n\) for the Euclidean volume of the unit ball. Then
\[
\boxed{\quad
d_{\rm Haus}(\Delta(S),\Delta(T))
\le {4R\over r}\left({d_{\rm sg}(S,T)\over\omega_n}\right)^{1/n}.
\quad} \tag{A}
\]
The same inequality holds directly for any nonempty compact convex \(K,L\subseteq B_R(0)\) each containing a ball of radius \(r\), with \(d_{\rm sg}\) replaced by \(\operatorname{Leb}(K\triangle L)\).

The exponent \(1/n\) **cannot be replaced by any larger exponent uniformly**, even for saturated full-lattice semigroups in one fixed cone whose bodies all contain the *same* fixed ball and have uniformly positive volume. This is a uniform local Hölder modulus on fixed-inradius strata, not a claim of global uniform continuity near volume zero.

## Proof of the geometric estimate (fully elementary)

Set \(\delta=d_{\rm Haus}(K,L)\). If \(\delta=0\) there is nothing to prove. After interchanging \(K,L\), compactness gives \(x\in K\) with \(\operatorname{dist}(x,L)=\delta>0\). Let \(y\) be the Euclidean metric projection of \(x\) onto the compact convex set \(L\), and put \(u=(x-y)/\delta\). The elementary projection variational inequality gives
\[
\langle u,z\rangle\le\langle u,y\rangle
=\langle u,x\rangle-\delta
\qquad(z\in L). \tag{B}
\]
Choose a closed radius-\(r\) ball \(B_r(p)\subseteq K\) and put \(t=\delta/(4R)\). Since \(K,L\subset B_R(0)\), we have \(0<t\le1/2\), and for any \(w\in B_r(p)\) we have \(\|w-x\|\le2R\). Thus
\[
\langle u,(1-t)x+tw\rangle
\ge\langle u,x\rangle-2Rt
=\langle u,x\rangle-\delta/2
>\sup_{z\in L}\langle u,z\rangle .
\]
By convexity the entire translated and rescaled ball
\[
(1-t)x+tB_r(p)=B_{tr}((1-t)x+tp)
\]
lies in \(K\), and by the strict separation just established it is disjoint from \(L\). Therefore
\[
\operatorname{Leb}(K\triangle L)\ge
\operatorname{Leb}(K\setminus L)\ge\omega_n(tr)^n
=\omega_n\left({r\delta\over4R}\right)^n.
\]
Rearranging proves (A) with symmetric-difference volume. This argument uses neither smoothness nor strict convexity; it works for all \(n\ge1\) and arbitrary separate inball centers.

## Passage to the actual semigroup pseudometric

For the positive-volume almost semigroups of the displayed theorem, use the **already recorded** isometry
\[
d_{\rm sg}(S,T)=\operatorname{Leb}(\Delta(S)\triangle\Delta(T)).
\tag{C}
\]
This is not inferred merely from volume equality (19.7.34). The earlier isometry proof uses full-degree counting, the positive-volume intersection-cone result (19.7.25), and Theorem 19.7.32 to pass to the positive-volume pseudometric closure. Equality (C) is a conditional upstream result and is intentionally **not recertified here as a new discovery**. Substituting it into the fully elementary geometric estimate proves (A).

For the saturated models used to prove optimality below, equality (C) can instead be checked without KK12: lattice Riemann sums converge for each compact convex body with nonempty interior because its boundary has zero Lebesgue measure. In fact, after translating an interior point to the origin, for every small \(\varepsilon>0\) the boundary lies in \((1+\varepsilon)K\setminus(1-\varepsilon)K\), whose volume tends to zero. The symmetric difference of two such bodies is Jordan measurable, so
\[
\lim_{k\to\infty}k^{-n}\#\bigl((kK\cap\mathbf Z^n)\triangle(kL\cap\mathbf Z^n)\bigr)
=\operatorname{Leb}(K\triangle L).
\]
For a full-dimensional convex body \(K\), \(S(K):=\{(m,k)\in\mathbf Z^{n+1}: k\ge0,\ m\in kK\}\) generates the full ambient lattice: at each sufficiently large height \(k\), a large Euclidean ball lies inside \(kK\), so two lattice points differing by each horizontal basis vector occur at that height, and a point at height \(k+1\) gives the last independent vertical generator modulo the horizontal vectors. This verifies membership in \(\mathcal S'(C)\) for the following examples.

## Sharpness: a fixed-volume cube with one clipped vertex

For any \(n\ge1\), use the **single fixed cone** over \(K=[0,1]^n\) and, for \(0<\varepsilon<1/4\), put
\[
L_\varepsilon
=\{x\in[0,1]^n:x_1+\cdots+x_n\ge\varepsilon\}.
\]
Both \(K\) and \(L_\varepsilon\) contain the same closed ball \(B_{1/4}((1/2,\ldots,1/2))\) and lie inside \(B_{\sqrt n}(0)\). Their lost corner is the simplex \(\{x_i\ge0,\ \sum_i x_i<\varepsilon\}\), hence
\[
\operatorname{Leb}(K\triangle L_\varepsilon)=\frac{\varepsilon^n}{n!}.
\tag{D}
\]
Orthogonal projection onto \(\{\sum_i x_i=\varepsilon\}\) gives
\[
d_{\rm Haus}(K,L_\varepsilon)=\frac{\varepsilon}{\sqrt n}.
\tag{E}
\]
Indeed, for \(x\in K\) with \(\sum x_i<\varepsilon\), adding \((\varepsilon-\sum x_i)/n\) to each coordinate remains in the cube when \(\varepsilon<1/4\), and this is the nearest point in the defining half-space. Equality is attained at \(x=0\).

The saturated semigroups \(S(K)\) and \(S(L_\varepsilon)\) lie in \(\mathcal S'(C)\), with all hypotheses independent of \(\varepsilon\). As explained above, their pseudometric is the symmetric-difference volume, so (D)–(E) give the **exact** relation
\[
d_{\rm Haus}(\Delta S(K),\Delta S(L_\varepsilon))
=\frac{(n!\,d_{\rm sg}(S(K),S(L_\varepsilon)))^{1/n}}{\sqrt n}.
\tag{F}
\]
A proposed exponent \(\beta>1/n\) with a coefficient depending only on \(n,R,r\) would give \(\varepsilon/\sqrt n\le A(\varepsilon^n/n!)^\beta\), impossible as \(\varepsilon\downarrow0\). For \(n=1\), the optimal exponent is \(1\) and the same example applies. The coefficient \(4R/r\) in (A) was **not** claimed optimal.

## Audit disposition, dependencies and downstream scope

* **Status:** verified conditional deduction, low. No original statement is false. Formula (A) is proved under a **uniform positive inradius** assumption; the exponent is sharp even with a common inball.
* **Proposed optional correction:** insert an explicitly optional quantitative corollary following §19.7.32 (and point §19.2.10 to it) if an effective body-continuity estimate is needed. The audit itself does not edit the reading text, source, registries or permanent tags.
* **Genuine dependencies:** (C) is the prior POME-OKO-SYMDIFF-ISOMETRY-001 deduction, itself relying on the positive-volume cone/intersection and count inputs listed above. The explicit saturated sharpness example and the convex-geometric ball estimate are self-contained. Keep KK12, WN14, Kho92 historic citations; do not relabel them as proofs we have independently reconstructed for their full scope.
* **Affected use cases:** quantitative stability in §19.7.32 / §19.2.10 for positive-volume bodies with a uniform inradius; optional control of approximating partial bodies in §19.4–5 when such a radius is separately established. **No** estimate for arbitrary shrinking-volume sequences, and **no** section-growth or partial Okounkov theorem verified transitively.
* **Remaining gaps:** a uniform inradius bound does not follow merely from each body's positive volume. The general Kaveh–Khovanskii interior-filling chain in §19.7.25 and partial-body applications are **not** certified in this run. No source-side changes, builds, tests, CI, PR, or website publication were performed.

**Coverage:** new selected geometric estimate and proof-level check of §19.7.17/.26/.31/.32; §19.7.20/.25 and §19.2.10 checked for exact hypotheses only. All these numbered sections were previously partially visited. **New first proof-level sections: 0. Entire sections certified: 0.** Current main inventory: **25 chapters, 747 numbered sections**. User-excluded Demailly regularization, Bergman, weighted L², Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof-completion tasks remain **deferred-by-user**, not resolved.
