# Nonpolar compact with a polar boundary spike; Remmert reduction of a zero-ruling cotangent torsor
**Date:** 2026-10-29 (Asia/Shanghai).  
**Reviewed production main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.  
**Audit branch before this pass:** `558b2abca69b5f2e2d118a0cbcb03478bf7413f4`.  
**Scope:** selected proof/model checks in §§3.8.2 and 12.33.3. No entire section or theorem dependency chain is certified.

## POME-PLANAR-GREEN-POLAR-BOUNDARY-SPIKE-001

- **Severity / status:** low / **verified conditional deduction**, **not a false printed theorem**.
- **Exact integrated source:** `docs/sections/planar-green-functions-and-conformal-maps/index.html`; main blob `bfee348bb5f4bbfaa4515e5c9333789a13dae861`, physical lines **53–69**; Proposition **3.8.2**, source key `klimek-pluripotential-theory-886FBC1A`, permanent tag **`3F05222ECC9E`**. The comparison with the already printed polar-boundary exception Example **3.8.3**, tag `FADCC209A003`, lines **73–82**, is contextual only.
- **Hypotheses:** a **nonpolar** compact subset (Ksubsetmathbb C), not a polar compact; its exterior component (Omega), and the polynomial extremal envelope (V_K) with upper-semicontinuous regularization (V_K^*).
- **New explicit check:** let (K=overline{mathbb D}cup{2}). For every polynomial (p) of degree (dge1) with (sup_K|p|le1), the maximum modulus principle on the disc gives (|p(z)|le |z|^d) for (|z|ge1): apply the maximum principle on the exterior to (p(z)/z^d), including its value at infinity. Hence (V_K(z)lelog^+|z|). Conversely, for each (Nge1),
  [
  p_N(z)=rac{z-2}{3},z^N,qquad deg p_N=N+1,
  ]
  satisfies (sup_K|p_N|le1), because it vanishes at (2) and (|z-2|le3) on the unit disc. For each fixed (z) with (|z|>1) and (z
e2),
  [
  lim_{N	oinfty}rac{log|p_N(z)|}{N+1}=log|z|.
  ]
  The constant polynomial (1) supplies the lower bound (0); on the closed disc and at (2), every admissible polynomial has modulus at most (1). Therefore the **raw** polynomial envelope is
  [
  V_K(z)=egin{cases}log^+|z|,&z
e2,\0,&z=2,end{cases}
  quad	ext{whereas}quad V_K^*(z)=log^+|z| 	ext{everywhere}.
  ]
  In particular (V_K(2)=0) but (V_K^*(2)=log2>0). The complement (Omega={|z|>1}setminus{2}) is connected and unbounded; (2) is an isolated polar boundary point, and (lim_{Omega
i z	o2}V_K^*(z)=log2
e0). This **directly proves that the polar exceptional set in the boundary claim of Proposition 3.8.2 cannot be eliminated**, even though (K) itself is nonpolar and (V_K^*) is locally bounded at every finite boundary point.
- **Proposed correction / dependents:** no change to the theorem. Add this optional short worked example after §3.8.2; preserve the distinction between the raw and upper-regularized envelopes. Do not canonicalize “zero on (K)” into “zero on (partialOmega) at every point.” This affects the boundary-zero qualifier in planar Green/equilibrium arguments; it does not alter the existing example of adding unbounded positive harmonic boundary spikes.
- **Limit:** uses the polynomial extremal definition and elementary maximum modulus, not an independent full proof of the Myrberg or polar-exception minimum principles in §3.8.2.

## POME-COTORSOR-A1-REMMERT-001

