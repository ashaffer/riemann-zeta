# Suzuki compact phase-mass fail-fast checkpoint

## Verdict

The proposed generic route to support-uniform compact spectral crowding has
failed.  Exponential type, reflection symmetry, the canonical zero at `i`,
and even a full fixed-window Weyl law do **not** force the boundary phase on a
fixed real compact to grow with the window.

The calculation nevertheless isolates an exact surviving target.  For the
repaired Suzuki construction, compact phase density is the reciprocal of the
squared projective coherence between two defect lines.  Linear growth in the
support is therefore neither an entire-function consequence nor a generic
uncertainty principle: it is a zeta-specific defect-line decorrelation
theorem.

This checkpoint does not prove or disprove RH.  It weakens the expected value
of an unweighted root-count obstruction to Suzuki's proposed
strong-resolvent limit, because growing root density can be compensated by
shrinking raw Clark atoms and, more decisively, by vanishing fixed-vector
spectral weights.

The trust map is:

- **F:** the scalar coherence, density, lower-bound, and Clark-weight
  consequences are checked by Lean in
  `RHBridge/BoundaryPhaseCoherence.lean`;
- **A:** the defect-kernel identity and the explicit meromorphic-inner
  countermodel below are conventional analytic arguments;
- **D:** all completed-Weil and finite-compression numbers are bounded-memory
  diagnostics, not continuum spectral theorems.

## 1. Exact normalization

Let

```text
T_(a,sigma) = A_a - sigma I > 0,
e_z(t) = exp(-i z t),
K_a(z,w) = <T_(a,sigma)^(-1) e_w, e_z>_L2,
s_a = K_a(-i,-i),
A_a(z) = (z+i) K_a(z,-i),
E_a(z) = -A_a#(z)/A_a(z).
```

Reflection gives `s_a=K_a(i,i)`.  On the real axis choose the increasing lift

```text
E_a(x) = exp(i Phi_a(x)).
```

With the displayed kernel orientation, Green's identity gives the raw Gram
formula

```text
K_a(z,w)
  = [A_a(z) conjugate(A_a(w))
       - A_a#(z) conjugate(A_a#(w))]
      / [2 i s_a (conjugate(w)-z)].                 (1.1)
```

There is no `2*pi` in (1.1).  Rescaling `A_a` by `sqrt(pi/s_a)` converts it to
the standard de Branges kernel normalization.  Taking the diagonal in (1.1)
gives

```text
-Im(A_a'(x) conjugate(A_a(x))) = s_a K_a(x,x).      (1.2)
```

Define the squared normalized defect-line coherence

```text
rho_a(x)^2
  = |K_a(x,-i)|^2 / [s_a K_a(x,x)].                 (1.3)
```

Then

```text
Phi_a'(x)
  = 2 s_a K_a(x,x) / |A_a(x)|^2
  = 2 / [(1+x^2) rho_a(x)^2],                       (1.4)

Delta Phi_a([u,v])
  = 2 integral_u^v dx / [(1+x^2) rho_a(x)^2].       (1.5)
```

Cauchy--Schwarz says only `0<rho_a(x)^2<=1`, so its entire generic content is

```text
Phi_a'(x) >= 2/(1+x^2).                             (1.6)
```

That lower bound has bounded mass on a fixed compact.  It cannot produce a
factor of `a` or `L=4a`.

For a Clark crossing `E_a(lambda)=exp(i theta)`, the repository's standard
upper-half-plane normalization is

```text
mu_(a,theta)({lambda})
  = 2*pi/Phi_a'(lambda)
  = pi (1+lambda^2) rho_a(lambda)^2.                (1.7)
```

Here `mu_(a,theta)` is the raw Clark measure.  For the canonical normalized
reference defect vector,

```text
nu_(a,theta)({lambda})
  = mu_(a,theta)({lambda})/[pi(1+lambda^2)]
  = rho_a(lambda)^2.                                (1.8)
```

The factor `1/[pi(1+lambda^2)]` is essential for atoms escaping to infinity.
An `a`-fold increase in raw root density can coexist with shrinking raw Clark
atoms or normalized reference weights.

