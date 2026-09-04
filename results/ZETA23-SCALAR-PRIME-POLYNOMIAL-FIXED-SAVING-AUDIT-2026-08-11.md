# Transition-scale scalar prime polynomial: a logarithmic theorem and the fixed-saving obstruction

Status: focused arithmetic audit, 2026-08-11.  A uniform logarithmic saving
for the exact sharp scalar polynomials is proved below from a published
pointwise prime-twist estimate.  No fixed power saving, Pick lower edge,
carrier margin, or zero-free strip is proved.

## 1. Verdict

Put

```text
Z_X(t)=sum_(n<=X) Lambda(n)n^(-1/2+it),
A_X(t)=Im Z_X(t),
D_X(t)=sum_(n<=X) Lambda(n)n^(-1/2)
                    *(L-log n)cos(t log n),
L=log X.                                                (1.1)
```

For every fixed `C>0`, uniformly when

```text
T*(log T)^(-C) <= X <= T*(log T)^C,
T <= abs(t) <= 2T,                                     (1.2)
```

one has the unconditional sharp-endpoint estimate

```text
abs Z_X(t) <<_C sqrt(X)/(log X)^(3/10),
abs D_X(t)/L <<_C sqrt(X)/(log X)^(13/10).              (1.3)
```

Consequently, on every critical grid,

```text
B_X(T):=osc_k A_X(tau_k)+(2/L)*max_k abs D_X(tau_k)
       <<_C sqrt(X)/(log X)^(3/10).                     (1.4)
```

This is a genuine pointwise gain over the absolute-value bound, but its
power exponent is

```text
1/2-(3/10)*loglog(X)/log(X) -> 1/2.                    (1.5)
```

It therefore does not give `B_X=o(X^alpha)` for any fixed
`alpha<1/2`.

More importantly, even such a bare scalar estimate would have to be matched
to the **actual signed carrier margin**.  In the normalization of the
quantitative carrier report, write

```text
K=(X^alpha/L)*r_T                                      (1.6)
```

for the normalized negative carrier edge.  The elementary Loewner estimate
gives a normalized prime error at most `B_X/L`, so the coupled condition is

```text
B_X=o(X^alpha*r_T).                                    (1.7)
```

The weaker statement `B_X=o(X^alpha)` is insufficient when `r_T` is allowed
to tend to zero without a power-scale lower bound.  Thus the two honest
routes are:

```text
(a) K >= X^(alpha-o(1))/L and a fixed-saving bound for B_X; or

(b) a direct constrained Pick-pencil lower bound whose complete prime,
    pole, archimedean, and remote-tail error is o(K) at the actual K.       (1.8)
```

The [quantitative carrier theorem card](ZETA23-QUANTITATIVE-SIGNED-CARRIER-REDUCTION-2026-08-11.md)
asks only for a margin large enough to beat
an exponentially tiny remote tail.  It does not prove the power-scale lower
bound in (1.8)(a).  The estimate (1.4) is therefore not useful at the
scale allowed by the current Schur information, even before the
fixed-exponent mismatch is considered.

## 2. A published sharp-twist estimate gives (1.3)

The required input is Lemma 7.9 and Remark 7.2 of Klurman--Mangerel--
Teravainen, *Multiplicative functions in short arithmetic progressions*.
Specialized to the principal character and the sharp weight, it says the
following.  If `y>=10`,

```text
abs(t) <= y^[(log y)^(1/25)],                           (2.1)
```

then, for every `epsilon in (0,1)`,

```text
S(y,t):=sum_(n<=y) Lambda(n)n^(it)

abs S(y,t)
 << epsilon*log(1/epsilon)^3*y
    +y/(log y)^(3/10)+y/(1+abs(t)).                    (2.2)
```

The last denominator is `1+t^2` for a fixed smooth weight and becomes
`1+abs(t)` for the sharp endpoint.  Choosing
`epsilon=(log y)^(-2/5)` absorbs the first term into the second for large
`y`.  The source uses `n^(-it)`; complex conjugation gives (2.2) with the
displayed sign.

