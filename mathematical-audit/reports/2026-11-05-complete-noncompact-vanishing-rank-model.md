# 2026-11-05 — Complete noncompact weak-exhaustion model with nonuniform positive curvature rank

**Finding:** `POME-VANISH-COMPLETE-PUNCTURED-TORUS-NONUNIFORM-001`  
**Severity / status:** **low / verified conditional deduction** (independent explicit geometric model; no false printed theorem, no claim to certify the general analytic proof).  
**Production main reviewed:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.  
**Integrated file:** `docs/sections/hodge-theory-curvature-and-compact-vanishing--semipositive-line-bundle-vanishing-on-weak-exhaustions/index.html`, blob `d3dfb60754a1df99aa6c283d0c54d96fa5a5fa01`.  
**Exact source/reader labels:** Theorem **10.52.1**, `demailly-complex-geometry:8601427A`, permanent `A46DE8D5D789`, physical HTML **lines 7–12**; section `D6A8ACD1845D`. The positive-rank eigenvalue argument and variable damping are printed at **lines 18–46** (Eq. 10.52.3: source `demailly-complex-geometry:E34CD770`, permanent `C7EBF8BB029C`). The later weighted estimates at lines 48–89 were **not audited**, and the excluded weighted-`L^2` programme was not pursued.

## Exact hypothesis tested

Theorem 10.52.1 concerns a weakly pseudoconvex Kähler complex (n)-manifold, a smoothly Hermitian holomorphic line bundle with semipositive curvature and at least (n-s+1) **strictly** positive eigenvalues at every point, (1\le s\le n). It asserts (H^{a,b}_{\bar\partial}(X,L)=0) when (a+b\ge n+s). The earlier, distinct `POME-VANISH-POSRANK-BOUNDARY-SHARP-001` established degree/rank optimality on a **compact** torus. The present review strengthens the *geometric test class*: connected **noncompact complete Kähler** manifolds with a **nonconstant smooth proper strictly subharmonic exhaustion along the noncompact end**, and with **no uniform positive lower eigenvalue bound**. Only the specific model below is verified; no proof of the general vanishing theorem is being supplied.

## A complete Kähler punctured elliptic curve with a proper PSH exhaustion

Let (E=\mathbb C/(\mathbb Z+\mathrm i\mathbb Z)), (p\in E), and let (A=\mathcal O_E(p)) have a smooth positive Hermitian metric (h_A). Such a metric can be obtained by replacing the curvature of any smooth metric by the positive constant area representative of the degree-one class: their difference is an exact mean-zero real ((1,1))-form on the elliptic curve, solved by the scalar Poisson equation. Let (\sigma\in H^0(E,A)) be the canonical section with divisor precisely (p), and (U=E\setminus\{p\}). Pick (C\in\mathbb R) so that
[
 \psi=-\log\|\sigma\|_{h_A}^2+C\ge1\quad\text{on }U.
]
On (U), the Poincaré–Lelong local identity gives
[
 \mathrm i\partial\bar\partial\psi=\theta_A:=\mathrm i\Theta(A,h_A)>0.
]
Since (E) is compact and the section has a simple zero, (\psi\to+\infty) when approaching (p); hence (psi) is a smooth proper strictly subharmonic exhaustion of (U). Set
[
 \omega_U=\omega_E+\mathrm i\partial\bar\partial(\psi^2)
 =\omega_E+2\psi\theta_A+2\mathrm i\partial\psi\wedge\bar\partial\psi.
]
It is a smooth Kähler form. It is **complete**: its associated real metric controls a positive constant times (|d\psi|^2), because of its last term; any curve leaving all compact subsets must satisfy (\psi\to\infty), so its length dominates a fixed multiple of the total variation of (\psi), which diverges. (Equivalently the metric behaves at least like (|dz|^2/|z|^2) close to the puncture.) The positive curvature eigenvalue of (\theta_A) relative to (\omega_U) is positive but tends to zero on the noncompact end: (\omega_U\ge2\psi\theta_A) implies
[
 0<\lambda_{\mathrm{end}}(x)\le\frac{1}{2\psi(x)}\longrightarrow0
 \quad (x\to p).
]
This also shows precisely why a global constant lower spectral gap is unavailable, despite strict positivity **at every point**.

## Product examples and cohomological nonvanishing

