# QP phase jets: a finite Bessel/inverse theorem and the major-arc cluster target

**Date:** 2026-08-25  
**Verdict:** there is a rigorous coefficient-uniform phase-jet dichotomy on
the actual discrete completion interval.  Off a graph of phase-jet major
arcs, first, second, or third finite differences bound every Gram entry;
`TT*` then gives a Bessel bound in terms of the maximum major-arc cluster.
Conversely, failure of that Bessel bound forces one packet to have a large
cluster of jet-resonant neighbors.

The nonlinear reciprocal action also has an exact rigidity theorem adapted
to the physical affine alias: its curvature jet
`(mathcal A'',mathcal A''',mathcal A'''')` recovers every regular stationary
mode up to left-right reflection, and the reflected actions differ by the
invisible integral affine phase `m*S`.  The fourth derivative is used only
to classify/track resonant cubic jets, not as a fourth-derivative
cancellation estimate.

At the worst QP endpoint, a natural block has length

```text
N=q^(1/3)=D^(11/16).
```

The optimal cubic-difference saving is `D^(-11/64)`.  This is strong enough
for the full `sqrt(A/B)=D^(-1/12)` operator gain by the very small margin
`D^(-1/192)`, and it exceeds the saving needed merely to repair the current
`D^(7/96)` deficit by `D^(-5/192)`.  Thus third-order jets are quantitatively
capable of closing the gap.

This does **not** yet prove the physical Bessel intertwining.  One must still
show that the nonlinear stationary actions satisfy the derivative
certificates outside the already classified algebraic major arcs, or prove
that the remaining jet-resonant clusters have the required bounded
multiplicity.  Integral affine wrap labels are exact aliases on integer
samples and form one coherent jet cluster; the theorem correctly does not
pretend that they are independent characters.  No sharp four-cycle bound is
claimed.

## 1. The arithmetic jet space is a quotient

Let

```text
I_N={0,1,...,N-1},             e(x)=exp(2*pi*i*x),
u_nu(s)=a_nu(s)e(phi_nu(s)),   ||u_nu||_2=1.          (1.1)
```

The packets are vectors in the finite space `ell^2(I_N)`.  There is no new
continuous character in this definition.

For integers `m_0,...,m_3`, put

```text
P(s)=sum_(0<=r<=3) m_r binom(s,r).                   (1.2)
```

This is integer-valued at every integer `s`, and hence

```text
e(phi(s)+P(s))=e(phi(s))                             (1.3)
```

sample by sample.  The correct cubic jet space is therefore the quotient by
the Newton lattice

```text
J_3=(real sampled phases)/(integer-valued degree <=3 polynomials). (1.4)
```

Equivalently, the four Newton coefficients are read modulo integers.  This
is not cosmetic.  The QP wrap label contributes an affine term `j*s` with
`j` integral, which is zero in `(1.4)`.

The hostile family

```text
phi_j(s)=j*s,       1<=j<=K,                         (1.5)
```

has very different real slopes but

```text
u_1=u_2=...=u_K,       ||Gram||=K.                   (1.6)
```

Thus any jet theorem formulated before taking the quotient `(1.4)` is
false.  Any useful separation of these labels must come from the nonlinear
stationary action left after the affine alias is removed.

## 2. Three genuinely discrete oscillation tests

Write `Delta f(s)=f(s+1)-f(s)`.  The following estimates concern finite
exponential sums over integer subintervals.  They may be applied after
subtracting any polynomial `(1.2)`, because that does not change the sum.

### Lemma 2.1 (finite phase-jet tests)

Let `J` be an integer interval of length at most `N` and let `f` be real on
the integer points needed below.

1. If `Delta f` has a monotone real lift contained in
   `[m+lambda,m+1-lambda]`, then

   ```text
   |sum_(s in J)e(f(s))| <<lambda^(-1).               (2.1)
   ```

2. If `Delta^2 f` has constant sign and

   ```text
   lambda<=|Delta^2 f|<=C_0*lambda<=1/4,             (2.2)
   ```

   then

   ```text
   |sum_(s in J)e(f(s))|
    <<_(C_0) N*sqrt(lambda)+lambda^(-1/2).            (2.3)
   ```

3. If `Delta^3 f` has constant sign and

   ```text
   lambda<=|Delta^3 f|<=C_0*lambda,                  (2.4)
   ```

   in the small-difference range, then

   ```text
   |sum_(s in J)e(f(s))|
    <<_(C_0) N*lambda^(1/6)+N^(1/2)*lambda^(-1/6).   (2.5)
   ```

