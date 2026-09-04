# QP balanced tensor: joint-character and dual-entropy gate

**Date:** 2026-08-15  
**Verdict:** the exact joint character sum does not presently give a
coefficient-uniform power improvement over the proved `sqrt(R)` Schur bound.
Gauss inversion turns the residual character coefficient into an **additive
product phase**, not a reciprocal phase.  At the coefficient layer where the
Schur argument can be sharp, the resulting four-variable Fourier box has
cardinality `Q^(98/99)` inside modulus `Q=q^3`.  It is below the ordinary
Fourier/sum-product entropy threshold by `Q^(1/99)`.  None of the checked
large-sieve, prime-field multilinear, fixed-prime-power twisted-moment, or
spectral-reciprocity theorems covers this box while retaining three arbitrary
coefficient vectors.

This is a theorem-range and method barrier.  It is not an actual-node lower
bound, and it proves no QP or strip statement.

---

## 1. Scales and the exact identity

Let

```text
q be an odd prime,                 Q=q^3,
Y=q/2,                             B=Y^A,
h=2-A in (0,1/2),                 R=q^h,
H=qR=q^(1+h),                     K=Q/H=q^(2-h)=q^A.       (1.1)
```

Let `I` be the unit residuals represented by
`0<|r|<=C_w H` modulo `Q`, and put

```text
Ihat(m)=sum_(r in I) e_Q(-mr),     e_Q(u)=exp(2 pi i u/Q). (1.2)
```

For arbitrary complex coefficient vectors on the actual prime-power shell,
the hard all-plus tensor has the exact additive completion

```text
T(x,y,z)
 = Q^-1 sum_(m mod Q) Ihat(m)
       sum_(a,b,c) x_a y_b z_c e_Q(8mabc).                 (1.3)
```

This is just finite Fourier inversion of `1_I(8abc)`, but it is important for
auditing the multiplicative-character proposal.  If `chi` is primitive modulo
`Q` and

```text
D(chi)=sum_(r in I)chi(r),
```

then the Gauss identity gives

```text
conjugate(D(chi))
 = tau(conjugate(chi))/Q
   sum_((m,q)=1) Ihat(m)chi(m).                            (1.4)
```

Primitive-character orthogonality, including its induced-character
subtraction, gives

```text
1/phi(Q) sum_(chi primitive mod Q)
  tau(conjugate(chi))chi(n)=e_Q(n),       (n,q)=1.         (1.5)
```

Indeed, the subtraction consists of the `q` lifts of one class modulo `q^2`,
whose additive phases sum to zero.  Consequently the primitive block of the
character identity is precisely the unit-frequency part of (1.3).  The phase
is

```text
e_Q(8mabc),                                               (1.6)
```

not `e_Q(m inverse(abc))`.  The lower-conductor character blocks correspond
to nonunit additive frequencies.

For a smooth residual cutoff, (1.2) is effectively supported on `|m|<<K`.
For the hard unit interval, writing it as the full interval minus its
multiples of `q` gives the more accurate bound

```text
|Ihat(m)|
 <<min(H,Q/||m||_Q)+min(H/q,q^2/||m||_(q^2)).             (1.7)
```

In particular, on a sufficiently short fixed fraction of the unit-frequency
range `0<|m|<=K`, the full-interval term has size comparable with `H` and the
deleted-multiple term is only `O(H/q)`.  Thus the first block has length
comparable with `K` and weight comparable with `H`.  Any proof which takes
absolute values after a dyadic frequency decomposition must control this
block.  This does not rule out a new argument exploiting signed cancellation
between different frequency blocks.

---

## 2. The critical box is below Fourier entropy

The raw integer geometry proves

```text
|T(x,y,z)|<<_w sqrt(R)||x||_2||y||_2||z||_2.              (2.1)
```

The restricted-set interpolation behind (2.1) can be sharp at the level of
its inputs when each coefficient support has size

```text
X=Y=Z=R.                                                  (2.2)
```

On the main additive-frequency block, the four summation-set sizes then have
product

```text
K R^3=q^(2-h+3h)=q^(2+2h)=Q^((2+2h)/3).                  (2.3)
```

