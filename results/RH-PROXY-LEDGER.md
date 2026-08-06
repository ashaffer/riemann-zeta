# Canonical RH proxy ledger

Status: canonical logical map, 2026-08-06.  This document does not claim a
proof of the Riemann Hypothesis.

## 1. Purpose

The chronological [`REDUCTION-REGISTRY.md`](REDUCTION-REGISTRY.md) records
what was tried.  It intentionally mixes exact equivalences, sufficient
conditions, consequences of RH or its negation, proof mechanisms, numerical
diagnostics, and rejected mechanisms.  This ledger performs the complementary
job: it deduplicates those entries by their underlying RH carrier and records
the direction of every logical arrow.

There is an important semantic point.  All exact RH criteria are in one
logical equivalence class.  The proxy families below are kept separate only
because they expose different mathematical structures that might provide an
independent proof engine.  Calling two families different does **not** mean
that they are logically or probabilistically independent.

The older [`RH-EQUIVALENCE-ATLAS.md`](RH-EQUIVALENCE-ATLAS.md) remains a
historical mechanism-ranking snapshot.  This file is the source of truth for
current logical status.

## 2. Labels and evidence boundary

| Label | Meaning |
|---|---|
| **EQ** | Both implications with RH are established, subject only to the evidence basis named in the row. |
| **EQ-L** | Exact equivalence after the explicitly named consensus-literature inputs are imported. |
| **SUFF** | The premise implies RH; the converse is unproved, false, or would require extra structure. |
| **NEC** | A proved consequence of RH, with no proved converse. |
| **COND** | A conditional implication, commonly a theorem about what an off-line zero would force. |
| **MECH** | A proposed or partial proof mechanism for another proxy; it has no RH implication by itself. |
| **DIAG** | A finite, numerical, or structural diagnostic only. |
| **CLOSED** | The stated proof mechanism has been refuted, made circular, or shown too weak. |

Unbolded words such as “endpoint,” “stronger,” “identity,” and “mixed” are
prose modifiers, not additional status labels.

“Project analytic” below means that a conventional proof is written in this
repository.  It is not a claim of peer review.  Several such proofs use named
standard inputs, especially Guinand--Weil, Suzuki's screw-function identity,
Krein--Langer theory, and first-crossing results.  The chronological registry
and the linked reports state those dependencies.  Lean checks of abstract
order, kernel, or finite-dimensional lemmas do not by themselves establish
the zeta specialization.

## 3. Canonical exact-proxy families

Write

```text
Delta = sup_rho abs(Re(rho)-1/2),
```

where the supremum is over nontrivial zeta zeros with multiplicity ignored.
The following representatives are exact RH proxies at the stated
quantifiers.

| Family | Canonical representative | Status and basis | Related registry rows |
|---|---|---|---|
| **P0: divisor geometry** | `Delta=0`, equivalently every nontrivial zero is on the critical line | **EQ**, definition; Speiser and full real-zero formulations are classical equivalents | R8; full targets in R20, R23, R43 |
| **P1: global Weil form** | `Q_W(f)>=0` for every admissible compactly supported test function | **EQ-L**, classical Weil criterion with the repository's arithmetic normalization | R1, full-square reading of R4, R28, R30, R33--R40, R54 |
| **P2: all-window nondegeneracy** | Every localized completed-form-domain Weil form has trivial radical | **EQ-L**, using small-window positivity, spectral continuity, and the named first-crossing package | R2 and its compressed-kernel form R16 |
| **P3: support-uniform floor stability** | The localized floors admit one support-independent lower bound; equivalently their negative deterioration is subexponential | **EQ-L**, project analytic semiboundedness theorem plus screw/Nevanlinna inputs | R5 endpoint, R56 vanishing-shift clause, R62 |
| **P4: one fixed box discrepancy** | For one fixed `ell>0`, the von Mangoldt discrepancy `D_ell(R)`, its actual-prime version `P_ell(R)`, or any fixed-order centered balanced Vaughan sum of R68 is bounded, equivalently subexponential | **EQ-L**, project analytic consequence of Guinand--Weil, the unconditional prime-power tail, and the exact fixed-order Vaughan decomposition; each exact growth exponent is `Delta` | R65--R70 |
| **P5: compressed prime Gårding endpoint** | `(PG_0)` holds on every `PW_(U/2)`, for every `eta>0`, with a support-independent `C_eta` | **EQ-L**, project analytic reduction using P3 and the explicit formula | R64 endpoint |
| **P6: Herglotz/de Branges/Schur positivity** | Every shifted ratio `Theta_a` is Schur; equivalently the exact completed zeta kernel has the required Herglotz or Hermite--Biehler positivity | **EQ-L**, classical analytic-function theory with normalization audited here | R9, R21, abstract global part of R22; also the signature coordinates R28 and R30 |
| **P7: global entire/operator spectrum** | The nonzero spectrum of the coefficient-defined trace-class companion `K` lies in the positive real axis | **EQ**, project analytic determinant theorem `det(I+wK)=X(w)` | R63; full real-rootedness targets R18, R20, R23, R43 are related carriers |
| **P8: prime/Möbius cancellation** | `M(x)=O_epsilon(x^(1/2+epsilon))` for every `epsilon>0`, or a Riesz or prime-error criterion at its exact classical quantifiers | **EQ-L**, classical criteria | R7; endpoint hidden in R44 and R48--R51 |
| **P9: Li coefficients** | `lambda_n>=0` for every positive integer `n` | **EQ-L**, Li's criterion | R24 |
| **P10: arithmetic extremals** | Nicolas's primorial inequalities, or Robin's inequality at the exact classical threshold | **EQ-L**, classical criteria | R25 and R26 |
| **P11: Nyman closure** | The Nyman--Beurling--Baez-Duarte `L^2` closure criterion | **EQ-L**, classical criterion | R27 |

