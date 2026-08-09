# Signed joint reciprocal compression and the zero-orbit gate

Status: R86 exact finite joint-operator theorem, shifted-Ramanujan kernel,
zero-orbit calculation, canonical dissipation/Schur identities, and uniform
native prime-point obstruction.  A fixed-power estimate for the complete
R71 kernel remains open.  No zero-free strip is proved.

This report pursues the last target isolated in R85 without first applying a
triangle inequality:

```text
square-root reciprocal Type-II term - canonical gamma contact.          (1.1)
```

The fail-fast answer is unusually clean.  In the unseparated square-root
frame, reciprocal transport has **no zero shift character**.  The zero orbit
of `R_j-I` is therefore exactly `-I`, so completion exposes `-gamma` instead
of absorbing it.  Whitening the canonical frame turns the joint operator
into a compression of a diagonal unitary.  This gives an exact dissipative
square and an exact Schur-leakage square, but no small parameter.  For the
actual positive prime weights `h_p=log(p)/p`, a pointwise argument at primes
proves that the full native signed residual has natural size uniformly in
the shift.

Thus the hoped-for fixed power does not exist in the Euclidean or canonical
frame norm of this complete square-root block.  What remains logically
possible is narrower: the particular R71 B-spline kernel, all `g`-sectors,
all axes and seams, and the Type-I corrections could have a signed pairing
which is small even though the underlying vector is not.  That is a new
kernel-specific theorem, not a consequence of ordinary dispersion,
Ramanujan centering, frame canonicality, or spectral reciprocity.

```text
signed joint algebra                         EXACT
ordinary reciprocal zero orbit               -gamma, not cancellation
canonical Hilbert contraction                FALSE
native complete-block contraction            FALSE
smooth flat-shift cancellation               POWER-SUPPRESSED
special complete R71 kernel pairing           OPEN
fixed zero-free strip                         NOT PROVED.              (1.2)
```

## 2. The exact unseparated signed field

Let `I` be an interval of `H` consecutive integers and let `P` be a finite
set of distinct primes such that

```text
pr>H-1,                   p,r in P, p!=r.              (2.1)
```

For the asymptotic norm comparisons below, take the R84 window
`c_-sqrt(H)<=p<=c_+sqrt(H)` with fixed `sqrt(2)<c_-<c_+`; this supplies both
(2.1) and the uniform lower frame bound.

Use every ordered pair and every primitive residue:

```text
Omega={(p,r,theta):p!=r, theta in (Z/(pr)Z)^*},

A_(n;(p,r,theta))=e(theta n/(pr)),       n in I.       (2.2)
```

Put

```text
S=AA^*,
v_n=Lambda(n)-1,
w=S^(-1)v,
gamma=A^*w.                                             (2.3)
```

R84 proves that `S` is uniformly comparable to `K^2 H I` in a fixed
multiplicative square-root-prime window and that

```text
A gamma=v,
norm(gamma)_2^2=v^*S^(-1)v.                            (2.4)
```

For an integer shift `j`, define the reciprocal rotation

```text
(R_j)_(p,r,theta)
 =e(-j theta inverse(p)/r).                            (2.5)
```

If `theta=ar-bp`, then the right side of (2.5) is `e(jb/r)`.  It is exactly
the factor which changes the slow beat into the native phase; there is no
cosine replacement and no sign ambiguity.

For the native coefficients set

```text
h_p=log(p)/p,
d_(p,r,theta)=h_p h_r.                                 (2.6)
```

### Theorem 2.1 (exact shifted Type-II synthesis)

For every `n in I` and every integer `j`,

```text
(A R_j d)(n)
 =sum_(p!=r)h_p h_r c_p(n)c_r(n-j)                    (2.7)

 =X(n)X(n-j)-sum_p h_p^2 c_p(n)c_p(n-j),

X(n)=sum_p h_p c_p(n).                                (2.8)
```

Consequently the bare signed joint object is exactly

```text
F_j=A R_j d-v=A(R_jd-gamma).                           (2.9)
```

#### Proof

Multiplying the frame column by (2.5) gives

```text
e[theta(n-jp inverse(p mod r))/(pr)].                  (2.10)
```

The translation in parentheses is `n` modulo `p` and `n-j` modulo `r`.
Summing primitive `theta` therefore gives

```text
c_(pr)(n-jp inverse(p mod r))=c_p(n)c_r(n-j).          (2.11)
```

