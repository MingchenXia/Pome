# Magnetic Landau levels: a sharp Riesz bound from midpoint convexity

**Audit date:** 2026-11-06. **Reviewed production main:** b6933b772f41b45918f7e25ed1afbbb1fd892272 (unchanged).
**Integrated reading-edition file:** docs/sections/magnetic-models-and-spectral-localization/index.html;
blob ee89de7d23cc96a8546c736ac7d068546b126f3a, physical lines **5–7, 31–54, 59–70, 76–79, 85–109**.

**Stable provenance (source: demailly-complex-geometry):**
Equation 2.24.4 source 4EE24E32, permanent tag 6919A4A3FD8F (lines 31–35);
Equation 2.24.5 source E2C26C03, permanent 72E6618A3A3C (lines 38–45);
Lemma 2.24.6 source 2FD17158, permanent 0F14CB3D46F3 (lines 49–70);
bound 2.24.7 source 3A39A2CF, permanent DD3B970F19C7 (lines 49–54).
Proposition 2.24.8, permanent C554004EA447, lines 76–109, was read only as a direct dependent: no certification of its full proof.

## Finding 1: sharp Riesz bound

**POME-MAGNETIC-MIDPOINT-RIESZ-CONVEX-ORDER-001** — **low / verified conditional deduction** from the printed explicitly normalized spectral measures.
The printed inequality (2.24.7) is **correct**; its Riesz-mean coefficient can be specified sharply, uniformly over all constant magnetic fields, without changing the theorem.

For a single magnetic pair, the integrated definitions are
\[
 \mu_b=\frac{b}{2\pi}\sum_{p\geq0}\delta_{(2p+1)b}\quad (b>0),
 \qquad \mu_0=\frac{dt}{4\pi}\quad\text{on }[0,\infty).
\]
For every nonnegative convex function $\varphi$ for which both integrals are
well-defined, Hermite–Hadamard midpoint convexity gives, on
$I_p=[2pb,2(p+1)b]$,
\[
 \frac{b}{2\pi}\varphi((2p+1)b)
 \leq \frac{1}{4\pi}\int_{I_p}\varphi(t)\,dt.
\]
Summing over $p$ proves
$\int\varphi\,d\mu_b\leq \int\varphi\,d\mu_0$.
For a field vector $\mathbf b=(b_1,\ldots,b_n)$ apply the inequality
one coordinate at a time to
$G_E(t_1,\ldots,t_n)=(E-t_1-\cdots-t_n)_+$.
The function is nonnegative and convex separately in each coordinate,
so successive Tonelli integration and replacement of any $\mu_{b_j}$
by $\mu_0$ preserve the inequality. All integrations are finite for
each fixed $E$ because the kernel vanishes whenever $\sum t_j\geq E$.
Thus
\[
 \begin{aligned}
 r_{\mathbf b}(E)
 &=\int G_E\,d\mu_{b_1}\cdots d\mu_{b_n}\\
 &\leq \int G_E\,d\mu_0^{\otimes n}
 =\boxed{\frac{(E_+)^{n+1}}{(4\pi)^n(n+1)!}}. \tag{A}
 \end{aligned}
\]
Indeed $\mu_0^{*n}(dt)=
t^{n-1}dt/((4\pi)^n(n-1)!)$ for $t\geq0$.
Equality holds at $\mathbf b=\mathbf0$, so the coefficient in (A)
is the **optimal all-field coefficient** in the Riesz-mean inequality.
This is stronger than the unspecified $C_n$ for $r_{\mathbf b}$
in equation 2.24.7; it does **not** assert a sharper counting bound.

In one magnetic pair, the zero-field discrepancy has a closed formula.
For $b>0$ and $E\geq0$, set
$x=E/(2b)$, $m=\lfloor x+\frac12\rfloor$.
The contributing positive terms have $p=0,\ldots,m-1$ (an endpoint
term may be zero), hence
\[
 r_b(E)=\frac{b}{2\pi}\sum_{p=0}^{m-1}(E-(2p+1)b)
 =\frac{b}{2\pi}(mE-bm^2)
 =\frac{E^2}{8\pi}-\frac{b^2}{2\pi}(x-m)^2.
\]
Since $m$ is a nearest nonnegative integer to $x\geq0$,
\[
 \boxed{0\leq r_0(E)-r_b(E)=
 \frac{b^2}{2\pi}
 \operatorname{dist}\left(\frac{E}{2b},\mathbb Z_{\geq0}\right)^2
 \leq\frac{b^2}{8\pi}}. \tag{B}
\]
For $E\leq0$ both means vanish. The constant in (B) is attained
at every odd Landau energy $E=(2k+1)b$; the $O(b^2)$ zero-field
Riesz convergence is **uniform for all $E\geq0$**. The exact
$\pi$-factors follow from the printed normalization and should
not be changed to a different convention.

## Finding 2: the counting analogue fails

**POME-MAGNETIC-COUNTING-FREE-BOUND-FAIL-001** — **low / verified conditional deduction**,
a counterexample only to an **unprinted proposed strengthening**, not
to a theorem or proof in Pome.

In one pair, let $E=(1+\epsilon)b$, $0<\epsilon<1$.
Only the first Landau level lies strictly below $E$, so
\[
 \nu_b(E)=\frac{b}{2\pi}
 >\frac{(1+\epsilon)b}{4\pi}
 =\nu_0(E).
\]
Therefore the coefficient from the zero-field counting function
cannot replace the unspecified constant in the $\nu_b$ part of
(2.24.7). The midpoint inequality applies to the **convex** first-Riesz
kernel $(E-t)_+$, but not to the discontinuous counting kernel
$\mathbf1_{[0,E)}(t)$.

The endpoint convention has a direct check:
\[
 r_b'(E^-)=\mu_b([0,E))=\nu_b(E),\qquad
 r_b'(E^+)=\mu_b([0,E]).
\]
The two derivatives differ precisely at a Landau atom, while the
Riesz mean itself stays continuous. This matches the strict
interval written in equation 2.24.5.

## Disposition, dependencies and coverage limits

**Correction direction:** optionally append the sharper coefficient
(A) as a remark to Lemma 2.24.6; retain the current counting estimate
and open-energy-interval convention. No production patch is included.
The direct dependent Proposition 2.24.8 uses both $r_{\mathbf b}$
and $\nu_{\mathbf b}$ in its boundary-layer error (lines 89–109).
Bound (A) can improve only its Riesz term, not the counting term.
Other downstream citations have **not** been exhaustively traced.

The integrated oscillator completeness and per-volume spectral
identification (Lemma 2.24.6, lines 59–68) were examined to
check assumptions and normalization, but are **not independently
certified** in this increment. The deductions (A) and (B) are
complete **conditional on the printed spectral measures** (2.24.4–5).
The general compact-form lemma, Dirichlet trace localization,
its uniformity in $b$, other sections and transitive dependencies
remain open. No printed false theorem, proof gap, general
formal-verification claim or whole-section certificate is inferred.

**Reproducible limited check actually performed:** 18 rational
pairs $(b,E)$ (after multiplying the Riesz formulas by $\pi$)
satisfy the finite Landau sum identity (B) exactly, without floating
point arithmetic. This finite check supports normalization only;
it is not a test or verification of the general theorem or Pome build.

**Owner's scope:** all Demailly approximation/regularization,
dedicated Bergman, weighted $L^2$, Ohsawa–Takegoshi,
multiscale-atlas and positivity-loss proof-completion work stays
**deferred-by-user**, neither revisited nor certified. No source,
main, registry, permanent-tag, CI or website changes.
