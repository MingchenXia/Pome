# Test-curve finite-join selection: a self-contained compact Choquet proof and uniform-in-parameter L1 convergence

**Date:** 15 November 2026. **Reviewed production main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. **Audit branch:** `review/mathematical-audit`.

**Finding:** `POME-TC-FINITEJOIN-UNIFORM-L1-001`. **Severity:** low. **Status:** **verified conditional deduction**, with a new self-contained *local* selection argument proposed as a proof replacement (not applied). The printed Proposition 17.15.31 remains a **true countable-selection statement** with its pre-existing **proof gap** `POME-TC-CHOQUET-DEAD-SLICES-001` still unresolved in the production reading edition. This report is neither a new disproof nor a certification of all upstream test-curve theory.

## Exact reviewed edition and stable anchors

- `docs/sections/test-curves--operations-on-test-curves/index.html`, main blob `3da617be8f58713f764d49ba22f49b803149a5e8`, standing assumptions on compact connected Kähler `X`, big smooth `theta` at **lines 5–10**; Corollary **17.15.17**, source `sgpt:8B734B07`, permanent `C8D1BA787705`, finite joins/order **lines 389–403**; Definition **17.15.20**, source `sgpt:0C7B668D`, permanent `4CC845CC4171`, uniform terminal bound **lines 505–522**; Proposition **17.15.22**, source `sgpt:7C36CCDA`, permanent `88665EBBD399`, increasing-net sup **lines 530–558**; Definition **17.15.25**, source `sgpt:BD3ECA71`, permanent `FA768FFB9E17`, finite-subset net **lines 592–613**; Proposition **17.15.28**, source `sgpt:6BC4C2B6`, permanent `C4A77DA880D9`, **lines 617–638**; Proposition **17.15.31**, source `sgpt:6B576942`, permanent `4B67ABC0083D`, statement **lines 662–665**, original problematic family **680–689**, reduction **693–718**.
- `docs/sections/test-curves--the-notion-of-test-curves/index.html`, main blob `6dfdfc2b5e599eb3a19a9558a9c963e79df71dc7`; Definition **17.12.1**, source `sgpt:ECCF19D5`, permanent `C8399F09D86D`, **lines 10–36** (normalized, concave decreasing slices); endpoint Remark **17.12.3**, source `sgpt:FCDC9660`, permanent `3D73AB2E32CB`, **lines 42–47**; rational left/right reconstruction Eq. **17.12.5**, source `sgpt:07C41068`, permanent `5EFADBE6069E`, **lines 71–78**.
- Context, not used as a quoted proof: `docs/sections/plurisubharmonic-functions--properties-of-plurisubharmonic-functions/index.html`, main blob `e7d871122eca3eb7416ab8a993063cdc8d3987f3`, Choquet Proposition **5.14.3**, source `sgpt:BAE53833`, permanent `1D624ECF05E9`, **lines 49–59**.

This is a mathematical consequence of the *actual integrated* finite-join and test-curve statements, not of a source theorem number alone. No Demailly regularization, Bergman, L2, Ohsawa–Takegoshi, multiscale-atlas or positivity-loss arguments are examined here.

## Precise new assertion

Let \((\Gamma^i)_{i\in I}\) be a nonempty family in \(\mathrm{TC}(X,\theta)_{>0}\) with
\[
 M=\sup_{i\in I}\Gamma^i_{\max}<+\infty,\qquad
 \Gamma=\operatorname*{sup}_{i\in I}{}^{*}\Gamma^i
\]
as defined by finite joins in §17.15.25. Fix **any** smooth strictly positive volume form \(dV\) on \(X\). There is a sequence of **nonempty increasing finite subsets** \(J_1\subseteq J_2\subseteq\cdots\subseteq I\), independent of the time parameter, such that for every compact interval \(K\Subset(-\infty,M)\),
\[
 \boxed{\quad
 \lim_{m\to\infty}\ \sup_{\tau\in K}
 \int_X\Bigl(\Gamma_\tau-
   \bigl(\bigvee_{j\in J_m}\Gamma^j\bigr)_\tau\Bigr)\,dV=0.
 \quad}
 \tag{A}
\]
The integrand is nonnegative almost everywhere, hence (A) is precisely **uniform \(L^1(dV)\) convergence on compact parameter intervals**. Every larger finite \(J\supseteq J_m\) satisfies the same upper error bound. This strengthens the countable-subfamily *identity* of the printed Proposition 17.15.31; it supplies no uniform **rate** or uniform estimate up to the terminal endpoint \(M\).

