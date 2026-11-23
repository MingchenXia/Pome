# Scalar normalization: logarithmic-density spike sharpness and ramified bundle tests — 2026-11-23

## Baseline, current reading, and classification

Reviewed production **main**: \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`. Pre-review branch is read freshly before the atomic write. The mathematical text below comes from the *integrated reading edition*, not inferred from source numbering.

| Current ToC scope | Exact main path and blob | Mathematical HTML lines, status |
| --- | --- | --- |
| §11.30, Ramified section tests and a positive root metric | \`docs/sections/gauduchon-metrics-and-linear-mass--ramified-section-tests-and-a-positive-root-metric/index.html\`, \`1e52ae44b41ea9547ce2bf3f7e51b836772baf26\` | 7–109, entire direct review |
| §11.32, Normalization and weak adjoint measures | \`docs/sections/normalization-and-weak-adjoint-measures/index.html\`, \`031b5d62d25d7ff03d95e4a14988399527cc946a\` | 7–12, entire short introduction/standing hypotheses, not a theorem certification |
| §11.33, The scalar functional | \`docs/sections/normalization-and-weak-adjoint-measures--the-scalar-functional/index.html\`, \`fff86de757578ed2be369ba752123f62f3d31044\` | 7–117, entire direct review |
| §11.35, A convex functional on probability measures | \`docs/sections/normalization-and-weak-adjoint-measures--a-convex-functional-on-probability-measures/index.html\`, \`9a4ba5a98abd3273a6872c68beccf764e936d3f0\` | 7–82, entire direct review |
| §11.29, Projective first jets and positive bundle metrics | \`docs/sections/gauduchon-metrics-and-linear-mass--projective-first-jets-and-positive-bundle-metrics/index.html\`, \`1705a4387f533f89e80775bf5de4087c04d2e91b\` | selected only: 87–113 and 175–214 for the finite-dimensional and matrix-measure alternatives; NOT a whole review |

Specific tagged anchors:
- §11.33.2, source \`non-kahler-pluripotential-theory:6D175DAF\`, permanent \`2770AB03C0D2\`, physical lines 26–51; §11.33.4, \`547E9FD9\` / \`8810E18F852C\`, lines 61–78; §11.33.5, \`D502EBBF\` / \`5E3583383688\`, lines 88–117.
- §11.35.2, \`A1D8D375\` / \`0C21983AC42D\`, lines 20–39; §11.35.4, \`9F623A72\` / \`6830F8DE9750\`, lines 43–82; Eq. 11.35.5 source \`3339FE17\`, permanent \`FA8EC628AEAE\`.
- §11.30.1, \`D05FB6F6\` / \`8B6FA358A78D\`, lines 16–42; §11.30.3, \`AFFAD954\` / \`A8FAF022D4CA\`, lines 68–92; §11.30.5, \`7459D02A\` / \`9F9E99FDE392\`, lines 97–105.
- Only selected: §11.29.4 \`EF2A9F6A\` / \`07EC0797039C\`, lines 87–113; §11.29.9 \`A9DCA741\` / \`C334EF3CAF72\`, lines 175–214.

## POME-SCALAR-LOGDENSITY-SPIKE-LP-DISCONTINUITY-001

**Severity/status: low / verified conditional deduction (sharpness obstruction).** This is **not** a false printed theorem and **not** an unconditional certification of the general singular equation. It proves that the common uniform \(L^\infty\) bound in §11.33.5 cannot be dropped and replaced by convergence in *any finite collection, or even all,* finite \(L^p\) norms of the logarithmic densities.

**Exact model and hypotheses.** Take \(X=\mathbb P^1\), let \(\omega\) be a smooth Kähler form normalized by \(\int_X\omega=1\), put \(\theta=\omega\), \(\mathrm dV=\omega\), and take the bounded model potential \(\varphi=0\). These satisfy §11.32's connected compact positive-background, model-envelope, and smaller-background conditions. For any *individually bounded* measurable real \(F\), the existing bounded-density solvability of §15.12.1 provides a bounded solution of
\[
\omega+dd^c u=c_\varphi(F)e^F\omega.
\]
Regardless of which normalized solution is selected, integrating the current equation over the compact curve yields
\[
1=\int_X(\omega+dd^c u)=c_\varphi(F)\int_Xe^F\omega,
\qquad
\boxed{B_\varphi(F)=-\log\int_Xe^F\omega.}
\]
In complex dimension one, the equality uses only that \(dd^c u\) is an exact distributional current; no higher non-pluripolar continuity, approximation, Bergman or \(L^2\) proof is involved.

**Explicit sharpness family.** For each integer \(j\ge2\), choose a Borel set \(E_j\subset\mathbb P^1\) with \(\int_{E_j}\omega=1/j\). One may choose nested spherical caps, making the convergence almost everywhere as well. Fix any \(r>0\) and define
\[
F_j=\log(1+rj)\,\mathbf1_{E_j},\qquad F=0.
\]
Every individual \(F_j\) lies in \(L^\infty\), but there is no *common* \(L^\infty\) bound. For each fixed \(1\le p<\infty\),
\[
\|F_j-F\|_{L^p(\omega)}
= j^{-1/p}\log(1+rj)\longrightarrow0.
\]
Nevertheless the exponential integral is **exactly**
\[
\int_X e^{F_j}\omega
= (1-j^{-1})+j^{-1}(1+rj)=1+r,
\]
and hence
\[
\boxed{B_\varphi(F_j)=-\log(1+r)\ne0=B_\varphi(0)}
\quad\hbox{for every }j.
\]
The defect \(\log(1+r)\) can have any prescribed positive size. More strongly, taking \(r=r_j=j\) still gives \(F_j\to0\) in *every fixed finite* \(L^p\), because \(\log(1+j^2)j^{-1/p}\to0\), while \(B_\varphi(F_j)=-\log(1+j)\to-\infty\). The exponential densities have a fixed (or growing) mass concentrated on sets whose background volume vanishes: the missing hypothesis is not a cosmetic estimate.

**Disposition and dependents.** Theorem 11.33.5 (permanent \`5E3583383688\`) is correct *with* its uniform bound and is not challenged by these examples. An optional English sharpness remark should be proposed after that theorem, not inserted into main in this audit. Any extension of its continuity step, and later uses in §§11.35–11.38, must assume uniform integrability of \(e^{F_j}\) or another condition strong enough to prevent this concentration; \(L^p\)-convergence of \(F_j\) alone, however large finite \(p\), does not suffice. This is distinct from the earlier §12.9 smooth-Hessian oscillatory probability counterexample: here the *log densities themselves* converge strongly in every finite \(L^p\), but the scalar normalization fails.

## Other new direct mathematical checks

### §11.30, complete: ramified test threshold and root weight

For the double cover \(\pi:C\to\mathbb P^1\) given by \(w^2=\beta\in H^0(\mathbb P^1,\mathcal O(2q))\) with \(2q\) simple zeros (\(q\ge2\)), local simple ramification gives a smooth projective curve, and the rank-two direct image \(\pi_*\mathcal O_C=\mathcal O\oplus\mathcal O(-q)\) yields the two-summand section count in Lemma 11.30.1. The product with \(\mathbb P^{n-1}\) preserves the asserted tensor factor and dimension count. The complete linear system of \(L^q\) contains the ramification coordinate \(w\), separating tangent directions and yielding the strictly positive root metric.

At \(j=q-1\), the Fubini–Study basis makes \(\widetilde G_{j,I}=e^\phi|v|^2\) strictly psh. For \(0\le j<q-1\), all sections factor through the ramified base. At a branch point, §11.30.3 constructs a vertical vector \(\xi_v\) and a corrected horizontal vector \(\xi_h\) such that, before normalization,
\[
\widetilde\Psi_j(\xi_v)=e^{-j\phi}pp^*,
\qquad
\widetilde\Psi_j(\xi_h)=-j\kappa e^{-j\phi}pp^*,
\quad \kappa>0.
\]
If their squared \(b\)-norms are \(a_v,a_h\), the normalized matrices are \(A\) and \(-cA\), where \(c=j\kappa a_v/a_h\). The weights \(c/(1+c)\) and \(1/(1+c)\) annihilate their barycenter for \(j>0\); \(j=0\) has a single zero-matrix horizontal witness. This checks the Carathéodory separation direction and the **exact \(q-1\)** threshold. It does not certify all of §11.29's \(C^2\)-density argument, nor does it infer a first successful level for the *different*, \(q\)-spaced fixed-very-ample family of §11.29.

### §11.33, complete: sign of the scalar comparison

The factor in the strict domination contradiction of §11.33.2 is \(c(F)/c(G)<1\) when \(F\le G\) and \(c(F)<c(G)\); allowing arbitrary constant translates of one solution produces the contradiction, so \(B\) is **decreasing**. Constant shifts have the opposite sign, \(B(F+a)=B(F)-a\); the two essential-extremum bounds in Eq. 11.33.3 follow. The Gårding/mixed-product estimate in §11.33.4 uses AM–GM in the correct direction:
\[
\bigl(tA^{1/n}+(1-t)C^{1/n}\bigr)^n\ge A^tC^{1-t};
\]
therefore the result is **concavity**, not convexity. The convergence proof in §11.33.5 uses a *common* bound on \(F_j\) to control \(c_j\), the Monge–Ampère densities, and \(e^{F_j}\) in \(L^1\); the explicit spike example above isolates why this assumption matters.

### §11.35, complete: convex dual and uniform integrability

The Fenchel-like dual formula in §11.35.2 follows from the definition of the supremum and existence of a supporting probability in §11.34.2, without reversing the inequality. In §11.35.4, one first fixes \(t>0\), obtains a common small-\(L^1\) modulus from the *uniformly bounded family* \(t\chi\) (\(0\le\chi\le1\)), and then lets \(t\) be large compared with the dual sublevel \(L-B(0)+1\). Regularity of finite measures and continuous cutoffs transfer this to all Borel sets. The subsequent Lusin approximation of bounded Borel test functions plus uniform integrability correctly upgrades weak measure convergence inside a fixed \(H_\varphi\)-sublevel to weak \(L^1\) convergence of its densities; this does **not** assert strong \(L^1\) convergence.

### §11.32 and selected §11.29

The short §11.32 setting was read to check connectedness, compactness, the model potential, smaller-background premise, and notation \(\mathrm{MA}^{\mathrm{ext}}_\theta\). §11.29's compact convex-hull separation and atomic matrix-obstruction proof were checked only where directly used by §11.30. No inference about arbitrary noncompact/disconnected bases or first-level bounds has been introduced.

## Ledger status and limitations

- **New:** one low / verified conditional deduction (sharpness obstruction), no newly confirmed false printed mathematical theorem, no new proof-gap allegation, no genuine duplication or permanent-tag change.
- **Direct:** three complete substantive current sections §§11.30, 11.33, 11.35, one complete *short introduction* §11.32, selected §11.29. Historical first visits are **not** inferred from the legacy matrix.
- **Uncertified upstream inputs:** §§15.12.1, 15.2.2, 13.14.10, 15.9.4, 11.34.2 and the full §11.29 \(C^2\)-density chain; referenced here but not each independently proved. The \(\mathbb P^1\) scalar formula and spike arithmetic are complete conditional on existence of the bounded solution. Zero full transitive proof-chain certifications.
- **Deferred-by-user, NOT resolved:** Demailly approximation/regularization and the dedicated Bergman, \(L^2\), Ohsawa–Takegoshi, multiscale-atlas, positivity-loss proof-completion programme. Occasional existing historical mentions in integrated text are not a mandate to reopen it.
- **No production write:** no main/source/body/registry/canonicalization/tag/site edit; no Actions CI, publishing, merging, build or project test. No claim to have reviewed the other ToC sections.
