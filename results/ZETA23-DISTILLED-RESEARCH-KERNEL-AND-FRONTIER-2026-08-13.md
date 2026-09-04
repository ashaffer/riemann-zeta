# Distilled research kernel and live frontier

**Date:** 2026-08-13

**Truth boundary:** no uniform zero-free strip and no improved zero bound has
been proved.  This note compresses the project into the smallest collection
of invariants, exact gates, and fail-fast tests needed for another attack.

## 1. The canonical problem

Every route studied so far can be put in the same form.  There is

```text
a carrier functional       c(x),
a family of local rows      A x,
a completed arithmetic form Q(x),
and a nonlocal remainder    R(x).                           (1.1)
```

The geometry can usually produce a state with large `c(x)` while nulling or
signing selected rows.  A strip follows only if the **same state** satisfies
a relative completed inequality of the form

```text
uncontrolled completed debt <= (1-epsilon)*target carrier. (1.2)
```

Separate norm bounds, separate states, or an estimate after deleting the
principal mode do not address (1.2).

The invariant quantity is therefore not an absolute matrix norm.  It is a
normalized defect,

```text
mathfrak D(x)=completed adverse remainder / retained carrier. (1.3)
```

The goal is `mathfrak D<1` uniformly for a candidate-adapted state.  Nearly
all unsuccessful imports changed the numerator's representation without
changing this quotient.

## 2. Logical distance: four levels of statement

Statements should be ranked before effort is spent on them.

1. **Finite arithmetic statements with no zero in the hypothesis.**  These
   have the greatest logical distance from the desired theorem.  The prime-log
   atomic cancellation/Schur problem is the main surviving example.
2. **Candidate-conditioned coefficient statements.**  These may close a
   contradiction, but they must retain the exact nonlocal completion which
   detects the candidate.
3. **Coefficient-specific analytic positivity statements.**  The full-theta
   `B_P` and Husimi reverse-localization gates lie here.  They are clean, but
   can already contain an RH-strength endpoint.
4. **Equivalent criteria.**  Mertens power savings, Nyman collar rates,
   all-degree tau-Li positivity, shifted Hermite--Biehler, and the first
   Laguerre inequality are valuable diagnostics.  Rewriting them is not a
   proof strategy unless a genuinely weaker intermediate estimate appears.

Zero density, almost-all estimates, and positive-density recurrence belong
outside this hierarchy: they tolerate the single offending zero that a
uniform strip must exclude.

## 3. Conservation laws

### 3.1 Scalarization

Matrix, quantum, character, free-probability, and auxiliary-channel lifts
descend through the final scalar readout to the same projective/Wiener cost.
For a linear two-leg state, GNS Cauchy--Schwarz is sharp.  A lift is useful
only if the final theorem is genuinely all-channel coercive or nonlinear
while retaining the required sign.

### 3.2 Conductor

A degree-`k` moment or tensor introduces products of arithmetic length
`Y^k`.  The available frequency aperture is `Y^(50/33+o(1))`, below `Y^2`.
The first new tensor layer is therefore already outside the audited
conductor.  Formal exterior powers are legal as proof language only when
their samples remain separate; combining them physically restores this bill.

### 3.3 Principal mode

Centering, differentiation, variance decomposition, complementary lossless
channels, and high-pass filters move the scalar Mertens/carrier mode but do
not remove it.  Stable forward inversion reconstructs it.  An estimate which
controls only the transverse variance is not a strip estimate.

### 3.4 Positive smoothing

Replacing the signed theta Wigner slice by a positive Husimi spectrogram
smooths conjugate variables.  In `(p,T)` coordinates the optimal Gaussian
has `sigma_p*sigma_T=1`.  Height localization necessarily adds an
unpolarized carrier; exact recovery is signed backward heat.

### 3.5 Partition versus curvature

