# R97 fermionic Fredholm determinant and trace-anomaly gate

Status: exact Schatten-class Euler determinant calculus, fermionic Fock
realization, Hilbert--Schmidt recurrence theorem, nonclosability of the
ordinary trace, index obstruction, and prime-minus-continuum relative-trace
audit.  Hilbert--Schmidt regularization extends through `Re(s)=1` but removes
the entire first-prime trace.  That removed trace is exactly where the zero
at `s=1` and all zeta singularities live.  Restoring it in a fixed strip is
equivalent to controlling the signed prime--continuum discrepancy there.
No fixed zero-free strip and no failure of every fixed strip is proved.

Date: 2026-08-07.

## 1. Verdict

Let

```text
H=ell^2({primes}),
D_s=diag_p(p^(-s)).                                        (1.1)
```

For `Re(s)>1`, the Euler product is the Fredholm determinant

```text
det(I-D_s)=product_p(1-p^(-s))=1/zeta(s).                 (1.2)
```

The operator becomes Hilbert--Schmidt already for `Re(s)>1/2`.  This looks
like a route to a fixed half-plane, but the exact regularized formula is

```text
det_2(I-D_s)
 =product_p(1-p^(-s))exp(p^(-s)),                         (1.3)

1/zeta(s)=det_2(I-D_s)exp(-Tr D_s),       Re(s)>1.        (1.4)
```

The two factors have completely different behavior.

```text
det_2(I-D_s)       holomorphic and nonzero for Re(s)>1/2;
exp(-Tr D_s)       defined by the prime trace only for Re(s)>1.             (1.5)
```

As `s->1+`, the regularized determinant tends to a finite nonzero value,
while

```text
exp(-Tr D_s)=exp(-sum_p p^(-s))asymp s-1.                (1.6)
```

Thus the zero of `1/zeta` at `s=1` is entirely a **trace anomaly**.  The
same first trace carries the logarithmic singularities associated with the
zeta zeros.  Hilbert--Schmidt regularization has not controlled them; it has
deleted them.

The fermionic formulation says the same thing geometrically.  The
squarefree Euler vector

```text
v_s=sum_(n squarefree)mu(n)n^(-s)e_n                      (1.7)
```

is a perfectly nonzero Hilbert vector for `Re(s)>1/2`, including at `s=1`.
The scalar augmentation `sum a_n`, which turns it into `1/zeta(s)`, is an
unbounded functional.  Finite Euler vectors converge in norm at `s=1`
while their augmentations tend to zero.

There are four exact no-go statements.

1. Any continuous holomorphic Hilbert--Schmidt determinant that agrees
   with (1.2) in `Re(s)>1` must retain the zero at one.  Hilbert--Schmidt
   vertical recurrence then forces recurrent translated zeros.  Since
   `1/zeta` has no zeros away from the unique pole of zeta at one, such a
   determinant cannot exist.
2. The trace on trace-class operators is not closable as a functional on
   Hilbert--Schmidt space.  A closed-graph completion cannot restore the
   missing coordinate without adding independent trace data.
3. `I-D_s` is invertible and null-homotopic for every `Re(s)>0`; its Fredholm
   index is identically zero.  No determinant zero or spectral flow can
   occur in the operator itself.
4. Pairing the prime trace with a continuous pole trace breaks the almost
   periodic recurrence, but ordinary positive operator traces cannot
   subtract the two measures.  A signed relative trace is precisely the
   prime-number discrepancy.  Trace-class control in a fixed left
   half-plane is a fixed-power PNT theorem; Hilbert--Schmidt relative
   control again removes the first-order discrepancy.

The operator route therefore identifies a useful obstruction but no new
strip.  A survivor would require a genuinely new *signed relative trace
theorem* for the actual prime-minus-continuum pair.  That is another exact
form of the R94--R96 queue, not a free determinant or index argument.

## 2. Schatten thresholds and regularized determinants

For `q>0`,

```text
||D_s||_(S_q)^q=sum_p p^(-q Re(s)).                       (2.1)
```

The prime sum converges exactly when

```text
q Re(s)>1.                                                 (2.2)
```

Consequently

```text
D_s in S_1      iff Re(s)>1,
D_s in S_2      iff Re(s)>1/2.                            (2.3)
```

