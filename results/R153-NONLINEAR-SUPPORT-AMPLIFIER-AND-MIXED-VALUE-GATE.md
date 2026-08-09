# R153 nonlinear support amplifier and mixed-value gate

## Status

This report tests the first mechanism in the degree-zero branch that really
beats the old conductor exponent on the Euler side.

Let

```text
F(s)=N(s)/D(s)=1+U(s)                                      (0.1)
```

be a positive head-deleted quotient from R147 or R151.  For even `q`, put

```text
P_q(s)=1-U(s)^q,
B_q(s)=P_q'(s)/P_q(s).                                     (0.2)
```

The nonlinear operation moves the Dirichlet support from `H` to `H^q`, while
its completed divisor ledger grows only linearly in `q`.  At the level of the
exponent ledger this makes the known cubic scale `log D asymp H` compatible
with Cauchy localization.  It is a genuine improvement over R147's linear
quotient.

It does not prove a strip.  The price is an algebraically mandatory
family of mixed value divisors

```text
F(s)=1+omega,                  omega^q=1.                   (0.3)
```

The non-target factors are linear combinations, not Euler products.  Existing
Artin and Hecke zero-density theorems do not select them away.  R155 proves
more: simultaneous avoidance is impossible along a growing deleted head
which retains the fixed zeta zero and has its auxiliary divisor removed.
Merely noting that the forced mixed residues have the same sign as the target
is insufficient: their phases can cancel a target jet for arbitrarily long,
field-dependent blocks.  At the known `log D asymp H` scale, a worst-case
Turan step needs order `qH`, whereas the amplified head controls only order
`q log H`.

```text
H -> H^q Euler-support amplification                       EXACT
linear-q completed divisor ledger                          EXACT
formal conditional closure at log D<<H                     THEOREM
mixed value divisors F=1+omega                             UNAVOIDABLE
simultaneous target-disc mixed-value avoidance              IMPOSSIBLE
favorable-residue uniform Turan bound                      FALSE
ordinary Artin/Hecke zero-density selection                INAPPLICABLE
rational scalar filter without equivalent extra divisors   IMPOSSIBLE
signed packet estimate including forced a-points            OPEN
fixed uniform zeta zero-free strip                         NOT PROVED
zeros approaching one                                      NOT PROVED
```

Date: 2026-08-08.

Predecessors:
[`R151-CLASS-CHARACTER-HEAD-QUOTIENT-GATE.md`](R151-CLASS-CHARACTER-HEAD-QUOTIENT-GATE.md)
and
[`R152-GENUS-REDEI-AND-BOOLEAN-CLASS-MASK-GATE.md`](R152-GENUS-REDEI-AND-BOOLEAN-CLASS-MASK-GATE.md).

## 1. Exact coefficient and support amplification

Assume that in `Re(s)>1`

```text
U(s)=sum_(n>H) u(n)n^(-s),               u(n)>=0.           (1.1)
```

For the head-deleted Artin and class-character quotients this follows from
the nonnegative logarithmic Euler coefficients: every nonconstant integer in
the Euler expansion has a prime divisor greater than `H`, hence is itself
greater than `H`.

For even `q`, differentiation of (0.2) gives

```text
B_q(s)=-q U(s)^(q-1)U'(s)/(1-U(s)^q)                       (1.2)

      =q[-U'(s)]U(s)^(q-1) sum_(j>=0)U(s)^(qj).             (1.3)
```

Every Dirichlet coefficient in (1.3) is nonnegative.  Every displayed
monomial has at least `q` nonconstant factors from (1.1), so

```text
supp B_q subset {n>H^q}.                                   (1.4)
```

This is multiplicative support amplification, not just deletion of more
prime powers.

Let

```text
z_*=1+r+i gamma,                    r>0.                    (1.5)
```

On `|s-z_*|=r/2`, positivity and the ordinary Euler tail imply

