# R115 reciprocal-discriminant `k`-sum gate

Status: unconditional finite-field classification, exact complete sums,
uniform complete mixed-twist and interval-completion bounds, and an exact
coefficient-pair frame identity.  The discriminant is never a nonzero square
as a polynomial in `k`; the only identically zero case is `P=Q=0`.  This
removes the polynomial-square obstruction but does **not** import a Burgess
bound for the resulting generic cubic character sequence.  A new exact
near-orthogonality in the two coefficients `(P,Q)` survives and is the best
remaining route.  Its application to the actual R71 packet requires a joint
Vieta-product collision estimate with the real `k`-dependent completion
profiles.  That estimate is not proved here.

Consequently this report proves neither a fixed zero-free strip nor the
nonexistence of one.  It kills the proposed pointwise nonlinear-Burgess
shortcut and replaces it by a sharper, explicitly testable joint-energy
theorem.

Date: 2026-08-07.

Predecessors:

* [`R110-TRACE-COLLISION-POWER-SAVING-THEOREM.md`](R110-TRACE-COLLISION-POWER-SAVING-THEOREM.md),
  for the weighted fixed-coefficient trace energy;
* [`R111-SEPARATED-OUTER-TRACE-LARGE-SIEVE-COROLLARY.md`](R111-SEPARATED-OUTER-TRACE-LARGE-SIEVE-COROLLARY.md),
  for reciprocal normalization and the fixed-`k` outer-prime ledger; and
* [`R112-CENTRAL-MATRIX-CORRECTION-BOUND.md`](R112-CENTRAL-MATRIX-CORRECTION-BOUND.md),
  for the distinction between trace `plusminus2` and the actual central
  matrices `plusminus I`; and
* [`R113-R105-MULTIPLIER-AVERAGE-FAIL-FAST-AUDIT.md`](R113-R105-MULTIPLIER-AVERAGE-FAIL-FAST-AUDIT.md)
  and
  [`R114-NUMERATOR-COMPLETION-AND-TRANSITION-GATE.md`](R114-NUMERATOR-COMPLETION-AND-TRANSITION-GATE.md),
  for the exact positive-multiplier average and the full-R105 transition
  normalization.

## 1. Verdict

Let `r` be an odd prime, let `chi` be its quadratic character extended by
`chi(0)=0`, and put

```text
P=h_1h_2h_3h_4,
Q=(h_1+h_3)(h_2+h_4).                                (1.1)
```

R111's reciprocal-normalized trace is

```text
U_k=P-kQ+2k^2,

U_k^2-4k^4
 =(P-kQ)(P-kQ+4k^2)=:D_(P,Q)(k).                    (1.2)
```

There are five exact conclusions.

1. In `F_r[k]`, `D_(P,Q)` is never a nonzero square.  It is identically
   zero exactly when `P=Q=0`.

2. All complete `k`-sums are explicit on the degenerate strata and satisfy
   the elliptic Weil bound in the generic case.  Every additive twist is
   `O(sqrt(r))`; completion therefore gives only

   ```text
   sum_(k in I) chi(D_(P,Q)(k)) << sqrt(r) log r.     (1.3)
   ```

3. Classical Burgess applies only when the squarefree part becomes linear,
   notably `P=0` or `P,Q!=0` with `Q^2=16P`.  There is no standard Burgess
   theorem at the `r^(1/4)` threshold for a general sequence
   `chi(f(k))` with nonlinear `f`.  Applying the ordinary Dirichlet-character
   Burgess bound to the generic cubic in (1.2) would be an error.

4. There is nevertheless a new exact cancellation mechanism.  For distinct
   nonzero `k,l`,

   ```text
   sum_(P,Q in F_r)
      chi(D_(P,Q)(k))chi(D_(P,Q)(l))=1,              (1.4)
   ```

   while the diagonal is `r(r-2)`.  Thus the `k`-columns form an exact
   near-orthogonal frame over coefficient space.  This bypasses pointwise
   nonlinear Burgess entirely.

