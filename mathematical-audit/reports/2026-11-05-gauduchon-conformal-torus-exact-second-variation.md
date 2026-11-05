# Exact Gauduchon root-volume variation on conformal backgrounds of a flat complex torus

Date: 2026-11-05. Finding **POME-GAUD-CONFORMAL-TORUS-EXACT-VARIATION-001**. **Low; verified conditional deduction.** The printed mathematical statements are correct. This is an independently constructed nonclosed-background solution family and an exact check of *both* second-variation identities and their equality cases, not a proof of all upstream Hermitian Monge–Ampère theory.

## Reviewed reading edition and immutable locators

Production main: **b6933b772f41b45918f7e25ed1afbbb1fd892272**.

- Main file **docs/sections/a-gauduchon-variational-volume--second-variation-on-background-classes/index.html**, blob **4992f82c6e84918ead47a972eab7e3238a147655**. Proposition **12.4.1** (source **non-kahler-pluripotential-theory:C55D0CC4**, permanent **67FDDBC10DBD**) at physical lines **22–28**; its twice-differentiated determinant proof at **33–64**. The paired displayed identities (12.4.2)–(12.4.3) carry source **non-kahler-pluripotential-theory:86F8F24F** and permanent **E544AEC2FDDB**, lines **24–27**. The bilinear background-class form (12.4.4), source **non-kahler-pluripotential-theory:B96CF85C**, tag **6BCEC0329DE5**, is at **69–75**.
- Supporting **docs/sections/a-gauduchon-variational-volume--the-quotient-and-the-smooth-equation/index.html**, blob **9ec67161d46b3ba20afa1b1c9a0c84f29322763e**: Definition **12.2.1** (line **17–21**), and Theorem **12.2.3** (source **non-kahler-pluripotential-theory:876DF057**, permanent **2DB664A6EFDF**) at **49–80**. The latter identifies the smooth Monge–Ampère constant with the root volume.
- Supporting **docs/sections/a-gauduchon-variational-volume--the-equality-case-of-concavity-and-the-first-variation/index.html**, blob **d94e3fc055b0642a86495c27ad8f5af6f24f17d1**: Proposition **12.3.2** (source **non-kahler-pluripotential-theory:6D3F0AB8**, permanent **94AFD9E43DE0**) lines **34–58**, consulted for differentiability only.

The separate duplicate nested-align equation alias at §12.4, physical line 79, is an **already recorded integration error** (POME-GAUD-SECONDVAR-EQ-ALIAS-NESTED-001); the present finding does not reclassify it as new work or propose changing tags.

## Exact model and construction

Let \(n\geq1\), \(E=\mathbb C/(\mathbb Z+i\mathbb Z)\), \(X=E^n\), with \(z_j=x_j+iy_j\). Put
\[
 \alpha_j=\frac i2 dz_j\wedge d\bar z_j=dx_j\wedge dy_j,\qquad
 \omega=\sum_{j=1}^n\alpha_j,\qquad V=\int_X\omega^n=n!,
 \quad \mu=\omega^n/V.
\]
Thus \(\mu\) is the *probability volume* in the definition of the Gauduchon quotient. Use the edition's convention \(dd^c=\frac{i}{2\pi}\partial\bar\partial\). Choose an arbitrary smooth real one-periodic \(f=f(x_1)\) and let \(\theta_t=(1+t f)\omega\) for real \(|t|\) small enough that \(a_t(x)=1+t f(x)>0\). Write normalized circle means as \(\langle h\rangle=\int_0^1 h(x)\,dx\), and set
\[
 M_t=\langle a_t\rangle=1+t m,\quad m=\langle f\rangle,\qquad
 H_t=\langle a_t^{-(n-1)}\rangle,\qquad
 \Lambda_t=\left(\frac{M_t}{H_t}\right)^{1/n}.
\]
Define
\[
 q_t(x)=\Lambda_t^n a_t(x)^{-(n-1)}-a_t(x).
\]
Its mean is **exactly zero**, \(\langle q_t\rangle=\Lambda_t^nH_t-M_t=0\). Hence the periodic ODE
\[
 u_t''(x_1)=4\pi q_t(x_1)
\]
has a smooth one-periodic solution, unique after requiring its circle mean zero. The factor \(4\pi\) is essential for the fixed \(dd^c\) convention: \(dd^c u_t=u_t''\alpha_1/(4\pi)=q_t\alpha_1\).

Therefore
\[
 \Omega_t:=\theta_t+dd^cu_t
 =\frac{\Lambda_t^n}{a_t^{n-1}}\alpha_1
   +a_t\sum_{j=2}^n\alpha_j>0,
 \qquad
 \Omega_t^n=\Lambda_t^n\omega^n=V\Lambda_t^n\mu.
\]
The construction works **for every such \(t\)**, not merely to second order. By the printed smooth-equation/quotient identification in Theorem 12.2.3, the exact root-volume value is
\[
 \boxed{\lambda_\mu(\theta_t)
 =V^{1/n}\left(\frac{1+t\langle f\rangle}
 {\langle(1+t f)^{-(n-1)}\rangle}\right)^{1/n}.}
\]
The expression also follows for \(n=1\) (where \(H_t=1\)). This identification uses the named theorem as an **upstream conditional input**, although the displayed smooth solution and its determinant are verified without it.

