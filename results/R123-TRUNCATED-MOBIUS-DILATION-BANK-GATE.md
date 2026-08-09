# R123 truncated-Mobius dilation bank gate

Status: a short-span exact cofactor-collapse theorem and a two-member
zero-faithful detector bank are proved.  Truncating the Mobius divisor sum
by its **integer value**, rather than expanding the Euler product over all
primes below the cofactor cutoff, removes the long-shift obstruction in
R106.  The operation collapses the free Vaughan cofactor exactly while
retaining every zeta-zero carrier up to a subpower loss.  It does not,
however, collapse either of the two balanced factors.  Its endpoint is
exactly the square-root `mu(d)Lambda(b)` block which R105 and R116 identify
as the primitive smooth-Mertens obstruction.  Thus this is a genuine
improvement in the dilation ledger, but not yet a fixed zero-free strip.

Date: 2026-08-07.

Predecessors:

* [`R105-GROWING-COFACTOR-DILATION-FILTER-GATE.md`](R105-GROWING-COFACTOR-DILATION-FILTER-GATE.md),
  for the Ramanujan-column dilation tensor;
* [`R106-ROUGH-EULER-DILATION-SIEVE-GATE.md`](R106-ROUGH-EULER-DILATION-SIEVE-GATE.md),
  for the full small-prime Euler-product sieve and its long shift span;
* [`R105-QH-VAUGHAN-TAIL-NATIVE-BRIDGE-AUDIT.md`](R105-QH-VAUGHAN-TAIL-NATIVE-BRIDGE-AUDIT.md),
  for the balanced endpoint which remains after the free cofactor is one;
  and
* [`R116-SIGNED-JOINT-TYPEII-ATTACK.md`](R116-SIGNED-JOINT-TYPEII-ATTACK.md),
  for the primitive reciprocal-to-smooth-Mobius duality.

## 1. The new operation

Let

```text
(tau_a F)(R)=F(R+a),

C_Y=sum_(1<=q<=Y) mu(q)q^(-1/2)tau_(-log q).          (1.1)
```

This is not R106's product over `p<=Y`.  That product contains translations
indexed by every squarefree divisor of `prod_(p<=Y)p`, and hence has shift
span `theta(Y)`.  Formula (1.1) retains only the integers `q<=Y`, so its
exact shift span is

```text
log Y.                                                (1.2)
```

Put

```text
f_R(t)=t^(-1/2)V_Q(R-log t),
F_(d,b)(R)=sum_(m>=1)f_R(mdb).                        (1.3)
```

The basic scaling identity is

```text
q^(-1/2)f_(R-log q)(t)=f_R(qt).                       (1.4)
```

Consequently

```text
C_Y F_(d,b)(R)
 =sum_(m>=1) [sum_(q|m;q<=Y)mu(q)]f_R(mdb).           (1.5)
```

This leads to the first exact theorem.

### Theorem 1.1 (short-span cofactor collapse)

Suppose the support of `f_R(mdb)` restricts the free cofactor to `m<=M`.
For every integer `Y>=M`,

```text
C_Y F_(d,b)(R)=f_R(db).                               (1.6)
```

#### Proof

For every active `m`, all of its divisors satisfy `q<=m<=M<=Y`.  The
bracket in (1.5) is therefore

```text
sum_(q|m)mu(q)=1_(m=1).                               (1.7)
```

Only `m=1` remains.  QED.

On the regular Vaughan schedule `log M=O(R/k)=o(R)`.  Thus (1.2) stays
inside the same logarithmic block after the usual safety margin.  This
removes the specific R106 incompatibility

```text
theta(Y) >> R       when       Y>=M=exp[Theta(R/k)].  (1.8)
```

The replacement has only `log Y=O(R/k)` span.

## 2. Exact action on the completed arithmetic field

For a finitely supported sequence `a`, write

```text
D_(a,V)(R)=sum_(n>=1)a(n)n^(-1/2)V(R-log n),
mu_<=Y(q)=mu(q)1_(q<=Y).                              (2.1)
```

Reindexing `n=qm` gives

```text
C_Y D_(a,V)=D_(mu_<=Y*a,V).                           (2.2)
```

In particular, on the center-annihilated prime field,

```text
C_Y D_(Lambda,V_Q)=D_(mu_<=Y*Lambda,V_Q).             (2.3)
```

Equations (2.2)--(2.3) are identities for the **whole** transformed field.
They therefore retain the exact cutoff heads and shells.  If one instead
uses (1.6) only on a frozen Vaughan tail, the same `C_Y` must still be
applied to all complementary pieces before claiming a statement about
zeta zeros.

The elementary critical triangle cost is subpower.  If uniformly on the
shifted block

```text
abs(F(S))<=exp(S/2+o(R)),                              (2.4)
```

then

```text
abs(C_YF(R))
 <=exp(R/2+o(R))sum_(q<=Y)abs(mu(q))/q
 <=exp(R/2+o(R))log(2Y).                              (2.5)
```

Also, on the real Fourier axis the multiplier has the coefficient-uniform
bound

