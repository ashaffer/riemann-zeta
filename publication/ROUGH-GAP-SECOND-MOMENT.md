# A second-moment bound for gaps between polynomially rough integers

## Abstract

Let \(\mathcal R_z\) be the positive integers having no prime divisor below
\(z\), and let \(G_2(X;z)\) be the sum of the squares of the consecutive
\(\mathcal R_z\)-gaps which meet \([X,2X]\).  We extract from Matomäki's
shifted-correlation estimate a uniform bound

\[
  G_2(X;z)\ll_\varepsilon X(\log X)^2
  \qquad
  \left(X^\varepsilon\le z\le X^{3/16-\varepsilon}\right).
\]

The proof combines a vector-sieve lower minorant, the raw form of
Matomäki's Lemma 5.4, Iwaniec's Jacobsthal bound, and an exact layer-cake
identity.  A fixed-level specialization with linear-sieve level \(X^{1/3}\)
already gives the simpler range \(z\le X^{1/6-\varepsilon}\).

The theorem type is not new.  Friedlander proved the same endpoint
\(X(\log X)^2\) for his self-sifted sequence in 1984, with an admissible
roughness exponent \(\alpha<1/25\).  More directly, Proposition 2 of his
2008 Oberwolfach report treats prescribed cutoffs through \(z\le X^{1/20}\)
and implies the corresponding gap-square bound.  The possible contribution
here is therefore only the larger polynomial exponent range.  The
literature audit in Section 8 makes no claim that the corollary below has
not appeared elsewhere.

## 1. Statement

Write

\[
  P(z)=\prod_{p<z}p,
  \qquad
  \mathcal R_z=\{n\ge1:(n,P(z))=1\}.
\]

List \(\mathcal R_z\) increasingly as \(r_1<r_2<\cdots\), put
\(g_j=r_{j+1}-r_j\), and define

\[
  G_2(X;z)=
  \sum_{\substack{j:\ (r_j,r_{j+1})\cap[X,2X]\ne\varnothing}}g_j^2.
  \tag{1.1}
\]

Thus (1.1) includes the gaps crossing the two endpoints.

**Theorem 1.**  Fix \(0<\varepsilon<3/32\).  Uniformly for real \(z\)
satisfying

\[
  X^\varepsilon\le z\le X^{3/16-\varepsilon},
  \tag{1.2}
\]

one has, as \(X\to\infty\),

\[
  G_2(X;z)\ll_\varepsilon X(\log X)^2.
  \tag{1.3}
\]

The following version keeps all auxiliary levels independent of the
endpoint margin.

**Corollary 2 (fixed linear level).**  For each fixed \(\varepsilon>0\),

\[
  G_2(X;z)\ll_\varepsilon X(\log X)^2
  \qquad
  \left(X^\varepsilon\le z\le X^{1/6-\varepsilon}\right).
  \tag{1.4}
\]

In particular, (1.4) contains the project-specific range
\(X^{0.1537}\le z\le X^{0.16}\).

Neither statement concerns gaps between primes, and neither statement by
itself implies a zero-free region for the Riemann zeta function.

## 2. The imported analytic estimates

Only the following published inputs are used.

1. Proposition 5.1 of Matomäki decomposes the mean square of a divisor-sum
   discrepancy with bounded coefficients supported on \(d\le D_0\), where
   \(D_0\le X^{1-c}\), into terms \(S_1,S_2,S_3\) and an error
   \(O(H^3(\log X)^3)\).

2. Matomäki's Lemma 5.4 holds for every \(2\le H\le X\), without the
   \(H\le X^{1/60}\) restriction imposed later in Lemma 5.3.  In exponent
   notation its exact upper bound is

   \[
   H^{1/2}X^{1/2+\xi/10}
   \left[
      (MQ)^2+
      \left(\frac{HMNQ}{X}+N\right)
      \left\{
        MQ\left(\frac{HMNQ}{X}+N\right)(Q+N^2)
        +\frac{H(MN)^3Q}{X}
      \right\}
   \right]^{1/4}.
   \tag{2.1}
   \]

