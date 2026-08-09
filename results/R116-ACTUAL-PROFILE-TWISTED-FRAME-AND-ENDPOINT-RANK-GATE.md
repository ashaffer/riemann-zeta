# R116 actual-profile twisted frame and endpoint-rank gate

Status: the exact `k`-dependence of the Blomer--Pascadi completion packet is
inserted into R115's coefficient-pair frame.  Retaining the additional
coordinate `x=h_1+h_3` restores an exact near-orthogonal frame, including a
sharper exact frame on `P=0`.  At the critical scale, however, the `H`
possible values of `x` consume exactly the gain needed at a multiplier block
of length `H`.  Even an ideal collision estimate for the enlarged
coefficient map reaches, but does not beat, the direct bound there.  A
Schatten-moment calculation also proves that a uniform low-rank separation
of the endpoint modulation is impossible: for at least half of the endpoint
residues, relative-accuracy separation needs rank `Omega(H)`.  Thus the
actual-profile phase cannot simply be absorbed at subpower cost.  No fixed
zero-free strip is proved.

Date: 2026-08-07.

Companion reports:
[`R105-QH-VAUGHAN-TAIL-NATIVE-BRIDGE-AUDIT.md`](R105-QH-VAUGHAN-TAIL-NATIVE-BRIDGE-AUDIT.md),
[`R111-OUTER-PRIME-PACKET-SEPARATION-AUDIT.md`](R111-OUTER-PRIME-PACKET-SEPARATION-AUDIT.md),
[`R112-CENTRAL-MATRIX-CORRECTION-BOUND.md`](R112-CENTRAL-MATRIX-CORRECTION-BOUND.md),
and
[`R115-RECIPROCAL-DISCRIMINANT-K-SUM-GATE.md`](R115-RECIPROCAL-DISCRIMINANT-K-SUM-GATE.md).

## 1. Verdict

For a fixed prime modulus `r`, the short-box Kloosterman multiplier is the
integer `k`.  Pascadi's completed odd profile is

```text
w_(1,k)(n)=Phihat(Mn/r)e_r(-s_1 k n).                 (1.1)
```

Consequently its autocorrelation is exactly

```text
z_(odd,k)(h)=e_r(-s_1 k h)z_odd^0(h),                 (1.2)
```

where `z_odd^0` is independent of `k`.  The two odd factors in the fourth
trace therefore contribute

```text
e_r(-s_1 k x),             x=h_1+h_3.                 (1.3)
```

This is not an unspecified smooth dependence.  It is a partial Fourier
matrix in `(k,x)`.

Put, as in R115,

```text
P=h_1h_2h_3h_4,
Q=(h_1+h_3)(h_2+h_4),
D_(P,Q)(k)=(P-kQ)(P-kQ+4k^2).                        (1.4)
```

The main positive result of this report is the exact twisted Gram identity

```text
G=B[r(r-2)-1]I+A,
A_(k,l)=sum_(x in X)e_r(-s_1(k-l)x),                 (1.5)
```

where `X` is any set of `B` retained `x`-values.  For `s_1!=0`, `A` is
positive semidefinite and `norm(A)<=r`.  Thus the `k`-columns remain almost
orthogonal after the real phase is retained.

The bad news is the diagonal in (1.5): it is `B r(r-2)`, and the actual
packet has `B asymp H` at `r asymp H^2`.  If `L` distinct multipliers are
being averaged, even the optimistic enlarged-coordinate energy

```text
sum_(P,Q,x)abs(C(P,Q,x))^2 <<H^epsilon Z^2           (1.6)
```

only gives, for unit multiplier weights,

```text
abs(T)<<r sqrt(HL) Z.                                (1.7)
```

The direct estimate is `L H^2 Z`.  At `r=H^2`, their ratio is
`sqrt(H/L)`.  Hence (1.7) saves only for `L>H` and is exactly the direct
scale at `L=H`.  The actual profile phase therefore removes the proposed
overlap from R115 Target 8.1: an ordinary fixed-power improvement from
`H Z^2` down toward `Z^2` is no longer sufficient at the transition.

