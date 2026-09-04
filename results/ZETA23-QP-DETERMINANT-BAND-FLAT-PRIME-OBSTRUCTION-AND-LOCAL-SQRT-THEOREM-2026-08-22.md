# QP determinant band: flat-prime obstruction and a local square-root theorem

**Date:** 2026-08-22  
**Verdict:** the proposed positive-tensor improvement

```text
W_D(z)=sum_(0<|ad-bc|<=D) |z_a z_b z_c z_d|
       <<D^(1-eta) q^o(1)||z||_2^4                         (0.1)
```

is false uniformly on the actual prime-power shell for every fixed
`eta>0`.  Flat weights on all shell primes give

```text
W_D(z)>>D/(log q)^2=D^(1-o(1)).                           (0.2)
```

This remains true after requiring all four colors to be distinct.  Thus
finite-field determinant distribution, a multiplicative large sieve, or
prime Sidonicity cannot improve the **positive** determinant-band tensor
uniformly; a signed or completion-sensitive restriction is indispensable.

There is, however, a sharp theorem at the narrower participation endpoint.
If all active colors lie in one integer interval `[X,X+L]` with

```text
D+L^2<X,                                                   (0.3)
```

then, for arbitrary weights,

```text
W_D(z)<<sqrt(D)||z||_2^4.                                 (0.4)
```

The same estimate holds with or without repeated colors and with any
subfamily, including the high-completion tuples.  At `D=q^(16/33)`, a
block of `D` prime colors occupying length `D q^o(1)` satisfies (0.3),
because its squared span is `q^(32/33+o(1))=o(q)`.  Hence the flat
`R_43~D` **localized** packet is not the broad obstruction: it has a full
square-root saving.  Scattered `R_43~D` weights and the restriction
`m(C)>=3` remain open.

For an arbitrary, possibly scattered **flat** support `A` of actual shell
prime powers with `M=|A|<=D`, a separate multiplicative-character argument
proves the unconditional power saving

```text
#{(a,b,c,d) in A^4:0<|ad-bc|<=D}/M^2
 <<q^o(1)[M*D/q+M^(1/4)*sqrt(D)]
 <<D^(3/4+o(1)).                                      (0.5)
```

The desired `D^(1/2+o(1))` follows from one exact remaining input: the
multiplicative energy of `A` modulo each `a in A` must be
`M^(2+o(1))` on average in the fourth-root sense.  The unconditional bound
is `M^3`, and no such actual-prime inverse theorem is presently known.

**Subsequent uniform synthesis.**  Formula (0.5) holds for every `M`, not
only `M<=D`.  Applied to factor-two coefficient-height bins, it meets the
proved diffuse participation estimate at `M=D^(7/4)`.  The small-bin broad
cap, the parabolic theorem, and the large-bin diffuse estimate all then
give the same fourth-trace exponent `D^(5/4)`.  Schatten-`4` triangle
recombination proves the new uniform theorem

```text
||A_z||_(S_4)^4, |Q_nd(z)|
 <<D^(5/4)q^o(1)||z||_2^4,                              (0.6)
```

improving the prior uniform `D^(21/16)` exponent by `D^(1/16)`.  The full
proof and hostile audit are in
`ZETA23-QP-UNIFORM-FIVE-FOURTHS-FLAT-BIN-CHARACTER-SYNTHESIS-2026-08-22.md`.
It gives operator exponent `5/16` and transferred transverse exponent
`43/66`; it does not prove the literal `D` four-cycle bound.

---

## 1. A proof-grade all-distinct flat-prime lower bound

Choose a fixed closed interval `[alpha q,beta q]` in the interior of the
project shell, with `0<alpha<beta`, and let `P_q` be its primes.  The prime
number theorem gives

```text
M=#P_q>>q/log q.                                           (1.1)
```

Use the `N=M(M-1)` ordered reduced slopes

```text
R={(a,b):a,b in P_q, a!=b},       rho_(a,b)=a/b.           (1.2)
```

Unique factorization makes these slopes distinct.  Partition their fixed
compact range into

```text
J<<q^2/D                                                   (1.3)
```

half-open intervals of length at most `D/(beta^2 q^2)`.  If
`rho_(a,b)` and `rho_(c,d)` occupy the same interval, then

```text
|ad-bc|=bd*|a/b-c/d|<=D.                                  (1.4)
```

