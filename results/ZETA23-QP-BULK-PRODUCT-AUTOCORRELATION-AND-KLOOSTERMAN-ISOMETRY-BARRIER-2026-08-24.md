# QP local lift: bulk product autocorrelation and Kloosterman isometry barrier

**Date:** 2026-08-24  
**Verdict:** after the coherent CRT ray, both coordinate axes, and the
product diagonal have been deleted, the difference-of-products coefficient
can still have a full polynomial `D` excess over the tensor input norm.
The excess can be placed on the macroscopic band

```text
3*D/2<Delta<=3*D,                                  (0.1)
```

so it is not a disguised `Delta=0` or small-difference term.  For a prime
top modulus, the normalized Kloosterman transform has an exact Parseval
identity and preserves this packet up to one constant Fourier mode.
Consequently neither local mask deletion nor spectral Plancherel supplies
the hoped-for coefficient contraction.

This is an exact fixed-modulus counterexample in the completed fan
coordinates.  It has an exact integral pullback to the balanced physical fan
residues for one aligned modulus, and that pullback is quantitatively broad,
not tangent.  It is not yet a counterexample to the full actual mask: it does
not prove that all pulled-back nodes are prime powers or that the unique
carrier selected by every product window is present.  It also does not
disprove a theorem which keeps one set of physical coefficients through the
complete moving-`c` DFI sum, because the pullback depends on `c`.  Any
remaining positive route must use one of those two facts before taking the
coefficient `l2` norm.

---

## 1. Exact noncoherent transform

For a prime top modulus `c` and `(a,c)=1`, the complete bilinear Gauss sum
is

```text
G_(c,a)(u,v)=sum_(x,y mod c)e_c(a*x*y+u*x+v*y)
            =c*e_c(-a_bar*u*v).                    (1.1)
```

Deleting the raw coherent colour ray `y=0` gives exactly

```text
G^perp_(c,a)(u,v)
 =c*(e_c(-a_bar*u*v)-1_(u=0)).                     (1.2)
```

Deleting both coordinate-zero rays changes (1.1) only by the corresponding
axis indicators and one `a`-independent Ramanujan correction.  Thus on

```text
1<=u,v<c                                           (1.3)
```

the nondegenerate phase in (1.1) is literally unchanged by every coherent
axis deletion.

For separable inputs `p_u,q_v`, put

```text
g(t)=sum_(u*v=t)p_u*q_v,
B_Delta=sum_t g(t+Delta)*conjugate(g(t)).           (1.4)
```

Two copies of (1.1), followed by the primitive numerator sum, produce the
Kloosterman index `Delta=u*v-u'*v'`.  It is the additive autocorrelation
(1.4), not a Hecke product coefficient.

## 2. A separated bulk saturator

Let `L` be divisible by four and put `D=L^2`, `m=L/4`.  In each fan take
the same support

```text
I_0={L,...,L+m-1},
I_1={2L-m+1,...,2L},
I=I_0 union I_1,                                   (2.1)
```

with coefficient `(2m)^(-1/2)`.  Hence

```text
||p||_2=||q||_2=1.                                 (2.2)
```

Consider only the terms in `B_Delta` for which `(u,v)` both lie in `I_1`
and `(u',v')` both lie in `I_0`.  They obey

```text
(7L/4)^2-(5L/4)^2<Delta<=(2L)^2-L^2,
3*L^2/2<Delta<=3*L^2.                              (2.3)
```

There are exactly `m^4` designated ordered quadruples and at most `2L^2`
integer values in the band.  All their coefficients are positive.  Cauchy
therefore gives, before normalization,

```text
sum_(3D/2<Delta<=3D)|B_Delta|^2>=m^8/(2L^2).       (2.4)
```

The normalization in (2.2) scales each `B_Delta` by `(2m)^(-2)`.  Thus

```text
sum_(3D/2<Delta<=3D)|B_Delta|^2
 >=m^4/(32L^2)
 =L^2/8192
 =D/8192.                                         (2.5)
```