## Exact second derivatives and endomorphism check

Let \(v=\langle(f-m)^2\rangle\). Differentiation under the integral is valid locally in \(t\), since \(a_t\) stays uniformly positive. At \(t=0\),
\[
 H_0=1,\quad H_0'=-(n-1)m,\quad
 H_0''=n(n-1)\langle f^2\rangle,\quad M_0=1,\quad M_0'=m.
\]
From \(\log\Lambda_t=(\log M_t-\log H_t)/n\), direct differentiation gives
\[
 \frac{\dot\lambda}{\lambda}=m,\qquad
 -\left.(\log\lambda_\mu(\theta_t))''\right|_{t=0}
 =m^2+(n-1)v,\qquad
 \frac{\ddot\lambda}{\lambda}=-(n-1)v.
\]
For an independent check of the *integrands*, differentiate \(q_t\) at zero:
\[
 \dot q_0=nm-nf,\qquad
 A_\chi=\omega^{-1}\bigl(f\omega+dd^c\dot u\bigr)
 =\operatorname{diag}\bigl(nm-(n-1)f,\ f,\ldots,f\bigr),
\]
where \(\chi=f\omega\). Its trace is the constant \(nm\). Since \(\omega\) is Kähler, the adjoint probability \(\nu_\omega\) equals \(\mu\), by Stokes' theorem and the defining adjoint identity. Thus
\[
 \frac1n\int_X\operatorname{tr}(A_\chi^2)d\nu_\omega
   =m^2+(n-1)v,\qquad
 \frac1n\int_X\|A_\chi-mI\|_\omega^2d\nu_\omega
   =(n-1)v.
\]
These are **exactly** the right sides of both printed equations (12.4.3) and (12.4.2), with the correct \(1/n\) factor, the *negative* sign in \(\lambda''/\lambda\), and the normalized adjoint probability. A symbolic polynomial reduction of the two trace identities was also performed independently, yielding zero differences.

For \(n\geq2\), the radial equality \(\lambda''=0\) in this family holds precisely when \(f\) is constant, and the \(-\log\lambda\) Hessian vanishes precisely for \(f=0\). For a nonconstant \(f\), the direction \(\chi=f\omega\) is generally nonclosed (\(d\chi=df\wedge\omega\ne0\)), so this is a genuinely **non-Kähler background-class variation**, rather than merely a Kähler intersection-number calculation. For \(n=1\), the formula gives \(\lambda_\mu(\theta_t)=1+tm\); every mean-zero \(f\omega\) is a \(dd^c\)-direction, which agrees with the equality clauses in dimension one.

As a fully explicit two-dimensional check, let \(n=2\), \(f(x)=\cos(2\pi x)\), so \(m=0\), \(v=1/2\). The standard circle integral yields \(H_t=(1-t^2)^{-1/2}\) for \(|t|<1\), hence
\[
 \lambda_\mu(\theta_t)=\sqrt 2\,(1-t^2)^{1/4},
 \quad \left.\frac{\lambda''}{\lambda}\right|_0=-\frac12,
 \quad -\left.(\log\lambda)''\right|_0=\frac12.
\]
Both are exactly reproduced by the diagonal matrix \(A_\chi=\operatorname{diag}(-f,f)\).

## Classification, dependents and limits

**Status:** verified conditional deduction; **severity:** low (new exact nonclosed test family, *not* an error or a repair). No counterexample to Proposition 12.4.1 or its equality cases was found. The proposed change, if desired, is only to add this explicit family as an example *after* the second-variation proposition, preserving canonical statement, tags, and historical attribution. Dependent interpretations: the intrinsic Hessian metric (12.4.4), the §12.6 completion programme, the smooth quotient relation §12.2.3 and the adjoint probability §11.23.2. We have **not** certified the general smooth Hermitian Monge–Ampère existence, Gauduchon conformal factor, adjoint regularity, global positive-definite metric or §12.6 completion. The earlier §12.4 duplicated-equation alias has its **own** open finding and is not repaired here.

New mathematical coverage: selected §12.4.1 smooth twice-differentiated determinant and equality statements, §12.4.4 as interpretive context. §12.2.1/.3 and §12.3.2 were checked only for exact hypotheses and dependence. This is **not** certification of §12.4 or any full numbered section. Actual current ToC remains **25 chapters / 747 numbered sections / zero entire sections mathematically certified**. All earlier statuses remain; the Demailly regularization/approximation and dedicated Bergman, weighted-\(L^2\), Ohsawa–Takegoshi, multiscale atlas and positivity-loss programmes remain **deferred-by-user** and are entirely outside this work. No production source, canonicalization, registry, tags, CI, tests, build or publication are changed.
