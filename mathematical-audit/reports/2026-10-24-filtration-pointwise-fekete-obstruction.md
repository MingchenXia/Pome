# 2026-10-24 — Pointwise Fekete-limit obstruction for filtration test curves

**Finding:** POME-FILT-FEKETE-LIM-001. **Severity:** medium. **Status:** confirmed error in a displayed auxiliary identity; verified local repair by a limsup identity. **NOT** a counterexample to the construction of the maximal test curve or to the theorem about filtrations.

**Freshly inspected main:** b6933b772f41b45918f7e25ed1afbbb1fd892272. **Starting audit head:** 81bcb013b6d99e412145d5c113246bbcef767077. The review complies with main AGENTS.md and documentation/proof-expansions.md and with the existing audit-branch README.md, LATEST.md, ledger and current 747-section ToC inventory. Dedicated Demailly approximation/regularization, Bergman, L², Ohsawa–Takegoshi, multiscale-atlas and positivity-loss work remains **deferred-by-user**, not reviewed or certified here.

## Exact integrated reading-edition location

* Source file: docs/sections/test-curves--model-test-curves/index.html, main Git blob **e058100104283d27de55bc64b4ce784f66ace28b**.
* Definition 17.14.8: source identifier **sgpt-...** as displayed on the integrated page; reader permanent tag **D6CC0BBA6D35**; physical lines **144–185** (left-continuous, multiplicative, linearly bounded filtration).
* Example 17.14.10: source id **sgpt-780413CB**, permanent tag **20A8C7BFE0BB**, physical lines **191–272**.
* Equation 17.14.11: source id **sgpt-8C49F56B**, permanent tag **79C9CAB675E4**, physical lines **200–209**. The line immediately before the displayed equation invokes Fekete's lemma to claim an **ordinary pointwise limit**.
* Cross-checks: Proposition 17.14.6, permanent tag **BF40FB71C62C**, physical lines **91–131**; Remark 17.14.15, tag **497927DD4340**, lines **282–283**; the filtration comparison in §22.1 was consulted only for dependency orientation, not certified.

For the superadditive potentials
\[
a_k(x):=\Gamma_\tau^{\mathcal F,k}(x)\in[-\infty,0],
\qquad a_{k+\ell}(x)\ge a_k(x)+a_\ell(x),
\]
the printed equation asserts
\[
\lim_{k\to\infty}\frac{a_k(x)}k
=\sup_{k\ge1}\frac{a_k(x)}k
\quad(\tau<\tau(\mathcal F)).
\tag{printed 17.14.11}
\]
An extended-valued superadditive sequence need **not** have this ordinary limit.

## Fully algebraic-geometric counterexample

Let \(E\) be a smooth complex elliptic curve, \(M\) a line bundle of positive degree \(d\ge1\), and \(T\in\operatorname{Pic}^0(E)\) a **nontrivial line bundle of order two**. Let
\[
p:X=\mathbb P_E(\mathcal O_E\oplus M)\longrightarrow E
\]
use the Grothendieck **quotient-line** convention, with tautological quotient \(\mathcal O_X(1)\), and set
\[
L=\mathcal O_X(1)\otimes p^*T .
\]
The ruled surface \(X\) is smooth and projective. Its distinguished section \(S\simeq E\) corresponds to the quotient \(\mathcal O_E\oplus M\twoheadrightarrow\mathcal O_E\); hence
\[
L|_S=T,\qquad L^k|_S=T^k.
\]

This \(L\) is **big**. Indeed, the projective-bundle pushforward and the genus-one Riemann–Roch formula give
\[
\begin{aligned}
H^0(X,L^k)
&\simeq \bigoplus_{j=0}^k H^0(E,M^j\otimes T^k),\\
h^0(X,L^k)
&=\frac{d\,k(k+1)}2+\mathbf1_{\{k\text{ even}\}}.
\end{aligned}
\]
For \(j\ge1\), the corresponding summand has dimension \(jd\), while the \(j=0\) summand is \(1\) precisely for even \(k\). Thus \(\operatorname{vol}(L)=d>0\), and \(H^0(X,L^k)\ne0\) for every \(k\ge1\).

Equip \(L\) with **any** smooth Hermitian metric \(h\). Consider the elementary, trivial filtration
\[
\mathcal F^\lambda_k=
\begin{cases}
H^0(X,L^k),&\lambda\le0,\\
0,&\lambda>0.
\end{cases}
\]
It is decreasing, left-continuous, multiplicative, and linearly bounded with \(C=1\) in (17.14.9). Because every degree has nonzero sections, \(\tau_k(\mathcal F)=0\), so \(\tau(\mathcal F)=0\). Fix **any** \(\tau<0\). Then \(\mathcal F_k^{k\tau}=H^0(X,L^k)\) for all \(k\).

