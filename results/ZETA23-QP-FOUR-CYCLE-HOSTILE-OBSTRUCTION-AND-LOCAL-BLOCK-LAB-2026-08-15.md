# QP four-cycle hostile audit: positive core, trace overkill, and local blocks

**Date:** 2026-08-15  
**Verdict:** no actual-prime-power counterexample to the proposed four-cycle
bound was found.  The search does prove three cautions which materially
restrict a proof.

1. For the natural symmetric legal time bump, the innermost carry core can be
   dephased to an **entrywise positive** tensor.  Cancellation between Fourier
   signs cannot prove the bound on that core.
2. Individual actual-prime rectangles can have constant color determinant.
   An exact fixture at `q=50021` has determinant `6`; hence determinant
   repulsion of the form `|Delta|>>q^eta` is false.
3. The fourth-trace estimate `(FC)` is strictly stronger than the desired
   operator estimate.  There are abstract partial-Latin systems with degree
   cap `D`, operator norm exactly `D^(1/4)`, and
   `Q_nd asymp D^(3/2)`.

The last point means that failure of `(FC)` would not by itself refute the
quarter-power tensor bound.  A proof should either exclude repeated coherent
blocks arithmetically or estimate the top singular value without summing the
fourth powers of all singular values.

All finite optimizations below are explicitly diagnostics.  They are neither
certified global maxima nor evidence for an asymptotic estimate.

---

## 1. The positive core survives dephasing

Use the fixed smooth probability bump

```text
psi(t)=C exp[-1/(1-(6t-3)^2)] 1_(1/3<t<2/3).       (1.1)
```

It is symmetric about `t=1/2`.  Writing `t=1/2+u` gives the exact identity

```text
hat(psi)(xi)=exp(i xi/2) Phi(xi),
Phi(xi)=int psi(1/2+u) cos(xi u)du in R.             (1.2)
```

For

```text
xi=B log(abc/Y^3),                                  (1.3)
```

the phase in (1.2) factors as a constant times one phase in each of `a`, `b`,
and `c`.  Row and column diagonal unitaries and a phase change of the color
vector therefore remove it without changing the fourth trace or `Q_nd`.

Continuity and `Phi(0)=1` give an absolute `xi_0>0` for which `Phi(xi)>0` on
`|xi|<=xi_0`.  For the explicit bump (1.1), the replay uses `xi_0=12`; a
192-point Gauss--Legendre evaluation gives

```text
min_(|xi|<=12) Phi(xi) > .7.                        (1.4)
```

Only positivity in some fixed neighborhood, which follows analytically from
continuity, is used in the structural conclusion.  Consequently, for
nonnegative `z`, every nondegenerate rectangle in this inner core contributes
with the same sign.  A proof of `(FC)` must control an unsigned rectangle
count there.  Oscillation in the outer Fourier tail cannot establish the
standalone inner-core estimate.

---

## 2. Exact actual-prime rectangle with determinant six

Set

```text
q=50021,                 Y=q/2,
(a1,a2)=(21277,22741),
(b1,b2)=(28277,28793),

          [26003  25537]
(c_ij) = [24329  23893].                            (2.1)
```

All eight displayed nodes are prime and satisfy

```text
|log(n/Y)|<.2.                                      (2.2)
```

At `A=50/33`, the four exact residuals `8 a_i b_j c_ij-q^3` and their
normalized logarithmic versions are

```text
17066235     .6287852733...
18768395     .6914993436...
 7565163     .2787295068...
10476011     .3859762633... .                       (2.3)
```

Thus all four edges lie even in the fixed core `|xi|<.7`.  Nevertheless,

```text
26003*23893-25537*24329=6.                          (2.4)
```

This is a rigorous finite obstruction to any argument which tries to prove
`(FC)` by showing that each nondegenerate color determinant has fixed-power
size.

There is still a useful exact lower statement.  In a shell of width
`2w<log 2`, at most one power of a given prime base occurs.  If a
nondegenerate prime-power rectangle had determinant zero, unique
factorization would pair the two prime bases on the left with those on the
right.  One of the pairings makes two colors in a common row equal; the other
makes two colors in a common column equal.  Both contradict pair uniqueness.
Hence

```text
Delta != 0,             |Delta|>=1,                (2.5)
```

but (2.4) shows that this integrality floor cannot be promoted to a power of
`q`.

---

## 3. Fourth trace can fail while the operator target holds

Let `L>=2`.  Take `L` disjoint row--column blocks, each of size `L` by `L`.
Color every block by the same Latin square on `L` colors, and put

```text
z_c=L^(-1/2).                                       (3.1)
```

Different blocks reuse the colors but have disjoint row and column vertices.
All pair-uniqueness and disjoint-support axioms remain valid.  Every color has
degree

```text
D=L^2.                                              (3.2)
```

The resulting matrix is block diagonal with `L` constant blocks, each entry
being `L^(-1/2)`.  Direct calculation gives

```text
||A||_F^2=L^2=D,
||A||_op=sqrt(L)=D^(1/4),
tr((A^*A)^2)=L^3=D^(3/2),
Q_nd=L(L-1)^2 asymp D^(3/2).                       (3.3)
```