If the bin occupancies are `n_j`, Cauchy--Schwarz gives

```text
sum_j n_j(n_j-1)
 >=N^2/J-N
 >>M^4 D/q^2-M^2.                                         (1.5)
```

Every tuple in (1.5) has nonzero determinant because the reduced slopes
are distinct.  Coordinate repetitions cost only `O(M^2)`, not `O(M^3)`:

* `a=c` would give `|a(d-b)|>=alpha q>D` unless `b=d`, which is the deleted
  identical slope; the same argument handles `b=d`;
* if `a=d`, then fixed `(a,b)` permits at most one integer `c`, since the
  interval `|a^2-bc|<=D` has length `2D/b<1`; the case `b=c` is identical.

Consequently the number `E_dist` of same-bin tuples with four distinct
prime coordinates obeys

```text
E_dist>>M^4 D/q^2-O(M^2)>>M^4 D/q^2,                      (1.6)
```

because `D/(log q)^2` tends to infinity.  Put
`z_p=M^(-1/2)` on `P_q` and zero on every other prime power.  Then

```text
||z||_2=1,
R_43(z)=||z||_(4/3)^4=M=q^(1+o(1))=D^(33/16+o(1)),       (1.7)

W_D,dist(z)>=E_dist/M^2>>D*M^2/q^2>>D/(log q)^2.          (1.8)
```

This proves (0.2), including the nonzero and all-distinct restrictions.
The primality of the scale parameter `q` is not used; the construction is
valid in particular along prime `q`.

### Consequence

For any fixed `eta>0`, (1.8) contradicts
`W_D<<D^(1-eta)q^o(1)`.  A logarithmic prime-density saving is a
`q^o(1)` effect and cannot change the determinant exponent.  The lower
bound is the constant/volume mode of determinant distribution, so a
finite-field or automorphic spectral decomposition must retain it.

---

## 2. Exact local reduction to a hyperbolic parallelogram

Now suppose the support of `z` is contained in `[X,X+L]` and (0.3) holds.
Write

```text
a=X+A, b=X+B, c=X+C, d=X+F,       0<=A,B,C,F<=L.          (2.1)
```

Then

```text
ad-bc=X(A+F-B-C)+(A*F-B*C).                              (2.2)
```

The second parenthesis has modulus at most `L^2`.  Therefore
`|ad-bc|<=D` and (0.3) force the integer coefficient of `X` to vanish:

```text
a+d=b+c.                                                   (2.3)
```

Substitute `d=b+c-a` into the determinant:

```text
ad-bc=-(a-b)(a-c).                                        (2.4)
```

Thus the nonzero local form is exactly

```text
sum_(h,k!=0, |hk|<=D) sum_a
 u_a u_(a-h) u_(a-k) u_(a-h-k),       u=|z|.              (2.5)
```

Weights outside `[X,X+L]` are understood to be zero.

---

## 3. Dyadic autocorrelation proves the square-root theorem

Normalize `||u||_2=1` and place the nonzero gaps in dyadic blocks

```text
H<=|h|<2H,       K<=|k|<2K.                              (3.1)
```

For fixed `h`, put

```text
v_h(a)=u_a u_(a-h).                                       (3.2)
```

The contribution of (3.1) is at most

```text
sum_(h~H) sum_(|k|<2K) <v_h,tau_k v_h>
 <<K sum_(h~H)||v_h||_2^2
 <=K,                                                       (3.3)
```

because convolution with an interval of `O(K)` shifts has `ell^2`
operator norm `O(K)` and

```text
sum_h ||v_h||_2^2
 =sum_(a,h)u_a^2 u_(a-h)^2
 =||u||_2^4=1.                                           (3.4)
```

Interchanging `h` and `k` also bounds (3.1) by `O(H)`.  Hence every block
costs

```text
O(min(H,K)).                                               (3.5)
```

Only blocks with `H*K<=D` occur.  The dyadic sum has no logarithmic loss:

```text
sum_(H,K dyadic, HK<=D) min(H,K)<<sqrt(D).                (3.6)
```

Indeed, in the half `H<=K`, it is
`sum_(i<=j,i+j<=log_2 D)2^i<<sqrt(D)`; the other half is symmetric.
Equations (2.5)--(3.6) prove (0.4).  If determinant zero is retained, the
branches `h=0` or `k=0` add at most `2||z||_2^4`.

