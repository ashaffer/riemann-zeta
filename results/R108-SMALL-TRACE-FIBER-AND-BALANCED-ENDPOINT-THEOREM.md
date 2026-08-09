# R108 small-trace fiber and balanced-endpoint theorem

Status: exact signed-box fiber improvement away from the balanced top-trace
sector.  Every nonparabolic trace fiber of height at most `H^2` has
`H^(1+o(1))` points, and every trace of height at most `H^(4-eta)` has a
fixed power saving over the previous `H^(2+o(1))` endpoint.  Equivalently,
all `H^(6-o(1))` collision obstructions are confined to two tuples whose
four coordinates are simultaneously of size `H^(1-o(1))` and whose common
trace is `H^(4-o(1))`.  The remaining balanced top sector is not bounded by
a fixed power here.

Date: 2026-08-07.

## 1. Statement

For `a=1`, put

```text
Tr(h_1,h_2,h_3,h_4)
 =h_1h_2h_3h_4-(h_1+h_3)(h_2+h_4)+2,                 (1.1)

r_T(H)=#{h in Z^4: abs(h_i)<=H, Tr(h)=T}.             (1.2)
```

The parabolic levels `T=plusminus2` are excluded below.  This is necessary
for the two divisor factorizations used in the proof: their right sides can
vanish precisely at those levels.

**Theorem 1.1 (height-sensitive nonparabolic fiber bound).**  Uniformly for
integral `T!=plusminus2`,

```text
r_T(H)
 <<_epsilon H^epsilon [
      H+min(H^2,(abs(T-2)+4H^2)^(1/2))].             (1.3)
```

In particular,

```text
abs(T)<=H^2       implies       r_T(H)<<H^(1+epsilon),       (1.4)

abs(T)<=H^(4-eta) implies       r_T(H)<<H^(2-eta/2+epsilon)
                               (0<eta<=2).                    (1.5)
```

The estimate is for the full signed box.  It does not require positivity or
opposite-pair primitivity.

There is also a useful sector form.  For a tuple with no zero coordinate,
let

```text
mu(h)=the product of the two smallest numbers among abs(h_1),...,abs(h_4).
                                                                    (1.6)
```

Let `r_(T,unbal)(H;kappa)` count the tuples in (1.2) with
`mu(h)<=H^(2-kappa)`, including the zero-coordinate tuples by convention.
Then, for every fixed `0<kappa<=1`,

```text
sup_(T!=plusminus2) r_(T,unbal)(H;kappa)
 <<_epsilon H^(2-kappa+epsilon).                     (1.7)
```

Consequently, if

```text
N_8(H)=sum_T r_T(H)^2,                                (1.8)
```

then all ordered nonparabolic collisions in which at least one tuple is in
the unbalanced sector contribute

```text
<<_epsilon H^(6-kappa+epsilon).                       (1.9)
```

For any fixed `0<kappa<=1`, the only sector in which the old
`H^(6+o(1))` endpoint can remain has, in both copies,

```text
mu(h)>H^(2-kappa),
abs(h_i)>H^(1-kappa) for every i,
abs(Tr(h))>=H^(4-2kappa)-4H^2-2.                     (1.10)
```

As `kappa` tends to zero, this is exactly the balanced top-trace sector.
The theorem therefore supplies a genuine power away from that sector, but
does not by itself prove `N_8(H)<<H^(6-delta)`.

## 2. The two fixed-pair factorizations

There are six possible pairs of coordinate positions.  By cyclic and
reflection symmetry they reduce to an adjacent pair and an opposite pair.

### 2.1 Adjacent pair

Fix `h_1,h_2` and put

```text
p=h_1h_2-1.
```

The exact adjacent-continuant identity is

```text
(p h_3-h_1)(p h_4-h_2)=p^2+pT+1.                    (2.1)
```

If `p!=0` and `T!=plusminus2`, the right side of (2.1) is nonzero.  Indeed,
if it vanished, then

```text
T^2-4=(2p+T)^2
```

would be an integer square.  The factorization

```text
(T-y)(T+y)=4
```

then forces `T=plusminus2`.  Thus the number of ordered factor pairs on the
right of (2.1) is `H^epsilon`, and each factor pair determines `h_3,h_4`.

The case `p=0` means `h_1h_2=1`, hence

```text
(h_1,h_2)=(1,1) or (-1,-1).                           (2.2)
```

For the first pair, `T=1-h_3-h_4`; for the second,
`T=1+h_3+h_4`.  Each fixed level therefore has only `O(H)` completions.
There are only two such fixed pairs for each adjacent position.

### 2.2 Opposite pair

Fix `h_1,h_3` and write

```text
u=h_1h_3,          x=h_1+h_3.
```

Then

```text
(u h_2-x)(u h_4-x)
 =x^2+u(T-2)
 =h_1^2+T h_1h_3+h_3^2.                              (2.3)
```

When `h_1h_3!=0` and `T!=plusminus2`, the right side is nonzero.  Otherwise
`h_1/h_3` would be a rational root of

```text
z^2+Tz+1=0,
```

so `T^2-4` would be a rational, hence integral, square; again this forces
`T=plusminus2`.  Divisor counting in (2.3) therefore gives `H^epsilon`
completions of every fixed nonzero opposite pair.

All integers appearing on the right sides of (2.1) and (2.3) have
polynomial height in `H` whenever the fiber is nonempty.  The usual divisor
bound is consequently uniform in the form used above.

