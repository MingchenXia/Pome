# Classical fine topology: countable polar sets prohibit nontrivial convergent sequences

**Audit date:** 2026-11-07. **Production main:** b6933b772f41b45918f7e25ed1afbbb1fd892272.
**Stable finding:** POME-FINE-POLAR-COUNTABLE-NOSEQUENCES-001.
**Classification:** low / **verified conditional deduction**. No printed theorem is false, and this is neither an independent certification of the full fine-potential theory nor a repair of its underlying propositions.
**Review branch:** review/mathematical-audit (audit Markdown only).

## Actual integrated text, source provenance and anchors

The main reading edition file is docs/sections/fine-topology-and-balayage/index.html, **Git blob d4c8eed09391441b4b6d13e2fa402a60da70be0d**, current section **4.2**, permanent section tag **8618E9B4AA3D**.

- Definition **4.2.2**, source label **foundations-of-pluripotential-theory:F5342A6A**, permanent tag **C067468FA3F0**, physical lines **29–37**, specifies the classical fine topology.
- Proposition **4.2.5**, source **foundations-of-pluripotential-theory:01F6C408**, permanent **9E787ECDB068**, physical lines **85–99**, proves that every fine neighborhood of a point has a positive-measure Borel portion in each sufficiently small Euclidean ball; in particular no point is fine-isolated.
- Proposition **4.2.6**, source **foundations-of-pluripotential-theory:1BE55D99**, permanent **498B2C3E2413**, physical lines **103–138**, proves that polar subsets are finely closed and are discrete in the fine subspace topology; its proof constructs a subharmonic potential finite at an arbitrary base point and equal to minus infinity at the other polar points nearby.
- The printed text at physical lines **140–141** explicitly records that all countable sets are polar in real dimension at least two, using Proposition 4.1.11.
- Example **4.2.8**, source **foundations-of-pluripotential-theory:3246187D**, permanent **4D234E8193AC**, physical lines **158–170**, proves failure of Lindelöf and second countability using an uncountable compact polar set; we compare its conclusion but do **not** recount or reprove that separate result here.

The supporting file is docs/sections/potentials-energy-and-capacity/index.html, **Git blob 4962a7cd576a64cb47fa0955dcc80cf87c3da9d1**. Proposition **4.1.11**, source **foundations-of-pluripotential-theory:7F3FDDFF**, permanent **64A94A9EE9E3**, physical lines **303–325**, asserts that countable unions of polar sets are polar. We read its local potential-and-positive-measure construction and Tonelli passage, but do not independently certify the Riesz-decomposition and basic-polarity dependencies.

## New deduction: every convergent fine sequence is eventually stationary

Let $\Omega\subset\mathbb R^d$ be a **nonempty open set**, $d\geq2$, with its classical fine topology. Assume precisely the three integrated inputs above: countable unions of polar sets are polar, polar sets are fine-closed and relatively discrete, and the fine topology has no isolated points. The following statements then all hold.

**(A) Every countable subset is fine-closed and relatively discrete.** A singleton is polar for $d\geq2$ (as recalled at §4.2, line 141). Thus a countable subset $S$ is polar by Proposition 4.1.11. Proposition 4.2.6 then says that $S$ is closed in the whole fine space and that its induced topology is discrete. Note that this does *not* say that the singletons of $\Omega$ are open.

**(B) Every fine-convergent sequence is eventually constant.** Suppose $x_j\to x$ in the fine topology. Form the countable set
\[
S=\{x\}\cup\{x_j:j\ge1\}.
\]
By (A), $S$ is a fine-closed discrete subspace. There is a fine-open set $N$ with $N\cap S=\{x\}$ (indeed Proposition 4.2.6 supplies a fine neighborhood with this property). Convergence implies $x_j\in N$ for all sufficiently large $j$. Since also $x_j\in S$, necessarily $x_j=x$ eventually.

The proof does **not** invoke sequential compactness or suppose that sequences characterize fine closure. It makes no assertion that nonconstant convergent **nets** do not exist.

**(C) No countable subset is dense.** Every countable $S$ is closed by (A), so its fine closure is itself. An open nonempty subset of $\mathbb R^d$ is uncountable, hence $\overline S^{\,f}=S\ne\Omega$. The classical fine topology is not separable.