The exponent `1/2` is sharp for this argument and for the full-integer
local model.  Take normalized flat weights on `L~sqrt(D)` consecutive
integers.  A positive proportion of the triples with distinct positive
gaps `h,k<=L/8` have four distinct coordinates and satisfy `|hk|<=D`;
there are `asymp L^3` such tuples, each of weight `L^(-2)`, giving
`W_D>>L~sqrt(D)`.

---

## 4. What happens at `R_43~D`

Partition a fixed interior shell interval into intervals of length

```text
L=C D log q.                                               (4.1)
```

There are `O(q/L)` intervals and `>>q/log q` shell primes, so for a fixed
large enough `C` at least one interval contains `>>D` primes.  Select a
constant multiple of `D` of them and use flat weights.  Then

```text
R_43(z)~D,
L^2=q^(32/33+o(1))=o(q),                                 (4.2)
```

and (0.4) gives

```text
W_D(z)<<D^(1/2)||z||_2^4.                                (4.3)
```

So the natural localized block of `D` consecutive-scale shell primes does
not reproduce the global Cauchy lower bound.  The lower bound (1.8) needs
the whole fixed-width shell and has `R_43=D^(33/16+o(1))`.

This distinction leaves two possible refined statements alive:

```text
support in one q^(1/2-o(1)) interval:       sqrt(D) theorem PROVED;
arbitrary/scattered R_43~D weights:          OPEN;
determinant mass restricted to m(C)>=3:      OPEN.          (4.4)
```

The global lower bound does not know whether a determinant tuple has an
actual carry completion, much less three completions.  Conversely, the
local theorem is positive and therefore applies automatically to every
completion-restricted subfamily inside one short color interval.  Existing
actual three-completion fixtures can have macroscopic color diameter, so
high completion does not force the hypothesis (0.3).

---

## 5. Method ledger

### 5.1 A scattered flat-support theorem from character fourth moments

Let `A` contain `M` actual prime powers in the narrow shell and assume
`M<=D`.  Distinct shell nodes have distinct prime bases and hence are
pairwise coprime.  Fix `a in A`.  In a nonzero determinant tuple, neither
`b` nor `c` can equal `a`: for example, `b=a` would give
`a(d-c)`, whose nonzero modulus is larger than `D`.  Thus `b,c` are units
modulo `a`.

For fixed `(a,b,c)`, the interval

```text
|a*d-b*c|<=D                                             (5.1)
```

has length `2D/a<1` in the integer `d`; hence there is at most one `d`.
Also (5.1) implies

```text
b*c (mod a) in I_a={r: r=+-1,...,+-D (mod a)}.          (5.2)
```

Discarding the requirement `d in A` only enlarges the count.  Write

```text
B_a(chi)=sum_(b in A\{a}) chi(b),
H_a(chi)=sum_(h in I_a) chi(h).                          (5.3)
```

Multiplicative-character orthogonality on `(Z/aZ)^*` gives a principal
term `O(M^2D/q)` and a nonprincipal remainder bounded by

```text
1/phi(a) sum_chi |B_a(chi)|^2 |H_a(chi)|.               (5.4)
```

Use Holder with exponents `2,4,4`, putting one copy of `B_a` in the second
moment and one in the fourth moment.  If

```text
E_a(A)=#{x1*x2=x3*x4 (mod a):xi in A\{a}},              (5.5)
```

orthogonality gives

```text
(5.4) <=M^(1/2)*E_a(A)^(1/4)*E_a(I_a)^(1/4).            (5.6)
```

The shell diameter is smaller than `a`, so all nodes have distinct
residues.  Consequently the trivial three-variable determination bound is

```text
E_a(A)<=M^3.                                             (5.7)
```

The short interval has a much sharper exact fourth moment.  Since

```text
2D^2<a                                                   (5.8)
```

at `D=q^(16/33)`, a congruence
`h1*h2=h3*h4 (mod a)` with `0<|hi|<=D` is an integer equality.  The divisor
bound therefore gives

```text
E_a(I_a)<<D^(2+o(1)).                                    (5.9)
```

Equations (5.6)--(5.9) bound the triples for one `a` by

```text
M^2D/q+M^(5/4)D^(1/2)q^o(1).                           (5.10)
```

Summing over the `M` choices of `a` and dividing by the flat normalization
`M^2` proves (0.5):

