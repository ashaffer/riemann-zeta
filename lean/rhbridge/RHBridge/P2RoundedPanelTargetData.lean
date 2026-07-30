/- Generated base constants for p=2 rounded panel checkpoints. -/
import RHBridge.P2EntryCertificate

namespace RHP2Bridge.P2RoundedPanelTargetData

def panelIntegralScale : Nat := 10 ^ 40

/-- Per-panel coarse radius.  The 32-panel total is `3.2e-17`, well below
the aggregate certificate allowance `10^-15`. -/
def panelAllowanceQ : ℚ := 1 / 10 ^ 18

end RHP2Bridge.P2RoundedPanelTargetData
