# QP pre-stationary operator: exact Fejer Stinespring lift, the fixed-`S` no-go, and the Airy assembly gate

**Date:** 2026-08-25  
**Scope:** the literal hard-window operator and its physical completion
variable  
**Verdict:** the original scalar coefficient norm transfers to supported
Fejer harmonics with no power loss.  The transfer is an exact Stinespring
factorization, and completion Fourier is an exact unitary change of
coordinates.  Composing this factorization with the localized
fixed-normal-lattice Airy `l2` theorem introduces no further normalization
loss.

This does **not** prove the four-cycle estimate.  Completion Fourier gives a
Kronecker delta in the physical sum `S`; on the surviving fixed-`S` fiber it
is identically one.  The remaining norm is exactly the coefficient-uniform
assembly over physical completions, tangent charts, and the post-peeling
pair mask.  The later Kraus-channel audit identifies the faithful global
target as a row-pair-preserving `S_1 -> S_2` channel bound, not the stronger
center-convolution/CCSR relaxation.  The proposed split

```text
eta_h=D^(-1/12),       eta_S=D^(-1/16),
eta_h*eta_S=D^(-7/48)                                  (0.1)
```

is a correct exponent ledger but is not an automatic product theorem.
Exact affine aliases have no `S` cancellation, and an unsplit Airy profile
does not have bounded Abel variation.  Both have to be treated by the
physical chart/cluster assembly.

No global Kraus/Airy Bessel theorem or sharp four-cycle theorem is claimed
below.

## 1. The literal pre-stationary operator

The operator before stationary phase is

```text
A_z(a,b)=sum_(c in S_q) z_c*kappa(a,b,c),
kappa(a,b,c)=1_(|8*a*b*c-q^3|<=q*D).                 (1.1)
```

Put

```text
C_c=q^3/(8c),
theta_(a,b,c)=C_c/a-b.                               (1.2)
```

Since `b` is integral, `e(h theta)=e(h C_c/a)`.  On the support of
`kappa`,

```text
|theta_(a,b,c)|
 =|q^3-8abc|/(8ac)
 <<D/q=1/H,                  H=q/D.                  (1.3)
```

Choose an integer `L=gamma H` with a sufficiently small fixed `gamma>0`
depending only on the fixed shell constants.  Let

```text
P_L(theta)=sum_(|h|<L) gamma_h*e(h theta),
gamma_h=(L-|h|)/L^2.                                 (1.4)
```

Then

```text
gamma_h>=0,       sum_h gamma_h=1,
P_L(theta)=|L^(-1)sum_(0<=r<L)e(r theta)|^2.         (1.5)
```

Taking `gamma` so that `L|theta|<=1/4` on (1.3), the elementary sine
bounds give

```text
P_L(theta)>=4/pi^2                                  (1.6)
```

there.  In particular

```text
r_(a,b,c)=kappa(a,b,c)/P_L(theta_(a,b,c))            (1.7)
```

is well-defined, supported on the original physical edge set, and bounded
by an absolute constant.  Equations (1.4)--(1.7) give the exact hard-window
identity

```text
kappa(a,b,c)
 =sum_(|h|<L) gamma_h*r_(a,b,c)*e(h theta_(a,b,c)).  (1.8)
```

Thus no smooth majorant and no sign assumption on `z` is needed for the
algebraic lift.  The price of retaining the hard window is only the bounded
amplitude `r`; this is a constant, not a power of `D`.

## 2. Exact Stinespring factorization

Define the vector-row operator

```text
V_z((a,h),b)
 =sqrt(gamma_h)*sum_c z_c*r_(a,b,c)*e(h theta_(a,b,c)), (2.1)
```

and the fixed harmonic contraction

```text
(R F)(a,b)=sum_h sqrt(gamma_h)*F((a,h),b).           (2.2)
```

Because `sum_h gamma_h=1`,

```text
||R||_(2->2)=1.                                      (2.3)
```

The identity (1.8) is precisely

```text
A_z=R V_z.                                           (2.4)
```

Consequently every Schatten ideal gives, in particular,

```text
||A_z||_(S_4)<=||V_z||_(S_4).                        (2.5)
```

There is also an explicit input isometry

```text
(Jz)_(c,h)=sqrt(gamma_h)*z_c,
||Jz||_2^2=sum_(c,h)gamma_h|z_c|^2=||z||_2^2.       (2.6)
```

