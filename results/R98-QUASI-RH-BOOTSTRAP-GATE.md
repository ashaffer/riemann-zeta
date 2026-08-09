# R98 quasi-RH bootstrap gate

Status: conditional exponent audit under

```text
Theta=sup_rho Re(rho)<1.
```

The resulting power PNT and Mertens estimates are imported and fed through
classical and current zero-density estimates, Turan power sums, zero
repulsion, mollified moments, and the functional equation.  Every valid
feedback loop either returns the same exponent `Theta`, controls only the
number of possible zeros, or applies only on the already zero-free side of
`Theta`.  No strict map `f(Theta)<Theta` is obtained.  This is a no-go for
the audited bootstrap mechanisms, not a proof that no different quasi-RH
bootstrap can exist.

Date: 2026-08-07.

## 1. Verdict

Assume

```text
1/2<=Theta:=sup{Re(rho):zeta(rho)=0, 0<Re(rho)<1}<1.      (1.1)
```

The exact classical consequences, with endpoint epsilon losses where
needed, are

```text
psi(x)-x=O(x^Theta log^2 x),                              (1.2)

M(x)=O_epsilon(x^(Theta+epsilon)),                        (1.3)

zeta(s)^(-1)-sum_(n<=X)mu(n)n^(-s)
 =O[ (1+abs(s)/(sigma-Theta-epsilon))
      X^(Theta+epsilon-sigma) ],                          (1.4)
```

where (1.4) requires `sigma>Theta+epsilon`.

The desired bootstrap would have to prove, from (1.1),

```text
zeta(s)!=0 for Re(s)>f(Theta),
f(Theta)<Theta.                                           (1.5)
```

Here is the exponent ledger.

| mechanism | strongest relevant output after assuming (1.1) | exclusion threshold |
|---|---|---|
| PNT/Mertens converse | analyticity of `-zeta'/zeta` or `1/zeta` in `sigma>Theta+epsilon` | `Theta`, unchanged |
| Guth--Maynard density | `N(sigma,T)<=T^((30/13)(1-sigma)+o(1))` | no individual-zero exclusion for any fixed `sigma<1` |
| Turan power sum | zero at `beta` gives a prime remainder of exponent `beta`; (1.2) allows exponent `Theta` | contradiction only if `beta>Theta` |
| classical zero repulsion | `1-beta` on the scale `1/log abs(gamma)` from positivity at `sigma>1` | weaker than the fixed assumed gap `1-Theta` |
| Deuring--Heilbronn | repulsion caused by an exceptional **real** character zero | no trigger for a complex zeta quartet |
| reciprocal mollifier | tail decays like `X^(Theta-sigma)` | useful only for `sigma>Theta` |
| mollified moments | density/proportion bounds | one sparse off-line zero remains allowed |
| functional equation | zeros lie in `1-Theta<=beta<=Theta` | reflection returns `Theta` |

Thus the direct iteration map supplied by the imported machinery is

```text
f_imported(Theta)=Theta.                                  (1.6)
```

The irreducible obstruction is an **individual-zero versus aggregate-bound
mismatch**.  A single zero at real part `beta<=Theta` contributes at its
own allowed exponent to the prime and Mobius remainders.  Density and
moment estimates can make such zeros arbitrarily rare, but rare is not
absent.

The only public manuscript found in the repository that explicitly
claims `quasi-RH => RH`, Puglisi's arXiv:2210.03121v9, was audited in R95.
Its final alternating-exponential inequality is false in the exact
parameter range used by the proof.  It supplies no bootstrap theorem.

## 2. The conditional baseline is exponent-sharp

Put

```text
E(x)=psi(x)-x.                                             (2.1)
```

The truncated explicit formula, at a suitable height `T`, is

```text
E(x)=-sum_(abs(gamma)<=T) x^rho/rho
     +O(x log^2(xT)/T+log x).                             (2.2)
```

Take `T` of order `x`, avoiding zero ordinates in the standard way.  From
`Re(rho)<=Theta` and

```text
sum_(0<abs(gamma)<=T)1/abs(rho)=O(log^2 T),               (2.3)
```

one gets (1.2).

The Mobius counterpart is the generalized Littlewood criterion.  A
zero-free half-plane `sigma>Theta` and standard good-height bounds for
`1/zeta(s)` give, for every `epsilon>0`, (1.3).  Conversely, (1.2) and
(1.3) cannot be improved past a zero without excluding it.  Indeed, for
`sigma>1`, partial summation gives

