# First actual-coefficient high-height carrier-slice fixture

Status: reproducible finite double-precision diagnostic, 2026-08-12.  The
prime, gamma, pole, and rational terms are all assembled from the completed
explicit formula; no zeta-zero table is used.  The selected reflected pair is
a hypothetical scan parameter, not an asserted zero.  This is not an interval
certificate, an asymptotic theorem, a uniform zero-free strip, or a proof of
RH.

## 1. Verdict

The zero-independent arithmetic side of the full-form carrier slice can now
be computed directly at modest high heights.  The implementation is
[`high_height_carrier_slice.py`](../src/high_height_carrier_slice.py), with
focused tests in
[`test_high_height_carrier_slice.py`](../src/test_high_height_carrier_slice.py).

For the deterministic scan

```text
T=32,64,128,256,512,   L=log T,   X=T,
gamma=3T/2,            alpha=2/5,
```

the direct constrained arithmetic support

```text
q_eta(K_ar)=max Tr(K_ar Gamma)
             Gamma>=0, Tr Gamma=1, Tr(N Gamma)>=eta
```

is positive at every tested carrier fraction `eta=theta*kappa`,
`theta=0.5,0.9,1`.  Thus the negative finite fail-fast test does not fire on
these five scan points.  The ratios are neither a bound nor a limit law.  In
particular, the full-carrier ratio falls below one at `T=512` but the
unscaled value remains positive, `q_kappa=1.00043884505`.

The target-subtracted support is also computed, solely as a bookkeeping
control.  It satisfies the exact aligned-baseline theorem

```text
q_eta+eta <= h_eta(K_ar+N) <= q_eta+kappa,
h_kappa(K_ar+N)=q_kappa+kappa.
```

It therefore supplies no new route beyond `q_eta`; the direct arithmetic
functional is the primary output.

## 2. Exact finite construction and normalization

On `[-L/2,L/2]`, use the sign-conjugated critical sharp grid

```text
tau_k=gamma+2*pi*k/L,
e_k(t)=(-1)^k exp(-i*tau_k*t) 1_[-L/2,L/2](t).
```

The finite aperture is `|k|<=floor(0.2*T/(2*pi/L))`, so every displayed grid
lies in `[T,2T]`.  If `f_c=sum_k c_k e_k`, then

```text
||f_c||_2^2=L ||c||_2^2.
```

The endpoint-jet space is

```text
W_m={c: sum_k k^r c_k=0 for 0<=r<m},
m=max(3,ceil(log T)).
```

The code uses a Legendre basis for the same polynomial row space to avoid an
ill-conditioned monomial Vandermonde.  These jets make the zero extension
admissibly endpoint-flat.  The choice `m=ceil(log T)` is illustrative: it is
not the project's mesoscopic or maximal budget `m` of order `T`, and the
computed space is not an all-constraints quotient.

For the hypothetical pair parameter put

```text
z=gamma-i*alpha,
v_k=2 sin(L(z-gamma)/2)/(z-tau_k)=x_k+i*y_k.
```

Let `U` be an orthonormal coefficient-space inclusion of

```text
S_T=W_m intersect ker(x^*).
```

Only this one selected positive row is nulled.  No unknown collateral-positive
row is used.  In the repository's common raw-row normalization,

```text
N_T=(2/L^2)(U^*y)(U^*y)^*,
kappa=lambda_max(N_T),
K_0=(2/L^2)(x x^*-y y^*),
U^*K_0 U=-N_T.                                      (2.1)
```

The carrier threshold used by the program is the absolute quantity
`eta=theta*kappa` after this compression; it is not an unnormalized overlap.

### Actual arithmetic data

For every prime power `n<=X`, the script uses the actual coefficient

```text
w_n=Lambda(n)/sqrt(n).
```

For `0<=u<=L` define the sign-conjugated shifted-overlap matrix

```text
S_ii(u)=(L-u) cos(tau_i*u),
S_ij(u)=[sin(tau_j*u)-sin(tau_i*u)]/(tau_i-tau_j), i!=j.
```

Then the positive prime matrix is exactly

```text
H_prime=2 sum_(n<=X) w_n S(log n).                  (2.2)
```

The completed form subtracts (2.2).  Both orientations of the complex pole
polarization are retained.  With

```text
p_(+/-),k=(-1)^k
  2 sinh(((+/-)1/2-i*tau_k)L/2)/((+/-)1/2-i*tau_k),
```

the Hermitian pole matrix is

```text
H_pole=conj(p_-)*p_+^T+conj(p_+)*p_-^T.             (2.3)
```

