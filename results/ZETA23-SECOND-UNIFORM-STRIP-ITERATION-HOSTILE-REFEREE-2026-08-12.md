# Second uniform-strip iteration: hostile referee audit

Status: **binary verdict -- NO STRIP PROVED**, 2026-08-12.

Audited reports:

1. `ZETA23-BERGMAN-RECIPROCAL-HYPERBOLA-AND-SIGNED-CANCELLATION-AUDIT-2026-08-12.md`;
2. `ZETA23-DYADIC-MERTENS-FORWARD-INVERSE-AND-DISPERSION-AUDIT-2026-08-12.md`;
3. `ZETA23-WIENER-EXTREMAL-SQUARE-ROOT-BARRIER-2026-08-12.md`.

The main identities and exponent calculations check after two local repairs:

- the exact Perron formula now uses the nonintegral cutoff `X_*=X+1/2`
  and treats the collision at `w=0` separately when `zeta(s)=0`;
- the Wiener construction now truncates at `H=Y^(1+eta)/4`, so its
  correction block `[2H,3H]` lies inside the theorem's stated aperture.

Neither repair changes a conclusion.  No report proves its final signed
fixed-power estimate, and no combination proves or enlarges a uniform
zero-free strip.

## 1. Bergman conductor recompletion

Let `Y=floor(T)`, `X=floor(T^1.03)`, and let
`sigma>=sigma_-=0.989`, `T-r<=abs(t)<=2T+r`.  Euler--Maclaurin between `Y`
and `X` is genuinely power-saving here.  With `K=C_0 log T`, its lower-end
ratio is

```text
(|t|+2K)/(2*pi*Y) <=1/pi+o(1)<1,
```

while the upper-end ratio is `T^(-0.03+o(1))`.  The Bernoulli bound therefore
makes the remainder smaller than any prescribed power, and the retained
lower endpoint terms form a convergent geometric sum.  Thus

```text
D_X(s)-D_Y(s)
 =[X^(1-s)-Y^(1-s)]/(1-s)+O(T^(-sigma)log^C T)
```

uniformly in the Bergman box.  Multiplication by the trivial bound

```text
|M_X(s)|<<X^(1-sigma_-+o(1))=T^(0.01133+o(1))
```

gives pointwise exponents `-0.97734` for the integral term and `-0.97767`
for the endpoint terms.  Squaring and integrating over ordinate length `T`
gives the stated

```text
||(D_X-D_Y)M_X||_2^2 <<T^(-0.95468+o(1)).
```

The coefficient-blind bounds

```text
||F_X||<<T^(0.02266+o(1)),
||G_(T,X)||<<T^(0.02233+o(1))
```

are much smaller than the reciprocal of this decay, so Cauchy--Schwarz
indeed upgrades the norm difference to

```text
||F_X||_2^2=||G_(T,X)||_2^2+o(1).
```

This conductor recompletion is rigorous.

## 2. Reciprocal-hyperbola coefficients and absolute walls

For

```text
G_(T,X)(s)=D_Y(s)M_X(s)-1=sum_(n>Y)b_(T,X)(n)n^(-s),
```

the coefficient identity

```text
b_(T,X)(n)=sum_(d|n; d<=X; n/d<=Y)mu(d)
```

is exact.  If `Y<n<=2Y`, then `X>2Y` and the admissibility condition removes
only `d=1` from the complete divisor sum.  Therefore

```text
b_(T,X)(n)=-1
```

throughout that full interval.  Its area-norm diagonal is consequently

```text
Delta_G >>T^(2-2sigma_-)/log T=T^0.022/log T.
```

Since the desired total norm is `o(1)`, its offdiagonal must have the
negative main term `-Delta_G+o(1)`; an estimate treating the offdiagonal as
a smaller error cannot suffice.

The mixed-semiprime calculation also checks.  For primes

```text
p in [X/2,X], q in [Y/2,Y],
```

only the representation `d=p`, `m=q` is admissible, so `b(pq)=-1`.  There
are `gg XY/(log X log Y)` distinct such products.  Binning them into `O(T)`
intervals at multiplicative resolution `1/T` and using the positive real
part of the ordinate kernel yields absolute same-sign mass

```text
gg (XY)^[2(1-sigma_-)]/log^5 T
 =T^[2*(1.03+1)*0.011+o(1)]
 =T^(0.04466+o(1)).
```

This is not a lower bound for the complete signed norm.  It correctly shows
that a proof must cancel fixed-power mixed near-products across other divisor
layers.

## 3. Perron and physical duals

For the integer cutoff `X`, exact Perron inversion requires a noninteger
threshold.  With `X_*=X+1/2`, the corrected formula is

```text
M_X(s)=1/(2*pi*i) integral_((c))
          X_*^w/[w zeta(s+w)]dw.
```

For `zeta(s)!=0`, multiplication by `zeta(s)` gives a residue one at `w=0`.
At a zeta zero, `w=0` collides with a denominator-zero singularity and the
residue cancellation is not uniform; the report now states this caveat.
Away from the collision, shifting left encounters `w=rho-s`, so a uniform
residue-free fixed shift already demands the desired zero-free information.

Partial summation independently gives the signed physical identity

```text
zeta(s)M_X(s)-1
 =zeta(s)[M(X)X^(-s)
          -s integral_X^infinity M(u)u^(-s-1)du].
```

The boundary and integral may cancel.  Bounding them separately would insert
a fixed-power Mertens estimate; retaining them together is exactly the
unresolved reciprocal-zeta mode.  The Perron, hyperbola, and physical
formulations are therefore equivalent coordinates, not three independent
savings.

## 4. Dyadic forward inverse

For `D(x)=M(x)-2M(x/2)`, iteration of
`D(2x)=M(2x)-2M(x)` and the prime number theorem give the exact forward
inverse

