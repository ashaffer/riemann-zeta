#!/usr/bin/env python3
"""Independent finite replay of the projected-Gram cluster/source gate."""

from __future__ import annotations

import math

import numpy as np

from qp_projected_gram_cluster_gate import (
    alternating_binomial,
    asymptotic_cluster_rate,
    carrier_residual_dual,
    cluster_rayleigh_upper_bound,
    cosine_atoms,
    critical_packet_slice,
    critical_regular_hadamard,
    guth_maynard_count_exponents,
    projected_dictionary,
    zero_center_source_condition,
)


nodes = np.asarray([0.011, 0.029, 0.053, 0.089, 0.127, 0.163, 0.191])
order = 6
times = 101.0 + np.arange(order + 1)
_, projected = projected_dictionary(nodes, times)
coefficients = alternating_binomial(order)
gram = projected.T @ projected
rayleigh = float(coefficients @ gram @ coefficients / (coefficients @ coefficients))
bound = cluster_rayleigh_upper_bound(len(nodes), order)
assert rayleigh <= bound * (1.0 + 1e-9)
assert float(np.linalg.eigvalsh(gram)[0]) <= rayleigh + 1e-12

source_matrix = cosine_atoms(nodes, [37.0, 61.0, 97.0])
source = zero_center_source_condition(source_matrix)
residual = carrier_residual_dual(source_matrix)
assert source.maximum_center_residual < 2e-12
assert source.carrier_normalization_residual < 2e-12
assert math.isclose(source.source_energy, source.source_from_leverage, rel_tol=2e-11)
assert math.isclose(source.source_energy, source.variational_probe, rel_tol=2e-11)
assert math.isclose(source.carrier_leverage, residual.carrier_leverage, rel_tol=2e-11)
assert math.isclose(source.zeroing_norm_square, residual.dual_norm_square, rel_tol=2e-11)
assert math.isclose(asymptotic_cluster_rate(), 4.608504631138533, rel_tol=1e-14)
gm_exponents = guth_maynard_count_exponents()
assert math.isclose(gm_exponents[0], 0.038, rel_tol=1e-14)
assert gm_exponents[1] < 0.0 and gm_exponents[2] < 0.0
critical = critical_packet_slice(2)
critical_dimension, critical_count = critical.shape
assert np.array_equal(critical.T @ critical, critical_dimension * np.eye(critical_count))
assert np.array_equal(critical @ (-np.ones(critical_count) / math.sqrt(critical_count)), np.ones(critical_dimension))
assert np.array_equal(
    critical @ (np.ones(critical_count) / critical_count),
    -np.ones(critical_dimension) / math.sqrt(critical_count),
)
regular = critical_regular_hadamard(power=2, repeats=2)
regular_dimension, regular_count = regular.shape
assert np.array_equal(regular.T @ regular, regular_dimension * np.eye(regular_count))
assert np.allclose(
    regular @ (np.ones(regular_count) / regular_count),
    -np.ones(regular_dimension) / math.sqrt(regular_count),
)

print(
    {
        "status": "PASS",
        "finite_rayleigh": rayleigh,
        "universal_upper_bound": bound,
        "cluster_rate": asymptotic_cluster_rate(),
        "source_energy": source.source_energy,
        "carrier_leverage": source.carrier_leverage,
        "guth_maynard_term_exponents": gm_exponents,
        "critical_orthogonal_packet_count": critical_count,
        "scope": "uniform arbitrary-set Gram lower bound is refuted; actual-prime source bound remains open",
    }
)
