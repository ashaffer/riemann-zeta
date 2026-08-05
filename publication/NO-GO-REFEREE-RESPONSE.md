# No-go atlas: adversarial referee response

Audit date: 2026-08-05.  Status: internal review response, not external peer
review.

Three independent reviews were requested: mathematical scope, literature and
priority, and artifact reproducibility.  This table records every material
objection and its disposition.  The canonical post-audit claims are in
[`../NO-GO-ATLAS.md`](../NO-GO-ATLAS.md); historical reports are not the claim
of record.

| Objection | Disposition | Resulting change or remaining debt |
|---|---|---|
| Uniform nonconvergence of an Euler symbol does not prove nonconvergence in a Calkin, strong, strict, or Fredholm-pair topology | Accepted | Removed the operator-topology no-go.  NG-02 now eliminates only inherited ordinary winding through a uniform invertible continuous-symbol limit.  Other operator topologies require a separately defined model. |
| `B^2` convergence does not imply that `B^2` has no possible index theory | Accepted | Replaced the universal statement by: `B^2` convergence alone supplies no canonical invertible continuous symbol or ordinary winding.  Added almost-periodic index prior art. |
| An arbitrary zero-density defect family need not have zero mean effect | Accepted | Restricted the density observation to finitely many uniformly localized defects; no arbitrary zero-density claim remains. |
| The symmetry census did not classify all eta, Krein, twisted, or equivariant refinements | Accepted | Restricted it to the displayed untwisted finite blocks and a precisely hypothesized antiunitary Fredholm example. |
| The remote quartet leaves the Euler-completed zeta class | Accepted as an essential scope boundary | NG-01 is explicitly an ambient compact-open/boundary-phase stress test, not a zeta-like arithmetic perturbation theorem. |
| The fixed-finite-place theorem relied on an unnamed “standard-sign” multiplier identity and did not exhibit the positive direction | Accepted; theorem core survives | The report now states the real test domain and both broad-bump constructions.  A standalone derivation and independent normalization audit remain amber debt. |
| The trace/polarization conclusion assumed an independent compact place torus not derived for the adelic quotient | Accepted | The place-torus action is now a headline hypothesis.  The eliminated class excludes non-equivariant, noncompact, and differently coupled models. |
| Formal-series character splitting is tautological and supertrace insufficiency does not forbid extra geometry | Accepted | These are supporting facts only.  The atlas claims that signed trace data do not determine a positive polarization in the stated class, not that extra geometry is impossible. |
| The bridge script checked words only through finite length | Accepted | Added the actual all-word proof: identical even and odd bridge representations cancel in supertrace for every word; the script is labeled a fixture. |
| The higher-differential theorem is nearly definitional and its continuum incidence operator has not been constructed as a closed Hilbert complex | Accepted | NG-06 is a bounded abstract supporting lemma.  The incidence report now marks dense domain, closure/closability, exact normalization, and form-domain identification as red debt. |
| The Möbius cylinder `100 or 011` is a superset, not the exact event that a collar substitution is available | Accepted; theorem strengthens safely | Corrected the wording.  Avoiding the larger cylinder still produces positive-density vertices with no allowed substitution edge. |
| The generalized hypertemplate density proof was asserted by analogy | Accepted | Added the explicit finite-prefix conditioning and deterministic multiples-tail argument in generalized notation. |
| The prime-edge Lean theorem proves optimal diagonal cost, while zeta-residual negativity was only floating-point evidence | Accepted | Demoted the zeta-specific no-go to red debt.  The exact local cost remains F-rated; a conventional or interval-certified residual witness is required. |
| Several Lean modules had no dedicated axiom audit or Apache release line | Accepted | Added `PrimeEdgePolarizationAudit.lean`; all formal artifacts named by the atlas now have focused audit files and Apache-2.0 release notices. |
| Individual “focused” Lean audits initially used 2.3--6.3 GB RSS and the worktree was not reproducible from current `HEAD` | Accepted | Replaced five broad imports and remeasured those audits at 1.5--2.4 GB.  Documentation requires serial focused commands and retains the clean-snapshot release blocker. |
| Much of the phase, Lyapunov, Hodge, and compactness machinery has substantial prior art | Accepted | These are labeled classical/supporting.  The only present theorem-level novelty candidates are the exact fixed-finite-place consequence and the scale-compatible summable Möbius-template formulation, both stated as priority-unconfirmed. |

## Surviving referee verdict

The audit found no fatal defect in the narrow fixed-finite-place theorem or in
the summable static Möbius-template theorem.  It did find fatal defects in
several broader summaries of the phase, finite trace, incidence, and local
Gram branches.  Those summaries have been narrowed or demoted.

This response is not a referee endorsement.  Before submission, the two
surviving analytic theorem candidates still require conventional standalone
proofs and review by mathematicians who were not involved in this repository.
