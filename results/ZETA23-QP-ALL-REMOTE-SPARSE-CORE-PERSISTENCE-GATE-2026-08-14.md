# QP all-remote sparse-core and persistence gate

**Date:** 2026-08-14

**Verdict:** every legal positive all-remote AP antipode has a deterministic
sparse negative-peak core, but that theorem is saturated by the newly proved
positive harmonic chambers and gives no finite-aperture exclusion.

If the depth is `r` and the AP step is `tau>=1`, at least

```text
r/(2-r)                                                 (0.1)
```

of the barycentric weight lies on at most

```text
O(r^-2 Y^o(1))                                          (0.2)
```

harmonics.  Hence one AP weight is at least

```text
r^3 Y^-o(1).                                            (0.3)
```

At `r=Y^(-kappa_promote+eta)`, (0.3) has exponent

```text
-3*kappa_promote+3*eta=-.0540909702+3*eta.             (0.4)
```

This does not force a low-cost representation on the core: the complement
can carry essential transverse coordinates.  More decisively, the explicit
all-remote chamber

```text
1/2+(c/M)sum_(k=M)^(2M-2)cos(k theta)
   +cos((2M-1)theta)                                    (0.5)
```

has fixed depth, one weight of order one, and all remaining weights of order
`1/M`.  It satisfies (0.1)--(0.3) with room to spare.

An exact Neumann-series calculation gives a phase persistence radius for
every strict positive Cramer cell.  Even under optimistic polynomial
conditioning, the guaranteed radius of (0.5) is only inverse-polynomial in
`M`; the Guth--Maynard dilation shadow has a much larger total-measure upper
bound.  Therefore shadow measure plus persistence cannot turn an
almost-everywhere obstruction into a deterministic no-hit theorem.

The sole remaining all-remote AP question is the growing-dimensional first
return of the actual prime-log flow before `B/M=Y^(17/33+o(1))`.  Nothing in
this audit proves either a visit or nonreturn in that aperture.  No QP
promotion or zero-free strip follows.

---

## 1. Deterministic sparse negative-peak core

Let

```text
a(t)=(cos(tu_j))_(j<=M),
S_Y(t)=sum_j cos(tu_j),
K={M,...,2M-1}.                                         (1.1)
```

Suppose

```text
sum_(k in K)w_k a(k tau)=-r q_0,
w_k>=0,       sum_k w_k=1,       tau>=1.                (1.2)
```

### Theorem 1.1 (sparse-core theorem)

Define

```text
K_-={k in K:S_Y(k tau)<=-rM/2}.                         (1.3)
```

Then

```text
sum_(k in K_-)w_k>=r/(2-r).                             (1.4)
```

If the absolute large-value set at threshold `rM/2` is covered by `R`
radius-one intervals, then

```text
#K_-<=3R,                                               (1.5)
max_k w_k>=r/[3(2-r)R].                                 (1.6)
```

At the promotion scale, Guth--Maynard gives

```text
R<=r^-2Y^o(1),                                         (1.7)
```

and (1.6) becomes (0.3).

#### Proof

Pair (1.2) with `q_0` and divide by `M`:

```text
sum_k w_k S_Y(k tau)/M=-r.                              (1.8)
```

On `K_-` the normalized summand is at least `-1`; on its complement it is
greater than `-r/2`.  If the weight of `K_-` is `alpha`, (1.8) forces

```text
-r>=-alpha-(1-alpha)r/2,
```

which rearranges to (1.4).  Since the points `k tau` are at least one apart,
any closed interval of length two contains at most three of them.  This
proves (1.5), and pigeonhole gives (1.6).  Finally (1.7) is the established
actual-integer large-value packet theorem with cost parameter `1/r`.  QED

The theorem retains the negative sign in the mass statement, although the
packet cover itself is for the larger absolute-value set.

---

## 2. Exact persistence of a positive determinant cell

For phases `theta=(theta_j)` and distinct positive harmonics `k_l`, put

```text
A(theta)_(j,l)=cos(k_l theta_j),
c(theta)=A(theta)^(-1)q_0.                              (2.1)
```

If every `c_l<0`, then the corresponding positive depth and weights are

```text
C=sum_l|c_l|,       r=1/C,       w_l=-c_l/C.            (2.2)
```

