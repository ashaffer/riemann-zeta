# Prime-log graph diffusion and the adjacent-pair tail gate

**Date:** 2026-08-13

**Verdict:** adjacent-pair transfers expose a useful high/low leverage, but
unrestricted multiscale graph filtering is not a smaller problem than the
remaining antenna problem.  On an ordered prime-log path, every
mass-preserving coefficient change is exactly an adjacent-edge flux.  Thus,
when the dual coefficient norm is unconstrained, signed graph transforms
parameterize the whole coefficient affine space rather than a tractable
subclass.

For one complex high-frequency value the statement is favorable and exact:
the least graph-transport cost of canceling amplitude `A` at height `t` is

```text
|A| / max_j {|exp(i t Delta_j)-1|/Delta_j}.            (0.1)
```

Whenever `t Delta_j` is small on one edge, this changes the entire low band
`|s|<=T` by only `O(|A|T/t)`, however large the edge coefficient itself is.
This confirms that coefficient blowup is not an admissible obstruction.
The difficulty is simultaneous uniform cancellation: far corrections can
make new peaks, and the needed quotient/Schur margin is not supplied by a
path-graph energy estimate.

There are two exact no-go statements for generic diffusion arguments.

1. On a uniform logarithmic mesh, `t=2 pi/h` is an exact alias, so every
   mass-preserving graph transform has high value equal in magnitude to its
   zero-frequency mass.  This remains true for arbitrarily large signed
   coefficients.  The uniform mesh satisfies stronger maximal- and
   mean-square-gap bounds than the prime mesh.
2. A genuine Markov heat flow retains its stationary graph mode.  Its
   long-time high tail is the Fourier transform of its stationary
   prime-node measure, so proving uniform damping still requires a global
   prime-log exponential-sum estimate.

Actual prime logs have no nonzero *exact* common alias by unique
factorization.  Quantifying that nonlattice fact uniformly through
`Y^(50/33)` is precisely the missing arithmetic theorem.  Local gap
moments, diffusion contractivity, and coefficient-norm growth do not prove
it.

No zero-free strip is claimed.

---

## 1. Every mass-preserving change is an adjacent-edge flux

Let

```text
v_1<...<v_M,             Delta_j=v_(j+1)-v_j           (1.1)
```

be the prime logarithms in the fixed shell, and let `q` be any baseline
coefficient vector of mass

```text
m=sum_j q_j.                                             (1.2)
```

For an edge-flux vector `z in C^(M-1)`, define the path incidence map by

```text
(Dz)_1=-z_1,
(Dz)_j=z_(j-1)-z_j       (2<=j<=M-1),
(Dz)_M=z_(M-1).                                         (1.3)
```

### Theorem 1.1 (path-flux completeness)

One has

```text
image(D)={delta in C^M: sum_j delta_j=0}.              (1.4)
```

More explicitly, the unique flux producing a given zero-mass `delta` is

```text
z_j=-sum_(k<=j) delta_k.                               (1.5)
```

If

```text
P_c(t)=sum_j c_j exp(i t v_j),                         (1.6)
```

then exact summation by parts gives

```text
P_(Dz)(t)
 =sum_(j<M) z_j[exp(i t v_(j+1))-exp(i t v_j)].       (1.7)
```

#### Proof

The entries in (1.3) telescope, so `sum Dz=0`.  Conversely, (1.5)
substituted into (1.3) gives `Dz=delta`.  Collecting the coefficient of
each `z_j` in (1.6) proves (1.7).  QED

Consequently a sequence of arbitrary signed adjacent-pair transfers reaches
every vector of mass `m`:

```text
q+image(D)={c in C^M:sum_j c_j=m}.                    (1.8)
```

This is the central coordinate warning.  A multiscale adjacent-pair
construction with unrestricted signed gains has not reduced H1; it has
merely written all of its coefficients in cumulative-flux coordinates.
Theorem 1.1 holds over either `R` or `C`; the real version applies directly
to the cosine antenna, while the complex version is a convenient stronger
diagnostic.

The same conclusion holds for a polynomial graph filter.  If a
self-adjoint path Laplacian `L` has simple spectrum and `q` has nonzero
projection on every eigenvector, spectral interpolation gives

```text
{p(L)q: degree(p)<M}=C^M.                              (1.9)
```

Imposing `p(0)=1` fixes the stationary mass component and leaves the full
same-mass affine space.  If this cyclicity happens to fail, independently
controlled edge transfers still give (1.8).

---

## 2. Exact one-point leverage, and why coefficient size is not a no-go

Put

```text
d_j(t)=exp(i t v_(j+1))-exp(i t v_j),
Lambda_Y(t)=max_(j<M) |d_j(t)|/Delta_j.               (2.1)
```

