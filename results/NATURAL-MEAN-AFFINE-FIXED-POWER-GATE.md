# Natural-mean centering and the affine fixed-power gate

Status: R85 exact arithmetic-centering theorem, imported fixed power for the
nonresonant mean-zero reciprocal component, affine Ward identity, and
top-prime/square-root-prime scale dichotomy.  The fixed-power bound for the
full centered R71 energy remains open.

R86 successor:
[`SIGNED-JOINT-RECIPROCAL-COMPRESSION-GATE.md`](SIGNED-JOINT-RECIPROCAL-COMPRESSION-GATE.md).

This report answers the question left by R84: can the favorable common-dual
coefficient be joined to the reciprocal phase by a constant-plus-linear
determinant counterterm, and can the resulting expression inherit a fixed
power from existing Kloosterman-fraction estimates?

The answer separates sharply into two parts.

1. There is a genuine fixed-power theorem for the **arithmetically
   mean-zero reciprocal fluctuation**.  In the balanced square-root box,
   Wright's current theorem gives the nominal relative saving
   `H^(-1/40+o(1))`, subject to the R84 kernel ledger.  Earlier theorems give
   weaker fixed powers under their own hypotheses.
2. Correct centering leaves the canonical coefficient `gamma` at full
   strength.  The proposed affine term is either an arbitrary
   integration-by-parts rewrite, or an exact null-gauge term at moduli whose
   scale makes it power-expensive.  At the square-root scale where its
   normalization would be useful, the null identity fails by exactly the
   near-square Type-II carrier.

Thus R85 proves a fixed power for a proper component, but it also proves
that this component is not the missing fixed-strip theorem.

## 1. The exact arithmetic mean

Write `e(x)=exp(2 pi i x)`.  Let `r` be prime, `(p,r)=1`, and put

```text
z_(r,k)(p)=e(-k inverse(p)/r).
```

Inversion permutes the nonzero residue classes modulo `r`.  Therefore the
complete primitive mean is

```text
mu_r(k)
 =1/(r-1) sum_(x mod r)^* e(-k inverse(x)/r)
 =c_r(k)/(r-1)
 ={-1/(r-1),  r does not divide k;
     1,        r divides k.}                           (1.1)
```

This is the arithmetic center of the inverse phase.  The subtraction by
`1` used to display R84 (5.4) is an algebraically valid split, but it is not
a centered Kloosterman fluctuation.  If `r` does not divide `k`, then

```text
sum_(p mod r)^* [z_(r,k)(p)-1]=-r,                     (1.2)

sum_(p mod r)^* [z_(r,k)(p)-mu_r(k)]=0.                (1.3)
```

The corresponding complete-residue square ledgers are

```text
sum_p^* abs(z_(r,k)(p)-1)^2=2r,

sum_p^* abs(z_(r,k)(p)-mu_r(k))^2
 =(r-1)-1/(r-1)=r(r-2)/(r-1)                          (1.4)
```

when `r` does not divide `k`.  Correct centering does not make the vector
small in `l2`; it removes its constant component, which is the hypothesis
used by completion and dispersion.

## 2. Exact carrier split

Use the notation of R84 Section 5 and put

```text
k=j theta,
Phi_(p,r,theta,j)
 =e(k/(pr)) A_(p,r,theta)(j),
h_(p,r)=h_p conjugate(h_r).                            (2.1)
```

### Theorem 2.1 (natural-mean decomposition)

Term by term, with no limiting or smoothness assumption,

```text
O-B
 =sum Phi {h_(p,r)[e(-k inverse(p)/r)-mu_r(k)]
            +[mu_r(k)h_(p,r)-gamma_(p,r,theta)]}.      (2.2)
```

#### Proof

Add and subtract `mu_r(k)h_(p,r)` inside

```text
h_(p,r)e(-k inverse(p)/r)-gamma_(p,r,theta).
```

That is (2.2).

For a nonresonant numerator `r` not dividing `k`, the second bracket is

```text
-gamma_(p,r,theta)-h_(p,r)/(r-1).                     (2.3)
```

For `p,r asymp Q`, the added native term is `Q^(-1)` smaller than
`h_(p,r)`.  The canonical term `-gamma` is unchanged.  At a resonance
`r|k`, the first bracket vanishes identically and the second is

```text
h_(p,r)-gamma_(p,r,theta).                             (2.4)
```

Thus resonant numerators are literal axes, not oscillatory exceptions.

