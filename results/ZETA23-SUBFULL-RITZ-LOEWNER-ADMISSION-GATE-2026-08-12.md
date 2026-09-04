# The sub-full carrier edge has an exact two-dimensional Ritz gate

Status: exact finite-dimensional theorem, completed-arithmetic reduction,
information-level counterexample, and floating actual-coefficient diagnostics,
2026-08-12.  No uniform arithmetic admission theorem, zero-free strip, or
improved bound for a zeta zero is proved.

## 1. Verdict

The smallest useful Ritz reduction of the direct carrier edge is exact and
strictly weaker than the full-carrier scalar.

Let

```text
N=kappa*a*a^*,       ||a||=1,
K=[[r,b^*],[b,D]] on C*a direct_sum a^perp.          (1.1)
```

For every fixed unit companion `w perpendicular a`, put

```text
d=<w,Dw>,             c=abs(<w,b>).                 (1.2)
```

The exact edge on `span{a,w}` at carrier fraction `theta` is

```text
Q_theta(a,w)=max_(theta<=x<=1)
 [x*r+(1-x)*d+2*c*sqrt(x*(1-x))].                  (1.3)
```

It has a closed `2 x 2` formula in Theorem 3.1 below.  In particular the
single boundary inequality

```text
theta*r+(1-theta)*d
 +2*sqrt(theta*(1-theta))*c >=-epsilon*kappa        (1.4)
```

is a rigorous sufficient condition for

```text
q_(theta*kappa)(K)>=-epsilon*kappa.                 (1.5)
```

This is genuinely weaker than estimating the full-carrier scalar `r`: a
large transverse completed correlation can compensate negative diagonal
values.  For example, at `theta=1/2`, the data `r=d=-M,c=M` give restricted
edge zero although the full-carrier scalar is `-M`.  It is also weaker than
positivity of the `2 x 2` compression.

There are two materially different ways to select `w`.

1. A geometry/background-defined `w` keeps `r,d,<w,b>` as three **linear**
   completed von Mangoldt--continuum--gamma scalars.  The exact target is a
   joint orientation inequality among those three scalars.
2. The first Lanczos direction

   ```text
   w_K=P_(a^perp)K*a/||P_(a^perp)K*a||              (1.6)
   ```

   maximizes `c`, but its `2 x 2` entries use `<a,K^2a>` and `<a,K^3a>`.
   It converts the linear prime problem into target-adaptive quadratic and
   cubic prime correlations.

The reduction therefore does **not** automatically improve the arithmetic
bound.  Applying the current KMT estimate separately to the three linear
entries still leaves

```text
O(sqrt(X)/L^(13/10))                                (1.7)
```

in normalized form, versus the fixed-depth carrier

```text
kappa asymp X^alpha/L.                              (1.8)
```

Their ratio is `X^(1/2-alpha)/L^(3/10)`, which diverges for every fixed
`alpha<1/2`.  Rank-two Loewner displacement does not force (1.4): even the
scalar matrix `-M*I` is a confluent Loewner matrix and defeats every
finite-dimensional carrier-rich Ritz space.

Thus the precise disposition is:

```text
exact low-dimensional constrained gate:                 PROVED;
strict weakening to one joint three-scalar inequality:   PROVED;
deduction from separate KMT magnitude estimates:         FAILS;
deduction from rank-two Loewner structure alone:         FAILS;
actual joint completed-prime orientation theorem:        OPEN.          (1.9)
```

## 2. The direct carrier edge

On the target-only quotient used by the high-height fixture, define

```text
q_(theta*kappa)(K)
 =max_(||z||=1, <z,Nz>>=theta*kappa) <z,Kz>,        (2.1)
```

where `0<=theta<=1`.  Since `N=kappa*a*a^*`, the constraint is simply

```text
abs(<a,z>)^2>=theta.                                (2.2)
```

Every unit vector in `span{a,w}` can, after a harmless global phase, be
written

```text
z=sqrt(x)*a+exp(i*phi)*sqrt(1-x)*w.                 (2.3)
```

