# R131 functional-equation paired-recurrence gate

Status: the functional equation does give an exact way to reconstruct the
left half of a symmetric contour from the right half.  For
`F_tau(s)=xi(s+i tau)`, the relevant symmetry is

```text
F_tau(1-conj(s))=conj(F_tau(s)).                       (0.1)
```

Equivalently, holomorphic reflection exchanges the paired shifts
`+tau` and `-tau`.  This does not yield zero replication from ordinary
right-half-plane universality.  There are two exact obstructions.  First,
completed translates tend exponentially to zero on fixed compact sets;
the gamma normalization which converts them back to zeta recurrence is
not compatible with (0.1).  Second, a connected symmetric contour records
only the total number of zeros on both sides of the critical line and so
does not retain the real-part localization needed for zero density.  The
natural nested-contour subtraction which restores that localization has a
right-hand difference region whose boundary is a complete closed contour
around the original off-line zero.  Its required estimate is exactly the
zero-bearing self-recurrence/Rouche estimate of R122 again.

Products of the paired shifts double the unlocalized divisor.  Their
quotient has reciprocal functional symmetry, but its zero and pole counts
cancel.  Neither construction changes the recurrence exponent required by
known zero-density bounds.  This closes this functional-equation
architecture, not the possibility of a fixed zero-free strip.

Date: 2026-08-08.

Predecessors:

* [`R122-ZERO-REPLICATION-DENSITY-GATE.md`](R122-ZERO-REPLICATION-DENSITY-GATE.md)
  for the quantitative Rouche/zero-density replication lemma;
* [`R126-PUNCTURED-CONTOUR-ALL-MOMENT-AND-KEYHOLE-GATE.md`](R126-PUNCTURED-CONTOUR-ALL-MOMENT-AND-KEYHOLE-GATE.md)
  for the all-moment cost of closing a contour gap; and
* [`R127-NEAR-ONE-MIXED-CONTOUR-DENSITY-GATE.md`](R127-NEAR-ONE-MIXED-CONTOUR-DENSITY-GATE.md)
  for the mixed universality/Euler-contour density ledger.

## 1. Exact paired-shift symmetries

Write

```text
h(s) = (1/2)s(s-1) pi^(-s/2) Gamma(s/2),
xi(s)=h(s)zeta(s).                                    (1.1)
```

Then `xi` is entire and

```text
xi(s)=xi(1-s),        xi(conj(s))=conj(xi(s)).         (1.2)
```

For real `tau`, put

```text
F_tau(s)=xi(s+i tau).                                 (1.3)
```

There are two useful reflections:

```text
J(s)=1-s,                 R(s)=1-conj(s).             (1.4)
```

The first is holomorphic and the second is reflection across the critical
line.  Directly from (1.2),

```text
F_tau(J(s))=F_(-tau)(s),
F_tau(R(s))=conj(F_tau(s)).                            (1.5)
```

Thus paired `+tau,-tau` data close a contour under `J`; after conjugacy,
one `+tau` translate already closes it under `R`.  This is a genuine exact
identity, not an approximation.

For later use define

```text
P_tau(s)=F_tau(s)F_(-tau)(s),
Q_tau(s)=F_tau(s)/F_(-tau)(s).                         (1.6)
```

Away from the poles of the quotient,

```text
P_tau(1-s)=P_tau(s),
Q_tau(1-s)=1/Q_tau(s).                                (1.7)
```

The product adds the two divisors; the quotient subtracts them.  Section 6
shows why neither operation produces the desired positive localized
divisor.

## 2. The completion cannot itself recur

Let `K` be a fixed compact set in a bounded vertical strip.  Stirling's
formula, uniformly for `s=sigma+it` in `K`, gives

```text
|h(s+i tau)|
 =C_K(s) tau^(sigma/2+3/2) exp(-pi tau/4)
   (1+O_K(1/tau)),                                    (2.1)
```

where `C_K(s)` is bounded above and below after the harmless factor
`exp(-pi t/4)` is included.  Standard polynomial bounds for zeta in a
fixed strip consequently imply