For a flux use the transport seminorm

```text
||z||_(1,Delta)=sum_(j<M) Delta_j |z_j|.              (2.2)
```

### Theorem 2.1 (one-height optimal edge transfer)

For every `A in C` and every `t` with `Lambda_Y(t)>0`,

```text
inf {||z||_(1,Delta): P_(Dz)(t)=A}
 =|A|/Lambda_Y(t).                                    (2.3)
```

Moreover the minimizer may be supported on one edge attaining the maximum
in (2.1), and it obeys

```text
sup_(|s|<=T)|P_(Dz)(s)|
 <=T |A|/Lambda_Y(t).                                 (2.4)
```

#### Proof

Equation (1.7) gives

```text
|A|<=Lambda_Y(t)||z||_(1,Delta).                      (2.5)
```

Equality is attained by taking only a maximizing `z_j` nonzero and choosing
its complex phase so that `z_j d_j(t)=A`.  Finally,

```text
|d_j(s)|<=|s|Delta_j                                  (2.6)
```

proves (2.4).  QED

If some edge has `0<|t|Delta_j<=pi`, then

```text
|d_j(t)|/Delta_j>=2|t|/pi,                            (2.7)
```

and (2.4) becomes

```text
sup_(|s|<=T)|P_(Dz)(s)|
 <=(pi/2)|A|T/|t|.                                    (2.8)
```

Thus at `T=Y^.01` and `|t|=Y^.751`, a single complex peak has a low/high
leakage ratio at most `Y^(-.741+o(1))`.  An average-sized prime-log gap is
`Y^(-1+o(1))`, so (2.7) is available uniformly up to
`t<=Y^(1-o(1))` after choosing one suitably short edge.

The flux coefficient used to attain (2.8) can be enormous.  That is not a
contradiction: the antenna dual imposes no coefficient norm bound.  Large
`l1`, `l2`, graph energy, or heat time can invalidate a proposed
triangle/Bernstein proof, but they cannot by themselves rule out the
coefficient vector.

Theorem 2.1 is written for the complex exponential relaxation.  In the
real cosine problem the identical linear-programming formula holds with

```text
d_j(t)=cos(t v_(j+1))-cos(t v_j),                     (2.9)
```

but (2.7) then also depends on the carrier phase.  Two-edge real correction
is the corresponding two-row interpolation problem.  None of these
one-point formulas controls the new peaks created elsewhere.

---

## 3. Fixed diffusion retains a prime-polynomial stationary mode

Let `Q_s=exp(-sL)` be a mass-preserving irreducible Markov semigroup on the
prime path, acting on coefficient columns, and let `pi` be its stationary
probability vector.  Then

```text
Q_s q -> m pi                                           (3.1)
```

and hence

```text
P_(Q_s q)(t) -> m sum_j pi_j exp(i t v_j).             (3.2)
```

The constant graph mode is not damped.  Choosing a physical-coordinate
Laplacian can make `pi` resemble the desired continuous profile, but a
uniform bound for the right side of (3.2) on

```text
Y^.751<=|t|<=Y^(50/33)                                (3.3)
```

is itself a weighted actual-prime exponential-sum theorem.  Shorter heat
time leaves additional graph modes and cannot remove the need to control
their sampled exponential phases.

There is also no exact scalar Fourier multiplier on a generic finite node
set.

### Lemma 3.1 (no nontrivial continuum multiplier)

Let `A:C^M->C^M` be linear.  If for every `t` in a nonempty real interval

```text
A^* a(t)=mu(t)a(t),       a(t)=(exp(i t v_j))_j,       (3.4)
```

then `A` is scalar.  If it also preserves mass, then `A=I`.

#### Proof

The vectors `a(t)` over any interval span `C^M`: otherwise a nonzero finite
exponential polynomial would vanish on an interval.  The scalar `mu(t)`
must take values in the finite spectrum of `A^*`.  Continuity and the
identity theorem put the entire curve in one eigenspace, which must
therefore be all of `C^M`.  Mass preservation and `a(0)=1` fix the scalar
as one.  QED

So the continuous heat heuristic `exp(-s t^2)` is only a continuum or
translation-invariant approximation.  On the irregular finite prime path,
turning it into a uniform estimate requires a separate discretization and
alias theorem.

---

## 4. Exact universal alias countermodel

Take a uniform logarithmic mesh

```text
v_j=v_0+jh.                                            (4.1)
```

At every alias height

```text
t_k=2 pi k/h                                          (4.2)
```

one has

```text
a(t_k)=exp(i t_k v_0) 1.                              (4.3)
```

Therefore, for every coefficient vector of mass `m`, with no positivity or
norm assumption,