Since `h<1/2`, this is strictly smaller than `Q`.  At the active aperture
`A=50/33`,

```text
h=16/33,
K R^3=q^(98/33)=Q^(98/99),
Q/(K R^3)=q^(1/33)=Q^(1/99).                             (2.4)
```

The same deficit appears after the most favorable elementary grouping.  Put
`u=ma` and `v=bc`.  Bounded divisor multiplicity costs only `q^o(1)`, while

```text
number of possible u <= K R=q^2,
number of possible v <= R^2=q^(32/33),
|U||V| <=q^(98/33)=Q/q^(1/33).                           (2.5)
```

Thus the grouped sum is a subcritical submatrix of the `Q`-point Fourier
matrix.  The universal bilinear estimate

```text
|sum_(u,v) A_u B_v e_Q(uv)|
 <=sqrt(Q)||A||_2||B||_2                                 (2.6)
```

is nontrivial against the flat trivial bound only once `|U||V|>Q`; at (2.5)
it misses that threshold by `q^(1/33)`.  This does not prove that the special
product sets fail to cancel.  It proves that Fourier unitarity or a generic
large sieve alone cannot certify the needed cancellation.

There is a second quantitative mismatch.  Suppose a multilinear theorem for
flat supports supplied a relative saving `rho` against the trivial
four-variable sum.  After the factor `1/K` in (1.3) and `ell^2`
normalization, the critical layer would give

```text
|T|<<R^(3/2) rho.                                        (2.7)
```

To reach even the existing Schur scale requires

```text
rho<=R^-1=q^-h=Q^(-h/3).                                 (2.8)
```

At the active aperture this is `Q^(-16/99)`.  A strict power improvement
would require `Q^(-16/99-eta/3)`.  Therefore even a hypothetical theorem
giving an unspecified tiny saving at this box would not automatically improve
(2.1).

---

## 3. Positive joint moments do not repair the loss

The exact character formula is

```text
T=phi(Q)^-1 sum_chi
  conjugate(D(chi))chi(8)X(chi)Y(chi)Z(chi).              (3.1)
```

Parseval gives

```text
E_chi |D(chi)|^2 asy H.                                  (3.2)
```

Combining `D` with one node polynomial before Cauchy does retain the actual
product structure: because `ra<Q`, the congruence `ra=sb (mod Q)` is an
integer equality and divisor multiplicity gives

```text
E_chi |D(chi)X(chi)|^2
 <<q^o(1) H||x||_2^2.                                    (3.3)
```

It does not save a power.  The diagonal `r=s, a=b` already has the scale on
the right.  The same diagonal remains in higher positive multiplicative
energies.  Hence Hölder, Cauchy, amplification followed by absolute values,
and weighted-energy estimates that discard the sign of (3.1) bottom out at
the previously recorded `sqrt(H)` scale, a factor `q^(1/2)` worse than
`sqrt(R)`.

Coefficient adaptivity also prevents a pointwise incompatibility assertion.
For every selected character `chi_0`, choosing
`x_a=conjugate(chi_0(a))/sqrt(X)` on any `X` nodes makes
`|X(chi_0)|=sqrt(X)`, and the same can be done independently in the other
two slots.  Thus a successful amplifier must prove cancellation across the
whole signed character average; it cannot merely say that a character with
large `D(chi)` cannot carry large restricted transforms.

---

## 4. Checked primary theorems and their exact mismatch

