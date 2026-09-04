#!/usr/bin/env python3
"""Replay the first A1 cell and the cheap BP conversion falsifiers.

This is a finite/exponent audit, not a proof or disproof of the sharp
four-cycle bound.  It freezes one literal all-prime four-completion cell,
checks that its off-axis mask is genuinely joint, and compares two known
scalar conversion costs with the Blomer--Pascadi exponent headroom.
"""

from __future__ import annotations

import math
import sys
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from qp_actual_prime_nds import (  # noqa: E402
    actual_prime_residual_double_star,
    four_completion_chains,
)
from qp_bp_rounding_hsm_ledger import shell_modulus_ledger  # noqa: E402
from qp_four_cycle_bp_bridge import reciprocal_layer_identity  # noqa: E402
from qp_four_completion_bezout_normal_form import (  # noqa: E402
    BezoutFourCompletionChart,
    prime_nonzero_mixed_remainder_fixture,
)
from qp_tagged_trace_projective_barrier import (  # noqa: E402
    paley_tagged_trace_ledger,
    principal_paley_hard_window_fixture,
)


def block_triangle_cost(modulus: int, block_length: int) -> float:
    """Exact l1(l2-block)/global-l2 ratio for a flat Fourier vector."""

    full_blocks, remainder = divmod(modulus, block_length)
    numerator = full_blocks * math.sqrt(block_length)
    if remainder:
        numerator += math.sqrt(remainder)
    return numerator / math.sqrt(modulus)


def balanced_bp_adapter(alpha: Fraction) -> Fraction:
    """Net exponent relative to the local D-Weil scale.

    One side is zero-padded from D=q^(16/33) to H=q^alpha and the full
    side is triangle-summed over H-blocks.  The three terms are the
    relative exponents in the balanced BP theorem.
    """

    d = Fraction(16, 33)
    conversion = (alpha - d) + (1 - alpha) / 2
    bp_terms = (
        Fraction(13, 32) - 7 * alpha / 8,
        Fraction(5, 16) - 11 * alpha / 16,
        Fraction(1, 9) - alpha / 3,
    )
    return conversion + max(bp_terms)


