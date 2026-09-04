# The direct constrained arithmetic edge is the surviving carrier frontier

Status: synthesis of the exact target-conditioned construction, the
aligned-baseline no-gain theorem, and the first actual-coefficient
sharp-Gabor fixtures, 2026-08-12.  The structural statements below are
finite-dimensional theorems.  The fixture values are ordinary
double-precision diagnostics, not interval certificates.  No uniform
zero-free strip or RH statement is proved.

Subsequent update: the planned interval scan and low-dimensional reduction
have been executed, and the target-only mirror-isolation branch has been
falsified by a normalized phase-flip configuration.  The current synthesis is
[`ZETA23-THREE-STEP-SUBFULL-CARRIER-ITERATION-SYNTHESIS-2026-08-12.md`](ZETA23-THREE-STEP-SUBFULL-CARRIER-ITERATION-SYNTHESIS-2026-08-12.md).

## 1. Verdict

The carrier program survives, but its correct object is not the support of
the target-subtracted remainder.

For a hypothetical reflected pair

```text
rho_0=1/2+alpha+i*gamma,                             (1.1)
```

let `S_T` be the endpoint-flat coefficient space with the selected positive
row nulled, and let

```text
N_T=kappa_T*a_T*a_T^*,       ||a_T||=1.             (1.2)
```

The completed arithmetic matrix

```text
K_ar,T=K_pole,T+K_arch,T-K_prime,T                  (1.3)
```

uses the actual von Mangoldt coefficients, every active prime power, and
the pole and gamma terms.  Apart from the explicitly chosen candidate
`(alpha,gamma)`, it uses no zero data.

The surviving finite quantity is

```text
q_eta(K_ar,T)
 =max {Tr(K_ar,T Gamma):
       Gamma>=0, Tr Gamma=1, Tr(N_T Gamma)>=eta}.    (1.4)
```

For `0<=eta<kappa_T`, it has the exact reductions

```text
q_eta(K_ar,T)
 =max_(||z||=1, <z,N_T z>>=eta) <z,K_ar,T z>
 =inf_(mu>=0)
    [lambda_max(K_ar,T+mu*N_T)-mu*eta].             (1.5)
```

At full carrier,

```text
q_kappa(K_ar,T)=<a_T,K_ar,T*a_T>.                   (1.6)
```

This is the smallest zero-independent, target-conditioned arithmetic edge
left by the categorical and carrier audits.  It is a one-dimensional
eigenvalue minimization, and at full carrier it is one completed
von-Mangoldt/pole/gamma scalar.

The earlier target-subtracted proposal

```text
R_full,T=(K_ar,T-K_0,T)|S_T                         (1.7)
```

contains a deterministic aligned baseline.  Since
`K_0,T|S_T=-N_T`, exactly

```text
R_full,T=N_T+K_ar,T|S_T.                            (1.8)
```

Consequently its support `h_eta(R_full,T)` is not a smaller arithmetic
remainder test.  If

```text
Phi_eta(mu)=lambda_max(K_ar,T+mu*N_T)-mu*eta,
```

then

```text
q_eta=inf_(mu>=0) Phi_eta(mu),
h_eta(R_full,T)=eta+inf_(mu>=1) Phi_eta(mu).         (1.9)
```

Target subtraction deletes the dual interval `0<=mu<1` and adds `eta`.
It can only lose information.  At full carrier,

```text
h_kappa(R_full,T)=kappa_T+q_kappa(K_ar,T).          (1.10)
```

Thus the revised decision is:

```text
retain:  direct q_eta(K_ar,T), especially q_kappa;
prune:   h_eta(K_ar,T-K_0,T) as an independent arithmetic route;
open:    a uniform carrier-scale sign theorem for q_eta and the matching
         target-isolation theorem on the divisor side.                 (1.11)
```

## 2. The target-conditioned logic is noncircular

There are three different uses of zero information and they must remain
separate.

### 2.1 Legitimate contradiction parameter

To test whether a zero can occur at `(alpha,gamma)`, assume that candidate
pair for contradiction and use it to define only

