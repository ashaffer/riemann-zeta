# Completion-preserving additive-mode audit

Status: exact discrepancy measure, cofactorwise Poisson completion, finite
reduced-rational completion, proportional-window mode identities, and the
off-axis reciprocal phase are proved; Wright-to-R71 exponent budget corrected.
Zero/diagonal-sector completion and net mode summation remain open.
Literature checked through 2026-08-07.  This report proves no new zero-free
strip and does not prove RH.

R82 follow-up: [`FINITE-RAMANUJAN-NULL-GAUGE-GATE.md`](FINITE-RAMANUJAN-NULL-GAUGE-GATE.md)
shows that the finite Mertens coefficient is gauge-dependent.  A Ramanujan
null cloud removes its displayed zero frequency at polylogarithmic cost, but
the center Schur complement is then exactly zero and the coherent replacement
packet retains the full major-arc carrier.  The analytic bound remains open.

R84 successor note: in the original nonprimitive cofactor expansion, the
coupled amplitude in (6.4) is log-Mellin separable after grouping
`k=j theta`; this avoids a power-sized shift triangle, conditional on a
uniform kernel-tail ledger.  The finite primitive common-`g` mask and the
axis/contact coefficient-phase mismatch remain open.  See
[`COEFFICIENT-SPECIFIC-LOW-BEAT-TENSOR-GATE.md`](COEFFICIENT-SPECIFIC-LOW-BEAT-TENSOR-GATE.md).

## 1. Verdict

The proportional-order bank in
[`PROPORTIONAL-ORDER-DETECTOR-BANK-GATE.md`](PROPORTIONAL-ORDER-DETECTOR-BANK-GATE.md)
solves the detector-side nonattainment problem.  The first audit of its
literature-powered arithmetic proposal changes the status of the dispersion
half, however.

1. The complete von Mangoldt field is exactly the convolution of the compact
   window with one signed **prime-minus-continuum measure**.  Its local energy
   is therefore one positive quadratic form in that measure.  This is the
   correct completion-preserving starting point.
2. The identity `Lambda=(-mu log)*1` allocates the continuum center exactly
   to every cofactor.  Poisson summation then gives a completion-preserving
   expansion containing only nonzero additive lattice modes.  This discharges
   the first algebraic mode-decomposition gate.  An imported finite Ramanujan
   expansion gives a second reduced-rational basis with only polylogarithmic
   coefficient norm; its one remaining zero frequency is exactly the
   logarithmically weighted Mertens tail.
3. An individual zeta-zero residue persists uniformly on polynomially many
   actual B-spline shells, and the whole-window multiplier at every fixed
   nonzero scaled frequency converges to a nonzero Gamma factor.  Thus
   “nonzero additive mode” is not synonymous with “away from zeta zeros.”
   Total-zero-sum noncancellation remains separate.
4. Wright's 2026 theorem really has a nominal `x^(-1/40)` gain for its own
   balanced trilinear Kloosterman form.  Grouping the exact double modes by
   `theta=an-bm` and applying Poisson summation to the solution lattice does
   produce Wright's reciprocal phase on the off-axis sector.  Completing that
   lattice introduces the missing axes, while its determinant-zero,
   dual-zero, and coupled-amplitude sectors are not native Wright sums.
   Dyadic absolute summation also destroys the conditional all-cofactor
   cancellation; the finite basis isolates the same issue as one Mertens zero
   mode.  At fixed detector slope the proposed fixed denominator can reach
   `x^((A_c+h)lambda)`.  The native gain survives that cost for sufficiently
   small slope in the most favorable regime, but no completed net saving has
   been proved.

Consequently there are now two red gates:

```text
complete R71 quadratic form
  -> direct cofactor modes / finite reduced rationals         THEOREM
  -> off-axis Wright-compatible reciprocal phase             THEOREM
  -> zero sectors + amplitude + completed zero mode              OPEN
  -> completed mode sum with zero-slope-uniform power             OPEN. (1.1)
```

The completed-zero-mode gate already contains the Mellin log derivative: a
fixed-power estimate for either the bare cofactor tail or the finite
Ramanujan zero coefficient would itself imply a fixed zero-free strip.  Wright
has therefore reached a genuine oscillatory sector, but current literature
cannot yet be imported as a bound for the completed form.

## 2. Exact prime-minus-continuum representation

Let `V` be any compactly supported real window used on a safe logarithmic
block, so that `r-sup(supp V)>=0`.  Define the locally finite signed measure
on `[1,infinity)`

```text
dP(t)=t^(-1/2)[sum_(n>=1) Lambda(n) delta_n(dt)-dt].     (2.1)
```

The pole-subtracted full field is exactly

```text
D_V(r)=integral V(r-log t)dP(t)

      =sum_n Lambda(n)n^(-1/2)V(r-log n)
       -exp(r/2)Vhat(1/2).                              (2.2)
```

Indeed, in the continuous term set `t=exp(y)` and then `u=r-y`:

```text
integral_1^infinity t^(-1/2)V(r-log t)dt
 =exp(r/2)integral exp(-u/2)V(u)du.                     (2.3)
```

For a nonnegative compact block weight `psi`, put

```text
K_(V,psi)(t,u)
 =integral psi(r)V(r-log t)V(r-log u)dr.                (2.4)
```

Fubini on the compact active product range gives the exact positive identity

