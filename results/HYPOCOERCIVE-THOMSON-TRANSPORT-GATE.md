# Hypocoercive and signed Thomson transport gate

Status: exact completed cutoff-Dirac gate, best-case arithmetic dilation
closure, exact factor-ratio audit, positive Thomson incidence reduction, and
finite diagnostics; 2026-08-06.  The natural versions of both proposed
global transports are closed as independent cancellation mechanisms.  This
note does **not** prove or disprove the Riemann Hypothesis.

## 1. Verdict

R74 proved that every finite Vaughan cutoff has the same Laurent principal
part at a zeta zero.  A nonreversible lift might nevertheless have worked if
a skew arithmetic transport rotated that cutoff-common mode into directions
where a positive dissipator acts.  A signed electrical-flow formulation
might also have retained Mobius cancellation before taking a norm.  We tested
the strongest honest finite versions of both ideas.

1. The exact completed cutoff lift has a canonical hypocoercive Dirac form.
   Its bracket controls only cutoff differences.  The entire cutoff-constant
   field, including every symbolic off-line exponential, is in its **exact**
   kernel.  With the exact Type-I head the arithmetic source is zero; with
   the explicit R71 center it is precisely the already-controlled Euler
   defect.
2. The canonical scale-average decomposition is commuting, so iterated
   brackets do not improve its low-frequency gap.  The gap remains quadratic
   and finite-volume scale transport has the familiar `L^(-2)` collapse.
3. The factor-ratio twist is genuinely noncommuting on a distinct semiprime
   fiber.  Its bracket gap is exactly

   ```text
   t^2 log(q/p)^2.                                       (1.1)
   ```

   It vanishes on `p^2`, on every singleton assignment fiber, at `t=0`, and
   along near-square semiprimes.  More importantly, it is the R72 Ward
   anisotropy channel, not the physical phase of the complete grouped Vaughan
   field.  Promoting it to the full state drops or reclassifies the unequal
   products and center.
4. Even granting independent control of every available one-prime dilation
   in the three Vaughan coordinates `d,b,m`, the finite controllability
   closure has a large exact kernel.  In the first R73 countermodel, `97.276%`
   of the active arithmetic vector and `100%` of its grouped coherent part
   remain uncontrolled.
5. The natural positive Thomson network realizes the ungrouped Vaughan tail
   exactly, but its Laplacian is invariant under flipping any Mobius-oriented
   edge.  Its minimization separates over total products and returns only a
   reweighted atomic diagonal.  Parallel factorization paths give at most a
   divisor-multiplicity gain `exp(o(R))`, never a fixed exponential saving.
6. Restoring unequal products and the rank-two center turns the incidence
   Gram matrix back into the full R73/R71 energy.  In Mellin coordinates the
   tail symbol has the same cutoff-independent residue `-m_rho` at every zeta
   zero.  A useful completed resistance or spectral-gap bound is therefore
   the open two-shift theorem, not a cheaper graph lemma.

Thus the proposed workaround was worth testing, but it does not pass its
fail-fast gates.  What survives is the direct global large-value/joint-
dispersion route, not a local or graph-theoretic contraction.

## 2. Exact completed cutoff-Dirac gate

Use one common terminal quadrature `(R_i,w_i)` for `K` consecutive cutoffs.
For each finite cutoff `Y`, let

```text
f_Y^app=B_Y-Z_Y^app=C_full+E_Y,                          (2.1)
f_Y^ex =B_Y-Z_Y^ex =C_full.                              (2.2)
```

Here `B_Y` is the complete grouped tail, `Z_Y^app` is the explicit R71
rank-two center, `E_Y` is its Euler evaluation defect, and `Z_Y^ex` retains
the unevaluated Type-I head.  Whiten every field by `W^(1/2)` with
`W=diag(w_i)`.

Let `D` be the path incidence on the cutoff index and put

```text
mathcal D=D tensor I,

S_c = [0  0],       A_c = [0          -mathcal D*].      (2.3)
      [0  I]             [mathcal D    0         ]
```

Then `S_c>=0` and `A_c*=-A_c`.  For a physical vertex state `X=(v,0)`,

