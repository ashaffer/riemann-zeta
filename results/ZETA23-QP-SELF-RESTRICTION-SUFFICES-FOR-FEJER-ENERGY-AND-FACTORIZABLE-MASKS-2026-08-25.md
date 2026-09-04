# QP reciprocal strip: diagonal self restriction suffices for the Fejer energy

**Date:** 2026-08-25  
**Verdict:** the sharp mixed dependence on `min(U,V)` is not needed to close
the scalar squared-Fejer completion energy.  A uniform hereditary **self**
restriction theorem at every width implies, by Fourier Cauchy, a weaker
symmetric mixed theorem; the exact `U^(-2)V^(-2)` Fejer weights absorb its
entire imbalance loss.  The remaining physical nonfactorable-tensor and
intertwining gaps are unchanged.

## 1. Diagonal hypothesis and the exact mixed consequence

For every dyadic `U`, assume uniformly in the shell and centre that every
complex sequence supported on

```text
A_U={a: ||C/a||<=c U/H}
```

satisfies

```text
||z*z||_2^2
 <=sqrt(D*U)*q^o(1)*||z||_2^4.                       (1.1)
```

For `z` supported on `A_U` and `y` supported on `A_V`, Plancherel and
Cauchy--Schwarz give exactly

```text
||z*y||_2^2
 =integral |zhat|^2 |yhat|^2
 <=(integral |zhat|^4)^(1/2)(integral |yhat|^4)^(1/2)
 <=sqrt(D)*(U*V)^(1/4)*q^o(1)*||z||_2^2||y||_2^2.   (1.2)
```

Compared with sharp mixed RSR, the energy constant loses only

```text
((max(U,V))/(min(U,V)))^(1/4).                       (1.3)
```

No positivity is used, so (1.2) retains arbitrary selected coefficients.
The hypothesis itself must be hereditary; a self-energy estimate only for
the full set `A_U` does not suffice for adversarial coefficients.

Up to dyadic-amplitude logarithms, (1.1) is equivalent to the strictly
diagonal hereditary flat theorem

```text
E^+(B)=||1_B*1_B||_2^2
 <<sqrt(D*U)*|B|^2*q^o(1)       for every B subset A_U. (1.4)
```

Indeed, Fourier Cauchy first turns (1.4) for two subsets `B,E subset A_U`
into the corresponding mixed flat estimate at the same width.  Decomposing
an arbitrary `|z|` into dyadic amplitude levels and using Minkowski then
recovers (1.1), with logarithms absorbed into `q^o(1)`.  Conversely, (1.1)
implies (1.4) by taking `z=1_B`.  Thus the new arithmetic target is a
one-family hereditary `Lambda(4)` theorem, not a two-width incidence theorem.

It is sharp in power.  At the symmetric centre, `A_U` contains a tangent
interval of length `L asymp sqrt(D*U)`, and its normalized self energy is

```text
E^+([1,L])/L^2=2L/3+1/(3L).                          (1.5)
```

## 2. Exact Fejer exponent sum

The one-product divisor count is

```text
|A_U|<<D*U*q^o(1).                                   (2.1)
```

For flat indicators, (1.2) and (2.1) imply

```text
||1_(A_U)*1_(A_V)||_2^2
 <<D^(5/2)*(U*V)^(5/4)*q^o(1),
||1_(A_U)*1_(A_V)||_2
 <<D^(5/4)*(U*V)^(5/8)*q^o(1).                      (2.2)
```

The normalized height-one Fejer majorant has the cumulative dyadic form

```text
P(C/a)<<sum_(U dyadic) U^(-2)*1_(A_U)(a).            (2.3)
```

After the two Fejer weights, the `(U,V)` contribution to the convolution
norm is therefore

```text
D^(5/4)*U^(-11/8)*V^(-11/8)*q^o(1).                 (2.4)
```

Both geometric sums converge:

```text
sum_(U dyadic) U^(-11/8)
 <=1/(1-2^(-11/8))<2.                               (2.5)
```

Minkowski in the convolution norm now gives

```text
||p*p||_2<<D^(5/4)*q^o(1),
sum_S |(p*p)(S)|^2<<D^(5/2)*q^o(1).                 (2.6)
```

This closes every dyadic mask at once; the Young tail split
`m^2 M^3>=sqrt(D)` and its residual core are no longer needed once (1.1) is
available.

For comparison, if `m=min(U,V)` and `M=max(U,V)`, sharp mixed RSR gave the
weighted norm term

```text
D^(5/4)*m^(-5/4)*M^(-3/2).                          (2.7)
```

The diagonal-to-mixed route gives

