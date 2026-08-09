# R101 Littlewood ramp sign-kill

Status: the square-root-cutoff sign conjecture left open in R99 is
rigorously false.  Unconditionally, the R96 von Mangoldt ramp has
two-sided oscillations at least of Littlewood size,

```text
R(x)=Omega_+ (sqrt(x) log log log x)
     and
R(x)=Omega_- (sqrt(x) log log log x).                 (0.1)
```

The statement also holds on the integers.  Consequently the signed
factorial ratio from R99 satisfies

```text
log P_(N,floor(sqrt(N)))
 =Omega_+ (N^(3/2) log log log N)
  and
 =Omega_- (N^(3/2) log log log N).                    (0.2)
```

In particular, this ratio is greater than one for infinitely many `N` and
less than one for infinitely many `N`.  The finite absence of a positive
value through `N=20,000,000` was a genuine but misleading finite pattern.

This closes only the proposed exact square-root endpoint mechanism.  It
proves neither a fixed zero-free strip nor failure of every fixed strip.
One-sided bounds `R(x)=O_one-sided(x^a)` with a fixed `a>1/2` remain open.

Date: 2026-08-07.

## 1. Objects and result

Retain the notation of R96 and R99:

```text
psi(x)=sum_(n<=x)Lambda(n),

D(x)=psi(x)-(x-1),

R(x)=D(x)-(2/x) integral_1^x D(t)dt

    =sum_(n<=x)Lambda(n)(2n/x-1)-1+x^(-1).            (1.1)
```

For a positive comparison function `G`, write `F=Omega_+(G)` if there are
`c>0` and arbitrarily large arguments with `F>=cG`, and define
`Omega_-` analogously.

**Theorem 1.1 (unconditional two-sided ramp oscillation).**  As `x` tends
to infinity through the reals,

```text
R(x)=Omega_+ (sqrt(x) log log log x),
R(x)=Omega_- (sqrt(x) log log log x).                 (1.2)
```

Both assertions remain true when `x` is restricted to positive integers.

The proof is an exhaustive RH/non-RH dichotomy.  Off RH, the R96 Landau
theorem gives a stronger power oscillation by contraposition.  On RH, an
exact first-Riesz explicit formula shows that the Volterra correction in
(1.1) is only `O(sqrt(x))`; it therefore cannot erase Littlewood's
`sqrt(x) log log log x` oscillations of `psi(x)-x`.

This use of RH inside one branch is not an assumption in Theorem 1.1.  The
two branches cover all possibilities.

## 2. The exact first-Riesz formula

Put

```text
Psi_1(x)=integral_1^x psi(t)dt
        =sum_(n<=x)Lambda(n)(x-n),       x>1.          (2.1)
```

The weight at `n=x` is zero, so (2.1) has no endpoint convention.

**Lemma 2.1 (first-Riesz explicit formula).**  For every real `x>1`,

```text
Psi_1(x)
 =x^2/2
  -sum_rho x^(rho+1)/[rho(rho+1)]
  -x log(2 pi)
  +zeta'(-1)/zeta(-1)
  -sum_(k>=1) x^(1-2k)/[2k(2k-1)].                   (2.2)
```

The first sum is over all nontrivial zeta zeros with multiplicity.  It is
absolutely convergent.

### Proof

For `c>1`, the order-one Perron formula is

```text
Psi_1(x)
 =1/(2 pi i) integral_(c-i infinity)^(c+i infinity)
   [-zeta'(s)/zeta(s)] x^(s+1)/[s(s+1)] ds.           (2.3)
```

Shift the line left through rectangles whose horizontal sides avoid the
zeros.  The extra factor `1/[s(s+1)]`, together with the standard
logarithmic-derivative bounds on such sides, makes the limiting shift
legitimate.  The residues are:

```text
s=1:       x^2/2,
s=rho:    -m_rho x^(rho+1)/[rho(rho+1)],
s=0:      -x log(2 pi),
s=-1:      zeta'(-1)/zeta(-1),
s=-2k:    -x^(1-2k)/[2k(2k-1)].                      (2.4)
```

Here `-zeta'/zeta` has residue `1` at the pole `s=1` and residue
`-m_rho` at a zero of multiplicity `m_rho`; also
`zeta'(0)/zeta(0)=log(2 pi)`.  Finally,

```text
sum_rho 1/abs(rho(rho+1)) < infinity                 (2.5)
```

