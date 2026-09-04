# QP dyadic reciprocal moment and hostile cubic gate

> **Correction (2026-08-27).**  Section 4 conflates the primitive
> rational-point count with an unreduced raw count.  The critical top slice
> actually has `gcd(A,B)=1`; without that condition there is a nontrivial
> content sum.  Also, the accessible Huxley-IV corollary used for the
> `P^(5/8)` exponent excludes integral powers, so that exponent is provisional
> until the original determinant-form theorem is checked.  The corrected
> quantifiers and fully licensed bounds are in
> `ZETA23-SHIFTED-CUBE-GCD-QUANTIFIER-AND-HUXLEY-AUDIT-2026-08-27.md`.
> This report does not prove the shifted-cube target or the sharp four-cycle
> theorem.

**Date:** 2026-08-22
**Verdict:** deleting the coherent modes only up to `q/D^2` does **not**
make the remaining unweighted second moment diagonal-sized.  The correct
candidate is the scale-by-scale estimate

```text
sum_(K<ell<=2K) |S_ell(A,C)|^2
  << (q^2/K) q^o(1),             q/D^2<=K<=q/D.     (0.1)
```

One contiguous tangent fan satisfies (0.1), and the first dyadic interval
saturates it.  For a whole completed scattered modular strip, however,
(0.1) is the diagonal-strength smooth HSM estimate in primal coordinates.
The fact that the completed coefficients are all-one interval transforms
does not remove the positive diagonal difficulty.  In the audited
Farey/Huxley implementation, the balanced top scale is reduced to the
sufficient primitive rational-cubic transition estimate

```text
#{A*u^3-B*P^3=Delta:
  gcd(A,B)=1, A,B~P^(9/16), u~P,
  0<|Delta|<=P^(7/16)}
  <<P^(9/16+o(1)).                                  (0.2)
```

No proof or counterexample to (0.1) is obtained.  The existing
`N(delta)<<delta*P^4+P^3` spacing fallback is not an estimate for the full
primal dyadic moment, so its `P` loss cannot be square-rooted and promoted
to a new four-cycle theorem without an additional bridge.

There is nevertheless a useful exact payoff ledger.  If the **primal**
version of (0.1) were proved with a loss `D^beta`, it would give

```text
Q_nd(z)<<D^(1+beta/2+o(1))*||z||_2^4.              (0.3)
```

Thus every `beta<5/8` improves the current `D^(21/16)` theorem.  In
particular, a genuine primal `sqrt(D)` moment loss would already give
`D^(5/4)`, an improvement by `D^(1/16)`.

---

## 1. Why a single global high-frequency second moment is false

Put

```text
q=2m+1,                 T=q^3/8,
L0=q/D^2,               H=q/D.
```

Let `eta>0` be a sufficiently small fixed constant, `M=floor(eta*D)`, and
take the two disjoint intervals

```text
A={m+x:0<=x<M},
C={m+y:3M<=y<4M}.                                (1.1)
```

These are not arbitrary sets.  They are first-coordinate projections of
one exact primitive determinant-lift strip.  Relative to `(m,m+1)`,

```text
det((m,m+1),(m+t,m+t+1))=-t.                       (1.2)
```

All the offsets in (1.1) are `O(D)`, all vectors are primitive, and their
ratio span is `O(M/q^2)`, hence they lie in a fixed number of the relevant
`D/q^2` slope blocks.  The construction uses the legal all-integer strip
enlargement; it is not an actual-prime-power strip because many consecutive
prime-power pairs are forbidden by parity.

Write

```text
f(x,y)=T/((m+x)*(m+y)),
g(x,y)=f(x,y)-f(0,0)+x+y.                           (1.3)
```

The common phase `f(0,0)` is harmless and `x+y` is integral.  At the
origin,

```text
partial_x g=partial_y g
 =1-(1+1/(2m))^3=O(1/m),
max_(0<=x,y<=4M) |second partials of g|<<1/m.       (1.4)
```

Taylor's theorem therefore gives

```text
|g(x,y)|<<M/m+M^2/m.                               (1.5)
```

For every integer `L0<ell<=2L0`, choosing `eta` as one sufficiently small
absolute constant makes `|ell*g(x,y)|<1/100` uniformly on (1.1).  Hence all
`M^2` summands lie in one fixed short arc and

```text
|S_ell(A,C)|>>M^2>>D^2.                            (1.6)
```

