# Sub-full direct-q fail-fast and rigorous finite certificate

Status: completed adversarial finite iteration, 2026-08-12.

This report concerns the target-conditioned sharp-grid arithmetic functional

```text
q_eta(K_ar) = max Tr(K_ar Gamma)
              Gamma >= 0, Tr Gamma = 1, Tr(N Gamma) >= eta,
eta = theta*kappa,  kappa = lambda_max(N).
```

It is a finite screening diagnostic.  It is not a uniform arithmetic
admission theorem, a zero-side exclusion theorem, a new zero-free region, or
a proof of RH.

## 1. Decision result

The negative fail-fast did **not** fire.

Two deterministic scans were run.  A broad, cheap boundary scan covered
61,896 valid full-carrier configurations.  A focused scalar-dual scan covered
11,565 valid slices at `theta=0.9,0.99,1`.  Neither scan produced a value below
`-1e-10`.

The closest grid point in normalized units was

```text
T=16, gamma/T=1.31, grid phase=0.49,
aperture=0.32, jet order=1, alpha=0.499.
```

At this point the floating values were

| `theta` | `q_eta` | `q_eta/kappa` | floating dual `mu` |
|---:|---:|---:|---:|
| 0.90 | 0.08510881917 | 0.507571839 | 4.60116860 |
| 0.99 | 0.01392877869 | 0.083068428 | 5.06557672 |
| 1.00 | 0.004319753120 | 0.025762137 | boundary |

The exact monotonicity

```text
theta_1 <= theta_2  ==>  q_(theta_1*kappa) >= q_(theta_2*kappa)
```

explains why the full-carrier boundary is the first, inexpensive sign screen
for each fixed matrix.  A positive boundary value rules out a negative
sub-full value for that same matrix.  A negative boundary value would not by
itself certify a negative sub-full value; the finite dual still has to be
checked at the requested `theta`.

## 2. Scan scope

The broad boundary scout used

```text
T in {8,12,16,24,32,48,64},
gamma/T in {1.12,1.215,1.31,1.405,1.5,1.595,1.69,1.785,1.88},
phase in {-0.49,-0.33,-0.17,0,0.17,0.33,0.49},
aperture in {0.08,0.12,0.16,0.20,0.24,0.28,0.32},
all admissible jet orders, alpha in {0.05,0.15,0.25,0.35,0.45,0.499}.
```

There were 1,121 valid arithmetic bases and 61,896 valid conditioned
full-carrier points.  The minimum sampled normalized value was
`q_kappa/kappa=0.02576213669` at the point displayed above.

The focused multi-theta run used

```text
T in {16,32,64},
the same nine gamma fractions and seven phases,
aperture in {0.16,0.24,0.32},
jet order in {0,1,2,3,5},
alpha in {0.25,0.4,0.499}, theta in {0.9,0.99,1}.
```

Of 567 requested base parameter tuples, 275 stayed inside the dyadic band and
left at least five critical-grid nodes.  They produced 11,565 valid slices;
810 conditioned requests were skipped because their jet budget left
insufficient dimension.  Runtime was 6.5 seconds on the development machine.

These are Cartesian samples, not coverage of continuous parameter boxes.  In
particular, no statement is made between sampled heights, phases, depths, or
apertures.

## 3. Correct phase-dependent selected row

For

```text
tau_k = gamma + 2*pi*(k+phi)/L,
z = gamma-i*alpha,
```

endpoint sign conjugation gives

```text
v_k = 2 sin(-i*alpha*L/2-pi*phi)/(z-tau_k).
```

Thus phase is not a harmless translation of the old centered-row formula.
The implementation uses this exact factor and tests that `phi=0` recovers the
established fixture.  Using the centered numerator at nonzero phase would
have scanned the wrong selected-null space.

## 4. Rigorous negative-dual interface

The implementation is
[`subfull_direct_q_failfast.py`](../src/subfull_direct_q_failfast.py), with
tests in
[`test_subfull_direct_q_failfast.py`](../src/test_subfull_direct_q_failfast.py).

