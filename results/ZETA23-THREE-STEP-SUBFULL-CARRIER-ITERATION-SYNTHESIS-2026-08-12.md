# Three-step iteration on the sub-full carrier frontier

Status: synthesis of one certified finite falsification experiment, one exact
low-dimensional arithmetic reduction, and one exact normalized near-tie
pruning theorem, 2026-08-12.  No uniform arithmetic sign, divisor-isolation
theorem, improved zero-free region, or RH statement is proved.

## 1. Outcome

The three planned decisions have now been executed.

| step | question | exact outcome |
|---|---|---|
| 1 | Does the direct constrained arithmetic edge quickly become negative under adversarial phase/depth/aperture/jet variation? | No negative was found in 61,896 full-carrier and 11,565 multi-`theta` finite slices.  The closest sample was rebuilt with Arb and proved strictly positive. |
| 2 | Can `q_(theta*kappa)` be reduced to a smaller theorem than a full-carrier prime-polynomial bound? | Yes.  Every fixed companion direction gives an exact two-dimensional Ritz formula and one joint three-scalar orientation inequality.  Separate magnitude bounds do not prove it. |
| 3 | Can an `alpha-o(1/L)` near-tie realize the previously constructed malicious transverse reservoir in normalized two-packet geometry? | Not in the separated fixed-width packet class after all corresponding positive rows are imposed.  The corrected Gram family has a Hermite collision limit, while the dominant mirror cross terms retain one sign. |

These outcomes materially prune the search, but do not tighten any known
bound on a zeta zero.  They leave a narrower coupled frontier:

```text
ARITHMETIC:
  prove a uniform joint-orientation admission inequality for an explicit
  zero-independent companion plane (or a comparably small Ritz space);

DIVISOR GEOMETRY:
  extend fixed-width mirror alignment to the target-only carrier slice,
  or exhibit a legal proportional-width state where a near-tie really
  reaches carrier scale;

CONTRADICTION:
  combine the two results on the same target-conditioned quotient.
```

Finite positivity in Step 1 proves neither of the two uniform inputs.

## 2. Step 1: adversarial direct-`q` scan and proof interface

For the target-only selected-null space let

```text
N=kappa*a*a^*,
q_(theta*kappa)(K_ar)
 =max {Tr(K_ar Gamma):
       Gamma>=0, Tr Gamma=1, Tr(N Gamma)>=theta*kappa}.
```

The new scanner varies height, target ordinate inside the dyadic band,
critical-grid phase, aperture, endpoint-jet order, target depth, and retained
carrier fraction.  The selected row is rebuilt with its exact phase factor;
using the old centered numerator at nonzero phase would condition on the
wrong row.

### 2.1 Finite decision result

The broad full-carrier scan covered 61,896 valid configurations.  The focused
multi-`theta` scan covered another 11,565 valid slices at
`theta in {0.9,0.99,1}`.  Neither produced a negative value at tolerance
`1e-10`.

The closest normalized sample was

```text
T=16, gamma/T=1.31, phase=0.49,
aperture=0.32, jet order=1, alpha=0.499,
q_kappa/kappa=0.02576213669.
```

At that same matrix,

| `theta` | `q_(theta*kappa)/kappa` |
|---:|---:|
| 0.90 | `0.507571839` |
| 0.99 | `0.083068428` |
| 1.00 | `0.025762137` |

This was not left as a floating sign.  A 192-bit Arb replay at the rational
parameters proved

```text
kappa
 =[0.1676783712331281021155089714978195237836 +/- 4.75e-41],

q_kappa
 =[0.004319753120250996038800722197058190834782 +/- 2.59e-43]
 >0.
```

Monotonicity in `theta` proves positivity for all smaller `theta` at this one
finite matrix only.  It says nothing between scan points or at unbounded
height.

### 2.2 Proof-producing negative certificate

The rigorous path does not use a floating nullspace.  It constructs:

1. an exact rational RREF basis `E` for the endpoint-moment kernel;
2. an Arb pivot elimination of the selected positive row;
3. the nonorthogonal Gram form `G=B^*B`, arithmetic form `K=B^*K_ar B`,
   and rank-one carrier `N`; and
