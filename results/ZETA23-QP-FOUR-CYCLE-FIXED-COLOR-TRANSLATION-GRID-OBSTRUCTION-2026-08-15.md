# ZETA23 QP four-cycle: fixed-color translation-grid obstruction

Date: 2026-08-15

## 1. Result

The proposed fixed-color completion estimate

\[
 m(C)\ \ll\ \left(1+\frac{D}{|\det C|}\right)(\log q)^{O(1)}       \tag{1.1}
\]

is false for the full-integer shell.  There is an exact infinite
translation-grid construction with

\[
 m(C)\asymp \sqrt D,\qquad |\det C|\asymp D.                       \tag{1.2}
\]

Thus the left side of (1.1) grows like `q^(8/33)`, while its proposed
right side is only polylogarithmic.

This is **not** a prime-power counterexample.  It rules out an integer-shell
lemma as the route to the actual four-cycle bound; it does not rule out an
estimate exploiting prime-power support.

---

## 2. Exact construction

Fix integers `R>S>0` and put

\[
 \alpha=2(R^2S)^{1/3}.
\]

Assume `R^2 S` is not a cube and that

\[
 e^{-w}< (S/R)^{2/3}<1<(R/S)^{1/3}<e^w.                            \tag{2.1}
\]

For example, `R=8,S=7` works for `w=0.2`.  Take a continued-fraction
convergent `q/n` to `alpha`.  Infinitely many convergent numerators `q` are
odd: two consecutive numerators cannot both be even.  Along that odd
subsequence,

\[
 |q-\alpha n|<1/n,
 \qquad |q^3-8R^2Sn^3|\ll q.                                     \tag{2.2}
\]

Set

\[
 A=Rn,\qquad C=Sn.
\]

For positive integers `ell` and translations `t`, define

\[
\begin{aligned}
 a_i(t)&=A+Ri\ell+t,\\
 b_j(t)&=A+Rj\ell-t,\\
 c_{ij}&=C-S(i+j)\ell,
 \qquad i,j\in\{0,1\}.
\end{aligned}                                                     \tag{2.3}
\]

Every `t` uses the same color matrix

\[
 \begin{pmatrix}
 C&C-S\ell\\
 C-S\ell&C-2S\ell
 \end{pmatrix},
 \qquad k:=\det C=-S^2\ell^2.                                    \tag{2.4}
\]

The cancellation behind the construction is

\[
 RC=SA.                                                           \tag{2.5}
\]

Writing `P_ij(t)=a_i(t)b_j(t)c_ij`, the exact increment from `A^2 C`
is

\[
\begin{aligned}
P_{ij}(t)-A^2C
={}&-R^2Sn\ell^2(i+j+ij)-2R^2S\ell^3ij\\
&+\bigl(R(j-i)\ell t-t^2\bigr)
  \bigl(Sn-S(i+j)\ell\bigr).                                    \tag{2.6}
\end{aligned}
\]

In particular, there is no term of size `q*ell`.

Let

\[
 B=(q/2)^{50/33},\qquad D=Uq^2/B\asymp q^{16/33}.                 \tag{2.7}
\]

Choose

\[
 \ell=\lfloor\epsilon\sqrt D\rfloor,
 \qquad |t|\le \lfloor\epsilon\sqrt D\rfloor                  \tag{2.8}
\]

with a sufficiently small fixed `epsilon`.  Equations (2.2) and (2.6) give

\[
 |8P_{ij}(t)-q^3|\ll q+\epsilon^2qD.                              \tag{2.9}
\]

For small enough `epsilon`, (2.9) implies the exact logarithmic cutoff

\[
 \left|B\log\frac{8P_{ij}(t)}{q^3}\right|\le U.                  \tag{2.10}
\]

Condition (2.1), together with `ell,t=o(q)`, places every node in the
width-`w` shell.  Also `D=o(q)`, so (2.9) is eventually smaller than half
the spacing between consecutive colors; the displayed `c_ij` is the unique
nearest integer used by the carry-core definition.

Consequently the fixed color matrix has at least

\[
 2\lfloor\epsilon\sqrt D\rfloor+1\asymp\sqrt D                 \tag{2.11}
\]

different completions, while (2.4) has determinant comparable with `D`.
This proves (1.2), rather than inferring it from finite numerics.

The repeated off-diagonal color in (2.4) is inessential.  Choose two
different steps `ell_r,ell_c` of order `sqrt(D)` and instead set

\[
\begin{aligned}
 a_i(t)&=A+Ri\ell_r+t,\\
 b_j(t)&=A+Rj\ell_c-t,\\
 c_{ij}&=C-S(i\ell_r+j\ell_c).
\end{aligned}                                                     \tag{2.12}
\]

The same linear cancellation holds, now with