5. The frame is useful only if the actual pushforward

   ```text
   h |-> (P(h),Q(h))                                  (1.5)
   ```

   has sufficiently small weighted collision energy.  The ideal
   arbitrary-weight bound is false on the full box: a coordinate axis
   forces a factor `H` at `r asymp H^2`.  Native completion profiles have
   point-evaluation flatness, and the `P=0` stratum has its own smaller
   exact frame, so this counterexample does not kill the actual-profile
   route.  It does kill a coefficient-uniform black-box theorem.

The clean next target is therefore not “prove Burgess for a cubic.”  It is
the profile-specific, axis-separated joint Vieta-product energy stated in
Section 8.

## 2. Polynomial-square classification

Expanding (1.2) gives

```text
D_(P,Q)(k)
 =P^2-2PQk+(Q^2+4P)k^2-4Qk^3.                       (2.1)
```

**Theorem 2.1 (complete square classification).**  For every odd prime
`r` and every `P,Q in F_r`, exactly one of the following holds:

```text
P=Q=0:       D_(P,Q)=0;
otherwise:   D_(P,Q) is not a square in F_r[k].       (2.2)
```

**Proof.**  If `Q!=0`, (2.1) has degree three and leading coefficient
`-4Q!=0`.  A nonzero polynomial square has even degree.

If `Q=0`, then

```text
D_(P,0)(k)=P^2+4Pk^2.                                (2.3)
```

For `P!=0`, a square of degree two would be `(ak+b)^2`.  Its zero linear
coefficient gives `2ab=0`.  Since the characteristic is odd, either its
leading coefficient or its constant coefficient would then vanish,
contrary to (2.3).  Finally `P=Q=0` gives the zero polynomial.  QED.

The proof is coefficient-uniform and includes primes at which the cubic
has repeated roots.  It says more than a pointwise nonsquare statement: no
nonzero principal Kummer sheaf occurs anywhere in this two-parameter
family.

## 3. Roots, exceptional strata, and exact complete sums

Write

```text
L(k)=P-Qk,
R(k)=P-Qk+4k^2.                                     (3.1)
```

If `P,Q!=0`, the root of `L` is not a root of `R`, since at `k=P/Q`
the second polynomial differs by `4(P/Q)^2!=0`.  The discriminant of `R`
is

```text
disc(R)=Q^2-16P.                                     (3.2)
```

Thus `D` is a squarefree cubic exactly when

```text
P Q (Q^2-16P) !=0.                                  (3.3)
```

The complete sums can be evaluated on every complementary stratum.

**Theorem 3.1 (complete `k`-sum table).**  Put

```text
S(P,Q)=sum_(k in F_r)chi(D_(P,Q)(k)).                 (3.4)
```

Then

```text
P=Q=0:                         S(P,Q)=0;
P=0, Q!=0:                     S(P,Q)=-1;
P!=0, Q=0:                     S(P,Q)=-chi(P);
P Q!=0, Q^2=16P:               S(P,Q)=-chi(-P);
P Q(Q^2-16P)!=0:               abs(S(P,Q))<=2sqrt(r).
                                                               (3.5)
```

**Proof.**  If `P=0,Q!=0`, then

```text
D_(0,Q)(k)=-Qk^2(4k-Q).                              (3.6)
```

Away from `k=0`, its character is the character of the displayed linear
factor times `chi(-Q)`.  The complete linear sum is zero, and its value at
the deleted point is one, giving `-1`.

If `Q=0,P!=0`, use the standard quadratic identity

```text
sum_k chi(ak^2+b)=-chi(a),       ab!=0,               (3.7)
```

and multiply by `chi(P)`.

If `P,Q!=0` and `Q^2=16P`, then

```text
R(k)=4(k-Q/8)^2.                                     (3.8)
```

