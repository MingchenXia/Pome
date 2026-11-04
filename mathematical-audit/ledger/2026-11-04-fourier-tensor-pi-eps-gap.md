# Classified mathematical-audit entry — 2026-11-04

| Field | Record |
| --- | --- |
| Stable ID | **POME-TENSOR-FOURIER-PI-EPS-GAP-001** |
| Severity | **low** |
| Status | **verified conditional deduction** (not a false original theorem, missing proof, duplication, or repair) |
| Production main | `b6933b772f41b45918f7e25ed1afbbb1fd892272` |
| Exact reading file | `docs/sections/concrete-completed-tensor-products/index.html` |
| Main file blob | `358f584ab4004b3531629e87f1dd73bdea1256d4` |
| Main source/permanent tags | Proposition **2.19.1** `demailly-complex-geometry:E56C631F` / `84C71E271314`, lines **11–31**; Proposition **2.19.2** `demailly-complex-geometry:4D711A6B` / `96A052277244`, lines **33–55** |
| Context, not recertified | Proposition **2.19.3** `demailly-complex-geometry:C614F79A` / `C9CDFE118A86`, lines **57–82**; §2.13 tensor norm conventions |
| Hypotheses | Complex `E=F=ell^1_m`, any odd integer `m>=3`, `zeta=exp(2pi i/m)`, `T_m=sum zeta^(jk)e_j tensor e_k` |
| Exact deduction | `||T_m||_pi=m^2`, `||T_m||_epsilon=m^(3/2)`; ratio `sqrt(m)` unbounded. |
| Complete justification | Coordinate decomposition plus triangle inequality give the projective norm. Fourier orthogonality gives the injective upper bound. Chirp `b_k=zeta^(k^2)` has all Fourier moduli `sqrt(m)` for odd m (direct change of variables `h=k-l`), giving equality. |
| Mathematical verdict | The two printed completed-tensor identities and the polar-unit-ball statement are **correct** and must not be canonically identified by ignoring the tensor norms. There is no new confirmed error. |
| Proposed correction | Optional new explanation/example after 2.19.2; **proposal only**. Preserve original statements, source attribution, proof variants and permanent tags. |
| Affected dependents | Interpretations of §2.13 projective/injective norms and future cross-references to §§2.19.1–3; no presently invalid dependent identified. |
| Actual coverage | New explicit all-odd-dimensional **complex** Fourier norm calculation in previously partly audited §2.19; no newly certified complete section or external theorem chain. |
| Excluded work | Demailly approximation/regularization, Bergman, weighted L2, Ohsawa--Takegoshi, multiscale and positivity-loss remain **deferred-by-user**, not reexamined or resolved. |
| Verification | Hand-verifiable exact finite-sum proof; no executable check, build, CI, formalization or publication. |
| Details | [Full mathematical report](../reports/2026-11-04-fourier-tensor-projective-injective-unbounded-gap.md) |

The existing resolved/unresolved/deferred records are unchanged. Actual ToC: **25 chapters, 747 numbered sections, zero complete mathematical-section certifications**.