There is no contradiction with the fixed-modulus Blomer--Pascadi theorem.
That theorem treats one `k` and is uniform in the interval endpoint.  The
new loss appears only when one tries to average many different `k` using a
single common `(P,Q)` coefficient frame.

## 2. Extraction of the exact packet phase

In the notation of R111 Section 3, a short box is

```text
I=[M]+s_1,                 J=[N]+s_2,
K_(m,n)=S(km,n;r).                                   (2.1)
```

Before the harmless Schwartz-tail truncation, the completion profiles are

```text
w_(1,k)(n)=Phihat(Mn/r)e_r(-s_1 k n),
w_2(n)=Phihat(Nn/r)e_r(-s_2 n).                      (2.2)
```

The factor `k` in the first endpoint phase is forced by the multiplier in
`S(km,n;r)`.  If

```text
R_w(h)=sum_(u-v=h)w(u)conjugate(w(v)),                (2.3)
```

then direct substitution into (2.2) gives

```text
R_(w_(1,k))(h)=e_r(-s_1kh)R_(w_(1,0))(h).            (2.4)
```

The normalization `4/H_1` in the BP definition of `z_i` is independent of
`k`, so (1.2) follows without an error term.  The common tail truncation
also preserves (2.4) exactly because the cutoff is imposed on the index,
not on `k`.

The fourth word uses two copies of the odd autocorrelation and two copies
of the even autocorrelation.  Removing the endpoint modulation from the
weights leaves a common product

```text
W_0(h)=product_(i=1)^4 z_i^0(h_i)                   (2.5)
```

and the full odd phase is precisely (1.3).  After multiplying the trace by
`k^2`, the ordinary quadratic-character contribution is

```text
chi_r(D_(P(h),Q(h))(k)).                              (2.6)
```

Thus a separated multiplier block has the exact form

```text
T=sum_(k in K)a_k sum_h W_0(h)
       e_r(-s_1k[h_1+h_3])chi_r(D_(P(h),Q(h))(k)).   (2.7)
```

Formula (2.7) concerns the ordinary noncentral character.  The special
`G=plusminus I` values must still be inserted using R112's central-word
classification; `D=0` alone is not a central condition.

In R81, the multiplier is the grouped integer `k=j theta`.  R105 proves
that this grouping is exact for the recombined Vaughan-tail coefficient.
Equation (2.7) applies once a genuine prime-modulus BP short box and a
separated `k`-weight have been produced.  It does not repair R105's prior
full-Fourier/modular-inverse support mismatch.

## 3. Exact twisted coefficient-pair frame

Let `mathcal K subset F_r^*`, let `mathcal X subset F_r`, and write
`B=#mathcal X`.  For `k in mathcal K` define a vector on
`F_r^2 times mathcal X` by

```text
V_k(P,Q,x)=e_r(-skx)chi_r(D_(P,Q)(k)).                (3.1)
```

### Theorem 3.1 (actual-profile twisted Gram matrix)

For `k,l in mathcal K`,

```text
<V_k,V_l>
 =B r(r-2),                            k=l,
 =sum_(x in mathcal X)e_r(-s(k-l)x),   k!=l.          (3.2)
```

Equivalently, if

```text
A_(k,l)=sum_(x in mathcal X)e_r(-s(k-l)x),            (3.3)
```

then

```text
G=B[r(r-2)-1]I+A.                                    (3.4)
```

If `s!=0`, then

```text
0<=A<=rI,
G<= {B[r(r-2)-1]+r}I.                               (3.5)
```

Therefore, for arbitrary coefficients `a_k`,

```text
sum_(P,Q,x in mathcal X)
 abs(sum_(k in mathcal K)a_k V_k(P,Q,x))^2

 =B[r(r-2)-1]sum_k abs(a_k)^2
   +sum_(x in mathcal X)abs(sum_k a_k e_r(-skx))^2

 <=[B(r(r-2)-1)+r]sum_k abs(a_k)^2.                 (3.6)
```

**Proof.**  R115 Theorem 7.1 gives

```text
sum_(P,Q)chi(D_(P,Q)(k))chi(D_(P,Q)(l))
 =r(r-2)  if k=l,
 =1       if k!=l.                                  (3.7)
```

