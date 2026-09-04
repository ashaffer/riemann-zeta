# Bergman super-conductor mollifier and reciprocal-jet gate

Status: independent fixed-strip attack, 2026-08-12.  This report proves an
exact two-dimensional zero detector, calibrates a barely super-conductor
Möbius mollifier at the line `Re rho = 0.99`, and isolates its one remaining
signed near-product correlation.  It also gives a separate high-derivative
audit for `1/zeta`: the ordinary Dirichlet mean-value error restores exactly
the boundary `Re s = 1` and no more.

No zero-free strip or improved zeta zero bound is proved here.

```text
zero => fixed Bergman-area obstruction                 THEOREM
natural mollifier diagonal at X=T^1.03                 o(1)
Euler--Maclaurin completion in the Bergman box          o(1)
remaining term                                          one signed offdiagonal
coefficient-blind offdiagonal bound                     X^0.044+o(1)
same-sign semiprime subblock                            >=X^0.044/log^5 X
termwise/absolute-value closure                         IMPOSSIBLE
signed cancellation of the complete offdiagonal        OPEN
uniform zero-free strip                                 NOT PROVED
```

## 1. A two-dimensional zero detector

Put

```text
beta_0=0.99,       r=0.001,
sigma_-=0.989,     sigma_+=1.001,
Omega_T=[sigma_-,sigma_+] x [T-r,2T+r].                 (1.1)
```

For any Dirichlet polynomial `M` let

```text
E_M(s)=1-zeta(s)M(s).                                  (1.2)
```

There is no pole of `E_M` in `Omega_T` when `T>2`.  If

```text
rho=beta+i gamma,
beta>=beta_0,       T<=gamma<=2T,                       (1.3)
```

is a zeta zero, then the closed disc `D(rho,r)` is contained in
`Omega_T` and

```text
E_M(rho)=1.                                             (1.4)
```

The area mean-value inequality for the subharmonic function `|E_M|^2`
therefore gives the coefficient-independent obstruction

```text
integral_(Omega_T) |E_M(s)|^2 dA(s)
 >=pi*r^2=pi*10^(-6).                                  (1.5)
```

This proves the following criterion.

**Theorem 1.1 (Bergman mollifier criterion).**  If for every sufficiently
large `T` one can exhibit a Dirichlet polynomial `M_T` such that

```text
integral_(Omega_T)|1-zeta(s)M_T(s)|^2dA(s)<pi*10^(-6),  (1.6)
```

then zeta has no zero with `beta>=0.99` at sufficiently large height.  The
finitely many remaining zeros are bounded a positive distance from one, so
(1.6) implies some fixed uniform zero-free strip.  If the low range is
separately checked at the same line, it implies the line `beta<0.99` itself.

The use of area, rather than one vertical line, is essential.  A point has
zero one-dimensional measure; an analytic function taking the value one at
the centre of a fixed disc has a fixed positive area cost.

## 2. The natural barely super-conductor mollifier

Take

```text
theta=1.03,       X=floor(T^theta),
M_X(s)=sum_(d<=X)mu(d)d^(-s),
D_X(s)=sum_(m<=X)m^(-s).                               (2.1)
```

The relevant finite product is

```text
D_X(s)M_X(s)=sum_(n<=X^2)c_X(n)n^(-s),
c_X(n)=sum_(d|n; d<=X; n/d<=X)mu(d).                   (2.2)
```

The complete divisor identity gives

```text
c_X(1)=1,
c_X(n)=0                 (2<=n<=X),
|c_X(n)|<=tau(n)          (X<n<=X^2).                  (2.3)
```

Thus

```text
1-D_X(s)M_X(s)=-sum_(X<n<=X^2)c_X(n)n^(-s).            (2.4)
```

This exact deletion through `X`, rather than an assumed cancellation of
Möbius sums, is why a length just beyond `T` is the natural threshold.

## 3. The long zeta truncation is legitimate in area

For a fixed integer `K>=1`, Euler--Maclaurin gives uniformly on `Omega_T`

```text
zeta(s)=D_X(s)+X^(1-s)/(s-1)-X^(-s)/2
 +sum_(1<=k<=K) [B_(2k)/(2k)!](s)_(2k-1)X^(-s-2k+1)
 +R_K(s),                                                  (3.1)

|R_K(s)| <<_K (1+|s|)^(2K)X^(1-sigma-2K).                 (3.2)
```

Changing an endpoint convention changes only one displayed endpoint term
and not any exponent below.  The trivial bound, uniform in the thin box, is

```text
|M_X(s)| << X^(1-sigma_-)*log X.                         (3.3)
```

The first two corrections in (3.1), after multiplication by `M_X`, have
squared area respectively

