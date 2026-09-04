# The actual Lanczos cubic scan never enters its informative branch

Status: branch-specific actual-coefficient execution, rigorous shifted
control, exact cubic-closure theorem, and a new spectral-floor/variance
admission lemma, 2026-08-12.  No actual negative full-carrier point was
found.  No uniform cubic sign, arithmetic admission theorem, zero-free
strip, or improved zeta-zero bound is proved.

## 1. Binary verdict

The proposed implication

```text
m_1=<a,Ka><0   ==>   m_3=<a,K^3a>>=0               (1.1)
```

was not falsified by the actual coefficients, but it was also **never
tested on its informative branch**.

Two new deterministic scans evaluated 253,302 target-conditioned completed
matrices/vectors.  Every matrix retained the actual von Mangoldt prime
powers, the pole matrix, and the archimedean matrix.  Their exact branch
counts were

```text
actual points with m_1<0:                         0;
actual points with m_1<0 and m_3<0:               0;
actual points with m_1<0 and theta_*<8/9:          0.   (1.2)
```

The zeros in the second and third lines are vacuous consequences of the
first.  Positive values of `m_3` at points with `m_1>=0` are not evidence for
(1.1), and this report does not present them as such.

A continuous differential-evolution attack on the closest newly identified
cell made another 6,784 evaluations.  It stopped at

```text
T=19, half-count=2, jet order=2,
grid center=24.010178811482195,
phase=-0.4787171374367561,
alpha=0.49999999898761205,

m_1=+2.046022171352036e-4.                           (1.3)
```

This is only a floating local minimum and has no continuous-box or uniform
meaning.  Its role is negative: a targeted between-grid optimizer still did
not produce an Arb replay candidate on the `m_1<0` branch.

The shifted control behaves in the opposite way.  At the previously
interval-rebuilt `T=16` point, replacing `K_ar` by `K_ar-I` gives

```text
m_1=-0.9956802468797483,
m_3=-0.9874341973818850,
theta_*=0                                             (floating).       (1.4)
```

More importantly, the existing 128-bit Arb `LDL*` certificate proves on the
entire selected quotient

```text
K_ar-I <= -10^(-3) I.                                (1.5)
```

Functional calculus therefore proves rigorously, for its unit carrier,

```text
m_1<=-10^(-3),          m_3<=-10^(-9).              (1.6)
```

This is a structural calibration only.  It changes the arithmetic operator
and makes no claim about zeta.  It proves that the implementation and moment
criterion do recognize a negative-`m_1`, negative-`m_3`, failed-admission
branch when one is present.

The exact disposition is

```text
actual finite counterexample to (1.1):             NOT FOUND;
actual finite evidence for (1.1):                  NONE (branch empty);
rigorous shifted negative control:                 PROVED;
uniform whole-space cubic positivity shortcut:    IMPOSSIBLE/TAUTOLOGICAL;
restricted carrier variance escape:               PROVED BELOW.       (1.7)
```

## 2. Reproducible branch scan

The implementation is

```text
src/lanczos_m3_branch_gate.py
src/test_lanczos_m3_branch_gate.py
```

For a grid with endpoint projection `Q`, let `x,y` be the selected positive
and negative rows and put

```text
P=Q-(Qx)(Qx)^*/||Qx||^2,
a=Py/||Py||.                                         (2.1)
```

The code evaluates the compressed powers without a new floating nullspace:

```text
v=P*K*a,
m_1=<a,v>,          m_2=||v||^2,
m_3=<v,Kv>.                                           (2.2)
```

Since `v` lies in `range P`, the last expression is exactly
`<a,(PKP)^3a>`.  The implementation reproduces the established centered
fixture moments through `m_3`.

### 2.1 Low and moderate heights

The first scan used

```text
T in {11,12,13,14,15,16,19,24,32,48,64,96,128},
half-count in {2,3,4,6,8} whenever the grid fitted,
11 equally spaced legal grid centers,
phase in {-1/2,-3/8,-1/4,-1/8,0,1/8,1/4,3/8,1/2},
alpha in {10^-6,.05,.15,.25,.35,.45,.499999},
every admissible endpoint-jet order.                  (2.3)
```

It comprised 440 arithmetic bases and 217,602 conditioned carrier points.
There were no `m_1<0` points.  The minimum sampled `m_1` was positive,
`0.0035946893`; this number is an audit marker, not evidence for a theorem.

### 2.2 Larger heights

The second scan used

```text
T in {192,256,384,512,768,1024},
half-count in {2,4,8,16},
7 legal grid centers,
phase in {-1/2,-1/4,0,1/4,1/2},
alpha in {10^-6,.05,.25,.45,.499999},
jet order 0,...,10.                                  (2.4)
```

It comprised 168 bases and 35,700 carrier points.  Again there were no
`m_1<0` points.  These trials are additional to the earlier 61,896-point
full-carrier adversarial scan, but overlapping parameter geometries are not
being counted as independent evidence.

### 2.3 Adaptive cell attack

The cell in (1.3) was selected by a prior integer-height/critical-coordinate
scout.  The adaptive routine then minimized jointly over the legal grid
center, phase, and `0<alpha<1/2`, with fixed discrete data `(T,n,m)=(19,2,2)`.
It converged successfully after 6,784 function evaluations.  Because no
interval subdivision of the continuous parameter box was performed, (1.3)
does not prove positivity between evaluations.

Reproduction of the deterministic default scan and shifted control:

```bash
PYTHONPATH=src python3 src/lanczos_m3_branch_gate.py
PYTHONPATH=src python3 -m pytest -q src/test_lanczos_m3_branch_gate.py
```

