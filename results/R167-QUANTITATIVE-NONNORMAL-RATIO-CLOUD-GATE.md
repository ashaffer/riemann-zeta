# R167 quantitative nonnormal-ratio cloud gate

## Status

R165 proves qualitatively that a safe `q=2` bridge section must have a
nonnormal multiplier ratio and hence an unbounded ratio-value cloud.  R166
shows that the same nonnormality issue is the remaining analytic bill in the
mixed-product amplifier.  This report quantifies that bill.

Suppose all channels satisfy, on a fixed nonempty right cap `V`,

```text
F_(j,H)=Z M_(j,H)=1+O(H^(-mu)),             mu>0,         (0.1)
```

and every `M_(j,H)` is a unit on the fixed localization disc.  If either
the `q=2` collective cofactor or the even mixed-product cofactor is
zero-free, then along a subsequence some unit ratio

```text
R_H=M_(j,H)/M_(1,H)                                      (0.2)
```

obeys the following quantitative alternatives on fixed nested subdiscs.

```text
T(R_H) >=c_0 mu log H-O(1),                              (0.3)

# distinct {R_H=a}
 >=c_1 mu log H-c_2 log^+ T_outer(R_H)-O(1)              (0.4)
```

for every fixed `a in C*\{1}` and suitable positive geometry constants.  In
particular:

1. if `T_outer(R_H)=O(log H)`, then

   ```text
   # distinct {R_H=a} >=c_1 mu log H-O(log log H);        (0.5)
   ```

2. if `T_outer(R_H)<=H^(lambda+o(1))`, then

   ```text
   # distinct {R_H=a}
    >=[c_1 mu-c_2 lambda-o(1)]log H-O(1).                 (0.6)
   ```

The second inequality is informative when the displayed coefficient is
positive.  Without a relation between `mu` and `lambda`, (0.3) is the
unconditional quantitative conclusion.

For two channels, take `a=-w_2/w_1`; (0.5) counts zeros of the weighted
mean `w_1M_1+w_2M_2`.  Taking `a=-1` in general counts an artificial
pairwise-cancellation cloud.

The proof has two elementary components.  A two-constants theorem propagates
the `H^(-mu)` cap smallness of `R_H-1`; any nonnormal excursion then forces
characteristic at least `asymp log H`.  The three-value second main theorem,
applied to the values `0`, `infinity`, and `a`, converts characteristic to
distinct `a`-points because a unit omits the first two values.

This is sharp in scale and does **not** contradict the R166 fixed-`q`
support ledger.  A logarithmic cloud fits inside an `H^(lambda+o(1))`
outer budget for every `lambda>0`, and it merely saturates an `O(log H)`
characteristic budget.  It supplies a mandatory term and a coefficient
inequality, not a no-go theorem.

```text
power-rate cap agreement                                 ASSUMED
safe cofactor                                             ASSUMED
nonnormal ratio                                           NECESSARY
ratio characteristic lower bound                         Omega(log H)
ratio a-point cloud under T=O(log H)                      Omega(log H)
two-channel weighted-mean zero cloud                      Omega(log H)
contradiction with H^lambda outer ledger                  NO
contradiction with fixed-q support amplification          NO
wild arithmetic safe section                             OPEN
fixed uniform zeta zero-free strip                        NOT PROVED
zeros approaching one                                     NOT PROVED
```

Date: 2026-08-08.

Predecessors:
[`R165-NONLINEAR-SAFE-FIBER-AND-GLOBAL-ENTIRE-GATE.md`](R165-NONLINEAR-SAFE-FIBER-AND-GLOBAL-ENTIRE-GATE.md)
and
[`R166-MIXED-PRODUCT-SUPPORT-AMPLIFIER-AND-COLLECTIVE-COFACTOR-GATE.md`](R166-MIXED-PRODUCT-SUPPORT-AMPLIFIER-AND-COLLECTIVE-COFACTOR-GATE.md).