For (n\ge1), put (X=E^{n-1}\times U), with the product of (n-1) flat Kähler forms and (\omega_U). It is connected, **noncompact complete Kähler**; the function (\Psi=\psi\circ\operatorname{pr}_U) is a smooth proper PSH exhaustion. For (1\le k\le n), let (L_k) be the tensor product of (\operatorname{pr}_U^*(A|_U)) and (k-1) copies of (\operatorname{pr}_j^*A) on selected compact elliptic factors, carrying product metrics. Its curvature is semipositive with **exactly (k) positive eigenvalues at each point**, and the smallest strictly positive eigenvalue has infimum zero along the puncture. Put (m=n-k); the remaining (m) compact elliptic factors are flat.

There is a nonzero holomorphic section (S) of (L_k), obtained by multiplying the pulled-back canonical sections on its (k) factors. Choose a point of the (k) positive-direction factors where all those sections are nonzero, and write (\Omega=dz_1\wedge\cdots\wedge dz_n) for the global holomorphic top form. The smooth (L_k)-valued form
[
 \gamma=S\Omega\wedge d\bar z_{j_1}\wedge\cdots\wedge d\bar z_{j_m},
]
where (j_1,\ldots,j_m) are the flat compact directions, is (\bar\partial_{L_k})-closed of bidegree ((n,m)). **It is not exact**, including when (m=0): if (m=0), there is no bidegree ((n,-1)) primitive. For (m\ge1), a hypothetical smooth (\gamma=\bar\partial_{L_k}\eta), after contracting with the (k) constant holomorphic vector fields in the positive directions and restricting to the compact slice (E^m), would make a nonzero constant multiple of
[
 dz_{j_1}\wedge\cdots\wedge dz_{j_m}\wedge
 d\bar z_{j_1}\wedge\cdots\wedge d\bar z_{j_m}
]
(\bar\partial)-exact. That is impossible: on forms of type ((m,m-1)), (\partial=0) for degree reasons, so the purported top form would be (d)-exact and have zero integral by Stokes; its actual integral is nonzero. Thus
[
 \boxed{H^{n,n-k}_{\bar\partial}(X,L_k)\ne0,\quad 1\le k\le n.}
]
No compact-support or `L^2` restriction is imposed on the claimed primitive; this is the **smooth analytic** Dolbeault cohomology of the printed theorem.

## Two quantified endpoints and interpretation

**Degree threshold, all (1\le s\le n).** Choose (k=n-s+1\ge1). Then (L_k) meets the printed curvature rank assumption **exactly** and has a positive eigenvalue tending to zero at the puncture, yet (H^{n,s-1}(X,L_k)\ne0). Thus the conclusion cannot be extended to (a+b=n+s-1), **even on connected complete noncompact Kähler manifolds with a proper smooth PSH exhaustion**.

**Rank threshold, (1\le s\le n-1).** Choose (k=n-s\ge1). Then the rank misses the printed assumption by one and (H^{n,s}(X,L_k)\ne0) *inside* the printed degree range. For (s=n), this particular connected noncompact model does **not** test rank-zero at ((n,n)): (k=0) cannot be included in the compact-slice argument because the only noncompact factor would then belong to the alleged top-degree Dolbeault class. The distinct earlier **compact** model already covers that endpoint. No stronger noncompact claim is made.

**Judgment:** the printed Theorem 10.52.1 remains correct. Its pointwise positive-rank hypothesis is meaningfully different from a uniform spectral gap; the global latter would exclude these legitimate complete weak-exhaustion examples. The examples show sharpness of the *unprinted* one-degree/one-eigenvalue relaxations in the stated ranges, **not** a counterexample to the actual theorem. The underlying elementary elliptic-curve section/Poisson facts are standard, with explicit uses above; no user-excluded approximation or weighted-`L^2` proof-completion is involved.

**Proposed source patch (not applied):** optional noncompact complete sharpness remark appended after Theorem 10.52.1, clearly separating the degree/rank endpoints and noting nonuniform eigenvalue positivity. **Affected dependents:** any purported stronger uniform vanishing threshold on complete noncompact weakly pseudoconvex Kähler manifolds; no known printed downstream theorem is false. The theorem's existing analytic proof and its `6.27.12`, `9.50.3` dependencies remain unaudited and unmodified. **Actual coverage:** integrated §10.52.1 statement/hypothesis plus the eigenvalue setup of (10.52.3) and new explicit complete noncompact model; no whole-section certification or project build/CI/site publication.
