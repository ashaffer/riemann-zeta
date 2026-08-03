# Modular-orbit Gram audit

Status: diagonal and first reflection-orbit positivity are falsified; only a
fully global Poisson block remains, 2026-08-01.

For theta summand transforms `H_n`, the bilinear contribution to the Laguerre
density is

`B_(n,m)=H_n'H_m'-(H_n H_m''+H_m H_n'')/2`.

The full density is `sum_(n,m) B_(n,m)`.  The diagonal `B_(1,1)` is already
known to become negative.  The smallest modular symmetry groups `(n,m)` with
`(m,n)`; because `B_(n,m)=B_(m,n)`, its orbit contribution is `2B_(n,m)`.

The script `src/xi_theta_cross_falsifier.py` shows that this first orbit level
is also indefinite.  At `t=0`, `0<=x<=120`:

- `B_(1,2)` ranges from about `-2.73e-9` to `+8.22e-9`;
- `B_(1,3)` ranges from about `-1.22e-15` to `+2.70e-15`.

Thus neither diagonal terms nor swap-complete pair orbits admit a positive
Gram interpretation.

## Two-dimensional lattice form

After centering the convolution variables, a product of the `n` and `m` theta
terms contains

`exp(-pi e^(4r)(n^2 e^(2w)+m^2 e^(-2w)))`.

The `r` integral can be evaluated by `y=e^(4r)` as derivatives of

`Gamma(alpha)[pi(n^2e^(2w)+m^2e^(-2w))]^(-alpha)`.

This gives an explicit rectangular-lattice expansion, but its four
differential pieces have signs `+,-,-,+`.  Swap symmetry does not repair those
signs.  Any positive block must therefore use the full two-dimensional Poisson
duality, mixing infinitely many lattice pairs and the derivative pieces at
once.

## Strength audit

Such a fully global block is no longer a local decomposition.  Its Fourier
transform is the complete Laguerre density itself.  Unless Poisson summation
produces a new square root or independently positive spectral measure, naming
the entire lattice sum a single orbit merely restates the target.

## Verdict

Path D fails its first two natural Gram gates.  Retain only one sharply stated
possibility: an explicit two-dimensional Poisson identity whose right side is
a sum of squares with factors defined without xi zeros.  No partial orbit,
finite lattice truncation, or sign-by-sign estimate can work.  In the absence
of that identity, Path D is downgraded rather than actively funded.
