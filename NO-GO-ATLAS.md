# Atlas of exact obstructions

> **Frontier notice (2026-09-03):** the obstruction cards retain their scoped
> force, but this atlas is not the latest route ranking.  Run
> `python3 src/zeta23_correction_context.py resume` and see
> [`results/ZETA23-EXTERIOR-FACTORIZATION-AND-BACKWARD-STRIP-AUDIT-2026-09-03.md`](results/ZETA23-EXTERIOR-FACTORIZATION-AND-BACKWARD-STRIP-AUDIT-2026-09-03.md).
> The 2026-09-02 decision path remains a verified pre-R181 snapshot.

Status: canonical scope and proof-debt index, 2026-08-07.

This atlas records what the project's negative results actually prove.  It is
not a list of failed conversations and it is not a no-go theorem for the
Riemann Hypothesis.  Each card identifies a precise candidate class, the
obstruction, the evidence level, and the surviving escape hatch.  Full proofs
remain in the linked reports and Lean modules.

The governing release rules are in
[`publication/PROOF-STANDARD.md`](publication/PROOF-STANDARD.md).  In this
file, “eliminated” always means “eliminated under the hypotheses printed in
the same card.”

The independent internal objections and their dispositions are recorded in
[`publication/NO-GO-REFEREE-RESPONSE.md`](publication/NO-GO-REFEREE-RESPONSE.md).
For a continuous mathematical narrative grouping the cards by their common
mechanisms, read
[`publication/NO-GO-THEOREM-GUIDE.md`](publication/NO-GO-THEOREM-GUIDE.md).

## 1. Evidence key

- **F:** Lean checks the named statement; the linked audit prints its axioms.
- **A:** a conventional analytic or algebraic proof is written in the linked
  report, but the full statement is not checked by Lean.
- **L:** the proof uses a named theorem from the literature.
- **C:** an exact or interval computer certificate proves a finite statement.
- **D:** a diagnostic computation or scout, not a theorem at the advertised
  infinite level.

The evidence code is attached to each component, not to a surrounding story.
In particular, an F-rated toy countermodel does not turn its zeta-specific
interpretation into an F-rated theorem.

## 2. Obstruction matrix

| ID | Exact candidate class eliminated or constrained | Decisive mechanism | Evidence | Smallest visible survivor |
|---|---|---|---|---|
| NG-01 | Integer detectors continuous for compact-open normalized divisor perturbations, or using only the real critical-line phase | A remote normalized off-line quartet tends to one on every fixed compact and is positive on the real line | A; finite quartet algebra F | A genuinely global weighted topology tied to arithmetic growth |
| NG-02 | Continuous-symbol winding obtained as a uniform limit of the two canonical finite-prime shifted Euler-loop models | Finite loops are null-homotopic; the literal product is not `B^2` bounded, while the normalized phase is `B^2` but not uniformly Cauchy in the relevant strip | finite contraction F; limit claims A | A completion-native relative index with independently specified operator topology and all-place summability |
| NG-03 | A fixed finite set of finite places plus the archimedean place, required to remain positive on arbitrarily large supports | Its pole-annihilated Fourier multiplier is negative at zero and positive at high frequency | A | Support-coupled activation of unboundedly many places |
| NG-04 | Improving an independently assigned prime-edge Gram factorization by splitting one cross coefficient among more positive channels | Positivity forces endpoint diagonal cost at least twice the cross mass; the difference square is sharp | F | Essential cross-coupling between distinct places and infinity |
| NG-05 | Treating a nonzero pure mixed Hilbert pairing itself as a universally nonnegative quadratic form | Flipping one channel reverses its sign | F | Additional diagonal terms or a separately constructed positive polarization |
| NG-06 | Repairing degree-zero Hodge coercivity solely by changing a later differential while the first differential is fixed | Degree-zero energy is exactly the norm square of the first differential | F | Change the first map, degree, domain, or pairing |
| NG-07 | Deriving the last Schur-complement sign only from convolution, evenness, analyticity, separate block positivity, and the weak old equation | An explicit analytic rank-one kernel satisfies those properties while its exterior response exceeds the old gap | F for the countermodel and pivot algebra | A zeta-specific prime--archimedean cancellation estimate |
| NG-08 | Inferring a positive spectral metric from functional-equation duality, or fitting that metric after the spectrum is known | An off-line pair preserves alternating duality but admits no strictly positive adjoint metric; the general metric equation already encodes critical-line spectrum | minimal rational block F; general finite characterization A | A canonical positive metric constructed independently of zero locations |
| NG-09 | Fixed countable, scale-compatible, summable dictionaries of finite sign-reversing prime-set substitutions on dyadic squarefree collars | A finite-prefix conditioning and summable tail bound leave positive density untouched | A | An `N`-adaptive, unbounded-incidence mechanism with global matching state |
| NG-10 | Fixed-prime-conditioned Bagchi tails used to approximate a continued zeta remainder containing an off-line zero | The limiting random Euler tail is zero-free, so a Rouché approximation event is empty | A+L | A growing-cutoff, zeta-specific continuation theorem outside the fixed-block limit |
| NG-11 | A strict regular commutator on a localized pure-point spectral subspace treated as an independent test; pure finite-section commutators; geometric dilation | Eigenstate commutator expectations and finite commutator traces vanish; geometric dilation has an unbounded negative simultaneous-prime symbol; the analogous boundary-compatible transport result is conditional on a localized pseudodifferential packet lemma | finite algebra F; dilation analysis A; transport step Amber; prime-5 scout D | Another local generator, completion of the transport asymptotic, a genuinely nonlocal mixed inequality, or a singular support-moving generator with the exact completed boundary defect retained |
| NG-12 | Inferring canonical phase-labelled extension families from equivalence of coercively shifted energy norms | The energy-dual adjoint repair is valid, but an exact Dirichlet family has a nonconstant shift quotient of its boundary phasors | Riesz core F; Dirichlet counterexample A; completed-Weil scan D | A zeta-specific adjoint intertwiner, or an explicitly tuned shift/phase sequence with a proved graph limit |
| NG-13 | Inferring support-uniform compact spectral crowding from exponential type, inner-function symmetry, and a fixed-support high-energy Weyl law whose onset/remainder may depend on support | An explicit type-`a` Hermite--Biehler family moves every added Blaschke zero beyond `a^2`, retaining the full far-tail density while its fixed-compact phase tends to the single Cayley factor | phase-floor/coherence scalar lemmas F; Hermite--Biehler countermodel and kernel normalization A; completed-Weil winding D | A zeta-specific characteristic or boundary-scattering limit; NG-15 shows that fixed-core strong-resolvent convergence is automatic under RH and moving defect vectors escape |
| NG-14 | Using a canonical fixed-negative-shift exhaustion to converge directly to the unshifted pure zeta-zero operator, or treating moving finite Clark vectors as fixed strong-resolvent probes | Even under RH the shift adds `c dx/(2*pi)` to the global Fourier measure, hence an absolutely continuous spectral component; strong resolvent controls the Clark measures only after the embedded reference vectors are proved to converge | shift-mass scalar lemmas F; Plancherel/zero-frame target and Clark normalization A; current Galerkin probes D | Target the honest mixed-spectrum shifted operator or a stronger boundary topology; NG-15 proves natural moving-vector compatibility fails, while admissible shifts tending to zero already encode all-window positivity |
| NG-15 | Using normalized finite reference-defect Clark measures or a phase-tuned strong-resolvent limit to select the zeta divisor | Translation invariance makes the reference Riesz norms grow exponentially and their unit vectors converge weakly to zero; once RH supplies the positive global space, the compact smooth core is a generator core, so every phase choice has the same generalized strong-resolvent limit | Riesz projection scalars F; translation escape, group-core, and generalized-resolvent theorem A; norm-growth scout D | A stronger boundary topology: locally uniform characteristic/Weyl convergence, norm resolvent or multiplicity-controlled projections, or a renormalized scattering limit of the unnormalized escaping kernels |
| NG-16 | Treating one fixed support-independent negative shift, or a uniform completed prime--archimedean `L2` remainder, as a weaker preliminary target than RH | `W+c delta_0` positive definite makes `g-(c/2)|t|` a global screw function; its Herglotz transform is `i(xi'/xi)(1/2-iz)+ic/2`, whose upper-half-plane holomorphy excludes off-line zeros | abstract floor/common-shift dichotomy F; Suzuki transform, Krein--Langer correspondence, and zeta implication A+L | The lower false-world rate is now proved: displacement `delta` forces eventual growth `exp((2 delta-o(1))a)`. The survivor is the reverse stability bound in terms of the supremal displacement `Delta` |
| NG-17 | Deriving the reverse localized-floor rate solely from the strip consequence `Psi(x)-x=O_eta(x^(1/2+Delta+eta))`, Stieltjes partial summation, and separate archimedean coercivity | Exact pole/main cancellation leaves a residual multiplier bounded by `exp((2 Delta+epsilon)a)(1+|t|)`, hence an `H^(1/2)` loss; the archimedean form controls only `log(1+t^2)`, and fixed-support modulations make the gap unbounded | A | A uniform oscillatory Mellin/exponential-sum estimate saving the derivative, or a genuinely joint prime--archimedean estimate |
| NG-18 | Deriving the reverse localized-floor rate only from a horizontal zero strip, full Riemann--von Mangoldt counting, symmetry, unsigned sampling, and even finite lower floor on every fixed support | Microscopic sparse clusters preserve counting to `O(1)` and qualitative local semiboundedness, yet boundary-bump tests make selected floors decay like `-exp(A_k^2+Delta A_k)` | A | A signed even/odd sampling-discrepancy estimate using Euler-product arithmetic; translation-bounded local horizontal second moment is one sufficient condition |
| NG-19 | Forcing positivity of the coefficient-defined trace-class xi companion through its natural leading sections, diagonal symmetrization, accretivity, raw Hankel moments, or coefficient total positivity as a weaker target | The dimension-two section has a certified nonreal pair and indefinite Hermitian part; the degree-six section has two left-half-plane eigenvalues; full `PF_infinity` is equivalent to RH by Edrei--Schoenberg | determinant algebra A; strict finite signs C | A genuinely infinite, non-compression arithmetic structure such as a sign-regular resolvent or normal dilation; finite Taylor sections cannot supply it |
| NG-20 | Replacing the signed Paley--Wiener Gårding inequality by pointwise positivity or a pointwise lower bound with the full logarithmic principal coefficient | The exact completed symbol is already negative at the certified `a=7/16` window; Kronecker recurrence aligns every active prime phase while the pole decays, forcing any pointwise coefficient-`1/2` remainder to be at least `B_a+log(2*pi)~4e^a` | recurrence and normalization A; negative scalar evaluation D with a deterministic unit test; compressed positive floor independently C/F | Retain the `PW_a` compression. A strict subleading pointwise coefficient remains logically open but would be a new uniform large-values theorem; the minimal compressed endpoint is RH-equivalent |
| NG-21 | Lifting positivity on all modulated interval/Fejer packets, even at every width and position, to positivity of the whole compressed Hermitian Toeplitz form | Individual packets omit coherent cross terms between separated blocks. A minimal `3 x 3` Toeplitz matrix, a continuous shifted-atom operator, and a real-even entire rank-three kernel all pass every packet while retaining a negative direction | finite and rational scalar algebra F; continuous and entire countermodels A | Add mixed Gram data for coherent packet superpositions or a zeta-specific arithmetic relation. One fixed separated-box cross orbit already detects the exact zero width, but bounding it is RH-equivalent |
| NG-22 | Obtaining a signed nonlocal Ward--innovation correction from exact Vaughan completion, Selberg's one-product Ward identity, and positivity of terminal Markov covariance | If `G` is the center/unequal-product remainder and `D` the tail diagonal, exact completion gives `G=K(C_full+E,C_full+E)-D`; the unknown completed carrier has only been renamed. The mandatory two-shift coefficient is `2log(p)log(q)cos(t log(p/q))`, of both signs | completion and Gram algebra A; complete finite arithmetic runs D | A genuinely new cutoff-complete two-shift correlation estimate for the full P4/R71 energy. This would be a direct arithmetic attack, not a Ward shortcut |
| NG-23 | Deriving a fixed exponential saving from a local Mobius cutoff martingale, Buchstab/scale contraction, factor-fiber gap, or centered Selberg--Riccati coercivity | Every finite cutoff tail has the same zero principal part, so shell differences are analytic and the carrier has multiplier one. The Riccati quadratic core admits `q=-1/(s-a)` at arbitrary `a` as a double-pole-null direction; the linear pole field remains. Exact completion is cutoff-invariant; explicit-center finite energies are nonmonotone | cutoff and Laurent algebra A; Riccati algebra A; complete finite arithmetic runs D | A genuinely global cross-product estimate retaining every cofactor and center term. One fixed saving is already essentially a fixed zero-free-strip theorem |
| NG-24 | Producing a completed fourth-moment power saving by independent-phase or exact-product Haar domination, or by first annihilating the rank-two center with a fixed second difference | Faithful finite completed blocks exceed both phase comparators.  The center-annihilator has a real-frequency multiplier bounded above and below and an explicit stable inverse, so it is norm-equivalent at every useful exponent | phase and multiplicative-energy formulas A; completed finite runs D; annihilator multiplier and inverse A | A coefficient-specific cancellation theorem for unresolved unequal products jointly with the continuous center; any fixed saving gives an explicit fixed zero-free strip |
| NG-25 | Obtaining the fixed fourth-moment saving from positive/monotone near-product cells, a power-saving pair-PNT variance, or a proportional-order scale filter | Pair-cell merge increments have both signs.  The pair Dirichlet series has a nonzero double pole at every zeta zero, so the required variance is already the same fixed strip.  Bernstein--Walsh forces an exponentially contracting all-carrier shift filter to have linear scale span, whose arithmetic cost restores the critical exponent | local moment and pole arguments A; filter theorem A; complete finite pair-cell runs D | A direct proof of the completed fixed-saving moment using genuinely new global arithmetic cancellation; the endpoint has exact exponent `4Delta` |
| NG-26 | Inferring positive-density completed-energy recurrence from the energy abscissa plus fixed Sobolev bounds, or from an arbitrary symmetric absolutely summable zero expansion with one off-line carrier but no attained outer edge | A sparse bump train has the exact energy abscissa and zero-density large blocks.  More sharply, successive non-attained quartet layers can approximate and cancel the earlier field on intervals occupying proportion `1-o(1)` while keeping their total coefficient `l1` mass summable | attained-edge Bohr theorem A; bump train and quartet construction A; clustered-divisor probe D | An attained outer edge, or a zeta-specific moving-edge uncertainty theorem using Riemann--von Mangoldt local counting and the prescribed detector coefficients |
| NG-27 | Obtaining a fixed R71 saving by optimizing a finite Ramanujan null gauge, estimating completed sectors separately, regularizing the zero Kloosterman index, or tensorizing an arbitrary primitive Farey-beat frame | `HK=0` transfers every gauge reduction to an exact contact term; determinant-zero fluctuations are harmless but leave the completed one-point prime axis. The matrix `(c_q(n))_(n,q<=Y)` has determinant `Y!`; `S(0,1;c)=mu(c)` makes a uniform axis power fixed-strip-strength. Square-root-denominator beats stably encode the axis and preserve its low-frequency zero carrier. R84 shows that the global canonical tensor avoids the generic rank cost, so rank is not the final obstruction | quotient, sector, rank, and frame algebra A; zero-index boundary L; finite sector/beat runs D | A coefficient-specific estimate for `H_(j theta!=0)-P_1-P_2` before absolute values |
| NG-28 | Converting the canonical common-dual low-beat tensor directly into a Wright saving, or prescribing the native low coefficients and discarding the high-beat repair by smoothness | The canonical coefficients are favorably separable as `W(theta/(pr))`, and `k=j theta` removes the shift triangle in the mask-free cofactor form, but this coefficient multiplies the slow phase rather than the native reciprocal phase. Reciprocity leaves `h_p conjugate(h_r)-gamma`. The high complement is onto but has exponentially small discrete-prolate directions; exact contact duality repays every Fourier-tail suppression when native low coefficients are prescribed | global frame, Mellin, reciprocity, Vandermonde, and powered-box algebra A; Wright boundary L; finite tensor/gauge runs D | Remove the finite primitive mask and prove an exact axis-renormalized reciprocal estimate for the full mismatch bracket, or derive an affine-in-theta counterterm with `Y^o(1)` projective mass |
| NG-29 | Obtaining the missing fixed power by centering the reciprocal phase at one, by a fixed-degree determinant counterterm, or by the exact top-prime affine null gauge | The true center is `mu_r(k)=c_r(k)/(r-1)`. The mean-zero nonresonant component is Wright-compatible, but its complement is `mu_r(k)h_p conjugate(h_r)-gamma`, essentially `-gamma`. IBP transfers the mismatch to a reciprocal derivative without changing this projection; killing it algebraically costs `1/abs(mu)asymp sqrt(H)`. The exact top-prime affine gauge costs `Y/T` on a low band, while at square-root scale its injective defect is the original Type-II tensor | arithmetic/Ramanujan and Ward/null-gauge algebra A; Wright fixed power L; complex finite falsifiers D | A signed prime-coefficient theorem for the complete square-root Type-II defect plus the canonical `gamma` contact, before arithmetic projection or absolute values |
| NG-30 | Obtaining that signed theorem from reciprocal zero-orbit completion, canonical-frame contraction, flat/smooth shift averaging, finite affine Schur controls, or balanced spectral reciprocity | With `R_j(p,r,theta)=e(-j theta inverse(p)/r)`, reciprocal transport has no zero shift character, so `R_j-I` has zero orbit exactly `-I`. Whitening gives a compressed unitary with an exact dissipative phase-defect square and Schur-leakage square, not a small parameter. Complete or long flat averaging suppresses the transported term and leaves `-gamma`. For the native `h_p=log(p)/p`, prime target points give a uniform full-scale residual in both Euclidean and canonical frame norms | shifted-Ramanujan, compression, averaging, and prime-point algebra A; spectral boundary L; exact finite compression runs D | Only a specially weighted complete R71 pairing, retaining every `g`-sector, mask, axis, seam, Type-I correction, and rectangular limit; test the actual amplitude's reciprocal-frequency variation before any norm split |
| NG-31 | Obtaining the R71 power for free by restoring common-`g` masks, degenerate axes, B-spline seams, Type I, and the natural rectangular limit | CRT/fiber Poisson is invertible; the only primitive zero character is a reducible face; the slow carrier is the punctured axis; exact all-sector recompletion reconstructs the original prime-minus-continuum energy. The actual reciprocal B-spline response is power-small relative to the slow axis in an explicit growing band | response, conservation, and spline/Gamma analysis A | A new signed high-determinant, reducible-face, and cross-cofactor estimate for the original completed energy |
| NG-32 | Producing a fixed strip from differentiated/conductor-cancelled positivity, marginal zero density, or a harmonic child cascade | Turan resolution needs derivative order `gg(delta log T)`, while retaining a zero at distance `e` against the closer pole needs `delta gg me`; hence only `e=O(1/log T)`. Harmonic positivity forces aggregate Poisson mass which an ordinary critical-line cloud can supply, and not a near-right child | explicit-formula, coefficient, and countermodel analysis A; zero-density inputs L | An actual-prime, target-conditioned signed cross-dilate estimate not implied by positivity or marginal density |
| NG-33 | Bounded-load, fixed-power-local, fixed-arity sign-reversing flow on squarefree Mobius collars | A positive-density family of sufficiently smooth odd squarefree vertices is isolated from every such exchange edge, for integral or fractional flow | flow implication and smooth-isolation proof A; smooth-number density L | Growing arity with joint signed smooth/rough cancellation, or long edges whose total boundary flux has an independent power bound |
| NG-34 | Using arbitrarily accurate q-free counting or exact Muntz quadrature as a nonvanishing theorem | `F_q(s)=zeta(s)/zeta(qs)` is uniformly zeta times a bounded nonzero factor right of `1/2`. The Muntz operator multiplies Mellin modes by zeta and therefore annihilates exactly the zero modes; a weight which retains them makes its output inherit the reciprocal-zeta pole | Euler/Mellin and convolution algebra A | A zero-sensitive weighted output with an independently proved fixed-power bound; the first natural example is the original centered prime discrepancy |
| NG-35 | Tempered polynomial interpolation which is nonnegative only on actual prime-power logarithms and cancels the closer pole at resolving scale | Prime logs have mesh `<<exp(-19X/40)`. Hiding a fixed negative Laplace mass in their gaps forces variation or degree-times-amplitude `gg exp(19X/40)`; at `X~log T` every stable/polylog-conditioned interpolant fails. Finite-order canonical products cannot encode the exponentially dense support | interpolation/variation algebra A; prime-gap theorem L | A power-conditioned superoscillatory weight together with a norm-uniform signed estimate for the full zero remainder |
| NG-36 | Promoting compact-local convergence of the Mobius Dirichlet series in a hypothetical fixed strip to vertical Bohr recurrence of `1/zeta` across `Re(s)=1` | For every finite block, Kronecker aligns `mu(n)n^(-it)` to `mu(n)^2`, so the uniform-convergence abscissa is exactly one. Accurate recurrence of a finite head around the reciprocal zero at `s=1` forces an order-one translated tail; full prime-phase return translates form a nonnormal family there | A | A recurrence-conditioned signed Mobius-tail estimate, or sufficiently fast growing-dimensional phase returns |
| NG-37 | Improving the fixed-power threshold by positive, capacitated, or phase-aware transport from the pole continuum to prime-power atoms | Radial projection of the Mellin spiral gives a lower cost `sigma integral e^(-sigma u)|D(u)|du`; arc length gives the matching upper threshold. Hence the convergence abscissa of optimal phase transport is exactly `sup Re(rho)`. Prefix Hall capacity is the same power-PNT discrepancy | A | A non-positive, scale-global estimate retaining the sign of the twisted prime--pole queue before taking transport cost |
| NG-38 | Pulling nonvanishing of later/reversed Luroth correlations back to the zeta-bearing first forward correlation, or obtaining it from a depth-uniform positive cylinder cone | The Perron operator contracts later lags toward a rational spectator but has a large kernel; reversed polynomial modes are rational and the forward/reverse pair laws are mutually singular. Positive future-digit martingales can have exponentially small target correlation | A | A coefficient-specific signed estimate for the first `O(t^2)` forward digits against the explicit Hurwitz-zeta tail |
| NG-39 | Removing the first-forward Luroth cancellation by adjacent pairing, finitely many resonance blocks, a finite polynomial observable, or recursive global Poisson summation | The natural cutoff is linear in height; every alias passes a nonzero Fourier coefficient, all stationary branches renormalize to exactly `zeta(1-s)`, and the second Poisson step is the neutral cycle `chi(s)chi(1-s)=1` | A | A genuinely new global relation among the actual complementary Dirichlet phases, not another Poisson/functional-equation rewrite |
| NG-40 | Obtaining a fixed power from closed normalized-scale cycles, coercive complex flows, finite pole-killing filters, or positivity/atomicity alone for the filtered prime queue | Scale shifts are a flat commuting cocycle; Hermitian Hodge projection deletes cycles, while noncoercive bilinear energy has false zero-cost sources. Finite filters have recurrent blind frequencies. A faithful continuous filter reduces the problem to one signed ramp, but positive atomic countermodels with off-line Mellin poles pass all generic sign and convexity tests | A | Prove either one-sided `O(x^a)`, `a<1`, envelope for the actual von Mangoldt ramp `sum Lambda(n)(2n/x-1)-1+x^(-1)` |
| NG-41 | Upgrading Mobius `B^2`/Carlson recurrence to pointwise or local-analytic recurrence around the zero of `1/zeta` at one | Same-line evaluation is unbounded and pays a sharp half-unit in Dirichlet `H^2`. More specifically, finite-prime conditioning selects Euler order: below one it tends to zero, whereas natural order tends hypothetically to `1/zeta(sigma)`; an explicit width-`1/log P` Euler boundary layer has exponentially growing local `L2` mass | A+L | A zeta-specific local-norm estimate at the Haar-null unit character, or an extraordinarily atypical recurrence-conditioned tail selection |
| NG-42 | Importing Puglisi v9's claimed `quasi-RH => RH` conclusion through its high-order alternating Taylor cutoff | Its Lemma 1 inequality is false at `x=13,J=30` in the exact final regime and is eventually reversed throughout every cutoff cell `J=2 floor(x+2)`; the uncontrolled Lagrange factor can dominate the alternating tail | exact integer and asymptotic analysis A | Quantitative control of the Taylor point below the true tail ratio, or a sign-definite integral remainder; the published argument supplies neither |
| NG-43 | Recovering the reciprocal-zeta divisor from a Hilbert--Schmidt prime diagonal by a regularized Fredholm determinant, Fock augmentation, index, or homotopy | `det_2(I-D_s)` is holomorphic and nonzero for `Re(s)>1/2`; the missing divisor is exactly the omitted first prime trace. That trace is nonclosable in `S_2`, the augmentation character is unbounded, and `I-D_s` is invertible, null-homotopic, and index zero | Schatten/Fredholm algebra A; finite probes D | A signed relative first-trace topology which is strong enough to retain the prime divergence and still admits an independent continuation or order theorem |
| NG-44 | Lowering the coefficient/Hilbert threshold by nonlinear Euler cancellation while preserving the reciprocal zero at one and no other zeros | Cancelling the prime layer lowers the threshold only by deleting the zero at one; every zero-preserving scalar germ retains a nonzero squarefree almost-prime layer and the half-unit barrier. More generally, a Dirichlet carrier with square-sum threshold below `1/2` and `T(1)=0` has a normal-convergence margin, so vertical recurrence forces artificial zeros approaching `Re(s)=1` | Euler/Taylor/Cauchy--Schwarz and recurrence algebra A; probes D | A non-scalar or non-normal construction whose first-trace anomaly is controlled without acquiring recurrent fake zeros |
| NG-45 | Escaping reciprocal recurrence or the coefficient barrier by an exceptional unimodular completely multiplicative twist | If the twisted reciprocal retains a simple zero at one, Landau positivity forces power pretentiousness to the trivial twist; Cauchy--Schwarz then makes the twist a normally convergent nonzero Euler multiplier of `1/zeta`. The same sign-alignment and boundary layer remain | pretentiousness/Euler-product analysis A | A genuinely non-normal, non-unimodular, or nonmultiplicative signed deformation with an independently controlled divisor |
| NG-46 | Bootstrapping an assumed fixed strip to a strictly wider strip using the imported PNT/Mertens converses, zero density, Turan power sums, classical repulsion, mollifiers, or functional symmetry | Conditional arithmetic bounds have infimal exponent exactly `Theta=sup Re(rho)` and their converses return it. Density/moments allow one sparse exception, Turan contradicts only `beta>Theta`, reciprocal tails decay only for `sigma>Theta`, and reflection sends the same band back to itself | conditional exponent analysis A; primary literature L | A per-zero negative-power count, a genuinely improved global arithmetic exponent, the one-sided signed ramp, or zeta-specific zero replication |
| NG-47 | Treating existence of an old-to-collar factor `Gamma=T A` at a Fredholm contact, an inverse/pseudoinverse or shifted-resolvent formula, finite invertible truncations, enlarged-support positivity, or an unqualified dense-core identity as an easier route to KNC | Closed range makes bounded factorization equivalent to `Gamma ker(A)=0`; the shifted factor has a reciprocal null-charge pole; PSD blocks permit only square-root alignment; a nonclosable summation factor fakes the identity on a dense graph core while charging the true kernel | finite algebra F; Hilbert factorization L; exact infinite-dimensional models A/C | A displayed inverse-free completed pole--archimedean--prime `T^src` with a declared operation grammar and independently proved closability/boundedness; otherwise use complete R71 or shifted `Psi` for the strip |
| NG-48 | Constructing `T^src` by finite regular Neumann/Krylov words, a regular translation-invariant xi-annihilator parametrix, a finite-rank boundary state, a collar-free causal ramp identity, scalar root--dilation noncommutativity, or coefficient-free split-Cauchy propagation | Finite division leaves the full contact charge; regular xi parametrices have residual one at zeros; the logarithmic source has infinite Hankel rank; and the causal ramp has collar `-V_delta`. R185 computes the exterior formulas. R186 serializes the split old operator and closes its weak/L2 form-domain adapter, but an exact synthetic PSD old-null split-Cauchy/dilation state retains nonzero exterior charge. Generic endpoint jets are also unavailable. Thus bookkeeping and soft covariance do not imply compatibility | finite algebra and exact rational/Gaussian-rational fixtures F; Suzuki/Carleman/Hankel/Landau inputs L; analytic project synthesis A | Seek a completed-zeta-specific unique-continuation, recurrence, quasianalyticity, or spectral-synthesis theorem for the total readout. For the strip, prove a new arithmetic bound for complete R71 or its globally oriented compact source derivative |

