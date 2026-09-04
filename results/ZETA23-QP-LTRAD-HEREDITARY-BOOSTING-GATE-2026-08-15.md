# QP LTRAD: hereditary boosting gate and long-interval obstruction

**Date:** 2026-08-15  
**Binary verdict:** no support-only weak-learning or hereditary interval
boosting theorem can prove `LTRAD(d,c)`.  There are finite-band node systems
of prime-shell cardinality for which every sufficiently long contiguous
interval has a strong negative uniform value at one common legal height,
while the full radial antipode radius is smaller than `N^-c`.

The obstruction can be made stable, distinct, rationally independent, and
supported in one fixed log shell.  It is not an exact actual-prime-log
counterexample: transferring it to the primes would require frequency
accuracy much finer than the available prime mesh.  Thus actual-prime
`LTRAD(d,c)` remains open, and no QP-to-strip implication is proved.

---

## 1. Exact target and its signed weak-learning dual

Put

```text
H_N=[N^.01,N^A],                 A=50/33,
K_N=[N^(1/2),N^(A')],            A'<A,
a(t)=(cos(tu_j))_(j<=M).                              (1.1)
```

At one fixed center, write `r_N^QP=r_+(H_N)`.  The weakest sufficient
reverse adapter isolated in the mass audit is a centerwise statement

```text
LTRAD(d,c):
E_N^-(A')>=N^-d  ==>  r_N^QP>=N^-c.                  (1.2)
```

Moment duality shows why ordinary boosting is mismatched.  To prove
`r_+(H_N)>=r`, one must defeat every **signed** coefficient vector `y` with
carrier `sum_j y_j=1`:

```text
inf_(t in H_N) sum_j y_j cos(tu_j)<=-r.              (1.3)
```

A large prime-interval event proves (1.3) for one nonnegative uniform
vector.  Even a hereditary collection of such events only tests interval
probabilities.  Multiplicative-weights boosting normally ranges over
nonnegative coordinate distributions; it does not test the signed affine
class in (1.3).  Assuming the signed weak-learner property (1.3) is exactly
assuming the desired radial conclusion by the same duality.

The following construction makes this mismatch quantitative.

---

## 2. A Fejer hard core

Fix exponents

```text
d>0, c>0, eta>0,          c+eta<1-d.                 (2.1)
```

Let

```text
M=floor(N/log N),                 L=floor(N^(c+eta)),
Delta=w/(4L),                    h_j=j Delta, 1<=j<=L. (2.2)
```

On these `L` hard nodes take the positive triangular weights

```text
lambda_j=2(L+1-j)/[L(L+1)].                           (2.3)
```

The Fejer identity gives, on the whole real line,

```text
sum_(j=1)^L lambda_j cos(t h_j)>=-1/L.               (2.4)
```

Perturb every hard node by at most

```text
delta_N<=1/(L N^A).                                  (2.5)
```

Since `sum lambda_j=1`, the cosine Lipschitz bound preserves

```text
sum_j lambda_j cos[t(h_j+epsilon_j)]>=-2/L
                                  for t in H_N.       (2.6)
```

Extend these weights by zero on every additional node.  They remain a legal
positive carrier-one DPA vector for the complete node family.  Hence

```text
r_+(H_N)<=2/L=2N^[-(c+eta)+o(1)]<N^-c.              (2.7)
```

Adding any number of easy nodes cannot remove this certificate because its
coefficients on those nodes are exactly zero.

---

## 3. A full-density easy block and hereditary negative intervals

Choose, for example,

```text
t_0=8 pi M/w asymp M asymp N/log N.                   (3.1)
```

This lies in both `K_N` and `H_N`.  There are `asymp M` odd lattice
frequencies

```text
e_k=(2m_k+1)pi/t_0                                   (3.2)
```

across `(0,w)`; the displayed constant leaves several times `M` choices.
Select `M-L` of them with bulk spacing `asymp 1/M`, omitting the `o(M)`
choices too close to a hard node.  At the common height `t_0`,

```text
cos(t_0 e_k)=-1.                                     (3.3)
```

Perturb all easy nodes, if desired, by the same scale (2.5).  Then
`t_0 delta_N=o(1)`, so every easy cosine in (3.3) is `-1+o(1)`.  The
perturbations may be selected off the countable union of rational
hyperplanes; all nodes are then distinct and rationally independent.