The right sides may always be replaced by the trivial bound `N`.  If the
certificate holds after partitioning into `L` intervals, multiply the
corresponding bound by `L`.

#### Proof

For `(2.1)`, summation of the geometric increments, or the usual polygonal
proof, gives the discrete first-difference estimate.  It holds uniformly on
every subinterval.

For `(2.3)`, `Delta f` is monotone.  Delete the indices where its distance
to an integer is less than a parameter `delta`.  From `(2.2)`, the deleted
set and the number of integer crossings together cost

```text
O_(C_0)(N*delta+delta/lambda+N*lambda+1).            (2.6)
```

On the complementary monotone pieces, `(2.1)` and summation over the
crossings cost

```text
O_(C_0)((N*lambda+1)/delta).                         (2.7)
```

Take `delta=sqrt(lambda)` to obtain `(2.3)`.

For `(2.5)`, apply the exact finite van der Corput inequality with a shift
parameter `H`.  The phase

```text
f_h(s)=f(s+h)-f(s)                                  (2.8)
```

has

```text
Delta^2 f_h(s)=sum_(0<=r<h) Delta^3 f(s+r),          (2.9)
```

so `(2.3)` applies with scale `h*lambda`.  Consequently

```text
|sum e(f)|^2
 <<N^2/H+N^2*lambda^(1/2)*H^(1/2)
          +N*lambda^(-1/2)*H^(-1/2).                (2.10)
```

Choosing `H` comparable to `lambda^(-1/3)`, truncated to `[1,N]`, proves
`(2.5)` and the trivial fallback.  Everything in this proof is a finite sum
or a finite difference. `square`

After division by `N`, define the normalized envelopes

```text
rho_1(N,lambda)=min(1, 1/(N*lambda)),
rho_2(N,lambda)=min(1, sqrt(lambda)+1/(N*sqrt(lambda))),
rho_3(N,lambda)=min(1, lambda^(1/6)
                         +N^(-1/2)*lambda^(-1/6)).   (2.11)
```

The constants in `(2.11)` depend only on the comparability constant and the
number of derivative-monotonicity pieces.

When a physical stationary action has a smooth real interpolation, ordinary
derivatives certify these genuinely discrete hypotheses through the exact
identity

```text
Delta^r f(s)
 =integral_[0,1]^r f^(r)(s+t_1+...+t_r) dt_1...dt_r. (2.12)
```

Thus a constant-sign comparable ordinary derivative yields the corresponding
finite-difference certificate.  Equation `(2.12)` is only a verification
device; the packet vectors, their Gram matrix, and all averaging in Theorem
4.1 remain on the integer completion set.

## 3. Amplitudes pass through by finite Abel summation

For a pair of packets set

```text
b_(nu,mu)(s)=a_nu(s)*conj(a_mu(s)),
V(b)=|b(N-1)|+sum_(s<N-1)|b(s+1)-b(s)|.             (3.1)
```

Finite Abel summation gives, exactly,

```text
|sum_s b(s)e(f(s))|
 <=V(b)*max_(J subset I_N)|sum_(s in J)e(f(s))|.    (3.2)
```

Thus if `V(b)<=V_0/N`, a derivative certificate with normalized envelope
`rho` implies

```text
|<u_nu,u_mu>|<<V_0*rho.                              (3.3)
```

Flat normalized packets have `V_0=1`.  Smooth cutoffs and a bounded number
of stationary charts cost only their finite variation and chart count.  No
sign condition on the synthesis coefficients is used.

## 4. Phase-jet Bessel/inverse theorem

Fix `0<=eta<1`.  Join `nu` and `mu` in the jet-major-arc graph if their
phase difference, after the Newton quotient `(1.4)`, has not been supplied
with a certificate from Section 2 strong enough to prove

```text
|<u_nu,u_mu>|<=eta.                                  (4.1)
```

Let `K` be the number of packets and `Delta_eta` the maximum degree of this
graph.

### Theorem 4.1 (finite phase-jet Bessel dichotomy)

For arbitrary complex coefficients `c_nu`, one has

```text
||sum_nu c_nu*u_nu||_2^2
 <=[1+Delta_eta+eta*(K-1-Delta_eta)]
   *sum_nu |c_nu|^2.                                (4.2)
```

Conversely, if the squared Bessel quotient is `L`, then

```text
Delta_eta
 >=(L-1-eta*(K-1))/(1-eta).                         (4.3)
```

In particular, a failure at level `L` forces one packet to have at least
the ceiling of the right side of `(4.3)` jet-major-arc neighbors.

#### Proof

