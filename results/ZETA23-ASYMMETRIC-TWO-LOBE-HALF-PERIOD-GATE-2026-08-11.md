# Asymmetric two lobes cross the exact-density half-period

Status: exact dimension and exponent ledger, an exact separated-frequency
threshold, an exact periodic-mirror target lemma, and identification of the
first unresolved confluent gate, 2026-08-11.  No zero-free strip is proved.

## 1. Verdict

The symmetric two-lobe proposal is vulnerable to a sparse exact-density
`k=2` island because each lobe has length below the reciprocal period
`L/2`.  An asymmetric allocation removes that particular obstruction.

Take a free left lobe of length `aL` and a right seed lobe of length `bL`,
with

```text
a>1/2,        b=b_T->0,        bL->infinity,
a+b<1.                                               (1.1)
```

Their center separation is

```text
d_(a,b)*L,       d_(a,b)=1-(a+b)/2.                  (1.2)
```

The free lobe pays the off-line positive rows, endpoint jets, cross-prime
rows, and poles.  Its dimension is `(a+o(1))N`, whereas the known off-line
positive-row count is at most `(r_0+o(1))N`, with
`r_0=0.163749648...`.  Thus the algebraic ledger has very large slack.

The same-lobe prime term has scale `X^(a/2+o(1))`; the seed same-lobe term
has scale only `X^(b/2+o(1))`.  A retained cross-center pair response has
scale

```text
X^(alpha*d_(a,b)-o(1)).                              (1.3)
```

Therefore the exact power gate is

```text
alpha*d_(a,b)>a/2
 iff alpha>a/(2-a-b).                                (1.4)
```

Letting `a` decrease to `1/2` and `b` decrease to zero makes the right side
of (1.4) tend to `1/3`.  A target-conditioned subpower theorem for this
asymmetric system would formally give the conditional right edge

```text
Re rho<=5/6+epsilon.                                 (1.5)
```

This is weaker than the symmetric conditional `3/4` edge, but it is **not**
countermodel-safe.  When `a+b<2/3`, one has `d_(a,b)>2/3`; the audited
variable-depth `k=3` island has full operator edge at most
`X^(2alpha/3+o(1))` and therefore refutes a universal
`X^(alpha*d_(a,b)-o(1))` target theorem on the current bulk class.

There is still exact positive structure:

1. a free lobe with `a>1/2` lies above the Ingham period of exact-density
   `k=2` rows;
2. for an exact periodic block, the endpoint point-packet model reflected
   through one full local support length makes every row phase identical,
   cancels every positive endpoint component, and doubles every negative
   component, even when the pair depths vary; a polylogarithmic island has a
   finite-band realization with only `X^o(1)` loss; and
3. exact repetitions with the same ordinate and depth merely add
   multiplicity and are equally favorable.

What remains is not another regular lattice.  Riemann--von Mangoldt permits
aperiodic collision groups of order `O(L)` and near-critical chains.  A
uniform, collision-stable target theorem for those groups is not supplied by
the current first two moments.  The independent cross-prime condition also
remains a Wiener-atomic, rather than Hilbert-space, interpolation problem.

The honest outcome is

```text
polylogarithmic tapered k2 island: handled by asymmetric mirror geometry;
power-length varying-depth k3:    still refutes the formal 5/6 premise;
separated real-frequency skeleton: handled for a>1/2;
aperiodic confluent deep rows: open target-conditioned gate;
completed arithmetic row: open target-aligned aggregate gate.
```

The first **zero-side** numerical target not contradicted by the `k=3` cap
approaches the carrier exponent `2alpha/3` from below.  At the limiting
ledger, comparison with `X^(a/2)` gives

```text
2*alpha/3>a/2,
alpha>3*a/4 -> 3/8 as a downarrow 1/2.               (1.6)
```

Thus the first `k=3`-cap-safe exponent ledger is the formal conditional
`7/8+epsilon`, not `5/6+epsilon`.  It is not safe after the completed
aggregate row is adjoined: the exact one-pair quotient makes that row
parallel to the target, as recorded in the logic audit cited in Section 8.

## 2. Geometry and dimension ledger

Use the physical intervals

```text
I_-=[-L/2,-L/2+aL],
I_+=[ L/2-bL, L/2].                                  (2.1)
```

Their centers are

