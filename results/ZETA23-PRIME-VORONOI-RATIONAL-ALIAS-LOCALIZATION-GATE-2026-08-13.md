# Prime-Voronoi rational-alias localization gate

**Date:** 2026-08-13

**Verdict:** the super-conductor part of the unresolved prime antenna can be
localized to a genuine minor-arc gap sum.  Let `P_Y(t)` be the positive
actual-prime Voronoi antenna from the mean-square-gap report.  For

```text
Y <= t <= Y^(50/33),       Q=Y^(1/10),       eta_t=sqrt(t)/Y,
```

delete every prime whose logarithmic Voronoi cell meets a point `x` at
which the local integer phase velocity

```text
omega_t(x)=t/(2*pi*x)
```

lies within `eta_t/q` of a reduced rational `a/q`, `q<=Q`.  The total
Voronoi coefficient mass deleted is

```text
O_epsilon(Y^(-181/6600+epsilon)),
181/6600=.0274242424...>.019>.0180303234.              (0.1)
```

Thus every low-denominator logarithmic chirp **stationary neighborhood at
this curvature resolution** in the entire range `[Y,Y^(50/33)]` is harmless
at the required power.  A full kill antenna is now implied by just two
estimates for the *same* Voronoi coefficients:

```text
sup_(Y^.751<=t<=Y) |P_Y(t)| <=Y^(-c),

sup_(Y<=t<=Y^(50/33)) |P_Y^minor(t)| <=Y^(-c),         (0.2)
```

for some `c>.0180303234`, where `P_Y^minor` is supported only on cells on
which

```text
|t/(2*pi*x)-a/q|>sqrt(t)/(Y*q)
for every reduced a/q with 1<=q<=Y^(1/10).             (0.3)
```

Neither estimate in (0.2) is proved here.  In particular, (0.3) does not
permit a coefficient-blind van der Corput argument: the coefficients are
consecutive-gap masses, and large-denominator gap aliases remain possible.
The theorem does, however, remove the natural curvature-scale neighborhoods
of all ordinary integer aliases, the parity alias, and every other
denominator through `Y^.1`, with fixed-power room.  It is a strictly smaller
arithmetic target than the undifferentiated tail.

No zeta bound or zero-free strip is claimed.

---

## 1. Physical-coordinate form of the Voronoi rule

Fix the shell

```text
I_Y=[Y*exp(-w),Y*exp(w)]
```

with fixed `0<w<1`.  Let `p_j` be the primes in this shell and let `C_j` be
their logarithmic Voronoi cells.  In physical coordinates the interior
boundaries are geometric means.  Put

```text
Phi_Y(x)=phi(log(x/Y)),
lambda_j=integral_(C_j) Phi_Y(x) dx/x,
P_Y(t)=sum_j lambda_j exp(i*t*log(p_j/Y)).              (1.1)
```

Taking real parts gives the cosine antenna.  Proper prime-power coordinates
retain coefficient zero.

For every union `U` of physical subintervals in `I_Y`, let `Cell(U)` be the
union of Voronoi cells meeting `U`.  Since `Phi_Y` is bounded,

```text
sum_(C_j meets U) lambda_j <<_w |Cell(U)|/Y.            (1.2)
```

If `R` is the number of connected components of `U`, then `Cell(U)` differs
from `U` by at most two boundary cells per component.  A physical Voronoi
cell has length bounded by a fixed multiple of the sum of its two adjacent
prime gaps.  Consequently Cauchy--Schwarz gives

```text
|Cell(U)|
 <<_w |U|+sqrt(R)*(sum_(p_j in I_Y^+) g_j^2)^(1/2),    (1.3)
```

where `g_j=p_(j+1)-p_j` and `I_Y^+` is a harmless fixed enlargement of the
shell.  Repeated boundary cells only improve this estimate.

Julia Stadlmann's mean-square-gap theorem supplies, for every fixed
`epsilon>0`,

```text
sum_(p_j in I_Y^+) g_j^2 <<_epsilon Y^(123/100+epsilon).
                                                                    (1.4)
```

Equations (1.2)--(1.4) are the only arithmetic input in the localization
theorem.

---

## 2. Low-denominator local aliases

For `t>=Y`, set

```text
K=t/Y,                 eta=sqrt(t)/Y.                  (2.1)
```

For `Q>=1`, define the rational-alias set

```text
M_t(Q)={x in I_Y:
        |t/(2*pi*x)-a/q|<=eta/q
        for some (a,q)=1, 1<=q<=Q}.                    (2.2)
```

The values of `t/(2*pi*x)` lie in an interval of length `asymp_w K`.
For a fixed denominator `q`, only `O_w(qK)` numerators occur.  Moreover

```text
|d/dx [t/(2*pi*x)]|asymp_w t/Y^2.                     (2.3)
```

Hence each component belonging to denominator `q` has physical length
`O_w(eta*Y^2/(q*t))`.  Summing first over its `O_w(qK)` numerators and then
over `q<=Q` gives

```text
|M_t(Q)|<<_w Q*eta*Y=Q*sqrt(t),                       (2.4)

number of components R_t(Q)<<_w K*Q^2.                (2.5)
```

Overlap only decreases the left sides.

### Theorem 2.1 (rational-alias Voronoi mass)

Uniformly for `Y<=t<=Y^A`, with fixed `1<=A<2`,

