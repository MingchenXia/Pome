# Atomic-trace Poisson equations: sharp \(L^p\) stability and failure at \(p=1\)

**Audit date:** 2026-10-31. **Reviewed production main:** b6933b772f41b45918f7e25ed1afbbb1fd892272.  
**Stable finding ID:** **POME-TRACE-POISSON-LP1-SHARP-001**.  
**Severity/status:** **low / verified conditional deduction**. The printed theorem is correct. The findings below strengthen its stability conclusion and demonstrate that its \(p>1\) hypothesis cannot be dropped for universal existence in the prescribed ordinary singularity type; they are **not** a false-theorem report, original proof gap, or entire-dependency certification.

## Pinpointed integrated reading edition

**Main file:** docs/sections/restriction-and-intrinsic-trace-data/index.html, blob **dbc3b722ceacb8232fe4c7b711e5ad98b0708f06**.

- **Theorem 20.3.15**, source **non-kahler-pluripotential-theory:46A3A7FE**, permanent tag **AFC6C3B6368C**; physical lines **318–353**. The density exponent and mass normalization occur at **319–327**, the Poisson construction at **334–345**, and uniqueness and mass necessity at **347–353**.
- The enclosing **§20.3.14**, source **non-kahler-pluripotential-theory:DFBA3531**, permanent tag **E07C398EC98F**, lines **313–315**.
- **Theorem 20.3.10**, source **non-kahler-pluripotential-theory:C5D10418**, permanent tag **879739B42EBB**, lines **226–272**, especially the finite atomic trace and compact-curve Green kernel at **254–270**. This is an **internal conditional input** for the review, not an independently certified upstream proof.
- **Proposition 20.3.13**, lines **290–309**, was consulted for its atomic-mass conventions only. Its approximation arguments, and all Demailly/regularization-related work, remain deferred by the user. Earlier audit findings POME-TRACE-ATOMIC-INTERPOLATION-001 and POME-TRACE-CURVE-NOWHERE-LOCALLY-COMPACT-001 concern different mathematical questions and are not counted again.

## Exact stability statement

Let \(Y\) be a connected compact Riemann surface, \(\beta\) a smooth real \((1,1)\)-form, \(M=\int_Y\beta>0\), and \(\eta\) a smooth positive \((1,1)\)-form with \(\int_Y\eta=1\). Let \(D\) be a finite positive atomic measure with total mass \(0\le d\le M\), in particular the atomic trace \(D_u\) in Theorem 20.3.10. By the compact-curve Green construction let

\[
 dd^c w_D=D-d\eta,\qquad dd^c s_*=M\eta-\beta,
\]

with the additive constants normalized to zero \(\eta\)-mean, where \(s_*\) is smooth. Choose the Green kernel \(G(x,y)\) with \(dd^c_xG(x,y)=\delta_y-\eta\), zero \(\eta\)-mean in \(x\), and local logarithmic singular part \(\log|z(x)-z(y)|^2\) in the convention used at §20.3.10.

For a probability density \(f\ge0\) with \(f\in L^p(\eta)\), \(p>1\), define

\[
 H_f(x)=\int_YG(x,y)(f(y)-1)\,\eta(y),\qquad
 s_{d,f}=s_*+(M-d)H_f,\qquad
 v_{D,f}=w_D+s_{d,f}.
\]

Then the correction \(s_{d,f}\) is continuous and bounded and

\[
 \beta+dd^cv_{D,f}=D+(M-d)f\eta,\qquad
 \operatorname{MA}^{\rm ext}_\beta(v_{D,f})=(M-d)f\eta.
\]

Thus \(v_{D,f}\) belongs to the **ordinary**, not merely multiplier-ideal, singularity type of \(w_D\). For \(M>d\), it is exactly the normalized solution considered in Theorem 20.3.15. For \(d=M\), it gives the stated zero-extended-mass endpoint.

