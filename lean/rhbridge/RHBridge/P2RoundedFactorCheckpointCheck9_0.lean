import RHBridge.P2RoundedFactorCheckpointData9

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel9FactorChunk0 :
    P2RoundedFactorCheckpointData.panel9Prefix0 =
      normalizedPrefixTermAtomApprox ⟨0, by decide⟩ ⟨9, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel9Prefix1 =
      normalizedPrefixTermAtomApprox ⟨1, by decide⟩ ⟨9, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel9Prefix2 =
      normalizedPrefixTermAtomApprox ⟨2, by decide⟩ ⟨9, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel9Prefix3 =
      normalizedPrefixTermAtomApprox ⟨3, by decide⟩ ⟨9, by decide⟩ := by
  decide +kernel

theorem panel9Prefix0_eq :
    P2RoundedFactorCheckpointData.panel9Prefix0 =
      normalizedPrefixTermAtomApprox ⟨0, by decide⟩ ⟨9, by decide⟩ := by
  exact panel9FactorChunk0.1

theorem panel9Prefix1_eq :
    P2RoundedFactorCheckpointData.panel9Prefix1 =
      normalizedPrefixTermAtomApprox ⟨1, by decide⟩ ⟨9, by decide⟩ := by
  exact panel9FactorChunk0.2.1

theorem panel9Prefix2_eq :
    P2RoundedFactorCheckpointData.panel9Prefix2 =
      normalizedPrefixTermAtomApprox ⟨2, by decide⟩ ⟨9, by decide⟩ := by
  exact panel9FactorChunk0.2.2.1

theorem panel9Prefix3_eq :
    P2RoundedFactorCheckpointData.panel9Prefix3 =
      normalizedPrefixTermAtomApprox ⟨3, by decide⟩ ⟨9, by decide⟩ := by
  exact panel9FactorChunk0.2.2.2

end RHP2Bridge
