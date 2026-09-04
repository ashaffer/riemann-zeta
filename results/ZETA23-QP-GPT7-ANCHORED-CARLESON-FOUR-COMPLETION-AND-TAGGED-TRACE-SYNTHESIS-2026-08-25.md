# QP sharp four-cycle: anchored Carleson, four completions, and the tagged-trace gate

**Date:** 2026-08-25  
**Binary verdict:** the sharp four-cycle bound is **not proved**.  The best
unconditional project estimate remains

```text
tr((A_z^* A_z)^2) << D^(9/8+o(1)) ||z||_2^4.
```

This closeout materially changes the shape of the last gap.  The residual
degree-product conjecture is unnecessarily strong, the earlier claimed
two-anchor broad-token gain disappears after the primitive-content scale is
inserted, and the exact positive closure is an anchored Carleson packing
theorem.  A genuine part of that theorem is now proved.

## 1. Correct residual closure

Let `T_res` be the residual cyclic incidence, with left vertices `p`, right
vertices `gamma`, and degrees `d(p)`.  Put

```text
W(gamma)=sum_(p~gamma) d(p).
```

One rowwise Cauchy inequality gives

```text
||T_res xi||_2^2 <=sum_gamma W(gamma)|xi_gamma|^2. (1.1)
```

Hence

```text
max_gamma W(gamma)<<Dq^o(1)                         (NDS)
```

implies the desired residual estimate.  This is strictly weaker than the
edgewise degree-product condition `(RDP)`.

The apparent rank-one relaxation

```text
sum_(c,C) W(c,C)x_c x_C
 <<Dq^o(1)(sum_c x_c)^2,              x_c>=0,       (WNDS)
```

is not asymptotically softer than `(NDS)`.  Positivity proves `(WNDS)` from
`max W`; conversely a vector with mass `1/2` on the two coordinates of one
off-diagonal ordered pair detects `W(c,C)/4`.  Thus the best constants obey

```text
(1/4)max W <= best WNDS constant <=max W.           (1.2)
```

The double-star model still proves that `(RDP)` is stronger than necessary,
but coefficient weights cannot hide a single heavy `W(c,C)` inside the
rowwise-Cauchy route.

## 2. The exact anchored Carleson theorem

For a fixed right vertex `gamma`, write

```text
r_gamma(eta)=#{p:p~gamma and p~eta}.
```

Double counting gives, exactly,

```text
W(gamma)=sum_eta r_gamma(eta).                      (2.1)
```

If `gamma=(c,C)` and `eta=(d,E)` are physical actual-shell pairs, the four
hard windows imply

```text
|C*d-c*E|<<D.                                      (2.2)
```

Primitivity and the narrow shell make a fixed determinant label identify at
most one `eta`.  Thus `r_gamma` has `O(D)` support.  The sharp remaining tail
is

```text
#{eta:r_gamma(eta)>=R} <<D/R*q^o(1)       for dyadic R. (ACCT)
```

Dyadic summation shows `(ACCT)` is equivalent to `(NDS)` up to `q^o(1)`.
The physical affine biclique has `R` completions on `D/R` partners and
saturates this estimate, so `(ACCT)` has the correct scale.

## 3. New unconditional Carleson range

Let

```text
H=deg(gamma),
B=max_(p!=p' in N(gamma)) codeg(p,p').
```

Every `R`-rich partner contains `R(R-1)` ordered distinct pairs from
`N(gamma)`.  Counting those pairs first proves

```text
#{eta:r_gamma(eta)>=R} R(R-1) <=H(H-1)B.           (3.1)
```

The audited fixed-row-pair theorem gives, in the all-distinct transverse
sector,

```text
B<<sqrt(D)q^o(1).                                  (3.2)
```

Consequently `(ACCT)` is proved whenever

```text
R >> H^2/sqrt(D) * q^o(1).                         (3.3)
```

In particular the complete residual `(NDS)` estimate is now proved for
every anchor satisfying

```text
H<=D^(1/4)q^o(1).                                  (3.4)
```

For a general anchor, only

```text
q^o(1)<<R<<min(sqrt(D),H^2/sqrt(D)),
H>>D^(1/4)                                         (3.5)
```

