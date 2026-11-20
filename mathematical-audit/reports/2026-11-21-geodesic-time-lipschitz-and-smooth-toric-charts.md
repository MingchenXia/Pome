# Mathematical audit — weak geodesic time stability and smooth toric charts (2026-11-21)

## Baseline, precise scope, and exclusions

- Reviewed **main**: `b6933b772f41b45918f7e25ed1afbbb1fd892272` (not the audit branch).
- Full directly read integrated reading edition: `docs/sections/relative-energy-and-perron-segments--subgeodesics-and-perron-segments/index.html`, blob `662f60d73fc585b6ea3b710f2a3472bac1de8a7c`, physical lines 5–284 (§17.7), including original source tags `foundations-of-pluripotential-theory:424728F5` (Proposition 17.7.4; permanent `61A0C5DD7757`; line 101), `...:E4E82D7E` (Lemma 17.7.6, permanent `7B309BFF1A4D`; line 157), `...:108758A0` (Theorem 17.7.8; permanent `2FECBE87C487`; line 186), `...:470B93BF` (Proposition 17.7.9; permanent `DD04D189A4D3`; line 214), and `...:40348539` (Proposition 17.7.10; permanent `6DDFC01E2315`; line 256).
- Full directly read: `docs/sections/relative-energy-and-perron-segments--energy-along-weak-geodesics/index.html`, blob `8d9b7af925289346c96df751c67049e90c9dfe1d`, physical lines 5–125 (§17.8). Source/permanent tags: `foundations-of-pluripotential-theory:9DEC569D` / `950F051CF55A` (Lemma 17.8.1, line 11), `...:B2CECD86` / `3D0F1309E327` (Lemma 17.8.2, line 43), `...:907171A2` / `678A18D6D406` (Theorem 17.8.3, line 59).
- Full directly read: `docs/sections/convex-analysis-and-toric-potentials--smooth-lattice-polytopes-and-projective-charts/index.html`, blob `f442a7b663689b97a9b89689b8b7ae8b366a53fe`, physical lines 5–168 (§21.8); Lemma 21.8.2 original/permanent `foundations-of-pluripotential-theory:86BADE82` / `41C54729DBFD` (line 25), Theorem 21.8.3 `...:0F7315B0` / `E49F0370E203` (line 108).
- Selected cross-reference only: `docs/sections/convex-analysis-and-toric-potentials--fans-divisors-and-character-sections/index.html`, blob `7ad2e6dbdd0ce59e1bf08cd9cb3c046e8c87ff6c`, Theorem 21.9.5 and proof from physical line 139 onward (original `foundations-of-pluripotential-theory:BD98CC5B`, permanent `69D3D97E7701`). This is **not** a full §21.9 audit.
- All the user-excluded Demailly regularization/Bergman/L2/Ohsawa–Takegoshi/multiscale-atlas/positivity-loss proof-completion programmes remain **deferred-by-user**; no proof or prerequisite inside those programmes was revisited.

## Finding: POME-GEODESIC-TIME-LIPSCHITZ-INTERPOLATION-001

**Status:** verified conditional deduction. **Severity:** low (mathematical strengthening; no printed theorem is shown false). **Affected dependents:** the bounded-endpoint-difference regime of §§17.7–17.9; the finite-energy endpoint stability regime of §17.8.3. This does not assert verification of all their transitive dependencies.

### Statement (sharp temporal and endpoint stability)

Let \(X,\theta,\phi\) and \(\mathcal E(X,\theta,\phi)\) be as in Theorem 17.7.8. Assume \(u_0,u_1\in\mathcal E(X,\theta,\phi)\) and that, outside a pluripolar set, the difference is defined and
\[
|u_1-u_0|\le C,\qquad C\ge 0.
\]
For the weak geodesic \(G_t=G_t(u_0,u_1)\), with \(G_0=u_0,G_1=u_1\), and every \(s,t\in[0,1]\),
\[
\boxed{G_t\le G_s+C|t-s|,\qquad G_s\le G_t+C|t-s|.} \tag{A}
\]
These are inequalities of \(\theta\)-psh potentials, interpreted on the common finite locus (and hence as global inequalities of extended-valued functions). Consequently each finite fiber \(t\mapsto G_t(x)\) is **\(C\)-Lipschitz**, not merely locally Lipschitz away from \(0,1\).

