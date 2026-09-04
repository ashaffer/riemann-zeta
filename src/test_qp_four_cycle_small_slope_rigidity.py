from math import gcd

from qp_four_cycle_small_slope_rigidity import (
    primitive_slope_rigidity_ledger,
)


def test_weighted_additive_example_gives_a_determinant_divisor() -> None:
    ledger = primitive_slope_rigidity_ledger(
        (2100, 1497, 1393, 993),
        (2, 3),
        (5, 7),
    )
    assert ledger.color_determinant == -21
    assert ledger.determinant_divisor == 7
    assert ledger.divisor_remainder == 0
    assert ledger.direction_bound == 7
    assert ledger.rank_one_lattice_certificate


def test_small_box_contains_divisor_many_primitive_directions() -> None:
    colors = (100_000, 99_993, 99_989, 99_982)
    bound = 5
    matrices: set[tuple[int, int, int, int]] = set()
    for r1 in range(-bound, bound + 1):
        for r2 in range(-bound, bound + 1):
            if gcd(abs(r1), abs(r2)) != 1:
                continue
            for s1 in range(-bound, bound + 1):
                for s2 in range(-bound, bound + 1):
                    if gcd(abs(s1), abs(s2)) != 1:
                        continue
                    defect = (
                        colors[0] * r1 * s1
                        - colors[1] * r1 * s2
                        - colors[2] * r2 * s1
                        + colors[3] * r2 * s2
                    )
                    if defect == 0:
                        matrix = (r1 * s1, r1 * s2, r2 * s1, r2 * s2)
                        if next((x for x in matrix if x), 1) < 0:
                            matrix = tuple(-x for x in matrix)
                        matrices.add(matrix)
                        ledger = primitive_slope_rigidity_ledger(
                            colors, (r1, r2), (s1, s2)
                        )
                        assert ledger.rank_one_lattice_certificate
    # det(C)=-77, so the theorem's safe bound is 4*tau(77)=16.
    assert 0 < len(matrices) <= 16
