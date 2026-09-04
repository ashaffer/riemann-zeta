# Bipartite Blaschke filters versus the arithmetic rows

Status: exact joint interpolation formulation, sharp branch-stability
criterion, exact fixed-finite-list compact construction,
character-independent unrestricted twisted-moment theorem, outer-factor
carrier bound, and quantitative scaling obstruction, 2026-08-12.  The
divisor and cross-leg arithmetic requirements are algebraically compatible
for every fixed list.  No uniform growing-list conditioning theorem,
arithmetic one-square sign, zero-free strip, or new zeta-zero bound is
proved.

## 1. Verdict

The balanced two-leg theorem and prime-power nulling do not compose by a
formal tensor product.  They do, however, admit two exact joint
formulations.

1. If the endpoint branches range over

   ```text
   V_K(q)=span{q,(-partial)q,...,(-partial)^K q},     (1.1)
   ```

   then prime nulling is stable under **every** pair of branches precisely
   when the base autocorrelation has a Hermite zero through order `2K` at
   every active prime offset.  This condition is both necessary and
   sufficient.  Compact positive-definite functions with those Hermite
   zeros exist explicitly, so every fixed branch list and fixed arithmetic
   list can be realized simultaneously.

2. For the actual chosen Blaschke split one need not pay the universal
   Hermite overconstraint.  If `B_R,B_L` are the two inner filters, the
   cross-prime spectrum is twisted by

   ```text
   U(xi)=B_R(i*xi)*conj(B_L(i*xi)).                  (1.2)
   ```

   The exact arithmetic problem is a positive convex moment problem for
   the curve `U(xi)(exp(i*xi*u_j))_j`.  If the retained real characters are
   independent, it has a solution beyond any prescribed lower frequency
   when no upper frequency cap is imposed.  Thus a finite Blaschke split
   creates no abstract positivity obstruction for such a fixed list.
   Opposite offsets may be grouped only when their **full twisted
   equations**, not merely their limiting untwisted characters, are exact
   conjugates.

The scaling obstruction is now precise.  The known central-ray condition
for the untwisted cosine curve does not control the transverse inradius of
the twisted complex moment hull.  An arbitrarily small phase twist can
destroy a ray solution whose convex representation lies on the boundary.
With a polynomial upper frequency cap, the missing datum is a
well-conditioned prime-orbit simplex, or equivalently a positive lower
bound for that transverse inradius.  The compact growing-list problem also
still has to realize two nontrivial inner filters, whose causal inverse
transforms have tails.

There is a cheaper alternative to pointwise nulling.  After one endpoint
leg is fixed, the weighted **cross-leg** prime aggregate is one linear
functional on the other leg.  Its exact carrier loss is a rank-one Schur
complement.  It retains the harmonic-mean carrier exactly unless the
projected aggregate vector aligns with the selected endpoint evaluation.
Same-leg arithmetic terms must still be controlled separately.  No current
zeta-specific estimate bounds the cross-leg angle uniformly.

## 2. The exact joint problem

For compactly supported local envelopes define

```text
F_f(z)=integral f(t)*exp(z*t)dt,
R_(f,g)(u)=integral f(t+u)*conj(g(t))dt.             (2.1)
```

Let `D_R f=0` and `D_L g=0` denote the red and blue endpoint Laplace
conditions from the bipartite coloring.  Let `a_R,a_L` be the selected
endpoint evaluation functionals, after the common exponential displacement
factor `exp(alpha*D/2)` has been removed.  The selected positive-row
condition is

```text
a_R(f)+a_L(g)=0.                                    (2.2)
```

For active cross-prime offsets

```text
u_j=log(n_j/Y_c),          u_j!=0,                  (2.3)
```

pointwise prime nulling is the bilinear system

```text
R_(f,g)(u_j)=0                 (1<=j<=M).            (2.4)
```

