# QP four-cycle: the mixed-`H^2` product large sieve and the parabolic barrier

**Date:** 2026-08-23  
**Verdict:** a second product before the primitive-character large sieve gives
the rigorous flat-bin estimate

```text
W_D(A)
 << M*D/q
    + min(D^(1/2)*M^(1/4), q^(1/4)*D^(1/2)*M^(-1/4)) q^o(1).       (0.1)
```

After the uniform third-slice cap and the principal/diffuse switch, (0.1)
controls the broad/singleton part of the fourth trace by

```text
D^(9/8+o(1)) ||z||_2^4.                                           (0.2)
```

This is a real improvement over the `37/32` singleton estimate.  It does
**not** improve the complete theorem: the separately proved occupied-line
parabolic curvature term is still

```text
D^(37/32+o(1)) ||z||_2^4,                                         (0.3)
```

so the uniform trace exponent remains `37/32`.  Improving the complete
theorem now requires new curvature aggregation, not another flat-bin
character moment alone.

---

## 1. Character expression and the mixed interpolation

Let `A` be a set of `M` actual prime powers in the project shell.  For a
shell modulus `a`, write

```text
B_a(chi)=sum_(b in A) chi(b),
H_a(chi)=sum_(0<|h|<<D) chi(h).                                   (1.1)
```

As in the primitive-product large-sieve proof, the nonprincipal determinant
count is bounded by

```text
R_np=sum_a 1/phi(a) sum_(chi!=1) |B_a(chi)|^2 |H_a(chi)|.          (1.2)
```

Set

```text
F =sum_a 1/phi(a) sum_(chi!=1) |B_a(chi)|^2,
E2=sum_a 1/phi(a) sum_(chi!=1) |B_a(chi)|^2 |H_a(chi)|^4.          (1.3)
```

The identity

```text
|B|^2 |H|=(|B|^2)^(3/4)(|B|^2 |H|^4)^(1/4)                       (1.4)
```

and Holder give

```text
R_np <=F^(3/4) E2^(1/4).                                          (1.5)
```

Parseval and residue injectivity in the shell give

```text
F<=M^2.                                                           (1.6)
```

## 2. The coefficient norm of `B H^2`

First take `1<=h<=C D`.  Multiplicativity writes

```text
B_a(chi) H_(a,+)(chi)^2=sum_n alpha_n chi(n),
alpha_n=#{(b,h_1,h_2):b in A, 1<=h_i<=C D, b*h_1*h_2=n}.          (2.1)
```

If two representations with different shell values satisfy

```text
b_1 h_1 h_2=b_2 h_3 h_4,                                        (2.2)
```

then pairwise coprimality of distinct shell prime powers forces
`b_1|h_3 h_4`.  But

```text
0<h_3 h_4<<D^2<min A                                             (2.3)
```

at `D=q^(16/33+o(1))`, so this is impossible.  Thus the shell factor is
unique.  For a fixed shell factor, the ordinary truncated divisor-energy
bound gives

```text
sum_n #{h_1 h_2=n}^2 <<D^(2+o(1)).                               (2.4)
```

Consequently

```text
sum_n |alpha_n|^2 <<M D^(2+o(1)).                                (2.5)
```

The symmetric nonzero interval causes no problem.  Split it into its two
signs before applying (2.1), or use
`H_a=(1+chi(-1))H_(a,+)`.  This costs only an absolute constant.  There is
no zero product because `h=0` is excluded.  Dirichlet characters themselves
remove nonunits.

The coefficient support has length

```text
N<<q D^2=q^(65/33+o(1))<q^2.                                    (2.6)
```

## 3. Primitive conductors and the large sieve

Write a shell modulus as `a=p^j`.  Every nonprincipal character modulo `a`
is the unique lift of a primitive character of conductor `f=p^s`, `s>=1`.
Distinct shell prime powers have distinct bases, hence these nontrivial
conductor families are disjoint.  The only repeated conductor is conductor
one, and it is precisely the principal character omitted in (1.3).

Moreover

```text
1/phi(a) <<q^(-1) f/phi(f).                                      (3.1)
```

The primitive multiplicative-character large sieve, (2.5), and (2.6)
therefore imply

```text
E2
 <<q^(-1)(q^2+N) M D^(2+o(1))
 <<q M D^(2+o(1)).                                                (3.2)
```

Combining (1.5), (1.6), and (3.2),

```text
R_np <<q^(1/4) D^(1/2) M^(7/4) q^o(1).                           (3.3)
```

The flat vector has normalization `M^(-2)`, so

```text
W_np <<q^(1/4) D^(1/2) M^(-1/4) q^o(1).                          (3.4)
```

Adding the principal term `M D/q` proves (0.1), after taking the better of
(3.4) and the earlier fourth-moment term `D^(1/2)M^(1/4)`.

## 4. Exact exponent optimization

Write `M=D^mu` and `q=D^(33/16+o(1))`.  The old and mixed nonprincipal mass
exponents are

```text
old:       1/2+mu/4,
mixed H^2: 65/64-mu/4.                                           (4.1)
```

They meet at

```text
mu=33/32,             mass exponent=97/128.                       (4.2)
```

The uniform third-slice cap is `D^(5/16)`, so the nonprincipal singleton
trace is at most

```text
D^(97/128+5/16)=D^(137/128).                                     (4.3)
```

The principal singleton trace exponent is

```text
mu-3/4,                                                         (4.4)
```

whereas the diffuse route has exponent

```text
max(1,3-mu).                                                     (4.5)
```

Their decreasing/increasing envelopes meet at

```text
mu=15/8,                 exponent=9/8.                            (4.6)
```

Since `9/8>137/128`, (4.6) is the uniform broad/singleton exponent.

## 5. Why a third interval product does not improve this route

The clean shell-factor uniqueness used in (2.3) stops at the next moment:

```text
D^3=q^(16/11+o(1))>q.                                            (5.1)
```

This is an actual collision mechanism when proper prime powers are retained.
For two shell prime cubes `b_1=p^3`, `b_2=r^3`, the residual triples
`(r,r,r)` and `(p,p,p)` give

```text
b_1*r^3=b_2*p^3.                                                 (5.2)
```

Even if one recovers a `q^o(1)` multiplicity bound by divisor estimates,
the support of `B H^3` has length `qD^3>q^2`; the length term, rather than
the conductor term, then controls the primitive large sieve.  The resulting
normalized bound is `D M^(-1/6)`, which crosses the old fourth-moment bound
at `mu=6/5` with mass exponent `4/5`.  This is weaker than the `97/128`
maximum furnished by `H^2`.  Higher fixed powers only worsen that profile.

## 6. Remaining bottleneck

The complete slice decomposition is the sum of:

```text
broad/singleton contribution       <<D^(9/8+o(1)),
occupied-line parabolic curvature  <<D^(37/32+o(1)).              (6.1)
```

Thus the complete trace remains `D^(37/32+o(1))`.  The productive next
question is whether the curvature aggregation has cancellation or sparse
self-correlation not visible in its present positive gap-token estimate.

