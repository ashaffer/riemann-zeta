# QP `q^2` packet triangles, weighted principal theorem, and residual Carleson gate

**Date:** 2026-08-24  
**Verdict:** the `q^2` family can be reorganized exactly into a canonically
ordered family of vertex-disjoint triangle matchings.  Its square function
already has the sharp `sqrt(D)` scale.  The coefficient-sensitive coarse
principal block is also harmless: it is a disjoint sum of weighted partial
permutations with operator norm `O(D/sqrt(q))`.

This does **not** yet prove the sharp four-cycle bound.  The surviving
statement is a deterministic, mask-sensitive **unsigned unconditionality**
or matrix-Carleson theorem for the ordered matching family.  It is not a
formal consequence of disjoint residual intervals.  Literal prime-power
examples have nonzero adjacent-block cross-Gram and even branching
cross-Gram of norm `sqrt(6)`.

Thus this audit finds a sharper route and closes the proposed principal
polar term, but it does not close the primitive common-neighbour covariance.

---

## 1. Exact coarse residual atoms

Let

```text
S=S(q)={prime powers in [(q/2)e^(-.2),(q/2)e^(.2)]},
D=floor(q^(16/33)),
r(a,b,c)=8abc-q^3.                                    (1.1)
```

Use the exact coarse lift

```text
2|r(a,b,c)|<q^2.                                      (1.2)
```

For every occupied centered residual `r`, put

```text
A_r(b,c)=sum_a 1_(r(a,b,c)=r).                        (1.3)
```

### Proposition 1 (one residual, one unordered triangle)

Every occupied coarse residual determines one unordered multiset
`{a,b,c}`.  The matrix `A_r` consists of its complete permutation orbit.
Consequently:

```text
three distinct nodes:       A_r is the K_3 adjacency,  |A_r|=6;
two equal nodes:            |A_r|=3;
three equal nodes:          |A_r|=1.                  (1.4)
```

In every case `||A_r||<=2`.

**Proof.**  The residual determines the integer product

```text
abc=(q^3+r)/8.                                        (1.5)
```

The ratio of the shell endpoints is `e^.4<2`.  Hence the shell contains at
most one power of any fixed base prime.  Unique factorization of (1.5)
therefore determines the multiplicity, between zero and three, of every
shell node.  Symmetry in `a,b,c` supplies the complete orbit.  The displayed
matrix classification and norm bound are immediate.  `square`

Distinct residual atoms have disjoint physical matrix entries: a fixed
pair `(b,c)` has an allowed `a`-interval of length below one.

---

## 2. Exact `q^2` packet reconstruction

Put

```text
R={r mod q^2:0<|r|<=qD, q does not divide r},
alpha_h=q^(-2) sum_(r in R)e_(-q^2)(hr),
C_h=sum_r e_(q^2)(hr)A_r.                             (2.1)
```

The conditional expectation of `1_R` on an additive fibre modulo `q` is
exactly `2D/q`.  Thus on every occupied unit residual,

```text
1_R(r)=2D/q + sum_(q does not divide h)alpha_h e_(q^2)(hr).  (2.2)
```

Consequently the fine physical carrier is

```text
T=(2D/q)C_0 + sum_(q does not divide h)alpha_h C_h.   (2.3)
```

The executable replay evaluates all `q^2` frequencies for small shells and
recovers every occupied atom to absolute error below `6e-11`.

---

## 3. The exact centered packet-Gram identity

Let `n=|S|`, `P=I-J/n`,

```text
d_r=A_r 1,             e_r=|A_r|.                    (3.1)
```

Disjoint physical supports give the exact integer formula

```text
n^2 <P A_r P,P A_s P>_HS
 =n^2 e_r 1_(r=s)-2n<d_r,d_s>+e_r e_s.               (3.2)
```

This is the sought low-rank identity at Hilbert--Schmidt level.  Relative
to the diagonal atom Gram, the correction in (3.2) has rank at most `n`:
the vector `(e_r)_r` already lies in the row-degree span because
`e_r=<d_r,1>`.

There is also a large exact flat eigenspace.  Restrict to all-distinct
atoms and let `H` be their atom--vertex incidence matrix.  If

```text
H^T gamma=0,                                           (3.3)
```

then the degree correction vanishes and `gamma` is an eigenvector of the
normalized centered atom Gram with eigenvalue six.  At `q=5003` this space
has dimension `11`; at `q=25013` it has dimension at least `1334` among
`1869` all-distinct coarse atoms.

