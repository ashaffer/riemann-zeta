# Exact twisted-second-moment reduction for the long-mollifier strip route

Status: **exact finite reduction proved; the classical main aggregate is at
natural scale by an elementary polylogarithmic bound; the Möbius-weighted
aggregate remainder remains OPEN.**

Date: 2026-08-09.

This note sharpens Gate A of the long-mollifier program.  It avoids choosing
an approximate functional equation prematurely and keeps the cutoff average,
Möbius signs, and rational twists together.

## 1. Averaged mollified moment

For `y>1`, put

```text
M_y(s)=sum_(d<=y) mu(d)d^(-s) log(y/d)/log y,

I_y(0,T)=integral_0^T
 |zeta(1/2+it)M_y(1/2+it)|^2dt.
```

For `Y>1`, define

```text
A(Y,T)=integral_1^Y I_y(0,T)dy.                          (1.1)
```

Let `K_Y(d,e)` be the positive cutoff kernel derived in
[`LONG-MOLLIFIER-CUTOFF-KERNEL.md`](LONG-MOLLIFIER-CUTOFF-KERNEL.md):

```text
K_Y(d,e)=integral_1^Y
  1_(d<=y)1_(e<=y)
  log(y/d)log(y/e)/(log y)^2dy.                          (1.2)
```

Finally define the rationally twisted zeta second moment

```text
J_T(d,e)=integral_0^T
 |zeta(1/2+it)|^2 (e/d)^(it)dt.                          (1.3)
```

## 2. Exact finite identity

Because the mollifier sum is finite, expansion and Fubini require no
convergence theorem beyond the ordinary integrability of the finite
expression.

### Proposition 2.1

For every `Y,T>1`,

```text
A(Y,T)
 =sum_(d,e<=Y)
   mu(d)mu(e)/sqrt(de) * K_Y(d,e) * J_T(d,e).            (2.1)
```

#### Proof

On the critical line,

```text
M_y(1/2+it)
 =sum_(d<=Y) mu(d)/sqrt(d)
   d^(-it) 1_(d<=y)log(y/d)/log y.
```

Multiplication by the conjugate produces the phase `(e/d)^(it)`.  Expanding
the two finite divisor sums, integrating first in `t` and then in `y`, gives
(2.1), with the `y` integral equal to (1.2).

This is the first fully completed arithmetic object in the route.  No prime
head, late-divisor correction, dual zeta sum, or cutoff boundary has yet been
estimated separately.

## 3. Classical twisted main term

Put

```text
g=(d,e).
```

The diagonal equation obtained by opening the two zeta Dirichlet series is

```text
n e = m d.                                               (3.1)
```

Writing `d=g d_0`, `e=g e_0`, with `(d_0,e_0)=1`, its solutions are

```text
m=e_0 r,
n=d_0 r.                                                (3.2)
```

This explains the universal gcd factor in the classical twisted-second-
moment main term.  For the sharp interval `[0,T]`, its standard shape is

```text
Main_T(d,e)
 =T g/sqrt(de)
  [log(T g^2/(2 pi d e))+2 gamma-1].                    (3.3)
```

The exact endpoint smoothing changes the displayed lower-order constants but
not the gcd structure.  Define the remainder by

```text
R_T(d,e)=J_T(d,e)-Main_T(d,e).                           (3.4)
```

Substitution into (2.1) gives

```text
A(Y,T)=MainAggregate(Y,T)+RemainderAggregate(Y,T),       (3.5)
```

where

```text
MainAggregate(Y,T)
 =T sum_(d,e<=Y) mu(d)mu(e) (d,e)/(de) K_Y(d,e)
   [log(T(d,e)^2/(2 pi d e))+2 gamma-1],                 (3.6)

RemainderAggregate(Y,T)
 =sum_(d,e<=Y) mu(d)mu(e)/sqrt(de)
   K_Y(d,e)R_T(d,e).                                    (3.7)
```

## 4. The main aggregate is already at natural scale

The main term does not contain the length barrier.  A completely elementary
absolute bound suffices.

First, because each cutoff weight lies in `[0,1]`,

```text
0<=K_Y(d,e)<=Y.                                         (4.1)
```

Next,

```text
sum_(d,e<=Y) (d,e)/(de)
 <=sum_(g<=Y) 1/g [sum_(a<=Y/g)1/a]^2
 <=(1+log Y)^3.                                         (4.2)
```

The first inequality writes `d=ga`, `e=gb` and drops the coprimality
condition.  The second uses the elementary harmonic-sum bound twice and then
again in `g`.

Finally, since

```text
1/Y^2 <= (d,e)^2/(de) <= 1,
```

the logarithmic bracket in (3.6) is bounded in absolute value by

```text
C[1+log T+log Y]                                        (4.3)
```

for an absolute constant `C`.  Combining (4.1)--(4.3) gives

```text
|MainAggregate(Y,T)|
 << T Y (1+log Y)^3(1+log T+log Y).                     (4.4)
```

For every fixed `theta>0` and `Y=T^theta`, (4.4) is

