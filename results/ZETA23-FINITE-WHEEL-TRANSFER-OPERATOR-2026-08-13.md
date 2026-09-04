# Finite-wheel transfer operator and uniform growing-wheel theorem

**Date:** 2026-08-13  
**Status:** exact finite-wheel/renewal theorem; exact full-period Eratosthenes
stage theorem; local actual-prime transfer remains open.

## Verdict

The earlier fixed-auxiliary-wheel estimate

```text
A_np(Pq;r)=O_P(q^-1)
```

admits a stronger result with no dependence on `P` at all.  Let `q` be prime,
`(P,q)=1`, and independently retain every unit modulo `Pq` with probability
`0<p<=1`.  Give each retained point its symmetrized one-dimensional Voronoi
cell mass and normalize by physical length.  For every `r` not divisible by
`q`, the nonprincipal additive mode satisfies

```text
|A_np(P,q,p;r)| <= 1/(q-1).                           (0.1)
```

This is exact for every finite `P`, even when `P=P(Y)` grows arbitrarily.  It
does not need `pq -> infinity`.  In the Zeta23 shell `q>=Y^.1537`, (0.1) has
saving exponent `.1537`, exceeding even the hostile carrier requirement
`kappa_max=.01974048` by

```text
.1537-.01974048=.13395952.                            (0.2)
```

The proof is not a delicate matrix estimate.  Couple the `Pq` process to the
`P` process and delete the marked centers divisible by `q`.  Before deletion,
`P`-periodicity puts exactly `1/q` of the expected Voronoi mass in every
residue modulo `q`.  Deleting centers can only enlarge the cells of every
surviving center.  Thus the final masses have the exact form

```text
m_0=0,
m_a=1/q+delta_a       (a=1,...,q-1),
delta_a>=0,
sum_(a!=0) delta_a=1/q.                              (0.3)
```

Equation (0.1) follows by one triangle inequality.  The sparse transfer
operator and exact rational checker independently reproduce (0.3).

This resolves **growing auxiliary wheels in the stationary/full-period
model**.  It does not resolve localization to a single physical block near
`Y`: the primorial period is exponentially larger than that block.  The
new local gate is a second moment for gaps in the polynomially rough sequence,
stated precisely in Section 7.

No zero-free strip is claimed here.

---

## 1. Exact sparse renewal operator

Let

```text
W=Pq,
U_W={u_0<...<u_(m-1)} subset (0,W],
d_i=u_(i+1)-u_i,                                    (1.1)
```

with cyclic lifting `u_m=u_0+W`.  Independently mark each candidate with
probability `p` and put `z=1-p`.  Conditional on a mark at candidate `i`, its
next marked candidate occurs `k` candidate steps later with probability

```text
p z^(k-1),       k>=1.                               (1.2)
```

On the finite candidate-index space, let `S` be cyclic forward shift.  The
dense successor kernel is exactly

```text
K=p S(I-zS)^(-1).                                    (1.3)
```

Its entries are

```text
K_(ij)=p z^(k(i,j)-1)/(1-z^m),                       (1.4)
```

where `k(i,j)` is the unique integer in `{1,...,m}` congruent to `j-i`
modulo `m`.  Every row sums exactly to one.

The dense matrix never has to be formed.  The conditional expected physical
distances to the right and left are the exact cyclic resolvents

```text
F_i=sum_(h>=0) z^h d_(i+h),
B_i=sum_(h>=0) z^h d_(i-h-1),                        (1.5)

F_i=d_i+zF_(i+1),
B_(i+1)=d_i+zB_i.                                    (1.6)
```

Thus two cyclic bidiagonal systems compute the answer in `O(phi(Pq))`
arithmetic operations.  The normalized expected Voronoi mass at `u_i` is

```text
s_i=p(F_i+B_i)/(2W).                                 (1.7)
```

Because `sum_i d_i=W`, summing either resolvent gives

```text
sum_i F_i=sum_i B_i=W/p,
sum_i s_i=1.                                         (1.8)
```

