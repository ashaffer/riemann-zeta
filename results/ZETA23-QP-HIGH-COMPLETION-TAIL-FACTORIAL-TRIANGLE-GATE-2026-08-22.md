# QP four-cycle: high-completion tail and the factorial-triangle gate

**Date:** 2026-08-22  
**Verdict:** the proposed dyadic high-completion estimate

```text
W_K(z)=sum_(C: K<=m(C)<2K) w_z(C)
      <<D/K*q^o(1)*||z||_2^4                         (HC_K)
```

is proved on every color fibre having one carrier line with `asymp K`
points.  The proof is exactly the height-versus-length cancellation

```text
H*K^2<<D,             color mass at height H <<sqrt(DH),
sqrt(DH)<<D/K.                                      (0.1)
```

Thus coherent tangent/Hankel packets are not the remaining obstruction.
After merging them, the unresolved family consists of `K` completions
spread across polynomially many one- and two-point lines or broad slices.

For that scattered residual there is an exact singleton-safe reduction.
Write the completion multiplicity as a codegree in the binary
row-pair/color-pair incidence matrix.  The desired tail follows from either
anchored factorial estimate

```text
F_(2,K)(gamma)<<D*K*q^o(1),                        (AF_2)
F_(3,K)(gamma)<<D*K^2*q^o(1).                      (AF_3)
```

The proved three-row elimination turns `(AF_3)` into the following precise
restricted reciprocal-height theorem:

```text
max_gamma sum_(X in X_(gamma,K)) 1/H(X)
   <<K^2*q^o(1).                                   (SRH_K)
```

Here `X_(gamma,K)` contains only row triples which are common to `gamma`
and to another color-pair `gamma'` with `K<=m(gamma,gamma')<2K`, after the
already merged packet triples are removed.  It does **not** include
irrelevant triples in the full neighborhood of `gamma`.

At the critical broad multiplicity

```text
K=D^(5/16),                                        (0.2)
```

the exact new target is

```text
R_(gamma,K)<<D^(5/8)q^o(1).                        (0.3)
```

The presently proved unrestricted reciprocal-height estimate is only
`D^(2+o(1))`.  A direct calculation below shows that one coherent tangent
packet actually satisfies (and essentially saturates) `(SRH_K)`, with
`R_K<<K^2 log K`.  The problem is aggregating polynomially many scattered
packets or singleton directions, not the internal height mass of one
packet.  No proof of (0.3) for that scattered actual-prime family is
obtained here.  This is the first irreducible gate in this route.

The anisotropic singleton-line endpoint gives the same quantitative gap as
the global theorem: current color mass `D^(15/16)`, required mass
`D^(11/16)`, missing saving `D^(1/4)`.  Hence this audit does not prove the
uniform four-cycle bound.

There is one unconditional new subrange: fixed nonzero color determinant
is a partial matching, so `(HC_K)` holds for

```text
0<|det C|<=D/K.                                    (0.4)
```

At (0.2), only the determinant range

```text
D^(11/16)<|det C|<=D                              (0.5)
```

remains.  This closes `11/16` of the logarithmic determinant-exponent axis,
but it gives no asserted fraction of the weighted mass; that mass may
concentrate in the remaining `5/16`-wide exponent interval.

There is a second unconditional dyadic reduction for the literal residual
one- and two-point-line family.  The identity

```text
e cross f=-det(C)*(a cross A)
```

places the residual points in a lattice of covolume `|det C|`.  An
anisotropic Minkowski/coset argument proves

```text
m(C)<<1+sqrt(E*F/|det C|),                         (0.6)
```

when their residual rectangle has side lengths `E,F` and every residual
affine line has at most two points.  Consequently the critical residual is
further confined to

```text
|det C|=D^ell, ell>11/16,       E*F>=D^(ell+10/16-o(1)). (0.7)
```

Only `17/64` of the formal high-determinant `(ell,log_D(EF))` exponent
rectangle survives (0.7).  This is again a geometric ledger, not a weighted
mass proportion.  Residual-affine lines with three or more points still
need an inverse/merger theorem.

