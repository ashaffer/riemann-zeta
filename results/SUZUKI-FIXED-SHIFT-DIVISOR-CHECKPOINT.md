# Suzuki fixed-shift selected-divisor checkpoint

Status: the auxiliary shift is now fixed at `sigma=-1/4` on a range where it
is genuinely admissible for the continuum completed-Weil operator.  A
one-phase, train/holdout divisor diagnostic fails throughout the presently
certified range.  Its root errors improve with support, however, so this is a
finite checkpoint rather than an asymptotic no-go theorem.

## 1. Why `-1/4` is safe here

In the repository convention the interval radius is `a=L/4`.  The existing
full-space certificates give

```text
L = 7/4       : Q_L(f) > 2.2699e-5 ||f||_2^2,
L = 497/200   : Q_L(f) > 9.99e-11  ||f||_2^2,
L = 749/250   : Q_L(f) > 9.9e-16   ||f||_2^2.
```

Zero extension and nested-support monotonicity propagate the last endpoint
to every smaller support.  Consequently, on `L<=749/250`,

```text
< (A_L-sigma I)f,f >
  = Q_L(f) + (1/4)||f||_2^2
  > (1/4 + 9.9e-16)||f||_2^2.                         (1.1)
```

Thus `sigma=-1/4` is not merely below the measured Galerkin floors: it is
continuum-admissible under the documented analytic plus FLINT-Arb trust base
of the full-space certificates.  The fixed `L=7/4` arithmetic core has the
strongest Lean-checked provenance; the two later full-space transfers remain
software/analytic certificates.

Lean proves the scalar identity behind (1.1), its lower-bound transfer, and
strict admissibility from a nonnegative floor in
[`NestedShiftRigidity.lean`](../lean/rhbridge/RHBridge/NestedShiftRigidity.lean).
These theorems use no project axiom.

This scope is essential.  Suzuki's operator is lower bounded separately at
each fixed support, but neither the literature audit nor this repository gives

```text
inf_(L>0) lambda_min(A_L) > -1/4.
```

Therefore `-1/4` has **not** been proved admissible on a cofinal all-support
family.  The test below stays inside the certified range.

## 2. Divisor test

For the finite Legendre compression of the operator in
[Suzuki's construction](https://arxiv.org/abs/2606.09096v1), put

```text
T_(L,sigma) = A_L - sigma I,
T_(L,sigma) v_+ = exp(+x),
T_(L,sigma) v_- = exp(-x).
```

For real `z`, the boundary phasor

```text
E_(L,sigma)(z)
  = -(z-i) integral(v_+(x) exp(i z x) dx)
       / ((z+i) integral(v_-(x) exp(i z x) dx))
```

has unit modulus, and `z` is a zero of the extension with phase `theta`
exactly when `E(z)=exp(i theta)`.

The first twelve target ordinates are immutable decimal centers from the
[Platt/LMFDB rigorously complete dataset](https://www.lmfdb.org/knowledge/show/rcs.source.zeros.zeta),
whose rigorous isolation method is documented in
[Platt's computation](https://doi.org/10.1090/mcom/3198).
LMFDB reports source precision `2^-102` (display precision `2.5e-31`).  The
diagnostic converts the centers to float64; its output is not interval
arithmetic.

The fitting protocol is deliberately hostile to overfitting:

1. odd-numbered targets train one phase; even-numbered targets are held out;
2. a deterministic 129-phase grid plus two local refinements minimizes actual
   training-root distance, not phasor distance;
3. roots are recomputed by bisection at the fitted phase;
4. dynamic programming matches all twelve targets to distinct roots in
   increasing order, so train and holdout cannot reuse a root;
5. no affine spectral reparameterization is allowed;
6. `sigma=-1` is run as a conditioning control;
7. both `theta=0` and `theta=pi` are run separately because exact inclusion
   of both `+gamma` and `-gamma` forces one of these symmetry phases.
   `theta=0` has a central zero, which is extraneous for a direct `Xi` target
   but not automatically for Suzuki's proposed `z^2 xi/xi'` target.

A scalar self-spectrum control recovers its planted phase and all held-out
roots at machine precision.

## 3. Result

The primary `sigma=-1/4` results over dimensions `8,10,12` are:

| support `L` | fitted train-only RMS | global injective RMS | held-out global RMS | fitted roots below `gamma_1` | fitted roots in `[gamma_1,gamma_12]` |
|---:|---:|---:|---:|---:|---:|
| `1.750` | `.888-.946` | `13.21-13.49` | `14.34-14.67` | `2` | `6` |
| `2.485` | `.920-1.085` | `4.87-5.06` | `5.25-5.33` | `3` | `8` |
| `2.996` | `.393-.879` | `1.90-2.65` | `2.24-3.06` | `3` | `10` |

The fitted phase therefore has respectively `8`, `11`, and `13` roots in
`[0,gamma_12]`, where the target has twelve.  When too few in-span roots are
available, the injective matcher must use roots above `gamma_12`; unlike the
discarded nearest-neighbor statistic, it cannot hide the density/index error
by reusing one root.

The robustness checks do not rescue the fit:

- at `sigma=-1`, global RMS ranges are `13.50-13.71`, `5.00-5.03`, and
  `2.23-2.43` at the three supports;
- at the symmetry phase `theta=0`, the primary ranges are `12.53-12.65`,
  `4.77-5.29`, and `2.52-2.72`, and the predicted central zero is present;
- at the exact-symmetry phase `theta=pi`, the corresponding primary ranges
  are `13.45-13.69`, `4.72-4.93`, and `2.04-2.47`.

The implementation is
[`suzuki_selected_divisor_alignment.py`](../src/suzuki_selected_divisor_alignment.py),
with regression tests in
[`test_suzuki_selected_divisor_alignment.py`](../src/test_suzuki_selected_divisor_alignment.py).
The doubled shift ladder used about 52 MB and 31 seconds on the audit machine.

## 4. Exact interpretation

If zero-free entire functions `h_n` satisfy

```text
h_n W_n -> Xi
```

compact-locally, Hurwitz/Rouche theory forces a distinct zero of `W_n` to
approach every simple zero of `Xi`, with matching zero counts on isolating
compact boundaries.  A zero-free normalization cannot repair a wrong
divisor.  Hence injective selected-divisor convergence is a necessary gate.
It is not sufficient for convergence of the functions.

Phasor coincidence at the exact ordinates is necessary and sufficient for
exact finite inclusion, but it is not necessary for asymptotic root
convergence when boundary-phase slopes can diverge.  This is why the headline
statistic uses actual roots and retains phasor residuals only as diagnostics.

The present rows fail the finite gate strongly, but their global error falls
as `L` increases.  They therefore do **not** disprove selected-extension
convergence as `L` tends to infinity.  They also do not certify convergence of
the Galerkin characteristics to the exact unbounded-operator characteristics.

The follow-up audit is now in
[`SUZUKI-SPECTRAL-COUNTING-CHECKPOINT.md`](SUZUKI-SPECTRAL-COUNTING-CHECKPOINT.md).
It proves the exact boundary-phase floor count but also shows why an ordinary
fixed-support Weyl law is insufficient: its onset and remainder can escape
with the support.  The remaining theorem must estimate the exact phase mass
on a fixed spectral compact uniformly as `L` grows.  In parallel, continuing
the fixed-shift route beyond `L=749/250` requires either a new continuum lower
bound below `-1/4` or an explicitly controlled support-dependent shift.
