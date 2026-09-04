# `LTRAD_full`: proof-or-counterexample run

**Date:** 2026-08-28  
**Verdict:** `LTRAD_full` was neither proved nor refuted.  The run did produce
one hostile-audited short-carrier no-go theorem, a conditional prime-only
reformulation, a reflected-difference leverage estimate, and a substantially
sharper description of the remaining obstruction.

The central conclusion is negative but useful:

```text
ordinary finite computation cannot reach the premise;
generic fourth-moment or sharp-four-cycle control is far too weak;
the simplest localized Fejer countercore is arithmetically impossible;
the surviving problem is source-sensitive carrier excitation and high-band
  cancellation.
```

No QP theorem, sharp global four-cycle bound, zeta zero-free strip, or Riemann
hypothesis is claimed.

---

## 1. Frozen statement and benchmark

To avoid the reversed positional convention in some older reports, use named
exponents:

```text
c_rad = radial conclusion exponent,
d_dir = directional premise exponent.
```

Fix `w=1/5`, `a=.01`, and `A=50/33`.  At scale `N`, let `Y` be an allowed
half-integer center with `N<=Y<=2 exp(w)N`.  For a prime interval `I` in the
shell and `t_0` in

```text
K_N=[N^(1/2),N^(A')],             A'<A,
```

put

```text
e(I,Y,t_0)=-(1/N) sum_(p in I) cos(t_0 log(p/Y)).     (1.1)
```

Let `S_Y` be the complete prime-power shell, let

```text
H_Y=[Y^.01,Y^(50/33)],
```

and let `r_+(H_Y;S_Y)` be the largest depth of an equal negative moment on
every node.  The centerwise statement audited here asserts, for every
sufficiently large `N`, every allowed `Y`, and every legal `I,t_0`, that

```text
LTRAD_full(c_rad,d_dir):
e(I,Y,t_0)>=N^(-d_dir)
  ==> r_+(H_Y;S_Y)>=N^(-c_rad).                       (1.2)
```

Fixed constants and `N^o(1)` margins can be inserted in the asymptotic
version.  If `E_N^-` is the supremum of the left side over legal events and
`R_N` the supremum of the radii over allowed centers, the weaker scale-global
statement

```text
E_N^->=N^(-d_dir) ==> R_N>=N^(-c_rad)                (1.2a)
```

would also suffice for the zeta bridge.  Statement (1.2) is the cleaner,
stronger centerwise form.

If

```text
h_Y(y)=sup_(t in H_Y) sum_n y_n cos(t|log(n/Y)|),
```

compact separation gives the exact dual identity

```text
r_+(H_Y;S_Y)=inf_(sum_n y_n=-1) h_Y(y).              (1.3)
```

Thus the premise of (1.2) must control **every** signed, adaptive dual vector
on all shell nodes.  This universal quantifier is the part that scalar prime
sum estimates do not address.

The useful strict benchmark is

```text
DPA exponent c_0=.019,
c_rad=.0189,
d_dir=.001.                                          (1.4)
```

For `d_dir=.001`, the audited Turan coverage inequality already holds with
`A'=1`, since

```text
r_d=(d_dir/A')^(1/6)=1/sqrt(10),
(1+r_d)/[2A'(1-r_d)]=.9624752955...<1.               (1.5)
```

Consequently `DPA(.019)` plus (1.2) at (1.4) would give a high-height
zero-free width

```text
(d_dir/A')^2=10^(-6).                                (1.6)
```

Both hypotheses remain unproved.

---

## 2. Why the useful premise cannot be computed directly

If `M` primes occur in `I`, then exactly

```text
e(I,Y,t_0)<=M/N.                                     (2.1)
```

The benchmark premise therefore needs at least `N^(.999)` primes.  A fixed
multiplicative shell contains only about `C_wN/log N` primes, so the necessary
asymptotic comparison is

```text
C_w/log N >= N^(-d_dir),
equivalently N^(d_dir) >= (log N)/C_w.                (2.2)
```

For every fixed positive `d_dir`, (2.2) eventually holds.  Hence the theorem
is not asymptotically vacuous.  But `N^.001` grows so slowly that the large
crossover is enormous.  In the PNT shell model, at the largest allowed center,