Multiplication by the two endpoint phases and summation over `x` proves
(3.2)--(3.4).  For `s!=0`, the residues `sk`, `k in mathcal K`, are
distinct.  The matrix `A` is a principal compression of the unnormalized
Fourier projection onto the coordinates in `mathcal X`; hence it is
positive semidefinite and has operator norm at most `r`.  This proves
(3.5)--(3.6).  QED.

If `s=0`, one should not enlarge the coefficient space: (3.3) is
`B 1 1^*`, while the original R115 `(P,Q)` frame applies directly without
the factor `B`.  Thus the anchored interval is genuinely easier than a
generic translated interval.

### Theorem 3.2 (twisted `P=0` frame)

On `P=0`, put

```text
phi_k(Q)=chi_r(Q(Q-4k)),
W=diag(chi_r(k):k in mathcal K).                     (3.8)
```

The Gram matrix of

```text
(Q,x)|->e_r(-skx)phi_k(Q)                            (3.9)
```

is exactly

```text
G_0=rB I-A-WAW.                                      (3.10)
```

In particular,

```text
0<=G_0<=rB I.                                        (3.11)
```

**Proof.**  R115 (7.11) says that the `Q`-correlation is

```text
r delta_(k,l)-1-chi_r(k)chi_r(l).                    (3.12)
```

Multiplying by the `x`-correlation (3.3) gives (3.10).  Both `A` and
`WAW` are positive semidefinite, which proves (3.11).  QED.

Thus the exceptional coordinate axes retain their better `r`-dimensional
frame even after the actual endpoint phase is included.

## 4. Weighted application and the exact transition loss

Aggregate the common weights in (2.7) by

```text
C(P,Q,x)
 =sum_(h:P(h)=P,Q(h)=Q,h_1+h_3=x) W_0(h),

E_x=sum_(P,Q,x)abs(C(P,Q,x))^2,
Z^2=product_i norm(z_i^0)_2^2.                       (4.1)
```

Cauchy--Schwarz and Theorem 3.1 give

```text
abs(T)^2
 <=E_x [B(r(r-2)-1)+r]sum_k abs(a_k)^2.             (4.2)
```

Here `B` may be taken to be the number of possible values of
`h_1+h_3`.  If all four profiles have support `O(H)`, then `B<<H`.

There is an elementary enlarged-fiber bound.

### Lemma 4.1 (nonzero-`P` enlarged fiber)

Assume `r asymp H^2`, each `h_i` lies in an integer interval of length
`O(H)`, and those intervals inject into `F_r`.  For fixed `(P,Q,x)` with
`P!=0`,

```text
# {h:(P(h),Q(h),h_1+h_3)=(P,Q,x)} <<H^(1+epsilon).   (4.3)
```

Consequently

```text
E_x^(P!=0)<<H^(1+epsilon)Z^2.                        (4.4)
```

**Proof.**  If `x!=0`, the congruence

```text
x(h_2+h_4)=Q                                         (4.5)
```

fixes `y=h_2+h_4` up to `O(1)` integer lifts.  Choose `h_1` in `O(H)`
ways and put `h_3=x-h_1`.  Since `P!=0`, `h_1h_3` is a unit, and

```text
h_2(y-h_2)=P/(h_1h_3) mod r                          (4.6)
```

has at most two residue roots.  If `x=0`, then `Q=0`; after
`h_3=-h_1`, the remaining fixed-product equation is bounded by the
divisor estimate, giving the same `H^(1+epsilon)` total.  Fiberwise
Cauchy--Schwarz proves (4.4).  QED.

Combining (4.2) and (4.4), and suppressing epsilon powers, gives

```text
abs(T_(P!=0))<<r H norm(a)_2 Z.                      (4.7)
```

For `L` unit-size multiplier coefficients this is

```text
abs(T_(P!=0))<<r H sqrt(L)Z.                         (4.8)
```

The elementary separated-weight estimate is

```text
abs(T)<=L H^2 Z.                                     (4.9)
```

At `r=H^2`, (4.8)/(4.9) is `H/sqrt(L)`.  The universal enlarged-fiber
bound therefore does not save anywhere before the complete range
`L=H^2`, where it merely meets (4.9).

