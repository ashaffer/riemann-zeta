from qp_broad_rectangle_label_fixture import (
    completion_a_product,
    completion_a_product_formula,
    defect_identity,
    interval_additive_energy,
    positive_broad_rectangle_count,
    rectangle_labels,
    replay,
)


def test_defect_and_product_identities() -> None:
    for n in range(15):
        assert defect_identity(101, n) == n
        assert completion_a_product(101, n) == completion_a_product_formula(101, n)


def test_rectangle_labels() -> None:
    labels = rectangle_labels(101, 2, 3, 5)
    assert labels.step_a_1 == 303
    assert labels.step_a_2 == 505
    assert labels.step_b_1 == 300
    assert labels.step_b_2 == 500
    assert labels.mixed_carrier == 30
    assert labels.completion_determinant == 0
    assert labels.mixed_carrier * 101**2 == 2 * labels.step_a_1 * labels.step_a_2


def test_counts_and_replay() -> None:
    assert interval_additive_energy(4) == 44
    assert positive_broad_rectangle_count(4) == 4
    assert replay(101, 20)["fixture_energy"] == 3.0
