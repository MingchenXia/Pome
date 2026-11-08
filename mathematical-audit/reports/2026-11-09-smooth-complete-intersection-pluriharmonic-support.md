# Smooth higher-codimension support for positive currents with order-zero \(\mathrm{dd}^{\mathrm c}\)

**Finding ID:** `POME-PLURI-SUPPORT-SMOOTH-CODIM-001`  
**Date:** 2026-11-09  
**Severity/status:** low / **verified conditional deduction** (a proposed internal corollary, not a false printed theorem or a repair of its proof).  
**Reviewed production main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.  
**Integrated source:** `docs/sections/gauduchon-metrics-and-linear-mass--pluriharmonic-currents/index.html`, blob `046c12d159f8aaeff268c57d822253da11ed41ba`.  
**Original reference:** Lemma 11.22.1, physical lines **11–36**, especially the normal-square test in **17–23**, the positivity argument in **25–33**, and the \(q=1\) conclusion in **35**. Stable source label `non-kahler-pluripotential-theory:9611A9E5`; permanent tag `D9A37BB4C36B`.

## Precisely proved extension

Let \(Z\) be a complex manifold of dimension \(m\), and \(j:Y\hookrightarrow Z\) a **smooth closed complex submanifold of pure codimension \(k\geq1\)**. Let \(R\) be a positive \((q,q)\)-current on \(Z\), \(0\leq q\leq m\), supported on \(Y\), whose \(\mathrm{dd}^{\mathrm c}R\) has order zero (measure coefficients). Then:

1. If \(q<k\), necessarily **\(R=0\)**.
2. If \(q\geq k\), there exists a **unique** positive \((q-k,q-k)\)-current \(S\) on \(Y\) such that \(R=j_*S\).
3. If \(\mathrm{dd}^{\mathrm c}R=0\), then \(\mathrm{dd}^{\mathrm c}S=0\). In particular, for **\(q=k\)** with \(Y\) compact and connected, \(R=c[Y]\) for a unique \(c\geq0\).

The statement requires no Kähler metric, global defining hypersurfaces, or resolution of singularities. It applies to *smooth* embeddings only; no assertion is made for arbitrary singular analytic subsets.

## Full proof, including the endpoint missed by direct iteration

**Zero-degree hypersurface step.** Let \(D=\{z_1=0\}\) be a smooth hypersurface in a coordinate polydisk of complex dimension \(d\geq1\). Suppose \(T\) is a positive \((0,0)\)-current supported on \(D\), with \(\mathrm{dd}^{\mathrm c}T\) of order zero. Positivity makes \(T\) a nonnegative Radon measure distribution. Take a compactly supported test form \(\eta\) of bidegree \((d-1,d-1)\). Since \(|z_1|^2\eta\) vanishes on \(D\) and \(\mathrm{dd}^{\mathrm c}T\) has order zero,
\[
0=\langle\mathrm{dd}^{\mathrm c}T,|z_1|^2\eta\rangle
 =\langle T,\mathrm{dd}^{\mathrm c}(|z_1|^2\eta)\rangle
 =\langle T,\mathrm{dd}^{\mathrm c}|z_1|^2\wedge\eta\rangle .
\]
All terms containing \(|z_1|^2\) or its first derivatives vanish on \(D\); this is legitimate because \(T\) is a measure. Choose \(\eta\) nonnegative, equal near \(D\) to a compactly supported scalar multiple of a positive **horizontal** \((d-1,d-1)\)-volume form. The last test is then a strictly positive multiple of the ambient volume form on the support of \(T\). Varying the scalar cutoff proves \(T=0\). For \(d=1\), take \(\eta\) to be a nonnegative function. Thus the hypersurface support conclusion extends to \(q=0\), where the only possible supported current is zero.

**Preservation of order zero under descent.** Lemma 11.22.1 proves that, when \(q\geq1\), a positive \((q,q)\)-current supported on a smooth hypersurface and having \(\mathrm{dd}^{\mathrm c}\) of order zero factors uniquely as \(i_*T\), with positive \(T\) on the hypersurface. It also proves this locally in dimension \(d=1\): the only relevant case \(q=d=1\) is top bidegree, so a positive measure current supported on a discrete divisor is uniquely a pushforward of positive point masses. Moreover,
\[
\mathrm{dd}^{\mathrm c}(i_*T)=i_*(\mathrm{dd}^{\mathrm c}T).
\]
If the left side has order zero, then so does \(\mathrm{dd}^{\mathrm c}T\): locally, extend each smooth compactly supported test form \(\varphi\) on the hypersurface to a test form \(\widetilde\varphi\) on the ambient space using a fixed tubular projection and normal cutoff, with \(\|\widetilde\varphi\|_\infty\leq C\|\varphi\|_\infty\). The order-zero bound for \(i_*(\mathrm{dd}^{\mathrm c}T)\) yields an order-zero bound for \(\mathrm{dd}^{\mathrm c}T\). This is a local estimate on every compact subset and does not assume closedness of \(T\).

