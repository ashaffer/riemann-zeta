# Single-hyperbolic-block isolation gate

Status: fail-fast gate closed at the structural level, 2026-08-11.  A
sharp-window qualitative survivor is recorded separately below.  Nothing in
this note proves a zero-free strip or makes a claim about the location of an
actual zeta zero.

## 1. Verdict

The proposed implication

```text
one off-line pair in a Zeta23 Gabor compression
    => one uniformly negative eigenvalue
```

does not follow from the Zeta23 zero-side block structure, its Gabor geometry,
or its local zero-count hypothesis.  There are two exact obstructions.

1. The abstract block hypotheses admit a two-dimensional configuration in
   which two hyperbolic pairs screen one another and the total matrix is
   strictly positive.
2. More strongly, for **every** real even window supported in
   `[-L/2,L/2]`, including the smoothed Zeta23 taper, a full modulation lattice
   of off-line pairs has a positive-semidefinite aggregate matrix.  Thus the
   negative atom of every selected pair has Birman--Schwinger leverage at most
   one against the aggregate positive atoms.

The sharp interval window has an important but insufficient escape: its
evaluation matrix is Cauchy and has full row rank whenever the number `q` of
distinct zero locations is at most the compression dimension `d` and the
nodes are distinct and nondegenerate.  In that regime Sylvester inertia
preserves every off-line negative block.  The current Zeta23 parameter range
does not guarantee `q <= d`, the sharp window has an unusably large remote
tail, and full rank supplies no lower bound on the smallest singular value.

Consequently a statement about the actual zeta zeros would require a new
effective signed-carrier theorem (a uniform sampling/interpolation theorem is
one sufficient route), not another trace estimate or a port of the existing
rank/inertia library.  The original single-block iteration is therefore
stopped before prime-side or Lean implementation.  The later endpoint-jet
report records a sharp-window collision-compactified carrier which improves
this qualitative gate but still has no asymptotic rate.

## 2. Exact rank-one criterion

Let `A` be a positive-semidefinite Hermitian matrix on a finite-dimensional
complex Hilbert space, let `u` be a vector, and let `A^dagger` denote the
Moore--Penrose inverse.

### Theorem 2.1 (rank-one screening)

```text
A - u u* is positive semidefinite
```

if and only if

```text
u belongs to range(A)
and
b(A,u) := u* A^dagger u <= 1.
```

If `u` is not in `range(A)`, then `A-u u*` has a negative direction.  If
`u` is in `range(A)` and `b>1`, the vector `x=A^dagger u` satisfies

```text
x*(A-u u*)x = b-b^2 = -b(b-1).
```

Writing

```text
c(A,u) := u* (A^dagger)^2 u = ||A^dagger u||^2,
```

gives the quantitative bound

```text
lambda_min(A-u u*) <= -b(b-1)/c(A,u).                 (2.1)
```

The same upper bound remains valid after subtracting any positive-semidefinite
matrix.  Adding a Hermitian error `R` changes its right side by at most
`||R||`.

#### Proof

If `u` is not in `range(A)=ker(A)^perp`, its projection `z` onto `ker(A)` is
nonzero and

```text
z*(A-u u*)z = -|u*z|^2 < 0.
```

Now suppose `u` is in `range(A)`.  Put
`w=(A^dagger)^(1/2)u`, so `||w||^2=b`.  Cauchy--Schwarz
in the range of `A` gives, for every `y`,

```text
|u*y|^2 <= b y*Ay.
```

This proves positivity when `b<=1`.  Conversely, substituting
`x=A^dagger u` gives `x*Ax=b` and `u*x=b`, hence `b-b^2`; this is negative
when `b>1`.  Dividing by `||x||^2=c(A,u)` proves (2.1).  This also proves the
only-if direction at `b=1`.  The kernel component of `u` was already handled.

For a Zeta23 off-line pair, write its evaluation vector as `v=x+i y`, with
`x,y` real.  The pair contributes

