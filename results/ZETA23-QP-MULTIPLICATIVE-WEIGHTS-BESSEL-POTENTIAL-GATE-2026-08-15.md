# QP multiplicative weights: exact Bessel potential and the all-order gate

**Date:** 2026-08-15  
**Verdict:** multiplicative weights does not prove the fixed-power
actual-prime QP-KILL from the available tent, KMT, Guth--Maynard, or
Heath--Brown estimates.  The method gives an exact algorithmic reformulation,
but its missing lower bound is asymptotically equivalent to the original
actual-node minimax statement.

There is no hidden cancellation in the normalization.  Dividing each Gibbs
factor by `I_0(eta)` removes the harmless Haar diagonal of size
`K eta^2/4`.  The exact Bessel expansion still has total positive coefficient
mass

```text
(exp(eta)/I_0(eta))^K=exp[eta K+O(eta^2 K)],          (0.1)
```

and its first harmonic is already critical when

```text
K asyp epsilon^(-2),                 eta asyp epsilon. (0.2)
```

The unconditional tent floor controls (0.1) only while

```text
eta K << log(1/delta_VK),                              (0.3)
```

whereas a potential drop of constant size requires

```text
eta K asyp 1/epsilon.                                  (0.4)
```

For `epsilon=Y^(-c)`, every fixed `c>0`,

```text
epsilon log(1/delta_VK)=o(1).                          (0.5)
```

Thus (0.3) ends before the potential has moved by even `o(1)`.  KMT is
weaker.  Guth--Maynard improves the first-harmonic absolute ledger exactly to
the critical scale `eta sqrt(K)`, not below it.  Heath--Brown leaves the same
repeated-difference direction already isolated in the square-reweighting
audit.

An exact compact-group model makes this sharp: every fixed-degree Fourier
character has the ideal `R^(-D/2)` decay and the shifted square ledger is
`O(1)`, yet every positive reweighting leaves one of `R` moments at most
`-R^(-1/2)`.  Its `I_0`-normalized Bessel partition has a nontrivial truncated
Gaussian limit rather than tending to one.  This is a no-go for the stated
black-box proof package, not a counterexample on the actual prime-power
nodes.  The actual fixed-power QP-KILL remains open.

---

## 1. The exact continuum multiplicative-weights algorithm

Let `u_1,...,u_M in (0,w]`, `w=1/5`, be the distinct actual prime-power
nodes, put

```text
X_t(j)=cos(t u_j),              H=[Y^.01,Y^(50/33)], (1.1)
```

and start from a probability `mu_j>0`.  The smooth tent rule can be made
strictly positive with a negligible uniform regularization

```text
mu=(1-tau)mu_tent+tau mu_unif,        tau=Y^(-10).    (1.2)
```

This changes every antenna value by at most `tau`, retains the tent floor,
and gives `log(1/min_j mu_j)=O(log Y)` because `M=Y^(1+o(1))`.

At stage `k`, if

```text
m_k=sum_j p_(k-1,j) X_(t_k)(j)<-epsilon              (1.3)
```

at a minimizing `t_k in H`, update

```text
p_(k,j)=p_(k-1,j) exp(eta X_(t_k)(j))/z_k,
z_k=sum_j p_(k-1,j)exp(eta X_(t_k)(j)).               (1.4)
```

The minimizer exists because the finite cosine polynomial is continuous on
the compact interval `H`.  If no `t_k` satisfies (1.3), the current `p` is a
legal **all-height** positive antenna with floor `-epsilon`; no discretization
has been hidden.  For a finite checker, the derivative bound

```text
|d/dt sum_j p_j cos(tu_j)|<=w                         (1.5)
```

spends at most `w Delta/2` on a grid of mesh `Delta`.

After `K` unsuccessful stages, put

```text
F_K(j)=sum_(k<=K)X_(t_k)(j),
Z_K=sum_j mu_j exp(eta F_K(j)).                       (1.6)
```

Telescoping gives the exact identity

```text
Z_K=product_(k<=K) z_k.                               (1.7)
```

Hoeffding's lemma for a variable in `[-1,1]` yields

```text
log Z_K<=K[-eta epsilon+eta^2/2].                    (1.8)
```

On the other hand, if `nu_K=K^(-1)sum_k delta_(t_k)`, then

```text
Z_K>=min_j(mu_j)
     exp[eta K max_j int_H cos(tu_j)dnu_K(t)].       (1.9)
```

Consequently a run of `K` violations constructs the exact orthant witness

```text
max_j int_H cos(tu_j)dnu_K(t)
 <=-epsilon+eta/2+log(1/min mu_j)/(eta K).           (1.10)
```

For example, `eta=epsilon/2` and

```text
K>=8 epsilon^(-2)log(1/min mu_j)                     (1.11)
```

