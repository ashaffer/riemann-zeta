# Nicolas criterion: exact primorial-transition audit

Status: first Nicolas--Robin fail-fast checkpoint; simple discrete order laws
rejected, extremal transition reduced exactly to Chebyshev error plus the next
prime; 2026-08-01.

## 1. Exact score and criterion

Let

`N_k = product_(j<=k) p_j`, `T_k=theta(p_k)=log N_k`, and

`P_k = N_k/phi(N_k) = product_(p<=p_k) (1-1/p)^(-1)`.

For `T_k>1`, define

`u_k = P_k/log T_k`

and the logarithmic Nicolas margin

`D_k = log u_k - gamma`.

Nicolas's theorem says RH is equivalent to `D_k>0` for every relevant `k`;
if RH is false, both signs occur infinitely often.  Mertens' theorem and the
prime number theorem give `D_k -> 0`.

## 2. Exact transition law

Put `q=p_(k+1)` and `ell=log q`.  Since

`P_(k+1)=P_k/(1-1/q)` and `T_(k+1)=T_k+ell`,

we obtain the identity

```
D_(k+1)-D_k
 = -log(1-1/q)
   - log( log(T_k+ell) / log T_k ).
```

There is no hidden primorial quantity left.  The direction of one extremizer
transition is determined entirely by the next prime `q` and the accumulated
Chebyshev value `theta(p_k)`.

The condition that `u_k>u_(k+1)` is equivalently

`log(1 + log(q)/theta(p_k)) > log(theta(q))/q`,

the transition inequality isolated by Choie--Planat--Solé.

## 3. The first-order cancellation is the whole difficulty

Both terms in the increment have leading size `1/q`:

```
-log(1-1/q)                  = 1/q + O(1/q^2),
log(log(T_k+log q)/log T_k) = log(q)/(T_k log T_k) + lower terms.
```

Because `T_k ~ q` and `log T_k ~ log q`, their main terms cancel.  The sign is
therefore controlled by the fine error in `theta(p_k)` together with the next
prime gap.  This is precisely the scale at which the explicit formula and a
hypothetical off-line zero act.  Primorial compression has not created a
macroscopic margin.

## 4. Monotonicity and convexity gates

An eventually decreasing `u_k` would prove the Nicolas inequality because
`u_k -> exp(gamma)`.  It is not a plausible invariant:

- Choie--Planat--Solé prove, conditional on Cramér's prime-gap conjecture, that
  `u_k>u_(k+1)` fails infinitely often;
- they also show unconditionally that eventual increase is impossible;
- direct computation through primes below two million finds every first
  difference negative, illustrating why finite computation misleadingly
  suggests the false monotonicity conjecture;
- over the same range, the second difference changes sign more than 72,000
  times.  Convexity, concavity, and simple interlacing are absent long before
  the predicted first reversal of monotonicity.

Higher finite-difference sign patterns are therefore not credible structural
carriers.  The reproducible computation is
`src/nicolas_transition_audit.py`.

## 5. What extremality did and did not buy

Primorials exactly maximize `n/phi(n)` among integers constrained by their
prime support.  This removes irrelevant integers and turns RH into a discrete
one-sided order statement.  But the transition itself contains no integrality
gap: `D_k` is real-valued and tends to zero, while its increment is a
difference of two asymptotically equal analytic quantities.

Thus Nicolas avoids the local-`L2` topology but recreates the collapsing-margin
problem in an ordered sequence.  The extremizers select where to test the
prime discrepancy; they do not constrain its sign.

## 6. First gate verdict

The naive Nicolas advantage--eventual monotonic approach to `exp(gamma)`--is
rejected.  The exact transition law is a disguised comparison between
`theta(p_k)` and the next prime.  Proving its sign uniformly would require
fine prime-distribution control and, conditionally on Cramér, would assert a
false statement.

One genuinely different possibility remains before demoting the whole
Nicolas--Robin family: colossally abundant transitions change **prime
exponents**, not merely append the next prime.  Their variational parameter
could supply a Legendre-envelope or slope-order invariant absent for
primorials.  The next gate should derive that envelope exactly and test Robin's
normalized score at every exponent-transition type.

## Literature anchors

- J.-L. Nicolas, *Petites valeurs de la fonction d'Euler*, J. Number Theory
  17 (1983), 375--388.
- Y. Choie, M. Planat, and P. Solé, *On Nicolas criterion for the Riemann
  Hypothesis*, 2010.
