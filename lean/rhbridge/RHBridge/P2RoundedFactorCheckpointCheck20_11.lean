import RHBridge.P2RoundedFactorCheckpointData20

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel20FactorChunk11 :
    P2RoundedFactorCheckpointData.panel20Prefix44 =
      normalizedPrefixTermAtomApprox ⟨44, by decide⟩ ⟨20, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel20Prefix45 =
      normalizedPrefixTermAtomApprox ⟨45, by decide⟩ ⟨20, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel20Prefix46 =
      normalizedPrefixTermAtomApprox ⟨46, by decide⟩ ⟨20, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel20Prefix47 =
      normalizedPrefixTermAtomApprox ⟨47, by decide⟩ ⟨20, by decide⟩ := by
  decide +kernel

theorem panel20Prefix44_eq :
    P2RoundedFactorCheckpointData.panel20Prefix44 =
      normalizedPrefixTermAtomApprox ⟨44, by decide⟩ ⟨20, by decide⟩ := by
  exact panel20FactorChunk11.1

theorem panel20Prefix45_eq :
    P2RoundedFactorCheckpointData.panel20Prefix45 =
      normalizedPrefixTermAtomApprox ⟨45, by decide⟩ ⟨20, by decide⟩ := by
  exact panel20FactorChunk11.2.1

theorem panel20Prefix46_eq :
    P2RoundedFactorCheckpointData.panel20Prefix46 =
      normalizedPrefixTermAtomApprox ⟨46, by decide⟩ ⟨20, by decide⟩ := by
  exact panel20FactorChunk11.2.2.1

theorem panel20Prefix47_eq :
    P2RoundedFactorCheckpointData.panel20Prefix47 =
      normalizedPrefixTermAtomApprox ⟨47, by decide⟩ ⟨20, by decide⟩ := by
  exact panel20FactorChunk11.2.2.2

end RHP2Bridge
