# Divisorial polar mass versus bounded-factor non-pluripolar products

**Date:** 2026-11-06. **Finding:** POME-NPP-DIVISOR-BASE-LOSS-001.
**Classification:** low severity; **verified conditional deduction**, a sharpness/interpretation guard, **not a confirmed error** or repair of a printed theorem.
**Reviewed production main:** b6933b772f41b45918f7e25ed1afbbb1fd892272.

## Integrated reading-edition evidence

- Proposition **13.4.3**, **docs/sections/non-pluripolar-products--bounded-factors-and-the-first-degree-product/index.html**, main blob **d234ab96e33bfd24ad1d53d29332b2c021cddeff**, physical lines **98–125** (statement at 99–103, reduction at 109–125). Source label **foundations-of-pluripotential-theory:38D341C7**, permanent tag **90E0E28D9A95**.
- Lemma **13.4.2**, same reading file, physical lines **72–94**; source **foundations-of-pluripotential-theory:12132441**, permanent tag **5D93FCFBA57F**. Its hypothesis that the base current has no pluripolar mass is indispensable for the stated *general* conclusion.
- Definition **13.2.4** and Lemma **13.2.2**, **docs/sections/non-pluripolar-products--truncation-and-plurifine-locality/index.html**, main blob **81be8c5acc360c96bd3c5acba05a3cdb5fafaf4c**, physical lines **7–13, 34–52, 57–63**. Source labels **foundations-of-pluripotential-theory:9D8E4DD8** and **:CE1D6DA5**, permanent tags **D79952D7E272** and **D59675D9F6D8**.
- The adjacent weighted CLN Lemma **13.4.1** was checked for the scope of its *locally bounded* potential hypothesis (lines **10–15**, plus steps **21–67**), but its full upstream weighted estimate and the general proof chain of Proposition 13.4.3 were **not** independently certified here. The later §13.4.4–5 fiber-Fubini arguments were not re-audited.

## Exact two-dimensional model

Work on \(U=\Delta^2\subset\mathbb C^2\), with the reading-edition convention
\[
 dd^c=\frac{i}{2\pi}\partial\bar\partial,\quad
 \beta_2=\frac{i}{2}\,dz_2\wedge d\bar z_2.
\]
Set \(u(z_1,z_2)=\log|z_1|^2\) and \(v(z_1,z_2)=|z_2|^2\). Then \(u\) is psh and unbounded at the divisor \(Z=\{z_1=0\}\); \(v\) is **smooth, locally bounded and psh**.

First compute the *ordinary* current. In one complex variable,
\[
 \Delta\log|z|^2=4\pi\delta_0,\qquad
 dd^c f=\frac{1}{4\pi}(\Delta f)\,dx\wedge dy
\]
as distributions; the first identity also follows by integrating by parts on a punctured disk and taking its inner-boundary flux. Therefore
\[
 dd^c u=[Z],\qquad dd^c v=\frac{1}{\pi}\beta_2,\qquad
 dd^c v\wedge dd^c u=\frac{1}{\pi}\,\beta_2\wedge[Z]\ne0.
\]
For \(0<r<1\), its mass along the measurable disk \(\{z_1=0,\ |z_2|<r\}\) is **exactly \(r^2\)**, since \(\pi^{-1}\int_{|z_2|<r}\beta_2=r^2\).

