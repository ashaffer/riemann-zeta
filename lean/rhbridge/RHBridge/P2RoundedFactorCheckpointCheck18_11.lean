import RHBridge.P2RoundedFactorCheckpointData18

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel18FactorChunk11 :
    P2RoundedFactorCheckpointData.panel18Prefix44 =
      normalizedPrefixTermAtomApprox ⟨44, by decide⟩ ⟨18, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel18Prefix45 =
      normalizedPrefixTermAtomApprox ⟨45, by decide⟩ ⟨18, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel18Prefix46 =
      normalizedPrefixTermAtomApprox ⟨46, by decide⟩ ⟨18, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel18Prefix47 =
      normalizedPrefixTermAtomApprox ⟨47, by decide⟩ ⟨18, by decide⟩ := by
  decide +kernel

theorem panel18Prefix44_eq :
    P2RoundedFactorCheckpointData.panel18Prefix44 =
      normalizedPrefixTermAtomApprox ⟨44, by decide⟩ ⟨18, by decide⟩ := by
  exact panel18FactorChunk11.1

theorem panel18Prefix45_eq :
    P2RoundedFactorCheckpointData.panel18Prefix45 =
      normalizedPrefixTermAtomApprox ⟨45, by decide⟩ ⟨18, by decide⟩ := by
  exact panel18FactorChunk11.2.1

theorem panel18Prefix46_eq :
    P2RoundedFactorCheckpointData.panel18Prefix46 =
      normalizedPrefixTermAtomApprox ⟨46, by decide⟩ ⟨18, by decide⟩ := by
  exact panel18FactorChunk11.2.2.1

theorem panel18Prefix47_eq :
    P2RoundedFactorCheckpointData.panel18Prefix47 =
      normalizedPrefixTermAtomApprox ⟨47, by decide⟩ ⟨18, by decide⟩ := by
  exact panel18FactorChunk11.2.2.2

end RHP2Bridge
