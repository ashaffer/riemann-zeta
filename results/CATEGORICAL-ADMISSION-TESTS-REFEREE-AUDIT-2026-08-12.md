# Referee audit: executed categorical admission tests

Status: **PASS AFTER PATCHES**, 2026-08-12.

Audited artifacts:

- `ZETA23-FINITE-OPERATOR-SYSTEM-ADMISSION-GATE-2026-08-12.md`,
  `src/categorical_operator_system_gate.py`, and its tests;
- `ZETA23-CARRIER-SLICE-SUPPORT-FINITE-FIXTURE-2026-08-12.md`,
  `src/carrier_slice_support.py`, and its tests; and
- `ZETA23-APPROXIMATE-POLARIZATION-SEMILOCAL-FAIL-FAST-2026-08-12.md`,
  `src/approximate_polarization_gate.py`, and its tests.

The verdict certifies the finite algebra and the honesty of the stated
numerical scope after the corrections below.  It does not certify a uniform
zero-free strip, RH, a high-height Gabor remainder, or a zeta spectral
realization of the semilocal generator.

## 1. Operator-system admission gate

### Exact claims checked

- The two-hat Gram matrix at `L=7/4` is
  `(7/144)(4I+J)`, and the first unsigned prime translation has the displayed
  positive coefficient.  Since the two matrices commute, whitening gives
  `(48 p_2/35)(4J-I)`.
- The whitened left/right support-ray contrast is exactly
  `(sqrt(15)/4)Z`.  The unit test now derives this from the exact Gram square
  root instead of merely checking a hard-coded constant.
- Coordinate probes kill `J`; parity probes diagonalize `span{I,J}` and have
  the UCP recovery `Psi(x,y)=xP_++yP_-`.
- The four-probe witness has exact eigenvalues `{-1/8,1}` and all four exact
  expectations are positive.
- No fixed finite scalar vector-state family can reflect order on all of
  `Sym_2(R)`: its local cone is polyhedral, whereas `Pos_2(R)` has a continuum
  of extreme rays.
- The full matrix pair probe is unitary conjugation.  Its unnormalized Choi
  matrix is `vec(U)vec(U)^*`, with spectrum `{0,0,0,2}`.
- Block dephasing has covariance `diag(BB*,B*B)`.  After diagonal
  normalization its norm is `||A^(-1/2)BD^(-1/2)||^2`, so the strict
  covariance threshold is exactly the usual Schur threshold.

### Corrections and limits

- The angular largest-gap witness was qualified to **real rank-one** probes.
  The nonpolyhedral proof still covers arbitrary fixed finite complex vector
  states.
- The stop recommendation now applies only to exact order reflection on the
  full asymmetric system.  It does not exclude a smaller independently
  specified arithmetic subspace or a theorem signing one actual element.
- The numerical `p=2` matrix is now explicitly labeled the unsigned form
  `P_2`; the completed Weil form uses `-P_2`.
- The unit suite is labeled mixed: the structural checks use SymPy exact
  arithmetic, while the place assembly and covariance regressions use
  floating arithmetic.

The gamma/pole/prime assembly and prime-5 coupling table reproduced.  They
remain ordinary floating diagnostics and supply no uniform coupling margin.

## 2. Carrier-slice admission gate

### Exact claims checked

For

```text
h_eta(R)=max Tr(R Gamma),
Gamma>=0, Tr(Gamma)=1, Tr(N Gamma)>=eta,
```

the scalar dual is

```text
h_eta(R)=inf_(mu>=0)
  [lambda_max(R+mu N)-mu eta]
```

when `eta<lambda_max(N)`.  The sign of `mu N` and of `-mu eta` is correct.

- Strong duality follows from a genuine primal Slater point: mix a top
  eigenstate of `N` with a sufficiently small full-rank normalized state.
  The original rank-one top state was strictly feasible for the scalar
  inequality but was not interior to the PSD cone; that proof sentence was
  corrected.
- At `eta=lambda_max(N)`, the objective is the largest eigenvalue of the
  compression of `R` **restricted to the top eigenspace**.  The original
  ambient `P_E R P_E` notation could add spurious zero eigenvalues when the
  true answer is negative; it was corrected.