Choosing `phi` to make the cross term positive gives (1.3), and immediately

```text
q_(theta*kappa)(K)>=Q_theta(a,w).                   (2.4)
```

The inequality is in the useful direction: a single explicit carrier-rich
state proves arithmetic admission.  It does not claim that the chosen plane
contains the optimizer of the full carrier slice.

## 3. Exact two-dimensional formula

### Theorem 3.1 (carrier-constrained `2 x 2` Ritz theorem)

With (1.1)--(1.3), set

```text
Delta=sqrt((r-d)^2+4*c^2),
lambda_+=(r+d+Delta)/2.                             (3.1)
```

If `Delta>0`, define the carrier mass of the unconstrained top Ritz vector
by

```text
p_+=(1+(r-d)/Delta)/2.                              (3.2)
```

Then

```text
Q_theta(a,w)=
  lambda_+,                                           if p_+>=theta,
  theta*r+(1-theta)*d
   +2*c*sqrt(theta*(1-theta)),                        if p_+<theta.       (3.3)
```

When `Delta=0`, the compression is scalar and `Q_theta=r=d`.

#### Proof

The function in (1.3) is the larger phase-optimized Rayleigh quotient of
the Hermitian block

```text
[[r,c],[c,d]].                                      (3.4)
```

Its unconstrained maximum is `lambda_+`, and a normalized top eigenvector
has first-coordinate mass (3.2).  The function of `x` in (1.3) is concave.
If its unconstrained maximizer lies in `[theta,1]`, the first line of (3.3)
applies.  Otherwise it is decreasing on that interval and its maximum is
the left endpoint `x=theta`.  QED

### Corollary 3.2 (shifted determinant and boundary alternatives)

To prove `Q_theta>=-epsilon*kappa`, shift both diagonals by
`epsilon*kappa`:

```text
R=r+epsilon*kappa,       E=d+epsilon*kappa.         (3.5)
```

The carrier mass `p_+` is unchanged.  If `p_+>=theta`, admission is
equivalent to the shifted top eigenvalue being nonnegative.  When `R<0` and
`E<0`, this is the determinant inequality

```text
c^2>=R*E.                                          (3.6)
```

If `p_+<theta`, the determinant can be misleading because its nonnegative
eigenvector has too little carrier.  The exact criterion is instead

```text
theta*R+(1-theta)*E
 +2*c*sqrt(theta*(1-theta))>=0.                     (3.7)
```

Condition (3.7) is always sufficient, without first checking `p_+`.

A convenient, slightly stronger orientation card is

```text
2*sqrt(theta*(1-theta))*c
 >=theta*(-r)_+ +(1-theta)*(-d)_+ -epsilon*kappa.   (3.8)
```

It displays the only possible low-dimensional gain: the transverse
correlation must pay the weighted negative diagonal deficit.  Separate
absolute-value estimates deliberately discard this gain.

## 4. The one-step Lanczos plane

Let

```text
m_j=<a,K^j a>,             j=1,2,3,
sigma^2=m_2-m_1^2.                                  (4.1)
```

If `sigma>0`, the companion (1.6) gives exactly

```text
r=m_1,
c=sigma,
d=(m_3-2*m_1*m_2+m_1^3)/sigma^2.                  (4.2)
```

Indeed `P_(a^perp)Ka=Ka-m_1a`, so its squared norm is `sigma^2`; expanding
`<Ka-m_1a,K(Ka-m_1a)>` proves the last identity.

This direction is extremal only for the coupling:

```text
abs(<w,b>)<=||b||=sigma                              (4.3)
```

for every unit `w perpendicular a`.  It need not maximize (1.3), because
the complement diagonal `d` also varies with `w`.

The arithmetic cost is important.  The completed matrix `K` is linear in
the actual prime powers, but `m_2` and `m_3` contain degree-two and
degree-three correlations of those prime sums.  The evaluated global
moments in the repository do not control these target-adaptive Krylov
moments.  Thus (4.2) is an excellent finite diagnostic and a possible new
correlation target, but it is not a free scalarization of the known linear
prime estimate.

