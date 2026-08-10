# Squarefree primitive-even sieve kernel for the reciprocity route

Status: **the character-orthogonality and local Euler-product identities are
proved exactly and tested by direct character enumeration. Their insertion
into a general integer-twist zeta reciprocity formula remains conditional on
deriving that formula with all local factors. No zero-free strip or RH proof is
claimed.**

Date: 2026-08-09.

This note extends
[`LONG-MOLLIFIER-PRIME-RECIPROCITY-STRESS.md`](LONG-MOLLIFIER-PRIME-RECIPROCITY-STRESS.md)
from prime moduli to the odd squarefree moduli selected by the Moebius
mollifier.

## 1. Primitive character sum for squarefree modulus

Let `d` be odd and squarefree. Extend every Dirichlet character by zero on
nonunits. For `(a,d)=1`, primitive characters modulo `d` are tensor products
of nonprincipal characters at every prime dividing `d`. Hence

```text
S_d(a):=sum_(chi mod d, primitive) chi(a)
      =product_(p|d)[(p-1)1_(a==1 mod p)-1].             (1.1)
```

If `(a,d)>1`, then `S_d(a)=0`.

Projection onto even characters gives

```text
S_d^+(a)
 :=sum_(chi primitive, chi(-1)=1)chi(a)
  =[S_d(a)+S_d(-a)]/2.                                  (1.2)
```

Equivalently, by conductor Moebius inversion,

```text
S_d(a)=sum_(c|(d,a-1)) phi(c)mu(d/c).                    (1.3)
```

Equations (1.1)--(1.3) are unconditional finite character orthogonality.

## 2. Moebius-weighted local product

The outer coefficient expected after a squarefree reciprocity transform is
`mu(d)/phi(d)`. Multiplying (1.2) by this coefficient yields the exact two-
branch product

```text
mu(d)/phi(d) S_d^+(a)

=1/2 product_(p|d)
   [1/(p-1)-1_(a==1 mod p)]

 +1/2 product_(p|d)
   [1/(p-1)-1_(a==-1 mod p)],                            (2.1)
```

provided `(a,d)=1`; both sides vanish otherwise.

Thus the squarefree modulus sum is a signed sieve kernel for the two shifted
integers `a-1` and `a+1`. It is not an unstructured character-family count.

## 3. Complete local Euler product

Ignore the terminal size cutoff for one moment and sum each squarefree local
factor independently over odd primes up to `P`. For one sign `epsilon` in
`{+1,-1}`, define

```text
c_p^epsilon(a)=0,                         if p|a,
                1/(p-1)-1_(a==epsilon mod p), otherwise.
```

Then exactly

```text
product_(3<=p<=P)[1+c_p^epsilon(a)]

=product_(3<=p<=P, p not divide a) p/(p-1)
 *product_(3<=p<=P, p|(a-epsilon)) 1/p.                  (3.1)
```

The first factor is a Mertens-type baseline. The second is a reciprocal
radical suppression factor from the small prime divisors of `a-epsilon`.

Formula (3.1) is the useful structural output:

- if `a-epsilon` contains many small prime factors, the branch is strongly
  suppressed;
- if it has none, the branch retains only a logarithmic Mertens-size baseline;
- no power of the modulus range appears in the fully factorized local model.

The actual mollifier uses `d<=y` and a logarithmic terminal taper, so the
squarefree sum is not literally the unrestricted product (3.1). A Mellin or
Perron treatment of the terminal cutoff is required before using (3.1) in an
analytic estimate.

## 4. Placement in the dual approximate functional equation

The prime stress test showed that the dual q-sum becomes a one-sided
character mollifier. In a general squarefree extension, opening the dual
`L`-square should produce a coefficient `a=re` inside the primitive character
sum. Character orthogonality would then replace the modulus family by

```text
mu(d)/phi(d) S_d^+(re),                                  (4.1)
```

and (2.1) would convert it into the two sieve branches for

```text
re-1,   re+1.                                            (4.2)
```

This is conditional only in its placement inside the unproved general-
integer reciprocity formula. The character identity itself is exact.

The resulting analytic target is no longer a generic large-sieve norm. It is
a shifted-product sum with reciprocal-radical weights, terminal smoothing,
and Moebius coefficients:

```text
sum_(r,e) tau(r)mu(e)/sqrt(re)
  V(r,d,T) W_y(e)
  [sieve_y(re-1)+sieve_y(re+1)].                         (4.3)
```

All common-factor, imprimitive, parity, gamma, and dual-AFE terms must be
retained in the actual formula.

## 5. Potential leverage and immediate danger

The leverage is that summing the primitive character family first removes the
raw family-size factor and exposes a centered multiplicative sieve kernel.
The local completion has only logarithmic baseline growth and exact radical
suppression.

The danger is that the AFE weight depends on the same modulus being summed.
One cannot replace the truncated squarefree modulus sum by the complete Euler
product before separating that dependence. Applying Cauchy or an absolute
large sieve too early recreates the `theta=1` barrier recorded in the prime
stress test.

The next rigorous task is therefore:

> derive a Mellin-separated general-squarefree reciprocity formula in which
> the modulus dependence of the dual AFE weight is represented by a complex
> power `d^{-z}`. Then evaluate the squarefree character kernel as an Euler
> product for `Re z>0`, continue it to the contour actually needed, and keep
> the terminal cutoff error signed.

A useful outcome would be a factorization of the form

```text
sum_(d odd squarefree)
  mu(d)S_d^+(a)/phi(d) d^{-z}
 =zeta(1+z) H_a^+(z)+zeta(1+z) H_a^-(z),                 (5.1)
```

where the `H_a` factors carry explicit local suppression from `a-1` and
`a+1` and are uniformly controlled on a right half-plane. Equation (5.1) is a
research target, not a theorem claimed here.

## 6. Reproducibility

The exact finite identities are implemented in

```text
src/squarefree_even_character_kernel.py
src/test_squarefree_even_character_kernel.py.
```

The tests verify:

1. primitive-even sums by direct enumeration of local primitive-character
   tuples for moduli through `105`;
2. equality of the Moebius-weighted character sum and the two local products;
3. the reciprocal-radical Euler-product factorization (3.1);
4. exact rational truncated squarefree kernel values.

These tests are finite algebra only. They do not establish a general-
integer zeta reciprocity formula or the long-mollifier moment bound.
