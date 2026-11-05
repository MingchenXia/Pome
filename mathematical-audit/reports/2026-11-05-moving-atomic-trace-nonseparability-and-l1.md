# Moving atomic traces: nonseparability of the singularity metric despite L1 continuity

Date: **2026-11-05**. Finding **POME-TRACE-MOVING-ATOMS-NONSEPARABLE-L1-001**; **low / verified conditional deduction**. This note reviews a previously unreviewed part of Chapter 20 and proves a new topology consequence of the *printed, correct* metric comparison. It neither challenges a source statement nor certifies its entire analytic dependency chain.

## Reviewed production text, labels and limitations

Production **main** at **b6933b772f41b45918f7e25ed1afbbb1fd892272**. Integrated reading file **docs/sections/restriction-and-intrinsic-trace-data/index.html**, blob **dbc3b722ceacb8232fe4c7b711e5ad98b0708f06**:

- **Lemma 20.3.20**, source **non-kahler-pluripotential-theory:72AC7E8E**, permanent tag **A374F6B4426E**: lines **399–429**, identifying an atomic measure D of mass at most A with a normalized ideal envelope q_D, its singularity class, and non-pluripolar mass A-D(Y).
- **Theorem 20.3.21**, source **non-kahler-pluripotential-theory:12E10B47**, permanent tag **2432A5A2AE14**: lines **435–465**; for positive atomic D,E of mass < A,
  \[
    \frac1{96}\|D-E\|_{\mathrm{TV}}
    \le d_{S,\beta}(q_D,q_E)
    \le \frac12\|D-E\|_{\mathrm{TV}}. \tag{1}
  \]
  The printed proof uses an ordered-potential distance formula, the comparison with two rooftop distances (factor 48), and the fact that the maximum has atomic part D wedge E. Those upstream steps are **assumed as printed**, not independently recertified here.
- **Corollary 20.3.22**, source **non-kahler-pluripotential-theory:6182A818**, permanent tag **D416A3AB0845**, lines **471–482**: completeness, density of analytic envelopes, and *non-total-boundedness*. Its existing final proof already gives infinitely many separated atoms. Our results below go further: **uncountably** many, plus convergence in L1 and weak currents but discontinuity in d_S.
- **Definition 18.4.1**, source **non-kahler-pluripotential-theory:4F9BDFEC**, permanent tag **F1F202AEE8FD**, at **docs/sections/multiplier-ideal-envelopes-and-goodness--ideal-projection/index.html**, blob **f1979b73c857f4874dd4a5cb10b93bcc047ebbdc**, lines **11–18**: ideal envelopes as regularized suprema of nonpositive theta-psh competitors in a fixed all-weight ideal class. Only the elementary equivariance of this *definition* is needed below.

Chapter index **docs/chapters/divisors-restriction/index.html**, blob **82cde7a874dde022c4287d5b1fc78cbab3f7bc5d**, lists the **eight current numbered sections 20.1–20.8**. This review is restricted to the indicated three statements of **§20.3** plus a **definition-only crosscheck** in §18.4. No entire section or chapter is certified.

## Result A: even positive-mass ideal-envelope metric spaces are nonseparable

Let Y be any connected compact Riemann surface, let beta be any smooth positive (1,1)-form, set A = integral_Y beta > 0, and choose epsilon with 0 < epsilon < A. Fix once and for all a real number a with 0 < a < A-epsilon. For each p in Y, let
\[
  D_p := a\delta_p,\qquad q_p:=P_\beta[w_{D_p}]_{\mathcal I},
\]
where w_D is the Green representative of Lemma 20.3.20.

The printed lemma gives
\[
  \int_Y\mathrm{MA}_\beta(q_p) = A-a >\varepsilon ,
\]
so every q_p belongs to the **same** positive-mass subspace of Corollary 20.3.22. If p and r are distinct, the mutually singular atomic measures have
\[
  \|D_p-D_r\|_{\mathrm{TV}} = \|a\delta_p-a\delta_r\|_{\mathrm{TV}}=2a.
\]
By (1),
\[
  \boxed{\quad a/48\ \le\ d_{S,\beta}(q_p,q_r)\ \le\ a
  \qquad(p\ne r).\quad} \tag{2}
\]
Since the set of points of a compact Riemann surface is uncountable, (2) exhibits an **uncountable, uniformly separated** subset of the complete metric space in Corollary 20.3.22. A separable metric space cannot contain such a subset: balls of radius a/192 about these points are pairwise disjoint, and a countable dense set would have to meet all these open balls. Thus this complete metric space is **not separable**. This strengthens, but does not contradict, the already printed observation that it is *not totally bounded*.

