# Exact Hamiltonian two-form and infinitely many compact periods on the non-Stein open union

**Finding ID:** `POME-STEIN-UNION-HAMILTONIAN-SPHERES-001`  
**Date:** 2026-11-16  
**Severity:** low  
**Status:** verified conditional deduction (an additional independently checked consequence; **not** a confirmed error, proof gap, or certification of the entire section).

## Reviewed sources and immutable anchors

- Reviewed `main`: `b6933b772f41b45918f7e25ed1afbbb1fd892272`.
- Integrated reading edition: `docs/sections/separation-strict-exhaustions-and-coverings--an-increasing-union-of-affine-stein-surfaces/index.html`, blob `26b2e856fc24b04616b0840caec5c688cc045ffa`.
- Section 9.27, source `demailly-complex-geometry:36411603`, permanent section tag `E65337AF838D`.
- Example 9.27.1, source `demailly-complex-geometry:BBFF78A8`, permanent statement tag `F00C66A8D202`. Stage equation and transition maps: physical lines 8–12; simple-root smoothness: 18; open embedding: 22–28; Hausdorff open union: 30; image of the coordinate projection: 32–35; compact-hull argument: 39–46.
- The existing printed example is **not refuted**. Its assertion of a connected non-holomorphically-convex complex surface remains valid. This audit addresses its symplectic geometry and compact two-cycles, not a full proof-chain certification of other sections.

## Statement (new sharp model-level information)

Let (a_j=1/j), (p_\nu(z)=\prod_{j=1}^{\nu}(z-a_j)), (X_\nu=\{(z,w,t)\in\mathbf C^3:wt=p_\nu(z)\}), and (j_\nu(z,w,t)=(z,w,(z-a_{\nu+1})t)) as in Example 9.27.1. Let (X=\bigcup_\nu X_\nu) be the specified increasing union of open holomorphic embeddings.

1. The expression
   [
      \Omega_\nu=\frac{dz\wedge dw}{w}\qquad(w\ne0)
   ]
   extends uniquely to a **nowhere-degenerate holomorphic two-form** on (X_\nu). The (\Omega_\nu) are compatible with (j_\nu) and define a holomorphic symplectic form (\Omega) on the non-Stein surface (X).
2. The compatible action (c\cdot(z,w,t)=(z,cw,c^{-1}t)), (c\in\mathbf C^*), is holomorphic and Hamiltonian:
   [
      \iota_V\Omega=-dz,\qquad V=w\partial_w-t\partial_t.
   ]
   Its fixed points are precisely the distinct (P_j=(a_j,0,0)\in X_j\subset X); they have no accumulation in (X).
3. For each (j\ge1), there is a compact smooth real two-sphere (C_j\subset X_{j+1}\subset X) lying over the interval ([a_{j+1},a_j]), and for **every** polynomial (F\in\mathbf C[z]),
   [
      \int_{C_j} F(z)\Omega
       =2\pi i\int_{a_{j+1}}^{a_j}F(z)\,dz.
   ]
   In particular (\int_{C_j}\Omega=2\pi i/[j(j+1)]\ne0): (\Omega) is not exact as a smooth complex-valued de Rham form, already on (X_2) when (j=1).
4. The classes ([C_j]\in H_2(X;\mathbf C)) are linearly independent. Thus
   [
      \dim_{\mathbf C}H_2(X;\mathbf C)=\infty.
   ]
   The conclusion is about **ordinary compact singular homology**; no claim about the complete cohomology ring or a Stein criterion is made.

## Proof