```text
(S_c+A_c)X=(0,mathcal D v).                              (2.4)
```

Consequently

```text
mathcal D f^ex =0,
mathcal D f^app=mathcal D E.                             (2.5)
```

The order-one controllability Gram is exactly

```text
B_1=S_c+A_c S_c A_c*
   =diag(mathcal D*mathcal D,I).                         (2.6)
```

Therefore

```text
ker(B_1)={(1_K tensor g,0):g arbitrary}.                 (2.7)
```

Every sampled exponential character

```text
(1_K tensor W^(1/2)e^(sR_i),0)                           (2.8)
```

is killed exactly, including `s=rho-1/2`.  Higher brackets cannot change
this because both `S_c` and `A_c` already annihilate (2.8).

The diagnostic uses `X=25`, `Y=2,3`, `h=.04`, `j=m=1` and a common
32-node quadrature.  It reports

```text
skew error                         0
bracket nullity                   32
exact-head cutoff difference       0
explicit-center cutoff difference  0.08346041380795877
Euler-defect cutoff difference      0.08346041380795878
source identity error              1.52e-17
symbolic carrier residual          0.                         (2.9)
```

This is an exact mechanism no-go up to floating evaluation of the explicit
center: the hypocoercive lift dissipates the cutoff defect and preserves the
quantity whose size is unknown.

## 3. Scale transport is commuting

For the order-`m` Markov average `Q=P_h^m`, the canonical decomposition is

```text
S_h=I-(Q+Q*)/2,
A_h=(Q*-Q)/2,
I-Q=S_h+A_h.                                             (3.1)
```

The exact innovation dissipator can instead be taken as

```text
S_inv=I-Q*Q.                                             (3.2)
```

On a Fourier mode with `q(t)=a_h(it)^m`, both choices are scalar.  Hence
`[S,A]=0` and every bracket has the same null set as `S`.  Near zero,

```text
1-|q(t)|^2  ~ m h^2 t^2/12,
|Im q(t)|   ~ m h |t|/2.                                (3.3)
```

There is damping but no hypocoercive transfer to another arithmetic
channel.  On a block of length `L`, the smallest scale frequency gives a
gap of order `L^(-2)`.

The R71 center cannot be appended as two artificial skew nodes.  Scale
differentiation on

```text
span(e^(R/2),R e^(R/2))
```

has coefficient matrix

```text
C=[1/2  1].                                              (3.4)
  [0   1/2]
```

Its real trace already excludes skew-adjointness in a positive metric.
After critical conjugation, `C-I/2` is a nonzero nilpotent Jordan block,
whereas a positive-metric skew operator is diagonalizable.  A full-center
hypocoercive model therefore needs a derived drift/source equation; merely
attaching two center coordinates is not legitimate.

## 4. The one noncommuting local bracket

On a fixed product `n`, let

```text
Omega_n={(d,b,m):dbm=n, d,b>Y, mu(d)Lambda(b)!=0},
P_n=projection onto constants,
S_n=I-P_n,
A_(n,t)=it diag_(Omega_n) log(d/b).                       (4.1)
```

For the normalized constant vector `u_n`,

```text
<u_n,B_1 u_n>
 =t^2 Var_(Omega_n)(log(d/b)).                            (4.2)
```

At `n=pq`, `p<q`, put `a=log(q/p)`.  In the constant/odd basis,

```text
S=[0 0],       A=-ita[0 1],       B_1=[t^2 a^2 0].       (4.3)
  [0 1]              [1 0]             [0       1]
```

The asymptotic decay gap of `S+A` is

```text
lambda(t,a)=
 (1-sqrt(1-4t^2a^2))/2,  2|ta|<1,
 1/2,                    2|ta|>=1.                       (4.4)
```

Thus `lambda~t^2a^2`.  At the first critical ordinate, the closest
consecutive-prime ratios in the upper half of four finite ranges give

```text
limit       pair          log(q/p)       lambda
100         71,73         2.77796e-2     1.90451e-1
1,000       881,883       2.26757e-3     1.02836e-3
10,000      9929,9931     2.01410e-4     8.10475e-6
100,000     99989,99991   2.00020e-5     7.99322e-8.      (4.5)
```

