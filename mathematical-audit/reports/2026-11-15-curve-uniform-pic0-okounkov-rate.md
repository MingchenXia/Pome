# Sharp uniform Picard-zero twisted Okounkov convergence on curves

**Finding:** \`POME-OKO-CURVE-UNIFORM-PIC0-SHARP-RATE-001\`  
**Date:** 2026-11-15  
**Classification:** **low / verified conditional deduction**; the printed Proposition 19.4.12 is **correct**, not a false theorem or repaired proof. This is a new *uniform-in-varying-flat-twist, exact quantitative curve specialization* of the printed fixed-twist Hausdorff convergence, not a claim about arbitrary-dimensional varieties.

## Reviewed reading-edition provenance

- Production \`main\` commit: \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`.
- Integrated file: \`docs/sections/the-theory-of-okounkov-bodies--algebraic-partial-okounkov-bodies/index.html\`, blob \`c661e264cab0995a2a344453039940028feff8e0\`.
- Definition **19.4.5**, original source label \`sgpt:CBA44DDF\`, permanent tag \`51F245B40203\`, physical lines **48–54**: the convex hull of normalized flag-valuations of sections of \(T\otimes L^k\).
- Proposition **19.4.12**, source \`sgpt:ADB3B184\`, permanent tag \`1ED4AF0D9A23\`, physical lines **174–179**, proof **181–209**: for each *fixed* line bundle \(T\) on a projective variety with \(L\) big, \(\Delta_{k,T}(L)\to\Delta_\nu(L)\) in Hausdorff distance. The proof injects sections by fixed auxiliary sections of \(L^{k_0}\otimes T^{\pm1}\).
- Theorem **19.2.5** (internal reference, not independently reproved in this increment) supplies the general asymptotic Okounkov-body convergence.

## New exact statement

Let \(X\) be a **smooth connected projective curve** of genus \(g\ge0\), \(p\in X\), and let \(L\) be a line bundle of integer degree \(d>0\). Let \(\nu=\operatorname{ord}_p\) be the flag valuation. For any integer \(k>0\) satisfying \(kd\ge2g\), and **every varying flat twist** \(T\in\operatorname{Pic}^0(X)\), the convex body \(\Delta_{k,T}(L)\) is defined and

\[
\Delta_\nu(L)=[0,d],\qquad
\Delta_{k,T}(L)=[0,m_k(T)/k],
\quad kd-g\le m_k(T)\le kd,
\]
and consequently
\[
0\le d_{\mathrm{Haus}}\bigl(\Delta_{k,T}(L),\Delta_\nu(L)\bigr)
=d-\frac{m_k(T)}{k}\le\frac{g}{k}.
\tag{1}
\]

For **every** such \(k\) when \(g\ge1\), there are degree-zero twists \(T\) attaining the upper bound, so in fact

\[
\boxed{\ \sup_{T\in\operatorname{Pic}^0(X)}
d_{\mathrm{Haus}}\bigl(\Delta_{k,T}(L),\Delta_\nu(L)\bigr)
=\frac{g}{k}\ }\quad(kd\ge2g).
\tag{2}
\]

When \(g=0\), the distance is identically zero. The order \(1/k\) is attained **for one fixed nontrivial twist for every \(k\ge2\)** on an elliptic curve (take \(L=\mathcal O_E(dp)\), \(T\ne\mathcal O_E\), \(kd\ge2\)). Thus it cannot be improved to \(o(1/k)\) even for a fixed twist in the full class of positive-degree curve examples.

## Complete proof of (1)

Set \(F=L^k\otimes T\), so \(\deg F=kd\), irrespective of \(T\in\operatorname{Pic}^0(X)\). By Serre duality, \(H^1(X,F(-p))=0\) because
\[
\deg(K_X\otimes F^{-1}(p))=2g-1-kd<0
\]
under \(kd\ge2g\). In the exact evaluation sequence
\(0\to F(-p)\to F\to F|_p\to0\), the evaluation on global sections is therefore surjective. Hence \(F\) has a section nonvanishing at \(p\), so \(0\) is among the possible orders of vanishing.

For the opposite endpoint consider the degree-\(g\) line bundle
\(G=F(-(kd-g)p)\). Riemann–Roch says
\[
h^0(X,G)-h^0(X,K_X\otimes G^{-1})=\deg G+1-g=1,
\]
so \(h^0(X,G)\ge1\). A nonzero section of \(G\) gives a nonzero section of \(F\) vanishing at least \(kd-g\) times at \(p\). Any nonzero section of \(F\) has zero divisor of degree \(kd\), so its vanishing at \(p\) is at most \(kd\). The finite set of valuations consequently has minimum \(0\) and maximum \(m_k(T)\in[kd-g,kd]\). Its convex hull, divided by \(k\), is exactly \([0,m_k(T)/k]\), not merely a subset of that interval.

For the untwisted \(T=\mathcal O_X\), the same inclusions imply \(\Delta_k(L)\to[0,d]\). By the printed Theorem 19.2.5 / Definition 19.4.8 this identifies \(\Delta_\nu(L)\) with \([0,d]\) (or use directly the curve semigroup and its asymptotic hull). Equation (1) follows from the exact Hausdorff distance of two nested closed intervals.

## Sharpness of the genus coefficient

Assume \(g\ge1\). The Abel map
\(\operatorname{Sym}^{g-1}(X)\to\operatorname{Pic}^{g-1}(X)\)
has image \(W_{g-1}\), exactly the locus of degree-\(g-1\) bundles with a nonzero section. Since the source has complex dimension \(g-1\), while \(\operatorname{Pic}^{g-1}(X)\) has dimension \(g\), \(W_{g-1}\) is proper. As \(T\) ranges over \(\operatorname{Pic}^0(X)\), the bundle
\[
F(-(kd-g+1)p)
= L^k\otimes T\otimes\mathcal O_X(-(kd-g+1)p)
\]
ranges bijectively over all of \(\operatorname{Pic}^{g-1}(X)\). Choose \(T\) whose displayed bundle is outside \(W_{g-1}\), so there is no section vanishing at least \(kd-g+1\) times at \(p\). Combined with the universal lower bound, this yields \(m_k(T)=kd-g\), proving (2). There is no need to choose the same \(T\) for all \(k\).

For a **fixed-twist** sharpness example, let \(X=E\) be an elliptic curve, \(p\in E\), \(L=\mathcal O_E(dp)\) for \(d\ge1\), and \(T\) any fixed nontrivial degree-zero line bundle. For \(kd\ge2\), the minimum vanishing is zero as above. Since \(F(-kdp)=T\) has no nonzero section, \(m_k(T)<kd\). Conversely \(F(-(kd-1)p)=T(p)\) has degree one, hence has a section by Riemann–Roch. Therefore \(m_k(T)=kd-1\) and the distance is **exactly \(1/k\)** for every such \(k\).

If \(g=0\), then \(X\simeq\mathbb P^1\), \(\operatorname{Pic}^0(X)=0\), and \(\mathcal O_{\mathbb P^1}(kd)\) has sections with all vanishing orders \(0,\dots,kd\) at \(p\); the distance is zero.

## Scope contrast and dependencies

This does **not** extend to completely unrestricted moving twists. If \(T_k=L^{-k}\) (whose degree tends to \(-\infty\)), then \(L^k\otimes T_k\simeq\mathcal O_X\), so \(\Delta_{k,T_k}(L)=\{0\}\), at positive Hausdorff distance \(d\) from \([0,d]\). The restriction \(T\in\operatorname{Pic}^0(X)\) matters.

The argument uses classical **Riemann–Roch and Serre duality for smooth curves** and the standard dimension / Abel-map description of \(W_{g-1}\). They are explicitly identified mathematical inputs here rather than falsely certified as part of this narrow audit. The curve calculations themselves are complete conditional on those inputs. No Demailly approximation, Bergman construction, weighted \(L^2\), Ohsawa–Takegoshi, multiscale gluing or positivity-loss proof is used or opened. Proposition 19.4.12's general proof has not been certified by this calculation, and prior separate §19.4 proof-gap and external-dependency IDs are unchanged.

## Recommendation, dependents and status

**No correction to the original Proposition 19.4.12 is required.** The useful proposed addition is an optional immediately following *curve-only remark* asserting the exact uniform bound and its sharpness, with the Picard-zero restriction and genus convention explicitly displayed. Potential readers/dependents: any use of finite-level Okounkov bodies of **varying flat twists** on a curve, including §19.4.12 and §19.9 curve specializations; no general-dimensional uniformity is inferred.

**Coverage:** actual current main ToC 25 chapters / 747 numbered sections. Newly checked selected proof/statement positions in previously partially audited **§19.4**, and narrow §19.2.5 context; **0 newly first-visited numbered sections**, **0 entire-section certifications**. No project tests, build, CI, publication, or mathematical-main edits were made.
