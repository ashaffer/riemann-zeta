# Shifted-xi adelic realization: first local gate

Status: factorwise passive realization is obstructed; only an irreducibly
global colligation could survive, 2026-08-01.

For `s=1/2+iz`, the finite-prime part of the shifted ratio has local factors

`theta_(p,a)(z)`

` = (1-p^(-(s-a)))/(1-p^(-(s+a)))`.

On the real boundary write `p^(-ix)=exp(-ix log p)`.  When this phase is near
`-1`,

`|1+p^(-(1/2-a))| / |1+p^(-(1/2+a))| > 1`.

Thus each local factor has boundary arcs of gain greater than one.  It cannot
be the transfer function of a passive Hilbert-space colligation.  For every
finite set of primes, simultaneous Diophantine approximation of the phases
produces real frequencies where all selected local gains point in the same
nonpassive direction.

The exact completed ratio nevertheless has unit boundary modulus because the
functional equation couples the globally continued zeta function to the
archimedean factor.  That cancellation is not present in a finite Euler
product and cannot be repaired by declaring each prime channel passive.

## Consequence

The proposed finite-`S` positive-colligation gate fails in its natural
factorwise form.  This repeats, in the sharper shifted-ratio setting, the
orientation obstruction found for passive Euler cascades.

An irreducibly global adelic mapping cone could still in principle realize
`Theta_a`, but its positivity would have to come from the global Poisson
relation before Euler decomposition.  General realization theory alone is no
help: it assigns a Pontryagin negative index equal to the poles, which merely
records the off-line-zero count.

## Verdict

Prune all constructions assembled from positive local prime colligations plus
an archimedean correction.  Retain Path C only if an explicit global Poisson
state space yields `Theta_a` and a Hilbert metric in one step, with neither xi
nor its Pick kernel inserted as input.  No such construction is currently in
hand, so the path is downgraded to long-horizon speculative status.