```text
|U(s)|<=U(1+r/2)<=H^(-r/2+o(1)),
|U'(s)|<=-U'(1+r/2)<=H^(-r/2+o(1)).                         (1.6)
```

For fixed `q` and large `H`, (1.2) and Cauchy's inequality therefore give

```text
|B_q(s)|<=H^(-qr/2+o(1)),                                   (1.7)

|B_q^(k)(z_*)|/k!
 <=(2/r)^k H^(-qr/2+o(1)).                                 (1.8)
```

Equation (1.8) is the gain that the linear quotient did not have.

## 2. Exact factorization and divisor ledger

Write `F=N/D`.  Since `U=(N-D)/D`,

```text
P_q=[D^q-(N-D)^q]/D^q.                                    (2.1)
```

Factoring the difference of powers and reindexing the roots of unity gives,
up to a nonzero constant,

```text
P_q=-D^(-q)N
     product_(omega^q=1, omega!=-1)[N-(1+omega)D].          (2.2)
```

Consequently

```text
B_q=N'/N
    +sum_(omega!=-1)[N-(1+omega)D]'/[N-(1+omega)D]
    -qD'/D.                                                (2.3)
```

The target factor is `N`, because `omega=-1` corresponds to `F=0`.  The
remaining factors vanish at the mixed values (0.3).

After completing `N` and `D`, every term in (2.3) has the same fixed-degree
conductor envelope.  Jensen's formula or a fixed-disc zero count therefore
gives the absolute local ledger

```text
C_q<<q[1+log D+log(|gamma|+T+3)].                           (2.4)
```

The key point is that (2.4) is linear in `log D`, not `(log D)^q`.

## 3. Conditional fixed-strip closure at the known field scale

Suppose

```text
rho=1-delta+i gamma,
d=|z_*-rho|=r+delta,
d<R<r+eta.                                                  (3.1)
```

Fix an even `q`.  Assume that for each large useful derivative order `k`
there is a head-deleted quotient (0.1) such that

1. `log D<<H`;
2. throughout `|s-z_*|<=R`, `D`, every non-zeta factor of `N`, and every
   mixed factor in (2.2) are nonzero; and
3. the only remaining local zeros of `P_q` are therefore the fixed zeta
   zeros.

Set

```text
H=exp(beta k).                                               (3.2)
```

The nearest-pole power-sum lemma now has a field-independent bounded gap,
and at its useful orders the target gives

```text
|B_q^(k)(z_*)|/k!
 >=c d^(-k-1)-O(C_q R^(-k-1)).                              (3.3)
```

The outer term is negligible if

```text
beta<log(R/d).                                               (3.4)
```

The Euler upper bound (1.8) is negligible relative to the target if

```text
qr beta/2>log(2d/r).                                        (3.5)
```

Thus (3.4)--(3.5) are compatible as soon as

```text
q>2 log(2d/r)/[r log(R/d)].                                 (3.6)
```

For every fixed hypothetical zero and fixed localization geometry, a fixed
even `q` satisfying (3.6) exists.  This proves the following formal
implication.

### Theorem 3.1 -- conditional nonlinear closure

The R148 family scale `log D<<H`, together with target-disc nonvanishing of
the finitely many mixed factors in (2.2) and the ordinary auxiliary factors,
would exclude the source zero `rho`.

Unlike the R147 criterion, Theorem 3.1 does not require
`log D=o(H^kappa)` with `kappa<1/2`.  The entire remaining difficulty is the
mixed-value condition.  R155 proves that this sufficient hypothesis cannot
hold along `H -> infinity` if the source zero is retained: for every useful
even `q>=4`, two omitted mixed values would make the quotient family normal,
and right-cap convergence to `1` would contradict its fixed zero.  Thus
Theorem 3.1 is a calibrated exponent implication with an impossible
avoidance premise, not a live conditional construction.

## 4. Why favorable mixed zeros do not suffice

