# The envelope law: derivation attempt, discriminating experiments, and the sharpened law

Agent working directory: `results/agent-law-theory/` (all scripts, data, logs there).
Date: 2026-07-26. Machine: the repo host, mpmath 1.2.1 + gmpy2, dps 50-55.

**Semantics used on every number.** The truncated frame form
Q = 2 SUM_{0<gamma<=Gcut} (v_re v_re^T + v_im v_im^T) in the orthonormal Legendre
basis on [-a, a], a = L/4, equals the truncated Weil form's zero side; deleting
gamma > Gcut deletes positive rank-ones, so every lambda reported is a **lower
bound increasing in Gcut** toward the infinite frame bound, and at fixed Gcut a
**Galerkin (Rayleigh-Ritz) minimum decreasing in m**. E := -ln lambda throughout.

---

## 0. Verdict, in one box

1. **Derivation from Landau-Widom / prolate concentration asymptotics: FAILED**,
   decisively and instructively. Every functional built from bulk concentration
   (Fuchs, LW plunge, Widom) predicts exponents of the wrong size *and* the
   wrong shape (sec. 2.2, 3.6). The margin is not a concentration phenomenon; it
   is a *discreteness* phenomenon (replacing the zero sum by its density
   integral makes lambda order one, sec. 2.0).
2. **Constant-density theory derived exactly and verified** (sec. 2.1, 3.1): for
   an arithmetic progression gamma_k = s0(k+1/2) the infinite-system margin is
   exactly 2pi/s0 (tight frame) for s0 <= pi/a and exactly **0** for s0 > pi/a
   (anti-periodization kernel). A strictly sub-Nyquist constant-density block
   costs *nothing*; the zeta margin is entirely a variable-density (chirp)
   effect.
3. **The law is sharpened, not derived.** The three-constant family is refit on
   a 9-point L-grid with Gcut-extrapolation, then broken out of its parameter
   degeneracy by two-parameter density deformations. Best global form, fitting
   the smooth staircase *and* the true-zeta five-window ladder with the *same*
   constants (sec. 4):

   **E(L) = -A + b e^{L/2}(L/2 + c0),  A = 11.11 +- 0.05, b = 1.51 +- 0.01, c0 = 5.04**

   (the repo's (10.2, 1.755, 4.0) is the same curve on the old fit window to
   +-0.01 - the parameters were degenerate; the deformation data selects
   (1.51, 5.04); joint fit over all 25 deformed points: A = 11.75, b = 1.39,
   c0 = 5.70, rms 0.14 - see sec. 3.3 for the spread).

   Invariant form (the new structural finding): with T* = 2 pi beta e^{2a/alpha},
   N(T*) the staircase count and D(T*) = (a/pi)T* - N(T*) = alpha T*/2pi the
   maximal Nyquist deficit,

   **E = -A + b [ N(T*) + mu D(T*) ],  mu = c0 + 1 ~ 6.0-6.7.**

4. **A new, sharp mechanism measurement** (sec. 3.4): the marginal
   exponent-worth of a single zero at height t is

   **f(t) ~ (pi^2/2) ln(e T*/t)  for t <~ 0.6 eT*,  = 0 beyond eT*,**

   with the coefficient measured at 0.98-1.04 x pi^2/2 across nine (t, L)
   combinations, and the support endpoint measured at the deficit-closure
   (capacity) height e T* at both L values. pi^2/2 is exactly the Landau-Widom /
   Bonami-Karoui exponent unit; e T* is exactly where a type-a function runs out
   of zero capacity for the staircase (D(eT*) = 0). Near the endpoint the
   profile is softened (consistent with (eT* - t)^{3/2} turning-point vanishing;
   two points only).
5. **E is NOT an additive per-zero functional.** The additive model
   SUM_j f(gamma_j) with the measured universal profile reproduces single-zero
   surgery but fails the alpha-deformation derivative by a factor ~3.4
   (sec. 3.3): zero-zero interactions (~15-25% of E) carry essential structure.