```text
2m (x x^T - y y^T).
```

Thus the selected negative atom in Theorem 2.1 is
`u=sqrt(2m)y`, while `A` contains the on-line atoms and every positive
`2m x x^T` half.  Formula (2.1) is the exact version of the proposed carrier
gate; trace and Frobenius moments do not determine either `b` or `c`.

## 3. Exact abstract screening counterexample

Take real coordinate vectors `e1,e2`.  Use two simple off-line pairs with

```text
x1=e1,  y1=e2,
x2=e2,  y2=e1,
```

and two simple on-line atoms with evaluation vectors `e1,e2`.  This satisfies
all fields of Zeta23's abstract `ZeroBlockData`: the reflected evaluation
vector is the complex conjugate and every multiplicity is one.

The two pair matrices cancel:

```text
2(e1 e1^T-e2 e2^T) + 2(e2 e2^T-e1 e1^T) = 0,
```

and the full zero-side block is `I_2`, hence strictly positive.  For the
negative atom of the first pair,

```text
A = I_2 + 2e1 e1^T + 2e2 e2^T = 3I_2,
u = sqrt(2)e2,
b(A,u) = 2/3 < 1.                                      (3.1)
```

The selected block is therefore screened even before the negative half of
the second pair is restored.  If the two on-line atoms are omitted, the full
matrix is zero and `b=1`, already disproving every strict uniform margin.

This counterexample is abstract.  It does not by itself settle whether the
special Gabor evaluation vectors used by Zeta23 prevent screening.  The next
two sections address exactly that distinction.

The audited Zeta23 source imposes no hidden separation hypothesis at this
stage.  Its `ZeroBlockData` requires only positive integer multiplicities, an
involution, equality of reflected multiplicities, and
`v(reflect rho)=conj(v(rho))`.  The concrete instantiation sets
`v(rho)_k=phiHat(gammaOf(rho)-tau_k)`.  Poisson summation supplies a norm
identity for a single real-ordinate vector, while the tail package assumes an
upper unit-window count and off-axis decay.  None of these inputs states a
lower zero spacing, full row rank, a lower frame bound, or a bounded
interpolation operator.

## 4. An exact Gabor screening identity

Let `phi` be any real even `L2` function supported in `[-L/2,L/2]`, put

```text
h = 2*pi/L,
F_alpha(r) = integral phi(t) exp(alpha*t) exp(i*r*t) dt,
```

and fix `alpha` with `0<alpha<1/2`.  For ordinates
`gamma_j=gamma_0+jh`, define the Gabor evaluation vectors

```text
v_j(k) = F_alpha(gamma_0-T+(j-k)h),       k=0,...,d-1.
```

These are exactly the vectors
`phiHat(gammaOf(rho_j)-tau_k)` for the off-line points
`rho_j=1/2+alpha+i*gamma_j`; their reflected partners have vectors
`conj(v_j)`.  Give every point multiplicity one.  The Zeta23 reflection
`rho -> 1-conj(rho)` sends `rho_j` to
`1/2-alpha+i*gamma_j`, so this is an explicit reflection-invariant
`ZeroConfig` at the level used by the block theorem.

### Theorem 4.1 (lattice screening)

For every finite coordinate set `0<=k,l<d`,

```text
sum_j v_j(k)v_j(l)
  = L * integral phi(t)^2 exp(-i*(k-l)h*t) dt.           (4.1)
```

The series is understood as the `l2` Fourier-coefficient pairing.  Its
right-hand side is the Gram matrix of the exponentials
`exp(-ikh*t)` in `L2(phi(t)^2 dt)`, multiplied by `L`, and is therefore real
and positive semidefinite.  Adding each reflected partner gives

```text
sum_j [v_j v_j^T + conj(v_j) conj(v_j)^T]
  = 2L * Gram_phi >= 0.                                 (4.2)
```

#### Proof

Let

