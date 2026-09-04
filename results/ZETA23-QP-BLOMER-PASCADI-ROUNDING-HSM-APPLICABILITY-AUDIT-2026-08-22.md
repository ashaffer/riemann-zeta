# QP high-completion tail: Blomer--Pascadi rounding/HSM applicability audit

**Date:** 2026-08-22  
**Binary verdict:** **NO direct application to the exact remaining QP
kernel.**  The new theorem is numerically strong enough in one optimistic
shell-modulus model, but neither exact QP interface is a legal
Blomer--Pascadi bilinear form with an affordable total conversion cost.

The positive statement is precise.  If one could losslessly rewrite the
rounding graph as one fixed-modulus form

```text
sum_(m,n in length-D intervals) alpha_m beta_n S(am,n;q),
D=q^(16/33),                                           (0.1)
```

then [Blomer--Pascadi, Theorem 1.1](https://arxiv.org/abs/2607.24311)
would save

```text
q^(-19/1056+o(1)).                                   (0.2)
```

The known sparse-cell shortfall is only `q^(-1/66)`, so the conditional
headroom is

```text
19/1056-1/66=1/352.                                  (0.3)
```

But the exact rounding object is a nested reciprocal-carrier **graph** with
a joint `(e,k)` mask, not two free intervals and not a complete Kloosterman
kernel.  In the exact DFI/HSM completion, a genuine Kloosterman sum does
appear, but at modulus `C=q^(25/33)` its natural arguments have the wrong
length geometry and carry a four-fan correlation.  The unequal-length
version of the paper does not repair this.  Moving moduli and the
Ramanujan/main axes remain additional unresolved complements.

No slope-block, high-tail, four-cycle, or `5/8` theorem follows.

---

## 1. What the paper actually permits

Theorem 1.1 treats a **fixed** integer modulus `c`, two additive intervals
of length at most `N`, arbitrary scalar sequences `alpha_m,beta_n`, a unit
`a mod c`, and the complete kernel

```text
S(am,n;c)=sum_(x mod c)^* e_c(amx+n inverse(x)).      (1.1)
```

At `N=sqrt(c)` its bound is

```text
||alpha||_2 ||beta||_2 c^(1-1/32+o(1)).             (1.2)
```

Arbitrary scalar coefficients are genuinely helpful: rough prime weights
are not an objection once they have become one sequence in each of the two
interval variables.  This does **not** cover an arbitrary joint matrix
weight `W(m,n)`, a vector kernel whose action changes with an external fan
index, or a family whose modulus is itself an unsummed outer variable.

For general translated intervals the theorem also retains
`(m,n,c)=1`.  Its removal without this restriction is stated for initial
intervals `{1,...,N}`, not for the signed intervals through zero that occur
in the HSM variables.  Thus zero and noncoprime axes cannot be silently put
inside (1.2).

## 2. Optimistic shell-modulus ledger: numerically yes, algebraically no

Take `c~q` and `N=D=q^(16/33)`.  Relative to the Weil/Cauchy scale, the
three factors in Theorem 1.1 have exact exponents

```text
13/32-(7/8)(16/33)   = -19/1056,
5/16 -(11/16)(16/33) = -1/48,
1/9  -(1/3)(16/33)   = -5/99.                      (2.1)
```

The first term dominates, proving (0.2) in the hypothetical model.  This is
the only interface with favorable numerical room, and (0.3) shows that its
total conversion budget is extremely small.

The exact shell-rounding chart instead has

```text
m(e)=R(e),             n(k)=R(k),
f(e,k)=eR(k)-kR(e),                                  (2.2)
```

and the actual incidence is the nested mask

```text
W(e,k)=1_{a_e,A_e,c'_k,d'_k,b_e,b'_(e,k) actual}
       *1_{four reciprocal product windows}.         (2.3)
```

The second carrier `b'_(e,k)` depends jointly on `(e,k)`.  The condition
`|f(e,k)|<<D` is automatic on the hostile Beatty family and creates no
complete internal unit sum such as (1.1).  Fourier completion introduces a
zero/main frequency and leaves the carrier detector coupled to the same
lift.  It has not factored (2.3) as `alpha_e beta_k`.

Writing a general joint mask as a sum of rank-one scalar masks is not free.
The theorem controls each rank-one term by its scalar norms, so the relevant
cost is a projective/nuclear norm.  The generic rank is as large as `D`;
even a square-root rank cost is `D^(1/2)=q^(8/33)`, overwhelmingly larger
than the entire `q^(1/352)` allowance in (0.3).  No low-rank theorem for the
nested actual-prime mask is known.

Finally, the modulus in this chart is an actual row/color coordinate and
moves with the outer pair.  Uniformity of a fixed-`c` estimate permits
applying it separately; it does not supply a square function or cancellation
over those moving moduli.  There is no normalized fixed-modulus reduction to
which (2.1) can presently be applied.

## 3. Exact top-DFI/HSM kernel: genuine Kloosterman, wrong variables

The fully transformed coprime top block does contain the exact identity

```text
1/c sum_(a mod c)^*
 e_c(-a h-a_bar (RS)^(-1) Delta)
   =S(-h,-(RS)^(-1)Delta;c)/c,                     (3.1)

Delta=nu*mu-nu'*mu'.                               (3.2)
```

At the balanced point,

```text
c~C=q^(25/33),
|nu|,|mu|,|nu'|,|mu'|<=V=q^(8/33)=C^(8/25),
|Delta|<=V^2=D=q^(16/33)=C^(16/25).                (3.3)
```

Neither native scale is a legal critical BP box:

* a single fan interval has exponent `8/25`, below the paper's balanced
  lower threshold `13/28` by `101/700` in `C`;
* the pushed-forward product-difference interval has exponent `16/25`,
  above the balanced useful range;
* Theorem 5.5 for unequal lengths contains the term
  `N^(1/3)/C^(1/5)`.  At `N=C^(16/25)` this is `C^(1/75)`, so that theorem
  is already worse than the fixed-modulus opening bound.

Splitting the `Delta` range into critical `sqrt(C)` intervals is also
quantitatively impossible with arbitrary coefficients.  There are

```text
C^(16/25-1/2)=C^(7/50)                              (3.4)
```

blocks.  Even if only this one axis were long, Cauchy across its blocks
costs `C^(7/100)`, while the critical saving is only `C^(-1/32)`.  The net
factor is a **loss**

```text
C^(7/100-1/32)=C^(31/800).                          (3.5)
```

If both axes require the subdivision, the loss is larger.

## 4. Why “arbitrary sequences” does not remove the four-fan gate

To use (3.1) with `Delta` as one scalar BP variable, the four fan weights
must first be pushed forward through (3.2).  For a product sequence

```text
p_t=sum_(nu*mu=t) x_nu y_mu,
```

the `Delta` coefficient is the autocorrelation

```text
B_Delta=sum_t p_(t+Delta) conjugate(p_t).           (4.1)
```

Blomer--Pascadi accepts `B_Delta` once its scalar `l2` norm is known, but it
does not prove the required norm estimate.  The generic Young bound loses a
full fan length `V` after normalization.  More conceptually, retaining the
fan indices as an external Hilbert coordinate is not a free tensorization:
the scalar kernel itself depends on those indices through
`nu*mu-nu'*mu'`, and the CRT permutation changes with `c`.

The paper's own fourth trace is already spent proving the scalar operator
norm (1.2).  It cannot be reused as a cost-free vector/four-fan moment for a
different nonlinear pushforward.  What would suffice here is a new
fan-aware vector Blomer--Pascadi theorem or a prior mask-preserving
factorization of (4.1) with subpower projective norm.

## 5. Moving modulus and main-term complements

The exact DFI coefficient is

```text
H_DFI(c/C,n/C^2),                                   (5.1)
```

where the mismatch `n` depends on the primal product variables.  It is not
a fixed scalar coefficient independent of the two BP variables.  The exact
delta identity contains all lower `c` blocks, and noncoprime blocks have
conductor-lowered complete sums.  The fixed-modulus theorem provides no
inter-modulus cancellation and no license to discard these blocks.

There are also genuine main axes:

```text
Delta=0:  S(-h,0;c)=c_c(h),
h=Delta=0: S(0,0;c)=phi(c).                         (5.2)
```

They violate the coprime input condition and are not covered by a
nondegenerate `c^(-1/32)` saving.  In the QP identity the `h=0` contribution
is tied to the product diagonal, while the remaining Ramanujan axes must be
combined with the signed zero-integral band-pass before absolute values are
taken.  A per-modulus BP application followed by triangle inequality would
destroy that cancellation.  The exact DFI zero-arc audit likewise shows
that the surviving zero arc reconstructs the original HSM gate; it is not
a negligible error term.

## 6. Exact disposition

```text
BP accepts arbitrary scalar l2 sequences:                 YES;
optimistic modulus-q, length-D saving:                     q^(-19/1056);
conditional room beyond the q^(-1/66) local gap:           q^(-1/352);
rounding mask separates as alpha_e beta_k:                 NO;
rounding graph contains a complete Kloosterman kernel:     NO;
fixed shell modulus survives the outer pair sum:           NO PROOF;
top DFI block contains a genuine Kloosterman sum:          YES;
native fan length lies in BP range at modulus C:           NO;
Delta pushforward lies in a useful balanced BP range:      NO;
unequal Theorem 5.5 repairs the lengths:                   NO, C^(1/75) term;
critical-block subdivision preserves the saving:          NO, C^(31/800) loss;
four-fan pushforward has subpower scalar/projective cost:   OPEN;
lower/noncoprime/moving-c blocks and main axes bounded:     OPEN;
direct BP improvement of rounding/HSM/four-cycle:          NO.
```

The exponent calculations are replayed in
`src/qp_bp_rounding_hsm_ledger.py` and its test module.
