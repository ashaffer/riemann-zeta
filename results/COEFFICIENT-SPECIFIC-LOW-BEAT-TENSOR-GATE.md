# Coefficient-specific structure in the canonical low-beat prime tensor

Status: R84 exact global-frame theorem, common-dual separation lemma,
mask-free shift-product Wright interface, phase-alignment no-go, low-band
superoscillation audit, and finite diagnostics; 2026-08-07.  No fixed
zero-free strip is proved.

R83 predecessor:
[`GAUGE-QUOTIENT-SECTOR-RECOMPLETION-GATE.md`](GAUGE-QUOTIENT-SECTOR-RECOMPLETION-GATE.md).

R85 successor:
[`NATURAL-MEAN-AFFINE-FIXED-POWER-GATE.md`](NATURAL-MEAN-AFFINE-FIXED-POWER-GATE.md).
It corrects the informal word "centered" in R84 (5.4): the exact reciprocal
mean is `c_r(k)/(r-1)`, not one, and it resolves the affine-counterterm gate.

## 1. Verdict

The canonical tensor is much less generic than R83's first rank diagnostic
suggested.  Averaging the primitive beat frames over many square-root prime
pairs and taking one common dual gives

```text
gamma_(p,r,theta)=W(theta/(pr)).                        (1.1)
```

Thus its dependence on the three nominal tensor variables is through one
ratio.  Log-Mellin separation removes the generic `H^(1/4)` tensor-rank
loss.  On determinants `abs(theta)<=H^epsilon`, the projective cost is only

```text
H^((epsilon+delta)/2+o(1)),                            (1.2)
```

for an arbitrarily small truncation margin `delta>0`.  This can fit under
Wright's nominal `H^(-1/40)` gain when `epsilon+delta<1/20`.

The actual R81 kernel amplitude has the same favorable ratio structure.
In the original nonprimitive cofactor expansion, grouping the shift and
determinant as `k=j theta`, rather than applying a theorem separately for
every `j`, turns each signed dyadic completed-lattice bulk box into scalar
Wright forms with only a divisor-function collision loss.  The finite
primitive basis retains a common-`g` mask.  Subject to that distinction,
generic tensor rank and a power-sized shift triangle are not the obstruction.

The obstruction is the placement of the coefficient.  The canonical
coefficient (1.1) multiplies the slow additive beat

```text
e(j theta/(pr)),                                       (1.3)
```

whereas the native R81 coefficient `h_p conjugate(h_r)` multiplies

```text
e(j theta inverse(r)/p).                               (1.4)
```

Additive reciprocity aligns the amplitudes but not the coefficients.  The
exact difference contains

```text
h_p conjugate(h_r)-gamma_(p,r,theta),                  (1.5)
```

still attached to (1.3).  This residual retains the completed one-point
prime carrier.

Prescribing the native coefficients on all low determinants and repairing
the vector with high determinants is always possible algebraically.  It is
not a controlled escape: the high frame has exponentially small prolate
directions, and exact contact duality forces the high coefficients to repay
any Fourier-tail suppression.  A single contact can be moved cheaply if the
low coefficients are also allowed to change, but then native phase alignment
is lost.  Uniform control of the translated/dilated contact family remains
the fixed-strip-strength statement.

```text
generic dense tensor rank                         REMOVED
canonical common-dual ratio structure            THEOREM
mask-free R81 amplitude and k=j theta grouping     EXACT INTERFACE
canonical coefficient on reciprocal phase        FALSE
native low coefficient + high-beat repair         ONTO / ILL-CONDITIONED
axis-renormalized coefficient-aligned power       OPEN.               (1.6)
```

## 2. The global primitive frame has one common dual

Let `P` contain the primes in a fixed multiplicative window

```text
c_- sqrt(H)<=p<=c_+ sqrt(H),
sqrt(2)<c_-<c_+ fixed,                                 (2.1)
```

and use every ordered pair `p!=r`.  On an interval `I` of `H` consecutive
integers put

```text
(A_(p,r))_(n,theta)=e(theta n/(pr)),
theta in (Z/(pr)Z)^*.                                  (2.2)
```

Let

```text
(P_p)_(n,m)=1_(p divides n-m),       J_(n,m)=1.
```

Since `pr>H-1`, the pairwise Ramanujan Gramian is

```text
A_(p,r) A_(p,r)^*
 =pr I-p P_p-r P_r+J.                                  (2.3)
```