---

## 1. The high tail is a weak form of FC, not a free corollary

Put

```text
w_z(C)=|z_c11*z_c12*z_c21*z_c22|,
S(z)=sum_C m(C)w_z(C).                              (1.1)
```

If `(HC_K)` holds for every dyadic `K`, then

```text
S(z)
 <=sum_(K dyadic) 2K*W_K(z)
 <<D*q^o(1)*||z||_2^4.                             (1.2)
```

Conversely, the positive FC estimate `S(z)<<Dq^o(1)||z||_2^4` immediately
implies `(HC_K)` by `K W_K<=S`.  Up to the logarithmic number of dyadic
levels, the family `(HC_K)` is therefore equivalent to the desired positive
four-cycle theorem.  A proof must use the same missing arithmetic; Markov's
inequality applied to the present `D^(5/4)` trace only gives

```text
W_K(z)<<D^(5/4)/K*q^o(1),                          (1.3)
```

which retains the complete missing `D^(1/4)`.

The stronger off-diagonal pair-energy theorem would give `D/K^2`, but that
theorem is open and is not used below.

## 2. Exact Gram/codegree formulation

### 2.1 The low color-determinant tail is already sharp

Fix a signed nonzero integer `k`.  Write

```text
C=(x,y;z,w),                    x*w-y*z=k.          (2.0a)
```

For fixed top pair `(x,y)`, two possible bottom pairs obey

```text
x*(w-w')=y*(z-z').                                (2.0b)
```

The all-distinct actual-shell colors `x,y` are coprime.  Hence

```text
(z-z',w-w')=j*(x,y).                               (2.0c)
```

The project shell diameter is smaller than every shell coordinate, so
`j=0`.  Reversing top and bottom proves the column statement.  Thus the
fixed-`k` color support is a partial matching between ordered top and bottom
color pairs.  With pair weights `v_(x,y)=|z_xz_y|`, its weighted mass is

```text
sum_(det C=k)w_z(C)<=||v||_2^2<=||z||_2^4.         (2.0d)
```

This remains true after requiring actual completions or `m(C)~K`.  Summing
the `O(L)` signed layers `0<|k|<=L` gives

```text
W_(K, |det C|<=L)(z)<<L*||z||_2^4.                (2.0e)
```

Taking `L=D/K` proves (0.4).  The high determinant interval (0.5) is where
a square-function across the distinct partial permutations is genuinely
needed; positive layer summation alone gives no further saving.

### 2.2 Residual-lattice lines close a second dyadic region

Fix two color columns

```text
p=(c_1,d_1),       q=(c_2,d_2),
k=det(p,q)!=0.                                      (2.0f)
```

For three common row vertices `(a_i,A_i)`, put

```text
e_i=c_1*a_i-d_1*A_i,
f_i=c_2*a_i-d_2*A_i.                               (2.0g)
```

The active product windows give `|e_i|,|f_i|<<D`.  Direct bilinearity of
the cross product gives the exact identity requested by the normal/content
audit:

```text
e cross f=-k*(a cross A).                          (2.0h)
```

In particular every residual point

```text
v_i=(e_i,f_i)
```

lies in the image lattice

```text
Lambda_(p,q)
 =( c_1 -d_1; c_2 -d_2 ) Z^2,
det Lambda_(p,q)=|k|.                              (2.0i)
```

This yields a sharp elementary theorem for the literal one- and two-point
residual-line sector.  Suppose the selected residual points lie in a
rectangle of coordinate side lengths `E,F`, and every affine lattice line
contains at most two selected points.  Scale the rectangle to a unit square.
The scaled lattice has covolume

```text
delta=|k|/(E*F).                                      (2.0j)
```

Minkowski supplies a primitive lattice vector `v_0` of scaled sup norm
`O(sqrt(delta))`.  The parallel lattice lines are the level sets of
`det(v_0,.)`; consecutive levels differ by exactly `|k|`.  In the original
coordinates the determinant functional has range `O(sqrt(|k|EF))` on any
translate of the rectangle.  Thus only `O(1+sqrt(EF/|k|))` parallel cosets
meet it.  The two-point line cap gives

