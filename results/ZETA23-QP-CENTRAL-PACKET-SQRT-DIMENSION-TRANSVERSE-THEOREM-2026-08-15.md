# QP central packets: a square-root-dimension transverse theorem

**Date:** 2026-08-15  
**Verdict:** on the restricted actual-node family

```text
S_(Y,H)={n=p^k:|n-Y|<=H},
Y=N+1/2,                 H<=Y^(1/2-epsilon),
```

odd half-integer parity eliminates all cubic resonances.  After retaining
the near-reflected difference coordinates, the centered standardized third
moment is `o(1)` uniformly in every signed coefficient vector.  Consequently
the restricted moment body satisfies

```text
s_v >> M_H^(-1/2),          r_+ >> M_H^(-1/2),      (0.1)
```

where `M_H=|S_(Y,H)|` and `v=a_H(t_0)+Dq_0`, uniformly for
`0<=t_0<=B` and `0<=D<=1`.

There is no cross-side cluster defect: a normalized reflected difference
becomes a divided difference of the smooth Fourier kernel, and its small
denominator is canceled by a derivative at frequency `>>B/Y`.

This is a theorem only for the coordinate projection to the central packet.
It does not give (0.1) for the full fixed-width shell, does not improve the
proved full-shell `49/66` theorem, and proves no QP or strip statement.

---

## 1. Setup

Fix `A>1`, put `B=Y^A`, and let `epsilon>0` be fixed.  Let `S_(Y,H)` be any
set of distinct integers in

```text
0<|n-Y|<=H<=Y^(1/2-epsilon).                        (1.1)
```

The theorem therefore applies, in particular, when the integers are actual
prime powers.  Set

```text
u_n=|log(n/Y)|,
a_H(t)=(cos(tu_n))_(n in S_(Y,H)),
q_0=(1,...,1),
M_H=|S_(Y,H)|.                                      (1.2)
```

Take either:

1. a fixed nonnegative smooth compactly supported probability `psi` on
   `(1/3,2/3)`; or
2. the explicit order-`q` B-spline probability from the nonlinear lab,
   whose scaled characteristic function is

```text
Phi_q(r)=exp(ir/2)sinc(r/(6q))^q.                   (1.3)
```

In the B-spline case assume

```text
q(A-1)>3/4.                                         (1.4)
```

The project choice `A=50/33`, `q=8` satisfies (1.4) with ample room; even
`q=2` does.  In both cases write

```text
rho_B(t)=B^(-1)psi(t/B),                            (1.5)
```

so `rho_B` is supported in `[B/3,2B/3]`, hence in the legal height band for
all sufficiently large `Y`.

For a coefficient vector `y`, put

```text
F_y(t)=sum_n y_n cos(tu_n),
m_y=int F_y rho_B,
V_y=int (F_y-m_y)^2rho_B,
mu_3(y)=int (F_y-m_y)^3rho_B.                       (1.6)
```

---

## 2. Odd parity separates every cubic frequency

Write

```text
h_n=|n-Y| in {1/2,3/2,5/2,...}.                    (2.1)
```

Uniformly under (1.1), Taylor's formula gives

```text
u_n=h_n/Y+O(H^2/Y^2).                               (2.2)
```

For arbitrary signs `sigma_i in {+1,-1}`, the number

```text
sigma_1 h_1+sigma_2 h_2+sigma_3 h_3                (2.3)
```

is an odd half-integer.  In particular, it is never zero and has absolute
value at least `1/2`.  Equations (1.1)--(2.2) therefore imply, uniformly in
repetitions and signs,

```text
|sigma_1u_1+sigma_2u_2+sigma_3u_3|
 >=1/(2Y)-O(H^2/Y^2)>=1/(3Y)                       (2.4)
```

for all sufficiently large `Y`.

The same expansion describes the collision geometry.  If two nodes have
different distances `h_n` from `Y`, their frequencies differ by
`>>1/Y`.  Thus the only possible `o(1/Y)` cluster consists of the two
symmetric integers `Y-h` and `Y+h`.  Its gap is

```text
delta_h=|-log(1-h/Y)-log(1+h/Y)|
        =-log(1-h^2/Y^2) asyp h^2/Y^2.             (2.5)
```

Every cluster has size at most two, and distinct clusters are `>>1/Y`
apart.

