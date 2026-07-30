import RHBridge.P2RoundedFactorCheckpointData10

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel10FactorChunk0 :
    P2RoundedFactorCheckpointData.panel10Prefix0 =
      normalizedPrefixTermAtomApprox ⟨0, by decide⟩ ⟨10, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel10Prefix1 =
      normalizedPrefixTermAtomApprox ⟨1, by decide⟩ ⟨10, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel10Prefix2 =
      normalizedPrefixTermAtomApprox ⟨2, by decide⟩ ⟨10, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel10Prefix3 =
      normalizedPrefixTermAtomApprox ⟨3, by decide⟩ ⟨10, by decide⟩ := by
  decide +kernel

theorem panel10Prefix0_eq :
    P2RoundedFactorCheckpointData.panel10Prefix0 =
      normalizedPrefixTermAtomApprox ⟨0, by decide⟩ ⟨10, by decide⟩ := by
  exact panel10FactorChunk0.1

theorem panel10Prefix1_eq :
    P2RoundedFactorCheckpointData.panel10Prefix1 =
      normalizedPrefixTermAtomApprox ⟨1, by decide⟩ ⟨10, by decide⟩ := by
  exact panel10FactorChunk0.2.1

theorem panel10Prefix2_eq :
    P2RoundedFactorCheckpointData.panel10Prefix2 =
      normalizedPrefixTermAtomApprox ⟨2, by decide⟩ ⟨10, by decide⟩ := by
  exact panel10FactorChunk0.2.2.1

theorem panel10Prefix3_eq :
    P2RoundedFactorCheckpointData.panel10Prefix3 =
      normalizedPrefixTermAtomApprox ⟨3, by decide⟩ ⟨10, by decide⟩ := by
  exact panel10FactorChunk0.2.2.2

end RHP2Bridge