Linearizing the warped lattice `u=log(n/Y)` on shorter integer blocks reduces
curvature but increases the number of blocks.  The separated FFT/wavelet
ledger charges `sum_j sqrt(M_j)>=sqrt(M)`.  This is a no-go for that charged
proof class, not a lower bound for globally coherent cancellation.

### 3.6 Relative determinant

The DPP/fermionic volume common to numerator and denominator cancels.  What
remains is the directional Christoffel leverage `q^*G^(-1)q`.  Estimating
`det G`, a common partition function, or singular values separately cannot
improve the carrier ratio.

### 3.7 Finite-head nonidentifiability

For every finite von Mangoldt head `n<=X`, candidate `rho`, and prime `q>X`,

```text
F(s)=(1-q^(rho-s))(1-q^(conj(rho)-s))                    (3.1)
```

has nonconstant logarithmic-derivative support only at `q^k`.  The symmetric
completion `F(s)F(1-s)` inserts the candidate quartet while preserving the
finite head, apart from an explicit constant completion term.  Thus a finite
PSD scan plus a zero label cannot identify a candidate-conditioned theorem.
The missing variable is necessarily a nonlocal Euler/functional-equation or
approximate-functional-equation remainder.

### 3.8 Relative-object principle

The surviving quantities are all relative:

```text
Schur complement       rather than two determinants,
Turan difference       rather than two modulus estimates,
outer/inner line ratio rather than separate growth bounds,
signed full remainder rather than componentwise prime bounds. (3.2)
```

Estimating the two large pieces separately normally loses exactly the power
needed for a fixed strip.

## 4. Exact live frontiers

### 4.1 Prime-log atomic cancellation: kill or promote

For the actual prime-log evaluation matrix `A` and carrier row `b`,

```text
E(A,b)=sup{|<b,h>|:Ah=0, ||h||_1<=1}
      =inf_lambda ||b-A^*lambda||_infinity,
E(A,b)^2=max_w Delta(w).                                  (4.1)
```

Split the frequency band into low carrier and high cancellation regions.
If `C_(T,B)` is the least total variation of a nulling measure with low
carrier one and `epsilon_T=sup_H|b|`, then

```text
1/C_(T,B)-epsilon_T <= E_B <= 1/C_(T,B)+epsilon_T.         (4.2)
```

At the first strip target the required theorem is

```text
E_Y>=Y^(-kappa+o(1)),       kappa<0.0180303234.            (4.3)
```

Equivalently, after a negligible target tail, success requires
`C_(T,B)=Y^(o(1))`.  A theorem `C_(T,B)>=Y^delta` with
`delta>.0180303234` kills this route.

Current evidence: one low atom supplies essentially all carrier and `M` high
atoms cancel its phase vector.  The cost tracks the random-polytope law
`sqrt(M/log B)`, giving a square-root rather than subpower prior.  This is not
an actual-prime upper theorem.

There is now a theorem-grade partial dual.  Baker--Harman--Pintz prime gaps
give actual log-node mesh `h_Y<<Y^(-19/40+o(1))`; piecewise-linear hat
quadrature gives

```text
|P_Y(t)-b(t)| << (1+t^2)Y^(-19/20).                    (4.3a)
```

With low band `t<=Y^.01`, this supplies exponent `.019>.0180303234`
uniformly through `t=Y^.4655`, even for arbitrary signed low measures.  The
entire unresolved content of the full-aperture kill theorem is now the high
tail

```text
Y^(19/40-o(1)) <= |t| <= Y^(50/33).                     (4.3b)
```

The all-integer second-derivative heuristic does not transfer to prime/gap
weights; the audited pointwise actual-prime theorem remains logarithmic there.

### 4.2 Full-theta third tail

Define

```text
B_P(w)=1/4 integral_R (|d|-P)_+^2
       Phi((w+d)/2)Phi((w-d)/2) dd.                       (4.4)
```

Then

```text
S_3(P,T)=Fourier_w[B_P](T).                               (4.5)
```