### Theorem 2.1 (global frame operator)

For `A` obtained by concatenating all the ordered-pair frames, one has

```text
S=AA^*
 =D I-2(K-1)sum_(p in P)pP_p+K(K-1)J,                 (2.4)

D=sum_(p!=r)pr=(sum_p p)^2-sum_p p^2.                 (2.5)
```

Moreover,

```text
lambda_min(S)
 >=D-2(K-1)sum_p p ceil(H/p),                         (2.6)

lambda_max(S)<=D+K(K-1)H.                             (2.7)
```

Consequently,

```text
K(K-1)(c_-^2-2+o(1))H I
 <=S<=K(K-1)(c_+^2+1+o(1))H I.                        (2.8)
```

#### Proof

Equation (2.3) is

```text
c_(pr)(n-m)
 =[p 1_(p divides n-m)-1][r 1_(r divides n-m)-1].     (2.9)
```

Summing (2.3) gives (2.4).  Each `P_p` is a positive
semidefinite block matrix with norm at most `ceil(H/p)`, while
`0<=J<=H I`.  Dropping the positive `J` for the lower bound and the negative
divisibility matrices for the upper bound proves (2.6)--(2.8).

For any vector `v` on `I`, define

```text
w=S^(-1)v,
gamma_(p,r,theta)=A_(p,r)^*w.                          (2.10)
```

Then

```text
v=A gamma,
sum_(p!=r,theta)abs(gamma_(p,r,theta))^2
 =v^*S^(-1)v,                                         (2.11)
```

and, crucially,

```text
gamma_(p,r,theta)
 =sum_(n in I)w_n e(-theta n/(pr))
 =W(theta/(pr)).                                      (2.12)
```

For a fixed multiplicative prime window, the prime number theorem gives
`K asymp sqrt(H)/log H`.  Applying (2.11) to
`v_n=Lambda(n)-1` and using the elementary second moment yields

```text
sum abs(gamma)^2<<log(H)/K^2<<log^3(H)/H.              (2.13)
```

The exact matrix identity, frame certificates, common-dual formula, energy
identity, and reconstruction are checked by
[`common_dual_prime_beat_probe.py`](../src/common_dual_prime_beat_probe.py).

## 3. The low tensor is Mellin-separable at small cost

Write `p=Q exp(u_p)`, `r=Q exp(u_r)`, where `Q asymp sqrt(H)`, and put
`s=u_p+u_r`.  Choose `chi` smooth and compactly supported, with `chi=1` on
the fixed compact log-product range, and set

```text
Phi_theta(s)
 =chi(s)W[(theta/Q^2)exp(-s)].                         (3.1)
```

Fourier inversion gives, exactly on the prime box,

```text
W(theta/(pr))
 =1/(2pi) integral Phihat_theta(t)
     (p/Q)^(it)(r/Q)^(it)dt.                          (3.2)
```

The `p` and `r` twists have unit modulus, so their `l2` norms are unchanged.
Equation (3.2), rather than a singular-value rank count, is the natural
coefficient interface for a trilinear theorem.

There is a quantitative finite version.  For

```text
0<abs(theta^flat)<=T=H^epsilon<min_(p in P)p,
R=T H^delta,                                           (3.3)
```

a smooth Fourier truncation in `s` gives

```text
gamma_(p,r,theta)
 =sum_(abs(ell)<=R)alpha_ell(p)beta_ell(r)nu_ell(theta)
   +E_(p,r,theta),                                    (3.4)

sup abs(E)<<_(B,delta)H^(-B)norm(w)_1.                 (3.5)
```

The remainder may be expanded entry by entry, so

```text
norm(E)_(pi,2)<=K^2 T sup abs(E).                      (3.5a)
```

Choosing `B` after `epsilon,delta` makes this negligible.

Parseval in `s` and the additive large sieve in `theta` give

```text
sum_(ell,theta)abs(nu_ell(theta))^2<<H norm(w)_2^2.
```

Therefore

```text
norm(gamma_(abs(theta)<=T))_(pi,2)
 <<K sqrt(RH)norm(w)_2
 <<sqrt(R)/(K sqrt(H)) norm(v)_2.                      (3.6)
```

For `v=Lambda-1`, this is

```text
norm(gamma_low)_(pi,2)
 <<sqrt(R)log^(3/2)(H)/sqrt(H).                        (3.7)
```