If \(f,g\) are two such probability densities and \(p'=p/(p-1)\), set

\[
 C_{p,Y,\eta}
 :=\sup_{x\in Y}\|G(x,\cdot)\|_{L^{p'}(\eta)}<\infty.
\]

The normalized corrections satisfy the **quantitative estimate**

\[
 \boxed{\quad
 \|s_{d,f}-s_{d,g}\|_{L^\infty(Y)}
 \le (M-d)\,C_{p,Y,\eta}\,\|f-g\|_{L^p(\eta)}.
 \quad}
\]

More generally, for another atomic measure \(E\) of mass \(e\le M\),

\[
 \|s_{d,f}-s_{e,g}\|_\infty
 \le C_{p,Y,\eta}
 \left((M-d)\|f-g\|_p+|d-e|\|g-1\|_p\right).
\]

**Structural observation:** the bounded correction depends on the atomic trace **only through its total mass**, and for \(f\equiv1\) is exactly \(s_*\), independent even of that mass. This does **not** say that the singular Green parts \(w_D\) are uniformly stable as atom positions move.

## Proof of the quantitative statements

Since \(dd^c_xG(x,y)=\delta_y-\eta\) and \(\int_Y(f-1)\eta=0\), we have

\[
 dd^cH_f=(f-1)\eta,\qquad \int_YH_f\,\eta=0.
\]

It follows directly that

\[
 \begin{aligned}
 dd^cs_{d,f}
 &=M\eta-\beta+(M-d)(f-1)\eta\\
 &=d\eta+(M-d)f\eta-\beta,
 \end{aligned}
\]

and adding \(dd^cw_D=D-d\eta\) proves the current identity. The absolutely continuous term \(f\eta\) charges no polar set, while all the atomic mass \(D\) lies at logarithmic poles. Consequently the degree-one extended non-pluripolar product removes precisely \(D\) and gives \((M-d)f\eta\). A bounded continuous correction leaves the ordinary type unchanged. If two such solutions have the same curvature measure, their difference is a global harmonic distribution and hence a constant on the connected compact curve.

The Green kernel is uniformly bounded away from a fixed neighborhood of the diagonal, and locally equals \(\log|z(x)-z(y)|^2\) plus a uniformly bounded smooth term. For every **finite** \(q\),

\[
 \int_0^\rho |\log r|^q r\,dr<\infty.
\]

A finite chart cover therefore gives

\[
 \sup_{x\in Y}\|G(x,\cdot)\|_{L^q(\eta)}<\infty.
\]

It also gives \(L^q\)-continuity in the first variable, by splitting into a small diagonal neighborhood (uniformly small \(L^q\)-mass) and its smooth complement. Taking \(q=p'<\infty\), Hölder's inequality proves both continuity of \(H_f\) and the boxed bound. The two-parameter bound follows from the exact algebraic identity

\[
 s_{d,f}-s_{e,g}=(M-d)(H_f-H_g)+(e-d)H_g.
\]

These steps use the compact-curve Green construction and elementary integration only. No Demailly regularization, Bergman estimate, \(L^2\) or Ohsawa–Takegoshi extension, or positivity-loss argument is involved.

## Sharp failure of universal existence at \(p=1\)

Take \(Y=\mathbb P^1\), \(\beta=\eta=\omega_{\rm FS}\) with \(\int_Y\eta=1\), \(D=0\), so \(M=1\) and the required ordinary trace type is the smooth/locally bounded type. In a coordinate \(z\) centered at a point \(o\), choose a nonnegative smooth cutoff \(\chi\), supported in \(|z|<e^{-2}\) and equal to \(1\) near \(o\). Put

\[
 f(z)=\frac{c\,\chi(z)}
 {|z|^2(\log(1/|z|))^2}
\]

on the chart and zero elsewhere, with \(c>0\) normalized by \(\int_Yf\eta=1\). This is a nonnegative \(L^1\) probability density, since

\[
 \int_0^\rho \frac{dr}{r(\log(1/r))^2}<\infty.
\]

However \(G(o,z)=\log|z|^2+O(1)\), so its Green potential at the center is \(-\infty\):

\[
 \int_YG(o,y)f(y)\eta(y)
 \asymp -\int_0^\rho\frac{dr}{r\log(1/r)}
 =-\infty
\]

(the symbol here indicates divergence with the displayed sign). Solving \(dd^cv=(f-1)\eta\) uniquely up to a constant produces this unbounded-below Green potential. Any solution in the **ordinary type of zero** would be globally bounded. The difference of two distributional solutions is harmonic and constant, hence no bounded solution exists. This is a counterexample to extending the **hypotheses** of Theorem 20.3.15 to arbitrary \(L^1\) densities, not to the printed \(p>1\) theorem. Notably \(f\eta\) has no atomic mass and all point Lelong numbers vanish; that alone does not yield bounded ordinary singularity type.

## Sharp failure of \(L^1\to C^0\) stability even for smooth positive data

In the same \(Y,\beta,\eta,D\) model, choose smooth probability bumps \(b_\epsilon\ge0\) supported in \(|z|<\epsilon\), obtained by rescaling one fixed radial bump and renormalizing against \(\eta\). For \(0<\epsilon<e^{-2}\), set

\[
 \delta_\epsilon=\frac1{|\log\epsilon|},\qquad
 f_\epsilon=(1-\delta_\epsilon)\cdot1+\delta_\epsilon b_\epsilon.
\]

Each \(f_\epsilon\) is **smooth, strictly positive and normalized**; \(\|f_\epsilon-1\|_{L^1(\eta)}\le2\delta_\epsilon\to0\). Let \(v_\epsilon\) denote the normalized smooth solution \(dd^cv_\epsilon=(f_\epsilon-1)\eta\), and \(v_0=0\). The diagonal logarithm and bump scaling give

\[
 \int_YG(o,y)b_\epsilon(y)\eta(y)
 =2\log\epsilon+O(1).
\]

The zero-mean Green normalization gives \(\int_YG(o,y)\eta(y)=0\) when the symmetric normalized kernel is used; with another fixed kernel normalization this term remains \(O(1)\), which yields the same limit. Therefore

\[
 v_\epsilon(o)
 =\delta_\epsilon(2\log\epsilon+O(1))
 \longrightarrow -2\ne v_0(o).
\]

There is no uniform convergence of smooth Poisson potentials despite the \(L^1\)-convergence of their strictly positive densities. The limit \(-2\) uses the explicit §20.3.10 convention that the Green logarithmic singularity is \(\log|z|^2\).

## Finding disposition, dependencies and exact coverage

**Status:** low / **verified conditional deduction**. Theorem 20.3.15 is correct; the exponent \(p>1\) is genuinely relevant to its ordinary-type conclusion, and the displayed estimate adds an explicit stability theorem. The used upstream input is the compact-curve Green representation of Theorem 20.3.10; this audit does not independently certify that theorem's full source chain. **Proposed optional correction to exposition:** add the estimate and the explicit \(L^1\) endpoint obstruction as a remark after 20.3.15. **No source correction is required.**

**Affected dependents:** interpretations of the atomic-trace Poisson construction later in §20.3 and of the trace-realization question §24.9; neither unconditional \(L^1\)-stability nor arbitrary \(L^1\) existence in a prescribed *ordinary* type follows from the printed theorem. Distinct historical versions, permanent tags and attributions must be retained.

**Actual new verification:** selected hypotheses, mass, Poisson construction and uniqueness of **20.3.15**, and just the Green/atomic normalization in **20.3.10**. **20.3.13** was consulted only as context. No section or chapter is fully certified. The durable matrix remains **25 chapters / 747 numbered ToC sections / zero completely certified mathematical sections**. Earlier errors, proof gaps, external inputs, genuine duplicates and conditional repairs are not reclassified.

**Explicitly excluded, deferred-by-user:** Demailly approximation/regularization and the dedicated Bergman, \(L^2\), Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof-completion programme. Nothing in that programme was reopened or deemed proved. This report is Markdown-only; **no project build, tests, CI, formal verification, site publication, main/source/registry/canonicalization edit or permanent-tag change** was performed.
