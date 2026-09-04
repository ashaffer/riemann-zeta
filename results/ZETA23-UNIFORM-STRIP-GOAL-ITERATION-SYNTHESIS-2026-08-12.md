# Uniform-strip goal iteration: exact collapses and surviving coefficient gates

Status: audited research synthesis, 2026-08-12.

**No fixed zero-free strip for the Riemann zeta function is proved in this
report.  No known unconditional zero-free region is improved.**  The purpose
of this iteration was to take the most favorable live reductions all the way
to their exact arithmetic endpoints, including an explicit arbitrarily thin
candidate strip.

The iteration produced four material conclusions.

1. A Bergman zero detector can be analytically completed with every diagonal
   and Euler--Maclaurin term power-saved, but conductor recompletion exposes a
   signed reciprocal hyperbola whose principal mode is a Mertens tail.
2. The dyadic high-pass `M(x)-2M(x/2)` is quantitatively equivalent, with the
   same power exponent, to ordinary Mertens mean-square cancellation.
3. Signed prime-log interpolation is cheap at point normalization, and an
   exact actual-node nuller exists at the square-root scale, but the required
   Laplace-carrier lower bound remains much larger and unproved.
4. Making the desired strip arbitrarily thin makes the excess exponent
   arbitrarily small, but known spectral estimates save only transverse
   modes.  The omitted zero mode is exactly the reciprocal/Mertens mode.

Two prior independent hostile audits checked the displayed implications and
constants.  Neither found a route from the proved statements to a strip.

## 1. The fixed target and truth boundary

For concreteness, the first Bergman implementation targeted

```text
Re rho < 0.99.                                                   (1.1)
```

If `rho` is a zero in a dyadic ordinate interval and `M` is any Dirichlet
polynomial, then

```text
E_M(s)=1-zeta(s)M(s),             E_M(rho)=1.                    (1.2)
```

A fixed disc around `rho` and subharmonicity therefore give a
coefficient-independent positive lower bound for the local area norm of
`E_M`.  Thus a uniform `o(1)` upper bound for a suitable mollifier excludes
every zero in the target strip, not merely almost all zeros.

This implication is exact.  What is not proved is the signed arithmetic
upper bound for that norm.

## 2. Bergman completion and the reciprocal hyperbola

For the `0.99` calibration, take

```text
sigma_-=0.989,          X=T^1.03,
M_X(s)=sum_(d<=X) mu(d)d^(-s),
D_X(s)=sum_(m<=X) m^(-s).                                      (2.1)
```

The product coefficients

```text
c_X(n)=sum_(d|n; d<=X; n/d<=X)mu(d)                            (2.2)
```

vanish for `2<=n<=X`.  The exact polynomial diagonal is

```text
O(T^(-0.00734+o(1))),                                          (2.3)
```

and nine Euler--Maclaurin terms make the analytic-completion remainder
`O(T^(-0.03468+o(1)))` in squared area norm.

Put `Y=floor(T)`.  Recompleting the unweighted factor at the conductor gives
the sharper exact identity

```text
D_X M_X-1 = D_Y M_X-1+o_(L2)(1),

D_Y(s)M_X(s)-1
 =sum_(m<=Y)m^(-s) sum_(Y/m<d<=X)mu(d)d^(-s).                  (2.4)
```

The squared recompletion error is

```text
O(T^(-0.95468+o(1))).                                         (2.5)
```

This removes an artificial high--high presentation, but it does not make the
norm diagonally small.  If `b_(T,X)(n)` denotes the coefficients in (2.4),
then complete divisor cancellation gives

```text
b_(T,X)(n)=-1                 (Y<n<=2Y).                       (2.6)
```

Consequently the conductor-block diagonal alone is

```text
>>T^0.022/log T.                                               (2.7)
```

The required theorem is therefore a signed asymptotic

```text
OffDiag=-Diagonal+o(1),                                       (2.8)
```

not an off-diagonal error estimate.  Mixed semiprimes at the two cutoff
scales retain absolute kernel mass `T^(0.04466+o(1))`.  Poisson or Perron
recompletion identifies the missing principal term as either

