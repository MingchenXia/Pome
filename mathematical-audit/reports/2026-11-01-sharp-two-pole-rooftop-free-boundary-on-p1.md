# Exact symmetric two-pole rooftop and free boundary on the projective line

**Date:** 2026-11-01. **Reviewed production main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.

**Stable finding ID:** **POME-ROOF-P1-SYMMETRIC-FREEBOUNDARY-001**.
**Severity/status:** **low / verified conditional deduction**. This is an independent explicit sharpening of a correct example, **not** a false theorem, full general rooftop theorem, or production repair. It is **not** an application of the user-excluded Demailly regularization, Bergman, L2, Ohsawa–Takegoshi, atlas, or positivity-loss programmes.

## Exact production anchors and dependencies

The current integrated reading edition is `docs/sections/envelopes-and-model-potentials--obstacles-and-rooftops/index.html`, blob SHA `e9129aaaab9e9f172da9704bffe939839f8afeb6`, under section tag `FBD81D436A6A`. Its **Example 16.11.8**, original source label `foundations-of-pluripotential-theory:108F276E`, permanent tag `908479CB91B3`, is at **physical HTML lines 165–172** (potentials and normalization at 166–170; two-unit-atom contradiction at 171). The competitor definition is **Definition 16.11.3**, source `foundations-of-pluripotential-theory:7FB6072B`, permanent `A4F165851008`, lines **73–86**; the largest-competitor criterion is **Proposition 16.11.4**, source `:3796C01B`, permanent `641F3FEC623D`, lines **88–136**; rooftop convention **Definition 16.11.5**, source `:D99E4099`, permanent `F80B4C1B3032`, lines **138–144**; and **Proposition 16.11.7**, source `:4EFFB27F`, permanent `046401771DAB`, lines **147–163**. The separate SGPT rooftop formula is retained as distinct provenance, `sgpt:0337BA47`, permanent `6AE4825E4C6F`, physical lines **174–177**. Its comparison of hypotheses and conclusions supports coexistence, **not a genuine duplication finding**.

The two local analytic inputs are the normalized Poincare–Lelong identity \(\theta+dd^cu_0=[0]\), \(\theta+dd^cu_\infty=[\infty]\), already cited by Example 16.11.8 from Theorem 5.5.6 (permanent `8D4BA339507E`), and the elementary one-dimensional atom/total-mass principle cited there from Theorem 6.7.6 (permanent `BD2098F182CC`). The present proof below explicitly uses the logarithmic potential and the one-dimensional subharmonic maximum principle; it does not certify all general results invoked elsewhere in §16.11.

## Statement: sharp feasibility and exact free boundary

Work on \(X=\mathbf P^1\), with \(dd^c=\frac{i}{2\pi}\partial\bar\partial\), the Fubini–Study form \(\theta=\omega_{\mathrm{FS}}\) normalized by \(\int_X\theta=1\), and exactly the printed potentials
\[
u_0(z)=\log\frac{|z|^2}{1+|z|^2},\qquad
u_\infty(z)=-\log(1+|z|^2).
\]
For \(0<\tau\le1\), both \(\tau u_0,\tau u_\infty\) are \(\theta\)-psh. Their rooftop \(p_\tau=P_\theta(\tau u_0,\tau u_\infty)\) is **nontrivial if and only if \(\tau\le\frac12\)**. It is identically \(-\infty\) if \(\frac12<\tau\le1\). At the sharp critical value,
\[
p_{1/2}=\tfrac12(u_0+u_\infty).
\]

For \(0<\tau<\frac12\), write
\[
d=1-2\tau,\quad a=-\log d,\quad
t=\log|z|^2,\quad f(t)=\log(1+e^t),
\]
\[
c_\tau=(1-\tau)\log(2(1-\tau))
                  -(\tfrac12-\tau)\log(1-2\tau).
\]
Then the **exact global rooftop** is
\[
p_\tau(z)=
\begin{cases}
\tau u_0(z),&
 |z|\le\sqrt{d},\\[2mm]
\frac12\log|z|^2+c_\tau-\log(1+|z|^2),&
 \sqrt d\le|z|\le1/\sqrt d,\\[2mm]
\tau u_\infty(z),&
 |z|\ge1/\sqrt d .
\end{cases}
\]
The pole values at \(0,\infty\) are interpreted by upper semicontinuity. Thus the annulus
\(\sqrt{1-2\tau}<|z|<(1-2\tau)^{-1/2}\) is **exactly the open noncontact region**; the two closed complementary caps are the corresponding contact regions. The pieces agree to first derivative at both circles, and there is **no singular circle measure** at the free boundary.

