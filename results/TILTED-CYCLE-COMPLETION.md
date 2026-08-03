# Tilted cycle-completion checkpoint

Status: the tilted-graph capacity formula and its monotonicity are exact.
Arbitrary fixed tilts drift upward under refinement, while the
incidence-normalized scalar and operator-Hodge tilts survive the tested
width-matched single-event steps.  The
operator-Hodge loss is smoothing and supplies the surviving analytic target.
All reported spectra are finite Galerkin diagnostics, not a proof of RH,
2026-08-01.

## 1. Exact graph capacity

Let the orthogonal fresh and return response factors satisfy

`Z_F* Z_F=F=G_old+G_shell`, `Z_R* Z_R=R=G_return`.

For the vertical graph

`J_t=range(x -> (Z_F x,t Z_R x))`, `0<=t<=1`,

orthogonal projection gives the exact response capacity

`G_t=(F+tR)(F+t^2 R)^dagger(F+tR)`.

This notation is important: a horizontal concatenation would have unchanged
range for every nonzero `t` and would not give this formula.  Explicit
square-root factors reproduce the displayed formula to at worst `9.1e-15`
in the scans below.  At the endpoints,

`G_0=F`, `G_1=F+R`.

Thus `t=1` is the full response range and exactly the Weil-Schur equivalence
boundary.  The noncommuting loss identity is

`F+R-G_t=(1-t)^2 [R-t^2 R(F+t^2R)^dagger R] >= 0`.

The bracket is a parallel sum.  It follows that `G_t` is Loewner-increasing
on `[0,1]`, so every pass set is one interval `[t_*,1]`.  It also gives the
simple lower bound

`G_t >= F+(2t-t^2)R`.

Consequently the additive sufficient condition is

`F+(2t-t^2)R >= H`,

or equivalently, with the full surplus `S_b=F+R-H`,

`S_b >= (1-t)^2 R`.

Existence of some section-dependent `t<1` follows by continuity whenever the
full inequality is strict.  Only a tilt fixed independently of the unknown
Weil margin, or a structurally forced tilt, is a meaningful new premise.

## 2. Fixed scalar tilts

Across the four original transitions, the exact thresholds are

| transition | `t_*`, `121/40` | `t_*`, `181/60` |
|---:|---:|---:|
| `1.750 -> 2.485` | `0` | `0` |
| `2.485 -> 2.996` | `0` | `0.154469` |
| `2.996 -> 3.555` | `0.739536` | `0.793054` |
| `3.555 -> 4.040` | `0.506731` | `0.703701` |

Thus `t=3/4` passes all four at `121/40`, but fails the controlling third
transition at `181/60`, where its ratio is `0.99996224`.  There `t=4/5`
passes with ratio `1.00000540`, and even its additive lower bound
`F+(24/25)R` passes with ratio `1.00000479`.

The next refinement rejects that constant too:

| pair | resolution | cutoff | `t_*` | `G_0/H` | `G_1/H` | canonical margin |
|---:|---:|---:|---:|---:|---:|---:|
| `2.996 -> 3.555` | `241/80` | `2000` | `0.807984` | `0.997640` | `1.00005629` | `2.37e-9` |
| `2.996 -> 3.555` | `241/80` | `2400` | `0.807239` | `0.997644` | `1.00006035` | `2.60e-9` |

At cutoff `2400`, `G_(4/5)/H=0.99999443` and the additive `24/25` ratio is
`0.99999378`.  The threshold cutoff drift is only `7.5e-4`.  Although
`1-t_*` is still about `0.19`, tens of millions of times the canonical
margin, the sequence `0.7395,0.7931,0.8072` supplies no fixed continuum
reserve.

## 3. Incidence-normalized scalar and Hodge tilts

The uniquely normalized propagated old column suggests the non-arbitrary
scalar

`alpha=sqrt(D_a/D_b)`.

The even simpler premise is therefore

`S_b >= (1-alpha)^2 R`,

equivalently

`F+(2alpha-alpha^2)R >= H`.

For the refined original hard pair, `alpha=0.923262`.  At `241/80` its exact
graph ratios are `1.00005286` and `1.00005693` at cutoffs `2000` and `2400`;
the additive coefficient `2alpha-alpha^2=0.994111` is well above the required
`0.96344` and `0.96316`.  The smaller choice `D_a/D_b=0.852412` also passes
this pair, but is not stable out of sample.

There is also a canonical mode-dependent graph.  On the old space put

`S=A*A`, `S_0=S+q^2 I`, `tau(S)=sqrt(S/S_0)`.

In the normalized return-coordinate realization, `tau(S)` acts after the
collar-to-return response map, so no identification of old and collar spaces
is needed.  If `Y` is that response factor, its graph capacity is

`G_tau=(F+Y* tau Y)(F+Y* tau^2 Y)^dagger(F+Y* tau Y)`.

The construction is canonical once the return parametrization is retained;
it cannot be recovered from the Gram matrix `R` alone.  Also, reusing `tau`
as the external graph tilt is a structured ansatz, not something forced by
the dual equations.  Under the inductive old-positivity hypothesis
`S>=D_a I`, one has `tau>=alpha I`, and its additive Hodge lower bound
dominates the scalar-alpha bound.

The implementation separately checks the actual return-coordinate factor:
`Z_R*Z_R=R`, operator tilt `I` gives `F+R`, and operator tilt `tI` agrees with
the scalar graph formula.  Representative relative errors are respectively
`1.1e-15`, `9.7e-17`, and `3.2e-18`.