\[
 \det(c_{ij})=-S^2\ell_r\ell_c.                                  \tag{2.13}
\]

All four colors are distinct.  Only four possible translations can create
an equality between a row node and a carrier node, so discarding those
translations leaves `asymp sqrt(D)` completions in which all eight displayed
coordinates are distinct.  Thus the obstruction is not confined to the
repeated-color or role-permutation sector.

---

## 3. Explicit prime-modulus, full-integer witness

There is also a compact exact finite witness with a prime value of `q`:

```text
q = 87,541,837                         (prime)
U = 12
D = 243,253.18037892473
R = 8, S = 7, n = 5,720,399
A = 45,763,192
C = 40,042,793
ell = 15
t = -152,...,152
```

For every one of the 305 translations, take

\[
\begin{aligned}
 (a_0,a_1)&=(45{,}763{,}192+t,\ 45{,}763{,}312+t),\\
 (b_0,b_1)&=(45{,}763{,}192-t,\ 45{,}763{,}312-t),
\end{aligned}
\]

and the fixed color matrix

\[
 \begin{pmatrix}
 40{,}042{,}793&40{,}042{,}688\\
 40{,}042{,}688&40{,}042{,}583
 \end{pmatrix}.                                                   \tag{3.1}
\]

Exact integer and high-precision logarithmic replay gives

```text
determinant                         = -11,025
completions                         = 305
max |B log(8abc/q^3)|              = 11.969927537022055 < 12
max |8abc-q^3|                     = 21,241,464,599,893
completions*|determinant|/D         = 13.823560270669066
completions/sqrt(D)                 = 0.6184015590322527
```

The adjacent translations `t=+-153` fail at the `(1,1)` corner, where the
absolute frequency is `12.0249853522573`.  Thus the displayed interval is
not an artifact of an arbitrary truncation.

All the labels in (3.1) and the row/carrier labels are ordinary integers.
They are not all prime powers.  The primality of `q` therefore does not make
this an actual-prime-power witness.

There is a stronger all-distinct replay at the same prime modulus.  Take

```text
ell_r = 15, ell_c = 14
t = -165,...,157
```

in (2.12).  The fixed color matrix is

\[
 \begin{pmatrix}
 40{,}042{,}793&40{,}042{,}695\\
 40{,}042{,}688&40{,}042{,}590
 \end{pmatrix}.                                                   \tag{3.2}
\]

Exact replay gives

```text
determinant                         = -10,290
completions                         = 323
max |B log(8abc/q^3)|              = 11.967216594202626 < 12
completions*|determinant|/D         = 13.663418479555305
completions/sqrt(D)                 = 0.6548973887456315
```

The four translations `t=-60,-4,0,56` are precisely the possible
row/carrier coincidences.  Removing them leaves 319 completions with all
eight coordinates distinct and

```text
319*|determinant|/D                 = 13.494212058755858.
```

---

## 4. Relation to the finite completion ledger

The earlier actual-prime-power ledger did not show this growth.  At cutoff
`U=12`, the maximum exact oriented multiplicities at
`q=25013,50021,100003,200003` were respectively

```text
2, 2, 2, 3.
```

The corresponding maxima of `m*|k|/D` were

```text
0.877, 0.873, 1.001, 1.065.
```

Those are finite diagnostics only.  They neither prove a prime-power
completion theorem nor conflict with the integer construction above.

The exact grid has the three distinct colors

\[
 S n,\qquad S(n-\ell),\qquad S(n-2\ell).                          \tag{4.1}
\]

In fact, when `S>1`, these three colors **cannot all be prime powers**.
Indeed, any prime dividing `S` must be the base prime of each of the three
putative prime powers.  They would therefore be three distinct powers of
one prime in arithmetic progression.  But

\[
 p^u+p^w=2p^v
\]

has no nonconstant solution.  If `p` is odd and `u<w`, comparison of
`p`-adic valuations forces `v=u`, after which `1+p^(w-u)=2`, impossible.
If `p=2` and `u<w`, the valuations force `u=v+1`, after which division by
`2^u` gives `1+2^(w-u)=1`, also impossible.  Hence `u=w`, and then all three
terms are equal.  This proves that the exact-slope grid is excluded from
actual prime-power support.

The asymmetric all-distinct version is excluded as well.  Its four colors
share the factor `S` and obey

\[
 c_{00}+c_{11}=c_{01}+c_{10}.                                    \tag{4.3}
\]

If all four were prime powers, they would be powers of the same prime.
Uniqueness of the base-`p` expansion of a sum of two distinct powers then
forces the two unordered pairs in (4.3) to be equal, contradicting the four
distinct colors.

That exclusion is specific to the exact cancellation `RC=SA`.  A perturbed
grid has a linear error proportional to