Sum (2.11) with (2.6).  Adding the forbidden diagonal and subtracting it
again gives (2.8), while (2.4) gives (2.9).

Equation (2.9) is the finite `g=1`, unequal-prime square-root layer before
the final R71 kernel contraction.  It is not the complete all-cofactor
energy.  This distinction is essential below.

## 3. The shifted Ramanujan operator

Define

```text
S_j=A R_j A^*.                                        (3.1)
```

### Theorem 3.1 (exact shifted kernel)

For `t,m in I`,

```text
S_j(t,m)
 =sum_(p!=r)c_p(t-m)c_r(t-m-j).                        (3.2)
```

Equivalently, put `delta=t-m` and

```text
Q_(p,r,j)(t,m)=1_(p|delta)1_(r|delta-j),
P_p(t,m)=1_(p|delta),
P_(r,j)(t,m)=1_(r|delta-j).
```

Then

```text
S_j
 =sum_(p!=r)pr Q_(p,r,j)
  -(K-1)sum_p pP_p
  -(K-1)sum_r rP_(r,j)
  +K(K-1)J.                                           (3.3)
```

At `j=0`, condition (2.1) turns the two-prime incidence into the identity
and recovers R84's global frame formula.  Formula (3.3) is useful because it
shows exactly where the Type-II incidence, the one-prime marginals, and the
constant contact occur.  A delta or dispersion step does not get to discard
the last three terms.

If pair weights `D_(p,r)` have zero row and column sums, their weighted
version obeys

```text
S_j[D]-S_0[D]
 =sum_(p!=r)prD_(p,r)(Q_(p,r,j)-I).                    (3.4)
```

This is a pure signed partial-translation coboundary.  It is not positive:
every nonzero row- and column-centered `D` has mixed signs.  Thus the
Dirichlet square attached to one translation cannot be summed with positive
coefficients to control the actual affine defect.

## 4. Whitening gives the complete cancellation criterion

Let

```text
U=A^*S^(-1/2),          U^*U=I,
Pi=UU^*,
x=S^(-1/2)v,
gamma=Ux,
C_j=U^*R_jU=S^(-1/2)S_jS^(-1/2).                     (4.1)
```

Thus `C_j` is a compression of a diagonal unitary and `norm(C_j)<=1`.

### Theorem 4.1 (full signed criterion)

For an arbitrary coefficient vector `d`,

```text
S^(-1/2)(A R_jd-v)
 =U^*R_j(d-gamma)+(C_j-I)x                            (4.2)

 =U^*(R_jd-gamma),                                    (4.3)

norm(A R_jd-v)_(S^(-1))
 =norm[Pi(R_jd-gamma)]_2.                              (4.4)
```

In particular, exact signed cancellation occurs if and only if

```text
Pi R_jd=gamma
 <=> R_jd-gamma belongs to ker(A).                    (4.5)
```

This is the correct null-space formulation.  The large coefficient
nullspace means that a coefficient-uniform lower bound is false in complete
generality.  It does not align the particular rank-one vector (2.6) with
the canonical `Lambda-1` dual.  That alignment is precisely the arithmetic
claim being tested, not a consequence of frame redundancy.

The first summand in (4.2) is the twisted native-versus-canonical mismatch.
The second is the canonical reciprocal slice.  They must not be conflated.

## 5. Canonicality gives dissipation, not a saving

The canonical slice alone has stronger exact structure.

### Theorem 5.1 (compression, dissipation, and leakage)

One has

```text
S^(-1/2)A(R_j-I)gamma=(C_j-I)x,                       (5.1)

Re <x,(C_j-I)x>
 =-1/2 norm[(R_j-I)gamma]_2^2,                        (5.2)

norm[(R_j-I)gamma]_2^2
 =norm[(C_j-I)x]_2^2
  +norm[(I-Pi)R_jgamma]_2^2,                          (5.3)

I-C_j^*C_j
 =U^*R_j^*(I-Pi)R_jU>=0.                              (5.4)
```

#### Proof

Equations (5.1) and (5.4) follow from (4.1).  Since `U` is an isometry and
`R_j` is unitary,

```text
Re <x,(C_j-I)x>
 =Re <gamma,(R_j-I)gamma>
 =-norm[(R_j-I)gamma]^2/2.                            (5.5)
```

Orthogonally split `(R_j-I)gamma` into its `Pi` and `I-Pi` components to
obtain (5.3).

