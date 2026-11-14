# Explicit entropy-controlled logarithmic scalar stability (selected §§11.32–11.38)

**Audit date:** 2026-11-15 (Asia/Shanghai). **Reviewed production main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. **Audit branch:** `review/mathematical-audit`.

**Finding ID:** `POME-ADJOINT-ENTROPY-EXPLICIT-LOGMODULUS-001`. **Classification:** low / **verified conditional deduction**. **Printed results remain correct**; this is neither a false theorem nor a repair of an original proof. The result is an *explicit* uniform-in-reference version of the previously proved **implicit** $\Psi_{L_M}$ modulus `POME-ADJOINT-DUAL-UNIFORM-L1-001` (2026-10-24), not a re-registration of that result. The leading-order sharpness below concerns **general entropy-bounded probabilities**, **not** the particular PDE supporting measures.

## Exact current-reading-edition inputs

All paths are relative to repository root and refer to production main at the SHA above.

| Scope / exact label | Integrated HTML path, blob and physical line anchors |
| --- | --- |
| Standing hypothesis, source `non-kahler-pluripotential-theory:75571769`, permanent `7091FEDB43F0` (§11.32) | `docs/sections/normalization-and-weak-adjoint-measures/index.html`, `031b5d62d25d7ff03d95e4a14988399527cc946a`, lines 5–12 |
| Proposition 11.33.2, source `non-kahler-pluripotential-theory:6D175DAF`, permanent `2770AB03C0D2`; Theorem 11.33.5, source `D502EBBF`, permanent `5E3583383688` | `docs/sections/normalization-and-weak-adjoint-measures--the-scalar-functional/index.html`, `fff86de757578ed2be369ba752123f62f3d31044`, lines 27–51 and 89–117 |
| Theorem 11.36.1, source `non-kahler-pluripotential-theory:ECDF9BCE`, permanent `99653D7759E2`; supporting inequality 11.36.2, source `4DCA70F5`, permanent `F840087A1B81` | `docs/sections/normalization-and-weak-adjoint-measures--bounded-measurable-densities-and-stability/index.html`, `9c045c6e7a5bc4f0830874030c18dad0cafae905`, lines 10–20, 30–55 |
| Corollary 11.38.5, source `non-kahler-pluripotential-theory:F9E8E533`, permanent `A13D502ACAAC` | `docs/sections/normalization-and-weak-adjoint-measures--entropy-bounds/index.html`, `d124ce19af09af2d0a65d655fe611e7b45804c3d`, lines 99–132 (especially 103–107, 125–131) |

**Hypotheses retained.** Let $X$ be connected compact complex, $\mu=dV$ a *probability* smooth volume form (as normalized in §11.38), and $\theta$ a smooth semipositive big real $(1,1)$ form. Fix $0<\varepsilon<1$, and consider **only** those ordinary model references $\varphi$ satisfying the stated smaller-background hypothesis $P_{\varepsilon\theta}(\varphi)\not\equiv-\infty$. Use a Hermitian $\Omega\geq\theta$ as in Corollary 11.38.5. The corollary provides one finite constant $a_2$, depending on the fixed background and $\varepsilon$ but **not** on $\varphi$, such that
\[
 a_2+\tfrac12\operatorname{Ent}_{\mu}(\nu)\leq H_\varphi(\nu)
\]
for every probability $\nu$. Its proof gives $B_\varphi(U)\leq B_{\Omega,0}(U)$ on bounded logarithmic densities. Theorem 11.36.1 supplies an absolutely continuous supporting probability $\nu\in\mathcal A_\varphi(U)$, with exact dual equality
\[
H_\varphi(\nu)=B_\varphi(U)+\int_X U\,d\nu
\]
and the support inequality
\[
B_\varphi(V)\leq B_\varphi(U)-\int_X(V-U)\,d\nu.
\]
These established integrated statements, including their nonlinear PDE upstream inputs, are used **conditionally** and are **not** transitively re-proved here. No regularization, Bergman, $L^2$, Ohsawa–Takegoshi, multiscale or positivity-loss proof was opened.

## New explicit modulus

Fix $M>0$ and put
\[
 K=2M,\qquad C=B_{\Omega,0}(0)+2M,\qquad
 E=\max\{0,\,2(C-a_2)\}.
\]
These constants are **uniform in every admissible $\varphi$**. For real $F,G$ with $\|F\|_\infty,\|G\|_\infty\leq M$ put
\[
\delta=\int_X|F-G|\,d\mu,\qquad s=\delta/K\in[0,1].
\]
Then
\[
\boxed{\quad
 |B_\varphi(F)-B_\varphi(G)|
 \leq K\inf_{r>0}
 \frac{E+\log\!\bigl(1+(e^r-1)s\bigr)}r
 \quad (0\leq s\leq1).
 \quad}
\tag{A}
\]
At $s=0$, interpret the bound as zero by passing to $r\to\infty$; this agrees with the $L^\infty$-class interpretation. Independently, the elementary Lipschitz estimate gives $|B_\varphi(F)-B_\varphi(G)|\le K$.

Writing $L=\log(K/\delta)$, for $0<\delta<K/e$ we get the **entirely explicit** uniform estimate
\[
\boxed{\quad
 |B_\varphi(F)-B_\varphi(G)|
 \leq K\min\left\{1,
     \frac{E+1/L}{L-\log L}
 \right\}.
 \quad}
\tag{B}
\]
Consequently
\[
\limsup_{\delta\downarrow0}
\sup_{\substack{\varphi\text{ admissible}\\
 \|F\|_\infty,\|G\|_\infty\le M\\
 \|F-G\|_{L^1(\mu)}=\delta}}
\frac{\log(K/\delta)}K\,|B_\varphi(F)-B_\varphi(G)|
\le E.
\tag{C}
\]
The supremum over an empty constraint set is taken as zero. These statements give a concrete **$O(1/\log(1/\delta))$** modulus, in contrast to the earlier implicit $\Psi$ estimate; they do not assert that a PDE-specific logarithmic rate is optimal.

