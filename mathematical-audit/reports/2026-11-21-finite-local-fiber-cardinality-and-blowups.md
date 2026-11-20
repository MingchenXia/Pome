# Mathematical audit: analytic finite germs and blowups (2026-11-21)

**Baseline:** production `main` at `b6933b772f41b45918f7e25ed1afbbb1fd892272` (freshly read). **Audit branch:** `review/mathematical-audit` at pre-update HEAD `d43b8452b1dccde4e21dc945a3c17767b47ac2be`.

**Scope:** *complete direct reading of the visible integrated mathematical text* of §9.5, physical HTML lines 7–115, blob `2c725646172203283ac4564bddd46213d9a75cbe`, and §9.6, physical lines 7–124, blob `f452f4b1abe5cdfe348ae11fcd934febcfdd570b`. These are
`docs/sections/complex-spaces-and-modifications--analytic-curves-and-finite-maps/index.html` and
`docs/sections/complex-spaces-and-modifications--blowups-and-resolution/index.html`, respectively.
Selected prerequisites read from §9.3: Corollary 9.3.13(2) (finite smooth stratification), Lemma 9.3.15(1) (Hausdorff-null images of low rank), *not* a full §9.3 audit. Prior 2026-11-15 analytic arc-degree decomposition and earlier selected §9.6 pivot/discrepancy audits are retained; neither is counted as a new result.

## Finding POME-COMPLEX-FINITE-FIBER-COUNT-SEMICONT-001

- **Severity / classification:** low / **verified conditional deduction**. The printed Lemma 9.5.5 is **not false**; this is an explicit strengthening of its local finite-map conclusion, not a replacement proof of its prerequisites.
- **Primary anchors:** §9.5 Lemma 9.5.5, source identifier `CB1EA559`, permanent tag `776A532CD79E`, lines 84, 89–99 (especially rank/critical locus at 92–96 and proper local biholomorphism at 98). Additional §9.5 Lemma 9.5.4, identifier `0E97EB60`, permanent tag `FDF6E2ABDF34`, lines 72–79.
- **Assumptions:** \((X,x)\) a reduced pure \(d\)-dimensional analytic germ, \(d\ge1\); holomorphic \(F:(X,x)\to(\mathbb C^d,0)\); \(x\) isolated in \(F^{-1}(0)\). Let \(F:X'\to B_\varepsilon\) be a sufficiently small representative supplied by Lemma 9.5.5: it is proper, finite, and onto. No normality or irreducibility of \(X'\) is assumed.
- **Result:** There is a relatively closed \(\mathcal H^{2d-1}\)-null analytic critical-value set \(E\subset B_\varepsilon\) and an integer \(q\ge1\) such that
  \[
  \#F^{-1}(w)=q\quad(w\in B_\varepsilon\setminus E),\qquad
  1\le \#F^{-1}(w)\le q\quad(w\in B_\varepsilon).
  \]
  Moreover \(w\mapsto \#F^{-1}(w)\) is **lower semicontinuous** on \(B_\varepsilon\). Each \(w_0\) has a neighborhood \(V\) on which
  \[
  \#F^{-1}(w)\ge \#F^{-1}(w_0)\qquad(w\in V).
  \]
  In general this function is **not upper semicontinuous**.

### Complete justification of the additional conclusions

The proof of Lemma 9.5.5 constructs \(C=X'_{\mathrm{sing}}\cup\{\operatorname{rank}dF<d\text{ on }X'_{\mathrm{reg}}\}\), proves \(\dim C\le d-1\), and concludes that \(E=F(C)\) is relatively closed and \(\mathcal H^{2d-1}\)-null. It proves that \(F\) is surjective and is proper and a local biholomorphism on the preimage of \(B_\varepsilon\setminus E\).

A proper local biholomorphism with finite fibers is locally a **finite-sheeted covering**. Indeed, for \(w_0\notin E\), write \(F^{-1}(w_0)=\{y_1,\dots,y_s\}\). Choose disjoint open neighborhoods \(U_i\) of these points on which \(F\) is a biholomorphism onto a neighborhood of \(w_0\). After shrinking a target ball \(V\), no point of \(F^{-1}(V)\) lies outside \(\bigcup_iU_i\): otherwise choose \(w_j\to w_0\) and \(z_j\notin\bigcup_i U_i\) with \(F(z_j)=w_j\). Properness gives a convergent subsequence with limit in \(F^{-1}(w_0)\), a contradiction. Thus \(F^{-1}(V)=\coprod_i(F|_{U_i})^{-1}(V)\). The sheet number is locally constant off \(E\), and \(B_\varepsilon\setminus E\) is path connected by Lemma 9.5.4, so it equals one fixed integer \(q\ge1\).

