# Adversarial audit: the factorial-ramp sign conjecture is false

Status: decisive unconditional kill.  The conjecture

```text
sum_(floor(sqrt N)<q<=N)(N-2q)Lambda(q) <= 0              (1.1)
```

cannot hold eventually.  In fact it fails for infinitely many integers `N`.
The proof does not assume RH:

1. eventual validity of (1.1) gives the one-sided estimate
   `R(x)>=-C sqrt(x)` for the exact R95--R96 ramp;
2. the one-sided Landau theorem already audited in R96 then forces RH;
3. under RH, the once-integrated explicit formula gives
   `R(x)=psi(x)-x+O(sqrt(x))`; and
4. Littlewood's theorem
   `psi(x)-x=Omega_+/- (sqrt(x) log log log x)` contradicts the
   one-sided square-root estimate.

The same argument proves that neither one-sided bound

```text
R(x)>=-C sqrt(x),             R(x)<=C sqrt(x)              (1.2)
```

can hold eventually.  The `sqrt(x)` boundary is materially different from
the exponent `a>1/2` target in R96: at the boundary Landau alone merely
forces RH, while Littlewood's quantitative oscillation theorem supplies the
contradiction.

```text
factorial sign conjecture                                  FALSE
number of violations                                       INFINITE
integer/real transfer                                      EXACT
prime-power convention                                     EXACT
Landau at exponent 1/2                                     FORCES RH
integrated explicit-formula correction under RH            O(sqrt x)
Littlewood oscillation transferred to R                    EXACT
finite-smoothing cross-check                               PASSES
fixed strip or RH obtained from the conjecture              VACUOUS.       (1.3)
```

## 2. Definitions and exact conventions

Let

```text
psi(x)=sum_(n<=x)Lambda(n),
A(x)=sum_(n<=x)n Lambda(n),
D(x)=psi(x)-(x-1),                                         (2.1)

R(x)=sum_(n<=x)Lambda(n)(2n/x-1)-1+1/x.                    (2.2)
```

The sums in this report are over ordinary positive integers.  Equivalently
one may write `q=p^k`, because `Lambda(n)` vanishes unless `n` is a prime
power and then `Lambda(p^k)=log p`.  Each prime power occurs once.  No
replacement of `psi` by `theta` is made.

Stieltjes summation gives

```text
Psi_1(x):=integral_1^x psi(t)dt
         =sum_(n<=x)Lambda(n)(x-n),

A(x)=x psi(x)-Psi_1(x).                                   (2.3)
```

Therefore

```text
R(x)=D(x)-(2/x)integral_1^x D(t)dt.                        (2.4)
```

The endpoint `n=x` causes no ambiguity in `Psi_1`, since its weight is zero.
The convention in (2.2) is right-continuous and includes a prime power at
`x`.

For an integer `N>=4`, put

```text
M=floor(sqrt N),

H_N=sum_(M<n<=N)(N-2n)Lambda(n),
L_N=sum_(n<=M)(N-2n)Lambda(n).                             (2.5)
```

If `N` is a square, the prime-power layer `n=sqrt N` belongs to `L_N`, not
`H_N`.  If it is not a square, `n>M` is exactly the same integer condition as
`n>sqrt N`.  Thus (2.5) agrees exactly with the cutoff in R99.

The factorial ratio of R99 satisfies

```text
log P_(N,M)=H_N.                                           (2.6)
```

Since `P_(N,M)>0`, its conjectured inequality `P_(N,M)<=1` is exactly
`H_N<=0`; there is no logarithm or rational-product sign reversal.

## 3. Exact transfer from the factorial sign to the ramp

Multiplying (2.2) by `N` yields

```text
N R(N)
 =sum_(n<=N)(2n-N)Lambda(n)-N+1
 =-H_N-L_N-N+1.                                           (3.1)
```

For `n<=M<=N/2`, the low coefficient `N-2n` is nonnegative.  Chebyshev's
elementary bound `psi(y)<<y` gives

```text
0<=L_N<=N psi(M)<<N^(3/2).                                (3.2)
```

Consequently, if `H_N<=0`,

```text
R(N)>=-C sqrt(N)-1.                                       (3.3)
```

This estimate transfers from integers to every real `x` without losing a
power.  If `N<=x<N+1`, the atomic sums are fixed and

```text
R(x)-R(N)
 =(2A(N)+1)(1/x-1/N).                                     (3.4)
```

Since `A(N)<=N psi(N)<<N^2`,

```text
|R(x)-R(N)|<<1.                                           (3.5)
```

Thus eventual validity of the factorial conjecture implies

```text
R(x)>=-C_1 sqrt(x)                                        (3.6)
```

for every sufficiently large real `x`.  R99's integer-to-real assertion is
therefore correct, including at prime-power jumps.

## 4. What Landau does, and what it does not do, at `1/2`

On logarithmic scale, set `mathcal R(U)=R(exp U)`.  Direct integration of
(2.2), or (2.4), gives for `Re s>1`

