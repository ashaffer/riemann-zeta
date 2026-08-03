# Shifted-xi Schur/Loewner audit

Status: the shifted ratio is an exact unsigned carrier, but its infinitesimal
Loewner sign is already RH-equivalent; the analytic amplifier is pruned,
2026-08-01.

Put `s(z)=1/2+iz` and

`Theta_a(z)=xi(s(z)+a)/xi(s(z)-a)`.

The functional equation gives unit modulus on the real boundary, and an
upper-half-plane pole corresponds to a zero with real part less than
`1/2-a`, hence by symmetry to a zero with real part greater than `1/2+a`.
Thus the negative-square index of the Pick kernel is a valid unsigned carrier.

## Exact cocycle and generator

The parameter identity

`Theta_(a+b)(z)=Theta_a(z-ib)Theta_b(z+ia)`

is immediate and exact.  Differentiating gives

`partial_a log Theta_a(z)`

` = (xi'/xi)(s(z)+a)+(xi'/xi)(s(z)-a)`.

At `a=0`, where `Theta_0=1`,

`partial_a log Theta_a(z)|_(a=0)=2(xi'/xi)(s(z))`.

If `Theta_a` is Schur for every sufficiently small positive `a`, then

`Re (xi'/xi)(1/2+iz) <= 0` for every `Im(z)>0` away from poles.

Conversely, the Hadamard zero expansion shows that this sign throughout the
left half-plane holds exactly when no zero lies there off the critical line:
under RH each critical-line zero contributes with the required sign, while a
left off-line zero produces a logarithmic-derivative pole and violates it in
a punctured neighborhood.

The first-order Pick kernel makes the same equivalence explicit.  Expanding
`Theta_a=1+2a xi'/xi+O(a^2)`, positivity of `K_a/a` is precisely the
Caratheodory/Herglotz kernel condition for `-xi'/xi` in the left half-plane.

## Why the cocycle does not propagate positivity downward

The factor `Theta_a(z-ib)` samples below the upper half-plane whenever
`0<Im(z)<b`.  Hence ordinary Schur closure under products cannot infer small-
`a` positivity from a known larger shift.  Reversing the factorization cannot
recover positivity of either factor from their product.

The cocycle is therefore a correct evolution law but not a monotone Loewner
semigroup in the domain needed for propagation.

## Verdict

The generalized-Schur index remains an excellent *carrier* for off-line zeros:
it is unsigned, quantized on bounded windows, and completion-native.  But the
proposed analytic amplifier fails.  Its infinitesimal Herglotz sign is already
an RH-equivalent logarithmic-derivative condition, and the parameter cocycle
does not transport positivity from the unconditional range.

Path B should remain only as the target transfer function for a genuinely
independent geometric realization (Path C), not as a standalone Loewner proof.
