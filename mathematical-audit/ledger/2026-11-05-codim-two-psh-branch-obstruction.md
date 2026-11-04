# Classified finding — 2026-11-05

| Field | Recorded value |
| --- | --- |
| Finding ID | `POME-REDUCED-CODIM2-PSH-NONDESCENT-001` |
| Status | **verified conditional deduction**: explicit and fully proved counterexample to an unprinted theorem strengthening; **not** confirmed error or proof gap in the original statements |
| Severity | **low**: hypothesis boundary / downstream guard |
| Reviewed production main | `b6933b772f41b45918f7e25ed1afbbb1fd892272` |
| Integrated §9.9 file | `docs/sections/complex-spaces-and-modifications--plurisubharmonic-functions-on-reduced-spaces/index.html` |
| §9.9 blob | `d9d8091b530c9843e5a725b49af2400936aeaa3a` |
| Main §9.9 anchors | Definition 9.9.1 line 11, `foundations-of-pluripotential-theory:025047FB` / tag `7A62ADAFC2A7`; Lemma 9.9.2 lines 19–41, `:45AEDF34` / `83D4170FB2B3`; Proposition 9.9.4 lines 63–89, `:A6674849` / `B43080BD49F3` |
| Integrated §9.10 file | `docs/sections/pluripotential-theory-on-unibranch-spaces/index.html` |
| §9.10 blob and anchor | `6edfa6b19fa7cdbaf0c2665389fa7b3ca338cdf4`; Grauert–Remmert Theorem 9.10.14 lines 140–156, `sgpt:EEFC0C9A` / `C69D2F0ABA4F` (printed dimension-one warning at line 155) |
| Precise hypotheses | `X=P_z\cup P_w\subset\mathbb C^4` for two transverse 2-planes; `A=\{0\}` has codimension two on each irreducible branch; `u=a` and `u=b` on the respective punctured branches. |
| Verified conclusion | `u\in\mathrm{PSH}(X\setminus A)` and `u` bounded, but a locally PSH extension exists **iff** `a=b`. The two disc submean inequalities force the incompatible fiber values. |
| Distinctness | Existing §9.10.14 footnote presents a dimension-one, codimension-one two-branch example. The present model tests the **stronger codimension-two hypothesis** of §9.9.4 and §9.10.14, with an exact matching criterion. |
| Status of printed statements | §9.9.4 is **correct**: it proves boundedness only. §9.10.14 is **correct**: it explicitly requires unibranchness. No printed false theorem established. |
| Proposed correction | Optional note after §9.9.4: boundedness does not imply extension on arbitrary reduced spaces, even with branchwise codimension two. Preserve the original Grauert–Remmert attribution and footnote. Do **not** change theorem hypotheses or permanent tags. |
| Potential dependents | Attempts to infer arbitrary-reduced codimension-two removability from §9.9.4; attempts to remove unibranchness in §9.10.14; any normalization descent without agreement on finite fibers. |
| Unchecked | General finite-projection proof of §9.9.4; general Grauert–Remmert extension; the external FN disc-test converse. |
| Report | [Complete proof](../reports/2026-11-05-codimension-two-branch-compatibility-for-psh.md) |

All previously classified genuine errors, proof gaps, external dependencies, valid duplicates and verified repairs retain their former status. The excluded Demailly approximation/regularization, Bergman, weighted-`L^2`, Ohsawa–Takegoshi, multiscale and positivity-loss programmes remain **deferred-by-user**, neither solved nor certified. No tests/build/CI/publication.
