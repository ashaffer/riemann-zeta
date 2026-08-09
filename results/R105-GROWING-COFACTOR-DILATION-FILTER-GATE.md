# R105 growing cofactor-dilation filter gate

Status: exact dilation/cofactor action, squarefree Ramanujan tensor identity,
complete-period norm ledger, zero-carrier exponent ledger, and a critical
shift-span no-go are proved.  A growing filter does not by itself give an
arithmetic power saving beyond the exponent compression of the modes it is
supposed to detect.  No fixed zero-free strip is proved or disproved.

Successor qualification (R123): this report treats products of the
single-modulus operators `A_q`, whose expansion has total shift span
`sum log q`.  R123 instead truncates the integer Mobius divisor sum directly;
that operator has span `log Y` and exactly collapses a free cofactor up to
`Y`.  It evades the particular span obstruction here but leaves the same
balanced `mu(d)Lambda(b)` endpoint, so the final fixed-strip status is
unchanged.

Date: 2026-08-07.

Predecessors:

* [`MOBIUS-TWO-SHIFT-RENORMALIZATION-GATE.md`](MOBIUS-TWO-SHIFT-RENORMALIZATION-GATE.md)
  for the faithful Vaughan cofactor depth and cutoff-gauge obstruction;
* [`FINITE-RAMANUJAN-NULL-GAUGE-GATE.md`](FINITE-RAMANUJAN-NULL-GAUGE-GATE.md)
  for finite Ramanujan null gauges and their zero Schur complement;
* [`R104-QH-FINITE-COFACTOR-SECTOR-THEOREM.md`](R104-QH-FINITE-COFACTOR-SECTOR-THEOREM.md)
  for the center-annihilated finite cofactor tail.

## 1. Verdict

Put

```text
f_R(t)=t^(-1/2)V_Q(R-log t),
F_(d,b)(R)=sum_(m>=1)f_R(mdb),
A_q=tau_(-log q)-q^(-1/2).                              (1.1)
```

The proposed coefficient action is exact, including its normalization:

```text
A_q F_(d,b)(R)
 =q^(-1/2)sum_(m>=1)(q 1_(q|m)-1)f_R(mdb).             (1.2)
```

For distinct primes `p|D`, the whole product is exactly

```text
product_(p|D) A_p F_(d,b)(R)
 =sum_(m>=1)c_D(m)/sqrt(D) f_R(mdb),                   (1.3)
```

where `D` is squarefree and `c_D` is the Ramanujan sum.  Thus the most
natural growing prime sieve is a single normalized Ramanujan column, not a
new multiplicative cancellation mechanism.

There are then three rigorous regimes.

```text
fixed filter                     bounded coordinate change;
shift span L=o(R)                only exp(o(R)) gain or loss;
shift span L comparable to R     effective scale R is replaced by R-L. (1.4)
```

The faithful frozen Vaughan block has shift/cofactor depth

```text
L=O(R/k)=o(R).                                             (1.5)
```

Hence every filter which stays inside the R77/R104 cofactor identity is
subpower.  A filter with `L` proportional to `R` leaves that identity.  If
it is applied to the complete field, its elementary bound and every
off-axis zero carrier are compressed by the same effective-scale change.
If it is applied only to the frozen tail, the omitted cutoff-shell and
completion terms are no longer negligible; R77 proves that these terms
preserve the common zeta principal part with multiplier one.

On a complete residue period, (1.3) has mean-square gain

```text
(1/D)sum_(m mod D)|c_D(m)/sqrt(D)|^2=phi(D)/D.          (1.6)
```

Even the product of all primes up to `y` therefore gives only
`asymp 1/log y` in energy.  Reaching a full period requires `D` no larger
than the free-cofactor range, and hence again `log D=o(R)`.  If `D` is much
larger than that range, the filter is precisely a long Ramanujan null
gauge of the R82 kind; there is no complete-period contraction and no
positive Schur floor.

The branch is therefore closed as an **automatic** source of a fixed power.
A power saving for the actual signed Vaughan weights after (1.3) would be a
genuinely new global joint estimate.  It is not supplied by the dilation
algebra, and it is at least as zero-sensitive as the remaining R104 bulk.

## 2. Exact action on the free cofactor

The square-root factor in (1.2) is important.  Directly from (1.1),

```text
f_(R-log q)(t)=sqrt(q)f_R(qt).                           (2.1)
```

Consequently

