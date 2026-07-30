/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Authors: Riemann-Zeta project contributors
-/
import RHBridge.P2Containment
import RHBridge.P2EntryCertificate
import RHBridge.P2EntryTable
import RHBridge.P2EntryError
import RHBridge.P2PoleApprox
import RHBridge.PolyEnclosure
import RHBridge.P2RationalPolynomial
import RHBridge.P2DigammaTail
import RHBridge.P2DigammaPrefix
import RHBridge.P2TailTelescopers
import RHBridge.P2ElementaryConstants
import RHBridge.P2AlphaEnclosure
import RHBridge.P2SphericalApprox
import RHBridge.P2CosApprox
import RHBridge.P2DefectApprox
import RHBridge.P2SphericalReal
import RHBridge.P2ComponentBounds
import RHBridge.P2ScaleCenters
import RHBridge.P2PanelComposition
import RHBridge.P2CanonicalRational
import RHBridge.P2PoleScaleCenters
import RHBridge.P2PoleRationalCenter
import RHBridge.P2RoundedBoundedCertificateCheck
import RHBridge.UniformSupportTransfer

/-!
# Composed RH proof bridges

This package imports the independent `glide` and `weilcert` developments so
their kernel-checked theorems can be composed without duplicating either
development.  The current focus is the unrestricted `p = 2` endpoint.
-/
