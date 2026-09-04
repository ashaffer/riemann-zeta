# Gap-residue character audit at the surviving denominator shell

**Date:** 2026-08-13

## Verdict

At a frozen rational frequency, the symmetrized forward/reverse gap antenna
has an exact Dirichlet-character expansion.  The principal character is
harmless.  The whole obstruction is the Gauss-weighted nonprincipal statistic

```text
C_q^sym(chi)
 =1/2 sum_j Delta_j
   [phi(v_j) chi(p_j)+phi(v_(j+1)) chi(p_(j+1))].       (0.1)
```

No theorem located here bounds (0.1), or its Gauss-weighted recombination,
pointwise for a selected modulus

```text
Y^(1537/10000)<q<=Y^(797/5000).                        (0.2)
```

The classical additive large sieve does give a genuine power saving for
**almost every reduced rational frequency** in this shell.  After the
`Y^(797/5000)` gap truncation, its root-mean-square saving at the bottom of
the shell is

```text
1537/10000-(797/5000)/2 = .074.                        (0.3)
```

This is much larger than the target
`kappa=.0180303234`.  It still permits more exceptional fractions than there
are moduli in the shell, so it does not control the rational approximant
selected by the logarithmic phase.

A finite pseudoprime construction below has exact unweighted residue
equidistribution at a selected prime modulus, vanishing nonprincipal
unweighted character sums, prime-density-shaped counting, the known
gap-square budget, the optimized large-gap-tail budget, and no deleted gap.
Its symmetrized gap DFT nevertheless has relative size `Y^(-kappa)`.  This is
a rigorous nonimplication for marginal residue/character inputs.  It is not a
counterexample made from actual primes and is not a no-go theorem for the
actual-prime route.

No zero-free strip is claimed here.

---

## 1. Exact transition, additive-DFT, and character identities

Put

```text
v_j=log(p_j/Y),             Delta_j=log(p_(j+1)/p_j),
e_q(x)=exp(2*pi*i*x/q).
```

On one frozen physical block, the leading symmetrized Voronoi mode at the
reduced rational frequency `r/q` is

```text
A_q(r)=1/2 sum_j Delta_j
 [phi(v_j)e_q(r p_j)+phi(v_(j+1))e_q(r p_(j+1))].       (1.1)
```

Endpoint clipping only changes the corresponding boundary terms.  Define

```text
M_q^L(a,b)=sum_(p_j=a, p_(j+1)=b mod q) Delta_j phi(v_j),
M_q^R(a,b)=sum_(p_j=a, p_(j+1)=b mod q) Delta_j phi(v_(j+1)). (1.2)
```

Then exactly

```text
A_q(r)=1/2 sum_(a,b mod q)
 [M_q^L(a,b)e_q(ra)+M_q^R(a,b)e_q(rb)].                (1.3)
```

Thus only the row marginal of `M^L` and the column marginal of `M^R` enter.
In the constant-amplitude specialization `M^L=M^R=M`, one edge contributes

```text
g e_q(r(a+b)/2) cos(pi*r*(b-a)/q),                    (1.4)
```

where the half-residue notation in (1.4) is an ordinary complex exponential
and does not require that `2` be invertible.  The cosine can have modulus one.

Every shell prime is coprime to `q`, since `q<Y`.  For characters on
`U_q=(Z/qZ)^*`, set

```text
Mhat_q^L(chi,psi)=sum_(a,b in U_q)M_q^L(a,b)chi(a)psi(b),
Mhat_q^R(chi,psi)=sum_(a,b in U_q)M_q^R(a,b)chi(a)psi(b),

C_q^sym(chi)=1/2[Mhat_q^L(chi,1)+Mhat_q^R(1,chi)].     (1.5)
```

The generalized Gauss coefficient is

```text
tau_q(chibar;r)=sum_(a in U_q) chibar(a)e_q(ra).       (1.6)
```

Character Fourier inversion gives the exact identity

```text
A_q(r)=1/phi(q) sum_(chi mod q)
                 tau_q(chibar;r) C_q^sym(chi).         (1.7)
```