```text
g(t)=phi(t) exp(alpha*t) exp(i*(gamma_0-T)*t)
```

on `[-L/2,L/2]`.  Then

```text
c_n := F_alpha(gamma_0-T+n h)/L
```

are its Fourier-series coefficients.  Parseval's bilinear coefficient
identity gives

```text
sum_j c_(j-k)c_(j-l)
 = (1/L) integral g(t)g(-t) exp(-i*(k-l)h*t) dt.
```

Evenness of `phi` makes `g(t)g(-t)=phi(t)^2`; both the off-line displacement
`alpha` and the base ordinate cancel.  Multiplication by `L^2` proves (4.1).

Writing `v_j=x_j+i y_j`, equation (4.2) says

```text
P := sum_j 2 x_j x_j^T,
N := sum_j 2 y_j y_j^T,
P-N >= 0.
```

Hence `P>=N>=2y_j y_j^T` for every selected `j`.  Theorem 2.1 then gives

```text
b(P,sqrt(2)y_j) <= 1.                                  (4.3)
```

This is exact Gabor screening, not an arbitrary-matrix model.  It applies to
the smooth Zeta23 taper as well as to the sharp window.

The configuration has one reflected pair per spacing `h`, so its point
density is `2/h=L/pi`.  At `lambda=1/2`, where
`L=(1/2)log(T/(2*pi))`, this is the leading Riemann--von Mangoldt density
`log(T)/(2*pi)`.  It also obeys the `O(log T)` unit-interval upper count used
by the Zeta23 tail argument.  Long lattice blocks can be placed at separated
heights and completed with on-line points outside them; truncating a block
far from the target compression changes (4.2) only by the tapered `r^-2`
tail.  More explicitly, retain the lattice ordinates in
`[T/2,5T/2]` and use the compression band `[T,2T]`.  The omitted rows have
distance at least `T/2` from that band.  The same estimate used in the Zeta23
tail proof bounds their aggregate operator norm by

```text
exp(alpha*L) * L^O(1) / T^2 = o(1)       (lambda=1/2,
                                          0<alpha<1/2). (4.4)
```

The retained finite block therefore has lower edge at least `-o(1)`, while it
contains off-line pairs at the fixed displacement `alpha`.  Its unit-window
count is bounded by an absolute constant times `log(t+3)` because all retained
ordinates satisfy `t asymp T`.  Widely separated copies give one locally
finite configuration with the same behavior along a sequence of heights.

Thus symmetry, the correct leading count scale, taper decay, and Gabor form
do not imply a strict selected-block margin.  Such artificial configurations do
not automatically satisfy the full Riemann--von Mangoldt formula, including
its secondary term and uniform global error, and they do not satisfy the zeta
explicit formula.  The exact identity therefore refutes a deduction from
`ZeroBlockData` plus the local-count/taper inputs; it is not a counterexample
to an additional theorem using genuinely zeta-specific arithmetic.  That
arithmetic is precisely what a successful isolation theorem would have to
use.

There is also a finite-cluster warning at the natural zero spacing.  For the
fixed-width flat-top tapers used by Zeta23, with
`u_gamma=(F_alpha(gamma-tau_k))_(k in Z)`, Fourier-series Parseval gives

```text
 ||u_(gamma+h/2)-i*u_gamma||^2 / ||u_gamma||^2
   = integral phi(t)^2 exp(2alpha*t)
       |exp(i*pi*t/L)-i|^2 dt
     / integral phi(t)^2 exp(2alpha*t) dt
   = O_(alpha,w)(L^-2).                                 (4.5)
```

The weight on the right concentrates a bounded distance from `t=L/2`.
Therefore two distinct off-line pairs separated by `pi/L` have positive and
negative features which nearly exchange roles.  Qualitative full rank does
not control this `O(1/L)` near-dependence.  For a reproducible numerical
check, take `w=1` and the monotone `C^3` ramp