follows from the classical count `N(T)=O(T log T)`, and the trivial-zero
series converges absolutely.  Taking the limiting rectangles proves
(2.2).  QED.

Let

```text
I(x)=integral_1^x D(t)dt.                             (2.6)
```

Since the integral of `t-1` is `(x-1)^2/2`, Lemma 2.1 gives the exact
identity

```text
I(x)
 =-sum_rho x^(rho+1)/[rho(rho+1)]
  +(1-log(2 pi))x
  +zeta'(-1)/zeta(-1)-1/2
  -sum_(k>=1) x^(1-2k)/[2k(2k-1)].                   (2.7)
```

**Corollary 2.2 (RH Riesz bound).**  On RH,

```text
I(x)=O(x^(3/2)),
R(x)=psi(x)-x+O(sqrt(x)).                             (2.8)
```

### Proof

On RH, `abs(x^(rho+1))=x^(3/2)`.  Absolute convergence in (2.5) therefore
bounds the zero sum in (2.7) by

```text
x^(3/2) sum_rho 1/abs(rho(rho+1))=O(x^(3/2)).        (2.9)
```

The elementary terms are `O(x)`.  Thus `I(x)=O(x^(3/2))`.  Substitution in

```text
R(x)=D(x)-2I(x)/x,
D(x)=psi(x)-x+1                                      (2.10)
```

proves the second assertion.  QED.

The absolute convergence in this argument is the reason first-Riesz
smoothing is sufficient.  No simplicity hypothesis for the zeros is used.

## 3. The RH branch: Littlewood survives the filter

The classical Hardy--Littlewood oscillation theorem, in the form needed
here, says that on RH

```text
psi(x)-x=Omega_+ (sqrt(x) log log log x),
psi(x)-x=Omega_- (sqrt(x) log log log x).             (3.1)
```