The actual Vaughan coefficient vector becomes almost entirely coherent as
`q/p->1`.  The PNT gives consecutive prime ratios tending to one, so (4.4)
has no uniform gap for any fixed `t`.  At `p^2`, the assignment fiber is the
singleton `(p,p,1)` and

```text
S=A=B_r=0                                                 (4.6)
```

for every bracket order.

There is a more fundamental completion issue.  The physical Mellin phase on
a grouped fixed-product fiber is

```text
n^(-it),
```

whose generator is `it log(n) I` and commutes with `S_n`.  The ratio phase in
(4.1) is exact only in the Ward connected channel

```text
2 log(p)log(q) cos(t log(p/q)).                           (4.7)
```

That is the already-audited anisotropy term.  It is not an operator on the
full completed Vaughan field.  A proof using (4.2) still needs an exact
forcing equation that restores every unequal-product and center term; that
forcing is the missing two-shift estimate.

## 5. Best-case coordinate-dilation closure

To give a different arithmetic skew transport every advantage, retain all
pre-grouping states

```text
V_(Y,N)={(n,d,b,m):n=dbm<=N, d,b>Y,
         mu(d)Lambda(b)!=0}.                             (5.1)
```

On each total-product fiber use the complete-graph projection `S_n=I-P_n`,
the strongest normalized reversible assignment dissipation.  Add every
available skew edge obtained by multiplying exactly one of `d,b,m` by one
prime, with weight `log p`.

Rather than select one favorable linear combination `A`, close `row(S)`
under **every edge generator independently**:

```text
R_0=row(S),
R_(j+1)=span(R_j,{R_j A_e:e an arithmetic edge}).         (5.2)
```

The saturated space contains the bracket row space of every word in these
edge generators.  A vector orthogonal to it is uncontrolled by the entire
transport topology.

The complete finite results are

```text
X    Y   N    states fibers edges  closure ranks  nullity
59   4   64   17     14     3      3,4,5          12
205  7   214  45     36     11     9,13,17        28.    (5.3)
```

On the active R71 vector the uncontrolled squared fractions are

```text
X=59:   raw 0.9727601209, grouped-coherent 1.0000000000,
X=205:  raw 0.9327305341, grouped-coherent 0.9927912943.  (5.4)
```

This closes prime dilation in the existing `d,b,m` topology.  It does not
prove that no imaginable skew coupling exists.  A new proposal must derive
its cross-product edges coefficient-for-coefficient from an exact completed
identity; an expander inserted by hand has no bearing on R71.

## 6. Positive Thomson incidence forgets Mobius signs

For a finite arithmetic function `f`, let `C_f` be truncated Dirichlet
convolution,

```text
(C_f x)(n)=sum_(d|n) f(d)x(n/d).                          (6.1)
```

The divisor-poset zeta and Mobius matrices are

```text
Z=C_1,       M=C_mu,       MZ=ZM=I.                      (6.2)
```

The exact tail operator is

```text
T_Y=C_(mu_>Y) C_(Lambda_>Y) Z,                           (6.3)
```

and `T_Y e_1=a_Y`.  With

```text
H_Y=C_(mu_<=Y)C_log+C_(Lambda_<=Y)
    -C_(mu_<=Y)C_(Lambda_<=Y)Z,                          (6.4)
```

one has the full operator identity

```text
T_Y+H_Y=C_Lambda.                                       (6.5)
```

There is a genuine positive graph realization.  For every assignment
`e=(d,b,m)`, connect a sink to `n=dbm`, orient the edge by `sign(mu(d))`, and
give it current

```text
j_e=|mu(d)|Lambda(b)/sqrt(dbm).                          (6.6)
```

Then the product divergence is exactly

```text
c_n=a_Y(n)/sqrt(n).                                     (6.7)
```

For any positive diagonal conductances `kappa_e`, Thomson minimization gives

```text
min_(Bj=c) sum_e |j_e|^2/kappa_e
 =sum_n |c_n|^2/K_n,
K_n=sum_(e:product(e)=n) kappa_e.                        (6.8)
```

The reason is structural.  Reversing a Mobius-oriented column of `B` leaves

