import RHBridge.P2RoundedFactorCheckpointData5

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel5FactorChunk0 :
    P2RoundedFactorCheckpointData.panel5Prefix0 =
      normalizedPrefixTermAtomApprox ⟨0, by decide⟩ ⟨5, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel5Prefix1 =
      normalizedPrefixTermAtomApprox ⟨1, by decide⟩ ⟨5, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel5Prefix2 =
      normalizedPrefixTermAtomApprox ⟨2, by decide⟩ ⟨5, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel5Prefix3 =
      normalizedPrefixTermAtomApprox ⟨3, by decide⟩ ⟨5, by decide⟩ := by
  decide +kernel

theorem panel5Prefix0_eq :
    P2RoundedFactorCheckpointData.panel5Prefix0 =
      normalizedPrefixTermAtomApprox ⟨0, by decide⟩ ⟨5, by decide⟩ := by
  exact panel5FactorChunk0.1

theorem panel5Prefix1_eq :
    P2RoundedFactorCheckpointData.panel5Prefix1 =
      normalizedPrefixTermAtomApprox ⟨1, by decide⟩ ⟨5, by decide⟩ := by
  exact panel5FactorChunk0.2.1

theorem panel5Prefix2_eq :
    P2RoundedFactorCheckpointData.panel5Prefix2 =
      normalizedPrefixTermAtomApprox ⟨2, by decide⟩ ⟨5, by decide⟩ := by
  exact panel5FactorChunk0.2.2.1

theorem panel5Prefix3_eq :
    P2RoundedFactorCheckpointData.panel5Prefix3 =
      normalizedPrefixTermAtomApprox ⟨3, by decide⟩ ⟨5, by decide⟩ := by
  exact panel5FactorChunk0.2.2.2

end RHP2Bridge
