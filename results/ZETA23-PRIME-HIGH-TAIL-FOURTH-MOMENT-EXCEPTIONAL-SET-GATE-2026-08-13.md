# Prime high-tail fourth-moment and exceptional-set gate

**Date:** 2026-08-13

**Verdict:** the remaining actual-prime antenna problem is still open, but
its high tail can be compressed much further than the second-moment audit
showed.  There is an explicit positive, diffuse prime-node quadrature which
has the required fixed-power accuracy on the low band and whose complete
high-band fourth moment is only `Y^o(1)`.  At the test exponent `.019`, all
frequencies at which this quadrature fails the desired sidelobe bound occupy
total length at most

```text
Y^(.076+o(1))
```

inside a legal aperture of length `Y^(50/33+o(1))`.  The part exceeding
twice the threshold lies in at most `Y^(.0855+o(1))` connected peak
components.  This is a genuine full-aperture theorem, not a computation.

The same fourth-moment argument gives a profile-free Christoffel obstruction:
an absolutely continuous high-band design of effective `L2` width `ell_2`
has principal cancellation cost at least

```text
ell_2^(1/4) Y^(-o(1)).
```

Thus every `L2`-diffuse design with
`ell_2 >= Y^(.0721212936+epsilon)` is already too expensive at the strip
threshold.  This strictly extends the fixed-profile result: no Fourier decay,
bounded variation, equilibrium shape, or density domination is assumed.

It does **not** give a uniform sidelobe bound.  The high cancellation measure
in the exact minimax problem is allowed to be atomic and can put all its mass
on the exceptional peaks.  Excluding, spanning, or correcting those peaks is
the remaining theorem.  Consequently this report proves neither the required
lower bound for `E_Y` nor a zero-free strip.

---

## 1. Direction audit: what kills the route and what helps the strip

Let

```text
a(t)=(cos(t*u_n))_(n in N_Y),
u_n=log(n/Y),
b(t)=integral_(-w)^w phi(u)cos(t*u)du,
phi(u)=(1-|u|/w)exp(alpha*u),
B=Y^(50/33+o(1)).                                      (1.1)
```

The continuous Wiener extremal is

```text
E_B=sup{|integral b dh| : integral a dh=0,
                         ||h||_TV<=1,
                         supp(h) subset [0,B]}.          (1.2)
```

Split `[0,B]=L union H`, with `L=[0,T]`, and define

```text
C_(L,H)=inf {||nu||+||mu|| :
             supp(nu) subset L, supp(mu) subset H,
             integral a d(nu+mu)=0,
             integral_L b dnu=1}.                        (1.3)
```

If `epsilon_T=sup_H |b|`, direct normalization gives

```text
1/C_(L,H)-epsilon_T <=E_B<=1/C_(L,H)+epsilon_T.          (1.4)
```

There are two opposite proof directions.

* A feasible low/high nulling measure of cost `C` proves a **lower** bound
  `E_B >=1/C-epsilon_T`.  A subpower-cost family would help the strip route.
* Coefficients `lambda_n` satisfying

  ```text
  sup_L |b(t)-P_lambda(t)|<=eta,
  sup_H |P_lambda(t)|<=epsilon,
  P_lambda(t)=sum_n lambda_n cos(t*u_n),                  (1.5)
  ```

  prove the dual lower bound

  ```text
  C_(L,H)>=1/max(eta,epsilon),                            (1.6)
  ```

  and the direct quotient upper bound

  ```text
  E_B<=max(eta,epsilon+epsilon_T).                        (1.7)
  ```

  A full-band exponent greater than
  `delta_*=.0180303234...` therefore **kills this sufficient strip route**;
  it does not prove a strip.

The proof of (1.6) is worth retaining because it prevents an orientation
error.  For every feasible `(nu,mu)`,

```text
1=|integral_L b dnu|
 <=eta||nu||+|integral_L P_lambda dnu|
 = eta||nu||+|integral_H P_lambda dmu|
 <=eta||nu||+epsilon||mu||.                              (1.8)
```

No positivity and no one-low-atom assumption occur here.

---

## 2. A diffuse coarse-cell quadrature on the actual primes

The BHP hat quadrature has excellent deterministic low-band accuracy, but its
largest coefficient can be as large as the maximal prime-log gap.  That is
too concentrated for a useful fourth-moment estimate.  Coarser cells give a
different quadrature whose individual weights are essentially `1/M`.

Fix

```text
tau=.01,       a=.03,       h_Y=Y^(-a),       T=Y^tau.   (2.1)
```

Partition `[-w,w]` into `K asyp Y^a` intervals `I` of comparable length
`h_Y`.  Let

```text
m_I=integral_I phi(u)du,
P_I={p prime : log(p/Y) in I},
N_I=#P_I.                                                (2.2)
```