The important point is not merely that the support has `O(H)` harmonics.
The square roots in (2.1), (2.2), and (2.6) specify exactly where their
normalization lives.  There is no `sqrt(H)` replication of the scalar
coefficient vector.

Expanding `V_z^*V_z` pairs equal output harmonics and produces the weights

```text
gamma_h*gamma_k                                     (2.7)
```

in the fourth power.  The color-pair coefficient is

```text
w_(c,c')=conj(z_c)*z_(c'),
sum_(c,c')|w_(c,c')|^2=||z||_2^4.                   (2.8)
```

Thus both the original color norm and the two Fejer weights entering the
normal-lattice calculation are fixed exactly by the physical operator.
No arbitrary harmonic signature has been inserted.

## 3. Exact pair bundle and completion Fourier

The endpoint reciprocal form makes the same identity especially
transparent.  Put

```text
v(theta)=(sqrt(gamma_h)e(h theta))_(|h|<L),
<v(theta),v(phi)>=P_L(theta-phi).                    (3.1)
```

For a physical pair `p=(a,b)`, define

```text
Phi_p=delta_(a+b) tensor v(C/a) tensor v(C/b).       (3.2)
```

Then `||Phi_p||=1`, and for arbitrary selected complex pair weights `w_p`,

```text
||sum_p w_p Phi_p||^2
 =sum_(a+b=c+d) w_(a,b)conj(w_(c,d))
    P_L(C/a-C/c) P_L(C/b-C/d).                       (3.3)
```

If `w_(a,b)=x_a y_b` on an arbitrary selected subset, then

```text
sum_(selected p)|w_p|^2<=||x||_2^2||y||_2^2.        (3.4)
```

So the pair lift is also coefficient-lossless.

Let `M` be larger than the range of completion sums.  Replacing the delta
in (3.2) by the normalized Fourier character

```text
M^(-1/2)(e_M(xi(a+b)))_(xi mod M)                    (3.5)
```

does not change (3.3).  Indeed

```text
M^(-1)sum_(xi mod M)e_M(xi[(a+b)-(c+d)])
 =1_(a+b=c+d).                                      (3.6)
```

Equations (3.3)--(3.6) are the exact supported-harmonic plus
completion-Fourier vectorization requested in the closeout audit.

They also give the decisive negative statement:

> **Fixed-`S` verdict.**  Once two pair states survive the physical
> completion constraint, their completion-Fourier inner product is exactly
> one.  It cannot supply an additional factor `D^(-1/16)`.

The Fourier variable dual to `S` is a bookkeeping isometry.  Cancellation
across a block of different integer completions must come from the
nonlinear stationary action or from a genuine outer Bessel theorem; it is
not furnished by (3.6).

## 4. Audit of the proposed `eta_h eta_S` split

The exponent arithmetic is exact.  Two comparable triangular Fejer
responses satisfy

```text
P_L(delta_1)P_L(delta_2)>eta_h
 => |delta|<<1/(H*eta_h^(1/4))                       (4.1)
```

when the two reciprocal gaps are comparable on a fixed wrap branch.  With

```text
Q=D^(33/16), H=D^(17/16), eta_h=D^(-1/12),          (4.2)
```

the corresponding physical cell is exactly

```text
Q/(H*eta_h^(1/4))=D^(49/48).                        (4.3)
```

Also

```text
eta_h*eta_S=D^(-1/12-1/16)=D^(-7/48),               (4.4)
```

and for a completion block

```text
N=q^(1/3)=D^(11/16),
H*N/q=N/D=D^(-5/16)<<eta_h.                         (4.5)
```

Thus, on a regular wrap chart on which the two Fejer-height paths have
`O(1)` monotonicity pieces, their total scaled excursion is less than one
Fejer lobe.  The elementary bounded-variation estimate on each piece is

```text
Var_S[P_L(delta_1(S))P_L(delta_2(S))]
 <<sup_S |P_L(delta_1(S))P_L(delta_2(S))|.           (4.6)
```

For a regular interior saddle of

```text
F(a,S)=-m*a+C*h/a+C*k/(S-a),                        (4.7)
```

put `b=S-a` and

```text
u=C*h/a^2, v=C*k/b^2, w=u*b+v*a.
```

