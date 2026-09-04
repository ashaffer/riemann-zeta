# QP radialization: singleton obstruction and the corrected Turan normalization

**Date:** 2026-08-15  
**Verdict:** `RAD_hi(lambda)` as presently formulated is not the intended
coefficient adapter.  Its directional quantity is identically one:

```text
D_N^-(A')=1                                             (0.1)
```

for every sufficiently large `N` and every fixed `A'>1/2`.  This is an exact
actual-prime construction, not an abstract convex countermodel.  It turns the
proposed power comparison into a constant lower bound for the complete
radial antipode, far stronger than—and unrelated to—the Turan prime-sum
event.

The correct directional quantity keeps the original `N` normalization:

```text
E_N^-(A')=
 sup [ -N^(-1) sum_(p in I) cos(t log(p/Y)) ]_+.       (0.2)
```

With all the same scale, shell, half-integer, and ordinate restrictions,

```text
E_N^-=sup (M/N)D(I,Y,t).                              (0.3)
```

An isolated prime now costs only `1/N`.  The phase-localization theorem
gives the lossless fixed-constant comparison

```text
L_N(A') <=(4J_w/3+o(1)) E_N^-(A'),                   (0.4)
```

and the reverse comparison holds after only a fixed enlargement of the
prime scale.  Thus `E_N^-` is exponent-equivalent to the actual Turan
modulus.

One corrected global radialization statement is

```text
ERAD_hi(lambda): E_N^-(A')<=C (R_N^hi)^lambda.        (0.5)
```

No fixed `lambda>0` is proved here.  Exact pairing introduces the factor
`M/N` and **no additional loss** from the prime-power nodes.  Passing to
von Mangoldt weights trades the familiar factor `log N`, which is
`N^o(1)` and irrelevant to fixed exponents.  Modulation, multiplicative
weights, convolution with the gapped nuller, and interval partitioning do
not supply the missing reverse inequality: each either restates the exact
radial moment problem, leaves only an orthant witness, exits the legal band,
or pays the existing exponential central-atom loss.

Accordingly the original `RAD_hi` is **closed as misnormalized**.  A
mass-normalized comparison is honest, but the weakest theorem actually needed
is the thresholded implication from one `K_N` event to the full legal radius
on `H_Y`; Section 5 formulates it as `LTRAD_full`.  It remains open.  No QP
theorem or strip is claimed.

---

## 1. The probability-normalized directional supremum is exactly one

Recall the original definition.  A canonical direction consists of an
allowed half-integer `Y`, a nonempty prime interval `I` in its fixed shell,
and `t in [N^(1/2),N^(A')]`; if `M=#(I intersect primes)`, its negative depth
is

```text
D(I,Y,t)=-M^(-1)sum_(p in I)cos(t log(p/Y)).          (1.1)
```

### Theorem 1.1 (actual-prime singleton saturation)

For every fixed `A'>1/2` and all sufficiently large `N`,

```text
D_N^-(A')=1.                                         (1.2)
```

#### Proof

By the prime number theorem (Bertrand plus an immaterial endpoint adjustment
also suffices on integer scales), choose a prime

```text
N<=p<=3N/2.                                          (1.3)
```

Put `q=max(1-A',0)` and choose a positive half-integer `h` with

```text
4pi N^q<=h<=4pi N^q+1.                               (1.4)
```

Then put

```text
Y=p+h,
u=log(Y/p)=log(1+h/p),
t_0=pi/u.                                            (1.5)
```

For the project constant `C_w=2exp(w)>2`, (1.3) gives

```text
N<=Y<=C_wN                                           (1.6)
```

for all large `N`.  Also `u<w`, so `p` belongs to the shell centered at
`Y`.  Isolate it with, for example,

```text
I=[p-1/4,p+1/4].                                     (1.7)
```

This interval contains the single prime `p`.

Here `h=o(N)`, and the elementary bounds

```text
x/(1+x)<=log(1+x)<=x             (x>0)               (1.8)
```

