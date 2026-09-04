# R120 primitive Mobius Mellin-kernel gate

Status: the primitive transform in R116 is normalization-correct on its
stated balanced squarefree semiprime support.  Its main kernel can be
Poisson-summed all the way back to the original `Q_h` Gram kernel.  The
result is a smooth periodized ratio kernel with zero **additive** mean, but
with a generically nonzero low **log-Mellin** spectrum.  After exact Vaughan
recompletion on both cofactor variables, the balanced-packet primitive term has
a Hermitian Mellin-diagonal representation with signed `-mu(n)log n` and
coprimality coefficients.  This does not furnish a positive Gram theorem for
the isolated packet, but it also does not by itself prove actual
indefiniteness.  The Type-I heads replace the truncated convolutions by
`-mu log` and kill the evaluated center, but they neither delete this
primitive term nor its low Mellin modes.  Vinogradov--Korobov gives the
usual subpower gain.  A fixed power for the complete all-class fixed-window
detector bank is precisely fixed-zero-free-strip strength.  No fixed strip, and no
failure of every fixed strip, is proved here.

Date: 2026-08-07.

**2026-09-02 successor correction (R128/S0 audit).**  The primitive object
in this report remains one isolated balanced-semiprime packet with a
signed-coefficient representation; completing its
Vaughan coefficients does not restore the omitted conductor, gcd, profile,
orientation, and modulus classes.  R128 later restores all of those classes
exactly.  That all-class family is the faithful positive detector currently
proved, and it is exactly the original R71 energy.  Consequently the strip-equivalence
statements below apply after this all-class restoration, not to a
primitive/head bank by itself.

Predecessors:

* [`R116-SIGNED-JOINT-TYPEII-ATTACK.md`](R116-SIGNED-JOINT-TYPEII-ATTACK.md)
  for the conductor collapse and primitive transform;
* [`R105-QH-VAUGHAN-TAIL-NATIVE-BRIDGE-AUDIT.md`](R105-QH-VAUGHAN-TAIL-NATIVE-BRIDGE-AUDIT.md)
  for the two balanced Vaughan factors;
* [`R104-QH-FINITE-COFACTOR-SECTOR-THEOREM.md`](R104-QH-FINITE-COFACTOR-SECTOR-THEOREM.md)
  for exact two-sided Vaughan recompletion; and
* [`R102-CENTER-ANNIHILATED-OFF-AXIS-GATE.md`](R102-CENTER-ANNIHILATED-OFF-AXIS-GATE.md)
  for the two `Q_h` moments and detector nonvanishing at every zeta zero.

## 1. Verdict

There are two superficially similar frequency statements, and confusing
them would give a false proof.

For the R116 kernel,

```text
Phi(x)=sum_(m,nu in Z) What(m,nu)e(-m nu x),           (1.1)
```

the `Q_h` marginal gives

```text
mean_(x mod 1) Phi(x)=0.                              (1.2)
```

This is additive cancellation at frequencies `m nu !=0`.  The global
Vaughan variables, however, see `x=n/c` multiplicatively.  Their relevant
coefficient is of the shape

```text
int chi(x)Phi(x)x^(-i tau) dx/x,                      (1.3)
```

or, after Hermitian normalization, the same integral with an additional
factor `x^(-1/2)`.  Neither is forced to vanish at `tau=0`, or on any
interval of `tau`, by (1.2).

After restoring both Vaughan heads, put

```text
C(n)=(mu*Lambda)(n)=-mu(n)log n.                      (1.4)
```

In the `g=1` normalization of R113--R116, the primitive main term is a
finite sum of forms

```text
P_X(t)=sum_(c,n asymp X)
 (1_((c,n)=1))C(c)C(n)c^(-it)n^(-1-it)
 Phi_(lambda)(n/c),                                   (1.5)
```

with smooth dyadic weights understood and with a bounded projective family
of fixed-ratio parameters `lambda`.  If the coprimality projector is first
removed (or all exact common-divisor sectors with the same frozen kernel
are summed), then at `t=0` one frozen ratio profile has the exact Mellin
diagonalization

