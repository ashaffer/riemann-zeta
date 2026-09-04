# Nyman first collar: favorable subsequences and the scalar Mellin gate

Status: final direct attack, 2026-08-13.

Binary verdict: **no fixed `10^(-6)` saving and no favorable full-collar
subsequence are proved**.  The exact ANOVA scalar has an explicit Mellin
transform containing `1/zeta`.  The dyadic mean-square bound needed to
select it by Markov at the `b=.999999` threshold already proves the same
fixed zero-free strip.  Modern averaged-Mobius input gives logarithmic, not
fixed-power, decay and does not cross this gate.

## 1. Full-Q subsequences versus first-collar subsequences

Let

```text
Q_(p,b)(n)^p
 =sum_(n<=m<=n^(1/b))|F_n(m)|^p m^(-1-pb).
```

If `rho=beta+i gamma` is a zeta zero with `beta>b`, the discrete principal
mode and the trivial remote-tail bound give, for every sufficiently large
`n`,

```text
Q_(p,b)(n)>=c_(rho,p,b)n^(beta-b).                  (1.1)
```

Consequently

```text
Q_(p,b)(n_j)=n_j^o(1) for one unbounded sequence
   => zeta(s)!=0 for Re(s)>b.                       (1.2)
```

This is why freedom to choose `n` is legitimate for the **full** localized
collar.  It is not legitimate after discarding the higher harmonic
cofactors.  A small first collar on a sparse sequence alone has no known
analytic implication, because it need not control the rest of `Q`.

## 2. Exact ANOVA scalar

Recall

```text
g(n)=sum_(k<=n)mu(k)/k,
C_n=n gamma(n)=n g(n)-M(n).
```

On `n<=m<2n`, `F_n(m)=M(m)+C_n`.  Its quadratic energy is

```text
sum_(n<=m<2n)|F_n(m)|^2
 =|L_n|^2/n
  +(1/n)sum_(0<=u<v<n)
       |sum_(u<j<=v)mu(n+j)|^2,                    (2.1)

L_n=n^2g(n)+sum_(j=1)^(n-1)(n-j)mu(n+j).           (2.2)
```

The normalization here is essential:

```text
F_n(m)=M(m)+n gamma(n)=M(m)-M(n)+n g(n).
```

It is **not** `M(m)+n g(n)`; omitting the `-M(n)` term changes both the
scalar mean and the ANOVA identity.

Both summands are nonnegative.  At `b=.999999`, the full first-collar
target would require

```text
|L_n|<=n^(1.999999+o(1)),                           (2.3)

bridge energy<=n^(2.999998+o(1)).                  (2.4)
```

The scalar (2.2), not the centered bridge, is the term left untouched by a
short-interval theorem which compares local averages with a retained long
mean.

## 3. The scalar is one explicit `1/zeta` carrier

Define the continuous interpolation

```text
w(x)=1/x,       0<x<=1,
     =2-x,       1<x<2,
     =0,         x>=2,

L(x)=x sum_(k>=1)mu(k)w(k/x).                       (3.1)
```

Then `L(n)=L_n` exactly.  The Mellin transform of `w`, initially for
`Re(s)>1`, is

```text
W(s)=integral_0^infinity w(x)x^(s-1)dx
    =1/(s-1)+2(2^s-1)/s-(2^(s+1)-1)/(s+1)
    =2[(s-1)2^s+1]/[s(s+1)(s-1)].                  (3.2)
```

Termwise substitution `y=k/x` gives the exact identity

```text
integral_0^infinity L(x)x^(-s-2)dx=W(s)/zeta(s),
                                                   Re(s)>1. (3.3)
```

The possible zeros of `W` satisfy

```text
(1-s)2^s=1.                                        (3.4)
```

If `0<Re(s)<1` and `|Im(s)|>1`, the modulus of the left side is
`2^Re(s)|1-s|>1`; hence (3.4) is impossible.  The classical verified
location of the first nontrivial zeta zero therefore shows that `W(rho)` is
nonzero at every nontrivial zeta zero.

### Theorem 3.1 (the Markov-scale scalar mean is strip strength)

Fix `0<b<1`.  Suppose that for all sufficiently large `X`,

```text
sum_(X<=n<2X)|L_n|^2 << X^(3+2b).                  (3.5)
```

Then `zeta(s)` has no zero in `Re(s)>b`.

#### Proof

On every open interval avoiding its finitely many breakpoints, (3.1) gives

```text
|L'(x)|<<x log(2x).                                 (3.6)
```

Continuity at the breakpoints and (3.6) show that (3.5) implies

```text
integral_X^(2X)|L(x)|^2dx<<X^(3+2b)+X^3 log^2 X
                         <<X^(3+2b).                (3.7)
```

For `sigma>b`, Cauchy--Schwarz on each dyadic interval gives

```text
integral_X^(2X)|L(x)|x^(-sigma-2)dx <<X^(b-sigma).
```

Dyadic summation therefore continues the left side of (3.3)
holomorphically to `Re(s)>b`.  Hence `W(s)/zeta(s)` is holomorphic there.
Since `W` does not vanish at a nontrivial zeta zero, no such zero can lie in
that half-plane.  QED

The exponent in (3.5) is exactly the exponent needed for Markov to produce
(2.3): there are `asymp X` candidate values of `n`, and the desired square
size is `X^(2+2b)`.  Thus an averaged proof of a favorable scalar at this
scale is not a lower-strength preliminary estimate; uniformly on dyadic
scales it is already the requested strip theorem.

## 4. Why current averaging does not select the required subsequence

Modern almost-all short-interval results give, for each **fixed** `A`,
Mobius cancellation of size `H/(log X)^A` outside an exceptional set of
size `O_A(X/(log X)^A)` in their stated ranges.  Inserted into the bridge
ledger, this yields fixed-`A` logarithmic savings after the usual dyadic
bookkeeping, not the factor

```text
X^(-2(1-b))=X^(-0.000002)                           (4.1)
```

needed in (2.4).  The power saving in the older sparse-support theorem is
in exceptional-set cardinality, not in the retained long mean `L_n`.

Having `O_A((log X)^(-A))` for every fixed `A` does not imply a
fixed-power favorable subsequence without quantitative uniformity in `A`.
For example,

```text
exp(-sqrt(log X))<<_A(log X)^(-A)                  (4.2)
```

for every fixed `A`, but it is `X^(-o(1))` and exceeds every `X^(-c)` for
large `X`.  A diagonal choice of `A` therefore cannot be made from the
published fixed-parameter quantifiers.

Likewise, selecting `n` at a sign change of a weighted Mertens scalar would
not suffice: no theorem audited here makes the same sparse `n` satisfy the
fixed-power bridge bound (2.4) and the higher-cofactor bounds needed for the
full `Q`.

## 5. Truth boundary

Proved here:

1. the exact scalar weight and Mellin identity (3.1)--(3.3);
2. noncancellation of its `1/zeta` poles by `W` at nontrivial zeros;
3. the fixed-strip implication (3.5);
4. the precise distinction between a full-Q subsequence and a first-collar
   subsequence.

Not proved:

1. (2.3) and (2.4) simultaneously on any unbounded sequence;
2. a fixed-power mean estimate (3.5);
3. `Q_(p,.999999)(n)=n^o(1)` on a subsequence;
4. any new zero-free strip.

The final direct route is therefore genuinely blocked at a coefficient-
specific fixed-strip theorem: either prove the scalar mean bound (3.5), or
find a sparse selection mechanism that controls `L_n`, the entire bridge,
and all harmonic cofactors jointly.  Current averaged-Mobius estimates do
not do this.