Pole cross rows may be appended to (2.4), and repeated offsets must be
grouped before counting.  The cross-leg part of the weighted prime
aggregate instead has the form

```text
A_pr(f,g)=2*Re <g,P_ar f>,
P_ar=sum_j c_j*T_(u_j)+P_pole+P_gamma,              (2.5)
```

with the actual von Mangoldt phases and weights absorbed into `c_j`.
Pointwise nulling is a sufficient overconstraint for this cross part;
aggregate admission asks only for the required sign or size of (2.5).
Equation (2.5) is not the same-leg part of the completed explicit form.

Fix a right-leg direction `f in ker D_R`.  In the left-leg Hilbert space put

```text
E=ker D_L,
v_j=P_E T_(u_j)f,
a=P_E a_L,                                          (2.6)
```

where a functional and its Riesz representer are denoted by the same
letter.  Let `V c=sum_j c_j v_j`, `G=V^*V`, and `b=V^*a`.  The maximum
selected left evaluation after all pointwise prime nulls is exactly

```text
sigma_L(f)^2
 =||P_(ker V^*)a||^2
 =||a||^2-b^*G^dagger*b.                            (2.7)
```

For one complex aggregate equality, replace `V` by its single column
`P_E P_ar f`.  Thus

```text
sigma_agg(f)^2
 =||a||^2
  -|<a,P_E P_ar f>|^2/||P_E P_ar f||^2.             (2.8)
```

The quotient is interpreted as zero when the denominator vanishes.
Equations (2.7)--(2.8) are identities, not estimates.  The actual equality
`Re <g,P_ar f>=0` is only one real constraint: regard `E` as a real Hilbert
space and project the phase-fixed selected real evaluation onto the real
hyperplane orthogonal to `P_E P_ar f`.  It is not (2.8) unless both the real
and imaginary parts of the aggregate are constrained.

If a unit right direction has selected capacity `sigma_R(f)` and the
admissible unit left direction has capacity `sigma_L(f)`, scaling the two
legs to satisfy (2.2), followed by unit normalization, gives

```text
|A|^2
 =exp(alpha*D)
  *[sigma_R(f)^(-2)+sigma_L(f)^(-2)]^(-1),          (2.9)

-Q_selected
 =(2/L^2)*|A|^2.                                    (2.10)
```

This is the same harmonic mean as in the bipartite theorem.  Arithmetic
coupling changes only the two capacities.  Consequently the sharp
aggregate obstruction is not dimension: it is the multiple-correlation
term `b^*G^dagger b` in (2.7), or the angle in (2.8).

The rank-one lift makes the remaining nonconvexity explicit.  With
`Gamma=f tensor conj(g)`, (2.4) and (2.5) are linear conditions on `Gamma`.
The endpoint conditions constrain its two factor ranges.  Positivity of a
larger covariance relaxation does not by itself recover the required
rank-one scalar state.

## 3. Ordinary prime zeros are not filter-stable

The exact differential identity is elementary and decisive.

### Theorem 3.1 (sharp Hermite stability)

Let `q` be smooth and compactly supported and let `P,Q` be polynomials.
Then

```text
R_(P(-partial)q,Q(-partial)q)(u)
 =P(-partial_u)*conj(Q)(partial_u)*R_q(u),           (3.1)

R_q=R_(q,q).                                        (3.2)
```

In particular, for the full branch family `V_K(q)`, the following are
equivalent at a fixed offset `u_0`:

```text
R_(f,g)(u_0)=0 for every f,g in V_K(q);             (3.3)

R_q^(m)(u_0)=0 for every 0<=m<=2K.                 (3.4)
```

#### Proof

Differentiating (2.1) in `u` gives

```text
R_((-partial)^a q,q)=(-partial_u)^a R_q.
```

Integration by parts in the second argument gives

```text
R_(q,(-partial)^b q)=(partial_u)^b R_q.
```

