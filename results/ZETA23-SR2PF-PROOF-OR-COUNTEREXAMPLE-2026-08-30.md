# SR2PF proof-or-counterexample audit

**Date:** 2026-08-30  
**Status:** broad matrix SR2PF remains open; the tensor-labelled theorem needed
by the digit-box application is proved; no zero-free strip and no proof of RH

## 0. Verdict

The proposed matrix theorem

```text
SR2PF:
  P=(p_ij) consists of pairwise-distinct primes p_ij asyp Y,
  rank_Q(P)<=2,
  |p_ij-x_i z_j|<<Y/B,             B=Y^(50/33);
  prove min(#rows,#columns)<=polylog(Y)
```

was not proved and was not refuted.  The stronger-looking but more structured
theorem actually supplied by the digit box **is** proved: retain the separated
product reference `Y exp(sum_j s_j omega_j)` of the cleaned construction and
the compatible rank-at-most-two condition under every bipartition.  Then

```text
r << log(Y)/log log(Y)                                (0.1)
```

for a binary `r`-mode restriction.  This contradicts the cleaned construction,
which has `r=(.0179+o(1))log(Y)/log log log(Y)`.  The distinction is important:
one arbitrary matrix flattening loses the compatibility that proves the
tensor theorem.

The run makes four substantial corrections.

1. For the broad matrix statement, an exact Schur--Pluecker reduction and a
   two-sided projective larger sieve give

   ```text
   min(#rows,#columns) << Y^(4/33+o(1)).              (0.2)
   ```

   This improves the elementary `Y^(8/33)` bound, but it is still much larger
   than the cleaned target `Y^(.00895-o(1))`.

2. A single matrix flattening was the wrong abstraction.  The actual digit-box
   transport has rank at most two under **every** bipartition.  The cubic
   flattening theorem of Landsberg--Manivel and Raicu therefore places the
   complete tensor on the second secant variety of a Segre variety.  There are
   two algebraic branches: an honest sum of two product tensors and a
   tangent/W degeneration.

3. The entire rational tangent/W branch can be excluded at the required
   dimension.  A p-adic disjoint-support lemma plus determinant-height
   factorial growth gives

   ```text
   r << log(Y)/log log(Y),                             (0.3)
   ```

   whereas the cleaned digit tensor needs

   ```text
   r=(.0179+o(1)) log(Y)/log log log(Y).               (0.4)
   ```

4. The honest-secant branch, including a quadratic-conjugate pair, is also
   excluded.  Its face minors form a bounded integer multiplicative orbit.
   There are only `O(log Y/log log Y)` distinct orbit ratios.  Grouping equal
   ratios produces exponentially many distinct prime traces with one fixed
   rational norm, while a uniform Pell/divisor argument permits only
   `exp(O(log Y/log log Y))` such traces.  This proves `(0.1)`.

Thus the run does **not** prove broad matrix SR2PF, but it proves the faithful
all-cut version and closes the finite algebraic obstruction for the cleaned
digit tensor.  This is not by itself a zero-free strip: the upstream analytic
transport into this exact tensor alternative remains a separate dependency.

Finite algebra and exponent checks are replayed by

```bash
python3 results/verify_zeta23_sr2pf.py
```

## 1. Frozen scales

Put

```text
epsilon=Y/B=Y^(-17/33),
H=Y epsilon=Y^2/B=Y^(16/33).                          (1.1)
```

All implied constants below may depend on the fixed shell constants and on
the fixed constant in the approximation, but not on `Y` or the dimensions.

For any two rows and columns, writing `p_ij=x_i z_j+e_ij` gives

```text
|p_ij p_kl-p_il p_kj| << Y epsilon = H.               (1.2)
```

The minor is nonzero: equality would equate two products of four globally
distinct primes, contrary to unique factorization.  In particular the matrix
has rank exactly two, not one.

## 2. What broad matrix SR2PF actually yields

### 2.1 Exact Schur normal form

Fix `p=p_00` and set

```text
d_ij=p p_ij-p_i0 p_0j.                                (2.1)
```

