# Uniform-strip to R68 reverse calibration

Date: 2026-09-02  
Status: conditional reverse implication proved in the licensed fixed-window
and regular frozen-cutoff scopes; no zero-free strip or RH proved

Passport:
[reverse-calibration preflight](context/zeta23_strip_to_r68_reverse_calibration_preflight_v1.json)

## 0. Verdict

The calibration succeeds.  Assume that for one fixed
\(0<\delta\le 1/2\),

\[
 \delta\le\Re\rho\le1-\delta                            \tag{0.1}
\]

for every nontrivial zero of zeta.  Then every licensed regular
frozen-cutoff R68/R71 block satisfies

\[
 E_I^{\rm app}\le
 \exp\{(1-2\delta)R+o(R)\},\qquad
 X_I\le\exp\{(1-2\delta)R+o(R)\}.                       \tag{0.2}
\]

Here \(R\) is the right endpoint, \(E_I^{\rm app}=D_I+X_I\) is the complete
centered energy, and only the grouped atomic diagonal \(D_I\) has been
removed in \(X_I\).  At \(\delta=1/2\), (0.2) is the subexponential bound
and therefore supplies every target exponent \(\eta<1/2\).

Consequently the fixed-window version of the proposed R68 estimate is not
stronger than the strip.  Together with the already audited forward
energy-width theorem, it is exponent-equivalent to the strip:

\[
 \boxed{\quad
 \Re\rho\le1-\delta
 \quad\Longleftrightarrow_{\rm exponent}\quad
 X_I\le e^{(1-2\delta)R+o(R)}
 \ \hbox{on every fixed-window regular block}.
 \quad}                                                  \tag{0.3}
\]

There is one qualification.  A bound only for the **single sublinear
fixed-step growing schedule used here** still needs a varying-test converse
before it can imply a strip.  The separate fixed-total-width near-square
schedule has the same unresolved varying-test status for a different
multiplier limit.  R80 already proves a moving-edge
converse for a distinct dyadic bank of proportional-order schedules; that
theorem does not transfer automatically to the single schedule considered
here.  The reverse direction proved here, strip to growing-order energy,
remains valid on schedules whose window and Euler-transfer costs are
\(e^{o(R)}\).

Thus the earlier concern that the every-block quantifier might make the
licensed estimate strictly stronger was wrong.  A pointwise zero-side bound
automatically controls every nonnegative block energy.

## 1. Width notation and exact field

Put

\[
 \Delta=\sup_\rho\left|\Re\rho-\frac12\right|,\qquad
 d=\frac12-\delta.                                      \tag{1.1}
\]

By functional-equation symmetry, (0.1) is exactly \(\Delta\le d\).

For \(h>0\), integer \(k\ge1\), and \(L=hk\), let
\({\cal V}_{h,k}\) be the normalized compact R71 coboundary window.  Its
bilateral Laplace transform is

\[
 \widehat{\cal V}_{h,k}(s)
 =\frac1{N_{h,k}}\frac{2\sinh(Ls/2)}s
   \left(\frac{\sinh(hs/2)}{hs/2}\right)^k.             \tag{1.2}
\]

The cutoff-independent completed field has the absolutely convergent
explicit formula

\[
 {\cal D}_{h,k}^{\rm full}(r)
 =-\sum_\rho m_\rho e^{(\rho-1/2)r}
       \widehat{\cal V}_{h,k}(\rho-1/2)
  -\sum_{m\ge1}e^{(-2m-1/2)r}
       \widehat{\cal V}_{h,k}(-2m-1/2).                 \tag{1.3}
\]

This is the formula audited in
[FULL-FIELD-VK-SUBPOWER-BOUND.md](FULL-FIELD-VK-SUBPOWER-BOUND.md).
The full field is the safe object: no analytically continued infinite
Vaughan tail is evaluated on the critical line.

## 2. Conditional pointwise bound

### Theorem 2.1

Assume (0.1).  For fixed \(h,k\),

\[
 |{\cal D}_{h,k}^{\rm full}(r)|
 \ll_{h,k,\delta} e^{dr},\qquad r>L+1.                  \tag{2.1}
\]

