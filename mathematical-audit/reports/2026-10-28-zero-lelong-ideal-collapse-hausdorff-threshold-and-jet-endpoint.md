# Selected mathematical audit — 2026-10-28: ideal-order collapse, Hausdorff trace threshold, and sharp jet-pole coefficient

**Reviewed production main:** b6933b772f41b45918f7e25ed1afbbb1fd892272.
**Starting review/mathematical-audit head:** 9bac0ec9e795112180b7af459d01f1d14fee153d.
**Scope:** selected nonexcluded integrated mathematical statements and proof passages in §§5.33, 5.34, and 9.29. **No complete section or upstream proof chain certified.** All historic dedicated Demailly approximation/regularization, Bergman, L², Ohsawa–Takegoshi, multiscale-atlas and positivity-loss completion tasks remain **deferred-by-user**, neither reopened nor resolved. In particular, the existence/smoothing estimates quoted in §9.29 have not been independently audited here.

## POME-IDEAL-ZEROLELONG-COLLAPSE-001

**Severity:** low. **Status:** verified conditional deduction (an additional explicit model, **not** a false printed theorem and **not** a verified repair to production text).

**Integrated anchors:** docs/sections/plurisubharmonic-functions-and-singularities--singularity-type-and-multiplier-ideals/index.html, blob c80624ee98ec8a3500112df6411c98bf4520fa86; Proposition 5.33.2, permanent tag 32843D040902, source non-kahler-pluripotential-theory:C73A1DEC, physical lines 38–45; Example 5.33.3, permanent tag 36A8480CE7DF, source non-kahler-pluripotential-theory:07A23101, lines 50–65. Compare the **already printed** single zero-Lelong unbounded model in §5.34, docs/sections/plurisubharmonic-functions-and-singularities--analytic-types-and-restriction/index.html, blob cff8b3156b07aff2f3d881d83d04608e87b7f2c8, physical lines 57–63. This comparison is essential: the present conclusion about equality of *all* weighted multiplier ideals is an additional calculation, not a claim that the underlying radial function is new.

**Exact model and proof.** On the disc \(D=\{|z|<\mathrm e^{-1}\}\), set \(s=-\log |z|^2\) and, for every \(0<a<1\),
\[
u_a(z)=-s^a\quad (z\ne0),\qquad u_a(0)=-\infty .
\]
The function \(F_a(t)=-(-t)^a\) on \(t<-2\) is increasing and strictly convex:
\[
F_a'(t)=a(-t)^{a-1}>0,\qquad
F_a''(t)=a(1-a)(-t)^{a-2}>0.
\]
Thus \(u_a=F_a(\log|z|^2)\) is subharmonic on the punctured disc and extends subharmonically across the pole by its indicated upper-semicontinuous value. Moreover \(\nu(u_a,0)=\lim_{s\to\infty}s^{a-1}=0\) with the collection's normalization \(\nu(\log|z|^2,0)=1\).

For a nonzero holomorphic germ \(f(z)=z^m h(z)\), \(h(0)\ne0\), and any **real** \(k>0\), local integrability of \(|f|^2\mathrm e^{-k u_a}\) reduces, up to two-sided positive constants, to
\[
\int_{s_0}^\infty \exp\bigl(-(m+1)s+ks^a\bigr)\,ds<\infty.
\]
This integral converges for every \(m\ge0\), since \(s^a=o(s)\). Hence \(\mathcal I(ku_a)=\mathcal O_D\) for **every** \(k>0\), including every positive real noninteger weight. All \(u_a\) have the same ideal type as the smooth zero potential; no claim of equivalence of ordinary singularity types follows.

Indeed, if \(0<a<b<1\), then \(u_b\le u_a\), but \(u_a-u_b=s^b-s^a\to+\infty\) at zero, so \(u_b\preceq u_a\) and \(u_a\not\preceq u_b\). Also \(0\not\preceq u_a\). The single all-weight ideal type of zero therefore contains an **uncountable strictly ordered chain of distinct ordinary singularity types**, all with Lelong number zero.

**Disposition/dependents:** Optional example after 5.33.3, preserving the printed log-pole computation and historical attribution. Use as a semantic guard when comparing ordinary singularity preorders (§16.7), ideal classes and envelopes (§§18.1–18.2). Do not deduplicate ordinary types from multiplier-ideal equality. This is a local example only; no unsupported compact-global realization is asserted.

## POME-HAUSDORFF-TRACE-EXPONENT-SHARP-001

**Severity:** low. **Status:** verified conditional deduction (sharpness of a correct printed assertion).

**Integrated anchors:** docs/sections/plurisubharmonic-functions-and-singularities--analytic-types-and-restriction/index.html, blob cff8b3156b07aff2f3d881d83d04608e87b7f2c8; Corollary 5.34.3, permanent tag C6F4FBF73B9E, source non-kahler-pluripotential-theory:5103AFE8, physical lines 74–87. The line-incidence example 5.34.4 (permanent tag 697E97CED780, source non-kahler-pluripotential-theory; lines 95–132) was separately checked for its \(dd^c=i\partial\bar\partial/(2\pi)\) normalization and summable family; see coverage below.

**Exact sharpness model.** Fix \(1\le j<n\), and take \(A=\{z_1=\cdots=z_j=0\}\subset\mathbb C^n\), a smooth complex plane of dimension \(p=n-j\). The integration current \(T=[A]\) is positive closed of bidegree \((j,j)\). For \(\kappa=dd^c|z|^2\), the trace measure
\[
\mu=T\wedge\kappa^{\,p}
\]
is a positive constant times ordinary \(2p\)-dimensional Lebesgue/Hausdorff volume along \(A\). Every nonempty relatively compact open subset of \(A\) has positive \(\mu\)-mass. For every exponent \(s>2p\), however, a bounded piece of the real \(2p\)-plane \(A\) has zero \(s\)-dimensional Hausdorff measure. Consequently the threshold \(2(n-j)\) in Corollary 5.34.3 **cannot be replaced by any larger Hausdorff dimension exponent** in a universal no-charging statement. Replacing it by a smaller exponent would be a weaker conclusion and is not contradicted.

