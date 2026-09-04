# Same-state bipartite Blaschke splitting

Status: exact two-leg factorization theorem, exact fixed-finite-list compact
Paley--Wiener realization (including real high-carrier realization), and
sharp scope boundary, 2026-08-12.  The
selected positive-row constraint does **not** intrinsically force the square
of the full Blaschke product.  Splitting collateral annihilation between the
two endpoint legs pays one full product, and one full product is sharp
within the exact-annihilation architecture.  Growing-list compact transfer
and actual-zeta collateral isolation remain open.  No zero-free strip is
proved.

## 1. Verdict

The apparent factor-two obstruction came from putting every collateral zero
on the same endpoint branch.

For a collateral reflected pair, the exact form is a product of two scalar
evaluations.  It vanishes if **either** evaluation vanishes.  After grouping
repeated rows with the same two evaluation nodes, color every distinct
effective collateral condition red or blue:

```text
red j:   F(beta_j-i*delta_j)=0,
blue j:  F(-beta_j-i*delta_j)=0.                    (1.1)
```

Let `B_R(alpha),B_L(alpha)` be the corresponding right-half-plane
Blaschke attenuations at the selected depth.  A coherent two-endpoint state
can be scaled so that its selected positive row vanishes exactly.  Its
negative selected carrier is

```text
K_split
 asymp exp(alpha*D)/L^2
       *[B_R(alpha)^(-2)+B_L(alpha)^(-2)]^(-1).     (1.2)
```

Writing

```text
S_R=-log B_R(alpha),
S_L=-log B_L(alpha),                                (1.3)
```

the exponent loss in (1.2) is

```text
2*max(S_R,S_L)+o(L).                                (1.4)
```

The weights of the individual conditions are nonnegative.  Greedy
two-bin balancing gives

```text
|S_R-S_L|<=max_j w_j,
w_j=-log |(alpha-z_j)/(alpha+conj(z_j))|.           (1.5)
```

Consequently, whenever `max_j w_j=o(L)`,

```text
2*max(S_R,S_L)
 =sum_j w_j+o(L).                                   (1.6)
```

This is exactly the **one-product** ledger.  The same state satisfies the
selected positive-row quotient; no unequal-endpoint relaxation is used.

For every fixed polynomially conditioned collateral list, the construction
has an exact compact PW realization, all endpoint jets vanish, and the
finite Gabor transfer loses only `X^o(1)`.  A real physical packet is obtained
by adjoining the counterrotating conjugate band.  Reality then forces only
far companion roots at relative ordinate about `-2*gamma`; their total Hardy
potential is `O(M/gamma^2)`, not a second copy of the local potential.  In
particular the
`+/-pi/D` phase-flip pair may be split between the two legs and costs one
reciprocal-scale product rather than its square.

The result does not yet handle an arbitrary `Theta(L)` actual-zero list.
For that, the two growing Hardy cascades must both be compactly realized,
near-confluent rows must be grouped without paying once per row, and the
resulting state must be coupled to the arithmetic inequality.  Those are
quantitative gates, not a remaining algebraic factor of two.

## 2. Exact reflected-pair algebra

Put

```text
F_q(z)=integral q(t)*exp(z*t)dt,                    (2.1)

z_j^+=beta_j-i*delta_j,
z_j^-=-beta_j-i*delta_j.                            (2.2)
```

The complete reflected-pair compression, with every coherent mixed term
retained, is

```text
Q_j(q)
 =(2/L^2)*Re[F_q(z_j^+)*conj(F_q(z_j^-))].          (2.3)
```

For the selected pair `(alpha,0)`, write

```text
A=F_q(alpha),       B=F_q(-alpha).                  (2.4)
```

Then

```text
Q_0(q)
 =(1/(2*L^2))*(|A+B|^2-|A-B|^2).                   (2.5)
```

The selected positive-row quotient is exactly

```text
A+B=0.                                              (2.6)
```

On it,

```text
Q_0(q)=-(2/L^2)*|A|^2.                              (2.7)
```

Equation (2.3) supplies the bipartite freedom: `Q_j=0` follows from either
`F(z_j^+)=0` or `F(z_j^-)=0`.  Equation (2.6) couples the two endpoint
amplitudes only at the selected pair.  It does not require that every
collateral condition be imposed on both endpoints or on one preassigned
endpoint.

