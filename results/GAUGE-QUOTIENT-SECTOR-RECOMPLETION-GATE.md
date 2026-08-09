# Gauge-quotient sector recompletion and the surviving axis carrier

Status: R83 exact algebraic recompletion, complete-block rank theorem,
primitive Farey-beat frame, primary-literature gate, and finite fail-fast
diagnostic; 2026-08-07.  No fixed zero-free strip is proved.

R84 successor note: the generic/fixed-pair tensor-rank diagnosis in Section 7
is not the final obstruction for a global canonical bank.  Its common dual
has ratio form `W(theta/(pr))` and admits norm-stable log-Mellin separation.
The surviving obstruction is coefficient/phase alignment; see
[`COEFFICIENT-SPECIFIC-LOW-BEAT-TENSOR-GATE.md`](COEFFICIENT-SPECIFIC-LOW-BEAT-TENSOR-GATE.md).

R82 predecessor:
[`FINITE-RAMANUJAN-NULL-GAUGE-GATE.md`](FINITE-RAMANUJAN-NULL-GAUGE-GATE.md).

## 1. Verdict

The null-gauge optimization does not create a power saving.  It moves energy
between the degenerate and Wright sectors while leaving the physical energy
exactly invariant.  In a finite shell proxy, the best gauge representatives
retain a fixed positive fraction of the natural scale.

There is nevertheless one real simplification.  After the determinant-zero,
dual-zero, and punctured-axis sectors are recompleted exactly, the
determinant-zero Ramanujan singular-series fluctuation has polylogarithmically
bounded partial sums.  Smooth summation makes this part harmless.  The exact
recompletion leaves one object:

```text
smoothed (Lambda(n) delta_n-dt) one-point carrier
       + centered off-axis reciprocal block.                       (1.1)
```

The one-point term retains every zeta-zero residue.  Existing Kuznetsov and
Kloosterman-fraction theorems control only the nondegenerate block; bounding
the axis separately by a fixed power is already a fixed-zero-free-strip
theorem.  The correct new target is therefore a **joint centered off-axis
estimate**, before absolute values:

```text
H_(j theta !=0)-P_1-P_2 <<Y^(1-2 eta+o(1)),   eta>0.                 (1.2)
```

Up to subexponential window factors, (1.2) gives the R71 fixed-power energy
bound and hence a fixed zero-free strip.  No theorem in the checked
literature proves (1.2).

```text
finite all-nonzero Ramanujan gauge
  -> minimize non-Wright sectors on the null orbit       NO GAIN
  -> exact Feshbach/contact recompletion                  THEOREM
  -> determinant-zero singular-series fluctuation        CLEARED
  -> small-denominator complete-block replacement        IMPOSSIBLE
  -> square-root individual Farey-beat replacement       EXACT / NO SAVING
  -> separate Kuznetsov axis estimate                     STRIP-STRENGTH
  -> centered axis + off-axis estimate (1.2)              OPEN.     (1.3)
```

## 2. Gauge optimization on the physical quotient

Let `B` synthesize the completed finite Ramanujan mode columns, let

```text
H=B*B,
```

and let the columns of `K` be finite Ramanujan null relations, so `BK=0`.
Split the exact Hermitian energy into

```text
H=A+W,                                                   (2.1)
```

where `A` contains `theta=0`, `j=0`, and the completion axes, while `W`
contains `j theta!=0`.  Since `HK=0`, every representative

```text
x(c)=x_0+Kc                                              (2.2)
```

has the same physical energy

```text
E=x(c)*H x(c)=x_0*H x_0,
x(c)*W x(c)=E-x(c)*A x(c).                               (2.3)
```

Thus every reduction of the bad block transfers exactly the same scalar to
the nominal Wright block.

For any Hermitian sector `S`, put

```text
M_S=K*S K,        b_S=K*S x_0.                          (2.4)
```

Then

```text
x(c)*S x(c)=x_0*S x_0+2 Re(c*b_S)+c*M_S c.              (2.5)
```

The unrestricted minimum is finite exactly when

```text
M_S>=0,        b_S in Range(M_S).                       (2.6)
```

In that case

```text
inf_c x(c)*S x(c)
 =x_0*S x_0-b_S* M_S^dagger b_S.                       (2.7)
```

