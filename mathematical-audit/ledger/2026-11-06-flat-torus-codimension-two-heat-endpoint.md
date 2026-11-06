# Classification ledger increment — 2026-11-06-flat-torus-codimension-two-heat-endpoint

- **Finding ID:** `POME-HEAT-CODIM2-LOGARITHMIC-L1-ENDPOINT-001`
- **Date:** 2026-11-06
- **Severity / status:** **low / verified conditional deduction**; no false theorem, proof-gap repair or genuine duplication.
- **Reviewed main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.
- **Source:** `docs/sections/heat-kernels-on-compact-manifolds/index.html`, blob `c59a1b3fab9433f1aae95db99adb4821857b5d8d`, §3.10.5, physical lines **85–105**, source `transcendental-positive-cones:DD00B1CA`, permanent `56A174D59425`; supporting §3.10.1 lines **10–83**, source `:327DDB8B`, permanent `126365F8EBD6`.
- **Exact finding:** a codimension-two subtorus measure satisfies the prescribed `r^(m-2)` growth and has `lim ||t h_t rho||_infty=1/(4 pi)`; nonetheless its pairing against every fixed nonnegative `L1` function tends to zero. Fixed `L1` data with logarithmic singularity yield exact decay `[log(e/sqrt(t))]^(1-p)/(2(p-1))`, `p>1`, not `O(t^delta)` for any positive `delta`.
- **Suggested correction (proposal only):** optional endpoint-sharpness remark following the existing lemma. Do not strengthen `t h_t rho -> 0` to `L-infinity` or to an unguarded uniform-in-density rate.
- **Affected reasoning:** time-dependent test densities, uniform-in-`L1` estimates, or purported polynomial rates in heat trace limits; none asserted false without further direct review.
- **Unresolved/external:** the global heat construction and Gaussian estimate of §3.10.1 and any full downstream use remain unverified; prior error, gap, external-dependency and deferred-by-user classifications preserved.
- **Audit scope:** selected first mathematical inspection of §3.10 (heat kernel, codimension-two mass bound, `L1` limit). Not a whole-section mathematical certification. No excluded regularization programme reopened.

[Detailed, reproducible calculation](../reports/2026-11-06-flat-torus-codimension-two-heat-endpoint.md) · [exact coverage](../coverage/2026-11-06-flat-torus-codimension-two-heat-endpoint.md).
