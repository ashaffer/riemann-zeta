# Low-energy rigidity obstruction

Status: the proposed implication from small old energy alone is false.  The
exact additional zeta-specific target has been isolated.

Let

`R(u,v) = B_pole(u,v) + B_arch(u,v) - B_prime(u,v)`.

Small `Q_old(u)` controls the old compression of the Euler--Lagrange operator.
It does not, by itself, control its projection into the collar.  The scalar
symmetric block matrix

`[[0, M], [M, D]]`

has zero old energy and arbitrary boundary residual `M`.  It is indefinite,
but it demonstrates that self-adjointness, low energy, and collar positivity
do not imply trace cancellation.  Lean now contains this obstruction.

For fixed old and collar vectors, Lean also proves the exact equivalence

`R(u,v)^2 <= Q_old(u) Q_collar(v)`

if and only if the form is nonnegative on every line `u+t v`.  Therefore the
desired universal boundary rigidity estimate is precisely mixed positivity,
not a weaker consequence of the low-energy hypothesis.

## Correct next target

The numerical cancellation remains meaningful: it suggests an additional
identity special to approximate ground states of the zeta screw kernel.  A
non-circular theorem would have to look like a boundary unique-continuation
or Euler--Lagrange estimate:

`||P_collar A_b u||_(Q_collar^{-1})^2 <= kappa Q_a(u)`,

with `kappa < 1`, proved from the explicit pole + Lerch/digamma - prime-ramp
kernel and the old-sector Euler--Lagrange equation.  Merely assuming this
estimate would assume the missing Schur inequality.

The next useful investigation is therefore to derive the distributional
Euler--Lagrange equation for the localized Suzuki kernel and compute its
boundary residual explicitly.  The observed three-way cancellation may then
become a boundary identity plus a controllable eigenvalue remainder.  Until
that derivation exists, “low-energy rigidity” is numerical evidence rather
than a theorem.