```text
d_dir=.019: log_10 N approximately 130.93,
d_dir=.001: log_10 N approximately 3967.99.           (2.3)
```

At the base center the corresponding estimates are `155.16` and `4400.80`.
These are model calibrations, not rigorous first-crossing theorems.

At the representative computed center `N=1000,Y=2400.5`,

```text
observed e                    = .030895,
exact prime-count ceiling     = .126,
benchmark threshold N^-.001  = .9931,
full radial interval          = [.169408,.169703].    (2.4)
```

The radial conclusion at (1.4) would fail there, but the directional premise
is impossible even before inspecting phases.  This is not a counterexample.

The expanded actual-prime scans found:

```text
base-center radial computations through N=4000;
allowed-center directional scans through N=3000;
all centers with both directional and radial brackets computed have their
  definite finite constant-one violation rectangles in d_dir>c_rad;
no sampled violation in the useful c_rad>d_dir wedge;
directional extrema roughly N^(-1/2) on the small grid;
radial effective exponents roughly 1/4 on adverse rows.
```

The adverse-center mnemonic `e roughly r_+^2` is not uniform in the center;
the observed effective powers range from about `1.93` to `3.2`.  More
importantly, typical `N^-1/2` behavior says nothing about the exceptional,
near-saturating event that a hypothetical zero would force at the scales in
(2.3).

---

## 3. New short-carrier no-go theorem

Fix `0<c<5/4-A/2`.  Along a family of half-integer centers tending to
infinity, let `P_Y` be a nonempty set of distinct ordinary primes whose
complete support lies in one physical interval of diameter at most
`Y^theta`, with fixed `0<=theta<1/2`.  For arbitrary signed coefficients with
sum one, put

```text
F_y(t)=sum_(p in P_Y)y_p cos(t|log(p/Y)|).
```

The audited argument proves

```text
inf_(t in H_Y)F_y(t)>=-Y^(-c)
  ==> theta >= (3A-2+6c)/11-o(1).                    (3.1)
```

At `A=50/33,c=.019`, the threshold is

```text
theta_min=.2417685950413223... .                     (3.2)
```

The mechanism has three steps.

1. Half-integrality of `Y` and parity of large primes produce a legal height
   `t_* asymp Y` at which every prime in a sufficiently short packet is an
   approximate common antipode.  Optimizing the central and off-center cases
   gives coordinate error

   ```text
   delta_p=1+cos(t_*|log(p/Y)|)
           <<Y^((4theta-2)/3).
   ```

2. Signed coefficients can escape that common antipode only by having large
   clustered sum/difference energy:

   ```text
   E_Y(y)^(1/2)>>Y^(2/3-11theta/6-o(1)).
   ```

3. The established actual-log fourth-moment range theorem converts this
   energy into a negative excursion elsewhere:

   ```text
   -inf F_y>>Y^(A/2-1/3-11theta/6-o(1)).
   ```

Comparing this with `Y^-c` gives (3.1).

This closes only the complete-support short-packet mechanism.  It does not
exclude a short core with a nonlocal correction tail, several packets, a
delocalized carrier, or proper-power coordinates.

There is a stronger rigidity statement for a literal one-sided harmonic
Fejer transfer.  Suppose `L=Y^(ell+o(1))=o(Y)`, `h>0`, the prime nodes are
distinct, the one-sided matching is injective, and the triangular Fejer
weights obey the exact perturbation budget

```text
B sum_j lambda_j|e_j|<<1/L.
```

If the log step is `o(Y^-1/2)`, integer second differences force the first
`floor(L/2)` matched primes into an exact arithmetic progression.  The
primorial divisibility obstruction then gives

```text
physical carrier diameter
  >>Y^(min(1,1/2+ell)-o(1)).                          (3.3)
```

For `ell=.019`, the required diameter is at least `Y^(.519-o(1))`.  This is
again a theorem about the literal one-sided matching, not arbitrary signed
or multicluster carriers.

---

## 4. Prime-only reformulation

Proper powers are not logically intrinsic to the Turan adapter.  Restrict
the moment curve to ordinary-prime coordinates and define `r_P`, `DPA_P`, and
`LTRAD_P` analogously.  Then

```text
DPA_P(c_0) + LTRAD_P(c_rad,d_dir),  c_0>c_rad,
```