```text
<<T^[-1+4*theta*(1-sigma_-)+o(1)]
  =T^(-0.95468+o(1)),                                    (3.4)

<<T^[1+2*theta*(1-2*sigma_-)+o(1)]
  =T^(-1.01468+o(1)).                                    (3.5)
```

The `k`-th Bernoulli term has squared-area exponent

```text
4k-1+4*theta*(1-sigma_--k)
 =-0.95468-0.12k,                                        (3.6)
```

and is therefore harmless.  From (3.2), the squared-area exponent of the
remainder times `M_X` is

```text
1+4K*(1-theta)+4*theta*(1-sigma_-).                      (3.7)
```

For `K=9`, (3.7) equals

```text
1-1.08+0.04532=-0.03468.                                (3.8)
```

Consequently

```text
norm_(L2[Omega_T])((zeta-D_X)M_X)=o(1).                 (3.9)
```

In particular, a proof that the polynomial in (2.4) has `L2(Omega_T)` norm
`o(1)` would prove (1.6).  The analytic conductor does not forbid the long
truncation: sufficiently many fixed Euler--Maclaurin terms make it rigorous.
The obstruction occurs in the near frequencies of the product polynomial.

## 4. Exact diagonal: it already has the needed saving

For positive integers `m,n`, define

```text
A_(m,n)=integral_(sigma_-)^(sigma_+)(mn)^(-sigma)d sigma
       =[(mn)^(-sigma_-)-(mn)^(-sigma_+)]/log(mn),       (4.1)

B_(m,n)=integral_(T-r)^(2T+r)exp[it log(n/m)]dt.         (4.2)
```

The exact polynomial area is

```text
P_T=sum_(X<m,n<=X^2)c_X(m)c_X(n)A_(m,n)B_(m,n).          (4.3)
```

The diagonal part is

```text
D_T=(T+2r)sum_(X<n<=X^2)c_X(n)^2
       [n^(-2sigma_-)-n^(-2sigma_+)]/(2log n).           (4.4)
```

Using `|c_X(n)|<=tau(n)` and
`sum_(n<=u)tau(n)^2<<u(log u)^3`, partial summation gives

```text
D_T <<T X^(1-2sigma_-)(log X)^3
    =T^[1+1.03*(1-1.978)+o(1)]
    =T^(-0.00734+o(1))=o(1).                            (4.5)
```

Thus neither the exact product diagonal nor the Euler--Maclaurin completion
blocks the strip.  Write

```text
O_T=sum_(m!=n)c_X(m)c_X(n)A_(m,n)B_(m,n).                (4.6)
```

The one missing estimate is simply

```text
O_T=o(1).                                                (4.7)
```

It is a signed statement: `O_T` is real after pairing `(m,n)` and `(n,m)`.
Equations (1.5), (3.9), and (4.5) prove that (4.7), uniformly on dyadic
heights, gives a fixed zero-free strip.

## 5. The coefficient-blind near-product wall is a real power

The Montgomery--Vaughan/Hilbert inequality applied at each `sigma` gives

```text
|O_T| << integral_(sigma_-)^(sigma_+)
             sum_(X<n<=X^2)n |c_X(n)|^2 n^(-2sigma)d sigma

       <<X^[4(1-sigma_-)](log X)^O(1)
        =X^(0.044+o(1))
        =T^(0.04532+o(1)).                               (5.1)
```

The real-part integration contributes a logarithm but no power.  More
importantly, the exponent in (5.1) is not just an artefact of applying the
Hilbert inequality to an arbitrary sequence.

Let `P_X` be the primes in `[X/2,X]`.  If `p` and `q` are distinct members
of `P_X`, then the only admissible central divisors of `pq` in (2.2) are
`p` and `q`.  Hence

```text
c_X(pq)=mu(p)+mu(q)=-2.                                 (5.2)
```

There are `>>X^2/(log X)^2` distinct such semiprimes.  Partition
`[X^2/4,X^2]` into intervals of length

```text
w=X^2/(100T).                                            (5.3)
```

There are `O(T)` intervals.  Cauchy--Schwarz, followed by
`sum_b binom(N_b,2)`, shows that the number of distinct pairs of these
semiprimes lying in a common interval is

```text
>>X^4/[T(log X)^4].                                      (5.4)
```

For every pair `m<n` counted by (5.4),

```text
0<log(n/m)<1/(20T).                                      (5.5)
```

After slightly enlarging the harmless numerical constant in (5.3), (5.5)
implies

```text
Re B_(m,n)>=cT.                                          (5.6)
```

Moreover, integration over the first `1/log X` of the sigma interval gives

```text
A_(m,n)>=c X^(-4sigma_-)/log X.                          (5.7)
```

All coefficients in this restricted block have the same sign.  Its
positive contribution, and hence the absolute kernel mass of the complete
offdiagonal, is at least