```text
#{residual points}<<1+sqrt(E*F/|k|).              (2.0k)
```

Consequently a scattered fibre with `m(C)~K` requires

```text
E*F>>|k|*K^2*q^(-o(1)).                            (2.0l)
```

This is pointwise, so every dyadic block violating (2.0l) is empty after
the residual-rich lines have been removed.  Combining it with (0.4), all
power-separated blocks are now closed unless

```text
|k|>D/K,                E*F>=|k|*K^2*q^(-o(1)).    (2.0m)
```

Write

```text
K=D^kappa, |k|=D^ell, E=D^e, F=D^f.               (2.0n)
```

At the critical `kappa=5/16`, the remaining exponent polytope is

```text
11/16<ell<=1,                e+f>=ell+10/16.       (2.0o)
```

Thus at the bottom determinant boundary both residual projections must
already have product at least `D^(21/16)`, and at `ell=1` their product must
be at least `D^(13/8)`.  In the formal two-dimensional `(ell,e+f)` rectangle,
(2.0o) occupies `17/64` of the previously remaining high-determinant area;
this is only an exponent-polytope fraction, not a claim about weighted
mass.

The scope is exact.  A three-point residual-affine line is not discarded by
(2.0k); it must either be identified with an already merged carrier packet
or treated by a separate rich-line inverse theorem.  The theorem therefore
proves a substantial dyadic range of the requested singleton-line family,
while isolating the two-large-residual-projection transition.

### 2.3 Two-sided residuals and the balanced-box theorem

There is an identical residual lattice on the carrier side.  With the
signed color matrix

```text
K_C=(c11,-c12;-c21,c22),          k=det K_C,        (2.0p)
```

put, for a completion `(a,b)`,

```text
r=K_C^T*a,                  s=K_C*b.               (2.0q)
```

Both maps have determinant `k`; both outputs lie in `O(D)` boxes.  If the
row residual rectangle has side lengths `E,F` and the carrier residual
rectangle has side lengths `G,H`, applying (2.0k) on both sides gives, in
the literal two-point-line sector,

```text
E*F>>|k|*K^2*q^(-o(1)),
G*H>>|k|*K^2*q^(-o(1)).                            (2.0r)
```

There is also an exact bilinear coupling.  If

```text
L=a^T*K_C*b,
```

then

```text
r^T*adj(K_C)*s=k*L.                                (2.0s)
```

The active fixed-level estimate is `|L|~|k|q`, while every entry of
`adj(K_C)` is `asymp q`.  Taking absolute values in (2.0s) proves

```text
(E+F)*(G+H)>>|k|^2,                                (2.0t)
```

or, dyadically, at least one row--carrier coordinate product has size
`D^(2ell-o(1))` when `|k|=D^ell`.

Thus the exact two-sided residual polytope at critical multiplicity is

```text
e+f>=ell+10/16,
g+h>=ell+10/16,
max(e,f)+max(g,h)>=2ell.                           (2.0u)
```

In a fully balanced box `E~F~G~H~D^rho`, equations (2.0r)--(2.0t) give

```text
rho>=max(ell/2+5/16,ell).                          (2.0v)
```

Throughout the remaining determinant interval `ell>11/16`, the second
term dominates.  Hence a balanced hostile block has every residual side at
least the color-determinant scale `D^ell`; near `ell=1` all four residual
projections must occupy essentially the full `D` range.

If one treats `(ell,e+f,g+h)` as a formal rectangular exponent ledger, the
two independent inequalities in (2.0r) leave only

```text
223/3072 = 0.07259...                              (2.0v1)
```

of the original high-determinant ledger volume; (2.0t) removes more.  As
before, this is not a density or weighted-mass assertion.

This is the strongest conclusion available from the bilinear equation
alone.  Bilinearity, injectivity, and absence of three collinear points do
not force a rich line.  For arbitrary distinct integers `t`, the matching