Order all nodes increasingly.  The easy nodes may be spread throughout the
whole shell, so no macroscopic frequency gap is needed.  For any contiguous
interval `J` containing `q` nodes, at most `L` are hard.
At `t_0`, even allowing the worst value `+1` on every hard node,

```text
sum_(j in J)cos(t_0u_j)<=-q+2L+o(q).                 (3.4)
```

Because `L=o(N^(1-d))`, every interval with
`q>=N^(1-d)` has negative mass `(1-o(1))q/N`.  At the literal endpoint
`q=N^(1-d)` this is just below `N^-d`; for every fixed `epsilon>0`, intervals
with `q>=(1+epsilon)N^(1-d)` realize the exact `N^-d` threshold for all
sufficiently large `N`.  Equivalently one may use the usual fixed-constant
or exponent slack in the premise.  The complete `M`-node interval is much
stronger:

```text
-N^-1 sum_(j=1)^M cos(t_0u_j)
 >=(1-o(1))M/N=(1-o(1))/log N>>N^-d.                 (3.5)
```

Thus the negative event uses the entire prime-density-sized carrier, and a
hereditary family of long subintervals has the same weak learner at one
common height.  Nevertheless (2.7) makes the radial conclusion in (1.2)
false.

### Theorem 3.1 (abstract hereditary LTRAD obstruction)

For every fixed `d,c>0` with `c<1-d`, and every fixed polynomial band
exponent `A>1`, there is a sequence of `M=N^(1+o(1))` distinct nodes in
`(0,w)` such that

1. the full uniform interval has mass-normalized negative depth
   `>>(log N)^(-1)>>N^-d` at a height in `K_N`;
2. every contiguous interval of at least `N^(1-d)` nodes has the same
   negative value up to `1-o(1)` relative error, and every interval of at
   least `(1+epsilon)N^(1-d)` nodes meets the exact `N^-d` threshold for each
   fixed `epsilon>0` and all sufficiently large `N`;
3. `r_+(H_N)<N^-c`;
4. the nodes may be chosen rationally independent and within
   `N^[-A-c-eta+o(1)]` of the displayed hard/easy model.

The theorem is centerwise; it does not assert a simultaneous construction
at every comparable center or control a supremum over such centers.  The
proof is (2.2)--(3.5).  It defeats any centerwise LTRAD theorem whose hypotheses
use only cardinality, compact shell support, polynomial aperture, ordering,
large interval mass, hereditary subinterval mass, or qualitative rational
independence.

---

## 4. Why this is not an actual-prime counterexample

The stability tolerance forced by the Fejer hard core is

```text
delta_N<<1/(L N^A)=N^[-A-c-eta+o(1)].                (4.1)
```

At the project aperture this is strictly finer than `N^-A`, whereas actual
prime-log nodes have average spacing about `log N/N` and the strongest
uniform prime-gap transfer used in the project is much coarser still.
Moving the model nodes to the nearest actual prime logs therefore incurs

```text
N^A * (prime-log displacement),                      (4.2)
```

which is not `o(1/L)`.  The countermodel is compatible with prime-shell
cardinality and average log mesh, and
survives rational-independence perturbation, but it does not preserve the
exact prime support.  It cannot be cited as a zeta no-go.

Conversely, constant-fraction support does not by itself help: the full
uniform direction in (3.5) already uses every node.  What an actual-prime
proof must exclude is the existence of a small adaptive hard core carrying
a Fejer-quality DPA certificate while the canonical prime mass is negative
mostly on its complement.  This is a source-sensitive carrier statement,
not an interval-counting or ordinary boosting lemma.

---

## 5. Binary disposition

```text
probability-normalized RAD:                FALSE on actual primes;
mass-normalized phase bridge:              PROVED;
generic LTRAD from one long interval:       FALSE;
generic LTRAD from all long subintervals:   FALSE;
nonnegative weak-learning/boosting:         INSUFFICIENT;
signed weak-learning hypothesis:            EQUIVALENT TO RADIAL GATE;
actual-prime LTRAD(d,c):                    OPEN;
QP => strip:                                NOT PROVED.
```

Executable exponent and Fejer replays:

- `src/qp_ltrad_hereditary_gate.py`;
- `src/test_qp_ltrad_hereditary_gate.py`.
