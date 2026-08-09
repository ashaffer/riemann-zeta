# R95 audit of Puglisi's claimed `quasi-RH => RH` theorem

Status: the claimed theorem in arXiv:2210.03121v9 is **not proved**.
The decisive error is an explicitly false alternating-exponential estimate
(Lemma 1), used in the only step that turns the analytic estimates into a
contradiction.  The estimate fails not merely for an irrelevant choice of
parameters, but eventually throughout the exact range forced by the final
choice `J=2 floor(z0 log U+2)`.  Consequently equation (45), and hence the
last contradiction, do not follow.

Date: 2026-08-07.

Primary source: [G. Puglisi, *On the complex zeros of the Riemann
Zeta-function*, arXiv:2210.03121v9 (2024)](https://arxiv.org/abs/2210.03121).
This audit uses the v9 TeX source and PDF dated 22 April 2024.

## 1. Verdict

The paper assumes the quasi-Riemann hypothesis

```text
B=sup_rho Re(rho)<1                                           (1.1)
```

and claims to deduce RH.  Much of the proof constructs an entire function

```text
F_V(s)=zeta(s) M_V(s+s_V-1),
M_V(s)=sum_(n<=V) mu(n)n^(-s),                                (1.2)
```

followed by a symmetrized Taylor detector `G_UV`.  The final analytic lemma
is intended to say that a high Taylor polynomial of `G_UV` is modeled by a
truncated exponential.  If all preceding estimates are granted, equation
(44) is

```text
-1+o(1)
 = sum_(j=1)^(J-1) (-x)^j/j! + q x^J/J! + o(1),               (1.3)

x=z0 log U,
q=U^(z0-z1),               exp(-x)<q<1,
J=2 floor(x+2).                                               (1.4)
```

The paper invokes Lemma 1 to assert that the main expression on the right
of (1.3) is negative with exponentially growing magnitude.  That assertion
is false.  In fact, the specific Lemma 1 inequality used there is eventually
reversed throughout the interval in (1.4).

Thus this paper cannot be imported as either

```text
fixed zero-free strip  => RH,
```

or as a proof of a fixed zero-free strip.  It assumes the latter and its
purported self-improvement to RH breaks at the final sign estimate.

## 2. The exact false statement

The paper defines

```text
p_j(u)=exp(-u)u^j/j!.                                        (2.1)
```

Lemma 1 states that, for every even `J>=2` and every `u<=0`,

```text
sum_(j=1)^(J-1) p_j(u) <= (1/2)p_(J-1)(u).                   (2.2)
```

Put `u=-x`, with `x>0`.  Since `J-1` is odd, division by the
positive factor `exp(x)` makes (2.2) equivalent to

```text
sum_(j=1)^(J-1) (-x)^j/j! + (1/2)x^(J-1)/(J-1)! <= 0.        (2.3)
```

This inequality is false.

### Proposition 2.1: an exact counterexample in the final parameter range

Take

```text
x=13,                u=-13,
J=30=2 floor(x+2).                                            (2.4)
```

Then the left side of (2.3) is strictly positive.

### Proof

Let

```text
R=sum_(j=30)^infinity (-13)^j/j!.                             (2.5)
```

The terms in (2.5) decrease in magnitude and the first term is positive,
so the alternating-series estimate gives

```text
0<R<13^30/30!.                                                (2.6)
```

Using the exponential series,

```text
D := sum_(j=1)^29 (-13)^j/j! + (1/2)13^29/29!
   = exp(-13)-1-R+(1/2)13^29/29!
   > exp(-13)-1+(1/2-13/30)13^29/29!
   = exp(-13)-1+(1/15)13^29/29!.                             (2.7)
```

The last quantity is positive because the exact integer inequality

```text
13^29 = 201538126434611150798503956371773
      > 132626429906095529318154240000000
      = 15 * 29!                                             (2.8)
```

holds.  Hence `D>exp(-13)>0`, contradicting (2.3).  Equivalently,

```text
sum_(j=1)^29 p_j(-13) > (1/2)p_29(-13).                       (2.9)
```

This is exactly compatible with every numerical restriction attached to
the final use: taking `U=exp(13/z0)` gives

```text
U>=exp(10/z0),          J=2 floor(z0 log U+2)=30.             (2.10)
```

So the counterexample is not outside the proof's parameter regime.

## 3. The failure is asymptotic and uniform in the chosen cutoff cell

The preceding example is only the first convenient exact witness.  The
problem becomes worse as `J` grows.

Let

```text
J=2m,
m-2 <= x < m-1.                                              (3.1)
```

Condition (3.1) is precisely equivalent to

```text
J=2 floor(x+2).                                               (3.2)
```

Write

```text
a_j=x^j/j!,
R_J=a_J-a_(J+1)+a_(J+2)-... .                                (3.3)
```

Since `x/J<1/2`, the tail is alternating with decreasing terms, and

```text
0<R_J<a_J.                                                    (3.4)
```

The defect in the asserted Lemma 1 inequality, after division by
`exp(x)`, is therefore

```text
D_J(x)
 =sum_(j=1)^(J-1)(-x)^j/j! +(1/2)a_(J-1)
 =exp(-x)-1-R_J+(1/2)a_(J-1)
 >exp(-x)-1+(1/2-x/J)a_(J-1).                                (3.5)
```

Throughout (3.1),

```text
1/2-x/J > 1/(2m),
a_(J-1) >= A_m := (m-2)^(2m-1)/(2m-1)!.                     (3.6)
```

Consequently

```text
D_J(x)>-1+A_m/(2m).                                          (3.7)
```

Stirling's formula gives

```text
log A_m=2m(1-log 2)+O(log m),                                (3.8)
```

and `1-log 2>0`.  Hence `A_m/(2m)` tends to infinity
exponentially.  It follows that

```text
D_J(x)>0                                                     (3.9)
```

for every `x` in the entire interval (3.1), once `m` is large.
Thus the inequality used by the paper is eventually reversed for every
large `V` under its own rule for `J`, not just along an exceptional
subsequence.

The proof printed under Lemma 1 exposes the mistake.  Its induction step
reduces to

```text
u^2+2(J+1)u+J(J+1)>=0.                                      (3.10)
```

This quadratic is negative when

```text
-(J+1)-sqrt(J+1) < u < -(J+1)+sqrt(J+1).                    (3.11)
```

The hypothesis `u<=0` does not exclude (3.11).  The subsequent observation
in the paper involving `J/2` supplies no missing restriction and cannot
validate the induction.

## 4. Exactly where the theorem proof breaks

With `x=z0 log U`, equation (44) is (1.3).  Equation (45) begins with

```text
sum_(j=1)^(J-1)(-x)^j/j! + q x^J/J!
 <= -(x^(J-1)/(J-1)!)(1/2-x/J),                              (4.1)
```

where only `q<=1` is known.  The derivation of (4.1) is exactly:

1. apply false inequality (2.2) to the truncated sum;
2. replace `q` by its upper bound `1`.

Therefore (4.1) has no proof.  It is concretely false.  For example, with
`x=13`, `J=30`, and `q=1`,

```text
sum_(j=1)^29(-13)^j/j! + 13^30/30!  > 0,                    (4.2)
```

whereas the right side of (4.1) is negative.  The final Taylor point only
implies `q<1`; it gives no quantitative separation of `q` from `1`, so
values arbitrarily close to this counterexample are not excluded.

One need not use the excluded endpoint `q=1`.  Take the admissible value
`q=9/10`.  The three-term alternating-tail bound

```text
R<a_30-a_31+a_32
```

gives

```text
sum_(j=1)^29(-13)^j/j! +(9/10)13^30/30!
 > -1-(1/10)a_30+a_31-a_32
 = 3671731337212080916480103242980019
   /7784936003955429886604083200000000
 >0.                                                           (4.3)
```

This `q` corresponds to

```text
z1-z0=(z0/13)log(10/9),
```

which lies strictly between `0` and `z0`, exactly as the Taylor remainder
allows.  No estimate in the paper rules out this part of the allowed range.

The correct identity is

```text
sum_(j=1)^(J-1)(-x)^j/j!=exp(-x)-1-R_J,                     (4.4)
```

with the alternating-tail bounds in (3.4).  When `J=2x+O(1)`,
the last factorial terms grow exponentially, and `R_J` is only a fraction
of `a_J`.  A possible positive `q a_J` can therefore overwhelm the negative
tail.  This is precisely the contribution that (2.2) incorrectly removes.

There is also a structural incompatibility behind the bad inequality.  If
one writes `J~c x`, Stirling gives

```text
x^J/J! roughly (e/c)^(cx)/sqrt(J).                           (4.5)
```

To make this Taylor tail uniformly small one needs `c>e`.  The paper's
factorial contradiction needs the same quantity to grow, which requires
`c<e`.  Taking `c=2` lies in the growing-tail regime and cannot at the same
time justify replacing the partial exponential by its limiting value.
Changing a harmless rounding constant in `J` does not bridge this gap.

## 5. Audit of the Perron and Cauchy stages

The false Lemma 1 already decisively kills the theorem.  For completeness,
the principal analytic stages were checked independently enough to locate
which issues are substantive and which look repairable.

### 5.1 Lemmas 2 and 3

Conditional on the standard Littlewood-type consequence of (1.1), namely

```text
1/zeta(s) <<_delta (1+|t|)^epsilon
```

on a half-plane a fixed distance to the right of `B`, the Perron contour in
Lemma 2 remains to the right of every zeta zero.  Its only relevant crossed
pole is the `1/z` pole, producing `1/zeta(s)`.  The local Rouche argument
near `s=1` is then coherent.

Lemma 3 says that its estimate also holds near `s=1` merely because
`F_V(s)-1` is holomorphic.  Holomorphy alone is not a quantitative estimate,
but here the statement can be supplied by the maximum-modulus principle:
the condition `r>=100 epsilon` makes `sigma+r>1` throughout the small disk,
so the same boundary exponent applies.  This is an omitted argument, not
the decisive obstruction.

### 5.2 A malformed contour in Lemma 4

In the second Perron deformation in Lemma 4, define

```text
L =1-s_V+Re(omega-z)-2r+3epsilon,
L'=1-s_V+Re(omega-z)-r.                                     (5.1)
```

As printed, the third integral runs from

```text
L-iT_1  to  L'+iT_1,                                        (5.2)
```

while the upper horizontal segment begins at `L+iT_1`.  These paths do not
form the boundary of a closed contour: the segment from `L+iT_1` to
`L'+iT_1` is unaccounted for.  Replacing `L'` by `L` in (5.2) gives the
expected vertical side and appears to repair this local defect.  The paper
does not say that this correction is intended.

The final sentence of Lemma 4 again invokes holomorphy near the canceled
pole without spelling out a maximum-modulus argument.  In that neighborhood
the asserted right side grows like a small positive power, so this gap also
looks repairable after uniform boundary estimates are stated.

### 5.3 Lemma 5's Cauchy circles

The two Cauchy circles themselves have the advertised geometry.  Their
center is `z1-z0` and radius is `z0`; since `z0<=z1<=2z0`,

```text
|z|<=z1                                                     (5.3)
```

on either circle.  Differentiating `(U/n)^(-z)` does produce the normalized
weights `(z0 log(n/U))^j/j!`.  Thus there is no intrinsic Cauchy-radius
miracle here: the estimates are only as strong as the uniform Perron bounds
fed into them.

There are two internal formula defects in this part.

1. In equation (32), the residue at `z=0` is printed with
   `sum_(j=0)^J p_J(...)`.  Direct substitution gives
   `sum_(j=0)^J p_j(...)`.  The next estimate uses the latter identity
   through `sum p_j<1`, so a correction is necessary.
2. Immediately before equation (39), Cauchy's formula correctly yields

   ```text
   [(-z0)^J/J!] D^J G_UV(...)=weighted Dirichlet sum+error.  (5.4)
   ```

   Equation (39) drops the factor `(-z0)^J/J!` from its left side while
   retaining normalized quantities on the right.  Lemma 5's statement
   restores the factor.  Read charitably, this is a typographical error;
   read literally, equation (39) is false.

These defects reduce confidence in the long estimate, but neither is needed
for the decisive refutation: even granting Lemma 5 in exactly its stated
form, the theorem still fails at (45).

### 5.4 Final exponent arithmetic

The compression of the error terms in equation (44) was rechecked under

```text
2r<=z0<=2.01r,
z0<=z1<=2z0,
epsilon<=r/100,
T<=V^(r/2),
U=V^(2/3).                                                  (5.5)
```

No decisive exponent error is needed there.  For example,

```text
V^(-2z0+r/4+6epsilon) U^z1
 <= V^(-13r/12+6epsilon),                                  (5.6)
```

and the apparent bottleneck is exactly

```text
V^(r/4+6epsilon) U^(-r)
 =V^(-5r/12+6epsilon).                                      (5.7)
```

The terms carrying powers of `T` remain smaller after using
`T<=V^(r/2)` and `r<=1/100`.  Thus, conditional on Lemma 5, the final
`O(V^(-5r/12+6epsilon))` collection is arithmetically plausible.  The
proof fails at the sign and size of the main truncated exponential, not at
this last bookkeeping step.

## 6. Consequence for the fixed-strip program

This audit supplies a hard literature gate:

```text
Puglisi v9 does not prove quasi-RH => RH.                     (6.1)
```

In particular it gives neither branch of the present objective:

```text
there exists eta>0 with zeta(s)!=0 for Re(s)>1-eta,
```

or

```text
sup_rho Re(rho)=1.                                          (6.2)
```

The useful residue is a reality check for future high-order Taylor
strategies.  Whenever a Lagrange remainder contributes

```text
q x^J/J!,             q only known to lie in (0,1),          (6.3)
```

one cannot obtain an exponentially large one-sided contradiction from an
alternating partial exponential at `J~2x`.  Either the Taylor point must be
quantitatively controlled so that `q` stays below the true tail ratio, or a
different representation with a sign-definite integral remainder is
needed.  Generic Cauchy bounds and parity alone do not provide that control.
