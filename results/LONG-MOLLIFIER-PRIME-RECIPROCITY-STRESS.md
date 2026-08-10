# Prime-twist reciprocity stress test for the long-mollifier strip route

Status: **exact prime-character factorization and centered-progression kernel
proved and regression-tested; the published pointwise reciprocity error returns
the theta=1 barrier under absolute summation. No zero-free strip or RH proof is
claimed.**

Date: 2026-08-09.

This note continues
[`LONG-MOLLIFIER-TWISTED-MOMENT-REDUCTION.md`](LONG-MOLLIFIER-TWISTED-MOMENT-REDUCTION.md).
It asks whether Khan's reciprocity formula supplies genuinely new
orthogonality after the two mollifier sums are inserted before absolute
values.

The answer is mixed:

1. the dual q-sum really does become a one-sided Dirichlet-character
   mollifier;
2. primitive-even character orthogonality turns that mollifier into a
   centered pair of residue classes;
3. however, summing the published pointwise error by absolute values gives
   exactly the old theta=1 length barrier.

Thus reciprocity remains viable only in a signed or exact aggregate form.

## 1. Prime-twist model

For a fixed terminal scale y, write

```text
w_y(n)=1_(n<=y) log(y/n)/log y,

a_y(n)=mu(n)w_y(n)/sqrt(n).
```

The prime-prime sector of the mollified second moment is

```text
sum_(p,q<=y, p,q odd primes) a_y(p)a_y(q) J_T(p,q),      (1.1)
```

where

```text
J_T(p,q)=integral_R (p/q)^(it)
 |zeta(1/2+it)|^2 exp(-t^2/T^2)dt.                       (1.2)
```

Khan's theorem gives, for distinct odd primes p,q, a main term plus a dual
term of the shape

```text
(T/(2 pi))^(1/2) sqrt(p)/(p-1)
 sum_(chi mod p, primitive even) chi(q)
 integral_R Gamma((1-2it)/4)(T/(2q))^(it)
 |L(1/2+it,chi)|^2dt,                                   (1.3)
```

and an error

```text
O_epsilon((pqT)^epsilon[sqrt(q/p)+sqrt(p/q)]).           (1.4)
```

The gamma factor makes the dual t-integral effectively bounded in length, but
this does not by itself control the modulus sum.

## 2. Exact one-sided character-mollifier factorization

For distinct primes, mu(p)=mu(q)=-1. Multiplying the coefficient in (1.3) by
`a_y(p)a_y(q)` gives exactly

```text
[-w_y(p)/(p-1)]
 [-w_y(q)chi(q)q^(-1/2-it)]
 (T/2)^(it).                                             (2.1)
```

Therefore the complete q-sum in the prime sector is

```text
M_y^prime(1/2+it,chi)
 =sum_(q<=y, q odd prime, q!=p)
   mu(q)w_y(q)chi(q)q^(-1/2-it).                         (2.2)
```

The dual object is not a family of unmollified L-moments. It is a one-sided
mollified character family:

```text
T^(1/2) sum_(p<=y) mu(p)w_y(p)/(p-1)
 sum_(chi mod p, primitive even)
 integral Gamma(...) (T/2)^(it)
 |L(1/2+it,chi)|^2 M_y^prime(1/2+it,chi)dt.              (2.3)
```

A general-squarefree reciprocity formula should produce the full character
mollifier, together with local coprimality and imprimitive corrections. Those
corrections must be derived rather than guessed.

## 3. Exact primitive-even orthogonality

Let p be an odd prime and extend characters by zero to multiples of p. Every
nonprincipal character modulo p is primitive. For any integer a,

```text
1/(p-1) sum_(chi mod p, primitive, chi(-1)=1) chi(a)
 =0,                                  if p divides a,
 =1/2 1_(a == 1 mod p)
  +1/2 1_(a == -1 mod p)
  -1/(p-1),                           otherwise.         (3.1)
```

Indeed the projection onto even characters is

```text
1/2 sum_chi [chi(a)+chi(-a)],                            (3.2)
```

and subtracting the principal character gives (3.1).

Consequently, for any finite coefficient sequence b(e),

```text
1/(p-1) sum_(chi primitive even) chi(r)
  sum_e b(e)chi(e)

=1/2 sum_(re == 1 mod p) b(e)
 +1/2 sum_(re == -1 mod p) b(e)
 -1/(p-1) sum_(p not divide re) b(e).                    (3.3)
```

Thus character orthogonality produces a **centered progression discrepancy**.
The two exceptional residue classes and their uniform baseline must remain
together.

For the mollifier sequence, the right side of (3.3) is a centered Moebius sum
in the two classes

```text
e == +/- r^(-1) mod p.                                  (3.4)
```

This is the first genuinely new arithmetic coordinate supplied by
reciprocity.

## 4. What happens after opening the dual L-square