A negative direction of `M_S`, or a linear forcing in its kernel, makes the
formal infimum `-infinity`; this is coordinate arbitrage, not cancellation.

When `M_A` is invertible, the canonical quotient forms are

```text
A#=A-AK(K*AK)^(-1)K*A,
W#=W+AK(K*AK)^(-1)K*A=H-A#.                            (2.8)
```

Both annihilate `K`.  The second formula displays the exact low-rank contact
term which must be added to the native Wright sector.  Consequently a
spectral theorem for `W` alone is not a theorem for the quotient; it must
control `W#`, or equivalently retain the contact carrier in (1.2).

There is an even shorter no-go inequality.  For every representative,

```text
abs(x*A x)+abs(x*W x)>=E.                               (2.9)
```

Null-gauge algebra alone therefore cannot make both pieces power-small.

If a Wright theorem only supplies a positive majorant `P` with
`abs(x*W x)<=x*P x`, then `R=P-W>=0` and

```text
inf_c x(c)*(A+P)x(c)
 =E+inf_c x(c)*R x(c)>=E.                              (2.10)
```

Optimization can remove slack in that majorant, but it cannot lower the
unknown physical energy.

## 3. Exact recompletion of the non-Wright sectors

Use R82's gauged coefficients `htilde_q`, with `htilde_1=1`, and work on a
range where

```text
lambda_N(n)=sum_(q<=N)htilde_q c_q(n)=Lambda(n).        (3.1)
```

Let `L(t,u)=K_(V,psi)(t,u)/sqrt(tu)` be the smooth compact kernel from R81
and define

```text
f(h)=integral L(u+h,u)du,
S_N(h)=sum_(q<=N)abs(htilde_q)^2 c_q(h)=1+R_N(h),

D_0=sum_n abs(lambda_N(n))^2 L(n,n),
A_1=sum_n lambda_N(n) integral L(n,u)du,
A_2=sum_n conjugate(lambda_N(n)) integral L(t,n)dt,
C  =double_integral L(t,u)dtdu.                         (3.2)
```

All limits below are the same smooth rectangular limits as R81--R82.

### Theorem 3.1 (sector recompletion)

With the primitive common-factor mask retained, the three completed sectors
satisfy

```text
H_(theta=0)=sum_h S_N(h)f(h),
H_(j=0)=D_0-S_N(0)f(0),
H_axes=-A_1-A_2+C.                                     (3.3)
```

Consequently, if

```text
Q_L=sum_h f(h)-C,
P_1=A_1-C,          P_2=A_2-C,                         (3.4)
```

then

```text
H_nonW
 =[D_0-f(0)]+Q_L-P_1-P_2
   +sum_(h!=0)R_N(h)f(h).                              (3.5)
```

#### Proof

For reduced rational frequencies, equality `a/q=b/r` forces `q=r` and
`a=b`.  Primitive Poisson summation in this equal-frequency line gives the
first formula in (3.3), because the primitive residue sum at integer
difference `h` is `c_q(h)`.

Poisson summation in the full solution lattice sends `j=0` to the physical
diagonal.  Summing the primitive masks reconstructs `lambda_N(n)` on each
side, giving `D_0`; the intersection with `theta=0` is `S_N(0)f(0)` and is
subtracted once.  Finally, inclusion--exclusion for the two zero numerators
added by completing the lattice gives `-A_1-A_2+C`.  Adding these identities,
writing `S_N=1+R_N`, and using (3.4) gives (3.5).

### Theorem 3.2 (the singular-series fluctuation is harmless)

For every integer interval `I` and every `q>1`, the divisor formula gives

```text
abs(sum_(h in I)c_q(h))<=sigma(q).                     (3.6)
```

Indeed, count multiples of every `d|q`, subtract the vanishing main term
`abs(I) sum_(d|q)mu(q/d)=0`, and bound each floor error by one.  Hence

```text
sup_I abs(sum_(h in I)R_N(h))
 <=sum_(q>=2)abs(htilde_q)^2 sigma(q)
 <<log^5(N)(log log N)^2.                              (3.7)
```

The last estimate uses R82's
`sum phi(q)abs(htilde_q)^2<<log^5 N` and
`sigma(q)/phi(q)<< (log log N)^2`.  Summation by parts now yields