```text
tau_(-log q)F_(d,b)(R)
 =sqrt(q)sum_(m>=1)f_R(qmdb)
 =sqrt(q)sum_(q|m)f_R(mdb),                             (2.2)
```

and subtracting `q^(-1/2)F_(d,b)` proves (1.2).

For an arbitrary finite list `q_1,...,q_r`, put

```text
D=product_(1<=j<=r)q_j,
q_S=product_(j in S)q_j.                                (2.3)
```

Expanding the commuting translations gives the exact coefficient formula

```text
product_j A_(q_j)F_(d,b)(R)
 =sum_m B_(q_1,...,q_r)(m)f_R(mdb),                     (2.4)

B_(q_1,...,q_r)(m)
 =D^(-1/2)sum_(S subset {1,...,r})
   (-1)^(r-|S|)q_S 1_(q_S|m).                           (2.5)
```

The average of (2.5) over any common period is zero: the average of
`q_S 1_(q_S|m)` is one, and

```text
sum_S(-1)^(r-|S|)=0.                                    (2.6)
```

Thus every nonempty product annihilates the continuum/constant cofactor
mode.  This is the coefficient form of

```text
A_q exp(R/2)=0.                                         (2.7)
```

If the `q_j` are pairwise coprime, divisibility by `q_S` factors and (2.5)
becomes

```text
B_(q_1,...,q_r)(m)
 =D^(-1/2)product_j(q_j 1_(q_j|m)-1).                   (2.8)
```

For distinct primes this is

```text
B_D(m)=D^(-1/2)product_(p|D)c_p(m)=c_D(m)/sqrt(D),      (2.9)
```

which proves (1.3).

Repeated or overlapping moduli do not obey (2.8); (2.5) is the correct
formula.  Repetition is not a hidden independent sieve.  It creates nested
divisibility spikes.  For example

```text
A_q^2 F:
B_(q,q)(m)=q^(-1)[q^2 1_(q^2|m)-2q 1_(q|m)+1],         (2.10)
```

whose complete-period mean square is `1-q^(-2)`, already closer to one
than the first filter's `1-q^(-1)`.  The third repeat already has mean
square

```text
(q-1)(q^2+4q+1)/q^3>1,              q>=2.             (2.11)
```

Thus repetitions amplify the nested divisibility fibers rather than
accumulate independent mean-square contraction.

## 3. Complete-period sieve ledger

For squarefree `D`, additive-character orthogonality gives

```text
sum_(m mod D)|c_D(m)|^2=D phi(D).                       (3.1)
```

Equation (1.6) follows.  For

```text
D_y=product_(p<=y)p,                                    (3.2)
```

Mertens' product theorem gives

```text
phi(D_y)/D_y=product_(p<=y)(1-1/p)
            asymp exp(-gamma)/log y.                   (3.3)
```

Thus a fully sampled prime tensor supplies a logarithmic energy gain, not
a fixed power.  More generally, the minimal order of `phi(D)/D` implies

```text
phi(D)/D >> 1/log log(3D)                               (3.4)
```

up to an absolute constant.  No squarefree complete-period tensor has a
power-small root-mean-square norm.

There is also no uniform contraction for arbitrary coefficient sequences.
Indeed

```text
c_D(D)=phi(D),
max_(m mod D)|c_D(m)/sqrt(D)|=phi(D)/sqrt(D).            (3.5)
```

The small complete-period average is balanced by large divisibility spikes.
Using (1.6) against the actual Vaughan weights therefore needs a
distribution theorem for those signed weights across the `D` residue
classes.  Orthogonality alone does not provide it.

If `m<=M<D`, then

```text
c_D(m)=mu(D/g)phi(g),       g=(D,m),
|c_D(m)|<=g<=m<=M.                                     (3.6)
```

This can make every displayed coefficient in (1.3) look tiny when
`D>>M^2`.  It is not a sampled sieve gain: the active interval sees less
than one period.  In the extreme case in which every `p|D` exceeds `M`,

```text
c_D(m)=mu(D),                    1<=m<=M,               (3.7)
```

so (1.3) is merely the scalar `mu(D)/sqrt(D)` on the whole active range.
This is exactly the top-prime Ramanujan null-gauge phenomenon in R82.

## 4. Real-frequency conditioning

Translations are unitary on `L^2(dR)`.  The Fourier multiplier of `A_q`
on the real axis is

```text
a_q(t)=exp(-it log q)-q^(-1/2),                         (4.1)
```