The Gram matrix has diagonal one.  In each row, at most `Delta_eta` entries
are major-arc entries and have absolute value at most one; every other entry
has absolute value at most `eta` by `(3.3)`.  The absolute row sum is the
right side of `(4.2)`.  Schur's test proves `(4.2)` for arbitrary
coefficients.  Solving `(4.2)` for `Delta_eta` proves `(4.3)`. `square`

The inverse conclusion is initially a large star rather than a clique.  If
the derivative failures are encoded as balls in the quotient jet metric,
the neighbors lie in a ball around the central packet and hence have twice
the stated mutual jet diameter.  No graph regularity or positivity is
assumed.

There is also a useful nonuniform form: retain the actual certified bounds
`eta_(nu,mu)` off the major arcs and use

```text
||T||^2<=1+max_nu[
 #E(nu)+sum_(mu notin E(nu),mu!=nu) eta_(nu,mu)].    (4.4)
```

This is the strongest automatic conclusion of pairwise phase-jet estimates;
any improvement over `(4.4)` would need cancellation inside the Gram rows,
not merely van der Corput.

## 5. Exact endpoint ledger

At the worst anisotropic endpoint,

```text
A=D,                 B=D^(7/6).                     (5.1)
```

Think of `K<<B*D^o(1)` as the wide packet multiplicity.  The full
anisotropic target is a Bessel norm `sqrt(A)` rather than `sqrt(B)`.  By
`(4.2)`, it is enough that

```text
eta<=A/B=D^(-1/6),       Delta_eta<<A*D^o(1).        (5.2)
```

This is exactly the pair-correlation and major-arc multiplicity split that
the proposed phase-jet/inverse strategy must prove.

There is a weaker threshold sufficient for the present numerical gap.  The
flattened no-wrap ledger is `D^(55/96)` and needs an operator saving
`D^(-7/96)`.  Since pair correlations enter under a square root, take

```text
eta=D^(-7/48).                                      (5.3)
```

Then

```text
B*eta=D^(49/48),                                    (5.4)
```

so `(4.2)` repairs the `D^(7/96)` deficit provided

```text
Delta_eta<<D^(49/48+o(1)).                           (5.5)
```

The full `sqrt(A/B)` theorem asks for the stronger cluster ceiling `D`, but
the currently missing power only asks for `(5.5)`.

Now take a natural local completion block

```text
N=q^(1/3)=D^(11/16).                                (5.6)
```

Write `lambda=D^(-t)`.  The exact saving exponents read from `(2.11)` are

```text
order 1:  11/16-t,
order 2:  min(t/2,11/16-t/2),
order 3:  min(t/6,11/32-t/6).                       (5.7)
```

The useful derivative ranges are:

| test | for full pair saving `D^(-1/6)` | for closing saving `D^(-7/48)` |
|---|---:|---:|
| first difference | `0<=t<=25/48` | `0<=t<=13/24` |
| second difference | `1/3<=t<=25/24` | `7/24<=t<=13/12` |
| third difference | `1<=t<=17/16` | `7/8<=t<=19/16` |

The cubic envelope is optimized at

```text
t=33/32,       rho_3=D^(-11/64).                    (5.8)
```

Therefore

```text
11/64-1/6 =1/192,       11/64-7/48=5/192.           (5.9)
```

This is the central quantitative finding: cubic jets on a full `q^(1/3)`
block are just strong enough even for the full anisotropic theorem.  A
polynomial shortening of the block can consume the small first margin, so
the physical stationary partition must preserve essentially the complete
block or compensate with a stronger first/second-difference certificate.

## 6. Exact rigidity of the nonlinear stationary-action three-jet

There is a second exact theorem, specific to the physical reciprocal phase,
which explains why order three is the correct stopping point.  Consider

```text
F(a,S)=C*(h/a+k/(S-a))-m*a                          (6.1)
```

and an interior stationary branch `a=a(S)`.  Put `b=S-a` and

```text
u=C*h/a^2,       v=C*k/b^2,       w=u*b+v*a.        (6.2)
```

The stationary equation and nondegeneracy are exactly

```text
m=v-u,                 F_(aa)=2*w/(a*b)!=0.         (6.3)
```

Let

```text
mathcal A(S)=F(a(S),S)                               (6.4)
```

be the nonlinear stationary action.

### Theorem 6.1 (regular stationary actions are three-jet rigid)

Assume

```text
a*b*u*v*m*w!=0.                                     (6.5)
```

At fixed `(C,S)`, the three numbers

```text
(mathcal A',mathcal A'',mathcal A''')               (6.6)
```