```text
D^(5/4)*m^(-11/8)*M^(-11/8),                        (2.8)
```

which is larger than (2.7) by `(M/m)^(1/8)` in norm.  The remaining powers
`m^(-11/8)M^(-11/8)` still sum absolutely, so there is no global loss.

The weighted-coefficient version is equally direct.  If the physical point
sequence is `x`, decompose the Fejer-multiplied sequence into
`x_U=U^(-2)x 1_(A_U)`.  Equation (1.2) and Minkowski give

```text
||sum_(U,V) x_U*x_V||_2
 <=D^(1/4)[sum_U U^(-15/8)||x 1_(A_U)||_2]^2 q^o(1)
 <<D^(1/4)||x||_2^2 q^o(1).                         (2.9)
```

Thus its squared energy is `<<sqrt(D)||x||_2^4 q^o(1)`, the normalized
weighted target behind (2.6).

## 3. Factorable post-peeling masks

Let pair weights factor as `w_(i,j)=z_i y_j`, and let a selected pair mask
satisfy

```text
|M_(ij,kell)|<=1,
M_(ij,kell)!=0 => a_i+b_j=a_k+b_ell.                (3.1)
```

Entrywise absolute values give

```text
|sum conjugate(w_ij) M_(ij,kell) w_(kell)|
 <=|| |z|*|y| ||_2^2.                               (3.2)
```

Applying (1.2) to `|z|,|y|` proves the local bound

```text
<<(sqrt(D)*(U*V)^(1/4))*||z||_2^2||y||_2^2.         (3.3)
```

For the literal local broad kernel recorded in the existing bridge, one
takes `z=y`; then (1.1) itself gives the old sharp diagonal constant
`sqrt(D*U)`.  For genuinely mixed widths, (3.3) misses the scale-sharp
`sqrt(D*min(U,V))` bound, but after the physical Fejer weights its dyadic sum
is exactly (2.4)--(2.6).  Hence `min(U,V)` is essential only if one insists
on a sharp **unweighted per-mask** theorem, not for the assembled factorable
Fejer form.

The same argument survives arbitrary pair-of-pair deletions and cross-bin
coherence whenever the full point-pair coefficient remains globally
factorable.  No packet-pair orthogonality is required for that scalar form.

## 4. What this does not close

Scalar self restriction controls rank-one pair weights.  It does not control
a general pair-space coefficient `w_(i,j)`.  A finite abstract witness is

```text
A={1,2,4,...,2^(L-1)},       B=-A.
```

The normalized scalar self energy of `A` is

```text
E^+(A)/|A|^2=2-1/L<2,                              (4.1)
```

but the completion-zero pair fiber `{(a,-a):a in A}` has `L` coordinates.
The all-ones mask on that fiber has pair-space operator norm `L`.  Thus no
dimension-free implication from scalar self restriction to an arbitrary
nonfactorable tensor is possible.  A bounded Schmidt-rank/nuclear
factorization or a genuinely vector-valued self-restriction theorem is still
needed if the second physical tensor does not factor.

The exact remaining assembly gaps are therefore:

1. prove the hereditary self theorem (1.1), uniformly in every physical
   shell, centre, and dyadic width (or only in the Young-unresolved masks);
2. transfer the original carrier/colour coefficients to scalar point weights
   with lossless `l2` normalization;
3. prove that the second physical tensor is factorable, has only `q^o(1)`
   factorization cost, or establish a vector-valued analogue of (1.1);
4. assemble centres/endpoints without polynomial participation or
   cross-centre coherence loss;
5. retain the completion-sum Fourier variable through stationary and Airy
   layers, including the still-open physical harmonic/Bessel intertwining.

Accordingly, this is a strict simplification of the conjectural arithmetic
input, not a proof of the sharp four-cycle bound.

## 5. Binary status

```text
self restriction => symmetric mixed restriction:       PROVED;
symmetric mixed restriction => Fejer energy D^(5/2):   PROVED;
sharp min(U,V) dependence needed for Fejer sum:         NO;
literal diagonal factorable post-peeling mask:          CONTROLLED BY SELF;
mixed factorable masks after Fejer summation:            CONTROLLED;
sharp unweighted mixed per-mask constant:                NOT RECOVERED;
general nonfactorable pair tensor from scalar self:      FALSE;
hereditary reciprocal-strip self restriction:            OPEN;
sharp four-cycle bound:                                  NOT PROVED.
```

The exact exponent identities, finite Fourier-Cauchy checks, dyadic geometric
sum, and nonfactorable Sidon witness are replayed in

```text
src/qp_self_restriction_assembly.py
src/test_qp_self_restriction_assembly.py
```