---

## 3. The divided-difference frame retains the reflected mode

For a singleton, use its ordinary coefficient.  For a two-node block with
frequencies `alpha,beta`, coefficients `c_alpha,c_beta`, and

```text
z=B|alpha-beta|,
p=c_alpha+c_beta,
d=min(1,z)(c_alpha-c_beta),                         (3.1)
```

use block energy `p^2+d^2`.  Let `E_H(y)` be the sum of these block energies.

The standard two-cluster calculation gives

```text
int F_y^2rho_B asyp E_H(y),                         (3.2)
sup_(0<=t<=B)|F_y(t)|<<sqrt(M_H)E_H(y)^(1/2).      (3.3)
```

For completeness, when `z<1`, the normalized difference mode is, up to an
absolute factor,

```text
[cos(talpha)-cos(tbeta)]/z.                         (3.4)
```

It is uniformly bounded for `0<=t<=B`, because the numerator is at most
`t|alpha-beta|`.  Its Gram entries are first or second divided differences
of the scaled Fourier transform.  The factors `z` in their denominators are
canceled by derivatives.  The within-block limiting Gram is positive
definite because `psi` has positive variance.  Between different blocks,
the derivative is evaluated at distance `>>B/Y`; Fourier decay makes the
off-block row sum `o(1)`.  This proves (3.2)--(3.3), including arbitrarily
small values of (2.5).

The identical cancellation controls cubic entries.  Express the normalized
block modes as `G_1,...,G_(M_H)`.  A product of three ordinary modes is a
finite sum of Fourier kernels at the signed frequencies (2.4).  Each
normalized difference mode applies one divided difference to that kernel.
After the denominator is canceled, this is a derivative of order at most
three.  This remains true if the same reflected block occurs two or three
times: regard the repeated copies as independent endpoint variables before
taking the corresponding mixed derivative.  Each normalized difference is
used only when its scaled gap `z<1`, so the entire scaled interpolation box
has width less than three.  Its corner arguments have modulus `>>B/Y` by
(2.4), and hence every point of the box still has modulus `>>B/Y`.  Blocks
with `z>=1` require no divided interpolation and are expanded endpoint by
endpoint.

More exactly, switching between the two endpoints of a reflected block does
not change its leading distance `h/Y`; it changes only the quadratic
remainder in (2.2).  Therefore **all corners of a fixed divided-difference
box share the same signed odd-half-integer leading term**.  They are not just
individually nonzero.  This also proves directly that a box from arbitrarily
repeated blocks cannot bridge the origin.

For every fixed `K`, the smooth bump therefore gives

```text
|int G_i G_j G_k rho_B|<<_K(Y/B)^K.                (3.5)
```

For the order-`q` B-spline, (1.3) and each of its first three derivatives
are `O_q((1+|r|)^(-q))`.  Explicitly, every fixed derivative of
`sinc(r/(6q))` is `O_q(|r|^(-1))`; Leibniz's rule leaves `q` such factors,
and derivatives of `exp(ir/2)` do not change the decay.  Thus (3.5) holds
with `K=q`.

The one-mode version of the same argument gives

```text
|int G_i rho_B|<<_K(Y/B)^K.                        (3.6)
```

---

## 4. Uniformly negligible centered skew

Write `F_y=sum_i b_iG_i`.  By construction and (3.2),

```text
||b||_2^2 asyp E_H(y).                              (4.1)
```

Equations (3.5)--(3.6) and Cauchy--Schwarz give

```text
|m_y|<<M_H^(1/2)(Y/B)^K E_H(y)^(1/2),              (4.2)
|int F_y^3rho_B|
 <<M_H^(3/2)(Y/B)^K E_H(y)^(3/2).                  (4.3)
```

Since `M_H<=2H+1`, the B-spline hypothesis (1.4) yields

```text
theta_Y:=M_H^(3/2)(Y/B)^q
 <<Y^(3/4-(3/2)epsilon-q(A-1))=o(1).               (4.4)
```

For the smooth bump, choose `K` sufficiently large and obtain the same
conclusion.  Equations (3.2), (4.2), and (4.4) imply

```text
V_y asyp E_H(y).                                    (4.5)
```

Finally,

```text
mu_3(y)=int F_y^3rho_B-3m_y int F_y^2rho_B+2m_y^3,
```

