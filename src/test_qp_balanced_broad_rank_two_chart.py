from fractions import Fraction

from qp_balanced_broad_rank_two_chart import (
    balanced_broad_ledger,
    divided_second_difference,
    dot,
    four_point_plane_vectors,
    max_complementary_projection_index,
    minor_content,
    prime_lattice_pair_upper_bound,
)


def test_primitive_plane_and_projection_index() -> None:
    v1 = (1, 0, 2, 1)
    v2 = (0, 1, 1, 3)
    assert minor_content(v1, v2) == 1
    assert max_complementary_projection_index(v1, v2) == 5


def test_divided_second_difference_cancels_transverse_direction() -> None:
    v1 = (1, 0, 2, 1)
    v2 = (0, 1, 1, 3)
    v3 = (2, -1, 0, 1)
    base = (7, 11, 13, 17)

    def point(t: int, x: int, y: int) -> tuple[int, int, int, int]:
        return tuple(
            base[i] + t * v3[i] + x * v1[i] + y * v2[i]
            for i in range(4)
        )  # type: ignore[return-value]

    p0 = point(1, 0, 1)
    p1 = point(4, 2, -1)
    p2 = point(9, -3, 4)
    f = divided_second_difference(p0, p1, p2, 1, 4, 9)

    # A normal to span(v1,v2) annihilates the divided second difference.
    normal = (-3, -4, 1, 1)
    assert dot(normal, v1) == dot(normal, v2) == 0
    assert dot(normal, f) == 0


def test_balanced_endpoint_has_exact_one_eighth_gap() -> None:
    ledger = balanced_broad_ledger()
    assert ledger.plane_covolume == Fraction(22, 16)
    assert ledger.slice_cap == Fraction(5, 16)
    assert ledger.fixed_plane_colors == Fraction(41, 16)
    assert ledger.fixed_plane_mass == Fraction(-19, 16)
    assert ledger.total_colors == Fraction(73, 16)
    assert ledger.trivial_slice_incidence == Fraction(78, 16)
    assert ledger.target_slice_incidence == Fraction(76, 16)
    assert ledger.missing_power == Fraction(1, 8)
    assert ledger.saturated_plane_labels == Fraction(2, 1)
    assert ledger.required_plane_labels == Fraction(15, 8)


def test_four_points_recover_two_plane_vectors() -> None:
    v1 = (1, 0, 2, 1)
    v2 = (0, 1, 1, 3)
    v3 = (2, -1, 0, 1)
    base = (7, 11, 13, 17)

    def point(t: int, x: int, y: int) -> tuple[int, int, int, int]:
        return tuple(
            base[i] + t * v3[i] + x * v1[i] + y * v2[i]
            for i in range(4)
        )  # type: ignore[return-value]

    times = (0, 1, 3, 7)
    points = (
        point(times[0], 0, 0),
        point(times[1], 0, 0),
        point(times[2], 1, 0),
        point(times[3], 0, 1),
    )
    g2, g3 = four_point_plane_vectors(points, times)
    normal = (-3, -4, 1, 1)
    assert dot(normal, g2) == dot(normal, g3) == 0
    assert any(value != 0 for value in g2)
    assert any(value != 0 for value in g3)
    assert minor_content(g2, g3) != 0


def test_integer_prime_lattice_bound_rounding() -> None:
    assert prime_lattice_pair_upper_bound(100, 1_000, 64) == 1_600
