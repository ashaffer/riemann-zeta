# Off-the-wall carrier sprint

## Control, QSP, coding, noncommutative lifts, and adversarial design

**Date:** 2026-08-13  
**Binary verdict:** **no strip and no improved zero-free bound.**

The sprint produced one concrete new exact reformulation that may be useful:
the actual prime-log Wiener extremal is the maximum Schur complement of an
adversarially weighted prime-log Gramian, and it always has a sparse optimal
frequency witness.  It also produced an exact pruning theorem: arbitrary
matrix/quantum ancillas representable by the diagonal linear two-leg readout
below have exactly the same optimum after normalization by
`sqrt(E_L*E_R)`, equivalently by half the total energy, as the scalar Wiener
problem.  Lossless QSP can move a
pole or null into a complementary channel, but cannot erase it from all
channels; after scalar compact realization it pays the original Wiener or
Blaschke cost.

---

## 1. The three constraints that every imported mechanism must respect

On a finite permitted frequency set `J`, let

```text
a_k=(exp(i*xi_k*u_j))_(1<=j<=M),
A=[a_1 ... a_D],
b_k=integral W_alpha(u)exp(i*xi_k*u)du.              (1.1)
```

The active `u_j` are the actual prime-power logarithms.  Up to harmless
conjugation conventions, the exact extremal is

```text
E(A,b)
 =sup{|<b,h>|:A*h=0, ||h||_1<=1}
 =inf_lambda ||b-A^*lambda||_infinity.              (1.2)
```

For the zeta parameters this is `E_Y`.  The required result remains

```text
E_Y>=Y^(-kappa+o(1)),       kappa<0.0180303234....   (1.3)
```

The sharp two-leg factorization says that a scalar cross coefficient vector
`h_k=conj(ell_k)r_k` costs

```text
inf (||ell||_2^2+||r||_2^2)=2||h||_1.               (1.4)
```

Thus an imported method is not allowed to normalize in `H-infinity` or in a
matrix norm and silently descend to (1.4) for free.  Finally, the carrier
vector `b` is the principal mode: projecting it out, squaring away its sign,
or assuming a relative bound against it deletes the target rather than
proving the target sign.

---

## 2. Mechanism menu

| imported idea | proposed use | audit outcome |
|---|---|---|
| adversarial optimal design / multiplicative weights | choose the most informative frequencies against every prime-log quadrature | **live exact PSD certificate and finite exchange engine; Theorem 3.1** |
| controllability/observability Gramians | measure the carrier component invisible to the prime outputs | **same Schur complement; useful language, not a bound by itself** |
| `H-infinity`/Youla model matching | synthesize a stable controller with prime notches and retained carrier | **norm mismatch: compact descent pays the Wiener norm** |
| QSP/paraunitary filtering | use a lossless polynomial notch sequence | **one channel can mask a mode, but its complement retains it** |
| coding/parity checks | regard prime evaluations as a check matrix and the carrier as a logical syndrome | **exact: `E_Y` is an `l-infinity` coset distance; sparse checks follow from Theorem 3.1** |
| tensor/product-code amplification | amplify the logical distance using unique factorization | **degree `q` needs aperture at least `Y^q`; the available `Y^(50/33+o(1))` does not reach `q=2`** |
| sparse-sieve/Boolean circuit | compile the prime-power predicate into a short notch circuit | **literal primorial expansion is exponentially costly before log transfer; recombined log-Wiener cost remains open** |
| noncommutative/free-unitary lift | make prime modes orthogonal before scalar compression | **no advantage for diagonal linear state readouts; Theorem 4.1** |
| adelic/character ancilla | separate Euler factors into local character channels | **no scalar gain after spherical-state compression; an all-channel coercive theorem is the only genuine loophole** |
| nonlinear quantum measurement | read a probability instead of an amplitude | **one probability loses the required sign and creates a positive diagonal/DC mode; general channel differences are outside the no-go** |

