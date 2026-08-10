import RHBridge.GuinandWeilLiteratureAudit
import RHBridge.WeilCriterionLiteratureAudit
import RHBridge.LocalizationLiteratureAudit
import RHBridge.SuzukiScrewLiteratureAudit
import RHBridge.SuzukiClosedDomainLiteratureAudit
import RHBridge.Stage4CanonicalConstructionLiteratureAudit
import RHBridge.ActivationCancellationAudit
import RHBridge.RelativeFactorObstruction
import RHBridge.R176NecessaryCondition
import RHBridge.FixedWindowStripReduction

/-!
# Consolidated trust-boundary audit

This module is the single audit entry point for load-bearing assumptions used
by the RHBridge development. The imported literature-audit modules print the
axiom dependencies of their public bridge theorems. The project-local modules
below should remain axiom-free except for assumptions explicitly imported
through one of those named boundary modules.
-/

#print axioms RHP2Bridge.RelativeFactorObstruction.exists_pos_factor_mul_le_iff
#print axioms RHP2Bridge.R176NecessaryCondition.savingCoefficient_le_rightArcWeight
#print axioms RHP2Bridge.FixedWindowStripReduction.closedStrip_of_fullFourthMomentExponent
#print axioms RHP2Bridge.FixedWindowStripReduction.criticalLineLocalization_of_allFourthMomentSavings
