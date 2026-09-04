# QP hybrid affine compression transfer

**Date:** 2026-08-29

**Status:** proved transfer theorem and exact falsification of the previous
factorial formulation.  The global affine extractor/packing theorem remains
open, so the sharp four-cycle bound is not proved here.

## 0. Result

The affine peel must be performed on physical completion rectangles before
ordered completion pairs are formed.  This removes the apparent mismatch
between the linear mass controlled by the affine/Hankel theorem and the
factorial mass stored by A2.

For every oriented color rectangle `C`, let `Gamma(C)` be its completion
occurrences and make one global, completion-consistent partition

```text
Gamma(C)=G(C) disjoint_union R(C),
g_C=|G(C)|,                 r_C=|R(C)|,
w(C)=product_(i,j)|z_(c_ij)|.
```

The direct positive four-cycle mass splits exactly:

```text
S=sum_C (g_C+r_C)w(C)=S_G+S_R.                       (0.1)
```

Host every completion in `G` exactly once in a certified pair-unique
affine/Hankel patch.  For patch `t`, let

```text
l_(t,c)=number of its matrix entries of color c,
L_t=max_c l_(t,c),
M_t=number of colors in the patch,
mu_t=min(L_t,M_t).
```

Define the affine Carleson load

```text
H_aff=max_c sum_t mu_t*l_(t,c).                      (0.2)
```

### Theorem HAC -- pre-factorial hybrid affine compression

If

```text
H_aff <<D q^o(1),                                   (0.3)
```

and the A2 serializer is regenerated only on ordered distinct pairs of
residual completions and its zero-remainder A4 certificate proves

```text
P_R=sum_C r_C(r_C-1)w(C)
    <<D q^o(1)||z||_2^4,                            (0.4)
```

then

```text
S<<D q^o(1)||z||_2^4.                               (0.5)
```

Thus `(0.3)` plus residual A2/A4 is a legal sufficient theorem for the sharp
positive four-cycle estimate.  With the existing exceptional-sector
reductions, it is sufficient for the project's sharp four-cycle bound.

## 1. Proof of the direct affine charge

Put

```text
x_c=|z_c|^2,
X_t=sum_(c in K_t)x_c,
F_t=sum_c l_(t,c)x_c.
```

The proved partial-matching patch lemma gives, for the absolute rectangle
mass `Q_t` assigned to patch `t`,

```text
Q_t<=min(F_t^2,M_t X_t F_t)
   <=mu_t X_t F_t.                                  (1.1)
```

The first branch is `||A_t||_F^4`; the second is
`||A_t||_op^2||A_t||_F^2`.  Since `X_t<=X=sum_c x_c`, positivity and `(0.2)`
give

```text
S_G
 <=sum_t mu_t X_t F_t
 <=X sum_c x_c sum_t mu_t l_(t,c)
 <=H_aff X^2
 =H_aff||z||_2^4.                                   (1.2)
```

This is the global summation condition missing from the earlier collection
of local affine-patch theorems.  Individual `O(D)` patch bounds do not imply
`(0.3)`.

## 2. Proof of the residual transfer

Let

```text
W_R=sum_(C:r_C>0)w(C).
```

The existing determinant-layer matching theorem gives

```text
W_R<=W_full<<D q^o(1)||z||_2^4.                    (2.1)
```

For every integer `r>=0`,

```text
r<=1_(r>0)+r(r-1)/2.                               (2.2)
```

Multiplying by `w(C)` and summing proves

```text
S_R<=W_R+P_R/2<<D q^o(1)||z||_2^4.                 (2.3)
```

Together with `(1.2)`, this proves `(0.5)`.  The familiar Cauchy form is also
valid:

```text
S_R^2<=W_R sum_C r_C^2w(C)=W_R(S_R+P_R).           (2.4)
```

## 3. Why the previous formulation was false

Factorial mass does not split linearly:

```text
(g+r)(g+r-1)
 =g(g-1)+r(r-1)+2gr.                               (3.1)
```

Direct affine trace bounds `g`; they bound neither `g(g-1)` nor the mixed
term `2gr`.  It is therefore invalid to retain the old full A2 manifest and
mark affine or affine--residual pair atoms as a harmless remainder.  A4
correctly rejects any positive remainder.

The legal operation is to restart the quadratic bootstrap on `R(C)` and
regenerate its A2 source manifest.  The full PAIR form is not proved, but it
is no longer needed: the structured first moment has already been charged
directly in `(1.2)`.

The full-integer multilevel tangent family makes the distinction unavoidable.
All its triples lie in one affine plane and its direct trace is `O(D)`, while
its spiked positive factorial mass is `Theta(D^(5/4))`.  It is not an
actual-prime counterexample, but it disproves any theorem that attempts to
deduce positive factorial compression from the existing affine geometry.

## 4. What remains open

The sought existence theorem is now exact:

> Construct a completion-consistent affine/residual partition for every
> actual QP cell, host every affine completion in a four-edge certified
> patch, prove `H_aff<<Dq^o(1)`, and give every induced residual signed cell
> a zero-remainder A2 cover satisfying the A4 load product
> `LR<<D^2q^o(1)`.

The project currently proves the local host theorem for one affine plane,
complete thickened exact-AP grids with fixed parameters, and rich lines of
one fixed primitive direction.  It does not prove cross-direction Carleson
packing, and it does not classify the one-/two-point scattered secants.

The literal `q=25013`, `U=40` falsifier reinforces the quantifiers.  Natural
affine directions retain only `60/5604` ordered atoms, but the `5288`-atom
remainder still has A4 value `4`, against target `18225`.  Consequently the
right theorem is packet-or-dispersive-remainder, conditional on genuine
operator excess; it is not unconditional positive-mass capture.

## 5. Verification

The exact finite algebra and the Carleson summation are replayed in

```text
src/qp_hybrid_affine_compression.py
src/test_qp_hybrid_affine_compression.py
```

Lean certifies the factorial split, the residual integer inequality, its
weighted form, and the quadratic Cauchy transfer in

```text
lean/weilcert/QPHybridAffineCompression.lean.
```

The independent literal audit is

```text
results/ZETA23-QP-AFFINE-COMPRESSION-LITERAL-FALSIFIER-AFFINE-FALSIFIER-2026-08-29.md.
```
