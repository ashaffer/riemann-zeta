# PRE-REGISTRATION — DG Round-3 vector shape test

Committed 2026-07-26 19:27 UTC, BEFORE any minimizer vector or envelope curve from
the configurations below was computed or inspected. Everything decision-relevant is
fixed here; the analysis section of PLAN-differential-geometry.md Round 3 will apply
these rules verbatim and report any deviation as a deviation.

## Configurations

Spectral Legendre basis, `src/spectral_margins.py` `spectral_form`/`spectral_lam_min`
(unmodified), eigenvectors via `vectors=True`:

| # | L | m | dps asm/solve | role |
|---|---|---|---|---|
| 0 | 4.50 | 160 | 75/65 | primary deep |
| 1 | 4.75 | 160 | 75/65 | primary deep |
| 2 | 4.50 | 144 | 75/65 | m-stability rung |
| 3 | 4.75 | 144 | 75/65 | m-stability rung |
| 4 | 3.555 | 112 | 50/40 | null control |
| 5 | 3.555 | 128 | 50/40 | control m-rung |

(One smoke run at (2.485, 24, 50/40) validates the pipeline; it is a debug
artifact, not a decision input.) Envelope: F(T) = φ̂(T) on 1600 log-uniform points
u = ln(T/2π) ∈ [ℓ−0.15, ℓ+1.45], 768-node GL quadrature, eval dps 50 (40 at
control). Two workers max (coordinator's core cap).

## Reference numbers (fixed in advance)

λ reproduction targets (runs.csv): 7.92448858514e-41 (4.5/160),
1.86366090828e-47 (4.75/160), 8.13421925362e-41 (4.5/144),
2.04044762883e-47 (4.75/144), 2.12668062431e-22 (3.555/112); 3.555/128 has no
prior value (new rung; must land in [Aitken 2.119e-22, m=112 value]).

Stopping-height references (Round 2 table): drift w = 1.2201/1.2285 at L=4.50/4.75,
smooth-cap 1.2199/1.2271, abrupt 1.2785; control drift w(3.555) ≈ 1.19;
w_E2 from the deep agent's scalars: 1.2192 (4.50), 1.2243 (4.75), 1.1970 (3.555).

Basis-resolution edge (Legendre coefficient of e^{iTx} ∝ j_k(aT); decay begins at
order k ≈ aT, so the node-representable edge is T_edge ≈ m/a, u_edge = ln(m/2πa)):

| L | m | x_edge = u_edge − ℓ | 2A(x_edge) = T*(e^x(x−1)+1) |
|---|---|---|---|
| 4.50 | 144 | 0.764 | 29.41 |
| 4.50 | 160 | 0.869 | 40.99 |
| 4.75 | 144 | 0.585 | 17.23 |
| 4.75 | 160 | 0.690 | 25.80 |
| 3.555 | 112 | 1.221 | (beyond descent ≈ 1.09: control is resolution-clean) |
| 3.555 | 128 | 1.355 | — |

Edge-tracking shift if the node zone is truncation-limited: Δx = ln(160/144) =
0.1054 (deep), ln(128/112) = 0.1335 (control). **Scope disclosure, fixed now:** at
m ≤ 160 the region x ∈ [0.9, 1.25] is beyond the node-representable edge at BOTH
deep L, so a direct y(x) break observation at x_b ≈ 1.0–1.2 is out of reach; the
pre-registered discrimination therefore runs through the node-edge and
graded-activity observables below. A direct in-zone test needs m ≈ 240 at L = 4.50
(≈ 5 h assembly at current scaling) — flagged as follow-up, not this round.

## Estimators (all fixed now)

- Envelope maxima: strict local maxima of ln|F| on the u-grid. ref = max over
  |u−ℓ| ≤ 0.1; ε(u) = ln|F| − ref; floor = min ε on [ℓ, ℓ+1.45];
  w_E1 = smallest u−ℓ with ε ≤ floor + 1.
- Nodes: strict local minima with contrast ≥ 3 nats below the mean of adjacent
  envelope maxima. x_nodes = largest node's u − ℓ; census N_nodes on (ℓ, ℓ+x_nodes].
- S0 coefficient tail: τ_c = Σ_{k ≥ m−16} c_k². τ_c ≥ 1e−6 ⇒ basis saturated;
  ≤ 1e−12 ⇒ comfortable.
- y(x): group envelope maxima with ε > floor+2 and x ≥ 0.20 into consecutive
  non-overlapping 5-tuples (u-span ≤ 0.12 else drop); per group LS slope s_g at
  centroid u_g; y_g = −s_g/(2πe^{u_g}), x_g = u_g − ℓ. Fit zone: x_g ≤ x_nodes − 0.05.
- M0: y = β₀x (LS). M1: continuous 2-segment (β₀, β₁, x_b; x_b grid over interior
  centroids, ≥ 3 groups/side). F = ((RSS0−RSS1)/2)/(RSS1/(n−3)); p from F(2, n−3)
  (regularized incomplete beta). Significance: p < 0.01.
- w_E2: solve T*(e^w(w−1)+1) = E_m + A, A = 11.5 (band 11.1–11.9), E_m = −ln λ_m.
- Graded-activity ratio: G = [ln λ(m₁) − ln λ(m₂)] / [2A(x_nodes(m₂)) − 2A(x_nodes(m₁))]
  for (m₁, m₂) = (144, 160), with 2A(x) = T*(e^x(x−1)+1) and MEASURED x_nodes.
  Meaning: graded dodging that is eigenvalue-active in the newly resolved shell
  predicts G ≈ 1; a capped/nodeless outer mechanism predicts G ≪ 1.

## Decision rules (verbatim; committed before data)

Gate C1 (pipeline): every λ within 1% of the runs.csv target (and ‖c‖ = 1,
λ₂/λ₁ ≥ 100). Fail ⇒ stop, verdict U (bug hunt first, per oracle discipline).

C2 (graded core): M0 slope β₀ ∈ [0.85, 1.15] on the fit zone at both deep L AND
the control. Fail ⇒ verdict U (estimator or theory anomaly; investigate before
any bend claim — a real β₀ anomaly at control would contradict Round-1's verified
descent and means the instrument, not the mechanism, until proven otherwise).

C3 (the discriminator):
 (a) node-edge m-stable at 4.50: |x_nodes(160) − x_nodes(144)| ≤ 0.04 with
     x_nodes ≤ 0.85 ⇒ dodging terminates below the basis edge while the λ-ladder
     is converged (geometric-model-tested by the deep agent) — drift's graded
     dodging to w ≈ 1.22 is falsified mechanically; OR
 (b) node-edge tracking or indeterminate, but G ≤ 0.2 at BOTH deep L ⇒ the outer
     shell's dodging is eigenvalue-inactive — same mechanical conclusion.
 Either (a) or (b) ⇒ C3 PASS. G ≥ 0.5 at either deep L ⇒ C3 FAIL-open (outer zone
 genuinely unresolved; drift not excluded at vector level).
 0.2 < G < 0.5 with tracking edges ⇒ C3 indeterminate.

C4 (null control): x_nodes(3.555) m-stable across 112→128 (shift ≤ 0.05, i.e.
NOT tracking the 0.1335 edge shift), β₀(control) ∈ [0.85, 1.15], and no p < 0.01
break with post-break slope < 0.5 inside the control's fit zone. Fail ⇒ the
estimator cannot distinguish mechanism-limited from truncation-limited node zones
⇒ verdict U.

C5: B_abrupt stays excluded: w_E2(4.75, m=160) ≤ 1.25.

**Verdicts:**
- **B_smooth CERTIFIED** ⇔ C1 ∧ C2 ∧ C3 ∧ C4 ∧ C5.
- **NOT CERTIFIED** (evidence favors, incomplete) ⇔ C1 ∧ C2 ∧ C4 ∧ C5 with C3
  indeterminate.
- **U** ⇔ C1, C2, or C4 fail, or C3 FAIL-open.

**What falsifies B_smooth outright** (pre-committed): edge-tracking node zones
with G ≈ 1 (∈ [0.5, 2]) at both deep L — that is graded dodging still absorbing
the action at the graded rate, i.e. drift, and the deep deviations revert to
Q1-bias territory; likewise any m-stable break with post-break slope > 1
(steepening — inconsistent with every cap mechanism on the table). If either
occurs I will say so in those words.

Secondary reports (no thresholds): S0 tails; in-zone break test at both deep L
and control (p, x_b, slopes); node census vs budget aT/π; beyond-edge tail
exponent p_tail = −d ln|F|/d ln T on [x_nodes+0.1, x_nodes+0.35]; w_E1; w_E2
reproduction of the deep agent's scalar values (±0.002).

Pre-computed illustrations (NOT measurements; using x_edge = m/a which the data
may move): if node zones sat exactly at the m/a edge, G would read 0.0023 (4.50)
and 0.0106 (4.75) from the runs.csv Δln λ — i.e. the scalar ladder already hints
the outer shell is nodeless; the vector run pins x_nodes and removes the m/a
heuristic from that inference. This expectation is recorded so that hindsight
cannot claim it.

---

## AMENDMENT 1 — committed 19:34 UTC, after the smoke test, BEFORE any deep or
## control envelope existed (worker logs establish the ordering)

The smoke config (2.485, m = 24; declared a debug artifact above) exposed a
degeneracy in the "x_nodes = largest node" estimator: it measured 1.408, far past
both the descent and the m/a edge (0.574 at that config). Cause, understood
analytically: a compactly supported φ with nonvanishing boundary data has
φ̂(T) ~ boundary-term/T with sinc-lattice nodes of spacing π/a persisting to
arbitrary height, so "largest node" is grid-limited and meaningless. The
discriminating structure is not node existence but node REGISTRATION: in the
dodging zone nodes are pinned to the sample points (the true zeta ordinates —
Groskin/keyhole), whereas free boundary-tail nodes sit on the π/a lattice, which
is strictly sparser than the staircase above T* and cannot stay registered.

**Revised estimator (replaces x_nodes everywhere in C3, C4, G):**
- Alignment: for each node, d = |T_node − nearest γ_k| / local mean spacing
  (γ_k = true ordinates, mp.zetazero, cached; local spacing = 2π/ln(T/2π)).
- **x_dodge** = last node of the maximal prefix (in increasing u, nodes above T*)
  with d ≤ 0.30.
- Cross-check estimator: x_spacing = last node whose spacing to the previous node
  is ≤ 0.9·(π/a); require |x_dodge − x_spacing| ≤ 0.08, else flag "estimator
  disagreement" and treat the config as indeterminate for C3/C4.
All thresholds of C3/C4 carry over verbatim with x_dodge in place of x_nodes
(m-stability ≤ 0.04 deep / ≤ 0.05 control; tracking shift 0.105 deep / 0.134
control; C3(a) requires x_dodge ≤ 0.85 at 4.50; G uses 2A(x_dodge)).
No threshold values were changed by this amendment; only the degenerate
estimator was replaced by the registration-aware one. The smoke config will be
re-reported with both estimators for the record.

**Amendment 1b (19:35 UTC; verified by `ls` that no deep/control envelope file
existed yet):** two calibration fixes from the smoke re-run, before any decision
data. (i) Alignment threshold 0.30 → 0.15: under random phase d is uniform on
[0, 0.5], so P(d ≤ 0.30) = 0.6 — too weak (expected prefix over-extension ~2.5
nodes); the smoke data is strongly bimodal (registered nodes d = 0.00/0.01/0.05/
0.09; first free node 0.29), and d ≤ 0.15 has random base rate 0.3 (bias < 0.5
node). Smoke x_dodge moves 0.667 → 0.55, consistent with its m/a edge 0.574.
(ii) The spacing cross-check's fixed 0.9·(π/a) cutoff is degenerate at T*
(staircase and sinc spacings coincide there BY DEFINITION of T*); replaced by
per-gap nearest-model classification (|ΔT − staircase| ≤ |ΔT − π/a| continues
the prefix). m-stability/tracking thresholds and all C-gates unchanged. Both
estimators are used differentially (144 vs 160), where any residual prefix bias
cancels.
