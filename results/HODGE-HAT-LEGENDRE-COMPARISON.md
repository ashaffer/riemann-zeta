# Hodge hat/Legendre fail-fast comparison

## Verdict

The positive hat scans were stable as *hat-section* calculations, but they
missed an admissible boundary-jump direction.  A cutoff-free, zero-extended
plain-Legendre section finds the complete strengthened event-row ratio above
one.  Thus more work on the selected rank-four determinants is not a useful
way to rescue this strengthened propagation criterion.

The numerical sign is not an interval-arithmetic certificate.  It is,
however, separated from zero by about `9e-5`, stable under independent degree
and quadrature ladders, and four orders of magnitude larger than the numerical
uncertainty visible in the nearly saturated ordinary row.  It is decisive
fail-fast evidence for pruning the route.

## 1. What the hat scan actually established

`src/hodge_low_sector_falsifier.py` eliminates the exact finite-section costs
of all old modes numbered `j >= 4`, then computes both selected parity Grams,
the complete strengthened row, and a separate `mu=3` medium/high split.  On
the activation of `5`, with matched collar mesh ratio `.42`, cutoff
`800+(20/3)N`, and interval density `30`, it gives:

| old degree `N` | collar degree | fifth Ritz value | fifth gap | odd `det(I-G)` | even `det(I-G)` | odd low ratio | even low ratio | complete ratio | complete minimum |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 61 | 13 | .105228 | .101754 | .0330934 | .396627 | .966550 | .601177 | .993846 | 7.493e-3 |
| 91 | 19 | .0984148 | .0952345 | .0106516 | .134364 | .988994 | .865260 | .998138 | 2.317e-3 |
| 121 | 26 | .0950960 | .0920545 | .00573408 | .0517653 | .993720 | .948079 | .998993 | 1.262e-3 |
| 151 | 33 | .0931015 | .0901453 | .00387672 | .0231911 | .995237 | .976696 | .999264 | 9.255e-4 |
| 181 | 39 | .0917347 | .0888385 | .00285494 | .0116819 | .995774 | .988190 | .999364 | 8.027e-4 |
| 211 | 46 | .0907333 | .0878821 | .00207439 | .00644277 | .996069 | .993410 | .999420 | 7.332e-4 |
| 241 | 53 | .0899866 | .0871693 | .00152848 | .00394108 | .996216 | .995913 | .999451 | 5.903e-4 |
| 301 | 66 | .0889669 | .0861965 | .000903878 | .00206864 | .996389 | .997828 | .999490 | 3.133e-4 |

There is no negative hat section in this ladder.  There are nevertheless
three warnings that were obscured by focusing on the degree-121 odd block:

1. both parity determinants collapse toward zero;
2. the even selected block overtakes the odd block by degree `301`;
3. the complete row approaches one more closely than either selected
   four-mode ratio because the medium modes matter.

The fifth gap remains near `.09` and the collar metric left after numerical
elimination of modes `j >= 4` remains positive (`.01555` at degree `61`,
`.01200` at degree `301`).  Hence the observed trend is not caused by a
closing rank-four spectral gap or an obviously singular finite collar solve.

## 2. Medium sector exposed rather than renamed high

The proved raw high estimate closes only above approximately `mu=3`; it does
not justify eliminating every mode after the fourth.  Splitting at `mu=3`
in the same finite matrices gives:

| `N` | modes below `3` | medium modes after the first four | exact high budget / raw collar | collar minimum after high | medium contraction | minimum after medium |
|---:|---:|---:|---:|---:|---:|---:|
| 61 | 46 | 42 | .05334 | .34992 | .96252 | .01555 |
| 121 | 59 | 55 | .08886 | .34808 | .96898 | .01298 |
| 181 | 68 | 64 | .09969 | .34712 | .97022 | .01246 |
| 241 | 72 | 68 | .10653 | .34680 | .97085 | .01217 |
| 301 | 73 | 69 | .11108 | .34655 | .97122 | .01200 |

This is stable finite-section evidence that the medium elimination is
positive.  It is not a proof: the medium contraction uses the same explicit
zeta cross matrices whose continuum control was at issue.