## 3. Zero-coordinate and exceptional strata

Suppose, for example, that `h_1=0`.  Equation (1.1) becomes

```text
2-T=h_3(h_2+h_4).                                    (3.1)
```

For `T!=2`, there are `H^epsilon` possible nonzero divisors `h_3` and
`O(H)` pairs with the prescribed sum `h_2+h_4`.  Hence this axis contributes
`H^(1+epsilon)` to a fixed fiber.  Cyclic symmetry gives the same estimate
for all four axes, including their intersections.  These are exactly the
zero cases omitted when (2.3) was divided by `u`.

Together with (2.2), all failures of the `H^epsilon` fixed-pair completion
bound contribute only

```text
O_epsilon(H^(1+epsilon))                              (3.2)
```

to a nonparabolic fixed fiber.

## 4. Proof of Theorem 1.1

For every tuple in the `T` fiber,

```text
abs(h_1h_2h_3h_4)
 <=abs(T-2)+abs(h_1+h_3)abs(h_2+h_4)
 <=abs(T-2)+4H^2=:Y.                                 (4.1)
```

Discard the zero-coordinate tuples, already handled in Section 3, and
order the four positive magnitudes as

```text
b_1<=b_2<=b_3<=b_4.
```

Then

```text
(b_1b_2)^2<=b_1b_2b_3b_4<=Y,                         (4.2)
```

so the product of the two smallest coordinates is at most `Y^(1/2)`.
There are six choices for their coordinate positions.  For any one choice,
the number of signed nonzero pairs `(v,w)` with

```text
abs(v),abs(w)<=H,
abs(vw)<=Z:=min(H^2,Y^(1/2))                          (4.3)
```

is

```text
<<H+Z log(2H).                                        (4.4)
```

This follows by summing `min(H,Z/n)` over `1<=n<=H` and restoring signs.

For each fixed pair in (4.4), Section 2 gives `H^epsilon` completions,
apart from the `O(H^(1+epsilon))` total exception in Section 3 and (2.2).
Multiplying (4.4) by the harmless divisor factor proves (1.3).  Statements
(1.4) and (1.5) follow immediately.

For (1.7), repeat the same count with `Z=H^(2-kappa)` instead of deriving
`Z` from (4.1).  R100's nonparabolic endpoint gives

```text
sup_(T!=plusminus2) r_T(H)<<H^(2+epsilon).             (4.5)
```

Therefore the number of ordered collisions with the first tuple unbalanced
is at most

```text
sup_T r_(T,unbal)(H;kappa) sum_T r_T(H)
 <<H^(2-kappa+epsilon) H^4.                           (4.6)
```

The same argument with the two copies exchanged proves (1.9).

Finally, if `b_1b_2>H^(2-kappa)`, then `b_1>H^(1-kappa)` because
`b_2<=H`.  Also `b_3b_4>=b_1b_2`, so

```text
abs(h_1h_2h_3h_4)>H^(4-2kappa).                      (4.7)
```

Combining (4.7) with (1.1) gives (1.10).

## 5. Primitive affine-line form and the remaining gate

The same calculation exposes the arithmetic still missing in the balanced
sector.  Let

```text
(r,s)=1,       u=rs,       x=r+s,
U=um-x,        B=2-xm.                                (5.1)
```

Then the trace is the affine line

```text
T=Un+B,                                                (5.2)
```

and, since `(u,x)=1`,

```text
U divides T-2+xm.                                     (5.3)
```

The `-2` in (5.3) is essential.  Equivalently,

```text
(um-x)(un-x)=x^2+(T-2)u.                              (5.4)
```

Away from `xm=0`, the map `(r,s,m)->(U,B)` has
`H^epsilon` multiplicity: first `m` divides `2-B`, then

```text
x=(2-B)/m,       u=(U+x)/m,                           (5.5)
```

and `r,s` are the two roots of `z^2-xz+u`.  Thus the primitive bulk is an
almost-simple family of about `H^3` distinct affine lines, with slopes of
height `H^3` but intercepts of height only `H^2`.

In the balanced top sector, (5.3) is a moving large-modulus divisor
condition.  Equivalently, writing `q=r+s`, the primitive fixed-trace problem
contains the quadratic-residue congruence

```text
L r^2 congruent -C (mod q),
C=T-2,                                                 (5.6)
```

where `L` is simultaneously forced into a short interval centered at
`C/[r(q-r)]`.  The general trilinear theorem in R107 and ordinary divisor
bounds both lose the `+1` for each `(r,s)` at exactly this point.  A power
estimate for this short moving quadratic-residue problem, or an equivalent
coefficient-sensitive affine-line incidence theorem, is still required to
finish the full collision bound.

## 6. Verdict

The previous `H^(2+o(1))` fixed-fiber endpoint is not a real obstruction on
small or moderately large trace levels.  It survives only where all four
variables and the trace are simultaneously at their natural maximum scale.
This is a strict narrowing of the R100/R107 gate:

```text
small trace abs(T)<=H^2:             H^(1+epsilon) fiber PROVED;
sub-top trace abs(T)<=H^(4-eta):     fixed power PROVED;
one unbalanced tuple in a collision: fixed power PROVED;
balanced top trace in both copies:   OPEN.             (6.1)
```

No fixed zeta zero-free strip, and no theorem excluding such a strip, is
proved by this report alone.
