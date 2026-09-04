# LTRAD actual-prime audit: short prime clusters cannot carry the hard core

**Date:** 2026-08-28  
**Verdict:** the Fejer hard core from the abstract hereditary obstruction
cannot be transferred to the actual primes by placing its carrier in a short
physical prime cluster.  This remains true for an arbitrary **signed**
carrier-one coefficient vector, not only for positive Fejer weights.

**Subsequent strengthening.**  The threshold proved here is valid but not
sharp for this method.  The localized frame range should cost `sqrt(M)` for
the active packet, rather than the global `sqrt(Delta)` fourth-moment loss.
That correction alone gives `theta>=(2+3c)/7-o(1)`.  Calibrating the common
antipode gives `theta>=(1+c)/3-o(1)` and removes the prime-parity assumption,
so the result extends to localized distinct integer/prime-power nodes.  See
`ZETA23-UNIFORM-STRIP-DECISION-TREE-CONSOLIDATION-AND-MAXIMUM-INFORMATION-GAIN-2026-08-30.md`.

Fix `w>0`, `0<a<1`, `1<A<2`, and

```text
0<c<5/4-A/2.                                        (0.0)
```

For a family of half-integer centers `Y=N+1/2` tending to infinity, let

```text
Y=N+1/2,                 B=Y^A,              1<A<2,
H_Y=[Y^a,B],             0<a<1,
F_y(t)=sum_(p in P)y_p cos(t|log(p/Y)|),
sum_(p in P)y_p=1,
```

where each `P=P_Y` is a nonempty set of distinct ordinary primes contained
in the fixed shell and in one physical interval of diameter at most
`Y^theta`, for one fixed `0<=theta<1/2`.  The coefficients and the carrier
interval may depend arbitrarily on `Y`.  If

```text
inf_(t in H_Y) F_y(t) >= -Y^(-c),
```

holds for every sufficiently large member of the family, then necessarily

```text
theta >= (3A-2+6c)/11-o(1).                         (0.1)
```

At the project aperture `A=50/33` and `c=.019`, the right side is

```text
28/121 + 6(.019)/11 = .2417685950... .              (0.2)
```

Equivalently, for every fixed `epsilon_0>0`, no such family exists with
`theta<=(3A-2+6c)/11-epsilon_0`.  Assumption (0.0) makes this threshold
strictly smaller than `1/2`, which is the range used by the proof.  Without
(0.0), the same argument gives only the capped statement with threshold
`min(1/2,(3A-2+6c)/11)`.

Thus no carrier supported entirely in a prime cluster of diameter
`Y^(.2417-epsilon_0)` can furnish the project-strength Delsarte antenna.  In
particular, a lone cluster containing the `Y^(.019+o(1))` nodes needed for a
nominal Fejer floor does not by itself realize the abstract hard core.

This is a method-scoped no-go.  It does not prove `LTRAD_full`: an adaptive
dual may be delocalized across the shell, may use proper prime powers, may
have a short-cluster core plus correction tails elsewhere, and may use the
selected long Turan interval only through a calibrated correlation.  The
theorem rules out only a carrier whose complete support lies in one short
physical ordinary-prime interval; it does not rule out multi-cluster or
approximately localized antennas.

---

## 1. A common antipode for every short cluster

Put `W=Y^theta` and choose

```text
R=Y^xi,                 xi=(1+theta)/3.              (1.1)
```

For fixed `theta<1/2`, one has `W=o(R)` and `R=o(Y^(1/2))`.
There are two cases.

We use the clustered quadratic form already established for the complete
actual prime-power shell.  Split the positive frequencies into singleton
blocks and lower/upper pairs at spacing `<c_w/Y`.  For a singleton the block
energy is `|y_j|^2`.  For a pair put

```text
z=min(1,B|u_j-u_k|),
p=y_j+y_k,                  q=z(y_j-y_k),
E_block(y)=|p|^2+|q|^2,                              (1.1a)
```

and let `E_Y(y)` be the sum of the block energies.  The proved frame theorem
states that `int F_y^2 rho_B asyp E_Y(y)`.

For a functional `b dot y` restricted to vectors supported on `P`, define

```text
||b||_(E_Y^*,P)=sup_(y!=0, supp y subset P)
                    |b dot y|/E_Y(y)^(1/2).          (1.1b)
```

If both endpoints of a pair belong to `P`, its dual block is, up to absolute
factors,

```text
|b_j+b_k|^2+|b_j-b_k|^2/z^2.                        (1.1c)
```

If only one endpoint belongs to `P`, then `E_block(y)>=|y_j|^2`, so the
restricted dual cost is at most `|b_j|`.  This last observation prevents an
outside zero coefficient from creating an artificial divided-difference
loss.

### 1.1 The cluster is central

Suppose one prime in the cluster has distance at most `2R` from `Y`.
Then every carrier prime has

```text
p=Y +/- h,              h in Z+1/2,       h<=3R.    (1.2)
```

Take the legal height

```text
t_*=2 pi Y asyp Y.                                  (1.3)
```

Taylor's formula gives