## Proof I: direct finite-join selection on one rational slice, without invoking Choquet's lemma

Fix \(q\in\mathbf Q\), \(q<M\). Choose \(i(q)\in I\) with \(\Gamma^{i(q)}_{\max}>q\). Let \(\mathcal F_q\) be the directed set of nonempty finite \(J\subset I\) **containing \(i(q)\)**, and write
\[
 u_J=\left(\bigvee_{j\in J}\Gamma^j\right)_q.
\]
By the actual finite-join corollary and definition of test curves, each \(u_J\) is a genuine \(\theta\)-psh function, **not** the identically \(-\infty\) function: its terminal parameter is \(>\!q\). All satisfy \(u_J\le0\) and \(u_J\ge u_{\{i(q)\}}\in L^1(X,dV)\), and the family increases under inclusion. Every omitted finite set \(H\) is dominated, at the \(q\)-slice, by \(H\cup\{i(q)\}\in\mathcal F_q\). Therefore
\[
 U_q=\operatorname*{sup}_{J\in\operatorname{Fin}(I)}{}^{*}
       \left(\bigvee_{j\in J}\Gamma^j\right)_q
     =\operatorname*{sup}_{J\in\mathcal F_q}{}^{*}u_J.
\]

Define \(A_q=\sup_{J\in\mathcal F_q}\int_Xu_J\,dV\), a finite number between \(\int_Xu_{\{i(q)\}}dV\) and \(0\). Choose \(H_m\in\mathcal F_q\) with \(\int_Xu_{H_m}dV>A_q-1/m\), and replace \(H_m\) by \(J_m(q)=\bigcup_{\ell\le m}H_\ell\). Then \(u_{J_m(q)}\) increases, its integrals converge to \(A_q\), and its pointwise increasing limit is finite almost everywhere. Write \(v\) for that limit and \(V=v^*\) for its upper-semicontinuous psh representative; monotone psh convergence gives \(V=v\) a.e.

For **any** \(J\in\mathcal F_q\), the finite-join order implies
\[
 u_{J\cup J_m(q)}\ \ge\
      \max\{u_J,u_{J_m(q)}\}.
\]
Consequently
\[
 0\le\int_X\bigl(\max\{u_J,u_{J_m(q)}\}-u_{J_m(q)}\bigr)dV
 \le A_q-\int_Xu_{J_m(q)}dV\longrightarrow0.
\]
As \(m\to\infty\), \(\max\{u_J,u_{J_m(q)}\}-u_{J_m(q)}
=(u_J-u_{J_m(q)})_+\) decreases to \((u_J-v)_+\) almost everywhere; its integrals converge by monotone/dominated convergence (e.g. it is bounded by the integrable \(-u_{\{i(q)\}}\)). Therefore \(u_J\le v\) a.e. A.e. order of \(\theta\)-psh functions implies order of their canonical usc representatives, so \(u_J\le V\) everywhere. Conversely \(V\le U_q\) from the definition of \(U_q\). Thus
\[
                 V=U_q.
                 \tag{B}
\]
This is an **independent compact-manifold Choquet selection proof** for this live finite-join family, based only on finite joins, elementary \(L^1\) monotone convergence and uniqueness of the psh representative. It does **not** apply §5.14.3 to the dead slices at lines 680–684 and does not inherit that general lemma's separately logged topological proof issue.

## Proof II: one common sequence and every real slice