remains in this positive route.

## 4. Exact four-completion sieve

Let `P_q` be the actual prime-power shell and let `F_u(v)` be the unique
actual node `w`, when it exists, satisfying

```text
|8uvw-q^3|<=qD.
```

Fix `gamma=(c,C)`.  Every two-step residual chain

```text
gamma -- (b,B) -- (d,E)
```

is equivalent, without multiplicity, to a pair `(a,x) in P_q^2` passing
the four tests

```text
b=F_a(c),       B=F_a(C),
d=F_x(b),       E=F_x(B).                          (4.1)
```

Thus `W(gamma)` is exactly a four-selected-completion count.  Define

```text
delta=b*c-B*C,       ell=C*d-c*E.
```

Both are `O(D)`, and the map from a chain to `(delta,ell)` is injective.
This gives an elementary `O(D^2)` bound and identifies `(NDS)` as an
occupied-cell theorem: only `Dq^o(1)` of the `D^2` determinant cells may be
physical.

The approximate-gcd ledger is

```text
r=x*d-a*c,       s=x*E-a*C,
x*ell=C*r-c*s.                                      (4.2)
```

Because `D^2<q`, fixed short error data has at most one shell divisor `x`.
That proves uniqueness inside a cell, not the required reduction from
`D^2` occupied cells to `D`.  The two other completion masks in (4.1) must
supply the aggregation.

### 4.1 Lossless Bezout-token normal form

Choose `u,v` with `c*u-C*v=1`.  The centre and endpoint determinant
coordinates lift unimodularly as

```text
b=u*delta-C*n,       B=v*delta-c*n,       P=(delta,n),
d=-v*ell+c*m,        E=-u*ell+C*m,        R=(ell,m).
```

The root `(c,C)` is `R_0=(0,1)`.  With

```text
K=(-2uv       cu+Cv
   cu+Cv      -2cC),                 det K=-1,
```

one has, exactly,

```text
b*d-B*E=det(P,R),        b*d+B*E=P^T*K*R.            (4.3)
```

Thus the two hard windows for a row `y` are the single diamond

```text
|4y P^T*K*R-q^3|+4y|det(P,R)|<=qD.                  (4.4)
```

Both token maps are in `GL_2(Z)`, so primitivity, actual masks, and row
multiplicity are preserved.  Consequently `W(gamma)` is losslessly the
number of selected primitive paths `R_0--P--R` in an `O(D)` token box
satisfying the two diamonds.  The Gram identity for `K` factors back into
the original two physical product legs and supplies no extra divisor
average.  Equivalently, its two Lorentz multiplication laws are identities
for `(2bc)(2Cd)` and `(2BC)(2cE)`; they do not create the absent third
diamond between the root and the endpoint.  In the literal all-prime
fixture, `delta=-72`, `ell=36`, and `delta*ell=-2592` despite `D^2<q`.

There is a further exact globalization which removes a misleading degree of
freedom.  Write the centre orbit as

```text
P_t=(t,n_t) <-> (b_t,B_t).
```

The endpoint with label `h=-j` is exactly

```text
R^j=-P_j,                 eta^j=(B_j,b_j).            (4.5)
```

Also `P_0=(0,-1)` corresponds to `(C,c)`.  If `X(t,j)` denotes the
symmetric two-product row mask for the cross-products

```text
b_t*B_j,                  B_t*b_j,
```

then the anchor mask is `X(t,0)` and

```text
W(gamma)=sum_t X(t,0) sum_j X(t,j).                  (4.6)
```

Thus the two token clouds are one reflected modular orbit, not independent
point sets.  The shell gives the exact strip identity

```text
n_t-(u/C)t=-b_t/C,                                  (4.7)
```

whose transverse width is below one.  This reduces the physical difference
directions from the crude `O(D^2)` count to `O(D)`.  It does not make the
orbit a bounded union of lines: one audited legal strip has `289` points,
`344` primitive difference directions, and largest affine line `18`.

More decisively, on the reflected orbit