```text
F_R(s):=integral_0^infinity mathcal R(U)exp(-sU)dU

 =[(s-1)/(s(s+1))]
   [-zeta'(s)/zeta(s)-1/(s-1)].                            (4.1)
```

At a nontrivial zero `rho` of multiplicity `m_rho`, the residue is

```text
Res_(s=rho) F_R(s)
 =-m_rho (rho-1)/[rho(rho+1)] !=0.                         (4.2)
```

All signs and rational factors agree with R96.  The continued transform is
analytic on the positive real axis: `zeta(s)<0` for `0<s<1`, the singularity
at one in the bracket is removable, and the rational multiplier has no
positive pole.

Assume (3.6) and change an initial compact interval if necessary.  Then

```text
g(U)=mathcal R(U)+C_1 exp(U/2)>=0.                          (4.3)
```

Its Laplace transform is `F_R(s)+C_1/(s-1/2)` plus an entire compact-support
term.  Let `sigma_c` be its finite convergence abscissa.  Landau's theorem
forces a singularity at the real point `s=sigma_c`.  Since the displayed
continuation is analytic at every real point greater than `1/2`, this first
shows `sigma_c<=1/2`.  The defining Laplace integral is consequently
holomorphic throughout `Re(s)>1/2`; but (4.2) gives it a nonremovable pole
at any zeta zero in that half-plane.  Hence no such zero exists, and the
functional equation then gives RH.

This argument does **not** itself contradict (3.6).  The added term has a
real pole exactly at `s=1/2`, so Landau's conclusion is compatible with a
convergence abscissa equal to `1/2`.  A claim that Landau alone kills a
one-sided `O(sqrt x)` bound would be a boundary error.  The quantitative
Littlewood step below is essential.