```text
S_T=ker(x_0^*) inside the chosen endpoint-flat space,
N_T=(2/L^2)*(P_(S_T)y_raw)*(P_(S_T)y_raw)^*.        (2.1)
```

Here `y_raw` is the raw sharp evaluation row used by the executable.  In the
normalized-row convention `y_0=y_raw/L`, the same formula is
`N_T=2(P_S y_0)(P_S y_0)^*`.

This is ordinary target conditioning.  For every candidate, the same
construction can be performed before knowing whether the candidate is an
actual zero.

### 2.2 Zero-independent arithmetic evaluation

After `(alpha,gamma)` fixes the quotient and carrier, `K_ar,T` is assembled
from

```text
actual Lambda(n)/sqrt(n) at log n in the support,
the two pole evaluations,
the exact archimedean multiplier.                   (2.2)
```

No collateral zero is used to build or evaluate (1.4).  This makes
`q_eta` a valid arithmetic quantity in a proof by contradiction and a
valid diagnostic even when the selected candidate is not a zero.

### 2.3 Divisor-side interpretation, not input

Only after assuming that `rho_0` is an actual zero may the completed
explicit formula be read as

```text
K_ar,T|S_T=-N_T+R_other,T.                          (2.3)
```

Here `R_other,T` contains on-line and nonselected reflected-pair
contributions.  Equation (2.3) explains screening and permits estimates
from independently proved zero-density or sampling theorems.  It does not
license constructing `S_T` as the kernel of all unknown positive zero rows.
That all-zero quotient would be circular as a zero-independent arithmetic
object.

## 3. Exact logic needed for a zero exclusion

The direct arithmetic edge and divisor isolation have complementary roles.
For the feasible state set `F_eta` in (1.4), (2.3) gives

```text
q_eta(K_ar,T)
 =max_(Gamma in F_eta)
    [-Tr(N_T Gamma)+Tr(R_other,T Gamma)].           (3.1)
```

Therefore

```text
h_eta(R_other,T)<eta
  implies q_eta(K_ar,T)<0.                          (3.2)
```

An arithmetic admission theorem in the opposite direction,

```text
q_eta(K_ar,T)>=0,                                   (3.3)
```

would contradict (3.2) and exclude the candidate pair.

Neither half may be silently assumed.

- The current shallow-depth sampling theorem makes the on-line rows and
  collateral pairs below `alpha*d-epsilon` subcarrier.  It does not control
  a deep near-tie pair, its signed orientation, or every open completion and
  localization summand.
- The current von Mangoldt estimates give logarithmic cancellation but no
  fixed-depth carrier-scale sign theorem for (1.4).

Thus a positive finite value of `q_eta` is an **arithmetic admission** for
that fixture, not a proof that an actual target zero is impossible.  A
rigorously certified negative value would furnish a negative completed Weil
test (and hence contradict RH by the Weil criterion), but it would not by
itself locate a zero at the selected candidate.  A floating negative value
would establish neither conclusion.

There is no conflict between this statement and the fixture's description
of `q_eta>=0` as only an admission.  A nonnegative target-only optimizer can
be deleted by additional positive zero rows, so (3.3) alone says nothing
about an actual divisor.  In the two-lemma closure, however, (3.2) is a
uniform upper bound on the **same target-only feasible set**; it says every
such optimizer is negative.  Only that paired assertion makes (3.2) and
(3.3) contradictory.

## 4. Exact construction used by the high-height fixture

The executable fixture in
[`high_height_carrier_slice.py`](../src/high_height_carrier_slice.py),
documented in
[`ZETA23-ACTUAL-HIGH-HEIGHT-CARRIER-SLICE-FIXTURE-2026-08-12.md`](ZETA23-ACTUAL-HIGH-HEIGHT-CARRIER-SLICE-FIXTURE-2026-08-12.md),
uses the following finite model.

```text
L=log T,                 X=exp L=T,
gamma=3T/2,
tau_k=gamma+2*pi*k/L,
phi=1_[-L/2,L/2].                                  (4.1)
```

A critical sharp Fourier aperture contained in `[T,2T]` is compressed by
the first `m` endpoint moments.  With sign conjugation, the code assembles