3. The proofs of Matomäki's equations (49) and (69), in Sections 6.1 and
   6.3, control \(S_1\) and \(S_3\) for the vector-sieve lower
   coefficients.  Their numerical choice \(D=X^{5/9}\) is not used in
   those two arguments.  They use a fixed-ratio beta sieve below
   \(w=X^\delta\), elementary Euler products above \(w\), and a Shiu
   bound.

4. In the proof of her equation (61), Matomäki invokes the standard
   well-factorable decomposition of the upper and lower linear-sieve
   weights (Friedlander--Iwaniec, Section 12.7).  For any prescribed
   factorization of the level, it gives finitely many convolutions of
   bounded factors supported at those two levels, with an arbitrarily
   small fixed power slack.  We retain this slack explicitly as
   \(X^\nu\).

5. Iwaniec's Jacobsthal theorem implies that the largest gap between
   integers avoiding all primes at most \(z\) is \(O(z^2)\).  The set
   avoiding primes below \(z\) is at least as dense, so

   \[
      \max_j g_j\ll z^2.
   \tag{2.2}
   \]

Items 1--4 are in K. Matomäki, *Almost primes in almost all very short
intervals*, especially Proposition 5.1, Lemma 5.4, and Sections 6.1--6.3.
The distinction between Lemmas 5.3 and 5.4 is essential: using the simplified
Lemma 5.3 would discard nearly all of the available range.

## 3. The lower minorant

Let

\[
  b=\frac{\log z}{\log X},\qquad
  d=\frac38-\varepsilon,\qquad
  e=\min\left(\frac1{1000},\frac\varepsilon{10}\right),
  \qquad L=d+e.
  \tag{3.1}
\]

Put \(D=X^d\), \(E=X^e\), and \(w=X^\delta\), where \(\delta>0\) is
chosen sufficiently small in terms of \(\varepsilon\).  In particular we
require

\[
  \delta<\varepsilon,
  \qquad
  \frac e\delta\ge30.
  \tag{3.2}
\]

Use beta-sieve upper and lower weights \(\rho_e^\pm\) of level \(E\) for
the primes below \(w\), and linear-sieve upper and lower weights
\(\lambda_d^\pm\) of level \(D\) for the primes in \([w,z)\).  Matomäki's
vector-sieve identity, her equations (14)--(16), gives coefficients
\(\alpha_r^-\) such that

\[
  \mathbf 1_{(n,P(z))=1}\ge \sum_{r\mid n}\alpha_r^-.
  \tag{3.3}
\]

The coefficients are bounded, are supported on \(r\le DE=X^L\), and use
only primes below \(z\).  Explicitly they are the three combinations
\(\lambda^+\rho^-+\lambda^-\rho^+-\lambda^+\rho^+\); the split prime
ranges make each convolution representation unique.

Let

\[
  A_z=\sum_r\frac{\alpha_r^-}{r}.
  \tag{3.4}
\]

If \(L^\pm\) and \(B^\pm\) denote the corresponding linear- and beta-sieve
main sums, then

\[
  A_z=L^+B^-+L^-B^+-L^+B^+
      =L^-B^+-L^+(B^+-B^-).
  \tag{3.5}
\]

The linear-sieve parameter is \(s=d/b\).  At the upper endpoint in (1.2),

\[
  d-2b\ge\varepsilon,
  \qquad s\ge2+c_\varepsilon>2.
  \tag{3.6}
\]

The dimension-one lower-sieve function is therefore bounded below by a
positive constant depending only on \(\varepsilon\).  The fundamental
lemma for \(\rho^\pm\), followed by the ordinary upper and lower linear
sieve in (3.5), yields, after making \(\delta\) smaller if necessary,

\[
  A_z\ge c_\varepsilon V(z)\gg_\varepsilon\frac1{\log X}.
  \tag{3.7}
\]

The subtraction in (3.5) is harmless because \(B^+-B^-\) can be made an
arbitrarily small fixed fraction of \(V(w)\).  This point is lost if one
simply multiplies two lower sieve bounds.