Then

```text
F_aa=2w/(ab),             da/dS=v*a/w.              (4.8)
```

On a compact regular chart with `w` bounded away from zero in normalized
coordinates, (4.8) gives

```text
d/dS log|F_aa|=O(1/q).                               (4.9)
```

Hence the normalized quadratic stationary amplitude and its cross-products
have Abel variation `O(1/N)` on an `N`-block.  In this regular, nonalias
sector, if a separate phase theorem proves normalized stationary-action
partial sums `O(eta_S)`, then (4.6), (4.9), and finite Abel summation really
do multiply the two gains.

There are two exact reasons this is not yet a global theorem.

### 4.1 Exact completion-action aliases

The physical reflection

```text
(a,h,k,m)->(S-a,k,h,-m)                             (4.10)
```

changes the stationary action by `mS`.  This is integral on the sampled
completion lattice and hence gives no `S` cancellation.  On the zero-dual
locus, take

```text
m=0,       h=r^2,       k=s^2.                      (4.11)
```

The stationary point and action are exactly

```text
a=S*r/(r+s),
J_(r,s)(S)=C*(r+s)^2/S.                              (4.12)
```

Every two pairs `(r,s)` with the same sum have identical completion action
for every real `S`, while their oriented two-inverse signatures can be
different.  Thus no universal estimate can replace a harmonic factor
`eta_h` by `eta_h eta_S`.  Reflection and zero-dual families must first be
placed in the arithmetic near graph or controlled by the existing
nonuniform row-sum estimates.

### 4.2 The unsplit Airy interpolation is not a bounded-variation amplitude

At the fold,

```text
F_aaa asy H/q^2,          partial_S F_a asy H/q.    (4.13)
```

The Airy coordinate therefore changes per physical completion by

```text
|Delta X| asy (H/q)/(H/q^2)^(1/3)
 =H^(2/3)q^(-1/3)=D^(1/48),                         (4.14)
```

and traverses

```text
N*|Delta X|=D^(17/24)                               (4.15)
```

on a full block.  The unsplit profile `Ai(-X)` has

```text
Ai(-X)=pi^(-1/2)X^(-1/4)
 sin(2X^(3/2)/3+pi/4)+O(X^(-7/4)),                  (4.16)
```

so its continuous variation through `[1,X_0]` is of order `X_0^(5/4)`,
not `O(sup |Ai|)`.  Consequently ordinary derivative-to-Abel transfer does
not justify using the unsplit uniform Airy interpolation as the amplitude.
This is a rigorous obstruction to that proposed proof step; it is not a
lower bound for every specially sampled Airy sequence, whose discrete
variation could in principle have additional aliases.

The standard repair is to split (4.16) into its two saddle phases outside
`|X|=O(1)` and keep only their monotone envelopes as amplitudes.  The
central transition occupies `O(1)` scaled Airy length.  Carrying this split
uniformly through all physical charts and all four saddle pairings is part
of the remaining assembly theorem, not a consequence of (4.9).

## 5. Composition with the fixed-normal-lattice Airy theorem

The localized Airy theorem uses exactly the weights produced by (2.7).
For the triangular coefficients,

```text
sum_h gamma_h^2=(2L^2+1)/(3L^3)<=1/L.              (5.1)
```

Thus the two-frequency field has

```text
||(gamma_h gamma_k)_(h,k)||_2
 =sum_h gamma_h^2<=1/L.                             (5.2)
```

On a primitive-normal curvature layer of width `d`, the physical support
has `O(dH)` sites and the stationary amplitude is `O(sqrt(q/d))`.  Vector
Plancherel gives

```text
sqrt(q/d)*sqrt(dH)/H=sqrt(q/H)=sqrt(D).              (5.3)
```

At the Airy width `d=J=D^(1/48)`, this is the exact cancellation

```text
D^(49/48)*D^(-25/48)=D^(1/2).                       (5.4)
```

There is no hidden loss when (5.3) is composed with the Stinespring lift:

```text
original color-pair norm:             ||z||_2^4;     EXACT;
harmonic contraction R:               norm 1;        EXACT;
hard-window inverse r:                O(1);          CONSTANT;
Fejer two-frequency l2 mass:          <=1/H;         GAIN;
localized Airy layer:                 sqrt(D);       TARGET;
dyadic layer/chart cutoffs:           q^o(1);        HARMLESS.
```

