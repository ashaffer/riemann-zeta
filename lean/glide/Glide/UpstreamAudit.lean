/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Riemann-Zeta project contributors
-/
import Glide.CompactSupportFourierLaplace
import Glide.BasicCore
import Glide.DigammaKernel
import Glide.GammaUniform

/-!
# Axiom audit for the reusable Glide layer
-/

#print axioms CompactSupportFourierLaplace.differentiable_transform
#print axioms CompactSupportFourierLaplace.integrableOn_of_integrableOn_norm_sq
#print axioms
  CompactSupportFourierLaplace.differentiable_transform_of_integrableOn_norm_sq
#print axioms
  CompactSupportFourierLaplace.norm_transform_le_sqrt_integral_sq_mul_exp
#print axioms CompactSupportFourierLaplace.analyticOrderAt_translate
#print axioms GlideKernel.frullani_cos
#print axioms GlideKernel.verticalDigammaReal_neg
#print axioms Complex.GammaSeq_tendstoLocallyUniformlyOn_re_pos
#print axioms Complex.hasDerivAt_digamma
#print axioms Complex.digamma_sub_eq_tsum
#print axioms Complex.digamma_eq_neg_eulerMascheroniConstant_add_tsum
#print axioms GlideKernel.verticalDigammaReal_sub_zero_eq_gaussVerticalKernel_integral
#print axioms GlideKernel.verticalDigammaReal_log_lower
#print axioms GlideKernel.verticalDigammaReal_log_upper
