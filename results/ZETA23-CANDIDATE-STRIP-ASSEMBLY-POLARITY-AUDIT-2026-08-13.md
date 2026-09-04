# Candidate-centred strip assembly: polarity and same-packet audit

**Date:** 2026-08-13  
**Verdict:** `GP + OD2 + GA2` is **not** a conditional strip theorem.  OD2
has the opposite polarity from the QP input needed by the construction, and
the current GP and GA2 targets do not yet contain a joint state-selection and
budget theorem.  No zero-free region is moved.

## 1. Exact polarity of QP

For the actual prime-power log nodes put

```text
a_Y(t)=(cos(t*u_n))_n,
b_alpha(t)=integral phi_alpha(u)cos(tu)du,
L_Y=[0,Y^.01],
H_Y=[Y^.01,Y^(50/33)].
```

The cancellation cost and quotient extremal are

```text
C_Y=inf {||nu||+||mu||:
         supp nu subset L_Y, supp mu subset H_Y,
         integral a_Y d(nu+mu)=0,
         integral b_alpha dnu=1},                    (1.1)

E_Y=sup {|integral b_alpha dh|:
         integral a_Y dh=0, ||h||_TV<=1,
         supp h subset L_Y union H_Y}.               (1.2)
```

With `epsilon_H=sup_(H_Y)|b_alpha|`, the proved comparison is

```text
1/C_Y-epsilon_H <=E_Y<=1/C_Y+epsilon_H.             (1.3)
```

The sufficient **promotion** statement is an upper bound

```text
QP+(eta): C_Y<=Y^(kappa_promote-eta+o(1)),
kappa_promote=.0180303234, eta>0 fixed,              (1.4)
```

uniformly at the lower depth.  The exact positive form which plugs into the
proved compact factorization is stronger and cleaner:

```text
-r_Y*1 in conv{a_Y(t):t in H_Y},
r_Y>=Y^(-kappa_promote+eta+o(1)).                    (1.5)
```

Indeed, (1.5) gives an even positive high-frequency probability with central
weight `w_0=r_Y/(1+r_Y)`; after normalizing the fixed nonzero value
`b_alpha(0)`, it gives (1.4).  The compact positive-definite multiplication
and continuous spectral factorization theorem then turns this particular
positive solution into a legal compact lobe without another power loss.

Neither a candidate zero nor GP implies (1.4) or (1.5).  They are independent
statements about the actual prime-log curve.  Current theorems prove the
atomic-to-compact transfer, an exact central mass only at the much smaller
`Y^(-1+o(1))` scale, and positive realizability when the polynomial upper
aperture is removed.  They prove no lower bound of the form (1.5) inside the
legal aperture.  Finite diagnostics are compatible with square-root loss.

## 2. What OD2 would imply—and what it would not

Let

```text
kappa_bar=1974048259/100000000000=.01974048259,
h_min=8/33,
theta=797/5000.
```

The diagonal-scale OD2 theorem closes the post-`q` common-height fourth
moment for every fixed

```text
0<epsilon_OD2<epsilon_* ,

epsilon_*=(h_min-4*kappa_bar-theta)/4
         =3351407453/3300000000000
         =.001015578016060606....                    (2.1)
```

Weighted Holder then gives a post-`q` contribution

```text
sum_I |B_I(t)| <<Y^(1-kappa_bar-epsilon_OD2+o(1)).  (2.2)
```

If, in addition, every low/mid, boundary, crossing, companion, and discarded
term were assembled at at least the same exponent, (2.2) would produce a
dual antenna with

```text
C_Y>=Y^(kappa_bar+epsilon_OD2-o(1)),
E_Y<=Y^(-kappa_bar-epsilon_OD2+o(1)).                (2.3)
```

This is **KILL**, not PROMOTE.  Since
`kappa_bar>kappa_promote`, (2.3) is asymptotically incompatible with (1.4).
It rules out this optional prime-null construction.  It does not rule out a
zeta zero:

1. `C_Y` and `E_Y` are defined without assuming any zero;
2. an actual candidate does not force a cheap nuller;
3. GP only says what would happen if a suitable state were constructed; and
4. therefore OD2 supplies no statement of the form
   `candidate => forbidden event`.

OD2 alone is slightly weaker still: it closes CH4, not all auxiliary terms
needed for the full antenna (2.3).  That completion issue cannot repair the
polarity.

## 3. The exact conditional strip theorem

Fix

```text
alpha_0=49/100, beta_0=1/2+alpha_0=99/100,
d=33/50, Y=X^d.
```