Thus a compact current equivalence spine is

```text
RH
  <=> P0
  <=> P1 <=> P2 <=> P3
  <=> P4 <=> P5
  <=> P6 <=> P7
  <=> P8 <=> P9 <=> P10 <=> P11.
```

This display records logical equivalence, not a chain of new proofs.  In
particular, P8--P11 are long-known criteria, while P3--P5 and the specific P7
companion are repository reductions whose novelty and proofs still require
specialist review.

## 4. What is genuinely stronger than RH

The following statements must not be promoted as exact proxies merely because
they would prove RH.

| Stronger or one-way target | Why it is not recorded as an exact equivalent |
|---|---|
| A scale-uniform adjacent-support contraction or complete collar propagation package (R3, R11--R15) | It is a sufficient proof certificate.  RH supplies positivity, but no converse construction of the proposed quantitative margins is known. |
| A particular compact-local limit of real-zero finite-window determinants to `xi` (R18, R19, part of R56) | Hurwitz gives the forward implication to RH.  RH does not presently construct this approximating family or its convergence. |
| A positive arithmetic Hodge, adelic colligation, or all-place trace realization (R10, arithmetic part of R22, R45, R46) | Its endpoint positivity is P1 or P6, but the requested arithmetic realization contains additional structure not known to follow from RH. |
| Hodge quotient observability or the strengthened Schur contraction (R41, R42) | The inequality is strictly stronger than Weil positivity and its intended implementation has a stable numerical counterexample. |
| Growing-cutoff shrinking-cylinder recurrence (R52) | It is an open sufficient recurrence theorem; no converse is known and the required uniform small-ball input may already carry RH-strength. |
| A canonical positive invariant metric for a global zeta operator (R53 or a strengthened R63) | Only after the global operator and its zeta spectral dictionary are constructed would the metric imply RH.  The metric also requires diagonalizability or semisimplicity and can therefore impose zero simplicity. |
| A positive logarithmic-energy reserve in R64 | The reserve is stronger than the endpoint P5 and forces an extra little-`o` zero-gap consequence. |
| Pointwise positivity of the R64 multiplier | It is stronger than compressed Paley--Wiener positivity and is false at the required scale. |

## 5. Complete R1--R70 map

The “family” column names the closest canonical endpoint, not a claim that the
row proves that endpoint.

### R1--R22