gives the same conditional strip chain, because the source event and every
subsequent Turan step already use only ordinary primes.

This is a conditional reformulation, not a consequence of full-node DPA.
Coordinate projection has

```text
r_full<=r_P,                                          (4.1)
```

so an upper bound for `r_full` does not upper-bound `r_P`.  A future upper
theorem must separately produce a prime-supported DPA certificate.

The reformulation is nevertheless natural in the reverse direction.  A
zero-free strip of width `delta<=1/2` gives `DPA_P(c)` for every `c<delta`:
delete the proper powers from the canonical smooth von Mangoldt antenna.
Their total unnormalized contribution is

```text
O(Y^(1/2)log^2Y),
```

or `O(Y^(-1/2)log^2Y)` after normalizing the prime mass.  Thus a genuine
strip already supplies the stronger prime-only positive antenna.

---

## 5. What close reflected pairs can and cannot do

The smaller legal source aperture `A'=1` separates the low Turan height from
the full QP top `B=Y^A`.  For lower/upper prime pairs with

```text
B|u_i-u_i'|<=1,
```

the antisymmetric coordinate is suppressed at `t_0` by `t_0/B`.  In the
one-atom transverse-mixing scheme, normalize its dual by `y dot v=-1`.  The
exact transverse target for that scheme is

```text
epsilon_tr=Y^(-(c_rad-d_dir)+o(1))=Y^(-.0179+o(1)).  (5.1)
```

For any putative transverse separator with support function at most
`epsilon_tr`, the aggregate close-pair antisymmetric contribution to its
low-band leverage satisfies

```text
|F_(y^-)(t_0)|
  <<epsilon_tr Y^(-1/33+o(1))
  =Y^(-.04820303...+o(1)).                            (5.2)
```

Therefore close reflected differences cannot supply the normalized source
leverage.  In the separately hypothesized prime-only formulation, the
unpaired and symmetric ordinary-prime coordinates must supply it.  For
`LTRAD_full` as stated, proper-prime-power coordinates may supply leverage as
well.

This does **not** eliminate the antisymmetric sector.  Its allowed energy is
only bounded by

```text
E_Y(y^-)^(1/2)
  <<epsilon_tr Y^((2-A)/2+o(1))
  =Y^(.22452424...+o(1)),                             (5.3)
```

which grows.  Such a zero-carrier corrector may still cancel positive peaks
of the symmetric carrier near the top of the QP band.  Controlling that
high-band cancellation is the surviving reflected-pair problem.

---

## 6. Why the sharp four-cycle bound would not finish this adapter

The one-atom transverse mixing identity needs

```text
s_v>=Y^(-(c_rad-d_dir)+o(1))=Y^(-.0179+o(1)).        (6.1)
```

The baseline generic fourth-moment route gives only

```text
s_v>>Y^(-49/66-o(1)).                                (6.2)
```

The current proved uniform carry refinement improves this to

```text
s_v>>Y^(-29/44-o(1)).                                (6.3)
```

Even the desired coefficient-uniform weighted sharp endpoint (a quarter-power
operator consequence of the sharp four-cycle program), fed through the same
smooth transverse argument, would improve this only to

```text
s_v>>Y^(-41/66-o(1)).                                (6.4)
```

Since `41/66=.621212...`, (6.4) misses the exponent in (6.1) by about
`.603312`.  The sharp four-cycle theorem would be a major advance for the QP
upper problem, but it would not by itself prove `LTRAD` through generic
moment conversion.  The adapter must exploit the special long negative prime
event, not merely the ambient shell geometry.

---

## 7. The remaining strip route

There are two independent open gates.  The QP-upper gate is to prove the
prime-supported statement `DPA_P(.019)`.  It is not part of `LTRAD_P`; it is
needed afterward to turn `LTRAD_P` into a strip.

For the adapter gate, condition on a long source event and put

```text
lambda = uniform probability on its M primes,
D=-lambda dot a_P(t_0)=Ne(I,Y,t_0)/M,
v=a_P(t_0)+Dq_P.                                     (7.1)
```

Here `M/N<1` for all sufficiently large project shells, so the benchmark
event gives `D>=N^(-.001+o(1))`.  The exact adapter-specific target is

```text
s_v=inf_(y:y dot v=-1) h_Y(y)>=Y^(-.0179+o(1)).      (7.2)
```

