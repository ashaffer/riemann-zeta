# Multiblock Gabor splitting: uncertainty and cross-term gate

Status: exact obstruction to the naive block-diagonal and phase-averaged
escapes, 2026-08-11.  The distinguished pair may be fixed in the modulation
core throughout.  This note proves no prime lower edge and no zero-free strip.

## 1. Verdict

Replacing one length-`L` scalar Gabor block by many shorter blocks does not,
by itself, improve the `X^(1/2)` prime scale relative to the `X^alpha`
off-line-pair scale.  There is an exact dichotomy.

1. If all block coordinates are retained, blockwise signs or phases are only
   a unitary change of coordinates.  They do not change the spectrum or norm
   of the prime matrix.  The scalar Weil form retains every interblock
   cross-autocorrelation.
2. Rademacher or phase averaging deletes the mixed prime blocks, but the same
   conditional expectation acts on the zero form.  A fixed core off-line
   pair can have its entire negative edge in those mixed blocks; an explicit
   two-coordinate hyperbolic example is annihilated by dephasing.
3. A time--bandwidth trace inequality forces total time-support measure
   `~log T` for `~T log T` stably core-localized scalar coordinates.  Splitting
   this measure among shorter intervals does not manufacture more scalar
   degrees of freedom.  If the mixed blocks are discarded, each short block
   again has too few coordinates to interpolate the core zero density.
4. Disjointness at shift zero is not orthogonality for the Weil form.  A prime
   at `y=log n` sees the translated overlap of two time blocks.  For any
   bounded support `E`, powers of two give the exact identity

   ```text
   sum_(m>=1) |E intersect (E+m*log 2)|
     = integral_[0,log 2) binom(n_E(r),2) dr.          (1.1)
   ```

   In particular, `|E|>log 2` forces at least one prime-power translated
   overlap (and it is intercomponent when every component is too short to
   overlap its own translate).
   A support of the `~log T` measure required by the dimension count therefore
   cannot null every prime-power cross term by fragmentation.
5. Endpoint-jet tail suppression also does not add across blocks for free.
   Independent blocks require independent boundary conditions.  With a fixed
   total surplus, distributing the jet budget over `J` blocks weakens the
   uniform tail exponent by a factor of order `J` in the full-band design.

The only honest multiblock survivor is consequently not a block-diagonal
argument.  It would have to retain one deterministic **full mixed** scalar
compression and prove simultaneously

```text
fixed-core carrier edge = -K_T,
full mixed remote norm  = o(K_T),
full mixed prime edge   >= -o(K_T).                   (1.2)
```

That is a legitimate new theorem target, but block splitting, orthogonality
at zero shift, and phase randomization do not prove any of its three lines.
The last line must include all interblock prime correlations.  This note does
not rule out a genuinely zeta-specific deterministic cancellation theorem
for them.

## 2. The exact dephasing obstruction

Let a scalar test-function synthesis be written as

```text
S : H_1 direct_sum ... direct_sum H_J -> H,
S(c_1,...,c_J)=sum_j S_j c_j.                         (2.1)
```

For any Hermitian form `Q` on `H`, its compression is the block matrix

```text
G=S^* Q S,        G_(ij)=S_i^* Q S_j.                 (2.2)
```

This applies separately to the zero, pole, archimedean, prime, and completed
forms.  For signs `epsilon_j in {+1,-1}`, put

```text
D_epsilon=diag(epsilon_1*I_(H_1),...,epsilon_J*I_(H_J)).
```

### Theorem 2.1 (full phase families do not randomize an edge)

If all block coordinates remain available, multiplication of block `j` by
`epsilon_j` changes the matrix to

```text
G_epsilon=D_epsilon^* G D_epsilon.                   (2.3)
```

Consequently

```text
spectrum(G_epsilon)=spectrum(G),
norm(G_epsilon)=norm(G),
lambda_min(G_epsilon)=lambda_min(G).                  (2.4)
```

In particular, choosing random signs cannot make the cross-prime operator
small in operator norm or improve its least eigenvalue.

#### Proof

The signed synthesis is `S D_epsilon`, so (2.3) is immediate.  The matrix
`D_epsilon` is unitary.  QED

The same statement holds for arbitrary unit-modulus complex phases whenever
the chosen scalar test class is closed under them.  In the real self-dual
Weil class, Rademacher signs suffice.

