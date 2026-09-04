# High primitive height: supported Newton information and a stable alias theorem

**Date:** 2026-08-25  
**Scope:** symmetric reciprocal chart, frequencies `|h|,|k|,|m|<=H`  
**Verdict:** the high-`p` support gap is a genuine conditioning barrier, not
an exact loss of injectivity.  Supported low frequencies can identify a
primitive direction with infinite precision, but their best sensitivity to
Farey-neighbor directions is only

```text
H/p^2.                                               (0.1)
```

At Newton-coefficient noise `eta=D^(-7/48)`, distinct directions therefore
become uniformly indistinguishable once

```text
p >>sqrt(H/eta)=D^(29/48).                          (0.2)
```

This is only `D^(7/96)` above the canonical support edge
`sqrt(H)=D^(17/32)`.  Higher Newton differences do not restore the lost
information; they are smaller by powers of `Q`.

There is a stronger sampled-packet statement.  On a block
`N=D^(11/16)`, Farey neighbors have correlations tending to one once

```text
p>>sqrt(H*N)=D^(7/8),                               (0.3)
```

and their entire aligned sampled phases are within `eta` once

```text
p>>sqrt(H*N/eta)=D^(91/96).                         (0.4)
```

An explicit infinite family shows this phenomenon on genuine non-square,
off-axis residual points in the energy core.  The family varies the centre
`Q`; consequently it is a uniform inverse-theorem obstruction, not a
fixed-`Q` high-multiplicity counterexample.  The actual prime-power support
may be sparser still.  Thus this theorem rules out unique recovery of the
virtual `p^2`/`p^3` fingerprint from supported Newton jets alone; it does
not rule out an arithmetic cluster bound or prove the sharp four-cycle
estimate.

## 1. Exact stationary support

Put

```text
chi=gcd(p+d,p-d),
a=(p+d)/chi,        b=(p-d)/chi.                    (1.1)
```

For the normalized reciprocal phase

```text
Phi(t)=h/(4t)+k/(4(1-t))-m*t,                       (1.2)
```

stationarity at `t=(p+d)/(2p)=a/(a+b)` is exactly

```text
p^2*(a^2*k-b^2*h)=chi^2*a^2*b^2*m.                 (1.3)
```

Since `gcd(p,chi*a*b)=1`, (1.3) forces

```text
p^2 | m.                                            (1.4)
```

If `|m|<p^2`, then `m=0`, and coprimality of `a,b` gives

```text
(h,k)=ell*(a^2,b^2).                                (1.5)
```

Every nonzero stationary frequency therefore has sup norm at least

```text
min(p^2,max(a^2,b^2)) >=p^2/4.                     (1.6)
```

Equivalently, the stationary lattice is the rank-two orthogonal lattice to
the primitive vector

```text
(chi^2*a^2*b^2, -p^2*b^2, p^2*a^2),                (1.7)
```

whose Euclidean norm, hence lattice covolume, is comparable with `p^4` in
a compact collar.  The divisibility argument supplies the sharp elementary
first-minimum lower bound (1.6).

Thus there is no nonzero supported exact stationary normal whenever
`p^2>4H`.  At exponent level this is `p>H^(1/2)`.  The constant cannot be
silently discarded in a literal finite theorem: for parity `chi=2`, the
zero-dual generator may have size near `p^2/4`, so some modes persist in
the short constant-width range `sqrt(H)<p<=2sqrt(H)`.

## 2. The actual integer Newton quotient

Sample the physical reciprocal phase by

```text
phi_(xi,t,Q)(s)=2Q*Phi_xi(t+s/(2Q)),     s in Z.    (2.1)
```

Repeated use of the fundamental theorem of calculus gives, exactly,

```text
Delta^r phi(s)
 =(2Q)^(1-r) integral_[0,1]^r
   Phi^(r)(t+(s+u_1+...+u_r)/(2Q)) du.              (2.2)
```

For `r=1`, the `-m*t` term contributes the integer `-m`; for `r>=2` it
vanishes.  Hence `m` is exactly invisible after quotienting by the integer
Newton lattice.  This is the real discrete quotient, not a continuous
surrogate.

Let `t,t'` lie in a fixed compact collar and let `delta=|t-t'|`.  From
(2.2), uniformly for all supported frequencies,

```text
dist_T(Delta^r phi_t,Delta^r phi_t')
 <<H*delta*Q^(1-r),             r=1,2,3.             (2.3)
```

The first coefficient dominates.  Conversely, a probe with `h` comparable
to `H` and `k=0` gives the reverse bound as long as `H*delta<1/10` and the
collar is split at its finitely many wrap points.  Therefore the local
metric induced by **all** supported Newton jets is

```text
d_Newton(t,t') asymp H*|t-t'|.                      (2.4)
```

