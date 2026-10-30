# Sharp global L1 stability of the closed-class normalization scalar and its supporting probability

**Date:** 2026-10-31. **Finding:** `POME-CLOSED-LOGPART-SHARP-L1-TV-001`. **Severity / status:** low / **verified conditional deduction**. The printed statements checked here are **not false**, and this note is neither an upstream existence proof nor an integrated repair.

**Production main reviewed:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. **Audit branch:** `review/mathematical-audit`.

## Exact integrated anchors and prior dependencies

- `docs/sections/normalization-and-weak-adjoint-measures/index.html`, blob `031b5d62d25d7ff03d95e4a14988399527cc946a`, §11.32, physical line **7**: the fixed model reference and ordinary singularity type under a smooth semipositive big background.
- `docs/sections/normalization-and-weak-adjoint-measures--the-scalar-functional/index.html`, blob `fff86de757578ed2be369ba752123f62f3d31044`, Eq. **11.33.1**, source `non-kahler-pluripotential-theory:19974F5F`, permanent tag `9D47DB96B6E3`, physical lines **10–20**; Proposition **11.33.2**, source `:6D175DAF`, permanent `2770AB03C0D2`, lines **27–50**; Theorem **11.33.5**, source `:D502EBBF`, permanent `5E3583383688`, lines **89–116**.
- `docs/sections/normalization-and-weak-adjoint-measures--entropy-and-the-closed-case/index.html`, blob `0710d0732ae7ef81de3d3d62206a0f9c6b5d321f`, Eq. **11.37.2**, source `non-kahler-pluripotential-theory:65FF799F`, permanent `803909FECEC0`, lines **54–61**; Proposition **11.37.3**, source `:460EAE65`, permanent `33DF3CE1122A`, lines **65–75**.
- `docs/sections/non-pluripolar-products--mass-comparison-and-projective-fibers/index.html`, blob `dd89e44c511fd6f6bdd164a09a77c1637c42b410`, Theorem **13.8.7**, source `foundations-of-pluripotential-theory:6A80B686`, permanent `60DE4F681F75`, lines **218–245**. Its mass monotonicity is an **assumed internal theorem**, not independently certified in this increment; its dedicated regularization-related prerequisites are not reopened.
- Existence and uniqueness of the *normalization scalar* for the prescribed ordinary type are used from the cited Theorem **15.12.1(2)** (reader permanent `7AFA75E73767`), and are not reproved.

## Precise result

Let `X` be a connected compact **Kähler** manifold of positive complex dimension. Let `theta` be a smooth **closed semipositive big** real (1,1)-form (which need not itself be Kähler). Let `phi` satisfy the standing model-reference hypotheses of §11.32 and have strictly positive ordinary-type non-pluripolar mass `m_phi`. Assume the cited prescribed-singularity equation is solvable with its uniquely determined positive scalar `c_phi(F)` for every real `F in L^infty(dV)`. Write `V=int_X dV>0`, `Z(F)=int_X exp(F)dV`, `B_phi(F)=log c_phi(F)`, and `nu_F=exp(F)dV/Z(F)`.

**Closed-class extension of the printed Kähler-form identity:** for all bounded `F`,
```text
B_phi(F) = log(m_phi) - log Z(F),
A_phi(F) = { nu_F }.
```
In particular the entropy dual identity of Proposition 11.37.3 holds under the same assumptions, although the printed proposition only states the Kähler-form case. This extension is *conditional* on mass monotonicity and existence; it is **not** an assertion for nonclosed Hermitian forms.

**Sharp quantitative stability:** for any fixed `M>0`, and real bounded `F,G` satisfying `|F|,|G|<=M` almost everywhere,
```text
|B_phi(G)-B_phi(F)| <= [exp(2M)/V] ||G-F||_{L1(dV)},
d_TV(nu_F,nu_G) <= [exp(2M)/V] ||G-F||_{L1(dV)},
d_TV(mu,nu) = sup_{Borel E} |mu(E)-nu(E)|.
```
The common coefficient `exp(2M)/V` is **best possible separately for both inequalities** for this class of pairs. The bounds are independent of the fixed singularity type and its positive mass, once the scalar equation is available.

## Proof, including sharpness

1. For any two positive currents `theta+dd^c u` and `theta+dd^c v` with `u~v~phi`, each potential dominates the other modulo a constant. Theorem 13.8.7 in both directions therefore gives the same finite non-pluripolar mass `m_phi`; its projective/Kähler hypotheses apply to the ambient `X` and the closed background `theta`, even when `theta` is degenerate. Integrate Eq. 11.33.1 to obtain `m_phi=c_phi(F) Z(F)`. Differentiating the explicit logarithmic integral in bounded directions `H` yields `DB_phi(F)[H]=-int H dnu_F`. The known supporting inequality (with the sign convention of §11.34) and uniqueness under both signs of `H` identify `A_phi(F)={nu_F}`. Substitution into the dual definition, together with Lemma 11.37.1, gives the claimed entropy formula under the extended closed-class assumptions.

