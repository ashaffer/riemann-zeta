# Execution synthesis for the categorical admission tests

Status: three proposed category-theoretic admission tests were instantiated on
the smallest available zero-independent finite fixtures, implemented, and
checked together on 2026-08-12.  Exact finite algebra is separated below from
floating Ritz and quadrature diagnostics.  No zero-free strip or RH theorem is
proved.

**Subsequent high-height correction.**  The recommendation below to continue
with the target-subtracted support `h_eta(R_T)` has now been executed and
pruned.  Exact bookkeeping gives

```text
R_T=N_T+K_ar,T|S_T,
q_eta=inf_(mu>=0) Phi_eta(mu),
h_eta=eta+inf_(mu>=1) Phi_eta(mu).
```

Thus target subtraction inserts an aligned carrier baseline and discards
dual multipliers in `[0,1)`; it does not create a smaller remainder problem.
The surviving object is the direct constrained arithmetic edge
`q_eta(K_ar,T)`.  The actual prime-power/pole/gamma fixture has also been
assembled and run, but only as a floating finite diagnostic.  This notice
supersedes the rankings in Sections 1 and 6; see
[`ZETA23-CARRIER-SLICE-ALIGNED-BASELINE-NOGO-2026-08-12.md`](ZETA23-CARRIER-SLICE-ALIGNED-BASELINE-NOGO-2026-08-12.md),
[`ZETA23-ACTUAL-HIGH-HEIGHT-CARRIER-SLICE-FIXTURE-2026-08-12.md`](ZETA23-ACTUAL-HIGH-HEIGHT-CARRIER-SLICE-FIXTURE-2026-08-12.md),
and
[`ZETA23-DIRECT-CARRIER-SLICE-FRONTIER-SYNTHESIS-2026-08-12.md`](ZETA23-DIRECT-CARRIER-SLICE-FRONTIER-SYNTHESIS-2026-08-12.md).

## 1. Executive verdict

The tests do not create a strip, but they materially shrink the search space.

| route | finite admission result | decision |
|---|---|---|
| scalar probe/sheaf order descent | fails exactly once the first zero-independent left/right support contrast is admitted | stop |
| parity CP recovery on the symmetric two-packet system | exists exactly, but only returns the two original eigenvalues | stop as an engine |
| full matrix-valued recovery | succeeds by retaining the whole block | conservative; no reduction |
| block-dephasing Stinespring covariance | equals the existing normalized Schur coupling squared | stop unless a different arithmetic covariance identity is found |
| one-sided carrier-slice support | exact scalar dual, strict improvement over an operator norm, and useful finite diagnostics | continue first |
| ungraded approximate polarization | impossible with defect below one because of the pole/Tate eigenvalues `0,1` | stop |
| graded middle-sector approximate polarization | exact spectral implication, but no zeta generator or divisor identification exists | architectural, low readiness |

The immediate mathematical target is therefore not another categorical
formalism.  It is the construction and estimation of one actual high-height
compressed remainder:

```text
S_T = positive-row-null two-lobe Gabor quotient,
N_T = selected-pair carrier on S_T,
R_T = actual prime/on-line/collateral aggregate remainder on S_T.
```

For a fixed carrier threshold `eta_T`, its first admission number is

```text
h_eta_T(R_T)
 = inf_(mu>=0)
     [lambda_max(R_T+mu*N_T)-mu*eta_T].             (1.1)
```

The solver is now elementary.  The missing work is to assemble or prove a
uniform theorem about `R_T`, and then to control the remaining completed-form
and Schur costs if (1.1) is carrier-sized.

## 2. What was actually executed

The three focused reports are:

- [`ZETA23-FINITE-OPERATOR-SYSTEM-ADMISSION-GATE-2026-08-12.md`](ZETA23-FINITE-OPERATOR-SYSTEM-ADMISSION-GATE-2026-08-12.md);
- [`ZETA23-CARRIER-SLICE-SUPPORT-FINITE-FIXTURE-2026-08-12.md`](ZETA23-CARRIER-SLICE-SUPPORT-FINITE-FIXTURE-2026-08-12.md); and
- [`ZETA23-APPROXIMATE-POLARIZATION-SEMILOCAL-FAIL-FAST-2026-08-12.md`](ZETA23-APPROXIMATE-POLARIZATION-SEMILOCAL-FAIL-FAST-2026-08-12.md).

