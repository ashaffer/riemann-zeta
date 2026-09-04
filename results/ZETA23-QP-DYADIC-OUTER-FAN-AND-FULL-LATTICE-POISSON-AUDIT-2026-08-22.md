# QP four-cycle: dyadic outer-fan and full-lattice Poisson audit

**Date:** 2026-08-22  
**Verdict:** a dyadic second moment avoids the known low-mode obstruction,
but the completed high-frequency fan problem remains.  Whole-lattice Poisson
summation does not reduce the outer fan to logarithmically many branches: it
has `q/D` active dual residues in every basis.  Quotient-translation Parseval
also gives no minor-residue saving.  An exact nonprincipal alias occurs in a
scale-legal chart whose modulus and reference nodes are all prime.  This is a
counterexample to coefficient-blind Cotlar decay, not to the desired
reciprocal `L^1` estimate.

## 1. The correct dyadic square-function target

For a dyadic interval `ell asymp K`, put

```text
M(K)=sum_(ell asymp K)|S_ell(A,C)|^2.
```

Cauchy--Schwarz proves the desired `L^1` bound on that interval from

```text
M(K) <<q^(2+o(1))/K.                              (1.1)
```

The product diagonal is `K*|A|*|C|<=K*D^2`.  It is admissible throughout
the full Selberg range because

```text
K*D^2<=q^2/K  iff  K<=q/D.                        (1.2)
```

At the lower endpoint `K=q/D^2`, the consecutive tangent strip has
`|S_ell| asymp D^2` on a fixed subinterval, and its moment has order
`K*D^4=q^2/K`.  Thus the old full-moment objection is not an objection to
(1.1): dyadic normalization gives exactly the extra factor `D` needed at
the coherent endpoint.

This does not prove (1.1).  Expanding its band-pass kernel and replacing it
by a positive spacing majorant loses the generic off-diagonal volume.  The
sign of the dyadic kernel, or equivalent arithmetic cancellation, has to be
retained.

## 2. General balanced-frequency ledger

In the balanced completed fan class write

```text
P=Q=sqrt(D),             R,S asymp q/P,
J_K asymp K*R,           X_K asymp K^2*R*S.
```

The stationary amplitude and the pair-coefficient square mass have the
scales

```text
A_K asymp q/(K*R*S)=D/(K*q),
||u||_2^2*||v||_2^2 asymp K^2*q^2.                (2.1)
```

Consequently the product diagonal after restoring the amplitude is exactly

```text
A_K^2*K*||u||_2^2*||v||_2^2 asymp K*D^2,         (2.2)
```

as required by (1.2).

The stationary short-product width and the spacing of aligned quotient
aliases are

```text
B_K=K*R*S/q asymp K*q/D,
alias spacing asymp S=q/P.                        (2.3)
```

Thus separate absolute treatment of the aligned packets costs

```text
M_alias(K) <<1+B_K/S asymp 1+K/P.                 (2.4)
```

It first becomes polynomial for `K>sqrt(D)` and at the top frequency is

```text
M_alias(q/D) asymp q/D^(3/2)=q^(3/11).            (2.5)
```

If each packet is bounded at diagonal strength and then summed absolutely,
the right side of (1.1) is multiplied by (2.4); Cauchy gives
`q*sqrt(M_alias(K))`, not `q`.  Dyadic summation does not remove the loss:
for `K>P`,

```text
M_alias(K)*q^2/K asymp q^2/P                     (2.6)
```

on every dyadic block.  A merged Hankel chart can cancel this packet
ledger, but packetwise Cotlar cannot.

## 3. Full determinant-lattice Poisson is basis invariant

Fix a primitive reference `(p,r)`.  In determinant/first-coordinate
variables one strip lies in

```text
Lambda={(h,a) in Z^2: a==-inverse(r)*h (mod p)}.
```

It has basis

```text
(p,0), (-r,1),          det Lambda=p.             (3.1)
```

The dual lattice is exactly

```text
Lambda^*={(j/p,n+r*j/p):j,n in Z}.                (3.2)
```

