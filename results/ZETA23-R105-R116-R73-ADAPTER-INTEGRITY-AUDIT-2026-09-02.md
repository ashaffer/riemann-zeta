# R105--R116--R73 adapter-integrity audit

**Date:** 2026-09-02  
**Status:** S0 completed; primitive-only go condition failed; no uniform
zero-free strip and no proof of RH

Machine-readable audit state:
[`context/zeta23_r105_r116_r73_adapter_audit_v1.json`](context/zeta23_r105_r116_r73_adapter_audit_v1.json).

## 0. Binary verdict

The literal adapter does **not** pass.

R116 proves a real local theorem on a balanced squarefree-semiprime packet:
its proper additive conductors are square-root smaller and its primitive
conductor has an exact ordinary-product dual.  It does not prove that the
complete R105 energy, and hence the complete fixed-window R73/R71 remainder,
equals that primitive packet plus fixed-power-safe errors.

The later R128 theorem repairs the missing conductor and modulus scopes
algebraically.  It does so by retaining every conductor, common-divisor
sector, fixed-ratio profile, conjugate orientation, and Vaughan component.
Their complete ordinary dual satisfies

\[
  O_{\rm full}=E_{Q_h,\mathrm{R71}}.                    \tag{0.1}
\]

Thus R128 supplies a faithful exact coordinate change, not a smaller
intermediate lemma.  An isolated primitive scalar has an exact
signed-coefficient representation, but no proved order-reflecting
upper-bound implication for the positive energy.  Its actual full-shell
indefiniteness is only numerically diagnosed.  Rephrasing “primitive” to
include the whole family makes the adapter true only tautologically.

The S0 disposition is therefore

```text
R116 balanced-semiprime theorem                 VALID IN SCOPE
R105 -> one R116 packet                         EXACT IN SCOPE
one R116 packet -> complete R73 remainder       FALSE
R128 all-class repair                           EXACT, BUT EQUALS ENDPOINT
primitive term + fixed-power-safe errors        NOT ESTABLISHED
S0 primitive-only go condition                  FAIL
uniform zero-free strip                         OPEN
RH                                              OPEN
```

The prescribed branch switch fires.  The honest first open edge is a
fixed-power estimate for the complete all-class `Q_h`-transformed energy,
or its exactly equal R128 ordinary dual.

## 1. The actual dependency chain

The name “R105 -> R116 -> R73” suppresses the two nodes which make the center
and Vaughan bookkeeping legitimate.  The exact chain is

```text
complete fixed-window R73/R71 field
  -- R102: apply Q_h before localization --> faithful center-free field
  -- R104: exact two-sided Vaughan completion --> tail + Euler defect
  -- R105: square and complete aliases --> full finite reciprocal energy
  -- R116: restrict to one balanced-semiprime packet --> local conductor split
  -- R120/R124: inspect primitive Mellin form --> positivity/order reflection unproved
  -- R128: restore every omitted class --> original complete Q_h energy.
```

The first three arrows are faithful under their recorded ordering and
fixed-window hypotheses.  The fourth arrow is a restriction, not an
equivalence.  The last arrow restores equivalence but removes the proposed
simplification.

### 1.1 R102: the center is eliminated legitimately

For fixed `h>0`, put

\[
 Q_h=(\tau_h-e^{h/2})^2.                              \tag{1.1}
\]

R102 proves that `Q_h` kills both rank-two center modes
(e^{R/2}) and (Re^{R/2}), makes both continuum marginals vanish, and has
nonzero multiplier at every nontrivial zeta zero.  On the real Fourier axis
it has the inverse

\[
 Q_h^{-1}=e^{-h}\sum_{j\ge0}(j+1)e^{-jh/2}\tau_h^j.   \tag{1.2}
\]

Consequently the center, tail--center terms, and center square are not being
silently discarded: `Q_h` is applied to the complete centered field, and
R102 proves that every nontrivial-zero carrier and the horizontal exponent
survive.  Formula (1.2) supplies the inverse on its recorded whole-line
`L^2` class; equivalently, the zero-side pole argument transfers the exponent
without reconstructing the rank-two center termwise.  This works only when
`Q_h` is applied on a
(2h)-enlarged frozen block **before** the output localizer.  Applying it
after localization creates the R102 boundary commutator at the unknown raw
scale.

This is an exponent adapter, not a termwise identity between the original
R73 block and one center-free packet on the same support.

