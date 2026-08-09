# R109 primitive cyclic-congruence bound

Status: a uniform fixed-power bound is proved for the primitive necessary
congruence below the cubic threshold, and a size-sensitive fixed-power
bound is proved for the full two-pair trace fiber below the quartic
threshold.  The zero-quotient and zero-factor ruled strata are classified
exactly.  The balanced quartic range remains open.  No fixed zero-free
strip, and no theorem excluding all fixed strips, is proved here.

Date: 2026-08-07.

Predecessors:

* [`R100-VARYING-PRIME-DISCRIMINANT-PARITY-GATE.md`](R100-VARYING-PRIME-DISCRIMINANT-PARITY-GATE.md)
  for the four-shift trace and its fixed-trace factorization; and
* [`R106-ROUGH-EULER-DILATION-SIEVE-GATE.md`](R106-ROUGH-EULER-DILATION-SIEVE-GATE.md)
  for the preceding coefficient filter gate.

## 1. Verdict

For `H>=2` and `C!=0`, define

```text
N_C(H)=# { (r,s,M) in (Z\{0})^2 x Z :
            |r|,|s|<=H, |M|<=2H, gcd(r,s)=1,
            rs divides (r+s)M+C }.                    (1.1)
```

The primitive condition gives

```text
gcd(r+s,rs)=1,                                        (1.2)
```

so (1.1) fixes one residue class of `M modulo |rs|`.  This
already gives the uniform critical estimate `N_C(H)<<H^(2+epsilon)`.  The
new point is that the large-product portion can instead be counted through
an exact divisor factorization.

**Theorem 1.1 (primitive cyclic-congruence bound).**  Fix `A>0`.  Uniformly
for `0<|C|<=H^A`, every `epsilon>0`, and every real `1<=P<=H^2`,

```text
N_C(H)
 <<_(A,epsilon) H^epsilon
    { H + P + H(H^2+|C|)/P }.                         (1.3)
```

Together with the direct critical estimate, this gives

```text
N_C(H)
 <<_(A,epsilon) H^epsilon min {
      H^2,
      H+[H(H^2+|C|)]^(1/2)
    },                                                (1.4)
```

whenever `H^2+|C|<=H^3`.  In particular,

```text
|C|<=H^2             => N_C(H)<<H^(3/2+epsilon),      (1.5)

|C|<=H^(3-eta)       => N_C(H)
                         <<H^(2-min(eta/2,1/2)+epsilon).
                                                               (1.6)
```

Thus the necessary congruence has a genuine fixed-power estimate throughout
every range lying a fixed power below `|C|=H^3`.  This theorem does
**not** reach the natural balanced trace range `|C|asymp H^4`.

There are two important reality checks.

1. The bound cannot reasonably be strengthened to a uniform polylogarithmic
   count.  The small-product sector alone gives `N_C(H)>>H(log H)^2`.
   Signed zero-quotient anti-diagonals can be larger by a subpower factor.
2. Those largest ruled families are artifacts of dropping the second
   primitive pair.  In the full trace equation the quotient and sum are
   constrained by `Q=v mn` and `M=m+n`; the zero-quotient family disappears,
   and the zero-factor lines collapse to finitely many tiny cases.

The remaining target is consequently precise: retain the second square
discriminant in the balanced quartic range, rather than try to prove an
unnecessarily strong estimate for (1.1) alone.

## 2. Small products

For a primitive pair `(r,s)`, (1.2) follows from

```text
gcd(r+s,r)=gcd(s,r)=1,
gcd(r+s,s)=gcd(r,s)=1.                                (2.1)
```

Consequently the congruence

```text
(r+s)M == -C (mod |rs|)                              (2.2)
```

has exactly one residue class modulo `|rs|`.  In the interval `|M|<=2H`
it has at most

```text
1+4H/|rs|                                             (2.3)
```

solutions.  The elementary hyperbola estimates

```text
# { (r,s): 1<=|r|,|s|<=H, |rs|<=P }
   << P log(2H),

sum_(1<=|r|,|s|<=H, |rs|<=P) 1/|rs|
   << (log(2H))^2                                    (2.4)
```

therefore give