```text
P_X(0)=1/(2pi) int_R lambda_P(tau)
             abs[sum_(n asymp X)
                 C(n)n^(-1/2)w(n/X)n^(i tau)]^2 d tau. (1.6)
```

Here `lambda_P` is real after the ordered pair and its conjugate orientation
are combined.  The generic Gram and marginal hypotheses do not force it to
be nonnegative, but nonnegativity of the actual profile is unclassified.
With the actual `g=1`
coprimality projector, (1.6) is replaced by an exact Mobius-weighted sum of
such squares; see (6.6) below.  Thus the primitive block has two layers of
signed coefficients, not a new proved positive energy.  The formula alone
does not witness an actual negative value.  Positivity is proved for the
complete reconstruction after all conductor pieces are put back; that
reconstruction is the original R71 Gram square.

The exact structural ledger is therefore

```text
R116 primitive normalization, c=pr balanced          CORRECT;
inverse Poisson formula for Phi                       EXACT;
additive constant mode                                ZERO;
low log-Mellin modes                                  PRESENT GENERICALLY;
two-sided Vaughan recompletion                        C=-mu log;
primitive quadratic form                              HERMITIAN / POSITIVITY UNPROVED;
Type-I cancellation of primitive low mode             ABSENT;
known bound                                            VK SUBPOWER;
uniform fixed power for a separating detector bank    FIXED-STRIP STRENGTH.
                                                               (1.7)
```

## 2. Audit of R116 Theorem 5.1

Keep the Fourier convention

```text
What(xi,eta)=double_integral W(sigma,tau)
             e(-xi sigma-eta tau)d sigma d tau.       (2.1)
```

For `c=pr`, `(p,r)=1`, R116 defines

```text
gamma_c(z)=sum_(db=z mod c)alpha_d beta_b,
F_c(a)=sum_z^* gamma_c(z)e_c(a inverse(z)),            (2.2)

V_c(a)=sum_(m,nu in Z)What(m,nu)S_c(m,nu a;c).        (2.3)
```

There is no missing factor of `c` in (2.3).  Indeed, splitting the lattice
by `j=x mod c`, `theta=a inverse(x) mod c` and applying Poisson to the two
unit-spaced translated grids gives (2.3) directly.

After inserting (2.2)--(2.3), the sum over `a` is

```text
H_c(m,nu;z)
 =sum_x^* e_c(mx)c_c(inverse(z)+nu inverse(x)).        (2.4)
```

The local prime calculation is exact.  Up to the harmless CRT scaling of
`m` in the additive character,

```text
H_p=p e_p(-m nu z)-c_p(m).                            (2.5)
```

Consequently CRT gives

```text
H_c(m,nu;z)
 =c e_c(-m nu z)
  -p e_p(-m nu z inverse(r))c_r(m)
  -r e_r(-m nu z inverse(p))c_p(m)
  +c_p(m)c_r(m).                                      (2.6)
```

The exact CRT phase representatives in the two cross terms do not affect
their sizes.  Formula (2.6) proves both the main coefficient `c` and its
sign.  It also gives

```text
abs[H_c-c e_c(-m nu z)]
 <<p(r,m)+r(p,m)+(p,m)(r,m).                          (2.7)
```

The second Fourier support is fixed and avoids `nu=0`; for large `p,r`,
therefore, `(nu,c)=1` and the solution `x=-nu z` used in (2.5) is a unit.
The first marginal kills `m=0`.  If `p|m` or `r|m`, then `abs(m)>=min(p,r)`
and the rapid first-frequency decay of `What` absorbs an arbitrary power of
that prime.  Summing (2.7) hence gives

```text
sum_(m,nu)abs What(m,nu)
 abs[H_c(m,nu;z)-c e_c(-m nu z)]
 <<c^(1/2+epsilon),                                   (2.8)
```

uniformly when `p,r asymp sqrt(c)`.  Finally