Take the union over the countably many rational \(q<M\) of all finite sets \(J_m(q)\) above; call the resulting countable index set \(I'\). It contains \(i(q)\) for every rational \(q<M\), so \(\sup_{i\in I'}\Gamma^i_{\max}=M\). Enumerate \(I'\) into increasing nonempty finite sets \(J_m\), each eventually containing each fixed \(J_k(q)\). From (B), monotonicity of finite joins and the definition of the supremum,
\[
 \left(\bigvee_{j\in J_m}\Gamma^j\right)_q
       \longrightarrow\Gamma_q\quad\text{in }L^1(dV)
       \quad(q\in\mathbf Q,\ q<M).
       \tag{C}
\]
The \(L^1\) convergence follows from the increasing psh limit and the common live lower bound on sufficiently late \(m\); its usc representative is \(\Gamma_q\).

Fix \(K=[a,b]\Subset(-\infty,M)\). Choose \(b<b_1<M\) and \(i_0\in I'\) with \(\Gamma^{i_0}_{\max}>b_1\). For all sufficiently large \(m\), \(i_0\in J_m\). On all \(\tau\in K\), both \(\Gamma_\tau\) and
\(\Gamma^{J_m}_\tau=(\bigvee_{j\in J_m}\Gamma^j)_\tau\) lie between the *same* integrable lower bound \(\Gamma^{i_0}_{b_1}\) and \(0\). Outside the pluripolar set where that bound equals \(-\infty\), each of these parameter profiles is a finite concave function on an open interval containing \(K\), hence continuous in \(\tau\). Dominated convergence therefore gives \(L^1\)-continuity in \(\tau\) for \(\Gamma_\tau\) and for every sufficiently late \(\Gamma^{J_m}_\tau\).

For any fixed real \(\tau\in K\), choose rational \(q_-<\tau<q_+<M\). Decreasingness in \(\tau\) and finite-join order yield, for all sufficiently large \(m\),
\[
 0\le f_m(\tau):=\int_X(\Gamma_\tau-\Gamma^{J_m}_\tau)dV
 \le\int_X(\Gamma_{q_-}-\Gamma^{J_m}_{q_+})dV.
\]
By (C), \(\limsup_m f_m(\tau)\le
\int_X(\Gamma_{q_-}-\Gamma_{q_+})dV\).
Send \(q_-\uparrow\tau\) and \(q_+\downarrow\tau\), using the just-proved \(L^1\)-continuity of \(\Gamma\); the right side tends to zero. Thus \(f_m(\tau)\downarrow0\) at each \(\tau\in K\).

For large \(m\), \(f_m\) is continuous on the compact interval \(K\); finite-join monotonicity gives \(f_{m+1}\le f_m\) and the limit is the continuous zero function. **Dini's theorem** now yields \(\sup_{\tau\in K}f_m(\tau)\to0\), proving (A). No interchange of an arbitrary net with the \(\tau\)-limit, no sequential compactness of the original family, and no nonlinear Monge–Ampère continuity is assumed: the sequence is **constructed** by a countable rational selection.

## Review disposition and affected dependents

- **No new false theorem.** Original Proposition 17.15.31 is correct, but its printed dead-slice claim is still incorrect. The existing `POME-TC-CHOQUET-DEAD-SLICES-001` status is **proof gap**, **not resolved in main**. The preceding arguments offer an alternative replacement of that local invocation, and the additional uniform-\(L^1\) deduction. Proposed production correction: restrict each \(q\)-slice to live finite joins; optionally use the compact-integral selection argument above in place of the citation to §5.14.3. Keep all historical attribution and permanent tags.
- **Prerequisites used, not newly transitively certified:** finite join Corollary 17.15.17 (whose proof invokes §17.15.14 and earlier rooftop-envelope facts); increasing test-curve supremum §17.15.22; concavity/normalization of §17.12.1 and the elementary psh \(L^1\) representative fact. The selection itself does **not** need the general Choquet lemma or Monge–Ampère mass continuity. No claim is made of capacity convergence, continuity of nonlinear mass or full theorem/section certification.
- **Potential dependents:** uses of countable finite-join reduction in §§17.15.31–32, the Legendre/test-curve constructions of §17.17, and the relevant §22.1 non-Archimedean constructions. Uniform compact-time \(L^1\) may be used only where an \(L^1\) estimate suffices; it cannot silently replace a capacity or mass hypothesis.
- **Coverage:** new proof-level reasoning for the **previously partly audited** §17.15.17/.20/.22/.25/.28/.31 and §17.12.1/.3/.5; §5.14.3 checked as a distinct unused candidate. **Newly first-visited numbered sections: 0; wholly certified sections: 0.** Current main ToC remains **25 chapters / 747 numbered sections**. All existing resolved/unresolved/confirmed-error statuses retained, and all user-excluded approximation/regularization and dedicated Bergman/L2/OT/multiscale/positivity-loss work stays **deferred-by-user**. No main/body/registry/tags/build/tests/CI/site change or external publication.
