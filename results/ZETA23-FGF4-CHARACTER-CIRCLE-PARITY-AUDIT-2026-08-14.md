# FGF4 character, circle, and parity audit

**Date:** 2026-08-14
**Status:** exact character/circle reductions and scoped method obstructions
are proved; no pointwise fixed-shift power theorem is obtained.

## Verdict

Put

```text
q = 3 (mod 4),       a=(q+1)/4,       alpha=a/q,
S_I(q)=sum_(p,p+4 prime; p in I) chi_4(p)e(p/(4q)).
```

For every odd `p`,

```text
chi_4(p)e(p/(4q))=-i e_q(ap),                       (0.1)
```

so the fixed character is not an extra source of cancellation: it is
exactly the quarter-frequency part of the selected additive character.
The target is

```text
S_I(q)=-i sum_(p,p+4 prime; p in I)e_q(ap).          (0.2)
```

The circle-method version of (0.2) is an autocorrelation of one ordinary
prime exponential sum with a translate of itself.  Equivalently, the
`chi_4`-twisted prime spectrum is the ordinary odd-prime spectrum translated
by `1/4`.  Thus nonprincipality removes (more precisely, relocates) a
low-denominator major arc; it does not reduce the minor-arc energy.  After
the harmless major term is removed, the residual--residual integral is
exactly the fixed-shift prime-pair correlation which was to be bounded.

There are three rigorous, deliberately scoped negative conclusions.

1. Translation-invariant `L^p`/restriction estimates cannot create a
   `q`-power: their bounds are unchanged when one factor is translated.
2. Even when small-denominator major arcs and their `alpha`-translate are
   disjoint, a minor-arc supremum plus Parseval gives only
   `U sqrt(H)` (up to logarithms).  An optimistic classical denominator
   saving `U=H q^(-1/4+o(1))` therefore gives
   `H^(3/2)q^(-1/4+o(1))`, much larger than the required
   `Hq^(-.128435...)` throughout `q<=H`.
3. A positive sieve majorant cannot be passed through the complex sign, and
   an exact unit-coefficient chirp saturates the translated autocorrelation
   for every `alpha`.  Hence coefficient-blind circle/Cauchy or order-sieve
   arguments cannot prove the desired saving.

These statements do **not** rule out a coefficient-specific dispersion
theorem for actual cousin primes.  Ford--Maynard's optimality theorems are
likewise about arbitrary nonnegative sequences satisfying specified
Type-I/II axioms; they are not a no-go theorem for (0.2).

The exact required exponent remains

```text
delta > kappa/.1537 = .1284351502... .               (0.3)
```

No published theorem located supplies it pointwise on one physical block,
at shift `4`, for one height-selected modulus.  No zero-free strip is
claimed.

## 1. Exact circle and translation identities

Let

```text
P_I(theta)=sum_(p prime; p in I)e(p theta),
P_(I+4)(theta)=sum_(p prime; p-4 in I)e(p theta).
```

Orthogonality on `R/Z` gives

```text
sum_(p,p+4 prime; p in I)e(alpha p)
 =int_0^1 P_I(theta+alpha)
          conjugate(P_(I+4)(theta))e(4theta)dtheta.   (1.1)
```

The same formula holds with smooth cutoffs and/or von Mangoldt weights.
For the odd-prime part define

```text
P_chi,I(theta)=sum_(p in I)chi_4(p)e(p theta).
```

Then (0.1) at `q=infinity` gives the exact spectral identity

```text
P_chi,I(theta)=-i P_I(theta+1/4).                    (1.2)
```

(The prime `2` is absent from a gap-four pair.)  Therefore a circle
decomposition of the character-twisted correlation is just a translated
ordinary-prime circle decomposition.  Saying that `chi_4` has no principal
character at the arc around zero overlooks the translated principal arc
around `-1/4`.

For a prime selected modulus, the local Fourier main is small rather than
mysteriously large.  Uniformly distributing lower endpoints over the
admissible residues `r !=0,-4 (mod q)` gives

