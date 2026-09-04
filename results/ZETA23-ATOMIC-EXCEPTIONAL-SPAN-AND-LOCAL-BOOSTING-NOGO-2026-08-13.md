# Atomic exceptional span and local-boosting no-go

**Date:** 2026-08-13

**Verdict:** the fourth-moment exceptional-set theorem does not close the
actual-prime antenna problem.  The obstruction is quantitative
transversality, not rank.  In fact:

1. the cosine vectors over **one arbitrarily short open high-time interval**
   already span the whole finite carrier space;
2. the fourth-moment bound, the `Y^(.076+o(1))` exceptional length, the
   `Y^(.0855+o(1))` component count, frequency separation, and minimal
   additive energy are all compatible with an exact norm-one high-time
   recurrence in a model having the same dimensions and aperture;
3. a stronger actual-integer large-values theorem compresses the extreme
   carrier-correlation set for a cost-`C` representation into only
   `C^2Y^o(1)` unit packets, or `Y^(.0360606468...+o(1))` packets at the
   target cost; this still supplies no angle between their jet span and the
   distinguished vector `q_0`;
4. translating the diffuse prime kernel to repair a high peak returns
   exactly another actual-prime antenna.  For a one-peak correction, the
   low-carrier leakage is the square of the peak being corrected.  For many
   peaks it is the corresponding Gram/Christoffel leverage.  Local
   quadrature does not estimate this remote leakage.

Thus component count, Caratheodory compression, restricted invertibility
without an arithmetic angle estimate, and termwise modulated Voronoi
quadrature do not prove the required lower bound for the cancellation cost.
The surviving statement is a genuinely arithmetic no-recurrence theorem for
the actual log-prime curve.  No such theorem is proved here.

A tempting product-log amplification is false even in the stronger
**complex-exponential** interpolation problem.  Convolution powers the
Fourier transform at the **same** argument; it does not turn samples at
`u_p,u_q` into a sample at `u_p+u_q`.  The known product of two sample values
is instead a two-dimensional tensor Fourier value on the Cartesian prime
grid, which has no finer mesh in either coordinate.  Realification has a
second exact obstruction: its Hermitian mixed sectors heterodyne the two
carrier signs back to time zero.  The earlier far-conjugate
`O(M/gamma^2)` estimate is linear and cannot suppress this quadratic
baseband term.

Nothing in this report proves a zero-free strip.  A cheap nuller helps the
strip route; a uniformly small antenna kills that route.  The inequality
direction is kept explicit below.

---

## 1. Exact orientation and what the exceptional set forces

Use the notation of the fourth-moment report.  Thus

```text
a(t)=(cos(t*u_p))_(p in P_Y),
u_p=log(p/Y),
L=[0,T],                    T=Y^.01,
H=[T,B],                    B=Y^(50/33+o(1)),
delta_*=.0180303234....                                  (1.1)
```

Let `C_(L,H)` be the minimum total variation of a low/high nuller normalized
by `integral_L b dnu=1`, and let `E_B` be the quotient extremal.  The exact
comparison is

```text
1/C_(L,H)-epsilon_T <= E_B <= 1/C_(L,H)+epsilon_T.       (1.2)
```

Consequently:

* a **feasible** nuller of cost `C` gives the lower bound
  `E_B>=1/C-epsilon_T` and helps the strip route;
* a dual antenna with low error and high sidelobe at most `Y^-c` gives
  `C_(L,H)>=Y^(c-o(1))` and `E_B<=Y^(-c+o(1))`; if
  `c>delta_*`, it kills this sufficient route and does not prove a strip.

Let `P_0` be the diffuse prime antenna from the companion report.  Fix
`c=.019`, put `epsilon=Y^-c`, and let

```text
E={t in H: |P_0(t)|>epsilon},
A=sup_E |P_0|.                                           (1.3)
```

The proved estimates are

```text
|E| <= Y^(.076+o(1)),
# components reaching 2 epsilon <=Y^(.0855+o(1)).        (1.4)
```

They imply the following useful but limited forcing statement.

### Lemma 1.1 (exceptional mass is necessary, not expensive)

Suppose `(nu,mu)` is a feasible nuller, and

```text
sup_L |b-P_0|<=eta,       sup_(H\E)|P_0|<=epsilon.       (1.5)
```