recover `a,h,k,m` uniquely.

#### Proof

Implicit differentiation of `F_a=0` first gives

```text
a'=v*a/w,       b'=u*b/w,       u'=v'=-2*u*v/w.     (6.7)
```

The envelope identity and one further differentiation then give

```text
mathcal A'  =-v,
mathcal A'' = 2*u*v/w,
mathcal A'''=-6*u*v*(u^2*b+v^2*a)/w^3.              (6.8)
```

Write these three derivatives as `(P_1,P_2,P_3)`.  Set

```text
v=-P_1,
rho=-2*v*P_3/(3*P_2^2).                             (6.9)
```

Using

```text
u^2*b+v^2*a=w*(u+v)-u*v*S                           (6.10)
```

in `(6.8)` gives

```text
rho=(u+v-P_2*S/2)/u,
u=(v-P_2*S/2)/(rho-1).                              (6.11)
```

The denominator is nonzero: in fact

```text
rho-1=v*a*m/(u*w).                                  (6.12)
```

Finally,

```text
w=2*u*v/P_2,
a=(w-u*S)/(v-u),       b=S-a,
h=u*a^2/C,             k=v*b^2/C,
m=v-u.                                             (6.13)
```

These are explicit inverse formulas. `square`

The reconstruction fails only on transparent stationary singularities:

```text
h=0,       k=0,       m=0,       or w=0.            (6.14)
```

The first two are one-inverse axes.  The last is the cubic fold.  The
positive zero-dual locus `m=0` is genuinely noninjective, rather than a
removable denominator: there

```text
mathcal A(S)=C*(sqrt(h)+sqrt(k))^2/S,                (6.15)
```

so `(h,k)` and `(k,h)` have the same action for every `S`.  Thus the exact
singular set of the three-jet map is precisely the geometric major-arc set
already isolated by the primal and dual analyses.

Theorem 6.1 is stronger than a dimension count: away from `(6.14)`, two
stationary modes with the same lifted nonlinear three-jet are the same mode.
It does not by itself count *near* coincidences modulo the integer Newton
lattice.  The inverse formulas show exactly where quantitative conditioning
can be lost--through small `u`, `v`, `m`, or `w`--and therefore identify the
correct variables for that remaining Diophantine count.

The appearance of `mathcal A'` in Theorem 6.1 means that one must first
choose an affine Newton lift.  There is a stronger formulation intrinsic to
the **physical affine-alias quotient** which explains the exact reflection
collision.

### Theorem 6.2 (affine-quotient-compatible curvature-jet rigidity)

Put

```text
q_j=mathcal A^(j)(S),       t=a/S,       alpha=a'(S),
J=-S*q_3/(3*q_2),
K=S^2*q_4/(3*q_2),
R=alpha*(1-alpha)/(t*(1-t)).                        (6.16)
```

Then exactly

```text
J=1+(alpha-t)^2/(t*(1-t)),
K=4*J^2-5*R*(J-1).                                  (6.17)
```

If `m!=0`, the curvature jet `(q_2,q_3,q_4)` determines the stationary mode
up to the simultaneous reflection

```text
(a,h,k,m) ->(S-a,k,h,-m).                           (6.18)
```

The two reflected actions differ by exactly the affine phase `m*S`, so for
integral Poisson frequency they are the same element of the Newton quotient.

#### Proof

Equations `(6.7)--(6.8)` and one more differentiation give `(6.17)` by
direct cancellation.  For the inverse, set

```text
omega=J-1,       R=(4*J^2-K)/(5*omega),
L=1-R-omega,     x=2*t-1,       y=2*alpha-1.        (6.19)
```

Since

```text
omega=(y-x)^2/(1-x^2),
R=(1-y^2)/(1-x^2),
L=2*x*(y-x)/(1-x^2),                                (6.20)
```

one obtains, when `L!=0`,

```text
x^2=L^2/(L^2+4*omega),
y=x*(L+2*omega)/L.                                  (6.21)
```

The two signs of `x` give precisely the simultaneous reflection
`(x,y)->(-x,-y)`.  If `L=0` and `m!=0`, then `x=0` and

```text
y^2=omega,                                           (6.22)
```

again leaving only reflection.  Indeed, the other formal possibility
`y=x` is equivalent to `alpha=t`, hence to `m=0`.

Finally `q_2` recovers the scaled frequencies in `(6.2)`:

```text
u=q_2*S*t/(2*alpha),
v=q_2*S*(1-t)/(2*(1-alpha)).                        (6.23)
```