### Theorem 2.2 (averaging is a common conditional expectation)

Averaging (2.3) over independent Rademacher signs gives

```text
E_epsilon G_epsilon
 = D(G):=diag(G_(11),...,G_(JJ)).                     (2.5)
```

This operation applies to every term of the explicit formula.  It is not
legal to replace the prime form by `D(G_prime)` while retaining the mixed
zero form.  Moreover,

```text
lambda_min(D(G)) >= lambda_min(G),                    (2.6)
```

so dephasing can raise, and hence erase, a negative carrier edge.

#### Proof

For `i!=j`, the expectation of `epsilon_i epsilon_j` is zero; diagonal
blocks are fixed.  Equation (2.6) follows either from concavity of
`lambda_min` or directly because every matrix in the average is unitarily
similar to `G`.  The explicit formula is an equality of forms for each test,
so averaging the equality necessarily averages all of its terms.  QED

### Example 2.3 (a fixed pair whose edge is purely mixed)

The contribution of one reflected pair to two real coordinates has the form

```text
H_pair=2*(x*x^T-y*y^T).                               (2.7)
```

Take its complex evaluation vector to be

```text
v=x+i*y=(1+i,1-i),
x=(1,1),       y=(1,-1).
```

Then

```text
H_pair=[[0,4],[4,0]],
spectrum(H_pair)={-4,4},
D(H_pair)=0.                                          (2.8)
```

Thus the pair has a strict negative direction before averaging and no edge
at all afterwards.  The example is local to one pair and is unaffected by
placing its ordinate at `3T/2`, or anywhere else in the modulation core.
These evaluation values are compatible with compactly supported real-even
Paley--Wiener coordinates.  Indeed, for fixed
`z=gamma-i*alpha`, `alpha>0`, `gamma!=0`, the transform of an even real
window can be written on the positive half-line as

```text
F(z)=2*integral phi(u)*[
       cosh(alpha*u)*cos(gamma*u)
       +i*sinh(alpha*u)*sin(gamma*u)] du.             (2.9)
```

The ratio of the imaginary and real kernels is
`tanh(alpha*u)*tan(gamma*u)` where defined, and it is not constant on any
open interval.  Two sufficiently concentrated even bumps therefore have
linearly independent complex evaluations; real linear combinations realize
any prescribed complex value.  This can be done separately in two disjoint
symmetric time blocks.  The example is still only an obstruction to the
averaging inference, not a proposed complete zeta-zero configuration.

More generally, replace the block labels by all `J` rows of a unitary phase
matrix.  Keeping all rows is again only a unitary change of basis.  Keeping
`r<J` rows is a genuine compression, but it reduces the dimension from
`Jd_0` to `rd_0` for equal blocks.  Phase cancellation is therefore obtained
only by discarding scalar directions; Section 4 records why those directions
are precisely the scarce resource in the carrier argument.

## 3. Disjoint time support does not diagonalize the Weil form

Use the Fourier convention

```text
fHat(t)=integral_R f(u)*exp(i*t*u) du.
```

For compactly supported `f,g`, Plancherel/Fourier inversion gives the exact
cross-autocorrelation identity

```text
C_y(f,g)
 := integral_R fHat(t)*conj(gHat(t))*exp(i*t*y) dt
  = 2*pi*integral_R f(u)*conj(g(u+y)) du.             (3.1)
```

For the real-even Zeta23 convention, the transforms are real on the real
axis and (3.1) is the same coefficient that appears in the cosine
constituent, up to the already recorded modulation phases.  If

```text
supp(f) subset E_i,       supp(g) subset E_j,
```

then the cross block at the prime shift `y=log n` can be nonzero exactly on
the translated overlap

```text
E_i intersect (E_j-y).                                (3.2)
```

It vanishes for every `f in L2(E_i)` and `g in L2(E_j)` if and only if this
overlap is null.  Ordinary orthogonality of disjoint supports is only the
case `y=0`.

For intervals of lengths `ell_i,ell_j` and centers `a_i,a_j`, (3.2) is
possible when

```text
abs(y-(a_j-a_i)) < (ell_i+ell_j)/2.                  (3.3)
```

