# Smooth convergence of Gauduchon derivative forms does not control recovered metrics at the positive-cone boundary

Date: 2026-11-06. Finding **POME-GAUD-RECOVERY-SMOOTH-DERIVATIVE-BOUNDARY-001**. **Severity: low; status: verified conditional deduction.** The printed Proposition 12.5.1 is **correct**. This is a new explicit boundary-instability model for its inverse formula, **not** a counterexample to recovery within the strictly positive cone, not a proof repair, and not a whole-section certificate.

## Precise reading-edition provenance

Production **main b6933b772f41b45918f7e25ed1afbbb1fd892272**.

- Primary file: **docs/sections/a-gauduchon-variational-volume--recovering-a-positive-class-from-its-gauduchon-derivative/index.html**, blob **829d10abfa8f92c7c77fde66704adb6486ccdc93**. Proposition **12.5.1**, source **non-kahler-pluripotential-theory:765CFEAC**, permanent tag **4BBB232A044C**, statement at physical lines **22–27**, proof at **32–43**; normalized derivative form at lines **10–19**.
- Dependency on the variational quotient and minimizers: **docs/sections/a-gauduchon-variational-volume--the-quotient-and-the-smooth-equation/index.html**, blob **9ec67161d46b3ba20afa1b1c9a0c84f29322763e**. Definition **12.2.1**, lines **7–21**; Theorem **12.2.3**, source **non-kahler-pluripotential-theory:876DF057**, permanent **2DB664A6EFDF**, lines **49–79**.
- First variation: **docs/sections/a-gauduchon-variational-volume--the-equality-case-of-concavity-and-the-first-variation/index.html**, blob **d94e3fc055b0642a86495c27ad8f5af6f24f17d1**. Proposition **12.3.2**, source **non-kahler-pluripotential-theory:6D3F0AB8**, permanent **94AFD9E43DE0**, lines **34–58**.
- The chapter's standing requirement that the volume form be a **probability form** occurs in **docs/sections/a-gauduchon-variational-volume/index.html**, line **8**. We respect it below.

## New statement, with all quantifiers

For **every integer n >= 2**, there exist a fixed compact complex torus X of dimension n, a fixed smooth positive probability form mu, and smooth strictly positive background forms theta_t, 0 < t <= 1, with the following properties.

1. Their Gauduchon root volumes all equal **lambda_mu(theta_t)=1**.
2. Their full first-variation covectors are represented by smooth positive dd^c-closed (n-1,n-1) forms Xi_t, and **Xi_t converges in C^k for every integer k >= 0** to a smooth **semipositive but degenerate** form Xi_0.
3. Their unique normalized smooth Monge–Ampere solution forms Omega_t=theta_t satisfy **||Omega_t||_C0 ~ t^(-1/n)** (up to constants depending only on n). More precisely, their L^q norms relative to a fixed flat reference metric, for any real q > 0, obey
   - bounded and convergent for 0 < q < n/2;
   - q-th power comparable to log(1/t) for q = n/2;
   - q-th power comparable to t^(1/2-q/n) for q > n/2.
   In particular, for n=2 the positive solution currents have **unbounded total mass** as t tends to zero, while their derivative covectors converge smoothly.

Therefore the exact recovery formula of Proposition 12.5.1 is not uniformly continuous up to the boundary of positive derivative forms, **even on the unit-root-volume slice**. It makes no assertion about continuity **inside** a fixed uniformly elliptic subset of the positive cone: the limiting Xi_0 is outside that domain.

## Full construction and calculation

Let E = C/(Z+iZ), X=E^n, and z_j=x_j+i y_j. Define
\[
 \alpha_j=\frac{i}{2}\,dz_j\wedge d\bar z_j=dx_j\wedge dy_j,\qquad
 \omega_0=\sum_{j=1}^n\alpha_j,\qquad
 \mu=\alpha_1\wedge\cdots\wedge\alpha_n=\frac{\omega_0^n}{n!}.
\]
Each real coordinate has period one, so **int_X mu=1**. This normalization matters: replacing mu by omega_0^n would not be a probability form.

For 0 < t <= 1 put
\[
 h_t(x_1)=t+\sin^2(\pi x_1),\qquad
 \gamma_t=h_t\alpha_1+\alpha_2+\cdots+\alpha_n.
\]
This is a smooth Hermitian metric. Write alpha_{\widehat j} for the product of all alpha_k with k != j. Its (n-1)st power is
\[
 \gamma_t^{n-1}=(n-1)!\left(\alpha_{\widehat 1}
       +h_t\sum_{j=2}^n\alpha_{\widehat j}\right).                 \tag{1}
\]
The only variable coefficients depend on x_1. In the edition's convention
\(dd^c=(i/2\pi)\partial\bar\partial\), \(dd^c h_t\) is a scalar multiple of alpha_1. Every alpha_{\widehat j} with j >= 2 already contains alpha_1. Thus
\[
 dd^c(\gamma_t^{n-1})=0.                                           \tag{2}
\]
Consequently gamma_t is **Gauduchon**, verified directly rather than inferred from a general conformal theorem.

