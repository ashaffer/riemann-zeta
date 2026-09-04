# QP actual-node Fejer transfer: an arithmetic rigidity ceiling

**Date:** 2026-08-15  
**Verdict:** a nodewise perturbative transfer of the harmonic Fejer hard
core to the actual prime-power logarithms cannot use more than

```text
L << Y^2/B.                                             (0.1)
```

Here `B` is the top of the time aperture and `L` is the Fejer support
length.  At the project aperture `B=Y^(50/33)`, this ceiling is

```text
L << Y^(16/33),       16/33=.48484848... .             (0.2)
```

Consequently the standard Lipschitz-stable harmonic transfer cannot certify
a Fejer floor smaller than `Y^(-16/33)` (up to constants).  This is just
short of the `M^(-1/2)=Y^(-1/2+o(1))` scale suggested by the finite
transverse experiments.

This is a **method-scoped obstruction**.  It does not construct an actual
Fejer core of length `Y^(16/33)`, prove an upper or lower bound of that size
for `s_v`, refute a nonperturbative actual-node certificate, or prove or
refute QP or a strip.

---

## 1. Actual nodes cannot shadow a long log arithmetic progression too well

Fix a half-integer `Y=N+1/2` and

```text
0<w<(log 2)/2,
S_Y={n=p^a:Y exp(-w)<n<Y exp(w)},
u_n=|log(n/Y)|.                                      (1.1)
```

Take `L` distinct elements `n_1,...,n_L` of `S_Y`, in any order, and try to
match their absolute logarithms to the harmonic progression

```text
u_(n_j)=j h+e_j,             1<=j<=L.                (1.2)
```

Use the normalized triangular Fejer weights

```text
lambda_j=2(L+1-j)/[L(L+1)].                           (1.3)
```

### Theorem 1.1 (weighted actual-log AP rigidity)

For every `L>=36`, every injective matching (1.2) satisfies

```text
sum_(j<=L) lambda_j |e_j|
 >=exp(-2w)/(72Y^2).                                  (1.4)
```

#### Proof

Color the index `j` according as `n_j<Y` or `n_j>Y`; equality is impossible
because `Y` is a half-integer.  Partition the first
`floor(L/2)` indices into disjoint consecutive blocks of nine.  The identity

```text
W(2,3)=9                                               (1.5)
```

means that every such block contains a nonconstant monochromatic
three-term arithmetic progression of indices

```text
i, k, 2k-i.                                           (1.6)
```

All three corresponding integers lie on the same side of `Y`.  Therefore
their absolute centered logarithms have one common sign, and

```text
|u_(n_i)-2u_(n_k)+u_(n_(2k-i))|
 =|log[n_i n_(2k-i)/n_k^2]|.                         (1.7)
```

Because `exp(2w)<2`, the shell contains at most one power of each prime
base.  The three distinct prime powers in (1.7) consequently have distinct
prime bases.  Unique factorization gives

```text
n_i n_(2k-i) != n_k^2.                                (1.8)
```

Both integers in the ratio in (1.7) are at most `Y^2 exp(2w)`.  Since their
difference is a nonzero integer,

```text
|log[n_i n_(2k-i)/n_k^2]|
 >=exp(-2w)/Y^2.                                      (1.9)
```

The progression part `jh` has zero second difference, so (1.2) and (1.9)
give, in every nine-block,

```text
|e_i|+2|e_k|+|e_(2k-i)| >=exp(-2w)/Y^2.              (1.10)
```

Thus the unweighted error sum in that block is at least
`exp(-2w)/(2Y^2)`.  There are at least `L/36` disjoint blocks.  Moreover, for every
`j<=floor(L/2)`, (1.3) gives `lambda_j>=1/L`.  Summing (1.10) over the
blocks proves (1.4).  QED

The proof permits an arbitrary matching and arbitrary interlacing of the
two shell sides.  The nine-point coloring step is what prevents alternating
the lower and upper nodes from evading integer rigidity.

---

## 2. Consequence for Lipschitz-stable Fejer transfer

For the exact progression, the Fejer identity is

```text
P_0(t):=sum_(j=1)^L lambda_j cos(t jh)
       =[F_(L+1)(th)-1]/L >=-1/L,                    (2.1)
```

where `F_(L+1)>=0` is the usual Fejer kernel.  For the matched actual nodes,
put

```text
P_u(t)=sum_(j=1)^L lambda_j cos(tu_(n_j)),
E=sum_(j=1)^L lambda_j|e_j|.                          (2.2)
```

The standard perturbative transfer uses only

```text
|P_u(t)-P_0(t)| <=tE <=BE              (0<=t<=B).    (2.3)
```

To retain an absolute-constant multiple of the Fejer floor through the
whole aperture, this proof requires

```text
BE <=C/L                                               (2.4)
```

for an absolute constant `C`.  Theorem 1.1 makes (2.4) possible only if

```text
L <=72C exp(2w)Y^2/B.                                 (2.5)
```

This proves (0.1).  With `B=Y^A`, the best floor scale accessible to this
specific argument is no smaller than

```text
1/L >>Y^(-(2-A)).                                     (2.6)
```

At `A=50/33`, (2.6) has exponent `16/33`.

Equation (2.3) is an upper error estimate, not an equality.  Therefore
(2.5) is a necessary condition for the **Lipschitz-budget proof**, not a
theorem that the perturbed cosine polynomial itself must fail when
`L>>Y^2/B`.  Cancellation among the perturbation errors, a nonharmonic
positive construction, or a genuinely signed transverse dual remains
outside this gate.

---

## 3. Relation to the transverse upper problem

A positive antenna with floor `epsilon` can give

```text
s_v <=epsilon/[D+P(t_0)]                              (3.1)
```

when the denominator is positive.  An exact `L`-term harmonic Fejer core
would have `epsilon=1/L`.  Theorem 1.1 shows why simply moving such a core
onto the actual prime-power logs cannot be justified at `L` near
`sqrt(M_Y)` by a worst-case nodewise Lipschitz estimate: the required
accuracy crosses the integer `Y^-2` rigidity scale exactly at
`L about Y^2/B`.

No existence statement is hidden here.  In particular:

```text
actual fixed-power upper for a legal residual:       NOT PROVED;
actual harmonic core of length Y^(16/33):            NOT CONSTRUCTED;
perturbative Fejer support beyond Y^2/B:              CLOSED;
nonperturbative or signed actual-node upper:          OPEN;
QP, LTRAD_full, or a uniform strip:                   NOT PROVED.
```

The exact coloring and exponent ledgers are replayed by
`src/qp_actual_fejer_rigidity_gate.py` and
`src/test_qp_actual_fejer_rigidity_gate.py`.
