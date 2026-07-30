import RHBridge.P2RoundedFactorCheckpointData2

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel2FactorChunk11 :
    P2RoundedFactorCheckpointData.panel2Prefix44 =
      normalizedPrefixTermAtomApprox ⟨44, by decide⟩ ⟨2, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel2Prefix45 =
      normalizedPrefixTermAtomApprox ⟨45, by decide⟩ ⟨2, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel2Prefix46 =
      normalizedPrefixTermAtomApprox ⟨46, by decide⟩ ⟨2, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel2Prefix47 =
      normalizedPrefixTermAtomApprox ⟨47, by decide⟩ ⟨2, by decide⟩ := by
  decide +kernel

theorem panel2Prefix44_eq :
    P2RoundedFactorCheckpointData.panel2Prefix44 =
      normalizedPrefixTermAtomApprox ⟨44, by decide⟩ ⟨2, by decide⟩ := by
  exact panel2FactorChunk11.1

theorem panel2Prefix45_eq :
    P2RoundedFactorCheckpointData.panel2Prefix45 =
      normalizedPrefixTermAtomApprox ⟨45, by decide⟩ ⟨2, by decide⟩ := by
  exact panel2FactorChunk11.2.1

theorem panel2Prefix46_eq :
    P2RoundedFactorCheckpointData.panel2Prefix46 =
      normalizedPrefixTermAtomApprox ⟨46, by decide⟩ ⟨2, by decide⟩ := by
  exact panel2FactorChunk11.2.2.1

theorem panel2Prefix47_eq :
    P2RoundedFactorCheckpointData.panel2Prefix47 =
      normalizedPrefixTermAtomApprox ⟨47, by decide⟩ ⟨2, by decide⟩ := by
  exact panel2FactorChunk11.2.2.2

end RHP2Bridge