```text
X^4/[T(log X)^4] * T * X^(-4sigma_-)/log X
 >>X^[4(1-sigma_-)]/(log X)^5
  =X^0.044/(log X)^5.                                   (5.8)
```

This matches the power in (5.1).  Sigma averaging has not crossed the
frequency-resolution barrier.  Any proof based on taking absolute values,
bounding rows independently, or retaining only coefficient squares must
pay a fixed positive power.

Equation (5.8) is **not** a lower bound for the full signed `O_T`: other
coefficient blocks can cancel the displayed semiprime block.  It proves
that precisely such cancellation is necessary.  The open target (4.7) is
therefore a concrete signed near-product theorem for the actual coefficients

```text
c_X=1_(<=X) * mu_(<=X),                                 (5.9)
```

at multiplicative resolution `1/T`, where `X=T^1.03`.  It is an averaged
quadratic target, but it carries a fixed-power arithmetic demand and is not
provided by generic mean values.

## 6. Independent audit: high derivatives of `1/zeta`

There is a second apparently attractive way to remove the pole and gamma
costs.  In `Re s>1`, put `F(s)=1/zeta(s)`.  For every integer `m>=0`,

```text
F^(m)(a+it)=(-1)^m sum_(n>=1)mu(n)(log n)^m n^(-a-it),
a>1.                                                      (6.1)
```

The Dirichlet mean-value theorem gives, on every fixed ordinate interval,

```text
integral |F^(m)(a+it)|^2dt
 <<H A_m(a)+B_m(a),                                      (6.2)

A_m(a)=sum mu(n)^2(log n)^(2m)n^(-2a),
B_m(a)=sum n mu(n)^2(log n)^(2m)n^(-2a).                 (6.3)
```

Integral comparison yields, up to factors with `m`-th root one,

```text
A_m(a)<=(2m)!/(2a-1)^(2m+1),
B_m(a)<=(2m)!/(2a-2)^(2m+1).                             (6.4)
```

The diagonal `A_m` alone would have normalized derivative radius
`a-1/2`.  The frequency-gap error `B_m` has radius only `a-1`.

To make this exact, centre at `s_0=a+i gamma`, apply the subharmonic
mean-value inequality to `F^(m)` in a disc of radius `epsilon<a-1`, and use
(6.2) on the containing fixed ordinate interval.  Stirling's formula gives

```text
limsup_(m->infinity)
 [|F^(m)(s_0)|/m!]^(1/m)
 <=1/(a-epsilon-1).                                     (6.5)
```

Letting `epsilon` tend to zero shows that the Taylor radius furnished by
this argument is only

```text
R(s_0)>=a-1.                                             (6.6)
```

If a zeta zero `beta+i gamma` is present, `F` has a pole at horizontal
distance `a-beta`.  Comparing with (6.6) yields only `beta<=1`, already
known from the Euler product.  Multiplicity and the size of `1/zeta'(rho)`
do not matter here: the Taylor-radius argument detects a pole without a
residue lower bound.  There is also no zeta-pole or gamma main term.  The
entire loss is the offdiagonal frequency-gap term in (6.2).

The exact conditional upgrade is informative.  If the `B_m` term in (6.2)
could be replaced, uniformly in `m`, by

```text
sum n^(1-eta)mu(n)^2(log n)^(2m)n^(-2a)                 (6.7)
```

for some fixed `eta>0` (or by a signed estimate with the same exponential
scale), then (6.5) would become

```text
R(s_0)>=a-1+eta/2,                                      (6.8)
```

and every zeta zero would satisfy

```text
beta<=1-eta/2.                                          (6.9)
```

Thus reciprocal high derivatives do formulate a strip as a fixed power
improvement in one local mean value, but the standard mean theorem lands
exactly at `eta=0`.  This is the reciprocal analogue of the
super-conductor wall in Sections 4--5.

## 7. Research verdict

The Bergman construction is a genuinely different zero detector from the
candidate-relative Pick and Mertens-increment routes.  It has three useful
features:

1. the target zero contributes the coefficient-free value `E_M(rho)=1`;
2. area subharmonicity turns one zero into a fixed positive norm cost;
3. at `0.99`, both the natural diagonal and analytic-completion errors are
   already power-saved with the modest length `X=T^1.03`.

Its remaining estimate is nevertheless a fixed-power signed arithmetic
correlation.  The semiprime theorem (5.8) proves that no absolute-value
implementation can close it.  The next admissible attack is narrowly
specified: estimate the complete signed form (4.6), retaining cancellation
between the semiprime block and the other central-divisor blocks.  Until
that estimate is proved, neither this route nor the reciprocal-jet route
gives a uniform strip.
