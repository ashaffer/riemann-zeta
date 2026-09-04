# Uniform-strip goal iteration: final hostile referee audit

Status: **binary verdict -- NO STRIP PROVED**, 2026-08-12.

This audit covers:

- `ZETA23-TINY-DELTA-BERGMAN-SPECTRAL-MOLLIFIER-AUDIT-2026-08-12.md`;
- `ZETA23-UNIFORM-STRIP-GOAL-ITERATION-SYNTHESIS-2026-08-12.md`.

The tiny-delta calculation is a valid conditional optimization: if one had a
fixed saving for the complete signed form, then choosing a sufficiently small
fixed `delta` would convert it into a uniform strip.  No cited theorem supplies
that saving.  The complete principal Mobius mode remains unestimated, so the
conditional does not fire.

## 1. Zero detector and logical direction

For `beta>=1-delta`, disc radius `r`, and

```text
sigma_-=1-delta-r, sigma_+=1+r,
```

the radius-`r` disc about a nontrivial zero is contained in the Bergman box.
At that zero `1-zeta M=1`, so the subharmonic mean inequality gives area at
least `pi*r^2`.  Since `delta` and `r` are fixed, this is a positive constant
independent of height.  Therefore a uniform `o(1)` area upper bound on every
dyadic height interval is sufficient to exclude all sufficiently high zeros
in the proposed region.  Finite low height then gives some positive strip,
or the same explicit strip after a finite verification.

The converse is not claimed.  In particular, diagonal power saving and
analytic completion are only components of the required upper bound; neither
alone is a zero-free theorem.

## 2. Deleted-product diagonal threshold

With `lambda=delta+r`, `sigma_-=1-lambda`, and `X=T^theta`, the divisor-bound
upper estimate has power

```text
T X^(1-2sigma_-)=T^[1-theta+2lambda*theta].
```

Thus

```text
theta>1/(1-2lambda)
```

is sufficient for a power-saved diagonal.  The coefficients
`c_X(2p)=-2` for primes `X/2<p<=X` give a matching lower power and rule out
`theta<1/(1-2lambda)`.  They do not decide equality because the lower bound
contains negative powers of `log X`.  Both audited reports were patched to
distinguish the sufficient strict inequality, the impossible lower range, and
the unresolved equality case.  This equality issue does not affect the
explicit strict calibration.

## 3. Explicit exponent and Euler--Maclaurin audit

For

```text
delta=10^(-6), r=10^(-12), lambda=delta+r,
theta=1+3*10^(-6),
```

exact decimal arithmetic gives

```text
1/(1-2lambda)                 =1.000002000006000016...,
theta-threshold               =0.999993999984...*10^(-6),
diagonal exponent             =-0.999991999994...*10^(-6),
absolute offdiagonal exponent = 4.000016000012...*10^(-6).
```

The explicit mollifier therefore lies strictly on the power-saved side of
the diagonal threshold.

The large Euler--Maclaurin order is legitimate.  It is not allowed to grow
with `T`; here `K=100000` is enormous but fixed once `delta` is fixed.  The
squared-area exponents are

```text
integral correction       -1+4theta lambda,
k-th Bernoulli term       4k-1+4theta(lambda-k),
K-th remainder            1+4K(1-theta)+4theta lambda.
```

At the displayed calibration these are, respectively,

```text
-0.999995999984...,
-0.999995999984...-0.000012 k,
-0.199995999984...             (K=100000).
```

All are strictly negative.  The constants may depend astronomically on the
fixed `K`, but this is harmless in an asymptotic statement with fixed
`delta`.  Hence the claimed analytic-completion `o(1)` is valid.

## 4. Conductor recompletion and the forced cancellation

Writing `Y=floor(T)`, conductor recompletion leaves

```text
G_(T,X)(s)=D_Y(s)M_X(s)-1
 =sum_(m<=Y)m^(-s)sum_(Y/m<d<=X)mu(d)d^(-s).
```

Its coefficients satisfy exactly

```text
b_(T,X)(n)=-1  (Y<n<=2Y).
```

The synthesis was patched to retain `Y=floor(T)` in this exact identity; the
replacement of `Y` by a real `T` can fail at the endpoint integer.  The block
forces diagonal