Then

```text
1 <= eta||nu||+epsilon||mu_(H\E)||+A||mu_E||.            (1.6)
```

In particular, if `eta,epsilon<=Y^(-c+o(1))`, `c>kappa`, and
`||nu||+||mu||<=Y^kappa`, then

```text
||mu_E|| >= (1-o(1))/A.                                  (1.7)
```

#### Proof

The null constraint gives

```text
integral_L P_0 dnu=-integral_H P_0 dmu.
```

Insert this into `1=|integral_L b dnu|` and split `mu` over `E` and its
complement.  This gives (1.6).  QED.

Equation (1.7) says only that a cheap nuller must spend constant mass on the
peaks.  It gives no power lower bound for that mass.

### Theorem 1.2 (strongest actual-prime packet compression)

For the principal interpolation problem

```text
q_0=integral_H a(t)dmu(t),       ||mu||_TV=C,            (1.8)
```

put

```text
S_Y(t)=<q_0,a(t)>,
E_C={t in H:|S_Y(t)|>=M/(2C)},       M=#P_Y.             (1.9)
```

Then

```text
|mu|(E_C)>=1/2.                                         (1.10)
```

Moreover, for `C<=Y^(kappa+o(1))`, the actual-integer large-values theorem
covers `E_C` by

```text
R<=C^2Y^o(1)                                             (1.11)
```

intervals of fixed width.  Subdivision gives
`C^3Y^o(1)` intervals of width `O(1/C)`.  At the target cost,

```text
R<=Y^(.0360606468...+o(1)).                              (1.12)
```

#### Proof ledger

Pair (1.8) with `q_0`.  Outside `E_C`, the contribution to
`M=integral S_Y dmu` is at most `M/2`; inside, it is at most
`M|mu|(E_C)`.  This proves (1.10).

