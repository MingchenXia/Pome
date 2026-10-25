# Uniform finite presentations behind the nuclear perturbation lemma

**Date:** 2026-10-25. **Reviewed main SHA:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. **Starting audit SHA:** `1cf916e662cd720ecc31f0ea084d4218d44312e0`. **Scope:** first selected integrated proof reading in §§9.41–9.43 and 9.45; incremental proof crosschecks in §§9.44, 9.46–9.47. Section 9.40 is an overview consulted for orientation only. These checks neither certify any complete section nor re-open the user-deferred Demailly approximation/regularization, Bergman, L², Ohsawa–Takegoshi, multiscale-atlas or positivity-loss programme.

## POME-RELNUC-BASECHANGE-FP-001

**Status:** verified conditional deduction. **Severity:** low (a mathematically substantive strengthening; the printed lemma is true, not false). **Recommended action:** optionally sharpen Lemma 9.46.3 to state a *uniform finite square presentation* under every allowed complete-Fréchet base change. No alteration of `main` or a source tag is authorized by this note.

**Exact source.** `docs/sections/analytic-tensor-products-and-proper-direct-images--relative-nuclearity-and-perturbation/index.html`, main blob `0a17de6159b423086dcfd306ba0734df57ff3bf7`, **Lemma 9.46.3**, source label `demailly-complex-geometry-B3B1AC10`, permanent tag `5C1AB5BDC27C`, physical lines 57–92. In particular the nuclear factorization is printed at lines 67–75; finite-index truncation, the Neumann inverse and its operator identity at lines 76–83; passage through actual (not necessarily Hausdorff) balanced quotients at lines 85–91.

**Precise strengthening.** Under *exactly* the printed hypotheses (unital Banach algebra `B`, Fréchet `B`-module `S`, `B`-nuclear endomorphism `v`), there are an integer `N>=0` and a `B`-linear endomorphism `K:B^N -> B^N` such that, for **every** continuous unital algebra homomorphism `rho:B -> C` into a complete Fréchet algebra for which the printed balanced base change is defined,
\[
 \operatorname{coker}(I-v_C)
 \simeq C^N/K_C(C^N),\qquad
 K_C=C\widehat\otimes_B K
 \quad(\text{the same finite matrix after }\rho).
\]
The isomorphism respects the *actual quotient topologies* even if either quotient is non-Hausdorff. In particular every such cokernel is **finitely presented as an algebraic `C`-module**, with one choice of `N` and one matrix over `B` valid simultaneously for all `C`; the printed lemma asserts only finite generation. There is **no** conclusion that the relation image is closed or that the quotient is a Fréchet space.

**Complete proof.** Use exactly the factorization in the printed proof: \(v=\beta\alpha\), \(\alpha:S\to L=\ell^1(B)\), \(\beta:L\to S\), and \(w=\alpha\beta\). Truncate the nuclear series so that
\[
 w=J\Lambda+w'',\quad
 J:B^N\to L,\quad \Lambda:L\to B^N,\quad
 \|w''\|<1 .
\]
The Neumann operator \(T=I_L-w''\) is a continuous \(B\)-linear automorphism of \(L\). Set \(Q=\Lambda T^{-1}:L\to B^N\) and the finite \(B\)-linear matrix \(K=I_{B^N}-QJ\). The **exact** identity
\[
 (I_L-w)T^{-1}=I_L-JQ
\]
shows that \(I_L-w\) and \(I_L-JQ\) have identical actual images, since \(T^{-1}\) is onto. The two maps \(Q:L\to B^N\) and \(J:B^N\to L\) induce mutually inverse maps on their cokernels: indeed
\[
 JQ=I_L-(I_L-JQ),\qquad
 QJ=I_{B^N}-K.
\]
Therefore \(\operatorname{coker}(I_L-w)\cong\operatorname{coker}K\). The original \(\alpha,\beta\) also induce inverse cokernel maps, since \(\beta\alpha=v\) and \(\alpha\beta=w\), and both endomorphisms act as the identity modulo the actual images of \(I-v\), respectively \(I-w\).

