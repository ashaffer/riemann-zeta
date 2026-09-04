import mpmath as mp

from harmonic_schur_collar_probe import mixed_extension_forms
from ward_source_extremizer_probe import (
    analyze_source_resolved_ward,
    generalized_max_vector,
    literal_collar_geometry,
    residual_source_matrices,
)


def test_generalized_max_vector_normalization():
    with mp.workdps(40):
        numerator = mp.matrix([[2, 0], [0, 9]])
        denominator = mp.matrix([[1, 0], [0, 3]])
        value, vector, second = generalized_max_vector(numerator, denominator)
        assert abs(value - 3) < mp.mpf("1e-30")
        assert abs(second - 2) < mp.mpf("1e-30")
        assert abs((vector.T * denominator * vector)[0] - 1) < mp.mpf("1e-30")


def test_residual_source_matrices_reconstruct_actual_residual():
    with mp.workdps(38):
        old_degree, collar_degree = 5, 1
        delta = mp.mpf("0.12")
        q, g, h, _, lnew = mixed_extension_forms(
            old_degree, collar_degree, delta, 5, 32
        )
        centers, widths, _, geometry_lnew = literal_collar_geometry(
            old_degree, collar_degree, delta, 5
        )
        sources, _ = residual_source_matrices(q, h, centers, widths, lnew)
        reconstructed = mp.matrix(q.rows)
        for source in sources.values():
            reconstructed += source
        assert abs(geometry_lnew - lnew) < mp.mpf("1e-35")
        assert max(
            abs(reconstructed[i, j] - (q[i, j] - h[i, j]))
            for i in range(q.rows)
            for j in range(q.cols)
        ) < mp.mpf("1e-30")
        assert set(sources) == {
            "archimedean_residual",
            "pole",
            "prime_power_2",
            "prime_power_3",
            "prime_power_4",
            "prime_power_5",
        }


def test_source_resolved_ward_extremizer_identities_and_symmetry():
    row = analyze_source_resolved_ward(
        7, 1, "0.12", dps=30, low_mode_count=5, smear_nodes=3
    )
    assert row["status"] == "FINITE_DIAGNOSTIC_ONLY"
    assert row["parity"]["dominant_sector"] in {"even", "odd"}
    for name, value in row["checks"].items():
        assert abs(mp.mpf(value)) < mp.mpf("1e-25"), (name, value)

    assert abs(
        mp.mpf(row["extremizer"]["HRW_prime_ratio"])
        - mp.mpf(row["ward_ratio"])
    ) < mp.mpf("1e-25")
    p5 = next(
        source
        for source in row["source_attribution"]["sources"]
        if source["name"] == "prime_power_5"
    )
    assert abs(mp.mpf(p5["old_old_block_max_abs"])) < mp.mpf("1e-28")
    assert row["all_source_sign_patterns_fixed_old_metric"]["pattern_count"] == 32
    assert len(row["low_old_modes_at_extremizer"]) == 5