make the right side at most `-epsilon/2`.

Equations (1.3)--(1.11) are a useful finite dichotomy:

```text
termination:       a positive actual-node antenna at floor -epsilon;
nontermination:    a probability on actual heights whose every node
                   transform is at most -epsilon/2.                 (1.12)
```

The second branch obstructs the positive-coefficient antenna.  It is not, by
itself, the exact uniform-ray antipode required by the full signed QP
promotion, so (1.12) must not be advertised as a proof of QP-PROMOTE.

### There is no free orthant-to-ray equalization

Write

```text
P=conv{a(t):t in H}.                                  (1.13)
```

The second branch of (1.12) proves only

```text
P intersects {x:x_j<=-epsilon/2 for every j}.         (1.14)
```

Full promotion asks instead for

```text
-r q_0 in P.                                         (1.15)
```

A convex set is not generally order-closed: already the singleton
`{(-2r,-r)}` meets the depth-`r` negative orthant and misses the radial line
at depth `r`.  Nothing in compact minimax changes this geometry.

Even illegally adjoining `t=0` does not repair it.  Mixing the witness with
`delta_0` changes its coordinate vector to

```text
alpha q_0+(1-alpha)z,                                (1.16)
```

whose unequal coordinates remain unequal.  One can formally null coordinate
`j` by convolving with

```text
[a_j delta_0+(1-a_j)nu],
a_j=-z_j/(1-z_j),                                    (1.17)
```

and then convolving all `M` factors.  But this expands support to sums of up
to `M` legal heights, fills the forbidden low gap, and pays an uncontrolled
product of `M` central masses.  It is the already-audited exponential
Bernoulli nuller, not a depth-preserving equalization lemma.  Therefore no
legal radial PROMOTE conclusion follows from (1.10).

On the fixed `d=33/50` ledger, positive KILL needs an exponent
`c>kappa_max=.018746369714728765...`, while full promotion needs depth
`Y^(-kappa_min+eta_0)` with
`kappa_min=.018030323424358778...`.  The exponents have a genuine gap.  A
same-scale algorithmic dichotomy cannot guarantee either architecture-wide
outcome: choosing `c>kappa_max` makes the orthant witness too shallow for the
promotion bill, while choosing `c<kappa_min` makes the terminating positive
antenna too weak for the KILL bill.

---

## 2. A potential lower bound of the needed strength is the original game

Define the positive actual-node game value

```text
v_Y=sup_(p in Delta_M) inf_(t in H) sum_j p_j X_t(j)
   =inf_(nu in Prob(H)) max_j int_H X_t(j)dnu(t).     (2.1)
```

The equality is compact minimax.  For `beta>0`, define the soft maximum

```text
L_beta(nu)=beta^(-1)log sum_j mu_j
                      exp[beta int_H X_t(j)dnu(t)].  (2.2)
```

For every `nu`,

```text
max_j int X_t(j)dnu + beta^(-1)log(min_j mu_j)
 <=L_beta(nu)
 <=max_j int X_t(j)dnu.                              (2.3)
```

It follows that

```text
v_Y+beta^(-1)log(min mu)
 <=inf_nu L_beta(nu)<=v_Y,                            (2.4)
lim_(beta to infinity) inf_nu L_beta(nu)=v_Y.         (2.5)
```

For the empirical measure in Section 1, `beta=eta K` and

```text
L_(eta K)(nu_K)=(eta K)^(-1)log Z_K.                 (2.6)
```

Therefore a uniform lower bound

```text
log Z_K>=-eta K epsilon-o(eta K)                     (2.7)
```

for every query sequence, at arbitrarily large `eta K`, implies
`v_Y>=-epsilon`.  Conversely `v_Y>=-epsilon` gives

```text
log Z_K>=-eta K epsilon+log(min mu)                  (2.8)
```

for every sequence.  Empirical probability measures are weakly dense in
`Prob(H)`, and there are only finitely many continuous coordinates, so no
measure-theoretic qualification is missing.

Thus the one-sided partition lower bound which would force the algorithm to
terminate is asymptotically equivalent to the positive actual-node minimax
inequality.  Multiplicative weights is an exact solver once that inequality
is known; its potential alone is not a proof of it.

---

## 3. Exact Bessel expansion and what `I_0` normalization cancels

Symmetrize `mu` on `+/-u_j` and write its real characteristic function as

```text
Phi(v)=sum_j mu_j cos(vu_j).                          (3.1)
```

The absolutely convergent identity

```text
exp(eta cos x)=sum_(m in Z) I_|m|(eta)exp(imx)       (3.2)
```

gives, with `t=(t_1,...,t_K)`,

```text
Z_K/I_0(eta)^K
 =sum_(m in Z^K) [product_k I_|m_k|(eta)/I_0(eta)]
                  Phi(sum_k m_k t_k).                (3.3)
```

