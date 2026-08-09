# R113 exact-R105 multiplier-average fail-fast audit

Status: additive Parseval gives a genuine quarter-power average in the
multiplier `k` for each fixed Vaughan product modulus.  On the actual
square-root product boxes, elementary divisor-fiber sparsity improves this
by a second quarter power.  Neither estimate survives the full top
`k=j theta` range as a fixed-power gain: folding `K asymp c^2` integer
multipliers modulo `c` costs `c^(1/2)`.  The two exact `Q_h` marginals can,
at best, remove this folding loss through square-root cancellation on
modular hyperbolas.  Even granting that strongest plausible improvement
for every composite Vaughan modulus, the complete top block returns only
to its natural `X^(1+o(1))` endpoint.  It does not go below it.

Date: 2026-08-07.

Predecessors:
[`R105-QH-VAUGHAN-TAIL-NATIVE-BRIDGE-AUDIT.md`](R105-QH-VAUGHAN-TAIL-NATIVE-BRIDGE-AUDIT.md),
[`R102-CENTER-ANNIHILATED-OFF-AXIS-GATE.md`](R102-CENTER-ANNIHILATED-OFF-AXIS-GATE.md),
and
[`COEFFICIENT-SPECIFIC-LOW-BEAT-TENSOR-GATE.md`](COEFFICIENT-SPECIFIC-LOW-BEAT-TENSOR-GATE.md).

## 1. Verdict and exact location of the average

On the `g=1` top block, fix the first cofactor product

```text
c=q_1 asymp X
```

and unfold the second one as `q_2=db`, where

```text
d asymp D,       b asymp B,       D,B asymp sqrt(c).
```

R105 (2.6), followed only by the exact identity defining the Vaughan
coefficient, gives

```text
E_top
 =integral_t sum_(c asymp X) h(c)c^(-it)
    sum_k nu_t(k) F_(c,t)(k) dt,                       (1.1)

F_(c,t)(k)
 =sum_(d in I_d,b in I_b;(db,c)=1)
    alpha_t(d) beta_t(b)e_c(k inverse(db)),            (1.2)

alpha_t(d)=mu(d)d^(-1-it),
beta_t(b)=Lambda(b)b^(-1-it).                          (1.3)
```

Dyadic endpoint weights may be inserted into (1.3).  They do not affect
any exponent below.  Formula (1.1) is the actual R105 object: the
multiplier is not an auxiliary variable, but

```text
k=j theta.                                             (1.4)
```

The top physical block has

```text
abs(j)asymp X,       abs(theta)asymp X,
abs(k)asymp K=X^2.                                    (1.5)
```

The favorable R84 kernel ledger, which we grant throughout this fail-fast
audit, is

```text
integral norm(nu_t)_2 dt
 <<X^o(1)sqrt(K)(1+Theta/X)^(1/2).                     (1.6)
```

Thus (1.6) is `X^(1+o(1))` on (1.5).  R105 (4.8)--(4.9)
shows why no power improvement in (1.6) follows from physical smoothness:
after scaling, the high-shift amplitude is a fixed nonzero profile on a
fixed positive-measure `(j/X,theta/X)` box.

The fixed-modulus multiplier average is real, but its exponent ledger is

```text
generic Parseval + generic folding                 X^(7/4+o(1));
product-fiber Parseval + generic folding            X^(3/2+o(1));
product-fiber Parseval + ideal Q_h/Weil folding     X^(1+o(1));
required complete-tail fixed power                  X^(1-delta). (1.7)
```

The last line is not reached for any fixed `delta>0`.

## 2. Exact additive Parseval theorem

The following statement works for every positive integer modulus, not only
for primes.

**Lemma 2.1 (inverse-product multiplier Parseval).**  Let `I_d,I_b` be
sets of distinct residues modulo `c`, of cardinalities `D,B`, and let the
weights be supported on units.  Put

```text
F_c(k)=sum_(d in I_d,b in I_b)
          alpha_d beta_b e_c(k inverse(db)).           (2.1)
```

Then

```text
sum_(k mod c)abs(F_c(k))^2
 =c sum_(x in (Z/cZ)^times)
     abs(sum_(db=x mod c)alpha_d beta_b)^2,            (2.2)

norm(F_c)_(l2(k mod c))
 <=sqrt(c) min(sqrt(D),sqrt(B))
      norm(alpha)_2 norm(beta)_2.                      (2.3)
```

**Proof.**  Define the multiplicative convolution

```text
C(x)=sum_(db=x mod c)alpha_d beta_b.
```

Inversion permutes `(Z/cZ)^times`, so `F_c` is the unnormalized additive
Fourier transform of `x |-> C(inverse(x))`.  Additive orthogonality proves
(2.2).  Young's inequality on the finite unit group gives

```text
norm(C)_2
 <=min(norm(alpha)_1 norm(beta)_2,
       norm(alpha)_2 norm(beta)_1),
```

