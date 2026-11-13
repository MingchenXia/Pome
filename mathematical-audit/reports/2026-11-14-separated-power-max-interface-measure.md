# 2026-11-14 mathematical audit: an exact interface Monge–Ampère measure for separated power maxima

**Finding:** `POME-SEPMAX-POWER-INTERFACE-001`  
**Classification:** low / **verified conditional deduction** (a sharp hypothesis test, **not** a false printed theorem or a proof repair).  
**Production baseline:** `main` commit `b6933b772f41b45918f7e25ed1afbbb1fd892272`.  
**Integrated source:** `docs/sections/separated-maximum-monge-ampere-products/index.html`, blob `a859ac5637379266fa191831656f214c51676ca1` (92 physical lines).  
**Precise anchors:** Lemma 7.33.1, source `isolated-plurisubharmonic-singularities:C4DA57C3`, permanent tag `11B8D65C2D19`, line 11; its equation 7.33.2, source `B0DA48D6`, permanent tag `32CB78FC0E95`, lines 12–16; its recurrence/locality proof, lines 20–35. Theorem 7.33.3, source `isolated-plurisubharmonic-singularities:DE8582D3`, permanent tag `F8604F30C7C6`, lines 39–49, and its support-based proof, lines 55–79; formula 7.33.5, source `35C6A147`, permanent tag `5E25FA94CA28`, lines 65–70. This report is based on the **integrated reading edition**, not title-only or source-number-only matching.

## Exact theorem and calculation

Normalize \(\mathrm{d}\mathrm{d}^c=\frac{i}{2\pi}\partial\bar\partial\), as in the integrated §7.33, and use real variables \(r=|z|^2\), \(s=|w|^2\). For **any real exponents \(a,b>0\)**, set on \(\mathbf C^2\)
\[
 f(z)=r^a,\qquad g(w)=s^b,\qquad
 h(z,w)=\max\{r^a,s^b\}.
\]
These are nonnegative and locally bounded plurisubharmonic potentials. If \(\lambda_\rho\) denotes normalized Haar probability on \(\{|z|=\rho\}\subset\mathbf C\), then **as a Bedford–Taylor measure on all of \(\mathbf C^2\)**,
\[
\boxed{
 (\mathrm{d}\mathrm{d}^c h)^2
   =2ab\int_0^\infty t\,
       \bigl(\lambda_{t^{1/(2a)}}\otimes
             \lambda_{t^{1/(2b)}}\bigr)\,\mathrm dt.
}
\tag{A}
\]
The integral denotes a locally finite measure; it has no atom at the origin. Equivalently, away from the coordinate axes, in four-real-dimensional Lebesgue measure with \(\delta\) the one-dimensional Dirac distribution,
\[
\boxed{
 (\mathrm{d}\mathrm{d}^c h)^2
   =\frac{a^2b^2}{\pi^2}
     r^{a-1}s^{b-1}(r^a+s^b)
     \delta(r^a-s^b)\,
       \mathrm dA(z)\,\mathrm dA(w).
}
\tag{B}
\]
In particular, for every \(R,S>0\), with \(\Delta_R=\{|z|<R\}\),
\[
\boxed{
 \int_{\Delta_R\times\Delta_S}(\mathrm{d}\mathrm{d}^c h)^2
   =ab\,\min\{R^{2a},S^{2b}\}^{2}.
}
\tag{C}
\]
The boundary of the box carries zero mass, so either open or closed discs yield the same value.

**Proof without Demailly approximation or any excluded programme.** Work first on \((\mathbf C^*)^2\). Put \(u=r^a\), \(v=s^b\), \(A=\mathrm{d}\mathrm{d}^cf\), \(B=\mathrm{d}\mathrm{d}^cg\), \(C=\mathrm{d}\mathrm{d}^ch\), \(q=u-v\). Since \(A^2=B^2=0\) by their separate variables, the printed bounded-product identity (7.33.2) at \(k=2\) reads
\[
 C^2=C\wedge(A+B)-A\wedge B.\tag{1}
\]
The elementary scalar distributional chain rule for the **real** maximum, valid here for smooth \(u,v\) off the axes, gives
\[
 C=\mathbf1_{\{q>0\}} A+
    \mathbf1_{\{q<0\}} B+
    \delta(q)\frac{i}{2\pi}\partial q\wedge\bar\partial q.
\tag{2}
\]
The hypersurface \(q=0\) is regular on \((\mathbf C^*)^2\). This chain rule also follows from the standard explicit convex smooth maxima
\((u+v+\sqrt{(u-v)^2+\epsilon^2})/2\); no Bergman kernels, \(L^2\), Ohsawa–Takegoshi, atlas or positivity-loss approximation is involved. The first two terms of (2), wedged with \(A+B\), sum to \(A\wedge B\) off a null hypersurface; (1) therefore cancels these terms exactly.