- An optimizer can be chosen rank one.  At an extreme point, a rank-`r`
  complex Hermitian support has `r^2` real perturbation dimensions and at
  most two active affine equations; compactness supplies an extreme
  optimizer.
- The one-pair mirror support is exactly `m`, hence its useful fraction is
  `sech(alpha D)`.
- The collateral closed form, its breakpoint
  `(1-1/sqrt(3))/2`, the `2/11` cancellation state, and the negative support
  at carrier fraction `3/4` all check algebraically.

### Numerical limits

The solver is a double-precision evaluator of the exact dual.  It uses
floating feasibility/boundary tolerances and golden-section minimization; it
is not an interval or exact-arithmetic certificate.  The report and code now
say so.  The prime-5 forms use 24-decimal mpmath assembly but are converted to
`float64` for eigensolves.  Both full and relative reported fixtures
reproduced.

No stored matrix is the actual high-height prime/collateral remainder
`R_T`.  Passing this finite necessary gate is not sufficient for completed
positivity because the complement coupling and full-form cost remain.

## 3. Approximate-polarization admission gate

### Exact claims checked

- For every eigenvalue `lambda`,

  ```text
  epsilon_G(A)>=abs(2 Re(lambda)-1).
  ```

  This follows from the relative Rayleigh quotient and does not require
  normality.
- If `A=S Lambda S^(-1)`, the fitted metric
  `(S^(-1))^*S^(-1)` attains the maximum horizontal spectral defect.  The
  conditioning identity is `cond_2(G_fit)=cond_2(S)^2`.
- The real off-line block has sharp defect `2|alpha|`.
- A generator retaining invariant eigenvalues zero and one has defect at
  least one for every positive metric, including metrics with cross-sector
  entries.
- For a positive moment Gram matrix `G` and symmetric shifted moment matrix
  `H`, `M=G^(-1)H` satisfies `M^T G=GM=H`; hence
  `A=(1/2)I+iM` has exactly zero algebraic defect.  A new nonquadrature unit
  test verifies this moment algebra.
- The Euler multiplier isometry is correctly normalized:
  `d mu_p=|phi_p|^(-2)d mu_infinity` and multiplication by `phi_p` is unitary
  in the stated direction.  It commutes with the scaling multiplier.
- The local weight crosses one exactly, so the metric update is not globally
  Loewner monotone under the identity realization.

### Corrections and limits

- The pole/Tate no-go was narrowed to models which actually retain the
  invariant eigenvalues `0` and `1`.  It does not exclude a different
  all-place generator that reproduces pole terms without those eigenvalues.
- `alpha` is explicitly real in the off-line control.
- NumPy tests and SciPy quadratures are labeled floating regressions of exact
  formulas, not exact-arithmetic or interval certificates.  The script's
  control heading was changed accordingly.

The native semilocal generator is polarized because it is rebuilt from the
same moment metric.  Its Ritz nodes lie on the critical line by construction;
no determinant, resolvent, or conservative limit identifies them with zeta
zeros.  The cross-stage defects reproduce numerically but prove only failure
of the fixed coefficient identity comparison at those finite sections.

## 4. Executed verification

The final suites pass:

```text
operator-system tests       9/9
carrier-slice tests         5/5
polarization tests          6/6
total                      20/20
```

The operator symbolic summary, numerical place assembly, mirror and
collateral demonstrations, both prime-5 diagnostics, and representative
semilocal diagnostics were also rerun successfully.  Their outputs match the
three reports to displayed precision.

## Final verdict

**PASS AFTER PATCHES.**  The finite mathematics is sound under the corrected
hypotheses and normalizations.  The admissions tests materially prune three
specific mechanisms: finite scalar order descent on the full asymmetric
system, subcarrier diagonal mirror support, and invariant-`(0,1)` ungraded
polarization.  The surviving operator-system, carrier-remainder, and
middle-sector polarization programs still require new zeta-specific objects
or estimates; none of these executions proves a strip.
