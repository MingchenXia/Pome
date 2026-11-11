# Sharp mixed non-pluripolar power-sum threshold for two zero-Lelong potentials

**Date:** 2026-11-11. **Reviewed production main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.
**Stable ID:** `POME-NPP-MIXED-POWER-SUM-THRESHOLD-001`. **Severity/status:** **low / verified conditional deduction**. The printed results are correct; this is a quantitative extension, **not** a confirmed error or complete proof-chain certification.

## Primary integrated statements, labels, and anchors

- `docs/sections/non-pluripolar-products--truncation-and-plurifine-locality/index.html`, blob **`81be8c5acc360c96bd3c5acba05a3cdb5fafaf4c`**.
- Lemma **13.2.2**, source `foundations-of-pluripotential-theory:CE1D6DA5`, permanent `D59675D9F6D8`, physical lines **34–52**. Its local-finiteness criterion Eq. **13.2.3**, source `:F86748C9`, permanent `E88E33ACAD5B`, lines **36–40**, requires uniformly bounded compact trace mass.
- Proposition **13.2.6**, source `foundations-of-pluripotential-theory:E82F0D73`, permanent `7F7123F92478`, lines **80–125**: plurifine locality and multilinearity for locally finite products.
- Example **13.2.9**, source `foundations-of-pluripotential-theory:2F8E45A2`, permanent `6F4C920FEDCA`, physical lines **151–165**: the single power $a=1/2$.
- Smooth determinant normalization Eq. **7.2.4**, permanent `706A589A680C`, `docs/sections/bedford-taylor-products-and-local-capacity--bounded-potentials-and-recursive-products/index.html`, verified main blob `18bd2395f3b76941b2c677079c09eb6accc5a9cb`.
- Theorem **13.3.1**, permanent `8A125B338F90`, `docs/sections/non-pluripolar-products--closedness-and-cutoff-gradients/index.html`, blob `f781fa61bd20944c7c4798e0e0984cfb81ef069f`, lines **10–47**, considered only as a dependent/internal premise.

## Statement (exact new unequal-exponent case)

Fix real $0<a,b<1$ and $0<c<\min(1-a,1-b)$. On
\[
 U_{a,b,c}=\{(x,y)\in\mathbb C^2:|x|^2<c,\ |y|<e^{-1}\}
\]
put $L=-\log|y|$ and
\[
 u_s(x,y)=(|x|^2-1)L^s\quad(s=a,b,\ y\neq0),\qquad
 u_s(x,0)=-\infty .
\]
Both $u_a$ and $u_b$ are plurisubharmonic, and **both have zero Lelong numbers along $y=0$**. Their mixed non-pluripolar product is locally finite **if and only if**
\[
\boxed{a+b<1.}
\]
Set $r=|x|^2$, $A=a(1-a)+b(1-b)$ and $B_{a,b}(r)=A(1-r)-2ab\,r$. On $y\neq0$, with zero extension across the pluripolar axis, the exact cutoff-limit measure is
\[
\boxed{
d\mu_{a,b}=
\frac{B_{a,b}(|x|^2)}{4\pi^2|y|^2L^{2-a-b}}\,dA(x)dA(y).}
\]
When $a+b<1$, for every $0<R^2<c$ and $T>1$, its compact-cylinder mass is exactly
\[
\boxed{
\mu_{a,b}\{|x|\le R,\ |y|\le e^{-T}\}
=\frac{A R^2-\frac12(A+2ab)R^4}{2(1-a-b)}\,T^{a+b-1}.
}
\]
At $a+b=1$ the mass of an inner annular cutoff $e^{-S}\le|y|\le e^{-T}$ grows proportionally to $\log(S/T)$; at $a+b>1$ it grows proportionally to $(S^{a+b-1}-T^{a+b-1})/(a+b-1)$. In both cases the non-pluripolar mixed product **fails** local finiteness on every neighborhood of the axis.

## Proof and normalization audit

For each $s\in\{a,b\}$, direct differentiation away from $y=0$ gives
\[
 (u_s)_{x\bar x}=L^s,\qquad
 (u_s)_{x\bar y}=-\frac{s\bar x}{2\bar y}L^{s-1},
 \qquad
 (u_s)_{y\bar y}=\frac{s(1-s)(1-r)}{4|y|^2}L^{s-2},
\]
and
\[
 \det((u_s)_{j\bar k})
 =\frac{s(1-s-r)}{4|y|^2}L^{2s-2}>0
 \qquad(r<c<1-s).
\]
The positive $(x,\bar x)$ minor and determinant prove strict plurisubharmonicity off the axis. On compact subsets in $x$, $(r-1)L^s$ tends uniformly to $-\infty$ as $y\to0$ and is locally bounded above. Its $-\infty$ extension is psh by exactly the polar-removal input used in Example 13.2.9. At $(x_0,0)$, the supremum on balls of radius $\rho$ has negative growth of order $(\log(1/\rho))^s$, hence its ratio to $\log\rho$ tends to zero because $s<1$. Thus every axial Lelong number vanishes.

