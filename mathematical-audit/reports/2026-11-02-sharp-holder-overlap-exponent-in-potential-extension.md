# Audit: sharp Hölder-versus-normal-pole exponent in local extension gluing

**Date:** 2026-11-02. **Reviewed production main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.
**Finding ID:** `POME-EXT-HOLDER-NORMAL-POLE-GAP-001`.
**Severity / status:** **low / verified conditional deduction**. The integrated theorem is **not** shown false; there is **no confirmed proof gap** and **no applied repair**.

## Exact integrated sources and coverage

- `docs/sections/global-potentials-and-positive-cohomology-classes--extension-from-a-compact-submanifold/index.html`, main blob `f29e7b7bd47a1986c7fd8360b929a4a543c576b8`.
- Theorem **10.8.26**, source `foundations-of-pluripotential-theory:325F663B`, permanent tag `853DA86626EB`: statement at physical lines 548–565, standing compact-Kähler/Hölder conditions and local extension proof at lines 566–650. **Only selected nonexcluded local steps are checked.**
- Equation **10.8.27**, source `foundations-of-pluripotential-theory:D2E157EA`, permanent tag `897524437A9B`, lines 581–591: the lower normal pole bound.
- **Step 3 and Equation 10.8.28**, source `foundations-of-pluripotential-theory:DC1778F8`, permanent tag `007C2EF0BE28`, lines **651–676**: the arbitrarily small overlap comparison. Step 4's index-switching use occurs at lines **678–698**.
- Lemma **10.8.24**, source `foundations-of-pluripotential-theory:8BAD0B28`, permanent `4BEE08C69CE8`, lines **475–519**: local Hölder coordinate transformations, compositions and powers.
- Lemma **10.8.25**, source `foundations-of-pluripotential-theory:8EDC50CC`, permanent `9C08A2D9AA88`, lines **520–545**: smooth log-sum-exp convex-Hessian identity and the claimed PSH closure. Its ordinary local convolution argument was **not** reaudited as any Demailly programme.

These are the current integrated reading-edition labels and anchors, not old manuscript section numbers. The excluded dedicated Demailly approximation/regularization, Bergman, weighted `L^2`, Ohsawa–Takegoshi, multiscale and positivity-loss programme was not considered.

## New quantitative deduction from the printed local hypotheses

Let `Y={w=0}` in a product coordinate chart near `p`, and let `pi_i` and `pi_j` be two holomorphic local retractions fixing `Y`. Write `E=e^F` for the common positive normal-pole term, and suppose on a sufficiently small chart

```text
| exp(phi(pi_i(z,w))) - exp(phi(pi_j(z,w))) | <= K |w|^alpha,
exp(F(z,w)) >= c_0 |w|^c,
0 < c < alpha <= 1,   K,c_0>0.
```

These are exactly the consequences of the local Hölder control and the printed estimate (10.8.27). Define
`Phi_k = log(exp(phi o pi_k)+E)+A R` for `k=i,j`, as in the theorem's proof. Off `Y`, the logarithms are finite since `E>0`. For `a,b>=0` and `E>0`,

```text
|log(a+E)-log(b+E)| <= log(1+|a-b|/E).
```

Indeed, if `a>=b`, then `(a+E)/(b+E)=1+(a-b)/(b+E)<=1+(a-b)/E`, and the opposite order is symmetric. Since the identical `A R` term cancels, we obtain the *quantitative overlap bound*

```text
|Phi_i(z,w)-Phi_j(z,w)| <= log(1+(K/c_0)|w|^(alpha-c))    (w != 0).
```

This strengthens the qualitative neighborhood-dependent `Phi_i<=Phi_j+eta` of (10.8.28): the overlap discrepancy is `O(|w|^(alpha-c))` uniformly along any fixed compact subchart. On `Y` both extensions restrict to `phi` (including at common poles), so the original **order comparison** still holds there without taking the undefined difference `-infinity-(-infinity)`. For any prescribed `eta>0`, choose `|w|` so that `(K/c_0)|w|^(alpha-c)<=exp(eta)-1`. This supplies the precise neighborhood width needed in Step 4.

## Endpoint sharpness, including compatibility with the theorem's global hypotheses

