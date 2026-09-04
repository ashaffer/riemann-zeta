from flint import ctx

import chuk_l08_arb_certificate as base
import chuk_p5_threshold_arb_certificate as cert


def _save_configuration():
    return base.CUTOFF, base.ALPHA, base.A_HALF_WIDTH, ctx.prec, ctx.threads


def _restore_configuration(saved):
    base.CUTOFF, base.ALPHA, base.A_HALF_WIDTH, ctx.prec, ctx.threads = saved


def test_exact_endpoint_mask_and_exterior_floor():
    saved = _save_configuration()
    try:
        ctx.prec = cert.DEFAULT_PRECISION
        log5 = cert.configure_base()
        checks = cert.endpoint_and_envelope_checks(log5)
        assert (checks["support_diameter"] - log5).contains(0)
        assert checks["beta_star"] > cert.A(cert.ALPHA)
        assert checks["real_multiplier_bound"] < cert.A(16)
        assert checks["ellipse_multiplier_bound"] < cert.A(21)
    finally:
        _restore_configuration(saved)


def test_quadrature_and_full_tail_ledger():
    saved = _save_configuration()
    try:
        ctx.prec = cert.DEFAULT_PRECISION
        cert.configure_base()
        assert base.quadrature_entry_error(80) < cert.A(cert.Q(16, 10**30))
        transfer = base.full_space_transfer(
            cert.DEFAULT_DEGREE,
            cert.HEAD_SHIFT,
            cert.FULL_SHIFT,
        )
        assert transfer["rho_tail"] < cert.A(cert.Q(9, 10**26))
        assert transfer["coupling"] < cert.A(cert.Q(5, 10**12))
        assert transfer["determinant"] > cert.A(cert.Q(7, 10**19))
    finally:
        _restore_configuration(saved)


def test_endpoint_bessel_recurrence_overlaps_direct_values():
    saved = _save_configuration()
    try:
        ctx.prec = cert.DEFAULT_PRECISION
        cert.configure_base()
        z = cert.A(base.A_HALF_WIDTH) * 249
        values = base.spherical_j_vector(z, cert.DEFAULT_DEGREE)
        for degree in (0, 100, 200, 299):
            assert values[degree].overlaps(base.spherical_j_direct(degree, z))
    finally:
        _restore_configuration(saved)


def test_effective_glide_crosses_the_p5_event():
    saved = _save_configuration()
    try:
        ctx.prec = cert.DEFAULT_PRECISION
        log5 = cert.configure_base()
        glide = cert.explicit_glide_instantiation(log5)
        assert glide["c_glide"] < cert.A(12662)
        assert glide["post_event_floor"] > cert.A(cert.Q(3733, 10**21))
    finally:
        _restore_configuration(saved)