For self-dual real-even tests, blocks away from the origin occur with their
reflections.  Formula (3.3) then includes both sums and differences of the
positive block centers.  Spreading short blocks over a span `S` therefore
creates cross-prime shifts throughout that span.  The safe support cutoff is
set by the diameter of the full union, not by the largest component length.

The zero form is even less local: a zero evaluation is an outer product of
the concatenated vector

```text
(F_1(z),...,F_J(z)).                                  (3.4)
```

Its off-diagonal blocks are present unless an actual evaluation
orthogonality theorem is proved.  Hence neither time-domain disjointness nor
ordinary `L2` orthogonality makes the completed Weil form block diagonal.

## 4. The scalar time--bandwidth budget

Let `E` be a bounded measurable time support of measure `M`, let `B` be a
frequency interval of length `T`, and let `V` be a `d`-dimensional subspace
of `L2(E)`.  Suppose every `f in V` satisfies the stable core-localization
bound

```text
integral_B abs(fHat(t))^2 dt/(2*pi)
  >= (1-epsilon)*||f||_2^2.                           (4.1)
```

### Theorem 4.1 (time--band trace inequality)

Under (4.1),

```text
d*(1-epsilon) <= M*T/(2*pi).                          (4.2)
```

#### Proof

Let `f_1,...,f_d` be an orthonormal basis of `V`.  At every real `t`, Bessel's
inequality applied to the vector `1_E(u)exp(-i*t*u)` gives

```text
sum_(r=1)^d abs(fHat_r(t))^2 <= M.                    (4.3)
```

Integrating (4.3) over `B`, dividing by `2*pi`, and using (4.1) proves
(4.2).  QED

At height `T`, the number of zero points in a dyadic core has leading size

```text
q_T ~ T*log(T/(2*pi))/(2*pi).                         (4.4)
```

Thus a stable scalar space with `d>=q_T` and `epsilon=o(1)` must have

```text
M >= (1-o(1))*log(T/(2*pi)).                          (4.5)
```

No collection of co-located window labels evades (4.2): if they are scalar
functions on the same set `E`, they are already counted in `V`.  Treating
the labels as independent vector-valued fibers would multiply the trace, but
the scalar zeta explicit formula would then be replaced by a direct sum of
independent copies.  Its zero form is block diagonal and it loses the mixed
interpolation mechanism of (3.4).

For ordinary critical Gabor blocks the same count is visible without an
asymptotic theorem.  A block of time length `ell_j` and modulation-band width
`T_j` has

```text
d_j = T_j*ell_j/(2*pi)+O(1)                           (4.6)
```

coordinates.  A vertical band of width `T_j` near height `T` contains
`~T_j log T/(2*pi)` zero points at the mean-density scale.  Therefore a
dephased block which must carry its assigned zero band by itself still needs

```text
ell_j >= (1-o(1))*log T.                              (4.7)
```

If every short block spans the full dyadic core, the deficit is more direct:
each block sees all `q_T` rows but has only `T*ell_j/(2*pi)` columns.  The
combined concatenated evaluation map may have enough columns only because of
its mixed blocks, exactly the entries removed by (2.5).

The hypothesis (4.1) is essential and states the uncertainty tradeoff
honestly.  A fixed compact interval contains arbitrarily large finite
subspaces, but directions beyond (4.2) place most of their Fourier energy
outside the target band.  They lie outside the existing continuum-decay
proof of the remote tail.  A discrete escape would require a new sampling
theorem showing that this exterior energy nevertheless misses all remote
zeta ordinates; no such theorem is being assumed here.

## 5. Prime powers prevent exact support-level decoupling

The dimension theorem forces large total measure, while cross-prime terms
sample translated overlaps.  Powers of a single prime already give an exact
support obstruction.

Put `a=log 2`.  For bounded measurable `E`, define for almost every
`r in [0,a)`

```text
n_E(r)=#{k in Z : r+k*a belongs to E}.                (5.1)
```

### Theorem 5.1 (power-of-two overlap identity)

One has

```text
M:=|E|=integral_0^a n_E(r) dr,                        (5.2)

sum_(m>=1) |E intersect (E+m*a)|
 = integral_0^a n_E(r)*(n_E(r)-1)/2 dr
 >= (M^2/a-M)/2.                                     (5.3)
```

In particular, if `M>a`, then

```text
|E intersect (E+log(2^m))|>0                         (5.4)
```

for at least one `m>=1`.

