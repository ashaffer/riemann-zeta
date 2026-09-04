# Breakthrough sprint: exact centered parity and the prime-moment frontier

Status: synthesis of new exact finite-dimensional theorems, audited analytic
reductions, and sharply isolated open arithmetic/divisor inputs, 2026-08-12.
No zero-free strip, improved bound on a zeta zero, or RH statement is proved.

## 1. What changed

The sprint produced one exact geometric closure and two materially narrower
arithmetic reductions.

1. **The inherited-anchor carrier loss disappears exactly.**  In a
   candidate-centered symmetric critical grid, choose the endpoint-jet order
   even.  The selected positive row and inherited Hahn anchor are even, while
   the selected carrier is odd.  Therefore

   ```text
   theta_*=1
   ```

   at finite dimension.  Every retained carrier fraction has an explicit
   geometry-only anchor-null companion.  The previously isolated uniform
   Hahn/Weyl asymptotic is unnecessary for this target-only construction.

2. **Sub-full arithmetic admission is a one-square or one odd-moment
   problem, not a whole-matrix problem.**  The first Lanczos plane has an
   exact shifted-Hankel sign criterion.  On its bad branch, the single sign
   `<a,K^3a> >= 0` produces an explicit nonnegative state retaining `8/9` of
   the carrier; more generally one quadratic projected-residual inequality
   suffices under a known lower spectral floor.

3. **Positive prime-log nulling is an honest compact construction.**  A
   positive spectral measure whose characteristic function vanishes at all
   active prime-power offsets transfers, by compact positive-definite
   multiplication and continuous spectral factorization, to a scalar compact
   two-lobe packet.  Its selected carrier is the relevant spectral mass, up
   to superpolynomial error.  Thus the remaining convex prime-log extremal is
   not a nonfactorable relaxation.

These are theorem-level advances inside the program.  They do not yet move a
zeta-zero bound because the actual one-square sign and the divisor-side
collateral exclusion remain open.

## 2. Exact centered-even parity theorem

Let

```text
tau_k=gamma+(2*pi/L)k,        -J<=k<=J,
```

be centered at the hypothetical target `1/2+alpha+i*gamma`.  After the
standard sign conjugation, its reflected-pair evaluation row is a harmless
positive scalar times

```text
x_k+i*y_k=q/(k^2+q^2)+i*k/(k^2+q^2),
q=alpha*L/(2*pi).
```

Thus `x` is even and `y` is odd.  If

```text
W_m={c:sum_k c_k k^r=0, 0<=r<m},
S_m=W_m intersect ker(x),
```

and `m` is even, reflection preserves `S_m`.  The degree-`m` Hahn row `q_m`
and its inherited projection `g=P_(S_m)q_m` are even, whereas

```text
a=P_(S_m)y/||P_(S_m)y||
```

is odd.  Hence `<a,g>=0` and the exact anchor threshold is one.  The exact
odd dimension is

```text
dim S_m^odd=(d-m-1)/2.
```

Thus, once `d-m>=5`, any odd unit `w in S_m intersect a^perp` gives

```text
z_theta=sqrt(theta)*a+omega*sqrt(1-theta)*w in g^perp
```

for every `0<theta<=1` and phase `|omega|=1`.

Given a required endpoint order `m_0`, the least even `m>=m_0` costs at most
one extra moment.  This dimension statement alone does not compare the two
carrier norms.  Instead choose even `m` from the outset and apply the
independent symmetric endpoint-flat packet theorem: it constructs an odd
state in `S_m` with carrier `X^(alpha-o(1))/L`.  Thus the exact parity
geometry and the full carrier exponent are compatible without asserting an
unproved one-step projection ratio.

The same parity gives an exact arithmetic simplification.  For every real odd
state `z`, its centered sharp synthesis is real odd and its square kernel
`W_z` is even.  Therefore the completed von Mangoldt square contains only

```text
sum_(n<=X) Lambda(n)/sqrt(n)
  *cos(gamma*log n)*W_hat_z(log n)
 - matching continuum,
```

with every sine phase canceled.  Neither factor has a fixed sign, so this is
a one-square reduction rather than a positivity theorem.

See
[`ZETA23-CENTERED-EVEN-JET-PARITY-COMPANION-2026-08-12.md`](ZETA23-CENTERED-EVEN-JET-PARITY-COMPANION-2026-08-12.md).

### 2.1 The remaining square is an explicit two-abscissa scalar

Before finite-aperture endpoint projection, the centered carrier is the
Fourier transform of

```text
f(x)=sinh(alpha*x) 1_(|x|<=L/2).
```