give, after using `N<=p<=3N/2`,

```text
N^(min(A',1))/5<=t_0<=N^(A')                         (1.9)
```

for all sufficiently large `N`.  Since `min(A',1)>1/2`, this implies

```text
N^(1/2)<=t_0<=N^(A')                                (1.10)
```

for every fixed `A'>1/2` and all large `N`.  Finally,

```text
cos[t_0 log(p/Y)]=cos(-pi)=-1.                       (1.11)
```

Thus (1.1) equals one.  No cosine probability average can have negative
depth greater than one, proving (1.2).  QED

The construction uses an actual prime, an allowed half-integer center, the
exact high band, and a legal shell interval.  Prime powers elsewhere in the
shell do not enter the chosen canonical coefficient vector, as the original
definition explicitly permits zero weights on them.

### Consequence for the proposed `RAD_hi`

Substituting (1.2) into

```text
D_N^-<=C(R_N^hi)^lambda                             (1.12)
```

forces

```text
R_N^hi>=C^(-1/lambda)                                (1.13)
```

for all large `N`.  In particular, (1.11) is incompatible with the intended
use of a fixed-power QP/DPA bound `R_N^hi<=N^(-c)`.  This is not evidence
against the intended reverse bridge; it proves that the probability
normalization discarded the prime-sum mass which the Turan theorem controls.

---

## 2. The corrected mass-normalized directional quantity

Define

```text
e(I,Y,t)=-N^(-1)sum_(p in I)cos(t log(p/Y)),          (2.1)
E_N^-(A')=sup [e(I,Y,t)]_+,                          (2.2)
```

over the same legal triples.  Then the identity

```text
e(I,Y,t)=(M/N)D(I,Y,t)                               (2.3)
```

is exact.  Theorem 1.1's singleton has corrected depth `1/N`, so it no
longer overwhelms a Turan event of size `N^(-d)`, `d<1`.

### Proposition 2.1 (phase localization in the corrected normalization)

With `J_w` the fixed logarithmic partition count in the phase-localization
theorem,

```text
L_N(A')<=(4J_w/3+o(1))E_N^-(A').                    (2.4)
```

#### Proof

For an interval sum `S` contributing to `L_N`, choose a logarithmic piece
`S_0` with

```text
|S_0|>=|S|/J_w.                                      (2.5)
```

The half-integer phase lemma supplies a legal `Y` for which

```text
Re[Y^(it)S_0]<=-3|S_0|/4.                            (2.6)
```

The left side is exactly the unnormalized centered cosine sum.  Therefore

```text
E_N^->=3|S|/(4J_wN).                                 (2.7)
```

Take the supremum and absorb endpoint `o(1)` terms.  QED

Conversely, for every legal triple,

```text
e(I,Y,t)
 <=N^(-1)|sum_(p in I)p^(-it)|.                      (2.8)
```

The shell and allowed center put all selected primes in one fixed
multiplicative enlargement `[c_wN,C_w'N]`.  Partitioning that enlargement
into `O_w(1)` intervals of ratio at most two and changing the reference
scale by fixed factors shows

```text
E_N^-(A')<=C_w max_(N' asyp_w N)L_(N')^cmp(A'),      (2.9)
```

where `L^cmp` is the same prime modulus with the harmless fixed-factor scale
enlargement.  Hence `E_N^-` and the Turan modulus have the same fixed-power
content.  There is no probability-normalization artifact left.

---

## 3. Exact pairing with a high-subband radial antipode

Fix a legal center `Y` and suppose a probability `nu` on `K_N` is radial at
depth `r` for the **complete** shell node set:

```text
int_(K_N) cos(t log(n/Y))dnu(t)=-r                  (3.1)
```

for every prime power `n` in the shell, after the prescribed absolute-node
identification.  For any prime interval `I` in that shell, Tonelli's theorem
and (3.1) give the exact identity

```text
int_(K_N)e(I,Y,t)dnu(t)=(M/N)r.                      (3.2)
```

Therefore

