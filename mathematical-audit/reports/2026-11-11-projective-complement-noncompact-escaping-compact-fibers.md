# Mathematical audit: an escaping family of compact projective fibers disproves noncompact projective-complement convexity

**Finding:** POME-PROJ-COMP-BASE-ESCAPING-COMPACT-FIBERS-001 — **high / confirmed error** in the noncompact scope of Theorem 11.18.2. The compact-base statement is valid; this is a counterexample to the *printed theorem*, not merely the failure of one proof.

**Reviewed main SHA:** b6933b772f41b45918f7e25ed1afbbb1fd892272. **Previously read audit branch:** 7f39817101bee3652f081647929b5dc342c06988. **Review date:** 2026-11-11.

## Pinned integrated reading

- Main **§11.18**: [integrated section](https://github.com/MingchenXia/Pome/blob/main/docs/sections/gauduchon-metrics-and-linear-mass--convex-norms-and-gauduchon-degrees--curvature-and-projective-complement-exhaustions/index.html), blob **fab309d460a8411fefcd1ef32a094927d6feea10**. Scope/hypotheses at physical lines **10–25**; Lemma 11.18.1 lines **29–45**, source **non-kahler-pluripotential-theory:F8D5B741**, permanent **5022159B8350**; Theorem 11.18.2 lines **51–68**, source **non-kahler-pluripotential-theory:9BF81039**, permanent **B93CB03C68B7**. Theorem 11.18.2 imposes *no compactness* on the base. Its proof at line **67** explicitly assumes the ambient projective bundle is compact. Corollary 11.18.4 lines **91–105**, source **non-kahler-pluripotential-theory:B119F64B**, permanent **18D33491ABFD**, cites this theorem.
- Main **§11.17**: [integrated section](https://github.com/MingchenXia/Pome/blob/main/docs/sections/gauduchon-metrics-and-linear-mass--convex-norms-and-gauduchon-degrees--concave-neighborhoods-and-dual-norms/index.html), blob **d49b7d4f2a213c8b70abfe2f337562202bb58dfb**, physical line **129**. For a complex $N$-fold, $q$-convexity means a smooth real exhaustion with at least $N-q+1$ positive Levi eigenvalues *outside a compact set*.
- Main **§11.3**, [chapter conventions](https://github.com/MingchenXia/Pome/blob/main/docs/sections/gauduchon-metrics-and-linear-mass/index.html), blob **02d635e918120c4026c38d14119db9377eefe61f**, line **7**, fixes $n\ge2$ and a Hermitian form but does **not** assume $X$ compact. Main [general conventions](https://github.com/MingchenXia/Pome/blob/main/docs/sections/conventions/index.html), blob **ef778e54d8d7413242387e95c52269b3c7d42cae**, physical lines **11 and 23**, require paracompactness/Hausdorffness rather than compactness. §11.18 explicitly sets $n\ge1$.

## Counterexample with all printed hypotheses

For any integer $d\ge2$, take the connected smooth complex manifold and positive Hermitian line bundle
$$
B=\mathbb P^d,\quad X=B\times\mathbb C,\quad n=d+1,\quad
E=\operatorname{pr}_B^*\mathcal O_{\mathbb P^d}(1),\quad r=1,
$$
with $h$ the pullback of the standard Fubini–Study Hermitian metric. In affine projective coordinates, the local holomorphic frame of $\mathcal O(1)$ has norm $h(e,e)=(1+\lVert z\rVert^2)^{-1}$. With the printed sign convention $F_h=\bar\partial(h^{-1}\partial h)$,
$$
\mathrm iF_h=\mathrm i\partial\bar\partial\log(1+\lVert z\rVert^2)
$$
is the positive Fubini–Study curvature along the $B$ factor. Consequently, for **every** $(x,v)$ with $v\ne0$, the Hermitian form
$$
\alpha_{h,v}=\mathrm i\,h(F_hv,v)
$$
has precisely $d$ positive complex eigenvalues in the $B$ directions and one zero eigenvalue along the $\mathbb C$ factor. Thus Theorem 11.18.2 applies with $s=d$, where $0\le s\le n$.

It would assert that
$$
U_E=\mathbb P(\mathcal O_X\oplus E)\setminus\mathbb P(\mathcal O_X)
$$
is $(n+r-s)=2$-convex. Since $\dim_\mathbb C U_E=N=d+2$, a $2$-convex exhaustion $\psi$ must have at least
$$
N-2+1=d+1\ge3
$$
strictly positive Levi eigenvalues outside some compact $K\subset U_E$.

The closed infinity divisor $Z=\mathbb P(E)$ lies inside $U_E$. Because $E$ has rank one, $Z\simeq X$. For each $t\in\mathbb C$, it contains the compact complex submanifold
$$
Y_t=\mathbb P(E)|_{B\times\{t\}}\simeq\mathbb P^d,
\qquad\dim_\mathbb C Y_t=d.
$$
These fibers **escape every compact subset** of $U_E$: the image of $K$ under the holomorphic projection $U_E\to\mathbb C$ is compact; choose $t$ outside this image. In particular $Y_t\cap K=\varnothing$. This step is indispensable because the definition permits exceptional compact sets.

Since $Y_t$ is compact, $\psi|_{Y_t}$ attains a maximum at $p\in Y_t$. At $p$, the Levi form of $\psi$ is nonpositive on $T_p^{1,0}Y_t$. Any complex subspace on which the ambient Levi form is positive definite must therefore meet $T_p^{1,0}Y_t$ trivially, and so has dimension at most
$$
\dim_\mathbb C T_pU_E-\dim_\mathbb C T_pY_t
=(d+2)-d=2.
$$
Thus the ambient Levi form has at most **two** positive eigenvalues at $p\notin K$, contradicting the required **$d+1\ge3$**. This proves **non-$2$-convexity** and therefore refutes the unqualified theorem.

The counterexample uses only explicit positive curvature, projective bundle geometry, compactness of $\mathbb P^d$, and the second derivative test at a maximum. It uses **no** excluded regularization or Bergman/L²/extension inputs.

## Repair, classification, dependencies

**Complete conditional repair of Theorem 11.18.2 (proposed, not applied):** Add the hypothesis **“$X$ is compact.”** Then $\mathbb P(\mathcal O_X\oplus E)$ is compact. The printed function $\psi=\chi(G)/G$, extended by zero at infinity, blows up only at the deleted zero section; consequently its finite sublevels are compact. Lemma 11.18.1 gives at least $s+1$ positive Levi directions where $\psi=1/G$ near the deleted section, outside a suitable compact set. This proves precisely $(n+r-s)$-convexity. The local Hessian computation in Lemma 11.18.1 is not challenged.

**Dependents:** Corollary 11.18.4 (tag **18D33491ABFD**) uses the theorem for its positive-mean-curvature assertion; it should explicitly inherit the compact-base qualification or receive an independent noncompact proof. The present model **does not disprove that corollary's weaker $(n+r-1)$-convexity claim**. Its stability/Hermitian–Einstein clause invokes an additional global existence result. Corollary 11.18.5 concerns a compact Hirzebruch surface and is **not** refuted. Definition 11.18.3's degree integral over noncompact $X$ raises separate convergence questions, not necessary here.

**Prior ledger reclassification:** The older **POME-PROJ-COMP-BASE-PROPER-001** (2026-10-23, proof gap) showed only that the specific printed cutoff need not be proper on a noncompact base; that record correctly refrained from declaring the theorem false. The present escaping-projective-fiber argument proves the theorem itself false on an allowed noncompact base. **Keep the older record as historical and superseded by this stronger confirmed-error finding.**

**Severity/status:** high / **confirmed error** for the original noncompact theorem; **verified repair under the compact-base hypothesis**, *not* verification of the original theorem. **Coverage:** only this counterexample and its exact definition/hypothesis/proof anchors; §§11.17 and 11.18 were previously partly examined, **0 new first-visited numbered sections and 0 whole-section mathematical certifications**; the actual ToC remains **25 chapters / 747 sections**. Earlier ledger findings remain intact; excluded Demailly approximation/regularization, dedicated Bergman, L², Ohsawa–Takegoshi, multiscale-atlas and positivity-loss programme remains **deferred-by-user**. No main, source-body, registry, canonicalization, permanent-tag, build, test, CI or website writes.