The Schur-complement rank formula and `rank(P)=2` imply that `(d_ij)` has rank
one.  It is an integer matrix with no zero entry, so there are nonzero integer
vectors `a_i,b_j` and a nonzero integer content `g` such that

```text
d_ij=g a_i b_j,             |g a_i b_j|<<H.           (2.2)
```

Modulo `p`, no factor in `(2.2)` vanishes and

```text
p_i0/a_i = R (mod p),       p_0j/b_j = S (mod p),
RS=-g (mod p).                                        (2.3)
```

Choosing integer representatives and writing

```text
p_i0=R a_i+p k_i,           p_0j=S b_j+p l_j,
RS+g=pq,
```

gives the exact bilinear normal form

```text
p_ij=q a_i b_j+R a_i l_j+S b_j k_i+p k_i l_j.         (2.4)
```

Equal `a_i` give first-column primes in one residue class modulo `p`; a fixed
multiplicative shell contains only `O(1)` representatives of that class.
The same holds for the `b_j`.  Consequently

```text
#rows << max|a_i|,       #columns << max|b_j|,
(#rows)(#columns)<<H,
min(#rows,#columns)<<H^(1/2)=Y^(8/33).                (2.5)
```

### 2.2 Two-sided projective larger sieve

There is a useful but still insufficient improvement.  Factor the integer
rank-two matrix through its saturated row lattice,

```text
P=UV,       U in Z^(R x 2),       V in Z^(2 x C).      (2.6)
```

Put

```text
A=max_(i!=k)|det(U_i,U_k)|,
D=max_(j!=l)|det(V_j,V_l)|.
```

Every minor factors, and hence `AD` is the maximum minor height, `AD<<H`.
For a prime `q<min p_ij`, let `rho_q` be the number of projective row classes
of `U` modulo `q` and `sigma_q` the number of projective column classes of
`V`.  Since `U_i dot V_j=p_ij` never vanishes modulo `q`, row classes and the
orthogonal images of column classes are disjoint in `P^1(F_q)`:

```text
rho_q+sigma_q<=q+1.                                    (2.7)
```

Collision counting in the nonzero wedge products gives

```text
sum_(q<=Q) log(q)/rho_q <= log A+theta(Q)/R+O(1),
sum_(q<=Q) log(q)/sigma_q <= log D+theta(Q)/C+O(1).    (2.8)
```

Using `1/rho+1/sigma>=4/(q+1)` in `(2.8)`, and taking
`Q` to be a sufficiently small fixed multiple of `min(R,C)`, yields

```text
4 log min(R,C) <= log(AD)+O(1),
min(R,C)<<H^(1/4)<<Y^(4/33).                           (2.9)
```

The desired balanced tensor side is only `Y^(.00895-o(1))`, so `(2.9)` does
not close the application.

### 2.3 Why the broad statement is genuinely broad

If all numbers

```text
p_ij=p+a_i+b_j
```

are distinct primes and `max|a_i b_j|<<H`, then the matrix has rank at most
two and

```text
|(p+a_i)(1+b_j/p)-p_ij|=|a_i b_j|/p<<Y/B.             (2.10)
```

Thus broad SR2PF contains the finite binary prime-sumset problem.  Current
general results for `A+B` contained in the primes do not supply the requested
polylogarithmic bound in this generality.  This is the first indication that
one flattening discarded essential information.

## 3. Corrected weighted cleaning

The previous five-point cleaning was unnecessarily weak.  Let

```text
n asyp log log Y,
r=ceil(.0179 log Y/log n),
m=n^r,
```

and let `mu(s)` be the normalized product triangular digit-difference law.
The weighted transport hypothesis makes the `C_0/B`-bad set have

```text
mu(Bad)<<1/m.                                           (3.1)
```

Choose independently in each central digit range a random interval of length

```text
q=floor(alpha n),                                      (3.2)
```

where `alpha>0` is a sufficiently small fixed constant.  For every central
digit `s_j`, its inclusion probability is at most `Cq` times its triangular
mass.  Therefore the expected number of bad vertices in the random product
box is at most

```text
(Cq)^r mu(Bad) << (Cq/n)^r=(C alpha)^r=o(1).           (3.3)
```