### Complete algebraic proof

1. **Common entropy budget.** For every supporter $\nu\in\mathcal A_\varphi(U)$ with $\|U\|_\infty\le M$, the translation rule and decreasing property of §11.33.2 imply $B_\varphi(U)\le B_\varphi(0)+M\le B_{\Omega,0}(0)+M$. Hence
   \[
   H_\varphi(\nu)=B_\varphi(U)+\int U\,d\nu\le C.
   \]
   Corollary 11.38.5 gives $\operatorname{Ent}_{\mu}(\nu)\le2(C-a_2)\le E$. Nonnegativity of entropy is compatible with the chosen maximum in $E$.

2. **Control of scalar increments by supporters.** Choose supporters $\nu_F,\nu_G$ supplied by §11.36.1. Apply its supergradient inequality once at $F$ and once at $G$, reversing the roles. Both inequalities together give
   \[
   |B_\varphi(F)-B_\varphi(G)|
   \le\max_{\nu\in\{\nu_F,\nu_G\}}\int_X|F-G|\,d\nu.
   \tag{D}
   \]

3. **Self-contained entropy variational bound.** Let $h=|F-G|/K$; then $0\le h\le1$ and $\int h\,d\mu=s$. For any probability $\nu\ll\mu$ and any $r>0$ define $Z=\int e^{rh}\,d\mu$ and $d\widetilde\mu=Z^{-1}e^{rh}\,d\mu$. The elementary relative-entropy inequality $D(\nu\|\widetilde\mu)\ge0$ (from $\log x\le x-1$) gives
   \[
   r\int h\,d\nu\le\operatorname{Ent}_\mu(\nu)+\log Z.
   \]
   By convexity of the exponential on $[0,1]$, $e^{rh}\le1+(e^r-1)h$, so $Z\le1+(e^r-1)s$. Combining with step 1, then (D), proves (A).

4. **Explicit choice of the parameter.** If $L=\log(1/s)>1$, take $r=L-\log L>0$. Then
   \[
   (e^r-1)s=L^{-1}-e^{-L}<L^{-1},
   \qquad\log Z\le\log(1+L^{-1})\le L^{-1}.
   \]
   Formula (B) follows from (A) and the $L^\infty$ bound; (C) follows on multiplying by $L$ and taking $L\to\infty$. No sequential extraction or interchange of a measure limit is used.

## Sharp information-theoretic limitation (not a PDE optimality claim)

For an arbitrary probability $\nu\ll\mu$ with $\operatorname{Ent}_\mu(\nu)\le E$ and a measurable set $A$ of $\mu$-mass $t\in(0,1)$, the log-sum inequality on the two cells $A,A^c$ yields, with $p=\nu(A)$,
\[
 \operatorname{Ent}_\mu(\nu)
 \ge p\log\frac p t+(1-p)\log\frac{1-p}{1-t}
 \ge p\log(1/t)-\log2.
\tag{E}
\]
Thus $p\le (E+\log2)/\log(1/t)$, an **explicit absolute-continuity modulus** for the *entire entropy sublevel*, and hence for the supporters considered above.

The leading logarithmic *order and coefficient $E$* cannot be improved for **arbitrary entropy-bounded probabilities**: on a nonatomic probability space select $A_t$ of $\mu$-mass $t=e^{-L}$ and the two-level density assigning $p_L=E/L$ mass to $A_t$ and $1-p_L$ to its complement. For fixed $E>0$ and all sufficiently large $L$,
\[
\operatorname{Ent}_\mu(\nu_L)
=p_L L+p_L\log p_L+(1-p_L)\log(1-p_L)
 -(1-p_L)\log(1-e^{-L})\le E,
\]
since the binary entropy term is negative with magnitude much larger than $e^{-L}$. For $|F-G|=K\mathbf1_{A_t}$ one has $\delta=Ke^{-L}$ but $\int|F-G|\,d\nu_L=KE/L$. This proves only the sharpness of the **entropy-to-integral mechanism** used in (A), not a lower bound for the PDE scalar $B_\varphi$ or an assertion that these $\nu_L$ occur in $\mathcal A_\varphi(F)$.

## Status, correction, dependents and coverage

- **Mathematical status:** verified conditional deduction; the printed §11.33.5 convergence and §11.36.1 support stability are correct; no confirmed source error or missing-proof claim. This is a stronger *explicit quantitative corollary*, conditional on the printed §11.36.1 and §11.38.5 and their recorded PDE prerequisites.
- **Proposed correction/addition only:** optionally add (B) after Corollary 11.38.5, with both uniform-reference and entropy-conditional qualifications; leave all printed statements, source tags and historical attribution intact.
- **Dependents:** scalar normalization and varying-density stability §§11.33, 11.36; reference-varying entropy estimates §§11.38–11.40. No transfer of full theorem certification to dependents.
- **Actually checked:** integrated §11.32 standing conditions, §§11.33.2/.5, 11.36.1, 11.38.5 and elementary entropy algebra; previous 2026-10-24 $\Psi$ modulus compared for non-duplication. **No first mathematical section visit** (all substantive selected proof inputs previously visited); **no complete-section certification**. Current main inventory remains **25 chapters / 747 numbered sections**.
- **Deferred-by-user:** all dedicated Demailly approximation/regularization, Bergman, $L^2$, Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof-completion work; prior notes remain neither fixed nor certified.
- **No operations claimed:** no project build, test suite, CI, source/body/tag/registry edits, merge or website publication.