For \(H\ge2\), define

\[
  \mathcal E_z(x;H)=
  \sum_r\alpha_r^-
  \left(
    \#\{m:x-H<rm\le x\}-\frac Hr
  \right).
  \tag{3.8}
\]

By (3.3),

\[
  \#\bigl((x-H,x]\cap\mathcal R_z\bigr)
  \ge HA_z+\mathcal E_z(x;H).
  \tag{3.9}
\]

## 4. The raw Lemma 5.4 calculation

Set

\[
  \eta=d.
  \tag{4.1}
\]

For one of the two linear weights occurring after expanding a product of
two \(\alpha^-\)'s, use well-factorability at

\[
  R=X^{2L/3},
  \qquad
  S=D/R.
  \tag{4.2}
\]

Group the beta-sieve variable of level \(E\) with the \(S\)-variable.  Up
to a support enlargement \(X^\nu\), dyadic subdivision gives the
parameters

\[
  M\le X^{2L/3+O(\nu)},
  \qquad
  N\le X^{L/3+O(\nu)},
  \qquad
  Q\le X^L,
  \tag{4.3}
\]

because

\[
  d-\frac{2L}{3}+e=\frac L3.
  \tag{4.4}
\]

The remaining \(\alpha^-\)-coefficient is the bounded \(Q\)-coefficient.
This is exactly the reduction used for Matomäki's equation (61), with a
different factorization of the linear level.

First ignore the arbitrarily small \(\nu\).  The decisive inequality is

\[
  \eta+\frac{5L}{3}
  =1-\frac{8\varepsilon}{3}+\frac{5e}{3}<1.
  \tag{4.5}
\]

Consequently \(HMNQ/X\le N\), and every term in the fourth-power bracket
of (2.1) has the following exponent:

\[
\begin{aligned}
  \frac{HMNQ}{X}+N &\ll X^{L/3},\\
  Q+N^2 &\ll X^L,\\
  MQ\left(\frac{HMNQ}{X}+N\right)(Q+N^2)
    &\ll X^{3L},\\
  \frac{H(MN)^3Q}{X}&\ll X^{\eta+4L-1}\le X^{3L},\\
  (MQ)^2&\ll X^{10L/3}.
\end{aligned}
  \tag{4.6}
\]

After multiplication by the outer factor
\(HMNQ/X+N\), the second line inside braces also contributes at most
\(X^{10L/3}\).  Thus (2.1) is

\[
  \ll
  X^{1/2+\eta/2+5L/6+O(\nu)+\xi/10}
  =X^{1-\Delta+O(\nu)+\xi/10},
  \tag{4.7}
\]

where

\[
  \Delta=\frac{4\varepsilon}{3}-\frac{5e}{6}
  \ge\frac{5\varepsilon}{4}>0.
  \tag{4.8}
\]

Choose the factorization slack \(\nu\) and the \(\xi\) in Lemma 5.4
sufficiently small in terms of \(\varepsilon\).  Logarithmic dyadic losses
are then absorbed by the fixed power saving in (4.7).  Since the weight
\(H-|k|\) in \(S_2\) costs at most one further factor \(H\), this proves

\[
  S_2\ll_\varepsilon \frac{XH}{\log X}
  \qquad(2\le H\le X^d).
  \tag{4.9}
\]

The proofs of Matomäki's (49) and (69) give, with the same modified fixed
parameters,

\[
  S_1+S_3\ll_\varepsilon\frac{XH}{\log X}.
  \tag{4.10}
\]

For clarity, their uniformity here uses the following facts: \(e/\delta\)
is at least the fixed beta parameter 30; \(\log z/\log w\) is bounded in
terms of \(\varepsilon\); \(DE=X^L\le X^{1-c_\varepsilon}\); and the
coefficients remain bounded.  No estimate in those two arguments becomes
worse when \(D=X^{5/9}\) is replaced by the smaller level in (3.1).

Finally,

\[
  H^3(\log X)^3\ll_\varepsilon\frac{XH}{\log X}
  \qquad(H\le X^d),
  \tag{4.11}
\]