Linearity proves (3.1), and (3.4) proves (3.3).  Conversely choose
monomials of degrees `a,b<=K`.  Every integer from `0` through `2K` is
`a+b` for such a pair, so (3.3) forces (3.4).  QED

Thus a simple positive-spectral zero is not enough.  For example, with

```text
q(t)=t*exp(-t^2/2),
R_q(u)=c*(2-u^2)*exp(-u^2/4),                       (3.5)
```

the autocorrelation vanishes at `u=sqrt(2)` but its derivative does not.
Taking one branch to be `-q'` makes the cross correlation nonzero there.
The displayed example is Schwartz rather than compact.  Multiplying it by
a smooth cutoff tending to one gives convergence of the autocorrelations
in `C^1` near `sqrt(2)`; the simple sign-changing zero and its nonzero
derivative therefore persist at a nearby point for all sufficiently large
cutoffs.  Hence the same counterexample exists in `C_c^infinity`, and
black-box composition with one first-order branch filter is false in the
compact class as well.

The Laplace side is simultaneously simple:

```text
F_(P(-partial)q)(z)=P(z)*F_q(z).                    (3.6)
```

Hence the same differential family which realizes endpoint interpolation
forces exactly the Hermite arithmetic condition (3.4).

## 4. Exact compact Hermite construction

The sharp condition is not an existence obstruction for a finite list.

### Theorem 4.1 (compact positive-definite branch-stable nuller)

Fix nonzero real offsets `u_1,...,u_M` and an integer `K>=0`.  Let `R_0` be
a nonzero smooth compactly supported positive-definite function and set

```text
Phi_(U,K)(u)
 =product_(j=1)^M
   cos^(2*K+2)(pi*u/(2*u_j)),                       (4.1)

R(u)=R_0(u)*Phi_(U,K)(u).                           (4.2)
```

Then:

1. `Phi_(U,K)` and `R` are positive definite;
2. `R` is smooth and has the same compact support as `R_0`;
3. `R^(m)(u_j)=0` for every `j` and `0<=m<=2K+1`;
4. continuous Fejer--Riesz--Krein factorization gives a compact scalar
   `q` with `R=q*tilde(q)`, and `q` may be taken smooth;
5. every two functions in `V_K(q)` have zero cross correlation at every
   `u_j`.

#### Proof

Each cosine is a characteristic function of a symmetric two-point
probability, and products and positive integer powers preserve positive
definiteness.  The even power in (4.1) is also pointwise nonnegative and
has a zero of order `2K+2` at its designated node.  Products preserve that
order or increase it.  Parts 1--3 follow.  The compact factorization theorem
gives `R=q*tilde(q)` with half the difference support.  Since `R` is smooth
and compactly supported, its nonnegative Fourier transform `W` is Schwartz.
The factor has `|Q(xi)|^2=W(xi)`, so `xi^m Q` is in `L^2` for every `m`;
Paley--Wiener and Sobolev embedding therefore give a smooth compact `q`.
This proves part 4, and Theorem 3.1 gives part 5.  QED

If the factor transform vanishes at one of finitely many endpoint
interpolation nodes, a generic modulation avoids that finite set while
preserving every Hermite zero.  Equation (3.6) then reduces the red, blue,
selected, and fixed counterrotating companion equations to ordinary
polynomial interpolation.  With `K` at least the largest branch
interpolation degree, all conjugation-compatible equations and all
cross-prime nulls hold on the same scalar envelope.  Scaling the two
translated legs gives exactly (2.9)--(2.10).  Thus fixed-list cross-leg
arithmetic coupling consumes no additional projection after the Hermite
base has been chosen.

There is an entirely real fixed-list fallback which avoids any issue about
the symmetry of a spectral factor.  Put

```text
delta_U=min_j |u_j|>0                               (4.3)
```

