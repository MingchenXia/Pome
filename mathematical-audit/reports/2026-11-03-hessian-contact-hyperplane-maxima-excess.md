# 2026-11-03 — an exact hypersurface contact mass for the bounded complex Hessian maximum inequality

**Finding:** `POME-HESS-MAX-CONTACT-SINGULAR-EXCESS-001`. **Severity:** low. **Status:** verified conditional deduction (an independently computed model for the printed measure inequality, **not** a false theorem and **not** a complete verification of its analytic proof). **Reviewed production main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. **Starting mathematical-audit branch head:** `2f7f0cc665d59720d360f6ad1d91c24ba7cd2931`.

## Pinned integrated reading-edition passages

- Main `docs/sections/complex-hessian-equations--locality-and-maxima-of-bounded-potentials/index.html`, blob `8750df56019c14e16704607ca20fa8b90f137fb0`: Proposition **8.12.1**, source `non-kahler-pluripotential-theory:C5CC915B`, permanent `9989CBEEE646`, physical lines **10–30** (strict-set locality and its proof); Theorem **8.12.2**, source `non-kahler-pluripotential-theory:D838B734`, permanent `655B0BBF4F9C`, physical lines **37–59** (measure domination including contact set).
- Normalization only, not new proof certification: `docs/sections/complex-hessian-equations--bounded-potentials-and-recursive-hessian-currents/index.html`, blob `117b866408974cdf706bf305df75e35e1b8affde`, equation **8.9.2**, lines **35–41**, source `non-kahler-pluripotential-theory:C10D5DA8`, permanent `66BDC02D9E25`; equation **8.9.5**, lines **83–90**, source `non-kahler-pluripotential-theory:E021C6DE`, permanent `17FA1BFF2491`; Proposition **8.9.7**, lines **123–144**, source `non-kahler-pluripotential-theory:633FD461`, permanent `26EFAEC0B76D`.
- Scope of the Hessian chapter: `docs/sections/complex-hessian-equations/index.html`, lines **6–13**, explicitly fixes `2 <= m < n`. We work with arbitrary integers `n >= 3, 2 <= m < n`.

## Statement and construction

Let `X = C^n/(Z+iZ)^n` with the translation-invariant Kähler form
\[
 \beta=\sum_{j=1}^{n}\beta_j,\qquad
 \beta_j=dd^c|z_j|^2=\frac{dx_j\wedge dy_j}{\pi},
 \qquad dd^c=\frac{i}{2\pi}\partial\bar\partial.
\]
Pick a small embedded coordinate box `V` and a real smooth cut-off `chi` supported in a larger embedded chart and equal to one near the closure of `V`. The globally smooth real function `f=chi x_1` is zero off that chart. Choose `t>0` small enough that `\beta+t dd^c f>0` globally. Set
\[
 u=0,\qquad v=tf,\qquad w=\max\{u,v\}.
\]
Both `u,v` are smooth strictly `\beta`-psh, and `w` is bounded continuous `\beta`-psh, hence all three are admissible for each `2 <= m < n`. On `V`, `v=t x_1`, `w=t(x_1)_+`, and
\[
  dd^c u=dd^c v=0,\qquad
  dd^c w=\frac{t}{4\pi}\delta(x_1)\,dx_1\wedge dy_1. \tag{A}
\]
Here `delta(x_1) dx_1` is the transverse Dirac measure. Formula (A) follows directly from `\Delta (x_1)_+=\delta(x_1)` in the real `(x_1,y_1)` plane and `dd^c g=(\Delta g)/(4\pi)\,dx\wedge dy` for functions of one complex variable; no singular-potential approximation theorem is used.

