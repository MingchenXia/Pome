# Total-variation convergence of smooth data does not force uniform convergence of the exponential variational Monge–Ampère solutions

**Finding ID:** POME-VARMA-TV-DATA-NONUNIFORM-001  
**Date:** 2026-11-17  
**Classification:** low / **verified conditional deduction** (sharp boundary of a possible strengthening; **no false printed theorem and no new confirmed proof gap**).  
**Reviewed production main:** b6933b772f41b45918f7e25ed1afbbb1fd892272.  
**Integrated reading edition:** docs/sections/relative-energy-and-perron-segments--variational-monge-ampere-equations/index.html, blob d86dcef056e4e8d03a5974027ed7cc226d35eefc.  
**Permanent/source anchors:** Proposition 17.5.7, source foundations-of-pluripotential-theory:B027C133, permanent 5BDA01022188, physical lines 125–143; Theorem 17.5.13, source foundations-of-pluripotential-theory:0B32BA83, permanent 109ED281DA22, physical lines 241–260. Definitions and variational setup, lines 7–10, 147–154; related bounded-density Corollary 17.5.26, lines 503–520, read for hypothesis contrast.  
**Nature of review:** actual printed statements and relevant comparison/existence proof passages; not a complete certification of §17.5 or of upstream comparison, capacity, or variational compactness results.

## Claim

Fix any $\lambda>0$. On the compact Kähler curve $(X,\omega)=(\mathbb P^1,\omega_{\mathrm{FS}})$, normalized by $\int_X\omega=1$ and with $\phi=0$, there are **smooth strictly $\omega$-psh potentials** $u_k$ with $\sup_Xu_k=0$ and **smooth strictly positive** measures $\nu_k$ such that

1. $\omega+dd^cu_k=e^{\lambda u_k}\nu_k$ and hence $u_k$ is the unique solution of the printed Theorem 17.5.13 for datum $\nu_k$;
2. $\|\nu_k-\omega\|_{\mathrm{TV}}\to0$ (full signed-measure variation norm), with an explicit $O(k^{-1})$ bound;
3. $u_k\to0$ in $L^1(X,\omega)$ and locally uniformly on $X\setminus\{p\}$, but $\|u_k\|_{L^\infty(X)}\to2$;
4. the densities $d\nu_k/d\omega$ have a uniform positive lower bound for $k\ge2$, though no uniform upper bound.

Thus **even total-variation convergence of smooth, everywhere positive input measures does not imply uniform convergence of the corresponding exponential variational solutions**. The original uniqueness/existence statement is correct. This observation does not contradict estimates requiring a uniform $L^p$, $p>1$, bound, or two-sided multiplicative comparison of the data.

## Explicit construction and proof

Write $z$ for an affine coordinate on $\mathbb P^1$, with $p=\{z=0\}$, and use Pome's convention
$$dd^c=\frac{\mathrm i}{2\pi}\partial\bar\partial,\qquad
\omega=dd^c\log(1+|z|^2).$$
The global smooth function
$$t=\frac{|z|^2}{1+|z|^2}$$
takes values in $[0,1]$ and equals $1$ at infinity. For $k\ge2$ set $\epsilon_k=1/k$, $r_k=e^{-k}$, and
$$u_k=\epsilon_k\log\frac{t+r_k^2}{1+r_k^2}.$$
These functions are smooth everywhere, nonpositive, with $\sup_Xu_k=0$. At $p$,
$$u_k(p)=\frac1k\log\frac{e^{-2k}}{1+e^{-2k}}
=-2-\frac1k\log(1+e^{-2k}),$$
so $\|u_k\|_\infty\to2$, and $0\le-u_k\le3$ for every $k\ge2$.

