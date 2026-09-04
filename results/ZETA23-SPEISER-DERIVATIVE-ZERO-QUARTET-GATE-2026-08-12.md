# The Speiser / derivative-zero route to a uniform strip

## Functional-equation quartets, logarithmic-derivative geometry, and a direct-method closure gate

**Date:** 2026-08-12  
**Question:** Can a zero \(\rho=\beta+i\gamma\) with \(\beta>1-\delta\) be converted, through the functional equation and the geometry of \(\zeta'\) or \(\xi'\), into a quantitatively forbidden critical-point configuration?  
**Verdict:** **No fixed \(\delta>0\) is proved by the presently available derivative-zero machinery.** Two parts of the hoped-for implication fail exactly:

1. a functional-equation quartet does **not** force an off-axis zero of the derivative of its completed factor; its three critical points can all lie on the critical axis;
2. Speiser's theorem and the Levinson--Montgomery refinement are global counting statements. Their \(O(\log T)\) boundary ledger, and even their far-left weighted density estimate, cannot exclude one arbitrarily sparse offending zero.

The useful outcome is a sharp pruning of the search space. A derivative-zero proof of a uniform strip now requires a genuinely new **per-zero quantitative Speiser theorem**, or a replication theorem turning one near-edge zero into more derivative zeros than the available density ledger permits. Quartet symmetry, Gauss--Lucas containment, and existing aggregate counts do not supply either mechanism.

---

## 1. Normalizations and the exact target

Write

\[
 \xi(s)=\frac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s),
 \qquad
 X(z)=\xi\!\left(\frac12+z\right).
\]

Then \(X\) is a real even entire function of order one:

\[
 X(-z)=X(z),\qquad X(\bar z)=\overline{X(z)}.
\]

If \(z_0=a+i\gamma\), with \(a\ne0\), is a zero, the functional equation and reality supply the quartet

\[
 \{a+i\gamma,-a+i\gamma,a-i\gamma,-a-i\gamma\}.
\]

A uniform strip would require a number \(\delta>0\), independent of \(\gamma\), such that every nontrivial zero satisfies

\[
 \delta\le \Re\rho\le1-\delta.
\]

Because one exceptional quartet is enough to destroy this conclusion, every successful density or critical-point argument must eventually exclude **one unit of multiplicity**, uniformly in height.

---

## 2. Exact quartet critical-point lemma

### Lemma 2.1 (a maximally displaced quartet has only axial critical points)

For \(a>0\) and \(\gamma>a\), let

\[
 Q_{a,\gamma}(z)
 =((z-i\gamma)^2-a^2)((z+i\gamma)^2-a^2).
\]

Its zeros are exactly the quartet \(\pm a\pm i\gamma\), while

\[
 Q'_{a,\gamma}(z)=4z\bigl(z^2+\gamma^2-a^2\bigr).
\]

Consequently its critical points are

\[
 z=0,qquad z=\pm i\sqrt{\gamma^2-a^2},
\]

and all lie on the critical axis \(\Re z=0\).

#### Proof

Direct multiplication gives

\[
 Q_{a,\gamma}(z)
 =z^4+2(\gamma^2-a^2)z^2+(\gamma^2+a^2)^2.
\]

Differentiating and using \(\gamma>a\) gives the asserted roots. \(\square\)

The critical point closest to the upper quartet has only a vertical displacement:

\[
 \gamma-\sqrt{\gamma^2-a^2}
 =\frac{a^2}{\gamma+\sqrt{\gamma^2-a^2}}
 =\frac{a^2}{2\gamma}+O\!\left(\frac{a^4}{\gamma^3}\right).
\]

Thus even when \(a\) is close to \(1/2\), the isolated completed quartet creates no horizontal derivative displacement at all.

### Corollary 2.2 (exact failure of the local quartet implication)

The implication

\[
 \text{off-axis functional-equation quartet}
 \quad\Longrightarrow\quad
 \text{off-axis critical point of its completed factor}
\]

is false. In particular, it cannot be repaired by optimizing \(a\), increasing \(\gamma\), or invoking the convex hull of the quartet.