Primary source:
[Klurman--Mangerel--Teravainen, Lemma 7.9 and Remark 7.2](https://doi.org/10.1112/plms.12546).

### Proposition 2.1 (exact transition-scale consequence)

Under (1.2), (1.3) holds.

#### Proof

Set

```text
Y_0=exp[(log(2T))^(25/26)].                            (2.3)
```

Then

```text
Y_0^[(log Y_0)^(1/25)]=2T.                            (2.4)
```

Thus (2.2), with `epsilon=(log y)^(-2/5)`, applies
uniformly for `Y_0<=y<=X` and `T<=abs(t)<=2T`:

```text
S(y,t)<<y/(log y)^(3/10)+y/T.                         (2.5)
```

For `y<Y_0`, Chebyshev's bound gives `S(y,t)<<y`.
Exact Abel summation, with the endpoint `n=X` included, gives

```text
Z_X(t)
 =X^(-1/2)S(X,t)+(1/2)*integral_1^X S(y,t)y^(-3/2)dy. (2.6)
```

Split the integral at `Y_0` and then at `sqrt(X)`.  Equations
(2.5)--(2.6) give

```text
abs Z_X(t)
 << sqrt(X)/(log X)^(3/10)+sqrt(X)/T+sqrt(Y_0).        (2.7)
```

In (1.2), `sqrt(Y_0)=T^o(1)` and the last two terms are absorbed by
the first.

There is also the exact identity

```text
D_X(t)=Re integral_1^X Z_y(t)dy/y.                    (2.8)
```

Indeed, the contribution of one `n` to the integral is
`Lambda(n)n^(-1/2+it) integral_n^X dy/y`, including the zero weight
when `n=X`.  Applying (2.7) with `X` replaced by `y`, using the trivial
bound below `Y_0`, and splitting once more at `sqrt(X)`, yields

```text
abs D_X(t)
 << sqrt(X)/(log X)^(3/10)+sqrt(X)/T+T^o(1).           (2.9)
```

Division by `L` proves the second assertion of (1.3).  Finally
`osc A_X<=2 sup abs Z_X`, proving (1.4).  QED

This proof uses the complete von Mangoldt sum.  It does not discard a
Vaughan head, a cofactor, a prime power, or a sharp endpoint.

### 2.1. Fixed zero-free strips: one implication, not an equivalence

There is a rigorous one-way comparison with zeros.  Fix `delta>0` and
suppose, apart from at most finitely many low zeros,

```text
zeta(s)!=0                 for Re(s)>1-delta.          (2.10)
```

Then, for every fixed `C>0` and `epsilon>0`, uniformly in (1.2),

```text
abs Z_X(t)+abs D_X(t)/L
       <<_(C,delta,epsilon) X^(1/2-delta+epsilon),     (2.11)

B_X(T)<<_(C,delta,epsilon) X^(1/2-delta+epsilon).     (2.12)
```

Indeed, truncated Perron inversion and its logarithmically smoothed version
are

```text
Z_X(t)=1/(2*pi*i) integral
       -zeta'/zeta(1/2+s-it)*X^s ds/s,

sum_(n<=X) Lambda(n)n^(-1/2+it)*log(X/n)
       =1/(2*pi*i) integral
       -zeta'/zeta(1/2+s-it)*X^s ds/s^2.              (2.13)
```

Shift from `Re(s)>1/2` to
`Re(s)=1/2-delta+epsilon`.  Condition (2.10) leaves no high zero pole in
the crossed strip, and the standard partial-fraction bound for
`zeta'/zeta` on the new line costs only powers of `log(XT)`.  The zeta pole
contributes respectively

```text
X^(1/2+it)/(1/2+it),
X^(1/2+it)/(1/2+it)^2,
```

which are negligible for `abs(t) asymp X`; residues of finitely many low
exceptional zeros have the same harmless large denominator.  This proves
(2.11), with logarithms absorbed into `X^epsilon`, and (2.12) follows from
`osc A_X<=2 sup abs Z_X`.  For a fixed smooth cutoff the contour shift is
immediate from rapid Mellin decay.  For the sharp cutoff in (1.1), one must
use truncated Perron, choose horizontal heights away from zeros, and account
for a possible endpoint term `Lambda(X)/sqrt(X)`; these change only
logarithmic factors.  Thus a fixed zero-free strip gives a fixed-power scalar
bound even at the sharp endpoint.

The converse is **not** supplied by the repository target.  The relevant
known benchmark is Turan's stronger localization criterion, reproduced at
the start of [Weber, *Local Suprema of Dirichlet Polynomials and Zerofree
Regions of the Riemann Zeta-Function*](https://arxiv.org/abs/1005.3932).
For fixed `D>0`, `0<E<=9/10`, and `0<beta<1`, it assumes, throughout

```text
T-T^E <= tau <= T+T^E,

T^(D*(1-beta^(1/6))) <= N <= N_1 < N_2 <= 2*N
                      <= T^(D*(1+beta^(1/6))),        (2.14)
```

the complex prime-interval estimate

```text
abs sum_(N_1<=p<=N_2) p^(-i*tau)
       <= c*N*(log N)^10/tau^beta.                   (2.15)
```

Its conclusion is a zero-free parallelogram

```text
Re(s)>1-beta^2,       T-T^E<=Im(s)<=T+T^E.           (2.16)
```

Consequently, a complex fixed-power estimate `N^(1-eta)` uniform over the
whole power-wide family (2.14) really does imply a fixed strip: choose
`beta>0` small enough that

```text
beta < eta*D*(1-beta^(1/6)).                          (2.17)
```

A complex von-Mangoldt estimate of size `N^(1/2-eta)` on every such
interval gives (2.15), up to logarithms and harmless prime powers, by
partial summation.

The scalar target (1.4) is missing three hypotheses in this criterion.
First, it gives the imaginary part of one sharp prefix and the real part of
one logarithmic Cesaro sum, not every complex interval sum; exactly

```text
D_X(t)=L*Re Z_X(t)-A_X'(t),                           (2.18)
```

and critical-grid values of `A_X` do not stably control `A_X'`.  At the
sampling step `2*pi/L`, an endpoint frequency `exp(i*L*t)` is constant on
the grid while its `D_X` multiplier is zero.  Second, (1.4) is discrete,
whereas (2.15) is continuous in `tau` on a full local window.  Third,
`X=T*(log T)^O(1)` is only a polylogarithmic transition band, whereas
(2.14) requires a fixed power-wide family of lengths and all subinterval
endpoints.  Smoothing helps the strip-to-sum contour shift but does not
restore these missing converse data.  Proving that the particular
arithmetic pair `(A_X,D_X)` nevertheless overcomes them would itself be a
new discrete confluent localization theorem; no such implication is used
or proved here.

## 3. The oscillation does not hide a large constant grid mode

The Loewner bound naturally contains `osc_k A_X`, rather than
`max_k abs A_X`.  At the transition scale the difference is harmless for a
deterministic reason, independently of Proposition 2.1.

Let

```text
h=2*pi/L,
tau_k=tau_0+k*h,       0<=k<d,
d=floor(T/h),
Zbar=d^(-1)*sum_(k<d) Z_X(tau_k).                     (3.1)
```

For `y=log n`, the geometric average multiplying the `n`-th coefficient is

```text
G_d(y)=d^(-1)*sum_(k<d)exp(i*k*h*y),

abs G_d(y)
 <=min(1,1/[d*abs sin(pi*y/L)])
 <<min(1,1/[T*min(y,L-y)]).                           (3.2)
```

Split the prime powers at `n=sqrt(X)` and split the upper half again at
`L-log n=1/T`.  Chebyshev's bound on the lower half and
`Lambda(n)<=L` on the upper half give

```text
abs Zbar
 << X^(1/4)/T + sqrt(X)*L^2/T + L/sqrt(X).            (3.3)
```

The last term includes the possible exact endpoint `n=X`; the short shell
`0<=L-log n<=1/T` is also included.  Hence `Zbar=o(1)` under (1.2).  Since
the real average of the numbers `A_X(tau_k)` lies between their minimum and
maximum,

```text
max_k abs A_X(tau_k)<=osc_k A_X(tau_k)+o(1).          (3.4)
```

Thus the scalar target cannot be satisfied merely by placing a large
constant imaginary mode on the grid.

## 4. Exact derivative pairing and center ledger

Differentiating (1.1) gives the exact confluent identity

```text
D_X(t)=Re[L*Z_X(t)+i*Z_X'(t)]
      =L*Re Z_X(t)-A_X'(t).                           (4.1)
```

This explains why the diagonal in the sharp Loewner matrix is independent
confluent data.  Critical-grid values of `A_X` alone do not control
`A_X'`: at Nyquist spacing a band-limited sine can vanish at every node and
have a large derivative there.  The `D_X` term restores precisely this
missing datum.  It is not an extra source of arithmetic cancellation.

The corresponding continuum center is completely explicit.  With
`a=1/2+it`,

```text
M_0(X,t)=integral_1^X x^(-1/2+it)dx
        =[exp(aL)-1]/a,

M_1(X,t)=integral_1^X x^(-1/2+it)(L-log x)dx
        =[exp(aL)-1-aL]/a^2.                          (4.2)
```

On (1.2),

```text
abs M_0 << sqrt(X)/T,
abs M_1 << sqrt(X)/T^2+L/T.                           (4.3)
```

So the pole center is negligible in the **original high-frequency scalar
coordinates**.  It may not be deleted before Vaughan completion, squaring,
Poisson summation, or conductor recombination: in those coordinates its
cross terms are part of the exact ordinary dual.

For comparison, a zero displacement parameter `z` is tested by the two
Mellin kernels

```text
K_0(z)=[exp(zL)-1]/z,
K_1(z)=[exp(zL)-1-zL]/z^2.                            (4.4)
```

At a matching ordinate `z=delta>0`, `K_0` is real, so its leading term can
be invisible to `A_X`; `K_1` is then real and is seen by `D_X`.  Dividing
`D_X` by `L` loses only a logarithm, not the power `X^delta`.  Formula
(4.4) is a response calculation, not a termwise zero lower bound: other
zeros can cancel, and the signed carrier is still needed.

## 5. Why completion-preserving Vaughan and Heath--Brown do not create a high-t power

The obstruction is exact separability, not a shortage of formal
decompositions.  On a rectangular Type-II block,

```text
B(t)=sum_(m~M,n~N) a_m*b_n*(mn)^(-1/2+it)

    =[sum_(m~M)a_m*m^(-1/2+it)]
     [sum_(n~N)b_n*n^(-1/2+it)].                      (5.1)
```

A smooth total-product cutoff is a Mellin superposition of (5.1).  Twisting

```text
a_m -> a_m*m^(it),       b_n -> b_n*n^(it)             (5.2)
```

preserves every coefficient norm.  Therefore a Type-II theorem uniform in
arbitrary coefficient phases gives exactly the same estimate at height `t`
as at height zero.  It cannot supply a high-frequency saving for this
phase.  The same statement holds in every arity because

```text
exp[it*log(m_1*...*m_j)]=product_r m_r^(it).           (5.3)
```

The derivative weight does not repair the degeneracy:

```text
L-log(mn)=L-log m-log n,                              (5.4)
```

so it produces only three separable tensors.  In differential language,
for `F(m,n)=t log(mn)`,

```text
partial_m partial_n F=0.                              (5.5)
```

Thus the mixed-curvature input behind ordinary bilinear stationary-phase
or dispersion estimates vanishes identically.

The one-variable stationary-phase dual is self-similar.  For

```text
f(x)=[t/(2*pi)]log x,
f'(x)=nu  iff  x=t/(2*pi*nu),                         (5.6)
```

the dual phase is

```text
exp{2*pi*i[f(x)-nu*x]}
 =constant(t)*nu^(-it).                               (5.7)
```

So the `B` process returns the same Archimedean character.  Endpoint terms
and the zero dual frequency are not errors; after all conductor classes are
restored they form the ordinary dual.

For fixed Vaughan cutoffs the coefficientwise identity is

```text
a_(U,V)+h_(U,V)=Lambda,

a_(U,V)=mu_(>U)*Lambda_(>V)*1,                        (5.8)

h_(U,V)=mu_(<=U)*log+Lambda_(<=V)
          -mu_(<=U)*Lambda_(<=V)*1.
```

The same cutoffs must be used at both endpoints when (2.8) or a scale
coboundary is formed.  Moving them while differentiating introduces cutoff
shells that belong to the heads in (5.8).  After full reciprocal/conductor
recompletion the coefficient is

```text
C=mu*Lambda=-mu*log,       C*1=Lambda.                (5.9)
```

Hence the complete ordinary dual is again the original prime field.  A
fixed power for the punctured nonzero reciprocal phases (such as the native
range of Wright's theorem) does not bound (5.9); the axes, heads, opposite
orientation, common-divisor sectors, and center restore it exactly.

This proves a precise method-level obstruction: any successful Vaughan or
Heath--Brown argument here must exploit cancellation in the actual
Mobius--prime coefficients **before** norm domination and must retain the
complete recombination.  Generic exponent-pair, coefficient-norm, or
nonzero-reciprocal estimates cannot prove the target.

## 6. Moment and base-height quantifiers

Write `X=T^(lambda+o(1))`.  For an even `p`, the unconditional diagonal
range for the `p`-th moment is

```text
lambda*p<2.                                           (6.1)
```

Even after the standard bandwidth/peak-width conversion, excluding one
grid-scale value of size `X^alpha` from a moment of bulk size
`T^(1+o(1))` requires

```text
alpha*lambda*p>1.                                     (6.2)
```

For `alpha<1/2`, (6.1)--(6.2) are disjoint.  At the transition endpoint
`lambda=1`, the boundary second moment still has `2alpha<1`.  Logarithmic
weights and (4.1) do not shorten the multiplicative product length.

There is a valid almost-all-base formulation, but it is stronger than a
mean theorem for ordinates.  A zero of ordinate `gamma` lies in `[T,2T]`
for every

```text
T in [gamma/2,gamma].                                 (6.3)
```

Thus it would suffice to have, outside an `o(Y)` set of **base heights** in
each dyadic base interval, the complete maximum bound

```text
max_(all grid k for that base T)
 [abs A_X(tau_k)+abs D_X(tau_k)/L] <= X^(alpha-sigma). (6.4)
```

Then some good base window contains any proposed large zero.  A theorem for
most ordinates, most pairs `(T,k)`, or an averaged matrix vector does not
imply (6.4): the exceptional coordinate and the minimizing Pick vector may
depend on `T`.  Conditions (6.1)--(6.2) quantify why the currently available
moments do not upgrade to the required maximum.

## 7. Pick-pencil disposition and the coupled theorem card

On the sharp critical grid the exact prime matrix is

```text
H_P=-2*diag(D_k)+(2/h)*(M_A*K_d-K_d*M_A),              (7.1)
```

and hence

```text
lambda_min(H_P)>=-2*max_k abs(D_k)-L*osc_k(A_k)
                =-L*B_X(T).                           (7.2)
```

After the `1/L^2` normalization and endpoint-jet compression, (7.2) becomes
the error `-B_X/L` used in (1.7).  Rank-two displacement does not improve
(7.2): signed smooth scalar multipliers realize arbitrary finite confluent
diagonals, and the signed Andreief minors retain prime products through
their full degree.  Any improvement must use the special arithmetic joint
law of `A_X,D_X`, not displacement rank alone.

The exact surviving alternatives are therefore:

```text
SCALAR/CARRIER ROUTE
  prove K >= X^(alpha-o(1))/L (or an explicit r_T=X^(-theta+o(1)));
  prove B_X <= X^(alpha-sigma+o(1)), with sigma>theta;
  bound every other normalized remainder by o(K).

DIRECT PICK ROUTE
  prove the constrained pencil is nonnegative at the actual Schur K,
  retaining D_X, the Hilbert commutator, all endpoint jets, pole and
  archimedean terms, and the remote tail in one inequality.              (7.3)
```

The logarithmic theorem (1.4) supplies neither line of (7.3).  It is the
strongest rigorous advance obtained in this scalar audit, and it confirms
that standard high-frequency prime-twist technology stops at
`X^(1/2-o(1))`, consistently with the completion and moment obstructions.

No prime lower edge, power-scale signed carrier, or zero-free strip is
claimed.
