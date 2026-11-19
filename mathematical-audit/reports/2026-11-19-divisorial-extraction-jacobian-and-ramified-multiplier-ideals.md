# Divisorial extraction: a Jacobian-step bound and the finite-level ramification carry

Date: 2026-11-19. Scope: **selected direct audit** of §20.3.43–45 and the dependency use in §20.3.48; this is **not** a whole-section audit of §20.3, nor a certification of its transitive dependencies.

## Revision, provenance and exact inspected range

- Reviewed baseline: main commit **b6933b772f41b45918f7e25ed1afbbb1fd892272**.
- Integrated reading edition: `docs/sections/restriction-and-intrinsic-trace-data/index.html`, blob **dbc3b722ceacb8232fe4c7b711e5ad98b0708f06**.
- Main local source: `non-kahler-pluripotential-theory:5028932D`, permanent tag **C53A2B3087AB**, Lemma 20.3.44, lines **843–909**, particularly the base blowup/Jacobian decrease at **858–882** and ramified Lelong comparison at **884–908**.
- Equation source `non-kahler-pluripotential-theory:F47EE864`, permanent tag **09D69C0F18B7**, (20.3.45), lines **847–852**.
- Dependent theorem: `non-kahler-pluripotential-theory:E3D6C8A2`, permanent tag **63EC1D93ABC1**, Theorem 20.3.48 and its selected proof lines **925–966**, notably **938–945**. The separate exact trace, closed-background and envelope steps in this proof are *not* newly certified.
- The existing audit ledger and coverage matrix were checked for overlapping findings. These two precise refinements were not found there. Do **not** recount previously established §19.7 Hausdorff/semigroup or §11.5 results as this session's progress.

## Finding POME-TRACE-JACOBIAN-EXTRACTION-STEP-BOUND-001

**Severity:** low. **Status:** verified conditional deduction (not a confirmed error; the original extraction lemma is not refuted). **Input:** the smooth-base, dominant-map and divisor conditions of Lemma 20.3.44; local smooth-center blowup charts and the permitted resolution/principalization convention. No Demailly approximation or excluded analytic completion programme is used.

**Claim.** Consider the successive *codimension-at-least-two divisor-image blowups used in the printed proof* of Lemma 20.3.44. At stage \(j\), let \(c_j\ge2\) be the codimension of the smooth generic image center \(S_j\), and let \(m_j\ge1\) be the minimum of the normal pullback vanishing orders along \(D\). Then, for \(N\) such steps,
\[
 J_D(f_{\mathrm{initial}})-J_D(f_{\mathrm{after}\ N})
       =\sum_{j=1}^{N}(c_j-1)m_j.
\]
In particular
\[
 \sum_{j=1}^{N}(c_j-1)m_j\le J_D(f_{\mathrm{initial}}),
 \qquad N\le J_D(f_{\mathrm{initial}}).
\]
If the initial Jacobian order is zero, the divisor image is already a divisor or the whole target. The bound counts *these specific generic reduced-center extraction steps*, not arbitrary resolution blowups outside the general image point.

**Proof.** Work near a very general smooth point of \(D\). Choose local coordinates \(x_1,\ldots,x_{\dim Z}\) with \(D=(x_1=0)\), and target coordinates \(y_1,\ldots,y_r\) with \(S=(y_1=\cdots=y_c=0)\). Let \(m=\min_{i\le c}\operatorname{ord}_D(f^*y_i)\), and renumber so the minimum occurs for \(i=1\). The coefficient of \(x_1^m\) in \(f^*y_1\) is a unit after removing a proper analytic subset of \(D\). For \(i\le c\) all the ratios \(f^*y_i/f^*y_1\) are consequently holomorphic locally near that generic point. The map lifts to the chart of the blowup in which \(y_1=s\), \(y_i=s t_i\) for \(2\le i\le c\). The exact top-form identity is
\[
 dy_1\wedge\cdots\wedge dy_r
   =s^{c-1}\,ds\wedge dt_2\wedge\cdots\wedge dt_c
                  \wedge dy_{c+1}\wedge\cdots\wedge dy_r,
\]
up to a harmless sign. Pulling back to the source, and taking the smallest valuation among coefficients of the respective \(r\)-forms, gives the *equality*
\[
 J_D(f_{\mathrm{before}})=(c-1)m+J_D(f_{\mathrm{after}}).
\]
The latter order is a nonnegative integer because the lifted map is holomorphic in this neighborhood. Iteration telescopes; a stage with codimension \(\ge2\) costs at least one unit of the initial order. When no such step remains, the proper image of \(D\) is divisorial. This also verifies that resolving the target *away from the preserved smooth generic chart* does not insert an unaccounted local step.

**Sharpness for the stated algorithm.** The local map
\[
 (x,t)\longmapsto(y_1,y_2)=(x,x^Jt),\qquad D=\{x=0\},
\]
has \(J_D(f)=J\) because \(dy_1\wedge dy_2=x^Jdx\wedge dt\), and \(f(D)\) is the origin in \(\mathbb C^2\). After the \(k\)-th blowup at the point image on the relevant chart, the residual target coordinate is \(y_2/y_1^k=x^{J-k}t\). The image of \(D\) is still a point for \(k<J\); at \(k=J\) it is the exceptional divisor. Thus precisely \(J\) of the printed codimension-two steps are required. This germ is realized near the last exceptional divisor of \(J\) successive infinitely-near point blowups of a compact smooth surface such as \(\mathbb P^2\).

**Recommended optional explanatory addition (proposal only):** after the existing displayed Jacobian drop, record the telescoping bound above, distinguishing generic extraction steps from subsequent off-generic desingularization. **Affected use:** Lemma 20.3.44 supplies divisor extraction in Theorem 20.3.48; the new bound gives a checkable termination invariant but does not change the theorem's stated hypothesis/conclusion.