```text
r_t=(t,t^2+1),
s_t=(t^2-t+1,1-t)                                  (2.0w)
```

satisfies

```text
r_t dot s_t=1.                                     (2.0x)
```

Both projections lie on nondegenerate parabolas and therefore have no
three collinear points, yet the matching can be arbitrarily long.  This is
an exact integer-algebraic countermodel, not an actual-prime carry model.
It proves that a stronger line-rich dichotomy must retain the prime-power
masks, product windows, or cross-pair incidences; it cannot follow from
(2.0s) and one-to-one pairing alone.

Let `alpha=(a_1,a_2)` be an ordered row pair and
`gamma=(c_1,c_2)` an ordered color pair.  Define

```text
B_(alpha,gamma)=1                                  (2.1)
```

when there is a common carrier `b` making both active triples
`(a_1,b,c_1)` and `(a_2,b,c_2)`.  Pair uniqueness makes `b` unique.  For
the two vertical color pairs of `C`,

```text
gamma=(c11,c21),       gamma'=(c12,c22),
m(C)=|N(gamma) intersect N(gamma')|
    =(B^*B)_(gamma,gamma').                        (2.2)
```

Let

```text
u_gamma=|z_c1*z_c2|.                               (2.3)
```

Then

```text
sum_gamma u_gamma^2<=||z||_2^4.                   (2.4)
```

All-distinct, determinant-band, orientation, and already deleted sector
restrictions only remove entries from the following nonnegative symmetric
kernels, so they cause no difficulty.

For `r=2,3`, define

```text
A_(r,K)(gamma,gamma')
 =1_(K<=m(gamma,gamma')<2K)*binom(m(gamma,gamma'),r),
gamma!=gamma'.                                    (2.5)
```

For `K>=2`, respectively `K>=3`,

```text
1_(K<=m<2K)<=4*K^(-2)*binom(m,2),
1_(K<=m<2K)<=27*K^(-3)*binom(m,3).                 (2.6)
```

Schur's test and (2.4) give the rigorous weak-type inequalities

```text
W_K(z)
 <<K^(-2)*max_gamma F_(2,K)(gamma)*||z||_2^4,
W_K(z)
 <<K^(-3)*max_gamma F_(3,K)(gamma)*||z||_2^4,      (2.7)

F_(r,K)(gamma)=sum_(gamma') A_(r,K)(gamma,gamma').
```

The bounded levels `K<3` are already covered by the determinant-layer
estimate.  Equations (2.7) prove `(AF_2)` or `(AF_3)` implies `(HC_K)`.

This use of `m`, rather than `m(m-1)` in the definition of the tail, is
legitimate: the factorial coefficient appears only as a positive majorant
after restricting to `m>=K`.  A singleton has zero factorial mass.

## 3. Exact anchored factorial identities

For two row vertices put

```text
t_2(alpha,beta)=|N(alpha) intersect N(beta)|,      (3.1)
```

and define `t_3(X)` similarly for a three-element row set `X`.  Double
counting gives, before the high-`K` restriction,

```text
sum_(gamma'!=gamma) binom(m(gamma,gamma'),2)
 =sum_({alpha,beta} subset N(gamma))
       (t_2(alpha,beta)-1),                        (3.2)

sum_(gamma'!=gamma) binom(m(gamma,gamma'),3)
 =sum_(X subset N(gamma), |X|=3)(t_3(X)-1).        (3.3)
```

The restricted versions are just as exact.  If

```text
n_(gamma,K)(X)
 =#{gamma'!=gamma:
      X subset N(gamma'), K<=m(gamma,gamma')<2K}, (3.4)
```

then

```text
F_(3,K)(gamma)=sum_(X subset N(gamma)) n_(gamma,K)(X).
                                                               (3.5)
```

In particular only triples participating in a high-completion color matrix
are charged.  Pure `K_C`, by contrast, charges every geometrically
available slice and is not singleton-safe.

## 4. Insert the K_(3,2) height lemma

For a row triple

```text
X=((a_1,A_1),(a_2,A_2),(a_3,A_3)),
h=(a_1,a_2,a_3) cross (A_1,A_2,A_3),               (4.1)
```