4. an interval no-pivot `LDL^*` test of

   ```text
   (mu*theta*kappa-delta)G-K-mu*N >0.
   ```

A successful test proves

```text
q_(theta*kappa)(K_ar)<=-delta
```

on the entire specified finite selected-null space.  The implementation
correctly rejects a false negative claim at the closest actual sample and
certifies a separately labelled shifted calibration.  Thus the fail-fast
interface is now rigorous even though no actual negative was found.

### 2.3 Interpretation

This is a meaningful failed falsification attempt, not evidence for a
uniform theorem.  More finite positive samples cannot prove admission.  The
most useful future numerical action is adaptive minimization followed by
interval replay of every near-zero candidate; a single certified negative
would kill that proposed uniform geometry.

The full report and implementation are
[`ZETA23-SUBFULL-DIRECT-Q-FAILFAST-AND-ARB-CERTIFICATE-2026-08-12.md`](ZETA23-SUBFULL-DIRECT-Q-FAILFAST-AND-ARB-CERTIFICATE-2026-08-12.md),
[`subfull_direct_q_failfast.py`](../src/subfull_direct_q_failfast.py), and
[`test_subfull_direct_q_failfast.py`](../src/test_subfull_direct_q_failfast.py).

## 3. Step 2: exact two-dimensional Ritz/Loewner gate

Write the arithmetic matrix relative to the carrier line as

```text
N=kappa*a*a^*,       ||a||=1,
K=[[r,b^*],[b,D]] on C*a direct_sum a^perp.
```

For any fixed unit companion `w perpendicular a`, put

```text
d=<w,Dw>,       c=abs(<w,b>).
```

Every carrier-rich state in `span{a,w}` has the phase-optimized Rayleigh
quotient

```text
F_w(x)=x*r+(1-x)*d+2*c*sqrt(x*(1-x)),
theta<=x<=1.
```

Hence

```text
q_(theta*kappa)(K)>=max_(theta<=x<=1) F_w(x).
```

Let

```text
Delta=sqrt((r-d)^2+4*c^2),
lambda_+=(r+d+Delta)/2,
p_+=(1+(r-d)/Delta)/2.
```

When `Delta>0`, the exact constrained Ritz edge is

```text
lambda_+,     if p_+>=theta,
F_w(theta),   if p_+<theta.
```

If `Delta=0`, the compression is scalar and the edge is simply `r=d`;
`p_+` need not be defined.

In particular the single boundary inequality

```text
theta*r+(1-theta)*d
 +2*sqrt(theta*(1-theta))*c >= -epsilon*kappa
```

is a sufficient admission certificate.  It is strictly weaker than a lower
bound on the full-carrier scalar `r`: transverse orientation can pay the
weighted negative diagonal deficit.

### 3.1 What arithmetic theorem is actually new

There are two choices for `w`.

- A geometry/background/confluent companion independent of the primes keeps
  `r,d,<w,b>` as three **linear** completed prime/pole/gamma scalars.  This
  exposes the smallest useful new target: a joint orientation inequality.
- The one-step Lanczos companion `w=P_(a^perp)Ka/||P_(a^perp)Ka||` maximizes
  the coupling, but uses `<a,K^2a>` and `<a,K^3a>`.  It trades a linear
  prime problem for target-adaptive quadratic and cubic correlations.

The current KMT estimate applied separately to the three linear entries
still leaves normalized size

```text
sqrt(X)/L^(13/10)
```

against carrier `X^alpha/L`, a ratio
`X^(1/2-alpha)/L^(3/10)`.  It therefore cannot prove the orientation
certificate at fixed `alpha<1/2`.  Rank-two Loewner displacement alone also
does not sign it, because arbitrary confluent diagonal data can make the
compression negative scalar.

Floating diagnostics show that the first Lanczos plane captured roughly
`98%--99%` of the computed full `q_.9` at `T=64,128,256,512`; a fixed
background-plus-confluent three-dimensional plane captured roughly
`71%--87%`.  Those favorable finite values are diagnostics only, and their
full-carrier scalar was already positive.

The exact theorem card is
[`ZETA23-SUBFULL-RITZ-LOEWNER-ADMISSION-GATE-2026-08-12.md`](ZETA23-SUBFULL-RITZ-LOEWNER-ADMISSION-GATE-2026-08-12.md),
with implementation in
[`carrier_ritz_loewner_gate.py`](../src/carrier_ritz_loewner_gate.py).