```text
sum_(r !=0,-4)e_q(ar)=-1-e_q(-4a)=-1-e_q(-1)=O(1),  (1.3)
```

against `q-2` available residues.  The expected selected main is therefore
of relative order `q^(-1)`, safely stronger than (0.3).  Proving that the
actual fixed-shift error has a power saving is the unresolved part.

## 2. What disjoint major arcs do and do not buy

Let `M(R,Delta)` be the union of arcs of radius `Delta` about reduced
rationals of denominator at most `R`.  If

```text
q>R^2,             2 Delta <1/(qR^2),                (2.1)
```

then

```text
M(R,Delta) intersect (M(R,Delta)-alpha)=empty.       (2.2)
```

Indeed, an intersection would approximate `a/q` within `2 Delta` by a
rational of denominator at most `R^2`.  Distinct such rationals are at
distance at least `1/(qR^2)`, while equality is impossible because `a/q` is
reduced and `q>R^2`.

Let `F,G` be the two prime polynomials in (1.1), and suppose their absolute
values on the minor arcs are at most `U_F,U_G`.  Splitting according to
which translated factor is minor gives only

```text
|int F(theta+alpha)conjugate(G(theta))e(4theta)dtheta|
 <=U_F ||G||_1+U_G ||F||_1
 <=U_F ||G||_2+U_G ||F||_2.                          (2.3)
```

Thus the absence of a major--major overlap is not itself a power theorem.
With von Mangoldt weights, Parseval leaves the full diagonal norm; with
prime indicators it leaves the square root of the number of primes.  In
either normalization a fixed power requires essentially square-root-size
minor sums, not the classical one-variable denominator saving.

To make the mismatch explicit, disjointness forces `R<sqrt(q)`.  Even
granting the optimistic classical shape

```text
U << H R^(-1/2)Y^o(1),
```

the best choice gives `U<<Hq^(-1/4)Y^o(1)`, and (2.3) gives

```text
H^(3/2)q^(-1/4)Y^o(1).                               (2.4)
```

For (2.4) to beat `Hq^(-delta)` one would need

```text
H^(1/2) <= q^(1/4-delta).
```

At `delta=.128435...`, `1/4-delta=.121564...`; this is impossible when
`q<=H`.  Actual short-interval prime estimates at the live
`H=Y^h`, `h` near `.248`, are weaker than the optimistic input above.

The remaining minor--minor integral cannot be discarded.  Translation is
unitary in every `L^p`, and Cauchy bounds it by the full Parseval energy.
For arbitrary unit coefficients this limitation is sharp: on each residue
class modulo `4`, define recursively

```text
c_(n+4)=c_n e(alpha n).
```

Then `|c_n|=1` and exactly

```text
sum_n c_n conjugate(c_(n+4))e(alpha n)=#terms.        (2.5)
```

This is a nonimplication for coefficient-blind norm arguments, not a model
of the primes.

## 3. Exact multiplicative-character audit

Every prime in the shell is a unit modulo `q`.  For

```text
T_I(chi)=sum_(p,p+4 prime; p in I)chi(p),
tau(chibar)=sum_(r in U_q)chibar(r)e_q(r),
```

character Fourier inversion gives

```text
sum_(p,p+4 prime; p in I)e_q(ap)
 =1/phi(q) sum_(chi mod q)chi(a)tau(chibar)T_I(chi). (3.1)
```

The principal coefficient is `mu(q)/phi(q)`.  By the cousin-prime upper
sieve its contribution is

```text
<< H q^(-1+o(1)),                                    (3.2)
```

and is harmless.  The exact energy identities are

```text
sum_chi |tau(chibar)|^2=phi(q)^2,                    (3.3)

sum_chi |T_I(chi)|^2
 =phi(q) sum_(r in U_q) A_I(r)^2,                   (3.4)
```

where `A_I(r)` counts cousin pairs with lower endpoint `r mod q`.
Consequently fixed-modulus character Cauchy/large-sieve estimates merely
return residue-class energy.  They do not produce a negative power of `q`
for the one Gauss-weighted direction in (3.1).  Modulus averaging can make
almost all directions small, but the architecture selects one modulus and
one numerator.