All formulas (1.4)--(1.8) are implemented over `fractions.Fraction`.  The
checker compares (1.5) against an independent exact summation obtained by
writing `k=h+am`; it does not compare one floating implementation against
another.

### Candidate-index spectrum

For `xi_l=exp(2 pi i l/m)`, (1.3) has eigenvalue

```text
lambda_l=p xi_l/(1-z xi_l).                          (1.9)
```

This diagonalizes renewal in candidate-index frequency.  The physical mode
`e_q(r u_i)` is generally not one candidate-index eigenvector; the exact tool
therefore keeps the physical gaps and phases separate rather than silently
identifying the two spectra.

---

## 2. Uniform growing-`P` theorem

### Theorem 2.1 (finite-wheel deletion coupling)

Let `q` be prime, `(P,q)=1`, and `0<p<=1`.  On the infinite periodic set

```text
C_P={n in Z:(n,P)=1},                                (2.1)
```

place independent Bernoulli-`p` marks.  Let `nu_P` be the expected
one-dimensional Voronoi mass measure, normalized on one interval of length
`Pq`.  Delete every marked center divisible by `q`; the retained process is
exactly Bernoulli-`p` marking on

```text
C_(Pq)={n in Z:(n,Pq)=1}.                            (2.2)
```

If `m_a` is its expected normalized cell mass at centers congruent to `a`
modulo `q`, then (0.3) holds.

#### Proof

The law of the base process is `P`-periodic.  Fix one unit residue `c` modulo
`P`.  Its `q` occurrences

```text
c, c+P, ..., c+(q-1)P                               (2.3)
```

in a `Pq` period have the same expected unnormalized cell mass.  Since `P` is
invertible modulo `q`, (2.3) visits every residue modulo `q` once.  Summing
over all unit residues `c mod P`, each `q`-residue therefore receives exactly
the same base mass.  The total normalized mass is one, so that mass is
exactly `1/q`.

Use the same Bernoulli marks in the two processes.  Passing from `C_P` to
`C_(Pq)` removes precisely marked centers with residue zero modulo `q`.  In
one dimension, removing centers from a Voronoi diagram can only move each
surviving cell boundary outward.  Therefore the aggregate mass at every
surviving residue `a!=0` cannot decrease.  Write its increase as
`delta_a>=0`.  No residue-zero center survives.  Conservation of total mass
then gives

```text
sum_(a!=0) delta_a
 =1-(q-1)/q
 =1/q.                                               (2.4)
```

This proves (0.3).  The infinite process almost surely has marked points in
both directions, so no finite-circle empty-configuration convention is
needed.  QED.

### Corollary 2.2 (uniform nonprincipal additive mode)

Put `omega=exp(2 pi i r/q)`, `q` not dividing `r`.  The full additive mode is

```text
A(r)=sum_(a=1)^(q-1) m_a omega^a
    =-1/q+sum_(a=1)^(q-1) delta_a omega^a.           (2.5)
```

In the multiplicative-character expansion, the principal character has
Gauss sum `-1`; because total mass is one, its contribution is
`-1/(q-1)`.  Hence

```text
A_np(r)=A(r)+1/(q-1)
       =1/[q(q-1)]+sum_(a=1)^(q-1)delta_a omega^a.   (2.6)
```

Equations (2.4) and (2.6) give the exact rational disk certificate

```text
center =1/[q(q-1)],
radius =1/q,
|A_np(r)|<=1/[q(q-1)]+1/q=1/(q-1).                  (2.7)
```

The result is simultaneous in every numerator `r`, every finite `P`, and
every `p`.  In particular, there is no hidden `O_P(1)` constant.

---

## 3. Relation to the exact Eratosthenes deletion charge

For an ordered active set `S` and data `f`, define its trapezoid

```text
T(S;f)=1/2 sum_(x<y consecutive in S)(y-x)(f(x)+f(y)). (3.1)
```

If an interior center `x` with neighbor gaps

```text
A=x-l,       B=r-x                                  (3.2)
```

is deleted, the exact update is

```text
Delta_x T
 =1/2[B f(l)+A f(r)-(A+B)f(x)].                      (3.3)
```

