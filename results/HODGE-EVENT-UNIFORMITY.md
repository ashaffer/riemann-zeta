# Hodge event-uniformity fail-fast audit

**Superseded verdict (2026-08-02):** the full-domain strengthened Hodge
inequality has a stable numerical counterexample.  A cutoff-free
zero-extended Legendre section at the activation of `5` has strengthened
ratio `1.0000575016` and Schur minimum `-8.9466e-5`; see
`PLAIN-LEGENDRE-HODGE-FALSIFIER.md`.  The positive hat scans below remain
valid diagnostics on boundary-vanishing subspaces, but they do not support
extension to the logarithmic form domain.

Status: the Hodge loss itself has a universal functional-calculus smoothing
bound, but the proposed domination by the new Weil Schur surplus is a
strictly stronger, zeta-specific quotient-energy observability statement.
It does not follow from old positivity, shell isometry, collar positivity, or
even strict positivity of the enlarged abstract Weil block; a rational
countermodel is formalized in Lean.  No finite-section counterexample was
found for the actual zeta matrices on the complete available consecutive
prime-power midpoint grid.  The hardest event remains the activation at `5`;
its direct Hodge surplus/loss constant decreases under matched refinement but
is still `7.16` at old degree `361`.  All spectral claims below are finite
Galerkin diagnostics, 2026-08-02.

## 1. The direct quantity

Retain the notation

`A=F+R-H`, `R=Y*Y`,

`tau=sqrt(S/(S+q^2 I))`, `K=I-tau`.

The preferred sufficient condition for the Hodge graph is

`A >= B := Y* K^2 Y`.

The diagnostic computes the best constant in this inequality,

`c_H = sup {c : A >= c B}`.

When `A>0`, including when `B` is singular, this is evaluated stably as

`c_H = 1/lambda_max(B,A)`.

Thus the proposed Hodge inequality passes exactly when `c_H>=1`.  This is the
primary statistic in this audit; the minimum generalized capacity ratio is
reported only as a secondary control.

The condition is sufficient rather than necessary.  If

`B_0=F+Y* tau^2 Y`, `C=Y*(tau-tau^2)Y`,

then the exact graph capacity satisfies

`G_tau=F+Y*(2tau-tau^2)Y+C B_0^dagger C`,

so

`G_tau-H=(A-Y*K^2Y)+C B_0^dagger C`.

The direct target deliberately discards the final positive correction.

## 2. Smoothing majorants

Functional calculus gives the exact pointwise representation and bounds

`K^2 = q^4 (S+q^2 I)^-1`

`        * ((S+q^2 I)^(1/2)+S^(1/2))^-2`,

`K^2 <= q^4/[4 S(S+q^2 I)] <= q^4/(4S^2)`.

Consequently either stronger inequality

`A >= (q^4/4) Y* [S(S+q^2I)]^-1 Y`,

or

`A >= (q^4/4) Y* S^-2 Y`

would prove the Hodge target.  These are attractive because the omitted
return loss is explicitly two orders smoothing in the old incidence
operator.  No commutation of `F`, `H`, and `Y` is used.

## 3. True consecutive-event grid

For activation locations `e_i=2 log(n_i)`, the scan uses the exact midpoint
step

`[(e_(i-1)+e_i)/2, (e_i+e_(i+1))/2]`,

which contains exactly the prime-power event `n_i`.  Collar hat widths are
kept at approximately `0.42` times the old hat width, subject to a minimum
collar dimension which scales with old resolution.  The default cutoff law
reproduces approximately

`1200,1600,2000,2400` at old degrees `61,121,181,241`,

with Simpson interval spacing about `0.01`.

The complete event catalog available in `PRIME_POWERS` was scanned from the
activation at `3` through the activation at `61` at old degree `61`.  Every
full endpoint was positive and every direct Hodge constant exceeded one.
The minimum was

`c_H=93.94`

at the activation at `5`.  At degree `121`, the early events through `16`
were rescanned; event `5` remained the minimum, at `14.83`.  Later coarse
events have much larger reserves because their event degree `q^2` is small
relative to the accumulated old incidence scale.

The driver [hodge_event_scan.py](../src/hodge_event_scan.py) records for every
row the event index and prime power, `q^2`, both endpoints of `spec(S)`,
`q^2/lambda_min(S)`, the exact and lower Hodge ratios, `c_H`, loss rank, and
cutoff controls.

## 4. Hard-event refinement

The controlling true midpoint step is

`2.995732273554 -> 3.555348061489`,

which activates `5`.  Matched refinement gives

| old / collar degree | cutoff | fresh ratio | full ratio | Hodge lower ratio | `c_H` | `c_H q^2/lambda_min(S)` |
|---:|---:|---:|---:|---:|---:|---:|
| `61 / 13` | `1206.7` | `0.9990673` | `1.0006962` | `1.0006889` | `93.9377` | `16.2645` |
| `121 / 26` | `1606.7` | `0.9979953` | `1.0001239` | `1.0001156` | `14.8346` | `2.56848` |
| `181 / 39` | `2006.7` | `0.9977829` | `1.0000822` | `1.0000735` | `9.41533` | `1.63018` |
| `241 / 53` | `2406.7` | `0.9976623` | `1.0000602` | `1.0000578` | `8.13437` | `1.40840` |
| `361 / 80` | `3206.7` | `0.9974918` | `1.0000214` | `1.0000188` | `7.15917` | `1.23955` |

