import RHBridge.P2RoundedFactorCheckpointData17

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel17FactorChunk11 :
    P2RoundedFactorCheckpointData.panel17Prefix44 =
      normalizedPrefixTermAtomApprox ⟨44, by decide⟩ ⟨17, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel17Prefix45 =
      normalizedPrefixTermAtomApprox ⟨45, by decide⟩ ⟨17, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel17Prefix46 =
      normalizedPrefixTermAtomApprox ⟨46, by decide⟩ ⟨17, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel17Prefix47 =
      normalizedPrefixTermAtomApprox ⟨47, by decide⟩ ⟨17, by decide⟩ := by
  decide +kernel

theorem panel17Prefix44_eq :
    P2RoundedFactorCheckpointData.panel17Prefix44 =
      normalizedPrefixTermAtomApprox ⟨44, by decide⟩ ⟨17, by decide⟩ := by
  exact panel17FactorChunk11.1

theorem panel17Prefix45_eq :
    P2RoundedFactorCheckpointData.panel17Prefix45 =
      normalizedPrefixTermAtomApprox ⟨45, by decide⟩ ⟨17, by decide⟩ := by
  exact panel17FactorChunk11.2.1

theorem panel17Prefix46_eq :
    P2RoundedFactorCheckpointData.panel17Prefix46 =
      normalizedPrefixTermAtomApprox ⟨46, by decide⟩ ⟨17, by decide⟩ := by
  exact panel17FactorChunk11.2.2.1

theorem panel17Prefix47_eq :
    P2RoundedFactorCheckpointData.panel17Prefix47 =
      normalizedPrefixTermAtomApprox ⟨47, by decide⟩ ⟨17, by decide⟩ := by
  exact panel17FactorChunk11.2.2.2

end RHP2Bridge
