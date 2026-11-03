# Gauduchon persistence: an exact two-form test and a non-Kähler Hopf-product model

**Date:** 2026-11-03. **Reviewed production main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.

**Finding:** `POME-HERM-GAUD-PERSIST-TWO-TORSION-001`; **severity low**; **status verified conditional deduction**, not a false printed statement and not a complete upstream proof certificate. This is a new smooth differential-form characterization and example. It does **not** reopen Demailly approximation/regularization, Bergman, weighted L², Ohsawa–Takegoshi, multiscale or positivity-loss work.

## Integrated reading statements and stable anchors

- `docs/sections/gauduchon-metrics-and-linear-mass--the-adjoint-measure-of-the-linearization/index.html`, main blob `519e50338be6560f6b2856fddce212738f5109bc`: Proposition **11.23.4**, physical lines **58–76**, source `non-kahler-pluripotential-theory:B9B9F692`, permanent tag `A914D4D9C6CB`; adjacent Example **11.23.5**, physical lines **78–99**, source `non-kahler-pluripotential-theory:324594DA`, permanent tag `28F39F2B7C2C`. The subsequent paragraph invokes the separately stated power identities of §11.1.7.
- `docs/sections/gauduchon-metrics-and-linear-mass--limits-of-adjoint-measures/index.html`, main blob `48117e4e5901381d5ae692cfd29f2cf5f1325abc`: Proposition **11.25.1**, physical lines **11–25**, source `non-kahler-pluripotential-theory:A07C226C`, permanent tag `3E5CF25D6E23`. The present audit checks only its **smooth persistence premise**. Its bounded-product extension and capacity-continuity argument, including the excluded approximation dependency, are **not** certified here.

Both main files were read directly, rather than inferred from source numbering or the audit matrix.

## New theorem: only two torsion identities are needed

Let `X` be a compact complex manifold, `n = dim_C X >= 2`, and let `omega` be any smooth positive real (1,1)-form. Write `omega_v = omega + dd^c v` and `H_omega = {v in C^\infty(X,R): omega_v > 0}`. The following are equivalent:

1. `dd^c(omega_v^{n-1}) = 0` for **every** `v in H_omega` (Gauduchon persistence).
2. `dd^c omega = 0` and `d omega wedge d^c omega = 0`. In complex dimension two, the second identity is automatic for degree reasons.
3. `dd^c(omega^j) = 0` for **all** `1 <= j <= n-1`.

In dimension one, persistence is automatic since `omega_v^0 = 1`; the two-form criterion is intentionally stated only for `n >= 2`.

**Proof.** Because `omega` has even degree, the graded Leibniz rule (with the same `d^c` convention as Pome) gives the pointwise identity, for every integer `k >= 1`,

$$
dd^c(\omega^k)
 = k\,dd^c\omega\wedge\omega^{k-1}
   + k(k-1)\,d\omega\wedge d^c\omega\wedge\omega^{k-2}.
\tag{1}
$$

The last term is absent for `k=1`. Thus (2) immediately implies (3). Conversely, `j=1` in (3) implies `dd^c\omega=0`; for `n>=3`, `j=2` and (1) imply `d\omega\wedge d^c\omega=0`. For `n=2`, its bidegree is (3,3), hence it vanishes. Therefore (2) and (3) are equivalent. Since `dd^c v` is annihilated by both `d` and `d^c`, and `d\omega_v=d\omega`, condition (2) applied to `omega_v` gives (1) and (i) immediately.

For the remaining implication, assume (1) of the theorem. Fix `x in X` and any *real* (1,1)-form `H` at `x`. A real compactly supported smooth test potential `v` in a coordinate ball can be chosen with `dd^c v(x)=H`. For all sufficiently small real `t`, `omega+t dd^c v` is positive. The Gauduchon identity at `x` is the following polynomial identity in `t`:

$$
0=(n-1)\,dd^c\omega\wedge(\omega+tH)^{n-2}
 +(n-1)(n-2)\,d\omega\wedge d^c\omega\wedge(\omega+tH)^{n-3}.
\tag{2}
$$

