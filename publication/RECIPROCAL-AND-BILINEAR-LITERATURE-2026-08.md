# Reciprocal-phase, bilinear, and signed-dispersion literature at the R87 gate

Status: primary-source applicability audit, current through 2026-08-07.
Preprints are identified by version and date.  This is an import matrix, not
a claim that the literature search proves an exhaustive nonexistence theorem.

## 1. Verdict and the exact gate

No source checked below proves a fixed zero-free strip for the Riemann zeta
function, and no source proves that such a strip does not exist.  In
particular, no 2025--2026 result crosses the complete, every-block,
fixed-power R71 threshold.

R87 sharpens the reason.  With

```text
nu=sum_n Lambda(n)delta_n-dt,
E_L(nu)=double_integral L(t,u)dnu(t)conjugate(dnu(u)),
```

its exact sector-conservation identity is

```text
H_off+H_(theta=0)+H_(j=0)+H_axes=E_L(nu).             (1.1)
```

The project-side derivation is
[`FULL-R71-RECIPROCAL-RESPONSE-GATE.md`](../results/FULL-R71-RECIPROCAL-RESPONSE-GATE.md).

The canonical slow response is the centered punctured axis `-P_1-P_2`, and
the only automatic cross-sector cancellation removes the singular-series
background introduced by the sector split.  Thus an external theorem passes
the R87 gate only if it retains, before absolute values,

1. the varying reciprocal modulus and balanced square-root factors;
2. the coupled B-spline amplitude, common-`g` masks, axes, seams, and Type-I
   correction;
3. the canonical prime-minus-continuum contact in (1.1); and
4. a fixed power uniformly on every carrier block as the detector slope
   tends to zero.

The matrix distinguishes a power saving for a source's native sum from a
power saving for (1.1).

## 2. Primary-source applicability matrix

