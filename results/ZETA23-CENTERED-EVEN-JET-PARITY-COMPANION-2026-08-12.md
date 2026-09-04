# Centered even-jet parity removes the inherited-anchor carrier loss

Status: exact target-only geometric theorem and exact cosine-only arithmetic
reduction, 2026-08-12.

This result closes the inherited-anchor **geometry** on a candidate-centered
target-only quotient.  It proves no sign for the remaining prime square, no
target-isolation theorem, and no zero-free strip.

## 1. Verdict

The uniform Hahn/Weyl-tail estimate is not needed for the target-only direct
carrier program.  Center the critical grid at the hypothetical target and
round the endpoint-jet order upward to an even integer.  Then parity gives

```text
theta_*=1                                             (1.1)
```

exactly, at every finite dimension where the selected carrier is nonzero.
The cost is at most one additional endpoint moment and one coefficient-space
dimension.

This is a design theorem, not a statement that arbitrary grid phase or
arbitrary additional zero rows preserve the geometry.

## 2. Exact theorem

### Theorem 2.1 (centered even-jet parity companion)

Fix an odd symmetric critical grid

```text
tau_k=gamma+h*k,       -J<=k<=J,       h=2*pi/L,      (2.1)
```

and a hypothetical reflected target of depth `alpha>0` centered at `gamma`.
After the standard sharp-grid sign conjugation, write its evaluation row as

```text
v_k=x_k+i*y_k
   =2*sin(-i*alpha*L/2)/(-h*k-i*alpha).              (2.2)
```

Let

```text
W_m={c: sum_k c_k k^r=0, 0<=r<m},
S_m=W_m intersect ker(x),                            (2.3)
```

where `m` is even.  Let `q_m` be the degree-`m` orthonormal Hahn polynomial,
and put

```text
a=P_(S_m)y/||P_(S_m)y||,
g=P_(S_m)q_m.                                       (2.4)
```

If the carrier is nonzero, then

```text
<a,g>=0.                                            (2.5)
```

Consequently, when `g!=0`, the inherited-anchor threshold is exactly

```text
theta_*=1-|<a,g/||g||>|^2=1.                        (2.6)
```

If `g=0`, the inherited anchor constraint is vacuous and the same full
carrier conclusion holds without invoking the quotient formula (2.6).
Moreover, if the odd part of `S_m` has dimension at least two, choose a unit

```text
w in S_m^odd intersect a^perp.                       (2.7)
```

Then for every `0<theta<=1` and every scalar phase `|omega|=1`,

```text
z_theta=sqrt(theta)*a
        +omega*sqrt(1-theta)*w                       (2.8)
```

is odd and hence lies in `g^perp`.  Thus every carrier fraction is
geometrically admissible.  One geometry-only construction orthogonalizes
`q_(m+1),q_(m+3),...` against `a` and takes the first nonzero result.  The
odd-dimension hypothesis is automatic in the asymptotic endpoint regime but
must be checked in a small finite fixture.

On the `d=2J+1` node grid its exact value is

```text
dim S_m^odd=J-m/2=(d-m-1)/2,                        (2.8a)
```

so the companion condition is equivalent to `d-m>=5`.

### Proof

Put `q=alpha/h`.  Since

```text
2*sin(-i*alpha*L/2)=-2*i*sinh(alpha*L/2),
```

(2.2) is a positive real scalar times

```text
q/(k^2+q^2) + i*k/(k^2+q^2).                       (2.9)
```

Hence `x` is even and `y` is odd in `k`.

Reflection `k -> -k` preserves the polynomial space of degrees below `m`,
so it preserves `W_m`.  Because `x` is even, its kernel also preserves
parity; therefore `S_m` is the orthogonal direct sum of its even and odd
parts.  It follows that `P_(S_m)y` is odd.

On a symmetric uniform grid the Hahn polynomial `q_m` has parity `(-1)^m`.
Since `m` is even, `q_m` is even, and its projection through the
parity-invariant space `S_m` remains even.  Thus `a` is odd, `g` is even, and
(2.5) follows.  Equations (2.6) and the `g=0` alternative are immediate.
The whole odd part of `S_m` is orthogonal to the even vector `g`, so (2.7)
and (2.8) prove the final assertion.
Before imposing the selected row, the odd coordinate space has dimension
`J`; among the polynomial degrees below the even integer `m`, exactly
`m/2` are odd.  The even constraint `x` removes no odd dimension, proving
(2.8a).
QED

## 3. The parity choice costs at most one moment

Given any required endpoint order `m_0`, choose

```text
m=2*ceil(m_0/2).                                    (3.1)
```

Then `m_0<=m<=m_0+1`.  Imposing the extra moment only strengthens endpoint
flatness and any tail estimate monotone under passage from `W_(m_0)` to
`W_m`; it removes at most one coefficient-space dimension.  In the
mesoscopic construction the available dimension surplus is of order
`eta*T`, so this `O(1)` cost is asymptotically negligible.  At a small finite
fixture one must still check that `dim S_m` is large enough for the desired
companion.

Dimension cost is not the same as carrier-amplitude cost.  Projection onto
`W_m` can reduce `||P_(S_m)y||`, and parity alone does not prove

```text
kappa_m/kappa_(m_0)=1-o(1)                          (3.2)
```

when one extra odd Hahn component is removed.  The direct program must choose
an even order inside a separately justified retained-carrier regime (or prove
(3.2)).  The theorem gives the full **fraction of the retained carrier**, not
a new lower bound for its absolute size.

