# Suzuki--xi characteristic calibration: fail-fast result

Status: the canonical one-scalar derivative calibration exists in the tested
completed-Weil Galerkin models, but its impressive agreement at two easy
imaginary-axis probes is a near-Cayley effect.  Real and genuinely off-axis
held-out probes remain large and nonmonotone.  The calculation does not
identify the finite model with the xi characteristic and does not disprove a
later asymptotic limit.

## 1. Normalization and conditionality

Put

```text
Xi(z)=xi(1/2-i z),                    L(s)=xi'(s)/xi(s).
```

The functional equation makes `Xi` real entire and even.  For

```text
Theta_xi(z)=(xi(s)-xi'(s))/(xi(s)+xi'(s))
           =(1-L(s))/(1+L(s)),       s=1/2-i z,
ell=L(3/2),                          alpha=(1-ell)/(1+ell),
```

the Frostman normalization at `z=i` simplifies exactly to

```text
S_xi(z)=(Theta_xi(z)-alpha)/(1-alpha Theta_xi(z))
       =(ell-L(s))/(ell+L(s))
       =(ell xi(s)-xi'(s))/(ell xi(s)+xi'(s)).          (1.1)
```

Lean checks the Mobius algebra, the normalizations at `L=ell` and `L=0`, and
the reciprocal symmetry in
[`FrostmanCayleyNormalization.lean`](../lean/rhbridge/RHBridge/FrostmanCayleyNormalization.lean).

Algebraically, (1.1) is an unconditional meromorphic function.  Calling it a
Schur/Livsic characteristic or using its de Branges--Rovnyak kernel as a
positive Gram kernel is not unconditional.  Under RH it is inner.  Conversely,
an off-critical xi zero in the upper-half spectral plane gives the removable
value `S_xi=-1` at an interior point; a nonconstant Schur function cannot take
a unimodular value there.  Thus Schur-innerness, and positivity of the global
model kernel, already carry RH-strength content.

This normalized minimal-operator characteristic is also stronger data than
the spectrum of one selected self-adjoint extension.  Selected-extension
strong-resolvent convergence does not by itself imply convergence of (1.1).

## 2. The one-scalar calibration

Differentiating (1.1) at `z=i` gives

```text
S_xi'(i)=(i/2) rho_xi,
rho_xi=L'(3/2)/L(3/2)
      =0.9968019520324009035288967047877578...
```

For the finite shifted metric `R_sigma=(Q-sigma I)^-1`, reflection gives

```text
E_(a,sigma)'(i)=(i/2) rho_a(sigma),

rho_a(sigma)
  = <e^(-x),R_sigma e^x>/<e^x,R_sigma e^x>
  = (EvenEnergy_sigma-OddEnergy_sigma)
      /(EvenEnergy_sigma+OddEnergy_sigma).              (2.1)
```

The diagnostic chooses `sigma` by the single equation
`rho_a(sigma)=rho_xi`.  All computations use mpmath matrices, analytic
Legendre coefficients of `exp(x)`, parity-block resolvent solves, and a
logarithmic floor-gap bisection.  No SciPy optimizer or float64 conversion is
used in the calibrated solve.

The constants and sign were independently checked:

```text
ell       = .046135928060462575359466006542272...
L'(3/2)   = .0459883831494955148955660...
S_xi(i/4) = .599518696380572462336788...
S_xi(2i)  =-.331218941352590480137589...
```

## 3. Result

The derivative residual is between `4e-34` and `1.1e-33`, as expected from
the calibration.  The chosen shifts can be extremely close to the Galerkin
floor:

| support | dimension | floor | calibrated `sigma` | floor gap | condition estimate |
|---:|---:|---:|---:|---:|---:|
| 1.750 | 12 | `3.248e-5` | `-8.265e-5` | `1.151e-4` | `2.60e4` |
| 2.485 | 12 | `7.531e-8` | `-5.579e-8` | `1.311e-7` | `2.18e7` |
| 2.996 | 12 | `4.063e-8` | `3.743e-8` | `3.199e-9` | `8.02e8` |

Across all nine `(support,dimension)` pairs with dimensions `8,10,12`:

- the `i/4` errors are `2.1e-7` to `3.8e-6`;
- the `2i` errors are `3.1e-6` to `5.1e-5`;
- the `14+.5i` errors are `.051` to `.312`;
- the `14+2i` errors are `.031` to `.216`;
- the integer real-grid RMS errors are `.197` to `.564`, with maxima `.837`
  to `1.985`.

The strong errors are not monotone under either support or dimension
refinement.  The two weak values are poor discriminators: the target differs
from the universal factor `-(z-i)/(z+i)` by only `4.8e-4` at `i/4` and
`2.1e-3` at `2i`.

There is also a structural explanation for why calibration is easy.  When the
lowest Galerkin eigenvector is even, the even resolvent energy diverges as
`sigma` approaches the floor from below while the odd energy stays bounded.
Equation (2.1) therefore tends generically to `1`; matching a target as close
to `1` as `rho_xi` mostly selects a point near that resolvent pole.  Existence
of the scalar match is not xi identification.

The implementation and regression tests are
[`suzuki_livsic_calibration.py`](../src/suzuki_livsic_calibration.py) and
[`test_suzuki_livsic_calibration.py`](../src/test_suzuki_livsic_calibration.py).
Every output row labels target-kernel positivity
`RH-equivalent-not-tested` and the model `finite-Galerkin-diagnostic`.

## 4. Verdict and next target

This prunes the inference

```text
match S'(i), S(i/4), and S(2i)
  => identify the finite Suzuki model with the xi model.
```

It does not rule out compact-local convergence at much larger support, and it
does not test only the selected extension asserted in Suzuki's weaker
strong-resolvent proposal.

That divisor-level gate is now complete through the certified endpoint
`L=749/250`; see
[`SUZUKI-FIXED-SHIFT-DIVISOR-CHECKPOINT.md`](SUZUKI-FIXED-SHIFT-DIVISOR-CHECKPOINT.md).
At `sigma=-1/4`, ordered injective held-out root matching fails throughout the
tested ladder, as do `sigma=-1` and `theta=pi` controls, but the error improves
with support and hence is not an asymptotic no-go theorem.  Analytically, the
load-bearing theorem remains direct compact-local convergence, after a proved
zero-free normalization, of entire real-zero finite characteristics to `Xi`;
the meromorphic `xi/xi'` target is not an acceptable whole-plane limit without
a removability theorem.
