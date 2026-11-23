# POME-POLAR-CURVE-AFFINE-NPP-MASS-SPECTRUM-001

- **Date:** 2026-11-23.
- **Status:** verified conditional deduction; **severity:** low.
- **Classification:** not a printed theorem error, not a new transitive certification.
- **Main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.
- **Integrated path/blob:** `docs/sections/non-pluripolar-products--bounded-factors-and-the-first-degree-product/index.html` / `d234ab96e33bfd24ad1d53d29332b2c021cddeff`.
- **Exact primary anchors:** Proposition §13.4.7, lines 195–250, permanent `3553558C2E27`; Proposition §13.4.10, lines 255–282, permanent `FB5ACFB46DB8`; Example §13.4.11, lines 287–295, permanent `E9D7DF5798B0`; polar-measure input §4.1.12 permanent `EBEA4A14BCD2`.
- **Hypotheses:** `P^1`, `int omega_FS=1`, atom-free probability `mu` supported on compact polar `K`, `q` from Example 13.4.11, `q_0=0`, `q_t=tq` for `0<t<=1`.
- **Proof and conclusion:** `T_t=(1-t)omega_FS+tmu`. For `t>0`, its pole locus contains `K`, and that polar set is smooth-volume null, so §13.4.7 gives `<T_t>=(1-t)omega_FS`; also true for `t=0`. Hence `int <T_t>=1-t`, `int T_t=1`, while every `nu(q_t,x)=0` and `I(s q_t)=O` for every `s>0`. This is an affine continuum of non-pluripolar masses with indistinguishable multiplier ideals, not a statement about equality of ordinary singularity types.
- **Affected dependents:** comparisons of numerical/non-pluripolar mass with multiplier-ideal type or Lelong data, relative energy and singularity models; not a correction to existing tags or the reader.
- **Action:** preserve as an independent derived example in the audit; any incorporation into the reader would require a separately reviewable PR. Upstream polar-carrier existence remains an internal mathematical dependency, not fully transitively certified.
- **Full anchored proof:** [report](../reports/2026-11-23-polar-curve-affine-mass-spectrum-and-gauduchon-problems.md). **Precise scope:** [coverage](../coverage/2026-11-23-bounded-factor-npp-and-hermitian-problems.md).
- **Exclusions:** dedicated Demailly approximation/regularization/Bergman/L²/OT/multiscale/positivity-loss programmes remain deferred-by-user.