```text
integral u^(-s)
  [sum_(u/Y<d<=min(u,X))mu(d)/d]du                             (2.9)
```

or the denominator poles of `zeta(s)/zeta(s+w)`.  These are the physical and
Mellin versions of the same signed Mertens obstruction.

## 3. The dyadic high-pass has an exact stable inverse

Put

```text
D(x)=M(x)-2M(x/2),
m(u)=e^(-u)M(e^u),
d(u)=e^(-u)D(e^u),
L=log 2.                                                       (3.1)
```

Then

```text
d(u)=m(u)-m(u-L).                                             (3.2)
```

The prime number theorem gives `m(u+kL)->0`.  Hence (3.2) has the forward
stable inverse

```text
m(u)=-sum_(j>=1)d(u+jL).                                      (3.3)
```

Minkowski's inequality and the resulting geometric series prove, for every
fixed `delta>0`,

```text
integral_X^(2X)|D(x)|^2dx << X^(3-delta)

    if and only if

integral_X^(2X)|M(x)|^2dx <<_delta X^(3-delta).                (3.4)
```

Thus the apparently favorable high-pass estimate does not improve the power
threshold.  Its Mellin multiplier removes the literal linear mode, but the
PNT boundary condition reconstructs that mode at all later dyadic scales.

## 4. Exact signed nulling and the Wiener carrier

For active prime-power offsets `u_j=log(n_j/Y)`, the correctly normalized
extremal is

```text
E_Y=sup {abs(sum_k b(xi_k)h_k):
         sum_k h_k exp(i xi_k u_j)=0 for all j,
         sum_k abs(h_k)<=1}.                                  (4.1)
```

Finite quotient duality gives

```text
E_Y=inf_lambda max_k
  abs(b(xi_k)-sum_j lambda_j exp(i xi_k u_j)).                  (4.2)
```

The iteration proved an exact actual-node construction.  A discrete Fourier
mask on the active integers, compact localization, truncation below the
available aperture, and a high-frequency Gram correction give a finite
nuller with

```text
carrier          >>1,
Wiener norm      O(sqrt(M)),
M                =Y^(1+o(1))/log Y.                             (4.3)
```

Therefore

```text
E_Y>>M^(-1/2)=Y^(-1/2+o(1)).                                  (4.4)
```

The all-integer chirp

```text
1-exp(2*pi*i*Y*exp(u))                                        (4.5)
```

vanishes at every integer-log node and has order-one unnormalized carrier,
but stationary phase proves that its compact Wiener norm is asymptotic to
`sqrt(Y)`.  It therefore lands at the same square-root scale.

The strip ledger requires the much stronger lower bound

```text
E_Y>=Y^(-kappa+o(1)),        kappa<0.0180303234... .            (4.6)
```

No such lower bound was proved.  The full aperture is only
`Y^(50/33+o(1))`, so a fourth-moment separation at scale `Y^2` is already
unavailable.  Even an optimistic diffuse-prime `2k`-th moment gives only
`sqrt(k/M)`;
reaching (4.6) by that route needs `k=M^(0.963939...+o(1))`.

## 5. Arbitrarily thin strips and the spectral zero mode

Let the desired right edge be `1-delta`, take disc radius `r`, and write

```text
lambda=delta+r,             sigma_-=1-lambda.                    (5.1)
```

For `X=T^theta`, strict inequality in

```text
theta>1/(1-2lambda)=1+2lambda+O(lambda^2).                       (5.2)
```

is sufficient for the deleted-product diagonal to be `o(1)`, while the
matching coefficient lower bound rules out `theta` below this threshold.
The equality case is not decided by the displayed logarithmic bounds and is
not used here.

An explicit calibration is

```text
delta=10^(-6),       r=10^(-12),       theta=1+3*10^(-6).       (5.3)
```

It gives

```text
deleted-product diagonal      T^(-0.999992*10^(-6)+o(1)),
absolute off-diagonal wall    T^(4.000016*10^(-6)+o(1)).        (5.4)
```

