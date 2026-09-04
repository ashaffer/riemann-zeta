# QP packet-free energy: reciprocal mixed differences and the broad-rectangle gate

**Date:** 2026-08-24  
**Verdict:** the reciprocal rounding does give a sharp new exclusion: an
additive completion rectangle whose two side lengths have product between
`D` and `q` cannot occur.  All rectangles below that gap contribute only
`O(D^2 log q)`, so the proposed `D^(5/2+o(1))` packet-free energy theorem
reduces to rectangles with side product `>>q`.  Neither line-packet peeling,
Szemeredi--Trotter, nor the centered fourth moment in Yao Zhi's
arXiv:2608.15458 controls those broad, possibly isolated, rectangles.

No packet-free energy theorem or sharp four-cycle bound is claimed.

## 1. Exact reciprocal mixed difference

Fix the endpoint `x` and write

```text
C=C_x=T/x asymp q^2,
|a_i v_i-C|<=C_0 D,
a_i,v_i in [alpha q,beta q].                         (1.1)
```

An additive-energy quadruple in the completion projection can be written

```text
a_00=a,       a_10=a+r,
a_01=a+s,     a_11=a+r+s,                            (1.2)
```

with all four entries in the shell.  Put

```text
Box v=v_00+v_11-v_10-v_01 in Z.                      (1.3)
```

Writing `v_i=C/a_i+epsilon_i`, `(1.1)` gives
`|epsilon_i|<<D/q`.  Direct subtraction gives the exact identity

```text
Box v
 =C*r*s*(2a+r+s)/[a(a+r)(a+s)(a+r+s)] + O(D/q).     (1.4)
```

Since all four denominators lie in one fixed positive shell,

```text
c_1 |r s|/q
 <= |C*r*s*(2a+r+s)/[a(a+r)(a+s)(a+r+s)]|
 <= c_2 |r s|/q.                                    (1.5)
```

Choose a sufficiently small fixed `c>0`.  If `|rs|<=c q`, then the
right side of `(1.4)` has absolute value below one for large `q`.
Consequently the integer `Box v` is zero.  Substitution back into `(1.4)`
and the lower bound in `(1.5)` then imply

```text
|r s|<<D.                                             (1.6)
```

Thus there is an exact forbidden annulus:

```text
C_1 D<|r s|<c q   =>   no occupied energy rectangle. (1.7)
```

Taking `r=s` recovers the reciprocal three-term-progression gap.  If
`a,a+s,a+2s` are occupied and `s^2<cq`, their carrier second difference is
zero, so the three full points form an affine packet; moreover existence
forces `s^2<<D`.

## 2. The entire narrow sector is below target

The parametrization `(1.2)` is injective once the ordered base and the two
ordered side lengths are fixed.  Degenerate rectangles (`r=0` or `s=0`)
contribute `O(H^2)`.  For each of the `H<=D` possible bases,

```text
#{(r,s) in Z^2:r*s!=0, |r*s|<<D}<<D log(2D).          (2.1)
```

Therefore `(1.6)` gives, without using packet peeling,

```text
E_narrow
 :=#{energy quadruples with |r*s|<c q}
 <<H D log q+H^2
 <<D^2 log q.                                        (2.2)
```

This is smaller than the desired `D^(5/2+o(1))` scale by a square-root
power.  On the packet-free family `P_0`, the reciprocal-projection theorem
is consequently equivalent, up to `(2.2)`, to the following broad estimate:

```text
#{packet-free occupied rectangles (1.2) with |r*s|>=c q}
 <<D^(5/2) q^o(1).                                   (BR)
```

For these rectangles `Box v` is allowed to be a nonzero integer of size
`asymp |rs|/q`; reciprocal rounding gives no zero-recurrence.

## 3. Why incidence and packet arguments stop at `(BR)`

The exact Freiman map identifies completion energy with defect energy, but
a popular defect difference may be a matching of disjoint two-point
secants.  The three-point lemma applies only when two such edges concatenate.
Behrend sets show that energy alone does not force this: a subset of an
interval can have energy `D^(3-o(1))` and no three-term progression.

The classical `|A|^(5/2)` energy bounds for convex sets do not apply to a
coordinate projection merely because the lifted points lie near a convex
reciprocal graph.  For the elementary model

