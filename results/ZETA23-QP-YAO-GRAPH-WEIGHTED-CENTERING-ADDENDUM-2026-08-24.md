# Yao centered fourth moment: graph-weighted specialization audit

**Date:** 2026-08-24  
**Verdict:** Yao's centering identity extends exactly to graph-supported
coefficients, but the saving in his Theorem 1.1 does not.  For a matching
`m=m(k)` with an arbitrary injective carrier mask, the best uniform bound
from centering and Cauchy/Young is cubic energy.  This is sharp even for an
interval denominator set and a graph with no three collinear points.  At
the QP scale it gives `D^3`, missing the required `D^(5/2)` by `D^(1/2)`.
Completing the graph to the Cartesian box in order to invoke Yao is much
worse and gives `D^6`.

This is a no-go theorem for a mask-blind graph specialization.  The fixture
below is not an actual-prime QP product-band configuration, so it is not a
counterexample to the packet-free reciprocal-energy conjecture.

---

## 1. Exact weighted centering on a graph

Let `p` be prime, let `K` be a shifted interval or an arbitrary subset of
`F_p^*`, and let

```text
Gamma={(m(k),k):k in K}                                (1.1)
```

be a graph.  For coefficients `c_k`, put

```text
v_k=m(k)k^(-1),
S_Gamma(a)=sum_(k in K)c_k e_p(a v_k).                 (1.2)
```

Thus `v_k` is exactly the selected carrier in the modular wedge relation
`k v_k=m(k)`.  Define the weighted difference correlation

```text
R(z)=sum_(v_i-v_j=z)c_i conjugate(c_j).                (1.3)
```

Additive orthogonality gives

```text
(1/p)sum_(a!=0)|S_Gamma(a)|^4
 =sum_z |R(z)-|sum_k c_k|^2/p|^2.                     (1.4)
```