Restricting the leading interval to positive digits makes the entire box
same-side without changing the argument.  Hence an all-good `q^r` box exists.
Since `log q/log n=1-o(1)`, its balanced flattenings have side

```text
q^(r/2)=Y^(.00895-o(1)).                               (3.4)
```

This replaces the old merely super-polylogarithmic side `5^(r/2)` by a fixed
power of `Y`.

## 4. Every cut, not one cut

On the clean box,

```text
p_s=X_s+O(Y/B),       X_s=Y exp(sum_j s_j omega_j),    (4.1)
```

and `X_s` is decomposable across every partition of the digit coordinates.
In any `3 x 3` minor of any flattening, the zero-error and one-error terms
vanish.  Thus

```text
|det_3|<<Y(Y/B)^2+(Y/B)^3<<Y^3/B^2=Y^(-1/33).         (4.2)
```

The determinant is an integer, hence zero for large `Y`.  This holds for
**every bipartition**.

Landsberg--Manivel proved set-theoretically, and Raicu ideal-theoretically,
that the `3 x 3` minors of all flattenings cut out the second secant variety
of a Segre variety.  After restricting each mode to its effective
two-dimensional space, the tensor is therefore, over an algebraic closure,
one of the following:

```text
Secant:   p_s=prod_j a_j(s_j)+prod_j b_j(s_j);         (4.3)

Tangent:  p_s=prod_j u_j(s_j)
                (c+sum_j f_j(s_j)).                   (4.4)
```

For a rational tensor, an identifiable secant pair is either rational or a
quadratic-conjugate pair.  Rational descent in the tangent branch is also
intrinsic.  In a fixed mode, contract against a covector.  There is a unique
covector line whose contraction is rank one: it is the annihilator of the
base-factor line.  Any other contraction retains two active tangent
directions and has a nonzero two-mode minor.  This line is defined by the
rational tensor, hence is Galois fixed.  Repeating in every mode recovers a
rational Segre base, and the tangent-space linear system is rational.  Thus
`(4.4)` can be taken over `Q`.  A zero coordinate of a base factor would make
that entire slice rank one, contrary to the nonzero prime minors.  Points
where uniqueness degenerates are assigned to the honest-secant branch.

This is the finite completion theorem that the earlier commuting-shift
program was trying to manufacture.  No infinite Hankel completion is needed.

## 5. The tangent/W branch is excluded

Restrict `(4.4)` to two chosen states in every mode and normalize the empty
vertex.  It becomes

```text
p_S=p_0 (prod_(i in S)x_i)(1+sum_(i in S)g_i),
                                      S subset [r],    (5.1)
```

with rational nonzero `x_i,g_i`.

### 5.1 Distinctness and height

Every `g_i` is nonzero.  Otherwise

```text
p_i/p_0=p_ik/p_k
```

for another coordinate `k`, contradicting unique factorization of four
distinct primes.  Similarly `g_i=g_j` would give

```text
p_i/p_j=p_ik/p_jk,
```

so the `g_i` are pairwise distinct.

Let

```text
Delta_ij=p_0 p_ij-p_i p_j,
a_i=g_i/(1+g_i).                                      (5.2)
```

Direct substitution in `(5.1)` gives

```text
-Delta_ij/(p_i p_j)=a_i a_j,
a_i^2=-Delta_ij Delta_ik/(p_i^2 Delta_jk).             (5.3)
```

All `Delta_ij` are nonzero integers of size `O(H)`.  Equation `(5.3)` shows
that every rational `a_i`, hence every `g_i`, has numerator and denominator
bounded by `Y^C` for one fixed `C`.

### 5.2 The p-adic diagonal-scale lemma

Fix a rational prime `ell` which is not one of the tensor entries, and let
`v=v_ell`.  Put `e_i=v(x_i)`.  From `(5.1)`,

```text
v(1+sum_(i in S)g_i)=-sum_(i in S)e_i.                (5.4)
```

For two coordinates `i,j`, the four affine factors satisfy the parallelogram
identity.  Their valuations are

```text
0, -e_i, -e_j, -e_i-e_j.                              (5.5)
```