and choose a real smooth seed supported in an interval of diameter less
than `delta_U`, with its Laplace transform nonzero at the finitely many
interpolation nodes.  Such a seed is obtained, for example, by sufficiently
narrow dilation of a real bump of nonzero integral.  Every derivative and
every counterrotating realification has the same support.  Therefore all
standard and anomalous cross correlations vanish at every `u_j`
geometrically.  A sufficiently large derivative family solves each finite
conjugation-compatible endpoint and companion interpolation system by its
confluent Vandermonde matrix.  This gives one exact real compact packet with
the harmonic-mean carrier for every such fixed list.

That fallback is not asymptotically cheap.  For a unit packet supported in
an interval of length `epsilon`, the translation-invariant
Cauchy--Schwarz bound is

```text
|F_q(alpha)*F_q(-alpha)|
 <=sinh(alpha*epsilon)/alpha
 =epsilon+O(alpha^2*epsilon^3),                    (4.4)
```

with the continuous value `epsilon` at `alpha=0`.  Hence support separation
alone retains at most `O(epsilon)` in the selected product.  At a nearest
prime-log gap `epsilon asymp Y^(-1)` this is already a full-power arithmetic
loss, before endpoint interpolation conditioning is counted.

## 5. The exact chosen-filter convex problem

The Hermite construction protects against every branch in `V_K`; it is
usually much stronger than necessary.  In the causal half-line model write

```text
G_R=B_R*H,             G_L=B_L*H,                  (5.1)
```

where `B_R,B_L` are the finite Blaschke products assigned to the two legs.
On the boundary their relative cross spectrum is

```text
U(xi)=B_R(i*xi)*conj(B_L(i*xi)),
|U(xi)|=1,
U(xi)->1                 as |xi|->infinity          (5.2)
```

after one harmless common unimodular normalization.  If
`W(xi)=|H(i*xi)|^2`, the exact pointwise arithmetic constraints are

```text
integral U(xi)*exp(i*xi*u_j)*W(xi)dxi=0.            (5.3)
```

This is the correct joint positive problem.  The untwisted condition
`integral exp(i*xi*u_j)W=0` does not imply (5.3).

To include compact factorization without a hidden atomic-to-smooth error,
fix a smooth compact positive-definite base `R_0`, let `W_0>=0` be its
Fourier transform, and define the **smeared twisted prime curve**

```text
Psi_j(eta)
 =(1/(2*pi))*integral
   U(xi)*W_0(xi-eta)*exp(i*xi*u_j)dxi.              (5.4)
```

For a probability `mu=sum_l a_l delta_(eta_l)`, the spectral density

```text
W_mu(xi)=sum_l a_l W_0(xi-eta_l)                    (5.5)
```

has compact inverse transform

```text
R_mu(u)=R_0(u)*sum_l a_l exp(i*eta_l*u).            (5.6)
```

Equations (5.3)--(5.6) show that exact arithmetic nulling is precisely

```text
sum_l a_l Psi(eta_l)=0,       a_l>=0,
sum_l a_l=1.                                         (5.7)
```

If an aligned atom at `eta=0` is prescribed, write

```text
mu=w_0*delta_0+(1-w_0)*nu,
r=w_0/(1-w_0).                                      (5.8)
```

The exact primal is

```text
-r*Psi(0) belongs to
conv{Psi(eta):eta in Omega}.                        (5.9)
```

Splitting complex coordinates into real and imaginary parts, its exact
separation dual is

```text
sup_(eta in Omega) <lambda,Psi_R(eta)>
 +r*<lambda,Psi_R(0)> >=0
for every real lambda.                              (5.10)
```

Here `Psi_R` denotes the realification of the complex vector.  Formula
(5.9), rather than the untwisted cosine ray, is the joint convex program
which should be computed.

### Theorem 5.1 (fixed-list unrestricted twisted compatibility)

Assume that the real functions

```text
{cos(xi*u_j),sin(xi*u_j):1<=j<=M}                  (5.11a)
```