```text
sup_(s in K)|F_tau(s)|
 <=exp(-pi tau/4) tau^C_K ->0,                        (2.2)

sup_(s in K)|P_tau(s)|
 <=exp(-pi tau/2) tau^C_K ->0.                        (2.3)
```

Therefore neither `F_tau` nor `P_tau` can recur to the nonzero boundary
values of `xi` or `xi^2` on a fixed Rouche contour.  The functional
equation has not removed the gamma decay.

On a right-hand region contained in `0<Re(s)<1`, `h` is holomorphic and
nonzero.  The exact local normalization

```text
A_tau(s)=h(s)/h(s+i tau)                              (2.4)
```

gives

```text
A_tau(s)F_tau(s)=h(s)zeta(s+i tau).                   (2.5)
```

Thus zeta self-recurrence would compare the right side with `xi(s)`.  But
`A_tau` does not obey the reflection law required in (0.1): in general

```text
A_tau(1-conj(s)) != conj(A_tau(s)).                   (2.6)
```

For the paired product the analogous normalization is

```text
B_tau(s)=h(s)^2/[h(s+i tau)h(s-i tau)],               (2.7)

B_tau(s)P_tau(s)
 =h(s)^2 zeta(s+i tau)zeta(s-i tau).                  (2.8)
```

It also fails the required reflection symmetry.  A scalar normalization
cannot convert a simultaneous zeta recurrence at two points of distinct
real parts into completed recurrence: under
`zeta(s+i tau)=zeta(s)+o(1)`, (2.1) requires scalar sizes differing by a
power `tau^((sigma_1-sigma_2)/2)` at the two points.  A variable analytic
normalization can remove the gamma factor locally, but making it
reflection-compatible reintroduces the full divisor constraint, as the
next lemma makes precise.

The paired gamma factor has the sharper analytic asymptotic

```text
h(s+i tau)h(s-i tau)
 =pi (2pi)^(-s) tau^(s+3) exp(-pi tau/2)
   (1+O_K(1/tau)).                                    (2.9)
```

This follows from
`Gamma(z+iy)Gamma(z-iy)=2pi exp(-pi y)y^(2z-1)(1+O(1/y))`.
Thus the paired magnitudes cancel, but a horizontal factor
`(tau/(2pi))^s` remains.  Even the canonical symmetrization consequently
has a visible power defect.  For an analytic function `C`, write

```text
C^sharp(s)=conj(C(1-conj(s))).                        (2.10)
```

On a simply connected zero-free neighborhood one can replace `B_tau` by
the reflection-compatible geometric mean

```text
M_tau=(B_tau B_tau^sharp)^(1/2).                      (2.11)
```

Stirling's formula gives, for fixed `s` with `sigma=Re(s)>1/2`,

```text
|M_tau(s)/B_tau(s)|
 =|h(1-s)/h(s)| (tau/(2pi))^(sigma-1/2)
   (1+o(1)).                                          (2.12)
```

Thus symmetrizing the natural zeta normalization changes the would-be
target by a nonconstant power of `tau`.  Fixed-target joint or hybrid
universality does not absorb this factor.  Removing it again returns to
the nonsymmetric normalization (2.7).

## 3. Half-contour Rouche is still full Rouche

The rectangle makes the geometry explicit.  For fixed `a,h>0` and real
`v`, let

```text
Omega_(a,h,v)
 ={s:|Re(s)-1/2|<a, |Im(s)-v|<h}.                    (3.1)
```

It is invariant under `R`.  Its right half-boundary is not just the right
vertical edge: it consists of that edge and the right halves of both
horizontal edges, forming a path between
`1/2+i(v-h)` and `1/2+i(v+h)`.  Reflection supplies the other three half
edges.  Hence horizontal connectors have not disappeared; they have been
moved into the right-hand compact, and their two joining points lie
exactly on the critical line.

Let `Omega` be a Jordan domain invariant under `R`, and suppose its
boundary is the union of a right arc `Gamma_+` and its reflected left arc.
The two endpoints lie on `Re(s)=1/2`.  Let `f` and `g` be holomorphic near
the closure, with no boundary zeros, and suppose

```text
f(R(s))=conj(f(s)),       g(R(s))=conj(g(s)).          (3.2)
```

