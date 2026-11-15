# Optimized Bedford–Taylor energy-to-capacity domination and sharp dimension-one exponent

**Stable finding:** \`POME-BT-ENERGY-CAPACITY-OPTIMAL-EXPONENT-001\`. **Date:** 2026-11-15. **Severity/status:** low / **verified conditional deduction**. The printed statements are correct; this is an additional estimate and a sharpness model, **not** a confirmed error or repair.

**Reviewed production main:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`.

**Exact integrated reading edition:** \`docs/sections/bedford-taylor-products-and-local-capacity--local-energy-moments/index.html\`; main blob \`e619f7aa95f80ce11aa676193b054db3180e59d4\`. The new mathematical inputs are **Lemma 7.11.19** (physical lines 386–426), especially **Eq. 7.11.21** (lines 394–398) and its proof (roughly 402–426); **Proposition 7.11.22** (lines 428–486) is compared for scope only. Definition 7.11.1 (lines 14 onward) supplies \(\mathcal E_0(B)\).

**Source labels/permanent reader tags:** Lemma 7.11.19 \`foundations-of-pluripotential-theory:2F603F4B\` / \`546063653198\`; Equation 7.11.20 \`:0E2CD2DD\` / \`B1ADA2B95634\`; Equation **7.11.21** \`:2CDB386B\` / \`92D8C50415C8\`; Proposition 7.11.22 \`:871210E1\` / \`1036F9F7DDDA\`. The existing capacity convention is Definition 7.4.2, \`:AF32B1A0\` / \`E9E7C75396D2\`. All source-label abbreviations in this paragraph have the prefix \`foundations-of-pluripotential-theory\`.

## 1. Optimized consequence of the printed estimate

Let \(B\subset\mathbb C^n\) be a ball, \(n\ge1\), \(p\ge1\), \(\varphi\in\mathcal E_0(B)\), and put
\[
 \mu_\varphi=(dd^c\varphi)^n,\qquad
 e=e_p(\varphi)=\int_B(-\varphi)^p\,d\mu_\varphi.
\]
For a Borel set \(E\subset B\), let \(C=\operatorname{Cap}_B(E)\), with the capacity convention of Pome. The printed Eq. 7.11.21 gives **for every** \(T>0\)
\[
 \mu_\varphi(E)\le C T^n+eT^{-p}.                                      \tag{1}
\]
For \(0<C<\infty\) and \(0<e<\infty\), the right-hand side has derivative \(nCT^{n-1}-peT^{-p-1}\); its unique minimizer is
\[
 T_*=\left(\frac{pe}{nC}\right)^{1/(n+p)}.
\]
Substitution in (1) yields
\[
 \boxed{\displaystyle
 \mu_\varphi(E)\le
 K_{n,p}\, e_p(\varphi)^{\,n/(n+p)}
                 \operatorname{Cap}_B(E)^{\,p/(n+p)},\qquad
 K_{n,p}=\frac{n+p}{n^{\,n/(n+p)}p^{\,p/(n+p)}}.}                     \tag{2}
\]
The two terms at \(T_*\) have ratio \(p:n\), as required by the derivative equation. If \(C=0\), send \(T\to\infty\) in (1) to obtain \(\mu_\varphi(E)=0\). If \(e=0\), send \(T\downarrow0\) when \(C<\infty\) to obtain the same conclusion. When \(C=\infty\), (2) is interpreted as a vacuous extended-valued upper bound; the useful assertion is for finite-capacity sets. All quantities \(e_p(\varphi)\) are finite in the stated bounded \(\mathcal E_0\) class.

Thus a family in \(\mathcal E_0(B)\) with \(\sup_\varphi e_p(\varphi)\le E_p<\infty\) has a **uniform quantitative capacity modulus**
\[
 \sup_\varphi\mu_\varphi(A)\le
 K_{n,p} E_p^{n/(n+p)}\operatorname{Cap}_B(A)^{p/(n+p)}
\]
for every finite-capacity Borel set \(A\). In particular these measures uniformly disregard capacity-null sets. This implication uses only the **already printed** truncation estimate; it does not establish its upstream Bedford–Taylor comparison and locality theorems.

The exponent in (2) should not be confused with **the different exponent \(n+p\)** in the *sublevel capacity* inequality of Proposition 7.11.22(1): the left sides are respectively \(\mu_\varphi(E)\) for an arbitrary \(E\) and \(\operatorname{Cap}_B(\{\varphi<-T\})\). There is no substitution of one conclusion for the other.

## 2. Exact radial model: the exponent is optimal when \(n=1\)

Fix \(p\ge1\) and \(\beta>p/(p+1)\). Choose
\[
 0<\alpha<\frac1{p+1},\qquad \alpha>1-\beta.
\]
Such an \(\alpha\) exists because \(\beta>p/(p+1)\). On the unit disc \(D\subset\mathbb C\), set
\[
 t=\log(1/|z|),\qquad g(t)=(1+t)^\alpha-1,\qquad
 u(z)=-g(t)=1-(1+\log(1/|z|))^\alpha
\]
on \(0<|z|<1\), and define \(u(0)=-\infty\). Since
\[
 g'(t)=\alpha(1+t)^{\alpha-1}>0,\qquad
 g''(t)=\alpha(\alpha-1)(1+t)^{\alpha-2}<0,
\]
the function \(u\) is subharmonic: for \(r=|z|\), \(r u_r=g'(t)\) and
\(\Delta u=-g''(t)/r^2>0\). It tends to \(0\) on \(\partial D\).
For \(M>0\), let
\[
 u_M=\max\{u,-M\},\qquad
 t_M=(1+M)^{1/\alpha}-1,
\]
so \(u_M\equiv-M\) on \(|z|\le e^{-t_M}\). This is a continuous bounded subharmonic function on \(D\), nonpositive with zero boundary values; the mass computation below makes \(u_M\in\mathcal E_0(D)\).

Pome's normalization \(dd^c=(i/2\pi)\partial\bar\partial\) gives, on the smooth radial part, \(dd^c u=(\Delta u/4\pi)\,dx\,dy\). Hence angular integration shows that in the logarithmic radial coordinate \(t\in(0,t_M)\) the measure \(dd^c u_M\) has mass density
\[
  -\tfrac12 g''(t)\,dt;
\]
the positive jump of the outward radial derivative at \(|z|=e^{-t_M}\) gives a **circle measure of total mass** \(g'(t_M)/2\). There is no atom at the origin, where \(u_M\) is constant. Consequently, for \(0<t<t_M\),
\[
 (dd^c u_M)(\overline D_{e^{-t}})
   =\frac{g'(t)}2
   =\frac{\alpha}{2}(1+t)^{\alpha-1},\qquad
 (dd^c u_M)(D)=\frac{g'(0)}2=\frac\alpha2.                        \tag{3}
\]
The energy has the *exact* expression
\[
 e_p(u_M)=\frac12\int_0^{t_M} g(s)^p[-g''(s)]\,ds
           +\frac12 M^p g'(t_M).                                \tag{4}
\]
At infinity the integrand in (4) is \(O((1+s)^{\alpha(p+1)-2})\), integrable because \(\alpha(p+1)<1\). The endpoint term satisfies
\[
 0\le M^pg'(t_M)\le
 \alpha(1+t_M)^{\alpha(p+1)-1}\le\alpha
\]
using \(M=g(t_M)\le(1+t_M)^\alpha\). Thus
\[
 \sup_{M>0}e_p(u_M)<\infty,\qquad
 \sup_{M>0}(dd^c u_M)(D)=\frac\alpha2.                            \tag{5}
\]
The uniformity in (5) is crucial: *each* \(u_M\) is bounded and belongs to the exact class in the printed lemma; no infinite-energy or unbounded-potential limit is being inserted into the theorem.

The exact unit-disc relative Bedford–Taylor capacity, already separately established in the earlier audit of §7.4, is
\[
 \operatorname{Cap}_D(\overline D_{e^{-t}})=\frac1{2t}\quad(t>0).
\]
It follows either from the logarithmic annular relative extremal function and its boundary circle current, or from the prior report
\`mathematical-audit/reports/2026-11-13-bt-disc-capacity-sharp-pole-rate.md\`;
**that previously established capacity calculation is reused, not re-registered as new work**.

Let \(t\to\infty\) and choose \(M_t=g(2t)\), so \(t_{M_t}=2t>t\). Then (3)–(5) give
\[
 \frac{(dd^c u_{M_t})(\overline D_{e^{-t}})}
 {\operatorname{Cap}_D(\overline D_{e^{-t}})^\beta}
 =\frac{\alpha}{2}(1+t)^{\alpha-1}(2t)^\beta
 \sim \alpha\,2^{\beta-1}t^{\,\beta+\alpha-1}\longrightarrow+\infty. \tag{6}
\]
Therefore **for every \(\beta>p/(p+1)\)** there is no uniform estimate of the form
\[
 (dd^cu)(A)\le C_{p,E}\operatorname{Cap}_D(A)^\beta
\]
for all \(u\in\mathcal E_0(D)\) with \(e_p(u)\le E\) and all Borel \(A\), even if the total masses are uniformly bounded. The exponent \(p/(n+p)\) derived in (2) is **sharp in complex dimension one**. Formula (6) makes *no assertion of sharpness of the numerical constant \(K_{n,p}\)*, and **does not establish exponent optimality in dimensions \(n\ge2\)**.

## 3. Classification, dependencies and precise coverage

- **Low / verified conditional deduction.** No printed statement is false and no repair is claimed. The optimization is elementary and complete conditional on printed Eq. 7.11.21; the radial distribution and uniform energy computation are direct. The exact disc-capacity normalization is a reused previously audited result, and the general proof of Lemma 7.11.19 still depends on the underlying Bedford–Taylor locality, mixed products, compact-perturbation mass invariance (Lemma 7.11.18), and comparison steps; these have **not** been transitively certified in this run.
- **Affected dependents:** Proposition 7.11.22's energy/capacity discussion, the capacity-control hypothesis in Lemma 7.11.27, and later compact-support Monge–Ampère existence arguments (Theorem 7.11.30) are possible applications, **not** newly certified implications or replacements. Do not interchange the quantified family limit with a varying exceptional set without the uniform estimate (2).
- **Proposed optional source edit:** introduce (2), its finite-capacity and zero-energy cases, and the dimension-one sharpness example as an independently reviewable explanatory remark after 7.11.19. **No production body, registry, permanent tag, source repository, main branch or website was modified by this audit.**
- **Exact new proof-level coverage:** integrated Lemma 7.11.19, Eq. 7.11.21 and its truncation-current proof, the new optimized inequality and dimension-one sharpness. Definition 7.11.1, capacity Definition 7.4.2, and Proposition 7.11.22 were read only to match hypotheses and distinguish claims. **Previously partially reviewed §7.11: +0 first-visited numbered sections, +0 wholly mathematically certified sections; current ToC still 25 chapters / 747 sections.** No project build, tests, CI or formal verification was run for this mathematical derivation.
- **Owner-deferred items:** Demailly approximation/regularization and dedicated Bergman, L², Ohsawa–Takegoshi, multiscale-atlas, positivity-loss proof-completion research remain **deferred-by-user**, neither resolved nor certified. The radial subharmonic example is an elementary one-dimensional calculation outside the excluded programme.
