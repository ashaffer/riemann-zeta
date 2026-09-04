# Hostile audit: Yang--Yang's claimed 79.62% zero-density result

**Date:** 2026-08-31  
**Scope:** Zenodo record [10.5281/zenodo.21975237](https://zenodo.org/records/21975237), repository commit [`d85bddf`](https://github.com/JoshuaHKU/zeta-0.7947-reproduction/tree/d85bddfe9d8f12856fba735fc9cb3ca23b48b3a8), and the comparison with Alpöge--Furman §7.2  
**Source policy:** primary paper, source repository, and Alpöge--Furman's primary preprint only

## Verdict

The preprint does **not presently establish** that 79.62% of the zeros are
simple and on the critical line.  This is a verdict on the supplied proof,
not a refutation of the numerical density statement.

The first fatal edge is Proposition 5.3, the truncation that is supposed to
replace all prime-power moduli by

```text
b_1,b_2 <= (log X)^B.
```

The proof assigns a cellwise factor `ell^(-k)`, but the paper has already
defined `ell_1 = log(T/2pi)+2log 2-1` as one global normalization.  The
shipped fourth-moment ledger instead has modulus weight

```text
Lambda(b_1)Lambda(b_2)/(b_1 b_2),
```

with the global `ell_1^4` normalization applied only after summation.  Hence
there is no displayed `ell^(-k)` tail in the modulus.  Mertens' formula gives

```text
S(P) = sum_{b<=P, b a prime power} Lambda(b)/b = log P + O(1),

S((log X)^B)^2 / S(X)^2
    = (B loglog X / log X)^2 + o(1)
    -> 0.
```

Thus the polylogarithmic-modulus cells carry a vanishing raw share, whereas
Proposition 5.3 needs them to carry all but an arbitrarily small log-power
tail.  This exact objection is now recorded as the still-open
[repository issue #1](https://github.com/JoshuaHKU/zeta-0.7947-reproduction/issues/1),
with no author response as of this audit.  I independently reproduced its
Mertens-weight table at `X=10^4` and `10^6`.

The paper itself says that its unrestricted fourth-moment assertion, with
moduli up to a power of `X`, remains open.  Once Proposition 5.3 is removed,
that unrestricted assertion is precisely what is needed.  Consequently

```text
Proposition 5.3 fails as written
  => truncated Lemma D does not imply the full fourth moment
  => m_4 = 13/4 is unproved
  => the 13/18 rung is unproved
  => the k=5,6 transports and the 0.7962/0.8981 headline lose their input.
```

## What reproduces, and what it proves

The repository is a real and useful conditional-certificate artifact.  It is
not an end-to-end reproduction of the analytic theorem.

| Check at commit `d85bddf` | Result | Licensed conclusion |
|---|---:|---|
| Zenodo English PDF versus repository `paper.pdf` | identical MD5 `0811e74faaffe8ef7b216cc004481eb5` | the audited source matches the deposited paper |
| `certification/certify_lp.py` | `1-2w_0 = 0.7962709657...`, `1-w_0 = 0.8981354828...` in exact rational arithmetic | the degree-six moment certificate is valid **if** its asserted moments are supplied |
| `pipeline/run_all.py` | `ALL GATES PASS` in 73 s | finite identities and calibration faces pass; no asymptotic theorem follows |
| `lake build` in `lean/RhGate` | clean build, 6 jobs | four files prove rational identities and finite residue enumerations |
| cited analytic archives | `V1_completion.md`, D1, bridge/glue/consumer memos, and rounds r93/r95/r100/r102 absent | the deferred analytic steps cannot be reproduced from the public package |

The Lean scope is especially important.  [`Certificate.lean`](https://github.com/JoshuaHKU/zeta-0.7947-reproduction/blob/d85bddfe9d8f12856fba735fc9cb3ca23b48b3a8/lean/RhGate/Certificate.lean)
contains no zeta function, prime sum, measure, limit, trace-moment theorem, or
Lemma D.  Its declarations establish polynomial identities, rational
inequalities, and the arithmetic implication

```text
claimed moments -> 0.7962 / 0.8981.
```

That is legitimate kernel checking, but it does not kernel-check the claimed
moments or the analytic bridge to zeros.

There is also reproducibility drift.  The finite LP face still asserts the
older `0.79472/0.89736` constants and therefore passes while testing a number
different from the deposited headline; this is documented in open
[issue #2](https://github.com/JoshuaHKU/zeta-0.7947-reproduction/issues/2).
It is a packaging defect, not the fatal analytic defect.

## Exact analytic status ledger

| Item | Status after audit | Reason |
|---|---|---|
| Main 0.7962/0.8981 claim | **unsupported preprint claim** | depends on unproved moments `m_4,m_5,m_6` |
| Exact Chebyshev--Markov certificate | **reproduced conditional theorem** | exact rational calculation; hypotheses are the moment values |
| Connected model constants | **exact finite/model arithmetic is plausible and archived** | their identification does not prove that zeta's trace moments equal the model moments |
| Lemma 5.1, cell-mass bound | **not established** | short sketch uses an undefined/conflicted cell parameter and supplies no modulus decay |
| Lemma 5.2, multiplicity | **asserted without proof** | the paper gives no definition adequate to derive the claimed divisor bound |
| Proposition 5.3, truncation--consumption | **refuted as written** | global normalization is mistaken for cellwise decay; actual ledger has Mertens mass at large moduli |
| Lemma 7.2, minor/mixed leaves | **write-out claim, not a proof** | the required hybrid large-sieve aggregation is summarized rather than derived |
| Theorem 7.5, Lemma D | **open in the required unrestricted range** | the paper proves only a claimed log-modulus version and explicitly calls the power-range version open |
| W1 and W3; `k=5,6` transports | **unproved** | they reuse Lemma D factorwise and say the higher-dimensional argument repeats verbatim |
| `mu_3=2` | **not fully public-reproducible** | two nonstandard steps are deferred to the absent `V1_completion.md` |
| Independent one-sided `0.6916` route | **not resolved by this audit** | it does not use Proposition 5.3, but it has its own archived/candidate analytic and numerical inputs |

The authors themselves label the analytic layer “certified-candidate,
pre-Lean, pre-review.”  The stronger conclusion here comes from locating a
specific false bridge, rather than merely downgrading the work because it is
unreviewed.

## Does `k=4` escape the Alpöge--Furman barrier?

No.  It removes the hard range by the invalid truncation.

Alpöge--Furman [§7.2](https://arxiv.org/html/2608.13637#S7.SS2)
state that at `X ~ T` the fourth Gabor trace encodes

```text
sum_m (Lambda * Lambda)(m) (Lambda * Lambda)(m+h),
|h| <= X^2/T,
```

a Hardy--Littlewood-type additive correlation, and name the corresponding
higher-trace input `HL*(4)`.  Yang--Yang's class `R` is the same arithmetic
phenomenon reorganized as correlations of restricted products
`b_1 m_1` and `b_2 m_2`.  Their Theorem 7.5 handles only
`b_1,b_2 <= (log X)^B` by Siegel--Walfisz/Vaughan, while the preprint itself
admits that the power-modulus version is open.  Since the omitted large
moduli carry the mass, the paper has not proved `HL*(4)` or bypassed it.

This is also why the Parseval and product identities, though exact, do not
solve the problem.  They re-express the global fourth moment; they do not
make its large-conductor mass disappear.

## Passport comparison with project CA4

| Field | Alpöge--Furman `HL*(4)` | Yang--Yang claimed Lemma D | Project CA4 |
|---|---|---|---|
| arithmetic mask | natural von Mangoldt convolution | natural prime-power/restricted-product weights | adjacent-consecutive-prime gap weights |
| localization | global Gabor trace | lock/cell aggregation | one shell and translated bandpass kernel |
| shift scale | `|h| <= X^2/T` | equivalent locked-product resolution | `H=Y^2/T` |
| coefficient structure | natural `Lambda*Lambda` | `Lambda^4` cell weights | signed/weighted hat coefficients |
| status | explicit conditional barrier | required unrestricted form open | open |

The shared physical resolution `X^2/T` (respectively `Y^2/T`) confirms that
CA4 is aimed at the genuine higher-trace correlation scale.  But the masks do
not match: even a valid natural-weight `HL*(4)` theorem would need a
quantitative adjacent-gap-mask transference theorem before it could enter
CA4.  Nothing in the Yang--Yang artifact supplies that adapter.

## Reframe for this project

1. **Import the conditional certificate, not the density theorem.**  The
   exact moment-to-density algebra is a reusable Weil-side interface.  It has
   no direct implication for a uniform zero-free strip, and a density-one
   statement would still tolerate `o(N)` off-line zeros.
2. **Do not import Lemma D.**  Its first bridge is broken, so it contributes
   no theorem to CA4, `DPA_P`, `LTRAD_P`, a uniform strip, or RH.
3. **Promote conductor-mass accounting to a preflight gate.**  Before using
   an easy small-modulus theorem, compute the exact share of the target norm
   carried by that range.  A fixed polylogarithmic cutoff is asymptotically
   negligible here.
4. **Retain CA4's current diagnosis.**  The first four-distinct
   balanced-semiprime covariance is not bookkeeping left over after
   Parseval; it is the weighted, localized analogue of the same
   Hardy--Littlewood higher-trace wall.
5. **The useful next comparison is an adapter falsifier.**  Ask whether the
   adjacent-gap-weighted CA4 form can be decomposed into a controlled finite
   combination of natural `Lambda*Lambda` correlations while retaining the
   shell, translated kernel, sign, and `Y^{-0.1}` gain.  Failure on any mask
   field blocks the import even if natural `HL*(4)` later becomes available.

## Theorem passport for any attempted repair

```text
Target: unrestricted fourth Gabor trace / CA4-scale covariance.
Mask: exact Lambda*Lambda for the Gabor theorem; exact adjacent-gap mask for CA4.
Range: all conductor/modulus cells carrying 1-o(1) of the normalized mass.
Resolution: |h| <= X^2/T (or H=Y^2/T).
Quantifiers: uniform through the full dyadic trace aggregation.
Rate: o(1) for the trace theorem; the recorded CA4 power gain for the project socket.
Nonvacuity: an explicit mass ledger showing the retained range is 1-o(1).
Stop rule: reject every truncation whose retained weighted mass tends to zero.
```

**Bottom line:** the artifact contains valid exact identities and a useful
conditional moment-consumption certificate.  Its claimed new analytic
mathematics is exactly the part that fails.  The literature therefore
reframes, rather than closes, our work: CA4 remains a genuine masked
higher-trace Hardy--Littlewood problem, and small-conductor serialization is
not an escape hatch.