so (4.2)--(4.5) prove the uniform estimate

```text
|mu_3(y)|/V_y^(3/2)<<theta_Y=o(1)                  (4.6)
```

for every nonzero signed coefficient vector.  This is where ordinary
coordinate estimates would fail: a reflected difference may have tiny
ordinary variance, but (3.4)--(3.5) show that normalization does not amplify
its cubic moment.

---

## 5. Positive range at the variance scale

Let

```text
Z=F_y-m_y,       gamma=mu_3(y)/V_y^(3/2),
H_Z=sup_(t in supp rho_B)Z(t).                      (5.1)
```

The sharp cubic endpoint inequality gives

```text
H_Z/sqrt(V_y)>=[gamma+sqrt(gamma^2+4)]/2.           (5.2)
```

By (4.2) and (4.6), `gamma=o(1)` and
`|m_y|=o(E_H(y)^(1/2))`.  Hence (4.5)--(5.2) give, uniformly in every
nonzero `y`,

```text
h_H(y):=sup_(t in H_Y)F_y(t)
 >=sup_(t in supp rho_B)F_y(t)
 >>E_H(y)^(1/2)>0.                                 (5.3)
```

This removes the `M_H^(-1/2)` positive-range loss in the earlier
second-moment argument.

---

## 6. Restricted transverse and radial floors

Let

```text
P_(Y,H)=conv{a_H(t):t in H_Y},
v=a_H(t_0)+Dq_0,       0<=t_0<=B,       0<=D<=1,
s_v=sup{s>=0:-sv in P_(Y,H)}.                       (6.1)
```

The pointwise bound (3.3) gives

```text
|y.v|<=|F_y(t_0)|+|F_y(0)|
      <<sqrt(M_H)E_H(y)^(1/2).                      (6.2)
```

Combining (5.3) and (6.2), for sufficiently small fixed `c>0` and every
dual vector `y`,

```text
y dot[-cM_H^(-1/2)v]<=h_H(y).                       (6.3)
```

Indeed, when `y.v<0`, this follows from (5.3)--(6.2); when `y.v>=0`, the
left side is nonpositive while (5.3) is positive.  Compact support-function
separation places the point on the left of (6.3) in `P_(Y,H)`.  Therefore

```text
s_v>>M_H^(-1/2).                                    (6.4)
```

Taking `v=q_0` and using `|F_y(0)|` in (6.2) proves identically

```text
r_+(H_Y;S_(Y,H))>>M_H^(-1/2).                      (6.5)
```

The constants may depend on `A`, `epsilon`, and the fixed time law, but not
on `Y`, `H`, the selected integer subset, `t_0`, `D`, or `y`.

---

## 7. Scope

```text
central-packet cubic nonresonance:                  PROVED;
reflected divided-difference cancellation:          PROVED;
restricted s_v,r_+ >>M_H^(-1/2):                   PROVED;
corresponding full-shell bounds:                    NOT PROVED;
QP, LTRAD_full, or a uniform strip:                 NOT PROVED.
```

The threshold `H<<sqrt(Y)` is structural for this proof.  At that scale the
quadratic logarithmic correction is `o(1/Y)` and cannot cancel the odd
half-integer linear term.  Once `H` reaches order `sqrt(Y)`, the correction
has the same size as the parity gap; beyond it, the argument supplies no
uniform cubic separation.

---

## 8. Exact audit replay

The parity, reflection-box corner identity, Taylor lower bound, and exponent
ledger are independently replayed with rational arithmetic in

```text
src/qp_central_packet_parity_gate.py
src/test_qp_central_packet_parity_gate.py.
```

The test suite also stresses three reflected difference blocks, including
all repeated cubic tensor entries, against the exact-transform B-spline
moment formulas.  This last check is floating and diagnostic; the proof
above uses the analytic divided-difference identity.

```bash
PYTHONPATH=src python3 src/qp_central_packet_parity_gate.py \
  --N 1000000 --H 200 --spline-order 8 \
  --epsilon-numerator 1 --epsilon-denominator 10

PYTHONPATH=src python3 -m pytest -q \
  src/test_qp_central_packet_parity_gate.py \
  src/test_qp_transverse_joint_invariant_lab.py
```

Current result: `11 passed`.