**(D) No point has a countable neighborhood base.** Fix $x\in\Omega$ and suppose $(U_j)_{j\ge1}$ is a countable local base of fine neighborhoods. Each finite intersection $V_j=U_1\cap\cdots\cap U_j$ is a fine neighborhood of $x$. Proposition 4.2.5 says that $x$ is not isolated, so choose $y_j\in V_j\setminus\{x\}$. For every fixed fine neighborhood $N$ of $x$, some $U_k\subset N$ by the local-base property, and for $j\ge k$ we have $y_j\in V_j\subset U_k\subset N$. Thus $y_j\to x$ finely, contradicting (B), since every $y_j\ne x$. So the space is nowhere first countable.

**(E) The fine topology is not sequential.** By (B), a limit of a sequence from any subset $A\subset\Omega$ must belong to $A$: the sequence is eventually its limit. Thus *every subset is sequentially closed*. But $\Omega\setminus\{x\}$ is not fine-closed, because its complement $\{x\}$ is not fine-open by Proposition 4.2.5. Therefore sequentially closed sets need not be closed, and the space is not sequential.

**(F) Countable tightness fails at every point.** Since $x$ is not isolated,
\[
x\in\overline{\Omega\setminus\{x\}}^{\,f}.
\]
For every countable $S\subset\Omega\setminus\{x\}$, (A) yields $\overline S^{\,f}=S$, which does not contain $x$. Thus no countable subfamily witnesses this particular closure relation. This explicitly exhibits failure of countable tightness, a stronger obstruction than mere non-first-countability.

These deductions are compatible with the quasi-Lindelöf theorem of §4.2.22: reduction to a countable subfamily **outside a polar exceptional set** is different from ordinary Lindelöfness, sequentiality or countable tightness. They are also compatible with the separately established density-one fine-neighborhood estimate; the Lebesgue density topology is a different topology.

## Mathematical status and proposed treatment

**What was proved here:** the six elementary implications (A)–(F) with all quantifiers, including a construction of the hypothetical convergent sequence from a countable local base. No limit interchange, sequential-closure criterion or transfer to the plurifine topology is assumed.

**Conditions still dependent on earlier internal proofs:** general polarity closure (§4.1.11), the polar-neighborhood construction (§4.2.6), and nonisolation (§4.2.5). These are identified *internal mathematical inputs*, not historical attribution; their full transitive proofs remain outside this narrow review. They are not part of the user-excluded Demailly regularization programme.

**Production correction:** none necessary; all printed assertions are consistent with (A)–(F). An optional, separately reviewable explanatory remark after §4.2.8 could state: “Every countable subset is fine-closed and discrete, so no non-eventually-constant sequence converges in the fine topology; despite this, the space has no isolated points and is nowhere first countable.” No source, body, registry or permanent tag was modified.

**Potential dependents:** §4.2.22–23 (Choquet/quasi-Lindelöf and fine-open measurability), §4.4 (fine-boundary convergence), and §5.47 (comparison with plurifine topology). In those contexts, one must not replace nets/topological closure by sequences. This report does **not** assert that the plurifine topology inherits any of these properties automatically.

## Exact coverage and preservation

Newly inspected selected statements: §4.2.5 and **§4.2.6**, with the §4.2.2 definition, §4.2.8 comparison and §4.1.11 source of countable-polar closure. §4.2 and §4.1 were **already partly audited**; this is a new *selected mathematical implication*, not a first visit or full section certification. The coverage baseline remains **25 chapters, 747 numbered current-ToC sections, zero complete mathematical-section certifications**. Other findings in the resolved/unresolved/deferred ledger retain their prior classifications; this item is an additive conditional deduction and does not settle their general prerequisites.

The owner-excluded Demailly approximation/regularization, dedicated Bergman, weighted $L^2$, Ohsawa–Takegoshi, multiscale atlas and positivity-loss programme remain **deferred-by-user** and are neither revisited nor certified. No project tests, builds, GitHub Actions, formalization, main-branch changes, source edits, PRs, merges or website publication form part of this result.
