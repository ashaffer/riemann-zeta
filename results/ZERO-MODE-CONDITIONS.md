# Localized zero-mode conditions

Status: exact necessary weak conditions proved; uniqueness remains open.

For any nonnegative quadratic form, a zero-energy vector lies in the radical.
The scalar line argument is now formalized in Lean.  Applied to the zeta Weil
form, a hypothetical localized zero mode `u` must satisfy, against every test
variation `v`,

`B_pole(u,v) + B_arch(u,v)
    = sum_active B_primePower_n(u,v)`.

This is the distributional Euler--Lagrange equation in the normalization of
the repository.  The right side is a finite sum of symmetric translations by
`+/- log n`; the left side is the rank-two pole trace plus the nonlocal
digamma/Lerch trace.  In Suzuki language it says the polarized screw-kernel
functional vanishes against every old-supported variation.

This converts nondegeneracy into a uniqueness problem for a finite-delay
nonlocal equation with compact support.  A zero mode must simultaneously
satisfy:

1. support in `[-a,a]` and smooth endpoint matching;
2. the pole/digamma versus prime-shift balance for every interior variation;
3. even or odd parity after decomposing the even kernel;
4. all shift-interface conditions at `x = +/-a +/- log n`.

The next concrete task is to write the balance as a pointwise distributional
finite-delay equation and propagate zero boundary data inward across the
ordered shift interfaces.  If each propagation step is uniquely determined,
compact support overdetermines the solution and excludes a zero mode.  The
failure mode is equally informative: a free datum surviving an interface
would show why this uniqueness route cannot close without additional global
input.