and hence

```text
1-q^(-1/2)<=|a_q(t)|<=1+q^(-1/2).                      (4.2)
```

For `P=product_j A_(q_j)`, Plancherel gives

```text
product_j(1-q_j^(-1/2)) ||F||_2
 <=||PF||_2
 <=product_j(1+q_j^(-1/2)) ||F||_2.                    (4.3)
```

In particular every fixed filter is boundedly invertible on the real
Fourier axis.  It cannot change a horizontal exponential order.

For the prime tensor `P_y=product_(p<=y)A_p`, the PNT and partial summation
give

```text
sum_(p<=y)p^(-1/2)<<sqrt(y)/log(2y),                    (4.4)
```

so

```text
exp[-O(sqrt(y)/log(2y))]||F||_2
 <=||P_yF||_2
 <=exp[ O(sqrt(y)/log(2y))]||F||_2.                    (4.5)
```

Even when `log D_y` is of order `y`, this is a subexponentially
conditioned change of real-frequency coordinates.  Therefore a power
estimate does not follow from the filter norm.  Any such estimate must use
new cancellation in the transformed arithmetic coefficients.

## 5. Exact zero-carrier compression

On an exponential mode `exp(lambda R)`,

```text
A_q exp(lambda R)
 =(q^(-lambda)-q^(-1/2))exp(lambda R).                  (5.1)
```

For a zeta-zero carrier `lambda=rho-1/2`, this is

```text
q^(-1/2)(q^(1-rho)-1)exp[(rho-1/2)R].                  (5.2)
```

It is nonzero whenever `1/2<Re(rho)<1`.  For `D_y` in (3.2), define

```text
M_y(rho)=D_y^(-1/2)product_(p<=y)(p^(1-rho)-1).         (5.3)
```

Writing `beta=Re(rho)` and using the triangle and reverse-triangle
inequalities gives

```text
D_y^(1/2-beta) product_(p<=y)(1-p^(beta-1))
 <=|M_y(rho)|
 <=D_y^(1/2-beta) product_(p<=y)(1+p^(beta-1)).         (5.4)
```

For fixed `1/2<beta<1`, the PNT implies

```text
log D_y=theta(y)=y+o(y),
sum_(p<=y)p^(beta-1)<<_beta y^beta/log(2y).             (5.5)
```

Therefore

```text
log|M_y(rho)|
 =-(beta-1/2)y+O_beta(y^beta/log(2y))+o(y).             (5.6)
```

This is a real and strong compression of an off-axis zero mode.  It is not
an arithmetic saving: it is the exact spectral multiplier of the detector.

To see the critical cost, let

```text
||F||_alpha=sup_R exp(-alpha R)|F(R)|,     alpha<1/2.  (5.7)
```

The exact forward-shift inverse is

```text
A_q^(-1)
 =sum_(r>=0)q^(-r/2)tau_((r+1)log q),                  (5.8)
```

and consequently

```text
||A_q^(-1)||_alpha
 <=q^alpha/(1-q^(alpha-1/2)).                           (5.9)
```

The factor `q^alpha` is sharp on the positive carrier `exp(alpha R)`.
For a product with

```text
L=sum_j log q_j,                                       (5.10)
```

reconstruction pays `exp(alpha L)` before the denominator ledger.  This
is exactly the scale transported backward by the filter.  At the critical
exponent `alpha=1/2`, the Neumann inverse ceases to be bounded.

Thus the small complex-frequency multiplier in (5.6) cannot be counted as
a saving and then inverted for free.  It is the amount by which the filter
has attenuated the very carrier that would witness an off-axis zero.

## 6. Effective-scale theorem

The preceding ledger can be stated without inversion.  Suppose

```text
L_y=log D_y=lambda R+o(R),       0<=lambda<1.           (6.1)
```

The expansion of `P_y` has `2^(pi(y))=exp(o(y))` translated terms.  If the
unfiltered completed field has its critical elementary bound

```text
|F(S)|<=exp(S/2+o(R))                                  (6.2)
```

uniformly for `(1-lambda)R+o(R)<=S<=R`, then every subset term in `P_yF(R)`
is at most

```text
exp[(R-L_y)/2+o(R)].                                   (6.3)
```

Indeed the coefficient of the translate by `log q_S` is
`D_y^(-1/2)sqrt(q_S)`, while (6.2) at `S=R-log q_S` is
`exp(R/2)/sqrt(q_S)` up to subexponential factors.  Hence

