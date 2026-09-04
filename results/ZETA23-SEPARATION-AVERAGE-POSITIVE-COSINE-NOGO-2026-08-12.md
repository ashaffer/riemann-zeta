# Positive separation averaging cannot preserve a fixed-power carrier

Status: exact carrier-leading packet kernel, exact positive-cosine support
theorem, and a quantitative normalization no-go, 2026-08-12.  The result
rules out a universal positive separation/modulation average in the
separated fixed-width packet class.  It does not rule out a profile tailored
to a finite known list of collateral ordinates, and it proves no zero-free
strip.

## 1. Verdict

The target-only phase flip is real.  On the selected negative carrier, a
same-depth collateral pair with ordinate gap `omega` has carrier-leading
contribution

```text
-b(D)*A(omega)*cos(omega*D+phi(omega)),              (1.1)
```

where `D` is the packet separation, `b(D)>0` is of order
`exp(alpha*D)`, and the fixed-width overlap factor
`A exp(i phi)` is independent of `D`.  Thus a single separation with
`omega*D` near `pi` has the wrong sign.

A tempting repair is a positive ensemble of separations whose normalized
cosine transform is nonnegative.  It fails at exactly the carrier scale
needed here:

1. After including the exact fixed-width overlap, the multiplier in (1.1)
   is the cosine transform of a **positive effective-delay measure**.  Its
   support is `D+[-w,w]`, where `w` is the fixed packet width.
2. A nonzero positive measure supported a positive distance from zero
   cannot have a globally nonnegative cosine transform.
3. If separations down to effective delay zero are admitted, global
   nonnegativity forces at least `Omega(epsilon/L)` of the cross-normalized
   mass into `|delay|<=epsilon`.  Those are `D=O(w+epsilon)` blocks, whose
   selected carrier is only the local packet scale, not
   `exp(alpha*d*L)`.
4. After unit covariance/ensemble normalization, the retained carrier is at
   most `L^O(1)` times the local packet scale.  Relative to a packet at
   `D=dL`, this loses

   ```text
   exp(-alpha*d*L)*L^O(1)=X^(-alpha*d+o(1)),         (1.2)
   ```

   a fixed power.

In the point-packet idealization there is a sharper **conditional** statement.
If the carrier-weighted phase measure itself is required to have globally
nonnegative cosine transform, the exact negative mirror eigenvalue is
quadratic at `D=0` and the witness norm diverges.  Global positivity of the
actual cross-weighted measure does not automatically transfer to this
carrier-weighted measure.  The general conclusion is therefore the
finite-width fixed-power loss in (1.2), proved independently below.

Therefore a Fejer/autocorrelation profile does not close the target-only
collateral problem.  Its nonnegative constant mode is purchased from
near-zero-separation blocks with no fixed-power carrier.  A coherent
superposition which manufactures a squared Fourier transform is not this
positive ensemble: its off-diagonal cross-scale arithmetic terms return,
exactly as in the multi-witness/multiscale SDP audit.

## 2. Exact fixed-width phase kernel

Let

```text
J=[-w/2,w/2],
M(q)=integral_J exp(q*s) ds,
p_q(ds)=exp(q*s) ds/M(q).                            (2.1)
```

Put two copies of `J` at centers `-D/2` and `D/2`.  For a reflected pair
`(alpha_j,gamma_j)`, the two exponential branches are

```text
A_j(t)=exp(( alpha_j-i*gamma_j)*t),
B_j(t)=exp((-alpha_j-i*gamma_j)*t).                  (2.2)
```

The norm product of the dominant left--right rank-one block is exactly

```text
b_j(D)=c_j*exp(alpha_j*D)*M(2*alpha_j),              (2.3)
```

where `c_j>0` is the common explicit-form normalization.  The reverse
cross block and same-lobe blocks have the already-audited relative scales
`exp(-2*alpha_j*D)` and `exp(-alpha_j*D)`.

Let pair `0` be selected and take its target-aligned negative cross mode.
Set

```text
omega=gamma_j-gamma_0,
q=alpha_0+alpha_j,
a_0j=M(q)^2/[M(2*alpha_0)*M(2*alpha_j)].             (2.4)
```