write `H(X)` for the infinity norm of the primitive vector on the line
spanned by `h`.  The proved three-row elimination gives

```text
t_3(X)<<1+D/H(X).                                  (4.2)
```

All realized pair determinants are `O(D)`, hence `H(X)<<D`; the right side
of (4.2) is therefore `O(D/H(X))`.  Equations (3.4)--(4.2) imply

```text
F_(3,K)(gamma)
 <<D*R_(gamma,K),                                  (4.3)

R_(gamma,K)
 =sum_(X in X_(gamma,K)) 1/H(X),                  (4.4)
```

where `X_(gamma,K)` is the support of (3.4).  After quotienting the already
proved coherent packet components, retain only residual triples in (4.4).
Combining (2.7) and (4.3) gives

```text
W_K(z)
 <<D*R_K/K^3*q^o(1)*||z||_2^4,
R_K=max_gamma R_(gamma,K).                         (4.5)
```

Therefore

```text
R_K<<K^2*q^o(1)  ==>  W_K(z)<<D/K*q^o(1)||z||_2^4. (4.6)
```

This proves the displayed `(SRH_K)` reduction.

If `K=D^k` and `R_K=D^r`, (4.5) has exponent

```text
1+r-3k.                                            (4.7)
```

The desired exponent is `1-k`; hence exactly `r<=2k` is required.  At
`k=5/16`, this is (0.3).

The earlier determinant-dyadic argument proves only

```text
sum_(X subset Y, |X|=3)1/H(X)<<D^(2+o(1))         (4.8)
```

for an arbitrary localized row set `|Y|<=D`.  Substitution into (4.5) is
far too weak.  More importantly, coherent affine/tangent packets make raw
factorial moments large while their merged operator is already at the `D`
target.  The calculation in the next section shows that one packet
nevertheless has exactly the correct reciprocal-height scale.  The actual
issue is a high-`K` restricted aggregation such as (4.4), not an estimate
for every triple in an arbitrary `D`-point row set.

## 5. Dominant carrier lines already have the sharp tail

Suppose a color fibre with `m(C)~K` has a maximal carrier line containing
`T~K` of its completions.  The exact quadratic line parameterization gives

```text
H(C)*T^2<<D,                                       (5.1)
```

where `H(C)` is the primitive tangent-direction height.  The gap-token
aggregation theorem gives, on a dyadic height block,

```text
sum_(C assigned, H(C)~H) w_z(C)
 <<sqrt(DH)q^o(1)||z||_2^4.                        (5.2)
```

Equations (5.1)--(5.2), summed over the logarithmically many
`H<=D/K^2`, yield

```text
W_(K,dominant-line)(z)
 <<D/K*q^o(1)||z||_2^4.                            (5.3)
```

The same packet is compatible sharply with `(SRH_K)`.  For consecutive
tangent rows

```text
x_i=(M+i,M+i+1),              0<=i<K,              (5.3a)
```

the primitive height of the triple `i<j<k` is exactly

```text
H(i,j,k)=(k-i)/gcd(j-i,k-j).                       (5.3b)
```

Writing `r=j-i`, `s=k-j`, its reciprocal-height sum is

```text
sum_(r,s>=1,r+s<K) (K-r-s)*gcd(r,s)/(r+s)
 <<K*sum_(n<K)tau(n)
 <<K^2 log K.                                      (5.3c)
```

Thus a single sharp `K`-point tangent packet uses precisely the allowed
`K^(2+o(1))` budget in `(SRH_K)`.  A successful square function must merge
or orthogonalize different packets; it must not demand an artificial
power saving inside one.

The same conclusion holds for the already merged at-least-three-point
fixed-direction affine/Hankel components.  This is the packet-merger half
of the proposed breakthrough.

A more general proved curvature estimate illustrates the exact loss.  If
a parabolic block has at most `J` occupied lines and `K` is larger than the
baseline `J`, then

```text
m(C)<<J+sqrt(DJ/H(C)),
K<=m(C)  ==>  H(C)<<D*J/K^2.                       (5.4)
```