On the interface `\{x_1=0\}\cap V` the canonical representative `w` vanishes. Consequently the product `w\,dd^c w` is exactly zero as a measure, so the integrated recursive definition gives
\[
 D_2(w,w)=dd^c(w\,dd^c w)=0,\qquad
 D_p(\underbrace{w,\ldots,w}_{p})=0\quad(p\ge2).
\]
All higher recursively defined terms involving at least one zero potential vanish too. Using the subset formula for the shifted product, for each `1 <= r <= m` with the remaining `m-r` arguments equal to zero, one therefore obtains **exactly on V**
\[
 \begin{aligned}
 \mu_r(w)&:=Q_m(\underbrace{w,\ldots,w}_{r},
                   \underbrace{0,\ldots,0}_{m-r})
            =\beta^n+r\,\beta^{n-1}\wedge dd^c w,\\
 \mu_r(u)&=\mu_r(v)=\beta^n,\\
 \mu_r(w)-\mathbf1_{\{u\ge v\}}\mu_r(u)
           -\mathbf1_{\{u<v\}}\mu_r(v)
          &=\frac{r t(n-1)!}{4\pi}\,
            \delta(x_1)dx_1\wedge dy_1\wedge
            \beta_2\wedge\cdots\wedge\beta_n. \tag{B}
 \end{aligned}
\]
The last expression is a **strictly positive, nonzero measure**, supported precisely by the local contact hypersurface `\{u=v\}\cap V`, for `r>=1`. To check the combinatorial coefficient, in `\beta^{n-1}\wedge dx_1\wedge dy_1` only the product `(n-1)!\beta_2\wedge\cdots\wedge\beta_n` survives. The ambient absolutely continuous term cancels because the partition `\{u\ge v\}\sqcup\{u<v\}` covers all of `V`.

This is a strictness example **within the full compact-manifold hypotheses** of Theorem 8.12.2 and for every permitted intermediate Hessian degree. In particular, no equality in that theorem can be inferred even from strictly admissible *smooth* input potentials `u,v`; the maximum creates hypersurface mass. The support is in a real codimension-one contact set and must not be confused with the codimension-two zero-Sobolev-capacity phenomena in Example 8.10.7.

## Direct verification and limits

The calculation can be checked independently without invoking decreasing convergence, quasi-continuity, any Bergman or L2 theorem, or any regularization programme: the only nonsmooth Hessian is the distributional second derivative of the one-variable positive part, and `w\,dd^c w=0` as a measure because the continuous coefficient vanishes on its support. In the integrated reading edition, all `D_p` appear inside the shifted subset sum; higher `D_p` vanish here, so no unsupported square of a delta distribution is formed.

Theorem 8.12.2 is *consistent* with (B), not refuted. The calculation checks the direction of its contact-set inequality and shows why replacing the printed domination by equality is invalid. It does **not** establish the theorem for arbitrary bounded admissible potentials: the general strict-set localization in Proposition 8.12.1 and weighted convergence/quasicontinuity upstream remain conditional dependencies. Do not regard this as a whole-section certification.

## Classification, correction and dependents

- **Classification:** low / **verified conditional deduction**; positive explicit model and sharp structural obstruction to an unclaimed equality, rather than a confirmed error or a proposed complete repair.
- **Proposed optional correction:** include a short warning/example after Theorem 8.12.2: even if both initial potentials are smooth and strictly `m`-admissible, the maximum may produce nonzero singular Hessian mass on their contact hypersurface. No change to Theorem 8.12.2 is called for.
- **Affected dependents:** any later comparison, localization or capacity argument using the Theorem 8.12.2 measure inequality, notably §8.13, must retain the inequality and cannot replace it by equality on contact. The older §8.9 torsion and §8.10 codimension-two findings are unchanged.
- **Actual coverage increment:** new exact local/max computation and direct statement/hypothesis inspection at §§8.12.1–2; §8.9.2/5 and §8.9.7 are **normalization and definition crosschecks only** (they were previously partially audited). Neither entire §8.12 nor a general bounded Hessian calculus is certified.
- **Permanent exclusions:** all Demailly approximation/regularization and dedicated Bergman, L2, Ohsawa–Takegoshi, multiscale-atlas, positivity-loss proof-completion items remain **deferred-by-user**, not resolved.
- **Operations:** review/audit Markdown only; no source, main, registry, tags, private data, tests, build, CI, formal verification or website publication.
