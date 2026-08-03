# Theta Laguerre density under heat evolution

Status: exact PDE derived; the elementary maximum-principle route is pruned,
2026-08-01.

Let `H=H_t(x)` satisfy the backward heat equation

`H_t = -H_xx`

and define its first Laguerre density

`L = H_x^2 - H H_xx`.

Differentiation gives the exact identities

`L_xx = H_xx^2 - H H_xxxx`,

`L_t = H_xx^2 - 2 H_x H_xxx + H H_xxxx`,

and hence

`L_t + L_xx = 2(H_xx^2 - H_x H_xxx)`.

The forcing term has no fixed sign for a general heat datum.  Modularity of
the initial theta kernel does not remove the mixed derivative term locally.
Therefore `L` is not governed by a closed scalar parabolic inequality to
which the ordinary maximum principle applies.

At a common real zero `H=H_x=0`, one has

`L=0`, `L_x=0`, and `L_t=L_xx=H_xx^2`.

These equalities are compatible with tangential creation or annihilation at a
first collision; they do not yield a sign contradiction.  Thus the local PDE
at the collision contains no automatic no-collision mechanism.

Together with `THETA-LAGUERRE-CONVOLUTION-AUDIT.md`, this prunes two generic
routes: convex Fourier criteria and an elementary maximum principle.  A
surviving theta argument must use a genuinely nonlocal modular identity or a
new monotone quantity involving more than the first Laguerre density.