If both `e_i` and `e_j` were nonzero, one of the four numbers in `(5.5)`
would be the unique minimum, in every possible sign configuration.  That is
impossible in a nonarchimedean four-term sum equal to zero.  Thus:

> For each `ell`, at most one coordinate has `v_ell(x_i)!=0`.

This covers every prime that can occur in an `x_i`.  Indeed, the face-minor
orbit `(5.10)` below gives `x_i^2=Delta({i})/Delta(empty)`; both nonzero
integers have size `O(H)<min_s p_s` for large `Y`.  Hence a prime in the
numerator or denominator of `x_i` cannot itself be a tensor entry.

For every other coordinate, `(5.4)` with `S={i}` says that `g_i` is
`ell`-integral.  Moreover, for every subset avoiding the exceptional
coordinate,

```text
1+sum_(i in S)g_i !=0 (mod ell).                       (5.6)
```

### 5.3 Near-rank-one stability

The p-adic lemma combines particularly cleanly with the original digit
labels.  Let `R_s=prod_i R_i(s_i)>0` be the reference tensor and put

```text
eta=(Y/B)/Y=1/B.                                      (5.7)
```

Writing the tangent tensor as `p_s=U_s L_s`, set `G_s=R_s/U_s`.  Then
`|L_s-G_s|<=eta|G_s|`.  Every mixed additive difference of `L` vanishes,
whereas `G` is a product tensor.  On a two-coordinate rectangle this gives

```text
 |G_i(a)-G_i(a')|       |G_j(b)-G_j(b')|
------------------- * ------------------- <= O(eta).  (5.8)
 |G_i(a)|+|G_i(a')|     |G_j(b)|+|G_j(b')|
```

Consequently at most one coordinate has chordal oscillation larger than
`O(sqrt(eta))`.  On every other coordinate, for two oriented adjacent digit
values,

```text
x_i=R_i(1)/R_i(0) (1+O(B^(-1/2))).                    (5.9)
```

Here the reference ratios are `exp(omega Q^i)`.  Their minimum displacement
from `1`, and their mutual separation, are `>>Y^(-.0179-o(1))`, whereas
`B^(-1/2)=Y^(-25/33)`.  After deleting at most one coordinate, the rational
numbers `x_i` are therefore positive, greater than `1`, and pairwise
distinct.

### 5.4 Determinant-height factorial closure

Fix two anchor coordinates and let `J` be the remaining stable coordinates.
For every subset `S` of `J`, the tangent formula gives the exact face-minor
orbit

```text
Delta(S)=Delta(empty) prod_(i in S)x_i^2.              (5.10)
```

Every member of this orbit is a nonzero integer of absolute value `O(H)`.
Write `x_i=A_i/B_i>1` in lowest terms.  Section 5.2 says that the prime
supports of distinct `x_i` are disjoint.  Integrality of all the values in
`(5.10)` therefore gives

```text
prod_(i in J) B_i^2 divides Delta(empty),
prod_(i in J) A_i^2 <= O(H).                           (5.11)
```

The positive integers `A_i` are pairwise coprime, distinct, and at least
`2`.  If `d=|J|=r-O(1)`, then

```text
(d+1)! <= prod_(i in J) A_i <= O(H^(1/2)).             (5.12)
```

Stirling's formula now yields

```text
r log r << log H << log Y,
r << log Y/log log Y.                                 (5.13)
```

This proves `(5.13)`, hence the tangent-branch bound `(0.3)`, and contradicts
the required size `(0.4)`.  The diagonal scalings were not
assumed constant: the p-adic lemma makes their prime supports disjoint, and
the physical near-rank-one labels make almost all of them distinct nonunits.

There is an independent sieve proof of `(5.13)`: after deleting the one
`ell`-adic exceptional coordinate, `(5.6)` and the contrapositive of
Croot--Mao--Yip Theorem 5.5 give
`#{i<j:g_i=g_j (mod ell)}>>min(r^2,r^3/ell)` for
`ell<=c r^2`; a product-of-rational-differences argument then gives
`r^3 log r<<r^2 log Y`.  The determinant-height proof above is shorter and
uses no rational common denominator.

### 5.5 A necessary warning fixture

Primality alone really does not remove diagonal scalings.  The tangent tensor

