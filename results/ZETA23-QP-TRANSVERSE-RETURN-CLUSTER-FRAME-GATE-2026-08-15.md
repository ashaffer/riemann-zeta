# QP transverse return: actual-node polynomial floor and the dimension barrier

**Date:** 2026-08-15  
**Verdict:** the near-reflection collisions of the actual absolute-log nodes
can be quotiented rigorously.  A smooth full-band mean-square argument then
proves the unconditional bounds

```text
s_v >>_w 1/M_Y >>_w (log Y)/Y,                       (0.1)
r_+(H_Y;S_Y) >>_w 1/M_Y >>_w (log Y)/Y,              (0.2)
```

where `M_Y` is the number of distinct prime-power nodes in the shell.  The
first estimate holds for every calibrated residual

```text
v=a(t_0)+D q_0,       0<D<=1,       0<=t_0<=Y^A.    (0.3)
```

Thus the transverse ray is always feasible: the exact obstruction is not
nonreturn.  It is the size of the return.  At the strip-relevant event
`D>=Y^(-d+o(1))`, (0.1) and exact transverse mixing give only
`r_Y>>Y^(-1-d+o(1))`, and (0.2) itself gives only exponent one.  Neither
reaches `LTRAD_full(c,d)` when `c-d` is small.

The `1/M_Y` scale is not an artifact of ignoring the long prime interval.
An explicit fixed-shell harmonic model has a contiguous block of
`asymp N/log N` nodes equal to `-1` at one legal height, while its calibrated
transverse depth is at most `C/M`.  It is not an actual-prime counterexample,
but it proves that cardinality, separation, a long negative block, ordinary
mean square, and higher moments cannot improve (0.1).  Any improvement on
the actual primes must exclude a small Fejer hard core by genuinely
coefficient-sensitive arithmetic.

No fixed-power QP upper bound, `LTRAD_full` at the required exponents,
QP-to-strip implication, or zero-free strip is proved here.

**Subsequent improvement.**  The dimension-only scale in this report is not
the final actual-node floor.  Integer-product fourth moments improve it to
`s_v,r_+>=Y^(-49/66-o(1))` at `A=50/33`; see
`ZETA23-QP-TRANSVERSE-FOURTH-MOMENT-AND-ACTUAL-UPPER-GATE-2026-08-15.md`.
The Fejer model below remains sharp for the support/spacing hypotheses used
here, but it is not compatible with that additional integer-product input.

---

## 1. Setup and the collision that must be retained

Fix `w>0`, a half-integer `Y`, and

```text
S_Y={n=p^k:Y exp(-w)<n<Y exp(w)},
u_n=|log(n/Y)|,
a(t)=(cos(tu_n))_(n in S_Y),
q_0=(1,...,1),
H_Y=[Y^a,Y^A],                 A>1.                 (1.1)
```

Repeated absolute nodes are merged, and `M_Y` denotes the resulting
dimension.  In fact the half-integer convention rules out a cross-side
equality: if `n<Y<m` and `u_n=u_m`, then `nm=Y^2`, impossible because `nm`
is an integer and `Y^2` has fractional part `1/4`.

There are three elementary spacing facts.  With constants depending only
on `w`,

```text
min_n u_n >=c_w/Y,                                  (1.2)
|u_n-u_m|>=c_w/Y       if n,m lie on the same side, (1.3)
|u_n-u_m|>=c_w/Y^2     for all distinct n,m.        (1.4)
```

For (1.2), use `|n-Y|>=1/2` and the mean value theorem.  Formula (1.3)
follows from `|log(n/m)|>>_w |n-m|/Y`.  For opposite sides,

```text
|u_n-u_m|=|log(nm/Y^2)|,
|nm-Y^2|>=1/4,                                      (1.5)
```

which proves (1.4).

The ordinary Montgomery--Vaughan inequality cannot use (1.4): the full
band has length `Y^A` with `A<2` in the project.  But (1.3) is stronger.
The positive frequencies are the union of two `c_w/Y`-separated families,
one from each side of `Y`.  Consequently every cluster at scale
`c_w/(10Y)` has size at most two.  These are precisely the possible
near-reflection pairs.  Their difference coordinate is small, but the
target vector (0.3) has the same smoothness in the node variable.  The next
lemma keeps that coordinate instead of discarding it.

---

## 2. Smooth clustered frame lemma

Put `B=Y^A`.  Choose once and for all a nonnegative smooth probability
`psi` supported in `(1/3,2/3)`, positive on a smaller interval.  Define