**Disposition/dependents:** Optional sharpness remark after 5.34.3; preserves the original statement, orientation, current-degree convention, and reference for monotonicity. Relevant to geometric mass/null-set tests and restriction arguments; no claim that the underlying monotonicity theorem is reproved here.

**Independent printed-example check:** In 5.34.4, each projective line \(L_j=\{x-a_jz=0\}\) has current mass one against normalized Fubini–Study form; \(\sum_{j\ge1}2^{-j-1}=1/2\). In local flat coordinates \(dd^c|w|^2=(1/\pi)\sum dx_k\wedge dy_k\), so for an affine complex line at Euclidean distance \(d\) its restricted area in a ball is precisely \((r^2-d^2)_+\), as in physical lines 117–126. The dominated Tonelli limit gives the printed pointwise Lelong number and the nonclosed strict level set \(\{p_j\}\); no new error. Siu's full analyticity theorem and all higher-order current estimates remain prerequisites, not certified by this model check.

## POME-STEIN-JET-WEIGHT-ENDPOINT-001

**Severity:** low. **Status:** verified conditional deduction for the *local vanishing mechanism*; the global interpolation theorem remains conditional on its separately quoted analytic inputs. **No false theorem.**

**Integrated anchors:** docs/sections/separation-strict-exhaustions-and-coverings--discrete-holomorphic-jets-and-the-stein-criterion/index.html, blob 05395f62951e3f992ef7b105424a5f1fe22d4947; Theorem 9.29.1, permanent tag 17CC905E00B7, source demailly-complex-geometry:24E0701D, physical lines 8–16, 18–37 and 61–76; Corollary 9.29.6, permanent tag 476E1C34C3CF, source demailly-complex-geometry:1B882AC9, lines 82–90.

**Exact local calculation.** In \(\mathbb C^n\), let \(h\) be nonzero holomorphic near the origin, with first nonzero homogeneous Taylor term of degree \(m\). On small spheres its mean squared modulus is bounded below and above by positive constants times \(r^{2m}\). For any real \(c\),
\[
\int_{B_\epsilon}|h(z)|^2|z|^{-2c}\,dV(z)<\infty
\quad\Longleftrightarrow\quad
\int_0^\epsilon r^{2m+2n-2c-1}\,dr<\infty
\quad\Longleftrightarrow\quad m>c-n.
\]
The weight exponent selected in 9.29.1 is \(c=n+\ell\). At precisely that endpoint an order-\(\ell\) jet produces the logarithmically divergent radial integral \(\int_0^\epsilon dr/r\), while every order-\(\ell+1\) germ is locally integrable. For **any** smaller coefficient \(c<n+\ell\), the polynomial \(h(z)=z_1^\ell\) is integrable and cannot be forced to vanish at that jet order by this weighted-integrability argument alone. Thus \(n+\ell\) is the *sharp coefficient for this local method*. This neither disproves global interpolation nor excludes alternative proof methods with different weights.

**Other actually read, nonexcluded steps:** Theorem 9.29.1's passage from a fixed weighted local integral to jet vanishing (lines 61–76) respects the \(n\)-dimensional radial Jacobian and the collection's \(\log|z|^2\) convention. In Corollary 9.29.6 (lines 82–90), a noncompact holomorphic hull supplies an exhaustion-escaping closed discrete sequence; interpolating unbounded values contradicts the defining hull inequalities, so the hull step is logically valid *conditional on* 9.29.1. The use of complete Kähler metrics, Richberg smoothing, weighted \(\bar\partial\) existence, and related \(L^2\) input in physical lines 14–58 is **not** independently certified or extended. None of the user-excluded dedicated proof-completion programmes was reopened.

**Disposition/dependents:** Optional explanatory endpoint remark alongside the jet-vanishing argument at 9.29.1, retaining the theorem and its source attribution. Dependents include 9.29.6's Stein separation/convexity and its applications. The conditional status of upstream analytic existence and fixed-weight limiting arguments is unchanged.

## Coverage and boundaries

- **New formerly inventory-only section rows with selected direct, nonexcluded proof/statement checks:** §5.33 (Propositions 5.33.1–2 and Example 5.33.3, lines 7–65), §5.34 (Proposition 5.34.1, Corollary 5.34.3 and Example 5.34.4, selected lines 7–132), and §9.29 (only local weight/jets and hull implications in Theorem 9.29.1/Corollary 9.29.6, selected lines 61–76, 82–90; other passages contextual).
- The §5.34.1 product/max/restriction argument was read for its ideal-power coefficient reconciliation and the connected/non-identically-vanishing restriction hypothesis. The printed statement is consistent. §5.34.3's upper mass bound uses the nondecreasing ball-mass ratio in the **correct direction**. The remaining deep inputs are not certified.
- No contradiction found in these three printed propositions/corollaries. Findings are sharpness and distinction tests, not new confirmed false theorems or production fixes.
- The existing current table of contents has **747 unique numbered sections**. This run upgrades only **three** previously inventory-only rows to precisely delimited selected checks. **Zero complete-section or chapter certifications**; all previous resolved/unresolved/deferred IDs preserved.
- All original source repositories, production main, canonicalization, tags, proof registries, static website, CI, tests and formalization remain untouched. No entire project build, local automated tests, or browser publication check is claimed.