The physical length of every cell is comparable with `Y^(1-a)=Y^.97`.
The classical Huxley prime-number theorem in short intervals (indeed, its
much weaker `7/12+epsilon` range suffices) gives, uniformly in these cells,

```text
N_I asyp_w Y*h_Y/log Y.                                  (2.3)
```

Define positive actual-prime weights

```text
lambda_p=m_I/N_I       for p in P_I,
lambda_n=0             for proper prime powers,
P_Y(t)=sum_p lambda_p cos(t*log(p/Y)).                    (2.4)
```

Then

```text
sum_p lambda_p=b(0)=O_(w,alpha)(1),
max_p lambda_p <<_(w,alpha) log Y/Y,
sum_p lambda_p^2 <<_(w,alpha) log Y/Y.                   (2.5)
```

### Theorem 2.1 (diffuse low-band antenna)

Uniformly for real `t`,

```text
|P_Y(t)-b(t)| <<_(w,alpha) |t|*Y^(-a).                   (2.6)
```

In particular,

```text
sup_(0<=t<=Y^.01)|P_Y(t)-b(t)| <<Y^(-.02).               (2.7)
```

#### Proof

For each cell choose any center `c_I`.  Both the prime probability measure
`N_I^(-1) sum_(p in P_I) delta_(log(p/Y))` and the probability measure
`m_I^(-1) phi(u)1_I(u)du` are supported in an interval of diameter
`O(h_Y)`.  Since `cos(tu)` is `|t|`-Lipschitz,

```text
|sum_(p in P_I)lambda_p cos(t*u_p)-m_I cos(t*c_I)|
 <=m_I |t|h_Y,

|integral_I phi(u)cos(tu)du-m_I cos(t*c_I)|
 <=m_I |t|h_Y.                                           (2.8)
```

Sum over `I`.  Equation (2.5) follows from (2.3),
`m_I<<h_Y`, and positivity.  QED.

The compact tent has a derivative of bounded variation and vanishes at both
endpoints, so

```text
|b(t)|<<_(w,alpha)(1+t^2)^(-1).                          (2.9)
```

Thus on `H=[Y^.01,B]`, `|b(t)|<<Y^(-.02)`.  Equations
(2.7) and (2.9) leave a margin over `delta_*`; only a uniform high-band
bound for `P_Y` is missing.

---

## 3. Exact fourth moment through the first unavailable conductor

The key point is that the aperture is longer than the one-prime conductor
`Y` but shorter than the two-prime conductor `Y^2`.

Let `P` be any set of primes in `[Y exp(-w),Y exp(w)]`, let

```text
F_lambda(t)=sum_(p in P)lambda_p exp(i*t*log(p/Y)),
S_2(lambda)=sum_p |lambda_p|^2.                            (3.1)
```

### Theorem 3.1 (prime-product fourth moment)

For every interval `J` of length `L`,

```text
integral_J |F_lambda(t)|^4 dt
 <<_w (L+Y^2) S_2(lambda)^2.                              (3.2)
```

The same estimate, with a `Y^o(1)` factor, holds for prime-power nodes.

#### Proof

Write

```text
F_lambda(t)^2
 =sum_r c_r exp(i*t*log(r/Y^2)),
c_r=sum_(pq=r)lambda_p lambda_q.                          (3.3)
```

Distinct integers `r` in the fixed window around `Y^2` have log frequencies
separated by `c_w/Y^2`.  The Montgomery--Vaughan mean-value/Hilbert
inequality therefore gives

```text
integral_J |F_lambda(t)^2|^2dt
 <<_w (L+Y^2)sum_r |c_r|^2.                               (3.4)
```

Unique factorization gives exactly

```text
sum_r |c_r|^2
 =sum_p |lambda_p|^4+4 sum_(p<q)|lambda_p lambda_q|^2
 =2 S_2(lambda)^2-sum_p |lambda_p|^4
 <=2 S_2(lambda)^2.                                      (3.5)
```

For prime powers, the multiplicity of a product representation is
`Y^o(1)` (only powers of the same underlying prime add a divisor-size
multiplicity), which proves the stated extension.  QED.

For the diffuse weights (2.4), (2.5), (3.2), and `B<Y^2` imply the complete
full-aperture estimate

```text
integral_0^B |P_Y(t)|^4dt
 <=integral_0^B |F_lambda(t)|^4dt
 <<Y^o(1).                                                (3.6)
```

This is the first useful multiplicative moment.  The second moment pays
`B/Y=Y^(17/33+o(1))`.  At the fourth moment, product-frequency separation
pays `Y^2`, which is exactly canceled by `S_2(lambda)^2=Y^(-2+o(1))`.
Higher moments also have total size `Y^o(1)` but give a worse exceptional-set
exponent.  Interpolation between the second and fourth moments is minimized
at the fourth endpoint for every threshold exponent below `17/66`.

