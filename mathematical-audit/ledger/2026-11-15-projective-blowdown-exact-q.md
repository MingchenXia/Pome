# 2026-11-15 additive classified finding: exact projective-complement convexity threshold

- **ID:** POME-PROJ-COMP-BLOWDOWN-EXACT-Q-001.
- **Status:** verified conditional deduction. **Severity:** low. Not a second confirmed false theorem, not a source repair, not a transitive certification.
- **Main:** b6933b772f41b45918f7e25ed1afbbb1fd892272.
- **Precise source:** §11.18 integrated file docs/sections/gauduchon-metrics-and-linear-mass--convex-norms-and-gauduchon-degrees--curvature-and-projective-complement-exhaustions/index.html, blob fab309d460a8411fefcd1ef32a094927d6feea10, lines 19–25, 28–45, 50–68. Theorem 11.18.2 source non-kahler-pluripotential-theory:9BF81039 / permanent B93CB03C68B7. §11.17 definition of smooth q-convexity at line 129, blob d49b7d4f2a213c8b70abfe2f337562202bb58dfb.
- **Result:** for d,m>=1, X=P^d×C^m, E=pr1^*O(1), U_E=Tot(O(-1))×C^m has **exact least smooth convexity index d+1**. The proper holomorphic blowdown to C^{d+m+1} yields a smooth globally proper squared-norm exhaustion whose Levi rank is N off the exceptional divisor and m+1 on it. Escaping P^d fibers forbid more than m+1 positive directions outside all compact subsets for arbitrary smooth exhaustions. The printed curvature bound would incorrectly demand q=m+1 for d>m.
- **Distinct prior finding, preserved unchanged:** POME-PROJ-COMP-BASE-ESCAPING-COMPACT-FIBERS-001 (high / confirmed error; 2026-11-11), which already disproved the unqualified theorem with m=1 and d>=2. The present proof contributes the exact optimal threshold and arbitrary m, **not** a rediscovery of that error.
- **Proposed correction:** retain proposed explicit compact-X qualification on Theorem 11.18.2 and dependent Corollary 11.18.4. Do not patch production text in this audit branch.
- **Dependents not certified:** §§11.18.4, 11.19–11.21; positivity hypothesis and properness must be checked separately in any application.
- **Exact actual coverage:** already partly read §§11.17, 11.18; first-visited numbered sections +0; fully certified sections +0; catalogue 25 chapters / 747 sections. The user-excluded Demailly and dedicated programmes stay **deferred-by-user**.
- **Full proof:** [2026-11-15 projective blowdown exact q](../reports/2026-11-15-projective-blowdown-exact-convexity-index.md).