## 3. The abstract two-leg theorem

Separate the physical support into a right endpoint lobe and a left endpoint
lobe whose centers differ by `D=dL+O(1)`.  After factoring their endpoint
Laplace weights, let

```text
sigma_R>0, sigma_L>0                                (3.1)
```

be the largest selected evaluation magnitudes of unit local packets subject
to the red and blue zero conditions, respectively.  Thus the unnormalized
selected capacities are

```text
R_0=exp(alpha*D/2)*sigma_R,
L_0=exp(alpha*D/2)*sigma_L.                         (3.2)
```

First ignore exponentially small reverse-endpoint leakage; Section 5 puts
it back exactly.  Choose unit local packets `r,l` attaining the two
capacities.  For a common selected amplitude `a`, use coefficients

```text
c_R=a/R_0,
c_L=-a/L_0.                                         (3.3)
```

Then `A=a`, `B=-a`, so (2.6) holds.  Unit normalization gives

```text
1=|a|^2*(R_0^(-2)+L_0^(-2)),                        (3.4)

|a|^2
 =exp(alpha*D)
  *[sigma_R^(-2)+sigma_L^(-2)]^(-1).               (3.5)
```

Combining (2.7) and (3.5) proves

```text
-Q_0(q)
 =(2/L^2)*exp(alpha*D)
   *[sigma_R^(-2)+sigma_L^(-2)]^(-1).              (3.6)
```

This elementary harmonic-mean formula is the whole factor-two mechanism.
It uses one scalar coherent state, not a mixed state or a positive average.

### Theorem 3.1 (balanced two-leg Blaschke splitting)

Let `J_R disjoint_union J_L={1,...,M}`.  In the causal half-line endpoint
models impose

```text
G_R(z_j^+)=0       (j in J_R),
G_L(-z_j^-)=0      (j in J_L).                      (3.7)
```

The left nodes `-z_j^-=beta_j+i*delta_j` are the reflected right-half-plane
nodes.  Define

```text
r_j=
 |(alpha-(beta_j-i*delta_j))
   /(alpha+(beta_j+i*delta_j))|,

B_R=product_(j in J_R) r_j,
B_L=product_(j in J_L) r_j.                         (3.8)
```

The two causal extremizers are their finite Blaschke products times the
reproducing kernel at `alpha`, so

```text
sigma_R=B_R/sqrt(2*alpha),
sigma_L=B_L/sqrt(2*alpha).                          (3.9)
```

Therefore the exact half-line carrier is

```text
-Q_0(q)
 =exp(alpha*D)/(alpha*L^2)
  *[B_R^(-2)+B_L^(-2)]^(-1),                        (3.10)
```

up to the common endpoint-profile normalization convention.

If

```text
S_R=sum_(j in J_R)(-log r_j),
S_L=sum_(j in J_L)(-log r_j),                       (3.11)
```

then

```text
log(-Q_0(q))
 =alpha*D-2*max(S_R,S_L)-2*log L+O(1).             (3.12)
```

The `O(1)` is uniform when the endpoint profiles and depth collar are fixed.

#### Proof

For `Re z_j^+>0`, the factor

```text
b_j(s)=(s-z_j^+)/(s+conj(z_j^+))                   (3.13)
```

is inner on the right half-plane and has modulus `r_j` at `s=alpha`.
Multiplying the reproducing kernel by the product of the assigned factors
preserves its `H^2` norm and multiplies its target value by the assigned
`B`.  Reflection gives the same modulus for the left node.  Equations
(3.4)--(3.6) then give (3.10).  Taking logarithms gives (3.12).  QED

### Lemma 3.2 (greedy balance)

Given nonnegative weights `w_1,...,w_M`, assign them one at a time to the
currently lighter of two bins.  At the end,

```text
|S_R-S_L|<=max_j w_j.                               (3.14)
```

Indeed, immediately after the last assignment that changes which bin is
heavier, the excess is at most the weight just assigned; every subsequent
assignment goes to the lighter bin until the same argument repeats.

Since

```text
2*max(S_R,S_L)
 =sum_j w_j+|S_R-S_L|,                              (3.15)
```

