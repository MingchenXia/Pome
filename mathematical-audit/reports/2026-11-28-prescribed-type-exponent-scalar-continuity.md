# Prescribed ordinary types: continuity and monotonicity in the exponent

Date: 2026-11-28 (Asia/Shanghai). Reviewed production main: b6933b772f41b45918f7e25ed1afbbb1fd892272.
Audit parent: 80f3b0ebd1abc0f6e47abc86e759f7beca0b7623.

## Finding POME-PRESCRIBED-TYPE-EXPONENT-SCALAR-MONOTONICITY-001

Severity: low. Status: **verified conditional deduction**, not a false printed statement and not a demonstrated proof gap. Proposed action: optional corollary following Theorem 15.12.1; preserve all existing tags, source labels, and attribution. No source/body/registry edits.

### Anchors and hypotheses

- `docs/sections/equations-with-prescribed-singularities--equations-in-a-prescribed-ordinary-type/index.html`, blob d35a6cd3e5fe394a270957aa5d27bbcefaec8860, whole mathematical lines 7–317. Theorem 15.12.1 source D77104B1 / permanent 7AFA75E73767, lines 17–36, positive-exponent proof 184–264 and zero-exponent proof 273–317. Lemma 15.12.2 FA584656 / D0B5A6CE28E9, lines 43–70; Theorem 15.12.3 43068D46 / 413B92CD2B72, lines 81–151; Lemma 15.12.4 9BF24AEC / 5A797D7301BB, lines 159–175.
- `docs/sections/equations-with-prescribed-singularities--domination-with-a-smaller-background/index.html`, blob 95dc2dd6ba0061e2c096947087c5125b9bad85b0, Theorem 15.2.2 1F4338C0 / D70D1E469F9D, lines 44–69 selected; Corollary 15.2.3 8F6F638A / AF890AD49AC5, lines 86–97.
- `docs/sections/equations-with-prescribed-singularities--compactness-with-a-common-lower-barrier/index.html`, blob 2d4d8889cbe39cf880723c59abcb6461b26812f7, Corollary 15.9.4 C466047F / F856D22ADF4C, lines 76–98.
- `docs/sections/equations-with-prescribed-singularities--bounded-equations-in-a-semipositive-big-background/index.html`, blob 84f49b16943ee4e0d5dcf8d8bf59cd815a1ef15f, Theorem 15.3.3 E540849F / 96A341EAF1D4, lines 75–87 selected, and 15.3.5 5F2BC208 / A972C11565ED, lines 126–134, statement-level input.
- `docs/sections/conventions/index.html`, blob ef778e54d8d7413242387e95c52269b3c7d42cae, line 123: X is compact connected, dimension n>=1.

Retain all premises of 15.12.1: semipositive big smooth background theta, a reference phi=P_theta[phi] with P_(epsilon theta)(phi) not identically minus infinity for a fixed 0<epsilon<1, and mu=f dV, nonnegative nonzero f in L^p, p>1. Write MA for the extended product used in the printed proof. For lambda>0 take the unique solution u_lambda of MA(u_lambda)=exp(lambda u_lambda) mu, and set v_lambda=u_lambda-sup_X u_lambda and c(lambda)=exp(lambda sup_X u_lambda). Thus sup v_lambda=0 and MA(v_lambda)=c(lambda) exp(lambda v_lambda) mu. For lambda=0 choose any normalized solution v_0 of MA(v_0)=c(0) mu; the printed theorem asserts uniqueness only of c(0).

### Order in the parameter

For 0<=s<t, shift v_t by A=log(c(t)/c(s))/t, and call the shifted potential w. Its t-weighted measure equals c(s) mu. The t-weighted measure of v_s is c(s) exp((s-t)v_s) mu, which is at least c(s) mu since v_s<=0. These comparisons are made off the common pole set, which mu does not charge. All the potentials are in the same ordinary type, and a smaller-background envelope exists for w by the bounded difference from phi. The weighted comparison Corollary 15.2.3 therefore gives w>=v_s. Taking suprema yields A>=0 and hence

    c(t)>=c(s),     v_s<=v_t+(log c(t)-log c(s))/t.

The argument for s=0 uses only the weighted measure comparison off the poles, not finiteness of exp(-t v_0) mu. It applies to every normalized solution at zero. The nondecreasing scalar is not claimed strictly increasing.

### Compactness and continuity

Fix B>0. As in the printed zero-exponent proof (280–300), use a bounded normalized solution h of MA(h)=a mu, a>0, given by 15.3.5. Set H_lambda=h+||h||_infty+(log a)/lambda. Its lambda-weighted measure is <=mu, and u_lambda is more singular than H_lambda. Weighted comparison gives u_lambda<=H_lambda. Consequently for 0<lambda<=B,

    b_p/||f||_p <= c(lambda) <= a exp(2 B ||h||_infty).

