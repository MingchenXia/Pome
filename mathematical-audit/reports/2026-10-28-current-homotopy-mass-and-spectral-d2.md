# Current-homotopy mass bounds and a nonzero second spectral differential — 2026-10-28

## Provenance, scope, and status

Reviewed production main: **b6933b772f41b45918f7e25ed1afbbb1fd892272**. Starting audit branch HEAD: **7aa546a53cb1d997f423f79cf74539ef11d92336**.
This is a selective new mathematical audit, not a full section/proof-chain certification. It does **not** address Demailly's plurisubharmonic approximation/regularization, Bergman or weighted L2 estimates, Ohsawa–Takegoshi, multiscale atlases, or positivity-loss completion. Those historical audits retain status **deferred-by-user**, not resolved.

New direct scope: the *real de Rham current-homotopy operator* in §5.54.2, and an independent algebraic second-page stress test of §10.54.2. §5.54.1 and the §10.55.2 double-complex sign convention were inspected only as the necessary, explicitly identified inputs. No global smoothing construction or psh regularization theorem is certified. Original statements inspected below are correct.

### POME-CURRENT-HOMOTOPY-TV-GAP-001

**Status:** verified conditional deduction. **Severity:** low (quantitative strengthening and a sharp warning about topology; *not* an error in the printed theorem).

**Integrated anchors:** §5.54.1 source label <code>demailly-complex-geometry:7A345420</code>, permanent tag <code>A748F8312A04</code>, and §5.54.2 source label <code>demailly-complex-geometry:C92BDA92</code>, tag <code>7D93F6AD9C80</code>. Main file <code>docs/sections/real-currents-submersions-and-homotopies--global-smoothing-and-the-poincare-lemma-for-currents/index.html</code>, Git blob <code>597a770e3f087693b98968c6e5fcf8bcd9ca0841</code>, physical lines **10–35, 40–57, 59–65, 80–81**. The current conventions of §5.53 (tag <code>A76ED2C3D96E</code>) are an internal input, not re-certified here.

**Exact refinement.** On an open subset of Euclidean space, fix the §5.54.1 function with \(0\leq\psi\leq 1/4\), \(|\nabla\psi|\leq1/4\) and the §5.54.2 operators defined using any nonnegative probability density \(\rho_\varepsilon\) supported in \(|v|\leq\varepsilon\). If \(1\leq q\leq m\) and \(T\) is any compactly supported degree-\(q\) current with *finite mass* (coefficient measures of finite total variation), then
\[
  {\bf M}(K_\varepsilon T)\leq C_{m,q}\varepsilon\,{\bf M}(T)
  \quad (0<\varepsilon<1).
\]
This is stronger than the theorem's stated weak \(K_\varepsilon T\to0\) but only for finite-mass currents, **not** for arbitrary currents of positive distributional order. In sharp contrast, the smooth \(R_\varepsilon T\) need **not** converge to \(T\) in mass/total variation, even for an atomic finite-mass current.

**Complete direct proof of the bound.** For the homotopy \(H_v(t,x)=x+t\psi(x)v\), its spatial differential satisfies
\[
  \|d_xH_v\|\leq1+\varepsilon/4\leq5/4,
  \qquad |\partial_tH_v|=|\psi(x)v|\leq\varepsilon/4.
\]
Pair \(K_\varepsilon T\) with a compactly supported smooth \((m-q+1)\)-form \(\eta\) of pointwise comass at most \(1\). In the pullback to \([0,1]\times\Omega\), the term paired with \([0,1]\otimes T\) has **exactly one** \(dt\) factor. That term contains \(\partial_tH_v\), while the remaining \(m-q\) factors have norm at most \(5/4\). The resulting pulled-back test has supremum norm at most \(C_{m,q}\varepsilon\), and, for a fixed compact support of \(\eta\), its spatial support is uniformly compact by §5.54.1. The measure-coefficient pairing is therefore bounded by \(C_{m,q}\varepsilon{\bf M}(T)\). Integrate in \(t\) and then against the probability density \(\rho_\varepsilon\), and take the comass-test supremum. This proves the claimed mass bound without assuming sequential compactness or exchanging singular limits.

**Exact one-dimensional sharpness model.** Let \(\Omega=\mathbb R\), \(y\in\Omega\), \(T=\delta_y\) regarded as a degree-one current, and choose a standard even nonnegative mollifier \(\rho_\varepsilon(v)=\varepsilon^{-1}\rho(v/\varepsilon)\) supported in \([-\varepsilon,\varepsilon]\), with integral \(1\) and nonzero first absolute moment. Put \(a=\psi(y)>0\). Then, on test functions \(g\),
\[
 (R_\varepsilon\delta_y)(g)
     =\int\rho_\varepsilon(v)g(y+av)\,dv,
\]
so \(R_\varepsilon\delta_y\) has the smooth probability density
\(a^{-1}\rho_\varepsilon((x-y)/a)\,dx\). It is mutually singular with \(\delta_y\), hence
\[
   \|R_\varepsilon\delta_y-\delta_y\|_{\mathrm{TV}}=2
   \quad\text{for every }\varepsilon>0.
\]
On a compactly supported one-form \(g(x)\,dx\), the degree-zero homotopy current acts (up to the global convention sign, irrelevant for mass) as
\[
 (K_\varepsilon\delta_y)(g\,dx)
   =\int\rho_\varepsilon(v)
          \left(\int_y^{y+av}g(s)\,ds\right)dv.
\]
Contributions from \(v>0\) are nonnegative densities supported on \(x>y\), and those from \(v<0\) are nonpositive densities supported on \(x<y\); there is no overlap/cancellation in their variation. Consequently
\[
  {\bf M}(K_\varepsilon\delta_y)
     =a\int |v|\rho_\varepsilon(v)\,dv
     =a\varepsilon\int|w|\rho(w)\,dw.
\]
The linear \(\varepsilon\) decay is optimal even for an atomic order-zero current.