Every zero of `P_q` has positive residue in `B_q=P_q'/P_q`.  That sign is not
a uniform high-jet lower bound, because reciprocal powers have phases.

Let the target reciprocal displacement be

```text
v_0=1/d.                                                     (4.1)
```

For a large integer `K`, add two favorable simple zeros with reciprocal
displacements

```text
v_+=v_0 2^(-1/K) exp(i pi/K),
v_-=v_0 2^(-1/K) exp(-i pi/K).                              (4.2)
```

They are farther from `z_*` than the target and lie in the same left
half-plane geometry.  At power `n=K+j`, their combined contribution is

```text
v_+^n+v_-^n
 =-v_0^n 2^(-j/K)cos(pi j/K).                               (4.3)
```

Hence the target plus the two favorable zeros vanishes exactly at `j=0` and
is `O_L(K^(-1))v_0^n` uniformly for every fixed `|j|<=L`.  No lower bound with
a field-independent bounded gap follows from residue sign alone.

The root-of-unity geometry makes the phenomenon exact.  In the affine local
model

```text
F(s)=1+(s-s_*)/d,
P_q(s)=1-[(s-s_*)/d]^q,                                    (4.4)
```

the `q` zero contributions cancel identically for derivative orders
`0,...,q-2`.  The first nonzero response occurs at order `q-1`.  Thus a
`q`-sized Turan loss is built into the amplifier even before conductor growth
is considered.

In a fixed target disc, the mixed divisor count is at most

```text
M_q<<q[log D+log(|gamma|+3)].                               (4.5)
```

and no theorem here bounds it by a field-independent constant.  At the known
scale `log D asymp H`, a worst-case power-sum selection may require

```text
k>>M_q asymp qH.                                            (4.6)
```

But the support `H^q` controls the derivative saddle only through

```text
log(H^q)=q log H.                                           (4.7)
```

The incompatible comparison `q log H>>qH` shows that ordinary Turan cannot
replace mixed-factor nonvanishing.

## 5. The mixed divisors are locally unavoidable when q grows

Suppose `F` has a zero of order `m` at `rho` and its denominator is nonzero
there.  For every sufficiently small `a`, Rouche's theorem gives exactly `m`
solutions of

```text
F(s)=a                                                     (5.1)
```

in a sufficiently small fixed neighborhood of `rho`, counted with
multiplicity.

Among the values `1+omega`, `omega^q=1`, there are `Theta(q epsilon)` in any
fixed `epsilon`-disc around zero.  Therefore, as `q` grows, every auxiliary
quotient has `Theta(qm)` mixed zeros near `rho`; no family selection can make
them absent.  For a simple target,

```text
rho_+-rho=-2 pi i/[qF'(rho)]+O(q^(-2)),
rho_--rho=+2 pi i/[qF'(rho)]+O(q^(-2)).                     (5.2)
```

More generally the nearest scale is `q^(-1/m)` after accounting for the local
leading coefficient.

Potential-theoretically,

```text
(1/q)log|1-U^q| -> log^+|U|                                (5.3)
```

away from `|U|=1`.  The mixed zeros converge as a Riesz measure to the
pullback lemniscate

```text
|F-1|=1.                                                    (5.4)
```

The target `F=0` is only one sampled point on this lemniscate.  A Jensen
kernel counts the whole positive mass, whose boundary characteristic is
`O(q log D)`; it does not isolate the target.

The stronger fixed-`q` normal-family theorem is in R155.  Exact head deletion
gives `F_H ->1` on a nonempty open right cap of the connected target disc.
For every fixed even `q>=4`, avoiding two values in (0.3) makes the
holomorphic family normal.  Every normal limit is then `1` on the cap and,
by the identity theorem, on the whole disc, contradicting `F_H(rho)=0`.
Thus mixed-value avoidance cannot persist even for the one fixed `q` used in
Section 3.  R155 also closes a one-value repeated-pole workaround by applying
Montel to `Log(2-F_H)` and the fixed finite zero divisor.