Across these runs,

`q^2=1.439525031107`,

`lambda_min(S)=8.314156...`,

so `q^2/lambda_min(S)=0.17314143` is effectively resolution invariant.  The
spectral widening occurs at `lambda_max(S)`, which grows from about `11.87`
to `13.63`.

At degree `241`, the sharp functional-calculus majorant has domination
constant `7.56898`, and the simpler `S^-2` majorant has constant `6.56928`.
Both stronger sufficient inequalities therefore still pass.  Raising the
cutoff by twenty percent changes the direct constant only from `8.13437` to
`8.13613`, while leaving the sign and all endpoint controls unchanged.

## 5. What the drift says

There is substantial refinement drift: the coarse constant `93.9` is not a
uniform reserve.  Nevertheless, the last three direct constants are

`9.42, 8.13, 7.16`,

still well above the required value one.  The normalized sequence

`c_H q^2/lambda_min(S) = 2.57,1.63,1.41,1.24`

from degrees `121,181,241,361` is suggestive of a limiting value near one.
If that pattern were real, it would predict

`c_H roughly lambda_min(S)/q^2 = 5.776`

for the hardest event, leaving a fixed factor above the Hodge threshold.
This is a heuristic pattern, not an extrapolation certificate: the available
resolutions do not exclude a later bend toward one or below.

No event-uniform theorem follows from the data.  The cleanest surviving
analytic target is the stronger smoothing inequality

`F+R-H >= (q^4/4) Y* S^-2 Y`

on every consecutive event.  It passes the hardest tested refinement by a
factor `6.57`; proving it would imply the exact Hodge loss inequality.  A
weaker possible law suggested by the drift is

`c_H q^2/lambda_min(S) >= 1`,

but it currently has no structural derivation.  Generic translation
geometry does not force either statement, and `A=F+R-H` still contains the
full Weil-Schur surplus.  The audit therefore identifies a numerically stable
zeta-specific target; it does not prove RH or uniform positivity.

## 6. Exact Schur and observability boundary

Let the enlarged Weil form on the orthogonal old/collar decomposition be

`Q_b = [[A_0,X],[X*,C]]`, with `A_0=Q_a>0`.

The incidence-capacity algebra gives the exact identity

`Sigma := F+R-H = C-X* A_0^-1 X`.

Thus `Sigma` is not an independent positive reserve: it is exactly the Schur
complement of the enlarged Weil form.  With

`T=(I-tau)Y`,

the direct Hodge target has the following equivalent forms:

`Sigma >= T*T`,

`Q_b-diag(0,T*T) >= 0`,

`inf_u Q_b(u+w) >= ||T w||^2` for every collar vector `w`,

`||A_0^(-1/2)Xw||^2+||Tw||^2 <= <Cw,w>`.

In particular it asserts that the boundary-return trace `T` is a contraction
from the quotient by the embedded old space, equipped with the reduced Weil
energy, into the old incidence-coordinate space.  Ordinary new-window
positivity pays only the first term in the last display.  The Hodge target is
strictly stronger.

This also explains why thin-collar uncertainty is insufficient.  It gives a
large lower bound on the raw diagonal `<Cw,w>`, but the old cross term
`X*A_0^-1 X` can cancel that bound arbitrarily closely.  What is needed is a
form-relative estimate after this cancellation, not another raw collar
floor.

## 7. Rational generic obstruction

The obstruction can be made entirely rational.  Take old degree `31/75`,
shell increment `3`, and incidence pieces

`E_old = [[1,8/5],[8/5,257/100]]`,

`E_shell = [[3,-8/5],[-8/5,64/75]]`.

Both are positive semidefinite, the old Weil gap on the old coordinate is
`44/75`, and the shell adds exactly `3 I` there.  The cross entries cancel,
so after subtracting the new degree `256/75` the enlarged Weil block is

`diag(44/75,1/100)>0`.

The fresh and return capacities are nevertheless

`F=1/100`, `R=256/75`,

while `tau=1/2` because `tau^2(1+3)=1`.  Hence

`F+R-H=1/100 < (256/75)(1-1/2)^2=64/75`.

So even strict old and new positivity plus the one-event shell algebra do not
force Hodge domination.  Lean theorem
`rational_hodge_event_countermodel` checks every displayed identity and
positivity assertion without research axioms.

## 8. Verdict and next theorem

What is proved uniformly is the event-independent smoothing law for the
loss.  What remains unproved is the zeta-specific lower bound for the reduced
surplus.  The cleanest surviving theorem is therefore

`inf_u Q_b(u+w) >= (q^4/4) ||S^-1 Yw||^2`

on every true consecutive event collar (or the sharper version with
`[S(S+q^2I)]^-1`).  This is a quantitative continuation/observability theorem
for the explicit combined prime--gamma kernel.  Proving it would imply the
Hodge graph certificate and propagate positivity; merely assuming it would
hide the remaining RH content.

## 9. Reproduction

Complete coarse event scan:

```text
python3 src/hodge_event_scan.py \
  --start-prime-power 3 --end-prime-power 61 \
  --old-degrees 61 --grid-size 3
```

Matched hard-event refinements:

```text
python3 src/hodge_event_scan.py \
  --start-prime-power 5 --end-prime-power 5 \
  --old-degrees 121 181 241 --grid-size 3
```

The degree-361 hard-event run takes several minutes on the current machine.