(1.6) follows whenever `max_j w_j=o(L)`.

For reciprocal-separation nodes and, more generally, nodes at
`L^(-O(1))` distance from the selected evaluation, `max w_j=O(log L)`.
Thus the balancing discrepancy is subpower.

## 4. Sharpness inside the exact-annihilation architecture

The one-product loss is not only attainable; it is the best possible loss
for this architecture.

Suppose every collateral product in (2.3) is killed by assigning at least
one of its two scalar factors to an exact-zero endpoint leg.  Let `S_R,S_L`
be the total Hardy potentials placed on the two legs.  The sharp scalar
Hardy evaluation bound gives

```text
sigma_R<=C*exp(-S_R),
sigma_L<=C*exp(-S_L).                               (4.1)
```

The selected constraint (2.6) forces the two target evaluations to have the
same magnitude.  Hence (3.6) gives an exponent loss at least

```text
2*max(S_R,S_L)
 >=S_R+S_L.                                         (4.2)
```

The right side is the one-product potential.  Balanced splitting attains it
up to the discrepancy in (3.14).  Therefore:

```text
one branch for every row:     loss 2*(S_R+S_L),
balanced two-leg assignment:  loss   S_R+S_L+o(L),
less than one full product:   impossible here.      (4.3)
```

This is a factorization/index statement.  Each scalar Blaschke zero has
integer index and must be placed on at least one of the two isotropic legs.
Balancing distributes the total index; it does not take a non-existent
scalar half-zero.  Identical rows must be grouped before this count: one
scalar zero annihilates every repeated copy of the same row.

Adding formal vector channels does not improve (4.2) for the physical
reflected-pair form.  On a genuine direct sum the selected positive square
is

```text
sum_k |A_k+B_k|^2.                                  (4.4)
```

Its zero set imposes `A_k=-B_k` in every channel.  Every channel which
contributes target carrier must therefore pay its own assigned scalar Hardy
bill.  A matrix square root of a Blaschke product would require a different
off-diagonal channel coupling; it is not the scalar zeta PW compression.

### Lemma 4.1 (conditional real rank-two realization for real rows)

The branch polynomials in the balanced construction are generally complex.
There is a simple realification only when every row under consideration is
real symmetric in one common coefficient basis.

Write a normalized complex coefficient vector as

```text
q=u+i*v,                 u,v real,                  (4.5)
```

and define

```text
Gamma=u*u^T+v*v^T.                                  (4.6)
```

Then `Gamma>=0`, `Tr Gamma=||q||^2=1`, and for every real symmetric
compressed row matrix `K`,

```text
Tr(K*Gamma)=u^T*K*u+v^T*K*v=q^*K*q.                (4.7)
```

The selected positive row is real.  Hence `x^T*q=0` implies separately

```text
x^T*u=x^T*v=0,
range Gamma subset ker x.                           (4.8)
```

Equations (4.7)--(4.8) then preserve exactly the selected carrier, the
selected positive-row quotient, and every assigned collateral zero **whose
row matrix is real**.

This hypothesis is substantive.  An individual collateral kernel contains
`exp(-i*delta*(t-s))` and is generally complex Hermitian, not real
symmetric.  If `K=A+i*C`, with `A` real symmetric and `C` real
skew-symmetric, then

```text
q^*Kq=u^T*A*u+v^T*A*v-2*u^T*C*v,                  (4.8a)
```

while `Tr(K*Gamma)` omits the last term.  Hence (4.6) does not realify an
arbitrary list of individual collateral rows.  It applies, for example, to
a genuinely real `+/-delta` row sum.  A general complex Hermitian system
requires a doubled realification with off-diagonal blocks, whose admission
to the physical scalar zeta compression is not proved here.

### Lemma 4.2 (real high-carrier embedding)

Equation `F_q(conj z)=conj(F_q(z))` would apply if the **demodulated
envelope** `q` itself were real.  That is not the correct reality condition
for a packet centered at a large ordinate `gamma`.

Let `q in C_c^infinity(R)` be complex and put

```text
Q(z)=integral q(t)*exp(z*t)dt,

p_gamma(t)=exp(-i*gamma*t)*q(t)
          +exp(i*gamma*t)*conj(q(t)).               (4.9)
```

