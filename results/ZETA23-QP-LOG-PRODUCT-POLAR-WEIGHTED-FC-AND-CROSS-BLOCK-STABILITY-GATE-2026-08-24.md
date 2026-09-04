# QP log-product polar: weighted FC and cross-block stability

**Date:** 2026-08-24  
**Verdict:** product conservation does not yield the hoped-for power-saving
boundary between aligned residual blocks.  It creates a genuine common
logarithmic mode for the unweighted symmetric carrier matrix.  Constant
centering alone is therefore the wrong proposed carrier theorem unless a
coarse principal/Eisenstein channel is removed.

This does **not** produce a counterexample to the weighted four-cycle
estimate.  In the actual weighted matrix

```text
A_z(a,b)=sum_c z_c 1_(|8abc-q^3|<=qD),
||z||_2=1,                                             (0.1)
```

the mod-`q^2` principal coarse operator carries the logarithmic density
mode with coefficient `2D/q`.  Elementary overlap, Hilbert--Schmidt, and
Schur bounds give

```text
||A_z^(0)||_(S_4)^4
 <<D^4*M*q/q^4*q^o(1)
 <=D^4/q^2*q^o(1)=q^(-2/33+o(1)),                    (0.2)
```

where `M=|supp z|<=q^(1+o(1))`.  It is negligible.  At the critical
`M=D^(15/8)` it is smaller still, `D^(-5/16+o(1))`.

Thus the correct weighted route is to remove the **whole coarse principal
operator**, bound it by (0.2), and prove the mask-sensitive `q^2` theorem
for the primitive remainder.  The minimal unweighted polar space is not
just `span{1,log(2s/q)}`: projecting the log vector removes one Rayleigh
direction but leaves the second local `-1` direction on every triangle.
No finite polynomial tower follows from the product identity.

The primitive, post-peeling, mask-stable square function remains open.

---

## 1. Exact logarithmic triangle identity

Restrict first to the all-distinct symmetric physical sector.  Every
unordered physical triple

```text
tau={a,b,c},             |8abc-q^3|<=qD               (1.1)
```

brings all six permutations, so its carrier--colour projection is the
adjacency matrix of the triangle on `{a,b,c}`.  Pair uniqueness prevents
two distinct physical triples from sharing an edge.

Put

```text
x_s=log(2s/q),
theta_tau=x_a+x_b+x_c=log(8abc/q^3).                  (1.2)
```

For `eta=D/q^2<1/2`, the fine window gives

```text
|theta_tau|<=eta/(1-eta)<<D/q^2.                      (1.3)
```

Let `T_ad` be the all-distinct triangle adjacency and let `H` be its set of
unordered triangles.  Direct expansion gives the exact identity

```text
x^*T_ad*x
 =sum_(tau in H)
    [theta_tau^2-(x_a^2+x_b^2+x_c^2)].                (1.4)
```

If `t_s` is the number of physical triangles containing `s`, then

```text
x^*T_ad*x
 =-sum_s t_s*x_s^2+sum_tau theta_tau^2.               (1.5)
```

Let

```text
mu=1^*T_ad*1/n^2>=0,          A_ad=T_ad-mu J.          (1.6)
```

The empirical constant subtraction makes this Rayleigh quotient more
negative:

```text
-x^*A_ad*x
 =sum_s t_s*x_s^2-sum_tau theta_tau^2
    +mu*|sum_s x_s|^2.                                 (1.7)
```

Consequently

```text
||A_ad||
 >=[sum_s t_s*x_s^2-|H|*(D/q^2)^2*q^o(1)]
      /sum_s x_s^2.                                   (1.8)
```

The error in (1.8) is negligible.  Formula (1.8) is an exact conditional
lower bound by the `x^2`-weighted triangle degree.  Under the usual prime
density heuristic this degree is `D/(log q)^2`, which eventually exceeds
`sqrt(D)` by a power.  This is a heuristic warning rather than an
unconditional counterexample: proving that the ultra-short reciprocal
samples distribute their triangle mass across the logarithmic shell is one
of the open prime-mask problems.

The identity can also be written pointwise on one residual block.  If
`Q_I` projects onto the vertices covered by its triangle matching, then

```text
(T_I x)_s=-x_s+theta_(tau_I(s)),       s in supp Q_I,

||T_I x+Q_I x||_2
 <=(D/q^2)q^o(1)*sqrt(|supp Q_I|).                   (1.9)
```

Thus product conservation tends to **align** the negative logarithmic
responses of different blocks.  It does not make them orthogonal.

Literal prime-power matrices already display (1.5), although their current
degrees are below one:

| `q` | `D` | centered log Rayleigh | `x^2`-weighted `t_s` |
|---:|---:|---:|---:|
| 7,817 | 77 | `-0.1414` | `0.1398` |
| 100,003 | 265 | `-0.1900` | `0.1853` |
| 500,009 | 579 | `-0.2154` | `0.2100` |
| 1,000,003 | 811 | `-0.2944` | `0.2866` |