```text
det(P_t,-P_j)=b_t*B_j-B_t*b_j=(t*b_j-j*b_t)/C=O(D)   (4.8)
```

for every physical pair in the label square.  Hence the middle determinant
band is globally automatic.  All of the missing saving must come from the
radial product window and its rounded actual row.

The radial diamond is essential: primitive adjacent tokens give `D^2`
small-determinant cells if it is deleted.  Conversely, on the principal
adjacent chart `P_r=(r,r-1)`, `R_s=(s,s+1)`, the first middle product window
forces

```text
(r-1)^2-(r-1)s+s^2<=5D/16,                           (4.9)
```

once `q/2>=16D^2`.  Hence that complete chart has only `O(D)` physical
cells.

The same calculation has a useful fixed-chart extension.  For

```text
P=P_0+rV,                 R=R_0+sW,
```

if `det(V,W)!=0`, harmonic summation over the distinct integral slopes of
`det(P,R)` gives `O(D log D)` cells from the determinant strip alone.  If
the directions are parallel, the radial product has the universal stationary
residual

```text
-x_0 b_0 d_0 (A^2+A*G+G^2+A*G(A+G)),                (4.10)
```

whose quadratic Hessian has determinant `3x_0^2p^2z^2`.  This gives `O(D)`
cells for a non-null parallel chart when its row is locked to the integral
stationary affine law.  Hessian degeneracy in the parallel branch is exactly
the coordinate tangent ruling, already covered by the tangent theorem.

The row lock is not automatic on the actual-prime mask, and the self-orbit
may cross many translated digital lanes.  The unproved step is now precisely
to sum the **rounded radial rows** of that one orbit with a `Dq^o(1)`
Carleson budget.

There is nevertheless exact rounded-row rigidity.  For
`f(b,d)=q^3/(8bd)`, four accepted corners obey

```text
Delta_b Delta_d x
 =(q^3/8)(1/b_0-1/b_1)(1/d_0-1/d_1)
   +Delta_b Delta_d(x-f).                            (4.11)
```

If the curvature term plus the four row errors is below one, integrality
forces the mixed row difference to vanish.  The seven-prime fixture is a
literal non-null parallel chart whose rows lie on an integral rounded plane,
even though the formal stationary slopes are nonintegral.  But (4.11)
controls occupied rectangles only: a rectangle-free support can still have
the `D^(3/2)` Zarankiewicz size.  The missing input is therefore sparse
incidence packing, not another Taylor expansion.

## 5. The Cramer two-anchor correction

For Cramer tokens `(k_i,r_i)`, the valid lattice bound is

```text
|V| <=(2 floor(E/g)+1)
      (floor(2Eg/Delta_12)+1),                     (5.1)
```

where `g=gcd(k_1,r_1)`.  Primitive physical vectors give

```text
g|delta,
Delta_12=|delta|*|det(u_1,u_2)|<=|delta|D,
E<<|delta|D.                                       (5.2)
```

Substitution shows the right side of (5.1) is always at least a constant
times `D`.  It never gives the needed `D/|U|` for a nontrivial opposite arm.
The two-anchor identity is correct; its earlier interpretation as a broad
sector closure was false.

## 6. What is already closed for the rank-one target

The exceptional successive-minima branch sends every power-rich partner
into `q^o(1)` rational affine/Hankel charts.  The previously proved
height-versus-length theorem and chart merger already bound the **weighted**
coherent high tail at the sharp `D/R` scale.  Therefore an unweighted
cross-chart version of `(ACCT)` is not needed for the original rank-one
problem.

The genuinely open weighted sector is the generic/scattered branch.  In
cardinal form its clean target is

```text
#{generic eta:r_gamma(eta)>=R} <<D/R*q^o(1).        (GP_R)
```

Equivalent weighted formulations are the existing anchored factorial
estimate `(AF_2)`/`(AF_3)` and the selected reciprocal-height square-function
gate `(SRH_R)`.  A generic rich partner may use `R^2` distinct secants once
each, so the fixed-secant divisor theorem does not aggregate this branch.

## 7. Why the newest analytic theorems do not close it

