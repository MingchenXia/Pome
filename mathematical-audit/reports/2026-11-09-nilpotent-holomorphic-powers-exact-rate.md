# Exact power rates on nilpotent thickenings: the strict spectral-radius gap

**Finding:** POME-STEIN-NILPOTENT-POWER-RATE-001  
**Date:** 2026-11-09  
**Severity / classification:** low / verified conditional deduction (sharpness of the printed estimate, *not* a false theorem and *not* a proof repair).  
**Production main:** b6933b772f41b45918f7e25ed1afbbb1fd892272.  
**Integrated target:** docs/sections/separation-strict-exhaustions-and-coverings--convexity-and-stein-spaces/index.html, blob 169e9d3bc872e9fd89d5135e69204e33fccd3783.  
**Stable source label / permanent tag:** demailly-complex-geometry:BA15E5E8 / FE34E9B148D1, Lemma 9.32.6, physical lines 83–106 (hypotheses and inequality 95–99; proof 104–106).  
**Downstream context:** the finite-block lift criterion (9.32.7), physical lines 109–124, and Proposition 9.32.8 (tag A13AE3DAF423), beginning at physical line 127. These are dependency orientation only, not certified here.

## Question checked

The printed Lemma 9.32.6 says that if a global holomorphic section on a possibly **nonreduced** complex space satisfies the scalar-value bound \(|f|\leq\theta<1\) on the closure of an embedded relatively compact patch \(U\), then for every continuous seminorm \(p\) on the **full intrinsic** Fréchet space \(\mathcal O_X(U)\) and every \(r\in(\theta,1)\), there is a constant \(C_{p,r}\) for which
\[
             p(f^m|_U)\leq C_{p,r}r^m,\qquad m\geq0.
\]
The distinction between scalar point values and nilpotent section coefficients makes the strict inequality \(r>\theta\) essential.

## A family with arbitrary polynomial loss at the critical rate

Fix an integer \(k\geq2\) and \(0<a<1\). Let the nonreduced analytic space
\[
 X_k=\{(z,w)\in\mathbb C^2:w^k=0\}
\]
carry its full quotient structure sheaf. Its underlying topological space is the \(z\)-line. Let \(D=\{|z|<1,\ |w|<1\}\) and take the embedded patch \(U=X_k\cap D\Subset X_k\). Its global sections are explicitly
\[
 \mathcal O_{X_k}(U)\cong\mathcal O(\Delta_z)[w]/(w^k).
\]
Take the globally holomorphic section \(f=a+w\). At every scalar point of \(X_k\), including on \(\overline U\), the nilpotent coordinate evaluates to zero. Consequently \(|f|=a\), so the printed hypothesis holds with the **optimal** scalar bound \(\theta=a\).

For \(0\leq j\leq k-1\), define the coefficient functional
\[
 L_j(h)=[w^j]\,h(0,w),\qquad p_j(h)=|L_j(h)|.
\]
These are continuous seminorms for the intrinsic Fréchet topology. Indeed \(L_j\) is the \(j\)-th Taylor-coefficient functional of any ambient holomorphic lift \(H(z,w)\), evaluated at \((0,0)\). It vanishes on \((w^k)\), is independent of the lift, and is continuous on ambient holomorphic functions by Cauchy estimates. It therefore descends continuously through the quotient topology, which is the intrinsic topology used immediately before Lemma 9.32.6.

By the finite binomial theorem *inside the nonreduced structure sheaf*,
\[
 f^m=\sum_{j=0}^{k-1}\binom mj a^{m-j}w^j,\qquad
 p_j(f^m)=
 \begin{cases}
   \binom mj a^{m-j},&m\geq j,\\
   0,&m<j.
 \end{cases}
\]
For the highest nonzero nilpotent coefficient \(j=k-1\),
\[
 \frac{p_{k-1}(f^m)}{a^m}
 =a^{-(k-1)}\binom m{k-1}
 \sim \frac{m^{k-1}}{(k-1)!\,a^{k-1}}\longrightarrow+\infty.
\]
Hence **there is no constant \(C\) such that \(p_{k-1}(f^m)\leq Ca^m\) for all \(m\)**. The estimate fails at the omitted endpoint \(r=\theta\), despite the scalar value of \(f\) being identically \(a\). Since \(k\) can be arbitrarily large, the critical-rate polynomial loss can have **any positive integer degree**.

Conversely the printed estimate holds for this whole family, for **every** continuous seminorm \(p\), not only the \(p_j\). The triangle inequality gives
\[
 p(f^m)\leq
   \sum_{j=0}^{k-1}\binom mj a^{m-j}p(w^j).
\]
For every \(r>a\), every scalar sequence
\[
 r^{-m}\binom mj a^{m-j}
 =a^{-j}\binom mj(a/r)^m
\]
is bounded in \(m\). There are only finitely many \(j\), so the right-hand side is at most \(C_{p,r}r^m\). In particular \(f^m\to0\) in the full intrinsic Fréchet topology. For each \(j\), the \(m\)-th root of the nonzero coefficient seminorm tends to \(a\), showing that the **exponential spectral radius is still exactly the scalar value \(a\)**; the endpoint obstruction is a polynomial factor, not a larger exponential rate.

For \(k=1\), the structure sheaf is reduced and \(f=a\) has exactly \(p(f^m)=a^mp(1)\). The critical-rate failure begins with genuine nilpotent directions (\(k\geq2\)), and is therefore invisible to an argument looking only at scalar point values.

## Judgment, dependency and proposed correction

**The printed Lemma 9.32.6 is correct as stated.** Its strict range \(r\in(\theta,1)\) cannot in general be replaced by the endpoint \(r=\theta\) for the full intrinsic section topology on nonreduced spaces. The exact finite-binomial computation above is self-contained; it invokes no regularization, Bergman estimates, \(L^2\) extension, Ohsawa–Takegoshi input, compactness of varying measures or unreviewed theorem. The general lemma's proof still cites the intrinsic-topology theorem 9.51.5, whose whole proof chain is **not certified by this example**.

A future, separately reviewable reading-edition patch could add the example immediately after Lemma 9.32.6, explicitly retaining the strict \(r>\theta\) hypothesis and the distinction between nilpotent coefficients and reduced scalar values. The proof of Proposition 9.32.8 uses the strict gap to control high holomorphic powers in all intrinsic seminorms; the example clarifies why discarding that gap would be unjustified. This is **not** a detected error in Proposition 9.32.8 or a claim that the whole §9.32 has been checked.

**Scope:** newly checked the printed Lemma 9.32.6 hypothesis, exact inequality and local quotient-topology mechanism; inspected the first uses at (9.32.7) and Proposition 9.32.8 only as dependents. No claim to have audited §9.32.2–4, Proposition 9.32.8's entire proof, the coherent-analytic dependencies, or a full section. Previous §9.32 selected/dependency-only coverage remains intact. Demailly approximation/regularization and its dedicated Bergman, \(L^2\), Ohsawa–Takegoshi, multiscale and positivity-loss programme remain **deferred-by-user**, neither resolved nor reopened.