```text
W_D(M^(-1/2)1_A)
 <<q^o(1)[M*D/q+M^(1/4)D^(1/2)].                       (5.11)
```

The argument is valid for prime-power moduli `a`, not merely primes: it
uses the full character group of the units modulo `a`.  No Burgess estimate
is needed.  Repeated coordinates excluded above contribute only to the
zero determinant layer.

For `M=D^mu`, `0<=mu<=1`, (5.11) and the matching bound give the profile

```text
min(D^mu,D^(1/2+mu/4))q^o(1),                           (5.12)
```

with crossover at `mu=2/3` and endpoint `D^(3/4)`.

### 5.2 Exact gate to the square-root endpoint

Retaining `E_a(A)` rather than (5.7), the same proof gives

```text
N_D(A)
 <<M^3D/q
   +M^(1/2)D^(1/2)q^o(1) sum_(a in A) E_a(A)^(1/4).     (5.13)
```

Therefore the desired scattered-support theorem

```text
N_D(A)/M^2<<D^(1/2)q^o(1)                              (5.14)
```

would follow from

```text
sum_(a in A) E_a(A)^(1/4)<<M^(3/2)q^o(1).              (ME)
```

In particular, the pointwise estimate
`E_a(A)<<M^(2+o(1))` suffices.  This is a precise inverse-sieve/sum-product
gate.  The diagonal lower bound has size `M^2`, so its exponent would be
best possible.  Generic finite-field sum-product does not prove `(ME)` for
an arbitrary subset: modulo one prime, an unrestricted integer set can be
lifted from a multiplicative subgroup and have energy `M^3`.  Showing that
the **same actual prime-power set containing the modulus** cannot do this
for many of its own moduli is the missing arithmetic theorem.  Dropping
the quotient condition `d in A` in (5.2) also means `(ME)` is sufficient,
not known to be necessary for (5.14).

No interval covering argument alone supplies `(ME)`: it controls the
localized chart of Sections 2--4, while modular energy measures interactions
between macroscopically scattered cells.

### 5.3 Promotion to a localized four-cycle theorem

On the oriented all-distinct retained sector, the proved global fixed-color
theorem says

```text
m(C)<<D^(1/2)q^o(1).                                    (5.15)
```

If `z` is supported in `[X,X+L]` under (0.3), positivity and (0.4) give

```text
sum_C m(C)|z_a z_b z_c z_d|
 <<D^(1/2)q^o(1) W_D(z)
 <<D q^o(1)||z||_2^4.                                  (5.16)
```

The orientation convention changes only an absolute factor.  A zero
determinant cannot occur with four distinct actual prime-power colors:
`ad=bc` and pairwise coprimality force the two unordered factor pairs to
coincide.  The repeated-node, permutation, square-edge, and opposite-color
equality sectors were already proved `O(Dq^o(1)||z||_2^4)`.  Adding them to
(5.16) proves the sharp four-cycle bound for **every** coefficient vector
supported in one interval satisfying (0.3), regardless of its support size
or coefficient flatness.

This is a genuine coefficient-location theorem, but not a uniform FC proof:
a broad vector can place mass in macroscopically separated shell intervals.

### 5.4 Binary ledger

```text
uniform W_D<=D^(1-eta)q^o for arbitrary weights: FALSE;
flat actual-prime all-distinct lower D/log^2 q:     PROVED;
prime/Sidon structure removes the constant mode:   FALSE;
local interval W_D<<sqrt(D):                       PROVED;
local exponent below 1/2 by geometry alone:        FALSE (integer packet);
localized flat R_43~D obstruction to a gain:       EXCLUDED;
localized sharp four-cycle bound Q_nd<<D:          PROVED;
scattered flat |A|<=D bound W_D<<D^(3/4+o):        PROVED;
scattered flat square-root bound from (ME):        CONDITIONAL;
actual-prime modular-energy theorem (ME):          OPEN;
scattered R_43~D positive-tensor gain:             OPEN;
high-completion-only positive-tensor gain:         OPEN;
uniform D^(5/4) four-cycle improvement:             PROVED BY SYNTHESIS;
literal uniform D four-cycle target:               OPEN.
```

Exact identities, collision subtraction, dyadic ledgers, and finite tests
are in `src/qp_determinant_band_sumproduct_audit.py` and
`src/test_qp_determinant_band_sumproduct_audit.py`.
