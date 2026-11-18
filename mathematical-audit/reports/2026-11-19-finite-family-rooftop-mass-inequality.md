# Finite-family rooftop mass inequality and a strict common-minorant criterion — §16.23 direct audit

**Finding:** POME-ROOFTOP-FINITE-FAMILY-MASS-INEQUALITY-001  
**Date:** 2026-11-19  
**Severity/status:** low / **verified conditional deduction** (relative to the explicitly named internal inputs below). **No false printed theorem** and no independently established new proof gap.  
**Production main reviewed:** b6933b772f41b45918f7e25ed1afbbb1fd892272.  
**Integrated reading edition:** docs/sections/envelopes-and-model-potentials--rooftops-and-mass-inequalities/index.html; blob e6a5d5222b356a650b3834f30f8d597efb15d052; complete physical lines 5–180.  
**Current table of contents:** 25 chapters, 747 numbered sections, checked against docs/chapters/index.html (blob c0c07abf4d8f7575b54cff2ec694fcf987f51cf8).

## Anchors and precise scope

- §16.23 opening, source foundations-of-pluripotential-theory:F75DA8B3 / permanent 4CC29395A55C, lines 5–9.
- Proposition 16.23.1, source :399D14C6 / permanent 3499B9FD713C, statement 10–16, proof 18–44: two-potential strict-mass existence criterion.
- Proposition 16.23.2, source :E9818AE3 / permanent E33C504A684F, statement 46–48, proof 50–56: model-rooftop stability.
- Proposition 16.23.3, source :EEB459D9 / permanent 37241FAAC9EF, statement 58–60, proof 62–96: replacement of full-mass model types.
- Lemma 16.23.4, source :29AEFF78 / permanent F4294ED919CC, statement 101–106, proof 108–128: upper semicontinuity of zero-contact mass along decreasing sequences with a nontrivial limit.
- Theorem 16.23.5, source :578DB8C4 / permanent 641CB44C78E9, statement 130–135, proof 137–179: two-potential rooftop mass inequality.
- Checked dependency statements, **not their entire proofs:** Corollary 16.13.5, permanent 7FE9391D7A51 (binary rooftop contact measure); Proposition 16.11.7, permanent 046401771DAB (rooftop associativity and decreasing continuity); Proposition 16.21.2, permanent 037CA226D141 (singularity envelope monotonicity and increasing reconstruction); Proposition 16.21.3, permanent 5ADA09DD223E (model contact concentration); Lemma 16.22.2, permanent 4D5FAF80D021 (model-relative sup); Theorem 16.22.11, permanent 4A1DC8C4E020 (positive-mass modelization); and Corollary 13.8.9 (monotone mass continuity).

## A finite-arity theorem

Let the class of the smooth closed real (1,1)-form θ be big on the compact connected Kähler manifold X of dimension n. Fix an **integer N≥2** and arbitrary θ-psh potentials u₁,...,u_N. Set

\[
 m_i=\int_X\langle(\theta+dd^c u_i)^n\rangle,\quad
 m=\int_X\langle(\theta+dd^c\max_i u_i)^n\rangle,\quad
 r=P_\theta(u_1,\ldots,u_N).
\]

The N-argument rooftop is obtained by repeated binary rooftops; associativity is Proposition 16.11.7.

**(A) Strict existence.** If
\[
 \boxed{\ \sum_{i=1}^N m_i>(N-1)m,\ }
\]
then r is not identically minus infinity; in fact the argument below forces a common θ-psh minorant.

**(B) Finite-family mass inequality.** Whenever r is a genuine θ-psh potential,
\[
 \boxed{\ \sum_{i=1}^N m_i\le (N-1)m+
       \int_X\langle(\theta+dd^c r)^n\rangle.\ }
\]
For N=2 these recover Proposition 16.23.1 and Theorem 16.23.5 exactly. These statements are *finite*-arity results. Neither arbitrary infinite intersections nor a uniform assertion about directed families is claimed.

### Step 1. Finite contact domination