The adversarial-design and noncommutative entries were pushed to exact
theorems below.  The QSP entry was also tested at the lossless-polynomial
level.

---

## 3. Best mechanism I: adversarial design equals a sparse Gramian certificate

For a probability vector `w=(w_k)` on `J`, put

```text
W=diag(w),
G_w=A*W*A^*,       g_w=A*W*b,       c_w=b^*W*b,
Delta(w)=c_w-g_w^*G_w^dagger*g_w.                   (3.1)
```

The last quantity is the Schur complement of `G_w` in the augmented weighted
Gramian.  In control language it is the output energy of the carrier left
unobservable by the prime-log output channels.  In experimental-design
language it is the `c`-optimal prediction variance; in electrical language
it is an effective resistance.

### Theorem 3.1 (Chebyshev--Wiener adversarial-design identity)

For every finite complex matrix `A` and vector `b`,

```text
E(A,b)^2=max_(w in simplex(J)) Delta(w).             (3.2)
```

If `E(A,b)>0`, there is an optimal design supported on at most `2M+1`
frequencies.  When `A,b` are real, at most `M+1` frequencies suffice.

At a saddle point, if

```text
r=b-A^*lambda
```

is the weighted least-squares residual, then

```text
A*W*r=0,
|r_k|<=E(A,b) for every k,
|r_k|=E(A,b) on supp(w),                              (3.3)
```

and the primal optimal nuller is explicitly

```text
h=W*r/E(A,b).                                        (3.4)
```

#### Proof

For `r_lambda=b-A^*lambda`,

```text
||r_lambda||_infinity^2
 =max_(w in simplex(J)) sum_k w_k|r_lambda,k|^2.     (3.5)
```

The right side is convex in `lambda` and affine in `w`.  Quotienting out
`ker(A^*)` and restricting to a sufficiently large finite-dimensional
sublevel set makes the first variable compact without changing the
infimum.  Finite-dimensional minimax therefore gives

```text
E(A,b)^2
 =max_w min_lambda ||W^(1/2)(b-A^*lambda)||_2^2.     (3.6)
```

Weighted least squares evaluates the inner minimum as (3.1).  This proves
(3.2).  Saddle-point optimality gives the normal equation and the
equioscillation statements (3.3).  Formula (3.4) then satisfies

```text
A*h=0,       ||h||_1=1,       <b,h>=E(A,b).          (3.7)
```

Finally, `A*W*r=0` writes zero as a convex combination of the vectors
`a_k r_k` in `C^M=R^(2M)`.  Caratheodory reduces the support to `2M+1`;
the real case gives `M+1`.  QED.

### Exterior-power / DPP form

There is an exact fermionic reformulation of the same certificate.  Let
`mu` be a probability design, write

```text
G=integral a(xi)a(xi)^*d mu(xi),
H=integral v(xi)v(xi)^*d mu(xi),
```

where `v` is the augmented `(M+1)`-vector chosen so that `H` has blocks
`[[G,g],[g^*,c]]` (in the conventions of (3.1), this may put `conj(b)` in
the last coordinate).  If `G` is nonsingular, Andreief's identity and the
Schur determinant formula give

```text
Delta(mu)=det(H)/det(G)
 =1/(M+1) *
   [integral_(Omega^(M+1)) |det[v(xi_0),...,v(xi_M)]|^2 d mu^(M+1)]
   /[integral_(Omega^M) |det[a(xi_1),...,a(xi_M)]|^2 d mu^M]. (3.7a)
```

The factor is exactly `M!/(M+1)!=1/(M+1)`.  Formula (3.7a) is undefined as
a determinant ratio when `G` is singular; then (3.1)'s pseudoinverse form is
the correct statement (or one first quotients by the null feature space).
It is a determinantal-point-process volume ratio built from independently
chosen legal frequencies.  Thus it does not literally introduce a single
frequency outside the allowed aperture.  It is nevertheless algebraically
the same scalar `Delta`: determinant expansion uses `(M+1)`-fold products,
and any estimate that treats those products as a new physical test must pay
the corresponding tensor/conductor bill.  The form may expose useful
Vandermonde or DPP structure for a specially chosen `mu`, but supplies no
normalization loophole by itself.