For a maximal one-separated subset of `E_C`, apply
[Guth--Maynard, Theorem 1.1](https://arxiv.org/abs/2405.20552) to the
dyadic pieces of the actual integer polynomial
`sum_(p in P_Y)p^(it)` (viewed as coefficients in `{0,1}`), with

```text
N asyp Y,       T<=Y^(50/33),       V>>M/C.              (1.13)
```

The three large-value terms are

```text
C^2Y^o(1),
Y^(-2/5)C^4Y^o(1),
Y^(50/33-8/5)C^4Y^o(1).                                 (1.14)
```

At `C<=Y^(kappa+o(1))`, the last two are smaller, proving (1.11).
The full derivation, including the harmless prime-power extension and the
shrinking-packet jet rank, is in
[`ZETA23-SINGULAR-ATOMIC-EXCEPTIONAL-SPAN-GATE-2026-08-13.md`](ZETA23-SINGULAR-ATOMIC-EXCEPTIONAL-SPAN-GATE-2026-08-13.md).

Each fixed packet has only `Y^o(1)` Taylor rank at any prescribed
fixed-power accuracy.  Thus the extreme-correlation contribution is
compressed to a space of dimension `C^2Y^o(1)`.  This is much stronger than
the `.0855` component count.  It still does not imply that the space misses
`q_0`; a one-dimensional space can contain one distinguished vector.  Nor
does (1.10) control the Euclidean size of the contribution from
`H\E_C`, whose carrier projection is small but whose transverse component
may cancel the packet contribution.

---

## 2. One component already has full algebraic span

The component-count heuristic fails before any number theory enters.

### Theorem 2.1 (open-interval full span)

Let `0<u_1<...<u_M` be distinct.  For every nonempty open interval
`J subset R`,

```text
span_R{(cos(t*u_j))_(j=1)^M:t in J}=R^M.                 (2.1)
```

The complex version with `exp(i*t*u_j)` spans `C^M`.

#### Proof

If `z` annihilates all vectors in (2.1), then

```text
f(t)=sum_j z_j cos(t*u_j)
```

vanishes on `J`.  The function `f` is entire, hence vanishes identically.
Linear independence of the exponentials with distinct frequencies gives
`z=0`.  The complex proof is identical.  QED.

### Corollary 2.2 (Caratheodory does not use component count)

For every such `J`, every carrier vector, including `q_0=(1,...,1)`, has an
exact signed representation by at most `M` points of `J`.  A minimizing
real atomic-norm representation, when it exists, can be compressed to at
most `2M+1` signed atoms by Caratheodory.

These are finite-dimensional existence statements.  Their coefficient norm
can be enormous.  Therefore neither one component nor
`Y^(.0855+o(1))` components yield a rank obstruction; only a lower bound for
the conditioning/atomic norm could help.

---

## 3. A precise countermodel to all geometry-only closures

The next result deliberately does **not** model the incommensurability of
actual prime logs.  Its point is sharper: every other input currently on the
table is compatible with a cheapest possible recurrence.  Therefore any
proof must use an arithmetic property that excludes this model.

Let `B=Y^(50/33)`, let `M asyp Y/log Y`, and take an integer interval
`I_B` of length `N asyp B`.  For `A subset I_B`, `#A=M`, put

```text
u_m=2*pi*m/B,
F_A(t)=M^-1 sum_(m in A) exp(i*t*u_m),
P_A(t)=Re F_A(t).                                       (3.1)
```

After choosing `I_B` appropriately, all `u_m` lie in any prescribed fixed
frequency window with nonempty interior.

### Theorem 3.1 (low-energy exact-alias model)

There are sets `A` as above, with

```text
min_(a!=b in A)|a-b| >>N/M,
min_(a!=b)|u_a-u_b| >>1/M asyp log(Y)/Y,                 (3.2)
```

for which

```text
E_add(A)=#{a+b=c+d:a,b,c,d in A}
         << M^2+M^4/N,                                  (3.3)

integral_0^B |F_A(t)|^4 dt
         =B E_add(A)/M^4
         << 1+B/M^2=O(1),                               (3.4)

P_A(B)=1,       and       (cos(B*u_m))_(m in A)=q_0.    (3.5)
```

Hence `delta_B` represents `q_0` with total variation exactly one.  At the
same time, for every fixed `c>0`,

```text
|{t in [0,B]:|P_A(t)|>Y^-c}| <<Y^(4c),                  (3.6)
```

and the number of components whose maximum reaches `2Y^-c` is

```text
<<Y^((9/2)c).                                            (3.7)
```

At `c=.019`, these are exactly the exponents `.076` and `.0855` from the
actual-prime fourth-moment theorem.

#### Proof

Put `L asyp N/M`.  Inside the ambient integer interval, place `M` active
blocks of length comparable with `L`, separated by gaps of the same length,
and choose one integer independently and uniformly from each active block.
This gives the separation in (3.2).  Apart from diagonal/repeated patterns,
only `O(M^3)` quadruples of block indices have overlapping pair-sum ranges.
For each such quadruple, conditioning on three selected integers leaves
probability `O(1/L)` for the fourth to solve the exact sum equation.  Hence

```text
E E_add(A)<<M^2+M^3/L<<M^2+M^4/N.
```

Some realization satisfies (3.3).

Orthogonality over one period gives the identity in (3.4).  Equation (3.5)
is immediate from `B*u_m=2*pi*m`.  Chebyshev gives (3.6).

For (3.7), `|P_A''|` is bounded by a constant depending only on the fixed
frequency window.  At an interior maximum of `|P_A|` of height at least
`2Y^-c`, Taylor's theorem supplies a subinterval of length
`gg Y^(-c/2)` on which `|P_A|>Y^-c`.  Distinct components give disjoint
subintervals.  The two boundary components are harmless.  Combine with
(3.6).  QED.

### Consequence 3.2

No theorem using only

```text
M, B, bounded frequency window, frequency separation,
fourth moment, additive energy, exceptional length,
component count, derivative bounds, or Caratheodory compression
```

can prove the required atomic transversality.  The exact-lattice alias must
be excluded using the arithmetic of the actual log-prime nodes.

### Corollary 3.3 (qualitative incommensurability is still insufficient)

For each finite `Y` and every `epsilon_0>0`, the frequencies in Theorem 3.1
can be perturbed to distinct, rationally independent frequencies
`u'_1,...,u'_M` such that

```text
integral_0^B |M^-1 sum_j exp(i*t*u'_j)|^4dt=O(1),
min_(j!=k)|u'_j-u'_k|>>1/M,                              (3.8)
```

and `q_0` has an exact representation on `H` of total variation at most
`1+epsilon_0`.

#### Proof

At the unperturbed frequencies, Theorem 2.1 supplies times
`s_1,...,s_M in H` for which the matrix with columns `a(s_j)` is invertible.
Invertibility persists under sufficiently small perturbation.  For the
perturbed curve, write

```text
r=q_0-a'(B),       c=[a'(s_1) ... a'(s_M)]^(-1)r.        (3.9)
```

As the perturbation tends to zero, `r` and hence `||c||_1` tend to zero.
Thus

```text
q_0=a'(B)+sum_j c_j a'(s_j)                              (3.10)
```

has cost at most `1+epsilon_0`.  Separation and the finite-interval fourth
moment are stable under a sufficiently small perturbation.  Finally, the
rationally dependent frequency vectors form a countable union of proper
hyperplanes, so the perturbation can be chosen outside that union.  QED.

Turning qualitative incommensurability into `C>=Y^delta` therefore requires
a **quantitative, actual-prime-specific** stability/Diophantine theorem, not
unique factorization alone.

---

## 4. What actual-prime arithmetic currently gives

Put

```text
S_Y(t)=sum_(p in P_Y) exp(i*t*log(p/Y)),       M=#P_Y.   (4.1)
```

### 4.1 The first dual vector is a pointwise prime-sum problem

If a complex measure `mu` represents `q_0`, then pairing with `q_0` gives

```text
M=|integral_H S_Y(t)dmu(t)|
 <=||mu|| sup_(t in H)|S_Y(t)|.                          (4.2)
```

The cosine version has the same statement with `Re S_Y`.  Thus the simplest
dual certificate would need

```text
sup_H |S_Y(t)| <=M Y^(-delta_*+o(1)).                    (4.3)
```

This is a uniform fixed-power bound for a natural prime Dirichlet
polynomial.  Mean values prove that (4.3) fails, if at all, only on a small
set; they do not prove (4.3).

### 4.2 Unique factorization has already been spent in the fourth moment

For every fixed integer `k>=2`, unique factorization gives the exact
multiplicative-energy bound for the `k`-fold prime product coefficients.
Montgomery--Vaughan then gives, as long as the aperture is below `Y^k`,

```text
integral_0^B |M^-1 S_Y(t)|^(2k)dt <<Y^o(1).              (4.4)
```

Among these fixed moments, `k=2` is the first one whose product conductor
exceeds `B`; it yields the best exceptional exponent.  Higher moments give
`Y^(2kc+o(1))`, which is weaker than `Y^(4c+o(1))` at a threshold `Y^-c`.
Unique factorization therefore controls multiplicative collisions but not
the location or height of a remaining peak.  The model in Section 3 has
minimal additive energy and still has an exact peak.

### 4.3 The full-interval prime Gram is well conditioned, but atoms evade it

The actual log-prime separation is `gg 1/Y`.  The
Montgomery--Vaughan Hilbert inequality gives

```text
G_(p,q)=integral_T^B exp(i*t*(u_p-u_q))dt,
||G-B I||_(op)<<Y.                                      (4.5)
```

Since `B=Y^(50/33)>>Y`, this is a genuine Riesz bound.  It proves that the
minimum **L2-density** interpolant has squared norm comparable with `M/B`.
It does not lower-bound the total variation of a singular measure.  Smoothing
an atom on a time scale large enough to exploit (4.5) changes its prime
samples; constructing a sample-preserving smoother is the original antenna
problem again.

### 4.4 Actual primes exclude the exact one-atom alias

There is a clean arithmetic rigidity statement at atomicity one.

### Lemma 4.1 (five-prime one-atom no-go)

If the window contains five distinct primes, there are no real `c` and
`t!=0` such that

```text
c a(t)=q_0.                                              (4.6)
```

#### Proof

The equations say `cos(t log(p/Y))=r=1/c`.  Fix
`theta in [0,pi]` with `cos(theta)=r`.  For every prime coordinate,

```text
t log(p/Y)=2*pi*k_p+epsilon_p theta,
epsilon_p in {+1,-1}.                                   (4.7)
```

Among five primes, three have the same sign.  Subtracting the equation for
one of them from those for the other two makes the ratio of two distinct
prime-log ratios rational.  Clearing denominators and exponentiating gives
a nontrivial multiplicative relation among three distinct primes, contrary
to unique factorization.  QED.

This removes the literal actual-prime analogue of (3.5).  It supplies no
TV lower bound for two or more incommensurable atoms; Corollary 3.3 explains
why atom count must be accompanied by a quantitative arithmetic condition.

### 4.5 Taylor curvature near `2*pi*m*Y` does not give coefficient-uniform
transversality

For `p=Y+r`,

```text
2*pi*m*Y log(p/Y)
 =2*pi*m r-pi*m*r^2/Y+O(m*|r|^3/Y^2).                   (4.8)
```

The linear integer phase disappears and the quadratic curvature predicts
square-root stationary blocks.  This is useful for a smooth integer sum.
For the actual prime restriction, however, passing through Vaughan or
Heath--Brown creates balanced Type-II sums with the same completed carrier.
A coefficient-uniform power saving for those sums is precisely the missing
actual-prime estimate; Taylor expansion alone does not supply it.

### 4.6 Quantitative Kronecker theory is far below the needed dimension

Unique factorization gives rational independence of the prime logarithms
(modulo the common-center qualification).  It implies recurrence only on an
unbounded time axis and excludes an exact one-atom alias at a generic finite
time.  A polynomial-time no-recurrence theorem would require simultaneous
Diophantine bounds in dimension `M asyp Y/log Y`.  Standard lower bounds for
linear forms in logarithms have constants exponential (or worse) in that
growing dimension, so they do not separate the polynomial aperture
`B=Y^(50/33)` at a fixed power.

This is the precise arithmetic gap: “incommensurable” is qualitative;
`C>=Y^delta` is quantitative.

---

## 5. Localized reconstruction and boosting return the same gate

Let the diffuse complex kernel be

```text
K_Y(s)=sum_p lambda_p exp(i*s*u_p),       K_Y(0)=1.      (5.1)
```

A translate centered at `t_r` is

```text
K_Y(t-t_r)=sum_p lambda_p exp(-i*t_r*u_p)exp(i*t*u_p).   (5.2)
```

Thus a finite correction bank has the exact form

```text
Q(t)=sum_r c_r K_Y(t-t_r)
    =sum_p lambda_p G(u_p)exp(i*t*u_p),
G(u)=sum_r c_r exp(-i*t_r*u).                            (5.3)
```

Equation (5.3) is another actual-prime antenna.  No new frequency nodes have
been created.

### Proposition 5.1 (one-peak leakage conservation)

To cancel the value `K_Y(t_r)` by a normalized translated kernel, take

```text
Q_r(t)=K_Y(t_r)K_Y(t-t_r).                               (5.4)
```

Then its leakage at the low carrier is exactly

```text
Q_r(0)=K_Y(t_r)K_Y(-t_r)=|K_Y(t_r)|^2                   (5.5)
```

for real weights.  Hence peak cancellation is not free even before
cross-interactions are considered.

The Guth--Maynard refinement lands exactly at the Bessel boundary, not
beyond it.  After scaling the diffuse coefficients so that they are bounded
by one, the set of one-separated centers where `|K_Y(t)|>=epsilon` has

```text
R<<epsilon^-2 Y^o(1).                                   (5.6)
```

Consequently the unconditional sum of the one-center squared leakages is
only

```text
R epsilon^2<<Y^o(1),                                    (5.7)
```

not a negative power.  Large-value packet compression therefore saturates
the elementary energy ledger; a power contraction still requires
directional cancellation or a Schur margin.

For several centers, the optimal correction is obtained by solving the
kernel Gram system

```text
Gamma_(r,s)=K_Y(t_r-t_s).                                (5.8)
```

The amount of low carrier spent is the corresponding Schur-complement or
Christoffel leverage.  Proving it is small is exactly a quantitative angle
bound between `q_0` and the exceptional atomic span.

The coarse prime-cell/Voronoi estimate is local in the offset:

```text
error at t from a kernel centered at t_r
        depends on |t-t_r| times the cell width.         (5.9)
```

It can estimate (5.4) near `t_r`.  At the low band, however,
`|t-t_r| asyp t_r`, which is in the unresolved high tail.  Modulating the
quadrature therefore transfers the unknown high-tail value into low leakage;
it does not estimate it.  The exact-alias model of Section 3 is periodic, so
an endpoint peak and the low carrier are literally the same vector and no
boosting iteration can contract it.

Localized oversampling remains useful only if supplemented by a new theorem
of the form

```text
q_0 has small projection onto every exceptional sampling subspace.       (5.10)
```

That is the atomic span gate, not a consequence of (1.4).

---

## 6. Product-log amplification and analytic-signal no-go

### 6.1 The proposed one-dimensional product lift is false

Even the stronger complex constraints

```text
F_mu(u_p)=integral_H exp(i*t*u_p)dmu(t)=1                (6.1)
```

do not create samples at balanced product logs.  The exact convolution
identity is

```text
F_(mu^(*k))(v)=F_mu(v)^k.                                (6.2)
```

Thus (6.1) implies `F_(mu^(*k))(u_p)=1` at the **same prime nodes**.  It
does not imply

```text
F_(mu^(*2))(u_p+u_q)=1.                                 (6.3)  FALSE
```

Indeed, the known product has the two-dimensional tensor form

```text
F_mu(u_p)F_mu(u_q)
 =integral_(H^2) exp(i[t*u_p+s*u_q])d(mu tensor mu)(t,s)
 =1.                                                     (6.4)
```

It is the Fourier transform of `mu tensor mu` at `(u_p,u_q)`, not the
Fourier transform of `mu*mu` at `u_p+u_q`.  Passing from `(t,s)` to one
variable by setting `t=s` replaces the product measure by a diagonal
measure and is not an allowed identity.

This distinction also appears on the dual side.  Squaring a prime antenna
creates product-log coefficient nodes, but pairing that square with `mu`
requires the unknown samples `F_mu(u_p+u_q)`.  Pairing two separate antenna
copies with `mu tensor mu` merely factors the original prime-node pairing.
The Cartesian grid `U_Y^k` retains the original prime mesh in every
coordinate, so it supplies no one-dimensional densification.

Consequently the previously tempting physical product-gap exponent
`.448787...` is not a theorem target.  It arose after the false step (6.3)
and must not be used.

### 6.2 Realification creates an exact Hermitian baseband sector

There is a second obstruction if one tries to add an analytic-signal or
oriented two-channel lift.  Let `mu` be real and supported on `H`, let
`mu^vee` be its reflection, and put

```text
rho=(mu+mu^vee)/2.                                      (6.5)
```

Then `hat(rho)(u)=integral cos(tu)dmu(t)`, so the cosine constraints become
complex constraints for `rho`, but on `H union (-H)`.  Its square is

```text
rho*rho=1/4[mu*mu+mu^vee*mu^vee
                 +mu*mu^vee+mu^vee*mu].                 (6.6)
```

The oriented sectors lie in `+2H` and `-2H`.  The Hermitian mixed sectors
lie in

```text
H-H=[-(B-T),B-T],                                       (6.7)
```

which contains zero.  If `mu` is localized near a high carrier `gamma`
with width `Delta`, the mixed sector is localized near zero with width
`2Delta`, independently of `gamma`.  On the Fourier side,

```text
hat(mu*mu^vee)(u)=hat(mu)(u)hat(mu)(-u)=|hat(mu)(u)|^2. (6.8)
```

At a cosine interpolation node, `Re hat(mu)=1`, so (6.8) is at least one.
The mixed channel is the baseband energy channel, not a small companion.

This is precisely why the `O(M/gamma^2)` estimate from the earlier real
high-carrier construction does not transfer.  That estimate controls a
**linear** counterrotating evaluation a distance about `2gamma` away.  In a
quadratic tensor/convolution step the two carrier signs heterodyne exactly
to zero:

```text
(+gamma)+(-gamma)=0.                                    (6.9)
```

Odd powers or a Chebyshev substitution do not give a universal escape.
For a single atom, `T_3(cos(tu))=cos(3tu)` does remove the baseband.  But
take the even measure

```text
rho=1/2[delta_t+delta_(-t)
        +epsilon*delta_(2t)+epsilon*delta_(-2t)],        (6.10)
```

with `t,2t in H`.  The six permutations of `t+t-2t=0` and its negative give

```text
[4 rho^(*3)-3 rho]({0})=3 epsilon!=0.                   (6.11)
```

Thus `T_3` cancels mixed sectors only on the one-frequency model; arbitrary
allowed packets recreate zero through cross-carrier relations.  Higher
fixed polynomials have the same issue after choosing a finite signed-sum
relation among points of the very wide interval `H`.

The two-channel notation exposes the missing datum.  Put

```text
F_+(u)=hat(mu)(u),       F_-(u)=hat(mu)(-u)=conj(F_+(u)). (6.12)
```

The actual scalar constraint is only

```text
[F_+(u_p)+F_-(u_p)]/2=1.                                (6.13)
```

It does not say `F_+(u_p)=1`.  Multiplication produces all four channel
tensors `++,+-,-+,--`.  Keeping only `++` adds the missing sine/orientation
constraint.  A formal direct-sum label is absent from the scalar carrier;
projecting back to a real same state restores the mixed Hermitian blocks.

### 6.3 Far-conjugate dual realification moves the carrier

For complex coefficients `z_p`, write

```text
K_z(t)=sum_p z_p exp(i*t*u_p),
x_p=2 Re[exp(-i*gamma*u_p)z_p].                          (6.14)
```

The real cosine polynomial obtained from the modulated companion pair is

```text
P_x(t)=Re K_z(t-gamma)+Re K_z(-t-gamma),
P_x(0)=2 Re K_z(-gamma).                                (6.15)
```

The complex dual objective for `q_0` is `Re K_z(0)`.  Thus the modulation
which separates conjugate bands also moves the distinguished low carrier
from `0` to `-gamma`.  Taking `gamma=0` preserves the objective but restores
the uncontrolled negative-time antenna.  A second packet that repairs
(6.15) is exactly the low-anchor Schur problem of Section 5.

The far-conjugate construction therefore remains valid in its original
scope: a designed complex packet around a selected nonzero carrier with
finitely many local linear conditions.  It neither creates the false
one-dimensional lift (6.3) nor preserves the `q_0` objective after an
oriented realification.  A successful nonlinear lift would need a new
same-state operation that supplies the missing sine channel and eliminates
the mixed baseband sectors without changing support.

---

## 7. The surviving actual-prime theorem card

The unresolved statement can be written without exceptional-set language.

### AP-TRANS (`actual-prime cosine transversality`)

For some fixed `delta>delta_*` and all sufficiently large `Y`, every signed
measure `mu` supported on `[Y^.01,Y^(50/33)]` satisfying

```text
integral cos(t*log(p/Y))dmu(t)=1
for every prime p in [Y exp(-w),Y exp(w)]                (7.1)
```

obeys

```text
||mu||_TV>=Y^(delta-o(1)).                               (7.2)
```

The corresponding target for the full low carrier replaces the right side
of (7.1) by the principal carrier vector and tracks the harmless fixed
normalization.

Equivalent dual form: construct actual-prime coefficients `lambda_p` for
which the low carrier is approximated and

```text
sup_(Y^.01<=t<=Y^(50/33))
 |sum_p lambda_p cos(t*log(p/Y))|
 <=Y^(-delta+o(1)).                                     (7.3)
```

The fourth-moment theorem proves (7.3) off a set of length
`Y^(.076+o(1))`.  Sections 2--5 prove that neither the length nor the number
of components controls (7.2).  A successful proof must add at least one of:

1. a fixed-power quantitative no-recurrence theorem for the actual
   log-prime curve up to polynomial time;
2. an arithmetic angle/leverage bound for every exceptional sampling
   subspace;
3. a genuinely new cosine-compatible same-state amplification (the naive
   convolution/product-log lift is false, and ordinary real powers retain
   baseband sectors);
4. a full uniform actual-prime antenna estimate such as (7.3).

No item in this list is currently proved.  The honest endpoint is therefore:

```text
fourth-moment compression:                         THEOREM;
Guth--Maynard C^2 packet compression:              THEOREM;
diffuse L2 designs too expensive:                  THEOREM;
component-count/rank closure:                      FALSE;
localized-kernel closure without new arithmetic:  CIRCULAR;
actual-prime atomic transversality:                OPEN;
uniform zero-free strip from this packet alone:    NOT PROVED.
```