For any $r>0$ put
$$T_r=\omega+dd^c\log(t+r^2).$$
On the $z$ chart,
$$T_r=dd^c\log\bigl(r^2+(1+r^2)|z|^2\bigr)
=\frac{r^2(1+r^2)}{\pi\bigl(r^2+(1+r^2)|z|^2\bigr)^2}\,dx\,dy.$$
On the chart $w=1/z$, the same current is
$$T_r=dd^c\log\bigl(1+r^2+r^2|w|^2\bigr).$$
Thus $T_r$ is a globally smooth strictly positive form. Stokes gives $\int_XT_r=\int_X\omega=1$. In particular
$$\mu_k:=\omega+dd^c u_k=(1-\epsilon_k)\omega+\epsilon_kT_{r_k}$$
is a smooth positive probability measure. Define
$$\nu_k=e^{-\lambda u_k}\mu_k.$$
It is smooth and strictly positive, and by construction
$$\mu_k=e^{\lambda u_k}\nu_k.$$
Theorem 17.5.13 (conditional on its printed upstream existence/uniqueness inputs) identifies $u_k$ as its unique solution; no attempt is made to reprove those general upstream theorems.

Here is an explicit variation estimate. The pushforward $t_*\omega$ is Lebesgue measure on $[0,1]$, as follows from the polar-coordinate expression $\omega=\pi^{-1}(1+|z|^2)^{-2}dx\,dy$. Hence
$$\int_X|u_k|\,\omega
=\frac1k\int_0^1\log\frac{1+r_k^2}{s+r_k^2}\,ds
\le\frac1k\int_0^1\log\frac2s\,ds
=\frac{1+\log2}{k}.$$
As $T_{r_k}$ is a probability measure and $|u_k|\le3$,
$$\int_X|u_k|\,d\mu_k
\le\frac{1+\log2+3}{k}
=\frac{4+\log2}{k}.$$
Furthermore $\|\mu_k-\omega\|_{\mathrm{TV}}
=\epsilon_k\|T_{r_k}-\omega\|_{\mathrm{TV}}\le2/k$.
For $-3\le u_k\le0$, the mean-value theorem yields
$$0\le e^{-\lambda u_k}-1
\le\lambda e^{3\lambda}|u_k|.$$
Since $\nu_k-\mu_k=(e^{-\lambda u_k}-1)\mu_k$,
$$\boxed{\displaystyle
\|\nu_k-\omega\|_{\mathrm{TV}}
\le\frac{2+\lambda e^{3\lambda}(4+\log2)}{k}
\longrightarrow0.}$$
The same integral estimate proves $u_k\to0$ in $L^1(\omega)$; on every compact subset of $X\setminus\{p\}$ one has $t\ge c>0$ and therefore $u_k\to0$ uniformly.

Finally, $e^{-\lambda u_k}\ge1$ and $\mu_k\ge(1-1/k)\omega$, so
$$\frac{d\nu_k}{d\omega}\ge1-\frac1k\ge\frac12.$$
However the local density ratio at $p$ is
$$\left.\frac{d\nu_k}{d\omega}\right|_p
=e^{-\lambda u_k(p)}
\left(1-\frac1k+\frac1k\frac{1+r_k^2}{r_k^2}\right)
\longrightarrow+\infty.$$
Thus uniform upper $L^\infty$ control of the densities is absent, exactly where a stronger potential estimate would require additional assumptions. In fact the density ratio grows exponentially.

## Scope, consequences, and classification

- **Verified mathematical content:** all explicit computations and the signed-measure variation bound above; the PDE solution identification is conditional on Theorem 17.5.13 as printed, rather than a newly certified global existence theorem.
- **Not a false theorem:** Theorem 17.5.13 asserts existence and uniqueness for each non-pluripolar datum, not TV-to-uniform continuous dependence. Proposition 17.5.7 assumes an ordered exponential density comparison; it is not contradicted.
- **Affected dependents:** any proposed extension of the §17.5 data-to-solution map from multiplicative or $L^p$ control to bare input total variation, even when all data are smooth, strictly positive and uniformly bounded below.
- **Proposed correction:** none to the printed statements. If a stability corollary is added, explicitly retain a uniform quantitative upper-density/capacity or multiplicative hypothesis. The counterexample is available as an optional caution next to §17.5.13 or §17.5.26; no body patch is made here.
- **Unresolved inputs:** underlying comparison/domination and full general variational existence proof, including Lemma 17.5.14 and compactness, were not transitively certified; they remain separately audited. The construction itself uses only elementary smooth forms on $\mathbb P^1$.
- **User deferral:** Demailly approximation/regularization, and the dedicated Bergman, $L^2$, Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof-completion work remain **deferred-by-user** and were not reviewed here.

No project build, test suite, CI, canonicalization/registry mutation, source edit or website publication was performed.
