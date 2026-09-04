# QP four-cycle: uniform `37/32` theorem from the primitive character large sieve

**Date:** 2026-08-23  
**Verdict:** applying the primitive multiplicative-character large sieve to
the *product* of the color and determinant-interval character sums improves
the normalized flat determinant mass to

```text
W_D(A) << M*D/q + sqrt(q*D/M) q^o(1).              (0.1)
```

The coefficient sequence in this large-sieve application has exactly
`M D q^o(1)` squared norm: multiplication of a shell prime power by an
integer shorter than the shell is collision-free.  Decomposing characters
modulo the shell prime powers into primitive conductors introduces neither
a multiplicity nor a lost power.

Combining (0.1) with the earlier character fourth-moment estimate, the
uniform third-slice cap, the occupied-line parabolic curvature theorem, and
the diffuse participation estimate proves

```text
||A_z||_(S_4)^4, |Q_nd(z)|
 << D^(37/32+o(1)) ||z||_2^4.                      (0.2)
```

Consequently

```text
||A_z||_op << D^(37/128+o(1)) ||z||_2,             (0.3)
```

and the established smooth transfer gives transverse exponent

```text
1/2+(37/128)*(16/33)=169/264.                      (0.4)
```

This is an unconditional improvement on the preceding `D^(5/4)` trace.
It is not the sharp `D^(1+o(1))` four-cycle theorem.

---

## 1. The fixed-modulus character expression

Let `A` be a set of `M` actual prime powers in the narrow project shell.
For a flat `L^2`-normalized vector on `A`, let `N_D(A)` count ordered
all-distinct color matrices with

```text
0<|a*d-b*c| << D q^o(1).                           (1.1)
```

Fix `a in A`.  Distinct shell prime powers have different prime bases and
are therefore pairwise coprime.  They are also distinct modulo `a`, since
the shell diameter is smaller than `a`.  Put

```text
B_a(chi)=sum_(b in A) chi(b),
H_a(chi)=sum_(0<|h|<<D) chi(h).                    (1.2)
```

Writing `b in A` rather than `A\{a}` changes nothing because every
Dirichlet character modulo `a` vanishes at `a`.  Character orthogonality,
after dropping the final quotient condition `d in A`, gives the principal
contribution

```text
O(M^2*D/q)                                         (1.3)
```

for this modulus, and bounds its nonprincipal contribution by

```text
1/phi(a) sum_(chi != chi_0) |B_a(chi)|^2 |H_a(chi)|. (1.4)
```

Summing (1.4) over the `M` choices of `a` and applying Cauchy--Schwarz gives

```text
R_np <= F^(1/2) E^(1/2),                           (1.5)

F=sum_a 1/phi(a) sum_(chi!=chi_0)|B_a(chi)|^2,
E=sum_a 1/phi(a) sum_(chi!=chi_0)|B_a(chi)H_a(chi)|^2.
```

Parseval on `(Z/aZ)^*` and residue injectivity give

```text
F <= M^2.                                          (1.6)
```

The gain comes from estimating `E` jointly over the varying moduli.

## 2. Primitive-conductor bookkeeping

Write one shell modulus as `a=p^j`.  Every nonprincipal character modulo
`p^j` is induced by a unique primitive character of conductor

```text
f=p^s,             1<=s<=j.                       (2.1)
```

There is no multiplicity attached to a fixed primitive character: its lift
to a character modulo `p^j` is unique.  The induced character and the
primitive character agree as arithmetic functions, including their zero
values on multiples of `p`.

Two distinct shell prime powers have distinct bases.  Hence the conductor
sets in (2.1) for different `a in A` are disjoint.  The only conductor which
would repeat is conductor one, and it corresponds exactly to the principal
characters already removed from `E`.

Since `a asymp q`, for every `f|a` one has

```text
1/phi(a) << 1/q <= (1/q)*f/phi(f).                 (2.2)
```

Thus the family in `E`, after conductor reduction, is a subfamily of the
usual primitive-character large sieve with its standard weights.

## 3. The product coefficient is collision-free

Multiplicativity gives

```text
B_a(chi)H_a(chi)
 =sum_n alpha_n chi(n),
alpha_n=#{(b,h): b in A, 0<|h|<<D, b*h=n}.        (3.1)
```

This representation is unique.  If

```text
b_1*h_1=b_2*h_2,                                  (3.2)
```

and `b_1!=b_2`, then `gcd(b_1,b_2)=1`, so `b_1|h_2`.
But `|h_2|<<D<min A` at the project scale, a contradiction.  Therefore
`b_1=b_2` and then `h_1=h_2`.  The two signs of `h` occupy disjoint product
supports.  Consequently

```text
sum_n |alpha_n|^2 << M*D q^o(1).                  (3.3)
```

The support of `alpha` has length `O(qD)`.  The primitive multiplicative
large sieve therefore yields

