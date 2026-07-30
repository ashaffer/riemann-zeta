import RHBridge.P2RoundedFactorCheckpointData10

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel10FactorChunk11 :
    P2RoundedFactorCheckpointData.panel10Prefix44 =
      normalizedPrefixTermAtomApprox ⟨44, by decide⟩ ⟨10, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel10Prefix45 =
      normalizedPrefixTermAtomApprox ⟨45, by decide⟩ ⟨10, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel10Prefix46 =
      normalizedPrefixTermAtomApprox ⟨46, by decide⟩ ⟨10, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel10Prefix47 =
      normalizedPrefixTermAtomApprox ⟨47, by decide⟩ ⟨10, by decide⟩ := by
  decide +kernel

theorem panel10Prefix44_eq :
    P2RoundedFactorCheckpointData.panel10Prefix44 =
      normalizedPrefixTermAtomApprox ⟨44, by decide⟩ ⟨10, by decide⟩ := by
  exact panel10FactorChunk11.1

theorem panel10Prefix45_eq :
    P2RoundedFactorCheckpointData.panel10Prefix45 =
      normalizedPrefixTermAtomApprox ⟨45, by decide⟩ ⟨10, by decide⟩ := by
  exact panel10FactorChunk11.2.1

theorem panel10Prefix46_eq :
    P2RoundedFactorCheckpointData.panel10Prefix46 =
      normalizedPrefixTermAtomApprox ⟨46, by decide⟩ ⟨10, by decide⟩ := by
  exact panel10FactorChunk11.2.2.1

theorem panel10Prefix47_eq :
    P2RoundedFactorCheckpointData.panel10Prefix47 =
      normalizedPrefixTermAtomApprox ⟨47, by decide⟩ ⟨10, by decide⟩ := by
  exact panel10FactorChunk11.2.2.2

end RHP2Bridge