The mean in (1.1) is exact for the complete unweighted unit group.  A sparse
prime interval with variable weights `h_p` does not itself have zero mean.
This does not affect (2.2); it says that a coefficient-uniform completion
theorem can act on the first bracket, not that the sparse prime sum cancels
without such a theorem.

## 3. What existing fixed powers actually prove

Define the nonresonant reciprocal fluctuation

```text
C_(r,k)(p)=e(-k inverse(p)/r)+1/(r-1),
             r does not divide k.                     (3.1)
```

### Proposition 3.1 (localized fixed-power component)

Consider a mask-free R84 dyadic box with

```text
p,r asymp Q=H^(1/2),
k=j theta !=0,
r does not divide k.                                  (3.2)
```

Assume the uniform kernel/projective ledger R84 (4.8), with all seam
seminorms `H^o(1)`, numerator product `abs(k)<=H^(1+o(1))`, and determinant
bandwidth

```text
abs(theta)<=H^tau,             0<=tau<1/20.            (3.2a)
```

Then the contribution of

```text
h_p conjugate(h_r) C_(r,k)(p)                         (3.3)
```

has a relative saving

```text
H^(-eta_tau+o(1)),
eta_tau=1/40-tau/2>0.                                 (3.4)
```

from Wright's Theorem 2.1.  The Ramanujan-mean summand in (3.1) has the
stronger elementary factor `Q^(-1)`.  Polynomial weights of fixed degree in
`k` are already allowed as changes to Wright's arbitrary numerator
sequence, but their coefficient norm must be charged.

#### Proof

R84 Proposition 4.1 groups the shift and determinant into the numerator
`k=j theta` and maps the mask-free box to Wright's scalar form.  At
`M=N=Q`, fixed denominator `R=1`, and numerator product at most
`H^(1+o(1))`, the weakest term of Wright's displayed estimate saves at least
`Q^(-1/20+o(1))=H^(-1/40+o(1))`.  R84 (4.8)--(4.10) charge the crude
determinant bandwidth by `H^(tau/2)`, giving (3.4).  Subtracting
`-1/(r-1)` costs at most `Q^(-1)` times the same nonoscillatory coefficient
ledger.  The conditional kernel hypothesis is exactly the hypothesis still
isolated in R84 (4.8), not a hidden claim that it has been proved for every
B-spline seam.

This is consistent with the primary literature:

* Duke--Friedlander--Iwaniec's bilinear theorem gives a balanced
  coefficient-uniform fixed power and explicitly exposes the Ramanujan sum
  at completion's zero frequency; in the present normalization its generic
  balanced saving is only `H^(-1/96)`.
* Bettin--Chandee's Theorem 1 gives the balanced Kloosterman-fraction power
  and accepts an additional inert smooth phase.  It still controls only the
  oscillatory term.
* Irving's Theorem 1.3 can give `H^(-1/16)` in the relevant balanced size,
  but requires prime-supported inner coefficients not supplied by every
  R71 box.
* Wright's Theorem 2.1 supplies the best directly compatible displayed
  power, `H^(-1/40)`, and permits arbitrary numerator coefficients.
* Fouvry--Radziwill's main-term subtraction concerns an unbalanced
  convolution, excludes the balanced box at its prime-modulus endpoint,
  and gives an averaged logarithmic conclusion rather than (2.2).

The cited primary sources are:

* Duke, Friedlander, and Iwaniec,
  [Bilinear forms with Kloosterman fractions](https://doi.org/10.1007/s002220050135);
* Bettin and Chandee,
  [Trilinear forms with Kloosterman fractions](https://arxiv.org/abs/1502.00769);
* Irving,
  [Average bounds for Kloosterman sums over primes](https://arxiv.org/abs/1301.6372);
* Fouvry and Radziwill,
  [Level of distribution of unbalanced convolutions](https://arxiv.org/abs/1811.08672);
* Wright,
  [Trilinear Kloosterman fractions I](https://arxiv.org/abs/2604.25177),
  current v1 on the audit date.

### Why Proposition 3.1 is not the desired theorem

The residual (2.3) is

```text
-gamma_(p,r,theta)+O(h_(p,r)/Q).                      (3.5)
```

The leading term is exactly the canonical slow beat that reconstructs the
prime-minus-continuum contact.  It has no inverse phase.  R84's contact
duality and low-band calculation show that moving it into a smooth high
tail repays the apparent decay.  Bounding (3.5) by a fixed power is therefore
the fixed-strip-strength part of the problem, not a consequence of
Proposition 3.1.

## 4. The affine integration-by-parts identity

Put

```text
q=gmn,
F_j(u)=L(u+gj,u),
D L=(partial_1+partial_2)L,

A_L(g,m,n,theta;j)
 =g integral F_j(u)e(theta u/q)du.                    (4.1)
```

### Theorem 4.1 (affine Ward identity)

On one smooth piece,

```text
theta A_L
 =q/(2 pi i){g[F_j(u)e(theta u/q)]_boundary-A_(D L)}. (4.2)
```

In particular, for a compactly supported smooth piece,

```text
theta A_L=-q A_(D L)/(2 pi i).                        (4.3)
```

For every coefficient `d`, every residual `R`, and a compact piece,

```text
R A_L
 =(R+theta d)A_L+q d A_(D L)/(2 pi i).                (4.4)
```

With a sharp or dyadic seam, subtract

```text
q g d [F_j e(theta u/q)]_boundary/(2 pi i)            (4.5)
```

from the right side of (4.4).

#### Proof

Integrate the derivative of `F_j(u)e(theta u/q)`.  Equation (4.4) follows
by adding the resulting zero identity.

This is a Ward identity, not a new estimate.  It does not produce a
preferred `d`; an affine coefficient can be inserted arbitrarily if the
derivative term and every seam term are retained.  More generally,

```text
theta^a A_L=(-q/(2 pi i))^a A_(D^a L)                 (4.6)
```

for every fixed `a` on a compact smooth piece.  Hence every fixed-degree
polynomial counterterm merely moves the same contact through finitely many
normalized derivatives.

On the balanced support, `q` is comparable to the physical kernel scale.
Each derivative costs the inverse scale, so `q^a D^a L` has the same
homogeneity as `L`.  There is no fixed power in (4.6).  In its direct form,
the derivative term retains the slow phase `e(k/(pr))`.

There is a clever exact way to attach a reciprocal phase to that derivative.
It narrows the algebra, but arithmetic centering shows that it cannot change
the residual.

### Theorem 4.2 (reciprocal derivative transfer)

Let

```text
P=e(k/(pr)),
R=e(-k inverse(p)/r),
c=h_p conjugate(h_r),
k=j theta,
q=gmn,
A=A_L,
A_D=A_(D L).                                           (4.7)
```

For `theta!=0` and compact support,

```text
c P R A-gamma P A
 =gamma P(R-1)A
   +q(gamma-c)/(2 pi i theta) P R A_D.                 (4.8)
```

The second term now has the native reciprocal phase.  After normalizing the
derivative by the physical scale `Y`, its extra coefficient is

```text
(q/Y)(gamma-c)/theta.                                  (4.9)
```

When `q/Y=H^o(1)`, division by a nonzero integer `theta` contracts the
theta-`l2` ledger.  Thus R84's log-Mellin separation and Wright's estimate
can, conditionally on the derivative version of the kernel ledger, control
this term with a fixed power.

#### Proof

By (4.3),

```text
q(gamma-c)A_D/(2 pi i theta)=(c-gamma)A.
```

Substitution in the right side of (4.8) gives
`cPRA-gamma PA`.

This transfer does not remove the contact.  Center both reciprocal factors
at the exact mean `mu=mu_r(k)`.  The two mean-zero pieces in (4.8) combine
back to

```text
c P(R-mu)A,                                            (4.10)
```

while their arithmetic-mean projection is exactly

```text
P[mu c-gamma]A.                                        (4.11)
```

Indeed, the mean contribution of the derivative term is
`mu(c-gamma)PA`, and adding `gamma(mu-1)PA` from the first term gives
`(mu c-gamma)PA`.  Equations (4.10)--(4.11) are precisely Theorem 2.1.
The derivative transfer therefore makes every nonconstant reciprocal piece
Wright-compatible, but leaves the same canonical slow carrier invariant.

The complete interpolation identity makes the coefficient tradeoff
explicit.  For every `a=a_(p,r,theta)`,

```text
c P R A-gamma P A
 =P{a(R-mu)A+(mu a-gamma)A
     +q(a-c)/(2 pi i theta)R A_D}.                     (4.12)
```

Choosing `a=gamma` gives (4.8).  Choosing

```text
a=gamma/mu                                             (4.13)
```

kills the displayed slow residual.  Off resonance, however,
`abs(mu)=1/(r-1)`, so this multiplies the canonical coefficient ledger by
`r-1 asymp H^(1/2)`.  The available Wright saving is only
`H^(-1/40+o(1))`; the exact centering cure is therefore power-fatal.  Any
attempt to split off the mean of the enlarged derivative term simply returns
the invariant bracket (4.11).

Trying to estimate `R-1` directly through

```text
R-1=-2 pi i k inverse(p)/r
       integral_0^1 e(-s k inverse(p)/r)ds             (4.14)
```

does not evade this projection: the layer `s` near zero is the contact, and
Wright's theorem has a nonzero integer phase rather than this continuous
parameter down to zero.

The common-dual profile gives the same warning directly:

```text
gamma_(p,r,theta)=sum_(n in I)w_n e(-theta n/(pr)),

partial_theta^a gamma
 =(-2 pi i)^a sum_n w_n(n/(pr))^a e(-theta n/(pr)).   (4.15)
```

For `n` and `pr` both of order `H`, the ratio `n/(pr)` is order one.
Taylor expansion in an integer `theta` therefore supplies no factor
`H^(-a)`.  Any extra moment cancellation in the actual `w` would itself be
new prime-discrepancy information.

## 5. The one exact affine null gauge and its scale obstruction

R82 contains a genuine source of an affine determinant coefficient.  Let
the active integer support lie in `1<=n<=Y` and let

```text
B_p=T(sum_n c_p(n)delta_n),
A=T(sum_n delta_n).
```

For every prime `Y<p<=2Y`, `c_p(n)=-1` on the active support, so

```text
B_p=-A.                                                (5.1)
```

### Theorem 5.1 (top-prime derivative null gauge)

Let `D=(D_(p,r))` be Hermitian and satisfy

```text
sum_(p,r)D_(p,r)=0.                                   (5.2)
```

Then

```text
sum_(p,r)D_(p,r)
 <Y(partial_t+partial_u)L,B_p tensor B_r>=0.           (5.3)
```

After primitive Fourier expansion, (5.3) is, up to the fixed Fourier sign,

```text
sum_(p,r)D_(p,r) sum_(a,b)^*
 [Y theta/(pr)] Lhat(-a/p,b/r)=0,

theta=ar-bp.                                          (5.4)
```

Thus an exact coefficient array may be changed by

```text
h_p conjugate(h_r)
 ->h_p conjugate(h_r)+[Y theta/(pr)]D_(p,r),           (5.5)
```

provided the complete primitive packet, its derivative kernel, and all
zero/intersection sectors are retained.

#### Proof

Equation (5.1) makes every tensor `B_p tensor B_r` the same tensor
`A tensor A`; (5.2) proves (5.3).  Fourier differentiation multiplies
`Lhat(-a/p,b/r)` by a constant times

```text
-a/p+b/r=-theta/(pr),
```

which gives (5.4).

This exact identity fails the useful bandwidth test.  Since `p,r asymp Y`,

```text
Y theta/(pr)asymp theta/Y.                            (5.6)
```

On `abs(theta)<=T<<Y`, changing a coefficient by its natural size requires

```text
abs(D_(p,r)) >= (Y/T) abs(h_p conjugate(h_r))          (5.7)
```

for at least the entries being changed.  Every homogeneous projective or
Hilbert ledger therefore pays at least `Y/T`.  At the R84 band
`T=Y^epsilon`, this is `Y^(1-epsilon)`, vastly larger than the available
fixed powers.

At `T asymp Y` the loss disappears, but complete determinant summation is
exactly R82's original physical prime correlation.  No carrier has been
discarded.

## 6. Why square-root primes do not repair the scale

At `p,r asymp sqrt(Y)`, the multiplier in (5.4) would be `asymp theta`,
which is the desired affine normalization.  But (5.1) is then false.  The
exact identity is

```text
B_p=-A+p M_p,

M_p=T(sum_(m<=Y/p)delta_(pm)).                         (6.1)
```

Substituting (6.1) into the left side of (5.3) produces the one-prime cross
terms and the near-square block

```text
sum_(p,r)D_(p,r)pr <Y D L,M_p tensor M_r>.             (6.2)
```

If row and column sums of `D` are chosen to remove the cross terms, (6.2)
remains.  On an interval `I subset [Y,CY]`, choose the R84 bank so that the
product of two distinct bank primes exceeds `sup I`.  Then the multiple
supports `M_p` are pairwise disjoint.  The rectangles
`M_p tensor M_r` are mutually orthogonal, and hence

```text
norm(sum_(p,r)pr D_(p,r) M_p tensor M_r)_HS^2
 asymp Y^3 sum_(p,r)abs(D_(p,r))^2.                    (6.3)
```

In particular, the defect map is injective: `D=0` is the only
coefficient-uniform exact null direction at this scale.  For a counterterm
of the size needed in (5.5), `pr D_(p,r)` has exactly the natural Type-II
size.  Hence the failure of the top-prime null identity at square-root scale
is not a small error: it is the original near-square prime tensor to be
bounded.

This gives the scale dichotomy:

```text
top primes p,r asymp Y:
    exact affine null identity, fatal Y/T coefficient cost;

square-root primes p,r asymp sqrt(Y):
    useful affine normalization, null defect = Type-II carrier. (6.4)
```

The dichotomy also closes the apparent loophole of choosing `D` so that the
defect feeds back into the native reciprocal block.  Its coefficient is of
identity scale, not a contraction; solving for it reproduces the original
R71 estimate.

## 7. Finite falsifiers

The exact arithmetic and affine identities are exercised by
[`natural_mean_affine_falsifier.py`](../src/natural_mean_affine_falsifier.py).
At the default parameters it returns

```text
r=11, k=3:                    mu=-0.1,
unit-mean error:              4.62e-16,
sum abs(e-1)^2:               22,
sum abs(e-mu)^2:               9.9,
random complex split error:   2.48e-16,
compact-piece IBP error:      6.85e-15 relative,
reciprocal transfer error:    7.38e-17,
1/abs(mu) coefficient cost:   10.                       (7.1)
```

A deliberately finite affine-profile stress test uses
`theta=1,...,10`, `H=64`, and `(p,r)=(11,13)`.  Its relative least-squares
residuals are

```text
canonical common dual for Lambda-1:      0.9638,
endpoint unit-mass adversary:             0.9948.       (7.2)
```

These values do not prove an asymptotic lower bound.  They correct the R84
centered-cosine diagnostic by using the native complex phase and show that
its favorable two-moment fit is not stable under this more faithful finite
model.

## 8. Fixed-power verdict

R85 finds a real fixed power, but not for the theorem that would imply a
zero-free strip:

```text
correctly centered, nonresonant reciprocal fluctuation:
    conditional fixed power H^[-(1/40-tau/2)+o(1)], tau<1/20;

Ramanujan mean correction:
    elementary Q^(-1) gain;

canonical residual -gamma:
    full contact scale, no reciprocal phase;

resonances r|k:
    literal axes;

fixed-degree theta counterterms:
    scale-neutral derivative rewrites;

exact top-prime affine gauge:
    power-expensive on the low determinant band;

square-root affine gauge defect:
    the original Type-II carrier.                         (8.1)
```

Therefore no fixed-power bound for the **full** R71 energy has been proved,
and no fixed zero-free strip follows from R85.  The remaining theorem cannot
be coefficient-uniform.  It must exploit the joint prime-derived structure
of

```text
gamma_(p,r,theta)=W(theta/(pr))                        (8.2)
```

together with the native near-square tensor before arithmetic centering or
absolute values separates them.  Equivalently, it must prove a fixed power
for the complete square-root defect (6.2) plus `-gamma` as one signed
operator.  That statement is now the irreducible fixed-strip-strength gate;
another scalar Kloosterman estimate or another finite-moment counterterm
will not reach it.  The finite primitive common-`g` mask, the uniform
B-spline seam ledger, and the natural all-cofactor rectangular limit remain
additional technical interfaces; clearing them alone would still leave this
contact projection.

### R86 successor disposition

R86 keeps the square-root reciprocal tensor and `-gamma` together.  Its
shifted-Ramanujan operator has no reciprocal zero character, so the joint
zero orbit is exactly the canonical carrier.  Canonical whitening supplies
dissipation and Schur leakage but no small parameter, and the actual positive
prime weights give a uniform full-scale residual at prime target points.
Thus a natural Hilbert contraction of the complete square-root block is
closed.  Only the specially weighted all-sector R71 kernel pairing remains
open; see
[`SIGNED-JOINT-RECIPROCAL-COMPRESSION-GATE.md`](SIGNED-JOINT-RECIPROCAL-COMPRESSION-GATE.md).
