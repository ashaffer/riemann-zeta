# QP reciprocal strip: fixed-`S` packet-or-dispersion gap audit

**Date:** 2026-08-25  
**Verdict:** the desired bound on occupied noncentral quotient sums is **not
proved**.  The attack produces exact two-level gap laws, a simultaneous
continued-fraction criterion for close pairs, and a sharp bound for every
actual affine rank-one packet.  These statements isolate the missing global
step: widely separated levels can avoid every local packet trigger, and the
current identities do not bound their number by `sqrt(D)`.

There is no power counterexample.  A finite full-integer fixture with eight
different scattered quotient sums shows, however, that distinct levels do
not automatically merge into one tangent packet.

## 1. Setup and centred coordinates

Let

```text
a+b=S asymp q,          v+w=U asymp q,
n=a*v=C+e,              m=b*w=C+f,
|e|,|f|<=D,             q=D^(33/16).                  (1.1)
```

Use doubled centred variables

```text
x=a-b,                  z=v-w,
sigma=e+f,              tau=e-f=n-m.                  (1.2)
```

Then exactly

```text
U*x+S*z=2*tau,                                           (1.3)
S*U+x*z=4*C+2*sigma,                                    (1.4)
U*(S^2-x^2)+2*tau*x=4*C*S+2*S*sigma.                   (1.5)
```

In particular

```text
U*x ==2*tau (mod S).                                    (1.6)
```

Equation (1.5) is both the Archimedean square law and the exact error
ledger.  It says that `U` is the unique integer, if any, in a window of
length `O(D/q)<1` around

```text
4*C*S/(S^2-x^2).                                        (1.7)
```

Equation (1.6) is the second, linked inverse condition.

## 2. One exceptional quotient sum, then one point per level

Writing

```text
a=S/2+h,       b=S/2-h,
v=U/2+k,       w=U/2-k,                                (2.1)
```

gives

```text
n-m=U*h+S*k,
(n+m)/2=S*U/4+h*k.                                     (2.2)
```

Eliminating `k` yields the necessary condition

```text
|S*U/4-C-(U/S)*h^2|<<D.                                (2.3)
```

As `U` increases by one, the centre on the left increases by
`S/4 asymp q`.  There is at most one exceptional first level at which the
corresponding interval for `h^2` can start near zero.  It has
`O(sqrt(D))` points.

At every later admissible level the interval for `h^2` has length `O(D)`
and is centred at `>>q`.  Consecutive squares there are separated by
`>>sqrt(q)>D`, since `q>D^2`.  Hence every later `U` supports only `O(1)`
solutions.  Therefore

```text
R(S)<<sqrt(D)+#{occupied scattered U-levels}.          (2.4)
```

The exact packet-or-dispersion target is

```text
#{occupied scattered U-levels}<<sqrt(D)*q^o(1).        (2.5)
```

## 3. Exact laws between two occupied levels

Take two solutions, indexed `i,j`, and put

```text
r=x_j-x_i,                 Delta=U_j-U_i,
A_i=S^2-x_i^2.                                         (3.1)
```

Subtracting (1.5) gives the exact quadratic gap law

```text
Delta*A_i-U_j*r*(x_i+x_j)
 =2*S*(sigma_j-sigma_i)
  -2*(tau_j*x_j-tau_i*x_i).                           (3.2)
```

Its right side is `O(D*q)`.  Cross-multiplying the two congruences (1.6)
also gives

```text
S | U_i*U_j*r-2*(U_i*tau_j-U_j*tau_i).                (3.3)
```

Thus the Archimedean gap and modular gap are not independent: they share
the same error labels `sigma_i,tau_i`.  Formulae (3.2)--(3.3) are the exact
two-level laws requested by the fixed-`S` reduction.

They do not yet imply (2.5).  The correction in (3.3) has size `O(D*q)`,
large enough to fill all residue classes modulo `S`, and at the target
cardinality the labels need not repeat.

## 4. Ordered matching and simultaneous continued fractions

Order two distinct solutions so that `a_2>a_1` and put

```text
r=a_2-a_1,
p=v_1-v_2,
s=w_2-w_1.                                             (4.1)
```

Because all products lie in one interval of length `2D<q`, monotonicity is
strict:

```text
p>0,                   s>0.                            (4.2)
```

Indeed, otherwise changing a factor of size `asymp q` by at least one
would change its product by more than `2D`.  The two product changes are
exactly

```text
v_1*r-a_2*p=n_2-n_1,
b_2*s-w_1*r=m_2-m_1.                                  (4.3)
```

Consequently

```text
|p/r-v_1/a_2|<<D/(q*r),
|s/r-w_1/b_2|<<D/(q*r).                               (4.4)
```

If

```text
r<c*q/D                                                   (4.5)
```

for a sufficiently small shell-dependent `c`, each reduced fraction in
(4.4) satisfies Legendre's criterion.  Thus the same denominator gap `r`
produces a continued-fraction approximant in **both** reciprocal legs.
This is a rigorous local rank-one trigger.

It does not close the global problem.  The threshold in (4.5) is

```text
q/D=D^(17/16).                                         (4.6)
```

An interval of length `q` can contain `asymp D` points separated by this
amount.  The desired number is only `sqrt(D)`, so a set at the critical
cardinality can avoid every close-gap trigger by a full factor `sqrt(D)`.
This is the exact local-to-global loss, not a looseness in Legendre's
criterion.

