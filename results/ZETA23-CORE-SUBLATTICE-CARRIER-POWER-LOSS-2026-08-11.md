# A count-compatible core sublattice with fixed carrier power loss

Status: exact collision-free counterconfiguration to a near-full-pair carrier
rate, 2026-08-11.  With only Riemann--von Mangoldt discrepancy and
unit-window counts, the strongest member displayed below is `k=3` and loses
the power `alpha/3`.  After also imposing the proved simple-critical-line
density, `k=3` is inadmissible but `k=7` remains admissible and loses the
fixed power `alpha/7`.  The distinguished pair lies at the center of the
modulation interval.

## 1. Verdict

There are reflection-invariant configurations satisfying the two stated
count bounds which

1. have total point multiplicity at most `dim V_m`;
2. satisfy the Riemann--von Mangoldt interval discrepancy with error `O(1)`
   and the unit-window count `O(log T)`;
3. contain a collision-free off-line pair of fixed depth `alpha` at `3T/2`;
   and
4. nevertheless satisfy, in the exact isolated-zero normalization,

```text
0 < K=-lambda_min(H_C)
  <= (10/3+o(1))*X^(2*alpha/3).                        (1.1)
```

Since `L=X^o(1)`, this is equivalently

```text
K <= X^(alpha-alpha/3+o(1))/L.                        (1.2)
```

In the matched notation `K=(X^alpha/L)*r_T`, the exact implication is

```text
r_T <= (10/3+o(1))*L*X^(-alpha/3).                   (1.3)
```

Thus a universal theorem based only on the stated counts cannot have

```text
K >= X^(alpha-theta+o(1))/L
```

with `theta<alpha/3`.  In particular, the hoped-for
`K>=X^(alpha-o(1))/L` is false even for a core pair and even without
collisions.

There is an important second ledger.  The currently imported zero-side
input also gives a lower density

```text
C_0=3/2-(1/sqrt(2))*cot(1/sqrt(2))
   =0.6725007036...                                   (1.4)
```

of simple critical-line zeros.  The `k=3` construction has on-line fraction
only `1-2/3=1/3` and violates this theorem.  The least integer sublattice
parameter satisfying

```text
1-2/k > C_0
```

is `k=7` (equivalently, `2/3<C_0<5/7`).  The same proof then gives a
counterconfiguration compatible with all current zero-count and density
inputs, with

```text
0<K <= (26/7+o(1))*X^(6*alpha/7),
r_T <= (26/7+o(1))*L*X^(-alpha/7).                   (1.5)
```

Thus, after enforcing the simple-line density, the rigorous fixed loss is
`theta=alpha/7`, rather than `alpha/3`.  The separate distinct-zero lower
density imposes no further restriction because every point in the
construction is simple and distinct.

The cutoff `k=7` does not depend on a decimal approximation.  Put
`x=1/sqrt(2)`.  Positivity of the omitted Maclaurin terms gives

```text
tan(x)>x+x^3/3+2*x^5/15=(6/5)*x,
```

so `x*cot(x)<5/6` and `C_0>2/3`.  Conversely the alternating Taylor bounds

```text
sin(x)/x <= 1-x^2/6+x^4/120=441/480,
cos(x)   >= 1-x^2/2=3/4
```

give `tan(x)/x<14/11`, hence `x*cot(x)>11/14` and `C_0<5/7`.

The counts-only construction uses one depth-`alpha` reflected pair every
third sharp coordinate spacing.  The count-and-density construction uses
every seventh spacing.  On-line atoms fill the remaining density and add a
positive semidefinite form.  A bilinear Poisson identity shows that the
`k`-sublattice can couple time points separated by at most `(1-1/k)L`;
hence its signed norm has scale `exp(alpha*(1-1/k)*L)`, rather than the
isolated-pair scale `exp(alpha*L)/L`.

This also identifies why a subcritical grouped Paley--Wiener interpolation
constant is not by itself enough for the requested rate.  The strict density
surplus concerns **all direct nodes**.  The count hypotheses allow a fixed
positive fraction of those nodes to be on-line, while the hyperbolic nodes
alone occupy the lower-density sublattice in Lemma 3.1.  Stable interpolation
can preserve the negative inertia without forcing its coefficient-metric
edge to retain the full isolated-pair exponent.