Then `p_gamma` is one real rank-one physical packet.  If `P_gamma` is its
bilateral Laplace transform, direct expansion gives the exact identities

```text
P_gamma(s)
 =Q(s-i*gamma)+conj(Q(conj(s)-i*gamma)),            (4.10)

P_gamma(z+i*gamma)
 =Q(z)+conj(Q(conj(z)-2*i*gamma)).                  (4.11)
```

Consequently a desired local zero at `z` is exact after imposing the two
envelope zeros

```text
z,             z#=conj(z)-2*i*gamma.                (4.12)
```

The selected positive row at the positive carrier is exact after imposing

```text
Q(alpha)+Q(-alpha)=0,
Q(alpha-2*i*gamma)=Q(-alpha-2*i*gamma)=0.           (4.13)
```

The two individual far zeros in the second line are stronger than needed;
one far affine equation would suffice.

For `z=beta-i*delta`, `0<beta<=alpha`, and
`abs(delta)<=gamma/2`, the companion in (4.12) has the same positive real
part after the appropriate endpoint reflection.  Its Hardy weight is

```text
w#
 =1/2*log(
   [((alpha+beta)^2+(2*gamma-delta)^2)]
   /[((alpha-beta)^2+(2*gamma-delta)^2)])
 =O(alpha*beta/gamma^2).                            (4.14)
```

The two selected far nodes in (4.13) obey the same estimate.  Hence `M`
local colored conditions acquire total additional potential

```text
S_far=O((M+1)/gamma^2).                              (4.15)
```

For the zeta carrier `gamma asymp T=exp(L)` this is `o(1)`, even for
`M=O(L)`.  It is not another copy of `S_R+S_L`.

Normalization also costs no exponent.  Direct expansion gives

```text
||p_gamma||_2^2
 =2*||q||_2^2
  +2*Re integral q(t)^2*exp(-2*i*gamma*t)dt,        (4.16)
```

and, for every `N`, integration by parts gives

```text
abs(integral q(t)^2*exp(-2*i*gamma*t)dt)
 <=(2*gamma)^(-N)*||(q^2)^(N)||_1.                 (4.17)
```

The fixed-list packets in Section 5 have derivative norms `exp(o(L))`, so
the last term is `X^(-N+o(1))`.  Equivalently, one may omit the explicit far
roots initially: every counterrotating evaluation is superpolynomially
small, and block Neumann inversion through the `exp(o(L))` local
interpolation inverse restores the physical zeros and selected row exactly.

After real normalization, the factor two in (4.16) cancels the factor two
from the `+/-gamma` conjugate carrier pair.  The carrier in (3.12) is
therefore unchanged up to `1+o(1)` and the negligible potential (4.15).

This proves real rank-one transfer for the fixed-list compact theorem in
Section 5.  Conjugation sends a local zero in the `+gamma` block to the
opposite `-gamma` block, a distance `2*gamma+O(1)` away.  It does **not**
send a relative `+delta` condition to relative `-delta` in the same block,
so physical reality does not force the two colors to agree.

It is not yet a growing-list compact theorem: although (4.15) is harmless,
for polynomial degree and interpolation dimension `Theta(L)` no uniform
Sobolev/counterrotating or inverse-Gram estimate is currently available.

## 5. Exact compact PW realization for a fixed list

The half-line theorem has a concrete compact realization when the number of
conditions is fixed and their interpolation cost is `X^o(1)`.

Choose a real-even

```text
phi in C_c^infinity((-w/2,w/2))                    (5.1)
```

and put translated packets at `+/-D/2`.  For a fixed partition define

```text
P_R(z)=product_(j in J_R)(z-z_j^+),
P_L(z)=product_(j in J_L)(z-z_j^-).                 (5.2)
```

The branch filters

```text
r_L=P_R(-partial_t)*phi(t-D/2),
l_L=P_L(-partial_t)*phi(t+D/2)                     (5.3)
```

have exact transforms

```text
F_(r_L)(z)=P_R(z)*exp(z*D/2)*Phi(z),
F_(l_L)(z)=P_L(z)*exp(-z*D/2)*Phi(z).               (5.4)
```

