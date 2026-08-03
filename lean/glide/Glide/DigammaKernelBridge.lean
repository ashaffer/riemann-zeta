/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Riemann-Zeta project contributors
-/
import Glide.DigammaKernel
import Glide.DigammaKernelQuarter
import Glide.DigammaP2Comparison

/-!
# Compatibility umbrella for the digamma kernel

New general-purpose clients should import `Glide.DigammaKernel`.  This module
also imports the project-specific p=2 comparison so existing callers retain
their API unchanged.
-/