```text
N_C(H; |rs|<=P)
 << P log(2H)+H(log(2H))^2.                           (2.5)
```

Primitivity only reduces the sums in (2.4).

Taking `P=H^2` in the same argument proves the direct uniform bound

```text
N_C(H)<<H^2+H(log H)^2.                               (2.6)
```

## 3. Large products and the exact factorization

On a solution of (1.1), put

```text
Q=((r+s)M+C)/(rs).                                    (3.1)
```

If `|rs|>P`, then

```text
|Q| <= (4H^2+|C|)/P.                                 (3.2)
```

The defining equation has the exact factorization

```text
(Qr-M)(Qs-M)=M^2+QC.                                  (3.3)
```

Suppose first that

```text
Q!=0,             M^2+QC!=0.                         (3.4)
```

For fixed `(Q,M)`, every solution gives an ordered signed factorization
`xy=M^2+QC` by

```text
x=Qr-M,           y=Qs-M.                            (3.5)
```

Conversely `x,y,Q,M` determine

```text
r=(x+M)/Q,        s=(y+M)/Q,                          (3.6)
```

so (3.5) is injective on the solutions.  Hence there are at most
`2 tau(|M^2+QC|)` pairs `(r,s)` for fixed `(Q,M)`.

Under `|C|<=H^A`, (3.2) makes every nonzero integer in (3.3) of size
`H^O_A(1)`.  The standard divisor bound therefore gives, uniformly in the
present range,

```text
tau(|M^2+QC|)<<_(A,epsilon)H^epsilon.                 (3.7)
```

There are `O(H)` choices for `M` and
`O(1+(H^2+|C|)/P)` choices for nonzero `Q`.  Thus the nonsingular
large-product sector contributes

```text
<<_(A,epsilon)
 H^(1+epsilon){1+(H^2+|C|)/P}.                        (3.8)
```

## 4. Complete singular-stratum classification

The factorization argument needs two singular cases separated before
division or divisor counting.

### 4.1. Zero quotient

If `Q=0`, then

```text
(r+s)M=-C.                                            (4.1)
```

Because `C!=0`, one has `M!=0`, `M|C`, and

```text
r+s=-C/M.                                             (4.2)
```

For each signed divisor `M` of `C`, (4.2) is one anti-diagonal and contains
`O(H)` points in the box.  Therefore

```text
# {Q=0 solutions} << H tau(|C|)<<_(A,epsilon)H^(1+epsilon).
                                                               (4.3)
```

### 4.2. Zero factor product

Let `Q!=0` and `M^2+QC=0`.  Equation (3.3) says either `Qr=M` or
`Qs=M`.  In the first case, writing `a=r`,

```text
M=Qa,             C=-Qa^2,                            (4.4)
```

and the original equation holds for every `s`; the second case is the
horizontal analogue.  Conversely (4.4) gives exactly such a ruled line.

The parameter `a` must have `a^2|C`, after which `Q=-C/a^2` and `M=Qa`
are fixed.  There are `O(tau(|C|))` signed parameter choices and `O(H)`
points on each line.  Hence

```text
# {Q!=0, M^2+QC=0 solutions}
 <<H tau(|C|)<<_(A,epsilon)H^(1+epsilon).              (4.5)
```

Equations (4.1) and (4.4) are all singular strata: outside them `Q` and the
right side of (3.3) are both nonzero, and (3.5)--(3.6) apply.

Combining (2.5), (3.8), (4.3), and (4.5), and absorbing logarithms in
`H^epsilon`, proves (1.3).

## 5. Optimization

Put

```text
A_0=H^2+|C|.                                          (5.1)
```

The two variable terms in (1.3) balance at

```text
P=[H A_0]^(1/2).                                      (5.2)
```

This is an admissible choice `P<=H^2` precisely when `A_0<=H^3`.
Substitution gives

```text
N_C(H)<<_(A,epsilon)
 H^epsilon{H+[H(H^2+|C|)]^(1/2)},                    (5.3)
```

which is (1.4) in that range.  If `|C|<=H^2`, (5.3) is
`H^(3/2+epsilon)`.  If `|C|<=H^(3-eta)`, it is