When `(r,q)=1`, the principal coefficient is the Ramanujan sum
`c_q(r)=mu(q)`.  Its contribution has size at most

```text
|C_q^sym(1)|/phi(q) << Y^(-1537/10000+o(1)),          (1.8)
```

after normalizing total shell mass to `O(1)`.  It is safely below the target.

For prime `q`, every nonprincipal character is primitive and

```text
tau_q(chibar;r)=chi(r)tau_q(chibar),
|tau_q(chibar)|=sqrt(q).                               (1.9)
```

Consequently the exact selected-frequency gate is

```text
|sum_(chi nonprincipal)
  [tau_q(chibar)/sqrt(q)] chi(r) C_q^sym(chi)|
       << sqrt(q) Y^(-c),       c>kappa.               (1.10)
```

This is not an ordinary prime character sum.  The coefficient of `chi(p_j)`
contains the preceding and following consecutive-prime gaps.

### 1.1 A clean sufficient fixed-modulus variance theorem

Define the symmetrized residue mass

```text
S_q(a)=1/2[sum_b M_q^L(a,b)+sum_b M_q^R(b,a)],
Sbar_q=phi(q)^(-1)sum_a S_q(a).                        (1.11)
```

Then `C_q^sym(chi)=sum_a S_q(a)chi(a)`, and character Parseval gives

```text
sum_(chi nonprincipal)|C_q^sym(chi)|^2
 =phi(q) sum_(a in U_q)|S_q(a)-Sbar_q|^2.             (1.12)
```

Also, since the numbers in (1.6) are the character-Fourier coefficients of
the unit-modulus function `a -> e_q(ra)`, Parseval gives

```text
sum_(chi mod q)|tau_q(chibar;r)|^2=phi(q)^2.           (1.13)
```

Therefore a sufficient theorem, uniform for every selected `q` in the
surviving shell, would be

```text
sum_(chi nonprincipal)|C_q^sym(chi)|^2 << Y^(-2c),
c>kappa,                                               (1.14)
```

or equivalently

```text
sum_(a in U_q)|S_q(a)-Sbar_q|^2
 << Y^(-2c)/phi(q).                                    (1.15)
```

In physical rather than normalized mass, the right sides of (1.14) and
(1.15) are multiplied by `Y^2`.  Equation (1.10) is the exact weaker target
for one numerator; (1.14) is a natural all-numerator sufficient condition.
Neither statement was found in the literature.

---

## 2. Multi-gap recurrences do not reduce to one-gap aliases

For `m>=1`, let

```text
D_(j,m)=p_(j+m)-p_j=g_j+...+g_(j+m-1).                (2.1)
```

The roots-of-unity filter for an `m`-gap return is exactly

```text
1_(q divides D_(j,m))
 =1/q sum_(r mod q)e_q(r(p_(j+m)-p_j)).               (2.2)
```

Since both endpoints are units, multiplicative character orthogonality also
gives

```text
1_(p_(j+m)=p_j mod q)
 =1/phi(q) sum_(chi mod q)chi(p_j)chibar(p_(j+m)).     (2.3)
```

Thus a recurrence-based proof would need weighted consecutive-prime
correlations of the form

```text
sum_j W_(j,m) chi(p_j)chibar(p_(j+m)),                (2.4)
```

uniformly for the relevant `m`, block, and growing `q`.  Bombieri--Vinogradov
controls one-point von-Mangoldt marginals; it does not control (2.4).

More importantly, a large aggregate in (1.3) need not contain any literal
return in (2.2).  Many small, nonzero phases can cohere.  Hence truncating
individual gaps at `Y^(797/5000)` does not cap the aggregate denominator.
The exact full-block statistic remains (1.7), while (2.4) is the additional
input needed by an attempted multi-step mixing proof.

---

## 3. What the classical large sieve really proves here

Let `a_n` be the normalized leading Voronoi coefficient supported on shell
primes, so that

```text
A(alpha)=sum_(n asymp Y)a_n e(alpha n),
sum_n |a_n| << 1.                                     (3.1)
```

After deleting every half-gap above