Every coefficient in (3.3) is nonnegative.  The zero multi-index contributes
exactly one, and every additional exact relation `sum m_k t_k=0` also has
positive sign.  However, the sum of all coefficients is

```text
L_K=(exp(eta)/I_0(eta))^K,
log L_K=K[eta-eta^2/4+O(eta^4)].                     (3.4)
```

Thus `I_0` normalization cancels the quadratic Haar term, not the linear
coefficient-mass exponent `eta K`.

The first Bessel layer is already explicit.  If

```text
a_1(eta)=I_1(eta)/I_0(eta)=eta/2+O(eta^3),           (3.5)
```

then its contribution to (3.3) is

```text
2a_1(eta)sum_(k<=K)Phi(t_k).                         (3.6)
```

At `K=epsilon^(-2)` and `eta asyp epsilon`, a packet family with
`Phi(t_k) asyp -epsilon` makes (3.6) a negative constant.  This is the
directional signal driving the upper potential estimate, not a removable
normalization error.

---

## 4. The strongest scalar floor has a provably insufficient horizon

The Bessel expansion permits a rigorous aperture and tail audit.  Let

```text
lambda=eta K.                                         (4.1)
```

Under the probability law

```text
Pr{N=m}=exp(-eta)I_|m|(eta),                          (4.2)
```

`N` is the difference of two independent `Poisson(eta/2)` variables.  For
independent `N_1,...,N_K`, the total absolute order obeys

```text
sum_k |N_k|<=J,                 J~Poisson(lambda).    (4.3)
```

Suppose

```text
Phi(v)>=-delta                 for |v|<=4lambda B.   (4.4)
```

The all-zero Bessel choice has probability `1/L_K`.  On `J<=4lambda`, every
combination in (3.3) lies in (4.4), while `|Phi|<=1` always.  The Poisson
Chernoff bound therefore proves

```text
Z_K/I_0(eta)^K
 >=1-delta(L_K-1)
   -exp[-4(log 4-1)lambda].                          (4.5)
```

Indeed

```text
Pr{J>4lambda}
 <=exp[-(4log4-3)lambda],
L_K<=exp(lambda),                                    (4.6)
```

which gives the last term in (4.5).

The unconditional actual-node tent theorem supplies (4.4), throughout every
fixed polynomial aperture, with

```text
delta_VK=exp[-c_A(log Y/log log Y)^(1/3)].            (4.7)
```

At the algorithmic horizon

```text
K=O(epsilon^(-2)log Y),       eta=O(epsilon),        (4.8)
```

the required aperture in (4.4) is only

```text
4lambda B<=Y^(50/33+c+o(1)),                         (4.9)
```

so height is not the problem.  The problem is coefficient mass.  Formula
(4.5) is informative only up to

```text
lambda<=(.5+o(1))log(1/delta_VK).                    (4.10)
```

Over that entire horizon, the maximum useful upper-potential drop is only

```text
eta epsilon K=epsilon lambda
 <<epsilon log(1/delta_VK)=o(1).                     (4.11)
```

In contrast, a constant drop requires `lambda asyp 1/epsilon`, and overcoming
the softmax entropy in (1.9) requires still more iterations.  The KMT
absolute floor has `log(1/delta_KMT)=O(log log Y)` and is weaker than (4.7).

This proves a sharp limitation of the scalar Bessel argument: to reach the
critical horizon using only a uniform scalar lower floor in (4.5), one would
need roughly

```text
delta<=exp[-Omega(1/epsilon)],                        (4.12)
```

not the known subpower floor.  A fixed-power scalar floor smaller than the
target would of course terminate the algorithm already at stage zero; (4.12)
describes the attempted bootstrap when the starting floor is larger than the
target.

---

## 5. Guth--Maynard and Heath--Brown stop at the critical Bessel scale

For a one-separated query family of critical cardinality

```text
R=epsilon^(-2)=Y^(2c),                c=.019,        (5.1)
```

the Guth--Maynard large-value theorem and its dyadic square summation give,
in the present aperture,

```text
sum_(k<=R)|Phi(t_k)|^2<=Y^o(1).                       (5.2)
```

Inserting (5.2) into the exact first layer (3.6) yields only

```text
|2a_1 sum_k Phi(t_k)|
 <=(1+o(1))eta sqrt(R)Y^o(1).                        (5.3)
```

The potential must take `eta sqrt(R) asyp 1` to make a constant amount of
progress.  Hence (5.3) is critical, not `o(1)`.  A vector with
`Phi(t_k) asyp-epsilon` saturates the sign and scale.