That separate retained-carrier input is available in the intended packet
regime.  The symmetric fixed-width construction in
`ZETA23-TARGET-ONLY-PHASE-FLIP-GATE-2026-08-12.md`, Sections 2 and 5, can be
formed as an odd packet difference with a common endpoint-flat cutoff of any
prescribed even order `m=O(eta*T)`, `eta=o(L)`.  It lies in `S_m^odd`, and
after coefficient normalization its selected-pair edge satisfies

```text
kappa_m >=(c_(alpha,w)+o(1))*exp(alpha*D)/L.         (3.3)
```

The binomial-band construction in
`ZETA23-ENDPOINT-PACKET-PRIME-FORM-THEOREM-CARD-2026-08-11.md`, Section 5,
has `D=L-o(L)` and gives `kappa_m=X^(alpha-o(1))/L`.  Hence one may choose
an even order from the outset and retain the required carrier exponent; no
comparison (3.2) with a preselected odd order is needed.  This is a separate
packet-retention theorem, not a consequence of parity.

The centered grid is likewise candidate-adapted, not zero-table-adapted.
In a contradiction argument `gamma` is already the hypothesized target
parameter, so choosing (2.1) uses no collateral-zero data.  The symmetric
aperture must fit inside the admissible modulation band.  One may choose the
dyadic scale so the candidate lies in the interior, or reduce the symmetric
aperture while retaining the required dimension.  The theorem does not
apply to a forced one-sided aperture.

## 4. Relation to the inherited boundary identity

Independently of parity, the inherited Jacobi anchor satisfies

```text
S_m intersect g^perp=W_(m+1) intersect ker(x).      (4.1)
```

For even `m`, Theorem 2.1 says the carrier is already in this one-more-moment
space after the selected-row projection.  Equivalently,

```text
||P_(W_(m+1) intersect ker(x))a||^2=1.              (4.2)
```

Thus no asymptotic Christoffel estimate is needed.  The open Hahn/Weyl-tail
lemma remains relevant only for robustness under a forced noncentered phase,
odd jet order, or other perturbation breaking exact parity.

## 5. Exact cosine-only prime reduction

Parity also simplifies, but does not sign, the remaining arithmetic square.
Let `z` be any odd coefficient vector on (2.1).  In centered frequency
coordinates `t=gamma+s`, its sharp synthesis has the form

```text
Phi_z(gamma+s)=2*S(s)*sum_k z_k/(s-h*k),             (5.1)
```

where `S(s)` is the real odd sharp sine factor.  Pairing `k` with `-k`
gives

```text
z_k/(s-h*k)+z_(-k)/(s+h*k)
 =2*h*k*z_k/(s^2-h^2*k^2),                          (5.2)
```

which is even in `s`.  Therefore `Phi_z(gamma+s)` is odd (real odd when `z`
is real) and

```text
W_z(s)=|Phi_z(gamma+s)|^2                           (5.3)
```

is real even.

Use the cosine-transform convention

```text
W_hat_z(u)=integral_R W_z(s)*cos(u*s) ds.            (5.4)
```

For the exact centered von Mangoldt fluctuation

```text
E_X(t)=sum_(n<=X) Lambda(n)n^(-1/2+i*t)
       -integral_1^X v^(-1/2+i*t)dv,                (5.5)
```

evenness cancels every sine phase and gives

```text
integral_R W_z(s)*Re E_X(gamma+s) ds
 =sum_(n<=X) Lambda(n)/sqrt(n)
      *cos(gamma*log n)*W_hat_z(log n)
  -integral_1^X v^(-1/2)
      *cos(gamma*log v)*W_hat_z(log v)dv.            (5.6)
```

Thus the prime-independent parity companion reduces the arithmetic target
to one cosine-only completed correlation.

There is no hidden positivity in (5.6):

* `cos(gamma*log n)` changes sign;
* `W_hat_z` is an autocorrelation transform and need not be nonnegative; and
* Hahn orthogonality imposes endpoint moments, not
  `W_hat_z(log p)=0` at prime logarithms.

The exact `+1` Herglotz completion still contributes only `2*pi/L` after
normalization.  Proving the required one-square sign in (5.6), with the
gamma and rational-pole completion included, remains the arithmetic gate.

## 6. Scope and non-transfer

The theorem has four essential scope clauses.

1. **Target-only quotient.**  Additional collateral positive rows generally
   mix parity.  Their common kernel need not preserve the odd carrier/even
   anchor splitting, so (2.6) does not transfer to the all-zero quotient.
2. **Candidate-centered symmetric grid.**  A forced phase `phi!=0` or
   asymmetric aperture breaks the exact parity proof.
3. **Even endpoint order.**  For odd `m`, `q_m` is odd and a nontrivial Hahn
   leverage remains.
4. **Geometry versus arithmetic.**  `theta_*=1` constructs an anchor-null
   carrier-rich state.  It neither proves the completed prime square is
   nonnegative, lower-bounds the absolute retained carrier after rounding,
   nor controls divisor-side collateral screening.

Accordingly, the exact next gate is now purely the paired arithmetic/divisor
gate already isolated by the direct carrier program:

```text
arithmetic:  <z_theta,(K_ar+2*pi/L)z_theta> >=0;
divisor:     h_(theta*kappa)(R_other)<theta*kappa.  (6.1)
```

Both estimates must hold on the same target-only feasible set before a zero
can be excluded.

## 7. Verification

The parity identities are exercised in
[`test_conditional_pick_actual_scan.py`](../src/test_conditional_pick_actual_scan.py):
the physical carrier is checked odd, the inherited anchor even, and
`theta_*=1` to twelve decimal places on a centered even-jet fixture.

```text
PYTHONPATH=src python3 -m pytest -q \
  src/test_conditional_pick_actual_scan.py \
  src/test_conditional_pick_companion.py \
  src/test_subfull_direct_q_failfast.py
```