```text
norm(gamma_c)_1
 <=norm(alpha)_1 norm(beta)_1<<c^epsilon              (2.9)
```

for the actual square-root Vaughan coefficients.  This verifies R116
Theorem 5.1, including the error normalization.

There are two scope restrictions worth retaining.

1. The square-root error in (2.8) uses `c=pr` with both primes balanced.  It
   must not be quoted unchanged for an arbitrary many-prime squarefree
   modulus.
2. In a frozen profile, (1.1) has no arithmetic dependence on `c`.
   R116's subscript in `Phi_c` records the smooth fixed-ratio/scaling family,
   not an arbitrary coefficient sequence indexed by `c`.  Corollary 3.2 of
   R116 supplies an absolutely summable vector-valued separation for this
   family.

## 3. Poisson summation back to the Gram kernel

Let

```text
W(sigma,tau)=int_R L(y+sigma,y)e(tau y)dy,             (3.1)
```

where `L` is the scaled `Q_h` Gram kernel.  Direct integration in `tau`
gives R116 (2.4):

```text
What(xi,eta)=e(xi eta)int_R L(t,eta)e(-xi t)dt.        (3.2)
```

At the integer arguments in (1.1), `e(m nu)=1`.  Applying the Dirac-comb
form of Poisson summation in `m` now gives the exact inverse formula

```text
Phi(x)
 =sum_(nu in Z)sum_(ell in Z)L(ell-nu x,nu).          (3.3)
```

Only finitely many `nu` occur, and only finitely many `ell` occur on a
fixed ratio interval.  Thus (3.3) is an ordinary locally finite smooth sum,
not merely a distributional identity.  In terms of

```text
L(t,u)=int psi(R)f_R(t)conjugate[f_R(u)]dR,            (3.4)
```

it is

```text
Phi(x)=int psi(R)sum_nu conjugate[f_R(nu)]
                    sum_ell f_R(ell-nu x)dR.          (3.5)
```

This is a cross-sampling operator on the Gram vectors.  It is not a norm
square: one argument lies on the integer lattice and the other on the
`x`-dependent affine lattice `ell-nu x`.

Equivalently, `Phi` has the rapidly convergent Fourier series

```text
Phi(x)=sum_(k!=0) A_k e(-kx),
A_k=sum_(m nu=k)What(m,nu),
abs(A_k)<<_A(1+abs(k))^(-A).                          (3.6)
```

The exclusion of `k=0` follows because `nu=0` is outside physical support
and `What(0,nu)=0`.  Formula (3.6) proves that `Phi` is smooth,
one-periodic, and

```text
int_0^1 Phi(x)dx=0.                                   (3.7)
```

The same conclusion follows from (3.3): for each positive integer `nu`,
the intervals `[ell-nu,ell]` cover the real line with multiplicity `nu`,
and the Jacobian is `1/nu`; the first marginal of `L` then vanishes.

This identifies exactly what the primitive transform has done.  It
periodizes the original center-annihilated Gram kernel along rational-slope
lattices.  It does not introduce high asymptotic oscillation: the first
surviving additive frequencies `k=plusminus1,plusminus2,...` make only a
bounded number of turns as `n/c` ranges over a fixed ratio box.

## 4. Additive nullity is not Mellin nullity

Let `chi` be a smooth cutoff to one fixed ratio interval and put

```text
kappa_chi(tau)
 =int_0^infinity chi(x)Phi(x)x^(-i tau)dx/x.           (4.1)
```

Then

```text
chi(n/c)Phi(n/c)
 =1/(2pi)int_R kappa_chi(tau)(n/c)^(i tau)d tau.       (4.2)
```

All derivatives of `kappa_chi` decay rapidly, so (4.2) is an exact
continuous projective-rank decomposition.  Truncating it to error `X^-A`
costs only a subpower number/projective norm of separated factors.  Thus the
primitive kernel has low log-Mellin rank; it has not created a random
two-dimensional Mobius tensor.

At zero Mellin frequency, (3.3) gives