For `f(n)=e_q(rn)` this is

```text
Delta_x T
 =e_q(rx)/2 [B e_q(-rA)+A e_q(rB)-(A+B)].           (3.4)
```

Take `P` to be the product of the sieve primes preceding `q`, use a cyclic
period `Pq`, and apply the `q`-stage deletion.  Every deleted center has
`q|x`, and the base `P`-wheel mode is exactly zero by `P`-periodicity.  The
sum of (3.4) over the entire stage is therefore the final `Pq`-wheel mode.
Equations (2.4)--(2.5) give the raw normalized stage bound

```text
|A(r)| <= 2/q.                                        (3.5a)
```

After subtracting the multiplicative-principal contribution, Corollary 2.2
gives the sharper `|A_np(r)|<=1/(q-1)`.  Thus `1/(q-1)` is a bound for the
principal-subtracted target, not literally for the raw deletion-stage sum.
Both statements have the same `q^-1` saving exponent.

This is a genuine per-sieve-stage result.  It does **not** assert that each
charge (3.4) is contractive or has a favorable sign.  The contraction comes
from global mass transport: the stage redistributes exactly the base
residue-zero mass `1/q` among the surviving residues.

For `p=1`, this statement is deterministic and is an exact theorem about the
full Eratosthenes wheel, not a random-model assertion.  For `p<1`, it is the
stationary renewal extension.

### 3.1 Every sequential stage below `q` is exactly zero

Fix the target Fourier modulus `q`.  Let

```text
P_j=product_(ell<=p_j) ell,       p_j<q.              (3.5)
```

At every pre-`q` Eratosthenes stage, both the candidate set before deleting
multiples of `p_j` and the candidate set afterwards are periodic with periods
coprime to `q`.  Extend both to the common cyclic period `qP_j`.  The argument
from Theorem 2.1 before any residue-zero deletion applies separately to both
sets: each physical `q`-residue has exactly mass `1/q`.  Therefore

```text
full q-mode before stage p_j =0,
full q-mode after stage p_j  =0,
full stage-p_j q-charge      =0.                     (3.6)
```

Thus the pre-`q` stages do not merely cancel after their charges are added;
each stage has zero aggregate target mode on its own full common period.  The
same statement holds if the sieve primes other than `q` are reordered: their
combined wheel is some `P` coprime to `q`, and `q` may be deleted last.

The first nonzero full-period raw target charge is the `q` stage itself.  Its
raw mode is bounded by (3.5a), and its principal-subtracted mode by (2.7).
Later coprime stages can be placed into `P` before this last deletion, so the
growing-`P` theorem already includes them at full-period level.

### 3.2 Exact interval truncation is a prefix coboundary

Full-period cancellation localizes to an exact identity, but not to an
automatic small bound.  Let `mu=(mu_0,...,mu_(q-1))` be the vector-valued
periodic Voronoi mass measure for any wheel of physical period `L` divisible
by `q`, and let

```text
M=mu((0,L]),
H(x)=mu((0,x])-(x/L)M,       0<=x<=L.                (3.7)
```

Extend `H` periodically.  Direct subtraction gives, for every pair of integer
endpoints,

```text
mu((A,B])-((B-A)/L)M = H(B)-H(A).                   (3.8)
```

This is the exact boundary discrepancy requested by the sequential deletion
picture.  Taking a nonzero additive `q`-mode gives

```text
mu_hat_r((A,B])
 -(B-A)/L mu_hat_r((0,L])
 =H_hat_r(B)-H_hat_r(A).                             (3.9)
```

For a pre-`q` stage, the period mean on the left is zero by (3.6), so the
entire local stage charge is an endpoint coboundary.  At the `q` stage, the
mean is `O(1/q)` by (2.7), and the only additional term is the same endpoint
coboundary.

The implementation stores `H` formally as a vector of rational `q`-residue
coefficients.  If

```text
D(P,q,p)=sup_(0<=x<=Pq) sum_a |H_a(x)|,              (3.10)
```

then every additive numerator satisfies the rigorous interval estimate

```text
|boundary error|<=2D(P,q,p).                         (3.11)
```

