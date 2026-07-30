import RHBridge.P2RoundedFactorCheckpointData14

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel14FactorChunk11 :
    P2RoundedFactorCheckpointData.panel14Prefix44 =
      normalizedPrefixTermAtomApprox ⟨44, by decide⟩ ⟨14, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel14Prefix45 =
      normalizedPrefixTermAtomApprox ⟨45, by decide⟩ ⟨14, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel14Prefix46 =
      normalizedPrefixTermAtomApprox ⟨46, by decide⟩ ⟨14, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel14Prefix47 =
      normalizedPrefixTermAtomApprox ⟨47, by decide⟩ ⟨14, by decide⟩ := by
  decide +kernel

theorem panel14Prefix44_eq :
    P2RoundedFactorCheckpointData.panel14Prefix44 =
      normalizedPrefixTermAtomApprox ⟨44, by decide⟩ ⟨14, by decide⟩ := by
  exact panel14FactorChunk11.1

theorem panel14Prefix45_eq :
    P2RoundedFactorCheckpointData.panel14Prefix45 =
      normalizedPrefixTermAtomApprox ⟨45, by decide⟩ ⟨14, by decide⟩ := by
  exact panel14FactorChunk11.2.1

theorem panel14Prefix46_eq :
    P2RoundedFactorCheckpointData.panel14Prefix46 =
      normalizedPrefixTermAtomApprox ⟨46, by decide⟩ ⟨14, by decide⟩ := by
  exact panel14FactorChunk11.2.2.1

theorem panel14Prefix47_eq :
    P2RoundedFactorCheckpointData.panel14Prefix47 =
      normalizedPrefixTermAtomApprox ⟨47, by decide⟩ ⟨14, by decide⟩ := by
  exact panel14FactorChunk11.2.2.2

end RHP2Bridge
