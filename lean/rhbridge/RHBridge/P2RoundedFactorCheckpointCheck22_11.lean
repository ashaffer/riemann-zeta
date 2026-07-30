import RHBridge.P2RoundedFactorCheckpointData22

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel22FactorChunk11 :
    P2RoundedFactorCheckpointData.panel22Prefix44 =
      normalizedPrefixTermAtomApprox ⟨44, by decide⟩ ⟨22, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel22Prefix45 =
      normalizedPrefixTermAtomApprox ⟨45, by decide⟩ ⟨22, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel22Prefix46 =
      normalizedPrefixTermAtomApprox ⟨46, by decide⟩ ⟨22, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel22Prefix47 =
      normalizedPrefixTermAtomApprox ⟨47, by decide⟩ ⟨22, by decide⟩ := by
  decide +kernel

theorem panel22Prefix44_eq :
    P2RoundedFactorCheckpointData.panel22Prefix44 =
      normalizedPrefixTermAtomApprox ⟨44, by decide⟩ ⟨22, by decide⟩ := by
  exact panel22FactorChunk11.1

theorem panel22Prefix45_eq :
    P2RoundedFactorCheckpointData.panel22Prefix45 =
      normalizedPrefixTermAtomApprox ⟨45, by decide⟩ ⟨22, by decide⟩ := by
  exact panel22FactorChunk11.2.1

theorem panel22Prefix46_eq :
    P2RoundedFactorCheckpointData.panel22Prefix46 =
      normalizedPrefixTermAtomApprox ⟨46, by decide⟩ ⟨22, by decide⟩ := by
  exact panel22FactorChunk11.2.2.1

theorem panel22Prefix47_eq :
    P2RoundedFactorCheckpointData.panel22Prefix47 =
      normalizedPrefixTermAtomApprox ⟨47, by decide⟩ ⟨22, by decide⟩ := by
  exact panel22FactorChunk11.2.2.2

end RHP2Bridge
