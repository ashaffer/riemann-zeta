import RHBridge.P2RoundedFactorCheckpointData23

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel23FactorChunk0 :
    P2RoundedFactorCheckpointData.panel23Prefix0 =
      normalizedPrefixTermAtomApprox ⟨0, by decide⟩ ⟨23, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel23Prefix1 =
      normalizedPrefixTermAtomApprox ⟨1, by decide⟩ ⟨23, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel23Prefix2 =
      normalizedPrefixTermAtomApprox ⟨2, by decide⟩ ⟨23, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel23Prefix3 =
      normalizedPrefixTermAtomApprox ⟨3, by decide⟩ ⟨23, by decide⟩ := by
  decide +kernel

theorem panel23Prefix0_eq :
    P2RoundedFactorCheckpointData.panel23Prefix0 =
      normalizedPrefixTermAtomApprox ⟨0, by decide⟩ ⟨23, by decide⟩ := by
  exact panel23FactorChunk0.1

theorem panel23Prefix1_eq :
    P2RoundedFactorCheckpointData.panel23Prefix1 =
      normalizedPrefixTermAtomApprox ⟨1, by decide⟩ ⟨23, by decide⟩ := by
  exact panel23FactorChunk0.2.1

theorem panel23Prefix2_eq :
    P2RoundedFactorCheckpointData.panel23Prefix2 =
      normalizedPrefixTermAtomApprox ⟨2, by decide⟩ ⟨23, by decide⟩ := by
  exact panel23FactorChunk0.2.2.1

theorem panel23Prefix3_eq :
    P2RoundedFactorCheckpointData.panel23Prefix3 =
      normalizedPrefixTermAtomApprox ⟨3, by decide⟩ ⟨23, by decide⟩ := by
  exact panel23FactorChunk0.2.2.2

end RHP2Bridge