because \(d<3/8<1/2\).  Proposition 5.1, with an \(O(1)\) family of smooth
cutoffs, now gives the mean-square estimate

\[
  \int_{\mathcal I_X}|\mathcal E_z(x;H)|^2\,dx
  \ll_\varepsilon\frac{XH}{\log X}
  \qquad(2\le H\le X^d),
  \tag{4.12}
\]

where \(\mathcal I_X\) may be any fixed multiplicative enlargement of
\([X,2X]\).

### 4.1 Why the moving-level statement is a theorem, not only an optimizer

The substitutions in (3.1) are not justified merely by matching exponents.
The following dependency audit was made against the published proof.

- Proposition 5.1 is printed for arbitrary bounded \(a_d\) supported on
  \(d\le D_0\le X^{1-c}\).  Here \(D_0=DE=X^L\), so its hypotheses are
  unchanged.

- For the lower coefficient, Matomäki's equation (49) is reduced on
  pp. 21--23 to her equation (55).  The linear-sieve part is bounded there
  by an Euler product over \(w\le p<z\); it is
  \(O_\varepsilon(1)\) because \(\log z/\log w=O_\varepsilon(1)\).
  Equations (58)--(60) use the beta level only through
  \(\log E/\log w\ge\beta=30\).  Thus replacing \(1/1000\) by the fixed
  positive exponent \(e\) in (3.1) changes only the
  \(\varepsilon\)-dependent constant.

- For \(S_3\), the proof of equation (69) on pp. 29--30 bounds the vector
  coefficient pointwise by beta-sieve divisor sums and reduces the claim to
  the same Shiu estimate used for (71).  The numerical value of \(D\) is
  absent after that reduction, and the only small-prime requirements are
  again fixed \(\beta=30\) and \(w=X^\delta\).

- For \(S_2\), the paragraph following equation (68) and leading to (61)
  is precisely where the finite well-factorable convolution is inserted.
  Replacing its printed factorization by (4.2) is allowed by the cited
  well-factorability statement; (4.5)--(4.8) then verify the hypotheses of
  the raw Lemma 5.4 term by term.

All exponents \(d,e,\delta,\nu,\xi\) are fixed after
\(\varepsilon\) is fixed.  The theorem claims no constant uniform as
\(\varepsilon\downarrow0\).  Consequently the standard fixed-parameter
meaning of the cited \(O\)-constants suffices, and \(3/16\) is promoted to
Theorem 1 rather than left as a conditional or formal frontier.

## 5. Empty intervals

Let \(B_X(H)\) be the set of \(x\) in a fixed enlargement of \([X,2X]\)
for which \((x-H,x]\cap\mathcal R_z\) is empty.  By (3.7), (3.9), and
(4.12),

\[
  \operatorname{meas} B_X(H)
  \ll_\varepsilon
  \frac{XH/\log X}{(H/\log X)^2}
  \ll_\varepsilon\frac{X\log X}{H}
  \qquad(2\le H\le X^d).
  \tag{5.1}
\]

This is an upper bound for empty intervals obtained from a lower minorant;
no asymptotic formula for the actual rough-number variance is asserted.

## 6. From empty intervals to gaps

Let \(\mathcal G\) be the multiset of gaps in (1.1), and put

\[
  T(H)=\sum_{g\in\mathcal G}(g-H)_+.
  \tag{6.1}
\]

For each gap of length \(g\), the endpoints \(x\) for which
\((x-H,x]\) lies inside the gap form an interval of measure
\((g-H)_+\).  These intervals are disjoint.  Since the boundary gaps are
also included and have length \(o(X)\), all such endpoints lie in one fixed
multiplicative enlargement of the shell.  Therefore

\[
  T(H)\le \operatorname{meas}B_X(H).
  \tag{6.2}
\]

At the upper endpoint in (1.2), (2.2) and (3.1) give

\[
  \max_{g\in\mathcal G}g
  \ll z^2
  \le X^{3/8-2\varepsilon}
  =X^{d-\varepsilon}.
  \tag{6.3}
\]

