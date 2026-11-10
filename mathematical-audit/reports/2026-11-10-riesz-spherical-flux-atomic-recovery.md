# Exact spherical Riesz-flux formula and atomic recovery

- **Finding ID:** POME-RIESZ-SPHERICAL-FLUX-ATOMIC-RECOVERY-001
- **Date:** 2026-11-10
- **Classification:** low / **verified conditional deduction**. This is neither a false printed theorem nor a completed certification of its dependencies.
- **Reviewed production main:** b6933b772f41b45918f7e25ed1afbbb1fd892272
- **Actual direct proof-level scope:** §3.4, Proposition 3.4.11, Theorem 3.4.12(2), Theorem 3.4.14, and the stated radial fundamental solution of §3.1.13; NOT the entirety of §§3.1 or 3.4.
- **Integration paths and Git blob SHA:** 
  - \`docs/sections/subharmonic-functions/index.html\`, \`3d06e9703f2eb184cf63a2c45524ed6acbeeebd2\`; Proposition 3.4.11 physical lines 186–214, Theorem 3.4.12 lines 218–285 (particularly formula 3.4.13 at 227–232), Riesz decomposition Theorem 3.4.14 lines 298–310, Example 3.4.15 lines 314–330.
  - \`docs/sections/harmonic-functions-and-the-dirichlet-problem/index.html\`, \`fc02188d6e246a21aa07acd8bf6d3712761ba6e5\`; Proposition 3.1.13 and equation 3.1.14 at physical lines 244–253.
- **Stable source-label / permanent-tag pairs:** Proposition 3.4.11 \`foundations-of-pluripotential-theory:45B5A1B8\` / \`1F52C5AF98EF\`; Theorem 3.4.12 \`foundations-of-pluripotential-theory:7E2C1398\` / \`E76E281548A5\`; Theorem 3.4.14 \`foundations-of-pluripotential-theory:A2BCDB4A\` / \`F04DBD614238\`; Proposition 3.1.13 \`foundations-of-pluripotential-theory:571B3697\` / \`F8A69601BB8C\`; equation 3.1.14 \`foundations-of-pluripotential-theory:BC51DE75\` / \`49DB76D43578\`.
- **Severity and dependents:** low. Provides a local radial mass-recovery tool for classical Riesz potentials and possible potential-theoretic applications of Chapters 3–4. It does not alter the statements or canonical entries, and no downstream theorem has been certified merely by citing it.

## Exact statement

Let \(\Omega\subset\mathbb R^d\) be open, \(d\ge2\), let \(u\in\mathrm{SH}(\Omega)\) be locally integrable, and let \(\mu=\Delta u\) be its positive Riesz measure (the normalization **without** a factor \(2\pi\)). Fix \(a\in\Omega\) and a radius \(R>0\) sufficiently small that \(\overline{B(a,2R)}\subset\Omega\). Write

\[
m_a(r)=\frac{1}{s_{d-1}r^{d-1}}\int_{\partial B(a,r)}u\,dS,\qquad0<r<R .
\]

Then \(m_a(r)\) is finite and continuous, and its one-sided derivatives exist for every \(0<r<R\), with the **exact** flux identities

\[
\boxed{\quad s_{d-1}r^{d-1}m'_{a,-}(r)=\mu(B(a,r)),\qquad
s_{d-1}r^{d-1}m'_{a,+}(r)=\mu(\overline{B(a,r)}) .\quad}
\]

In particular,

\[
s_{d-1}r^{d-1}\bigl(m'_{a,+}(r)-m'_{a,-}(r)\bigr)
=\mu(\partial B(a,r)),
\]
and both normalized one-sided fluxes converge to \(\mu(\{a\})\) as \(r\downarrow0\). These are one-sided radial derivatives of the **spherical mean**, not derivatives of \(u\) at \(a\).

The same atom is recovered by the singular growth:

\[
\boxed{\begin{aligned}
d=2:&\quad \lim_{r\downarrow0}\frac{m_a(r)}{\log r}=\frac{\mu(\{a\})}{2\pi},\\
d\ge3:&\quad \lim_{r\downarrow0}r^{d-2}m_a(r)
=-\frac{\mu(\{a\})}{(d-2)s_{d-1}}.
\end{aligned}}
\]

No pointwise finiteness of \(u(a)\), density, absence of spherical atoms, or regularity of \(\mu\) is assumed.

## Independent proof from the integrated inputs

1. **Local decomposition and normalization.** Choose \(0\le\eta\le1\) compactly supported in \(\Omega\), equal to one on a neighborhood of \(\overline{B(a,R)}\). The printed Riesz decomposition (§3.4.14) gives
   \[
   u(x)=p(x)+h(x),\qquad p(x)=\int E_d(x-y)\,d\lambda(y),\quad \lambda=\eta\mu,
   \]
   for \(x\) in a neighborhood of \(\overline{B(a,R)}\); \(h\) is harmonic and \(\lambda\) is a finite positive compactly supported measure. The fundamental solution is \(E_2(t)=(2\pi)^{-1}\log t\) and \(E_d(t)=-[(d-2)s_{d-1}]^{-1}t^{2-d}\) for \(d\ge3\); in **every** \(d\ge2\),
   \[
   E'_d(t)=\frac1{s_{d-1}t^{d-1}}\quad (t>0).
   \]

2. **Spherical-shell identity.** For any \(r>0\), \(y\in\mathbb R^d\),
   \[
   \frac1{s_{d-1}}\int_{S^{d-1}}E_d(a+r\omega-y)\,dS(\omega)
   =E_d\bigl(\max\{r,|y-a|\}\bigr). \tag{*}
   \]
   If \(|y-a|>r\), apply the harmonic mean-value property in the \(x\)-variable to \(E_d(x-y)\). If \(|y-a|<r\), the sphere average, viewed as a function of \(y\), is harmonic, radial and bounded near \(a\) on \(B(a,r)\); a bounded radial harmonic function on a ball is constant, equal to its value \(E_d(r)\) at \(a\). At \(|y-a|=r\), continuity follows from local integrability of the weak spherical singularity: the cap integral near the singular point is \(O(\delta)\) for \(d\ge3\) and \(O(\delta|\log\delta|)\) for \(d=2\); the remaining part is continuous. This proves (*), including atoms located on the sphere. Apply Tonelli/Fubini first to a constant upper bound minus \(E_d\) on the compact \(x-y\) range; (*) makes the integrated result finite for fixed \(r>0\). The harmonic mean of \(h\) is \(h(a)\). Hence
   \[
   m_a(r)=h(a)+\int E_d(\max\{r,|y-a|\})\,d\lambda(y). \tag{1}
   \]
   The integral is finite and continuous for each \(r>0\), by dominated convergence on each compact \(r\)-interval.

3. **All-radii one-sided derivatives.** For fixed \(r>0\), difference quotients of the integrand of (1) are uniformly bounded on a small \(r\)-interval by \(\sup E'_d\), so dominated convergence applies. From the right, each \(y\) with \(|y-a|\le r\) contributes \(E'_d(r)\); from the left, only \(|y-a|<r\) contributes. Thus
   \[
   m'_{a,+}(r)=E'_d(r)\lambda(\overline{B(a,r)}),\quad
   m'_{a,-}(r)=E'_d(r)\lambda(B(a,r)).
   \]
   As \(\eta=1\) on these balls, \(\lambda=\mu\) there. The flux jump is precisely the spherical mass, not an error term; continuity from above of finite \(\lambda\) gives the limit \(\mu(\{a\})\).

4. **Singular-growth coefficients.** For \(d\ge3\), multiply (1) by \(r^{d-2}\) and use
   \[
   r^{d-2}E_d(\max\{r,\rho\})=
   -\frac1{(d-2)s_{d-1}}\left(\frac r{\max(r,\rho)}\right)^{d-2}.
   \]
   The parenthesis is in \([0,1]\), and tends pointwise to \(\mathbf 1_{\{\rho=0\}}\). Dominated convergence and \(r^{d-2}h(a)\to0\) prove the asserted limit. For \(d=2\), divide (1) by \(\log r\) (\(r<1\)): for \(0<\rho\le1\), the ratio \(\log\max(r,\rho)/\log r\) is in \([0,1]\) and tends to zero; at \(\rho=0\), it equals one. For \(\rho>1\), the ratio is uniformly \(o(1)\) on the compact support of \(\lambda\). Dominated convergence yields the coefficient \(\lambda(\{a\})/(2\pi)\). This completes both formulas without interchanging unsupported singular limits.

## Sharp boundary: pole value does not detect an atom

The converse assertion “\(u(a)=-\infty\) implies \(\mu(\{a\})>0\)” is false, even for compactly supported **purely atomic** Riesz measures. On \(\mathbb R^2\), put \(r_k=e^{-4^k}\) and
\[
\lambda=\sum_{k\ge1}2^{-k}\delta_{r_ke_1},\qquad u=E_2*\lambda.
\]
The integrated Proposition 3.4.11 makes \(u\) globally subharmonic and locally integrable. There is no atom at the origin, \(\lambda(\{0\})=0\); nevertheless
\[
u(0)=\frac1{2\pi}\sum_{k\ge1}2^{-k}\log r_k
=-\infty.
\]
Its spherical means still obey \(m_0(r)/\log r\to0\). Similarly, for \(d\ge3\), choose \(r_k=2^{-2k/(d-2)}\) with the same masses. Then \(\lambda(\{0\})=0\) but \(u(0)=-\infty\), while \(r^{d-2}m_0(r)\to0\). Thus atomic flux and polar value are different invariants.

## Audit judgment and proposed text

- **Printed statements:** no error found in the checked clauses of Proposition 3.1.13, Proposition 3.4.11, Theorem 3.4.12 or Theorem 3.4.14.
- **New result:** exact one-sided radial flux, spherical-shell mass jump, and zero-scale atom normalization for arbitrary positive Riesz measure, with an explicit no-atom pole. This is not the previously logged Bôcher computation for a function harmonic on a punctured ball (which has an isolated distributional atom): diffuse and off-center masses are permitted here, and the entire radial distribution is recovered.
- **Suggested addition:** a corollary after Theorem 3.4.14 containing the boxed flux and atom formulas, with the no-atom pole example to prevent the false converse. **Proposed only**, not applied.
- **Dependencies not transitively certified:** printed Riesz decomposition, compactly supported potential, harmonic mean-value property and Euclidean fundamental-solution normalizations; these were checked in the exact portions cited, not re-proved globally. No Demailly approximation/regularization, Bergman, \(L^2\), Ohsawa–Takegoshi, multiscale atlas or positivity-loss work was examined.
- **Coverage:** one new selected proof-level topic within already partly reviewed §3.4; §3.1 only a normalization read. **0 first proof-level numbered-section visits; 0 complete-section certifications.** The actual current ToC has 25 chapters and 747 numbered sections.