## 5. Linear completed companions

Two companion directions avoid the nonlinear price.

### 5.1 Completed-background companion

Write

```text
K=B+H_E,                                             (5.1)
```

where `B` is the exact archimedean plus rational-pole background and `H_E`
is the centered actual von Mangoldt Loewner matrix.  Put

```text
w_B=P_(a^perp)B*a/||P_(a^perp)B*a||.                (5.2)
```

The direction depends on the candidate geometry and completed background,
not on the prime coefficients.  Therefore

```text
<a,Ka>,       <w_B,Kw_B>,       <w_B,Ka>            (5.3)
```

are three linear completed arithmetic scalars.  From the confluent data
`A_X,D_X`, each is obtained by contracting the exact Loewner matrix

```text
H_E(k,l)=2*(A_k-A_l)/(tau_k-tau_l),  k!=l,
H_E(k,k)=-2*D_k.                                    (5.4)
```

Equivalently each is one completed cross-correlation against
`d(psi(v)-v)`, with every prime power, the gamma term, and both pole pieces
retained.

### 5.2 Confluent target-row companion

Let `y_alpha` be the selected negative evaluation row and differentiate it
with respect to target depth before projecting to the target-only quotient.
The collision-stable geometric companion is

```text
w_alpha=normalize(P_(a^perp) P_S partial_alpha y_alpha).              (5.5)
```

It is also independent of the prime coefficients, so its three entries in
(1.2) remain linear completed scalars.  It probes the confluent direction
which survives when nearby evaluation rows collide.

The more naive Jacobi companion `P_(a^perp)J*a` is not uniformly useful.
The endpoint and target projections can make it vanish (and in the finite
fixture its size is strongly parity-sensitive); this is the same
boundary-leakage phenomenon behind the rank-two compressed displacement.

### 5.3 A three-dimensional version

Let `E=span{w_B,w_alpha}` after orthonormalization, and write

```text
D_E=P_E*K|E,          b_E=P_E*K*a.                  (5.6)
```

At the exact boundary `x=theta`, the best three-dimensional value is

```text
theta*r+(1-theta)*G_theta,

G_theta=max_(w in E, ||w||=1)
 [<w,D_E*w>+2*sqrt(theta/(1-theta))*abs(<b_E,w>)].  (5.7)
```

This is a two-variable trust-region problem.  In the generic case, after
fixing the harmless phase, its maximizer satisfies

```text
w=t*(lambda*I-D_E)^(-1)b_E,
t=sqrt(theta/(1-theta)),
t^2*<b_E,(lambda*I-D_E)^(-2)b_E> = 1.               (5.8)
```

with `lambda>lambda_max(D_E)`.  Hence even the `3 x 3` boundary gate reduces
to one scalar secular equation.  It uses more completed scalar data, but it
does not acquire a sign from rank-two displacement.

## 6. Why the known estimates still stop at strip strength

For any geometry-defined unit vectors `u,v`, the centered entry
`<u,H_Ev>/L^2` is bounded by the normalized completed operator estimate.
The current KMT consequence gives the scale

```text
M_T=sqrt(X)/L^(13/10).                              (6.1)
```

Bounding the three entries in (5.3) separately therefore proves at best

```text
Q_theta(a,w)>=-O(M_T)-O(1/L).                       (6.2)
```

At fixed depth, comparison with `kappa asymp X^alpha/L` gives

```text
M_T/kappa
 asymp X^(1/2-alpha)/L^(3/10),                      (6.3)
```

before any additional carrier-retention loss.  This diverges.  Moving
`alpha` close enough to `1/2` to reverse (6.3) enters the classical
zero-free region and yields no new strip.

The only way (1.4) can improve this ledger is a new **joint sign/orientation
theorem** showing that whenever the two diagonal scalars are negative at
the root scale, the off-diagonal scalar has the compensating size required
by (3.8).  Neither KMT nor current first/two-moment information asserts such
a relation.

Low Loewner displacement alone cannot assert it.  The scalar matrix

```text
K_bad=-M*I                                           (6.4)
```

