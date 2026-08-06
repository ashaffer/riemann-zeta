# Metric-shift versus boundary-phase covariance: fail-fast audit

Status: a constant, spectral-parameter-independent relabeling of the full
phase-labelled boundary family is not a generic consequence of changing the
positive metric from `T_(a,lambda)=A_a-lambda I` to
`T_(a,mu)=A_a-mu I`.  The pointwise covariance fails in a genuine coercive
continuum control, and a selected-phase inclusion test fails numerically in
the completed-Weil Galerkin shadow.  This does not disprove a special
infinite-dimensional zeta intertwiner or a tuned single-phase construction.

## 1. Exact finite criterion

Suzuki's deficiency vectors are normalized by

```text
T_s v_+ = exp(x),             T_s v_- = exp(-x),
T_s = A-sI,
```

and the characteristic function is

```text
W_s(theta,z)
  = (z-i) I_(s,+)(z) + exp(i theta) (z+i) I_(s,-)(z),

I_(s,+/-)(z) = integral_(-a)^a v_+/-(x) exp(i z x) dx.
```

This is equation (1.11) in
[Suzuki's finite-window construction](https://arxiv.org/abs/2606.09096v1).
For real `z`, define

```text
E_s(z) = -(z-i) I_(s,+)(z) / ((z+i) I_(s,-)(z)).
```

Reflection symmetry gives `|E_s(z)|=1`, and exactly

```text
W_s(theta,z)=0  iff  E_s(z)=exp(i theta).
```

Suppose `z_j` are zeros for shift `lambda` and phase `theta`.  A single target
phase `theta'`, independent of `z`, makes every listed `z_j` a zero at shift
`mu` if and only if all phasors `E_mu(z_j)` are equal.  Equality of the two
complete zero sets additionally requires that the target have no extra zeros.
The experiment measures the chord diameter and fits the best common phase;
unequal target phasors are therefore a decisive necessary obstruction.  A
zero-free entire multiplier cannot evade this obstruction because it cannot
remove a missing source zero from the target divisor.

There is also an infinitesimal version.  The resolvent identity gives

```text
d/ds T_s^-1 = T_s^-2,

d/ds arg E_s(z)
  = Im(I'_(s,+)(z)/I_(s,+)(z)
       - I'_(s,-)(z)/I_(s,-)(z)).
```

A differentiable constant phase remapping requires this phase velocity to be
the same at every reference zero.  Its range is therefore an earlier local
falsifier.

## 2. Controls

The positive control is `A=cI`.  Every change of shift merely multiplies both
deficiency vectors by the same scalar, so `E_s` is exactly shift-independent.
The implementation recovers this through dimension 12: the phase chord
diameter is below `2.6e-13`, the maximum normalized characteristic residual
is below `1.2e-13`, and the phase-velocity range is below `6.2e-16` in the
archived run (the dependency-free bisection replay is slightly more accurate).

The negative control is not an arbitrary matrix.  It is the continuum form

```text
t_alpha(u) = integral_(-a)^a (|u'|^2 + alpha |u|^2) dx,
u in H_0^1(-a,a),             alpha=1.
```

The Galerkin basis consists of the exact Dirichlet sine eigenfunctions.  This
is a coercive energy for which `i d/dx` is symmetric on the compactly
supported interior core.

There is also an exact continuum obstruction, independent of the Galerkin
calculation.  Write

```text
T_kappa = -d^2/dx^2 + kappa,       v_kappa=T_kappa^-1 exp(x)
```

with Dirichlet boundary conditions on `(-a,a)`, and put

```text
r_kappa = integral x v_kappa(x) dx / integral v_kappa(x) dx.
```

The Dirichlet Poincare inequality makes `T_0` already strictly positive, so
every member used below is coercive even though the mass parameter starts at
zero.

Reflection gives `I_-(z)=I_+(-z)` on the real axis.  Direct logarithmic
differentiation of the boundary phasor at `z=0` therefore gives

```text
d/dz arg E_kappa(z) |_(z=0) = 2 + 2 r_kappa.           (2.1)
```

At `kappa=0`, solving the two elementary Dirichlet problems for
`T_0^-1 1` and `T_0^-1 x` gives

```text
r_0 = a^2 sinh(a)/(3(a cosh(a)-sinh(a))) - 1.
```

Since `kappa T_kappa^-1` converges strongly to the identity as
`kappa -> infinity`,

```text
lim r_kappa = a coth(a)-1.
```

These values are already unequal at `a=1`:

```text
r_0 = (e^2-7)/6,                 lim r_kappa = 2/(e^2-1).
```

Indeed their difference is
`(5+8e^2-e^4)/(6(e^2-1))>0`; the elementary bounds `7<e^2<8`
make the numerator at least `5`.  Thus a shift-independent pointwise phase
quotient would have two different derivatives at the common point
`E_kappa(0)=1`.  Full phase-labelled covariance fails for some pair of
strictly coercive members of this exact continuum family.  This derivative
argument does not say that the zero sets at one specially selected phase
differ; it disproves the stronger pointwise quotient needed to relabel every
extension phase at once.  In particular, equivalence of the shifted energy
norms cannot prove that stronger covariance.

The finite calculation supplies a quantitative check at the particular pair
`kappa=1,2` (equivalently shifts `0,-1` from the base operator
`-d^2/dx^2+1`).  Dimensions `6` to `12` stabilize at

| modes | phase chord diameter | phase-velocity range | fitted RMS residual | nearest-root RMS |
|---:|---:|---:|---:|---:|
| 6 | `.4554` | `.5320` | `.0565` | `.0245` |
| 8 | `.4606` | `.5381` | `.0609` | `.0263` |
| 10 | `.4626` | `.5404` | `.0634` | `.0273` |
| 12 | `.4635` | `.5415` | `.0651` | `.0279` |

Thus norm equivalence between the shifted Hilbert spaces does not, even for a
legitimate differential-energy model, identify their full phase-labelled
extension families by a constant `U(1)` reparameterization.

## 3. Completed-Weil Galerkin shadow

The zeta diagnostic uses the repository's normalization-matched Legendre Weil
matrix at program support `L=1.75`, whose interval radius is `a=L/4=.4375`.
It solves the finite systems

```text
(Q_N-sI) v_(s,+/-) = projection_N(exp(+/-x))
```

and applies the same exact phasor criterion.  To avoid making the result rest
on the very small ground margin at shift zero, the headline comparison uses
the comfortably coercive shifts `lambda=-.05` and `mu=-.25`:

| modes | roots used | phase chord diameter | fitted RMS residual | maximum residual | nearest-root RMS |
|---:|---:|---:|---:|---:|---:|
| 6 | 11 | `1.9982` | `.5879` | `.9935` | `1.2910` |
| 8 | 11 | `2.0000` | `.6119` | `.9675` | `1.2143` |
| 10 | 11 | `2.0000` | `.6107` | `.9711` | `1.2108` |
| 12 | 11 | `1.9996` | `.6245` | `.9688` | `1.2130` |

The chord diameter is essentially its maximum possible value `2`; the listed
reference zeros demand nearly opposite target phases.  The corresponding
phase-velocity range stays near `96`, so the obstruction is already present
infinitesimally.  The comparison from shift `0` to `-.25` fails as well, but
its very large phase velocity is amplified by the near-null direction and is
not needed for the verdict.

This is not peculiar to the initially selected phase `.37`.  A coarse sweep
of 32 equally spaced reference phases at dimension 8 found its smallest RMS
residual at the symmetry phase `theta=pi`.  Repeating that phase under
refinement gives chord diameters `.7310, .9479, .9741, .9730` and RMS
residuals `.1419, .1554, .1523, .1524` at dimensions `6,8,10,12`.  Thus even
the best phase seen in the sweep does not make all listed reference roots
target roots.  The phase sweep is a diagnostic, not an interval proof
excluding every possible real phase.

Complete data are in
[`shift-phase-covariance.csv`](shift-phase-covariance.csv), generated by
[`shift_phase_covariance_falsifier.py`](../src/shift_phase_covariance_falsifier.py).
The headline rows are reproduced with

```bash
for n in 6 8 10 12; do
  PYTHONPATH=src python3 src/shift_phase_covariance_falsifier.py \
    --include-completed --dimension "$n" --z-min -40 --z-max 40 \
    --samples 12001 --root-limit 11
done
```

## 4. Scope and verdict

At the displayed floating precision, the calculation reports that no one
constant target phase makes the listed reference zeros common to the two
shifted Galerkin characteristic surrogates.  The margins are large and stable
under the printed refinements, but no interval enclosure is claimed.  If two
source zeros require different target phases, equality of the complete finite
zero sets is impossible, even after multiplication by a zero-free entire
factor; here that implication is numerical evidence, not a certified finite
theorem.

It does **not** establish that Suzuki's exact infinite-dimensional zero sets
depend on the auxiliary shift.  The Legendre truncation preserves reflection
and the defining resolvent equations, but it is not a certified graph-limit
approximation of the unbounded self-adjoint extensions.  A special arithmetic
intertwiner could still exist.

What is pruned exactly is the generic full-family argument

```text
H(T_(a,lambda)) is isomorphic to H(T_(a,mu))
  => their phase-labelled extension families agree after one constant phase change.
```

An actual proof of full shift independence must construct an intertwiner that
also conjugates the adjoint differential operators and induces a
`z`-independent unitary map on their boundary spaces.  Mere equivalence of the
positive norms does not provide those properties.  A canonical, specially
tuned `(shift,phase)` sequence is a distinct survivor.  No conclusion about
RH follows.