For comparison, the general Mellin oscillation theorem of Kaczorowski and
Pintz applies directly to (4.1) if RH is false and yields two-sided
oscillations of size `x^(Theta-epsilon)`, where `Theta>1/2` is the rightmost
zero abscissa.  See J. Kaczorowski and J. Pintz,
[*Oscillatory properties of arithmetical functions I*](https://personal.math.ubc.ca/~gerg/teaching/592-Fall2018/papers/1986.Kaczorowski_1.pdf),
Theorem 1 and Corollary 1.  This is stronger than needed for the logical
implication above.

## 5. The integrated explicit formula under RH

It remains to determine whether RH could coexist with (3.6).  It cannot.

The integrated Perron formula is

```text
Psi_1(x)
 =1/(2 pi i) integral_((c))
    [-zeta'(s)/zeta(s)] x^(s+1)/[s(s+1)] ds,     c>1.       (5.1)
```

The weight `(x-n)_+` is continuous, so the resulting identity holds at
integer and noninteger `x` with the same endpoint convention.  Moving the
contour and summing residues gives

```text
Psi_1(x)
 =x^2/2
  -sum_rho x^(rho+1)/[rho(rho+1)]
  -x log(2 pi)
  +zeta'(-1)/zeta(-1)
  -sum_(k>=1)x^(1-2k)/[2k(2k-1)].                         (5.2)
```

Zeros are counted with multiplicity.  The zero sum is absolutely convergent,
because `N(T)<<T log T` implies

```text
sum_rho 1/|rho(rho+1)|<infinity.                           (5.3)
```

Under RH, `Re rho=1/2`, so (5.2) gives uniformly for `x>=2`

```text
Psi_1(x)-x^2/2=O(x^(3/2)).                                 (5.4)
```

Since

```text
integral_1^x D(t)dt=Psi_1(x)-(x-1)^2/2,                    (5.5)
```

the harmless linear terms in (5.2)--(5.5) yield

```text
(2/x)integral_1^x D(t)dt=O(sqrt x).                        (5.6)
```

Combining (2.4) and (5.6),

```text
R(x)=D(x)+O(sqrt x)
    =psi(x)-x+O(sqrt x).                                   (5.7)
```

This is stronger than the estimate obtained by integrating the usual
pointwise RH bound `D(x)=O(sqrt(x)log^2 x)`.  Naively integrating that bound
would retain logarithms.  The removal of the logarithms in (5.6) comes from
the extra absolutely summable factor `1/[rho(rho+1)]` in the integrated
explicit formula.

## 6. Littlewood kills the boundary estimate

Littlewood's quantitative oscillation theorem states unconditionally that

```text
psi(x)-x=Omega_+/- (sqrt(x) log log log x).                 (6.1)
```

A modern primary-source proof and strengthening is J. Kaczorowski and
K. Wiertelak,
[*Oscillations of a given size of some arithmetic error terms*](https://doi.org/10.1090/S0002-9947-09-04803-X),
Transactions of the AMS 361 (2009), 5023--5039.  Equation (1.1) states
(6.1), and Theorem 1.1 proves many alternating oscillations of the more
general size `sqrt(x) log log H(T)`.

Adding one to `psi(x)-x` does not affect (6.1).  Under RH, (5.7) therefore
transfers it exactly to the ramp:

```text
R(x)=Omega_+/- (sqrt(x) log log log x).                     (6.2)
```

In particular, for every fixed `C`, there are arbitrarily large `x` with

```text
R(x)<-C sqrt(x),                                           (6.3)
```

and arbitrarily large `x` with `R(x)>C sqrt(x)`.

Now suppose the factorial sign conjecture held eventually.  Section 3 would
give (3.6); Section 4 would force RH; and (6.3) would contradict (3.6).
Therefore (1.1) fails infinitely often.

Exactly the same dichotomy, using the positive side of (6.2), proves that an
eventual upper estimate `R(x)<=C sqrt(x)` is impossible too.

## 7. Finite-smoothing cross-check

The preceding proof already closes the conjecture.  There is an independent
way to check that the high-pass multiplier has not destroyed Littlewood's
oscillation mechanism.

Under RH, Kaczorowski and Wiertelak use the analytic zero series

```text
K_D(z)=sum_(gamma>0) [1/rho] exp(i gamma z),
rho=1/2+i gamma.                                           (7.1)
```

They prove that it belongs to their class `A`, with boundary value equal to
the normalized prime-number-theorem error up to elementary decaying terms.
Their Theorem 2.1 applies an explicit finite `m`-fold box smoothing, whose
frequency multiplier is

```text
[sin(delta_m gamma)/(delta_m gamma)]^m.                    (7.2)
```

The two sectorial logarithmic singularities of `K_D` then force alternating
large boundary values.

For the present ramp, replace (7.1) by

```text
K_R(z)
 =sum_(gamma>0) [(rho-1)/(rho(rho+1))] exp(i gamma z).      (7.3)
```

The coefficient difference is

```text
(rho-1)/(rho(rho+1))-1/rho
 =-2/[rho(rho+1)].                                         (7.4)
```

By (5.3), the series of differences converges absolutely and uniformly down
to the real boundary.  Hence `K_R-K_D` is bounded and continuous there.
Every class-`A` hypothesis used by their finite smoothing is preserved:

* the frequency count is unchanged;
* weighted coefficient summability remains valid;
* boundary existence and local boundedness gain only a bounded term; and
* the two opposite logarithmic sector blowups are unchanged up to `O(1)`.

Thus their finite-sinc certificate proves (6.2) directly for `R`.  Equation
(5.7) is the simpler arithmetic expression of the same fact: the ramp
multiplier differs from one by an absolutely summable zero multiplier.

This cross-check also verifies the residue sign in (4.2).  The boundary
series for `-R` has coefficient `(rho-1)/[rho(rho+1)]`; the Laplace transform
of `R` consequently has its negative, exactly as in (4.2).

## 8. Infinitely many explicit sign failures, but no effective first one

At integers, solve (3.1) for the factorial high tail:

```text
H_N=-N R(N)-L_N-N+1.                                      (8.1)
```

Under RH, choose the negative Littlewood sequence in (6.2) and move each
point to its integer floor.  Equation (3.5) changes `R` by only `O(1)`, while
the Littlewood magnitude tends to infinity after division by `sqrt x`.
Together with `L_N<<N^(3/2)`, (8.1) gives

```text
H_N>0                                                     (8.2)
```

for infinitely many `N`.  If RH is false, the stronger off-line-zero
oscillation from the Mellin theorem quoted in Section 4 gives the same
conclusion.  Equivalently, the contradiction argument already shows that
only finitely many violations is impossible.

This proof is ineffective at any practical scale.  Littlewood's theorem does
not locate the first violation, so the scan through `20,000,000` in R99 is
fully compatible with (8.2).  It is evidence only of a long initial bias.

## 9. Disposition

The factorial/lcm algebra in R99 remains correct, but its surviving sign
conjecture is closed:

1. `log P_(N,floor sqrt N)` is exactly the full prime-power high ramp.
2. Its conjectured nonpositivity gives a lower square-root bound for `R` at
   integers and, with only `O(1)` loss, at every real point.
3. Landau at the exact exponent `1/2` forces RH but does not itself give a
   contradiction.
4. Under the resulting RH, the integrated explicit formula differs from the
   raw PNT error by only `O(sqrt x)`.
5. Littlewood's unbounded `log log log x` factor then forces both signs past
   every fixed square-root constant.
6. Hence the factorial sign fails infinitely often; no divisibility,
   majorization, or finite scan can prove it.

The correct surviving target remains the R96 one-sided estimate at an
exponent strictly larger than `1/2`, for example

```text
R(x)>=-C_a x^a,                  1/2<a<1,                    (9.1)
```

or its upper analogue.  Such a statement proves a fixed zero-free strip but
is not contradicted by Littlewood's critical-line oscillations.  The exact
square-root sign conjecture was stronger than RH and is false.