### What is genuinely gained

The required all-coefficient statement (1.3) can now be attacked by finding
one probability design `w` for which the explicit PSD Schur complement
satisfies

```text
Delta(w)>=Y^(-2*kappa+o(1)).                         (3.8)
```

Only `2M+1` actual frequencies are ever needed, even though the permitted
band contains far more modes.  This removes the need to control every dual
coefficient simultaneously in a proof certificate.  It also suggests an
adaptive search: alternate weighted least squares with an adversary that
moves mass toward the largest residuals.

What is not gained is a generic lower bound.  If the principal vector `b`
is well approximated by an actual prime-log quadrature, every Schur
complement in (3.2) is small.  Uniform or random designs reproduce the old
square-root scale; a successful proof must show that an **actual arithmetic
design** has a much larger residual.

### Reproducible actual-node check

Run

```text
python3 results/prime_wiener_adversarial_design_probe.py
```

in the real-cosine restriction.  With width `.2`, `alpha=.49`, and
bandwidth `2Y`, it returns

| `Y` | nodes `M` | modes | `E_cos` | `sqrt(Delta(w))` | support |
|---:|---:|---:|---:|---:|---:|
| 50 | 7 | 63 | .0384635354 | .0384635354 | 8 |
| 100 | 9 | 147 | .0357121314 | .0357121314 | 10 |
| 200 | 17 | 338 | .0344078623 | .0344078623 | 18 |
| 300 | 23 | 545 | .0372626993 | .0372626993 | 24 |

The weighted normal-equation residuals are below `5e-16`; LP/dual/Schur
agreement is at `1e-14` or better.  At `Y=300` and the previously used full
finite aperture ratio `18.9`, all three values are `.0553954589` and the
design again has `M+1=24` atoms.  This verifies the identity and sparsity,
not an asymptotic lower bound for the full complex `E_Y`.

### Continuous Remez/exchange card

The finite grid can be removed.  On a compact legal band `Omega`, put

```text
E_Omega=inf_lambda sup_(xi in Omega)
        |b(xi)-<a(xi),lambda>|.                       (3.9)
```

The same minimax proof, now over probability measures on `Omega`, gives

```text
E_Omega^2
 =max_(omega in Prob(Omega)) min_lambda
   integral_Omega |b(xi)-<a(xi),lambda>|^2 d omega(xi). (3.10)
```

In the real-cosine problem, an optimal measure has at most `M+1` atoms.
Write these as `(xi_l,w_l)`, let `s_l` be the sign of the residual, and
suppose for clarity that an atom is in the interior of `Omega`.  The exact
saddle/stationarity equations are

```text
r(xi_l)=s_l*E_Omega,
r'(xi_l)=0,                                          (3.11)

sum_l w_l*s_l*a(xi_l)=0,       sum_l w_l=1,
w_l>0.                                               (3.12)
```

At a band endpoint the derivative equation is replaced by the appropriate
one-sided extremum condition.  Equation (3.11) follows either because every
support point maximizes `|r|`, or by differentiating the optimized Schur
complement with respect to `xi_l` when the weighted least-squares minimizer
is locally unique (equivalently, after removing redundant directions, the
weighted design has full rank):

```text
partial_(xi_l) Delta=2*w_l*r(xi_l)*r'(xi_l).         (3.13)
```

For `M+1` interior atoms, (3.11)--(3.12), together with the `M`
coefficients `lambda` and `E`, form a square nonlinear system.  There is no
general ordered `+,-,+,-` alternation theorem here: the highly oscillatory
prime-log feature family is not a Chebyshev system on the full band.  Equal
modulus and stationary interior support are the invariant assertions.

The new script

```text
python3 results/prime_wiener_continuous_exchange_probe.py --full-aperture
```

implements a semi-infinite cutting-plane/Remez loop:

1. solve the Chebyshev LP on the current frequency set;
2. search for sign-changing stationary points on an oversampled grid and
   refine those found;
3. add the worst violating extrema and repeat;
4. recover a sparse signed design on the final extrema.

For `B=Y^(50/33)`, width `.2`, and `alpha=.49`, the exploratory output is

| `Y` | `M` | `B` | `E_Omega` | support | median support frequency | median gap |
|---:|---:|---:|---:|---:|---:|---:|
| 100 | 9 | 1072.3 | .06842194 | 10 | 388.2 | 90.8 |
| 300 | 23 | 5665.2 | .05541187 | 24 | 2856.2 | 145.4 |
| 1000 | 61 | 35111.9 | .04046958 | 62 | 16401.1 | 502.8 |
| 3000 | 151 | 185509.2 | .03157984 | 152 | 105746.8 | 793.3 |

For the first three rows the sampled exchange discrepancy is about `1.4e-6`
relatively or less, prime-null residuals are below `4e-15`, and refined
interior derivatives are below `3e-13`.  At all four scales the sparse design
uses `M+1` atoms and
spreads them across a macroscopic fraction of the full band; it is not a
low-frequency cluster.  The signs do not exhibit simple total alternation.
At `Y=3000` the sampled exchange discrepancy is `1.79e-6` and the prime-null
residual is `2.30e-13`; the local fitted exponent from `Y=1000` to `3000` is
about `.226`, with no credible asymptotic inference from this range.  A
different diagnostic is strikingly flat:

```text
Y                         300       1000      3000
E_Omega*(log Y)^(5/3)    1.009      1.014     1.011.
```

Thus the same data are also compatible with polylogarithmic decay; meanwhile
`E_Omega*sqrt(M)` rises from `.266` to `.316` to `.388`.

These are exploratory sampled values, not certificates for the global
continuous supremum: fixed oversampling can miss two derivative zeros in one
cell.  A certified exchange implementation would need interval root
isolation or an analytic zero-count bound for each residual derivative.

A short-range log-log fit gives an apparent exponent between `.226` and
`.26`, but the polylogarithmic diagnostic above makes even its qualitative
meaning unclear.  The useful conjecture-mining observation is
structural instead: an extremal design appears saturated (`M+1` atoms),
globally distributed, and controlled by irregular high-frequency prime-log
resonances.  A plausible analytic target is therefore a lower bound for the
continuous Schur system (3.11)--(3.12), not a uniform-grid mean square.
This continuous problem is a relaxation/conjecture engine; if a particular
compact model mandates a discrete frequency grid, rounding the atoms still
requires a uniform Lipschitz and barycentric-conditioning estimate.

---

## 4. Best mechanism II: quantum/noncommutative ancillas do not enlarge the carrier

Let `(mathcal A,phi)` be a unital `C*`-algebra with a state, and allow
arbitrary left/right ancilla coefficients `L_k,R_k`.  Define

```text
h_k=phi(L_k^*R_k),
E_L=sum_k phi(L_k^*L_k),
E_R=sum_k phi(R_k^*R_k).                              (4.1)
```

### Theorem 4.1 (linear-state ancilla compression)

If the scalar prime readouts vanish,

```text
sum_k exp(i*xi_k*u_j)h_k=0       for every j,        (4.2)
```

then

```text
|sum_k b_k h_k|
 <=E(A,b)*sqrt(E_L*E_R)
 <=E(A,b)*(E_L+E_R)/2.                              (4.3)
```

The same conclusion holds if the stronger operator-valued expressions
inside (4.2) vanish before applying `phi`.  Conversely, scalar coefficients
embedded in `mathcal A=C` attain equality in both normalized formulations:

```text
sup |sum_k b_k h_k|/sqrt(E_L*E_R)=E(A,b),
sup 2*|sum_k b_k h_k|/(E_L+E_R)=E(A,b).              (4.3a)
```