For a hypothetical counterexample to (7.2), split its dual vector as

```text
y=y_car+y_corr,                                      (7.3)
```

where `y_corr` is the aggregate antisymmetric part on `B^-1`-close reflected
pairs and `y_car` contains the symmetric, unpaired, and non-close coordinates.
The proved leverage estimate gives

```text
F_corr(t_0)=o(Y^(-.0179+o(1))),
E_Y(y_corr)^(1/2)<<Y^(.22452424...+o(1)).             (7.4)
```

It is not known that `y_car` is delocalized.  The short-carrier theorem applies
to it only if one separately establishes that its complete support, carrier
normalization, and global-floor hypotheses match that theorem.

Working entirely in the conditional prime-only framework, the missing
source-sensitive theorem can now be stated without that localization
assumption: for every decomposition (7.3) with `y dot v=-1` and (7.4), prove

```text
sup_(t in H_Y)[F_car(t)+F_corr(t)]
  >=Y^(-.0179+o(1)).                                  (7.5)
```

This must prove both that the source-normalized carrier has a large enough
positive excitation and that the corrector cannot hide all such excitations.
Noncancellation alone is insufficient.

Once (7.5) is proved, transverse mixing gives

```text
r_P>=D s_v/(1+s_v)
   >=N^(-.001)N^(-.0179+o(1))
   =N^(-.0189+o(1)).                                  (7.6)
```

Thus the full conditional strip route is:

```text
1. prove prime-supported DPA_P(.019);
2. condition on the long source event e>=N^-.001;
3. prove the universal source-sensitive excitation/noncancellation theorem
   (7.5), hence LTRAD_P(.0189,.001);
4. combine the two independent gates and invoke Turan.
```

Statement (7.5) is not a standard large sieve.  It must retain both the actual-prime
mask and the source normalization.  Equivalently, it is a carrier/corrector
noncancellation or source-sensitive vector-valued inverse theorem.

The present evidence raises the cost of constructing a counterexample—the
complete-support short Fejer carrier is excluded—but a short core with
nonlocal correction tails remains open, as does the general carrier/corrector
configuration.  The distance to the adapter is therefore still qualitative:
one new theorem of the type (7.5), not an exponent optimization of an existing
moment bound.  The full strip route additionally needs the independent
prime-supported upper theorem `DPA_P`.

---

## 8. Reproducibility and status

Detailed artifacts:

```text
results/ZETA23-QP-LTRAD-FULL-ACTUAL-PRIME-NUMERIC-AUDIT-2026-08-28.md
results/ZETA23-QP-LTRAD-ACTUAL-PRIME-CLUSTER-HARD-CORE-NOGO-2026-08-28.md
results/ZETA23-QP-LTRAD-PRIME-ONLY-AND-REFLECTED-DIFFERENCE-REDUCTION-2026-08-28.md
src/qp_ltrad_full_numeric_audit.py
src/qp_ltrad_hereditary_gate.py
```

Regression command:

```bash
PYTHONPATH=src python3 -m pytest -q \
  src/test_qp_ltrad_full_numeric_audit.py \
  src/test_qp_radialization_lab.py \
  src/test_qp_radialization_mass_gate.py \
  src/test_qp_ltrad_hereditary_gate.py \
  src/test_qp_radial_covariance_gate.py \
  src/test_qp_transverse_fourth_moment_gate.py \
  src/test_qp_transverse_sharpness_lab.py
```

The final run reports `48 passed`.  The tests replay exponent algebra and
finite numerical diagnostics; they do not formally verify the analytic
short-carrier proof.

```text
exact statement and polarity audit:                   PASS;
expanded finite actual-prime audit:                    PASS;
useful premise reached computationally:                NO;
short complete ordinary-prime carrier no-go:           PROVED, SCOPE-RESTRICTED;
literal one-sided Fejer transfer rigidity:              PROVED, SCOPE-RESTRICTED;
prime-only bridge reformulation:                        PROVED CONDITIONAL;
close-reflected low-band leverage suppression:          PROVED;
high-band carrier/corrector noncancellation:             OPEN;
LTRAD_full or LTRAD_P:                                  OPEN;
uniform zero-free strip:                                NOT PROVED.
```
