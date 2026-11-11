# Green level boundary measures: exactly which harmonic test functions are reproduced?

**Finding:** \`POME-GREEN-BDY-HARMONIC-VS-PLURIHARMONIC-001\`  
**Assessment:** low / **verified conditional deduction**. No error in the printed propositions.  
**Audit date:** 2026-11-11.  
**Production main reviewed:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`.  
**Integrated reading-edition file:** \`docs/sections/green-level-measures-and-boundary-representation/index.html\`; Git blob \`895dbdfaa3c78ce41abe556f573644d857ab7517\`.

## Source-accurate anchors and scope

- Section 7.20, opening convention on physical line 7: \(d^c=i(\bar\partial-\partial)/(4\pi)\), \(dd^c=i\partial\bar\partial/(2\pi)\), and \(m_n=2^{-n}\).
- Proposition **7.20.2**: \`klimek-pluripotential-theory:1F1C8FD9\`, permanent tag \`351C8FCB17FF\`, physical lines **47–82**. Its monotonicity/Jensen formula is read as background, not independently certified.
- Proposition **7.20.3**: \`klimek-pluripotential-theory:62713F04\`, permanent tag \`EC62871F80C4\`, physical lines **85–105**. The printed result reproduces **pluriharmonic** test functions, not all real-harmonic ones.
- Proposition **7.20.4**: \`klimek-pluripotential-theory:D0489F01\`, permanent tag \`438C4583CB39\`, physical lines **109–132**. Its explicit boundary measures for the ball and polydisc are the sole nontrivial input for the calculations below.
- Proposition **7.20.1**: \`klimek-pluripotential-theory:1821D4AD\`, permanent tag \`1359A4B6C1D8\`, physical lines **10–35**, was read for the level-flux convention, but its general chain-rule proof was not independently recertified.

All calculations below concern the **normalized probability** \(\rho_{D,a}:=2^n\mu_{D,a}\); without this normalization, each displayed expectation is multiplied by \(2^{-n}\).

## Verified statement: sharp test-class distinctions

Let \(n\ge 2\), \(B=\{z\in\mathbb C^n:|z|<1\}\), and \(\Delta^n\) be the unit polydisc. Set
\[
v(z)=|z_1|^2-|z_2|^2,\qquad a_t=(t,0,\ldots,0),\quad 0<t<1.
\]
Then \(v\) is real-harmonic for the **Euclidean** real Laplacian:
\(\Delta_{\mathbb R^{2n}}v=4-4=0\), but it is not pluriharmonic, since \(dd^c v\ne0\).

**(A) The polydisc admits an exact failure for every \(t\).** Proposition 7.20.4 puts \(\rho_{\Delta^n,a}\) on the distinguished torus \(\mathbb T^n\), where \(|\zeta_1|=|\zeta_2|=1\). Consequently,
\[
\boxed{\int_{\partial\Delta^n}v\,d\rho_{\Delta^n,a_t}=0
       \ne t^2=v(a_t)\quad(0<t<1).}
\]
In contrast, this product boundary measure reproduces **every continuous separately harmonic function** on the closed polydisc: apply the one-variable disc Poisson formula in each coordinate successively, with the other coordinates fixed. This is a larger test class than pluriharmonic functions. For example,
\(\operatorname{Re}(z_1\bar z_2)\) is separately harmonic but not pluriharmonic, and is reproduced by the product kernel.

**(B) The ball has a strict, quantified failure for small \(t\).** Let \(\sigma\) be normalized spherical probability and write
\[
K_t(\zeta)=\left(\frac{1-t^2}{|1-t\zeta_1|^2}\right)^n,
\qquad
d\rho_{B,a_t}=K_t\,d\sigma .
\]
The unit sphere's rotational invariance gives
\[
\mathbb E_\sigma|\zeta_j|^2=\frac1n,\qquad
\mathbb E_\sigma|\zeta_1|^4=\frac{2}{n(n+1)},\qquad
\mathbb E_\sigma|\zeta_1|^2|\zeta_2|^2=\frac{1}{n(n+1)}.
\]
For completeness, \(s=|\zeta_1|^2\) has density
\((n-1)(1-s)^{n-2}ds\) on \([0,1]\), and conditionally on \(s\) the remaining coordinate squares have mean \((1-s)/(n-1)\). The beta integrals immediately give all three formulas.

Uniformly in \(\zeta\) for \(t\) in a small fixed interval, expand
\[
K_t=1+nt(\zeta_1+\bar\zeta_1)
+t^2\left[\frac{n(n+1)}2(\zeta_1^2+\bar\zeta_1^2)
+n^2|\zeta_1|^2-n\right]+O_n(t^3).
\]
Multiplication by \(v(\zeta)=|\zeta_1|^2-|\zeta_2|^2\) and integration kills the constant, the linear and the nonzero angular-frequency terms. Its quadratic coefficient is
\[
n^2\mathbb E_\sigma[v|\zeta_1|^2]
=n^2\left(\frac{2}{n(n+1)}-\frac1{n(n+1)}\right)
=\frac{n}{n+1}.
\]
The expectation is even and real analytic in \(t\) near \(0\): replace
\(\zeta_1\) by \(-\zeta_1\), which leaves \(v\) and \(\sigma\) fixed and sends \(K_t\) to \(K_{-t}\).
The remainder is therefore \(O_n(t^4)\), yielding the sharp local comparison
\[
\boxed{
\int_{\partial B}v\,d\rho_{B,a_t}
=\frac{n}{n+1}t^2+O_n(t^4),\qquad
v(a_t)-\int_{\partial B}v\,d\rho_{B,a_t}
=\frac{t^2}{n+1}+O_n(t^4).}
\]
The difference is strictly positive for all sufficiently small positive \(t\). In particular, for \(n\ge2\), \(\rho_{B,a}\) is **not** the Euclidean harmonic measure of the ball in general: it is the Poisson–Szegő-type boundary measure induced by the pluricomplex Green function. The kernel's normalization is consistent to order two, since \(\mathbb E_\sigma K_t=1+[n^2/n-n]t^2+O(t^4)=1+O(t^4)\); exact normalization already follows from Proposition 7.20.3.

**(C) Dimension one is the boundary case.** For \(n=1\), the printed ball and polydisc kernel reduces to the ordinary disc Poisson kernel, and every real-harmonic function on a plane domain is locally pluriharmonic. The preceding mismatch requires at least two complex coordinates.

## Audit classification, dependency boundary and proposed documentation note

The printed Proposition 7.20.3 correctly limits its zero-correction representation to *pluriharmonic* tests, and Proposition 7.20.4 correctly distinguishes the ball and polydisc boundary supports. **No printed assertion is refuted.** The result precisely rules out a tempting but incorrect downstream extrapolation from a positive Green level measure to arbitrary Euclidean harmonic data in complex dimension \(>1\).

Proposed **non-applied** editorial clarification immediately after Proposition 7.20.4: “In dimensions \(n>1\), these Green boundary measures should not be confused with Euclidean harmonic measure. They reproduce pluriharmonic functions; on the polydisc, the product kernel also reproduces continuous separately harmonic functions, but neither kernel reproduces arbitrary Euclidean harmonic functions.”

**Affected dependents:** any future claim identifying \(\mu_{D,a}/m_n\) with Euclidean harmonic measure or applying Proposition 7.20.3 to all Euclidean harmonic test functions. No concrete printed dependent asserting this was identified in this review. The existing statements themselves need no repair.

**Dependencies:** the explicit kernels and support statements in Proposition 7.20.4, and the mass normalization from Proposition 7.20.3. These are not transitively certified here. The new countertests and moment calculation are elementary and self-contained *conditional on these printed kernels*. No Demailly approximation, Bergman, \(L^2\), Ohsawa–Takegoshi, multiscale-atlas or positivity-loss work is used or reopened.

**Actual coverage:** first proof-level visit to **§7.20** in this audit ledger; detailed calculations for Propositions 7.20.3–4 and direct reading of Propositions 7.20.1–2 for scope and normalization. Other Chapter 7 sections, full proofs of the Green boundary constructions, and their upstream classical Bedford–Taylor/Green identities are **not certified**. The inventory remains **25 chapters / 747 distinct numbered sections**, with **one newly visited section and zero fully mathematically certified sections** in this run. No project build, tests, formal verification, CI or website publication was performed. The excluded regularization programme remains **deferred-by-user**, not solved.