```text
rho(s)=0                                      (s<=0),
rho(s)=35s^4-84s^5+70s^6-20s^7               (0<s<1),
rho(s)=1                                      (s>=1),
phi(t)=rho(L/2-|t|).
```

Numerical quadrature of the exact ratio in (4.5), with `alpha=1/4`, gave
relative errors

```text
L              12       24       48       96
relative error .7491    .4142    .2123    .1068
L * error      8.99     9.94     10.19    10.26.
```

The computation is only a check of the exact identity (4.5), not evidence
about zeta-zero locations.

## 5. The sharp-window full-spark survivor

For the sharp interval window,

```text
phiHat(z) = 2 sin(Lz/2)/z,       phiHat(0)=L.
```

Since `tau_k=T+2*pi*k/L`, a non-grid-degenerate row has

```text
phiHat(z_j-tau_k)
 = 2(-1)^k sin(L(z_j-T)/2)
     / (z_j-T-2*pi*k/L).                                (5.1)
```

After nonzero row and column scalings this is a Cauchy matrix.  Here `q`
counts every distinct point separately: an on-line point once and both
members of an off-line reflection pair; multiplicity does not duplicate a
row.  Consequently, if `q<=d` and the complex nodes
`z_j=gammaOf(rho_j)` are distinct and avoid the displayed degeneracies, the
`q` evaluation rows have rank `q`.  Grid collisions are handled separately
by the corresponding cardinal rows; the nondegenerate statement is enough
for the present audit.

Rows belonging to a reflected pair are complex conjugates.  The
reflection-conjugation-fixed codomain has real dimension `q`, and the complex
rank statement above is the complexification of surjectivity from
`R^d` onto that real codomain.  The zero-side form there is a direct sum of
positive one-dimensional forms and one `(1,1)` hyperbolic form per off-line
pair; its positive multiplicity weights do not change inertia.  Surjectivity
therefore makes the pullback congruent to that direct sum plus `d-q` zero
coordinates.  It has exactly one negative direction per off-line pair.  This
is a genuine qualitative carrier and must not be conflated with the abstract
counterexample in Section 3.

It does not currently yield the desired theorem for four independent
reasons.

### 5.1 The dimension inequality is unavailable

Zeta23 fixes

```text
d = floor(L*T/(2*pi)),       L=lambda*log(T/(2*pi)),
0 < lambda <= 1.
```

Riemann--von Mangoldt gives

```text
N(T,2T)
 = T[log(T/(2*pi))+2log(2)-1]/(2*pi) + O(log T).
```

Thus, for fixed `lambda<1`, `d/N` tends to `lambda`.  Even at `lambda=1`,

```text
N(T,2T)-d
 = (2log(2)-1)T/(2*pi) + O(log T) > 0.                  (5.2)
```

The enlarged zero window `I'` contains still more points.  The number `q` of
distinct locations can equal the multiplicity count, so no unconditional
input in Zeta23 proves `q<=d`.  Its distinct-zero lower bound does not provide
the required upper bound.  Taking `lambda>1` or padding the modulation band
could force `d>=N`, but lies outside the proved prime-side package and would
require a new boundary and second-moment analysis.

### 5.2 The sharp tail is too large

The paper's Remark 4.3 observes that the sharp window has only `1/|r|`
off-axis decay.  Its remote-zero estimate is not `o(L)` even with a much wider
collar than the one used in Zeta23.  The smooth taper and its `1/|r|^2` decay
are essential to the proved small-tail comparison.  Hence the Cauchy formula
cannot simply replace the actual window.

### 5.3 Smooth tapering does not preserve a proved full-spark theorem

For the smoothed kernel `K(z)=phiHat(z)`, the column functions
`K(z-tau_k)` are linearly independent: an identically zero combination would
Fourier-invert to

```text
phi(t) * sum_k c_k exp(-i*tau_k*t) = 0,
```