```text
H^(max(3/2,2-eta/2)+epsilon)
 =H^(2-min(1/2,eta/2)+epsilon),                       (5.4)
```

as asserted.

For `|C|asymp H^4`, (5.2) lies beyond the available product range and the
optimization returns only the direct `H^(2+epsilon)` scale.  This is the
balanced quartic obstruction, not a loss hidden in the singular cases.

## 6. Sharp lower-scale reality checks

For positive coprime `r,s<=sqrt(H)`, one has `rs<=H`.  Every residue class
modulo `rs` occurs `gg H/(rs)` times in `|M|<=2H`.  Consequently

```text
N_C(H)
 >= c H sum_(r,s<=sqrt(H), gcd(r,s)=1)1/(rs)
 >> H(log H)^2.                                       (6.1)
```

This holds for every `C` and shows that the `H` scale naturally carries
logarithmic multiplicity.

There are larger signed ruled examples.  If `d|C`, choose

```text
M=-C/d,            r+s=d.                             (6.2)
```

Then `Q=0`.  Taking a squarefree primorial `C<=H/2` and summing the primitive
points over `d|C` yields

```text
N_C(H)
 >= H exp{(log 2+o(1))log H/log log H}.               (6.3)
```

Thus no bound `H(log H)^B` with fixed `B` is uniform in `C`.  This is still
`H^(1+o(1))`, so it does not obstruct a fixed-power improvement over `H^2`.

The exclusion `C!=0` is essential.  For `C=0`, the plane `M=0` contains
every primitive pair and gives

```text
N_0(H) asymp H^2.                                     (6.4)
```

## 7. Inverse-square CRT coordinate

There is a sharper exact coordinate for the balanced range.  Put

```text
q=r+s,             p=rs,                              (7.1)
```

and suppose `q!=0`.  Choose integers `x,y` with

```text
xr+ys=1,           d=x-y,
U=x^2r+y^2s.                                          (7.2)
```

Direct expansion gives

```text
qU=1+p d^2,                                           (7.3)
```

because the difference between the two sides after removing
`(xr+ys)^2=1` is `rs(x-y)^2`.  Also

```text
dr==1 (mod |q|).                                      (7.4)
```

All integer solutions of

```text
qM+C=Qp                                               (7.5)
```

are therefore

```text
M=-CU+t p,
Q=-C d^2+t q,            t in Z.                     (7.6)
```

In particular,

```text
Q==-C d^2 (mod |q|),      dr==1 (mod |q|),            (7.7)
```

or equivalently

```text
Q r^2==-C (mod |q|).                                  (7.8)
```

Thus the remaining balanced problem is an incomplete inverse-square, or
quadratic-Kloosterman, incidence problem.  Formula (7.7) is stronger than a
generic inverse residue, but by itself it does not control quartic `C`: the
admissible quotient interval can then traverse many complete periods.

## 8. Why the full trace equation is stronger

In the primitive full off-axis trace sector one has

```text
v r s m n-(r+s)(m+n)=C,       v>=1,                  (8.1)
```

with both primitive pairs and all four variables nonzero.  Set

```text
M=m+n,             Q=v mn.                            (8.2)
```

Then `(r,s,M)` is counted by (1.1), but it also satisfies

```text
M^2-4Q/v=(m-n)^2.                                     (8.3)
```

The second square discriminant (8.3) was completely discarded in
`N_C(H)`.

It also kills the large ruled strata from Section 4.

* Since `m,n` are nonzero, `Q=v mn!=0`; the anti-diagonals (4.1) do not
  lift.
* On a vertical line (4.4), the lift would require

  ```text
  m+n=v a m n.                                        (8.4)
  ```

  But then

  ```text
  (v a m-1)(v a n-1)=1.                               (8.5)
  ```

  For nonzero integer variables this forces `vam=van=2`, leaving only
  bounded tiny cases.  The horizontal lines behave identically.

Equivalently, with

```text
S=r+s, P=rs, M=m+n, N=mn,                             (8.6)
```

the full problem is the determinant equation

```text
vPN-SM=C                                               (8.7)
```

subject to the two simultaneous square conditions