```text
sup_t abs sum_(q<=Y)mu(q)q^(-1/2-it)
 <=sum_(q<=Y)q^(-1/2)<<sqrt(Y).                       (2.6)
```

When `log Y=O(R/k)` and `k` tends to infinity, both (2.5) and (2.6) cost
`exp(o(R))`.

## 3. A two-member bank retains every zeta zero

On a zero carrier the exact multiplier is

```text
C_Y exp[(rho-1/2)R]
 =A_Y(rho)exp[(rho-1/2)R],

A_Y(s)=sum_(q<=Y)mu(q)q^(-s).                         (3.1)
```

A single `A_Y(rho)` has no known uniform lower bound.  This is not fatal:
two adjacent cutoffs above the cofactor range form a faithful bank.

### Theorem 3.1 (adjacent-cutoff zero-faithfulness)

Let `M>=2`.  Choose a prime `P` with

```text
M<P<2M                                                     (3.2)
```

(with the harmless endpoint modification in the smallest cases), and put
`Y_0=P-1`, `Y_1=P`.  Then both operators collapse every cofactor `m<=M`,
and for every complex `s` with `0<Re(s)<1`,

```text
max(abs A_(Y_0)(s),abs A_(Y_1)(s))
 >=(1/2)P^(-Re(s))
 >=1/(4M).                                           (3.3)
```

#### Proof

Both cutoffs are at least `M`, so Theorem 1.1 applies.  Since `P` is prime,

```text
A_P(s)-A_(P-1)(s)=mu(P)P^(-s)=-P^(-s).               (3.4)
```

The triangle inequality gives the first bound in (3.3).  The second uses
`P<2M` and `Re(s)<1`.  QED.

Bertrand's postulate supplies (3.2); choosing the least prime above `M`
is enough.  At the regular scale, (3.3) loses only

```text
exp[-O(log M)]=exp[-O(R/k)]=exp[o(R)].                (3.5)
```

Thus no hypothetical off-axis zero can be hidden simultaneously from the
two collapsed fields.  Composing with R102's `Q_h` preserves this
conclusion because its zero multiplier is nonzero at every nontrivial zeta
zero.

This bank argument is deliberately weaker than an `L^2` inverse for
`C_Y`: no such coefficient-uniform inverse is asserted.  For a
zero-exclusion argument it is enough to prove the required arithmetic
upper bound for both members of the finite bank and then use (3.3) on the
rightmost zero carrier.

## 4. The endpoint after exact collapse

Apply Theorem 1.1 to the actual balanced Vaughan tail.  It gives

```text
sum_(d>U,b>V)mu(d)Lambda(b) C_YF_(d,b)(R)
 =sum_(d>U,b>V)mu(d)Lambda(b)f_R(db).                 (4.1)
```

At `U,V=X^(1/2-o(1))`, the surviving top block has

```text
d asymp sqrt(X),       b asymp sqrt(X),       db asymp X. (4.2)
```

This is exactly R105's `m=1` balanced block.  The identity
`sum_(q|m)mu(q)=1_(m=1)` acts on the **free cofactor** `m`; it does not
replace either `d` or `b` by one and it does not make the composite product
`db` prime.

After the signed reciprocal completion of R116, (4.1) becomes the same
primitive ordinary-product packet

```text
c sum_(d,b)
 mu(d)Lambda(b)/(db)^(1+it) Phi_c(db/c),              (4.3)
```

and, after restoring the Vaughan heads, the same weighted-Mertens carrier

```text
-c sum_n mu(n)log(n)n^(-1-it)Phi_c(n/c).              (4.4)
```

The two-bank lower bound (3.3) proves that the filter has not discarded a
zero responsible for (4.4).  It supplies no cancellation inside (4.3) or
(4.4).  In particular, R118's sparse prime-average theorem still needs a
native bridge from the composite full-support packet; cofactor collapse
does not create that bridge.

## 5. What was gained, and what was not

The exact ledger is now

```text
full small-prime Euler product shift span       theta(Y);
truncated integer-Mobius shift span             log Y;
free cofactor m<=M, Y>=M                       collapses exactly;
two adjacent cutoffs above M                    zero-faithful, subpower;
balanced d,b endpoint                           unchanged;
primitive smooth-Mobius packet                  unchanged;
fixed zero-free strip                           still open.           (5.1)
```

Accordingly, the long-span objection in R106 is not a universal objection
to exact Mobius cofactor collapse; (1.1) works around it.  The sharper
reality check is that the free cofactor was not the final obstruction.
Once it is removed without damaging the detector, the square-root
`mu(d)Lambda(b)` tensor remains at full exponent size.

The next valid use of this theorem is as a preprocessing step in any
attempt to bridge the balanced composite packet to R118/R119.  It permits
that attempt to set the free Vaughan cofactor exactly equal to one, with a
finite zero-faithful detector bank and only a subpower shift cost.  A proof
must still exploit cancellation in the two balanced factors jointly; a
second invocation of (1.7) on the already collapsed cofactor does not do
so.
