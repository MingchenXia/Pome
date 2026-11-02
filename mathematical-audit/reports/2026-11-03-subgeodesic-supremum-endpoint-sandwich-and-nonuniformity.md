# Pointwise supremum subgeodesics: a dominated endpoint proof and the absence of a family-uniform modulus

**Finding ID:** POME-GEO-SUBGEO-ENDPOINT-SANDWICH-001  
**Date:** 2026-11-03 (Asia/Shanghai)  
**Reviewed production main:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`  
**Severity/status:** low / **verified conditional deduction** (an independent proof and a sharpness example; **not** a false printed theorem, proof-gap certification, or applied repair).  
**Scope:** new selected proof-level inspection of the *early* subgeodesic material in §17.10, especially Proposition 17.10.13 and its endpoint proof. The much later radial-energy results of §17.10 are a separate, previously audited subject.

## Exact integrated anchors

- \`docs/sections/geodesic-rays-in-the-space-of-potentials/index.html\`, main blob \`52bf9e459a0dfb1c8afe79556db037450be06bb3\`.
- Proposition **17.10.7**: original source \`sgpt:DBC4F9ED\`, permanent \`1880C1FBD88F\`, physical lines **88–139**. Its convexity and the psh lower envelope \(\inf_{0<t<1}\varphi_t\) are used as printed.
- Corollary **17.10.9**: \`sgpt:B35F3B4F\`, permanent \`C645EE3517E1\`, lines **144–170**; its endpoint equality is *quasi-everywhere*, not everywhere.
- Proposition **17.10.13**: \`sgpt:BBFDD373\`, permanent \`5ECD747A7B0B\`, lines **194–266**. Choquet countability and the equality (17.10.14) are in lines **224–257**; compactness of normalized psh functions is invoked in lines **259–265**. The exact equality (17.10.14) has source \`sgpt:5593AC43\`, permanent \`BA313A9B1A1F\`.
- Standing assumptions: \(X\) compact, connected, Kähler; \(\theta\) smooth closed and big; all families are of genuine \(\theta\)-psh functions and uniformly bounded **above** at both endpoints. No convergence of arbitrary directed nets is asserted.

## A direct \(L^1\)-endpoint proof that avoids compactness

Write \(u_t=(\sup_i u_t^i)^*\) and \(u_j=(\sup_i u_j^i)^*\) for \(j=0,1\), using exactly the envelopes of Proposition 17.10.13. As established in its lines 203–236, their interior complexification is \(p_1^*\theta\)-psh and Choquet's lemma permits a **countable** subsystem representing the interior envelope and both endpoints simultaneously. Denote this subsystem by \(I'\).

1. The pointwise convexity of each \(t\mapsto u_t^i(x)\) and Corollary 17.10.9 yield \(u_t^i(x)\to u_0^i(x)\) as \(t\downarrow0\) outside a pluripolar set depending on \(i\). Because \(I'\) is countable, the union of exceptional sets remains pluripolar. At every remaining point where the pointwise envelope of the countable endpoint family equals its upper regularization (outside another pluripolar set), the inequalities
   \[
     u_t^i\le u_t\le(1-t)u_0+t u_1
   \]
   give
   \[
      u_0=\sup_{i\in I'}u_0^i
      \le \liminf_{t\downarrow0}u_t
      \le \limsup_{t\downarrow0}u_t
      \le u_0 .
   \]
   Therefore \(u_t\to u_0\) almost everywhere. This uses the precise quasi-everywhere qualification; it does **not** upgrade individual endpoint limits to everywhere convergence.
2. Fix just one \(i_0\in I'\). Proposition 17.10.7 ensures
   \[
     w:=\inf_{0<t<1}u_t^{i_0}\in\mathrm{PSH}(X,\theta)
   \]
   and \(w\le u_0^{i_0}\). Thus \(w\le u_t\) for every \(t\), and \(w\le u_0\). The upper bound
   \[
      u_t\le(1-t)u_0+t u_1\le W:=\max\{u_0,u_1\}
   \]
   holds pointwise. Both \(w\) and \(W\) are integrable on compact \(X\), and
   \[
      |u_t-u_0|\le W-w\quad\text{almost everywhere for all }0<t<1.
   \]
   Dominated convergence then proves
   \[
      \boxed{\ \|u_t-u_0\|_{L^1(X)}\longrightarrow0\quad(t\downarrow0).\ }
   \]
   The right endpoint is symmetric. This argument does **not** use the relative \(L^1\)-compactness step at lines 259–265 or infer sequential compactness for an arbitrary directed family.

This is an alternative proof of a **correct** printed proposition. It relies on the stated Choquet and quasi-everywhere endpoint results, which are not re-certified here; it is not an unconditional replacement of their proof chains.

## No common endpoint modulus from common endpoints and common height bounds

Take any connected compact Kähler \(X\), set \(\theta=\omega>0\), and normalize a smooth reference volume \(dV\) by \(\int_XdV=1\). Let \(0<\varepsilon<1\) and define the scalar convex function
\[
 f_\varepsilon(t)=
 \begin{cases}
  -t/\varepsilon,&0\le t\le\varepsilon,\\
  -(1-t)/(1-\varepsilon),&\varepsilon\le t\le1.
 \end{cases}
\]
Its slope jumps upwards from \(-1/\varepsilon\) to \(1/(1-\varepsilon)\). Hence \(f_\varepsilon(\operatorname{Re}z)\) is subharmonic on the strip (distributionally its Laplacian is a positive measure on the vertical line \(\operatorname{Re}z=\varepsilon\)). The spatially constant potentials
\[
 \varphi_t^\varepsilon(x)=f_\varepsilon(t)
\]
are thus subgeodesics in the **exact** sense of Definition 17.10.2, with
\[
 \varphi^\varepsilon_0=\varphi^\varepsilon_1=0,\qquad
 -1\le\varphi^\varepsilon_t\le0,\qquad
 \|\varphi^\varepsilon_\varepsilon-\varphi^\varepsilon_0\|_{L^1(dV)}=1.
\]
For each fixed \(\varepsilon\), the endpoints are attained continuously, as the printed statement requires. But as \(\varepsilon\downarrow0\), the distance in time to an endpoint tends to zero while the \(L^1\) gap remains one. Consequently **there is no uniform modulus \(m(t)\to0\)** valid for all such subgeodesics based solely on common endpoints, common bounds \([-1,0]\), and spatial psh positivity. This also applies to a proposed universal modulus for the envelope construction of Proposition 17.10.13, since singleton families are allowed. Additional *uniform time-slope* control is required for such a quantitative claim. The example is about arbitrary subgeodesics, **not** about canonical Perron geodesics, which can have stronger properties.

## Classification and impact

- **Verified conditional deduction:** dominated-sandwich endpoint proof; it supplies an independent internal route once the printed Choquet and quasi-everywhere endpoint inputs are granted.
- **Verified sharpness counterexample:** no family-uniform endpoint \(L^1\) modulus under only the hypotheses above.
- **Not a confirmed error or proof gap:** Proposition 17.10.13's existing compactness proof is not contradicted; the upper-semicontinuous regularization and countability cannot silently be dropped.
- **Affected dependents:** only possible *quantitative* strengthening of the endpoint assertion of Proposition 17.10.13 or arbitrary-subgeodesic claims that try to infer a rate. Lemma 17.10.22's qualitative Perron endpoint result is unchanged.
- **Suggested optional change:** add the short dominated-sandwich argument after equation (17.10.14), and, if desired, a remark separating qualitative endpoint \(L^1\) convergence from uniform modulus. Do **not** alter statements, source bodies, labels, canonicalization, or the live reading edition in this audit branch.
- **Audit boundaries:** no Demailly approximation/regularization, dedicated Bergman, weighted \(L^2\), Ohsawa–Takegoshi, multiscale-atlas or positivity-loss argument was examined. No tests, build, CI, formalization, publication or complete mathematical-section certification performed. Existing unresolved/deferred findings retain their statuses.
