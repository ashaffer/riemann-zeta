import RHBridge.P2RoundedFactorCheckpointData28

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel28FactorChunk11 :
    P2RoundedFactorCheckpointData.panel28Prefix44 =
      normalizedPrefixTermAtomApprox ⟨44, by decide⟩ ⟨28, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel28Prefix45 =
      normalizedPrefixTermAtomApprox ⟨45, by decide⟩ ⟨28, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel28Prefix46 =
      normalizedPrefixTermAtomApprox ⟨46, by decide⟩ ⟨28, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel28Prefix47 =
      normalizedPrefixTermAtomApprox ⟨47, by decide⟩ ⟨28, by decide⟩ := by
  decide +kernel

theorem panel28Prefix44_eq :
    P2RoundedFactorCheckpointData.panel28Prefix44 =
      normalizedPrefixTermAtomApprox ⟨44, by decide⟩ ⟨28, by decide⟩ := by
  exact panel28FactorChunk11.1

theorem panel28Prefix45_eq :
    P2RoundedFactorCheckpointData.panel28Prefix45 =
      normalizedPrefixTermAtomApprox ⟨45, by decide⟩ ⟨28, by decide⟩ := by
  exact panel28FactorChunk11.2.1

theorem panel28Prefix46_eq :
    P2RoundedFactorCheckpointData.panel28Prefix46 =
      normalizedPrefixTermAtomApprox ⟨46, by decide⟩ ⟨28, by decide⟩ := by
  exact panel28FactorChunk11.2.2.1

theorem panel28Prefix47_eq :
    P2RoundedFactorCheckpointData.panel28Prefix47 =
      normalizedPrefixTermAtomApprox ⟨47, by decide⟩ ⟨28, by decide⟩ := by
  exact panel28FactorChunk11.2.2.2

end RHP2Bridge
