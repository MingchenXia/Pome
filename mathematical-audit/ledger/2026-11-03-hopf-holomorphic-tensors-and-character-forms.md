# Classified audit finding — 2026-11-03 — contracting Hopf holomorphic tensors

**Stable ID:** POME-HOPF-HOLOMORPHIC-TENSORS-CHARACTER-001  
**Severity:** low  
**Status:** verified conditional deduction (not a false theorem, proof gap or integrated repair)  
**Reviewed main:** b6933b772f41b45918f7e25ed1afbbb1fd892272  
**Primary current source:** docs/sections/contracting-hopf-quotients/index.html, blob d09d9bac3785b78b557ff5178ad7a52b34b20dac, Theorem 23.3.3 (source demailly-complex-geometry:371996B7, permanent D81E3145A1B4), physical lines 9–21 and 26–50. Equation 23.3.4 (source demailly-complex-geometry:F5EE64FF, permanent 436562DE848D), lines 27–34.  
**Conventions crosscheck only:** docs/sections/meromorphic-sections-and-divisor-classes/index.html, blob d0c40d1e3f6f515eb13169ed1cd3fb447ca161c8, Definition 20.7.2 (source demailly-complex-geometry:37374C87, permanent F9B013D39957), lines 8–9, and Proposition 20.7.3 (source demailly-complex-geometry:00A05C89, permanent ACC6D09EDDD9), lines 13–27.

**Precise assertion:** On both explicitly printed contracting diagonal and triangular Hopf complex surfaces, every positive-degree holomorphic covariant tensor vanishes; all global holomorphic functions are constants and all plurigenera vanish, so Kodaira dimension is negative infinity. For diagonal Hopf surfaces, the entire holomorphic p-form character spectrum is the finite monomial weight basis determined by
\(\lambda_1^{a+\mathbf1_{1\in I}}\lambda_2^{b+\mathbf1_{2\in I}}=\chi\).
For the scalar character \(q^k\), its dimension is \(\binom2p(k-p+1)\) if integer \(k\ge p\), otherwise zero. The line-bundle twist convention is explicitly fixed; no diagonal-character basis is asserted for a non-diagonalizable triangular map.

**Proof / hypotheses:** Complete Cauchy-integral extension of all coefficient functions across the isolated missing origin in complex dimension two; first nonzero Taylor jet invariant under the \(d\)-th symmetric and \(r\)-fold tensor representation of \(DF(0)^*\); every resulting eigenvalue has absolute value below one whenever \(d+r>0\), also for the Jordan case. For diagonal maps, compare each monomial of the extended entire coefficient against the character. The nonzero-character fixed-weight set is finite, justifying the polynomial conclusion. All steps, including extension, appear in [the precise full report](../reports/2026-11-03-hopf-covariant-tensors-and-holomorphic-character-spectrum.md).

**Suggested correction / addition:** An optional corollary after the unchanged Theorem 23.3.3, with separate character-weight example. No mathematical correction to the printed theorem, no change in its historical attribution, source tags or equation labels. **Affected dependents:** canonical flat character, Hopf plurigenera, holomorphic differentials and covariance conventions in §20.7; not an assertion about absence of meromorphic functions.

**Nonduplication:** POME-HOPF-JORDAN-MEROMORPHIC-FIELD-001 concerns fields of meromorphic functions; POME-HOPF-CHAR-MEROMORPHIC-SECTIONS-001 concerns existence (not dimension or holomorphicity) of meromorphic sections of character line bundles. Both remain untouched.

**Coverage / remaining uncertainty:** new independent proof-level §23.3.3 result within a previously partially checked section; §20.7 only conventions, no whole-section certificate or recertification of covering construction and Hodge comparison. The full Pome collection remains 25 chapters, 747 numbered sections, zero entirely certified sections. Existing error/gap/external ledgers retain their statuses. All Demailly approximation/regularization, dedicated Bergman, weighted L², Ohsawa–Takegoshi, multiscale-atlas and positivity-loss work stays **deferred-by-user**. No production main, body, source, registry, tag, tests, CI, formal proof or publication action.
