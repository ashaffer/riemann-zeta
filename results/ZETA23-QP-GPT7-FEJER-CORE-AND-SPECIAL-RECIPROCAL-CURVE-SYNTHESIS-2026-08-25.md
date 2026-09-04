# QP sharp four-cycle attack: the Fejer core and the special reciprocal-curve theorem

**Date:** 2026-08-25  
**Status:** the sharp `D^(1+o(1))` fourth-trace bound is **not proved**.  The
best unconditional project bound remains `D^(9/8+o(1))`.

This attack nevertheless makes a strict reduction.  It closes every dyadic
reciprocal mask outside an explicit cusp, proves the exact rigidity supplied
by the actual prime-power support, and isolates one sharp special-curve
estimate which would finish the fixed-sum route.

## 1. Exact Fejer reduction

At the critical scale put

```text
q=D^(33/16),       H=q/D.
```

For fixed `S`, sum over the fixed `a`-shell, with `a,S-a asymp q` and
`C asymp q^2`.  Take `0<=W<=1`, with `W=1` on the support being counted.  The
concrete normalized Fejer majorant reduces the count to

```text
mathcal R(S)=sum_a W(a)P(C/a)P(C/(S-a)),
P(theta)<<min(1,(H*||theta||)^(-2)).                   (1.1)
```

For dyadic `U,V>=1`, let

```text
N(U,V)=#{a:
 ||C/a||<<U/H,
 ||C/(S-a)||<<V/H},
m=min(U,V),       M=max(U,V).                          (1.2)
```

Then

```text
mathcal R(S)<<sum_(U,V) N(U,V)/(U^2*V^2).              (1.3)
```

Counting the product labels in the narrower coordinate gives rigorously

```text
N(U,V)<<D*m*q^o(1).                                    (1.4)
```

Therefore one mask contributes at most

```text
D/(m*M^2)*q^o(1).                                      (1.5)
```

Every mask with

```text
m*M^2>=sqrt(D)                                         (1.6)
```

is already closed at the desired `sqrt(D)` scale.  The only unhandled region
is

```text
m*M^2<sqrt(D).                                         (1.7)
```

In particular `M<D^(1/4)`, and a balanced mask has
`U,V<D^(1/6)`.  This is sharper than the earlier square
`U,V<=D^(1/4)`.

## 2. What local packet rigidity does and does not give

Partition the `a`-line by a regular grid of length
`ell=c*q^(1/3)` (apart from endpoint fragments).  Three counted points in one
block make both integer reciprocal determinants vanish.  Hence every
populated block is one bi-affine packet, up to two isolated atoms.  A packet
has capacity

```text
O(1+sqrt(D*m)).                                        (2.1)
```

This is rigorous, but it is not the global inverse theorem.  The shell has
`asymp q^(2/3)` such blocks, while even the largest desired count in (1.7) is

```text
D^(7/6)=q^(56/99)<q^(2/3).                             (2.2)
```

Thus the local argument permits a target-sized hostile set with one atom in
each of distinct blocks.  Local collinearity cannot force two such atoms onto
a common packet.
The proved inverse conclusion is only that a power violation uses many
spatially separated block locations, not many distinct directions.

## 3. Exact gain from the actual prime-power support

The physical nodes are

```text
P_q={p^j:(q/2)e^(-0.2)<=p^j<=(q/2)e^(0.2)}.            (3.1)
```

Since the endpoint ratio is `e^0.4<2`, there is at most one power of each
prime base in the shell.  Distinct nodes are pairwise coprime, and

```text
u*z=u'*z'  =>  {u,z}={u',z'}                          (3.2)
```

as multisets.

For a fixed actual colour `x`, let `X=av-bw`.  The zero-defect slice is now
completely rigid:

```text
X=0  =>  diagonal or swapped tangent,
N_(X=0)(U,V)<<1+sqrt(D*m).                             (3.3)
```

Every nonzero defect of size `o(q)` uses four cross-disjoint nodes and lies
in the primitive, cross-coprime chart.  This deletes spurious rational
tangent slopes, but it does not count the nonzero labels.

There is a useful matching formulation.  Fix the harmless band constant `c`
and take `q` large enough that `2*c*D*M<min(P_q)`.  Define

```text
T_U(a)=v  iff  a,v in P_q and |a*v-C|<=c*D*U,          (3.4)
```

and define `T_V` similarly.  Each is an order-reversing partial involution;
two distinct product labels in the union of the two bands cannot share a
factor.  The literal count is exactly

```text
N_P(U,V)=#{a in dom(T_U): S-a in dom(T_V)}.             (3.5)
```

So the remaining problem is an overlap of two multiplicative matchings under
the additive reflection `a -> S-a`.  Unique factorization proves only
`N_P(U,V)<<D*m`: it does not control the number of isolated alternating
matching components, and arbitrary selected weights may retain all of them.

The physical centre adds no hidden modulus.  After fixing `x`,

```text
r=8*x*n-q^3                                             (3.6)
```

is a bijective relabelling of the `O(D*m)` product labels.  The congruence
`r==-q^3 (mod 8x)` is therefore not an independent saving.

## 4. The exact factorization ceiling

If

```text
n=a*v,       ell=(S-a)*w,
```

then the identity

```text
(S*v-n)*(S*w-ell)=n*ell                                (4.1)
```

