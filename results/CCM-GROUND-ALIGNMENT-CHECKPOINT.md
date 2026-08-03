# CCM ground-alignment checkpoint

Status: numerical falsification checkpoint, 2026-07-31.

## Question

Does the canonical Connes--Consani--Moscovici vector merely align with the
lowest localized Weil eigenvector in `L2`, or does it approximate that vector
in the relative energy topology needed for a support-uniform Feshbach proof?

The tested vector is the CCM same-Fourier-sign combination of angular prolate
modes 0 and 4 which vanishes at the origin, followed by the arithmetic map

`E(h)(u) = sqrt(u) * sum_(n >= 1) h(nu)`.

It is projected into the orthonormal Legendre Galerkin space used by
`spectral_margins.py`.  For the resulting unit vector `k` and Weil matrix `Q`,
the diagnostic is

`R = 1 - 1 / (<k,Qk> * <k,Q^(-1)k>)`.

This is exactly the Schur ratio `<b,C^(-1)b>/<k,Qk>` in the decomposition
`span(k) + k^perp`.  Thus `0 <= R < 1` for a positive finite matrix, `R = 0`
when `k` is an eigenvector, and a support-uniform comparison needs `R` bounded
away from one.  The test is scale-free and therefore does not conceal the
collapsing Weil margin in an absolute error tolerance.

## Refined computation

Command:

```text
python3 src/ccm_ground_alignment.py \
  --supports 2.485 2.996 3.1 3.2 3.3 3.4 3.5 3.555 \
  --dimension 36 --prolate-nodes 240 --x-nodes 400 --dps 70
```

Representative output:

| support | lowest eigenvalue | `L2` alignment | scalar defect | `R` |
|---:|---:|---:|---:|---:|
| 2.485 | 3.65e-10 | 0.999999368 | 4.63e-10 | 0.211916 |
| 2.996 | 5.13e-15 | 0.999999988 | 6.23e-15 | 0.176737 |
| 3.100 | 4.47e-16 | 0.999999995 | 2.44e-14 | 0.981677 |
| 3.200 | 6.17e-17 | 0.999999703 | 4.87e-14 | 0.998735 |
| 3.300 | 7.49e-18 | 0.999997866 | 1.13e-13 | 0.999934 |
| 3.400 | 3.29e-18 | 0.999995280 | 2.96e-13 | 0.999989 |
| 3.500 | 3.15e-18 | 0.999914607 | 8.65e-13 | 0.999996 |
| 3.555 | 9.36e-19 | 0.999861991 | 7.66e-12 | 0.999999878 |

At support 3.555, changing the Galerkin dimension from 32 to 36 and the
prolate quadrature from 180 to 240 changed the last digits but not the verdict:
`R` remained above `0.9999996`.  The implementation uses multiprecision for
the Weil eigensystem and for the inverse quadratic form; fixed-degree
differential PSWFs avoid the arbitrary rotations caused by numerically
degenerate finite-Fourier eigenvalues.

## Verdict

The strong `L2` alignment is real but is not the required relative-energy
alignment.  Once the lowest spectral scales collapse, a minute component in
higher modes dominates `<k,Qk>` and drives the Feshbach ratio to one.  The
plain CCM-vector relative-gap route therefore fails its stated kill rule.

This does not refute CCM determinant convergence or RH.  It says that a proof
cannot pass directly from `L2` alignment to support-uniform positivity.  A
viable repair would need a corrected comparator which cancels the energetic
tail, or a new theorem giving convergence in the graph norm of the localized
Weil operator.  Either repair is substantially stronger than the alignment
observed so far and is the next honest analytic checkpoint.

The values are numerical evidence, not certified interval bounds.  SciPy's
spheroidal evaluator becomes unreliable at still larger parameters, so those
scales require an independent high-precision PSWF implementation before they
can sharpen this conclusion.