and Cauchy's inequality proves (2.3).  QED.

At `D,B asymp sqrt(c)`, (2.3) is precisely

```text
norm(F_c)_2
 <<c^(3/4)norm(alpha)_2 norm(beta)_2.                 (2.4)
```

For the actual coefficients (1.3), uniformly in `t`,

```text
norm(alpha_t)_2<<c^(-1/4+o(1)),
norm(beta_t)_2 <<c^(-1/4+o(1)).                       (2.5)
```

Hence the proposed coefficient-uniform estimate gives

```text
norm(F_(c,t))_2<<c^(1/4+o(1)).                        (2.6)
```

No primality, Kloosterman completion, or short additive support has been
used.

## 3. The actual square-root boxes give a sharper Parseval bound

The generic factor `c^(1/4)` in (2.6) is unnecessary on the fixed-ratio
R105 product boxes.

**Lemma 3.1 (bounded product-fiber multiplicity).**  Suppose

```text
I_d subset [lambda_d sqrt(c),mu_d sqrt(c)],
I_b subset [lambda_b sqrt(c),mu_b sqrt(c)]             (3.1)
```

for fixed positive endpoints.  Then

```text
max_(x mod c)#[(d,b) in I_d times I_b: db=x mod c]
 <<c^epsilon.                                         (3.2)
```

Consequently

```text
norm(F_c)_2
 <<c^(1/2+epsilon)norm(alpha)_2 norm(beta)_2.          (3.3)
```

**Proof.**  Every integer product `db` lies in one fixed multiple interval
`[A c,B c]`.  For fixed `x mod c`, it can therefore equal only one of
`O(1)` integers `x+ell c`.  Each such integer has at most
`tau(x+ell c)<<c^epsilon` admissible factorizations.  This proves (3.2).
For each residue fiber, Cauchy's inequality gives

```text
abs(C(x))^2
 <=c^epsilon sum_(db=x mod c)abs(alpha_d beta_b)^2.
```

Sum in `x` and use (2.2).  QED.

For (1.3), (2.5) and (3.3) give the particularly clean bound

```text
norm(F_(c,t))_2<<c^o(1).                              (3.4)
```

This second quarter power is coefficient-independent; it comes from the
geometry of the actual Vaughan support, not cancellation in `mu` or
`Lambda`.

## 4. Folding `k=j theta` modulo `c`

Parseval sees only one complete residue system.  The R81 multiplier is an
integer with range up to `c^2`.  Define

```text
V_(c,t)(a)=sum_(k in K; k=a mod c)nu_t(k),             (4.1)
```

where `K` denotes one signed dyadic multiplier block.  Periodicity gives
the exact identity

```text
sum_(k in K)nu_t(k)F_(c,t)(k)
 =sum_(a mod c)V_(c,t)(a)F_(c,t)(a).                  (4.2)
```

**Lemma 4.1 (residue-folding cost).**  If the integer support has diameter
`O(K)`, then

```text
norm(V_(c,t))_2
 <=[1+K/c]^(1/2)norm(nu_t)_2.                         (4.3)
```

This is Cauchy's inequality in each residue class.  It is sharp for a flat
sequence on a complete interval.  At the top range `K asymp c^2`, (4.3)
costs

```text
c^(1/2).                                              (4.4)
```

Combining (2.6), (4.2)--(4.4), and (1.6) gives, for one fixed `c`,

```text
integral abs(sum_k nu_t(k)F_(c,t)(k))dt
 <<c^(1/4+o(1))*c^(1/2)*c
 =c^(7/4+o(1)).                                       (4.5)
```

Using the sharper actual-support estimate (3.4) improves this only to

```text
c^(3/2+o(1)).                                         (4.6)
```

Finally,

```text
sum_(c asymp X)abs(h(c))
 <=sum_(c asymp X)tau(c)log(c)/c=X^o(1),              (4.7)
```

so the outer `c`-sum in (1.1) changes neither exponent.  Equations
(4.5)--(4.7) prove the first two lines of (1.7).  They are respectively
`X^(3/4-o(1))` and `X^(1/2-o(1))` worse than R105's elementary
`X^(1+o(1))` energy bound.

For reference, the general favorable ledgers before setting `K=c^2` are

```text
B_generic(K)
 <<c^(1/4+o(1))sqrt(K)sqrt(1+K/c),

B_product(K)
 <<c^o(1)sqrt(K)sqrt(1+K/c).                          (4.8)
```

Thus multiplier Parseval is useful on low products.  The full top box is
the obstruction.

## 5. What `Q_h` can and cannot do to the fold

The transformed kernel satisfies exactly

```text
Lhat_Q(xi,0)=Lhat_Q(0,eta)=0.                         (5.1)
```

Before grouping by `k`, its scaled top amplitude has the form

```text
W(j/X,theta/X)
 =integral mathcal L_Q(y+j/X,y)
    e((theta/X)y/rho)dy,                              (5.2)
```