### Lemma 2.1 (certified sign-persistence radius)

At a strict positive point define

```text
beta=||A(theta)^(-1)||_infinity,
m=min_l(-c_l),
K_max=max_l k_l.                                        (2.3)
```

Every phase vector `theta'` with

```text
||theta'-theta||_infinity<=rho,

rho=min{1/(2 beta M K_max),
        m/(4 beta K_max C)}                             (2.4)
```

has an invertible evaluation matrix and all its Cramer coefficients remain
negative.  Its depth is at least

```text
1/(C+Mm/2).                                             (2.5)
```

#### Proof

Let `E=A(theta')-A(theta)`.  The cosine Lipschitz bound gives

```text
||E||_infinity<=M K_max rho.                            (2.6)
```

The first term in (2.4) makes
`||A^-1E||_infinity<=1/2`; hence the Neumann series gives

```text
||(A+E)^(-1)||_infinity<=2 beta.                        (2.7)
```

Because `sum|c_l|=C`, the sharper vector estimate is

```text
||Ec||_infinity<=K_max rho C.                           (2.8)
```

The resolvent identity and the second term in (2.4) now give

```text
||c(theta')-c(theta)||_infinity
 <=2 beta K_max rho C<=m/2.                             (2.9)
```

Thus every coefficient remains negative and its new TV is at most
`C+Mm/2`, proving (2.5).  QED

Along the actual flow `theta_j=tau u_j`, this supplies a step interval of
radius at least `rho/max_j|u_j|` around any strict hit.

---

## 3. Why persistence plus shadow measure still fails

For the uniform all-remote template (0.5), with fixed small `c>0`,

```text
C=2[1+c(M-1)/M] asymp1,
r=1/C asymp1,
m=2c/M,
K_max=2M-1.                                             (3.1)
```

If its selected interpolation minor has inverse norm `beta`, Lemma 2.1
gives

```text
rho>>1/(beta M^2).                                      (3.2)
```

The universal chamber theorem guarantees a finite `beta` but does not give
a uniform polynomial bound for the rank-selected minor.  A generic
Cauchy--Binet/cofactor estimate is exponential in `M`; numerical explicit
minors are much better conditioned, but that observation is not an
asymptotic proof.

Even granting the optimistic `beta=Y^o(1)`, (3.2) is only

```text
rho=Y^(-2+o(1)),                                        (3.3)
```

because `M=Y^(1-o(1))`.  For fixed depth the dilation-shadow theorem gives
only a total step measure `Y^o(1)`, not `o(Y^-2)`.  At promotion depth its
upper bound is larger, `Y^(2kappa_promote+o(1))`.  A shadow of that measure
can plainly contain an interval of radius (3.3).  No contradiction results.

The torus box in Lemma 2.1 has Haar log-volume

```text
M log(rho/pi).                                          (3.4)
```

For any inverse-polynomial `rho`, this is `-Theta(M log M)`.  Kronecker
recurrence therefore remains compatible with an exponentially late first
visit.  Volume is not a deterministic lower hitting-time theorem in any
case.  Thus neither the chamber's openness nor the almost-everywhere shadow
settles the legal polynomial aperture.

---

## 4. Disposition

```text
negative exceptional harmonic mass r/(2-r):       PROVED;
exceptional harmonic count O(r^-2 Y^o):            PROVED;
largest AP weight >=r^3 Y^-o:                       PROVED;
strict Cramer-cell persistence radius:              PROVED;
sparse core contradicts all-remote chamber:         FALSE;
shadow measure exceeds every cell persistence:      NOT PROVED;
actual flow avoids chamber before B/M:              OPEN;
actual flow hits chamber before B/M:                OPEN;
QP-PROMOTE / strip:                                  NOT PROVED.
```

The next theorem must be an actual-prime **finite-aperture nonreturn** result
or an interval-certified legal hit.  Another coefficient-sign, root-count,
openness, packet-measure, or generic recurrence argument cannot decide it.

## 5. Replay

```bash
PYTHONPATH=src python3 -m pytest -q src/test_qp_remote_sparse_core.py
python3 results/verify_zeta23_qp_remote_sparse_core.py
```

The current replay is `3 passed`, and the verifier prints `PASS`.