```text
K_ar=(H_arch+H_pole-H_prime)/L^2.                   (4.2)
```

The prime matrix retains all prime powers `n<=X` with their actual weights
`Lambda(n)/sqrt(n)`.  The archimedean matrix is evaluated from closed
digamma/trigamma formulas with an exponentially convergent finite-support
tail.  The pole matrix is rank two.

There is an independent completion check:

```text
H_arch+H_pole-H_prime
 =H_centered_actual+H_arch+H_rational.              (4.3)
```

The left side is assembled directly, while `H_centered_actual` is rebuilt
from the exact confluent-Loewner scalar data `A_X,D_X` after subtracting the
continuum.  This checks every sign and completion term by a second formula.

The selected candidate row is then projected through the endpoint-null
space, its positive part is nulled, and the negative part gives `N_T`.
No actual-zero table is loaded.  In particular, the fixture explicitly
records

```text
candidate_is_asserted_zero = false.                 (4.4)
```

## 5. First actual-coefficient finite diagnostics

The following run used

```text
alpha=0.4,
aperture fraction=0.2,
m=ceil(log T) with a minimum of 3,
T in {32,64,128,256,512}.                           (5.1)
```

This slowly growing `m` is an illustrative endpoint-flat fixture choice.  It
is not the maximal mesoscopic Zeta23 jet budget, whose relevant orders can be
of size `eta*T`, and the table does not transfer to that different quotient.

All entries below are floating values.  `dim S` is the dimension after the
endpoint moments and selected positive row are removed.  `ret` is the ratio
of the retained finite carrier to the infinite sharp-lattice carrier.

| `T` | `dim S` | `kappa` | `ret` | `lambda_min(K_ar|S)` | `q_.5/kappa` | `q_.9/kappa` | `q_1/kappa` |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 32 | 2 | 0.052956 | 0.1502 | 0.21449 | 10.109 | 8.924 | 7.113 |
| 64 | 11 | 0.287376 | 0.5428 | 0.000362 | 4.105 | 3.286 | 2.338 |
| 128 | 33 | 0.584987 | 0.7726 | `1.17e-12` | 2.238 | 1.612 | 1.078 |
| 256 | 84 | 0.890464 | 0.8505 | `-3.42e-14` | 1.715 | 1.407 | 1.216 |
| 512 | 195 | 1.311849 | 0.9283 | `-8.84e-14` | 1.223 | 0.980 | 0.763 |

The final three minimum eigenvalues are at numerical zero and must not be
reported as certified signs.  The constrained maxima `q_eta`, however, are
unscaled-positive in all fifteen displayed cases.  At `T=512`, the ratios at
`theta=0.9,1` fall below one while the raw values remain
`1.286210907,1.000438845`; this is another reason not to extrapolate a ratio
from five points.

At full carrier the decomposition is especially transparent:

| `T` | background top scalar | centered actual top scalar | `q_1` |
|---:|---:|---:|---:|
| 32 | 0.586333 | -0.209637 | 0.376696 |
| 64 | 0.655454 | 0.016508 | 0.671961 |
| 128 | 0.704734 | -0.073923 | 0.630811 |
| 256 | 0.741664 | 0.341539 | 1.083203 |
| 512 | 0.770377 | 0.230062 | 1.000439 |

Here `background=arch+rational`, and `centered actual` is the completed
von Mangoldt fluctuation.  Their signs and sizes vary with `T`; the four
points do not support a monotonic extrapolation.

The largest observed algebraic residuals were below `4e-14` for the
independent completed decomposition and below `7e-15` for endpoint and
selected-row nulling, except that these are again floating residuals rather
than certified enclosures.  The five focused fixture tests pass.  The
default five-height run took about `2.5 s` and peaked near `65 MB` resident
memory on the reporting machine.

The target-subtracted values also obeyed exactly the predicted baseline
sandwich

```text
q_eta+eta<=h_eta<=q_eta+kappa.                      (5.2)
```

At full carrier their gap was `h_kappa-q_kappa=kappa` to roundoff.  This is
a validation of the aligned-baseline theorem, not evidence for a collateral
reservoir.

