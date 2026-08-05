# Guide to the exact positivity certificates

Status: human-facing guide to the formal certificate layer, 2026-08-05.

This document explains the mathematics represented by the large generated
Lean files.  The generated integers are proof witnesses, not the mathematical
idea.  The reusable argument is short: prove a shifted midpoint positive by
an exact congruence, spend that shift as an error budget, and—when an
infinite-dimensional conclusion is wanted—combine the certified finite block
with separate complement and cross estimates.

The principal reusable files are
[`CertFramework.lean`](../lean/weilcert/CertFramework.lean) and
[`FullInfTransfer.lean`](../lean/weilcert/FullInfTransfer.lean).  The
prime-5 instance is
[`Prime5Rescue12.lean`](../lean/weilcert/Prime5Rescue12.lean), with its public
axiom audit in
[`Prime5Rescue12Audit.lean`](../lean/weilcert/Prime5Rescue12Audit.lean).

## 1. The mathematical reduction

Let $A$ be an $n\times n$ scaled midpoint matrix.  An exact certificate
supplies matrices $W,W_i$, positive diagonal entries $g_k$, scalars
$c,f\ne0$, and a margin $s$, satisfying

$$
c^2(A-sI)=W^{\mathsf T}\operatorname{diag}(g)W,
\qquad W_iW=fI.
$$

The second identity makes $W$ injective: if $Wx=0$, then
$fx=W_iWx=0$, hence $x=0$.  Therefore, for every $x\ne0$,

$$
c^2x^{\mathsf T}(A-sI)x
  =\sum_k g_k (Wx)_k^2>0.
$$

Thus $x^{\mathsf T}Ax>s\lVert x\rVert_2^2$ for every nonzero $x$.  No
eigenvalue routine or floating-point factorization is trusted in this step:
the displayed identities are exact field identities checked by Lean.

Now let $M$ be the real or rational matrix of interest, and suppose

$$
\left|M_{ij}-\frac{A_{ij}}{\mathit{scale}}\right|\le\delta
\quad\text{for every }i,j,
\qquad \mathit{scale}>0.
$$

For $E=\mathit{scale}M-A$, the elementary estimate

$$
|x^{\mathsf T}Ex|
 \le n\,\mathit{scale}\,\delta\,\lVert x\rVert_2^2
$$

follows from the triangle inequality and
$(\sum_i|x_i|)^2\le n\sum_i x_i^2$.  Consequently the exact shifted
positivity survives every allowed perturbation whenever

$$
n\,\mathit{scale}\,\delta\le s.
$$

This is `CertFramework.cert_window_positive`.  The structure
`CertFramework.LDLPosCertificate` packages the exact data, and
`LDLPosCertificate.sound` is the same implication through a smaller public
interface.

The estimate is intentionally conservative.  An operator-norm enclosure can
be sharper, but the entrywise bound is simple, basis-explicit, and easy to
certify using rational interval endpoints.

## 2. A hand-checkable two-dimensional instance

The mechanism can be understood without reading any generated constant.  The
existing non-RH example in
[`CurveCertE5.lean`](../lean/weilcert/CurveCertE5.lean) uses

$$
G=\begin{pmatrix}10&-15\\-15&50\end{pmatrix},\qquad
s=4,\qquad
G-sI=\begin{pmatrix}6&-15\\-15&46\end{pmatrix}.
$$

Take

$$
W=\begin{pmatrix}6&-15\\0&1\end{pmatrix},\quad
W_i=\begin{pmatrix}1&15\\0&6\end{pmatrix},\quad
g=(6,306),\quad c=f=6.
$$

Direct multiplication gives

$$
W_iW=6I,
\qquad
W^{\mathsf T}\operatorname{diag}(6,306)W
  =36(G-4I).
$$

Both diagonal weights are positive, so $G-4I$ is positive definite.  If
every entry of a rational $2\times2$ matrix $M$ differs from the
corresponding entry of $G$ by at most $2$, the perturbation loss is at
most

$$
n\delta\lVert x\rVert_2^2=2\cdot2\lVert x\rVert_2^2
  =4\lVert x\rVert_2^2.
$$

That exactly fits the stored margin.  Hence $x^{\mathsf T}Mx>0$ for every
nonzero rational vector $x$.  This is
`CurveCertE5.curve_window_positive`.  The example is useful because every
certificate identity fits on a page; its separate interpretation in terms of
a curve is not needed to verify the positivity mechanism.

## 3. What the generated prime-5 file proves

`Prime5Rescue12.lean` stores two 12-dimensional midpoint intervals at
$L=327/100$: a `Full` interval and an `Old` interval.  It also stores one
exact vector $v$.  Its public theorem `finitePrime5Rescue` takes arbitrary
real matrices `Full` and `Old` together with explicit proofs that their
entries lie in those intervals.  It concludes all three of the following:

1. $x^{\mathsf T}\mathrm{Full}\,x>0$ for every $x\ne0$;
2. $v^{\mathsf T}\mathrm{Old}\,v<0$;
3. $v^{\mathsf T}(\mathrm{Full}-\mathrm{Old})v>0$.

The first conclusion uses the exact congruence and the generic window
theorem.  The other two use exact midpoint evaluations plus the same
entrywise perturbation estimate.  In particular, the theorem is robust over
the entire stored boxes; it is not merely a floating-point sign at their
centres.