Moreover

```text
||D_s||=2^(-Re(s))<1,             Re(s)>0.                (2.4)
```

Thus `I-D_s` is boundedly invertible throughout the positive half-plane.

For `D_s in S_2`, the second regularized determinant is

```text
det_2(I-D_s)=det[(I-D_s)exp(D_s)].                        (2.5)
```

Its absolutely convergent logarithm is

```text
log det_2(I-D_s)
 =-sum_p sum_(k>=2)p^(-ks)/k,        Re(s)>1/2.            (2.6)
```

Every factor in (1.3) is nonzero, and (2.6) is locally normally convergent.
Therefore

**Theorem 2.1.**

```text
det_2(I-D_s) is holomorphic and nonzero in Re(s)>1/2.      (2.7)
```

For `Re(s)>1`, separate the missing `k=1` term:

```text
log det(I-D_s)
 =log det_2(I-D_s)-sum_p p^(-s),                          (2.8)
```

which is (1.4).

At `s=1`,

```text
det_2(I-D_1)
 =product_p(1-1/p)exp(1/p) in (0,infinity),               (2.9)
```

because `log[(1-x)exp(x)]=O(x^2)`.  In contrast, Euler's divergence of
`sum_p 1/p` gives

```text
exp(-sum_p p^(-s))->0,             s->1+.                 (2.10)
```

The sharper first-order behavior in (1.6) follows from the classical
singularity of the prime zeta function.

Higher regularization makes the information loss more explicit.  For an
integer `m>=2`, `D_s in S_m` when `Re(s)>1/m`, and

```text
log det_m(I-D_s)
 =-sum_p sum_(k>=m)p^(-ks)/k.                             (2.11)
```

The determinant extends farther left by deleting more low-order prime
traces.  Since `I-D_s` remains invertible, every `det_m` is nonzero in its
domain.  Extending the topology and retaining the unregularized Euler
determinant are opposing operations.

## 3. Where the zeta divisor went

Let

```text
P(s)=sum_p p^(-s),               Re(s)>1.                 (3.1)
```

Then

```text
log zeta(s)=sum_(k>=1)P(ks)/k,                            (3.2)

log det_2(I-D_s)=-sum_(k>=2)P(ks)/k.                      (3.3)
```

The second expression is holomorphic in `Re(s)>1/2`.  The entire difference
between `-log zeta` and (3.3) is `-P(s)`.

Möbius inversion gives the familiar continuation formula

```text
P(s)=sum_(k>=1)mu(k)log zeta(ks)/k                        (3.4)
```

where branches are chosen in a zero-free starting region.  Formula (3.4)
shows why the missing trace is not an elementary counterterm.  It has
logarithmic singularities at

```text
s=rho/k                                                   (3.5)
```

and at the rescaled pole locations.  In particular, in `Re(s)>1/2` the
`k=1` term carries the original zeta divisor while (3.3) is regular.

Exponentiating a continued branch of `-P(s)` would restore (1.4), but a
single-valued holomorphic branch across a proposed half-plane exists only
after the corresponding zeta zeros have been excluded.  The trace
counterterm is the zero-free problem, not a known regularization constant.

## 4. Fermionic Fock space keeps the vector and loses the sum

Let

```text
F_-=direct_sum_(k>=0) exterior^k H                        (4.1)
```

be fermionic Fock space.  Its standard orthonormal basis is indexed by
finite prime sets, equivalently by squarefree integers.  Define

```text
v_s
 =sum_(S finite)(-1)^|S| product_(p in S)p^(-s)e_S
 =sum_(n squarefree)mu(n)n^(-s)e_n.                       (4.2)
```

Its norm is

```text
||v_s||^2
 =sum_(n squarefree)n^(-2 Re(s))
 =product_p(1+p^(-2 Re(s)))
 =zeta(2 Re(s))/zeta(4 Re(s)).                            (4.3)
```

Hence `v_s` exists and depends holomorphically on `s` throughout
`Re(s)>1/2`.  Its vacuum coordinate is one, so

```text
v_s!=0                                                     (4.4)
```

everywhere in that domain.

The scalar Euler series is the formal augmentation