The archimedean matrix is the exact sharp compression

```text
(H_arch)_ij = integral_R
  [Re psi(1/4+i*t/2)-log pi]
  eHat_i(t) conj(eHat_j(t)) dt/(2*pi).              (2.4)
```

The implementation evaluates (2.4) by the equivalent digamma/trigamma
divided-difference formula and an exponentially convergent tail.  Its
off-diagonal form is

```text
-2 integral_0^L S_ij(u) e^(-u/2)/(1-e^(-2u)) du,
```

with the exact diagonal limit treated separately.

The normalized, target-conditioned arithmetic operator is

```text
K_ar=U^*(H_arch+H_pole-H_prime)U/L^2.               (2.5)
```

Thus the factors `2/L^2` in (2.1) and `1/L^2` in (2.5) use the same
coefficient normalization.

### Independent completion check

The program separately constructs the centered actual von Mangoldt matrix.
For `s=1/2+i*t`, put

```text
Z(t)=sum_(n<=X) Lambda(n)/sqrt(n) exp(i*t*log n),
C(t)=(exp(sL)-1)/s,
A(t)=Im(Z(t)-C(t)),
D(t)=Re sum_(n<=X) Lambda(n)/sqrt(n)(L-log n)exp(i*t*log n)
     -Re[(exp(sL)-1-sL)/s^2].
```

Its Loewner matrix is

```text
(H_E)_ij=2[A(tau_i)-A(tau_j)]/(tau_i-tau_j), i!=j,
(H_E)_ii=-2D(tau_i).
```

Independently, `H_0` is assembled from the positive rational density
`1/(2*pi*(1/4+t^2))`, whose physical kernel is `exp(-|u|/2)`.  The code then
checks the exact algebraic completion identity numerically:

```text
H_arch+H_pole-H_prime = H_E+H_arch+H_0.             (2.6)
```

This avoids defining the rational term as a residual.  The largest raw
spectral-norm residual in (2.6) over the five runs is
`3.65e-14`.

## 3. Direct constrained arithmetic results

The exact scalar dual used for `theta<1` is

```text
q_eta(K_ar)=inf_(mu>=0)
  [lambda_max(K_ar+mu*N_T)-mu*eta].                 (3.1)
```

At `theta=1`, feasibility forces the top carrier state and the program
evaluates its Rayleigh quotient directly.  No external SDP package is used.

| `T` | grid `d` | `m` | `dim S_T` | prime powers | `kappa` | carrier retained | `q_.5k/k` | `q_.9k/k` | `q_k/k` |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 32 | 7 | 4 | 2 | 18 | 0.0529556815 | 0.150218 | 10.109223 | 8.924253 | 7.113426 |
| 64 | 17 | 5 | 11 | 27 | 0.287376492 | 0.542806 | 4.105359 | 3.286236 | 2.338261 |
| 128 | 39 | 5 | 33 | 44 | 0.584987125 | 0.772559 | 2.237767 | 1.612378 | 1.078334 |
| 256 | 91 | 6 | 84 | 70 | 0.890464010 | 0.850494 | 1.714954 | 1.406702 | 1.216447 |
| 512 | 203 | 7 | 195 | 117 | 1.311848714 | 0.928308 | 1.222956 | 0.980457 | 0.762618 |

Here `carrier retained` means `kappa` divided by the exact infinite sharp-
lattice carrier `sinh(alpha*L)/(alpha*L)-1`; it does not compare against an
unknown zero-side quotient.

The unscaled direct values are:

| `T` | `q_.5k` | `q_.9k` | `q_k` | `h_k(K_ar+N)=q_k+kappa` |
|---:|---:|---:|---:|---:|
| 32 | 0.535340778 | 0.472589880 | 0.376696324 | 0.429652006 |
| 64 | 1.179783726 | 0.944387105 | 0.671961379 | 0.959337871 |
| 128 | 1.309064859 | 0.943220305 | 0.630811278 | 1.215798403 |
| 256 | 1.527104887 | 1.252617627 | 1.083202633 | 1.973666644 |
| 512 | 1.604333602 | 1.286210907 | 1.000438845 | 2.312287559 |

The direct arithmetic slice had floating extremal eigenvalues

```text
T=32:  [ 2.14488e-1, 5.35341e-1]
T=64:  [ 3.62437e-4, 1.19678]
T=128: [ 1.16982e-12,1.58266]
T=256: [-3.42267e-14,1.80082]
T=512: [-8.83714e-14,1.91086].
```

The last two lower edges are at roundoff scale and are not positivity
certificates.

## 4. Mechanical residuals

