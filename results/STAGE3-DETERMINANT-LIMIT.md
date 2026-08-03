# Stage 3: corrected determinant/de Branges target

## Entire-limit audit

Suzuki's 2026 finite-window characteristic function `W(a, theta; z)` is
entire and has only real zeros because it is the characteristic function of a
self-adjoint extension.  The paper proposes compact-uniform convergence on
all of `C` to

`z^2 xi(1/2-i z) / xi'(1/2-i z)`.

There is a necessary preliminary issue: a compact-locally uniform limit of
entire functions is entire, whereas this ratio is a priori meromorphic at
zeros of `xi'`.  Thus the stated convergence can hold only if all those
apparent poles are removable (or if the convergence domain/topology is
weakened).  The repository now kernel-checks the general entire-limit
consequence.  We should not assume this limit formula as written.

## Corrected target

The viable route is direct convergence to the completed critical-line xi
function, as suggested by the finite-dimensional regularized-determinant
construction of Connes--Consani--Moscovici:

1. construct entire finite-window characteristic functions independently of
   RH;
2. obtain real zeros from self-adjointness;
3. prove compact-local convergence, after nonvanishing normalization, directly
   to `z -> xi(1/2-i z)`;
4. apply Hurwitz to transfer real-zero rigidity to xi.

`Stage3DeterminantLimit.lean` formalizes this as
`DeterminantXiLimitTarget` and proves that it implies RH.  Classical Hurwitz
zero transfer and the normalization-matched xi/RH dictionary are explicit
literature axioms.  The determinant convergence itself is not assumed and is
the sole open research field of the package.

## Next analytic subproblem

Define the approximants concretely from the finite-dimensional restrictions
of the Weil operator, then prove a trace-class or canonical-product estimate
on compact sets.  Merely knowing that every approximant is self-adjoint is
insufficient; convergence and identification with xi carry the new content.

## Concrete two-parameter package

`Stage3CCMDeterminant.lean` now formalizes the actual shape of the
Connes--Consani--Moscovici proposal.  A cofinal sequence must send both the
support parameter `lambda` and Fourier cutoff `N` to infinity.  Each finite
window supplies an entire real-zero characteristic function, and an arbitrary
zero-free entire normalization is allowed.  Lean proves that normalization
preserves the real zero set and that compact-local convergence to critical xi
implies RH.

The finite-level construction has two hypotheses that are not currently known
uniformly: the lowest eigenvalue of the truncated Weil matrix is simple and its
eigenvector is even.  The paper's self-adjoint perturbation and determinant
identity assume these properties.  They therefore form the first concrete
subproblem; after that, the genuinely global subproblem is compact-local
control along a cofinal `(lambda,N)` sequence.

`Stage3FiniteWindowParity.lean` proves abstractly that reflection commutation
and a simple lowest eigenspace force the eigenvector to be even whenever the
reflection-invariant Dirichlet boundary functional is nonzero on it.  This is
an alternative formulation, not yet a net reduction: the CCM commutator
argument derives boundary nonvanishing only after evenness is assumed.

`Stage3ParityNoGo.lean` gives an axiom-free simple odd ground-state model.
Thus reflection symmetry and simplicity alone cannot prove the needed parity.
The first genuinely zeta-specific finite target is now the strict block
ordering

`lowest even Weil eigenvalue < lowest odd Weil eigenvalue`,

together with simplicity inside the even block.  Prolate-wave operators have
this property, but transferring it to the Weil matrices is one of the two
missing steps explicitly identified by CCM.

## Parity-ordering falsification screen

`src/ccm_parity_scan.py` evaluates the actual high-precision Legendre--Weil
Galerkin matrices and splits them into reflection-even and reflection-odd
blocks.  At dimension 16, the strict ordering survived the first scan:

| support | even minimum | odd minimum | odd minus even |
|---:|---:|---:|---:|
| 1.000 | 3.337e-2 | 4.090e-1 | 3.756e-1 |
| 1.750 | 3.190e-5 | 4.027e-3 | 3.995e-3 |
| 2.485 | 4.468e-9 | 4.074e-7 | 4.029e-7 |
| 2.996 | 1.286e-10 | 3.023e-8 | 3.010e-8 |
| 3.555 | 1.901e-11 | 3.324e-10 | 3.134e-10 |
| 4.000 | 9.762e-13 | 5.998e-10 | 5.988e-10 |
| 5.000 | 1.457e-13 | 7.930e-12 | 7.784e-12 |
| 6.000 | 1.558e-14 | 4.504e-13 | 4.348e-13 |
| 8.000 | 9.036e-17 | 1.789e-14 | 1.780e-14 |

This supports viability but is not a proof: these are Galerkin upper values,
and the gap collapses rapidly.  No uniform positive separation is suggested.
The result points toward a relative/interlacing theorem or a controlled
comparison with the prolate operator, not an absolute spectral-gap estimate.

## Comparator normalization correction

The actual CCM comparison vector is not a single prolate ground mode.  It is
`k_lambda = E(h_lambda)`, where `h_lambda` is the normalized zero-integral
linear combination of prolate modes 0 and 4.  CCM prove that
`Fourier(k_lambda)` converges to completed xi uniformly on closed substrips.
Accordingly, the global determinant problem compresses to proving that the
normalized lowest Weil eigenvector approaches this specific `k_lambda` in a
topology strong enough to transfer its Fourier transform.  Any future
experiment using an ordinary top-concentration vector alone tests the wrong
identification.
