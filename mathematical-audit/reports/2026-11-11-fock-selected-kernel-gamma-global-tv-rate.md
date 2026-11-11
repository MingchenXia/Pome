# 2026-11-11 — exact global total-variation error for a selected Fock kernel

**Stable finding:** POME-PARTIAL-Fock-GAMMA-GLOBAL-TV-SHARP-001  
**Severity/status:** low / **verified conditional deduction** (elementary new consequence, not a refutation or a repair of a false statement).  
**Production main reviewed:** b6933b772f41b45918f7e25ed1afbbb1fd892272.  
**First mathematical visit:** §18.41 (one newly visited numbered section; no whole-section certification).

## Exact integrated source and boundary of the audit

The audited reading-edition file is **docs/sections/partial-kernels-and-quotient-equilibrium--degenerate-curvature-and-growing-vanishing-orders/index.html**, Git blob **dae61db0ce6641977b7cc33469d95e9c820a7bff**, in production main b6933b772f41b45918f7e25ed1afbbb1fd892272. Its current section is **18.41 Degenerate curvature and growing vanishing orders**, permanent section tag **99460DD0DBB7** (title at physical HTML line 5). The mathematical inputs examined directly are:

- **Proposition 18.41.1**, source label **non-kahler-pluripotential-theory:0D642FCA**, permanent tag **85EDCA2D872C**, physical lines **26–50**. Equation (18.41.2), source label **non-kahler-pluripotential-theory:CEEB555A**, permanent tag **33E9A1B502F8**, at line **28**, gives the exact orthogonal-monomial reproducing kernel; the norm/Parseval justification is at lines **43–50**.
- **Proposition 18.41.6**, source **non-kahler-pluripotential-theory:28DA5323**, permanent **79BA8CB51C0E**, lines **112–129**, and equation (18.41.7), source **non-kahler-pluripotential-theory:9F81B3A7**, permanent **69B0FF116418**, line **114**. Its Poisson representation motivates the exact specialized identity; the proof below does not need its asymptotic error bound.
- **Theorem 18.41.9**, source **non-kahler-pluripotential-theory:4EBD44F4**, permanent **313505FAE88E**, lines **145–216**. Its local-total-variation claim is equation (18.41.10), source **non-kahler-pluripotential-theory:9BF776B4**, permanent **F26D2556A21E**, line **151**. The present result supplies a strictly stronger *global integrable difference and sharp rate* in the independent Gaussian case r=1; it does not claim the printed theorem already gives this rate.

This is the **independent explicit entire-function model** from §18.41, *not* an attempt to continue Demailly approximation/regularization or its dedicated Bergman, weighted L², Ohsawa–Takegoshi, multiscale or positivity-loss proof-completion programme. No regularization proof or L² extension is invoked here.

## Exact theorem, including infinite-mass caveat

Fix r=1 in the printed Hilbert space of entire functions with weight exp(-m|z|²) and Euclidean area dA, where m>0. Let q≥1 be an integer. Write

\[
 B_{m,1}^{(q)}(z)=\frac{m}{\pi}e^{-m|z|^2}
 \sum_{k=q}^{\infty}\frac{(m|z|^2)^k}{k!},\qquad
 \mu_{m,q}:=\frac1m B_{m,1}^{(q)}\,dA.
\]

For any real a≥0 set
\[
 \nu_{m,a}:=\frac1\pi\mathbf1_{\{m|z|^2>a\}}\,dA.
\]
Both measures have **infinite** total mass, but their **signed difference is a finite signed measure** and its total-variation norm (without the optional factor 1/2 used for probability distances) satisfies the exact formula
\[
 \boxed{\ \|\mu_{m,q}-\nu_{m,a}\|_{\rm TV}
     =\frac1m\,\mathbb E|Y_q-a|,\quad
     Y_q\sim\operatorname{Gamma}(q,1).\ } \tag{A}
\]
Its signed total mass is exactly
\[
 \boxed{\ \int_{\mathbb C}(\mu_{m,q}-\nu_{m,a})
     =\frac{a-q}{m}.\ } \tag{B}
\]
For the *matching threshold* a=q, the absolute error is explicitly
\[
 \boxed{\ \|\mu_{m,q}-\nu_{m,q}\|_{\rm TV}
     =\frac{2q^{q}e^{-q}}{m\,\Gamma(q)}
     =\frac{2q^q e^{-q}}{m(q-1)!}.\ } \tag{C}
\]
In particular, for every fixed λ>0 and q_m=floor(mλ), at all sufficiently large m (when q_m≥1), the fixed-circle target of (18.41.10) is ν_λ=π^{-1}1_{|z|>sqrt(λ)}dA=ν_{m,mλ}, and
\[
 \boxed{\ \sqrt m\,\|\mu_{m,q_m}-\nu_\lambda\|_{\rm TV}
 \longrightarrow\sqrt{\frac{2\lambda}{\pi}}.\ } \tag{D}
\]
The exact signed defect in this fixed-circle comparison equals λ-q_m/m∈[0,1/m), whereas its absolute discrepancy is asymptotically of order m^{-1/2}. Thus no universal o(m^{-1/2}) total-variation rate can hold for this fixed selected Gaussian model, even though the signed mass error is O(m^{-1}).