```text
sup_(t in K_N)e(I,Y,t)>=(M/N)r.                      (3.3)
```

This recovers the already known easy direction: directional support is at
least radial support.  It does not reverse it.

This pairing requires the radial measure itself to stay in `K_N`, because
`E_N^-` is defined only on that subband.  The weaker forward implication used
later—one event in `K_N` forces a radial measure on the full `H_Y`—does not
need or claim this easy-direction pairing.

### Prime powers introduce no factor

Equation (3.2) uses only the prime coordinates, but (3.1) holds for them
because primes are a subset of the complete prime-power node set.  The
additional proper-prime-power constraints can only make radialization
harder; they do not change the coefficient `M/N`, insert a logarithm, or
invalidate the pairing.

### Where the logarithm appears with von Mangoldt weights

If instead one defines

```text
e_Lambda(I,Y,t)
 =-N^(-1)sum_(n in I)Lambda(n)cos(t log(n/Y)),       (3.4)
```

then radial pairing gives

```text
int e_Lambda dnu
 =r N^(-1)sum_(n in I)Lambda(n).                     (3.5)
```

On a fixed multiplicative prime interval, the prime part has
`Lambda(p) asyp log N`; proper powers contribute `O(N^(1/2)log N)`.  Thus
partial summation trades (2.1) and (3.4) by the expected `log N=N^o(1)`
factor plus a half-power error.  It changes no fixed exponent.  The
unweighted normalization (2.1) is nevertheless the exact one matching the
Turan modulus used in the reverse bridge.

---

## 4. Why the proposed constructive equalizers do not prove `ERAD`

This section records exact scope, not an impossibility theorem for every
future actual-prime construction.

### 4.1 Translation or modulation averaging

Starting from a negative height `t_0`, translate it by a probability `mu`:

```text
nu=law(t_0+S),                 S~mu.                  (4.1)
```

Its complex moment at node `u_j` is

```text
exp(it_0u_j)hat mu(u_j).                              (4.2)
```

Exact radialization asks for a positive `mu`, supported in the translated
legal interval, satisfying

```text
Re[exp(it_0u_j)hat mu(u_j)]=-r       for every j.    (4.3)
```

Equations (4.3) are another copy of the complete positive moment problem.
The single scalar identity

```text
sum_j lambda_j cos(t_0u_j)=-D                        (4.4)
```

supplies no coordinatewise interpolation data for (4.3).  Uniform
translation averaging makes the moments small, not equal, and exact
correction requires the missing condition-number/inradius theorem.

### 4.2 Multiplicative weights and exact equalization

Positive multiplicative weights can find a point of the height simplex if the
target orthant is feasible.  If they do not terminate, their empirical
height measure has

```text
int cos(tu_j)dnu(t)<=-epsilon        for every j,     (4.5)
```

but the coordinates in (4.5) need not be equal.  The convex hull of the
actual cosine curve is not known to be order-closed.  Mixing with the
forbidden atom at zero preserves coordinate differences, and
coordinate-by-coordinate convolution both exits `K_N` and pays an
exponential product.  Thus multiplicative weights supplies neither a legal
orthant-to-ray lemma nor (0.5).

### 4.3 Convolution with the gapped nuller

The exact gapped Bernoulli construction supplies a spectral-null probability
on `{0} union +/-K_N`; deleting its central atom gives a legal radial
antipode, but its depth is

```text
r=1/(2^G-1)                                           (4.6)
```

for `G` nonempty one-sided nulling factors.  Nulling the complete shell by
bounded-size groups has `G=Y^(1-o(1))`, so (4.6) is exponentially small.
Convolving this measure with the negative atom at `t_0` multiplies Fourier
moments by `cos(t_0u_j)`, destroying radial equality; its support also becomes
a sumset rather than `K_N`.  Mixing retains the same nonradial coordinate
vector.  A macroscopic group factor would evade (4.6), but constructing it
is precisely the original growing-dimensional radialization problem.

### 4.4 Prime-interval partitions