```text
rho_B(t)=B^(-1)psi(t/B).                             (2.1)
```

For large `Y`, its support lies in `H_Y`.

### Lemma 2.1 (two-cluster frame and leverage)

Let `u_1,...,u_M` satisfy (1.2)--(1.3), with the nodes split into their two
sides of `Y`, and put

```text
F_y(t)=sum_j y_j cos(tu_j).                          (2.2)
```

There is a positive quadratic form `E_Y(y)` such that, uniformly in real
`y`,

```text
c_w E_Y(y)<=int F_y(t)^2 rho_B(t)dt<=C_w E_Y(y),    (2.3)
|F_y(t)|<=C_w sqrt(M) E_Y(y)^(1/2)   (0<=t<=B),     (2.4)
|int F_y(t)rho_B(t)dt|
 <=C_(w,K)sqrt(M)(Y/B)^K E_Y(y)^(1/2)               (2.5)
```

for every fixed `K`.

#### Proof

Order the positive frequencies and join consecutive frequencies whose gap
is less than `c_w/(10Y)`.  By (1.3), no component has three vertices.
Distinct components are `c_w/Y`-separated after a harmless change of the
constant.  Do the same to the signed frequencies `+/-u_j`; (1.2) prevents a
positive-negative cluster.

For a singleton, use its ordinary coefficient.  For a pair with
frequencies `xi_1,xi_2`, coefficients `c_1,c_2`, and

```text
z=B|xi_1-xi_2|,
p=c_1+c_2,
q=min(1,z)(c_1-c_2),                                (2.6)
```

use `|p|^2+|q|^2` as its block energy.  The sum of these block energies,
restricted to the conjugate-symmetric coefficients which represent the
real cosine sum, is `E_Y(y)`.

After scaling `t=Bx`, the diagonal two-point Gram matrix has off-diagonal
entry

```text
hat psi(z)=int psi(x)exp(izx)dx.                     (2.7)
```

Because `psi` has nonzero variance,

```text
1-|hat psi(z)| asyp z^2        (0<=z<=1),            (2.8)
sup_(z>=1)|hat psi(z)|<1.                            (2.9)
```

The second assertion follows from strictness in the triangle inequality on
an interval and rapid decay at infinity.  Hence the two eigenvalues of the
block Gram matrix are uniformly equivalent to the two terms in (2.6).  One
minor phase point is worth making explicit because `psi` need not be
symmetric.  For `z<=1`, after removing the common modulation, the pair is

```text
p cos(zx/2)+i(c_1-c_2)sin(zx/2).                    (2.9a)
```

In the variables `(p,z(c_1-c_2))` this converges uniformly to
`p+i z(c_1-c_2)x/2`.  Its two-by-two Gram determinant is a positive
multiple of `Var_psi(x)`.  Compactness for `0<=z<=1` therefore gives the
claimed equivalence even though `hat psi(z)` is complex; for `z>=1`, (2.9)
and compactness away from zero apply directly.
For completeness, `hat psi(z)` need not be real, so the last statement is
not an assertion that `p,q` are its literal eigenvectors.  When `0<=z<=1`,
the block itself is

```text
p cos(zx/2)+i(c_1-c_2)sin(zx/2).                    (2.9a)
```

In the variables `(p,r)`, `r=z(c_1-c_2)`, this converges at `z=0` to
`p+i r x/2`.  Its limiting two-dimensional Gram matrix is positive definite
because `psi` has positive variance.  Compactness for `0<=z<=1` gives the
claimed equivalence to `|p|^2+|r|^2`; for `z>=1`, (2.9) gives it directly.
This also handles the harmless phase rotation in the exact Gram eigenvectors.

Different blocks are separated by `>>B/Y` in the scaled frequency.  Every
derivative of `hat psi` is rapidly decreasing.  If a block uses a divided
difference, the factor `min(1,z)` in (2.6) is canceled by the corresponding
first or second difference of `hat psi`.  The absolute row sum of all
off-block Gram entries is therefore

```text
<<_(w,K) sum_(m>=1)(1+mB/Y)^(-K)=o_w(1).             (2.10)
```

Taking `K>=2`, the block Gram comparison and (2.10) prove (2.3).

For (2.4), a pair contributes

```text
exp(i(xi_1+xi_2)t/2)
 [p cos((xi_1-xi_2)t/2)
  +i(c_1-c_2)sin((xi_1-xi_2)t/2)].                  (2.11)
```

