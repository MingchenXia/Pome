# Verified conditional deduction — POME-GEO-SUBGEO-L1-VARIATION-W11-SHARP-001

**Date:** 2026-11-11. **Reviewed main:** b6933b772f41b45918f7e25ed1afbbb1fd892272. **Severity:** low. **Status:** verified conditional deduction (printed §17.10 statements not refuted).

**Anchor:** docs/sections/geodesic-rays-in-the-space-of-potentials/index.html, blob 52bf9e459a0dfb1c8afe79556db037450be06bb3. Definition 17.10.2 **sgpt:9287531D / 8699FCF63094** (lines 27–56); Proposition 17.10.7 **sgpt:DBC4F9ED / 1880C1FBD88F** (lines 88–140); Corollary 17.10.9 **sgpt:B35F3B4F / C645EE3517E1** (lines 144–174); Corollary 17.10.11 **sgpt:9B844C56 / E31D1E7DDF87** (lines 176–191).

**New result:** Any subgeodesic with its specified L1 endpoints is a Bochner W^{1,1}([0,1];L1(X,dV)) path. Put m=inf_t u_t and A=max(u_0,u_1). Its exact L1 time-variation and integrated derivative norm equal int_X(u_0+u_1-2m)dV, bounded by 2 int_X(A-m)dV. On [delta,1-delta], the L1 Lipschitz constant is at most delta^{-1}int_X(A-m)dV. Both coefficients are optimal, and no universal W^{1,p} for p>1 or endpoint Lipschitz estimate exists, even for smooth constant-in-space endpoints.

**Proof:** [Complete source-anchored report](../reports/2026-11-11-subgeodesic-l1-variation-w11-sharpness.md). Essential justifications: q.e. endpoint equality gives scalar endpoint continuity a.e.; scalar convex absolute continuity and exact variation; Tonelli/Fubini for L1 derivative; fixed nested dyadic partitions justify equality of L1 metric variation, without moving supremum through an integral; explicit convex scalar models establish sharpness.

**Correction proposed:** optional corollary after 17.10.11; no printed theorem correction necessary. §§17.13/17.17 are possible downstream applications, not certified dependents. Prior §17.10 endpoint-envelope/rooftop/ray records unchanged.

**Coverage:** selected §17.10 only; 0 first numbered-section visits and 0 full mathematical certifications, ToC 25/747. User-excluded Demailly regularization/Bergman/L2/OT/multiscale/positivity-loss remains **deferred-by-user** (not resolved). Audit Markdown only; no main/source/body/registry/tag edits, tests/build/CI or website publication.