## 6. What these numerics establish

They establish that:

1. the target-conditioned quotient and rank-one carrier can be constructed
   without loading collateral zeros;
2. the actual prime-power, pole, and gamma matrices can be assembled at
   moderate height with low memory;
3. the independent completion spelling agrees to double precision;
4. the direct constrained edge is computationally inexpensive after matrix
   assembly; and
5. the target-subtracted support visibly contains the exact aligned
   baseline predicted by (1.8)--(1.10).

They do **not** establish that:

1. `(alpha,gamma)` in any run is a zeta zero;
2. any displayed eigenvalue or `q_eta` is interval-certified;
3. the sign persists for all candidates, heights, apertures, jet orders, or
   limiting packet geometries;
4. a deep collateral pair cannot provide screening;
5. the sharp finite aperture is already in its asymptotic regime; or
6. a zero-free strip or RH follows.

In particular, the table is a successful pipeline admission test.  It is
not statistical evidence for a theorem about the zeta divisor.

The earlier low-dimensional prime-5 Ritz fixture proved that the
carrier-slice SDP is computationally nontrivial and can be sharper than an
unrestricted positive-part norm.  It did not assemble a high-height
completed zeta matrix.  The present fixture supplies that missing
actual-coefficient pipeline, while the aligned-baseline theorem explains
why its primary output must be `q_eta`, not the target-subtracted `h_eta`.

## 7. Why the standard estimates stop at the same frontier

For a normalized two-packet carrier with separation `D_T`, put

```text
Y=exp(D_T),
kappa_T=Y^(alpha+o(1))/L.                           (7.1)
```

The top-carrier centered arithmetic scalar contains the smooth actual
von Mangoldt polynomial

```text
S_(Y,w)(gamma)
 =integral v^(-1/2)*omega_(T,w)(log(v/Y))
                  *cos(gamma*log v)d(psi(v)-v).     (7.2)
```

The available pointwise KMT upper bound is

```text
S_(Y,w)(gamma)
 <<_w Y^(1/2)/(log Y)^(3/10).                       (7.3)
```

Relative to a fixed-depth carrier, this leaves

```text
Y^(1/2-alpha)/(log Y)^(3/10),                       (7.4)
```

which diverges for every fixed `alpha<1/2`.  Positive von Mangoldt
coefficients do not help because the packet correlation has the phase
`cos(gamma log n)` and completion centers `d psi` by `dv`.  A local large
sieve returns the same root scale at a pointwise selected ordinate.
Confluent rank-two displacement reconstructs the matrix from scalar data
but does not sign its free diagonal.

For the moving depth

```text
alpha=1/2-delta_Y,
delta_Y*log Y<=(3/10-epsilon)*loglog Y,              (7.5)
```

(7.3) is genuinely `o(Y^alpha)`.  That very narrow regime lies inside the
classical zero-free region and supplies no new zeta result.  At a fixed
depth, a matched improvement to `o(Y^alpha)` uniformly at all selected
ordinates is the same strip-strength prime-polynomial input isolated by the
earlier endpoint and Loewner audits.

## 8. The smallest surviving theorem

The finite fixture suggests one precise arithmetic theorem which is weaker
than positivity of the whole completed matrix.

### Direct constrained arithmetic admission target

Find fixed parameters

```text
alpha_0 in (0,1/2),
theta in (0,1],
an admissible endpoint-flat packet/aperture geometry,                 (8.1)
```

and prove, uniformly for every sufficiently large `T`, every candidate
depth `alpha in [alpha_0,1/2)`, and every `gamma` in a fixed dyadic core
`[(1+sigma)T,(2-sigma)T]`,

```text
q_(theta*kappa_T)(K_ar,T;alpha,gamma)>=0.            (8.2)
```

Varying `T` continuously, or using a sufficiently fine overlapping
geometric cover, covers all sufficiently large ordinates by such cores.
Allowing the packet parameters to depend on `alpha` is harmless only if the
family and all constants remain uniform for `alpha>=alpha_0`.