## 6. Scalar rational-filter conservation law

The extra values in (2.2) are not an accident of the monomial `U^q`.

Let `R(z)dz` be a rational logarithmic response used as

```text
R(F(s))F'(s).                                               (6.1)
```

Suppose it

1. has residue one at `z=0`, retaining an `F`-zero;
2. vanishes to order at least `q-1` at `z=1`, shifting the Euler support to
   the `q`-fold level; and
3. is `O(1/z)` at infinity, so that poles of `F` retain a logarithmic rather
   than power-size conductor ledger.

If the denominator of `R` has degree `L`, condition 3 makes its numerator
degree at most `L-1`.  Condition 2 forces that numerator to contain
`(z-1)^(q-1)`, hence `L>=q`.  One pole unit is the target at zero, so at least
`q-1` further finite value-divisor units are unavoidable.  The root-of-unity
filter is degree-optimal.

If all finite extra divisors are forbidden, the unique-zero transform is of
truncated-log type:

```text
G_q(F)=F exp[-sum_(j=1)^(q-1)(-1)^(j+1)(F-1)^j/j],          (6.2)

G_q'/G_q=(-1)^(q-1)(F-1)^(q-1)F'/F.                        (6.3)
```

It has exactly the `F`-zeros and the desired shifted support.  But every
`F`-pole becomes an essential singularity of (6.2), while (6.3) has pole
order growing with `q`.  The transform itself has boundary growth exponential
in `|F|^(q-1)`; its logarithmic response has an order-`q` pole/boundary bill
rather than the simple-divisor ledger (2.4).  Rational Pade replacements
merely redistribute the same `q-1` divisor units.

Thus scalar functional calculus has a trilemma:

```text
shift support by q;
retain only logarithmic conductor complexity;
introduce no new finite value divisors.                     (6.4)
```

At most two of the three can hold.

There is also a nonrational boundary version of this conservation law.  Let

```text
G(A)=1+sum_(n>=q)c_n A^n,
G(-1)=0,                                                     (6.5)
```

and suppose `G` is holomorphic on `|A|<=S`, where `S>1`.  If
`M_S=max_(|A|=S)|G(A)|`, Cauchy's coefficient bound and (6.5) give

```text
1<=M_S sum_(n>=q)S^(-n),
M_S>=(S-1)S^(q-1).                                          (6.6)
```

Thus an exact `q`-fold Taylor gap which still vanishes at the target either
has exponential value-plane boundary growth or introduces a pole before
radius `S`.  Polynomial, rational, and entire amplifiers are different
placements of the same bill.

## 7. Differential powers do not evade the ledger

Another natural attempt is to put

```text
A=-F'/F,
Q_q=A^q.                                                     (7.1)
```

The coefficients of `Q_q` are nonnegative and its support starts beyond
`H^q`.  If `F` has a zero at `rho`, the isolated top pole in the normalized
`k`th derivative has, with `K=k+q`, size

```text
T_top=binom(K-1,q-1)c^q d^(-K).                             (7.2)
```

Let `M` denote the one-factor absolute remote ledger.  Leibniz expansion
gives the matching bound

```text
E<=binom(K-1,q-1)M^q R^(-K).                                (7.3)
```

The binomial target amplification cancels exactly between (7.2) and (7.3).
At `M asymp log D asymp H`, Euler-tail suppression requires, up to the usual
fixed saddle constant `lambda>1`,

```text
q log H>=lambda K/r,                                        (7.4)
```

whereas outer localization requires

```text
q log M<K log(R/d).                                         (7.5)
```

Since `r log(R/d)<eta<1/2`, (7.4)--(7.5) are incompatible for every
`q=q(k)`, including `q` proportional to `k`.

The top Laurent coefficient is itself ill-conditioned.  In the sharp local
model

```text
A_d=c(1/w-1/d),                                             (7.6)
```