More precisely, writing `R=Y*Y`, the exact graph loss gives

`G_tau >= F+Y*(2 tau-tau^2)Y`.

The operator-valued sufficient target is therefore

`F+R-H >= Y*(I-tau)^2Y`.                                      `(Hodge)`

This is sharper than replacing `tau` by its scalar lower bound.  It also has
a genuine smoothing feature: functional calculus gives

`(I-tau)^2 <= q^4/(4 S^2)`.

Thus the capacity which may be discarded is controlled by two inverse powers
of the old incidence operator.  This targets the low old-incidence sector
rather than asking for a fixed fraction of the entire return channel.

## 4. Out-of-sample stress test and the event-grid correction

The deliberately broad exploratory grid `4.04,4.6,5.2,5.8` initially looks
unfavorable.  At `121/40` its thresholds are

`0.893665, 0.871889, 0.770579`.

At `181/60`, the first two become `0.927984` and `0.936184`.  On
`4.6 -> 5.2`, scalar `alpha=0.901496` fails with ratio `0.99998709`; the
mode-dependent Hodge graph improves this only to `0.99999190`, still below
one.  A fixed `t=0.94` and its additive coefficient `0.9964` pass all finite
sections tested, but this observation alone has no independent content.

Those broad steps each cross two prime-power activations.  They are useful
stress tests but are not the intended adjacent-event recursion.  Splitting at
one event per step and scaling the collar discretization to its physical
width gives the valid exploratory grid

`4.04, 4.28, 4.60, 4.95, 5.20`.

At `121/10`, the fresh capacity already passes the events at `8`, `9`, and
`13`.  Only the event at `11`, `4.60 -> 4.95`, needs return capacity:

| resolution | cutoff | `F/H` | `t_*` | scalar-alpha | additive alpha | Hodge | full |
|---:|---:|---:|---:|---:|---:|---:|---:|
| `121/10` | `1600` | `0.9993793` | `0.408782` | `1.00033075` | `1.00033075` | `1.00033134` | `1.00033348` |
| `181/15` | `2000` | `0.9991391` | `0.662929` | `1.00010750` | `1.00010750` | `1.00010811` | `1.00011028` |
| `181/15` | `2400` | `0.9991394` | `0.662601` | `1.00010772` | `1.00010771` | `1.00010832` | `1.00011049` |
| `241/20` | refined | below `1` | `0.721034` | `1.00007345` | passes | `1.00007406` | `1.00007625` |

Here `alpha=0.946531`, and the Hodge spectrum at `181/15` is approximately
`[0.946531,0.961389]`.  The cutoff comparison is stable.

Fixed `121/40` collars on the two thinnest event intervals were invalid: the
collar hats became much narrower while the cutoff stayed `1600`, and even the
full equivalence endpoint fell spuriously to about `0.88`.  Those rows are
excluded rather than interpreted as evidence about zeta or RH.

The midpoint construction was then continued through the consecutive
prime-power activations

`16,17,19,23,25,27,29,31,32,37,41,43,47`.

At old degree `121`, with collar degrees `5--10` scaled to physical interval
width, every fresh ratio already exceeds one.  A later refinement used the
single-event step

`5.200000 -> 5.605802066296`,

where `F/H=1.00009464`.  Refining that step to `181/15` at cutoff `2400`
makes fresh capacity cross slightly below one but leaves a substantial forced
tilt reserve:

| event | `F/H` | `t_*` | scalar-alpha | additive alpha | Hodge | full |
|---:|---:|---:|---:|---:|---:|---:|
| `16` | `0.99988256` | `0.416011` | `1.000048533` | `1.000048533` | `1.000048536` | `1.000048547` |

Here the Hodge spectrum is approximately
`[0.988874326,0.991659575]`.  These event supports and discretizations are
exploratory choices, and every number in this section remains finite-
dimensional.  Their value is fail-fast discrimination: unlike arbitrary
fixed tilts, the degree-normalized and Hodge candidates have not yet failed
on a valid adjacent-event section.  A separate `181/16` check of the midpoint
activation-`19` step `5.7777 -> 6.0799` gives `F/H=0.99927350`,
`t_*=0.428952`, scalar-alpha `1.00018248`, Hodge `1.00018263`, and full
`1.00018316`.

## 5. Verdict

The mixed tilted family is not generically pruned.  It yields an exact proper
subspace criterion for every prescribed `t<1`, and the incidence-normalized
choice survives the tested, numerically valid single-event refinements
through the activation at `47`.

It is not a solution either.  The new analytic target is the cofinal
single-event inequality

`F+R-H >= (1-sqrt(D_a/D_b))^2 R`.

Proving it would give the additive alpha certificate and hence the tilted
graph completion at every event.  The sharper and now preferred target is the
operator inequality `(Hodge)` above; its `S^-2` loss may permit an estimate
which the scalar comparison hides.

Generic translation geometry cannot prove either statement: the existing
strict-positive countermodels allow arbitrary return-free defect index, and
`t=1` remains exactly the original Weil Schur condition.  The premise must
therefore come from a zeta-specific comparison between the full surplus and
the smoothing return loss.  The present finite Galerkin data identify that
target and pass a fail-fast checkpoint; they do not establish it uniformly
or imply RH.