Let \(A_0=(i/2\pi)\mathrm dz\wedge\mathrm d\bar z=\mathrm dA(z)/\pi\) and \(B_0=(i/2\pi)\mathrm dw\wedge\mathrm d\bar w=\mathrm dA(w)/\pi\). On \((\mathbf C^*)^2\),
\[
 A=a^2r^{a-1}A_0,\quad B=b^2s^{b-1}B_0,
\quad
 \partial q=a r^{a-1}\bar z\,\mathrm dz-
            b s^{b-1}\bar w\,\mathrm dw.
\]
The mixed \(\mathrm dz\wedge\mathrm d\bar w\) terms vanish when wedged with \(A+B\), giving
\[
 \frac{i}{2\pi}\partial q\wedge\bar\partial q\wedge(A+B)
 =a^2b^2r^{a-1}s^{b-1}(r^a+s^b)A_0\wedge B_0.
\tag{3}
\]
Thus (1)–(3) establish (B) on \((\mathbf C^*)^2\). Polar coordinates satisfy
\(A_0=\mathrm dr\,\mathrm d\theta_z/(2\pi)\), \(B_0=\mathrm ds\,\mathrm d\theta_w/(2\pi)\). The change \(u=r^a,\ v=s^b\) converts (B) to
\[
 ab(u+v)\delta(u-v)\,
 \mathrm du\,\mathrm dv\,
 \frac{\mathrm d\theta_z}{2\pi}
 \frac{\mathrm d\theta_w}{2\pi}
 =2ab\,t\,\mathrm dt\,
 \frac{\mathrm d\theta_z}{2\pi}
 \frac{\mathrm d\theta_w}{2\pi}
 \quad(u=v=t).
\tag{4}
\]
This proves (A) off the axes and (C). Since \(h\) is locally bounded psh, its bounded Bedford–Taylor top product does **not charge pluripolar sets**, in particular the axes \(\{zw=0\}\); thus there are no omitted axis or origin terms, and (A)–(C) hold globally. That standard no-pluripolar-mass property is an **identified upstream Bedford–Taylor input**, not an independent certification of all its proofs.

For comparison, direct one-variable differentiation gives
\[
 A\wedge B=
 \frac{a^2b^2}{\pi^2}r^{a-1}s^{b-1}\,
 \mathrm dA(z)\,\mathrm dA(w),
\qquad
 \int_{\Delta_R\times\Delta_S}A\wedge B
  =ab\,R^{2a}S^{2b}.
\tag{D}
\]
On any box meeting the interface away from the axes, the measures in (A) and (D) are mutually singular: the former lives on the real hypersurface \(r^a=s^b\), the latter is absolutely continuous with respect to four-dimensional Lebesgue measure. Neither dominates the other as measures. If \(R^{2a}=S^{2b}\), their **total** masses coincide despite this singularity; if the radii are unbalanced, their total masses differ explicitly by (C)–(D).

**Minimal reproducible numerical sanity check (not a proof):** \(a=b=1,R=1,S=2\) gives interface mass \(1\), whereas \(\int A\wedge B=4\). For \(a=2,b=3,R=S=1\), both total masses equal \(6\), although the measures remain mutually singular.

## What this tests in the printed theorem

Theorem 7.33.3 explicitly assumes
\(\mathbf1_{\{f>0\}}(\mathrm d\mathrm d^cf)^p=0\) and
\(\mathbf1_{\{g>0\}}(\mathrm d\mathrm d^cg)^q=0\).
Our \(p=q=1\) functions do **not** satisfy those assumptions: their Hessians are positive on the positive-value loci. Consequently the example is **not a counterexample to the printed theorem**. It proves the top-product identity cannot simply be extended to all nonnegative locally bounded psh functions by dropping the full-mass support conditions, not even in \(\mathbf C^2\). It also distinguishes equality of total masses from equality of Bedford–Taylor measures.

For an additional proof check, the printed Lemma 7.33.1 first uses bounded-product maximum locality to obtain \((h-f)C^k=(h-f)B^k\), then applies \(\mathrm d\mathrm d^c\) and closedness to derive \(C^{k+1}-A C^k=CB^k-AB^k\). In the test class, (1) and the direct interface calculation agree, with **no missing factorial** or negative sign. Theorem 7.33.3 uses its support assumption essentially at physical lines 72–78 to replace \(h\) by \(f\) or \(g\) against the relevant weighted mixed current. Nothing in this audit replaces that step by an unsupported cancellation.

## Classification, proposed correction, dependencies, and precise coverage

- **Severity/status:** low / verified conditional deduction; the original lemma and theorem are **not refuted**. No production correction is mathematically required.
- **Optional proposed edit:** add (A) for \(a=b=1\), or a short warning after Theorem 7.33.3, clarifying that the full-mass-on-zero-set hypotheses cannot be erased and that matching total masses on balanced bidiscs do not imply the measure identity. Preserve original source attribution and both permanent tags.
- **Affected readers/dependents:** direct users of Lemma 7.33.1 and Theorem 7.33.3; product-envelope calculations in §7.33, and local max/BT normalization comparisons in §§7.2–7.3. This is a restriction on an **unclaimed extension**, not a retroactive correction to any theorem.
- **Explicit mathematical inputs not certified here:** local bounded Bedford–Taylor recursion, locality, and the standard absence of mass on pluripolar sets. The interface calculation and elementary scalar distribution chain rule were proved directly. No spectral, PDE, resolution or Demailly-approximation input is used.
- **Actual coverage:** inspected integrated §7.33.1 (lines 11–35), §7.33.3 (lines 39–79), formula 7.33.5 (65–70), and computed a new two-power family exactly. The section **was already partially reviewed** (including previous `POME-BT-SEPMAX-MULTIBLOCK-001` abstract many-block induction and `POME-SEPMAX-WEIGHTED-TORUS-001` weighted log-torus atom). The present family has **diffuse continuum-of-tori interface mass** and fails the support hypotheses, rather than being another supported-zero-set torus atom. **+0 previously unvisited numbered sections, +0 entire-section or chapter certificates**. The current main ToC remains 25 chapters / 747 numbered sections; no claim of all-project verification.
- **Excluded scope:** Demailly approximation/regularization and the dedicated Bergman, \(L^2\), Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof programmes remain **deferred-by-user**, neither reopened nor resolved.
- **Operations:** audit Markdown only on `review/mathematical-audit`; no mathematical source/body/registry/tag changes, main edits, GitHub Actions CI, builds, publication or automated merge. No old arithmetic checks reclassified as new work.