```text
Q_N={(n,n^2):1<=n<=N},
```

no three lifted points are collinear, while the first projection is
`[1,N]` and has additive energy `(2N^3+N)/3`.  Convex-energy theorems require
the *values whose energy is counted* to have the relevant strictly convex
spacing; they do not bound an arbitrary coordinate projection.  The
physical product band adds the mixed-difference restriction `(1.7)`, but
after `|rs|>>q` that restriction has no zero-integer consequence.

Szemeredi--Trotter controls rich lines.  A broad rectangle in `(BR)` uses
two secants and can have every full affine line incident to only two retained
points.  Hence the standard rich-line decomposition has no term that pays
for `(BR)`.  Applying an incidence theorem only to the completion projection
is also invalid: completion-collinear points need not have affine carrier
coordinates, which is exactly what `(1.4)` measures.

For two defect/completion difference vectors `(d,r)` and `(e,s)`, the
lattice determinant

```text
Delta=(d*s-e*r)/y in Z,        |Delta|<<D             (3.1)
```

is exact.  It does not reduce `(BR)`: the additional integer label
`Box v` ranges up to `asymp |rs|/q`, and fixed `(Delta,Box v)` still permits
isolated two-secant configurations.  A Pluecker pigeonhole therefore faces
as many as `D*q` raw labels, already larger than the desired energy scale.

## 4. Audit of the August 2026 centered fourth moment

Theorem 1.1 of Yao Zhi,
[*Five-Term and Higher Congruences Involving Arbitrary Sets and Short
Intervals Modulo a Prime*](https://arxiv.org/abs/2608.15458), proves

```text
sum_(a!=0)|sum_(m in M,x in X)e_p(a*m*x^(-s))|^4
 <<p H^2 M^2 (H+min(M,sqrt(p)))^2 p^o(1).            (4.1)
```

At `p=y asymp q` and `H=M=D=p^(16/33)<sqrt(p)`, `(4.1)` is

```text
<<p D^6 p^o(1),                                      (4.2)
```

or `D^6 p^o(1)` after dividing by `p` in its centered-correlation identity.

The exact wedge elimination has the schematic modular form

```text
k*v ==T+x*e (mod y),          |k|,|e|<<D,             (4.3)
```

so `v=m*k^(-1)` with `m=T+x e`.  This resemblance does not give `(BR)`:

1. `(4.1)` controls the full Cartesian set `M x X`.  The physical wedges
   form a graph `m=m(k)` and are then cut by the arbitrary actual-carrier
   mask.  No graph-weighted or matching-weighted estimate appears in
   Theorem 1.1.
2. PFRE counts `k_1-k_2=k_3-k_4`.  Using `(4.3)` turns this into a four-term
   congruence in `m_i*v_i^(-1)` whose denominators `v_i` lie in the arbitrary
   carrier mask, not shifted intervals.
3. Even a positivity majorant by the full Cartesian fourth moment lands at
   the `D^6` correlation scale, whereas PFRE needs `D^(5/2)`.
4. The paper's sub-square-root application starts with five additive ratio
   summands.  There is no fifth physical relation available here, and the
   four-term/masked energy is precisely the exceptional structured case.
5. Theorem 1.1 requires a prime modulus.  A physical endpoint is only known
   to be a prime power, so even the unmasked formal specialization is not
   uniform over the actual endpoint set.

Thus `(4.1)` is not a proof of PFRE, though its centered-energy mechanism is
a plausible model for the genuinely new graph-weighted theorem that would
be needed.

## 5. Exact surviving gate

```text
reciprocal 3AP/rectangle mixed-difference identity: PROVED;
forbidden product annulus D<<|r*s|<<q:              PROVED;
narrow energy O(D^2 log q):                         PROVED;
Szemeredi--Trotter closes broad two-secants:         NO;
Yao Theorem 1.1 applies to the physical graph mask: NO;
broad-rectangle estimate (BR):                      OPEN;
packet-free reciprocal energy D^(5/2+o(1)):         OPEN.
```

The rational identities and exact exponent margins are replayed in
`src/qp_dense_defect_cf_energy_gate.py` and
`src/test_qp_dense_defect_cf_energy_gate.py`.