### 1.2 R104 and R105: the full transformed energy is retained

R104 gives, at field level,

\[
 D_{V_Q}=T_{U,V,Q}+e_Q,                               \tag{1.3}
\]

where `e_Q` is the controlled Euler-evaluation defect.  It also proves
polylogarithmic bounds for the equal-frequency, dual-zero, punctured-axis,
and reducible faces.  The three unevaluated Vaughan heads are not individually
deleted; either (1.3) is used with their evaluated center and defect, or all
tail/head cross packets are restored coefficientwise.

R105 then squares the complete tail and obtains the exact finite form

\[
 E_T=\sum_{q_1,q_2}h(q_1)\overline{h(q_2)}
       \sum_{a,b\ne0}\widehat L_Q(-a/q_1,b/q_2).       \tag{1.4}
\]

It runs over every `q_1,q_2`, every
`g=(q_1,q_2)`, every supported ratio profile, and every off-axis box.  R116
starts only after one outer modulus and one balanced factor box have been
selected from (1.4).

## 2. Literal normalization correction

There is a repairable phase omission in R116 (10.2) and in the former
decision-path display.

R113's exact packet contains

\[
 h(c)c^{-it}\sum_k\nu_t(k)F_{c,t}(k).                 \tag{2.1}
\]

The R116 chirp transform contributes a factor (c).  Hence the ordinary
dual carries

\[
 h(c)c^{1-it}=A_{U,V}(c)c^{-it},                      \tag{2.2}
\]

not merely (h(c)c).  After recompletion on both coefficient variables,

\[
 A_{U,V}+\text{three Vaughan heads}
   =C,\qquad C(n)=-\mu(n)\log n,                      \tag{2.3}
\]

the `g=1` tail/head family has the form

\[
 \sum_{(c,n)=1} C(c)C(n)c^{-it}n^{-1-it}
          \Phi_\lambda(n/c),                         \tag{2.4}
\]

together with its conjugate orientation.  One may absorb (c^{-it}) into a
(t)-dependent coefficient for a norm estimate, but it cannot be omitted
from an exact identity.

R105 has already squared the field before reaching (2.1).  The correct
ordering requirement is therefore “before Cauchy--Schwarz or absolute values
in the outer/profile sum,” not “before squaring.”

## 3. The first load-bearing scope failure

R116's complete proper-conductor saving and primitive transform assume

\[
 c=pr,\qquad p,r\asymp\sqrt c,                        \tag{3.1}
\]

with (p,r) distinct primes and with the second-frequency support smaller
than both.  Its general squarefree estimate is only

\[
 \text{proper-conductor cost}
       \ll c^{1+\varepsilon}/P^-(c),                  \tag{3.2}
\]

where (P^-(c)) is the least prime factor.  This is not a fixed saving when
(P^-(c)) is small.

Two concrete legal tail moduli expose the missing scope.

1. If `c=p^2` and `p` exceeds both cutoffs, then

   \[
   A_{U,V}(p^2)=\mu(p)\Lambda(p)=-\log p,
   \qquad C(p^2)=0.                                   \tag{3.3}
   \]

   The nonsquarefree packet disappears only after exact head recompletion;
   it is not an R116 error which may be dropped.

2. Let `c=2pq` be of size `X`, with `p,q` of size `sqrt(X/2)`.  For any fixed
   near-square cutoff exponent below (1/2), this occurs in the tail.  The
   proper conductor (c/2) is near primitive, while (3.2) gives only
   (O(c^{1+o(1)})).  The balanced-semiprime square-root conclusion does not
   apply.

Common-divisor sectors `g>1` are also absent from the R116 `g=1` display.
None of these pieces can be bounded separately at the desired exponent:
R120 and R128 show that separated omitted-factor sectors retain zeta-zero
poles and strip-strength weighted-Mertens content.

## 4. Complete sector ledger

