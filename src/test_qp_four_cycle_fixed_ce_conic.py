from qp_four_cycle_fixed_ce_conic import (
    beta_norm_identity,
    fixed_ce_conic_invariants,
)


def test_fixed_ce_canonical_identities() -> None:
    # M=(2,3)^T(5,7), M'=(11,13)^T(17,19).
    product = (10, 14, 15, 21)
    other = (187, 209, 221, 247)
    energy = tuple(a - b for a, b in zip(product, other))
    # K=(1,-5;-6,9) is exactly orthogonal to E and is nonsingular.
    colors = (1, 5, 6, 9)

    data = fixed_ce_conic_invariants(colors, energy, product)
    assert data.color_determinant == -21
    assert data.energy_determinant == -168
    assert data.color_energy_pairing == 0
    assert data.a_trace == 0
    assert data.a_determinant == (
        data.color_determinant * data.energy_determinant
    )
    assert data.idempotent_quadric_left == data.idempotent_quadric_right
    assert data.level_plane_left == data.level_plane_right
    assert data.infinity_discriminant == (
        -16 * data.color_determinant * data.energy_determinant
    )
    assert data.full_degeneracy_parameter != 0
    assert beta_norm_identity(data)[0] == beta_norm_identity(data)[1]


def test_reported_full_integer_collision_has_same_invariants() -> None:
    colors = (718, 714, 714, 710)
    first = (531, 534, 712, 716)
    second = (534, 537, 708, 712)
    product = (
        first[0] * first[2],
        first[0] * first[3],
        first[1] * first[2],
        first[1] * first[3],
    )
    other = (
        second[0] * second[2],
        second[0] * second[3],
        second[1] * second[2],
        second[1] * second[3],
    )
    energy = tuple(a - b for a, b in zip(product, other))
    assert energy == (0, -12, 12, 0)

    data = fixed_ce_conic_invariants(colors, energy, product)
    assert data.color_determinant == -16
    assert data.energy_determinant == 144
    assert data.color_energy_pairing == 0
    assert data.a_trace == 0
    assert data.a_determinant == -16 * 144
    assert data.idempotent_quadric_left == data.idempotent_quadric_right
    assert data.level_plane_left == data.level_plane_right
    assert data.full_degeneracy_parameter != 0
    if data.beta:
        assert beta_norm_identity(data)[0] == beta_norm_identity(data)[1]