- **Severity / status:** low / **verified conditional deduction**, **not a false printed theorem**.
- **Exact integrated source:** `docs/sections/a-gauduchon-variational-volume--orders-of-degeneration-at-the-nef-boundary--cotangent-extensions-with-zero-ruling-component/index.html`; main blob `67f63edb723e3cfd5ddb9723cc6061190e473feb`, physical lines **75–99**; Proposition **12.33.3**, source key `non-kahler-pluripotential-theory-B736897D`, permanent tag **`0414E2D53266`**. The zero-ruling coordinate changes are in this file's lines **7–20**, and the previously audited isomorphic *graded section algebra* is Proposition 12.33.2, tag `A78CB65BF75E` (a distinct mathematical statement).
- **Hypotheses and conditional input:** the established zero-ruling cotangent torsor model of the proposition and its printed universal-cover identification (widetilde T_Wsimeqmathbb C^2	imes operatorname{Tot}(mathcal O_{mathbb P^1}(-2))). We do **not** independently certify the torsor's global elliptic-lattice construction.
- **New exact contraction and proof:** on the finite ruling chart of the total space let the base coordinate be (t), the fiber coordinate (y); on the opposite chart set (v=1/t) and (y_infty=-t^2y), as in the printed proposition. The globally holomorphic functions
  [
  A=y,qquad B=ty,qquad C=t^2y
  ]
  satisfy (AC=B^2). On the (v)-chart they read (A=-v^2y_infty, B=-vy_infty, C=-y_infty), so they indeed extend across the two charts. Let
  [
  Q={(A,B,C)inmathbb C^3:AC=B^2}.
  ]
  The map (q:operatorname{Tot}(mathcal O(-2))	o Q) is a biholomorphism away from the zero section and the vertex: if (A
e0), recover (t=B/A, y=A); if (C
e0), recover (v=B/C, y_infty=-C). Its vertex fiber is exactly the compact zero section (mathbb P^1). It is **proper**: the base (mathbb P^1) is compact, and on either of its two compact subcharts the fiber coordinate is bounded by (|A|) or (|C|) on preimages of compact subsets of (Q). Thus (q) contracts precisely the rational curve of normal bundle (mathcal O_{mathbb P^1}(-2)).
  
  To identify global holomorphic functions, lift a holomorphic function on (Qsetminus{0}) along the double-cover parametrization ((s,t)mapsto(s^2,st,t^2)). Its lift is even under ((s,t)mapsto(-s,-t)); Hartogs extension across the origin in (mathbb C^2), locally uniformly in the untouched (mathbb C^2) factor, gives an even entire function. It descends to a holomorphic function on the normal quotient (Q=mathbb C^2/{pm1}). Conversely, every holomorphic function on the total space is constant on its exceptional (mathbb P^1) (compact connected complex curve) and descends over the complement by the explicit inverse; the preceding Hartogs argument extends that function across the vertex. Hence
  [
  H^0(mathbb C^2	imesoperatorname{Tot}(mathcal O(-2)),mathcal O)
  simeq H^0(mathbb C^2	imes Q,mathcal O)
  ]
  by pullback. Since (mathbb C^2	imes Q) is a closed analytic subset of affine space, it is Stein. Therefore (operatorname{id}_{mathbb C^2}	imes q) is the **proper Remmert reduction** of the stated universal cover, with exceptional fibers precisely the projective lines over (mathbb C^2	imes{0}). This sharpens the printed non-Stein assertion: the total space is holomorphically convex but not holomorphically separable.
- **Proposed correction / dependents:** optional corollary after Proposition 12.33.3, preserving the zero/nonzero-ruling distinction and the previously verified graded section algebra equality. Do not infer that equal section algebras identify the torsors or their Stein properties. The proof of the contraction is independent of §12.31/§12.32 dimension counts and of all excluded analytic regularization work. Only the printed global cover identification is a conditional input.
- **Limit:** not a proof that the original base torsor itself is holomorphically convex, nor that every cotangent extension has an analogous Remmert reduction.

## Scope, standing ledger, and exclusions

Only **selected** new nonexcluded passages of §§**3.8.2** and **12.33.3** were directly checked; earlier §3.8.1 and §12.33.2 were used for context without repeating old findings. Both original assertions survive these tests. There is **no new confirmed false theorem, no repaired general proof and no complete section certification**. The existing matrix retains **25 chapters / 747 numbered sections** because production main is unchanged; we did not claim a fresh exhaustive re-count. Every earlier confirmed error, proof gap, candidate, external input and genuine duplication keeps its status.

**Strict user exclusion:** all dedicated Demailly approximation/regularization, Bergman, (L^2), Ohsawa–Takegoshi, multiscale-atlas, and positivity-loss proof-completion records remain **deferred-by-user**, neither certified nor re-opened. No source/body/registry/permanent-tag/main/website updates; no build, GitHub Actions CI, tests, or formalization run.