```text
T Y T^epsilon                                           (4.5)
```

for any fixed `epsilon>0`, once `T` is sufficiently large.  Therefore the
main aggregate already meets the natural-scale requirement of the averaged
mollifier criterion.  No Möbius cancellation is needed for this part.

The sole analytic obstruction in this reduction is now (3.7).

## 5. Why individual-twist absolute values are the wrong norm

The target for `Y=T^theta` is

```text
A(Y,T) << T Y T^epsilon.                                 (5.1)
```

A pointwise estimate for each `R_T(d,e)`, followed by

```text
sum_(d,e) |mu(d)mu(e)K_Y(d,e)R_T(d,e)|/sqrt(de),         (5.2)
```

discards every Möbius sign and every reciprocity cancellation.  Since the
early supported part of `K_Y` is of order `Y`, this recovers the ordinary
long-Dirichlet-polynomial barrier rather than crossing it.

The required theorem is an estimate for the **signed aggregate** (3.7), not a
uniform estimate for a single rational twist.

## 6. Reciprocity form of the missing theorem

Recent twisted-second-moment work makes the remainder structurally explicit.
Khan's reciprocity formula, for prime twists and with a stated extension to
general integer twists, transforms a rationally twisted zeta second moment
into:

1. its gcd/main terms;
2. a dual family of twisted Dirichlet `L`-function second moments;
3. controlled transform errors.

Applying that transformation to (3.7) **before** absolute values suggests the
following route.

### Reciprocity program

1. Use one fixed smooth even time weight so every transform is uniform.
2. Extend/freeze the reciprocity identity for squarefree integer twists
   `d,e`, the only twists surviving the Möbius weights.
3. Insert the identity into (3.7) and sum over `d,e` first.
4. Evaluate the resulting Möbius--character transforms exactly where
   possible.
5. Apply a hybrid large sieve only to the complete dual family.
6. Retain the cutoff kernel and all diagonal correction terms throughout.

The hope is not that reciprocity makes each `R_T(d,e)` small.  It is that the
complete double Möbius sum of the dual moments has lower conductor or an
additional orthogonality unavailable in the original variables.

## 7. Precise target theorem

For one fixed smooth time weight `W`, let `R_{T,W}(d,e)` denote the remainder
after subtracting the normalization-matched smooth main term.  Since the main
aggregate is covered by (4.4), the exact missing estimate is

```text
there exists theta>1 such that, for Y=T^theta and every epsilon>0,

sum_(d,e<=Y) mu(d)mu(e)/sqrt(de)
 K_Y(d,e) R_{T,W}(d,e)
  <<_epsilon T Y T^epsilon.                              (7.1)
```

Any bound of the stronger form `T Y T^(-eta)` is a useful safety margin, but
is not logically necessary for obtaining a fixed strip.

The quantifiers matter: the estimate must hold for every sufficiently large
`T`, not merely on average over `T`, because the mollifier criterion excludes
individual zeros.

## 8. Relation to the short-interval barrier

Opening `J_T(d,e)` by a Fourier/approximate-functional-equation calculation
recovers the near-shift scale

```text
H=Y/T.
```

Thus the short-Möbius-sum formulation and the twisted-moment remainder
formulation are two coordinate systems for the same obstruction:

```text
near shifts in the original Dirichlet polynomial
        <==>
dual rational-twist moments under reciprocity.          (8.1)
```

The reciprocity coordinate system is preferable if the complete Möbius sum
can be transformed before Cauchy--Schwarz.  If every argument still takes
absolute values twist by twist, it collapses back to the missing factor `H`
identified in the cutoff-kernel audit.

## 9. Immediate implementation tasks

1. Freeze a smooth version of `J_T(d,e)` and its main term with all constants.
2. Verify (2.1) numerically for small `Y` as a regression test.
3. Transcribe the squarefree-integer reciprocity formula, including common
   factors and parity.
4. Derive the exact Möbius--character coefficient after summing `d,e`.
5. Estimate the complete dual family by the hybrid large sieve and record the
   resulting exponent ledger.

A successful exponent beyond `theta=1` would give a genuine fixed zero-free
strip through `LongMollifierStripReduction.lean`.  No such exponent is proved
in this note.

## 10. Primary literature

- R. Balasubramanian, J. B. Conrey, and D. R. Heath-Brown, *Asymptotic mean
  square of the product of the Riemann zeta-function and a Dirichlet
  polynomial*, J. reine angew. Math. 357 (1985), 161--181.
- S. Bettin, V. Chandee, and M. Radziwill, *The mean square of the product of
  the Riemann zeta-function with Dirichlet polynomials*, J. reine angew. Math.
  729 (2017), 51--79.
- R. Khan, *A reciprocity relation for the twisted second moment of the
  Riemann Zeta function*, arXiv:2401.01057, 2024.
- H. Ishikawa and K. Matsumoto, *An explicit formula of Atkinson type for the
  product of the Riemann zeta-function and a Dirichlet polynomial*, Cent. Eur.
  J. Math. 9 (2011), 102--126.