A smoothed approximate functional equation for

```text
|L(1/2+it,chi)|^2
```

has coefficients indexed at conductor scale p. Inserting (2.2) and applying
(3.3) turns the dual family schematically into

```text
sum_(p<=y) mu(p)w_y(p)
 sum_r tau(r)/sqrt(r) V(r/p)
 [
   1/2 sum_(e<=y, re == +/-1 mod p)
      mu(e)w_y(e)/sqrt(e)
   -1/(p-1) sum_((e,p)=1)
      mu(e)w_y(e)/sqrt(e)
 ].                                                       (4.1)
```

The exact gamma, parity, dual-AFE, and local factors are suppressed in (4.1)
and must be frozen before an analytic estimate is claimed.

Formula (4.1) shows what would be needed:

> a power-saving dispersion estimate for centered Moebius progression sums,
> averaged jointly over the modulus p and the AFE index r, with the terminal
> cutoff retained.

A twist-by-twist estimate or an uncentered sector bound destroys the only new
cancellation.

## 5. Published reciprocity error returns the theta=1 barrier

The pointwise error (1.4), multiplied by the two prime mollifier coefficients,
has absolute majorant

```text
w_y(p)w_y(q)[1/p+1/q] T^epsilon.                         (5.1)
```

For any nonnegative weights w_p, there is the exact finite identity

```text
sum_(p,q) w_p w_q(1/p+1/q)
 =2 [sum_p w_p][sum_p w_p/p].                            (5.2)
```

With logarithmic taper weights over primes up to y, the right side is

```text
y^(1+o(1)).                                              (5.3)
```

Therefore absolute summation of the published pointwise error gives, for one
mollifier length y,

```text
Error_y^abs <= y^(1+o(1)),                               (5.4)
```

and after integrating `1<=y<=Y`,

```text
integral_1^Y Error_y^abs dy <= Y^(2+o(1)).               (5.5)
```

The long-mollifier strip target is `T Y T^epsilon`. For `Y=T^theta`, comparing
(5.5) with that target requires

```text
theta<=1+o(1).                                           (5.6)
```

This is a limitation of the **pointwise-error plus triangle-inequality
method**, not a lower bound for the true signed error. To cross theta=1 one
must do at least one of the following:

1. obtain an exact reciprocity identity suitable for the complete integer
   twists;
2. retain and sum the signed transform error before absolute values;
3. prove cancellation in the Moebius-weighted error aggregate.

## 6. Symmetry supplies no contraction by itself

The original kernel in `(p,q)` is symmetric. Khan's corollary explains that
the dual moments transform compatibly under `p<->q`. Therefore reciprocity of
the exchange alone controls an antisymmetric difference, while the positive
mollified quadratic form sees the symmetric component.

For a symmetric finite weight `W(p,q)`,

```text
sum_(p,q) W(p,q)R(p,q)
 =sum_(p,q) W(p,q)[R(p,q)+R(q,p)]/2.                     (6.1)
```

The antisymmetric part cancels identically. A power gain must come from a
bound on the symmetric dual aggregate, not merely from the fact that it is
reciprocal.

## 7. Current smallest viable theorem

Choose one fixed smooth time weight and derive a general-squarefree version of
Khan's transform before inserting any absolute values. Then prove, for some
fixed theta>1 and `Y=T^theta`, that the combined dual family and signed
transform error satisfy

```text
integral_1^Y |
  Dual_y(T)+SignedTransformError_y(T)
| dy
 << T Y T^epsilon.                                      (7.1)
```

The expression inside (7.1) must retain:

- the full logarithmic mollifier, not only primes;
- the centered residue-class baseline;
- imprimitive-character and common-factor corrections;
- both sides of the approximate functional equation;
- the exact y-cutoff kernel.

Generic large-sieve Cauchy bounds are expected to return approximately
`T^(1/2)y` before the y-average and do not by themselves reach (7.1) for
arbitrary theta>1. The sought gain must be coefficient-specific.

## 8. Reproducibility

The exact finite prime-model identities are implemented in

```text
src/prime_reciprocity_sieve_kernel.py
src/test_prime_reciprocity_sieve_kernel.py.
```

The tests verify:

1. (3.1) by direct enumeration of all primitive even characters for small
   odd primes;
2. the centered progression identity (3.3) for rational coefficient data;
3. the factorization (2.1) for complex phases;
4. the exact error-majorant identity (5.2).

All tests are finite algebra. They do not certify the analytic continuation,
weight transforms, or error terms in a general integer-twist reciprocity
formula.

## 9. Primary source

- R. Khan, *A reciprocity relation for the twisted second moment of the
  Riemann Zeta function*, arXiv:2401.01057. Theorem 1 is stated for distinct
  odd prime twists. The paper notes that the proof extends to general integer
  twists with more complicated primitive-character orthogonality.