Assume a finite-height base case `LOW(T_0)`: there is no zeta zero with
`Re rho>.99` and `|Im rho|<=T_0`.  Suppose there are fixed constants
`g>u>=0` and a deterministic selection rule such that every hypothetical
actual zero

```text
rho=1/2+alpha+i*gamma,
alpha in [alpha_0,1/2), |gamma|>T_0,                (3.1)
```

is assigned **one compact state** `q_rho` and one normalization `K_rho>0`
for which, on that same state,

```text
GP/divisor upper: R_other(rho;q_rho)
                    <=u*K_rho+o(K_rho),             (3.2)

GA2/Lambda lower: R_Lambda(rho;q_rho)
                    >=g*K_rho+o(K_rho).             (3.3)
```

The completed explicit formula at an actual selected zero gives exactly

```text
R_Lambda(rho;q_rho)=Q_ar(q_rho)+K_rho
                   =R_other(rho;q_rho).             (3.4)
```

Equations (3.2)--(3.4) contradict `g>u` for sufficiently large height.
Together with `LOW(T_0)` and conjugation, they prove

```text
zeta(s)!=0 for Re(s)>.99,
delta_ZF=1-.99=1/100.                               (3.5)
```

The arithmetic number in (2.1) is **not** the strip width.  It is a strict
`Y`-exponent slack in one dual-antenna estimate.  The `g-u` in (3.2)--(3.3)
is a fixed fractional reserve, a third different quantity.

## 4. What is missing to instantiate the theorem

The route needs all of the following, none of which may be placed on a
different optimizer.

1. **Budgeted GP, not bare GP.**  If GP first retains an `X`-exponent
   `sigma_GP` and QP then costs `Y^(-kappa_QP)`, one needs

   ```text
   sigma_GP>d*kappa_QP+sigma                       (4.1)
   ```

   for a fixed `sigma>0`.  The current bare GP target merely leaves some
   unspecified positive exponent.  Equivalently, its compact correction and
   the QP loss must be charged jointly.
2. **QP-PROMOTE.**  Use (1.5), or a signed theorem together with a new legal
   positivity/compact-state adapter.  OD2 cannot occupy this slot.
3. **Phase/state compatibility.**  GA2 selects the transverse direction
   `v_*=P_W R_Lambda e/||P_W R_Lambda e||` (or a top transverse
   eigenvector) from the actual Lambda coefficients.  GP must be uniform for
   that selected direction and phase, or GA2 must hold uniformly on the
   deterministic geometry-first GP output.  Existence of one GP optimizer
   and one GA2 optimizer separately is insufficient.
4. **Scalar GA2 reserve.**  The current GA2 theorem is a reduction, not
   (3.3).  It proves that the selected target deletes itself transversely and
   that, under isolation, every GA2 invariant is `o(K)`.  A positive GA2
   theorem must force a favorably oriented collateral deeper than
   `alpha*d-epsilon` (at the first slice, real part
   `>.8234-epsilon`) or a carrier-sized open remote term.
5. **Uniform remote and finite-height closure.**  Every `o(K)` is uniform in
   (3.1), and `LOW(T_0)` is discharged independently.

Items 1--3 are the missing same-packet compatibility lemma in its exact
form: a single selection map must preserve the GP sign, the QP central mass,
the GA2-selected coherent direction, compact support, and a positive joint
exponent margin.  Without it, even hypothetical proofs of the three
separate existential gates do not compose.

The rounded constants themselves are not the obstruction.  The GP base
ledger leaves

```text
S=.3234-.298008745=.025391255.
```

At the endpoint (2.1), the counterfactual bill

```text
d*(kappa_bar+epsilon_*)=13699/1000000=.013699
```

would leave `.011692255` of `X`-exponent.  This demonstrates numerical room
only; a dual lower bound cannot be charged as if it were a promotion cost.

## 5. Cache correction and reproduction

The compact proof-tree source now says explicitly that a dual antenna rules
out only the optional prime-null construction, never a candidate zero.  The
`QP -> FHC` edge was changed from `requires` to `alternative`, and the OD2
target is labeled a KILL result.

Run

```bash
python3 src/test_candidate_strip_assembly_gate.py
python3 results/verify_zeta23_candidate_strip_assembly_gate.py
```

The checker uses exact rational arithmetic for (2.1), (3.5), the GP ledger,
the polarity incompatibility, and the same-packet sign contradiction.  It
does not assert any open gate.