For `0<=t<=B`, its modulus is `O(|p|+|q|)`.  Sum over at
most `M` blocks and apply Cauchy--Schwarz.

Finally, `Bu_j>>B/Y`, so rapid decay gives

```text
|hat psi(Bu_j)|<<_(w,K)(Y/B)^K.                     (2.12)
```

For a close pair, the first difference in (2.12), divided by `z`, is a
derivative of `hat psi` at an argument `>>B/Y` and obeys the same bound.
For `z>=1`, use (2.12) separately.  Cauchy--Schwarz over the blocks proves
(2.5).  QED

This is the precise resolution of the cross-side collision issue.  Replacing
the two close nodes by one node would lose the difference coordinate; using
the scaled divided difference retains it with a uniform Gram constant.

---

## 3. A positive-range inequality for every signed dual

Let

```text
Q=int F_y(t)^2rho_B(t)dt,
m=int F_y(t)rho_B(t)dt,
h_0=sup_(t in supp rho_B)F_y(t),
h=sup_(t in H_Y)F_y(t)>=h_0.                         (3.1)
```

The number of prime powers in a fixed multiplicative shell satisfies

```text
M_Y<<_w Y/log Y.                                    (3.2)
```

Indeed the primes contribute `O(Y/log Y)` by Chebyshev, and the proper
prime powers contribute `O(sqrt(Y)log Y)`.

Choose `K` in (2.5) so that

```text
M_Y(Y/B)^K=o(1).                                    (3.3)
```

At the project value `A=50/33`, `K=3` already gives
`Y(Y/B)^3=Y^(-18/33)`.  Lemma 2.1 then implies

```text
|m|<=o(M_Y^(-1/2))Q^(1/2),
U:=sup_(supp rho_B)|F_y|<=C sqrt(M_Y)Q^(1/2).        (3.4)
```

For every real `x` in `[-U,h_0]`,

```text
(h_0-x)(U+x)>=0,
x^2<=h_0 U+(h_0-U)x.                                (3.5)
```

Average (3.5) against `rho_B`.  By (3.4), for all sufficiently large `Y`,

```text
Q<=h_0 U+(U-h_0)|m|=h_0(U-|m|)+U|m|,
U|m|<=Q/2.                                          (3.6)
```

Here `h_0<=U`, and the first inequality is valid for either sign of `m`.
Since `U>|m|`, (3.6) first proves `h_0>0` and then gives

```text
h>=h_0>=(Q-U|m|)/(U-|m|)>=Q/(2U)
 >=c_w Q^(1/2)/sqrt(M_Y)
  >=c_w E_Y(y)^(1/2)/sqrt(M_Y).                     (3.7)
```

This extends the canonical-positive-return argument to **every signed
dual**.  The price is exactly the square root of the dimension in (3.7).
Combining it with the point-evaluation price in (2.4) produces `1/M_Y`.

---

## 4. The actual transverse ray always returns

Fix `0<=t_0<=Y^A`, `0<D<=1`, and

```text
v=a(t_0)+Dq_0,
P_Y=conv{a(t):t in H_Y},
s_v=sup{s>=0:-sv in P_Y}.                           (4.1)
```

### Theorem 4.1 (actual-node transverse polynomial floor)

For every sufficiently large half-integer center `Y`,

```text
s_v>=c_w/M_Y>>_w(log Y)/Y.                          (4.2)
```

#### Proof

For a dual vector `y`, write `F=F_y`.  Lemma 2.1 gives

```text
|y dot v|=|F(t_0)+D F(0)|
 <=C_w sqrt(M_Y)E_Y(y)^(1/2).                       (4.3)
```

Together with (3.7), this yields

```text
h_Y(y):=sup_(t in H_Y)y dot a(t)
 >=(c_w/M_Y)[-y dot v]                              (4.4)
```

whenever `y dot v<0`.  If `y dot v>=0`, the right side in the support
inequality for `-(c_w/M_Y)v` is nonpositive, while (3.7) gives
`h_Y(y)>=0`.  Hence, for every `y`,

```text
y dot[-(c_w/M_Y)v]<=h_Y(y).                         (4.5)
```

The support-function characterization of the compact convex set `P_Y`
places `-(c_w/M_Y)v` in `P_Y`.  This proves (4.2), including feasibility of
the ray.  QED

The proof does not use the calibrated identity `lambda dot v=0`; it applies
to every vector (0.3).  In particular it applies to the residual selected
by a long negative prime interval.

### Corollary 4.2 (unconditional actual-node radial floor)