Its autocorrelation is

```text
C(u)=sinh(alpha*(L-u))/(2*alpha)
     -(L-u)*cosh(alpha*u)/2,       0<=u<=L,
```

and its prime correlation is exactly

```text
1/4 Re{
   (T^alpha/alpha) P_T(1/2+alpha+i*gamma)
  -(T^-alpha/alpha)P_T(1/2-alpha+i*gamma)
  -D_T(1/2+alpha+i*gamma)
  -D_T(1/2-alpha+i*gamma)},

D_T=L P_T+P_T'.
```

Thus the arithmetic gate is one concrete two-abscissa inequality, not an
unspecified matrix estimate.  Two natural shortcuts are now rigorously
closed.  The parity-evenized completed multiplier is not pointwise positive
(an Arb certificate gives a negative value at `T=4096`), and a positive
height average supported in `[-H,H]` has too few zeros to annihilate all
prime logs unless `H >> T/(log T)^2`.

The functional equation also supplies no hidden sign.  It reduces the
complementary completed logarithmic derivatives to the signed curvature

```text
2*[(cosh(alpha*L)/alpha)u'(alpha)-u''(alpha)],
u(alpha)=log|Xi(1/2+alpha+i*gamma)|,
```

not to a square.  More decisively, the special kernel assigns a strictly
negative response to a matched functional-equation-symmetric off-line
quartet at sufficiently large height.  Multiplication by a symmetric
polynomial which is positive on the critical line preserves the functional
equation, reality, order, and critical-line phase while amplifying that
negative response.  Hence any proof of the scalar sign must use the actual
Euler/von-Mangoldt coefficients (or equivalent zero-location information).

See
[`ZETA23-CENTERED-COSINE-ONE-SQUARE-ARITHMETIC-GATE-2026-08-12.md`](ZETA23-CENTERED-COSINE-ONE-SQUARE-ARITHMETIC-GATE-2026-08-12.md)
and
[`ZETA23-CENTERED-SINH-TENT-FUNCTIONAL-EQUATION-NOGO-2026-08-12.md`](ZETA23-CENTERED-SINH-TENT-FUNCTIONAL-EQUATION-NOGO-2026-08-12.md).

Classical harmonic amplification does not supply the missing Euler input.
The positive polynomial `3+4*cos(theta)+cos(2*theta)` retains the matched
negative quartet at full carrier scale, but the exact sinh-tent
autocorrelation is positive on `[0,L/3]` and negative on `[L/2,L)`.  A
nonnegative trigonometric multiplier therefore leaves a sign-changing prime
weight.  Its unavoidable constant harmonic also creates a same-sign pole
response larger than a fixed-depth target by `exp((1/2-delta)L)`; cancelling
that pole with remote harmonics costs quadratic coefficient mass.  This
closes the bare de la Vallee Poussin/Turan positivity adapter, not
coefficient-specific cancellation between the two prime ranges.  See
[`ZETA23-HARMONIC-CENTER-SINH-TENT-AMPLIFICATION-NOGO-2026-08-12.md`](ZETA23-HARMONIC-CENTER-SINH-TENT-AMPLIFICATION-NOGO-2026-08-12.md).

## 3. Exact Lanczos/Hankel alternative

For a Hermitian arithmetic compression `K`, a unit carrier `a`, and

```text
m_j=<a,K^j a>,        sigma^2=m_2-m_1^2,
```

the first Lanczos plane is exact.  In the decisive branch `m_1<0`, it
contains a nonnegative carrier-rich state precisely when the shifted Hankel
determinant reverses sign and the exact root threshold is met:

```text
Delta_H=m_2^2-m_1*m_3>=0,
s_0=(-m_1)/(sigma+sqrt(Delta_H)/sigma),
theta<=1/(1+s_0^2).
```

Ordinary Hamburger moment positivity is automatic and does not imply this
condition.  The sharp corollary is

```text
m_1<0<=m_3
  => sqrt(8/9)*a+(1/3)*(K-m_1)a/sigma
     has nonnegative K-energy.
```

The retained fraction `8/9` is optimal.

If only `K>=-M I` is known and `m_1=-r<0`, the exact sum-of-squares identity

```text
m_3+M*m_2=||(K+M I)^(1/2)K a||^2
```

gives the more usable sufficient condition

```text
m_2>=max(r*M,r^2/(1-theta)).
```

Failure forces the carrier to be a geometric-mean-scale approximate negative
quasimode.  Raw large-sieve energy does not prove this after endpoint and
selected-row projection: the exact identity is