## 2. Setup and normalization

Use the notation

```text
l      = log(T/(2*pi)),
ell_1  = l+2*log(2)-1,
L      = ell_1+eta,
X      = exp(L),
h      = 2*pi/L,
d      = floor(T*L/(2*pi)),
n      = d-m.
```

Assume

```text
eta*T >> sqrt(T)*l,
eta=o(l),
exp(eta)*log(l)/l -> 0,                               (2.1)
```

and use fixed constants `mu,nu>0`, `mu+nu<1`, with

```text
m = (mu+o(1))*eta*T/(2*pi),
D = (nu+o(1))*eta*T/(2*l).                            (2.2)
```

Let `V_m` be the real endpoint-jet subspace of the sharp coefficient space,
with its inherited coefficient `ell^2` norm.  Center the coordinate grid at
`tau_c` and write

```text
p_c(t)=sum_k c_k*exp(-i*(tau_k-tau_c)*t).
```

Then

```text
F_c(gamma-i*alpha)
 = integral_(-L/2)^(L/2)
     p_c(t)*exp(alpha*t)*exp(i*(gamma-tau_c)*t)dt.     (2.3)
```

Every reflected pair has multiplicity one and contributes

```text
(2/L^2)*Re(F_c(gamma-i*alpha)^2).                     (2.4)
```

Equation (2.4) is the coefficient `ell^2` and `1/L^2` normalization from the
quantitative signed-carrier reduction.  No row is duplicated: a reflected
pair costs two points and one hyperbolic plane.

## 3. Exact sublattice identity

The following lemma is stated for the full sharp coefficient space.  It
therefore remains true after restriction to `V_m`.

### Lemma 3.1 (one pair every `k` coordinate spacings)

Fix an integer `k>=2`, put

```text
P=L/k,
s=2*pi/P=k*h,
gamma_j=tau_c+beta+j*s,             j in Z,
```

and place a depth-`alpha` reflected pair at every `gamma_j`.  Let
`H_(k,infinity)` be the sum of their normalized signed forms.  Then, for
every real coefficient vector `c`,

```text
abs(c^T*H_(k,infinity)*c)
 <= (2/k)*sum_(q=-(k-1))^(k-1) exp(alpha*q*L/k)
       *||c||_2^2
 <= (2*(2k-1)/k)*X^(alpha*(1-1/k))*||c||_2^2.         (3.1)
```

#### Proof

Set

```text
g_c(t)=1_[-L/2,L/2](t)
       *p_c(t)*exp(alpha*t)*exp(i*beta*t).
```

For

```text
F_j=F_c(gamma_j-i*alpha)
```

the bilinear Poisson/Parseval identity at spacing `s=2*pi/P` is

```text
sum_(j in Z) F_j^2
 = P*sum_(q in Z) integral_R g_c(t)*g_c(q*P-t)dt.      (3.2)
```

The series is well defined by the `ell^2` Fourier-coefficient pairing; in
fact `sum_j abs(F_j)^2<infinity`.  Since `g_c` is supported on an interval of
length `L=kP`, the terms `abs(q)>=k` have intersection of measure zero or
are empty.  For `abs(q)<=k-1`,

```text
integral g_c(t)*g_c(q*P-t)dt
 = exp(alpha*q*P)*exp(i*beta*q*P)
   *integral p_c(t)*p_c(q*P-t)dt.                     (3.3)
```

Translation, reflection, restriction to the overlap, and Cauchy--Schwarz
give

```text
abs(integral p_c(t)*p_c(q*P-t)dt)
 <= ||p_c||_2^2
 = L*||c||_2^2.                                       (3.4)
```

The last equality is exact orthogonality of the sharp coordinate
exponentials.  Finally,

```text
c^T*H_(k,infinity)*c=(2/L^2)*Re(sum_j F_j^2).
```

Substituting (3.2)--(3.4) and `P=L/k` proves (3.1).  QED

For `k=3`, Lemma 3.1 gives the counts-only bound

```text
lambda_min(H_(3,infinity))
 >= -(10/3)*X^(2*alpha/3).                            (3.5)
```

The pair point density is

```text
2/s=L/(3*pi),                                         (3.6)
```

