# QP singleton tail: common-`X` progression and the global reuse cutoff

**Date:** 2026-08-23  
**Verdict:** the relocated primitive parabolic face cannot support the
global full-integer countermodel required by the former principal
`D^(9/8)` obstruction.  Exact chart integrality limits every fixed relation
chart to `q/max(R,S)` colors over unrestricted integers.  On the actual
prime-power shell this sharpens to

```text
1+q/(R*S).                                           (0.1)
```

At support `M=D^(15/8)`, the resulting primitive-face trace is at most
`D^(15/16+o(1))` for unrestricted integers and `D^(1/2+o(1))` for actual
prime powers.  Thus the principal crossover is not a faithful obstruction
on this face.

This does **not** prove the sharp four-cycle theorem.  At the smaller
support `M=D^(33/32)`, the progression is longer than the support and the
existing nonprincipal estimates still give the exact residual

```text
D^(137/128+o(1)).                                  (0.2)
```

Broad nonparabolic one-point sectors are not silently included in the
parabolic chart conclusion.

## 1. Exact progression

Fix primitive directions `r=(r1,r2)`, `s=(s1,s2)` and determinant tokens
`eta,theta`.  With `X=x`, the exact color chart is

```text
y    =(s1*X-r2*eta)/s2,
zeta =(r1*X+s2*theta)/r2,
w    =(r1*y+s1*theta)/r2.                         (1.1)
```

Hence integral colors require

```text
s1*X == r2*eta  (mod s2),
r1*X ==-s2*theta (mod r2).                         (1.2)
```

Primitivity makes `s1` invertible modulo `s2` and `r1` invertible modulo
`r2`.  Thus `X` occupies one residue modulo

```text
lcm(|r2|,|s2|).                                   (1.3)
```

The shell colors are all comparable with `q`.  The token identities, for
example

```text
s1*x-s2*y=r2*eta,
r1*x-r2*zeta=-s2*theta,                            (1.4)
```

have error terms `o(qS)` and `o(qR)` throughout the feasible exponent
polytope.  Therefore, after the finite row/column orientations already
used in the chart decomposition,

```text
|r1|,|r2|~R,             |s1|,|s2|~S.             (1.5)
```

Equations (1.3)--(1.5) give the unrestricted bound

```text
#X in one chart <<1+q/max(R,S).                    (1.6)
```

## 2. Prime-power sharpening

Put `d=gcd(r2,s2)`.  Reducing the first equation in (1.4) modulo `d`
gives

```text
d | s1*X.
```

Since `d|s2` and `(s1,s2)=1`, one has `(s1,d)=1`, hence

```text
d|X.                                               (2.1)
```

If `d>1` and `X` is a prime power, every admissible `X` on the fixed chart
has the prime base dividing `d`.  The project shell has total ratio less
than two, so it contains at most one power of a fixed prime.  The chart
then contains at most one actual `X`.

If `d=1`, (1.3) is the product modulus `|r2*s2|~R*S`.  These two cases prove
(0.1).  Notice that this is an exact use of the actual-node mask; no prime
distribution theorem is involved.

In the coprime case, writing `X=X0+n*r2*s2` makes all four colors affine:

```text
Delta_n(x,y,zeta,w)
 =(r2*s2, s1*r2, r1*s2, r1*s1).                  (2.2)
```

This formula describes the residual obstruction below.

## 3. Flat-bin bound

Let a factor-two coefficient bin have support `M` and normalized squared
mass one.  Every color coefficient has size `O(M^(-1/2))`.  If `L_gamma`
is the number of actual `X` values on one chart, then direct counting and
the common-parameter Holder estimate give

```text
W_gamma <<min(M^(-1), L_gamma*M^(-2)).             (3.1)
```

The number of dyadic relation charts is

```text
<<R^2*S^2*E*T/G*q^o(1).                           (3.2)
```

If `D^j` bounds the occupied singleton lines, (0.1), (3.1), and (3.2)
give the exponent

```text
2r+2s+e+t-g+j-mu
 +min(0,33/16-r-s-mu).                            (3.3)
```

