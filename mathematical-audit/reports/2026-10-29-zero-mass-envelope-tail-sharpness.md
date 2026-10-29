# Audit — sharp normalized tails in a zero-mass envelope limit

**Date:** 2026-10-29. **Pinned production main:** b6933b772f41b45918f7e25ed1afbbb1fd892272. **Scope:** new selected proof checks in the previously partly reviewed §17.6; not a whole-section certificate. Demailly approximation/regularization and its dedicated Bergman, L², Ohsawa–Takegoshi, multiscale and positivity-loss work is **deferred-by-user**, untouched.

**Main source and permanent anchors.** The integrated section is **docs/sections/relative-energy-and-perron-segments--singularity-envelopes-at-arbitrary-mass/index.html**, main blob **addc238e2dc806ff14a69fa8c8e5bdf46da448f2**, 194 physical HTML lines, provenance **foundations-of-pluripotential-theory**. Proposition 17.6.1 source label **1031B084**, permanent tag **DC1056C1A4A1**, line **17**, proof lines **25–128**. Normalized tail Eq. 17.6.2 source **910485A3**, tag **C6464A625C78**, lines **52–58**. Finite-obstacle volume Eq. 17.6.3 source **BCEC201E**, tag **A5C05836DEF9**, lines **112–117**, limit ordering lines **119–127**. Definition 17.6.4 source **739AB03B**, tag **0C3B4338E463**, line **131**; Theorem 17.6.5 source **402BEA9A**, tag **C6C3A19AAB0D**, lines **140–180**. Statement-only upstream comparison check: §16.25.4 source **C32431185924**, main **docs/sections/envelopes-and-model-potentials--singularity-constraints-and-relative-capacity/index.html**, blob **4207ba03590b2988456f1df4da4123e1e572c8de**, line **76**; constant-density existence §17.5.6 source **8972585EBF32**, main **docs/sections/relative-energy-and-perron-segments--variational-monge-ampere-equations/index.html**, blob **d86dcef056e4e8d03a5974027ed7cc226d35eefc**, line **102**; positive-mass model ceiling §16.22.11 source **4A1DC8C4E020**, main blob **17191d65c793e508c1785dd617ddb1dbc5f5d213**, line **229**.

## POME-ENV-ZEROMASS-TAIL-OPT-001

**Severity/status:** low / **verified conditional deduction**. The printed result is **correct**, not an unproved theorem or new defect. This is distinct from historical POME-ENV-MASS-ORDER-001, which computed only total-mass vanishing orders; we establish sharpness of the **normalized mass-distribution tail**, and optimize the proof's finite-obstacle bound.

### Exact sharpness of Eq. 17.6.2 as mass tends to zero

On \(X=\mathbb P^1\), let \(\omega=\omega_{\rm FS}=dd^c\log(1+|z|^2)\) with \(\int_X\omega=1\), \(dd^c=\frac{\mathrm i}{2\pi}\partial\bar\partial\), and \(V_\omega=0\). Define
\[
u(z)=\log\frac{|z|^2}{1+|z|^2}\le0,\qquad u(\infty)=0.
\]
Poincaré–Lelong gives \(\omega+dd^cu=[0]\), so \(\nu_1=\langle\omega_u\rangle=0\), while \(\nu_0=\omega\), \(a_0=1\). The normalized tail function in Proposition 17.6.1 is exactly
\[
r(A)=\omega(\{u<-A\})=e^{-A},\qquad A>0,
\]
since \(s=|z|^2/(1+|z|^2)\) is uniformly distributed on \([0,1]\) under \(\omega\) (direct check: \(\omega\{|z|\le R\}=R^2/(1+R^2)\)) and \(u=\log s\).

For \(w_\varepsilon=(1-\varepsilon)u\), \(0<\varepsilon<1\), the full current is
\[
\omega+dd^cw_\varepsilon=\varepsilon\omega+(1-\varepsilon)[0],
\]
and therefore \(\mu_{w_\varepsilon}=\langle\omega_{w_\varepsilon}\rangle=\varepsilon\omega\), \(m_\varepsilon=\varepsilon\downarrow0\). Yet
\[
\boxed{\frac{\mu_{w_\varepsilon}(\{w_\varepsilon<V_\omega-A\})}{m_\varepsilon}
=\exp\!\left(-\frac{A}{1-\varepsilon}\right)
\uparrow e^{-A}=r(A)\quad(\varepsilon\downarrow0).}
\]
Thus the normalized-tail bound Eq. 17.6.2 is **asymptotically attained for every fixed A even when limiting non-pluripolar mass is zero**. This checks both the exclusion of polar current mass and the necessity of normalizing by \(m_\varepsilon\). It neither repeats the old vanishing-order calculation nor invokes any approximation theorem.

