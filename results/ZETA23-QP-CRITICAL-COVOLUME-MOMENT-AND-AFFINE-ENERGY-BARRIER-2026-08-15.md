# QP four-cycle: critical covolume-moment and affine-energy barrier

**Date:** 2026-08-15  
**Verdict:** the tempting fixed-direction moment

```text
sum_C det(Gamma_C) w_z(C) << D q^o(1)             (0.1)
```

is false in the full integer shell model.  It already fails for one color
matrix at null height `D^(1/4)`, even when its plane covolume is below the
low-product cutoff `q/D`.  This does not refute an actual-prime theorem, but
it rules out proving (0.1) from the rank-one relation, determinant cutoff,
shell localization, and exact covolume formula alone.

The affine-group energy theorem of Petridis--Roche-Newton--Rudnev--Warren
also does not by itself give a new exponent here.  The color square does
embed in an affine-group composition identity, but the theorem controls the
number of transformation quadruples, whereas the missing factor is the
number of carrier completions attached to each fixed color square.  Its two
structured concentration branches require, respectively, a rational
parallel-map patch and a concurrent-map (multiplicative) patch; only the
equal-direction additive/Hankel special case has currently been proved.

## 1. Exact critical family

Let `N>=16` and set

```text
D=N^16,       q=4N^33,       n=N^2,
t=N^13,       T=2N^29,
r=s=(n,n+1),  eta=1,         theta=t.              (1.1)
```

Put `X=(n+1)T-1-t` and define

```text
x=(n+1)X,
y=nX-1,
z=nX-t,
w=n^2 T-n(1+t).                                   (1.2)
```

Then all four entries are positive, distinct, and equal to
`q/2*(1+O(N^-2))`.  Direct substitution gives

```text
r1 s1 x-r1 s2 y-r2 s1 z+r2 s2 w=0,
xw-yz=-t.                                         (1.3)
```

Thus this is an active rank-one color relation with `0<|det C|<=D`.  Its
primitive null matrix is `e=r s^T`, so

```text
h(e)=(n+1)^2 = D^(1/4)(1+o(1)).                   (1.4)
```

The exact plane-covolume identity gives, since `gcd(eta,theta)=1`,

```text
P_C^2
 =(eta^2 ||r||_2^4+theta^2 ||s||_2^4)
 =(1+t^2)(2n^2+2n+1)^2.                           (1.5)
```

Consequently

```text
P_C=(2+o(1))N^17,
D=N^16,
q/D=4N^17.                                        (1.6)
```

In particular `D << P_C < q/D`.

Put `z_c=1/2` on these four color labels and zero elsewhere.  Then
`||z||_2=1`, and this single matrix contributes

```text
P_C |z_x z_y z_z z_w|=P_C/16 >> D                 (1.7)
```

to (0.1).  The excess is a genuine power, `D^(1/16)`.

This construction uses integer shell labels, not actual primes.  Hence it
is a method obstruction, not a counterexample to the actual-prime
four-cycle statement.

## 2. The exact `Aff x Add` embedding

There is a stronger exact formulation of the chart square.  Write the row
and column carriers as

```text
A_i(t)=a_i+r_i t,          B_j(t)=b_j+s_j t,
```

and attach to cell `(i,j)` the affine map and additive tag

```text
g_ij=A_i o B_j^(-1),       d_ij=r_i s_j c_ij.      (2.1)
```

Then

```text
g_11^(-1) g_12
 =B_1 o B_2^(-1)
 =g_21^(-1) g_22.                                  (2.2)
```

The scaled-additivity identity is

```text
d_11+d_22=d_12+d_21,
```

or equivalently

```text
d_12-d_11=d_22-d_21.                               (2.3)
```

Thus the four pairs `(g_ij,d_ij)` form an exact energy quadruple in the
direct product `Aff(Q) x Add(Z)`.  No equal-slope assumption is used.

For a finitely supported coefficient function `f(g,d)`, put

```text
F_xi(g)=sum_d f(g,d) exp(2 pi i xi d).              (2.4)
```

Fourier orthogonality gives the exact weighted identity

```text
E_(Aff x Add)(f)=integral_0^1 E_Aff(F_xi) dxi.     (2.5)
```

This identity is useful, but Parseval alone does not make repeated affine
maps logarithmically cheap.  Put one unit coefficient at `(id,d)` for
`1<=d<=L`.  The affine projection has one element, while

```text
integral |F_xi(id)|^4 dxi
 =E^+([1,L])
 =(2L^3+L)/3.                                      (2.6)
```

So a tag fibre costs cubic additive energy, not its quadratic `ell^2`
mass.  This is sharp for arithmetic-progressive tags.

## 3. Why affine-group energy is not yet a closure theorem

The cited affine-energy theorem bounds, for a finite transformation set,

```text
max(E(A),E*(A)) << m^(1/2)|A|^(5/2)+M|A|^2,       (3.1)
```

where `m` is the largest equal-slope fibre and `M` the largest collinear
family in the affine-parameter plane.  This is an indicator-set theorem.
Applied uniformly to (2.5), taking absolute values replaces `F_xi(g)` by
`sum_d |f(g,d)|` and loses precisely the tag-fibre multiplicity.  Retaining
the Fourier average instead requires a new weighted version whose right
side detects the additive energy in (2.6).

The theorem also does not include the parabolic carrier multiplicity

```text
m_ch(C) << sqrt(D/h(e)).                           (3.2)
```

attached after the color square has been chosen.  At the critical scale,
(3.2) is `D^(3/8)`, exactly the factor that must be averaged rather than
inserted pointwise.

Moreover the two concentration terms in (3.1) are not both covered by the
existing affine/Hankel patch:

* an equal-slope fibre is a family of parallel rational affine maps; the
  proved patch closes the equal-direction translation-grid specialization,
  not every rational dilation fibre with its carrier weights;
* a general collinear family of affine parameters is a concurrent family of
  graph lines (a torus coset after conjugation).  Its natural merger is
  multiplicative/Helson-type, and no corresponding carrier theorem has been
  proved here.

Thus PRNRW supplies a useful structural dichotomy only after a weighted
incidence-to-carrier bridge and both structured operator patches are proved.
The `Aff x Add` augmentation adds a second exact dichotomy: low tag energy
is Fourier-summable, while high tag energy has additive inverse structure.
However, since `d=r_i s_j c`, additive structure in `d` is not additive
structure in the prime color `c` when slope scales vary.  Promoting it to a
rational-dilation carrier patch is the new missing inverse theorem.  Neither
PRNRW nor Parseval alone can currently be inserted into the exponent ledger
as a saving.

```text
critical integer covolume-moment countermodel:      PROVED;
countermodel lies below P=q/D:                      PROVED;
actual-prime covolume moment:                        OPEN;
affine-group composition embedding:                 PROVED;
Aff x Add tagged embedding and Fourier identity:     PROVED;
one-fibre cubic additive-energy barrier:             PROVED;
PRNRW theorem alone improves D^(11/8):              NO;
rational parallel/concurrent carrier patches:       OPEN;
high-tag-energy inverse-to-carrier theorem:          OPEN;
full four-cycle D^(1+o):                            OPEN.
```

The identities are replayed in
`src/qp_four_cycle_covolume_moment_barrier.py`,
`src/qp_four_cycle_affine_additive_energy.py`, and their tests.
