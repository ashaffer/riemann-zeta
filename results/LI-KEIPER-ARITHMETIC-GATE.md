# Li--Keiper fail-fast checkpoint III: arithmetic order audit

Status: final Li promotion gate rejected; branch demoted; 2026-08-01.

## 1. Exact finite-place formula

Let

`K_n(x) = L_(n-1)^(1)(x)
        = sum_(j=1)^n binom(n,j)(-1)^(j-1)x^(j-1)/(j-1)!`.

Bombieri--Lagarias' regularized finite-place term is

```
S_f(n) = lim_(N->infinity) [
  sum_(m<=N) Lambda(m)/m K_n(log m)
  - sum_(j=1)^n binom(n,j)(-1)^(j-1)(log N)^j/j!
].
```

With the completed archimedean contribution `S_infinity(n)`, the exact formula
is

`lambda_n = 1 + S_infinity(n) - S_f(n)`.

Equivalently, `S_f(n)` is the regularized pairing of `K_n` with

`d nu(t) = sum_m Lambda(m)/m delta_(log m)(t) - dt`.

Both the measure `d nu` and, for `n>=2`, the Laguerre kernel are signed.  This
is the decisive obstruction to a primewise order law.

## 2. What the prime kernel really supplies

For every `n>=2`, `K_n` has `n-1` positive simple zeros and alternates sign
between them.  Thus even individual prime-power contributions have no fixed
sign.  The associated Laguerre recurrence is

`n K_(n+1)(x) = (2n-x)K_n(x)-nK_(n-1)(x)`.

It does not order `S_f(n)`: its coefficients change sign, and integration is
also against the signed discrepancy `d nu`.

Indeed, between prime powers the cutoff follows an alternating polynomial
counterterm, while at a prime power its jump has the sign of
`K_n(log(p^k))`.  Neither the continuous pieces nor the jumps have a uniform
direction.  Applying the recurrence under the pairing introduces

`<x K_n, d nu>`,

which is a new logarithmic moment.  Repeating produces the entire Laurent
coefficient hierarchy.  There is no closed scalar recurrence for `S_f(n)`.

## 3. No order reappears after taking the limit

Using the exact generating-function values of `lambda_n` and the explicit
archimedean block gives

```
S_f(1) = -0.5772156649...
S_f(2) = -0.9668850969...
...
S_f(6) = -1.4882983272...
S_f(7) = -1.4801908402...
S_f(8) = -1.4448557441...
```

Thus `S_f(n)` decreases through `n=6` and then increases.  Pointwise
monotonicity of `K_n` does not survive the signed prime discrepancy.

The script `src/li_prime_kernel_audit.py` computes the regularized cutoffs
directly from prime powers and displays their scale dependence.

## 4. Why the remaining domination inequality is RH-strength

Li positivity is exactly

`S_f(n) <= 1 + S_infinity(n)` for every n`.

The left side pairs a growing Laguerre polynomial with the prime-number-theorem
discrepancy.  As `n` grows, this family is precisely the conformal amplifier
that detects an off-line zero.  Therefore a uniform estimate strong enough to
prove the displayed inequality must control the coherent Mellin modes that
encode those zeros.  Bombieri--Lagarias identify these same tests as special
values of Weil's quadratic functional.

No sign, monotonicity, orthogonality, or recurrence of the oscillatory kernel
controls its pairing with the signed discrepancy.  Supplying the missing
uniform domination without a new arithmetic invariant is the Li/Weil
criterion itself.

## 5. Countermodel separation

Functional-equation-symmetric entire functions with inserted off-line
quartets fail Li positivity through exponential conformal amplification, but
they have no Euler product.  Hence they correctly show that an arithmetic
input is necessary.

The Euler product contributes positive Mangoldt atoms, but the Li test applies
the oscillatory Laguerre weight and completion forces subtraction of the
continuous main term `dt`.  Replacing the kernel or discarding that subtraction
can manufacture positivity only by destroying the equality with `lambda_n`.
Retaining both restores fidelity but removes order.  This is another exact
instance of the repository's fidelity--amplification--closure trilemma.

## 6. Verdict

The Li--Keiper route is **demoted as a primary proof program**:

- it is an excellent, completion-native exceptional-zero amplifier;
- its ordinary moment and finite-difference structures fail;
- its natural conditional/Toeplitz structure is exactly RH;
- its prime Laguerre kernels oscillate and their recurrence does not close
  after renormalization;
- the remaining domination statement is the restricted Weil criterion.

This is not a claim that no proof through Li coefficients can exist.  It is a
portfolio conclusion: the audited structures provide no independent slack,
and further coefficient manipulation is likely to chase the same obstruction.
The next active target should be Nicolas--Robin extremality, specifically
whether transitions between primorial or colossally abundant extremizers carry
a discrete order invariant that does not collapse to the explicit-formula
error term.

## Literature anchors

- E. Bombieri and J. C. Lagarias, *Complements to Li's criterion for the
  Riemann hypothesis*, J. Number Theory 77 (1999), 274--287.
- J. C. Lagarias, *Li coefficients for automorphic L-functions*, Ann. Inst.
  Fourier 57 (2007), especially the finite/archimedean decomposition and Weil
  interpretation.
