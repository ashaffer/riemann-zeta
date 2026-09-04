from qp_product_error_cube_algebra import (
    ap_third_identity,
    cube_algebra,
    cube_determinant_algebra,
    determinant_algebra,
    rectangle_algebra,
)


def test_rectangle_product_leibniz() -> None:
    carriers = {(0, 0): 31, (1, 0): 27, (0, 1): 24, (1, 1): 23}
    result = rectangle_algebra(101, 7, 11, carriers, 3000)
    assert result.mixed_product_error == result.leibniz_rhs


def test_cube_product_leibniz() -> None:
    carriers = {
        (i, j, k): 80 - 3 * i - 5 * j - 7 * k + 2 * i * j - i * k + 3 * j * k
        for i in (0, 1)
        for j in (0, 1)
        for k in (0, 1)
    }
    result = cube_algebra(211, 13, 17, 19, carriers, 15000)
    assert result.third_product_error == result.leibniz_rhs


def test_ap_third_product_leibniz() -> None:
    lhs, _, rhs = ap_third_identity(101, 9, (40, 35, 33, 34), 4000)
    assert lhs == rhs


def test_determinant_elimination() -> None:
    carriers = {(0, 0): 31, (1, 0): 27, (0, 1): 24, (1, 1): 23}
    result = determinant_algebra(101, 97, 7, 6, 11, 10, carriers, 3000, 2900)
    assert result.first_elimination_lhs == result.first_elimination_rhs
    assert result.second_elimination_lhs == result.second_elimination_rhs


def test_cube_determinant_eliminations() -> None:
    carriers = {
        (i, j, k): 80
        - 3 * i
        - 5 * j
        - 7 * k
        + 2 * i * j
        - i * k
        + 3 * j * k
        + 4 * i * j * k
        for i in (0, 1)
        for j in (0, 1)
        for k in (0, 1)
    }
    result = cube_determinant_algebra(
        211,
        197,
        13,
        12,
        17,
        16,
        19,
        17,
        carriers,
        15000,
        14000,
    )
    assert result.elimination_lhs == result.elimination_rhs