```text
Aug(v_s)=sum_(n squarefree)mu(n)n^(-s)=1/zeta(s).          (4.5)
```

But

```text
Aug((a_n))=sum_n a_n                                      (4.6)
```

is not a bounded functional on `ell^2`.  For example, the vector having
its first `N` coordinates equal to `N^(-1/2)` has norm one and augmentation
`sqrt(N)`.

This failure is visible exactly at `s=1`.  Let `v_(1;X)` retain only primes
`p<=X`.  Then

```text
v_(1;X)->v_1                  in Fock norm,                (4.7)

Aug(v_(1;X))=product_(p<=X)(1-1/p)->0.                    (4.8)
```

The limiting vector is nonzero, by (4.3)--(4.4).  The zero occurs only
after applying the discontinuous augmentation.

The operator supertrace is the same phenomenon.  Fermionic second
quantization gives

```text
Gamma(D_s)e_S=product_(p in S)p^(-s)e_S,                  (4.9)

Str Gamma(D_s)=det(I-D_s)=1/zeta(s),      Re(s)>1.        (4.10)
```

`Gamma(D_s)` is Hilbert--Schmidt for `Re(s)>1/2`, but its supertrace is
defined continuously only in trace norm, again requiring `Re(s)>1`.

There is no hidden Hilbert factorization.  If one splits the scalar sum as
a bounded inner product with weights of real exponents `alpha` and
`s-alpha`, square summability requires

```text
Re(alpha)>1/2,
Re(s-alpha)>1/2,                                          (4.11)
```

and therefore `Re(s)>1`.  Moving weights from one Fock vector to the other
does not cross the Euler line.

## 5. Hilbert--Schmidt recurrence forces forbidden determinant zeros

The map

```text
s -> D_s                                                     (5.1)
```

is holomorphic with values in `S_2` for `Re(s)>1/2`.  It is also uniformly
recurrent under vertical translation on every compact subset.

**Lemma 5.1 (Hilbert--Schmidt recurrence).**  Let `K` be compact in
`Re(s)>1/2`.  There are `tau_j->infinity` such that

```text
sup_(s in K)||D_(s+i tau_j)-D_s||_(S_2)->0.               (5.2)
```

### Proof

If `sigma_0=min_(s in K)Re(s)>1/2`, then

```text
||D_(s+i tau)-D_s||_(S_2)^2
 =sum_p p^(-2 Re(s))abs(exp(-i tau log p)-1)^2.            (5.3)
```

Choose a finite prime cutoff so the tail, uniformly in `s`, is arbitrarily
small.  Simultaneous recurrence of the finitely many phases
`tau log p` modulo `2pi` makes the remaining finite sum arbitrarily small
along an unbounded sequence.  QED.

This proves a stronger impossibility than the loss seen in (2.9).

**Theorem 5.2 (no continuous Hilbert--Schmidt Euler determinant).**  There
is no holomorphic functional `Phi`, continuous in Hilbert--Schmidt topology
on a neighborhood of the curve `{D_s:Re(s)>1/2}`, such that

```text
Phi(D_s)=det(I-D_s)=1/zeta(s),          Re(s)>1.           (5.4)
```

### Proof

Put

```text
f(s)=Phi(D_s).                                              (5.5)
```

Since `D_s->D_1` in `S_2` as `s->1+`, continuity and (5.4) give

```text
f(1)=0.                                                     (5.6)
```

The zero is simple because (5.4) holds to the right and `1/zeta(s)` has a
simple zero at one.

Lemma 5.1 and continuity of `Phi` imply uniform recurrence

```text
f(s+i tau_j)->f(s)                                         (5.7)
```

on a small closed disk around one.  To justify the uniformity, note that
the image of the disk under `s -> D_s` is compact.  If uniform continuity
along this compact image failed, there would be `X_j` on the image and
`Y_j-X_j -> 0` in `S_2` for which
`abs(Phi(Y_j)-Phi(X_j))` stayed bounded away from zero.  A convergent
subsequence of `X_j`, followed by continuity of `Phi`, gives a
contradiction.  Rouche's theorem then puts a zero of `f` in every
sufficiently large translated disk.

On the other hand, the meromorphic identity

