# Sharp residual-versus-divisor energy tails in the nonclosed ruled-surface trace model

**Stable finding ID:** POME-TRACE-RULED-DUAL-ENERGY-TAILS-001  
**Date:** 2026-11-15 (Asia/Shanghai)  
**Severity/status:** low / **verified conditional deduction**. No printed assertion is refuted; the printed first-moment threshold is recovered as a special case.  
**Reviewed production main SHA:** b6933b772f41b45918f7e25ed1afbbb1fd892272  
**Integrated reading edition:** docs/sections/restriction-and-intrinsic-trace-data/index.html  
**Integrated Git blob:** dbc3b722ceacb8232fe4c7b711e5ad98b0708f06

## Exact source and permanent anchors

- §20.3, *Restriction and intrinsic trace data*, section permanent tag **E6AE4A881F9F**.
- §20.3.63 setup, original/source **non-kahler-pluripotential-theory:ECB5F6D3**, permanent heading **070063ADB7C2**, HTML physical lines **1185–1203** (Green normalization, nonclosed Hermitian background, divisor and residual pole).
- Lemma **20.3.65**, source **non-kahler-pluripotential-theory:8F6D11C0**, permanent **72230836D2EE**, physical lines **1206–1227**, including the explicit $\chi_L$ tail.
- Theorem **20.3.66**, source **non-kahler-pluripotential-theory:D8182E16**, permanent **9EDE5892D63B**, physical lines **1232–1243** (existence exactly for $b<c$, finite mass and optimized volumes), proof lines **1248–1307**; in particular the positive restricted product and zero divisor mass, **1255–1267**, and expansion **1283–1298**. Equation **20.3.69**, source **non-kahler-pluripotential-theory:AB4D6D19**, permanent **F060F71204CB**, lines **1293–1298**.
- The previously printed **first-moment** computation appears at physical lines **1310–1311**. Its $\alpha<1/2$ result is **pre-existing**, not registered here as new.
- Theorem's general cohomological comparison and arbitrary-type mass equalities are **not** proved here. This note computes the actual extended measure of the *separated explicit representatives*, without using any user-excluded approximation or regularization.

## New result: exact singular-mass tails and two distinct moment thresholds

Let $w$ be the probability Fubini–Study form on $\mathbf P^1$, and let $G=G_p\le0$ satisfy
\[
 dd^cG=[p]-w,\qquad \sup_{\mathbf P^1}G=0,\qquad dd^c=\frac{i}{2\pi}\partial\bar\partial.
\]
On $Y=\mathbf P^1\times\mathbf P^1$, put $D=\{p\}\times\mathbf P^1$ and
\[
 \theta=cw_1+a\,w_2,\quad
 0<\alpha<1,\quad c>0,\quad 0\le b<c,\quad k=c-b>0,
\]
where $a>0$ is any smooth function of the first coordinate. For $L$ sufficiently large, set $\epsilon_L=\alpha(1+L)^{\alpha-1}<k/2$ and take precisely the printed
\[
 \chi(t)=1-(1-t)^\alpha,\qquad
 \chi_L(t)=\begin{cases}\chi(t)+C_L,&t<-L,\\ \epsilon_Lt,&-L\le t\le0,\end{cases}
 \quad C_L=-\epsilon_LL-\chi(-L).
\]
Define $q_L=\chi_L(G)$, $v_L=bG+q_L$. They are nonpositive, $q_L\sim U$, $v_L\sim bG+U$, and $v_L\in{\rm PSH}(Y,\theta)$ with a strict residual lower bound. Let
\[
 \mu_L={\rm MA}^{\rm ext}_{\theta}(v_L).
\]
The divisorial contribution $b[D]$ is discarded by the extended/non-pluripolar product; $\mu_L$ has no mass on $D$.

Put $T=-G$ (viewed on $Y$ by projection). As $R\to+\infty$, with **exact leading coefficient**
\[
 \boxed{\quad \mu_L\{T>R\}\sim2\alpha\,a(p)\,R^{\alpha-1}.\quad} \tag{A}
\]
In particular, the mass is finite but its singular-coordinate tail has a polynomial decay independent of $b,c,L$.

For the **residual weight** $Q_L=-q_L$, set $\kappa=(1-\alpha)/\alpha$. Then
\[
 \boxed{\quad \mu_L\{Q_L>R\}\sim2\alpha a(p)R^{-\kappa},
 \qquad \int_Y Q_L^s\,d\mu_L<\infty\iff 0<s<\kappa.\quad} \tag{B}
\]
At $s=\kappa$ the moment diverges logarithmically, not merely by an unspecified failure of integrability.

For the **unsubtracted divisor-plus-residual potential** $V_L=-v_L$, whenever $b>0$,
\[
 \boxed{\quad \mu_L\{V_L>R\}\sim
 2\alpha a(p)b^{1-\alpha}R^{-(1-\alpha)},\qquad
 \int_Y V_L^s\,d\mu_L<\infty\iff0<s<1-\alpha.\quad} \tag{C}
\]
At $s=1-\alpha$ the divergence is logarithmic. When $b=0$, $V_L=Q_L$ and (B) applies. Thus the ordinary singularity type's **sublogarithmic residual** and the **whole logarithmic representative** have *different sharp energy hierarchies*, despite inducing the same non-pluripolar measure after the divisor is removed. All statements are for this explicit model; no abstract energy-class theorem is inferred.