**Induction on codimension.** Near each point of \(Y\), use coordinates \((z_1,\ldots,z_k,w)\) in which \(Y=\{z_1=\cdots=z_k=0\}\). Apply the hypersurface lemma first in \(D_1=\{z_1=0\}\), obtaining a positive current \(T_1\) supported on \(Y\) and with order-zero \(\mathrm{dd}^{\mathrm c}T_1\). Repeat within \(D_1\) using \(z_2=0\), then within \(D_1\cap D_2\), and so on. Each step lowers both the ambient dimension and the current bidegree by one, preserves positivity, and preserves the order-zero condition by the preceding paragraph.

If the bidegree reaches zero before all \(k\) hypersurfaces have been processed, the zero-degree hypersurface step forces that intermediate current, and hence \(R\), to vanish. Otherwise we obtain a positive \((q-k,q-k)\)-current \(S\) on \(Y\) with \(R=j_*S\). Uniqueness follows from injectivity of pushforward by an embedding, and patches the local \(S\)'s into a global current without requiring global hypersurface equations.

Since pushforward commutes with \(\mathrm{dd}^{\mathrm c}\) and is injective, \(\mathrm{dd}^{\mathrm c}R=0\) implies \(\mathrm{dd}^{\mathrm c}S=0\). If \(q=k\), then \(S\) is a nonnegative scalar distribution on \(Y\) with \(\mathrm{dd}^{\mathrm c}S=0\). Distributional Weyl regularity makes \(S\) a smooth pluriharmonic function; on compact connected \(Y\), the maximum principle makes \(S=c\geq0\). The same conclusion is immediate for a zero-dimensional connected \(Y\) (one point).

## Sharpness of the order-zero hypothesis

On a bidisk in \(\mathbb C_z\times\mathbb C_w\), let \(D=\{z=0\}\) and consider the positive order-zero \((1,1)\)-current
\[
R=\delta_{\{z=0\}}\,\frac{\mathrm i}{2}\,dw\wedge d\bar w,
\]
where \(\delta_{\{z=0\}}\) denotes the scalar measure distribution supported on the \(w\)-axis. The current has only a **horizontal** Hermitian matrix component. Therefore it is **not** \(i_*S\) for any positive scalar distribution \(S\) on \(D\): such pushforwards have only the **normal** \(dz\wedge d\bar z\) component. Its \(\mathrm{dd}^{\mathrm c}R\) contains the nonzero second normal derivative \(\partial_z\bar\partial_z\delta_{\{z=0\}}\), a distribution of order two rather than a measure. Thus merely assuming that \(R\) itself has order zero is insufficient. This example explains, rather than contradicts, the precise original hypothesis.

## Scope, dependencies and proposed change

The argument uses the **actual integrated proof** of Lemma 11.22.1 and its local positivity/order-zero calculation, plus elementary local coordinate extension and the maximum principle. This is an internally conditional deduction: the lemma's complete independent dependency chain has **not** been transitively certified. It is independent of the previously logged `POME-PLURI-FIBER-LIOUVILLE-001` and `POME-PLURI-FIBER-HIGHERDIM-001` (both concern fiberwise *descent*, not support on a codimension-\(k\) embedding).

**Proposed change only:** add a separately tagged corollary immediately after Lemma 11.22.1 in the reading edition, keeping its original historical attribution, source label, permanent tag and full statement unchanged. **Affected dependents:** any smooth-stratum support/decomposition argument for positive \(\mathrm{dd}^{\mathrm c}\)-closed currents, in particular the \((k,k)\) rigidity \(R=c[Y]\). Do not apply it without qualification across singular strata. No production source, canonicalization, formalization, CI, or publishing action is authorized by this note.

**Actual coverage:** direct proof-level reading of Lemma 11.22.1 (lines 11–36); contextual source cross-check of §§11.22.2–4 only. Section §11.22 had been selected previously, so **zero new first section visits**, and **no complete mathematical-section certification**. Current main ToC inventory: **25 chapters, 747 numbered sections, zero whole-section certifications**. The owner-excluded Demailly regularization/Bergman/L²/Ohsawa–Takegoshi/multiscale/positivity-loss programme remains **deferred-by-user**, never resolved or certified here.
