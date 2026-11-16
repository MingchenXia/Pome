# Quantitative energy concentration for bounded degenerate Hermitian Monge–Ampère solutions

**Finding ID:** POME-DEGENMA-ENERGY-OSC-SHARP-TV-001  
**Date:** 2026-11-16  
**Status / severity:** **verified conditional deduction / low**. The original Proposition 14.24.5 and Theorem 14.24.1 have **not** been disproved. The constants are sharp **within the abstract signed-measure identities furnished by Proposition 14.24.5**, not claimed to be realizable in every geometric Monge–Ampère class.  
**Reviewed main:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`  
**Integrated page:** \`docs/sections/uniqueness-for-degenerate-equations--bounded-uniqueness-and-connectedness/index.html\`, blob \`52185a663bef778cc6da47299bda5c32fcb05670\`.  
**Exact anchors:** Proposition 14.24.5, source \`non-kahler-pluripotential-theory:8137BCDB\`, permanent \`25FABE38E60B\`, physical lines 58–80; Equation 14.24.6, source \`09035D3B\`, permanent \`5EA1FD990FD5\`, lines 60–63; Equation 14.24.7, source \`B0F9B793\`, permanent \`B3915B7974CA\`, lines 65–71; the moment-zero and positive-density argument, lines 106–112. Dependent Theorem 14.24.1, source \`3B7B4CAD\`, permanent \`98EC31947E4C\`, lines 10–16 and its closing proof; Lemma 14.24.11 is a contextual downstream consumer, not independently re-proved here.

## Statement and hypotheses

Let \(X\) be compact with Hermitian background \(\omega\), and suppose \(u,v\) are **continuous bounded** \(\omega\)-psh potentials with equal Monge–Ampère measures \(A^n=B^n=F\omega^n\), where \(F\ge0\) is bounded and measurable, exactly as in Proposition 14.24.5. Put \(w=u-v\), \(a=\min_Xw\), \(b=\max_Xw\), \(L=b-a\). Let
\[
 T=\sum_{j=0}^{n-1}A^j\wedge B^{n-1-j},\qquad
 E=dw\wedge d^cw\wedge T,\qquad
 \zeta=dd^cT,\qquad M=\|\zeta\|_{\mathrm{TV}}.
\]
These objects are defined distributionally in the printed proposition. It proves \(E\ge0\), \(\zeta\) is a finite signed top-degree measure, and
\[
 \nu=w_*E=k(t)\,dt,\quad
 \sigma=w_*\zeta,\quad
 k(t)=\int_{\mathbb R}(s-t)_+\,d\sigma(s)\ge0,
 \qquad
 \sigma(\mathbb R)=\int s\,d\sigma(s)=0.
\]
The measure \(\sigma\) is supported on \([a,b]\) and \(m:=\|\sigma\|_{\rm TV}\le M\).

**New quantitative deductions:**
\[
 0\le k(t)\le {m\over2}\min\{(t-a)_+,(b-t)_+\}\quad (a\le t\le b),
 \tag{A}
\]
\[
 E\{a\le w\le a+h\},\
 E\{b-h\le w\le b\}
 \le {m h^2\over4}\le{M h^2\over4}\quad(0\le h\le L),
 \tag{B}
\]
and the **sharper global bound**
\[
 \boxed{E(X)=\int_X dw\wedge d^cw\wedge T
       \le {m\over16}\operatorname{osc}_X(w)^2
       \le {M\over16}\operatorname{osc}_X(w)^2.}
 \tag{C}
\]
At \(L=0\), \(E=0\) directly, so the formulas remain valid. Neither (A)–(C) requires connectedness of \(\{F>0\}\), continuity of \(F\), or the auxiliary smooth test-density construction of Proposition 14.24.13. The conditional input is exactly the construction and pushforward identity of Proposition 14.24.5, rather than a new proof of its Bedford–Taylor prerequisites.

## Full elementary proof

Since \(\sigma(\mathbb R)=0\), its positive and negative parts have equal masses \(m/2\). The map \(t\mapsto(s-t)_+\) is 1-Lipschitz, and the exact one-sided derivative of \(k\) is, at all points outside the at most countably many atoms,
\[
 k'(t)=-\sigma((t,b]).
\]
Consequently \(|k'(t)|\le m/2\) a.e., because a signed measure of total mass zero has \(|\sigma(B)|\le m/2\) for **every** Borel set \(B\). From the two moment cancellations one gets \(k(a)=\int(s-a)\,d\sigma=0\); also \(k(b)=0\), and outside \([a,b]\) the function vanishes. Lipschitz continuity therefore implies the two-sided tent majorant (A). Integrating (A) on either extreme layer gives (B), using the **exact** identity \(w_*E=k(t)\,dt\); endpoint atoms do not contribute.

The global constant \(1/16\) does **not** follow from simply integrating the tent majorant, which would only give \(1/8\). Instead, by signed Fubini on the bounded interval,
\[
 E(X)=\int_a^b k(t)\,dt
 =\frac12\int_a^b(s-a)^2\,d\sigma(s).
\]
Put \(x=s-a\) and consider
\[
 Q(x)=\frac{x^2}{2}-\frac{Lx}{2}+\frac{L^2}{16}.
\]
On \(0\le x\le L\), the quadratic takes value \(+L^2/16\) at both endpoints and \(-L^2/16\) at the midpoint; hence \(\|Q\|_\infty=L^2/16\). Both the constant and first-order terms integrate to zero against \(\sigma\). Therefore
\[
 0\le E(X)=\int Q(s-a)\,d\sigma(s)
 \le \|\sigma\|_{\mathrm{TV}}\,\|Q\|_\infty
 =mL^2/16,
\]
which proves (C).

## Abstract optimality and exact finite checks

These claims concern **only finite signed measures with the two printed moment cancellations and nonnegative \(k\)**; they do not certify existence of corresponding smooth Hermitian data.

* **Global coefficient \(1/16\) is attained.** Take \(a=0\), \(b=L\) and \(\sigma=H\delta_0-2H\delta_{L/2}+H\delta_L\). It has zero mass and first moment, \(m=4H\), and \(k(t)=H\min(t,L-t)\) for \(t\in[0,L]\). Hence \(E(X)=HL^2/4=mL^2/16\).
* **Endpoint coefficient \(1/4\) is asymptotically optimal.** Fix \(0<d<L\), \(A>0\), and the piecewise linear nonnegative function
\[
 k_d(t)=
 \begin{cases}
 A(t-a),&a\le t\le a+d,\\
 Ad(b-t)/(L-d),&a+d\le t\le b,\\
 0,&\text{otherwise}.
 \end{cases}
\]
Let \(\sigma_d=k_d''\), a finite signed sum of three atoms. Then \(\sigma_d(\mathbb R)=\int s\,d\sigma_d(s)=0\), \(m_d=2AL/(L-d)\), and for \(h=d\),
\[
 \frac{\int_a^{a+h}k_d(t)\,dt}{m_d h^2/4}=1-\frac dL\longrightarrow1
 \quad(d/L\downarrow0).
\]
This proves that the abstract constant \(1/4\) cannot be reduced. The independent exact-rational small check under \`mathematical-audit/checks/check_degenerate_ma_energy_tv_bounds.py\` verifies these identities for several rational \(d/L\); the displayed proof does not rely on the check.

## Dependencies and correction recommendation

The geometric energy construction, existence of \(dd^cT\) as a finite signed measure, the two moment cancellations, and \(w_*E=k(t)dt\) all come from **Proposition 14.24.5**. Its proof uses bounded Bedford–Taylor products, local regularity and monotone continuity (§5.27), and weak convergence of regularizations, which have **not** been re-certified here. The downstream uniqueness theorem also invokes Lemma 14.24.11, the strict comparison argument of Proposition 14.24.2, modified comparison §14.19.6, and the auxiliary test-potential/Dirichlet argument of Proposition 14.24.13. None of these is certified transitively by (A)–(C).

**Proposed optional addition, audit-only:** after Equation 14.24.7, add the two endpoint layer estimates and the sharp global total-variation/oscillation estimate (with a clear conditional reference to the two moment identities). This is a strengthening of a correct statement, not a necessary error fix. No source text, production reading page, registry, canonical labels, or permanent tags have been changed.

**Coverage:** direct new quantitative proof check limited to §14.24.5, Eqs. 14.24.6–7 and printed proof lines 106–112; §14.24 was already partly audited. **+0 first-visited numbered sections, +0 entire-section certifications; actual ToC 25 chapters / 747 sections.** Demailly approximation/regularization and its Bergman/L²/Ohsawa–Takegoshi/multiscale/positivity-loss proof programme remain **deferred-by-user**, untouched.
