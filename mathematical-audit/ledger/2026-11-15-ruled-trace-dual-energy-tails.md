# Ledger: two energy hierarchies on the nonclosed ruled-surface trace model

**Finding:** POME-TRACE-RULED-DUAL-ENERGY-TAILS-001  
**Date:** 2026-11-15  
**Severity:** low  
**Status:** **verified conditional deduction** (original printed theorem correct; no proof-gap closure or full-section certification claimed).

**Reviewed main:** b6933b772f41b45918f7e25ed1afbbb1fd892272.  
**Exact main reading path:** docs/sections/restriction-and-intrinsic-trace-data/index.html; Git blob **dbc3b722ceacb8232fe4c7b711e5ad98b0708f06**.

**Source/permanent anchors:** §20.3 source/section **non-kahler-pluripotential-theory / E6AE4A881F9F**; §20.3.63 source **ECB5F6D3**, permanent **070063ADB7C2**, lines 1185–1203; Lemma 20.3.65 source **8F6D11C0**, permanent **72230836D2EE**, lines 1206–1227; Theorem 20.3.66 source **D8182E16**, permanent **9EDE5892D63B**, lines 1232–1243 and proof 1248–1307; Equation 20.3.69 source **AB4D6D19**, permanent **F060F71204CB**, lines 1293–1298; previous first-moment statement lines 1310–1311.

**Exact hypotheses:** $Y=P^1\times P^1$; $0<\alpha<1$; $\theta=cw_1+a w_2$ with $c>0$ and $a>0$ smooth on the first factor (nonclosed when $a$ is nonconstant); $0\le b<c$; $k=c-b$; fixed sufficiently large $L$ with $\epsilon_L=\alpha(1+L)^{\alpha-1}<k/2$; explicitly printed $q_L=\chi_L(G_p)$ and $v_L=bG_p+q_L$. $p$-moments below use a different letter $s>0$ to avoid confusion with the chosen pole point $p$.

**New result / full justification:** For the finite positive extended product $\mu_L={\rm MA}^{\rm ext}_\theta(v_L)$, its exact local density outside $D$ is $2a[(k-\chi_L'(G_p))w+\chi_L''(G_p)dG_p\wedge d^cG_p]\wedge w_2$, with no mass on $D$. Unit Lelong normalization of $G_p$ and a polar-coordinate coarea calculation give $\mu_L(T>R)\sim2a(p)\alpha R^{\alpha-1}$, $T=-G_p$. The residual tail for $Q=-q_L$ is $2a(p)\alpha R^{-(1-\alpha)/\alpha}$; its $s$-moment is finite iff $s<(1-\alpha)/\alpha$. When $b>0$, the whole potential $V=-v_L$ has tail $2a(p)\alpha b^{1-\alpha}R^{-(1-\alpha)}$; its $s$-moment is finite iff $s<1-\alpha$. Both boundary moments diverge logarithmically. Full proof and constants in [report](../reports/2026-11-15-ruled-trace-residual-and-divisor-energy-tails.md).

**Old result not counted again:** printed §20.3 first-moment $s=1,b=0$ iff $\alpha<1/2$ (line 1311). Other previous §20.3 audit findings stay unchanged.

**Disposition:** optional English production addendum distinguishing residual and whole-logarithmic moments; source/registry/canonicalization edit proposed only, not made. **Affected dependents:** interpretations of §20.3.66, equation 20.3.69 and §20.3.71's ideal-order example; none is refuted.

**Coverage:** previously partially examined §20.3; new selected §§20.3.65–69, zero first-visited numbered sections and zero complete mathematical-section certificates. See [coverage](../coverage/2026-11-15-ch20-ruled-trace-energy-tails.md). **Unresolved:** general ordinary-type comparison and extended-product existence outside the explicit separated representative; no entire theorem proof certified. **Deferred-by-user:** all Demailly approximation/regularization and dedicated Bergman/$L^2$/OT/multiscale/positivity-loss proof-completion, without status alteration.
