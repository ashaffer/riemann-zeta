import RHBridge.P2RoundedFactorCheckpointData25

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel25FactorChunk0 :
    P2RoundedFactorCheckpointData.panel25Prefix0 =
      normalizedPrefixTermAtomApprox ⟨0, by decide⟩ ⟨25, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel25Prefix1 =
      normalizedPrefixTermAtomApprox ⟨1, by decide⟩ ⟨25, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel25Prefix2 =
      normalizedPrefixTermAtomApprox ⟨2, by decide⟩ ⟨25, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel25Prefix3 =
      normalizedPrefixTermAtomApprox ⟨3, by decide⟩ ⟨25, by decide⟩ := by
  decide +kernel

theorem panel25Prefix0_eq :
    P2RoundedFactorCheckpointData.panel25Prefix0 =
      normalizedPrefixTermAtomApprox ⟨0, by decide⟩ ⟨25, by decide⟩ := by
  exact panel25FactorChunk0.1

theorem panel25Prefix1_eq :
    P2RoundedFactorCheckpointData.panel25Prefix1 =
      normalizedPrefixTermAtomApprox ⟨1, by decide⟩ ⟨25, by decide⟩ := by
  exact panel25FactorChunk0.2.1

theorem panel25Prefix2_eq :
    P2RoundedFactorCheckpointData.panel25Prefix2 =
      normalizedPrefixTermAtomApprox ⟨2, by decide⟩ ⟨25, by decide⟩ := by
  exact panel25FactorChunk0.2.2.1

theorem panel25Prefix3_eq :
    P2RoundedFactorCheckpointData.panel25Prefix3 =
      normalizedPrefixTermAtomApprox ⟨3, by decide⟩ ⟨25, by decide⟩ := by
  exact panel25FactorChunk0.2.2.2

end RHP2Bridge
