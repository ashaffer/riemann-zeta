from fractions import Fraction

from qp_weighted_triangle_packet_inverse import (
    packet_safe_inverse_target,
    tangent_unconditionality_ledger,
)


def test_exact_tangent_packet_has_sqrt_degree_unconditionality_loss():
    ledger = tangent_unconditionality_ledger(12)
    assert ledger.product_window_holds
    assert ledger.labels_are_proper
    assert ledger.alternating_label_rectangles == 0
    assert ledger.all_plus_fourth == Fraction(2 * 12**4, 23**2)
    assert ledger.rademacher_fourth == Fraction(2 * 12**2, 23)
    assert ledger.unconditionality_ratio == Fraction(12**2, 23)


def test_loss_grows_linearly_in_packet_order():
    small = tangent_unconditionality_ledger(4)
    large = tangent_unconditionality_ledger(20)
    assert large.unconditionality_ratio > 4 * small.unconditionality_ratio


def test_target_explicitly_requires_packet_extraction():
    target = packet_safe_inverse_target()
    assert "extract" in target
    assert "remainder" in target