Log-convexity of `M` gives `0<a_0j<=1`.  Direct multiplication of the two
normalized local overlaps gives, up to conjugating the whole expression
according to the inner-product convention,

```text
M(q+i*omega)^2/[M(2*alpha_0)*M(2*alpha_j)]
 =a_0j*(integral exp(i*omega*s) p_q(ds))^2.          (2.5)
```

Consequently the exact carrier-leading expectation of pair `j` on the
selected cross mode is

```text
-b_j(D)*a_0j
 *integral cos(omega*(D+s_1+s_2))
           p_q(ds_1)*p_q(ds_2).                    (2.6)
```

Changing the row convention replaces `s_1+s_2` by `s_1-s_2`; nothing below
changes.  In either convention the local variable lies in `[-w,w]` and its
law is positive.  Formula (2.6), rather than a bare informal cosine, is the
exact fixed-width kernel.  At `j=0`, `omega=0` and `a_00=1`, so it has the
selected negative sign.

If `alpha_j=alpha_0-delta`, then (2.3) contributes the additional positive
tilt

```text
b_j(D)/b_0(D)=constant*exp(-delta*D).                (2.7)
```

Thus unequal depth only reweights a positive delay measure.  It does not
alter the support argument below.

Now give separations positive ensemble weight `dw(D)` and define

```text
B_0=integral b_0(D) dw(D),
dnu(D)=b_0(D)dw(D)/B_0.                              (2.8)
```

For a fixed depth gap, the normalized version of (2.6) is the real Fourier
transform of the positive measure obtained from `nu`, the positive tilt in
(2.7), and the two local laws in (2.6).  If

```text
D in [D_-,D_+],       D_->w,                        (2.9)
```

that effective measure is supported in
`[D_--w,D_++w]`, a positive distance from zero.

## 3. The positive-cosine support theorem

### Theorem 3.1 (a universal positive profile needs zero delay)

Let `mu` be a nonzero finite positive measure on the real line.  If

```text
C_mu(t)=integral cos(t*x) mu(dx)>=0    for every real t,  (3.1)
```

then the support of `mu` cannot be separated from zero after
symmetrization.  In particular, no nonzero positive measure supported in
`[a,A]`, with `0<a<A<infinity`, satisfies (3.1).

#### Proof

Replace `mu` by its symmetrization `sigma`; then `C_mu` is the Fourier
transform of `sigma`.  Suppose `sigma` vanishes on `(-a,a)`.  Choose
`0<epsilon<a` and the triangular function

```text
tau_epsilon(x)=(1-|x|/epsilon)_+.                   (3.2)
```

Its Fourier transform is nonnegative.  Hence

```text
h=sigma*tau_epsilon                                 (3.3)
```

has nonnegative Fourier transform and is a continuous positive-definite
function.  The support gap gives `h(0)=0`.  Every positive-definite function
satisfies

```text
|h(x)|<=h(0),                                       (3.4)
```

by its `2 x 2` Gram minor.  Thus `h` is identically zero.  But both factors
in (3.3) are nonnegative and nonzero, so their convolution has positive
integral.  Contradiction.  QED

The theorem includes atomic ensembles.  Equivalently, a finite cosine
polynomial with positive coefficients and no zero-frequency atom has Bohr
mean zero, so it cannot be everywhere nonnegative unless it is zero.

Applied to (2.6)--(2.9), Theorem 3.1 proves:

> No positive average over genuinely separated fixed-width packets makes
> every possible collateral phase nonpositive while retaining a nonzero
> selected cross block.

The conclusion is unaffected by a positive depth tilt, a bounded packet
offset, or a bounded modulation jitter: these only convolve or reweight the
same positive delay measure, and its support remains away from zero.

## 4. Quantitative central mass and carrier loss

The support theorem also identifies the cost of allowing small separations.

### Lemma 4.1 (central mass of a positive-cosine probability)

Let `sigma` be a symmetric probability supported in `[-A,A]` and suppose
its Fourier transform is nonnegative.  For `0<epsilon<=A`,

```text
sigma([-epsilon,epsilon])>=epsilon/(8*A).           (4.1)
```

#### Proof

