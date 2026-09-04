# QP weighted near-determinant gate: primary-source audit and an absolute-L3 no-go

**Date:** 2026-08-15  
**Verdict:** none of the surveyed primary incidence, Kloosterman, modular-root,
or multiplicative-energy theorems gives a fixed-power saving for the actual
weighted rank-one form

```text
T_q(y)=sum_(n,m,l in S_Y) y_n y_m y_l
       W((2nm-q l)/H),                             (0.1)
q=2Y=2N+1,       H=Y^2/B,       B=Y^A.             (0.2)
```

Here `S_Y` is the actual prime-power shell, `y` is an arbitrary real
coefficient vector, and `W` is a fixed short-window majorant or smooth
kernel.  The missing estimate remains

```text
|T_q(y)| << H^(1/2) Y^(-eta+o(1)) ||y||_2^3       (0.3)
```

for some fixed `eta>0`, uniformly for **every** odd `q` in the relevant
range.  Existing results lose at least one indispensable feature:

1. they require a prime modulus or average over moduli;
2. they allow only two separated arbitrary coefficient slots;
3. they require a curved monomial, whereas the quotient coordinate is
   linear; or
4. they estimate unweighted exact set energy rather than the signed
   rank-one tensor (0.1).

There is also a rigorous negative result for a tempting bypass.  The bound

```text
int_0^B |sum_(n in S_Y) a_n (n/Y)^(it)|^3 dt
 << (B+Y^(3/2+o(1))) ||a||_2^3                     (0.4)
```

is false for arbitrary coefficients on the **actual primes**, along a
sequence of half-integer centers.  At `A=50/33` there are normalized
coefficient vectors for which the left side is

```text
>> B Y^(4/33)/(log Y)^(3/2).                       (0.5)
```

This refutes an absolute-`L3` shortcut.  It does not lower-bound the signed
cubic moment: cancellation away from the revival neighborhoods can remain,
and the exact signed expansion is again (0.1).

No exponent below `49/66`, no QP theorem, and no strip theorem is proved
here.

---

## 1. The exact operator which needs a saving

Put

```text
Y=N+1/2,       q=2Y,       H=Y^(2-A),       1<A<2. (1.1)
```

The mixed term in the signed cubic expansion is supported where

```text
|2nm-q l| << H,                  n,m,l asyp Y.      (1.2)
```

For each ordered pair `(n,m)`, (1.2) permits at most one integer `l`.
For fixed `l`, the product `nm` lies in an interval of length `O(H)`.
The bounded representation multiplicity of products of two shell prime
powers and Schur's test therefore give

```text
|T_q(y)| << H^(1/2)||y||_2^3.                      (1.3)
```

At the active aperture

```text
A=50/33,       H=Y^(16/33),
H^(1/2)=Y^(8/33),
1/2+8/33=49/66.                                    (1.4)
```

Thus a useful imported theorem must improve (1.3) for arbitrary `y`, not
merely count unweighted triples or average the center.  It must also keep
the actual quotient weight

```text
y_l = y_((2nm-r)/q),                 |r|<<H.        (1.5)
```

Dropping (1.5) changes the problem.

---

## 2. Bettin--Chandee: a numerically strong but inapplicable theorem

Theorem 1 of Bettin--Chandee estimates

```text
sum_(a~A0,m~M,n~N,(m,n)=1)
 alpha_m beta_n nu_a e(theta a mbar/n)              (2.1)
```

for three arbitrary separated sequences.  In the balanced case `M~N~Y`,
`A0~H`, its displayed bound would formally save

```text
min(H^(3/20)Y^(1/20),Y^(1/8)).                     (2.2)
```

At `H=Y^(16/33)`, the first term wins and the formal saving is

```text
(3*(16/33)+1)/20=27/220.                           (2.3)
```

If (2.1) actually represented (0.1), it would change `49/66` to

```text
49/66-27/220=409/660.                              (2.4)
```

Equation (2.4) is **not an achieved exponent**.  The mapping fails exactly
at (1.5).  Detecting

```text
2nm == r (mod q)                                   (2.5)
```

