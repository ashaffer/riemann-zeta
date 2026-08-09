# R166 mixed-product support amplifier and collective-cofactor gate

## Status

Let `q` be a fixed even integer and let

```text
F_j(s)=1+U_j(s),             1<=j<=q,                    (0.1)

U_j(s)=sum_(n>H)u_j(n)n^(-s),       u_j(n)>=0.           (0.2)
```

The mixed product

```text
V(s)=product_(j=1)^q U_j(s),
P(s)=1-V(s),
B(s)=P'(s)/P(s)                                             (0.3)
```

has the same `H -> H^q` support amplification as R153's diagonal power,
and `B` has nonnegative Dirichlet coefficients.  If the channels share a
zeta carrier,

```text
F_j=Z A_j/D_j,                                            (0.4)
```

then

```text
P=Z C/product_j D_j                                      (0.5)
```

for one explicit collective cofactor `C`.  In the diagonal specialization
this cofactor splits into R153's `q-1` fixed-value factors.  For genuinely
independent channels it is instead the multivariate hypersurface

```text
product_j(F_j-1)=1.                                      (0.6)
```

This distinction matters.  R155 still forces individual `F_j=2` points
(or extra channel zeros), but those points do not force (0.6).  Applying
R155 to `P` itself merely forces the harmless value

```text
P=2  iff  product_j U_j=-1,                              (0.7)
```

which is not a pole of `P'/P`.  Explicit local analytic models exist for
every even `q` with distinct channels, zero-free individual multipliers,
and no collective zero except the common target.  Thus fixed-value Montel
does **not** close the independent mixed-product route.  R165 nevertheless
shows that a bridge-wide safe family cannot have normal multiplier ratios
and cannot arise from a fixed global entire exponential identity.  Any
successful realization must pay a growing ratio-value cloud; whether that
cloud fits within the outer ledger below is still open.

The conditional exponent ledger is also favorable.  If the analytic outer
remainder has size `H^(lambda+o(1))`, the usual right-center geometry closes
provided

```text
q>2 lambda log(2d/r)/[r log(R/d)].                       (0.8)
```

At completed log-conductor `O(H)`, `lambda=1`.  For optional Euler controls
through `Y=H^kappa` and a localization disc whose left penetration past one
is `a=R-r`, the natural boundary ledger is

```text
Y^(a+o(1))=H^(kappa a+o(1)),                             (0.9)
```

so `lambda=kappa a`.  A fixed even `q` can still cross the formal exponent
gate.

No strip follows yet.  The exact remaining condition is a quantitative
zero-free/lower-bound theorem for `C` on the complete localization disc.
R163 gives local optional-prime shaping, while R164 and Section 6 below show
that the desired algebra is feasible.  Neither supplies bridge-wide control
of the arithmetic cofactor.

```text
mixed H -> H^q support amplification                     EXACT
nonnegative coefficients of P'/P                         EXACT
common-zeta factor and one collective cofactor            EXACT
fixed-q conductor/divisor ledger                         LINEAR
conditional high-jet closure at log conductor O(H)        THEOREM
conditional optional-cutoff exponent ledger              THEOREM
R155 individual fixed-value obstruction                   EVADED
R165 normal-ratio/global-entire shortcut                   CLOSED
local distinct-channel analytic template                  THEOREM
quantitative nonnormal ratio cloud within outer budget     OPEN
arithmetic collective-cofactor lower bound                OPEN
fixed uniform zeta zero-free strip                        NOT PROVED
zeros approaching Re(s)=1                                 NOT PROVED
```

Date: 2026-08-08.