```text
T_s=sum_j b_j(s_j) prod_(h!=j)a_h(s_h),

a_1=(1,1),   a_2=(4,4),   a_3=(1,3),
b_1=(15,45), b_2=(15,41), b_3=(-16,-19)
```

has the eight distinct prime entries

```text
11, 149, 37, 227, 131, 509, 157, 587.                 (5.14)
```

Its Cayley hyperdeterminant is zero, as required for the tangent branch, but
one mixed additive second difference is `240`, not zero.  Thus the p-adic
argument above is essential; a direct reduction to an ordinary additive
Hilbert cube would have been false.

## 6. A secant subbranch that is impossible

The most natural small-correction secant is

```text
p_s=delta+prod_j z_j(s_j),
0<|delta|<<Y^(-17/33).                                (6.1)
```

Write `delta=A/Q` in lowest terms.  On a two-dimensional face, rank one of
`p_s-delta` gives

```text
p_00p_11-p_01p_10
 =delta(p_00+p_11-p_01-p_10).                         (6.2)
```

The left side is nonzero by unique factorization, so the second factor is
also nonzero.  Since it is `O(Y)`,

```text
Y^(17/33)<<Q<<Y.                                      (6.3)
```

Now

```text
T_s=Qp_s-A                                             (6.4)
```

is a positive integer rank-one tensor, all of whose entries are congruent to
`-A` modulo `Q`.  Factor it primitively as `T_s=g prod_j v_j(s_j)`.  Every
factor is a unit modulo `Q`, and cancellation in `(6.4)` shows that all local
values `v_j(s)` lie in one residue class modulo `Q`.  Distinct prime entries
make those local values distinct.  Shell comparability then gives, in every
active mode with `q` states,

```text
min_s v_j(s)>>qQ.                                     (6.5)
```

Fix all but any three active modes.  Equations `(6.4)--(6.5)` imply

```text
QY >> (qQ)^3,
Q^2 q^3 <<Y,                                          (6.6)
```

contradicting `Q^2>>Y^(34/33)`.  Thus `(6.1)` has at most two active modes.
The case `delta=0` is already impossible on a `2 x 2` face.

This kills the prototype “dominant product plus a tiny constant product.”
Section 7 supersedes it by treating an arbitrary varying second product.

## 7. The honest-secant branch is excluded

The local-degeneration formulation from the first pass was a false target.
For example, modulo every prime `ell=3 (mod 4)`, rational-square local ratios
remain in the square subgroup while `-1` does not.  Thus local subgroup escape
can be completely genuine.  The following global norm-fiber argument bypasses
it.

### 7.1 Rational or quadratic descent

On a binary restriction, write the honest secant as

```text
p_s=A_s+B_s,
A_s=prod_j a_j(s_j),       B_s=prod_j b_j(s_j).        (7.1)
```

No local vectors `a_j=(a_j(0),a_j(1))` and
`b_j=(b_j(0),b_j(1))` are proportional.  Proportionality would make the two
prime slices in that mode proportional, and two background contexts would
then equate products of four distinct primes.  No local coordinate vanishes
either: that would leave a rank-one prime slice and force one of its `2 x 2`
prime minors to vanish.

Consequently any three-mode `2 x 2 x 2` seed is an identifiable honest
secant.  Equivalently, if its two matrix slices are `M_0,M_1`, then `M_0` is
invertible and the two distinct eigenvalues of `M_1 M_0^(-1)` recover the two
summands.  Galois invariance of the rational tensor now gives one fixed
quadratic etale algebra

```text
E=Q x Q,                         rational summands; or
E=Q(sqrt(D)),                    conjugate summands,   (7.2)
```

such that, at every vertex,

```text
z_s=(A_s,B_s) in Q x Q, or z_s=A_s in Q(sqrt(D)),
p_s=Tr_E(z_s),             N_s:=A_s B_s=Norm_E(z_s) in Q*.  (7.3)
```

### 7.2 The bounded determinant orbit

Reserve modes `1,2,3`, fix mode `3` and all other unmentioned modes at their
zero states, and use modes `1,2` as a face.  For a background subset
`S subset {4,...,r}`, put

