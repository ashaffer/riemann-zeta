# Uniform-strip sprint synthesis: what moved and what did not

Status: consolidated theorem ledger, 2026-08-12.  The target calibration is
the fixed strip

```text
Re rho < 0.99,
```

with

```text
alpha=0.49,       d=0.66,       L=log gamma.
```

No uniform zero-free strip, improvement to a known zero-free region, or
instance of RH is proved here.

## 1. Binary verdict

The sprint produced three substantive exact advances.

1. The completed logarithmic derivative gives a reflected-pair Carleson
   budget which couples background density and endpoint excess.  The
   strongest lower-bound obstruction presently certified by the explicit
   growing Pick screen does not exhaust the resulting conditional surcharge.
   This does not construct an upper-loss transfer for that screen.
2. Every target-local one-cell fan of scaled depth
   `Lambda_L=o(L/log L)` has a coherent compact realization with only
   `o(L)` carrier loss, irrespective of its row count and spacing.  Only
   cusp-reaching deep fans remain geometrically relevant.
3. Positive Poisson/log-derivative auxiliaries have the wrong polarity for
   the missing arithmetic reserve.  Canceling their main term necessarily
   destroys zero-side positivity.

These advances do **not** compose to a strip.  Two logically independent
gates remain:

```text
global deep-fan Pick/compact transfer;
signed target-conditioned actual-prime lower edge.
```

The second gate is not supplied by the first.

## 2. The unconditional zero-count improvement

At

```text
sigma=1+L^(-1/2)
```

the completed logarithmic derivative gives

```text
sum_rho (sigma-beta)/[(sigma-beta)^2+(t-gamma)^2]
 =L/2+O(sqrt L).                                  (2.1)
```

Consequently, in a fixed microscopic window `|gamma-t|<=C/L`,

```text
#{rho: beta>=sigma_0}
 <=[(1-sigma_0)/2+o(1)]L.                         (2.2)
```

At the first-strip edge this is `0.005L+o(L)`.  Integrating (2.1) across an
ordinate interval gives the stronger reflected-pair statement

```text
N_pair(I)<=[|I|/(4*pi)+O(sqrt |I|)]L+o(L)          (2.3)
```

in the long-interval regime, together with the exact padded fixed-width
bound in the depth-count report.  This couples the Riemann--von Mangoldt
background and local endpoint discrepancy: they cannot be charged as two
independent positive populations.

The quantifiers in (2.3) are sequential: first let the central height tend
to infinity for each fixed `|I|`, and then let `|I|` tend to infinity.  Its
`O(sqrt |I|)L` boundary allowance is not `o(L)` for one fixed short
interval, so (2.3) is not a uniform local finite-section density margin.

This is an upper-count theorem, not a spacing theorem and not a lower edge.

## 3. The conditional Green--Poisson carrier surplus

Assume temporarily that each occupied phase cell is reduced to one actual
reflected-pair representative and that the singular target cell is handled
with subexponential loss.  At the fixed line `Re s=1.4`, an exact
Green--Poisson dual calculation with `lambda=0.304` gives

```text
one-representative Pick bill <=0.2980087448 L,
raw selected carrier          >=0.3234 L,
conditional surplus          >=0.0253912552 L.     (3.1)
```

The one-dimensional residual integral is

```text
1.3889415384...<1.39.
```

The potential calculation is exact modulo the stated representative and
target-cell hypotheses; no separate Bellotti endpoint-discrepancy payment
is needed.  It remains an unrestricted causal potential ledger, not a
compact realization theorem.

The first fully quantitative growing adversary is an interlaced binomial
half-disk screen.  Without actual counts it can force exponent
`0.0189350155...`.  The integrated reflected-pair cap restricts an
actual realization of that family (and, more weakly, every member not
excluded by this Poisson count) to

```text
c<=0.00465416454...,
loss >=F(c)L,       F(c)<=0.01118512309....        (3.2)
```

Thus the binomial theorem does not certify enough forced loss to exhaust
(3.1).  Equation (3.2) bounds the **lower bound furnished by that
argument**; it is not an upper bound on the true optimum loss and does not
prove that the adversarial list is affordable.

## 4. The conformal cusp and the shallow-fan theorem

The all-jet cell has the exact conformal parametrization

```text
h(x)=-lambda_0+(2/d)log cos(x/2)-i*x/d,
w(h)=2 exp[d(h+lambda_0)/2]-1,
w(h(x))=exp(-i*x).                                 (4.1)
```

The ideal full contour is rigid for bounded subcritical-type functions.
The physical half-plane, however, removes an exponentially small cusp at
`w=-1`.  The sharp elementary escape is the half-delay

```text
U(z)=exp(-dLz/2),                                  (4.2)
```

which signs a whole phase cell at cost

```text
alpha*d*L/2=0.1617L.                               (4.3)
```

More usefully, let a target-local fan have rows

```text
beta_j=alpha-lambda_j/L,
delta_j=c_j/L,
0<=lambda_j<=Lambda_L,
|c_j|<=C.
```

If

```text
(Lambda_L+1)log L=o(L),                            (4.4)
```

then a degree `O(Lambda_L+1)` virtual-translation filter, applied to fixed
Gevrey endpoint packets, signs every row and retains carrier

```text
exp[alpha*d*L-O((Lambda_L+1)log L)]
 =exp[alpha*d*L-o(L)].                             (4.5)
```

The bound is independent of row cardinality and spacing.  In particular,
the natural `Theta(L)` root-of-unity sampling of (4.1) reaches only
`Lambda_L=O(log L)` and costs `O((log L)^2)=o(L)`.