Predecessors:
[`R153-NONLINEAR-SUPPORT-AMPLIFIER-AND-MIXED-VALUE-GATE.md`](R153-NONLINEAR-SUPPORT-AMPLIFIER-AND-MIXED-VALUE-GATE.md),
[`R155-NORMAL-FAMILY-MIXED-VALUE-INEVITABILITY-GATE.md`](R155-NORMAL-FAMILY-MIXED-VALUE-INEVITABILITY-GATE.md),
[`R163-PRIME-BLOCK-LIFT-AND-RANDOM-SIGN-ROUNDING-GATE.md`](R163-PRIME-BLOCK-LIFT-AND-RANDOM-SIGN-ROUNDING-GATE.md),
[`R164-EXPLICIT-Z-PLANE-COLLECTIVE-COFACTOR-TEMPLATE.md`](R164-EXPLICIT-Z-PLANE-COLLECTIVE-COFACTOR-TEMPLATE.md),
and
[`R165-NONLINEAR-SAFE-FIBER-AND-GLOBAL-ENTIRE-GATE.md`](R165-NONLINEAR-SAFE-FIBER-AND-GLOBAL-ENTIRE-GATE.md).

## 1. Exact support and coefficient positivity

### Theorem 1.1

Under (0.1)--(0.2), `B=P'/P` has an absolutely convergent Dirichlet series
with nonnegative coefficients wherever `V` converges absolutely and
`|V|<1`.  Its nonconstant support is contained in

```text
{n:n>H^q}.                                                (1.1)
```

### Proof

Dirichlet convolution gives

```text
V(s)=sum_(n>H^q)v(n)n^(-s),       v(n)>=0.               (1.2)
```

because every contributing integer is a product of `q` integers, each
strictly larger than `H`.  Moreover

```text
-V'(s)=sum_(n>H^q)v(n)log(n)n^(-s).                      (1.3)
```

Since `P'= -V'`, the geometric expansion gives

```text
B(s)=[-V'(s)]/[1-V(s)]
    =[-V'(s)]sum_(k>=0)V(s)^k.                           (1.4)
```

Every coefficient in (1.4) is nonnegative.  The factor `-V'` already has
support beyond `H^q`; multiplication by further copies of `V` cannot lower
it.  QED.

This conclusion needs no equality among the channels.  Evenness of `q` is
not used for coefficients; it is used to retain the common zero in Section
2.

### Right-circle bound

Let

```text
s_*=1+r+i gamma,       r>0.                              (1.5)
```

On `|s-s_*|=r/2`, positivity gives

```text
|U_j(s)|<=U_j(1+r/2),
|U_j'(s)|<=-U_j'(1+r/2).                                 (1.6)
```

For the standard positive head-deleted Euler channels,

```text
U_j(1+r/2)+[-U_j'(1+r/2)]
       <=H^(-r/2+o(1))                                  (1.7)
```

uniformly for fixed `q`.  Hence

```text
|V(s)|<=H^(-qr/2+o(1)),
|-V'(s)|<=H^(-qr/2+o(1)),                                (1.8)
```

and, for large `H`,

```text
|B(s)|<=H^(-qr/2+o(1)).                                  (1.9)
```

Cauchy's inequality therefore gives

```text
|B^(k)(s_*)|/k!
 <=(2/r)^k H^(-qr/2+o(1)).                              (1.10)
```

The harmless factors `q` and powers of `log H` in differentiating the
tails are absorbed by `H^o(1)`.

## 2. Exact common-carrier factorization

Assume (0.4), where `Z,A_j,D_j` are holomorphic or meromorphic on the domain
under consideration and the displayed quotients are defined.  Then

```text
U_j=[Z A_j-D_j]/D_j.                                    (2.1)
```

Because `q` is even,

```text
product_j[Z A_j-D_j]=product_j[D_j-Z A_j].              (2.2)
```

Expanding the latter product gives the following exact theorem.

### Theorem 2.1 (one collective cofactor)

Put

```text
C=
 sum_(emptyset!=S subset {1,...,q})
 (-1)^(|S|+1) Z^(|S|-1)
 [product_(j in S)A_j][product_(ell notin S)D_ell].      (2.3)
```

Then