| Sector or operation | Exact audit disposition |
|---|---|
| Rank-two center and its energy cross terms | Killed exactly after `Q_h` acts on the complete field before localization. R102's zero-faithfulness transfers the exponent; the center is not reconstructed termwise or silently omitted. |
| Atomic diagonal | Subexponential by R102; safe. |
| Equal-frequency, `j=0`, axes, and reducible faces | Polylogarithmic in the fully recombined `Q_h` coordinate by R104; safe. |
| Full R105 off-axis tail energy | Exact finite identity; still contains all `q_1,q_2,g`, ratios, and shifts. |
| Balanced squarefree-semiprime `g=1` box | R116 applies; proper conductors are square-root smaller and the unit class is dualized. |
| General squarefree outer modulus | Near-primitive proper conductors are not fixed-power-saved by R116. |
| Nonsquarefree tail modulus | Must cancel through exact Vaughan heads; cannot be deleted before recompletion. |
| Tail--head, head--tail, head--head | Required on both coefficient variables to obtain `C=-mu log`; they are not independently negligible. |
| `g>1` and unequal-product sectors | Main members of the complete ordinary dual, not errors. |
| Fixed-ratio profiles | R116's vector-valued separation is exact/subpower, but every profile must be restored before positivity or an upper bound is invoked. |
| Conjugate orientation | Required to form a Hermitian scalar at nonzero Mellin parameter. |
| B-spline seams | Controlled by fixed seminorms/bounded-variation limits, provided signed translates are recombined first. |
| Output-localization collars | Safe only when `Q_h` precedes localization on enlarged frozen blocks. |
| Moving cutoff shells | Must be handled by frozen-block recompletion and the proved Euler defect; a globally moving cutoff cannot be differenced as though fixed. |
| Outer Möbius sign | Must remain until after the complete sum; early Cauchy leaves the primitive diagonal. |

The load-bearing rows are the general modulus, `g>1`, Vaughan cross, and
profile/orientation rows.  They are exactly the rows restored by R128.

## 5. What R128 repairs—and why that does not pass S0

For every positive integer `c`, R128 proves the complete chirp identity

\[
 \sum_{a\bmod c}F_c(a)V_c(a)
 =c\sum_z^*\gamma_c(z)
       \sum_{m,\nu}\widehat W(m,\nu)e_c(-m\nu z).      \tag{5.1}
\]

No squarefreeness, semiprime hypothesis, Weil bound, or Cauchy inequality is
used.  In conductor language, the nonunit classes exactly cancel the
Ramanujan proper-divisor correction of the unit class.  The conductor
remainder is zero.

But this identity must be applied to every `g`, ratio profile, orientation,
tail/head packet, and coefficient variable.  After coefficientwise
recompletion, R128 obtains

\[
\begin{aligned}
 O_{\rm full}
 &=\sum_{q_1,q_2}C(q_1)C(q_2)
     \sum_{m_1,m_2\ge1}L(q_1m_1,q_2m_2)\\
 &=\int\psi(R)\left|\sum_q C(q)\sum_m f_R(qm)\right|^2dR
 =E_{Q_h,\mathrm{R71}}.                              \tag{5.2}
\end{aligned}
\]

One frozen primitive/profile member of (5.2) has R120's exact
signed-coefficient Mellin diagonalization.  R124 proves a positive narrow
band and exhibits both full-shell signs only in a D-rated floating audit.
Thus no order-reflecting comparison from that isolated scalar to the
positive energy is proved; neither a one-sided nor an absolute bound for it
currently controls the complete energy.

So the two truthful statements are:

```text
primitive R116 packet + safe errors = complete energy       FALSE;
complete R128 ordinary dual          = complete energy       TRUE.
```

The second statement is an exact representation of the endpoint identified
by R180, not an independently easier target.

## 6. Fixed-window quantifier and exponent audit

Let `X=e^R`.  A sufficient fixed-window socket is

\[
 E^Q_I\le X^{1-\kappa+o(1)},\qquad 0<\kappa\le1       \tag{6.1}
\]

for one fixed `h,k` and every block of one fixed bounded-overlap regular
partition.  Uniform future-block bounds and (1.2) give a convergent inverse
series with ratio `e^{-(kappa/2-o(1))h}` in the licensed class; alternatively,
R102's nonvanishing zero multiplier gives the same exponent conclusion
directly.  Thus (6.1) preserves the detector exponent, and R180 yields

\[
 \Delta\le\frac{1-\kappa}{2},\qquad
 \frac\kappa2\le\Re\rho\le1-\frac\kappa2.             \tag{6.2}
\]

For the **complete** energy in the relevant range `0<kappa<=1`, the correct
normalization remains `eta=kappa/2`.

The top-cofactor shortcut has a different ledger.  At the most favorable
fixed-order cutoff

\[
 \theta_k=\frac12-\frac1{4(k+1)},                    \tag{6.3}
\]

