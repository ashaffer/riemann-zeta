# QP Fu--Guth--Maldague critical-`L3` macroblock audit

**Date:** 2026-08-15  
**Primary source:** Fu--Guth--Maldague,
[*Decoupling inequalities for short generalized Dirichlet sequences*](https://arxiv.org/abs/2104.00856),
especially Theorems 1.2, 4.4, and 7.1 and Proposition 3.5.  
**Verdict:** Theorem 1.2 proves the sharp QP `L3` target on every
`q^(1/2)`-node macroblock.  The paper's proved full-sequence recombination,
Theorem 7.1, loses exactly `q^(1/12+o(1))` at `p=3`.  Its bilinear and
refined statements do not remove that loss across the `q^(1/2)` different
macroblocks.  A better actual-logarithm recombination remains open.

No global `L3`, four-cycle, QP, or strip theorem is asserted here.

---

## 1. Exact scale match

Use the project notation

```text
T=B=q^(50/33),
D=q^2/B=q^(16/33),
R=q/sqrt(B)=q^(8/33)=sqrt(D).                       (1.1)
```

Partition the node shell into ordinary macroblocks `J` of `q^(1/2)`
consecutive integers.  After reversing and negating frequencies if needed,
the sequence

```text
{log n:n in J}
```

is a `q^(1/2)`-short generalized Dirichlet sequence with parameter `Nasympq`:
its gaps are `asymp q^(-1)` and its successive gap differences are
`asymp q^(-2)`.  Deleting non-prime-power nodes is handled by setting their
coefficients to zero.

Multiplication by a smooth time cutoff adapted to an interval of length
`T` broadens each frequency by `O(T^(-1))`.  In Theorem 1.2 choose

```text
L=R=q/sqrt(T),
L^2/q^2=T^(-1).                                    (1.2)
```

This is in the theorem's range because `1<=R<<q^(1/2)`.  Its canonical
frequency pieces are precisely the ordinary critical node blocks of length
`R`, up to harmless endpoint constants.

## 2. One macroblock reaches the target

Write `X_J=sum_(I subset J)X_I`, where each `I` has at most `R` nodes.
Theorem 1.2 at `p=3` gives, after the standard compact-Fourier cutoff and
normalization by `T^(-1/3)`,

```text
||X_J||_3
 <<q^o(1) (sum_(I subset J)||X_I||_3^2)^(1/2).     (2.1)
```

Local `L2` orthogonality and the pointwise Cauchy bound give

```text
||X_I||_3<<R^(1/6)||x_I||_2.                       (2.2)
```

Consequently

```text
||X_J||_3
 <<q^o(1) R^(1/6)||x_J||_2
 =q^o(1)D^(1/12)||x_J||_2.                         (2.3)
```

Thus the previously missing reverse square function is now proved inside
each entire `q^(1/2)` macroblock, not merely inside one `R`-node block.

## 3. What the paper proves globally

There are `asymp q^(1/2)` macroblocks.  Section 7 treats a full generalized
Dirichlet sequence of `N` terms by applying the short-sequence theorem in
each `N^(1/2)` frequency window and then flat decoupling between those
windows.  Theorem 7.1 states, for `2<=p<=6`, the loss

```text
N^(1/4-1/(2p)+epsilon).                             (3.1)
```

At `p=3` and `Nasympq`, this is

```text
q^(1/12+epsilon)
=(q^(1/2))^(1/2-1/3),                              (3.2)
```

exactly the flat-decoupling loss over the macroblocks.  Combining (2.3)
with Theorem 7.1 proves only

```text
||X||_3
 <<q^(1/12+o(1))D^(1/12)||x||_2
 =q^(49/396+o(1))||x||_2.                          (3.3)
```

The target exponent is `D^(1/12)=q^(4/99)=q^(16/396)`, so (3.3) retains
the full extra `q^(1/12)=q^(33/396)`.  Cubing retains an extra `q^(1/4)`.

Theorem 7.1 is sharp for some generalized Dirichlet sequences constructed
in that paper.  This does not show that the loss is necessary for the
specific logarithmic sequence; it shows only that generalized convexity
cannot remove it.

## 4. Why the bilinear/refined results do not certify a better merge

The potentially relevant statements have the following exact scopes.

1. **Theorem 4.4 (refined decoupling)** holds for `2<=p<=6`, but for the
   canonical partition of one `N^(1/2)`-short sequence.  It strengthens the
   mechanism behind (2.1); it is not a theorem coupling the
   `N^(1/2)` separate macroblocks of a full sequence.

2. **Proposition 3.5 (bilinear restriction)** controls an `L2` norm of a
   product, equivalently an `L4`-type expression, for two transversal
   frequency unions inside the same short-sequence geometry.  It neither
   states a `p=3` cross-macroblock inequality nor applies to the union of
   polynomially many separated macroblocks.

3. **Theorems 1.3 and 8.1 (small-cap decoupling)** explicitly assume
   `p>=4`.  They therefore cannot be substituted at the required `p=3`.

4. **Theorem 7.1** is the paper's actual full-sequence recombination of the
   short/refined theory, and its factor at `p=3` is exactly (3.2).

Therefore no result in this paper proves a cross-macroblock loss smaller
than `q^(1/12+o(1))` for the QP `L3` problem.  Beating it would require a
new theorem exploiting arithmetic or long-range curvature specific to
`log n`, beyond the short generalized-sequence hypotheses.

```text
critical R-node block target:                       PROVED (elementary);
q^(1/2)-node macroblock target:                     PROVED (FGM Thm 1.2);
full-shell bound from FGM:                          q^(1/12)D^(1/12);
cross-macroblock loss below q^(1/12) from FGM:      NOT PROVED;
global arbitrary-coefficient D^(1/12) target:       OPEN;
four-cycle / QP / strip:                            NOT PROVED.
```
