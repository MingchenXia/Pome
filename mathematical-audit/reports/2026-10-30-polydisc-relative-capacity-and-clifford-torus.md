# 2026-10-30 — Exact relative capacity of arbitrary concentric polydiscs and concentration on their distinguished torus

**Stable finding:** \`POME-BT-POLYDISC-SHILOV-CAP-001\`  
**Severity / status:** **low / verified conditional deduction**, not a false theorem, proof-gap allegation, or complete verification of any section.  
**Reviewed production main:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`.  
**Destination:** audit notes only on \`review/mathematical-audit\`; optional mathematical example, not a production correction.

## Precisely inspected integrated sources

- **§7.16**, section tag \`554C8622D718\`: \`docs/sections/relative-extremals-on-bounded-hyperconvex-domains/index.html\`, main blob \`c6560283c5ff9e2587ffe93f7f2e7ba687105243\`. Relative extremal definition (physical lines **5–13**); **Proposition 7.16.1**, source \`klimek-pluripotential-theory:7B045988\`, permanent tag \`11F76749E371\` (statement **16–35**, proof and complex-norm ball formula **38–63**, especially **53–59**); **Proposition 7.16.4**, source \`klimek-pluripotential-theory:2CB6C014\`, tag \`CF1B00103D5B\` (proper-map equivariance **96–106**); **Theorem 7.16.5**, source \`klimek-pluripotential-theory:68BF935A\`, tag \`08DA18E923C1\` (capacity/mass statement **110–116** and proof **118–176**, with the explicit disc normalization near **179–185**).
- **§21.5**, \`docs/sections/convex-analysis-and-toric-potentials--the-real-monge-ampere-measure/index.html\`, main blob \`7089aa41ae2422b1bd6b5094e46668cbc8ed37be\`. **Theorem 21.5.1**, source \`foundations-of-pluripotential-theory:4A0FAEB3\`, tag \`409656CC47D4\`, physical lines **10–21**: the project's **n!** normalization of Alexandrov mass; Theorem 21.5.2, tag \`F4072D9ED060\`, lines **43–49**, local-uniform convex continuity. The elementary toric Jacobian is computed below rather than asserted from a source-number match.
- Local BT continuity and the fact that a locally bounded PSH Monge–Ampère measure does not charge pluripolar coordinate hyperplanes are **standing internal inputs** from Chapter 7. They were not transitively recertified in this session. No Demailly regularization, Bergman, L2, Ohsawa–Takegoshi, or positivity-loss proof was consulted or used.

## Exact result

Fix \`n>=1\`, radii \`0<r_i<R_i<infinity\`, the bounded hyperconvex polydisc
\[
 \Omega=\prod_{i=1}^n\{|z_i|<R_i\},\qquad
 K=\prod_{i=1}^n\{|z_i|\le r_i\},\qquad
 L_i=\log(R_i/r_i)>0 .
\]
With \(\log 0=-\infty\), the **raw and regularized** relative extremals coincide and have the formula
\[
\boxed{
 h_{K,\Omega}(z)=H_{K,\Omega}(z)
  =\max\left\{-1,\max_{1\le i\le n}
          \frac{\log(|z_i|/R_i)}{L_i}\right\}.
}
\tag{A}
\]
Let \(T_{\boldsymbol r}=\{|z_i|=r_i\text{ for every }i\}\), and let \(\sigma_{\boldsymbol r}\) be its normalized angular Haar probability. Under Pome's \(dd^c=(i/2\pi)\partial\bar\partial\) convention,
\[
\boxed{
 (dd^cH_{K,\Omega})^n
     =\frac{1}{2^n\prod_{i=1}^nL_i}\,
        \sigma_{\boldsymbol r},
 \qquad
 \operatorname{Cap}_{\Omega}(K)
     =\operatorname{Cap}_{\Omega}^{*}(K)
     =\frac{1}{2^n\prod_{i=1}^n\log(R_i/r_i)} .
}
\tag{B}
\]
Thus for \(n\ge2\) the entire Monge–Ampère mass is supported on the **real n-dimensional distinguished torus** \(T_{\boldsymbol r}\), a proper subset of \(\partial K\), despite \(H_K=-1\) on **all** of \(K\). This refines the support *inclusion* asserted in Theorem 7.16.5 without contradicting it. For equal radii and \(n=1\), (B) specializes exactly to the printed disc capacity \(1/(2\log(R/r))\).

## Proof

**1. Equal modulus ratios via a complex norm.** Suppose first that all \(R_i=1\) and all \(r_i=e^{-L}\) for one \(L>0\). The sup norm \(N(w)=\max_i|w_i|\) is a complex norm. The explicit norm-ball calculation in Proposition 7.16.1, lines 53–59, gives
\[
h_{\overline{\Delta}_{e^{-L}}^n,\Delta^n}
 =H_{\overline{\Delta}_{e^{-L}}^n,\Delta^n}
 =\max\{-1,L^{-1}\max_i\log|w_i|\}.
\]
The formula is continuous and PSH; the original norm-ball proof bounds every competitor on each complex radial line. No additional norm-smoothing theorem is invoked here.

**2. Arbitrary commensurable modulus ratios via a finite proper map.** Suppose integers \(m_i\ge1\) and \(L>0\) satisfy \(m_iL_i=L\) for all \(i\). The map
\[
 f:\Omega\longrightarrow\Delta^n,\quad
 f_i(z)=(z_i/R_i)^{m_i}
\]
is finite, proper, holomorphic, and surjective, and
\(f^{-1}(\overline{\Delta}_{e^{-L}}^n)=K\).
The raw and regularized equalities of Proposition 7.16.4, lines 96–105, imply (A) after composition, since \(m_i/L=1/L_i\). In particular, this step uses **proper finite-map equivariance**, not an unjustified assertion that arbitrary multiradius boxes are norm balls.

**3. General modulus ratios by decreasing compact sets.** Choose eventually positive rational numbers
\(L_i^{(k)}=\lfloor k!L_i\rfloor/k!\). These are nondecreasing in \(k\), converge to \(L_i\), and have pairwise rational ratios for each fixed \(k\). Set
\(K_k=\prod_i\{|z_i|\le R_i e^{-L_i^{(k)}}\}\).
After dropping finitely many indices, \(K_k\Subset\Omega\) and \(K_k\downarrow K\). Each \(K_k\) satisfies the commensurable case, and its explicit extremal \(u_k\) increases pointwise to the continuous function on the right of (A): every \(\log(|z_i|/R_i)\le0\) is divided by an increasing positive \(L_i^{(k)}\). Proposition 7.16.1(2), lines 25–27 and 40–41, gives \(h_{K_k,\Omega}\uparrow h_{K,\Omega}\), hence \(h_K=u\). Continuity yields \(H_K=u\) as well. This controls **all** ratios without presuming a finite-map construction for irrational ratios.

**4. Convex gradient simplex and concentration.** On \(\Omega\cap(\mathbb C^*)^n\) write \(x_i=\log|z_i|\) and
\[
 F(x)=\max\left\{-1,\frac{x_1-\log R_1}{L_1},
                         \ldots,\frac{x_n-\log R_n}{L_n}\right\}.
\]
The \(n+1\) affine pieces all meet only at
\(x_*=(\log r_1,\ldots,\log r_n)\).
Their slopes are \(0,e_1/L_1,\ldots,e_n/L_n\), so
\[
 \partial F(x_*)=\operatorname{conv}(0,e_1/L_1,\ldots,e_n/L_n),
 \qquad
 \operatorname{vol}\partial F(x_*)=\frac{1}{n!\prod_iL_i}.
\]
At every other \(x\) fewer than \(n+1\) affines are active, so the subgradient has dimension below \(n\), hence zero \(n\)-volume. Therefore the real Alexandrov measure in **Pome's** convention is exactly
\[
 \operatorname{MA}_{\mathbb R}(F)
      =n!\operatorname{vol}(\partial F(\cdot))
      =\frac{1}{\prod_iL_i}\delta_{x_*}.
\]

**5. Exact complex normalization, not a guessed \(n!\).** For any smooth convex \(F\), logarithmic polar coordinates \(z_i=e^{x_i+i\theta_i}\) give
\[
 (dd^c F(\log|z|))^n
 =\frac{n!}{(4\pi)^n}\det D^2F(x)\,
   \prod_i(dx_i\wedge d\theta_i)
\]
as an oriented positive measure. Integrating each \(\theta_i\) over \([0,2\pi]\) shows
\[
 (\log|\cdot|)_*((dd^c F(\log|z|))^n)
       =2^{-n}\operatorname{MA}_{\mathbb R}(F).
\tag{C}
\]
For the finite piecewise-affine \(F\) here, locally uniform convex approximations in the \(x\)-variables, Alexandrov's local weak continuity from Theorem 21.5.2, and locally bounded Bedford–Taylor continuity give (C) on \((\mathbb C^*)^n\). The bounded PSH function (A) has no Monge–Ampère mass on the pluripolar coordinate hyperplanes, so no mass is lost when passing to \(\Omega\). Thus the pushforward mass is \(2^{-n}(\prod_iL_i)^{-1}\delta_{x_*}\). Coordinatewise angular invariance forces the lift to be exactly this constant times normalized Haar probability on \(T_{\boldsymbol r}\), proving the first equality (B). The capacity formula follows from Theorem 7.16.5, not from a claim that all intermediate capacities were independently reproved.

## Disposition, limitations, downstream use

- **Status:** verified conditional deduction; **original Propositions 7.16.1/7.16.4 and Theorem 7.16.5 are correct in this model**. No new theorem error or demonstrated proof gap is alleged. These source theorems and BT/convex continuity inputs have **not** been fully recertified.
- **Proposed addition:** an optional explicit \`n\`-dimensional example after Theorem 7.16.5, retaining all existing source labels, permanent tags, historical attributions, and the original weaker support statement.
- **Affected mathematical consumers:** numerical capacity benchmarks in §§7.4–7.6 and 7.16; exact finite-coordinate-map normalization in Proposition 7.16.4; the distinction between real Alexandrov mass (§21.5.1) and complex \(dd^c\)-mass. The result is **not** a general capacity-multiplicity theorem for arbitrary proper maps, nor a replacement for comparison or local BT continuity.
- **Newly performed scope:** direct selected proof/formula checks of §7.16.1(2–3), the norm-barrier argument at §7.16.1, §7.16.4's finite-map equality, §7.16.5's mass normalization, and §21.5.1–2's convex measure convention. Not all of §7.16 or §21.5; no whole section/chapter certified.
- **Ledger and coverage:** preserve all pre-existing confirmed errors, unresolved gaps, candidate and external-dependency statuses without silently resolving any. The separately excluded Demailly approximation/regularization and its dedicated Bergman/L2/OT/multiscale-atlas/positivity-loss programme remains **deferred-by-user** and was not used.
- **Operational boundary:** report-only audit update; no main, mathematical source/body, canonicalization, permanent tag, website, CI, build, or formal-verification changes.
