from qp_simultaneous_divisor_rdp import (
    endpoint_gcd_ledger,
    mixed_error_ledger,
    prime_scale_mixed_no_go,
    rectangular_mixed_remainder,
)


def test_endpoint_gcds_and_lcm_divide_residual_determinant() -> None:
    ledger = endpoint_gcd_ledger((30, 42), (35, 25))
    assert ledger.base_determinant == 0
    assert ledger.left_gcd == 6
    assert ledger.right_gcd == 5
    assert ledger.gcd_lcm == 30

    residual = endpoint_gcd_ledger((6, 10), (9, 3))
    assert residual.base_determinant == 24
    assert residual.base_determinant % residual.gcd_lcm == 0


def test_exact_mixed_error_expansion_and_rectangular_cancellation() -> None:
    base = mixed_error_ledger(
        377, (391, 440), (449, 399), 377, (449, 399), 377, (391, 440)
    )
    cross = mixed_error_ledger(
        377, (391, 440), (449, 399), 349, (485, 431), 440, (335, 377)
    )
    assert base.left_errors == (0, 0)
    assert base.right_errors == (0, 0)
    assert cross.left_errors == (-8, -4)
    assert cross.right_errors == (-7, 0)
    assert rectangular_mixed_remainder(
        base.left_errors,
        cross.left_errors,
        base.right_errors,
        cross.right_errors,
    ) == 56


def test_prime_q_hard_window_disproves_automatic_mixed_vanishing() -> None:
    fixture = prime_scale_mixed_no_go()
    assert fixture.q == 809
    assert fixture.D**2 < fixture.q
    assert max(abs(value) for value in fixture.residuals) <= fixture.q * fixture.D
    assert fixture.cross_determinants == ((-1, -8), (-5, -12))
    assert fixture.mixed_remainder == 56