Thus physical centering removes the vertex-degree directions but leaves a
large balanced hyperedge-cycle space.  A finite list of degree or log-polar
modes does not diagonalize the operator problem.

### Scope of (3.2)

Equation (3.2) is a genuine exact identity, but it is a Frobenius identity.
It does not control

```text
C_h^* C_k                                                   (3.4)
```

in physical operator norm.  Transforming back to residual atoms turns
(3.4) into common-vertex walks between different triangles.  Those are
exactly the centered common-neighbour covariance.

---

## 4. A coefficient-uniform packet theorem needs an atomic term

The schematic estimate

```text
||sum_h alpha_h C_h||^2 << q sum_h |alpha_h|^2        (4.1)
```

cannot hold for arbitrary primitive packet coefficients before an
atomic/polar term is charged.  Fix one occupied residual `r_0` and put

```text
alpha_h=q^(-2)e_(-q^2)(h r_0),       q does not divide h.   (4.2)
```

Then

```text
sum_h |alpha_h|^2=(q-1)/q^3,
q sum_h |alpha_h|^2=(q-1)/q^2,                         (4.3)
```

whereas its physical synthesis is exactly

```text
1_(r=r_0)-q^(-1)1_(r=r_0 mod q).                       (4.4)
```

This retains an order-one triangle atom.  At the literal `q=107` shell,
even after double centering its squared norm is more than fifty times the
budget in (4.3).

This is not a counterexample to the actual interval coefficients (2.1),
nor to the sharp four-cycle bound.  It proves that the vector theorem must
use their interval structure, or include an explicit atom/polar term; an
arbitrary coefficient frame bound with square constant `q` is false.

---

## 5. The weighted coarse principal theorem

The unweighted coarse matrix `C_0` is not the correct object for the
coefficient-sensitive principal contribution.  For a coefficient vector
`z=(z_c)`, define

```text
P_c(a,b)=1_(2|8abc-q^3|<q^2),
A_0(z)=(2D/q) sum_c z_c P_c.                           (5.1)
```

### Proposition 2 (weighted principal Schatten bounds)

Every `P_c` is a partial permutation: it has row and column degrees at most
one.  The physical supports of `P_c` and `P_c'` are disjoint for `c!=c'`.
Therefore

```text
||A_0(z)||_HS^2
 =(2D/q)^2 sum_c |z_c|^2 |P_c|
 <=(2D/q)^2 n ||z||_2^2,                              (5.2)

||A_0(z)||_op <=2D sqrt(n)/q ||z||_2
              <=2D/sqrt(q) ||z||_2,                  (5.3)

||A_0(z)||_S4^4 <=16D^4/q^2 ||z||_2^4.               (5.4)
```

**Proof.**  For fixed `(a,c)`, condition (5.1) puts `b` in an interval of
total length

```text
q^2/(8ac)<1,                                          (5.5)
```

because every shell node is at least `(q/2)e^(-.2)`; the same argument
holds with `a,b` interchanged.  This proves the partial-permutation claim.
For fixed `(a,b)`, the allowed `c`-interval also has length below one, which
proves disjointness.  Equation (5.2) is then Pythagoras.  The inequalities
`||.||op<=||.||HS`, `|P_c|<=n`, `n<=q`, and
`||.||S4^4<=||.||HS^4` prove (5.3)--(5.4).  `square`

This closes the entire coefficient-sensitive coarse principal block at a
scale much smaller than `sqrt(D)`.  A log-polar subtraction may describe
some of its finite eigenvectors, but is not needed for its bound.

---

## 6. Canonical short-residual matching blocks

Let

```text
m=min S,                 L=8m,                        (6.1)
```

and partition `[-qD,qD]` into half-open intervals of length `L`.  Let `B_I`
be the sum of the selected triangle atoms whose residuals lie in `I`.

### Proposition 3 (each short block is a triangle matching)

The unordered triangles in a fixed block are vertex-disjoint.  Hence

```text
||B_I||<=2.                                            (6.2)
```

**Proof.**  Suppose atoms of residuals `r,s` share a vertex `v`.  Write
their complementary products as `xy,x'y'`.  Then

```text
r-s=8v(xy-x'y').                                      (6.3)
```

Two residuals in one half-open block have `|r-s|<8m<=8v`.  Equation (6.3)
therefore forces `xy=x'y'`; unique factorization makes the unordered
triangles equal.  Distinct atoms cannot do this.  Thus the atoms are
vertex-disjoint and `B_I` is a direct sum of matrices from (1.4). `square`