already has zero commutator with every coordinate/Jacobi operator and is a
confluent Loewner matrix: the constant sharp multiplier has matrix
`2*pi*L*I`, so a negative constant gives (6.4) after scaling.  For every
carrier and every companion,

```text
r=d=-M,        c=0,        Q_theta=-M.              (6.5)
```

Adding the fixed completed background changes this only by its operator
scale.  More generally, the arbitrary-confluent-data proposition in the
sharp Loewner audit permits the same prescribed finite bad compression.
This is an information-level counterexample, not an actual-von-Mangoldt
counterexample.  The positive artificial-coefficient completed model in
the KMT obstruction report separately shows why coefficient positivity and
completion do not repair the missing sign.

## 7. Actual-coefficient finite diagnostics

The implementation is

```text
src/carrier_ritz_loewner_gate.py
src/test_carrier_ritz_loewner_gate.py
```

It uses the same actual-prime-power/pole/gamma assembly as the high-height
carrier fixture.  At `alpha=0.4`, aperture fraction `0.2`, and carrier
fraction `theta=0.9`, it gave:

| `T` | `dim S` | `kappa` | full `q_.9` | background + confluent `3D` | `3D/full` | arithmetic-Lanczos `2D` | `2D/full` |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 64 | 11 | 0.287376 | 0.944387 | 0.787203 | 83.36% | 0.936265 | 99.14% |
| 128 | 33 | 0.584987 | 0.943220 | 0.669319 | 70.96% | 0.935689 | 99.20% |
| 256 | 84 | 0.890464 | 1.252618 | 1.090394 | 87.05% | 1.225892 | 97.87% |
| 512 | 195 | 1.311849 | 1.286211 | 1.098660 | 85.42% | 1.277437 | 99.32% |

These are ordinary double-precision diagnostics.  The selected candidates
are not asserted to be zeros, and the signs are not interval-certified.
Every full-carrier scalar in this short run was already positive, so the
table does not test the decisive compensation scenario (negative diagonals
rescued by a cross term).  It establishes only that one Lanczos step is a
high-fidelity surrogate for the finite `theta=0.9` optimization in these
four fixtures.

Five regression tests verify (3.3) against a dense angular maximization,
exercise the boundary branch, check the moment identities (4.2), and test
the scalar Loewner countermodel (6.4).

Reproduction:

```bash
PYTHONPATH=src python3 -m pytest -q src/test_carrier_ritz_loewner_gate.py
PYTHONPATH=src python3 src/carrier_ritz_loewner_gate.py \
  --heights 64,128,256,512 --theta 0.5,0.9
```

## 8. Research consequence

The low-dimensional route should be retained in one sharply delimited form:

> Find a geometry-defined companion `w` (or the two-dimensional complement
> `span{w_B,w_alpha}`) and prove the carrier-normalized joint orientation
> inequality (3.8) for the **actual completed** von Mangoldt data, uniformly
> in target depth and ordinate.

This target is logically weaker than `r>=-o(kappa)` and much weaker than a
whole-matrix lower edge.  It is not implied by any current estimate.  If one
instead bounds all entries separately, the reduction collapses immediately
to the fixed-depth prime-polynomial barrier (6.3).

For computation, the arithmetic-Lanczos plane is the preferred fail-fast
surrogate because it nearly saturates the observed high-carrier edge.  For
analysis, the background/confluent plane is preferable because its entries
remain linear in the completed prime data.  Confusing those two choices
would hide the degree-two/three correlation bill.

Principal dependencies:

- `ZETA23-DIRECT-CARRIER-SLICE-FRONTIER-SYNTHESIS-2026-08-12.md`,
- `ZETA23-CONSTRAINED-SHARP-LOEWNER-PRIME-EDGE-2026-08-11.md`,
- `ZETA23-COMPLETED-CONSTRAINED-PICK-KMT-OBSTRUCTION-2026-08-11.md`, and
- `ZETA23-LOW-ORDER-NONLINEAR-CERTIFICATE-NOGO-2026-08-12.md`.
