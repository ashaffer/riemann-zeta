from itertools import product
from math import prod

from qp_three_by_three_grid import (
    determinant3,
    grid_determinant_certificate,
    qj_residual_determinant_bound,
    two_by_two_minors,
)


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    divisor = 2
    while divisor * divisor <= n:
        if n % divisor == 0:
            return False
        divisor += 1
    return True


def test_exact_diagonal_factorization() -> None:
    rows = (5, 7, 11)
    columns = (13, 17, 19)
    colors = ((23, 29, 31), (37, 41, 43), (47, 53, 59))
    products = [
        [8 * rows[i] * columns[j] * colors[i][j] for j in range(3)]
        for i in range(3)
    ]
    assert determinant3(products) == (
        8**3 * prod(rows) * prod(columns) * determinant3(colors)
    )


def test_qj_residual_bound_exhaustively_at_unit_height() -> None:
    Q = 7
    H = 1
    bound = qj_residual_determinant_bound(Q, H)
    for entries in product((-1, 0, 1), repeat=9):
        residual = [entries[0:3], entries[3:6], entries[6:9]]
        matrix = [[Q + residual[i][j] for j in range(3)] for i in range(3)]
        assert abs(determinant3(matrix)) <= bound


def test_zero_residual_completed_grid_is_certified_singular() -> None:
    rows = (10, 11, 12)
    columns = (13, 14, 15)
    common = prod(rows) * prod(columns)
    colors = [
        [common // (rows[i] * columns[j]) for j in range(3)]
        for i in range(3)
    ]
    certificate = grid_determinant_certificate(
        rows, columns, colors, Q=8 * common, H=0
    )
    assert certificate.hypotheses_force_singular
    assert certificate.color_determinant == 0
    assert certificate.conclusion_verified


def test_distinct_prime_rank_two_matrix_defeats_naive_classification() -> None:
    # C_ij=x_i+y_j, so rank(C)<=2.  These are nine distinct primes in a
    # 0.012-percent shell, and every 2-by-2 minor is nonzero and small.
    colors = (
        (844_427, 844_433, 844_439),
        (844_457, 844_463, 844_469),
        (844_511, 844_517, 844_523),
    )
    flat = tuple(value for row in colors for value in row)
    minors = two_by_two_minors(colors)
    q = 1_688_917
    assert is_prime(q)
    assert all(is_prime(value) for value in flat)
    assert len(set(flat)) == 9
    assert determinant3(colors) == 0
    assert all(value != 0 for value in minors)
    assert max(abs(value) for value in minors) == 1008
    assert 1008**33 < q**16  # 1008 < q^(16/33)
    assert max(flat) / min(flat) < 1.001
