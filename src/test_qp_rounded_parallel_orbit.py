from fractions import Fraction
from itertools import permutations

from qp_actual_prime_nds import actual_prime_residual_double_star, four_completion_chains
from qp_affine_four_completion_hessian import StationaryAffineProduct
from qp_four_completion_bezout_token import BezoutTokenChart
from qp_rounded_parallel_orbit import (
    nonreturn_two_inverse_ledger,
    orbit_reflection_ledger,
    parallel_orbit_direction_ledger,
    return_bilinear_transfer_ledger,
    rounded_rectangle_ledger,
    virtual_endpoint_bilinear_ledger,
    virtual_bilinear_cycle_ledger,
)
from qp_scattered_token_search import (
    RootedTokenScanner,
    exact_balanced_degree,
    full_integer_shell,
)


def test_endpoint_population_is_the_reflected_single_orbit() -> None:
    chart = BezoutTokenChart.canonical(11, 13)
    for center in ((17, 19), (23, 29), (31, 37)):
        ledger = orbit_reflection_ledger(chart, center)
        assert ledger.endpoint_token == tuple(-value for value in ledger.center_token)
        assert ledger.reflected_endpoint == center[::-1]
        assert ledger.center_transverse_numerator == -center[0]
        assert ledger.endpoint_transverse_numerator == center[0]


def test_parallel_orbit_determinant_has_only_affine_terms() -> None:
    chart = BezoutTokenChart.canonical(11, 13)
    ledger = parallel_orbit_direction_ledger(
        chart, (-2, -1), (101, 103), (107, 109)
    )
    assert ledger.physical_direction == (1, 1)
    assert ledger.token_label_step == -2
    assert ledger.nonnull
    assert ledger.middle_determinant_r_step == 2
    assert ledger.middle_determinant_s_step == -2


def test_literal_prime_fixture_is_one_parallel_nonnull_rounded_chart() -> None:
    fixture = actual_prime_residual_double_star()
    middle = fixture.q // 2
    chart = BezoutTokenChart.canonical(*fixture.central.colors)
    chains = four_completion_chains(
        fixture.q,
        fixture.D,
        fixture.primes,
        fixture.central.colors,
        residual_only=False,
    )
    assert len(chains) == 15
    for chain in chains:
        P = chart.center_to_token(chain.centers)
        R = chart.endpoint_to_token(chain.next_colors)
        # Two distinct parallel digital lines of primitive direction (6,5).
        assert 5 * P[0] - 6 * P[1] == 6
        assert 5 * R[0] - 6 * R[1] == -6
        # The unique actual-prime completion rows obey a rounded affine law.
        assert chain.next_row == 3 * middle - chain.centers[0] - chain.next_colors[0]

    # That integral law is not the formal stationary affine law at a base
    # cell: both rational slopes have nontrivial denominators.
    base = chains[0]
    stationary = StationaryAffineProduct(
        base.next_row,
        base.centers[0],
        base.next_colors[0],
        -6,
        -6,
    )
    assert not stationary.integral_row_law


def test_four_corner_identity_for_an_exact_product_rectangle() -> None:
    # q=2M and the four products are deliberately not all exact; D is chosen
    # from their literal maximum residual.
    q = 2000
    left = (997, 1003)
    right = (991, 1009)
    rows = tuple(
        round(q**3 / (8 * b * d))
        for b in left
        for d in right
    )
    residual = max(
        abs(8 * rows[2 * i + j] * left[i] * right[j] - q**3)
        for i in range(2)
        for j in range(2)
    )
    D = (residual + q - 1) // q
    ledger = rounded_rectangle_ledger(q, D, rows, left, right)
    assert ledger.integer_mixed_difference == (
        rows[0] - rows[1] - rows[2] + rows[3]
    )
    assert ledger.forced_additivity
    assert ledger.integer_mixed_difference == 0


def test_return_transfer_and_nonreturn_error_pair_on_literal_prime_chains() -> None:
    fixture = actual_prime_residual_double_star()
    chains = four_completion_chains(
        fixture.q,
        fixture.D,
        fixture.primes,
        fixture.central.colors,
        residual_only=False,
    )
    row_by_center = {chain.centers: chain.base_row for chain in chains}
    saw_return = False
    saw_nonreturn = False
    for chain in chains:
        general = nonreturn_two_inverse_ledger(
            fixture.q,
            fixture.D,
            fixture.central.colors,
            chain.base_row,
            chain.centers,
            chain.next_row,
            chain.next_colors,
        )
        assert general.determinant_identity == (
            chain.next_row * general.endpoint_determinant
        )
        virtual = virtual_endpoint_bilinear_ledger(
            fixture.q,
            fixture.D,
            fixture.central.colors,
            chain.base_row,
            chain.centers,
            chain.next_row,
            chain.next_colors,
        )
        assert virtual.first_row_error.denominator > 0
        assert virtual.second_row_error.denominator > 0
        reflected = chain.next_colors[::-1]
        if reflected in row_by_center:
            saw_return = True
            transfer = return_bilinear_transfer_ledger(
                fixture.q,
                fixture.D,
                fixture.central.colors,
                chain.base_row,
                chain.centers,
                row_by_center[reflected],
                reflected,
                chain.next_row,
            )
            assert abs(transfer.transfer_residual) <= min(
                transfer.first_absolute_ceiling,
                transfer.second_absolute_ceiling,
            )
        else:
            saw_nonreturn = True
    assert saw_return
    assert saw_nonreturn


