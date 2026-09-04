# Actual-prime mass-radialization finite-scale lab

**Verdict.**  No actual-prime counterexample to mass radialization was found,
and no fixed-power radialization theorem was proved.  On the tested scales the
arbitrary-interval directional extremizers are broad prime intervals, not
singletons, and both the high-subband and full-QP antipode radii remain much
larger than the directional mass.  This is compatible with a fixed-power
upper law, but is not asymptotic evidence strong enough to choose a power.

The fail-fast limitation is definitive: at the strip exponent `d=.019`, every
event in the threshold premise must contain at least `N^.981` primes.  At all
accessible scales this exceeds the *entire* fixed-width shell prime count.
Thus the true implication

```text
E_N^->=N^(-.019)  ==>  r_+(H_Y)>=N^(-c)
```

has no nonvacuous finite instance in this lab.  Fractional-shell and fixed-cell
experiments below are diagnostics only; they do not test that premise.

Replay is in
`src/qp_radialization_lab.py`; tests are in
`src/test_qp_radialization_lab.py`.

---

## 1. Exact finite formulations

For an allowed half-integer center `Y`, use every actual prime power in

```text
[Y exp(-.2),Y exp(.2)]
```

and its nonzero node `u=|log(n/Y)|`.  Write

```text
a(t)=(cos(tu_1),...,cos(tu_m)).
```

Two ordinate bands are kept distinct:

```text
K_N=[N^(1/2),N^(3/2)],
H_Y=[Y^.01,Y^(50/33)].
```

The first is the exact Turan subband on which `E_N^-` is measured.  The second
is the full QP band bounded by DPA/QP.  Since `K_N` is contained in `H_Y` in
the tested range, monotonicity gives

```text
r_+(K_N;S_Y)<=r_+(H_Y;S_Y).
```

For a finite pool `T` of heights, the primal LP is

```text
maximize r
subject to sum_(t in T) w_t a(t)=-r 1,
           sum w_t=1,  w_t>=0.                       (1.1)
```

A finite-pool solution is a continuum-feasible antipode and hence a lower
bound for the continuum radius.  The dual polynomial is

```text
f_y(t)=sum_j y_j cos(tu_j),       sum_j y_j=-1,
```

and `sup_H f_y` is an upper bound for every feasible radius.  The code solves
the finite dual, locates its largest validation-grid peaks, adds them to the
pool, and repeats.

The gap between the validation grid and the continuum is guarded
analytically.  If its spacing is `h`, then

```text
L=sum_j |y_j|u_j,        C=sum_j |y_j|u_j^2,
sup_H f_y <= max_grid f_y + min(Lh/2,Ch^2/8).         (1.2)
```

The quadratic term follows by interpolation between the two endpoints of
each grid cell.  This is a valid continuum estimate for the displayed
floating coefficients.

The mass-normalized directional quantity is scanned exactly over all
contiguous prime intervals at each grid height:

```text
E(I,Y,t)=-N^(-1)sum_(p in I)cos(t log(p/Y)).          (1.3)
```

A linear-time maximum-subarray calculation handles the interval switch at
each height.  Bounded minimization refines the winning fixed interval.  The
continuum upper guard uses

```text
C_E=N^(-1)sum_(all shell primes p) log(p/Y)^2,        (1.4)
```

which dominates every interval and therefore remains valid when the winning
interval changes between grid points.

The code also reports:

- the exact mass-normalized singleton floor `1/N`;
- the required threshold class `#I>=ceil(N^.981)`;
- the whole-shell direction;
- an optional shell partition into fixed log-width `.1` cells.

The last family resembles fixed pieces used in phase localization, but is not
equivalent to the threshold class: the original Turan interval may itself be
short and need not align with this particular shell grid.

### Certification boundary

Equations (1.1)--(1.4) and the derivative guards are exact mathematical
identities.  The reported endpoints are nevertheless **not interval-arithmetic
certificates**: SciPy/HiGHS and the cosine evaluations are floating point.
Primal equality residuals were between about `10^-15` and `2.4*10^-9` in the
reported runs.  Accordingly the brackets below are analytically guarded
floating brackets, not theorem-grade rational enclosures.

---

## 2. Main scale run

Parameters are `Y=N+1/2`, shell width `.2`, high aperture `A'=1.5`, full
aperture `A=50/33`, antipode phase mesh at most `.08`, and directional phase
mesh at most `.06`.  Here `m_pp` and `m_p` are the actual shell prime-power
and prime counts.

| `N` | `m_pp/m_p` | `r_+(K_N)` | `r_+(H_Y)` | arbitrary-interval `E` | winning primes (`count`) |
|---:|---:|---:|---:|---:|:---|
| 70 | 9/7 | [.427472,.428143] | [.432432,.432895] | [.0678416,.0678466] | 59--83 (7) |
| 200 | 17/15 | [.316470,.316819] | [.354074,.354582] | [.0345857,.0345995] | 167--229 (12) |
| 600 | 40/36 | [.260054,.260515] | [.260847,.261242] | [.0224490,.0224558] | 523--733 (32) |
| 1000 | 61/58 | [.219800,.220032] | [.221057,.221424] | [.0203919,.0204006] | 821--1123 (47) |
| 1800 | 99/94 | [.185728,.186038] | [.187632,.188000] | [.0140059,.0140126] | 1511--2131 (82) |