```text
kappa_chi(0)
 =sum_(nu,ell)int L(t,nu)
   chi((ell-t)/nu) dt/(ell-t),                        (4.3)
```

where only cells with `(ell-t)/nu>0` are retained.  The weight
`chi((ell-t)/nu)/(ell-t)` is not constant in `t`.  Therefore

```text
int L(t,nu)dt=0                                       (4.4)
```

does not annihilate (4.3).

R102 in fact gives the stronger one-variable identities

```text
int f_R(t)dt=0,
int f_R(t)log(t)dt=0.                                 (4.5)
```

They make the corresponding Mellin transform of `f_R` vanish to second
order at the pole mode.  They still do not kill (4.3), whose lattice-cell
weight is reciprocal-affine rather than `1` or `log t`.  In Fourier
language, (4.5) controls derivatives at the deleted continuous axis
`m=0`; (3.6) samples the remaining integers `m!=0`.

Summing all fixed-ratio shells does not repair this mismatch.  If
`sum_j chi_j=1` on the active ratio range, then the sum of (4.3) merely
replaces `chi_j` by that active dyadic weight.  Even over complete additive
periods, (3.7) is an identity for `dx`; the raw Mellin measure is `dx/x`,
and the Hermitian quadratic normalization below uses `x^(-1/2)dx/x`.
Neither weight is constant on an additive period.

There is also an exact coboundary calculation.  By (3.7), choose a smooth
one-periodic primitive `Psi` with `Psi'(x)=Phi(x)`.  In logarithmic
coordinates `x=exp u`,

```text
Phi(exp u)=exp(-u)d/du[Psi(exp u)].                    (4.7)
```

Thus the raw Mellin kernel and the Hermitian-normalized kernel satisfy

```text
Phi(exp u)
 =d/du[exp(-u)Psi(exp u)]+exp(-u)Psi(exp u),

exp(-u/2)Phi(exp u)
 =d/du[exp(-3u/2)Psi(exp u)]
  +(3/2)exp(-3u/2)Psi(exp u).                         (4.8)
```

After the shell partition is summed, internal boundary terms cancel.  The
remaining Mellin multipliers contain respectively the factors `1+i tau`
and `3/2+i tau`, neither of which vanishes for real `tau`.  Hence the
additive coboundary leaves a nonzero mass term in multiplicative
coordinates; no antisymmetry survives the Jacobian and the `n^(-1)`
normalization.

There is no hidden algebraic identity forcing these coefficients to zero.
For a legal profile, take a sufficiently narrow nonzero smooth input bump
`V`, form its three separated `Q_h` translates, and choose the scale so
that exactly one translate contains an integer second-coordinate sample
`nu`.  On a small ratio cell, (3.5) then contains a single nonzero Gram
cell.  Varying the bump location makes (4.3) a nonzero continuous
functional; cancellation at every location would force that Gram cell,
and hence the bump, to vanish.  Narrow smooth approximations preserve the
two identities (4.5), which are automatic after applying `Q_h`.  Thus even
the sum over all cells has a generically nonzero low Mellin coefficient.

For the actual detector family one does not need to trust genericity.  The
multiplier on a zero term is

```text
q_h(rho-1/2)
 =[exp(h(rho-1/2))-exp(h/2)]^2,                       (4.6)
```

which is nonzero for every nontrivial zeta zero because zeta has no zero on
`Re(s)=1`.  Mellin transforms of nonzero compact profiles are analytic and
have only discrete zeros.  The recorded dilation/modulation detector bank
therefore has no common Mellin zero at a zeta zero.  An isolated zero of one
particular `kappa_chi` is harmless; uniform cancellation of the whole bank
is impossible without making the detector zero.

## 5. Exact Vaughan recompletion on both variables

For cutoffs `U,V`, write

```text
A_(U,V)(q)
 =sum_(db=q;d>U,b>V)mu(d)Lambda(b).                   (5.1)
```