This uses only the elementary geometry of atoms and (1), and applies to **every** smooth compact curve and every positive background beta. No curve-specific classification or outside approximation result is invoked.

## Result B: L1 and weak-current convergence do not imply singularity-metric convergence

For a completely explicit geometry, take
\[
  Y=E:=\mathbb C/(\mathbb Z+i\mathbb Z),\qquad
  \beta=\frac{i}{2}\,dz\wedge d\bar z,\qquad
  \int_E\beta=1.
\]
Our convention is \(dd^c=\frac{i}{2\pi}\partial\bar\partial\). Fix \(0<a<1\); let G(z,p) be the translation-invariant Green kernel for \(dd^c\), shifted by a constant so that G is nonpositive, with
\[
  dd^c_zG(z,p)=\delta_p-\beta,\qquad G(z,p)=g(z-p).
\]
The logarithmic singularity of g is locally integrable, so g belongs to L1(E). Then
\[
  w_p(z)=aG(z,p),\qquad
  \beta+dd^cw_p=a\delta_p+(1-a)\beta\ge0. \tag{3}
\]
Let \(q_p=P_\beta[w_p]_{\mathcal I}\). As a direct consequence of Definition 18.4.1, for any translation \(T_h(z)=z+h\), pullback preserves beta, the nonpositive constraint and the all-weight multiplier ideals. It therefore bijects the two entire competitor families, commutes with their upper-semicontinuous regularized suprema, and yields the **exact identity**
\[
  q_p(z)=q_0(z-p). \tag{4}
\]
There is no limiting approximation or interchange of independent limits in this argument.

For any \(p_j\to0\) with \(p_j\ne0\), the standard **strong continuity of translations on L1(E)** gives
\[
  \|q_{p_j}-q_0\|_{L^1(E,\beta)}\longrightarrow0. \tag{5}
\]
For completeness, approximate the integrable q_0 in L1 by a continuous function f. Translations preserve the L1 norm of the error, while uniform continuity of f makes \(\|f(\cdot-p_j)-f\|_1\to0\). The triangle inequality proves (5). The q_p are indeed L1 functions because they are nontrivial quasi-psh functions on a compact complex manifold.

Equation (5) implies **weak convergence of their entire curvature currents**:
\[
 \beta+dd^cq_{p_j}\ \rightharpoonup\ \beta+dd^cq_0 ,
\]
since \(dd^c:L^1_{\mathrm{loc}}\to\mathcal D'\) is continuous. Their atomic curvature measures \(a\delta_{p_j}\) converge weakly to \(a\delta_0\). Nevertheless, by (2),
\[
 \boxed{\quad d_{S,\beta}(q_{p_j},q_0)\ge a/48
          \quad\text{for every }j.\quad} \tag{6}
\]
So even **L1 convergence of normalized ideal envelopes plus weak convergence of complete curvature currents does not imply d_S convergence**, despite uniform positive non-pluripolar mass \(1-a\).

The same proof shows discontinuity of the *action* of the translation group at a singular envelope: \(T_{p_j}\to\mathrm{id}\) smoothly but \(q_0\circ T_{-p_j}\not\to q_0\) for d_S. Individual translations do preserve the metric by invariance of all defining operations; it is the dependence on a translation tending to the identity which fails.

## Status, correction proposal, dependents, and exclusions

**Classification:** **low / verified conditional deduction.** Lemma 20.3.20, Theorem 20.3.21 and Corollary 20.3.22 remain **correct** as printed; no false statement, missing hypothesis, duplicate entry, or proved general theorem repair is asserted. The independently checked part is the atomic total-variation calculation, uncountable separation, translation-equivariance of the actual envelope definition, and the L1/weak-current convergence argument. The metric inequality (1) and its dependencies (including the printed ordered-distance and rooftop comparisons) are accepted **conditionally**.

**Proposed optional addition:** after Corollary 20.3.22, add a remark distinguishing nonseparability and the strong d_S topology from L1 and current-weak convergence, using (2)–(6). Retain the current theorem, labels, hypotheses, original references and attribution without edits. This observation matters for any attempted sequential/compactness argument involving **§20.3.20–22**, the **Kähler trace comparison in §20.3.17**, and later trace or model-envelope topologies; it does not on its own identify an invalid downstream argument.

**Unreviewed:** the general proof of Theorem 20.3.21 from the upstream rooftop-distance estimate; §§20.1–20.2, 20.4–20.8 and the rest of §20.3; higher-dimensional intrinsic trace constructions, and any dependent Monge–Ampère/regularity theorem. The excluded Demailly approximation/regularization and dedicated Bergman, weighted-L2, OT, multiscale-atlas and positivity-loss programme stays **deferred-by-user**, not reviewed here. No production edits, formal verification, builds, tests, CI, or publication.