can generate a reciprocal phase, but the third actual coefficient becomes
`y_((2nm-r)/q)`, a joint function of all three summation variables.  It is
not any of the separated factors `alpha_m beta_n nu_r` in (2.1).

Their Corollary 1 makes the mismatch equally transparent.  It treats

```text
m1*n2-m2*n1=Delta                                  (2.6)
```

with arbitrary sequences only on `n1,n2`; the one-variable weights on
`m1,m2` must be smooth on dyadic intervals.  Under

```text
(m1,n2,m2,n1)=(2n,m,q,l),                          (2.7)
```

there are three arbitrary actual weights `y_n,y_m,y_l` but only two
arbitrary slots.  Permuting the entries cannot change that count.  If the
singleton `q` is put in a smooth slot, a unit-scale cutoff at dyadic size
`q` also forces the derivative parameter in their corollary to be
`eta asyp q`, destroying the stated error saving.

Hence (2.3) is only a useful measurement of what a new theorem with one
joint quotient slot could deliver.

---

## 3. Deshouillers--Iwaniec: smooth Kloosterman averages do not absorb the quotient weight

The primary paper's Theorems 8 and 9 estimate bilinear sequences `a_m b_n`
against Kloosterman sums, with a smooth weight in the modulus and the
archimedean variables.  Theorem 10 allows `a_m` and a joint sequence
`b_(n,r,s)`, but the remaining factor is still a smooth function and the
Kloosterman kernel is averaged over moduli of the form `sc`; see formulas
(1.42)--(1.56) on journal pages 234--236.

After (2.5), the target coefficient is instead

```text
y_n y_m y_((2nm-r)/q).                             (3.1)
```

Whichever variable is singled out as `a_m`, the other two actual weights
and the residual are not a function of the allowed complementary indices:
one factor still depends jointly on both sides of the bilinear split.  No
smooth partition removes this dependence for arbitrary `y`.  Completing
the congruence first does not help; it produces arbitrary samples of the
quotient sequence, not a smooth modulus weight.

The Deshouillers--Iwaniec theorem is therefore not an estimate for (0.1).
In particular, its cancellation in smooth averages of Kloosterman sums
cannot be quoted as a fixed-`q`, three-weight rank-one saving.

---

## 4. Robert--Sargos: the necessary specialization has zero curvature

Robert--Sargos Theorem 1 concerns

```text
sum_(h~H0,n~N0) a(h,n) sum_(m~M0) b(m)
 e(X h^beta n^gamma m^alpha /
   (H0^beta N0^gamma M0^alpha)),                   (4.1)
```

with arbitrary bounded coefficients, but with the explicit hypothesis

```text
alpha(alpha-1) beta gamma != 0.                    (4.2)
```

Its proof uses curvature in `m`.  Their Theorem 2 likewise counts the
four-variable spacing relation for `m^alpha` with `alpha != 0,1`.

Fourier inversion of (1.2) gives a phase bilinear in `n,m` and linear in
`l`.  Trying to put the quotient variable into (4.1) requires
`alpha=1`, for which

```text
alpha(alpha-1)=0.                                  (4.3)
```

This is exactly outside the theorem.  Eliminating `l` instead creates the
discontinuous nearest quotient and the arbitrary sample (1.5), neither of
which is a curved monomial phase.  The Robert--Sargos spacing theorem thus
supplies no exponent for (0.1).

---

## 5. Shkredov modular hyperbolas and Kloosterman forms

Shkredov works over `F_p` with `p` an odd prime.

* Theorem 4 gives a fixed power saving for bilinear Kloosterman forms when
  one shifted-interval support has length at most `p^(1-c)` for a fixed
  `c>0`.  The prime-power shell occupies an ambient interval of length
  `asyp p`; its cardinality `p/log p=p^(1-o(1))` does not provide a fixed
  `c` in this support-length hypothesis.
* Theorem 32 assumes the structured interval parameter `N<=p^tau` with
  `tau<1/8`.  The residual set here has length
  `H=p^(16/33)`, far beyond that range, and its equation is not the
  four-shift fixed-hyperbola incidence in that theorem.
* Theorems 33 and 34 estimate bilinear Kloosterman kernels.  Their power
  saving requires either a short/structured factor with controlled Wiener
  norm or parameter inequalities not furnished by arbitrary weights on the
  full shell.  The quotient sample (1.5) is still not a bilinear factor.