Use `h=sigma*tau_epsilon` as above.  Positive definiteness gives
`h(x)<=h(0)`, while

```text
h(x)>=(1/2)*sigma([x-epsilon/2,x+epsilon/2]),
h(0)<=sigma([-epsilon,epsilon]).                    (4.2)
```

At most `4*A/epsilon` intervals of the displayed type cover `[-A,A]`.
Sum (4.2) over such a cover and use total mass one.  QED

The order `epsilon/A` is sharp: the triangular probability on `[-A,A]`
has Fourier transform proportional to `sinc(A*t/2)^2` and has that order of
central mass.

### Theorem 4.2 (unit-norm carrier cap)

Assume the fixed packet width is `w=O(1)`, all physical separations lie in
`[0,A]`, and `A=O(L)`.  Give unit packet states positive weights `dw(D)` and
normalize their total covariance trace by

```text
W=integral dw(D)=1.                                 (4.3)
```

Suppose their cross-normalized effective-delay measure has globally
nonnegative cosine transform.  Then for any fixed `epsilon>0`, Lemma 4.1
and the support `D+[-w,w]` imply

```text
nu([0,w+epsilon]) >= c*epsilon/(A+w).               (4.4)
```

On this interval (2.3) is bounded by a local packet constant

```text
b_0(D)<=b_loc
 :=c_0*M(2*alpha_0)*exp(alpha_0*(w+epsilon)).        (4.5)
```

Equations (2.8), (4.3), and (4.4) now give

```text
1=B_0*integral b_0(D)^(-1) nu(dD)
 >=B_0*c*epsilon/[(A+w)*b_loc],

B_0<=C*b_loc*(A+w)/epsilon.                         (4.6)
```

The exact negative eigenvalue of the normalized mirror block is

```text
n_0(D)=m_0*(cosh(alpha_0*D)-1),                     (4.7)
```

whereas its cross coefficient is `m_0*cosh(alpha_0*D)` and its dominant
cross branch is comparable with (2.3).  Hence `n_0(D)<=C*b_0(D)` uniformly,
so the selected carrier of the unit-trace ensemble obeys

```text
K=integral n_0(D)dw(D)
 <=C*B_0
 <=C'*b_loc*L.                                     (4.8)
```

All omitted constants are independent of `L`.  A single state at
`D=dL`, `d>0`, instead has

```text
n_0(dL)=b_loc*exp(alpha_0*dL+O(1))
       =b_loc*X^(alpha_0*d+o(1)).                   (4.9)
```

Thus (4.8) loses the fixed power stated in (1.2).  Any polynomial endpoint-
jet or finite interpolation factor merely changes the `X^o(1)` term.

There is also a conditional point-packet formulation.  Suppose the phase
measure normalized directly by the selected carrier `n_0(D)` is itself
required to have globally nonnegative cosine transform.  Unit trace then
requires

```text
integral n_0(D)^(-1) dnu_n(D)<infinity.             (4.10)
```

But (4.1) holds at every `epsilon`, and
`n_0(D)=m_0*alpha_0^2*D^2/2+O(D^4)`.  Therefore

```text
integral n_0(D)^(-1)dnu_n(D)
 >=constant*epsilon^(-2)*nu_n([0,epsilon])
 >=constant/(A*epsilon) -> infinity.               (4.11)
```

So exact carrier normalization is impossible in this narrower zero-width
model.  This does not follow merely from positivity of the `b_0`-weighted
cross measure used in Theorem 4.2.  The independently proved finite-width
result (4.8) is the general statement needed here: local jitter permits
effective zero delay at `D=O(w)`, but only at local, non-carrier scale.

## 5. What modulation can and cannot change

A common modulation of both packets changes `gamma_0` and `gamma_j` by the
same amount, so `omega=gamma_j-gamma_0` and the target-aligned phase
`omega*D` do not change.  An independent constant lobe phase is absorbed in
the selected negative eigenvector and also cancels from the relative phase.

A bounded spatial offset or a positive modulation average which genuinely
produces a cosine transform adds a bounded random delay to (2.6).  This is
already covered by convolution with the local law.  If

```text
D_- > w + modulation_radius,                        (5.1)
```