---

## 4. Full-band exceptional-set compression

For `c>0`, put

```text
E_c(Y)={t in [Y^.01,B] : |P_Y(t)|>Y^(-c)}.              (4.1)
```

### Corollary 4.1 (exceptional length)

For every fixed `c>0`,

```text
|E_c(Y)|<=Y^(4c+o(1)).                                    (4.2)
```

This is immediate from (3.6) and Chebyshev.  At `c=.019`,

```text
|E_.019(Y)|<=Y^(.076+o(1)).                               (4.3)
```

Outside this set, the dual residual satisfies

```text
|b(t)-P_Y(t)|<=Y^(-.019)+O(Y^(-.02)).                    (4.4)
```

Together with (2.7), this is already stronger than the required exponent
everywhere except `E_.019(Y)`.

There is also a peak-count statement.  Positivity and (2.5) give

```text
sup_t |P_Y''(t)|<=w^2 sum_p lambda_p=O_(w,alpha)(1).       (4.5)
```

Every connected component of `E_c(Y)` which meets
`{|P_Y|>2Y^(-c)}` contains an interior extremum of fixed sign.  Taylor's
theorem and (4.5) put an interval of length `>>Y^(-c/2)` inside that
component.  Hence:

### Corollary 4.2 (large peak components)

The set

```text
{t in [Y^.01,B]: |P_Y(t)|>2Y^(-c)}                        (4.6)
```

is contained in at most

```text
Y^((9/2)c+o(1))                                           (4.7)
```

connected components of `E_c(Y)`, apart from two possible boundary
components.  At `c=.019`, this is `Y^(.0855+o(1))`.

This is a substantial dimensional reduction: the unresolved set has
power-small relative measure and fewer than `Y^.086` macroscopic peak
components, while the coefficient space has `Y^(1-o(1))` dimensions.
It is not yet a correction theorem because no lower singular-value bound is
known for the prime-node evaluation matrix on those adaptively selected
peaks.

---

## 5. A profile-free `L2` Christoffel obstruction

The fourth moment also strengthens the design-side obstruction.  For the
principal carrier, write

```text
q_0=a(0),
S_Y(t)=<q_0,a(t)>,
G_rho=integral a(t)a(t)^T d rho(t),
L_rho=q_0^T G_rho^dagger q_0.                              (5.1)
```

The prime-power extension of Theorem 3.1 and `M=Y^(1-o(1))` give

```text
integral_H |S_Y(t)|^4dt <<Y^(2+o(1))M^2.                  (5.2)
```

Suppose `rho` is absolutely continuous, `d rho=f(t)dt`, with
`f in L2` and `integral f=1`.  Holder and (5.2) give

```text
q_0^T G_rho q_0
 =integral |S_Y(t)|^2 f(t)dt
 <=Y^(1+o(1))M ||f||_2.                                  (5.3)
```

The metric Cauchy--Schwarz inequality gives

```text
L_rho*(q_0^T G_rho q_0)>=||q_0||^4=M^2.                  (5.4)
```

Consequently:

### Theorem 5.1 (`L2`-diffuse design obstruction)

Define the effective `L2` width

```text
ell_2(f)=||f||_2^(-2).                                    (5.5)
```

Then

```text
L_rho>=Y^(-o(1))||f||_2^(-1),
sqrt(L_rho)>=Y^(-o(1))*ell_2(f)^(1/4).                    (5.6)
```

In particular, if

```text
ell_2(f)>=Y^(4*delta_*+epsilon)
        =Y^(.0721212936+epsilon),                         (5.7)
```

then the principal high-band representation cost exceeds
`Y^(delta_*+epsilon/5)` for all sufficiently large `Y`.

No pointwise Fourier decay of `f` is assumed.  If an atomic probability
measure is convolved with any probability kernel of `L2` effective width
`ell`, Young's inequality gives `ell_2(f)>=ell`; therefore every smoothing
at scale `Y^(.0721212936+epsilon)` also crosses the obstruction.  A surviving
design must retain genuinely narrower or singular atoms.

The same proof applies uniformly to any fixed compact family of low atoms
`q=a(s)`: replace the coefficients `1` in (3.3) by `cos(su_n)`.  It does not
automatically apply to an arbitrary signed low measure, whose feature vector
can have small Euclidean norm despite normalized carrier.  The full
carrier-aware inequality remains open.

---

## 6. Why the suggested generic tools stop at the exceptional set

### 6.1 BHP mesh and Beurling--Selberg