## 2. An explicit full-type countermodel

Let

```text
b_w(z) = (z-w)/(z-conjugate(w)),
u_(a,n) = pi*n/a,
N_a = ceil(a^3/pi),

E_a(z)
  = -b_i(z) product_(n>N_a)
      b_(u_(a,n)+i)(z) b_(-u_(a,n)+i)(z).           (2.1)
```

The Blaschke condition holds because the paired zeros have imaginary part one
and `sum_(n>N_a) u_(a,n)^(-2)<infinity`.  Hence (2.1) is meromorphic inner in
the upper half-plane.  Directly,

```text
E_a(i)=0,       E_a(-x)=E_a(x)^(-1),       E_a(0)=1. (2.2)
```

For the lift with `Phi_a(0)=0`,

```text
Phi_a'(x)
 = 2/(1+x^2)
   + sum_(n>N_a) [
       2/((x-u_(a,n))^2+1)
       + 2/((x+u_(a,n))^2+1)].                     (2.3)
```

The added lattice begins beyond `a^2`.  More explicitly, if `a^2>=2R`, then
for `|x|<=R`,

```text
0 <= Phi_a'(x)-2/(1+x^2) <= 16/(pi*a).              (2.4)
```

Indeed, each paired summand is at most `16/u_(a,n)^2`, and
`sum_(n>N_a) n^(-2)<=1/N_a`.  Therefore

```text
Phi_a(R)-Phi_a(-R)
  = 4 arctan(R) + O_R(1/a),                         (2.5)
```

so every fixed compact has bounded phase mass.

This is not merely an abstract inner function of unspecified growth.  Put

```text
H_a(z)
  = (z+i) sin(a(z+i))
      / product_(n=-N_a)^N_a (z-u_(a,n)+i).         (2.6)
```

The apparent poles cancel sine zeros, so `H_a` is entire of exponential type
exactly `a`, has no upper-half-plane zeros, and direct cancellation gives

```text
H_a#/H_a
  = b_i product_(n>N_a)
      b_(u_(a,n)+i) b_(-u_(a,n)+i),
E_a = -H_a#/H_a.                                   (2.7)
```

For each fixed `a`, its far-tail phase-level count satisfies

```text
N_(a,theta)([-T,T]) = (2a/pi) T + O_a(1)            (2.8)
```

as `T` tends to infinity.  The remainder contains a term of size
`-2N_a`, hence order `-a^3`; (2.8) has no useful fixed-compact content as
`a` grows.  This realizes, within a regular Hermite--Biehler model, the exact
order-of-limits failure previously illustrated only by an escaping sequence.

For fixed `-pi<theta<pi`, the unique compact crossing satisfies

```text
lambda_(a,theta) -> tan(theta/2),
mu_(a,theta)({lambda_(a,theta)})
  -> pi sec(theta/2)^2,                              (2.9)
```

while its normalized reference-vector weight tends to one.  The total
normalized weight of all other atoms is

```text
2 sec(theta/2)^2/(pi*a) + o(1/a).                   (2.10)
```

At the exceptional parameter `theta=pi`, there is no finite limiting
crossing.  The two nearest atoms escape as

```text
lambda_a^+/- = +/-sqrt(pi*a/2)(1+o(1)),             (2.11)
```

each carrying normalized weight `1/2`.  Fixed-index crossings in the large
zero-free gap occur at scale `a`, have raw Clark weight `O(a)`, but normalized
weight `O(1/a)`.  In the eventual lattice region beyond scale `a^2`, crossings
have density `O(a)` and raw weights `O(1/a)`.

Consequently, full exponential type, all the displayed symmetries, the
canonical upper-half-plane zero, and a fixed-`a` Weyl law cannot prove the
desired compact phase growth.

## 3. The auxiliary-shift warning

There is a second, independent reason not to seek a theorem uniform over all
admissible shifts.  Suppose a self-adjoint metric `A` has an isolated simple
floor `lambda_0`, with reflection-parity eigenvector `phi`, and the forcing
vectors have nonzero overlap with `phi`.  As `sigma` increases to
`lambda_0`, the resolvent expansion is