```text
integral psi(r)abs(D_V(r))^2dr
 =double_integral K_(V,psi)(t,u)dP(t)dP(u).             (2.5)
```

Expanding (2.5) produces the prime--prime term, both prime--continuum cross
terms, and the continuum--continuum term.  None may be estimated separately
without an additional theorem.  The retreated Euler transfer in R80 says that
the frozen Vaughan tail with its evaluated rank-two center differs from this
field by a superexponentially small amount at every fixed proportional slope.

The Mellin transform of the same completed measure is, initially for
`Re(s)>1`,

```text
integral_[1,infinity) t^(-(s-1/2))dP(t)
 =-zeta'(s)/zeta(s)-1/(s-1).                            (2.6)
```

Thus the pole-bearing centered log derivative is not an analogy imposed after
the fact; it is the Mellin transform of the exact measure in (2.5).

## 3. What an additive mode decomposition must retain

Choose a smooth cutoff `chi` equal to one on the compact `t`-projection of
the kernel in (2.4), and use `e(z)=exp(2 pi i z)`.  The additive transform of
the completed measure is

```text
P_chi(alpha)
 =sum_n Lambda(n)n^(-1/2)chi(n)e(-alpha n)
  -integral chi(t)t^(-1/2)e(-alpha t)dt.                (3.1)
```

Fourier inversion of `K_(V,psi)` rewrites (2.5), distributionally or after an
arbitrarily small smoothing, as a two-frequency quadratic form in the values
`P_chi(alpha)`.  Equation (3.1) is the important ledger: the continuum center
is present for **every** `alpha`.  Attaching it only to `alpha=0` does not
reproduce (2.5).

This also identifies the mismatch with the current exact R71 formula.  Its
frequency-side kernel is the continuous log-ratio coupling

```text
psihat(u-t)Vhat(t)conjugate(Vhat(u)),                    (3.2)
```

as proved in
[`DIRECT-CUTOFF-COMPLETE-TWO-SHIFT-GATE.md`](DIRECT-CUTOFF-COMPLETE-TWO-SHIFT-GATE.md).
It is not yet an additive Diophantine constraint

```text
d_1 b_1 m_1-d_2 b_2 m_2=h_shift.                       (3.3)
```

A delta/circle or complementary-divisor derivation of (3.3), with the two
continuous terms in (2.5) retained, is an open reduction rather than a formal
change of variables.

### Theorem 3.1 (canonical cofactorwise Poisson completion)

Put

```text
c(q)=-mu(q)log q,
D_q=sum_(r>=1)delta_(qr)-dt/q.                          (3.4)
```

As distributions on compact subsets of `(0,infinity)`,

```text
sum_n Lambda(n)delta_n-dt=sum_(q>=1)c(q)D_q.            (3.5)
```

Moreover, with `e(z)=exp(2pi i z)`,

```text
D_q=(1/q)sum_(a in Z-{0})e(a t/q)dt                    (3.6)
```

distributionally on the same positive test domain.  Consequently the exact
completed field (2.2) has the nonzero-mode expansion

```text
D_V(r)=sum_q c(q)/q sum_(a!=0) I_(q,a)(r),

I_(q,a)(r)
 =integral_0^infinity t^(-1/2)V(r-log t)e(a t/q)dt.     (3.7)
```

All sums in (3.5)--(3.7) are understood as their natural distributional
limits against the compact active test.

#### Proof

The coefficient identity

```text
Lambda=(-mu log)*1                                     (3.8)
```

follows either coefficientwise or from
`zeta(s)(1/zeta(s))'=-zeta'(s)/zeta(s)`.  The PNT, equivalently the imported
Vinogradov--Korobov/Mertens bound, gives the ordinary conditional limit

```text
sum_(q>=1)c(q)/q=(1/zeta)'(1)=1.                        (3.9)
```

Expanding the right side of (3.5), its atomic coefficient at `n` is
`sum_(q|n)c(q)=Lambda(n)`, while its continuous coefficient is `-1` by
(3.9).  This proves (3.5).

On a compact positive test interval, `sum_(r>=1)delta_(qr)` agrees with the
full lattice comb `sum_(r in Z)delta_(qr)`.  Ordinary Poisson summation gives

```text
sum_(r in Z)delta_(qr)
 =(1/q)sum_(a in Z)e(a t/q)dt.
```

Subtracting `dt/q` removes exactly the `a=0` mode and proves (3.6).  Inserting
(3.6) into (2.2) proves (3.7).

Squaring (3.7) inside the block weight produces an exact
`q_1,q_2,a_1,a_2` form with `a_1a_2!=0`; the continuum center has not been
discarded but has canceled the zero lattice mode cofactor by cofactor.  This
is the requested completion-preserving additive-mode decomposition.

The phases in (3.7) are direct additive phases `a t/q`, whereas Wright
requires a reciprocal phase `vartheta A inverse(m)/(nR_0)`.  Section 6 shows
that a second Poisson summation produces that phase exactly off axis.  It also
identifies the determinant-zero, dual-zero, punctured-axis, and amplitude
separation terms that prevent (3.7) from being a completed Wright estimate.

### Proposition 3.2 (fixed rational modes are genuine major arcs)

Let `chi_0` be smooth and compactly supported in `(0,infinity)`, put
`chi_X(t)=chi_0(t/X)`, and define `P_(chi_X)` by (3.1).  If `q>=2` is fixed
and squarefree and `(a,q)=1`, then