Their implementations and exact regression tests are:

```text
src/categorical_operator_system_gate.py
src/test_categorical_operator_system_gate.py
src/carrier_slice_support.py
src/test_carrier_slice_support.py
src/approximate_polarization_gate.py
src/test_approximate_polarization_gate.py
```

The combined deterministic suite passes:

```text
python3 -m pytest -q \
  src/test_categorical_operator_system_gate.py \
  src/test_carrier_slice_support.py \
  src/test_approximate_polarization_gate.py

20 passed
```

## 3. Order reflection: the first asymmetric fixture is decisive

At support `L=7/4`, two interior hats and the first prime translation generate
the reflection-symmetric operator system

```text
E_mir=span_C{I,J},                 J=[[0,1],[1,0]].
```

Coordinate scalar probes have `J` in their kernel and therefore fail order
reflection.  Parity probes do admit the exact UCP recovery

```text
Psi(x,y)=x P_+ + y P_-.
```

On the normalized reflected-pair block `m(I+CJ)`, however, these outputs are
exactly `m(1+C)` and `m(1-C)`.  The recovery exposes the negative carrier; it
does not sign it arithmetically.

The first zero-independent left/right support contrast adds

```text
Z=diag(1,-1),
span_R{I,J,Z}=Sym_2(R).
```

No fixed finite set of scalar vector-state probes can reflect the PSD order
on this full space: finitely many scalar inequalities define a polyhedral
cone, while the `2 x 2` PSD cone is nonpolyhedral.  This does not exclude a
smaller independently specified arithmetic subspace or a theorem signing one
actual element.  The four natural coordinate/parity probes
already miss the exact strict witness

```text
A_*=7/16 I-(9 sqrt(2)/32)(J+Z),
spec(A_*)={-1/8,1},
all four probe values >=(14-9 sqrt(2))/32>0.         (3.1)
```

A full matrix-valued parity-pair probe has a UCP inverse because it retains
the complete matrix.  This is conservative transport, not a smaller local
positivity theorem.

The natural nonlinear candidate also collapses.  For block dephasing of

```text
H=[[A,B],[B*,D]],
```

the Stinespring/Kadison covariance is

```text
diag(BB*,B*B),
```

and after diagonal normalization its norm is exactly

```text
||A^(-1/2) B D^(-1/2)||^2.                          (3.2)
```

Thus it repackages the old Schur coupling.  The tested prime-5 fixtures have
normalized couplings from about `0.878` to `0.99985`; those are ordinary
floating diagnostics, not uniform bounds.

### Decision

Do not spend further effort refining finite scalar covers of the asymmetric
packet system.  A future operator-system experiment is admissible only if it
uses a **proper** matrix-valued cross probe, has CP recovery on the actual
arithmetic system, omits genuine ambient directions, and produces output
matrices whose signs are independently easier to prove.

## 4. Carrier-slice support: the surviving executable test

For Hermitian `R`, `N>=0`, and

```text
F_eta={Gamma>=0: Tr Gamma=1, Tr(N Gamma)>=eta},
```

the exact support function is

```text
h_eta(R)=max_(Gamma in F_eta) Tr(R Gamma)
        =inf_(mu>=0)
           [lambda_max(R+mu N)-mu eta],             (4.1)
```

when `eta<lambda_max(N)`, with the largest eigenvalue of `R` restricted to the
top eigenspace of `N` at equality.  A rank-one optimizer always exists.  This
turns the proposed SDP into one
scalar convex eigenvalue minimization.

Two exact controls show why this quantity matters.

1. On the normalized one-pair mirror, the positive-null quotient is one
   dimensional.  The exact diagonal remainder has support `m`, while the
   aligned cross bill is `m cosh(alpha D)`.  Their ratio is

   ```text
   sech(alpha D),
   ```

   so this obvious remainder is subcarrier.
2. In the abstract two-pair collateral fixture, `h_eta` has a closed
   piecewise formula and reproduces the exact `2/11` aggregate-null state.
   At a `75%` carrier requirement it is negative even though `R_+` is
   nonzero.  Therefore unrestricted positive-part norms can give a false
   positive verdict that the carrier slice correctly rejects.