No row excludes all possible uses of its subject.  The last column is part of
the theorem's scope, not an invitation to call the surviving idea plausible.

## 3. Canonical theorem cards

### NG-01 — Compact-local invisibility of a remote quartet

**Statement.**  For `gamma, delta > 0`, let

```text
Q_(gamma,delta)(z)
  = ((z-gamma)^2+delta^2)((z+gamma)^2+delta^2),
A = gamma^2+delta^2.
```

For real `x`, `Q_(gamma,delta)(x)>0`.  For every fixed `R`,

```text
sup_(|z|<=R) |Q_(gamma,delta)(z)/A^2-1|
  <= 2 R^2/A + R^4/A^2,
```

which tends to zero as `gamma` tends to infinity with `delta` fixed.
Consequently, no integer-valued detector continuous for this compact-open
normalization can distinguish every such remote quartet from the baseline;
real critical-line phase alone cannot distinguish it at any height.

**Evidence and trust base.**  The inequality is an elementary analytic
calculation.  Lean checks the expansion, evenness, strict real positivity,
and sign preservation in
[`QuantizedPhaseIndexNoGo.lean`](lean/rhbridge/RHBridge/QuantizedPhaseIndexNoGo.lean),
with the advertised declarations listed in
[`QuantizedPhaseIndexNoGoAudit.lean`](lean/rhbridge/RHBridge/QuantizedPhaseIndexNoGoAudit.lean).
Lean does not presently check the compact-open estimate.

**Sharpness and nonclaim.**  Multiplication by `Q/A^2` changes global growth
and need not preserve an Euler product.  The theorem constrains compact-local
divisor or boundary-phase carriers, not arithmetic topologies that retain
global growth.  It does not construct a modified zeta function.

**Full argument.**
[`QUANTIZED-PHASE-INDEX-VERDICT-2026-08.md`](results/QUANTIZED-PHASE-INDEX-VERDICT-2026-08.md).

### NG-02 — Finite Euler loops lose their index at the all-prime limit

**Statement.**  Two assertions must be kept separate.

1. For `|r|<1`, the local unit phase
   `(1-r conjugate(z))/(1-r z)` on `|z|=1` contracts through nonvanishing unit
   phases by replacing `r` with `t r`, `0<=t<=1`.  Every finite product has
   trivial ordinary winding class.
2. For `0<a<1/2`, the literal two-sided shifted quotient has unbounded
   Besicovitch `B^2` norm as primes are added.  The functional-equation-
   normalized right phase is `B^2`-Cauchy for every `a>0`, but is not uniformly
   Cauchy for `0<a<=1/2`.

Therefore ordinary continuous-symbol winding does not pass from these finite
loops to an all-prime symbol in the RH-relevant strip: the topology in which
a limit is proved does not by itself supply an invertible continuous symbol,
and uniform symbol convergence fails.

**Evidence and trust base.**  Assertion 1 is F-rated in the phase module and
audit above.  Assertion 2 is A-rated: it uses prime-coordinate orthogonality,
the divergence/convergence of the displayed prime sums, unique factorization,
and Kronecker approximation.  Those analytic statements are not yet in Lean.

**Exact eliminated class.**  Uniform continuous-symbol limits of the two
finite-prime Euler-loop models specified in the report, equipped with ordinary
winding inherited from those approximants.

**Nonclaim.**  Uniform symbol nonconvergence does not prove nonconvergence in
a Calkin, strong, strict, or Fredholm-pair topology; no such operator model is
defined here.  No universal arithmetic index theorem is asserted.  A new
completion-native semifinite or relative index with a separately proved
operator topology is not addressed.