The outer coefficient in R105 is `h(q)=A_(U,V)(q)/q`.
R116's primitive factor `c` therefore changes the outer coefficient into
`A_(U,V)(c)`, while the unfolded inner coefficient remains
`A_(U,V)(n)/n`, with the recorded Mellin phases.  The primitive tail-tail
term is consequently

```text
sum_((c,n)=1) A_(U,V)(c)A_(U,V)(n)
 c^(-it)n^(-1-it)Phi(n/c).                            (5.2)
```

This is the `g=1` block.  Other common-divisor blocks have coefficients
`A_(U,V)(gc),A_(U,V)(gn)` and correspondingly rescaled kernels.

The exact complementary sequence is the sum of the three Vaughan heads

```text
mu_(<=U)*log + Lambda_(<=V)
 -mu_(<=U)*Lambda_(<=V)*1.                            (5.3)
```

Adding it before estimating gives, coefficient by coefficient,

```text
A_(U,V)+(three heads)=mu*Lambda=-mu log=C.             (5.4)
```

Doing this on **both** the outer and inner variables turns (5.2), together
with its tail-head, head-tail, and head-head companions, into (1.5).  This
is a recompletion, not an extra cancellation theorem.

The balanced semiprime family makes the point particularly sharply.  If
`q=p r`, `p!=r`, and both primes exceed both cutoffs, then

```text
A_(U,V)(q)=-log p-log r=-log q=C(q).                  (5.5)
```

Every head coefficient is zero there.  Hence no Type-I head can cancel the
primitive leading piece on this substantial top family.

At field level, R102 evaluates the heads as

```text
exp(R/2)(alpha+beta R)+periodic-Euler defect.          (5.6)
```

`Q_h` kills the displayed rank-two center and leaves the Euler defect in
its previously controlled class.  It does not kill the unevaluated head
coefficient term by term, and it does not alter `Phi`'s Mellin spectrum.
Deleting the heads rather than using (5.4) would therefore be invalid.

## 6. Mellin diagonalization and sign

Set `t=0` first, use the same real dyadic cutoff `w` on both variables, and
suppress a fixed ratio parameter.  First omit the `g=1` coprimality
projector and put

```text
b_X(n)=C(n)n^(-1/2)w(n/X),
k(u)=exp(-u/2)Phi(exp u).                              (6.1)
```

Then the unrestricted ordered primitive sum is

```text
P_X=sum_(c,n)b_X(c)b_X(n)k(log(n/c)).                 (6.2)
```

Only the Hermitian part contributes to the real quadratic scalar:

```text
k_H(u)=1/2[k(u)+conjugate(k(-u))],
k_H(-u)=conjugate(k_H(u)).                            (6.3)
```

After inserting the ratio cutoff, let

```text
lambda_P(tau)=int_R k_H(u)e(-tau u/(2pi))du.          (6.4)
```

With the equivalent angular-frequency convention, Fourier inversion gives
exactly (1.6).  In particular, this unrestricted primitive form is positive
semidefinite if and only if

```text
lambda_P(tau)>=0 for every real tau.                  (6.5)
```

The actual `g=1` term has `(c,n)=1`.  Mobius inversion of that projector
gives the exact refinement

```text
P_X^(g=1)
 =1/(2pi)int_R lambda_P(tau)
    sum_(d>=1)mu(d)abs[B_(d,X)(tau)]^2d tau,           (6.6)

B_(d,X)(tau)
 =sum_a b_X(da)a^(i tau).                             (6.7)
```

The dyadic cutoff in `b_X(da)` makes the `d` sum finite.  Therefore
coprimality introduces a second signed multiplier `mu(d)`; the displayed
representation does not create or prove positivity.  Exact gcd sectors partition all pairs.  If their
scaled kernels happened to be identical, summing every gcd would remove
the projector and recover (1.6).  In the actual R81 identity the kernels
also depend on `g` through `L(u+gj,u)` and its scaling, so this simplification
is not available before the recorded fixed-ratio separation.