This proves both sides of the information statement:

* exact supported probes remain locally injective;
* no inverse based only on those probes can be uniformly more stable than
  (2.4).

All supported frequencies provide only the two base torus responses of the
`h` and `k` coordinates and their integer multiples up to `H`; the `m`
coordinate adds no quotient information.

## 3. Farey neighbors saturate the conditioning

For every odd `p`, take the primitive directions

```text
(p,d)=(p,1),             (p',d')=(p+2,1).           (3.1)
```

Their tangent parameters obey the exact identity

```text
|t-t'|=1/[p*(p+2)].                                  (3.2)
```

Equations (2.3)--(3.2) show that their complete supported third-order
Newton signatures differ by at most

```text
O(H/p^2).                                            (3.3)
```

Taking `H=D^(17/16)` and `eta=D^(-7/48)`, the right side is `O(eta)` for

```text
p>=D^((17/16+7/48)/2)=D^(29/48).                   (3.4)
```

This is a noise-stable alias, modulo the actual integer Newton lattice.
The canonical curvature frequency of size `p^2` would amplify (3.2) back
to constant scale; precisely that frequency is missing.

## 4. What the phase-jet correlation test can see

The coefficient noise `eta` in Section 3 should not be confused with an
off-diagonal correlation threshold on a block.  For the geometric
first-difference bound to prove correlation at most `eta`, one needs

```text
lambda >=1/(N*eta)=D^(-13/24).                      (4.1)
```

For Farey neighbors, `lambda<<H/p^2`.  Thus the supported first-, second-,
and third-difference certificates all become too weak once

```text
p>>D^((17/16+13/24)/2)=D^(77/96).                  (4.2)
```

The second and third differences in (2.3) are smaller by `Q^(-1)` and
`Q^(-2)` and cannot repair this.  Statement (4.2) means the pair must remain
in the phase-jet major-arc graph; it does not yet assert that its actual
correlation is large.

For that stronger conclusion, align the irrelevant constant phases.  The
mean-value theorem gives on `0<=s<N`

```text
|(phi_t(s)-phi_t(0))-(phi_t'(s)-phi_t'(0))|
 <<H*N*|t-t'|.                                      (4.3)
```

If the right side is `epsilon<1/4`, the normalized packet correlation is at
least

```text
1-2*pi^2*epsilon^2.                                 (4.4)
```

Consequently Farey-neighbor packets have correlation tending to one for
`p>>D^(7/8)`, and their aligned phases are themselves `O(eta)`-close for
`p>>D^(91/96)`.  These are rigorous packet statements for the local
reciprocal phase (2.1), not merely derivative heuristics.

## 5. A genuine residual alias sequence

The previously proved non-square residual family makes the obstruction
physical at the integer cusp level.  Fix `M>=2` and for `d>2` put

```text
p=M*d+1,              ell=p^2-d^2,
g=2d,                 Q=(p*ell-1)/d,
y=ell,                n=1.                          (5.1)
```

It has

```text
e=-(p-d),       f=-(p+d),       v=0,       z=2d,
(z+dv)(z-dv)=4d^2!=0,           d^2 does not divide g. (5.2)
```

Thus it survives the balanced, one-band, and square-content peels.  The
members with parameters `d` and `d+1` satisfy

```text
|t_d-t_(d+1)|=1/[2*p_d*p_(d+1)].                   (5.3)
```

Here `Q asymp d^2`.  If `D=Q^(16/33)`, then

```text
p asymp D^(33/32),          H/p^2 asymp D^(-1),
N*H/p^2 asymp D^(-5/16).                            (5.4)
```

Both are smaller than `eta=D^(-7/48)`.  Moreover the errors have size
`asymp d`.  Taking a balanced mask factor

```text
m_mask=M_mask asymp D^(1/32)                        (5.5)
```

puts `A=B=D*m_mask asymp d`` and

```text
m_mask^2*M_mask^3=D^(5/32)<sqrt(D).                 (5.6)
```

So this is genuinely inside the unresolved energy ledger.  It proves that
the bad conditioning is attained on non-square transverse integer residual
points, rather than only on abstract rational directions.

The two sampling scales are not identical, but this does not change the
estimate.  The exact polynomial in this family has

```text
Q_d=M*(M^2-1)*d^2+(3M^2-1)*d+3M,                  (5.7)
```

so `Q_(d+1)-Q_d=O(d)` and

```text
N*|Q_d^(-1)-Q_(d+1)^(-1)|=O(d^(-7/3))=o(|t_d-t_(d+1)|).
```

Indeed, after constant alignment,

```text
phi_(Q,t)(s)-phi_(Q,t)(0)
 =integral_0^s Phi'(t+u/(2Q)) du.
