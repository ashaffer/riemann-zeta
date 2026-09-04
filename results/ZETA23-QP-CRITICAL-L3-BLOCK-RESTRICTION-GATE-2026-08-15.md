# QP critical absolute-`L3` block restriction gate

**Date:** 2026-08-15  
**Verdict:** the sharp arbitrary-coefficient absolute-`L3` estimate is
**open**.  It is not contradicted by the half-integer revival packet: that
packet saturates its power, up to logarithms.  A block-local proof is
elementary, but its global recombination is a new curvature-sensitive
reverse square-function theorem.  Ordinary Littlewood--Paley theory does
not supply that direction.

No four-cycle bound, QP theorem, or strip theorem is claimed here.

---

## 1. Normalization and the target

Let

```text
B=Y^(50/33),       D=Y^2/B=Y^(16/33),
R=Y/sqrt(B)=sqrt(D)=Y^(8/33).                       (1.1)
```

On a fixed compact `s`-interval, with a fixed nonnegative smooth density
`psi`, put

```text
X_x(s)=sum_(n in S_Y) x_n exp(i B s log(n/Y)).       (1.2)
```

The proposed restriction estimate is

```text
||X_x||_(L^3(psi ds))
  << Y^o(1) D^(1/12)||x||_2
   =Y^o(1) R^(1/6)||x||_2.                          (1.3)
```

Its cubed form is a normalized third-moment bound `D^(1/4)||x||_2^3`.
By Holder, (1.3) for three coefficient vectors gives

```text
|int X_x X_y X_z psi|
 <<Y^o(1) D^(1/4)||x||_2||y||_2||z||_2.             (1.4)
```

Thus (1.3) is a sufficient bypass for the desired trilinear estimate.  It
is stronger than the signed trilinear statement; no converse is being
asserted.

---

## 2. The critical block estimate is proved

Partition the node interval into ordinary integer intervals `I` of length
at most `R`, and write

```text
X_I(s)=sum_(n in S_Y cap I) x_n exp(i B s log(n/Y)). (2.1)
```

### Lemma 2.1 (one critical block)

Uniformly in `I` and in the coefficients,

```text
||X_I||_3 <<_(w,psi) R^(1/6)||x_I||_2.              (2.2)
```

### Proof

For distinct shell integers `m,n`, the mean-value theorem gives

```text
|B log(n/m)| >>_w (B/Y)|n-m|.                       (2.3)
```

Schwartz decay of `hat(psi)` and Schur's test therefore give

```text
||X_I||_2 <<_(w,psi)||x_I||_2,                      (2.4)
```

because `B/Y` tends to infinity.  There are at most `R+1` integers in
`I`, so Cauchy gives

```text
||X_I||_infinity <=sqrt(R+1)||x_I||_2.              (2.5)
```

Finally,

```text
||X_I||_3^3 <=||X_I||_infinity ||X_I||_2^2,         (2.6)
```

which proves (2.2).  This proof does not use primality.  QED

The exponent in (2.2) is sharp: a nearly arithmetic packet of `R` integer
nodes behaves like a normalized Dirichlet kernel.

---

## 3. The exact missing recombination theorem

Put

```text
S_x(s)=(sum_I |X_I(s)|^2)^(1/2).                    (3.1)
```

If one could prove the logarithmic-curvature reverse square function

```text
||sum_I X_I||_3 <<Y^o(1)||S_x||_3,                 (3.2)
```

then Lemma 2.1 would finish (1.3).  Indeed, Minkowski in `L^(3/2)` gives

```text
||S_x||_3^2
 =||sum_I |X_I|^2||_(3/2)
 <=sum_I ||X_I||_3^2
 <<R^(1/3)sum_I ||x_I||_2^2.                       (3.3)
```

Equivalently, introduce independent signs `epsilon_I`.  Khintchine gives

```text
E_epsilon ||sum_I epsilon_I X_I||_3^3
 asyp ||S_x||_3^3
 <<R^(1/2)||x||_2^3.                               (3.4)
```

The unresolved assertion is that the deterministic all-plus block sum is
no larger, up to `Y^o(1)`, than this randomized block average.  This is the
precise block-coherence obstruction.

At the scale `R`, the frequency map `lambda(n)=B log(n/Y)` obeys

```text
lambda'(n)R asyp sqrt(B),       |lambda''(n)|R^2 asyp 1. (3.5)
```

Thus `R` is exactly the transition where one block is approximately
linear but adjacent block centers feel order-one curvature.

### Why ordinary interval Littlewood--Paley theory does not close (3.2)

The reverse direction is false for arbitrary disjoint frequency
intervals.  On the circle take `f_j(t)=exp(ijt)`, `1<=j<=J`.  Then

```text
||(sum_j |f_j|^2)^(1/2)||_3=sqrt(J),                (3.6)
```

whereas the Dirichlet-kernel lower bound on `|t|<=c/J` gives

```text
||sum_j f_j||_3 >>J^(2/3).                          (3.7)
```

The missing factor is `J^(1/6)`.  Consequently frequency separation and
an arbitrary-interval square function alone cannot prove (3.2); one must
use the specific logarithmic curvature and the actual integration scale.

---

## 4. The sharp revival lower bound

The half-integer construction in
`ZETA23-QP-WEIGHTED-NEAR-DETERMINANT-LITERATURE-AUDIT-2026-08-15.md`
chooses, along arbitrarily large centers, normalized coefficients on the
primes in a one-sided node interval of length `R`.  It proves

```text
int |X_x|^3 psi ds
 >> sqrt(R)/(log Y)^(3/2)
  = D^(1/4)/(log Y)^(3/2).                          (4.1)
```

Equivalently,

```text
||X_x||_3 >>D^(1/12)/(log Y)^(1/2).                 (4.2)
```

Therefore (1.3), if true, is power-sharp.  The known revival is not a
counterexample.

---

## 5. Why the immediate `L2`--`L4` interpolation fails

The estimate

```text
||X||_3 <=||X||_2^(1/3)||X||_4^(2/3)               (5.1)
```

would require the normalized fourth moment

```text
||X||_4^4 <<D^(1/2+o(1))||x||_2^4.                 (5.2)
```

But (5.2) is false for arbitrary coefficients.  The fixed shell contains
`K asyp Y/log Y` primes.  Choose coefficients of modulus `K^(-1/2)` whose
phases make all summands align at one interior time.  They remain in a
fixed arc on a time interval of length `asymp_w 1`, and the normalized
measure of that interval is `asymp 1/B`.  Hence

```text
||X||_4^4 >>K^2/B asyp D/(log Y)^2,                 (5.3)
```

which exceeds (5.2) by a fixed power.

This one isolated global peak does not refute the third-moment target: its
third-moment contribution is only

```text
K^(3/2)/B=Y^(-1/66+o(1)),                           (5.4)
```

far below `D^(1/4)=Y^(4/33)`.  A proof of (1.3) must therefore be genuinely
`L3` or use a truncated fourth-moment/large-values argument; plain
interpolation loses the needed power.

---

## 6. Binary ledger

```text
critical one-block L3 bound D^(1/12):               PROVED;
ordinary reverse interval square function:          FALSE;
log-curvature reverse square function (3.2):        OPEN;
global arbitrary-coefficient L3 target (1.3):       OPEN;
half-integer packet counterexample to (1.3):         NO (it saturates);
plain L2--L4 proof of (1.3):                         IMPOSSIBLE;
four-cycle bound / QP / strip from this route:       NOT PROVED.
```
