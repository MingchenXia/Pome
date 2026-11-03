# A polar truncation obstruction to replacing Bedford–Taylor maximality by non-pluripolar vanishing

**Checkpoint:** 2026-11-04. **Production main reviewed:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.
**Finding:** `POME-BT-NPP-POLAR-MAXIMALITY-001` — **low / verified conditional deduction**. This is a counterexample to an *unprinted strengthening*, **not** an error in Pome's Theorem 7.7.7 or Definition 13.2.4. No correction to their printed statements is requested.

## Precisely reviewed integrated text and provenance

1. `docs/sections/bedford-taylor-products-and-local-capacity--the-homogeneous-dirichlet-problem-and-balayage/index.html`, main blob `928f3d3e36f2d03a42623b91487ecec7d189e6c7`. **Definition 7.7.6**, source `foundations-of-pluripotential-theory:4A1DBBE1`, permanent tag `FD8547B922C9`, physical **lines 159–161**, defines maximality by all compactly supported plurisubharmonic competitors. **Theorem 7.7.7**, source `foundations-of-pluripotential-theory:5C75D8E4`, permanent tag `BCFDDA1FCB7A`, physical **lines 164–175**, assumes *locally bounded* psh and uses the classical Bedford–Taylor top wedge `(dd^c u)^n`. The forward proof truncates an arbitrary competitor before applying comparison (lines 170–171); the converse invokes local ball balayage (lines 172–173). This was a selected renewed reading of hypotheses and proof quantifiers, not independent recertification of comparison or balayage.
2. `docs/sections/non-pluripolar-products--truncation-and-plurifine-locality/index.html`, main blob `81be8c5acc360c96bd3c5acba05a3cdb5fafaf4c`. The level sets and truncation `u_k=max(u,-k)`, `O_k={u>-k}`, `S_k=1_{O_k}dd^c u_k` are at physical **lines 7–16**. **Definition 13.2.4**, source `foundations-of-pluripotential-theory:9D8E4DD8`, permanent tag `D79952D7E272`, physical **lines 58–64**, defines the locally finite non-pluripolar product, which deliberately discards pluripolar mass. **Lemma 13.2.2**, source `foundations-of-pluripotential-theory:CE1D6DA5`, permanent tag `D59675D9F6D8`, **lines 35–52**, proves monotonicity of the *cutoff measures*, not convergence of the uncut classical truncation measures to the cutoff limit.
3. Normalization: `dd^c=(i/2\pi)\partial\bar\partial`, hence `dd^c\log|z|^2=\delta_0` on the plane. There is no use of Demailly regularization, Bergman kernels, weighted L2, Ohsawa–Takegoshi or the deferred approximation programme.

## Exact counterexample and three measures

Set `\Omega=\{z\in\mathbb C:|z|<1\}` and for any `a>0` put `u_a(z)=a\log|z|^2`, with `u_a(0)=-\infty`. It is psh but is not locally bounded. For integers `k\ge1` define
```text
r_k = exp(-k/(2a)),
u_{a,k} = max(a log|z|^2, -k),
O_k = { |z| > r_k }.
```
Write `\sigma_r` for the probability measure on the circle `|z|=r` obtained by normalized angular Lebesgue measure. Green–Stokes on the two sides of the circle (or radial Laplacian flux) gives the exact identity
```text
dd^c u_{a,k} = a sigma_{r_k}.
```
Indeed the radial derivative in the variable `\log|z|` jumps from zero inside the circle to `2a` outside. The total `dd^c` mass is `a` by the adopted normalization, and no mass occurs away from the interface because both branches are harmonic there. Consequently `dd^c u_{a,k}\rightharpoonup a\delta_0` as `k\to\infty`. This is also the classical Riesz mass of the decreasing limit `u_a`.

On the other hand, **the measure `a\sigma_{r_k}` is entirely supported on the excluded level `u_a=-k`**, not on `O_k=\{u_a>-k\}`. Thus *at every level*
```text
S_k = 1_{O_k} dd^c u_{a,k} = 0.
```
The non-pluripolar measure defined in §13.2 therefore exists, is locally finite, and satisfies
```text
<dd^c u_a> = lim_k S_k = 0,
whereas dd^c u_a = a delta_0 != 0.
```
In particular, even **monotonically decreasing locally bounded psh potentials** `u_{a,k}\downarrow u_a` have non-pluripolar products `<dd^c u_{a,k}>=a\sigma_{r_k}` converging weakly to `a\delta_0`, **not** to `<dd^c u_a>=0`. One may not interchange formation of the final polar cutoff and the weak limiting process. The zero cutoff-current sequence `S_k` is consistent with, and does not refute, §13.2.2.

## Failure of maximality in exactly the printed sense

For any fixed `0<r<1` define globally on `\Omega`
```text
v_r(z) = max{ a log|z|^2, a log r^2 }.
```
It is subharmonic as the maximum of two subharmonic functions, agrees with `u_a` on the complement of the compact disk `\{|z|\le r\}\Subset\Omega`, and is *strictly greater* than `u_a` wherever `|z|<r` (including at the pole). Therefore `u_a` is **not maximal** by Definition 7.7.6, although its *non-pluripolar* Monge–Ampère measure is identically zero. The classical first-order Monge–Ampère measure is `a\delta_0\ne0`, so there is no contradiction with the locally bounded/classical hypothesis of Theorem 7.7.7.

The parameter `a>0` allows arbitrary prescribed deleted polar mass. The location can be translated to any specified interior point of a planar domain; adding a harmonic function changes neither the two measures nor the argument when the compact competitor is formed by adding the same harmonic term. These elementary examples are distinct from the prior §7.7.6–7.7.7 **bounded quadratic ball Dirichlet** model (`POME-BT-QUADRATIC-DIRICHLET-EIGENVALUE-001`): this new test concerns an unbounded pole, the exact level-set cutoff, and the distinction between `dd^c u_k\rightharpoonup dd^c u` and `\langle dd^c u\rangle`.

## Classification, dependencies and proposed handling

- **Status/severity:** low / verified conditional deduction; *no false printed theorem* and *no demonstrated gap* in the selected §7.7.7 proof. The only falsified assertion is the tempting but **unprinted** extension `<dd^c u>=0 => u maximal` for all possibly unbounded psh functions.
- **Affected dependents if hypotheses were weakened:** the local maximality criterion §7.7.7; uses of its ball balayage/compact comparison in §7.7; any transitive attempt to replace classical Bedford–Taylor mass by non-pluripolar mass in maximality arguments such as §17.8. No claim is made that those downstream theorems actually commit this substitution.
- **Proposed optional note, separately reviewable:** immediately after Theorem 7.7.7, point out the polar-logarithm example and state explicitly why the theorem assumes local boundedness and why §13.2's non-pluripolar product cannot simply replace its classical top wedge. Preserve all source attributions, source labels and permanent tags. No source/body/registry change is made by this audit.
- **Actual coverage:** one newly checked *sharp-hypothesis and limiting-operation boundary* across already partly sampled §7.7.6–7 and §13.2.2/.4; no new entire section certification or re-claim of the previous quadratic result. The current ToC has 25 chapters and 747 numbered sections, with zero completely mathematically certified sections. Existing confirmed errors, genuine gaps, external dependencies and all owner-excluded items remain in their previous classifications, including `deferred-by-user` for the excluded work.
- **Not performed:** project tests, build, CI, formal verification, website publication; no main/source file changed.