```text
Y |log(1 +/- h/Y)| = h+O(h^2/Y).                    (1.4)
```

Since `2 pi h` is an odd multiple of `pi`, (1.3)--(1.4) imply

```text
delta_p:=1+cos(t_*|log(p/Y)|)
          <<R^4/Y^2.                                (1.5)
```

The half-integer center is essential: it turns every nearby integer node
into the same approximate antipode.

Paired lower/upper nodes do not spoil the estimate in the clustered energy.
Write their half-distances as `h_-` and `h_+`.  Fix the frame's clustering
constant `c_w` sufficiently small that `0<c_w<1/4`.  The pair condition
`|u_--u_+|<=c_w/Y` gives

```text
|(h_--h_+)+O(R^2/Y)|<=c_w.                          (1.5a)
```

Here `h_--h_+` is an integer and `R^2/Y=o(1)`.  Hence (1.5a) forces that
integer to vanish for large `Y`.  Thus such a pair has one common physical
half-distance `h`, and

```text
|u_--u_+| asyp h^2/Y^2,
|delta_--delta_+| <<h^5/Y^3.                        (1.6)
```

In the divided-difference coordinate

```text
z=min(1,B|u_--u_+|),
```

(1.5)--(1.6) give

```text
|delta_-+delta_+| + |delta_--delta_+|/z
 <<R^4/Y^2.                                         (1.7)
```

For `z<1`, (1.6) and
`z=B|u_--u_+|asymp B h^2/Y^2` give

```text
|delta_--delta_+|/z <<h^3/(BY)<<R^4/Y^2,            (1.7a)
```

using `B>Y` and `R>=1`.  For `z=1`,

```text
|delta_--delta_+|/z<<h^5/Y^3<<R^4/Y^2              (1.7b)
```

because `h<=R<Y`.  These are the two divided-difference cases used below.

### 1.2 The cluster is far from the center

Otherwise the cluster is wholly on one side of `Y`.  Fix a carrier prime
`p_0`, put `u_0=|log(p_0/Y)|`, and choose an odd-phase height

```text
t_*=(2l+1)pi/u_0
```

nearest to `pi p_0`.  Then

```text
|t_*-pi p_0|<=pi/u_0<<Y/R,             t_*asympY.   (1.8)
```

All large ordinary primes are odd, so `p-p_0` is even.  Expanding
`log(p/p_0)` therefore gives, modulo `2 pi`,

```text
t_*|log(p/Y)|
 =pi (mod 2pi)+O(W/R+W^2/Y).                        (1.9)
```

Consequently

```text
delta_p<<W^2/R^2+W^4/Y^2.                           (1.10)
```

With (1.1), the central and far bounds balance:

```text
R^4/Y^2 = Y^((4theta-2)/3),
W^2/R^2 = Y^((4theta-2)/3),
W^4/Y^2 <=Y^((4theta-2)/3).                         (1.11)
```

Thus in both cases there is a legal `t_*asympY` for which every carrier
coordinate is `-1+delta_p`.  Equations (1.1b)--(1.1c), (1.5),
(1.7a)--(1.7b), and (1.10), followed by Cauchy--Schwarz over the at most `M`
blocks meeting `P`, give the restricted clustered-frame dual norm

```text
||delta||_(E_Y^*,P)
 <<sqrt(M)Y^((4theta-2)/3),          M=#P.           (1.12)
```

This statement concerns the functional restricted to coefficients supported
on `P`; it makes no claim that `delta` is small on shell nodes outside the
carrier interval.

---

## 2. Escaping the antipode forces large clustered energy

Assume the proposed antenna has floor `-epsilon`, with `epsilon=o(1)`.
At the height from Section 1,

```text
F_y(t_*)=-1+y dot delta >=-epsilon,
```

so `y dot delta>=1-o(1)`.  Dual Cauchy--Schwarz and (1.12) yield

```text
E_Y(y)^(1/2)
 >>M^(-1/2)Y^((2-4theta)/3).                        (2.1)
```

There are at most `W+1` integers in the carrier interval, hence

```text
M<=Y^(theta+o(1)),
E_Y(y)^(1/2)>>Y^(2/3-11theta/6-o(1)).               (2.2)
```

This is where signed adaptivity is paid for.  Positive weights cannot escape
the common antipode at all; signed weights can do so only through a large
sum/difference energy, including the correctly scaled reflected difference
coordinates.

---

## 3. Large energy forces a negative excursion elsewhere

The already proved actual-log fourth-moment theorem applies to every signed
coefficient vector on the complete prime-power shell, and hence to the
zero-extension of a vector supported on `P`.  With

```text
Delta=1+Y^2/B=Y^(2-A+o(1)),                         (3.1)
```

it gives

```text
int F_y^2 rho_B asyp E_Y(y),
int F_y^4 rho_B <<Delta E_Y(y)^2,                   (3.2)
```

The actual frame mean estimate is, for every fixed `K`,

```text
|m_y|:=|int F_y rho_B|
 <<_(w,K) sqrt(M_Y)(Y/B)^K E_Y(y)^(1/2),             (3.2a)
```