The maximal mesh alone cannot control the high tail.  For an equally spaced
node set of mesh `h`, every coefficient vector satisfies the exact grating
identity

```text
P(2*pi/h)=exp(i*constant)*P(0).                            (6.1)
```

The BHP value `h=Y^(-19/40+o(1))` places this alias at
`Y^(19/40+o(1))`, exactly where the existing hat proof stops and well inside
the legal aperture.  Thus no theorem using only the maximal mesh can extend
the result.  Beurling--Selberg localization can construct primal witnesses
or average majorants, but an atomic optimizing measure can select the
uncontrolled peaks.

### 6.2 Pairwise large sieve

The second moment proves only that the rms sidelobe is at the square-root
scale.  It neither bounds the supremum nor controls an atomic design.  The
uniform lattice in (6.1) has rms size `M^(-1/2)` and unit grating lobes, an
exact counterexample to upgrading mean square to a supremum without
additional arithmetic input.

### 6.3 Turan--Nazarov and power sums

The generic exponential-polynomial Remez bound loses exponentially in the
number `M` of prime nodes.  Reversing it supplies only a lower sidelobe of
size `exp[-O(M)]`, far below every fixed power of `Y`.  Turan power sums do
not use the multiplicative coefficient profile and therefore do not remove
the atomic exceptional set.

### 6.4 Random discrepancy

For random coefficients `X_p` with prescribed means, concentration controls
only

```text
sum_p (X_p-E X_p) exp(i*t*u_p).                            (6.2)
```

The deterministic mean

```text
sum_p (E X_p) exp(i*t*u_p)                                (6.3)
```

is precisely the prime antenna that must be bounded.  Conditioning random
signs to retain the low carrier recreates this mean term.  Salem--Zygmund or
vector-balancing estimates can flatten the centered fluctuation, but do not
cancel (6.3) without a new target-dependent discrepancy theorem.

### 6.5 Additive energy

Unique factorization is genuinely useful once: it proves Theorem 3.1 and
compresses the bad set to (4.2).  The aperture is still below `Y^2`, so the
fourth moment pays the whole two-prime conductor.  Higher product moments
give exceptional lengths `Y^(2kc+o(1))`, worse than `Y^(4c+o(1))` for
`k>2`.  Additive energy alone does not say that an atomic measure cannot
span the carrier using the remaining peaks.

---

## 7. Exact surviving theorem and hostile decision

The full route would be closed by either one of the following.

1. **Exceptional-peak removal.**  Modify the diffuse coefficients (2.4),
   while retaining the low error `Y^(-.019+o(1))`, so that every component
   in Corollary 4.2 is also below `Y^(-.019+o(1))` and no new component is
   created.
2. **Exceptional-span obstruction.**  Prove that the actual prime-log atoms
   on the set (4.1) cannot represent any carrier-rich low feature vector
   with total variation below `Y^(.0180303234+o(1))`.

The first is a lower-singular-value/interpolation theorem for at most
`Y^(.0855+o(1))` adaptive peak components.  The second is the same fact in
the exact Christoffel dual language.  Neither follows from the measure bound
alone.

The present truth boundary is therefore

```text
diffuse actual-prime low quadrature                   PROVED;
low error exponent .020                              PROVED;
complete high-band fourth moment Y^o(1)              PROVED;
bad-set length Y^(.076+o(1)) at threshold .019       PROVED;
large-peak component count Y^(.0855+o(1))            PROVED;
all L2-diffuse designs beyond width Y^.072121...     POWER-OBSTRUCTED;
atomic exceptional-peak span                         OPEN;
full C_(L,H)>=Y^.0180303234                           NOT PROVED;
full E_Y<=Y^(-c), c>.0180303234                       NOT PROVED;
required E_Y lower bound for the strip                NOT PROVED;
uniform zero-free strip                               NOT PROVED.       (7.1)
```

The inequality directions in the last three lines are deliberately
different.  A full dual upper bound would refute this strip mechanism; it
would not by itself establish the requested strip.

---

## 8. References and reproduction

The only short-interval input used in Section 2 is far inside the classical
range.  One may cite M. N. Huxley, *On the difference between consecutive
primes*, Invent. Math. **15** (1972), 164--170,
doi:`10.1007/BF01418933`, or the later elementary-identity treatment in
D. R. Heath-Brown, *Prime numbers in short intervals and a generalized
Vaughan identity*, Canad. J. Math. **34** (1982), 1365--1377,
doi:`10.4153/CJM-1982-095-9`.

The symbolic exponent and product-energy ledger is checked by

```bash
python3 results/verify_prime_high_tail_fourth_moment_ledger.py
```

That script checks exact rational exponent inequalities and the convolution
identity (3.5).  It is a replay of the algebra, not a substitute for the
asymptotic proof.
