# 2026-11-07 audit ledger — Hopf radial-action Fourier signature

**POME-PERRON-HOPF-FOURIER-SIGNATURE-001** — **low / verified conditional deduction**.

- **Reviewed main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.
- **Integrated target:** `docs/sections/perron-interpolation-and-the-geodesic-equation/index.html` (blob `dc8dc381257360c94fe1c792499bb1ddf1bf5997`, lines 447–497). Theorem 17.16.25 source `non-kahler-pluripotential-theory:A1289B04` / permanent `944944D6FF68`; radial action 17.16.24 source `E8F59B3B` / permanent `905CCA72845B`; Hessian 17.16.26 source `5B7EC348` / permanent `F20F3B72C244`. Geometry §23.1.32 main blob `f53618e8d808de21687ff9166971cb9302ea8cfb`, lines 560–577.
- **Hypotheses:** \(n\ge3\), \(d=n-1\), \(c\ne0\), smooth two-periodic radial \(w(t,r)\) zero at \(t=0,1\), sufficiently small variations preserving \(\omega+\mathrm{dd}^{\mathrm c}u>0\).
- **Verified addition:** after \(s=r-dct\), the full radial Hessian is \(2n\int(W_t^2-\frac{d(d+1)}2c^2W_s^2)\). The real sine/cosine modes indexed by \(\ell,k\ge1\) have exact Hessian values \(\frac{n\pi^2}2(\ell^2-\frac{d(d+1)}2c^2k^2)\); the spatially constant sine mode is positive. Full Fourier orthogonality proves infinite indices of both signs, precisely locates resonance, and gives two-sided unbounded Rayleigh quotients.
- **Proof/dependence status:** complete elementary calculation **conditional on the printed Hopf geometric density**, which was crosschecked but not fully certified. General Perron, Kähler completion, CAT(0), and global geometry claims not certified. The printed theorem is **not false**.
- **Proposed change:** optional separately reviewable spectral corollary to Theorem 17.16.25; no source/body/tag changes made.
- **Full proof:** [report](../reports/2026-11-07-hopf-raw-action-full-fourier-signature.md). **Exact coverage:** [coverage delta](../coverage/2026-11-07-ch17-hopf-raw-action-fourier-signature.md).
- **Other statuses:** previous confirmed errors, open proof gaps, candidate issues, external dependencies and duplications unchanged. Excluded Demailly regularization and all associated dedicated completion work retain **deferred-by-user** classification.
