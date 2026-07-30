import RHBridge.P2RoundedFactorCheckpointData0

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel0FactorChunk0 :
    P2RoundedFactorCheckpointData.panel0Prefix0 =
      normalizedPrefixTermAtomApprox ⟨0, by decide⟩ ⟨0, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel0Prefix1 =
      normalizedPrefixTermAtomApprox ⟨1, by decide⟩ ⟨0, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel0Prefix2 =
      normalizedPrefixTermAtomApprox ⟨2, by decide⟩ ⟨0, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel0Prefix3 =
      normalizedPrefixTermAtomApprox ⟨3, by decide⟩ ⟨0, by decide⟩ := by
  decide +kernel

theorem panel0Prefix0_eq :
    P2RoundedFactorCheckpointData.panel0Prefix0 =
      normalizedPrefixTermAtomApprox ⟨0, by decide⟩ ⟨0, by decide⟩ := by
  exact panel0FactorChunk0.1

theorem panel0Prefix1_eq :
    P2RoundedFactorCheckpointData.panel0Prefix1 =
      normalizedPrefixTermAtomApprox ⟨1, by decide⟩ ⟨0, by decide⟩ := by
  exact panel0FactorChunk0.2.1

theorem panel0Prefix2_eq :
    P2RoundedFactorCheckpointData.panel0Prefix2 =
      normalizedPrefixTermAtomApprox ⟨2, by decide⟩ ⟨0, by decide⟩ := by
  exact panel0FactorChunk0.2.2.1

theorem panel0Prefix3_eq :
    P2RoundedFactorCheckpointData.panel0Prefix3 =
      normalizedPrefixTermAtomApprox ⟨3, by decide⟩ ⟨0, by decide⟩ := by
  exact panel0FactorChunk0.2.2.2

end RHP2Bridge
