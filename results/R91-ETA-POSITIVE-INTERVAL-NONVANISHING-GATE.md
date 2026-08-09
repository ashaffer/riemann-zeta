# R91 eta positive-interval nonvanishing gate

Status: exact positive Mellin/Laplace representations, a sharp monotone
nonvanishing theorem, an explicit order-two total-positivity failure, a
regular-smoothing no-go theorem, and positive as well as general normally
convergent scalar-multiplier recurrence obstructions.  The two-modulus vector removes the individual
eta-factor zeros, but its common-zero problem is exactly the zeta-zero
problem.  This route does not prove a fixed zero-free strip, and it does not
prove that no such strip exists.

Date: 2026-08-07.

## 1. Verdict

There is a genuinely attractive positive representation.  If

```text
E = union_(n>=1) [2n-1,2n],
B_2(u) = 1_E(exp(u)),
```

then, absolutely for `Re(s)>0`,

```text
eta(s)/s
  = integral_E x^(-s-1) dx
  = integral_0^infinity B_2(u)e^(-su) du.             (1.1)
```

The hoped-for implication

```text
positive deterministic interval geometry
       => zero-free Laplace transform
```

fails at the first exact check.  The transform in (1.1) has the explicit
zeros

```text
s = 1 + 2 pi i k/log(2),       k in Z\{0},            (1.2)
```

coming from

```text
eta(s) = (1-2^(1-s))zeta(s).                            (1.3)
```

Thus scalar eta nonvanishing cannot possibly prove any half-plane reaching
left of `Re(s)=1`.  These are not zeta zeros; they are zeros of the
positive-interval encoding.

The natural repair is useful but ultimately diagnostic.  For every integer
`q>=2`, put

```text
E_q(s) = (1-q^(1-s))zeta(s),
A_q(x) = floor(x)-q floor(x/q) = floor(x) mod q.       (1.4)
```

Then `A_q(x)` takes values in `{0,...,q-1}` and

```text
E_q(s)/s = integral_0^infinity A_q(exp(u))e^(-su)du,
                                                        Re(s)>0.       (1.5)
```

The factors for `q=2` and `q=3` have no common zero except their formal
zero at `s=1`, where the zeta pole cancels them and
`E_q(1)=log(q)`.  Consequently

```text
E_2(s)=E_3(s)=0, Re(s)>0
       if and only if
zeta(s)=0.                                             (1.6)
```

So the pair of positive transforms is an exact vector encoding of the
zeta-zero problem.

It is not an automatic improvement.  Every fixed positive scalarization

```text
c_2 E_2(s)+c_3 E_3(s),       c_2,c_3>0,                (1.7)
```

has new artificial zeros with real parts tending to `1` from the left.
The same is true for every finite or countable positive combination over
integer `q` which has enough moment to be analytic in a fixed left
neighborhood of `1`.  This is proved in Section 6 by recurrence of discrete
logarithmic frequencies.  Hence positive averaging over moduli cannot
convert the vector problem into a scalar zero-free transform.

The exact surviving target is a **joint signed estimate** proving that the
two transforms in (1.5) cannot vanish simultaneously.  Positivity of each
coordinate, total positivity, ordinary smoothing, fixed positive
scalarization, and log-scale renewal do not supply that estimate.

## 2. Exact positive representations

For `Re(s)>0`, pairing consecutive terms gives

```text
sum_(n>=1) integral_(2n-1)^(2n) x^(-s-1) dx
 = (1/s)sum_(n>=1)((2n-1)^(-s)-(2n)^(-s))
 = eta(s)/s.                                          (2.1)
```

The paired integral series is absolutely convergent: its `n`-th absolute
value is `O_s(n^(-Re(s)-1))`.  The change of variables `x=e^u` gives
(1.1), with no continuation or boundary term hidden in the calculation.

There is a wider family.  In `Re(s)>1`,

```text
E_q(s)
 = sum_(n>=1) (1-q 1_(q|n)) n^(-s).                  (2.2)
```

The partial sum of the coefficient sequence is exactly

```text
sum_(n<=x)(1-q 1_(q|n))
 = floor(x)-q floor(x/q)
 = A_q(x).                                            (2.3)
```

