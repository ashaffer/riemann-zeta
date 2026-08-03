# Möbius/Chowla bridge audit

Status: exact algebraic bridge obtained; no new implication is claimed.

## 1. Exact conversion of the prime functional

Let `g` be compactly supported on the logarithmic line and put

\[
 P(g)=\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}g(\log n).
\]

The elementary Dirichlet-convolution identity

\[
 \Lambda=\mu*\log,
 \qquad
 \Lambda(n)=\sum_{dm=n}\mu(d)\log m
\]

gives the finite identity

\[
 P(g)=\sum_{d,m\ge1}
 \frac{\mu(d)\log m}{\sqrt{dm}}g(\log d+\log m).
 \tag{MC}
\]

Thus every prime term in the compact-support Weil form can be expressed as a
linear Möbius statistic.  Compact support makes (MC) a finite rearrangement,
so it requires no analytic continuation or RH.

For fixed `g`, define

\[
 F_g(d)=d^{-1/2}\sum_m\frac{\log m}{\sqrt m}g(\log(dm)).
\]

Then `P(g)=sum_d mu(d) F_g(d)`.  Abel summation converts any bound for the
Mertens function `M(x)=sum_{n<=x} mu(n)` into a bound for `P(g)`:

\[
 \left|\sum_{d\le X}\mu(d)F_g(d)\right|
 \le |M(X)F_g(X)|+
 \int_1^X |M(t)|\,|F_g'(t)|\,dt,
 \tag{AS}
\]

with the standard piecewise-smooth interpretation.  This is a useful transfer
lemma, but it does not by itself supply the sign needed by Weil positivity.

## 2. Strength audit: square-root Möbius cancellation

The tempting hypothesis

\[
 M(x)=O_\varepsilon(x^{1/2+\varepsilon})
 \quad\text{for every }\varepsilon>0
 \tag{SM}
\]

is not an independent route to RH.  It is the classical Littlewood criterion,
equivalent to RH.  Indeed, partial summation makes

\[
 \frac1{\zeta(s)}=s\int_1^\infty M(x)x^{-s-1}\,dx
\]

analytic for `Re(s)>1/2` under (SM), while RH gives (SM) by the usual Perron
contour argument (with epsilon loss).  Consequently, using (SM) in (AS) may
be diagnostically useful but cannot be advertised as reducing RH to an
independently weaker conjecture.

## 3. A precise two-point target, and why it is also RH-equivalent

Define the *aggregate Chowla correlation*

\[
 A(X)=\sum_{h=1}^{X-1}\sum_{n\le X-h}\mu(n)\mu(n+h).
\]

The exact identity

\[
 M(X)^2=\sum_{n\le X}\mu(n)^2+2A(X)                         \tag{AC}
\]

shows that the apparently correlation-theoretic conjecture

\[
 |A(X)|=O_\varepsilon(X^{1+\varepsilon})
 \quad\text{for every }\varepsilon>0                        \tag{AGC}
\]

implies (SM), hence RH.  Conversely RH implies (AGC), after changing
`epsilon`, because `sum mu(n)^2=O(X)` and (AC).  Therefore (AGC) is a clean,
elementary two-point reduction, but it is exactly RH-equivalent rather than a
strictly simpler known conjecture.  Its possible value is methodological: it
asks for cancellation after summing all shifts, a statistic amenable to
harmonic/additive-combinatorial tools.

Ordinary Chowla is qualitatively different: it concerns each fixed collection
of distinct shifts as `X -> infinity`.  Even the known logarithmically averaged
two-point theorem does not provide the support-uniform, power-scale aggregate
bound (AGC).  One must not cite qualitative or logarithmic Chowla as if it
implied RH.

## 4. Rejected disguised reformulation

Substituting (MC) into the desired inequality

\[
 2\operatorname{Re}P(g)\le Q_{\rm pole}(g)+Q_{\rm arch}(g)
\]

does produce a “Möbius domination conjecture.”  For autocorrelations `g` in
the Weil class, however, this is algebraically the same Weil positivity
criterion.  It is not a new bridge and should not enter the reduction registry
except as a rejected reformulation.

## 5. Viable next experiment

Study the spectral decomposition of `A(X)` by logarithmic frequency and compare
its exceptionally small modes with the near-null modes of the windowed Weil
form.  A useful new result would need an intermediate estimate that:

1. is materially weaker than (SM)/(AGC),
2. exploits the restricted autocorrelation weights occurring in (MC), and
3. still controls their sign, rather than merely their absolute magnitude.

Without item 3, Möbius cancellation only bounds the prime block and does not
establish Weil positivity.

## Primary literature anchors

- J. E. Littlewood, *On the Riemann Zeta-Function*, Proc. London Math. Soc.
  (1926), DOI: <https://doi.org/10.1112/plms/s2-24.1.175>.
- T. Tao, *The logarithmically averaged Chowla and Elliott conjectures for
  two-point correlations*, Forum Math. Pi 4 (2016), e8,
  <https://arxiv.org/abs/1509.05422>.
- T. Tao, *Equivalence of the logarithmically averaged Chowla and Sarnak
  conjectures*, Number Theory—Diophantine Problems, Uniform Distribution and
  Applications (2017), <https://arxiv.org/abs/1605.04628>.