Writing a canonical prime probability as

```text
lambda=sum_l theta_l lambda_l                        (4.7)
```

and pigeonholing (4.4) locates a negative block.  It does not manufacture
equal moments at prime-power nodes outside that block.  Radializing each
block separately would already assume the desired theorem; mixing
nonradial block measures averages their coordinate defects without forcing
them equal.

### 4.5 Multiplicativity and the Euler structure

The Euler and von Mangoldt structure is multiplicative in the node variable
`n`.  Radialization varies the dual height `t`.  Convolution in height
multiplies Fourier moments at `log(n/Y)` and expands ordinate support by
sumsets; multiplication or division of nodes generates log frequencies not
in the prescribed fixed shell.  Unique factorization therefore supplies no
support-preserving permutation or averaging action which sends the canonical
direction to `-r q_0`.  Any successful use of Euler structure must prove a
new coefficient-sensitive positive moment theorem, not merely rewrite the
existing scalar prime sum.

---

## 5. The weakest sufficient theorem is full-band, thresholded, and long-interval

Even the global corrected inequality (0.5) is stronger than the reverse
bridge needs.  Put

```text
H_Y=[Y^.01,Y^A],                  A=50/33,            (5.0)
```

and let `r_+(H_Y;S_Y)` be the full legal QP radius.  Fix exponents `c,d>0`
and define the weakest local threshold statement

```text
LTRAD_full(c,d):
 e(I,Y,t_0)>=N^(-d)
   ==> r_+(H_Y;S_Y)>=N^(-c),                          (5.1)
```

with harmless fixed constants or `N^o(1)` margins allowed on both sides.
Here the event height remains in the Turan subband `K_N`, but the radializing
measure may use the complete legal band `H_Y`.  This keeps the center `Y`
produced by phase localization and is enough because DPA/QP KILL bounds the
full radius.  Requiring the radial measure to remain in `K_N` defines the
strictly stronger optional statement `LTRAD_hi(c,d)`; it is unnecessary for
the strip contradiction.

### Proposition 5.1 (large mass is automatic and exact)

Every witness to the premise of (5.1) has

```text
M/N>=N^(-d),                 M>=N^(1-d).              (5.2)
```

#### Proof

Each summand in (2.1) is at most one in absolute value, so

```text
e(I,Y,t_0)<=M/N.                                     (5.3)
```

Insert the premise of (5.1).  QED

Thus the relevant interval contains at least `N^(1-d)` primes and has
physical length at least `N^(1-d)-1`.  It is not the singleton or short-block
regime.  If

```text
E_(N,d)^long=
 sup_(M>=N^(1-d)) [e(I,Y,t)]_+,                      (5.4)
```

then the threshold equivalence is exact:

```text
E_N^->=N^(-d)  iff  E_(N,d)^long>=N^(-d).            (5.5)
```

The forward implication is Proposition 5.1 and the reverse is inclusion of
the restricted class.  Likewise, a Turan modulus event
`L_N>=C N^(-d)` produces, after the fixed logarithmic partition and phase
alignment, a block with `M>=cN^(1-d)` automatically, because the modulus of
an `M`-term unit sum is at most `M`.

The probability depth of such a witness is

```text
D(I,Y,t_0)=N e(I,Y,t_0)/M.                           (5.6)
```

Using the standard upper count `M<<N/log N` on a fixed multiplicative
interval, the premise also forces

```text
D(I,Y,t_0)>>N^(-d)log N,                             (5.7)
```

but it supplies only one weighted scalar direction, not equal moments.

### Exact logical role of `LTRAD_full`

Suppose a fixed-power QP/DPA theorem gives, at the same centers,

```text
r_+(H_Y;S_Y)<N^(-c).                                 (5.8)
```

The contrapositive of (5.1) then gives `E_N^-<N^(-d)`.  Proposition 2.1
gives the corresponding prime-modulus estimate, and the audited Turan theorem
gives a strip.  Conversely, the localized zero contrapositive produces a
witness to the premise of (5.1), so (5.1) contradicts (5.8).  Up to the
already explicit fixed constants and strict exponent margins, this is the
exact weakest long-interval adapter used by the reverse argument.

