# QP critical Walsh tail: close/transverse codegree audit

**Date:** 2026-08-24  
**Verdict:** the diffuse-bin square gain moves the entire critical Walsh
problem to effective multiplicity

```text
H>D^(7/8).                                             (0.1)
```

The existing close-endpoint theorem closes `|x-y|<=D^(3/8)`.  For the
remaining transverse endpoints there are two exact carrier-preserving
identities and a polynomial determinant-collision consequence.  They make
the inverse problem much denser than the former `H=D^(1/8)` formulation,
but do not yet prove the required actual-prime codegree bound.

The remaining pointwise theorem is only

```text
deg(x,y)<<D^(7/8)q^o(1),
|x-y|>D^(3/8),                                        (0.2)
```

not the older and much stronger `sqrt(D)` conjecture.  Proving (0.2), or a
weighted substitute on the high-Walsh fibres, closes the critical
`M=D^(15/8)` bin.

No sharp four-cycle theorem is proved here.

## 1. Exact automatic Carleson range

Let `R_H` be the randomized mass on endpoint fibres with effective Walsh
multiplicity in `[H,2H)`.  On a factor-two coefficient bin of support `M`,
the refined square theorem gives

```text
sum_H R_H <= C D min(1,D/M)q^o(1)||z||2^4.           (1.1)
```

For `M>D`, (1.1) is `C D^2/M`.  Therefore

```text
H<=M/D  =>  R_H<=C D^2/M<=C D/H.                    (1.2)
```

This is exactly the desired Carleson estimate in that range.  At

```text
M=D^(15/8),
randomized budget =D^(1/8),
H_0=M/D=D^(7/8).                                     (1.3)
```

For a fixed endpoint cell `(x,y)`, Cauchy gives

```text
m_xy<=#{active Walsh signatures}
    <=#{physical common-neighbor walks between x and y}.                (1.4)
```

Thus a uniform physical codegree bound `H_0 q^o(1)` makes the range
`H>H_0` empty, while (1.2) handles the range below it.  This proves the
claimed implication with no sign or phase assumption.

## 2. Close endpoints are already closed

The proved common-neighbor estimate is

```text
deg(x,y)
 <<(|x-y|+1)D^(1/2)+D^(13/16).                       (2.1)
```

Consequently

```text
|x-y|<=D^(3/8)
  => deg(x,y)<<D^(7/8)+D^(13/16)
               <<D^(7/8)q^o(1).                     (2.2)
```

The only pointwise range left by this route is (0.2).

## 3. Exact transverse carrier identity

Fix actual prime-power endpoints `x<y`, put `g=y-x`, and let one common
walk have carrier `v` and completions `a,b`.  Write

```text
r=8xva-q^3,                 s=8yvb-q^3,
k=xa-yb,                    j=a-b.                  (3.1)
```

Direct expansion gives the two exact identities

```text
r-s=8v k,                                            (3.2)
y r-x s=8xyv j-gq^3.                                (3.3)
```

Since `|r|,|s|<<qD` and all shell nodes are comparable with `q`, (3.2)
gives `|k|<<D`, while (3.3) gives

```text
|v j-gq^3/(8xy)|<<D.                                (3.4)
```

Thus the transverse fibre is a literal short-product fan in `(v,j)` of
length `O(D)`, and it retains the physical common carrier `v`.  Fixed
`(x,y,k)` determines `(a,b)` on the actual narrow shell, and then determines
`v`; hence the nontrivial walks have distinct nonzero defects `k`.

Equation (3.4) is stronger bookkeeping than a carrier-free determinant
relation, but an ordinary divisor bound over a length-`D` interval still
allows `Dq^o(1)` points.  It does not by itself save the required eighth
power.

## 4. Determinant collision energy above the new threshold

For two walks `i,l`, put

```text
Delta_il=a_i b_l-a_l b_i.                            (4.1)
```

Their defects satisfy another exact identity:

```text
x Delta_il=k_i b_l-k_l b_i.                          (4.2)
```

It follows that `|Delta_il|<<D`.  For distinct actual all-distinct walks,
`Delta_il` is nonzero: proportional primitive completion pairs would be
equal, and fixed-pair uniqueness would then identify the walks.

If a fibre contains `N` walks and `r_Delta` counts its ordered completion
pairs of determinant `Delta`, then