The proof path uses python-flint 0.9.0 with Arb/Acb ball arithmetic.  It does
not reuse the floating SciPy nullspace.

Let `E` be an exact rational RREF basis of

```text
W_m = {c : sum_k k^r c_k=0, 0<=r<m}.
```

The selected real row `x*E` is evaluated with Arb.  A pivot interval separated
from zero eliminates one coordinate and produces a full, generally
nonorthonormal interval basis `B` of `W_m intersect ker(x*)`.  Put

```text
G = B*B,
K = B* K_ar B,
n = B*y,
N = (2/L^2) n n*,
kappa = (2/L^2) n* G^(-1) n.
```

The prime matrix uses every exact prime power `n<=T` with Arb coefficient
`log(p)/sqrt(n)`.  Pole entries use the closed rank-two formula.  The
archimedean divided-difference formula uses Acb digamma and polygamma values;
the remaining exponential series is enclosed by the explicit geometric
tails

```text
exp(-r_N L)/(r_N(1-exp(-2L)))
and
exp(-r_N L)/(r_N^2(1-exp(-2L))).
```

Given rational `mu>=0` and `delta>0`, an interval `LDL*` factorization tests

```text
(mu*theta*kappa-delta)G - K - mu*N > 0.              (4.1)
```

If every interval pivot has positive lower endpoint, (4.1) proves on the
entire finite selected-null space

```text
K_ar+mu*N <= (mu*theta*kappa-delta)I,
q_(theta*kappa)(K_ar) <= -delta.
```

This is a proof-producing interface: a floating negative number is never
promoted unless the full interval rebuild and (4.1) succeed.

## 5. Honest interval replay of the closest sample

The closest sampled full-carrier point was rebuilt at 192-bit precision using
the rational parameters

```text
T=16, gamma/T=131/100, phase=49/100,
aperture=8/25, alpha=499/1000, m=1.
```

The selected-null dimension is three.  Arb returned

```text
kappa = [0.1676783712331281021155089714978195237836 +/- 4.75e-41]
q_kappa = [0.004319753120250996038800722197058190834782 +/- 2.59e-43].
```

Therefore this one finite boundary slice is rigorously strictly positive.
The result is not a certificate for adjacent parameter values and not a
sub-full or uniform theorem.  Monotonicity does imply positivity for every
`theta<=1` at this exact same finite matrix.

As an honesty check, asking the dual checker to prove the false unshifted
claim with `mu=0, delta=1/1000` fails at its first interval LDL pivot.  A
separately labeled calibration replacing `K_ar` by `K_ar-I` succeeds, with
minimum interval LDL pivot lower bound `0.4867011087`.  The shift is only a
mechanical test of the certificate machinery and carries no arithmetic claim.

## 6. What changed and what did not

Material gains from this iteration are:

1. The direct-q search now has an adversarial phase/height/depth/aperture/jet
   scanner rather than five centered examples.
2. The selected-null proof basis is exact-rational plus interval, removing the
   principal provenance gap in the floating fixture.
3. A proposed negative point can now be promoted to a rigorous finite theorem
   by one explicit dual inequality.
4. The closest sampled boundary point has itself been promoted to a rigorous
   finite positive statement.
5. Full-carrier monotonic pre-screening prunes unnecessary sub-full dual solves
   whenever that boundary scalar is already positive.

What did not change:

* No sampled sign controls an unbounded height range or a continuous parameter
  box.
* No uniform lower bound for `q_(theta*kappa)` has been proved.
* No theorem says an actual off-strip zero forces a negative direct-q value.
* No published or project zero-free bound has been numerically tightened.

The next fail-fast use of this machinery should move to substantially larger
heights with adaptive minimization of the full-carrier scalar, interval-replay
every near-zero candidate, and only then solve the more expensive sub-full dual
when the boundary screen is negative.  Analytically, the unresolved target is
still a uniform arithmetic mechanism; more finite positive samples cannot
replace it.