```text
c_-=-(1-a)*L/2,
c_+=(1-b)*L/2,                                      (2.2)
```

which proves (1.2).  The two same-lobe difference sets have lengths `aL`
and `bL`.  The positive cross-lobe differences range over

```text
[(1-a-b)*L,L].                                      (2.3)
```

Let

```text
N=N(T,2T)=(1+o(1))*T*L/(2*pi).                      (2.4)
```

The free lobe has complex Shannon dimension `(a+o(1))N`.  The complete
condition ledger is

```text
off-line positive rows       <=(r_0+o(1))*N,
endpoint jets and collar       o(N),
cross-prime-power rows          o(N),
two poles and target            O(1).                (2.5)
```

Indeed, (2.3) gives at most

```text
#{n=p^k:X^(1-a-b)<=n<=X}
 <=(1+o(1))*X/L,                                    (2.6)
```

and the standard padding condition gives

```text
(X/L)/N=O(exp(eta)/L^2)=o(1).                       (2.7)
```

Thus the surplus is at least `(a-r_0-o(1))N`.

The short seed must still support the endpoint-flat packet.  If

```text
s_0=O(sqrt(eta*L))                                  (2.8)
```

is the binomial endpoint layer, it is enough to choose

```text
b->0,          bL/s_0->infinity,
b*L^2/exp(eta)->infinity.                            (2.9)
```

For example
`b=(eta/L)^(1/4)+L^(-1/3)` has these properties throughout the admissible
mesoscopic regime.
The last condition says that the seed has more effective modes than the
`O(X/L)` cross-prime rows.  It is compatible with the raw-prime condition
`exp(eta)*log L/L->0`.  No positive fraction of the ambient dimension is
spent on the seed.

### Real-admissibility audit

The asymmetric lobe space need not itself be invariant under physical
reflection.  This causes no loss of admissibility.  It is a subspace of the
complexification of the real endpoint-jet coefficient space.  For the full
real symmetric completed matrix `A`, if `z=x+i*y`, then exactly

```text
conj(z)^T*A*z=x^T*A*x+y^T*A*y.                      (2.10)
```

Hence a negative total form for the asymmetric complex packet yields a
negative admissible real packet, `x` or `y`.  Individual prime nulls and
individual lobe supports need not survive in that component; the total
identity (2.10) is what is used.

## 3. The exact power ledger

For a normalized packet whose two active pieces are centered at (2.2), the
selected reflected pair has a cross response at the separation (1.2):

```text
K_target=X^(alpha*(1-(a+b)/2)-o(1)).                (3.1)
```

The free-free prime differences are at most `aL`, so Chebyshev and partial
summation give

```text
P_same<<X^(a/2+o(1)).                               (3.2)
```

The seed-seed part is at most `X^(b/2+o(1))`; it is smaller than (3.2).
All cross-prime terms in (2.3) are to be nulled by the joint interpolation
system.  Pole, archimedean, and remote-tail terms are subpower relative to
(3.1) under the usual endpoint hypotheses.

Comparing (3.1) and (3.2) proves (1.4).  More explicitly, for every fixed
`epsilon>0` and `alpha>1/3+epsilon`, one can first choose a fixed
`a>1/2` sufficiently close to `1/2`, and then choose `b=o(1)`, so that

```text
alpha*(1-(a+b)/2)>a/2+c_epsilon                     (3.3)
```

for a fixed positive `c_epsilon`.

Equation (3.3) is the formal center-carrier ledger, not a surviving theorem
on the current bulk class.  A target not contradicted by the zero-side
`k=3` cap must retreat to a fixed separation

```text
1/2<d_*<2/3.                                        (3.4)
```

Put the seed packet at `x_+=(1-b)L/2` and the free packet at
`x_-=x_+-d_*L`.  For `a>1/2`, small `b`, and (3.4), both points lie in the
interiors of the intervals (2.1).  The retained response would have scale

```text
X^(alpha*d_*-o(1)),                                 (3.5)
```

and its prime comparison is

```text
alpha*d_*>a/2.                                      (3.6)
```

Letting `a` decrease to `1/2` and `d_*` increase to `2/3` makes (3.6) tend
to `alpha>3/8`.  The strict inequalities in (3.4) keep this reduced carrier
strictly below the audited `X^(2alpha/3+o(1))` `k=3` cap.