```text
P_(chi_X)(a/q)
 =mu(q)/phi(q) X^(1/2)
    integral_0^infinity chi_0(u)u^(-1/2)du
  +o_q(X^(1/2)).                                      (3.10)
```

Indeed, the PNT in each fixed reduced residue class, followed by partial
summation, gives the prime main term in (3.10); summing its additive character
over those classes gives the Ramanujan sum `c_q(a)=mu(q)`.  Prime powers in
nonreduced classes are lower order.  Meanwhile repeated integration by parts
gives

```text
integral chi_X(t)t^(-1/2)e(-a t/q)dt
 =O_(A,q,chi_0)(X^(1/2-A))                            (3.11)
```

for every fixed `A`.

Thus the continuum reference measure cancels the `q=1` prime-density term,
not the singular-series terms at all rational points.  For example,
`P_(chi_X)(1/2)` has a negative main term of order `X^(1/2)`.  Any use of a
minor-arc theorem must therefore exclude a full rational--Archimedean
major-arc union; deleting only a small interval around zero is false.  This
is compatible with (3.7), whose nonzero lattice modes occur precisely at
rational frequencies.

These major arcs are also spectral carriers, not removable deterministic
noise.  For fixed reduced `a/q`, character orthogonality gives schematically

```text
sum_n Lambda(n)e(-an/q)n^(-s)
 =1/phi(q) sum_(chi mod q)tau(conjugate(chi))chi(-a)
     [-L'(s,chi)/L(s,chi)]+H_(a,q)(s),                (3.11a)
```

where `H_(a,q)` is analytic for `Re(s)>0` and accounts for the primes dividing
`q`.  The principal character contributes `mu(q)/phi(q)` times
`-zeta'/zeta`, up to those local analytic factors; nonprincipal characters
bring their own `L`-zero poles.  Subtracting the singular-series density can
cancel the pole at one, but it cannot remove these zero carriers.  Any
rational-major-arc model must therefore remain inside the completed detector
rather than be discarded as a known main term.

### Proposition 3.3 (exact finite reduced-rational basis)

There is a second, finite way to group the same arithmetic.  For a finite
active range `N`, define

```text
Lambda_N(n)=-sum_(d<=N,d|n)mu(d)log d.
```

The standard finite Ramanujan expansion is

```text
Lambda_N(n)=sum_(q<=N) LambdaHat_N(q)c_q(n),           (3.12)

LambdaHat_N(q)
 =-mu(q)/q sum_(d<=N/q,(d,q)=1)mu(d)log(dq)/d,

abs(LambdaHat_N(q))<<log^2(N)/q.                      (3.13)
```

