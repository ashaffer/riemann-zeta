# QP actual prime powers: fixed-`S` shifted-product rigidity and the surviving primitive gate

**Date:** 2026-08-25  
**Verdict:** the actual prime-power mask gives a real but structural gain.  It
collapses the whole zero-defect slice to the diagonal and the swapped tangent,
and it forces every nonzero small-defect solution into the primitive,
cross-coprime sector.  It does **not** bound the number of nonzero product
labels, carrier sums, or defects by `D^(1/2)q^o(1)`.

The special project centre `C=q^3/(8x)` does not supply an extra modulus after
the colour `x` is fixed.  Clearing its denominator merely replaces an integer
product label by one residue progression, bijectively.  Thus this audit gives
no new power saving in the remaining `m M^2<sqrt(D)` core and does not prove
the sharp four-cycle bound.

## 1. Exact support inherited from the QP model

The physical row, carrier, and colour coordinates all lie in

```text
P_q={p^k : (q/2)e^(-0.2)<=p^k<=(q/2)e^(0.2)}.          (1.1)
```

Its endpoint ratio is

```text
e^0.4<2.                                                (1.2)
```

Two different positive powers of one prime have ratio at least two.
Consequently `P_q` contains at most one power of each prime base.  In
particular, for distinct `u,z in P_q`,

```text
gcd(u,z)=1,                                             (1.3)
```

and unique factorisation gives the multiplicative-Sidon law

```text
u*z=u'*z'  =>  {u,z}={u',z'} as multisets.              (1.4)
```

Fix an actual colour `x in P_q`.  The true product window is

```text
I_x={n in Z: |8*x*n-q^3|<=H},       H<<qD.              (1.5)
```

Thus `#I_x<<D`, and the simplified centre is exactly

```text
C_x=q^3/(8x).                                           (1.6)
```

All four variables in the fixed-sum problem are actual nodes:

```text
a,b,v,w in P_q,       a+b=S,
n=a*v in I_x,         m=b*w in I_x.                    (1.7)
```

This is stronger than an arbitrary composite shell and is also stronger than
merely assuming that the four variables have few divisors.

## 2. Zero-defect rigidity is completely closed

Put

```text
X=n-m=a*v-b*w.                                          (2.1)
```

If `X=0`, (1.4) gives

```text
{a,v}={b,w}.                                            (2.2)
```

There are only two cases:

```text
a=b and v=w;                       (diagonal)
a=w and v=b.                       (swapped tangent)     (2.3)
```

The diagonal has at most one point after fixing `S`.  In the swapped case,
`b=S-a` and the product condition is

```text
a*(S-a) in I_x.                                         (2.4)
```

Since

```text
4*a*(S-a)=S^2-(2a-S)^2,                                 (2.5)
```

an interval of length `O(D)` contains only `O(1+sqrt(D))` relevant square
values.  Hence

```text
R_0(S;x)<<1+sqrt(D).                                    (2.6)
```

Unlike the full integer shell, there are no other rational tangent slopes:
actual prime powers have killed them exactly.

## 3. A nonzero small defect is primitive and cross-coprime

Let `L=min(P_q)` and suppose

```text
0<|X|<L.                                                (3.1)
```

If, for example, `a=b`, then

```text
X=a*(v-w),                                              (3.2)
```

which is either zero or has magnitude at least `L`.  The same argument after
the appropriate relabelling applies to `v=w`, `a=w`, and `b=v`.  Therefore

```text
{a,v} intersection {b,w}=empty.                        (3.3)
```

Using (1.3), this proves the exact identities

```text
gcd(a,b)=gcd(v,w)=1,
gcd(a*v,b*w)=1,
gcd(X,a*b*v*w)=1.                                      (3.4)
```

In particular, the complementary-divisor normal form has

```text
g=gcd(a,b)=1                                            (3.5)
```

throughout the nonzero sector.  This is important, but its direction is
opposite to a closure: the actual mask deletes every large-`g` chart and
leaves precisely the primitive `g=1` chart which the two-inverse argument
does not yet control.

## 4. The special centre gives an exact gcd, not a saving

Define the two physical residuals

```text
r=8*x*n-q^3,              s=8*x*m-q^3.                (4.1)
```

Then exactly

```text
r==s==-q^3 (mod 8x),
r-s=8*x*X.                                                (4.2)
```

By (3.4), every nonzero small-defect solution also obeys

```text
gcd(q^3+r,q^3+s)
 =gcd(8*x*n,8*x*m)=8*x.                                (4.3)
```

Equivalently,

```text
gcd(n,X)=1.                                             (4.4)
```

These are genuine exact consequences.  They do not shorten the label
interval.  For fixed `x`, the map

```text
n -> r=8*x*n-q^3                                       (4.5)
```

is a bijection between `I_x` and the admissible residuals in the single
class `-q^3 mod 8x`.  Once `X` is fixed, `s=r-8xX` automatically belongs to
the same class.  Condition (4.4) merely removes the residue classes of `n`
sharing a factor with `X`; for small fixed `X` it can leave a positive
proportion of all `O(D)` labels.

