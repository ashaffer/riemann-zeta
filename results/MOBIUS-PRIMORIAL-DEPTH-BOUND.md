# Primorial-depth bound for Möbius resonance channels

Status: the natural growing-depth coprimality tree is quantitatively pruned,
2026-08-01.

Let `rho=beta+i gamma` be a hypothetical zero with `1/2<beta<1`, and let

`q_y = product_(p<=y) p`.

The residue multiplier on the `q_y`-coprime Möbius Dirichlet series is

`R_y(rho) = product_(p<=y) (1-p^(-rho))^(-1)`.

Elementary absolute-value bounds give

`exp(-O(sum_(p<=y) p^(-beta))) <= |R_y(rho)|`

`<= exp(O(sum_(p<=y) p^(-beta)))`.

By the prime number theorem,

`sum_(p<=y) p^(-beta) = O(y^(1-beta)/log y) = o(y)`.

Hence the pole residue changes only by `exp(o(y))` across the full primorial
exclusion.  In contrast, the corresponding dilated channel has density

`phi(q_y)/q_y^2 = exp(-y+o(y))`.

Even the formal number of subset branches is

`2^(pi(y)) = exp(O(y/log y)) = exp(o(y))`.

Therefore the most optimistic aggregate obtained by multiplying channel
density, the largest allowed Euler residue multiplier, and all formal branch
counts is still

`exp(-y+o(y)) -> 0`.

This is not merely a missing constant: the density loss is exponential in
`y`, whereas both residue amplification and branch entropy are subexponential.
Selecting a sparser sequence of larger primes only worsens density per new
branch.  Repeating a prime is unavailable because `mu(p^2 n)=0`.

## Verdict

The fixed-depth pole propagation theorem is exact and useful, but the natural
prime-dilation construction cannot amplify it to positive-density entropy at
unbounded depth.  Reviving this path would require a different notion of
information that does not weight branches by their ambient integer density,
plus an inverse theorem capable of using that notion.  The originally
proposed positive-measure nested-block contradiction is pruned.