## 3. Hat mesh and Fourier controls do not explain the discrepancy

At old degree `121`, independently varying the collar mesh gives:

| mesh ratio | collar degree | odd determinant | even determinant | complete ratio |
|---:|---:|---:|---:|---:|
| .28 | 40 | .00563273 | .0515080 | .99901169 |
| .35 | 32 | .00568487 | .0516370 | .99900223 |
| .42 | 26 | .00573408 | .0517653 | .99899301 |
| .55 | 20 | .00580581 | .0520336 | .99897897 |
| .70 | 15 | .00590875 | .0522862 | .99895751 |

At the same degrees, scaling the Fourier cutoff while holding its integration
density at `30` gives:

| cutoff scale | odd determinant | even determinant | complete ratio |
|---:|---:|---:|---:|
| .50 | .00545936 | .0475014 | .99903402 |
| .75 | .00568348 | .0510177 | .99900073 |
| 1.00 | .00573408 | .0517653 | .99899301 |
| 1.25 | .00573592 | .0517673 | .99899260 |
| 1.50 | .00575081 | .0520077 | .99899040 |

Changing Simpson interval density through `10,20,30,60,120` changes none of
the displayed degree-121 quantities at eight significant digits.  Therefore
the positive hat sign is internally well resolved; it is the trial space,
not Simpson noise, that matters.

## 4. The direction the hats suppress

Every hat group used by `hodge_sector_scan.py` vanishes at the endpoints of
its interval.  The smooth polynomial-bump checks do the same.  A fixed
section therefore suppresses the old/collar boundary jump trace.

The plain-Legendre calculation instead zero-extends ordinary polynomials from
each interval.  Their endpoint jumps are allowed in the intended logarithmic
form domain: their Fourier transforms are `O(1/|xi|)`, so

`integral log(2+|xi|) |fhat(xi)|^2 dxi < infinity`.

The moment projection does not remove these jumps.  It only annihilates the
two exponential pole moments.  Approximating a jump with endpoint-vanishing
hats requires an increasingly thin boundary layer, so the approach of the
hat ratios to one from below is consistent with, rather than contrary to,
the Legendre counterdirection.

## 5. Corroborating cutoff-free Legendre ladders

With collar degree `20` and spatial quadrature order `128`, the complete
plain-Legendre result is:

| old degree | strengthened ratio | strengthened minimum | witness parity |
|---:|---:|---:|---:|
| 12 | .99957352 | 4.845e-4 | even |
| 16 | 1.00002092 | -3.357e-5 | odd |
| 20 | 1.00004713 | -8.021e-5 | odd |
| 24 | 1.00004976 | -8.601e-5 | odd |
| 28 | 1.00005212 | -8.820e-5 | odd |
| 32 | 1.00005750 | -8.947e-5 | odd |
| 36 | 1.00006073 | -9.076e-5 | odd |
| 40 | 1.00006094 | -9.097e-5 | odd |
| 48 | 1.00006161 | -9.255e-5 | odd |

At old degree `32`, changing the collar degree from `8` through `40` changes
the strengthened minimum only from `-8.94624e-5` to `-8.94670e-5`.  Changing
spatial order through `64,80,96,112,128,160,192,256` keeps it between
`-8.94661357e-5` and `-8.94661461e-5`.  The ordinary Schur minimum is only of
order `1e-8` and is not sign-resolved by this floating calculation, but that
uncertainty is immaterial to the much larger strengthened defect.

## 6. Consequence

The selected odd determinant was not the true continuum gate.  Even its
conjunction with the even determinant and a medium-sector theorem would not
prove the desired full-domain contraction, because an admissible jump mode
already violates the complete strengthened row.

The reusable outputs are:

- the algebraic high-tail estimate;
- the rank-four spectral-cluster observation;
- the ordinary Weil row's near-saturation;
- the diagnosis that the extra Hodge trace spends more than the ordinary
  reserve on an odd boundary-jump direction.

The strengthened criterion should be pruned.  A successor propagation route
must avoid requiring `X* A^-1 X + T* T <= C`, for example by cancelling the
return trace before it is charged or by supplying a genuinely new positive
capacity rather than spending the already saturated ordinary Weil reserve.