```text
P=Z C/product_j D_j,                                    (2.4)

B=Z'/Z+C'/C-sum_j D_j'/D_j.                             (2.5)
```

In particular, at a zero `rho` of `Z`,

```text
C(rho)=sum_(j=1)^q A_j(rho)
                    product_(ell!=j)D_ell(rho).          (2.6)
```

If the factors in (2.6) are finite and its sum is nonzero, `P` has exactly
the same multiplicity at `rho` as `Z`.

### Proof

The numerator of `P` is

```text
product_j D_j-product_j(D_j-ZA_j).                      (2.7)
```

Its subset expansion is `ZC`, proving (2.3)--(2.4).
Logarithmic differentiation proves (2.5), and setting `Z=0` in (2.3)
leaves exactly the singleton subsets, proving (2.6).  QED.

For odd `q`, every common zero has `U_j=-1`, so `P=1-(-1)^q=2`; the carrier
is not retained.  The parity condition is therefore essential.

### Diagonal specialization

If all `F_j=F=N/D`, then (2.4) is exactly

```text
P=1-(F-1)^q,                                             (2.8)
```

and `C` factors into the `q-1` root-of-unity mixed factors in R153.  Thus
the mixed product is new only when the channels are genuinely independent.

## 3. Divisor and outer-growth ledger

For a fixed `q`, the cofactor (2.3) has only `2^q-1` terms and each term is
a product of at most `q-1` copies of `Z` and one choice of `A_j` or `D_j`
for every channel.  The elementary Nevanlinna inequalities therefore give,
on every fixed enlarged localization domain,

```text
T(C)
 <<_q (q-1)T(Z)+sum_j[T(A_j)+T(D_j)]+1.                 (3.1)
```

After the usual completion of fixed-degree `L`-data, this is

```text
O_q(1+sum_j log Q_j+log(|gamma|+3)),                     (3.2)
```

where `Q_j` denotes the relevant analytic conductor.  Hence the zero/pole
ledger in (2.5) remains linear in the log-conductors for fixed `q`; taking a
product has not exponentiated the completed divisor count.

Equation (3.1) is an upper characteristic, not a lower bound.  Cancellation
among the singleton terms in (2.6) can make the target multiplicity larger,
and cancellation on the boundary can make `C'/C` large even if `C` has no
zero in the localization disc.  A useful application must require either a
standard completed-function normalization which controls this conditioning,
or an explicit two-sided boundary bound for `C`.  This is part of the open
collective-cofactor gate, not something positivity supplies automatically.

### Optional finite-Euler ledger

Suppose instead that every varying multiplier is a finite Euler product
through

```text
Y=H^kappa                                                   (3.3)
```

with uniformly bounded local exponents.  Let the localization disc be
`|s-s_*|<=R` and put

```text
a=R-r,       so its left edge is Re(s)=1-a.              (3.4)
```

When `0<a<1/2`,

```text
sum_(p<=Y)p^(-(1-a))<<Y^(a+o(1)).                        (3.5)
```

Consequently the logarithmic boundary size of each multiplier, its inverse,
and every fixed-`q` term of `C` is

```text
O_q(Y^(a+o(1)))=O_q(H^(kappa a+o(1))).                  (3.6)
```

If `C` is zero-free and quantitatively conditioned on the enlarged disc,
the same exponent controls its logarithmic derivative remainder.  Merely
knowing that `C` has no zero is not enough for this last inference; a lower
boundary or one interior normalization is required.

## 4. Conditional high-jet closure

The following statement isolates the exponent implication without hiding
the cofactor hypothesis.

### Theorem 4.1

Suppose

```text
rho=1-delta+i gamma,
s_*=1+r+i gamma,
d=|s_*-rho|=r+delta,
d<R.                                                     (4.1)
```

For a sequence `H -> infinity`, assume:

1. (0.1)--(0.2) and the uniform tail bound (1.7) hold;
2. `P` has a simple zero at `rho`;
3. on `|s-s_*|<R`, write

   ```text
   B(s)=1/(s-rho)+G_H(s),                                (4.2)
   ```

   where `G_H` is holomorphic and

   ```text
   sup_(|s-s_*|=R)|G_H(s)|<=H^(lambda+o(1))              (4.3)
   ```

   for one fixed `lambda>0`.

If

```text
q>2 lambda log(2d/r)/[r log(R/d)],                       (4.4)
```

these hypotheses are inconsistent for all large `H`.

### Proof

Choose `beta` strictly between

```text
2 log(2d/r)/(qr)<beta<log(R/d)/lambda.                   (4.5)
```

For each sufficiently large `H`, take

```text
k=floor(log H/beta).                                      (4.5a)
```

Changing `k` by this bounded rounding error only changes the estimates
below by fixed factors.  From (4.2),
Cauchy's inequality, and (4.3),

```text
|B^(k)(s_*)|/k!
 >=d^(-k-1)-H^(lambda+o(1))R^(-k).                      (4.6)
```

The second term is `o(d^(-k-1))` by the upper inequality in (4.5).  On the
other hand, (1.10) is `o(d^(-k-1))` by the lower inequality in (4.5).  This
is a contradiction.  QED.

If finitely many fixed carrier zeros lie closer than `R`, the standard
nearest-pole power-sum lemma replaces (4.2) and selects derivative orders
with a bounded gap.  It does not alter (4.4).  The single-pole statement was
used only to display the implication without extra notation.

### Two scales

For completed fixed-degree channels with total log-conductor `O(H)`, the
standard outer ledger has `lambda=1`, so (4.4) becomes

```text
q>2 log(2d/r)/[r log(R/d)].                              (4.7)
```

For optional Euler controls through `Y=H^kappa`, (3.6) gives, conditional
on the stated cofactor conditioning,

```text
lambda=kappa(R-r).                                       (4.8)
```

The formal threshold is then

```text
q>2 kappa(R-r)log(2d/r)/[r log(R/d)].                    (4.9)
```

In either case a fixed even `q` exists for every fixed hypothetical zero and
fixed localization geometry.  These are conditional exclusion theorems,
not a proof that the required channels and cofactor bound exist.

## 5. Precise comparison with R153 and R155

R153 uses one channel and the diagonal power `1-U^q`.  Algebra factors its
artificial divisor into the scalar values

```text
F=1+omega,       omega^q=1.                              (5.1)
```

For useful even `q`, at least two of these values must be avoided to obtain
the clean target ledger.  R155 proves that such avoidance is incompatible
with a retained zero and right-cap convergence to one.

For the mixed product, the bad set is instead the single hypersurface

```text
(F_1-1)(F_2-1)...(F_q-1)=1.                             (5.2)
```

R155 has two consequences, neither fatal:

1. Applied to an individual `F_j` whose zero divisor stays bounded, it says
   that `F_j=2` must occur.  At such a point only `U_j=1`; equation (5.2)
   also needs `product_(ell!=j)U_ell=1`, which is not forced.
2. Applied to `P`, which tends to one on the right cap and retains the
   target zero, it says that bounded zero divisor forces `P=2` somewhere.
   By (0.3), this is `product_jU_j=-1`, a regular value of `B=P'/P`.

Thus the normal-family debt has been exported from a pole of the detector to
a harmless value.  No omission of two fixed scalar values is assumed, and
the logarithmic-lattice theorem does not give a collective zero.

This does not mean the cofactor is automatically zero-free.  It means only
that R155 is no longer a proof that it must vanish.  A new multichannel
arithmetic or topological theorem is required.  R165 sharpens this warning:
a safe bridge-wide family forces at least one multiplier ratio to be
nonnormal and to carry an unbounded prescribed-value cloud, and no fixed
global entire exponential identity supplies an escape.  Such a cloud can
still have polynomial outer growth, so R165 does not contradict Theorem 4.1;
it identifies a mandatory contribution to its open remainder bound (4.3).