There is a second, uniformity-level failure: `q=2N+1` ranges over every odd
integer.  It need not be prime.  A theorem for prime `p`, or for almost all
prime moduli, cannot prove the all-center QP assertion.

---

## 6. Modular-root and variety energy results

Kerr--Shkredov--Shparlinski--Zaharescu Theorems 1.1 and 1.2 estimate the
unweighted exact additive energies of modular square roots of a short
interval, for prime `q`.  Theorem 1.3 is an average over prime moduli.  The
authors explicitly note after Theorem 1.4 that a general weighted energy
could be inserted only "in principle" and do not state or prove that
weighted theorem.  None of these results contains the quotient weight
(1.5) or an all-composite-modulus uniform estimate.

Shkredov's *On multiplicative energy of subsets of varieties* proves an
unweighted estimate for a set `A` lying in a fixed subvariety of a finite
algebraic group; its basic energy is

```text
#{(a,b,c,d) in A^4: ab^(-1)=cd^(-1)}.              (6.1)
```

The target (0.1) is instead a signed weighted form over a union of `O(H)`
translated near-product relations, with an archimedean quotient and an
arbitrary odd modulus.  Treating the union as one variety loses the
fixed-degree hypothesis, and (6.1) has no three-slot rank-one conclusion.

Thus neither modular-root energy nor multiplicative energy of varieties
proves (0.3).

---

## 7. A rigorous counterexample to the absolute third-moment shortcut

### Proposition 7.1

Fix `4/3<A<2`.  There are arbitrarily large half-integers `Y` and
coefficient vectors supported on primes in the fixed shell, with
`||a||_2=1`, such that, for `B=Y^A`,

```text
int_0^B |P_Y(t)|^3 dt
 >>_A B Y^(1/2-A/4)/(log Y)^(3/2),                 (7.1)
P_Y(t)=sum_p a_p (p/Y)^(it).                       (7.2)
```

Consequently (0.4) is false.  At `A=50/33`, (7.1) is (0.5).

### Proof

Let `X` be large and set

```text
L=c X^(1-A/2),                                     (7.3)
```

where `c>0` is a sufficiently small fixed constant.  Average the prime
count

```text
K(Y)=#{p prime:Y<p<=Y+L}                           (7.4)
```

over half-integers `Y` in `[X,2X]`.  Every prime in
`[X+L,2X]` belongs to `L+O(1)` such windows.  The prime number theorem
(indeed, standard Chebyshev lower bounds suffice after restricting the
range) gives

```text
sum_Y K(Y) >> L X/log X.                           (7.5)
```

Hence some half-integer `Y` has

```text
K:=K(Y) >> L/log Y.                                (7.6)
```

For large `Y`, these primes lie in the fixed multiplicative shell.  Put
`a_p=K^(-1/2)` on them.

Consider the revival times

```text
t_j=4 pi j Y,       1<=j<=c_1 B/Y.                (7.7)
```

Write `p=Y+x`, so `x` is a half-integer.  The linear Taylor phase aligns
**exactly**:

```text
t_j x/Y = 4 pi j x = 2 pi j(2x) in 2 pi Z.        (7.8)
```

Moreover,

```text
t_j |log(1+x/Y)-x/Y|
 << B L^2/Y^2 <<_A c^2.                            (7.9)
```

If `|s|<=c_2Y/L`, then also

```text
|s log(1+x/Y)|<<c_2.                               (7.10)
```

Choosing `c,c_1,c_2` small, (7.8)--(7.10) put every summand in a fixed
arc about `1`.  Therefore

```text
|P_Y(t_j+s)| >> sqrt(K)                            (7.11)
```

throughout each such interval.  The intervals are disjoint, their number
is `asyp B/Y`, and each has length `asyp Y/L`; their total measure is
`asyp B/L`.  Thus

```text
int_0^B |P_Y(t)|^3dt
 >> (B/L)K^(3/2)
 >> B sqrt(L)/(log Y)^(3/2)
 >> B Y^(1/2-A/4)/(log Y)^(3/2).                  (7.12)
```

