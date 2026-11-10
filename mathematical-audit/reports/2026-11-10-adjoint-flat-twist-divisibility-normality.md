# Audit: adjoint flat-twist divisibility, exact local multiplier threshold, and the pointwise-limit boundary

**Finding:** POME-ADJOINT-FLAT-DIVISIBILITY-SCOPE-001  
**Date:** 2026-11-10  
**Classification:** low / **verified conditional deduction** (exact local and global examples independently verified; printed theorem not refuted).  
**Reviewed production main:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`.  
**Integrated reading page:** \`docs/sections/flat-twists-of-adjoint-section-envelopes/index.html\`, blob \`f106e8f79d1a1341045f1e3c41cdeb531b5f699b\`, physical lines **9–13, 19–29, 31–55, 58–59**.  
**Statement:** Theorem 19.11.1, source \`cao-paun-foliations:24E1B42B\`, permanent tag \`1D4EB7891AC1\` (lines 9–13). Equation 19.11.2: source \`cao-paun-foliations:91A7CA06\`, permanent tag \`354F33395764\` (lines 37–39).  
**Internal dependencies inspected at the statement level only:** Theorem 10.102.1 (Nadel vanishing; source \`cao-paun-foliations:274E8A7B\`, permanent \`4F4355678C85\`, \`docs/sections/strictly-positive-singular-metrics/index.html\`, blob \`0816e58d94c6cdd7dd6ee5d1de369ffcdf473b43\`, lines 8–13); Lemma 10.103.1 (flat-twist Euler invariance; source \`cao-paun-foliations:885C5EE8\`, permanent \`E897B72A71BA\`, \`docs/sections/euler-characteristics-under-flat-twists/index.html\`, blob \`99c65b6051fef34b6ec0b8822c973ab5470bb30a\`, lines 8–15). Their analytic proof programmes are **not** certified in this review; the excluded approximation/L2 programme remains **deferred-by-user**.

## Exact local audit of the factorization argument

Assume the hypotheses of Theorem 19.11.1: smooth projective connected \(Z\), a semipositive singular metric \(h_F\) with \(\mathcal I(h_F)=\mathcal O_Z\), and the bundles and integer divisibilities stated there. Fix \(s\in H^0(Z,k_0D+\rho)\), and put \(k=\ell k_0\), \(\ell\ge2\). The metric chosen for \(B_k\) has, in the normal direction to a prime divisor of \(s\), the unbounded part
\[
 \frac{k-1}{k_0}\log|s|^2+\phi_F.
\]
At a smooth generic point of such a divisor \(E\), take a transverse coordinate \(z_1\) and write \(s=z_1^r \cdot\text{unit}\), \(r=\operatorname{ord}_E s\ge1\). Since a plurisubharmonic local weight \(\phi_F\) is locally bounded above, integrability of the chosen \(u_k\) in (19.11.2) implies integrability after discarding its nonnegative weight contribution \(e^{-\phi_F}\ge C^{-1}\). If \(u_k=z_1^j\cdot\text{unit}\) generically, the transverse integral dominates a multiple of
\[
 \int_0^\varepsilon R^{2(j-\alpha)+1}\,dR,\qquad
 \alpha=r\Bigl(\ell-\frac1{k_0}\Bigr).
\]
This is finite exactly when \(j>\alpha-1\); hence \(j\ge\lfloor\alpha\rfloor\). As
\[
 \alpha-(\ell-1)r=r(1-1/k_0)\ge0,
 \qquad
 \lfloor\alpha\rfloor\ge(\ell-1)r,
\]
every prime-divisor component of \(s\) divides \(u_k\) to at least the \((\ell-1)\)-st power. On **smooth** \(Z\), local holomorphic function rings are factorial (or, equivalently, divide by the defining hypersurface equations away from codimension two and use Hartogs extension); the quotient is holomorphic. It transforms as a section of
\[
 k_0D+\rho_0-(\ell-1)\rho,
\]
which proves the *exact factorization step* at printed lines 44–47. No assertion about Nadel vanishing or existence of \(u_k\) is needed for this conditional implication.

The generic transverse conclusion can be sharpened for an explicit local analytic weight. Suppose near a smooth point \(\phi_F=c\log|z_1|^2+O(1)\) with \(0\le c<1\), with the \(O(1)\) term bounded above and below, and all other factors smooth nonvanishing. The local multiplier ideal is **exactly**
\[
 J_k=(z_1^{\lfloor r(\ell-1/k_0)+c\rfloor}),
\]
because \(z_1^j\) is square-integrable precisely for \(j>r(\ell-1/k_0)+c-1\). The restriction \(c<1\) also gives \(\mathcal I(h_F)=\mathcal O\) in this model. For \(r=3,k_0=2,\ell=2\), one obtains \(J_k=(z_1^4)\) when \(c=0\), and \(J_k=(z_1^5)\) when \(c=3/5\), while the printed factorization only needs \(s^{\ell-1}=z_1^3\). Thus the statement's coarse exponent is safe but intentionally not sharp; the sharper floor is local and cannot be universally promoted without controlling the weight.

## Normality really is needed to convert orders into a holomorphic quotient

The smooth/normal hypothesis is not ornamental. On the nonnormal cusp
\[
 C=\{y^2=x^3\}\subset\mathbb C^2,\qquad
 \mathcal O_{C,0}=\mathbb C\{t^2,t^3\},\quad(x,y)=(t^2,t^3),
\]
take \(s=x\) and \(u=y\). On the normalization, \(\operatorname{ord}_0(u)=3\ge2=\operatorname{ord}_0(s)\), but
\[
 u/s=y/x=t\notin\mathbb C\{t^2,t^3\}.
\]
Indeed, any convergent series in \(t^2,t^3\) has zero coefficient of \(t\). Thus generic (normalized) order domination does **not** imply divisibility in a nonnormal local ring. This countermodel **does not refute** Theorem 19.11.1, which assumes smooth \(Z\); it prohibits extending its displayed divisor argument to arbitrary reduced spaces without a separate normality/saturation analysis.

## A global admissible factorization with no pointwise convergence

There is also a useful sharpness check on the actual limit topology at printed lines 50–58. Let \(Z=\mathbb P^1\), \(F=\mathcal O\) with the trivial metric, \(A=\mathcal O(3)\), \(m_0=k_0=1\), and \(\rho=\rho_0=\mathcal O\). Then \(K_Z=\mathcal O(-2)\) and \(D=\mathcal O(1)\). Choose two nonzero sections \(s,v\in H^0(\mathbb P^1,\mathcal O(1))\) with **distinct** simple zeros \(p_s,p_v\). Put
\[
 u_k=c\,s^{k-1}v\in H^0(\mathbb P^1,\mathcal O(k))
 \quad(k\ge2),
\]
where the single nonzero constant \(c\), independent of \(k\), normalizes the fixed weighted integral in (19.11.2) to one. (Upon cancellation of the \(s^{k-1}\) factor this integral is a fixed positive integral of \(|cv|^2\) against the smooth positive residual metric.) These sections belong to the very multiplier ideals \(J_k=(s^{k-1})\) in the printed construction. The quotient sections \(v_k=cv\) have fixed nonzero bounded supremum, and
\[
 \frac1k\log|u_k|^2
  =\frac{k-1}{k}\log|s|^2+\frac1k\log|cv|^2
  \longrightarrow\log|s|^2
\]
in \(L^1_{\mathrm{loc}}\) with any fixed smooth reference metrics, since the logarithms of nonzero section norms are locally integrable. **At \(p_v\)**, however, every left-hand side is \(-\infty\), while the proposed limit is finite because \(s(p_v)\ne0\). Pointwise convergence, even for this constant flat twist and fixed quotient \(v\), is therefore false. The printed proof correctly claims only \(L^1\) convergence and passes its envelope inequality via the canonical qpsh representative; replacing that step by pointwise convergence would be invalid.

## Classification, dependencies, and proposed editorial action

- **Status:** verified conditional deduction. The local order threshold, failure on a nonnormal cusp, and pointwise failure on a projective curve have complete independent justifications. **No confirmed false Pome theorem, no proven general repair.**
- **Severity:** low. The printed Theorem 19.11.1 already assumes smooth projective \(Z\), already uses \(L^1\) rather than pointwise convergence, and requires only the weaker integer factorization exponent.
- **Proposed optional addition:** a short remark after the proof specifying that the normality and \(L^1\)-topology choices are essential; optionally include the exact transverse floor formula under a divisorial analytic-weight hypothesis. No source/registry/tag changes are made.
- **Affected dependents:** any proposed generalization of 19.11.1 from smooth \(Z\) to nonnormal reduced spaces; any proposed upgrade of the normalized-section argument at lines 52–58 to pointwise convergence. The exact theorem's flat-twist equality is **not** contradicted.
- **Unresolved upstream:** the existence of \(u_k\) via the Nadel vanishing input 10.102.1 and its excluded analytic/L2 proof programme is *not* verified, and the global flat-twist equality is not hereby certified. Lemma 10.103.1 was read only for its statement and conditional use. Retain all earlier findings and user-deferred records without changing their statuses.

**Coverage delta:** detailed new proof-level checks for a previously sampled §19.11, with statement-level cross-reference only to §§10.102–10.103. **0 first proof-level section visits, 0 full mathematical section certifications**. Current main chapter/numbered-section inventory: **25 / 747**. No builds, tests, CI, publication or formal proof checks performed.