## 4. Step 3: normalized near-tie Gram and mirror alignment

On a centered fixed-width packet put

```text
M(s)=integral exp(s*t)dt,
e_(alpha,gamma)(t)=exp((alpha-i*gamma)t)/sqrt(M(2*alpha)).
```

For mean depth `alpha_bar` and parameter differences
`Delta alpha,Delta gamma`, the exact two-row Gram determinant is

```text
det G
 =1-|M(2*alpha_bar+i*Delta gamma)|^2
      /[M(2*alpha_bar-Delta alpha)
        M(2*alpha_bar+Delta alpha)].
```

The mean-depth dependence corrects the earlier suggested formula.  At a
collision,

```text
det G
 =Var_(2*alpha_bar)(t)
   *(Delta alpha^2+Delta gamma^2)+O(|Delta|^4),
```

and the divided difference tends to the normalized centered Hermite row

```text
(t-E_(2*alpha_bar)t)e_(alpha_bar,gamma_bar).
```

The four reflected branches have two singular values of constant size and
two comparable to `|Delta|`.  Thus a gap `L^(-2)` costs only a polynomial
factor.  Collision itself is not the fixed-power obstruction.

### 4.1 The mirror-sign theorem

For two fixed-width packets separated by `D=dL`, the carrier-leading block
of pair `j` has the form

```text
K_j,cross=U_j V_j^*+V_j U_j^*.
```

If every corresponding positive row is imposed, then

```text
U_j(ell)+V_j(r)=0,
```

and hence exactly

```text
Re <ell,P_F K_cross r>
 =-sum_j c_j*|V_j(r)|^2.
```

The terms cannot cancel by changing near-tie angles or passing to Hermite
directions.  Genuine same-lobe terms are smaller than the dominant cross
carrier by `exp(-alpha D)`, and reverse cross terms by `exp(-2 alpha D)`.
The conclusion remains carrier-scale when the aggregate weak-block error is
explicitly `o(kappa)`; merely saying there are polynomially many pairs is not
enough.

Therefore the earlier malicious abstract two-pair block is not realizable at
carrier scale in this normalized separated fixed-width packet class after
all its positive rows are imposed.  The result transfers to the finite
growing endpoint-jet model for the finite compact-packet family.

### 4.2 Scope at the end of Step 3

The all-positive-row theorem itself does **not** cover:

1. proportional-width lobe states, whose same-lobe separations may themselves
   be proportional to `L`;
2. the target-only direct-`q` quotient, which imposes the selected positive
   row but not every collateral positive row (the follow-on in Section 5
   settles this extension negatively);
3. the actual prime/pole/gamma matrix, which is not a positive sum of the
   reflected-pair cross blocks; or
4. a uniform divisor-isolation theorem.

The result therefore prunes one concrete normalized near-tie escape without
proving that all deep collateral screening is impossible.

The exact report is
[`ZETA23-NEAR-TIE-GRAM-AND-MIRROR-ALIGNMENT-2026-08-12.md`](ZETA23-NEAR-TIE-GRAM-AND-MIRROR-ALIGNMENT-2026-08-12.md),
with checks in
[`near_tie_packet_gram.py`](../src/near_tie_packet_gram.py).

## 5. Follow-on: the target-only phase flip

The proposed target-only extension is false in the same normalized
fixed-width packet class.  For packet separation `D`, a collateral ordinate
gap `delta` has ideal expectation on the selected negative carrier

```text
m_beta*(1-cosh(beta*D)*cos(delta*D)),
```

with relative local-width error `O(w/D)` at `delta=pi/D`.  Thus a collateral
pair at either gap `+/-pi/D` sees the selected negative carrier as its own
positive carrier direction.

One equal-depth pair cancels the selected value to `o(kappa)` and therefore
destroys every uniform `-c*kappa` margin, without fixing the residual sign.
More decisively, choose two distinct collateral pairs at gaps `+pi/D` and
`-pi/D`, both at depth

```text
beta=alpha-epsilon_L,
epsilon_L>0,       epsilon_L*D ->0.
```