```text
m_2=r^2+||P_(S intersect a^perp)K_0a||^2,
```

and a finite-rank projection can erase the entire transverse residual.

Actual-coefficient execution found no `m_1<0` point in 253,302 sampled
configurations, so the informative cubic branch was not empirically entered.
This is not evidence for its uniform sign.

See
[`ZETA23-LANCZOS-HANKEL-SIGN-REVERSAL-GATE-2026-08-12.md`](ZETA23-LANCZOS-HANKEL-SIGN-REVERSAL-GATE-2026-08-12.md),
[`ZETA23-ACTUAL-LANCZOS-M3-BRANCH-EXECUTION-2026-08-12.md`](ZETA23-ACTUAL-LANCZOS-M3-BRANCH-EXECUTION-2026-08-12.md),
and
[`ZETA23-PROJECTED-RESIDUAL-RIESZ-GATE-2026-08-12.md`](ZETA23-PROJECTED-RESIDUAL-RIESZ-GATE-2026-08-12.md).

## 4. Positive spectral prime-null theorem

For the active prime-power offsets

```text
u_j=log(n_j/Y_c),
v(xi)=(cos(xi*u_j))_j,
```

consider an even positive spectral probability

```text
mu=w_0*delta_0+(1-w_0)*nu,
supp(nu) subset {Y<=|xi|<=T},
integral cos(xi*u_j)dmu=0 for every j.
```

Writing `r=w_0/(1-w_0)`, feasibility is exactly

```text
-r*1 in conv{v(xi):Y<=xi<=T}.
```

This finite-dimensional convex problem has an exact separation dual and a
Caratheodory solution with at most `M+1` noncentral frequencies.

Let `phi=mu_hat` and multiply it by any fixed smooth compact
positive-definite autocorrelation `R_0`.  Then `R=R_0 phi` is smooth, compact,
positive definite, and vanishes at every `u_j`.  Continuous
Fejer--Riesz/Krein factorization gives `R=q*tilde(q)` with compact scalar
`q`.  Because the noncentral spectral atoms lie above `Y`,

```text
integral R(u)e^(alpha*u)du
 =w_0*C_0(alpha)+O_A(Y^-A).
```

For `p_D=q-q(.-D)`, the selected two-lobe response is exactly

```text
-4*sinh^2(alpha*D/2)
  *[w_0*C_0(alpha)+O_A(Y^-A)],
```

and every active cross-prime value is zero.  Coherent internal spectral
cross terms are retained; none was discarded by diagonal averaging.

Current rigorous information is

```text
w_0<=1/2,
w_0 << (log Y)^(-3/10)              [KMT, upper only],
compact carrier asymp Y^-1          [explicit narrow-lobe construction;
                                     not a bound on w_0],
w_0>=Y^-o(1)                        [open].
```

Four exploratory LP values are compatible with the generic
`M^-1/2=sqrt(log Y/Y)` scale, but prove no asymptotic.  Optimizing the compact
positive-definite multiplier can in principle harvest the heaviest
bounded-frequency cluster rather than the central atom.  Caratheodory only
guarantees that an atomic solution with at most `M+1` atoms has some atom of
mass at least `1/(M+1)=Y^-1+o(1)`; converting that atom into a compact-packet
carrier also requires spectral resolvability and margin inside the available
frequency aperture.  It gives no subpower carrier by itself.

The Riesz-product audit separates positivity from finite spectral type even
more sharply.  On the full prime-coordinate torus, with no upper bound on
the scalar spectral parameter, there is an exact positive measure giving all
active prime-power moments a common value

```text
-r,       r>=c/log Y
```

(and fixed `r` for a multiplicatively generic center).  Kronecker density
then gives a finite scalar atomic realization beyond any prescribed lower
frequency.  What it does not give is return before the polynomial upper cap
`T=Y^(1/d)`.

For the natural grouped prime Riesz product, unique factorization gives the
exact condition numbers

```text
||P_r||_A =exp(Theta(r*M)),
||P_r||_2^2=exp(Theta(r^2*M)),       M=Y^(1+o(1)).
```

Consequently the audited bounded-degree absolute-Wiener transfer stops at
`r=Y^(-1+o(1))`, while its bounded-degree `L^2` or stably Gram-corrected
counterpart stops at `r=Y^(-1/2+o(1))`.  Exponential tilting meets the same
condition-number barrier.  This is a no-go for those transfer mechanisms,
not for every possible high-degree absolute estimate and not an upper bound
for the unrestricted finite-band convex program: a successful escape must
exploit coherent high-degree near-relations of the actual one-dimensional
prime-log orbit.

