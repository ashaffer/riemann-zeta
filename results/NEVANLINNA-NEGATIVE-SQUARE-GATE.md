# Generalized-Nevanlinna negative-square census

Status: abstract index theorem validated; arithmetic promotion gate failed;
path demoted to a diagnostic; 2026-08-01.

## 1. Completed real entire function

Set

`Xi(z)=xi(1/2-i z)`.

Then `Xi` is a real entire, even function: `Xi(conjugate(z))` is the conjugate
of `Xi(z)`, and `Xi(-z)=Xi(z)`.  RH says exactly that all its zeros are real.

Define the meromorphic logarithmic derivative

`m(z)=-Xi'(z)/Xi(z)`.

For points of holomorphy in the upper half-plane, form the Nevanlinna kernel

`N_m(z,w)=(m(z)-conjugate(m(w)))/(z-conjugate(w))`.

If all zeros are real, the canonical logarithmic-derivative expansion writes
this kernel as a positive sum of rank-one Cauchy kernels.  Hence `m` is a
Nevanlinna/Herglotz function.

## 2. Exact finite-zero index theorem

Let `P` be a real polynomial, or a finite real-symmetric canonical product,
with no zero at the sample points, and put `m_P=-P'/P`.  If `P` has `kappa`
distinct zero locations in the open upper half-plane, then `m_P` has exactly
`kappa` negative squares:

1. every Pick matrix `(N_m(z_j,z_l))` has at most `kappa` negative
   eigenvalues;
2. some finite set of upper-half-plane sample points realizes exactly
   `kappa` negative eigenvalues.

This is the rational logarithmic-derivative instance of generalized
Nevanlinna factorization.  It can also be seen directly.  A real zero `a`
contributes

`1/((a-z)(a-conjugate(w)))`,

a positive rank-one kernel.  A nonreal conjugate pair contributes an
indefinite two-feature block with one negative direction.  Independence of
the Cauchy features lets sufficiently many evaluation points realize all of
those directions.

For zeta, an ordinary off-line quartet

`beta +/- i gamma`, `1-beta +/- i gamma`

maps to two zeros of `Xi` in the upper half-plane and their two conjugates
below.  It therefore contributes **two negative squares** in the complex Pick
space.  This last count is for distinct locations.  If a nonreal zero has
algebraic multiplicity `r`, its logarithmic-derivative residue is multiplied
by `r`, but the same rank-one Cauchy feature is merely rescaled; the scalar
Pick-kernel negative index does not automatically increase by `r`.

The diagnostic `src/nevanlinna_negative_square_scan.py` illustrates the
theorem: a real-zero model has no negative eigenvalues, while adding one
off-axis quartet produces exactly two.

## 3. Infinite zeta statement

Subject to the standard canonical-product limiting interpretation:

- RH implies `m` belongs to the ordinary Nevanlinna class `N_0`;
- if `Xi` has finitely many upper-half-plane zeros, `m` lies in `N_kappa`,
  where `kappa` is their number of distinct locations;
- if it has infinitely many, the Pick kernels have unbounded negative index
  rather than membership in any finite `N_kappa`.

Thus the negative-square index solves the small-amplitude problem perfectly.
A zero arbitrarily close to the real line still contributes an integer unit
of index.

## 4. Comparison with the finite-zero Weil form

For a finite zero multiset with the involution

`tau(rho)=1-conjugate(rho)`,

the Weil pairing is

`Q(F)=sum_rho F(rho) conjugate(F(tau(rho)))`.

A critical-line zero is a fixed point of `tau` and contributes `|F(rho)|^2`.
Each two-element off-line `tau` orbit contributes the Hermitian block

`[[0,1],[1,0]]`,

with signature `(1,1)`.  A full off-line quartet consists of two such orbits,
again giving two negative directions.  Entire interpolation realizes
independent values on any finite zero set.

Therefore the Nevanlinna negative-square census and the finite-zero Weil
signature on the space of distinct evaluation values are the same invariant
in two coordinate systems.  A multiplicity-sensitive jet construction is a
different enlargement and is not supplied by the scalar logarithmic
derivative kernel above.

## 5. Arithmetic-side decomposition

Writing `s=1/2-i z`, one has

`m(z)=i xi'(s)/xi(s)`

and hence the exact completed decomposition into pole, gamma, and Euler terms:

```
m(z)=i [1/s + 1/(s-1) - (1/2)log pi
        + (1/2)psi(s/2) + zeta'(s)/zeta(s)].
```

The Euler Dirichlet series for `zeta'/zeta` converges only in `Re(s)>1`, which
corresponds to the upper sub-half-plane `Im(z)>1/2`.  Extending the Pick kernel
through the remainder of the upper half-plane encounters precisely the poles
at the hypothetical off-line zeros whose index is being sought.

Applying the explicit formula to finite Pick combinations produces the
completed Weil quadratic form: prime, pole, and archimedean terms together.
Consequently the available arithmetic computation of the index is

`supremum of negative eigenvalue counts of completed Weil Gram matrices`.

This is a definition/minimization of the same index, not a local trace or
place-by-place formula.  The prime part is not trace class by itself at the
required boundary, and the completion counterterms do not preserve negative
index additively.

## 6. Why no local index sum follows

Negative index is not additive under sums of Hermitian kernels.  A positive or
negative eigenvalue of one local block can cross zero after another place is
added.  The explicit formula's local conductor terms therefore cannot be
assigned integers and summed without first constructing a Fredholm pair or a
spectral-flow homotopy with controlled essential spectrum.

Neither generalized Nevanlinna factorization nor Suzuki's trace-class theorem
for each finite window supplies that global Fredholm structure.  Computing
`kappa` from `m` by contour winding is exactly the argument-principle count of
upper-half-plane zeros.

## 7. Gate verdict

The checkpoint has a clean mixed outcome:

- **validated:** negative squares give the desired phase-sensitive,
  small-amplitude-proof integer carrier;
- **identified exactly:** two negative squares per off-line zeta quartet;
- **failed promotion:** the known arithmetic realization is the completed
  Weil form itself, and the alternative analytic computation is zero counting;
- **missing object:** a global Fredholm pair or relative index whose value is
  computable from local conductor/commutator data.

Path 1 is therefore demoted as an independent proof route, but it has produced
the correct target for Path 2.  The next justified checkpoint is Burnol's
adelic conductor-commutator route, beginning with the compactness and
summability audit required to define a relative index at all.

## Literature anchors

- M. Suzuki, *Aspects of the screw function corresponding to the Riemann
  zeta-function* (2023).
- A. Dijksma, H. Langer, A. Luger, and Yu. Shondin, factorization theory for
  generalized Nevanlinna functions.
- H. de Snoo, H. Winkler, and M. Wojtylak, *Zeros of nonpositive type of
  generalized Nevanlinna functions with one negative square* (2011).