Every map and **both inverse identities** are continuous and \(B\)-linear *before quotienting*. Apply the functor \(C\widehat\otimes_B-\) by forming the actual completed-projective balanced quotient, exactly as justified at printed lines 85–91. Continuous maps and their composition identities descend; in particular \(T_C^{-1}\) remains the two-sided inverse of \(T_C\), and the free-factor collapse identifies \((B^N)_C=C^N\). The same algebraic identities yield
\[
 \operatorname{coker}(I-v_C)
 \xrightarrow[\alpha_C]{\simeq}
 \operatorname{coker}(I-w_C)
 =\operatorname{coker}(I-J_CQ_C)
 \xrightarrow[Q_C]{\simeq}
 C^N/(I-Q_CJ_C)C^N.
\]
The matrix \(Q_CJ_C\) is precisely \(\rho(QJ)\). All induced maps are continuous by quotient universality, and their displayed continuous inverses establish homeomorphisms even in the non-Hausdorff quotient category. There is no unjustified completion of the *cokernel*, no closure of relation images, and no topological open-mapping assertion on a non-Hausdorff quotient. This proves the claimed uniform finite presentation.

**Dependency boundary.** The only non-elementary input is the *existing* relative nuclear-series factorization/Neumann setup of Lemma 9.46.3; this note verifies its extra finite-matrix reduction, not the complete transversality theory. Lemma 9.46.3 is used by Theorem 9.46.5 (tag `741AFF17E7BD`), which then feeds the finite-free model of Theorem 9.46.7 (tag `71936EFE5494`) and the proper direct-image proof in §9.47.2 (tag `1A9A12704621`). A **quotient of a finitely presented module need not itself be finitely presented without additional control of its kernel**; accordingly this new conclusion must **not** be propagated automatically to Theorem 9.46.5, nor advertised as an independent proof of the proper direct-image theorem.

## POME-RELNUC-NONHAUS-COKER-001

**Status:** verified conditional deduction. **Severity:** low (explicit witness that a necessary caveat in the *correct* printed lemma is sharp). **Same source:** Lemma 9.46.3, lines 57–62 and 76–92; the non-Hausdorff warning is deliberate, not a source error.

Take the complex unital Banach algebra \(B=C([0,1],\mathbb C)\) with uniform norm, the Fréchet \(B\)-module \(S=B\), and let \(t(x)=x\). Define \(v(f)=(1-t)f\). This is \(B\)-nuclear **by one term**: \(v(f)=\xi(f)y\) with \(\xi=\operatorname{id}_B:S\to B\), bounded \(y=1-t\), and scalar coefficient \(1\). Thus
\[
 \operatorname{coker}(I-v)=B/tB.
\]
The ideal \(tB\) is not closed in \(B\). Indeed \(h(t)=\sqrt t\notin tB\), since \(h(t)/t=t^{-1/2}\) has no continuous extension to the origin, whereas
\[
 h_\varepsilon(t)=\frac{t\sqrt t}{t+\varepsilon}
   =t\frac{\sqrt t}{t+\varepsilon}\in tB,
 \qquad
 \|h-h_\varepsilon\|_\infty
 =\sup_{0\le t\le1}\frac{\varepsilon\sqrt t}{t+\varepsilon}
 \le \frac{\sqrt\varepsilon}{2}\longrightarrow0
\]
for \(0<\varepsilon\le1\), by \(t+\varepsilon\ge2\sqrt{t\varepsilon}\). Hence \(B/tB\) is a non-Hausdorff quotient of a Banach space, *even with no base change* (\(C=B\)). The matrix in the preceding finding can be taken to be the \(1\times1\) matrix \((t)\); finite presentation alone cannot force a closed image. This is not a counterexample to the printed theorem.

## Other new and incremental proof passages actually checked