which is strictly below the zeta-zero density throughout the dyadic carrier
for all sufficiently large `T`.

For `k=7`, the corresponding count-and-density statements are

```text
lambda_min(H_(7,infinity))
 >= -(26/7)*X^(6*alpha/7),                            (3.7)

pair point density = L/(7*pi).                       (3.8)
```

## 4. Finite carrier and endpoint-jet tail

Choose `beta` so that one of the ordinates `gamma_j` is exactly `3T/2`, and
retain only the pairs with ordinates in

```text
J_D=(T-D,2T+D].
```

Write their form as `H_(3,J)` and the omitted-pair form as `H_out`, so that

```text
H_(3,J)=H_(3,infinity)-H_out.                         (4.1)
```

For `c in V_m`, the endpoint-jet estimate with the actual depth `alpha`
gives

```text
abs(F_c(gamma-i*alpha))
 <= L*X^(alpha/2)
       *(W/abs(gamma-tau_c))^m*||c||_2,               (4.2)
```

where `W=T/2+O(h)`.  The omitted lattice has `O(L)` ordinates per unit
interval.  Summing (4.2) outside `J_D` yields

```text
||H_out|V_m||
 <= C*L*X^alpha*(1+(W+D)/m)
       *(W/(W+D-O(h)))^(2m)
 = o(1).                                              (4.3)
```

The last equality follows from (2.1)--(2.2), because the decisive negative
logarithm is a positive constant times `eta^2*T/l`, while
`alpha*L+O(log T)=O(l)`.

Combining (3.5), (4.1), and (4.3) gives

```text
lambda_min(H_(3,J)|V_m)
 >= -(10/3+o(1))*X^(2*alpha/3).                       (4.4)
```

## 5. Completing the exact Riemann--von Mangoldt count

Put

```text
rho_T(t)=(1/(2*pi))*log(t/(2*pi)),
sigma_T(t)=rho_T(t)-L/(3*pi),            t in J_D.    (5.1)
```

Because `eta=o(l)`, uniformly on `J_D`,

```text
sigma_T(t)
 = (3*log(t/(2*pi))-2*L)/(6*pi)>0                    (5.2)
```

eventually.  The retained off-line lattice has point-count discrepancy at
most two from the constant density `L/(3*pi)`: every lattice ordinate
carries the two points of one reflected pair.  Fill the remaining density
with simple on-line atoms placed at the quantiles of `sigma_T`.  Quantile
rounding at the two ends can be chosen so that, for every interval
`I subset J_D`, the completed configuration `C_T` satisfies

```text
#(C_T cap I)=integral_I rho_T(t)dt+O(1),              (5.3)
#(C_T cap [x,x+1])=O(l).                              (5.4)
```

Choose the lattice offset and the quantile offset generically to avoid an
unused real sine-grid point.  All multiplicities are one.  The configuration
is reflection invariant and collision-free, and it contains the core pair at
`3T/2`.  The quantile construction does not assert a lower separation for
the union of the pair lattice and the on-line atoms.

Its total point multiplicity is

```text
#C_T
 = T*ell_1/(2*pi)+D*l/pi+O(D+D^2/T+1).
```

As in the exact cardinal budget,

```text
n-#C_T
 = (1-mu-nu+o(1))*eta*T/(2*pi)>0.                    (5.5)
```

Hence `#C_T<=dim V_m`.  Cauchy--Vandermonde surjectivity gives at least one
negative direction.  The added on-line atoms form a positive semidefinite
matrix `P_on`, so

```text
H_C=H_(3,J)|V_m+P_on
```

and (4.4) proves (1.1).

### 5.1 Current count-and-density specialization

For the version which also obeys the simple-critical-line density theorem,
repeat Sections 4--5 with `k=7` and

```text
sigma_(T,7)(t)=rho_T(t)-L/(7*pi)>0.                   (5.6)
```

The pair point fraction is

```text
(L/(7*pi))/rho_T(t)=2/7+o(1),                         (5.7)
```

uniformly on the dyadic carrier, so the simple on-line fraction is
`5/7+o(1)>C_0`.  All points have multiplicity one, hence the distinct-zero
fraction is one.  The interval discrepancy, unit-window bound, cardinal
budget, generic nonblindness, and positive-semidefinite filler argument are
unchanged.  Lemma 3.1 and the same `o(1)` omitted-lattice tail give exactly
(1.5).

