# QP balanced cubic: curved-incidence theorem-class barrier

**Date:** 2026-08-15  
**Verdict:** no fixed-power saving below the coefficient-uniform
`sqrt(R)` tensor bound is proved.  A direct audit of curvature, Cartesian
incidence, point-plane, reciprocal, and local-energy routes gives a sharp
theorem-class barrier:

1. the thickened product surface is **exactly group-related** in the sense
   excluded from the Elekes--Szabó incidence saving;
2. the strongest directly applicable convex-lattice estimate is slightly
   weaker than the elementary prime-power product count;
3. the natural point-plane lift is a maximal pencil, so Rudnev's collinearity
   term is trivial;
4. one-step `TT*` or Cauchy reduction lands on an unsigned near-product
   energy which is `R/q^o(1)` already for uniform weights on actual primes.

This does not prove that the actual signed tensor has norm
`>>sqrt(R)`.  It proves that a saving must preserve a joint signed
three-slot feature which all four theorem classes discard.

---

## 1. Exact target and baseline

Let

```text
q be an odd prime,             Y=q/2,
B=Y^A,                         3/2<A<2,
R=q^2/B=q^(h+o(1)),            h=2-A<1/2,
H=qR=q^3/B=q^(1+h+o(1)),
S_Y={n=p^j:Y exp(-w)<n<Y exp(w)}.                  (1.1)
```

For arbitrary real or complex coefficient vectors, the unresolved balanced
all-plus hard tensor is

```text
T(x,y,z)=sum_(a,b,c in S_Y) x_a y_b z_c
          1_(|8abc-q^3|<=C_wH).                   (1.2)
```

A fixed pair `(a,b)` admits `O_w(1)` possible `c` because the interval for
`c` has length `O(H/q^2)=O(R/q)=o(1)`.  For fixed `c`, the product `ab`
lies in an interval of length `O(H/q)=O(R)`, and a fixed integer has
`O_w(1)` representations by two shell prime powers.  Flattening pairs
against `c` therefore gives

```text
|T(x,y,z)|<<_w sqrt(R)||x||_2||y||_2||z||_2.     (1.3)
```

At `A=50/33`, the tensor exponent is `h/2=8/33`.  Coupled with the generic
`q^(1/2+o(1))` leverage, this is the current full-shell exponent `49/66`.

---

## 2. Nonzero ordinary curvature is not the right invariant

On a positive chart the exact level surface is

```text
c=X/(ab).                                          (2.1)
```

Its graph Hessian has determinant `3X^2/(a^4b^4)>0`; thus it has genuine
ordinary curvature.  Nevertheless it is a multiplicative group surface.

Introduce the unique integer residual

```text
r=8abc-q^3,                  |r|<=C_wH,            (2.2)
```

and the four-variable polynomial

```text
F(a,b,c,r)=8abc-q^3-r.                              (2.3)
```

Raz--Sharir--de Zeeuw, Theorem 1.1 in their four-dimensional
Elekes--Szabó paper, gives a Cartesian-product power saving unless the zero
set is locally equivalent to

```text
phi_1(a)+phi_2(b)+phi_3(c)+phi_4(r)=0.             (2.4)
```

Our surface is exactly in that exceptional class.  On the positive shell
take

```text
phi_1(a)=log a,          phi_2(b)=log b,
phi_3(c)=log c,          phi_4(r)=-log((q^3+r)/8). (2.5)
```

All four maps are locally invertible, and (2.3) is equivalent to (2.4).
For every fixed residual `r`, the three-variable slice is similarly
exceptional via the first three logarithms.  Thus neither introducing the
thickening variable nor slicing it into exact levels escapes the group-law
case.  The `n^(8/3)` four-dimensional and `n^(11/6)` three-dimensional
incidence alternatives are not available.

This is a precise reason why a nonzero Hessian determinant, a curved cell
decomposition, or a generic polynomial-incidence slogan does not by itself
address (1.2).

---

## 3. Convex lattice-point bounds miss the active exponent

In the original lattice coordinates, the band (1.2) has physical normal
thickness `delta`; after scaling `(a,b,c)=q(u,v,w)`, the corresponding
normalized thickness is `delta/q`.  Here

```text
delta asyp H/q^2=R/q,       delta/q asyp H/q^3.    (3.1)
```