```

Comparing the two integrals adds only
`O(H*N^2*|Q_d^(-1)-Q_(d+1)^(-1)|)`, smaller than the
`O(H*N*|t_d-t_(d+1)|)` term in (5.4).

The consecutive members have different centres `Q_d`.  They do **not**
form a large coherent cluster at one fixed centre, and the construction does
not impose the actual prime-power node support.  Those two facts prevent
this example from being a counterexample to the desired fixed-`Q` Bessel
theorem.

## 6. A full vector signature has affordable fixed-centre fibers

The stable pair alias does not imply a large fixed-`Q` cluster.  The full
supported interval contains the harmonics

```text
(h,k,m)=(j,0,0), (0,j,0),          1<=j<=cH,        (6.1)
```

with a fixed `c>0` if one stays away from the vanishing edge of the Fejer
triangle.  The following elementary torus lemma captures their joint
information:

> If `||j*theta||_T<=eta<1/4` for every `1<=j<=L`, then
> `||theta||_T<=eta/L`.

Indeed, if `L*||theta||_T<=1/2`, the last harmonic proves the claim.  If
not, the first multiple crossing `1/2` has torus distance greater than
`eta`, a contradiction.  Applying the lemma to both reciprocal coordinates
and splitting their bounded real ranges at the finitely many integer wraps
shows that a full supported-signature neighborhood of one tangent is a
union of `O(1)` intervals of length

```text
O(eta/H).                                            (6.2)
```

Now restore physical points at one fixed centre.  Their exact tangent error
is

```text
|t-t_0|=|n|/(2Qp)<=B/(Q*g*p).                       (6.3)
```

In the residual chart `g*p>=p>=P_0=D^(77/160)`.  Hence every interval in
(6.2) contains shifts `y` in an interval of length at most

```text
Q*eta/H+B/P_0
 <<D^(41/48)+D^(329/480).                           (6.4)
```

For fixed `y`, each product band of width `o(Q)` permits only `O(1)` integer
values of `r,s`.  Therefore a fixed-`Q` full-signature fiber has cardinality

```text
O(D^(41/48+o(1))).                                  (6.5)
```

This is below the full anisotropic cluster allowance `D^(1+o(1))`, and
well below the weaker `D^(49/48+o(1))` allowance needed to close the current
gap.

The qualification **full vector signature** is decisive.  A single packet
jet does not automatically reveal all harmonics in (6.1).  Thus (6.5) is
not yet the physical Bessel theorem; it proves that a vector-valued theorem
which retains the supported harmonic family would have enough information
even though unique direction recovery is false.

## 7. Consequence for the proposed transference theorem

A theorem saying that one supported sampled jet uniquely and stably
reconstructs the virtual fingerprint `(chi,K_2,J_2,J_3)` throughout the
high tail is false.  Past (3.4), its direction component alone is below the
stated noise.  Past (4.3)--(4.4), even the full local packet rays coalesce.

On the other hand, (6.5) shows that the **full vector of supported
harmonics** has small fixed-centre fibers.  This is the precise positive
route left by the no-go: prove a vector-valued Bessel/intertwining theorem
which preserves those joint responses rather than selecting one virtual
normal per direction.

A viable high-tail theorem must instead use at least one of:

1. fixed-centre arithmetic spacing of actually occupied residual points;
2. content and product-error labels not contained in the direction jet;
3. a cluster theorem allowing all directions in one `eta/H` Farey cell;
4. averaging across centres or masks before taking absolute values.

The result is therefore a **no-go for unique direction-only transference**,
not a no-go for the mask-sensitive Bessel programme.

## 8. Status

```text
stationary lattice covolume ~p^4:                   PROVED;
every stationary mode has p^2|m:                   PROVED;
no supported exact stationary mode for p^2>4H:     PROVED;
actual affine m-mode vanishes in Newton quotient:   PROVED;
supported Newton metric locally ~H*|t-t'|:          PROVED;
eta-alias threshold p=D^(29/48):                    PROVED;
phase-jet certificate barrier p=D^(77/96):          PROVED;
sampled packet coherence threshold p=D^(7/8):       PROVED;
sampled eta-phase alias threshold p=D^(91/96):      PROVED;
non-square residual energy-core alias sequence:      PROVED;
full harmonic torus resolution eta/H:                PROVED;
fixed-Q full-signature cluster D^(41/48+o(1)):       PROVED;
fixed-Q residual alias cluster above allowance:      NOT PROVED;
actual prime-power alias family:                     NOT PROVED;
sharp four-cycle bound:                              NOT PROVED.
```

Exact arithmetic and finite packet checks are in
`src/qp_high_p_newton_information.py` and
`src/test_qp_high_p_newton_information.py`.