It is still unproved.  Large mass removes the singleton defect but does not
turn the scalar average (5.6) into the complete exact radial equations.  In
particular, the negative primes occupy only one coefficient direction; the
proper prime powers and all primes outside `I` remain unconstrained.

### Exact convex dual at the selected center

Fix `Y`, write

```text
a(t)=(cos(tu_j))_(j<=M_total),
P_Y=conv{a(t):t in H_Y},
q_0=(1,...,1),
h_Y(y)=sup_(t in H_Y)y dot a(t).                     (5.9)
```

The exact radial depth is

```text
r_Y=sup{r>=0:-r q_0 in P_Y}
   =inf_(y:q_0 dot y=-1)h_Y(y).                      (5.10)
```

The second identity is compact separation of the ray from `P_Y`, with the
usual convention if the positive ray is infeasible.  Consequently
`LTRAD_full(c,d)` is exactly the following candidate-conditioned dual claim:

```text
e(I,Y,t_0)>=N^(-d)
  ==> h_Y(y)>=N^(-c)
      for every y with q_0 dot y=-1.                 (5.11)
```

This formulation keeps the quantifiers that scalar estimates usually lose:
`y` is signed, adaptive, supported on every prime-power node, and tested on
the complete continuum `H_Y`.

### A calibrated transverse-return lemma

There is a sharper sufficient condition which shows exactly what a
constructive equalizer must do.  Let `lambda` be the uniform probability on
the selected prime interval, extended by zero to the other nodes, and put

```text
D=-lambda dot a(t_0)>0,
v=a(t_0)+D q_0.                                      (5.12)
```

Then

```text
lambda dot v=0.                                      (5.13)
```

If `v=0`, the atom at `t_0` is already radial at depth `D` and there is
nothing to prove.  Assume below that `v!=0`.

Define the opposite transverse-return depth

```text
s_v=sup{s>=0:-s v in P_Y}.                           (5.14)
```

Whenever this ray is feasible, the same compact separation gives

```text
s_v=inf_(y:y dot v=-1)h_Y(y).                        (5.15)
```

Equivalently, `s_v>=s` if and only if the homogeneous inequalities

```text
h_Y(y)>=s[-y dot v]
       for every y with y dot v<0                    (5.16)
```

hold.  This is a coefficient-sensitive statement: the residual vector `v`
depends on the actual long prime interval and its actual negative height.

### Proposition 5.2 (exact transverse mixing)

For every feasible `s` in (5.14),

```text
r_Y>=D s/(1+s).                                      (5.17)
```

#### Proof

Choose a probability `mu` on `H_Y` with

```text
int a(t)dmu(t)=-s[a(t_0)+Dq_0].                      (5.18)
```

Then the legal probability

```text
nu={s/(1+s)}delta_(t_0)+{1/(1+s)}mu                 (5.19)
```

has moment vector

```text
int a(t)dnu(t)=-{Ds/(1+s)}q_0.                       (5.20)
```

QED

Since a threshold witness has `D>=e>=N^(-d)`, for `c>d` the single estimate

```text
s_v>=N^(-(c-d)+o(1))                                (5.21)
```

implies `r_Y>=N^(-c+o(1))`.  Thus the weakest precise hypothesis for this
one-atom constructive scheme is not a general Gram bound: it is the signed
candidate-specific residual inequality (5.16) at
`s=N^(-(c-d)+o(1))`.

The original negative scalar gives no part of (5.16).  It says only
`lambda dot v=0`, while (5.16) ranges over every signed dual direction which
points negatively along `v`.  This is the exact transverse information that
translation, scaling, or boosting would have to manufacture.

### What translations and scalings would have to prove

A translated measure `t=t_0+S` proves (5.21) only if its characteristic
function solves all equations