All residuals below are double-precision spectral norms or absolute scalar
errors.  `pair` checks (2.1), `completion` checks (2.6), `q-full` checks that
`q_kappa` is the carrier Rayleigh quotient, and `baseline` checks
`h_kappa=q_kappa+kappa`.

| `T` | endpoint jets | selected `x` | pair `=-N` | completion | `q-full` | baseline |
|---:|---:|---:|---:|---:|---:|---:|
| 32 | 3.24e-16 | 4.21e-16 | 2.22e-17 | 3.67e-15 | 1.67e-16 | 1.39e-17 |
| 64 | 7.77e-16 | 3.86e-16 | 9.13e-17 | 5.36e-15 | 4.44e-16 | 5.55e-17 |
| 128 | 1.60e-15 | 1.97e-15 | 2.74e-16 | 3.32e-14 | 3.33e-16 | 5.55e-16 |
| 256 | 3.08e-15 | 3.08e-15 | 5.07e-16 | 3.65e-14 | 4.44e-16 | 2.22e-16 |
| 512 | 6.41e-15 | 2.12e-15 | 7.87e-16 | 3.04e-14 | 4.44e-16 | 2.44e-15 |

The baseline sandwich is also checked at all three carrier fractions; its
worst signed slack is `-2.45e-15`.

## 5. What a sign does and does not decide

If the parameter `(alpha,gamma)` is assumed to be an actual off-line zero,
the explicit formula gives the conditional zero-side interpretation

```text
K_ar|S_T=-N_T+R_collateral.                         (5.1)
```

For that conditional target, `q_eta<0` would decisively show that **every**
state in this target-only carrier slice has negative completed form.  Because
any quotient obtained by nulling additional positive rows is smaller, the
same negative upper bound would survive there whenever its slice at the same
absolute `eta` is nonempty.  If that smaller slice is empty, the additional
rows have already deleted the requested carrier fraction.  Either alternative
rules out a nonnegative carrier-screening state at that fraction.

That is a decision about the proposed finite screening mechanism, not a zero
exclusion by itself.  At full carrier, `q_kappa<0` is simply one negative
target-adaptive Weil value; turning it into a contradiction still requires an
independent arithmetic lower bound for the same value.  Conversely,
`q_eta>=0` merely exhibits a nonnegative state in the relaxed target-only
space.  Unknown collateral-positive rows may delete it, and it does not prove
aggregate cancellation or the existence of a zero.

All five computed `q_eta` are positive.  Hence this run admits, but does not
construct, the finite reservoir contemplated by the gate at floating-point
level.  It neither confirms nor excludes the hypothetical pair.

A target exclusion would require two uniform statements on the same feasible
set: an arithmetic admission theorem `q_eta>=0`, and, conditional on the
candidate being an actual zero, a divisor-isolation theorem forcing
`q_eta<0`.  Neither sign alone excludes the candidate.  The table is only
finite numerical evidence for the first sign and proves neither uniform
statement.

## 6. Reproduction and scope boundary

Run:

```bash
PYTHONPATH=src python3 -m unittest src/test_high_height_carrier_slice.py
PYTHONPATH=src python3 src/high_height_carrier_slice.py
```

The focused suite reports `5/5` tests passing.  On the current machine the
default five-height run took about `2.5 s` and peaked near `65 MB` resident
memory.  The script emits the complete JSON records, including all direct and
baseline values and residuals.

The sequence `T=2^j` defines a reproducible cofinal family, but only the five
displayed terms were evaluated.  There is no interval arithmetic, error
enclosure for the digamma/trigamma evaluation, conditioning theorem uniform
in `T`, or proof that the displayed trend continues.  The model is one sharp
full-form block; it is not the exact two-lobe cross observable, whose
reduction needs the common kernel of four lobe-restricted selected rows.  No
claim about that cross construction is inferred here.

This computation implements the direct target recommended after
[`ZETA23-HIGH-HEIGHT-CARRIER-SLICE-ANALYTIC-REDUCTION-2026-08-12.md`](ZETA23-HIGH-HEIGHT-CARRIER-SLICE-ANALYTIC-REDUCTION-2026-08-12.md)
and the baseline pruning theorem
[`ZETA23-CARRIER-SLICE-ALIGNED-BASELINE-NOGO-2026-08-12.md`](ZETA23-CARRIER-SLICE-ALIGNED-BASELINE-NOGO-2026-08-12.md).
It replaces the formerly missing high-height arithmetic matrix fixture.  It
does not replace the still-missing uniform signed prime-polynomial estimate,
and it proves no zero-free strip.