Thus every relevant \(H\) in the exact identity

\[
  \sum_{g\in\mathcal G}g^2
  =2\int_0^\infty T(H)\,dH
  \tag{6.4}
\]

lies in the range of (5.1), once \(X\) is sufficiently large.  The total
length of the gaps in \(\mathcal G\) is \(O(X+z^2)=O(X)\), so
\(T(H)\ll X\) for \(0\le H<2\).  Combining this with (5.1)--(6.4) gives

\[
\begin{aligned}
  G_2(X;z)
  &\ll X+X\log X\int_2^{O(z^2)}\frac{dH}{H}\\
  &\ll_\varepsilon X(\log X)^2.
\end{aligned}
  \tag{6.5}
\]

This proves Theorem 1.

## 7. Fixed-level corollary and the exact frontier

For Corollary 2 take

\[
  d=\eta=\frac13,
  \qquad e=\frac1{1000},
  \qquad L=\frac{1003}{3000}.
  \tag{7.1}
\]

The same balanced factorization gives the exact raw-correlation saving

\[
  1-\left(\frac12+\frac d2+\frac{5L}{6}\right)
  =\frac{197}{3600}.
  \tag{7.2}
\]

Lower-sieve positivity and Jacobsthal coverage both hold whenever
\(2b<1/3\), proving (1.4).  At \(b=0.16\), for example,

\[
  \frac db=\frac{25}{12}>2,
  \qquad 2b=0.32<\frac13.
  \tag{7.3}
\]

The exponent \(3/16\) is the exact supremum of this balanced parameter
scheme.  With general linear level \(X^d\), beta level \(X^e\), and
variance ceiling \(X^\eta\), the three strict constraints are

\[
  2b<d,
  \qquad
  2b<\eta,
  \qquad
  \eta+\frac{5(d+e)}3<1.
  \tag{7.4}
\]

Letting \(e\downarrow0\), one obtains

\[
  2b<\min\left(d,1-\frac{5d}{3}\right).
  \tag{7.5}
\]

The two affine branches in (7.5) meet at \(d=3/8\), and their common half
is \(b=3/16\).  Hence no choice of \(d,\eta,e\) within this particular
minorant, two-factor Lemma 5.4, and \(J(z)\ll z^2\) architecture crosses
\(3/16\).  This is a method frontier, not a no-go theorem for rough gaps.

## 8. Prior work and novelty audit

### 8.1 Direct overlap: Friedlander (1984 and 2008)

For fixed \(\alpha\), Friedlander considered

\[
  S(\alpha)=\{m:\text{no prime }p<m^\alpha\text{ divides }m\}.
\]

His theorem states that one may take \(\alpha_0=1/25\) and, for fixed
\(0<\alpha<\alpha_0\) and \(0\le\gamma<2\),

\[
  \sum_{s_n\le X}(s_{n+1}-s_n)^\gamma
  \ll X(\log X)^{\gamma-1}.
\]

Remark (c) on the first page gives the endpoint produced by his method:

\[
  \sum_{s_n\le X}(s_{n+1}-s_n)^2
  \ll X(\log X)^2.
  \tag{8.1}
\]

For fixed \(0<b<1/25\), choose \(\alpha\) strictly between \(b\) and
\(1/25\).  On any fixed dyadic enlargement of \([X,2X]\), one has
\(m^\alpha\ge X^b\) for all sufficiently large \(X\).  Hence the points of
\(S(\alpha)\) there form a subset of the \(X^b\)-rough integers.  Adding
points only refines gaps and decreases the sum of their squares; the two
boundary gaps are also controlled by the adjacent Friedlander gaps (or by
Jacobsthal).  Thus (8.1) already yields the fixed-shell theorem in that
earlier exponent range.

There is a stronger prescribed-cutoff overlap.  Proposition 2 in
Friedlander's 2008 Oberwolfach report states, uniformly for
\(2\le z\le x^{1/20}\), that if

\[
  w=\eta(x)\log z,\qquad \eta(x)\longrightarrow\infty,
\]