The tensor input norm on the right of the hoped-for local lift is one.
Equation (2.5) is consequently a polynomial `D` loss.  Every fan frequency
is nonzero, every displayed `Delta` is nonzero and larger than `D`, and no
coherent-axis, product-diagonal, or low-difference tangent cutoff touches
this energy.

### 2A. Exact aligned pullback is broad in physical fan geometry

The preceding packet is not broad merely in an abstract Fourier label.  Let
`R>4L` be odd and put

```text
S=R+1,       c=R+2,       U=R-1,       V=R,
R*V-S*U=1.                                         (2.6)
```

The exact two Poisson support congruences are

```text
nu == U*r*c == -2r (mod R),
mu == V*s*c ==  -s (mod S).                        (2.7)
```

Restrict the `nu` support in (2.1) to its even elements, retain the whole
`mu` support, and set

```text
r=-nu/2,                 s=-mu.                    (2.8)
```

Because `R>4L`, all quantities lie in the centered residue windows, so
(2.7) is an equality of the intended centered lifts, not a wrapping
artifact.  Most importantly,

```text
Delta=nu*mu-nu'*mu'=2*(r*s-r'*s').                 (2.9)
```

The exact stationary/tangent equation in these fan coordinates is
`r*s-r'*s'=0`.  Every designated high--high versus low--low term instead
satisfies

```text
3D/4<r*s-r'*s'<=3D/2.                              (2.10)
```

Thus this packet lies a macroscopic distance from the tangent variety.  It
has `m` row frequencies and `2m` colour frequencies.  Repeating the Cauchy
count with unit `l2` vectors gives

```text
sum_(3D/2<Delta<=3D)|B_Delta|^2>=D/32768.          (2.11)
```

This is an exact balanced, transverse fixture at one completed modulus.  It
does **not** by itself provide an occupied rectangle in the original graph.
That stronger statement would require, simultaneously, prime-power shell
nodes for the chosen fan residues and the actual unique carrier/product
window for the relevant pairs.  Those are precisely the pieces erased when
one replaces the physical selector by an arbitrary completed coefficient
box.

## 3. Exact Kloosterman square-function identity

Let `lambda` be a unit modulo the prime `c`, assume the signed difference
support of `B` is injective modulo `c`, and define

```text
K_B(h)=c^(-1)*sum_Delta B_Delta*S(-h,-lambda*Delta;c).
                                                               (3.1)
```

Opening the Kloosterman sum gives

```text
K_B(h)=c^(-1)*sum_(a mod c)^* e_c(-a*h)
              *sum_Delta B_Delta*e_c(-a_bar*lambda*Delta).
                                                               (3.2)
```

Additive Parseval in `h`, followed by the fact that inversion permutes the
nonzero residues, proves the exact identity

```text
sum_(h mod c)|K_B(h)|^2
 =sum_Delta|B_Delta|^2
  -c^(-1)*|sum_Delta B_Delta|^2.                  (3.3)
```

For the normalized packet of Section 2,

```text
sum_Delta B_Delta=|sum_t g(t)|^2=(2m)^2=L^2/4.    (3.4)
```

Combining (2.5)--(3.4) gives

```text
sum_h|K_B(h)|^2
 >=D/8192-D^2/(16c).                              (3.5)
```

At the balanced top block

```text
D=q^(16/33),             c~q^(25/33),             (3.6)
```

the second term is `o(D)`.  Thus the primitive Kloosterman square function
is a near-isometry on a coefficient vector which already exceeds the tensor
norm by `D`.  Replacing finite Parseval by Kuznetsov, Yang Plancherel, or an
abstract spectral square function cannot create a contraction which the
local transform itself does not have.

The physical shift range is longer than one modulus at this point:

```text
B_0/c=q^(34/33-25/33)=q^(9/33).                   (3.7)
```

Hence the lack of a full residue period in `h` is not the obstruction.
What can still matter is the signed, nonconstant DFI/archimedean weight
across those periods.

## 4. Exact remaining scope

In the coprime top block the maps from physical fan indices to `u,v` are
injective while `|u|,|v|<<c`.  For the aligned modulus in (2.6), equations
(2.7)--(2.8) give the pullback explicitly and integrally.  Hence arbitrary
coefficients on those physical **fan residues** have exactly the completed
noncoherent transform above.