Abel summation therefore gives

```text
E_q(s)=s integral_1^infinity A_q(x)x^(-s-1)dx.        (2.4)
```

Because `0<=A_q(x)<=q-1`, the integral is holomorphic throughout
`Re(s)>0`.  Identity (2.4), first proved in `Re(s)>1`, continues there.
Changing variables gives (1.5).

For `q=2`, `A_2` is exactly the alternating unit-interval indicator in
(1.1).  For general `q`, it is the nonnegative periodic staircase

```text
0,1,...,q-1,0,1,...,q-1,...                           (2.5)
```

on consecutive unit intervals in the `x` variable.  It is important that
this periodicity is in `x`, not in `u=log x`: its log-frequency becomes
exponentially faster with `u`.

## 3. A real sufficient theorem: decreasing Laplace densities

There is a clean positivity theorem close to the hoped-for argument.

**Theorem 3.1 (monotone Laplace nonvanishing).**  Let
`C:[0,infinity)->[0,infinity)` be nonincreasing, locally bounded, and not
zero almost everywhere.  Then

```text
C_hat(s)=integral_0^infinity C(u)e^(-su)du != 0
                                                        for Re(s)>0.  (3.1)
```

### Proof

Let `ell=lim_(u->infinity) C(u)>=0` and let `nu=-dC` be the positive
Stieltjes measure of its drops.  Up to immaterial endpoint conventions,

```text
C(u)=ell+nu((u,infinity)).                             (3.2)
```

Tonelli's theorem first on real `s>0`, followed by analytic continuation
inside the absolutely convergent half-plane, gives

```text
s C_hat(s)
 = ell + integral_[0,infinity) (1-e^(-sv))dnu(v).     (3.3)
```

If `s=sigma+it` with `sigma>0`, then for every `v>0`,

```text
Re(1-e^(-sv)) = 1-e^(-sigma v)cos(tv) > 0.            (3.4)
```

The real part of (3.3) is therefore strictly positive, unless `C` is zero
almost everywhere.  Thus `s C_hat(s)` and `C_hat(s)` are nonzero.  QED.

A completely monotone density gives an even more familiar special case.
If

```text
C(u)=integral_[0,infinity) e^(-lambda u)dmu(lambda),
```

then

```text
C_hat(s)=integral_[0,infinity) dmu(lambda)/(s+lambda), (3.5)
```

whose real part is positive in `Re(s)>0`.

Theorem 3.1 is an exact sufficient mechanism of the requested kind.  The
rest of the report records why neither `B_2` nor a zero-preserving regular
smoothing of it can meet its hypothesis.

## 4. Total positivity fails before any subtle analytic issue

The function `B_2` drops from `1` to `0` at `u=log 2` and rises from `0`
to `1` at `u=log 3`; it is not monotone.  More strongly, its Toeplitz
kernel fails total nonnegativity already at order two.

Put

```text
x = log(3/2),
y = log(7/2),
m = (x+y)/2,
h = (y-x)/2.                                          (4.1)
```

Then `e^x=3/2` and `e^y=7/2` lie in occupied alternating intervals, while
`e^m=sqrt(21)/2` lies in the gap `(2,3)`.  Hence

```text
B_2(x)=B_2(y)=1,       B_2(m)=0.                      (4.2)
```

Using rows `m<y` and columns `0<h`, the order-two Toeplitz minor is

```text
det [[B_2(m),   B_2(m-h)],
     [B_2(y),   B_2(y-h)]]

 = det [[B_2(m),B_2(x)],
        [B_2(y),B_2(m)]]
 = -1.                                                (4.3)
```

Thus `B_2` is not even `PF_2`, much less a Pólya-frequency function of all
orders.  There is no variation-diminishing theorem available directly from
its translation kernel.  This agrees with Schoenberg's classical
Fourier--Laplace classification of Pólya-frequency convolution kernels:
their transforms have a reciprocal Laguerre--Pólya form in their strip of
convergence, whereas (1.1) has the explicit zero lattice (1.2).