Take any point \(x\in S\). For every **odd** \(k\), the restriction to \(S\) of each global section of \(L^k\) is a global section of \(T\), and hence zero, since a nontrivial degree-zero line bundle on an elliptic curve has no global sections. Consequently
\[
\Gamma_\tau^{\mathcal F,k}(x)=-\infty\qquad(k\ \mathrm{odd}).
\]
This remains true after the upper-semicontinuous regularization in Example 17.14.10: in each finite-dimensional \(H^0(X,L^k)\), the global sup-norm unit ball is compact and evaluation vanishes identically on \(S\), hence its evaluation norm tends to zero near \(S\).

For every **even** \(k\), the \(j=0\) summand of the displayed direct sum supplies a section nonvanishing on \(S\). In particular, choose \(s_2\in H^0(X,L^2)\) with \(s_2(x)\ne0\), scaled to satisfy \(\sup_X|s_2|_{h^2}^2\le1\). Its \(m\)-th power is an admissible section of \(L^{2m}\), and therefore
\[
\frac{1}{2m}\Gamma_\tau^{\mathcal F,2m}(x)
\ \ge\ \frac12\log|s_2(x)|^2_{h^2}>-\infty.
\]
The normalized potentials are \(-\infty\) for every odd index yet uniformly bounded below along the even subsequence. **Their pointwise ordinary limit does not exist** at \(x\), contrary to (17.14.11), although \(L\) is big and \(\tau<\tau(\mathcal F)\).

This counterexample concerns the **pointwise** reading of the printed, unqualified limit; it does not exclude a distinct \(L^1\), almost-everywhere, or envelope interpretation, none of which is asserted or proved by the cited sentence.

## Exact local repair, including the extended-valued case

The following identity is valid for every superadditive sequence \(a_k\in[-\infty,\infty)\):
\[
\boxed{\displaystyle
\limsup_{k\to\infty}\frac{a_k}{k}
=\sup_{k\ge1}\frac{a_k}{k}.}
\tag{repaired 17.14.11}
\]
**Proof.** Write \(B=\sup_k a_k/k\). The upper bound on the limsup is immediate. If every \(a_k=-\infty\), both sides are \(-\infty\). Otherwise, for each \(m\) with \(a_m>-\infty\), superadditivity gives \(a_{rm}\ge r a_m\) for all \(r\ge1\); along the unbounded subsequence \(rm\), the normalized values are at least \(a_m/m\). Thus \(\limsup_k a_k/k\ge a_m/m\) for each such \(m\); take the supremum. \(\square\)

**Correction proposed, not integrated:** In the reading edition, change the initial \(\lim\) in Equation 17.14.11 to \(\limsup\) and replace “by Fekete's lemma” / “exists” with the elementary multiples-subsequence argument above. Preserve the equation's permanent tag, source attribution, normalization and all original filtration hypotheses. **Do not** silently interpret the printed ordinary limit as existing everywhere. If a full pointwise limit is desired, add and prove an eventual-finite/evaluation-semigroup hypothesis.

**Affected dependents and scope.** The **immediately following definition** of \(\Gamma_\tau^{\mathcal F}\) in Example 17.14.10 uses the **right-hand supremum**, not the nonexistent ordinary limit, and so this counterexample does **not** invalidate that definition, its subsequent concavity and full-mass arguments, Remark 17.14.15, or §22.1's use of the resulting curve. Those conclusions remain conditional on their other dependencies. This is a false **displayed formula/proof step**, not a proved counterexample to the main geometric construction. No full section or upstream section-growth theorem has been certified.

## Actual coverage and verification record

Directly read integrated §17.14 Definition .1, Propositions .2–.4, Definition .5, Proposition .6, Definition .8, Example .10 (the graded multiplication, rational interpolation, the printed limit, the supremum-envelope, and the later full-mass argument), and the concluding Remarks .14–.15. §17.11 and §21.1 are **section-title wrappers**, not independently certified mathematics. §22.1.94–.98 and .107–.113 were consulted selectively for dependencies but their deep GAGA, uniform generation and non-Archimedean extension inputs were not re-proved; no excluded Demailly programme was pursued.

The proof here is analytic-free apart from elementary geometry of elliptic curves, projective bundles and the explicitly displayed section counts; no numerical script, full build, CI, website publication or formal verification was run. This review creates **audit notes only**; source, tags, registries, published documents and main are left untouched. Existing ledger findings (including the distinct §22.1.88 concave-tail defect) retain their previous status.
