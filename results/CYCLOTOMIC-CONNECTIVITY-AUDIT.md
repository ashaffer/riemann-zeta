# Cyclotomic connectivity audit

Status: the naive `THR(Z)` gamma-ladder proposal is falsified, 2026-08-01.

## Verdict

The formal spectrum `s, s+2, s+4, ...` has exactly the completed-zeta gamma
determinant up to an elementary exponential normalization.  But it is not the
complexified positive-degree spectrum of `THR(Z)`.

The Bökstedt splitting is

`THH(Z) = HZ ∨ ⋁_(k>=1) Sigma^(2k-1) HZ/k`,

and, away from 2, the real calculation has positive summands
`Sigma^(2k-1,k) H(Z/k)`.  Thus all positive-degree pieces are torsion and
vanish after complexification.  The mod-2 polynomial degree-two classes in
geometric fixed points cannot produce a complex regularized determinant.

Periodic `TP` has the opposite defect: its degree-two periodicity is
bi-infinite, while gamma requires a canonical one-sided ladder.  Existing
archimedean determinant constructions use a separate archimedean
cohomology/log-Frobenius object.  The determinant match is genuine; its
proposed native realization in `THR(Z)` was not.

## Consequence for the portfolio

The unified-`THR` route is pruned.  A weaker global construction might glue
finite-prime cyclotomic cohomology to an independently defined archimedean
cohomology.  That is not yet a construction, is not novel merely at the level
of local determinants, and still lacks the decisive positive polarization
`Theta* + Theta = 1`.  Further resources require evidence for canonical
gluing or for that pairing.

Primary references:

- Dotto--Moi--Patchkoria--Reeh, *Real topological Hochschild homology*,
  arXiv:1711.10226.
- Hesselholt, *Topological Hochschild homology and the Hasse--Weil zeta
  function*, arXiv:1602.01980.
- Consani--Marcolli, *Archimedean cohomology revisited*, arXiv:math/0407480.
- Morin, *Topological Hochschild homology and Zeta-values*, arXiv:2011.11549.