The optional finite zeta-coefficient control uses the `{2,3}` form and the
actual `p=5` event at `L=3.27`.  It gives `h_eta/eta` about `6.88` for the full
fixture and `9.37` for the relative fixture.  This passes the **necessary**
one-sided sign test, but the full coupling is still nearly critical and the
full minimum is tiny.  These floating finite-stage values are not evidence
for a high-height strip.

### Decision

This is the highest-priority route because the categorical problem has been
reduced to an explicit scalar quantity and the existing countermodels make
its polarity meaningful.  The next theorem must control the actual `R_T` in
(1.1), not optimize the solver or test more unrelated small matrices.

## 5. Approximate polarization: exact implication, missing object

For a finite generator `A` and `G>0`, define

```text
epsilon_G(A)
 =||G^(-1/2)(A*G+GA-G)G^(-1/2)||.                  (5.1)
```

Every eigenvalue obeys the exact lower bound

```text
epsilon_G(A)>=|2 Re(lambda)-1|.                     (5.2)
```

For diagonalizable `A`, an eigenvector-fitted metric attains equality.  Such
a post-hoc optimization reads back the desired spectral width and is not an
independent proof.

Two fail-fast conclusions follow.

- Any ungraded generator which retains invariant pole/Tate eigenvalues `{1,0}`
  forces `epsilon>=1` for every positive metric, including metrics with
  cross-sector entries.  Such a model must isolate a positive middle degree
  before a strict defect below one is possible.
- The natural semilocal Euler metric is not Loewner-monotone under the
  identity realization when a prime is added.  Frozen-generator finite
  diagnostics can exceed one.

There is an exact positive control: in the gamma-plus-one-Euler-factor cyclic
measure, compression of multiplication by `1/2+i s` has defect zero in its
native metric, and the Euler multiplier transports this control isometrically.
This is zero-independent but tautological at the spectral level: the
multiplication spectrum is on the critical line by construction, and no
determinant or resolvent identifies it with the nontrivial zeta divisor.

### Decision

Stop metric optimization until there is a degree-isolated, zero-independent
middle zeta generator with connected prime/gamma trace and a conservative
spectral identification.  Once such an object exists, an interval-certified
test of `epsilon<1` would be decisive.  Before then, the LMI is a detector,
not an engine.

## 6. Pruned and surviving search nodes

### Pruned now

- finite scalar sheaf/probe refinements on the asymmetric two-packet system;
- parity recovery as a source of a new sign;
- full-block CP recovery as a reduction;
- the obvious dephasing covariance as a new transverse reservoir;
- ungraded pole-inclusive approximate polarization; and
- post-hoc Lyapunov metric fitting.

### Survives, ranked

1. **Actual carrier-slice theorem.**  Construct `S_T,N_T,R_T`; estimate
   (1.1) uniformly and then pay the full completed-form/Schur cost.
2. **Proper matrix-valued arithmetic recovery.**  Only test a larger fixture
   if the proposed cross cover is strictly smaller than the ambient block and
   its output sign has an independent arithmetic formulation.
3. **Graded middle quasi-polarization.**  Construct the missing generator and
   divisor identification before optimizing any metric.
4. **Signed covariance/cross-effect identity.**  Reopen only if an exact
   completed arithmetic formula inserts a positive multiplicative defect with
   the needed sign and at carrier scale.

The first item is closest to the existing explicit-formula machinery.  The
third could be more conceptually powerful, but it currently requires a new
cohomological/spectral object rather than an estimate on an existing one.

## 7. Truth boundary

These experiments certify finite algebraic admissions and exclusions inside
the stated construction grammar.  They do not prove that every categorical
approach is impossible, do not identify an actual off-line zeta zero, and do
not establish or refute any fixed zero-free strip.  A successful next step
must add one of the genuinely missing arithmetic inputs; changing categorical
vocabulary without changing the order or carrier information will not do so.

The independent hostile audit records verdict **PASS AFTER PATCHES** in
[`CATEGORICAL-ADMISSION-TESTS-REFEREE-AUDIT-2026-08-12.md`](CATEGORICAL-ADMISSION-TESTS-REFEREE-AUDIT-2026-08-12.md).