6. **beta-linearity is exact to 1%** and *is* the family (conductor)
   universality: E is linear in the height-scale beta with slope E + A, which is
   the measured q-scaling law T*_chi = (2pi/q)e^{L/2} of PROGRAM.md 2.16
   (sec. 4.1). The exact dilation identity lam_{a,beta*Gamma} =
   (1/beta) lam_{beta*a,Gamma} was verified to 2e-15 (V4).

---

## 1. Instruments and validation

`law_core.py` rebuilds `src/model_zeros.frame_form` with exact spherical-Bessel
overlaps: v_k(gamma) = sqrt(a(2k+1)/2) * 2(-i)^k j_k(gamma a), parity-split
blocks, top-two orders from mp.besselj + stable downward recurrence. ~100x
faster than the quadrature builder; that made the grids affordable.

Validation (`validate.py`, all PASS):
- V1 entrywise vs frame_form (m=8, 3 gammas): max difference **0.0** at dps 50.
- V2 staircase generator vs model_zeros.smooth_zeros: max diff 1.7e-49.
- V3 EXPECTED regression (L=2.485, m=48, Gcut=420): true zeros **2.68972e-10**,
  smooth **2.75124e-10** - all printed digits of src/model_zeros.py.
- V4 dilation identity (in run_alphabeta.py): relative error 2.2e-15.

---

## 2. Theory

### 2.0 The margin is a discreteness effect

Under the certified ledger lambda_min(L) is the lower frame bound of {e^{i g x}}
on [-a, a]. If the zero *sum* 2 SUM |phihat(gamma)|^2 is replaced by its density
integral INT |phihat(t)|^2 2 rho(t) dt (rho = (1/2pi) ln(t/2pi)), the resulting
operator is bounded below by ess-inf 2 rho > 0 on any band above 2pi - order
one, not e^{-22}. All exponential smallness lives in the sum-vs-integral gap:
phihat vanishes *at* the points and carries its mass *between* them. Any
derivation from smoothed (prolate-type) operators alone is therefore
structurally unable to produce the law; the discreteness must enter (this kills
the naive route and frames the problem in the clustered-node/Vandermonde
territory of agent-prior-art.md sec. 3.3).

### 2.1 Constant density: exact theory (the calibration)

For gamma_k = s0(k + 1/2), k >= 0, both signs, and phi in L^2[-a,a], Poisson
summation gives Q(phi) = SUM_{k in Z} |phihat(s0(k+1/2))|^2
= P INT_0^P |Phi(x)|^2 dx with P = 2pi/s0 and Phi(x) = SUM_n (-1)^n phi(x+nP):

- **s0 <= pi/a** (P >= 2a): translates don't overlap; INT |Phi|^2 = ||phi||^2;
  the system is a **tight frame, lambda = 2pi/s0 exactly**, for *every* phi.
- **s0 > pi/a** (P < 2a): Phi = 0 has nontrivial solutions - phi supported on
  two edge slivers of width s = 2a - P with matched alternating values - so
  **lambda = 0 exactly**, with an infinite-dimensional kernel.

Corollary: a strictly sub-Nyquist block of constant density imposes **zero**
cost in the operator limit. There is no "per-zero suppression cost" at constant
density; the zeta exponent is purely the cost of the *gliding* local spacing.
Measured confirmation in sec. 3.1.

### 2.2 The naive functionals and how they fail

With T* = 2pi e^{L/2} (Nyquist-crossing height), D(T) = (a/pi)T - N(T):