In dimension one the envelope curvature measure is explicitly
\[
\boxed{\quad
\theta+dd^cp_\tau
 =\tau[0]+\tau[\infty]
 +(1-\tau)\,\mathbf1_{\{|z|\le\sqrt d\}\cup
             \{|z|\ge d^{-1/2}\}}\,\theta .
\quad}
\]
Its smooth part has total mass \(1-2\tau\), and each atomic mass is \(\tau\). At \(\tau=1/2\) only the two atoms remain, with no positive smooth part. At the harmless limit \(\tau=0\), the rooftop is \(p_0=0\).

## Complete proof

**1. Sharp feasibility.** As in the printed example, \(dd^cu_0=[0]-\theta\) and \(dd^cu_\infty=[\infty]-\theta\). Since \(0<\tau\le1\), each scaled potential is \(\theta\)-psh:
\(\theta+dd^c(\tau u_0)=(1-\tau)\theta+\tau[0]\), and analogously at infinity. If \(v\) is a common \(\theta\)-psh minorant, the curvature \(\mu_v=\theta+dd^cv\) has masses \(\mu_v(\{0\})\ge\tau\), \(\mu_v(\{\infty\})\ge\tau\) by the logarithmic growth inequality, while \(\mu_v(X)=1\). Thus \(2\tau\le1\). Conversely, for \(2\tau\le1\),
\(w_\tau=\tau(u_0+u_\infty)\) satisfies
\[
\theta+dd^c w_\tau=(1-2\tau)\theta+
\tau[0]+\tau[\infty]\ge0.
\]
Because \(u_0,u_\infty\le0\), \(w_\tau\le\tau u_0,\tau u_\infty\). It is a common minorant, proving sufficiency. For \(\tau=1/2\), any minorant must have \(\mu_v=\frac12[0]+\frac12[\infty]=\mu_{w_{1/2}}\), hence \(v-w_{1/2}\) is harmonic on \(\mathbf P^1\), so is a constant. The constraint \(v\le\frac12u_0\), evaluated in the limit \(z\to0\) and using \(u_\infty(0)=0\), forces that constant to be at most zero. Therefore \(p_{1/2}=w_{1/2}\).

