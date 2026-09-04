# QP carrier: exact mod-`q^2` coarse lift and the hybrid Mellin gate

**Date:** 2026-08-24  
**Verdict:** inserting a coarse Archimedean cutoff repairs the lost-lift
defect of reduction modulo `q^2`, and it gives an exact conductor
decomposition.  It does **not** prove the selected-shell BDH estimate, the
centered carrier bound, or the sharp four-cycle theorem.

The apparent conductor saving is a time--frequency repackaging.  The coarse
cutoff by itself has Mellin bandwidth `q`, but the primitive residual
projection has `asymp q/D` coherent additive packets.  Packet `h` is
centered at Mellin frequency `t asy hq`, so the union reaches

```text
q*(q/D)=q^2/D,
```

exactly the native bandwidth of the original fine product window.  The
scalar Plancherel ledger is tantalizingly sharp, but converting it to a
physical operator estimate is precisely a mask-sensitive vector-valued
two-inverse large-sieve theorem.  Its off-diagonal Gram terms are the open
centered common-neighbor covariance.

There is a second issue: the principal character produces a smoothed
**coarse carrier operator**, not the physical scalar constant mode.  Current
geometry bounds this term only at the `D` operator scale before a new polar
or local-chart subtraction.  Pólya--Vinogradov is better here than the
`r=2` Burgess bound, but it is worse than residual Parseval and does not
control either operator obstruction.

No unconditional four-cycle exponent improvement follows.  In particular,
the proved global `D^(9/8+o(1))` fourth-trace exponent is unchanged.

---

## 1. An exact lift selector modulo `q^2`

Let `q` be an odd prime and let

```text
D=q^(16/33+o(1)),             H=qD<q^2/4,
X(a,b,c)=8abc-q^3.                                      (1.1)
```

All shell nodes are units modulo `q`.  Put

```text
R={r mod q^2:0<|r|<=qD and q does not divide r}.         (1.2)
```

Choose a fixed smooth function `W` which is one on `[-1/4,1/4]` and
supported in `(-1/2,1/2)`.  Then the following identity is exact:

```text
1_(|X(a,b,c)|<=qD)
 =W(X(a,b,c)/q^2) 1_R(8abc mod q^2).                    (1.3)
```

Indeed, the forward implication uses `H<q^2/4`.  Conversely, write

```text
X=r+kq^2,                    |r|<=qD.                   (1.4)
```

The support of `W` gives `|X|<q^2/2`.  If `k` were nonzero, then
`|X|>=q^2-|r|>3q^2/4`, a contradiction.  Hence `k=0`, and the residue
condition is the desired fine inequality.

Thus the proposed hard coarse cutoff really does repair the quotient-lift
problem.  The smooth plateau in (1.3) is preferable: it retains exactness
and gives rapid Mellin decay.  This part of the idea succeeds completely.

## 2. Exact conductor filtration and the principal coarse operator

Let

```text
Phi=phi(q^2)=q(q-1),
Rhat(chi)=sum_(r in R) conjugate(chi(r)).                 (2.1)
```

Multiplicative character inversion on the units gives

```text
1_(|X|<=qD)
 =W(X/q^2)/Phi sum_(chi mod q^2)
      Rhat(chi) chi(8abc).                              (2.2)
```

The exact conductor counts are

```text
conductor 1:       1,
conductor q:       q-2,
conductor q^2:     (q-1)^2.                              (2.3)
```

The positive residual interval is the disjoint union

```text
r=qv+u,       0<=v<D,       1<=u<q,                     (2.4)
```

and the negative half is its reflection.  Every nonprincipal character
induced modulo `q` therefore cancels on every complete `q`-block:

```text
Rhat(chi)=0,              cond(chi)=q, chi nonprincipal. (2.5)
```

Also

```text
|R|=2D(q-1),              |R|/Phi=2D/q.                 (2.6)
```

For the physical carrier matrix

```text
T(b,c)=sum_(a in S)1_(|8abc-q^3|<=qD),                  (2.7)
```

the principal term in (2.2) is exactly

```text
T_0(b,c)=(2D/q) sum_(a in S)W((8abc-q^3)/q^2).          (2.8)
```