**Proposed action / dependents:** An optional remark after §5.54.2 can distinguish weak convergence of \(R_\varepsilon T\) from strong mass convergence of the homotopy correction. Do **not** strengthen the theorem to strong convergence of \(R_\varepsilon T\); that would be false. This matters for downstream uses of currents, de Rham comparison and trace operations, but does not identify a faulty printed theorem or an upstream Demailly approximation obligation.

### POME-SPECTRAL-D2-ZIGZAG-001

**Status:** verified conditional deduction. **Severity:** low (sign and indexing stress test; printed spectral-sequence theorem correct).

**Integrated anchors:** §10.54.2 source label <code>demailly-complex-geometry:311B37F9</code>, tag <code>E83B7568FE4B</code>; main file <code>docs/sections/spectral-sequences-support-and-cup-products--filtered-complexes-and-spectral-sequences/index.html</code>, Git blob <code>2d26dcf0ea764f1d8823bae057dc951063053a50</code>, physical lines **17–58**. The context for the total differential and the finite-diagonal convention is §10.55.2, source <code>demailly-complex-geometry:F6A52A0C</code>, tag <code>D461C5DFED48</code>, main file <code>docs/sections/spectral-sequences-support-and-cup-products--hypercohomology-and-direct-image-spectral-sequences/index.html</code>, blob <code>83ea6c60c0691a7e3559214e363361863f3ea2a2</code>, lines **7–16, 38–56**. The latter is a contextual convention, not a new certification of the sheaf cohomology comparison.

**Model and full computation.** Let \(k\) be a field, and consider a bounded first-quadrant double complex with only four nonzero vector spaces:
\[
 C^{0,1}=ka,\quad C^{1,0}=kb,\quad
 C^{1,1}=kc,\quad C^{2,0}=kd.
\]
Declare the horizontal arrows \(a\mapsto c\), \(b\mapsto d\), and the vertical arrow \(b\mapsto c\) to be the identity on the chosen generators; all other arrows vanish. The double-complex identities hold (all possible composites land in zero groups). With the §10.55 totalization convention \(D=d_h+(-1)^p d_v\), one obtains
\[
 D(a)=c,\qquad D(b)=d-c.
\]
The total degree-one to degree-two differential has matrix
\[
  \begin{pmatrix}1&-1\\0&1\end{pmatrix}
\]
in bases \((a,b)\), \((c,d)\), so the total complex is acyclic.

Filter by column \(p\). On the first page, the vertical complex in column \(1\) is \(kb\xrightarrow{\sim}kc\) and is acyclic; thus the only nonzero terms are
\[
 E_1^{0,1}=k[a],\qquad E_1^{2,0}=k[d].
\]
There is no possible \(d_1\), hence \(E_2=E_1\). The class \([a]\) has an \(E_2\)-representative \(x=a+b\), since the added \(b\) lies in the next filtration step and cancels the column-one boundary:
\[
 D(a+b)=c+(d-c)=d\in F^2.
\]
By §10.54.2's representative rule, \(d_2[a]=[d]\), a nonzero isomorphism \(E_2^{0,1}\xrightarrow{\sim}E_2^{2,0}\). Therefore \(E_3=0\), agreeing with the directly computed vanishing of total cohomology. No unproved limit interchange, sequence-compactness claim or analytically excluded input is involved.

**Proposed action / dependents:** Optional short example at §10.54.2 to verify indexing and the \((-1)^p\) convention, illustrating that a bounded double complex can have nonzero \(d_2\); neither a second-page degeneration nor a canonical splitting is claimed in Pome. This is independent of the prior 2026-10-25 audit of §10.54's general page algebra and is not a duplicate of an earlier filed finding.

## Precise coverage and exclusions

First direct selected **non-psh** current-homotopy/mass-convergence passage in previously inventory-only §5.54, without inspecting/endorsing any analytic singularity regularization or global smoothing proof programme. Incremental, independent algebraic stress test in previously selected §10.54.2; §10.55 totalization signs only contextual. Main ToC still has **25 chapters / 747 section rows**; **zero** whole-section or chapter certifications. Neither result is a false Pome theorem, a completed proof-chain repair, or a formal verification.

Prior findings and their confirmed error / proof gap / candidate / external dependency / duplication / deferred-by-user statuses remain untouched. The Demailly approximation/regularization and dedicated Bergman, L2, Ohsawa–Takegoshi, multiscale-atlas and positivity-loss programme remain **deferred-by-user**, not solved or certified.

Only this Markdown report and audit ledgers/matrix are proposed for the review branch. No edits to production main, source bodies, registry, permanent tags, website, CI, builds, tests or automatic publication.