The small difference has the predicted sign and consists of the residual
square and empirical-centering terms.  These are finite diagnostics, not
asymptotic lower bounds.

## 2. What large cross-block correlation actually forces

Let `T_I,T_J` be two residual triangle blocks, let `U_I,U_J` be their
covered vertex sets, and put

```text
y_I=T_I z,                  y_J=T_J z.                (2.1)
```

Both output vectors are supported on their respective covered sets.  If

```text
|<y_I,y_J>|>=rho*||y_I||_2*||y_J||_2,                (2.2)
```

then, with `C=U_I intersect U_J`,

```text
||1_C y_I||_2>=rho||y_I||_2,
||1_C y_J||_2>=rho||y_J||_2.                          (2.3)
```

Indeed the inner product in (2.2) is supported on `C`, and Cauchy applied
in either order proves (2.3).

Let `cl_I(C)` be the union of the `I`-triangles which meet `C`.  Each
triangle has two neighbours at every vertex, so

```text
||1_C T_I z||_2^2<=4||1_(cl_I(C))z||_2^2.             (2.4)
```

Equations (2.3)--(2.4) are the strongest elementary weighted implication:
large normalized correlation forces coefficient mass in the two triangle
closures of a common output set.  It does **not** say that the two covered
vertex multisets are nearly equal.  At a small power violation of the
global square-root theorem, the average normalized correlation may itself
be a small power, and the forced common mass in (2.4) is correspondingly
tiny.

## 3. The log-product boundary has no power at project scale

There is an exact conservation law for the vertices covered by one block.
If block `I` contains `t` disjoint triangles and covers `U_I`, then

```text
sum_(s in U_I) log s
 =sum_(tau in I)log(product(tau)).                     (3.1)
```

Suppose blocks `I,J` have the same number `t` of triangles.  Let
`lambda_I,lambda_J` be representative log-products of their intervals,
let `delta` be their log-radius, and let

```text
r=|U_I minus U_J|=|U_J minus U_I|.                    (3.2)
```

The logarithmic diameter of the shell is `0.4`.  Subtracting an arbitrary
common reference from all vertex logs and using (3.1) gives

```text
r>=t*(|lambda_I-lambda_J|-2*delta)_+/0.4.             (3.3)
```

This proves that two perfect covers of exactly the same vertex set cannot
occupy disjoint residual intervals.  Quantitatively it is far too weak.
Across the entire fine window,

```text
|lambda_I-lambda_J|<<D/q^2,
t<=q^(1+o(1)),
```

so the right side of (3.3) is at most

```text
D/q*q^o(1)=q^(-17/33+o(1))=o(1).                     (3.4)
```

After integrality, (3.3) says only `r>=1`.  One boundary shell label has
`q^(1+o(1))` possible values, already enough entropy to distinguish the
`D=q^(16/33+o(1))` residual blocks.  Thus neither the mean identity nor a
simple entropy count forces a power-sized boundary.

There is a literal all-prime finite warning at

```text
q=10007,                     D=87.                    (3.4a)
```

The active product window contains the two triangles

```text
{4423,4877,5807},       residual -441567,
{4877,4967,5171},       residual -597631.              (3.4b)
```

Every displayed node is prime and lies in the project shell.  Partitioning
the product coordinate into intervals of width `4095<min(S)` puts the two
triangles in distinct blocks, while their covered sets share the vertex
`4877`.  This is not a power-sized countermodel, but it confirms that exact
primality/product support permits the one-boundary behavior left open by
(3.3); distinct blocks are not vertex-disjoint.

This explains why the affine triangle-factor obstruction is not repaired
quantitatively by saying that exact perfect covers are arithmetically
impossible.  A power spectral excess can be supported by many modest
clusters, and the product-mean ledger does not prohibit clusters differing
on only a few low-weight boundary labels.  No faithful asymptotic
prime-power realization of such a cluster is claimed.

## 4. Why the unweighted carrier warning is not an FC counterexample

The original weighted matrix satisfies the exact contraction identity

```text
(A_z*1)_a=sum_(b,c) z_c 1_(|8abc-q^3|<=qD)=(Tz)_a.     (4.1)
```

Hence a large carrier response only gives

```text
||A_z||_(2->2)>=||Tz||_2/sqrt(n),                      (4.2)
```

where `n=|S|=q^(1+o(1))`.  Even the heuristic logarithmic carrier size
`D/(log q)^2` yields through (4.2) only

```text
D/sqrt(q)*q^o(1)=q^(-1/66+o(1)),                       (4.3)
```

which tends to zero.  The coefficient normalization and the constant input
needed to pass from `T` to `A_z` remove the apparent operator obstruction.
Thus failure of the overly strong unweighted `sqrt(D)` carrier theorem
would not itself disprove FC.

There is a stronger direct estimate for the channel which carries this
mode.

## 5. The whole `q^2` principal coarse operator is weighted-negligible

The exact mod-`q^2` decomposition gives

