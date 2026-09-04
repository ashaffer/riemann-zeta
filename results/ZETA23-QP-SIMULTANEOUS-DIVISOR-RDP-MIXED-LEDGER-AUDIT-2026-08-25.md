# QP residual degree product: simultaneous-divisor and mixed-ledger audit

**Date:** 2026-08-25
**Verdict:** the residual degree-product theorem

```text
deg(b,B) deg(c,C) << D q^o(1)                       (RDP)
```

is **not proved or refuted**.  Two tempting shortcuts are now closed
decisively:

1. endpoint gcds do not yield a square-root arm bound;
2. although the two-arm error ledger has an `O(D^2)` mixed remainder,
   `D^2<q` does not force it to vanish.

The strongest new exact statement is the mixed-error formula in Section 3.
It exposes a genuine small bilinear remainder, but the four weights have
different denominators `x_i y_j`; there is no common modulus of size `q`.

## 1. Exact gcd information and its limit

Fix a residual edge

```text
(b,B) -- (c,C),             delta=b*c-B*C !=0.
```

The two base hard windows give `|delta|<<D`.  If

```text
g_L=gcd(b,B),               g_R=gcd(c,C),
```

then exactly

```text
lcm(g_L,g_R) | delta.                                (1.1)
```

For a left neighbor `(d,D')`, put `k=b*d-B*D'`.  Then `g_L|k` and
`|k|<<D`.  For fixed `k`, the integral solutions differ by

```text
(d,D') -> (d+B/g_L, D'+b/g_L).
```

Consequently a fixed proportional shell gives only the elementary bound

```text
deg(b,B)
 <<(1+D/g_L)(1+g_L)
 <<D+g_L+D/g_L.                                    (1.2)
```

The row witness is unique once `(b,d)` is fixed because its interval has
length `O(D/q)<1`.

There is no improvement to `min(g,D/g)`.  The literal affine hard-window
biclique in the tangent/Pluecker report has consecutive endpoint
coordinates, hence `g_L=g_R=1`, and both arms have length `asymp sqrt(D)`.
Thus the proposed gcd bound would give `O(1)` on a physical family where the
truth is `Omega(sqrt(D))`.

On the actual narrow prime-power shell, two distinct endpoint coordinates
are coprime, so every residual endpoint has `g_L=g_R=1`.  Formula (1.2) then
gives only `O(D)`.  The finite actual-shell scans having residual degree one
do not turn this into an asymptotic theorem.

## 2. Individual-arm status

For a base row/color triple `(a,c,C)`, a left neighbor with row `x` obeys

```text
|x*d-a*c|<<D,                 |x*D'-a*C|<<D.         (2.1)
```

It therefore follows a dilated curve

```text
t -> (t,A/t,B/t).                                  (2.2)
```

The last two coordinates in (2.2) are proportional.  Its torsion is
identically zero, so the nonvanishing-torsion space-curve estimates do not
apply.  Even ignoring that failed hypothesis, Huang's bound has generic
error `q^(3/5+o(1))`, whereas the needed arm scale is

```text
sqrt(D)=q^(8/33+o(1)).                              (2.3)
```

See J.-J. Huang, [Integral points close to a space
curve](https://arxiv.org/abs/1809.07796).  Planar near-curve estimates also
do not retain the linked second product mask and are numerically too large.

The physical affine family proves that a uniform `O(sqrt(D))` arm theorem,
if true, is sharp.  No proof of it is known here.  No super-square-root
physical arm and no actual-prime-power counterexample was found.  These are
finite observations, not asymptotic conclusions.

## 3. Exact two-arm mixed-error ledger

Around one shared edge write the six triples as

```text
(a,b,c), (a,B,C),
(x,b,d), (x,B,D'),
(y,e,c), (y,E,C).
```

Define the divided product errors

```text
alpha=x*d-a*c,             beta=x*D'-a*C,
gamma=y*e-a*b,             eta=y*E-a*B.             (3.1)
```

Every one has size `O(D)`.  Direct expansion gives the exact identity

```text
x*y*(d*e-D'*E)
 =a^2*(b*c-B*C)
  +a*b*alpha-a*B*beta
  +a*c*gamma-a*C*eta
  +alpha*gamma-beta*eta.                            (3.2)
```

For left indices `i=1,2` and right indices `j=1,2`, put

```text
W_ij=x_i*y_j*(d_i*e_j-D_i*E_j).
```

The constant and one-variable terms in (3.2) cancel under a rectangular
mixed difference, leaving exactly

```text
W_11-W_12-W_21+W_22
 =(alpha_1-alpha_2)(gamma_1-gamma_2)
  -(beta_1-beta_2)(eta_1-eta_2).                    (3.3)
```

Hence the right side is `O(D^2)=o(q)` at the active aperture.  This is a
real second-order gain.  It does **not** imply that (3.3) vanishes: its left
side is a combination of multiples of four different numbers `x_i*y_j`,
not a multiple of one common `q`-scale integer.

## 4. Literal prime-`q` no-go for automatic vanishing

Take

```text
q=809 (prime),             D=26,             D^2=676<q,
(a,b,B,c,C)=(377,391,440,449,399),
(x,d,D')=(349,485,431),
(y,e,E)=(440,335,377).
```

The six residuals `8uvw-q^3` are

```text
10815, 13831, -14209, -249, -14329, 13831,
```

all bounded by `qD=21034`.  All coordinates lie in the same fixed
proportional shell.  The four cross determinants (base/neighbor by
base/neighbor) are

```text
(-1, -8;
 -5,-12),                                               (4.1)
```

so every corner is residual and lies in the required `O(D)` strip.
Relative to the base point, the nonzero error pairs are

```text
(alpha,beta)=(-8,-4),       (gamma,eta)=(-7,0).
```

Therefore (3.3) equals

```text
(-8)*(-7)-(-4)*0=56 !=0.                              (4.2)
```

This is a literal six-window instance at a prime scale below the
square-root aperture.  Its coordinates are ordinary integers, not all
prime powers, and its degree product is small.  Thus it is **not** an RDP
counterexample.  It proves exactly that shell integrality, the six hard
windows, prime `q`, and `D^2<q` do not force the mixed remainder to vanish.

## 5. Remaining theorem

The surviving target is still a two-sided inverse theorem:

```text
if both physical arms are large and every Cartesian cross determinant
is O(D), extract a rank-one/affine ruling of sufficient density;
otherwise prove deg_L*deg_R <<D q^o(1).              (5.1)
```

Equation (3.3) may be useful inside such an inverse theorem, especially
after fixing or compressing error directions.  By itself it recovers only
the already understood rank-one situation where the error-difference
pairings vanish.  The scattered, varying-error case remains open.

Mechanical checks:

```text
PYTHONPATH=src pytest -q src/test_qp_simultaneous_divisor_rdp.py
(cd lean/weilcert && lake env lean QPSimultaneousDivisorRDP.lean)
```

Binary status:

```text
lcm endpoint-gcd divisibility:                       PROVED;
elementary gcd/lift arm bound O(D+g+D/g):             PROVED;
min(g,D/g) arm bound:                                 FALSE;
exact mixed-error ledger (3.2)--(3.3):                PROVED;
D^2<q forces mixed remainder zero:                    FALSE;
individual physical arm O(sqrt(D)q^o):                OPEN;
actual-prime-power RDP counterexample:                 NOT FOUND;
uniform residual degree-product theorem:              OPEN.
```