More generally, if \(k=k_R\), \(L_R=hk_R=o(R)\), and \(k_R=o(R)\), then
uniformly for \(r\le R\) in a regular block,

\[
 |{\cal D}_{h,k_R}^{\rm full}(r)|
 \le \exp\{dr+o(R)\}.                                   \tag{2.2}
\]

#### Proof

For \(|\gamma|\ge1\) and \(|\sigma|\le1/2\), the exact multiplier satisfies

\[
 |\widehat{\cal V}_{h,k}(\sigma+i\gamma)|
 \le \frac{4e^{B_hk}}{\sqrt L}\,|\gamma|^{-k-1}.         \tag{2.3}
\]

The number of zeros with \(e^j\le|\gamma|<e^{j+1}\), including
multiplicity, is \(O(e^j(j+1))\).  Under (0.1),

\[
 |e^{(\rho-1/2)r}|\le e^{dr}.                           \tag{2.4}
\]

The contribution of the \(j\)-th high-zero shell is therefore at most

\[
 \frac{e^{dr+B_hk}}{\sqrt L}\,O((j+1)e^{-kj}).           \tag{2.5}
\]

The sum over \(j\) converges uniformly for \(k\ge1\).  The finitely many
lower zeros cost at most
\[
 e^{dr}\|\mathcal V_{h,k}\|_1e^{Ld}
 \le 2\sqrt L\,e^{dr+Ld},                               \tag{2.6}
\]
and the trivial-zero series decays exponentially once \(r>L+1\).
Equations (2.3)--(2.6) prove (2.1).  If \(k,L=o(R)\), every multiplier and
normalization loss displayed above is \(e^{o(R)}\), proving (2.2).

No cancellation between zeros is used.  This is why the conclusion is
uniform on every block rather than merely on almost all blocks.

## 3. From the full field to the complete R68 block

Let \(0\le\psi\le1\) be supported on a licensed regular block \(I\) with
right endpoint \(R\) and length \(H_I=e^{o(R)}\).  From (2.2),

\[
 E_I^{\rm full}
 =\int_I\psi(r)|{\cal D}_{h,k}^{\rm full}(r)|^2\,dr
 \le \exp\{2dR+o(R)\}
 =\exp\{(1-2\delta)R+o(R)\}.                            \tag{3.1}
\]

The exact cutoff-completion comparison is

\[
 \left|\sqrt{E_I^{\rm app}}-\sqrt{E_I^{\rm full}}\right|
 \le\|\sqrt\psi\,\varepsilon_I\|_2.                     \tag{3.2}
\]

For fixed-order R68 cutoffs, the audited Euler error is bounded or
power-decaying and hence has \(L^2\)-norm \(e^{o(R)}\).  On the regular
single fixed-step growing-order schedule, the proved estimate is stronger:

\[
 \|\sqrt\psi\,\varepsilon_I\|_2
 \le \exp\{-cR+O_h(k^2+k\log(k+2))\}.                   \tag{3.3}
\]

Whenever \(k^2=o(R)\), (3.2)--(3.3) preserve (3.1).  Finally,

\[
 E_I^{\rm app}=D_I+X_I,\qquad D_I\ge0,                 \tag{3.4}
\]

so

\[
 X_I=E_I^{\rm app}-D_I\le E_I^{\rm app}.               \tag{3.5}
\]

This proves (0.2).  The off-diagonal formulation creates no additional
conditional burden on its upper side.

## 4. The converse and the window-order distinction

For one fixed window, the completed cumulative energy obeys the audited
width law

\[
 \limsup_{R\to\infty}
 \frac{\log(1+E_{\le R})}{2R}=\Delta.                   \tag{4.1}
\]

Suppose the fixed-window estimate

\[
 X_I\le\exp\{(1-2\eta+o(1))R\},\qquad 0<\eta\le\tfrac12, \tag{4.2}
\]

