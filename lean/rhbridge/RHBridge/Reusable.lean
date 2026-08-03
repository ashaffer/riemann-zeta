/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Riemann-Zeta project contributors
-/
import RHBridge.SimplePole
import RHBridge.AutocorrelationPlancherelCore
import RHBridge.SmoothCutoff

/-!
# Reusable RHBridge infrastructure

This small umbrella contains only the compact, application-independent modules
prepared for possible upstream extraction.  In particular, its residue import
is the standalone principal-part/circle layer rather than the much larger
rectangle implementation.  It imports no RH literature assumptions and no
generated numerical certificate instances.
-/