```text
Re[exp(it_0u_j)hat mu(u_j)]
 =-s[cos(t_0u_j)+D]                 (j<=M_total).    (5.22)
```

This is exactly (5.18), with positivity and translated support retained.
The long scalar average cancels after applying `lambda` to (5.22), but gives
no individual equation.

Using the full band does materially improve support headroom.  Since
`t_0<=N^(A')`, `A'<A`, the legal integer harmonics include

```text
1<=k<=K_0=floor(Y^A/t_0),
K_0>=Y^(A-A'-o(1)).                                  (5.23)
```

Thus the earlier high-subband objection `t_0>B/2` is irrelevant to the
weakest full-band theorem.  Harmonic scaling succeeds exactly when

```text
-s v in conv{a(k t_0):1<=k<=K_0}.                   (5.24)
```

Equivalently,

```text
max_(1<=k<=K_0)y dot a(k t_0)>=s[-y dot v]
     for every y with y dot v<0.                    (5.25)
```

This is the discrete restriction of (5.16).  For the Turan choice `A'`
close to `A`, `K_0=Y^(A-A'+o(1))` is polynomial but much smaller than the
`Y^(1-o(1))` node count.  The long negative scalar does not prove that its
residual vector lies in this low-dimensional convex hull.  Continuous
scaling restores the whole interval `H_Y` and hence simply restates (5.18),
but it is no longer blocked by lack of ordinate headroom.

### Optional constant-fraction cells

If one strengthens the premise by requiring `I` to contain a fixed fraction
of the shell primes, then `lambda` is diffuse with
`||lambda||_2=Y^(-1/2+o(1))`.  The exact dual and residual conditions
(5.11)--(5.16) do not change: nodes outside `I`, and all proper prime powers,
still occur with arbitrary signed coefficients in `y`.  No available
translation or Euler symmetry permutes the selected prime cell onto those
coordinates while preserving `H_Y` and exact equality.  Diffuseness helps
scalar and fixed-degree estimates, but the existing halfspace/rank-tax audit
shows why an all-order residual inequality is still required.  In the
actual Turan provenance only (5.2), not a constant fraction, is automatic.

### One actual transverse condition can be proved: the canonical normal returns

Although the full residual inequality (5.16) remains open, the actual
integer-log geometry proves its necessary zero-direction condition for the
canonical positive normal.

First split a selected prime interval at `Y`.  If

```text
e(I,Y,t_0)>=N^(-d),                                  (5.26)
```

then one of the two one-sided prime intervals has mass-normalized negative
value at least `N^(-d)/2`.  Replace `I` by that side and let `lambda` be its
uniform prime probability.  All its absolute log nodes now come from the
same side of `Y`.

### Proposition 5.3 (positive return of a one-sided prime cell)

For every nonempty one-sided prime interval in the shell, with `M` selected
primes,

```text
sup_(t in H_Y) sum_(p in I)M^(-1)cos(t|log(p/Y)|)
 >=c_w/M                                               (5.27)
```

for all sufficiently large `Y`.

#### Proof

Write `u_p=|log(p/Y)|` and

```text
P(t)=M^(-1)sum_(p in I)cos(tu_p).                    (5.28)
```

Because `Y` is a half-integer and the `p` are distinct integers on one side,

```text
min_p u_p>=c_w/Y,
min_(p!=q)|u_p-u_q|>=c_w/Y.                          (5.29)
```

Hence the symmetric frequency set `{+/-u_p}` is `c_w/Y`-separated.  The
Montgomery--Vaughan Hilbert inequality on an interval of length
`L=|H_Y|=Y^(A+o(1))` gives

```text
L^(-1)int_(H_Y)P(t)^2dt
 >=(1-o(1))/(2M).                                    (5.30)
```

The first moment is much smaller.  Direct integration and the fact that the
distances `|p-Y|` are distinct positive half-integers give

```text
|L^(-1)int_(H_Y)P(t)dt|
 <=C_w L^(-1)M^(-1)sum_p u_p^(-1)
 <=C_w Y log(Y)/(LM)=o(1/M),                         (5.31)
```