**Prior-art boundary.**  Almost-periodic Wiener--Hopf and mean-winding index
theories already exist, including work of
[Coburn--Douglas--Schaeffer--Singer](https://www.numdam.org/item/PMIHES_1971__40__69_0/),
[Murphy](https://doi.org/10.1016/j.jfa.2005.08.012), and
[Yakubovich](https://arxiv.org/abs/math/0606153).  The claim here is only the
failure of the two displayed Euler direct limits to furnish the required
continuous symbol, not a general theorem that mean topologies admit no index.

**Full argument.**
[`QUANTIZED-PHASE-INDEX-VERDICT-2026-08.md`](results/QUANTIZED-PHASE-INDEX-VERDICT-2026-08.md).

### NG-03 — Fixed finite-place Weil forms are eventually indefinite

**Statement.**  Fix a finite set `P` of primes and include the standard
archimedean place.  On the subspace annihilating the two pole moments, the
corresponding form has Fourier multiplier

```text
M_P(t) = -log(pi) + Re psi(1/4+i t/2)
         - 2 sum_(p in P) log(p) sum_(m>=1) p^(-m/2) cos(m t log p).
```

Then `M_P(0)<0`, whereas `M_P(t)` tends to positive infinity as `|t|` tends
to infinity.  Compactly supported broad bumps can satisfy the pole moments
exactly and concentrate their Fourier mass at zero.  Hence the fixed-place
form has a negative direction on sufficiently large support and is genuinely
indefinite.

**Evidence and trust base.**  A-rated conventional proof using Plancherel,
standard digamma asymptotics, and dominated convergence.  The floating-point
two-prime scan in the report is only D-rated corroboration and is not used in
the theorem.

**Sharpness and nonclaim.**  The prime set is fixed while support grows.  The
result neither contradicts positivity on a fixed small window nor treats the
full form, where newly active prime powers change with support.

**Prior-art boundary.**  The localization method is standard and belongs
near the variational Weil-form and semilocal literature, including
[Bombieri](https://eudml.org/doc/252338) and
[Connes--Consani](https://arxiv.org/abs/2006.13771).  The audit did not locate
the exact fixed-`P` indefiniteness statement.  This supports only “plausibly
new as stated,” pending specialist review.

**Full argument.**
[`TWO-PRIME-INFINITY-FAIL-FAST.md`](results/TWO-PRIME-INFINITY-FAIL-FAST.md).

### NG-04 — Optimal local Gram cost for one prime edge

**Statement.**  If vectors `u,v` in a real inner-product space satisfy
`<u,v>=w`, then

```text
2w <= ||u||^2+||v||^2.
```

The bound is attained by equal endpoint vectors.  Thus replacing the standard
difference-square representation of one negative cross coefficient by a
higher-rank direct sum of independent positive Gram channels cannot lower its
total endpoint diagonal cost.

**Evidence and trust base.**  F-rated in
[`PrimeEdgePolarization.lean`](lean/rhbridge/RHBridge/PrimeEdgePolarization.lean)
and its focused
[`PrimeEdgePolarizationAudit.lean`](lean/rhbridge/RHBridge/PrimeEdgePolarizationAudit.lean).

**Exact eliminated class.**  Independent place-by-place Gram channels that
reproduce each prime edge separately and sum their endpoint diagonal costs.

**Proof debt and nonclaim.**  The existing negative zeta-residual table is an
ordinary floating-point diagnostic.  Until a negative residual witness is
proved analytically or by a frozen interval certificate, the zeta-specific
application is not a complete no-go theorem.  Essential cross-place channels
are outside the local-cost theorem.

**Full argument.**
[`PRIME-EDGE-POLARIZATION-NOGO.md`](results/PRIME-EDGE-POLARIZATION-NOGO.md).

### NG-05 — Pure mixed pairings are not positive

**Statement.**  In a real inner-product space, a nonzero mixed coefficient
`2<u,v>` has a negative direction after replacing `v` by `-v`.  If the mixed
pairing is nonnegative for both signs, then `<u,v>=0`.

**Evidence and trust base.**  F-rated in
[`GlobalMobiusCancellation.lean`](lean/rhbridge/RHBridge/GlobalMobiusCancellation.lean)
and
[`GlobalMobiusCancellationAudit.lean`](lean/rhbridge/RHBridge/GlobalMobiusCancellationAudit.lean).
The same module imports mathlib's identity `moebius * log = vonMangoldt`; that
identity does not supply positivity.

**Exact eliminated class.**  A construction whose entire proposed positive
quadratic form is a nonzero pure off-diagonal Hilbert pairing.

**Nonclaim.**  Indefinite mixed terms can occur inside a positive block after
independently controlled diagonal terms are added.  Nonlocal Möbius incidence
is not itself ruled out.

### NG-06 — Later differentials cannot repair degree-zero energy

**Statement.**  In a two-step Hilbert complex
`C0 --d0--> C1 --d1--> C2`, the degree-zero Hodge energy is `||d0 x||^2`.
With `d0` and a scalar degree term fixed, its nonnegativity is exactly the
original relative Poincaré inequality and is independent of `d1`, even when
the square-zero law is imposed.

**Evidence and trust base.**  F-rated in
[`CompletedIncidenceComplexNoGo.lean`](lean/rhbridge/RHBridge/CompletedIncidenceComplexNoGo.lean)
and
[`CompletedIncidenceComplexNoGoAudit.lean`](lean/rhbridge/RHBridge/CompletedIncidenceComplexNoGoAudit.lean).

**Scope and novelty boundary.**  This is an elementary structural lemma, not
a standalone research theorem.  It eliminates only the proposal to repair a
fixed degree-zero form by appending or changing a later differential.

The Lean theorem concerns bounded continuous maps on ambient Hilbert spaces.
Applying it to a concrete continuum incidence operator additionally requires
a densely defined closed or closable realization, fixed domains and metrics,
and an exact normalized identification with the Weil form.  Those
zeta-specific obligations are not proved by this card.

**Survivor.**  A construction may change `d0`, the grading, the domain, or the
pairing, but then it must derive the target arithmetic form anew.

### NG-07 — Generic low-sector structure does not force contraction

**Statement.**  For the rank-one convolution form

```text
Q(f)=||f||_2^2-alpha |integral f|^2
```

on two disjoint sets of measures `m,n`, choose `alpha m<1`, `alpha n<1`, and
`alpha(m+n)>1`.  Both separate compressions are positive and the nonlocal
kernel is entire and even, yet the exterior response exceeds the old gap and
the union has a negative direction.  For `m=n=1`, `alpha=3/4` is a rational
example.  The exact one- and two-mode Schur pivots are also recorded.

**Evidence and trust base.**  F-rated countermodel and algebra in
[`HodgeLowSectorNoGo.lean`](lean/rhbridge/RHBridge/HodgeLowSectorNoGo.lean)
and
[`HodgeLowSectorNoGoAudit.lean`](lean/rhbridge/RHBridge/HodgeLowSectorNoGoAudit.lean).

**Exact eliminated inference.**  Contraction cannot be deduced solely from
self-adjoint convolution form, evenness, analyticity off the diagonal,
separate block positivity, and the weak old eigen-equation.

**Nonclaim.**  The countermodel is not the zeta kernel.  It leaves open an
event-specific estimate exploiting exact cancellation between prime and
archimedean response entries.

**Full argument.**
[`HODGE-LOW-SECTOR-DTN-NOGO.md`](results/HODGE-LOW-SECTOR-DTN-NOGO.md).

### NG-08 — Duality is weaker than a positive polarization

**Statement.**  For nonzero rational `a`, the real off-line block

```text
A_a = diag(1/2+a,1/2-a)
```

preserves the standard alternating functional-equation pairing, but there is
no strictly positive rational quadratic metric `G` satisfying
`A_a^T G+G A_a=G`.  The real critical-line block has the identity as a
positive control.  More generally, over the complex numbers a positive
Hermitian solution exists exactly when `A-1/2` is similar to a skew-Hermitian
matrix, equivalently when `A` is diagonalizable with spectrum on the critical
line.

**Evidence and trust base.**  The rational two-by-two statements are F-rated
in
[`FinitePolarizationNoGo.lean`](lean/rhbridge/RHBridge/FinitePolarizationNoGo.lean)
and
[`FinitePolarizationNoGoAudit.lean`](lean/rhbridge/RHBridge/FinitePolarizationNoGoAudit.lean).
The general finite-dimensional characterization is A-rated standard linear
algebra in the linked report.

The latter is an instance of classical Lyapunov/inertia theory; see, for
example, [Ostrowski--Schneider](https://doi.org/10.1016/0022-247X(62)90030-6).
No novelty is claimed for that equivalence.

**Exact eliminated inference.**  Functional-equation duality alone cannot be
promoted to positivity, and solving for a metric from already known spectral
data does not independently explain the critical line.

**Survivor.**  A geometric or arithmetic polarization fixed before and
independently of the spectrum.

**Full argument.**
[`GLOBAL-TRACE-POLARIZATION-FINITE-GATE-2026-08.md`](results/GLOBAL-TRACE-POLARIZATION-FINITE-GATE-2026-08.md).

### NG-09 — Static summable prime substitutions miss positive density

**Statement.**  Let `T` be a fixed countable dictionary of scale-compatible
sign-reversing templates `(p;q,r)` on odd squarefree dyadic collars, and
suppose

```text
sum_((p;q,r) in T) 1/(qr) < infinity.
```

Then a positive-density set of squarefree integers avoids both support
patterns `100` and `011` for every template.  Its intersection with
`(N/2,N]` has `(d/2)N+o(N)` elements, and none of those vertices can be an
endpoint of an allowed substitution.  The same holds for pairs of disjoint
nonempty finite prime sets of opposite parity with summable endpoint-cylinder
weights.  Bounded prime incidence implies the required summability.

**Evidence and trust base.**  A-rated proof.  Finite-prime squarefree density
is converted to a countable statement by an explicit prefix conditioning and
the deterministic tail bound

```text
#{n<=x : some tail template applies}
  <= x sum_tail (1/p+1/(qr)).
```

No independence between overlapping templates is assumed.  Independent
referee review and a full prior-art comparison remain amber debt.

The support-pattern event contains the event that a substitution is actually
available in a particular collar; it need not equal it, because the proposed
target can leave the collar.  Avoiding the larger cylinder is what yields the
claimed isolated vertices.

**Exact eliminated class.**  Fixed summable dictionaries, including every
fixed bounded-incidence family of finite, scale-compatible, parity-flipping
prime-set substitutions.  The theorem concerns applicability, so it applies
regardless of how an algorithm prioritizes applicable templates.

**Nonclaim.**  An `N`-dependent sequential matching with unbounded incidence
and global collision resolution is outside the theorem.  No Mertens estimate
is proved.

**Full argument.**
[`MOBIUS-STATIC-EXCHANGE-NOGO-2026-08.md`](results/MOBIUS-STATIC-EXCHANGE-NOGO-2026-08.md).

**Prior-art boundary.**  The density passage is close to classical
convergent-multiples arguments of
[Davenport--Erdos](https://www.impan.pl/en/publishing-house/journals-and-series/acta-arithmetica/all/2/1/93274/on-sequences-of-positive-integers),
while squarefree divisibility complexes already appear in
[Bjorner](https://arxiv.org/abs/1101.5704) and
[Pakianathan--Winfree](https://arxiv.org/abs/1104.4324).  The potentially new
piece is the exact scale-compatible substitution formulation and its
bounded-incidence corollary.  Priority remains unestablished.

### NG-10 — Fixed-cutoff conditioned Euler tails are zero-free

**Statement.**  Fix a prime cutoff `y` and a compact disk `K` in
`1/2<Re(s)<1`.  The conditional Bagchi tail after removing primes at most `y`
is almost surely the exponential of a locally uniformly convergent
holomorphic random series, hence is zero-free on `K`.  If the analytically
continued deterministic remainder has a zero in `K`, every boundary
approximation close enough for Rouché's theorem is impossible.  Its limiting
conditional probability is zero.

**Evidence and trust base.**  A+L-rated.  The local zero-free/Rouché
obstruction is elementary once the random Euler tail is constructed.  The
translation-frequency formulation uses Bagchi's functional limit framework
and a classical zero-density estimate, with sources and normalization in the
full report.

**Exact eliminated class.**  Fixed-cutoff phase conditioning followed by
ordinary zero-free random Euler-tail approximation to a zero-bearing
continued remainder.

**Nonclaim.**  A cutoff growing with height is a different shrinking-target
problem and is not covered.  It currently lacks the required zero-bearing
conditional small-ball theorem.

**Full argument.**
[`BAGCHI-CONDITIONED-TAIL-NOGO-2026-08.md`](results/BAGCHI-CONDITIONED-TAIL-NOGO-2026-08.md).

### NG-11 — Regular virial commutators cannot order the localized Weil spectrum

**Statement.**  Three claims have distinct trust bases.

1. If `H psi=lambda psi` and the commutator with a regular generator `G` is
   defined on `psi`, then

   ```text
   <psi,[H,G]psi>=0.
   ```

   Thus a strictly positive commutator on a nonempty pure-point spectral
   subspace is impossible.  Every finite matrix commutator also has trace
   zero, so it cannot be positive definite.
2. For the completed localized Weil form, geometric dilation has Fourier
   multiplier

   ```text
   r m_a'(r)
    = r tau_(1/4)(r)
      + sum_(log n<2a) (2 Lambda(n)/sqrt(n))(log n) r sin(r log n).
   ```

   In the prime-2-only window, this multiplier plus any fixed nonnegative
   multiple of `m_a` tends to minus infinity along an explicit frequency
   sequence.  Kronecker approximation makes all finitely many active
   prime-power slopes negative simultaneously at every fixed larger support.
3. If `G_v=v d/dx+v'/2` preserves the interval, then `v` vanishes at both
   endpoints and every nonzero such `v` has `v'<0` somewhere.  A
   high-frequency packet supported there in an interval shorter than `log 2`
   kills every prime translation and the pole term asymptotically.  The claim
   that its archimedean commutator tends to the negative `v'` average uses a
   localized pseudodifferential packet lemma whose symbol/remainder proof is
   not yet written out here.  Thus the transport conclusion remains
   conditional/Amber.

**Compression identity.**  For `P^2=P` and `R=I-P`,

```text
P[H,X]P=[PHP,PXP]+PHRXP-PXRHP.
```

The internal term has trace zero.  Any nonzero positive trace in a compressed
calculation is boundary leakage, not positivity of a pure commutator.

**Evidence and trust base.**  Lean checks the eigenvector identity, finite
trace obstruction, compression identity, and an exact `2x2` leakage model in
[`VirialCommutatorNoGo.lean`](lean/rhbridge/RHBridge/VirialCommutatorNoGo.lean),
with declarations listed by
[`VirialCommutatorNoGoAudit.lean`](lean/rhbridge/RHBridge/VirialCommutatorNoGoAudit.lean).
The bounded form-domain version, expressed only through Riesz representatives
and the pivot metric, is checked in
[`FormDomainVirial.lean`](lean/rhbridge/RHBridge/FormDomainVirial.lean) and
[`FormDomainVirialAudit.lean`](lean/rhbridge/RHBridge/FormDomainVirialAudit.lean).
The geometric-dilation symbol argument is A-rated.  The transport wave-packet
argument is Amber pending its localized archimedean remainder lemma.  The
Legendre prime-5 experiment is D-rated.

**Exact scope and nonclaim.**  This eliminates regular strict Mourre
estimates as an independent test, pure Galerkin commutator certificates, and
geometric dilation with a fixed scalar repair once a prime power is active.
The real transport-flow conclusion additionally depends on the named packet
lemma.  The result does not prove the Weil form indefinite and does not rule
out another local generator, a genuinely nonlocal mixed estimate, or a
singular support-moving generator.  The last must retain and sign the full
prime--archimedean--pole boundary defect; that is the existing collar problem
rather than a standard virial shortcut.

**Full argument.**
[`COMPLETED-WEIL-VIRIAL-COMMUTATOR-NOGO.md`](results/COMPLETED-WEIL-VIRIAL-COMMUTATOR-NOGO.md).

### NG-12 — Equivalent energy norms do not identify phase-labelled boundary families

**Statement.**  Let a coercive closed form define an energy Hilbert space `V`
on a finite interval, let differentiation be symmetric on a dense smooth
core, and assume the inclusion from the usual test-function topology on that
core into `V` is continuous.  The last hypothesis ensures that every
continuous energy-dual functional restricts to a distribution.  The
adjoint-domain argument is then valid in the energy dual:

```text
Dom(D*)={v : D^x(Jv) belongs to J(V)},
J(D*v)=D^x(Jv).
```

Consequently the deficiency vectors are `J^-1 exp(-izx)`, or
`T^-1 exp(-izx)` when the form is represented by `T`, and the deficiency
indices are `(1,1)`.  This repairs the topology/domain gap in the fixed-window
argument without assuming positivity at shift zero.

The repair does not make the extension spectrum independent of the coercive
shift.  For the exact Dirichlet family

```text
T_kappa=-d^2/dx^2+kappa  on H_0^1(-a,a),
```

the derivative at `z=0` of the boundary phase is `2+2r_kappa`, where
`r_kappa=(integral x T_kappa^-1 e^x)/(integral T_kappa^-1 e^x)`.  At `a=1`,

```text
r_0=(e^2-7)/6,             lim_(kappa->infinity) r_kappa=2/(e^2-1),
```

and these values are strictly different.  Thus equivalent shifted energy
norms do not, by themselves, identify the full phase-labelled extension
families by one constant boundary-phase relabeling.  This derivative argument
does not compare the complete zero sets at one specially selected phase.

A later zeta-specific scalar calibration is also insufficient: matching the
derivative at `z=i` forces two weak imaginary-axis values to high accuracy,
but those values are close to the universal Cayley factor.  Real and off-axis
held-out errors remain large and nonmonotone.  This prunes inference from the
one-jet calibration, not possible compact-local convergence at much larger
support.

There is a stronger exact necessary condition when an actual unitary adjoint
intertwiner is claimed.  Since every labelled defect fiber is one-dimensional,
the normalized defect Gram kernels must differ by a diagonal phase gauge.
Their pairwise magnitudes and Bargmann triple products are invariant.  An
affine-coordinate completed-Weil Galerkin scan retains a held-out defect, but
this last statement is diagnostic rather than an infinite-dimensional
theorem.

Across nested supports the shift itself has an exact obstruction.  Canonical
zero extension changes shifted energy by
`(sigma_a-sigma_b)||f||_2^2`.  For an antitone spectral-floor family, existence
on a cofinal support sequence of strictly admissible shifts tending to zero is
equivalent to nonnegativity of every floor.  Thus a natural-core construction
cannot use a vanishing auxiliary shift as an independent route to global
positivity.

**Evidence and trust base.**  The exact Riesz/partial-adjoint equivalences are
Lean-checked in
[`GelfandTripleAdjoint.lean`](lean/rhbridge/RHBridge/GelfandTripleAdjoint.lean).
The projective Gram theorem, scalar shift identity, and cofinal equivalence are
Lean-checked in
[`ProjectiveGramInvariant.lean`](lean/rhbridge/RHBridge/ProjectiveGramInvariant.lean),
[`NestedShiftRigidity.lean`](lean/rhbridge/RHBridge/NestedShiftRigidity.lean),
and
[`CofinalShiftPositivity.lean`](lean/rhbridge/RHBridge/CofinalShiftPositivity.lean).
The distribution-compatibility hypothesis, exponential classification, and
Dirichlet computation are A-rated analytic inputs/arguments.  The
completed-Weil phase scan is D-rated and is reported separately.

**Exact scope and nonclaim.**  This closes the generic inference from Hilbert-
space isomorphism to pointwise covariance of the full boundary family.  It
does not disprove a zeta-specific intertwiner, compare exact zeta zero sets at
one selected phase, or exclude a specially tuned shift/phase sequence, and it
says nothing directly about RH.  Any surviving finite-to-infinite
construction must specify those choices and prove that the comparison map
conjugates both the adjoint derivatives and their boundary spaces.  Exact
cross-window unitary equivalence is stronger than selected-extension
strong-resolvent convergence; failure of the former does not exclude the
latter.  In the zeta specialization, however, an admissible shift sequence
tending to zero already carries the RH-strength all-window positivity target.

**Full arguments.**
[`SUZUKI-ENERGY-ADJOINT-REPAIR.md`](results/SUZUKI-ENERGY-ADJOINT-REPAIR.md)
and
[`SHIFT-PHASE-COVARIANCE-FAIL-FAST.md`](results/SHIFT-PHASE-COVARIANCE-FAIL-FAST.md),
with the projective/cofinal checkpoint in
[`SUZUKI-PROJECTIVE-KERNEL-CHECKPOINT.md`](results/SUZUKI-PROJECTIVE-KERNEL-CHECKPOINT.md)
and the normalized scalar test in
[`SUZUKI-LIVSIC-CALIBRATION-FAIL-FAST.md`](results/SUZUKI-LIVSIC-CALIBRATION-FAIL-FAST.md).

### NG-13 — Fixed-support Weyl density does not control growing-support compact counts

**Statement.**  Let `Phi_a` be a strictly increasing real lift of the unit
boundary characteristic for a simple symmetric extension family.  On a
half-open interval its phase-level count is exactly

```text
N_(a,theta)((u,v])
  = floor((Phi_a(v)-theta)/(2*pi))
      - floor((Phi_a(u)-theta)/(2*pi)),
```

and differs from `(Phi_a(v)-Phi_a(u))/(2*pi)` by less than one.  Thus the
varying-support problem is a local phase-mass problem.

An ordinary Weyl law takes the opposite order of limits.  This failure persists
inside the regular de Branges class, not merely for an abstract escaping
sequence.  Put `u_(a,n)=pi*n/a`, `N_a=ceil(a^3/pi)`, and

```text
E_a=-b_i product_(n>N_a)b_(u_(a,n)+i)b_(-u_(a,n)+i).
```

Then `E_a=-H_a#/H_a`, where

```text
H_a(z)=(z+i)sin(a(z+i))
       /product_(n=-N_a)^N_a(z-u_(a,n)+i)
```

is entire Hermite--Biehler of exact type `a`.  It has the required reflection
symmetry, `E_a(i)=0`, and a fixed-`a` level count
`N_(a,theta)([-T,T])=2aT/pi+O_a(1)`.  Nevertheless, on every fixed compact,

```text
Phi_a(R)-Phi_a(-R)=4 arctan(R)+O_R(1/a).
```

All added phase density begins beyond order `a^2`; the Weyl remainder contains
a term of order `-a^3`.  Therefore no statement whose high-energy onset or
remainder is allowed to depend on `a` can imply fixed-compact crowding.

For the repaired Suzuki characteristic, Cartwright theory gives at fixed
`a`

```text
N_a([-R,R])=(d_a/pi)R+o_a(R),       0<=d_a<=2a.
```

The full coefficient `d_a=2a` additionally requires endpoint support of the
characteristic distribution, which Suzuki v1 does not prove.  The explicit
family above shows that even granting it does not repair the quantifier
reversal.  For the exact Suzuki kernel, the normalized defect coherence obeys

```text
Phi_a'(x)=2/[(1+x^2)rho_a(x)^2],
sigma_(a,theta)({lambda})=pi(1+lambda^2)rho_a(lambda)^2,
nu_(a,theta)({lambda})=rho_a(lambda)^2.
```

Thus support growth is precisely a zeta-specific decorrelation theorem, and
growing raw counts can be offset by shrinking raw Clark atoms or fixed-vector
weights.  Bounded-memory
completed-Weil models wind close to `L*T/(4*pi)` on the presently certified
range; that is D-rated evidence, not a continuum theorem.

**Evidence and trust base.**  The exact floor membership/cardinality/error
theorems and the escaping-onset spacing statements are Lean-checked in
[`BoundaryPhaseCounting.lean`](lean/rhbridge/RHBridge/BoundaryPhaseCounting.lean).
The scalar coherence consequences are Lean-checked in
[`BoundaryPhaseCoherence.lean`](lean/rhbridge/RHBridge/BoundaryPhaseCoherence.lean).
The kernel normalization, Hermite--Biehler countermodel, Cartwright
indicator-width formula, and endpoint-support boundary are A-rated
conventional analysis.  The numerical tables and their scope are in the two
checkpoint reports linked below.

**Exact scope and nonclaim.**  This rejects a fixed-support Weyl asymptotic as
the missing support-uniform theorem.  It does not reject compact-local
selected-divisor convergence, much less RH.  Moreover, divergent raw compact
counts would refute a locally uniform characteristic limit but not
strong-resolvent convergence by themselves: surplus eigenvectors may escape
weakly, and their fixed-vector weights can vanish.  A zeta-specific bound such
as weighted-average `rho_a^2=O_R(1/a)` would still control the raw-count
question.  The follow-up NG-15 shows, however, that fixed-core strong-
resolvent convergence is conditionally automatic while the canonical moving
reference vectors escape.  The surviving operator target is therefore a
stronger characteristic or boundary-scattering statement.

**Full argument.**
[`SUZUKI-SPECTRAL-COUNTING-CHECKPOINT.md`](results/SUZUKI-SPECTRAL-COUNTING-CHECKPOINT.md)
and
[`SUZUKI-COMPACT-PHASE-MASS-FAIL-FAST.md`](results/SUZUKI-COMPACT-PHASE-MASS-FAIL-FAST.md).

### NG-14 — A fixed coercive shift does not target the pure zeta-zero operator

**Statement.**  Grant RH and the global zero-frame representation.  With
`c=-sigma>0`, Plancherel gives

```text
Q_W(f)+c||f||_2^2
  = sum_gamma m_gamma |fhat(gamma)|^2
      + (c/(2*pi)) integral_R |fhat(t)|^2 dt.
```

The natural global Fourier completion therefore has multiplication measure

```text
sum_gamma m_gamma delta_gamma + c dt/(2*pi).
```

Its translation generator has a nonzero absolutely continuous component.
It is a different operator from the unshifted pure-point zeta-zero generator,
even after RH is assumed.  Hence a canonical fixed-negative-shift exhaustion
cannot be identified directly with Suzuki's stated unshifted target.

There is a second topology requirement.  If `sigma_alpha` is the raw Clark
measure, the canonical normalized reference-defect measure in the regular
model is

```text
nu_alpha(dx)=sigma_alpha(dx)/[pi(1+x^2)],
nu_alpha({lambda})=2/[(1+lambda^2)Phi'(lambda)]=rho(lambda)^2.
```

Its Stieltjes transform is root-free:

```text
m(z)=[i H_alpha(z)-z]/(1+z^2).
```

But these finite reference vectors move with the support.  Strong-resolvent
convergence controls their measures only if the comparison embeddings also
send them to one convergent ambient vector.  NG-15 proves that the natural
embeddings cannot do so: the normalized reference vectors weakly escape.  An exact full-type
Hermite--Biehler family additionally shows that at `alpha=-1` all normalized
Clark mass may escape to infinity; generic type and symmetry do not imply the
missing tightness.

**Evidence and trust base.**  Lean checks the raw/reference atom conversion,
the phase-density cancellation, and the strict positive mass added by a
negative shift in
[`ClarkSpectralWeight.lean`](lean/rhbridge/RHBridge/ClarkSpectralWeight.lean).
The absolutely continuous density uses Plancherel and Suzuki's global
zero-frame representation under RH.  The Herglotz conversion and explicit
countermodel are A-rated.  The completed-Weil phase and Cauchy rows are
D-rated and are not used to infer a continuum obstruction.

**Exact scope and nonclaim.**  This does not disprove Suzuki's proposed
varying-window limit, RH, or a noncanonical comparison construction.  It
forces the target to be stated correctly.  At fixed negative shift, the
honest canonical target has mixed spectrum.  To recover the pure target one
must either construct an operator-intertwining quotient or remove the shift.
For antitone cofinal window floors, however, existence of strictly admissible
shifts tending to zero is already equivalent to nonnegativity of every floor,
so the latter is not an independent proof of RH.

**Full argument.**
[`SUZUKI-WEIGHTED-CLARK-MEASURE-CHECKPOINT.md`](results/SUZUKI-WEIGHTED-CLARK-MEASURE-CHECKPOINT.md).

### NG-15 — Defect-vector escape makes the strong-resolvent limit phase-blind

**Statement.**  Let the finite window spaces be nested isometrically by zero
extension at one fixed common shift.  The `-i` defect vector `v_(a,-)` is the
Riesz representative of

```text
ell_-(f)=fhat(i)=integral f(x)e^(-x) dx.
```

Translation preserves the energy norm but multiplies this functional by an
arbitrary exponential factor.  Translating one fixed compact test toward the
left endpoint gives

```text
||v_(a,-)||^2 >= C exp(2a).
```

The Riesz projection identity across nested windows then implies that the
normalized vectors converge weakly to zero.  They cannot converge strongly,
even after phases are changed, to a nonzero global de Branges defect vector.
The `+i` vectors obey the reflected statement.

There is a complementary positive theorem under RH.  The global Weil space
is the completion of `C_c^infinity(R)` in a translation-invariant norm, and
translations form a strongly continuous unitary group.  Group mollification
shows that `C_c^infinity(R)` is a graph core for its Stone generator.  Hence
the closure of the compact-core derivative is already the self-adjoint zeta
translation generator.  Every finite self-adjoint extension agrees with this
generator on each fixed test once the window is large enough.  For every
off-real `z`, therefore,

```text
J_a(D_(a,theta(a))-z)^(-1)J_a*
  -> (D_infinity-z)^(-1) strongly
```

for every phase function `theta(a)`.  This is generalized strong resolvent
convergence because the embedded finite operators are nondense.  Arbitrary
self-adjoint completions on the orthogonal complements give the corresponding
ordinary strong-resolvent theorem.

The fixed-core scalar measures consequently converge, with finite atoms

```text
|hhat(lambda)|^2/K_a(lambda,lambda),
```

to `sum m_gamma|hhat(gamma)|^2 delta_gamma` in the unshifted RH model.  This
does not apply to the moving normalized defect kernels.

**Evidence and trust base.**  The exact projection/coherence/tail formulas
and the amplified Riesz lower-bound algebra are Lean-checked in
[`RieszKernelEscape.lean`](lean/rhbridge/RHBridge/RieszKernelEscape.lean).
The translation argument, Bochner-mollifier core lemma, dense-set resolvent
proof, and functional-calculus corollary are A-rated conventional functional
analysis.  A bounded-memory Galerkin norm scout agrees with the analytic
escape but is D-rated and unnecessary for the theorem.

**Exact scope and nonclaim.**  This proves neither RH nor failure of Suzuki's
entire-function limit.  The positive global space used for the unshifted
resolvent theorem is itself RH-conditional.  The theorem instead shows that
strong resolvent convergence is too weak to select extension phases or raw
eigenvalues: it holds for all phases while the boundary vectors disappear
weakly.  Locally uniform characteristic convergence, norm resolvent control,
or a renormalized boundary-scattering limit remains open and strictly
stronger.

**Full argument.**
[`SUZUKI-DEFECT-ESCAPE-AND-RESOLVENT-CHECKPOINT.md`](results/SUZUKI-DEFECT-ESCAPE-AND-RESOLVENT-CHECKPOINT.md).

### NG-16 — A global `L2` semibound is already RH-equivalent

**Statement.**  Let

```text
Q_W(f)=W(f*f_tilde),
lambda(a)=inf Q_W(f)/||f||_2^2
```

over nonzero smooth tests supported in `(-a,a)`.  Then the following are
equivalent:

```text
RH;
there is c<infinity with Q_W(f)>=-c||f||_2^2 globally;
inf_(a>0) lambda(a)>-infinity;
one strict shift sigma<lambda(a) works for every a.
```

Hence failure of RH forces `lambda(a)` to tend to `-infinity`, not merely to
become negative once.

For the analytic implication, put `g=-Psi`, where Suzuki proves
`W=-g''`, and set `h=g-(c/2)|t|`.  Positivity of `W+c delta_0=-h''`
implies, by a compact-mollifier double-primitive argument, that `h` is a
global screw function.  Krein--Langer then gives a Herglotz function on the
upper half-plane.  Suzuki's exact one-sided transform fixes it as

```text
q_c(z)=i(xi'/xi)(1/2-i z)+i c/2.
```

An off-line zero to the right of the critical line would produce a genuine
pole in that half-plane, a contradiction.  Reflection by the functional
equation excludes the left side.  Conversely, RH gives `c=0` by Weil
positivity.

**Evidence and trust base.**  The abstract equivalence between a uniform
lower bound and one strict global shift, and the `-infinity` alternative for
an antitone floor, are Lean-checked in
[`SemiboundedFloorDichotomy.lean`](lean/rhbridge/RHBridge/SemiboundedFloorDichotomy.lean)
and its audit.  The zeta implication is A+L-rated: it uses Suzuki's
distribution identity and transform, the Krein--Langer correspondence, and
Suzuki's form-core identification of the localized floor.  Bochner--Schwartz
plus the older Benedetto--Joyner tempered-Weil criterion gives an independent
short check.

**Exact scope and nonclaim.**  This does not rule out proving a uniform
completed bound; doing so would prove RH.  It rules out presenting that bound
or a globally admissible fixed negative shift as an easier scaffolding lemma.
Termwise autocorrelation estimates have coefficient sum asymptotic to
`4 exp(a)`, and the prime term itself is unbounded with support, so separate
component estimates cannot reach the target.  The subsequent quantitative
audit does produce an explicit two-bump family: a zero of displacement
`delta` forces `lambda(a)<=-C_epsilon exp((2 delta-epsilon)a)` eventually.
The pole proof controls the complete divisor, and the all-support upgrade uses
Bondarenko--Radchenko--Seip cardinal interpolation followed by smooth
truncation.  This is a conditional false-world theorem, not evidence that an
off-line zero exists.

**Full argument.**
[`SEMIBOUNDED-WEIL-DICHOTOMY.md`](results/SEMIBOUNDED-WEIL-DICHOTOMY.md).
The rate theorem is
[`QUANTITATIVE-WEIL-FLOOR-DIVERGENCE.md`](results/QUANTITATIVE-WEIL-FLOOR-DIVERGENCE.md).

### NG-17 — Prime-counting error does not control the reverse floor in `L2`

**Statement.**  Put `U=2a`, `X=exp(U)`, and

```text
R(x)=Psi(x)-x,
c_f(u)=integral f(x) conjugate(f(x+u)) dx.
```

After splitting `dPsi=dx+dR`, the pole term cancels the exponentially large
main prime term exactly.  The harmless remainder is bounded below by
`-4||f||_2^2`, while the error is

```text
E_U(f)=2 Re integral_0^U c_f(u) exp(-u/2) dR(exp u).
```

If all zero displacements are at most `Delta`, the standard explicit-formula
consequence `R(x)=O_eta(x^(1/2+Delta+eta))` and Stieltjes partial summation
give

```text
|E_U(f)| <= C exp((2 Delta+epsilon)a)
  [||f||_2^2 + integral |t| |fhat(t)|^2 dt/(2 pi)].
```

The exponent is the desired one, but the norm is not: the added integral is
the squared homogeneous `H^(1/2)` norm.  The archimedean part of the Weil
form controls only the logarithmic Fourier weight.  For a fixed compact bump
`g`, modulation by `exp(iNx)` preserves support and `L2` norm, while these
two energies grow respectively like `N` and `log N`.  Compact support
therefore supplies no missing interpolation inequality.

**Evidence and trust base.**  This is an A-rated Stieltjes partial-summation
calculation using the standard zero-strip prime-counting estimate.  It is
written with all normalizations in Section 7.1 of
[`QUANTITATIVE-WEIL-FLOOR-DIVERGENCE.md`](results/QUANTITATIVE-WEIL-FLOOR-DIVERGENCE.md).

**Exact scope and nonclaim.**  This does not disprove the reverse floor
estimate.  It eliminates the route that retains only the cumulative
prime-counting error and tries to absorb its Abel-summation loss using the
archimedean term separately.  A smoothed or oscillatory exponential-sum
estimate could still save the derivative, as could a joint estimate that
never separates the prime and archimedean pieces.

### NG-18 — Strip and counting data do not control signed vertical sampling

**Statement.**  Strip width, functional-equation symmetry, the full
Riemann--von Mangoldt count, unsigned sampling, and qualitative lower
semiboundedness on every fixed support do not jointly imply the reverse
localized-floor rate.  There is a simple symmetric order-one divisor with
counting discrepancy `O(1)` and finite floor on every fixed support, but with

```text
lambda(A_k) <= -c exp(A_k^2+Delta A_k)
```

along a sequence `A_k->infinity`.

The local mechanism is already visible in the divisor

```text
Z={plus_or_minus exp(k) plus_or_minus i Delta : k>=1},
```

with multiplicity `k`.  For a real even nonnegative compact bump `phi`, put

```text
f_0(t)=phi(t-b)-phi(t+b),
F_0(z)=2i phihat(z) sin(bz).
```

Then the paired block at height zero satisfies

```text
2 Re[F_0(i Delta) conjugate(F_0(-i Delta))]
  = -8 phihat(i Delta)^2 sinh(b Delta)^2 < 0.
```

Modulating `f_0` to frequency `exp(k)` preserves support and norm.  The
target block contributes `k` times this negative constant, while all other
blocks vanish asymptotically by uniform strip-Schwartz decay.  To restore the
full main count, begin with a real divisor having that count and, in sparse
fixed-length windows, relocate the `O(log T_k)` real nodes into these
conjugate clusters.  The gap/cluster discrepancy is still `O(log T)`.  The
windows can be chosen long enough that the residual real-node sampling tail
is smaller than the negative cluster.

The sharper construction begins with a critical-line quantile divisor of
density `w(T) asymp log T`.  Choose

```text
d_k=exp(A_k^2),
log T_k asymp d_k,
p_k=exp(-Delta A_k).
```

An interval of length `p_k` contains `m_k asymp p_k d_k` base nodes.  Pair
them and move each pair to the two simple off-line points of displacement
`Delta` at their midpoint.  The completed count changes by zero, and the
in-window discrepancy is at most one.

For any fixed support `a`, weighted Plancherel--Polya bounds make the tail
perturbation at most `C_(a,Delta) sup_(k>K)p_k` times the positive quantile
sampling energy.  It is absorbed for large `K`; the finite head is finite
rank.  Thus every fixed floor is finite.  At support `A_k`, however, an odd
two-boundary bump has vertical paired value of size `-c exp(2Delta A_k)`.
The cluster contributes

```text
-c m_k exp(2Delta A_k)
  asymp -c exp(A_k^2+Delta A_k),
```

while the critical-line background is only `O(d_k)`.  Rapid separation and
strip-Schwartz decay suppress the other clusters.

**Evidence and trust base.**  The construction and the quartet algebra are
A-rated.  The full proof and its normalization are in Sections 7.2--7.4 of
[`QUANTITATIVE-WEIL-FLOOR-DIVERGENCE.md`](results/QUANTITATIVE-WEIL-FLOOR-DIVERGENCE.md).
The existing `Stage4SamplingLiterature` interface records only the unsigned
upper-sampling theorem and does not rule out this behavior.

**Exact scope and nonclaim.**  The synthetic divisor is not zeta: it has no
Euler product.  The refined version deliberately does share zeta's
fixed-window semiboundedness and is sparse enough to obey ordinary global
zero-density bounds.  It proves that the missing input must be signed
Euler-product arithmetic controlling the placement of horizontal splitting,
not that the zeta reverse bound is false.

There is a sharp sufficient survivor.  If

```text
nu_2=sum m_j delta_j^2 delta_(gamma_j)
```

is translation bounded, then a Plancherel--Polya estimate applied to
`sinh(delta_j t)f` gives

```text
Q_W(f)>=-C M_2(1+a^2)[sinh(Delta a)/Delta]^2||f||_2^2.
```

Hence the localized-floor exponent equals `Delta`, even with infinitely many
off-line zeros.  This second-moment condition is not known for zeta.  Without
it, the survivor is a signed Garding estimate comparing the even `cosh` and
odd `sinh` traces jointly.

### NG-19 — Natural finite sections of the xi companion are not positive

**Statement.**  The centered function

```text
X(w)=xi(1/2+sqrt(w))/xi(1/2)=sum a_n w^n
```

has an explicit coefficient-defined trace-class companion `K` with
`det(I+wK)=X(w)`.  Its natural `N`-dimensional leading compression satisfies

```text
det(I+wK_N)=sum_(j=0)^N a_j w^j.
```

This finite-section route fails at the first nontrivial level.  The
dimension-two matrix is

```text
[[a_1,-a_2],[1,0]],
```

and rigorous 768-bit Arb balls give

```text
a_1^2-4a_2
  = -0.0004594955082930186652828466279458948... < 0.
```

It has a nonreal conjugate eigenvalue pair, admits no positive metric making
it self-adjoint, is not diagonally symmetrizable, and has indefinite Hermitian
part.  The raw coefficient Hankel minor is also negative.  At degree six the
certified Hurwitz signs are `+,+,-,-,-,-`; the Routh count gives two Taylor
roots in the right half-plane and therefore two companion eigenvalues in the
left half-plane.

**Evidence and trust base.**  The infinite determinant identity and the
finite compression formula are A-rated trace-class/rank-one algebra.  The
strict signs are C-rated FLINT/Arb interval results reproduced by
[`xi_companion_failfast.py`](src/xi_companion_failfast.py).  The complete
operator statement and coefficient enclosures are in
[`TRACE-CLASS-XI-COMPANION-GATE.md`](results/TRACE-CLASS-XI-COMPANION-GATE.md).

**Exact scope and nonclaim.**  This does not refute the infinite companion
identity or RH.  Taylor-section roots may escape to infinity, corresponding
to spurious eigenvalues collapsing to zero.  It closes leading-section
symmetrization, accretivity, oscillation, and raw-moment positivity as the
missing mechanism.

The infinite coefficient escape is not an easier named condition: by the
Edrei--Schoenberg classification, `PF_infinity` of `(a_n)` forces the product
of negative-real linear factors, and RH gives the converse.  Thus complete
Toeplitz total positivity and all-degree Jensen hyperbolicity are RH-equivalent
here.  A survivor must use genuinely infinite arithmetic structure not
visible in the leading compressions.

### NG-20 — The completed multiplier cannot be bounded pointwise at the endpoint scale

**Statement.**  For support radius `a`, direct Fourier compression of the
rank-two pole term gives

```text
Omega_a(t)=Re psi(1/4+it/2)-log pi
  -2 sum_(log n<2a) Lambda(n)n^(-1/2)cos(t log n)
  +4 integral_0^(2a) cosh(u/2)cos(tu)du.
```

At `a=7/16`, where only `n=2` is active,

```text
Omega_a(0)=-2.73971447387<0,
```

although the existing unrestricted certificate proves that the compressed
`PW_a` floor is strictly positive.  More generally, put

```text
B_a=2 sum_(log n<2a) Lambda(n)n^(-1/2).
```

Rational independence of the active prime logarithms and Kronecker recurrence
give `t_j->infinity` with all prime phases tending to one.  The pole symbol
tends to zero on that sequence, while the digamma asymptotic gives

```text
Omega_a(t_j)-(1/2)log(1+t_j^2) -> -B_a-log(2*pi).
```

Since `B_a~4e^a`, every pointwise lower bound with the full principal
coefficient needs the trivial exponential remainder.  It cannot prove the
displacement-sensitive reverse floor rate.

**Evidence and trust base.**  The pole sign, exact prime-main cancellation,
recurrence proof, and endpoint/RH quantifier audit are A-rated in
[`SIGNED-PRIME-GARDING-CHECKPOINT.md`](results/SIGNED-PRIME-GARDING-CHECKPOINT.md).
The scalar evaluation and low-memory scan are reproduced by
[`signed_garding_failfast.py`](src/signed_garding_failfast.py) and its unit
test.  The strict positive compressed floor at `a=7/16` is the existing
separate clipped-symbol certificate.

**Exact scope and nonclaim.**  This does not obstruct the form inequality.
It also does not eliminate a pointwise bound with a coefficient strictly
below `1/2`; the archimedean slack can pay for sufficiently late recurrence.
Such a bound would require a new uniform large-values estimate for the prime
Dirichlet polynomial.  The parsimonious survivor is the compressed endpoint,
not pointwise positivity.

### NG-21 — Triangular packets do not generate the full autocorrelation cone

**Statement.**  Positivity of a Hermitian Toeplitz or compressed convolution
form on every modulated interval indicator, even after allowing every interval
length and position, does not imply positivity of the form.

The smallest discrete example is

```text
    [ 1    0   5/4 ]
T = [ 0    1    0   ].
    [ 5/4  0    1   ]
```

Every consecutive modulated box has value at least `1/2`, but the endpoint
vector `(1,0,-1)` has value `-1/2`.  Dimension three is minimal.

On `L2(0,3/2)`, the even shifted-atom kernel

```text
k=delta_0+(5/4)(delta_1+delta_(-1))
```

has normalized packet value at least `1/6` for every width, position, and
modulation, while antisymmetric separated blocks have Rayleigh quotient
`-1/4`.  The phenomenon is not a distributional loophole: on a length-`L`
interval the real-even entire kernel

```text
k_ent(u)=2cos(pi u/(2L))-1/4
```

is nonnegative on all the same packets but negative on the projection of the
constant function orthogonal to the two exponential modes.

**Evidence and trust base.**  The complete analytic calculations, including
the global sinc inequality for the entire kernel, are in
[`TRIANGULAR-PACKET-CONE-NOGO.md`](results/TRIANGULAR-PACKET-CONE-NOGO.md).
Lean checks the exact finite/rational scalar values in
[`SelbergPacketConeNoGo.lean`](lean/rhbridge/RHBridge/SelbergPacketConeNoGo.lean),
with its focused axiom report in `SelbergPacketConeNoGoAudit.lean`.

**Exact scope and nonclaim.**  The theorem rules out a generic convex-density
or Toeplitz lift from diagonal Fejer packets.  It does not rule out a relation
special to the completed von Mangoldt comb.  The missing information is
polarized interference between separated packets.  In fact one fixed box's
separation orbit has exact growth exponent equal to the maximal horizontal
zero displacement; see
[`FIXED-BOX-WEIL-WIDTH-SPECTROMETER.md`](results/FIXED-BOX-WEIL-WIDTH-SPECTROMETER.md).
That survivor is a detector, not an independently proved bound.

### NG-22 — Exact completion collapses the nonlocal Ward remainder

**Statement.**  Let `K` be the terminal Markov covariance, let
`T=sum_n a_n phi_n` be the grouped Vaughan tail, let `Z` be its complete
center, and set

```text
D=sum_n abs(a_n)^2 K(phi_n,phi_n).
```

The proposed center/unequal-product remainder is exactly

```text
G=K(T-Z,T-Z)-D.                                          (NG22.1)
```

Exact Vaughan completion gives `T-Z=C_full+E_Y`, where `C_full` is the
completed von Mangoldt carrier and `E_Y` is the signed Type-I Euler-evaluation
defect.  Therefore

```text
G=K(C_full+E_Y,C_full+E_Y)-D.                            (NG22.2)
```

Selberg's identity can decompose a chosen semiprime part of `D` into a
connected term and factor-ratio anisotropy.  It has no second product index
and gives no sign to the remaining Gram entries.  After block Fourier
decomposition, the needed connected factor at `pq` is

```text
2log(p)log(q)cos(t log(p/q)),                             (NG22.3)
```

which changes sign.  Positive covariance alone gives only the sharp bound
`G>=-D`; elementary positive-semidefinite Gram models make either proposed
Ward orientation fail.

**Evidence and trust base.**  The completion and polarization calculation is
A-rated in
[`NONLOCAL-WARD-COVARIANCE-NOGO.md`](results/NONLOCAL-WARD-COVARIANCE-NOGO.md).
The exact semiprime and higher-cumulant coefficient gates are reproduced by
[`ward_vaughan_bridge_falsifier.py`](src/ward_vaughan_bridge_falsifier.py).
The complete B-spline/Vaughan diagnostic
[`ward_nonlocal_covariance_probe.py`](src/ward_nonlocal_covariance_probe.py)
retains every unequal product and the explicit center.  Its three-product and
44-product configurations reject all four natural sign orientations, but
those runs are D-rated floating diagnostics, not interval certificates.
The direct sign, diagonal-domination, and low-frequency gates are isolated in
[`DIRECT-CUTOFF-COMPLETE-TWO-SHIFT-GATE.md`](results/DIRECT-CUTOFF-COMPLETE-TWO-SHIFT-GATE.md)
and reproduced by
[`r71_two_shift_bound_probe.py`](src/r71_two_shift_bound_probe.py).

**Exact scope and nonclaim.**  This eliminates a sign derived from Vaughan
completion, the one-shift Ward identity, conditional expectation, or
polarization.  It does not exclude a large-scale theorem special to the exact
zeta coefficients and fixed window.  By (NG22.2), such a theorem must control
the complete two-shift P4/R71 energy itself.  The formal identity
`abs(xi'/xi)^2=-(xi'/xi)^2` on the critical boundary is not an escape: it
multiplies poles at known critical zeros, and an honest two-sided regulator
restores a contact term with mass `pi/sigma` near a simple zero.

### NG-23 — Local Mobius renormalization preserves every zero residue

**Statement.**  For `Re(s)>1`, let

```text
K=-zeta'/zeta,
A_Y=(1-zeta M_Y)(K-L_Y).
```

If `rho` is a zeta zero of multiplicity `m_rho`, then for every finite
cutoff `Y`,

```text
principal_part_rho A_Y=-m_rho/(s-rho).                  (NG23.1)
```

Consequently every finite shell difference `A_(Y')-A_Y` is analytic at
`rho`: the mode which the recursion must damp is an exact eigenvalue-one
direction.  The strongest centered Selberg recursion has Mellin form

```text
-Q'+2Q/(s-1)+Q^2=zeta''/zeta-2/(s-1)^2,
Q=-zeta'/zeta-1/(s-1).                                  (NG23.2)
```

Its homogeneous core is not coercive, since

```text
q_a=-1/(s-a),       -q_a'+q_a^2=0                       (NG23.3)
```

for every complex `a`.  This solves only the quadratic core: the linear term
in (NG23.2) leaves a simple pole.  Thus the off-axis pole is a
double-pole-null direction, not a solution of the full homogeneous equation;
there is no positive double-pole square.  Cole--Hopf normalization returns
the missing inverse-zeta factor.

**Evidence and trust base.**  The cutoff, Laurent, convolution, and Riccati
identities are A-rated in
[`MOBIUS-TWO-SHIFT-RENORMALIZATION-GATE.md`](results/MOBIUS-TWO-SHIFT-RENORMALIZATION-GATE.md).
The exact coefficient shell update and complete explicit-center finite gate
are reproduced by
[`mobius_cutoff_recursion_probe.py`](src/mobius_cutoff_recursion_probe.py).
At `X=25,Y:2->3`, the raw diagonal is unchanged while energy grows by a
factor `2.708`; other tested channels move in opposite directions.  These
finite runs are D-rated.  With the unevaluated Type-I head, the exact
completed field is cutoff-independent as Vaughan's identity requires.

**Exact scope and nonclaim.**  This closes local cutoff monotonicity,
finite-shell martingales, factor-fiber gaps, and Riccati double-pole
coercivity as sources of a fixed saving.  It does not refute a global estimate
special to the full Mobius coefficient.  After all local contractions are
removed, that survivor is the complete R73 remainder bound and is essentially
equivalent to a fixed zero-free strip.

### NG-24 — Phase transfer and center annihilation do not create a saving

**Statement.**  Let `F_I` be the compact completed R71 transform, with all
boundary channels and the signed rank-two center retained.  The natural
independent-phase fourth and sixth moments are

```text
2S_2^2-S_4,
6S_2^3-9S_2S_4+4S_6.                                  (NG24.1)
```

Grouping all pair or triple monomials with the same integer product gives
the corresponding exact-product Haar comparator.  Neither comparator
dominates the short real orbit in the complete finite model: at
`X=127,Y=8,T=80`, the completed/comparator ratios are respectively
`1.6335,1.7162` and `1.5947,1.6236` for moments four and six.

For fixed `h>0`, the exact center-annihilator

```text
Q_h=(tau_h-exp(h/2))^2                                  (NG24.2)
```

kills both `exp(R/2)` and `R exp(R/2)`.  On the real Fourier axis its
multiplier obeys

```text
(exp(h/2)-1)^2
 <=abs((exp(iht)-exp(h/2))^2)
 <=(exp(h/2)+1)^2.                                      (NG24.3)
```

It is explicitly invertible:

```text
Q_h^(-1)=exp(-h)sum_(j>=0)(j+1)exp(-jh/2)tau_h^j.       (NG24.4)
```

Thus a fixed-saving fourth-moment estimate after applying `Q_h` transfers
back to the original field.  The operator deletes the displayed center but
does not suppress the real low frequencies or unequal-product coherence.

**Evidence and trust base.**  The phase formulas, exact collision grouping,
multiplier bounds, and inverse series are A-rated.  The completed finite
ratios are D-rated and reproduced by
[`r71_fixed_strip_moment_probe.py`](src/r71_fixed_strip_moment_probe.py).
The full reduction and boundary-commutator audit are in
[`FIXED-UNIFORM-ZERO-FREE-STRIP-SPRINT.md`](results/FIXED-UNIFORM-ZERO-FREE-STRIP-SPRINT.md).

**Exact scope and nonclaim.**  The finite ratios refute the proposed
universal finite domination inequalities, not an asymptotic theorem special
to the actual Mobius--Vaughan coefficient.  The ellipticity argument closes
fixed center annihilation as an independent source of contraction, not as a
useful coordinate change.  The surviving completed four-shift estimate
remains open.

### NG-25 — Pair cells and proportional-order filters return the strip

**Statement.**  For a continuously translated fixed completed localizer,
let

```text
U_p(R)=integral abs(F_R(t))^pdt,       2<=p<infinity.
```

Fourier duality against a compact subwindow and the fixed-window pole law,
together with Hausdorff--Young in the other direction, give

```text
limsup_(R->infinity)log(1+U_p(R))/R=pDelta.             (NG25.1)
```

In particular, a fixed fourth-moment saving `kappa` is exponent-equivalent
to the strip `Re(rho)<=1-kappa/4`.

Grouping the exact pair channels into any cells gives

```text
U_4=D_atom+I_within+I_across.                           (NG25.2)
```

The increment from merging two cells is a signed cross inner product.  A
power-saving mesoscopic variance for the completed `Lambda*Lambda` measure
does not avoid (NG25.1): `(-zeta'/zeta)^2` has a nonzero double pole at every
zero, and the variance bound forces the identical fixed strip.

Finally, let a forward-shift filter have span `L_R` and multiplier `p_R`.
Bernstein--Walsh gives

```text
sup_t abs(p_R(d+it))
 <=exp(dL_R)sup_t abs(p_R(it)).                         (NG25.3)
```

Real-axis contraction `exp(-aR)` while retaining every carrier at
displacement `d_0` therefore requires
`L_R>=(a/d_0-o(1))R`.  The resulting proportional scale enlargement has a
square-root arithmetic cost exceeding the retained contraction whenever
`d_0<1/2`.

**Evidence and trust base.**  The moment/pole theorem, pair identity, variance
reverse implication, and filter tradeoff are A-rated in
[`FIXED-STRIP-FOURTH-MOMENT-PROOF-ATTEMPT.md`](results/FIXED-STRIP-FOURTH-MOMENT-PROOF-ATTEMPT.md).
The signed cell and merge behavior is reproduced by
[`r71_pair_cell_probe.py`](src/r71_pair_cell_probe.py); those finite runs are
D-rated.

**Exact scope and nonclaim.**  This closes positive or monotone cell merging,
the proposed pair-PNT variance as a weaker input, and proportional-order
finite-shift filtering as independent engines.  It does not prove or refute
the fixed strip.  A new global arithmetic cancellation theorem for the
completed pair field remains possible, but by (NG25.1) its fixed saving is
the strip itself at exponent scale.

### NG-26 — Non-attained edges need not recur with positive density

**Statement.**  The exact scale-energy abscissa and all fixed Sobolev bounds
do not imply positive-density large blocks.  If `R_n=2^(2^n)` and `phi` is a
fixed compact smooth bump, then

```text
f(R)=sum_n exp(delta R_n)phi(R-R_n)                     (NG26.1)
```

has weighted-`L2` abscissa `delta` and
`abs(f^(q)(R))<<_q exp(delta R)` for every fixed `q`, while every
fixed-length large-energy set has lower density zero.

The obstruction also occurs in a symmetric absolutely summable exponential
class.  Given

```text
0<d<delta_0<Delta<1/2,                                  (NG26.2)
```

there is a real-even quartet series with one nonzero `delta_0` carrier,
displacements increasing to but not attaining `Delta`, distinct nonzero
frequencies, and summable coefficient mass, such that

```text
lower_density{
 R:integral_0^L abs(G(R+u))^2du>=exp(2dR)
}=0.                                                     (NG26.3)
```

The construction uses a small higher-displacement trigonometric layer to
approximate the negative of all earlier layers on a long interval.  The
real displacement gap makes its Fourier `l1` cost summable; mirrored even
cutoffs give all four zero symmetries.

By contrast, if the global edge `Delta` is attained, absolute summability
gives

```text
exp(-Delta R)G(R)->sum_gamma b_gamma exp(i gamma R)     (NG26.4)
```

uniformly.  The nonzero Bohr diagonal then forces positive right lower
Banach density, with explicit lower bound

```text
sum abs(b_gamma)^2/
[2(sum abs(b_gamma))^2-sum abs(b_gamma)^2].              (NG26.5)
```

**Evidence and trust base.**  The attained-edge theorem and both
countermodels are A-rated in
[`EDGE-ATTAINMENT-RECURRENCE-GATE.md`](results/EDGE-ATTAINMENT-RECURRENCE-GATE.md).
The fixed-width R5 stress test is D-rated and reproduced by
[`clustered_divisor_recurrence_probe.py`](src/clustered_divisor_recurrence_probe.py).

**Exact scope and nonclaim.**  The quartet countermodel does not impose
Riemann--von Mangoldt local frequency counting and does not prescribe every
coefficient by the zeta triangular multiplier.  It eliminates recurrence
arguments using only symmetry, `l1` convergence, one carrier, and a
non-attained edge.  It does not refute a zeta-specific moving-record theorem.
The attained-edge theorem remains valid for the exact fixed-order zeta
detector.

### NG-28 — Canonical beat separability does not align its phase

**Statement.**  Let `A` be the ordered square-root-prime primitive beat bank
on `H` consecutive integers.  Its global frame operator is constant-tight,
and for the canonical common dual

```text
gamma_(p,r,theta)=W(theta/(pr)).                        (NG28.1)
```

Thus the low tensor is log-Mellin separable with projective loss
`H^((epsilon+delta)/2+o(1))` on `abs(theta)<=H^epsilon`; the generic
`H^(1/4)` rank cost is not intrinsic.  In the original nonprimitive cofactor
expansion, the off-axis amplitude is also separable after grouping
`k=j theta`, with only divisor loss.  The finite primitive basis retains an
open periodic mask.

Nevertheless the exact phases occur as

```text
gamma_(p,r,theta)e(j theta/(pr)),
h_p conjugate(h_r)e(j theta inverse(r)/p).              (NG28.2)
```

Additive reciprocity leaves the mismatch

```text
h_p conjugate(h_r)-gamma_(p,r,theta)                   (NG28.3)
```

on the slow phase.  Prescribing the native coefficients for
`0<abs(theta^flat)<=T` and completing with the high columns is algebraically
possible by Vandermonde surjectivity.  A powered-box witness gives

```text
lambda_min(A_high A_high^*)
 <<K^2 H^2 exp(-cT),                                  (NG28.4)
```

and exact null/contact duality gives

```text
norm(z_high)_2
 >=abs(<z_low,A_low^*G>)/norm(A_high^*G)_2.             (NG28.5)
```

Therefore smooth high-frequency suppression is repaid by coefficient growth
unless the prescribed low mismatch is already small against the whole
contact family.

**Evidence and trust base.**  The frame, Mellin, reciprocity, Vandermonde,
powered-box, and contact identities are A-rated in
[`COEFFICIENT-SPECIFIC-LOW-BEAT-TENSOR-GATE.md`](results/COEFFICIENT-SPECIFIC-LOW-BEAT-TENSOR-GATE.md).
Wright's scalar estimate and the discrete-prolate comparison are L-rated.
The finite tensor and gauge experiments are D-rated and reproduced by the
linked probes.

**Exact scope and nonclaim.**  This closes only the direct
canonical-tensor-to-Wright lift and the smooth-high-tail gauge shortcut.  It
does not close an axis-renormalized theorem for the full bracket.  NG-29 now
closes the fixed-degree affine-counterterm escape.  No zero-free strip is
proved or refuted.

### NG-29 — Arithmetic centering preserves the canonical contact

**Statement.**  For prime `r`, the complete primitive mean of the reciprocal
phase is

```text
mu_r(k)=c_r(k)/(r-1).
```

Consequently the native-minus-canonical bracket splits exactly as

```text
h_p conjugate(h_r)[e(-k inverse(p)/r)-mu_r(k)]
 +mu_r(k)h_p conjugate(h_r)-gamma_(p,r,theta).         (NG29.1)
```

If `r` does not divide `k`, then `mu_r(k)=-1/(r-1)`.  Existing
Kloosterman-fraction estimates can power-save the first, mean-zero bracket,
but the second remains `-gamma` up to an extra inverse-modulus term.  If
`r|k`, the first bracket is zero and the second is the literal axis.

For `A_L=g integral L(u+gj,u)e(theta u/(gmn))du`, compact support gives

```text
theta A_L=-gmn A_((partial_1+partial_2)L)/(2 pi i).    (NG29.2)
```

This can attach the mismatch to a reciprocal derivative term.  For any
interpolating coefficient `a`, however, the exact identity retains

```text
mu_r(k)a-gamma                                        (NG29.3)
```

on the slow phase.  Setting it to zero multiplies the coefficient ledger by
`1/abs(mu_r(k))=r-1`, which overwhelms every imported fixed power.

There is one exact derivative null gauge for R82's primes `Y<p,r<=2Y`, but
its determinant multiplier is `Y theta/(pr)asymp theta/Y`; changing the low
band `abs(theta)<=T` at natural size costs `Y/T`.  At R84's useful
`p,r asymp sqrt(Y)` scale the null relation fails by the near-square
prime-multiple tensor.  With disjoint multiple supports that defect map is
injective and has squared Hilbert--Schmidt size `asymp Y^3 norm(D)_F^2`.

**Evidence and trust base.**  The Ramanujan mean, carrier split, Ward
identities, top-prime null gauge, and square-root injectivity calculation are
A-rated in
[`NATURAL-MEAN-AFFINE-FIXED-POWER-GATE.md`](results/NATURAL-MEAN-AFFINE-FIXED-POWER-GATE.md).
The localized `H^(-1/40)` reciprocal saving imports Wright and remains
conditional on R84's uniform kernel/seam ledger, hence L-rated.  The native
complex-phase and quadrature checks are D-rated.

**Exact scope and nonclaim.**  This closes arithmetic recentering,
fixed-degree determinant moments, and the top-prime null cloud as independent
fixed-power engines.  It does not rule out cancellation specific to the
joint prime-derived `gamma` and square-root Type-II defect.  Proving that
signed joint estimate would be the desired fixed-strip-strength theorem.  No
fixed strip, RH, or negation of RH follows from NG-29.

### NG-30 — Reciprocal compression exposes rather than cancels the contact

**Statement.**  Concatenate the ordered primitive square-root-prime frames

```text
A_(n;(p,r,theta))=e(theta n/(pr)),
S=AA^*,
gamma=A^*S^(-1)v,
(R_j)_(p,r,theta)=e(-j theta inverse(p)/r).             (NG30.1)
```

Then the exact transported kernel is

```text
(A R_jA^*)(t,m)
 =sum_(p!=r)c_p(t-m)c_r(t-m-j).                         (NG30.2)
```

With `U=A^*S^(-1/2)`, `x=S^(-1/2)v`, and `C_j=U^*R_jU`,

```text
S^(-1/2)A(R_j-I)gamma=(C_j-I)x,

Re<x,(C_j-I)x>=-norm[(R_j-I)gamma]_2^2/2,              (NG30.3)

norm[(R_j-I)gamma]_2^2
 =norm[(C_j-I)x]_2^2+norm[(I-UU^*)R_jgamma]_2^2.       (NG30.4)
```

On every fixed-`r` block the shift Fourier projection of `R_j` at zero is
zero, because `theta inverse(p)` is nonzero modulo `r`.  Hence `R_j-I` has
zero orbit `-I`.  Complete shift averaging sends the signed field to `-v`;
over `N` consecutive shifts its transported remainder is `O(sqrt(H)/N)` in
the canonical metric.

For the actual native coefficient

```text
d_(p,r,theta)=[log(p)/p][log(r)/r],
```

one has

```text
(A R_jd)(n)=sum_(p!=r)h_ph_r c_p(n)c_r(n-j).           (NG30.5)
```

At every prime target point above the bank, (NG30.5) is at most
`(sum h_p)^2-sum h_p^2=O(1)`, uniformly in `j`, while
`v_n=Lambda(n)-1=log n-1`.  The PNT and the R84 frame bounds therefore give
a constant lower bound for the full native residual in both `l2` and
`S^(-1)` norms.

**Evidence and trust base.**  The shifted kernel, whitening, dissipation,
Schur leakage, shift-Fourier projections, short-average estimate, and
prime-point ceiling are A-rated in
[`SIGNED-JOINT-RECIPROCAL-COMPRESSION-GATE.md`](results/SIGNED-JOINT-RECIPROCAL-COMPRESSION-GATE.md).
The spectral-reciprocity and Eisenstein-coefficient boundaries are L-rated.
The exact finite identities and compression rows are D-rated and reproduced
by
[`common_dual_reciprocal_compression_probe.py`](src/common_dual_reciprocal_compression_probe.py).

**Exact scope and nonclaim.**  This closes a Euclidean or canonical-Hilbert
contraction of the complete native square-root block, ordinary shift
completion, smooth flat-shift mixing, finite affine-moment control, and
balanced reciprocity as independent engines.  It does not lower-bound the
complete signed R71 form by isolating one block.  A cancellation special to
the full B-spline kernel, all cofactors, axes, seams, Type-I corrections, and
natural rectangular limit remains open.  No fixed strip, RH, or negation of
RH follows from NG-30.

### NG-31 — Exact sector recompletion conserves the R71 carrier

**Statement.**  On every reduced primitive cofactor sector, CRT followed by
Poisson summation along the solution fiber gives

```text
A_theta(j)=g integral L(u+gj,u)e(theta u/(gmn))du,

sum_j A_theta(j)e(j alpha)
 =sum_k Lhat(-(k+alpha)/g,
             (k+alpha-theta/(mn))/g).                 (NG31.1)
```

The canonical slow character is `alpha=theta/(mn)` and has the exact
punctured-axis term `Lhat(-theta/(gmn),0)`.  The reciprocal character stays a
distance at least `1/m` and `1/n` from both axes when `m,n>1`; its only zero
character is the reducible `m=1` or `n=1` face.  Common-`g` masks translate
the amplitude by fractions of `1/g` without changing this classification.

Restoring every sector gives the conservation identity

```text
H_nonW+H_off
 =<sum_n Lambda(n)delta_n-dt,
    L(sum_n Lambda(n)delta_n-dt)>.                    (NG31.2)
```

The exact Type-I head reconstructs the same field.  For the actual R71
B-spline, total variation across every seam gives reciprocal response
`Y^(-1/2+o(1))` relative to kernel mass, while an exact Gamma asymptotic
keeps the slow axis nonzero on an explicit growing band.

**Evidence and trust base.**  The CRT, Poisson, masks, sector conservation,
Type-I comparison, spline variation, and Gamma-band proofs are A-rated in
[`FULL-R71-RECIPROCAL-RESPONSE-GATE.md`](results/FULL-R71-RECIPROCAL-RESPONSE-GATE.md).

**Exact scope and nonclaim.**  This closes hidden algebraic cancellation and
unrecorded B-spline seam conversion.  It does not estimate the signed
high-determinant/reducible-face cofactor sum which equals the original energy.
No strip or no-strip conclusion follows.

### NG-32 — Pole retention and critical-line capacity stop positivity cascades

**Statement.**  For `Q_m=(-1)^mD^(m)` and `p=m+1`, a target
`rho_0=1-e+iT` seen from `sigma=1+delta` has, relative to the pole at one,

```text
r=(delta/(delta+e))^p.                               (NG32.1)
```

Keeping `r>=r_0>0` forces `delta gg pe`.  Resolving the `Theta(log T)` zeros
in the local vertical cloud by a reciprocal-power/Turan step requires
`p gg delta log T`.  Combining the two inequalities gives

```text
e log T=O_(r_0)(1).                                   (NG32.2)
```

Conductor-cancelled trigonometric positivity does not bypass (NG32.2).  It
only imposes moments of a positive circle measure.  The measure

```text
(1-q)dtheta/(2pi)+q delta_pi
```

satisfies every scalar, tensor, and Toeplitz positivity inequality while
placing the required first-harmonic displacement in ordinary moments.
Moreover, an abstract Riemann--von Mangoldt multiset with all collateral
zeros on `Re=1/2` can realize those moments by moving only `O(1/e)` zeros in
each harmonic block.  The known zero-free region makes `1/e=o(log T)`, so
the critical-line cloud has ample capacity.  No near-right child is forced.

**Evidence and trust base.**  The differentiated ledger and exact tradeoff
are A-rated in
[`R89-DIFFERENTIATED-POSITIVITY-GATE.md`](results/R89-DIFFERENTIATED-POSITIVITY-GATE.md).
The all-degree moment and critical-line compensation constructions are
A-rated in
[`R90-TARGET-CONDITIONED-HARMONIC-CASCADE-GATE.md`](results/R90-TARGET-CONDITIONED-HARMONIC-CASCADE-GATE.md).
The zero-free-region and density comparisons are L-rated.

**Exact scope and nonclaim.**  This closes differentiation, another
trigonometric-polynomial search, marginal density, and child iteration as
standalone engines.  It does not rule out an arithmetic correlation which
holds specifically when `T` is a near-one zeta-zero ordinate.

### NG-33 — Smooth vertices isolate every bounded-arity local Mobius flow

**Statement.**  Suppose a flow on odd squarefree integers changes at most
`k` primes per side, has displacement at most `D N^(1-alpha)`, bounded load,
and divergence `mu(n)` outside `O(N^(1-beta))` collar vertices.  Its boundary
flux would imply

```text
M(N)=O(N^(1-min(alpha,beta))).                         (NG33.1)
```

But with

```text
y=(N^alpha/(8D))^(1/k),                               (NG33.2)
```

every sufficiently large odd squarefree `y`-smooth collar vertex is isolated
from the exchange graph.  Such vertices have asymptotic positive density
proportional to `rho(k/alpha)`.  Hence a linear set, not a power-small
exception, violates the divergence requirement.  Fractional matchings and
symmetric Markov kernels obey the same Hall/cut obstruction.

**Evidence and trust base.**  The transfer, prefix-cut, fixed-arity
isolation, and fractional-flow arguments are A-rated in
[`R89-MOBIUS-NEAR-ISOMETRIC-FLOW-GATE.md`](results/R89-MOBIUS-NEAR-ISOMETRIC-FLOW-GATE.md);
the smooth-number asymptotic is L-rated.

**Exact scope and nonclaim.**  This eliminates bounded-arity power-local
transport, not global Mobius cancellation.  Growing arity or a signed bound
for long-edge flux remains possible.  The positive-density isolated set is
not evidence that its signed sum is large.

### NG-34 — Accurate q-free counts and Muntz quadrature preserve or erase the divisor

**Statement.**  For every integer `q>=2`,

```text
Q_q(x)=x/zeta(q)+O(x^(1/q)),
F_q(s)=zeta(s)/zeta(qs).                                (NG34.1)
```

Uniformly for `Re s>=sigma_0>1/2`, `F_q` is zeta times a factor bounded
above and away from zero independently of `q` and height.  Thus even an
arbitrarily small counting-error exponent leaves every target zero in place.

The Newton/Riesz heat transform gives a sharper-looking exact identity.  If

```text
F(t)=sum_n mu(n)n^(-2)e^(-t/n^2),
h(x)=x^(-2)F(x^(-2)),                                  (NG34.2)
```

then

```text
M[h](s)=Gamma(1-s/2)/(2zeta(s)),
sum_m h(mx)=x^(-2)e^(-x^(-2)).                         (NG34.3)
```

The dilation sum is exponentially small because its Mellin multiplier is
`zeta(s)`: it cancels exactly the pole of `M[h]` at every zeta zero, with
full multiplicity.  More generally a weighted dilation with Dirichlet
series `A` has output coefficients `a*mu` and multiplier `A/zeta`.  A tame
output makes `A` carry the annihilating zeta factor; a zero-sensitive output
inherits the reciprocal-zeta pole.  Taking `a(n)=log n` gives `a*mu=Lambda`
and returns the centered prime heat discrepancy.

**Evidence and trust base.**  The q-free estimates and uniform comparison
are A-rated in
[`R90-QFREE-RATIO-NONVANISHING-GATE.md`](results/R90-QFREE-RATIO-NONVANISHING-GATE.md).
The Newton equivalence, lossless Poissonization, Muntz identity, and weighted
dichotomy are A-rated in
[`R90-NEWTON-COEFFICIENT-CANCELLATION-GATE.md`](results/R90-NEWTON-COEFFICIENT-CANCELLATION-GATE.md).

**Exact scope and nonclaim.**  Continuation, counting accuracy, and
quadrature accuracy are not lower bounds.  A fixed power beyond the unsigned
Newton scale remains an exact sufficient target and is not disproved.

### NG-35 — Prime-support interpolation must be superoscillatory

**Statement.**  A differentiated weight `W` need only satisfy
`W(log p^j)>=0`; it may be negative between prime powers and can therefore
reverse continuous Laplace monotonicity.  This loophole is real.  However,
the prime-log mesh above height `X` satisfies

```text
Delta(X)<<exp(-19X/40).                                  (NG35.1)
```

If `A=H_W(delta+e)>0` and pole cancellation retains fixed reserve,
`H_W(delta)<=qA` with `q<1`, then the negative pole-weighted mass is at least
`(1-q)A`.  Negative mass hidden above `X` obeys

```text
N_delta(X;W)<=Delta(X)e^(delta Delta(X))V_delta(X;W),
N_delta(X;W)<=(deg W+1)Delta(X)B_delta(X;W).             (NG35.2)
```

Thus a stable interpolant resolving zero spacing at `X asyp log T` pays a
fixed power of `T` in variation, degree, or amplitude.  A finite-order
canonical product cannot evade this because prime logarithms have
exponential counting density in `X`.

**Evidence and trust base.**  The discrete example, reserve lemma, mesh
inequalities, and explicit-formula criterion are A-rated in
[`R90-DISCRETE-PRIME-SUPPORT-INTERPOLATION-GATE.md`](results/R90-DISCRETE-PRIME-SUPPORT-INTERPOLATION-GATE.md).
The exponent `19/40` imports Baker--Harman--Pintz and is L-rated.

**Exact scope and nonclaim.**  Tempered and stable interpolation is closed.
An arbitrarily power-conditioned superoscillatory weight is not ruled out,
but it must also satisfy a norm-uniform signed estimate for every collateral
zero and trivial term.  That estimate remains fixed-strip strength.

### NG-36 — Conditional Mobius convergence is not vertical recurrence

**Statement.**  For every real `sigma` and finite block,

```text
sup_t abs(sum_(N<n<=M)mu(n)n^(-sigma-it))
 =sum_(N<n<=M)mu(n)^2n^(-sigma).                       (NG36.1)
```

Indeed, Kronecker recurrence can make every prime phase in the block tend to
`-1`, turning each nonzero Mobius summand positive.  Thus the abscissa of
uniform convergence of `sum mu(n)n^(-s)` is exactly one, unconditionally.
Under a hypothetical strip `Re(s)>theta`, the same series converges only
compact-locally there.  On every Rouche circle around the simple zero of
`1/zeta` at `s=1`, an accurate `+1` phase return of a finite head forces the
translated conditional tail to have a fixed order-one norm.  Along a full
diagonal prime-phase return sequence, the translates of `1/zeta` are not a
normal family on that disc.

**Evidence and trust base.**  A-rated proofs by Kronecker, partial summation,
Rouche, Montel, the identity theorem, and Hurwitz are in
[`R94-RECIPROCAL-ZETA-VERTICAL-RECURRENCE-GATE.md`](results/R94-RECIPROCAL-ZETA-VERTICAL-RECURRENCE-GATE.md).

**Exact scope and nonclaim.**  This closes only the inference from a fixed
strip to height-uniform Dirichlet-tail control or ordinary Bohr recurrence
across the absolute-convergence boundary.  It neither disproves a fixed strip
nor bounds the recurrence-conditioned tail.  Proving that tail small along
one sufficiently accurate return sequence would prove the no-strip
alternative.

### NG-37 — Positive Mellin transport retains the full PNT exponent

**Statement.**  Put

```text
D(u)=psi(exp u)-(exp u-1),
d_s(u,v)=abs(exp(-su)-exp(-sv)),       Re(s)=sigma>0.
```

After equalizing the two finite-cutoff masses at the endpoint, the optimal
transport cost satisfies

```text
sigma integral_0^U exp(-sigma u)abs(D(u))du
 <=W_(d_s)(U)
 <=abs(s) integral_0^U exp(-sigma u)abs(D(u))du.       (NG37.1)
```

The lower bound is contraction to the strictly monotone radial coordinate of
the Mellin spiral; the upper bound is monotone transport measured in spiral
arc length.  Consequently its convergence threshold is exactly
`sup Re(rho)`.  A power-local positive matching also forces the corresponding
power-saving PNT estimate through the Hall prefix cut.

**Evidence and trust base.**  A-rated cumulative-flux, one-dimensional
transport, Hall, and partial-summation proofs are in
[`R94-PRIME-POLE-PHASE-TRANSPORT-GATE.md`](results/R94-PRIME-POLE-PHASE-TRANSPORT-GATE.md).

**Exact scope and nonclaim.**  Positive couplings, chord/arc costs, and
capacitated local matchings are constrained.  A signed flow may cancel across
many cuts before a modulus is taken and is outside the theorem.  Establishing
a fixed power for that signed queue would itself prove a fixed strip.

### NG-38 — Luroth mixing reaches a rational spectator, not the zeta lag

**Statement.**  For the Luroth Perron operator,

```text
Lip(Pf)<=(pi^2/3-3)Lip(f).                             (NG38.1)
```

This makes sufficiently late forward Mellin correlations nonzero, but those
correlations converge to `1/(2s)` rather than to the first-lag carrier
`(s-1)zeta(s)/[s(s+1)]`.  The operator has an explicit infinite-dimensional
kernel, so the conclusion cannot be inverted.  Reversed affine and
polynomial correlations are rational spectators; their pair law is mutually
singular to the forward graph law.  Moreover positive finite-depth
future-digit martingales can have correlation `O(2^(-m))` at a target zero.
The exact digit tail beyond `N` is a Hurwitz-zeta expression and is coherent
for `N gg |s|^2`, leaving the first `O(t^2)` digits as the unresolved signed
head.

**Evidence and trust base.**  A-rated operator, graph-singularity,
martingale, and Hurwitz-zeta proofs are in
[`R94-LUROTH-FORWARD-CORRELATION-GATE.md`](results/R94-LUROTH-FORWARD-CORRELATION-GATE.md).

**Exact scope and nonclaim.**  Generic spectral-gap, time-reversal,
polynomial-observable, and depth-uniform positive-cone transfers are closed.
The coefficient-specific finite forward head remains open; no lower bound or
zero-free strip is inferred from the later-lag theorem.

### NG-39 — Global Luroth aliases are the functional equation, not a new sign

**Statement.**  The first-forward Luroth tail already has a nonzero linear-
cutoff symbol when `N asymp |t|`.  At the stationary aliases
`n asymp t/(2 pi k)`, its natural windows have leading coefficient
proportional to `k^(s-1)`.  Summing every branch with the required continuum
counterterm gives

```text
lim_(K->infinity)[sum_(k<=K)k^(s-1)-K^s/s]=zeta(1-s). (NG39.1)
```

The stationary Gaussian phase matches the gamma factor exactly.  Reapplying
Poisson summation multiplies by `chi(s)chi(1-s)=1`; it creates no residual
sector.  A finite polynomial change of the positive observable either keeps
the same alias or loses the zeta divisor.

**Evidence and trust base.**  A-rated finite-head, nonstationary-tail,
stationary-window, observable-rigidity, and global Poisson proofs are in
[`R95-LUROTH-RESONANT-HEAD-ALIASING-GATE.md`](results/R95-LUROTH-RESONANT-HEAD-ALIASING-GATE.md)
and
[`R96-LUROTH-GLOBAL-ALIAS-POISSON-GATE.md`](results/R96-LUROTH-GLOBAL-ALIAS-POISSON-GATE.md).

**Exact scope and nonclaim.**  Adjacent pairing, finitely many phase-locked
blocks, finite polynomial observables, and recursive Poisson renormalization
are closed.  Equation (NG39.1) is an exact rewrite, not a nonvanishing
estimate; a new global arithmetic relation among the complementary phases
remains outside the theorem.

### NG-40 — Flat scale cycles leave one faithful signed ramp

**Statement.**  Pole-normalized scale shifts form a commuting semigroup, so
their prime--pole defects are an exact flat cocycle.  Hermitian complex-flow
minimization projects away every circulation; deleting conjugation permits
nonzero sources with zero quadratic energy.  Finite pole-killing filters have
arbitrarily high recurrent blind frequencies.  The continuous exponential
delay avoids that last defect and has multiplier

```text
B_2(s)=(s-1)/(s+1),
R_2(log x)=sum_(n<=x)Lambda(n)(2n/x-1)-1+x^(-1).       (NG40.1)
```

It is uniformly faithful on the nontrivial zeta divisor.  By Landau's
one-sided theorem, either `R_2(log x)>=-C x^a` or
`R_2(log x)<=C x^a`, for one `a<1`, excludes every zero with real part
larger than `a`.  Complementary, lcm, convexity, scale-averaging, and
centered-Selberg identities do not prove either side; positive atomic
prime-like countermodels carry arbitrary off-line Mellin poles.

**Evidence and trust base.**  A-rated cocycle/Hodge/filter/Landau and exact
von Mangoldt identities are in
[`R95-SIGNED-MULTISCALE-QUEUE-CYCLE-GATE.md`](results/R95-SIGNED-MULTISCALE-QUEUE-CYCLE-GATE.md)
and
[`R96-ONE-SIDED-VON-MANGOLDT-RAMP-GATE.md`](results/R96-ONE-SIDED-VON-MANGOLDT-RAMP-GATE.md).

**Exact scope and nonclaim.**  The generic cycle, coercive-flow, finite-filter,
and positivity-only engines are closed.  The one-sided estimate for the
actual von Mangoldt coefficients is not disproved; proving it would establish
a fixed strip.

### NG-41 — Besicovitch recurrence selects the exceptional Euler ordering

**Statement.**  For every `sigma>1/2`, the Mobius series has exact diagonal
`B^2` recurrence because

```text
sum_n mu(n)^2n^(-2sigma)=zeta(2sigma)/zeta(4sigma).     (NG41.1)
```

Same-line point evaluation is nevertheless unbounded; Dirichlet `H^2`
recovers it only after a sharp half-unit right shift.  More specifically,
conditioning all primes `p<=P` to phase one gives

```text
A_P(sigma)H_P ->0             in conditional L2,
sum_(n<=P)mu(n)n^(-sigma) ->1/zeta(sigma)              (NG41.2)
```

under a hypothetical strip, for `1/2<sigma<1`.  Thus the conditioned tail
tends to `-1/zeta(sigma)`, exactly canceling the recurring natural head.
Inside every Rouche disc the same `A_P` has a width-`1/log P` boundary layer
whose local square mass grows exponentially.

**Evidence and trust base.**  The coefficient calculations and spike lemma
are A-rated; the Hardy-space and Carlson boundary are L-rated from the named
primary sources in
[`R96-MOBIUS-BESICOVITCH-RECURRENCE-GATE.md`](results/R96-MOBIUS-BESICOVITCH-RECURRENCE-GATE.md).

**Exact scope and nonclaim.**  Global mean recurrence cannot be promoted to
local recurrence at the Haar-null unit character by generic embedding or
ergodicity.  A coefficient-specific local-norm estimate along an exceptional
return sequence remains open and would prove the no-strip alternative.

### NG-42 — Puglisi's alternating cutoff inequality is reversed

**Statement.**  The claimed `quasi-RH => RH` proof in arXiv:2210.03121v9
uses, for even `J`, an alternating-exponential inequality that is false at

```text
x=13,                  J=30=2 floor(x+2).              (NG42.1)
```

An exact integer comparison shows the asserted nonpositive expression is
positive.  More generally, throughout the cutoff cell
`J=2m`, `m-2<=x<m-1`, its defect is bounded below by a quantity growing like
`exp(2m(1-log 2)+O(log m))`; the final Lagrange factor is not quantitatively
separated from one and can dominate the alternating tail.

**Evidence and trust base.**  The exact counterexample, uniform asymptotic
reversal, and audit of the surrounding Perron/Cauchy bookkeeping are A-rated
in
[`R95-PUGLISI-QUASI-RH-AUDIT.md`](results/R95-PUGLISI-QUASI-RH-AUDIT.md).

**Exact scope and nonclaim.**  This refutes the printed implication, not the
mathematical statement `quasi-RH => RH`.  A sign-definite integral remainder
or quantitative control of the Taylor point would be a different proof.

### NG-43 — Hilbert--Schmidt regularization deletes the first prime trace

**Statement.**  For the prime diagonal `D_s=diag_p(p^(-s))`, one has
`D_s in S_2` exactly for `Re(s)>1/2`.  In that half-plane
`det_2(I-D_s)` is holomorphic and nonzero.  The identity with `1/zeta(s)`
valid to the right of one additionally contains `exp(-Tr D_s)`; this omitted
first trace carries both the pole cancellation at one and the reciprocal
divisor.  The trace is nonclosable in `S_2`, while the natural Fock
augmentation is unbounded and `I-D_s` has index zero.

**Evidence and trust base.**  The Schatten identities, nonclosability
example, Fock-domain audit, and homotopy/index calculation are A-rated in
[`R97-FERMIONIC-FREDHOLM-TRACE-ANOMALY-GATE.md`](results/R97-FERMIONIC-FREDHOLM-TRACE-ANOMALY-GATE.md).

**Exact scope and nonclaim.**  This closes `S_2`-continuous regularized
determinants and the named Fock/index shortcuts.  It does not exclude a new
signed relative trace in a different topology.

### NG-44 — Low-threshold scalar Euler carriers cannot keep the divisor

**Statement.**  Removing the linear prime coefficient can lower a Dirichlet
square-sum threshold, but it also removes the simple reciprocal zero at one.
If a holomorphic scalar germ preserves that zero, its first nonconstant
Taylor layer supplies nonzero coefficients on every squarefree almost-prime
of the corresponding degree, retaining the half-unit barrier.  More
generally, if a Dirichlet carrier has square-sum threshold below `1/2` and
vanishes at one, Cauchy--Schwarz gives a fixed normal-convergence margin;
vertical recurrence then forces high artificial zeros with real parts
tending to one.

**Evidence and trust base.**  The coefficient formulas, threshold theorem,
recurrence corollary, and regression probes are A/D-rated in
[`R97-NONLINEAR-EULER-PRIME-ZETA-RIGIDITY-GATE.md`](results/R97-NONLINEAR-EULER-PRIME-ZETA-RIGIDITY-GATE.md).

**Exact scope and nonclaim.**  This is a rigidity theorem for scalar
Dirichlet/Euler carriers with normal convergence.  It is not a theorem about
all nonlinear or operator-valued realizations.

### NG-45 — Zero-preserving multiplicative twists are normal multipliers

**Statement.**  Let a unimodular completely multiplicative twist be chosen
so that its reciprocal Euler product retains a simple zero at one.  Landau's
positivity theorem forces a power-weighted pretentious distance to the
trivial twist to converge.  Cauchy--Schwarz upgrades this to normal
convergence of the Euler quotient in a left neighborhood of one.  The twist
therefore changes `1/zeta` only by a holomorphic nonzero multiplier and
inherits the same exceptional-character recurrence obstruction.

**Evidence and trust base.**  The Landau, pretentiousness, Euler quotient,
and sign-alignment calculations are A-rated in
[`R97-EXCEPTIONAL-MULTIPLICATIVE-TWIST-GATE.md`](results/R97-EXCEPTIONAL-MULTIPLICATIVE-TWIST-GATE.md).

**Exact scope and nonclaim.**  The result concerns unimodular completely
multiplicative twists.  It does not eliminate nonmultiplicative or genuinely
non-normal signed deformations.

### NG-46 — The imported quasi-RH bootstrap has identity exponent map

**Statement.**  Assume `Theta=sup_rho Re(rho)<1`.  The conditional PNT and
Mertens bounds have infimal power exponent exactly `Theta`; their Mellin
converses therefore return the same boundary.  Zero-density and mollified
moment estimates permit one sparse exception, Turan power sums contradict
only `beta>Theta`, reciprocal mollifier tails decay only to the right of
`Theta`, classical positivity remains anchored at `Re(s)>1`, and the
functional equation preserves the band.  Thus the audited imported toolbox
provides `f(Theta)=Theta`, not `f(Theta)<Theta`.

**Evidence and trust base.**  The conditional exponent ledger and the
primary-source audit are A+L-rated in
[`R98-QUASI-RH-BOOTSTRAP-GATE.md`](results/R98-QUASI-RH-BOOTSTRAP-GATE.md).

**Exact scope and nonclaim.**  This is not a proof that quasi-RH cannot imply
RH, nor evidence that `Theta=1`.  It closes only the explicitly audited
compositions and isolates the need for a new per-zero mechanism.

### NG-48 — Regular source words and bulk four-Cauchy covariance leave the contact charge

**Statement.**  For `A=I+K` and collar charge `Gamma`, the finite inverse-free
word `T_m=Gamma sum_(j<m)(-K)^j` satisfies
`Gamma=T_mA+Gamma(-K)^m`.  On `ker A`, its remainder is exactly `Gamma` at
every depth.  Regular scalar functions of `K` have the same contact residual.
A regular translation-invariant mean-periodic parametrix likewise has
residual multiplier one at every xi zero.  Independently, Suzuki's
logarithmic near-edge source has infinite Hankel rank, excluding a
finite-dimensional scalar boundary state, and the causal pole-killed ramp
contains a fixed initial collar.

R185 performs the exterior-source part of the resulting calculation.  The
fourth-root filter cancels exactly one decaying pole mode on each exterior
side, but leaves the opposite pole, an infinite every-fourth-moment tail, and
active prime samples.  These formulas hold for arbitrary smooth data and do
not use the old homogeneous equation.  Root rotations and positive dilations
commute before localization.
Reflection has the semidirect law `J S_r=S_(1/r)J` and merely swaps the two
channels of the reflection-invariant paired prime source.  Fixed-window/cut/
trace compression adds an explicit two-boundary leakage cocycle, but that
cocycle is only one channel of the total completed readout.  The old Lerch
operator is a split finite-part/Carleman operator.  R186 subsequently gives an
exact counterterm-free serialization, assembles the weak/L2 global state, and
shows that generic endpoint jets cannot be passed by form-core density.
Global exterior solution-independence remains exactly `Gamma ker(A)=0`.

**Survivor.**  A precise zeta-specific continuum recurrence,
quasianalyticity, unique continuation, or spectral-synthesis theorem could force the total
readout to vanish.  That would be new input, not a consequence of bulk
rotation/dilation algebra.

**Evidence and trust base.**  Finite identities are kernel-checked in
`CompletedSourceConstructiveSearch.lean` and
`CompactSourceDerivativeBridge.lean` and
`FourCauchyGlobalCompatibility.lean` and
`SplitCarlemanFormDomainCloseout.lean`; exact rational/Gaussian-rational
fixtures and the scoped analytic derivations are recorded in
[`ZETA23-CONSTRUCTIVE-COMPLETED-SOURCE-AND-COMPACT-DERIVATIVE-AUDIT-2026-09-03.md`](results/ZETA23-CONSTRUCTIVE-COMPLETED-SOURCE-AND-COMPACT-DERIVATIVE-AUDIT-2026-09-03.md)
and
[`ZETA23-FOUR-CAUCHY-GLOBAL-COMPATIBILITY-CALCULATION-2026-09-03.md`](results/ZETA23-FOUR-CAUCHY-GLOBAL-COMPATIBILITY-CALCULATION-2026-09-03.md).
The final topology and falsifier audit is
[`ZETA23-SPLIT-CARLEMAN-FORM-DOMAIN-CLOSEOUT-2026-09-03.md`](results/ZETA23-SPLIT-CARLEMAN-FORM-DOMAIN-CLOSEOUT-2026-09-03.md).

**Exact scope and nonclaim.**  NG-48 does not exclude continuum integral
operators, distributed-memory systems, range-specific nontranslation-
invariant parametrices, variable-coefficient source-specific propagation, or
ambiently convergent infinite synthesis with independent closure.  The
exact charged contact shows only that the finite split-Cauchy/dilation grammar
does not force exterior null charge; its coefficients are synthetic and it is
not the actual Suzuki/von-Mangoldt operator.  NG-48 excludes only the
listed regular and coefficient-free constructions; it
does not close orientation-sensitive four-Cauchy compatibility.  It proves
neither KNC, a strip, the four-cycle bound, nor RH.

## 4. Supporting countermodels, not headline no-go theorems

These artifacts are useful because they prevent invalid logical shortcuts.
They should not be advertised as independent progress on RH.

| Artifact | Exact lesson | Evidence boundary |
|---|---|---|
| [`Stage3BoundaryNoGo.lean`](lean/rhbridge/RHBridge/Stage3BoundaryNoGo.lean) | A quantitative collar-size lower bound alone does not exclude a new radical direction | F-rated two-dimensional countermodel only |
| [`Stage3ParityNoGo.lean`](lean/rhbridge/RHBridge/Stage3ParityNoGo.lean) | Simplicity of a ground state and reflection symmetry do not force the state into the even sector | F-rated two-dimensional countermodel only |
| [`LEE-YANG-INVERSE-CONE-FINAL-2026-08.md`](results/LEE-YANG-INVERSE-CONE-FINAL-2026-08.md) | A finite model-free moment cone can hold while the stronger independent-spin cone fails | C/D finite statement; no infinite Lee--Yang theorem |
| [`MOBIUS-RESIDUE-TO-DENSITY-FINAL-2026-08.md`](results/MOBIUS-RESIDUE-TO-DENSITY-FINAL-2026-08.md) | Large every-scale partial sums do not imply pretentiousness for general bounded multiplicative functions; the exact Möbius parameter is singular | A+L counterexample to a generic inverse gate, not to every Möbius-specific inverse theorem |
| [`CYCLOTOMIC-TWO-PRIME-TRACE-FINAL-2026-08.md`](results/CYCLOTOMIC-TWO-PRIME-TRACE-FINAL-2026-08.md) | Pure Euler coefficients with no mixed coefficient do not make a finite positive global trace | Exact finite algebra; infinite geometric realizations remain open |
| [`TWO-WAVE-ORTHOGONAL-FAIL-FAST-2026-08.md`](results/TWO-WAVE-ORTHOGONAL-FAIL-FAST-2026-08.md) | Ten proposed mechanisms were reduced to explicit gates or counterexamples | Research ledger; each row inherits only the evidence of its linked proof |

The complete branch registry is
[`results/REDUCTION-REGISTRY.md`](results/REDUCTION-REGISTRY.md).  A registry
entry is not promoted merely by appearing there.  Its canonical logical
classification and nearest RH proxy are recorded in
[`results/RH-PROXY-LEDGER.md`](results/RH-PROXY-LEDGER.md).

## 5. The common theorem behind the failures

The results point to a recurring structural obstruction, not a universal
meta-theorem:

```text
one off-line zero
      |
      v
global coherent phase --------- visible to continuation/divisor topology
      |
      +---- locally square-summable or zero-density
      |             |
      |             +---- erased by mean, mass, or fixed-resolution topology
      |
      +---- requires all places and infinity
                    |
                    +---- broken by fixed-place or termwise positive assembly
```

The precise reusable lesson is a design test.  A proposed RH mechanism must
name:

1. the object changed by one off-line zero;
2. the topology in which that change has nonvanishing size;
3. the all-place completion native to that topology;
4. an independent order, contraction, or exclusion theorem;
5. a closed global limit in the same topology.

NG-01 and NG-02 attack items 1--2; NG-03 through NG-08, NG-11, NG-12,
NG-16 through NG-48 attack
attempts to manufacture item 4 locally; NG-09 and NG-10 show how locality and
averaging can lose items 2--3; NG-13 through NG-15 isolate quantifier,
topology, target-identification, and boundary-escape failures in the
completion step.  This synthesis guides candidate selection.
It is not, by itself, a proof that every future route must fail.

## 6. Current proof-debt ledger

| ID | State | Required action before publication as a headline result |
|---|---|---|
| NG-01 | Amber | Typeset the compact-open lemma independently of the phase narrative; obtain a referee check of the exact detector corollary |
| NG-02 | Amber | Formalize or independently referee the `B^2` norm identities and Kronecker nonuniformity; freeze the two model definitions |
| NG-03 | Amber | Write a standalone theorem with the test-function scaling and domination details; independent normalization audit |
| NG-04 | Green for the abstract cost; Red for the zeta application | The focused audit passes; prove or interval-certify a negative residual witness before claiming the full local-edge class is eliminated |
| NG-05 | Green as a supporting lemma | Keep it subordinate; it is elementary and does not establish positivity of any completed form |
| NG-06 | Green as a bounded supporting lemma; Red for the continuum instantiation | Construct the densely defined closed/closable operator, fix its domain and metric, and prove the exactly normalized form identity before invoking the lemma |
| NG-07 | Green for logical insufficiency | Do not transfer the countermodel's bad sign to the zeta kernel; the zeta-specific estimate remains open |
| NG-08 | Green for the rational block; Amber for the general characterization/application | Add a primary-source comparison and, if used centrally, formalize the general Hermitian statement |
| NG-09 | Amber | Independent proof review, prior-art comparison, and a clean standalone manuscript proof |
| NG-10 | Amber | Independent audit of the conditional-law convention and every zero-density normalization; state literature inputs verbatim |
| NG-11 | Green for the finite algebra; Amber for the completed smooth-core application | Independently audit the operator/core hypotheses, differentiation under the kernel integral, dilation normalization, finite-frequency trigamma bound, Kronecker step, and boundary-compatible packet asymptotics; do not promote the floating prime-5 scout to evidence for an infinite statement |
| NG-12 | Green for the abstract Riesz repair and Dirichlet pointwise counterexample; Red for exact zeta shift dependence | Obtain independent review of the form-core and distributional application; any transfer of the Galerkin selected-root failure requires graph/resolvent convergence, while exact full-family covariance would require a separate zeta calculation |
| NG-13 | Green for the scalar floor/coherence theorems; Amber for the analytic kernel identity, Hermite--Biehler family, and Suzuki application | Independently review the raw-versus-de-Branges normalization, infinite-product convergence, exact type, Clark factor, Cartwright criterion, and endpoint support; do not infer strong-resolvent failure from unweighted count divergence |
| NG-14 | Green for the scalar normalization/shift algebra; Amber for the global Fourier-completion statement | Independently review density of the Fourier core in the mixed atomic/Lebesgue space and the varying-space resolvent convention; NG-15 settles natural named-vector compatibility negatively, but do not infer failure of every noncanonical quotient or of an asymptotic unshifted construction |
| NG-15 | Green for the scalar projection algebra; Amber for the analytic application | Independently referee the Riesz projection identity, translation convention, group-mollifier graph-core proof, and generalized functional calculus; keep the RH assumption explicit and do not promote Galerkin norm rows to continuum evidence |
| NG-16 | Green for the abstract floor theorem; Amber for the zeta analytic synthesis and quantitative rate | Independently referee the mollifier-to-screw calculation, every transform sign and factor, the BRS vertical-strip extraction, cutoff sampling estimate, and form-core passage; present the results as an RH-equivalent quantifier audit plus a conditional false-world rate, not as a proof of RH |
| NG-17 | Amber | Independently check the pole/main normalization, Stieltjes boundary terms, zero-strip-to-prime-error input, and modulation countertest; state only the failure of this estimate architecture, not failure of the reverse rate |
| NG-18 | Amber | Independently referee quantile-divisor sampling, `O(1)` count preservation, tail absorption for every fixed support, boundary-bump asymptotics, and the translation-bounded second-moment theorem; do not transfer the synthetic divisor's superexponential floors to zeta |
| NG-19 | Green for the interval signs; Amber for the infinite operator exposition | Re-run the one-thread Arb script and independently check the rank-one determinant, compression indexing, Routh count, and Edrei--Schoenberg specialization; do not infer anything about the limiting spectrum from Taylor-section failures |
| NG-20 | Green for the exact scalar algebra and recurrence; Amber for the analytic synthesis | Independently audit the screw-preprint sign discrepancy, Fourier normalization, strict-gap implication, and use of the quantitative floor theorem; do not promote sampled subleading minima to a global bound |
| NG-21 | Green for the finite/rational scalar algebra; Amber for the analytic cone exposition | Independently referee the continuous operator-domain spelling and the global sinc inequality; keep the conclusion to failure of the generic packet lift, not failure of any zeta-specific mixed-packet theorem |
| NG-22 | Green for the completion/polarization algebra; Amber for the Toeplitz and regulated-boundary synthesis; finite arithmetic runs D | Independently referee the Fourier normalization and the two-sided `xi'/xi` regulator calculation. Keep the conclusion to failure of an identity/sign derived from the named ingredients; do not promote the floating B-spline models to exclusion of a large-scale zeta-specific two-shift estimate |
| NG-23 | Green for the finite-cutoff/Laurent and Riccati algebra; finite arithmetic runs D; full-field Vinogradov--Korobov synthesis and classical Euler transfer internally audited A+L | Do not promote the quadratic-core null direction to a solution of the full Riccati equation.  The `R^(4/5-o(1))` bound is now a theorem for both the cutoff-independent exact-head and frozen explicit-center fields.  A converse for that single sublinear schedule remains open, but the program-level moving-edge need is discharged by R80's proportional bank.  The global fixed-power joint-dispersion theorem remains open. |
| NG-24 | Green for the annihilator algebra and exact finite comparator formulas; completed finite runs D | Independently check the Fourier convention, inverse-shift convergence, and localization commutator.  Treat the finite ratios only as counterexamples to the tested domination inequalities, not as an asymptotic lower bound or a rejection of Mobius-specific cancellation |
| NG-25 | Green for the local-moment exponent and Bernstein--Walsh filter arguments; completed pair-cell runs D | Independently check the continuously translated block quantifier, Fourier-duality constants, noncancellation of the selected zero pole, and scale-span arithmetic cost.  Treat finite cell signs only as failures of the sampled domination/monotonicity claims; the fixed-saving endpoint remains open |
| NG-26 | Green for the independently audited attained-edge Bohr theorem; Amber for the non-attained quartet construction; clustered run D | Independently referee the Fourier-`l1` discretization and nested-interval tail control.  Do not transfer the abstract countermodel to zeta without Riemann--von Mangoldt local counting and the prescribed zero coefficients. |
| NG-27 | Amber for the analytic sector recompletion and spectral comparison; Green for the finite triangular/frame algebra; finite optimizers D | Independently audit the common-factor primitive mask, natural rectangular limits, normalized shell bounds, and every Kuznetsov normalization.  The beat frame is a coordinate theorem, not cancellation; do not describe the surviving centered joint estimate as weaker than a fixed strip. |
| NG-28 | Amber for the Wright/kernel interface and contact-family normalization; Green for the global frame, reciprocity, Vandermonde, and powered-box algebra; finite tensor/gauge runs D | Independently referee the log-Mellin projective bound, `k=j theta` norm ledger, exact placement/sign of both phases, and uniform B-spline seam estimates.  Do not infer a zeta asymptotic from the envelope probes or claim that one scalar contact is gauge-invariant. |
| NG-29 | Green for the Ramanujan, Ward, null-gauge, and disjoint-support algebra; Amber for the complete R71 normalization; Wright interface L and finite falsifiers D | Independently check the Fourier signs in reciprocal derivative transfer, the `1/mu` norm charge, top-prime versus square-root scale conventions, and all primitive axes/seams.  State the `H^(-1/40)` power only for the conditional mean-zero component, never for the full energy. |
| NG-30 | Green for the finite shifted-Ramanujan, compression, zero-orbit, averaging, and prime-point algebra; Amber for the complete R71 kernel identification; spectral imports L and compression runs D | Independently referee the reciprocal phase orientation, `S^(-1)` normalization, prime-window PNT comparison, and flat-versus-actual shift-weight distinction.  Do not promote the blockwise norm lower bound to a lower bound for the complete signed energy; the all-sector kernel pairing remains open. |
| NG-31 | Amber for the all-sector normalization; Green-candidate for the finite CRT/Poisson and spline algebra | Independently referee the rectangular-limit interchange, primitive-mask shifts, both punctured-axis orientations, Type-I normalization, B-spline seam integration, and the growing Gamma-band constants. Do not infer a lower bound for the signed full energy from response separation. |
| NG-32 | Amber | Independently audit every explicit-formula sign, the target/pole optimization, the Turan order hypothesis, the infinite harmonic-block countermodel, and the imported density exponent. Keep the conclusion to failure of positivity-plus-density, not failure of a zeta-specific conditional correlation. |
| NG-33 | Amber | Independently referee the collar-flux transfer, squarefree smooth-number density with odd restriction, fixed-arity quantifiers, and fractional Hall equivalence. Do not infer that the isolated smooth sector has a large signed sum. |
| NG-34 | Green-candidate for the elementary Euler/Mellin identities; Amber for the general half-plane transfer | Independently check q-uniform constants, Newton-series normal convergence, depoissonization, ordinary integrability at the Muntz endpoint, and weighted-dilation convergence. State the fixed Newton power as an equivalent/sufficient target, not an achieved estimate. |
| NG-35 | Amber; prime-gap exponent L | Independently referee the differentiated explicit formula for arbitrary polynomial weights, the global prime-log mesh deduction, weighted variation bounds, stable Markov/Remez hypotheses, and all tail normalizations. Arbitrary superoscillation remains open and must retain its full condition number. |
| NG-36 | Green-candidate for the finite Kronecker identity; Amber for the strip/normal-family synthesis | Independently check the squarefree-density endpoint at `sigma=1`, the reciprocal zero count on the Rouche disc, and every quantifier in the diagonal-return/Montel argument. Do not describe forced tail anti-recurrence as evidence that the strip is false. |
| NG-37 | Amber | Independently referee endpoint mass equalization, the radial pushforward orientation, the fixed-power PNT equivalence, and Hall collar capacities. Keep the signed multiscale queue explicitly outside the positive-transport theorem. |
| NG-38 | Amber | Independently check the Luroth branch convention, exact contraction constant, mutual-singularity graph argument, uniform Hurwitz expansion, and martingale conditioning. Do not transfer later-lag nonvanishing backward through the noninjective Perron operator. |
| NG-39 | Amber | Independently referee the linear-cutoff Euler--Maclaurin remainder, stationary-window constants, overlap counterterm, gamma phase, and polynomial-observable rigidity. Treat the final `zeta(1-s)` identity as recombination, not a bound. |
| NG-40 | Amber | Independently check the normalized-shift convention, continuous-delay Stieltjes calculation, Landau abscissa argument, lcm exponents, and positive atomic countermodel. Never report the one-sided ramp criterion as an achieved estimate. |
| NG-41 | Amber; Hardy/Carlson boundary L | Independently audit the order of the natural, Euler, prime-dimension, and vertical-mean limits; the conditional `L2` normalization; and the uniform constants in the boundary-layer spike. Do not identify a Bohr equivalence class with its value at the unit character. |
| NG-42 | Green-candidate for the exact counterexample; Amber for the full preprint audit | Recheck the v9 source, indexing convention, integer comparison, and uniform cutoff-cell asymptotic. State only that the printed proof fails; do not infer that quasi-RH fails to imply RH. |
| NG-43 | Green-candidate for the operator algebra; Amber for the analytic synthesis | Independently audit the prime-diagonal Schatten thresholds, regularized determinant convention, Fock augmentation domain, trace nonclosability example, and index/homotopy statement. Do not infer that every relative trace is impossible. |
| NG-44 | Green-candidate | Independently check the squarefree almost-prime coefficient formula, the general normal-margin quantifiers, and the recurrence theorem's nonvanishing-log hypothesis. Keep finite vanishing Euler factors explicitly excluded. |
| NG-45 | Amber | Independently referee the Landau abscissa step, weighted pretentiousness exponents, Euler-quotient normal convergence, and the sign-alignment transfer. State the unimodular complete-multiplicativity hypotheses prominently. |
| NG-46 | Amber; literature inputs L | Independently verify every conditional endpoint epsilon, current density exponent/range, mollifier-tail domain, and the sparse symmetric profile. State only that the audited bootstrap map is the identity. |
| NG-47 | Green for finite Lean algebra and exact models; Douglas/Suzuki inputs L; analytic zeta synthesis Amber | Independently referee the bounded form-space typing, closed-range step, dense-core closability proof, and backward conditional dichotomy. Do not promote the abstract models to a completed-zeta counterexample or claim that failure to specify `T^src` disproves KNC. |
| NG-48 | Green for finite Lean algebra and exact rational/Gaussian-rational fixtures; Suzuki/Carleman/Kronecker/Landau inputs L; global source synthesis Amber | Independently referee the R186 form-core and finite-collar boundedness arguments. Treat serialization as a normal form, not a completed factor; do not use generic endpoint jets or promote the exact synthetic charged model to actual-zeta KNC. |

“Green” here certifies only the exact card component named in the state
column.  It is not a novelty or importance grade.

## 7. Focused reproduction and memory warning

The formal obstruction audits can be checked individually without replaying
the generated certificate corpus.  They should still be run serially.  Before
import minimization, several cold individual Lean processes peaked above 6 GB
RSS.  After replacing the five broad `Mathlib` imports in this layer, the
remeasured audits peaked at roughly 1.5--2.4 GB; the other focused no-go audits
were previously in the 2.3--2.7 GB range.  These commands are lower-risk than
an umbrella build, not tiny-memory:

```text
cd lean/rhbridge
lake env lean RHBridge/PrimeEdgePolarizationAudit.lean
lake env lean RHBridge/GlobalMobiusCancellationAudit.lean
lake env lean RHBridge/CompletedIncidenceComplexNoGoAudit.lean
lake env lean RHBridge/HodgeLowSectorNoGoAudit.lean
lake env lean RHBridge/FinitePolarizationNoGoAudit.lean
lake env lean RHBridge/QuantizedPhaseIndexNoGoAudit.lean
lake env lean RHBridge/Stage3BoundaryNoGoAudit.lean
lake env lean RHBridge/Stage3ParityNoGoAudit.lean
lake env lean RHBridge/VirialCommutatorNoGoAudit.lean
lake env lean RHBridge/GelfandTripleAdjointAudit.lean
lake env lean RHBridge/FormDomainVirialAudit.lean
lake env lean RHBridge/ProjectiveGramInvariantAudit.lean
lake env lean RHBridge/NestedShiftRigidityAudit.lean
lake env lean RHBridge/CofinalShiftPositivityAudit.lean
lake env lean RHBridge/SemiboundedFloorDichotomyAudit.lean
lake env lean RHBridge/BoundaryPhaseCountingAudit.lean
lake env lean RHBridge/BoundaryPhaseCoherenceAudit.lean
lake env lean RHBridge/ClarkSpectralWeightAudit.lean
lake env lean RHBridge/RieszKernelEscapeAudit.lean
lake env lean RHBridge/SelbergPacketConeNoGoAudit.lean
```

These commands check only the named Lean statements.  They do not validate
the A- or L-rated arguments in the reports.  Those require conventional
referee review under the proof standard.  A fresh clean-checkout measurement
remains a release task.  The present working-tree artifacts must also be
committed before any clean-checkout reproduction claim is made.
