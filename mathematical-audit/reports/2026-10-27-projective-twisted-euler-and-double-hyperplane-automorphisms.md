# 2026-10-27 — projective twisted Euler polynomials and infinitesimal automorphisms of doubled hyperplanes

**Reviewed main commit:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.
**Starting audit head:** `e506fcdabac003a47bb5e3040f3989d9c03dcdf7`.
**Status boundary:** two low-severity *verified conditional deductions*; neither is a claim of a false printed theorem, a wholly certified source section, or a correction to the author's original mathematics.

## POME-PN-TWISTED-EULER-POLYNOMIAL-001 — low / verified conditional deduction

**Exact integrated locations:**

- `docs/sections/hodge-theory-curvature-and-compact-vanishing--twisted-differential-forms-on-projective-space/index.html`, main blob `1099020d78b8b36519f68ba31ce180c0d843f518`: definition and Euler contraction lines 7–30, Lemma 10.51.3, source label `demailly-complex-geometry-D4085D2A`, permanent tag `CA86EAF3228C`, lines 33–65; Proposition 10.51.5, source `demailly-complex-geometry-E45C60C7`, tag `74AA0E1253DB`, lines 70–90; Theorem 10.51.6, source `demailly-complex-geometry-EAA2912D`, tag `BEB304EB7449`, lines 94–139; its explicit top-form representation examples, lines 143–149.
- `docs/sections/hodge-theory-curvature-and-compact-vanishing--the-cohomology-of-spheres-and-projective-space/index.html`, main blob `a45ae3fefbf6746eca800f490163ac7ce2456c07`: Proposition 10.50.1, source `demailly-complex-geometry-F8CC338E`, tag `DD72F1B19307`, lines 10–28; Lemma 10.50.2, tag `2E46F3014687`, lines 32–44; Theorem 10.50.3, source `demailly-complex-geometry-81E1E8D3`, tag `558E1268EEED`, lines 48–88.

Let `V` be complex of dimension `n+1`, let `P(V)` parametrize lines, and let `O(k)` use the tautological linearization fixed in §10.51. For `0 ≤ p ≤ n`, define the generalized binomial `B(x,r)=x(x-1)...(x-r+1)/r!` for integers `r ≥ 0` (and `B(x,0)=1`). Then, **for every integer `k`, including negative twists and dimension zero**,

\[
\boxed{\chi\bigl(\mathbf P(V),\Omega^p(k)\bigr)
= \sum_{q=0}^n(-1)^q h^q\bigl(\mathbf P(V),\Omega^p(k)\bigr)
=\binom{k-1}{p}\binom{k+n-p}{n-p}.}
\]

**Proof from the precise cases of printed Theorem 10.51.6.** Assume first `n ≥ 1`. For `k>p`, only `H^{p,0}` survives and Lemma 10.51.3 gives the displayed positive dimension. For `1 ≤ k ≤ p` all groups vanish, and the first generalized binomial is zero. For `k=0` only `H^{p,p}=C` survives, giving `(-1)^p`; on the polynomial side `B(-1,p)B(n-p,n-p)=(-1)^p`. For negative `k` in the range `p-n ≤ k < 0`, all groups vanish, and `0 ≤ k+n-p < n-p` forces the second binomial to vanish (this interval is empty when `p=n`). Finally if `k<p-n`, only the top group survives, and printed Serre duality gives

\[
\chi=(-1)^n\binom{-k-1}{n-p}\binom{-k+p}{p}.
\]

The two universal polynomial identities

\[
\binom{k-1}{p}=(-1)^p\binom{-k+p}{p},\qquad
\binom{k+n-p}{n-p}=(-1)^{n-p}\binom{-k-1}{n-p}
\]

convert the formula into the claimed polynomial. For `n=0`, printed Theorem 10.51.6 gives one-dimensional `H^0(O(k))` for every integer `k`, and both zero-order binomials equal one. This settles all cases, with no Hirzebruch–Riemann–Roch invocation.

The polynomial has degree `n`, leading coefficient `1/(p!(n-p)!) = binom(n,p)/n!`, and zeros at `k=1,...,p` and `k=-1,...,-(n-p)` (empty ranges allowed). The sign reversal under Serre duality is the exact polynomial identity

\[
\chi(\Omega^p(k))=(-1)^n\chi(\Omega^{n-p}(-k)).
\]

These facts give a fully explicit Hilbert index polynomial whose leading coefficient agrees with `rank(Ω^p)∫ω_FS^n/n!` using the normalization in §10.50.3. The §10.50 proof's projective-space Mayer–Vietoris computation and direct volume integral were crosschecked; the `n=0`, `n=1` and finite-dimensional endpoint conditions are preserved. A small exhaustive **arithmetic** check over `0≤n≤7`, `0≤p≤n`, `-14≤k≤14` tested 1044 cases against all printed cohomology regimes with no discrepancy; this check is not a mathematical proof or a project test/build.

**Proposed change:** optional corollary after 10.51.6, stating the generalized-binomial convention explicitly and preserving the theorem's existing representation-theoretic `V`/`V*` distinctions. **Affected dependents:** twisted-index calculations, Euler characteristics, projective-space cohomology dimension checks; no existing claims are refuted.

**Dependency/verification limit:** the actual published Bott cohomology calculation is used as a conditional input. Its positive-twist case invokes Nakano tensor positivity from §§10.33–10.34 and Dolbeault from §10.43; its negative-twist case invokes analytic Serre duality §10.46.7; its `k=0` case invokes Hodge theory §10.47.13 and §10.50.3. Those upstream theorems have **not** been independently recertified here. No Demailly approximation or related excluded analytic programme was examined.

## POME-DOUBLE-HYPERPLANE-AUTOMORPHISMS-001 — low / verified conditional deduction