Both suprema are attained by scalar factorization with
`E_L=E_R=||h||_1`.  Thus, if one instead imposes `E_L+E_R<=1`, the optimum
raw cross amplitude is `E(A,b)/2`.  These assertions cover arbitrary
ancillas representable in the diagonal linear form (4.1).  Shared
cross-frequency readouts `phi(L_k^*R_l)`, `k!=l`, are not covered unless
they are expanded into output-frequency coefficients and charged the
corresponding direct-sum energy.

#### Proof

Choose phases `omega_k` so that
`omega_k phi(L_k^*R_k)=|phi(L_k^*R_k)|`.  Cauchy--Schwarz in the direct sum
of the GNS Hilbert spaces gives

```text
sum_k |h_k|<=sqrt(E_L*E_R).                           (4.4)
```

After dividing by the right side, `h` is feasible in (1.2), proving the
first inequality.  The second is arithmetic--geometric mean.  Scalar sharp
Wiener factorization proves the converse.  QED.

This theorem directly audits the compact two-leg constraint: ancillas can
redistribute the same scalar cross coefficients, but they cannot reduce
their projective/Wiener energy.  Free Khintchine or matrix concentration may
make noncommuting words orthogonal before readout; the state compression
(4.1) restores the scalar ledger.

### QSP and lossless-control corollaries

A scalar QSP or lossless-FIR output is a Laurent polynomial

```text
p(z)=sum_k h_k z^k,       |p(z)|<=1 on |z|=1.        (4.5)
```

Bounded-real normalization controls `||p||_infinity`, whereas compact
two-leg realization costs `||p||_A=sum|h_k|`.  Hence its normalized carrier
is

```text
|sum b_k h_k|/||p||_A<=E(A,b).                       (4.6)
```

The gap can be a square root: a length-`N` Rudin--Shapiro polynomial,
normalized to have circle supremum at most one, has Wiener norm
`asymp sqrt(N)`.  Fejer--Riesz completes it to a lossless two-channel
polynomial.  Thus QSP unitarity can hide precisely the normalization loss
which reappears on descent to the compact carrier.

There is also an exact complementary-channel obstruction.  For a
paraunitary column `(p,q)` of degree `N`, with paraconjugation denoted by a
tilde,

```text
p(z)*p_tilde(z)+q(z)*q_tilde(z)=z^N.                 (4.7)
```

If `a!=0` and `p(a)=0`, then

```text
q(a)*q_tilde(a)=a^N!=0.                              (4.8)
```

So a lossless controller can cancel a pole or principal mode in one observed
channel only by placing it in the complementary channel.  A square
polynomial/Laurent paraunitary QSP matrix has determinant `c*z^d`, hence is
invertible at every `a!=0` and cannot annihilate a nonzero residue vector in
all channels.  This last statement is not asserted for arbitrary rational
inner matrices; scalar Blaschke factors already show why that broader claim
would be false.

If only one scalar channel is retained, the ordinary Schur/Pick bound
returns.  A Schur function with interior zeros `a_1,...,a_s` obeys

```text
|p(0)|<=product_j |a_j|.                              (4.9)
```

This reproduces, rather than improves, the exact compact two-leg ledger.
Map the selected point to zero and let the collateral assignments on the
right and left legs have Blaschke products `B_R,B_L`.  If the two selected
leg contributions must cancel and the total coefficient energy is one,
then

```text
max selected carrier
 <=[B_R^(-2)+B_L^(-2)]^(-1).                         (4.9a)
```

Here `selected carrier` means the squared selected cross coefficient when
the two branch norm-squares sum to one.  The physical polarized row still
carries its external `2/L^2` normalization (and any endpoint factor); (4.9a)
must not be conflated with the raw amplitude normalization in Theorem 4.1.
This is the existing harmonic-mean formula.  Lossless channel mixing cannot
beat its one-product exponent under exact-zero assignment.  Even replacing
zeros by a ninety-degree phase condition has a sharp Pick cost: if `r` is
the pseudohyperbolic distance between two interpolation points and the two
Schur values are orthogonal in phase, then