the free Vaughan cofactor can be as large as

\[
 M\le X^{1-2\theta_k}=X^{a_k},
 \qquad a_k=\frac1{2(k+1)}.                           \tag{6.4}
\]

R123 can collapse it with a two-member truncated-Möbius bank, but its
uniform zero-carrier lower bound costs `M^{-1}` in amplitude.  If the
collapsed energy is bounded by `X^{1-kappa+o(1)}`, the recorded uniform
ledger gives

\[
 \Re\rho\le1-\frac\kappa2+a_k,qquad
 \eta_{\rm safe}=\frac\kappa2-a_k.                   \tag{6.5}
\]

Retaining the sharper `M^{-Re(rho)}` term gives

\[
 \Re\rho\le\frac{1-\kappa/2}{1-a_k},\qquad
 \eta_{\rm sharp}=\frac{\kappa/2-a_k}{1-a_k}.         \tag{6.6}
\]

Either version requires

\[
 \kappa>2a_k=\frac1{k+1}.                             \tag{6.7}
\]

This exponent computation is a conditional calibration, not a genuine
cofactor-collapsed reduction.  R125 proves that for adjacent prime cutoffs
`P-1,P` above the frozen cofactor range,

\[
 C_{P-1}T=C_PT,
 \qquad C_{P-1}-C_P=P^{-1/2}\tau_{-\log P}.           \tag{6.8}
\]

The two bank members are rank one on the collapsed tail.  Their sole
independent zero-faithful direction lives in the restored heads and is
exactly a shifted complete original field at scale `X/P`.  A tail-only
bound has no strip implication; bounds for both complete bank members give
(6.6) only by rescaling the original endpoint.  The fork is therefore
`EXACT SCALE REPLICATION / NOT A REDUCTION`.

The former decision path's unqualified `kappa=2 eta` relation omitted
this fixed-window cost for a cofactor-collapsed primitive target.  Taking
`k -> infinity` makes (6.4) subpower, but no varying-test converse is proved
for either sublinear single schedule: fixed total width `h=ell/k` with
`k log k=o(R)`, or fixed step `h` with `k^2=o(R)`.  R80's
proportional-order dyadic-bank converse concerns a different detector family.
Even if the missing converse were supplied, R125 shows that the adjacent
filter only scale-replicates the complete endpoint.  One must therefore
attack the complete fixed-`k` energy or introduce genuinely new arithmetic
structure before the rescaling.

## 7. Decision-tree correction

The most important mistake occurred at the attack-surface selection, before
any new estimate was attempted:

1. a theorem scoped to one balanced-semiprime packet was promoted to a
   global primitive reduction;
2. R120/R124's isolated-scalar/order-reflection warning and R128's all-class equality were not
   propagated into the selected route;
3. the growing-order `X^{o(1)}` cofactor ledger was mixed with the
   fixed-window converse; and
4. “before squaring” was requested even though R105 had already formed the
   quadratic energy.

The corrected first-open edge is

\[
 \boxed{\quad O_{\rm full}=E^Q_I
       \le X^{1-\kappa+o(1)}\quad}                    \tag{7.1}
\]

on one fixed window and every block of one licensed partition, with all
`g`-sectors, profiles, orientations, and Vaughan components retained before
Cauchy or absolute values.  By R180 this is strip-equivalent.  It should be
used as an endpoint and a hostile admission test for genuinely new
mechanisms, not advertised as the surviving primitive lemma.

A future mechanism earns reduction credit only if it produces a finite
identity or inequality for the **complete** family which is not merely
(5.2), retains the actual `C=-mu log` coefficients and completion source,
  and leaves one independently motivated fixed-power arithmetic debt.  The
R123/R125 fork receives no reduction credit: (6.5)--(6.8) show that it is a
conditional rescaling of the complete endpoint.

## 8. Trust and nonclaims

- This is an internal dependency, normalization, and quantifier audit.  It
  makes no literature-novelty claim.
- It imports the stated R102, R104, R105, R113, R116, R120, R123, R124,
  R128, and R180 results at their recorded trust levels.
- The accompanying checker validates claim-state and cross-file invariants;
  it does not prove the analytic inputs.
- S0 has been resolved negatively only for the primitive-only adapter.  It
  does not show that a uniform strip is false or that no different proof can
  work.
- RH remains open, and even a uniform strip would not imply RH without a new
  amplifier.