## 1. Fixed geometry and characteristic notation

All constants below depend only on the fixed localization geometry.  After
a conformal change of coordinate, work in the unit disc.  Choose a closed
disc `E` compactly contained in the right cap and fixed nested domains

```text
E subset U_0 compactly in U_1 compactly in U_2
  compactly in U_3 compactly in Omega.                   (1.1)
```

The domain `U_0` is chosen large enough to contain `E` and a compact set on
which a nonnormal ratio makes an excursion.  We write `T_j(R)` for a
standard Nevanlinna characteristic on a coordinate circle enclosing `U_j`.
Changing the coordinate circles only changes fixed constants.

If the assumed outer bound is stated for the individual multipliers in
Nevanlinna characteristic, it transfers to their ratios: the first main
theorem and the cap normalization give

```text
T(M_j/M_1)<=T(M_j)+T(1/M_1)+O(1)
            <=T(M_j)+T(M_1)+O(1).                        (1.2)
```

A one-sided supremum bound for `M_j` alone does not control a ratio, since a
unit can be extremely small.  In that formulation one needs the
corresponding bound for `1/M_j`, or directly for the ratios.

Two standard local estimates will be used:

```text
sup_(U_j) log^+|R|
 <=C_j[T_(j+1)(R)+1],                                    (1.3)
```

and the three-value second main theorem on nested discs,

```text
T_1(R)
 <=Nbar_2(R,0)+Nbar_2(R,infinity)+Nbar_2(R,a)
   +C log^+[T_3(R)+2]+C.                                 (1.4)
```

Here `Nbar` is the truncated counting function.  Since all radii are fixed
and separated, a lower bound for `Nbar_2(R,a)` gives the same-order lower
bound for the number of distinct `a`-points in a slightly larger fixed
subdisc.

## 2. Quantitative propagation of cap smallness

### Lemma 2.1 -- two-constants characteristic lower bound

Let `R_H` be units on `Omega` satisfying

```text
sup_E|R_H-1|<=C H^(-mu).                                 (2.1)
```

Suppose that for some fixed compact `K subset U_0\E`, some `delta>0`, and
a subsequence,

```text
sup_K|R_H-1|>=delta.                                     (2.2)
```

Then

```text
T_1(R_H)>=c_0 mu log H-O(1).                             (2.3)
```

#### Proof

Apply the two-constants theorem to the subharmonic function

```text
u_H=log|R_H-1|                                            (2.4)
```

on `U_0\E`.  The harmonic measure of `partial E`, viewed from `K`, has a
positive geometry-dependent lower bound `theta`.  If

```text
L_H=log^+ sup_(U_0)|R_H-1|,                              (2.5)
```

then (2.1)--(2.2) give

```text
log delta
 <=theta[log C-mu log H]+(1-theta)L_H+O(1).              (2.6)
```

Consequently

```text
L_H>=[theta/(1-theta)]mu log H-O(1).                     (2.7)
```

The local characteristic estimate (1.3), applied on one larger fixed
domain, proves (2.3).  QED.

If one assumes directly that

```text
log sup_(U_0)(1+|R_H|)<=B log H+O(1),                    (2.8)
```

then the same proof gives the explicit necessary coefficient inequality

```text
B>=[theta/(1-theta)]mu+o(1).                             (2.9)
```

Thus an arbitrarily accurate cap approximation cannot coexist with a
fixed polynomial-growth exponent unless that exponent grows proportionally.

## 3. From characteristic to distinct ratio values

### Theorem 3.1 -- quantitative unit-ratio cloud

Under the hypotheses of Lemma 2.1, for every fixed `a in C*\{1}`,

```text
# distinct {s in U_3:R_H(s)=a}
 >=c_1 mu log H-c_2 log^+[T_3(R_H)+2]-O(1).              (3.1)
```

#### Proof

Because `R_H` is a holomorphic unit,