The surviving theta statement is: **every `B_P` is positive definite**.
At `P=0` this is the first Laguerre inequality
`Z'(T)^2-Z(T)Z''(T)>=0`.  For `P>0` it is strictly stronger than generic
Laguerre--Polya/Hermite--Biehler structure: an exact positive-definite LP
atomic model has `S_3(7,pi/2)=-1/16`.

The actual theta kernel numerically survives through `T=1000` over the full
tested transition region.  This is not an interval theorem.  The admissible
next moves are a complete two-dimensional Poisson factorization of `B_P`, or
a targeted Arb negative certificate.

The two-dimensional Poisson calculation is now complete and narrows that
instruction.  For

```text
R(u)=e^u theta(e^(4u))-2cosh(u),
```

one has the exact new sign/convolution lemma

```text
R<0,       r=-R=8 e^(-|.|)*Phi.                         (4.5a)
```

The modular product is nevertheless an inclusion--exclusion orbit
`+bulk-axis-axis+corner`; every finite, axiswise, and even complete
primal/dual orbit Gram proposal has a sign-changing Fourier transform.  Only
infinite global orbit mixing remains.  A separate Arb certificate at
`T=152.7` shows `S_2(P,T)` has ordered signs `+,-,+`, so the proposed
one-crossing reduction is false.  Neither result falsifies `S_3` or positive
definiteness of the complete actual `B_P`.

### 4.3 Husimi reverse localization

With `U_x(T)=|F(x-iT)|^2`, `A=alpha+eta`, `B=alpha-eta`, and normalized
Gaussian convolution `G_s`, phase-space positivity proves unconditionally

```text
e^(s^2*A^2)(G_s*U_A)(T)
 >=e^(s^2*B^2)(G_s*U_B)(T).                            (4.6)
```

Equivalently,

```text
G_s*(U_A-U_B)
 >=-tanh(2*s^2*alpha*eta) G_s*(U_A+U_B).                 (4.7)
```

A candidate outer-line zero would be excluded if its coefficient-specific
local behavior forced the strict reverse inequality

```text
(G_s*U_A)(T_0)
 <e^(-4*s^2*alpha*eta)(G_s*U_B)(T_0)                    (4.8)
```

for some admissible `s`.  Generic analyticity, Wigner positivity, and zero
density do not imply (4.8).  The missing theorem is a zeta/theta-specific
reverse-localization estimate.

The local zero jet has now been eliminated as its source.  For
`F(z)=C(z-z_0)^m`, exact Gaussian moments give

```text
M_s(A,T_0)/M_s(B,T_0)>=exp(-8*m*eta^2*s^2),             (4.8a)
```

so (4.8) is impossible whenever `2*m*eta<=alpha`.  A bounded nonzero
cofactor of variation ratio `K` can escape only if

```text
log K>2*eta*(alpha-2*m*eta)*s^2.                        (4.8b)
```

Thus the strict survivor is a global coefficient/divisor estimate for the
nonzero cofactor, not a consequence of the candidate zero or multiplicity.

### 4.4 Nonlocal candidate-conditioned arithmetic

The centered matrix has the exact signless structure

```text
H_E=2*L_A-2*(log X)*diag(Re E_X),
rank([diag(tau),H_E])<=2.                                 (4.9)
```

Prime-separable Fejer/SOS lower bounds are negative on positive scan cases;
the sign uses common-height cross-prime coherence.  Any machine-discovered
certificate must therefore include an exact nonlocal completion/AFE
remainder.  A larger finite PSD regression cannot learn the conditional
implication.

The most local Lee--Yang completion is now closed as well.  On the exact
two-prime AFE cylinder

```text
F=(1+x_2)(1+x_3)+g(1+y_2)(1+y_3)+r,
```

the Rayleigh minor is

```text
Delta_(x_2,x_3)=-g(1+y_2)(1+y_3)-r,                   (4.10)
```