are linearly independent.  Equivalently, the retained `u_j` are nonzero
and pairwise distinct up to sign.  Choose a smooth compact
positive-definite `R_0` with `R_0(u_j)!=0`.  For every `R>0` there is a
finite positive measure of the form (5.8), with `w_0>0` and every atom of
`nu` larger than `R`, which solves (5.7).  Consequently the two finite
Blaschke branches and every such fixed prime-offset list can be realized
simultaneously in the causal positive-spectral model.

More generally one may first delete exact real-linear redundancies of the
**full** curve `Psi`.  It is not valid to delete an opposite offset merely
because the limiting untwisted characters are conjugate: for nontrivial
`U`, the two equations in (5.3) need not be conjugates.

#### Proof

Because `R_0` is smooth and compactly supported, `W_0` is Schwartz and in
`L^1`.  After changing variables `xi=eta+x`, the bound
`|U(eta+x)-1|*W_0(x)<=2*W_0(x)` permits dominated convergence and gives

```text
Psi_j(eta)
 =R_0(u_j)*exp(i*eta*u_j)+o(1)       (eta->infinity). (5.11)
```

The closure of every positive tail of the scalar orbit is the same compact
subgroup generated by the characters.  Haar measure on that subgroup has
zero mean in every nontrivial character.  Character orthogonality and
(5.11a) say that the retained real and imaginary coordinate functions are
linearly independent in Haar `L^2`.  If zero were on the boundary of their
convex hull, a
nonzero real linear combination of those functions would be nonnegative
everywhere and have Haar integral zero.  It would therefore vanish
identically, contradicting that independence.  Thus zero lies in the
interior.  Multiplication by the invertible realified diagonal
`R_0(u_j)` preserves interior.  Moreover (5.11) is uniform on a sufficiently
late tail.  The support-function perturbation bound therefore puts a fixed
ball about zero inside the convex hull of that subtail of `Psi`.

It consequently contains a relative ball about zero.  A sufficiently small
negative multiple of the fixed vector `Psi(0)` lies in that ball, which is
(5.9) for some `r>0`.  Approximating an interior simplex by actual tail
orbit points and adjusting its barycentric weights makes the representation
exact; Caratheodory then gives a finite atomic `nu`.  The density (5.5) is
nonnegative and is the Fourier transform of the smooth compact function
(5.6), so Krein factorization supplies a smooth compact scalar base `H`.
QED

The aligned atom retains the bilateral compact-autocorrelation carrier:

```text
integral R_mu(u)*exp(alpha*u)du
 =w_0*C_0(alpha)+O_(A,R_0)(R^(-A)),                 (5.12)
```

where `C_0(alpha)=integral R_0(u)*exp(alpha*u)du`, the other atoms are
beyond `R`, and `alpha` ranges in a fixed compact set.  There is also a
direct causal endpoint bound, which is the needed justification for the
harmonic-mean claim.  Let `H_0,H` be the minimum-phase outer Krein factors
of `W_0,W_mu`, with the same boundary-norm convention.  Since

```text
W_mu(xi)>=w_0*W_0(xi),                              (5.13)
```

the outer Poisson formula for `log|H|` gives

```text
log(|H(alpha)|^2/|H_0(alpha)|^2)
 =(1/pi)*integral_R
   [alpha/(alpha^2+xi^2)]*log(W_mu(xi)/W_0(xi))dxi
 >=log w_0,

|H(alpha)|^2>=w_0*|H_0(alpha)|^2.                  (5.14)
```

Real-axis zeros are harmless because their logarithms are locally
integrable; equivalently one obtains (5.14) by the standard outer-factor
approximation.  Inner multiplication preserves the two boundary norms and
attenuates the selected endpoint evaluations by `|B_R(alpha)|` and
`|B_L(alpha)|`.  After common normalization, the causal carrier is at
least

