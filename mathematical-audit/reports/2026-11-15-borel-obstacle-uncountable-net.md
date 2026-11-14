# Directed Borel obstacles do not admit unrestricted monotone-net envelope continuity

Date: 2026-11-15 (Asia/Shanghai). Stable finding: **POME-BOREL-OBSTACLE-UNCOUNTABLE-NET-001**.
Classification: **low / verified conditional deduction** (sharpness counterexample to an *unclaimed* net extension); **not an error in the printed theorem**.

## Pinned integrated reading-edition evidence

- Reviewed `main`: `b6933b772f41b45918f7e25ed1afbbb1fd892272`.
- `docs/sections/envelopes-and-model-potentials--obstacles-and-rooftops/index.html`, blob `e9129aaaab9e9f172da9704bffe939839f8afeb6`; §16.11 permanent section tag `FBD81D436A6A`, source `foundations-of-pluripotential-theory:FD8D661F`, physical line 5.
- Definition 16.11.3, source `foundations-of-pluripotential-theory:7FB6072B`, permanent tag `A4F165851008`, physical lines **76–84**: a Borel obstacle is constrained *quasi-everywhere*, and the envelope is `-infinity` if the candidate set is empty.
- Proposition 16.11.4, source `foundations-of-pluripotential-theory:3796C01B`, permanent tag `641F3FEC623D`: pluripolar-invariance clause (3), physical lines **97–99, 129**; explicitly **sequential** decreasing-continuity clause (5), physical lines **109–110**, proof **133–134**.
- Context only: `docs/sections/the-envelope-operators/index.html`, blob `1751b26b427c36506d7ed35ca6f52aefc56f8b04`, §16.1 intro tag `2AC9E2799656`, source `sgpt:D8A4D4BA`, physical lines 5–20; `docs/sections/the-envelope-operators--p-envelopes/index.html`, blob `912f81b3bccf3e1ead96fd18005261a708dfcb4e`, §16.2 introduction; `docs/sections/envelopes-and-model-potentials/index.html`, blob `decb273ec97fcb9bb0ace2e0b90270723ecbea3e`, §16.10 introductory conventions, lines 5–16. Those introduction sections contain no proof to certify.

## Exact sharpness construction

Let `X` be **any connected compact Kähler manifold of complex dimension at least one**; set `theta=omega` for its Kähler form. Let `I` be the directed set of **all finite subsets** `F⊂X`, ordered by inclusion. For each `F` define the extended-real Borel obstacle

```text
f_F(x) = -infinity, if x belongs to F;
         0,         otherwise.
```

Then `F⊂G` implies `f_G≤f_F`, so the indexed family is a pointwise decreasing **net**. Every finite set is pluripolar: locally each singleton is contained in the pole locus of a logarithmic psh germ, and finite unions remain pluripolar. Consequently `f_F` and the zero obstacle agree quasi-everywhere. By **the exact competitor definition** in 16.11.3, their competitor sets coincide, and since `0∈PSH(X,omega)` is their maximal competitor,

```text
P_omega(f_F) = 0 for every finite F.
inf_F P_omega(f_F) = 0.
```

On the other hand, each `x∈X` belongs to the finite subset `{x}`, so

```text
f(x):=inf_F f_F(x) = -infinity  for all x∈X.
```

There is **no** candidate `v∈PSH(X,omega)` satisfying `v≤f` outside a pluripolar set: such a `v` would equal `-infinity` on the complement of a pluripolar, hence Lebesgue-null, set. This contradicts local integrability and the requirement that a psh function is not identically `-infinity`. Therefore Definition 16.11.3 stipulates

```text
P_omega(inf_F f_F) = -infinity,
which is NOT inf_F P_omega(f_F) = 0.
```

Both sides are defined; all `f_F` have the common upper bound zero, and all *individual* envelope candidate sets are nonempty. Thus neither unboundedness nor mass escape accounts for the failure.

### Why the printed sequence statement remains correct

For any increasing **sequence** `F_1⊂F_2⊂⋯` of finite subsets, `F_*=∪_j F_j` is countable and therefore pluripolar. Its obstacle `inf_j f_{F_j}` agrees with zero quasi-everywhere, hence `P_omega(inf_j f_{F_j})=0=inf_j P_omega(f_{F_j})`. The original proof of Proposition 16.11.4(5) at line 133 explicitly takes the **countable union** of exceptional pluripolar sets `N_j`; this is mathematically justified and cannot be replaced by an arbitrary union. There is no countable cofinal subset of the directed set of finite subsets, because its union would be countable whereas `X` is uncountable. Passing to a sequence cannot repair the proposed net extension.

This construction uses only elementary pluripolarity and the stated Borel q.e. competitor definition. No Demailly approximation/regularization, Bergman kernels, L2 estimates, Ohsawa–Takegoshi, or multiscale/positivity-loss inputs occur.

## Classification, dependencies, and proposed action

- **Printed statement:** Proposition 16.11.4(5) is a **correct sequence theorem**, and its displayed proof's countable exceptional-set union is justified. No theorem or proof error is alleged.
- **New claim ruled out:** the unrestricted replacement of *sequence* by *directed net* of bounded-above Borel obstacles is **false**, even with all individual envelopes identically zero.
- **Severity/status:** low / **verified conditional deduction** (the explicit compact Kähler test model and a sharp boundary for any later use of the theorem).
- **Potential downstream dependents:** any future comparison of arbitrary directed infima with obstacle envelopes in §§16.11–16.13, 16.21–16.27, or in non-pluripolar contact-set arguments. These are **potential logical interfaces**, not allegations that an actual downstream result currently commits the error.
- **Recommended non-source-changing note:** retain the word *decreasing sequence* in clause (5). If documenting nets, warn that an arbitrary union of pluripolar exceptional sets need not be pluripolar; a separate hypothesis or a new proof is necessary. No body/registry/canonicalization edits are authorized.
- **Distinct prior finding:** an older §15.32 net-dominated-convergence obstruction also used finite-set indexing, but concerned equivalence classes in `L^n`, not Borel obstacle envelopes. It is retained unchanged rather than claimed as new here.
- **Upstream proof status:** elementary local pluripolarity, countable subadditivity of pluripolar exceptional sets and local `L^1`-integrability of nontrivial psh functions are used in this model. Other general envelope/Monge–Ampère and mass theorems are **not** transitively certified by this selected check.

## Scope and actual coverage

New independent exact example plus direct check of Definition 16.11.3 and Proposition 16.11.4(3),(5) at the indicated physical lines. The §16.11 theorem had **previous selected proof-level coverage**: **0 first-visited numbered sections, 0 completed section certifications**. Introductory §§16.1, 16.2, and 16.10 were consulted for conventions only and contain no new proof certification. The actual ToC remains **25 chapters / 747 numbered sections**, an inventory rather than a verification count. Dedicated Demailly approximation/regularization and its Bergman/L2/OT/multiscale/positivity-loss programme remain **deferred-by-user** and untouched. No build, tests, CI, or publication were run.