## 4. Exact-density `k=2` crosses from supercritical to subcritical

The local exact-density pair centers have spacing

```text
Delta_2=4*pi/ell,          ell/L=1+o(1).             (4.1)
```

Lemma 2.1 of the symmetric one-third audit gives, on the free lobe,

```text
integral_(I_-)
 abs(sum_j c_j*exp(i*gamma_j*t))^2dt
 >=(aL-ell/2)*sum_j abs(c_j)^2
 = (a-1/2+o(1))*L*||c||_2^2                        (4.2)
```

for every `Delta_2`-separated frequency set.  The corresponding upper bound
is `(a+1/2+o(1))*L*||c||_2^2`.  Thus the real-frequency sampling skeleton has
a right inverse whose normalized cost is

```text
sqrt((a+1/2+o(1))/(a-1/2+o(1)))=O_a(1).             (4.3)
```

The `k=3` spacing has threshold `L/3` and therefore has still more room.
This proves that neither regular lattice has the exponentially bad proper-
arc singular vector which defeated symmetric lobes.

Equation (4.2) is not silently promoted to the full theorem.  Exact
hyperbolic rows have depth-dependent endpoint multipliers, and collision
groups require divided differences with their natural weights.  The point
of (4.2) is precise: after `a>1/2`, raw real-frequency density is no longer
the obstruction.

## 5. Periodic mirror target retention

There is a stronger exact statement for the tapered periodic islands
themselves.

### Lemma 5.1 (full-period endpoint mirror)

Let the pair centers be

```text
gamma_j=beta+j*(2*pi/P),                             (5.1)
```

and allow their depths `alpha_j` to vary arbitrarily.  In the endpoint
point-packet model, suppose the right seed and a reflected copy inside the
free lobe are separated by

```text
D=k*P,             k in Z.                           (5.2)
```

Then the phase acquired under this translation is

```text
exp(-i*gamma_j*D)=exp(-i*beta*D)                    (5.3)
```

for every `j`.  Reflection makes the two hyperbolic endpoint magnitudes
equal for each individual depth `alpha_j`.  Multiplying the reflected point
packet by the negative of the common phase in (5.3) therefore gives, row by
row,

```text
positive endpoint coordinate=0,
negative endpoint coordinate=2*(seed coordinate),  (5.4)
```

up to the harmless common sign convention for the negative row.  The two
packet pieces have equal coefficient norm.  QED

For exact-density `k=2`, `P=ell/2` and the two inward endpoints are separated
by `D=ell=2P`.  For the audited sharp `k=3` lattice, `P=L/3` and the sharp
endpoints are separated by `D=L=3P`.  The reflected seed fits
inside the free lobe for every `a>b`; in particular it fits under (1.1).
Thus (5.4) applies to the constant-depth and tapered islands, including the
distinguished deepest pair.  Their other negative rows have the favorable
sign.

This is target retention, not merely a lower singular-value estimate.  It
also shows why slowly varying depth does not defeat the endpoint point-
packet mirror: the cancellation is paired row by row before the depths are
compared.

For a finite-width packet, reflection reverses its local Fourier variable;
thus (5.4) is not asserted literally for an arbitrary broad seed.  If the
island has ordinate span `H`, a sufficient point-approximation condition is

```text
H*w=o(1),              max_j alpha_j*w=o(1).         (5.5)
```

The two reflected local Fourier integrals and their hyperbolic weights then
differ from the point-packet identity by `o(1)`.  But this relative statement
does **not** by itself retain the desired carrier power.  The exact normalized
endpoint-band response contains

```text
c_(alpha,w)=4*sinh(alpha*w/2)^2/(alpha^2*w)~w.       (5.6)
```

Thus shrinking `w` costs the factor `w`.  For a polylogarithmic `k=2` island,
say `H=L^B`, one may take `w=L^(-B-2)`: (5.5) holds and `w=X^(-o(1))`, so the
finite packet loses only `X^o(1)`.  This rigorously transfers the point mirror
for that obstruction.