```text
w_0*|H_0(alpha)|^2
 *[|B_R(alpha)|^(-2)+|B_L(alpha)|^(-2)]^(-1).      (5.15)
```

Thus every fixed character-independent list retains the same one-product
divisor exponent in the causal model.  This statement uses the outer
factor; (5.12) alone controls a bilateral product and would not by itself
control the individual causal evaluation.

The theorem deliberately has no polynomial upper bound on its atoms and no
growing-list lower bound on `w_0`.  It also does not turn a nontrivial inner
factor into an exactly compact endpoint branch: a finite Blaschke factor
has a causal tail.  For a fixed list the compact Hermite construction in
Section 4 gives an exact scalar fallback.  Uniformly retaining the
Blaschke-sharp carrier while truncating two growing inner cascades and
preserving (5.7) is still open.

## 6. The conditioning invariant for a finite band

For a capped band `Omega=[-T,-Y] union [Y,T]`, define

```text
K_(U,T)=conv{Psi_R(eta):eta in Omega},
E_(U,T)=span_R{Psi_R(eta):eta in Omega},
rho_(U,T)=sup{rho>=0:rho*B_(E_(U,T))
                         subset K_(U,T)}.           (6.1)
```

Thus the ball is centered at zero and taken in the real linear span.  If
`rho_(U,T)>0`, if `Psi_R(0)` belongs to that span, and if

```text
r*||Psi_R(0)||<rho_(U,T).                           (6.2)
```

then (5.9) is feasible.  This is the needed transverse inradius.  If the
central vector has a component outside `E_(U,T)`, no positive `r` is
feasible; a central-ray lower bound alone does not control either issue.

There is a useful perturbative form.  If, in one common real span, an
untwisted moment hull contains a ball of radius `rho`, and its twisted curve
differs uniformly by at most `epsilon`, then support functions show that the
twisted hull contains the ball of radius

```text
max(rho-epsilon,0).                                 (6.3)
```

For one Blaschke factor with root `z=beta+i*delta`,

```text
|(i*xi-z)/(i*xi+conj(z))-1|
 =2*beta/|i*xi+conj(z)|.                            (6.4)
```

Thus, away from all root ordinates and for a finite product,

```text
sup |U(xi)-1|
 <=sum_roots 2*beta/|i*xi+conj(z)|.                 (6.5)
```

For fixed roots and `|xi|>=Y`, this is `O(Y^(-1))`.  Hence a genuinely
interior finite-band prime simplex is stable under every fixed branch
split.  What is not known is a uniform lower bound for its inradius, or a
polynomial-height return producing such a simplex.

The need for an inradius is sharp.  In one abstract coordinate the
untwisted convex set consisting of the point `-1` cancels a central `+1`.
Rotating the remote point to `-exp(i*epsilon)` destroys exact cancellation
for every nonzero `epsilon`, however small.  The original solution had
zero transverse margin.  This is exactly what a ray-only estimate fails to
exclude.

For an explicitly chosen atomic simplex, (6.1) can equivalently be replaced
by its barycentric conditioning.  Choose coordinates in its affine span,
let `A` be the square augmented real matrix whose columns are
`(1,Psi_R(eta_l))`, let `a=A^(-1)(1,0)`, and let `Delta A` be a perturbation.
Put

```text
kappa=||A^(-1)||*||Delta A||.                       (6.6)
```

If `kappa<1`, the perturbed weights obey

```text
||a_new-a||_2
 <=[kappa/(1-kappa)]*||a||_2.                       (6.7)
```

They therefore remain positive whenever the right side is less than
`min_l a_l`.  (For an overcomplete representation one first extracts a
simplex or uses a chosen right inverse with the analogous bound.)  This is
the finite-dimensional quantity to audit numerically; atom count alone
gives no such estimate.  The shorter condition previously suggested by
`||A^dagger||*epsilon<min a_l` omits the Neumann denominator and is not, by
itself, sufficient.