If `diam(E)<=S`, then only `m*a<=S` can occur and

```text
sum_(m>=1) Lambda(2^m)/sqrt(2^m)
              *|E intersect (E+m*a)|
 >= exp(-S/2)*(M^2-a*M)/2.                           (5.5)
```

#### Proof

Decompose the real line into the fibers `r+a*Z`.  Tonelli gives (5.2).
Every unordered pair of occupied points in one fiber contributes once to
the left side of (5.3), proving the identity.  Cauchy--Schwarz gives

```text
integral_0^a n_E(r)^2 dr >= M^2/a,
```

which proves the inequality.  Finally

```text
Lambda(2^m)/sqrt(2^m)=a*exp(-m*a/2)
                     >= a*exp(-S/2)
```

on every nonzero overlap; substituting (5.3) proves (5.5).  QED

For the sharp nonnegative window `1_E`, the overlap in (5.4) is exactly its
autocorrelation coefficient at the activated prime power.  For a general
finite Gabor subspace, (5.4) says that the corresponding translation block
is a nonzero operator on the full `L2(E)` space; a specially chosen smaller
subspace could still annihilate it.  Likewise, (5.5) is a support/absolute-
coefficient statement, not a signed lower-edge theorem.  Its exact scope is
important: it proves that fragmentation alone cannot make all prime cross
blocks vanish, but it does not preclude a new cancellation theorem for their
signed, modulated sum.

Combining (4.5) with Theorem 5.1 shows that every sufficiently large
tail-controlled scalar multiblock support activates a power-of-two overlap.
Also, if the union has diameter `S`, then

```text
S >= |E| >= (1-o(1))*log T.                           (5.6)
```

The only support-uniform explicit-formula cutoff is therefore
`exp(S)>=T^(1-o(1))`.  Using a shorter cutoff requires a proved hole or
cancellation for **each** mixed block; it does not follow from the component
lengths.

## 6. Why the prime/carrier exponent is not improved

Suppose for clarity that `J` equal short blocks have component length

```text
ell=L/J,       L~log T.                               (6.1)
```

There are two incompatible readings.

### 6.1 Keep the full scalar union

The total coordinate count can be `~T*L/(2*pi)`, and the concatenated zero
evaluation map may exploit all of it.  But then equations (3.1)--(3.3) retain
the cross-prime matrices.  If the blocks are packed in a union of measure
`~L`, its diameter is at least `L`; if they are spread farther apart, the
diameter only grows.  The Paley--Wiener type and the support-uniform prime
cutoff are governed by this full diameter `S`, giving the same envelope

```text
off-line depth-alpha scale: exp(alpha*S),
absolute prime scale:       exp(S/2).                 (6.2)
```

for `alpha<1/2`.  Support holes may improve the second line only after a new
estimate for the complete mixed matrix.  Treating it as the sum of the
short-block prime matrices simply omits the terms in (3.2).

### 6.2 Dephase to the direct sum

After (2.5), the self-prime cutoff of block `j` may be as short as
`X_j=exp(ell_j)`, potentially placing it in a much easier range `X_j<<T`.
But the carrier is now also the direct sum of the individual zero forms.
Each block has only `~T*ell_j/(2*pi)` full-core coordinates, so the dimension
surplus that supported combined interpolation has disappeared.  Example
2.3 shows that a negative edge need not survive at all.

If instead each block is kept long enough to meet the zero density by itself,
then `ell_j~log T`, `X_j~T`, and one is back at the transition-scale scalar
prime problem.  Direct sums do not average an operator edge:

```text
lambda_min(direct_sum_j G_j)=min_j lambda_min(G_j),
norm(direct_sum_j G_j)=max_j norm(G_j).                (6.3)
```

Thus neither more blocks nor independent signs turn the known
`X_j^(1/2-o(1))` pointwise bound into `o(X_j^alpha)` for fixed
`alpha<1/2`.

This argument is compatible with the sharper core-sublattice result in
[`ZETA23-CORE-SUBLATTICE-CARRIER-POWER-LOSS-2026-08-11.md`](ZETA23-CORE-SUBLATTICE-CARRIER-POWER-LOSS-2026-08-11.md):
even the unsplit carrier need not retain the full `X^alpha/L` scale from
counting alone.  Splitting and dephasing cannot repair that loss because they
discard, rather than strengthen, the mixed signed Schur information.