Relative to the common-dual Hilbert scale, the separation costs only
`sqrt(R)=H^((epsilon+delta)/2)`.  Thus the generic `H^(1/4)` loss in R83
does not apply to the canonical global tensor.  If (3.4) were attached to a
native reciprocal phase, Wright's balanced `1/40` saving would survive for

```text
epsilon+delta<1/20.                                   (3.8)
```

The hypothesis in the preceding sentence is the failed gate in Section 5.

## 4. A second positive result: the actual R81 amplitude separates

R81's exact completed off-axis amplitude is

```text
A_(g,m,n,theta)(j)
 =g integral L(u+gj,u)e(theta u/(gmn))du.              (4.1)
```

For a signed dyadic box `abs(j)asymp J`,
`abs(theta)asymp Theta`, define

```text
F_(g,j)^plusminus(y)
 =g integral L(u+gj,u)e(plusminus y u/g)du.            (4.2)
```

Then (4.1) is exactly

```text
F_(g,j)^(sign theta)(abs(theta)/(mn)).                 (4.3)
```

Choose a smooth `y` cutoff equal to one on the dyadic ratio box and Mellin
invert that localization of (4.2):

```text
F_(g,j)^plusminus(y)=integral c_(g,j)^plusminus(t)y^(it)dt.
```

Now group

```text
k=j theta,              abs(k)asymp K_0=J Theta,       (4.4)
```

and define

```text
nu_(g,t)(k)
 =abs(k)^(it)
   sum_(j divides k; j~J; k/j~Theta)
     c_(g,j)^(sign(k/j))(t)abs(j)^(-it).               (4.5)
```

### Proposition 4.1 (mask-free shift-product Wright interface)

For the original nonprimitive cofactor expansion, put

```text
h_q=c(q)/q.
```

After splitting `k>0` and `k<0`, and at most two product-dyadic intervals,
the whole box is exactly

```text
integral_R sum_((m,n)=1,k)
 [h_(gm)m^(-it)]
 [conjugate(h_(gn))n^(-it)]
 nu_(g,t)(k)e(k inverse(n)/m)dt.                       (4.6)
```

For each fixed `(g,t)` and sign, (4.6) is Wright's scalar trilinear form with
Wright variables `m_W=n`, `n_W=m`, numerator `a_W=abs(k)`, and fixed phase
`vartheta=sign(k)`.  No vector-valued extension is being assumed: apply the
scalar theorem first, then integrate its bound in `t`.  The original
cofactor expansion retains its conditional rectangular-limit bookkeeping.
For R82's finite primitive basis, `(theta,mn)=1` and the common-`g`
periodic mask produce fractional dual shifts; removing that mask is still an
open interface lemma.  The mask-free statement also excludes `j=0` and
`theta=0` throughout.

The factorization collisions cost only

```text
norm(nu_(g,t))_2^2
 <=K_0^o(1) Theta sum_(j~J)abs(c_(g,j)(t))^2.          (4.7)
```

What scalar Wright requires after integration is the projective ledger

```text
integral_R [sum_(j~J)abs(c_(g,j)(t))^2]^(1/2)dt.       (4.7a)
```

For every `s>1/2`, vector Mellin Plancherel and Cauchy--Schwarz give

```text
(4.7a)
 <<_s [sum_(j~J)norm(chi_y F_(g,j))_(H^s(dy/y))^2]^(1/2).  (4.7b)
```

The still-required uniform Fourier-tail/kernel lemma is

```text
integral norm(nu_(g,t))_2dt
 <<K_0^o(1)g sqrt(K_0)(1+Z)^(1/2) S_L,

Z=Theta Y/(gMN),             S_L=Y^o(1),               (4.8)
```

uniformly on the completed boxes.  Equation (4.8) does not follow from
Plancherel alone; it also needs nonstationary-phase tails and uniform control
of the B-spline seams.  An arbitrarily small truncation margin is absorbed
into `K_0^o(1)`.  Conditional on (4.8), the elementary
original-cofactor bound

```text
abs(h_(gm))<<log(Y)/(gm),
```

the coefficient ledger per `g` is

```text
<<log^2(Y)K_0^(1/2+o(1))(1+Z)^(1/2)S_L/[g sqrt(MN)].  (4.9)
```

The dyadic decompositions are logarithmic, but the `g` sum is only
logarithmic when `Z=O(1)`.  In general
`sum_g g^(-1)(1+C/g)^(1/2)<<log Y+sqrt(C)`, and the square-root bandwidth
cost must be charged.  The remaining analytic work is to prove
`S_L=Y^o(1)` uniformly through the actual B-spline seams, control its `g,j`
dependence, treat the primitive mask if that basis is used, and integrate by
parts in boxes with `Z>>1`.