```text
|P_c(t_k)|=|m|.                                       (4.4)
```

For a real-cosine countermodel, center the mesh so that `v_0/h` is an
integer.  Then the common phase in (4.3) is one and the cosine value itself,
not merely the complex modulus, equals `m`.

In particular (4.4) survives every mass-preserving graph diffusion,
signed edge transfer, multiscale filter, and iterative correction.

Choose `M asyp Y/log Y` and `h asyp log Y/Y`.  Then the first alias has
height `Y^(1+o(1))`, inside (3.3), while

```text
max Delta_j=Y^(-1+o(1)),
sum_j Delta_j^2=Y^(-1+o(1)).                          (4.5)
```

These are stronger than both gap inputs used by the Voronoi theorem.  Thus
no proof based only on path locality, mesh size, maximal gaps, mean-square
gaps, or diffusion dissipation can yield the desired full-tail damping.
It must use a genuinely nonlattice feature of the actual prime logs.

For actual primes there is no nonzero exact common complex alias.  Indeed,
if three distinct primes `p,q,r` had equal phases, then

```text
t log(p/q)=2 pi m,       t log(r/q)=2 pi n            (4.6)
```

for nonzero integers `m,n`.  Their quotient would make
`log(p/q)/log(r/q)` rational, hence give a nontrivial multiplicative
relation among `p,q,r`, contrary to unique factorization.  This qualitative
fact supplies no power-uniform lower phase margin on (3.3).  Approximate
aliases also do not obstruct unbounded coefficients by themselves; one
needs a quantitative continuum interpolation statement.

---

## 5. The exact quotient problem is unchanged

Let

```text
L={|t|<=T},
H={Y^.751<=|t|<=Y^(50/33)},                            (5.1)
```

and let the real baseline `q` have the correct zero-frequency mass.  Write

```text
C_c(t)=sum_j c_j cos(t v_j).                           (5.2)
```

For a low tolerance `eta`, define

```text
E_graph(eta)
 =inf_(z in R^(M-1)) {||C_(q+Dz)-b||_(C(H)):
                      ||C_(q+Dz)-b||_(C(L))<=eta}.    (5.3)
```

Theorem 1.1 gives the exact identity

```text
E_graph(eta)
 =inf_(c in R^M, sum c=m) {||C_c-b||_(C(H)):
                            ||C_c-b||_(C(L))<=eta}.   (5.4)
```

The right side is the original unrestricted antenna approximation problem.
Thus a successful signed graph construction would be a genuine solution,
but graph coordinates alone neither weaken nor prove it.

For finitely many protected low samples `S` and high correction centers
`T_0`, the edge response matrix is

```text
A_(T_0)D,       A_(T_0)=(cos(t_r v_j))_(r,j).         (5.5)
```

An exact alias is an exact row relation killing `D`, as in (4.3).  In the
absence of exact rank loss, a very small singular value only forces very
large edge coefficients.  Since those coefficients are unconstrained, that
is not a feasibility obstruction.  It matters only when one tries to turn
finite interpolation into uniform control: the large coefficients enlarge
derivatives and can create unresolved between-grid peaks.

The complex-exponential version is identical after complexification.  The
required invariant is therefore not an ordinary graph spectral gap or
an `l2` condition number.  It is a **quotient Chebyshev margin**: a bound for
the high evaluation operator on edge fluxes modulo the continuum low-band
seminorm.  Equivalently, by the Wiener/Hahn--Banach duality already audited
in the antenna reports, it is the same carrier-relative atomic/Schur margin
as H1.

---

## 6. Decision

```text
adjacent-pair flux parameterizes all same-mass coefficients:      EXACT;
one-complex-height optimal transport cost (0.1):                  EXACT;
single-height low leakage O(T/t) below the first mesh scale:      PROVED;
large coefficient/flux norm rules out a dual candidate:          FALSE;
fixed Markov diffusion removes its stationary prime mode:         FALSE;
uniform-mesh alias survives arbitrary signed transforms:          EXACT;
local gap moments exclude that alias mechanism:                   FALSE;
actual primes have a nonzero exact common complex alias:           FALSE;
quantitative prime-log nonlattice margin through Y^(50/33):       OPEN;
graph/diffusion uniformly damps the remaining tail:               NOT PROVED;
uniform zeta zero-free strip:                                     NOT PROVED.
```

The graph idea remains useful only if it produces genuinely new arithmetic
control of the quotient in (5.4), for example a uniform multiscale
nonalias theorem for actual prime-log gaps together with a continuum
between-peak bound.  Without that input, unrestricted signed filtering is a
change of variables and contractive positive diffusion ends at another
unresolved prime polynomial.