This is not generally `kappa J`.  It is a smoothed coarse product-incidence
operator.  Subtracting the physical constant vector deletes at most one of
its Mellin modes; it does not delete (2.8).

For the project shell, a fixed `(a,b)` admits only `O(1)` integers `c` in
the support of `W`.  If `N=|S|=q^(1+o(1))`, Schur therefore gives only

```text
||T_0|| <=(D/q) O(N)=D q^o(1).                          (2.9)
```

Double centering is contractive but does not improve (2.9).  The desired
centered scale is `sqrt(D)q^o(1)`.  Hence the principal block is harmless
only after one proves that its nonconstant part is an already controlled
polar/tangent/chart operator.  No such global norm-controlled pullback
follows from character orthogonality.

## 3. The coarse cutoff has Mellin width `q`

Put

```text
s=8abc/q^3,             w_q(s)=W(q(s-1)).                (3.1)
```

Then `W(X/q^2)=w_q(s)`.  With the Mellin convention

```text
what_q(t)=integral_0^infinity w_q(s)s^(-it) ds/s,        (3.2)
```

fixed smoothness of `W` and the change of variables `u=log s` give, for
every `A>0`,

```text
|what_q(t)| <<_A q^(-1)(1+|t|/q)^(-A),
integral |what_q(t)| dt <<1,
integral |what_q(t)|^2 dt asymp q^(-1).                 (3.3)
```

Thus the coarse Archimedean gate alone really has bandwidth `q`.  If it
were the only oscillatory input, it would lie at the shell Nyquist scale.
The error is to infer from (3.3) that the complete decomposition has the
same bandwidth.

## 4. Primitive `q^2` projection is an additive fibre difference

Extend `1_R` by zero to all residues modulo `q^2`.  The kernel of

```text
(Z/q^2 Z)^* -> (Z/q Z)^*                                  (4.1)
```

is `{1+qt:t mod q}`.  For a unit `x`, its orbit is

```text
x(1+qt)=x+q(xt),                                         (4.2)
```

which is the complete additive fibre above `x mod q`.  Therefore the
conditional expectation onto characters induced modulo `q` is

```text
E_1F(x)=q^(-1) sum_(t mod q)F(x+tq).                    (4.3)
```

Every nonzero fibre contains exactly `2D` elements of `R`, so

```text
E_1 1_R=(2D/q)1_((x,q)=1).                              (4.4)
```

This recovers (2.5)--(2.6) directly.  The primitive conductor-`q^2`
projection is

```text
P_2 1_R=(I-E_1)1_R.                                     (4.5)
```

Additive Fourier transform modulo `q^2` diagonalizes (4.3): `E_1` retains
the frequencies divisible by `q`.  Hence, on all residues,

```text
P_2 1_R(x)
 =q^(-2) sum_(h mod q^2, q does not divide h)
       Rtilde(h)e_(q^2)(hx),                            (4.6)

Rtilde(h)=sum_(r in R)e_(q^2)(-hr).                    (4.7)
```

Equation (4.6) is the exact additive recombination of the primitive
multiplicative characters; it makes the hidden frequency scale visible.

## 5. A flat primitive band of `q/D` packets

For

```text
1<=h<=q/(100D),                                         (5.1)
```

all phases on the positive interval satisfy

```text
|2*pi*h*r/q^2|<=2*pi/100.                              (5.2)
```

The negative interval is its conjugate.  Consequently

```text
|Rtilde(h)| >=2 cos(2*pi/100)D(q-1) asymp qD.           (5.3)
```

Every frequency in (5.1) is primitive because it is positive and smaller
than `q`.  There are `asymp q/D` such frequencies.  They alone contribute

```text
(q/D)(qD)^2 asymp q^3D                                  (5.4)
```

to additive Fourier energy, while full Parseval is

```text
sum_(h mod q^2)|Rtilde(h)|^2
 =q^2|R| asymp q^3D.                                    (5.5)
```

Thus the low primitive band carries a fixed proportion of all residual
energy.  Its normalized coefficients in (4.6) have

```text
alpha_h=q^(-2)Rtilde(h) asymp D/q,
sum_(h in flat band)|alpha_h|^2 asymp D/q.              (5.6)
```

It cannot be discarded as an exceptional tail.

## 6. The lost factor `q` returns as packet modulation

For one additive mode define the coarse packet matrix