```text
-zeta'(s)/zeta(s)
 =s integral_1^infinity psi(x)x^(-s-1)dx,                 (2.4)

1/zeta(s)
 =s integral_1^infinity M(x)x^(-s-1)dx.                  (2.5)
```

If `E(x)=O(x^a log^B x)`, subtracting the transform of `x` in (2.4)
continues `-zeta'/zeta` holomorphically to `sigma>a`, apart from the known
pole term at one.  A zeta zero there would create a pole, so

```text
E(x)=O(x^a log^B x)  =>  Theta<=a.                        (2.6)
```

Likewise,

```text
M(x)=O_epsilon(x^(a+epsilon)) for every epsilon>0
                    =>  Theta<=a.                         (2.7)
```

The reverse implications hold with endpoint epsilon or logarithmic losses.
Consequently the two arithmetic exponents are not downstream quantities
that the zero-free hypothesis has accidentally overestimated.  Their
infimal power exponent is `Theta` itself:

```text
inf{a:E(x)=O_epsilon(x^(a+epsilon))}=Theta,
inf{a:M(x)=O_epsilon(x^(a+epsilon))}=Theta.                (2.8)
```

This already blocks a naive loop

```text
zero-free line -> power PNT -> better zero-free line.      (2.9)
```

The first arrow and its Turan/Allison converse preserve the exponent.
There is no slack to iterate.

Primary sources for the converse direction include Turan's 1950 papers,
Pintz's sharpenings, and Allison's Mobius version:

* [Turan, *On the remainder-term in the prime-number formula, II*](https://doi.org/10.1007/BF02021308),
  Acta Math. Acad. Sci. Hungar. 1 (1950), 155--166;
* [Pintz, *On the remainder term of the prime number formula II; On a
  theorem of Ingham*](https://doi.org/10.4064/aa-37-1-209-220), Acta
  Arith. 37 (1980), 209--220;
* [Allison, *On obtaining zero-free regions for the zeta-function from
  estimates of M(x)*](https://doi.org/10.1017/S030500410004562X), Proc.
  Cambridge Philos. Soc. 67 (1970), 333--337.

## 3. Zero density improves frequency, not the edge

Let

```text
N(sigma,T)=#{rho:Re(rho)>=sigma, abs(Im(rho))<=T}.         (3.1)
```

The classical Ingham and Huxley estimates are

```text
N(sigma,T)
 <=T^[3(1-sigma)/(2-sigma)+o(1)],                         (3.2)

N(sigma,T)
 <=T^[3(1-sigma)/(3sigma-1)+o(1)]                         (3.3)
```

in their useful respective ranges.  Guth--Maynard improve the transition
range and prove

```text
N(sigma,T)
 <=T^[15(1-sigma)/(3+5sigma)+o(1)]                        (3.4)
```

in the new range.  Combining the ranges gives the convenient uniform
corollary

```text
N(sigma,T)<=T^[(30/13)(1-sigma)+o(1)].                   (3.5)
```

See [Guth--Maynard, *New large value estimates for Dirichlet
polynomials*](https://arxiv.org/abs/2405.20552), Theorem 1.2.  The original
classical references are [Ingham, *On the estimation of
N(sigma,T)*](https://doi.org/10.1093/qmath/os-11.1.201) and
[Huxley, *On the difference between consecutive
primes*](https://doi.org/10.1007/BF01418933).

Insert the proposed new line `sigma=Theta-delta`, with fixed `delta>0`,
into (3.5):

```text
N(Theta-delta,T)
 <=T^[(30/13)(1-Theta+delta)+o(1)].                       (3.6)
```

Since `Theta<1`, the exponent remains strictly positive even as
`delta->0+`:

```text
(30/13)(1-Theta)>0.                                      (3.7)
```

Therefore (3.6) never becomes `<1` for large `T`.  It cannot exclude one
zero.  The sharper piece (3.4) has the same defect:

```text
d_GM(Theta)
 =15(1-Theta)/(3+5Theta)>0.                               (3.8)
```

This is not merely a weakness of the numerical constant.  Even the density
hypothesis

```text
N(sigma,T)<<_epsilon T^[2(1-sigma)+epsilon]               (3.9)
```

has a positive exponent for every fixed `sigma<1`.  A density theorem can
prove a fixed strip, after the initial compact range is handled, only if
its dyadic count yields

```text
N(sigma;T,2T)=o(1)                                       (3.10)
```

for the desired `sigma`, or an equivalent negative-power upper bound.
None of (3.2)--(3.5) has that form.

### 3.1 The short-interval corollary does not give `17/30`

Guth--Maynard also prove the prime number theorem in every interval of
length

```text
h>=x^(17/30+epsilon).                                     (3.11)
```

It is tempting to feed (3.11) into Turan and announce a zero-free line
`17/30`.  That would give an unconditional fixed strip and is false.

A zero term changes a short interval by

```text
[(x+h)^rho-x^rho]/rho
 =h x^(rho-1)(1+O(h/x))                                   (3.12)
```

when `h=o(x)`.  Relative to the main term `h`, its size is

```text
x^(beta-1)=o(1)                                           (3.13)
```

for every `beta<1`, independently of the exponent of `h`.  Thus an
asymptotic prime count in such intervals is compatible with every
nontrivial zeta zero.  Turan's converse needs a **global remainder bound**,
not merely the correct first-order local increment.

### 3.2 Density cannot sharpen the pointwise explicit formula

Under (1.1), absolute summation of (2.2) already gives

```text
sum_(abs(gamma)<=T)abs(x^rho/rho)
 <=x^Theta O(log^2 T).                                   (3.14)
```

Density can reduce the average contribution from zeros well left of
`Theta`, but one zero with real part arbitrarily near `Theta` still has
size `x^(Theta-o(1))/abs(rho)`.  Any pointwise upper bound valid for all
`x` must accommodate it.  Replacing (3.14) by a mean-square estimate also
does not remove that diagonal contribution; it changes frequency, not its
horizontal exponent.

## 4. Turan power sums return the same exponent

The useful content of a Turan power-sum theorem is that, after localizing a
finite cluster of zero terms, one term of maximal modulus cannot be
canceled for every member of a controlled block of powers.  Schematically,
a zero `rho_0=beta+i gamma` produces some scale `X` for which

```text
abs(E(X)) >= X^(beta-o(1)).                               (4.1)
```

The hypothesis (1.1) supplies only

```text
abs(E(X)) <= X^(Theta+o(1)).                              (4.2)
```

Comparing the two yields a contradiction exactly when

```text
beta>Theta.                                               (4.3)
```

But (4.3) is the region excluded by the definition of `Theta`.

Taking a higher power does not amplify the horizontal gap.  If the power
sum raises a zero carrier to its `m`th power, then the ledgers are

```text
zero lower carrier:       x^(m beta),
PNT upper carrier:        x^(m Theta+o(m)),               (4.4)
```

and division by `m` again gives (4.3).  Fixed smoothing inserts powers of
`1/rho` but leaves the exponent of `X` equal to `beta`.  It can improve
height losses, not the boundary abscissa.

This matches the exact converse theory.  Ingham sends a zero-free boundary
to a PNT remainder boundary, while Turan, Stas, and Pintz recover the same
zero-free boundary from the remainder.  In the standard subexponential
parameterization,

```text
zero-free gap (log t)^(-a)
 <-> PNT saving exp[-c(log x)^(1/(1+a))],                 (4.5)
```

up to constants and secondary factors.  In the fixed-power specialization,
(4.5) becomes the identity `a_arithmetic=Theta` in (2.8), not a contraction.

Pintz's explicit oscillation theorems are valuable for a different reason:
they show that an exposed zero cannot remain invisible to the prime
remainder.  But an oscillation of size `X^beta` is fully compatible with
the allowed envelope `X^Theta` when `beta<=Theta`.

## 5. Zero repulsion has no quasi-RH trigger

Classical zero-free regions use the nonnegative coefficients in

```text
-zeta'(s)/zeta(s)=sum_n Lambda(n)n^(-s),       Re(s)>1,   (5.1)
```

often combined through a nonnegative trigonometric polynomial.  If a zero
`beta+i gamma` is isolated in the logarithmic derivative, the resulting
inequality has the schematic form

```text
1/(sigma-beta)
 <=C[1/(sigma-1)+log(abs(gamma)+3)].                      (5.2)
```

Optimizing with

```text
sigma-1 asymp 1/log(abs(gamma)+3)                         (5.3)
```

gives the classical height-dependent gap

```text
1-beta >= c/log(abs(gamma)+3),                            (5.4)
```

or its Vinogradov--Korobov refinement after stronger zeta estimates.

Under quasi-RH, `1-beta>=1-Theta` is already a fixed positive gap.  Putting
that into (5.2) produces no new term proportional to
`(Theta-beta) log gamma`; it only makes an already valid inequality more
comfortable.  One cannot move the evaluation point from `sigma>1` to
`sigma=Theta+delta<1`, because the positive Dirichlet series (5.1) no
longer converges there.  Analytic continuation retains the formula but
loses the coefficient positivity that powers the argument.

### 5.1 Deuring--Heilbronn is inapplicable

The Deuring--Heilbronn phenomenon is a genuine horizontal repulsion
mechanism, but its trigger is an exceptional **real** zero of a real
Dirichlet `L`-function extremely close to one.  Modern statements make this
hypothesis explicit; see [Benli--Goel--Twiss--Zaman, *Explicit
Deuring--Heilbronn phenomenon for Dirichlet
L-functions*](https://arxiv.org/abs/2410.06082), Corollary 1.1.

The Riemann zeta function has no real nontrivial zero in `(0,1)`.  For real
`0<s<1`,

```text
zeta(s)=eta(s)/(1-2^(1-s))<0,                             (5.5)
```

since the alternating eta series is positive and the denominator is
negative.  A hypothetical off-line zeta zero instead occurs in a complex
quartet

```text
beta +/- i gamma,
1-beta +/- i gamma.                                      (5.6)
```

Such a quartet does not supply the real-character positivity behind
Deuring--Heilbronn.  Treating one complex member as an exceptional zero
silently drops the sign condition.

Nor does ordinary local zero spacing help.  A sequence of off-line zeros
can be spaced superexponentially in height and satisfy every known local
repulsion inequality while its real parts approach `Theta`.

## 6. The reciprocal-mollifier tail has the wrong sign below `Theta`

Let

```text
M_X(s)=sum_(n<=X)mu(n)n^(-s).                             (6.1)
```

For `sigma>1`, partial summation gives the exact identity

```text
1/zeta(s)-M_X(s)
 =-M(X)X^(-s)+s integral_X^infinity M(u)u^(-s-1)du.       (6.2)
```

Under (1.3), choose `eta>0`.  The right side converges and obeys

```text
abs(1/zeta(s)-M_X(s))
 <=C_eta [1+abs(s)/(sigma-Theta-eta)]
          X^(Theta+eta-sigma),                           (6.3)
```

but only when

```text
sigma>Theta+eta.                                         (6.4)
```

This is the exact mollifier ledger.  Put `X=T^kappa` and try to detect
zeros on

```text
sigma=Theta-delta.                                       (6.5)
```

The formal tail factor becomes

```text
X^(Theta-sigma)=T^(kappa delta),                          (6.6)
```

which grows.  On `sigma=Theta+delta` it decays like
`T^(-kappa delta)`, but that half-plane is zero-free by the hypothesis.
Longer mollifiers make (6.6) worse below the edge.

Thus the conditional Mertens estimate does not provide a reciprocal
approximation on the side where a bootstrap must operate.  Any argument
that inserts (6.3) at (6.5) has analytically continued a divergent tail
through the very poles it is supposed to exclude.

## 7. Mollified moments do not exclude a sparse zero

The other use of a mollifier does not approximate `1/zeta` pointwise.
One studies a detector such as

```text
F_X(s)=1-zeta(s)M_X(s).                                   (7.1)
```

At a zeta zero,

```text
F_X(rho)=1.                                               (7.2)
```

Mean-square or large-value estimates for `F_X`, combined with a local zero
detector or a separated selection of ordinates, can then bound how many
such points occur.  The conclusion is a zero-density estimate, not a
pointwise reciprocal approximation.

In the Levinson--Conrey architecture one instead forms a mollified
auxiliary function `G_X(s)=V(s)M_X(s)`, where the argument of `V` is tied to
zeros of zeta on the critical line.  Littlewood's lemma turns a boundary
mean into a horizontally weighted count of zeros of this **auxiliary**
function:

```text
2pi sum_(rho_G in rectangle)(Re(rho_G)-sigma_0)
 <= integral_0^T log abs(G_X(sigma_0+it))dt
    +boundary terms.                                     (7.3)
```

Here `F_X` is the separate pointwise detector in (7.1).  The argument
principle converts the auxiliary zero count into a lower bound for the
proportion of critical zeta zeros.  An upper bound of order `T`,
`o(T log T)`, or even a positive power `T^epsilon` may prove a proportion or
a density theorem.  It does not force every off-line zeta zero to
disappear.

The best unconditional critical-line proportion results illustrate the
distinction.  Conrey's long-mollifier theorem proves more than two fifths,
and later work proves slightly more than five twelfths:

* [Conrey, *More than two fifths of the zeros of the Riemann zeta
  function are on the critical line*](https://doi.org/10.1515/crll.1989.399.1);
* [Pratt--Robles--Zaharescu--Zeindler, *More than five-twelfths of the
  zeros of zeta are on the critical
  line*](https://doi.org/10.1007/s40687-019-0199-8).

These theorems use impressive cancellation in mollified moments, but any
fixed proportion, and even density one, is compatible with a zero-density
sequence off the line whose real parts approach `Theta`.

Assumption (1.1) can improve the behavior of a Mobius mollifier on lines to
the right of `Theta`; Section 6 shows exactly why that improvement stops at
the old edge.  On lines to the left, the moment calculation reverts to an
aggregate zero detector and cannot exclude one exception.

## 8. Functional-equation symmetry preserves the width

The completed zeta function satisfies

```text
xi(s)=xi(1-s)=conjugate(xi(conjugate(s))).                (8.1)
```

Therefore (1.1) implies the two-sided band

```text
1-Theta<=Re(rho)<=Theta.                                  (8.2)
```

In terms of the displacement

```text
Delta=Theta-1/2,                                         (8.3)
```

reflection maps `Delta` to the same `Delta`.  If the known upper endpoint
is `Theta`, the reflected lower endpoint is `1-Theta`, and reflecting that
lower endpoint gives

```text
1-(1-Theta)=Theta.                                       (8.4)
```

There is no interval contraction.

The asymmetric equation

```text
zeta(s)=chi(s)zeta(1-s)                                  (8.5)
```

also gives no modulus comparison at a zero: both sides of (8.5) are zero.
Dividing by either zeta factor at such a point is invalid.  The fact that
`abs(chi(s))` is generally not one off the critical line constrains ratios
at nonzeros, not the common zero divisor.

For the reciprocal inside the nontrivial critical strip, (8.5) says that
`1/zeta(s)` is known holomorphic in

```text
Theta<sigma<1       and       0<sigma<1-Theta.             (8.6)
```

The unknown zeros lie in the middle band (8.2).  A three-lines or
Phragmen--Lindelof argument across that band requires holomorphy there;
supplying it is precisely the desired theorem.

## 9. Why combining the mechanisms still does not contract

One could hope that each theorem is individually exponent-neutral but
their composition is not.  The possible compositions have only three
interfaces.

### 9.1 Zeros to arithmetic and back

```text
Theta
 -> E(x),M(x) of exponent Theta
 -> zero-free abscissa Theta.                             (9.1)
```

Equations (2.4)--(2.8) prove that this loop is the identity at the power
level.  Turan changes constants and height localization but not the power.

### 9.2 Density to arithmetic and back

Density estimates improve averages of explicit-formula sums and yield
short-interval or almost-all conclusions.  A single edge zero contributes
`x^beta/rho` globally and `h x^(beta-1)` locally.  The former is within the
`x^Theta` envelope; the latter is lower order for every `beta<1`.
Consequently neither output supplies an arithmetic exponent below
`Theta` for all `x`, which is what the converse requires.

### 9.3 Mertens to a mollifier to density

The Mertens input makes the reciprocal tail small only for
`sigma>Theta`; there the zero count is already zero.  Moving the detector
left replaces decay by the growth factor (6.6).  Mean values can then
recover a density estimate, but Section 3 shows that density does not
exclude the edge.

Hence every closed route through the imported nodes contains one of the
following irreducible inequalities:

```text
beta>Theta                         (Turan/PNT contradiction),
sigma>Theta                        (reciprocal-tail convergence),
d(sigma)>0                         (density count),
1-(1-Theta)=Theta                  (functional symmetry). (9.2)
```

No algebraic optimization of auxiliary lengths changes these four signs.

## 10. A sparse edge profile that passes every aggregate test

The logical weakness can be made concrete without claiming that the
following is a possible zeta divisor.  Fix `Theta` in `(1/2,1)` and, for
sufficiently large integers `n`, put

```text
beta_n=Theta-1/n,
t_n=exp(exp(n^2)).                                        (10.1)
```

Add the symmetry quartets

```text
beta_n +/- i t_n,
1-beta_n +/- i t_n.                                      (10.2)
```

For each fixed `sigma<Theta`, the number of right-hand members up to height
`T` is

```text
O(sqrt(log log T)).                                      (10.3)
```

This is smaller than `T^epsilon` for every fixed `epsilon>0`, hence far
below all the density bounds in Section 3.  The heights are separated by
far more than any standard local zero-repulsion scale.  The off-line
profile has zero relative density among `T log T` zeros and therefore
passes every positive-proportion or density-one critical-line statement.
It obeys the functional-equation symmetry exactly.

Its explicit-formula carriers have powers

```text
x^beta_n<=x^Theta,                                       (10.4)
```

so the power PNT envelope also allows them.  An even simpler profile is one
fixed off-line quartet with real part `Theta`; a bounded number of zeros is
also compatible with every positive-power density upper bound.

Again, (10.1)--(10.2) is not asserted to come from an Euler product.  It is
a witness that the **inequalities being imported** do not encode the
missing per-zero exclusion.  Any successful bootstrap must use a zeta
specific constraint absent from this profile.

## 11. What a real bootstrap theorem would need

The audit leaves four quantitatively precise possible upgrades.

1. **A negative-power zero count.**  From quasi-RH, prove for some
   `g(Theta)<Theta` and every fixed `sigma>g(Theta)` that the dyadic count
   satisfies

   ```text
   N(sigma;T,2T)<<T^(-c).                                 (11.1)
   ```

   Since the left side is an integer, this excludes all sufficiently high
   such zeros; finite verification or a separate compact argument handles
   the initial range.  Ordinary zero density has the opposite sign.

2. **A genuinely improved global arithmetic exponent.**  Derive

   ```text
   psi(x)-x=O(x^(g(Theta)+epsilon))
   ```

   or the analogous Mertens bound with `g(Theta)<Theta`.  By Section 2 this
   immediately proves the improved strip, but it is exactly the missing
   cancellation, not a free corollary of quasi-RH.

3. **A one-sided signed estimate.**  R95--R96 show that an eventual
   one-sided bound for the signed von Mangoldt ramp at exponent `a`
   excludes zeros to the right of `a`.  Such a theorem can kill one sparse
   edge carrier because it uses its forced oscillation, rather than its
   density.  Quasi-RH currently supplies only a two-sided absolute
   envelope.

4. **A zeta-specific replication theorem.**  Prove that one off-line zero
   forces sufficiently many controlled copies to violate (3.5).  Standard
   universality does not approximate vanishing targets, and strong
   self-recurrence across a compact containing a zero is an RH-level issue.
   No imported recurrence theorem supplies this step.

These are not cosmetic improvements of an auxiliary exponent.  Each one
adds an individual-zero exclusion mechanism, which is precisely what
density, moments, and symmetry lack.

## 12. Bottom line

Under `Theta<1`, the repository may safely import

```text
power PNT exponent                         Theta
power Mertens exponent                     Theta+epsilon
reciprocal Dirichlet tail                  only right of Theta
current zero-density bounds                positive-power counts
Turan oscillation from one zero            exponent beta
functional symmetry                        [1-Theta,Theta]. (12.1)
```

Systematically composing these statements does not yield
`f(Theta)<Theta`.  The fixed-strip assumption is stable under the audited
classical machinery: it neither bootstraps to RH nor contradicts itself.

The reality check is therefore negative but useful.  A future quasi-RH
bootstrap should be rejected immediately if its decisive line uses a
reciprocal Mobius tail at `sigma<=Theta`, turns a positive-power density
bound into zero exclusion, imports short-interval primes as a global PNT
power, divides the functional equation at a zero, or treats a complex zeta
zero as a Deuring--Heilbronn exceptional real zero.

No fixed strip and no theorem `Theta=1` is proved here.  The surviving
direction is the signed individual-zero route from R95--R96, not another
round of aggregate density or mollification.