It does not transfer the canonical power-length `k=3` island.  There
`H=X^(alpha/3)`.  The condition `Hw=o(1)` forces at least the fixed-power
loss `w<=X^(-alpha/3-o(1))`; the narrower endpoint transition choice
`w=O(sqrt(L/T))` loses `T^(-1/2+o(1))`.  Conversely a fixed-width packet
retains the carrier power but does not satisfy (5.5).  Therefore Lemma 5.1
is exact for point packets, has a power-preserving finite realization for
polylogarithmic islands, and supplies no power-preserving realization for
the audited power-length varying-depth `k=3` island.

For the polylogarithmic case, finite endpoint ramps and the `L-ell=o(L)`
padding are handled by placing the two packets at the inward exact-density
endpoints `+-ell/2` and using the endpoint-flat binomial construction.  Their
loss is `X^o(1)`.  No analogous claim is made here for the power-length `k=3`
island.

## 6. What collision grouping proves and what it does not

Exact repetitions with the same ordinate **and the same depth** are benign.
Those equal rows merge by adding their positive integer multiplicities, and
(5.4) is unchanged.  Rows at the same ordinate but different depths are not
equal; they belong to the confluent problem below.  A cluster tending to a
common full row parameter has matched expansions such as

```text
x(gamma+epsilon)
 =sum_(r>=0)epsilon^r*x^(r)(gamma)/r!,
y(gamma+epsilon)
 =sum_(r>=0)epsilon^r*y^(r)(gamma)/r!,               (6.1)
```

and the positive and negative Gram matrices carry the same moment weights
`sum epsilon_j^(r+s)`.  Normalizing every divided difference independently
would destroy these weights and recreate a false small-singular-value
obstruction.

If both ordinate and depth vary, (6.1) is replaced by the corresponding
two-parameter Taylor expansion in `(gamma,alpha)`.  The same warning applies
to its multi-index moment matrix.

There are therefore two exact endpoint cases:

```text
separated group centers at k2 scale:  Fourier skeleton controlled by (4.2);
exactly repeated full rows:           signed target retained by (5.4).
```

The missing theorem is the uniform bridge between them.  Riemann--von
Mangoldt supplies only

```text
#(zeros in [u,u+R])
 =integral_u^(u+R)log(t/(2*pi))/(2*pi)dt+O(L),
#(zeros in [u,u+1])=O(L).                            (6.2)
```

Thus one collision group may have order `O(L)`, and near-critical chains may
persist over polylogarithmic intervals before the `O(L)` discrepancy is
exhausted.  The leading trace and Frobenius identities average over
`asymp TL` directions and do not control the condition number of such one-
block confluent data.

### Why blocks of width `R=log L` do not close the gate

Frequency localization into polylogarithmic ordinate blocks gives the right
dimension heuristic, but Riemann--von Mangoldt alone gives no quantitative
Hermite constant.  The exact obstruction already occurs for

```text
f_j(t)=exp(i*j*epsilon*t),       0<=j<=R.             (6.3)
```

Normalize the `R`-th difference coefficients

```text
c_j=(-1)^(R-j)*binom(R,j)/sqrt(binom(2R,R)).         (6.4)
```

Then `||c||_2=1` and, on any lobe contained in a physical interval of size
`O(L)`,

```text
||sum_j c_j*f_j||_2
 =||[exp(i*epsilon*t)-1]^R||_2/sqrt(binom(2R,R))
 <=C*sqrt(L)*(C*epsilon*L)^R.                        (6.5)
```

Thus a uniform arbitrary-data right inverse costs at least

```text
c*L^(-1/2)*(c/(epsilon*L))^R.                       (6.6)
```

Neither (6.2) nor the unit-window count gives a lower bound for `epsilon`.
With `R=log L` and `epsilon=exp(-L)`, (6.6) is
`exp(Omega(LR))`, not `exp(O(R))`.  Such a cluster is far smaller than the
`O(L)` rows which (6.2) permits in one unit interval.  Cutting ordinate
space into adjacent blocks also leaves arbitrarily close row spaces across a
block boundary.

Natural divided differences remove the small powers of `epsilon` only when
the entire near-collision cluster is merged with its matched analytic
weights.  They do not justify truncating its order at `R`.  The exact
target-specific inequality still needed for a block `B` is

```text
y_B^*(A_B*A_B^*)^dagger*y_B
 <=L^O(1)*||r||^2,       y_B=A_(+,B)*r,              (6.7)
```