An immediate lower bound is

```text
norm[A(R_j-I)gamma]_(S^(-1))/norm(v)_(S^(-1))
 >=norm[(R_j-I)gamma]_2^2/[2norm(gamma)_2^2].          (5.6)
```

Hence a small canonical signed output would force the reciprocal phase
defect itself to be small.  Leakage into the coefficient nullspace cannot
hide that fact.  The identity is dissipative only in the canonical test
`S^(-1)v`; an arbitrary R71 contact has no sign.  It is therefore a sharp
reality check, not the missing kernel estimate.

There is also an exact failure of the compressed group law:

```text
C_(j+k)-C_jC_k=U^*R_j(I-Pi)R_kU.                      (5.7)
```

Thus iterating the compressed rotations creates the same Schur leakage; it
does not create a semigroup contraction that can be applied for free.

## 6. The zero orbit is the carrier

Fix the second prime `r` and write

```text
a_(p,r,theta)=theta inverse(p) mod r,       a!=0.      (6.1)
```

For `ell mod r`, define the shift Fourier projection

```text
E_(r,ell)=1/r sum_(j mod r)e(ell j/r)R_j.              (6.2)
```

It is the coordinate projection onto `a_(p,r,theta)=ell`.  Primitivity gives

```text
E_(r,0)=0.                                             (6.3)
```

This is the decisive zero-orbit test:

```text
reciprocal transport R_j:       zero character = 0;
joint transport R_j-I:          zero character = -I.  (6.4)
```

Applied to the canonical coefficient, the second line is exactly
`-gamma`; after synthesis it is `-v`.  Complete reciprocal dispersion
therefore exposes the contact which it was supposed to cancel.

Let `L_P=lcm(P)`.  Complete shift averaging gives, for every coefficient
vector `d`,

```text
1/L_P sum_(0<=j<L_P)R_jd=0,                            (6.5)

1/L_P sum_j(A R_jd-v)=-v,                             (6.6)

1/L_P sum_j norm(A R_jd-v)_(S^(-1))^2
 >=norm(v)_(S^(-1))^2.                                (6.7)
```

Thus no fixed coefficient packet can cancel the contact uniformly in the
shift or in complete-shift mean square.

There is a useful short-average version.  For `N` consecutive shifts and
`r<=Q`, the geometric-sum bound gives

```text
norm[1/N sum_(0<=j<N)R_j]_(op)
 <=1/[N sin(pi/Q)]<<Q/N.                              (6.8)
```

Consequently

```text
norm{
  1/N sum_j A(R_j-I)gamma+v
}_(S^(-1))
 <<(Q/N)norm(v)_(S^(-1)),                             (6.9)

1/N sum_j norm[(R_j-I)gamma]_2^2
 =[2+O(Q/N)]norm(gamma)_2^2.                          (6.10)
```

At `Q asymp sqrt(H)` and `N asymp H`, averaging suppresses the transported
part by `H^(-1/2)` and leaves `-v` at full scale.  These statements use flat
weights.  They do not silently replace the actual R71 B-spline amplitude by
a constant.

### Smooth weights do not repair the zero orbit

For any finite scalar weight `q_j` and nonzero `a mod r`, summation by parts
gives

```text
abs sum_j q_j e(-ja/r)
 <<r[2norm(q)_infinity+sum_j abs(q_(j+1)-q_j)].        (6.11)
```

If `q` has mass `asymp N norm(q)_infinity` and bounded normalized total
variation, its reciprocal-frequency response is only `O(r/N)` of its zero
response.  On the square-root geometry this is `O(H^(-1/2))` for a full
length-`H` bulk.  Therefore a successful cross-cancellation cannot come
from a slowly varying interior weight.  It would have to be supplied by
coefficient-dependent seams, resonances, or the other exact R71 sectors.
This identifies a precise role for the still-open uniform seam ledger.

## 7. A uniform obstruction for the actual native weights

The zero-orbit calculation is an average statement.  The positive prime
weights give a stronger pointwise obstruction.

### Theorem 7.1 (prime-point ceiling)

Let `d` be (2.6), and suppose that the prime target point `n` exceeds every
prime in `P`.  Then, uniformly in the integer shift `j`,

```text
(A R_jd)(n)
 <=B_P:=(sum_p h_p)^2-sum_p h_p^2.                    (7.1)
```