because `A>1`.  Put `P_+=max(P,0)`.  Since `|P|<=1`,

```text
P^2<=|P|=2P_+-P.                                     (5.32)
```

Average (5.32), use (5.30)--(5.31), and bound the average of `P_+` by its
supremum.  This proves (5.27).  QED

In particular,

```text
h_Y(lambda)>0.                                       (5.33)
```

This matters because `lambda dot v=0`: any transverse return `-sv in P_Y`
must have zero `lambda`-projection, so `P_Y` must reach the nonnegative side
of the canonical functional.  Proposition 5.3 proves that necessary return
with room.  More explicitly, if `P(t_0)=-D` and `P(t_1)=G>0`, then

```text
[G/(D+G)]a(t_0)+[D/(D+G)]a(t_1)                    (5.34)
```

lies in `P_Y` and has zero `lambda`-projection.

What remains is orientation inside the `lambda`-orthogonal hyperplane.
Equation (5.34) is one point there; (5.18) asks for the particular ray
`-s[a(t_0)+Dq_0]`.  The signed duals in (5.16) can be supported on primes
outside `I` and on proper prime powers, so (5.27) does not control them.
This cleanly separates a proved actual-prime recurrence from the still-open
coefficient-sensitive radialization.

### Why global `ERAD` asks unnecessarily more

The corrected global supremum always has the unconditional singleton floor

```text
E_N^->=1/N.                                          (5.35)
```

Consequently (0.5) would force

```text
R_N^hi>=C^(-1/lambda)N^(-1/lambda)                  (5.36)
```

even when no Turan-sized event exists.  Such a polynomial lower bound is not
known; the generic gapped nuller gives only exponential depth.  The reverse
bridge for `d<=.019` never uses events as small as `N^-1`.  Therefore
`LTRAD_full(c,d)` is strictly better targeted than global `ERAD_hi(lambda)`.

---

## 6. Corrected frontier

The honest reverse bridge now reads

```text
zero near one
  => L_N(A') large
  => E_N^-(A') large                   [proved]
  => r_+(H_Y;S_Y) large                [LTRAD_full, open]. (6.1)
```

The weakest exact missing statement is `LTRAD_full(c,d)` in (5.1); global
(0.5) and `LTRAD_hi` are stronger optional versions.  Since `E_N^-` is
exponent-equivalent to the prime modulus, a fixed-power proof would be a genuinely new
actual-prime directional-to-radial theorem.  The available scalar KMT bound
is only logarithmic; the tent theorem controls one fixed diffuse direction;
and the Heath--Brown/Guth--Maynard estimates leave the adaptive repeated-
difference direction.  None proves (0.5).

Binary disposition:

```text
original probability-normalized D_N^-:                 IDENTICALLY 1;
original RAD_hi(lambda) as a Turan adapter:             CLOSED/MISNORMALIZED;
mass-normalized E_N^- removes singleton saturation:     PROVED;
L_N <= fixed constant * E_N^-:                          PROVED;
E_N^- <= fixed-scale enlarged prime modulus:            PROVED;
radial pairing factor for an M-prime interval:           EXACTLY M/N;
extra prime-power loss in that pairing:                  NONE;
von Mangoldt conversion cost:                            log N=N^o(1);
one-sided canonical prime cell returns positive on H_Y:  PROVED;
full signed transverse residual inequality (5.16):       OPEN;
translation/MW/convolution/partition closure:            NOT OBTAINED;
ERAD_hi(lambda) for any fixed lambda>0:                  OPEN;
thresholded long-interval LTRAD_hi(c,d):                 OPEN;
thresholded full-band LTRAD_full(c,d):                   OPEN (WEAKEST);
QP, QP-to-strip, or uniform strip:                       NOT PROVED.
```

Executable replay:

- `src/qp_radialization_mass_gate.py`;
- `src/test_qp_radialization_mass_gate.py`;
- `results/verify_zeta23_qp_radialization_mass_gate.py`.
