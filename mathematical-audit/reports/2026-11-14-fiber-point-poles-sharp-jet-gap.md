# A sharp first-order jet-space defect for point poles on product fibrations

**Finding ID:** POME-FIBER-POINT-POLES-SHARP-JET-GAP-001  
**Date:** 2026-11-14  
**Classification:** low / **verified conditional deduction** (an exact finite-dimensional strengthening and sharpness example, **not** a false printed theorem and not a certification of the analytic convergence theorem).

## Provenance and actual inspection

- Main reviewed: \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`.
- New first direct proof-level reading: \`docs/sections/partial-kernels-and-quotient-equilibrium--isolated-logarithmic-poles-on-a-fibration/index.html\`, blob \`c63860c49c4b05ac31665aada937e81f848266b7\`.
- §18.37.1, **Lemma**: source \`non-kahler-pluripotential-theory:08207DCC\`, permanent \`22D696DB398E\`, physical lines **13–31**; exact nested-space positivity, total variation, and determinant estimates.
- §18.37.2, logarithmic pole equation: source \`non-kahler-pluripotential-theory:C1AEB350\`, permanent \`DA25AD427AC7\`, lines **33–50**.
- §18.37.3, **Proposition**: source \`non-kahler-pluripotential-theory:C595893C\`, permanent \`BEF6F7AD320C\`, lines **55–93**; exact fiberwise maximal coefficient, jet injection, and the $O(m^{q-1})$ bound.
- §18.37.4, **Theorem**: source \`non-kahler-pluripotential-theory:5221B002\`, permanent \`D9B0D46D42B2\`, lines **98–124**; the stated $O(m^{-1})$ measure comparison and finite-dimensional determinant comparison, followed by analytic convergence from §18.35.5.
- Contextual, not newly certified: \`docs/sections/partial-kernels-and-quotient-equilibrium--the-determinant-functional/index.html\`, blob \`626a4c74bb7f5e6659320052c54ec29902646b61\`, Proposition 18.34.1 source \`576F8072\`, permanent \`A1D3D26087E7\`, lines **19–49**; \`docs/sections/partial-kernels-and-quotient-equilibrium--kernels-on-a-fibration/index.html\`, blob \`f8a231d3de6115aad857e48f9700b2c48938e1f0\`, Proposition 18.36.1 source \`DF971029\`, permanent \`7E88736EF73B\`, lines **31–66**; \`docs/sections/plurisubharmonic-functions-and-singularities--multiplier-ideals-and-logarithmic-poles/index.html\`, blob \`9256668b88735f821d06b0919466a6a8cba777ed\`, Lemma 5.37.1 source \`94144E8D\`, permanent \`C21A2A6F9E07\`, lines **13–24**.

The reading-edition statement and proof of §18.37.3 are examined directly; §18.35.5 is **not** independently reproved, and no Demailly approximation, regularization, or dedicated Bergman/L²/Ohsawa–Takegoshi/multiscale/positivity-loss proof-completion programme is opened. The result concerns elementary point-ideal jets and finite-dimensional orthogonal projections only.

## New proposition: exact and asymptotically optimal defect

Let $q,f\geq1$, $n=q+f$, and $0<a<1$. Put
\[
 B=\mathbf P^q,\quad X=\mathbf P^q\times\mathbf P^f,\quad
 \pi:X\longrightarrow B,\quad A=\mathcal O_{\mathbf P^q}(1),\quad L=\pi^*A.
\]
Choose $b=[1:0:\cdots:0]\in B$ and $y\in\mathbf P^f$. There are a quasi-psh selecting potential $\varphi$ on $X$ with a **single** logarithmic point pole of coefficient $a$ at $(b,y)$, and a $\theta$-psh potential $\psi$ on $B$, $\theta=c_1(A,h_{\rm FS})$, with the same coefficient at $b$, locally bounded away from $b$, and of strictly positive non-pluripolar mass.

For each sufficiently large integer $m$, let $V_m$ be the pulled-back section space selected by $\varphi$ and $W_m$ the space on $B$ selected by $\psi$, as in §18.37.3. Then, with $k_m=\lfloor ma\rfloor$,
\[
 \boxed{\quad d_m:=\dim V_m-\dim W_m
 =\binom{k_m}{q}-\binom{k_m-f}{q}.\quad}                 \tag{A}
\]
For **every** continuous weight $v$ and every smooth positive probability measure used for the section norms, §18.37.1 therefore gives the **exact** total-variation identity
\[
 \left\|\beta^{(q)}_{V_m,v}-\beta^{(q)}_{W_m,v}\right\|_{\rm TV}
 =\frac{q!}{m^q}
  \left[\binom{\lfloor ma\rfloor}{q}
  -\binom{\lfloor ma\rfloor-f}{q}\right]
 =\boxed{\frac{qfa^{q-1}}m+O(m^{-2})}.                 \tag{B}
\]
The same identity holds for the lifted measures on $X$ (with lifted probability volume). Consequently
\[
 \boxed{\lim_{m\to\infty}
 m\,\|\beta^{(q)}_{X,m,v\circ\pi,\varphi}
       -\mathcal L(\beta^{(q)}_{W_m,v})\|_{\rm TV}
 =qfa^{q-1}>0.}                                      \tag{C}
\]
Thus **the $O(m^{-1})$ comparison in Theorem 18.37.4 is optimal in general**. For $q=1$ the difference $d_m=f$ is eventually constant, so (B) is exactly $f/m$ without an error term.

The determinant-functional comparison in §18.37.1 has the same sharp rate: for each constant weight $v\equiv c$,
\[
 \boxed{\mathcal F^{(q)}_{V_m}(c)-\mathcal F^{(q)}_{W_m}(c)
 =c\,\frac{q!d_m}{m^q}.}                             \tag{D}
\]
In particular, for $c\ne0$ its absolute value is asymptotic to
$|c|qfa^{q-1}/m$. This does **not** claim a universal first-order coefficient for arbitrary nonconstant weights.

## Proof, including the global hypotheses

1. **The selecting potential on $X$.** In a holomorphic coordinate ball at $(b,y)$ use local coordinates $w=(z,\tau)\in\mathbf C^{q+f}$, and choose a smooth cutoff $\chi$ supported strictly inside the ball and equal to one around $w=0$. Extend $\varphi=a\chi(w)\log |w|^2$ by zero outside. The cross terms in $dd^c(\chi\log|w|^2)$ are smooth and bounded on the cutoff annulus; hence $\varphi$ is globally quasi-psh, has just the prescribed logarithmic pole, and is locally bounded elsewhere. No approximation construction is used.

2. **Positive-mass base potential.** In homogeneous coordinates $[Z_0:\cdots:Z_q]$ set
\[
 \psi=a\log\frac{|Z_1|^2+\cdots+|Z_q|^2}
                       {|Z_0|^2+\cdots+|Z_q|^2}.
\]
This is globally well-defined and smooth outside $b$, with $\psi=a\log|z|^2+O(1)$ there. On $B\setminus\{b\}$,
\[
 \theta+dd^c\psi=(1-a)\theta
       +a\,dd^c\log\bigl(|Z_1|^2+\cdots+|Z_q|^2\bigr)
 \ \geq\ (1-a)\theta,
\]
where the last term is the pullback of the Fubini–Study form on $\mathbf P^{q-1}$ (zero for $q=1$). Thus the non-pluripolar mass is at least $(1-a)^q\int_B\theta^q>0$.

3. **The exact point ideals.** For $u=a\log|w|^2+O(1)$ in complex dimension $d$, a holomorphic germ of order $j$ has locally integrable $|g|^2e^{-mu}$ precisely when $j+d-ma>0$. Indeed the radial power in the volume integral is $2(j+d-ma)-1$, and a nonzero leading homogeneous term has a positive spherical integral. Hence the exact ideal is the $(\max\{\lfloor ma\rfloor-d+1,0\})$th maximal-ideal power. This independently verifies the elementary point-pole instance of Lemma 5.37.1 without invoking regularization. Applied on $X$ and $B$, for all large $m$ the powers are
\[
 r_m=k_m-q-f+1,\qquad s_m=k_m-q+1=r_m+f,
\]
and $0\leq r_m<s_m\leq m$. As in the directly read §18.37.3, sections on $X$ descend to sections on $B$, since each compact connected $\mathbf P^f$ fiber has only constant holomorphic functions.

4. **Jet-surjectivity, not merely an upper bound.** In the affine chart $Z_0\ne0$ at $b$, every monomial $z^\alpha$ of total degree $|\alpha|\leq m$ is the local expression of the global degree-$m$ homogeneous section $Z_0^{m-|\alpha|}Z_1^{\alpha_1}\cdots Z_q^{\alpha_q}$. Consequently the map
\[
 H^0(B,\mathcal O(m)\otimes\mathfrak m_b^{r_m})
 \longrightarrow\mathfrak m_b^{r_m}/\mathfrak m_b^{s_m}
\]
is **surjective** whenever $0\leq r_m\leq s_m\leq m+1$. Its kernel is precisely the $s_m$-vanishing space. Thus
\[
 d_m=\sum_{j=r_m}^{s_m-1}\binom{j+q-1}{q-1}
 =\binom{s_m+q-1}{q}-\binom{r_m+q-1}{q},
\]
which is (A). The source only uses injectivity to obtain its general upper bound; this special case achieves equality.

5. **Sharp asymptotics and norms.** For fixed $f$ and $q\geq2$,
\[
 \binom{k}{q}-\binom{k-f}{q}
   =\frac{f}{(q-1)!}k^{q-1}+O(k^{q-2});
\]
for $q=1$ it is identically $f$ at large $k$. Since $k_m=am+O(1)$, this proves (B). Extending an orthonormal basis of $W_m$ to one of $V_m$ at **each** fixed weight makes the difference of kernel densities a sum of squares, with integral $d_m$. It follows that their difference is a positive measure whose total variation is its total mass $q!d_m/m^q$. The probability-fiber lift preserves this total mass and its positivity. This establishes (B)–(C), not just convergence along a subsequence or for a special weight.

6. **Constant-weight determinant exactness.** By the displayed Gram determinant definition in §18.34, replacing $v=0$ by $v=c$ multiplies each Gram entry by $e^{-mc}$. Since the determinant has size $\dim U_m$, the normalized functional for any fixed space $U_m$ satisfies $\mathcal F_{U_m}^{(q)}(c)=cq!\dim U_m/m^q$ and vanishes at $c=0$. Subtract $U_m=V_m,W_m$ to get (D), proving the first-order bound for the determinant functional cannot generally be replaced by $o(m^{-1})$ either.

## Classification, dependent results, and proposed action

**Verified conditional deduction / low**: the finite-dimensional identities (A)–(D), the qpsh model, and the resulting sharpness are proved directly. Printed Lemma 18.37.1, Proposition 18.37.3, and Theorem 18.37.4 are **not** counterexamples; the stated $O(m^{-1})$ remains correct. A possible *separate proposed addendum*, not a production edit, is to append this product-model sharpness immediately after Theorem 18.37.4, explicitly recording that both comparison bounds are optimal and that a projective-space jet map can be surjective. The affected statements are §§18.37.1, 18.37.3–4 and the constant-shift clause of §18.34.1.

**Unresolved analytic boundary:** the general convergence $\beta_{W_m}\rightharpoonup\mathrm{MA}_\theta(E(v))$ invoked from §18.35.5, and existence/regularity of the general partial envelope, have **not** been newly authenticated in this review. No Demailly approximation, dedicated Bergman/L²/OT/multiscale or positivity-loss argument is reopened; all prior corresponding notes remain **deferred-by-user**, not resolved or certified. The full §18.37 is not certified.

**Coverage accounting:** one newly first-proof-reviewed current-ToC section (§18.37); zero entire numbered sections certified; §18.34, §18.36, §5.37 only narrowly crosschecked. The actual 2026-11-14 production ToC remains 25 chapters / 747 numbered sections; no build, tests, CI, site publishing, source, registry, or tag modifications were made.