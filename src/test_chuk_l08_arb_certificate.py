from flint import ctx

import chuk_l08_arb_certificate as cert


def test_constants_are_not_frozen_at_default_precision():
    assert cert.PI.rel_accuracy_bits() >= 500
    assert cert.PRIME_MASS.rel_accuracy_bits() >= 500


def test_scalar_and_full_tail_ledger():
    old_precision = ctx.prec
    try:
        ctx.prec = 384
        cert.support_and_envelope_checks()
        assert cert.quadrature_entry_error(80) < cert.A(cert.Q(13, 10**30))
        transfer = cert.full_space_transfer(
            250,
            cert.Q(9, 10**18),
            cert.Q(89, 10**19),
        )
        assert transfer["rho_tail"] < cert.A(cert.Q(6, 10**32))
        assert transfer["coupling"] < cert.A(cert.Q(4, 10**15))
        assert transfer["determinant"] > cert.A(cert.Q(4, 10**20))
    finally:
        ctx.prec = old_precision


def test_downward_bessel_vector_overlaps_direct_values():
    old_precision = ctx.prec
    try:
        ctx.prec = 384
        z = cert.A(123)
        values = cert.spherical_j_vector(z, 250)
        for degree in (0, 50, 123, 249):
            assert values[degree].overlaps(cert.spherical_j_direct(degree, z))
    finally:
        ctx.prec = old_precision
