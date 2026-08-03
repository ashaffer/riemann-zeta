# Additive--multiplicative commutator audit

Status: the naive four-point invariant is trivial; the corrected commutator
detects a pole only after an RH-scale aggregate, 2026-08-01.

## 1. The proposed rectangle collapses

For a prime `p`, consider

`R_(p,h)(n) = mu(n)mu(n+h)mu(pn)mu(p(n+h))`.

On the locus where `p` divides neither `n` nor `n+h`, multiplicativity gives

`mu(pn)=-mu(n)`, `mu(p(n+h))=-mu(n+h)`.

Therefore

`R_(p,h)(n)=mu(n)^2 mu(n+h)^2`,

and it is zero on the excluded divisibility or nonsquarefree loci.  The
four-point statistic is just a squarefree-pair count.  It has discarded the
signs, the Mellin resonance, and any hypothetical zeta zero.  Adding a Mellin
phase afterward does not restore a pole of `1/zeta`; it merely modulates a
squarefree correlation.

Thus the initially proposed cocycle is not a viable invariant.

## 2. The genuinely noncommuting configuration

Let additive translation and prime dilation act by

`T_h f(n)=f(n+h)`, `D_p f(n)=f(pn)`.

Then

`D_p T_h f(n)=f(pn+h)`,

while

`T_h D_p f(n)=f(pn+ph)`.

The corrected finite commutator correlation for a finitely supported sequence
`f` is

`K_p(h)=sum_n f(n)(f(pn+h)-f(pn+ph))`.

This does not collapse under multiplicativity because `pn+h` usually has no
factor `p`.

## 3. Exact aggregate identity

Put `S=sum_n f(n)` and `S_p=sum_m f(pm)`.  Summing over every integer shift
and rearranging finite sums gives

`sum_h K_p(h)=S(S-S_p)`.                         `(C)`

Indeed `pn+h` runs over every integer as `h` varies, whereas `pn+ph` runs
over the multiples of `p`.

For the truncated Möbius sequence `f(n)=mu(n)1_(1<=n<=N)`, this becomes

`sum_h K_p(h)=M(N)(M(N)-sum_(m<=N/p)mu(pm))`.

The second factor is another explicitly prime-restricted Mertens sum.  A
hypothetical pole `rho=beta+i gamma` can therefore create aggregate size on
the scale `N^(2 beta)` along favorable scales, with computable local Euler
modification.

## 4. Why known additive uniformity does not contradict it

For fixed `p`, there are `O(pN)` relevant shifts.  An aggregate of size
`N^(2 beta)` forces only average commutator size

`N^(2 beta-1)`.

Because `1/2<beta<1`, this is `o(N)`.  Qualitative Chowla estimates and modern
higher-order short-interval uniformity give cancellation relative to the
length `N`; they do not supply the power-sensitive bound

`o(N^(2 beta-1))`

uniformly over the full shift range.  Summing an `o(N)` bound over `O(N)`
shifts permits `o(N^2)`, which is compatible with every `N^(2 beta)` for
`beta<1`.

Conversely, the exact identity `(C)` shows that a sufficiently strong bound on
the full commutator aggregate is directly a bound on `M(N)` and its local
restriction.  Without an independent sign, sparsity, or orthogonality gain,
such a bound is another square-root-cancellation target rather than a weaker
consequence of existing Gowers uniformity.

## Verdict

The question has a negative answer for the proposed invariant:

- the multiplicatively aligned four-point cocycle is sign-trivial;
- the genuinely noncommuting cocycle retains the sign but a pole forces it
  only in an all-shifts aggregate;
- present additive-uniformity theorems are quantitatively too weak at exactly
  the exceptional-zero scale.

A successor would need an exact mechanism concentrating `(C)` onto a sparse
family of shifts where an independent power-saving estimate is available.
Prime dilation alone spreads rather than concentrates the aggregate, so the
commutator does not currently provide that mechanism.
