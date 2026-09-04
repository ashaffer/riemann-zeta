# QP small/small final focused campaign closeout

**Date:** 2026-08-27  
**Verdict:** this campaign proves a new one-tower rigidity theorem and a
subpolynomial-remainder branch of the dyadic reciprocal large sieve.  It does
not prove the full dyadic theorem or the sharp four-cycle bound.  The remaining
analytic problem is now sharply isolated as a signed product-action/HSM
estimate inside one canonical rational tower.

## 1. New theorem obtained

At dyadic scale `K R^2=q`, let `U=(p,P)` be a realized primitive direction,
with

```text
rho_U=c*p-C*P,       ||U||_infinity*R<=D,
|rho_U|*R^2<=2D^2,   sqrt(D)<=R<=D.
```

For any other radius-`R` realized primitive direction `V=(s,S)`,

```text
C*det(U,V)=rho_U*s-rho_V*p,
|C*det(U,V)|<=4D^2/R<C.
```

Integrality forces `det(U,V)=0`.  Thus one hard direction absorbs every
radius direction: the entire nontrivial radius graph is one parallel tower,
not a collection of competing continued-fraction directions.

The full integer orbit has at most `|rho_U|` contiguous tower lines.  Distinct
lines satisfy

```text
|rho_U|*|Delta b|>=C-2D|p|,
|rho_U|*|Delta B|>=c-2D|P|,
```

so they are separated by `asymp q/|rho_U|`.  Their two-dimensional stationary
gradient images are separated by

```text
>>K/|rho_U|>=q/(2D^2)=q^(1/33)/2.
```

This proves stationary-index multiplicity one.  Combining the line count with
the existing one-fan estimate also proves

```text
sum_(K<h<=2K)|S_gamma(h)|^2
 <<|rho_U|^4*(q^2/K)q^o(1).
```

Consequently the desired dyadic estimate holds on every hard-tower branch
with `|rho_U|=q^o(1)`.  This includes bounded remainder and polylogarithmic
bottom-band regimes, but no fixed-power portion sufficient for the global
four-cycle theorem.

## 2. Exact reason the last aggregation does not follow

For the reciprocal B-process, stationarity of

```text
A/(x*y)+m*x+n*y
```

gives, with `f=A/(x*y)`,

```text
f+m*x+n*y=3f,       f^3=A*m*n.
```

The scalar stationary action is therefore

```text
3*(A*m*n)^(1/3).
```

It forgets the separated two-dimensional stationary index and remembers only
the product `m*n`.  Hence disjoint gradient supports do not imply scalar
Bessel orthogonality.  Exact product aliases are divisor-controlled, but the
near-product terms are precisely the signed Möbius/HSM discrepancy left open
in the previous closeout.

## 3. The canonical tower does not add a saving congruence

There is an exact critical family

```text
F=N^8, R=N^25, q=2FR, D=F^2,
d=(R,R+1), e=(-1,-1),
(C,c)=F*d+e, gamma=(c,C).
```

For `z_(m,n)=m*d+n*e`, its orbit label is exactly

```text
t_(m,n)=m-F*n.
```

One canonical full-integer orbit contains a constant-density all-one
rectangle with `Theta(F)` parallel lines of `Theta(F)` points.  Its reciprocal
kernel is literally

```text
q^3/[8*(R*m-n)*((R+1)*m'-n')],
```

the aligned completed-strip HSM chart.  Its diagonal cubic frequency is

```text
beta_u=((R+1)/R)*(u/F)^3,
```

so the quality-one transition

```text
A*u^3-B*F^3=Delta,
A,B~F^(9/16), 0<|Delta|<=F^(7/16),
```

survives tower integrality.  A finite replay even has both anchor coordinates
prime.  This refutes the hoped-for congruence shortcut; it is not a
counterexample to the dyadic moment.

## 4. Adversarial computation

The exact-residue numerical laboratory grouped equal products before phase
evaluation and scanned every integral dyadic start in both the actual
Selberg-truncated and stronger diagnostic ranges.

```text
largest actual normalized moment observed:       2.2207082;
largest actual aggregation factor observed:      2.1830216;
balanced critical-tower normalized moment:       <=0.301 (tested);
polynomial growth or finite counterexample:       NOT FOUND.
```

The largest constant came from the adjacent orbit and is explained by exact
factor-swapping aliases, already covered by the divisor bound.  The data
support the dyadic conjecture but do not upgrade it to a theorem.

## 5. Final status and stop decision

```text
unique hard-tower theorem:                         PROVED;
macroscopic interline and gradient separation:     PROVED;
subpolynomial-remainder hard branch of DRPLS:       PROVED;
extra canonical-tower congruence saving:            FALSE;
finite polynomial obstruction to DRPLS:             NOT FOUND;
single-tower signed product-action/HSM estimate:     OPEN;
full DRPLS:                                         OPEN;
sharp four-cycle bound:                             NOT PROVED;
best unconditional global exponent:                9/8 (UNCHANGED).
```

The present geometric route is exhausted: further progress requires a new
signed shifted-cube/product-energy theorem, or a global canonical-orbit
cancellation mechanism which bypasses the localized positive Fejer diagonal.

Detailed reports:

```text
results/ZETA23-QP-SELF-ORBIT-SMALL-SMALL-TOWER-RIGIDITY-2026-08-27.md
results/ZETA23-QP-CANONICAL-TOWER-HOSTILE-CUBIC-SURVIVAL-2026-08-27.md
results/ZETA23-QP-CANONICAL-SELF-ORBIT-DRPLS-ADVERSARIAL-LAB-2026-08-27.md
```