holds uniformly on every regular block.  The range
`0<eta<=1/2` is necessary here: since \(D_I=e^{o(R)}\), (3.4)
then gives the same upper exponent for \(E_I^{\rm app}\).  For
`eta>1/2` the displayed exponent is negative and the diagonal term can no
longer be absorbed; no such converse is claimed.  The blocks have
subexponential overlap and count, so summation and (4.1) give

\[
 \Delta\le\frac12-\eta.                                 \tag{4.3}
\]

Zeta symmetry then gives \(\eta\le\Re\rho\le1-\eta\).
Combining (0.2) and (4.3) proves the fixed-window exponent equivalence.

For \(k=k_R\to\infty\), (1.2) changes with \(R\) and can increasingly
suppress a fixed zero ordinate.  The implication

\[
 \text{fixed strip}\Longrightarrow\text{growing-order block bound}
                                                               \tag{4.4}
\]

is proved by Theorem 2.1, but the reverse implication for this single
schedule is not licensed until a varying-test carrier theorem is supplied.
R80's proportional-order dyadic bank has its own moving-edge converse and
is not a counterexample to this scoped statement.  A single-schedule
growing-order bound alone must not be advertised as strip-equivalent.

## 5. The aggregate R68 coordinate

For fixed \(h,k\), the exact Vaughan identity writes the centered aggregate
as

\[
 B_{U,V}^{(k)}(x)-Z_{U,V}^{(k)}(x)
 =C_{h,k}(\log x)+O_{h,k}(1)                            \tag{5.1}
\]

at the endpoint cutoff and with a decaying error below it.  Its zero
multiplier is \(O_{h,k}(|\gamma|^{-k-1})\).  Thus the same proof gives the
endpoint conditional estimate

\[
 B_{U,V}^{(k)}(x)-Z_{U,V}^{(k)}(x)
 =O_{h,k,\delta}(x^{1/2-\delta}).                       \tag{5.2}
\]

Conversely, an \(O(x^{1/2-\eta})\) estimate for all sufficiently large real
\(x\) gives \(\Delta\le1/2-\eta\).  This sharpens the conservative
\(+\epsilon\) reverse statement obtainable from the limsup identity alone:
the endpoint bound in (5.2) uses absolute convergence of the fixed-window
zero series.

The fixed aggregate and fixed-window energy are therefore two
strip-equivalent coordinates, not independently easier lemmas.

## 6. Causal-box control case

For fixed \(L>0\), put

\[
 {\mathfrak B}_L(x)=\int_{xe^{-L}}^xR_\zeta(y)\frac{dy}{y},\qquad
 K_L(s)=\frac{1-e^{-Ls}}s.                              \tag{6.1}
\]

Its nontrivial-zero expansion is

\[
 \sum_\rho
 \frac{1-\rho}{\rho(\rho+1)}K_L(\rho)x^\rho,            \tag{6.2}
\]

up to the explicit pole and trivial-zero terms.  Since

\[
 \frac{1-\rho}{\rho(\rho+1)}K_L(\rho)
 =O_L(|\rho|^{-2}),                                     \tag{6.3}
\]

the series is absolutely convergent.  Hence (0.1) implies the endpoint
bound

\[
 {\mathfrak B}_L(x)=O_L(x^{1-\delta}).                  \tag{6.4}
\]

Conversely, either eventual one-sided orientation

\[
 {\mathfrak B}_L(x)\ge-Cx^a
 \quad\hbox{or}\quad
 {\mathfrak B}_L(x)\le Cx^a                             \tag{6.5}
\]

excludes zeros with \(\Re\rho>a\), because every nonzero zero of \(K_L\)
lies on \(\Re s=0\) and Landau's theorem applies.  Thus for each fixed
\(L\), the causal-box statement is endpoint-equivalent to a fixed strip.
Its extra smoothing removes the logarithmic or \(\epsilon\) loss in the
routine strip-to-pointwise-R95 estimate.

## 7. Where overspecification really begins

The honest block \(I\) above is a scale block of the fully recompleted
field.  It is not a dyadic rectangle, one cofactor, or one parity sector.
The strip does not give the same exponent saving separately on those
components.

For example, on a central \(m=1\) rectangle with
\(D,Q\asymp x^{1/2}\), the rank-one term is