**Exact integrated locations:**

- `docs/sections/finite-type-algebraic-models-and-analytic-structure-sheaves--analytic-local-models-and-infinitesimal-information/index.html`, main blob `7a3c24deaab8602c3d2b4be2e31d739f02b5a657`; Proposition 9.60.1, source `demailly-complex-geometry-2090FB67`, permanent tag `57433F7B0D87`, lines 11–32, specifically the double-hyperplane self-map formulas at lines 11–13, 23–29.
- `docs/sections/finite-type-algebraic-models-and-analytic-structure-sheaves--finite-type-models-and-nilpotent-structure/index.html`, main blob `96eb7c1f6ee63ce6d222ed3f608a242a0a64b7f0`; Theorem 9.58.2, source `demailly-complex-geometry-3F3FF286`, tag `36502A11961A`, lines 12–27, and Proposition 9.58.3, source `demailly-complex-geometry-5EF3B92E`, tag `72F3ADBDFF9A`, lines 35–60. Their closed-point and nilpotent conventions were checked, not confused with all-prime spectra.

Fix the global model of the doubled hyperplane `D = (C^m, O_{C^m}[ε]/(ε²))`, `m≥1`, or its germ at a point. Proposition 9.60.1 describes every analytic endomorphism by

\[
F_{f,a,c}(z,\epsilon)=\bigl(f(z)+\epsilon a(z),\,\epsilon c(z)\bigr),
\]

where `f : C^m→C^m`, `a : C^m→C^m` and `c : C^m→C` are holomorphic (replace by germs for the local version). **The map is an analytic automorphism if and only if `f` is a biholomorphism and `c` is nowhere zero.** For a germ at the origin this means `f` is a local biholomorphism of germs and `c(0)≠0`; the source and target marked points must of course match.

**Proof.** An automorphism induces an automorphism of the reduction, so `f` must be biholomorphic. The nilradical sheaf is the square-zero ideal `(ε)`, and the induced map on that line over the reduction is multiplication by `c`; invertibility forces `c` to be a unit. Conversely suppose these two conditions hold and write `g=f^{-1}`. The explicit inverse is

\[
G(w,\delta)=\left(g(w)+\delta b(w),\,\delta d(w)\right),\qquad
d(w)=\frac1{c(g(w))},\quad
b(w)=-\frac{Dg_w\,a(g(w))}{c(g(w))}.
\]

Using `ε²=0`, both `G∘F` and `F∘G` are the identity: all terms beyond first order in `ε` vanish, and the remaining tangent term cancels by `Dg_{f(z)} Df_z=I`.

More generally, the **exact composition law** is

\[
F_{g,b,d}\circ F_{f,a,c}=
F_{\,g\circ f,\;(Dg\circ f)a+c(b\circ f),\;c(d\circ f)}.
\]

In particular, the kernel of reduction on the global automorphism group consists of all pairs `(a,c)` with `a` an arbitrary holomorphic vector field on `C^m` and `c` a nowhere-vanishing holomorphic function; for outer `(b,d)` after inner `(a,c)` its law is

\[
(b,d)\circ(a,c)=(a+c b,cd).
\]

The subgroup `c≡1` is the additive group of holomorphic vector fields. Thus the reduction map from automorphisms of the double hyperplane to automorphisms of the ordinary hyperplane is surjective but not injective, in a completely controlled way. For instance `(f,a,c)=(id,a,1)` with any nonzero `a` fixes all points and the reduced structure but not the nilpotent sheaf.

**Proposed change:** optional corollary following Proposition 9.60.1 with the global/germ qualifications and explicit inverse; no replacement of the original classification or of the crucial nilpotent structure sheaf. **Affected dependents:** nonreduced analytic automorphisms, reduction functor faithfulness and local embedding/infinitesimal structures. This is not a new proof of analytic coherence.

**Dependency/verification limit:** Proposition 9.60.1's analytic Nullstellensatz and coherent-radical inputs retain the previously registered `POME-ANMOD-ANALYTIC-COHERENCE-001` **external dependency / medium**; we neither close nor replay that finding. The self-map triple formula and its calculus are directly readable and checked independent of that external coherence proof. §§9.58.2–3 were incrementally crosschecked for Jacobson/closed-point localization and nilpotent sheaf conventions, not wholly recertified.

## Coverage, source integrity and exclusion boundary

First direct selected proof-level review of **§10.50.1–3** (Mayer–Vietoris, spheres, `P^n` and FS normalization) and **§10.51.1–6** (Euler contraction, dual pairing, polynomial horizontal forms, positive/negative twists, `n=0` exception), two previously *inventory-only* ToC rows. Incremental proof/calculus crosscheck of §§9.58.2–3 and 9.60.1; previously recorded `9.60` analytic-coherence external dependency remains open. `5.60`/`5.61` Skoda–El Mir and cycle-integration entries were consulted for potential duplication only and not claimed as new coverage. No complete section, analytic Serre duality, Hodge theory or other upstream machinery certified.

Both IDs are new and were checked against the existing ledger; the older twisted-bundle and analytic-monomial findings were not repeated. Keep the exact 747-entry chapter/section matrix, all old statuses, permanent tags, alternate canonical versions and existing net conventions. Nothing in this report asserts a false printed theorem or a completed proof replacement.

Dedicated **Demailly approximation/regularization**, Bergman, L², Ohsawa–Takegoshi, multiscale-atlas, and positivity-loss work remains **deferred-by-user**. No audit of those statements, no inference of their certification from references in the new sections, and no edits to `main`, source bodies, registries, publication, tags, CI, or GitHub Actions. The arithmetic check described above is the only newly executed small check; no project build, test suite, browser check or formal verification was run.