## 6. Local analytic feasibility for every even q

There is no finite-dimensional holomorphic obstruction hidden in (5.2).
Here is an explicit construction.

For even `q`, write `w=z-1` and put

```text
L_(q-1)(w)=sum_(n=1)^(q-1)(-1)^(n+1)w^n/n,
P_q(z)=z exp[-L_(q-1)(z-1)].                             (6.1)
```

Then `P_q` has only the simple zero `z=0`, `P_q(1)=1`, and

```text
1-P_q(z)=(z-1)^q/q+O((z-1)^(q+1)).                      (6.2)
```

For `0<z<1`, the omitted tail in the logarithm is strictly negative, so
`P_q(z)<1`.  Hence there is a sufficiently thin simply connected
neighborhood `Omega_q` of the interval `[0,1]` in which `1-P_q` has only
the order-`q` zero at `1`.  Choose the holomorphic root

```text
a(z)^q=1-P_q(z),       a(0)=1.                           (6.3)
```

Let `h_1,...,h_q` be sufficiently small holomorphic functions on a slightly
larger neighborhood, with

```text
h_j(0)=0,       sum_j h_j=0,                             (6.4)
```

and choose them distinct.  Set

```text
F_j(z)=1-a(z)exp(h_j(z)),
U_j(z)=F_j(z)-1.                                         (6.5)
```

For zero perturbation, `1-a` has only the simple zero at `0`; by Rouche,
after shrinking the common size in (6.4), every `F_j` is

```text
F_j(z)=z m_j(z)                                          (6.6)
```

with `m_j` holomorphic and zero-free on a slightly smaller
`Omega_q`.  Also `F_j(1)=1`, and, exactly,

```text
product_j U_j
 =(-1)^q a^q exp(sum_jh_j)
 =1-P_q.                                                 (6.7)
```

Therefore the mixed detector is `P_q`, whose only zero is the common target
`z=0`.  This is a genuinely distinct-channel model for every even `q`.

The construction is local and makes no claim that the `F_j` have positive
Dirichlet coefficients.  Its role is decisive but limited: it proves that
normality, Waring geometry, and local divisor topology alone cannot close
the mixed-product cofactor premise.

For `q=2`, R164 supplies a larger explicit strip model.  If `r^2=1-z
exp(1-z)`, then

```text
F_+(z)=1-r(z)exp(h(z)),
F_-(z)=1-r(z)exp(-h(z))                                  (6.8)
```

have `1-(F_+-1)(F_--1)=z exp(1-z)`.  On a compact subdomain, small nonzero
`h` makes the channels distinct while preserving their sole common zero.

## 7. The remaining arithmetic theorem

The mixed product has removed one specific impossibility premise from R153.
What remains is concrete:

1. construct `q` independent positive head-deleted arithmetic channels with
   a common zeta carrier;
2. prove the target nondegeneracy (2.6);
3. prove that the collective cofactor (2.3) is zero-free and quantitatively
   conditioned on the complete localization disc; and
4. keep its boundary ledger at `H^(lambda+o(1))` with `q` satisfying (4.4).

R163 supplies substantial local freedom from signed optional primes, and
Section 6 provides compatible analytic templates.  R165 proves that any
safe bridge section must use quantitatively nonnormal multiplier ratios.
The gap is that R163's
filled microdiscs do not control the entire bridge from the retained zero to
the right circle used in Theorem 4.1.  Individual forced mixed points can
occur in that uncontrolled collar and may still create a collective zero.

Accordingly the next useful result is not another scalar `a`-point theorem.
It is a joint transversality or corona estimate for

```text
1-product_j(F_j-1)                                       (7.1)
```

under independently signed optional-prime controls, with a quantitative
boundary lower bound.  Until that estimate is proved, (4.4) is a calibrated
conditional closure rather than a fixed zero-free strip.