For `n=2`, (2) directly gives `dd^c\omega=0`. For `n>=3`, the coefficient of `t^{n-2}` forces `dd^c\omega(x)\wedge H^{n-2}=0` for **every** real Hermitian `H`. Polarization of the powers `H^{n-2}`, followed by the nondegenerate complementary-bidegree pairing, yields `dd^c\omega(x)=0`. With that term absent, the coefficient of `t^{n-3}` forces `d\omega(x)\wedge d^c\omega(x)\wedge H^{n-3}=0` for all `H`. The same polarization argument yields `d\omega\wedge d^c\omega(x)=0`; when `n=3` this is just the (3,3) identity itself. Since `x` was arbitrary, (2) holds globally. This proves all three equivalences. There is no use of approximation, curvature-loss estimates, or a sequential compactness step.

**Smooth mass and adjoint probability.** Under these conditions, for every smooth `v\in H_omega`, the segment `omega_{tv}` remains positive and

$$
\frac{d}{dt}\int_X\omega_{tv}^n
 =n\int_X dd^cv\wedge\omega_{tv}^{n-1}
 =n\int_X v\,dd^c(\omega_{tv}^{n-1})=0.
$$

Consequently `M=\int_X\omega^n` is the common mass. The smooth adjoint multiplier is the constant `M^{-1}` since `dd^c(\omega_v^{n-1})=0`, agreeing with §11.23.4 and with the **smooth case** of §11.25.1. No assertion is made about extending this proof to bounded singular potentials; that separate task relies on upstream results not checked in this run.

## Explicit persistent but non-Kähler model in every dimension n >= 2

Let `0<q<1` be real and take the diagonal Hopf surface

$$
H=(\mathbb C^2\setminus\{0\})/(z\sim qz).
$$

On its cover put `r^2=|z_1|^2+|z_2|^2`, `omega_0=(i/2)\sum_{j=1}^2 dz_j\wedge d\bar z_j`, and

$$
\omega_H=\frac{\omega_0}{r^2}.
$$

The scale factors in the numerator and denominator cancel under `z\mapsto qz`, so `omega_H` descends to a smooth positive Hermitian metric on the compact Hopf surface. The real four-dimensional identity `\Delta_{\mathbb R^4}r^{-2}=0` on `r>0` shows

$$
dd^c\omega_H=(dd^c r^{-2})\wedge\omega_0=0,
$$

because in complex dimension two the wedge on the right is a universal multiple of the Euclidean Laplacian of `r^{-2}`. The metric is **not closed**: `d\omega_H=d(r^{-2})\wedge\omega_0\ne0` at, for example, `(z_1,z_2)=(r,0)`.

For `n>2`, let `E` be a flat elliptic curve, let `X=H\times E^{n-2}`, and define `omega=pr_H^*\omega_H+\sum pr_j^*\eta_E`, with `eta_E` a flat Kähler form. Then `dd^c\omega=0`. Both `d\omega` and `d^c\omega` are pulled back from the complex surface `H`, so their wedge has bidegree (3,3) on `H` and is zero. Hence **every** positive smooth `omega+dd^cv` on `X` is Gauduchon and has the **same** Monge–Ampère mass although `d\omega\ne0`. This is not the existing three-torus example §11.23.5, where Gauduchon persistence fails, nor the previously audited two-torus constant-curl computation.

## Assessment, correction proposal, boundaries

- **Mathematical status:** The original propositions 11.23.4 and 11.25.1 are **not shown false**. The new result gives an independently proved necessary-and-sufficient smooth hypothesis test and a genuinely non-Kähler persistence model. Severity **low**, classification **verified conditional deduction**, not a repair of a gap.
- **Suggested optional editorial addition:** after Proposition 11.23.4, note that the `n-1` power identities reduce to the two explicit torsion identities, with `d\omega\wedge d^c\omega` automatic on surfaces. An optional example is the Hopf surface and its products above; do not replace the valid contrasting Example 11.23.5.
- **Dependents:** the smooth mass/adjoint formula of §11.23.4, the persistence premise of §11.25.1, and the sufficient hypothesis in §11.23.11. The full parabolic flow and its existence are not checked.
- **Excluded dependencies:** §11.25.1's bounded-product extension invokes §11.1.7 (including excluded approximation) and bounded-capacity continuity. Those are **deferred-by-user**, not resolved; this report proves only the smooth differential-form claim independently.
- **Coverage actually performed:** physical statement/proof and preceding/following commentary of §11.23.4, local Example 11.23.5 for contrast, and the hypothesis/selected proof of §11.25.1. No entire §11.23/§11.25 or full dependency chain certified; **25 chapters, 747 numbered sections, zero complete-section certificates**. No source, tag, registry, main, builds, CI, or website modified.