```text
sum_(Delta!=0) r_Delta=N(N-1),
sum_(Delta!=0) r_Delta^2
 >>N^2(N-1)^2/D.                                     (4.3)
```

In particular, one nonzero determinant occurs at least

```text
max_Delta r_Delta >>N^2/D.                           (4.4)
```

At `N>D^(7/8)`, (4.3) supplies `D^(5/2-o(1))`
equal-determinant four-walk collisions and (4.4) supplies a determinant
matching of size `D^(3/4-o(1))`.  Determinant pigeonholing is therefore no
longer below threshold.

There is a useful rigidity check.  For primitive vectors `P_i=(a_i,b_i)`
in the project collar, if

```text
det(P_(i-1),P_i)=det(P_i,P_(i+1))=Delta!=0,           (4.5)
```

then

```text
det(P_i,P_(i-1)+P_(i+1))=0.
```

Primitivity makes `P_(i-1)+P_(i+1)=lambda P_i` with integral `lambda`.
The collar ratio is below `e^.4<3/2`, so `1<lambda<3` and therefore
`lambda=2`.  Every constant-determinant path is an exact vector arithmetic
progression.  The actual-prime progression lemma restricts one long path to
`q^o(1)` length.

This does **not** bound (4.4): a popular determinant relation is a partial
matching and may consist of `D^(3/4)` isolated edges.  Scalar determinant
energy alone does not provide the quotient collisions or global packing
needed by BSG.

## 5. Stronger affine recurrence and its remaining packing gap

The companion critical-recurrence audit proves a sharper statement using
defect differences.  On a fixed endpoint fan, the map

```text
k -> (a_k,b_k)                                        (5.1)
```

is a Freiman two-isomorphism.  Indeed, equality of two defect differences
makes the two completion-coordinate discrepancies an integer multiple of
`(y,x)`; twice the shell diameter is below either endpoint, so that multiple
must vanish.

Consequently an `N`-walk fan has one nonzero completion translation
`(alpha,beta)` repeated

```text
Omega(N^2/D).                                        (5.2)
```

times.  At the critical high tail this is again `D^(3/4-o(1))`, and all
corresponding color matrices lie in the exact affine plane

```text
c11-c21=alpha,              c12-c22=beta.            (5.3)
```

This identifies a genuine tangent/translation object, not just a scalar
collision.  One plane has weighted color mass at most `||z||2^4`; what is
still missing is a Carleson packing theorem over the planes and endpoint
pairs.  The exact recurrence and Pluecker ledgers are in
`ZETA23-QP-CRITICAL-DEFECT-FAN-RECURRENCE-AND-ENDPOINT-QUADRUPLE-GATE-2026-08-24.md`.

## 6. Equivalent transverse two-inverse target

Put `T=q^3/8` and `delta=C D/q`.  Dropping only the requirement that the
two nearest integers are themselves prime powers gives the safe majorant

```text
deg(x,y)
 <=sum_(v in S)
    1_(||T/(xv)||<=delta) 1_(||T/(yv)||<=delta).      (6.1)
```

Majorize each interval by a Selberg polynomial of degree

```text
Q asymp delta^(-1)=q/D.                              (6.2)
```

The nonzero Fourier phases are

```text
S_(r,s)=sum_(v in S)
 e(T(ry+sx)/(xyv)),             |r|,|s|<=Q.          (6.3)
```

Because actual distinct endpoints are coprime and `2Q<min(x,y)`, the map

```text
(r,s) -> ry+sx                                      (6.4)
```

is injective in the frequency box.  The zero phase occurs only at
`(r,s)=(0,0)` and contributes merely `D^2/q=D^(-1/16+o(1))`.

A mask-sensitive vector-valued reciprocal large-sieve estimate strong
enough to bound the remaining part of (6.1) by `D^(7/8)q^o(1)` would prove
(0.2).  Standard scalar absolute-value estimates do not currently supply
that power; the slow ray `(r,s)=(1,-1)` is precisely the close-gap mode
already isolated in Section 2, while transverse rational-approximation rays
must be controlled collectively.

### 6.1 A larger modular-inverse sector is now closed

The defect itself supplies a one-dimensional chart which is stronger than
termwise use of (6.3).  Put

```text
w_y=least absolute residue of x^(-1) mod y,
w_x=least absolute residue of -y^(-1) mod x,
w=min(w_x,w_y).                                      (6.5)
```