Lettington's integer-point estimate near a three-dimensional strictly
convex surface has the scale

```text
N<<q^(3-2+2/(3+1))+q^(3-1)delta
  =q^(3/2)+qR.                                     (3.2)
```

At the active aperture,

```text
qR=q^(49/33),             q^(3/2)=q^(99/66),
3/2-49/33=1/66.                                   (3.3)
```

Hence the curvature term is worse by the fixed factor `q^(1/66)`.
Moreover, for the actual nodes a simpler arithmetic count is already
stronger: every integer product `abc` has `O_w(1)` ordered
prime-power representations, so the `O(H)` possible product values give

```text
#support(T)<<_wH=qR.                               (3.4)
```

Neither (3.2) nor the sharper unweighted (3.4) is a weighted `ell^2`
tensor estimate.  Curved lattice counting therefore supplies no saving
over (1.3).

---

## 4. The point-plane lift is a maximal pencil

Writing `u=bc`, the exact residual equation is

```text
8ua-r=q^3.                                         (4.1)
```

The standard point-plane lift associates to each `u` a plane

```text
Pi_u: 8u x-y=q^3                                  (4.2)
```

in a three-dimensional ambient space.  All these planes contain the same
line

```text
x=0,             y=-q^3.                           (4.3)
```

Rudnev's point-plane theorem has the form
`O(m sqrt(n)+m k)`, where `k` is the maximum collinear/pencil
multiplicity.  Here `k` equals the whole `u`-family size.  The `m k` term
is therefore the trivial incidence count.  Permuting the three factors
only produces the same pencil in another coordinate.

This degeneracy is the linear-incidence shadow of the logarithmic group
law in Section 2.

---

## 5. Direct `TT*` hits an actual-prime energy wall

Cauchy--Schwarz in the `a` slot of (1.2) implies, after harmless changes
in the hard-window constant,

```text
|T(x,y,z)|^2
 <=||x||_2^2
   sum_(b,c,b',c':|bc-b'c'|<=C_wR)
   |y_b z_c y_b' z_c'|.                            (5.1)
```

Indeed, if one `a` is incident to both `(b,c)` and `(b',c')`, subtraction
of the two residual equations gives `|bc-b'c'|<<H/q=R`.

The right side of (5.1) cannot have a coefficient-uniform fixed-power
improvement.  Choose a fixed interval inside the shell containing

```text
M>>_wq/log q                                       (5.2)
```

actual primes, and put `y_p=z_p=M^(-1/2)` there.  The `M^2` ordered
products lie in an interval of length `O_w(q^2)`.  Partition it into
`J<<_wq^2/R` bins of length at most `R`, and let `N_j` be the number of
ordered products in bin `j`.  Cauchy--Schwarz gives

```text
sum_j N_j^2 >=M^4/J >>_w M^4R/q^2.                (5.3)
```

Pairs in one bin are counted by the near-product energy in (5.1), so after
the unit `ell^2` normalization,

```text
sum_(|bc-b'c'|<=R)|y_bz_cy_b'z_c'|
 >>_w M^2R/q^2
 >>_w R/(log q)^2.                                (5.4)
```

Thus no bound `R q^(-eta)` for this unsigned energy can hold for any fixed
`eta>0`.  Taking its square root recovers `sqrt(R)` up to logarithms.

Equation (5.4) does **not** lower-bound the signed tensor (1.2), because
(5.1) is one-way.  It proves that any successful `TT*` argument must retain
additional correlation with the eliminated `a` incidence; replacing that
correlation by absolute local product energy necessarily loses the desired
power.

---

## 6. Other primary theorem mismatches

Fourier inversion of the hard residual window produces the monomial phase
`theta abc`.  Robert--Sargos's three-dimensional monomial theorem requires
`alpha(alpha-1) beta gamma !=0`; all three exponents here equal one, so
every choice of their curvature variable has `alpha(alpha-1)=0`.  Their
four-variable spacing theorem likewise excludes exponent `1`.  It gives no
weighted bound for (1.2).

Eliminating `c` instead produces

```text
c=nearest_integer(q^3/(8ab)),
|c-q^3/(8ab)|<<R/q<1.                              (6.1)
```

