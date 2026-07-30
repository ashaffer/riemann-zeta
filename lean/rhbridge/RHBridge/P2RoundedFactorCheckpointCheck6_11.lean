import RHBridge.P2RoundedFactorCheckpointData6

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel6FactorChunk11 :
    P2RoundedFactorCheckpointData.panel6Prefix44 =
      normalizedPrefixTermAtomApprox ⟨44, by decide⟩ ⟨6, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel6Prefix45 =
      normalizedPrefixTermAtomApprox ⟨45, by decide⟩ ⟨6, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel6Prefix46 =
      normalizedPrefixTermAtomApprox ⟨46, by decide⟩ ⟨6, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel6Prefix47 =
      normalizedPrefixTermAtomApprox ⟨47, by decide⟩ ⟨6, by decide⟩ := by
  decide +kernel

theorem panel6Prefix44_eq :
    P2RoundedFactorCheckpointData.panel6Prefix44 =
      normalizedPrefixTermAtomApprox ⟨44, by decide⟩ ⟨6, by decide⟩ := by
  exact panel6FactorChunk11.1

theorem panel6Prefix45_eq :
    P2RoundedFactorCheckpointData.panel6Prefix45 =
      normalizedPrefixTermAtomApprox ⟨45, by decide⟩ ⟨6, by decide⟩ := by
  exact panel6FactorChunk11.2.1

theorem panel6Prefix46_eq :
    P2RoundedFactorCheckpointData.panel6Prefix46 =
      normalizedPrefixTermAtomApprox ⟨46, by decide⟩ ⟨6, by decide⟩ := by
  exact panel6FactorChunk11.2.2.1

theorem panel6Prefix47_eq :
    P2RoundedFactorCheckpointData.panel6Prefix47 =
      normalizedPrefixTermAtomApprox ⟨47, by decide⟩ ⟨6, by decide⟩ := by
  exact panel6FactorChunk11.2.2.2

end RHP2Bridge