On each unwrapped defect branch the first completion is affine with step
`w`, while the reciprocal carrier phase has second and third derivatives
of sizes `w^2/q` and `w^3/q^2`.  Optimizing the degree of the Selberg
majorant and using the third-derivative estimate, including the
`1+wD/q` wrap count, first proves

```text
w<=D^(13/12)  =>  deg(x,y)<<D^(7/8)q^o(1).          (6.6)
```

There is a stronger wrapped-branch estimate.  A natural branch has length
`N=q/w`, the phase parameter in Fourier degree `h` is `T_h asymp hq`, and
there are `J<<wD/q` branches.  On a dyadic block `h asymp H`, Bourgain's
local exponential-sum bound

```text
beta(alpha)<=1/12+(2/3)alpha,     5/12<alpha<=3/7,
alpha=log(N)/log(T_h),                                  (6.7)
```

is stronger here than every single global exponent pair.  Take Selberg
degree `K=D^(1/8)`.  At the endpoint `w=D^(73/64)` one has

```text
N=D^(59/64),       J=D^(5/64),       T_K=D^(35/16),
alpha_K=59/140,    beta(alpha_K)=51/140.              (6.8)
```

Thus the top dyadic block is exactly

```text
J*T_K^(1/12)*N^(2/3)=D^(5/64+51/64)=D^(7/8).          (6.9)
```

The lower blocks lie in this line or the adjacent Bourgain line
`13/84+alpha/2`; their exponents increase continuously to `(6.9)`.
The zero and Selberg-resolution terms are respectively `D^(-1/16)` and
`D^(7/8)`.  Consequently

```text
w<=D^(73/64)  =>  deg(x,y)<<D^(7/8)q^o(1).           (6.10)
```

Thus the remaining pointwise sector is only

```text
|x-y|>D^(3/8),       w_x>D^(73/64),
                     w_y>D^(73/64).                 (6.11)
```

The full proof, the free-degree second-derivative precursor, and the exact
exponent ledger are in
`ZETA23-QP-TRANSVERSE-TWO-INVERSE-POINTWISE-AND-LITERATURE-AUDIT-2026-08-24.md`.
This is a genuine new closed range, not a uniform codegree theorem.

### 6.2 Why the two inverse windows are not independent

The two inverse charts share one exact Bezout coordinate.  Choose `s,m`
with

```text
g*s+1=m*x,             so m*x-g*s=1.                 (6.12)
```

Then every solution of `xa-yb=k` is parametrized by

```text
a=(s+m)k+y*n,          b=s*k+x*n.                    (6.13)
```

Here `s` represents `-y^(-1) (mod x)`, `s+m` represents
`x^(-1) (mod y)`, and the two least inverse steps are their distances to
the corresponding modulus lattices.  In particular the two rotations are
not independent random coordinates.

The reciprocal phases are even closer:

```text
T/(xa)-T/(yb)=-T*k/(x*y*a*b)<<D/q.                   (6.14)
```

This is the same size as the physical window.  Hence the diagonal Fourier
modes of the two windows are coherent throughout the allowed defect range.
A coefficient-blind product large sieve cannot obtain the desired gain by
treating the two inverse conditions as independent; any continuation must
use cancellation across wrap branches, the selected mask, or packet
extraction.

### 6.3 Euclidean rebranching closes two large-step sectors

The first Euclidean descent is nevertheless useful.  In either signed
completion chart write its host modulus as

```text
Q_0=L*w+r,             rho=|r|=min(Q_0 mod w,w-(Q_0 mod w)).            (6.15)
```

If the old lift is `a=w*k-Q_0*n`, the unimodular change `t=k-L*n` gives

```text
k=t+L*n,               a=w*t-r*n.                                     (6.16)
```

On a fixed `t`-fibre the completion step is now `rho`, while the number of
fibres is

```text
B<<1+q/w+rho*D/q.                                                   (6.17)
```

Running the second- and third-derivative Selberg arguments on these fibres
proves the target in either of the following sectors:

```text
w>=D^(21/16),   rho<=D^(27/32),   w*rho>=D^(27/16);                  (6.18)
w>=D^(25/16),   rho<=D^(13/12),   w*rho>=D^(7/3).                    (6.19)
```

The exact bounds are, respectively,

