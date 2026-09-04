from qp_fold_height_divisor_count import (
    fold_height_divisor_data,
    fold_height_divisor_majorant,
    fold_height_energy_exponents,
    reconstruct_fold_height_points,
)


def test_report_fixture_and_its_signed_reflection() -> None:
    point = fold_height_divisor_data(Q=30, p=5, d=2, a=1, w=1)
    assert (point.g, point.y, point.e, point.f) == (2, 11, 2, 12)
    assert point.small_left_factor == point.small_left_target == 57
    assert point.large_left_factor == point.large_left_target == 84

    reflected = fold_height_divisor_data(Q=30, p=5, d=-2, a=-1, w=-1)
    assert (reflected.g, reflected.y) == (2, -11)
    assert (reflected.e, reflected.f) == (12, 2)


def test_zero_w_and_zero_eta_are_counted_by_nonzero_targets() -> None:
    # a*(p^2-d^2)=2*d*(Q/p): 2*8=2*1*8.
    zero_w = fold_height_divisor_data(Q=24, p=3, d=1, a=2, w=0)
    assert zero_w.e == zero_w.f == 0
    assert zero_w.small_left_target == 2 * zero_w.Q

    # The standard fixture has no zero eta; construct one by scanning a
    # small exact reconstruction and check any available e=0, w!=0 point.
    points = reconstruct_fold_height_points(Q=120, A=25, B=100)
    zero_eta = [point for point in points if point.w and point.eta_left == 0]
    for point in zero_eta:
        assert point.e == 0
        assert point.large_left_target == 2 * point.Q


def test_divisor_reconstruction_contains_direct_bounded_scan() -> None:
    Q, A, B = 120, 25, 100
    reconstructed = {
        (point.p, point.d, point.a, point.w)
        for point in reconstruct_fold_height_points(Q, A, B)
    }
    direct: set[tuple[int, int, int, int]] = set()
    for p in range(1, Q + 1):
        if Q % p:
            continue
        for d in range(-p + 1, p):
            if d == 0:
                continue
            for a_abs in range(1, 101):
                a = a_abs if d > 0 else -a_abs
                numerator = 2 * d * (Q // p) - a * (p * p - d * d)
                if numerator % 3:
                    continue
                w = numerator // 3
                try:
                    point = fold_height_divisor_data(Q, p, d, a, w)
                except (ValueError, AssertionError):
                    continue
                if abs(point.e) <= A and abs(point.f) <= B:
                    direct.add((p, d, a, w))
    assert direct <= reconstructed
    assert len(reconstructed) <= fold_height_divisor_majorant(Q, A)


def test_energy_target_margin() -> None:
    powers = fold_height_energy_exponents()
    assert str(powers["sqrt_A_max"]) == "11/20"
    assert str(powers["target_nonzero_margin"]) == "121/80"