after quotienting exact repeated full rows and using the natural confluent
basis.  Here `A_B` is the free-lobe sampling map and `r` is the short-seed
datum.  Inequality (6.7), together with retention of the distinguished
negative coordinate, may exploit that `y_B` is matched analytic data; (6.5)
does not disprove it.  But (6.7) is precisely the target-conditioned Hermite
theorem sought, and it is not a consequence of the block count.

There is a rigorous depth reduction.  Choose the distinguished pair to have
maximal depth `alpha` in the carrier, and fix `sigma>0`.  For the formal
center carrier, the unit-count sampling argument applied to all pairs of
depth at most

```text
beta_* =alpha*d_(a,b)-sigma                          (6.8)
```

bounds their complete positive Gram operator by

```text
X^(beta_*+o(1))*L^O(1)
 =o(X^(alpha*d_(a,b))).                              (6.9)
```

They need not be interpolated individually.  Only the rows of depth
`>beta_*` enter the confluent gate.  Classical horizontal zero-density
estimates make their global number `o(N)` for fixed parameters, but do not
prevent all `O(L)` rows allowed by (6.2) from lying in the one local group
containing the target.  Thus this reduction saves the shallow population
without resolving the local problem.

For the reduced carrier, replace `d_(a,b)` by `d_*` throughout
(6.8)--(6.9).

An exact zero-side closure statement is:

> For the deepest pair in the carrier, group all other off-line pairs in a
> collision-stable basis and prove that the inhomogeneous positive-row
> system generated by the short seed has a solution in the free lobe with
> coefficient cost `X^o(1)`, while its selected negative coordinate retains
> `X^(alpha*d_(a,b)/2-o(1))`.

The regularized Birman--Schwinger formulation is equivalent: at the proposed
carrier scale `K`, derivative directions whose matched Gram weight is below
`K` must be merged, while the remaining grouped directions must satisfy the
target-conditioned Schur inequality.  Neither a raw least singular value nor
the first two global moments proves this assertion.

At the formal center carrier `X^(alpha*d_(a,b))` with `d_(a,b)>2/3`, the
power-length `k=3` island is already a counterconfiguration to this grouped
statement.  No current **zero-side-only** counterconfiguration is known to
violate the reduced carrier statement at a fixed separation `d_*<2/3`.
After adjoining the completed aggregate arithmetic row, however, the exact
one-pair quotient is already target-aligned and refutes a universal
augmented-angle statement on the abstract operator class.  The selected
block is also realized exactly by two normalized compact-support
Paley--Wiener packets, and to superpolynomial accuracy with all growing
endpoint jets on the finite Gabor grid; see
[`ZETA23-ASYMMETRIC-PW-MIRROR-BLOCK-REALIZATION-AUDIT-2026-08-12.md`](ZETA23-ASYMMETRIC-PW-MIRROR-BLOCK-REALIZATION-AUDIT-2026-08-12.md).
For actual zeta, whether collateral rows provide a transverse reservoir is
unknown.  This is the first coupled gate after the corrected regular-lattice
audit.

## 7. The prime form is one target-aligned aggregate

Fixing the short seed makes the **entire** cross-prime form one
complex-linear functional of the free lobe.  For one negative Weil witness,
only its real part must be controlled.  Thus the pointwise prime conditions
counted in (2.6)--(2.7) are a sufficient overconstraint, not an intrinsic
second gate.

If one nevertheless imposes all pointwise prime nulls, independent
polarization gives

```text
h_k=conj(ell_k)*r_k,
inf ||ell||_2*||r||_2=sum_k abs(h_k).                (7.1)
```

so that optional stronger route is again a Wiener-`l^1` extremal.  Its dual is the
`l^infinity` distance from the asymmetric Laplace carrier vector to the span
of the active prime-log evaluation vectors.  The audited KMT quadrature gives
only a logarithmic upper approximation error; it does not give the matching
subpower lower bound needed to retain the carrier.

The minimal formulation adjoins instead the single completed aggregate row
to the grouped zero system and asks for the augmented target angle.  By the
operator identity `K_comp=K_zero`, that row contains the selected negative
target itself.  The one-pair quotient makes them exactly parallel.  Thus
the reduction from many prime rows to one equation simplifies the count but
does not supply the angle; this is the coupled gate in Section 8.

There is an equivalent direct arithmetic warning.  At the asymmetric center
put