```text
E
 << q^(-1) (q^2+qD) sum_n |alpha_n|^2 q^o(1)
 << q*M*D q^o(1),                                 (3.4)
```

because `D<q`.  Equations (1.5), (1.6), and (3.4) give

```text
R_np << M^(3/2)*sqrt(qD) q^o(1).                  (3.5)
```

After summing (1.3) over `a` and dividing the count by the flat
normalization `M^2`, this proves (0.1):

```text
N_D(A)/M^2
 << M*D/q + sqrt(qD/M) q^o(1).                   (3.6)
```

The symmetric determinant interval is merely the union of two ordinary
intervals; splitting signs costs a constant.  Nonunits need not be removed
by hand because Dirichlet characters vanish on them.

## 4. Crossover with the fourth-moment bound

The previously proved character fourth-moment estimate is

```text
N_D(A)/M^2
 << M*D/q + D^(1/2)*M^(1/4) q^o(1).              (4.1)
```

Write `M=D^mu` and use `q=D^(33/16+o(1))`.  The two nonprincipal exponents
in (3.6), (4.1) are

```text
large sieve:       49/32-mu/2,
fourth moment:     1/2+mu/4.                       (4.2)
```

They agree at

```text
mu=11/8,
mass exponent=27/32.                              (4.3)
```

Thus their minimum is at most `D^(27/32+o(1))` for every support size.
The principal mass has exponent

```text
mu-17/16.                                          (4.4)
```

## 5. Inserting the slice and parabolic theorems

For every fixed all-distinct color matrix, let

```text
K_C=1+D/lambda_3(C).
```

Successive-minima ordering gives

```text
lambda_1 lambda_2 <=q^(2/3),
K_C<<D^(5/16+o(1)).                                (5.1)
```

The nondegenerate and identically-zero binary restrictions have
`m(C)<<K_Cq^o(1)`.  In the nonzero degenerate/parabolic case, the proved
occupied-line estimate is

```text
m_par(C)
 <<K_C+sqrt(D*K_C/h_C) q^o(1).                    (5.2)
```

The first term in every case is a singleton term.  On a factor-two
coefficient bin, positivity permits restricting (3.6), (4.1) to any slice
subfamily, and (5.1) costs `D^(5/16)`.  At (4.3) its trace exponent is

```text
27/32+5/16=37/32.                                 (5.3)
```

The gap-token theorem aggregates the second term of (5.2) over each
dyadic height block, and (5.1) gives

```text
Q_par,curv <<D*sqrt(K_max)q^o(1)||z||_2^4
             <<D^(37/32+o(1))||z||_2^4.           (5.4)
```

Zero-component remnants and heights above `D` are bounded per slice and
belong to the singleton term.  The relation assignment and its chart
multiplicity cost only `q^o(1)`.  Hence (5.3), (5.4) exhaust every
all-distinct slice type.

## 6. Principal/diffuse switch

For a factor-two coefficient bin of size `M=D^mu`, multiplying (4.4) by
the slice cap gives principal trace exponent

```text
mu-3/4.                                            (6.1)
```

It remains at most `37/32` through `mu=61/32`.  Independently, the proved
diffuse participation estimate gives complete trace

```text
D+D^3/M,                                           (6.2)
```

which is at most `D^(37/32)` from `mu=59/32` onward.  The two ranges overlap
by `D^(1/16)` in support exponent.  We may therefore use the character and
slice proof for

```text
M<=D^(59/32)
```

and (6.2) for larger bins.  Every bin has fourth trace bounded by
`D^(37/32+o(1))` times its fourth `L^2` mass.

## 7. Recombination and status

After deleting a superpolynomially tiny coefficient tail, there are only
`O(log q)` factor-two height bins.  Schatten-`4` triangle followed by
Cauchy--Schwarz recombines them with a `q^o(1)` loss.  Repeated-node,
permutation, square-edge, and opposite-color-equality sectors are already
`Dq^o(1)`.  This proves (0.2), and fourth roots give (0.3).  The established
band transfer gives (0.4).

```text
primitive-conductor reduction without multiplicity: PROVED;
product-convolution squared norm M*D:                 PROVED;
flat determinant mass (0.1):                         PROVED;
fourth-moment/large-sieve crossover mu=11/8:          PROVED;
parabolic singleton and curvature D^(37/32):          PROVED;
principal/diffuse overlap [59/32,61/32]:              PROVED;
uniform fourth trace D^(37/32+o(1)):                  PROVED;
uniform operator exponent 37/128:                     PROVED;
sharp four-cycle bound D^(1+o(1)):                    OPEN.
```

Exact finite convolution checks and rational-exponent ledgers are in
`src/qp_uniform_thirty_seven_thirty_seconds.py` and its test module.

The imported analytic inequality is the primitive multiplicative-character
large sieve of H. L. Montgomery and R. C. Vaughan, *The large sieve*,
Mathematika 20 (1973), 119--134.
