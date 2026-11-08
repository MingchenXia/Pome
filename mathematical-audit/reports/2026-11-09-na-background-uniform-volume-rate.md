# 9 November 2026 — a uniform Kähler-background volume rate in non-Archimedean potential theory

## Version, classification and exact scope

- **Stable finding ID:** POME-NA-VOLUME-UNIFORM-BACKGROUND-RATE-001.
- **Severity / status:** **low / verified conditional deduction**. This is a quantitative consequence of the printed comparison calculation, not a correction of a false theorem. No printed theorem is alleged false.
- **Reviewed production main:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`. **Audit branch at start:** \`bca67749de54565b96ca58e8f81ee4d8f53eaf70\`.
- **Primary integrated reading page:** \`docs/sections/non-archimedean-pluripotential-theory/index.html\`, Git blob \`8448d710690ebe1cc28040f9611d05c9d008a961\`.
- **Definition 22.1.7:** original stable label \`sgpt:6F37B588\`, permanent tag \`A92D6DFAC0CF\`, physical lines **118–123**.
- **Proposition 22.1.39:** original stable label \`sgpt:20714EEA\`, permanent tag \`15E20104530B\`, physical lines **614–673**, particularly the projective-background mass computation **653–671**. Its equation (22.1.40) has original label \`sgpt:0912AC73\`, permanent tag \`AA5696D80091\`, physical lines **616–619**.
- **Context only, NOT independently certified:** Proposition 17.12.19 (\`sgpt:129B6722\` / \`724BF0CAE002\`), and Theorem 13.13.11 (\`sgpt:00CC32E0\` / \`0E5F6133B048\`), read at their current integrated tag pages; Definition 17.12.1 (\`sgpt:ECCF19D5\` / \`C8399F09D86D\`) read at \`docs/sections/test-curves--the-notion-of-test-curves/index.html\`, blob \`6dfdfc2b5e599eb3a19a9558a9c963e79df71dc7\`, lines 7–39.
- **Excluded work:** no Demailly approximation/regularization, dedicated Bergman/L²/Ohsawa–Takegoshi, multiscale-atlas, or positivity-loss proof programme was inspected or replayed. Any historical unresolved notes remain **deferred-by-user**, not repaired.

## Precise quantitative deduction

Let \(X\) be a compact connected Kähler manifold of complex dimension \(n\geq1\), and let \(\theta\) be a smooth closed real \((1,1)\)-form with pseudo-effective class. Fix a Kähler form \(\omega_0\). Choose a Kähler form \(\Omega\) with
\[
             \Omega\geq\theta+\omega_0
\]
as smooth real \((1,1)\)-forms (for instance take a sufficiently large positive multiple of \(\omega_0\)). For **every** \(\Gamma\in\mathrm{PSH}^{\mathrm{NA}}(X,\theta)\) put
\[
 M_\delta(\Gamma)=
 \int_X\left\langle
  \bigl(\theta+\delta\omega_0+
  dd^c\Gamma^{\theta+\delta\omega_0}_{-\infty}\bigr)^n
 \right\rangle,\qquad 0<\delta\leq1,
\]
and \(m(\Gamma)=\operatorname{vol}\Gamma\) as in Definition 22.1.7. Here the brackets denote the **non-pluripolar** product; the displayed integral in the source uses its established shorthand.

Then the following bound holds with **one constant for the entire non-Archimedean space**, without a positive-volume condition and without monotonicity of a family:
\[
\boxed{
0\leq M_\delta(\Gamma)-m(\Gamma)\leq
B(\delta):=\sum_{k=1}^{n}\binom nk\delta^k
 \int_X\Omega^{n-k}\wedge\omega_0^k
\leq C\delta,
}
\tag{*}
\]
where \(C=\sum_{k=1}^{n}\binom nk\int_X\Omega^{n-k}\wedge\omega_0^k\) is independent of \(\Gamma\).

Consequently, for **any nonempty indexing set** \(I\) and arbitrary collection \((\Gamma^i)_{i\in I}\subset\mathrm{PSH}^{\mathrm{NA}}(X,\theta)\),
\[
 0\leq \sup_{i\in I}M_\delta(\Gamma^i)
       -\sup_{i\in I}m(\Gamma^i)\leq B(\delta),
\]
and likewise for the infima. In particular,
\[
 \lim_{\delta\downarrow0}\sup_{i\in I}M_\delta(\Gamma^i)
 =\sup_{i\in I}\operatorname{vol}\Gamma^i,
 \qquad
 \lim_{\delta\downarrow0}\inf_{i\in I}M_\delta(\Gamma^i)
 =\inf_{i\in I}\operatorname{vol}\Gamma^i.
\]
These statements justify interchanging a supremum or infimum over **arbitrary** metrics with the **cofinal Kähler-background limit**. They do **not** assert
\(\operatorname{vol}(\sup_i^{*}\Gamma^i)=\sup_i\operatorname{vol}\Gamma^i\)
for an arbitrary family: the increasing-net hypothesis in printed Proposition 22.1.39 addresses a different, necessary fixed-background continuity step.

### Proof, including the directed-net quantifier

For \(0<\eta<\delta\leq1\) set
\[
 T_\eta=\theta+\eta\omega_0+
           dd^c\Gamma^{\theta+\eta\omega_0}_{-\infty}\geq0.
\]
The transition compatibility, the model-envelope mass identity of Proposition 17.12.19, and the precise mass computation already made in **lines 653–662** of the printed proof of Proposition 22.1.39 yield
\[
 M_\delta(\Gamma)
 =\int_X\langle(T_\eta+(\delta-\eta)\omega_0)^n\rangle.
\]
Thus, by multilinearity of non-pluripolar products with a smooth semipositive form,
\[
 M_\delta(\Gamma)-M_\eta(\Gamma)
 =\sum_{k=1}^{n}\binom nk(\delta-\eta)^k
       \int_X\langle T_\eta^{n-k}\rangle\wedge\omega_0^k.
\tag{1}
\]
All summands are nonnegative. Since \(\Omega-\theta-\eta\omega_0\geq0\), comparison of the cohomologous positive current
\(T_\eta+(\Omega-\theta-\eta\omega_0)\)
with the **smooth** representative \(\Omega\), using the non-pluripolar monotonicity theorem (Theorem 13.13.11), gives for \(0\leq a\leq n\)
\[
 0\leq\int_X\langle T_\eta^a\rangle
                 \wedge\omega_0^{n-a}
 \leq\int_X\Omega^a\wedge\omega_0^{n-a}.
\tag{2}
\]
The first inequality is positivity. For the second, adding the positive smooth difference only increases each mixed product, while the smooth \(\Omega\) is less singular than the resulting positive current and has total mixed mass equal to its cohomological intersection number. The case \(a=0\) is equality.

Applying (2) to (1) and using \(0<\delta-\eta\leq\delta\) proves the **uniform** comparison
\[
0\leq M_\delta(\Gamma)-M_\eta(\Gamma)\leq B(\delta).
\tag{3}
\]
The ray \(\eta\omega_0\) with \(\eta\downarrow0\) is **cofinal** in the reversed-order directed set of Kähler forms from §22.1.1: for every Kähler form \(\omega'\) on \(X\), sufficiently small \(\eta>0\) satisfies \(\eta\omega_0\leq\omega'\). Thus Definition 22.1.7, not an unjustified sequential-compactness assertion, implies
\(M_\eta(\Gamma)\downarrow m(\Gamma)\).
Let \(\eta\downarrow0\) in (3) to establish (*).

For every \(i\), one has \(m_i\leq M_{\delta,i}\leq m_i+B(\delta)\); taking the supremum or infimum preserves these inequalities, with no exchange of non-pluripolar limits or Choquet reductions. All quantities are finite, bounded by the finite smooth cohomological mass of the corresponding positive class. Finally \(B(\delta)\to0\).

### Sharpness of the linear exponent (not of the displayed constant \(C\))

Take \(X=\mathbf P^n\) with its Fubini–Study form \(\omega=\omega_{\mathrm{FS}}\), normalized to have \(V=\int_X\omega^n>0\), and set \(\theta=\omega_0=\omega\). Let \(\Gamma\) be the elementary constant-model test curve
\(\Gamma_\tau\equiv0\) for \(\tau<0\), with cutoff \(\Gamma_{\max}=0\) (and \(-\infty\) above the cutoff). In every background \(\theta+\delta\omega\), its model envelope remains \(0\), so
\[
 M_\delta(\Gamma)=(1+\delta)^n V,\quad
 m(\Gamma)=V,\quad
 M_\delta(\Gamma)-m(\Gamma)
   =\bigl((1+\delta)^n-1\bigr)V
   =nV\delta+O(\delta^2).
\]
Therefore the universal \(O(\delta)\) **rate cannot be improved to \(o(\delta)\)**, already for a single smooth positive model, and in every complex dimension. Nothing here asserts that the particular upper-bound coefficient \(C\) in (*) is optimal.

## Classification, proposed edit, dependents and limitations

- **Printed Proposition 22.1.39:** its theorem and original background comparison remain valid; this is an **additional explicit uniform modulus and arbitrary-family interchange**, not an error or a repaired missing lemma. The fixed-background increasing-net convergence and its cited dependencies are not recertified.
- **Possible optional production change (NOT performed):** after Proposition 22.1.39, insert a separately tagged remark giving (*) and the \(\mathbf P^n\) linear-sharpness example. Keep the original labels, historical attribution and all reader conventions.
- **Potential dependents:** applications of Definition 22.1.7 and Proposition 22.1.39 that take sup/inf over variable non-Archimedean metrics while shrinking a Kähler background. Only the **background** limit exchange proved above is authorized; no new conclusion about NA envelope suprema follows without its own continuity argument.
- **Dependencies treated as conditional:** Proposition 17.12.19 and Theorem 13.13.11 were read in the integrated edition and their exact hypotheses matched; their entire proof chains, including unrelated regularization claims, are not certified.
- **Actual coverage:** first direct selected inspection of the background-estimate passages of **§22.1.39** and Definition 22.1.7; §22.1 had prior partial audits, hence **zero first visits to a new numbered section and zero complete-section certifications**. Total current ToC: **25 chapters / 747 numbered sections / 0 fully certified sections**.
- **Actions actually taken:** mathematical argument and source-statement/tag/hypothesis cross-checks; **no numerical tests, project build, GitHub Actions CI, formal verification, source/main/registry/canonicalization changes, or site publication**.