For `Y asymp MN`, `M=N=H^(1/2)`, and `K_0=H^a`, Wright's weaker displayed
theorem alone gives

```text
s_W(a)=min(1/16,1/40+a/20)-(a-1)_+/4.                 (4.10a)
```

If `Theta=H^tau` and one additionally pays the crude square-root
determinant-band charge in (4.8), the conditional net becomes

```text
s_W(a)-tau/2.                                         (4.10)
```

Thus, in the mask-free interface and subject to the stated kernel ledger,
`K_0<=H^(1+o(1))` and `Theta=H^o(1)` preserve at least the nominal
`1/40-o(1)` saving.  This repairs the old claim that the shift sum must
automatically cost a power.  It does not repair the primitive mask,
conditional cofactor completion, or contact phase in Section 5.

The imported theorem is Theorem 2.1 of Wright's
[Trilinear Kloosterman fractions I](https://arxiv.org/abs/2604.25177),
current v1 on the audit date.  As in R81, only its weaker displayed statement
is used.

## 5. Exact reciprocity exposes the coefficient mismatch

Suppress `g` to display the issue.  After the same lattice completion, the
canonical beat contact and native reciprocal block have the aligned
amplitude

```text
A_(p,r,theta)(j)
 =integral L(u+j,u)e(theta u/(pr))du,                  (5.1)
```

but take the forms

```text
B=sum gamma_(p,r,theta)e(j theta/(pr))A_(p,r,theta)(j),

O=sum h_p conjugate(h_r)
      e(j theta inverse(r)/p)A_(p,r,theta)(j).          (5.2)
```

Additive reciprocity gives

```text
e(j theta inverse(r)/p)
 =e(j theta/(pr))e(-j theta inverse(p)/r).             (5.3)
```

Consequently,

```text
O-B
 =sum e(j theta/(pr))A_(p,r,theta)(j)
   {h_p conjugate(h_r)[e(-j theta inverse(p)/r)-1]
     +[h_p conjugate(h_r)-gamma_(p,r,theta)]}.         (5.4)
```

The first bracket is the hoped-for centered reciprocal difference and
vanishes on `j theta=0`.  The second bracket is unavoidable.  Moving the
canonical term to the reciprocal phase would insert
`e(j theta inverse(p)/r)` into its coefficient and destroy (1.1).

There is a blunt full-frame obstruction.  Every tensor `d_(p,r)` constant
over the full primitive `theta` set synthesizes

```text
u_d(n)=sum_(p!=r)d_(p,r)c_(pr)(n).                     (5.5)
```

On integers divisible by none of the bank primes, every `c_(pr)(n)=1`, so
`u_d` is constant.  On an interval `[H,2H]`, the prime-versus-composite
variance gives

```text
inf_C sum_(n in I; p does not divide n for every bank p)
 abs[Lambda(n)-1-C]^2>>H log H.                        (5.6)
```

Thus such a full primitive native tensor cannot approximate the prime vector
in synthesis norm by a power.  Since only low determinants meet a smooth
contact strongly, Section 6 separately audits the possible high-determinant
escape.

## 6. Prescribing the low coefficients creates a prolate trap

Let `A_low` contain the symmetric residues

```text
0<abs(theta^flat)<=T
```

and let `A_high` contain the remaining primitive columns.  Prescribe

```text
d_(p,r,theta)=h_p conjugate(h_r)                       (6.1)
```

on the low band and put

```text
b=v-A_low d.                                          (6.2)
```

If `pr asymp 4H` and `T=o(H)`, even one pair has more than `H` high primitive
residues.  Any `H` distinct Fourier roots form an invertible
consecutive-row Vandermonde matrix.  Hence an exact repair always exists,
and its minimum-Hilbert-norm form is

```text
gamma_high=A_high^*(A_high A_high^*)^(-1)b.            (6.3)
```

This algebraic freedom is badly conditioned.  Take

```text
b_N=N^(-1)1_(0<=n<N),
f=b_N^(star L),           N asymp H/T,  L asymp T,      (6.4)
```

translated into `I`.  Then

```text
fhat(xi)=e(*)[sin(pi N xi)/(N sin(pi xi))]^L.          (6.5)
```

Every high beat has circular distance at least `T/(C^2H)` from zero, so

```text
abs(fhat(theta/(pr)))<=exp(-c_C T).                    (6.6)
```

The Rayleigh quotient therefore gives

```text
lambda_min(A_high A_high^*)
 <<K^2 H^2 exp(-2c_C T).                              (6.7)
```

The full-frame scale is `K^2H`.  Once `T/log H` tends to infinity, a uniform
polynomial inverse ledger is impossible in the worst directions.  This is the familiar
discrete-prolate transition; see Slepian's
[discrete uncertainty paper](https://doi.org/10.1002/j.1538-7305.1978.tb02104.x)
and Moitra's
[sharp Vandermonde-conditioning threshold](https://arxiv.org/abs/1408.1681).
Here (6.4)--(6.7) give the needed project-specific witness directly.

There is also an exact contact version which does not rely on a worst-case
singular vector.  If a null modification has prescribed low part `z_low`,
then

```text
A_high z_high=-A_low z_low.                            (6.8)
```

For every sampled contact weight `G`, taking the inner product with `G`
gives

```text
<z_high,A_high^*G>=-<z_low,A_low^*G>,                 (6.9)

norm(z_high)_2
 >=abs(<z_low,A_low^*G>)/norm(A_high^*G)_2.            (6.10)
```

For `G(n)=g(n/H)`, `g` smooth and compactly supported,

```text
norm(A_high^*G)_2<<_B K H T^(1/2-B).                  (6.11)
```

Thus Fourier suppression in the high band forces reciprocal coefficient
growth unless the prescribed low mismatch is already small against the
contact family.  That latter assertion is exactly the missing centered-axis
estimate.

For the raw prime-cofactor weight `h_p=log(p)/p` on a fixed multiplicative
prime bank, this mismatch is visibly full-scale for a positive smooth
contact.  Assume `supp(G)` lies in `(0,pr)` for every bank pair, as it does
for a suitable `[H,C_0H]` shell with the constant in (2.1) chosen large
enough.  Then

```text
sum_n G(n)c_(pr)(n)
 =pr sum_l G(prl)-p sum_l G(pl)-r sum_l G(rl)+sum_n G(n)
 =-integral G+o(H),                                   (6.12)
```

because the first sum vanishes under this support condition.

Moreover,

```text
sum_(p!=r)h_p h_r ->log^2(c_+/c_-)>0.                 (6.13)
```

The native packet therefore has a nonzero order-`H` full contact.  Repeated
summation by parts gives its high-determinant tail

```text
<<_B H T^(1-B)(sum_p abs(h_p))^2=o(H).                 (6.14)
```

The canonical `Lambda-1` full contact is `o(H)` by the PNT.  From (2.13) and
(6.11), its high tail is

```text
<<_B H log^(1/2)(H)T^(1/2-B)=o(H)                     (6.15)
```

after letting `T` grow sufficiently.  Equations (6.12)--(6.15) show that the
**low** native-minus-canonical mismatch is order `H`.  Matching (6.1)
therefore forces the compensating high packet to retain the missing contact.
For the finite R81 coefficients
instead of `log(p)/p`, the unconditional statement is (6.9)--(6.10); the
positivity in (6.13) must not be assumed.

This does not say that every individual contact is an expensive gauge
constraint.  If the low coefficients may vary, one scalar contact can be
zeroed at bounded finite cost.  But then (6.1) and the reciprocal-phase
alignment are gone.  The invariant target is a translated/dilated family or
its square function, not one adaptively selected pairing.

## 7. Finite fail-fast diagnostics

Three distinct finite experiments were kept separate.

First, independent low beats from all unordered prime pairs in
`[sqrt(H)/2,sqrt(H)]` were used to reconstruct a constant contact envelope.
At `H=10000`, `theta=1,...,4` in the real centered-cosine convention, the
minimum-`l2` tensor gave

```text
RMS error                 0.0015006
coefficient l1            41.4085
coefficient l2             4.6844
prime unfolding rank      10 of 10
output-aware rank          10 of 10
fixed-pair RMS error        0.9480.                    (7.1)
```

The rank grows, but its nuclear/projective proxies do not.  Over
`H=10000,...,10^6`, the output-aware ranks were

```text
10, 21, 32, 61, 73,
```

while the corresponding prime-unfold nuclear norms were

```text
7.91, 3.05, 2.57, 1.60, 1.27.                         (7.2)
```

This different finite model is qualitatively consistent with the distinction
in Section 3: counting separated terms can pay a power even when
separation-norm proxies remain bounded.  It is not a finite realization of
the exact `Lambda-1` common-dual frame.

Second, an adaptive-grid minimum-`l1` representative at `H=10000` achieved
4097-point holdout error `0.025013<251/H` using 16 beats, cosine-amplitude
`l1=21.25`, and the crude CP-rank bound 32.  This is evidence for
redundancy, not a certified continuum optimum or an arithmetic coefficient
theorem.

Third, impose equal amplitudes across the four centered-cosine theta columns
for each pair.  This is a surrogate for theta-independent native complex
weights: recentering the cosine basis inserts a theta-dependent complex
phase.  At `H=4096`, the adaptive LP reconstructing the constant envelope
within ten percent returned

```text
theta profile       parameter l1       expanded beat l1
constant             4.026e8             1.610e9
affine                 10.15                30.31.      (7.3)
```

The affine basis is `1,z_theta` with
`z_theta=(-1,-1/3,1/3,1)`, so its parameter norm is basis-dependent; the
expanded amplitude norm is the safer comparison.  The equal-profile LP was
severely ill-conditioned, while a two-moment surrogate escaped.  No continuum
dual certificate is claimed.

In a separate exact `H=128` synthetic constant-target frame, the
minimum-norm tied-low plus free-high gauge reconstructed to `2e-14` but
retained high contact `0.2263` against total contact `0.3838`.  Allowing its
low packet to adapt could zero that one contact with total coefficient norm
rising only from `0.570` to `0.820`; fitting the whole target instead is
ill-conditioned.  This is not the canonical `Lambda-1` common dual or a
native R81 coefficient computation.  It illustrates the distinction made
after (6.13).

The envelope/tensor experiment is reproduced by
[`global_prime_beat_frame_probe.py`](../src/global_prime_beat_frame_probe.py),
and the tied-profile/high-completion audit by
[`low_theta_native_gauge_probe.py`](../src/low_theta_native_gauge_probe.py).
They are mechanism falsifiers, not zeta computations.

## 8. What this means for the fixed-strip program

R84 removes two reasons for pessimism:

1. the canonical low-beat tensor is not generically dense in the norm that
   matters; and
2. in the mask-free cofactor bulk, the R81 shift index can be absorbed into
   Wright's numerator sequence by `k=j theta`, without a power-sized
   triangle inequality.

It also identifies the sharper obstruction.  A separable coefficient is
useful only when it is attached to the reciprocal phase.  Here the good
canonical coefficient is attached to the slow additive phase, and the good
reciprocal phase carries a different coefficient.  Frame gauge can exchange
those placements only through a high-frequency packet whose contact and norm
repay the exchange.

The next theorem should therefore not be another tensor-rank lemma.  It must
be a **coefficient-aligned, axis-renormalized reciprocal estimate** for the
whole bracket in (5.4), with the contact family inside the estimate before
absolute values.  One fixed power for that bracket still yields the desired
fixed zero-free strip.

There is one concrete off-wall subproblem worth testing before returning to
the full theorem.  The centered-cosine surrogate in (7.3) says that a
constant-plus-linear theta profile can be well conditioned even though its
equal-profile version is not.  The honest next gate is:

```text
derive, from the exact completed lattice rather than by insertion,
a two-moment theta counterterm whose constant part is native and whose
linear part is an integration-by-parts derivative of the same R81 kernel;
then test whether both pieces remain Wright-admissible with projective
mass H^o(1).                                            (8.1)
```

If no exact recompletion produces that affine term, the numerical escape is
coordinate fiction and should be closed.  If it does, (8.1) is the first
mechanism found here that attacks the phase/coefficient interface rather
than merely relocating the carrier.

### R85 successor disposition

R85 finds both exact affine identities and closes this fork.  Ordinary
integration by parts transfers the mismatch to a reciprocal derivative term,
but its projection onto the true Ramanujan mean remains
`mu_r(k)h_p conjugate(h_r)-gamma`; eliminating that projection costs
`1/abs(mu_r(k))asymp sqrt(H)`.  R82's top-prime null cloud gives a second
exact affine term, but it costs `Y/T` on the low determinant band.  At
square-root moduli its null defect is injectively the original near-square
Type-II tensor.  See
[`NATURAL-MEAN-AFFINE-FIXED-POWER-GATE.md`](NATURAL-MEAN-AFFINE-FIXED-POWER-GATE.md).