The total number of possible blocks is

```text
ceil((2qD+1)/(8m))=O(D).                              (6.4)
```

This construction is literal; it keeps the prime-power shell and hard fine
mask and performs no interval completion.

---

## 7. The sharp square function is already available

In the all-distinct sector, one triangle adjacency satisfies

```text
A_r^2=2I_(vertices of r)+A_r.                         (7.1)
```

The triangles inside one `B_I` are vertex-disjoint, so cross products
inside its square vanish.  Summing (7.1) gives the exact identity

```text
sum_I B_I^2=2 diag(d)+T,                              (7.2)
```

where `d(v)` is the hyperedge degree and `T=sum_I B_I`.

If `Delta=max d(v)`, Schur gives `||T||<=2Delta`.  Therefore

```text
||(sum_I B_I^2)^(1/2)||<=2 sqrt(Delta).               (7.3)
```

Repeated-node atoms are an already affordable bounded correction.  Also,
if `X_I=P B_I P`, then the Loewner inequality

```text
sum_I X_I^2 <= P(sum_I B_I^2)P                       (7.4)
```

holds, because the difference term is
`sum_I P B_I(I-P)B_I P>=0`.

At the active geometry `Delta<<Dq^o(1)`, (7.3)--(7.4) have exactly the
desired `sqrt(D)q^o(1)` scale.

### The surviving theorem

It would now suffice to prove the arithmetic unsigned-unconditionality
estimate

```text
||sum_I P B_I P||
 <<q^o(1)||(sum_I (P B_I P)^2)^(1/2)||.              (7.5)
```

More generally, a one-sided row/column square-function version compatible
with the actual masks would suffice.

For arbitrary disjoint-entry matching families, (7.5) is false: a
one-factorization of disconnected regular components has an all-plus
component eigenvector of size `D`, while its signed square function has
size `sqrt(D)`.  The only plausible source of (7.5) here is the arithmetic
ordering and product conservation of the actual residual blocks.

This is a more precise GPT-7 path than a scalar character estimate: prove
an arithmetic unconditionality theorem for the canonical matching family,
not a packetwise bound.

---

## 8. Product conservation and the boundary-order theorem

For an all-distinct matching block with `k` triangles and vertex set `V(I)`,

```text
prod_(r in I)(q^3+r)=8^k prod_(v in V(I))v.           (8.1)
```

Let two ordered blocks `I<J` contain the same number `k` of triangles.  If
`C=V(I) intersect V(J)`, cancellation in (8.1) gives

```text
 [prod_(s in J)(q^3+s)]/[prod_(r in I)(q^3+r)]
 = [prod_(v in V(J)\C)v]/[prod_(u in V(I)\C)u] >1.   (8.2)
```

Consequences:

1. Distinct ordered blocks cannot cover exactly the same vertex multiset.
2. The later block has strictly larger boundary product.
3. If the two blocks differ by only one vertex each, with earlier `x` and
   later `y`, then `y>=x+1`.  Writing `U=max S`, the exact necessary
   inequality is

```text
(U+1)/U <=((q^2+D)/(q^2-D))^k.                       (8.3)
```

At `q=25013`, (8.3) requires `k>=152`, while the largest observed block has
two atoms.  Thus the closest possible common-support obstruction is ruled
out very strongly.

For two or more boundary vertices, integer products can in principle be
much closer, so (8.2) alone does not prove (7.5).  A successful proof would
need a multi-boundary expansion or entropy theorem, not merely monotonicity.

---

## 9. Literal cross-block obstructions

The short-block theorem does not make different blocks orthogonal.

### Adjacent tangent overlap at `q=151`

The two selected all-distinct atoms are

```text
r=-1439:       {71,73,83},
r=-775:        {64,81,83}.                            (9.1)
```

They occupy adjacent canonical blocks and share `83`.  Exactly

```text
(-775)-(-1439)=664=8*83,
64*81-71*73=1.                                       (9.2)
```

Thus this is the minimal fixed-defect/tangent overlap.  Its raw cross norm
is `2`, and after deleting the physical constant mode,

```text
||P B_0 P B_1 P||=1.1203575988... .                  (9.3)
```

Deleting the additional log-linear mode lowers it only to
`0.94746...`; it does not create exact orthogonality.

### Branching overlap at `q=4751`

One earlier triangle is

```text
r=-251055:     {2048,2381,2749}.                     (9.4)
```

Two vertex-disjoint triangles in a later block are