Its volume and the exact quotient denominator are
\[
 \gamma_t^n=n!h_t\mu,\qquad
 D_t:=D_\mu(\gamma_t)
  =(n!)^{(n-1)/n}\int_X h_t^{(n-1)/n}\,\mu.                       \tag{3}
\]
As t decreases to zero, D_t tends to the finite **strictly positive**
\[
 D_0=(n!)^{(n-1)/n}\int_0^1\sin^{2(n-1)/n}(\pi x)\,dx.
\]
Now define the background and candidate solution to be the same form:
\[
 \theta_t=\Omega_t=(n!h_t)^{-1/n}\gamma_t
  =(n!)^{-1/n}\left(h_t^{(n-1)/n}\alpha_1
                    +h_t^{-1/n}\sum_{j=2}^n\alpha_j\right).       \tag{4}
\]
They are smooth and strictly positive for t>0, and
\[
 \Omega_t^n=(n!h_t)^{-1}\gamma_t^n=\mu.                            \tag{5}
\]

There is also a **direct quotient proof**, without assuming the full general PDE existence theory, that their root volume is exactly one. For every Gauduchon metric delta the pointwise arithmetic–geometric mean inequality gives
\[
 \Omega_t\wedge\delta^{n-1}
       \geq\left(\frac{\Omega_t^n}{\delta^n}\right)^{1/n}\delta^n
       =\left(\frac{\mu}{\delta^n}\right)^{1/n}\delta^n.
\]
Integrating proves Q_mu(theta_t,delta)>=1. For delta=gamma_t, equality holds **pointwise**, because Omega_t is conformal to gamma_t. Hence lambda_mu(theta_t)=1 and gamma_t is a minimizing Gauduchon metric.

Proposition **12.3.2** now identifies the full derivative (the only substantial pre-existing analytic input needed for the *derivative* identification):
\[
 (d\lambda_\mu)_{\theta_t}(\chi)=\int_X\chi\wedge\Xi_t,\qquad
 \Xi_t=\frac{\gamma_t^{n-1}}{D_t}
      =\frac{(n-1)!}{D_t}\left(\alpha_{\widehat1}
                     +h_t\sum_{j=2}^n\alpha_{\widehat j}\right).   \tag{6}
\]
Both numerator coefficients and all their spatial derivatives converge smoothly as t -> 0, while D_t -> D_0 > 0. Therefore **Xi_t -> Xi_0 in C^infinity**; the limit is smooth, semipositive and dd^c-closed by (2). At any point with x_1=0 it is a multiple of alpha_2 wedge ... wedge alpha_n, and is not a strictly positive (n-1,n-1) form. This is precisely where the positive-root inverse in Proposition 12.5.1 approaches its boundary.

At x_1=0, the eigenvalues of Omega_t relative to omega_0 are
\[
 (n!)^{-1/n}t^{(n-1)/n}\quad\text{in the first direction},
 \qquad (n!)^{-1/n}t^{-1/n}\quad\text{in each other direction}.    \tag{7}
\]
This gives the stated exact **t^(-1/n)** C^0 blow-up.

For the finer L^q statement, equation (4) and 0<h_t<=2 give, with constants depending on n and q but not t,
\[
 \|\Omega_t\|_{L^q(\mu;\omega_0)}^q
       \asymp \int_0^1\big(t+\sin^2(\pi x)\big)^{-q/n}\,dx.        \tag{8}
\]
Near each zero of sin(pi x), periodicity and the Taylor expansion give
\(c\,d(x,\mathbb Z)^2\leq\sin^2(\pi x)\leq C\,d(x,\mathbb Z)^2\).
The local integral is therefore comparable to
\(\int_0^{1/4}(t+s^2)^{-q/n}ds\). Split it at s=sqrt(t):
the portion 0<=s<=sqrt(t) has size comparable to t^(1/2-q/n);
the remainder has size comparable to the integral of s^(-2q/n).
This gives exactly the three regimes in the statement. For n=2 and q=1, (8) grows logarithmically. Because Omega_t is positive and omega_0 is fixed, this is also growth of its total trace mass, up to a fixed factor.

## Interpretation, dependencies, and possible editorial note

**Mathematical verdict:** no printed assertion in Proposition 12.5.1 is false; the proposition assumes a **strictly positive derivative form associated with a point in the positive cone**. This example lies in that domain for every t>0 and merely approaches a degenerate boundary point. It shows why a proposed global stability theorem based solely on C^infinity convergence of derivative representatives and normalization lambda=1 would be false. A local stability result on uniformly elliptic sets remains compatible with the model.

An optional explanatory sentence after Proposition 12.5.1 could state: *Recovery from the derivative is an interior result; without a uniform lower bound on its positive (n-1,n-1) representative, even smooth convergence of the normalized derivative does not control the recovered solution forms.* No changes to printed text or permanent labels are made in this audit.

**Affected but unverified downstream areas:** the Hessian metric/completion discussion in §12.6 and compact Gauduchon duality/boundary discussions in §§12.7–12.11. These are **not** certified or contradicted here. No Demailly approximation, regularization, Bergman, weighted L^2, Ohsawa–Takegoshi, multiscale atlas or positivity-loss proof programme was examined.

**Coverage limit:** new exact flat-torus model plus the displayed quotient, derivative and inverse hypotheses of §12.5.1; selected §12.2.1/3 and §12.3.2 only as stated dependencies. No general PDE, global smooth-family theorem, full §12.5 certification, build, tests, CI or website publication is asserted.
