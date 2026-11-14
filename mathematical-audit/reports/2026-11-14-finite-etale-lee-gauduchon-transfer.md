# Finite étale transfer for Lee–Gauduchon and pseudoeffective Lee cones

**Finding:** `POME-LG-ETALE-TRANSFER-DUAL-CONE-001`. **Status:** verified conditional deduction; **severity:** low. **No theorem in the integrated reading edition is refuted.**

**Production baseline:** `main` commit `b6933b772f41b45918f7e25ed1afbbb1fd892272`. **Integrated source:** `docs/sections/locally-conformally-kahler-geometry/index.html`, blob `6ebf8e604b45d3eb748037af506145273ca3875d`. In particular, source `non-kahler-pluripotential-theory:19904244` / permanent `FC269BC81E64`, Definition 23.2.57 (physical lines 1036–1041); `non-kahler-pluripotential-theory:F88B67B6` / `EBFA309383E5`, Proposition 23.2.59 (1054–1080); `non-kahler-pluripotential-theory:B41AA0AF` / `DB27896B9A96`, Theorem 23.2.60 (1082–1111); `non-kahler-pluripotential-theory:63D571EA` / `D4DABE9DA177`, Lemma 23.2.62 (1119–1139); `non-kahler-pluripotential-theory:98212B61` / `ED85C468C237`, Lemma 23.2.63 (1144–1160); `non-kahler-pluripotential-theory:CDA139E7` / `403FA017D33B`, Theorem 23.2.64 (1162–1184); `non-kahler-pluripotential-theory:95E265D1` / `BF1CE00DF8A7`, Corollary 23.2.66 (1190–1205). The underlying chapter's displayed finite-dimensional duality is not being re-proved here.

## Precisely scoped statement

Let `p:Y -> X` be a **connected finite étale holomorphic covering of degree d>=1**, with `X,Y` connected compact complex manifolds of the same dimension `n>=2`. Write `V_Z=H^1_dR(Z,R)`, `K_Z=ker(j_Z)`, `C_Z={xi in V_Z : j_Z(xi) is pseudoeffective}`, and `LG(Z)={ [d^c(gamma^(n-1))] : gamma is a Gauduchon metric on Z }`, as in §§23.2.55–60. Then

1. `p_* LG(Y)=LG(X)` as sets in `H^(2n-1)_dR(X,R)` (ordinary zero-dimensional-fiber trace, **not** division by d);
2. `p^* C_X=C_Y intersect p^* V_X` and `p^* K_X=K_Y intersect p^* V_X`;
3. `0 in LG(X)` if and only if `0 in LG(Y)`, and **X admits a balanced Hermitian metric if and only if Y does**.

These do **not** assert `p^*V_X=V_Y` or identify the entire Lee–Gauduchon cones by pullback. That false analogy with the bimeromorphic case would require an unwarranted cohomological surjectivity assertion.

## Complete proof outside excluded scope

For a real differential form `alpha` on `Y`, define `p_* alpha` locally on an evenly covered open set `U subset X` by the finite sum `sum_{j=1}^d (p|_{U_j}^{-1})^* alpha`. Holomorphicity makes this construction preserve bidegree, reality, positivity, `d`, `d^c`, and `dd^c`. The definitions agree on overlaps. On forms on `X`, `p_*p^*=d id`. The same formula applies to currents by duality and preserves positive closed (1,1)-currents. Hence `p^*:H^1_dR(X,R)->H^1_dR(Y,R)` is injective, since `(1/d)p_*p^*=id`.

For any `gamma_Y` Gauduchon, put `Omega_Y=gamma_Y^(n-1)`. This is a smooth **strictly positive** (n-1,n-1)-form with `dd^c Omega_Y=0`. The finite trace `Omega_X=p_*Omega_Y` is again smooth and strictly positive: for every nonzero decomposable test vector of complementary degree, each lifted evaluation is positive and the finite sum is positive. Moreover `dd^c Omega_X=0`. The pointwise linear-algebraic (n-1)-st-root theorem, used in the proof of the integrated Proposition 23.2.59, gives a unique Hermitian form `gamma_X` such that `gamma_X^(n-1)=Omega_X`. Thus `gamma_X` is Gauduchon, and
`p_*[d^c Omega_Y]=[d^c(p_*Omega_Y)] in LG(X)`.
Conversely, start with any Gauduchon `gamma_X` and set `Omega_Y=(1/d)p^*(gamma_X^(n-1))`. It is a smooth strictly positive `dd^c`-closed (n-1,n-1)-form, so it too has a Gauduchon root. Its trace satisfies `p_*[d^c Omega_Y]=[d^c gamma_X^(n-1)]`. This proves **equality**, rather than just inclusion, in (1).

Let `xi in V_X` be represented by a smooth closed real one-form `lambda`. Holomorphic pullback gives `j_Y(p^*xi)=p^*j_X(xi)`. If `j_X(xi)` contains a positive closed (1,1)-current, so does its pullback by the local biholomorphism `p`. Conversely, if `j_Y(p^*xi)` contains such a current `T`, the current `(1/d)p_*T` is positive and closed and represents `j_X(xi)`: the trace commutes with `dd^c` and `(1/d)p_*p^*j_X(xi)=j_X(xi)`. Thus `xi in C_X iff p^*xi in C_Y`. The identical trace argument without positivity shows `j_X(xi)=0 iff j_Y(p^*xi)=0`. Together with injectivity this proves (2). Notice that the argument uses the trace of **cohomology classes**, not an unsupported equality of smooth potentials across different manifolds.

If `0 in LG(X)`, pulling back a Gauduchon (n-1)-power with zero `d^c)-class gives `0 in LG(Y)`. Conversely apply (1) to the zero class. If `X` is balanced, its strictly positive `d`-closed (n-1)-power pulls back to one on `Y`; if `Y` is balanced, the finite trace of its strictly positive `d`-closed (n-1)-power is a strictly positive smooth `d`-closed (n-1,n-1)-form on `X`, with a Hermitian root. This proves (3). **Do not replace the balanced conclusion by the generally unjustified converse `0 in LG iff balanced`.**

## Relation to Pome and disposition

The production Theorem 23.2.64 treats **modifications and bimeromorphic maps**, not finite coverings. Its proof uses degree-one cohomological isomorphisms; a finite cover in general only gives an injection in `H^1`. The present trace/pullback identities provide a distinct finite-map result and a self-contained check of the cohomological and positivity bookkeeping in §§23.2.55–66. There is no false theorem and no new proof gap asserted in those printed results. A nonproduction optional corollary can state (1)–(3), explicitly retaining the finite **étale** hypothesis: for ramified maps the trace of a smooth form need not remain smooth at the branch locus, so the proof does not transfer verbatim.

**Dependencies:** basic finite-cover differential-form trace, positivity of (n-1,n-1)-forms, and the unique Hermitian root invoked in §23.2.59. Historical attribution and all prior findings remain unchanged. No use of Demailly approximation/regularization, Bergman, L², Ohsawa–Takegoshi, multiscale atlases, or positivity-loss proof programmes. No source, registry, canonicalization, permanent tag, CI, or site changes are proposed. This local statement does not certify the full cone duality or the project.