1. [Bourgain--Garaev, *Kloosterman sums in residue rings*, Lemma
   1](https://arxiv.org/abs/1309.1124) quotes Bourgain's general-modulus
   sum-product theorem in the following useful form: for every `gamma>0`
   there are `epsilon,tau>0` and a number of factors `k=k(gamma)` such that a
   `k`-fold product phase has a power saving, under nonconcentration in every
   large quotient.  It does not assert the result for four factors.  The
   balanced tensor has exactly the four factors `m,a,b,c`; adding factors by
   absolute Cauchy reintroduces the diagonal in Section 3.

2. [Bourgain's optimal-entropy prime-field theorem, as stated in the
   introduction of Kerr--Macourt](https://arxiv.org/abs/1901.00975), treats
   `e_p(x_1...x_n)` when every source has positive entropy and their product
   exceeds `p^(1+epsilon)`.  [Kerr--Macourt's weighted
   refinements](https://arxiv.org/abs/1901.00975) likewise work in the prime
   field `F_p`.  Our phase has modulus `q^3`, and the critical cardinality is
   below that modulus by (2.4).  Moreover `K<q^2`, so the effective nonzero
   frequencies contain no multiple of `q^2`; none of the main primitive
   block descends to a prime-field phase modulo `q`.

3. [Gao--Zhao, *Twisted fourth moment of Dirichlet L-functions to a fixed
   modulus*, Theorem 1.1](https://arxiv.org/abs/2507.18186) assumes a modulus
   `q_0^n_0` with `n_0>=50`, twists by two fixed integers `a,b`, and imposes
   `(ab)^7<<q^(min(1/576,1/n_0)-epsilon)`.  Here the depth is `n_0=3`, and
   (3.1) contains three arbitrary length-`q` coefficient vectors.  Summing
   fixed-twist formulas does not preserve the theorem's twist range.

4. [Milicevic's p-adic exponent-pair
   theory](https://arxiv.org/abs/1407.4100) estimates one-variable
   p-adically analytic phases in the depth aspect; its stated subconvex bound
   contains a fixed power of the base prime in front.  It supplies no
   coefficient-uniform four-variable theorem when the depth is fixed at
   three and the base prime grows.

5. Recent bilinear Kloosterman estimates such as [Blomer--Pascadi, Theorem
   1.1](https://arxiv.org/abs/2607.24311) estimate bilinear forms in complete
   rank-two Kloosterman sums.  Equation (1.6) is an incomplete rank-one
   additive product phase.  Introducing the extra complete variable needed
   to manufacture a Kloosterman sum changes the kernel and restores the
   zero/degenerate modes; the cited theorem is not a bound for (1.3).

6. Power-modulus large sieves average one common coefficient polynomial over
   varying moduli.  In the transverse dual problem the node set and all three
   dual coefficient vectors may depend on `q`.  Allowing a different vector
   in every modulus turns the direct sum into a block-diagonal operator and
   removes cross-modulus cancellation.  Thus these results give neither an
   every-prime theorem nor a density-one theorem uniform over all admissible
   duals.

Spectral reciprocity has the same coefficient mismatch: the checked formulas
exploit approximate-functional-equation divisor coefficients or fixed twists,
not three freely chosen shell vectors.  No checked theorem accepts all five
features simultaneously:

```text
fixed modulus q^3 of depth exactly 3;
frequency length q^(50/33);
three independent actual-node coefficient vectors;
the rank-one phase e_(q^3)(8mabc);
coefficient-uniform saving beyond sqrt(R).                (4.1)
```

---

## 5. Binary conclusion

At `A=50/33`:

```text
exact character-to-additive product identity:       PROVED;
reciprocal phase after Gauss inversion:              FALSE;
critical dual entropy Q^(98/99):                     PROVED;
generic Fourier/large-sieve cancellation there:      OUT OF RANGE;
positive joint-energy gain over sqrt(H):             NO;
checked literature theorem covering (4.1):           NONE FOUND;
balanced tensor bound below sqrt(R):                 NOT PROVED;
full-shell transverse exponent below 49/66:          NOT PROVED;
actual-node saturation at sqrt(R):                   NOT PROVED;
QP or strip consequence:                             NOT PROVED.          (5.1)
```

The missing input can now be stated precisely: a fixed-depth `q^3`
restriction/dispersion estimate for the **subcritical**, rank-one product box
in (2.3), strong enough to save at least `Q^(16/99+eta)` relative to the flat
sum while retaining arbitrary coefficients.  Existing separate character
bounds, positive energies, and generic Fourier estimates do not provide it.

Executable checks:

```bash
PYTHONPATH=src python3 -m pytest -q \
  src/test_qp_balanced_joint_character_gate.py
```

The tests replay the exact rational exponent ledger, finite Fourier
inversion, the primitive-character/unit-frequency identity for small prime
cubes, and the active entropy deficits.