def main() -> None:
    fixture = actual_prime_residual_double_star()
    chart = BezoutFourCompletionChart.from_anchor(fixture.central.colors)
    chains = four_completion_chains(
        fixture.q,
        fixture.D,
        fixture.primes,
        fixture.central.colors,
    )
    off_axis = tuple(chain for chain in chains if chain.endpoint_determinant != 0)
    centers = tuple(sorted({chain.centers for chain in off_axis}))
    endpoints = tuple(sorted({chain.next_colors for chain in off_axis}))
    mask = tuple(
        tuple(
            int(
                any(
                    chain.centers == center and chain.next_colors == endpoint
                    for chain in off_axis
                )
            )
            for endpoint in endpoints
        )
        for center in centers
    )

    expected_mask = (
        (0, 0, 1, 1),
        (0, 0, 1, 1),
        (1, 1, 0, 1),
        (1, 1, 1, 0),
    )
    expected_center_tokens = ((-216, 35), (-180, 29), (-72, 11), (-36, 5))
    expected_endpoint_tokens = ((216, -35), (180, -29), (72, -11), (36, -5))
    center_tokens = tuple(chart.center_token(center) for center in centers)
    endpoint_tokens = tuple(chart.partner_token(endpoint) for endpoint in endpoints)

    if len(chains) != 14 or len(off_axis) != 10:
        raise SystemExit("FAIL: the frozen actual-prime cell changed")
    if mask != expected_mask:
        raise SystemExit("FAIL: the frozen off-axis mask changed")
    if center_tokens != expected_center_tokens:
        raise SystemExit("FAIL: the center-token list changed")
    if endpoint_tokens != expected_endpoint_tokens:
        raise SystemExit("FAIL: the endpoint-token list changed")

    # The first two rows agree, so rank <= 3.  The last three rows and the
    # last three columns have determinant 2, so rank >= 3.  In particular
    # the mask is not one factor alpha(P) beta(R).
    minor_determinant = 2
    if minor_determinant == 0:
        raise AssertionError("the exact rank witness vanished")
    frobenius = math.sqrt(10)
    nuclear = math.sqrt(17) + 1
    actual_nuclear_ratio = nuclear / frobenius

    mixed = prime_nonzero_mixed_remainder_fixture()
    if mixed.ledger.delta * mixed.ledger.h != -2592:
        raise SystemExit("FAIL: the literal mixed remainder changed")
    if not mixed.base_diamond.holds or not mixed.next_diamond.holds:
        raise SystemExit("FAIL: a literal hard window no longer holds")

    first_layer = reciprocal_layer_identity(
        center_prime=mixed.q,
        first_row=mixed.base_row,
        second_row=mixed.next_row,
        carrier=mixed.center[0],
        first_color=mixed.anchor[0],
        second_color=mixed.partner[0],
    )
    second_layer = reciprocal_layer_identity(
        center_prime=mixed.q,
        first_row=mixed.base_row,
        second_row=mixed.next_row,
        carrier=mixed.center[1],
        first_color=mixed.anchor[1],
        second_color=mixed.partner[1],
    )
    if not (first_layer.unit_shift and second_layer.unit_shift):
        raise SystemExit("FAIL: the two frozen reciprocal shifts stopped being units")
    if first_layer.congruence_error or second_layer.congruence_error:
        raise SystemExit("FAIL: a reciprocal-layer congruence failed")
    if (first_layer.shift, first_layer.multiplier) != (180, 2160):
        raise SystemExit("FAIL: the first frozen reciprocal layer changed")
    if (second_layer.shift, second_layer.multiplier) != (144, 2592):
        raise SystemExit("FAIL: the second frozen reciprocal layer changed")
    if first_layer.multiplier == second_layer.multiplier:
        raise SystemExit("FAIL: the two reciprocal numerators unexpectedly merged")

    bp = shell_modulus_ledger()
    one_side_loss = Fraction(17, 66)
    loss_beyond_margin = one_side_loss - bp.conditional_margin
    if bp.conditional_margin != Fraction(1, 352):
        raise SystemExit("FAIL: the BP exponent margin changed")
    if loss_beyond_margin != Fraction(269, 1056):
        raise SystemExit("FAIL: the direct block deficit changed")

    # The balanced objective is piecewise linear.  Its only possible
    # interior minimum is the b_2=b_3 breakpoint alpha=29/51; checking it
    # against both endpoints and the b_1=b_2 breakpoint alpha=1/2 gives the
    # exact optimum below.
    balanced_candidates = (
        Fraction(16, 33),
        Fraction(1, 2),
        Fraction(29, 51),
        Fraction(1, 1),
    )
    balanced_values = tuple(
        balanced_bp_adapter(alpha) for alpha in balanced_candidates
    )
    balanced_optimum = min(zip(balanced_values, balanced_candidates))
    if balanced_optimum != (Fraction(124, 561), Fraction(29, 51)):
        raise SystemExit("FAIL: the optimized balanced BP adapter changed")
    balanced_target_deficit = balanced_optimum[0] + bp.required_saving
    if balanced_target_deficit != Fraction(265, 1122):
        raise SystemExit("FAIL: the optimized balanced target deficit changed")

    # On the final branch of the asymmetric theorem the alpha dependence
    # cancels: 1/66+(1-alpha)/2+(alpha/2-61/198)=41/198.
    asymmetric_net = Fraction(1, 66) + Fraction(1, 2) - Fraction(61, 198)
    asymmetric_target_deficit = asymmetric_net + bp.required_saving
    if asymmetric_net != Fraction(41, 198):
        raise SystemExit("FAIL: the asymmetric BP plateau changed")
    if asymmetric_target_deficit != Fraction(2, 9):
        raise SystemExit("FAIL: the asymmetric BP target deficit changed")

    elementary_target_deficit = Fraction(1, 33)

    modulus = fixture.central.colors[0]
    finite_block_cost = block_triangle_cost(modulus, fixture.D)
    finite_allowance = fixture.q ** float(bp.conditional_margin)
    if finite_block_cost <= finite_allowance:
        raise SystemExit("FAIL: the finite point-mass block test unexpectedly passed")

    # This is a four-hard-window integer-mask method obstruction, not an
    # actual-prime-power counterexample.  It rules out lossless scalarization
    # from the window/Bezout identities alone.
    paley_prime = 43
    paley = paley_tagged_trace_ledger(paley_prime)
    paley_fixture = principal_paley_hard_window_fixture(paley_prime)
    paley_allowance = paley_fixture.q ** float(bp.conditional_margin)
    if not paley_fixture.distinct_bands or paley_fixture.D**2 >= paley_fixture.q:
        raise SystemExit("FAIL: the Paley hard-window fixture is invalid")
    if paley.rigorous_ratio_lower_bound <= paley_allowance:
        raise SystemExit("FAIL: the Paley scalarization lower bound no longer beats BP room")

    print("PASS QP A1 first-cell and fast-falsifier replay")
    print(
        "actual cell: "
        f"q={fixture.q}, D={fixture.D}, chains={len(chains)}, "
        f"off_axis={len(off_axis)}"
    )
    print(f"center tokens={center_tokens}")
    print(f"endpoint tokens={endpoint_tokens}")
    print(f"joint mask={mask}")
    print(
        "joint-mask rank=3, "
        f"nuclear/HS=(sqrt(17)+1)/sqrt(10)={actual_nuclear_ratio:.12f}"
    )
    print(
        "mixed remainder: "
        f"delta*h={mixed.ledger.delta * mixed.ledger.h}, D^2<q="
        f"{mixed.D**2 < mixed.q}"
    )
    print(
        "reciprocal layers at common modulus "
        f"{first_layer.modulus}: (v,lambda)="
        f"({first_layer.shift},{first_layer.multiplier}),"
        f"({second_layer.shift},{second_layer.multiplier})"
    )
    print(
        "BP powers: "
        f"saving={bp.dominant_saving}, required={bp.required_saving}, "
        f"margin={bp.conditional_margin}"
    )
    print(
        "point-mass block conversion: "
        f"loss=q^(17/66), deficit=q^({loss_beyond_margin}), "
        f"finite_cost={finite_block_cost:.12f}, "
        f"finite_allowance={finite_allowance:.12f}"
    )
    print(
        "optimized scalar adapters: "
        f"balanced alpha={balanced_optimum[1]}, "
        f"target_deficit={balanced_target_deficit}; "
        f"asymmetric_target_deficit={asymmetric_target_deficit}; "
        f"full_length_Parseval_target_deficit={elementary_target_deficit}"
    )
    print(
        "Paley four-window scalarization control: "
        f"p={paley_prime}, D={paley_fixture.D}, "
        f"rigorous_projective/HS>{paley.rigorous_ratio_lower_bound:.12f}, "
        f"BP_allowance={paley_allowance:.12f}"
    )


if __name__ == "__main__":
    main()