| ID | Family | Logical role | Canonical disposition |
|---|---|---|---|
| R1 | P1 | **EQ-L** | Canonical global Weil representative. |
| R2 | P2 | **EQ-L** | Exact after the named continuity and first-crossing inputs; not an independent positivity proof. |
| R3 | P2 | **SUFF / MECH** | Finite-product propagation certificate; uniform factors remain open. |
| R4 | P1 | **NEC** as written | The RH-conditional zero-frame square factorization is a coordinate expression; asserted for all tests it becomes P1. |
| R5 | P3, P4 | **COND**, with an **EQ-L** endpoint | An off-line zero forces exponential negative witnesses; subexponential floor deterioration is P3.  R65 later isolates an exact analytic scalar width exponent. |
| R6 | none | **COND**; metamathematical | Finite-witness independence lemma; the analytic-to-arithmetic bridge is absent. |
| R7 | P8 | endpoint **EQ-L**; other forms **CLOSED** or **SUFF** | The exact Mertens criterion is `M(x)=O_epsilon(x^(1/2+epsilon))` for every `epsilon>0`; qualitative Chowla is too weak; a restricted-weight estimate remains only sufficient. |
| R8 | P0 | endpoint **EQ**; spacing route **CLOSED**; occurrence injectivity stronger | Pointwise ordinate-location rigidity is P0; asymptotic spacing is insufficient; injectivity on occurrences also forces simplicity. |
| R9 | P6 | endpoint **EQ-L**; identity **MECH** | Exact zeta Herglotz positivity is P6; the unconditional kernel identity alone has no RH implication. |
| R10 | P1 | **SUFF** | Arithmetic Hodge/trace transfer proposal; its exact positive realization is additional structure. |
| R11 | P2 | **SUFF / MECH** | Full smooth collar package would propagate positivity; the decisive relative estimate is open. |
| R12 | P2 | **MECH / CLOSED** | Exact activation-defect identity, but its symbol has no positive `L^2` floor. |
| R13 | P2 | **SUFF / MECH** | Event-driven propagation; separate low-block positivity failed, coupled control remains open. |
| R14 | P2 | local identity; global **SUFF** | Exact block-Schur certificate at one event; all-event control would reach P1. |
| R15 | P2 | **MECH / DIAG** | Leakage result and finite ratios do not supply the required form-relative contraction. |
| R16 | P2 | **EQ-L** | Best compressed-operator representative of R2; zeta instantiation imports named domain inputs.  The remaining ordinary-`L^2` representative regularity concerns the proposed realization, not this completed-domain iff. |
| R17 | P2 | **COND** | First-crossing radical support saturation under negated RH; no contradiction follows. |
| R18 | P7 | **SUFF** | A specified real-zero determinant limit would prove RH; its existence is stronger and open. |
| R19 | P7 | **SUFF / MECH** | Concrete R18 approximation package; parity shortcut is closed. |
| R20 | P0 | **MECH / CLOSED** | Heat-flow degree repackages the Laguerre collision target and lacks global boundary control. |
| R21 | P6 | **EQ-L** | Shifted-Schur representative; the Loewner amplifier is closed. |
| R22 | P6 | abstract endpoint **EQ-L**; arithmetic realization **SUFF**; factorwise route **CLOSED** | Abstract passive realization is equivalent to Schur; an explicit adelic realization is stronger; factorwise construction failed. |

### R23--R44

| ID | Family | Logical role | Canonical disposition |
|---|---|---|---|
| R23 | P0 | **MECH / CLOSED** | Modular-orbit Gram engine for the heat-flow/Laguerre target failed; the first Laguerre inequality alone is not recorded as an iff. |
| R24 | P9 | **EQ-L**, engines **CLOSED** | Li positivity is exact; Hankel, moment, finite-difference, CND, and Toeplitz shortcuts added no independent sign law. |
| R25 | P10 | **EQ-L**, added order **CLOSED** | Nicolas is exact; the proposed transition order is stronger and conditionally false under Cramér. |
| R26 | P10 | **EQ-L**, concavity **MECH** | Robin is exact; CA-envelope concavity compresses candidates but gives no height bound. |
| R27 | P11 | **EQ-L** | Exact closure and Blaschke detector; no arithmetic mechanism forces the inner factor to be trivial. |
| R28 | P1, P6 | **EQ-L** | Zero negative-square index is Weil/Herglotz positivity in signature coordinates. |
| R29 | P1 | **CLOSED** | Local-conductor index assemblies are non-Fredholm or return ordinary zero counting. |
| R30 | P1, P6 | **EQ-L** | Positive Sonine reflection metric is the same signature invariant as R28. |
| R31 | P1 | **CLOSED** | Placewise Gram polarization cannot pay the required completed endpoint cost. |
| R32 | P1 | identity plus **CLOSED** lift | `mu*log=Lambda` cancels disconnected terms, but the direct positive lift is indefinite. |
| R33 | P1 | **MECH**, conditionally exact endpoint | The desired all-support Poincaré gap is restricted Weil positivity after the stated domain identifications. |
| R34 | P1 | **SUFF**, conditional iff | Boundary Weyl signature implies positivity; the converse requires the index-one and invertibility hypotheses. |
| R35 | P1 | **CLOSED** | Proposed monotone positive prime update is false. |
| R36 | P1 | **MECH** | Exact contraction/generator identity; the missing sharp deficit is P1. |
| R37 | P1 | **CLOSED** | Generic probabilistic gaps lose the sharp constant; an exact gap would restate P1. |
| R38 | P1 | exact rewrite plus failed **MECH** | Unrestricted dual-frame domination is Douglas/Weil positivity; fixed-rank angle engines fail. |
| R39 | P1 | unrestricted route **CLOSED** as circular | Unrestricted completion is P1, while the named restricted channels were pruned. |
| R40 | P1 | full endpoint **EQ-L**; proper subclasses **SUFF** and mostly **CLOSED** | Full cycle capacity is the Weil Schur condition; proper-cycle subclasses are stronger and mostly pruned. |
| R41 | P1 | stronger **SUFF**, then **CLOSED** | Hodge observability is strictly stronger than P1 and failed on the intended numerical model. |
| R42 | P1 | **CLOSED** | High-tail lemma is valid, but the required strengthened low-sector contraction has a stable counterexample. |
| R43 | P0, P7 | full endpoint **EQ**; finite cones **DIAG**; product model **CLOSED** | Full centered-`xi` real-rootedness is P0; finite cones are diagnostics; the independent-spin representation is false. |
| R44 | P8 | generic route **CLOSED**; residual **MECH** | Generic pretentious inverse theorem is false; a Möbius-specific endpoint remains only a possible route. |