The Airy theorem permits arbitrary deletion and contractive internal
vectors **inside one fixed normal lattice**.  It does not control repeated
physical output rows or the common-center vector selector coupling them.

## 6. Corrected remaining operator theorem: Kraus/Airy Bessel

For `P_b[a,c]=kappa(a,b,c)`, define

```text
Phi(X)=sum_b P_b X P_b^*.                            (6.1)
```

The original fourth-trace target is exactly

```text
||Phi(z z^*)||_HS<=sqrt(D)q^o(1)||z||_2^2.          (6.2)
```

Kraus Gram Cauchy and singular-value decomposition show, with no constant
loss, that (6.2) is equivalent to

```text
||Phi||_(S1->S2)=||Phi^*||_(S2->Sinf)
 <<sqrt(D)q^o(1).                                   (6.3)
```

The Stinespring factorization in Section 2 is compatible with (6.3).  If
`P_b=R Q_b` and `Psi(X)=sum_b Q_b X Q_b^*`, then

```text
Phi^*(Y)=Psi^*(R^*Y R),
||R^*Y R||_HS=||Y||_HS.                             (6.4)
```

In the literal expansion of (6.4), the two lifted row factors turn
`R^*YR` into the exact weights `gamma_h gamma_k` required by the Airy
vector theorem.  Thus there is no hidden harmonic or Schatten loss.

Let `tau` now index the physical stationary normal lattice, curvature
layer, chart, and branch.  The fixed-lattice theorem controls one `tau`.
It does not prove the simultaneous synthesis estimate

```text
||sum_tau Phi_tau^*(Y)||_Sinf
 <<sqrt(D)q^o(1)||Y||_HS,                            (6.5)
```

because the same colour input can participate in many `tau`.  Indeed the
Fejer phase loses the integral carrier `b` modulo one; carrier multiplicity
remains in the hard support rather than becoming an orthogonal character.
A direct CP model `P_b=e_b:C->C^L` has every local channel norm equal to
one but global `S1->S2` and dual `S2->Sinf` norm `sqrt(L)`.  Hence (6.5)
cannot be inferred formally from the fixed-lattice theorem.

Vectorizing (6.1), the exact remaining physical statement is

```text
||H(conjugate(z) tensor z)||_2
 <<sqrt(D)q^o(1)||z||_2^2,                           (6.6)
```

with the ungrouped row-pair coordinate retained.  The multiplicative
tangent sector of (6.6) is now closed.  Its residual sector requires the
two-sided Kraus/chart Bessel theorem (6.5), or a sufficient arithmetic
degree-product theorem.  The global center-convolution/CCSR relaxation is
not used; it is stronger than the true row-pair norm and has separate
countermodels.

## 7. Binary status

```text
literal hard-window reciprocal phase:               RECONSTRUCTED;
supported Fejer representation of kappa:             EXACT;
scalar coefficient l2 lift:                          ISOMETRIC;
Schatten-4 Stinespring domination:                   EXACT;
pair coefficient norm ||z tensor zbar||_2:           EXACT;
completion Fourier realization:                      UNITARY;
completion Fourier decay inside fixed S:             FALSE (factor = 1);
eta_h=D^(-1/12) two-Fejer cell D^(49/48):             EXACT LEDGER;
eta_h*eta_S=D^(-7/48):                               EXACT LEDGER;
automatic multiplication by eta_S:                   FALSE;
regular-chart Abel compatibility:                    PROVED AT LEADING SYMBOL;
unsplit Airy BV from the standard interpolation:      FALSE;
fixed-normal-lattice Airy normalization loss:         NONE;
fixed-lattice Airy amplitude reduced to sqrt(D):      PROVED ELSEWHERE;
pure-state/S1->S2/S2->Sinf equivalence:               EXACT;
global Kraus/chart Bessel synthesis:                  OPEN;
center convolution / CCSR used in final target:       NO;
residual rank-one H / sharp four-cycle bound:          NOT PROVED.
```

The exact finite identities, hard-window replay, completion DFT, zero-dual
alias, mask obstruction, and exponent ledger are implemented in

```text
src/qp_pre_stationary_fejer_completion_bundle.py
src/test_qp_pre_stationary_fejer_completion_bundle.py
```