```text
sum_(C_j meets M_t(Q)) lambda_j
 <<_(w,epsilon)
 Q*sqrt(t)/Y + Q*sqrt(t)*Y^(-177/200+epsilon).         (2.6)
```

#### Proof

Apply (1.3) to (2.4)--(2.5), then use (1.4):

```text
|Cell(M_t(Q))|/Y
 << Q*sqrt(t)/Y
    +[sqrt((t/Y)*Q^2)*Y^(123/200+epsilon)]/Y

 =  Q*sqrt(t)/Y
    +Q*sqrt(t)*Y^(-177/200+epsilon).                   (2.7)
```

Now use (1.2).  QED

The second term is the price of the prime gaps at the boundaries of all
major-arc components.  It is larger than the geometric-length term at the
present unconditional mean-square-gap exponent.

---

## 3. Exact exponent at the legal aperture

Take

```text
A=50/33,              Q=Y^(1/10).                     (3.1)
```

The two savings in (2.6), evaluated at the largest legal `t`, are

```text
d_length
 =1-A/2-1/10
 =8/33-1/10
 =47/330
 =.1424242424...,

d_boundary
 =177/200-A/2-1/10
 =177/200-25/33-1/10
 =181/6600
 =.0274242424....                                     (3.2)
```

The boundary term dominates, proving (0.1).  The available room over the
conservative antenna exponent `.019` is

```text
181/6600-.019=.0084242424....                          (3.3)
```

Thus the auxiliary epsilon in
[Stadlmann's theorem](https://arxiv.org/abs/2212.10867) can be fixed small
enough without approaching the required threshold.

More generally, denominators `q<=Y^r` can be removed with saving

```text
d_alias(r)=177/200-25/33-r=841/6600-r.                (3.4)
```

To remain beyond the exact strip-route threshold `delta_*`, it suffices that

```text
r<841/6600-delta_*=.1093939187....                     (3.5)
```

The rational choice `r=1/10` leaves a comfortable theorem margin.

---

## 4. The exact remaining quotient

Let

```text
G_t(Q)={j:C_j does not meet M_t(Q)},

P_Y^minor(t)=sum_(j in G_t(Q))
             lambda_j exp(i*t*log(p_j/Y)).             (4.1)
```

Theorem 2.1 and positivity of the Voronoi weights give

```text
|P_Y(t)-P_Y^minor(t)|
 <=sum_(C_j meets M_t(Q))lambda_j
 <<Y^(-181/6600+epsilon)                               (4.2)
```

uniformly on the super-conductor range.  Every cell occurring in (4.1)
satisfies the pointwise Diophantine condition (0.3) throughout the cell.

Combining (4.2) with the already proved Voronoi low-band theorem yields the
following exact successor gate.

### Corollary 4.1 (two-regime successor gate)

If, for one fixed `c` with

```text
.0180303234<c<181/6600,
```

the two estimates (0.2) hold (with harmless `Y^epsilon` room), then the
same positive actual-prime Voronoi coefficients give a full-aperture dual
antenna of exponent `c`.

The first line of (0.2) is a compact transition problem from the proved
`.751` endpoint to the one-prime conductor.  The second is a genuinely
minor-arc, high-denominator consecutive-gap sum.  In particular it no
longer contains the curvature-scale neighborhoods of:

```text
integer local aliases (q=1);
the parity local alias (q=2);
or any reduced rational local alias with q<=Y^.1.       (4.3)
```

This decomposition matches the numerical aperture sweep: the optimized
extremal changes mainly after `B` reaches the one-prime conductor.  The
numerics are motivation only; no numerical value enters the proof.

---

## 5. Why the minor estimate is still arithmetic

Condition (0.3) is not enough for a coefficient-blind exponent-pair bound.
On consecutive primes, the phase increment is

```text
t*log(p_(j+1)/p_j),                                    (5.1)
```

and a large-denominator rational relation can make (5.1) nearly integral
even when the local derivative avoids every rational of denominator
`<=Y^.1`.  Arbitrary positive subsequences of the integers can manufacture
such aliases while satisfying excellent mesh and gap-moment bounds.

What (4.1) asks for is narrower: prove cancellation for the **actual**
consecutive-prime path after every low-denominator local resonance has been
removed.  A suitable theorem could take the form

```text
sup_(Y<=t<=Y^(50/33))
 |sum_(j in G_t(Y^.1)) lambda_j exp(i*t*log(p_j/Y))|
 <=Y^(-c),                                             (5.2)
```

with `c>.0180303234`.  This is not the ordinary smooth-`Lambda` twist and
does not carry its standard bump-family quantifiers.  Conversely, another
Lebesgue moment or exceptional-set count does not prove (5.2), because the
required conclusion is pointwise.

The strongest current unconditional prime-gap theorem therefore removes
the complete low-denominator major-arc sector with power to spare, but no
published theorem found in the literature audit controls (5.2).  The
remaining gate is a signed/nonlattice estimate for inverse-density gap
weights, exactly where the prior renewal and ordinary mean-value arguments
stop.

---

## 6. Reproduction

The rational exponent identities and margins are replayed by

```bash
python3 results/verify_prime_voronoi_rational_alias_gate.py
```

The checker audits the power ledger; it is not a substitute for
Stadlmann's imported mean-square-gap theorem.