For a smooth determinant cutoff of length `D`, full two-dimensional Poisson
therefore contains the factor

```text
What_h(D*j/p).
```

It leaves

```text
|j|<<p/D asymp q/D                               (3.3)
```

active fractional branches.  The integer `n` absorbs the integer part of
the stationary derivative in the shell coordinate.  An `ell`-dependent
unimodular basis merely reindexes (3.2); the dual covolume and the number of
points selected by (3.3) are invariant.  A continued-fraction partition may
have only logarithmically many named cells, but those cells collectively
retain the same `q/D` dual multiplicity.  With two strips their coupled
stationary correlations are the existing HSM/outer-fan kernel.

## 4. Parseval and an actual-reference alias

For an interval of `P<=R` quotient translations,

```text
W_P(j)=sum_(0<=r<P)e(-j*U*r/R)
```

satisfies exactly

```text
sum_(j mod R)|W_P(j)|^2=R*P,
sum_(j mod R,j!=0)|W_P(j)|^2=R*P-P^2.             (4.1)
```

Since `P/R<<1`, deleting the coherent residue removes only a negligible
fraction of the translation `L^2` mass.

The following finite fixture shows that a nonprincipal cross-block phase
can also be exactly one without violating odd-prime or actual-reference
arithmetic:

```text
q=159779,              P=16,             K=312,
S=4992=K*P,            R=4993,           (U,V)=(1,1),
x=P*(R,S)+(U,V)=(79889,79873).                     (4.2)
```

Here `q`, `79889`, and `79873` are prime; the two coordinates of `x` lie
strictly in the project shell, `R*V-S*U=1`, and `det((R,S),x)=1`.  Moreover
`D=q^(16/33)` is comparable with `P^2`, while

```text
q/D^2<K<q/D.                                      (4.3)
```

In the stabilizer increment from the stationary fan orbit, choose

```text
d=K, A=P, g=1, (r,r',s,s')=(1,1,2,1).
```

Then `Delta=s*r-s'*r'=1` is nonprincipal but

```text
-d*A*Delta/(g^2*S)=-1.                            (4.4)
```

Thus no coefficient-blind Cotlar estimate can demand decay between all
distinct quotient blocks, even in a chart containing an actual prime
reference.  The filled points responsible for a completed alias need not
all be actual prime powers, so (4.2)--(4.4) do not disprove the desired
mask-sensitive `L^1` theorem.

## 5. Why the `P^3` spacing fallback gives no hidden improvement

The quantity in (2E.F7N1)--(2E.F7N3) controls only the outer-center diagonal

```text
sum_(ell,m,n)|G_(m,n)(ell)|^2,
G_(m,n)(ell)=P^(-2)D_P(ell*A_mn)D_P(ell*B_mn).    (5.1)
```

It does not control

```text
sum_ell |sum_(m,n)e(phi_mn(ell))*G_(m,n)(ell)|^2, (5.2)
```

whose expansion contains all distinct-center pairs.  Identifying (5.1)
with (5.2) would incorrectly turn the loss `P` in (2E.F7N3) into a
`sqrt(P)` loss after Cauchy and suggest a `D^(5/4)` slope cap.  A
coefficient-blind passage from (5.1) to (5.2) costs the `P^2` outer centers
by Cauchy, and supplies no improvement.  A signed cross-center HSM theorem
is exactly the missing input.

## 6. Status

```text
dyadic target M(K)<<q^2/K:                         EXACT SUFFICIENT FORM;
diagonal admissible on every Selberg dyadic block: PROVED;
full-lattice Poisson logarithmic-cell bypass:       FALSE;
translation Parseval minor-residue saving:          FALSE;
odd-prime actual-reference nonprincipal alias:      EXPLICIT FINITE FIXTURE;
F7N1 implies a D^(5/4) slope cap:                   FALSE;
merged exact affine/Hankel packets:                 CLOSED PREVIOUSLY;
scattered signed high-frequency aggregation:        OPEN;
slope-block and uniform four-cycle bounds:           OPEN.
```

