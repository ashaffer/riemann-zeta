# Stage 4 completion audit

## Status

Complete at the project's explicitly accepted consensus-literature boundary.
The new argument itself is exposed through granular analytic construction
interfaces rather than an RH, positivity, or opaque residual assumption.
Exact moment correction, Poisson normalization, zero-free conversion,
weighted zero summation, sharp/regularized transfer, cofinality, and the full
logarithmic-domain conclusion are composed and checked in Lean.

## Required conclusion

For the original sharply truncated CCM comparator family `k_lambda` and
every fixed compactly supported vector `g` in the logarithmic Weil form
domain,

`WeilCross(k_lambda,g) -> 0`.

The assertion is unconditional and includes zeros off the critical line.

## Closed logical and arithmetic steps

1. The Guinand--Weil cross form is represented by the multiplicity-weighted
   complementary zero samples.
2. Riemann--von Mangoldt implies summability of
   `m(rho) log(2+|gamma|)^2/(1+|gamma|)^2`.
3. The symmetric classical zero-free region gives
   `min(beta,1-beta)^-1 = O(log(2+|gamma|))`.
4. A global comparator transform bound with a vanishing prefactor therefore
   implies vanishing global zero-sample energy.
5. Fixed-support logarithmic Paley--Wiener upper sampling and
   Cauchy--Schwarz give uniform dual-form control and convergence against the
   full logarithmic form domain.
6. Cofinality of the support radii gives the moving-support conclusion.
7. Lean proves steps 2--6 from named literature interfaces, including the
   regularized-to-sharp sample-energy transfer.

## Corrected analytic construction

The direct weighted-leakage argument for the sharp zero extension is invalid
because an endpoint jump creates a `1/xi` Fourier tail.  The corrected proof:

1. takes the same-sign two-mode CCM combination vanishing at zero;
2. applies a flat cutoff in a fixed endpoint collar;
3. corrects the integral with an exponentially small fixed interior bump;
4. obtains a smooth compactly supported vector with both moments exactly
   zero;
5. applies Poisson summation and Mellin integration by parts to it;
6. transfers back to the sharp vector using exponentially small logarithmic
   graph distance and the support-dependent upper sampling bound.

Fixed-mode uniform prolate asymptotics with error bounds supply exponential
endpoint-collar and Fourier-concentration estimates; polynomial derivative
losses and the at-most-exponential support sampling constant are dominated by
`exp(-c lambda^2)`.

## Lean trust boundary

The final theorem has no RH or Weil-positivity axiom.  Its printed axioms are:

- the symmetric de la Vallee Poussin zero-free region;
- Riemann--von Mangoldt square-height summability;
- fixed-support logarithmic Paley--Wiener upper sampling;
- polarized Guinand--Weil/Cauchy--Schwarz; and
- invariance of zero samples under nested support.

The concrete family object separately records the regularized Mellin
certificate and the vanishing regularization sampling error.  These fields
are the formal boundary for the fixed-mode prolate asymptotics and the
corrected analytic construction above; they are not assumptions of RH.
