# Finite-rank invariance of the Fredholm index in the Pome Fréchet framework (2026-11-07)

**Stable finding ID:** \`POME-FREDHOLM-FINITERANK-INDEX-001\`  
**Severity / status:** low / **verified conditional deduction**. **Not** a false printed theorem, proof-gap repair, or certification of the full compact-perturbation theorem.  
**Reviewed production main:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`.  
**Reading edition:** \`docs/sections/open-maps-nuclear-spaces-and-inverse-limits--open-maps-compact-perturbations-and-finite-cohomology/index.html\`, main blob \`dd12ea5ca837e3ec507930eeed8a0eb38bd3f6a4\`.  
**Section:** §2.12, permanent section tag from the live ToC \`AB0CD215F15E\`.  
**Exact printed anchors:** Proposition 2.12.1, source \`demailly-complex-geometry:F97537CF\` / permanent \`71B16A3EF23E\`, physical HTML lines 13–30; Corollary 2.12.2, source \`demailly-complex-geometry:BCEF25A2\` / permanent \`181D2DF97074\`, lines 32–48; Theorem 2.12.3, source \`demailly-complex-geometry:5C1FDFEE\` / permanent \`E27FE1F7DE85\`, lines 50–99; and Theorem 2.12.5 (Cartan–Serre), source \`demailly-complex-geometry:77D28452\` / permanent \`D8E2BCEBC75D\`, lines 101–117. The source name here denotes provenance of functional analysis, **not** the owner-excluded approximation/regularization programme.

## Scope and precise claim

Theorem 2.12.3 proves that compact perturbations preserve quasi-isomorphisms of Fréchet spaces (closed image, finite-dimensional kernel and cokernel); it **does not explicitly assert the Fredholm index formula**. The following is an independent, precise *finite-rank* strengthening. It neither substitutes a finite-rank operator for a general compact operator nor claims density of finite-rank operators in compact operators.

**Proposition (complete proof conditional only on the printed Fréchet open-map/finite-codimension result).** Let \`E,F\` be Fréchet spaces, \`T:E→F\` a continuous linear Fredholm map (closed range and finite-dimensional kernel and cokernel), and \`R:E→F\` a continuous finite-rank map. Then \`T+R\` is Fredholm and
\[
 \boxed{\operatorname{ind}(T+R)=\operatorname{ind}(T)},\qquad
 \operatorname{ind}T:=\dim\ker T-\dim(F/T(E)).
\]
No Banach norm, approximation property, or compactness of a sequence of unit vectors is assumed.

## Exact-sequence proof

Set \`S=R(E)\`, a finite-dimensional (hence closed) subspace of \`F\`, let \`Q:F→F/S\` be the Hausdorff quotient, and put \`A=QT=Q(T+R)\`. The subspace \`T(E)+S\` is closed: the sum of a closed linear subspace and a finite-dimensional subspace is closed (pass to the Hausdorff quotient by \`T(E)\`, where the image of \`S\` is finite-dimensional and closed). Consequently
\[
 A(E)=(T(E)+S)/S
\]
is closed in \`F/S\`. Its cokernel is
\[
 (F/S)/A(E)\simeq F/(T(E)+S),
\]
of dimension at most \(\dim(F/T(E))\). Also
\[
 0\longrightarrow\ker T\longrightarrow\ker A
   \overset{T}{\longrightarrow}S\cap T(E)\longrightarrow0
\]
is exact. Thus \(\dim\ker A=\dim\ker T+\dim(S\cap T(E))<\infty\): \`A\` is Fredholm.

Writing \`U=T+R\`, one has \`U(E)+S=T(E)+S\`. Therefore the **algebraic** codimension of \`U(E)\` in \`F\` is finite, bounded by
\(\dim S+\dim(F/(T(E)+S))\).
Corollary 2.12.2 says that the image of a continuous linear map between **Fréchet** spaces with finite algebraic codimension is automatically closed. This is the only topological step that cannot be replaced by the false general claim that arbitrary finite-codimensional subspaces of arbitrary locally convex spaces are closed. It follows that \`U(E)\` is closed. Moreover \(\ker U\subseteq\ker A\), so \`U\` is Fredholm.

For either \`V=T\` or \`V=U\`, the common identity \`QV=A\` gives an **exact sequence of finite-dimensional vector spaces**
\[
 0\to\ker V\to\ker A
   \xrightarrow{\,V\,} S
   \longrightarrow F/V(E)
   \longrightarrow (F/S)/A(E)\to0. \tag{*}
\]
The middle map is \(\ker A\ni x\mapsto Vx\in S\); the next is the inclusion-induced map \(s\mapsto[s]\); the final map is induced by \`Q\`. Exactness follows respectively from \(\ker(QV)=\ker A\), \(Vx=0\iff x\in\ker V\), and \(QV(E)=A(E)\). In particular the kernel of the last map consists precisely of classes represented by elements of \`S\`.

Taking alternating dimensions in (*) yields
\[
 \operatorname{ind}(V)
 =\dim\ker A-\dim S-\dim((F/S)/A(E))
 =\operatorname{ind}(A)-\dim S.
\]
Applying this equality to \`V=T\` and \`V=U\` proves the claimed index identity, including cases where **both individual kernel and cokernel dimensions change**. This proof only uses finite-dimensional algebra, elementary quotient topology, and the internal Corollary 2.12.2.

## Explicit change in nullity and corank

Take \`E=ℝ²\`, \`F=ℝ³\`, \`T(x,y)=(x,y,0)\`, and \`R(x,y)=(-x,0,0)\`. Then \(\ker T=0\), \(\dim\operatorname{coker}T=1\), while \((T+R)(x,y)=(0,y,0)\), so \(\dim\ker(T+R)=1\) and \(\dim\operatorname{coker}(T+R)=2\). Both indices are \(-1\). Thus only the **difference**, not the separate dimensions, is invariant.

## A direct Cartan–Serre finite-rank consequence

In the setup of Theorem 2.12.5, if the chain map \(\rho^q:E^q\to F^q\) has finite rank \`r\` and \(H^q(\rho)\) is surjective, then \(H^q(F)\) is a quotient of the finite-dimensional image of \(\rho^q|_{Z^q(E)}\). Hence
\[
 \dim H^q(F)\le\operatorname{rank}(\rho^q|_{Z^q(E)})\le r.
\]
The **Hausdorff** conclusion still needs the printed compact Cartan–Serre proof or an independent closed-boundary argument; finite-dimensional *algebraic* cohomology by itself does not prove its quotient topology Hausdorff. Finite-rank continuous maps are compact, so the printed theorem supplies that additional conclusion **conditional on its own proof**.

## Audit judgment, dependencies, and unreviewed scope

- **Classification:** verified conditional deduction, low severity. Theorem 2.12.3, Corollary 2.12.2 and Theorem 2.12.5 are **not refuted**. The main independent new proof is the exact-sequence calculation for all continuous finite-rank perturbations of a Fréchet Fredholm map. The finite-codimensional closed-image step uses the already integrated Corollary 2.12.2, whose complete underlying Fréchet open-mapping/Baire argument is not transitively certified in this run.
- **Proposed addition (NOT applied to production):** append an optional finite-rank index corollary with exact sequence (*) after §2.12.3; retain existing provenance, permanent tags, and the distinct full compact-perturbation theorem.
- **Downstream:** the Fredholm language in §2.12, the finite-cohomology use in Theorem 2.12.5, and related elliptic Fredholm comparisons in §2.18. No assertion that compact perturbations of general Fréchet maps preserve the index is proved **here**; in particular, do not infer it from an unproved finite-rank approximation property.
- **Not checked:** the full compact-perturbation argument (Theorem 2.12.3) beyond its hypotheses and conclusions, the complete Baire/open-mapping proof of Proposition 2.12.1, all cohomological proof inputs of §2.12.5, or other chapters. No excluded regularization/Bergman/L²/OT/multiscale/positivity-loss work.

This is new *selected* proof-level coverage of previously partly sampled §2.12, **not** a first-section visit and **not** a full §2.12 certification. Actual inventory remains 25 chapters, 747 sections, zero fully certified sections. No project tests, builds, CI, formal verification or website publication performed.