then all but a set of \(y\in(x,2x]\) of measure \(O(x/\eta(x))\) satisfy

\[
  \#\{y-w<n\le y:(n,P(z))=1\}\asymp\frac{w}{\log z}.
  \tag{8.2}
\]

For \(H\ge(\log\log X)\log z\), apply (8.2) on dyadic values of \(H\)
with \(\eta=H/\log z\).  It gives the empty-interval bound

\[
  \operatorname{meas}B_X(H)\ll\frac{X\log z}{H}.
  \tag{8.3}
\]

The trivial bound below that threshold, followed by the same dyadic
layer-cake argument as Section 6, gives

\[
  G_2(X;z)\ll X(\log X)^2
  \qquad(z\le X^{1/20}).
  \tag{8.4}
\]

Thus the strongest explicit polynomial prior-art frontier located in this
audit is \(1/20\), not \(1/25\).  Accordingly, (1.3) should be described as
an exponent-range extension from \(1/20\) and a new extraction from
Matomäki, not as a new kind of gap theorem.

### 8.2 Related but not identical results

- Friedlander's *Sifting short intervals* I and II study exceptional empty
  intervals for sifted sequences.  They are direct ancestors of (8.2), but
  neither their publisher records nor the later 2008 report reaches the
  exponent range in (1.2).

- Huxley's *Irregularity in sifted sequences* proves upper and lower bounds
  for residue-class variance of sifted sequences.  Its advertised variance
  is not a consecutive-gap second moment and does not rule out (1.3).

- Gorodetsky obtains an asymptotic for the variance of the actual rough
  indicator in a substantial range.  His polynomial simultaneous regime
  does not contain \(z=X^b\), \(H=X^\eta\) with fixed positive \(b,\eta\)
  as used here.  His limitations on that asymptotic are therefore not a
  no-go theorem for the lower-minorant upper bound (4.12).

- Gafni and Tao study rough integers inside consecutive prime gaps, with a
  subpolynomial cutoff such as \(\exp((\log X)^\beta)\), and use higher
  moments of singular series.  Their target and parameter regime differ
  from (1.3).

The search located no primary source explicitly printing (1.3) in the
range \(1/20<b<3/16\).  A literature search cannot establish absence, so
no stronger novelty claim is made.  Before journal submission, this point
should be checked with specialists in sieve methods and against descendants
of Friedlander's 1984 argument.

## 9. Hostile hypothesis ledger

The proof uses every item below; omitting any one creates a genuine gap.

| Item | Required fact | Where checked |
|---|---|---|
| Sifting convention | \(P(z)=\prod_{p<z}p\); Iwaniec's \(p\le z\) survivors form a subset | (2.2) |
| Small-prime split | \(w<z\) uniformly | (3.2) and (1.2) |
| Beta fundamental lemma | \(\log E/\log w\ge30\), then \(\delta\) smaller for the desired error | (3.2), (3.7) |
| Linear parity threshold | \(s=\log D/\log z>2\) by a fixed margin | (3.6) |
| Vector minorant | Use \(L^-B^+-L^+(B^+-B^-)\), not a product of lower bounds | (3.3)--(3.7) |
| Coefficient hypotheses | \(|\alpha_r^-|\le3\), support \(r\le DE\) | Section 3 |
| Proposition 5.1 support | \(DE=X^L\le X^{1-c_\varepsilon}\) | (3.1) |
| Well-factorability | Finite sum of bounded convolutions at the chosen split; retain \(X^\nu\) slack | (4.2)--(4.3) |
| Raw Type II range | Use Lemma 5.4, not the \(H\le X^{1/60}\) corollary | (2.1), (4.5)--(4.8) |
| Every monomial | Both terms inside braces and \((MQ)^2\) are dominated | (4.6) |
| Shift weight | \(H-|k|\) costs one factor \(H\) | (4.9) |
| Diagonal pieces | Matomäki's (49) and (69) remain uniform for fixed new ratios | (4.10) |
| Decomposition error | \(H^3(\log X)^3\) is below \(XH/\log X\) | (4.11) |
| Smooth localization | An \(O(1)\) family covers the enlarged shell | (4.12) |
| Empty-interval polarity | Empty implies \(\mathcal E_z\le-HA_z\) | (3.9), (5.1) |
| Gap ceiling | \(z^2\le X^{d-\varepsilon}\) | (6.3) |
| Boundary gaps | Included in the enlarged-shell empty-start sets | (6.1)--(6.3) |
| Layer cake | \(g^2=2\int_0^g(g-H)\,dH\) | (6.4) |
| Scope | Rough gaps only; no prime-gap or zeta-strip conclusion | after (1.4) |