This does **not** assert that the full \(X'\) has only axial zeros. If

\[
 X(z)=Q_{a,\gamma}(z)R(z),
\]

then

\[
 X'(z)=Q'_{a,\gamma}(z)R(z)+Q_{a,\gamma}(z)R'(z),
\]

so the rest of the divisor can move the critical points. The point is precisely that the motion is global and has no sign or minimum horizontal size supplied by the quartet.

### Same-height pair version

At height \(\gamma\), the horizontally reflected pair is modeled in the coordinate

\[
 w=s-\left(\frac12+i\gamma\right)
\]

by \(p(w)=w^2-a^2\). Its sole critical point is \(w=0\), again on the critical line. Hence even before conjugate completion, the most naive ``a pair creates a critical point between it'' argument lands on, rather than off, the critical line.

---

## 3. What Gauss--Lucas does and does not say

For a polynomial, Gauss--Lucas places every derivative zero in the convex hull of all zeros. It does not give the converse, assign a derivative zero to each pair or quartet, or lower-bound the distance of a derivative zero from a symmetry axis. Lemma 2.1 realizes the failure in the smallest functional-equation-symmetric example.

There are two further losses for \(X\):

1. The classical theorem is a polynomial theorem. One may apply it to carefully chosen symmetric canonical-product truncations and pass to locally convergent subsequences, but this still produces only global containment.
2. The convex hull coming from the unconditional critical strip is the same unbounded vertical strip one started with. It contains no improved fixed strip unless improved horizontal information about the zeros has already been inserted.

Thus a Gauss--Lucas limit argument has the wrong logical polarity for the present task:

\[
 \text{known location of all zeros}
 \Longrightarrow
 \text{containment of derivative zeros},
\]

whereas the desired proof would need a reverse, localized inference from a derivative constraint to each original zero.

There is also a general divisor warning. If \(P(z_0)\ne0\), then

\[
 F(z)=e^{cz}P(z),
 \qquad
 c=-\frac{P'(z_0)}{P(z_0)},
\]

has exactly the zeros of \(P\) but satisfies \(F'(z_0)=0\). Derivative zeros are not divisor-only data. For the actual \(\xi\) and \(\zeta\), the zero-free factors are of course fixed; the example identifies why those factors and the full global product cannot be discarded in a rigorous localization argument.

---

## 4. \(\xi'\) and \(\zeta'\) are different geometric problems

Set

\[
 H(s)=\frac12s(s-1)\pi^{-s/2}\Gamma(s/2),
 \qquad \xi(s)=H(s)\zeta(s).
\]

Away from zeros and poles,

\[
 \frac{\xi'}{\xi}(s)
 =\frac{H'}{H}(s)+\frac{\zeta'}{\zeta}(s).
\]

Therefore, at a point where \(\zeta(s)\ne0\),

\[
 \zeta'(s)=0
 \quad\Longleftrightarrow\quad
 \frac{\xi'}{\xi}(s)=\frac{H'}{H}(s),
\]

not \(\xi'(s)=0\). Speiser's theorem concerns \(\zeta'\), while the even quartet polynomial naturally models \(\xi'\). Passing silently between these two derivatives loses the gamma-factor field, whose size is of logarithmic order at height \(T\).

This distinction blocks the tempting chain

\[
 \text{quartet geometry for }\xi
 \Longrightarrow
 \text{a forbidden zero of }\zeta'.
\]

An additional quantitative estimate comparing the two logarithmic derivatives would be needed, including all other-zero contributions and the gamma factor with the correct sign.

---

## 5. The exact Speiser / Levinson--Montgomery ledger

Let

\[
 N^-(T)
 =\#\{\rho=\beta+i\gamma:\zeta(\rho)=0,
                 0<\gamma<T,\ 0<\beta<1/2\},
\]

and let \(N_1^-(T)\) be the analogous count for zeros of \(\zeta'\), with multiplicity. Levinson and Montgomery prove

\[
 N_1^-(T)=N^-(T)+O(\log T). \tag{5.1}
\]

They also prove that, unless \(N^-(T)>T/2\) for every sufficiently large \(T\), there is a sequence \(T_j\to\infty\) on which

\[
 N_1^-(T_j)=N^-(T_j). \tag{5.2}
\]

Their corollary is Speiser's equivalence:

\[
 \mathrm{RH}
 \quad\Longleftrightarrow\quad
 \zeta'(s)\ne0
 \text{ for }0<\Re s<1/2. \tag{5.3}
\]

These are powerful global statements, but they do not preserve horizontal depth or give a per-zero correspondence.

### Proposition 5.1 (one-unit obstruction)

Equation (5.1), by itself, cannot rule out a single functional-equation quartet at arbitrarily large height.

#### Proof

A right-hand zero \(\beta+i\gamma\), \(\beta>1/2\), supplies a reflected left-hand zero \(1-\beta+i\gamma\), changing \(N^-(T)\) by one unit of multiplicity after \(T\) passes \(\gamma\). For all sufficiently large \(T\),

\[
 1\le C\log T
\]

for the implicit constant in (5.1). Hence the error ledger admits that unit. Nothing in (5.1) locates the corresponding derivative zero, if any, at the same height or at comparable horizontal depth. \(\square\)

Even (5.2) does not fix this: equality of aggregate counts is not a bijection and does not say that a zero near \(\Re s=0\) produces a derivative zero near \(\Re s=0\).

### The available forbidden region is on the wrong side

Levinson--Montgomery Theorem 9 proves that for \(n\ge2\) there is one real zero of \(\zeta'\) in \((-2n,-2n+2)\), and there are no other zeros of \(\zeta'\) in \(\Re s<0\). Thus nonreal derivative zeros are indeed forbidden to the left of zero.

But Speiser supplies only a zero somewhere in

\[
 0<\Re s<1/2,
\]

which is an allowed region. Existing Speiser theory does not say that a reflected zero with \(\Re\rho=\varepsilon\) produces a \(\zeta'\)-zero with real part \(\le0\), or even with real part \(O(\varepsilon)\).

### Why the theorem is qualitative

The proof uses the sign of \(\Re(\zeta'/\zeta)\) on the vertical boundaries of the left half-strip and an argument-principle calculation. The \(O(\log T)\) term in (5.1) comes from horizontal-boundary changes of argument. Topological degree records a net count; it does not retain the distance of the responsible zero from a vertical boundary.

---

## 6. Short intervals and far-left derivative-density bounds still admit one

Levinson--Montgomery also obtain short-interval clustering for intervals of length \(U>T^{1/2}\). Their Theorem 6 gives, for \(U=T^a\), \(1/2<a\le1\), and \(\delta>C/\log T\), a bound of the form

\[
 \sum_{\substack{T<\gamma'<T+U\\
                  \beta'<1/2-\delta}}
 \left(\frac12-\delta-\beta'\right)
 \ll
 (1+\delta\log U)^2
 U^{1-\delta(2-1/a)/4}. \tag{6.1}
\]

For fixed \(0<\delta<1/2\), the power of \(T\) on the right is

\[
 a\left[1-\frac{\delta}{4}\left(2-\frac1a\right)\right]
 =a-\frac{\delta}{4}(2a-1)>0. \tag{6.2}
\]

Indeed \(0<2a-1\le1\), so the subtracted term in the final expression in (6.2) is less than \(1/8\), while \(a>1/2\). Hence the upper bound in (6.1) tends to infinity (up to logarithmic factors) and does not exclude even one derivative zero of fixed positive depth.

This establishes an exact quantitative gate:

> Existing far-left \(\zeta'\)-density estimates are compatible with a sparse sequence containing one fixed-depth derivative zero in widely separated long intervals.

Shrinking the interval to isolate a candidate is not available in this theorem: the proof requires \(U>T^{1/2}\). Increasing the derivative order does not repair the logical issue; aggregate derivative-zero clustering remains compatible with isolated exceptions, and it supplies no inverse map back to an individual \(\zeta\)-zero.

---

## 7. Local logarithmic-derivative geometry: the missing uniform estimate

Near a simple zero \(\rho\), write

\[
 \frac{\zeta'}{\zeta}(s)
 =\frac1{s-\rho}+A_\rho(s), \tag{7.1}
\]

where \(A_\rho\) is analytic only on a disk containing no other zero or pole. A nearby zero of \(\zeta'\) would satisfy

\[
 \frac1{s-\rho}+A_\rho(s)=0. \tag{7.2}
\]

If one had a uniform disk and a stable approximation

\[
 A_\rho(s)=A_\rho(\rho)+o(|A_\rho(\rho)|),
\]

Rouche's theorem would suggest a critical point near

\[
 s=\rho-\frac1{A_\rho(\rho)}. \tag{7.3}
\]

At height \(T\), the regular background commonly has logarithmic scale, suggesting a displacement of order \(1/\log T\). This heuristic does not close uniformly, for three independent reasons:

1. **No uniform isolation radius.** Zeros may be arbitrarily close or multiple; no unconditional separation estimate applies to every candidate.
2. **The remainder is global.** \(A_\rho\) contains the other nontrivial zeros, the pole/trivial-zero terms, and the gamma-factor contribution. It has no candidate-independent one-sided bound strong enough for (7.3).
3. **The target region is still legal.** Even a displacement \(O(1/\log T)\) from a reflected zero at \(\Re\rho=\varepsilon\) need not cross \(\Re s=0\), and Speiser's allowed region extends all the way from zero to \(1/2\).

If \(\rho\) has multiplicity \(m\ge2\), then \(\zeta'\) has multiplicity \(m-1\) at \(\rho\). This is a precise per-zero statement, but it creates a derivative zero at an allowed point and gives no contradiction.

The missing input can therefore be stated cleanly.

### Required new lemma A (quantitative per-zero Speiser map)

There would have to exist fixed constants \(\delta,c>0\) and a controlled height window such that every zero

\[
 \rho=\beta+i\gamma,\qquad \beta>1-\delta,
\]

forces a zero \(\rho'\) of \(\zeta'\) satisfying a quantitatively forbidden condition, for example

\[
 \Re\rho'\le0,
\]

or a region excluded by some independent theorem. No such unconditional localization follows from (5.1)--(6.1).

### Required new lemma B (replication)

Alternatively, one offender would have to force at least \(M(T)\) distinct derivative zeros in a controlled box, with \(M(T)\) exceeding the best density upper bound there. Quartet symmetry supplies only a bounded number of original zeros, and existing argument-principle identities supply net counts rather than superconstant replication.

Without A or B, derivative-zero density is structurally mismatched to a uniform zero-free strip.

---

## 8. Interlacing, Laguerre--Polya, and canonical systems

Define the real entire function of a real variable

\[
 \Xi(t)=\xi\!\left(\frac12+it\right).
\]

Rolle's theorem interlaces zeros of \(\Xi'\) only between real zeros of \(\Xi\), i.e. zeros already on the critical line. An off-line quartet is a pair of nonreal conjugate roots in the \(t\)-plane and is invisible to ordinary real interlacing.

The converse inference is false in elementary form: a real polynomial may have only real critical points while retaining nonreal roots. Lemma 2.1 gives the symmetry-adapted version: the quartet polynomial has all of its critical points on the axis while all four roots are off it.

Stronger interlacing results require a hypothesis such as membership in the Laguerre--Polya class, or a Hermite--Biehler / de Branges inequality. For a real entire function of the relevant genus, Laguerre--Polya membership already encodes real-rootedness. Likewise, a positive canonical system producing the needed Hermite--Biehler function would supply essentially the missing spectral positivity. Invoking such an interlacing principle without proving its positivity hypothesis independently is circular for RH and does not yield a weaker uniform strip for free.

The same warning applies to ``self-adjoint critical-point'' heuristics: self-adjointness can force a real spectrum only after the operator/domain/positive Hamiltonian has been constructed. The zeta functional equation alone is not that construction.

---

## 9. Exact closure gate for the audited proof package

Consider the package of inputs

\[
 \mathcal P={
 \text{functional-equation quartet symmetry},
 \text{Gauss--Lucas containment},
 \text{Speiser equivalence},
 \text{(5.1)},
 \text{(6.1)}
 \}.
\]

The following conclusions are exact.

### Proposition 9.1 (audited-package closure gate)

The two closure mechanisms furnished by \(\mathcal P\)—a forbidden derivative-zero location or a contradiction with a derivative-zero count—do not establish an unconditional fixed zero-free strip without an additional per-zero localization or replication input.

#### Proof

There are two necessary transitions.

1. To obtain a geometric contradiction from the completed quartet, one must force a derivative zero away from the critical axis or into a forbidden region. Lemma 2.1 is an exact counterexample to that transition at the quartet-factor level, while Gauss--Lucas adds only containment.
2. To obtain a counting contradiction from Speiser, one must make one reflected zero exceed the available derivative-zero ledger. It contributes one unit. Formula (5.1) has an unbounded \(O(\log T)\) error, and the right side of (6.1) grows as a positive power of \(T\) for fixed \(\delta\). Both ledgers admit that unit.

Neither branch closes the quantifier ``for every zero at every sufficiently large height.'' \(\square\)

This is a closure audit for the specified proof package, not a formal logical-independence theorem and not a theorem that all derivative-zero approaches are impossible. A new theorem of type A or B in Section 7 would enlarge the package and could change the verdict.

---

## 10. Search-space decision table

| Proposed implication | Status | Reason |
|---|---:|---|
| Off-axis quartet \(\Rightarrow\) off-axis zero of its completed derivative | **False** | Lemma 2.1 |
| Gauss--Lucas \(\Rightarrow\) a critical point assigned to each quartet | **False** | One-way global containment only |
| \(\xi'(s)=0\) and \(\zeta'(s)=0\) are interchangeable | **False** | Gamma/pole factor in Section 4 |
| Existence of any off-line zeta zero \(\Rightarrow\) existence of some \(\zeta'\)-zero left of \(1/2\) | **Yes, only as a global existential statement** | Speiser equivalence; no assignment to that zero |
| The forced \(\zeta'\)-zero has comparable height and horizontal depth | **Not known from these inputs** | No per-zero map in (5.1) |
| \(N_1^-(T)=N^-(T)+O(\log T)\) excludes one offender | **No** | One-unit obstruction |
| Existing far-left weighted density excludes one fixed-depth \(\zeta'\)-zero | **No** | RHS of (6.1) grows polynomially |
| Rolle / real interlacing sees off-line quartets | **No** | It applies only to real zeros in the \(t\)-plane |
| Laguerre--Polya / de Branges interlacing is available unconditionally | **No** | Required positivity is essentially the missing theorem |
| A fixed zeta zero-free strip follows | **Not proved** | Necessary quantifier does not close |

---

## 11. Most promising derivative-zero subproblem

If this route is pursued further, the highest-value target is not another global density estimate. It is a **depth-sensitive, height-local Speiser theorem**. A useful prototype would bound a transport cost rather than merely a count:

\[
 \sum_{\substack{\zeta'(\rho')=0\\
                  |\Im\rho'-\gamma|\le L(T)}}
 \Phi\!\left(\frac12-\Re\rho'\right)
 \ \ge\ 
 \Psi\!\left(\frac12-\Re(1-\bar\rho)\right)-E(T),
\]

where \(E(T)=o(1)\) for one fixed-depth offender, or where the left side is independently \(<\Psi(1/2-\varepsilon)\). The present argument-principle error \(O(\log T)\) has the opposite scale.

Any proposed lemma should be hostile-tested against:

- the exact quartet polynomial in Lemma 2.1;
- arbitrarily close and multiple zeros;
- the distinction between \(\xi'\) and \(\zeta'\);
- a single sparse offender rather than a positive-density family;
- horizontal-boundary argument errors;
- the fact that \(0<\Re s<1/2\) is not a forbidden region for \(\zeta'\).

Until one of these tests is overcome quantitatively, the derivative-zero route is a diagnostic equivalence for RH, not a proof of a fixed strip.

---

## References

1. N. Levinson and H. L. Montgomery, *Zeros of the derivatives of the Riemann zeta-function*, **Acta Mathematica 133** (1974), 49--65. [DOI](https://doi.org/10.1007/BF02392141); [archival PDF](https://archive.ymsc.tsinghua.edu.cn/pacm_download/117/6174-11511_2006_Article_BF02392141.pdf).
2. A. Speiser, *Geometrisches zur Riemannschen Zetafunktion*, **Mathematische Annalen 110** (1935), 514--521. Speiser's equivalence is also stated and proved through the counting theorem in Reference 1.

## Final binary verdict

\[
 \boxed{\text{UNCONDITIONAL FIXED STRIP FROM THIS ROUTE: NOT PROVED.}}
\]

What has been proved here is the exact obstruction: isolated quartet geometry can place all completed critical points on the axis, and every audited unconditional \(\zeta'\) ledger is too coarse to reject one sparse fixed-depth event.
