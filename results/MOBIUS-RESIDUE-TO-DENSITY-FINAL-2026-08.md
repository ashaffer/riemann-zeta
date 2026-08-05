# Mobius residue-to-density: near-density succeeds, the inverse gate fails

Status: fail-fast branch completed, 2026-08-04.

## Verdict

This branch separates into two conclusions.

1. The residue-to-density idea is much less speculative than the earlier
   ledger suggested.  A theorem of Pintz shows that **one** zeta zero
   `rho = beta + i gamma`, `beta >= 1/2`, forces positive and negative Mertens
   peaks of order `x^beta` in every sufficiently large logarithmic window of
   width `O((log log X)^(3/2))`.  That is near-syndetic, but it is not the
   desired constant-width log-syndetic statement.
2. Even granting resonance on *every* sufficiently large scale does not imply
   bounded pretentious distance.  An explicit Selberg--Delange family has
   squarefree support, prime values arbitrarily close to those of Mobius,
   super-square-root sums on every large scale, and divergent pretentious
   distance.

Thus the proposed two-gate route to RH is pruned.  Improving Pintz's growing
window to a constant window would be a real standalone result, but it cannot
feed the proposed general inverse theorem.

## 1. The proposed gates

For a fixed scale test `w`, put

```text
S_w(X; gamma) = sum_n mu(n) n^(-i gamma) w(n/X).
```

Its formal Mellin carrier is

```text
Mellin(S_w)(s) = W(s) / zeta(s + i gamma).
```

The intended route was:

```text
one zero beta+i gamma, beta>1/2
        -> fixed-test resonance of size X^beta on log-syndetic scales
        -> bounded pretentious distance
        -> contradiction with mu(p)=-1.
```

The two arrows are logically distinct.  The first is a quantitative
oscillation theorem; the second is an inverse theorem for multiplicative
functions.

## 2. What one zero really gives

Pintz proved the following effective theorem.  If

```text
zeta(rho) = 0,    rho = beta+i gamma,    beta >= 1/2,
```

then, for every sufficiently large `Y`, there are `x_+` and `x_-` in

```text
[Y exp(-5 (log_2 Y)^(3/2)), Y]
```

such that

```text
 M(x_+) >  x_+^beta / (48 |rho|^3),
 M(x_-) < -x_-^beta / (48 |rho|^3).
```