The historical classification is recorded in I. J. Schoenberg,
[On totally positive functions, Laplace integrals and entire functions of
the Laguerre--Pólya--Schur type](https://pmc.ncbi.nlm.nih.gov/articles/PMC1078971/),
and the variation-diminishing formulation in
[On Pólya frequency functions II](https://acta.bibl.u-szeged.hu/13626/).
The determinant (4.3), not the classification, is enough for the present
fail-fast conclusion.

## 5. Regular convolution cannot repair monotonicity while preserving zeros

Consider any causal convolution

```text
C=B_2*K                                                   (5.1)
```

for which the Laplace transform `K_hat(s)` is finite at the points (1.2)
and the ordinary convolution theorem is valid there.  Then

```text
C_hat(s)=eta(s)K_hat(s)/s.                              (5.2)
```

At every `s_k=1+2 pi i k/log 2`, `k!=0`, the right side vanishes.  By
Theorem 3.1, `C` therefore cannot be a nonzero nonnegative nonincreasing
function.  The same argument excludes a completely monotone output and,
under the usual integrability hypotheses, a Pólya-frequency output whose
Laplace transform is zero-free in its convergence strip.

This obstruction does not depend on `K` being positive.  A signed regular
smoothing also preserves the zero lattice.  To remove (1.2), its multiplier
must have poles there, so it is not a regular smoothing transform in that
half-plane.  Those poles are exactly what appears when one divides by
`1-2^(1-s)`.

There is also a simple boundary check for positive causal kernels.  Unless
`K` has an atom at zero, `B_2*K` starts from zero and initially increases,
so it cannot be nonincreasing.  Adding an atom avoids this elementary
endpoint defect but not the transform obstruction (5.2).

This identifies the precise invalid step in a tempting proof:

```text
smooth B_2 until it is monotone
  + invoke monotone-transform nonvanishing
  + divide away the harmless smoothing multiplier.   (5.3)
```

No regular multiplier can make the middle line true, because it would have
to erase actual eta-factor zeros.

## 6. Two moduli remove common fake zeros; scalarization adds them back

Let

```text
f_q(s)=1-q^(1-s),       E_q(s)=f_q(s)zeta(s).          (6.1)
```

If a complex number other than `s=1` is a common zero of `f_2` and `f_3`,
then for nonzero integers `k,l`,

```text
k/log(2)=l/log(3),
```

which would imply `3^k=2^l`.  This is impossible.  At `s=1`,

```text
lim_(s->1) E_q(s)=log(q),                              (6.2)
```

so neither `E_q` vanishes.  This proves the exact common-zero statement
(1.6).

One might now take a fixed positive combination so that the inverse
Laplace density remains nonnegative.  For `c_2,c_3>0`, however,

```text
c_2 E_2(s)+c_3 E_3(s)
 = P(s)zeta(s),

P(s)=c_2+c_3-c_2 2^(1-s)-c_3 3^(1-s).                (6.3)
```

The following theorem shows that this reintroduces artificial zeros
arbitrarily close to the desired boundary.

**Theorem 6.1 (discrete positive scalarizations have recurrent zeros).**
Let `(q_j)` be a finite or countable family of integers at least `2`, and
let `c_j>0`.  Suppose that for some `eta_0>0`,

```text
sum_j c_j q_j^(eta_0) < infinity.                     (6.4)
```

Set

```text
C=sum_j c_j,
P(s)=sum_j c_j(1-q_j^(1-s)).                          (6.5)
```

Then `P` has zeros `s_n` with `abs(Im(s_n))->infinity` and

```text
Re(s_n) <= 1,             Re(s_n) -> 1.               (6.6)
```

If the numbers `log(q_j)` lie in one common real lattice, `P` already has
nonzero zeros on `Re(s)=1`.  Otherwise one can choose the recurrent zeros
with `Re(s_n)<1`.

### Proof

Normalize `p_j=c_j/C` and write `s=1+z`.  Then

```text
P(1+z)/C = g(z)=1-phi(z),
phi(z)=sum_j p_j exp(-z log(q_j)).                    (6.7)
```

The moment condition makes `phi` holomorphic in `Re(z)>-eta_0`.  Moreover,

```text
g(0)=0,
g'(0)=sum_j p_j log(q_j)>0,                           (6.8)
```

so zero is simple.

Simultaneous Diophantine approximation gives a sequence `tau_n->infinity`
such that

```text
exp(-i tau_n log(q_j)) -> 1                           (6.9)
```

for every fixed `j`.  This recurrence is uniform after truncating to any
finite set of indices.  For any fixed disc `abs(z)<=r<eta_0`, the tail is
uniformly bounded by

```text
sum_(j>J) p_j q_j^r,                                  (6.10)
```

which tends to zero by (6.4).  Hence

```text
g(z+i tau_n) -> g(z)                                  (6.11)
```

uniformly on a small circle about zero.  Choose that circle to contain no
other zero of `g`.  Rouché's theorem gives a zero `w_n` of
`g(z+i tau_n)` with `w_n->0`.  Therefore

```text
z_n=i tau_n+w_n                                      (6.12)
```

is a zero of `g`, with `Re(z_n)->0`.

There are no zeros in `Re(z)>0`, since there

```text
abs(phi(z)) <= sum_j p_j q_j^(-Re(z)) < 1.            (6.13)
```

On `Re(z)=0`, equality `phi(it)=1` in the convex triangle inequality
requires `exp(-it log(q_j))=1` for every `j`.  This is exactly the common
lattice case.  In the nonlattice case every nonzero recurrent zero lies in
`Re(z)<0`.  Translating back by `s=1+z` proves (6.6).  QED.

For example, with `c_2=c_3=1`, numerical roots of

```text
2-2^(1-s)-3^(1-s)=0                                  (6.14)
```

begin along continued-fraction near-periods as follows:

```text
Re(s)             Im(s)
0.9031530861       17.52401003
0.9812955491       45.58804394
0.9987394326      108.70807358
0.9999700747      480.41961088
0.9999928282     2773.80957843
0.9999999869     6028.03876778.                       (6.15)
```

These numbers are only an illustration; Theorem 6.1 is the rigorous
statement.

The theorem closes not merely the `q=2,3` average but every positive
countable scalarization with a fixed analytic margin.  If (6.4) fails for
every `eta_0>0`, the positive sum itself supplies no absolutely convergent
continuation into any fixed half-strip by this construction.  If (6.4)
holds, the scalar factor has zeros in every such half-strip.

Positivity is not essential to the recurrence obstruction.  The following
form closes signed Beatty-, divisor-, or Dirichlet-multiplier scalarizations
whenever their advertised left margin comes from normal convergence.

**Theorem 6.2 (every normally convergent pole-cancelling Dirichlet
multiplier recurs).**  Let

```text
B(s)=sum_(n>=1)b_n n^(-s),
sum_(n>=1)|b_n|n^(-1+eta_0)<infinity                 (6.16)
```

for some `eta_0>0`.  Suppose `B` is not identically zero and `B(1)=0`.
Then there are zeros `s_j` of `B` such that

```text
abs(Im(s_j))->infinity,             Re(s_j)->1.       (6.17)
```

If `B` has no zeros in `Re(s)>1`, these zeros satisfy `Re(s_j)<=1`; if it
also has no nonzero boundary zero, they lie strictly to the left.

### Proof

Put `G(z)=B(1+z)`.  On every closed disc `abs(z)<=r<eta_0`, (6.16) gives
normal convergence.  Simultaneous recurrence of the phases
`exp(-i tau log n)` on each finite set, followed by the normally small tail,
gives unbounded `tau_j` for which

```text
G(z+i tau_j)->G(z)                                  (6.18)
```

uniformly on that disc.  Choose a circle about zero which contains no other
zero of `G` on its boundary.  Rouché gives the same positive number of zeros
of `G(z+i tau_j)` inside.  Repeating on circles whose radii tend to zero and
diagonalizing the recurrence times produces zeros

```text
s_j=1+i tau_j+o(1).                                  (6.19)
```

The last two assertions follow from the assumed zero-free open half-plane
and, respectively, boundary line.  QED.

Thus an absolutely convergent arithmetic multiplier cannot replace the eta
factor by a scalar factor having only its required zero at `s=1`.  Its local
pole-cancelling zero is copied arbitrarily high by vertical almost
periodicity.  Escaping Theorem 6.2 requires conditional convergence in the
proposed fixed strip; proving the uniform cancellation which legitimizes
that conditional multiplier is then part of the fixed-strip problem rather
than a positivity shortcut.

The mechanism is the classical arithmetic/non-strongly-nonarithmetic
renewal obstruction in elementary form: a discrete distribution of delays
`log(q_j)` has arbitrarily accurate almost periods.  Positivity forces the
scalar factor to be `1-phi`; its zero at the origin recurs close to the
imaginary axis.

## 7. Why the vector and Gram routes do not yet add information

The two positive transforms have the exact rank-one factorization

```text
(E_2(s),E_3(s))
 = zeta(s)(f_2(s),f_3(s)).                            (7.1)
```

Equivalently,

```text
f_3(s)E_2(s)-f_2(s)E_3(s)=0                          (7.2)
```

identically.  Thus they are algebraically two encodings but not two
independent holomorphic functions.  Every fixed holomorphic scalarization
is zeta times its corresponding scalar factor.  Keeping the scalarization
positive invokes Theorem 6.1; choosing signed or complex coefficients can
remove the artificial factor, but also removes the positive-density
argument.

For real `sigma>0` one can form the tautologically nonnegative quantity

```text
J(sigma,t)=abs(E_2(sigma+it))^2
          +abs(E_3(sigma+it))^2.                     (7.3)
```

It vanishes exactly at a zeta zero.  Expanding (7.3) as a double integral
does produce positive-semidefinite Gram matrices, but only after the two
oscillatory integrals have already been squared.  Gram positivity says
`J>=0`; it gives no strict lower bound.  Proving

```text
J(sigma,t)>0          for sigma>1-eta                 (7.4)
```

is exactly the desired fixed-strip theorem in different notation.

There is also no uniform rescue by selecting whichever coordinate has the
larger explicit factor.  Although `f_2` and `f_3` never vanish together,
simultaneous Diophantine approximation gives

```text
inf_(abs(t)>T) max(abs(f_2(1+it)),abs(f_3(1+it))) = 0 (7.5)
```

for every `T`.  Pointwise division is possible, but its condition number is
unbounded at high near-periods.

On consecutive unit `x`-intervals the density vector is periodic modulo
six:

```text
n mod 6:       0     1     2     3     4     5
(A_2,A_3):   (0,0) (1,1) (0,2) (1,0) (0,1) (1,2).   (7.6)
```

In particular, even the pointwise vector has a zero sector on every sixth
interval.  No positive linear functional of this finite vector is bounded
below by a positive constant or becomes monotone.

## 8. Exact binary renewal and the boundary term it hides

Let

```text
N(u)=floor(exp(u)),        N(u)=0 for u<0.             (8.1)
```

The least-significant-binary-digit identity is

```text
N(u)=B_2(u)+2N(u-log 2).                               (8.2)
```

Iterating gives the finite pointwise sum

```text
N(u)=sum_(j>=0) 2^j B_2(u-j log 2).                   (8.3)
```

Taking Laplace transforms where the renewal sum converges yields

```text
N_hat(s)
 = [eta(s)/s]/[1-2^(1-s)]
 = zeta(s)/s,                    Re(s)>1.              (8.4)
```

This is the exact positive convolution that divides away the artificial
eta factor.  It explains why regular smoothing could not do so: the renewal
kernel

```text
sum_(j>=0) 2^j delta_(j log 2)                        (8.5)
```

grows like `e^u` and has abscissa of convergence `1`.  It supplies no
positive Laplace representation to the left of `Re(s)=1`.

Subtracting the growth exposes the missing boundary term:

```text
N(u)=e^u-{e^u},                                       (8.6)
```

and hence

```text
zeta(s)/s
 = 1/(s-1)
   - integral_0^infinity {e^u}e^(-su)du.              (8.7)
```

The integral on the right is holomorphic for `Re(s)>0`, but the formula is
now a **difference** between the pole and a positive transform.  If
`zeta(s)=0`, (8.7) becomes

```text
1/(s-1)=integral_0^infinity {e^u}e^(-su)du.           (8.8)
```

The raw positive bound gives only

```text
1/abs(s-1) <= 1/Re(s),
```

or

```text
abs(s-1)>=Re(s).                                      (8.9)
```

This is a bounded zero-free disk near `s=1`, not a fixed vertical strip.
At large height (8.9) is vacuous.  Improving (8.8) uniformly in height by a
fixed power is another form of the prime/integer cancellation problem, not
a consequence of positivity.

The same renewal identity holds for every integer `q`:

```text
N(u)=A_q(e^u)+qN(u-log q).                            (8.10)
```

The vector construction changes the digit systems but does not change the
growing renewal object `N(u)` recovered after division.

## 9. Fourier and functional-equation reality checks

Away from integer endpoints, the square wave has Fourier series

```text
A_2(x)
 = 1/2-(2/pi)sum_(m>=1, m odd) sin(pi m x)/m.         (9.1)
```

After `x=e^u`, these are chirps `sin(pi m e^u)`, not fixed log
frequencies.  For a Mellin height `t`, their stationary interactions occur
around

```text
pi m e^u approximately abs(t).                       (9.2)
```

Thus a fixed-width smoothing in `u` does not produce uniform high-height
cancellation: the resonant scale moves outward with `t`.  Termwise use of
(9.1) also requires an Abel cutoff at the jump points.  Dropping that cutoff
or its endpoint terms is another way of silently deleting the factor zeros
(1.2).

The functional equation gives the final invariant check:

```text
eta(s)/s
 = (1-2^(1-s)) chi(s) zeta(1-s)/s.                   (9.3)
```

The positive Laplace transform therefore contains both the known line-one
factor zeros and every nontrivial zeta zero.  In particular, under RH it
would have infinitely many zeros on `Re(s)=1/2` despite its positive
density.  Any general principle asserting that positive interval geometry
alone makes (1.1) zero-free is false.

A two-atom toy model already gives the basic warning.  The Laplace
transform of the positive measure

```text
delta_0+a delta_L,       a>1,
```

has zeros

```text
s=log(a)/L + (2k+1)pi i/L.                            (9.4)
```

Positive Laplace measures can have zeros arbitrarily far into a right
half-plane.  Theorem 3.1 works because of monotonicity, not positivity by
itself.

## 10. Exact disposition and surviving target

The route has produced four reusable facts.

1. A nonnegative nonincreasing log-density has a zero-free Laplace
   transform in `Re(s)>0` (Theorem 3.1).
2. The eta density fails order-two total positivity by the explicit minor
   (4.3), and no regular zero-preserving convolution can make it monotone.
3. The pair `(E_2,E_3)` has common zeros exactly at zeta zeros in
   `Re(s)>0`; this is the cleanest positive-vector reformulation found here.
4. Every fixed positive discrete scalarization analytic across `Re(s)=1`
   has recurrent artificial zeros approaching that line (Theorem 6.1), and
   the same recurrence holds for every signed Dirichlet multiplier whose
   fixed left margin is supplied by normal convergence (Theorem 6.2).

Accordingly, this branch has not proved that a fixed zero-free strip exists
or that it does not exist.  It has killed the scalar positivity,
variation-diminishing, regular-smoothing, and positive-modulus-averaging
versions without assuming anything about zeta zeros.

The one non-tautological successor would be a genuinely joint estimate,
for some fixed `eta>0`, of the form

```text
max_(q in {2,3})
 abs(integral_0^infinity A_q(e^u)e^(-(sigma+it)u)du)
   >= L(sigma,t)>0,                                  (10.1)
```

uniformly for `sigma>1-eta`, where the proof uses the incompatible residue
patterns in (7.6) before taking absolute values.  No positive scalarization
can prove (10.1), because Theorem 6.1 manufactures near-line-one fake zeros
for every such scalarization.  A successful argument must therefore retain
the signed phase relation between the two coordinates.  By (1.6), proving
(10.1) is already a fixed zero-free strip theorem; it is not an automatic
lemma supplied by the interval geometry.
