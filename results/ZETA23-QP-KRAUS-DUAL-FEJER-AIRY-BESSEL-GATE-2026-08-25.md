# QP Kraus dual: exact Fejer compatibility and the remaining Airy--Bessel gate

**Date:** 2026-08-25
**Verdict:** the completely positive channel formulation is exact and
removes no information.  The pure-state fourth-trace estimate is, with the
same constant, the norm estimate

```text
Phi:S_1(colour)->S_2(row),
Phi^*:S_2(row)->S_infinity(colour).                  (0.1)
```

The lossless Fejer Stinespring lift is perfectly compatible with this
duality.  In the dual expansion it produces exactly the two weights
`gamma_h gamma_k` used by the fixed-normal-lattice Airy vector theorem, and
the Hilbert--Schmidt norm of the test matrix is unchanged.

This still does **not** prove (0.1).  The Airy theorem controls one retained
stationary normal lattice/curvature chart.  It gives no Bessel inequality
for summing the physical Kraus carriers and all normal lattices which reuse
the same colour input.  The Fejer phase contains no carrier character, so
that missing orthogonality is not hidden in the exact lift.  A direct
completely positive repetition example proves that uniformly bounded local
channel pieces can have a global `S_1 -> S_2` norm larger by the square root
of their multiplicity.

Thus the first remaining norm theorem is a row-pair-preserving, two-sided
Airy/Kraus Bessel inequality, equivalently the residual rank-one `H` bound
or the dual residual channel bound.  It is not the disproved center
convolution estimate.

## 1. Pure states, trace class, and the dual have the same norm

For the physical carry matrices

```text
P_b[a,c]=kappa(a,b,c),
Phi(X)=sum_b P_b X P_b^*.                            (1.1)
```

put `u_b=P_b x` and `v_b=P_b y`.  The Kraus Gram identity is

```text
||Phi(x y^*)||_HS^2
 =sum_(b,b') <u_b,u_b'> conjugate(<v_b,v_b'>).       (1.2)
```

The two Gram-matrix Hilbert--Schmidt norms are

```text
||( <u_b,u_b'> )||_HS=||Phi(x x^*)||_HS,
||( <v_b,v_b'> )||_HS=||Phi(y y^*)||_HS.            (1.3)
```

Consequently

```text
||Phi(x y^*)||_HS^2
 <=||Phi(x x^*)||_HS ||Phi(y y^*)||_HS.             (1.4)
```

If

```text
||Phi(z z^*)||_HS<=K||z||_2^2                       (1.5)
```

for every `z`, then (1.4) gives

```text
||Phi(x y^*)||_HS<=K||x||_2||y||_2.                 (1.6)
```

Apply (1.6) termwise to a singular-value decomposition
`X=sum_j s_j x_j y_j^*`.  Triangle inequality gives

```text
||Phi(X)||_HS<=K sum_j s_j=K||X||_S1.               (1.7)
```

Conversely, (1.7) applied to `X=zz^*` gives (1.5).  Hence, exactly,

```text
sup_(z!=0) ||Phi(zz^*)||_HS/||z||_2^2
 =||Phi||_(S1->S2)
 =||Phi^*||_(S2->Sinf).                             (1.8)
```

At the target scale, `K=sqrt(D)q^o(1)`.  This reformulation loses neither a
constant nor a power of `D`.

## 2. Exact Fejer Stinespring factorization of the channel

Let

```text
theta_(a,b,c)=q^3/(8ac)-b,
kappa(a,b,c)=sum_h gamma_h r_(a,b,c)e(h theta_(a,b,c)),
sum_h gamma_h=1,                                    (2.1)
```

be the supported hard-window identity from the pre-stationary audit.  On
lifted row space define

```text
Q_b[(a,h),c]
 =sqrt(gamma_h) r_(a,b,c)e(h theta_(a,b,c)),
(R F)(a)=sum_h sqrt(gamma_h)F(a,h).                 (2.2)
```

Then

```text
R R^*=I,          ||R||=1,          P_b=R Q_b.      (2.3)
```

For the lifted completely positive map

```text
Psi(X)=sum_b Q_b X Q_b^*,                            (2.4)
```

one has the exact identities

```text
Phi(X)=R Psi(X)R^*,
Phi^*(Y)=Psi^*(R^*Y R).                              (2.5)
```

Moreover

```text
(R^*Y R)[(a,h),(a',k)]
 =sqrt(gamma_h gamma_k)Y[a,a'],
||R^*Y R||_HS=||Y||_HS.                             (2.6)
```

Substitution of (2.2) and (2.6) into (2.5) gives the literal dual kernel

```text
[Phi^*(Y)]_(c,c')
 =sum_(a,a',b,h,k)
   gamma_h gamma_k conjugate(r_(a,b,c)) r_(a',b,c')
   e(-h theta_(a,b,c)+k theta_(a',b,c'))Y_(a,a').   (2.7)
```

Thus the two fourth-power Fejer weights do not rely on `Y` being rank one;
they are present for every Hilbert--Schmidt test matrix.  This exactly
matches the `c_h c_k` normalization in the Airy vector-Plancherel theorem.
There is no `sqrt(H)` replication.

There is also an exact warning in (2.7).  Since `b,h,k` are integers,

```text
e(-h theta_(a,b,c)+k theta_(a',b,c'))
 =e(-h q^3/(8ac)+k q^3/(8a'c')).                    (2.8)
```