Thus the assigned dominant endpoint evaluation vanishes exactly.  The
opposite endpoint contributes an exponentially small leakage of relative
size `exp(-beta_0*D)`, where

```text
beta_0=min_j beta_j>0.                              (5.5)
```

Use a finite family of endpoint derivatives through an order at least the
number of assigned conditions on either branch (so
`max(|J_R|,|J_L|)` in the complex-envelope system) and solve simultaneously
for

```text
F_q(z_j^+)=0       (j in J_R),
F_q(z_j^-)=0       (j in J_L),
F_q(alpha)+F_q(-alpha)=0.                           (5.6)
```

For the real physical packet of Lemma 4.2, augment (5.6) by the companion
zero `conj(z)-2*i*gamma` for every assigned local zero `z`, together with the
two far selected zeros in (4.13), and enlarge the endpoint derivative
family to the resulting (still fixed) number of conditions.  This makes the
physical row equations exact by (4.11), before any limiting argument.  The far polynomial factors
may be normalized as

```text
(z-z#)/(alpha+conj(z#)).                            (5.6a)
```

Since `abs(z#) asymp gamma`, the corresponding differential operator is a
bounded zeroth-order multiplier plus `O(partial_t/gamma)` on every fixed
smooth packet.  Thus adjoining a fixed number of far roots does not insert
a hidden `gamma^M` norm loss.  Their target attenuation is exactly
`exp(-S_far)` with `S_far` bounded by (4.15).

Choose the seed so that `Phi` is nonzero on this fixed interpolation set.
After the endpoint exponentials and the nonzero row factors `Phi(z_i)` are
factored out, the derivative bases give (confluent) Vandermonde evaluation
blocks and the off-diagonal blocks at the collateral rows are
`O(exp(-beta_0*D))`.  Thus the rapid Fourier decay of `Phi` at the far roots
does not itself enter the interpolation condition number.  Confluent
divided differences handle collisions.
Whenever the inverse diagonal interpolation cost is `exp(o(L))`, block
Neumann inversion gives an exact solution whose correction to (5.3) is

```text
exp(-min(alpha,beta_0)*D+o(L)).                     (5.7)
```

Here the additional `alpha` accounts for the reverse-endpoint leakage in
the selected row.  Its target carrier is consequently (3.6) up to
`exp(o(L))`.

For every fixed list whose relevant target distances and confluent
conditioning are `exp(-o(L))`, the hypothesis holds.  Reciprocal-scale
nodes have only polynomial cost.  The compact packets lie strictly inside
the physical support, so every endpoint jet vanishes exactly.  The common
endpoint-flat cutoff and Fourier truncation used by the existing mirror
packet audit then transfer (5.6)--(5.7) to the finite Gabor grid with
`o(K_split)` error.  Exact finite-grid row projection restores (5.6) after
truncation.  For the real construction use the doubled symmetric
`+/-gamma` Gabor section and conjugate the two absolute-frequency bands;
the one-sided complex grid is its analytic half.  Projecting in this real
subspace restores the augmented system following (5.6) exactly.

This is an exact normalized scalar PW/Gabor construction.  The two packets
are components of one coherent function, and (2.3) retains all their mixed
terms.

For complex envelope coefficients this statement is literal.  Lemma 4.1
explains why the same-coordinate covariance `u*u^T+v*v^T` is not a valid
realification of individual complex `delta`-rows.  Lemma 4.2 supplies the
correct physical realification: adjoining the opposite carrier block and
including its small counter-rotating matrix in the fixed interpolation
solve gives one real rank-one compact packet with the same exponent and
exact physical row zeros.  This last conclusion is limited to the fixed,
`exp(o(L))`-conditioned family treated here.

### Corollary 5.1 (the reciprocal phase-flip pair)

For collateral gaps `delta=+/-pi/D` and depth
`beta=alpha-L^(-2)`, assign the `+` pair to the right leg and the `-` pair
to the left leg.  Each individual Hardy weight is

```text
w=log L+O(1).                                       (5.8)
```

The two bins are exactly balanced.  Hence the selected positive-row state
has

```text
-Q_0(q)
 =exp(alpha*D)*L^(-2+O(1/log L))/L^2                (5.9)
```

