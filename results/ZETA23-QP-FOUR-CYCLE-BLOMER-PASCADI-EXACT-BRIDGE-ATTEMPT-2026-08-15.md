# QP four-cycle: exact Blomer--Pascadi bridge attempt

**Date:** 2026-08-15  
**Verdict:** additive completion does expose a classical Kloosterman kernel
exactly, but not with the two short separated frequency sequences required
by Blomer--Pascadi.  The native arbitrary prime/color mask has full additive
Fourier support.  A direct length-`D` block decomposition loses at least
`q^(17/66)` on one side, while the new theorem leaves room for only
`q^(1/352)`.  Therefore the direct bridge fails by a fixed power.

This is a precise obstruction to the naive completion, not a proof that no
more global arithmetic use of the new theorem is possible.  The four-cycle
bound remains open.

---

## 1. Exact variable-numerator inversion layers

Fix two actual rows `a_1,a_2`, a common carrier `b`, and its colors `c,d`.
Put

```text
Q=q^3,
r=8a_1bc-Q,
v=a_2d-a_1c.                                        (1.1)
```

The second residual is exactly

```text
r'=8a_2bd-Q=r+8bv.                                  (1.2)
```

Reducing (1.2) modulo `m=a_2` gives

```text
8bv == -Q-r (mod m).                                (1.3)
```

For an odd modulus and a unit shift `v`, define

```text
rho=r mod m,
lambda_rho=-(Q+rho)*inverse(8) mod m.               (1.4)
```

Then every common edge in residual class `rho` lies on the exact modular
inversion graph

```text
b == lambda_rho*inverse(v) (mod m).                 (1.5)
```

For a prime row modulus, every nonzero `|v|<m` is a unit.  For a prime-power
row, nonunit shifts form an additional sector not covered by the coprime
version of the bilinear theorem.

The all-prime `q=50021`, determinant-six fixture replays (1.3)--(1.5)
exactly; with the convention (1.1), its first carrier has `v=-42`.

---

## 2. The fixed-layer Fourier transform really is Kloosterman

For a fixed unit `lambda mod m`, let

```text
T_lambda(f,g)=sum_(x mod m)^* f(x)g(lambda*inverse(x)). (2.1)
```

With the unnormalized additive Fourier transform

```text
f_hat(h)=sum_(x mod m) f(x)e_m(-hx),                (2.2)
```

double Fourier inversion gives the exact identity

```text
T_lambda(f,g)
 =m^(-2) sum_(h,n mod m) f_hat(h)g_hat(n)
             S(h,n*lambda;m),                      (2.3)
```

where

```text
S(h,n;m)=sum_(x mod m)^* e_m(hx+n*inverse(x)).      (2.4)
```

Thus the new paper is not merely analogous to the carrier graph: its kernel
is exactly the double Fourier transform of each fixed residual layer.

If `f_hat` and `g_hat` were supported in intervals of length
`D=q^(16/33)`, Blomer--Pascadi would save `q^(19/1056-o(1))`, enough to
clear the `1/66` numerical shortfall with margin `1/352`.

---

## 3. Why the theorem's interval hypothesis is not present

The interval variables in Blomer--Pascadi are `h,n` in (2.3), not the
physical carrier and shift variables `x,lambda*inverse(x)`.  The native
weights contain:

* the prime-power indicator of the carrier;
* the arbitrary factors `conjugate(z_c)z_d`;
* the smooth cubic residual weight;
* the restriction to the actual residual class `rho`.

Even on one inversion layer these combine into an arbitrary function of
the physical edge.  Pair uniqueness lets a sparse `z` select a single edge.
A physical point mass has

```text
|f_hat(h)|=1                       for every h mod m. (3.1)
```

It therefore has no short additive frequency support at all.

This is not repaired by the fact that `|v|<<D`.  A smooth physical interval
of length `D` has natural dual width `m/D`, while an arbitrary prime/`z`
mask can occupy the entire dual group.  The residual numerator also varies:
the row-pair graph is a union over `rho` of (1.5), not one fixed
`lambda`-layer.

---

## 4. Exact loss of the direct block decomposition

Split all `m` frequencies of the point mass (3.1) into consecutive blocks
of length at most `D`.  There are at least

```text
R=ceil(m/D)                                           (4.1)
```

blocks.  Their `ell^2` norms are `sqrt(|I_j|)`, so applying a short-interval
bilinear estimate blockwise costs, on just one unrestricted side,

```text
(sum_j sqrt(|I_j|))/sqrt(m) >=sqrt(m/D)              (4.2)
```

up to the harmless final partial block.  At the active scale `m asymp q`,

```text
R=q^(17/33+o(1)),
one-side loss=q^(17/66+o(1)).                        (4.3)
```

If both Fourier sequences are unrestricted, the analogous product loss is
`q^(17/33+o(1))`.  By comparison,

```text
BP saving=19/1056,
needed square-root gain=1/66,
allowed bridge loss=19/1056-1/66=1/352.             (4.4)
```

The one-side block loss exceeds the allowance by

```text
17/66-1/352=269/1056.                               (4.5)
```

This loss is forced already by one legal coefficient pattern; it is not an
artifact of a loose divisor estimate.

### 4.1 Sparse/diffuse weights do not remove the block gate

The point mass is not the only coefficient pattern with the loss (4.2).
For a physical layer weight `f` on `Z/mZ`, write

```text
B_D(f)=sum_(frequency blocks I, |I|<=D)||f_hat||_(2,I)
       /(sqrt(m)*||f||_2).                          (4.6)
```