Because `H` is piecewise affine and its coefficient `l1` norm is convex
between atoms, evaluating the two one-sided values at every wheel site gives
the exact rational maximum in (3.10).  No complex interval rounding is
needed.

For a smooth shell weight `w`, Stieltjes integration by parts yields the
corresponding exact weighted identity

```text
integral w dmu_hat_r
 =mu_hat_r((0,L])/L integral w dx
  -integral H_hat_r(x) w'(x) dx                     (3.12)
```

up to the displayed endpoint convention.  Hence a sufficient localization
condition on a `Y`-scale tent is

```text
D(P,q,p)/Y <<Y^(-kappa-epsilon).                     (3.13)
```

The trivial full-period estimate gives `D=O(Pq)`, useful only while
`Pq<<Y^(1-kappa)`.  A sequential primorial crosses that range quickly.  This
pinpoints the failure: the exact coboundary exists, but the full-period theorem
does not bound its prefix norm once the wheel period exceeds the shell.

### 3.3 Simultaneous deletion gives a local positive transport identity

There is a second exact localization identity which avoids the order-dependent
gaps in (3.3).  Let `B` be any locally finite active set and `D subset B` the
centers to be deleted simultaneously.  Let `nu_B` and `nu_(B\D)` be their
atomic Voronoi cell-mass measures.  Every physical point initially assigned
to a surviving center remains assigned to that center after deletion; only
points initially assigned to a center in `D` can move.  Consequently

```text
nu_(B\D)-nu_B = eta_D - nu_B|_D,                     (3.14)
eta_D>=0,
eta_D(R)=nu_B(D)                                     (3.15)
```

on a finite cyclic period (and componentwise on the line).  Thus

```text
||nu_(B\D)-nu_B||_TV=2 nu_B(D).                      (3.16)
```

This is the order-free form of the entire deletion-charge sum.  In
particular, for every phase `|f|=1`,

```text
|integral f d(nu_(B\D)-nu_B)|<=2 nu_B(D).            (3.17)
```

If the pre-deletion neighboring gaps at `x in D` are `g^-(x),g^+(x)`, then

```text
nu_B(D)=1/2 sum_(x in D)[g^-(x)+g^+(x)].             (3.18)
```

This identity is important for the rough-gap gate below: it uses the gaps of
the one fixed **pre-deletion** sequence.  It does not make the invalid move of
bounding sequential deletion charges by gaps which have already merged.
For a compact shell one must include the components meeting the shell (or an
endpoint collar); that is ordinary boundary bookkeeping, not a change to
(3.14).

---

## 4. Additive and character spectral modes

Let

```text
C(chi)=sum_(a=1)^(q-1) m_a chi(a),
tau_r(bar chi)=sum_(b=1)^(q-1) bar(chi(b)) e_q(rb).  (4.1)
```

Multiplicative Fourier inversion gives the exact identity

```text
A(r)=1/(q-1) sum_chi tau_r(bar chi) C(chi).           (4.2)
```

The implementation constructs every multiplicative character from a
primitive root, computes (4.1), and verifies (4.2) against the direct additive
mode.  This numerical evaluation is a diagnostic of the spectral wiring.
The inequality (2.7) itself does not depend on floating roots of unity: its
center, radius, nonnegativity, and normalization are all exact rational
checks.

Theorem 2.1 controls the **whole nonprincipal bank after recombination at one
additive numerator**.  It does not give an equally strong bound on every
individual `C(chi)`; the positive excess measure may have large character
coefficients of total size `1/q`, which is still exactly what (2.7) can
afford.

---

## 5. Growing-wheel behavior and sharpness

The proof never estimates candidate gaps, the Jacobsthal function, or
`phi(P)/P`.  It remains valid when:

```text
P is squarefree or not;
P contains arbitrarily many auxiliary primes;
P grows faster than every power of q;
p tends to zero at any rate;
pq is bounded or unbounded.                           (5.1)
```

The `q^-1` exponent cannot be improved from mass transport alone.  The
deleted base sector contains exactly mass `1/q`; absent further information,
that mass can be redistributed with nearly aligned phase.  Thus (2.7) is the
right uniform conclusion of positivity and periodicity.