```text
abs(sum_h R_N(h)f(h))
 <<log^5(N)(log log N)^2
   [norm(f)_infinity+Var(f)].                          (3.8)
```

For the normalized R71 shells, the bracket and all window losses are
`Y^o(1)`.  Also `D_0-f(0)=Y^o(1)` by the elementary diagonal bound for
`Lambda^2`, and `Q_L=Y^o(1)` by ordinary smooth Poisson summation.  Thus

```text
H_nonW=-P_1-P_2+Y^o(1).                                (3.9)
```

For a Hermitian kernel, `P_2=conjugate(P_1)`.  Explicitly,

```text
P_1=<sum_n Lambda(n)delta_n-dt,
     t |-> integral L(t,u)du>.                         (3.10)
```

The explicit formula for (3.10) contains the residue sum over every zeta
zero.  A separate fixed-power estimate for it is already fixed-strip
information.  Equation (3.9) is therefore a simplification, not a proof: it
shows exactly which degenerate term must cancel against the off-axis block.

## 4. A complete-block uncertainty theorem

The hoped-for repair was to absorb the remaining carrier using only small
complete Ramanujan blocks.  There is an exact finite obstruction.

### Theorem 4.1 (Ramanujan matrix determinant)

Let

```text
C_Y=(c_q(n))_(1<=n,q<=Y).                              (4.1)
```

Then

```text
det(C_Y)=product_(q<=Y)q=Y!.                           (4.2)
```

#### Proof

The divisor formula factors `C_Y=A_Y B_Y`, where

```text
A_Y(n,d)=1_(d|n),
B_Y(d,q)=d mu(q/d)1_(d|q).                             (4.3)
```

The first matrix is lower triangular with diagonal one.  The second is upper
triangular with diagonal `1,2,...,Y`.  This proves (4.2).

### Corollary 4.2

There is no nonzero complete-block null relation supported on `q<=Y` over
the active integers `1<=n<=Y`.  In particular, a block-coherent exact gauge
which changes the `q=1` coefficient must use a modulus `q>Y`.

This explains the scale in R82 without a conditioning heuristic: the
high-prime cloud is not an inefficient choice that can be compressed into
complete blocks of Wright size.  Individual Farey frequencies are more
overcomplete, but a coefficient-uniform replacement then meets the usual
`Q^2` conditioning threshold and does not preserve the Ramanujan arithmetic
vector.

The factorization, determinant certificate, interval bound, and exact
Ramanujan-correlation law are exercised by
[`ramanujan_sector_recompletion_probe.py`](../src/ramanujan_sector_recompletion_probe.py).

## 5. Why current spectral theorems stop at the same carrier

For the classical Kloosterman sum,

```text
S(0,n;c)=c_c(n),            S(0,1;c)=mu(c).             (5.1)
```

Moreover, initially in the common absolute-convergence half-plane
`Re(s)>2`,

```text
sum_(c>=1)S(0,n;c)c^(-s)=sigma_(1-s)(n)/zeta(s),
sum_(c>=1)S(0,0;c)c^(-s)=zeta(s-1)/zeta(s).            (5.2)
```

Thus a smooth dyadic estimate, uniform through the axis and with a fixed
power saving, would include

```text
sum_c mu(c)w(c/C)<<C^(1-eta).                          (5.3)
```

A uniform family of (5.3), followed by Mellin inversion, gives a fixed
zero-free strip.  The missing spectral axis literally contains the target.

The closest imported theorems respect this boundary:

1. Deshouillers--Iwaniec's
   [Kloosterman-sum theorem](https://doi.org/10.1007/BF01390728) requires
   both Kloosterman indices to be nonzero and separable coefficient data.
2. Pascadi's 2025
   [optimized DI theorem](https://doi.org/10.1112/S0010437X2500747X)
   removes the zero Fourier mode and determinant diagonal before invoking
   the spectral estimate.  Its phase parameter is fixed independently of
   the level variables, unlike R81's coupled amplitude.
3. Pascadi's
   [exceptional-spectrum large sieve](https://arxiv.org/abs/2404.04239)
   improves the exceptional contribution, not the regular spectrum,
   diagonal, or zero index.
4. Wright's 2026
   [trilinear estimate](https://arxiv.org/abs/2604.25177) assumes a nonzero
   phase and does not supply the joint subtraction in (1.2).  The stronger
   Dong--Robles--Zeindler comparison once proposed in
   [arXiv:2601.00292](https://arxiv.org/abs/2601.00292) was withdrawn after a
   missing factor destroyed the claimed improvement, so it is not an
   imported theorem here.

Regularized Kuznetsov theory does not merge the axis either.  Bruggeman's
[original formula](https://webspace.science.uu.nl/~brugg103/notes/78B-fcmf.pdf)
assumes both Fourier indices are nonzero.  At a zero index the classical
kernel argument `4 pi sqrt(abs(mn))/c` collapses to zero for every modulus,
so an `m->0` limit loses modulus localization.  Zagier's
[regularized Rankin--Selberg theorem](https://doi.org/10.15083/00039589)
subtracts prescribed growth only from the zeroth Fourier coefficient.  The
nonzero Eisenstein coefficient remains proportional to
`sigma_(1-2s)(n)/xi(2s)`, exactly the denominator in (5.2).  Mean-zero
centering removes the residual pole at `s=1`; it does not cancel the poles at
`2s=rho`.  Regularization makes the pairing finite but leaves a separate
scattering/contact term carrying the same zeta zeros.

The literature conclusion is not that spectral technology is irrelevant.
It is that an importable theorem controls `H_(j theta!=0)` only after the
term which must cancel it has been separated.  A successful estimate must be
coefficient-specific and Eisenstein/axis-renormalized before Cauchy--Schwarz.

## 6. Finite fail-fast calculation

A finite-torus proxy used

```text
S_(nq)=c_q(n),          1<=n<=Y, q<=2Y,
Sx=Lambda|_[1,Y],       x_1=1,                         (6.1)
```

with a smooth positive shell kernel.  Primitive Farey modes were clustered
at resolution `1/Y`, averaged over eight shifted partitions, to form a
positive proxy for the non-Wright sector.  Under a coefficient ledger at
most ten times the baseline, the optimized values were

| `Y` | optimized bad energy divided by `Y` |
|---:|---:|
| 64 | 0.453 |
| 80 | 0.441 |
| 96 | 0.443 |
| 128 | 0.431 |

The values stabilize at natural scale.  Changing the Farey resolution keeps
the quotient between approximately `0.44Y` and `0.52Y`.

The exact top-prime null witness is even sharper.  With

```text
w_p=1/[(p-1)sum_(Y<r<=2Y)1/(r-1)],
u=(1,(w_p)_(Y<p<=2Y)),                                 (6.2)
```

one has `Su=0`, while

| `Y` | `u*B_bad u/Y` | ledger `u*W u` | `lambda_max/Y` |
|---:|---:|---:|---:|
| 64 | 1.936 | 7.87 | 0.516 |
| 128 | 1.916 | 8.89 | 0.511 |
| 256 | 1.927 | 9.52 | 0.509 |

At `Y=256`, the proxy decomposes the null witness as

```text
theta-zero       153.28
axes             -78.52
j-zero proxy     418.65
off-axis        -493.41.                               (6.3)
```

The full synthesis is zero, so the natural-size cancellation in (6.3) is
exact.  Gauge optimization frequently inflates the individual diagonal and
axis pieces while reducing their sum by only a constant factor.

This calculation collapses integer aliases on a finite torus and proxies the
continuous `j=0` split.  It is a fail-fast diagnostic, not an asymptotic
theorem.  Its role is to reject a proposed power mechanism; the exact
quotient algebra in Section 2 supplies the rigorous reason.

## 7. An exact quadratic Farey-beat gauge

Combining (3.9) with the full sector identity gives

```text
E_R71=H_(j theta!=0)-P_1-P_2+Y^o(1).                  (7.1)
```

The next theorem should be formulated directly for the centered expression
on the right, restricted to the exact finite von Mangoldt coefficient
vector.  A coefficient-uniform statement is false or strip-strength by the
specialization (5.1).

There is a nonstandard exact way to move the axis into nonzero frequencies
without the large **individual** moduli of Section 4.  It passes the phase,
modulus, and coefficient-square-norm gates, but fails the coefficient class
accepted by current Wright estimates.

### Theorem 7.1 (primitive beat frame)

Let `I` be `H` consecutive integers, take distinct primes `p,r`, put `M=pr`,
and define

```text
A_(n,theta)=e(theta n/M),
n in I, theta in (Z/MZ)^*.                              (7.2)
```

Then

```text
(AA*)_(n,m)=c_M(n-m)
 =M 1_(n=m)-p 1_(p|n-m)-r 1_(r|n-m)+1                 (7.3)
```

provided `H<M`.  Consequently

```text
kappa I<=AA*<=(M+H)I,
kappa=M-p ceil(H/p)-r ceil(H/r).                       (7.4)
```

Choose `p,r=(2+o(1))sqrt(H)`.  Then

```text
M=(4+o(1))H,             kappa=(2+o(1))H.              (7.5)
```

Every vector `v=(v_n)_(n in I)` therefore has the exact minimum-norm
expansion

```text
v_n=sum_(theta in (Z/MZ)^*)gamma_theta e(theta n/M),
gamma=A*(AA*)^(-1)v,                                   (7.6)

norm(v)_2^2/(M+H)<=norm(gamma)_2^2
                  <=norm(v)_2^2/kappa.                 (7.7)
```

For every unit `theta mod M`, the Chinese remainder theorem gives unique
nonzero residues `a mod p`, `b mod r` such that

```text
theta=ar-bp (mod pr),
e(theta n/M)=e(n[a/p-b/r]).                            (7.8)
```

Thus all modes in (7.6) are genuine primitive beats of two denominator
`asymp sqrt(H)` frequencies.

#### Proof

The first equality in (7.3) is the primitive character sum.  Multiplicativity
and `c_p(h)=p 1_(p|h)-1` give its second line.  The divisibility matrices in
(7.3) are positive semidefinite block matrices whose operator norms are at
most `ceil(H/p)` and `ceil(H/r)`; the all-one matrix is positive.  This gives
the lower bound.  Dropping the two negative matrices and bounding the
all-one matrix by `H I` gives the upper bound.  Equations (7.6)--(7.7) are the
canonical frame inverse, and (7.8) is CRT.

Apply the theorem to `v_n=Lambda(n)-1` on an active interval comparable with
its height.  The elementary second moment gives

```text
sum_theta abs(gamma_theta)^2<<log H.                   (7.9)
```

If `G(t)=integral L(t,u)du`, Poisson summation gives the exact axis rewrite

```text
P_G
 =sum_(a,b)gamma_(a,b)
    sum_(k in Z)Ghat(k-a/p+b/r)
  +sum_(k!=0)Ghat(k).                                  (7.10)
```

The last sum is the ordinary smooth Euler error.  It is smaller than every
fixed power after normalized smooth scaling.  Hence the prime axis really
can be moved into primitive nonzero beats with `p,r asymp sqrt(H)` and a
polylogarithmic square ledger.

### Why this is not yet a Wright estimate

The frame is well conditioned in both directions.  It preserves the full
`L2` information in `Lambda-1`; it does not cancel it.  Even the vector
`v_n=1` has `norm(gamma)_2=O(1)` but pairs with a smooth plateau at size
`asymp H`.  Therefore nonzero beat phase plus a small Hilbert ledger cannot
imply a power saving for arbitrary coefficients.

For one fixed pair `(p,r)`, (7.6) has no denominator averaging.  A bank of
pairs produces a dense tensor `gamma_(p,r,theta)`, whereas the imported
Wright form has separable data `alpha_p beta_r nu_theta`.  Reshaping one
coefficient block as a `(p-1)` by `(r-1)` matrix can require rank
`asymp sqrt(H)`.  Termwise singular-value decomposition costs as much as

```text
sqrt(rank) asymp H^(1/4),                              (7.11)
```

which overwhelms the nominal `H^(-1/40)` Wright saving.  Dimension counting
makes this generic: a universal rank-`R` representation needs

```text
R(p+r-R)>=H,
```

so `R>>sqrt(H)` in this range.

A separate approximation diagnostic found that roughly twenty independent
Farey beats can approximate a smooth constant envelope to errors between
`0.06` and `0.002` over `Y=256,...,8000`, with bounded observed `L1` and `L2`
coefficients.  This confirms that frequency approximation itself is not the
barrier.  Those independent coefficients have not been realized as the
shared-denominator arithmetic tensor in (7.10), and the computation is not
an asymptotic certificate.  It is reproduced by
[`farey_beat_envelope_probe.py`](../src/farey_beat_envelope_probe.py).

The square-root scale is essentially forced.  If every constituent
denominator is at most `Q`, then every nonzero scaled beat obeys

```text
abs(nu)=Y abs(a/q-b/r)>=Y/Q^2.
```

If `sum_j c_j e(nu_j x)` approximates one on `[0,1]` with uniform error
`epsilon<1`, integration and the sinc bound give

```text
sum_j abs(c_j)>=pi(1-epsilon)Y/Q^2.                   (7.11a)
```

Thus a polylogarithmic `L1` ledger requires
`Q>=sqrt(Y)/polylog(Y)`.  The beat construction reaches the critical scale;
there is no much-smaller-modulus version with comparable coefficient cost.

The beat mechanism therefore advances the target one gate: large individual
moduli are avoidable.  The live theorem would have to exploit the canonical
prime-derived dense tensor without a rank loss.  A generic arbitrary-tensor
version is impossible because its coefficients can select the conjugate
phase term by term.

This remains true for Hilbert-valued extensions of Wright.  A scalar estimate
on pure tensors extends to a general coefficient tensor only with its
projective/separable norm

```text
norm(C)_(pi,2)
 =inf_(C=sum_s alpha_s tensor beta_s tensor nu_s)
   sum_s norm(alpha_s)_2 norm(beta_s)_2 norm(nu_s)_2,   (7.12)
```

not its Frobenius norm.  Every matrix flattening nuclear norm is a lower
bound for (7.12).  Taking the coefficient tensor to be the conjugate of the
oscillatory kernel removes every phase termwise, showing that a generic
Frobenius-norm gain is impossible.  The canonical fixed-`(p,r)` beat matrix
can itself have full rank by a Vandermonde factorization, so there is no
hidden universal low-rank repair.

The actual canonical `Lambda-1` tensor also shows no finite low-rank rescue:

| `H` | `p,r` | nuclear/Frobenius norm | numerical rank |
|---:|---:|---:|---:|
| 32 | 13,17 | 3.216 | 12 |
| 64 | 17,19 | 3.540 | 16 |
| 128 | 23,29 | 4.291 | 22 |
| 256 | 37,41 | 5.317 | 36 |
| 512 | 47,53 | 5.951 | 46 |
| 1024 | 67,71 | 7.005 | 66 |

This is a floating finite diagnostic, not an asymptotic lower bound.  It
does reject the hope that the first tested prime tensors are accidentally
bounded rank.

Finally, the smallest beats are exactly the old carrier in new coordinates.
For `G_Y(t)=g(t/Y)` and `M=cY+o(Y)`, (7.10) becomes

```text
P_(G_Y)/Y
 =sum_(0<abs(theta)<=Y^epsilon)gamma_theta W_c(theta)
  +O_B(Y^(-B)),                                        (7.13)
```

for every fixed `epsilon,B>0`; Schwartz decay removes larger symmetric
representatives.  The explicit formula for the left side contains

```text
-sum_rho Y^(rho-1) Mellin(g)(rho).                     (7.14)
```

Thus a `Y^(-eta)` bound for the weighted low-beat sum in (7.13) is itself a
fixed zero-free strip.  The quadratic gauge has relocated the axis to a
square-root-denominator principal band; it has not made that band a routine
minor arc.

The exact frame, CRT beat map, eigenvalue certificate, reconstruction, and
coefficient norm bounds are exercised by
[`farey_beat_frame_probe.py`](../src/farey_beat_frame_probe.py).  The finite
sector optimization is implemented separately in
[`ramanujan_sector_gauge_numeric.py`](../src/ramanujan_sector_gauge_numeric.py).

## 8. Reality check

R83 has not produced a fixed zero-free strip.  It has removed three false
targets:

* optimize a null-cloud representative until every sector is small;
* import a spectral theorem uniformly through its zero index; and
* tensorize a separable Wright estimate losslessly on an arbitrary beat
  frame.

It has also produced a sharper positive reduction: the determinant-zero
singular-series block is not the obstruction.  The frontier is the joint
axis-renormalized off-axis estimate (1.2), with its contact term present
inside the theorem.  Proving that estimate with one fixed power would be the
new zero-free strip.