For `A>4/3`, (7.12) exceeds
`B+Y^(3/2+o(1))` by a fixed power along these centers.  This proves the
proposition.  QED

The same construction works against a smooth normalized measure which is
bounded below on a fixed interior subinterval: after division by `B`, its
absolute third moment is

```text
>> sqrt(L)/(log Y)^(3/2).                          (7.13)
```

### Signed-moment warning

Equations (7.11)--(7.13) do **not** imply a lower bound for

```text
int (Re P_Y(t))^3 rho_B(t)dt.                      (7.14)
```

The complement of the revival intervals may cancel their signed
contribution.  Replacing all coefficients by their negatives only negates
the whole quantity (7.14); it does not remove that cancellation.  Expanding
(7.14) exactly returns the signed near-determinant tensor (0.1).

---

## 8. The precise open theorem suggested by the audit

The especially attractive target is

```text
|T_q(y)| << H^(1/4+o(1))||y||_2^3.                (8.1)
```

At `A=50/33`, (8.1) would give standardized skew exponent `4/33` and
the transverse exponent

```text
1/2+4/33=41/66.                                    (8.2)
```

This quarter-power is not supplied by any source above.  Combinatorially,
the relation (1.2) is a partial multiplication table: every two coordinates
determine at most one third coordinate, while a one-coordinate fibre has
size `O(H)`.  General partial Latin tables can saturate the Schur norm
`H^(1/2)`.  Proving (8.1) means ruling out dense partial subsquares using
the actual prime-power arithmetic and retaining the signs and the same
vector in all three slots.  Unweighted energy or a two-weight bilinear
Kloosterman theorem does not make that inference.

The identity

```text
L=Y/sqrt(B)=sqrt(H),       sqrt(L)=H^(1/4)          (8.3)
```

explains why the absolute-`L3` revival obstruction also appears at the
quarter-power scale.  It neither proves nor refutes the signed estimate
(8.1).

---

## 9. Scope and executable checks

```text
current signed Schur exponent 49/66:                PROVED EARLIER;
applicable surveyed fixed-power incidence theorem: NONE FOUND;
Bettin--Chandee formal saving 27/220:                INAPPLICABLE;
absolute arbitrary-coefficient L3 bound (0.4):      FALSE;
signed H^(1/4+o(1)) theorem:                        OPEN;
transverse exponent 41/66:                          NOT PROVED;
QP, QP-to-strip, or a uniform strip:                NOT PROVED.
```

Run the exact ledger and normalization checks with

```bash
python3 -m pytest -q \
  src/test_qp_weighted_near_determinant_literature_gate.py
```

---

## Primary sources

1. J.-M. Deshouillers and H. Iwaniec,
   [*Kloosterman sums and Fourier coefficients of cusp forms*](https://gdz.sub.uni-goettingen.de/download/pdf/PPN356556735_0070/LOG_0019.pdf),
   Invent. Math. 70 (1982), 219--288;
   [DOI](https://doi.org/10.1007/BF01390728).
2. S. Bettin and V. Chandee,
   [*Trilinear forms with Kloosterman fractions*](https://arxiv.org/abs/1502.00769),
   Adv. Math. 328 (2018), 1234--1262.
3. O. Robert and P. Sargos,
   [*Three-dimensional exponential sums with monomials*](https://perso.univ-st-etienne.fr/rool6510/robert-2006-crelle.pdf),
   J. Reine Angew. Math. 591 (2006), 1--20;
   [DOI](https://doi.org/10.1515/CRELLE.2006.012).
4. I. D. Shkredov,
   [*Modular hyperbolas and bilinear forms of Kloosterman sums*](https://arxiv.org/abs/1905.00291).
5. B. Kerr, I. D. Shkredov, I. E. Shparlinski, and A. Zaharescu,
   [*Energy bounds for modular roots and their applications*](https://arxiv.org/abs/2103.09405),
   J. Inst. Math. Jussieu 24 (2025), 1765--1806.
6. I. D. Shkredov,
   [*On multiplicative energy of subsets of varieties*](https://arxiv.org/abs/2101.09770).

Only primary papers are used for the technical literature claims in this
audit.