and takes both signs.  The weighted version remains affine with nonzero
slope in every retained additive dual or tail variable.  Consequently no
coordinatewise invertible real `GL(2)` holographic change can make the
additive primal--dual AFE lift stable on a product of half-planes.  Only a
genuinely cross-channel transform, mixed primal--dual polynomial, or
separately justified non-product complex cone remains open.

## 5. Admission test for every new idea

Before developing a route, answer all of the following.

1. **Exact object:** What is the precise scalar inequality that implies the
   strip?
2. **Same state:** Are carrier, constraints, and arithmetic sign evaluated on
   the same state?
3. **Normalization:** What norm is used before and after scalar descent?
4. **Principal mode:** Where did the rank-one/Mertens mode go?
5. **Conductor:** What arithmetic length appears after products, moments, or
   tensors?
6. **Completion:** Can a remote symmetric factor change the conclusion while
   preserving all data used by the argument?
7. **Singleton:** Does the estimate exclude one adversarial zero, or only a
   positive density of them?
8. **Relative cancellation:** Was the common main term canceled before
   applying absolute values?
9. **Generic falsifier:** Does an FE-symmetric, LP, positive-definite, or
   structural countermodel already defeat the claimed implication?
10. **Uniformity:** Are height, aperture, degree, and boundary limits uniform
    in the order actually required?

A route failing any one item is diagnostic only.

## 6. Ranked program

1. **Prime high-tail antenna.**  The low/mid fixed-power certificate is now
   proved.  Prove or refute its extension over (4.3b); do not collect more
   unstructured Remez points.
2. **Infinite-orbit `B_P` theorem or falsifier.**  Finite Poisson/Gram and
   one-crossing shortcuts are closed.  The complete actual cone remains open;
   kill immediately on a certified negative.
3. **Husimi reverse localization with exact theta coefficients.**  This is
   now criterion-strength: the local zero jet is closed, so continue only if
   a global cofactor estimate independently beats (4.8b).
4. **Proof-carrying symbolic search with an AFE remainder.**  Reject every
   learned SOS which uses only a finite von Mangoldt head, and reject every
   coordinatewise product-half-plane holographic transform by (4.10).
5. **Mertens/Nyman/Li/HB criteria as diagnostics.**  Use them to test whether a
   proposed input is already strip-equivalent, not as nominally new routes.

## 7. Compact context block

```text
GOAL:
  prove some fixed delta>0 with zeta(s)!=0 for Re(s)>1-delta.

STATUS:
  no strip; no improved zero region.

CORE_INVARIANT:
  normalized completed debt / retained carrier on the same state.

PROVED:
  E^2=max Schur complement;
  low/high cancellation comparison (4.2);
  actual-prime exponent .019 through t=Y^.4655;
  DPP/SUSY collapse to directional leverage;
  Wigner identity and Husimi inequality (4.6);
  R<0 and exact full-theta Poisson inclusion-exclusion;
  S2, fractional theta cones, and S2 one-crossing false;
  finite-head candidate nonidentifiability;
  local product-domain AFE Lee--Yang stability false;
  local warped-FFT and linear ancilla no-gos.

LIVE:
  B_P positive definite for every P via infinite global orbit mixing;
  full-aperture prime high tail above Y^(19/40-o(1));
  coefficient-specific reverse localization (4.8);
  nonlocal AFE-coupled arithmetic SOS or cross-channel cone stability.

DO_NOT_REPEAT:
  separate KMT bounds;
  density/average arguments tolerating one zero;
  finite-head PSD regression;
  generic LP/HB/Wigner positivity;
  local FFT partitions;
  determinant estimates before taking the relative ratio;
  tensor moments beyond the aperture;
  more unstructured floating scaling points.

SUCCESS_THRESHOLD:
  prime atomic route needs kappa<0.0180303234 at d=.66, alpha=.49.
```