For smooth Hessians $H_a,H_b$, the **polarization of determinant** gives the mixed coefficient
\[
\begin{aligned}
D(H_a,H_b)
&=(H_a)_{x\bar x}(H_b)_{y\bar y}
 +(H_b)_{x\bar x}(H_a)_{y\bar y}\\
&\quad -(H_a)_{x\bar y}(H_b)_{y\bar x}
 -(H_b)_{x\bar y}(H_a)_{y\bar x}\\
&=\frac{[a(1-a)+b(1-b)](1-r)-2ab\,r}
       {4|y|^2}L^{a+b-2}.
\end{aligned}
\]
It is strictly positive because the two Hessians are positive definite. In Pome's convention $dd^c=(i/2\pi)\partial\bar\partial$, the mixed smooth wedge has density $D(H_a,H_b)/\pi^2$ relative to $dA(x)dA(y)$. At $a=b$, $D(H_a,H_a)=2\det H_a$, recovering Eq. 7.2.4 and the registered diagonal audit exactly.

By bounded Bedford–Taylor plurifine locality, every high enough truncated mixed product agrees with this smooth wedge on a compact set away from the polar axis. The cutoff-limit measure gives zero mass to the axis and therefore coincides with this density extended by zero; here no **a priori** assertion of local finiteness is needed, only the increasing Borel trace measures supplied in §13.2.

The decisive integral is
\[
\int_{0<|y|\le e^{-T}}\frac{dA(y)}{|y|^2 L^{2-a-b}}
=2\pi\int_T^\infty t^{a+b-2}\,dt.
\]
It converges exactly for $a+b<1$, where it equals
$2\pi T^{a+b-1}/(1-a-b)$. The remaining factor integrates over the $x$-disk to
\[
\int_{|x|\le R}B_{a,b}(|x|^2)\,dA(x)
=\pi\left[A R^2-\frac{A+2ab}{2}R^4\right].
\]
Multiplication proves the exact displayed cylinder formula. For $a+b\ge1$ the positive integral diverges on any cylinder centered on the axis. The equivalence with the trace criterion Eq. 13.2.3 now establishes the locally finite versus infinite dichotomy.

**Genuinely mixed phenomenon:** choose $a=1/8$, $b=3/4$ and $c<1/4$. Then $a+b=7/8<1$, so the mixed product is locally finite, while $2b=3/2>1$ and the **self-product of $u_b$ is not**. Thus existence of a mixed product cannot be inferred from local finiteness of *each diagonal product* in the converse direction; neither zero Lelong numbers nor first-degree local finiteness is sufficient to guarantee a self-product. This is new relative to the diagonal-only October 30 finding `POME-NPP-POWER-SINGULARITY-THRESHOLD-001`, whose status is unchanged.

## Classification and boundaries

**Verified conditional deduction / low:** no false printed statement, no proof gap newly claimed, no duplicate canonization proposed. The calculation is self-contained once the established psh extension, bounded BT locality, smooth determinant formula and §13.2 trace criterion are granted; **their full upstream proofs are not certified by this model**.

**Proposed correction (not applied):** optional short mixed-parameter remark following Example 13.2.9, highlighting the strict sum threshold, exact wedge density, and the $a=1/8,b=3/4$ distinction. **Affected dependent contexts:** §§13.2–13.5 local finiteness and multilinearity; §13.14 global products; any energy argument using mixed products. All old unresolved and external-dependency ledgers remain unchanged.

**Actual coverage:** new computation of the selected §13.2.2/.6/.9 passages, with contextual §13.3.1 and Eq. 7.2.4. §13.2 was already partially reviewed: **0 first-visited numbered sections, 0 fully certified sections**, actual ToC **25 chapters / 747 sections**. Demailly approximation/regularization and its dedicated Bergman, L², Ohsawa–Takegoshi, multiscale atlas and positivity-loss proof programme remain **deferred-by-user**, neither reopened nor certified. No source/body, tags, registry, main, website, build, CI or formalization changes.