- **First selected §9.41:** `docs/sections/analytic-tensor-products-and-proper-direct-images--completed-tensors-gluing-and-cohomology/index.html`, blob `c3c927f7b2b5b9adb40857b3fd11ef8680c5888e`. Lemma 9.41.1 (tag `8B7B03395780`, lines 11–65): contraction separates points of the injective completion, countable-product compatibility and the no-closed-range kernel formula; Corollary 9.41.4 (tag `50BD63BB3B28`, lines 71–82): sheaf gluing for completed nuclear tensor; Proposition 9.41.5 (tag `F635AEC8E8F7`, lines 87–105): Cauchy/density proof on products of polydiscs; Theorems 9.41.7/10 (tags `2A05F95A1DE7`, `52191CAACAB5`, lines 129–200): closed-range and finite-cohomology Künneth, with quotient-topology qualifications. No independent certification of the abstract nuclear exactness theorem §2.13.5.
- **First selected §9.42:** `docs/sections/analytic-tensor-products-and-proper-direct-images--coherent-analytic-applications-and-their-analytic-inputs/index.html`, blob `a292cc7f3a75c2891c0a48243f5f572874a8d77c`. Precisely the conditional analytic inputs at lines 7–32; Proposition 9.42.2 (tag `7BF5CAEB536D`, lines 36–50), double-Čech total comparison (lines 54–83), Corollaries 9.42.4–5 (tags `FAB99B827E4B`, `781692B04304`, lines 86–131). The Hausdorff and finite-dimensional cases have distinct hypotheses; they are not silently interchanged.
- **First selected §9.43:** `docs/sections/analytic-tensor-products-and-proper-direct-images--coherent-products-and-nuclear-analytic-modules/index.html`, blob `057ae61b984be97c533852e3be4f7964799be4e0`. Proposition 9.43.1 (tag `BDBDC4F6CABA`, lines 11–34): nonreduced quotient ideals and finite presentations; Proposition 9.43.2 (tag `3D82D215FD97`, lines 39–46): stalkwise exactness of filtered vector-space colimits for Godement direct images; Lemma 9.43.3 (tag `CE08E5D64C0A`, lines 51–58): compact coherent restrictions and nuclearity. The local analytic Cartan/Oka input remains a condition, not an extra certificate.
- **First selected §9.45:** `docs/sections/analytic-tensor-products-and-proper-direct-images--transversality-and-analytic-restriction/index.html`, blob `eb6d9e770e09bcc75557965a42a8d155ef780f7e`. Theorem 9.45.1 (tag `ED1150490F04`, lines 11–61): actual non-Hausdorff balanced quotient, base change and corrected cone signs; Proposition 9.45.4 (tag `8308DB03978F`, lines 66–79): coherent free resolutions on fixed compact product neighborhoods. Conditional on the source's coherent vanishing and exactness results; no transitive certification.
- **Incremental §§9.44, 9.46–9.47:** §§9.44.2–3 (tags `32299AAD67C6`, `C8C2118EE2C8`, blob `33c9658f92156b3f0676ea53e77715ef7fd06f49`, lines 17–69): free-bar contracting homotopy and actual quotient comparison; §§9.46.1–3/.5–7 (tags `4BBFDD591C1E`, `5C1AB5BDC27C`, `741AFF17E7BD`, `06B015B619A5`, `71936EFE5494`, main blob above, lines 17–161): relative nuclearity, finite-generation perturbation and finite-free model; §§9.47.1–2 (tags `81A3D17F4D37`, `1A9A12704621`, blob `94a7e39e68ce5dee99508213be822611b96db9d2`, lines 7–79): nonreduced diagonal graph and proper-image finite-cover argument. Prior §9.46.6 terminology candidate about “multiplicative” versus submultiplicative quotient seminorms is *not* repeated as new finding.

**Coverage and statuses.** Both new IDs are complete elementary deductions **conditional on the printed Banach nuclear factorization**, neither a false Pome theorem, corrected integration defect, nor independent proof of the entire §9.47 direct-image theorem. The existing resolved/unresolved/deferred ledger, all 747 current ToC inventory rows, permanent tags, original source records and prior notes must be retained. Nothing in this report requires or opens Demailly approximation/regularization, Bergman, L², Ohsawa–Takegoshi, multiscale-atlas or positivity-loss work; all remain **deferred-by-user**, not resolved. No build, CI, source/tag/registry/main/site edits or formal verification were executed.