The adaptive run is exposed as
`adaptive_minimum_m1(height=19,half_count=2,jet_order=2)`.

## 3. Why a whole-space cubic theorem is not a shortcut

### Theorem 3.1 (cubic closure)

For every finite-dimensional Hermitian operator `K`,

```text
K^3>=0    iff    K>=0.                                (3.1)
```

Equivalently, the implication

```text
<u,Ku><0  ==>  <u,K^3u>>=0                           (3.2)
```

holds for **every** unit vector `u` if and only if `K>=0`.

#### Proof

The eigenvalues of `K^3` are the cubes of the real eigenvalues of `K`, so
they have exactly the same signs.  If (3.2) held while `K` had a negative
eigenvalue `lambda` with unit eigenvector `u`, then its two sides would be
`lambda<0` and `lambda^3<0`, a contradiction.  Conversely, when `K>=0` the
antecedent in (3.2) never occurs.  QED

Thus proving `m_3>=0` on the whole selected quotient, or even proving the
conditional sign for every vector there, is exactly the original lower-edge
problem.  The eight-ninths theorem survives only because it asks for (1.1)
on the much smaller, geometry-defined family of target carrier directions.

## 4. A sum-of-squares escape from the cubic correlation

There is, however, a new exact way to replace the cubic sign by a quadratic
residual lower bound.

### Theorem 4.1 (spectral-floor/variance Lanczos admission)

Let `K=K*` satisfy

```text
K>=-M*I,                 M>=0,                       (4.1)
```

and let `a` be a unit carrier with

```text
m_1=<a,Ka>=-r<0,
m_2=<a,K^2a>.                                       (4.2)
```

Fix `0<theta<1`.  If

```text
m_2 >= max {r*M, r^2/(1-theta)},                    (4.3)
```

then the first Lanczos plane `span{a,Ka}` contains a unit vector `z` with

```text
|<a,z>|^2>=theta,           <z,Kz>>=0.              (4.4)
```

In particular, at `theta=8/9` it is sufficient that

```text
m_2 >= max {r*M, 9*r^2}.                            (4.5)
```

#### Proof

Since `K` commutes with its functional calculus, (4.1) gives the exact
sum-of-squares identity

```text
m_3+M*m_2
 =<Ka,(K+M*I)Ka>
 =||(K+M*I)^(1/2)Ka||^2 >=0.                        (4.6)
```

For `m_1=-r`, the shifted-Hankel reversal from the Lanczos theorem satisfies

```text
Delta_H=m_2^2-m_1*m_3
        =m_2^2+r*m_3
       >=m_2*(m_2-r*M).                             (4.7)
```

The first condition in (4.3) therefore gives `Delta_H>=0`.  Moreover

```text
sigma^2=m_2-r^2
 >=r^2*theta/(1-theta).                             (4.8)
```

The smallest nonnegative Lanczos slope is

```text
s_0=r/(sigma+sqrt(Delta_H)/sigma)<=r/sigma
    <=sqrt((1-theta)/theta).                        (4.9)
```

Hence its carrier fraction `1/(1+s_0^2)` is at least `theta`, proving
(4.4).  QED

### Corollary 4.2 (negative quasimode alternative)

Under (4.1)--(4.2), failure of carrier-`theta` Lanczos admission forces

```text
m_2 < max {r*M, r^2/(1-theta)}.                     (4.10)
```

In particular, failure to find any nonnegative vector in a nondegenerate
first Lanczos plane forces

```text
m_2<r*M.                                             (4.11)
```

Thus a hostile negative carrier cannot be arbitrary.  It must be an
approximate negative eigenstate at the geometric-mean scale:

```text
||(K+r*I)a||^2=m_2-r^2 < r*(M-r).                   (4.12)
```

The inequalities are sharp at the level of general spectral measures.
They do not follow merely from nonzero Lanczos variance.

## 5. Arithmetic consequence

The completed lower-edge estimate currently available has scale

```text
M_T=O(sqrt(X)/L^(13/10)+1/L),                       (5.1)
```

whereas a fixed-depth hostile carrier would have

```text
r asymp kappa=X^alpha/L,       alpha<1/2.           (5.2)
```

Consequently

```text
M_T/r asymp X^(1/2-alpha)/L^(3/10) -> infinity.     (5.3)
```

Theorem 4.1 does not make this loss disappear.  It turns it into one exact
quadratic, sum-of-squares target:

```text
||K a||^2=m_2 >= r*M_T,                             (5.4)
```

together with the much smaller carrier-retention condition in (4.3).  In
variance language, the target is

```text
||(K+rI)a||^2 >= r*(M_T-r).                         (5.5)
```

Separate upper bounds on prime words cannot prove a lower bound such as
(5.4).  But (5.4) is materially different from the cubic sign: it is the
norm square of the completed arithmetic residual.  If its typical root-scale
size is present, then `m_2` is much larger than `r*M_T` and admission follows;
failure requires cancellation so strong that the target carrier becomes an
approximate negative eigenvector of the complete prime--pole--gamma matrix.

This gives the next precise analytic target:

> Use the confluent-Loewner displacement identity and the explicit Cauchy
> geometry of the target carrier to exclude a negative quasimode satisfying
> (4.12), or prove the residual lower bound (5.5) directly from the actual
> completed coefficients.

That target uses only a quadratic actual-prime correlation and an exact
sum-of-squares.  It is not proved here.  The finite scans cannot test it on
the decisive branch because no actual sampled carrier has `m_1<0`.