Together with (5.2),

```text
W_(K,J,curvature)(z)
 <<D*sqrt(J)/K*q^o(1)||z||_2^4.                   (5.5)
```

Thus `(HC_K)` is sharp when `J=q^o(1)`.  The factor `sqrt(J)` measures the
unmerged cross-direction problem.  Formula (5.5) does not address the
baseline case `K~J`, where multiplicity comes from many one-point lines.

## 6. The scattered singleton-line endpoint

After (5.3), a hostile fibre has no line containing a fixed positive
fraction of its `K` points.  In the sharp residual model it has polynomially
many lines with only one or two occupied parameters.  Such a fibre creates
`asymp K^2` transverse secants and `asymp K^3` noncollinear triangles.

The second-factorial formulation says that it is enough to prove the
scale-sensitive transverse-secant estimate

```text
max_gamma sum_(gamma':m~K) binom(m(gamma,gamma'),2)
 <<D*K*q^o(1).                                     (6.1)
```

The third-factorial formulation says equivalently, as a sufficient
condition, that the scattered triangle row sum is

```text
max_gamma sum_(gamma':m~K) binom(m(gamma,gamma'),3)
 <<D*K^2*q^o(1).                                   (6.2)
```

Fixing one secant and the color determinant gives a partial matching, and
fixing two independent secants gives `O(1)` weighted color mass.  Neither
fact proves (6.1) or (6.2): the secant and triangle planes vary with `C`.
The exact triangle normal satisfies

```text
det N_T=-Delta_01*Delta_12*Delta_20,               (6.3)
```

and the two carrier sides obey simultaneous variable-coefficient Pluecker
relations.  Summing the varying primitive normals is precisely the missing
arithmetic large-sieve step.  Local plane estimates cannot control the
cross-plane term; the Farey matching is an exact integer countermodel to
that purely geometric inference, although it does not embed in the actual
prime-power carry support.

Consequently a proof of `(SRH_K)`, (6.1), or (6.2) must use the actual
prime-power masks to show that distinct scattered triangle/tangent labels
are orthogonal on average.  This is the promised "packet merger plus square
function" theorem in a quantitatively exact form.

## 7. Critical exponent ledger

The determinant-content parabolic endpoint has

```text
m(C)~D^(5/16),          current color mass D^(15/16). (7.1)
```

The desired high tail requires

```text
D/m(C)=D^(11/16).                                  (7.2)
```

Thus the missing color-mass saving is

```text
15/16-11/16=1/4.                                  (7.3)
```

Multiplying by `m(C)` gives the identical completed ledger

```text
15/16+5/16=5/4,             desired exponent 1.   (7.4)
```

The factorial-triangle route has not reduced that numerical gap yet; it
has isolated it to the scattered, varying-plane actual-prime family.

```text
HC_K for a dominant K-point carrier line:          PROVED;
HC_K for merged rich affine/Hankel packets:         PROVED;
exact second/third factorial weak-type reductions: PROVED;
K23 reduction HC_K <= D*R_K/K^3:                   PROVED;
critical reciprocal-height target R_K<=D^(5/8):    DERIVED;
HC_K on color determinants |det C|<=D/K:            PROVED;
critical remaining determinant range (11/16,1]:    ISOLATED;
two-point residual-line bound 1+sqrt(EF/|det C|):   PROVED;
critical remaining residual range e+f>=ell+10/16:  ISOLATED;
two-sided residual product constraints:            PROVED;
balanced residual side rho>=ell:                    PROVED;
bilinear level alone forces a rich line:             FALSE (INTEGER MODEL);
raw unrestricted reciprocal-height D^2:            PROVED EARLIER / TOO WEAK;
scattered residual SRH_K or triangle square sum:    OPEN;
uniform HC_K and four-cycle bound:                  OPEN.
```

Finite factorial identities and exponent arithmetic are replayed in
`src/qp_high_completion_tail_gate.py` and
`src/test_qp_high_completion_tail_gate.py`.