```text
C_h(b,c)=sum_(a in S)w_q(8abc/q^3)e_(q^2)(8habc).       (6.1)
```

Since `8abc=q^3s`, its scalar kernel in logarithmic coordinates is

```text
g_(h,q)(u)=W(q(e^u-1)) e(hq e^u),       u=log s.        (6.2)
```

On its support `u=O(1/q)`.  The phase derivative is

```text
d/du [2*pi*hq e^u]=2*pi*hq+O(h),                       (6.3)
```

and the support uncertainty is `q`.  Equivalently, after writing `v=qu`,

```text
g_(h,q)(u)
 =e(hq)W(v+O(v^2/q))e(hv+O(hv^2/q)).                  (6.4)
```

For `h<=q/D`, the final error is `O(1/D)`.  The Mellin transform of
`g_(h,q)` is therefore concentrated in a packet of width `asymp q`
centered at

```text
t=2*pi*hq.                                             (6.5)
```

The energetic range `1<=h<<q/D` from Section 5 consequently occupies

```text
q <= |t| <= q^2/D.                                    (6.6)
```

This is exactly the fine-window Mellin bandwidth.  Numerically at the
project scale,

```text
D=q^(16/33),
number of flat packets q/D=q^(17/33),
largest packet centre q^2/D=q^(50/33)=D^(25/8).        (6.7)
```

Thus conductor lowering creates `q/D` Nyquist-sized packets; it does not
create one Nyquist-sized problem.  Multiplication by the residue selector
restores the factor lost from the modulus.

## 7. The exact square-function budget and the missing theorem

Combining (2.2) and (4.6), the primitive carrier is

```text
T_* =sum_(q does not divide h) alpha_h C_h,
alpha_h=q^(-2)Rtilde(h).                              (7.1)
```

The flat band has the exact favorable scalar ledger

```text
q * sum_h|alpha_h|^2
  asymp q*(q/D)*(D/q)^2
  =D.                                                  (7.2)
```

Accordingly, a mask-sensitive vector-valued theorem of the schematic form

```text
||P sum_h alpha_h C_h P||_(2->2)^2
 <<q^(1+o(1)) sum_h|alpha_h|^2                         (7.3)
```

with the appropriate coefficient-valued version and compatible treatment
of the nonflat tail would prove the desired `D` squared norm for the
primitive part.

But (7.3) is not a consequence of scalar character estimates.  Expanding
its left side produces all cross terms

```text
C_h^* C_k,                  h!=k,                      (7.4)
```

on the same physical carrier--colour mask.  On a fine edge
`|8abc-q^3|<=qD`, the phases of every `h<=cq/D` vary by only `O(c)`;
the low packets are deliberately coherent there.  Their sum reconstructs
the hard fine selector.  Orthogonality can arise only after proving
cancellation among different common carriers, which is exactly the
selected-degree/common-neighbor covariance problem.

In other words, (7.3) is a clean formulation of the requested
mask-sensitive vector-valued two-inverse large sieve.  Proving it would be
a breakthrough; writing (7.1) does not prove it.

There is an equivalent scalar Plancherel coincidence.  Character Parseval
and (3.3) give

```text
[Phi^(-1)sum_chi|Rhat(chi)|^2]
       *integral|what_q(t)|^2dt
  asymp(qD)*(1/q)=D.                                  (7.5)
```

The multiplier has exactly the desired norm.  The missing assertion is
that its character--Mellin synthesis into the restricted physical matrix
is contractive after the allowed polar channels are removed.  Restrictions
of the rank-one character tensors span the whole symmetric physical matrix
space, so this contractivity is not formal Plancherel.

## 8. The `t-s` hybrid Gram is where scalar Burgess stops

After Mellin separation, the physical shell vectors are

```text
v_(chi,t)(n)=chi(n)n^(it),             n in S.          (8.1)
```

Their cross-Gram kernel is

```text
<v_(chi,t),v_(psi,s)>
 =K_(conjugate(chi)psi)(s-t),
K_eta(u)=sum_(n in S)eta(n)n^(iu).                    (8.2)
```

Thus fourth moments and operator squares retain both character difference
and Mellin difference.  Even inside one coarse packet, `|t-s|` ranges up
to `q`; between additive packets it ranges through the full scale in
(6.6).