Thus clearing the physical denominator creates no second independent
congruence.  Any argument which counts the modulus `8x` as an additional
`q`-sized saving is counting the same integrality twice.

## 5. Exact surviving shifted-product formula

For an integer `n`, put

```text
F(n)={(u,n/u):u in P_q, u|n, n/u in P_q}.              (5.1)
```

The multiplicative-Sidon law gives

```text
#F(n)<=2,                                               (5.2)
```

the two possibilities being orientations of one unordered factor pair.
For fixed `(S,X,x)`, the nonzero count is exactly

```text
R_X(S;x)
 =sum_(n in I_x, n-X in I_x)
    sum_((a,v) in F(n))
      1_((S-a,(n-X)/(S-a)) in F(n-X)).                 (5.3)
```

Consequently UFD proves `O(1)` multiplicity **at each exact `n`**, but only

```text
R_X(S;x)<<D                                             (5.4)
```

after the `n`-sum.  Summing termwise over `X` is worse, while using product
fibre uniqueness first recovers only the familiar total `O(D)` bound.

The missing statement is therefore the selected shifted-semiprime
correlation

```text
sum_(0<|X|<<D) R_X(S;x)<<sqrt(D)*q^o(1),               (5.5)
```

or its equivalent occupied-carrier-sum/nonzero-dual formulation.  Neither
(1.4), (3.4), nor (4.3) proves (5.5).

## 6. Primes, proper prime powers, and composite shells

For a prime-only shell, the proof above is unchanged.  Away from the unique
small even exception all nodes are odd, so `X` is even.  This is only a
factor-two restriction.  The remaining formula (5.3) is a simultaneous
four-prime, short shifted-product correlation with a fixed additive
constraint.

Allowing proper prime powers does not reintroduce common factors: (1.2)
still permits only one node for each prime base.  The number of proper prime
powers in the shell is at most

```text
q^(1/2+o(1))=D^(33/32+o(1)),                           (6.1)
```

which is far above `sqrt(D)`.  Their global sparsity therefore cannot close
the target.  There is at most one even node (a power of two), and solutions
using it in any one of the four roles contribute only `O(1)` for fixed `S`;
the odd proper-power sector remains part of (5.3).

For an arbitrary composite integer shell, all three special properties can
fail: distinct nodes may share bases, `gcd(a,b)` may be nontrivial, and one
product can have divisor-many shell orientations.  Then `#F(n)` is only
`q^o(1)` rather than at most two, and `X=0` contains general rational tangent
packets.  Results proved for that larger shell remain valid majorants, but
they do not describe the sharper actual-mask rigidity above.

## 7. Exact finite evidence

There are nonzero physical solutions even with all five displayed nodes
prime and with the exact project centre.  For

```text
q=211,       x=113,       D=13,
(a,b,v,w)=(97,101,107,103),                            (7.1)
```

one has

```text
S=198,       U=210,       X=-24,
|8*x*a*v-q^3|<=8*x*D,
|8*x*b*w-q^3|<=8*x*D.                                 (7.2)
```

Thus nonzero `X` is not eliminated by primality, UFD, or the special centre.

There can also be more than one nonzero carrier-sum level at the same exact
centre and fixed `S`.  With

```text
q=4951,      x=2557,      D=62,       S=5016,          (7.3)
```

the two all-prime rows

| `a` | `b` | `v` | `w` | `U` | `X` |
|---:|---:|---:|---:|---:|---:|
| 2399 | 2617 | 2473 | 2267 | 4740 | -12 |
| 2473 | 2543 | 2399 | 2333 | 4732 | -92 |

both satisfy the two exact residual inequalities in (7.2) with the new
parameters.  This is not an asymptotic counterexample; it is a finite audit
showing that the nonzero projection is genuinely present.

The earlier prime-only sweep at arbitrary centres found at most two
scattered levels for `q<=1200`.  That experiment omitted higher prime powers
and did not enforce (1.6), so it cannot be cited as evidence for an exponent.
The exact-centre fixtures above repair the support mismatch but are likewise
only consistency checks.

The shell, defect, residual-gcd, and fixture identities are machine-checked
in `src/qp_fixed_s_packet_dispersion_audit.py` and
`src/test_qp_fixed_s_packet_dispersion_audit.py`.

## 8. Binary status

```text
actual shell has one node per prime base:              PROVED;
distinct actual nodes are pairwise coprime:            PROVED;
fixed product has at most two orientations:            PROVED;
actual X=0 slice is diagonal or swapped tangent:       PROVED;
actual X=0 count O(sqrt(D)):                            PROVED;
nonzero |X|<min(shell) is primitive/cross-coprime:      PROVED;
physical residual gcd equals 8*x:                      PROVED;
special centre gives a further q-sized modulus gain:   FALSE;
UFD gives O(1) per exact product label n:               PROVED;
UFD sums the O(D) nonzero labels with power saving:     NO;
actual-prime scattered nonzero levels exist:           VERIFIED;
actual-prime-power fixed-S sqrt(D) bound:               OPEN;
remaining m M^2<sqrt(D) core:                           OPEN;
sharp four-cycle bound:                                 NOT PROVED.
```