with harmless fixed ratio `rho`.  Integrating (5.2) in its first variable
and using the second kernel marginal gives

```text
integral_R W(sigma,tau)d sigma=0                      (5.3)
```

for every `tau`.  Therefore `Q_h` does remove the constant Fourier mode
from a **fully recombined** smooth shift profile.

This suggests a legitimate improvement over (4.3).  For a prime modulus
and a unit residue `a`, the folded pre-product weight is a modular-hyperbola
sum

```text
V_c(a)=sum_(j theta=a mod c)W(j/c,theta/c).            (5.4)
```

Completing a smooth `W` additively writes its nonconstant terms as
Kloosterman sums

```text
sum_(j mod c)^* e_c(mj+na inverse(j)),                (5.5)
```

of square-root size.  If the sampled zero mode and both sampled axes are
recombined using (5.1), the optimistic consequence is

```text
abs(V_c(a))<<c^(1/2+o(1)),
norm(V_c)_(l2(a mod c))<<c^(1+o(1)).                  (5.6)
```

The same scale is plausible for the Vaughan composite moduli after divisor
stratification and the composite Weil bound.  Establishing it uniformly
through finite spline regularity, nonunit `j,theta`, and every ordered
physical shell would still require a proof.  We do not need to assume that
proof here: grant (5.6) for free.

The ungrouped top amplitude has `l2` scale `c^(1+o(1))`.  Thus (5.6)
removes exactly the `c^(1/2)` folding loss in (4.4), but supplies no saving
beyond the random/Weil scale.  Combining the best coefficient estimate
(3.4) with (5.6) gives only

```text
abs(E_top)<<X^(1+o(1)),                               (5.7)
```

the third line of (1.7).

There are three reasons not to claim more from marginal nullity.

1. Marginal cancellation is not hyperbola cancellation.  Over `F_p`, let
   `chi` be a nonprincipal multiplicative character and put

   ```text
   W(j,theta)=chi(j theta),       j,theta!=0.
   ```

   Both marginals vanish, but

   ```text
   sum_(j theta=a)W(j,theta)=(p-1)chi(a),              (5.8)
   ```

   so the generic `sqrt(p)` folding ratio is saturated.  Extra smooth
   structure, not (5.1) alone, is essential.
2. The modular zero class contains nonzero integers

   ```text
   k=ell c,       1<=abs(ell)<<c.                     (5.9)
   ```

   R104 removes integer `j=0` and `theta=0`; it does not remove (5.9).
   For these aliases `F_c(k)=F_c(0)` and the inverse-product phase has no
   oscillation.  This is the low-conductor resonance already isolated in
   R105 (6.5)--(6.6).
3. `Q_h` is a fixed three-translate operator, and its Gram kernel is a
   fixed nine-packet sum.  It creates no modulus-dependent factor capable
   of beating the square-root scale in (5.5).  R105 (4.9) moreover proves
   that a fixed positive-measure high `(j/X,theta/X)` region remains at
   natural size.

Thus the kernel can plausibly recover the loss caused by treating aliases
independently.  It does not create the additional fixed power required
after that recovery.

## 6. Exact endpoint and next possible theorem

The best version of this route uses all three favorable facts:

```text
inverse-product additive Parseval                    EXACT;
bounded square-root product fibers                   EXACT;
Q_h removal of the smooth hyperbola constant mode    EXACT CONTINUOUSLY;
uniform composite hyperbola square-root bound         GRANTED;
resulting complete top energy                         X^(1+o(1)). (6.1)
```

To obtain `X^(1-delta)`, one would still need a **joint** estimate saving a
power in the pairing

```text
sum_(a mod c)F_(c,t)(a)V_(c,t)(a),                    (6.2)
```

not separate `l2` bounds for its two factors.  Equivalently, one needs one
of the following genuinely new inputs.

* A power-saving correlation theorem between the additive Fourier
  transform of the square-root inverse-product Vaughan convolution and the
  smooth center-annihilated modular-hyperbola trace.
* A varying-`c` large sieve applied before the triangle inequality in
  (4.7), strong enough to save beyond the `X^1` endpoint and uniform in the
  low conductors `(k,c)`.
* A fixed-power estimate for the modular-zero coefficient
  `F_c(0)`, together with the corresponding estimates for every large
  divisor of `(k,c)`.  For the actual `mu` factor this already asks for
  fixed-power Möbius cancellation and cannot be imported as elementary
  input to a strip proof.

The multiplier average is therefore valuable: it replaces the unavailable
short-box partition by an exact native operation and identifies a possible
`Q_h`--Kloosterman interaction.  It does not, by itself or together with
the currently proved kernel identities, yield a fixed zero-free strip.

```text
fixed uniform zero-free strip                         NOT YET PROVED;
nonexistence of such a strip                          NOT PROVED. (6.3)
```
