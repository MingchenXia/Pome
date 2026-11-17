# Contracting Hopf quotients: the complete connected covering tower

**Finding:** \`POME-HOPF-ALL-CONNECTED-COVERS-CYCLIC-TOWER-001\`  
**Review date:** 2026-11-18  
**Severity/status:** low / **verified conditional deduction**. This is a new corollary, *not* a false printed theorem and *not* a completed audit of all of Chapter 23.  
**Reviewed production main:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`.  
**Reading edition:** \`docs/sections/contracting-hopf-quotients/index.html\`, blob \`d09d9bac3785b78b557ff5178ad7a52b34b20dac\`.  
**Primary anchor:** Theorem 23.3.3, original \`demailly-complex-geometry:371996B7\`, permanent \`D81E3145A1B4\`, physical lines 8–21; its actual integrated proof is at lines 24–51.  
**Iteration anchor:** Eq. 23.3.4, original \`demailly-complex-geometry:F5EE64FF\`, permanent \`436562DE848D\`, lines 29–32.  
**Internal cohomological dependency:** Theorem 10.79.2, original \`demailly-complex-geometry:CDC8E3DF\`, permanent \`F90F5D542AFB\`, \`docs/sections/compact-curves-periods-and-complex-tori--integral-periods-picard-tori-and-albanese-maps/index.html\`, blob \`81ec78509629e15d648cfd3b686fe4d691437330\`, lines 26–35. Its complete general proof chain is **not** certified by this check.

## Exact new conclusion

Let \(F\colon\mathbb C^2\to\mathbb C^2\) be *one of the two forms explicitly stated* in Theorem 23.3.3: either
\[
 F(z,w)=(\lambda_1 z,\lambda_2 w),\quad
 0<|\lambda_1|\le|\lambda_2|<1,
\]
or
\[
 F(z,w)=(\lambda z,\lambda w+z^p),\quad
 0<|\lambda|<1,\quad p\in\mathbb Z_{\ge1}.
\]
Write \(U=\mathbb C^2\setminus\{0\}\), \(X_F=U/\langle F\rangle\), and, for \(m\ge1\), \(X_{F^m}=U/\langle F^m\rangle\). Then:

1. The natural map
   \[
     q_m:X_{F^m}\longrightarrow X_F,\qquad
     [z]_{\langle F^m\rangle}\longmapsto[z]_{\langle F\rangle},
   \]
   is a connected regular unramified **holomorphic** covering of degree exactly \(m\); its deck group is canonically \(\langle F\rangle/\langle F^m\rangle\simeq\mathbb Z/m\mathbb Z\).

2. Every connected unramified holomorphic covering of \(X_F\), up to isomorphism **over \(X_F\)**, is either \(U\to X_F\), the universal (infinite-sheeted) cover, or exactly one \(q_m\). In particular \(q_m\) is the unique connected degree-\(m\) cover over \(X_F\), and no connected finite-sheeted cover of \(X_F\) is simply connected.

3. If \(\eta_F\in H^1(X_F,\mathbb Z)\) and \(\eta_{F^m}\in H^1(X_{F^m},\mathbb Z)\) are the primitive classes with period \(1\) on the loops corresponding respectively to \(F\) and \(F^m\), then
   \[
      q_m^*\eta_F=m\,\eta_{F^m}.
   \]
   The same identity holds for their de Rham real images. For any top-degree smooth form \(\Omega\) on \(X_F\),
   \[
      \int_{X_{F^m}}q_m^*\Omega=m\int_{X_F}\Omega.
   \]
   The integration identity is degree counting for an oriented covering, not an asserted identity of singular Monge–Ampère products.

4. The iterated map \(F^m\) is again, after a **linear coordinate change**, of the corresponding printed family. In the diagonal case the multipliers are \(\lambda_i^m\). In the triangular case,
   \[
   F^m(z,w)=(\lambda^m z,\lambda^m w+c_{m,p}z^p),\qquad
   c_{m,p}=\lambda^{m-1}\sum_{j=0}^{m-1}\lambda^{(p-1)j}\ne0.
   \]
   The linear change \(A(z,w)=(z,w/c_{m,p})\) gives
   \[
     A F^m A^{-1}(z,w)=(\lambda^m z,\lambda^m w+z^p).
   \]
   Thus the finite covering tower stays in the specified diagonal/triangular models. No claim is made for an arbitrary contracting germ not covered by the printed theorem.

## Proof: no classification theorem hidden in the argument

The integrated proof of Theorem 23.3.3 establishes directly that \(U\) is simply connected, that the \(F\)-action is free and properly discontinuous, and that \(U\to X_F\) is a holomorphic covering with \(\pi_1(X_F)=\langle F\rangle\simeq\mathbb Z\). The same argument applies to \(F^m\). Since the subgroup \(\langle F^m\rangle\) has index \(m\) in \(\langle F\rangle\), every orbit of \(\langle F\rangle\) splits into exactly \(m\) orbits of \(\langle F^m\rangle\), giving the degree. The subgroup is normal (the ambient group is abelian), so the residual action gives the stated deck group.

For completeness, the covering classification can be recovered directly from path lifting: pull any connected unramified cover \(Y\to X_F\) back to simply connected \(U\). The pullback is a disjoint union of copies of \(U\). The group \(\langle F\rangle\) permutes these copies, transitively because \(Y\) is connected; choosing one copy identifies its stabilizer with a subgroup \(H\subseteq\mathbb Z\). The cover is isomorphic over \(X_F\) to \(U/H\to U/\mathbb Z\). Every subgroup of \(\mathbb Z\) is \(m\mathbb Z\) for one \(m\ge0\), with \(0\mathbb Z=\{0\}\). The case \(m=0\) gives \(U\); each \(m\ge1\) gives \(X_{F^m}\). The source \(\pi_1(X_{F^m})=m\mathbb Z\simeq\mathbb Z\), hence no finite cover is simply connected. Because \(U\) and \(X_F\) carry holomorphic covering charts, these quotient isomorphisms are holomorphic rather than merely topological.

The map on fundamental groups sends the positive generator \(F^m\) to \(m\) times the generator \(F\). Evaluating the integer-valued period character gives \(q_m^*\eta_F(F^m)=m\), hence the exact first-cohomology pullback. The de Rham conclusion follows from the period comparison in Theorem 10.79.2 (and can also be seen by integrating a closed representative along lifted loops). A local even-dimensional orientation chart of \(q_m\) has degree \(+1\), so summing the \(m\) inverse-image sheets of a partition of unity proves the top-form integration identity.

Finally Eq. 23.3.4 supplies the displayed iterate coefficient. For \(p=1\), \(c_{m,1}=m\lambda^{m-1}\ne0\). For \(p>1\), the sum equals \((1-\lambda^{(p-1)m})/(1-\lambda^{p-1})\), and both numerator and denominator are nonzero because \(0<|\lambda|<1\). Direct substitution of \(A\) proves the stated conjugacy. None of these steps uses Demailly regularization, Bergman kernels, weighted \(L^2\) estimates, Ohsawa–Takegoshi extension, multiscale atlases or positivity-loss arguments.

## Audit classification and dependents

- **Confirmed printed error:** none in the targeted Theorem 23.3.3 or Eq. 23.3.4. The printed proof's freeness, quotient, compactness and fundamental-group passages (lines 26–50) match the hypotheses needed here.
- **New item:** \`POME-HOPF-ALL-CONNECTED-COVERS-CYCLIC-TOWER-001\` — **verified conditional deduction**, with explicit proof above and conditional reliance on the printed covering/fundamental-group construction; no full certification of Theorem 10.79.2 or the rest of §23.3.
- **Possible affected dependents:** descriptions of finite unramified Hopf covers, integral first periods, and the behavior of character line bundles under covers. This is an optional mathematical corollary; no existing theorem is identified as requiring a correction.
- **Proposed edit:** if desired, add a short corollary after Theorem 23.3.3 recording items 1–3 and the iterate normalization. **Proposal only**; do not edit the mathematics/body in this audit branch.
- **Duplication check:** existing audit material on §23.3 includes polynomial scalar conjugacy, meromorphic fields, automorphism centralizers, and the \(S^3\times S^1\) topology. Those are left untouched and are **not** counted as new. The new object is the exhaustive covering tower and its integral-period pullback.
- **Actual scope:** selected §23.3.3 statement/iterates/quotient construction and targeted §10.79.2 period comparison. Both sections previously partly audited: **0 newly first-visited numbered sections; 0 newly fully certified sections**. The fresh main table of contents has **25 chapters and 747 numbered sections**. No build, tests, formal verification or website checks were run.

The user-excluded approximation/regularization and dedicated Bergman/\(L^2\)/Ohsawa–Takegoshi/multiscale-atlas/positivity-loss proof-completion programme remains **deferred-by-user**, neither resolved nor reopened.