Always `B_D(f)<=sqrt(ceil(m/D))`.  There is no improving upper bound in
terms of physical support or participation alone, even for nonnegative
weights.  An exact example is supplied by a prime `m==3 (mod 4)`.  Let `Q`
be its nonzero quadratic residues, `k=(m-1)/2`, and put

```text
f_theta(0)=sqrt(theta),
f_theta(x)=sqrt((1-theta)/k)  for x in Q,
f_theta(x)=0                  otherwise.            (4.7)
```

Then `||f_theta||_2=1` and

```text
M_4(f_theta)
 =[theta^2+(1-theta)^2/k]^(-1).                    (4.8)
```

As `theta` varies, (4.8) ranges from the atomic scale to a constant
proportion of `m`.  Since the quadratic Gauss sum is purely imaginary, for
every nonzero frequency `h`

```text
|f_theta_hat(h)|^2
 =(sqrt(theta)-.5*sqrt((1-theta)/k))^2
   +m*(1-theta)/(4k).                              (4.9)
```

This is bounded below by an absolute constant uniformly in `theta` and
`m>=7` (split into `theta<=1/2` and `theta>1/2`).  Every nonzero full block
therefore has norm `>>sqrt(D)`, and

```text
B_D(f_theta)>>sqrt(m/D)=q^(17/66+o(1)).            (4.10)
```

Thus removing atomic physical weights does not improve the exponent of the
direct block bridge.  This is a coefficient-class obstruction; (4.7) is not
asserted to be an actual prime-power carrier mask.

There is a still more direct obstruction to using the **global**
participation of `z`.  Take `L` disjoint color pairs in `L` different
residual layers and put `z` flat on their `2L` colors.  Then

```text
M_4(z)=2L,
each residual-layer physical weight is one point mass. (4.11)
```

This respects the matching/pair-uniqueness architecture.  Hence restriction
to a layer can collapse arbitrarily large global participation to one;
controlling (4.11) requires a new square-function theorem across layers.
No such theorem is part of Blomer--Pascadi.

The existing combinatorial bounds make the remaining range explicit.  For
unit `z`, the proved diffuse estimate is

```text
Q_nd(z)<<D+D^3/M_4(z),                             (4.12)
```

so `M_4(z)>=D^2*q^(-o(1))` is already closed without BP.  For a roughly
uniform literal support of size `M`, the degree bounds give

```text
Q_nd(z)<<D+
 {D*M,       M<=D,
  D^3/M,     D<=M<=D^2}.                           (4.13)
```

Consequently (4.13) reaches `D*q^o(1)` only for subpolynomial support or
for `M>=D^2*q^(-o(1))`.  In `q`-powers, writing `M=q^mu`, the unresolved
roughly uniform interval is exactly

```text
0<mu<32/33,                                        (4.14)
```

with a change of formula at `mu=16/33`.  The block loss (4.10) is present
throughout this interval and exceeds the BP allowance by `269/1056`, so the
direct bridge does not shrink (4.14).

There is one additional rigorous atomic endpoint.  Let `tau_3` be the
`ell^2` mass of `z` outside its three largest coordinates.  The retained
all-distinct quartic vanishes on three colors.  Symmetrize its positive
four-linear tensor and polarize the proved global bound
`Q_nd<<D^(21/16)q^o||z||_2^4`.  Every surviving term in the expansion
`z=z_top3+z_tail` contains a tail factor, whence

```text
Q_nd(z)<<D^(21/16)q^o*sqrt(tau_3).                 (4.15)
```

(The polarization constant is absolute: expand the diagonal polynomial of
the sum of four normalized nonnegative inputs.)  Therefore

```text
tau_3<=D^(-5/8)                                    (4.16)
```

is closed.  Equations (4.12) and (4.16), together with the separately
proved subpolynomial-support, repeated, and projectively sparse sectors,
still leave arbitrary vectors satisfying

```text
M_4(z)<D^2*q^(-o(1)),       tau_3>D^(-5/8),        (4.17)
```

and having polynomial near-parallel clusters.  A four-color or other
fixed-size **global** packet is closed combinatorially.  The obstruction is
that a point-mass physical layer can occur as one of polynomially many
layers of a globally intermediate-support vector, as in (4.11).  It is that
aggregation, not the isolated packet, which remains open.

---

## 5. Precise remaining bridge

The direct delta/Fourier route cannot feed the QP row-pair Gram into
Theorem 1.1 coefficient-uniformly.  A successful use of Blomer--Pascadi
would need an additional theorem that does at least one of the following:

1. proves additive-frequency concentration of the **aggregate** actual
   prime/color coefficient after the sparse and repeated sectors are removed;
2. obtains square-summable cancellation across frequency blocks and across
   the variable residual parameters `lambda_rho`, avoiding (4.2);
3. reorganizes the global rank-one four-cycle sum into short Kloosterman
   arguments before taking absolute values.

Any such reorganization may lose at most `q^(1/352-o(1))` if it uses only
the dominant term of the present Blomer--Pascadi bound.

```text
fixed residual class => modular inversion graph:     PROVED;
double Fourier transform => classical S(h,n;m):      PROVED;
BP exponent clears numerical 1/66 gap:               PROVED;
native coefficients short in h and n:                FALSE;
direct block bridge within q^(1/352):                 FALSE;
global block/residual orthogonality theorem:          OPEN;
global `M_4` controls residual-layer participation:  FALSE;
three-atom tail `tau_3<=D^(-5/8)`:                  PROVED;
weighted sparse/diffuse split closes all supports:    NO;
four-cycle bound (FC):                                OPEN.
```

Finite replay:

```bash
PYTHONPATH=src python3 -m pytest -q \
  src/test_qp_four_cycle_bp_bridge.py
```