The same argument with `v=q_0` gives

```text
r_+(H_Y;S_Y)>=c_w/M_Y>>_w(log Y)/Y.                 (4.6)
```

This is a lower bound on the antipode radius, not the QP upper bound sought
elsewhere.  It is compatible with the unconditional Vinogradov--Korobov
upper bound, which is much larger than `Y^-1`.

For a threshold event, exact transverse mixing now yields

```text
r_Y>=D s_v/(1+s_v)>>D/M_Y.                          (4.7)
```

Since `D>=Y^(-d+o(1))`, this is only

```text
r_Y>>Y^(-1-d+o(1)).                                 (4.8)
```

The unconditional floor (4.6) is actually stronger than (4.8).  Therefore
Theorem 4.1 proves a binary fact about the missing ray but does not prove the
strip-relevant estimate `s_v>=Y^(-(c-d)+o(1))`.

---

## 5. The `1/M` loss is sharp for dimension-only methods

The following model retains the features used above and also has a long
contiguous negative block.  Let `m asyp N/log N` and take

```text
Delta=w/(10m).                                       (5.1)
```

Put the hard nodes

```text
u_j=j Delta,                  1<=j<m,               (5.2)
```

in `(0,w/10)`.  In the disjoint interval `(3w/10,2w/5)` take the `m`
consecutive half-mesh nodes

```text
e_k=(k+1/2)Delta,              3m<=k<4m.            (5.3)
```

The total dimension is `M=2m-1 asyp N/log N`.  Extra half-mesh nodes may be
inserted in the unused shell regions without changing the argument.  At

```text
t_0=2pi/Delta asyp M,                               (5.4)
```

every hard node has cosine `+1` and every easy node has cosine `-1`.
Thus the easy nodes form a contiguous interval of prime-shell cardinality,
its uniform probability has `D=1`, and its `N`-normalized negative mass is
`asymp1/log N>>N^-d`.  The height (5.3) lies in the project Turan band for
every fixed `A'>1`.

Let

```text
K_m(x)=1+2 sum_(j=1)^(m-1)(1-j/m)cos(jx)>=0         (5.5)
```

be the Fejer kernel and use the dual polynomial

```text
F(t)=[1-K_m(Delta t)]/[2(m-1)].                     (5.6)
```

Its coefficients are supported only on the hard nodes.  For the calibrated
residual `v=a(t_0)+q_0`, `v=2` on the hard block and `v=0` on the easy block.
Moreover,

```text
F(0)=-1/2,
y dot v=2F(0)=-1,
sup_(t in R)F(t)<=1/[2(m-1)].                       (5.7)
```

The transverse dual formula therefore gives

```text
s_v<=1/[2(m-1)]<<1/M.                               (5.8)
```

This is not an actual-prime-log construction.  It is an exact
method-scoped obstruction: even shell support, prime-sized mesh and
cardinality, a legal common height, and a full long negative interval do not
beat `1/M`.  In particular, the model is itself a union of two
`>>1/N`-separated families, so it satisfies the clustered geometry used in
Lemma 2.1 and shows that theorem's dimension loss is sharp.  Perturbing it
through the full aperture requires accuracy
`o((MY^A)^-1)`, so it cannot be transferred to actual primes at their
available mesh.

Higher moments do not remove this barrier.  Replacing the two
`sqrt(M)` losses in Sections 3--4 by their `L^p` Nikolskii analogues merely
redistributes the same total factor `M`; the Fejer model (5.5)--(5.8)
saturates the resulting range asymmetry.  To improve (4.2) on the actual
nodes one must prove that no adaptive small prime-power hard core can carry
the separating polynomial while the natural long prime block supplies the
negative event.  That is arithmetic information not contained in an
ordinary Hilbert, Gram, or moment estimate.

---

## 6. Binary disposition

```text
cross-side Y^-2 collisions ignored:                 INVALID;
cross-side collisions quotiented as two-clusters:   PROVED;
all-signed-dual positive return:                     PROVED;
actual transverse-ray feasibility:                  PROVED;
s_v >>1/M_Y>>(log Y)/Y:                             PROVED;
actual radial floor r_+>>1/M_Y:                     PROVED;
dimension-only improvement beyond 1/M:              FALSE;
actual-prime improvement beyond 1/M:                PROVED (to 49/66);
strip-scale LTRAD_full(c,d):                         OPEN;
QP upper bound, QP-to-strip, or uniform strip:       NOT PROVED.
```