**Holomorphic extension and nondegeneracy.** On (w\ne0), ((z,w)) are holomorphic coordinates and (\Omega_\nu) is nowhere zero. If (w=0), the defining equation forces (z=a_k) for some (k\le\nu). Since all roots are simple, (p_\nu'(a_k)\ne0), so ((w,t)) are local holomorphic coordinates near the point. Differentiating (wt=p_\nu(z)) yields
[
    t\,dw+w\,dt=p_\nu'(z)\,dz.
]
Consequently on the punctured chart
[
    \frac{dz\wedge dw}{w}
      =\frac{dt\wedge dw}{p_\nu'(z)},
]
which extends holomorphically and is nonzero at (w=0). Uniqueness follows on the dense (w\ne0) locus. As (z,w) are unchanged under (j_\nu), (j_\nu^*\Omega_{\nu+1}=\Omega_\nu), including across (w=0) by analytic continuation. A holomorphic top-degree form on a complex surface is closed, so (\Omega) is symplectic.

**Action.** The vector field (V=w\partial_w-t\partial_t) annihilates (wt-p_\nu(z)), hence is tangent to every (X_\nu). It is compatible with (j_\nu), integrates to the displayed (\mathbf C^*)-action, and on (w\ne0)
[
  \iota_V(dz\wedge dw/w)
     =-dz.
]
Holomorphic continuation establishes the identity everywhere. The fixed-point equations are (w=t=0) and (p_\nu(z)=0), hence the (P_j). Since their projections ((a_j,0)) approach ((0,0)\notin\pi(X)) by the printed formula at lines 32–35, no compact subset of (X) contains an infinite accumulating subsequence of fixed points.

**Spheres and periods.** Fix (j\ge1) and work in (X_{j+1}). On the real interval (I_j=[a_{j+1},a_j]), the polynomial (p_{j+1}) has no zero in the interior, and its real sign there is a constant (\sigma_j\in\{\pm1\}). Parametrize (z(s)=a_{j+1}+s(a_j-a_{j+1})) for (0\le s\le1), and put (r(s)=\sqrt{|p_{j+1}(z(s))|}). For (0<s<1), use the circle
[
  (z,w,t)=\bigl(z(s),r(s)e^{i\vartheta},
       \sigma_jr(s)e^{-i\vartheta}\bigr).
]
This lies on (X_{j+1}). As (s\to0,1), the circles collapse to (P_{j+1}), (P_j); the closed cylinder with end circles collapsed is (S^2). In ((w,t))-coordinates near either end, (r(s)\asymp\sqrt{s}) or (\sqrt{1-s}), with a nonzero smooth positive correction; using (r e^{i\vartheta}) as a real coordinate proves the capped map is smooth and regular there. In the interior,
[
  \frac{dw}{w}=\frac{r'(s)}{r(s)}ds+i\,d\vartheta,
  \qquad
  (F(z)\Omega)|_{C_j}=iF(z(s))z'(s)\,ds\wedge d\vartheta.
]
Integration, followed by the harmless limits at both caps, gives the claimed exact period. For (F=1), it is nonzero. If (\Omega=d\alpha) for a smooth (\alpha), Stokes on the truncated cylinder would express the period as the difference of integrals of (\alpha) on two circles whose lengths tend to zero in smooth local coordinates at the caps, a contradiction.

**Independence.** Suppose a finite relation (\sum_{j=1}^N c_j[C_j]=0) holds. Every (F(z)\Omega) is a closed smooth two-form, so
[
    0=\sum_{j=1}^Nc_j\int_{C_j}F(z)\Omega
     =2\pi i\sum_{j=1}^Nc_j
      \bigl(P(a_j)-P(a_{j+1})\bigr)
]
for (F=P'), with (P\) any polynomial. The (N+1) values (P(a_1),\ldots,P(a_{N+1})) can be prescribed independently by the elementary Lagrange interpolation formula, since the (a_j) are distinct. Their successive differences can therefore be arbitrary; each (c_j=0). As (N) was arbitrary, infinitely many compact sphere classes are independent.

## Verification, classification, and scope

- Directly checked the integrated stage equations, simple roots, open embeddings, and projection image against the pinned HTML lines cited above. Recomputed the form extension, Hamiltonian sign and period normalization, including the (2\pi i) factor.
- An independent exact-rational SymPy check evaluated the determinants of the monomial moment matrices (M_{jk}=\int_{a_{j+1}}^{a_j}z^{k-1}dz), (1\le j,k\le N), for (N=1,\ldots,6). All six determinants were nonzero (a finite check only; the Lagrange argument is the proof).
- **Status:** verified conditional deduction. Its only material input is the existing explicitly defined smooth open-union model; neither a new error in the printed theorem nor a repair of an identified proof gap is alleged.
- **Dependents/context:** Example 9.27.1's non-holomorphic-convexity statement remains untouched; this result adds independent symplectic and ordinary-homology invariants. The adjacent local-separation criterion §9.26.1/.2 is only context, not a new dependency certification. No claim that (X) satisfies the local-separation hypothesis at its fixed points.
- **Exclusions:** no Demailly approximation/regularization, Bergman, L², Ohsawa–Takegoshi, multiscale-atlas or positivity-loss proof programme was inspected or reopened. Those older notes remain **deferred-by-user**.
- **Repository actions:** audit documentation only; no change to mathematical bodies, canonicalization, registry, permanent tags, published website or main. No project test suite, build, CI or publication was run. This is a selected proof-level addition, **not** a complete §9.27 or chapter certification.
