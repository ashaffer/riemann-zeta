# Birman--Schwinger numerical checkpoint

## Question

Does preconditioning the localized zeta Weil operator by its log-elliptic
archimedean part reveal a sign, monotonicity, or prime-event interlacing law
that is stronger than the original positive Galerkin margin?

Write

`Q = P + R`,  `P = A_arch + mu G`,  `K = -P^{-1} R`.

The shift `mu` is chosen above the negative generalized spectral floor of
`A_arch`, so `P` is positive definite.  A zero mode of `Q` is then exactly an
eigenvector of `K` with eigenvalue one.  The reproducible scan is
`src/birman_schwinger_scan.py`.

## Results

At hat dimension 31 and support `L=1.75`, changing the positive shift gives:

| added shift | original `lambda_min(Q,G)` | `1-kappa_max` | ground alignment |
|---:|---:|---:|---:|
| 0.25 | `3.972e-5` | `6.806e-5` | `0.999999948` |
| 1 | `3.972e-5` | `2.979e-5` | `0.999999990` |
| 4 | `3.972e-5` | `9.166e-6` | `0.999999999` |

The transformed gap changes by a factor greater than seven under an arbitrary
shift, while its extremizer remains essentially the original ground state.

At fixed added shift `0.25`, refinement gives:

| support | dimension | `lambda_min(Q,G)` | `1-kappa_max` | alignment |
|---:|---:|---:|---:|---:|
| 1.75 | 21 | `4.596e-5` | `7.980e-5` | `0.999999937` |
| 1.75 | 31 | `3.972e-5` | `6.806e-5` | `0.999999948` |
| 1.75 | 41 | `3.775e-5` | `6.429e-5` | `0.999999950` |
| 2.1972 | 21 | `1.375e-5` | `1.847e-5` | `0.999968343` |
| 2.1972 | 31 | `3.737e-6` | `4.830e-6` | `0.999997457` |
| 2.1972 | 41 | `1.448e-6` | `1.850e-6` | `0.999999604` |
| 2.996 | 21 | `9.035e-6` | `1.418e-5` | `0.999509599` |
| 2.996 | 31 | `2.538e-6` | `3.888e-6` | `0.999326750` |
| 2.996 | 41 | `7.630e-7` | `1.112e-6` | `0.999757271` |

Across small neighborhoods of the first three tested prime-power activation
thresholds, the transformed gap changed smoothly and decreased across the
event.  No alternating jump, sign barrier, or interlacing pattern appeared.

## Verdict

This preconditioner is numerically a near-diagonal rescaling of the known
ground-state problem.  It does not expose an independent invariant.  For any
positive `P`, the inequality `kappa_max < 1` is already algebraically
equivalent to positive definiteness of `Q` in the same Galerkin space, and the
near-unit alignments show that the extremal vectors also carry almost no new
structure.

This is a negative checkpoint for the proposed generic log-elliptic
preconditioner, not evidence against RH.  It should not be promoted into a
proof route unless a different, arithmetically canonical factorization yields
an exact sign or interlacing identity independent of the original margin.

The surviving target returns to the explicit constant-convolution equation.
The next useful decomposition must exploit arithmetic cancellation between
the archimedean continuum and prime translations, rather than merely invert
the archimedean principal part.
