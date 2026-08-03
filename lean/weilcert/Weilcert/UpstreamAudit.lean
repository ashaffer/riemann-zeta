/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Riemann-Zeta project contributors
-/
import CertFramework
import FullInfTransfer
import LegendreIntervalL2
import LegendreScaledL2
import LegendrePlaneWaveL2

/-!
# Axiom audit for the reusable WeilCert layer
-/

#print axioms LegendreIntervalL2.normalizedLegendrePolynomial_pair
#print axioms LegendreIntervalL2.normalizedLegendreHilbertBasis
#print axioms LegendreIntervalL2.FourierLegendre.parseval
#print axioms LegendreIntervalL2.FourierLegendre.projection_error
#print axioms LegendrePlaneWaveL2.complexPlaneWave_projection_tail
#print axioms CertFramework.two_by_two_lower_bound_optimal
#print axioms CertFramework.twoBlockLowerEigenvalue_isGreatest
#print axioms CertFramework.twoBlockLowerEigenvalue_pos
#print axioms CertFramework.LDLPosCertificate.sound
#print axioms FullInfTransfer.bilinear_two_block_lower_bound_optimal
#print axioms FullInfTransfer.starProjection_lower_bound_optimal
