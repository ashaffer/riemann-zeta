import RHBridge.P2RoundedFactorCheckpointData8

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel8FactorChunk11 :
    P2RoundedFactorCheckpointData.panel8Prefix44 =
      normalizedPrefixTermAtomApprox ⟨44, by decide⟩ ⟨8, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel8Prefix45 =
      normalizedPrefixTermAtomApprox ⟨45, by decide⟩ ⟨8, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel8Prefix46 =
      normalizedPrefixTermAtomApprox ⟨46, by decide⟩ ⟨8, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel8Prefix47 =
      normalizedPrefixTermAtomApprox ⟨47, by decide⟩ ⟨8, by decide⟩ := by
  decide +kernel

theorem panel8Prefix44_eq :
    P2RoundedFactorCheckpointData.panel8Prefix44 =
      normalizedPrefixTermAtomApprox ⟨44, by decide⟩ ⟨8, by decide⟩ := by
  exact panel8FactorChunk11.1

theorem panel8Prefix45_eq :
    P2RoundedFactorCheckpointData.panel8Prefix45 =
      normalizedPrefixTermAtomApprox ⟨45, by decide⟩ ⟨8, by decide⟩ := by
  exact panel8FactorChunk11.2.1

theorem panel8Prefix46_eq :
    P2RoundedFactorCheckpointData.panel8Prefix46 =
      normalizedPrefixTermAtomApprox ⟨46, by decide⟩ ⟨8, by decide⟩ := by
  exact panel8FactorChunk11.2.2.1

theorem panel8Prefix47_eq :
    P2RoundedFactorCheckpointData.panel8Prefix47 =
      normalizedPrefixTermAtomApprox ⟨47, by decide⟩ ⟨8, by decide⟩ := by
  exact panel8FactorChunk11.2.2.2

end RHP2Bridge