and the exponential polynomial must vanish on the nonempty interval where
`phi=1`.  Therefore some square evaluation minor is nonzero, and generic
node configurations have full row rank.

This is not the every-configuration full-spark property of the Cauchy kernel.
The Zeta23 source proves conjugation, real-axis reality, Poisson norm
identities, and decay bounds; it contains no theorem excluding a zero of an
evaluation determinant at the actual zero nodes.  The lattice identity
(4.2) also shows that smoothing cannot by itself prohibit collective
screening when the row count exceeds the dimension.

### 5.4 Full rank has no quantitative margin

Suppose nevertheless that a padded smooth evaluation map `E` were
surjective.  A right inverse can isolate one negative coordinate, but the
resulting Rayleigh margin is proportional to

```text
sigma_min(E)^2.                                          (5.3)
```

To dominate the remote tail one needs a uniform lower bound for this singular
value in the same normalization.  Distinctness alone gives none: evaluation
rows vary continuously, and allowed nodes can approach one another or the
near-dependences in (4.5).  Zeta23 assumes only an upper local count, not a
minimum spacing, a Riesz-sequence inequality, or a bounded interpolation
operator.  Its trace and Frobenius estimates are averages and cannot bound
`sigma_min(E)`, `b(A,u)`, or `c(A,u)`.

Accordingly, upgrading qualitative full spark by this *ungrouped right-
inverse route* to the carrier/tail inequality requires an unavailable uniform
interpolation theorem.  This does not rule out a grouped signed-carrier
argument in which collision multiplicities merge.

## 6. Stop/go decision

**Stop:** do not port more Zeta23 linear algebra, attempt a prime-edge bound,
or enlarge the numerical support window under the assumption that one
hyperbolic block automatically survives.  The strict structural statement is
false, and the exact Gabor lattice model shows why.

**Conditional survivor:** a different project could try all four of the
following as one package:

1. construct a tapered or otherwise tail-controlled window with an
   every-node full-spark theorem;
2. choose a compression with `d` at least the full distinct-zero count;
3. prove a zeta-specific signed-carrier lower bound strong enough to dominate
   the remote tail (a grouped interpolation estimate or a singular-value
   bound would suffice); and
4. prove the independent prime-side lower spectral-edge estimate.

Items 2--3 are not consequences of the Anthropic density theorem and item 4
is already fixed-strip-strength arithmetic.  The later additive-edge and
endpoint-jet reports supply item 2 and a fixed-parameter qualitative form of
item 3, but not the effective carrier/tail comparison.  The sharp Cauchy
observation is therefore retained, while the original single-block gate is
closed as the next iteration target.

In theorem-card form, the surviving route would have to prove, for every
`delta0>0`, one common compression and a constant `kappa(delta0)>0` such that
uniformly at large `T`:

```text
dimension:  number of relevant zero points (with multiplicity) <= d(T),
carrier:    an off-line pair at displacement >= delta0
              => lambda_min(A_T) <= -kappa(delta0),
tail:       ||E_tail,T|| < kappa(delta0)/4,
prime edge: lambda_min(G_prime,T) > -kappa(delta0)/2.
```

Here a lower bound for `sigma_min(E_T)` would imply `carrier`, but collision
merging shows that it is not logically necessary.  The carrier constant must
still be effective in the same normalization as `tail`.  The lattice
construction disproves this card when `dimension/carrier` are replaced merely
by the original local counting, Poisson norms, or trace moments.  The precise
decision for the original smooth family remains **no-go on the current
inputs; go only after an independent effective carrier theorem is found**.

Primary external artifacts inspected: Anthropic's
[full paper](https://www-cdn.anthropic.com/564f962e60643842f5fcb4a17c9dbc8f608f1c37.pdf)
and tagged
[Zeta23 Lean source](https://github.com/anthropics/zeta-23-lean/tree/v1.0),
especially `Defs.lean`, `ZeroSide.lean`, `Poisson.lean`, and `Tail.lean`.