```text
|f(a)f(b)|<=r^2/[1+sqrt(1-r^4)].                     (4.9b)
```

For the half-plane pair `beta+-i*delta`, this is
`delta^2/(2*beta^2)+O(delta^4/beta^4)`.  Thus a phase-only QSP repair still
pays reciprocal-scale attenuation when both values come from one scalar
Schur interpolant.  The estimate alone does not rule out a two-function or
matrix tangential-Pick design.

For the tau--Li map `a_rho=1-tau/rho`, a zero with
`Re(rho)>tau/2` lies inside the disk.  Since

```text
sum_(rho: Re rho>tau/2) (1-|a_rho|)
 <<sum_(rho: Re rho>tau/2) (1+|Im rho|)^(-2)<infinity, (4.10)
```

an infinite Blaschke controller can even mask every hypothetical bad pole
while retaining nonzero gain.  Filtered analyticity alone therefore proves
nothing: requiring an invertible filter or control of every complementary
channel restores the original pole exclusion.

### Principal-mode audit

A single probability readout does not provide the required signed linear
observable.  Replacing an amplitude by a probability produces

```text
|p(exp(iu))|^2
 =sum_(k,l) h_k*conj(h_l)exp(i(k-l)u),               (4.11)
```

whose zero-frequency coefficient is `sum|h_k|^2>0`.  The desired polarized
sign is gone and a positive diagonal principal mode has been introduced.
Subtracting channels may restore a sign, but Theorem 4.1 applies only after
that architecture has actually been reduced to the diagonal form (4.1) and
its direct-sum energy has been charged; no categorical nonlinear-measurement
no-go is claimed here.

---

## 5. Sparse-sieve, Boolean-circuit, and adelic audit

The prime-power nodes have far more algorithmic structure than a generic
`M`-point set.  That does not automatically reduce their Wiener cost.  For
example, with `R>=sqrt(bY)` the exact small-prime sieve on integers
`n<=bY` is

```text
F_R(n)=1-product_(p<=R)(1-1_(p|n)),

1_(p|n)=(1/p)sum_(a mod p)exp(2*pi*i*a*n/p).         (5.1)
```

On an active window `[aY,bY]`, once `aY>R`, `F_R` vanishes exactly on primes
and equals one on composites.  Globally, primes `p<=R` instead have
`F_R(p)=1`, while `F_R(1)=0`.  The sparse higher prime powers can then be
corrected separately.  Although (5.1) has a short Boolean description, its
exact normalized additive Fourier norm on the primorial group is

```text
||product_(p<=R)(1-1_(p|.))||_A
 =product_(p<=R) 2*(1-1/p)
 =exp((log 2+o(1))*pi(R)).                            (5.2)
```

Writing `delta_R=product_(p<=R)(1-1/p)`, the exact norm of `F_R` is

```text
||F_R||_A=1+product_(p<=R)2*(1-1/p)-2*delta_R.       (5.2a)
```

Thus the literal term-by-term primorial compilation is exponentially costly
before transfer to logarithmic coordinates.  This group norm is not the
log-coordinate Wiener norm, however, and it supplies no lower bound for the
norm after the character terms have been recombined and transferred.

The logarithmic coordinate adds a second tax.  An additive character becomes

```text
u -> W(u)exp(2*pi*i*theta*Y*exp(u)).                  (5.3)
```

For fixed `theta` bounded away from zero, stationary phase gives

```text
||Fourier[(5.3)]||_1 asymp_W sqrt(Y).                 (5.4)
```

This is the exact scale already seen for the localized all-integer mask
`1-exp(2*pi*i*Y*exp(u))`.  But sieve characters include `theta=a/p` tending
to zero; their individual stationary-phase scale is instead
`sqrt(theta*Y)` in the oscillatory range, and cancellation among the many
chirps is uncontrolled.  Thus (5.4) does not establish a universal
`sqrt(Y)` transfer tax.