| model | predicted exponent | shape | verdict |
|---|---|---|---|
| M0 area deficit | 2pi INT_0^{T*}(a/pi - rho)dt = **T*** | e^{L/2} | wrong shape (known); accidental equality with E at L=2.485 only |
| M1/C8 LW plunge | 2 pi^2 D(T*)/ln(16 a T*) = **pi T*/ln(16aT*)** | e^{L/2}/L | wrong shape *and* even smaller |
| C7/Fuchs concentration | max_T -ln(1-lambda_{2#(T)}(aT)) | ~ 2 a gamma_1, linear in L | wrong size and shape; optimum degenerates to a band below the first zero or two |

Fuchs-model numbers (fit3.py; 1-lambda_n(c) ~ 4 sqrt(pi) 8^n c^{n+1/2}
e^{-2c}/n!, the same asymptotic Connes's sec. 6.4 comparator uses at n=4;
exact statements in results/agent-prior-art.md sec. 3):

| L | E_Fuchs (optimal T, #zeros vanished) | E measured |
|---|---|---|
| 2.200 | 12.98 (T=14.5, k=0) | 16.72 |
| 2.485 | 14.98 (T=14.5, k=0) | 21.99 |
| 2.996 | 18.67 (T=20.7, k=1) | 33.13 |
| 3.400 | 22.53 (T=20.7, k=1) | 44.53 |

The model's optimum never engages the staircase (k = 0-1), grows ~linearly in
L, and undershoots E increasingly - consistent with concentration being a valid
but far-from-optimal *strategy* (its lambda is an upper bound; the true
minimizer exploits the gaps that concentration wastes). The measured exponent
sits in the Widom n ln n regime, as the prior-art sweep anticipated, but no
bulk mode-counting assignment of (n, c) reproduces it; the mechanism is the
discrete chirp, not the plunge.

### 2.3 The capacity height eT*

D'(T) = (1/2pi) ln(T*/T): the deficit grows to D(T*) = T*/2pi at the crossing
and closes at **T_cap = e T*** (ln(T_cap/2pi) = L/2 + 1). By Jensen/Levinson
counting, a Paley-Wiener function of type a cannot vanish on the staircase
beyond the height where the cumulative count reaches its zero capacity -
heuristically exactly T_cap. The marginal experiment (sec. 3.4) finds the
per-zero worth supported on precisely [0, eT*], at both L values. This is the
empirical meaning of the law's "+c0": the exponent integrates structure up to
eT*, not T*.

### 2.4 The chirp correspondence (geometry, no rigor claimed)

Stationary phase pairs the support point x with the height r(x) = 2pi e^{2x}
via x = pi N'(r) = (1/2) ln(r/2pi): the test function
phi(x) = A(x) cos(pi e^{2x} + phi0) has phihat oscillating as
cos(pi N(r) + const), vanishing to leading order on the whole staircase, with
the support edge x = a mapping exactly to T*. The WKB phase S(x) = pi e^{2x} is
the natural "scaling-site" coordinate; the near-null keyhole vectors of
PROGRAM.md 2.13 should be this chirp (not re-verified here). The law's exponent
is the *failure* of this leading-order annihilation - its corrections are what
the experiments below measure.

---

## 3. Experiments

### 3.1 RUN 2 - arithmetic progressions (run_ap.py, data/ap.jsonl)

L = 2.485 (Nyquist spacing pi/a = 5.0569); each cell lambda at (m, Gcut):

| s0 | s0/(pi/a) | lam_inf theory | m=32 G420 | m=48 G420 | m=64 G420 | m=48 G840 | m=64 G840 |
|---|---|---|---|---|---|---|---|
| 3.2 | 0.633 | 1.9635 | 0.829 | 0.155 | 7.8e-3 | 0.729 | 0.235 |
| 4.6 | 0.910 | 1.3659 | 0.580 | 0.108 | 5.3e-3 | 0.503 | 0.167 |
| 5.0567 | 1.000 | 1.2425 | 0.172 | 2.7e-3 | 3.6e-6 | 0.120 | 6.8e-3 |
| 5.2 | 1.028 | **0** | 7.9e-3 | 9.8e-5 | 1.6e-7 | 2.1e-3 | 6.2e-5 |
| 5.5 | 1.088 | **0** | 3.4e-4 | 1.1e-6 | 1.1e-9 | 3.6e-6 | 4.2e-8 |
| 6.0 | 1.187 | **0** | 8.8e-6 | 5.4e-9 | 9.9e-13 | 9.2e-9 | 7.0e-12 |
| 7.0 | 1.384 | **0** | 1.2e-8 | 1.4e-12 | 1.9e-17 | 3.2e-12 | 8.0e-17 |

(L = 2.996 subset confirms the same dichotomy at its pi/a = 4.1944.)

Reading. **Undersampled side: collapse toward the exact-0 theory with m at
every Gcut** - a pure basis artifact with no floor, as the anti-periodization
kernel demands; contrast the chirped staircase, which *converges* in m.
**Oversampled side: values rise with Gcut toward 2pi/s0 but sag with m**: the
high-degree Legendre modes carry endpoint mass whose 1/r^2 transform tail lies
beyond Gcut, so the finite-Gcut Galerkin minimizer is a truncation-exploiting
artifact vector (tail mass ~ (2m+1)/(2a s0 Gcut) - order 0.1 at m=64,
Gcut=420). In the AP experiment Gcut->inf must be taken *before* m->inf; the
convergence-status columns are the honest record. The dichotomy itself - tight
frame vs exact kernel across s0 = pi/a - is unambiguous.

### 3.2 RUN 1 - the smooth-staircase law on a fine L-grid (run_smoothlaw.py)

lambda for the alpha=beta=1 staircase (excerpt; full table in
data/smoothlaw.jsonl):

| L | m=48 G840 | m=64 G840 | m=64 G1680 | m=64 G3360 |
|---|---|---|---|---|
| 2.2 | 5.1768e-8 | 5.0063e-8 | 5.3608e-8 | 5.4616e-8 |
| 2.5 | 2.6318e-10 | 2.5423e-10 | 2.7374e-10 | 2.7941e-10 |
| 2.8 | 4.8511e-13 | 4.6790e-13 | 5.0751e-13 | 5.1927e-13 |
| 3.1 | 2.7757e-16 | 2.6717e-16 | 2.9263e-16 | 3.0034e-16 |
| 3.4 | 4.1045e-20 | 3.9401e-20 | 4.3726e-20 | 4.5055e-20 |

m-drift 48->64 is <= 4% in lambda (<= 0.04 in E); Gcut-drift is geometric with
ratio q ~ 0.28 per doubling, so E was extrapolated to Gcut->inf (total
correction <= 0.10 in E; table in fits.py output). Fit of the extrapolated
9-point grid:

**ln lam = 11.128 - 1.5089 e^{L/2}(L/2 + 5.040), rms 0.0074** -
an order of magnitude tighter than the five-window fit, on a pure-density model
with no arithmetic. (At m=48 instead: b = 1.525, c0 = 4.98 - basis drift moves
the pair slightly along its degeneracy direction.)

Degeneracy note: on L in [2.2, 3.4] the repo's 1.755 e^{L/2}(L/2+4) equals
1.509 e^{L/2}(L/2+5.04) - 0.94 to +-0.01 - the same curve with the constant
absorbed in A. The L-scan alone cannot separate (b, c0); the deformations can.

### 3.3 RUN 3 - two-parameter staircases (run_alphabeta.py)

N_{alpha,beta}(T) = alpha (T/2pi) ln(T/(2 pi beta e)) + 7/8. Measured E
(deepest Gcut; m=64):

L=2.485: E(alpha): 24.86 (0.85), 23.08 (0.925), 21.81 (1), 20.70 (1.075),
19.88 (1.15); E(beta): 13.55 (0.75), 17.70 (0.875), 21.81 (1), 25.90 (1.125),
29.98 (1.25). L=2.996: E(alpha): 39.45, 35.78, 33.13, 30.93, 29.26;
E(beta): 21.66, 27.41, 33.13, 38.82, 44.51.

**Measured derivatives** (central, m=64; m=48 agrees to 0.3%):

| L | dE/dalpha | dE/dbeta |
|---|---|---|
| 2.485 | -15.97 | +32.82 |
| 2.996 | -32.55 | +45.65 |

**beta: exactly linear** (increments constant to 1%), with slope = E(1,1) + A
using the *independently fitted* A ~ 11.1 from RUN 1 (32.94 predicted vs 32.82
measured; 44.26 vs 45.65). So E + A is homogeneous of degree 1 in the height
scale beta - the family-universality law re-derived inside the frame model
(sec. 4.1).

**alpha: the discriminator.** Candidate functionals, each calibrated to match
E(1,1) + A, predict dE/dalpha at (L = 2.485, 2.996):

| candidate | pred dE/dalpha | measured | verdict |
|---|---|---|---|
| C1 b N(T*) | -87.6, -113.1 | -16.0, -32.6 | dead |
| C5 b N(eT*) (flat toll to capacity) | -38.6, -64.3 | | dead |
| C3 b area-deficit | -8.2, -22.5 | | dead (factor 2 low) |
| additive SUM_j (pi^2/2) ln(eT*/gamma_j)_+ (the measured marginal profile!) | -54.2, -100.3 | | dead => **E is not additive** |
| **b beta e^{2a/alpha}(2a + c0 alpha)** | -16.6, -31.9 (at c0=5.7) | | **passes** |

The passing form was found from the data: writing E = -A + F, the measured
log-derivatives dlnF/dalpha = -0.486, -0.736 at the two L's are matched by
F ~ alpha e^{2a/alpha}(2a/alpha + c0) = e^{2a/alpha}(2a + c0 alpha) with
alpha-independent A (solving the two-L system gives exponent p = 0.98 ~ 1 on
the alpha-prefactor and dA/dalpha = 0.7 ~ 0). Joint least squares over all 25
deep points (9 L-grid + 16 deformed; fit3.py):

**E = -11.75 + 1.391 beta e^{2a/alpha}(2a + 5.70 alpha), rms 0.136**
(E range 13.6-44.5); block-wise: L-grid-only (11.13, 1.509, 5.04, rms 0.007),
deformations-only (11.80, 1.408, 5.62, rms 0.17). The residual spread
(alpha = 1.15 worst, +0.32) is the honest error bar on the constants:
b = 1.39-1.51, c0 = 5.0-5.7, A = 11.1-11.8.

### 3.4 RUN 4 - the marginal worth of a single zero (run_marginal.py)

DeltaE(gamma_j) = ln lam(full) - ln lam(staircase minus gamma_j) >= 0,
everything else fixed. Stable across m = 48/64 and Gcut = 840/1680 to <= 0.02.
Compared to **(pi^2/2) ln(eT*/gamma_j)** (no fitted parameters):

L = 2.485 (eT* = 59.2), entries gamma: measured / prediction / ratio -
14.5: 6.923/6.932/**0.999** ; 20.7: 5.277/5.193/**1.016** ;
25.5: 4.256/4.155/**1.024** ; 33.6: 2.737/2.789/**0.981** ;
44.0: 0.724/1.462/0.50 ; 56.1: 0.049/0.261/0.19 ; 77.4 and beyond: <=0.036 -> 0.

L = 2.996 (eT* = 76.4): 14.5: 8.062/8.193/**0.984** ;
20.7: 6.485/6.454/**1.005** ; 25.5: 5.536/5.416/**1.022** ;
33.6: 4.214/4.050/**1.041** ; 44.0: 2.727/2.723/**1.001** ;
56.1: 0.855/1.522/0.56 ; 77.4 and beyond: <=0.046 -> 0.

Findings: (i) coefficient **pi^2/2 to 1-4%** over nine (t, L) points with
t <~ 0.6 eT*; (ii) support endpoint at the **capacity height eT*** at both L
(worth < 0.05 for every zero beyond it, measured out to gamma = 746);
(iii) edge softening in the last e-fold (ratios 0.5 at u := gamma/T* ~ 2.0,
0.2 at u ~ 2.6), consistent with (e-u)^{3/2} turning-point vanishing (two
points - suggestive only); (iv) insertions (midpoint extra zero) give
DeltaE = -5.35 (at gamma = 17.6), -0.32 (35.4), -0.00 (78.7) at L = 2.485 -
same profile, opposite sign, ~20% smaller than removals at matched height:
mild concavity; (v) the 13 measured marginals sum to 20.0 (L=2.485) and 27.9
(L=2.996) vs E_total 21.8 and 33.1 - with the six unmeasured low indices
interpolated the sums overshoot by ~20%: **E is close to, but not, a sum of
per-zero worths**, in agreement with the alpha-test's rejection of additivity.

### 3.5 The identified law vs the true-zeta ladder

Fitting the repo's five-window true-form operator estimates (f(2)..f(7),
RESULTS.md) with c0 pinned at 5.04:

**A = 11.106, b = 1.5122, rms 0.026** (residuals -0.021, +0.033, +0.011,
-0.040, +0.016) - versus rms 0.073 for the repo's (10.2, 1.755, 4.0) shape.
The true zeros and the smooth staircase share **all three constants**
(A: 11.106 vs 11.128; b: 1.5122 vs 1.5089) - the strongest statement yet of
2.17's "the law is a functional of N alone, at maximal rigidity": not just the
slope but the absolute normalization coincides to 0.02 in E.

---

## 4. The best-supported functional

Over the full deformation family N_{alpha,beta} and both zero sets (staircase,
true):

**E(a; alpha, beta) = -A + b beta e^{2a/alpha}(2a + c0 alpha)
  = -A + b [ N(T*) + mu D(T*) ] + O(1) b,   mu = c0 + 1,**

with T* = 2 pi beta e^{2a/alpha} the local-Nyquist crossing, N the counting
function, D(T*) = alpha T*/2pi the maximal Nyquist deficit, and

  A = 11.1-11.8, b = 1.39-1.51, c0 = 5.0-5.7 (mu = 6.0-6.7);
  cleanest single determination (L-grid, Gcut-extrapolated):
  **(A, b, c0) = (11.13, 1.509, 5.04)**.

Versus the measured (1.755, 4.0): same curve on the original fit window
(difference absorbed by A to +-0.01); the deformation experiments break the
degeneracy and select (1.51, 5.04). The per-zero reading of the old constants
("1.755 per zero below T*") does not survive: the correct structure is "b per
zero below the crossing **plus b mu ~ 9 per unit of maximal deficit**",
equivalently the bracket (2a + c0 alpha) whose two terms scale differently
under density deformations - support-Nyquist (2a) and density-prefactor
(c0 alpha).

### 4.1 Family universality is the beta-linearity

For real characters the zero density is (1/2pi) ln(qT/2pi): height-scale
beta = 1/q. The measured exact beta-linearity of E + A reproduces PROGRAM.md
2.16's "one decay constant in T*_chi = (2pi/q)e^{L/2}, conductor only in the
offset" as a *structural property of the frame model* rather than an empirical
parallel: E + A is degree-1 homogeneous in beta, and A (the offset) is
beta-independent.

### 4.2 Suggestive constants (labeled speculation)

b = 1.51 +- .06 is 3/2 within its error bar (also pi^2/6 = 1.645 at 2 sigma);
mu = 6.0-6.7 brackets 6 and 2pi; the marginal coefficient is pi^2/2 to 1-4%
(measured, not fitted); the capacity height is e T* exactly (measured). A
guess-form E ~ -A + (3/2) N(T*) + 9 D(T*)-type with the marginal law
f(t) = (pi^2/2) ln(eT*/t) is consistent with everything here but NOT derived.

---

## 5. What now looks provable (concrete targets)

**P1 (support endpoint; Jensen/Levinson route).** Any near-minimizer's phihat
must vanish (to accuracy e^{-E/2}) at every staircase point below
(1-o(1)) eT*, and the worth of zeros above eT* is O(e^{-E}): the capacity
statement D(eT*) = 0 turned quantitative. The measured f-support [0, eT*] is
exactly this; the proof ingredients are the classical zero-density bound for
PW_a functions plus the tight-frame identity of sec. 2.1 above the crossing.
This is the most theorem-shaped fact the data has produced.

**P2 (marginal law; BK route).** The Gateaux derivative of -ln lambda_min under
deletion of one frequency at height t equals (pi^2/2) ln(eT*/t)(1 + o(1)) for
t <= (1-delta) eT*. The constant pi^2/2 is the Landau-Widom/Bonami-Karoui
exponent unit ((BK) in agent-prior-art.md sec. 3:
lambda_n ~ (1/2) exp(-pi^2(n+1/2)/2 INT dt/(t E(t)^2))); the appearance of
exactly this constant in a *rank-one-removal derivative* suggests a
perturbative proof from the BK profile applied to the chirped system, and is
precisely the "locate lambda_min on the BK crossover" program the prior-art
sweep proposed - now with the measured target in hand.

**P3 (beta-homogeneity).** E(a, beta) + A = beta (E(a, 1) + A) for the pure
height-scale family - measured to 1%. Combined with the exact dilation
identity lam_{a,beta Gamma} = (1/beta) lam_{beta a, Gamma} (verified to 2e-15)
this pins the two-variable structure of the law; a proof would give the
conductor-universality of 2.16 for free.

**P4 (upper bound with the right shape).** A test-function construction
vanishing on the staircase through (1-delta) eT* (canonical product x window,
the chirp of sec. 2.4 as the leading profile) with cost
<= -A' + b' e^{L/2}(L/2 + c0') for *some* explicit constants - the measured
non-additivity (sec. 3.3-3.4) warns that per-zero cost accounting alone will
overshoot; the construction must let the zeros share their suppression (the
20% interaction).

What does *not* look provable from here: the exact constants (b, c0) by bulk
prolate asymptotics - sec. 2.2's failures are structural, not technical.

---

## 6. Caveats (complete list)

- All lambdas are Rayleigh-Ritz-in-m and truncated-in-Gcut; every table carries
  both labels; RUN 1 E's are Gcut-extrapolated with geometric-tail fits
  (correction <= 0.10, extrapolation uncertainty ~ 0.01-0.03 in E). Deformation
  points are raw at their deepest Gcut (drift <= 0.1 in E, partially
  common-mode in derivatives).
- The window is small-a (L = 2.2-3.4 grid; 1.75-4.025 with the repo ladder):
  (2a + c0 alpha) with c0 ~ 5 means the "constant" term still dominates; all
  asymptotic readings are extrapolations. Sub-leading terms (e.g. + d ln in the
  bracket) are not excluded; the quoted constant ranges are the honest spread.
- The marginal profile is measured at 13 heights x 2 L on the smooth staircase
  only; single-zero removal is a finite (DeltaE ~ 7) perturbation, not an
  infinitesimal one; "(pi^2/2)" is the observed plateau of ratios, not a fit
  with an error model.
- The alpha-family's first zero moves with alpha; all candidate integrals were
  evaluated as *discrete sums/exact formulas* at the actual finite a - the
  asymptotic small print of each candidate does not affect the rejections
  (they fail by factors 2-5, far above every stated drift).
- Everything here concerns the *density functional* (staircase); agreement of
  the true-zeta form is inherited through the repo's five operator estimates
  (themselves Rayleigh-Ritz upper bounds, deepest-m).

## 7. Reproduction

```
results/agent-law-theory/
  law_core.py      exact-Bessel frame builder + staircase/AP/zero generators
  validate.py      V1-V3 (run first; ~1 min after zero cache)
  runs.py          json-lines runner
  run_smoothlaw.py RUN 1 (L-grid)              -> data/smoothlaw.jsonl
  run_ap.py        RUN 2 (APs)                 -> data/ap.jsonl
  run_alphabeta.py RUN 3 (alpha/beta + V4)     -> data/alphabeta.jsonl
  run_marginal.py  RUN 4 (single-zero surgery) -> data/marginal.jsonl
  theory.py        candidate functionals, exact prolate spectrum, Fuchs model
  fits.py          tables + (b, c0) refits + Gcut extrapolation
  analysis2.py     discrete-functional refit, marginal-profile test, alpha/beta
  fit3.py          joint global fit + true-form refit + Fuchs numbers
```
Total compute ~ 40 min on 3 cores. No repo file was modified.