The Gram positivity of `L` does not imply (6.5).  Formula (3.5) is a cross
sample, and Theorem 5.1 kept the top Ramanujan divisor while discarding its
proper-divisor companions.  This operation is not an orthogonal
projection.

One can see the failure without arithmetic coefficients.  Take a real
rank-one positive Gram kernel `L(t,u)=f(t)f(u)` with both required marginal
moments zero and with second-coordinate support containing only the integer
`nu=1`.  On a ratio interval near one, arrange the support so that

```text
Phi(x)=f(1)f(2-x).                                    (6.8)
```

Disjoint smooth bumps allow `f(1)=1` while `f(2-x_0)` and
`f(2-1/x_0)` are both negative with arbitrarily large magnitude; two
additional disjoint bumps enforce the two moment constraints without
changing these values.  The two-scale Hermitian matrix at ratio `x_0` then
has positive diagonal and an off-diagonal larger in magnitude than its
geometric mean, so its determinant is negative.  The same construction can
be made after `Q_h` by starting with separated input bumps and smoothing.
Thus Gram positivity plus the exact `Q_h` marginals is insufficient to make
the primitive main term positive.

For nonzero R113 Mellin parameter `t`, a single orientation gives the cross
form

```text
1/(2pi)int kappa(tau)B_X(t+tau)B'_X(t-tau)d tau,      (6.9)
```

with the harmless convention-dependent conjugation in `B'`.  Pairing the
conjugate orientation restores a Hermitian spectral form with signed
coefficients.  It does not settle the sign of the actual constrained form.

By contrast, if every conductor class and every Vaughan component is
restored, the exact kernel is

```text
K_full(q_1,q_2)
 =sum_(m_1,m_2>=1)L(q_1m_1,q_2m_2),                  (6.10)
```

and

```text
sum_(q_1,q_2)C(q_1)C(q_2)K_full(q_1,q_2)
 =int psi(R)abs[sum_q C(q)sum_m f_R(qm)]^2dR>=0.      (6.11)
```

The proper-conductor terms omitted from (6.2) are part of the exact
reconstruction.  This is why positivity may not be imported from (6.11)
back into the primitive block.  R124 supplies exact positive low-frequency
information and D-rated evidence of full-shell sign change, not a certified
negative spectral witness.

## 7. What estimates the Mellin form actually gives

Define the smooth Mobius-log polynomial

```text
B_(X,w)(tau)
 =sum_n -mu(n)log(n)n^(-1/2)w(n/X)n^(i tau).          (7.1)
```

Since

```text
sum_n -mu(n)log(n)n^(-s)=(1/zeta(s))',                (7.2)
```

the classical zero-free region and contour shift give, uniformly on every
fixed `tau` interval,

```text
B_(X,w)(tau)
 <<X^(1/2) exp{-C(log X)^(3/5)(loglog X)^(-1/5)}.     (7.3)
```

The rapid decay of `lambda_P` handles large `tau`.  Substitution in (1.6)
therefore gives the unrestricted estimate

```text
P_X
 <<X exp{-C'(log X)^(3/5)(loglog X)^(-1/5)}.          (7.4)
```

The same exponent holds for the coprime form (6.6).  For squarefree `d`,
multiplicativity gives `B_(d,X)` a factor `d^(-1/2)` and a Mobius sum of
length `X/d`, with the finitely removed Euler factors `p|d`.  The
zero-free-region estimate is uniform up to `d^epsilon`, so, with the usual
harmless adjustment when `X/d` is short,

```text
abs B_(d,X)(tau)
 <<X^(1/2)d^(-1+epsilon)
   exp{-C(log X)^(3/5)(loglog X)^(-1/5)}.             (7.4a)
```

The squares are summable in `d`.  Coprimality changes the sign structure,
but not the best known exponent.

This is the honest unconditional gain furnished by the global
recombination.  It is `X^(1-o(1))`, not `X^(1-delta)`.