Ordinary high moments do not reach those relations.  If

```text
S_Y(xi)=sum_(p in the active shell)(p/Y_c)^(i*xi),
```

then a common negative prime moment `-r` necessarily satisfies

```text
r <= sup_(Y_c<=xi<=T)|S_Y(xi)|/M.
```

Applying the Dirichlet-polynomial mean-value theorem to `S_Y^q` and using
`|S_Y'|<<M` gives, for every fixed `q>=1`,

```text
[sup |S_Y|/M]^(2q+1)
 <<_q (T+Y_c^q)/M^q.
```

At `T=Y_c^(1/d)` the normalized power exponent is
`max(1/d,q)-q>=0` for every fixed `q`.  The conductor and
observation-length costs meet exactly.  The explicit uniform version has
right side `O(4^q q! (T+(C Y_c)^q)/M^q)`, so growing `q` does not rescue this
direct mean-value/derivative conversion either.  This closes that ordinary
Montgomery scheme and its coefficient-blind generic large-sieve conversion,
not a coefficient-specific high-degree prime near-relation theorem.

See
[`ZETA23-POSITIVE-SPECTRAL-PRIME-NULL-SQUARE-ROOT-GATE-2026-08-12.md`](ZETA23-POSITIVE-SPECTRAL-PRIME-NULL-SQUARE-ROOT-GATE-2026-08-12.md)
and
[`ZETA23-PRIME-RIESZ-PRODUCT-SCALAR-ORBIT-GATE-2026-08-12.md`](ZETA23-PRIME-RIESZ-PRODUCT-SCALAR-ORBIT-GATE-2026-08-12.md).
The exact early-return calculation is in
[`ZETA23-PRIME-LOG-EARLY-RETURN-MEAN-VALUE-GATE-2026-08-12.md`](ZETA23-PRIME-LOG-EARLY-RETURN-MEAN-VALUE-GATE-2026-08-12.md).

## 5. What was decisively pruned

Two tempting repairs are now closed in their stated classes.

* In the audited fixed-width target-only packet model, a carrier cannot be
  protected uniformly by choosing a positive separation profile after seeing
  collateral zeros.  On every fixed admissible macroscopic separation
  interval there is a finite positive cosine polynomial with a strict
  negative margin.  It produces a fixed microscopic collateral cluster which
  defeats every positive ensemble profile, including an adaptive one.  This
  is an abstract divisor counterconfiguration, not a zeta-zero construction.
  This obstruction is specific to positive ensembles.  A coherent
  fixed-degree virtual-translation packet retains every mixed term and signs
  **every** pair in an arbitrary-cardinality bounded rescaled rectangle
  `L*(alpha-beta)=O(1)`, `L*(gamma'-gamma)=O(1)` negatively, while retaining
  `X^(alpha*d-o(1))`.  It defeats the `+/-pi/D` phase-flip screen and even an
  `O(L)` near-confluent chain.  A second exact construction removes the
  apparent same-state square loss: color collateral conditions between the
  two endpoint legs and balance their nonnegative Hardy potentials.  The
  selected positive-row equation then leaves the harmonic-mean carrier with
  loss `2*max(S_R,S_L)=S_total+o(L)`, exactly one full Blaschke product.
  This has an exact real compact realization for every fixed,
  polynomially-conditioned list.  Broad unit-width lists remain open only at
  the growing compact/discrete-Pick step, not at an algebraic factor of two.
* Ordinary raw Riesz/large-sieve energy cannot be pushed through endpoint
  projection to obtain the Lanczos residual bound.  A rank-`m+1` loss can be
  concentrated exactly on the required target-dependent coefficient.

Coherent separation superpositions, actual-zeta spacing/orientation input,
and the actual prime-log convex inradius are not covered by these no-go
statements.

