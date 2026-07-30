import RHBridge.P2RoundedFactorCheckpointData3

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel3FactorChunk0 :
    P2RoundedFactorCheckpointData.panel3Prefix0 =
      normalizedPrefixTermAtomApprox ⟨0, by decide⟩ ⟨3, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel3Prefix1 =
      normalizedPrefixTermAtomApprox ⟨1, by decide⟩ ⟨3, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel3Prefix2 =
      normalizedPrefixTermAtomApprox ⟨2, by decide⟩ ⟨3, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel3Prefix3 =
      normalizedPrefixTermAtomApprox ⟨3, by decide⟩ ⟨3, by decide⟩ := by
  decide +kernel

theorem panel3Prefix0_eq :
    P2RoundedFactorCheckpointData.panel3Prefix0 =
      normalizedPrefixTermAtomApprox ⟨0, by decide⟩ ⟨3, by decide⟩ := by
  exact panel3FactorChunk0.1

theorem panel3Prefix1_eq :
    P2RoundedFactorCheckpointData.panel3Prefix1 =
      normalizedPrefixTermAtomApprox ⟨1, by decide⟩ ⟨3, by decide⟩ := by
  exact panel3FactorChunk0.2.1

theorem panel3Prefix2_eq :
    P2RoundedFactorCheckpointData.panel3Prefix2 =
      normalizedPrefixTermAtomApprox ⟨2, by decide⟩ ⟨3, by decide⟩ := by
  exact panel3FactorChunk0.2.2.1

theorem panel3Prefix3_eq :
    P2RoundedFactorCheckpointData.panel3Prefix3 =
      normalizedPrefixTermAtomApprox ⟨3, by decide⟩ ⟨3, by decide⟩ := by
  exact panel3FactorChunk0.2.2.2

end RHP2Bridge