The zero additive mean does not improve (7.3).  Expanding (3.6) asks for
Mobius sums twisted by `e(k n/c)` with fixed nonzero `k`.  On an interval of
length comparable to `c`, this phase makes only `O(abs(k))` turns.  The
small `k` coefficients survive, while the large `k` coefficients are
already rapidly decaying.  Discrete integration by parts using a periodic
primitive of `Phi` merely moves a difference onto `mu(n)log n`; it supplies
no controlled factor `X^-delta`.

If zeta has a fixed strip

```text
sup_rho Re(rho)<=1-eta,                               (7.5)
```

then shifting (7.2) to `Re(s)=1-eta+epsilon` gives

```text
B_(X,w)(tau)<<X^(1/2-eta+epsilon),                    (7.6)
P_X<<X^(1-2eta+epsilon).                              (7.7)
```

Conversely, a zero `rho=beta+i gamma` contributes to a suitable member of
the modulated detector bank at size

```text
X^(beta-1/2)q_h(rho-1/2),                             (7.8)
```

up to logarithmic factors for multiplicity.  Its positive localized energy
has exponent `2beta-1`.  Because (4.6) is nonzero and the bank has no common
Mellin zero, a uniform theorem

```text
complete separating all-conductor/all-profile family
       <<X^(1-delta)                                  (7.9)
```

that is strong enough to reconstruct the corresponding Hermitian detector
energy forces

```text
2beta-1<=1-delta,
beta<=1-delta/2                                      (7.10)
```

for every zeta zero.  This is the desired fixed strip.

There is an important logical qualification.  Because one isolated
primitive form is not proved order-reflecting, a bound for that one scalar
form alone is not presently proved to imply a strip.  The signed
representation and R124's
numerical sign changes explain the hazard but do not prove actual
indefiniteness.  In light of R128, the strip implication applies to the requested
complete theorem only after every conductor and gcd sector is also restored,
together with all fixed-ratio shells and conjugate orientations, the exact
heads, and a nondegenerate dilation/modulation bank, before Cauchy.
Equivalently one
may require a positive spectral lower frame on each bounded Mellin band.
Under that nondegeneracy, (7.7)--(7.10) give the exponent correspondence

```text
fixed strip eta       <==>       full fixed-window energy power 2eta,
```

up to arbitrary epsilon and the already recorded completion errors.

R116's `O(X^(1/2+epsilon))` completion error follows on the balanced
semiprime packet after multiplication by `h(c)<<X^(-1+epsilon)` and
summation over `c`.  It must not be extended to every many-prime modulus
without also treating the near-primitive proper conductors.  R128
subsequently discharges this scope issue by exact recombination, not by
bounding the omitted classes.  The resulting object is the original R71
energy, so (7.10) supplies no smaller primitive-only intermediate theorem.

## 8. Fail-fast conclusions and next valid target

The proposed off-wall mechanisms have exact outcomes.

```text
Poisson back to Q_h Gram kernel       exposes a cross-sampling operator;
periodic zero mean                    kills only additive frequency zero;
all fixed-ratio shells                preserve weighted Mellin low modes;
two-sided Vaughan heads               replace tail coefficients by -mu log;
balanced semiprime heads              identically absent;
Mellin separation                     low rank, not arithmetic mixing;
primitive positivity                  NOT FORCED BY GENERIC GRAM/Q_h DATA;
actual primitive sign                 OPEN;
full all-conductor positivity         true but is the original energy;
VK/PNT                                subpower only;
fixed-power complete bank             equivalent to a fixed strip.       (8.1)
```

The primitive duality is still useful: it has removed a reciprocal phase
and reduced the endpoint to a transparent spectral object.  But it has not
created a cheaper theorem.  R128 resolves the former cross-conductor
possibility algebraically: the remainder cancels exactly, while the complete
ordinary dual remains equal to R71.  The surviving target is therefore a
zeta-specific fixed-power estimate for the **complete** Mobius-log family,
with every reconstructing class retained.  This is fixed-strip-level new
information.  Failure of the
additive-zero and Type-I shortcuts, and failure of generic Gram data to
force primitive positivity, are not evidence
that no fixed strip exists.