Hu's 2026 hereditary off-diagonal Young theorem controls full-vector
convolutions on suitable algebraic varieties.  The QP factorial quantity is
instead an `ell^1` norm of a **zero-tag slice** after summing over pinned
normals/levels.  The safe full-tag rank-one ambient variety has intrinsic
energy exponent `13/5`, not the near-diagonal exponent `2`; fixing one tag
recovers a quadratic surface, but loses aggregation across tags.

Even granting near-quadratic hereditary energy fiberwise is insufficient.
The product-of-parabolas set

```text
S_(P,K)={(r,r^2,t,t^2)}
```

has no affine lines and every subset has near-quadratic full-vector energy,
while its zero-tag off-diagonal trace has size `P*K*(K-1)`.  At
`P=D,K=sqrt(D)` this exceeds the desired factorial scale by `sqrt(D)`.

The missing analytic statement is therefore a **tagged-trace Carleson
Young inequality**, schematically

```text
Tr_0(F,G)(E)=sum_tau sum_(X-Y=E) F(tau,X)conj(G(tau,Y)),
||Tr_0(F,F)||_(ell^1(E!=0)) <<D*R*q^o(1)            (7.1)
```

on the selected physical `R`-rich masks, or an equivalent vector-valued
Bessel theorem across the pinned levels combined with reciprocal-height
Carleson packing.  Existing full-vector energy and scalar Kloosterman
theorems do not provide (7.1).

The Bezout lift does not cure this mismatch: it only permutes the rows and
columns of the incidence matrix, so it preserves the partner degrees, the
zero-tag factorial mass, and every singular value.  An exact Paley mask on a
literal four-hard-window principal chart quantifies the resulting scalar
loss.  For a prime `p=3 mod 4`, the quadratic-residue difference matrix has

```text
K=(p-1)/2,
F_2=p*K*(K-1),
singular values (p-1)/2 and sqrt(p+1)/2,
||W||_*/||W||_F asymp sqrt(p).                       (7.2)
```

Embedding `p~sqrt(D)` makes the unavoidable projective/nuclear cost
`D^(1/4)`.  This is a method witness, not an actual-prime counterexample.
Even four hypothetical independent applications of the current scalar
Blomer--Pascadi saving exceed the remaining `D^(1/8)` project gap by only
`D^(3/128)`; the exact scalarization cost is larger by `D^(29/128)`.
Therefore the needed theorem must retain the joint mask as a genuinely
vector-valued or tagged-trace object.

There is also no shortcut obtained by multiplying the pointwise
`sqrt(D)` codegree theorem by an unselected determinant-band estimate.  On
one color interval of squared length `o(q)`, the positive rank-one
determinant-band mass is indeed `O(sqrt(D)||z||_2^4)`, and this proves the
localized sharp theorem.  Globally, however, flat weights on the actual
shell primes have determinant-band mass `D^(1-o(1))`; this constant mode is
sharp.  Pointwise codegree times the global positive band therefore gives
only `D^(3/2+o(1))`.  The required gain must be conditional on the
high-completion mask--precisely `(GP_R)`, `(AF_2)`, or (7.1)--rather than a
property of the bare determinant band.

## 8. Hostile checks

Two complementary examples delimit the theorem.

1. The all-integer affine hard-window biclique has side `L`, window
   `D=Theta(L^2)`, and anchored mass `L^2=Theta(D)`.  It sharply saturates
   `(ACCT)`.
2. A literal seven-prime actual-shell fixture at
   `q=5,868,182`, `D=1,912` has a residual central support with endpoint
   degrees `4,4` and anchored `W=14`.  Thus actual prime support is not a
   matching, although the fixture is safely below the conjectural bound.

A larger full-integer scan at `q=200,000`, `D=371` finds

```text
H=18,               max neighbour degree=18,
W=271=.730458...D.
```

All `271` paths lie on one pair of parallel token lines.  A deterministic
`3,927`-root broad-direction stress test has maximum `W=7` and at most two
paths off the best centre line.  A complete actual-prime-power shell at
`q=10,604,226`, with `137,783` nodes, gives `W=10`; all ten paths are again
parallel.  These are finite diagnostics, not an asymptotic inverse theorem.