Write R_j=P_θ(a₁,...,a_j) for potentials with a common θ-psh minorant. Applying Corollary 16.13.5 to (R_{j-1},a_j), and inducting, gives the inequality of positive measures
\[
 \mu_{R_N}\le \sum_{i=1}^N {\bf1}_{\{R_N=a_i\}}\mu_{a_i}.
 \tag{1}
\]
Indeed, on the piece where R_j=R_{j-1}, the induction measure bound for R_{j-1} is supported by R_{j-1}=a_i, hence by R_j=a_i. This is a genuine induction on the **measure** inequality, not an assumed partition of possibly overlapping contact sets.

### Step 2. Proof of (A) by a common-model cutoff

By subtracting one constant, normalize every u_i≤0. Each m_i≤m by mass monotonicity, so the strict inequality forces m>0. Put s=max_i u_i and φ=P_θ[s]. Theorem 16.22.11 makes φ a model potential of mass m; s≤φ≤0.

The non-pluripolar measures μ_{u_i} do not charge pole sets, and u_i≤φ. As T increases, the sets {u_i>φ−T} exhaust the common finite locus for μ_{u_i}; hence choose T>0 with
\[
 \sum_i\mu_{u_i}(\{u_i>\phi-T\})>(N-1)m.       \tag{2}
\]
For C>T let a_{i,C}=max(u_i,φ−C) and R_C=P_θ(a_{1,C},...,a_{N,C}). The common minorant φ−C and the upper bound φ show R_C∼φ and μ_{R_C}(X)=m. By Proposition 16.11.7, R_C decreases to r as C→∞.

Suppose r≡−∞. Compact Hartogs monotone convergence (the same Corollary 10.3.6 used at printed Proposition 16.23.1) gives sup_X R_C→−∞; Lemma 16.22.2 then gives R_C≤φ−T for all sufficiently large C. Applying (1) and the inclusion {R_C=a_{i,C}}⊂{a_{i,C}≤φ−T} yields
\[
\begin{aligned}
m
&\le\sum_i\mu_{a_{i,C}}(\{a_{i,C}\le\phi-T\})\\
&=Nm-\sum_i\mu_{u_i}(\{u_i>\phi-T\})<m,
\end{aligned}
\]
a contradiction. The equality uses C>T, so {a_{i,C}>φ−T}={u_i>φ−T}, and plurifine locality identifies μ_{a_{i,C}} and μ_{u_i} there. This proof does not require modelizing each u_i separately.

### Step 3. Prove (B) for model potentials

Assume first that each u_i=φ_i is model and let γ=max_i φ_i, m=M(γ), q=P_θ(φ_1,...,φ_N), assumed nontrivial. All φ_i≤0, and each μ_{φ_i} is supported on {φ_i=0} by Proposition 16.21.3 and contact concentration for V_θ.

For C>0 put φ_{i,C}=max(φ_i,γ−C) and q_C=P_θ(φ_{1,C},...,φ_{N,C}). Every φ_{i,C} and q_C has the singularity type of γ, hence mass m; q_C decreases to q. Locality near {φ_i=0}, which lies in {φ_i>γ−C}, gives a **positive measure decomposition**
\[
 \mu_{\phi_{i,C}}=\mu_{\phi_i}+\nu_{i,C},
 \qquad \nu_{i,C}(X)=m-M(\phi_i).
\]
The μ_{φ_i} part cannot contribute to the contact bound (1) on {q_C<0}: whenever q_C=φ_{i,C} on {φ_i=0}, one has q_C=0. Therefore
\[
 \mu_{q_C}(\{q_C<0\})
 \le\sum_i\bigl(m-M(\phi_i)\bigr).
\]
Since μ_{q_C}(X)=m,
\[
 \mu_{q_C}(\{q_C=0\})\ge
      \sum_iM(\phi_i)-(N-1)m.              \tag{3}
\]
Apply Lemma 16.23.4 to the decreasing sequence q_C along positive integers, **only because the limit q is a potential**:
\[
 M(q)\ge\mu_q(\{q=0\})
 \ge\limsup_{C\to\infty}\mu_{q_C}(\{q_C=0\})
 \ge\sum_iM(\phi_i)-(N-1)m.
\]
This proves (B) for model inputs. It does not attempt to use the decreasing-limit lemma when the limit is −∞.