Over unrestricted integers, replace `r+s` in the last term by
`max(r,s)`.

## 4. The requested hostile face is globally impossible

Put `H=D^(1/16)`.  The relocated primitive face is

```text
q=H^33, E=T=H^8, R=S=H^7,
K=H^5, M=H^30, G=1.                               (4.1)
```

There are at most `H^44` relation charts.  An unrestricted chart contains
at most `H^26` colors, whereas an actual prime-power chart contains at most
`H^19`.  Consequently the total numbers of color matrices are at most

```text
unrestricted: H^70,
actual:       H^63.                                (4.2)
```

Saturating the principal obstruction would require

```text
M^3*D/q=H^73                                      (4.3)
```

matrices.  Thus even the unrestricted model misses the required reuse by
`H^3=D^(3/16)`.  Granting all `H^5` singleton completions to every retained
matrix and multiplying by the flat weight `M^(-2)=H^(-60)` gives

```text
unrestricted trace <=H^15=D^(15/16),
actual trace       <=H^8 =D^(1/2).                 (4.4)
```

This rules out the requested global countermodel without needing to decide
whether one isolated unrestricted-integer fiber can contain `H^5` points.

## 5. Exact residual after the principal face

The chart cutoff closes the principal contribution on every parabolic
singleton block, not only at (4.1).  The principal determinant mass has
exponent `mu-17/16`; since `j<=5/16`, its completed exponent is at most

```text
mu-3/4.                                            (5.1)
```

This is at most one for `mu<=7/4`.  Suppose `mu>7/4` and put
`v=r+s<=1`, `u=e+t<=1`.  If the cardinality term in (3.3) is active, then

```text
(3.3)
 <=v+u+j+33/16-2mu
 <=35/8-2mu<7/8.                                  (5.2)
```

If it is inactive, then `v<=33/16-mu`, and

```text
(3.3)
 <=2v+u+j-mu
 <=87/16-3mu<3/16.                                (5.3)
```

Thus the actual parabolic principal singleton term is `O(D^(1+o(1)))`
uniformly.

The nonprincipal determinant mass is bounded, uniformly in `mu`, by

```text
min(1/2+mu/4,65/64-mu/4)<=97/128.                 (5.4)
```

Adding `j<=5/16=40/128` proves the scoped parabolic-singleton bound

```text
D^(137/128+o(1)).                                  (5.5)
```

The exponent ledger in (5.5) is sharp for the presently combined routes.

The same primitive geometry survives at

```text
mu=33/32.                                         (5.6)
```

Now the actual chart length has exponent `19/16>33/32`, so (3.1) reverts
to `M^(-1)` and yields no saving.  The two proved nonprincipal masses meet:

```text
1/2+mu/4=65/64-mu/4=97/128.                       (5.7)
```

Adding the occupied-line exponent `5/16=40/128` gives (0.2).

On the coprime-component charts, (2.2) has step `D^(7/8)`.  A segment of
`M=D^(33/32)` parameters spans only

```text
D^(7/8+33/32)=D^(61/32)<q.                        (5.8)
```

Thus it fits inside the shell.  Requiring its four affine forms to be
prime is a four-linear-form sieve condition; it predicts logarithmic, not
power, thinning and supplies no unconditional lower bound here.  Globally,
saturating (0.2) requires only `D^(9/128)` color points per relation chart
on average.  No further exact shell/progression cutoff removes that power.

```text
common-X congruences:                              PROVED;
unrestricted q/max(R,S) chart length:              PROVED;
actual 1+q/(R*S) chart length:                     PROVED;
global hostile primitive-face countermodel:        IMPOSSIBLE BY COUNT;
principal D^(9/8) face on this chart:              REMOVED;
nonprincipal D^(137/128) residual:                 STILL OPEN;
sharp uniform four-cycle bound:                    NOT CLAIMED.
```

The exact algebra and exponent ledger are replayed in
`src/qp_parabolic_chart_progression_gate.py` and its test module.