This is the graph version of equation (2) in Section 3 of
[Yao's paper](https://arxiv.org/html/2608.15458).  Nothing is lost at the
centering step.

Assume, as in the physical fixed-endpoint fan, that the carriers `v_k` are
distinct.  Regard `c` as a function on the carrier set.  Young's convolution
inequality applied to `(1.3)` gives

```text
sum_z |R(z)|^2 <=||c||_1^2 ||c||_2^2
                 <=|K| ||c||_2^4.                    (1.5)
```

Since centering only subtracts a nonnegative square from the uncentered
energy, `(1.4)--(1.5)` prove

```text
(1/p)sum_(a!=0)|S_Gamma(a)|^4
 <=|K| ||c||_2^4.                                     (1.6)
```

For flat unnormalized coefficients and `|K|=N`, this is `N^3`.  This is the
best possible bound using only graph support, carrier injectivity, and an
arbitrary carrier mask; Section 4 gives equality in power.

The physical defect-energy relation may instead be written after reindexing
the same matching by its carrier: `k=m(v)v^(-1)`.  Formulae `(1.3)--(1.6)`
are invariant under that relabelling and require no interval structure in
the denominator index.  They therefore give the same `N^3` ceiling when the
phase points are the defects whose additive energy is being counted.

Without carrier injectivity, even `(1.6)` fails: coefficients on equal
carriers first coalesce, and a constant carrier gives fourth moment of
order `p||c||_1^4` before division by `p`.

---

## 2. Where Yao's proof uses the Cartesian product

For the full sum

```text
S_M,X(a)=sum_(m in M,x in X)e_p(a m x^(-1)),           (2.1)
```

Yao decomposes the centered correlation into pairs `(x,y)`.  Because the
same numerator set `M` occurs for every `x` and `y`, the squared norm of one
piece is

```text
D_M(x/y)=E^+(M,(x/y)M)-M^4/p.                          (2.2)
```

The decisive input is then the common-set estimate

```text
sum_(lambda in Lambda)D_M(lambda)
 <=M^2(min(M,sqrt(p))^2+|Lambda|),                     (2.3)
```

coupled dyadically to the interval ratio multiplicities.  This produces

```text
sum_(a!=0)|S_M,X(a)|^4
 <<p H^2 M^2(H+min(M,sqrt(p)))^2 p^o(1).              (2.4)
```

These are precisely Lemma 2.3 and Theorem 1.1 of the primary source.

For graph coefficients, the numerator set in row `k` is the singleton
`{m(k)}` and varies with `k`.  The centered pair piece is now

```text
F_(k,l)(z)
 =c_k conjugate(c_l)
  [1_(z=v_k-v_l)-1/p],                                (2.5)

||F_(k,l)||_2^2
 =|c_k|^2 |c_l|^2(1-1/p).                             (2.6)
```

There is no common `D_M(lambda)` to which `(2.3)` can be applied.  Literal
pairwise Minkowski gives only

```text
[(1/p)sum_(a!=0)|S_Gamma(a)|^4]^(1/2)
 <=(1-1/p)^(1/2)||c||_1^2,                            (2.7)
```

or `N^4` for flat coefficients.  Retaining the locations of the atoms in
`(2.5)` and applying one global Young inequality improves `(2.7)` to the
sharp `N^3` bound `(1.6)`, but no further.  The precise surviving term is
the nonzero-difference additive energy of the selected carrier mask.

Thus the obstruction is not a forgotten zero-frequency diagonal.  Yao's
centering removes that diagonal exactly; it does not remove structured
correlations at nonzero carrier differences.

---

## 3. Completing the graph loses far more

One can enlarge `(1.1)` to the full Cartesian product

```text
M_Gamma x K,             M_Gamma={m(k):k in K}.        (3.1)
```

For nonnegative unit coefficients, graph energy is bounded by the
uncentered Cartesian energy.  Therefore Yao's theorem gives

```text
E_Gamma
 <=(|M_Gamma||K|)^4/p
   +H^2 M^2(H+M)^2 p^o(1),                            (3.2)
```

when `H=M=N<sqrt(p)`.  Hence

```text
E_Gamma <<N^8/p+N^6 p^o(1).                           (3.3)
```

At the project scale

```text
p=D^(33/16),             N=D,                         (3.4)
```

the two terms in `(3.3)` are

```text
D^(95/16)  and  D^6.                                  (3.5)
```

The centered theorem term `D^6` is larger by `D^(1/16)` and exceeds the
desired `D^(5/2)` by

```text
D^(7/2).                                               (3.6)
```

So positivity/completion cannot transfer Yao's Cartesian estimate to the
physical graph at the needed scale.

---

## 4. A faithful matching coefficient fixture

Take `s=1`, a prime `p`, and an integer `N` with `N^2<p`.  Let

```text
K={1,...,N},              m(k)=k^2,
M_Gamma={1^2,...,N^2}.                                  (4.1)
```

Then `(m(k),k)` is a matching between two `N`-element sets, and

```text
m(k)k^(-1)=k (mod p).                                  (4.2)
```

Thus the carrier mask is the injective interval `{1,...,N}`.  The graph
points

```text
(k,m(k),v_k)=(k,k^2,k)                                 (4.3)
```

have no three distinct collinear points: their projection to `(k,k^2)` is
a nondegenerate parabola.  Consequently graph matching and the elementary
three-point affine packet exclusion both hold.

Because `2N<p`, modular and integral additive energy agree.  Exactly

```text
E^+({1,...,N})=(2N^3+N)/3.                             (4.4)
```

Equation `(1.4)` therefore becomes

```text
(1/p)sum_(a!=0)|sum_(k<=N)e_p(ak)|^4
 =(2N^3+N)/3-N^4/p.                                   (4.5)
```

With `N=D=p^(16/33+o(1))`, the subtracted centered baseline is only

```text
N^4/p=D^(31/16),                                      (4.6)
```

whereas the nonzero-difference term is `D^(3+o(1))`.  Hence `(1.6)` is
sharp in power and misses `D^(5/2)` by exactly

```text
D^(1/2).                                               (4.7)
```

More explicitly, if `r(d)=N-|d|` for `|d|<N`, then

```text
sum_(d!=0)r(d)^2=(2N^3-3N^2+N)/3.                     (4.8)
```

This is the precise term surviving centering.

The fixture lies literally inside Yao's finite-field phase and satisfies
the requested graph, matching, interval-denominator, injective-carrier, and
no-three-collinear properties.  It does not satisfy the QP real product
windows or prime-power shell, so it only proves that those extra physical
conditions are indispensable.

---

## 5. Consequence for the final gate

There is no graph-/matching-weighted corollary of Yao's Theorem 1.1 that
uniformly reaches `D^(5/2)` for an arbitrary carrier mask.  In increasing
order of loss, the exact available ledgers are

```text
global graph centering + Young:       D^3, loss D^(1/2);
literal pairwise Yao/Minkowski:        D^4, loss D^(3/2);
completion to Yao's Cartesian box:     D^6, loss D^(7/2).              (5.1)
```

A successful `D^(5/2)` theorem must use the reciprocal product-band
rounding, the broad-rectangle mixed difference, or the actual post-peeling
carrier geometry before taking absolute values.  It cannot follow from
graph support, matching, interval ratio multiplicity, and additive-frequency
centering alone.

Exact finite identities and exponent arithmetic are replayed in
`src/qp_yao_graph_centering_gate.py` and
`src/test_qp_yao_graph_centering_gate.py`.

```text
weighted graph centering identity:                         PROVED;
best arbitrary injective-mask Cauchy/Young bound D^3:      PROVED SHARP;
Yao common-dilate-energy step survives graph restriction: NO;
Cartesian completion reaches D^(5/2):                     NO, D^6;
physical packet-free reciprocal energy D^(5/2):           OPEN.
```