Since `L0=q^(1/33)` tends to infinity at `D=q^(16/33)`, this proves

```text
sum_(L0<ell<=2L0)|S_ell|^2 >>L0*D^4=q*D^2.        (1.7)
```

Thus the proposed global tail estimate `sum_(L0<ell<=H)|S_ell|^2<<qD`
is false by a factor `D`.  There is no exact modulo-one alias in the
argument: it is a genuine near-tangent packet just beyond the cutoff.

On the other hand, the right side of (0.1) at `K=L0` is

```text
q^2/L0=q*D^2,                                      (1.8)
```

so this same example is exactly target-sized for the dyadic formulation.
Removing a fixed multiple of `L0` merely moves the construction to a
smaller fixed `eta`; tangent energy has to be treated scale by scale, not
discarded once at the bottom.

## 2. One fan proves the dyadic estimate

For one contiguous tangent-band pair, the already proved two-dimensional
`B`-process estimate is

```text
|S_ell(one fan pair)| << (q/ell) q^o(1),
                           ell<=q/D.                (2.1)
```

The trivial estimate covers its degenerate lower transition.  Therefore

```text
sum_(K<ell<=2K)|S_ell|^2
 <<K*(q/K)^2*q^o(1)
 =(q^2/K)q^o(1).                                   (2.2)
```

So (0.1) is proved on every single fan pair.  The issue is entirely the
outer aggregation of the reduced fans.

## 3. Exact whole-strip normalization

Choose a slope-adapted unimodular basis

```text
d=(R,S), e=(U,V),                 R*V-S*U=1,
a=R*m+U*r, c=S*n+V*s.                             (3.1)
```

Complete the quotient variables `r,s` to intervals before Fourier
expansion and use smooth positive shell majorants.  Poisson summation in
the long variables gives the exact formula

```text
S_tilde_ell
 =1/(R*S) sum_(j,k) W_P(j) W_Q(k) I_ell(j,k),      (3.2)

W_P(j)=sum_(r<P)e(-j*U*r/R),
W_Q(k)=sum_(s<Q)e(-k*V*s/S).                       (3.3)
```

This removes fanwise boundary errors.  On the stationary range the smooth
integral has phase

```text
3*(T*ell*j*k/(R*S))^(1/3)                          (3.4)
```

and amplitude `q/(ell*R*S)` after the prefactor in (3.2).  Mellin
separation of the smooth cutoffs reduces the dyadic moment to

```text
sum_(ell~K) |sum_(j,k)u(j)v(k)
 e(3*(T*ell*j*k/(R*S))^(1/3))|^2.                 (3.5)
```

At the balanced top scale, put

```text
P=Q=sqrt(D), R=S=q/sqrt(D), K=L=q/D,
J=K_dual=q^2/D^(3/2), X=J*K_dual.                 (3.6)
```

Then

```text
||u||_2^2*||v||_2^2~D*X,
(q/(L*R*S))^2 * L*D*X=q*D.                        (3.7)
```

Thus (0.1) is exactly the diagonal-strength HSM target in the completed
coordinates.  It is not a generic large-sieve corollary.

The all-one specialization does give real structure: `u` and `v` are the
Dirichlet transforms (3.3), their autocorrelations are triangular, and the
product diagonal is bounded by the divisor function.  But those triangular
autocorrelations are positive near the origin.  They therefore retain,
rather than cancel, the next obstruction.

## 4. Exact hostile positive diagonal forced by (0.1)

On the diagonal stationary fibre, the two translation frequencies have
the form

```text
A_m=q^3/(8*R^2*S*m^3),
B_m=q^3/(8*R*S^2*m^3),              m~P.           (4.1)
```

Whenever

```text
||ell*A_m||, ||ell*B_m|| <<1/P,                    (4.2)
```

both interval transforms in (3.3) have size `>>P`; this is a positive
Fejer peak.  Consequently a diagonal-strength bound for (3.5), and hence
(0.1) for the completed strips, forces

```text
E_diag=sum_(a~L,m~P) 1_(||a*beta_m||<<1/P)
       <<L*q^o(1),                                 (4.3)
```

with `beta_m~m^3/P^3`.  Exact rational cube rays contribute only
`O(Lq^o(1))`, so they are target-sized.

The audited Farey/Huxley upper-bound decomposition of the noncoherent part
contains
the transition