```text
D_S=p_(00,S)p_(11,S)-p_(01,S)p_(10,S).                (7.4)
```

These are nonzero integers with `|D_S|<<H`.  Direct expansion of `(7.1)` gives

```text
D_S=D_empty prod_(i in S) q_i,
q_i=a_i(1)b_i(1)/(a_i(0)b_i(0)) in Q*.                (7.5)
```

Choose one representative of every distinct value among the `q_i`, and write
it as `u_i/v_i` in lowest terms, with `v_i>0`.  For each rational prime `ell`,
apply integrality in `(7.5)` to the subset of representatives for which
`v_ell(q_i)<0`.  This shows

```text
prod_i v_i divides D_empty.
```

Applying `(7.5)` to the subset of all representatives then shows

```text
prod_i |u_i|<=O(H),          prod_i v_i<=O(H).         (7.6)
```

There are `O(T^2)` signed rationals of projective height at most `T`.  Thus, if
`K` is the number of distinct `q_i` and their heights are put in increasing
order, the `j`-th height is `>>sqrt(j)`.  From `(7.6)`,

```text
sqrt(K!)<<C^K H^2,
K<<log(Y)/log log(Y).                                  (7.7)
```

### 7.3 A large fixed-norm fiber

Group the `d=r-3` background modes according to their common `q_i`, with group
sizes `m_1,...,m_K`.  A vector of Hamming counts

```text
(|S intersect G_1|,...,|S intersect G_K|)
```

fixes `prod_(i in S)q_i`, and hence fixes `N_S`, because

```text
N_S/N_empty=D_S/D_empty=prod_(i in S)q_i.             (7.8)
```

There are at most `prod_g(m_g+1)` count vectors, so one fixed-norm fiber has
cardinality at least

```text
2^d / prod_g(m_g+1).                                  (7.9)
```

The norm in this fiber has polynomial height, uniformly in `r`.  Indeed, on
the reserved three-mode seed, put

```text
D_ij=N_empty(alpha_i-beta_i)(alpha_j-beta_j).
```

Its nonzero Cayley hyperdeterminant is

```text
Hyp=N_empty^2 prod_(i=1)^3(alpha_i-beta_i)^2,
N_empty=D_12 D_13 D_23/Hyp.                           (7.10)
```

All quantities on the right are integer polynomials in eight primes of size
`O(Y)`, while `|D_ij|<<H`.  Thus `h(N_empty)<=Y^C`; `(7.8)` gives the same
bound for every `N_S`.  The square class of `Hyp` is also the fixed quadratic
field in `(7.2)`.

### 7.4 Fixed norm has too few integer traces

Fix `N=u/v in Q*` in lowest terms and `E=Q(sqrt(D))`, allowing `D=1` for the
split algebra.  If an element of `E` has integer trace `p` and norm `N`, write
it as `(p+w sqrt(D))/2`.  With

```text
X=vp,        n=vw,
```

the norm equation becomes

```text
X^2-D n^2=4uv.                                         (7.11)
```

Here `n` is an integer: `D n^2` is integral and squarefree `D` cannot absorb
the square of a nontrivial denominator.  In the split case `(7.11)` is an
ordinary factor-pair equation.  In a quadratic field,
`(X+n sqrt(D))` is a principal ideal divisor of `(4uv)`.  There are at most
`tau(|4uv|)^O(1)` such ideal divisors.  Generators of one ideal differ by a
unit; the restriction `|p|<<Y`, together with polynomial height of `u,v`,
allows `O(log Y)` unit powers in a real quadratic field and `O(1)` in an
imaginary field.  Uniformly in `D`, the number of possible integer traces is

```text
exp(O(log(Y)/log log(Y))).                             (7.12)
```

All primes in `(7.9)` are distinct traces with the same norm.  Jensen's
inequality and `(7.7)` give

```text
sum_g log(m_g+1)<=K log(1+d/K).
```

Comparing `(7.9)` with `(7.12)` therefore yields

```text
d log 2
 <=K log(1+d/K)+O(log(Y)/log log(Y)),
r<<log(Y)/log log(Y).                                  (7.13)
```