The target remains strictly deepest, while the exact normalized three-pair
form on its full-carrier vector is

```text
-kappa+2*(1-o(1))*kappa=(1-o(1))*kappa>0.
```

The compact packets, full reflected-pair remainder, and growing endpoint
jets contribute only `o(kappa)`.  An `O(1)` cluster of this kind is permitted,
but not implied, by current count, density, simplicity, and leading-moment
inputs.  It is not asserted to occur among zeta zeros.

The obvious multiscale repair also fails universally.  A positive ensemble
over separations produces the cosine transform of a positive effective-delay
measure.  If all delays stay away from zero, that transform must change sign.
Forcing it nonnegative imports mass at zero separation, where the carrier is
only local scale; unit normalization then loses the fixed power
`X^(alpha*d-o(1))`.  A coherent autocorrelation square restores the cross-scale
arithmetic terms rather than giving a positive ensemble for free.

The remaining loophole is finite and adaptive: a separation profile tailored
to a known finite collateral list is an explicit convex-feasibility problem.
No current theorem solves it with all coherent arithmetic terms retained.

See
[`ZETA23-TARGET-ONLY-PHASE-FLIP-GATE-2026-08-12.md`](ZETA23-TARGET-ONLY-PHASE-FLIP-GATE-2026-08-12.md),
[`ZETA23-SEPARATION-AVERAGE-POSITIVE-COSINE-NOGO-2026-08-12.md`](ZETA23-SEPARATION-AVERAGE-POSITIVE-COSINE-NOGO-2026-08-12.md),
and the independent
[`ZETA23-PHASE-FLIP-AND-SEPARATION-AVERAGE-REFEREE-ADDENDUM-2026-08-12.md`](ZETA23-PHASE-FLIP-AND-SEPARATION-AVERAGE-REFEREE-ADDENDUM-2026-08-12.md).

## 6. Coupled conclusion

The three results are useful together because they isolate two different
quantifiers that cannot replace one another.

1. Step 1 tests and certifies a zero-independent arithmetic matrix on the
   target-only quotient.  It found no finite counterexample, but proves no
   uniform sign.
2. Step 2 shows that a proof need not control the full matrix or even the
   full-carrier scalar.  It may prove one carrier-rich joint orientation
   inequality in a fixed low-dimensional plane.
3. Step 3 shows that the simplest normalized fixed-width near-tie model does
   not generate the adverse transverse orientation once all its positive
   rows are imposed.
4. The follow-on shows that this sign does not survive the target-only
   quotient used in Steps 1--2: reciprocal-separation phase flips give an
   explicit normalized screen compatible with all current bulk zero inputs.

Accordingly the best next analytic target is not a larger blind scan and not
three separate exponential-sum estimates.  It is:

> Choose an explicit zero-independent geometry/background companion `w` and
> prove the **joint completed orientation inequality** for
> `(r,d,<w,b>)`.  On the divisor side, either solve the adaptive finite-list
> separation problem with all arithmetic cross terms retained, or supply new
> zeta-specific local spacing/depth information that rules out the proved
> phase-flip screen.

Pure packet geometry and current count/moment inputs cannot provide the
second half.  A successful arithmetic half without a new divisor input is
only admission; a successful divisor input without the arithmetic half is
only isolation.  A strip would come from their contradiction on the same
quotient.

## 7. Verification and truth boundary

The focused executable suites cover the interval certificate, Ritz formula,
collision/Hermite limit, and mirror-sign algebra.  They are computational
checks of the displayed finite formulas; only the Arb replay and interval
`LDL^*` success paths are interval certificates.

No statement in this synthesis:

- locates an off-critical zeta zero;
- excludes one;
- improves a classical zero-free region;
- proves or disproves a uniform zero-free strip;
- proves RH; or
- asserts independence from ZFC.

The numerical bound on a zeta zero has therefore not moved.  What moved is
the frontier: one finite geometry survived a rigorous falsification attempt,
the arithmetic theorem was reduced to a precise joint orientation target,
one previously open normalized near-tie mechanism was excluded in its
fixed-width/all-positive-row scope, and its target-only extension was then
falsified by a genuine reciprocal-separation packet configuration.  Universal
positive separation averaging was also pruned at fixed-power carrier scale.
