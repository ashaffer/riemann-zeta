# Reciprocal-translate tangent normal form and near-square gate

## Verdict

The proposed estimate

\[
 \sup_{h\ne0}|A_W\cap(A_W-h)|
 \ll q^{o(1)}\left(W^{1/2}+\frac{W^2}{q}\right)
 \tag{RTI}
\]

was **not proved or refuted** in this sprint.  What was proved is an exact,
lossless reduction of every translated pair to a primitive tangent coordinate
system.  It does three useful things:

1. it proves that the `sqrt(W)` term is necessary, by an explicit family;
2. it proves the desired bound on each fixed primitive tangent line;
3. it identifies the only remaining issue: a masked near-square count while the
   primitive direction varies.  Summing the fixed-line estimates without that
   arithmetic input can lose as much as a factor comparable with `h`.

Thus (RTI) remains a genuine theorem, not a consequence of an elementary
divisor estimate already present in the project.

The exact reductions and finite hostile sweeps are implemented in
`src/qp_reciprocal_translate_intersection.py`, with nine focused tests in
`src/test_qp_reciprocal_translate_intersection.py`.  The polynomial identities
are also independently certified by Lean in
`lean/weilcert/QPReciprocalTranslateNormalForm.lean`.

## 1. Setup

Write the central integer as `M` to avoid confusing it with dyadic constants.
Suppose

\[
 an=M+e,\qquad (a+h)m=M+f,\qquad |e|,|f|\le W,
 \tag{1}
\]

where `a,n,m` are positive integers of size comparable with `q`, `h>0`, and
`2W<min(a,a+h)`.  The latter condition makes the quotient attached to each
denominator unique.  Put

\[
 k=n-m,\qquad X=2a+h,\qquad Y=n+m.
\tag{2}
\]

In the dyadic reciprocal box, `k` is positive and comparable with `h`.

## 2. Exact midpoint identities

Direct expansion gives

\[
 Xk-Yh=2(e-f),
 \tag{3}
\]

and

\[
 XY-hk-4M=2(e+f).
 \tag{4}
\]

Conversely, if `X,Y,h,k` have the parities needed to make

\[
 a=\frac{X-h}{2},\qquad
 n=\frac{Y+k}{2},\qquad
 m=\frac{Y-k}{2}
\tag{5}
\]

integral, then (3)--(4) reconstruct `e,f` and hence (1).  In particular,
translated reciprocal pairs are in exact bijection with the parity-restricted
integer points satisfying

\[
 \boxed{
 |XY-hk-4M|+|Xk-Yh|\le 4W.}
 \tag{6}
\]

This is the cleanest formulation of the residual theorem.  The first term is
radial displacement from the midpoint hyperbola; the second is failure of the
chord `(h,-k)` to be tangent.

## 3. Primitive tangent normal form

Write

\[
 h=gs,\qquad k=gr,\qquad (r,s)=1,
\tag{7}
\]

and define

\[
 T=rX+sY,\qquad Z=rX-sY.
\tag{8}
\]

Then

\[
 gZ=2(e-f)
\tag{9}
\]

and

\[
 T^2-Z^2-4rs(4M+g^2rs)=8rs(e+f).
\tag{10}
\]

The integer-coordinate masks are exactly

\[
 T+Z\equiv0\pmod{2r},\qquad
 T-Z\equiv0\pmod{2s},
\tag{11}
\]

since `(T+Z)/(2r)=X` and `(T-Z)/(2s)=Y`.

Using

\[
 \max(|e|,|f|)=\frac{|e+f|+|e-f|}{2},
\]

the two window inequalities in (1) are equivalent to the single exact diamond

\[
\boxed{
 \left|T^2-Z^2-4rs(4M+g^2rs)\right|
 +4grs|Z|\le16rsW.}
\tag{12}
\]

No triangle inequality or loss was used in obtaining (12).

## 4. The `sqrt(W)` obstruction is real and sharp

Take `M=Q^2`.  For integers `t>=0`, let

\[
 a=Q+t,\quad n=Q-t,\quad m=Q-t-h.
\]

Then

\[
 an-Q^2=-t^2,
 \qquad
 (a+h)m-Q^2=-(t+h)^2.
\]

Consequently every

\[
 0\le t\le \lfloor\sqrt W\rfloor-h
\]

lies in the translate intersection.  Hence, already for fixed small `h`,

\[
 |A_W\cap(A_W-h)|\ge \lfloor\sqrt W\rfloor-h+1.
\tag{13}
\]

This is a literal tangent parabola: along the lattice tangent direction, the
first nonzero product error is quadratic.  Any valid uniform theorem must retain
the `sqrt(W)` term.

## 5. A fixed tangent line satisfies the target bound

Fix `g,r,s,T`.  From (12), every admissible `Z` satisfies

\[
 |Z^2-B|\le16rsW
\tag{14}
\]

for the fixed real number

\[
 B=T^2-4rs(4M+g^2rs).
\]

The set of real `Z` satisfying (14) is the union of at most two intervals whose
total length is `O(sqrt(rs W))`.  Meanwhile (11) implies that the difference of
any two admissible `Z` values is divisible by

