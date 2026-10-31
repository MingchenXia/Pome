# 2026-10-31 — Representation-independent Martin sweeping and nested compact reductions

**Reviewed production `main`:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. **Classification:** `POME-MART-SWEEP-PROJECTIVE-001` — **low / verified repair (proposed, not integrated)**. The original theorem is **not** shown false. This is a self-contained *local proof bridge conditional on the stated earlier reduction and interior-Riesz results*, not certification of the Martin representation theorem or its external topology inputs.

## Integrated reading-edition anchors (all at the reviewed main)

- `docs/sections/green-energy-and-martin-boundaries/index.html`, blob `976a90f2a5eba299658f73a1eee8b9d3fef8020f`.
- §4.5.10, Lemma, original source `classical-potential-theory:F432655F`, permanent tag `B0A113187C30`, physical lines **135–149**: for compact `C\Subset\Omega`, the compact reduction of a positive `K`-potential has a **unique interior** representing Riesz measure `μ_C`; `γ_{y,C}` is the compact reduction of a point boundary kernel and `T_C f(y)=∫ f\,dγ_{y,C}`.
- §4.5.11, Lemma, original source `classical-potential-theory:20921377`, permanent tag `FDE7BF6A9927`, physical lines **153–161**: nonnegative integral-sweeping and the barycentric identity `μ_C=∫_Δ γ_{y,C}\,dμ(y)`.
- §4.5.12, Theorem, original source `classical-potential-theory:57D18B4C`, permanent tag `6736FBE7368C`, physical lines **165–185**. **Exact proof hinge, line 176:** after choosing a subsequential weak limit `ν` of `μ_{C_j}` and proving `Kν=Kμ`, the proof uses `∫ f\,dν_{C_j}=∫ f\,dμ_{C_j}` inside its lattice argument, without explicitly demonstrating why two potentially *different* Martin-boundary representing measures have identical compact sweeps.
- §4.5.13, Theorem, source `classical-potential-theory:854603A2`, permanent tag `0E65F552B1A6`, lines **189–212**, is a conditional downstream user of the unique minimal Martin representation. Section `4.5.9` (source `classical-potential-theory:1677A9F0`, tag `9D6B5CF5E0CF`, lines 109–122) supplies the compact metrizable kernel setting and is not re-certified here.

## Precise local proof

Assume the §4.5.10–11 reduction construction and the interior Riesz-measure uniqueness stated there. Let $h\geq0$ be harmonic and let $\mu$ and $\nu$ be *arbitrary finite positive measures on the Martin boundary* such that

\[
K\mu=K\nu=h.
\]

No uniqueness of $\mu$ or $\nu$ is assumed; in particular, do **not** presume the conclusion of §4.5.12. For any compact $C\Subset\Omega$, by the definition of compact sweep and the fact that reduction depends only on the function,

\[
K\mu_C=\widehat R_C(K\mu)=\widehat R_C h
       =\widehat R_C(K\nu)=K\nu_C.
\]

Both $\mu_C$ and $\nu_C$ are supported *inside* $\Omega$, and are uniquely determined by their Green potential by the interior Riesz distributional identity. Hence

\[
\boxed{\quad \mu_C=\nu_C,\qquad C\Subset\Omega.\quad}
\]

This is independence of the choice of boundary representing measure, not uniqueness of that measure itself.

For two nested compact sets $C\subset D\Subset\Omega$, the elementary reduction absorption law gives

\[
\widehat R_C(\widehat R_Dh)=\widehat R_Ch.
\]

Indeed the reduction on $D$ is a superharmonic minorant of $h$ which agrees with $h$ quasi-everywhere on $D$; reduction on $C\subset D$ depends only on the quasi-everywhere obstacle there, and its lower-semicontinuous representative is canonical. Alternatively, the two elementary majorant comparisons for unregularized reductions, followed by regularization, give the same identity. Applying interior uniqueness again yields the **projective consistency of compact sweeps**

\[
\boxed{\quad (\mu_D)_C=\mu_C.\quad}
\]

The previous assertion requires only the established reduction regularization and quasi-everywhere stability; it does not assert convergence or uniqueness of arbitrary Martin boundary representing measures.

Using the §4.5.11 barycentric formula and Tonelli for positive measures, for every $f\in C(M)$ we obtain the representation-independent functional identity

\[
\boxed{\quad
\int_\Delta T_Cf(y)\,d\mu(y)
 =\int_\Omega f(t)\,d\mu_C(t)
 =\int_\Delta T_Cf(y)\,d\nu(y).
\quad}
\]

This explicitly justifies the equality used at line 176 of §4.5.12. It works even when $\mu\ne\nu$, so the existence proof does not circularly import the uniqueness that it is trying to establish.

### Direct insertion proposed for the proof of §4.5.12

After `Kν=Kμ` is established, insert:

> For every compact `C\Subset\Omega`, the measures `μ_C` and `ν_C` are both the unique interior Riesz measure of the same compact reduction `\widehat R_C(Kμ)=\widehat R_C(Kν)`. They are therefore equal, independently of any uniqueness of the boundary representing measure. By the integral-sweeping identity of Lemma 4.5.11, `\int T_Cf\,dν=\int f\,dν_C=\int f\,dμ_C`, which is the equality used below.

No change to the statement, tags, source attribution, normalizations, or canonicalization is proposed. The nested consistency statement may be added as an optional corollary; it is not needed for the minimal insertion.

## Audited scope, existing history and limits

This run inspected the exact compact-sweeping identities in §§4.5.10–11 and the representation-change step in §4.5.12, and checked §4.5.13 only as a downstream dependency. It did not reprove general reduction regularity, the compact-space representation construction, weak-limit existence, Stone–Weierstrass, or the rest of the Martin representation theorem. Those remain established internal/explicit general-topology inputs *conditional* for this local argument.

Unlike the preexisting `POME-MART-SW-001` (Stone–Weierstrass proof), `POME-MART-GDELTA-001` (topological classification), and `POME-MART-UNI-001` (caution against claiming unique arbitrary boundary measures), the present finding identifies and proves the **representation-independent compact-sweep identity** at the proof's exact lattice-equality hinge. Those older statuses stay unchanged. The printed theorem is not a false theorem, and no full-section mathematical certification is claimed.

**Coverage:** previously visited §4.5 receives an additional selected proof-level check only. Collection inventory remains **25 chapters, 747 actual numbered sections, zero whole-section mathematical certifications**. No tests, scripts, project build, CI, publication or formal proof were run. The user's excluded Demailly approximation/regularization, dedicated Bergman, `L^2`, Ohsawa–Takegoshi, multiscale-atlas and positivity-loss programmes were **not reopened**; their historical records remain `deferred-by-user`.