Equations `(6.3)` and `(6.13)` then recover `h,k,m`.  Direct substitution
shows that the action of the reflected mode is `mathcal A(S)+m*S`, proving
the quotient assertion. `square`

Theorem 6.2 uses `q_4` only for inverse classification; the cancellation
theorem still uses finite differences only through order three.  In a
physical proof, `q_4` controls how a nearly resonant cubic jet moves across
the block.  No fourth-derivative van der Corput estimate, and therefore no
new exponent loss, is being inserted.  A hypothetical integral quadratic or
cubic Newton alias would still require a choice of higher lift (or would stay
in the major-arc graph); `(6.16)--(6.23)` are exactly invariant under the
affine alias that actually produces the reflected QP collision.

## 7. What the inverse theorem asks the arithmetic to classify

Apply `(4.3)` to the physical stationary packets after removing their
integer affine Newton aliases.

* If the full `sqrt(A)` Bessel conclusion fails, there must be a packet with
  `D^(1+o(1))` or more neighbors for which all supplied first-, second-, and
  third-difference certificates fail at correlation scale `D^(-1/6)`.

* If only the saving needed to close the current `D^(7/96)` gap fails, there
  must be a packet with `D^(49/48+o(1))` or more neighbors at scale
  `D^(-7/48)`.

These are phase-jet major-arc clusters.  The intended arithmetic inverse
theorem would show that a cluster of this size forces one of the already
peeled structures

```text
z=0,       z=d*v,       z=-d*v,       or d^2|g.      (7.1)
```

or its reflected central-content counterpart.  Those structures have
already been counted far below the thresholds above.  What is not yet proved
is that `(7.1)` exhausts the large *near*-clusters of **nonlinear stationary
actions**.  Theorem 6.1 proves the corresponding exact, nonresonant
injectivity statement.

Failure of a derivative certificate need not mean that all real derivatives
are small.  A derivative can cross an integer frequently, or sit on a
rational major arc.  Such pairs correctly remain in the graph for the
arithmetic classification.  Calling every large real derivative
"oscillatory" would repeat the wrap-label error exposed by `(1.5)`.

## 8. The remaining physical theorem

For each stationary residue layer, let `Psi_ell(S)` denote the actual
completion packet after its affine Poisson alias is removed.  A sufficient
route to the desired result is now precise:

1. work on integer `S`-blocks of length `q^(1/3-o(1))` and prove a uniform
   finite-variation bound for every cross-amplitude;
2. for every pair outside the classified algebraic major arcs, verify on a
   bounded partition one of the difference conditions `(2.1)`, `(2.2)`, or
   `(2.4)` with the ranges in Section 5;
3. alternatively, prove directly that each unresolved jet-major-arc
   neighborhood has at most `D^(49/48+o(1))` members (enough to close the
   current gap), ideally at most `D^(1+o(1))` members (the full anisotropic
   theorem);
4. apply Theorem 4.1.  Its conclusion is uniform for arbitrary complex
   coefficients, so no later hereditary-weight step is lost.

This is a genuine combination of a phase-jet large sieve and a
coherence-to-major-arc inverse theorem.  The analytic half is proved here;
the QP-specific classification of large nonlinear-action near-jet clusters is the
remaining new mathematics.

## 9. Reproducibility and status

The finite Newton quotient, Gram/Schur audit, exact inverse floor, and all
endpoint exponent windows are implemented in

```text
src/qp_phase_jet_bessel_inverse.py
src/test_qp_phase_jet_bessel_inverse.py
```

Thirteen focused tests verify the identities, the exact affine-alias
counterfamily, finite Fourier orthogonality, the inverse-cluster floor, all
exponent margins, stationary-action reconstruction, its zero-dual
noninjectivity, the quotient-compatible reflection, central reconstruction,
and the cubic-fold singularity.

```text
finite first/second/third difference envelopes:       PROVED;
finite Abel transfer for stationary amplitudes:        PROVED;
coefficient-uniform TT*/Schur Bessel theorem:           PROVED;
inverse large-jet-cluster theorem:                      PROVED;
integer Newton quotient is necessary:                  PROVED;
cubic q^(1/3) scale is numerically sufficient:          PROVED;
regular stationary-action three-jet injectivity:        PROVED;
affine-quotient curvature rigidity up to reflection:    PROVED;
lifted q1--q3 singular set = known geometric arcs:      PROVED;
nonlinear stationary-action derivative certificates:   OPEN;
large nonlinear near-jet cluster => classified axes:    OPEN;
physical completion-sum Bessel intertwining:            OPEN;
sharp four-cycle bound:                                 NOT PROVED.
```
