# Li--Keiper fail-fast checkpoint I

Status: normalization, exceptional-zero amplification, and first structural
falsification; 2026-08-01.

## 1. Exact normalization

Use

`xi(s) = (1/2) s(s-1) pi^(-s/2) Gamma(s/2) zeta(s)`.

For `n >= 1`, Li's coefficient is

`lambda_n = 1/(n-1)! * D^n [s^(n-1) log xi(s)] at s=1`.

Equivalently, near `z=0`,

`log xi(1/(1-z)) = log xi(1) + sum_(n>=1) (lambda_n/n) z^n`,

and, with symmetric zero summation,

`lambda_n = sum_rho [1 - ((rho-1)/rho)^n]`.

These three conventions agree; in particular

`lambda_1 = 1 + gamma/2 - log(4 pi)/2 = 0.023095708966...`.

## 2. The topology mismatch is genuinely repaired

Put `w(rho)=(rho-1)/rho`.  Direct calculation gives

`|w(rho)|^2 - 1 = (1 - 2 Re(rho))/|rho|^2`.

Consequently:

- `Re(rho)=1/2` exactly when `|w(rho)|=1`;
- a zero left of the line has `|w(rho)|>1`;
- its functional-equation partner `1-rho` lies right of the line and has
  modulus below one.

For a finite symmetric multiset of zeros, choose the terms of maximal modulus
`R>1`.  Their contribution is `R^n` times a nonzero real trigonometric sum.
Simultaneous Diophantine approximation supplies infinitely many `n` for which
all dominant phases are arbitrarily close to zero.  On that subsequence the
dominant sum is positive, so the minus sign in
`lambda_n = sum(1-w^n)` makes `lambda_n` exponentially negative.  Lower
moduli cannot cancel it.

For the actual infinite zero set, convergence and competing high zeros require
the standard analytic treatment; Voros's non-RH asymptotics give the resulting
non-tempered oscillation.  The finite argument is nevertheless the exact
countermodel lemma needed by this repository.

This is a substantive improvement over the failed local-prime routes.  An
off-line zero has exponentially increasing size in the Li topology rather
than square-summable local mass.

## 3. Exact completed arithmetic decomposition

Define the Laurent coefficients `eta_k` at `s=1` by

`-zeta'(s)/zeta(s) = 1/(s-1) + sum_(k>=0) eta_k (s-1)^k`.

Thus `eta_0=-gamma`, and

`D^j log((s-1)zeta(s)) at s=1 = -(j-1)! eta_(j-1)`.

Leibniz's rule and the polygamma values at `1/2` then give

```
lambda_n = 1 - n/2 (gamma + log(4 pi))
           + sum_(j=2)^n binom(n,j)(-1)^j(1-2^(-j)) zeta(j)
           - sum_(j=1)^n binom(n,j) eta_(j-1).
```

The first line and the finite zeta-value sum are the pole/archimedean block;
the final binomial transform is the arithmetic block.  The `eta_k` are
regularized global prime data: using them does not make positivity local or
termwise.  Replacing them by von Mangoldt sums requires the Guinand--Weil
regularization of Bombieri--Lagarias, not an absolutely convergent
term-by-term substitution at `s=1`.

## 4. Relation to Weil positivity

Lagarias proves that generalized Li coefficients are values of Weil's
quadratic functional on a specific family of test functions.  Therefore
`lambda_n >= 0` is not an independent positivity principle as presently
stated: it is a countable, conformally amplified sampling of the same global
Weil form.

This does not immediately kill the route.  The sampling has much better
exceptional-zero gain than compact-window localization.  But a proof must
discover extra structure on this special family; invoking positivity of the
ambient Weil functional would be circular.

## 5. First moment/total-positivity test: falsified

The most naive new structure would make either `(lambda_n)` or
`(lambda_n/n)` a Stieltjes moment sequence.  Every leading Hankel matrix would
then be positive semidefinite.  High-precision expansion gives

```
lambda_1 = 0.0230957089661210...
lambda_2 = 0.0923457352280467...
lambda_3 = 0.207638920554325...

det [[lambda_1, lambda_2],
     [lambda_2, lambda_3]] = -0.003732166735646... < 0,

det [[lambda_1, lambda_2/2],
     [lambda_2/2, lambda_3/3]] = -0.000533411010648... < 0.
```

So neither natural normalization is a Stieltjes/Hamburger moment sequence,
and ordinary Hankel total positivity fails already at order two.  The
reproducible diagnostic is `src/li_keiper_structure_scan.py`.

## 6. Bayesian verdict and next gate

The first checkpoint is mixed:

- **validated:** Li coordinates solve the exceptional-zero amplification
  problem exactly;
- **negative:** positivity is already known to be a restricted Weil
  functional, and the simplest independent moment explanation is impossible;
- **still live:** the special Li test family may possess a signed or
  transformed structure--finite-difference positivity, conditional negative
  definiteness, a Toeplitz kernel, or an arithmetic recurrence--not shared by
  arbitrary Weil tests.

The next fail-fast gate is therefore to classify finite differences and
Toeplitz kernels of the completed sequence, while testing every surviving
identity on functional-equation-symmetric entire countermodels with inserted
off-line quartets.  If the only positive kernel is equivalent to the Weil
form, Li--Keiper should be demoted rather than pursued indefinitely.

## Literature anchors

- X.-J. Li, *The positivity of a sequence of numbers and the Riemann
  hypothesis*, JNT 65 (1997).
- E. Bombieri and J. C. Lagarias, *Complements to Li's criterion for the
  Riemann hypothesis*, JNT 77 (1999).
- J. C. Lagarias, *Li coefficients for automorphic L-functions*, Ann. Inst.
  Fourier 57 (2007).
- A. Voros, *Sharpenings of Li's criterion for the Riemann Hypothesis* (2005).