Therefore a fixed-power one-cell obstruction must, along some subsequence,
reach scaled depth

```text
Lambda_L=Omega(L/log L)                            (4.6)
```

and also satisfy the cumulative Poisson budget.  Remote-cell composition
and such deep fans remain open.

## 5. Why the Poisson surplus cannot buy the arithmetic sign

On the exact line used in Section 3, a selected reflected pair of depth
`alpha<=1/2` has Poisson charge at most

```text
1/(0.9-alpha)+1/(0.9+alpha)<=45/14.                (5.1)
```

The total completed Poisson mass is `L/2+O(1)`.  Hence the mass of all
other zeros divided by the selected mass is at least

```text
(7/45)L-O(1).                                      (5.2)
```

On the selected-positive quotient, the required arithmetic statement is
the exact reserve identity

```text
Q_ar(q_rho)=-K_rho+R_rho,
R_rho=Q_ar(q_rho)+K_rho.                           (5.3)
```

Adding a positive Poisson auxiliary with coefficient `lambda` rewrites the
reserve as

```text
R_rho
 =sum_other [h_q+lambda A]-lambda A_rest.          (5.4)
```

The last term has the adverse sign.  In any universal rowwise-positive
repair, a duplicate or arbitrarily close selected row forces
`lambda A_0` to be carrier-sized, after which (5.2) produces an
`Omega(LK_rho)` wrong-sign bill.  Homogeneous rescaling within this same
auxiliary scheme cannot remove the ratio; this is not a no-go theorem for
an independent signed correlation or a different coupled state.

If a signed resolvent combination cancels the `L/2` main term, its vertical
integral is zero.  Every nonzero target-positive real kernel then changes
sign.  Functional-equation pairing preserves this zero mass.

Thus the following routes are closed:

```text
fixed-line positive Poisson repair;
positive mixtures of such lines;
main-term-cancelled but termwise-positive resolvent repair.
```

What remains is a signed, target-conditioned correlation involving the
actual von Mangoldt coefficients.  This is the arithmetic reserve itself,
not a consequence of the geometric surplus.

## 6. The independent Mertens formulation

Let

```text
M(X)=sum_(n<=X) mu(n),
J(X,H)=sum_(n<=X-H)|M(n+H)-M(n)|^2.
```

The exact window ANOVA identity gives

```text
J(X,H)>=[H^2/(X-H)](|M(X)|-H)_+^2.                (6.1)
```

Therefore

```text
J(X,X^theta)<<X H^(2-eta)                          (6.2)
```

implies a zero-free strip of width

```text
delta=min(1-theta,theta*eta/2).                    (6.3)
```

For the `0.99` target, the boundary-safe exact calibration is

```text
theta=49/50,       eta=1/49.                       (6.4)
```

All Fourier frequencies outside

```text
||xi||<X^0.01/H                                   (6.5)
```

already satisfy the needed power bound by the Dirichlet-kernel estimate.
The entire missing power lies in this principal band, and its rank-one
zero mode is the weighted Mertens mean itself.  Centered Type-II dispersion
controls only the orthogonal variance.  Known logarithmic almost-all
short-interval estimates do not give the fixed `H^(-1/49)` saving.

This is a clean independent strip-equivalent target, not a proved bound.

## 7. Research decision

The completed-carrier route is now geometrically narrower but still has two
independent unresolved theorems:

1. compress cusp-reaching deep fans and compose remote cells below the
   `0.025391255L` surcharge;
2. prove the signed candidate-relative von Mangoldt reserve (5.3).

The first theorem cannot supply the second by positive Poisson coupling.
Accordingly, the shortest standalone implication chain is now the
principal-band Mertens estimate (6.2)--(6.5), or an equivalent signed
all-divisor recombination.  This is an equivalent-strength reformulation,
not evidence that the estimate is easier than the signed candidate-relative
reserve.  The carrier/Pick work remains valuable as a separate candidate-
local geometry program, especially for proving or falsifying the deep-fan
compressor.

The next claimed strip proof should be rejected immediately unless it
contains one of these two genuinely new arithmetic inputs:

```text
a fixed-power principal-band/Mertens estimate;
a signed target-conditioned actual-prime reserve.
```

Density, functional equation, positive Poisson mass, finite SDP evidence,
or subexponential carrier retention alone do not suffice.

## 8. Verification and dependencies

Reproducibility modules:

```text
src/green_poisson_pick_ledger.py
src/conformal_pick_cusp.py
```

Primary theorem cards:

- `ZETA23-DEPTH-SENSITIVE-MICROSCOPIC-ZERO-COUNT-2026-08-12.md`;
- `ZETA23-GREEN-POISSON-DUAL-PICK-LEDGER-2026-08-12.md`;
- `ZETA23-GLOBAL-HALFDISK-PICK-BINOMIAL-AND-POISSON-AUDIT-2026-08-12.md`;
- `ZETA23-CONFORMAL-CUSP-AND-SHALLOW-FAN-PRUNING-2026-08-12.md`;
- `ZETA23-CANDIDATE-RELATIVE-FRACTIONAL-ARITHMETIC-EDGE-AUDIT-2026-08-12.md`;
- `ZETA23-POISSON-ARITHMETIC-RESERVE-POLARITY-GATE-2026-08-12.md`;
- `ZETA23-MERTENS-TYPEII-PRINCIPAL-BAND-GATE-2026-08-12.md`;
- `ZETA23-UNIFORM-STRIP-SPRINT-HOSTILE-REFEREE-2026-08-12.md`.

All numerical constants quoted above are reproducible by elementary
one-variable calculations.  They are not evidence for an asymptotic zero
region beyond the exact conditional statements displayed here.
