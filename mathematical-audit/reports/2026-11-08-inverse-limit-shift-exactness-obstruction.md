# A dense-degreewise inverse system whose limit is not exact

**Date:** 2026-11-08. **Finding:** `POME-INV-LIM-DENSE-DEGREE-NONEXACT-001`. **Severity:** low. **Status:** verified conditional deduction (sharpness of printed hypotheses; no printed Pome theorem is false). **Production main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.

**Actual integrated reading edition:** `docs/sections/open-maps-nuclear-spaces-and-inverse-limits--cohomology-of-countable-inverse-limits/index.html`, main blob `30e6e5800601450ce52d9c01dc5abea06a403d6e`. Exact anchors: Theorem 2.14.4, source `demailly-complex-geometry:3D7EF38C`, permanent `50E84369B7A2`, physical lines 77–118; Theorem 2.14.6 (especially item (3)), source `demailly-complex-geometry:7A48110C`, permanent `10E2183C49C3`, lines 122–159, especially 131–132; Proposition 2.14.7, source `demailly-complex-geometry:CD05CCE6`, permanent `F529678A1F94`, lines 162–185. The density mechanism in Lemma 2.14.2, source `demailly-complex-geometry:AAE7DFD2`, permanent `139720D2EFCA`, lines 41–56, was separately checked. The source identifier denotes a provenance collection, *not* the user-excluded Demailly approximation programme.

## Precisely tested proposed strengthening

The printed Theorem 2.14.4 assumes degreewise dense bonding maps and concludes that
`Theta^q: H^q(lim E_n) -> lim H^q(E_n)` is onto. It asserts injectivity **only if** the bonding maps on `H^{q-1}` also have dense image. Theorem 2.14.6(3) retains the latter hypothesis even when the `H^q` bonding maps are injective. Proposition 2.14.7 requires density of the *kernel* bonding maps for strict exactness of an inverse limit of short exact sequences. We test, and disprove, the respective **unprinted** claims obtained by removing those hypotheses, *even while keeping degreewise density of the whole complexes*.

## Complete Hilbert-space construction

Let `K=L=ell^2(N_{>=1}, C)` with orthonormal basis `e_1,e_2,...`. Let
`R(k_1,k_2,...)= (0,k_1,k_2,...)` (the right shift),
`D(l_1,l_2,...)= (l_1,l_2/2,l_3/3,...)`, and
`alpha(l)=sum_{j>=1} l_j/j`.
The functional `alpha` is continuous by Cauchy–Schwarz, since `(1/j)_j in ell^2`. Put
`S:K direct_sum L -> K direct_sum L` by
`S(k,l)=(Rk+alpha(l)e_1, Dl)`.

For each `n>=0` use the two-term bounded complex
`E_n^0=K direct_sum L --d_n--> E_n^1=L`,
where `d_n(k,l)=l`; all other groups are zero. Define the transition chain map in degrees zero and one to be `S` and `D` respectively. Since `d_n S=D d_{n+1}`, these maps give an inverse sequence of complexes of Hausdorff complex Banach (hence Frechet) spaces. Each `d_n` is surjective:
`H^0(E_n)=K, H^1(E_n)=0`.
The induced map `H^0(E_{n+1})->H^0(E_n)` is `R`, whose range is the *closed codimension-one* subspace `{k:k_1=0}`. In contrast the `H^1` maps are maps `0->0` and are simultaneously injective and surjective.

**Every degreewise bonding map nevertheless has dense range.** The diagonal map `D` has dense image because every finitely supported sequence lies in its range. For `S`, suppose a continuous linear functional `(a,b) in K^* direct_sum L^*` annihilates `S(K direct_sum L)`. Its restriction to `S(k,0)=(Rk,0)` implies `a=c e_1^*`. Its restriction to `S(0,l)=(alpha(l)e_1,Dl)` gives
`c alpha + b o D=0`. Identifying the Hilbert duals via coordinates, this requires `b_j/j=-c/j` for every `j`, hence `b_j=-c` for every `j`. Square summability forces `c=0`, then `b=0`. Thus the annihilator of the range is zero; Hilbert-space orthogonal-complement duality implies `closure(range(S))=K direct_sum L`. (There is no assertion that `S` is onto.)

**The inverse-limit differential is not onto.** Set `x_n=2^n e_2 in E_n^1` for every `n>=0`. Since `D x_{n+1}=x_n`, the sequence `x=(x_n)` defines an element of `E^1=lim E_n^1`. Suppose `x=d(k_n,l_n)_n` for a coherent element of `E^0=lim E_n^0`. Then `l_n=x_n`, and coherence forces
`k_n=R k_{n+1}+alpha(x_{n+1})e_1=R k_{n+1}+2^n e_1`.
Comparing successive coordinates, the first `m` coordinates of `k_0` are
`1,2,4,...,2^{m-1}`, for **every** `m`. This is impossible for `k_0 in ell^2`. Thus `x` is a cycle but not a boundary and `H^1(E) != 0`, whereas `lim H^1(E_n)=0`.

No sequential-compactness argument or exchange of infinite limits occurs: `x` is an explicit compatible family; the contradiction examines each finite coordinate and then the definition of `ell^2`.

## Consequences and scope

1. In Theorem 2.14.4, `Theta^1` is **not injective**, while its printed surjectivity assertion is true (the target is zero). The missing assumption in the false strengthened claim is exactly density on `H^0`.
2. In Theorem 2.14.6(3), all `H^1` transitions are injective, but `H^1(E)->H^1(E_0)=0` is **not injective**. The printed requirement that `H^0` transitions be dense cannot simply be removed.
3. For Proposition 2.14.7 take the degreewise strictly exact sequence `0->K->K direct_sum L->L->0` and transition maps `R,S,D`. Both **middle and quotient** transitions are dense, but the inverse-limit projection `lim(K direct_sum L)->lim L` fails to be onto; hence density of the kernel transitions is substantive.
4. In fact the image `d(E^0)` is dense in `E^1`: for any finite-coordinate neighbourhood of a compatible `x`, lift its coordinate at level `N` to `E_N^0` and approximate this lift by the image of `lim E_n^0` using the elementary dense-projection argument of Lemma 2.14.2. Earlier coordinates are controlled by continuous bonding maps. Thus this example also distinguishes **nonzero (non-Hausdorff) cohomology** from reduced cohomology; no separated-cohomology claim is made.

**No printed result is contradicted.** The source's summable approximate-lift proofs correctly distinguish degreewise density from density on cycle/kernel cohomology. This model is a proposed optional explanatory note after 2.14.7, not a proposed change to any theorem, source tag, convention or proof registry. It has no dependence on Demailly regularization or its deferred Bergman/weighted-L2/Ohsawa–Takegoshi programme.

**Dependency / coverage limit:** Only the displayed hypotheses, the local dense-projection argument and this countermodel were independently verified; the general Frechet open-mapping theorem, all algebraic `lim^1` formalism, the entirety of §2.14 and downstream applications have not been certified. Previously recorded findings remain classified as before.
