# 2026-10-27 — Degenerate Monge–Ampère trace sharpness and the ABP–viscosity input

**Reviewed main:** b6933b772f41b45918f7e25ed1afbbb1fd892272 (freshly checked against the remote main branch).
**Starting audit branch:** review/mathematical-audit at 5dc554e85f165dfb8656f891d7244c03d59b3dca.
**Scope:** first selected proof-level inspection of §15.18 of the current integrated reading edition. No other section is counted as newly reviewed. All source/body/registry/tag changes are proposals only.

## Exact integrated source anchors

- Main path: docs/sections/equations-with-prescribed-singularities--interior-smoothness-on-the-regular-locus/index.html; blob 92eb0397f5c1a2fb58e2ddfbff378ffd70d95ae2; section tag **899B82DE5E84**; contributing source family **non-kahler-pluripotential-theory**.
- Proposition **15.18.5**, permanent tag **7DF8FE8A18D7**, original source label **00738DAE**; hypotheses/three equivalences at physical lines **135–149**, smooth-density equation (15.18.6), permanent tag **7A41D9785A7C**, lines **136–138**; proof lines **157–213**.
- Independent contextual checks: local comparison Proposition 15.18.3, tag **D2F8F8FD5A17**, original label **175BF5DC**, lines **50–126**; torsion-gradient Lemma 15.18.8, tag **3EBB652C42D7**, original label **08DA38DC**, lines **225–290**; ball-boundary trace Proposition 15.18.14, tag **6586F9B3B128**, original label **68359EE0**, lines **295–411**.
- The shared normalization from docs/sections/conventions/index.html is $\mathrm{dd}^{\mathrm c}=(\mathrm i/2\pi)\partial\bar\partial$, with no $1/n!$ in Monge–Ampère masses.

## POME-MA-INTERIOR-POSITIVE-DENSITY-NECESSITY-001

**Status:** verified conditional deduction; **severity:** low (sharpness/necessary hypothesis, not a false printed theorem).  
**Affected statement:** Proposition 15.18.5, especially the implication (3) $\Rightarrow$ (1) in lines 180–210, with the strictly positive smooth density $F$ in lines 135–138.  
**Suggested disposition:** preserve strict positivity of $F$ and optionally add the following self-contained counterexample near Proposition 15.18.5. No theorem correction is required.

Let $n\geq2$, let $B\Subset\mathbb C^n$ be a ball intersecting $\{\operatorname{Re}z_1=0\}$, put $\vartheta=0$, and use
\[
 \beta=\frac{\mathrm i}{2\pi}\sum_{j=1}^n dz_j\wedge d\bar z_j,
 \qquad u(z)=\bigl(\max\{\operatorname{Re}z_1,0\}\bigr)^2.
\]
Writing $x=\operatorname{Re}z_1$, the one-variable function $f(x)=(x_+)^2$ is convex, continuously differentiable, and has distributional second derivative $f''=2\mathbf1_{\{x>0\}}$. There is **no Dirac mass** along $x=0$, since $f'$ is continuous there. Consequently $u$ is a bounded local plurisubharmonic function, belongs to $C^{1,1}$ but not $C^2$ across that real hypersurface, and
\[
 T=\mathrm{dd}^{\mathrm c}u
 =\frac12\mathbf1_{\{x>0\}}\frac{\mathrm i}{2\pi}
     dz_1\wedge d\bar z_1\geq0,\qquad
 \operatorname{tr}_{\beta}T=\frac12\mathbf1_{\{x>0\}}\in L^\infty_{\rm loc}.
\]
Every usual smooth convolution of $u$ depends only on $x$ and has a $(1,1)$-Hessian of complex rank at most one. Its $n$th exterior power vanishes for $n\geq2$. By bounded Bedford–Taylor monotone continuity (or the canonical decreasing one-variable convolution), the Bedford–Taylor Monge–Ampère measure also vanishes:
\[
                       T^n=0=F\beta^n,\qquad F\equiv0.
\]
Here $F$ is **smooth and nonnegative**, and condition (3) of Proposition 15.18.5 holds, while condition (1) fails and no $T\geq\delta\beta$ with $\delta>0$ is possible. Thus replacing the printed assumption $F>0$ by $F\geq0$ invalidates its trace-to-smoothness and trace-to-ellipticity implications, even among $C^{1,1}$ solutions.

This is a boundary/sharpness example only, not a counterexample to the printed proposition. Its equation is maximally degenerate $F=0$, rather than the previously recorded **positive-constant-density** discontinuous model of §15.21; those are mathematically different claims. The constant-rank argument does not require regularization of Demailly type or any of the author-excluded analytic programmes. It is specifically dimension-dependent: the displayed $T^n=0$ argument requires $n\geq2$.