**2. Convex radial obstacle.** For \(0<\tau<1/2\), set \(F=f+p_\tau\) on the punctured affine chart. The two obstacles become
\[
A(t)=f+\tau u_0=\tau t+(1-\tau)f(t),
\qquad
B(t)=f+\tau u_\infty=(1-\tau)f(t).
\]
They are convex and \(A(t)-B(t)=\tau t\); their minimum is \(A\) for \(t\le0\) and \(B\) for \(t\ge0\). Put \(s(t)=f'(t)=e^t/(1+e^t)\). With \(a=-\log d\),
\[
s(-a)=\frac d{1+d}=\frac{1-2\tau}{2(1-\tau)},
\qquad
s(a)=\frac1{1+d}=\frac1{2(1-\tau)}.
\]
Therefore
\[
A'(-a)=\tau+(1-\tau)s(-a)=\frac12,\quad
B'(a)=(1-\tau)s(a)=\frac12.
\]
A direct substitution gives
\(A(-a)+a/2=B(a)-a/2=c_\tau\).
Consequently the common tangent \(\ell(t)=t/2+c_\tau\) lies below **both** convex functions \(A,B\) for every \(t\). The piecewise function
\[
F_\tau(t)=
\begin{cases}
A(t),& t\le-a,\\
\ell(t),& -a\le t\le a,\\
B(t),&t\ge a
\end{cases}
\]
is convex, \(C^1\), and satisfies \(F_\tau\le\min(A,B)\). The function \(F_\tau-f\) extends over \(0,\infty\) as a \(\theta\)-psh potential because it equals \(\tau u_0\) near \(0\) and \(\tau u_\infty\) near \(\infty\). Hence it is a competitor.

**3. Global maximality without assuming the competitor is radial.** Let \(v\) be *any* \(\theta\)-psh common minorant. On the outer caps \(v\le\tau u_0\) and \(v\le\tau u_\infty\), which are the candidate there. On the annulus \(e^{-a/2}<|z|<e^{a/2}\), the function \(v(z)+f(\log|z|^2)\) is subharmonic and on the two boundary circles is bounded above respectively by \(A(-a)=\ell(-a)\) and \(B(a)=\ell(a)\). The function \(\ell(\log|z|^2)=\frac12\log|z|^2+c_\tau\) is harmonic on this annulus. The subharmonic maximum principle yields
\(v+f\le\ell\) everywhere inside. Hence \(v\le F_\tau-f\) globally. Because the candidate itself is admissible, it is **exactly** the rooftop, without a rotational averaging or symmetry assumption.

**4. Curvature and contact.** Away from \(0,\infty\), \(\theta+dd^c(F_\tau-f)=dd^cF_\tau\). On the middle annulus \(F_\tau=\ell\) is harmonic, so this curvature vanishes. In each outer cap, \(F_\tau=A\) or \(B\) and \(dd^cF_\tau=(1-\tau)\theta\). At \(0,\infty\), the log singularities contribute atoms of masses \(\tau,\tau\). Since \(F_\tau\) is \(C^1\) at \(t=\pm a\), it has no distributional first-derivative jumps, hence no boundary circle atoms. Finally, with \(s=f'\) and \(\int_{\{t_1<t<t_2\}}\theta=s(t_2)-s(t_1)\), the smooth cap mass equals
\[
(1-\tau)\bigl(s(-a)+1-s(a)\bigr)
=(1-\tau)\frac{2d}{1+d}=1-2\tau.
\]
The displayed formula has total mass \(1\), as required. Strict inequality against both obstacles holds on the open annulus: \(\ell(t)<A(t)\) except at \(-a\), and \(\ell(t)<B(t)\) except at \(a\), by strict convexity of \(A,B\).

## Reproducible small exact checks and proposed correction

As an independent *small coefficient check*, take \(\tau=1/4\): then \(d=1/2\), \(a=\log2\), \(s(-a)=1/3\), \(s(a)=2/3\), so \(A'(-a)=B'(a)=1/2\), and the smooth cap mass is \(1-2\tau=1/2\). A separate exact SymPy substitution was executed for \(\tau=1/10,1/4,2/5\): at each value both tangency differences simplified to zero and both slopes to \(1/2\). These **three local symbolic substitutions**, not project tests, only cross-check the already proved algebra.

**Proposed isolated reading addition:** place an optional quantitative sub-example or corollary immediately after Example 16.11.8, identifying the feasibility threshold, explicit free boundary and curvature measure, while preserving the example's source attribution, permanent tag, and the separate SGPT formula. No alteration of the printed result is mathematically required.

**Affected dependents:** concrete obstacle-envelope feasibility and singularity type calculations, contact-set concentration in §§16.12–16.14, and rooftop examples in §§16.22–16.27; these *general* theorems were not re-proved. This calculation does not infer a general global rooftop existence theorem from a projective-line model.

**Actual review coverage:** proof-level selected scrutiny of Definition 16.11.3, Proposition 16.11.4(1)/(2)/(5), Definition 16.11.5, Proposition 16.11.7 and **new sharp analysis of Example 16.11.8** in §16.11. The section was already selected-reviewed on 2026-10-23; **not a first-visited or wholly certified section**. No other current section was newly certified. Project inventory remains **25 current chapters / 747 numbered ToC sections / 0 fully mathematically certified sections**.

**Scope and repository impact:** all older findings retain their recorded statuses, especially deferred-by-user Demailly approximation/regularization and dedicated Bergman/L2/OT/multiscale/positivity-loss work. No source/body/registry/permanent-tag/main change, build, CI, formalization or website publication; only audit Markdown is proposed for `review/mathematical-audit`.