For concrete wheels the mode is often much smaller.  Those extra gains come
from the distribution of the `delta_a`, not from a stronger universal mass
ledger, and the selected numerator cannot be assumed generic.

---

## 6. What this does and does not prove

```text
exact finite candidate transition kernel:             PROVED
linear-time sparse cyclic resolvent:                   PROVED
stationary mass normalization:                        PROVED
additive/character diagonalization:                   PROVED
uniform all-finite-P O(q^-1) model bound:              PROVED
uniform full-period deterministic raw q-stage <=2/q:   PROVED
principal-subtracted q-stage <=1/(q-1):                 PROVED
each pre-q full-period stage mode equals zero:          PROVED
exact interval prefix-coboundary identity:              PROVED
single Y-block localization:                           OPEN
actual consecutive-prime selected mode:                OPEN
zero-free strip:                                       NOT PROVED
```

The distinction between full-period and local is essential.  If
`P=prod_(p<q)p`, then `log P~q`; for `q=Y^b` its period is exponentially
larger than the physical block of length comparable with `Y`.  A full-period
identity therefore permits a short block to carry an atypical share of the
redistributed mass.

---

## 7. The local rough-gap moment gate

The deletion formula suggests a concrete localization theorem.  Just before
the sieve stage `q`, let `R_<q` denote integers having no prime factor below
`q`.  For consecutive points `n<n^+` of this sequence intersecting `[Y,2Y]`,
put

```text
g_q(n)=n^+-n,
G_2(Y;q)=sum g_q(n)^2.                               (7.1)
```

Let `N_q(Y)` count the points deleted at stage `q`, namely multiples of `q`
which survived all earlier stages.  The standard upper-sieve scale is

```text
N_q(Y) << Y/(q log q) * q^o(1).                      (7.2)
```

Apply the simultaneous transport identity (3.14) to the `q`-multiples in the
pre-`q` rough sequence.  By (3.18), Cauchy--Schwarz and
`(a+b)^2<=2(a^2+b^2)` give

```text
nu_(R_<q)(D_q)
 <=[N_q(Y) G_2(Y;q)]^(1/2)                           (7.3)
```

up to an absolute constant and the two shell boundary gaps.  Indeed each
rough gap is incident to at most two deleted centers.  Equation (3.17)
therefore gives

```text
(1/Y)|stage-q local charge|
 << [N_q(Y) G_2(Y;q)]^(1/2)/Y.                       (7.4)
```

Consequently the uniform moment

```text
G_2(Y;q) << Y q^o(1),                                (7.5)
```

together with (7.2), would give

```text
(1/Y)|stage-q local charge|
 << q^(-1/2+o(1)),                                   (7.6)
```

which has exponent at least `.07685` at `q>=Y^.1537`, comfortably beyond the
carrier bill.  This is a cleaner target than asking directly for cancellation
in (3.4): it uses only an unsigned gap moment in the denser rough sequence.

The scope of this reduction is exactly the simultaneous **stage-`q` charge**.
It does not bound the localized mode of the pre-`q` rough sequence, nor the
sum of the later SPF deletion stages.  A proof of the final prime mode still
requires separate bounds for those two terms (or one direct estimate of their
sum), as well as the physical-to-logarithmic weighted transfer.

### Fail-fast literature audit and post-audit closure

No theorem located states (7.5) verbatim for
`q=Y^b`, `.1537<=b<=.25`, on every prescribed `Y`-block.  However, a
subsequent parameter audit found that the lower-sieve component of
Matomaki's published short-interval argument *implies the needed estimate*
through the range used by the denominator construction.  More precisely,
for any fixed

```text
.1537<=b<=.160,   z=Y^b,
```

Matomaki's vector lower minorant at linear level `Y^(1/3)`, her raw Lemma
5.4, and Iwaniec's `J(z)<<z^2` bound give

```text
G_2(Y;z) << Y (log Y)^2.                             (7.5a)
```