```text
S^2-4P=(r-s)^2,       M^2-4N=(m-n)^2.                 (8.8)
```

For fixed `(P,S)`, the second condition is the factorable conic

```text
(vPM-2S)^2-(vP(m-n))^2=4(S^2+vPC).                   (8.9)
```

The quartic task is now isolated without its false ruled obstructions:
prove a fixed-power count for (8.7)--(8.8), using the inverse-square
coordinate (7.7), a double square sieve, or a genuinely stronger
average-conic estimate.  The next theorem makes the last sentence precise.

## 9. Size-sensitive full-fiber theorem

Define the full primitive off-axis fiber

```text
F_(C,v)(H)=# { (r,s,m,n) in (Z\{0})^4:
                |r|,|s|,|m|,|n|<=H,
                gcd(r,s)=gcd(m,n)=1,
                v r s m n-(r+s)(m+n)=C }.            (9.1)
```

The following argument does not need primitivity, but retaining it records
the exact application.

**Theorem 9.1 (subquartic full-fiber bound).**  Fix `A>0`.  Suppose
`1<=v<=H^A`, `|C|<=H^A`, and

```text
vC not in {0,-4}.                                     (9.2)
```

Then, for every `epsilon>0`,

```text
F_(C,v)(H)
 <<_(A,epsilon) H^epsilon
    {1+[(|C|+H^2)/v]^(1/2)}.                          (9.3)
```

In particular, for every fixed `eta>0`,

```text
|C|<=v H^(4-eta)
    => F_(C,v)(H)
       <<_(A,epsilon)H^(2-eta/2+epsilon)+H^(1+epsilon).
                                                               (9.4)
```

Thus every range lying a fixed power below the natural quartic height has
a fixed-power fiber saving.  Only `|C|=vH^(4-o(1))` remains critical.

### Proof

Place the four absolute values in dyadic intervals

```text
|r|asymp R, |s|asymp S, |m|asymp M, |n|asymp N.      (9.5)
```

There are only `O((log H)^4)` such boxes.  On every solution,

```text
v|rsmn|
 <=|C|+|(r+s)(m+n)|
 <=|C|+4H^2.                                          (9.6)
```

It follows that

```text
RSMN << (|C|+H^2)/v,                                  (9.7)
```

and hence

```text
min(RS,MN)
 <=(RSMN)^(1/2)
 <<[(|C|+H^2)/v]^(1/2).                               (9.8)
```

Suppose first that `RS<=MN`, and fix `(r,s)`.  Put `P=rs` and `S_0=r+s`.
The full equation has the exact factorization

```text
(vP m-S_0)(vP n-S_0)=S_0^2+vPC.                      (9.9)
```

The right side cannot vanish under (9.2).  Indeed, if it vanished then the
rational number `r/s` would be a root of

```text
X^2+(2+vC)X+1.                                       (9.10)
```

Its discriminant `vC(vC+4)` would be an integer square.  The elementary
identity

```text
(vC+2-y)(vC+2+y)=4                                   (9.11)
```

shows that `y^2=vC(vC+4)` is possible only for `vC=0` or `vC=-4`:
the two factors in (9.11) have the same parity, and the only same-parity
signed factor pairs of `4` are `(2,2)` and `(-2,-2)`.

Consequently (9.9) has `H^epsilon` signed factor pairs, uniformly under the
polynomial-height hypotheses.  Each factor pair determines `(m,n)` because
`vP!=0`.  There are `O(RS)` choices of `(r,s)` in the dyadic box, so this
box contributes

```text
<<_(A,epsilon)(RS)H^epsilon.                          (9.12)
```

If `MN<RS`, fix `(m,n)` and use the symmetric factorization instead.  The
box contribution is then `<<(MN)H^epsilon`.  In either case (9.8) gives
the right side of (9.3).  Summing the dyadic boxes and absorbing their
logarithmic number into `H^epsilon` proves the theorem.  QED.

For the original unscaled trace, `v=1` and `C=T-2`; condition (9.2) is
exactly the nonparabolic restriction `T!=plusminus2`.  The theorem therefore
upgrades the old coefficient-uniform `H^(2+o(1))` fiber bound everywhere
except the genuinely balanced quartic shell.