There is already a barrier in the optimistic full-integer-shell model.
For an interval of length `q` and a primitive character modulo `q^2`, the
`r=2` Burgess estimate is

```text
|K_eta(0)| <<q^(7/8+o(1)),                            (8.3)
```

a saving of only `q^(1/8)` from the trivial interval bound.  Partial
summation with `n^(iu)` gives only

```text
|K_eta(u)| <<(1+|u|)q^(7/8+o(1)).                     (8.4)
```

It is nontrivial by this route only in a narrow neighborhood
`|u|<=q^(1/8-o(1))` of `t=s`, while the native coarse Gram has
`|u|<=q`.  The actual prime-power mask is no easier.  This is the precise
`K_(t-s)` obstruction: a scalar near-diagonal Burgess saving does not give
the full hybrid frame bound (7.3).

## 9. Pólya--Vinogradov and Burgess do not improve the ledger

For primitive characters modulo `q^2`, Pólya--Vinogradov gives

```text
|Rhat(chi)| <<q log q.                                (9.1)
```

The `r=2` Burgess estimate gives

```text
|Rhat(chi)|
 <<(qD)^(1/2)(q^2)^(3/16+o(1))
 =q^(7/8)D^(1/2)q^o(1).                              (9.2)
```

At `D=q^(16/33)`, the two exponents in `q` are

```text
Pólya--Vinogradov:              1,
Burgess r=2:                    295/264=1.1174... .   (9.3)
```

So Pólya--Vinogradov is stronger.  But residual Parseval already has RMS

```text
sqrt(qD)=q^(49/66),                                  (9.4)
```

which is smaller than (9.1) by `q^(17/66)`.  Replacing an average by the
pointwise Pólya--Vinogradov bound goes in the wrong direction.  Neither
(9.1) nor (9.2) controls the cross-Gram (8.2), and neither shows that the
principal coarse operator (2.8) is an allowed polar term.

## 10. Comparison with the primitive `q^3`/second-Fermat route

The two formulations have the same total Archimedean resolution.

For modulus `q^3`, the residual interval of length `qD` has a flat additive
band

```text
h<=q^3/(qD)=q^2/D.                                    (10.1)
```

Since `8abc=q^3s`, mode `h` has Mellin center `t asy h`.  The final
bandwidth is `q^2/D`.

For modulus `q^2`, the flat band is shorter,

```text
h<=q^2/(qD)=q/D,                                      (10.2)
```

but `8abc/q^2=qs`, so mode `h` has center `t asy hq`.  The final bandwidth
is again `q^2/D`.

Wild conductor-`q^3` characters sample the second Fermat quotient of shell
nodes.  Wild conductor-`q^2` characters sample the first Fermat quotient,
but the coarse Archimedean lift selector supplies the missing factor `q` in
frequency.  Thus the `q^2` route is p-adically simpler but not a smaller
joint restriction problem.  It also replaces the simple `q^3` principal
mode by the richer coarse operator (2.8).

## 11. Binary conclusion

```text
coarse cutoff repairs the mod-q^2 lift:                 PROVED, EXACT;
smooth plateau can retain exactness:                    PROVED;
conductor-q nonprincipal residual block:                ZERO;
principal coefficient:                                 2D/q, EXACT;
principal physical block = scalar J:                    FALSE IN GENERAL;
coarse Mellin bandwidth:                                q;
primitive flat additive packet count:                   q/D;
packet h Mellin centre:                                 hq;
combined energetic Mellin bandwidth:                    q^2/D;
scalar multiplier L2 budget:                            D, EXACT;
PV/Burgess proves the vector-valued synthesis:           NO;
principal coarse block below sqrt(D):                   NOT PROVED;
mask-sensitive packet square function (7.3):            OPEN;
selected-shell BDH / centered covariance:               OPEN;
new unconditional four-cycle exponent:                  NONE;
sharp four-cycle bound:                                 NOT PROVED.
```

The exact conductor counts and exponent arithmetic are replayed by

```text
src/qp_q2_coarse_lift_gate.py
src/test_qp_q2_coarse_lift_gate.py
```

with

```bash
PYTHONPATH=src pytest -q src/test_qp_q2_coarse_lift_gate.py
```