The physical carrier `b` has disappeared from the phase.  It remains only
in the hard support and the bounded factors `r`.  Hence the Fejer lift
itself supplies no oscillation or orthogonality among Kraus carriers.

## 3. What fixed-lattice Airy Plancherel actually proves

For one fixed stationary normal lattice `tau` and one curvature layer of
width `d`, the existing theorem applies to a field of the form

```text
sum_((h,k) in E_(tau,d))
 A_(tau,d)(h,k) gamma_h gamma_k v_(tau,h,k),         (3.1)

#E_(tau,d)<<dH,
|A_(tau,d)(h,k)|<<sqrt(q/d),
||v_(tau,h,k)||<=1.                                 (3.2)
```

It proves, uniformly for Hilbert-valued `v`,

```text
||(3.1)||<<sqrt(q/H)=sqrt(D).                        (3.3)
```

Equations (2.6)--(2.7) show that an arbitrary `Y` is compatible with the
Hilbert-valued part of this theorem and that its Fejer normalization is
correct.  What has not been proved is the physical intertwining/Bessel
statement which simultaneously:

1. decomposes (2.7), with controlled stationary remainders, into the actual
   normal-lattice fields (3.1);
2. retains the ungrouped row-pair coordinate; and
3. square-sums all carrier, lattice, curvature, and chart labels without
   copying the same colour input polynomially many times.

The local estimate (3.3) bounds each chart after normalizing its internal
coefficient vector by the **full** input norm.  Applying it separately to
`L` charts permits a `sqrt(L)` loss in the global Hilbert norm.  Neither
(2.5) nor vector Plancherel contains a theorem which removes that loss.

## 4. Exact CP repetition obstruction to formal aggregation

This failure already occurs for the smallest completely positive channel.
Take one colour, `L` rows, `L` carriers, and

```text
P_b=e_b:C->C^L,             1<=b<=L.                (4.1)
```

Every one-carrier channel

```text
Phi_b(x)=x e_b e_b^*                                (4.2)
```

has `S_1 -> S_2` norm one.  The pieces even have orthogonal row support.
But their sum is

```text
Phi(x)=x I_L,
||Phi||_(S1->S2)=sqrt(L).                            (4.3)
```

The dual is

```text
Phi^*(Y)=tr(Y),
||Phi^*||_(S2->Sinf)=sqrt(L),                        (4.4)
```

with equality at `Y=I_L/sqrt(L)`.  Thus local CP bounds do not aggregate
with constant one, even when the outputs of the pieces are exactly
orthogonal and even after passing to the dual formulation.

This is a logical counterexample to an automatic local-to-global
implication, not a counterexample to the physical QP channel.  In the
physical problem the missing arithmetic theorem must bound precisely this
participation multiplicity and the additional cross-colour correlations.

## 5. Exact remaining theorem

Vectorizing (1.1) gives the original row-pair/color-pair incidence

```text
H_((a,a'),(c,c'))
 =sum_b kappa(a,b,c)kappa(a',b,c').                  (5.1)
```

The channel theorem is equivalently

```text
||H vec(X)||_2<=sqrt(D)q^o(1)||X||_S1,              (5.2)
```

or, on the pure sector,

```text
||H(conjugate(z) tensor z)||_2
 <=sqrt(D)q^o(1)||z||_2^2.                          (5.3)
```

The exact multiplicative-tangent part of (5.3) is already proved.  For the
nonzero-determinant residual, one sufficient concrete theorem is the
two-sided edge-degree product bound

```text
max_(p~gamma) deg_left(p)deg_right(gamma)
 <<Dq^o(1).                                         (5.4)
```

Alternatively one may prove directly the row-pair-preserving Airy/Kraus
Bessel estimate

```text
||Phi_res^*(Y)||_Sinf
 <=sqrt(D)q^o(1)||Y||_HS.                            (5.5)
```

The fixed-normal-lattice theorem proves the localized diagonal pieces
needed for (5.5); it does not prove their two-sided synthesis bound.  That
is the first exact remaining operator obstruction after the lossless Fejer
normalization.

```text
pure-state/channel norm equivalence:              EXACT;
dual S2->Sinf formulation:                         EXACT;
Fejer Stinespring factorization of Phi:            EXACT;
dual Fejer weights gamma_h gamma_k:                EXACT;
Hilbert--Schmidt norm through R^*Y R:              ISOMETRIC;
fixed-lattice Airy normalization:                  sqrt(D), PROVED;
automatic sum over physical lattices/carriers:     FALSE ABSTRACTLY;
physical Kraus/chart Bessel intertwining:          OPEN;
tangent channel sector:                            CLOSED;
residual channel / rank-one H sector:              OPEN;
sharp four-cycle bound:                            NOT PROVED.
```

## 6. Reproducibility

The channel/adjoint identities and Kraus Gram Cauchy inequality are replayed
in

```text
src/qp_pure_state_channel.py
src/test_qp_pure_state_channel.py
```

The exact hard-window Stinespring contraction, Fejer normalization, and
fixed-lattice vector Plancherel are replayed in

```text
src/qp_pre_stationary_fejer_completion_bundle.py
src/test_qp_pre_stationary_fejer_completion_bundle.py
src/qp_airy_shift_square_function.py
src/test_qp_airy_shift_square_function.py
```
