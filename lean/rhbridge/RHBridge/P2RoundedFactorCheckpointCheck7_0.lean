import RHBridge.P2RoundedFactorCheckpointData7

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel7FactorChunk0 :
    P2RoundedFactorCheckpointData.panel7Prefix0 =
      normalizedPrefixTermAtomApprox ⟨0, by decide⟩ ⟨7, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel7Prefix1 =
      normalizedPrefixTermAtomApprox ⟨1, by decide⟩ ⟨7, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel7Prefix2 =
      normalizedPrefixTermAtomApprox ⟨2, by decide⟩ ⟨7, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel7Prefix3 =
      normalizedPrefixTermAtomApprox ⟨3, by decide⟩ ⟨7, by decide⟩ := by
  decide +kernel

theorem panel7Prefix0_eq :
    P2RoundedFactorCheckpointData.panel7Prefix0 =
      normalizedPrefixTermAtomApprox ⟨0, by decide⟩ ⟨7, by decide⟩ := by
  exact panel7FactorChunk0.1

theorem panel7Prefix1_eq :
    P2RoundedFactorCheckpointData.panel7Prefix1 =
      normalizedPrefixTermAtomApprox ⟨1, by decide⟩ ⟨7, by decide⟩ := by
  exact panel7FactorChunk0.2.1

theorem panel7Prefix2_eq :
    P2RoundedFactorCheckpointData.panel7Prefix2 =
      normalizedPrefixTermAtomApprox ⟨2, by decide⟩ ⟨7, by decide⟩ := by
  exact panel7FactorChunk0.2.2.1

theorem panel7Prefix3_eq :
    P2RoundedFactorCheckpointData.panel7Prefix3 =
      normalizedPrefixTermAtomApprox ⟨3, by decide⟩ ⟨7, by decide⟩ := by
  exact panel7FactorChunk0.2.2.2

end RHP2Bridge
