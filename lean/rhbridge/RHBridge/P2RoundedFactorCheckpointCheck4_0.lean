import RHBridge.P2RoundedFactorCheckpointData4

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel4FactorChunk0 :
    P2RoundedFactorCheckpointData.panel4Prefix0 =
      normalizedPrefixTermAtomApprox ⟨0, by decide⟩ ⟨4, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel4Prefix1 =
      normalizedPrefixTermAtomApprox ⟨1, by decide⟩ ⟨4, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel4Prefix2 =
      normalizedPrefixTermAtomApprox ⟨2, by decide⟩ ⟨4, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel4Prefix3 =
      normalizedPrefixTermAtomApprox ⟨3, by decide⟩ ⟨4, by decide⟩ := by
  decide +kernel

theorem panel4Prefix0_eq :
    P2RoundedFactorCheckpointData.panel4Prefix0 =
      normalizedPrefixTermAtomApprox ⟨0, by decide⟩ ⟨4, by decide⟩ := by
  exact panel4FactorChunk0.1

theorem panel4Prefix1_eq :
    P2RoundedFactorCheckpointData.panel4Prefix1 =
      normalizedPrefixTermAtomApprox ⟨1, by decide⟩ ⟨4, by decide⟩ := by
  exact panel4FactorChunk0.2.1

theorem panel4Prefix2_eq :
    P2RoundedFactorCheckpointData.panel4Prefix2 =
      normalizedPrefixTermAtomApprox ⟨2, by decide⟩ ⟨4, by decide⟩ := by
  exact panel4FactorChunk0.2.2.1

theorem panel4Prefix3_eq :
    P2RoundedFactorCheckpointData.panel4Prefix3 =
      normalizedPrefixTermAtomApprox ⟨3, by decide⟩ ⟨4, by decide⟩ := by
  exact panel4FactorChunk0.2.2.2

end RHP2Bridge