```text
Y=X^d,              d=d_(a,b)=1-(a+b)/2.            (7.2)
```

The hypothetical depth-`alpha` residue itself has size `Y^alpha`.  A direct
uniform estimate for the completed centered von Mangoldt polynomial of the
form

```text
S_(Y,W)(gamma)=o(Y^alpha)
```

or even `O(Y^(alpha-sigma))` with fixed `sigma>0`, is therefore already the
desired strip-strength residue estimate at that hypothetical ordinate.  It
is not a routine consequence of exponent-pair bounds.  The audited KMT input
gives only the much larger square-root-scale transition estimate and a
logarithmic atomic approximation error.  Cross-prime nulling is an attempt
to avoid assuming this direct residue bound; it does not prove it for free.

## 8. Conditional implications and the exact next target

### Formal implication 8.1 (`5/6`, with a bulk-refuted premise)

Fix `alpha>1/3+epsilon` and choose `a,b` as in (3.3).  If one assumes a
uniform target-conditioned theorem retaining (3.1), together with the
corresponding Wiener-atomic prime bound, then (3.1) dominates (3.2) and the
completed remainders.  Formally this gives the right edge (1.5).

This implication is arithmetically correct but is **not** a viable theorem
from the present hypotheses: the power-length varying-depth `k=3` island
already refutes its zero-side premise whenever `d_(a,b)>2/3`.  In particular,
the point-packet identity of Lemma 5.1 cannot be used to certify (3.1) for
that island, because its finite-width normalization loses a fixed power.

### Conditional theorem 8.2 (formal `7/8` certificate)

Fix `alpha>3/8+epsilon`.  Choose fixed parameters `a>1/2` and `d_*<2/3`, as
close to `1/2` and `2/3`, respectively, that (3.6) has a fixed positive
margin; choose `b=o(1)` satisfying (2.9).  Assume uniformly for every
hypothetical deepest core pair that:

1. fixed-width packets centered at the two points below (3.4) have remote
   leakage `o(X^(alpha*d_*))`;
2. the grouped/confluent zero-row system has subpower target-conditioned cost
   and retains the selected response (3.5); and
3. after adjoining the single real completed arithmetic aggregate (or a
   convenient stronger complex row), the **same** solution retains the
   target and the completed arithmetic lower edge has subcarrier error.

Then (3.5) dominates the same-lobe prime term (3.2) and all completed
remainders.  The resulting zero-side upper and arithmetic-side lower bounds
contradict the exact completed explicit formula.  These hypotheses would
give the conditional right edge `7/8+epsilon`.

This theorem is still conditional: items 2 and 3 are open, and no assertion
about an actual zeta zero follows.  Moreover, when item 3 is quantified over
actual offending zeta pairs, the full package is truth-value equivalent to
the `7/8+epsilon` strip: the package excludes every such pair, while the
strip makes the universal condition vacuous.  Under a nonvacuous universal
quantifier over the current abstract operator class, item 3 is false.  In
the exact one-pair quotient the completed aggregate row is parallel to the
selected negative target; even the minimal real aggregate equation cancels
the useful target quadrature.  The normalized PW/Gabor realization of this
selected block does not realize the actual von Mangoldt aggregate.  See
[`ZETA23-ASYMMETRIC-PW-MIRROR-BLOCK-REALIZATION-AUDIT-2026-08-12.md`](ZETA23-ASYMMETRIC-PW-MIRROR-BLOCK-REALIZATION-AUDIT-2026-08-12.md)
and
[`ZETA23-CONDITIONAL-SEVEN-EIGHTHS-LOGIC-AUDIT-2026-08-12.md`](ZETA23-CONDITIONAL-SEVEN-EIGHTHS-LOGIC-AUDIT-2026-08-12.md).

What is proved unconditionally here is narrower but useful:

1. the exact dimension and both power ledgers, formal (1.4) and reduced
   (3.6), are consistent;
2. separated exact-density `k=2` rows cross their period precisely at
   `a=1/2`;
3. the periodic mirror is exact in the point model and has an `X^o(1)` finite
   realization for the polylogarithmic `k=2` island, but not for the
   power-length varying-depth `k=3` island; and
4. below the `k=3` cap, collision-stable aperiodic grouping and the single
   target-aligned completed aggregate form one coupled, strip-strength gate.