More revealingly, suppose the strongest ordinary collision estimate one
could reasonably request were available:

```text
E_x^(P!=0)<<H^epsilon Z^2.                           (4.10)
```

Then (4.2) would become

```text
abs(T_(P!=0))<<r sqrt(HL)Z.                          (4.11)
```

At `r=H^2`, the ratio of (4.11) to (4.9) is

```text
sqrt(H/L).                                           (4.12)
```

Thus the ideal enlarged-coordinate collision scale only starts saving for
`L>H`; at `L=H` it is exactly at the direct endpoint.  To obtain a fixed
power at `L=H` from (4.2) alone would require

```text
E_x<<H^(-delta)Z^2                                  (4.13)
```

for some `delta>0`, or a new estimate which avoids the Cauchy--Schwarz
factorization in (4.2).  R115 Target 8.1 asks for a fixed improvement over
`H Z^2` in the two-coordinate energy.  Once the real phase forces the
third coordinate, that target by itself no longer creates the desired
transition overlap.

### The axis contribution for the native flat packet

R112 proves, up to an arbitrary epsilon loss,

```text
norm(z_i^0)_infinity<<H^(-1/2+epsilon)norm(z_i^0)_2.
                                                               (4.14)
```

On an axis such as `h_1=0`, fixing `x=h_3` and `Q=h_3(h_2+h_4)` leaves
at most `O(H)` pairs `(h_2,h_4)`.  Fiberwise Cauchy--Schwarz and (4.14)
cancel this `H`.  The double intersection `h_1=h_3=0` is also harmless:

```text
abs[z_1(0)z_3(0)(sum z_2)(sum z_4)]^2<<H^epsilon Z^2.
                                                               (4.15)
```

The other three axes are identical after exchanging the two opposite
pairs.  Splitting their intersections gives

```text
E_x^(P=0)<<H^epsilon Z^2.                            (4.16)
```

Theorem 3.2 now yields

```text
abs(T_(P=0))<<sqrt(rHL)Z                             (4.17)
```

for `L` unit multiplier weights.  The direct native-axis bound is
`LH Z`.  At `r=H^2` their ratio is again `sqrt(H/L)`: the smaller axis
frame and packet flatness remove the algebraic axis loss, but the endpoint
modulation still lands exactly at `L=H`.

## 5. Uniform projective absorption is impossible

One might try to avoid the new `x` coordinate by separating
`e_r(-skx)` into a short projective sum in `k` and `x`.  The following
finite calculation rules this out uniformly in the interval endpoint.

For `1<=H<r`, let

```text
M_s(k,x)=e_r(skx),          1<=k,x<=H.               (5.1)
```

### Theorem 5.1 (endpoint modulation has linear approximate rank)

One has the exact fourth-Schatten average

```text
(1/r)sum_(s mod r)norm(M_s)_(S^4)^4=2H^3-H^2.        (5.2)
```

Consequently, for at least `r/2` endpoint residues `s`,

```text
norm(M_s)_(S^4)^4<=4H^3.                             (5.3)
```

For every such `s`, if a rank-`q` matrix `R` satisfies

```text
norm(M_s-R)_F<=epsilon norm(M_s)_F=epsilon H,         (5.4)
```

then

```text
q>=[(1-epsilon^2)^2/4]H.                             (5.5)
```

**Proof.**  Expanding the Schatten moment and averaging in `s` leaves the
congruence

```text
(k-l)(x-y)=0 mod r.                                  (5.6)
```

Because both intervals inject into `F_r` and `r` is prime, this means
`k=l` or `x=y`.  Inclusion--exclusion gives exactly
`H^3+H^3-H^2`, proving (5.2).  Markov's inequality gives (5.3).

Let `sigma_j` be the singular values of `M_s`.  If (5.4) holds, the
Eckart--Young theorem gives

```text
sum_(j<=q)sigma_j^2>=(1-epsilon^2)H^2.               (5.7)
```

On the other hand, Cauchy--Schwarz and (5.3) give

