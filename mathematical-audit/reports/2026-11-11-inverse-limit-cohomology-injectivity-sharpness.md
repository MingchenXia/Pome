# A surjective Hilbert tower with noninjective inverse-limit cohomology

**Finding:** \`POME-INV-LIM-COHOM-INJECTIVITY-SHIFT-001\`  
**Date:** 2026-11-11  
**Classification:** low / **verified conditional deduction** (sharpness countermodel; **no error in the printed theorems**)  
**Production \`main\`:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`.  
**Review branch:** \`review/mathematical-audit\`; audit documents only.

## Exact reading-edition provenance

- \`docs/sections/open-maps-nuclear-spaces-and-inverse-limits--cohomology-of-countable-inverse-limits/index.html\`, Git blob \`30e6e5800601450ce52d9c01dc5abea06a403d6e\`.
- §2.14 introductory Fréchet and cohomology conventions: **physical lines 5–16**, source \`demailly-complex-geometry:487D3283\`, section permanent tag \`0A983B5FB454\`.
- **Theorem 2.14.4:** physical **lines 77–83** (proof lines 85–118); source \`demailly-complex-geometry:3D7EF38C\`, permanent tag \`50E84369B7A2\`. Its injectivity conclusion expressly assumes dense bonding maps on \(H^{q-1}\), *in addition* to degreewise density.
- **Theorem 2.14.6(3):** physical **lines 123–139**, proof lines 142–159; source \`demailly-complex-geometry:7A48110C\`, permanent tag \`10E2183C49C3\`.
- **Proposition 2.14.7:** physical **lines 162–185**, source \`demailly-complex-geometry:CD05CCE6\`, permanent tag \`F529678A1F94\`. The proposition requires dense bonding maps on the *kernels* of a tower of short exact sequences.

The **hypotheses actually printed** are satisfied exactly where they are used. The construction below only disproves several tempting, stronger versions **with an expressly printed hypothesis deleted**. It is not a proof gap or a false theorem in Pome. The first proof-level inspection of this section took place earlier; this report is a new, independent sharpness computation.

## One fixed tower and its cohomology

Let \(H=\ell^2(\mathbb N_0;\mathbb C)\), with standard orthonormal basis \(e_0,e_1,\ldots\). Write
\[
 R(x_0,x_1,\ldots)=(0,x_0,x_1,\ldots),\qquad
 L(x_0,x_1,\ldots)=(x_1,x_2,\ldots).
\]
Thus \(LR=I\), \(L\) is surjective, while \(R(H)=\{x:x_0=0\}\) is a proper **closed** codimension-one subspace.

At every stage \(\nu\geq0\), take the same two-term complex of Hilbert (hence Fréchet) spaces, concentrated in degrees \(0,1\):
\[
 E_\nu^0=H\oplus H\xrightarrow{\ d\ }E_\nu^1=H,\qquad
 d(h,y)=y .
\]
The bonding chain map \(r_\nu\), independent of \(\nu\), is
\[
 r^0(h,y)=\bigl(Rh+\langle y,e_0\rangle e_0,Ly\bigr),
 \qquad r^1(y)=Ly .
\]
The identity \(d r^0=r^1d\) is immediate. **Both degreewise maps are surjective:** for a prescribed \((u,v)\in H\oplus H\), choose
\[
 y=(u_0,v_0,v_1,\ldots),\qquad h=Lu;
\]
then \(Ly=v\) and \(Rh+y_0e_0=u\). The degree-one bonding map \(L\) is surjective as well.

Each stage has
\[
 H^0(E_\nu^\bullet)=\{(h,0):h\in H\}\simeq H,\qquad
 H^1(E_\nu^\bullet)=0.
\]
The induced bonding map on \(H^0\) is **\(R\)**, so the extra density hypothesis of Theorem 2.14.4 for \(q=1\) is violated. Its failure is not an artifact of the chain maps being non-surjective: **all degreewise transitions here are open surjections between Hilbert spaces.**

## Complete calculation of the inverse-limit cohomology

Write \(E^\bullet=\varprojlim_\nu E_\nu^\bullet\). A degree-one element \(y=(y_\nu)_{\nu\ge0}\) is coherent precisely when \(Ly_{\nu+1}=y_\nu\). Every such sequence is uniquely parametrized by
\[
 y_0\in H,\qquad a=(a_1,a_2,\ldots)\in\mathbb C^{\mathbb N},\qquad
 y_\nu=(a_\nu,a_{\nu-1},\ldots,a_1,(y_0)_0,(y_0)_1,\ldots)
 \quad(\nu\ge1).
\]
For each fixed \(\nu\) only finitely many new scalar coordinates are prepended, so **no \(\ell^2\) condition is imposed on the infinite sequence \(a\)**. This gives a linear homeomorphism
\[
 E^1\simeq H\times\mathbb C^{\mathbb N},
\]
where the second factor has the *product*, not \(\ell^2\), topology. Indeed every finite stage uses \(y_0\) and only finitely many \(a_i\); conversely their coordinate evaluations are continuous.

A coherent degree-zero element \(x_\nu=(h_\nu,y_\nu)\) must satisfy
\[
 h_\nu=Rh_{\nu+1}+a_{\nu+1}e_0.
\]
Comparing successively its first, second, and subsequent coordinates yields the **exact** forced formula
\[
 (h_\nu)_k=a_{\nu+k+1}\quad (k\ge0).
\]
Thus a coherent primitive for a given \(y\in E^1\) exists **if and only if**
\[
 a=(a_1,a_2,\ldots)\in\ell^2(\mathbb N).
\]
Sufficiency is explicit: set \(h_\nu=(a_{\nu+1},a_{\nu+2},\ldots)\in H\). Conversely, \(h_0\in H\) implies the \(\ell^2\) condition. Since \(d:E^0\to E^1\) is induced by projection onto \(y\),
\[
 \operatorname{im}d
 \simeq H\times\ell^2(\mathbb N)
 \ \subsetneq\ H\times\mathbb C^{\mathbb N}=E^1,
\qquad
 \boxed{H^1(E^\bullet)\simeq
 \mathbb C^{\mathbb N}/\ell^2(\mathbb N)}
\]
as vector spaces; this identification also respects the quotient locally convex (possibly non-Hausdorff) topology.

For an explicit nonzero cohomology class, put \(y_0=0\) and **\(a_j=1\) for every \(j\ge1\)**. Then \(y_\nu=\sum_{k=0}^{\nu-1}e_k\in H\), satisfying \(Ly_{\nu+1}=y_\nu\), but any compatible primitive would force \(h_0=(1,1,\ldots)\notin H\).

Meanwhile every stage has \(H^1(E_\nu)=0\). Consequently
\[
 \boxed{\Theta^1:H^1(E)\longrightarrow
 \varprojlim_\nu H^1(E_\nu)=0
 \quad\text{is surjective but not injective}.}
\]
This is **exactly** the missing-degree-\(0\)-cohomology-density phenomenon: all **chain-level** transition maps are surjective, but \(H^0(r_\nu)=R\) has closed, nondense range.

## Topology and kernel-density threshold

The subspace \(\ell^2(\mathbb N)\) contains all finitely supported scalar sequences and is therefore **dense** in \(\mathbb C^{\mathbb N}\) with the product topology. Hence \(B^1(E)=\operatorname{im}d\) is a proper dense subspace of \(Z^1(E)=E^1\), and
\[
 \overline{H}^1(E)=Z^1(E)/\overline{B^1(E)}=0,
\]
whereas the **unreduced** cohomology above is nonzero. In fact its quotient topology is indiscrete: every nonempty open saturated subset of \(H\times\mathbb C^{\mathbb N}\) under the dense vector subspace \(H\times\ell^2\) is the whole space. This distinction matters because §2.14 expressly allows nonclosed boundaries.

The same example is a tower of *degreewise short exact* Hilbert sequences
\[
 0\longrightarrow H
 \xrightarrow{h\mapsto(h,0)}
 H\oplus H
 \xrightarrow{(h,y)\mapsto y}
 H\longrightarrow0.
\]
Every middle and right bonding map is surjective. The **kernel** bonding map is \(R\), which fails the dense-image requirement of printed Proposition 2.14.7. The induced inverse-limit map
\[
 \varprojlim(H\oplus H)\longrightarrow\varprojlim H
\]
is **not onto** (it omits the coherent family with all \(a_j=1\)). Thus the kernel-density hypothesis of Proposition 2.14.7 cannot be replaced by surjectivity of the middle and target transitions.

## Classification, dependencies, and proposed editorial note

**Status: verified conditional deduction / sharpness countermodel. Severity: low.** The computation is fully explicit in Hilbert spaces and uses no upstream existence theorem, no external analytic input, and no Demailly regularization. The conditional classification refers only to its placement as an addendum to correctly printed general results.

**Affected statements (only if one weakens their hypotheses):** Theorem 2.14.4 injectivity, Theorem 2.14.6(3), and Proposition 2.14.7 strict exactness. **Not affected:** their actual printed versions, the positive surjectivity conclusion in Theorem 2.14.4, and the previous distinct finding \`POME-INV-LIM-COHOM-SURJECTIVITY-DENSITY-001\`, which tests the *degreewise density requirement for surjectivity* with a different tower.

**Proposed optional reading-edition note (not applied):** After Theorem 2.14.4, distinguish degreewise surjectivity from cohomological density; cite this two-term Hilbert tower as a counterexample to deleting the \(H^{q-1}\) density hypothesis. At Proposition 2.14.7, note that surjective maps on \(B_\nu,C_\nu\) alone do not imply strict exactness if the \(A_\nu\)-transition ranges are nondense.

**Verification scope:** Exact algebraic Hilbert-tower construction, compatibility, inverse-limit computation, quotient topology, and hypothesis comparison checked. No whole-section proof-chain certification, build, code tests, CI, source-body edits, permanent-tag or registry changes, or website publication. The owner-deferred Demailly/Bergman/\(L^2\)/Ohsawa–Takegoshi/multiscale/positivity-loss programme remains **deferred-by-user**, not resolved.