```text
Nbar_2(R_H,0)=Nbar_2(R_H,infinity)=0.                    (3.2)
```

Equations (1.4) and (2.3) therefore give

```text
Nbar_2(R_H,a)
 >=c_0 mu log H-C log^+[T_3(R_H)+2]-O(1).                (3.3)
```

Take the characteristic coordinate center inside `E`.  Since `a!=1`,
(2.1) excludes `a`-points from a fixed neighborhood of that center for all
large `H`.  Every remaining distinct point therefore contributes at most a
fixed amount to the counting function on the fixed outer circle.  Hence the
number of distinct points is bounded below by a fixed multiple of (3.3),
proving (3.1).  QED.

If `T_3(R_H)=O(log H)`, the error in (3.1) is `O(log log H)`, which proves
(0.5).  If

```text
T_3(R_H)<=H^(lambda+o(1)),                               (3.4)
```

then

```text
log^+T_3(R_H)<=(lambda+o(1))log H,                       (3.5)
```

which gives (0.6) after renaming the fixed constants.

## 4. Why a safe section supplies the required excursion

Equation (0.1) gives, uniformly on the cap,

```text
M_(j,H)/M_(1,H)=F_(j,H)/F_(1,H)
               =1+O(H^(-mu)).                           (4.1)
```

For the `q=2` square-average cofactor, R165, Theorem 2.1, proves that at
least one ratio family is nonnormal.  Therefore, after taking a subsequence,
there are a fixed compact `K` and `delta>0` for which (2.2) holds.

The same conclusion holds for the even mixed-product cofactor.  Here is the
short reduction.  Suppose all ratios

```text
r_j=M_j/M_1                                              (4.2)
```

were normal.  Cap convergence and the identity theorem would give
`r_j->1` locally throughout a slightly smaller localization disc.  Regard

```text
Phi_H(s,x)=product_j[x r_j(s)-1]-1                       (4.3)
```

as a polynomial in `x`.  For even `q`, `x=0` is always one root.  The
simple diagonal root `x=2` persists as a holomorphic unit root

```text
a_H(s)=2+o(1)                                             (4.4)
```

on the smaller disc.  If the mixed-product cofactor is zero-free, then

```text
F_(1,H)(s)!=a_H(s).                                      (4.5)
```

Consequently

```text
G_H=2F_(1,H)/a_H                                         (4.6)
```

is holomorphic, has exactly the fixed zero divisor of `Z`, tends to one on
the cap, and omits `2`.  This contradicts R155, Theorem 2.1.  Hence a safe
mixed-product family also supplies a nonnormal ratio and Lemma 2.1 applies.

## 5. The precise ledger consequence

For two channels, the weighted mean satisfies

```text
w_1M_1+w_2M_2=0
iff
M_1/M_2=-w_2/w_1.                                       (5.1)
```

Thus (0.5) forces `Omega(log H)` distinct weighted-mean zeros whenever the
ratio characteristic is `O(log H)`.  For arbitrary `J`, taking `a=-1`
forces the same number of pairwise cancellations `M_j+M_1=0` for at least
one channel.

This lower bound is the natural quantitative form of the R165 cloud, but
its scale is not fatal to R166.  The R166 outer ledger is

```text
H^(lambda+o(1)),                                         (5.2)
```

and its fixed-`q` support gain closes conditionally once `q` exceeds a
fixed multiple of `lambda`.  Since

```text
log H=H^(o(1)),                                          (5.3)
```

the forced cloud changes constants and logarithmic factors, not the power
`lambda`.  Even in the sharp `T=O(log H)` regime, (0.5) merely shows that
the available characteristic is saturated up to constants.  It does not
contradict a fixed sufficiently large `q`.

Accordingly, the remaining theorem is still arithmetic: construct the
nonnormal optional-prime ratios while proving that their collective
cofactor stays safe.  Quantitative normal-family theory alone charges the
logarithmic bill but does not close the route.