## 7. Why the universal repair does not yet scale

The Hermite theorem supplies an exact rank ledger.  If the compact Gabor
autocorrelation is a nonzero trigonometric polynomial of degree `J`, let
`N` be the number of distinct forced nodes modulo its period, including
the Hermitian reflections `-u_j` and grouping all collisions.  Multiplicity
`2K+1` then requires

```text
N*(2K+1)<=2*J.                                      (7.1)
```

This is just the zero count with multiplicity and is necessary for the
universal branch-stable architecture.  Writing `M` in (7.1) is valid only
when `M=N`; if the listed nodes contain only one sign, autocorrelation
symmetry can make `N` larger.

The explicit factor (4.1) has spectral radius at most

```text
B_(U,K)
 =(K+1)*pi*sum_j 1/|u_j|,                           (7.2)
```

and its displayed central atom has weight at least

```text
[binom(2K+2,K+1)/4^(K+1)]^M.                       (7.3)
```

Other frequency collisions can only add mass at zero.  Equations
(7.1)--(7.3) are not a no-go for a better Hermite moment solution, but they
show why independent product factors are badly conditioned when both the
prime list and branch degree grow.

Taking a fixed power of a subpower carrier is still subpower, so a fixed
branch degree creates no exponent obstruction in a tensor implementation
whose compact carrier transfer is otherwise controlled.  For the intended
divisor application, however, the ungrouped branch degree can be `Theta(L)`.
Raising one ordinary null factor to the required order, or multiplying one
repair per branch cell, then incurs a growing power and does not retain the
one-product exponent.  The chosen-twist program (5.9) avoids this universal
overconstraint and is therefore the only positive-spectral version worth
scaling.

The aggregate program is cheaper still: the real-Hilbert variant following
(2.8) spends one real direction, not one condition per prime power.  The
complex equality in (2.8) spends two real directions.  A sufficient
remaining theorem is the zeta-specific angle estimate

```text
|<P_E a_L,P_E P_ar f>|^2
 <=(1-X^(-o(1)))*||P_E a_L||^2*||P_E P_ar f||^2,   (7.4)
```

or a stronger favorable-sign estimate.  Generic Hilbert-space geometry,
global zero counts, and the existence of a large kernel do not imply
(7.4).

## 8. Research decision

The fixed-list question is settled positively, but three different scales
must not be conflated.

| assertion | verdict |
|---|---|
| ordinary prime-null autocorrelation survives arbitrary endpoint filtering | **false**, already for one derivative |
| Hermite zeros through order `2K` are sufficient for degree-`K` branches | **proved** |
| that Hermite order is necessary for stability over the whole branch family | **proved** |
| every fixed branch list and fixed cross-prime list have an exact compact scalar realization | **proved** |
| every fixed conjugation-compatible real list has an exact real realization | **proved by support separation**, with a fixed-power scaling loss |
| a fixed Blaschke split is compatible with positive spectral moments beyond any lower frequency | **proved without an upper cap under retained-character independence** |
| the causal chosen-filter construction retains the one-product harmonic-mean ledger | **proved in that scope, using the outer-factor bound (5.14)** |
| untwisted central mass alone transfers uniformly through the branch twist | **false without a transverse margin** |
| a polynomial-band twisted inradius of size `Y^(-o(1))` is known | **no** |
| two growing Blaschke cascades have a joint compact prime-null transfer with `X^o(1)` loss | **open** |
| the completed cross-leg aggregate has a uniform favorable Schur angle | **open** |
| a zero-free strip follows | **no** |

The next arithmetic computation should therefore solve (5.9) for the actual
balanced branch twist and report both the optimized aligned mass and the
smallest singular value/barycentric margin of the active simplex.  The next
analytic theorem should target either that transverse inradius or the
single aggregate angle (7.4).  Reusing an untwisted central-ray solution as
a black-box factor is not a viable proof step.