```text
D^2/q+D/K+D*rho*sqrt(K/q)
 +(1+q/w+rho*D/q)*sqrt(q)/(rho*sqrt(K)),                              (6.20)

D^2/q+D/K+D*rho^(1/2)*q^(-1/3)*K^(1/6)
 +sqrt(D*(1+q/w+rho*D/q))*q^(1/3)*rho^(-1/2)*K^(-1/6).               (6.21)
```

An independent hostile exponent audit found no missing branch factor.  These
are disconnected closed subsets of `(6.11)`, not a covering of it.

### 6.4 The dense remainder has one canonical packet ray

For a fan of `H` defects `K`, the map `k -> (a_k,b_k)` is an exact Freiman
two-isomorphism.  Hence either completion projection `A` satisfies

```text
E^+(A)>=E^+(K)>>H^4/D.                                                (6.22)
```

At `H=D^(7/8)` the forced energy is exactly `D^(5/2)`.  Moreover every
genuine three-or-more-point affine/Hankel packet in one endpoint fan has a
direction `(d,p_a,p_b,-p_v)` with `|d|<<D` and
`|p_a|+|p_b|+|p_v|<<sqrt(D)`.  Since `(d,p_a)` lies in the determinant-`y`
lattice `p_a==x^(-1)d (mod y)`, two such directions have determinant both a
multiple of `y` and `O(D^(3/2))=o(q)`.  It is zero.  Thus every actual packet
in the fan lies on one primitive continued-fraction completion ray.

What remains after peeling that ray is the explicit open estimate

```text
E^+(A_packet-free)<<D^(5/2)*q^o(1).                                  (6.23)
```

Together with `(6.22)`, `(6.23)` would prove the required
`H<<D^(7/8)q^o(1)`.  It is not a consequence of additive density alone:
the popular chords may all be isolated two-point secants.

There is one further exact reduction inside `(6.23)`.  Write an additive
completion rectangle as `a,a+r,a+s,a+r+s`.  Its integral carrier mixed
difference obeys

```text
Box(v)=C_x*r*s*(2*a+r+s)/[a*(a+r)*(a+s)*(a+r+s)]+O(D/q).              (6.24)
```

For `|r*s|<=c*q`, integrality forces `Box(v)=0`, after which the shell lower
bound in `(6.24)` forces `|r*s|<<D`.  Thus `D<<|r*s|<<q` is an empty
annulus, and all rectangles below it contribute only

```text
O(H*D*log q+H^2)<<D^2*log q.                                           (6.25)
```

The packet-free energy gate is therefore confined to broad rectangles
`|r*s|>>q`.  This removes the entire narrow sector by a square-root margin,
but broad isolated two-secants remain uncontrolled.

## 7. Binary status

```text
critical randomized budget D^(1/8):                  PROVED;
automatic Carleson range H<=D^(7/8):                 PROVED;
effective Walsh multiplicity <= physical codegree:   PROVED;
endpoint gaps <=D^(3/8):                             CLOSED;
inverse steps min(w_x,w_y)<=D^(73/64):               CLOSED;
shared Bezout/phase-coherence identities (6.12)-(6.14): PROVED;
Euclidean remainder sectors (6.18)-(6.19):           CLOSED;
unique low-height CF completion ray per fan:          PROVED;
packet-free reciprocal energy (6.23):                 OPEN;
mixed-difference annulus D<<|r*s|<<q:                 EMPTY;
narrow reciprocal energy (6.25):                      CLOSED;
broad rectangles |r*s|>>q:                            OPEN;
carrier short-product identity (3.3):                PROVED;
determinant collision lower bound (4.3):             PROVED;
popular affine translation D^(3/4):                  PROVED;
global translation-plane Carleson packing:           OPEN;
transverse actual-prime codegree D^(7/8):             OPEN;
sharp four-cycle theorem:                             NOT PROVED.
```

Executable replay:

```text
src/qp_critical_walsh_codegree_audit.py
src/test_qp_critical_walsh_codegree_audit.py
src/qp_residual_walsh_defect_inverse.py
src/test_qp_residual_walsh_defect_inverse.py
src/qp_transverse_two_inverse_ledger.py
src/test_qp_transverse_two_inverse_ledger.py
src/qp_dense_defect_cf_energy_gate.py
src/test_qp_dense_defect_cf_energy_gate.py
```

The mixed-difference and current-literature audit is
`ZETA23-QP-PACKET-FREE-RECIPROCAL-MIXED-DIFFERENCE-AND-YAO-AUDIT-2026-08-24.md`.