```text
M(x)=-sum_(j>=1)2^(-j)D(2^j x).
```

If

```text
integral_X^(2X)|D(x)|^2dx <<X^(3-delta),
```

then scaling a dyadic block and multiplying by `2^(-j)` gives the norm ratio

```text
2^(-j*delta/2).
```

Minkowski therefore proves the same-exponent bound for `M`.  Conversely,
the two terms in `D` give exactly the constant `1+2^(delta/2)` after scaling
the block `[X/2,X]`.  Thus, for every fixed `delta>0`, the two energy bounds
are equivalent.  In particular

```text
integral_X^(2X)|D(x)|^2dx <<X^2.98
```

is not a weaker high-pass problem; it is equivalent to ordinary Mertens
mean-square energy `<<X^2.98`.

The local coefficient formulas

```text
b(m)=mu(m), b(2m)=-3mu(m), b(4m)=2mu(m)
```

for odd `m` are correct.  Odd-squarefree density `4/pi^2` gives

```text
sum_(n<=Y)b(n)^2=(26/pi^2)Y+O(sqrt Y),
sum_(n<=Y)|b(n)|=(12/pi^2)Y+O(sqrt Y).
```

Partial summation against the exact triangular kernel then gives diagonal

```text
(39/pi^2)X^2+O(X^(3/2)),
```

whereas the ordered offdiagonal absolute mass on `m,n<=X` is at least

```text
(144/pi^4+o(1))X^3.
```

The Mellin--Plancherel identity and the boundary pole budget also check.  A
zero of multiplicity `m` on `Re(s)=q` contributes
`gg(sigma-q)^(1-2m)`.  The allowed energy growth is only
`O((sigma-q)^(-1))`, so the exponent alone excludes multiple boundary zeros
but not a simple boundary zero.  Zeros strictly to the right are excluded by
holomorphic continuation, conditional on the unproved energy estimate.

The short-interval literature is used with the correct polarity.  The
Matomaki--Radziwill power occurs in the exceptional-set cardinality while
the long mean is retained.  The Matomaki--Teravainen all-interval comparison
ends explicitly in a long Mobius sum plus a logarithmic error.  Neither gives
the missing fixed-power principal mean.

## 5. Wiener square-root construction

Under the report's stated unrestricted periodic Wiener-grid hypothesis, the
DFT mask construction is valid.  If `G` is the residue mask of `M` actual
integers modulo `Q asymp Y`, Parseval gives

```text
integral_0^Q|G(x)|^2dx=M.
```

After the change `x=Y exp(u)`, a fixed compact `u`-window therefore has

```text
||chi(u)G(Y exp(u))||_2 <<sqrt(M/Y).
```

The carrier of `q_infinity=chi(1-G(Y exp(u)))` is consequently
`b_0+O(sqrt(M/Y))`.  Bernstein plus the chain rule gives, for every fixed
`r`,

```text
||f^(r)||_2 <<_r Y^r sqrt(M/Y).
```

Parseval and weighted Cauchy--Schwarz then give total Wiener norm
`O(sqrt M)`.  Beyond `H=Y^(1+eta)/4`, the same calculation gives tail

```text
<<H^(1/2-r)Y^r sqrt(M/Y),
```

which is `O_A(Y^(-A))` after choosing one sufficiently large fixed `r`.
The logarithmic separation of distinct integer nodes makes the normalized
Gram row sum on `[2H,3H]`

```text
O(Y log(M+1)/H)=o(1).
```

Its inverse is bounded, and the minimal Hilbert correction has coefficient
`l^1` norm controlled by the node-error `l^2` norm.  It therefore restores
the nulls exactly without changing the carrier or the `O(sqrt M)` bill.
After normalization this proves only

```text
E_Y>>M^(-1/2)=Y^(-1/2+o(1)).
```

The direction is important and correct: a primal nuller proves a lower bound;
the von-Mangoldt dual quadrature proves the logarithmic upper bound.  The
strip ledger instead needs the much stronger lower bound

```text
E_Y>=Y^(-0.0180303234...+o(1)).
```

The construction does not provide it.  It also lives in the unrestricted
Wiener grid; extra endpoint-jet or prolate projections need not preserve the
factorization, as the report now states.

The chirp stationary-phase calculation is consistent: `asymp Y` Fourier
modes each have coefficient size `Y^(-1/2)`, giving Wiener norm
`asymp sqrt Y`.  Higher-moment diagonalization requires frequency length
`H>>Y^k` to resolve products near `Y^k`.  Since the physical aperture is
`Y^(50/33+o(1))<Y^2`, only `k=1` is available.  The report now scopes its
formal `sqrt(k/M)` improvement to the optimistic diffuse-prime diagonal;
it is not asserted as an all-coefficient theorem.

## 6. Combined verdict

The three reports do not supply complementary halves of one proof:

```text
Bergman recompletion     exact, but leaves complete signed Mertens tail;
dyadic high-pass         exactly invertible below cubic scale;
Wiener nuller            valid at square-root scale, wrong exponent;
fixed uniform strip      NOT PROVED.
```

The narrowest sufficient endpoint remains

```text
||D_Y(s)M_X(s)-1||_(L2(Omega_T))=o(1),
X=T^1.03,
```

equivalently a negative reciprocal-hyperbola offdiagonal main term cancelling
the growing `b(n)=-1` diagonal.  The clean alternative is the ordinary
Mertens energy bound `int_X^(2X)|M(x)|^2dx<<X^2.98`.  The Wiener theorem
does not approach either endpoint at the needed exponent.

```text
explicit delta>0 proved                    NO
known zero-free region improved            NO
new exact pruning/equivalence theorems      YES
remaining obstruction                      signed fixed-power arithmetic
```