The LP primal used exactly `m_pp` positive support heights in every row.  The
directional maximizers used 80--100 percent of the shell primes except at
`N=70`, where the entire shell also wins.  Their refined heights were about

```text
409, 1254, 706, 10408, 53216,
```

respectively.  There is no singleton extremizer in this run.

The whole-shell and optional fixed-cell values were:

| `N` | whole-shell `E` | fixed `.1`-log-cell `E` | primes in winning fixed cell |
|---:|---:|---:|---:|
| 70 | [.0678416,.0678466] | [.0285581,.0285615] | 2 |
| 200 | [.0312686,.0312830] | [.0291249,.0291296] | 6 |
| 600 | [.0208237,.0208316] | [.0147191,.0147226] | 12 |
| 1000 | [.0203320,.0203401] | [.0106197,.0106217] | 17 |
| 1800 | [.0131221,.0131297] | [.00813692,.00813969] | 27 |

As a consistency check, the whole-shell lower value exceeded even

```text
(upper guard for r_+(K_N)) * m_p/N
```

by factors `1.58, 1.32, 1.33, 1.59, 1.35`.  This is the expected pairing
inequality `E_shell>=r_+(K_N)m_p/N`, with room larger than the numerical
guard.  It does not give the missing reverse inequality.

---

## 3. The strip threshold is unavailable at these scales

For `d=.019`, the minimum atom count and the actual shell count are:

| `N` | `ceil(N^.981)` | all shell primes | `N^(-.019)` | absolute mass ceiling `m_p/N` |
|---:|---:|---:|---:|---:|
| 70 | 65 | 7 | .922 | .100 |
| 200 | 181 | 15 | .904 | .075 |
| 600 | 532 | 36 | .886 | .060 |
| 1000 | 878 | 58 | .877 | .058 |
| 1800 | 1562 | 94 | .867 | .0522 |

Thus `E>=N^(-.019)` is not merely absent: it is impossible in each sampled
base-center shell at these tiny scales.  The implementation returns
`available=false` rather than substituting the earlier diagnostic choice
`d=.66`.

The singleton floor is also separated cleanly.  It is `1/N`, whereas the
observed arbitrary-interval values are between roughly `5/N` and `25/N`.
This confirms at finite scale that mass normalization removes singleton
saturation without making singletons the relevant extremizers.

---

## 4. Center variation

To check that `Y=N+1/2` was not hiding a simple scale-separated failure, a
small grid of other legal half-integer centers was run.  Values below are
rounded diagnostics; each radius was computed with its own continuum guard.

| `N` | `Y` | `r_+(K_N)` | `r_+(H_Y)` | arbitrary `E` |
|---:|---:|---:|---:|---:|
| 200 | 200.5 | .3165 | .3543 | .03459 |
| 200 | 250.5 | .2798 | .3057 | .03786 |
| 200 | 300.5 | .2528 | .2955 | .04580 |
| 200 | 400.5 | .2382 | .3036 | .05755 |
| 600 | 600.5 | .2603 | .2610 | .02245 |
| 600 | 900.5 | .2033 | .2405 | .02660 |
| 600 | 1200.5 | .1842 | .2264 | .03591 |

In this sparse grid the high-band radius was largest near `Y=N`, while the
mass-normalized direction was largest at the largest tested center.  Taking
the separate sampled suprema still produced no adverse scale separation:

```text
N=200:  sup_sample E / sup_sample r_+(K_N) about .18,
N=600:  sup_sample E / sup_sample r_+(K_N) about .14.
```

This is not a computation of the supremum over every allowed half-integer
center.

---

## 5. What the finite ratios do and do not say

At the base centers, using radius midpoints,

```text
E/r_+(K_N) = .159, .109, .086, .093, .075.
```

The pointwise exponents solving `E=r^lambda` are approximately

```text
3.17, 2.93, 2.82, 2.57, 2.54.
```

This finite table is compatible with `E<=C r^lambda` for several fixed
positive powers and modest constants.  It does not establish boundedness of
any ratio as `N` tends to infinity, and fitting a slope to five highly
preasymptotic points would have no theorem-grade meaning.  Conversely, no
ratio grows in a way that suggests a finite-scale actual-prime
counterexample.

The full-band radii matter for the weakest sufficient threshold adapter:
DPA bounds `r_+(H_Y)` directly, so a theorem

```text
E_N^->=N^-d  ==>  r_+(H_Y)>=N^-c
```

would already suffice.  The high-band radii are the sharper objects needed
for the direct `MRAD_hi` formulation and for the whole-shell pairing.  The
lab reports both rather than conflating them.

---

## 6. Binary status

```text
actual nodes and continuum derivative guards:     IMPLEMENTED;
high/full band distinction:                        IMPLEMENTED;
mass-normalized singleton floor:                   EXACT;
strip threshold d=.019 tested nonvacuously:        NO (structurally unavailable);
finite actual-prime MRAD counterexample:            NOT FOUND;
fixed-power MRAD or INV theorem:                    NOT PROVED;
QP or a uniform zeta strip:                         NOT PROVED.
```

Replay:

```bash
PYTHONPATH=src python3 -m pytest -q src/test_qp_radialization_lab.py
PYTHONPATH=src python3 src/qp_radialization_lab.py --N 70 200 600 1000 1800
```

The first command currently reports `8 passed`.