```text
Delta_G>>T^(2lambda)/log T,
```

which tends to infinity.  Therefore the desired norm estimate requires

```text
OffDiag_G=-Delta_G+o(1).
```

A spectral estimate for nonzero modes, or an offdiagonal error smaller than
the diagonal, is not sufficient.  The zero mode is the continuous signed
Mobius reciprocal-hyperbola sum displayed in the report.

## 5. Conditional spectral implication

The coefficient-blind excess is `T^(4theta lambda+o(1))`.  Consequently an
estimate for the *complete signed form*

```text
OffDiag_F=O(T^[4theta lambda-kappa+epsilon])
```

with one fixed `kappa>0`, uniform for sufficiently small fixed `delta`, would
give `o(1)` after choosing `4theta lambda<kappa` and a smaller `epsilon`.
The explicit choice `delta<kappa/8`, after a harmless absolute smallness
restriction, satisfies both the diagonal and offdiagonal inequalities.

This implication is sufficient and correctly quantified.  It is wholly
conditional: known Kuznetsov, Kloosterman-fraction, exponent-pair, and
large-sieve inputs estimate oscillatory/nonprincipal modes after a principal
term is separated.  They do not evaluate the principal Mobius term with the
negative main term required above.

## 6. Smoothing and Perron residues

A nonnegative ordinate weight majorizing the zero disc has positive integral,
so it cannot delete frequency zero.  For a fixed smooth mollifier cutoff
`U(d/X)` equal to one near zero, its Mellin transform has a pole at `w=0`
with residue one.  This is precisely the normalization that preserves the
constant coefficient of the reciprocal mollifier.  A zero residue would
leave an order-`T` constant error in the area norm.

Thus smoothing does not erase the reciprocal-zeta poles.  The sharp Perron
formula was repaired to use `X_*=X+1/2`, avoiding the integer endpoint:

```text
M_X(s)=1/(2*pi*i)integral X_*^w/[w zeta(s+w)]dw.
```

For `zeta(s)!=0`, a left shift sees poles `w=rho-s`.  At `zeta(s)=0`, the
point `w=0` collides with such a denominator zero, so the residue-one
cancellation cannot be asserted uniformly through the candidate zero.  This
collision is the Mellin form of the same obstruction, not a way around it.

## 7. External range audit

The Bettin--Chandee--Radziwill ranges quoted in the tiny-delta report agree
with their stated arbitrary-polynomial and special-factorable ranges and are
strictly sub-conductor here.  The Wright result subtracts an expected
principal term before obtaining nonprincipal distribution, so it does not
supply the forced main term.

One current-source defect was material enough to patch: arXiv:2601.00292 by
Dong--Robles--Zeindler is withdrawn.  Its arXiv record says that a missing
factor invalidates the claimed improved bound.  It therefore supplies no
unconditional `1/46` theorem.  The report had used the claimed result only as
an example that was still too weak; deleting it cannot create a strip and
strengthens the negative literature verdict.

## 8. Synthesis audit

The synthesis correctly preserves the following directions after patching:

```text
Bergman o(1) norm                         sufficient for a strip;
diagonal and Euler--Maclaurin savings      necessary components only;
dyadic high-pass X^(3-delta)               equivalent to Mertens energy;
Wiener nuller Y^(-1/2+o(1))                lower bound, too small;
spectral T^(-kappa) saving                 hypothetical sufficient input;
Xi qualitative countermodel               scoped no-go, not actual Xi.
```

The optimistic higher-moment sentence was scoped to its diffuse-prime
diagonal, and the Xi statement was limited to the listed qualitative
properties rather than arbitrary possible shape information.

## Binary verdict

```text
explicit fixed delta proved                         NO
known zero-free region improved                     NO
tiny-delta exponent optimization                    VALID, CONDITIONAL
K=100000 Euler--Maclaurin completion                VALID
smoothing removal of principal mode                 IMPOSSIBLE AS PROPOSED
known complete signed spectral saving               NOT AVAILABLE
remaining obstruction                               principal Mobius mode
```

The final iteration is a sharper conditional reduction, not a proof of a
uniform zero-free strip.