The lower bound follows from Lemma 15.12.2 applied to the density c(lambda) exp(lambda v_lambda) f. Applying Theorem 15.12.3 uniformly gives phi-C_B<=v_lambda<=phi, as in lines 302–308; the density is bounded above by a exp(2B||h||_infty) f. The constants depend on the fixed data and B.

Take an arbitrary sequence lambda_j>0 tending to lambda_*>=0. Restrict to a bounded parameter interval. Normalized PSH compactness and the scalar bounds yield a subsequence on which v_lambda_j converges in L^1 to v and c(lambda_j) converges to c>0. The common singularity bounds hold for the canonical representative of v (pass to the a.e. inequalities and then to canonical PSH representatives). The fixed finite non-pluripolar dominating measure permits use of Corollary 15.9.4: convergence in capacity and weak convergence of MA. Along a further subsequence with a.e. convergence for dV, dominated convergence gives

    c(lambda_j) exp(lambda_j v_lambda_j) f -> c exp(lambda_* v) f in L^1(dV).

At lambda_*=0 the exponential limit is 1 at every point of a.e. finite convergence. Hence MA(v)=c exp(lambda_* v) mu. For lambda_*>0, v+(log c)/lambda_* solves the unique unnormalized equation of Theorem 15.12.1(1), so v=v_lambda_* and c=c(lambda_*). At lambda_*=0, uniqueness of the scalar in part (2) gives c=c(0) but does not identify v uniquely. The subsequence criterion proves full scalar continuity on [0,infinity), L^1 and capacity continuity of v_lambda at every positive lambda, and full TV continuity of the resulting MA measures even at zero. At zero the potential statement is only that every L^1 cluster point belongs to the fixed ordinary type and solves the zero-exponent normalized equation. This argument does not assert a unique limit of v_lambda there.

### Quantitative defect at zero

The common lower bound gives 0<=-v_lambda<=C_B-phi almost everywhere. The fixed quasi-PSH reference has finite L^{p/(p-1)} norm by the exponential integrability input already used in 15.12.3, so K=integral (C_B-phi) dmu is finite by Hölder. The inequality 1-exp(-x)<=x for x>=0 implies, with the full signed total variation norm,

    ||MA(v_lambda)-c(lambda) mu||_TV
       = c(lambda) integral (1-exp(lambda v_lambda)) dmu
       <= a exp(2B||h||_infty) K lambda.

This is an O(lambda) bound relative to the *moving* scalar c(lambda), not a rate for c(lambda)-c(0) or for MA(v_lambda)-c(0) mu. Those rates are not proved here.

### Review of the original argument and dependencies

Directly read all mathematical paragraphs in §15.12, including the strict density lower bound (the translated competitor forces a contradiction by strict domination); the convex increasing G(x,y)=x+chi(y-x) on y<=x (derivatives in both coordinates nonnegative, Hessian PSD); the truncation/locality passage off poles; the polynomial factor absorbed by an exponential; the same-type rooftop supersolution and the zero reference contact measure on the strict branch; weighted-mass maximization with fixed finite carrier and continuous-test approximation; the no-deficit addition step; and the zero-exponent scalar uniqueness by arbitrary translations. No newly confirmed theorem error or precise proof gap was found in these steps conditional on their printed inputs. In particular, the original text does not assert uniqueness of the normalized zero-exponent potential.

Internal premises used, not certified transitively: smaller-background strict/weighted domination (15.2.2–3), bounded subsolutions/existence and density estimates (15.3.1, 15.3.3, 15.3.5), exponential integrability (5.26.2), convex composition (5.28.13), common-barrier compactness (15.9.4), weighted convergence (5.44.2, 5.44.5), addition (15.11.1), and rooftop/contact support (16.28.6–7). Any regularization dependencies of these results remain deferred-by-user; no Demailly/Bergman/L2/OT/multiscale/positivity-loss proof is reopened. No new external dependency asserted for this deduction; upstream existence and comparison are still conditional.

Affected dependents: optional strengthening of the zero-exponent limiting argument in 15.12.1(2); any downstream use of its normalized scalar can use monotonicity/continuity under the same hypotheses. No downstream source theorem is refuted, and no exhaustive reverse-reference search is claimed.

## Coverage and repository checks

One whole directly reviewed conditional section: §15.12 lines 7–317. Three selected dependency sections §§15.2, 15.3, 15.9 and the convention line only; no historical first-visit claim. Previous historical statuses retained. Matrix has 747 numbered rows and 747 distinct locators; Chapter 15's 37 numbered section locators were compared with the actual current chapter ToC, no missing/extra. Main, AGENTS.md, documentation/proof-expansions.md, and both LATEST.md and README.md on the audit branch were freshly fetched; previous material retained. No tests, builds, CI, publication, formal verification or changes to main or production files. Zero new confirmed errors, zero new demonstrated gaps, one verified conditional deduction, zero complete upstream proof-chain certifications.
