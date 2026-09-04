import numpy as np

from semilocal_relative_ward_probe import relative_old_collar_coordinates


def test_relative_coordinates_are_moment_null_and_g_orthonormal() -> None:
    rng = np.random.default_rng(20260901)
    total = 11
    old_degree = 7
    seed = rng.normal(size=(total, total))
    gram = seed.T @ seed + np.eye(total)
    moments = rng.normal(size=(2, total))

    coordinates, split, diagnostics = relative_old_collar_coordinates(
        gram, moments, old_degree
    )

    assert coordinates.shape == (total, total - 2)
    assert split == old_degree - 2
    assert np.linalg.norm(moments @ coordinates, ord=2) < 1.0e-12
    assert np.linalg.norm(
        coordinates.T @ gram @ coordinates - np.eye(total - 2), ord=2
    ) < 1.0e-12
    assert np.linalg.norm(coordinates[old_degree:, :split], ord=2) < 1.0e-14
    assert diagnostics["g_orthogonality_error"] < 1.0e-12


def test_relative_coordinates_annihilate_the_rank_two_pole_form() -> None:
    rng = np.random.default_rng(20260902)
    total = 9
    old_degree = 5
    seed = rng.normal(size=(total, total))
    gram = seed.T @ seed + 2 * np.eye(total)
    plus = rng.normal(size=total)
    minus = rng.normal(size=total)
    moments = np.vstack([plus, minus])
    pole = np.outer(plus, minus) + np.outer(minus, plus)

    coordinates, _, _ = relative_old_collar_coordinates(
        gram, moments, old_degree
    )

    compressed = coordinates.T @ pole @ coordinates
    assert np.linalg.norm(compressed, ord=2) < 1.0e-14