### R45--R68

| ID | Family | Logical role | Canonical disposition |
|---|---|---|---|
| R45 | P1 | **SUFF / CLOSED** | Finite cyclotomic trace architectures failed; a genuinely infinite all-place construction remains open. |
| R46 | P1 | **CLOSED / MECH** | Bare ultraproduct transfer is insufficient; every useful enrichment still lacks the sign-controlled bridge. |
| R47 | P0 | fixed-partner route **CLOSED**; diagonal fork open | Fixed-partner exceptional-zero replication failed; no exact proxy was produced. |
| R48 | P8 | stability route **CLOSED**; endpoint tautological | Stability is too weak; the exact root-product control is Mertens in factorized form. |
| R49 | P8 | **MECH** | Matching identity is exact, but after saturation its deficiency is exactly `abs(M(N))`. |
| R50 | P0 | **CLOSED** | Fixed-cutoff conditioned Bagchi recurrence has zero-free limiting support. |
| R51 | P8 | **MECH** | Blocker-forest decomposition leaves the Mertens endpoint unchanged. |
| R52 | P0 | **SUFF** | Growing-cutoff recurrence remains open; no converse is known. |
| R53 | P7 | conditionally **SUFF** after a global spectral dictionary; finite class **CLOSED** | The metric would force P0 and diagonalizability only after a canonical global zeta operator is supplied; the finite equivariant trace architecture failed. |
| R54 | P1 | **EQ-L** endpoint; engine **CLOSED** | Vanishing localized Morse index is P1 in index coordinates; natural Euler loops did not compute it. |
| R55 | P1 | standard route **CLOSED**; transport fork conditional | Strict Mourre positivity is circular on the bad subspace; standard dilation mechanism failed. |
| R56 | P3, P7 | vanishing-shift endpoint **EQ-L**; characteristic limit **SUFF**; unitary shortcut **CLOSED** | Cofinal shifts tending to zero are P3; characteristic convergence is stronger; exact unitary shortcut failed. |
| R57 | P7 | **DIAG** | Fixed-shift finite divisor fit fails on present windows but does not refute a cofinal limit. |
| R58 | P7 | **DIAG** | Exact phase-count formula is a topology gate, not an RH proxy. |
| R59 | P7 | **DIAG**; generic route **CLOSED** | Exact coherence reduction; generic de Branges structure cannot force the desired compact phase growth. |
| R60 | P7 | normalization theorem; shortcut **CLOSED** | Clark normalization shows that fixed shift selects mixed spectrum; no RH equivalence results. |
| R61 | P7 | **NEC** | Under RH, generalized strong resolvent and fixed-core measure convergence hold; there is no converse. |
| R62 | P3 | **EQ-L** | Canonical support-uniform semiboundedness/floor dichotomy. |
| R63 | P7 | **EQ** | Canonical trace-class companion spectrum criterion; finite sections do not inherit it. |
| R64 | P5 | **EQ-L** at endpoint | Positive reserve is stronger; pointwise endpoint is false; compressed endpoint remains open. |
| R65 | P4 | **EQ-L** | Canonical one-fixed-box width spectrometer; the required prime bound remains open. |
| R66 | P4 | actual-prime endpoint **EQ-L**; naive transfer routes **CLOSED** | Quantitative PNT makes the centered prime-power remainder summable on geometric progressions.  The surviving centered actual-prime Birkhoff-sum or completed mixed-prime reflection law remains open. |
| R67 | P4 | naive Selberg transfer **CLOSED**; completed arithmetic gate **OPEN** | The exact causal Riccati--Volterra and reflection factorizations expose an indefinite mixed term and pole-scale forcing; generic positivity, fixed finite-codimension or bounded-rank completion, Möbius inversion, and ordinary functional-equation symmetry do not control it. |
| R68 | P4 | fixed-order centered Type-II endpoint **EQ-L**; tested ambient metric/reflection classes **CLOSED** | The exact actual-prime primitive and fixed-order aggregate Vaughan sum have growth exponent `Delta`; fixed-order smoothing confines the bilinear variables to `x^(1/2+/-epsilon)` for any fixed positive `epsilon`.  Direct reflection is two-sided unbounded, rough Euler updates expand, scalar Doob normalization inserts `1/zeta`, and the scalar filtered isometry has centered-ramp dual norm at least `exp(R/2)R^(3/2)`.  The balanced coefficient series retains every zero pole.  Fixed finite cofactor blocks and the separate Euler bulk/boundary pieces raise a multiplicity-`m` zero pole to order `m+1` and remain unbounded after ordinary centerings; only their full sum restores the simple pole.  Uniform smoothing constants also give a moving-order `x^(1/2+o(1))` arithmetic localization, without a proved RH converse.  Aggregate moving-cutoff near-square Type-II cancellation remains open. |
| R69 | P4 | tested ambient-norm/reflection classes **CLOSED**; aggregate polylog gate **EQ-L** | The logarithmic kernel has Volterra--Hankel singular values proportional to its collar width, so fixed-rank centerings and norm-only estimates do not contract.  Equal-cutoff reflection reinforces a coherent semiprime block of size `x^theta/log x`; only the joint moving `B-Z` jump cancels automatically.  A uniform polylogarithmic bound for the full fixed-order centered aggregate is P4/RH-equivalent and remains open; `sqrt(log x)` is only the fully decorrelated heuristic scale.  An `exp(O_ell(k log k))` Euler bound now gives an unconditional growing-order `x^(1/2+o(1))` arithmetic localization, but no varying-test converse, so that moving proxy is not known RH-equivalent. |
| R70 | P4 | exact cutoff conservation **MECH**; tested algebraic sign/contraction engines **CLOSED** | The outer-product cutoff table, weighted logarithmic derivative, flat cutoff transport, full singular reconstruction, and divisor-collar involution all couple the R68 pieces exactly.  After all modes and cofactors are restored they reduce to Vaughan's identity and `-zeta'/zeta`.  The exterior-square defect of entrywise ramp evaluation changes sign, including after prime-power deletion, so it supplies neither positivity nor coercivity.  The remaining non-fiberwise arithmetic estimate is still the P4 aggregate gate, not a new proxy. |

## 6. Research-allocation rule

An exact reformulation is a **detector**, not yet a proof engine.  A branch is
promoted only if it supplies a law not already equivalent by definition to
the sign, zero-exclusion, or cancellation being sought.  Before opening a new
branch, record:

1. its canonical family above;
2. its exact quantifiers and arrow direction;
3. the new source of sign, order, compactness, integrality, or cancellation;
4. a countermodel separating that source from the desired conclusion; and
5. whether the proposed estimate is stronger than RH.

On that standard, the cleanest present scalar target is P4/R66--R70: bound one
fixed-log-width triangular discrepancy over actual primes, prove its
centered actual-prime geometric Birkhoff sums uniformly bounded, or prove the
equivalent aggregate centered Type-II estimate in R68.  P5/R64 is the exact
compressed quadratic target when polarization is essential.  P3/R62 explains
why a common negative shift cannot evade RH, and P7/R63 is a compact global
spectral restatement but currently has no arithmetic positivity mechanism.
None of these statements supplies the still-missing bound or positivity law.

## 7. Maintenance rule

Every new registry row must either map to P0--P11, introduce a genuinely new
carrier with both arrows audited, or be labelled as a mechanism, diagnostic,
conditional theorem, or no-go result.  If a later proof changes an arrow, edit
this ledger and the originating registry row in the same change.