## Proof: precise normalization and no hidden mass at the divisor

Because $dd^cG=-w$ away from $p$, on $Y\setminus D$ the smooth (except at the harmless piecewise-$C^2$ matching interface) residual form is
\[
 A_L=kw_1+dd^cq_L
   =\bigl(k-\chi_L'(G)\bigr)w_1
      +\chi_L''(G)\,dG\wedge d^cG.
\]
It is positive since $\chi_L'\le\epsilon_L<k/2$ and $\chi_L''\ge0$. The other factor is $a\,w_2$. Both factors square to zero by their separate factor dimensions. The product of the original current is therefore, off $D$,
\[
 (\theta+dd^cv_L)^2=2A_L\wedge a\,w_2. \tag{D}
\]
The current also contains $b[D]$, but the **extended product** is the zero extension of this bounded-factor product away from $D$, as stated explicitly in the integrated proof at lines 1255–1261. Consequently (D) determines $\mu_L$ completely, with no polar atom. The $C^1$ matching of $\chi_L$ produces no delta term along $\{G=-L\}$.

Choose a local coordinate $z$ centered at $p$. The normalization $dd^c\log|z|^2=\delta_p$ and the Green equation give
\[
 G(z)=\log|z|^2+h(z),\qquad h\text{ smooth near }0.
\]
For $r=|z|$ and angular coordinate $\vartheta$,
\[
 dG=\frac{2\,dr}{r}+O(1),\qquad
 d^cG=\frac{d\vartheta}{2\pi}+O(r).
\]
The coarea/angular integral of $dG\wedge d^cG$ between levels $T$ and $T+dT$ is therefore $(1+O(e^{-T/2}))dT$: the coefficient **one** follows directly from $\int_0^{2\pi}d\vartheta/(2\pi)=1$ and $dT=-2dr/r+O(dr)$. The smooth $w$ term has exponentially decaying level density $O(e^{-T})dT$; also $a(z)=a(p)+O(e^{-T/2})$.

For $T>L$ the nonlinear branch applies and
\[
 \chi_L''(-T)=\alpha(1-\alpha)(1+T)^{\alpha-2}.
\]
After integrating $w_2$ to one, (D) gives the precise level-density asymptotic
\[
 \frac{d\,\mu_L(T\in dT)}{dT}
 =2a(p)\alpha(1-\alpha)T^{\alpha-2}(1+o(1)). \tag{E}
\]
This is an ordinary local coarea statement, not a claim that $T$ itself is a global smooth coordinate. Integration from $R$ to infinity yields (A), since
\[
 \int_R^\infty\alpha(1-\alpha)(1+T)^{\alpha-2}dT
 =\alpha(1+R)^{\alpha-1}.
\]

On the same tail, the definitions of $\chi_L$ and $v_L$ give
\[
 Q_L=(1+T)^\alpha-1-C_L\sim T^\alpha,\qquad
 V_L=bT+(1+T)^\alpha-1-C_L\sim bT\quad(b>0). \tag{F}
\]
Their superlevel sets are therefore precisely $\{T>R^{1/\alpha}(1+o(1))\}$ and $\{T>(R/b)(1+o(1))\}$, respectively. Applying (A) proves the coefficients and exponents in (B),(C).

Finally $\mu_L$ is finite (outside the small tail, the product is locally bounded; (A) controls the tail). For any $W\ge0$ and $s>0$, Tonelli's layer-cake identity gives
\[
 \int W^s\,d\mu_L=s\int_0^\infty R^{s-1}\mu_L\{W>R\}\,dR.
\]
The two power tails yield the exact iff conditions in (B),(C), with $\int^\infty R^{-1}dR$ at their boundaries. For $s=1$ and $b=0$, (B) reduces to the **previously printed** $\alpha<1/2$ threshold at physical line 1311. The new content is the all-real-$s$ pair of sharp tails, their constants, and the separation caused by a nonzero logarithmic divisor.

## Classification, dependents, and editorial proposal

- **Classification:** low / **verified conditional deduction** based on the actual selected separated representative and the printed definition of extended products. This does not refute Theorem 20.3.66, prove its whole optimization theorem, certify every step of the local-to-global ordinary-type comparison, or solve any general trace-realization problem.
- **Affected interpretations:** the singularity representatives of §20.3.65–66, the fixed ordinary-type volume normalization (20.3.67–69), and the interpretation of analytic ideal orders in §20.3.71 (consulted for context only, not used in the proof). A proposed optional explanatory addendum should distinguish moments of the *residual* from moments of the *whole* logarithmic representative, perhaps recording the sharp exponents (B)–(C). No production patch is applied here.
- **Earlier results:** the printed $s=1,b=0$ test, and all prior audit work on §20.3.2/.4/.6/.10/.13/.15/.17/.20–22/.27/.44 and nearby sections, remain unchanged; none is re-counted as new. First-visited numbered sections **0**, fully certified numbered sections **0**; precise new selection in the companion coverage file.
- **Explicit unresolved inputs:** general extended-product theory, regularity of arbitrary-type competitors, and general cohomological volume comparison remain outside this selected direct calculation. Any occurrence of Demailly approximation/regularization is **deferred-by-user**, and no Bergman, $L^2$, Ohsawa–Takegoshi, multiscale-atlas or positivity-loss proof programme is reopened.
