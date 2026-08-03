# Hodge high-sector closure

**Roadmap update (2026-08-02):** the high-tail estimate below remains a valid
abstract theorem, but the strengthened Hodge propagation route has been
numerically falsified in the low/full-domain sector by the witness recorded in
`PLAIN-LEGENDRE-HODGE-FALSIFIER.md`.  Consequently this theorem no longer
serves as one half of a prospective RH propagation proof.

Status: the high-incidence tail has a noncircular quantitative closure
theorem.  It reduces every fixed event to a finite low spectral sector once
the standard raw collar bounds and compact-resolvent input are supplied.  The
repository does not yet prove those constants uniformly over all events.

Let `Q_a` be the old Weil operator, `D_a` its degree, and

`S=Q_a+D_a I`, `d=q^2`, `K=I-sqrt(S/(S+dI))`.

On the old spectral tail `Q_a>=mu I`, the incidence spectrum satisfies
`S>=D_a+mu`.  Functional calculus gives

`||K P_high||^2`

` <= d^2/[4(D_a+mu)(D_a+mu+d)]`.

Suppose the raw collar block has floor `C>=c_0 I`, the ordinary old--collar
cross operator has norm at most `M_X`, and the return trace has squared norm
at most `M_Y^2`.  Completing the old variable and paying the Hodge loss costs
at most

`delta_high(mu) = M_X^2/mu`

`  + d^2 M_Y^2/[4(D_a+mu)(D_a+mu+d)]`.

Therefore `delta_high(mu)<=c_0` proves nonnegativity of the complete
Hodge-modified high block.  More precisely, the high block is bounded below
by `-delta_high(mu)||w||^2`; the low-sector theorem must be proved against the
residual collar form `C-delta_high(mu)I`.  This bookkeeping prevents the same
collar reserve from being spent twice.

The proof assumes no positivity of the desired Weil Schur complement.  Its
inputs are the unminimized old energy, raw collar floor, cross norm, and return
norm.  Lean also proves the sharp scalar multiplier bound, the explicit
cutoff criterion, and the exact high/low composition rule.

For the hardest available event, activation at `5`, the degree-121 Galerkin
section at `mu=3` gives the diagnostic budget

`0.24816 + 0.000709 < 0.36497`.

Thus that finite high tail closes with reserve about `0.1161`.  This number is
not a continuum certificate.

For each fixed event, bounded cross/return maps, a positive raw collar floor,
and compact resolvent make `delta_high(mu)` tend to zero as `mu` tends to
infinity, so only finitely many old modes remain.  Uniform closure over
arbitrarily large support additionally needs event-uniform versions of those
three analytic bounds and uniform spectral-tail control.  The present theorem
isolates those assumptions; it does not silently import them or RH.

Formal artifacts:

- `RHBridge/HodgeHighSector.lean`;
- `RHBridge/HodgeHighSectorAudit.lean`.

The axiom audit reports only standard foundational axioms.