where the complete shell size satisfies `M_Y<<Y/log Y`.  Choose `K` so that
the right side of (3.2a) is
`o(Delta^(-1/2)E_Y(y)^(1/2))`, uniformly in `y`.

Interpolation gives

```text
int |F_y|rho_B
 >=(int F_y^2rho_B)^(3/2)/(int F_y^4rho_B)^(1/2)
 >>Delta^(-1/2)E_Y(y)^(1/2).                        (3.2b)
```

The established positive-range argument applied first to `y` and then
separately to `-y` uses (3.2a) with means `m_y` and `-m_y`.  It therefore
gives both signed excursions.  In particular,

```text
-inf_(t in H_Y)F_y(t)
 >>Delta^(-1/2)E_Y(y)^(1/2).                        (3.3)
```

Combining (2.2)--(3.3) proves

```text
-inf F_y
 >>Y^[A/2-1/3-(11/6)theta-o(1)].                   (3.4)
```

If the floor were `-Y^(-c)`, (3.4) would require

```text
A/2-1/3-(11/6)theta <=-c+o(1),
theta >=(3A-2+6c)/11-o(1),                          (3.5)
```

which is (0.1).

---

## 4. Consequence for the LTRAD decision tree

The abstract hereditary countermodel hides a small Fejer carrier while its
long negative interval lives on the complement.  Equations (0.1)--(0.2)
rule out an actual embedding in which the *entire* carrier is replaced by
ordinary primes from one short physical interval, even if its coefficients
are signed and arbitrarily large.

Any actual-prime obstruction to `LTRAD_full` must instead use at least one of
the following features:

1. a carrier not contained in any physical interval of diameter
   `Y^(.2417-epsilon_0)` (this includes multi-cluster carriers and short
   cores with correction tails);
2. a material proper-prime-power component;
3. a genuinely global reflected-pair construction; or
4. a calibrated dual coupling to the long Turan event which is not visible
   from support localization alone.

The result does **not** control those possibilities.  In particular it does
not establish `LTRAD_full(c,d)`, a QP upper bound, a QP-to-strip implication,
or a zero-free strip.

---

## 5. A stronger rigidity for the literal one-sided Fejer transfer

There is a complementary obstruction when the proposed hard core literally
shadows one harmonic log progression on one side of `Y`.  Let `L=L(Y)` tend
to infinity with `L=o(Y)`.  Suppose `h>0`, the primes `p_1,...,p_L` are
distinct, the matching below is injective, and

```text
u_(p_j)=j h+e_j,                  1<=j<=L,           (5.1)
```

all `p_j` are ordinary primes on the same side of `Y`, and the triangular
Fejer weights

```text
lambda_j=2(L+1-j)/[L(L+1)]                         (5.2)
```

are transferred through the standard Lipschitz budget

```text
B sum_j lambda_j |e_j| <<1/L.                       (5.3)
```

For every `j<=L/2`, (5.2)--(5.3) imply

```text
|e_j|<<1/B.                                         (5.4)
```

Write `sigma=+1` above the center and `sigma=-1` below it.  Then

```text
p_j=Y exp[sigma(jh+e_j)]
    =Y exp(sigma jh)+O_w(Y/B).                      (5.5)
```

The ideal sequence in (5.5) has second difference `O_w(Yh^2)`, while
the error contributes only `O_w(Y/B)=o(1)`.  Therefore, if

```text
h=o(Y^(-1/2)),                                      (5.6)
```

the integer second differences of `p_1,...,p_floor(L/2)` vanish identically
for all large `Y`.  These primes form an exact ordinary arithmetic
progression.

Put `K=floor(L/2)`.  The progression has nonzero common difference because
the matching primes are distinct.  Since `L=o(Y)` and every shell prime is
`asymp_wY`, one has `p_j>K` for large `Y`.  If an arithmetic progression
contains these `K` primes, its common difference is divisible by every
prime `ell<=K`: otherwise the first `ell` consecutive terms cover every
residue modulo `ell`, so one is `0 mod ell`; it cannot equal `ell` because
it is larger than `K`.  Hence the absolute common difference is at least

```text
product_(ell<=K, ell prime) ell=exp[(1+o(1))K].      (5.7)
```

Since the progression lies in a fixed shell, its total span is `O(Y)`.
Equations (5.7) and `K=floor(L/2)` force

```text
L<<log Y.                                           (5.8)
```

Quantitatively, the same integer argument applies whenever
`h<=c_wY^(-1/2)` for a sufficiently small fixed `c_w`; hence a
polynomial-length one-sided Fejer transfer, say
`L=Y^(ell+o(1))` with `0<ell<1`, must have

```text
h>>_wY^(-1/2),
physical carrier diameter
  >>_w min(Y,L sqrt(Y))=Y^(min(1,1/2+ell)-o(1)).    (5.9)
```

For the nominal project core `ell=.019`, this is diameter at least
`Y^(.519-o(1))`.

This argument does not cover an arbitrary interlacing of upper and lower
prime nodes along the harmonic indices, nor a nonharmonic signed antenna.
It does close the most literal route from the abstract Fejer construction to
a one-sided actual-prime progression.