For a fixed multiplicative square-root-prime window, `B_P=O(1)`.  On an
interval `I subset [H,CH]`, the PNT therefore gives

```text
norm(A R_jd-v)_2^2>>H log H asymp norm(v)_2^2          (7.2)
```

uniformly in `j`.  The R84 frame bounds imply

```text
norm(A R_jd-v)_(S^(-1))
 >=c_0 norm(v)_(S^(-1))                               (7.3)
```

for a fixed `c_0>0` depending only on the prime window.

#### Proof

At such a prime `n`, `c_p(n)=-1` for every bank prime.  Let
`H_P=sum_p h_p`.  From (2.7),

```text
(A R_jd)(n)
 =sum_r h_r(h_r-H_P)c_r(n-j)

 =H_P^2-sum_r h_r^2
  +sum_(r|n-j)r h_r(h_r-H_P).                         (7.4)
```

Every term in the last sum is nonpositive, proving (7.1).  Mertens' prime
sum, or the PNT by partial summation, gives

```text
sum_(c_-sqrt(H)<=p<=c_+sqrt(H))log(p)/p
 =log(c_+/c_-)+o(1),                                  (7.5)
```

so `B_P=O(1)`.  At the `asymp H/log H` primes in `I`,
`v_n=log n-1`, and each squared residual is `gg log^2 H`.  This proves
(7.2).  Finally use

```text
cK^2H I<=S<=CK^2H I                                  (7.6)
```

on both `A R_jd-v` and `v` to obtain (7.3).

The conclusion is exact for the complete native square-root bank: its
signed residual is not power-small in either natural Hilbert metric.  It
does not permit a lower bound on the complete R71 energy by isolating this
block; other cofactors and Type-I pieces are signed and must remain joint.

## 8. The affine/Schur loophole does not give a uniform repair

R85's square-root affine counterterm can be written as a constrained control
map.  Let `D_0` be the Hermitian pair matrices with zero row and column sums
and put

```text
(J D)_(p,r,theta)=[Y theta/(pr)]D_(p,r),
B_j=U^*R_jJ.                                           (8.1)
```

The best possible unpenalized affine fit is the exact Schur projection

```text
inf_(D in D_0)norm[A(R_jJD-gamma)]_(S^(-1))^2
 =norm[P_(ker B_j^*)x]_2^2.                            (8.2)
```

With a quadratic penalty `lambda norm(D)^2`, it is

```text
lambda x^*(B_jB_j^*+lambda I)^(-1)x.                  (8.3)
```

Canonicality supplies the vector `x`; it does not force either quantity to
vanish.  Moreover

```text
rank(B_j)<=(K-1)^2=O(H/log^2 H)=o(H).                 (8.4)
```

Every fixed-degree moment lift still has sub-full rank.  Hence this class
cannot cancel arbitrary targets.  Dimension alone does not prove that the
particular prime vector has fixed mass in the complement, but Theorem 7.1
already rules out the actual native rank-one cancellation in the complete
frame norm.  Finite low-band fits merely move the debt into the full packet,
as R84's prolate argument predicts.

## 9. Finite exact diagnostics

The identities above are exercised by
[`common_dual_reciprocal_compression_probe.py`](../src/common_dual_reciprocal_compression_probe.py).
It checks the phase orientation, shifted Ramanujan kernel, native synthesis,
isometry, compression, dissipation, Schur leakage, complete shift average,
and prime-point ceiling.

For `I=[H+1,2H]`, `j=1`, and primes in approximately
`[1.5sqrt(H),3.2sqrt(H)]`, representative rows are

```text
 H    K   norm(C_j)  s_min(C_j-I)  canonical S^-1  native S^-1   corr
 64   4    .2363          .9621          1.0576          1.3017    .0224
 96   5    .1881          .9619          1.0389          1.3379   -.0292
128   5    .2091          .9336          1.0425          1.2630   -.0047
192   6    .1629          .9401          1.0259          1.2352    .0303. (9.1)
```

Here `canonical S^-1` is

```text
norm[A(R_j-I)gamma]_(S^(-1))/norm(v)_(S^(-1)),
```

`native S^-1` is the corresponding ratio for `A R_jd-v`, and `corr` is
the whitened correlation between `A R_jd` and `v`.  The compressed twisted
canonical term is small, so `C_j-I` is approximately `-I`; the native term
is nearly orthogonal to the contact.  These rows are D-rated diagnostics,
not asymptotic evidence.  Theorems 6.1 and 7.1 supply the rigorous statements.