## Finding POME-TRACE-RAMIFIED-MULTIPLIER-FLOOR-001

**Severity:** low. **Status:** verified conditional deduction / exact local boundary example (not a false printed theorem). **Input:** local holomorphic ramification and the convention \(\mathcal I(\varphi)=\{g:|g|^2e^{-\varphi}\in L^1_{\rm loc}\}\). This computation is independent of any excluded approximation, Bergman, \(L^2\)-completion or Ohsawa–Takegoshi programme.

**Claim.** Let \(e\ge2\), \(c>0\), \(f(z_1,z')=(z_1^e,z')\), and \(w(y_1,y')=c\log|y_1|^2\). Along \(D=(z_1=0)\) and \(F=(y_1=0)\), for every \(t>0\),
\[
 \begin{aligned}
 \mathcal I(tw)&=(y_1^{\lfloor ct\rfloor}),\\
 \mathcal I(tw)\mathcal O_Z&=(z_1^{e\lfloor ct\rfloor}),\\
 \mathcal I(t(w\circ f))&=(z_1^{\lfloor ect\rfloor}),
 \end{aligned}
\]
and hence
\[
 \operatorname{ord}_D\mathcal I(t(w\circ f))
 -\operatorname{ord}_D(\mathcal I(tw)\mathcal O_Z)
       =\lfloor e\{ct\}\rfloor\in\{0,\ldots,e-1\}.
\]
The two ideals generally differ **at a fixed level** despite the exact asymptotic equality
\[
 \lim_{t\to\infty}\frac{\operatorname{ord}_D\mathcal I(t(w\circ f))}{t}
 =\lim_{t\to\infty}\frac{e\operatorname{ord}_F\mathcal I(tw)}{t}
 =ec=\nu(w\circ f,D).
\]
More exactly, the fixed-level ideals agree iff \(\{ct\}<1/e\); they differ whenever \(1/e\le\{ct\}<1\).

**Proof.** For a holomorphic function with generic vanishing order \(m\) on \((y_1=0)\), the normal complex-line factor of \(|g|^2e^{-tw}\) has polar integral
\(\int_0^\epsilon \rho^{2m-2ct+1}d\rho\). Finiteness is equivalent to \(m>ct-1\), or the integer condition \(m\ge\lfloor ct\rfloor\). This proves the first ideal identity. The pullback has normal order \(e\lfloor ct\rfloor\), whereas \(t\,w\circ f=ect\log|z_1|^2\) gives the third identity by the same radial integral. Write \(ct=\lfloor ct\rfloor+\{ct\}\) to obtain the *bounded carry* formula. Dividing by \(t\) and sending \(t\to\infty\) proves the asserted asymptotic agreement, consistent with (20.3.45).

For an explicit discrepancy take \(e=2\), \(c=1/2\), \(t=1\): the base ideal is the unit ideal but the pulled-back weight has multiplier ideal \((z_1)\). These germs can be globalized without changing the local computation by the branched map \(z\mapsto z^2\) on \(\mathbb P^1\) and a quasi-psh logarithmic pole of coefficient \(1/2\) at \(0\).

**Logical boundary.** Lemma 20.3.44 asserts functoriality of *coherent ideal orders under ordinary pullback* and of *divisorial Lelong numbers under quasi-psh pullback*. It does **not** assert the false equality \(\mathcal I(t(w\circ f))=\mathcal I(tw)\mathcal O_Z\). The displayed equality of asymptotic coefficients is a local illustration only; the bounded carry formula is **not** asserted for arbitrary singular residual weights or arbitrary maps. This distinction is relevant when using (20.3.42) and (20.3.45) in the divisorial chain at lines 938–945, but creates no contradiction there: those lines use ordinary pulled-back restricted ideals and *normalized* trace orders, not fixed-level multiplier-ideal commutation.

**Recommended optional explanatory addition (proposal only):** explicitly warn that a levelwise multiplier-ideal pullback identity is not available; show the \(e=2,c=1/2\) test in an audit note, leaving the integrated theorem unchanged. **Affected dependents:** readers comparing Lemma 20.3.44, trace orders in Theorem 20.3.2 and projective trace Theorem 20.3.48. No new proof of Theorem 20.3.2's analytic approximation dependencies is attempted.

## Audit disposition and coverage accounting

- **Original Lemma 20.3.44:** no confirmed error found in its selected local extraction and residual Lelong argument. The divisorial Lelong proof still invokes the internal non-strict Lelong level theorem (5.34.2), Skoda integrability and the permitted resolution input. Its full dependency chain is **not certified**.
- **Theorem 20.3.48:** directly checked the application of the lemma to \(q\circ\pi\) at lines 938–945 and the roles of ramification, ideals and divisorial coefficients. The separately needed exact base trace model (20.3.47), group-invariance descent, closed-background positivity and envelope dominance are **not certified** by this audit.
- **Coverage added:** +1 **selected partial** mathematical proof review in §20.3; +0 new fully checked sections; +0 newly certified full upstream chains. Historical first-visit status remains **unreconciled**, rather than being counted as a first visit. The repository's existing 25-chapter/747-section coverage matrix is retained.
- **Excluded programme:** Demailly approximation/regularization and its specified Bergman, \(L^2\), OT, multiscale-atlas and positivity-loss completion work remain **deferred-by-user**. Merely acknowledging the analytic approximants used elsewhere in §20.3 does not reopen or certify them.
- **Operational scope:** audit Markdown only, on `review/mathematical-audit`; no source, canonicalization, registry, permanent-tag, site, main, CI, test or build mutation.