## 5. Fixed-residue factorisation law

Let `C_0` be any fixed integer within `O(1)` of `C` and define

```text
E_i=n_i-C_0,              F_i=m_i-C_0,
X_i=S*v_i-C_0,            Y_i=S*w_i-C_0.              (5.1)
```

Then

```text
X_i==Y_i==-C_0 (mod S),                                (5.2)

X_i*Y_i-C_0^2
 =S*(E_i*w_i+F_i*v_i).                                 (5.3)
```

Thus every solution lies on one fixed residue lattice near a hyperbola;
the product displacement in (5.3) is `O(D*q^2)`.  For two solutions,

```text
Y_j*(v_j-v_i)+X_i*(w_j-w_i)
 =(E_j*w_j+F_j*v_j)-(E_i*w_i+F_i*v_i).                (5.4)
```

The right side is `O(D*q)`.  Since `X_i,Y_j asymp q^2`, (5.4) gives another
proof that the two quotient differences have opposite signs.

If the error pair `(E,F)` repeats, (5.4) collapses to the exact rank-one
law

```text
a_j*w_j*(v_j-v_i)+b_i*v_i*(w_j-w_i)=0.                (5.5)
```

But there are `O(D^2)` possible error pairs and only `sqrt(D)` points at
the desired threshold.  Repetition cannot be used as the global extraction
mechanism.  Fixed-label factorisation gives `q^o(1)` multiplicity, while
unique labels remain the hard case.

## 6. Every actual affine rank-one packet is already sharp

Suppose a family lies on one integral affine direction:

```text
a_j=a_0+r*j,       b_j=b_0-r*j,
v_j=v_0-p*j,       w_j=w_0+s*j                         (6.1)
```

for consecutive integers `j`, with positive `r,p,s`.  Then

```text
a_j*v_j=n_0+(r*v_0-p*a_0)*j-r*p*j^2,
b_j*w_j=m_0+(b_0*s-r*w_0)*j-r*s*j^2.                  (6.2)
```

The range of a quadratic with leading coefficient of magnitude `A` on
`L` consecutive integers is `>>A*L^2`.  Since both products stay in
intervals of length `2D`, (6.2) gives

```text
L<<1+min(sqrt(D/(r*p)),sqrt(D/(r*s)))<<sqrt(D).       (6.3)
```

This includes packets with changing quotient sum
`U_j=U_0+(s-p)j`, not only the aligned tangent family `s=p`.  Therefore a
successful inverse theorem may safely output a macroscopic affine packet:
the packet itself is already at the sharp scale.  What is unproved is that
too many scattered levels must have such a common direction.

## 7. A physical scattered fixture

The following is a full-integer configuration, not an abstract incidence
model:

```text
q=800,       D=26,       S=2176,       C=1228776.
```

For the eight rows below, `a+b=S`, all four factors lie in `[q,2q)`, and
both product errors have absolute value at most `D`.

| `a` | `b` | `v` | `w` | `U=v+w` | `a*v-C` | `b*w-C` |
|---:|---:|---:|---:|---:|---:|---:|
| 800 | 1376 | 1536 | 893 | 2429 | 24 | -8 |
| 917 | 1259 | 1340 | 976 | 2316 | 4 | 8 |
| 926 | 1250 | 1327 | 983 | 2310 | 26 | -26 |
| 957 | 1219 | 1284 | 1008 | 2292 | 12 | -24 |
| 963 | 1213 | 1276 | 1013 | 2289 | 12 | -7 |
| 976 | 1200 | 1259 | 1024 | 2283 | 8 | 24 |
| 983 | 1193 | 1250 | 1030 | 2280 | -26 | 14 |
| 999 | 1177 | 1230 | 1044 | 2274 | -6 | 12 |

Reflecting each row by `(a,b,v,w)->(b,a,w,v)` gives sixteen solutions on
the same eight quotient sums.  Each level has only its reflected pair; the
eight levels do not form one affine packet.  This is a constant-scale
warning, not an asymptotic counterexample: `8` is only a constant multiple
of `sqrt(26)`.

## 8. Literature and exact status

General rational-point estimates near planar curves do not retain both the
fixed denominator sum and the linked product labels.  For example, Huang's
near-curve theorem treats a broader denominator average and does not imply
(2.5): [Rational points near planar curves and Diophantine
approximation](https://arxiv.org/abs/1403.7388).

The identities and finite fixture are checked in
`src/qp_pair_sum_selberg_ledger.py` and
`src/test_qp_pair_sum_selberg_ledger.py`.

```text
centred one-level equations (1.3)--(1.5):              PROVED;
exceptional U <=sqrt(D), later levels O(1):           PROVED;
quadratic two-level gap law (3.2):                    PROVED;
cross-level congruence (3.3):                        PROVED;
ordered matching and determinant laws (4.2)--(4.4):  PROVED;
simultaneous close-gap CF trigger (4.5):              PROVED;
fixed-residue factorisation (5.2)--(5.4):             PROVED;
affine rank-one packet length <=sqrt(D):              PROVED;
eight-level physical fixture:                         VERIFIED;
many scattered levels force one rank-one packet:     OPEN;
occupied scattered-level bound (2.5):                OPEN;
fixed-S pointwise sqrt(D) theorem:                    NOT PROVED;
power counterexample:                                 NOT FOUND.
```