```text
B diag(kappa) B*                                        (6.9)
```

unchanged.  Positive conductance remembers parallel-path multiplicity but
forgets every sign.  Signed conductances retain signs only by destroying
positivity; their circulation energy can be unbounded below.

At `N=30,Y=2`, the diagnostic verifies (6.2)--(6.8) and reports

```text
assignments                         20
max Mobius-inverse error             0
tail regrouping error                0
Vaughan operator completion error    3.33e-16
divergence error                     0
orientation-Laplacian error          0
canonical critical flow energy       1.34658720949
minimum Thomson energy               0.880157534460
pseudoinverse energy                 0.880157534460
grouped coefficient L2               1.44805153353.       (6.10)
```

Since the number of assignments over one product is at most `tau_3(n)`, the
best parallel-path gain for `n~exp(R)` is `exp(o(R))`.  It cannot yield the
required `exp(-2 eta R)`.

## 7. Mellin obstruction and completion collapse

For `chi_s(n)=n^(-s)`, finite transpose convolution gives

```text
(C_f* chi_s)(m)
 =chi_s(m) sum_(d<=N/m) f(d)d^(-s).                      (7.1)
```

In the convergent infinite model,

```text
Z*chi_s=zeta(s)chi_s,
M*chi_s=zeta(s)^(-1)chi_s.                              (7.2)
```

The free cofactor is exactly the `zeta(s)` factor.  The tail symbol is

```text
A_Y(s)
 =(1-zeta(s)M_Y(s))
  [-zeta'(s)/zeta(s)-L_Y(s)].                            (7.3)
```

At a zero `rho` of multiplicity `m_rho`, every finite cutoff satisfies

```text
A_Y(s)=-m_rho/(s-rho)+O(1).                              (7.4)
```

At the first zeta zero and `s=rho+10^(-6)`, the finite check gives

```text
Y     (s-rho)A_Y(s), real part
1     -0.99999881
2     -0.99999781
3     -0.99999675
5     -0.99999619
10    -0.99999525.                                      (7.5)
```

Thus the graph formulation has not altered the carrier.  If cross-product
conductances and the R71 center are added coefficient-for-coefficient, the
analysis map becomes the complete field map and its Gram expansion is the
full two-shift energy.  A fixed completed resistance bound is then the open

```text
X_(I,U,V)<=exp((1-2eta+o(1))R),                          (7.6)
```

not a consequence of Thomson's principle.

## 8. Reproducibility and research consequence

The executable diagnostic is
[`src/hypocoercive_thomson_probe.py`](../src/hypocoercive_thomson_probe.py),
with focused tests in
[`src/test_hypocoercive_thomson_probe.py`](../src/test_hypocoercive_thomson_probe.py).

Run

```text
python3 src/hypocoercive_thomson_probe.py
python3 -m pytest -q src/test_hypocoercive_thomson_probe.py
```

Any revival must pass all of the following gates.

1. State an exact completed equation `(S+A)X=F` including unequal products,
   the Euler defect, and the rank-two center.
2. Prove `S>=0` and `A*=-A` in the actual weighted metric.
3. Show that `F` contains only independently controlled boundary/Euler data,
   not the grouped field or original energy.
4. Test every symbolic exponential `e^(sR)` and every fixed-product constant;
   a bracket that kills them has deleted the RH carrier.
5. Track the Mellin symbol without using `1/zeta`, analytic continuation of a
   finite polynomial, or zero locations.
6. Obtain a gap whose accumulated logarithmic-scale decay is `eta R+o(R)`.
   A vanishing local gap yields only subpower cooling.

The two off-wall candidates have therefore done useful work: they identify
exactly where a new mechanism would have to be global.  But neither supplies
that mechanism.  The remaining credible route is to make one hypothetical
off-line zero force a resolvable large-value set and then prove that the
complete Mobius-specific polynomial has exceptional measure smaller than one
such peak.  That is a direct global theorem and should be recognized as the
next hard target.  Its sharp minimum-width and current-large-value audit is
carried out in
[`MINIMUM-WIDTH-LARGE-VALUE-GATE.md`](MINIMUM-WIDTH-LARGE-VALUE-GATE.md).