Indeed, after dividing by `log(Y)/log log(Y)`, the left side is linear in the
normalized `d`, while the first term on the right grows only logarithmically.
This excludes both rational and quadratic-conjugate honest secants at the
dimension required by `(0.4)`.

## 8. Counterexample search and lower boundary

No super-polylogarithmic construction satisfying the full conditions was
found.  Several tempting sources fail:

- CRT and Schinzel-type constructions do not control a growing
  `q^r=Y^(.0179-o(1))` family in one shell.
- Additive/W constructions are excluded by `(5.13)`.
- Constant-shift product constructions are excluded by `(6.6)`.
- Proper-subgroup escape really occurs locally (squares modulo primes
  `3 (mod 4)` give an explicit example), but the fixed-norm argument in
  Section 7 bypasses it globally.
- Green--Tao or narrow-prime-AP constructions only handle fixed pattern size
  with available quantitative bounds.

There can be no absolute dimension bound.  For every fixed `q,r`, Shao's
narrow-prime-AP theorem supplies fixed-length prime progressions with
polylogarithmic common difference.  Reshape such a progression using a fixed
mixed-radix index:

```text
p_s=p_0+d sum_j w_j s_j.                              (8.1)
```

This is an unscaled W tensor, so every flattening has rank at most two.  The
positive decomposable reference

```text
X_s=p_0 prod_j(1+d w_j s_j/p_0)                       (8.2)
```

differs from `(8.1)` by `O_(q,r)(d^2/Y)`, which is
`o(Y^(-17/33))` for fixed `q,r`.  Thus fixed-size examples exist; the sought
theorem must be genuinely quantitative.

## 9. Decision-tree correction

The important mistake was one level above the projective sieve: choosing one
balanced matrix flattening erased the compatible minors from every other
cut.  The corrected route is

```text
weighted prime transport
        |
        v
alpha*n cleaning: q^r=Y^(.0179-o(1))
        |
        v
all bipartition ranks <=2
        |
        v
sigma_2(Segre)
     /              \
tangent/W         honest secant
  CLOSED          CLOSED
     \              /
      \            /
       r << logY/loglogY.                              (9.1)
```

The finite tensor gate is therefore closed.  For the zero-free-strip program,
the maximum-information next step moves back upstream to the analytic
transport that is supposed to produce this all-good prime tensor.  Proving the
broader one-flattening matrix conjecture is no longer required for that
application, although it remains an independent problem.

## 10. Status ledger

```text
broad matrix SR2PF polylog bound:                         OPEN
broad matrix bound min(R,C)<<Y^(4/33):                   PROVED
improved alpha*n weighted cleaning:                      PROVED
clean balanced side Y^(.00895-o(1)):                     PROVED
all bipartition flattening ranks <=2:                    PROVED
global sigma_2 secant/tangent fork:                      IMPORTED
rational tangent/W bound r<<logY/loglogY:                PROVED
constant tiny-shift secant with >=3 modes:               EXCLUDED
genuinely two-sided rational/quadratic secant:            EXCLUDED
faithful all-cut tensor SR2PF bound r<<logY/loglogY:       PROVED
actual-prime tensor-Fejer transport:                      NOT RESOLVED
uniform zero-free strip:                                 NOT PROVED
RH:                                                       NOT PROVED
```

## 11. Literature used

- J. M. Landsberg and L. Manivel, [*On the ideals of secant varieties of
  Segre varieties*](https://arxiv.org/abs/math/0311388).
- C. Raicu, [*Secant Varieties of Segre--Veronese
  Varieties*](https://arxiv.org/abs/1011.5867).
- E. Croot, J. Mao, and C. H. Yip, [*Hilbert cubes in sets with arithmetic
  properties*](https://arxiv.org/abs/2603.14654), especially Theorem 5.5 and
  Corollary 2.14.
- X. Shao, [*Narrow arithmetic progressions in the
  primes*](https://arxiv.org/abs/1509.04955).

This report supersedes the single-flattening recommendation and the
five-point cleaning estimate in
`ZETA23-UNIFORM-STRIP-DECISION-TREE-CONSOLIDATION-AND-MAXIMUM-INFORMATION-GAIN-2026-08-30.md`.