```text
A_z^(0)(a,b)
 =(2D/q) sum_c z_c W((8abc-q^3)/q^2),                  (5.1)
```

where `W` is bounded and supported in a fixed subinterval of
`(-1/2,1/2)`.

For fixed `(a,c)`, its allowed `b` interval has length `O(1)`.  The same is
true after interchanging `a,b,c`.  Consequently, if `P_c^(0)` denotes the
unscaled coarse layer in (5.1),

```text
max row degree(P_c^(0))+max column degree(P_c^(0))=O(1),
||P_c^(0)||_(HS)^2<<q^(1+o(1)),                         (5.2)

max_(a,b) #{c:P_c^(0)(a,b)!=0}=O(1).                  (5.3)
```

For `||z||_2=1`, (5.2)--(5.3) and cellwise Cauchy give

```text
||A_z^(0)||_(HS)^2<<D^2/q*q^o(1).                     (5.4)
```

If `M=|supp z|`, Schur gives

```text
||A_z^(0)||_(2->2)
 <<(D/q)||z||_1 q^o(1)
 <=D*sqrt(M)/q*q^o(1).                                (5.5)
```

Therefore

```text
||A_z^(0)||_(S_4)^4
 <=||A_z^(0)||_(2->2)^2||A_z^(0)||_(HS)^2
 <<D^4*M/q^3*q^o(1).                                  (5.6)
```

Since `M<=q^(1+o(1))`, (5.6) proves (0.2).  At
`M=D^(15/8)` it is `D^(-5/16+o(1))`.

This bound is raw: it needs no constant, log, tangent, or chart
subtraction.  Schatten triangle then permits the entire operator (5.1) to
be removed before treating the primitive remainder.  Cross terms do not
create a problem.

The unweighted carrier version of (5.1) has row degree on the expected
`D/(log q)^2` scale, so it naturally contains the logarithmic Rayleigh mode
from Section 1.  This reconciles the two ledgers: the same coarse principal
channel is large in unweighted carrier norm and negligible after the
`2D/q` coefficient and the normalized FC weights are retained.

## 6. Minimal polar space and projection of the log mode

For weighted FC the economical polar choice is the **entire operator**
`A_z^(0)`, bounded by (5.6).  Replacing it by the two vectors `1,x` is both
unnecessary and insufficient.

On one triangle the adjacency spectrum is

```text
2 on the constant vector,
-1 on the two-dimensional sum-zero plane.              (6.1)
```

The physical log vector lies within `O(D/q^2)` of that sum-zero plane by
(1.3).  Projecting it removes at most one of the two local negative
directions.  If a block has `N` disjoint triangles, the `-1` eigenspace has
dimension `2N`; after imposing orthogonality to both the global constant
and global log vectors, dimension at least `2N-2` remains.  Hence

```text
||P_(1,x)^perp T_I P_(1,x)^perp||=1                 (6.2)
```

whenever the block contains more than one triangle.  There is no local
norm gain.

Nor does the product identity force a polynomial tower.  From
`x_a+x_b+x_c=O(D/q^2)` one controls the linear sum only.  For example,

```text
x_a^2+x_b^2+x_c^2
```

is generally of constant size and depends on the free difference between
two triangle coordinates.  Higher powers are not small or determined by
the remaining coordinate.  A fixed list `1,x,...,x^k` removes only a fixed
number of directions from the `2N`-dimensional local negative space.

Analytically, the coarse kernel in log variables has width `1/q`, hence
Mellin bandwidth `q`.  Its natural polar description is a full Mellin or
Eisenstein continuum, not a fixed polynomial rank.  In the weighted FC
norm, (5.6) is precisely what makes constructing that continuum
unnecessary.

After removing (5.1), the desired primitive theorem must still be stable
under the second-tensor and post-peeling masks from the companion mask
audit.  Projection of `x` does not address that problem.

## 7. Binary status

```text
exact triangle log Rayleigh identity (1.4):             PROVED;
empirical constant centering removes the log mode:       NO;
product conservation forces cross-block cancellation:   NO;
large normalized cross term => common covered output:    PROVED (2.3);
product-mean boundary lower bound:                        PROVED (3.3);
that boundary has a power at project scale:               NO;
unweighted carrier sqrt(D) from constant centering:       HEURISTICALLY FALSE;
unconditional actual-prime violation:                     NOT PROVED;
log mode directly violates normalized weighted FC:        NO;
weighted q^2 principal HS bound (5.4):                    PROVED;
weighted q^2 principal S4^4=o(1):                        PROVED;
minimal weighted polar:                                   WHOLE COARSE BLOCK;
span{1,x} controls post-peel remainder:                   NO;
finite polynomial tower is forced by product identity:    NO;
primitive mask-sensitive q^2 square function:             OPEN;
sharp four-cycle theorem:                                 NOT PROVED.
```

Finite identities and exponent replays are in

```text
src/qp_log_product_polar_gate.py
src/test_qp_log_product_polar_gate.py
```