```text
G=Y^theta,                 theta=797/5000=.1594,      (3.2)
```

positivity and `Delta_j<<g_j/Y` give

```text
max_n |a_n| << Y^(theta-1),
sum_n |a_n|^2 << Y^(theta-1).                         (3.3)
```

The sharp large-sieve inequality of Montgomery--Vaughan gives, for
`Q=Y^b` with `Q^2=o(Y)`,

```text
sum_(Q<q<=2Q) sum_((r,q)=1)|A(r/q)|^2
 <<(Y+Q^2)sum_n|a_n|^2
 <<Y^(theta+o(1)).                                    (3.4)
```

There are `Y^(2b+o(1))` reduced fractions in (3.4), so the root-mean-square
size is

```text
Y^(theta/2-b+o(1)).                                   (3.5)
```

At the lowest surviving denominator, (3.5) saves exactly

```text
b-theta/2=.1537-.0797=.074.                           (3.6)
```

This is a useful positive theorem, not merely a heuristic.

But Markov's inequality applied to (3.4) allows

```text
# {r/q: |A(r/q)|>Y^(-kappa)}
 <<Y^(theta+2kappa+o(1))
 =Y^(.1954606468...+o(1)).                            (3.7)
```

The number of moduli at the lower edge is only
`Y^(.1537+o(1))`.  Thus (3.7) is consistent with at least one bad numerator
for **every modulus**.  It cannot control the numerator and denominator
selected by Dirichlet approximation to `t/(2*pi*x)`.

At one fixed denominator, the same inequality over the `q` equally spaced
numerators gives only

```text
sum_(r mod q)|A(r/q)|^2 <<Y^(theta+o(1)),              (3.8)
```

whose root-mean-square bound is
`Y^((theta-b)/2+o(1))`; this is not even a negative power when `b<theta`.

Without the optimized truncation, Stadlmann's
`sum g_j^2<<Y^(1.23+epsilon)` gives
`sum|a_n|^2<<Y^(-.77+epsilon)`.  The global large-sieve RMS saving at
`b=.1537` would still be `.1537-.115=.0387`, but the same selected-frequency
obstruction remains.