Thus `(FC)` fails by `D^(1/2)` in this abstract model even though the desired
operator bound is sharp.  The obstruction is not one rank-one Latin square;
it is the accumulation of `L` harmless top singular values from disjoint
coherence blocks.

This changes the interpretation of the proposed route:

```text
(FC)  ==> quarter-power operator bound,             PROVED EARLIER;
quarter-power operator bound ==> (FC),              FALSE;
failure of (FC) ==> failure of quarter-power bound, FALSE.  (3.4)
```

An arithmetic proof of `(FC)` must therefore rule out repeated coherent
blocks, not merely rule out a single Schur-saturating Latin core.

---

## 4. Exact integer multiplicative blocks incur exponential ambient size

There is a direct exact integer analogue of one additive Latin rectangle.
For integers `m,L,s>=1`, put

```text
a_i=s m^(2L-2-i)(m+1)^i,                 0<=i<L,
b_j=s m^(2L-2-j)(m+1)^j,                 0<=j<L,
c_k=s m^k(m+1)^(2L-2-k),                 0<=k<=2L-2. (4.1)
```

Then

```text
a_i b_j c_(i+j)=s^3 m^(4L-4)(m+1)^(2L-2)           (4.2)
```

exactly.  Taking `m>>_w L` places all entries in one fixed multiplicative
shell about the cube root of (4.2).  This demonstrates that integer
factorization alone does not forbid coherent blocks.

It does not embed the power-sized countermodel (3.3) into the QP shell.  The
ambient entries in (4.1) have logarithm

```text
log Y >> L log m >>_w L log L.                      (4.3)
```

Thus this construction has only

```text
L<<_w log Y/log log Y=Y^o(1).                       (4.4)
```

Moreover its natural cube-root center need not be a legal half-integer
`q/2`; tuning it to the `B^(-1)` carry window is a separate Diophantine
condition and is not claimed here.  No integer-shell realization with
`L=Y^eta`, and no actual-prime realization of (3.3), was found.

---

## 5. Actual-prime-power smooth-kernel diagnostics

The executable lab builds the actual prime-power shell at prime half-centers,
uses (1.1), dephases by (1.2), and truncates at `|xi|<=12`.  It then runs
deterministic projected ascent from degree-ordered nonnegative supports.  Write

```text
R=q^2/B,                 D_geom=12R.                (5.1)
```

The returned `best Q_nd` is only a finite lower bound for the maximum.

| `q` | nodes | core entries | `R` | max weighted color degree | best `Q_nd` | `Q_nd/R` |
|---:|---:|---:|---:|---:|---:|---:|
| 25,013 | 535 | 4,002 | 387.75 | 18.22 | .6074 | 1.57e-3 |
| 50,021 | 996 | 9,675 | 542.60 | 22.79 | .8151 | 1.50e-3 |
| 100,003 | 1,875 | 21,741 | 759.20 | 29.98 | .6120 | 8.06e-4 |
| 200,003 | 3,496 | 50,292 | 1,062.44 | 36.41 | .3957 | 3.72e-4 |

No growing violation is visible in these four scales.  This sentence is a
description of the table, not an asymptotic inference.

The more targeted hostile scan puts uniform nonnegative `z` on numerical
color intervals of width `L=sqrt(R)` through `8L`.  Up to 200 interval starts
are sampled at each width.

| `q` | `L` | best local `Q_nd` | `Q_nd/R` |
|---:|---:|---:|---:|
| 25,013 | 20 | .1625 | 4.19e-4 |
| 50,021 | 23 | .2093 | 3.86e-4 |
| 100,003 | 28 | .02767 | 3.64e-5 |
| 200,003 | 33 | .05743 | 5.41e-5 |

Using blocks of `L` through `8L` consecutive prime-power indices instead of
integer intervals gives a largest observed ratio `Q_nd/R=7.34e-5`.  Thus the
specific local-coherence-block falsifier was not found at these scales.

For comparison, the full integer shell has much larger finite fourth-trace
accumulation: at `q=1601,...,12853`, uniform or projected nonnegative vectors
give `Q_nd` of order `8,000--10,000`.  The ratio to `D_geom` decreases over
the tested range and does not constitute a big-O counterexample.  It does
show why finite constants and prime-power sparsity must not be conflated.

---

## 6. Binary status

```text
centered-phase dephasing identity:                  PROVED;
positive fixed inner core:                         PROVED;
actual all-prime determinant-six rectangle:         PROVED;
power determinant repulsion for every rectangle:   FALSE;
FC stronger than the quarter-power operator bound: PROVED;
power-size integer-shell repeated-Latin embedding: NOT FOUND;
actual-prime-power counterexample to FC:            NOT FOUND;
uniform four-cycle bound (FC):                      NOT PROVED;
quarter-power balanced tensor estimate:             NOT PROVED.
```

Executable replay:

```bash
python3 -m pytest -q src/test_qp_four_cycle_hostile_lab.py
```

The diagnostic builders and searches are in
`src/qp_four_cycle_hostile_lab.py`.