```text
f(s)zeta(s)=1                                             (5.8)
```

holds first in `Re(s)>1` and hence throughout the connected half-plane by
analytic continuation; at `s=1`, the zero in (5.6) cancels the unique pole
of zeta.  Equation (5.8) forbids every translated zero of `f`, since zeta
has no pole there.  This contradicts Rouche.  QED.

This is the exact recurrence alternative requested by the operator route:

```text
retain the zero at s=1 in S_2 topology
       => recurrent high zeros of the determinant
       => contradiction;

use det_2 to avoid the contradiction
       => the zero at s=1 is removed.                      (5.9)
```

## 6. The trace has no closed graph in Hilbert--Schmidt space

One might try to adjoin the ordinary trace as an unbounded but closed
functional on `S_2`.  It is not closable.

**Theorem 6.1 (trace nonclosability).**  The functional

```text
Tr:S_1 subset S_2 -> C                                    (6.1)
```

is not closable in the `S_2` norm.

### Proof

Let `A_N` be diagonal of rank `N`, with all nonzero diagonal entries equal
to `1/N`.  Then

```text
||A_N||_(S_2)=N^(-1/2)->0,
Tr A_N=1.                                                  (6.2)
```

Thus the graph contains a sequence converging to `(0,1)`, while it also
contains `(0,0)`.  No closed extension can be single-valued.  QED.

The example uses positive diagonal operators, so positivity or restriction
to a commutative diagonal algebra does not repair the problem.

The graph norm

```text
||A||_(S_2)+abs(Tr A)                                     (6.3)
```

can of course be completed, but its limit contains an independent trace
coordinate not determined by the Hilbert--Schmidt operator.  Vertical
recurrence of `D_s` in `S_2` says nothing about this added coordinate.  For
the prime diagonal, specifying it is precisely specifying a renormalized
prime trace `P(s)`.

Using `S_1` itself restores trace continuity, but (2.3) then excludes
`D_1` and every point to its left.  The two desired properties cannot be
obtained from one ordinary Schatten topology.

## 7. Index and determinant topology are trivial here

For every `Re(s)>0`, (2.4) gives the explicit inverse

```text
(I-D_s)^(-1)=sum_(m>=0)D_s^m.                             (7.1)
```

The path

```text
t -> I-tD_s,                    0<=t<=1,                  (7.2)
```

stays invertible.  Hence `I-D_s` is null-homotopic in the invertible group
and

```text
index(I-D_s)=0.                                           (7.3)
```

Every regularized determinant zero for an operator `I+K`, `K in S_m`,
detects noninvertibility.  Since noninvertibility never occurs here,
`det_m(I-D_s)` cannot encode the zeta zeros or the pole at one.

The same objection applies to a proposed spectral flow: there is no
eigenvalue crossing through zero in the positive half-plane.  An index of a
Toeplitz or boundary operator could be nontrivial only after a symbol
involving the continued zeta function is inserted.  Verifying that the
symbol is nonzero on the boundary would then be the desired zero-free
theorem, not a consequence of the diagonal Euler operator.

## 8. Prime-minus-continuum pairing

The trace anomaly suggests subtracting a continuous pole trace before
regularizing.  At logarithmic level the relevant prime-power determinant
measure is

```text
dPi(u)=sum_(p,k>=1)(1/k)delta_(k log p)(du),               (8.1)
```

because

```text
log zeta(s)=integral_0^infinity exp(-su)dPi(u).            (8.2)
```

The logarithmic pole has the continuous model

```text
dC(u)=1_(u>=u_0) exp(u)du/u.                              (8.3)
```

Indeed, up to a function entire near `s=1`,

```text
-integral_(u_0)^infinity exp(-(s-1)u)du/u=log(s-1).       (8.4)
```

Therefore the signed relative trace

```text
integral exp(-su)d(Pi-C)(u)                              (8.5)
```

is, up to an explicit analytic correction,

```text
log[(s-1)zeta(s)].                                        (8.6)
```

This pairing has two real advantages:

* the singularity at one cancels;
* the continuum spectrum destroys the high-frequency almost-periodic
  recurrence of the prime diagonal.