For **any** \(w_0\in B_\varepsilon\), let \(F^{-1}(w_0)=\{z_1,\dots,z_m\}\). Choose pairwise disjoint neighborhoods \(U_i\) of these points in \(X'\). Since \(F\) has finite fibers, \(z_i\) is isolated in the fiber of the germ \((F-w_0):(X',z_i)\to(\mathbb C^d,0)\). Every germ \((X',z_i)\) is pure \(d\)-dimensional (the representative is pure-dimensional). **Apply Lemma 9.5.5 separately at each \(z_i\)**, choosing the new source representatives inside \(U_i\). For each \(i\), a ball \(V_i\ni w_0\) is covered by points of \(U_i\). On the intersection \(V=\bigcap_iV_i\), every fiber contains at least one point of each distinct \(U_i\), hence at least \(m\) points. This is the asserted lower semicontinuity. Because \(E\) has empty interior, choose \(w\in V\setminus E\), so \(m\le q\); surjectivity gives \(m\ge1\).

**Sharpness/direction:** for the proper finite map \(F:\Delta\to\Delta\), \(F(t)=t^q\) with \(q\ge2\), the fiber count is \(q\) at \(w\neq0\), and \(1\) at \(w=0\). Thus the lower-semicontinuity direction is sharp and the reversed upper-semicontinuity assertion is false. Fiber cardinality is not a multiplicity-weighted degree; this report does **not** assert preservation of an unweighted count across branch values.

**Proposed source addition (not applied):** after Lemma 9.5.5, optionally note the generic \(q\)-sheeted covering and lower semicontinuity of unweighted fiber count, citing the existing lemma and path-connectivity argument. **Affected dependents:** finite-projection arguments using §9.5.5 (including §9.5.6 zero-set purity); this only supplies additional control, not a needed correction to those arguments.

## Other mathematical content directly checked, without new verified finding

### §9.5, all six statements

- Proposition 9.5.1 (permanent `A3A9384DC317`, lines 11–36): connected punctured covering gives transitive cyclic monodromy, the \(t\mapsto t^q\) parameter, and regularity of normal complex curves. This requires irreducibility/connectedness; it was checked rather than replaced.
- Proposition 9.5.2 (`1497A0492453`, lines 41–50): the norm \(N\) of a nonzero germ is nonzero on a connected covering locus, and generic lines avoid \(\{\delta N=0\}\). Prior generic arc ramification result is **not** new here.
- Corollary 9.5.3 (`F7B8B4ADF874`, lines 55–64): one-variable maximum principle on normalized arcs, and the compact analytic subset contradiction via \(\sum|\gamma'_j|^2\).
- Lemma 9.5.4 (`FDF6E2ABDF34`, lines 72–79): the measure-zero cone-of-directions estimate and a two-segment path in the ball complement.
- Lemma 9.5.5 (`776A532CD79E`, lines 84–99): properness from isolation of the central fiber, finite fibers, rank-locus/critical-values estimate, and surjectivity. Selected §§9.3.13/9.3.15 were read to check the smooth-strata and Hausdorff-null inputs.
- Proposition 9.5.6 (`0E64BF4DC7C7`, lines 104–115): cutting a pure-dimensional germ by \(d-1\) generic linear forms, applying the finite map, and showing every zero-set branch has dimension \(d-1\).

### §9.6, all visible construction and existence clauses

- Definition 9.6.1 (`757D038DF549`, lines 11–19) and Proposition 9.6.2 (`1CAC94BB1C9D`, lines 23–36): reduced graph closure, properness, invertible pullback ideal, universal property, and canonical gluing.
- Proposition 9.6.3 (`865FE5EC97E6`, lines 50–78): explicit pivot charts \(w_i=t,\ w_j=tv_j\), Jacobian \(\pm t^{r-1}\), exceptional hypersurface, strict transforms and the exact identity \(I_W\mathcal O_{M'}=\mathcal O_{M'}(-E)I_{W'}\). The displayed identity assumes **\(C\subset W\) and positive codimension of \(C\) in \(W\)**; the disjoint-center case is correctly separate.
- Theorems 9.6.6 (`4CEF0578EFE0`, line 86) and 9.6.7 (`24330D25741D`, lines 91–96), and the deduction of log resolutions (lines 100–124): these are explicitly quoted Hironaka resolution/principalization inputs, **status: external dependency (permitted), not independently proved or certified**. The transform and normal-crossings support bookkeeping was checked conditionally on them.

**Classification:** No new confirmed error in either printed section. Neither a false theorem nor an independently certified full upstream chain is asserted. The present finding is a verified deduction *conditional on the printed finite-map lemma*. Earlier audited geometry, existing ledger entries, permanent tags and historical attribution remain unchanged. Demailly regularization/approximation and its excluded Bergman, L², Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof-completion programmes remain **deferred-by-user**; nothing here audits or reopens those programmes.

**Actual new coverage:** 2 complete direct reading-edition sections (§§9.5–9.6), 1 selected upstream section (§9.3.13 and §9.3.15 only), **0** completed transitive upstream-chain certificates. No claim of first historical visit. No software tests, manuscript builds, CI, website publication or production/source/registry/tag modifications.