All Euler--Maclaurin terms are `o(1)` with a sufficiently large fixed order.
Thus a complete spectral saving `T^(-kappa)` would indeed prove a strip once
`delta<kappa/8`.

The difficulty is qualitative rather than numerical.  Kuznetsov,
Kloosterman, exponent-pair, and large-sieve estimates save nonzero or
transverse modes.  Conductor recompletion leaves (2.6), so its zero mode must
produce the full negative main term (2.8).  In physical variables this is a
uniform Mobius sum on intervals of length

```text
H=X/T=T^(3*delta),                                             (5.5)
```

and in Mellin variables it is the pole divisor of
`zeta(s)/zeta(s+w)`.  Positive ordinate smoothing has nonzero mass at
frequency zero; mollifier smoothing must retain Mellin residue one in order
to cancel the constant coefficient.  Setting either quantity to zero also
deletes the zero detector.  Known spectral savings therefore do not apply to
the one mode that matters.

## 6. Independent Xi-kernel pruning

The exact theta kernel remains a possible coefficient-specific source, but
qualitative Fourier shape is insufficient.  There are even, positive,
real-analytic, strictly log-concave kernels with

```text
log h(u)=-pi*exp(4|u|)+O(u^2),                                  (6.1)
```

the corresponding functional-equation symmetry, and arbitrarily displaced
transform zeros.  Hence positivity, strict log-concavity, the leading Xi
tail, and the other listed qualitative shape data cannot prove a fixed
horizontal strip.  A successful Fourier-kernel route must use the exact
theta arithmetic in a quantitative shifted Hermite--Biehler inequality.

## 7. What is actually left

The iteration does not leave a coefficient-blind analytic estimate.  The
remaining statements are genuinely arithmetic:

1. prove the complete signed reciprocal-hyperbola asymptotic (2.8), including
   its zero frequency;
2. prove the large lower bound (4.6) for the actual prime-log Wiener
   quotient, not merely a frame or point-normalized interpolation bound; or
3. prove an exact theta-arithmetic shifted Hermite--Biehler inequality for
   some shift below one half.

The first endpoint is the narrowest direct sufficient statement, but (2.9)
shows why it has fixed-strip strength.  The second is a more geometric
adapter and still needs the rest of the completed-form ledger.  The third is
independent in presentation but cannot follow from generic kernel shape.

## 8. Binary conclusion

```text
explicit fixed delta proved                         NO
known zero-free region improved                     NO
Bergman analytic/diagonal completion                YES
conductor reciprocal-hyperbola identity             YES
dyadic high-pass exponent improvement               NO -- exact equivalence
actual-node signed nuller                            YES, square-root only
tiny-delta spectral closure                         NO -- principal mode
generic Xi shape closure                            NO -- countermodel
remaining obstruction                               signed arithmetic
```

Primary iteration artifacts:

- `ZETA23-BERGMAN-SUPERCONDUCTOR-MOLLIFIER-AND-RECIPROCAL-JET-GATE-2026-08-12.md`;
- `ZETA23-BERGMAN-RECIPROCAL-HYPERBOLA-AND-SIGNED-CANCELLATION-AUDIT-2026-08-12.md`;
- `ZETA23-DYADIC-MERTENS-FORWARD-INVERSE-AND-DISPERSION-AUDIT-2026-08-12.md`;
- `ZETA23-SIGNED-HEIGHT-FILTER-LAPLACE-CARRIER-GATE-2026-08-12.md`;
- `ZETA23-WIENER-EXTREMAL-SQUARE-ROOT-BARRIER-2026-08-12.md`;
- `ZETA23-TINY-DELTA-BERGMAN-SPECTRAL-MOLLIFIER-AUDIT-2026-08-12.md`;
- `ZETA23-XI-FOURIER-KERNEL-STRIP-NOGO-2026-08-12.md`;
- `ZETA23-UNIFORM-STRIP-ITERATION-HOSTILE-REFEREE-2026-08-12.md`;
- `ZETA23-SECOND-UNIFORM-STRIP-ITERATION-HOSTILE-REFEREE-2026-08-12.md`.