The Heath--Brown shifted difference-square theorem improves the dispersive
pair-count and top-aperture terms, but its repeated-difference term is `R`.
After the diagonal cancellation this is the same directional autocorrelation
left in the square-reweighting report.  It supplies no favorable sign for the
second and higher Bessel layers.  The stable uniform critical AP is excluded
by the separate Fejer argument, but weighted mixtures and the adaptive
coefficient vector remain.

More generally, at `R=epsilon^(-2)` a degree-`D` Fourier estimate at its
natural square-root scale is multiplied by

```text
(eta sqrt(R))^D.                                     (5.4)
```

Every fixed degree can therefore contribute at constant scale when the
potential makes constant progress.  Taking `eta sqrt(R)=o(1)` makes a
fixed-order expansion perturbative, but then the total descent
`eta epsilon R=eta sqrt(R)` is also `o(1)`.  This is the exact all-order
barrier; a finite cumulant or fixed-moment truncation cannot decide the sign.

---

## 6. Sharp compact-group model for the normalized potential

Let `Theta_1,...,Theta_R` be independent Haar angles,

```text
X_i=cos Theta_i,             S_R=sum_i X_i,          (6.1)
```

and condition Haar measure on

```text
S_R<=-sqrt(R).                                      (6.2)
```

As proved in the companion Gibbs halfspace report, this probability measure
has, uniformly over every nonzero torus character,

```text
|hat mu_R(k)|<<R^(-1/2),                             (6.3)
```

and for every fixed character of `l1` degree `D`,

```text
hat mu_R(k)=O_k(R^(-D/2)).                           (6.4)
```

Its shifted `R`-by-`R` square ledger is `O(1)`.  Nevertheless every positive
reweighting satisfies

```text
min_i E_h X_i<=-R^(-1/2).                            (6.5)
```

Thus the target `-1/(2sqrt(R))` is infeasible.

The `I_0` normalization can be evaluated exactly at the critical step size.
For fixed `a>0`, take `eta=a/sqrt(R)` and one symmetric batch of all `R`
coordinates.  The central limit theorem and
`I_0(a/sqrt(R))^R ->exp(a^2/4)` give

```text
 E_(mu_R) exp[(a/sqrt(R))S_R]
 ---------------------------------
        I_0(a/sqrt(R))^R

 -> Phi_N(-sqrt(2)-a/sqrt(2))/Phi_N(-sqrt(2)),       (6.6)
```

where `Phi_N` is the standard normal distribution function.  The right side
is strictly below one and tends to zero as `a` grows.  The diagonal variance
has canceled exactly; the collective halfspace remains in the normalized
partition.

Equations (6.3)--(6.6) show that even ideal fixed-degree Fourier decay, an
excellent shifted square ledger, and stable Gibbs normalization do not imply
the needed one-sided potential lower bound.  All Bessel orders collectively
encode the support wall.

This model is not the one-dimensional actual prime-log orbit.  It proves
only that KMT, Guth--Maynard/Heath--Brown fixed-moment data, and generic
multiplicative-weights potential inequalities cannot close the actual-prime
statement without an additional scalar-orbit theorem.

---

## 7. The surviving actual-prime statement

The new input would have to exclude every adaptive query measure `nu` by
proving, for some fixed `c>.018746369714728765...`,

```text
max_(p^m in the shell)
 int_H cos(t log(p^m/Y))dnu(t)>=-Y^(-c)              (7.1)
```

for every probability `nu` on the complete height band, with the exact
aggregation at equal absolute nodes.  By (2.1), this is precisely the
positive actual-node minimax theorem.  Equivalent analytic inputs include an
all-order Laplace-transform comparison for the actual prime-log curve or a
candidate-specific nonlinear covariance theorem retaining the complete
partition function.  It is not supplied by the presently imported scalar or
fixed-degree estimates.

Binary disposition:

```text
exact continuum multiplicative-weights identities:        PROVED;
finite termination/orthant-witness dichotomy:              PROVED;
soft partition lower bound versus game value:              EQUIVALENT;
exact I_0-normalized Bessel expansion:                     PROVED;
polynomial-aperture control of the effective Bessel tail:   PROVED;
tent/KMT floor reaches the critical iteration horizon:      NO;
Guth--Maynard first Bessel layer is subcritical:            NO, CRITICAL;
Heath--Brown removes the repeated-difference direction:     NO;
fixed-degree moment data imply all-order repair:            FALSE ABSTRACTLY;
actual-prime all-order/anti-halfspace theorem:              OPEN;
fixed-power positive or signed QP-KILL:                     NOT PROVED;
QP-PROMOTE, uniform strip, or QP/strip equivalence:         NOT PROVED.
```

Executable replay:

- `src/qp_multiplicative_weights_gate.py`;
- `src/test_qp_multiplicative_weights_gate.py`;
- `results/verify_zeta23_qp_multiplicative_weights_gate.py`.