Deleting its double root from the complete linear sum in `L` gives
`-chi(-P)`.  Under (3.3), `y^2=D(k)` is a nonsingular genus-one curve, and
Hasse--Weil gives the final line.  QED.

The complete mean is therefore never large.  This fact alone does not
control a short interval at the critical length.

### 3.1. Size of the algebraic exceptional sets in the small box

Suppose `h_i in [-H,H]`, `2H<r`.  Then

```text
# {h:P=0}                         <<H^3,
# {h:Q=0}                         <<H^3,
# {h:P=Q=0}                       <<H^2,
# {h:Q^2=16P}                     <<H^3.              (3.9)
```

The first three estimates follow because `P=0` forces a zero coordinate
and `Q=0` forces `h_1=-h_3` or `h_2=-h_4`.  For the last, fix
`h_1,h_2,h_3`; the equation is quadratic in `h_4`.  If its leading
coefficient vanishes, then `h_1+h_3=0`, and the remaining equation is a
union of `O(H^2)` zero-coordinate strata.  Otherwise there are at most two
residue roots and, because `2H<r`, at most two integer representatives.

Hence the linearizable cases are lower-dimensional.  They are useful for
disposing of exceptional pieces, but they do not represent the generic
four-variable mass.

## 4. Mixed complete sums and what completion really proves

For `a in F_r`, put

```text
S_a(P,Q)=sum_(k in F_r)
 chi(D_(P,Q)(k)) e_r(ak).                            (4.1)
```

**Theorem 4.1 (uniform mixed Weil bound).**  If `(P,Q)!=(0,0)`, then

```text
abs(S_a(P,Q)) << sqrt(r)                             (4.2)
```

uniformly in `P,Q,a` and `r`; the implied constant is absolute.  If
`P=Q=0`, the sum is zero.

**Proof.**  On the squarefree locus this is the standard Weil--Deligne
bound for the tensor product of the quadratic Kummer sheaf pulled back by
`D` and the Artin--Schreier sheaf `e_r(ak)`.  The conductor is bounded by
an absolute constant because `deg(D)<=3`.  The tensor product is not
geometrically trivial: `D` has a root of odd multiplicity.  On each
repeated-root stratum, remove the square factor as in (3.6) or (3.8); this
reduces (4.1), up to `O(1)` missing values, to a linear Gauss sum or to the
same bounded-degree mixed Weil estimate.  The case `a=0` is also covered
directly by Theorem 3.1.  QED.

