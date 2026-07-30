import RHBridge.P2RoundedFactorCheckpointData3

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel3FactorChunk5 :
    P2RoundedFactorCheckpointData.panel3Prefix20 =
      normalizedPrefixTermAtomApprox ⟨20, by decide⟩ ⟨3, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel3Prefix21 =
      normalizedPrefixTermAtomApprox ⟨21, by decide⟩ ⟨3, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel3Prefix22 =
      normalizedPrefixTermAtomApprox ⟨22, by decide⟩ ⟨3, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel3Prefix23 =
      normalizedPrefixTermAtomApprox ⟨23, by decide⟩ ⟨3, by decide⟩ := by
  decide +kernel

theorem panel3Prefix20_eq :
    P2RoundedFactorCheckpointData.panel3Prefix20 =
      normalizedPrefixTermAtomApprox ⟨20, by decide⟩ ⟨3, by decide⟩ := by
  exact panel3FactorChunk5.1

theorem panel3Prefix21_eq :
    P2RoundedFactorCheckpointData.panel3Prefix21 =
      normalizedPrefixTermAtomApprox ⟨21, by decide⟩ ⟨3, by decide⟩ := by
  exact panel3FactorChunk5.2.1

theorem panel3Prefix22_eq :
    P2RoundedFactorCheckpointData.panel3Prefix22 =
      normalizedPrefixTermAtomApprox ⟨22, by decide⟩ ⟨3, by decide⟩ := by
  exact panel3FactorChunk5.2.2.1

theorem panel3Prefix23_eq :
    P2RoundedFactorCheckpointData.panel3Prefix23 =
      normalizedPrefixTermAtomApprox ⟨23, by decide⟩ ⟨3, by decide⟩ := by
  exact panel3FactorChunk5.2.2.2

end RHP2Bridge