## 9. Verification and exact status

New executable ledgers and tests:

```text
src/qp_narrow_token_row_sum_gate.py
src/test_qp_narrow_token_row_sum_gate.py
src/qp_actual_prime_nds.py
src/test_qp_actual_prime_nds.py
src/qp_four_completion_bezout_token.py
src/test_qp_four_completion_bezout_token.py
src/qp_four_completion_bezout_normal_form.py
src/test_qp_four_completion_bezout_normal_form.py
src/qp_affine_four_completion_hessian.py
src/test_qp_affine_four_completion_hessian.py
src/qp_scattered_token_search.py
src/test_qp_scattered_token_search.py
src/qp_tagged_trace_projective_barrier.py
src/test_qp_tagged_trace_projective_barrier.py
src/qp_rounded_parallel_orbit.py
src/test_qp_rounded_parallel_orbit.py
src/qp_tangent_plucker_inverse.py
src/test_qp_tangent_plucker_inverse.py
src/qp_rank_one_h_tangent_residual.py
src/test_qp_rank_one_h_tangent_residual.py
src/qp_pure_state_channel.py
src/test_qp_pure_state_channel.py
src/qp_simultaneous_divisor_rdp.py
src/test_qp_simultaneous_divisor_rdp.py
```

New or extended Lean certificates:

```text
lean/weilcert/QPNarrowTokenRowSumGate.lean
lean/weilcert/QPActualPrimeNDS.lean
lean/weilcert/QPFourCompletionBezoutToken.lean
lean/weilcert/QPFourCompletionBezoutNormalForm.lean
lean/weilcert/QPAffineFourCompletionHessian.lean
lean/weilcert/QPScatteredTokenOrbitReflection.lean
lean/weilcert/QPRoundedParallelOrbit.lean
lean/weilcert/QPTangentPluckerInverse.lean
lean/weilcert/QPRankOneHTangentResidual.lean
lean/weilcert/QPPureStateChannel.lean
lean/weilcert/QPSimultaneousDivisorRDP.lean
```

The consolidated focused suite passes `81` Python tests and all `11` Lean
certificates listed above.

```text
RDP is necessary:                                      FALSE ABSTRACTLY;
NDS implies the residual operator bound:               PROVED;
WNDS differs asymptotically from NDS:                   FALSE;
NDS iff anchored codegree L1/Carleson up to q^o:        PROVED;
four-completion formulation and determinant injection:  PROVED;
lossless Bezout-token/two-diamond normal form:            PROVED;
principal adjacent q=2M full-integer chart is O(D):      PROVED;
endpoint cloud is the reflected centre orbit:             PROVED;
self-orbit kernel is symmetric and rooted at j=0:         PROVED;
physical token difference directions are O(D):            PROVED;
transverse fixed affine chart is O(D log D):               PROVED;
stationary non-null parallel chart is O(D):                PROVED CONDITIONALLY ON ROW LOCK;
exact rounded reciprocal four-corner identity:              PROVED;
actual rounded-row parallel chart is O(D):                 OPEN;
D^2<q collapses D^2 occupied cells to D:                FALSE AS AN ARGUMENT;
two-anchor token count closes broad sectors:             FALSE;
ACCT for R>>H^2/sqrt(D):                                PROVED;
NDS for H<=D^(1/4)q^o:                                  PROVED;
weighted coherent/parabolic high tail:                  PROVED PREVIOUSLY;
Hu off-diagonal Young implies generic GP_R:              NO;
scalarization of the joint mask has only q^o loss:       FALSE AS A METHOD;
generic tagged-trace/Carleson packing:                   OPEN;
sharp four-cycle bound:                                  NOT PROVED.
```

The remaining gap is no longer “prove a degree-product bound,” nor is it a
sum over unrelated Bezout charts.  It is one specific theorem: a
mask-sensitive rounded-row/tagged-trace Carleson estimate for the symmetric
self-orbit kernel `(4.6)`.  That theorem would close the residual sector;
together with the proved tangent and coherent theorems, it would finish the
sharp four-cycle bound.

## 10. Addendum: total-kernel reduction and the exact major-arc obstruction