This asks only for one carrier-retaining nonnegative state, not
`K_ar,T>=0` on the full test space.  It is therefore the smallest direct
arithmetic sign theorem supported by the exact reduction and the finite
fixtures.

It does not close a strip alone.  The matching target-isolation statement is:

```text
if rho_0=1/2+alpha+i*gamma is a zeta zero with alpha>=alpha_0, then
h_(theta*kappa_T)(R_other,T)<theta*kappa_T,          (8.3)
```

or any sharper direct argument implying

```text
q_(theta*kappa_T)(K_ar,T)<0.                         (8.4)
```

Equations (8.2) and (8.4) are contradictory.  Current sampling proves
(8.3) only for the already isolated shallow part; a deep near-tie
collateral pair and open completion/localization tails remain.

Accordingly, the smallest honest closing package is:

```text
ARITHMETIC
  prove the direct admission inequality (8.2) from the actual completed
  von Mangoldt/Loewner pencil;

DIVISOR GEOMETRY
  prove that a hypothetical depth-alpha_0 target cannot have a
  carrier-sized signed deep/transverse screening remainder;

CONTRADICTION
  combine (3.1)--(3.3), without constructing an all-zero quotient.       (8.5)
```

The fixed fixture demonstrates that the first clause is executable and
exactly formulated; it does not prove its required uniformity.  The second is
where near-tie collateral geometry remains genuinely open.  Neither should
be hidden inside the target-subtracted support functional.

## 9. Next disciplined iteration

1. Replace the floating `q_eta` values by interval-certified eigenvalue
   bounds for a small fixture, including interval enclosures of the
   archimedean tail.
2. Scan candidate phase and depth on a fixed certified aperture to test
   whether the sign in (8.2) is even plausible uniformly; report minima,
   not selected favorable points.
3. Use the confluent-Loewner representation to reduce a uniform lower bound
   for `q_eta` to the smallest possible completed scalar inequality.
4. Separately attack the normalized two-pair restriction map or another
   signed-angle invariant that can rule out a carrier-scale deep transverse
   remainder.
5. Stop the route immediately if an interval-certified candidate produces
   `q_eta<0` in the proposed uniform parameter regime; that falsifies
   (8.2) for that geometry but is not a zeta-zero claim.

Principal inputs:

- [`ZETA23-HIGH-HEIGHT-CARRIER-SLICE-ANALYTIC-REDUCTION-2026-08-12.md`](ZETA23-HIGH-HEIGHT-CARRIER-SLICE-ANALYTIC-REDUCTION-2026-08-12.md),
- [`ZETA23-ACTUAL-HIGH-HEIGHT-CARRIER-SLICE-FIXTURE-2026-08-12.md`](ZETA23-ACTUAL-HIGH-HEIGHT-CARRIER-SLICE-FIXTURE-2026-08-12.md),
- [`ZETA23-CARRIER-SLICE-ALIGNED-BASELINE-NOGO-2026-08-12.md`](ZETA23-CARRIER-SLICE-ALIGNED-BASELINE-NOGO-2026-08-12.md),
- [`ZETA23-CARRIER-SLICE-SUPPORT-FINITE-FIXTURE-2026-08-12.md`](ZETA23-CARRIER-SLICE-SUPPORT-FINITE-FIXTURE-2026-08-12.md),
- [`ZETA23-ENDPOINT-PACKET-PRIME-FORM-THEOREM-CARD-2026-08-11.md`](ZETA23-ENDPOINT-PACKET-PRIME-FORM-THEOREM-CARD-2026-08-11.md), and
- [`ZETA23-CONSTRAINED-SHARP-LOEWNER-PRIME-EDGE-2026-08-11.md`](ZETA23-CONSTRAINED-SHARP-LOEWNER-PRIME-EDGE-2026-08-11.md).

The combined reduction, no-go theorem, executable, fixture, and synthesis
have independent verdict **PASS AFTER PATCHES** in
[`HIGH-HEIGHT-CARRIER-SLICE-REFEREE-AUDIT-2026-08-12.md`](HIGH-HEIGHT-CARRIER-SLICE-REFEREE-AUDIT-2026-08-12.md).