For `n<=N`, this is exactly `Lambda(n)`.  It follows immediately from
`sum_(q|d)c_q(n)=d 1_(d|n)`; the formula and bound are also an imported lemma
from [Laporta's 2024 finite
expansion](https://doi.org/10.1007/s12188-024-00282-4).  In particular,

```text
sum_(q<=N)phi(q)abs(LambdaHat_N(q))^2<<log^5(N).       (3.14)
```

Poisson summation of the periodic Ramanujan comb gives, on a positive test
supported below `N`,

```text
sum_n Lambda(n)delta_n-dt
 =[LambdaHat_N(1)-1]dt
  +LambdaHat_N(1)sum_(k!=0)e(kt)dt
  +sum_(2<=q<=N) LambdaHat_N(q)
     sum_((a,q)=1,1<=a<q) sum_(k in Z)e([k+a/q]t)dt.  (3.15)
```

Thus every oscillatory coefficient is finite and reduced-rational, with a
polylogarithmic Hilbert ledger.  The sole zero frequency is

```text
LambdaHat_N(1)-1
 =sum_(d<=N)-mu(d)log(d)/d-1=-R(N),                   (3.16)
```

where `R` is the cofactor tail in (6.7).  Formula (3.15) is a useful
completion-preserving alternative to the conditional rectangular limit
(6.1), but it does not estimate the completion: a fixed power for (3.16)
already implies a fixed zero-free strip.  It isolates the zero-mode problem
instead of removing it.  The coefficient identity is checked symbolically in
[`finite_ramanujan_completion_probe.py`](../src/finite_ramanujan_completion_probe.py).

The exact finite coefficients in (3.13) cannot be replaced by their formal
fixed-denominator limits `mu(q)/phi(q)` at a power cutoff.  Indeed, put

```text
R_Q(n)=sum_(q<=Q)mu(q)c_q(n)/phi(q),
A(Q)=sum_(q<=Q)mu(q)^2/phi(q)=log Q+O(1).              (3.17)
```

For every prime `p>Q`, `c_q(p)=mu(q)`, hence `R_Q(p)=A(Q)`.  If
`Q=X^theta`, `theta<1`, and
`f(p)=phi(p)Lambda(p)/p=(1-1/p)log p`, then the PNT gives

```text
sum_(X<p<=2X)abs(f(p)-R_Q(p))^2
 >=[(1-theta)^2+o(1)]X log X.                         (3.18)
```

This is the full natural `L2` scale of `f`, not a power-saving error.  The
same obstruction is visible spectrally.  If

```text
A_Q(s)=sum_(q<=Q)mu(q)/phi(q)
          sum_(d|q)d^(1-s)mu(q/d),
```

then exactly

```text
sum_n R_Q(n)n^(-s)=zeta(s)A_Q(s).                     (3.18a)
```

Although `A_Q(1)=1` makes the residual
`-zeta'/zeta-zeta A_Q` pole-free at one, `zeta A_Q` is analytic at every
nontrivial zeta zero, so the residual retains every zero pole.  A finite
rational-model subtraction therefore moves the full RH carrier into its
error term.

On the other hand,
`Lambda-f` is spectrally harmless: on `n=p^k`,

```text
Lambda(n)-f(n)=log p/p,

sum_n abs(Lambda(n)-f(n))n^(-1/2)<infinity,            (3.19)
```

and its Dirichlet series

```text
sum_p log p/[p(p^s-1)]                                (3.20)
```

is analytic for `Re(s)>0`.  Thus `f` has the same nontrivial-zero poles as
`Lambda`.  Hardy's conditional identity

```text
f(n)=sum_q mu(q)c_q(n)/phi(q)                         (3.21)
```

holds by natural-`q` convergence for each fixed `n>1` (and diverges at
`n=1`).  But the relevant Ramanujan basis norm is not
`sum abs(mu(q)/phi(q))^2`; since `norm(c_q)^2=phi(q)`, it is

```text
sum_(q<=Q)mu(q)^2/phi(q)=log Q+O(1).                  (3.22)
```

The equal-frequency diagonal already carries this logarithmic mass, and
(3.18) shows that a power cutoff leaves the full prime `L2` scale.  Hence the
formal infinite coefficients do not provide an `L2` shortcut.  The
scale-adapted finite coefficients (3.13), including moduli up to the full
active range, are essential.

## 4. Principal-band persistence of a zero carrier

The exact zero/nonzero-frequency split is also too sharp spectrally.  Let
`W` be smooth and compactly supported inside `(0,infinity)`, and use the
critical normalization of the measure (2.1):

```text
S_W^(1/2)(X,xi)
 =sum_n Lambda(n)n^(-1/2)W(n/X)e(-xi n/X)
  -integral t^(-1/2)W(t/X)e(-xi t/X)dt.                 (4.1)
```

Put

```text
M_W^(1/2)(s,xi)
 =integral W(u)e(-xi u)u^(s-3/2)du.                    (4.2)
```

Mellin inversion and a standard contour shift give the zero contribution

```text
S_W^(1/2)(X,xi)
 =-sum_rho m_rho X^(rho-1/2)M_W^(1/2)(rho,xi)
  +trivial-zero and contour terms.                      (4.3)
```

For every fixed zero `rho`, `M_W^(1/2)(rho,xi)` is an entire function of
`xi`.  If `M_W^(1/2)(rho,0)!=0`, continuity gives an `xi_0>0` such that the
same individual `X^(rho-1/2)` residue is nonzero for every
`abs(xi)<xi_0`.  Suitable `W` with this property always exist.  This does not
by itself exclude cancellation in the total zero sum or verify nonvanishing
for the repository's actual quadratic kernel; those require the block-norm
and multiplier analysis.

Hence, for this fixed scaled localizer, an off-line zero is not confined to
the point `alpha=0`.  It occupies a principal additive band

```text
alpha=xi/X,       abs(xi)<xi_0.                         (4.4)
```

For the proportional-order family the corresponding weights depend on `X`
and the full active product range is
`X^(1-h lambda+o(1))<=n<=X^(1+h lambda+o(1))`.  The next two results remove
the apparent band-width obstruction for an individual zero residue.

### Theorem 4.1 (universal shellwise band)

Let `s=delta+i gamma`, let `I=[a,b]` have length
`ell<=log 2`, and let `chi_I>=0` be supported in `I`.  For the actual
nonnegative normalized B-spline window `V_(h,k)`, put

```text
m_(I,k,s)(xi)
 =integral_I chi_I(t)V_(h,k)(t)exp(-st)
    e(-xi exp(b-t))dt,

L_I=integral_I chi_I(t)V_(h,k)(t)exp(-delta t)dt.       (4.5)
```

If `L_I>0` and `abs(gamma)ell<=pi/2`, then

```text
abs(m_(I,k,s)(xi))>=L_I/(2sqrt(2))                     (4.6)
```

uniformly for

```text
abs(xi)<=1/(8sqrt(2)pi).                               (4.7)
```

#### Proof

At `xi=0`, rotate by the phase at the midpoint of `I`.  The remaining phase
lies in `[-pi/4,pi/4]`, so the real part is at least `L_I/sqrt(2)`.  Also

```text
abs[e(-xi exp(b-t))-1]
 <=2pi abs(xi)exp(ell)<=4pi abs(xi).
```

Equations (4.6)--(4.7) follow by the triangle inequality.

At detector scale `X=exp(R)`, set `Y=X exp(-b)`.  Then
`exp(b-t)=n/Y`, so (4.5) is exactly the shell-normalized additive phase
`e(-xi n/Y)`, with the continuum subtraction retained through (3.1).
Choose a zero-independent mesh `ell_R=1/R`.  For every fixed hypothetical
zero, the phase condition holds for all large `R`; the proportional support
needs only `O(R^2)` shells.  Thus the actual window has a universal shellwise
band at polynomial decomposition cost.

This proves nonvanishing of each selected zero residue on each nonempty
shell.  It does not prove that the total zero sum cannot cancel, nor does it
identify Wright's integer reciprocal phase with `xi`.

### Theorem 4.2 (whole-window Gamma limit)

For the unnormalized window `W_(h,k)`, define

```text
T_(h,k)(s,xi)
 =integral_R W_(h,k)(t)exp(-st)e(-xi exp(-t))dt.        (4.8)
```

For `0<Re(s)<1` and fixed `xi!=0`,

```text
lim_(k->infinity) T_(h,k)(s,xi)
 =Gamma(s)(2pi abs(xi))^(-s)
    exp[-i sign(xi)pi s/2].                            (4.9)
```

The convergence is uniform when `xi` ranges over a compact subset of
`R-{0}`.  In particular, the limit is never zero.

#### Proof

Let `S_k` be a sum of `k` independent uniforms on `[0,h]`.  Symmetry gives
the exact identity

```text
W_(h,k)(t)=Prob(S_k>=abs(t)).                           (4.10)
```

Consequently (4.8) is

```text
E[J_(s,xi)(S_k)],

J_(s,xi)(A)=integral_(-A)^A exp(-st)e(-xi exp(-t))dt. (4.11)
```

After `y=exp(-t)`, the truncated integral `J_(s,xi)(A)` is the integral of
`y^(s-1)e(-xi y)` over `[exp(-A),exp(A)]`.  For `0<Re(s)<1` these truncated
integrals are uniformly bounded in `A`: the endpoint at zero is absolutely
integrable, and one integration by parts controls the oscillatory endpoint
at infinity.  They converge to the classical oscillatory Gamma integral on
the right side of (4.9).  Since `S_k` tends to infinity in probability,
bounded convergence in (4.11) proves (4.9).  The same integration-by-parts
bound is uniform when `xi` stays in a compact annulus away from zero.

Division by `N_(h,k)asymp_h sqrt(k)` costs only a polynomial.  Therefore an
individual right-hand zero contributes its full horizontal factor
`X^(rho-1/2)` at every fixed nonzero scaled frequency, up to a nonzero Gamma
multiplier.  The zero-frequency formula (2.4) and the nonzero-frequency limit
(4.9) are nonuniform as `xi->0`; the limits in `k` and `xi` do not commute.

The numerical algebra is exercised by
[`scaled_additive_twist_probe.py`](../src/scaled_additive_twist_probe.py).
These results discharge uniform individual-residue band width, but not
total-sum noncancellation or the missing arithmetic mode map.  In particular,
`xi` is continuous whereas Wright's `vartheta` is an integer, so the
hypothesis `vartheta!=0` does not by itself show that the theorem acts away
from all zeta-zero carriers.

## 5. Correct Wright exponent budget

Theorem 2.1 of Thomas Wright's
[Trilinear Kloosterman fractions I](https://arxiv.org/abs/2604.25177)
bounds its native form

```text
sum_(a~A_W,m~M,n~N;(m,nR_0)=1)
 alpha_m beta_n nu_a
 e(vartheta a inverse(m)/(nR_0)),                       (5.1)
```

where `vartheta` is a nonzero integer, `R_0` is the partially fixed integer
denominator, `M<<N^2`, and `R_0<<M^C`.  In the dense balanced limit

```text
M=N=x^(1/2+o(1)),       R_0=x^o(1),
abs(vartheta)A_W<=MN x^o(1),                            (5.2)
```

the largest term in Wright's displayed bracket is `x^(-1/40+o(1))` relative
to the theorem's Cauchy baseline.  This is a theorem about (5.1), not yet
about R71.

For the retreated cutoff schedule of R80, at a fixed slope `k=lambda log x`,
the central product shell `n asymp x` has

```text
U,V=x^((1-A_c lambda+o(1))/2),
central cofactor<=x^(A_c lambda+o(1)).                   (5.3)
```

Thus a cofactor used as `R_0` is a small fixed power of `x`.  Under the most
favorable hypothetical map

```text
M=N=x^((1-A_c lambda)/2+o(1)),
R_0=x^(A_c lambda+o(1)),
A_W=x^o(1),
1+abs(vartheta)A_W/(MN)=x^o(1),                         (5.4)
```

direct substitution in Wright's theorem gives the nominal net saving

```text
eta_W(lambda)
 =1/40-(11/40)A_c lambda+o(1).                          (5.5)
```

The `11 A_c lambda/40` cost consists of `R_0^(1/4)` and the worst bracket
term.  The displayed branch is active for `A_c lambda<3/13`; its whole
positive range `A_c lambda<1/11` is therefore covered.

The full proportional window reaches products
`n<=x^(1+h lambda+o(1))`.  On its upper shell the free cofactor can be as
large as `x^((A_c+h)lambda+o(1))`.  Under the same favorable assumptions the
crude full-window budget is consequently

```text
eta_W^full(lambda)
 =1/40-[(11A_c+10h)/40]lambda+o(1).                    (5.6)
```

A positive phase-ratio exponent costs one quarter of that exponent; a
power-sized mode triangle inequality costs its full exponent.  Formulas
(5.5)--(5.6) prove only that the fixed-denominator cost is not an automatic
fail for sufficiently small slope.  They do not verify (5.4), construct
(5.1), decompose and recombine every shell, or sum any R71 modes.

The exact five-term substitution is implemented in
[`wright_r71_exponent_budget.py`](../src/wright_r71_exponent_budget.py).
The audit uses the weaker displayed statement of Wright's Theorem 2.1; the
current v1 proof has a different power of `A_W` in one intermediate display,
which does not improve the imported claim.

## 6. The exact off-axis reciprocal phase and its stopping point

Put `L(t,u)=K_(V,psi)(t,u)/sqrt(tu)` and initially smooth the compact kernel.
With the Fourier convention of Section 3, its completed energy is exactly the
natural rectangular limit

```text
lim_(Q->infinity) sum_(q_1,q_2<=Q) c(q_1)c(q_2)/(q_1q_2)
  sum_(a,b!=0) Lhat(-a/q_1,b/q_2).                     (6.1)
```

This is not asserted to be an absolutely convergent rearrangement.  Write
`q_1=gm`, `q_2=gn`, with `(m,n)=1`, and group a mode pair by
`theta=an-bm`.  If `a_0 n=theta (mod m)` and
`b_0=(a_0 n-theta)/m`, every integer solution is

```text
a=a_0+m ell,       b=b_0+n ell,       ell in Z.        (6.2)
```

Define

```text
H_(g,m,n,theta)(s)
 =Lhat(-s/g,[s-theta/(mn)]/g).                         (6.3)
```

One-dimensional Poisson summation in `ell` gives

```text
sum_(ell in Z) H(ell+a_0/m)
 =sum_(j in Z)e(j theta inverse(n)/m) A_(g,m,n,theta)(j),

A_(g,m,n,theta)(j)
 =g integral_R L(u+gj,u)e(theta u/(gmn))du.            (6.4)
```

Thus the sector `j theta!=0` has a literal Wright phase.  One may take
Wright's two denominator variables to be `n,m`, fixed denominator `R_0=1`,
phase integer `theta`, and numerator variable `j`; the coprimality condition
is exactly `(m,n)=1`.  This is an exact algebraic advance beyond the
continuous log-ratio formula.

It is not yet a quantitatively admissible Wright form.  The amplitude in
(6.4) couples `m,n,theta,j`.  On a finite smooth dyadic box it has a separable
Fourier expansion, but no uniform `x^o(1)` bound for the expansion's total
coefficient mass and sequence norms has been proved.  Merely grouping the
product `j theta` therefore does not discharge the amplitude gate.

Three algebraic sectors also remain outside Wright's nonzero phase:

1. `theta=0`, the equal-rational-frequency diagonal;
2. `j=0`, the Poisson main mode; and
3. the punctured axes.  Indeed, the original lattice has `a b!=0`, whereas
   (6.2) is complete.  Its exact correction is

```text
-1_(m|theta)Lhat(0,-theta/(gmn))
-1_(n|theta)Lhat(-theta/(gmn),0)
+1_(theta=0)Lhat(0,0).                                (6.5)
```

The one-sided zero modes in (6.5) are the prime--continuum pieces temporarily
reintroduced by completing the lattice.  They are not generic Wright forms.
The congruence, inverse placement, and punctured-axis divisibilities are
exercised by
[`reciprocal_solution_lattice_probe.py`](../src/reciprocal_solution_lattice_probe.py).

There is a further conditional-summation obstruction.  If a compact test `f`
is supported below `Y`, then for every `q>Y`,

```text
D_q[f]=-(1/q)integral f(t)dt.                          (6.6)
```

For `Q>Y`, the exact omitted measure is therefore `-R(Q)dt`, where

```text
R(Q)=1-sum_(q<=Q)c(q)/q.                              (6.7)
```

This remainder may be retained exactly, so finite truncation alone is not a
new zero-free-strip theorem.  What is already strip-strength is discarding it
with a fixed power at a polynomially related cutoff.  If, for some fixed
`eta>0`,

```text
R(Q)=O(Q^(-eta)),                                     (6.8)
```

then partial summation makes
`sum_q c(q)q^(-s)=(1/zeta)'(s)` analytic for
`Re(s)>1-eta`.  A zero of zeta there would give this derivative a pole.
Consequently (6.8) implies the fixed zero-free half-plane
`Re(s)<=1-eta`.  Equivalently, for `0<eta<1`, (6.8) is a power bound for the
logarithmically weighted Mertens sum
`sum_(q<=Q)-mu(q)log q`, up to the exact partial-summation identity; ordinary
Mertens power control is equivalent after logarithms or an arbitrarily small
exponent loss.

This does not rule out retaining `R(Q)` exactly, taking a superpolynomial
cutoff using Vinogradov--Korobov, or treating (6.4)--(6.7) jointly.  It proves
that a triangle inequality over cofactors, followed by a bare polynomial-tail
power estimate, has renamed the desired theorem.

### Remaining application gates for the Kloosterman input

The exact-object gate has been passed by Theorem 3.1, and (6.4) passes the
native-phase gate on the completed off-axis lattice.  Before Wright's theorem
can be called an R71 lemma, a derivation must still verify all of the
following.

1. **Non-Wright sectors.**  Recombine `theta=0`, `j=0`, and the `a=0` and
   `b=0` corrections with the off-axis estimate without separating a
   pole-sized prime--continuum term.
2. **Cofactor/zero-mode completion.**  Either preserve (3.9) across every
   dyadic modulus range, or use the finite basis (3.15) and retain its scalar
   `-R(N)` inside the same square.  A triangle inequality in `q` is
   inadmissible, and the bare power-tail shortcut (6.8) is already the desired
   strip.
3. **Ranges and norms.**  Record dyadic `A_W,M,N,R_0`, all sequence `L2`
   norms, and the phase-ratio factor.  The schematic sizes in (5.4) cannot be
   assumed.
4. **Total losses.**  Sum complementary divisors, shifts, moduli, dual modes,
   and all cross-shell terms quadratically.  The shell refinement in Theorem
   4.1 and every conditional cofactor limit in (3.7) must be uniform.  The
   total power loss must be strictly smaller than the applicable shell budget,
   in particular (5.6) for a crude full-window treatment.
5. **Arithmetic mode coverage.**  Separate the rational--Archimedean major
   arcs detected by Proposition 3.2 from genuine minor arcs without losing
   the completion.  Explain how the shell bands in Theorem 4.1 map to the
   resulting integer modes and why the total zero sum cannot evade the final
   square.  Calling every nonzero integer mode a minor mode is insufficient.

No current repository derivation passes these five remaining gates.
Accordingly, Wright's theorem remains a promising candidate input rather
than a proved power-saving half of the R71 architecture.

## 7. Calibrated MRSTT import

The shell-truncated R71 **tail coefficient** is an admissible Type-II
coefficient:

```text
a_(U,V)=alpha*beta_V,
alpha(d)=mu(d)1_(U<d<=Y exp(O(hk))/V),
beta_V(q)=sum_(b|q,b>V)Lambda(b),
0<=beta_V(q)<=log q.                                   (7.1)
```

This verifies the elementary `L2` and `L4` coefficient hypotheses in the
balanced range.  It does not by itself give a large-correlation set of starts,
which is an input to the contagion argument.

The Type-`I_2` route still fails: the offending rough factor
`Lambda_(>V)` has variation `gg V` already on `(V,2V]`.  For Type II, the
abelian inverse conclusion places a locally Mellin-like phase in the permitted
major-arc class; it is more precise than the slogan “the theorem returns
`T=-t`,” and it does not exclude that class.

Most importantly, the MRSTT almost-all theorems are scalar statements for
objects such as `Lambda-Lambda^sharp`.  They do not directly prove the joint
tail--head--continuum square, every-block bank bound, or uniform frequency
supremum required here.  The completion-preserving vector estimate proposed
in R80 remains a new theorem, not an existing logarithmic-saving corollary.

There is nevertheless one safe completed minor-arc corollary.  Specialize
MRSTT Theorem 1.1(ii) and Corollary 1.2(ii) to linear phases, take
`H>=Y^(1/3+epsilon)`, and define the polylogarithmic minor arcs by

```text
H norm(q alpha)>log^B(Y)  for every q<=log^B(Y).       (7.2)
```

After bounded-variation summation by parts, the deterministic continuum
integral is separately logarithmically small on (7.2).  Choosing one favorable
translate of the `H`-grid then turns the common exceptional-start estimate
into

```text
sup_(alpha satisfying (7.2)) sum_J abs(C_J(alpha))^2
 <<_(A,epsilon) YH log^(-A)(Y),                        (7.3)
```

for the dimensionally normalized completed scalar cells `C_J`, with arbitrary
fixed `A`.  This is a short project corollary of the cited theorems, not their
verbatim statement.  It gives only a logarithmic saving and only for a
suitably translated partition, not the repository's predetermined every-block
bank.

Proposition 3.2 also rules out an overstrong formulation of that proposal.
The exceptional set cannot be only the principal interval `abs(alpha)ll1/Y`:
fixed rational phases `a/q` have their own order-`Y^(1/2)` prime main terms.
The natural MRSTT inverse output is a union of rational--Archimedean major
arcs, including locally Mellin-like phases.  The literature may help on its
complement, but the complete major-arc contribution remains in the R71
target.

Running MRSTT Theorem 4.2 and Lemma 4.4 with a power threshold
`delta=Y^(-nu)` suggests a stronger power minor-arc square outside denominators
`q<=delta^(-C)` and radii of order `delta^(-C)Y/H^2`.  That statement is not
currently an imported theorem: the bounded-variation inverse step, measurable
frequency choice, and translated-grid bookkeeping have not been written at
power precision.  Even if proved, the radius `Y/H^2` reaches the natural
`1/Y` spectral scale only when `H` is essentially `Y`, and all rational major
arcs remain.

Primary sources are
[Higher uniformity I](https://doi.org/10.1017/fmp.2023.28) and
[Higher uniformity II](https://doi.org/10.1007/s00222-026-01408-6).

## 8. A damped-cofactor workaround, and why it fails componentwise

A natural way to force absolute cofactor convergence is to pay a small
horizontal shift.  For fixed `epsilon>0`, put

```text
c_epsilon(q)=c(q)q^(-epsilon),
C_epsilon=sum_q c(q)q^(-1-epsilon)=(1/zeta)'(1+epsilon),
f_epsilon=c_epsilon*1.                                 (8.1)
```

Then the completed critical measure

```text
dP_epsilon(t)=t^(-1/2)[sum_n f_epsilon(n)delta_n-C_epsilon dt]
```

has the absolutely convergent cofactor representation
`sum_q c_epsilon(q)D_q`, and its Mellin transform is

```text
zeta(s)(1/zeta)'(s+epsilon)-C_epsilon/(s-1).           (8.2)
```

The pole at one cancels.  If `rho` is a simple zeta zero and
`zeta(rho-epsilon)!=0`, it creates a double pole at `rho-epsilon`; for all but
a countable set of `epsilon` the noncoincidence holds simultaneously.  Thus an
amplitude bound `X^(1/2-eta+o(1))` for this shifted field would imply only

```text
Re(rho)<=1+epsilon-eta.                               (8.3)
```

The desired strip width is `eta-epsilon`: the absolute convergence has a
price.  Absolute convergence here concerns the outer cofactor sum on compact
tests; after Poisson summation the modes inside each comb are still
distributional and cannot be summed termwise in absolute value.

That price cannot be recovered by separately bounding the cofactor tail and
the favorable Wright sector.  Truncate at `Q=X^A`.  On `n asymp X`, the
omitted atomic coefficient and center satisfy

```text
abs(sum_(q>Q,q|n)c(q)q^(-epsilon))
 <<Q^(-epsilon)tau(n)log n,

abs(sum_(q>Q)c(q)q^(-1-epsilon))
 <<_epsilon Q^(-epsilon)log Q.                        (8.4)
```

Consequently the critical-field tail has amplitude at best
`X^(1/2-A epsilon+o(1))` by absolute values.  A componentwise proof therefore
has `eta<=A epsilon`.  In the ideal central-shell Wright ledger with a
cofactor exponent `A`, the native gain is at most

```text
eta_W(A)=(1-11A)/40.                                  (8.5)
```

Optimizing the two available gains gives

```text
max_(A>0) min[A epsilon,(1-11A)/40]
 =epsilon/(40epsilon+11)<epsilon.                     (8.6)
```

Thus even this optimistic balanced-cutoff ledger fails to repay the shift in
(8.3), before the full-window, amplitude-separation, zero-dual, or axis losses
are charged.  There is also a cutoff-independent version of the same wall.
On a physical shell below `X`, every `q>X` has no atom, so its whole
contribution is the scalar center

```text
-T_epsilon(X)dt,
T_epsilon(X)=sum_(q>X)c(q)q^(-1-epsilon)
             <<X^(-epsilon+o(1))                      (8.7)
```

at current Vinogradov--Korobov strength.  Taking an artificial `Q>X` does not
remove it: the included block `X<q<=Q` is itself pure continuum and restores
`T_epsilon(X)-T_epsilon(Q)`.  Estimating this sector separately caps
the currently imported gain at `eta=epsilon+o(1)`, hence gives no fixed net
strip.  Improving (8.7) by a further fixed power is itself new zero-free
information.

The concrete fatal atomic face is `q=n` at primes: it has free quotient one,
contributes `log(p)p^(-epsilon)`, and is outside the balanced Wright core.  Its
cancellation against the continuum is precisely the shifted PNT major arc.

This kills the **separated** damped-cofactor strategy.  It does not disprove a
joint cancellation theorem that keeps the tail, axes, and off-axis Wright
sector in one square; such a theorem is again the live major-arc problem.

## 9. Updated live target

The detector side now gives an exact implication: a fixed power uniform along
slopes tending to zero yields a fixed zero-free strip, and limiting amplitude
zero yields RH.  The arithmetic side should be developed in this order:

1. derive an exact mode formula for (2.5), with the center in every mode;
   this is now Theorem 3.1;
2. use (6.4) for the literal Wright phase on the off-axis solution lattice;
   this algebraic step is now proved;
3. recombine the determinant-zero, dual-zero, punctured-axis, and conditional
   cofactor sectors without a triangle inequality or the strip-strength
   shortcut (6.8), while controlling the amplitude separation in (6.4); the
   finite basis (3.15) may replace conditional summation, but its `-R(N)`
   zero mode must remain in the same square;
4. run the complete
   exponent ledger, killing the route if the total loss reaches the relevant
   budget (5.5) or (5.6);
5. split genuine minor arcs from the rational--Archimedean major arcs of
   Proposition 3.2; and
6. seek a joint power bound or an exact further renormalization for the major
   arcs without separating the Mobius, prime, and continuum pieces.

Step 6 is still the fixed-strip-strength centered major-arc theorem.  Step 3
is now the narrowest fail-fast bridge; it must be completed before treating
Kloosterman technology as a bound for the whole object.

Two tempting detours are now closed.  Truncating Hardy's limiting Ramanujan
coefficients leaves full prime `L2` energy by (3.18), and fixed cofactor
damping cannot repay its horizontal shift by (8.6).  Neither should be
reintroduced as a claimed power-saving completion.

## 10. Reproduction and nonclaims

Run the exponent audit with

```text
PYTHONPATH=src python3 src/wright_r71_exponent_budget.py \
  --damping-epsilon 0.01
PYTHONPATH=src python3 src/scaled_additive_twist_probe.py
PYTHONPATH=src python3 src/reciprocal_solution_lattice_probe.py
PYTHONPATH=src python3 src/finite_ramanujan_completion_probe.py
PYTHONPATH=src python3 -m pytest -q \
  src/test_wright_r71_exponent_budget.py \
  src/test_scaled_additive_twist_probe.py \
  src/test_reciprocal_solution_lattice_probe.py \
  src/test_finite_ramanujan_completion_probe.py
```

The script checks only Wright's displayed exponent algebra under supplied
schematic parameters.  It does not construct a delta method, verify a mode
range, estimate primes, or certify a zero-free region.  The identities
(2.2), (2.5), (2.6), and (4.3) are conventional analytic arguments, not Lean
theorems, and should receive independent specialist review before any novelty
claim.
