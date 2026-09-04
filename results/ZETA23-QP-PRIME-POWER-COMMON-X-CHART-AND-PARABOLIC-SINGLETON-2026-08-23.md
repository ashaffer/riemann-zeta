# QP parabolic singleton: the prime-power common-`X` chart

**Date:** 2026-08-23  
**Verdict:** integrality of the two first color coordinates puts the common
chart parameter `X` in one residue class modulo both `s2` and `r2`.  For
unrestricted integers this gives chart length `q/lcm(r2,s2)`.  The actual
prime-power shell improves it uniformly to

```text
# X on one chart <<1+q/(R*S).                         (0.1)
```

Indeed, if `d=gcd(r2,s2)>1`, the congruences force `d|X`, so every actual
prime power `X` on the chart has one fixed prime base.  The project shell,
whose diameter is smaller than its minimum, contains at most one power of
that base.  If `d=1`, the Chinese remainder modulus is `|r2*s2|~R*S`.

On a flat coefficient bin of support `M`, (0.1) gives the block estimate

```text
W_chart
 <<R^2*S^2*E*T*min(M,1+q/(R*S))*M^(-2)*q^o(1)
   *||z_bin||_2^4.                                  (0.2)
```

This removes the principal determinant obstruction in the parabolic
singleton sector.  Combining (0.2) with the existing principal estimate
shows that the principal singleton exponent is at most `23/24`.  The
remaining nonprincipal mixed-`H^2` estimate has sharp ledger exponent

```text
137/128.                                            (0.3)
```

Thus the complete parabolic singleton estimate supplied by these inputs is
`D^(137/128+o(1))`, not the former `D^(9/8+o(1))`.  This does not improve
the separately treated broad sector or the `D^(71/64)` parabolic curvature
term, and it does not prove the sharp four-cycle theorem.

---

## 1. The two exact congruences

Fix primitive nonzero relation directions

```text
r=(r1,r2),              s=(s1,s2),
||r||_infinity~R,       ||s||_infinity~S,
```

and determinant factors `|eta|~E`, `|theta|~T`.  After one of four row and
column permutations, at an absolute constant cost, assume

```text
|r2|~R,                 |s2|~S.                    (1.1)
```

The exact common-parameter color chart is

```text
x=X,
y=(s1*X-r2*eta)/s2,
zeta=(r1*X+s2*theta)/r2,
w=(r1*y+s1*theta)/r2.                              (1.2)
```

The integrality of `y` and `zeta` gives

```text
s1*X == r2*eta       (mod s2),
r1*X ==-s2*theta     (mod r2).                     (1.3)
```

Since `r` and `s` are primitive, each congruence separately selects one
residue class.  If they are compatible, their intersection is one residue
class modulo

```text
lcm(|r2|,|s2|).                                    (1.4)
```

The last integrality condition in (1.2), the coefficient support, and all
four product and prime-power masks only thin this set.

## 2. Prime powers replace the LCM by the product

Put

```text
d=gcd(|r2|,|s2|).                                  (2.1)
```

Reduce the first congruence in (1.3) modulo `d`.  Its right side vanishes.
Also `(s1,d)=1`, because `d|s2` and `(s1,s2)=1`.  Consequently

```text
d|X.                                               (2.2)
```

If `d>1` and `X` is an actual prime power, every prime divisor of `d` must
be the prime base of `X`.  Thus either no `X` exists, or every admissible
`X` is a power of one fixed prime.  Two distinct positive powers of one
prime have ratio at least two, whereas the shell has maximum strictly less
than twice its minimum.  Hence this case contributes at most one `X`.

If `d=1`, (1.4) is the modulus `|r2*s2|~R*S`, so an interval of length
`O(q)` contains

```text
O(1+q/(R*S))                                       (2.3)
```

values.  Equations (2.2)--(2.3) prove (0.1) uniformly.  Notice the precise
role of the actual mask: for unrestricted integers the best uniform bound
is only `q/max(R,S)`, because a large cross-GCD shortens the LCM.

## 3. Weighted flat-bin estimate

There are at most

```text
O(R^2*S^2*E*T)                                     (3.1)
```

tuples `(r,s,eta,theta)` in one dyadic block.  A color may admit several
relations, but this causes no problem: first assign one relation to each
color, then dominate the assigned sum by all tuples in (3.1).

Let the coefficient bin have `M` nonzero entries and squared mass `Z^2`.
Factor-two flatness gives