\[
 A\ell(RC-SA),                                                     \tag{4.2}
\]

so an actual analogue with `ell` of order `sqrt(D)` would only need the
near-slope condition `|RC-SA|=O(sqrt(D))`; it is not ruled out by the
argument above.  Removing all such near-grids requires genuinely arithmetic
input.  Determinant geometry alone cannot do so.

---

## 5. Why accumulation of this grid stops at FC scale

Completing many levels of (2.12) does not produce an FC counterexample.  It
produces a compressed Hankel matrix.  After harmless affine reindexing, its
positive majorant has the form

\[
 H_{uv}=|z_{u+v}|,qquad u\in I, v\in J,                           \tag{5.1}
\]

where the product cutoff forces

\[
 |I|,|J|,|I+J|\ll W,\qquad W\ll\sqrt D.                           \tag{5.2}
\]

For a color vector of squared mass

\[
 x=\sum_{s\in I+J}|z_s|^2,
\]

the matching multiplicity of each sum and Young's convolution inequality
give

\[
 \|H\|_F^2\le W x,
 \qquad
 \|H\|_{\rm op}^2\le |I+J|x\le 2Wx.                              \tag{5.3}
\]

The smooth positive kernel is entrywise at most this majorant, so (5.3)
also bounds the weighted patch.  Consequently

\[
 \operatorname {tr}(H^*H)^2
 \le \|H\|_{\rm op}^2\|H\|_F^2
 \le 2W^2x^2
 \ll D x^2.                                                       \tag{5.4}
\]

This is the exact budget inequality that the isolated completion count
misses.  A 2-by-2 fixed-color grid contributes only `sqrt(D)`; filling all
overlapping levels increases both norm budgets until their product reaches,
but does not exceed, order `D`.

More generally, suppose such tangent patches are row/column disjoint and
each color belongs to at most `mu` patches.  If `x_nu` is the color mass in
patch `nu`, then

\[
 \sum_\nu x_\nu\le\mu,
 \qquad
 \sum_\nu x_\nu^2\le\mu,
\]

and (5.4) gives total fourth trace `O(D mu)`.  Thus the blocked-Latin
countermodel would require polynomial color reuse.  In the exact factorized
integer grid, reuse of a fixed color progression across different row and
carrier scalings is controlled by choices of a factor pair and is therefore
divisor-type.  Promoting that observation from exact tangent patches to the
whole actual shell remains open.

The explicit all-distinct witness confirms the budget numerically without
being used as proof.  Add both `(a,b,c)` and `(b,a,c)`, put `z=1/2` on the
four colors in (3.2), and use the actual smooth kernel.  Exact sparse replay
gives

```text
nodes                              = 447
matrix entries                     = 1,532
smooth Q_nd                        = 122.15963796706342
smooth fourth trace                = 570.463409693488
unweighted Q_nd                    = 161.5
D                                  = 243,253.18037892473
```

Thus the 323-completion family is only `0.0005022 D` after the color budget
is imposed.

A projected finite search of complete integer cores at cutoff `U=1` and
`q=401,809,1295,1601,2151,3203,6421` found best lower-bound ratios `Q_nd/D`
between `0.004` and `0.071`.  At `U=12`, very small `q` is in the dense
preasymptotic regime `D` comparable with the entire shell and ratios up to
about `9` occur; this is a fixed constant, not an asymptotic violation.
Neither calculation is a global optimization or an asymptotic argument.
No integer-shell FC counterexample was found.

---

## 6. Consequences for the four-cycle program

```text
fixed-color (D/|k|)*polylog bound, full integers:     FALSE;
sqrt(D) fixed-color multiplicity, full integers:      PROVED POSSIBLE;
same with four colors/all eight coordinates distinct: PROVED POSSIBLE;
explicit prime-q/full-integer witness:                 VERIFIED EXACTLY;
same construction on actual prime-power nodes:        NOT OBTAINED;
exact-slope construction on prime-power nodes:         IMPOSSIBLE;
FC on exact tangent/Hankel patches:                     PROVED;
integer-shell FC counterexample:                        NOT FOUND;
actual prime-power fixed-color theorem:                OPEN;
four-cycle bound (FC):                                 OPEN.
```

This does not refute FC: a single fixed-color family of size `sqrt(D)` is
still below an `O(D)` fourth-moment target.  It does refute the proposed
`D/|k|` completion lemma and identifies the missing mechanism precisely:
any successful argument must detect prime-power incompatibility with the
opposite-translation grid.

---

## 7. Reproduction

The exact identities and finite witness audit are implemented in

```text
src/qp_four_cycle_translation_grid.py
src/test_qp_four_cycle_translation_grid.py
```

Run

```bash
PYTHONPATH=src python3 -m pytest -q \
  src/test_qp_four_cycle_translation_grid.py
```