```text
|P_yF(R)|<=exp[(R-L_y)/2+o(R)].                         (6.4)
```

On the other hand, (5.6) maps a zero carrier with
`delta=beta-1/2>0` to size

```text
exp[delta(R-L_y)+o(R)].                                (6.5)
```

Comparing (6.4) and (6.5) gives only

```text
delta<=1/2,                                             (6.6)
```

the original critical bound.  Both sides have undergone the exact
replacement

```text
R  ->  R-L_y.                                          (6.7)
```

More generally, a bound

```text
|P_yF(R)|<=exp[(1/2-eta)(R-L_y)+o(R)]                  (6.8)
```

would imply the desired exclusion `beta<=1-eta`; but (6.8), not the
dilation identity, is precisely a fixed-power arithmetic estimate on the
remaining signed field.

The condition `lambda<1` is essential.  If `L_y>=R-O(1)`, some translates
reach the initial/support boundary, where the asymptotic zero-carrier
expansion is not uniform.  Counting (5.3) while discarding those boundary
transients would falsely make known critical-line carriers disappear.

## 7. Why the Vaughan cofactor cannot support a long filter

R77's faithful frozen-tail identity has

```text
m<=exp[O(R/k)],
H=O(R/k),
k -> infinity,
R/k=o(R).                                               (7.1)
```

The product `P` contains translations all the way back by

```text
L=sum_j log q_j.                                       (7.2)
```

For every translated term to remain in the same frozen Vaughan block one
must have

```text
L<=H=O(R/k)=o(R).                                      (7.3)
```

Then (4.3), (5.1), and (5.9) show that all gains, losses, and carrier
changes are `exp(o(R))`.  A fixed horizontal exponent is unchanged.

Taking `L` proportional to `R` creates two different objects which must
not be conflated.

1. Applying `P` to the **complete field** is legitimate, but gives the
   effective-scale ledger of Section 6 and no automatic strip.
2. Applying the Ramanujan coefficient `B_D(m)` only to the **frozen
   Vaughan tail** leaves the safe block.  Re-freezing the cutoff at each
   translated scale creates shell, Type-I, and completion terms.  R77's
   exact cutoff-flow theorem says their common zero principal part has
   multiplier one.  Omitting them is exactly the forbidden separate-
   cofactor truncation.

This is the critical-cost no-go.  The long filter needed for a fixed power
is incompatible with the short free-cofactor identity on which its
coefficient interpretation rests.

## 8. Relation to the R82 null gauge

Equation (2.9) places the filter directly inside the finite Ramanujan frame
of R82.  Two endpoints reproduce its conclusions.

* If `p>M`, then `c_p(m)=-1` throughout the active range `m<=M`.  Such a
  prime filter is a scalar coordinate adjustment, not arithmetic
  cancellation.
* If enough periods are present to use Ramanujan orthogonality, the exact
  ledger is only (3.3), and the physical sequence can still concentrate
  on the divisibility spikes (3.5).

R82 proves that inserting these null columns moves the center among
nonzero modes with a polylogarithmic coefficient cost, while the joint
Moore--Penrose Schur complement remains exactly zero.  Tensoring the same
columns does not manufacture a positive coercive direction.  Any estimate
which treats `c_D(m)/sqrt(D)` as independently small but drops its cross
terms is a basis-dependent estimate, not an estimate of the completed
field.

## 9. Final disposition

```text
exact A_q action on m                         PROVED
distinct-prime product = c_D/sqrt(D)          PROVED
complete-period energy factor phi(D)/D        PROVED
fixed/safe-span power gain                    IMPOSSIBLE FROM FILTER
long-filter zero exponent compression         EXACTLY QUANTIFIED
long-filter reconstruction/transport cost     CRITICAL
R77 frozen-tail compatibility                 ONLY FOR L=o(R)
R82 Schur coercivity                           ZERO
new signed joint Vaughan--Ramanujan estimate   OPEN
fixed zero-free strip                          NOT PROVED OR DISPROVED. (9.1)
```

The only potentially productive descendant is not another dilation
identity.  It would have to prove cancellation of the actual balanced
`mu(d)Lambda(b)` tail against the long Ramanujan cofactor
`c_D(m)/sqrt(D)`, with every cutoff-shell and completion cross term kept.
By Sections 5--7, its claimed gain must be measured **after** the exact
zero-carrier multiplier is removed.  No such surplus gain is presently
derived.