The next attack removes the root selector completely.  Put

```text
E_gamma=sum_(t,j) X(t,j).
```

Since `X` is zero-one,

```text
W(gamma)=sum_t X(0,t)sum_j X(t,j) <= E_gamma.       (10.1)
```

Thus the stronger total-edge estimate

```text
E_gamma << D*q^o(1)                                (TE)
```

would imply `(NDS)`.  A one-window Selberg majorant gives

```text
E_gamma
 <<D^3/q +(D/q)sum_(1<=|h|<=q/D)|S_gamma(h)|,

S_gamma(h)=sum_(t,j) alpha_t alpha_j
 e(h*q^3/(8*b_t*B_j)).                             (10.2)
```

The zero mode is

```text
D^3/q=D^(15/16+o(1)),                              (10.3)
```

strictly below the target.  A diagonal-strength reciprocal-product large
sieve would close `(10.2)`, but its coefficient-uniform enlargement to the
full-integer orbit is false before coherent packets are removed.  This does
not refute the corresponding theorem with the actual-prime mask retained.
On the adjacent integer orbit `gamma=(M,M+1)`, `q=2M`, the phase
has an integer linear part and a quadratic remainder `O(D^2/q)`.  Hence a
whole low-frequency band has size `asymp D^2`; global Cauchy loses exactly
`sqrt(D)`, although the corresponding positive radial ellipse itself has
only `O(D)` cells.  The required analytic statement must therefore be a
**packet-subtracted** reciprocal-product large sieve, not a uniform scalar
one.

Short cycles have a complementary exact invariant.  For an oriented edge
`i -> i+1`, put

```text
kappa_i=b_i*B_(i+1)-B_i*b_(i+1).
```

Telescoping the two product legs and using `D^2/q=o(1)` forces

```text
sum_i x_i*kappa_i=0                                (10.4)
```

on every cycle of length `O(log D)`.  If all such zero-holonomy cycles could
be charged to `O(D*q^o(1))` coherent packet edges, the Moore bound would make
the remaining graph linear-sized and prove `(TE)`.  The charging theorem is
not known.  More precisely, with

```text
F_i=(q^3/8)log(b_i/B_i),
w_ij=x_ij det(v_i,v_j),
```

each hard edge satisfies

```text
|(F_i-F_j)-w_ij|
 <=D^2/[16q(1-D/q^2)].                             (10.5)
```

Thus `D^2<q` forces exact zero circulation on every cycle through length
`16`.  On a zero-holonomy triangle, if its three row labels have span less
than `e^(-0.4)q/D`, its three physical orbit vertices are exactly collinear.
This is a genuine packet seed.  It is not a complete inverse theorem:
noncollinear triangles can escape by a row jump of order `q/D` or larger.

Exact hostile tests also show why a global charging theorem must retain the
actual mask and the nonreturn split:
a critical full-integer nonreturn bridge produces an induced nonplanar
six-cycle, while the audited search's first reported all-distinct scattered
prime six-cycle at `q=25013` requires literal `D=8344`, versus the critical
`D=135`.

The finite evidence for `(TE)` is favorable but non-probative.  The richest
complete integer scan has `E/D=432/371=1.16442`, with every incident vertex
on one affine line; the tested actual-prime kernel has `E/D=14/2548`.  The
multilevel tangent obstruction contributes only a linear-sized biclique to
one fixed self-orbit chart.  No critical-window counterexample was found.

The exact finite implication `(10.1)` and the product telescoping behind
`(10.4)` are certified in
`lean/weilcert/QPSelfOrbitTotalKernel.lean`.  The analytic packet-subtracted
large sieve and the cycle-charging inverse theorem remain open.  Therefore
this addendum sharpens the last theorem but does **not** change the binary
verdict: the sharp four-cycle bound is not proved.

The expanded focused suite, including the total-kernel adversarial and log-
holonomy ledgers, passes `89` Python tests and `12` standalone Lean
certificates.  Lean certifies only the stated finite algebraic identities; it
does not certify `(10.2)`, the analytic phase estimate, packet charging,
`(TE)`, or the sharp four-cycle theorem.