```text
(A-sigma I)^(-1)
  = P_phi/(lambda_0-sigma) + O(1).                  (3.1)
```

After removing the common Fourier factor of `phi`, the characteristic tends
to

```text
E_infinity(z) = -epsilon (z-i)/(z+i),               (3.2)
```

where `epsilon` is the parity of `phi`.  Its reduced phase has

```text
Phi_infinity'(x)=2/(1+x^2),
Phi_infinity(T)-Phi_infinity(0)=2 arctan(T),         (3.3)
```

and its parity-matched raw Clark atom has weight `pi`, while the canonical
normalized reference-vector atom has weight one.

This is an exact resolvent-pole calculation, but its scope matters.  At real
zeros of the common Fourier factor, un-reduced finite characteristics can
develop rapid loops; a non-structure-preserving Galerkin projection can even
show phase backtracking.  Thus (3.1)--(3.3) do not by themselves prove bounded
raw phase mass for the exact completed-Weil family.  They do show that
admissibility of `sigma` alone cannot be the source of a uniform estimate.  A
surviving theorem must fix the shift, keep it quantitatively below the floor,
or control the common-factor singular regions separately.

## 4. Numerical scout and its boundary

The bounded-memory diagnostic in
`src/suzuki_compact_scaling_diagnostic.py` tested fixed shifts, near-floor
shifts, a scalar control, and a Dirichlet-energy control.  In completed-Weil
Legendre compressions at fixed shifts `-1/4` and `-1`, the sampled values were

```text
0.439 <= [Phi_L(T)-Phi_L(0)]/(L*T) <= 0.520
```

over the default grid, with similar rows for dimensions `10,12,14,16`.  This
is consistent with compact phase growth, but it is D-rated.

Near a simple Galerkin floor, the Dirichlet control approaches the reduced
Cayley behavior: at `L=3.555` and `T=96`, the sampled ratio was `0.009144`.
The completed-Weil near-floor rows become dimension-sensitive and can
backtrack, precisely where the projected characteristic ceases to preserve
the continuum Green identity.

This last point is load-bearing.  Direct comparison of the exact coherence
formula (1.4) with the finite-difference derivative of a completed-Weil
Galerkin phasor agrees at low frequency but fails badly at high frequency.
The finite projection is therefore not a structure-preserving discretization
of the Livšic kernel identity.  The numerical root, derivative, and formal
Clark columns are diagnostics only; none is promoted to a continuum claim.

## 5. The precise surviving theorem

Fix a cofinally admissible shift, for example `sigma=-1/4` if its full-space
admissibility can first be extended beyond the currently certified support.
For each fixed `R`, the desired raw-count result is exactly

```text
integral_(-R)^R dx/[(1+x^2) rho_a(x)^2] >= c_R a.   (5.1)
```

Two sufficient, genuinely quantitative versions are:

1. on a set `S_a` with uniformly positive
   `integral_(S_a) dx/(1+x^2)`, prove
   `rho_a(x)^2 <= C_R/a`;
2. prove the averaged estimate

   ```text
   integral_(-R)^R rho_a(x)^2 dx/(1+x^2) <= C_R/a.  (5.2)
   ```

Weighted Cauchy--Schwarz turns (5.2) into (5.1).  Neither estimate follows
from generic de Branges theory, as Section 2 proves.  It must arise from the
specific prime--archimedean structure of the completed Weil metric.

Even success at (5.1) would close only the unweighted divisor-convergence
branch.  Equation (1.7) describes the raw Clark measure, not automatically
the spectral probability of Suzuki's comparison vector.  For the canonical
reference defect vector its normalized measure is (1.8).  For any other
proposed comparison vector, the corresponding squared boundary-transform
factor must be computed explicitly.  The decisive checkpoint is whether the
extra roots carry vanishing total fixed-vector mass on compact sets.  The
follow-up in
[`SUZUKI-WEIGHTED-CLARK-MEASURE-CHECKPOINT.md`](SUZUKI-WEIGHTED-CLARK-MEASURE-CHECKPOINT.md)
shows that this additionally requires tightness, vector-compatible embeddings,
and the correct shifted global target.
