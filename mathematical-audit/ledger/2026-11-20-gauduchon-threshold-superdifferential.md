# Classified finding: Gauduchon threshold derivatives

**ID:** POME-GAUD-THRESHOLD-DANSKIN-SUPERDIFFERENTIAL-001  
**Date:** 2026-11-20  
**Classification:** low / **verified conditional deduction**; *not* confirmed error, proof gap, unconditional proof repair or historical duplicate.  
**Main SHA:** b6933b772f41b45918f7e25ed1afbbb1fd892272.

**Direct mathematical evidence:** docs/sections/gauduchon-metrics-and-linear-mass--compactness-and-duality-of-gauduchon-currents/index.html, blob 31d17f258f2ff178bf52be3d3f92d5a995878d3a, complete mathematical lines 5–76; source/permanent labels **C21ACA47/155386134D9E** (Proposition 11.7.1, lines 16–45) and **4B74203A/A97DA8CE2358** (Corollary 11.7.4, lines 47–73); equation source/permanent labels **9C9E2FC6/7F6E8313B3F8**, **84FCF311/EDF0C9D4A983**. Selected prerequisites: Theorem 11.6.1, Corollary 11.6.2 (permanent F83E15A1F529), and Gauduchon's Theorem 11.4.2.

**Verified conditional claim:** For compact connected X, n>=2, at any smooth (1,1) form theta the minimizing face F_theta of normalized weak Gauduchon currents exactly represents the entire concave superdifferential of kappa_omega(theta). For a smooth real direction eta the right slope is min over F_theta of pairing(eta,T), and the left slope is max over F_theta. All directional slopes agree iff F_theta is a singleton; then kappa is Gâteaux differentiable and its derivative is the unique minimizing current.

**Proof:** [Full complete compact-variational argument](../reports/2026-11-20-gauduchon-threshold-superdifferential.md), using only compactness, smooth-test separation and the existing weak dual representation. It does not assume a smooth minimizer or sequential compactness outside the bounded metrizable set.

**Status and dependencies:** Original §§11.7.1 and 11.7.4 remain valid in the directly reviewed arguments. No new confirmed false theorem. Full upstream proofs of Lamari/Fredholm and subsequent §12.34.1 applications not certified. The connectedness hypothesis is explicit in this new deduction because §11.4.2's proof uses it. No regularization/Bergman/L²/OT/multiscale/positivity-loss review; user-excluded programme remains **deferred-by-user**.

**Proposed patch and dependents:** An optional separately reviewable statement about one-sided slopes and the minimizing face in §11.7, preserving exact source labels, attributions and original proof. Potential dependent uses: perturbations of Gauduchon positivity thresholds and weak minimizer stability. Audit-only; no source, registry, main, permanent tags or publication changed.

**Coverage:** +1 complete direct §11.7 reading, +0 full upstream dependency-chain certifications; historical first visits unreconciled. Prior torus spectral-face/cusp finding not re-counted. No tests or builds.
