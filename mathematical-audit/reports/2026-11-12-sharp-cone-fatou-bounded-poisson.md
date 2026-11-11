# 2026-11-12 — Sharp cone necessity for universal bounded Poisson boundary convergence

**Finding ID:** POME-HARM-FATOU-CONE-UNIVERSAL-SHARPNESS-001  
**Severity/status:** low / **verified conditional deduction**; no false statement or missing proof in the cited original theorems is asserted.  
**Reviewed production main:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`.  
**Integrated reading edition:** \`docs/sections/classical-harmonic-analysis/index.html\`, blob \`75e982788e627af602981823a82863cbd36ee712\`.  
**Exact anchors:** Theorem 3.3.9, source \`classical-potential-theory:4ADDEE1E\`, permanent tag \`CAE5D89698DF\`, physical lines 119–139; Theorem 3.3.12, source \`classical-potential-theory:4AD4672F\`, tag \`5F363A880A\`, lines 160–185; Theorem 3.3.14, source \`classical-potential-theory:7C0C933C\`, tag \`EEE7DD56F49D\`, lines 190–212; its explicit nontangential kernel bound at lines 196–203.

## Precise new statement

Let \(d\ge2\), \(B\subset\mathbb R^d\) be the open unit ball, \(S=\partial B\) with ordinary area measure \(\sigma\), and \(\zeta\in S\). Write
\[
P(x,\eta)=\frac{1-|x|^2}{s_{d-1}|x-\eta|^d},
\qquad t(x)=1-|x| .
\]
For a sequence \(x_n\in B\) converging to \(\zeta\), the following are equivalent.

1. \(\sup_n |x_n-\zeta|/t(x_n)<\infty\) after dropping finitely many terms (i.e. the sequence eventually lies in a fixed nontangential cone).
2. For **every** bounded measurable real boundary function \(f\) having the approximate value \(a\) at \(\zeta\),
\[
\lim_{r\downarrow0}\frac{1}{\sigma(C_r(\zeta))}
 \int_{C_r(\zeta)}|f-a|\,d\sigma=0,
\]
the normalized ball Poisson extension \(u=P[f\sigma]\) satisfies \(u(x_n)\to a\).

More sharply, when condition 1 fails, one can take a *single* \(f\) with \(0\le f\le1\), approximate value \(0\) at \(\zeta\), and a subsequence \(x_{n_k}\) such that \(P[f\sigma](x_{n_k})\ge c_d>0\), although \(P[f\sigma](x)\to0\) along **every** fixed nontangential cone at \(\zeta\). Thus the aperture restriction in Theorem 3.3.14 is universally sharp even for **bounded nonnegative harmonic functions and absolutely continuous boundary measures**. It cannot be replaced by unrestricted approach under mere approximate continuity of boundary values. This does not contradict Theorem 3.2.12, which assumes genuine continuity of \(f\) at the boundary point.

## Proof: sufficiency, with the exact kernel bound

Put \(\nu=|f-a|\sigma\), a finite positive measure. Approximate value \(a\) means
\(\nu(C_r(\zeta))=o(r^{d-1})\), since \(c_dr^{d-1}\le\sigma(C_r(\zeta))\le C_dr^{d-1}\) for small \(r\). If \(x\) satisfies \(|x-\zeta|\le A\,t\), then \(|x-\eta|\ge t\) and
\[
|\eta-\zeta|\le|\eta-x|+At\le(A+1)|\eta-x|.
\]
Consequently
\[
0\le P(x,\eta)\le C_{A,d}\frac{t}{(t+|\eta-\zeta|)^d}.
\]
Fix \(\epsilon>0\). For some \(\delta>0\) and every \(0<r\le\delta\),
\(\nu(C_r)\le\epsilon r^{d-1}\). The integral on \(C_t\) is bounded by \(C\epsilon\). On \(2^{j-1}t<|\eta-\zeta|\le2^jt\le\delta\), it is at most \(C\epsilon2^{-j}\); summing gives \(C'\epsilon\). On the complement of \(C_{\delta/2}\), the kernel is at most \(Ct\delta^{-d}\), so the integral is \(o(1)\). Therefore \(P\nu(x)\to0\), and because \(P\sigma=1\),
\[
|P[f\sigma](x)-a|\le P\nu(x)\longrightarrow0.
\]
This establishes 1 \(\Rightarrow\) 2, independently for the given point \(\zeta\). No almost-everywhere quantifier is needed once approximate continuity is supplied.

## Proof: necessity, including disjoint boundary caps

Suppose the ratio in 1 is unbounded. Choose a subsequence, relabelled \(x_j\), such that
\[
t_j=1-|x_j|,\qquad \xi_j=x_j/|x_j|,\qquad
r_j=|\xi_j-\zeta|,\qquad
r_{j+1}\le r_j/4,\quad 0<t_j/r_j\le 2^{-j-4}.
\]
Such a subsequence exists: \(|x-\zeta|-t\le|\xi-\zeta|\le|x-\zeta|+t\), and the quotient \(|x-\zeta|/t\) is unbounded along a subsequence tending to \(\zeta\). Define the closed spherical caps
\[
D_j=\{\eta\in S:|\eta-\xi_j|\le t_j\},\qquad
f=\mathbf1_{\bigcup_{j\ge1}D_j}.
\]
The caps are disjoint: for \(i<j\),
\(|\xi_i-\xi_j|\ge r_i-r_j\ge3r_i/4\), while \(t_i+t_j<r_i/4\).
Their areas satisfy \(\sigma(D_j)\le C_dt_j^{d-1}\).

If \(D_j\cap C_s(\zeta)\ne\varnothing\), then \(r_j\le s+t_j\le s+r_j/16\), hence \(r_j<2s\). Choose \(J\to\infty\) with \(r_{J+1}<2s\le r_J\). Only indices \(j\ge J+1\) contribute. Geometric decay and \(t_j\le2^{-j-4}r_j\) give
\[
\frac{\int_{C_s(\zeta)}f\,d\sigma}{\sigma(C_s(\zeta))}
 \le\frac{C_d\sum_{j\ge J+1}t_j^{d-1}}{c_ds^{d-1}}
 \le C_d'2^{-J(d-1)}\longrightarrow0.
\]
Thus \(f\) has approximate boundary value \(0\) at \(\zeta\) (and \(f(\zeta)=0\)). The sufficiency estimate above shows \(P[f\sigma]\to0\) along every fixed cone.

But at \(x_j=(1-t_j)\xi_j\), every \(\eta\in D_j\) satisfies
\(|x_j-\eta|\le2t_j\), and \(1-|x_j|^2=2t_j-t_j^2\ge t_j\). Also \(\sigma(D_j)\ge c_dt_j^{d-1}\) for all sufficiently large \(j\). Hence
\[
P[f\sigma](x_j)\ge\int_{D_j}
 \frac{t_j}{s_{d-1}(2t_j)^d}\,d\sigma
 \ge\frac{c_d}{2^d s_{d-1}}>0,
\]
uniformly in \(j\). Since \(P\sigma=1\), \(0\le P[f\sigma]\le1\), so this is a counterexample **inside the bounded positive harmonic class**. It proves 2 \(\Rightarrow\) 1 by contraposition.

**Explicit reproducible sequence:** Fix \(\zeta=e_d\), set
\(\xi_j=(\sin 2^{-j},0,\ldots,0,\cos2^{-j})\),
\(t_j=2^{-j}j^{-2}\), \(x_j=(1-t_j)\xi_j\), for \(j\) sufficiently large. Then \(r_j\asymp2^{-j}\), \(t_j/r_j\asymp j^{-2}\), and the same cap construction works.

## Classification, source interface and dependencies

* **Classification:** verified conditional deduction / sharpness; **not** a counterexample to Theorem 3.3.9 or 3.3.14, nor a completed proof of all of §3.3.
* **Mathematical input:** only the ball Poisson kernel and its normalization, the spherical-cap area estimate, and elementary dyadic integration. These are checked explicitly in the cited integrated proof, but the entire classical Poisson/Dirichlet construction upstream is not certified in this report.
* **Correction proposed (not applied):** optional English remark after Theorem 3.3.14: nontangential approach is optimal for a universal theorem with only approximate boundary continuity, even among bounded positive Poisson integrals; full approach requires a stronger pointwise assumption, e.g. genuine continuity as in §3.2.12.
* **Potential dependents:** any later step using the theorem's a.e. Fatou limit as an unrestricted boundary limit. No specific printed dependent with that error has been identified; this is a scope warning, not a proven downstream bug.
* **Duplication check:** existing 2026-11-08 Poisson \(L^p\)/TV report and 2026-11-05 half-space vague-boundary uniqueness report concern different questions. Theorem 3.3.14's original cone convergence is *not* re-registered.
* **Coverage:** previously partially checked §3.3; new independent sharpness of the spatial approach hypothesis, **0 first proof-level section visits, 0 whole-section mathematical certifications**. Current main table of contents remains **25 chapters / 747 numbered sections**.
* **Excluded scope:** Demailly approximation/regularization and all dedicated Bergman, \(L^2\), Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof work remain **deferred-by-user**, not resolved or certified. No source, main, registry, permanent-tag, canonicalization, CI, build or site change.