```text
r=76625:       {2048,2357,2777},
r=78825:       {2083,2341,2749}.                     (9.5)
```

The earlier triangle shares two different vertices with the two later
triangles.  Consequently

```text
||B_2 B_23||=sqrt(6),
||P B_2 P B_23 P||=2.2918449812... .                 (9.6)
```

Projection off `span{1,log(2p/q)}` leaves `2.2906647429...`.  Hence neither
constant/degree subtraction nor the first log polar removes this genuine
branching cross-Gram.

An exhaustive scan of all `2737` prime values `101<=q<25000` found twelve
block pairs with overlap at least two.  Each had the same branching norm
`sqrt(6)`; no overlap larger than two occurred in that scan.  Representative
scans through `q=1000003` also had block-pair overlap at most two.  This is
useful evidence for a sparse interaction theorem, not a proof of one.

---

## 10. Log-polar spectral audit

Put

```text
x_p=log(2p/q)                                          (10.1)
```

and orthonormalize `1,x,x^2,...` on the actual shell.

For the fine selected carrier, the extreme vectors are not low-degree log
polynomials.  For example:

| `q` | constant-projected norm | `{1,x}`-projected norm | top tested linear correlation |
|---:|---:|---:|---:|
| 4,751 | 2.790719 | 2.790016 | below 0.023 |
| 25,013 | 2.542809 | 2.542573 | below 0.001 |
| 1,000,003 | 3.638350 | 3.638350 | negligible |

At `q=4751`, the carrier/square-function ratio is

```text
off constants:       1.147838...,
off {1,x}:           1.147895....                    (10.2)
```

Thus the linear log polar does not explain the primitive unsigned
alignment.

The unweighted coarse matrix does possess a real log-polar mode.  At
`q=25013`, a centered eigenvalue `-10.023988...` has `0.7748` squared
correlation with `x` and `0.8200` mass in degrees one through eight.  But an
unrelated positive eigenvalue `10.1864...` remains after deleting `x`.
Proposition 2 controls the coefficient-weighted coarse block in full, so no
finite polynomial extrapolation is needed there.

---

## 11. Finite spectral ledger

The following uses the literal prime-power shell.  `primitive norm` means
double centering after subtracting the exact weighted value `2D/q` from
every coarse residual atom in the unweighted diagnostic.

| `q` | `n` | coarse atoms | selected atoms | occupied blocks | cross-block shared vertices | fine norm | primitive norm |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 107 | 6 | 2 | 1 | 1 | 0 | 1.0000 | 0.9571 |
| 151 | 8 | 3 | 2 | 2 | 1 | 1.5000 | 1.3263 |
| 503 | 20 | 7 | 1 | 1 | 0 | 1.7000 | 1.5953 |
| 5,003 | 133 | 140 | 3 | 3 | 0 | 2.0000 | 1.9522 |
| 25,013 | 535 | 1,883 | 13 | 12 | 1 | 2.5428 | 2.5186 |

Every short block in the scan has norm at most two, exactly as Proposition
3 predicts.  Coarse-principal subtraction changes these already sparse
finite selected norms only modestly; its importance is the uniform weighted
theorem in Section 5.

---

## 12. Binary status

```text
one coarse q^2 residual = one unordered triangle:       PROVED;
exact primitive q^2 packet reconstruction:              PROVED;
centered packet HS Gram = diagonal + rank<=n correction:PROVED;
large balanced-flow Gram eigenspace:                    PROVED;
arbitrary coefficient square constant q:                FALSE;
weighted coarse principal op <=2D/sqrt(q):              PROVED;
weighted coarse principal S4^4 <=16D^4/q^2:             PROVED;
length-8min(S) residual blocks are matchings:            PROVED;
each block norm <=2:                                    PROVED;
sharp block square-function scale:                      PROVED;
ordered equal blocks cannot have identical support:     PROVED;
one-boundary near-common support below q/D atoms:        EXCLUDED;
different blocks are orthogonal:                        FALSE;
log-linear polar removes primitive cross-Gram:           FALSE;
arithmetic unsigned unconditionality (7.5):              OPEN;
mask-sensitive vector-valued two-inverse theorem:        OPEN;
sharp four-cycle bound:                                 NOT PROVED.
```

The exact builders and tests are

```text
src/qp_q2_packet_cross_gram_discovery.py
src/test_qp_q2_packet_cross_gram_discovery.py
```

and replay with

```bash
PYTHONPATH=src pytest -q src/test_qp_q2_packet_cross_gram_discovery.py
```

