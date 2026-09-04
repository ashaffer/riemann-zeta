"""Regression tests for the QP/Turan source-fiber bifurcation algebra."""

from __future__ import annotations

from fractions import Fraction
import math

import numpy as np

from qp_source_fiber_bifurcation import (
    DIFFUSE_ANTENNA_ERROR_EXPONENT,
    DIFFUSE_SOURCE_FIBER_EXPONENT,
    DPA_TARGET_EXPONENT,
    RADIAL_TARGET_EXPONENT,
    SOURCE_DEPTH_EXPONENT,
    TRANSVERSE_TARGET_EXPONENT,
    certify_source_fiber,
    exponent_ledger,
    fejer_closed_form,
    fejer_probability_transform,
    fejer_probability_weights,
    fejer_source_fiber_replay,
    normalized_separator,
    radial_dual,
    source_direction,
)


def test_legal_source_is_null_on_its_source_direction() -> None:
    depth = 0.17
    source_atom = np.array([-0.4, -0.2, 0.6, 0.9])
    source = np.array([0.5, 0.5, 0.0, 0.0])
    assert abs(float(source @ source_atom) + depth + 0.13) < 1e-14
    # Adjust the second source atom so the probability response is exactly -D.
    source_atom[1] = -2 * depth - source_atom[0]
    assert abs(float(source @ source_direction(source_atom, depth))) < 1e-14


def test_normalized_antenna_is_an_exact_bad_fiber_separator() -> None:
    depth = 0.2
    atom0 = np.array([0.3, -0.4, 0.7])
    alpha = np.array([0.2, 0.3, 0.5])
    separator, denominator = normalized_separator(alpha, atom0, depth)
    direction = source_direction(atom0, depth)
    assert denominator > 0.0
    assert abs(float(separator @ direction) + 1.0) < 1e-14


def test_probability_antenna_gives_the_direct_radial_dual() -> None:
    alpha = np.array([0.2, 0.3, 0.5])
    atom = np.array([0.7, -0.4, 0.1])
    dual = radial_dual(alpha)
    assert abs(float(np.sum(dual)) + 1.0) < 1e-14
    assert abs(float(dual @ atom) + float(alpha @ atom)) < 1e-14


def test_projective_floor_identity_on_a_finite_time_pool() -> None:
    depth = 0.24
    atom0 = np.array([0.8, -0.1, 0.4, -0.2])
    source = np.array([0.0, 0.0, 0.0, 1.0])
    # Make the disjoint source coordinate exactly legal.
    atom0[-1] = -depth
    alpha = np.array([0.2, 0.3, 0.5, 0.0])
    atoms = np.array(
        [
            [0.2, -0.3, 0.1, 0.9],
            [-0.5, 0.1, 0.4, -0.7],
            [0.7, 0.8, -0.6, 0.2],
        ]
    )
    certificate = certify_source_fiber(
        source_probability=source,
        antenna_probability=alpha,
        source_atom=atom0,
        high_band_atoms=atoms,
        depth=depth,
    )
    assert certificate.source_null_residual < 1e-14
    assert certificate.separator_pairing_residual < 1e-14
    assert certificate.projective_identity_residual < 1e-14
    assert abs(
        certificate.v_dual_level
        - certificate.q_dual_level / certificate.denominator
    ) < 1e-14


def test_fejer_triangular_weights_are_a_probability() -> None:
    for order in (2, 3, 17, 101):
        weights = fejer_probability_weights(order)
        assert np.all(weights > 0.0)
        assert abs(float(np.sum(weights)) - 1.0) < 1e-14


def test_fejer_transform_matches_square_closed_form() -> None:
    for order in (7, 31, 101):
        for theta in (0.0, 0.13, 2.0 * math.pi / order, 1.7):
            assert abs(
                fejer_probability_transform(order, theta)
                - fejer_closed_form(order, theta)
            ) < 3e-13


def test_fejer_source_fiber_has_exact_projective_floor() -> None:
    for order, depth in ((11, 0.1), (101, 0.2), (257, 0.03)):
        replay = fejer_source_fiber_replay(order, depth)
        assert replay.source_null_residual < 1e-14
        assert replay.separator_pairing_residual < 1e-14
        assert replay.fiber_level_residual < 3e-14


def test_diffuse_pseudonode_exponents_defeat_both_soft_targets() -> None:
    assert SOURCE_DEPTH_EXPONENT == Fraction(1, 1000)
    assert TRANSVERSE_TARGET_EXPONENT == Fraction(179, 10_000)
    assert SOURCE_DEPTH_EXPONENT + TRANSVERSE_TARGET_EXPONENT == RADIAL_TARGET_EXPONENT
    assert DIFFUSE_ANTENNA_ERROR_EXPONENT > DPA_TARGET_EXPONENT
    assert DIFFUSE_SOURCE_FIBER_EXPONENT == Fraction(499, 1000)
    assert DIFFUSE_SOURCE_FIBER_EXPONENT > TRANSVERSE_TARGET_EXPONENT
    ledger = exponent_ledger()
    assert ledger["mixing_identity"] is True
    assert ledger["pseudo_q_radius_below_dpa_upper_scale"] is True
    assert ledger["pseudo_q_radius_violates_direct_ltrad_scale"] is True
    assert ledger["pseudo_v_radius_violates_transverse_scale"] is True