the ratio of the true high jet to the isolated order-`q` pole jet is

```text
product_(j=1)^(q-1)(k-j)/(k+j).                             (7.7)
```

For `q=alpha k<k`, (7.7) is exponentially small in `k`; for `q>=k` it is
zero.  If the regular Laurent part is bounded only by `M`, even its first
lower layer relative to the top is of size `asymp M d q^2/(k+q)`.  Thus
differential powers reproduce both R142's tensor entropy and its Laurent
conditioning, rather than the linear divisor ledger of (2.4).

A proper rational response illustrates why mixed values return.  For

```text
C(U)=K U^m/[(1+U)product_j(1-x_jU)],       x_j>0,            (7.8)
```

the response has shifted Taylor support and is `O(1/U)` at infinity, but its
new poles are precisely

```text
U=1/x_j,
N-(1+1/x_j)D=0.                                             (7.9)
```

For distinct `x_1<...<x_m`, their residues alternate relative to the target:

```text
sgn(r_j/r_target)=(-1)^(j+1).                              (7.10)
```

Repeated nodes create higher-order value poles.  Normalizing the target
residue gives

```text
|K|=product_j(1+x_j),
|c_infinity|=product_j(1+1/x_j),
|K c_infinity|>=4^m.                                      (7.11)
```

So a growing proper rational filter pays at least `2^m` on one side and, for
`m>=2`, also introduces adverse mixed values.  The case `m=1` shifts support
only to `H^2`, which cannot cross the `eta<1/2` geometry.

## 8. Why positive kernels and standard density do not close the gate

A holomorphic divisor response which has nonnegative real part for every
possible favorable zero and also tends to zero at infinity cannot have
high-order localization.  After mapping to the reciprocal half-plane, the
minimum principle or Herglotz representation forces a nonzero positive-real
response to retain a `1/z` tail.  Exponential outer suppression requires a
sign or phase change and returns to the Turan problem.

The factors

```text
N-(1+omega)D                                                (8.1)
```

are additive combinations of completed functions.  They have no Euler
product, and ordinary Hecke/Artin log-free zero density does not apply.
Known value-distribution results concern point values or unconditioned
families, not a zero-free target disc after exponentially many local head
conditions.  Non-Euler linear combinations are also known to have abundant
zeros, sometimes already to the right of one, so a global zero-free theorem
is not a plausible substitute.

The surviving input must instead be target-local, signed, and conditional on
the selected head:

```text
control, jointly in the auxiliary field, the forced a-points
F_K(s)=1+omega in |s-z_*|<=R for a fixed finite root set, strongly enough
that their signed reciprocal-power packet cannot cancel the target.         (8.2)
```

No imported theorem supplies (8.2).  R155 proves that replacing it by
zero-free selection is impossible and that the deterministic truncated-zeta
common mode naturally has polynomially many mixed points.  Therefore the
nonlinear mechanism yields a sharp exponent calculation and an equally sharp
signed-divisor gate, but not a proof of either side of the fixed-strip
dichotomy.

Relevant value-distribution context includes Mine,
[*The value-distribution of Artin L-functions associated with cubic fields in
conductor aspect*](https://arxiv.org/abs/1905.11851),
and examples of zeros of non-Euler linear combinations in Booker--Thorne,
[*Zeros of L-functions outside the critical strip*](https://arxiv.org/abs/1306.6362),
and Andersson,
[*Joint universality on the half plane of absolute
convergence*](https://arxiv.org/abs/2008.05947).

Successor:
[`R154-COPRIME-FILTER-PACKET-AND-RESULTANT-GATE.md`](R154-COPRIME-FILTER-PACKET-AND-RESULTANT-GATE.md)
and
[`R155-NORMAL-FAMILY-MIXED-VALUE-INEVITABILITY-GATE.md`](R155-NORMAL-FAMILY-MIXED-VALUE-INEVITABILITY-GATE.md).
