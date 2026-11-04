# Fourier matrices: an exact unbounded projective/injective tensor-norm gap

- **Finding:** `POME-TENSOR-FOURIER-PI-EPS-GAP-001`.
- **Classification:** **low / verified conditional deduction**; the printed propositions are correct, not a false theorem or an omitted proof.
- **Reviewed production main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`, 2026-11-04.
- **Integrated reading edition:** `docs/sections/concrete-completed-tensor-products/index.html`, blob `358f584ab4004b3531629e87f1dd73bdea1256d4`. Proposition **2.19.1**: source `demailly-complex-geometry:E56C631F`, permanent tag `84C71E271314`, physical lines **11–31**. Proposition **2.19.2**: source `demailly-complex-geometry:4D711A6B`, tag `96A052277244`, lines **33–55**. Proposition **2.19.3**: source `demailly-complex-geometry:C614F79A`, tag `C9CDFE118A86`, lines **57–82**, consulted only for the distinction in scopes. §2.13 is the convention source for tensor norms, not newly proof-certified.

## Exact theorem and proof

For **every odd integer** `m>=3`, take the complex spaces `E=F=ell^1_m`, their canonical basis `e_0,...,e_(m-1)`, and `zeta=exp(2*pi*i/m)`. Define the finite tensor

```text
T_m = sum_(0<=j,k<m) zeta^(j*k) e_j tensor e_k.
```

Then **`||T_m||_pi=m^2` and `||T_m||_epsilon=m^(3/2)`**. Consequently the ratio `||T_m||_pi/||T_m||_epsilon=sqrt(m)` is unbounded. This rules out a dimension-independent comparison of these two norms on the same complex tensor spaces; it does **not** contradict either of Pome's printed, distinct tensor-product isomorphisms.

**Projective norm.** For any finite matrix tensor `T=sum_(j,k) a_jk e_j tensor e_k`, coordinate-basis decomposition shows `||T||_pi<=sum|a_jk|`. For every representation `T=sum_r x_r tensor y_r`, the triangle inequality gives

```text
sum_(j,k)|a_jk| <= sum_r (sum_j |(x_r)_j|)(sum_k |(y_r)_k|).
```

Taking the infimum proves the reverse inequality, and therefore `||T||_pi=sum_(j,k)|a_jk|`. Since all Fourier coefficients have modulus one, `||T_m||_pi=m^2`.

**Injective upper bound.** As `(ell^1_m)'=ell^infty_m`, the injective norm is

```text
||T_m||_epsilon
 = sup_(|a_j|,|b_k|<=1) |sum_(j,k) zeta^(j*k) a_j b_k|
 = sup_(|b_k|<=1) sum_j |(F_m b)_j|,
(F_m b)_j = sum_k zeta^(j*k) b_k.
```

Cauchy--Schwarz and discrete Fourier orthogonality imply

```text
sum_j |(F_m b)_j|
 <= sqrt(m) [sum_j |(F_m b)_j|^2]^(1/2)
 = sqrt(m) [m sum_k |b_k|^2]^(1/2)
 <= m^(3/2).
```

The complex unit-disc dual vectors are essential: using only real signs would compute a different norm.

**Matching lower bound for every odd m.** Take the quadratic chirp `b_k=zeta^(k^2)`. Put `S_j=sum_k zeta^(k^2+j*k)`. With `h=k-l`, a direct finite sum gives

```text
|S_j|^2
 = sum_(h,l mod m) zeta^((l+h)^2-l^2+j*h)
 = sum_(h mod m) zeta^(h^2+j*h) sum_(l mod m) zeta^(2*h*l).
```

As `m` is odd, `2h=0 mod m` implies `h=0 mod m`. Thus the inner sum is zero for all nonzero `h` and equals `m` for `h=0`; **`|S_j|=sqrt(m)` for each j**, including odd composite m. Choosing the first dual vector's coordinate phases to align these `S_j` gives `||T_m||_epsilon>=sum_j |S_j|=m^(3/2)`. This meets the upper bound. No external Gauss-sum theorem or analytical limiting process is used.

## Adjudication and actual coverage

The integrated Proposition 2.19.1 is the **projective** identity `ell^1(I) completed_tensor_pi ell^1(J) = ell^1(I x J)`. Proposition 2.19.2 states a **polar-unit-ball relation** and the **injective** identity `c_0(I) completed_tensor_epsilon c_0(J)=c_0(I x J)`; it correctly warns that the polar statement does not identify the entire dual in arbitrary Banach spaces. Neither proposition asserts a universal comparison between `pi` and `epsilon` on the *same* spaces. They are both mathematically correct and distinct; their canonical entries and source attributions must remain separate.

**Optional proposed edit only:** an example after Proposition 2.19.2 emphasizing the exact unbounded Fourier gap; no source/body/registry/permanent-tag edits are authorized here. Potential downstream effect: future tensor-topology arguments invoking §2.13 or §§2.19.1–3 without distinguishing `pi` from `epsilon`. **No existing Pome theorem is refuted**. This is a new finite-dimensional, all-odd-index norm computation in an **already partly reviewed** §2.19, not a claim of first section coverage or full certification. The old finite-matrix density and compact-space approximation checks are not repeated as new findings.

Existing confirmed errors, proof gaps, external dependencies and genuinely duplicate variants retain their classifications. All explicitly excluded Demailly approximation/regularization and dedicated Bergman, weighted L2, Ohsawa--Takegoshi, multiscale-atlas and positivity-loss work stays **deferred-by-user**, not certified or reopened. No private material was used. No build, test suite, CI, formalization or website publication was run. Project inventory remains **25 chapters / 747 numbered sections / zero fully certified mathematical sections**.