Fan-residue realizability is weaker than actual-mask realizability.  A fan
residue still has to be occupied by a prime-power shell node, and a row--
colour pair still has to survive the unique carrier/product-window selector.
The construction has not established either condition on a power-sized
rectangle.  In particular, it must not be cited as a literal prime-power
four-cycle counterexample.

The pullback depends on `c`.  Therefore this construction refutes:

```text
* every fixed-`c` contraction for arbitrary completed fan coefficients;
* coefficient-blind Plancherel/Kuznetsov tensorization;
* deletion of u=0, v=0, Delta=0, or |Delta|<=D;
* the proposed unconditional Hecke fold of B_Delta.
```

It does not refute a global theorem in which one fixed physical vector is
carried through all DFI moduli and the signed mismatch weight is retained.
The aligned tangent local-mean theorem shows that such archimedean
cancellation can indeed save special coherent packets.  For general
scattered Bezout pullbacks, however, that global mask-sensitive theorem is
precisely the surviving open problem; it cannot be replaced by an `l2`
bound for (1.4).

## 5. Major arcs are not the existing physical packet projection

There is a useful analytic explanation for the size in (2.5).  If

```text
F(theta)=sum_(nu,mu)p_nu*q_mu*e(theta*nu*mu),       (5.1)
```

then `B_Delta` is the Fourier coefficient of `|F|^2` and

```text
sum_Delta|B_Delta|^2=int_0^1 |F(theta)|^4 dtheta.  (5.2)
```

On the denominator-one arc `|theta|<<1/D`, all products in the separated
box have nearly the same phase.  Its contribution to (5.2) is already
`asymp D` after unit-vector normalization.  This does not make the physical
packet tangent.  Equation (2.10) shows that the individual positive terms
used for the lower bound have fan determinant `asymp D`.  More generally, a
rational arc imposes a congruence on product differences; it does not impose
the exact physical equation `r*s=r'*s'`.

Consequently, “subtract every rational major arc” is not a reformulation of
the proved affine/Hankel packet merger.  The merger charges actual occupied
families lying in certified rational tangent charts.  A circle-method major
arc is a signed, nonlocal projection of a completed rectangle and contains
many transverse pairs such as (2.10).  Turning all such arcs into physical
packets would require a new mask-preserving inverse theorem.

The same warning applies to polar shifted-divisor terms.  A polar term may
subtract the smooth mean of a completed shifted-divisor correlation, but it
is not automatically a positive subfamily of the original masked trace.  To
use that subtraction in an upper bound one must exhibit an exact primal
identity, retain its signs through the DFI weight, and bound the resulting
physical correction.  The current packet merger supplies none of those
steps for a transverse determinant packet.  The aligned tangent local-mean
theorem is the legitimate special case: there the stationary centre pulls
back to the actual product diagonal and the signed local mean is controlled.
It does not authorize a blanket polar/major-arc deletion in the broad
sector.

## 6. Binary status

```text
coherent-axis deletion changes nonzero G phase:        NO;
separable nonzero-frequency packet:                    EXPLICIT;
packet avoids Delta=0 and |Delta|<=D:                  YES;
normalized bulk autocorrelation energy >=D/8192:       PROVED;
aligned physical-fan determinant is asymp D:            PROVED;
aligned physical-fan bulk energy >=D/32768:             PROVED;
prime Kloosterman square-function identity (3.3):       PROVED;
spectral/Plancherel contraction of this coefficient:   FALSE;
fixed-c completed-fan coefficient contraction:          FALSE;
full prime/product-window realization of the packet:    NOT SHOWN;
prime/product mask forces every survivor tangent:       NOT PROVED;
major-arc subtraction equals existing packet merger:    NO;
same physical packet saturates all moving c:           NOT SHOWN;
global signed DFI/tangent projection theorem:           OPEN;
sharp four-cycle theorem from this route:               NOT PROVED.
```

Exact replay code and tests:

```text
src/qp_autocorrelation_bulk_saturator.py
src/test_qp_autocorrelation_bulk_saturator.py
```