Primary source: Montgomery and Vaughan,
[*The large sieve*](https://doi.org/10.1112/S0025579300004708), Theorem 1.
Bombieri's earlier prime-distribution application is
[*On the large sieve*](https://doi.org/10.1112/S0025579300005313).

---

## 4. Audit of the proposed character tools

### 4.1 Bombieri--Vinogradov and Barban--Davenport--Halberstam

These theorems estimate the progression errors of `Lambda`, averaged over
moduli (and, for BDH, over residue classes).  They do not estimate `S_q(a)`
in (1.11).  Even their unweighted selected-modulus consequence is at
logarithmic rather than fixed-power strength, and an average over moduli
cannot be assigned to the phase-selected modulus.

The original primary sources are Bombieri's paper above and Davenport--
Halberstam,
[*Primes in arithmetic progressions*](https://doi.org/10.1307/mmj/1028999608).
Kim's actual-prime forward statistic is still conjectural even for one fixed
`q>=3`; see Section 4.4 below.  Hence there is no valid summation-by-parts
bridge from the classical progression theorems to (1.11).

### 4.2 Dirichlet zero density and recent character large values

Chen--Gupta--Li,
[*Large Value Estimates for Dirichlet Polynomials with Characters and Zero
Density of Dirichlet L-Functions*](https://arxiv.org/abs/2507.08296v2),
Theorems 1.1--1.2, prove a fixed-modulus character large-value theorem for
arbitrary bounded coefficients and the zero-density exponent `7/3`.  Their
arithmetic applications concern ordinary primes in progressions.

This does not close (1.10):

1. zero detection accesses `Lambda(n)chi(n)`, not successor-gap weights;
2. the large-value theorem counts large individual character polynomials,
   whereas (1.10) is one prescribed Gauss-weighted superposition of all
   characters;
3. after normalizing (3.3) to coefficients bounded by one, the first term
   `N^2/V^2` in their Theorem 1.1 is already trivial at the power needed here
   in the regime `N=Y`, `q=Y^b`, `b<.16`.

The possibility of an exceptional real character is therefore not the only
issue.  Even a hypothetical pointwise GRH estimate for the ordinary twisted
von-Mangoldt sum would leave the nonlinear coefficient identity (0.1)
unproved.

Harper's
[*Simple Barban--Davenport--Halberstam type asymptotics for general
sequences*](https://arxiv.org/abs/2412.19644), Theorem 1, begins at
`Q>sqrt(2Y)`, far above (0.2), and assumes sequence-specific progression,
nonconcentration, and hereditary-sparsity hypotheses.  For the present gap
sequence, its progression hypothesis is already a close relative of the
missing conclusion; it is not supplied by the prime-number BV theorem.

### 4.3 Burgess and upper-bound sieves

Burgess's theorem,
[*On character sums and primitive roots*](https://www.mathnet.ru/eng/mat267),
controls interval sums of a Dirichlet character.  The available block lengths
are more than long enough relative to `q^(1/4)`.  The problem is the
coefficient: (0.1) is supported at primes and weighted by the neighboring
successor gaps.  Those weights have no bounded-variation estimate that would
permit partial summation from Burgess.

Brun--Titchmarsh and Selberg-sieve estimates are nonnegative upper bounds.
After expanding the condition that two primes are consecutive, the exclusion
of every intermediate prime requires growing-order inclusion--exclusion;
truncating it loses the sign.  No fixed-dimensional upper-bound sieve theorem
located here produces either (1.10), (1.14), or (2.4).

### 4.4 Prime-running functions identify the exact open statistic

Jaeyoon Kim,
[*Prime Running Functions*](https://doi.org/10.1080/10586458.2020.1786863),
defines the forward marginal in (1.11).  His Conjecture 2.2 is its
equidistributed main term; beyond `q=2`, even that actual-prime main term is
not proved.  Theorems 4.3 and 4.5 concern a fixed-sieve modified Cramer model,
not actual primes.  Section 6 predicts the opposite first bias for the reverse
statistic, which motivates the symmetrization, but supplies no actual-prime
error term and no growing-modulus uniformity.

Thus the character transform has diagonalized the missing object; it has not
turned it into an existing Dirichlet `L`-function coefficient.

---

## 5. A selected-modulus marginal-equidistribution countermodel

This construction is deliberately scoped to the frozen additive model.  It
shows that density, gap tails, gap square, and even exact unweighted
equidistribution at the selected modulus do not imply (1.10).

Choose

```text
beta=1537/10000,
theta=797/5000,
beta<b<b_*:=2/15+(13/9)kappa=.1593771338...,
q asyp Y^b prime,
d=ceil(log Y),
K asyp Y^kappa/d.                                    (5.1)
```

Multiplication by `d` permutes the nonzero residues modulo `q`.  Make one
residue cycle

```text
d,2d,...,(q-1)d  (mod q),                             (5.2)
```

using physical gaps `d` between successive displayed residues and a final
gap `2d` from `-d` back to `d`, skipping residue zero.  Every cycle visits
every unit exactly once and has physical length `qd`.

Every `K` cycles, replace one fixed transition `d -> 2d` of length `d` by a
transition of length `d+q`.  Its endpoint residue is unchanged.  The whole
future residue itinerary is therefore unchanged, and a supercycle has:

```text
K visits to every unit residue,
K(q-1) nodes,
physical length Kqd+q.                                (5.3)
```

Repeat complete supercycles through a shell of length comparable with `Y`.
The following statements are exact up to the harmless two shell boundaries.

1. **Prime-shaped density.**  The number of nodes is `asymp Y/d`, hence
   `asymp Y/log Y`.  Since every gap is at least `d`, the same construction
   has the local upper count

   ```text
   #(X_Y intersect J)<<1+|J|/log Y.                  (5.4)
   ```
2. **Perfect selected-q marginal distribution.**  Every unit is visited the
   same number of times.  Every nonprincipal unweighted character sum is
   exactly zero on complete supercycles.
3. **No deleted gap.**  The largest gap is `q+d=Y^(b+o(1))`, and
   `b<theta`.
4. **Mean-square budget.**  The small gaps contribute `O(Y log Y)`.  The
   long gaps contribute

   ```text
   <<Y^(1+b-kappa+o(1))=o(Y^1.23).                    (5.5)
   ```

5. **Exceptional-tail budget.**  Their total long-gap mass is

   ```text
   Y^(1-kappa+o(1)).                                  (5.6)
   ```

   On the Gafni--Tao envelope used in the optimized tail audit, the allowed
   mass at threshold `Y^b` is

   ```text
   Y^[1-c(b)+o(1)],   c(b)=(9/13)(b-2/15).            (5.7)
   ```

   The choice `b<b_*` is exactly `c(b)<kappa`, so (5.6) is allowed.
6. **Critical symmetrized DFT.**  At numerator `r=1`, the added length on
   the distinguished edge contributes

   ```text
   q/2 [e_q(d)+e_q(2d)],                              (5.8)
   ```

   of modulus `q(1+o(1))`.  All supercycles have the same phase.  The base
   cycle's symmetrized DFT is

   ```text
   d sum_(a in U_q)e_q(a)+d/2[e_q(d)+e_q(-d)]
    =-d+d cos(2*pi*d/q)=O(d),                         (5.9)
   ```

   so `K` base cycles contribute only `O(Kd)=O(Y^kappa)`, while
   `q>>Y^kappa`.  Dividing (5.8) by the supercycle mass `asymp Kqd` gives

   ```text
   |A_q(1)| asyp 1/(Kd)=Y^(-kappa+o(1)).             (5.10)
   ```

The calculation above used physical, constant-amplitude edge mass.  It
persists for the logarithmic coefficient in (1.1).  Place the construction
in a compact interior subshell on which `phi` is positive, and put

```text
h(x)=phi(log(x/Y))/x,       h(x) asyp 1/Y,
|h'(x)|<<1/Y^2.                                      (5.11)
```

Freezing `h` on each cycle of length `qd` makes all base cycles contribute
in total

```text
O(1/q)+O(qd/Y)=o(Y^(-kappa)).                        (5.12)
```

Replacing `log(1+g/x)` by `g/x` costs

```text
O(sum_j g_j^2/Y^2)=o(Y^(-kappa)).                    (5.13)
```

The added `q`-increments retain one common complex direction, while their
smooth factors are positive and comparable.  Their total logarithmic mass
is still `asymp 1/(Kd)`.  Thus (5.10) is genuinely the exponent of the
log-weighted frozen rational statistic, not only of an unnormalized physical
toy sum.

This model has zero unweighted marginal discrepancy at the selected modulus,
yet it saturates the desired gap-weighted bound.  Therefore no argument using
only unweighted selected-q residue marginals, the current gap-square estimate,
the optimized gap tail, and the retained-gap cutoff can prove (1.10).

The model is not made from primes, does not claim full Bombieri--Vinogradov
distribution simultaneously for all moduli, and does not include the global
logarithmic curvature.  Those actual-prime structures remain legitimate
sources of extra cancellation.

---

## 6. Precise surviving theorem

The roots-of-unity/character route has reduced the frozen rational component
to either of the following genuinely new actual-prime inputs.

**Exact selected-frequency form.**  Uniformly for every retained block,
reduced `r/q`, and `q` in the one-gap or multi-gap Dirichlet range, prove

```text
|1/phi(q) sum_(chi nonprincipal)
 tau_q(chibar;r) C_q^sym(chi)| <<Y^(-c),
c>kappa.                                               (6.1)
```

**Stronger fixed-modulus dispersion form.**  Prove (1.14), equivalently
(1.15), uniformly at each selected growing modulus.

For a proof based on block returns rather than direct marginals, one must in
addition establish a weighted version of (2.4), uniformly through

```text
q<=Y/sqrt(t),
Y<=t<=Y^(50/33).                                      (6.2)
```

The standard large sieve proves (6.1) for almost all rational frequencies,
not for the selected one.  The literature surveyed here contains no
pointwise theorem and no actual-prime no-go theorem for (6.1).