But it is not an ordinary positive operator trace.  A positive trace on a
direct sum of atomic and continuous algebras **adds** their masses.  The
minus sign in `Pi-C` is an externally imposed signed trace.  Standard
Fredholm positivity, Fuglede--Kadison determinant, and index theorems do not
apply to that difference.

The analytic obstruction is exact.  A single-valued holomorphic choice of
(8.6) on a simply connected half-plane exists if and only if

```text
(s-1)zeta(s)!=0                                           (8.7)
```

there.  Thus a holomorphic signed relative determinant in a fixed strip is
already the fixed zero-free theorem.

There is a norm version of the same boundary.  Suppose, in the most
favorable version of the proposal, that prime locations can be paired with
continuum quantiles so that the resulting relative perturbation is
Hilbert--Schmidt in a left half-plane.  This is the operator analogue of
the finite phase-aware `L2` transports considered in R94; it is a granted
hypothesis here, not a new matching theorem.  A second-order relative
determinant then deletes

```text
Tr(A_s-C_s),                                               (8.8)
```

the first signed prime--continuum discrepancy.  Recovering the ordinary
relative determinant requires (8.8) to exist as a trace.  In cumulative
form, convergence of that trace in `Re(s)>a` is a power-saving prime number
theorem with exponent `a`, up to the standard endpoint losses.

The pairing has therefore moved the anomaly from

```text
Tr D_s=sum_p p^(-s)                                       (8.9)
```

to

```text
Tr(A_s-C_s)=prime trace-continuum trace.                  (8.10)
```

It has not bounded it.

There is also a compactness obstruction to a literal continuum diagonal.
Multiplication by a nonzero function on a nonatomic `L2` space is not a
compact operator.  Ordinary Fredholm determinants do not apply.  Passing to
a semifinite von Neumann determinant produces a positive real modulus and
again cannot implement the signed subtraction in (8.5) without an external
relative-trace choice.

## 9. Relative Hilbert--Schmidt pairing still loses first order

The preceding conclusion can be formulated abstractly.  Suppose `A_s` and
`C_s` are bounded operators such that

```text
I-A_s and I-C_s are invertible,
(I-A_s)(I-C_s)^(-1)-I in S_2.                             (9.1)
```

Then the relative second determinant

```text
det_2((I-A_s)(I-C_s)^(-1))                                (9.2)
```

is well-defined and nonzero.  Its logarithm begins at quadratic order in
the relative perturbation.  The linear term needed for the ordinary
relative determinant is the trace in (8.8).

If the relative perturbation is only Hilbert--Schmidt, Theorem 6.1 prevents
that trace from being recovered continuously.  If it is trace class in a
fixed strip, its trace Laplace transform supplies exactly the signed
prime--continuum cancellation that the repository is seeking.  There is no
intermediate determinant/index theorem which creates the linear estimate
from quadratic membership.

This also explains why a Hilbert--Schmidt matching can look very strong
numerically.  Squaring a local prime-location error changes the convergence
threshold, while the determinant regularization simultaneously removes the
unsquared first moment.  Zeta's divisor lives in the removed moment.

## 10. Bottom line

The exterior/Fock construction is exact and useful as a reality check:

```text
squarefree Euler vector in Fock space          exists for Re(s)>1/2
Hilbert--Schmidt prime diagonal                exists for Re(s)>1/2
regularized determinant det_2                  nonzero there
ordinary Euler scalar/supertrace               requires Re(s)>1
zero at s=1                                    entirely first-trace anomaly
zeta-zero singularities                        entirely first-trace anomaly
Fredholm index of I-D_s                        identically zero
closed Hilbert--Schmidt trace                   impossible
prime-minus-continuum signed trace              fixed-strip-equivalent.     (10.1)
```

Hilbert--Schmidt recurrence does produce a theorem: any continuous
determinant which retained the zero at one would acquire forbidden recurrent
zeros.  The actual regularized determinant avoids the contradiction by
discarding that zero.

No fixed strip and no proof that zeros approach one follows.  A viable
operator revival must establish a new trace-class or one-sided signed-trace
estimate for the actual prime-minus-continuum pair.  Merely placing the pair
in Hilbert--Schmidt class, invoking a regularized determinant, taking a Fock
norm, or computing an index cannot recover the missing first-order
cancellation.