```text
A*u^3-B*P^3=Delta,
A,B~mathcal_T=P^(9/16), u~P,
0<|Delta|<=mathcal_H=P^(7/16).                     (4.4)
```

On the critical top-content slice one has `gcd(A,B)=1`.  Closing this
particular upper-bound argument would follow from the primitive count in
(4.4) at the scale

```text
R_transition <<mathcal_T*P^o(1).                  (4.5)
```

This is a sufficient local gate for this proof route; no reverse reduction
from the transition box to the original moment is proved here.  For the
literal nonprimitive raw count, content multiplicity is not divisor-bounded;
see the correction cited at the start of this report.

The tangent point `u=P,A=B,Delta=0` is not the problem.  The nonzero
transition is a quality-one near-cubic equation.  Even in the audited
conditional-`abc` decomposition, after lower-height ranges are removed,
Huxley's remaining term has the `P^(5/8)` floor, a factor `P^(1/16)` above
(4.5).  An exact abstract occupancy pattern meets all currently proved gap
constraints at that floor.  This is not a counterexample to (4.5); it
identifies the first theorem-sized all-one obstruction.

## 5. Why the proved `P^3` spacing fallback does not bridge (0.1)

The proved local spacing statement is

```text
N(delta)=sum_(m,n~P) #{0<|h|,|k|<=P:
 ||h*A_mn+k*B_mn||<=delta}
 <<(delta*P^4+P^3)q^o(1).                          (5.1)
```

Dyadic integration gives

```text
mathcal_K=sum_(m,n,h,k)
 min(L,||h*A_mn+k*B_mn||^(-1))
 <<P^4*q^o(1)+L*P^3*q^o(1).                       (5.2)
```

After the particular Dirichlet normalization used in that spacing row,
`P^(-2) mathcal_K<<L*P*q^o(1)`.  It is tempting to read this as a primal
second moment with loss `P` and then take a square root.  That inference is
not valid.  Equations (5.1)--(5.2) control a linearized spacing/Schur
subproblem after taking absolute values.  They do not supply an identity or
inequality bounding the full signed cubic-root quadratic form (3.5), with
all cross-base product fibres and stationary pieces, by that normalized
row.  Precisely that missing bridge is the shifted multiplication-table
HSM theorem.

Accordingly the existing ledger's `D*P=D^(3/2)` local fallback is a method
ledger, not the consequence of a proved primal estimate

```text
sum_(ell~K)|S_ell|^2 <<(q^2/K)*P.                  (5.3)
```

If (5.3) itself were proved, the square root in the next section would be
mandatory and would produce a new result.  At present, (5.3) has not been
derived from (5.1).

## 6. Exact payoff of any weaker primal dyadic theorem

Assume uniformly for all relevant completed strip pairs and all dyadic
`L0<=K<=H` that

```text
sum_(ell~K)|S_ell|^2
 <<(q^2/K)*D^beta*q^o(1).                          (6.1)
```

Cauchy--Schwarz on one dyadic block gives

```text
sum_(ell~K)|S_ell|
 <<sqrt(K)*sqrt(q^2*D^beta/K)*q^o(1)
 =q*D^(beta/2)*q^o(1).                             (6.2)
```

There are only `O(log q)=q^o(1)` blocks.  The modes below `L0` cost `q`
trivially, so the Selberg reduction gives

```text
E_ij <<D^3/q+D^(1+beta/2)q^o(1)
      <<D^(1+beta/2)q^o(1).                        (6.3)
```

The slope-block-to-restricted-type proof is homogeneous in this cap:
`min(x_i*y_j,M)<=sqrt(M*x_i*y_j)`.  The subsequent Gram/operator argument
is homogeneous in the same `M`.  Therefore

```text
Q_nd(z)<<D^(1+beta/2+o(1))*||z||_2^4.             (6.4)
```

Comparison with `D^(21/16)` gives the exact threshold

```text
1+beta/2<21/16   iff   beta<5/8.                   (6.5)
```

In particular

```text
beta=0:     D^(1+o(1))       (the four-cycle target),
beta=1/2:   D^(5/4+o(1))     (uniform improvement by D^(1/16)),
beta=5/8:   D^(21/16+o(1))   (ties the current theorem).          (6.6)
```

The exact phase and exponent assertions are regression-tested in
`src/qp_dyadic_reciprocal_moment_gate.py` and
`src/test_qp_dyadic_reciprocal_moment_gate.py`.