up to the common packet normalization.  The important invariant is the
power: the two conditions cost `L^(-2)` in the carrier, whereas putting both
on one endpoint costs `L^(-4)`.  Both are `X^(alpha*d-o(1))`, but only the
split ledger has the one-product exponent needed for a growing-list limit.

## 6. Growing lists: what transfers and what remains open

For `M=M_L` growing, Theorem 3.1 remains an exact causal Hardy theorem.  A
compact PW realization additionally needs enough physical room for both
causal cascades and a quantitative confluent grouping theorem.

For one leg with `m` roots of real part at least `a_0`, the shifted-boundary
estimate gives

```text
||1_[W,infinity)*g||_2^2
 <=C_eta*exp[-2*eta*W
             +2*m*log((a_0+eta)/(a_0-eta))].        (6.1)
```

Thus a sufficient tail condition is

```text
W>2*m/a_0.                                         (6.2)
```

Balancing also balances the root counts when the individual weights are
comparable.  It halves the all-pass load on each endpoint, but both compact
tails still have to fit inside the physical interval without destroying
the opposite selected evaluation.  No such uniform two-tail theorem is
claimed here.

Likewise, exact zeros pay once per distinct row.  Sections 3--4 of
`ZETA23-COHERENT-MICROCLUSTER-PHASE-TRANSPORT-2026-08-12.md` sign an entire
bounded rescaled cluster with one fixed-degree virtual translation, but a
global theorem composing those grouped cluster filters over `Theta(L)`
phase cells is not yet proved.  Combining that grouping with the balanced
two-leg ledger is the precise next divisor-side problem.

### 6.1 The periodic all-pass identity

There is a concrete reason to pursue one grouped representative per phase
cell.  Put right-half-plane Blaschke zeros on the ordinate lattice

```text
z_k=a+i*(omega_0+2*pi*k/D),       k in Z.           (6.3)
```

The boundary group delays add to the classical Poisson-kernel lattice sum

```text
sum_(k in Z)
  2*a/[a^2+(omega-omega_0-2*pi*k/D)^2]

 =D*sinh(a*D)/[cosh(a*D)-cos(D*(omega-omega_0))]
 =D+O(D*exp(-a*D)),                                (6.4)
```

uniformly in `omega`.  Thus one Blaschke factor per `2*pi/D` phase cell has
boundary phase derivative equal to the desired delay `D` up to an
exponentially small ripple.  Alternating or balancing these cell factors
between the two endpoint legs is the canonical global continuation of
Theorem 3.1.

Equation (6.4) is exact, but it is only a boundary all-pass identity.  The
actual collateral evaluations lie on positive-real vertical lines, a
finite list has endpoints, and the inverse transforms must fit in compact
physical support.  Those interior, truncation, and cluster-multiplicity
steps are not inferred from (6.4).

## 7. Actual-zeta and arithmetic scope

What is proved:

| statement | verdict |
|---|---|
| selected positive-row equality necessarily squares the full Blaschke product | **false** |
| balanced two-leg exact annihilation pays one product | **proved in the causal endpoint model** |
| fixed finite polynomially conditioned lists have exact compact PW/Gabor realization | **proved** |
| the one-product ledger has an exact real realization | **yes for the fixed compact list**, by the opposite-carrier construction (4.9) and exact correction |
| one real rank-one packet realizes the same coloring for a growing list | **open**; the required counter-rotating and inverse-Gram bounds are not uniform |
| `+/-pi/D` screen survives coherent two-leg splitting | **no** |
| less than one-product loss is possible in exact scalar leg-zero architecture | **no**, by (4.2) |
| arbitrary growing actual-zero list has compact grouped realization | open |
| current Bellotti--Wong count closes the divisor support bound | no |
| arithmetic one-square sign on the same state | open |
| uniform zero-free strip | not proved |

The factor-two obstruction has therefore been removed at the correct
algebraic level.  The remaining divisor question is quantitative:

> Balance grouped phase-cell conditions between the two endpoint legs,
> compactly realize both growing causal filters with `X^o(1)` leakage, and
> prove the resulting support-function estimate uniformly on the same
> arithmetic feasible set.

No count, density, or zeta-specific spacing theorem presently supplies that
conclusion automatically.