The derivation, including the well-factorable split, every Type-II exponent,
and the empty-start layer-cake argument, is audited in
[`ZETA23-ROUGH-GAP-LOWER-SIEVE-HOSTILE-AUDIT-2026-08-13.md`](ZETA23-ROUGH-GAP-LOWER-SIEVE-HOSTILE-AUDIT-2026-08-13.md).
Thus the local unsigned rough-gap gate is closed with `rho=0`; it remains
scoped exactly as stated above to a simultaneous deletion charge.

For a target prime `q>=z`, reorder the exact deletion telescope so that the
primes below `z` are deleted first, `q` is deleted next, and all other primes
are deleted afterwards.  The pre-`q` set in (7.3) is then the denser
`z`-rough set, so (7.5a) bounds the resonant `q`-stage for every such `q`.
This reordering does not bound the initial localized `z`-rough mode or the
aggregate post-`q` deletion tail.

The observations below explain why the direct rough-indicator variance
literature did not itself state (7.5a), and why that absence is not a no-go
theorem.

Ofir Gorodetsky proves exact asymptotics for the variance of rough numbers in
short intervals, but the parameter condition is

```text
(1+a) log H/loglog H
 <=(1-epsilon) log Y/log q,
a=loglog H/log q.                                    (7.7)
```

For `q=Y^b`, the right side of (7.7) is the fixed constant `O(1/b)`, while
the left side diverges already for ordinary growing interval lengths such as
`H=log Y`.  That theorem therefore does not reach the polynomial roughness
regime needed by (7.5).  The paper itself emphasizes that rough-number
variance becomes prime-like as the cutoff grows and records the connection
between prime variance and strong pair correlation.

Gafni--Tao prove that almost every prime gap contains a number rough at the
scale of that gap, using fixed and higher moments.  Their theorem controls a
different adaptive cutoff and exceptional prime-gap count.  It does not state
the uniform consecutive-gap second moment (7.5) for a preassigned polynomial
cutoff `q=Y^b`.

The small-sieve fundamental lemma can force a rough number in sufficiently
long intervals once the available sieve level is beyond the parity threshold,
but that supplies only a much larger maximum-gap scale and does not imply the
near-linear total second moment (7.5).

Thus (7.5) is not supplied by the periodic operator or by the cited
rough-indicator variance theorem.  It is nevertheless a corollary of the
structured lower-sieve variance estimate just described.  Its
almost-all-in-translation input is sufficient here because Chebyshev is
integrated over *all empty starts* and the exact layer-cake identity converts
that measure bound into the global consecutive-gap moment on each prescribed
shell; no favorable-shell subsequence is selected.

---

## 8. Reproducibility

Implementation:

```text
src/finite_wheel_transfer_operator.py
```

Unit tests:

```text
pytest -q src/test_finite_wheel_transfer_operator.py
```

Standalone exact checker:

```text
python3 results/verify_zeta23_finite_wheel_transfer_operator.py
```

Expected output:

```text
finite-wheel sparse resolvent identities: PASS
exact rational deletion-coupling certificates: PASS
uniform growing-P bound: |A_np| <= 1/(q-1)
target exponent margin: beta-kappa_max = 0.13395952
additive/character diagonalization: PASS
sequential pre-q zero modes and prefix coboundary: PASS
scope: full-period/renewal wheel; local actual-prime transfer OPEN
```

The unit suite checks the sparse systems against an independently grouped
infinite renewal series, verifies stochastic transition rows exactly, tests
`P=1,2,6,30,210,1024`, audits both `p=1` and rational `p<1`, and checks the
character reconstruction.

## Primary sources used for the localization audit

- Ofir Gorodetsky, [*The variance of integers without small prime factors in
  short intervals*](https://doi.org/10.1007/s00209-024-03601-w), especially
  Theorem 1.1 and Corollary 1.2.
- Ayla Gafni and Terence Tao, [*Rough numbers between consecutive
  primes*](https://arxiv.org/abs/2508.06463), especially Lemmas 2.1 and 3.1
  and Theorem 1.1.

The transfer-operator identities and Theorem 2.1 are derived here; they are
not attributed to those papers.