Take a bidisk in `C_z x C_w`, `Y={w=0}`, `0<alpha<=1`, and the legitimate local holomorphic retractions

```text
pi_1(z,w)=(z,0),     pi_2(z,w)=(z+w,0).
```

On `Y`, let `phi(z)=alpha log|z|`, with `phi(0)=-infinity`. Then `exp(phi(z))=|z|^alpha` is `alpha`-Hölder. Set `R=|w|^2`, `F=(c/2)log R=c log|w|`, so that `E=|w|^c` and the smooth common `A R` contribution cancels. Along `z=0` and `w!=0`,

```text
Phi_1(0,w) = c log|w| + A|w|^2,
Phi_2(0,w) = log(|w|^alpha+|w|^c) + A|w|^2,

Phi_2(0,w)-Phi_1(0,w) = log(1+|w|^(alpha-c)).
```

Thus the upper estimate above is **attained as an equality** with `K=c_0=1`. For `c=alpha`, the discrepancy is identically `log 2`; the arbitrary-`eta` overlap property fails for `eta<log 2`, no matter how much the charts are shrunk. For `c>alpha`, the discrepancy even diverges to `+infinity` as `w->0`. For `c<alpha` it tends to zero at the exact power `alpha-c`. Hence the *strict* inequality `c<alpha` is sharp as a universal hypothesis for this **specific log-sum-exp overlap scheme**. This does **not** imply failure of the extension theorem, which explicitly chooses `c<alpha`.

The local example can occur under the theorem's **compact Kähler hypotheses**: let `X=P^1 x P^1`, `Y=P^1 x {0}`, and use `omega=omega_FS,z+omega_FS,w`. For a point `p in Y`, give `O(p)` its Fubini–Study metric and set `phi=(alpha/2)log|s_p|_FS^2`. With `dd^c=i/(2pi)partial barpartial` and the usual normalization `dd^c log|s_p|^2=[p]-omega_FS`, this yields

```text
omega|_Y+dd^c phi=(1-alpha/2)omega_FS+(alpha/2)[p]
                  >=(1-alpha/2)omega_FS>0.
```

Its exponential is locally `C(z)|z|^alpha` with `C(0)>0` smooth, hence globally `alpha`-Hölder. The two retractions are defined on an overlapping coordinate bidisk. The same endpoint discrepancy has a strictly positive limit (with an inessential chart-dependent constant). There is no global counterexample to Theorem 10.8.26.

## Further checks, implications, and classification

The smooth log-sum-exp computation agrees with the printed `p(1-p)` positive semidefinite Hessian term; the common smooth `A R` does not affect chart comparisons. The exact exponent gap, rather than mere continuity of `exp(phi)`, is what permits **arbitrarily small** boundary penalties at indices entering/leaving the finite maximum in Step 4 (lines 690–696). At a point where `exp(phi)>0`, a different local argument might work at the endpoint; the countermodel exploits a *pole on Y*, which the theorem explicitly allows.

**Proposed editorial addition only:** immediately after (10.8.28), state the quantitative `log(1+C|w|^(alpha-c))` estimate and optionally the `z=0` local endpoint example. Preserve both existing stable tags, the original proof, and attribution. **No source/body/registry/canonicalization/permanent-tag change is made.**

**Affected dependents:** the fixed-index local maximum argument in Theorem 10.8.26 Step 4 and its global potential gluing in Step 5, **conditionally on** the unverified background existence/PSH lemmas already invoked by the printed proof. This audit checks neither the theorem's full global proof, its singularity-resolution steps, nor any unrelated `L^2` extension passage in §10.8. The status is **verified conditional deduction**, not false theorem, proof gap, or certified global repair.

**Coverage:** First newly selected direct proof-level review of this *nonexcluded* §10.8.24–26 local Hölder/log-sum-exp/overlap portion; the section was previously inventory-only. The surrounding Ohsawa–Takegoshi/`L^2` arguments in §§10.8.1–22 remain **excluded by the user's scope**, not reviewed or resolved. No section-wide mathematical certification; project totals remain **25 chapters, 747 numbered sections, zero whole-section mathematical certifications**.