\[
 \operatorname{lcm}(2r,2s)=2rs.
\]

Therefore a fixed primitive tangent line contributes

\[
 \boxed{O\!\left(1+\sqrt{\frac{W}{rs}}\right)}.
\tag{15}
\]

This is the desired local square-root law.  It is uniform in all complex or
adversarial selections because it is a cardinality statement, not an average.

## 6. Exact tangent centers have only divisor multiplicity

At an exact center, `Z=0` and equality holds in the central conic:

\[
 T^2=4rs(4M+g^2rs).
\tag{16}
\]

The masks (11) force `T=2rs d` for an integer `d`.  Thus

\[
 rs(d-g)(d+g)=4M.
\tag{17}
\]

For integral `M`, the number of exact central tuples is at most a fixed divisor
function of `4M`, hence `M^{o(1)}`.  This proves that the exact major arcs are
harmless.  It does **not** count all near centers: the error window allows `T`
to miss (16), and that moving near-square problem is the unresolved part.

## 7. The remaining near-square gate

Equation (12) first gives

\[
 |Z|\le \frac{4W}{g}.
\tag{18}
\]

Since `r` and `s` are comparable in the dyadic box and `T` is of size
`q sqrt(rs)`, it also gives

\[
 \left|T-2\sqrt{rs(4M+g^2rs)}\right|
 \ll
 \frac{\sqrt{rs}\,W}{q}
 +\frac{W^2}{g^2q\sqrt{rs}}.
\tag{19}
\]

For a single `(g,r,s)`, (19) leaves at most one integer `T` in much of the
application range.  The problem is that the existence of that one integer cannot
be summed trivially over all reduced directions.  Since `gs=h` and `r` ranges
over a constant-factor interval around `s`, the naive leading term is

\[
 \sum_{s\mid h}\ \sum_{r\asymp s,(r,s)=1}1,
\]

which can be as large as `h q^{o(1)}`.

The precise missing theorem is a **masked, varying-direction near-square
large sieve**: after imposing (11), (18), and (19), prove that the sum of the
fixed-line multiplicities (15) is

\[
 \ll q^{o(1)}\left(\sqrt W+\frac{W^2}{q}\right).
\tag{20}
\]

Dropping the masks loses the arithmetic that makes the exact-center
factorization (17) possible.  Dropping `T` and retaining only the scalar
correlation also loses the fixed-line square-root spacing.  This explains why
the earlier scalar inverse attempts did not settle the translate theorem.

General results on points near parabolas confirm that square factors and major
arcs must be separated, but do not directly prove (20) because the modulus and
primitive direction co-vary here; see Huang--Li,
[On two lattice points problems about the parabola](https://arxiv.org/abs/1902.06047).

## 8. Application exponents

In the widest projected range,

\[
 q=D^{33/16},\qquad W=DU\le D^{7/6}=q^{56/99}.
\]

The conjectured two terms become

\[
 \sqrt W\le D^{7/12},
 \qquad
 \frac{W^2}{q}\le D^{13/48}.
\]

Thus the tangent term dominates and is exactly on the scale needed by the
weighted reciprocal-strip argument.  The exponent ledger is favorable; the
unproved content is entirely the global near-square summation (20).

## 9. Finite hostile sweeps

The target-sweep routine enumerates product-pair intervals and sweeps every
integer target in `[Q^2-3Q,Q^2+3Q]`; it does not sample target values.  Maximizing
over shifts `1<=h<=20` gave:

| `Q` | `W=floor(Q^0.57)` | largest intersection | attaining `h` | ratio to `sqrt(W)` |
|---:|---:|---:|---:|---:|
| 500 | 34 | 20 | 4 | 3.4300 |
| 1,000 | 51 | 23 | 2 | 3.2206 |
| 2,000 | 76 | 29 | 12 | 3.3265 |
| 5,000 | 128 | 43 | 4 | 3.8007 |
| 10,000 | 190 | 49 | 12 | 3.5548 |

These searches find the expected tangent clusters and no super-square-root
family.  They are evidence, not a proof of (20).

## 10. Honest handoff

What is now rigorous:

- the midpoint bijection (3)--(6);
- the primitive normal form and exact diamond (7)--(12);
- the sharp tangent lower bound (13);
- the fixed-line upper bound (15);
- the divisor classification of exact tangent centers (17);
- the application exponent ledger and exhaustive finite fixtures.

Mechanical verification completed successfully:

```text
lake env lean QPReciprocalTranslateNormalForm.lean
# no errors

python3 -m pytest -q src/test_qp_reciprocal_translate_intersection.py
9 passed
```

What is not rigorous because it is not yet known:

- the masked near-square direction sum (20);
- consequently, the full reciprocal translate-intersection theorem (RTI);
- consequently, any global four-cycle conclusion that uses (RTI) as an input.

The next serious attack should work on (20) in the `(T,Z,r,s,g)` variables,
preserving both CRT masks.  A quadratic large sieve or complete Gauss-sum
argument is structurally appropriate; an unrestricted scalar maximum-degree
argument is not.