**Affected dependents:** whenever the local smoothness criterion of Proposition 15.18.5 is applied in the regular-locus arguments of §15.18, retain the uniform local bound $F\geq m>0$ used at physical lines 180–188. Do not infer ellipticity from a bounded trace alone if the determinant density may vanish.

## POME-MA-INTERIOR-ABP-VISCOSITY-INPUT-001

**Status:** external dependency (unresolved self-containment); **severity:** medium. **Not a disproof of Proposition 15.18.5 or a finding that the stated analytic theorem is false.**

**Exact anchor:** same source, lines **188–210**, specifically the supporting-plane operator in lines **188–200** and viscosity transfer and elliptic bootstrap in **202–210**. The proof explicitly invokes the *Aleksandrov maximum principle*, with citation **GT01, Chapter 9, Theorem 9.1**, at line **208**, and then a variable-coefficient Evans–Krylov theorem plus Schauder regularity at line **210**.

After the bounded-trace hypothesis gives $u\in W^{2,q}_{\rm loc}$ for all finite $q$ and
\[
 \delta I\leq \Theta(x)+P(D^2u)\leq LI \text{ a.e.},\qquad
 \delta=mL^{1-n}>0,
\]
the displayed concave extension is
\[
 G(x,M)=\inf_{\delta I\leq A\leq LI}
 \left\{\log\det A+
   \operatorname{tr}\!\big(A^{-1}[\Theta(x)+P(M)-A]\big)\right\}
 -\log F(x).
\]
Its a.e. equation follows from the tangent-plane formula for $\log\det$; the positive and finite ellipticity constants are supplied by $\delta,L$. To deduce viscosity inequalities, the proof invokes a maximum principle for a $W^{2,q}$ function tested against a uniformly elliptic second-order operator. The **upper-touch** argument freezes $A$; in the **lower-touch** argument it chooses a **measurable field $A(x)$** of admissible matrices and applies the maximum principle to the corresponding nondivergence operator with merely measurable principal coefficients. An ordinary smooth maximum principle is not by itself a complete replacement for this step.

**Precise proof-completion task, outside the excluded scope:** check whether a previously proved **internal** Aleksandrov–Bakelman–Pucci estimate or $W^{2,q}$-strong-to-viscosity lemma applies to uniformly elliptic measurable nondivergence coefficients; if absent, add a narrowly stated/proved internal lemma or retain the explicit GT01 input. Separately retain the variable-coefficient Evans–Krylov/Schauder input as a genuine analytic prerequisite, rather than silently treating the supporting-plane construction as a proof of these regularity theorems. This is an **application-specific dependency registration**, not a duplicate purported discovery of the general Evans–Krylov external-input issue already logged as **POME-MA-SMOOTH-REG-EXTERNAL-001** for §14.5. No internal ABP/viscosity lemma has been certified in this audit.

**Affected dependents:** Proposition 15.18.5, the section's regular-locus smoothing theorem 15.18.1 wherever its proof invokes that proposition, and any later step relying on the asserted smoothness upgrade. No formalization or independent PDE-theorem proof is claimed.

## Additional checks without separate new findings

1. The matrix inequality at lines 166–175 is correct: if $\lambda_i=\delta+a_i$, $a_i\geq0$, then
   $\prod_i\lambda_i\geq\delta^n+\delta^{n-1}\sum_i a_i
     =\delta^{n-1}(\sum_i\lambda_i-(n-1)\delta)$.
2. The lower eigenvalue bound $m/L^{n-1}$ at lines 180–186 follows from determinant $F\geq m$ and each eigenvalue $\leq L$; it **essentially** uses $m>0$.
3. Selected local comparison (§15.18.3) and Hermitian torsion-gradient / boundary trace (§15.18.8, §15.18.14) steps were read for hypotheses and signs, but their full PDE dependence and the remaining §15.18 theorem chains have **not** been independently certified.

**Coverage and integrity:** exactly one previously inventory-only actual ToC row (§15.18) is upgraded to **selected-passages only**; preserve 747 current unique numbered sections and do not certify an entire section. No source modifications, publishing, integration/canonicalization edits, tests, build, CI, or formal verification. The dedicated Demailly approximation/regularization and Bergman, $L^2$, Ohsawa–Takegoshi, multiscale-atlas, positivity-loss proof-completion programmes remain **deferred-by-user**, neither reopened nor certified. The use of elementary convolution in the printed local PDE argument is read only as a stated independent input and is not a renewal of that deferred programme.