The value `z_c` is then an arbitrary sample of the coefficient vector at a
discontinuous nearest-quotient map.  Reciprocal-energy and smooth
Kloosterman-fraction theorems do not supply a three-arbitrary-weight norm
for this sample.  Taking absolute values reduces again to (5.1).

The nonlinear Brascamp--Lieb theorem also stops at the wrong input norm.
On the two-dimensional surface `abc=X`, the three coordinate maps have
one-dimensional targets.  An `ell^2` estimate would correspond in the
Brascamp--Lieb notation to the symmetric exponents

```text
p_1=p_2=p_3=1/2.                                  (6.2)
```

But finiteness requires the scaling identity

```text
2=dim(surface)=sum_j p_j dim(target_j),            (6.3)
```

whereas the right side of (6.3) is `3/2`.  Thus the underlying linear
Brascamp--Lieb constant is infinite, and the nonlinear theorem cannot give
the desired `ell^2` tensor estimate.  The symmetric scale-invariant choice
is instead `p_j=2/3`, which controls `L^(3/2)` inputs.  Passing from those
norms to arbitrary `ell^2` shell coefficients incurs a positive support-size
loss, not a power saving.

The finite-field variety-energy route is excluded for the same structural
reason.  Shkredov's power-saving theorem explicitly requires that the
variety not contain a coset of an algebraic subgroup comparable in size to
the variety.  In the multiplicative torus,

```text
{(a,b,c):abc=X}=(X,1,1){(u,v,w):uvw=1},            (6.4)
```

so the whole level surface is such a coset.  Moreover that theorem concerns
unweighted multiplicative energy over finite algebraic groups, not the
archimedean signed three-weight norm (1.2).  Its saving alternative is
therefore unavailable here.

---

## 7. Binary conclusion and the missing theorem

```text
balanced tensor norm <<sqrt(R):                    PROVED;
fixed-power saving by generic curved incidence:    EXCLUDED CASE;
fixed-power saving by convex lattice counting:     NO;
fixed-power saving by Rudnev point-plane lift:      PENCIL DEGENERACY;
fixed-power saving by unsigned TT*/energy:          IMPOSSIBLE;
actual tensor norm >>sqrt(R):                       NOT PROVED;
full-shell exponent below 49/66:                    NOT PROVED.
```

The viable missing statement is necessarily a **joint signed** theorem.
One formulation is a power-saving bound for the contraction in (5.1)
before the `a` incidence is discarded; another is an inverse theorem saying
that a near-extremizing weighted tensor creates a large logarithmic
approximate subgroup and then ruling that structure out for the actual
prime-power nodes.  None of the audited primary theorems provides either
statement.

Executable checks:

```bash
python3 -m pytest -q src/test_qp_balanced_curved_incidence_barrier.py
```

Primary sources used for theorem-level claims:

1. O. E. Raz, M. Sharir, and F. de Zeeuw,
   [*The Elekes--Szabó Theorem in four dimensions*](https://arxiv.org/abs/1607.03600),
   Theorem 1.1; and
   [*Polynomials vanishing on Cartesian products: The Elekes--Szabó
   Theorem revisited*](https://arxiv.org/abs/1504.05012), Theorem 1.1.
2. M. C. Lettington,
   [*Integer points close to convex surfaces*](https://eudml.org/doc/278130),
   Acta Arith. 138 (2009), 1--23.
3. M. Rudnev,
   [*On the number of incidences between points and planes in three
   dimensions*](https://arxiv.org/abs/1407.0426), Combinatorica 38
   (2018), 219--254.
4. O. Robert and P. Sargos,
   [*Three-dimensional exponential sums with monomials*](https://perso.univ-st-etienne.fr/rool6510/robert-2006-crelle.pdf),
   J. Reine Angew. Math. 591 (2006), 1--20.
5. J. Bennett, N. Bez, S. Buschenhenke, M. G. Cowling, and T. C. Flock,
   [*On the nonlinear Brascamp--Lieb inequality*](https://arxiv.org/abs/1811.11052),
   Theorem 1.1 and the necessary scaling condition (1.7).
6. I. D. Shkredov,
   [*On multiplicative energy of subsets of varieties*](https://arxiv.org/abs/2101.09770),
   Theorem 1 and its algebraic-subgroup-coset criterion.

Only primary papers support the literature claims.  The group-form check,
prime-power product count, pencil computation, and actual-prime energy
lower bound are proved directly above.