### Lemma 3.1 -- symmetric half-boundary lemma

If `M` is holomorphic, zero-free, and satisfies the same reflection law,
then

```text
|M(s)f(s)-g(s)|<|g(s)|       for s in Gamma_+         (3.3)
```

implies

```text
Z(f;Omega)=Z(g;Omega),                                (3.4)
```

with multiplicity.

**Proof.**  Reflection turns (3.3) into the identical inequality on the
left arc.  Rouche applies on the whole boundary.  Since `M` is zero-free,
`Mf` and `f` have the same zeros.  QED.

Consequently, if the two zero counts differ, every reflection-compatible
normalizer must fail the Rouche inequality somewhere on the right half.
Symmetry halves the set on which one checks the estimate; it does not
weaken its topological content.

The endpoints expose the same fact in one real variable.  On the critical
line,

```text
F_tau(1/2+it)=xi(1/2+i(t+tau)) is real.               (3.5)
```

A zero-free normalizer satisfying (3.2) is real and of constant sign on a
critical-line joining segment.  It cannot delete a sign change or zero of
(3.5).  Deleting neighborhoods of the two endpoints returns exactly to
the punctured-contour derivative problem of R122 and R126.

There is also a domain-of-universality issue.  A symmetric Jordan curve
which reaches both sides of the critical line must meet the line at least
twice.  Standard universality controls fixed compacta strictly inside
`1/2<Re(s)<1`, not the two joining points.  Functional symmetry therefore
does not provide a free endpoint theorem.

## 4. What a connected symmetric contour loses

Suppose a hypothetical zero

```text
rho_0=beta+i gamma_0,       beta>1/2                   (4.1)
```

lies in an `R`-invariant domain `Omega`.  Its reflected zero
`1-conj(rho_0)` lies there as well.  Lemma 3.1 could in principle transfer
the **total** zero count in `Omega` to a high translate.

That conclusion does not say that the translated domain contains a zero
with real part near `beta`.  The new zeros may all lie on, or arbitrarily
near, the critical line.  Accordingly the incidence argument can use only
the total zero count `N(T)`, of order `T log T`; it cannot use
`N(sigma,T)=o(T)` for a fixed `sigma>1/2`.  Positive-density recurrence of
an unlocalized total count is therefore compatible with the available
zero-counting bounds.

This is not just an inefficient choice of contour.  There is an exact
dichotomy:

```text
connected R-symmetric contour     closes from one right arc,
                                  but loses Re(s)>1/2 localization;

right-localized contour           retains the zero-density contradiction,
                                  but its right boundary is closed.       (4.2)
```

The next section proves the second line for the strongest natural attempt
to combine the two advantages.

## 5. Nested symmetric contours restore the original obstruction

Take two `R`-symmetric contours which use the same thin corridors from the
critical line into `Re(s)>sigma_*`, where

```text
1/2<sigma_*<beta.                                    (5.1)
```

Let their right arcs split only after reaching that line, with the outer
and inner arcs enclosing a right-hand lens `L` containing `rho_0`.  They
may be chosen so that

```text
closure(L) subset {Re(s)>sigma_*},
zeta has no zero on boundary L.                       (5.2)
```

The reflected lens `R(L)` contains the mate of `rho_0`.  Subtracting the
two symmetric argument-principle counts cancels the common corridors and
gives

```text
Z(f;Omega_outer)-Z(f;Omega_inner)
 =Z(f;L)+Z(f;R(L))
 =2Z(f;L)                                             (5.3)
```

for every function with the reflection law and no boundary zeros.

This looks like a way to recover real-part localization after using only
right arcs.  But the portions of those arcs which do not cancel are
exactly

```text
boundary L.                                           (5.4)
```

They form a complete closed contour in the universality strip.  If

```text
m_L=min_(s in boundary L)|zeta(s)|,                   (5.5)
```

then the estimate which would transfer (5.3) is precisely

```text
sup_(s in boundary L)
 |zeta(s+i tau)-zeta(s)|<m_L.                         (5.6)
```

