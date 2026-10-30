# Sharp affine endpoint stability for Perron segments and a directed-net subgradient theorem

**Audit date:** 2026-10-30. **Reviewed production \`main\`:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`.
**Audit scope:** new selected examination of the *integrated reading edition* §§17.16.2–7 and 21.11.63, not a complete review of either section or its dependency graph. Neither result below is an alleged false source theorem. No Demailly approximation/regularization, Bergman, \(L^2\), Ohsawa–Takegoshi, multiscale or positivity-loss programme was examined.

## POME-PERRON-AFFINE-ENDPOINT-CONTRACTION-001

**Severity/status:** low / **verified conditional deduction** (original §17.16.2, Proposition 17.16.6 and Theorem 17.16.7 remain correct; new sharp corollary, not a repair).

**Pinned production evidence:**
- \`docs/sections/perron-interpolation-and-the-geodesic-equation/index.html\`, main blob \`dc8dc381257360c94fe1c792499bb1ddf1bf5997\`.
- Standing setup (notably \(\theta\) smooth but **not required closed**) at physical lines 7, 20–29; affine invariance Proposition **17.16.2** at 32–40, source \`non-kahler-pluripotential-theory:16B06DB1\`, permanent tag \`1A5A4BBF82E3\`.
- Perron definition lines 67–75; largest-envelope and endpoint/restriction Proposition **17.16.6**, lines 78–102, source \`non-kahler-pluripotential-theory:071B00B3\`, permanent tag \`5D2A9C4885B8\`.
- Bounded-difference existence Theorem **17.16.7**, lines 109–138, source \`non-kahler-pluripotential-theory:CADEDF46\`, permanent tag \`66E38862017F\`; the proof uses the explicit maximum of two affine barriers. These are the exact proof steps checked, not an assertion that all prerequisites §5.24/§5.40 are independently certified.

**Statement and exact hypotheses.** Let \(X\) be a connected compact complex manifold, \(\theta\) any smooth real \((1,1)\)-form, and let
\[
 (u_0,u_1),\qquad (v_0,v_1)
\]
be two pairs of \(\theta\)-psh endpoints, with \(u_0\sim u_1\) and \(v_0\sim v_1\) in the *ordinary bounded-difference* singularity order. Assume that the respective endpoints have a common bounded comparison:
\[
 v_j+a_j\le u_j\le v_j+b_j,\qquad j=0,1,
 \qquad a_j,b_j\in\mathbb R.
\]
Here the inequalities are those of extended-valued \(\theta\)-psh functions. Because of the finite comparisons, all four have the same pole set; read differences only on its complement. By Theorem 17.16.7 both Perron segments \(P_t(u_0,u_1)\), \(P_t(v_0,v_1)\) exist. Then, for every \(0\le t\le1\),
\[
\boxed{
(1-t)a_0+ta_1
\le P_t(u_0,u_1)-P_t(v_0,v_1)
\le (1-t)b_0+tb_1.
}
\tag{1}
\]
In particular, if \(\lvert u_j-v_j\rvert\le\varepsilon_j\), \(\varepsilon_j\ge0\), then
\[
\boxed{\lvert P_t(u_0,u_1)-P_t(v_0,v_1)\rvert
\le(1-t)\varepsilon_0+t\varepsilon_1.}
\tag{2}
\]
The weights, including at both endpoints, are optimal. The estimates hold for Hermitian/nonclosed backgrounds just as for Kähler backgrounds: no energy integration-by-parts is used.

**Proof.** Denote the admissible family defining the Perron envelope with endpoints \(a,b\) by \(\mathscr A(a,b)\). If \(a\le a'\) and \(b\le b'\), the joint upper endpoint constraints imply the inclusion \(\mathscr A(a,b)\subseteq\mathscr A(a',b')\). Taking suprema and their upper-semicontinuous regularizations therefore shows the pointwise order preservation
\[
P_t(a,b)\le P_t(a',b')
\]
where these Perron segments exist. For constants \(c_0,c_1\), the operation \(V_t\mapsto V_t+(1-t)c_0+tc_1\) is a *bijection* between admissible families for \((a,b)\) and \((a+c_0,b+c_1)\): its complexification adds a pluriharmonic affine function of the strip coordinate (Proposition 17.16.2), and it shifts the joint upper boundary values by exactly \(c_0,c_1\). Hence upper regularization commutes with this continuous affine shift and
\[
P_t(a+c_0,b+c_1)=P_t(a,b)+(1-t)c_0+tc_1.
\]
Apply these two facts to the endpoint inequalities first with \((a_0,a_1)\), then with \((b_0,b_1)\), to get (1); taking \(a_j=-\varepsilon_j,b_j=\varepsilon_j\) gives (2). The inequalities are meaningful off the common pole set, and their extended-valued ordered versions remain true everywhere.

**Sharpness.** Choose any \(\varphi\in\mathrm{PSH}(X,\theta)\), for instance \(\varphi=0\) on a Kähler manifold with \(\theta>0\). Take \(v_0=v_1=\varphi\) and \(u_0=\varphi+b_0\), \(u_1=\varphi+b_1\). The affine path \(\varphi+(1-t)b_0+tb_1\) is a subgeodesic equal to the chord upper bound, hence is exactly its Perron segment. Equality in the upper estimate (1) holds *at every time*. Applying the same construction with \(a_j\) gives sharpness of the lower estimate. No smaller uniform coefficients can follow from the endpoint comparisons alone.

**Directed-net consequence (no sequential compactness):** for a directed family of endpoint pairs \((u_{0,\lambda},u_{1,\lambda})\) with each pair of bounded-difference type and \(\sup_{X\setminus P}\lvert u_{j,\lambda}-u_j\rvert\le\varepsilon_{j,\lambda}\to0\) for \(j=0,1\), the corresponding Perron segments converge uniformly jointly in space off \(P\) and in \(t\in[0,1]\), with exact error bounded by \(\max(\varepsilon_{0,\lambda},\varepsilon_{1,\lambda})\). This is a direct inequality for nets, not an application of sequential compactness.

**Proposed correction/addition:** no original correction required; an optional short sharp corollary after Theorem 17.16.7 can record (1)–(2) and net stability. **Potential affected dependents:** endpoint perturbation passages in §§17.7, 17.16 and Legendre/Perron comparisons in §17.17; none is hereby certified.

## POME-CONVEX-SUBGRAD-NET-SQUEEZE-001

**Severity/status:** low / **verified conditional deduction**, with a self-contained proof; the printed one-dimensional sequential Lemma 21.11.63 is **correct**, and is not repeated as an error.

**Pinned production evidence:** \`docs/sections/convex-functions-and-convex-bodies/index.html\`, blob \`2a123a863642a5a75caa173f0f73aff439a02ea4\`; Lemma **21.11.63** at physical lines **864–925**, source \`sgpt:F7AADC82\`, permanent tag \`66B643EAC79A\`. The printed proof uses the support-line inequality and one-sided difference quotients, lines 881–915. The separate earlier §21.11.20 dense convergence theorem is not assumed here.

**Sharpened theorem.** Let \(U\) be an open convex neighborhood of \(0\) in a finite-dimensional real vector space \(V\). Let \(f_\lambda:U\to\mathbb R\) be a **net** of finite convex functions indexed by a directed set and \(g:U\to\mathbb R\) an arbitrary function differentiable at \(0\). Assume, for every *fixed* \(x\in U\),
\[
 \limsup_\lambda f_\lambda(x)\le g(x),\qquad
 f_\lambda(0)\longrightarrow g(0),
\]
where \(\limsup\) uses tails of the directed set, not a sequence. Then, for every norm on \(V^*\) and every \(\epsilon>0\), eventually
\[
\boxed{
\partial f_\lambda(0)
\subseteq B_\epsilon(Dg(0)).
}
\tag{3}
\]
Each subdifferential is nonempty because \(f_\lambda\) is finite and convex on an open convex domain. Thus *every* choice of subgradients \(p_\lambda\in\partial f_\lambda(0)\) converges to \(Dg(0)\), whether or not any \(f_\lambda\) is differentiable at \(0\).

**Proof.** Choose a basis \(e_1,\ldots,e_d\) and \(h>0\) small enough that \(\pm he_j\in U\). For every \(p\in\partial f_\lambda(0)\), the supporting-hyperplane inequality gives
\[
 \frac{f_\lambda(0)-f_\lambda(-he_j)}h
 \le \langle p,e_j\rangle
 \le\frac{f_\lambda(he_j)-f_\lambda(0)}h.
\]
The upper-limit assumption and convergence at zero imply the *uniform-in-\(p\)* eventual bounds
\[
 \liminf_\lambda\inf_{p\in\partial f_\lambda(0)}
   \langle p,e_j\rangle
 \ge\frac{g(0)-g(-he_j)}h,\qquad
 \limsup_\lambda\sup_{p\in\partial f_\lambda(0)}
   \langle p,e_j\rangle
 \le\frac{g(he_j)-g(0)}h.
\]
The expressions are understood as tail infima/suprema; no compactness of subgradient selections is used. Differentiability of \(g\) at zero makes both difference quotients approach \(\langle Dg(0),e_j\rangle\) as \(h\downarrow0\). Given an accuracy, fix such an \(h\) and choose a tail on which both estimates hold for each of the finitely many \(j\); directedness supplies a common tail. Equivalence of finite-dimensional norms yields (3). This also works if \(g\) is **not convex**.

**Sharp necessity of differentiability at the touching point.** On \(U=(-1,1)\), let \(g(x)=|x|\) and \(f_k(x)=(-1)^kx\). Each \(f_k\) is affine, \(f_k(x)\le g(x)\) for all \(x\), \(f_k(0)=g(0)=0\), and both are convex; nevertheless \(f'_k(0)=(-1)^k\) does not converge. The differentiability of \(g\) cannot be removed from this convergence conclusion.

**Proposed correction/addition:** no amendment to the correct printed Lemma 21.11.63; an optional finite-dimensional, nonsmooth, directed-net strengthening can be added separately, preserving its label, historical attribution, and the original sequential statement. **Potential dependent uses:** convex Legendre/Monge–Ampère differentiability arguments in §§21.3, 21.5 and 21.11, and pointwise one-sided convergence situations; no claim of verifying their full proof chains.

## Scope and disposition

The new actual mathematical work is **selected** integrated reading-edition verification of §§17.16.2/.3/.6/.7, including the endpoint envelope/affine-change proof, and **new** detailed proof reading of §21.11.63 with the above independent strengthening; §21.11.20 is contextual only. Source labels and tags above are those of production main \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`. Neither finding is a defect of the printed theorems, neither is a full proof-chain certification, and neither repeats prior time-Lipschitz or convex-duality audit entries. Baseline inventory remains **25 chapters, 747 numbered table-of-contents sections, zero complete mathematical section certifications**.

All historical confirmed errors, proof gaps, candidates, external dependencies and repairs retain their earlier status. Demailly approximation/regularization and its dedicated Bergman, \(L^2\), Ohsawa–Takegoshi, multiscale-atlas and positivity-loss programme remain **deferred-by-user**, neither resolved nor certified. No mathematical body, source, registry, permanent tag or published document was changed. No project build, numerical experiment, CI, website publication or formal verification was run.