Equations (5.2)--(5.4) do **not** prove a universal `sqrt(Y)` lower bound for
every cleverly compiled sieve.  Different additive characters could cancel
after the nonlinear change of variables.  Proving that no such cancellation
beats `sqrt(M)` would itself be an all-coefficient theorem close to the open
extremal.  The correct assessment is therefore:

```text
Boolean/AKS circuit size => low Wiener cost:          FALSE;
literal primorial compilation before log transfer:   EXPONENTIALLY COSTLY;
generic fixed-theta log chirp:                        sqrt(Y) SCALE;
exceptional coherent compiled sieve:                 NOT RULED OUT,
                                                     but exactly an E_Y witness.
```

Tensor or arithmetic circuits do not evade the aperture either.  A degree
`q` product introduces integer products of length `Y^q`; the legal band is
below `Y^2`, so only the unamplified layer is available.  Nonlinear AND/OR
gates evaluated before scalar readout must be linearized into these product
frequencies, or else they no longer define the permitted compact
cross-correlation.

An adelic or character ancilla separates the local prime factors beautifully,
but the zeta carrier lives in the trivial spherical channel.  Applying that
state to any linear all-channel construction is exactly the compression in
Theorem 4.1.  Nontrivial characters have no copy of the zeta pole/principal
residue to cancel; projecting back to the spherical vector restores `E_Y`.
There is one genuine logical loophole: prove a coercive **all-character,
all-channel** tangential-Pick inequality and an independent implication from
that vector inequality to the scalar zeta sign.  No such bridge is present
here, and simple character averaging does not provide it.

---

## 6. Coding and control consequences

The code

```text
C=range(A^*) subset C^J                              (6.1)
```

has `E(A,b)` as the `l-infinity` distance of the logical word `b` from
`C`; a primal `h` is a parity check in `C^perp`.  Theorem 3.1 says that an
optimal logical check can be supported on at most `2M+1` symbols.  This is a
real reduction of the finite search space.

Ordinary code-distance amplification tensors the check matrix.  In the
prime-log model, the `q`-fold tensor introduces products of `q` integers and
requires frequency length beyond `Y^q`.  The available aperture
`Y^(50/33+o(1))` is below `Y^2`, so the first nontrivial product-code
amplification is unavailable.  Expander or LDPC language does not change
this conductor bill.

Likewise, balanced truncation or a lower bound on `G_w` alone is
insufficient.  The relevant invariant is the augmented Schur complement
(3.1), which includes the carrier/prime cross vector `g_w`.  Bounding its
three pieces separately recreates the old square-root loss.

---

## 7. Research decision

The only promoted mechanism is the adversarial-design certificate (3.8).
It is worth testing at larger actual-node scales because:

1. it uses frequencies only inside the legal polynomial aperture;
2. it needs at most `2M+1` of them;
3. it preserves the exact Wiener normalization and therefore descends to
   the existing compact two-leg construction;
4. it keeps the principal carrier in the augmented Gramian rather than
   smoothing it away.

A successful analytic theorem would construct arithmetic designs `w_Y`
with the Schur lower bound (3.8), uniformly in `Y`.  Generic random designs,
ordinary moments, matrix ancillas, QSP boundedness, and code tensoring do not
supply that theorem.

The concrete next computation is to solve the square continuous system
(3.11)--(3.12) from the exchange output, continue its `M+1` support atoms as
`Y` varies, and look for stable multiplicative/phase-cell structure in those
atoms and weights.  Any proposed pattern should then be interval-certified
against the full residual on `[0,Y^(50/33)]`.  Merely extending the three
floating data points cannot establish a power law.

The exact truth boundary is therefore

```text
adversarial Gramian identity and sparse witness:    PROVED;
finite actual-node verification:                    PASSED;
matrix/QSP ancilla improvement after descent:       IMPOSSIBLE;
uniform arithmetic Schur lower bound (3.8):         OPEN;
required E_Y lower bound:                           NOT PROVED;
uniform zeta zero-free strip:                       NOT PROVED.
```