## Proof (direct, not dependent on the general partial-kernel machinery)

**1. Identify the gamma distribution without a limiting argument.** For r=1, Proposition 18.41.1 follows directly by polar integration:
\[
 \|z^k\|_{m,1}^{2}=\pi k!\,m^{-k-1}.
\]
Parseval on circles and Tonelli show that normalized monomials of degree k≥q form an orthonormal basis of the selected Hilbert space, giving the displayed formula for B. With t=m|z|², put
\[
 F_q(t):=e^{-t}\sum_{k=q}^{\infty}\frac{t^k}{k!}
       =1-e^{-t}\sum_{k=0}^{q-1}\frac{t^k}{k!}.
\]
Differentiation yields F_q'(t)=t^{q-1}e^{-t}/(q-1)! for t>0, with F_q(0)=0 and F_q(t)→1. Hence F_q(t)=P(Y_q≤t), where Y_q has gamma density t^{q-1}e^{-t}/Γ(q). This *exact finite-parameter identity* is stronger than invoking a Poisson CLT.

**2. Compute the global variation by the layer-cake identity.** In polar coordinates dA=2πρdρ and t=mρ², so dA=(π/m)dt. Therefore
\[
 \begin{split}
 \|\mu_{m,q}-\nu_{m,a}\|_{\rm TV}
 &=\frac1m\int_0^\infty|F_q(t)-\mathbf1_{\{t>a\}}|\,dt\\
 &=\frac1m\left(\int_0^aF_q(t)\,dt
            +\int_a^\infty(1-F_q(t))\,dt\right)\\
 &=\frac1m\bigl(\mathbb E(a-Y_q)_+ +\mathbb E(Y_q-a)_+\bigr)
 =\frac1m\mathbb E|Y_q-a|.
 \end{split}
\]
The two integrals are finite because E Y_q=q. This proves both that the *difference* is globally integrable despite the two individual infinite masses and (A). Removing the absolute value and using (a-Y)_+−(Y-a)_+=a-Y proves (B). In particular, the signed difference is not a comparison of individually finite total masses.

**3. Compute the centering constant exactly.** Since E Y_q=q, the positive and negative parts of Y_q−q have the same expectation. A gamma integration by parts, or Γ(q+1,q)=qΓ(q,q)+q^q e^{-q}, gives
\[
 \begin{split}
 \mathbb E(Y_q-q)_+
 &=\frac1{\Gamma(q)}\int_q^\infty(t-q)t^{q-1}e^{-t}\,dt\\
 &=\frac{q^q e^{-q}}{\Gamma(q)}.
 \end{split}
\]
Twice this quantity proves (C) for every integer q≥1. It also shows that the global variation rate is not a numerical artifact.

**4. Obtain the sharp limit with no exchange of divergent masses.** Stirling's formula gives
\[
 \frac{2q^q e^{-q}}{\Gamma(q)}
 =\sqrt{\frac{2q}{\pi}}\left(1+O(q^{-1})\right)
 \qquad(q\to\infty).
\]
For a=mλ and q=q_m=floor(mλ), the elementary 1-Lipschitz property of x↦|Y_q-x| and |mλ-q_m|<1 imply
\[
 \left|\mathbb E|Y_{q_m}-m\lambda|
      -\mathbb E|Y_{q_m}-q_m|\right|<1.
\]
Divide by m, multiply by sqrt(m), and use q_m/m→λ>0 to obtain (D). No limit is taken separately of the two infinite measures; the integrable difference is computed first.

## Classification, dependence and recommended optional addition

- **Status/severity:** **low / verified conditional deduction**. The exact Gaussian formula has been independently reconstructed from the monomial orthogonality proof; the deduction uses only elementary gamma calculus, polar coordinates and Stirling. The printed Theorem 18.41.9 is **not false** and does not have an identified proof gap here. Its general-r statement and all other sections remain uncertified.
- **Nonduplication:** §18.41.9 states *local* total-variation convergence for all positive integers r and q_m=floor(mλ). It does not supply the **global** finite variation of the *difference* on the noncompact plane, the exact gamma absolute-deviation identity, the finite-q factorial constant, the signed mass defect or the sharp m^{-1/2} constant. This §18.41 was marked inventory-only in the existing coverage matrix.
- **Proposed change:** an *optional* corollary immediately after Theorem 18.41.9 explicitly restricted to r=1, with formulas (A)–(D) and the infinite-mass caveat. Preserve theorem wording, historical attribution, source labels, permanent tags and conventions; this audit does **not** edit production text.
- **Affected dependents:** quantitative Gaussian model comparisons for the §18.41→§18.42 localization discussion; a global constant may not be transported to a compact curved model without new geometric estimates. No claim is made about the general-r leading constant or weighted global L² arguments.
- **Coverage limit:** first proof-level selected visit to §18.41, with the exact kernel, r=1 specialization and Theorem 18.41.9 limit comparison inspected. We did **not** audit §18.42's L²-correction chain and did **not** certify any complete section, chapter, proof-expansion dependency chain, build, CI or published edition.
- **User-deferred topics:** Demailly approximation/regularization and its dedicated Bergman, L², Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof-completion programme remain **deferred-by-user**, not resolved, certified or re-opened.