This standard mixed estimate is recorded explicitly, for example, in the
finite-field form used in Section 3.4 of Tao's
[*The Hardy--Littlewood--Chowla conjecture in the presence of a Siegel
zero*](https://doi.org/10.1112/jlms.12663).

Fourier completion now gives the honest interval theorem.

**Corollary 4.2 (Pólya--Vinogradov scale).**  For every interval
`I subset F_r`, every nonzero dilation `theta`, and `(P,Q)!=(0,0)`,

```text
abs(sum_(k in I)chi(D_(P,Q)(k)))
  <<min{abs(I),sqrt(r)log r},                         (4.3)

abs(sum_(j in I)chi(D_(P,Q)(theta j)))
  <<min{abs(I),sqrt(r)log r}.                         (4.4)
```

Indeed, the `l^1` norm of the Fourier transform of an interval is
`O(r log r)`, and (4.2) is inserted with the `1/r` inversion factor.

The estimate has a fixed relative power only when the interval length is
larger than `r^(1/2)` by a fixed power.  It gives no power at length
`r^(1/4)` and only the direct scale at length `r^(1/2)`.

The same theorem handles a completion phase pulled out of an actual odd
Blomer--Pascadi autocorrelation: for fixed `h`,

```text
sum_(k mod r)e_r(k L(h))chi(D_(P(h),Q(h))(k))
 <<sqrt(r),                                          (4.5)
```

unless `P=Q=0`, when the summand vanishes.  Formula (4.5) is a complete
`k`-sum statement.  An incomplete interval still pays (4.3).

## 5. The Burgess applicability audit

For an ordinary nonprincipal Dirichlet character, Burgess gives, for every
integer `nu>=1`,

```text
sum_(n in I)chi(an+b)
 <<_(nu,epsilon)
 abs(I)^(1-1/nu) r^((nu+1)/(4nu^2)+epsilon),          (5.1)
```

uniformly for `a!=0`.  It is power-saving once
`abs(I)>r^(1/4+epsilon)`.

There are two places where (5.1) legitimately enters the present family.

### 5.1. Squarefree-part-linear strata

If `P=0,Q!=0` and `k!=0`, then exactly

```text
chi(D_(0,Q)(k))=chi(-Q)chi(4k-Q).                    (5.2)
```

If `P,Q!=0` and `Q^2=16P`, then the sequence differs at only one point
from

```text
chi(P-Qk).                                           (5.3)
```

Thus (5.1) applies to (5.2)--(5.3), including after fixing one nonzero
factor in `k=j theta` and summing over the other factor.

### 5.2. What Burgess does not say

For `Q=0,P!=0`, the squarefree part is a genuine quadratic.  On the generic
locus it is a squarefree cubic.  The classical Burgess proof for
`chi(n)` or `chi(an+b)` does not automatically extend to either sequence.

Mei-Chu Chang's survey
[*Character Sums in Finite Fields*](https://math.ucr.edu/~mcc/paper/DubProc.pdf),
Section 3, states the distinction explicitly: Weil plus completion gives
`O_f(sqrt(r)log r)` for `chi(f(n))`, while no general analogue of the
Burgess inequality is available there.  The weaker polynomial theorem of
Burgess applies when the polynomial splits into rational linear factors,
but gives only

```text
abs(sum_(n in I)chi(f(n)))
 <abs(I)-c abs(I)^2/sqrt(r),                          (5.4)
```

in its stated range.  At the fourth-root scale this proves variation, not
a fixed multiplicative saving.  The original references are Burgess,
[*On Dirichlet Characters of Polynomials*](https://doi.org/10.1112/plms/s3-13.1.537)
and
[*On the Quadratic Character of a Polynomial*](https://doi.org/10.1112/jlms/s1-42.1.73).

Recent multidimensional theorems do not fill this precise gap:

* Pierce--Xu,
  [*Burgess bounds for short character sums evaluated at forms*](https://arxiv.org/abs/1907.03108),
  treats admissible homogeneous forms in boxes.  In dimension two its
  generic side-length threshold is `r^(1/3+epsilon)`, and (1.2) composed
  with `k=j theta` is an affine polynomial in the product, not an
  admissible homogeneous binary form supplied by that theorem.
* Fouvry--Kowalski--Michel--Sawin,
  [*Bilinear forms with trace functions*](https://arxiv.org/abs/2511.09459),
  v3, gives Type-II cancellation for gallant rank-at-least-two sheaves when
  `MN>=r^(3/4+delta)`.  The native function `chi(D(k))` is a rank-one
  Kummer pullback with finite abelian monodromy, so it is not gallant; the
  critical product here is only about `r^(1/2)` in any event.

This is an applicability statement, not an exhaustive theorem that no
future nonlinear Burgess estimate can exist.  It is enough to reject the
proposed import at the present gate.

## 6. Complete multiplicative diagonalization

There is a second standard complete estimate.  Put

```text
K_(P,Q)(x)=chi(D_(P,Q)(x)),       x in F_r^*.         (6.1)
```

For every multiplicative character `eta` of `F_r^*`,

```text
sum_(x in F_r^*)K_(P,Q)(x)eta(x) <<sqrt(r)            (6.2)
```

when `(P,Q)!=(0,0)`.  To see this, tensor the Kummer sheaf in Theorem 4.1
with the Kummer sheaf for `eta(x)`.  The latter is ramified only at zero and
infinity, while the former has quadratic local monodromy at some nonzero
odd-multiplicity root of `D`; hence the tensor product cannot be
geometrically trivial.  Its conductor is uniformly bounded.

Mellin inversion and Cauchy--Schwarz give the following coefficient-uniform
bilinear estimate.

**Theorem 6.1 (complete Mellin bilinear bound).**  If the supports of
`alpha` and `beta` inject into `F_r^*`, then

```text
abs(sum_(j,theta)alpha_j beta_theta
       K_(P,Q)(j theta))
 <<sqrt(r) norm(alpha)_2 norm(beta)_2.                (6.3)
```

For unit weights on intervals of lengths `J,Theta`, this is

```text
<<sqrt(r J Theta).                                   (6.4)
```

It improves the direct bound `J Theta` only when `J Theta>r`.  At the
critical product `J Theta<=r^(1/2)`, it is much worse.  Thus complete
Mellin diagonalization is rigorous but does not close the high box.

## 7. The new exact coefficient-pair frame

Pointwise short-sum estimates miss an exact two-parameter orthogonality.
For `k in F_r^*`, define the vector

```text
v_k(P,Q)=chi(D_(P,Q)(k)),       (P,Q) in F_r^2.       (7.1)
```

**Theorem 7.1 (exact `(P,Q)` Gram matrix).**  For nonzero `k,l`,

```text
sum_(P,Q)v_k(P,Q)v_l(P,Q)
 ={r(r-2),  k=l;
   1,       k!=l.}                                   (7.2)
```

Consequently, for every set `mathcal K subset F_r^*` of distinct residues
and complex coefficients `a_k`,

```text
sum_(P,Q)abs(sum_(k in mathcal K)a_k v_k(P,Q))^2
 =[r(r-2)-1]sum_k abs(a_k)^2
   +abs(sum_k a_k)^2.                                (7.3)
```

**Proof.**  On the diagonal, set `A=P-kQ`.  For each `A` there are `r`
choices of `Q`, and `v_k^2` is one except at
`A=0,-4k^2`.  This gives `r(r-2)`.

For `k!=l`, the linear change of variables

```text
A=P-kQ,             B=P-lQ                           (7.4)
```

is invertible.  Therefore the correlation factors as

```text
[sum_A chi(A(A+4k^2))]
[sum_B chi(B(B+4l^2))]=(-1)(-1)=1.                  (7.5)
```

Expanding the square now proves (7.3).  QED.

This identity is stronger than a square-root estimate: all off-diagonal
correlations are evaluated exactly.

For separated weights `z_i`, aggregate

```text
C_r(P,Q)
 =sum_(h:P(h)=P,Q(h)=Q mod r) product_i z_i(h_i),

E_(P,Q)(z)=sum_(P,Q)abs(C_r(P,Q))^2.                 (7.6)
```

Cauchy--Schwarz and (7.3) prove the interface theorem

```text
abs(sum_(k in mathcal K)a_k
     sum_h product_i z_i(h_i)chi(D_h(k)))^2
 <=E_(P,Q)(z)
   {[r(r-2)-1]sum_k abs(a_k)^2+abs(sum_k a_k)^2}.
                                                               (7.7)
```

No interval structure is needed.  If `k=j theta` with integer products
smaller than `r`, one first sets

```text
a_k=sum_(j theta=k)alpha_j beta_theta.                (7.8)
```

The divisor bound gives

```text
sum_k abs(a_k)^2
 <<H^epsilon norm(alpha)_2^2 norm(beta)_2^2           (7.9)
```

on polynomial-height dyadic boxes.  Thus the factorization of `k` costs
only a divisor loss at this exact frame stage.

### 7.1. The `P=0` frame

The coordinate-axis stratum has an even smaller coefficient space.  For
`k!=0`, put

```text
phi_k(Q)=chi(Q(Q-4k)).                                (7.10)
```

Then

```text
sum_Q phi_k(Q)^2=r-2,

sum_Q phi_k(Q)phi_l(Q)=-1-chi(kl),       k!=l.        (7.11)
```

Indeed, after removing the common square `Q^2`, the complete quadratic
correlation is `-1`; at `Q=0` one must subtract `chi(kl)`.  If
`w_k=chi(k)`, the Gram matrix is exactly

```text
r I-1 1^*-w w^*.                                    (7.12)
```

It is positive semidefinite and has operator norm at most `r`.  Therefore

```text
sum_Q abs(sum_k a_k phi_k(Q))^2
 =r sum_k abs(a_k)^2
   -abs(sum_k a_k)^2
   -abs(sum_k a_k chi(k))^2
 <=r sum_k abs(a_k)^2.                               (7.13)
```

This exact identity is preferable to treating all coordinate axes by a
generic cubic estimate.

## 8. The joint-energy obstruction and the sharpened next theorem

The ideal coefficient-uniform estimate

```text
E_(P,Q)(z) <<H^epsilon product_i norm(z_i)_2^2        (8.1)
```

is false on the full box at `r asymp H^2`.

Take

```text
z_1=delta_0,
z_2=z_3=z_4=1_[1,H].                                 (8.2)
```

Then `P=0`, while

```text
Q=h_3(h_2+h_4).                                      (8.3)
```

There are `H^3` triples distributed among at most `r` residues.  Hence
Cauchy's inequality gives

```text
E_(P,Q)(z)>=H^6/r asymp H^4,                         (8.4)

product_i norm(z_i)_2^2=H^3.                        (8.5)
```

A factor `H` is unavoidable for arbitrary weights.  This is a genuine
counterexample, not a loss in the proof of the frame theorem.

There is also a simple universal fiber bound away from `P=0`.  At
`r asymp H^2` and `2H<r`, fix `(P,Q)` with `P!=0`.  The integer
`q=(h_1+h_3)(h_2+h_4)` has only `O(1)` lifts of `Q` in its natural range.
If `q!=0`, factor it as `q=xy` in `H^epsilon` ways, choose `h_1`, put
`h_3=x-h_1`, and then solve

```text
h_2(y-h_2)=P/(h_1h_3) mod r.                         (8.6)
```

There are at most two residue roots.  If `q=0`, split `x=0` or `y=0` and
use the divisor bound on the remaining product.  Thus every nonzero-`P`
fiber has size

```text
<<H^(1+epsilon),                                     (8.7)
```

and fiberwise Cauchy yields

```text
E_(P,Q)^(P!=0)(z)
 <<H^(1+epsilon)product_i norm(z_i)_2^2.             (8.8)
```

At the inherited R111 normalization `r=H^2`, a dyadic `k`-block of `L`
distinct residues, and unit-size `a_k`, (7.7)--(8.8) give

```text
abs(S_block)
 <<H^epsilon r sqrt(LH) product_i norm(z_i)_2.       (8.9)
```

The direct separated-weight bound is

```text
abs(S_block)
 <<L H^2 product_i norm(z_i)_2.                      (8.10)
```

For `L=H=sqrt(r)`, (8.9) and (8.10) are the same size.  The elementary
fiber theorem therefore lands exactly at the high-box endpoint; it does
not supply the missing fixed power.  It begins to save when `L>H` and
would save `H^(1/2)` for a complete `L=r` sum.

The native Blomer--Pascadi profiles are not arbitrary weights.  They obey
the point-evaluation estimate

```text
norm(z_i)_infinity
 <<H^(-1/2+o(1))norm(z_i)_2,                         (8.11)
```

proved in R112 for the relevant fixed profile family.  In particular,
the counterexample (8.2) is not a native profile.  On `P=0`, every axis
already contributes one point evaluation, and the `P=Q=0` intersections
contribute two; (8.11), together with the smaller frame (7.13), has exactly
the scaling needed to cancel the forced axis loss.

This leaves the following concrete theorem.

**Target 8.1 (native joint Vieta-product energy).**  After separating the
`P=0` axes with (7.13), prove for the actual finite family of R111/R112
completion profiles, uniformly for `r asymp H^2`,

```text
E_(P,Q)^(P!=0)(z_actual)
 <<H^(1-delta+epsilon)
    product_i norm(z_i)_2^2                         (8.12)
```

for some fixed `delta>0`.  The ideal bound has `delta=1`; any fixed
`delta>0` creates an overlap with the low-`k` R111 saving after the split is
chosen sufficiently close to `k=H`.

There is a useful equivalent opposite-pair formulation.  Put

```text
(u,x)=(h_1h_3,h_1+h_3),
(v,y)=(h_2h_4,h_2+h_4).                              (8.13)
```

Then

```text
(P,Q)=(uv,xy).                                       (8.14)
```

The Vieta map `(a,c)|->(ac,a+c)` has multiplicity at most two over
`F_r`.  Thus (8.12) is a multiplicative-energy theorem for two sparse
Vieta images in the two-dimensional coordinatewise product group.  This
is the precise coefficient-specific structure that a successful proof
must exploit.

One can locate the remaining power geometrically.  After fixing nonzero
integer lifts

```text
x=h_1+h_3,              y=h_2+h_4,                   (8.15)
```

the fixed-`P` equation becomes the bidegree-`(2,2)` curve

```text
a(x-a)b(y-b)=P.                                      (8.16)
```

For `P!=0`, it is generically a genus-one curve.  Its partial derivatives
can vanish simultaneously only at `a=x/2,b=y/2`, so the only nonzero
singular parameter is

```text
16P=x^2y^2.                                          (8.17)
```

There is no generic linear component to count away.  Standard incomplete
curve estimates in a box of side `H asymp sqrt(r)` recover the `O(H)`
fiber scale in (8.7), exactly the unresolved loss.  Target 8.1 is therefore
a critical square-root-box elliptic/multiplicative-energy estimate, not a
routine divisor refinement.

## 9. Critical exponent audit

Return to the R111 critical scale

```text
r asymp R=H^2.                                       (9.1)
```

For a fixed common integer `k<=H`, R111 gives, conditionally on its
separated outer packet,

```text
relative factor=(k/H)^(1/4).                         (9.2)
```

Thus `k<=H^(1-eta)` has a saving `H^(-eta/4)`, which
vanishes as `k` approaches `H`.

Now put `k=j theta` on a dyadic box with

```text
J Theta asymp K,
H^(1-eta)<=K<=H.                                    (9.3)
```

In the worst balanced box,

```text
max(J,Theta) asymp sqrt(K)
 <=H^(1/2)=r^(1/4).                                  (9.4)
```

There is no positive margin above the classical fourth-root threshold even
at `K=H`.  More importantly, the generic cubic is outside ordinary
Burgess regardless of that margin.

The proven methods start in the following incompatible ranges:

```text
fixed-k R111:       saves for K<=H^(1-eta);
Pólya in k:         saves for interval length >H^(1+eta);
Mellin bilinear:    saves for J Theta>r=H^2;
FKMS Type II:       requires J Theta>r^(3/4+eta)
                    and excludes this rank-one sheaf;
elementary PQ frame with (8.8):
                    starts saving only for L>H;
target PQ frame with (8.12):
                    overlaps R111 near L asymp H.     (9.5)
```

Hence the original “low `k` by trace energy, high `k` by Burgess because
one factor exceeds `r^(1/4)`” plan does not close.  The exact `(P,Q)` frame
identifies a different possible overlap, but only after Target 8.1 and the
actual coefficient interface are proved.

There is a second way to state the same endpoint, useful when comparing
with the positive Blomer--Pascadi multiplier average.  In the present
normalization, the low common-`k` theorem has relative factor

```text
(K/H)^(1/4),                 K<H,                    (9.6)
```

whereas completing a positive multiplier block of cardinality `A` gives
the complementary factor

```text
(H/A)^(1/4),                 A>H.                    (9.7)
```

They meet at `A asymp K asymp H` with no fixed power.  A genuine native
short Blomer--Pascadi box has an independent fixed-modulus estimate at
side length `sqrt(r)`, with relative saving `r^(-1/32+o(1))`; see Theorem
1.1 of
[*Bilinear forms with Kloosterman sums via quadratic characters*](https://arxiv.org/abs/2607.24311).
That theorem would cover the transition **after** two native short
intervals have been produced.  R105's exact full-tail completion instead
has a full Fourier support and a modular-inverse image support, as audited
in R111's outer-packet report.  Substituting short intervals for those
supports is precisely the still-open R71 bridge.  Thus the transition is
closed in the published short-box model and remains open for the actual
full R105/R71 support geometry.

## 10. The actual R71 interface

The following statements are proved finite-field algebra:

1. the identity (1.2) and square classification (2.2);
2. the complete and mixed sums in Sections 3--4;
3. the Mellin bound (6.3);
4. the exact coefficient frames (7.3) and (7.13); and
5. the arbitrary-weight obstruction (8.4) and nonzero-`P` endpoint
   (8.8).

They do **not** yet prove that the actual R71 sum satisfies the hypotheses
needed to use the favorable side of the frame.  Four interfaces remain.

### 10.1. The `k`-dependent profile phase

In the actual Blomer--Pascadi short-box completion, the odd
autocorrelations depend on the multiplier `k` through a phase of the form

```text
e_r(-s_1 k(h_1+h_3)).                                (10.1)
```

Thus one cannot simply form a common coefficient `C_r(P,Q)` and apply
(7.7).  Either (10.1) must be absent after the exact R71 recombination, or
the pushforward must retain the additional invariant `h_1+h_3` and prove
a correspondingly twisted frame/energy theorem.  For a complete `k`-sum,
Theorem 4.1 gives (4.5); for a short sum it restores the completion
threshold.

### 10.2. Signed `k=j theta` aggregation

The actual amplitude couples `j,theta,g,p,r` through B-spline profiles,
common-factor masks, and seam translates.  Equation (7.9) handles a genuine
separated product weight, but no assertion is made here that the complete
R71 coefficient has that form with subpower projective cost before
absolute values are taken.

### 10.3. Central matrices

`D=0` means trace `plusminus2`, not necessarily matrix `plusminus I`.
The ordinary Legendre term vanishes there.  The exceptional value of the
special `SL_2` character is governed by the stricter central-word
classification in R112.  That report bounds it for native flat profiles,
conditional on the same outer-packet lift.  It must not be recreated by
treating every root of `D` as a central contribution.

### 10.4. Outer-prime and rectangular limits

The common-`r` rows, ramified rows, Type-I correction, axes, and completed
rectangular limiting order must remain together.  The frame theorem is
fixed-modulus.  Summing its conclusion over `r` is legitimate only after
the actual row weights and projective costs are exposed; it does not supply
that decomposition automatically.

## 11. Research verdict

The polynomial algebra is favorable: there is no hidden nonsquare failure,
and the complete family has more orthogonality than the pointwise approach
reveals.  The literature reality check is unfavorable to the proposed
shortcut: no imported nonlinear Burgess theorem supplies the required
fourth-root estimate for the generic cubic.

The most valuable next move is now narrow and falsifiable:

```text
retain the real BP/R71 k-dependent phase;
split P=0 and use its exact r-dimensional frame;
prove or disprove a fixed-power improvement over the H-loss in
the nonzero-P joint Vieta-product energy;
then insert that theorem before the outer Hölder/large-sieve step. (11.1)
```

If (8.12) fails for the native profiles, this coefficient-pair mechanism is
killed at the same endpoint as pointwise completion.  If it holds and the
interfaces in Section 10 are supplied, it gives the first genuine overlap
between R111's low-`k` trace saving and a high-`k` cancellation theorem.
That would still be a component of the fixed-strip proof, not by itself a
proof of a zero-free strip.