Here `log_2 Y = log log Y`.  See J. Pintz, *Oscillatory properties of
M(x), III*, Theorem 2.1 in
[Acta Arithmetica 43 (1984), 105--113](http://matwbn.icm.edu.pl/ksiazki/aa/aa43/aa4323.pdf).
Part I also proves a strong `L1` mean lower bound over a much broader
multiplicative interval: [Acta Arithmetica 42 (1982),
49--55](http://matwbn.icm.edu.pl/ksiazki/aa/aa42/aa4214.pdf).

In log time `u=log x`, Pintz gives a peak of each sign within distance

```text
5 (log u)^(3/2).
```

This has three precise consequences for the gate.

- The old description "an arbitrarily sparse Omega subsequence" was too
  pessimistic and is now superseded.
- The theorem still does not give a fixed `L` such that every interval
  `[u,u+L]` contains a peak.
- It concerns the sharp Mertens cutoff.  Converting it to one predetermined
  smooth twisted test without losing the scale density is an additional
  step, not a harmless change of notation.

[Kaczorowski--Pintz](https://doi.org/10.1007/BF01949062) oscillation theorems
similarly give many sign changes and super-root peaks in subpower
multiplicative windows.  None of these results supplies constant log gaps or
positive lower log measure.

## 3. The exact conditional log-syndetic lemma

There is a clean sufficient condition, but it is much stronger than "RH is
false".

Assume that, after twisting by `gamma`, all globally rightmost poles relevant
to `W(s)/zeta(s+i gamma)` are finitely many simple poles

```text
s_j = beta+i tau_j,
```

that every other pole lies to the left of `beta-eta`, and that horizontal
contours and the reciprocal-zeta remainder justify a shift with error
`O(X^(beta-eta'))`.  Then

```text
S_w(e^u; gamma) = e^(beta u) (P(u) + O(e^(-eta' u))),
P(u) = sum_j c_j e^(i tau_j u).
```

If at least one `c_j` is nonzero, `P` is a nonzero trigonometric polynomial.
Uniform almost periodicity makes a fixed superlevel set of `|P|` relatively
dense.  Consequently `|S_w(X;gamma)| >= c X^beta` on a log-syndetic set.  A
unique dominant pole gives the inequality at every sufficiently large scale.

An arbitrary off-line zero does **not** provide these hypotheses.  The
supremum of the real parts need not be attained, there need not be a gap below
a dominant line, and bounds needed to sum the residue tail are load-bearing.

There is also a tempting but invalid shortcut.  The identity

```text
integral S_w(X;gamma) X^(-s) dX/X = W(s)/zeta(s+i gamma)
```

is initially a time-domain integral only where the Dirichlet series
converges.  Analytically continuing the right side to the pole does not
continue the generally divergent left-side integral.  An Abel-energy or
Plancherel conclusion at `Re s=beta` would already require the growth control
being sought.

## 4. Point density is not mass density

For `w` fixed and compactly supported, coefficient boundedness gives

```text
|d/du S_w(e^u;gamma)| <= C_w e^u.
```

A peak of height `e^(beta u)` is therefore guaranteed to persist only on the
logarithmic width

```text
Delta u asymp e^(-(1-beta)u).
```

Even one such guaranteed neighborhood per unit log interval has finite total
log measure.  This does not prove that actual peaks are narrow; it proves that
point-syndeticity alone cannot be silently upgraded to the positive-measure or
entropy premise needed by an averaged inverse argument.

## 5. A fatal counterexample to the inverse gate

Fix `z` with `0<|z|<=1`, excluding the nonpositive integer endpoint when a
nonzero leading term is wanted, and define

```text
f_z(n) = mu(n)^2 z^omega(n).
```

This is a `1`-bounded multiplicative function with exactly Mobius's
squarefree support.  Its Dirichlet series factors as

```text
sum_n f_z(n)n^(-s)
  = product_p (1+z p^(-s))
  = zeta(s)^z H_z(s),

H_z(s) = product_p (1+z p^(-s))(1-p^(-s))^z.
```

The linear prime terms cancel in `log H_z`, so `H_z` is holomorphic and
nonzero for `Re s>1/2`.  Selberg--Delange therefore gives

```text
sum_(n<=x) f_z(n)
  = H_z(1)/Gamma(z) * x (log x)^(z-1)
    + O_z(x (log x)^(Re z-2)).
```

See de la Bretèche--Tenenbaum, *Remarks on the Selberg--Delange method*,
[Acta Arithmetica 200 (2021)](https://arxiv.org/abs/2010.12929).  Partial
summation gives the same leading scale for every fixed smooth `w` with
nonzero integral.  Hence, for every fixed `beta<1`,

```text
|sum_(n<=x) f_z(n)| / x^beta -> infinity.
```

The resonance occurs at **every** sufficiently large scale, not merely on a
log-syndetic set.

There are two useful versions of the distance obstruction.  First take real
`z=r` with `0<r<1`.  Uniformly for every character `chi` and every real `t`,

```text
D(f_r, chi n^(it);x)^2 >= (1-r) sum_(p<=x) 1/p -> infinity.
```

Thus the general inverse gate is false even if its character and phase are
allowed to vary with `x`.

For the sharper Mobius-adjacent version, take `|z|=1`, `z!=-1`, and then let
`z` approach `-1`.  For any fixed Dirichlet character `chi` and real `t`, the
pretentious distance

```text
D(f_z, chi n^(it);x)^2
 = sum_(p<=x) [1-Re(z conj(chi(p))p^(-it))]/p
```

diverges.  For the principal character and `t=0` it equals

```text
(1-Re z) log log x + O(1),
```

and otherwise the twisted prime sum is bounded while `sum 1/p` diverges.
This is exactly the distance framework introduced by
[Granville--Soundararajan](https://arxiv.org/abs/math/0608407); sharp Halasz
bounds are consistent with, rather than contrary to, this example
([Granville--Harper--Soundararajan](https://arxiv.org/abs/1706.03755)).

Adding `n^(i gamma)` to `f_z` produces the same counterexample at any desired
observed Mellin phase.  Moreover, `z` can be chosen arbitrarily close to
`-1`, so its prime values are arbitrarily close to Mobius's while its
every-scale mean remains much larger than `x^beta`.

There is also a direct scale mismatch in Halasz's theorem.  A resonance
`|S(x)|=x^beta` has relative mean `x^(beta-1)`.  Inverting a bound of the form
`(1+M)e^(-M)` permits `M` as large as roughly `(1-beta)log x`; it does not
force `M=O(1)`.  Mobius's prime distance is only of logarithmic-logarithmic
size.  Therefore even the hypothetical log-syndetic upgrade would require a
new multiscale amplifier, not merely a sharper reading of standard Halasz.

## 6. Why the exact Mobius point is singular

At `z=-1`, the family becomes exactly

```text
f_-1(n)=mu(n),       product_p(1-p^(-s))=1/zeta(s).
```

The generic Selberg--Delange coefficient vanishes because
`1/Gamma(-1)=0`.  In fact the fixed logarithmic asymptotic coefficients at
the nonpositive-integer exponent vanish.  The zeta-zero contribution is
beyond every fixed order of that expansion.

Near `z=-1`, the leading generic mean is approximately

```text
(z+1) x / (log x)^2.
```

To resolve an exceptional `x^beta` Mobius signal through this deformation
would require

```text
|z+1| on the scale x^(beta-1)(log x)^2 -> 0.
```

Thus the desired inverse theorem is not robust under arbitrarily small
Euler-factor perturbations.  It would have to use the exact identity
`mu(p)=-1` and the exact reciprocal-zeta cancellation.  That is a new
Mobius-specific RH-scale theorem, not a consequence of resonance density plus
general pretentious machinery.

## 7. Final status and reusable result

The branch yields a useful corrected reduction:

```text
one off-line zero
  --known--> Pintz near-syndetic sharp-cutoff peaks
  --open-->  fixed smooth phase + constant log gaps
  --false--> general bounded-distance inverse theorem.
```

The lightweight finite scout
`src/mobius_residue_density_falsifier.py` displays the Selberg--Delange family
and its exact prime-distance growth.  It is illustrative only; the analytic
factorization above is the proof.

This route should not receive further RH allocation unless a genuinely
Mobius-specific invariant is found that is discontinuous at the exact
`z=-1` Euler factor for an independently arithmetic reason.  The next planned
orthogonal gate is the cyclotomic Lefschetz trace calculation.