## 7. Remote zeros and the fragmentation cost

There is a separate tail ledger.  For a sharp block of length `ell_j`, a
critical modulation grid spanning a frequency interval of width `T`, and
`m_j` endpoint-jet conditions, the integration-by-parts argument used in the
single-block endpoint construction gives schematically, with exact
exponential dependence,

```text
abs(F_(j,c)(z))
 <= ell_j*exp(alpha*ell_j/2)
      *(W_j/abs(z-tau_(c,j)))^m_j*||c||_2,
W_j=T/2+O(1/ell_j).                                   (7.1)
```

Independent blocks have independent boundary traces.  In the critical-grid
model, imposing order `m_j` at both endpoints costs `m_j` independent moment
conditions in block `j`; hence the total cost is

```text
sum_j m_j.                                            (7.2)
```

For general disjoint piecewise-smooth supports the zero extension must have
the required jets at every boundary point.  Uniform repeated integration by
parts cannot cancel distinct boundary exponentials for all remote
frequencies.

For a common collar width `D`, the decisive squared tail factor in block `j`
is

```text
(W_j/(W_j+D))^(2*m_j)
 = exp(-(4+o(1))*m_j*D/T).                            (7.3)
```

If a total dimension surplus permits at most `s` jet conditions, then
`sum_j m_j<=s`.  Protecting all `J` full-band blocks uniformly forces some
`m_j<=s/J`, so the worst-block exponent in (7.3) is at most `1/J` of the
single-block exponent.  The full remote evaluation vector is concatenated;
its rank-one norm involves the sum of the squared block evaluations, not a
probabilistic cancellation.  Rademacher averaging would delete its cross
entries only by applying the same dephasing that can delete the core carrier.

Smooth tapers avoid literal jet constraints, but they do not evade the
theorem card: every new transition zone must be included in the derivative
norms and in the full mixed remote operator.  This note does not assert a
universal lower bound for all smooth fragmented tapers.  It records that the
existing endpoint-jet tail theorem does not improve under fragmentation.

The pair in (1.2) is assumed to satisfy, for example,

```text
gamma in [T+c*D,2T-c*D]                               (7.4)
```

with fixed `c>0`.  None of Theorems 2.1--5.1 uses a collar placement, so the
obstruction is not the collar obstruction from
[`ZETA23-ENDPOINT-JET-COLLAR-CARRIER-RATE-OBSTRUCTION-2026-08-11.md`](ZETA23-ENDPOINT-JET-COLLAR-CARRIER-RATE-OBSTRUCTION-2026-08-11.md).

## 8. The surviving theorem card

A multiblock proposal should be considered live only after specifying one
scalar synthesis `S_T` and proving all of the following in one common
coefficient metric.

```text
SCALARITY
  The blocks synthesize actual scalar Weil tests.  Artificial vector-valued
  copies are not counted as extra zeta coordinates.

DIMENSION / UNCERTAINTY
  The stable core-localized subspace has enough dimensions for the complete
  collared zero count after every boundary and taper constraint.

CORE CARRIER
  If one reflected pair of depth alpha is in the fixed core, then the full
  mixed compact zero matrix satisfies lambda_min <= -K_T.

REMOTE TAIL
  The full mixed remote-zero operator, including cross-block evaluations,
  has norm o(K_T).

PRIME EDGE
  The full prime matrix [G_prime,ij], including every i!=j
  cross-autocorrelation at log n, has lambda_min >= -o(K_T).

COMPLETED REMAINDER
  Pole and archimedean mixed blocks obey the same matched o(K_T) ledger.
                                                               (8.1)
```

If averaging is used, `CORE CARRIER` must be proved **after the identical
average** has been applied to every explicit-formula term.  Combined interpolation before
averaging is irrelevant.  If a phase code retains all block channels, it is
unitarily equivalent to the original full mixed matrix; if it discards
channels, the resulting dimension loss must be paid in `DIMENSION /
UNCERTAINTY`.

No audited estimate in the current repository proves the `PRIME EDGE` line
for this multiblock matrix, and Example 2.3 prevents deriving `CORE CARRIER`
from its unaveraged counterpart.  The multiblock route is therefore closed
as an exponent shortcut.  It remains open only as a demand for a new
zeta-specific deterministic mixed-cross-term theorem, with no current strip
conclusion.