See
[`ZETA23-FINITE-ADAPTIVE-SEPARATION-COUNTERCONFIGURATION-2026-08-12.md`](ZETA23-FINITE-ADAPTIVE-SEPARATION-COUNTERCONFIGURATION-2026-08-12.md).
The coherent correction and its exact broad-list gates are in
[`ZETA23-COHERENT-MICROCLUSTER-PHASE-TRANSPORT-2026-08-12.md`](ZETA23-COHERENT-MICROCLUSTER-PHASE-TRANSPORT-2026-08-12.md)
and
[`ZETA23-SAME-STATE-BIPARTITE-BLASCHKE-SPLITTING-2026-08-12.md`](ZETA23-SAME-STATE-BIPARTITE-BLASCHKE-SPLITTING-2026-08-12.md).
Under the still-unproved global one-condition-per-phase-cell compression,
the corrected Riemann--von Mangoldt/Bellotti--Wong potential bill leaves the
strict exponent `0.0133834...` at `alpha=1/2,d=2/3`.  The exact half-line
ledger and the remaining finite-Pick/compact gate are in
[`ZETA23-BLASCHKE-DENSITY-ISOLATION-FACTOR-TWO-GATE-2026-08-12.md`](ZETA23-BLASCHKE-DENSITY-ISOLATION-FACTOR-TWO-GATE-2026-08-12.md).
The universal one-zero-per-cell inner function signs the entire collateral
continuum exactly, but spends the whole carrier; truncating it and restoring
the missing delay spends precisely the apparent tail saving.  Thus uniform
dummy-lattice completion is closed, while tailored discrete Pick
interpolation at the actually occupied clusters remains open.  See
[`ZETA23-GLOBAL-PHASE-CELL-COMPRESSION-PICK-LATTICE-GATE-2026-08-12.md`](ZETA23-GLOBAL-PHASE-CELL-COMPRESSION-PICK-LATTICE-GATE-2026-08-12.md).

The divisor filters and the arithmetic rows are also now coupled exactly at
fixed complexity.  Degree-`K` branch filters preserve every prime null iff
the base autocorrelation has Hermite zeros through order `2K`; compact
positive-definite examples exist.  For the chosen efficient branches the
finite-band scaling invariant is instead the transverse inradius of a
twisted prime moment hull (or one aggregate Schur angle).  The fixed-list
problem is compatible; no uniform inradius is known.  See
[`ZETA23-BIPARTITE-BLASCHKE-ARITHMETIC-COUPLING-GATE-2026-08-12.md`](ZETA23-BIPARTITE-BLASCHKE-ARITHMETIC-COUPLING-GATE-2026-08-12.md).

The exact half-disk Pick program has one further sharp model result.  An
alternating one-node-per-cell lattice is signed by an explicit inner
function with target amplitude `1/sqrt(cosh(a))`, exactly the half-product
exponent.  Conversely, a five-point single-cell configuration forces
double-zero behavior and refutes a literal one-simple-root-per-cell rule.
A global half-product theorem is therefore the precise open interpolation
target.  See
[`ZETA23-HALF-DISK-PICK-EXTREMAL-PROBE-2026-08-12.md`](ZETA23-HALF-DISK-PICK-EXTREMAL-PROBE-2026-08-12.md).
The local obstruction extends to every fixed jet order: a finite cluster of
at most `4r+4` rows can force `r+1` Schur attenuations.  This does not yet
multiply across growing cells.  After the exact dimension correction, small
factor-two clusters remain affordable; a proved adverse conditional ledger
first appears only at very large fixed multiplicity.  See
[`ZETA23-TAILORED-DISCRETE-PICK-JET-OBSTRUCTION-2026-08-12.md`](ZETA23-TAILORED-DISCRETE-PICK-JET-OBSTRUCTION-2026-08-12.md).

## 6. Exact remaining closure package

After centering and choosing even endpoint order, geometry is no longer the
bottleneck.  A strip proof through this route still needs two estimates on
the same candidate-adapted state:

```text
ARITHMETIC ONE-SQUARE:
  <z_theta,(K_ar+2*pi/L)z_theta> >= 0;

DIVISOR ISOLATION:
  h_(theta*kappa)(R_other)<theta*kappa
  on the same target-only feasible set.
```

The cosine-only completed correlation, shifted-Hankel/Lanczos condition, and
positive prime-log convex inradius are alternative arithmetic branches, not
interchangeable estimates on a fixed state.  Whichever branch is used must
prove its arithmetic sign and the divisor support-function inequality for the
same constructed state.  The latter requires actual-zeta collateral
information: current count, density, moment, and fixed-packet geometry permit
sparse microscopic phase-flip clusters.

This is a much smaller search space than the original whole-matrix program,
but neither line is currently proved uniformly.  Consequently no known
zero-free bound has been tightened.

## 7. Verification boundary

The centered parity, companion, direct-carrier, and Lanczos implementations
have deterministic tests.  A focused rerun on 2026-08-12 returned

```text
25 passed.
```

The finite Arb certificates prove the signs of their displayed rational
states only.  They do not interpolate parameter neighborhoods or imply an
asymptotic law.  Every structural counterconfiguration is explicitly scoped
away from the assertion that it is realized by the actual von Mangoldt
sequence or the actual zeta divisor.