| Source and current version | Exact theorem and regime | Native saving | R71 mismatch | R87 contact verdict |
|---|---|---|---|---|
| [Wright, *Trilinear Kloosterman fractions I*](https://arxiv.org/abs/2604.25177), v1, 2026-04-28, Theorem 2.1 | For `M << N^2`, `R << M^C`, and nonzero integer phase `vartheta`, the fixed-factor trilinear form `B(M,N,A;R)` is at most `M^eps norm(alpha)norm(beta)norm(nu)(AMN)^(1/2)R^(1/4)(1+abs(vartheta)A/(MN))^(1/4)` times `N^(-1/8)+R^(1/8)N^(1/8)M^(-1/4)+M^(1/10)/(R^(3/20)A^(1/20)N^(3/20))+N^(3/20)/(A^(3/20)M^(1/5))+N^(3/8)M^(-1/2)`. | With `M=N=x^(1/2+o(1))` and `A,R=x^o(1)`, the worst term is `x^(-1/40+o(1))`. | This is the closest native theorem to the R81 nonzero reciprocal phase.  It does not include `theta=0`, `j=0`, punctured axes, the conditional cofactor limit, or the full coupled R71 kernel ledger.  Corollary 2.2 is an unbalanced, modulus-averaged logarithmic theorem, not the balanced completed estimate. | The theorem controls an off-axis representation.  R87 identifies the omitted slow term as the actual centered axis, not a removable zero mode.  Wright therefore remains an imported lemma for a nonzero sector only. |
| [Drappeau, *Sums of Kloosterman sums in arithmetic progressions*](https://arxiv.org/abs/1504.05549), v4, 2016-12-11; PLMS 2017, Theorem 5.1 | Put `x=MN`, `x^(1/4)<=Q`, `x^eta<=N<=Q^(2/3-eta)`, `Q<=x^(1/2+delta)`, and `R,abs(a_1),abs(a_2)<=x^delta`.  For divisor-bounded coefficients, the signed discrepancy with `u_R(n;q)=1_(n=1 mod q)-phi(q)^(-1) sum_(cond chi<=R) chi(n)` is `<< x(log x)^O(1)R^(-1)`. | Choosing a power-sized `R` gives a native fixed power in its allowed unbalanced range. | At the R71 square-root point `M=N=x^(1/2+o(1))`, `Q=x^(1/2+o(1))`, the condition would require `x^(1/2)<=x^(1/3-o(1))`.  Moreover, the retained projector is onto low-conductor characters, not the finite canonical `Lambda-1` contact. | It is a genuine signed theorem, but its signed main term is the wrong object.  R87 makes the missing term explicit as `-P_1-P_2` inside (1.1). |
| [Fouvry--Radziwill, *Level of distribution of unbalanced convolutions*](https://arxiv.org/abs/1811.08672), v1, 2018-11-21, and Wright Corollary 2.2 above | An essentially arbitrary long sequence convolved with a tiny Siegel--Walfisz sequence has weak level of distribution `x^(1/2+1/66-eps)`.  Wright's updated ranges include `N<=Q^(-33/28)X^(17/28-eps)`, or `N<=X^(7/90-eps)` / `X^(101/630-eps)` under the stated bounds on `Q` and `a`. | Logarithmic distributional saving beyond `1/2` for strongly unbalanced convolutions. | R71 has two factors of size `x^(1/2+o(1))`, not one tiny factor, and needs a deterministic completed quadratic form rather than an average over moduli. | No canonical contact is present, so R87 prevents importing this as an all-sector estimate. |
| [Fouvry--Kowalski--Michel--Sawin, *Bilinear forms with trace functions*](https://arxiv.org/abs/2511.09459), v3, 2026-03-11, Theorem 1.1 | For prime `q`, a gallant rank-at-least-two trace sheaf, nonzero `b,c`, `q^delta<=M`, `MN>=q^(3/4+delta)`, and `M,N<=q/2`, arbitrary coefficients satisfy `sum alpha_m beta_n K(m^b n^c) << norm(alpha)norm(beta)(MN)^(1/2-eta)`. | A fixed power `eta(delta)>0`; in the balanced case it reaches `M=N>=q^(3/8+delta/2)`. | The raw inverse additive phase `K(x)=e_q(a/x)` is a rank-one Artin--Schreier pullback and is not gallant.  Turning it into a rank-two Kloosterman trace function requires completion, which restores the zero and axis terms.  The modulus is also fixed and prime. | The hypotheses exclude the native reciprocal character, while the completion needed to enter the theorem is precisely where R87 locates the contact. |
| [Blomer--Pascadi, *Bilinear forms with Kloosterman sums via quadratic characters*](https://arxiv.org/abs/2607.24311), v1, 2026-07-27, Theorem 1.1 | For every modulus `c`, intervals `I,J` of length at most `N<=c`, arbitrary coefficients, and `(a,c)=1`, `sum alpha_m beta_n S(am,n;c) << norm(alpha)norm(beta)c^(1+o(1))[N^(1/8)c^(-3/32)+N^(5/16)c^(-3/16)+N^(2/3)c^(-7/18)]`, subject to the displayed coprimality condition.  It is nontrivial for `c^(13/28+eps)<N<c^(7/12-eps)`. | At `N=sqrt(c)`, `<< norm(alpha)norm(beta)c^(1-1/32+o(1))`, a relative `c^(-1/32)` saving. | This is a fixed-modulus sum of complete Kloosterman sums.  R71 has a varying denominator in `e_r(j theta inverse(p))`.  Completing the `p`-interval introduces an additive frequency and the zero/main modes; the useful balanced variables of this theorem are not the native `p,r` pair. | Arbitrary coefficients do not repair the mismatch.  R87 says the completed modes plus their degenerate terms reconstruct (1.1), so the `c^(-1/32)` gain cannot be assigned to the full R71 energy. |
| [Mohammadi, *Bilinear Kloosterman sums over small boxes*](https://arxiv.org/abs/2608.01203), v1, 2026-08-02, Theorem 1 | For `q=p^n`, boxes `B_1,B_2` with `abs(B_1)abs(B_2)>=q^(1/2+eps)`, arbitrary `abs(alpha),abs(beta)<=1`, and `b!=0`, `max_(a,b) abs(sum alpha(x)beta(y) psi(axy+b x^(-1)y^(-1))) <<_eps p^(-delta)abs(B_1)abs(B_2)`. | A fixed `p^(-delta(eps))` gain; for fixed extension degree this is a fixed power of `q`. | The modulus is a fixed finite field, and the phase depends on the product `xy`.  R71 uses a varying prime denominator and the ratio-like phase `theta inverse(p)`.  Replacing a variable by its inverse destroys the interval/box hypothesis. | This theorem formalizes mixing of nonzero reciprocal Fourier modes.  R86--R87 show why such mixing alone suppresses the transported term and leaves the canonical contact rather than cancelling it. |
| [Conrey--Kwan--Lin--Turnage-Butterbaugh, *Critical Zeros and Unconditional Mean Value Theorems*](https://arxiv.org/abs/2607.00282), v1, 2026-07-01, Theorems 1.3, 1.7, and 1.11 | Coefficients are supported on `h<=(TQ)^theta` and may satisfy Condition `(Lambda)`: `lambda_h<<h^(1/2)` and `sum abs(lambda_h)^(2m)/h << (TQ)^eps` for `m=1,2`; von Mangoldt and Möbius-log coefficients meet it.  For PGL(3), under Hypothesis `(Pi4)` when Condition `(Lambda)` replaces the stronger pointwise hypothesis, `Q^eps<=T<=Q^(1/3-eps)` and the bilinearly averaged error is `<<(TQ)^(7/4+theta/2+O(eps))`; `(Pi4)` is known for self-dual `Pi`.  The PGL(2) theorem is unconditional, has `Q^eps<=T<=Q^(1-eps)`, and error `<<(TQ)^(3/2+theta/2+O(eps))`.  Main terms have typical size `TQ^2`. | If `T=Q^omega`, direct comparison of the displayed errors with `TQ^2` gives PGL(3) nontrivial for `theta<(1-3omega)/(2(1+omega))-O(eps)` and PGL(2) for `theta<(1-omega)/(1+omega)-O(eps)`. | The theorem averages even primitive characters (with the odd case analogous), all moduli `q` near `Q`, and `t`.  In PGL(2) the polynomial length is less than `Q^(1-omega-o(1))`, missing the R71 endpoint `Q` by `Q^omega`; the gap collapses only as `omega->0`, where the theorem is not uniform.  R71 is every-block, prime-modulus, and Gauss-weighted.  The automorphic representation is fixed cuspidal; the zeta/Eisenstein degeneration is outside the theorem. | These theorems retain their own exact diagonal and dual main terms, making them the strongest structural comparator.  Those terms are not R87's canonical punctured-axis contact.  Naive subdivision of an endpoint polynomial introduces enough pieces to consume the displayed endpoint gain; the theorem states no signed recombination that avoids that loss. |
| [Matomaki--Radziwill--Shao--Tao--Teravainen, *Higher uniformity II*](https://arxiv.org/abs/2411.05770), v2, 2026-01-23; Inventiones DOI [10.1007/s00222-026-01408-6](https://doi.org/10.1007/s00222-026-01408-6) | For `X^(1/3+eps)<=H<=X`, almost all interval starts, fixed-complexity nilsequences, and every fixed `A`, the `Lambda-Lambda^sharp` correlation is `<<H log^(-A)X`; corresponding Gowers and Type-II contagion results follow. | Arbitrary logarithmic saving, not a fixed power. | The quantifier is almost every start and the theorem is scalar.  Rational--Archimedean major arcs are retained; it is not a deterministic joint tail--head--continuum square on the R71 bank. | It can import minor-arc cancellation but does not retain or estimate the R87 axis/contact combination. |
| [Kwan, *Spectral Moment Formulae II: The Eisenstein Case*](https://arxiv.org/abs/2310.09419), v3, 2026-03-16; JIMJ 2026, and [Yang, *Symmetric Spectral Reciprocity for GL(2)*](https://arxiv.org/abs/2607.04476), v1, 2026-07-05 | Kwan proves an exact Motohashi identity between shifted GL(2) cubic and GL(1) fourth moments with the full main terms.  Yang's Theorem A gives symmetric fourth-moment reciprocity with 24 explicit correction periods and proves `L(1/2,pi)<<C(pi)^(1/4-1/120+eps)`. | Exact identities; Yang has a `C^(-1/120)` subconvex gain for its native central value. | The coefficients are fixed divisor/Hecke data.  Eisenstein differentiation produces divisor-log coefficients, not `-zeta'/zeta`; logarithmic derivatives occur in normalizations and degenerate residues.  Balanced reciprocity is self-dual and does not contract the R71 scale. | The explicit correction periods confirm rather than remove the degenerate/contact terms.  None is identified with the finite canonical `Lambda-1` dual in (1.1). |

## 3. Direct zeta, reciprocal, and Mertens baselines

| Source | Exact current conclusion | Fixed-strip calibration |
|---|---|---|
| [Bellotti--Trudgian--Yang, *Zero-free regions inspired by work of Heath-Brown*](https://arxiv.org/abs/2603.21490), v1, 2026-03-23 | `zeta(sigma+it)!=0` for `t>=3` and `sigma>=1-1/(4.896 log t)`. | The width tends to zero; it is not a fixed strip. |
| [Bellotti, *A new zero-density estimate for zeta*](https://arxiv.org/abs/2508.02041), v1, 2025-08-04 | `N(sigma,T)=O(1)` sufficiently near the left edge of the Vinogradov--Korobov region, with the optimal PNT transfer for that region. | `O(1)` is not zero; one exceptional zero is fatal for R71. |
| [Lee--Leong, *New explicit bounds for Mertens function*](https://arxiv.org/abs/2208.06141), v4, 2024-07-26 | Explicit bounds of the form `M(x)<<x exp(-eta(log x)^(3/5)(log log x)^(-1/5))`. | This is `x^(1-o(1))`, not `x^(1-eta_0)`.  Conversely, a uniform bound `M(x)=O(x^(1-eta_0))` would analytically continue `1/zeta(s)` to `Re(s)>1-eta_0` and is already fixed-strip strength. |
| [Leong, *Explicit estimates for the logarithmic derivative and reciprocal of zeta*](https://arxiv.org/abs/2405.04869), v5, 2026-01-30 | Within known zero-free regions, `1/zeta(s)<< (log t)^(11/12)` in the classical region and `<<(log t)^(2/3)(log log t)^(1/4)` in the Vinogradov--Korobov region. | These improve size bounds inside an existing region; they do not widen it to a fixed half-plane. |

## 4. Version and search warnings

- [Dong--Robles--Zeindler, arXiv:2601.00292](https://arxiv.org/abs/2601.00292)
  was withdrawn on 2026-01-05.  The authors report a missing `L^2` factor;
  the claimed improved balanced Kloosterman-fraction and long-twist results
  are not admissible inputs.
- [Azevedo, arXiv:2012.09091](https://arxiv.org/abs/2012.09091), whose title
  claims a fixed strip from the PNT, was withdrawn with the comment “fatal
  error in proof.”  In the archived argument, continuity produces a radius
  depending on the fixed cutoff `x`; treating that radius as uniform for
  unbounded `x` is the fatal quantifier interchange.
- [Burton, arXiv:2106.04644](https://arxiv.org/abs/2106.04644), whose title
  claims existence of a fixed strip via a charged mean-ergodic theorem, is
  withdrawn; the author's withdrawal comment says the claims are
  unsubstantiated.  It is not an admissible lemma.
- [Puglisi, arXiv:2210.03121v9](https://arxiv.org/abs/2210.03121) claims that
  quasi-RH implies RH.  The exact audit in
  [`../results/R95-PUGLISI-QUASI-RH-AUDIT.md`](../results/R95-PUGLISI-QUASI-RH-AUDIT.md)
  finds a false final alternating-exponential inequality at
  `x=13,J=30=2 floor(x+2)` and an asymptotic reversal throughout the paper's
  large cutoff cells.  Consequently the printed theorem is not available as
  an import; this does not disprove the implication itself.
- [Broadbent--Fiori--Kadiri--Ng--Wilk, *Bounds for Mertens Sums*](https://arxiv.org/abs/2608.01498),
  v1, 2026-08-02, concerns prime harmonic sums and products such as
  `sum_(p<=x)1/p`; it is not a power bound for the Mobius Mertens function.
- [Verjovsky, *Local Moments of Mobius Fourier Polynomials and RH*](https://arxiv.org/abs/2607.25002),
  v1, 2026-07-27, gives an RH-equivalent local-moment criterion.  It supplies
  no new moment bound and therefore does not lower the R71 target.
- CKLTB v1 Remark 1.4 prints the PGL(3) range
  `theta<(1-3omega)/(2(1-omega))-O(eps)`.  This does not follow from its
  displayed error `(TQ)^(7/4+theta/2)` and stated main-term size `TQ^2`:
  for `T=Q^omega`, direct exponent comparison gives denominator
  `2(1+omega)`.  The matrix uses the displayed theorem bound and records
  the remark as a v1 inconsistency rather than silently importing it.

## 5. R87-guided research triage

Two source architectures expose a concrete experiment, but neither is an
imported proof.

1. **Quadratic-discriminant recombination.**  Blomer--Pascadi obtain their
   gain by converting a fourth power of the fixed-modulus Kloosterman
   operator into quadratic-character sums.  A genuinely new theorem would
   have to perform this conversion *after* retaining the outer prime-modulus
   sum and the R87 axes.  The fail-fast datum is the signed contribution of
   the square-discriminant locus: unless it reproduces the exact
   `P_1+P_2` coefficient and B-spline weight, it cannot cancel the contact.
2. **Gauss-weighted asymptotic large sieve.**  Multiplicative-character
   expansion of `e_r(k inverse(p))` introduces Gauss/root-number weights, so
   the CKLTB family is a structural model.  The missing theorem would need
   all of: prime-modulus restriction, Gauss weights, an Eisenstein/zeta
   degeneration with residues uniform, endpoint coefficient length `Q`,
   and a signed main term equal to the R87 axis.  The published PGL(2)
   endpoint algebra shows that block subdivision alone cannot supply this.

The practical conclusion is narrow: current literature can power-save
several nonzero or averaged pieces, but R87 identifies the unestimated
piece explicitly.  Proving its cancellation is the fixed-strip theorem,
not a remaining routine completion step.  Failure of the surveyed methods
does not prove nonexistence of a fixed zero-free strip.