The name “prime-5 rescue” records the external analytic construction of the
two intervals.  Lean proves the three displayed matrix statements from
interval containment.  It does **not** prove inside this module that the
stored matrices are Legendre matrices of a Weil form or that their difference
is precisely a prime-5 contribution.  Those are model-identification and
interval-enclosure obligations outside the generated certificate.

## 4. How generated data enter the proof

The generator performs a search and emits exact integers for $A,W,W_i,g$
and the witness vector.  The resulting Lean file then asks the kernel to
verify, among other things,

- the congruence $c^2(A-sI)=W^{\mathsf T}\operatorname{diag}(g)W$;
- the inverse witness $W_iW=fI$;
- positivity of every $g_k$ and nonvanishing of $c,f$;
- the exact quadratic-form values of the stored witness; and
- the rational inequalities showing that the perturbation budgets fit.

This gives the generator a limited role.  A faulty generator can emit data
that fail to compile, or data proving an irrelevant statement, but it cannot
make a false exact identity pass Lean's kernel.  Human review must therefore
focus on the semantic interfaces: what matrix the constants are meant to
represent, how its interval was enclosed, and whether the formal conclusion
matches the paper's claim.

Large integer witnesses remain in a separate generated module.  They should
not be copied into a manuscript proof.  A paper should state the generic
soundness theorem, the interval and margin parameters, the final signs, and a
hash or path identifying the machine-readable witness.

## 5. From a finite certificate to a full-space estimate

A finite positive matrix is not automatically a positive operator.  Suppose
an orthogonal decomposition writes $h=u+w$, with $u$ in a certified
finite subspace and $w$ in its orthogonal complement.  For a symmetric
bilinear form $B$, assume independently that

$$
B(u,u)\ge\beta\lVert u\rVert^2,
\quad B(w,w)\ge d\lVert w\rVert^2,
\quad |B(u,w)|\le c\lVert u\rVert\lVert w\rVert.
$$

Then

$$
B(h,h)\ge
\beta\lVert u\rVert^2+d\lVert w\rVert^2
 -2c\lVert u\rVert\lVert w\rVert.
$$

The best universal coefficient obtained from these three bounds is the
smaller eigenvalue

$$
\lambda_{-}=
\frac{\beta+d-\sqrt{(\beta-d)^2+4c^2}}{2}.
$$

`CertFramework.two_by_two_lower_bound_optimal` proves the scalar inequality
and `twoBlockLowerEigenvalue_isGreatest` proves its optimality.
`FullInfTransfer.starProjection_lower_bound_optimal` transports it through a
canonical orthogonal projection.

This transfer theorem is reusable and exact, but conditional.  The finite
certificate supplies at most the $\beta$ estimate.  Complement coercivity
$d$ and cross control $c$ are independent analytic theorems; generated
finite data cannot replace them.  Positivity follows from this route only
when $\lambda_{-}>0$, equivalently under the familiar strict conditions
$\beta>0$, $d>0$, and $c^2<\beta d$.

## 6. Trust and claim boundary

| Layer | What is checked | What remains outside that layer |
|---|---|---|
| Generic certificate algebra | Exact congruence, injectivity argument, perturbation inequality, and soundness implication | Any concrete constants or analytic interpretation |
| Generated instance | Exact arithmetic identities and rational sign/margin checks for the stored data | Why those data represent the intended analytic matrix |
| Interval bridge | Entrywise containment of the intended matrix in the stored box | Normally an external interval computation unless separately formalized |
| Two-block transfer | The exact implication from finite, complement, and cross estimates to a global lower bound | Proofs of the three block estimates |
| Zeta interpretation | Nothing merely from the certificate modules | Explicit-formula normalization, form-domain identification, support-uniform estimates, and the RH equivalence |

The axiom audit for the reusable layer is
[`Weilcert/UpstreamAudit.lean`](../lean/weilcert/Weilcert/UpstreamAudit.lean).
The prime-5 audit prints the axioms of its five advertised endpoints.  In the
pinned environment these audits expose only Lean/mathlib's standard
foundational axioms; there are no project literature axioms in the certificate
soundness chain.  This foundational audit does not discharge the semantic
obligations in the last column of the table.

## 7. Precise nonclaims

The certificate layer does not prove any of the following:

- that a numerically proposed matrix is the matrix of the intended analytic
  form;
- that an interval computation used outward rounding correctly, unless that
  enclosure is itself formalized;
- positivity outside the named finite dimension and parameter window;
- positivity of an infinite-dimensional operator from Galerkin positivity
  alone;
- a support-uniform lower bound;
- the Guinand–Weil explicit formula or its normalization; or
- the Riemann Hypothesis.

It does prove something useful and sharply delimited: once entrywise
containment is supplied, exact finite positivity and the advertised witness
signs no longer depend on floating-point eigensolvers or on trusting a
certificate generator.

## 8. Minimal reproduction

From the repository root, the reusable theory and the hand-checkable example
can be checked serially with

```text
cd lean/weilcert
lake env lean CertFramework.lean
lake env lean FullInfTransfer.lean
lake env lean CurveCertE5.lean
lake env lean Weilcert/UpstreamAudit.lean
```

The generated prime-5 endpoint and its audit are checked with

```text
cd lean/weilcert
lake env lean Prime5Rescue12.lean
lake env lean Prime5Rescue12Audit.lean
```

The latter check is intentionally separate: it recompiles a generated exact
artifact and can require materially more time and memory than the generic
framework.
