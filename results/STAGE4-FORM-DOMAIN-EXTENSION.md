# Stage 4 full form-domain extension

## Status

The dense-core extension theorem is formalized.  Applying it to the CCM
residual requires one genuinely additional estimate: uniform boundedness of
the residual functionals in the logarithmic form norm.

Density alone is insufficient.  On `ell^2`, the functionals
`L_n(x)=n x_n` vanish eventually on the dense finite-support core, while for
`x_n=1/n` one has `L_n(x)=1`.  Their operator norms diverge.  Thus extending
the smooth Stage-4 theorem without an equicontinuity estimate would be an
invalid argument.

## Exact extension theorem

Let `D_b` be the completed logarithmic form domain at a fixed compact support
`b`, and let

`L_lambda(g) = WeilCross(k_lambda, embed_b_to_lambda(g))`.

If

1. globally `C^2` compact tests are dense in `D_b`;
2. `sup_lambda ||L_lambda||_(D_b^*) < infinity`; and
3. `L_lambda(g) -> 0` on that smooth core (proved in Stage 4),

then `L_lambda(g) -> 0` for every `g in D_b`.

`Stage4FormDomainExtension.lean` proves this implication with an explicit
epsilon argument and no mathematical axioms.

## Remaining analytic target

The useful route to condition 2 is not absolute pointwise zero decay.  It is a
weighted sampling estimate for Paley--Wiener transforms at the zeta zeros,
combined with convergence of the CCM comparator in the logarithmic graph
norm:

`||k_lambda-k||_log -> 0`,

where the transform of `k` is `Xi` and therefore vanishes on the zero set.
The expected ingredients are:

- the `O(lambda^-2)` uniform prolate-to-Hermite approximation;
- its resulting `O(lambda^-1/2)` logarithmic-coordinate `L^2` error after
  applying `E`;
- a polynomial first-derivative bound for that error;
- logarithmic interpolation between `L^2` and `H^1`;
- a multiplicity-weighted Paley--Wiener sampling inequality whose density
  cost is exactly the logarithmic Fourier weight.

Equivalently, the single load-bearing comparator estimate is

`sum_rho multiplicity(rho)
  (|K_lambda(rho-1/2)|^2 + |K_lambda(1/2-rho)|^2)
  / log(2+|Im rho|) -> 0`.

The fixed-support sampling inequality would then bound the residual against
an arbitrary logarithmic-domain `g` by the square root of this quantity times
`||g||_log`.  This is exactly the uniform dual convergence consumed by the
formal extension theorem.

Compact-strip convergence does not imply this global weighted statement.  Its
proof must combine the low-ordinate CCM Mellin remainder with high-ordinate
endpoint estimates for the truncated prolate vector.  This is the current
unclosed Stage-4 checkpoint.

Together these would give convergence in the dual form norm, stronger than
mere boundedness, and complete the full-domain extension.  None of these
steps assumes RH, but the weighted sampling statement must be checked for
off-line zero quartets rather than silently using critical-line sampling.
