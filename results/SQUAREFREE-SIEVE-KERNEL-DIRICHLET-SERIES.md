# Dirichlet series of the squarefree reciprocity sieve kernel

Status: **an exact Euler-product factorization and pole residue are derived for
the squarefree primitive-even character kernel. This is unconditional
character algebra. Its placement inside a complete long-mollifier reciprocity
formula and the required uniform contour estimate remain open. No zero-free
strip or RH proof is claimed.**

Date: 2026-08-09.

This note continues
[`SQUAREFREE-RECIPROCITY-SIEVE-KERNEL.md`](SQUAREFREE-RECIPROCITY-SIEVE-KERNEL.md).
It evaluates the modulus Dirichlet series suggested by the two local branches
of the primitive-even character sum.

## 1. One-branch coefficients

Fix an integer `a` and a sign `epsilon` in `{+1,-1}`. For an odd prime `p`, put

```text
c_p^epsilon(a)=0,                         if p|a,
                1/(p-1)-1_(a==epsilon mod p), otherwise. (1.1)
```

For an odd squarefree integer `d`, define

```text
c_d^epsilon(a)=product_(p|d)c_p^epsilon(a).              (1.2)
```

The two-branch primitive-even kernel is

```text
c_d^even(a)=[c_d^+(a)+c_d^-(a)]/2.                       (1.3)
```

By the exact character calculation in the preceding note,

```text
c_d^even(a)
 =mu(d)/phi(d)
  sum_(chi mod d, primitive, chi(-1)=1)chi(a).           (1.4)
```

## 2. Euler product

For `Re z>0`, define

```text
F_a^epsilon(z)
 =sum_(d odd squarefree)c_d^epsilon(a)d^(-z)
 =product_(p odd)[1+c_p^epsilon(a)p^(-z)].               (2.1)
```

The universal local factor is

```text
B_p(z)=1+p^(-z)/(p-1).                                  (2.2)
```

Remove the zeta factor by writing

```text
h_p(z)=B_p(z)[1-p^(-1-z)].                              (2.3)
```

A direct expansion gives

```text
h_p(z)-1
 =p^(-z)/[p(p-1)]-p^(-1-2z)/(p-1).                     (2.4)
```

Therefore

```text
H(z)=product_(p odd)h_p(z)                              (2.5)
```

converges absolutely and locally uniformly in

```text
Re z>-1/2.                                               (2.6)
```

For `a` and `a-epsilon` both nonzero, the exact factorization is

```text
F_a^epsilon(z)
 =zeta(1+z)[1-2^(-1-z)]H(z) C_a^epsilon(z),              (2.7)
```

where the finite correction is

```text
C_a^epsilon(z)
 =product_(p|a, p odd) B_p(z)^(-1)

  *product_(p|(a-epsilon), p odd)
   [1-(p-2)p^(-z)/(p-1)]/B_p(z).                        (2.8)
```

The two prime sets in (2.8) are disjoint. In the half-plane (2.6), the
denominators in (2.8) are nonzero because

```text
|p^(-z)/(p-1)|<1                                        (2.9)
```

for every odd prime when `Re z>-1/2`.

If `a=0` or `a=epsilon`, infinitely many local factors are changed and the
zeta pole discussed below is removed; these special cases must be handled
separately.

## 3. Exact residue at z=0

At zero,

```text
h_p(0)= [p/(p-1)][1-1/p]=1.                             (3.1)
```

Thus `H(0)=1`, while the odd-prime zeta factor has residue `1/2`. The finite
corrections satisfy

```text
B_p(0)^(-1)=(p-1)/p,                                    (3.2)

[1-(p-2)/(p-1)]/B_p(0)=1/p.                             (3.3)
```

Consequently

```text
Res_(z=0) F_a^epsilon(z)

=1/2 product_(p|a, p odd)(1-1/p)
    product_(p|(a-epsilon), p odd)1/p.                  (3.4)
```

For the primitive-even average,

```text
Res_(z=0) F_a^even(z)
 =[Res F_a^+(z)+Res F_a^-(z)]/2.                         (3.5)
```

The residue is explicit, nonnegative, and carries reciprocal-radical
suppression from both `a-1` and `a+1`.

## 4. Logarithmic terminal taper

The modulus weight in the standard mollifier is

```text
W_y(d)=1_(d<=y) log(y/d)/log y.                          (4.1)
```

Formally, Perron inversion gives

```text
sum_d c_d^even(a)W_y(d)

=1/log y * 1/(2 pi i)
 integral F_a^even(z)y^z dz/z^2.                         (4.2)
```

If

```text
F_a^even(z)=C_a/z+D_a+O(z),                              (4.3)
```

then the pole contribution to (4.2) is

```text
(C_a/2)log y+D_a.                                       (4.4)
```

The exact leading coefficient is therefore

```text
1/4 * [
  1/2 product_(p|a)(1-1/p)product_(p|a-1)1/p
 +1/2 product_(p|a)(1-1/p)product_(p|a+1)1/p
],                                                       (4.5)
```

with products restricted to odd primes and the special cases from Section 2
removed appropriately. The implementation computes the equivalent rational
formula directly.

## 5. Why this is potentially useful

The raw primitive-character family has size comparable to the modulus. After
the Moebius outer weight and character orthogonality are combined, the modulus
Dirichlet series has only:

1. one explicit zeta pole at `z=0`;
2. a universal Euler product analytic to `Re z>-1/2`;
3. finite local corrections determined by `a`, `a-1`, and `a+1`.

This is a genuine compression of the modulus family. It suggests that a
Mellin-separated general-squarefree reciprocity formula could evaluate the
entire modulus sum before applying Cauchy or a large sieve.

## 6. The remaining uniformity problem

The continuation to `Re z>-1/2` is not automatically a square-root saving
uniformly in `a`. On the line `Re z=-eta`, a correction at a prime dividing
`a-epsilon` can have size about

```text
p^eta.                                                    (6.1)
```

Hence the finite correction may cost

```text
rad_odd(a-epsilon)^eta.                                  (6.2)
```

A contour shift by `eta` gains `y^(-eta)` but can lose the factor (6.2). In
the dual approximate functional equation, `a` is a product such as `re`, so
this dependence must be combined with the coefficient `1/sqrt(re)` and the
AFE support before a net gain is asserted.

The smallest rigorous next theorem is therefore a **uniform tapered kernel
estimate** of the form

```text
sum_d c_d^even(a)W_y(d)
 =(C_a/2)log y+D_a
  +O_epsilon(y^(-eta)(1+|a|)^(eta+epsilon)),             (6.3)
```

for one explicit `eta>0`, with a correspondingly explicit bound for `D_a`.
Equation (6.3) is a target, not a theorem claimed in this note.

After (6.3), the exponent ledger must be run against the ranges of the dual
AFE indices. A useful result requires the coefficient weights to absorb the
`a`-dependence without recreating the theta=1 barrier.

## 7. Reproducibility

The finite local and residue identities are implemented in

```text
src/squarefree_kernel_dirichlet_series.py
src/test_squarefree_kernel_dirichlet_series.py.
```

The tests verify:

- the exact local correction factorization;
- the finite Euler product as partial zeta factor times the analytic product
  and finite corrections;
- `h_p(0)=1`;
- the rational residue formula (3.4);
- the leading logarithmic-taper coefficient from (4.4).

The tests do not prove the uniform contour estimate (6.3) or a complete
integer-twist reciprocity formula.