## 6. Exact implication for the missing theorem

The construction proves a fixed power loss without using collisions,
uncontrolled multiplicities, or a raw interpolation singular value.  It
respects both the collision weights and the coefficient normalization.

For a uniform depth threshold `delta>0`, take `alpha=delta`.  Then the
counting hypotheses alone are compatible with

```text
K <= X^(2*delta/3+o(1))/L.                            (6.1)
```

Therefore they cannot prove a lower bound with exponent greater than
`2*delta/3`, or equivalently with loss `theta<delta/3`.

More generally, the same construction with one pair every `k>=3`
coordinate spacings gives

```text
K <= X^(alpha*(1-1/k)+o(1))/L.                        (6.2)
```

The `k=3` construction is the strongest member of this simple
counts-only family.  Once the simple-critical-line density (1.4) is imposed,
the strongest admissible integer member is `k=7`, and (6.2) becomes

```text
K <= X^(6*alpha/7+o(1))/L.                            (6.3)
```

For a uniform threshold `alpha=delta`, all current zero-count and density
inputs therefore preclude a count-derived lower bound with loss
`theta<delta/7`.  They leave
open all of the following:

```text
a counts-only core lower bound with loss theta>=alpha/3;
a current-count-and-density core lower bound with loss theta>=alpha/7;
a stronger bound using zeta-specific arithmetic beyond zero counts;
and a different legal screening construction with still larger power loss.
```

## 7. Hostile audit of the tempting `k=2` thinning

The exact `k=2` lattice has pair point density `L/(2*pi)`, just above the
Riemann--von Mangoldt density.  It cannot simply be used and completed by
positive on-line atoms.  The obvious repair is to delete a regularly spaced
fraction

```text
p=(L-log(t/(2*pi)))/L=(eta+O(1))/L.                  (7.1)
```

of its pairs.  This repair does **not** preserve the `X^(alpha/2)` Poisson
bound.

This near-full thinning is relevant only to the counts-only ledger.  Under
the simple-critical-line theorem, at most `1-C_0` of all zero points may be
put into off-line pairs in an artificial worst case.  Thus at least a
`C_0>2/3` fraction of the `k=2` pairs must instead be removed and replaced by
simple on-line atoms.  The count-and-density ledger therefore rules out a
near-full `k=2` configuration before any Poisson estimate; the integer uniform
sublattice first compatible with that ledger is `k=7`.

For the constant-density model, delete every `q`th pair from the `k=2`
lattice.  The required thinning obeys
`q^(-1)=O((eta+1)/L)=o(1)`, and hence `q -> infinity`.  If `H_2` is the full
`k=2` form and `H_(2q,beta)` is the deleted coset, then exactly

```text
H_retained=H_2-H_(2q,beta).                           (7.2)
```

Lemma 3.1 gives

```text
||H_2|| <= 3*X^(alpha/2),
||H_(2q,beta)||
 <= (4+o(1))*X^(alpha*(1-1/(2q)))
 = X^(alpha-o(1)).                                    (7.3)
```

This is not merely a wasteful comparison caused by merging the two Poisson
formulas.  In the formula for the deleted coset, the alias

```text
r=2q-1,
r*L/(2q)=L-L/(2q)                                    (7.4)
```

has nonzero coefficient and has no counterpart in the full `k=2` formula,
whose only nontrivial aliases are at `+-L/2`.  Thus the first periodic hole
reintroduces an endpoint-overlap term at the near-isolated exponent
`X^(alpha*(1-1/(2q)))`.  Edge blocks have the same defect at each block
boundary.

Consequently regular thinning supplies no rigorous upper bound better than
`X^(alpha-o(1))`; in particular it does not strengthen (1.5) to a loss
`alpha/2`.  To turn (7.4) into a matching lower bound for the negative edge
after endpoint-jet compression requires a quantitative concentration
estimate on the overlap interval of length `L/(2q) asymp eta`.  That extra
lower-bound step is not proved here.  Hence this audit closes the **obvious
periodic-deletion proof**, but does not claim that every nonperiodic or
depth-varying thinning scheme is impossible.