See G. H. Hardy and J. E. Littlewood,
[*Contributions to the theory of the Riemann zeta-function and the theory
of the distribution of primes*](https://projecteuclid.org/journals/acta-mathematica/volume-41/issue-none/Contributions-to-the-theory-of-the-riemann-zeta-function-and/10.1007/BF02422942.pdf),
Acta Mathematica **41**, 119--196.
For a modern primary-source statement and strengthening, see J. Kaczorowski
and K. Wiertelak,
[*Oscillations of a given size of some arithmetic error terms*](https://doi.org/10.1090/S0002-9947-09-04803-X),
Transactions of the AMS **361** (2009), equation (1.1) and Theorem 1.1.

By Corollary 2.2, the difference between `R(x)` and `psi(x)-x` is
`O(sqrt(x))`.  Since

```text
log log log x -> infinity,                            (3.2)
```

an `O(sqrt(x))` perturbation cannot destroy either sequence in (3.1).
Therefore (1.2) holds if RH is true.

## 4. The non-RH branch: R96 gives a stronger oscillation

Suppose RH is false.  The functional equation and conjugation symmetry
then give a nontrivial zero

```text
rho_0=beta_0+i gamma_0,       beta_0>1/2.             (4.1)
```

Choose any fixed

```text
1/2<a<beta_0.                                          (4.2)
```

R96 proved the following one-sided Landau implication:

```text
R(x)>=-C x^a eventually    OR
R(x)<= C x^a eventually

        ==> zeta(s) has no zero with Re(s)>a.          (4.3)
```

The zero in (4.1) makes the conclusion of (4.3) false.  Applying the
contrapositive separately to its lower- and upper-bound versions shows
that, for every `C>0` and every `X`, there are `x_+,x_->=X` with

```text
R(x_+)> C x_+^a,
R(x_-) <-C x_-^a.                                     (4.4)
```

In other words,

```text
limsup_(x->infinity) R(x)/x^a=+infinity,
liminf_(x->infinity) R(x)/x^a=-infinity.              (4.5)
```

Because

```text
x^a/[sqrt(x) log log log x] -> infinity               (4.6)
```

for `a>1/2`, (4.5) implies (1.2).  This completes the proof of Theorem 1.1
on the real line.

The pole calculation behind the use of R96 is worth retaining.  For
`Re(s)>1`,

```text
integral_1^infinity R(x)x^(-s-1)dx
 =[(s-1)/(s(s+1))]
  [-zeta'(s)/zeta(s)-1/(s-1)].                        (4.7)
```

At a nontrivial zero `rho` of multiplicity `m_rho`, its residue is

```text
-m_rho (rho-1)/[rho(rho+1)],                          (4.8)
```

which never vanishes.  Thus the ramp filter does not cancel an off-line
zero pole.

## 5. Real oscillations transfer to integers

Let

```text
A(N)=sum_(n<=N)n Lambda(n).                            (5.1)
```

For `N<=x<N+1`, the arithmetic atoms do not change, and (1.1) gives

```text
R(x)=2A(N)/x-psi(N)-1+1/x.                            (5.2)
```

Consequently

```text
R(x)-R(N)=(2A(N)+1)(1/x-1/N).                        (5.3)
```

Chebyshev's bound `psi(N)<<N` gives `A(N)<=N psi(N)<<N^2`, while

```text
abs(1/x-1/N)<=1/N^2.                                 (5.4)
```

It follows uniformly that

```text
R(x)-R(floor(x))=O(1).                               (5.5)
```

Also

```text
sqrt(x) log log log x
  ~(sqrt(N) log log log N),       N=floor(x).         (5.6)
```

Taking floors of the two real sequences from Theorem 1.1 therefore proves
both integer assertions.  Prime-power endpoints cause no ambiguity: if
`x` is an integer then (5.3) is exactly zero, and otherwise the atoms are
constant throughout its unit interval.

## 6. The R99 factorial ratio changes sign on the logarithmic scale

For `M<N/2`, R99 constructed the explicit signed factorial ratio
`P_(N,M)` and proved

```text
log P_(N,M)
 =sum_(M<q<=N)(N-2q)Lambda(q),                        (6.1)

E_(N,M)
 :=sum_(q<=M)(N-2q)Lambda(q),                         (6.2)

N R(N)=-log P_(N,M)-E_(N,M)-N+1.                    (6.3)
```

For

```text
M=floor(sqrt(N)),                                     (6.4)
```

Chebyshev gives

```text
0<=E_(N,M)<=N psi(M)<<N^(3/2).                       (6.5)
```

Rearrange (6.3):

```text
log P_(N,M)=-N R(N)-E_(N,M)-N+1.                    (6.6)
```

Along the negative integer sequence from Theorem 1.1,

```text
R(N)<=-c sqrt(N) log log log N,                       (6.7)
```

so (6.5)--(6.6) give

```text
log P_(N,M)
 >=c N^(3/2)log log log N-O(N^(3/2))
 =Omega_+(N^(3/2)log log log N).                     (6.8)
```

Along the positive sequence,

```text
R(N)>=c sqrt(N) log log log N,                        (6.9)
```

and the nonnegative residual only strengthens the opposite inequality:

```text
log P_(N,M)
 <=-c N^(3/2)log log log N+O(N)
 =Omega_-(N^(3/2)log log log N).                    (6.10)
```

This proves (0.2).

**Corollary 6.1 (the R99 sign conjecture is false).**  Each of

```text
P_(N,floor(sqrt(N)))>1,
P_(N,floor(sqrt(N)))<1                               (6.11)
```

holds for infinitely many positive integers `N`.  In particular, neither
eventual sign is possible.

## 7. What this does and does not close

The R99 finite pattern was aimed at

```text
P_(N,floor(sqrt(N)))<=1                              (7.1)
```

eventually.  Equation (6.8) disproves (7.1), while (6.10) also disproves
the reverse eventual sign.  Equivalently, Theorem 1.1 rules out both exact
square-root one-sided ramp estimates

```text
R(x)>=-C sqrt(x),
R(x)<= C sqrt(x).                                    (7.2)
```

This is a useful fail-fast closure, not a resolution of the zero-free-strip
goal.  For every fixed `a>1/2`, the Littlewood scale satisfies

```text
sqrt(x)log log log x=o(x^a),                          (7.3)
```

so the oscillation theorem is compatible with either one-sided
`O(x^a)` bound sought in R96.  Such a bound would still prove a fixed
zero-free half-plane `Re(s)>a`; R101 neither proves it nor rules it out.

The reusable lesson is exact:

```text
first-Riesz correction on RH       O(sqrt(x)) after filtering
Littlewood prime error             two-sided sqrt(x) log log log x
off-RH retained zero pole          two-sided x^a for some a>1/2
integer sampling loss              O(1)
sqrt-cutoff residual in log P      O(N^(3/2))
resulting log P oscillation         N^(3/2) log log log N, both signs. (7.4)
```

The square-root-support integrality certificate from R99 remains exact and
potentially reusable.  Its hoped-for sign is now closed.