## 10. Literature boundary and the spectral-reciprocity detour

No checked theorem bounds (2.9) with the canonical contact retained.

* Drappeau's
  [signed dispersion theorem](https://arxiv.org/abs/1504.05549) retains a
  congruence block minus an exact low-conductor character projector and can
  give a fixed power.  At `Q asymp x^(1/2)`, its condition
  `N<=Q^(2/3-eta)` is unbalanced (`N` is at most about `x^(1/3)`), and its
  projector is not `A^*(AA^*)^(-1)(Lambda-1)`.
* Fouvry--Radziwill's
  [unbalanced-convolution theorem](https://arxiv.org/abs/1811.08672) has the
  same architecture but not the balanced square-root range or a fixed-power
  canonical contact estimate.
* Kowalski--Michel--Sawin prove fixed powers for balanced
  [bilinear Kloosterman trace-function sums](https://arxiv.org/abs/1511.01636)
  after the main/contact term has already been extracted.  Their theorem
  supplies no estimate for the surviving `-gamma` orbit.
* Andersen--Kiral's
  [level reciprocity](https://arxiv.org/abs/1801.06089) and Blomer--Khan's
  [spectral reciprocity](https://arxiv.org/abs/1706.01245) exchange two
  levels.  At `p asymp r` the dual problem has the original size.  The
  canonical profile `W(theta/(pr))` is in the symmetric sector, so
  antisymmetrizing in `p,r` removes the target rather than bounding it.
* The 2026 symmetric formula of Yang
  [regularizes Eisenstein fourth moments](https://arxiv.org/abs/2607.04476)
  and proves a subconvex saving, but its data are automorphic
  Hecke/Whittaker coefficients and explicit residue terms, not the finite
  canonical dual here.

A tempting off-wall variant is to differentiate the Eisenstein spectral
parameter.  It also fails the coefficient test.  The nonzero Fourier
coefficients have divisor form

```text
tau_s(n)=sum_(ab=n)(a/b)^s,                            (10.1)
```

as in Li--Knightly's
[Kuznetsov treatment](https://arxiv.org/abs/1202.0189).  Differentiation
produces log-weighted divisor sums, not `Lambda`.  The required nonlinear
`-zeta'/zeta` appears in normalizing/scattering factors and degenerate
residues.  Differentiation increases their pole order at zeta zeros; it
relocates the obstruction rather than estimating it.  Wu's
[Motohashi formula](https://arxiv.org/abs/2001.09733) likewise keeps those
degenerate residue distributions explicit.  Applying a Möbius/logarithmic
derivative to the entire reciprocity formula would require re-proving bounds
for all induced zero poles and is the original problem in new notation.

## 11. Exact disposition and next theorem

R86 closes the broad signed-contraction idea:

```text
ordinary shift completion:
    reciprocal zero orbit absent; joint zero orbit = -gamma;

canonical compression:
    contraction C_j exists, but C_j-I is natural size and dissipative;

native square-root packet:
    A R_jd-v has a uniform full-scale prime-point lower bound;

flat or slowly varying shift weights:
    reciprocal transport averages away and leaves the carrier;

affine fixed-moment controls:
    sub-full-rank Schur family, with the old full-packet debt;

balanced spectral reciprocity:
    self-dual, symmetric target, no scale contraction;

Eisenstein differentiation:
    divisor-log coefficients and worse zero-pole residues.             (11.1)
```

The remaining statement is not “prove that the signed square-root vector is
small”; Theorem 7.1 shows that statement is false.  The only live version is

```text
prove a fixed-power bound for the pairing of the full signed field with
the actual complete R71 kernel, retaining every g-sector, primitive mask,
axis, seam, Type-I correction, and conditional rectangular limit.       (11.2)
```

Equation (6.11) gives the next fail-fast test.  Compute the exact discrete
variation/Fourier response of the real R71 amplitude at the character gap
`theta inverse(p)/r`.  If its smooth bulk obeys the expected variation
ledger, it is power-orthogonal to the contact and cannot be the cancellation
source.  Any survivor must then be localized explicitly to seams,
resonances, or cross-`g`/Type-I terms.  Those pieces must be recombined before
any norm or absolute value is taken.

No conclusion about the truth, falsity, or ZFC independence of RH follows
from this gate.  It removes a proposed mechanism and makes the residual
theorem more specific.
