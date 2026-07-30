import RHBridge.P2RoundedFactorCheckpointData20

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel20FactorChunk4 :
    P2RoundedFactorCheckpointData.panel20Prefix16 =
      normalizedPrefixTermAtomApprox ⟨16, by decide⟩ ⟨20, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel20Prefix17 =
      normalizedPrefixTermAtomApprox ⟨17, by decide⟩ ⟨20, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel20Prefix18 =
      normalizedPrefixTermAtomApprox ⟨18, by decide⟩ ⟨20, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel20Prefix19 =
      normalizedPrefixTermAtomApprox ⟨19, by decide⟩ ⟨20, by decide⟩ := by
  decide +kernel

theorem panel20Prefix16_eq :
    P2RoundedFactorCheckpointData.panel20Prefix16 =
      normalizedPrefixTermAtomApprox ⟨16, by decide⟩ ⟨20, by decide⟩ := by
  exact panel20FactorChunk4.1

theorem panel20Prefix17_eq :
    P2RoundedFactorCheckpointData.panel20Prefix17 =
      normalizedPrefixTermAtomApprox ⟨17, by decide⟩ ⟨20, by decide⟩ := by
  exact panel20FactorChunk4.2.1

theorem panel20Prefix18_eq :
    P2RoundedFactorCheckpointData.panel20Prefix18 =
      normalizedPrefixTermAtomApprox ⟨18, by decide⟩ ⟨20, by decide⟩ := by
  exact panel20FactorChunk4.2.2.1

theorem panel20Prefix19_eq :
    P2RoundedFactorCheckpointData.panel20Prefix19 =
      normalizedPrefixTermAtomApprox ⟨19, by decide⟩ ⟨20, by decide⟩ := by
  exact panel20FactorChunk4.2.2.2

end RHP2Bridge