is exact.  Fixing `(n,ell)` gives only `q^o(1)` possibilities by divisor
enumeration.  Summing over the short label rectangle, however, returns the
one-product ceiling (1.4); it does not create the missing factor
`sqrt(D)/(m*M^2)`.  The shifted-semiprime formula in the actual support has
the same limitation: `O(1)` orientations per label, but `O(D*m)` labels.

## 5. Generic space-curve theory is too weak

Normalize `a=q*t`, `S=q*s`, `C=q^2*c`.  The ideal curve is

```text
gamma(t)=(t,c/t,c/(s-t)),
det(gamma',gamma'',gamma''')
 =12*c^2*s/(t^4*(s-t)^4).                              (5.1)
```

Thus torsion is uniformly nonzero on the shell.  The torsion hypothesis is
not the issue.  Even granting uniformity over this compact curve family,
Huang's fixed-denominator theorem gives only, after enlarging to the
isotropic thickness `D*M/q`,

```text
N(U,V)<<D^2*M^2/q+q^(3/5)*(log q)^(4/5).               (5.2)
```

The generic error is `q^(3/5)=D^(99/80)`.  In (1.7), the largest desired
right side is `D^(7/6)`, so (5.2) misses even its most favourable core mask
by `D^(17/240)`.  See [Huang, *Integral points close to a space
curve*](https://arxiv.org/abs/1809.07796), Theorem 1.

The August 2026 varying-denominator theorem of Chen--Seeger--Srivastava--
Technau gives an essentially sharp aggregate count, but it does not imply a
fixed-`S` estimate: a single denominator may consume its error term, and
varying `S` while holding `C` fixed changes the normalized curve parameter
`C/S^2`.  See [*Sharp Bounds for Rational Points Near Space
Curves*](https://arxiv.org/abs/2608.09009), Theorem 1.2.

## 6. The precise breakthrough theorem

The natural special reciprocal-curve estimate is

```text
N(U,V)
 <<q^o(1)*(D^2*U*V/q+sqrt(D*min(U,V))).                (6.1)
```

The first term is the anisotropic volume prediction.  The second is
necessary: for `C=Q^2`, `S=2Q`,

```text
(a,b,v,w)=(Q+y,Q-y,Q-y,Q+y)
```

has both product errors `-y^2` and supplies `asymp sqrt(D*m)` full-integer
tangent points.

Equation (6.1) closes every mask.  Indeed,

```text
[D^2*U*V/q]/[U^2*V^2]=D^2/(q*U*V)<=D^(-1/16),
sqrt(D*m)/(U^2*V^2)=sqrt(D)/(m^(3/2)*M^2)<=sqrt(D).    (6.2)
```

Only logarithmically many dyadic masks occur.  Hence (6.1) would prove the
fixed-`S` `sqrt(D)q^o(1)` theorem and complete this route to the sharp
four-cycle input.  The project-wide compatibility with the remaining
post-peeling sectors would still have to be assembled explicitly.

No current argument proves (6.1).  A successful proof must combine:

1. an arithmetic major-arc classification showing that the reciprocal
   curve's only power-sized fixed-denominator obstruction is the tangent
   packet;
2. an anisotropic minor-arc estimate giving the volume term while retaining
   both reciprocal masks;
3. either the actual multiplicative matching or a vector-valued average in
   the physical sum parameter, so that isolated components cannot be summed
   absolutely.

This is the point at which a genuinely new mask-sensitive two-inverse large
sieve, rather than another local packet lemma, is required.

## 7. Binary status

```text
sharp fourth trace D^(1+o(1)):                         NOT PROVED;
best unconditional fourth trace:                       D^(9/8+o(1));
Fejer masks m*M^2>=sqrt(D):                            CLOSED;
balanced unresolved mask range:                        U,V<D^(1/6);
local q^(1/3) bi-affine packet structure:               PROVED;
constant-threshold global-packet inverse:               FALSE;
exponent-level global-packet inverse:                   NOT PROVED;
actual zero-defect slice <=sqrt(D*m):                   PROVED;
actual core slice 0<|X|<min(P_q) primitive/cross-coprime: PROVED;
special centre supplies an independent modulus:         FALSE;
generic space-curve theorem closes the core:             NO;
special reciprocal-curve estimate (6.1):                OPEN;
power counterexample to (6.1):                          NOT FOUND.
```

## Reproducibility

The exact ledgers and fixtures are in:

```text
src/qp_coupled_cusp_fejer_inverse.py
src/test_qp_coupled_cusp_fejer_inverse.py
src/qp_pair_sum_selberg_ledger.py
src/test_qp_pair_sum_selberg_ledger.py
src/qp_fixed_s_packet_dispersion_audit.py
src/test_qp_fixed_s_packet_dispersion_audit.py
```

The detailed companion reports are:

```text
results/ZETA23-QP-COUPLED-CUSP-FEJER-TTSTAR-AND-REMOTE-PACKET-INVERSE-2026-08-25.md
results/ZETA23-QP-FIXED-S-PACKET-OR-DISPERSION-GAP-AUDIT-2026-08-25.md
results/ZETA23-QP-FIXED-S-PACKET-OR-DISPERSION-HOSTILE-STABILITY-AUDIT-2026-08-25.md
results/ZETA23-QP-ACTUAL-PRIME-POWER-FIXED-S-SHIFTED-DIVISOR-AUDIT-2026-08-25.md
```