\[
 T_{\rm rect}=
 \left(\sum_{d\sim D}\frac{\mu(d)}{\sqrt d}\right)
 \left(\sum_{p\sim Q}\frac{\log p}{\sqrt p}\right).
                                                               \tag{7.1}
\]

A strip of width \(\delta\) gives, with an arbitrarily small exponent loss,

\[
 M(D)\ll D^{1-\delta+\epsilon},\qquad
 T_{\rm rect}\ll x^{1/2-\delta/2+\epsilon}.              \tag{7.2}
\]

Conversely, a sufficiently uniform sliding-rectangle estimate

\[
 |T_{\rm rect}|\ll x^{1/2-\eta+o(1)}                    \tag{7.3}
\]

forces \(M(D)\ll D^{1-2\eta+o(1)}\), hence a strip of width
\(2\eta\).  Demanding the complete-field saving \(\eta=\delta\)
separately on every rectangle is therefore stronger than the assumed
strip.  The missing factor of two is recovered only through the
cross-rectangle, cross-cofactor, and center terms.

Likewise, extending (0.2) to arbitrary frozen cutoffs would require the
additional transfer estimate

\[
 \|\sqrt\psi\,\varepsilon_I\|_2
 \le\exp\{(1/2-\delta+o(1))R\},                          \tag{7.4}
\]

which is not supplied by the strip.  The licensed theorem quantifies only
over cutoff schedules for which the existing Euler ledger proves (7.4).

For the forward strip implication, a single fixed bounded-overlap regular
partition is enough; requiring every admissible weight is unnecessary.
The strip happens to imply the stronger every-weight statement because
(2.2) is pointwise.

## 8. Decision-tree correction

The reverse audit changes the roadmap in three ways.

1. The complete fixed-window R68 bound is correctly calibrated, but it is
   the strip written as a positive energy.  It should not be called an
   easier intermediate lemma.
2. The every-block quantifier is necessary for the forward implication and
   is automatically supplied by the strip in reverse.  It is not the source
   of excess strength.
3. The single fixed-step growing-order coordinate is conditionally easier in one
   direction because its multiplier cools the zero spectrum.  Without a
   varying-test converse it is not yet a faithful replacement for the
   fixed-window endpoint.

Therefore a genuine intermediate theorem must introduce an independently
motivated arithmetic mechanism that implies the complete fixed-window
energy bound.  Merely restating (4.2), or proving it only for the
spectrally cooling growing window, does not reduce the problem.

The best scalar calibration remains (6.5): it is faithful, absolutely
convergent, and exactly strip-strength.  It is cleaner than R68 for
diagnosis, but currently has no easier coefficient-side proof.

## 9. Trust and nonclaims

- The zero-side explicit formula, multiplier bound, zero counting, Vaughan
  completion, Euler-transfer estimate, and fixed-window energy law are
  imported from the audited local R68/R71 chain.
- The reverse implication is a direct synthesis of those results.  No
  literature-level novelty is claimed.
- Finite tests replay the exponent map, block-energy implication, and
  faithful fixed-box multiplier.  They do not prove the analytic inputs.
- Six reverse-calibration tests pass; the combined R68/R95 suite has 90
  passing tests.
- No fixed zero-free strip, unconditional fixed-\(\eta\) estimate, or RH is
  proved.

The resulting claim table is

\[
\begin{array}{c|c}
\text{strip}\Rightarrow\text{fixed-window R68 block bound}&\text{PROVED, conditional}\\
\text{fixed-window R68 block bound}\Rightarrow\text{strip}&\text{AUDITED IMPORT}\\
\text{strip}\Rightarrow\text{single fixed-step growing block bound}&\text{PROVED, conditional}\\
\text{single fixed-step growing block bound}\Rightarrow\text{strip}&\text{OPEN}\\
\text{strip}\Longleftrightarrow\text{fixed causal-box exponent}&\text{PROVED}\\
\text{unconditional strip}&\text{OPEN}\\
\text{RH}&\text{OPEN}
\end{array}
\]