## 4. Exact order-sieve obstruction and parity scope

If `0<=x_n<=w_n`, no inequality of the form

```text
|sum u_n x_n| <= |sum u_n w_n|,       |u_n|=1,       (4.1)
```

is valid.  The two-point example

```text
x=(1,0),       w=(1,1),       u=(1,-1)
```

has left side `1` and right side `0`.  Thus a Selberg upper majorant for
`1_(p+4 prime)` cannot be inserted through the phase.  The valid triangle
inequality discards the phase and returns only the logarithmic cousin-prime
upper bound.

Vaughan and Heath--Brown identities are exact rearrangements.  Applied to
both prime factors, they leave product variables subject to the fixed
incidence

```text
product(d_i)-product(e_j)=4.                          (4.2)
```

Taking absolute values loses the additive phase; Cauchy after grouping by
the products asks for the same shifted correlation.  Murty--Vatwani make
the missing parity information explicit in a related framework: even
prime Elliott--Halberstam input is supplemented by a conjectural
shifted-prime/Mobius equidistribution hypothesis before their argument can
cross the parity barrier.  This identifies a missing kind of input; it is
not a theorem that (0.2) is false.

Ford--Maynard construct optimal counterexamples within a specified abstract
Type-I/Type-II class of nonnegative sequences.  Their results justify
rejecting an unspecified Type-I/II invocation, but do not apply as a no-go
theorem to the signed, coefficient-specific actual-prime sum (0.2).

## 5. Literature boundary

- Green--Tao, [*Restriction theory of the Selberg sieve, with
  applications*](https://jtnb.centre-mersenne.org/articles/10.5802/jtnb.538/),
  proves `L^p`, `p>2`, bounds for prime-tuple exponential sums, not a
  selected-frequency power bound.
- Mikawa, [*On prime twins in arithmetic
  progressions*](https://tsukuba.repo.nii.ac.jp/record/16157/files/8.pdf),
  averages the fixed-gap error over both shifts and moduli.
- Matomaki--Radziwill--Tao,
  [*Correlations of the von Mangoldt and higher divisor functions
  I*](https://arxiv.org/abs/1707.01315), proves the prime-pair asymptotic for
  almost all shifts in a long shift range, not for shift `4`.
- Murty--Vatwani, [*Twin primes and the parity
  problem*](https://doi.org/10.1016/j.jnt.2017.05.011), uses a conjectural
  shifted-Mobius distribution hypothesis to cross parity.
- Ford--Maynard, [*On the theory of prime-producing
  sieves*](https://arxiv.org/abs/2407.14368), is an optimality theory for
  abstract nonnegative Type-I/II sequences, with the scope stated above.
- Chou--Haag--Huryn--Ledoan, [*The error term in counting prime
  pairs*](https://arxiv.org/abs/2308.14888), emphasizes that for an
  individual fixed nonzero shift no nontrivial prime-pair error theorem is
  currently known.  It does not itself exclude the special twisted
  coefficient here.

## 6. Truth boundary

```text
chi_4 collapse (0.1):                                EXACT
circle autocorrelation (1.1):                        EXACT
quarter-translation identity (1.2):                  EXACT
small-denominator arc separation (2.2):              EXACT
norm-only bound and chirp saturation (2.3)--(2.5):   EXACT
Gauss expansion and energy (3.1)--(3.4):             EXACT
positive-majorant transfer through phase:            FALSE
classical circle/Vaughan machinery proves q-power:    NO
published pointwise fixed-shift selected-q theorem:   NOT FOUND
published no-go eliminating actual FGF4:              NOT FOUND
FGF4 fixed-gap sector:                                OPEN
whole signed tail / zero-free strip:                  OPEN / NOT CLAIMED
```

Reproduce the finite identities with

```bash
python3 results/verify_zeta23_fgf4_character_circle_gate.py
```