### Step 4. Transfer (B) to arbitrary positive-mass inputs

If some m_i=0, the claim is immediate because every other m_j≤m, so assume m_i>0 for all i. Shift every u_i≤0 and put φ_i=P_θ[u_i]. Theorem 16.22.11 gives model φ_i with M(φ_i)=M(u_i) and u_i≤φ_i.

For each C>0, η_{i,C}=P_θ(u_i+C,V_θ) satisfies u_i≤η_{i,C}≤u_i+C, so max_i η_{i,C}∼max_i u_i. Proposition 16.21.2 gives η_{i,C}↑φ_i, and the finite maximum also increases to γ=max_i φ_i. By monotone non-pluripolar mass continuity (Corollary 13.8.9),
\[
 M(\gamma)=M(\max_i u_i)=m.               \tag{4}
\]

Let q=P_θ(φ_1,...,φ_N), so r≤q. If M(q)=0, monotonicity implies M(r)=0 (given r is a potential), and the model inequality already gives the required bound. If M(q)>0, replace φ₁, then φ₂, ..., then φ_N by u₁,...,u_N. At each stage group the *remaining N−1 arguments* into a single rooftop ψ; the old common rooftop is P_θ(φ_j,ψ) of positive mass. Proposition 16.23.3 applies with the first argument u_j∈E(X,θ,φ_j) and the second unchanged ψ∈E(X,θ,ψ), and preserves the positive rooftop mass. Therefore M(r)=M(q). Combining (3)–(4) yields (B). No sequentialization of a general directed net occurs.

## Review of the existing §16.23 proofs and dependencies

All five printed statement/proof pairs (lines 10–179) were read directly. Proposition 16.23.1 uses strict inequality only after a fixed mass cutoff; no subtraction of infinite extended masses occurs. Proposition 16.23.2's reverse rooftop inequality depends on the normalization w≤0. Proposition 16.23.3 uses the positive-mass extrapolation with a>1 and transfers the mass through both endpoint replacements, not merely the existence of a common minorant. Lemma 16.23.4 localizes weighted Bedford–Taylor convergence away from the analytic bad locus and takes limits in the order j, then t, with its required nontrivial decreasing limit. Theorem 16.23.5 separates model contact concentration from the full-mass replacement. No new wrong sign, normalization defect, or independently confirmed proof gap was found in these direct steps.

**Uncertified upstream dependencies:** binary rooftop contact domination (16.13.5), model concentration (16.21.3), positive-mass modelization (16.22.11), extrapolation (16.22.4 and 16.23.3), and the local bounded Bedford–Taylor weighted convergence and monotone non-pluripolar mass continuity used in Lemma 16.23.4 and (4). Only their relevant hypotheses/conclusions were crosschecked; no entire transitive proof chain was certified.

**Excluded/deferred-by-user:** Demailly approximation/regularization and the dedicated Bergman, L², Ohsawa–Takegoshi, multiscale-atlas and positivity-loss programme. No part of this report attempts to complete, reclassify, or restart those proofs. Any independent regularization-derived prerequisite remains deferred, not resolved.

## Classification and possible patch

**POME-ROOFTOP-FINITE-FAMILY-MASS-INEQUALITY-001:** low / **verified conditional deduction**. The original two-potential statements are correct; this is a finite-arity strengthening using their contact/extrapolation machinery. Optional proposed addition after Theorem 16.23.5: the boxed (A)–(B) formulas, the finite-contact induction (1), and the model reduction, clearly specifying finite N. No source-body, canonicalization, registry, tag, or published-doc modification is made. Existing binary results are not duplicates; the arity is materially different. Potential mathematical dependents are future finite common-rooftop arguments, rather than an asserted defect in a particular existing theorem.

**Coverage recorded:** direct entire §16.23, including every numbered statement and proof, with specific upstream statements sampled for dependency checking only. This increases direct entire-section readings by one; zero complete transitive upstream-chain certifications. Prior first-visit count is not asserted without a reliable historical matrix merge. No build, tests, GitHub Actions, CI or publication.