```text
sum_(j<=q)sigma_j^2
 <=sqrt(q)(sum_j sigma_j^4)^(1/2)
 <=2sqrt(q)H^(3/2).                                  (5.8)
```

Comparison proves (5.5).  QED.

Every sum of `q` separated products `f_n(k)g_n(x)` has matrix rank at most
`q`.  Hence Theorem 5.1 proves that for many admissible BP interval
endpoints, even fixed relative `l^2` accuracy costs `Omega(H)` separated
terms.  In particular, the `H^o(1)` projective-cost technology of R111
cannot absorb (1.3) uniformly.

Recentering a multiplier interval does not change this conclusion.  If
`k=k_0+k'`, the factor `e_r(-sk_0x)` can be absorbed into the common odd
profiles, but the residual matrix is `e_r(-sk'x)` and Theorem 5.1 applies
to the new interval.  This is an approximate-rank obstruction, not merely
the observation that the exact Vandermonde matrix has full algebraic rank.

## 6. Other attempted absorptions

Three algebraically valid rewrites do not improve the ledger.

1. **Move the multiplier to the even Kloosterman coordinate.**  The
   symmetry `S(km,n;r)=S(m,kn;r)` replaces `(s_1,x)` by
   `(s_2,y)`, where `y=h_2+h_4`.  It helps an individually anchored side,
   but the full R105 block partition has arbitrary offsets on both sides.

2. **Rescale the odd trace variables.**  Setting
   `u_i=inverse(k)h_i` removes the reciprocal coefficient from the group
   word, but changes the weight to `z_i^0(ku_i)` and changes the endpoint
   phase to a `k^2` modulation.  The short common support is thereby sent
   to a `k`-dependent dilate, so no common coefficient frame results.

3. **Complete the `x` coordinate.**  Summing (3.1) over every
   `x in F_r` makes distinct `k` columns exactly orthogonal.  Its diagonal
   is then `r^2(r-2)`, replacing the actual support factor `H` by `r` and
   worsening the critical bound by `sqrt(r/H)=sqrt(H)`.

The anchored case `s_1=0` is the one genuine exception.  Then the actual
profiles are common in `k`, and the original R115 `(P,Q)` frame may be
used without enlargement.  A proof for anchored intervals, however, does
not cover the full-Fourier and modular-inverse support blocks of R105.

## 7. Consequence and next falsifiable theorem

The actual-profile audit has the following rigorous ledger:

```text
exact odd-profile k modulation                 PROVED, (2.4)
twisted (P,Q,x) Gram matrix                    EXACT, (3.4)
twisted P=0 frame                              EXACT, (3.10)
native P=0 enlarged energy                     IDEAL SCALE, (4.16)
universal nonzero-P enlarged energy            H-LOSS, (4.4)
ideal enlarged energy at L=H                   DIRECT ENDPOINT
uniform subpower phase separation              FALSE, Theorem 5.1
central matrices                               SEPARATE / R112
full R105 short-box lift                        STILL ABSENT
fixed zeta zero-free strip                      NOT PROVED.           (7.1)
```

The remaining possible workaround must use information discarded by the
single-endpoint frame.  The narrowest candidate is a vector-valued theorem
which keeps the complete family of interval offsets, their actual R105
coefficients, and the multiplier sum together:

```text
sum_(s,k) b_s(k) sum_h W_s(h)e_r(-sk[h_1+h_3])
                    chi_r(D_h(k)).                   (7.2)
```

Orthogonality in `s` can in principle repay the rank in Theorem 5.1, but
only before a triangle inequality or a separate spectral norm is applied
to each short box.  In the exact full-tail language, this is the same
joint-correlation requirement isolated in R113: retain the full Fourier
coefficient and modular-inverse image coefficient inside one vector
Kloosterman/trace estimate rather than partitioning them into scalar BP
boxes.

Accordingly, further work on the two-coordinate collision target alone is
not sufficient.  The next useful theorem must either

```text
(a) prove a vector/square-function BP estimate across all endpoints, or
(b) estimate the unpartitioned R105 joint multiplier correlation directly.
                                                               (7.3)
```

Neither statement is proved here.  Failure of this particular frame
mechanism does not prove that a fixed zero-free strip is false.