```text
|z_c|<<Z/sqrt(M),          w_z(C)<<Z^4/M^2.        (3.2)
```

Also `X=x` must belong to the support, so one chart has at most

```text
min(M,1+q/(R*S))                                  (3.3)
```

admissible values.  Multiplying (3.1)--(3.3) proves (0.2).

Write

```text
R=D^r, S=D^s, E=D^e, T=D^t, G=D^g, M=D^mu,
q=D^(33/16+o(1)),
p=max(e+2r,t+2s)-g,
kappa=max(0,p-17/16).                              (3.4)
```

After multiplying by the pointwise singleton cap `D^kappa`, (0.2) has
trace exponent

```text
C=kappa+2r+2s+e+t-2mu
  +min(mu,33/16-r-s).                              (3.5)
```

At the formerly critical primitive-content face

```text
(e,t,r,s,g,mu)=(1/2,1/2,7/16,7/16,0,15/8),
kappa=5/16,                                        (3.6)
```

the chart count, color mass, and completed trace exponents are respectively

```text
44/16+19/16=63/16,
63/16-60/16=3/16,
3/16+5/16=1/2.                                    (3.7)
```

In particular the uncompleted mass is much smaller than the high-tail
target `D^(11/16)`.  The implication `g=0` in (3.6) is also exact when the
transverse content is one: `gcd(eta,theta)` divides
`gcd(eta*alpha,theta*beta)`.

## 4. Exact principal envelope: `23/24`

The existing principal determinant estimate, after the singleton cap, is

```text
P=kappa+mu-17/16.                                  (4.1)
```

The feasible slice constraints give

```text
e+t<=1,       r+s<=1,       kappa<=5/16.           (4.2)
```

On the progression-limited branch of (3.5), use (4.2) to obtain

```text
C<=5/16+1+1+33/16-2mu=35/8-2mu,
P<=mu-3/4.                                         (4.3)
```

The two affine functions in (4.3) meet at

```text
mu=41/24,              C=P=23/24.                 (4.4)
```

On the support-limited branch, suppose for contradiction that `P>23/24`.
Then `mu>41/24`.  The branch condition gives

```text
r+s<=33/16-mu<17/48.                               (4.5)
```

Using (4.2) in the support-limited version of (3.5),

```text
C=kappa+2r+2s+e+t-mu
 <5/16+34/48+1-41/24=5/16<23/24.                  (4.6)
```

Thus `min(C,P)<=23/24` on both branches.  Equality is feasible, for example
at

```text
(e,t,r,s,g,mu)=(1/2,1/2,1/2,1/2,1/8,41/24),
p=11/8,                 kappa=5/16.                (4.7)
```

There (3.5) is progression-limited and (4.4) is exact.  The anchored and
diffuse bounds are larger, so they introduce no hidden equality condition.

## 5. First surviving loss: the mixed nonprincipal term

The two proved nonprincipal flat-bin estimates give, after the singleton
cap,

```text
N=kappa+min(1/2+mu/4,65/64-mu/4).                  (5.1)
```

Their minimum is maximized where the two branches meet:

```text
mu=33/32,
min(...)=97/128.                                   (5.2)
```

Since `kappa<=5/16=40/128`,

```text
N<=137/128.                                        (5.3)
```

This ledger maximum is compatible with all other block bounds.  One clean
face is

```text
(e,t,r,s,g,mu)=(1/2,1/2,7/16,7/16,0,33/32),
kappa=5/16.                                        (5.4)
```

At (5.4), the chart, anchored, and diffuse exponents are all strictly
larger than `137/128`, so (5.3) is the first exact loss left by this
argument.  Any further improvement of the parabolic singleton sector must
use high-fibre structure inside the nonprincipal character term, rather
than the principal common-`X` count.

```text
two common-X congruences:                           EXACT;
unrestricted chart length q/lcm:                   PROVED;
actual prime-power chart length 1+q/(R*S):          PROVED;
flat weighted chart estimate (0.2):                PROVED;
primitive critical principal face:                 CLOSED (trace D^(1/2));
uniform principal parabolic singleton:             D^(23/24+o(1));
uniform nonprincipal parabolic singleton:          D^(137/128+o(1));
complete parabolic singleton from these inputs:    D^(137/128+o(1));
uniform sharp four-cycle bound:                    NOT PROVED.
```

The rational exponent ledger is replayed in
`src/qp_prime_power_common_x_chart.py` and its test module.