Rouche applied to (5.6) is the original local zero-replication theorem.
The compact `boundary L` has disconnected complement, and its target has
nonzero winding about zero.  Ordinary empty-interior universality cannot
approximate it through the Rouche threshold; the zero-free random Euler
product has winding zero there.  Opening (5.4) by a gap returns to the
quantitative unwinding gates of R122 and R126.

### Theorem 5.1 -- localization-versus-closure gate

Any subtraction of `R`-symmetric contour counts which cancels the
critical-line part and isolates zeros in a fixed region
`Re(s)>sigma_*>1/2` leaves, after cancellation, a closed right-hand cycle
surrounding that region.  Transferring its nonzero count by a uniform
boundary homotopy is equivalent to a zero-bearing Rouche recurrence on
that cycle.

**Proof.**  The formal difference of the two oriented boundaries is a
one-cycle supported away from the common corridors.  Every component with
nonzero winding around a localized zero is a closed right-hand cycle.  On
that cycle the two argument-principle integrals differ by the localized
zero count.  A boundary homotopy which avoids zero transfers that count;
conversely, a Rouche-small homotopy is such a homotopy.  In the nested
Jordan case this cycle is exactly (5.4), proving the claim without any
homology formalism.  QED.

Thus the seemingly promising two-contour cancellation does not merely
run short of an estimate.  Once it has enough localization to invoke zero
density, it has reconstructed the exact closed contour that functional
symmetry was meant to avoid.

The missing datum can also be written as one integer.  On `boundary L`
put, wherever the boundary values are nonzero,

```text
q_tau(s)=zeta(s+i tau)/zeta(s).                       (5.7)
```

Then

```text
(1/(2 pi i)) integral_(boundary L) d log q_tau
 =Z(zeta(.+i tau);L)-Z(zeta;L).                       (5.8)
```

Approximation on separately opened outer and inner arcs controls local
branches of `log q_tau`, but does not determine the integer (5.8).  The
integer can change through either joining gap.  Proving that it vanishes
on a sufficiently dense set is exactly the signed localized-winding
estimate, not a consequence of the functional equation.

## 6. Products and quotients of the paired shifts

### 6.1 The product

The product `P_tau` has exact holomorphic symmetry, but

```text
Z(P_tau;Omega)
 =Z(F_tau;Omega)+Z(F_(-tau);Omega).                   (6.1)
```

It therefore doubles the unlocalized critical-strip divisor.  Direct
comparison with `xi(s)^2` is impossible by (2.3).  The normalization (2.7)
reduces right-hand control to joint recurrence of
`zeta(s+i tau)zeta(s-i tau)` toward `zeta(s)^2`, but breaks the symmetry
which was supposed to close the left half.  If a symmetric zero-free
normalizer nevertheless achieved the half-boundary Rouche estimate,
Lemma 3.1 says it would already prove the full zero-count recurrence.

### 6.2 The quotient

The quotient has the attractive cancellation of the main gamma size, but
its divisor is signed:

```text
(1/(2 pi i)) integral_(boundary Omega) Q_tau'/Q_tau
 =Z(F_tau;Omega)-Z(F_(-tau);Omega).                   (6.2)
```

On a domain invariant under `s ->1-s`, (1.7) pairs every numerator zero
with a denominator zero, so the right side is zero.  More generally, a
positive winding of the quotient can be supplied by a missing denominator
zero just as well as by a new numerator zero.  It cannot force a zeta zero
without a separate pole exclusion, and that exclusion reinstates the
individual zero problem.

The uncompleted paired product

```text
Z_tau(s)=zeta(s+i tau)zeta(s-i tau)                   (6.3)
```

does not secretly retain the completed symmetry.  If
`zeta(s)=chi(s)zeta(1-s)`, then

```text
Z_tau(1-s)
 =Z_tau(s)/[chi(s+i tau)chi(s-i tau)].                (6.4)
```

The missing cocycle is exactly the gamma factor removed in (2.7).

## 7. Joint and hybrid recurrence on the right

On a conjugation-invariant right-hand compact set `K`, one translate
already controls both signs:

```text
sup_K |zeta(s+i tau)-zeta(s)|<epsilon

implies

sup_K |zeta(s-i tau)-zeta(s)|<epsilon.                (7.1)
```

