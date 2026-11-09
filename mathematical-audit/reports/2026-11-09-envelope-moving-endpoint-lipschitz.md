# Audit: exact Lipschitz stability of a constrained minimum under endpoint perturbations

**Finding:** \`POME-ENVELOPE-MOVING-ENDPOINT-LIPSCHITZ-001\`.  
**Date:** 2026-11-09. **Severity/status:** low / verified conditional deduction; the printed lemma remains correct. This is an independently proved supplemental consequence, not a repair or a complete verification of its dependency chain.

**Reviewed production main:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`.  
**Integrated source:** \`docs/sections/envelopes-and-model-potentials--measures-on-contact-sets--a-minimum-with-a-varying-upper-radius/index.html\`, blob \`879fd87eacb65755ae0e7a9ffc95e71d1c262d39\`. Lemma 16.18.1, source label \`foundations-of-pluripotential-theory:1E3A3A35\`, permanent tag \`93E8FFBE7FEB\`; original hypotheses at physical lines 10–24, the penalized scalar minimization at 27–42, the Schur complement at 43–49 and the distributional limit at 52–55.

## Statement and scope

Fix $z$ and $c>0$. Suppose the real function $s\mapsto H(s)=H(z,s)$ is $C^2$ on $(-\infty,B]$ and satisfies $H_s\ge0$, $H_{ss}>0$, and a lower bound as $s\to-\infty$. Define, for $b\le B$,
$$
F(s)=H(s)-cs,\qquad V_H(b)=\min_{s\le b} F(s).
$$
The minimum is well-defined, because $H(s)-cs\to+\infty$ as $s\to-\infty$. The following **endpoint-value** estimates require neither the joint Levi hypothesis of the printed lemma nor any derivatives of the endpoint function $b(z)$.

For every $b_1\le b_2\le B$,
$$
\boxed{0\le V_H(b_1)-V_H(b_2)\le c(b_2-b_1).}\tag{A}
$$
In fact $V_H$ is $C^1$ as a function of the scalar endpoint, with exact derivative
$$
\boxed{\frac{dV_H}{db}(b)=\min\{H_s(b)-c,0\}\in[-c,0].}\tag{B}
$$
If $H_1,H_2$ satisfy these same hypotheses on the common half-line $(-\infty,\max\{b_1,b_2\}]$, and
$$
|H_1(s)-H_2(s)|\le\delta\qquad(s\le\max\{b_1,b_2\}),
$$
then the exact **two-input stability estimate** is
$$
\boxed{|V_{H_1}(b_1)-V_{H_2}(b_2)|
       \le\delta+c|b_1-b_2|.}\tag{C}
$$
The coefficients $1$ and $c$ cannot be decreased uniformly. For $z$-dependent $H_i,b_i$, (A)–(C) apply at each $z$; in particular, taking suprema gives the corresponding $C^0$ or $L^\infty$ error bound whenever the displayed uniform hypotheses hold. A distributional complex-Hessian estimate still needs the separate **joint Levi condition and smooth-background assumptions** of printed Lemma 16.18.1. The scalar estimate is not a substitute for those conditions.

## Complete elementary proof

Nested feasible sets give $V_H(b_1)\ge V_H(b_2)$. For any competitor $s\le b_2$, set $t=\min\{s,b_1\}$. If $s\le b_1$, then $F(t)=F(s)$. If $s>b_1$, the sole inequality $H_s\ge0$ yields
$$
F(t)-F(s)
 =F(b_1)-F(s)
 =\int_{b_1}^{s}(c-H_s(\sigma))\,d\sigma
 \le c(s-b_1)\le c(b_2-b_1).
$$
Thus $V_H(b_1)\le F(t)\le F(s)+c(b_2-b_1)$, and infimizing over $s\le b_2$ proves (A). This clipping argument works even for nonsmooth endpoint functions $b_i(z)$, as long as the minima are pointwise meaningful.

To derive (B), $F'(s)=H_s(s)-c$ is strictly increasing. Because $H_s$ is nonnegative and increasing, $\ell=\lim_{s\to-\infty}H_s(s)\ge0$ exists. If $\ell>0$, integrating $H_s\ge\ell$ from $s$ to a fixed reference point forces $H(s)\to-\infty$, contradicting the lower bound. Hence $\ell=0$ and $F'$ tends to $-c$ at the left end. If $H_s(b)<c$, $F$ decreases all the way to $b$, so the unique minimum is attained at $b$ and $V_H'(b)=H_s(b)-c$. If $H_s(b)>c$, there is a unique interior solution $s_0<b$ to $H_s(s_0)=c$; it remains the minimizer as $b$ moves locally, so $V_H'(b)=0$. When $H_s(b)=c$, both one-sided derivatives coincide and vanish. Formula (B) follows, including the transition point.

At fixed $b$, a uniform inequality $|H_1-H_2|\le\delta$ changes the infimum by at most $\delta$: apply the pointwise inequality to all admissible $s$ and take infima in both directions. Combine this bound with (A) for one of the $H_i$ to prove (C).

## Sharpness and necessity of the slope hypothesis

1. **The coefficient of $\delta$ is exactly one.** With $H_2=H_1+\delta$ and a common endpoint, the minimum changes by exactly $\delta$.
2. **The endpoint coefficient $c$ is sharp.** Take $H(s)=e^s$. For $b<\log c$, the minimum is on the boundary, so $V_H(b)=e^b-cb$. For any fixed $h>0$ with $b+h<\log c$,
   $$
   \frac{V_H(b)-V_H(b+h)}{h}
     =c-e^b\frac{e^h-1}{h}\longrightarrow c
       \quad (b\to-\infty).
   $$
   Thus no smaller universal endpoint coefficient is possible.
3. **Nonnegative $H_s$ is essential.** If it is dropped, $H(s)=e^s-Ms$ ($M>0$) has strictly positive second derivative and is lower bounded at $-\infty$, but at deep negative endpoints its constrained minimum is $e^b-(M+c)b$. Its endpoint slope tends to $-(M+c)$, violating the $c$-Lipschitz conclusion. This example **does not contradict the original lemma**, because it violates its explicitly printed $H_s\ge0$ assumption.

The previously recorded \`POME-ENVELOPE-VARYING-RADIUS-SHARP-BARRIER-001\` also used $H=e^s$, **for a different assertion**: the optimal $\varepsilon\log(1/\varepsilon)$ penalty convergence and the optimal curvature-loss coefficient $cC_b$. Neither of those findings is repeated here or relabeled as new. The new result concerns exact sensitivity of the *minimum value* to $b$ and to $H$.

## Classification, corrections, dependencies, and coverage

**Original statement:** Lemma 16.18.1 correct. **Status:** verified conditional deduction, severity low; neither confirmed error nor proof gap. A suitable optional **Remark** after the lemma would record (A)–(C) and their sharpness. No source or canonical statement edits are authorized here, and source labels, permanent tags, and historical attribution must stay intact.

**Potential dependents:** §§16.19–16.20 may use the bound if the exact common-domain and $H_s\ge0$ assumptions hold. No assertion is made that their full joint-Hessian, envelope, or PDE arguments have been certified. The present proof is independent of Kiselman's theorem (cited by the original Hessian proof), and it does not inspect or resume any Demailly approximation, dedicated Bergman, $L^2$, Ohsawa–Takegoshi, multiscale-atlas, or positivity-loss proof-completion task; those remain \`deferred-by-user\`.

**Coverage:** Already-sampled §16.18 received one selected new exact mathematical deduction and its independent proof. Zero newly visited numbered sections; zero completely certified sections (project baseline 25 chapters / 747 sections). No tests, build, CI, formal verification, website publication, or production-main changes performed.