def test_literal_prime_six_cycle_has_subunit_virtual_area_and_is_additive() -> None:
    fixture = actual_prime_residual_double_star()
    chains = four_completion_chains(
        fixture.q,
        fixture.D,
        fixture.primes,
        fixture.central.colors,
        residual_only=False,
    )
    edges = {
        (chain.base_row, chain.next_colors): chain.next_row for chain in chains
    }
    left = (2_934_067, 2_934_073, 2_934_091)
    right = (
        (2_934_079, 2_934_073),
        (2_934_103, 2_934_097),
        (2_934_097, 2_934_091),
    )
    diagonal = tuple(edges[left[index], right[index]] for index in range(3))
    shifted = tuple(edges[left[(index + 1) % 3], right[index]] for index in range(3))
    c, C = fixture.central.colors
    Q = Fraction(fixture.q**3, 8)
    scale = Fraction(c * C, 1) / Q
    heights = tuple(Q / (c * endpoint[1]) for endpoint in right)
    ledger = virtual_bilinear_cycle_ledger(
        scale, left, heights, diagonal, shifted
    )
    assert ledger.forced_additivity
    assert ledger.integer_alternating_sum == 0


def _determinant_4_by_4(rows: tuple[tuple[int, int, int, int], ...]) -> int:
    """Tiny exact determinant helper for the hostile six-cycle fixture."""

    total = 0
    for permutation in permutations(range(4)):
        inversions = sum(
            permutation[i] > permutation[j]
            for i in range(4)
            for j in range(i + 1, 4)
        )
        product = 1
        for row, column in enumerate(permutation):
            product *= rows[row][column]
        total += (-1 if inversions % 2 else 1) * product
    return total


def test_full_integer_nonreturn_bridge_has_induced_noncoherent_six_cycle() -> None:
    """Exact obstruction to a mask-free ``all short cycles are planes`` claim.

    This is deliberately a full-integer fixture, not an actual-prime one.
    Four edges return to the rooted neighbourhood and the two edges through
    the final endpoint do not.  The latter bridge makes the induced cycle
    nonadditive and noncoplanar.
    """

    q = 100_000
    D = exact_balanced_degree(q)
    anchor = (50_000, 50_007)
    scanner = RootedTokenScanner(q, D, full_integer_shell(q))
    audit = scanner.root_audit(anchor)
    assert D == 265
    assert audit.neighbourhood_degree_sum == 98

    left_tokens = ((-7, -7), (7, 5), (35, 29))
    right_tokens = ((-35, -29), (7, 7), (-36, -30))
    cycle_keys = (
        (left_tokens[0], right_tokens[0]),
        (left_tokens[1], right_tokens[0]),
        (left_tokens[1], right_tokens[1]),
        (left_tokens[2], right_tokens[1]),
        (left_tokens[2], right_tokens[2]),
        (left_tokens[0], right_tokens[2]),
    )
    lookup = {
        (path.center_token, path.endpoint_token): path for path in audit.paths
    }
    paths = tuple(lookup[key] for key in cycle_keys)

    # These are exactly the three possible chords of this six-cycle.
    missing_chords = (
        (left_tokens[0], right_tokens[1]),
        (left_tokens[1], right_tokens[2]),
        (left_tokens[2], right_tokens[0]),
    )
    assert all(key not in lookup for key in missing_chords)

    for path in paths:
        nonreturn_two_inverse_ledger(
            q,
            D,
            anchor,
            path.base_row,
            path.center,
            path.next_row,
            path.endpoint,
        )

    assert tuple(path.next_row for path in paths) == (
        49_997,
        49_999,
        49_993,
        49_997,
        58_338,
        58_331,
    )
    alternating_holonomy = sum(path.next_row for path in paths[::2]) - sum(
        path.next_row for path in paths[1::2]
    )
    assert alternating_holonomy == 1

    # A nonzero augmented 4-by-4 minor certifies that the six physical
    # points (b,d,x) do not lie in one affine plane.
    physical_points = tuple(
        (path.center[0], path.endpoint[0], path.next_row) for path in paths
    )
    witness_rows = tuple(
        (*physical_points[index], 1) for index in (0, 1, 2, 4)
    )
    assert _determinant_4_by_4(witness_rows) == 14_304

    # The common last right vertex is genuinely nonreturn.  The other two
    # right vertices are reflections of actual root neighbours.
    c, C = anchor
    first = scanner.completion_map(c)
    second = scanner.completion_map(C)
    root_centers = {
        (first[row], second[row])
        for row in first.keys() & second.keys()
        if first[row] * c != second[row] * C
    }
    assert tuple(path.endpoint[::-1] in root_centers for path in paths) == (
        True,
        True,
        True,
        True,
        False,
        False,
    )

    # Constants matter: D^2<q does not make this three-step cycle subunit.
    # Its ideal virtual area is already just above one, so the exact local
    # forcing lemma correctly makes no additivity claim.
    Q = Fraction(q**3, 8)
    scale = Fraction(c * C, 1) / Q
    diagonal = (paths[0].next_row, paths[2].next_row, paths[4].next_row)
    shifted = (paths[1].next_row, paths[3].next_row, paths[5].next_row)
    left_rows = (paths[0].base_row, paths[2].base_row, paths[4].base_row)
    right_heights = tuple(
        Q / (c * path.endpoint[1]) for path in (paths[0], paths[2], paths[4])
    )
    cycle = virtual_bilinear_cycle_ledger(
        scale, left_rows, right_heights, diagonal, shifted
    )
    assert cycle.integer_alternating_sum == 1
    assert cycle.ideal_alternating_sum > 1
    assert not cycle.forced_additivity