Indeed, apply the first estimate at `conj(s)` and conjugate.  For a compact
not invariant under conjugation one may enlarge it to `K union conj(K)`.
This shows that the paired shifts do not provide two independent random
Euler tails whose errors might be averaged.

If `K` is an open arc or a finite tree of arcs strictly inside the
universality strip, ordinary or hybrid universality gives positive-density
control because the complement is connected and there is no enclosed
winding.  If the arcs are combined in the localized cycle (5.4), the
complement becomes disconnected and the target carries the hypothetical
zero.  The limiting random Euler product is zero-free, so the Rouche ball
has probability zero.  Finite Euler-phase recurrence on `Re(s)>1` has the
same issue: a contour wholly controlled there cannot enclose a zero with
`beta<1`, while joining it to a left excursion recreates the transition
and density losses quantified in R127.

There is no hidden density gain from asking for both signs.  In the R127
geometry with right margin `eta`, direct absolute-Euler control at fixed
accuracy uses

```text
P=exp((u+o(1))/eta)
```

prime coordinates and has phase-cylinder density

```text
exp{-exp(u/eta+o(1/eta))}.                            (7.2)
```

The same phase return controls `+tau` and `-tau`, since their Euler phases
are complex conjugates.  Hence pairing does not square this already tiny
density, but neither does it enlarge it; (7.2) remains smaller than every
fixed power of `eta`, while closing the transition still requires the
localized winding event.

The functional equation therefore improves neither the support nor the
density of the relevant recurrence event.

## 8. Quantitative zero-density ledger

Let `L` be as in (5.2), let its vertical diameter be `H_L`, and suppose it
contains `j>=1` zeros.  Define the actual localized recurrence set

```text
U_L(T,epsilon)
 ={tau in [T,2T]:
   sup_(s in boundary L)|zeta(s+i tau)-zeta(s)|<epsilon},

0<epsilon<m_L.                                       (8.1)
```

The integrated Rouche argument of R122 gives

```text
j meas U_L(T,epsilon)
 <=H_L N(sigma_*;T+O_L(1),2T+O_L(1)).                (8.2)
```

The Guth--Maynard corollary imported in R98 and R122 is

```text
N(sigma,T)<=T^[(30/13)(1-sigma)+o(1)].                (8.3)
```

Thus a recurrence lower bound

```text
meas U_L(T,epsilon)>=T^(kappa-o(1))                   (8.4)
```

would exclude the zero whenever

```text
kappa>(30/13)(1-sigma_*).                             (8.5)
```

Equivalently it would force

```text
beta<=1-13kappa/30+r                                  (8.6)
```

when `sigma_*=beta-r`.  Positive-density recurrence contradicts the
classical Bohr--Landau estimate `N(sigma,T)=o(T)` for every fixed
`sigma>1/2`.

Adding the `-tau` translate only doubles both the replicated-zero incidence
and the zero-counting side of (8.2); it does not change the exponent.  For
a connected symmetric contour without the subtraction in Section 5,
`sigma_*` falls back to `1/2` and (8.2) is replaced by a total-zero bound
of order `T log T`, which is useless against a set of measure at most `T`.

## 9. Verdict

The proposed functional-equation mechanism has one real success:

```text
right-half completed data + exact symmetry
        -> full symmetric-contour data.               (9.1)
```

It fails at the next logical arrow:

```text
full symmetric count
        -/-> a zero with Re(s)>=beta-r.                (9.2)
```

Restoring (9.2) by nested count cancellation produces the closed localized
cycle (5.4), and control of that cycle is exactly the self-recurrence event
whose quantitative density is the open gate in R122 and R126.  Gamma
normalization, paired products, quotients, hybrid universality, and finite
Euler recurrence do not alter this topology or the exponent (8.5).

Accordingly this route proves neither a fixed zero-free strip nor the
failure of every such strip.  It rules out the claim that functional
equation symmetry by itself converts ordinary right-half-plane recurrence
into zero replication.  A genuine successor would have to estimate the
localized winding event (5.6), or an equivalent signed contour-count
difference, with density strong enough for (8.5); that is precisely the
individual-zero input still missing from the existing literature.