### An explicit optimized finite-A volume estimate in every dimension

Use the printed proof's definitions \(\phi_\varepsilon=P_\theta[w_\varepsilon]\), \(p_{\varepsilon,A}=P_\theta(w_\varepsilon+A,V)\), and \(E_{\varepsilon,A,\delta}=\{\phi_\varepsilon>p_{\varepsilon,A}+\delta\}\), \(\delta>0\). Let \(\Omega=\int_X\omega^n\), and choose a uniform \(C_1>0\) for \(\int_X(-\chi_\varepsilon)\omega^n\) from Step 4. The printed Eq. 17.6.3 gives, for \(B>1\), uniformly in \(0<\varepsilon<1\),
\[
\operatorname{Vol}_{\omega}(E_{\varepsilon,A,\delta})
\le C_1/B+\Omega\min\{1/2,\delta/(4B)\}^{-n}r(A).
\tag{*}
\]
Fix \(\delta>0\). For \(B\ge B_0=\max(2,\delta/2)\), the minimum equals \(\delta/(4B)\), and (*) becomes \(C_1/B+\alpha B^n\), where \(\alpha=\Omega\,4^n\delta^{-n}r(A)\). For \(0<r(A)\) sufficiently small, \(B_*=(C_1/(n\alpha))^{1/(n+1)}\ge B_0\), so optimizing yields
\[
\boxed{\operatorname{Vol}_{\omega}(E_{\varepsilon,A,\delta})
\le (n+1)n^{-n/(n+1)}C_1^{n/(n+1)}
\bigl(4^n\Omega\,\delta^{-n}r(A)\bigr)^{1/(n+1)}.}
\]
If \(r(A)=0\), letting \(B\to\infty\) in (*) gives zero volume. The estimate remains **uniform in \(\varepsilon\)** without any positive lower bound on \(m_\varepsilon\). The factor \(r(A)^{1/(n+1)}\) is optimal **for balancing the two terms in the printed inequality**, not claimed to be the intrinsically sharp asymptotic for the actual envelope. In the \(\mathbb P^1\) example, \(r(A)=e^{-A}\), \(\Omega=1\), \(n=1\), so for fixed \(\delta\) and sufficiently large \(A\) the estimate becomes \(4\sqrt{C_1/\delta}\,e^{-A/2}\).

### Mathematical dependencies, precise limits, and disposition

This proof independently checks Step 2's finite sum of nonnegative non-pluripolar mixed currents and the fact that each gives the polar set zero mass. Step 3 bounds rooftop potentials between \(w_\varepsilon\) and \(\phi_\varepsilon\). Step 5 uses comparison **only at strictly positive** \(m_\varepsilon\ge\varepsilon^na_0>0\), consistent with the actual condition in Proposition 16.25.4. The constant density \(g=m_\varepsilon/\Omega\) has the correct total mass for Theorem 17.5.6; its full existence proof remains an **uncertified internal dependency**. Dividing by \(m_\varepsilon\) eliminates degeneration. Step 6's limiting proof must take \(A\to\infty\) **before** \(B\to\infty\); the order was retained and no general-net compactness assertion was introduced.

**Proposed optional correction:** add the exact \(\mathbb P^1\) sharpness model after Proposition 17.6.1, and the optimized bound as a quantitative consequence of Eq. 17.6.3 with a specified sufficiently-small-tail threshold. **Affected dependents:** Proposition 17.6.1, Theorem 17.6.5 and quantitative zero-mass singularity-ceiling applications; no original statement or proof is declared false or replaced. This is an **incremental substantive audit of already partially examined §17.6**, not a first visit or whole section certification. Prior POME-ENV-MASS-ORDER-001 remains distinct and unchanged; **25 current chapters / 747 numbered ToC sections / zero complete-section certifications**. No source, main, tag, registry, site, build, CI or formalization change.