More generally, if \(u_i,v_i\in\mathcal E(X,\theta,\phi)\) and \(|u_i-v_i|\le C_i\) quasi-everywhere for \(i=0,1\), then
\[
\boxed{|G_t(u_0,u_1)-G_t(v_0,v_1)|
 \le(1-t)C_0+tC_1} \tag{B}
\]
on the common finite locus; equivalently, both corresponding global psh inequalities hold. This is simultaneous endpoint perturbation stability with the **sharp affine weights**.

If additionally \(u_0,u_1\in\mathcal E^1(X,\theta,\phi)\), with model mass \(m=\int_X\langle(\theta+\mathrm{dd}^c\phi)^n\rangle\), then
\[
\boxed{|E_\theta^\phi(G_t)-E_\theta^\phi(G_s)|
 \le mC|t-s|.} \tag{C}
\]
For \(u_1=u_0+c\) with \(|c|=C\), all three bounds (with matching constant endpoint perturbations in (B)) can attain equality. For (A) and (C), use Proposition 17.7.9(6) and the energy translation law, respectively.

### Proof

Fix a point \(x\) outside the common pole locus and the pluripolar exceptional sets in the endpoint identification of Proposition 17.7.4. By Lemma 17.7.3 and that proposition, \(g(t)=G_t(x)\) is finite convex on \((0,1)\) and extends continuously to \([0,1]\) with \(g(0)=u_0(x)\), \(g(1)=u_1(x)\). The two lower barriers from Proposition 17.7.9(5) are
\[
g(r)\ge g(0)-Cr,\qquad g(r)\ge g(1)-C(1-r),\qquad 0\le r\le1.
\]
For \(0<s<t<1\), the elementary monotonicity of secant slopes of a convex function (Lemma 17.7.2(2)) gives
\[
\underbrace{\frac{g(s)-g(0)}s}_{\ge -C}
 \ \le\ \frac{g(t)-g(s)}{t-s}
 \ \le\ \underbrace{\frac{g(1)-g(t)}{1-t}}_{\le C}.
\]
Hence \(|g(t)-g(s)|\le C(t-s)\). Continuity handles the endpoints. Because a quasi-everywhere inequality between two \(\theta\)-psh functions extends everywhere (the comparison principle for quasi-psh representatives recalled in §16.11, *not* a Monge–Ampère comparison theorem), the two inequalities (A) hold as asserted, including at poles. No interchange of nets or limits is used.

For (B), the quasi-everywhere endpoint inequalities extend everywhere. Monotonicity of weak geodesics in Proposition 17.7.9(1) and the affine-constant covariance in Proposition 17.7.9(2) yield
\[
G_t(u_0,u_1)\le G_t(v_0+C_0,v_1+C_1)
 =G_t(v_0,v_1)+(1-t)C_0+tC_1.
\]
Reverse the roles of \(u_i\) and \(v_i\) for the other inequality. This proof does not assume bounded individual endpoints, only bounded pairwise differences.

For (C), by (A), \(G_s-\mathrm{const}\le G_t\le G_s+\mathrm{const}\) with constant \(C|s-t|\). Monotonicity of \(E_\theta^\phi\) on the finite-energy class and its translation rule \(E_\theta^\phi(w+a)=E_\theta^\phi(w)+am\) give (C). Theorem 17.8.3 supplies independently that \(t\mapsto E_\theta^\phi(G_t)\) is affine; (C) identifies its sharp global slope bound. For \(u_1=u_0+c\), Proposition 17.7.9(6) gives \(G_t=u_0+tc\), so the constant cannot be improved.