## 10. Reproducibility

Run

```text
python3 results/verify_rough_gap_second_moment_frontier.py
```

The checker uses exact rational arithmetic to replay every monomial in
(2.1), verifies the saving \(197/3600\) in the fixed-level corollary,
checks representative members of the moving-level family including
factor-support slack, and derives the optimizer \(3/16\).  It deliberately
does not claim to certify the imported analytic theorems.

The earlier project-band ledger remains independently replayable with

```text
python3 results/verify_zeta23_matomaki_rough_gap_gate.py
```

## References

1. W. Banks, K. Ford, and T. Tao, *Large prime gaps and probabilistic
   models*, Invent. Math. **233** (2023), 1471--1518.
   [doi:10.1007/s00222-023-01199-0](https://doi.org/10.1007/s00222-023-01199-0).

2. J. B. Friedlander, *Sifting short intervals*, Math. Proc. Cambridge
   Philos. Soc. **91** (1982), 9--15.
   [doi:10.1017/S0305004100059065](https://doi.org/10.1017/S0305004100059065).

3. J. B. Friedlander, *Sifting short intervals II*, Math. Proc. Cambridge
   Philos. Soc. **92** (1982), 381--384.
   [doi:10.1017/S0305004100060084](https://doi.org/10.1017/S0305004100060084).

4. J. B. Friedlander, *Moments of sifted sequences*, Math. Ann. **267**
   (1984), 101--106. [EuDML full record and scan](https://eudml.org/doc/163883).

5. J. B. Friedlander and H. Iwaniec, *Opera de Cribro*, American
   Mathematical Society Colloquium Publications **57**, 2010; especially
   Section 12.7.

6. A. Gafni and T. Tao, *Rough numbers between consecutive primes*,
   arXiv:2508.06463 (2025), revised 2026.
   [arXiv](https://arxiv.org/abs/2508.06463).

7. O. Gorodetsky, *The variance of integers without small prime factors in
   short intervals*, Math. Z. **308** (2024), article 59.
   [doi:10.1007/s00209-024-03601-w](https://doi.org/10.1007/s00209-024-03601-w).

8. M. N. Huxley, *Irregularity in sifted sequences*, J. Number Theory
   **4** (1972), 437--454.
   [doi:10.1016/0022-314X(72)90035-2](https://doi.org/10.1016/0022-314X(72)90035-2).

9. H. Iwaniec, *A new form of the error term in the linear sieve*, Acta
   Arith. **37** (1980), 307--320.
   [doi:10.4064/aa-37-1-307-320](https://doi.org/10.4064/aa-37-1-307-320).

10. H. Iwaniec, *On the problem of Jacobsthal*, Demonstratio Math. **11**
    (1978), 225--232.
    [doi:10.1515/dema-1978-0121](https://doi.org/10.1515/dema-1978-0121).

11. K. Matomäki, *Almost primes in almost all very short intervals*, J.
    London Math. Soc. (2) **106** (2022), 1061--1097.
    [doi:10.1112/jlms.12592](https://doi.org/10.1112/jlms.12592),
    [arXiv:2012.11565](https://arxiv.org/abs/2012.11565).

12. J. B. Friedlander, *Sifting short intervals*, contribution to
    *Analytic Number Theory*, Oberwolfach Rep. **5** (2008), 690--691;
    Proposition 2.
    [doi:10.4171/OWR/2008/14](https://doi.org/10.4171/OWR/2008/14).
