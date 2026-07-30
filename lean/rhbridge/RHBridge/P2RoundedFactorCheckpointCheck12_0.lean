import RHBridge.P2RoundedFactorCheckpointData12

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel12FactorChunk0 :
    P2RoundedFactorCheckpointData.panel12Prefix0 =
      normalizedPrefixTermAtomApprox ⟨0, by decide⟩ ⟨12, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel12Prefix1 =
      normalizedPrefixTermAtomApprox ⟨1, by decide⟩ ⟨12, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel12Prefix2 =
      normalizedPrefixTermAtomApprox ⟨2, by decide⟩ ⟨12, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel12Prefix3 =
      normalizedPrefixTermAtomApprox ⟨3, by decide⟩ ⟨12, by decide⟩ := by
  decide +kernel

theorem panel12Prefix0_eq :
    P2RoundedFactorCheckpointData.panel12Prefix0 =
      normalizedPrefixTermAtomApprox ⟨0, by decide⟩ ⟨12, by decide⟩ := by
  exact panel12FactorChunk0.1

theorem panel12Prefix1_eq :
    P2RoundedFactorCheckpointData.panel12Prefix1 =
      normalizedPrefixTermAtomApprox ⟨1, by decide⟩ ⟨12, by decide⟩ := by
  exact panel12FactorChunk0.2.1

theorem panel12Prefix2_eq :
    P2RoundedFactorCheckpointData.panel12Prefix2 =
      normalizedPrefixTermAtomApprox ⟨2, by decide⟩ ⟨12, by decide⟩ := by
  exact panel12FactorChunk0.2.2.1

theorem panel12Prefix3_eq :
    P2RoundedFactorCheckpointData.panel12Prefix3 =
      normalizedPrefixTermAtomApprox ⟨3, by decide⟩ ⟨12, by decide⟩ := by
  exact panel12FactorChunk0.2.2.2

end RHP2Bridge