**Status boundary:** (A) and (B) use the stated existing weak-geodesic and quasi-psh comparison facts; (C) additionally uses the established energy monotonicity and translation facts. This is a complete deduction *conditional on those inputs*, **not** a stand-alone new existence or regularity theorem. Theorem 17.8.3's whole proof chain has not been re-proved here.

## Direct mathematical checks beyond the new deduction

1. **§17.7, §§17.7.2–17.7.10.** Checked the extended-valued convex-function alternatives, joint (not slicewise) psh requirement, countable extraction and Fubini in the Perron upper-envelope lemma, endpoint quasi-everywhere identification versus \(L^1\), cut-and-paste across seams, rooftop/end-point recovery, monotone endpoint limits, and affine obstacle representation. No new **confirmed** printed error found. In particular, the proof of (A) above does **not** infer pointwise endpoint identification from \(L^1\) alone; it uses the separately proved q.e. endpoint assertion.
2. **§17.8, §§17.8.1–17.8.3.** Inspected the locally bounded cutoff reduction for maximal psh functions and top non-pluripolar vanishing, group symmetrization of a local competitor, compact \(X\times\mathbb P^1\) gluing, mixed non-pluripolar mass/fiber pushforwards, radial harmonicity, and monotone finite-energy passage. The reduction invokes named prior results on capacity-weighted convergence, integration by parts, and fiber integration; their complete upstream proof chains are **not certified** by this reading. No new confirmed error is asserted.
3. **§21.8, §§21.8.1–21.8.3.** Inspected primitive edge lattice normalization, facet inequalities and tangent cones, vertex affine graph charts, homogeneous binomial equations, irreducibility via Laurent polynomials, and Fubini–Study curvature positivity. The apparent *forward reference* from the final paragraph of §21.8.3 to §21.9.5 is **not a circular dependence**: the §21.9.5 section-basis proof uses only the previously constructed vertex charts and Laurent expansions, not the very-ampleness conclusion of §21.8.3. This check is selected, not a full §21.9 review. No new confirmed printed error.
4. **Normalization check:** in each \(U_v\), the local Fubini–Study potential \(H_v=\log\sum_{m\in P\cap M}|w^{b(m)}|^2\) has the constant monomial \(1\) and the linear monomials \(w_1,\ldots,w_n\). Thus \(\bigl(\partial^2H_v/\partial w_j\partial\bar w_k\bigr)(0)=\delta_{jk}\), consistent with the strict positivity proof of §21.8.3 and the \(\mathrm{dd}^c\) convention. This is a check, not counted as a separate new mathematical finding.

## Dependencies, proposed actions, and disposition

- **Verified conditional deduction:** POME-GEODESIC-TIME-LIPSCHITZ-INTERPOLATION-001, low. Suggested *optional* body addition (not made here): a corollary immediately after Proposition 17.7.9 giving (A)–(B), and an energy consequence after Theorem 17.8.3. No tags or canonical identities need changing.
- **Open upstream proof dependencies (not newly found to be false):** §17.7 uses the psh-envelope theorem 5.10.2, endpoint compactness 17.4.3, rooftop/mass results 17.4.7/16.25.2; §17.8 uses the BT capacity-weighted continuity theorem 7.5.8, non-pluripolar fiber formula 13.6.1, bounded-difference integration-by-parts 17.2.5, and finite-energy passage 17.3.13; §21.8 uses convex separation 21.2.3 and the chosen 21.9.5/21.9.4 cross-reference. Do not infer transitive certification from this audit.
- **Resolved/unresolved/deferred accounting:** No printed theorem overturned or source repair committed in these sections; the new implication is proved conditional on the cited established statements. Other pre-existing unresolved entries remain unresolved. The entire specified Demailly proof-completion programme remains **deferred-by-user** and must not be relabeled as solved.

**Coverage increment:** three complete direct current sections (§§17.7, 17.8, 21.8), one selected current statement/proof (§21.9.5), **zero** fully certified transitive proof chains. Earlier visits have not been reconciled as first-time visits. No build, test, CI run, publication, GitHub Actions, or mathematical source/body/registry/tag modifications performed.