Now apply the *actual* non-pluripolar truncation. Put
\[
 u_k=\max(\log|z_1|^2,-k),\quad
 O_k=\{u>-k\}=\{|z_1|>e^{-k/2}\}.
\]
On \(O_k\), \(u_k=u\) is pluriharmonic; hence by ordinary open-set locality of the Bedford–Taylor product
\[
 \mathbf1_{O_k}\,dd^c u_k=0,\qquad
 \mathbf1_{O_k}\,dd^c v\wedge dd^c u_k=0
 \quad\text{for every }k\ge1.
\]
For the two-factor definition, \(v\ge0\) needs no truncation at positive levels, so the displayed mixed restriction is exactly its level-\(k\) non-pluripolar current. In particular both products are locally finite and
\[
 \boxed{\langle dd^c u\rangle=0,\quad
 \langle dd^c v\wedge dd^c u\rangle=0
       =dd^c v\wedge\langle dd^c u\rangle,}
 \qquad
 \boxed{dd^c v\wedge dd^c u\ne0.}
\]
This checks the precise distinction in Proposition 13.4.3: **its base is the non-pluripolar current \(S=\langle dd^c u\rangle\), not the ordinary divisorial current \(dd^c u\)**. Substituting the latter would give a false strengthening, but the printed proposition correctly makes no such substitution.

## General local statement and proof

Let \(g\) be a nonzero holomorphic function on a coordinate domain \(D\), with a nonempty divisor, and set \(u=\log|g|^2\). For any tuple \(v_1,\ldots,v_q\) of locally bounded psh functions, provided \(q+1\le\dim_{\mathbb C}D\),
\[
 \langle dd^c u\wedge dd^c v_1\wedge\cdots\wedge dd^c v_q\rangle=0.
\]
Indeed every level set in Definition 13.2.4 lies in \(\{g\ne0\}\), and \(dd^c u=0\) there because a nowhere-zero holomorphic \(g\) admits a local holomorphic logarithm. The bounded Bedford–Taylor product of the truncations therefore vanishes on that level set by locality. **Every truncated non-pluripolar current is zero, so the limiting product is zero**, without any unjustified interchange of limits. The same argument actually handles further unbounded psh factors at their common finite-level sets; no finiteness hypothesis is needed when every truncated restricted current vanishes.

This statement is *local* and uses a **pure logarithmic-divisor potential** without an additional smooth curvature term. It does not say that all currents with divisorial singularities have zero non-pluripolar mass, nor that ordinary Bedford–Taylor wedge products with divisorial currents vanish.

## Why the no-polar-mass input matters

The same example, with \(T=[Z]\) of bidimension \((1,1)\), explicitly explains Lemma 13.4.2's assumption. This \(T\) is closed and positive but **does charge** the pluripolar set \(Z\), and the locally bounded factor \(v\) yields \(dd^c v\wedge T=\pi^{-1}\beta_2\wedge[Z]\), which also charges \(Z\). The original lemma begins instead with a current whose trace measure gives no mass to any pluripolar set, a property enjoyed by \(S=\langle dd^c u\rangle=0\). The example shows the hypothesis cannot simply be omitted.

## Disposition and dependencies

**Finding POME-NPP-DIVISOR-BASE-LOSS-001:** low / verified conditional deduction; confirmed exact mixed-current contrast and a necessary hypothesis guard. **Not a false statement**, and not a repair of 13.4.2 or 13.4.3. Suggested optional exposition: add this short divisor/smooth-factor example following Proposition 13.4.3, emphasizing the distinction between ordinary and non-pluripolar bases; source/body edits require separate review and are **not performed** here. Affected interpretation: §13.4.2–3 and any subsequent use of bounded-factor insertion (e.g. the multilinear mixed-measure use at §17.2.3, physical line 139, checked as a reference only). No duplicate/canonicalization replacement is proposed.

**Coverage limitation:** direct proof covers this model and the indicated local generalization; it does not certify the general weighted Chern–Levine–Nirenberg argument, theorem 13.4.3's full proof, or any complete section. The earlier selected §13.4 audits (including 2026-10-27 polar examples and 2026-10-31 Borel/fiber integration checks) remain distinct and unchanged. The owner's Demailly approximation/regularization, Bergman, weighted-\(L^2\), Ohsawa–Takegoshi, multiscale and positivity-loss programmes remain **deferred-by-user**, not certified. No tests, project builds, CI, formalization or publication were run.