2. Set `H=G-F`, `F_t=F+tH`, `Z_t=Z(F_t)`, and `p_t=exp(F_t)/Z_t`, `0<=t<=1`. Since `|F_t|<=M`, `Z_t >= V exp(-M)` and `0<=p_t<=exp(2M)/V` almost everywhere. Differentiation under the integral is justified by boundedness and finite volume:
```text
d/dt B_phi(F_t) = -int_X H p_t dV .
```
Taking absolute values and integrating `t` proves the scalar inequality.

3. The probability densities `p_t` are differentiable in `L1(dV)`, with
```text
(d/dt)p_t = p_t (H - int_X H p_t dV).
```
Consequently, using `int p_t=1`,
```text
(1/2) int_X |(d/dt)p_t| dV
 <= (1/2)[int |H|p_t + |int Hp_t|]
 <= int |H|p_t
 <= [exp(2M)/V] ||H||_1 .
```
Integrate from `0` to `1`, apply the triangle inequality in `L1`, and use `d_TV=(1/2)||p-q||_1` for probability densities. No sequential compactness or limit interchange of singular Monge–Ampère measures is invoked in Steps 2–3.

4. To prove **both constants sharp**, use nonatomicity of the smooth positive measure `dV` (positive complex dimension). Let `E_a` be measurable with `dV(E_a)=a` for arbitrarily small `a>0`. Put
```text
F_a = M on E_a, -M outside E_a;
G_{a,eps} = M-eps on E_a, -M outside E_a, 0<eps<2M.
Z_a = a exp(M) + (V-a) exp(-M).
q_a = nu_{F_a}(E_a) = a exp(M)/Z_a.
```
Both inputs obey the `M` bound and `||F_a-G_{a,eps}||_1=eps a`. First take `eps downarrow0` at fixed `a`. The scalar ratio tends to `q_a/a=exp(M)/Z_a`; the TV ratio tends to `q_a(1-q_a)/a`, because on each of `E_a` and its complement the normalized densities are constant and the total-mass transfers are opposite. Then `a downarrow0` makes both ratios tend to `exp(2M)/V`. Hence no smaller universal coefficient is possible for either inequality.

These are finite-volume, bounded-density arguments. The only non-elementary inputs are the **explicitly declared** closed-class mass comparison and prescribed-type scalar existence; neither is certified here. In particular this does not solve the general nonclosed Hermitian scalar problem.

## Classification, interaction, and coverage

- **Status:** `verified conditional deduction` / low. The printed §§11.33.2, 11.33.5, 11.37.2, 11.37.3 are not falsified. The new step is a *sharp L1-to-scalar and L1-to-total-variation coefficient*, plus extending the explicit closed formula from a Kähler form to semipositive big closed backgrounds on a compact Kähler manifold.
- **Different from prior findings:** previous Kähler adjoint `tanh` TV estimates concern bounded **L-infinity perturbations**; this note treats the **L1(dV)** topology and its sharp global density-box modulus. The earlier general Hermitian §11.33.5 gives qualitative L1 sequential continuity, not the closed-case sharp estimate here.
- **Proposed optional addition:** a clearly conditional closed-class corollary after Eq. 11.37.2 and a reference in Theorem 11.33.5 explaining the stronger closed-class topology. Keep original Kähler statement, history, source labels and permanent tags; no canonicalization, source edit, or published modification.
- **Affected dependents:** supporting probabilities §11.34, dual entropy §11.37–11.38, and §11.33.5 closed-case stability. The open nonclosed Hermitian problems and the earlier scalar existence and comparison dependencies remain open where not verified.
- **Exact new mathematical coverage:** Eq. 11.33.1 normalization, one quantitative closed-class strengthening of Theorem 11.33.5, and Eq. 11.37.2/Proposition 11.37.3. The cited §13.8.7 mass theorem and §15.12.1 existence theorem were used as stated internal dependencies only. This is **not** the first reading of §11.33 or §11.37, and is **not** a complete mathematical verification of any section, chapter, theorem-chain, or project.
- **Matrix:** 25 actual chapters, 747 numbered current ToC sections, **0 fully mathematically certified sections**; all previously logged errors, proof gaps, candidates, external dependencies, duplicates and user-deferred items unchanged.
- **Strict user exclusion:** Demailly approximation/regularization and the dedicated Bergman, L2, Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof-completion programmes remain **deferred-by-user**, neither resolved nor reopened. We did not audit any of their prerequisites. No project tests, build, CI, website publication or formalization run.