Theorem 3.1 still applies.  Reaching zero effective delay requires a
modulation/offset range comparable with `D=Theta(L)`, outside the separated
fixed-width regime; Theorem 4.2 then charges the construction to the
small-delay blocks and removes the fixed-power carrier.

One can obtain a manifestly nonnegative multiplier

```text
|integral exp(i*omega*D)a(D)dD|^2                  (5.2)
```

from an autocorrelation.  But (5.2) is quadratic in the profile.  A
positive ensemble of separate Weil forms is linear in its weights and gives
`integral cos(omega*D)dnu(D)`, not (5.2).  Realizing (5.2) with one coherent
test function retains every `D,D'` cross term.  Those are the off-block
prime, pole, archimedean, and collateral terms of the coherent multiscale
problem; deleting them while keeping (5.2) is inconsistent.

## 6. The finite-frequency loophole

The universal quantifier over `omega` is essential.  Given a finite known
list `omega_1,...,omega_m` and an allowed interval `I`, a tailored positive
profile exists exactly when

```text
conv { (cos(omega_1*D),...,cos(omega_m*D)) : D in I }
  intersects R_+^m.                                 (6.1)
```

If it exists, Caratheodory gives a profile with at most `m+1` atoms.  By
finite-dimensional separation, (6.1) fails exactly when there are
`lambda_j>=0`, not all zero, such that

```text
sup_(D in I) sum_j lambda_j*cos(omega_j*D)<0.        (6.2)
```

The exact packet problem replaces each cosine coordinate by (2.6) and adds
the positive depth tilt; the same convex criterion holds.

Nothing in the present zero-count, density, simplicity, or pair-correlation
inputs proves (6.1) uniformly for the actual collateral list.  Conversely,
Theorem 3.1 does not prove that every finite actual list violates (6.1).
This adaptive finite-list problem is therefore open, but it is a concrete
linear feasibility problem rather than a universal positive-kernel escape.

## 7. Relation to the multi-witness and multiscale no-go

The ensemble above is logically legitimate because all weights are
nonnegative.  Its covariance is

```text
Gamma=integral z_D*z_D^* dw(D)>=0.                  (7.1)
```

If its complete averaged Weil form were negative, one constituent would be
negative.  But the exact completion identity is also averaged with the same
weights.  Aggregate cancellation of a raw-prime row therefore charges the
selected carrier to a pole/archimedean/collateral or off-block term of the
same size; changing separation phases supplies no free arithmetic row.

On one common admissible space, the one-real-row SDP has a rank-one
extremizer.  On a labelled direct sum of genuinely different separations,
the aligned mirror blocks all have the same sign once their positive rows
are imposed.  In the present target-only quotient the collateral positive
rows are not imposed, which is why the single-`D` phase flip (1.1) remains a
real issue.  Theorems 3.1 and 4.2 show that positive separation averaging
does not solve that issue uniformly at fixed-power scale.

If instead one forms a coherent superposition across `D`, the covariance
has off-diagonal blocks and the arithmetic operator must be evaluated on
them.  This is precisely the surviving `R` term in the robust multi-witness
inequality, not a contradiction to that audit.

## 8. Exact scope

What is proved:

| statement | status |
|---|---|
| exact fixed-width carrier-leading phase kernel | proved in (2.3)--(2.6) |
| positive profile supported away from zero has globally nonnegative cosine transform | impossible |
| allowing effective zero delay while keeping unit ensemble norm retains fixed-power carrier | impossible; carrier is at most local scale times `L^O(1)` |
| finite atomic profile without `D=0` has global nonnegative cosine response | impossible |
| coherent autocorrelation square is a positive ensemble | false; off-diagonal terms are required |

What is not proved:

1. A profile tailored to a finite actual collateral list may satisfy (6.1).
2. The full proportional-width packet space is not reduced to the fixed-
   width delay law used here.
3. The actual von Mangoldt operator may have target-transverse directions
   unrelated to separation averaging.
4. No uniform arithmetic admission inequality, divisor-isolation theorem,
   or zero-free strip follows.

The less-obvious escape is therefore pruned in its proposed universal form:
nonnegative cosine averaging is possible only by inserting the zero-delay
constant mode, and that mode costs the entire fixed-power carrier advantage.
